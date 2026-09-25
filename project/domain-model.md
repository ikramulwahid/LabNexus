# LabNexus Controlled Domain-Model Baseline

## Status
**CONTROLLED BASELINE — P0-TASK-007 COMPLETE; NO SCHEMA OR APPLICATION IMPLEMENTATION AUTHORIZED**

This document establishes the controlled domain-model position for PCD-03, PCD-05, PCD-13 and PCD-14. It is a domain/requirements baseline, not a database schema, API contract, UI specification or implementation authorization.

## 1. Authority and source relationship

Current authority is reconciled from:
- `../Main_Prompt.md` §§7, 12–14, 20 and 39.
- `../PreCoding_Questions_v0.8.md` as reconciled historical requirements and question/answer evidence.
- `../Decision_register.md` PCD-03, PCD-05, PCD-13 and PCD-14.
- `project/decision-register.md` as the living decision index.
- `project/security.md` for the controlled security boundary affecting authorization, re-authentication and audit.

Historical source documents are preserved unchanged. Later accepted PCD decisions govern the current position when older PQ answers differ. Superseded PQ answers are not silently revived.

## 2. Domain-model objectives

The controlled model must:
1. distinguish RBAC authorization from record-specific TestInstance SoD;
2. preserve immutable historical result states and approval snapshots;
3. distinguish rework, retest, repeat and post-approval correction semantics;
4. preserve independent Sample and TestInstance lifecycles;
5. freeze report-visible technical state into ReportRevision snapshots;
6. support deterministic end-to-end historical reconstruction;
7. preserve actor, time, policy/configuration version and audit meaning for controlled actions.

No laboratory formula, acceptance criterion, reporting wording or other laboratory policy is invented by this document.

## 3. Core domain vocabulary

### 3.1 TestInstance

A TestInstance is the controlled execution instance of a TestRequest against a specific TestDefinition.

The authoritative structural relationship remains:

```text
TestRequest
→ TestInstance
→ TestDefinition
→ MethodVersion
→ Method
```

TestInstance is the scope for per-record SoD decisions and the primary scope of Review, Verification and Approval actions.

### 3.2 Analyst

For PCD-03, an Analyst is any user recorded as primary or contributing analyst on the TestInstance, or a user who entered, changed or corrected its observations, results or calculations.

Analyst status is determined from recorded activity, not merely job title.

### 3.3 Result and ResultRevision

```text
Result
├── ResultRevision (Correction)
├── ResultRevision (ApprovalSnapshot)
├── ResultRevision (Correction)
└── ResultRevision (ApprovalSnapshot)
```

The Result row represents the current live technical state. ResultRevision rows preserve the controlled historical sequence.

### 3.4 Report and ReportRevision

```text
Report
→ ReportRevision
→ ReportResultSnapshot
→ exact DocumentVersion / PDF artifact
```

ReportRevision owns the result snapshots used for that revision. A snapshot directly identifies the represented ResultRevision.

## 4. PCD-03 — TestInstance segregation of duties

### 4.1 Policy scope

RBAC answers what a user may do generally. TestInstance SoD answers whether that user may perform the action on the specific TestInstance after considering recorded actions on that record.

SoD is evaluated per TestInstance. The same user may act normally on different TestInstances where otherwise authorized.

### 4.2 Controlled matrix

| First recorded role/action | Second action on same TestInstance | Controlled rule |
|---|---|---|
| Analyst | Review | **HARD BLOCK** |
| Analyst | Verification | **HARD BLOCK** |
| Analyst | Approval | **HARD BLOCK** |
| Reviewer | Verification | **HARD BLOCK** |
| Reviewer | Approval | Policy-controlled; **default BLOCK** |
| Verifier | Approval | Policy-controlled; **default BLOCK** |
| Approver | Report Issue | Allowed only where the user is an Authorized Signatory |
| Analyst | Reopen / correction approval | May request; may not authorize |
| Correction author | Approval of that correction | **BLOCK**; renewed Review/Verification/Approval applies |

Hard blocks have no bypass.

Unlisted role/action combinations default to BLOCK unless later governed by an explicitly accepted matrix version.

### 4.3 Policy-controlled exceptions

