# LabNexus Living Decision Register

## Purpose
This is the living project-control index for decisions. Historical source text remains in `../Decision_register.md`.

## Current decision index

| ID | Current position | Status |
|---|---|---|
| PCD-01 | Password minimum 8; mandatory offline blocklist; high-risk re-entry; privileged-role 12-character option open | CONFIRMED; 12-CHARACTER OPTION NOT RECORDED / PENDING |
| PCD-02 | Commercial charge/pricing logic out of v1 | CONFIRMED |
| PCD-03 | Detailed TestInstance SoD Matrix v1; hard blocks, governed policy-controlled combinations, origin-analyst inheritance and versioned policy | SIGN-OFF NOT RECORDED / PENDING |
| PCD-04 | Versioned TestDefinition/ParameterDefinition | CONFIRMED |
| PCD-05 | One ResultRevision stream with Correction/ApprovalSnapshot, sequential numbering, direct report linkage and no current_revision_id | CONFIRMED |
| PCD-06 | Accreditation resolved at execution start | SIGN-OFF NOT RECORDED / PENDING |
| PCD-07 | Internal Sample ID globally authoritative; external ID unique per customer | CONFIRMED |
| PCD-08 | 10-year retention/archive baseline | SIGN-OFF NOT RECORDED / PENDING |
| PCD-09 | Canonical project-control structure under `project/` | CONFIRMED |
| PCD-10 | Decimal canonical TEXT in SQLite | CONFIRMED |
| PCD-11 | 50-test baseline; 80-test stretch; technical disposition B with operational monitoring; formal acceptance pending | TECHNICAL B; FORMAL ACCEPTANCE NOT RECORDED / PENDING |
| PCD-12 | No Phase 3 schema exists; build anew | CONFIRMED |
| PCD-13 | Replicate/rework/retest/repeat/correction semantics with explicit TestInstance and Sample state models | SIGN-OFF NOT RECORDED / PENDING |
| PCD-14 | ReportRevision freeze creates immutable snapshots; stale-before-issue creates a new revision | CONFIRMED |
| PCD-15 | High-risk password re-entry | CONFIRMED |
| PCD-16 | Explicit core entity model | CONFIRMED |
| PCD-17 | Controlled competence model | SIGN-OFF NOT RECORDED / PENDING |
| PCD-18 | Tiered backups and thresholds | CONFIRMED |
| PCD-19 | Defender quarantine scan, shipped Chromium, runtime controls, Unicode normalization | CONFIRMED |
| PCD-20 | Clock-integrity guards | CONFIRMED |
| PCD-21 | Unified audit write path | CONFIRMED |
| PCD-22 | Selective migration default | CONFIRMED; ASSESSMENT PENDING (PHASE 1) |
| PCD-23 | Functional roles + named role-holder matrix | SIGN-OFF/INPUT NOT RECORDED / PENDING |
| PCD-24 | Launch Test Catalogue and golden cases | LAB INPUT NOT RECORDED / PENDING |
| PCD-25 | QC/scope/report inputs | LAB INPUT NOT RECORDED / PENDING |
| PCD-26 | Sample disposal/labels/storage inputs | LAB INPUT NOT RECORDED / PENDING |
| PCD-27 | Boilerplate PQ dispositions | CONFIRMED |

## P0-TASK-011 authority/laboratory decision review — 26 September 2026

The current GitHub `main` state was reviewed at commit `a78b00a594c7a947eab1c3dff2fec57e3139f951`. Recent commit history shows no commit after P0-TASK-010. Repository searches across code, issues and pull requests found no newly recorded authority acceptance/sign-off or laboratory input for the outstanding Phase 0 items.

| Ref | P0-TASK-011 result | Controlled status |
|---|---|---|
| PCD-03 | No new Quality Authority / Project Owner sign-off identified | NOT RECORDED / PENDING |
| PCD-06 | No new Quality Authority approval / Technical concurrence identified | NOT RECORDED / PENDING |
| PCD-08 | No new Quality Authority + Project Owner approval identified | NOT RECORDED / PENDING |
| PCD-13 | No new Technical Authority sign-off identified | NOT RECORDED / PENDING |
| PCD-17 | No new Technical Authority sign-off identified | NOT RECORDED / PENDING |
| PCD-23 | No named Role-Holder Matrix/staffing decision identified | NOT RECORDED / PENDING |
| PCD-01 option | No decision adopting the optional 12-character privileged-role minimum identified | NOT RECORDED / PENDING; DEFAULT 8 |
| PCD-11 | No formal acceptance record for technical disposition B identified | TECHNICAL B; FORMAL ACCEPTANCE NOT RECORDED / PENDING |
| PCD-24 | No approved Launch Test Catalogue/golden cases identified | LAB INPUT NOT RECORDED / PENDING |
| PCD-25 | No approved QC/scope/report-format/watermark inputs identified | LAB INPUT NOT RECORDED / PENDING |
| PCD-26 | No approved disposal/label/storage inputs identified | LAB INPUT NOT RECORDED / PENDING |
| PCD-22 | No new migration assessment identified | CONFIRMED DEFAULT; ASSESSMENT PENDING (PHASE 1) |

No absence-of-record condition has been interpreted as approval. Historical root sources remain unchanged.

## Rule
A later accepted decision may supersede an earlier one only through controlled change. Historical source files are never silently rewritten.
