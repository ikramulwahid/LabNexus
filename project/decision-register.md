# LabNexus Living Decision Register

## Purpose
This is the living project-control index for decisions.

## Precedence
1. `../Main_Prompt.md` — governing frozen baseline.
2. `../PreCoding_Questions_v0.8.md` — reconciled question/answer history.
3. `../Decision_register.md` — PCD-01…PCD-27 reconciliation source.
4. This file and future accepted project decisions/ADRs update the living position through controlled change.

## Current decision index

| ID | Current position | Status |
|---|---|---|
| PCD-01 | Password minimum 8; mandatory offline blocklist; re-entry controls; privileged-role 12-character option remains open | CONFIRMED; OPTION OPEN |
| PCD-02 | Charge calculation, Rate/CustomerRate and related pricing/invoicing logic are out of v1 | CONFIRMED |
| PCD-03 | TestInstance SoD Matrix v1 with hard blocks and governed policy-controlled combinations | SIGN-OFF PENDING |
| PCD-04 | TestDefinition/ParameterDefinition row-versioning; no re-pointing of used historical definitions | CONFIRMED |
| PCD-05 | Single ResultRevision history with Correction/ApprovalSnapshot types; no stored current_revision_id | CONFIRMED |
| PCD-06 | Accreditation applicability resolved at execution start; issue guard applies for later suspension/withdrawal | SIGN-OFF PENDING |
| PCD-07 | Internal Sample ID globally authoritative; external ID unique per customer | CONFIRMED |
| PCD-08 | Minimum 10-year retention; later of last ReportRevision issue and closure, with governed archive/hold semantics | SIGN-OFF PENDING |
| PCD-09 | Canonical project-control naming/structure under `project/` with living decision/register/control files | CONFIRMED |
| PCD-10 | SQLite Decimal values stored as canonical TEXT via SQLAlchemy TypeDecorator | CONFIRMED |
| PCD-11 | 50 tests/sample design baseline; 80 stretch; Windows spike completed with 0 integrity failures; technical disposition B with documented operational controls/monitoring | TECHNICAL DISPOSITION B; FORMAL ACCEPTANCE PENDING |
| PCD-12 | No Phase 3 schema exists; data architecture is built anew | CONFIRMED |
| PCD-13 | Explicit execution/rework/retest/correction/state semantics | TECHNICAL AUTHORITY SIGN-OFF PENDING |
| PCD-14 | Freeze-time ReportRevision snapshots; stale-before-issue creates new revision | CONFIRMED |
| PCD-15 | Password re-entry for designated high-risk actions; Review/Verification retain attributable e-signature evidence without re-entry | CONFIRMED |
| PCD-16 | Explicit Customer/Project/Contract/Request/Sample/TestRequest/TestInstance model; SamplePortion included | CONFIRMED |
| PCD-17 | Controlled user_competence model; active competence required for designated actions | TECHNICAL AUTHORITY SIGN-OFF PENDING |
| PCD-18 | Tiered backups, coherence verification and disk thresholds | CONFIRMED |
| PCD-19 | Defender quarantine scan; Code128/QR labels; pinned shipped Chromium; WinSW/Task Scheduler; SQLite ≥3.35; Unicode *_key normalization | CONFIRMED |
| PCD-20 | Clock backward-jump/drift guards for approval and report issue | CONFIRMED |
| PCD-21 | AuditService/repository atomic normal writes plus autonomous denied-attempt logging | CONFIRMED |
| PCD-22 | Selective migration default; final migrate/no-migration assessment at end of Phase 1 | CONFIRMED; ASSESSMENT PENDING |
| PCD-23 | Functional role groups plus named role-holder matrix and alternates; staffing feasibility check | SIGN-OFF/INPUT PENDING |
| PCD-24 | Launch Test Catalogue and golden cases required; no formulas/rounding/unit conversion invented | LAB INPUT PENDING |
| PCD-25 | Launch QC Matrix, NABL scope/writing/report format/watermark inputs required | LAB INPUT PENDING |
| PCD-26 | Retained-sample period, disposal/hold, label printer and actual host/storage details required | LAB INPUT PENDING |
| PCD-27 | Boilerplate PQ answers explicitly dispositioned into current controlled behavior | CONFIRMED |

## Phase 1 evidence package
P0-TASK-006 defines P0-WP-002 covering requirements evidence, security verification planning, laboratory authority inputs, role-holder feasibility, V&V preparation and pre-implementation acceptance gates.

## Security prerequisite
P0-TASK-005 remains the required consolidation task for SB-AMEND-001 before Phase 1 security execution.
