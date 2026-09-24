# LabNexus — Pre-Coding Decision Register

| Field | Value |
|---|---|
| Document | `project/decision-register.md` |
| Version | 1.0 (Project Owner confirmed; authority sign-offs pending, see §6) |
| Date | 24 September 2026 |
| Owner | Project Owner / Laboratory Business Owner |
| Basis | Reconciliation of `Main_Prompt.md` (MP) against `PreCoding_Questions.md` R0.8 (PQ) |
| Supersedes | Contradicted or ambiguous answers listed in §4 |

---

## 1. Purpose and status

This register records the 27 decisions needed to resolve the contradictions, ambiguities and gaps found when MP and PQ were reconciled. It gives coding agents one authoritative baseline for those points.

**This document does not authorize implementation.** Coding remains subject to `PROJECT → PHASE → WORK PACKAGE → AUTHORIZED TASK → IMPLEMENTATION → TEST → VERIFICATION → EVIDENCE → CHECKPOINT` (D-009).

**Precedence.**
1. MP frozen decisions D-001…D-015 control.
2. PQ R0.8 refines them.
3. This register overrides PQ where §4 says so.
4. Where this register amends MP text (D-011, §23, §31), the entry here is the formal change record. It does not change any of D-001…D-015 in substance.

**Project-state facts recorded here.**
- No Phase 3 schema exists. The data architecture is to be built anew.
- MP's "~52 tables" is a planning figure, not a constraint. The MP §22 foreign-key list and the invariants in this register are inputs to Phase 3, not a finished design.
- Phase 0 is in progress. Phases 1–3 decisions are SPECIFIED only; no checkpoint is ACCEPTED.

**Decision types** (per PQ Q1499–1502): TD = Technical Decision, LD = Laboratory Decision, JA = Joint Approval, CSR = Commercial Scope Record.

---

## 2. Summary

**Status legend**
- **CONFIRMED**: confirmed by the Project Owner; no further authority sign-off required.
- **CONFIRMED — SIGN-OFF PENDING**: confirmed by the Project Owner, but a named authority must also sign before it becomes effective controlled behavior.
- **DEFAULT ADOPTED — LAB INPUT OUTSTANDING**: the mechanism is adopted, but laboratory content is still needed.

| ID | Decision | Type | Status | Sign-off needed |
|---|---|---|---|---|
| PCD-01 | Password minimum length = 8 | TD | CONFIRMED | — |
| PCD-02 | Charge calculation and Rate/CustomerRate out of v1 | CSR | CONFIRMED | — |
| PCD-03 | SoD matrix v1 | JA | CONFIRMED — SIGN-OFF PENDING | Quality Authority + Project Owner; Technical Authority reviews implementability (Q47) |
| PCD-04 | TestDefinition/ParameterDefinition row-versioning | TD | CONFIRMED | — |
| PCD-05 | ApprovalSnapshot and Result/ResultRevision lifecycle | TD | CONFIRMED | — |
| PCD-06 | Accreditation resolution point | JA | CONFIRMED — SIGN-OFF PENDING | Quality Authority; Technical concurrence (Q48) |
| PCD-07 | Sample identifier scheme | TD | CONFIRMED | — |
| PCD-08 | Retention meaning and trigger | LD | CONFIRMED — SIGN-OFF PENDING | Quality Authority + Project Owner (Q50) |
| PCD-09 | Repository structure and naming | TD | CONFIRMED | — |
| PCD-10 | Decimal storage in SQLite | TD | CONFIRMED | — |
| PCD-11 | Capacity baseline, hardware and performance spike | TD | CONFIRMED | — |
| PCD-12 | Project state (no schema exists) | TD | CONFIRMED | — |
| PCD-13 | Execution semantics and state models | JA | CONFIRMED — SIGN-OFF PENDING | Technical Authority |
| PCD-14 | ReportRevision mechanics | TD | CONFIRMED | — |
| PCD-15 | Actions requiring password re-entry | TD | CONFIRMED | — |
| PCD-16 | Core entity model | TD | CONFIRMED | — |
| PCD-17 | Competence entity | JA | CONFIRMED — SIGN-OFF PENDING | Technical Authority |
| PCD-18 | Backup tiers, coherence and disk thresholds | TD | CONFIRMED | — |
| PCD-19 | Mechanisms (scan, labels, PDF, services, SQLite version) | TD | CONFIRMED | — |
| PCD-20 | Clock integrity | TD | CONFIRMED | — |
| PCD-21 | Audit write path | TD | CONFIRMED | — |
| PCD-22 | Migration default | TD | CONFIRMED | Assessment outcome at end of Phase 1 |
| PCD-23 | Role-holder feasibility | JA | CONFIRMED — SIGN-OFF PENDING | Project Owner + Quality Authority (named individuals) |
| PCD-24 | Launch methods, tests, parameters, formulas | LD | DEFAULT ADOPTED — LAB INPUT OUTSTANDING | Technical Authority |
| PCD-25 | QC matrix, accreditation scope/wording, report format, watermark | LD | DEFAULT ADOPTED — LAB INPUT OUTSTANDING | Quality + Technical Authority |
| PCD-26 | Disposal, holds, labels, storage hardware | LD | DEFAULT ADOPTED — LAB INPUT OUTSTANDING | Quality/Technical Authority |
| PCD-27 | Disposition of the ~115 boilerplate PQ answers | TD | CONFIRMED | — |

