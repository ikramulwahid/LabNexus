#!/usr/bin/env python3
import argparse, csv, json, multiprocessing as mp, os, platform, queue, random, shutil, sqlite3, statistics, sys, tempfile, time
from pathlib import Path

try:
    import psutil
except ImportError:
    psutil = None

SIZES = [10, 25, 50, 65, 80]
WRITERS = [1, 3, 5]
REPS = 3
SAMPLES_PER_WRITER = 5
BUSY_TIMEOUT_MS = 5000
RETRY_MAX = 6
RETRY_BASE = 0.005
SAMPLE_COUNT_OVERRIDE = SAMPLES_PER_WRITER

SCHEMA = """
PRAGMA foreign_keys=ON;
CREATE TABLE sample (
    id INTEGER PRIMARY KEY,
    writer_id INTEGER NOT NULL,
    name TEXT NOT NULL UNIQUE
);
CREATE TABLE test_instance (
    id INTEGER PRIMARY KEY,
    sample_id INTEGER NOT NULL REFERENCES sample(id),
    test_no INTEGER NOT NULL,
    status TEXT NOT NULL,
    UNIQUE(sample_id, test_no)
);
CREATE TABLE observation (
    id INTEGER PRIMARY KEY,
    test_instance_id INTEGER NOT NULL REFERENCES test_instance(id),
    value_text TEXT NOT NULL
);
CREATE TABLE result (
    id INTEGER PRIMARY KEY,
    test_instance_id INTEGER NOT NULL REFERENCES test_instance(id),
    value_text TEXT NOT NULL,
    UNIQUE(test_instance_id)
);
CREATE TABLE audit_event (
    id INTEGER PRIMARY KEY,
    entity_type TEXT NOT NULL,
    entity_id INTEGER NOT NULL,
    event_type TEXT NOT NULL,
    actor TEXT NOT NULL,
    created_at REAL NOT NULL
);
CREATE INDEX idx_test_instance_sample ON test_instance(sample_id);
CREATE INDEX idx_observation_test ON observation(test_instance_id);
CREATE INDEX idx_result_test ON result(test_instance_id);
CREATE INDEX idx_audit_entity ON audit_event(entity_type, entity_id);
"""


def conn_open(db):
    con = sqlite3.connect(db, timeout=BUSY_TIMEOUT_MS/1000, isolation_level=None)
    con.execute("PRAGMA foreign_keys=ON")
    con.execute(f"PRAGMA busy_timeout={BUSY_TIMEOUT_MS}")
    con.execute("PRAGMA synchronous=FULL")
    return con


def with_retry(fn, metrics):
    delay = RETRY_BASE
    for attempt in range(RETRY_MAX + 1):
        try:
            return fn()
        except sqlite3.OperationalError as e:
            msg = str(e).lower()
            if "locked" not in msg and "busy" not in msg:
                raise
            if attempt >= RETRY_MAX:
                raise
            metrics["retries"] += 1
            t0 = time.perf_counter()
            time.sleep(delay + random.random() * delay)
            metrics["retry_sleep_s"] += time.perf_counter() - t0
            delay = min(delay * 2, 0.5)


def tx(con, fn, metrics):
    t0 = time.perf_counter()
    def body():
        con.execute("BEGIN IMMEDIATE")
        try:
            fn()
            con.execute("COMMIT")
        except Exception:
            try:
                con.execute("ROLLBACK")
            except Exception:
                pass
            raise
    try:
        with_retry(body, metrics)
        ok = True
    except Exception:
        metrics["errors"] += 1
        ok = False
        raise
    finally:
        metrics["tx_latencies_ms"].append((time.perf_counter()-t0)*1000)
    return ok


