# LabNexus Living Decision Register

## Purpose
This is the living project-control index for decisions. Historical source text remains in `../Decision_register.md`.

## Current decision index

| ID | Current position | Status |
|---|---|---|
| PCD-01 | Password minimum 8; mandatory offline blocklist; high-risk re-entry; privileged-role 12-character option open | CONFIRMED; OPTION OPEN |
| PCD-02 | Commercial charge/pricing logic out of v1 | CONFIRMED |
| PCD-03 | TestInstance SoD Matrix v1 | SIGN-OFF PENDING |
| PCD-04 | Versioned TestDefinition/ParameterDefinition | CONFIRMED |
| PCD-05 | ResultRevision/ApprovalSnapshot; no current_revision_id | CONFIRMED |
| PCD-06 | Accreditation resolved at execution start | SIGN-OFF PENDING |
| PCD-07 | Internal Sample ID globally authoritative; external ID unique per customer | CONFIRMED |
| PCD-08 | 10-year retention/archive baseline | SIGN-OFF PENDING |
| PCD-09 | Canonical project-control structure under `project/` | CONFIRMED |
| PCD-10 | Decimal canonical TEXT in SQLite | CONFIRMED |
| PCD-11 | 50-test baseline; 80-test stretch; technical disposition B with operational monitoring; formal acceptance pending | TECHNICAL B; FORMAL ACCEPTANCE PENDING |
| PCD-12 | No Phase 3 schema exists; build anew | CONFIRMED |
| PCD-13 | Execution/rework/retest/correction semantics | TECHNICAL SIGN-OFF PENDING |
| PCD-14 | Freeze-time ReportRevision snapshots | CONFIRMED |
| PCD-15 | High-risk password re-entry | CONFIRMED |
| PCD-16 | Explicit core entity model | CONFIRMED |
| PCD-17 | Controlled competence model | TECHNICAL SIGN-OFF PENDING |
| PCD-18 | Tiered backups and thresholds | CONFIRMED |
| PCD-19 | Defender quarantine scan, shipped Chromium, runtime controls, Unicode normalization | CONFIRMED |
| PCD-20 | Clock-integrity guards | CONFIRMED |
| PCD-21 | Unified audit write path | CONFIRMED |
| PCD-22 | Selective migration default | CONFIRMED; ASSESSMENT PENDING |
| PCD-23 | Functional roles + named role-holder matrix | SIGN-OFF/INPUT PENDING |
| PCD-24 | Launch Test Catalogue and golden cases | LAB INPUT PENDING |
| PCD-25 | QC/scope/report inputs | LAB INPUT PENDING |
| PCD-26 | Sample disposal/labels/storage inputs | LAB INPUT PENDING |
| PCD-27 | Boilerplate PQ dispositions | CONFIRMED |

## Security consolidation
P0-TASK-005 consolidated SB-AMEND-001 and PCD-01/15/19/20/21 into `project/security.md`. The historical root Decision Register remains unchanged.

## Rule
A later accepted decision may supersede an earlier one only through controlled change. Historical source files are never silently rewritten.
