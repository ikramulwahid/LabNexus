# P0-TASK-007 — Establish the Controlled Domain-Model Baseline for PCD-03, PCD-05, PCD-13 and PCD-14

## Status
**COMPLETE**

## Authorization
Explicit project instruction dated 25 September 2026 authorizing P0-TASK-007.

## Objective
Establish the controlled domain-model baseline for TestInstance SoD, ResultRevision/ApprovalSnapshot history, execution and correction semantics, and ReportRevision freeze/stale behavior.

## Source set reconciled
- `Main_Prompt.md` §§7, 12–14, 20 and 39.
- `PreCoding_Questions_v0.8.md` reconciled historical answers.
- `Decision_register.md` PCD-03, PCD-05, PCD-13 and PCD-14.
- `project/decision-register.md` living decision index.
- `project/security.md` controlled authorization, re-authentication and audit boundary.

## Scope
- Establish the current domain-model position without implementing schema or code.
- Preserve historical decisions and supersession references.
- Identify remaining authority/laboratory inputs.
- Reconcile domain behavior with the architecture and controlled security baseline.
- Correct stale control-document references discovered during reconciliation.

## Completion criteria
- [x] PCD-03 TestInstance SoD matrix and hard/policy-controlled rules are documented.
- [x] PCD-05 ResultRevision and ApprovalSnapshot lifecycle is documented.
- [x] PCD-13 execution, rework, retest, repeat, correction and state semantics are documented.
- [x] PCD-14 ReportRevision freeze and stale-before-issue behavior is documented.
- [x] Historical/source precedence and supersession handling are preserved.
- [x] Remaining authority and laboratory inputs are explicitly identified.
- [x] Domain model is checked for consistency with `project/security.md`.
- [x] The stale P0-TASK-005 next-task reference is corrected.
- [x] No application, database, schema, migration, API, UI, calculation or feature implementation was introduced.

## Reconciliation result

### PCD-03
The Master Prompt contains the baseline hard blocks and policy-controlled Reviewer/Approver behavior. PCD-03 supplies the detailed matrix, Analyst definition, origin-analyst inheritance, default BLOCK treatment for unlisted pairs, policy versioning/effective dating and staffing implication. These details are current controlled requirements.

### PCD-05
The Master Prompt and PCD-05 agree on a single ResultRevision history with Correction and ApprovalSnapshot types, immutable approval snapshots, direct report linkage and no current_revision_id. PCD-05 additionally fixes revision numbering and approval-event linkage direction.

### PCD-13
The Master Prompt requires explicit state machines. PCD-13 supplies the controlled distinction between replicate, rework, retest, repeat and post-approval correction, plus the normal TestInstance path and independent Sample lifecycle. The full transition matrix remains a later Phase 1–2 deliverable as explicitly stated by PCD-13; missing laboratory guards were not invented.

### PCD-14
The Master Prompt requires ReportRevision/ReportResultSnapshot reconstruction. PCD-14 adds the freeze transaction, stale-before-issue behavior, revision numbering/gap rules, one-open-revision invariant and audit classification of issue/reissue/withdrawal.

### Security consistency
The domain baseline remains consistent with `project/security.md`: backend authorization is authoritative; hard SoD blocks are non-bypassable; Approval and report issue are high-risk re-authentication actions; denied actions and report controls remain auditable.

## Remaining controlled inputs
PCD-03 and PCD-13 sign-offs remain pending. PCD-23 staffing feasibility remains pending. PCD-24/25 laboratory inputs remain pending. PCD-06 accreditation operational sign-off remains pending where applicable.

## Result
**Domain-model baseline established.** Implementation, schema, testing, verification and checkpoint acceptance remain separately governed.
