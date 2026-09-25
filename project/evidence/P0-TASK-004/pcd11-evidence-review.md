# PCD-11 Evidence Review — P0-TASK-004

## Evidence source
Windows execution of P0-WP-001 using the LabNexus synthetic SQLite performance harness, plus the supplementary R5 Windows host-telemetry run.

## Execution completeness
The workload matrix was executed for:

- 10, 25, 50, 65 and 80 tests per Sample;
- 1, 3 and 5 simultaneous writers;
- 3 repetitions per cell;
- 45 cells total.

The 50-test design baseline and 80-test stretch were both exercised at every required writer count.

## Windows environment
- Windows 11 build `10.0.26100-SP0`.
- Python 3.13.5 64-bit.
- SQLite 3.49.1.
- 4 logical CPUs.
- Approximately 61 GB free space at the benchmark start.
- SQLite busy timeout: 5,000 ms.
- Configured retry maximum: 6.
- SQLite synchronous mode: FULL.

## Hard correctness
| Measure | Result |
|---|---:|
| Matrix cells | 45 |
| Integrity failures | 0 |
| Application errors | 0 |
| Original-run total retries | 24 |
| Original-run maximum retries | 4 |
| R5 maximum retries | 5 |
| Retry-budget exhaustion | 0 |
| Benchmark exit code (R5) | 0 |

The tested Windows workload completed without integrity loss or application error.

## Host telemetry
R5 captured 138 valid telemetry samples with zero telemetry-error samples.

| Metric | Minimum | Average | Maximum |
|---|---:|---:|---:|
| CPU utilization | 0% | 20.014% | 72% |
| Committed memory | 69% | 69.297% | 71% |
| Disk time | 0% | 8.123% | 72% |
| Disk bytes/sec | 0 | 36,070,893 | 90,306,996 |

`AvgDiskSecPerTransfer` was below the recorded display precision and is not used for acceptance.

## Tail-latency findings
The Windows results show generally low p95 latency but occasional multi-second maximum transaction latency. The largest supplied values are approximately 10.4–10.6 seconds in 5-writer cases. Similar high maxima also appeared in one-writer cases.

These events are therefore treated as genuine operational anomalies. The evidence does not prove that SQLite writer contention is the sole cause. Host telemetry shows average CPU/disk utilization is moderate, with transient peaks; storage and background activity remain plausible contributors.

## Technical disposition
**B — Baseline supported with documented operational controls/monitoring.**

The tested evidence supports retaining SQLite for the defined small-laboratory workload envelope. The evidence warrants explicit monitoring of retry frequency and tail latency in later application validation.

## Acceptance boundary
No production SLA is inferred from this synthetic spike. Formal acceptance remains subject to the project's authority/checkpoint process. Until that record is completed, PCD-11 remains **technical disposition B / formal acceptance pending**.