Reviewer→Approval and Verifier→Approval may only be permitted under the specific controlled exception described by PCD-03:
- a different Verifier must have performed the verification;
- the exception is countersigned;
- the exception is visible and auditable;
- it is never introduced as an emergency exception.

The SoD matrix is versioned and effective-dated. Each approval-chain event records the policy version used.

### 4.4 Origin analyst inheritance

Retest, rework and any correction path that requires a new execution/TestInstance inherit the origin TestInstance's analyst set for hard-block evaluation.

This does not collapse separate TestInstances into one lifecycle. It preserves the originator relationship needed for SoD.

### 4.5 Replicates

Replicates are additional observations within the same TestInstance, distinguished by the approved replicate mechanism. They do not create a separate SoD scope.

### 4.6 Staffing implication

Under the default matrix, a controlled TestInstance requires four distinct competent people across analyst, reviewer, verifier and approver roles. Staffing feasibility is separately governed by PCD-23.

### 4.7 Security consistency

The domain model is consistent with `project/security.md`:
- backend/domain authorization is authoritative;
- UI-only SoD blocking is insufficient;
- hard blocks cannot be bypassed;
- Approval remains a high-risk re-authentication action;
- security denials must be auditable.

## 5. PCD-05 — ResultRevision and ApprovalSnapshot lifecycle

### 5.1 One revision stream

There is one controlled ResultRevision table/record stream.

Allowed revision types:
- `Correction`
- `ApprovalSnapshot`

They are semantically distinct and must not be collapsed into one generic history meaning.

### 5.2 Correction

A Correction represents a controlled historical technical-value change produced by reopening a post-approval TestInstance for data or calculation correction.

Correction does not mean a silent overwrite. The correction remains reconstructable as a numbered revision event/state in the ResultRevision sequence.

### 5.3 ApprovalSnapshot

An ApprovalSnapshot is the immutable historical version marker associated with successful Approval.

The snapshot carries the approved frozen representation specified by PCD-05, including:
- value;
- qualifier;
- unit;
- rounded value;
- TestDefinition and MethodVersion representation;
- analyst representation;
- resolved accreditation representation;
- approval time.

The exact represented ResultRevision is directly identifiable.

### 5.4 Revision numbering

`revision_number` is strictly sequential per Result across both revision types and is unique for the Result.

Submission before Review creates no ResultRevision. Pre-review edits are audited with old/new values.

The first successful Approval creates revision 1 as an ApprovalSnapshot.

A later controlled Correction creates the next revision number. Renewed Approval then creates the next ApprovalSnapshot.

### 5.5 Current live result

No stored `current_revision_id` is part of the approved model.

The current Result row carries the live technical values. Historical revision order is reconstructed from the deterministic ResultRevision sequence; the latest revision number is the maximum revision number for that Result.

### 5.6 Approval-chain linkage

The approved direction is:

```text
approval_chain_event.result_revision_id
→ result_revision.id
```

The ResultRevision does not carry a reverse FK to the approval-chain event; this avoids a circular dependency.

### 5.7 No-orphan ApprovalSnapshot invariant

The domain invariant is:
1. the successful Approval event and its ApprovalSnapshot are created atomically;
2. only one successful Approval event may point to a given ResultRevision;
3. verification must identify zero orphan ApprovalSnapshots.

The exact database mechanism is a later schema implementation concern; the invariant itself is controlled now.

### 5.8 Report-snapshot integrity

A ReportResultSnapshot must directly identify:
- ReportRevision;
- Result;
- ResultRevision.

The ResultRevision and Result identities must agree. The exact ResultRevision must never be inferred from the current Result row.

ResultRevision, ApprovalSnapshot and ReportResultSnapshot are historical records and must not be updated destructively to rewrite history.

## 6. PCD-13 — Execution, rework, retest, repeat, correction and state semantics

### 6.1 Execution-type semantics

| Type | Controlled representation |
|---|---|
| Replicate | Extra observations within the same TestInstance |
| Rework (pre-approval) | Same TestInstance returns to Rework; limited to data, calculation or transcription fixes that do not re-run the analysis |
| Retest | New TestInstance linked to the origin, reason RETEST, when the analysis must be re-run |
| Repeat | New TestInstance linked to the origin, reason REPEAT, under an approved rule |
| Correction (post-approval) | Same TestInstance is reopened; a Correction revision is created; renewed Review, Verification and Approval follow |
| Correction re-execution requiring a new analysis execution | Treated as a new TestInstance path rather than silently modifying the historical execution |

