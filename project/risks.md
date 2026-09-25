# LabNexus Project Risks

| ID | Risk | Current treatment | Status |
|---|---|---|---|
| R-001 | Drift between historical root documents and living control documents | Preserve root history; living files index rather than copy; controlled changes update affected baselines | OPEN |
| R-002 | Required authority sign-offs remain outstanding | Record each dependency explicitly; affected controlled behavior remains non-deployable | OPEN |
| R-003 | Launch technical inputs are not yet supplied | Do not invent technical behavior; use PCD-24/25 gates | OPEN |
| R-004 | Role-holder/staffing feasibility has not been demonstrated | Complete PCD-23 role-holder matrix before affected workflow activation | OPEN |
| R-005 | SQLite/workload assumptions require continued application-level validation | P0-WP-001 technical disposition B; retain monitoring and validate again against the implemented application workload | OPEN |
| R-006 | Security baseline consolidation was incomplete | Consolidated into `project/security.md`; implementation/verification remain separately governed | CLOSED for Phase 0 documentation scope |
| R-007 | Historical migration cannot fabricate approval chains | Perform controlled migration assessment; record No Migration Required where appropriate | OPEN |
| R-008 | Privileged-role password-length option remains undecided | Current controlled default remains 8; obtain Project Owner decision before changing it | OPEN |