Where one person holds several authority roles in this small laboratory, each required sign-off is still recorded separately by role. The independence rules (proposer ≠ approver and so on) still apply.

---

## 3. Decisions

### PCD-01 — Password minimum length = 8
- **Decision.** The minimum password length is **8 characters**. Allow at least 64 characters and support paste.
- **Rationale.** Project Owner risk acceptance for a single-site, LAN-only, offline system with about 10 named users. This is below current NIST guidance (15 for single-factor passwords) and is accepted knowingly. Weaker length is compensated by the controls below and by lockout.
- **Compensating controls (mandatory).**
  - An offline blocklist is required, not "where implemented". It covers roughly the 10,000 most common passwords plus the username, laboratory name and "labnexus" variants.
  - No complexity rules and no periodic expiry.
  - Argon2id; lockout after 5 failures for 15 minutes; password history of 5; per-IP throttling.
  - Fresh password re-entry for the actions in PCD-15.
- **Supersedes.** Q645 (12) and Q646 (15). Q647 stays valid, and its blocklist is now mandatory.
- **Open option (not adopted).** A 12-character minimum for Approver, Authorized Signatory and System Administrator accounts. Project Owner to decide; default is 8 for all roles.
- **Verification.** Unit tests for length boundaries (7 rejected, 8 accepted, 64+ accepted), blocklist rejection and history reuse. Security Baseline updated (§5).

### PCD-02 — Charge calculation out of v1
- **Decision.** Confirmed out of v1: rates, customer rates, charge snapshots, discounts, overrides, tax and invoicing. No placeholder columns.
- **Effects.** Rate and CustomerRate are removed from the tables to be designed and from MP §23's temporal review. Temporal review remains for MethodVersion, UserRoleAssignment and AccreditationScope. `TestRequest` is a request line without pricing.
- **Supersedes.** Q129–137 and Q80's charge-calculation clause, in favor of Q757–758 and Q1336–1353. MP D-011 said charges "may exist", so this is a scope reduction and not a frozen-decision change.
- **Later change.** Requires an approved commercial work package.

### PCD-03 — SoD matrix v1
- **Definition.** "Analyst" is any user recorded as primary or contributing analyst on the TestInstance, or who entered, changed or corrected its observations, results or calculations. It is judged by recorded actions, not job title.

| First action | Second action (same TestInstance) | Rule |
|---|---|---|
| Analyst | Review / Verification / Approval | **HARD BLOCK** (3 rules) |
| Reviewer | Verification | **HARD BLOCK** |
| Reviewer | Approval | Policy-controlled, default BLOCK. May be permitted only if a different Verifier verified, with a countersigned exception. Never as an emergency exception. |
| Verifier | Approval | Policy-controlled, default BLOCK, same exception form |
| Approver | Report issue | Allowed; the issuer must be an Authorized Signatory |
| Analyst | Reopen / correction approval | May request; may not authorize |
| Correction author | Approval of that correction | Blocked. The renewed Review, Verification and Approval follow the hard blocks, and the corrector counts as an analyst. |

- **Retest, rework and correction re-execution** create new TestInstances. They inherit the origin's analyst set for the hard blocks.
- **Replicates** are observations within one TestInstance and need no rule.
- **Unlisted pairs** default to BLOCK. Emergencies never affect hard blocks. SoD applies per TestInstance only (Q715).
- **Staffing note.** Under the defaults, each TestInstance needs four distinct competent people (analyst, reviewer, verifier, approver). See PCD-23.
- **Supersedes.** Q385 ("Approved for v1", non-responsive) and Q384's "recommended" wording. Q705's four hard blocks are confirmed.
- **Policy versioning.** The matrix is versioned and effective-dated. Every approval-chain event records the policy version used.