The distinction between correction of data/calculation and a path that genuinely re-runs the analysis is mandatory.

### 6.2 TestInstance state baseline

Normal path:

```text
Created
→ Assigned
→ In Execution
→ Result Ready
→ PendingReview
→ Reviewed
→ PendingVerification
→ Verified
→ PendingApproval
→ Approved
```

Documented exceptional states include:
- Hold
- Rework
- Cancelled
- Reopened

Known transaction boundaries:
- Reviewed→PendingVerification advances in the same transaction as the Review action.
- Verified→PendingApproval advances in the same transaction as the Verification action.

Approved is a normal forward terminal state. Only a controlled Reopen leaves Approved.

Any transition not in the subsequently accepted transition matrix is forbidden.

### 6.3 Sample independence

Sample follows an independent lifecycle. The controlled baseline includes:

```text
Received
→ Accepted / Conditionally Accepted / Rejected
→ Registered
→ Active
→ Completed
→ Disposed or Returned
→ Archived
```

On Hold is additionally available for identity investigation.

A Sample and its TestInstances therefore do not share one combined state machine.

### 6.4 Reopen and renewed control sequence

A post-approval correction does not bypass Review, Verification or Approval. After the controlled Correction action, the affected TestInstance follows the renewed control stages required by the PCD-13/PCD-05 baseline.

The correcting user is treated as an Analyst for the renewed SoD evaluation.

### 6.5 Detailed transition-matrix boundary

PCD-13 explicitly reserves the full transition matrix—source state, target state, actor, guard, reason and audit—for a later Phase 1–2 deliverable.

This P0 baseline therefore records the approved semantics without inventing missing laboratory or workflow guards.

Every later accepted transition row must have a corresponding verification test.

## 7. PCD-14 — ReportRevision freeze and stale-before-issue

### 7.1 Draft and freeze

A DRAFT ReportRevision contains the result selection only.

The freeze operation:
1. creates all required ReportResultSnapshot records;
2. freezes the report-visible technical representation;
3. moves the revision to `READY_FOR_ISSUANCE`;
4. performs these operations as one transaction.

Snapshots do not exist for a DRAFT revision before freeze.

### 7.2 Snapshot contents

The report snapshot freezes the report-visible data required by the approved model, including as applicable:
- value;
- unit;
- TestDefinition representation;
- resolved accreditation status;
- analyst representation;
- approval timestamp;
- exact ResultRevision identity.

The exact issued PDF is separately represented through the ReportRevision's approved DocumentVersion relationship.

### 7.3 Stale-before-issue rule

If a frozen revision becomes stale before issue:
1. the existing revision is marked `STALE`;
2. its snapshots are not updated;
3. a new ReportRevision is created;
4. the new revision receives new snapshots at its freeze;
5. issuance proceeds only from the current acceptable revision.

The stale revision remains historical.

### 7.4 Revision numbering and gaps

- Report number is allocated when the Report is created.
- Report `revision_no` is allocated at freeze.
- A stale, never-issued revision leaves its number gap.
- Numbers are never reused.

### 7.5 Open-revision invariant

At most one open ReportRevision exists for a Report, enforced by the approved uniqueness strategy at implementation time.

### 7.6 Issue fields and transitions

`issued_by_user_id` and `issued_at` are nullable before issue.

The controlled invariant is:

```text
status = ISSUED
⇒ issued_by_user_id IS NOT NULL
AND issued_at IS NOT NULL
```

Permitted ReportRevision status transitions are controlled and must not allow arbitrary mutation of historical issued content.

### 7.7 Issue, reissue and withdrawal

Issue, reissue and withdrawal are recorded on ReportRevision plus `audit_event`, including the required re-authentication evidence class.

These events are not `approval_chain_event` records because `approval_chain_event` is TestInstance-scoped.

## 8. Cross-cutting historical reconstruction

The model must support reconstruction:

