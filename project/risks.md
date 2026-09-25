# LabNexus Project Risks

| ID | Risk | Current treatment | Status |
|---|---|---|---|
| R-001 | Drift between historical root documents and living control documents | Preserve root history; update living controls through controlled change | OPEN |
| R-002 | Required authority sign-offs remain outstanding | Record each dependency explicitly; affected controlled behavior remains non-deployable | OPEN |
| R-003 | Launch technical inputs (tests, formulas, QC, report wording/scope) are not yet supplied | Do not invent technical behavior; use PCD-24/25 gates | OPEN |
| R-004 | Role-holder/staffing feasibility has not yet been demonstrated against PCD-03 | Complete named Role-Holder Matrix before affected workflow activation | OPEN |
| R-005 | SQLite workload has occasional multi-second tail events under synthetic write contention | Technical disposition B; document bounded retry/monitoring controls; no production SLA inferred | OPEN |
| R-006 | Full SB-AMEND-001 security baseline is not yet consolidated into `project/security.md` | Complete P0-TASK-005 before Phase 1 security execution | OPEN |
| R-007 | Migration content may be useful but historical approval chains cannot be fabricated | Perform controlled migration assessment; record No Migration Required where appropriate | OPEN |
| R-008 | Phase 1 implementation could start before laboratory/authority gates are complete | P0-WP-002 defines explicit pre-implementation gates and checkpoint control | OPEN |

No application implementation or production configuration has been introduced by P0-TASK-006.