### PCD-04 — TestDefinition and ParameterDefinition versioning
- `test_definition` carries `test_code` and `version_no`, with UNIQUE(`test_code`, `version_no`). Effective periods for the same `test_code` must not overlap.
- Each version belongs to exactly one MethodVersion. The frozen chain TestInstance→TestDefinition→MethodVersion→Method is unchanged.
- A new MethodVersion, or any semantic change (Q264), creates a **new TestDefinition version** by cloning it, with a new approval. A row is never re-pointed to another MethodVersion.
- `parameter_definition` belongs to a TestDefinition version; `parameter_code` is unique within it. Formulas resolve parameter codes in that version's context.
- Accreditation override integrity holds by construction: the override's `test_definition_id` implies its MethodVersion.
- **Amends.** Q257 (effective-dated re-pointing of one TestDefinition) and the global uniqueness reading of Q255/Q260 (now unique per version, with the code shared across versions).

### PCD-05 — ApprovalSnapshot and Result/ResultRevision lifecycle
- **One revision table.** `result_revision.revision_type` ∈ {Correction, ApprovalSnapshot}.
- An ApprovalSnapshot revision carries the Q410 frozen fields: value, qualifier, unit, rounded value, TestDefinition and MethodVersion representation, analyst representation, resolved accreditation and approval time.
- **FK direction.** Only `approval_chain_event.result_revision_id → result_revision.id`. The revision has no FK back to the event, which avoids a circular FK.
- **"No orphan snapshot" (Q349)** is enforced by three things:
  - both rows are created in one transaction;
  - a partial UNIQUE index on approval events (`result_revision_id` WHERE stage = APPROVAL AND outcome = SUCCESS);
  - a verification query that must return zero orphans.
- **Numbering.** `revision_number` is strictly sequential per Result across both types, UNIQUE(`result_id`, `revision_number`).
- **Submission creates no revision.** Pre-review edits are audited with old and new values. The first approval creates revision 1. A later correction creates the next number.
- **No stored `current_revision_id`.** The Result row holds the live values, and "current revision" is `MAX(revision_number)`. This amends Q339 and Q367.
- **Snapshot integrity (MP §22).** UNIQUE(`id`, `result_id`) on `result_revision`, and a composite FK (`result_revision_id`, `result_id`) on `report_result_snapshot`.
- **Append-only.** `result_revision`, `approval_chain_event`, `report_result_snapshot`, `calculation_run` and `audit_event` are trigger-protected.

### PCD-06 — Accreditation resolution point
- **Single applicability instant:** the TestInstance's execution start (first transition to In Execution).
- The ApprovalSnapshot and the ReportResultSnapshot store the same resolved state and scope-record reference. The ReportResultSnapshot is authoritative for what was reported.
- **Issuance guard.** If scope was accredited at execution start but is suspended or withdrawn at issue time, issuance is blocked and routed to the Quality Authority.
- **No scope record** means non-accredited. No accreditation claim is rendered, and issuance is not blocked (Q1485).
- Retrospective scope corrections follow Q424–425.
- **Clarifies.** Q429, which named no rule.
- **Sign-off.** The Quality Authority confirms the execution-start rule.

### PCD-07 — Sample identifiers
- The internal Sample ID (`SAM-…`) is the only globally authoritative identifier and the only one printed on labels and barcodes.
- The external ID is unique per (customer, normalized external ID) among current authoritative values. Normalization is trim plus Unicode casefold. Duplicates within a customer are blocked. Cross-customer duplicates are allowed, with a search warning.
- Superseded or submitted values live in an identity-history table, marked provenance-only. The original external ID is immutable (Q182).
- **Amends.** Q150–153, which required global uniqueness. Customers routinely reuse labels such as "Sample 1".

### PCD-08 — Retention
- The retention period is 10 years minimum, counted from the **later of the last ReportRevision issue date and record closure**. The Retention Matrix may define other start events per record class, owned by the Quality Authority.
- Archive is a logical, read-only, searchable state in the same database and document store. It never deletes anything.
- v1 schema carries `retention_start`, `retention_until`, `archive_state` and hold references only. States are Active → Archived → Eligible for Destruction.
- **No destruction workflow in v1.** Nothing becomes eligible for about 10 years.
- Physical sample disposal is separate and is in v1 (PCD-26).
- **Clarifies.** Q12, Q625 and Q1061–1067.

### PCD-09 — Repository structure and naming
- MP §31 and Q1391 are canonical: `constitution.md`, `requirements.md`, `scope.md`, `architecture.md`, `domain-model.md`, `security.md`, `roadmap.md`, `current-state.md`, `active-task.md`, `handoff.md`, `open-items.md`, `traceability.md`, `work/`, `checkpoints/`.
- Additions required by Q1393: `decision-register.md` (this file), `risks.md`, `changes.md`, `adr/`, `contracts/` (database, api, ui), `evidence/`, `checkpoints/checkpoint-register.md`.
- The Project Charter content lives in `constitution.md`.
- **Naming.** kebab-case for control files. UPPER_CASE names are used only for generated register exports.
- **Supersedes.** Q1395–1403 file names (`PROJECT_STATE.md`, `ACTIVE_TASK.md`, `TRACEABILITY_MATRIX.md`, `ARCHITECTURE_BASELINE.md`, `CHECKPOINT_REGISTER.md`) and Q1404's UPPER_SNAKE_CASE rule.

