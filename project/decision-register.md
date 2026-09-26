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

## Security consolidation
P0-TASK-005 consolidated SB-AMEND-001 and PCD-01/15/19/20/21 into `project/security.md`. The historical root Decision Register remains unchanged.

## P0-TASK-007 domain-model reconciliation

`project/domain-model.md` is the current controlled baseline for PCD-03/05/13/14.

### Historical/supersession position
- The root `Decision_register.md` remains the historical PCD reconciliation source.
- `PreCoding_Questions_v0.8.md` remains historical requirements/Q&A evidence.
- Older PQ answers superseded by PCD decisions remain historical and are not silently revived.
- PCD-03 retains its documented supersession of earlier Q384/Q385 wording and the detailed Q715 per-TestInstance scope.
- PCD-05 retains its documented amendment of earlier Q339/Q367 current-revision approaches.
- PCD-14 retains its documented clarifications of Q528/Q552/Q564/Q565/Q784/Q1190.

### Current controlled interpretation
PCD-03 is the authoritative detailed SoD matrix; PCD-05 is the authoritative ResultRevision/ApprovalSnapshot history model; PCD-13 governs execution/rework/retest/repeat/correction semantics and state-model boundaries; PCD-14 governs ReportRevision freeze/staleness and revision-number behavior.

## P0-TASK-009 authority/checkpoint reconciliation — 26 September 2026

The current GitHub `main` state was reviewed together with the Phase 0 checkpoint dossier, living control records, historical decision register, and searchable repository acceptance surfaces. No new authority acceptance record was identified for the outstanding decisions below.

| Ref | Evidence-backed result as of 26 Sep 2026 | Controlled status |
|---|---|---|
| PCD-03 | No Quality Authority / Project Owner formal sign-off record identified; existing detailed matrix remains the controlled baseline | NOT RECORDED / PENDING |
| PCD-06 | No Quality Authority sign-off / Technical concurrence record identified | NOT RECORDED / PENDING |
| PCD-08 | No Quality Authority + Project Owner acceptance record identified | NOT RECORDED / PENDING |
| PCD-13 | No Technical Authority sign-off record identified; detailed transition matrix remains later Phase 1–2 work | NOT RECORDED / PENDING |
| PCD-17 | No Technical Authority competence-model sign-off record identified | NOT RECORDED / PENDING |
| PCD-23 | No named Role-Holder Matrix / staffing-feasibility acceptance record identified | NOT RECORDED / PENDING |
| PCD-01 privileged-role option | Existing controlled risk acceptance supports the 8-character baseline; no decision adopting the optional 12-character minimum was identified | 12-CHARACTER OPTION NOT RECORDED / PENDING; DEFAULT 8 |
| PCD-11 | P0-TASK-004 technical disposition B is recorded; no separate formal acceptance record identified | TECHNICAL B; FORMAL ACCEPTANCE NOT RECORDED / PENDING |
| PCD-24 | No approved Launch Test Catalogue / golden-case laboratory input identified | LAB INPUT NOT RECORDED / PENDING |
| PCD-25 | No approved QC/scope/report-format/watermark laboratory input identified | LAB INPUT NOT RECORDED / PENDING |
| PCD-26 | No approved retained-sample/disposal/label/storage input identified | LAB INPUT NOT RECORDED / PENDING |
| PCD-22 | Selective migration remains the confirmed default; final migrate / No Migration Required assessment remains a Phase 1 assessment | CONFIRMED; ASSESSMENT PENDING (PHASE 1) |

No absence-of-record condition has been interpreted as approval. Historical sources remain unchanged.

## P0-TASK-010 controlled follow-up plan — 26 September 2026

The remaining Phase 0 dependencies are now classified by gate. Formal P0 checkpoint acceptance is the overall Phase 1 entry gate. PCD-03/06/08/13/17/23, PCD-11 formal acceptance, and the PCD-01 privileged-role option decision are checkpoint/entry dependencies. PCD-24/25/26 are dependent implementation/operational input gates. PCD-22 final migration assessment remains an end-of-Phase-1 activity.

No pending item is treated as approved without attributable evidence. Named individuals are not invented where only an authority role is currently known.

## Rule
A later accepted decision may supersede an earlier one only through controlled change. Historical source files are never silently rewritten.
