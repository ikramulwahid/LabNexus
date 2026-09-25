# P0-WP-002 — Phase 1 Security / Requirements Evidence and Pre-Implementation Gates

## Status
**DEFINED — EXECUTION NOT AUTHORIZED**

## Purpose
Establish the controlled evidence package for Phase 1 (Requirements & Laboratory Model) and the acceptance conditions that must be satisfied before implementation phases can begin.

This Work Package defines evidence and governance. It does not implement the software.

## Authority and source hierarchy
1. `../Main_Prompt.md` — governing project baseline and development-control sequence.
2. `../PreCoding_Questions_v0.8.md` — complete reconciled question/answer history.
3. `../Decision_register.md` — PCD-01…PCD-27 supersession/reconciliation source.
4. `../project/security.md` — current Phase 0 security index pending P0-TASK-005 consolidation.
5. Accepted Phase 1 evidence records, authority sign-offs and checkpoints become authoritative for their respective subjects.

## Execution prerequisites
Phase 1 execution shall not begin until the following are satisfied or explicitly dispositioned under controlled change:

- P0-TASK-005 security-baseline consolidation completed and committed.
- PCD-11 technical evidence is accepted through the applicable project/technical acceptance record; current disposition is B and formal acceptance remains pending.
- Applicable authority sign-offs for PCD-03, PCD-06, PCD-08, PCD-13 and PCD-17 are recorded.
- PCD-23 Role-Holder Matrix is completed sufficiently to demonstrate approval/SoD feasibility.
- PCD-24 Launch Test Catalogue and golden cases are supplied by the Technical Authority.
- PCD-25 QC Matrix, NABL scope mapping, report wording/format and watermark inputs are supplied/approved.
- PCD-26 retained-sample/disposal/label/storage inputs are supplied/approved where needed for Phase 1 deliverables.

These are gates; they are not developer assumptions.

## Evidence stream 1 — Requirements baseline

### Required evidence
- Scope and exclusion baseline.
- Actor/role catalogue.
- End-to-end laboratory workflow model.
- Sample/TestRequest/TestInstance lifecycle definitions.
- Method/Test/Parameter versioning rules.
- Result/ResultRevision/ApprovalSnapshot rules.
- Review/Verification/Approval control model.
- Reporting and historical-reconstruction requirements.
- Quality, equipment, competence, retention, backup and operational requirements.
- Non-functional requirements derived from approved architecture and the performance-spike disposition.

### Traceability
Every material requirement shall trace through:

`Source → Decision/Policy → Phase 1 Requirement → Work Package/Task → Planned Test → Verification → Evidence → Checkpoint`

Where implementation has not begun, the downstream links may remain planned rather than falsely marked complete.

## Evidence stream 2 — Security verification definition

P0-TASK-005 shall create the controlled security baseline. P0-WP-002 then defines the verification evidence expected for at least:

| Control area | Minimum objective evidence |
|---|---|
| Password policy | Boundary tests for minimum/maximum length; no composition rules; paste support; blocklist rejection |
| Password hashing | Demonstration of Argon2id configuration and safe password-storage properties |
| Lockout/throttling | Tests for 5-failure/15-minute lockout and per-IP throttling |
| Password history | Reuse of the most recent five passwords rejected |
| Sessions | 30-minute idle and 12-hour absolute expiry; secure cookie attributes |
| CSRF | Negative/positive command tests under the chosen session architecture |
| High-risk re-entry | Re-authentication evidence for PCD-15 actions; Review/Verification exemption verified |
| RBAC | Backend permission matrix tests |
| TestInstance SoD | 100% of applicable PCD-03 cells tested, including hard blocks and policy-controlled combinations |
| Audit | Atomic business-change + audit persistence tests and denied-attempt audit tests |
| Clock integrity | Backward-jump and drift blocking behavior for approval/report issue |
| File/database boundary | Clients cannot access SQLite directly; application is the authoritative access path |
| Error handling | Errors do not disclose SQL, stack traces, secrets or internal paths |
| Malware quarantine | Unscanned/failed files remain blocked; Defender scan evidence |
| SQLite runtime | Startup/runtime version check and approved operational configuration |
| Unicode uniqueness | Normalization and unique-key behavior tested with relevant Unicode cases |
| Backup/recovery | Evidence for backup controls and restore/integrity checks at the appropriate later phase |