### PCD-10 — Decimal storage in SQLite
- Store decimals as **canonical TEXT** (e.g. `'12.3400'`) through a SQLAlchemy `TypeDecorator` mapping to Python `Decimal`. Never REAL, and never SQLAlchemy `Numeric` on SQLite.
- Each numeric value keeps its reported precision or significant-figure metadata.
- CHECK constraints enforce a valid decimal pattern and MP §11's numeric-vs-text exclusivity.
- Range and limit checks run in the domain layer under a fixed Decimal context.
- The rounding mode is set per FormulaVersion from the method. There is no global default.

### PCD-11 — Capacity, hardware and performance spike
- **Design baseline is 50 tests per sample.** 80 is a stretch case, not an acceptance target. This amends the PQ Q9/Q11 ambiguity.
- **Two datasets.**
  - A realistic set: 250,000 samples × about 8 tests ≈ 2M TestInstances.
  - A stress set: 12.5M TestInstances.
- **PQ's 5 GiB database target** (Q1219) is treated as unverified. The unmeasured planning estimate is 3–8 KB per TestInstance including results, revisions, approval events, audit, observations and calculation runs, which is a much larger database. Measurements from the spike replace the estimate.
- **Performance spike.** The first Phase 5 work package runs it on the actual mini PC (i3-9100, 8 GB), using a seeded synthetic generator. It measures write p95, search and queue p95, backup time and WAL behavior. It verifies D-004's premise and does not reopen SQLite. Any failed target goes through an ADR.
- **Deployment recommendation.** 16 GB RAM, an SSD and a separate backup disk. The 8 GB host also runs Windows, Caddy, FastAPI, antivirus and Chromium.
- **Supersedes.** Q1217, Q1219 and Q1225 as fixed acceptance figures, pending spike results.

### PCD-12 — Project state
- `current-state.md` is set to: **Phase 0 IN PROGRESS; Phases 1–3 decisions SPECIFIED; no checkpoint ACCEPTED; no Phase 3 schema exists.**
- The Phase 3 data architecture is built anew, using MP §21–23 and this register as inputs.
- MP §0's reference to "approved Phase 3 data architecture" is read as the intended outcome, not existing work.
- The first authorized tasks (§7) are the Phase 0 baseline documents.

### PCD-13 — Execution semantics and state models
**Execution types**

| Type | Representation |
|---|---|
| Replicate | Extra observations (`replicate_no`) within the same TestInstance |
| Rework (pre-approval) | Same TestInstance returns to Rework. Only for data, calculation or transcription fixes that do not re-run the analysis. |
| Retest | New TestInstance, reason RETEST, linked to the origin. Used when the analysis must be re-run, before or after approval. |
| Repeat | New TestInstance, reason REPEAT, under an approved rule (e.g. customer request) |
| Correction (post-approval) | Reopen the same TestInstance, create a Correction revision, then renewed Review, Verification and Approval. Data or calculation fixes only. |

**TestInstance states**
- Normal path: Created → Assigned → In Execution → Result Ready → PendingReview → Reviewed → PendingVerification → Verified → PendingApproval → Approved.
- Exceptional states: Hold, Rework, Cancelled, Reopened.
- Reviewed→PendingVerification and Verified→PendingApproval advance in the same transaction as the action.
- Approved is a normal forward terminal state. Only a controlled Reopen leaves it.
- Any transition not in the matrix is forbidden.

**Sample states (independent).** Received → Accepted / Conditionally Accepted / Rejected → Registered → Active → Completed → Disposed or Returned → Archived, plus On Hold for identity investigation.

The full matrix (source, target, actor, guard, reason, audit per row) is a Phase 1–2 deliverable in `domain-model.md`. Every row gets a test. Sign-off: the Technical Authority confirms the rework/retest boundary.

