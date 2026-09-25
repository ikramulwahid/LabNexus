# LabNexus Current State

## State as of 25 September 2026
**Phase 0 — IN PROGRESS**

### Baseline status
- Repository reviewed before structural change.
- Original source files are preserved:
  - `../Main_Prompt.md`
  - `../PreCoding_Questions_v0.8.md`
  - `../Decision_register.md`
- The repository initially contained only those three project source files.
- The canonical living project-control layer is under `project/`.
- No Phase 3 schema exists.
- No application development has been started by the Phase 0 project-control tasks.
- No database, API, UI, migration, or feature implementation has been performed by the Phase 0 project-control tasks.
- No performance spike has been executed.
- No checkpoint is ACCEPTED.
- The current active work is recorded in `active-task.md`.

### Authoritative current position
The three root files remain historical source material. `project/decision-register.md` indexes the accepted reconciliation and is the living place for future project decisions. `project/traceability.md` records the relationship between requirements, superseding decisions and current position.

### Current baseline facts
- Frozen architecture remains unchanged.
- PCD-01…PCD-27 remain the current pre-coding decisions unless later formally superseded.
- PCD-11 now has a defined performance-spike Work Package; execution remains pending separate authorization.
- Outstanding authority/laboratory inputs are listed in `open-items.md`.
- Known project risks are listed in `risks.md`.
- Significant baseline/history changes are listed in `changes.md`.
- Checkpoint status is tracked in `checkpoints/checkpoint-register.md`.

### Guardrail for every future agent
Before doing work: read `current-state.md`, `active-task.md`, the relevant requirements/architecture/ADR/contract files, and the applicable checkpoint/decision records. Implement only an explicitly authorized task.

### Baseline commits
- Starting commit reviewed: `f93576c009935d6197c7d0fba30b8f603a96f7b2`
- Project-control baseline: `5a25763dd8ffc1bbc7bf125134ef1cdc5da217d1`
- P0-TASK-001 completion: `c8b734fb1bed8800f62aa0b6cd03e9597f953f8e`
