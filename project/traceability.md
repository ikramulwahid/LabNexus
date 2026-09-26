# LabNexus Traceability Index

## Purpose
This is a control index, not the full requirement-to-test matrix. The detailed 1,502-question history remains in `../PreCoding_Questions_v0.8.md`.

## Source → decision → current position

| Source/history | Current controlling record | Current position |
|---|---|---|
| Main Prompt D-001…D-015 | Main Prompt + living decision index | Frozen architectural baseline |
| PQ R0.8 architecture confirmations Q60–84 | PCD-01…27 where applicable | Confirmed/reconciled |
| PQ Q129–137 / Q80 | PCD-02 | Commercial charge calculation removed from v1 |
| PQ Q384–385 | PCD-03 + `project/domain-model.md` | Explicit TestInstance SoD Matrix |
| PQ Q255–260 / Q257 | PCD-04 | Versioned TestDefinition/ParameterDefinition |
| PQ Q339/Q367 and Q409–410 | PCD-05 + `project/domain-model.md` | ResultRevision/ApprovalSnapshot model |
| PQ Q424–425 / Q429 | PCD-06 | Accreditation resolved at execution start |
| PQ Q150–153 | PCD-07 | External ID unique per customer |
| PQ Q12/Q625/Q1061–1067 | PCD-08 | Controlled 10-year retention/archive baseline |
| PQ Q1391–1404 | PCD-09 | Canonical project structure/naming reconciled |
| PQ Q9/Q11/Q1217/Q1219/Q1225 | PCD-11 + P0-TASK-003/004 evidence | 50-test baseline, 80-test stretch; technical disposition B; formal acceptance pending |
| MP §0 and §21 schema wording | PCD-12 | No existing Phase 3 schema; build anew |
| PCD-03 detailed matrix | PCD-03 + `project/domain-model.md` | Per-TestInstance SoD, policy versioning and origin-analyst inheritance |
| PCD-05 detailed lifecycle | PCD-05 + `project/domain-model.md` | One ResultRevision stream, sequential numbering, no current_revision_id |
| PCD-13 execution semantics | PCD-13 + `project/domain-model.md` | Replicate/rework/retest/repeat/correction and independent states |
| PCD-14 reporting mechanics | PCD-14 + `project/domain-model.md` | Freeze-time snapshots and stale-before-issue new revision |
| PQ Q406–408 and Q1186–1189 | PCD-15 | Re-entry reserved for high-risk actions |
| PQ Q1359–1363 | PCD-17 | Controlled competence model |
| PQ Q895–905/Q942–943 | PCD-18 | Backup/disk thresholds clarified |
| PQ Q604/Q814/Q863 and related mechanism answers | PCD-19 | Operational mechanisms constrained |
| PQ Q1205–1207 | PCD-20 | Clock-integrity guards |
| PQ Q225/Q397/Q608 | PCD-21 | Unified audit service/write-path model |
| PQ Q15/Q1089/Q1099–1100 | PCD-22/27 | Controlled selective migration; no generic import |
| PQ Q1121–1144 | PCD-27 | Module/layer/API/error/concurrency conventions |
| PQ Q1229–1265 | PCD-27 | V&V/test pyramid and evidence rules |
| PQ Q1324–1333 | PCD-27 | Controlled exports; no raw table dump |
| PQ Q1354–1366 | PCD-27 | Training/help/manual requirements remain deployment/validation work |
| PQ Q1373–1375 | PCD-27 | Production changes remain Task/test/evidence/release controlled |

## Phase 0 evidence chain

The controlled Phase 0 performance evidence chain is:

`PCD-11 → P0-WP-001 → P0-TASK-003 → Windows evidence → P0-TASK-004 technical review → technical disposition B → formal acceptance pending`

The controlled security/domain documentation chain is:

`PCD-01/15/19/20/21 → P0-TASK-005 → project/security.md`

`PCD-03/05/13/14 → P0-TASK-007 → project/domain-model.md`

## Traceability rule
A material requirement shall ultimately trace through:

`Requirement/Source → Decision/Policy → Work Package → Task → Implementation → Test → Verification → Evidence → Checkpoint → Release`

Where implementation has not begun, downstream links remain planned rather than falsely marked complete.