```text
Customer
→ Project
→ Sample
→ TestRequest
→ TestInstance
→ TestDefinition
→ MethodVersion
→ Method
→ ParameterDefinition
→ Analyst
→ Equipment
→ Equipment eligibility
→ Observations
→ Formula / FormulaVersion
→ CalculationRun
→ Result
→ ResultRevision
→ Review
→ Verification
→ Approval
→ ApprovalSnapshot
→ Accreditation representation
→ Report
→ ReportRevision
→ ReportResultSnapshot
→ exact DocumentVersion / PDF
→ AuditEvent
```

Representative historical path:

```text
Result Revision 1
→ ApprovalSnapshot
→ ReportRevision 1
→ ReportResultSnapshot
→ PDF A

Later controlled Correction
→ Result Revision 2
→ renewed Review
→ renewed Verification
→ ApprovalSnapshot
→ ReportRevision 2
→ ReportResultSnapshot
→ PDF B
```

ReportRevision 1 remains reconstructable after later corrections.

The project's mandatory traceability question remains the acceptance test for the complete chain.

## 9. Controlled invariants

| Invariant | Classification | Current status |
|---|---|---|
| SoD hard blocks are non-bypassable | Domain rule + authorization policy | Controlled |
| Policy-controlled SoD exceptions require governed version/countersign | Domain rule + policy | Controlled; PCD-03 sign-off pending |
| ResultRevision numbers are sequential per Result | Domain rule + database uniqueness | Controlled |
| Only Correction / ApprovalSnapshot revision types are permitted | Domain rule + database CHECK | Controlled |
| No stored current_revision_id | Domain architecture | Controlled |
| ApprovalSnapshot is created atomically with successful Approval linkage | Domain transaction rule + verification | Controlled |
| ReportResultSnapshot directly references ResultRevision | Domain model + relational integrity | Controlled |
| DRAFT ReportRevision has no snapshots before freeze | Domain rule | Controlled |
| Freeze creates all snapshots atomically | Domain transaction rule | Controlled |
| Stale snapshots are immutable; new revision receives new snapshots | Domain rule | Controlled |
| One open ReportRevision per Report | Domain rule + database uniqueness | Controlled |
| Issued ReportRevision has issuer and issue time | Domain rule + database CHECK | Controlled |
| Report issue/reissue/withdrawal use audit_event, not approval_chain_event | Audit/domain rule | Controlled |
| Sample and TestInstance lifecycles are independent | Domain model | Controlled |
| Unspecified state transitions are forbidden | State-machine rule | Controlled; detailed matrix pending |

## 10. Remaining authority and laboratory inputs

The following remain outside this P0 baseline:
- PCD-03 formal SoD sign-off by the required authorities;
- PCD-13 Technical Authority sign-off on rework/retest/correction boundaries and detailed transition guards;
- PCD-23 named role-holder/staffing feasibility;
- laboratory-specific Test Catalogue, golden cases, QC matrix, report wording/template and related inputs under PCD-24/25;
- accreditation-scope operational inputs under PCD-06 where required.

PCD-05 and PCD-14 are confirmed domain decisions; this document does not reopen them.

## 11. Verification preparation

Later implementation verification shall include at least:
- same-TestInstance SoD hard-block tests;
- policy-controlled SoD exception tests and policy-version traceability;
- inherited-origin analyst tests for retest/rework/new-execution paths;
- sequential ResultRevision tests;
- ApprovalSnapshot no-orphan tests;
- correction → renewed Review/Verification/Approval tests;
- exact ResultRevision linkage in report snapshots;
- freeze atomicity;
- stale-before-issue creates a new revision without modifying old snapshots;
- revision-number gap preservation;
- report issue/reissue/withdrawal audit classification;
- full historical reconstruction test.

No such test execution is claimed by P0-TASK-007.

## 12. Explicit non-authorizations

This baseline does not authorize:
- application implementation;
- database schema or migration creation;
- API/UI implementation;
- formulas or calculation engines;
- laboratory-specific workflow guards not already decided;
- production configuration;
- UAT or validation execution.

Future work remains governed by:

`PHASE → WORK PACKAGE → AUTHORIZED TASK → IMPLEMENTATION → TEST → VERIFICATION → EVIDENCE → CHECKPOINT`