def worker(db, writer_id, tests_per_sample, outdir, sample_count, seed):
    rng = random.Random(seed)
    con = conn_open(db)
    metrics = {"retries":0,"errors":0,"retry_sleep_s":0.0,"tx_latencies_ms":[]}
    rows = []
    expected = 0
    try:
        for s in range(sample_count):
            sample_id = writer_id * 1_000_000 + s + 1
            sample_name = f"S-{writer_id}-{s+1}"
            tx(con, lambda sid=sample_id, sn=sample_name: (
                con.execute("INSERT INTO sample(id,writer_id,name) VALUES (?,?,?)", (sid,writer_id,sn)),
                [con.execute("INSERT INTO test_instance(id,sample_id,test_no,status) VALUES (?,?,?,?)", (0,sid,t,'PENDING')) for t in []]
            ), metrics)
            for t in range(1, tests_per_sample+1):
                ti_id = sample_id * 1000 + t
                val = f"{rng.random():.8f}"
                def exec_test(ti=ti_id, sid=sample_id, tn=t, value=val):
                    con.execute("INSERT INTO test_instance(id,sample_id,test_no,status) VALUES (?,?,?,?)", (ti,sid,tn,'EXECUTING'))
                    con.execute("INSERT INTO observation(test_instance_id,value_text) VALUES (?,?)", (ti,value))
                    con.execute("INSERT INTO result(test_instance_id,value_text) VALUES (?,?)", (ti,value))
                    con.execute("UPDATE test_instance SET status='EXECUTED' WHERE id=?", (ti,))
                    con.execute("INSERT INTO audit_event(entity_type,entity_id,event_type,actor,created_at) VALUES (?,?,?,?,?)", ('TEST_INSTANCE',ti,'EXECUTED',f'writer-{writer_id}',time.time()))
                tx(con, exec_test, metrics)
                rows.append({"writer":writer_id,"sample":sample_name,"test_no":t,"stage":"execution"})
                expected += 1
            # Review / verification / approval each as short write transaction.
            for stage, status in (("REVIEW","REVIEWED"),("VERIFICATION","VERIFIED"),("APPROVAL","APPROVED")):
                def control(st=status, sg=stage, sid=sample_id):
                    con.execute("UPDATE test_instance SET status=? WHERE sample_id=?", (st,sid))
                    con.execute("INSERT INTO audit_event(entity_type,entity_id,event_type,actor,created_at) VALUES (?,?,?,?,?)", ('SAMPLE',sid,sg,f'writer-{writer_id}',time.time()))
                tx(con, control, metrics)
            rows.append({"writer":writer_id,"sample":sample_name,"test_no":"","stage":"review"})
    finally:
        con.close()
        with open(Path(outdir) / f"worker_{writer_id}.json", "w", encoding="utf-8") as f:
            json.dump({"metrics":metrics,"expected_tests":expected,"rows":len(rows)}, f)


def percentile(vals, p):
    if not vals: return None
    vals=sorted(vals)
    k=(len(vals)-1)*p
    lo=int(k); hi=min(lo+1,len(vals)-1)
    if lo==hi: return vals[lo]
    return vals[lo] + (vals[hi]-vals[lo])*(k-lo)


def env_capture(root):
    disk=shutil.disk_usage(root)
    data={
        "platform":platform.platform(),"system":platform.system(),"release":platform.release(),"python":sys.version.replace("\n"," "),
        "sqlite":sqlite3.sqlite_version,"cpu_logical":os.cpu_count(),"disk_free_bytes":disk.free,"disk_total_bytes":disk.total,
        "cwd":str(Path(root).resolve())
    }
    if psutil:
        data["ram_total_bytes"]=psutil.virtual_memory().total
        data["boot_time"]=psutil.boot_time()
    return data


