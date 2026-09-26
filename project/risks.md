# LabNexus Project Risks

| ID | Risk | Current treatment | Status |
|---|---|---|---|
| R-001 | Drift between historical root documents and living control documents | Preserve root history; living files index rather than copy; controlled changes update affected baselines | OPEN |
| R-002 | Required authority sign-offs remain outstanding | P0-TASK-011 found no new authority acceptance records; affected controlled behavior remains non-deployable until role-specific decisions are recorded | OPEN |
| R-003 | Launch technical inputs are not yet supplied | Do not invent technical behavior; use PCD-24/25 gates | OPEN |
| R-004 | Role-holder/staffing feasibility has not been demonstrated | Complete PCD-23 role-holder matrix before affected workflow activation | OPEN |
| R-005 | SQLite/workload assumptions require continued application-level validation | P0-WP-001 technical disposition B; retain monitoring and validate again against the implemented application workload | OPEN |
| R-006 | Security baseline consolidation was incomplete | Consolidated into `project/security.md`; implementation/verification remain separately governed | CLOSED for Phase 0 documentation scope |
| R-007 | Historical migration cannot fabricate approval chains | Perform controlled migration assessment; record No Migration Required where appropriate | OPEN |
| R-008 | Privileged-role password-length option remains undecided | Current controlled default remains 8; P0-TASK-011 found no adoption decision for 12 characters | OPEN |
| R-009 | Detailed TestInstance state-transition guards are not yet fully specified | Complete the approved Phase 1–2 transition matrix without inventing laboratory rules | OPEN |
| R-010 | Result/report historical reconstruction could be weakened by implementation shortcuts | Preserve direct ResultRevision and ReportResultSnapshot linkage; verify end-to-end reconstruction | OPEN |
| R-011 | Phase 0 checkpoint may be treated as accepted because documentation is complete | Keep checkpoint status explicitly OPEN / NOT ACCEPTED until required authority record exists | OPEN |
| R-012 | P0-TASK-001 has no dedicated task file in `project/work/` | Retain commit/control-record evidence; optionally backfill a historical task record only through a separately controlled documentation task | OPEN |
| R-013 | Phase 1 entry could be confused with dependent implementation gates or the later migration assessment | P0-TASK-010 explicitly classifies checkpoint/entry dependencies, affected-scope implementation gates, and the end-of-Phase-1 migration assessment | CLOSED after Phase 0 control-plan clarification |
## P0-TASK-012 checkpoint reassessment â€” 26 September 2026

P0-TASK-012 rechecked the repository and searchable GitHub acceptance surfaces and found no new decision evidence. R-002, R-003, R-004, R-007, R-008, R-011 and related open dependencies therefore retain their existing treatments and OPEN status. No risk closure was inferred from the absence of a decision record.