### PCD-14 — ReportRevision mechanics
- **Snapshots exist only after freeze.** A DRAFT revision holds just the result selection. The freeze step creates all snapshots in one transaction and moves the status to READY_FOR_ISSUANCE.
- **Stale before issue.** Mark the revision STALE (a status change) and create a **new** revision with new snapshots. Snapshots are never updated.
- **One open revision per Report**, enforced by a partial unique index.
- **Numbers.** The Report number is allocated at Report creation. `revision_no` is allocated at freeze. A stale, never-issued revision leaves a gap that is not reused (Q784).
- **Nullable issue fields.** `issued_by_user_id` and `issued_at` are nullable, with a CHECK that status = ISSUED ⇒ NOT NULL. A trigger limits mutable fields to permitted forward transitions.
- **Extra links.** `template_document_version_id`, `pdf_document_version_id` and a `report_revision_attachment` link table (Q528, Q564).
- **Issue, reissue and withdrawal** are recorded on the ReportRevision plus `audit_event`, including the re-authentication evidence class. They are not `approval_chain_event` rows, because that table is TestInstance-scoped.
- **Clarifies.** Q552, Q565 and Q1190.

### PCD-15 — Password re-entry
- **Re-entry required for:** Approval, Reapproval, approval revocation, Reopen of an approved TestInstance, correction approval, report issue/reissue/withdrawal, configuration approval (especially accreditation, SoD and formulas), role-assignment approval, emergency declaration and countersign, and database restore.
- **No re-entry, but full e-signature evidence:** Review and Verification. They are attributable and revalidated server-side.
- **Batching.** One TestInstance's full result set is approved in a single action.
- **UAT review.** If per-approval re-entry proves impractical, change control may introduce a short (for example 5-minute) re-authentication window.
- **Clarifies.** Q406–408, Q1186–1189.

### PCD-16 — Core entity model
- Customer has sites and contacts.
- Contract (`CON-`) and Project (`PRJ-`) are separate optional grouping nodes.
- Request (`REQ-`) requires a Customer and optionally references a Project and Contract.
- A Sample belongs to exactly one Request in v1.
- TestRequest is one requested TestDefinition for one Sample, i.e. the request line.
- TestInstance links to its TestRequest and directly to its TestDefinition, with a nullable `sample_portion_id`. A composite FK plus a service rule ensures the portion belongs to the TestRequest's sample.
- **SamplePortion is in v1.** Splits, composites and derived samples stay out (Q176–178).
- **Clarifies.** MP's single "Project / Contract" node, and Q131, Q138, Q196.

### PCD-17 — Competence
- Add `user_competence(user_id, competence_type, scope_ref, valid_from, valid_to, evidence_document_link, approved_by)`.
- Scopes: discipline or TestDefinition, equipment type, workflow stage.
- The backend requires an active row at the action timestamp for assignment, execution, review, verification, approval and equipment use.
- Expiry **blocks** the action (fail closed) and warns 30 days ahead.
- Proposer ≠ approver, and the Technical Authority approves.
- No HR or training module. Training records stay external and are referenced as documents (Q1363).
- **Answers.** Q1359–1361.

### PCD-18 — Backup tiers, coherence and disk thresholds
**Tiered RPO**

| Tier | Schedule | Effective RPO |
|---|---|---|
| Local copy on a separate physical disk | every 4 h | ≤ 4 h |
| Encrypted offline copy | daily | ≤ 24 h |
| Off-site rotation | weekly | site-loss case |

- **Coherence without pausing the app.**
  1. Take the Online Backup API snapshot of the database first.
  2. Copy the write-once, hash-identified documents.
  3. Verify that every document the snapshot references exists with a matching hash. Extra documents are harmless.
- **RTO.** Requires an available replacement host. Recommendation: one second PC serving as validation/UAT machine (Q870), restore-test machine (Q922) and cold spare. Without one, state the RTO as restore time onto an available host.
- **Disk thresholds.**
  - Warn when free space falls below the *smaller* of 20% or 20 GiB.
  - Block risky writes below the *smaller* of 10% or 10 GiB.
  - Alert when projected days-to-full drops below 30.
- **Clarifies.** Q895–905, Q942–943.

### PCD-19 — Mechanisms
- **Malware scan.** Microsoft Defender `MpCmdRun.exe -Scan -File` on a quarantine upload folder (works offline). Fail closed: an unscanned or failed file stays PENDING/QUARANTINED.
- **Labels.** Code 128 or QR generated as SVG in a configurable HTML template, printed via the browser to the Windows printer driver with `@page` sizing.
- **PDF.** Playwright for Python driving a **Chromium pinned and shipped in the release bundle**. One or two workers at most, network blocked, local fonts only.
- **Services.** WinSW hosts uvicorn (single process) and Caddy. Windows Task Scheduler runs backup, integrity and disk checks via an app CLI. A light in-app scheduler handles overdue detection and notifications. Correctness never depends on a scheduler; emergency and configuration expiry are evaluated by timestamp at read time.
- **SQLite.** Require ≥ 3.35 (for `UPDATE … RETURNING`, Q149). Check at startup and refuse to start otherwise. Pin Python and record the actual SQLite version (Q814).
- **Antivirus.** No exclusions by default (Q1295). Test on the real host under load. If SQLITE_BUSY or I/O errors appear, add one narrowly scoped, documented exclusion for the database folder only.
- **Unicode uniqueness.** Normalize codes on write (NFKC + casefold + strip) into a `*_key` column with UNIQUE. `COLLATE NOCASE` is ASCII-only and is not used.