def monitor_sizes(db, stop, samples, pids):
    peak_db=peak_wal=0
    max_cpu=0
    max_mem=0
    max_child_cpu=0
    max_child_rss=0
    proc=psutil.Process(os.getpid()) if psutil else None
    while not stop.is_set():
        try:
            peak_db=max(peak_db,os.path.getsize(db) if os.path.exists(db) else 0)
            wal=db+"-wal"
            peak_wal=max(peak_wal,os.path.getsize(wal) if os.path.exists(wal) else 0)
            if proc and psutil:
                max_cpu=max(max_cpu,proc.cpu_percent(interval=None))
                max_mem=max(max_mem,proc.memory_info().rss)
                for pid in list(pids):
                    try:
                        cp=psutil.Process(pid)
                        max_child_cpu=max(max_child_cpu,cp.cpu_percent(interval=None))
                        max_child_rss=max(max_child_rss,cp.memory_info().rss)
                    except Exception:
                        pass
        except Exception:
            pass
        time.sleep(0.1)
    samples["peak_db_bytes"]=peak_db
    samples["peak_wal_bytes"]=peak_wal
    samples["max_monitor_process_cpu_percent"] = max_cpu
    samples["max_monitor_process_rss_bytes"] = max_mem
    samples["max_child_cpu_percent"] = max_child_cpu
    samples["max_child_rss_bytes"] = max_child_rss


