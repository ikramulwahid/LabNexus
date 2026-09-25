# LabNexus Current State

## State as of 25 September 2026
**Phase 0 — IN PROGRESS**

### Baseline status
- Canonical `project/` control layer exists in the repository.
- Original source files remain preserved at repository root.
- No Phase 3 schema exists.
- No application development has been started by the Phase 0 control tasks.
- No production database, API, UI, migration or feature implementation has been performed.
- P0-WP-001 performance spike was executed on Windows with 45/45 cells completed and no integrity/application errors.
- PCD-11 technical disposition is B; formal acceptance remains subject to the project's acceptance record.
- SB-AMEND-001 is consolidated into the controlled `project/security.md` baseline.
- No Phase 0 checkpoint is ACCEPTED.

### Current active work
P0-TASK-007 — controlled domain-model baseline — complete.

### Domain-model position
PCD-03, PCD-05, PCD-13 and PCD-14 are now consolidated into `project/domain-model.md`. PCD-03 and PCD-13 retain their documented sign-off dependencies; PCD-05 and PCD-14 remain confirmed decisions.

### Authoritative position
Use the root source documents for historical/source detail and `project/decision-register.md` for the living decision index. Do not revive superseded answers silently.

### Security position
The controlled security baseline now includes authentication, sessions, password controls, authorization/SoD, high-risk re-authentication, application/database boundary, audit write path, malware/PDF/service mechanisms and clock-integrity controls. Implementation and verification remain separately governed work.

### Guardrail
No application, database, schema, API, UI, migration or feature implementation is authorized merely because a Phase 0 control document is complete.