### PCD-20 — Clock integrity
- **Backward-jump guard.** If current time is earlier than the latest recorded audit timestamp by more than 60 seconds, block approval and report issuance and raise an alert.
- **Drift.** Block those two actions if measured offset against the reference exceeds **2 minutes**. Warn above 30 seconds.
- **Source.** Windows Time against the LAN/domain source, or a time-only outbound NTP rule if the laboratory permits. Otherwise the administrator records a manual check in the operations log, with a warning if none is recorded within 7 days.
- Only server time is stored; client clocks are ignored.
- **Answers.** Q1205–1207.

### PCD-21 — Audit write path
- One `AuditService` and repository with two transaction modes:
  - *in-transaction* with the business change (normal);
  - *autonomous short transaction* for denied attempts, which have no business write.
- **Ownership.**
  - `approval_chain_event` records decisions on the technical record only: passed, failed with reason, revoked, countersigned.
  - Permission, SoD and authentication denials go to `audit_event` only.
- Denial events are aggregated per source per minute so they cannot flood the database.
- **Clarifies.** Q225, Q397, Q608 against MP §19's single write path.

### PCD-22 — Migration default
- **Default assumption.** Migrate only the customer master list and historical issued report PDFs, as read-only historical documents linked to customers and legacy sample references (Q1089). No historical results or TestInstances enter live tables, because that would mean fabricating approval chains.
- **Schema impact.** `migration_batch`, `record_origin` (NATIVE / MIGRATED_HISTORICAL), `legacy_reference`, and a HISTORICAL_REPORT link type. Legacy report numbers do not use the sequences.
- **Confirmation.** Formalized at the end of Phase 1. If the assessment finds nothing suitable, record "No Migration Required" (Q15).

### PCD-23 — Role-holder feasibility
- The roughly 15 authorities in Q35–59 and Q676 are collapsed into about six functional groups: Lab Head / Project Owner, Quality Manager, Technical Manager, Analysts, Reviewers, System Administrator. Each has named individuals and alternates.
- A **Role-Holder Matrix** is completed in Phase 1 and checked for:
  - enough people to satisfy PCD-03;
  - a second named person for every approval authority (Q54);
  - separate proposer and approver for configuration changes.
- Any action with fewer than two eligible people is flagged.
- The System Administrator cannot approve technical results (Q702), even if also the Project Owner.
- **Lab input.** Names and competences.

### PCD-24 — Launch methods, tests, parameters, formulas *(Lab input outstanding)*
- The laboratory completes a **Launch Test Catalogue** sheet per test:
  - name and code; standard, edition and clause; matrix;
  - parameters (code, type, unit, range, precision, rounding, qualifiers);
  - observations and inputs;
  - the formula verbatim with constants;
  - reportable outputs, QC needs, equipment types, TAT, scope status.
- **Pilot slice.** 3–5 highest-volume tests per discipline. Likely candidates, to be confirmed against the NABL scope: moisture, ash, volatile matter, fixed carbon (calculated, tests dependent calculations) and calorific value, with basis conversion.
- **Golden cases.** At least 3 worked examples per formula from validated worksheets, including a boundary case, with expected values approved by the Technical Authority.
- No formula, rounding rule or unit conversion is invented by the implementation (Q1486).

### PCD-25 — QC matrix, scope, wording, report format, watermark *(Lab input outstanding)*
- **QC.** Launch QC Matrix template per test: type, frequency, criterion, blocking or warning, disposition. **No TestDefinition becomes effective without an approved QC record**, even one that states "no QC required". A QC failure blocks approval by default until the Technical Authority classifies it.
- **Scope.** Imported from the NABL certificate and scope schedule, approved by the Quality Authority. Anything not listed is non-accredited.
- **Wording and marks.** Supplied and approved by the laboratory. Templates that need them are not issuable until then.
- **Report format.** The current controlled report reproduced as a Jinja template, one Test Report type, held as a controlled DocumentVersion approved by Technical and Quality Authorities.
- **Watermark.** Draft/non-issued renders carry "DRAFT – NOT ISSUED". Issued PDFs are never altered. Superseded or withdrawn status is shown in the application and in the replacement report's statement, not as an in-file watermark. Quality Authority confirms.
- **Answers.** Q468–479, Q1184, Q1485–1488.