def run_cell(root, size, writers, rep):
    sample_count=SAMPLE_COUNT_OVERRIDE
    run_dir=Path(root)/f"size_{size}_writers_{writers}_rep_{rep}"
    run_dir.mkdir(parents=True,exist_ok=True)
    db=str(run_dir/"spike.sqlite3")
    con=conn_open(db)
    con.executescript(SCHEMA)
    con.execute("PRAGMA journal_mode=WAL")
    con.execute("PRAGMA synchronous=FULL")
    con.close()
    # Warm-up one tiny transaction, not measured.
    con=conn_open(db); con.execute("BEGIN"); con.execute("INSERT INTO sample(id,writer_id,name) VALUES (?,?,?)",(99999999,0,'WARMUP')); con.execute("COMMIT"); con.close()
    warm=conn_open(db); warm.execute("DELETE FROM sample WHERE id=99999999"); warm.close()

    stop=mp.Event(); mon={}
    import threading
    procs=[]
    child_pids=[]
    t0=time.perf_counter()
    import threading
    th=threading.Thread(target=monitor_sizes,args=(db,stop,mon,child_pids),daemon=True); th.start()
    for w in range(writers):
        p=mp.Process(target=worker,args=(db,w+1,size,run_dir,sample_count,rep*1000+w+1))
        p.start(); procs.append(p); child_pids.append(p.pid)
    for p in procs: p.join()
    elapsed=time.perf_counter()-t0
    stop.set(); th.join(timeout=2)
    exitcodes=[p.exitcode for p in procs]

    # Reconciliation
    con=sqlite3.connect(db)
    counts={
        "samples":con.execute("SELECT COUNT(*) FROM sample").fetchone()[0],
        "tests":con.execute("SELECT COUNT(*) FROM test_instance").fetchone()[0],
        "observations":con.execute("SELECT COUNT(*) FROM observation").fetchone()[0],
        "results":con.execute("SELECT COUNT(*) FROM result").fetchone()[0],
        "audits":con.execute("SELECT COUNT(*) FROM audit_event").fetchone()[0],
        "non_approved_tests":con.execute("SELECT COUNT(*) FROM test_instance WHERE status!='APPROVED'").fetchone()[0],
        "fk_check":con.execute("PRAGMA foreign_key_check").fetchall(),
        "integrity_check":con.execute("PRAGMA integrity_check").fetchone()[0],
    }
    con.close()
    metrics=[]
    for w in range(1,writers+1):
        with open(run_dir/f"worker_{w}.json",encoding="utf-8") as f:
            metrics.append(json.load(f))
    lat=[]; retries=errors=0; retry_sleep=0; expected_tests=0
    for m in metrics:
        lat.extend(m["metrics"]["tx_latencies_ms"]); retries += m["metrics"]["retries"]; errors += m["metrics"]["errors"]; retry_sleep += m["metrics"]["retry_sleep_s"]; expected_tests += m["expected_tests"]
    expected_samples=writers*sample_count
    expected_audits=expected_samples*3 + expected_tests
    integrity_ok=(counts["integrity_check"]=="ok" and not counts["fk_check"] and counts["samples"]==expected_samples and counts["tests"]==expected_tests and counts["observations"]==expected_tests and counts["results"]==expected_tests and counts["audits"]==expected_audits and counts["non_approved_tests"]==0 and errors==0 and all(x==0 for x in exitcodes))
    result={
        "size_tests_per_sample":size,"writers":writers,"rep":rep,"samples_per_writer":sample_count,
        "elapsed_s":elapsed,"throughput_tx_s":(len(lat)/elapsed if elapsed else None),
        "tx_count":len(lat),"latency_ms":{"p50":percentile(lat,.50),"p95":percentile(lat,.95),"p99":percentile(lat,.99),"max":max(lat) if lat else None,"mean":statistics.mean(lat) if lat else None},
        "retries":retries,"retry_sleep_s":retry_sleep,"errors":errors,"process_exitcodes":exitcodes,
        "expected_samples":expected_samples,"expected_tests":expected_tests,"expected_audits":expected_audits,"counts":counts,
        "integrity_ok":integrity_ok,"peak_db_bytes":mon.get("peak_db_bytes",0),"peak_wal_bytes":mon.get("peak_wal_bytes",0),
        "final_db_bytes":os.path.getsize(db) if os.path.exists(db) else 0,"final_wal_bytes":os.path.getsize(db+'-wal') if os.path.exists(db+'-wal') else 0,
        "monitor":mon
    }
    with open(run_dir/"result.json","w",encoding="utf-8") as f: json.dump(result,f,indent=2)
    return result


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--root",default="runs")
    ap.add_argument("--reps",type=int,default=REPS)
    ap.add_argument("--samples",type=int,default=SAMPLES_PER_WRITER)
    args=ap.parse_args()
    Path(args.root).mkdir(parents=True,exist_ok=True)
    sample_count=args.samples
    env=env_capture(args.root)
    env["samples_per_writer"]=sample_count
    env["busy_timeout_ms"]=BUSY_TIMEOUT_MS
    env["retry_max"]=RETRY_MAX
    env["synchronous"]="FULL"
    results=[]
    global SAMPLE_COUNT_OVERRIDE
    SAMPLE_COUNT_OVERRIDE=sample_count
    for size in SIZES:
        for writers in WRITERS:
            for rep in range(1,args.reps+1):
                print(f"RUN size={size} writers={writers} rep={rep}",flush=True)
                results.append(run_cell(args.root,size,writers,rep))
    with open(Path(args.root)/"environment.json","w",encoding="utf-8") as f: json.dump(env,f,indent=2)
    with open(Path(args.root)/"results.json","w",encoding="utf-8") as f: json.dump(results,f,indent=2)
    fields=["size_tests_per_sample","writers","rep","elapsed_s","throughput_tx_s","tx_count","retries","retry_sleep_s","errors","integrity_ok","final_db_bytes","peak_wal_bytes","lat_p50_ms","lat_p95_ms","lat_p99_ms","lat_max_ms"]
    with open(Path(args.root)/"results.csv","w",newline="",encoding="utf-8") as f:
        wr=csv.DictWriter(f,fieldnames=fields); wr.writeheader()
        for r in results:
            wr.writerow({"size_tests_per_sample":r["size_tests_per_sample"],"writers":r["writers"],"rep":r["rep"],"elapsed_s":r["elapsed_s"],"throughput_tx_s":r["throughput_tx_s"],"tx_count":r["tx_count"],"retries":r["retries"],"retry_sleep_s":r["retry_sleep_s"],"errors":r["errors"],"integrity_ok":r["integrity_ok"],"final_db_bytes":r["final_db_bytes"],"peak_wal_bytes":r["peak_wal_bytes"],"lat_p50_ms":r["latency_ms"]["p50"],"lat_p95_ms":r["latency_ms"]["p95"],"lat_p99_ms":r["latency_ms"]["p99"],"lat_max_ms":r["latency_ms"]["max"]})
    print(json.dumps({"environment":env,"runs":len(results),"integrity_failures":sum(not r["integrity_ok"] for r in results),"max_retries":max(r["retries"] for r in results)},indent=2))

if __name__=='__main__': main()