P0-WP-002 defines these evidence expectations only. No security implementation or security test execution is authorized by P0-TASK-006.

## Evidence stream 3 — Laboratory authority inputs

### PCD-03 / PCD-06 / PCD-08 / PCD-13 / PCD-17
Record the responsible authority, decision date/reference, approval state and affected requirements.

### PCD-24 — Launch Test Catalogue
Required fields include test name/code, standard/edition/clause, matrix, parameters, types, units, ranges, precision/rounding, observations/inputs, verbatim formulas/constants, reportable outputs, QC needs, equipment types, TAT and accreditation status.

Golden cases shall be supplied for each implemented formula before formula behavior can become controlled.

### PCD-25 — QC / NABL / reporting inputs
Required evidence includes:
- approved QC Matrix, including an explicit “no QC required” record where applicable;
- supplied NABL scope/schedule and approved mapping;
- approved wording/marks;
- approved controlled report format/template;
- watermark/status behavior decision.

### PCD-26 — operational laboratory inputs
Required evidence includes retained-sample periods by discipline, disposal authority/witness rules, legal-hold treatment, confirmed label-printer details and actual host/storage requirements.

## Evidence stream 4 — Role-Holder Matrix / feasibility

Create a controlled matrix covering the functional groups identified by PCD-23:

- Lab Head / Project Owner
- Quality Manager
- Technical Manager
- Analysts
- Reviewers
- System Administrator

For each controlled role/stage record:
- named primary;
- named alternate where required;
- competence scope/status;
- approval authority;
- segregation-of-duties conflicts;
- proposer/approver separation for configuration changes;
- feasibility status.

The matrix must demonstrate that the intended staffing model can satisfy PCD-03 and the designated approval authorities. The System Administrator must not approve technical results merely because of another role assignment.

## Evidence stream 5 — V&V and acceptance preparation

Define, before implementation, the evidence architecture for:

`Unit → Integration → API contract → End-to-end → Non-functional → Validation → UAT`

The Phase 1 plan shall identify:
- high-risk requirements;
- required negative-path tests;
- independence/verification responsibilities;
- evidence storage location and naming;
- defect/deviation handling;
- checkpoint entry/exit criteria.

No claim of test execution is permitted until execution evidence exists.

## Pre-implementation acceptance gates

### Gate G0 — Governance readiness
- Phase 1 Work Package accepted.
- Task authorization recorded.
- No scope creep or unresolved authority conflict.

### Gate G1 — Requirements baseline
- Requirements are traceable to source/decision authority.
- Scope/exclusions are controlled.
- Core workflow/state definitions are internally consistent.

### Gate G2 — Laboratory input readiness
- Required PCD-24/25/26 inputs are supplied and approved for the implementation slice.
- No formula, QC criterion, report wording or retention rule is invented by development.

### Gate G3 — Authority/staffing readiness
- PCD-23 Role-Holder Matrix demonstrates feasible role coverage.
- Required PCD authority sign-offs are recorded.
- SoD and alternate-approver feasibility is demonstrated.

### Gate G4 — Security readiness
- P0-TASK-005 security baseline is complete and controlled.
- Security verification evidence plan is accepted.
- Any remaining security open item has an explicit owner, disposition and effect statement.

### Gate G5 — Architecture/performance readiness
- PCD-11 evidence review is complete.
- Current technical disposition B is formally accepted or otherwise dispositioned by the applicable authority before implementation dependency is activated.
- SQLite architecture remains unchanged unless separately changed through formal architecture control.

### Gate G6 — V&V readiness
- High-risk requirements have planned verification.
- Independence and evidence rules are defined.
- Validation/UAT entry conditions are defined.

### Gate G7 — Phase checkpoint
The applicable Phase 1 checkpoint may be proposed for acceptance only after G0–G6 are satisfied, applicable deviations are controlled, and repository state is updated.

## Change-control rule
A missing laboratory input or authority decision shall not be converted into a developer default. Any change to a gate or acceptance condition requires controlled decision/ADR/change management.

## Non-goals
- No production implementation.
- No schema/migration implementation.
- No API/UI work.
- No feature development.
- No automatic approval of outstanding PCD sign-offs.

## Expected result
A complete, auditable Phase 1 evidence package exists before dependent implementation work begins, and a future checkpoint decision can determine whether the project may proceed to the implementation lifecycle.