### PCD-26 — Disposal, holds, labels, storage hardware *(Lab input outstanding)*
- **Disposal authority.** The Technical Authority or a designated Sample Custodian authorizes; a Sample Receiving user executes; a witness is added where a customer contract requires it. Disposal is blocked until all of the sample's TestInstances are Approved or Cancelled and the retained-sample period has elapsed. The **retained-sample period is a laboratory policy per discipline** and is not supplied here.
- **Legal hold (minimal).** `retention_hold` with scope (customer, project, sample or report), reason, placed-by, authorized-by (Quality Authority) and dates. It blocks disposal and any future destruction.
- **Labels.** Template size is configurable. Two example sizes ship; one is confirmed in UAT. The laboratory names a Windows-driver thermal printer before the intake work package.
- **Storage.** Record the real disk capacity, model and free space. Indicative sizing after the spike: at least a 512 GB SSD, a separate backup drive of at least 1 TB, and two encrypted USB drives for rotation.
- **Answers.** Q172, Q999, Q1005, Q1080, Q840.

### PCD-27 — Disposition of the boilerplate PQ answers
About 115 PQ questions received a shared, non-responsive paragraph. Their dispositions:

| Questions | Answer | Owner |
|---|---|---|
| Q150–153 | PCD-07 | Phase 3 |
| Q356, Q362–366 | Three classes: technical result correction, report representation error, customer-data error. A result correction always triggers a report-impact assessment via snapshots (Q567). A new ReportRevision is mandatory if an issued snapshot referenced the changed value. Representation-only errors get a ReportRevision without a result revision. | Phase 11/15 |
| Q480–491 | A blocking QC failure auto-creates a nonconformance. The investigation is the NC record, closed by Technical or Quality Authority. CAPA is an optional linked reference. **No control charts, Westgard rules or statistical QC in v1.** | Phase 12/13 |
| Q966–967, Q1150 | Form state stays in React memory with retry. No localStorage or IndexedDB. Warn 2 minutes before idle timeout. Data beyond the tab's life is accepted as lost. | Phase 4 |
| Q1099–1100, Q1334–1335 | No generic import. Only a go-live master-data seed (customers, equipment, storage locations) via a validated, audited admin CLI, plus migration batches. External IDs are reference fields. | Phase 7/14 |
| Q1121–1144 | Modules: `identity_access`, `audit`, `numbering`, `master_data`, `sample`, `test_execution`, `method_config`, `review_approval`, `equipment_qc`, `quality`, `documents`, `reporting`, `ops`. Layers: router → application service → domain → repository; no cross-module repository access, enforced by import-linter. REST/JSON at `/api/v1`, OpenAPI-generated. RFC 7807 errors with `code`, `message`, `correlation_id`, `field_errors`. `row_version` on mutable controlled rows (409/412). `Idempotency-Key` on command endpoints. `X-Request-ID` stored in audit events. Pagination default 50, max 200, cursor for audit and queues. Whitelisted sort fields. Responses never expose hashes, secrets or filesystem paths. | Phase 2/5 |
| Q1229–1265 | See V&V summary below | Phase 1–2 (V&V Plan), Phase 18 |
| Q1324–1333 | CSV/XLSX for lists, PDF for reports. Exports respect permissions and filters. Each export is audited with query and row count. Bulk export needs a separate permission (Quality or Admin roles). No raw table-dump endpoint. | Phase 6/14 |
| Q1354–1366 | Tooltips on complex fields; versioned PDF user guides as controlled documents; local user manual before go-live; role-based work instructions (Q1276). Approvers and reviewers need a competence record (PCD-17). Training records are external. | Phase 19 |
| Q1373–1375 | Every production change follows Task → test → evidence → release. Emergency fixes use a minimal hotfix branch, are still tested, never skip the pre-change backup, and get retrospective review within 5 working days. After go-live, a Change Request becomes a Task under a per-release lightweight WP. | Phase 0 governance / 20 |

**V&V summary (Q1229–1265)**
- **Layers.** Unit (domain, state machine, SoD, formula evaluator with golden cases) → integration (real temp SQLite, constraint and trigger tests, concurrency) → API contract → Playwright end-to-end → non-functional (performance, restore drill) → validation → UAT.
- **Gates.** 100% of state-matrix rows and SoD cells have tests. At least 90% branch coverage on SoD, state machine, formula evaluator, numbering and audit. Overall coverage is informational.
- **Data.** Seeded synthetic data only. Production data never enters test environments.
- **Independence.** Verification by someone other than the implementer. Validation by Technical and Quality Authorities. UAT by scripted scenarios run by laboratory users.
- **Evidence.** Markdown evidence records plus pytest JUnit XML and Playwright reports under `evidence/`.
- **Deviations.** Minor ones need an owner and due date. A checkpoint cannot be ACCEPTED with an open defect touching a high-risk requirement (MP §28 list).

