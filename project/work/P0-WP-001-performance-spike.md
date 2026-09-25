# P0-WP-001 — SQLite / Workload Performance Spike

## Status
**DEFINED — EXECUTION NOT AUTHORIZED**

## Parent decision
PCD-11 — 50 tests/sample design baseline; 80 tests/sample stretch; empirical performance spike required.

## Purpose
Empirically determine whether the approved v1 SQLite architecture remains operationally suitable for the confirmed small-laboratory workload on the actual or representative Windows host, using synthetic data and representative application transaction patterns.

This Work Package is a validation activity. It does not itself reopen the SQLite decision.

## Constraints and baseline

| Item | Baseline |
|---|---|
| Deployment | Windows single-host |
| Database | SQLite |
| Live DB location | Local fixed disk only; never NAS/SMB |
| SQLite operating mode | WAL, foreign keys enabled, busy timeout, short write transactions |
| Concurrent writers | 1–5 |
| Design baseline | 50 tests per Sample |
| Stretch case | 80 tests per Sample |
| Data | Synthetic only |
| Internet | Not required |
| Production data | Prohibited |

The actual test host and software versions shall be recorded before execution.

## Questions to answer

1. Does the system sustain the design workload of 50 tests per Sample with up to 5 simultaneous writers without data-integrity failures?
2. How does the system behave at the 80-test stretch case?
3. Does write contention remain operationally manageable under the approved SQLite controls?
4. Are there materially different results for read/write mix, cold/warm cache state, or repeated batches?
5. Are database size, WAL growth/checkpoint behavior, CPU, memory and disk I/O acceptable for the host?
6. Does the observed behavior support retaining the current SQLite architecture, retaining it with documented operational limits/tuning, or raising a formal architecture review?

## Workload model

The execution task shall map the following abstract workload stages to the actual application commands available at execution time:

| Workload stage | Representative activity |
|---|---|
| Intake | Sample/request registration and identifier allocation |
| Setup | TestRequest/TestInstance creation and assignment |
| Execution | Observation entry, result calculation/persistence and save operations |
| Control | Review/verification/approval persistence |
| Reporting | Report revision/snapshot/document persistence where implemented |

The spike shall emphasize write paths because SQLite's concurrency envelope is most sensitive to writes. Read activity may be introduced to represent ordinary LAN use but shall not obscure the writer-concurrency results.

### Workload sizes

Minimum sample-size cases:

- 10 tests/sample — small case
- 25 tests/sample — intermediate case
- 50 tests/sample — design baseline
- 65 tests/sample — near-stretch case
- 80 tests/sample — stretch case

### Writer concurrency

Each applicable workload case shall be exercised at:

- 1 simultaneous writer
- 3 simultaneous writers
- 5 simultaneous writers

The final execution matrix may add intermediate or repeated cases where needed to localize a contention boundary, but it shall not drop the 50/80 design/stretch cases.

## Execution methodology

### Environment capture
Before testing, record:

- Windows edition/version/build
- CPU model and logical processors
- installed RAM
- storage device type/model for the live DB
- live DB disk free space
- Python version
- SQLite runtime version
- application/release identifier, when an executable application exists
- relevant SQLite configuration
- antivirus/Defender state and any approved scoped exclusions
- background services/processes relevant to the test host

No unrecorded tuning shall be treated as part of the evidence.

### Data preparation
Use synthetic, deterministic datasets representing realistic laboratory records without any production information.

The dataset must be sufficiently large to exercise the 50- and 80-test/sample cases and must permit exact pre/post reconciliation of counts and values.

### Run structure
For each matrix cell:

1. Start from a known database state.
2. Perform any defined warm-up separately from measured runs.
3. Execute at least three measured repetitions.
4. Capture raw measurements and integrity checks for every repetition.
5. Record anomalies, retries, lock contention and failed operations.
6. Checkpoint/cleanly close the database according to the test procedure before the next independent condition where applicable.

Warm-cache and restart/cold-start conditions should be distinguished where they materially affect the observed result.

## Measurements

### Correctness / integrity — mandatory
- Lost writes: **0 permitted**
- Duplicate command effects where idempotency is applicable: **0 permitted**
- Foreign-key/constraint corruption or unexpected integrity failures: **0 permitted**
- Unexplained transaction failures: **0 permitted**
- Post-run reconciliation mismatch: **0 permitted**

Any integrity failure is a significant result even if average performance appears acceptable.

### Performance
Capture at minimum:

- operation/transaction latency
- p50 latency
- p95 latency
- p99 latency where the sample count permits
- throughput / completed operations per unit time
- retry count and retry delay
- SQLite busy/locked events
- queue/wait time attributable to write contention, where measurable

No absolute latency or throughput pass threshold is invented by this Work Package. Execution must record the agreed operational acceptance envelope before the results are declared pass/fail.

### Host / storage behavior
Capture:

- CPU utilization
- memory utilization
- disk utilization / I/O wait where available
- database file size
- WAL file growth and checkpoint behavior
- free-space change
- abnormal OS/application events

## Acceptance logic

The evidence review shall classify the spike result as one of:

### A. Baseline supported
Observed behavior supports the current SQLite architecture for the confirmed workload, with no material integrity failure and within the approved operational acceptance envelope.

### B. Baseline supported with documented limits/tuning
The architecture remains viable, but evidence identifies bounded operational limits or configuration/tuning requirements that must be documented and approved before dependent implementation proceeds.

### C. Architecture review required
The evidence demonstrates that the confirmed workload cannot be supported reliably within the approved constraints. This does not automatically authorize a database replacement. A formal architectural change assessment must be opened with the evidence attached.

## Required evidence

The execution task shall produce:

1. Environment record.
2. Test-data generation record.
3. Executed workload matrix.
4. Raw measurement files.
5. Integrity/reconciliation results.
6. Performance summary.
7. Anomaly/incident log.
8. Final technical conclusion.
9. Traceability from PCD-11 → Work Package → execution task → evidence → checkpoint decision.

## Stop conditions

Stop the run and record the condition if:

- database integrity is compromised or cannot be reconciled;
- unexplained data loss or duplicate effects occur;
- the host becomes unstable;
- the test procedure deviates materially from the approved matrix;
- a result can no longer be attributed to the intended workload condition.

A stopped run is evidence, not a reason to silently discard the condition.

## Dependencies

Execution requires, at minimum:

- an authorized execution task;
- a defined benchmark/test harness or approved execution mechanism;
- an available Windows host representative of the intended deployment;
- the applicable application/data model or controlled test double sufficient to represent the intended transaction paths;
- approved operational acceptance thresholds before final pass/fail classification.

## Non-goals

This spike does not:

- certify laboratory performance;
- establish regulatory compliance;
- replace UAT or validation;
- justify arbitrary schema denormalization;
- justify network-share SQLite;
- permit production-data use;
- authorize a PostgreSQL migration or any other architecture change.

## Decision record

The final evidence review shall update PCD-11 status and, where necessary, open an architecture/change record. Until that evidence exists, PCD-11 remains **SPIKE EXECUTION PENDING**.
