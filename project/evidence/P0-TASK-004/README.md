# P0-TASK-004 Evidence Closure

The technical review is provisionally complete, but final PCD-11 acceptance is held pending time-aligned Windows host telemetry.

The existing P0-TASK-003 Windows evidence must not be overwritten.

Run `RUN_WINDOWS_TELEMETRY_VALIDATION_R2.ps1` from the repository after copying this file into `project/evidence/P0-TASK-004/`. The script executes the same 45-cell workload into a separate `windows-validation-r2` directory while sampling CPU, memory and physical-disk counters.

After execution, review:

- `windows-validation-r2/environment.json`
- `windows-validation-r2/results.csv`
- `windows-validation-r2/results.json`
- `windows-validation-r2/host-telemetry.csv`
- `windows-validation-r2/benchmark.stdout.log`
- `windows-validation-r2/benchmark.stderr.log`

Do not interpret the rerun as a replacement for the original evidence; it is supplementary confirmation.