**Other "closed but really open" PQ answers**
- **Q604.** Hash-verify a rotating 1/7 slice weekly, a full pass monthly, and a full pass after every restore or deploy.
- **Q863.** Chrome and Edge current stable, tested versions recorded per release. Firefox unsupported in v1.
- **Q385.** Superseded by PCD-03.
- **Q514.** Superseded by Q1183/1193: no cryptographic PDF signature in v1.

---

## 4. Amendment register

| Source | Change | By |
|---|---|---|
| Q645, Q646 | Password minimum 12/15 → 8; blocklist mandatory | PCD-01 |
| Q80 (charge clause), Q129–137 | Superseded by deferral; MP §23 Rate/CustomerRate dropped | PCD-02 |
| Q385, Q384 | Replaced by SoD matrix v1 | PCD-03 |
| Q255, Q257, Q260 | TestDefinition versioned by row; no re-pointing | PCD-04 |
| Q339, Q367 | `current_revision_id` removed | PCD-05 |
| Q429 | Applicability instant defined | PCD-06 |
| Q150–153 | Global uniqueness → per-customer | PCD-07 |
| Q1395–1404 | File names and casing | PCD-09 |
| Q9, Q11, Q1217, Q1219, Q1225 | Capacity figures provisional pending spike | PCD-11 |
| MP §0, §21 ("approved Phase 3") | Read as intended outcome; no schema exists | PCD-12 |
| Q942, Q943 | "Whichever first" → the smaller of % or GiB | PCD-18 |
| MP §23, §31 text | Amended as above; MP file itself not edited | PCD-02, PCD-09 |

---

## 5. Security Baseline amendment SB-AMEND-001

To be merged into `security.md` when Phase 0 baseline documents are created.

| Control | Value |
|---|---|
| Minimum password length | **8** (was 12/15). Maximum accepted ≥ 64. |
| Composition rules | None. No periodic expiry. |
| Blocklist | Mandatory, offline (about 10,000 common passwords plus username, lab name, "labnexus" variants) |
| Hashing | Argon2id |
| Lockout | 5 failures → 15 minutes; per-IP throttling |
| Password history | 5 |
| Sessions | 30 min idle, 12 h absolute |
| Re-entry | Actions listed in PCD-15 |
| MFA | Not required in v1 |
| Risk acceptance | Project Owner, 24 September 2026: length below NIST guidance accepted for a single-site, LAN-only, offline system with about 10 named users, compensated by the controls above |

---

## 6. Outstanding sign-offs and laboratory inputs

| Ref | Item | Needed from |
|---|---|---|
| PCD-03 | Approve SoD Matrix v1 | Quality Authority + Project Owner; Technical Authority review |
| PCD-06 | Confirm execution-start accreditation rule | Quality Authority (Technical concurrence) |
| PCD-08 | Approve retention start and archive rule | Quality Authority + Project Owner |
| PCD-13 | Confirm rework/retest boundary | Technical Authority |
| PCD-17 | Approve competence model | Technical Authority |
| PCD-23 | Named Role-Holder Matrix | Project Owner + Quality Authority |
| PCD-01 (option) | 12-character minimum for privileged roles: yes/no | Project Owner |
| PCD-24 | Launch Test Catalogue and golden cases | Technical Authority |
| PCD-25 | QC Matrix, NABL scope, wording, report format, watermark | Quality + Technical Authority |
| PCD-26 | Retained-sample period, disposal authority, label printer, host disk details | Quality/Technical Authority, IT |
| PCD-22 | "Migrate/No Migration Required" outcome | Migration assessment, end of Phase 1 |

Until these are signed or supplied, the affected behavior remains non-deployable (Q1481–1489). Items that do not depend on them may proceed in Phase 0.

---

## 7. Proposed follow-on Phase 0 tasks (not authorized)

These are proposals only. Each needs explicit task authorization (D-009).

1. Create the repository skeleton per PCD-09.
2. Populate `current-state.md` per PCD-12.
3. Merge SB-AMEND-001 into `security.md`.
4. Draft `domain-model.md` sections for PCD-03, PCD-05, PCD-13 and PCD-14.
5. Create `open-items.md`, `risks.md` and `changes.md` from §6 and the risks in PCD-11 and PCD-23.
6. Define the performance-spike work package (PCD-11).

---

## 8. Approval record

| Role | Name | Decision | Date | Signature/reference |
|---|---|---|---|---|
| Project Owner | | Confirmed (24 Sep 2026) | | |
| Laboratory Quality Authority | | | | |
| Laboratory Technical Authority | | | | |
| Document/Project Controller | | | | |
