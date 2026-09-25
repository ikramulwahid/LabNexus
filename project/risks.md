# LabNexus Project Risks

| ID | Risk | Current treatment | Status |
|---|---|---|---|
| R-001 | Drift between historical root documents and living control documents | Preserve root history; living files index rather than copy; future accepted changes must update the living register and affected baselines/contracts | OPEN |
| R-002 | Required authority sign-offs remain outstanding | Record each dependency explicitly; affected controlled behavior remains non-deployable | OPEN |
| R-003 | Launch technical inputs (tests, formulas, QC, report wording/scope) are not yet supplied | Do not invent technical behavior; use PCD-24/25 gates | OPEN |
| R-004 | Role-holder/staffing feasibility has not yet been demonstrated against PCD-03 | Complete named Role-Holder Matrix before affected workflow activation | OPEN |
| R-005 | SQLite/workload capacity assumptions have not yet been empirically verified | Define and execute the PCD-11 performance spike only under an authorized later task | OPEN |
| R-006 | Security baseline is indexed but not yet consolidated into its fuller controlled `security.md` document | Complete the separately proposed Phase 0 security-baseline task | OPEN |
| R-007 | Migration content may be useful but historical approval chains cannot be fabricated | Perform controlled migration assessment; record No Migration Required where appropriate | OPEN |

No new technical implementation risk has been introduced by this baseline task.
