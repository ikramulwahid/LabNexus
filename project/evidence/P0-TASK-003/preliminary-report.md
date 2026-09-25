# P0-TASK-003 — Performance Spike Evidence Report

## Execution status
**Preliminary test-double execution complete; Windows deployment-host validation remains outstanding.**

The execution used a standalone controlled SQLite test double because the LabNexus application and Phase 3 schema do not yet exist. The available execution host is Linux, so these results are not claimed as Windows deployment evidence.

## Matrix executed
- 10, 25, 50, 65 and 80 tests per Sample.
- 1, 3 and 5 concurrent writers.
- 3 measured repetitions per matrix cell.
- 25 Samples per writer per run.
- 45 matrix cells total.
- WAL, foreign keys, 5,000 ms busy timeout, short `BEGIN IMMEDIATE` write transactions and `synchronous=FULL`.
- Deterministic synthetic data only.

## Integrity result
- Transactions executed: **168,750**.
- Integrity failures: **0**.
- Worker/application errors: **0**.
- Retry events after busy/locked timeout: **0**.
- `PRAGMA integrity_check`: `ok` in every run.
- `PRAGMA foreign_key_check`: no violations in every run.

## Mean results

| tests/sample | writers | mean throughput tx/s | mean p50 ms | mean p95 ms | mean p99 ms | worst max ms | mean peak WAL MB |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 1 | 17,236 | 0.031 | 0.064 | 0.134 | 0.3 | 0.00 |
| 10 | 3 | 16,108 | 0.030 | 0.081 | 0.287 | 53.7 | 2.25 |
| 10 | 5 | 16,309 | 0.030 | 0.080 | 0.309 | 82.7 | 2.53 |
| 25 | 1 | 18,770 | 0.030 | 0.081 | 0.296 | 1.7 | 0.00 |
| 25 | 3 | 18,119 | 0.029 | 0.075 | 0.230 | 79.7 | 3.96 |
| 25 | 5 | 17,958 | 0.030 | 0.081 | 0.248 | 179.2 | 4.04 |
| 50 | 1 | 21,776 | 0.030 | 0.075 | 0.168 | 0.9 | 0.00 |
| 50 | 3 | 19,028 | 0.031 | 0.087 | 0.214 | 180.6 | 3.98 |
| 50 | 5 | 18,612 | 0.030 | 0.072 | 0.186 | 333.8 | 4.06 |
| 65 | 1 | 19,838 | 0.030 | 0.081 | 0.199 | 7.4 | 0.00 |
| 65 | 3 | 18,073 | 0.030 | 0.076 | 0.213 | 180.4 | 3.99 |
| 65 | 5 | 15,973 | 0.030 | 0.076 | 0.229 | 438.4 | 4.66 |
| 80 | 1 | 20,342 | 0.030 | 0.072 | 0.193 | 8.4 | 0.00 |
| 80 | 3 | 19,012 | 0.031 | 0.077 | 0.231 | 229.7 | 3.98 |
| 80 | 5 | 17,082 | 0.031 | 0.082 | 0.245 | 530.6 | 5.34 |

## Findings
- No data-integrity failure was observed across the complete controlled matrix on this host.
- Median and p95 transaction latency remained low in the test double.
- The long-tail maximum reached **530.6 ms** at **80 tests/sample and 5 writers**, indicating intermittent write-contention waits.
- These waits did not produce transaction errors or reconciliation failures under the 5-second busy timeout.

## Limitation and required next evidence
- Host: Linux 6.18.44 x86_64; Python 3.13.5; SQLite 3.46.1; 3 logical CPUs; approximately 5.8 GiB RAM.
- Intended deployment host: Windows 11 Pro and/or Windows Server.
- The current evidence validates the benchmark method and gives a non-Windows SQLite contention baseline only.
- Run the included Windows validation script on the intended/representative Windows host before the final PCD-11 acceptance classification.

## Acceptance position
**No final A/B/C acceptance classification is made from the Linux run alone.** The result does not trigger an architecture change. PCD-11 remains open pending Windows-host evidence and formal review.

## Evidence contents
- `environment-linux.json`
- `results-linux.json` / `results-linux.csv`
- `summary-linux.csv`
- `raw-transaction-latencies-linux.csv`
- `sqlite_performance_spike.py
