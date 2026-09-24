# LabNexus Pre-Coding Questions — Complete Reconciled Q1–Q1502

**Compilation status:** COMPLETE SOURCE-BASED RECONCILIATION + REVISION 0.8 DECISION CLOSURE

**Reconciliation baseline:** Revision 0.8 — ACCEPTED PRE-CODING DECISION BASELINE — READY FOR PHASE 0 BASELINE / AUTHORIZED-TASK CREATION

**Supersedes:** Revision 0.7 working baseline and all prior reconciliation working states.

The original question wording and numbering are preserved. Revision 0.8 controls supersede contradictory or incomplete source answers for affected questions; unaffected questions retain their source answers.

## Revision 0.8 Decision Closure Register

Revision 0.8 closes the remaining pre-coding decision blockers identified in the prior reconciliation baseline.

### Closure rules

1. Every Q1–Q1502 has a reconciled answer and an explicit Revision 0.8 status.
2. No question remains in an unresolved **LABORATORY DECISION REQUIRED**, **TECHNICAL DECISION REQUIRED**, **PROPOSED DEFAULT — PENDING APPROVAL**, **CONFLICT — REQUIRES RESOLUTION**, or **DEPLOYMENT INPUT** state.
3. Questions whose resolved answer is intentionally governed by a later project phase are marked **CLOSED — SAFE TO DEFER** rather than left unresolved.
4. Commercial charge calculation is explicitly deferred from v1; invoicing, accounts receivable, payments, and tax/accounting remain external.
5. The approved security defaults are now controlled baseline decisions.
6. Equipment-status vocabulary and transition semantics are now controlled baseline decisions.
7. Repository-control structure is established as the mandatory Phase 0 target baseline.
8. This document is an accepted **pre-coding decision baseline**. It does **not** itself authorize implementation. Coding remains subject to the Main_Prompt development-control chain:
   PROJECT → PHASE → WORK PACKAGE → AUTHORIZED TASK → IMPLEMENTATION → TEST → VERIFICATION → EVIDENCE → CHECKPOINT.

### Q1. What exact legal/business name should appear in the LIMS, reports, documents, and configuration?

**Reconciled Answer:** Capture at deployment as controlled laboratory identity data. Any later change must be controlled, effective-dated, and must not alter historical reports/records.
	Details to be recorded:
	Legal Entity Name 
	Business/Display Name
	Laboratory Name
	Site Name
	Site Address
	Contact Information
	Accreditation Identification/Representation where applicable
	Effective From
	Effective To

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q2. What exact laboratory/site name should appear in records and reports?

**Reconciled Answer:** Same treatment as #1. Historical report identity must remain reconstructable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q3. Is v1 for exactly one physical laboratory/site?

**Reconciled Answer:** v1 represents exactly one physical laboratory/site.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q4. Are there any satellite rooms, sample collection points, field teams, branches, or temporary locations that v1 must represent?

**Reconciled Answer:** Out of v1 scope.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q5. If multiple physical locations exist, are they part of the same laboratory or separate entities?

**Reconciled Answer:** No multi-location model required for v1.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q6. Is the intended v1 user population still approximately 1–10 named users?

**Reconciled Answer:** Design baseline remains approximately 1–10 named users.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q7. Is the expected simultaneous writer count still approximately 1–5 users?

**Reconciled Answer:** Use 1–3 normal concurrent writers for operational workload testing; retain the stated higher stress scenario where appropriate.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q8. What is the expected number of samples per day, week, and month at launch?

**Reconciled Answer:** The launch workload shall be based on 100 samples per day as the approved launch workload baseline.

This operating workload shall remain distinct from:
- supported technical capacity;
- normal operating peak;
- stress-test workload; and
- supported concurrency.

The applicable operating-calendar assumption shall be documented separately so that daily, weekly, and monthly workload figures remain internally consistent.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q9. What is the expected number of test instances per sample?

**Reconciled Answer:** At launch 3-5 tests per sample, later it may increase to 50 or even 80 tests.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q10. What is the expected number of reports per day, week, and month?

**Reconciled Answer:** 1 report/sample should be the normal launch assumption, but the system should not structurally require exactly one report per sample because later report revisions/reissues/partial or grouped reporting may differ.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q11. What peak workload should the system be designed and tested for?

**Reconciled Answer:** 100 samples/day with 50 tests/sample.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q12. What data-retention period is required for controlled laboratory records?

**Reconciled Answer:** 10 years is the laboratory's current retention requirement then archived. "Archived" must mean controlled, retrievable, integrity-preserved archival—not deletion. Destruction only when separately authorized

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q13. What data-retention period is required for audit records?

**Reconciled Answer:** Same as #12. Preserve audit history and its relationship to the technical records.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q14. What data-retention period is required for reports and issued PDFs?

**Reconciled Answer:** Same as #12. Exact issued PDFs and their metadata must remain retrievable and verifiable during the retention period and controlled archive period.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q15. What historical paper/spreadsheet records must be migrated into v1?

**Reconciled Answer:** LabNexus shall support controlled, selective migration of approved historical paper/spreadsheet records where the laboratory determines that migration provides operational, traceability, quality, contractual, legal, or historical value.

Legacy records shall undergo documented discovery and assessment before migration. Only records approved for migration shall be migrated.

If the assessment determines that no suitable historical records require migration, the project shall formally record **No Migration Required.**

Historical data shall never be fabricated, reconstructed without evidence, or entered merely to satisfy a migration requirement.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q16. Which historical records will remain outside the LIMS?

**Reconciled Answer:** Historical records not approved for migration shall remain outside the LIMS under the laboratory's applicable controlled retention and document-management arrangements.
The Migration Assessment shall identify the record sets or categories remaining outside LabNexus and, where appropriate, their source location or reference.
Remaining outside the LIMS does not mean uncontrolled, unretained, or disposable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q17. Is historical migration required before go-live, after go-live, or optional?

**Reconciled Answer:** Historical migration shall be performed through a controlled phased process.
Historical records required for safe operational continuity, necessary traceability, or another formally approved go-live requirement shall be migrated before the affected operational use begins.
Additional approved historical migration may occur after go-live using the same controlled migration procedure.
Historical migration shall not silently convert historical records into ordinary contemporaneous LIMS records.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q18. Who decides whether an old paper/spreadsheet record is trustworthy enough to migrate?

**Reconciled Answer:** Migration suitability shall be governed as follows:
| **Activity**                    | **Responsible authority**             |
| ------------------------------- | ------------------------------------- |
| Discover legacy records         | Migration Assessor / Project Team     |
| Assess source quality           | Migration Assessor                    |
| Assess technical interpretation | Technical Authority                   |
| Approve migration suitability   | Laboratory Quality/Business Authority |
| Execute migration               | Authorized Migration Executor         |
| Verify migrated data            | Independent Verifier                  |
| Accept migration evidence       | Project/Quality Authority             |

The migration executor shall not be the sole authority for determining source suitability or accepting migration evidence.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q19. Must the LIMS support retrospective entry of historical records?

**Reconciled Answer:** LabNexus shall support controlled retrospective entry of approved historical information where required.
Retrospective entry shall distinguish the **historical event date/time** from the **actual LIMS entry timestamp** and shall preserve source/provenance, entering user, verification status, and applicable approval/evidence.
Ordinary users shall not be able to bypass workflow controls merely by entering a historical date.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q20. If historical records are entered, how will their original date, source, and provenance be recorded?

**Reconciled Answer:** A historical record shall preserve, where known/applicable:
- original event date/time;
- date precision or uncertainty where the exact date is unknown;
- LIMS entry timestamp;
- entering user;
- source type;
- source reference/location;
- source date or period;
- migration batch/reference;
- transformation/mapping performed;
- original source value where transformation occurred;
- verification status;
- verifier;
- approval/evidence reference;
- exceptions or unresolved ambiguity;
- migration/retrospective-entry status.

Where the source does not establish an exact date, the system shall preserve the known date precision or range and shall not invent a more precise dat

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q21. What functionality is explicitly outside v1 even if it might be useful later?

**Reconciled Answer:** The following explicitly outside v1 unless a later approved requirement changes scope:
	- Multi-tenancy
	- Multiple laboratory/site operation in one deployment
	- Cloud dependency
	- Public/customer portal
	- Public API ecosystem
	- ERP/accounting
	- Invoicing/account receivables/payments
	- Payroll/HR
	- Procurement system
	- Mobile LIMS application
	- Field sampling/field-team management
	- GPS/GIS workflow
	- Advanced instrument middleware/instrument integration
	- Enterprise data warehouse/BI
	- AI/ML decision systems
	- Advanced statistical QC beyond actual laboratory requirements
	- Complex inventory/warehouse management
	- Automated email/SMS dependent workflows
	- Cross-laboratory shared database
	- Plugin framework

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q22. What future capabilities must be architecturally possible but not implemented in v1?

**Reconciled Answer:** Category A - Laboratory expansion
	- Additional disciplines
	- Additional matrices
	- Additional methods
	- Additional MethodVersions
	- Additional TestDefinitions
	- Additional parameters
	- Additional calculation models
	- Additional report formats

	Category A - Operational expansion
	- Instrument/device integration
	- Automated data import
	- Additional barcode workflows
	- More sophisticated QC
	- Additional equipment controls
	- Customer-facing document exchange
	- Controlled external integrations

	Category A - Deployment expansion
	- Larger user population
	- Higher transaction volume
	- Additional independent laboratory deployments

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q23. Are there any regulatory, contractual, customer, or business requirements not represented in the Master Prompt?

**Reconciled Answer:** Accreditation and QMS
	- Current NABL certificate
	- Current NABL scope of accreditation
	- Current quality manual/system document
	- Applicable NABL policies
	- Applicable NABL specific criteria
	- Applicable laboratory SOPs
	- Applicable technical methods/standards
	- Current controlled forms/registers
	- Current quality procedures

	LIMS/data-management requirements
	- Electronic records
	- Record corrections
	- Audit trails
	- Electronic approvals/signatures
	- Access control
	- Data backup
	- Data restoration
	- System failure
	- Downtime operation
	- System changes
	- Software validation
	- Data transfer verification
	- Calculation verification
	- Report authorization

	Laboratory business requirements
	- Customer types
	- Customer-specific reporting requirements
	- Sample numbering conventions
	- Test/report numbering conventions
	- Turnaround-time rules
	- Commercial/rate rules
	- Report distribution rules
	- Confidentiality requirements
	- Authorized signatory rules
	- Customer communication rules
	- Record retention/legal-hold requirements

	Existing laboratory controls
	- Equipment calibration/verification policy
	- QC policy
	- Nonconforming-work policy
	- Corrective-action process
	- Rework/retest policy
	- Sample rejection policy
	- Sample disposal/return policy
	- Method-change policy
	- Emergency-change policy
	- Document-control policy
	- Training/competency records

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q24. Who has final authority to accept the scope baseline?

**Reconciled Answer:** Project owner.

## 1.2 Future disciplines

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q25. Which disciplines are definitely required at launch?

**Reconciled Answer:** - Solid Fuel (Coal)
	- Solid Biofuel

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q26. Which disciplines are only future possibilities?

**Reconciled Answer:** - Air
	- Water
	- Soil
	- Noise
	- Stack/Emissions
	- Other laboratory disciplines as requirements arise

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q27. Is Solid Fuel required in v1 from day one?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q28. Is Solid Biofuel required in v1 from day one?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q29. Which future discipline should be used for the first extensibility-validation exercise?

**Reconciled Answer:** Water

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q30. What real future test/method scenario should be used to prove that the core architecture is reusable?

**Reconciled Answer:** Water — Total Suspended Solids (TSS), using the laboratory-approved applicable method; IS 3025 (Part 17):2022 is a concrete Indian-standard example.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q31. Are there discipline-specific workflows that are already known to differ from the common workflow?

**Reconciled Answer:** No specific divergence should be assumed at present. Design around a common workflow plus configurable/controlled extensions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q32. Are there discipline-specific regulatory or reporting requirements that must be modeled now?

**Reconciled Answer:** Only the reusable mechanisms, not future discipline-specific rules.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q33. Are field sampling workflows required for any future discipline?

**Reconciled Answer:** Not for v1. Architecturally possible later.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q34. Are environmental monitoring programs required now or later?

**Reconciled Answer:** Later, unless a specific current laboratory requirement says otherwise.

---

# 2. Laboratory Governance and Decision Ownership

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q35. Who is the final business owner of the LIMS?

**Reconciled Answer:** The lims app name is LabNexus, the final business owner of the LIMS is the Project Owner / Laboratory Business Owner using it.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q36. Who is the laboratory quality authority for the LIMS?

**Reconciled Answer:** Laboratory Quality Authority, normally the Quality Manager or equivalent person formally responsible for the QMS.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q37. Who is the technical authority for methods and results?

**Reconciled Answer:** Laboratory Technical Authority, normally Technical Manager/Technical Head or equivalent competent person.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q38. Who is the system administrator?

**Reconciled Answer:** Designated LIMS System Administrator.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q39. Who can approve controlled configuration changes?

**Reconciled Answer:** Authorized Configuration Approver, with domain-appropriate Quality/Technical approval; proposer and implementer should not approve their own change.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q40. Who can approve emergency configuration changes?

**Reconciled Answer:** Pre-designated Alternate Emergency Approver with appropriate authority and competence.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q41. Who can approve production deployment?

**Reconciled Answer:** Designated Production/Release Authority, after successful verification/acceptance; business release authorization from Project Owner or delegate.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q42. Who can approve rollback or recovery after a failed update?

**Reconciled Answer:** Technical/Operations Authority may authorize immediate rollback to restore controlled operation; required business/quality review follows.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q43. Who can accept validation/UAT results?

**Reconciled Answer:** Project Owner / Laboratory Business Owner, with Quality Authority verifying validation evidence.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q44. Who can approve creation of new users?

**Reconciled Answer:** User Access Approver designated by laboratory management, typically Project Owner/Lab Head or delegate.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q45. Who can disable users?

**Reconciled Answer:** System Administrator executes; authorized management/quality/security authority may order immediate disablement.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q46. Who can assign roles?

**Reconciled Answer:** System Administrator executes only approved role assignments; approval comes from User Access Approver.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q47. Who can approve changes to SoD policy?

**Reconciled Answer:** Laboratory Quality Authority + Project Owner, with Technical Authority review of implementability.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q48. Who can approve accreditation-scope configuration?

**Reconciled Answer:** Laboratory Quality Authority as final approval, with Technical Authority concurrence.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q49. Who can approve report templates?

**Reconciled Answer:** Technical Authority for technical correctness and Quality Authority for controlled-document approval.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q50. Who owns the retention policy?

**Reconciled Answer:** Laboratory Quality Authority, with Project Owner/business authority for final policy acceptance.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q51. Who owns backup/recovery procedures?

**Reconciled Answer:** Technical/Operations Authority; System Administrator executes the procedures.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q52. Who owns the controlled project documents?

**Reconciled Answer:** Project Owner owns the project baseline; a designated Document/Project Controller maintains repository state.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q53. What happens if the designated approver is unavailable?

**Reconciled Answer:** Use the pre-approved alternate-approver path. No ad-hoc substitution.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q54. What is the approved alternate-approver path?

**Reconciled Answer:** Named alternate with equivalent authority/competence, active authority period, no prohibited conflict, and full audit trail.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q55. What counts as an emergency for configuration or operational decisions?

**Reconciled Answer:** A situation requiring immediate action to protect data integrity, security, controlled laboratory operation, report correctness, or recovery from a failed/unsafe change where normal approval cannot be completed in time.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q56. Who is permitted to declare an emergency?

**Reconciled Answer:** Designated Emergency Authority; recommend Quality Authority or Technical/System Authority depending on the emergency type.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q57. What must be documented when an emergency path is used?

**Reconciled Answer:** Reason, urgency, unavailable normal path, affected object/configuration, risk, authorizer, executor, exact change, start/end time, evidence, post-change verification, expiry, and retrospective review.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q58. Who performs retrospective review of emergency actions?

**Reconciled Answer:** Quality Authority + relevant Technical Authority; security incidents additionally reviewed by the responsible system/security authority.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q59. How often must emergency use be reviewed?

**Reconciled Answer:** Monthly operational review, plus immediate review of any high-risk event; periodic management trend review can be quarterly.

---

# 3. Frozen Architecture — Confirmation Questions

These are not intended to reopen the baseline. They are confirmation questions to detect contradictions before coding starts.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q60. Is React + TypeScript + Vite + MUI still the approved frontend stack?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q61. Is FastAPI + Python still the approved backend stack?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q62. Is SQLAlchemy 2.x still the approved ORM?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q63. Is SQLite still the approved v1 database?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q64. Is Alembic still the approved migration tool?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q65. Is Argon2id plus server-side sessions still the approved authentication architecture?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q66. Is RBAC plus backend authorization plus per-TestInstance SoD still the approved authorization model?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q67. Is Caddy still the approved reverse proxy?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q68. Is Jinja2 plus HTML/CSS plus Chromium still the approved reporting pipeline?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q69. Are pytest and Playwright still the approved testing tools?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q70. Are Code 128 and QR still the approved barcode formats?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q71. Is Windows 11 Pro and/or Windows Server still the approved deployment target?

**Reconciled Answer:** Yes — Windows 11 Pro and Windows Server are approved deployment targets; exact production OS is selected during deployment planning.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q72. Is the modular-monolith architecture still approved?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q73. Is the single-host architecture still approved?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q74. Is offline-first operation still mandatory?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q75. Is the rule that the live SQLite database must remain on local fixed storage still mandatory?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q76. Is the rule against NAS/SMB live-database hosting still mandatory?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q77. Is the no-cloud-dependency requirement still mandatory?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q78. Is the no-multi-tenancy decision still valid for v1?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q79. Is the no-public-API boundary still valid for v1?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q80. Is the commercial boundary still limited to charge calculation inside LIMS, with invoicing/accounting/payments outside the system?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q81. Is documentation-as-code still mandatory?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q82. Is the repository the authoritative source of project state?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q83. Is explicit task authorization before coding still mandatory?

**Reconciled Answer:** Yes

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q84. Is the frozen architecture change process agreed and operationally understood?

**Reconciled Answer:** Yes — the architecture-change process is agreed and understood; any approved change must be recorded in the authoritative repository and affected baselines/contracts updated before implementation.

---

# 4. Laboratory Operating Model

## 4.1 Daily operation

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q85. What does a normal working day in the laboratory look like?

**Reconciled Answer:** Receipt → Registration → Identification → Test Allocation → Testing → Observations → Calculation → Review → Verification → Approval → Report → Delivery → Retention/Archive.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q86. Who receives samples?

**Reconciled Answer:** Authorized Sample Receiving/Laboratory User.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q87. Who registers samples?

**Reconciled Answer:** Authorized Sample Receiving/Registration User.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q88. Who identifies or labels samples?

**Reconciled Answer:** Authorized Sample Receiving/Registration User.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q89. Who allocates samples to tests?

**Reconciled Answer:** Authorized Laboratory Coordinator/Technical User.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q90. Who performs tests?

**Reconciled Answer:** Authorized Analyst

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q91. Who records observations?

**Reconciled Answer:** Analyst performing the TestInstance.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q92. Who performs calculations?

**Reconciled Answer:** Controlled LIMS calculation engine using approved FormulaVersions; analyst supplies/reviews required inputs.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q93. Who reviews results?

**Reconciled Answer:** Authorized Technical Reviewer

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q94. Who verifies results?

**Reconciled Answer:** Authorized Technical Verifier

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q95. Who approves results?

**Reconciled Answer:** Authorized Approver / Authorized Signatory

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q96. Who issues reports?

**Reconciled Answer:** Authorized Report-Issuing User after approval

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q97. Who delivers reports?

**Reconciled Answer:** Authorized Report/Administrative User

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q98. Who performs archival/retention activities?

**Reconciled Answer:** Designated Records/Quality User

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q99. Can one person perform multiple roles on the same day?

**Reconciled Answer:** Permitted, subject to authorization and TestInstance-level SoD.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q100. Can the same person perform multiple stages on different TestInstances?

**Reconciled Answer:** Permitted, subject to authorization and policy.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q101. Which actions require two-person control?

**Reconciled Answer:** Required for designated high-risk controlled decisions and wherever approved laboratory SoD/QMS policy requires independent control.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q102. Which actions can be performed by one authorized person?

**Reconciled Answer:** Ordinary authorized actions where no SoD or two-person requirement applies.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q103. Which actions must never be performed by the same person on the same TestInstance?

**Reconciled Answer:** Analyst + Review
    Analyst + Verification
    Analyst + Approval.
    Other combinations are policy-controlled unless explicitly blocked.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q104. Are there informal laboratory practices that must be made explicit in the system?

**Reconciled Answer:** At minimum, an Analyst shall not Review, Verify, or Approve the same TestInstance. Other combinations shall be determined by the approved TestInstance-level SoD policy. Hard blocks cannot be bypassed.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q105. Are there paper forms or registers that remain legally or operationally required after go-live?

**Reconciled Answer:** Paper forms/registers may remain after go-live only where required by law, accreditation/QMS procedure, technical method, operational necessity, or an approved business decision. Where an existing paper control is replaced by LIMS, the electronic control must be formally assessed and validated as the replacement.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q106. Which existing manual controls must be preserved or replaced with equivalent electronic controls?

**Reconciled Answer:** Must be mapped to equivalent or stronger electronic controls before replacement.
	| --------------------------- | ------------------------------------------------------------ |
	| Current/manual control      | LIMS replacement                                             |
	| --------------------------- | ------------------------------------------------------------ |
	| Sample register             | Sample registration + immutable lifecycle/audit              |
	| Sample handwritten ID       | System-generated unique sample identifier + controlled label |
	| Test allocation register    | TestRequest/TestInstance workflow                            |
	| Analyst worksheet           | Observation + CalculationRun + Result                        |
	| Manual calculation sheet    | Controlled FormulaVersion + CalculationRun                   |
	| Reviewer signature          | Review event                                                 |
	| Verifier signature          | Verification event                                           |
	| Approver signature          | Approval event                                               |
	| Report register             | Report/ReportRevision                                        |
	| Report PDF folder           | Controlled DocumentVersion                                   |
	| Correction register         | ResultRevision + audit/correction workflow                   |
	| Configuration register      | Controlled configuration + proposal/approval history         |
	| Equipment validity register | Equipment status/calibration/eligibility                     |
	| Audit log/register          | Application audit architecture                               |
	| Backup register             | Backup evidence + validation/restore records                 |
	| --------------------------- | ------------------------------------------------------------ |

## 4.2 Work outside the laboratory

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q107. Are samples collected by the laboratory?

**Reconciled Answer:** No field-sampling workflow in v1. Samples are received by the laboratory from customers/authorized external sources unless a specific launch requirement says otherwise.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q108. Are samples collected by customers or third parties?

**Reconciled Answer:** Yes, this should be supported as the normal v1 assumption.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q109. Are field observations or field measurements required?

**Reconciled Answer:** No, not in v1.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q110. Must field activity be recorded in the LIMS?

**Reconciled Answer:** No field-activity module in v1.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q111. Is offline/mobile field entry required in v1?

**Reconciled Answer:** No, not in v1.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q112. Are chain-of-custody records required?

**Reconciled Answer:** Not assumed as a universal v1 requirement; determine based on actual sample/customer/QMS requirements.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q113. Are sample transport conditions required to be captured?

**Reconciled Answer:** Capture where relevant to sample integrity/method/customer requirements.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q114. Are receipt temperatures or other transport conditions required?

**Reconciled Answer:** Configurable/capturable where applicable; do not require universally.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q115. Are sample containers or preservation conditions relevant?

**Reconciled Answer:** Yes, the data model should be capable of recording them where applicable, but not every Solid Fuel/Solid Biofuel sample needs those fields.

---

# 5. Customer, Project, Contract, and Request Model

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q116. What is the exact definition of a Customer?

**Reconciled Answer:** A Customer is the external person or legal/business entity that requests, contracts for, or receives laboratory services and to whom the laboratory's commercial/administrative relationship belongs.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q117. Can one Customer have multiple sites or addresses?

**Reconciled Answer:** Yes. One Customer can have multiple sites/locations and addresses.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q118. Can one Customer have multiple contacts?

**Reconciled Answer:** Yes. One Customer can have multiple contacts, with contact roles/statuses.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q119. What customer fields are mandatory?

**Reconciled Answer:** Customer ID, customer/legal name, active/inactive status, and minimum identity/address information required by the laboratory. Other commercial/contact fields should be conditional.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q120. Are customer identifiers internally assigned or externally supplied?

**Reconciled Answer:** Internal Customer ID assigned by LIMS. External customer codes/IDs may also be stored separately.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q121. Can customer names be changed after records exist?

**Reconciled Answer:** Yes, but as a controlled master-data change; do not overwrite the historical identity used by issued records.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q122. If a customer name changes, should historical reports preserve the original displayed name?

**Reconciled Answer:** Yes, absolutely.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q123. What is the definition of a Project?

**Reconciled Answer:** Project is a controlled grouping of related laboratory work undertaken for a Customer, normally representing a defined engagement, contract, job, program, or continuing body of work.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q124. Is a Project always linked to a Customer?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q125. Can one Project have multiple samples?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q126. Can one Project contain multiple requests?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q127. Can one Customer have multiple contracts?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q128. Can a Contract exist without a Project?

**Reconciled Answer:** Yes. A Contract may exist independently and support one or more Projects/Requests.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q129. What commercial information must the LIMS keep?

**Reconciled Answer:** Rates, rate basis, applicable customer-specific rates, calculated charges, approved request-level overrides, commercial references, and charge history where required.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q130. What information stays outside the LIMS?

**Reconciled Answer:** Invoices, accounts receivable, payments, tax/accounting ledger, banking, and full financial accounting.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q131. Is pricing required at request time, test time, report time, or invoice time?

**Reconciled Answer:** Request acceptance / request-line creation, using the applicable effective rate; charge snapshots must remain historically stable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q132. How are rates selected?

**Reconciled Answer:** Controlled precedence using active effective-dated standard/customer-specific rates, with approved request override where permitted.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q133. Are rates effective-dated?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q134. Are customer-specific rates required?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q135. Who can change rates?

**Reconciled Answer:** Authorized commercial/configuration authority; System Administrator implements only approved changes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q136. Can rates be overridden for a specific request?

**Reconciled Answer:** Yes, where authorized, with reason, actor, timestamp and audit trail.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q137. If rates change later, must historical charges remain unchanged?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q138. What is the exact definition of a Request?

**Reconciled Answer:** A Request is a customer's controlled instruction/order for one or more laboratory services on one or more samples, including requested tests and applicable commercial/technical information.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q139. Can one request contain multiple samples?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q140. Can one request contain multiple TestDefinitions?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q141. Can a request be cancelled after work starts?

**Reconciled Answer:** Yes, through controlled cancellation. It must not erase started/completed TestInstances or historical records.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q142. What happens to charges when a request is cancelled?

**Reconciled Answer:** Retain charges already legitimately incurred; unstarted work is cancelled; cancellation fees/other commercial rules depend on approved policy.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q143. Can a customer request a specific method?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q144. Can the laboratory substitute an approved method?

**Reconciled Answer:** Yes, only under controlled technical rules and where permitted by applicable requirements/accreditation/customer agreement.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q145. Who can approve method substitution?

**Reconciled Answer:** Laboratory Technical Authority, with Quality/customer approval where the governing requirement requires it.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q146. Must the original customer request remain visible after changes?

**Reconciled Answer:** Yes. Original request and subsequent amendments must remain reconstructable.

---

# 6. Sample Intake and Sample Identity

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q147. What is the exact definition of a Sample?

**Reconciled Answer:** A uniquely identified physical/material specimen received or otherwise placed under the laboratory's responsibility for one or more laboratory activities.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q148. What makes a Sample uniquely identifiable?

**Reconciled Answer:** LIMS-generated immutable Sample ID is the authoritative identity.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q149. What is the internal sample number format?

**Reconciled Answer:**  All business identifiers (samples, customers, equipment, etc.) are allocated from a centralized `number_sequence` registry defining prefix, padding, increment, and reset policy per sequence. Allocation is atomic (single-statement UPDATE ... RETURNING); gaps are acceptable for sample numbers.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q150. What is the external/customer sample identifier format?

**Reconciled Answer:** Retain the approved rule that the **current authoritative** customer/external Sample ID is globally unique across the deployment. Historical provenance-only submitted/source values are retained but are not live identifiers.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q151. Which identifier is printed on the physical sample label?

**Reconciled Answer:** Retain the approved rule that the **current authoritative** customer/external Sample ID is globally unique across the deployment. Historical provenance-only submitted/source values are retained but are not live identifiers.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q152. Can the customer supply duplicate sample identifiers?

**Reconciled Answer:** Retain the approved rule that the **current authoritative** customer/external Sample ID is globally unique across the deployment. Historical provenance-only submitted/source values are retained but are not live identifiers.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q153. How are duplicate external identifiers handled?

**Reconciled Answer:** Retain the approved rule that the **current authoritative** customer/external Sample ID is globally unique across the deployment. Historical provenance-only submitted/source values are retained but are not live identifiers.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q154. What information must be captured at receipt?

**Reconciled Answer:** Customer/source, external ID, receiving date/time, received-by user, packaging/container condition, physical condition, quantity where relevant, accompanying documents, apparent sample description, deviations, receipt decision.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q155. What information must be captured at registration?

**Reconciled Answer:** Internal Sample ID, customer/project/request link, sample description/matrix, external ID, receipt data, required tests/request links, acceptance status, storage requirements/location where applicable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q156. Is sample receipt date/time mandatory?

**Reconciled Answer:** Mandatory

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q157. Is sample collection date/time mandatory?

**Reconciled Answer:** Conditional mandatory where supplied, technically required, or relevant to method/holding-time requirements

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q158. Is sample receipt condition mandatory?

**Reconciled Answer:** Mandatory assessment, with detailed condition data conditional

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q159. Which rejection reasons are required?

**Reconciled Answer:** - Unidentified / ambiguous identity
	- Missing required identification
	- Insufficient quantity
	- Improper container
	- Damaged container
	- Leakage
	- Contamination / suspected contamination
	- Improper preservation
	- Out-of-range transport/storage condition
	- Exceeded applicable holding time
	- Missing required information/documentation
	- Sample unsuitable for requested test
	- Customer instruction not satisfied
	- Other approved reason

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q160. Who may reject a sample?

**Reconciled Answer:** Sample rejection may be performed by an authorized Sample Receiving user when a predefined objective rejection criterion is met; technical/discretionary rejection should require appropriate technical authority.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q161. What happens after sample rejection?

**Reconciled Answer:** Rejected sample is placed in a controlled Rejected state; reason, evidence, actor, date/time and customer communication/decision are retained. No downstream testing may proceed unless a permitted controlled disposition changes the status.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q162. Can a rejected sample be re-opened?

**Reconciled Answer:** Yes, but only through a controlled review/disposition process; not by simply changing Rejected back to Accepted.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q163. Can a sample be conditionally accepted?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q164. Who can approve conditional acceptance?

**Reconciled Answer:** Conditional acceptance should require an authorized person with the competence/authority defined by laboratory policy, normally the Technical Authority or designated sample-acceptance authority.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q165. What sample condition checks are required?

**Reconciled Answer:** - Identity/label
	- Packaging
	- Container
	- Integrity/damage
	- Quantity
	- Material/sample description
	- Preservation, if applicable
	- Temperature, if applicable
	- Transport condition, if applicable
	- Collection information
	- Required documentation
	- Holding-time eligibility, if applicable
	- Visible contamination/degradation
	- Customer instructions

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q166. Are sample quantity/volume/mass requirements enforced?

**Reconciled Answer:** Yes, where required.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q167. Are sample preservation requirements enforced?

**Reconciled Answer:** Yes, where applicable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q168. Are container requirements enforced?

**Reconciled Answer:** Yes, where applicable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q169. Are sample storage locations tracked?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q170. Are sample storage conditions tracked?

**Reconciled Answer:** Yes, where applicable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q171. Is sample disposal tracked?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q172. Who authorizes disposal?

**Reconciled Answer:** The prior `Yes` answer is invalid. The laboratory must designate the authority who authorizes sample disposal; that authority and the disposal workflow must be captured in the Retention / Archive / Disposal Authority Matrix before operational use.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q173. What evidence is retained for disposal?

**Reconciled Answer:** - Sample ID
	- Disposition
	- Date/time
	- Authorized by
	- Executed by
	- Reason
	- Quantity/disposition where relevant
	- Method of disposal
	- Witness where required
	- Related retention rule
	- Certificate/evidence reference where applicable

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q174. Are sample portions/aliquots/sub-samples required?

**Reconciled Answer:** Yes — the architecture should support them.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q175. If yes, how are portions linked to the parent sample?

**Reconciled Answer:** SamplePortion.parent_sample_id → Sample.id

	A portion should retain:
	- portion ID
	- parent Sample
	- created date/time
	- created by
	- quantity/unit where needed
	- purpose/use
	- status
	- location
	- disposition

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q176. Are sample splits or composites required?

**Reconciled Answer:** Sample splits, composites, and derived-sample lineage are not required for v1 and are out of v1 scope.
V1 shall support the required physical sample identity and traceability model without implementing split/composite workflows.
Any future introduction of splits, composites, derived samples, relabelling lineage, or related identity transformations shall be handled as a controlled architectural change.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q177. If a composite sample is created, how are source samples recorded?

**Reconciled Answer:** Composite samples are out of v1 scope.
V1 shall not implement composite-sample creation or source-sample lineage.
If composites are introduced in a future controlled change, the source-sample lineage model shall be formally defined and approved before implementation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q178. Can one physical sample map to multiple Sample records?

**Reconciled Answer:** V1 shall not provide sample-lineage capability in which one physical sample maps to multiple Sample records.
V1 does not implement sample splitting, derived samples, or one-to-many physical-sample lineage.
The v1 Sample model shall maintain the defined physical sample identity without introducing implicit multiple-record mappings.
Any future requirement for such mappings shall be addressed through a controlled architectural change.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q179. How are relabeling and identity corrections handled?

**Reconciled Answer:** V1 does not implement split/composite or broader physical-sample lineage.
Identity corrections and relabelling, where required by the v1 sample workflow, shall be handled through controlled correction and audit mechanisms without silently replacing historical identity information.
Any future requirement for lineage-aware relabelling or identity transformation shall require a controlled architectural change.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q180. What is the process when a sample identity is discovered to be wrong after testing begins?

**Reconciled Answer:** If a sample identity is suspected to be incorrect after testing has started, the system shall trigger a controlled investigation and immediately pause all affected tests.
The affected work shall remain blocked pending authorized investigation and disposition.
The original recorded identity, evidence, discovery event, actors, affected TestInstances, and subsequent disposition shall remain historically traceable.
No user shall resolve the issue by silently editing the original Sample identity.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q181. What sample fields are allowed to change after registration?

**Reconciled Answer:** Generally editable under normal rules until they become operationally relied upon, for example:
	- Non-critical description
	- Administrative notes
	- Internal handling notes
	- Planned storage location
	- Non-critical customer contact information
	- Some scheduling/administrative metadata
	subject to audit where appropriate.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q182. Which sample fields become immutable after a defined stage?

**Reconciled Answer:** - Internal Sample ID
	- Original external/customer Sample ID
	- Receipt date/time
	- Receipting actor
	- Original receipt condition
	- Initial acceptance/rejection decision
	- Collection data once relied upon
	- Sample origin/source
	- Sample identity
	- Material/matrix identity
	- Sample lineage
	- Critical preservation/transport facts

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q183. Which changes require correction/reopen rather than normal editing?

**Reconciled Answer:** - Sample identity
	- Customer/sample association
	- Test eligibility
	- Applicable MethodVersion
	- Accreditation applicability
	- Test conditions
	- Sample acceptance status
	- Sample integrity
	- Holding-time compliance
	- Observation/result validity
	- Report content
	- Traceability

---

# 7. Sample Allocation and Chain of Custody

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q184. Is internal sample allocation required?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q185. What exactly is being allocated: physical sample, aliquot, portion, or TestInstance?

**Reconciled Answer:** Primarily a Sample or SamplePortion to a TestInstance. Allocation is a laboratory work-control relationship, not necessarily a physical transfer.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q186. Must each allocation be traceable to a person, location, and time?

**Reconciled Answer:** Yes. Allocation and significant physical movement should record actor, timestamp and location/state.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q187. Are sample transfers between rooms or storage locations required?

**Reconciled Answer:** Yes, where applicable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q188. Are custody handovers required?

**Reconciled Answer:** Supported, but not mandatory for every internal movement.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q189. Is chain-of-custody legally or procedurally required for any test type?

**Reconciled Answer:** Not established as a universal v1 requirement. Must be determined per applicable test/customer/regulatory requirement.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q190. What events constitute a custody transfer?

**Reconciled Answer:** A controlled change in the person/organizational responsibility for the physical sample/portion, or an externally relevant handover. Mere movement within the same person's control is not necessarily a custody transfer.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q191. Who can record a transfer?

**Reconciled Answer:** Authorized users responsible for sample handling/transfer.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q192. Who can receive custody?

**Reconciled Answer:** Authorized users designated for the receiving location/activity.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q193. What happens if custody is interrupted or undocumented?

**Reconciled Answer:** Mark the chain/transfer as exceptional or unresolved, prevent affected controlled use where integrity could be affected, investigate and document disposition.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q194. Are storage locations controlled master data?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q195. Must the system prevent use of a sample that is not in an eligible state/location?

**Reconciled Answer:** Yes, where the configured business rule requires it. Backend must enforce it.

---

# 8. Test Request, Test Assignment, and TestInstance

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q196. What is the exact business meaning of a TestRequest?

**Reconciled Answer:** A requested laboratory service/test representing what the customer/laboratory has requested for a Sample.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q197. What is the exact business meaning of a TestInstance?

**Reconciled Answer:** A specific controlled execution occurrence of a TestDefinition against a Sample/Portion, with its own assignment, execution, observations, calculations, result, review, verification and approval history.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q198. Can one TestRequest create multiple TestInstances?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q199. Under what conditions are repeat TestInstances created?

**Reconciled Answer:** A new TestInstance shall be created only when the laboratory workflow determines that a distinct execution occurrence is required.

The creation reason shall be explicitly classified, at minimum distinguishing:
- repeat;
- replicate;
- retest;
- rework;
- correction/re-execution;
- other approved execution reason.

The new TestInstance shall retain a traceable relationship to the originating TestInstance/TestRequest and shall not overwrite the history of the prior execution.

Exact creation conditions for each category shall be defined in the **Master State / Execution Semantics Decision Table.**

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q200. How are repeats distinguished from corrections?

**Reconciled Answer:** A **repeat** represents a new execution of the test because another measurement/execution is required under an approved laboratory rule. It creates a distinct TestInstance and preserves the prior execution.
A **correction** represents a controlled correction to an existing technical record/result or its provenance because the existing record is determined to be incorrect or incomplete.
A correction shall not be represented merely as an ordinary repeat, and a repeat shall not overwrite the original TestInstance/result history.
The reason classification shall be mandatory where the distinction affects workflow, review, verification, approval, reporting, or traceability.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q201. How are re-tests distinguished from routine replicate measurements?

**Reconciled Answer:** A **replicate** is a planned or method-required repeated measurement/execution performed as part of the defined analytical procedure or QC strategy.
A **retest** is a new test execution initiated because the prior test/result requires another execution under an approved reason, such as an invalid or failed execution, technical concern, authorized disposition, or other defined laboratory condition.
Replicates and retests shall therefore have distinct reason classifications and traceability.
Neither may silently replace the original execution history.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q202. Can a TestInstance be cancelled independently of the Sample?

**Reconciled Answer:** Yes. A TestInstance may be cancelled independently of the Sample.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q203. Can a Sample remain active while one TestInstance is cancelled?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q204. Can a TestInstance be reopened after approval?

**Reconciled Answer:** A TestInstance may be reopened after approval only through a controlled reopening process.

Reopening shall require:
- an authorized requester;
- documented reason;
- authorization according to the applicable workflow/policy;
- preservation of the prior approved state;
- identification of affected technical and report records;
- required rework/correction;
- renewed review, verification, and approval where affected;
- complete audit history.

Reopening shall never modify or erase the historical approved state.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q205. Who may create a TestInstance?

**Reconciled Answer:** TestInstance creation should be system-controlled and permitted to authorized users/services when a valid TestRequest and TestDefinition exist.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q206. Who may assign a TestInstance to an analyst?

**Reconciled Answer:** Authorized Laboratory Coordinator/Technical User may assign a TestInstance to an eligible analyst.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q207. Can an analyst assign work to themselves?

**Reconciled Answer:** An analyst may assign work to themselves only if the laboratory's policy explicitly permits self-assignment and doing so does not create a prohibited SoD condition.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q208. Can a TestInstance have multiple analysts?

**Reconciled Answer:** Yes, a TestInstance may have multiple analysts where the approved test procedure requires/permits multiple responsible performers.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q209. Is there one primary analyst or multiple responsible analysts?

**Reconciled Answer:** Recommend one primary responsible analyst, with zero or more additional contributors/participants.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q210. Can assignment be changed after execution begins?

**Reconciled Answer:** Assignment may be changed before or during execution under controlled conditions. Changes after execution begins must retain history and reason.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q211. What happens to previous assignment history?

**Reconciled Answer:** Previous assignment history remains permanently traceable; it is never overwritten.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q212. Are assignment queues required?

**Reconciled Answer:** Yes, assignment/work queues are required.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q213. How is workload prioritized?

**Reconciled Answer:** Workload is prioritized using controlled priority + due date + operational rules; priority must not be an arbitrary analyst decision.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q214. Is due date tracking required?

**Reconciled Answer:** Yes, due-date tracking is required.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q215. Are turnaround-time rules required?

**Reconciled Answer:** Yes, TAT rules are required.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q216. What events pause or restart turnaround time?

**Reconciled Answer:** TAT starts/stops from controlled lifecycle events; pauses occur for configured external/customer/laboratory hold conditions and resume on the defined release event.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q217. Are overdue TestInstances escalated?

**Reconciled Answer:** Yes, overdue TestInstances should be visibly escalated.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q218. Who can change priority?

**Reconciled Answer:** Priority may be changed only by authorized users; reason and audit history required for significant changes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q219. Are customer priority requests supported?

**Reconciled Answer:** Yes, customer priority requests may be captured, but they do not automatically override laboratory priority or technical controls.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q220. What is the exact lifecycle of a TestInstance?

**Reconciled Answer:** The TestInstance lifecycle shall be implemented as a controlled state machine rather than a collection of freely editable status values.

At minimum, the normal path shall support:
Created/Planned → Assigned → In Execution → Observations/Calculations → Result Ready → Pending Review → Reviewed → Pending Verification → Verified → Pending Approval → Approved

Controlled exceptional states/transitions shall support:
- Hold;
- Rework;
- Retest;
- Repeat;
- Correction;
- Reopen;
- Cancellation;
- Failed review;
- Failed verification;
- Failed approval;
- other approved exceptional disposition.

The lifecycle shall distinguish normal forward progression from exceptional transitions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q221. What transitions are legal?

**Reconciled Answer:** Every TestInstance state shall have an explicitly defined set of permitted outgoing transitions in the authoritative Master State / Transition Matrix.

A transition shall be permitted only when:
- the current state allows it;
- the actor is authorized;
- required prerequisites are satisfied;
- required SoD rules are satisfied;
- required reason, evidence, or approval is present;
- the transition is permitted for the applicable TestDefinition/workflow configuration.

The backend/domain layer shall be authoritative for transition enforcement.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q222. What transitions are forbidden?

**Reconciled Answer:** Any transition not explicitly defined as legal in the authoritative Master State / Transition Matrix shall be forbidden.

The system shall prevent uncontrolled transitions that:
- bypass required Review, Verification, or Approval;
- move backward through the normal workflow without an authorized reopen/rework mechanism;
- alter an approved technical state in place;
- bypass required SoD controls;
- create a result without required observations/calculations;
- approve work without satisfying required prerequisites;
- turn a cancelled/invalid execution into a normal completed execution without controlled disposition;
- silently erase previous state history.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q223. Which transitions require a reason?

**Reconciled Answer:** A reason shall be mandatory for transitions that represent an exception, deviation, reversal, cancellation, correction, or other non-routine action.

At minimum:
| Transition/Event              | Reason                                       |
| ----------------------------- | -------------------------------------------- |
| Hold                          | Required                                     |
| Rework                        | Required                                     |
| Retest                        | Required                                     |
| Repeat                        | Required  where not inherently method-driven |
| Reopen                        | Required                                     |
| Correction                    | Required                                     |
| Cancellation                  | Required                                     |
| Rejection/failure disposition | Required                                     |
| Identity-related disposition  | Required                                     |
| Exceptional approval/recovery | Required                                     |

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q224. Which transitions require another authorized person?

**Reconciled Answer:** The Master State / Transition Matrix + Execution Semantics Decision Table shall identify transitions that require another authorized person.

At minimum, a second authorized person shall be required where the transition involves:
- Review, Verification, or Approval under the approved SoD policy;
- reopening an approved TestInstance;
- correction approval where the correction affects an approved technical result;
- exceptional or policy-controlled SoD actions requiring independent authorization;
- emergency exceptions to policy-controlled actions, where such exceptions are permitted.

Routine workflow transitions shall not require unnecessary dual approval unless the approved workflow or SoD policy explicitly requires it.

The required second person, authorization level, independence requirement, and applicable SoD restriction shall be explicitly defined in the authoritative matrix.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q225. Which transitions generate audit events?

**Reconciled Answer:** The following events shall generate immutable audit evidence:
- every successful TestInstance state transition;
- every controlled exceptional transition;
- every reopen, rework, retest, repeat, correction, hold, and cancellation event;
- every Review, Verification, Approval, rejection, failure, revocation, or equivalent approval-chain event;
- every authorization-sensitive transition;
- every transition requiring a reason or additional authorization.

Rejected or denied transition attempts involving authorization, SoD, or other controlled restrictions shall also be recorded where required by the audit/security model.

The audit event shall identify, as applicable, the TestInstance, prior state, new state, actor, timestamp, action, reason, authorization context, and related evidence/reference.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q226. Which states are terminal?

**Reconciled Answer:** Replace strict terminal wording with **normal forward terminal state** where controlled reopening exists.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q227. Which states allow rework?

**Reconciled Answer:** Controlled rework shall be permitted only from states where the technical work may legitimately require correction or additional execution.
At minimum, rework shall be available for applicable execution and failed-review/failed-verification conditions where the underlying work can be corrected without creating an uncontrolled history change.
Post-approval changes shall not use ordinary rework. They shall proceed through the controlled **Reopen / Correction process.**
Rework shall preserve the prior state, reason, actor, timestamp, affected records, and subsequent re-execution history.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q228. Which states allow reopening?

**Reconciled Answer:** Reopening shall be a controlled exceptional transition rather than a general backward status change.
For v1, the primary reopening state shall be **Approved.**
A TestInstance may move from Approved into the authorized correction/rework path only through a controlled reopen process with reason, authorization, audit, and preservation of the prior approved state.
Pre-approval problems shall normally use the applicable rework/correction transition rather than the formal Reopen transition.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q229. Which states allow cancellation?

**Reconciled Answer:** TestInstance cancellation shall be a controlled transition available only while the TestInstance has not reached an approved final state and where cancellation is permitted by the applicable workflow.

Cancellation may be permitted from appropriate pre-approval states such as:
- Created/Planned;
- Assigned;
- In Execution;
- Hold;
- Rework;
- other explicitly authorized pre-approval states.

Cancellation after execution has begun shall preserve all work already performed and require a reason and appropriate authorization.

An Approved TestInstance shall not be returned to Cancelled through an ordinary cancellation transition; any post-approval disposition shall use the controlled reopen/correction/report-governance path.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q230. Which state transitions are reversible?

**Reconciled Answer:** A TestInstance transition shall be considered reversible only where the Master State / Transition Matrix explicitly defines a valid controlled return path.

Reversibility shall not mean editing the previous state or deleting the transition history.

Examples of controlled reversible behavior may include:
- Hold → permitted working state;
- failed Review/Verification → controlled Rework/Correction path;
- controlled assignment changes;
- other explicitly approved workflow returns.

Approved, Cancelled, or other normal forward terminal states shall not be reversed by simply editing the status.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q231. Which transitions are irreversible?

**Reconciled Answer:** A transition shall be considered irreversible at the historical-event level once recorded: prior transition events shall never be deleted or rewritten.

At the workflow level, the following shall be treated as normal forward terminal states for v1:
- Approved;
- Cancelled, where the applicable cancellation path has completed.

Neither state may be changed directly into an earlier ordinary workflow state.

Where a later action is legitimately required, it shall use the appropriate controlled mechanism such as Reopen, Correction, or a new TestInstance rather than reversing the historical event.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q232. What is the definition of a Method?

**Reconciled Answer:** Method is the stable identity of a defined laboratory analytical or testing methodology, independent of the specific revision or edition used at a particular point in time.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q233. What is the definition of a MethodVersion?

**Reconciled Answer:** MethodVersion is a controlled technical version of a Method that defines the exact method reference, edition/revision, laboratory implementation, technical instructions, applicability, and effective period under which laboratory work may be performed.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q234. What identifies one Method uniquely?

**Reconciled Answer:** Globally unique internal Method ID; additionally a controlled human-readable Method Code.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q235. What identifies one MethodVersion uniquely?

**Reconciled Answer:** Globally unique internal MethodVersion ID plus unique version designation within its Method.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q236. Which fields belong to Method versus MethodVersion?

**Reconciled Answer:** Method and MethodVersion shall have clearly separated responsibilities.

**Method** represents the stable identity of the laboratory methodology, independent of a particular edition/revision.

**MethodVersion** represents the controlled technical version actually applicable to laboratory work. It contains the exact edition/revision, technical implementation, applicability, effective period, approval/evidence references, and other version-specific attributes.

The authoritative relationship is:
**Method → MethodVersion**

Method shall not contain mutable fields that actually describe one specific technical revision. MethodVersion shall contain the properties whose meaning may change between controlled revisions.
Do not add redundant predecessor/successor/version-history columns merely for convenience. Historical relationships shall be reconstructed through the version records and effective history.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q237. How is an external standard/method reference represented?

**Reconciled Answer:** Structured fields: issuing organization, standard/method number, title, edition/year, amendment/corrigendum, relevant section/clause, source/document reference.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q238. How is a method edition or revision represented?

**Reconciled Answer:** Represented explicitly on MethodVersion, never by overwriting the previous edition.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q239. When does a method change require a new MethodVersion?

**Reconciled Answer:** Any controlled technical change that can affect how the laboratory performs the method, evaluates data, calculates results, interprets results, determines applicability, uses required equipment/materials, or meets defined performance requirements shall create a new MethodVersion. When there is doubt whether a change affects technical meaning, treat it as a new MethodVersion.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q240. Can a MethodVersion be edited after it is effective?

**Reconciled Answer:** No substantive editing. Effective technical content is immutable. Controlled correction requires a new version or formally controlled administrative correction where technically harmless.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q241. What happens when a MethodVersion is retired?

**Reconciled Answer:** The MethodVersion is no longer permitted for new TestInstances after its retirement/effective-end point, but remains permanently available for historical reconstruction.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q242. Can historical TestInstances use a retired MethodVersion?

**Reconciled Answer:** Yes. Always preserve the original MethodVersion used.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q243. How is method status represented?

**Reconciled Answer:** Method and MethodVersion status should be represented separately.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q244. What states can a MethodVersion have?

**Reconciled Answer:** Draft → Under Review → Approved → Effective → Retired/Superseded.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q245. Who approves a new MethodVersion?

**Reconciled Answer:** Laboratory Technical Authority, with Quality involvement where QMS/accreditation control requires it.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q246. Who approves method revisions?

**Reconciled Answer:** Same technical authority; Quality approval where the revision affects controlled QMS/accreditation/reporting requirements

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q247. Is method validation/verification evidence stored in the LIMS?

**Reconciled Answer:** Yes. Evidence records and/or controlled documents must be linked to the specific MethodVersion.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q248. Is a method allowed to become effective before approval evidence is attached?

**Reconciled Answer:** No. Required verification/validation and approval evidence must exist before the version becomes effective.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q249. Are method documents linked to MethodVersion?

**Reconciled Answer:** Yes, to MethodVersion through exact DocumentVersion.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q250. Are internal laboratory SOP versions linked to MethodVersion?

**Reconciled Answer:** Yes, exact SOP/document version linked to the MethodVersion.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q251. What happens if an external method standard changes?

**Reconciled Answer:** Review impact → create/adopt appropriate MethodVersion → verify again → approve → make effective.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q252. Does the system need to track obsolete/superseded methods?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q253. Must method applicability be effective-dated?

**Reconciled Answer:** Yes.

---

# 10. TestDefinition

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q254. What exactly is a TestDefinition?

**Reconciled Answer:** TestDefinition is the controlled definition of a laboratory test or service that may be requested and executed for a Sample, specifying its technical method relationship, required parameters, prerequisites, equipment requirements, applicable rules, and reporting representation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q255. What identifies a TestDefinition uniquely?

**Reconciled Answer:** Globally unique internal TestDefinition ID, plus a unique controlled Test Code.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q256. Can one MethodVersion contain multiple TestDefinitions?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q257. Can one TestDefinition ever reference more than one MethodVersion?

**Reconciled Answer:** A TestDefinition shall have **one effective MethodVersion at a time for a given applicability context**, while historical TestDefinition→MethodVersion relationships must remain permanently reconstructable.
A TestDefinition may change from one MethodVersion to another through controlled, effective-dated configuration.
For historical TestInstances, the exact MethodVersion applicable to that execution shall remain identifiable even after the TestDefinition later points to a newer MethodVersion.
A TestDefinition shall not simultaneously rely on multiple MethodVersions for the same execution context without an explicitly modeled technical reason and approved configuration rule.
If parallel MethodVersions are genuinely required for different matrices, disciplines, or other applicability contexts, that distinction must be represented explicitly rather than allowing ambiguous overlapping references.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q258. What descriptive fields are required for a TestDefinition?

**Reconciled Answer:** TestDefinition ID, code, technical name, customer-facing name, status, description, discipline/matrix applicability, MethodVersion, and relevant configuration references.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q259. Is there a customer-facing test name separate from the technical test name?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q260. Is a test code required?

**Reconciled Answer:** Yes, and I recommend making it globally unique.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q261. Are synonyms or aliases required?

**Reconciled Answer:** Yes, where useful for search/customer terminology; the controlled Test Code remains authoritative.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q262. Can a TestDefinition be active/inactive/retired?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q263. Can a TestDefinition be changed after use?

**Reconciled Answer:** Yes for controlled non-semantic metadata; no silent modification of technical meaning.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q264. Which TestDefinition changes require versioning instead of editing?

**Reconciled Answer:** A TestDefinition change shall require controlled versioning rather than ordinary in-place editing when it changes technical meaning or could affect execution, calculation, interpretation, reporting, eligibility, or historical reconstruction.

Changes requiring controlled versioning include:
* MethodVersion association;
* Required/optional parameters;
* Parameter meaning or applicability;
* Units or conversion rules where technically meaningful;
* Required equipment;
* Preconditions/prerequisites;
* Calculation/formula relationships;
* QC requirements;
* Accreditation behavior;
* Result interpretation;
* Reportable technical fields;
* Technical acceptance criteria;
* Other behavior that can alter the meaning or execution of the test.

Non-semantic administrative corrections may be permitted under controlled rules with audit evidence.
A TestDefinition must never be edited in a way that changes the technical interpretation of an already executed TestInstance.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q265. Can TestDefinition requirements vary by sample matrix or discipline?

**Reconciled Answer:** Yes. Test-specific rules may vary by matrix/discipline through controlled configuration.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q266. Are test prerequisites required?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q267. Are required equipment types defined at TestDefinition level?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q268. Are required parameters defined at TestDefinition level?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q269. Are report display rules defined at TestDefinition level?

**Reconciled Answer:** Yes, but detailed template/document versioning remains separate.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q270. Is accreditation override defined at TestDefinition level exactly as specified?

**Reconciled Answer:** Yes. TestDefinition-specific override targets the applicable MethodVersion and takes precedence over its default.

---

# 11. ParameterDefinition

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q271. What is a ParameterDefinition?

**Reconciled Answer:** ParameterDefinition is a controlled definition of a data element required or permitted for a TestDefinition, including its semantic meaning, data type, unit rules, validation rules, precision, applicability, and reporting behavior.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q272. What uniquely identifies a ParameterDefinition?

**Reconciled Answer:** Globally unique internal ParameterDefinition ID + stable Parameter Code.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q273. Which parameter data types are required?

**Reconciled Answer:** Numeric decimal, integer, text, boolean, date, datetime, controlled single-selection; multi-selection only where a genuine multi-valued concept exists.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q274. Are parameters numeric, text, boolean, date/time, selection, or other types?

**Reconciled Answer:** Support numeric, text, boolean, date/time and controlled selections; avoid arbitrary JSON/EAV types.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q275. Which result values can have units?

**Reconciled Answer:** Primarily numeric measurement/calculation quantities.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q276. Are units centrally controlled?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q277. Are parameter units versioned?

**Reconciled Answer:** Unit definitions should be controlled/immutable; don't version every use. A materially different unit definition gets a new controlled unit.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q278. Can one parameter have multiple allowed units?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q279. Is unit conversion required?

**Reconciled Answer:** Yes, with a canonical unit and controlled conversion rules.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q280. Who defines allowed input ranges?

**Reconciled Answer:** Laboratory Technical Authority/method owner, based on the approved method and laboratory policy.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q281. Are warning limits different from hard acceptance limits?

**Reconciled Answer:** Yes, distinctly modeled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q282. Are decimal precision and display precision distinct?

**Reconciled Answer:** Yes, distinct.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q283. Is rounding applied during calculation or only display?

**Reconciled Answer:** Calculation only where method explicitly requires it; otherwise preserve precision internally and round for controlled final reporting/display.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q284. Must the unrounded value be preserved?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q285. Are significant figures required?

**Reconciled Answer:** Support as method/configuration-specific; not universally mandatory.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q286. Are below-detection-limit values required?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q287. How are non-detects represented?

**Reconciled Answer:** Structured qualifier + detection limit/decision value where applicable; never rely on text such as "<0.1" as the underlying value.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q288. How are less-than/greater-than qualifiers stored?

**Reconciled Answer:** Store as structured qualifiers, separately from the numeric value.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q289. Are qualitative result categories required?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q290. Are reference ranges required?

**Reconciled Answer:** Yes, where applicable, but distinguish them from acceptance/specification limits.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q291. Are customer-specific reference ranges required?

**Reconciled Answer:** Customer-specific reference ranges shall not be treated as a generic requirement by default.

LabNexus shall distinguish between:
- reference intervals;
- specification/acceptance limits;
- customer-specific contractual requirements;
- customer display/reporting preferences.

A customer-specific value shall be modeled as a reference interval only where the laboratory has an approved technical basis for treating it as such.

Where the customer requirement is actually an acceptance/specification criterion or a reporting preference, it shall be represented using the appropriate model rather than being incorrectly stored as a reference range.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q292. Are matrix-specific parameter rules required?

**Reconciled Answer:** Yes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q293. Are parameter comments/remarks required?

**Reconciled Answer:** Yes, but comments cannot replace structured technical fields.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q294. Are required parameters mandatory before result submission?

**Reconciled Answer:** Yes before result submission, unless explicitly marked Not Applicable through a controlled rule.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q295. Can a parameter be not applicable for a specific TestInstance?

**Reconciled Answer:** Yes, where permitted by configuration, with reason.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q296. Who can override a parameter-level validation rule?

**Reconciled Answer:** Ordinary analysts should not bypass hard validation. Warnings may be acknowledged; hard business/technical constraints require controlled policy/configuration or authorized technical disposition.

---

# 12. Formula and Calculation Engine

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q297. Which tests require calculated results?

**Reconciled Answer:** Laboratory-configurable. The laboratory defines through controlled configuration which TestDefinitions produce calculated results. No test is assumed to require calculation unless configured and approved.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q298. What formulas are currently used by the laboratory?

**Reconciled Answer:** Laboratory-configurable. Authorized laboratory technical personnel enter or define formulas through a controlled FormulaVersion mechanism. Approved laboratory methods/SOPs remain the authoritative source for the formula; LabNexus does not invent formulas.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q299. Which formulas depend on other results?

**Reconciled Answer:** CalculationRun shall explicitly record all upstream result dependencies used by the calculation.
Where a formula depends on another result, parameter, calculation, lookup, or controlled derived value, the CalculationRun shall preserve sufficient dependency information to establish exactly what input/result version was used.

At minimum, dependency provenance shall identify:
* Upstream Result/ResultRevision where applicable;
* Parameter/input identity;
* Relevant CalculationRun;
* FormulaVersion;
* Controlled lookup/configuration version where applicable;
* Input value used;
* Unit/representation where technically relevant.

A later correction of an upstream result must not silently change the historical meaning of an earlier CalculationRun.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q300. Which formulas depend on sample metadata?

**Reconciled Answer:** Yes. A formula may use configured Sample/Request/TestInstance metadata where the selected method requires it. The laboratory selects which metadata fields are valid inputs.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q301. Which formulas depend on equipment values?

**Reconciled Answer:** Yes. Formulas may use controlled equipment values, such as approved calibration/correction values. The laboratory configures which equipment values are inputs.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q302. Which formulas depend on environmental conditions?

**Reconciled Answer:** Yes. Environmental-condition values may be used where applicable. The laboratory defines whether they are required for a particular test/formula.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q303. Which formulas depend on constants or correction factors?

**Reconciled Answer:** Yes. Constants and correction factors are controlled configuration objects with their own values, units, effective dates, approval and history.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q304. Which formulas require conditional logic?

**Reconciled Answer:** Yes. Conditional logic is supported through a restricted expression mechanism. The laboratory configures the conditions; arbitrary programming is prohibited.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q305. Which formulas require lookup tables?

**Reconciled Answer:** Yes. Controlled lookup tables are supported and configured by the laboratory. Lookup-table versions used by a calculation are preserved.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q306. Which formulas require averaging?

**Reconciled Answer:** Yes. Averaging/aggregation functions are engine capabilities; the laboratory determines where and how they are used.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q307. Which formulas require replicate handling?

**Reconciled Answer:** Yes. Replicate handling is supported as a configured rule. The laboratory defines how replicate observations are combined for each applicable test.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q308. Which formulas require blank correction?

**Reconciled Answer:** Yes. Blank correction is a reusable engine capability. The laboratory configures whether and how a particular test uses it.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q309. Which formulas require recovery correction?

**Reconciled Answer:** Yes. Recovery correction is supported as a reusable capability and configured only where required.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q310. Which formulas require moisture/dry-basis conversion?

**Reconciled Answer:** Yes. Moisture/dry-basis conversion is supported as a reusable calculation mechanism; the laboratory defines which basis conversions each test requires.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q311. Which formulas require unit conversion?

**Reconciled Answer:** Yes. Unit conversion is a core engine capability; allowed units and conversion paths are controlled configuration.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q312. Which formulas require significant-figure rules?

**Reconciled Answer:** Yes. Significant-figure rules are configurable per applicable test/result/parameter.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q313. Which formulas require rounding at intermediate steps?

**Reconciled Answer:** Yes. Intermediate rounding is configurable, but only the approved formula/method can require it.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q314. Which formulas require rounding only at final output?

**Reconciled Answer:** Yes. Final-output rounding can be configured by the laboratory.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q315. What formula language/expression syntax should be supported?

**Reconciled Answer:** Use a restricted declarative formula language provided by LabNexus. The laboratory enters formulas using that language; it does not write Python/JavaScript/SQL.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q316. What operations are allowed in the constrained evaluator?

**Reconciled Answer:** The evaluator should support controlled arithmetic, comparison, Boolean logic, approved functions, conditionals, parameter references and controlled lookups.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q317. What operations are prohibited?

**Reconciled Answer:** Arbitrary code execution, imports, file/network access, SQL, OS commands, dynamic execution, reflection and mutation are prohibited.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q318. Are functions such as sqrt, log, exp, min, max, abs, round required?

**Reconciled Answer:** The engine should provide a controlled function library such as ABS, MIN, MAX, SQRT, ROUND; additional functions such as LOG, LOG10, EXP, POW can be enabled in the platform when genuinely required. The laboratory does not create arbitrary functions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q319. Are conditional expressions required?

**Reconciled Answer:** Yes. Conditional expressions are supported through the restricted formula language.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q320. Are loops or recursion forbidden explicitly?

**Reconciled Answer:** Yes. Explicitly forbidden. No loops or recursion.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q321. How are formula inputs named?

**Reconciled Answer:** Formula inputs use stable Parameter Codes and other controlled tokens/namespaces, not raw database IDs or arbitrary field names.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q322. How are missing inputs handled?

**Reconciled Answer:** Missing required inputs must block calculation unless the applicable configured rule explicitly permits absence. Missing, zero, N/A and non-detect remain distinct states.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q323. How are divide-by-zero or invalid-input conditions handled?

**Reconciled Answer:** Divide-by-zero, invalid units, missing dependencies and other invalid conditions cause a controlled calculation failure; they never silently become zero, null or another fabricated value.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q324. How are calculation failures presented to users?

**Reconciled Answer:** The user sees a clear business/technical message; detailed diagnostics remain in controlled technical evidence/logging and are not exposed as raw stack traces.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q325. Who can define formulas?

**Reconciled Answer:** Authorized laboratory technical users define formulas through the application. They do not modify source code.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q326. Who can approve a FormulaVersion?

**Reconciled Answer:** Authorized Laboratory Technical Authority approves FormulaVersion. Quality involvement is added where the formula affects controlled QMS/accreditation/reporting requirements.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q327. Can formulas be changed after use?

**Reconciled Answer:** A FormulaVersion shall never be changed in place after it has been used for an authoritative CalculationRun.

A new FormulaVersion is required when a change can alter calculation behavior, including:
* Formula expression;
* Inputs or dependencies;
* Constants;
* Lookup tables;
* Unit/conversion logic;
* Rounding behavior;
* Conditional logic;
* Reference to another FormulaVersion;
* Interpretation of an input;
* Calculation engine semantics that materially affect the outcome.

Harmless administrative metadata corrections may be handled under controlled rules where they cannot alter calculation meaning.
The effective FormulaVersion used by each CalculationRun remains immutable historical evidence.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q328. What makes a new FormulaVersion necessary?

**Reconciled Answer:** Yes. Every authoritative CalculationRun shall store the **exact FormulaVersion** used.
The relationship shall be explicit and immutable.
A CalculationRun shall not merely store the current formula ID because that would make later formula changes capable of changing historical interpretation.
The FormulaVersion reference shall identify the exact controlled formula version effective for that calculation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q329. Must each calculation run store the formula version used?

**Reconciled Answer:** Yes. Every authoritative CalculationRun shall preserve an **input snapshot sufficient to reproduce and audit the calculation**.
The snapshot shall include the actual values used, not merely references to mutable current values.
Where an input is itself a controlled result/configuration, the snapshot shall also retain its historical identity/version reference.
The objective is deterministic historical reconstruction without depending on current mutable state.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q330. Must each calculation run store input snapshots?

**Reconciled Answer:** Yes. The calculation engine shall have deterministic behavior for a given CalculationRun, controlled FormulaVersion, input snapshot, and relevant configuration/version context.
Historical results must not become dependent on whichever future software version happens to recalculate them.
Where calculation-engine behavior changes materially, the engine/version identity shall change and existing CalculationRuns shall remain associated with the engine version under which they were originally performed.
Historical calculations shall not be silently recomputed merely because the calculation engine was upgraded.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q331. Must the calculation engine be deterministic across future software versions?

**Reconciled Answer:** The calculation engine version shall be recorded explicitly for every authoritative CalculationRun.

The recorded engine identity should include sufficient information to distinguish materially different execution behavior, such as:
* Application/release version;
* Calculation-engine version;
* Formula-evaluation implementation version where separately controlled.

The exact implementation need not reproduce the entire application package inside every CalculationRun, but it must provide an immutable reference to the controlled software version capable of identifying the relevant execution behavior.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q332. How is calculation engine version tracked?

**Reconciled Answer:** Each CalculationRun shall retain a deterministic evidence bundle containing, as applicable:
* CalculationRun ID;
* TestInstance;
* Result/ResultRevision relationship;
* FormulaVersion;
* Calculation-engine version;
* Input snapshot;
* Upstream dependency identities/revisions;
* Units and conversion context;
* Lookup/configuration versions;
* Calculation timestamp;
* Actor/system identity;
* Result produced;
* Success/failure status;
* Error/failure information where applicable.

This evidence shall remain reconstructable after later formula, configuration, software, or input changes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q333. What evidence is retained for a calculation run?

**Reconciled Answer:** A completed calculation shall produce an immutable CalculationRun record.
Failed execution shall also be preserved as an execution event/evidence record where required for auditability.
The CalculationRun shall be linked to the resulting ResultRevision where a result was produced. Re-execution after correction or controlled change shall create a new CalculationRun rather than overwrite the earlier one.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q334. How are manually entered versus automatically calculated values distinguished?

**Reconciled Answer:** Yes. Observed, calculated, imported and explicitly adjusted values are distinguished by provenance metadata.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q335. Can an authorized user override a calculated result?

**Reconciled Answer:** Yes, manual calculation adjustment may exist only where explicitly enabled/approved for named tests/parameters and must preserve the calculated provenance.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q336. If yes, under what conditions and with what evidence?

**Reconciled Answer:** Where manual calculation adjustment is permitted, all of the following conditions shall apply:
- the affected TestDefinition/parameter is explicitly configured as permitting adjustment;
- the adjustment is performed only by an authorized user;
- the reason for adjustment is recorded;
- the original calculation result remains preserved;
- the CalculationRun and FormulaVersion remain traceable;
- the adjusted value and actor/timestamp are recorded;
- supporting evidence is recorded where required;
- the adjustment follows applicable Review, Verification, Approval, and SoD requirements;
- the system does not treat the adjusted value as though it were the original calculated output.

Where an approved result is being adjusted, the controlled reopen/correction process shall apply.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q337. Can a calculated result be manually corrected after approval?

**Reconciled Answer:** Yes, but only through controlled reopen/correction. An approved calculated result is never edited in place. A new CalculationRun/ResultRevision is created where appropriate, followed by required review/verification/approval.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q338. Which calculation outputs are reportable?

**Reconciled Answer:** Configurable. The laboratory defines which outputs are reportable. Intermediate calculations and internal inputs remain in the technical record unless explicitly configured for reporting.

---

# 13. Result Model and Revision Rules

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q339. What exactly is the current live Result state?

**Reconciled Answer:** Result is the current live technical state of one result for one TestInstance. It represents the currently effective value/qualifier/unit/status and points to the current effective ResultRevision.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q340. Which values belong to Result versus ResultRevision?

**Reconciled Answer:** Result holds stable identity and current-state representation; ResultRevision holds immutable historical snapshots of technical result state, including revision type and provenance.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q341. Which fields are immutable after result submission?

**Reconciled Answer:** Result identity, TestInstance linkage, and historical revision records become immutable after controlled creation; technical values cannot be silently overwritten after submission.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q342. Which fields may be edited before review?

**Reconciled Answer:** Before Review, permitted technical fields may be edited according to TestDefinition/workflow configuration, with audit history.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q343. Which fields may be edited after review?

**Reconciled Answer:** After Review, ordinary editing is blocked; changes require controlled rework/correction according to the affected field and workflow state.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q344. Which fields may be edited after verification?

**Reconciled Answer:** After Verification, ordinary editing is blocked; changes require controlled reopening/rework/correction and renewed verification where applicable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q345. Which fields may be edited after approval?

**Reconciled Answer:** After Approval, no ordinary editing is permitted. Changes require controlled reopen/correction and a new approval cycle.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q346. What exactly triggers a Correction revision?

**Reconciled Answer:** A **Correction ResultRevision** shall be created when an existing technical Result is intentionally changed through a controlled correction process.

A Correction revision requires:
* Existing Result identification;
* Corrected technical value/qualifier/unit/status;
* Correction reason;
* Actor;
* Timestamp;
* Authorization;
* Original historical state preserved;
* Relevant CalculationRun where recalculation occurs;
* Review/Verification/Approval again where required;
* Impact assessment on issued reports.

A correction shall never modify the historical ResultRevision in place.
A correction revision does not represent an approval by itself; approval remains a separate controlled event/ApprovalSnapshot.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q347. What exactly triggers an ApprovalSnapshot revision?

**Reconciled Answer:** An **ApprovalSnapshot ResultRevision** shall be created when an approved technical state must be frozen as the authoritative approved result representation.
Each approval shall be associated with the exact approved ResultRevision and shall produce the corresponding immutable ApprovalSnapshot.
The snapshot shall preserve the result information necessary to reconstruct exactly what was approved, including applicable result value/qualifier/unit, TestDefinition/MethodVersion representation, relevant analyst/approval identity, accreditation representation, timestamps, and associated calculation/result provenance as required.
An ApprovalSnapshot must never be rewritten after approval.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q348. Must every approved result create an ApprovalSnapshot?

**Reconciled Answer:** Yes. **Every successful Approval of a technical Result shall create an ApprovalSnapshot.**
This ensures that approval is not merely a mutable status on the current Result.

The ApprovalSnapshot shall identify:
* Approved Result;
* Exact ResultRevision;
* TestInstance;
* Approval event;
* Approver;
* Approval time;
* Applicable authorization/SoD context;
* Report-relevant approved representation;
* Relevant accreditation/configuration context where required.

Failed or rejected approval attempts shall generate approval-chain events but shall not create a successful ApprovalSnapshot.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q349. Can an ApprovalSnapshot exist without an approval event?

**Reconciled Answer:** No. An ApprovalSnapshot shall **never exist without a corresponding successful approval event**.

The authoritative relationship is:
**ResultRevision → Approval event → ApprovalSnapshot**

Database/domain invariants shall prevent an orphan ApprovalSnapshot.
A failed, cancelled, rejected, or otherwise incomplete approval attempt shall remain an approval-chain event but shall not create an authoritative ApprovalSnapshot.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q350. Can a Correction exist without a formal reopen/correction event?

**Reconciled Answer:** No. A Correction ResultRevision shall not be created without a corresponding **controlled correction/reopen event**.
The correction process shall establish the reason, authorization, actor, impact, and applicable workflow state before the technical revision is committed.
The business operation creating the correction event, ResultRevision, necessary CalculationRun, audit evidence, and applicable state transition shall be transactionally controlled so that the system cannot leave a correction revision without its required provenance.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q351. How are revision numbers assigned?

**Reconciled Answer:** ResultRevision numbers are assigned by the system, sequentially per Result, within the transaction that creates the revision.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q352. Are revision numbers strictly sequential?

**Reconciled Answer:** Yes. Revision numbers are strictly sequential per Result: 1, 2, 3… with no reused number.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q353. Can revisions ever be deleted?

**Reconciled Answer:** No revisions may ever be deleted.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q354. Can revisions ever be voided?

**Reconciled Answer:** ResultRevisions shall **not be voided in place**.

The approved v1 ResultRevision vocabulary shall remain limited to the controlled technical revision semantics already established:
* Correction;
* ApprovalSnapshot.

If a prior result becomes inappropriate for further use, the system shall preserve the historical ResultRevision and express the changed condition through the appropriate controlled workflow, correction, reopen, approval-chain event, or report withdrawal/reissue process.
Do not introduce a generic `Void` or `Superseded` ResultRevision type merely to represent a later business state.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q355. If a correction is rejected, is a revision created anyway or only an event recorded?

**Reconciled Answer:** If a correction request is rejected, no Correction ResultRevision is created; the request/rejection itself is preserved as an event/audit record.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q356. How are correction reasons classified?

**Reconciled Answer:** Separate technical-result correction from report/document correction and report representation errors.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q357. Who may request a correction?

**Reconciled Answer:** Authorized laboratory users who identify a problem may request a correction; ordinary users do not automatically receive approval authority.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q358. Who may approve a correction?

**Reconciled Answer:** Correction approval should be performed by the authorized Technical Authority or designated correction approver, with Quality involvement where required.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q359. Does correction require technical review again?

**Reconciled Answer:** Yes, where the correction could affect technical validity.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q360. Does correction require verification again?

**Reconciled Answer:** Yes, where the correction affects the verified technical content.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q361. Does correction require a new approval?

**Reconciled Answer:** Yes. Any correction that changes an already approved result requires new approval before re-release.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q362. What happens to previously issued reports after a correction?

**Reconciled Answer:** Separate technical-result correction from report/document correction and report representation errors.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q363. Must a correction automatically identify affected reports?

**Reconciled Answer:** Separate technical-result correction from report/document correction and report representation errors.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q364. What report/revision consequences are mandatory after correction?

**Reconciled Answer:** Separate technical-result correction from report/document correction and report representation errors.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q365. Can a result be corrected without changing the report?

**Reconciled Answer:** Separate technical-result correction from report/document correction and report representation errors.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q366. What conditions permit or prohibit that?

**Reconciled Answer:** Separate technical-result correction from report/document correction and report representation errors.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q367. How is the current result identified when multiple historical revisions exist?

**Reconciled Answer:** Current Result is identified by the Result row plus its current_revision_id/current-state pointer.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q368. How is a historical result revision reconstructed?

**Reconciled Answer:** Historical ResultRevision reconstruction uses the immutable revision snapshot, its revision number/type, associated correction/reopen/approval event, and linked CalculationRun/ReportSnapshot data.

---

# 14. Review, Verification, and Approval

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q369. What exactly does Review mean in laboratory practice?

**Reconciled Answer:** Review = technical examination of the completed test work/result for completeness, consistency, calculations, required observations, QC status, method compliance and obvious issues before verification.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q370. What exactly does Verification mean?

**Reconciled Answer:** Verification = independent confirmation that the result/test record satisfies defined technical and acceptance requirements and is suitable to proceed to Approval.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q371. What exactly does Approval mean?

**Reconciled Answer:** Approval = formal authorization that the verified result is approved for controlled reporting/release, creating the ApprovalSnapshot.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q372. Who may perform Review?

**Reconciled Answer:** Review is performed by an authorized Technical Reviewer.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q373. Who may perform Verification?

**Reconciled Answer:** Verification is performed by an authorized Technical Verifier.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q374. Who may perform Approval?

**Reconciled Answer:** Approval is performed by an authorized Approver/Authorized Signatory.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q375. Are different roles required for the three stages?

**Reconciled Answer:** The roles are logically distinct. Whether different individuals are always required is governed by the approved SoD policy; the hard Analyst restrictions remain mandatory.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q376. What qualifications are required for each stage?

**Reconciled Answer:** Each stage requires defined competence/authority appropriate to the activity.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q377. Are qualifications represented in the LIMS?

**Reconciled Answer:** Yes. Relevant competence/authorization status should be represented or referenced in LIMS.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q378. What happens when a qualified person is unavailable?

**Reconciled Answer:** Use the approved alternate-approver/authorized substitute path; never use an ad-hoc substitute.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q379. What alternate-approver process is allowed?

**Reconciled Answer:** Alternate must be predesignated, competent, authorized and not prohibited by SoD.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q380. Exactly which combinations are hard-blocked by SoD?

**Reconciled Answer:** Hard blocks: Analyst→Review, Analyst→Verification, Analyst→Approval on the same TestInstance.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q381. Is Analyst → Review always blocked on the same TestInstance?

**Reconciled Answer:** Always blocked.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q382. Is Analyst → Verification always blocked on the same TestInstance?

**Reconciled Answer:** Always blocked.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q383. Is Analyst → Approval always blocked on the same TestInstance?

**Reconciled Answer:** Always blocked.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q384. What is the approved Reviewer → Technical Verification rule?

**Reconciled Answer:** The Reviewer → Technical Verification relationship shall be explicitly classified in the SoD Matrix.

For the same TestInstance, the recommended v1 rule is:
**The user who performs Review shall not perform Technical Verification.**

Technical Verification shall therefore provide an independent confirmation after Review.
This is a TestInstance-level restriction and shall not automatically prevent the same user from reviewing one TestInstance and verifying another where otherwise authorized.
Emergency mechanisms shall not bypass this hard restriction.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q385. Is Technical Reviewer → Approval allowed normally, blocked normally, or policy-controlled?

**Reconciled Answer:** Approved for v1

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q386. What exact policy controls Technical Reviewer → Approval?

**Reconciled Answer:** Where Technical Reviewer → Approval is policy-controlled, the policy shall define:
- whether the same user may perform both actions;
- whether independent Verification by another authorized person is mandatory;
- required competence/authorization;
- applicable TestDefinition or test-category scope;
- prohibited combinations;
- alternate-authority requirements;
- required documentation and reason where an exception is used;
- whether countersigned evidence is required;
- how the decision is represented in the SoD policy version in effect.

The rule shall be effective-dated and historically reconstructable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q387. Which SoD combinations require countersigned exception evidence?

**Reconciled Answer:** Countersigned exception evidence shall be required for any policy-controlled SoD combination where an approved exception mechanism is used.

The exception evidence shall include, as applicable:
- affected TestInstance;
- action/stage;
- normal SoD rule;
- reason for the exception;
- identity of the actor;
- identity and authority of the authorizer;
- independent countersigner;
- date/time;
- applicable policy version;
- affected result/report;
- evidence/reference;
- expiry or completion condition;
- retrospective review where required.

Absolute hard-blocked SoD combinations shall not be made valid merely by countersigning.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q388. Are there any legitimate emergency exceptions to policy-controlled combinations?

**Reconciled Answer:** Emergency exceptions may be permitted only for policy-controlled SoD combinations where the approved laboratory policy explicitly allows them.

Emergency handling shall not bypass absolute hard blocks such as:
- Analyst → Review on the same TestInstance;
- Analyst → Verification on the same TestInstance;
- Analyst → Approval on the same TestInstance;
- other explicitly classified hard prohibitions.

Where an emergency exception is permitted, it shall be bounded, visibly identified, fully audited, independently countersigned, and subject to retrospective review.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q389. What does the system do when an actor loses authorization between stages?

**Reconciled Answer:** If an actor loses required authorization between workflow stages:
- the actor's next controlled action shall be blocked;
- previously completed and valid actions shall remain historical;
- the TestInstance shall remain in its current controlled state unless the loss of authorization itself requires a separate disposition;
- another currently authorized person may continue the workflow where permitted;
- the authorization change and blocked/continued workflow actions shall remain auditable.

The system shall not automatically invalidate previously recorded Review, Verification, or Approval events solely because the actor later lost authorization, unless an authorized policy/process determines that retrospective impact assessment is required.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q390. Can an approval be revoked?

**Reconciled Answer:** Approval may be revoked only through controlled revocation/reopen governance; never by deleting or editing the approval event.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q391. If approval is revoked, what state follows?

**Reconciled Answer:** Revocation leads to a controlled state such as ApprovalRevoked / ReopenedForCorrection, according to the reason and procedure.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q392. Can a verified result be re-opened?

**Reconciled Answer:** A verified result may be reopened only through authorized rework/correction procedure.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q393. Can an approved result be re-opened?

**Reconciled Answer:** An approved result may be reopened only through controlled correction/reopen procedure.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q394. Who may reopen an approved TestInstance?

**Reconciled Answer:** Reopening an approved TestInstance requires authorized Technical/Quality authority according to the reason and policy.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q395. What reason is required for reopening?

**Reconciled Answer:** Mandatory structured reason, explanation, impact assessment and authorizer.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q396. Does reopening create an audit event, result revision, or both?

**Reconciled Answer:** Reopening creates both an audit event and, where the technical Result changes, the appropriate ResultRevision; reopening itself is always audited.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q397. What exactly is recorded in approval_chain_event?

**Reconciled Answer:** approval_chain_event records each review/verification/approval/rejection/revocation/attempt event, with TestInstance, stage, actor, timestamp, outcome, reason/comments, authorization context and relevant ResultRevision/ApprovalSnapshot references.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q398. Can the same stage be performed more than once?

**Reconciled Answer:** Yes. A stage may be performed more than once, especially after rework/reopen.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q399. If so, how are repeated attempts represented?

**Reconciled Answer:** Each attempt is a separate immutable approval_chain_event with sequence/order information and outcome; successful completion advances the lifecycle.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q400. How are rejected/failed review attempts preserved?

**Reconciled Answer:** Failed Review attempts are preserved as events with outcome and reason/comments.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q401. How are rejected/failed verification attempts preserved?

**Reconciled Answer:** Failed Verification attempts are preserved similarly.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q402. How are rejected/failed approval attempts preserved?

**Reconciled Answer:** Failed Approval attempts are preserved similarly.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q403. Are comments mandatory for failed stages?

**Reconciled Answer:** Yes. Comments/reason are mandatory for failed/negative outcomes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q404. Are electronic acknowledgements/signatures required?

**Reconciled Answer:** Yes. Controlled electronic acknowledgement/signature evidence should be required for Review, Verification and Approval according to the laboratory's approved policy.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q405. If yes, what is the exact meaning of the electronic signature?

**Reconciled Answer:** An electronic signature means a controlled, attributable act by an authenticated authorized user indicating that they performed the specified stage and accepted the recorded outcome at that time.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q406. Is the secure user session sufficient evidence of user identity, or is re-authentication required for approval?

**Reconciled Answer:** An authenticated secure server-side session is sufficient for ordinary authorized actions but is **not sufficient by itself for high-risk approval/signing actions**.
High-risk approval actions shall require fresh authentication/re-authentication immediately before the action, with the server revalidating the user's current authorization and applicable SoD rules.
This provides stronger attribution for Review/Verification/Approval/signing actions without requiring a separate authentication mechanism for every ordinary operation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q407. Is a second-factor or password re-entry required for high-risk actions?

**Reconciled Answer:** For v1, **fresh password re-entry is required for high-risk approval/signing actions**.
A second factor/MFA is not required for v1 and shall not be introduced as an implicit dependency.
The architecture shall remain capable of adding stronger authentication later through controlled change, but the v1 approval control is password re-entry plus authenticated server-side session, authorization, and SoD enforcement.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q408. Must approval require a current password or session re-authentication?

**Reconciled Answer:** Yes. Approval and other designated high-risk signing actions shall require **current password re-entry** in v1.
The normal browser session remains valid for ordinary work, but the approval operation shall require fresh authentication, followed by server-side authorization and SoD evaluation against the exact TestInstance/record.
A previously authenticated session shall not by itself authorize the highest-risk approval action.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q409. What constitutes an approval snapshot as distinct from a normal revision?

**Reconciled Answer:** An ApprovalSnapshot is distinct from a normal technical ResultRevision because it represents the **exact technical state formally accepted by the approval event**.
A normal ResultRevision records a controlled technical result state, such as a correction.
An ApprovalSnapshot records the state actually approved and binds it to the exact approval-chain event.
The distinction is important because a Result may later undergo correction and create a new ResultRevision, while the earlier ApprovalSnapshot must continue to reconstruct exactly what was previously approved.
The relationship shall therefore be explicit:

**Result → ResultRevision → ApprovalSnapshot ↔ Approval Event**

An ApprovalSnapshot is immutable and remains historical evidence even after later rework, correction, reapproval, report reissue, or other controlled changes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q410. What data must be frozen at approval?

**Reconciled Answer:** Freeze all report/technical data needed to reconstruct exactly what was approved: Result value, qualifier, unit, precision/rounded value, TestDefinition representation, MethodVersion, relevant analyst representation, approval actor/time, applicable accreditation representation, calculation/result references and other required report-visible technical attributes.

---

# 15. Accreditation Scope

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q411. Which methods are currently within NABL scope?

**Reconciled Answer:** Not hard-coded. At deployment, the laboratory imports/enters its current approved accreditation scope and maps applicable methods to its controlled MethodVersions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q412. Which MethodVersions are currently in scope?

**Reconciled Answer:** Determined by the laboratory's configured accreditation-scope records and evidence. No MethodVersion is assumed accredited by LabNexus.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q413. Which TestDefinitions are currently in scope?

**Reconciled Answer:** Determined through the deployment's controlled scope configuration, including any TestDefinition-specific override.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q414. Are all tests under a method automatically accredited unless overridden?

**Reconciled Answer:** Not as a universal LabNexus assumption. The deployment may configure a MethodVersion-level default applicability, and a TestDefinition override may supersede it, exactly as your frozen hybrid architecture specifies.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q415. Which tests require a non-accredited override?

**Reconciled Answer:** The laboratory configures the specific TestDefinitions that must be treated as non-accredited despite the MethodVersion default.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q416. Which tests require an accredited override?

**Reconciled Answer:** The laboratory configures specific TestDefinitions as accredited where the approved scope warrants an override against the MethodVersion default.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q417. Is the override always specific to a MethodVersion?

**Reconciled Answer:** Yes. The TestDefinition override must belong to and explicitly identify the MethodVersion whose default it overrides.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q418. What is the business meaning of an accreditation-scope record?

**Reconciled Answer:** A controlled, effective-dated statement of the accreditation applicability configured for a specific deployment, framework, and MethodVersion/TestDefinition target, supported by evidence.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q419. What fields are needed to display accreditation status on a report?

**Reconciled Answer:** Resolved accreditation status, accreditation framework/body, applicable scope representation, target MethodVersion/TestDefinition, effective applicability, approved report wording/mark configuration, and required evidence/reference identifiers.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q420. What effective date/time should scope changes use?

**Reconciled Answer:** The laboratory enters the effective date/time from its approved accreditation evidence/decision. LabNexus stores it precisely for deterministic historical resolution.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q421. Who can propose a scope change?

**Reconciled Answer:** A change to accreditation-scope applicability may be proposed by an authorized **Laboratory Quality/Accreditation Authority** or a formally designated Technical Authority acting within the laboratory's approved governance process.
A proposer shall not make the scope change effective merely by creating the proposal.
The proposal shall identify the affected MethodVersion/TestDefinition scope, supporting evidence, proposed effective date/time, reason, and any known impact on existing or future TestInstances and reports.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q422. Who can approve a scope change?

**Reconciled Answer:** Accreditation-scope changes shall be approved by the designated Laboratory Quality Authority, with Technical Authority concurrence where the change affects technical method applicability.

The approval shall confirm:
- the supporting accreditation evidence;
- affected MethodVersion/TestDefinition records;
- effective date/time;
- applicability boundaries;
- impact on existing work;
- required report representation;
- any required controlled follow-up.

System administrators or implementation personnel shall not independently approve accreditation scope.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q423. What evidence supports a scope change?

**Reconciled Answer:** Evidence supporting an accreditation-scope change shall be linked to the controlled scope record and shall be sufficient to establish the authority, applicability, and effective date of the change.

Evidence should include, as applicable:
- current accreditation certificate or controlled scope document;
- approved amendment/change notice;
- relevant accreditation correspondence or decision;
- applicable internal approval;
- affected MethodVersion/TestDefinition mapping;
- effective date/time;
- supporting technical assessment;
- impact assessment for affected work/reports.

LabNexus shall record references to controlled evidence rather than inventing accreditation status independently.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q424. Can scope status be changed retrospectively?

**Reconciled Answer:** Accreditation-scope status may be changed retrospectively only through a controlled historical correction process where authoritative evidence establishes that the prior LIMS representation was incorrect or that the effective applicability must be represented retrospectively.

A retrospective scope correction shall:
- never silently overwrite the previous scope record;
- preserve the original configuration history;
- record the authoritative effective date/time;
- identify the reason and supporting evidence;
- identify the person who proposed, approved, implemented, and verified the correction;
- assess affected TestInstances and reports;
- trigger controlled report/result correction or reissue processes where required.

Historical records shall remain reconstructable according to the approved effective scope that actually applied.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q425. If yes, under what controlled process?

**Reconciled Answer:** Where a retrospective accreditation-scope change is justified, the controlled process shall be:
**Identify authoritative evidence → assess applicability → identify effective date/time → identify affected MethodVersions/TestDefinitions → identify affected TestInstances/reports → propose correction → Quality approval with Technical concurrence where applicable → implement effective-dated scope correction → independently verify → perform affected-record/report impact assessment → complete any required correction/reissue actions → retain full audit evidence.**

The historical scope record shall not be deleted or overwritten.

Any report issued under the earlier represented scope shall be assessed individually according to the approved report-correction/reissue rules rather than being silently regenerated.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q426. How are conflicting temporal scope records resolved?

**Reconciled Answer:** Conflicting temporal accreditation-scope records shall not be resolved by arbitrary precedence or by mutable current state.

The applicable scope shall be determined by:
- identifying the relevant MethodVersion/TestDefinition target;
- resolving the effective-date/time intervals;
- applying the approved temporal-boundary rule;
- rejecting or flagging overlapping records where the overlap is not explicitly permitted;
- requiring controlled correction where conflicting records represent an invalid configuration.

A valid active scope state shall be deterministic for any given applicable date/time.
Historical TestInstances and reports shall resolve against the scope record that was effective for the relevant historical event according to the approved applicability rule.
No later scope configuration may silently rewrite the historical accreditation representation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q427. What happens when a MethodVersion expires or is retired?

**Reconciled Answer:** When a MethodVersion expires or is retired, it shall no longer be available for new TestInstances after its effective end/retirement point.
Existing TestInstances that legitimately reference the MethodVersion shall retain that original MethodVersion and remain historically reconstructable.
Retirement shall not delete, alter, or invalidate historical method or accreditation records.
Where retirement affects an in-progress TestInstance, the applicable disposition shall be determined through controlled laboratory/technical rules rather than by automatically replacing the MethodVersion.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q428. What happens to existing TestInstances when scope changes after testing?

**Reconciled Answer:** A change in accreditation scope after testing has begun shall not automatically rewrite the accreditation status of an existing TestInstance.

The system shall preserve the scope state applicable to the relevant historical activity and shall identify the impact of any later scope change on:
- existing TestInstances;
- results;
- approvals;
- report revisions;
- issued reports.

Where the scope change affects work that has not yet reached the relevant controlled stage, the applicable current scope may be used according to the approved temporal rule.
Where already completed or issued work is affected, a controlled impact assessment and correction/reissue process shall apply where required.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q429. Is accreditation status determined at test execution time, approval time, report time, or by a specific policy?

**Reconciled Answer:** Accreditation status shall be determined according to a defined **applicability event/time rule**, not by whichever status happens to be current when a report is generated.
For v1, the accreditation applicability shall be resolved using the controlled effective-dated scope applicable to the relevant TestDefinition/MethodVersion and the approved laboratory rule for the relevant TestInstance activity.
The resolved accreditation state shall then be preserved as part of the technical/report history so that later configuration changes cannot alter historical representation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q430. Which historical scope value must an issued report preserve?

**Reconciled Answer:** An issued report shall preserve the exact historical accreditation state that applied to the reportable work.

At minimum, the report snapshot shall preserve:
- resolved accreditation status;
- applicable accreditation framework/body representation;
- relevant MethodVersion/TestDefinition applicability;
- effective scope reference;
- approved report wording/mark representation where applicable;
- the evidence/reference used to resolve the scope.

A later accreditation-scope change shall not alter the historical accreditation representation of an already issued report.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q431. Are accreditation symbols, marks, logos, or wording required on reports?

**Reconciled Answer:** Accreditation symbols, marks, logos, and/or wording shall be treated as controlled report content.
Whether such elements appear, where they appear, and for which reportable work they may be used shall be determined by the laboratory's approved accreditation and reporting requirements.
LabNexus shall not independently infer or create an accreditation claim merely because a MethodVersion is configured as accredited.
Accreditation marks and wording shall therefore be governed through controlled report configuration and approval.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q432. What exact wording is approved for accredited versus non-accredited work?

**Reconciled Answer:** The exact wording used for accredited and non-accredited work shall be provided and approved by the laboratory through controlled report configuration.

LabNexus shall support separate controlled representations for:
- accredited work;
- non-accredited work;
- mixed reports where permitted;
- any required qualification, limitation, disclaimer, or scope wording.

The system shall not invent regulatory or accreditation wording.
Any change to approved accreditation wording shall follow controlled report/configuration change governance.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q433. Are there tests that can never display an accreditation claim even if the method is in scope?

**Reconciled Answer:** Yes. The laboratory may identify TestDefinitions that shall not display an accreditation claim even where the associated MethodVersion has an accredited default.

Such exclusions shall be explicitly configured and approved at the TestDefinition level, consistent with the frozen accreditation precedence:
**TestDefinition override > MethodVersion default**

The exclusion shall be effective-dated and historically reconstructable.
No report shall display an accreditation claim solely because the underlying MethodVersion has an accredited default when an approved TestDefinition-specific exclusion applies.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q434. Who validates accreditation configuration before it becomes effective?

**Reconciled Answer:** Accreditation configuration shall be validated before becoming effective.

Validation shall confirm, as applicable:
- the affected MethodVersion/TestDefinition mapping;
- the accreditation evidence;
- effective date/time;
- precedence and temporal consistency;
- required report representation;
- absence of conflicting scope records;
- historical reconstruction implications.

The Laboratory Quality Authority shall provide final approval, with Technical Authority involvement where technical applicability is affected.
Implementation shall be performed only after approval, followed by independent verification of the effective configuration.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q435. What equipment categories are required?

**Reconciled Answer:** Equipment categories should be configurable. Core categories: measuring instruments, test instruments/apparatus, sample-preparation equipment, temperature/environment-control equipment, support equipment, reference/monitoring equipment. Actual launch inventory comes from the laboratory.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q436. What uniquely identifies an equipment item?

**Reconciled Answer:** Each Equipment item has a globally unique internal Equipment ID, system-generated, immutable and never reused.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q437. Which equipment fields are mandatory?

**Reconciled Answer:** Mandatory fields: Equipment ID, equipment type/category, name/description, manufacturer, model/type where applicable, unique/serial identification, status, current location, ownership/source as relevant, and applicable validity/control information.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q438. Are serial numbers mandatory?

**Reconciled Answer:** Serial number is mandatory where the manufacturer provides one; where absent, another controlled unique identifier is required.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q439. Are manufacturer and model mandatory?

**Reconciled Answer:** Manufacturer and model/type should be mandatory for equipment where those attributes exist.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q440. Are equipment locations tracked?

**Reconciled Answer:** Yes. Current equipment location is required and location history should be retained where operationally significant.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q441. Are equipment ownership/custody details required?

**Reconciled Answer:** Ownership/custody should be captured where relevant, but it need not be mandatory for every laboratory item.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q442. What equipment statuses exist?

**Reconciled Answer:** Freeze the v1 equipment-status vocabulary as **ACTIVE, OUT_OF_SERVICE, UNDER_MAINTENANCE, CALIBRATION_DUE, CALIBRATION_EXPIRED, QUALIFICATION_PENDING, and RETIRED**. Status transitions shall be controlled, auditable, and policy-driven. Equipment eligibility for a TestInstance shall be evaluated as-of the relevant activity timestamp. A later laboratory policy may add a controlled state only through the normal configuration-governance process.

**Revision 0.8 Status:** CLOSED — LABORATORY DECISION
**Primary Closure Artifact / Decision Record:** Equipment Eligibility / Activity Rule

### Q443. What status blocks use?

**Reconciled Answer:** At minimum, Out of Service, Quarantined, Retired and any other configured non-operational status must block use.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q444. What is the definition of calibration-valid?

**Reconciled Answer:** Calibration-valid = required calibration is current, evidence exists, acceptance criteria were met, and the calibration is within its approved validity interval.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q445. What is the definition of qualification-valid?

**Reconciled Answer:** Qualification-valid = required qualification has been completed, accepted and remains within its configured validity period/conditions. Where qualification is not applicable, status is N/A rather than failed.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q446. What is the definition of verification-valid?

**Reconciled Answer:** Verification-valid = required verification has been performed, accepted and remains within its configured validity period/conditions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q447. What is the definition of maintenance-valid?

**Reconciled Answer:** Maintenance-valid = no overdue mandatory maintenance that the laboratory has defined as affecting fitness for use; routine maintenance must have documented status.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q448. Which validity conditions must be checked before TestInstance execution?

**Reconciled Answer:** Before TestInstance execution, the system shall determine equipment eligibility using the controlled Equipment Eligibility / Activity Rule applicable to the TestDefinition, equipment, user, and relevant activity date/time.

Where required, eligibility shall consider:
- equipment status;
- calibration validity;
- qualification validity;
- verification validity;
- maintenance/fitness-for-use requirements;
- equipment-specific authorization/competence;
- applicable TestDefinition requirements;
- any approved exceptional-use condition.

The system shall preserve explicit EquipmentUse/activity evidence identifying the equipment actually used for the TestInstance, together with the relevant date/time and actor.
Historical eligibility shall be reconstructed from the equipment and activity evidence applicable at the time of the work, rather than from the equipment's current status.
Where equipment is found to have been ineligible or its status is later corrected, the affected TestInstances shall be identified and assessed through the controlled equipment/nonconformance impact process.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q449. Which checks are blocking?

**Reconciled Answer:** Equipment eligibility checks shall be classified explicitly as blocking or warning-only in the Equipment Eligibility / Activity Rule.

Blocking conditions shall include, at minimum, equipment states or conditions that make the equipment ineligible for the applicable controlled activity, such as:
- Out of Service;
- Quarantined;
- Retired;
- required calibration not valid;
- required qualification not valid;
- required verification not valid;
- other explicitly configured fitness-for-use failures.

Where a condition is not technically sufficient to block work, it may be configured as warning-only.
The exact blocking rules shall be defined by test/equipment requirement and shall be enforced by the backend/domain layer.
Historical EquipmentUse/activity records shall preserve what equipment was actually used, regardless of later status changes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q450. Which checks are warning-only?

**Reconciled Answer:** Warning-only equipment conditions shall be limited to conditions that the laboratory explicitly determines do not automatically make the equipment unsuitable for the affected activity.

Examples may include:
- a non-critical maintenance condition;
- an informational status;
- a condition requiring operator attention but not immediate blocking;
- another approved non-blocking equipment control.

Warnings shall be visible and auditable.
A warning shall not silently permit use where the approved rule defines the condition as blocking.
The laboratory shall define the blocking/warning classification through the controlled Equipment Eligibility / Activity Rule.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q451. Can a test use equipment with an expired calibration under any approved exception?

**Reconciled Answer:** Use of equipment with expired calibration shall normally be **blocked** where calibration validity is required for the affected TestInstance.
An exception may be permitted only where the laboratory has an approved controlled rule allowing such exceptional use for the applicable circumstance.
The exception shall not bypass other mandatory equipment or technical controls and shall not retroactively make the equipment normally eligible.
Any work performed under an approved exception shall remain explicitly identifiable for subsequent review and impact assessment.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q452. If yes, how is the exception approved and recorded?

**Reconciled Answer:** An expired-calibration exception shall require a controlled authorization and documented evidence.

At minimum, the record shall identify:
- Equipment;
- affected TestInstance(s);
- calibration status/expiry;
- reason for the exception;
- risk/impact assessment where required;
- authorizing authority;
- user performing the work;
- date/time;
- applicable policy/rule;
- supporting evidence;
- post-use review/disposition where required.

The exception shall be traceable from the equipment history to every affected TestInstance.
An administrator shall not be able to bypass the rule simply by changing the equipment status.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q453. Can equipment be temporarily unavailable?

**Reconciled Answer:** Equipment may be temporarily unavailable.
Temporary unavailability shall be represented as a controlled equipment state or condition and shall prevent use where the applicable eligibility rule requires blocking.

The record shall preserve, as appropriate:
- reason;
- start date/time;
- expected/actual return-to-service information;
- affected equipment;
- responsible actor;
- related maintenance/repair/qualification/verification evidence.

Returning equipment to service shall require the applicable controlled checks before it becomes eligible again.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q454. Can equipment be reserved or booked?

**Reconciled Answer:** Equipment reservation/booking may be supported where operationally useful, but reservation shall not itself establish technical eligibility.

A reservation shall identify, where applicable:
- equipment;
- intended TestInstance/work;
- reserved period;
- reserving user;
- status;
- conflicts.

Reservation logic shall prevent or flag conflicting bookings according to the approved equipment-use rule.
Technical eligibility, calibration/qualification/verification status, and authorization remain independent controls.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q455. Can multiple TestInstances use the same equipment at the same time?

**Reconciled Answer:** Multiple TestInstances may use the same equipment at the same time only where the equipment and laboratory procedure permit concurrent use.
The system shall not assume that every equipment item is single-use or mutually exclusive.

Concurrency shall be governed by configurable equipment-use rules, which may define:
- single-user/single-TestInstance operation;
- permitted concurrent users;
- permitted concurrent TestInstances;
- exclusive-use periods;
- required reservation;
- other applicable operational restrictions.

Actual EquipmentUse/activity shall remain historically traceable for each TestInstance.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q456. Is equipment scheduling required?

**Reconciled Answer:** Equipment scheduling shall be supported only to the extent required by the approved v1 operational rules.

At minimum, LabNexus shall support controlled equipment availability/use information sufficient to:
- identify unavailable equipment;
- prevent prohibited use;
- identify conflicts where applicable;
- support reservations/bookings where approved;
- maintain actual equipment-use history.

A full enterprise resource scheduling subsystem is not required for v1 unless separately approved.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q457. How are equipment users authorized?

**Reconciled Answer:** Equipment users shall be authorized through controlled user/equipment eligibility rules.

Authorization shall consider, where applicable:
- user identity;
- active authorization;
- required competence/qualification;
- equipment type/item;
- applicable TestDefinition or activity;
- effective authorization period;
- any role or SoD restriction.

The backend shall enforce equipment-use authorization.
An authorized user must not be able to bypass equipment restrictions merely by manually selecting an equipment item.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q458. Are user qualifications linked to equipment?

**Reconciled Answer:** Yes. Where equipment requires specific competence or authorization, the user's qualification/competence shall be linked to the applicable equipment type and/or equipment item.
The eligibility determination shall consider whether the qualification was valid for the relevant date/time.
Historical EquipmentUse records shall preserve the user, equipment, activity, and applicable authorization/qualification context needed for later reconstruction.
Where no equipment-specific qualification is required, no artificial qualification requirement shall be imposed.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q459. How is as-of eligibility determined for historical reconstruction?

**Reconciled Answer:** Historical equipment eligibility shall be determined as-of the relevant date/time of the TestInstance activity, using the controlled equipment state, validity records, authorization/qualification records, and explicit EquipmentUse/activity evidence applicable at that time.
The system shall not determine historical eligibility from the equipment's current status alone.

The historical determination shall consider, where applicable:
- equipment identity and status;
- calibration validity;
- qualification validity;
- verification validity;
- maintenance/fitness-for-use requirements;
- user authorization/competence;
- applicable TestDefinition requirements;
- approved exceptional-use records;
- relevant effective dates/times.

The actual equipment used for the TestInstance shall be recorded in an immutable EquipmentUse/activity record with the relevant actor and timestamp.
If historical records show that equipment eligibility was uncertain, invalid, or later corrected, the affected TestInstances shall be identified and assessed through the controlled equipment/nonconformance impact process.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q460. How are calibration certificates linked?

**Reconciled Answer:** Calibration certificates must be linked to the specific Equipment item and calibration event.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q461. Are calibration certificates stored in the document system?

**Reconciled Answer:** Yes. Controlled calibration certificates should be stored/referenced through the Document/DocumentVersion system.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q462. How are equipment repairs represented?

**Reconciled Answer:** Repairs are immutable history events linked to the Equipment item, including description, dates, affected condition, action, service provider/actor, evidence and return-to-service decision.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q463. How are equipment modifications represented?

**Reconciled Answer:** Modifications require controlled equipment-history records and an impact/verification assessment where relevant.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q464. How are maintenance events represented?

**Reconciled Answer:** Maintenance events are recorded as dated controlled events, including planned/completed status, work performed, actor/provider and next-due information where applicable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q465. How are verification records represented?

**Reconciled Answer:** Verification records are controlled records linked to the equipment, verification event, criteria, results, outcome, assessor and evidence.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q466. What happens to historical TestInstances if equipment status is later corrected?

**Reconciled Answer:** If equipment status is later corrected, the correction shall not rewrite historical TestInstance eligibility or equipment use.
Historical TestInstances shall retain the exact EquipmentUse/activity record identifying the equipment actually used and the applicable date/time.
Where the corrected equipment status indicates that the equipment may have been ineligible at the time of use, the system shall identify the affected TestInstances and initiate the controlled equipment/nonconformance impact process.
The impact assessment shall determine, as applicable, whether affected work requires review, retest, rework, result correction, report correction/reissue, or other controlled disposition.
The historical equipment status correction, impact assessment, disposition, and resulting actions shall remain fully traceable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q467. How are equipment-related nonconformities handled?

**Reconciled Answer:** Equipment-related nonconformance follows a controlled impact path: identify the equipment issue and affected equipment state; identify affected TestInstances; perform documented impact assessment; determine disposition including retest/rework/report impact where applicable; record corrective action; and authorize return to service.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q468. Which QC types are actually used by the laboratory today?

**Reconciled Answer:** The actual QC types used by the laboratory at launch shall be established through the approved **Launch QC / QC Configuration Matrix** and shall not be invented by the LIMS project.

The matrix shall identify the QC mechanisms applicable to the launch disciplines, particularly Solid Fuel and Solid Biofuel, including where applicable:
- blanks;
- duplicates;
- replicates;
- spikes;
- reference materials/CRMs;
- calibration checks;
- other laboratory-approved QC activities.

LabNexus may implement the generic QC mechanism independently of the final launch-specific matrix, but no launch-specific QC rule shall become effective until the corresponding laboratory QC configuration is approved.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q469. Which tests require blanks?

**Reconciled Answer:** Which tests require blanks shall be defined in the approved Launch QC / QC Configuration Matrix.

For each applicable TestDefinition, the matrix shall identify whether blanks are:
- required;
- optional;
- not applicable;
together with the required frequency, acceptance criteria, failure handling, and relationship to result approval where applicable.

No test shall be assumed to require a blank merely because a generic blank capability exists.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q470. Which tests require duplicates?

**Reconciled Answer:** Which tests require duplicates shall be defined in the approved **Launch QC / QC Configuration Matrix.**
The matrix shall identify applicable TestDefinitions, duplicate frequency/conditions, acceptance criteria, failure handling, and whether the duplicate affects result release or approval.
Duplicate requirements shall remain controlled technical configuration rather than arbitrary analyst decisions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q471. Which tests require replicates?

**Reconciled Answer:** Which tests require replicates shall be defined in the approved Launch QC / QC Configuration Matrix and applicable laboratory methods/SOPs.

The matrix shall define:
- applicable tests;
- replicate requirements;
- number/frequency where applicable;
- how replicate observations are identified;
- how they contribute to calculations/results;
- acceptance criteria;
- failure/disposition rules.

Replicate execution shall remain distinguishable from ordinary retest or correction activity.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q472. Which tests require spikes?

**Reconciled Answer:** Which tests require spikes shall be defined in the approved **Launch QC / QC Configuration Matrix** and supported by the applicable laboratory method/SOP.
For each applicable test, the matrix shall define the spike requirement, frequency, applicable acceptance criteria, calculation/interpretation rules, and failure handling.
No spike requirement shall be inferred solely from generic QC capability.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q473. Which tests use reference materials or CRMs?

**Reconciled Answer:** Use of reference materials or CRMs shall be defined by the approved **Launch QC / QC Configuration Matrix** and applicable laboratory methods/SOPs.

The matrix shall identify:
- applicable TestDefinitions;
- material/reference identity;
- frequency or use condition;
- acceptance criteria;
- result interpretation;
- failure handling;
- required evidence and traceability.

CRM/reference-material use shall remain linked to the relevant QC event and affected work where applicable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q474. Which tests require calibration checks?

**Reconciled Answer:** Calibration-check requirements shall be defined in the approved **Launch QC / QC Configuration Matrix** and applicable equipment/method controls.

The matrix shall identify:
- applicable tests/equipment;
- when calibration checks are required;
- acceptance criteria;
- actions when the check fails;
- whether affected TestInstances are blocked;
- required investigation or disposition.

Generic calibration-check capability may be implemented, but launch-specific rules require approved laboratory configuration.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q475. What acceptance criteria apply to each QC type?

**Reconciled Answer:** Acceptance criteria for each QC type shall be defined in the approved **Launch QC / QC Configuration Matrix**, based on the applicable laboratory method, SOP, equipment requirement, technical procedure, or other authoritative laboratory source.

Each QC rule shall identify, where applicable:
- the criterion;
- units/data type;
- calculation or comparison method;
- tolerance/limit;
- pass/fail interpretation;
- blocking or warning consequence;
- required disposition when failed.

LabNexus shall not invent technical QC acceptance limits.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q476. Are QC criteria numeric, categorical, or formula-based?

**Reconciled Answer:** QC criteria may be numeric, categorical, formula-based, or a controlled combination of these, according to the applicable laboratory rule.

The QC configuration model shall therefore support:
- numeric limits and ranges;
- categorical outcomes;
- Boolean pass/fail rules;
- formula-based evaluation;
- controlled lookup/reference criteria.

The applicable QC Matrix shall identify the evaluation type for each QC rule.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q477. Which QC failures block result approval?

**Reconciled Answer:** Which QC failures block result approval shall be defined explicitly in the approved **Launch QC / QC Configuration Matrix.**
A QC failure shall block approval where the approved laboratory rule determines that the affected result cannot proceed without investigation, correction, retest, rework, or authorized disposition.
The system shall enforce configured blocking rules at the backend/domain level.
No QC failure shall be treated as automatically blocking unless the approved QC rule says so.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q478. Which QC failures allow documented acceptance with justification?

**Reconciled Answer:** A QC failure may permit documented acceptance with justification only where the approved laboratory QC rule explicitly allows such disposition.

The disposition shall require, as applicable:
- identified QC failure;
- affected TestInstance/result;
- reason and justification;
- authorized decision-maker;
- impact assessment where required;
- required review/verification/approval;
- complete audit evidence.

An analyst shall not bypass a configured blocking QC rule through an ordinary acceptance action.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q479. Who decides whether a QC failure blocks work?

**Reconciled Answer:** The authority to determine whether a QC failure blocks work shall be the **Laboratory Technical Authority**, with Quality involvement where the laboratory's QMS or controlled QC governance requires it.
The resulting rule shall be captured in the approved **Launch QC / QC Configuration Matrix** and controlled through configuration governance.
System administrators shall implement approved QC rules but shall not independently decide the technical blocking criteria.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q480. Must QC failures automatically open an investigation?

**Reconciled Answer:** Keep minimum controlled investigation/CAPA linkage; do not create a general enterprise CAPA subsystem without approved need.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Quality Management / NC-CAPA Boundary

### Q481. What is an investigation record?

**Reconciled Answer:** Keep minimum controlled investigation/CAPA linkage; do not create a general enterprise CAPA subsystem without approved need.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Quality Management / NC-CAPA Boundary

### Q482. Who can investigate a QC failure?

**Reconciled Answer:** Keep minimum controlled investigation/CAPA linkage; do not create a general enterprise CAPA subsystem without approved need.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Quality Management / NC-CAPA Boundary

### Q483. Who can close a QC investigation?

**Reconciled Answer:** Keep minimum controlled investigation/CAPA linkage; do not create a general enterprise CAPA subsystem without approved need.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Quality Management / NC-CAPA Boundary

### Q484. What corrective-action linkage is required?

**Reconciled Answer:** Keep minimum controlled investigation/CAPA linkage; do not create a general enterprise CAPA subsystem without approved need.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Quality Management / NC-CAPA Boundary

### Q485. What preventive-action linkage is required, if any?

**Reconciled Answer:** Keep minimum controlled investigation/CAPA linkage; do not create a general enterprise CAPA subsystem without approved need.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Quality Management / NC-CAPA Boundary

### Q486. Are CAPA records required in v1?

**Reconciled Answer:** Keep minimum controlled investigation/CAPA linkage; do not create a general enterprise CAPA subsystem without approved need.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Quality Management / NC-CAPA Boundary

### Q487. Are control charts required?

**Reconciled Answer:** Keep minimum controlled investigation/CAPA linkage; do not create a general enterprise CAPA subsystem without approved need.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Quality Management / NC-CAPA Boundary

### Q488. Are trend charts required?

**Reconciled Answer:** Keep minimum controlled investigation/CAPA linkage; do not create a general enterprise CAPA subsystem without approved need.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Quality Management / NC-CAPA Boundary

### Q489. Are Westgard or similar rules required?

**Reconciled Answer:** Keep minimum controlled investigation/CAPA linkage; do not create a general enterprise CAPA subsystem without approved need.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Quality Management / NC-CAPA Boundary

### Q490. Are statistical QC calculations required?

**Reconciled Answer:** Keep minimum controlled investigation/CAPA linkage; do not create a general enterprise CAPA subsystem without approved need.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Quality Management / NC-CAPA Boundary

### Q491. Which QC capabilities are explicitly out of scope?

**Reconciled Answer:** Keep minimum controlled investigation/CAPA linkage; do not create a general enterprise CAPA subsystem without approved need.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Quality Management / NC-CAPA Boundary

### Q492. Must QC records be linked to the exact TestInstance?

**Reconciled Answer:** Yes. QC records shall be linked to the exact **TestInstance** whenever the QC activity is performed for, associated with, or used to determine the validity of a specific execution.
Where QC is broader than one TestInstance, such as an equipment-level, batch-level, run-level, or environmental QC event, the QC record shall retain the appropriate higher-level context and explicit links to affected TestInstances where applicable.

QC records shall never be stored as untraceable standalone pass/fail values.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q493. Must QC records be linked to equipment or MethodVersion?

**Reconciled Answer:** Yes. Where relevant, QC records shall be linked to the exact **Equipment** and/or **MethodVersion** involved.

The applicable linkage shall depend on the QC type and shall preserve sufficient context to reconstruct:
- which QC was performed;
- for which TestDefinition/TestInstance or work group;
- using which Equipment;
- under which MethodVersion;
- at what date/time;
- by whom;
- under which applicable QC configuration.

The Launch QC / QC Configuration Matrix shall define which relationships are mandatory for each QC type.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q494. Must failed QC history be preserved even when the result is later accepted?

**Reconciled Answer:** Yes. Failed QC history shall always be preserved, even when the affected result is later accepted through an authorized disposition.

The system shall preserve:
- the original QC failure;
- date/time;
- actor;
- measured/observed value or outcome;
- applicable acceptance criterion;
- affected TestInstance(s);
- investigation/disposition;
- justification where acceptance was permitted;
- subsequent corrected/repeated QC result;
- relevant approval/evidence.

Later acceptance shall not erase or overwrite the original QC failure.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q495. What report types are required in v1?

**Reconciled Answer:** The v1 report types shall be frozen through the approved **Report Lifecycle, Composition and Issuance Model** and the laboratory's controlled report requirements.
At minimum, v1 shall support the laboratory's approved primary issued laboratory report format for completed work.
Additional report types, such as separate certificates or specialized reports, shall be included only where an actual v1 laboratory, customer, contractual, or technical requirement exists.
The report model shall not structurally assume that every Sample has exactly one report.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q496. Are reports called reports, test reports, certificates, or multiple document types?

**Reconciled Answer:** The laboratory shall approve the controlled terminology used for its issued reporting documents.

For v1, LabNexus shall support the approved report/document type(s), whether the laboratory uses terms such as:
- Laboratory Report;
- Test Report;
- Certificate;
- another controlled document type.

Where multiple document types are required, each shall have its own controlled identity, lifecycle, composition, and issuance rules.
The system shall not treat differing terminology as different technical concepts unless the laboratory's reporting requirements require distinct document types.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q497. Which report layouts are required?

**Reconciled Answer:** Required report layouts shall be defined through controlled report templates and the approved **Report Lifecycle, Composition and Issuance Model.**
The v1 report layout shall support the laboratory-approved primary report format and shall preserve the required technical, customer, traceability, approval, and accreditation information.
Where multiple layouts are genuinely required, each shall be separately controlled and versioned.
Report layout changes shall follow controlled report/template governance and shall not silently alter previously issued PDFs.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q498. What is the laboratory's official report format?

**Reconciled Answer:** The laboratory's official report format shall be the approved controlled report template/document version adopted for LabNexus.
The exact visual layout, wording, field placement, logos/marks, signatures/representations, disclaimers, and other presentation rules shall be derived from the laboratory's approved controlled reporting format rather than invented by the software project.
The exact approved template/document version shall be linked to each ReportRevision so that historical reports remain reconstructable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q499. Which fields appear in the report header?

**Reconciled Answer:** The report header shall contain the laboratory-approved identity and report-control information required for the issued report.

The controlled baseline should support, where applicable:
- laboratory/business identity;
- site identity;
- report/document number;
- report revision;
- issue date/time;
- customer identity;
- relevant project/request reference;
- sample/report context;
- required accreditation representation.

The exact header content and wording shall be approved through the controlled report template.
Historical issued reports shall retain the header representation that applied at issuance.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q500. Which customer information appears on reports?

**Reconciled Answer:** Customer information shown on reports shall be limited to the laboratory-approved reporting fields required for identification, communication, contractual requirements, and traceability.

The controlled report model should support, where applicable:
- customer legal/business name;
- customer code/reference;
- customer address or contact information where required;
- customer-specific reference/order identifier.

The exact customer information displayed shall be determined by the approved report template and customer/reporting requirements.
Historical reports shall preserve the customer representation used at issuance.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q501. Which project/contract information appears on reports?

**Reconciled Answer:** Project/Contract information shall appear on reports where required for traceability, contractual identification, or customer reporting.

The report model should support, where applicable:
- Project identifier/name;
- Contract/reference number;
- Request identifier;
- customer order/reference;
- other approved engagement identifiers.

Only fields approved for reporting shall be rendered.
The exact values used in an issued report shall be frozen within the ReportRevision/report snapshot rather than taken from later mutable master data.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q502. Which sample identification fields appear on reports?

**Reconciled Answer:** Reports shall display the laboratory-approved Sample identification fields necessary for unambiguous sample traceability.
At minimum, the report model shall support the authoritative internal Sample ID and the approved customer/external Sample ID where applicable.
Additional sample information such as sample description, matrix, receipt/collection information, or other identifiers shall be included where required by the approved report template or applicable technical/customer requirements.
Historical report snapshots shall preserve the exact sample identity representation used at issuance.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q503. Which test/method fields appear on reports?

**Reconciled Answer:** Reports shall display the TestDefinition and method information required by the laboratory's approved reporting requirements.

The report model shall support, where applicable:
- Test name;
- Test Code;
- Method/MethodVersion reference;
- applicable method edition/revision;
- required technical test description;
- other approved technical identifiers.

The exact method representation shall be frozen in the ReportResultSnapshot/ReportRevision rather than regenerated from mutable current configuration.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q504. Which result fields appear on reports?

**Reconciled Answer:** Reports shall display the approved reportable result fields for each applicable TestDefinition.

The report result representation shall support, where applicable:
- value;
- qualifier;
- unit;
- required precision/rounding;
- applicable reference/specification information;
- detection-limit information;
- uncertainty information where required;
- result status/interpretation where approved.

Only approved reportable outputs shall be rendered.

The issued report shall preserve the exact value and representation that was approved.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q505. Which units appear on reports?

**Reconciled Answer:** Units displayed on reports shall come from controlled unit definitions and the approved TestDefinition/Parameter configuration.
The report shall use the unit applicable to the reportable result and shall not derive a different unit from mutable current configuration after issuance.
Where unit conversion is performed, the result and conversion/provenance shall remain traceable to the underlying controlled calculation/result.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q506. Which qualifiers appear on reports?

**Reconciled Answer:** Result qualifiers shall be displayed where required by the approved parameter/result configuration and applicable reporting rules.

The model shall support structured qualifiers such as, where applicable:
- less-than;
- greater-than;
- non-detect;
- estimated/qualified result;
- other approved result qualifiers.

Qualifiers shall remain distinct from the underlying numeric/text result value and shall be rendered according to the controlled report template.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q507. Which uncertainty information is required, if any?

**Reconciled Answer:** Uncertainty information shall be displayed only where required by the applicable laboratory method, technical procedure, customer requirement, accreditation/reporting rule, or approved report template.
The system shall support controlled uncertainty representation where applicable, including the appropriate value/unit or associated statement.
LabNexus shall not invent uncertainty values or assume that every reported result requires uncertainty.
The reporting requirement shall be defined per applicable TestDefinition/Parameter where necessary.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q508. Which detection-limit information is required, if any?

**Reconciled Answer:** Detection-limit information shall be included where required by the applicable method, parameter definition, laboratory reporting rule, customer requirement, or approved report template.
Where applicable, the report shall distinguish the relevant detection/decision limit information from the actual result and qualifier.
The underlying structured detection-limit information shall not be represented only as free text.
Exact terminology and reporting representation shall be controlled by the applicable technical/reporting configuration.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q509. Which method references appear on reports?

**Reconciled Answer:** Method references appearing on reports shall come from the controlled Method/MethodVersion configuration applicable to the TestInstance.
The report shall preserve the exact method reference/edition used for the reported work, including any approved laboratory implementation representation required by the report.
A later method revision shall not change the method reference shown on a previously issued report.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q510. Which accreditation representation appears on reports?

**Reconciled Answer:** Accreditation representation on reports shall be determined from the resolved, effective accreditation scope applicable to the reportable work and the approved report template/configuration.

The report shall preserve the exact historical accreditation representation used at issuance, including where applicable:
- accredited/non-accredited status;
- applicable scope representation;
- approved wording;
- approved accreditation mark/logo;
- required limitations or qualifications.

LabNexus shall not independently create an accreditation claim.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q511. Which analyst information appears on reports?

**Reconciled Answer:** Analyst information displayed on reports shall follow the laboratory's approved reporting requirements.
Where analyst identity is required, the report should preserve the approved representation of the responsible analyst or analysts, based on the TestInstance record and controlled report snapshot.
The exact historical identity displayed shall remain reconstructable even if the user's name, role, or account information changes later.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q512. Which reviewer/verifier/approver information appears on reports?

**Reconciled Answer:** Reviewer, Verifier, and Approver information displayed on reports shall be governed by the approved report template and laboratory reporting policy.

Where required, the report shall preserve the approved representation of:
- reviewer;
- verifier;
- approver/authorized signatory;
- relevant approval date/time.

The report shall derive these values from the controlled approval history and ReportRevision snapshot rather than mutable current user-role data.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q513. Are signatures printed, rendered, represented by names, or handled another way?

**Reconciled Answer:** Signature representation on reports shall follow the laboratory's approved controlled reporting policy.

The system shall support the approved representation, which may include:
- printed name;
- role/title;
- controlled electronic signature representation;
- signature image where specifically approved;
- another controlled representation.

The report's displayed signature representation shall correspond to the underlying attributable approval event and shall not create an independent or misleading signature record.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q514. Are electronic signatures required on the PDF itself?

**Reconciled Answer:** Electronic signatures shall be supported according to the laboratory's approved electronic-signature policy.
Whether the PDF itself contains a cryptographic/electronic signature or instead contains a controlled visual representation of an application-recorded electronic approval shall be explicitly decided before report implementation.
The underlying authoritative approval event remains the application approval record, and the exact PDF/report representation shall be frozen with the issued ReportRevision.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q515. Are report page numbers required?

**Reconciled Answer:** Issued reports shall use controlled page numbering where required by the laboratory's approved report format.
The report rendering system should support page numbering and total-page representation so that the issued PDF provides a stable document boundary.
Exact page-number format shall be controlled by the approved report template.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q516. Are document numbers required?

**Reconciled Answer:** A controlled report/document number shall be assigned to each issued report where required by the laboratory's numbering policy.

The report number shall be:
- system-controlled;
- unique within the deployment;
- immutable after issuance;
- historically reconstructable;
- distinct from the ReportRevision number where both are required.

The exact numbering format shall be defined in the approved Numbering and Identifier Allocation Matrix.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q517. Are report revision numbers displayed?

**Reconciled Answer:** Report revision numbers shall be controlled and shall be displayed where required by the approved report format.
Where revision numbering is displayed, each ReportRevision shall have a unique sequential revision designation and shall preserve its relationship to the underlying Report.
A later revision shall not overwrite the historical revision number or issued report artifact.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q518. Is issue date required?

**Reconciled Answer:** An issue date shall be required for an issued report.
The issue date shall represent the controlled date on which the particular ReportRevision was formally issued.
The issued date shall be preserved in the ReportRevision/snapshot and shall not change if the report is later superseded or corrected.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q519. Is issue time required?

**Reconciled Answer:** An issue time shall be recorded for an issued report to provide precise issuance traceability.
The issue timestamp shall be system-recorded using the approved laboratory time-zone convention and shall be preserved with the ReportRevision and issuance audit event.
The timestamp shall not be replaced by a later regeneration time.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q520. Is reissue/correction status displayed?

**Reconciled Answer:** Yes. Where a report is a correction, reissue, replacement, withdrawal-related revision, or other non-original report state, that status shall be clearly represented according to the approved report lifecycle.
The report shall identify its current revision/status and preserve the relationship to prior ReportRevisions.
The exact customer-facing wording shall be controlled by the approved report template.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q521. How is a revised report identified to customers?

**Reconciled Answer:** A revised report shall be identifiable through a combination of controlled report number, ReportRevision, issue date, and approved revision/reissue wording.
Where required by laboratory policy, the revised report shall explicitly state that it supersedes or revises a previous report.
The identification shall allow the customer and internal staff to distinguish the revised report from the earlier issued artifact without ambiguity.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q522. Must the previous report number be referenced in a revised report?

**Reconciled Answer:** Where a revised report replaces or corrects an earlier issued report, the revised ReportRevision shall retain an explicit relationship to the previous ReportRevision.
Where required by the laboratory's approved reporting policy, the previous report number/revision shall be displayed on the revised report.
The historical relationship shall always be retained internally even if the previous report number is not displayed to the customer.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q523. What statement explains corrections or reissues?

**Reconciled Answer:** The correction/reissue statement shall be controlled through the approved report template and report lifecycle policy.

It shall clearly identify, where applicable:
- that the report is revised/corrected;
- the affected report/revision;
- the reason or category of correction where required;
- the issue/revision date;
- any required statement regarding supersession of the previous report.

LabNexus shall not invent regulatory correction wording; the exact approved wording shall be supplied through controlled configuration.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q524. What statement explains accreditation status?

**Reconciled Answer:** The accreditation statement on a report shall be derived from the resolved accreditation configuration and approved report wording.
It shall accurately distinguish accredited and non-accredited work and shall use only laboratory-approved wording/marks.
The wording shall remain historically frozen in each issued ReportRevision.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q525. Are disclaimers or laboratory notes required?

**Reconciled Answer:** Disclaimers and laboratory notes shall be supported where they are required by the approved report template, laboratory policy, customer requirements, method requirements, or accreditation/reporting rules.

Controlled notes shall be distinguishable from:
- technical result values;
- regulatory/accreditation claims;
- correction statements;
- ordinary report narrative.

Required controlled disclaimers shall be versioned with the report template and historically preserved in issued reports.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q526. Are customer-specific report formats required?

**Reconciled Answer:** Customer-specific report formats may be supported where there is an approved v1 customer or contractual requirement.
Such formats shall be implemented as controlled report templates/configurations and shall not require bespoke code for each customer where the requirement can be represented through the approved report-template model.
Customer-specific formatting shall not be permitted to alter controlled technical meaning, approval, accreditation, or traceability rules.
Each approved customer-specific format shall have explicit ownership, versioning, approval, and historical applicability.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q527. Are discipline-specific report templates required?

**Reconciled Answer:** Discipline-specific report templates shall be supported where genuinely required by approved laboratory or reporting requirements.
The v1 architecture shall permit different controlled templates for Solid Fuel, Solid Biofuel, and other approved disciplines without changing the underlying report lifecycle or result-snapshot model.
Discipline-specific templates shall be versioned, approved, effective-dated, and historically reconstructable.
No discipline-specific template shall introduce uncontrolled technical or accreditation behavior outside the approved configuration model.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q528. Are attachments part of issued reports?

**Reconciled Answer:** Attachments shall be part of issued reports only where explicitly included by the approved report composition/configuration.
The ReportRevision shall identify which attachments, if any, form part of the issued report package and shall preserve their exact DocumentVersion/file identity and integrity information.
An attachment shall not be considered part of an issued report merely because it happens to exist in the LIMS.
Where attachments form part of the issued report package, their inclusion, ordering, identity, and integrity shall be frozen and reconstructable with the ReportRevision.
Unattached or independently retained source documents shall remain separate controlled records unless explicitly incorporated into the issued report package.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q529. Are raw data or worksheets ever included with reports?

**Reconciled Answer:** Raw data and worksheets may be included with a report where required by the approved laboratory, customer, contractual, technical, or regulatory reporting requirement.
Where included, each raw-data/worksheet attachment shall be treated as a controlled report component with explicit identity, DocumentVersion, integrity information, and relationship to the relevant ReportRevision.
Raw data or worksheets shall not be included merely because they exist in the LIMS.
Where they are part of an issued report package, their exact inclusion and version shall be frozen and historically reconstructable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q530. Is a certificate separate from the main report for any test type?

**Reconciled Answer:** A certificate may be represented as a separate controlled report/document type where an approved laboratory, customer, contractual, or technical requirement requires it.
Where a certificate is functionally part of the laboratory's normal test-report output, it may instead be represented through the primary Report/ReportRevision model.
The exact v1 document types shall be approved through the Report Lifecycle, Composition and Issuance Model.
Separate certificate types shall have controlled identity, lifecycle, template/version, approval, issuance, and historical reconstruction rules.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q531. Which report elements are frozen in ReportResultSnapshot?

**Reconciled Answer:** The ReportResultSnapshot shall freeze every report-visible result attribute needed to reconstruct exactly what was reported.

At minimum, this shall include, where applicable:
- ReportRevision linkage;
- Result;
- exact ResultRevision;
- TestDefinition/report representation;
- reported value;
- qualifier;
- unit;
- precision/rounded value;
- applicable reference/specification information;
- detection-limit information where reported;
- uncertainty information where reported;
- analyst representation where reported;
- approval timestamp/reference;
- accreditation representation;
- other report-visible technical attributes.

The snapshot shall not depend on later mutable Result, TestDefinition, MethodVersion, or configuration state.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q532. Which elements are generated dynamically at report rendering time?

**Reconciled Answer:** Only genuinely presentation-time information may be generated dynamically during report rendering.

Dynamic rendering may include deterministic presentation elements such as:
- page numbers;
- page count;
- document rendering layout;
- approved static headers/footers;
- other non-technical presentation elements explicitly allowed by the report model.

Technical, approval, accreditation, identity, and report-visible result information shall be frozen before issuance and shall not be resolved from mutable current data at rendering time.
The rendered PDF itself shall then be persisted, hashed, verified, and linked to the ReportRevision.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q533. Must reports be reproducible byte-for-byte, or only semantically equivalent?

**Reconciled Answer:** The authoritative requirement is **exact issued-artifact preservation**, not an absolute requirement that every future re-render produce byte-for-byte identical PDF bytes.
For every issued ReportRevision, LabNexus shall preserve the exact PDF artifact that was actually issued, together with its SHA-256 hash and report/artifact identity.
Within the same controlled rendering environment, deterministic rendering should be targeted and tested. However, future Chromium/font/template changes may legitimately produce different byte representations.
Therefore:
* Previously issued PDF bytes remain authoritative;
* Re-rendering is not permitted to overwrite them;
* Historical report reconstruction retrieves the stored issued artifact;
* Any newly generated PDF is a new artifact and must be independently persisted/verified.

Semantic equivalence alone is insufficient for historical issuance; exact artifact preservation is mandatory.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q534. Must the exact PDF file hash be stored?

**Reconciled Answer:** Yes. The exact issued PDF bytes shall have a **SHA-256 hash** recorded in the report artifact metadata.
The hash shall be calculated from the final persisted PDF bytes.

The system shall use the hash for:
* Integrity verification;
* Backup/restore verification;
* Artifact identification;
* Detection of unintended modification;
* Historical evidence.

A changed hash means changed PDF bytes. The prior artifact must never be silently overwritten.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q535. What PDF metadata must be stored?

**Reconciled Answer:** Issued PDF metadata shall include controlled non-sensitive information appropriate to the artifact, including where technically supported:
* Laboratory identity;
* Report number;
* Report revision;
* Report title/type;
* Issue date/time;
* Author/issuer representation where approved;
* PDF creation metadata where useful.

The authoritative report identity remains the LabNexus ReportRevision and persisted artifact record, not PDF metadata alone.
Metadata shall not contain unnecessary confidential information, passwords, internal secrets, or uncontrolled implementation details.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q536. What file naming convention is required for issued PDFs?

**Reconciled Answer:** Issued PDF filenames shall be generated by the system and shall not be the authoritative identifier.

Recommended format:
`<ReportNumber>-R<Revision>.pdf`

For example:
`RPT-00012345-R1.pdf`

Where necessary, an internal immutable artifact identifier may be used in the physical storage path to avoid collisions and filesystem-name dependencies.
The filename shall be deterministic enough for human handling while remaining subordinate to the ReportRevision/artifact identity.
Issued files shall never be renamed by ordinary users through direct filesystem access.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q537. How are report files delivered?

**Reconciled Answer:** LabNexus shall support controlled report delivery through:
* Browser-controlled download;
* Controlled printing;
* Manual transfer/export where authorized.

Electronic delivery through email shall **not be a mandatory v1 dependency** because the system is offline-first.
Where email is later approved, delivery shall be treated as a separate controlled event and shall not redefine the authoritative issued report.
Delivery records should identify ReportRevision, recipient/destination where applicable, actor/system, timestamp, delivery method, and outcome.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q538. Is email delivery required in v1?

**Reconciled Answer:** No. **Email delivery is not required for v1.**

The core report lifecycle shall work completely offline:
**Approved → PDF generated → persisted → hashed → verified → issued → authorized download/print/manual delivery**

No report shall depend on SMTP, Internet connectivity, cloud email, or an external messaging service.
Email delivery may be added later as a controlled integration without changing the authoritative report/issuance model.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q539. Is printer output required?

**Reconciled Answer:** Yes, controlled printer output shall be supported where the laboratory needs physical reports.
Printing shall be a delivery/presentation function and shall not be required for report issuance.
The authoritative issued record remains the persisted ReportRevision/PDF artifact. A failed printer operation must not change report issuance status or require re-approval.
Where technically observable, application-controlled printing may be recorded as a delivery event.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q540. Is manual download/USB delivery required?

**Reconciled Answer:** Yes. Authorized users shall be able to **manually download/copy an issued report for controlled delivery**, including transfer through approved removable media where the laboratory's operational procedure permits it.
Manual delivery shall remain subject to authorization and confidentiality controls.
The application shall record the controlled download/export event where the delivery occurs through LabNexus.
The LIMS cannot guarantee physical handling after a file leaves the application's controlled environment, so the laboratory's external delivery/custody procedure remains part of the control boundary.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q541. Who can issue a report?

**Reconciled Answer:** Only an authorized **Authorized Signatory/report issuer** shall be permitted to issue a report.
Issuance permission shall be separate from ordinary report viewing, drafting, result entry, Review, Verification, and general system administration.

Before issuing, the backend shall verify:
* ReportRevision state;
* Required Result/ResultRevision approvals;
* Required ApprovalSnapshot;
* SoD;
* Issuer authorization;
* Report completeness;
* Artifact persistence;
* Artifact hash;
* Artifact integrity verification;
* Absence of blocking report-impact conditions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q542. Who can reissue a report?

**Reconciled Answer:** Report reissue shall require a dedicated **Report Reissue** permission and shall be available only to authorized report issuers/signatories or explicitly designated Quality/Technical authority according to the report governance policy.
A reissue shall never modify the original issued ReportRevision.
Where technical/report content changes, the reissue shall create a new ReportRevision with explicit linkage to the previous revision and the reason for reissue.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q543. Who can void a report?

**Reconciled Answer:** There shall be **no generic destructive `Void` operation for issued reports**.

Where an issued report must be invalidated, the approved v1 mechanism shall be **controlled withdrawal** with:
* Authorized actor;
* Reason;
* Timestamp;
* Impact assessment;
* Customer/recipient notification where required;
* Link to any replacement ReportRevision;
* Preservation of the original issued PDF and history.

Thus, no ordinary user is given a `Void Report` operation that removes the report from history.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q544. Can an issued report ever be deleted?

**Reconciled Answer:** No. **An issued report shall never be deleted through normal application operation.**
Its ReportRevision, ReportResultSnapshots, approval relationships, exact issued PDF, hash, delivery history, and audit history shall remain preserved for the applicable retention period.
Destruction after retention expiry is a separate controlled records-destruction process and must not be confused with report deletion.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q545. What happens when a report was generated but not issued?

**Reconciled Answer:** A generated but not-yet-issued report shall remain in a **non-issued ReportRevision/artifact state**.

The system shall clearly distinguish:
* Generated;
* Persisted;
* Verified;
* Issued.

A generated PDF that has not completed issuance controls is not an issued laboratory report.
It may be retained as a draft/non-issued artifact for troubleshooting or workflow continuation, subject to controlled access. It must not be presented as an authoritative issued report.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q546. What happens when report generation fails?

**Reconciled Answer:** If PDF generation fails:
* The ReportRevision shall not enter `ISSUED`;
* The failure shall be recorded;
* No partial PDF shall become authoritative;
* Technical diagnostic information shall be retained in controlled evidence without exposing internals to ordinary users;
* The report shall enter an appropriate failure/recovery state;
* Authorized personnel may retry generation after the cause is addressed.

A failed rendering attempt shall not modify the underlying approved result or ApprovalSnapshot.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q547. What happens when PDF storage fails after approval?

**Reconciled Answer:** If PDF storage fails after approval, the report shall **remain non-issued**.
Approval of the technical result is not sufficient to declare the report issued.
The system shall retain the approved Result/ApprovalSnapshot and ReportRevision while the artifact remains in a recovery-required/non-issued state.
After storage is successfully completed, the exact bytes shall be hashed and verified before issuance.
No partially written or unverified PDF may receive `ISSUED` status.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q548. Must report issuance be atomic with snapshot creation and artifact recording?

**Reconciled Answer:** Yes, report issuance shall have **logical atomicity**, but it cannot depend on a literal single ACID transaction spanning SQLite and the filesystem.

The controlled issuance protocol shall be:
**Prepare ReportRevision → create/freeze snapshots → render → persist exact PDF → calculate hash → verify artifact → commit authoritative issuance state → record issuance event**

If any required step fails, the ReportRevision shall remain non-issued/recovery-required.
A database transaction shall atomically commit the database-side state and issuance event. The application shall use explicit recovery/verification logic to bridge the database/filesystem boundary.
This prevents the system from claiming `ISSUED` when the exact PDF does not exist, cannot be verified, or is not linked correctly.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q549. What event creates a new ReportRevision?

**Reconciled Answer:** A new ReportRevision shall be created whenever a new reportable state must be preserved as a distinct report revision, including:
- initial report preparation where a report revision is established;
- a corrected/revised report;
- a reissued report containing changed report-visible content;
- another controlled report change requiring historical preservation.

A new ReportRevision shall not be created merely because the PDF is regenerated without any change to the approved report state.
The exact ReportRevision creation triggers shall be defined in the Report Lifecycle, Composition and Issuance Model.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q550. Is every issuance a new ReportRevision?

**Reconciled Answer:** Not every issuance event necessarily creates a new ReportRevision.
A ReportRevision represents a distinct controlled report state. Issuance is an event/lifecycle transition applied to that revision.
If the same already-prepared ReportRevision is issued after successful verification of the exact persisted artifact, no additional revision is required merely because the issuance action occurred.
A new ReportRevision is required when the report-visible content/state changes and must be preserved as a separate revision.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q551. Is a corrected report always a new ReportRevision?

**Reconciled Answer:** Yes. A corrected report shall always be represented as a new ReportRevision.
The previous issued ReportRevision and PDF shall remain historically intact.
The new revision shall identify its relationship to the prior revision and shall preserve the reason, correction/reissue history, new report snapshot, approval state, and exact issued PDF.
A correction shall never overwrite an existing issued ReportRevision.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q552. Can a ReportRevision be drafted without being issued?

**Reconciled Answer:** Yes. A ReportRevision may exist in a controlled draft/pre-issuance state.
A draft ReportRevision shall not be treated as issued and shall not become the authoritative issued report until the required workflow, approval, PDF generation, persistence, integrity verification, and issuance controls are completed.
Draft revisions shall remain distinguishable from issued revisions and shall not be visible as authoritative issued reports.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q553. What status values exist for ReportRevision?

**Reconciled Answer:** ReportRevision shall use a controlled lifecycle. At minimum, the model should support:

**DRAFT → READY_FOR_ISSUANCE → ARTIFACT_PERSISTED → ARTIFACT_VERIFIED → ISSUED**

with controlled exceptional states such as:
- GENERATING;
- ISSUANCE_FAILED;
- RECOVERY_REQUIRED;
- WITHDRAWN;
- SUPERSEDED where required by the approved report model.

A ReportRevision shall not be ISSUED unless the exact PDF artifact has been persisted, hashed, verified, and linked.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q554. Can an issued ReportRevision ever return to draft?

**Reconciled Answer:** No. An issued ReportRevision shall never return to Draft.
If changes are required after issuance, the system shall create a new ReportRevision through the approved correction/reissue/replacement process.
The previously issued revision and artifact shall remain historically preserved.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q555. Who may create a ReportRevision?

**Reconciled Answer:** A ReportRevision may be created only by an authorized user or controlled system workflow with the appropriate report permissions.
Creation of a draft ReportRevision does not itself constitute approval or issuance.
The actor, timestamp, source report/revision where applicable, and applicable authorization context shall be recorded.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q556. Who may issue it?

**Reconciled Answer:** Only an authorized report issuer/Authorized Signatory may issue a report.
Issuance shall require all applicable technical Review, Verification, Approval, report checks, and artifact-integrity controls to have been satisfied.
The issuing action shall generate an immutable issuance event linked to the exact ReportRevision and persisted PDF artifact.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q557. Can a ReportRevision contain a mixture of current and historical ResultRevisions?

**Reconciled Answer:** A ReportRevision shall not contain an uncontrolled mixture of mutable current results and historical ResultRevisions.
Each ReportResultSnapshot shall refer to the exact ResultRevision used for that report state.
A report may legitimately contain different ResultRevisions for different results where those exact revisions were approved for inclusion in that ReportRevision, but every included result shall have an explicit historical reference.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q558. Must every ReportResultSnapshot refer to an exact ResultRevision?

**Reconciled Answer:** Yes. Every ReportResultSnapshot shall refer to the exact ResultRevision represented in that ReportRevision.
The relationship shall be explicit and immutable after the report revision is finalized.
A ReportResultSnapshot shall not rely on the current live Result alone because later corrections must not alter the meaning of an earlier issued report.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q559. What other report-level snapshots are required?

**Reconciled Answer:** In addition to Result snapshots, the ReportRevision shall freeze all report-level information necessary for historical reconstruction.

This shall include, as applicable:
- report identity and revision;
- customer/project/sample representation;
- TestDefinition/method representation;
- accreditation representation;
- analyst/reviewer/verifier/approver representation;
- report dates/timestamps;
- controlled template/DocumentVersion;
- report-visible notes/disclaimers;
- attachment membership;
- exact issued PDF artifact and integrity hash.

Only information necessary for deterministic reconstruction shall be frozen; mutable operational data that is not report-visible need not be duplicated.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q560. Must customer/project/sample metadata also be frozen?

**Reconciled Answer:** Yes. Customer, project, contract, request, and sample information that appears in a report shall be frozen in the ReportRevision/report snapshot as report-visible historical data.
This prevents later master-data changes from altering the historical meaning of an issued report.
The snapshot shall preserve the exact representation used at issuance rather than merely referencing current Customer/Project/Sample data.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q561. Must method and accreditation metadata be frozen?

**Reconciled Answer:** Yes. Method and accreditation metadata that is report-visible shall be frozen in the ReportRevision/report snapshot.

This shall preserve, where applicable:
- Method/MethodVersion representation;
- method edition/revision;
- resolved accreditation status;
- applicable scope representation;
- approved accreditation wording/mark information.

Later method or accreditation configuration changes shall not alter an issued report's historical representation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q562. Must analyst/approver identity be frozen?

**Reconciled Answer:** Yes. Analyst and approval-chain identities that are displayed or otherwise required for report reconstruction shall be frozen in the ReportRevision/report snapshot.
The snapshot shall preserve the identity representation used at issuance, including the relevant role/title and approval relationship where applicable.
Later changes to user name, role, authorization, or account status shall not alter the historical report.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q563. Must timestamps be frozen?

**Reconciled Answer:** Yes. Report-relevant timestamps shall be frozen.

This includes, where applicable:
- report creation/preparation timestamp;
- approval timestamp;
- issue timestamp;
- relevant sample/test dates displayed on the report;
- revision timestamp;
- other report-visible controlled dates/times.

The canonical internal timestamp shall remain UTC, with the approved laboratory timezone used for user-facing representation where applicable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q564. Must document version and PDF hash be frozen?

**Reconciled Answer:** Yes. The exact controlled DocumentVersion/template and exact issued PDF artifact shall be frozen and linked to the ReportRevision.
The issued PDF shall have an integrity hash and sufficient metadata to identify the exact persisted artifact.
A later template change, document change, or PDF regeneration shall not alter the historical association of the issued ReportRevision.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q565. What happens if the source result changes after report creation but before issuance?

**Reconciled Answer:** If the source Result changes after a ReportRevision has been created but before it is issued, the pending ReportRevision shall **not be issued using stale data**.

The system shall:
1. Detect/validate the ResultRevision change;
2. Compare the pending ReportRevision's exact result references against the newly effective approved state;
3. Mark the pending report revision as invalid/stale or otherwise require regeneration;
4. Perform report-impact assessment;
5. Create/update the appropriate new ReportRevision;
6. Regenerate and verify the PDF;
7. Require the applicable issuance controls again.

The previously generated non-issued artifact may be retained as technical evidence but must never be confused with the final issued report.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q566. What happens if the source result changes after issuance?

**Reconciled Answer:** If the source result changes after a report has been issued, the issued ReportRevision shall remain unchanged.
The corrected Result/ResultRevision shall trigger a controlled impact assessment to identify affected reports.
Where the correction affects an issued report, a new ReportRevision shall be created through the controlled correction/reissue process.
The original issued PDF shall remain preserved and identifiable as the earlier issued state.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q567. How are affected report revisions found?

**Reconciled Answer:** Affected report revisions shall be identified through explicit ReportResultSnapshot relationships linking each ReportRevision to the exact ResultRevision represented in that report.
A result correction shall therefore allow the system to query all ReportRevisions containing the affected Result/ResultRevision.
The relationship shall also support identification of issued PDFs and downstream report revisions requiring assessment.
Affected-report discovery shall not depend on comparing rendered PDF text.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q568. What is the formal process for corrected reports?

**Reconciled Answer:** The formal corrected-report process shall be:
**Identify correction → identify affected ResultRevision/report revisions → assess impact → authorize correction → create corrected ResultRevision where applicable → complete required Review/Verification/Approval → create new ReportRevision → freeze new snapshots → generate/persist/verify exact PDF → issue corrected report → preserve prior issued report.**
The original report shall never be overwritten.
The new report shall clearly identify its correction/revision relationship according to the approved report policy.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q569. What is the formal process for withdrawing/recalling an issued report?

**Reconciled Answer:** Withdrawal/recall of an issued report shall be a controlled event.

The process shall:
- identify the affected ReportRevision;
- record the reason;
- identify the authorizing authority;
- preserve the original issued report and PDF;
- change the report lifecycle state to the approved withdrawal state;
- record customer/internal notification or delivery implications where applicable;
- identify whether a replacement/corrected report is required;
- preserve the full audit trail.

Withdrawal shall not delete or destroy the previously issued artifact.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q570. Is report withdrawal allowed?

**Reconciled Answer:** Yes. Report withdrawal shall be supported as a controlled lifecycle action where the laboratory determines that an issued report must no longer be treated as the current valid report.
Withdrawal shall require authorization and documented reason.
The withdrawn report remains permanently retrievable as historical evidence and shall be clearly identified as withdrawn.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q571. If withdrawal is allowed, what status and evidence are required?

**Reconciled Answer:** A withdrawn report shall have a distinct controlled status such as **WITHDRAWN** or another approved equivalent.

Required evidence shall include:
- Report/ReportRevision identity;
- exact issued PDF;
- withdrawal reason;
- authorizing user;
- date/time;
- relevant approval/reference;
- affected ResultRevision(s), where applicable;
- customer/delivery impact where applicable;
- replacement report relationship where applicable.

The withdrawn report shall never be silently returned to Draft or deleted.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q572. Can customers see report revision history through the system?

**Reconciled Answer:** Customer access to report revision history shall be controlled and shall not automatically expose the full internal revision/audit history.
The system shall support a defined customer-facing representation where the laboratory chooses to provide prior report revisions.
The customer-visible history shall include only the information approved for external disclosure.
Internal historical reconstruction shall remain available to authorized laboratory personnel independently of customer-facing visibility.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q573. Must internal staff see all report revisions?

**Reconciled Answer:** Authorized internal staff shall have access to the report history required for their role and responsibilities.
Users shall not automatically receive unrestricted access merely because they are staff.
Access shall be controlled by role/permission and confidentiality requirements, while privileged Quality/Technical/administrative roles may access the complete report revision history needed for investigation, audit, correction, and reconstruction.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q574. What is the retention requirement for superseded PDFs?

**Reconciled Answer:** Superseded and withdrawn PDFs shall remain retained for the same controlled retention period applicable to issued reports, unless a formally approved retention rule establishes a longer or otherwise specific requirement.
The exact issued PDF shall remain retrievable and integrity-verifiable throughout its required retention/archive period.
Superseded PDFs shall never be deleted merely because a newer report revision exists.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q575. What document types must the system support?

**Reconciled Answer:** The v1 document system shall support a controlled, typed set of document types rather than unrestricted arbitrary document relationships.

At minimum, the model shall support categories required for:
- controlled laboratory/QMS documents;
- method/SOP documents;
- equipment/calibration/maintenance evidence;
- sample/request supporting documents;
- TestInstance/technical evidence;
- QC evidence;
- report/document artifacts and attachments;
- accreditation evidence;
- migration evidence;
- configuration/change evidence;
- recovery/backup evidence where applicable.

The exact closed document-type set shall be defined in the DocumentLink Entity / Relationship Matrix.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q576. What is the difference between Document and Attachment in laboratory practice?

**Reconciled Answer:** A **Document** is a controlled logical document identity/versioned record maintained by the LIMS, such as an SOP, method document, certificate, report artifact, or other controlled document.
An **Attachment** is a file or supporting document associated with another controlled business record and does not necessarily have an independent controlled-document lifecycle.
Where an attachment itself requires controlled versioning, approval, retention, or historical identity, it shall be represented through the appropriate Document/DocumentVersion model rather than treated as an arbitrary file.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q577. What documents are controlled documents?

**Reconciled Answer:** Controlled documents are documents whose content, version, approval, effective status, applicability, or retention is subject to the laboratory's document-control process.

Examples include:
- quality-system documents;
- SOPs;
- methods and method-support documents;
- controlled forms;
- controlled work instructions;
- approved report templates;
- other laboratory documents explicitly designated as controlled.

Controlled documents shall have appropriate versioning, approval, effective dates, and historical retention.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q578. What documents are technical records?

**Reconciled Answer:** Technical records are records that provide evidence of laboratory work, observations, calculations, results, equipment use, QC, review/verification/approval, or related technical activity.
A technical record may be structured data, an immutable event/snapshot, or a controlled document/attachment.
Documents that provide evidence of technical work may therefore be both documentary objects and technical records, but the classification and retention meaning shall remain explicit.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q579. Which documents require version control?

**Reconciled Answer:** Documents requiring version control include all controlled documents and any other documents whose historical content can affect laboratory work, technical interpretation, authorization, reporting, accreditation representation, or traceability.

Examples include:
- SOPs;
- method documents;
- controlled forms;
- report templates;
- approved configuration-support documents;
- accreditation-supporting documents.

Ordinary non-controlled administrative files need not use controlled DocumentVersion semantics unless required.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q580. Which documents require approval before use?

**Reconciled Answer:** Documents requiring approval before use shall be those whose content affects controlled laboratory operation, technical work, QMS requirements, authorization, accreditation representation, calculation/reporting behavior, or other controlled processes.
At minimum, controlled SOPs, methods, report templates, controlled technical procedures, and equivalent QMS-controlled documents shall not become effective until required approval is complete.
Approval requirements shall be defined by document type.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q581. Which documents require effective dates?

**Reconciled Answer:** Effective dates shall be required for controlled documents whose applicability changes over time or whose historical use must be reconstructable.

Effective dating shall be used, where applicable, for:
- SOPs;
- methods/supporting controlled documents;
- report templates;
- controlled procedures;
- other effective-dated laboratory controls.

Documents that are purely informational and have no controlled applicability period do not require artificial effective dates.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q582. Which documents require expiry/review dates?

**Reconciled Answer:** Expiry/review dates shall be required where the laboratory's document-control process requires periodic review or a defined validity period.

The document model shall support:
- next-review date;
- expiry/end date where applicable;
- review status;
- reviewer/approver;
- extension/revision action;
- retirement/supersession.

A document should not silently remain effective after an applicable mandatory expiry without an approved disposition.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q583. Who can upload documents?

**Reconciled Answer:** Document uploads shall be permitted only to authorized users according to document type and the user's role/permission.

Upload permission shall be distinct from:
- approval;
- activation/effectivity;
- retirement;
- deletion/voiding.

A user who uploads a controlled document shall not thereby gain authority to approve or make it effective unless the approved role permits both actions and the applicable SoD rules are satisfied.
All uploads shall be audited.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q584. Who can approve document versions?

**Reconciled Answer:** Document versions shall be approved by the designated authority appropriate to the document type.

Typical authority shall include:
- Quality Authority for QMS-controlled documents;
- Technical Authority for technical methods/procedures;
- designated report authority for controlled report templates;
- other formally assigned authority where required.

The proposer/uploader and approver should be different users for controlled documents where the applicable SoD policy requires independence.
Approval shall be recorded against the exact DocumentVersion.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q585. Who can retire document versions?

**Reconciled Answer:** Document versions shall be retired by an authorized document-control/Quality authority according to the document type and governing policy.

Retirement shall preserve:
- the exact DocumentVersion;
- effective period;
- retirement reason;
- actor;
- date/time;
- superseding DocumentVersion where applicable;
- affected links/uses where required.

Retirement shall not delete the historical document version.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q586. Can a document have multiple simultaneous active versions?

**Reconciled Answer:** No. A single controlled document identity shall not have multiple simultaneously effective versions for the same scope.
One approved version shall be the effective version for a given scope/time interval.
A draft or future version may coexist with the current effective version, but overlapping effective versions shall be prevented unless the document's controlled scope explicitly distinguishes them.
Historical versions remain available for reconstruction.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q587. Can a draft version exist while another version is effective?

**Reconciled Answer:** Yes. A draft DocumentVersion may exist while another DocumentVersion is currently effective.
The draft shall remain non-effective until review/approval and its effective date are satisfied.
The current effective version shall continue governing live controlled behavior until the new version becomes effective.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q588. What file types are allowed?

**Reconciled Answer:** V1 shall use a controlled allowlist of permitted file types rather than unrestricted file upload.

At minimum, the allowlist may support laboratory-appropriate formats such as:
- PDF;
- DOCX/DOC;
- XLSX/XLS;
- CSV;
- TXT;
- JPG/JPEG;
- PNG.

Executable files, scripts, installers, and other inherently executable content shall be prohibited unless a separately approved requirement establishes otherwise.
The exact v1 allowlist shall be controlled configuration and shall be enforced by the backend.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q589. What maximum file sizes are allowed?

**Reconciled Answer:** A maximum attachment size shall be enforced at the application level and through the reverse proxy/storage boundary.
For v1, a **50 MB maximum per uploaded file** is recommended as the default planning limit, with the ability to configure a lower limit where operationally appropriate.
Larger files shall not silently bypass the limit; they shall require a separately approved mechanism if a genuine laboratory requirement arises.
The limit shall apply consistently to uploads through all supported application paths.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q590. Are attachments virus/malware scanned locally?

**Reconciled Answer:** Yes. Uploaded attachments shall be subjected to local malware scanning before being treated as trusted application documents, using an approved local scanning mechanism that does not require mandatory Internet access.
The upload workflow shall preserve the scan outcome, timestamp/status, and applicable scanner information where available.
A file that fails scanning or cannot be safely assessed shall not be treated as a trusted document until an authorized disposition is completed.
The system shall not claim that a file is safe merely because an upload succeeded.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q591. Is antivirus integration required?

**Reconciled Answer:** Yes. V1 shall support integration with an approved local host malware-scanning mechanism, such as the Windows security/antivirus facility available on the production host.
The integration shall not create a mandatory Internet dependency.

The security baseline shall define the required behavior for:
- successful scan;
- malware detection;
- scan failure;
- scanner unavailable;
- quarantine;
- retry/manual disposition.

Application-level controls shall complement, not replace, host filesystem and antivirus protections.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q592. How are files named and stored?

**Reconciled Answer:** Files shall be stored using application-controlled, non-user-selectable internal storage paths.
The logical Document/Attachment identity shall be stored in the database, while the physical file location shall remain an internal implementation detail.
File naming shall use collision-resistant system-generated identifiers rather than user-supplied filenames as the physical storage key.
The original filename may be retained as metadata for display and provenance.
Users shall never receive arbitrary filesystem paths as the storage mechanism.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q593. How are file hashes stored?

**Reconciled Answer:** Each stored file shall have an integrity hash, using a cryptographically appropriate hash such as **SHA-256**.
The hash shall be calculated from the exact persisted file bytes and stored with the corresponding Document/Attachment record.
The system shall use the hash for integrity verification, duplicate detection where applicable, backup/restore verification, and exact-artifact verification.
A changed file shall produce a different hash and shall not silently replace an existing controlled artifact.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q594. Are duplicate files permitted?

**Reconciled Answer:** Exact duplicate files shall not create uncontrolled duplicate content.
The system should detect identical file content using the stored content hash.
Where the same binary file is legitimately required in multiple controlled contexts, the system may allow multiple logical DocumentLink relationships while retaining one exact content identity where appropriate.
A duplicate upload shall not overwrite an existing controlled file or create ambiguous versions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q595. Are documents immutable after approval?

**Reconciled Answer:** Yes. An approved DocumentVersion shall be immutable.
After approval/effectivity, its file content shall not be edited or replaced in place.
Any substantive correction shall create a new DocumentVersion while preserving the previous version.
Only non-substantive administrative metadata changes that do not affect the document's content, meaning, applicability, approval, or historical interpretation may be handled through controlled metadata correction, with audit evidence.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q596. What corrections to controlled documents require a new version?

**Reconciled Answer:** Any substantive correction to an approved controlled document shall require a new DocumentVersion.

A new version is required where the change affects the document's:
- technical meaning;
- instructions or requirements;
- applicability;
- approval status;
- effective content;
- QMS/compliance meaning;
- report/configuration behavior;
- historical interpretation.

The previous approved version shall remain immutable and historically available.
Only genuinely non-substantive administrative corrections that do not alter meaning or controlled content may be handled as controlled metadata corrections with audit evidence.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q597. What document metadata is mandatory?

**Reconciled Answer:** Mandatory document metadata shall include, as applicable:
- Document ID;
- document type;
- title/name;
- version;
- status;
- owner/responsible authority;
- creation date/time;
- version date;
- effective date where applicable;
- review/expiry date where applicable;
- approval status and approval reference;
- source/origin where applicable;
- original filename where applicable;
- storage/content reference;
- content hash;
- confidentiality/access classification where required.

DocumentVersion shall remain distinguishable from the logical Document identity.
The exact required metadata shall be finalized by document type in the DocumentLink Entity / Relationship Matrix.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q598. What document link types are required?

**Reconciled Answer:** DocumentLink shall use a controlled, typed set of relationship types rather than unrestricted free-text or arbitrary relationships.

The v1 relationship model shall support relationships such as:
- source/supporting document;
- evidence for;
- applicable to;
- attached to;
- generated from;
- supersedes;
- superseded by;
- approved by/supporting approval;
- report attachment/component;
- controlled reference.

The exact closed set shall be defined in the DocumentLink Entity / Relationship Matrix.
Invalid or undefined relationship types shall be rejected by the backend.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q599. Which entities may legally have attached documents?

**Reconciled Answer:** Only approved laboratory entities shall be permitted to have Document/Attachment relationships.

The v1 model should support document relationships to entities such as:
- Customer;
- Project/Contract;
- Request;
- Sample;
- TestInstance;
- Result/ResultRevision where technically appropriate;
- Equipment;
- QC record;
- Report/ReportRevision;
- Method/MethodVersion;
- TestDefinition;
- configuration/change records;
- migration/recovery evidence records;
- other explicitly approved controlled entities.

The relationship must be typed and must comply with the allowed entity/link matrix.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q600. What is the closed set of allowed polymorphic DocumentLink entity types?

**Reconciled Answer:** The polymorphic DocumentLink target shall use a **closed, explicitly controlled entity-type set**.

For v1, the permitted target types shall be limited to the approved business and control entities defined in the DocumentLink Entity / Relationship Matrix, at minimum covering:
- Customer;
- Project/Contract;
- Request;
- Sample;
- TestInstance;
- Result/ResultRevision where approved;
- Method/MethodVersion;
- TestDefinition;
- Equipment;
- QC records;
- Report/ReportRevision;
- configuration/change records;
- migration/recovery evidence.

New polymorphic target types shall not be added implicitly through development. Any addition requires controlled schema/governance approval.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q601. Can users delete attachments?

**Reconciled Answer:** Users shall not directly delete controlled attachments or documents after they become part of the controlled record.

Where a file is erroneously uploaded:
- the original upload remains auditable;
- the file may be marked invalid/void/unusable through a controlled process;
- a replacement file, where required, is uploaded as a new controlled object/version;
- the reason, actor, timestamp, and disposition are retained.

Physical deletion may occur only where separately authorized by the applicable retention/disposition rule and shall never be used to rewrite required historical evidence.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q602. If deletion is not allowed, how are erroneous uploads handled?

**Reconciled Answer:** Erroneous uploads shall be handled through controlled invalidation/voiding rather than silent deletion.
The system shall retain the original upload's identity, metadata, hash, uploader, timestamp, reason, and disposition.
A corrected document shall be stored as a new upload or DocumentVersion as appropriate.
The invalid upload shall no longer be used as the effective document, but its historical existence shall remain traceable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q603. What happens when the underlying file is missing or corrupted?

**Reconciled Answer:** If an underlying file is missing, unreadable, or fails integrity verification:
1. the Document/Attachment shall be marked as integrity-failed or unavailable;
2. the stored hash and expected artifact identity shall be retained;
3. the event shall be audited;
4. affected records shall be identified where the file is operationally or historically significant;
5. restoration from a validated backup shall be attempted through the controlled recovery procedure;
6. the restored file shall be rehashed and independently verified;
7. unresolved loss shall be escalated as a documented recovery/nonconformance event.

The system shall never silently substitute an unverified file for the original artifact.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q604. Must storage integrity be periodically verified?

**Reconciled Answer:** Periodic document-storage integrity verification is required in principle, but the exact routine frequency remains a closure decision. Pre-restore and post-restore verification, plus post-deployment integrity verification, must also be defined.
**Revision 0.8 Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** DocumentLink Entity / Relationship Matrix + Document Storage Integrity Control

### Q605. What events must always create audit records?

**Reconciled Answer:** All controlled state changes, security events, workflow decisions, report/document issuance, configuration changes and significant operational failures always create audit events.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q606. Which read events, if any, must be audited?

**Reconciled Answer:** Read/access events shall be audited for categories where access itself is security-, confidentiality-, integrity-, or disclosure-significant.

At minimum, the system shall audit:
- download of controlled/sensitive documents;
- report/PDF download;
- audit-record access/export;
- controlled-document access where confidentiality requires it;
- bulk export;
- sensitive record export;
- other designated privileged/read operations.

Ordinary routine page viewing need not be individually audited where it does not provide meaningful security or confidentiality control.

The exact audited-read categories shall be defined in the Security Baseline and shall be consistently enforced.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q607. Which authentication events must be audited?

**Reconciled Answer:** Log login success/failure, logout, session creation/expiry/revocation, password changes/resets, account lockout and other authentication/security events.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q608. Which authorization failures must be audited?

**Reconciled Answer:** Authorization failures must always be audited.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q609. Which sample events must be audited?

**Reconciled Answer:** Audit receipt, registration, identification, acceptance/rejection, conditional acceptance, allocation, movement, storage, disposal, identity correction and sample status changes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q610. Which TestInstance events must be audited?

**Reconciled Answer:** Audit TestInstance creation, assignment, reassignment, start/stop, hold, rework, retest, cancellation, reopening and state transitions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q611. Which result events must be audited?

**Reconciled Answer:** Audit result creation, submission, revision, correction, reopen and status changes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q612. Which calculation events must be audited?

**Reconciled Answer:** Audit CalculationRun creation/execution/failure and exact FormulaVersion/engine version references.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q613. Which review/verification/approval events must be audited?

**Reconciled Answer:** Audit every Review/Verification/Approval attempt, success/failure/revocation/reopen.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q614. Which report events must be audited?

**Reconciled Answer:** Audit report generation, revision creation, issue, amendment, reissue, withdrawal, void, failed generation and delivery events.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q615. Which configuration events must be audited?

**Reconciled Answer:** Audit controlled configuration proposal, approval, rejection, implementation, activation, retirement and emergency change events.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q616. Which accreditation changes must be audited?

**Reconciled Answer:** Audit every accreditation-scope proposal/change/approval/effective-date change/reversal.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q617. Which user/role changes must be audited?

**Reconciled Answer:** Audit user creation, disabling, reactivation, password/security changes, role assignment/removal and authorization changes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q618. Which document events must be audited?

**Reconciled Answer:** Audit document upload, approval, activation, retirement, supersession, voiding, link/unlink, download of sensitive controlled documents and integrity failures.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q619. Which backup/restore events must be audited?

**Reconciled Answer:** Audit backup creation, validation, failure, restore, recovery test, migration and recovery verification.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q620. What actor information is required in each audit event?

**Reconciled Answer:** Each audit event requires event ID, timestamp, actor/system, event type, target entity/record, outcome and relevant before/after/change context.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q621. Is user ID sufficient, or must role/session/device information also be stored?

**Reconciled Answer:** User ID alone is insufficient for high-risk events. Store actor ID, effective role/authorization context, session ID, source host/IP where available, authentication context, and system/service identity where applicable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q622. What timestamp standard will be used?

**Reconciled Answer:** Use UTC as the internal canonical timestamp.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q623. Is UTC required internally?

**Reconciled Answer:** Yes. UTC should be stored internally.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q624. What timezone should be displayed to users?

**Reconciled Answer:** User-facing time uses the deployment's configured laboratory timezone; this should not be hard-coded to India in the reusable product.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q625. How are old audit records retained?

**Reconciled Answer:** Audit records follow the laboratory's configured retention policy; your current baseline is 10 years active retention followed by controlled archival.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q626. Can audit events ever be archived separately?

**Reconciled Answer:** Yes. Audit records may be archived separately, provided linkage, integrity, retrievability and retention remain intact.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q627. Can an audit record ever be corrected?

**Reconciled Answer:** No direct correction. An existing audit event is immutable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q628. If an audit record is wrong, how is the correction represented without rewriting history?

**Reconciled Answer:** A correction is represented by a new compensating/correction event referring to the original event; original audit content remains unchanged.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q629. Who can view audit records?

**Reconciled Answer:** Only authorized roles should view audit records.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q630. Are audit records visible to all administrators or only selected roles?

**Reconciled Answer:** Not every administrator automatically gets unrestricted audit access. Audit access should be a specific privileged permission.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q631. Are audit searches/filtering required?

**Reconciled Answer:** Yes. Audit search/filtering is required.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q632. Must audit records be exportable?

**Reconciled Answer:** Yes. Authorized users may export audit records in a controlled format.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q633. Are audit exports themselves audited?

**Reconciled Answer:** Yes. Audit exports must themselves generate audit events.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q634. What database trigger protections are required exactly?

**Reconciled Answer:** Append-only controlled event tables require DB-level UPDATE/DELETE protection using SQLite triggers that abort unauthorized changes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q635. Which tables are append-only?

**Reconciled Answer:** At minimum: audit_event, approval_chain_event, result_revision, report_result_snapshot, calculation_run, and other historical event/snapshot tables designated append-only by the schema contract.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q636. Which tables require database-level protection against UPDATE/DELETE?

**Reconciled Answer:** All append-only historical/event/snapshot tables require database-level protection against UPDATE/DELETE; current-state tables use appropriate controls according to their lifecycle.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q637. What is the approved behavior if trigger protection conflicts with a migration?

**Reconciled Answer:** Migrations that affect protected tables must use an explicitly designed/tested migration path that preserves all data and recreates protections. No ad-hoc trigger disabling in ordinary operation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q638. How is audit atomicity tested?

**Reconciled Answer:** Test transaction atomicity using failure injection, rollback tests, concurrency tests, audit/business-write consistency checks and database-integrity checks.

---

# 22. Authentication and Account Security

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q639. What are the exact user account fields?

**Reconciled Answer:** User account contains: immutable internal User ID, unique username, legal/display name, staff/employee ID where applicable, email/phone if supplied, status, password/authenticator metadata, creation/activation/deactivation data, and security/session metadata. Roles are assigned through separate role-assignment records.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q640. Is a unique username required?

**Reconciled Answer:** Yes. Username must be globally unique within the deployment.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q641. Is email required?

**Reconciled Answer:** No. Email is optional unless a deployment-specific workflow requires it. Core authentication cannot depend on email because the system is offline-first.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q642. Is phone number required?

**Reconciled Answer:** No. Phone is optional.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q643. Is employee/staff ID required?

**Reconciled Answer:** Yes for laboratory staff where an official employee/staff ID exists. It is an identity/provenance attribute, not the login credential.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q644. How are disabled users represented?

**Reconciled Answer:** Separate ACTIVE, PENDING, DISABLED, SUSPENDED/LOCKED status concepts. Temporary lockout must not be confused with deliberate account disabling.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q645. What password policy is required?

**Reconciled Answer:** The v1 password/security baseline is: minimum password length **12 characters**; Argon2id password hashing; secure server-side sessions; no Internet-dependent password validation; an offline locally controlled password-blocklist mechanism where implemented; password history of **5 previous passwords**; **5 failed attempts** trigger a **15-minute** temporary lockout; idle session timeout **30 minutes**; absolute session lifetime **12 hours**; high-risk approval/signing requires fresh password re-entry; MFA/second factor is not required for v1.

**Revision 0.8 Status:** CLOSED — APPROVED SECURITY BASELINE
**Primary Closure Artifact / Decision Record:** Security Baseline

### Q646. What is the minimum password length?

**Reconciled Answer:** 15 characters minimum for the normal single-factor password architecture. Allow at least 64 characters.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q647. Are password complexity rules required?

**Reconciled Answer:** No mandatory uppercase/lowercase/number/symbol mixture. Use length + blocklist/compromised-password checks instead.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q648. How long is password history retained?

**Reconciled Answer:** Password history shall retain the **5 most recent previous passwords**. A password shall not be changed to any of those retained values. The history is enforced server-side and shall never be exposed to ordinary users.

**Revision 0.8 Status:** CLOSED — APPROVED SECURITY BASELINE
**Primary Closure Artifact / Decision Record:** Security Baseline

### Q649. How often must passwords be changed, if at all?

**Reconciled Answer:** No periodic password expiry. Force change when compromised, explicitly reset, or otherwise required by security incident.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q650. Are forced password changes required after administrative reset?

**Reconciled Answer:** Yes. Administrative password reset must force a new password at next authentication.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q651. Who can reset passwords?

**Reconciled Answer:** Authorized System Administrator/User Access Administrator may initiate reset after identity verification. The reset itself is audited.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q652. Does a password reset invalidate existing sessions?

**Reconciled Answer:** Yes. Password reset invalidates all existing sessions for the user.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q653. How are failed login attempts handled?

**Reconciled Answer:** Failed logins are rate-limited, recorded, and subject to progressive delay/temporary lockout.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q654. Is account lockout required?

**Reconciled Answer:** Yes, temporary account lockout/protection is required, combined with throttling so attackers cannot trivially lock out users indefinitely.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q655. If lockout is required, what threshold and duration apply?

**Reconciled Answer:** After **5 failed authentication attempts**, the account is temporarily locked for **15 minutes**. The lockout condition and reset/expiry events shall be auditable. Administrative reset is permitted only to an authorized system administrator/authority through the controlled account-management path.

**Revision 0.8 Status:** CLOSED — APPROVED SECURITY BASELINE
**Primary Closure Artifact / Decision Record:** Security Baseline

### Q656. Is IP-based throttling required?

**Reconciled Answer:** Yes. Apply IP/source-based throttling in addition to per-account throttling.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q657. Is session timeout fixed or configurable?

**Reconciled Answer:** Session timeout should be deployment-configurable within platform-defined safe bounds.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q658. What is the idle timeout?

**Reconciled Answer:** The normal authenticated session shall expire after **30 minutes of inactivity**. High-risk approval/signing requires fresh password re-entry regardless of the remaining ordinary session lifetime.

**Revision 0.8 Status:** CLOSED — APPROVED SECURITY BASELINE
**Primary Closure Artifact / Decision Record:** Security Baseline

### Q659. What is the absolute session lifetime?

**Reconciled Answer:** The absolute session lifetime is **12 hours**. Re-authentication is required after expiry. High-risk approval/signing additionally requires fresh password re-entry before the action is accepted.

**Revision 0.8 Status:** CLOSED — APPROVED SECURITY BASELINE
**Primary Closure Artifact / Decision Record:** Security Baseline

### Q660. What happens when a user logs out?

**Reconciled Answer:** Logout immediately invalidates the server-side session and clears the browser authentication state.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q661. How are all sessions revoked for a user?

**Reconciled Answer:** Server-side session revocation by user/session/all-session scope; revoke all sessions is required.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q662. Must administrators be able to terminate sessions?

**Reconciled Answer:** Yes. Authorized administrators can terminate selected or all sessions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q663. What cookie security flags are mandatory?

**Reconciled Answer:** Session cookie: Secure, HttpOnly, SameSite=Strict, Path=/, preferably __Host- prefix, no sensitive data in cookie. OWASP recommends these protections.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q664. What CSRF protection approach is approved?

**Reconciled Answer:** Use server-side synchronizer CSRF tokens tied to the authenticated session, plus Origin/Referer validation as defense in depth.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q665. Is HTTPS mandatory even on the LAN?

**Reconciled Answer:** Yes. HTTPS is mandatory even on the LAN. OWASP explicitly recommends TLS for the entire authenticated session.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q666. How will certificates be managed offline?

**Reconciled Answer:** Use an offline local/private CA. For the small deployment, Caddy's internal CA is a practical baseline; install/trust the CA certificate on authorized workstations. Manage renewal without Internet dependency.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q667. Is HTTP allowed only during initial setup or never?

**Reconciled Answer:** No HTTP over the LAN. Production application access is HTTPS-only. A loopback-only bootstrap/maintenance endpoint may exist if technically necessary, but must not be exposed to LAN clients.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q668. Are local host-only administrative endpoints required?

**Reconciled Answer:** Yes. Host-only operational endpoints may exist for health, controlled maintenance, migration/recovery and bootstrap, but they are not authorization bypasses and should not expose normal laboratory data operations.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q669. Is concurrent login from multiple workstations allowed?

**Reconciled Answer:** Concurrent sessions from multiple workstations are **permitted for an individual named user**, subject to the approved account/session policy. Shared user accounts remain prohibited. Each session remains independently attributable, and high-risk actions require fresh authentication.

**Revision 0.8 Status:** CLOSED — APPROVED SECURITY BASELINE
**Primary Closure Artifact / Decision Record:** Security Baseline

### Q670. Is concurrent login from multiple browsers allowed?

**Reconciled Answer:** Concurrent sessions from multiple browsers are **permitted for an individual named user**, subject to the approved account/session policy. Shared accounts are prohibited. Session identifiers are independent and high-risk actions require fresh password re-entry.

**Revision 0.8 Status:** CLOSED — APPROVED SECURITY BASELINE
**Primary Closure Artifact / Decision Record:** Security Baseline

### Q671. Are shared user accounts prohibited?

**Reconciled Answer:** Yes. Shared user accounts are prohibited.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q672. How is user identity verified before account creation?

**Reconciled Answer:** Account creation requires identity verification by an authorized person using the laboratory's staff identity/onboarding evidence.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q673. What happens to audit history when a user is disabled or renamed?

**Reconciled Answer:** Audit history remains associated with the immutable internal User ID. Disabling a user never removes or rewrites historical actor references.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q674. Can usernames be changed?

**Reconciled Answer:** Username changes may be permitted as a controlled administrative operation, but the immutable internal User ID never changes and the old username is retained in history.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q675. What happens if a user leaves the laboratory?

**Reconciled Answer:** Disable the account immediately; revoke all sessions; remove future access; retain all historical records/audit attribution under the original User ID.

---

# 23. RBAC and Permission Model

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q676. What roles are needed at launch?

**Reconciled Answer:** The launch role model shall use a controlled set of roles whose permissions are defined separately from competence and SoD.

The v1 role set should support, as applicable:
- Project Owner / Laboratory Business Owner;
- Laboratory Quality Authority;
- Laboratory Technical Authority;
- LIMS System Administrator;
- User Access Administrator;
- Sample Receiving/Registration;
- Laboratory Coordinator;
- Analyst;
- Technical Reviewer;
- Technical Verifier;
- Authorized Approver/Authorized Signatory;
- Configuration Approver;
- Backup/Operations authority where required.

Roles may be combined for a small laboratory where operationally necessary, but the underlying permissions, competence requirements, and same-TestInstance SoD restrictions remain independently enforced.
Role possession itself is not an SoD violation; the actual attempted action is evaluated against permission, competence, workflow state, scope, and TestInstance history.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q677. What permissions are needed at launch?

**Reconciled Answer:** Launch permissions shall cover at minimum:
- authentication/session management;
- user/account administration;
- role assignment;
- customer/project/request management;
- sample receipt/registration/identity control;
- sample allocation/storage/disposition;
- TestRequest/TestInstance creation and assignment;
- execution/observation entry;
- calculation execution;
- result creation/correction;
- Review;
- Verification;
- Approval;
- TestInstance reopen/rework/retest/cancellation;
- report creation/revision/issuance/reissue/withdrawal;
- document upload/approval/retirement;
- equipment management/use;
- QC management;
- configuration proposal/approval/activation;
- audit viewing/export;
- backup/restore operations;
- controlled migration;
- system administration.

Permissions shall be action-oriented and context-aware rather than being simple unrestricted table CRUD permissions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q678. What is the smallest meaningful permission unit?

**Reconciled Answer:** The smallest meaningful permission unit shall be a controlled **action on a defined resource within an applicable context**.

The permission model shall therefore be able to distinguish, for example:
Result.Edit ≠ Result.Submit ≠ Result.Correct ≠ Result.Approve
and shall additionally evaluate context such as:
- TestInstance;
- workflow state;
- role;
- competence;
- discipline/TestDefinition;
- effective authorization;
- SoD;
- other applicable scope.

Pure table-level CRUD shall not be treated as the authoritative permission model.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q679. Are permissions action-based, entity-based, workflow-based, or a combination?

**Reconciled Answer:** Permissions shall use a combination of:
- action-based permissions;
- resource/entity scope;
- workflow/state conditions;
- competence/authorization;
- TestInstance-specific SoD;
- effective-dated role assignments;
- other controlled contextual restrictions where necessary.

RBAC provides the base authorization model, while backend/domain rules determine whether the requested action is actually permitted in the current context.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q680. Are permissions separated for create/read/update/delete/approve/issue/export actions?

**Reconciled Answer:** Yes. Permissions shall distinguish materially different actions such as:
- create;
- view/read;
- edit/update;
- cancel;
- submit;
- assign;
- review;
- verify;
- approve;
- correct;
- reopen;
- issue/reissue;
- withdraw;
- export;
- manage configuration.

Delete shall not be assumed merely because a CRUD-style permission model contains a "delete" operation.
For controlled records, deletion is generally prohibited or replaced by controlled lifecycle/disposition actions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q681. Are view permissions different from action permissions?

**Reconciled Answer:** Yes. View/read permissions shall be distinct from action permissions.
A user may have permission to view a record without having permission to modify, approve, issue, export, correct, or otherwise act upon it.
Sensitive document/report/audit access may have additional read/export restrictions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q682. Who can manage roles?

**Reconciled Answer:** Role creation, modification, retirement, and permission assignment shall be restricted to authorized system/user-access administrators under controlled governance.
Changing role definitions shall be treated as a controlled authorization change and shall require appropriate approval.
Ordinary laboratory users shall not manage role definitions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q683. Who can assign roles to users?

**Reconciled Answer:** Role assignment shall be executed by an authorized System/User Access Administrator only after approval by the designated User Access Approver.

The assignment shall record:
- user;
- role;
- applicable scope;
- effective date/time;
- approver;
- executor;
- reason where applicable;
- audit evidence.

The person executing the assignment shall not approve their own controlled role assignment.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q684. Can a user have multiple roles?

**Reconciled Answer:** Yes. A user may hold multiple roles.
Having multiple roles is not by itself an SoD violation.

The system shall evaluate the actual action against:
- the user's effective permissions;
- competence/authorization;
- workflow state;
- TestInstance history;
- hard SoD rules;
- policy-controlled SoD rules.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q685. If multiple roles grant permissions, are permissions additive?

**Reconciled Answer:** Yes. Where multiple valid roles apply, their permissions are generally additive.

However, additive permission does not override:
- workflow restrictions;
- competence requirements;
- effective dates;
- TestInstance-level SoD;
- hard authorization blocks;
- other domain rules.

A role cannot grant an action that the domain state or hard SoD rules prohibit.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q686. Can a role deny a permission granted by another role?

**Reconciled Answer:** No general role-level explicit-deny mechanism is required for v1.

The authoritative model should use:
**default deny + explicit grant + domain/SoD enforcement.**

Where two roles provide overlapping permissions, the effective permission is additive unless a higher-priority domain rule prevents the action.
Hard prohibitions shall be enforced independently of role grants and cannot be overridden by adding another role.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q687. Is explicit deny required?

**Reconciled Answer:** No separate general-purpose explicit-deny permission layer is required for v1.
An action is permitted only when an applicable permission exists and all contextual/domain conditions are satisfied.
Hard-blocked actions shall remain blocked regardless of the user's other roles or permissions.
This keeps authorization deterministic and avoids contradictory grant/deny combinations.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q688. Are permissions scoped by discipline, site, or TestInstance?

**Reconciled Answer:** Yes. Permissions shall support controlled contextual scope.

For v1 this may include:
- discipline/TestDefinition scope;
- workflow action;
- TestInstance;
- equipment or document type where applicable;
- administrative scope;
- effective role assignment.

V1 has exactly one physical laboratory/site, so a multi-site permission model is not required.
TestInstance-specific SoD shall be evaluated independently for each TestInstance.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q689. Are permissions time-limited?

**Reconciled Answer:** Yes. Role/authorization assignments shall be capable of being effective-dated.

The system shall support:
- effective-from;
- effective-to where applicable;
- current status;
- historical assignment;
- future assignment where approved.

The authorization applicable at the time of an action shall remain historically reconstructable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q690. Are temporary role assignments required?

**Reconciled Answer:** Yes. Temporary role assignments shall be supported where operationally required.

Temporary assignments shall have:
- defined scope;
- effective start;
- effective end;
- approving authority;
- reason where applicable;
- audit history.

They shall automatically cease to grant authority after their effective period expires.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q691. Are role assignments effective-dated?

**Reconciled Answer:** Yes. Role assignments shall be effective-dated.
A role assignment shall have a defined period of validity, allowing the system to determine which authorization was effective at a particular date/time.
Historical actions shall be attributable to the authorization state that applied when the action occurred.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q692. Can a role assignment overlap another assignment?

**Reconciled Answer:** Role assignments may overlap where they represent different valid roles or scopes.
However, the same user shall not have overlapping assignments for the **same role and same scope** unless the overlap is explicitly meaningful and governed.
Conflicting or ambiguous overlapping assignments shall be rejected or require controlled resolution before becoming effective.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q693. What is the rule for conflicting role assignments?

**Reconciled Answer:** Conflicting role assignments shall be resolved by the Authorization Matrix and role-assignment governance rather than by arbitrary permission precedence.

Where assignments create an impermissible authorization or SoD combination:
- the conflicting assignment shall not become effective;
- the system shall identify the conflict;
- the assigning/approving authority shall resolve it through role/scope changes or approved policy;
- hard SoD restrictions shall remain absolute.

Permissible multiple-role combinations shall remain allowed where they do not create a prohibited action.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q694. Are inactive users automatically denied all actions?

**Reconciled Answer:** Yes. Inactive, disabled, or suspended users shall be denied normal application actions.
The denial shall apply regardless of previously assigned roles.
Any host/system recovery functions are outside ordinary laboratory-user authorization and shall remain separately controlled.
Historical records and audit attribution associated with the user shall remain intact.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q695. Does deactivation terminate existing sessions immediately?

**Reconciled Answer:** Yes. User deactivation shall immediately terminate the user's active application sessions and prevent creation/use of new sessions.
Any existing session shall be invalidated server-side rather than being allowed to continue until its ordinary timeout.
The deactivation event and resulting session revocation shall be audited.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q696. Are special permissions needed for emergency configuration changes?

**Reconciled Answer:** Yes. Emergency configuration changes shall require a specific controlled permission that is distinct from ordinary configuration administration.

The permission shall not by itself bypass:
- proposal/authorization requirements;
- hard SoD blocks;
- evidence/countersigning;
- post-change verification;
- retrospective review.

Emergency configuration authority shall be granted only to designated competent users.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q697. Are special permissions needed for report reissue?

**Reconciled Answer:** Yes. Report reissue shall require a distinct controlled permission.

Reissue shall be subject to:
- affected-report identification;
- authorized reason/process;
- required technical/quality approval;
- correct ReportRevision creation;
- exact snapshot preservation;
- PDF integrity/issuance controls;
- applicable SoD.

Possession of ordinary report-view or report-generation permission shall not imply reissue authority.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q698. Are special permissions needed for result correction?

**Reconciled Answer:** Yes. Result correction shall require a distinct controlled permission and correction workflow.

Correction authority shall be evaluated together with:
- correction reason;
- current TestInstance/Result state;
- required authorization;
- SoD;
- Review/Verification/Approval consequences;
- Report impact;
- ResultRevision requirements.

Ordinary result-edit permission shall not allow correction of an already approved result.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q699. Are special permissions needed for reopening?

**Reconciled Answer:** Yes. Reopening shall require a distinct controlled permission.
Reopen authority shall be limited to designated competent Technical/Quality authority according to the approved workflow and SoD policy.
A Reopen permission shall not itself permit direct editing of approved records; the resulting work must follow the controlled Reopen → Correction/Rework → Review/Verification/Approval path as applicable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q700. Are special permissions needed for backup/restore operations?

**Reconciled Answer:** Yes. Backup/restore operations shall require privileged operational permissions separate from laboratory technical permissions.

Backup and restore authority shall be limited to designated Technical/Operations/System Administration personnel and shall include:
- backup creation;
- backup validation;
- restore execution;
- recovery testing;
- recovery verification.

Restore operations shall not provide a hidden mechanism for bypassing application authorization or controlled audit requirements.
All backup/restore activity shall be audited.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q701. Are administrator permissions intentionally separated from laboratory technical permissions?

**Reconciled Answer:** Yes. System/administrative permissions shall be intentionally separated from laboratory technical permissions.
System administrators manage the application infrastructure, accounts, configuration implementation, deployment, backup/recovery, and related operational functions according to their authority.
Laboratory technical roles perform and approve laboratory work.
Administrative privileges shall not automatically grant technical Review, Verification, Approval, result correction, or other laboratory decision-making authority.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q702. Must system administrators be prevented from approving technical laboratory results?

**Reconciled Answer:** Yes. System administrators shall be prevented from approving technical laboratory results unless they separately hold an explicitly authorized laboratory role and meet all competence and SoD requirements.
Administrator status alone shall never grant result Approval authority.
The backend shall enforce this independently of UI role visibility.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q703. Must database/server administrators be prevented from changing records through the application?

**Reconciled Answer:** Yes. Database/server administrators shall not be able to modify laboratory records **through the LabNexus application** merely because they possess infrastructure privileges.
The application shall authorize all normal record changes through the domain/application layer.
Direct filesystem/database access is outside the LIMS application authorization boundary and shall instead be controlled by the Windows/host security boundary, operational procedures, and restricted administrative access.
The system shall not claim that application authorization prevents a person who has unrestricted operating-system/database access from directly manipulating the underlying SQLite file.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q704. How is privilege escalation prevented and tested?

**Reconciled Answer:** Privilege escalation shall be prevented through:
- default-deny authorization;
- explicit action permissions;
- backend/domain enforcement;
- separation of administrative and laboratory permissions;
- effective-dated role assignments;
- hard SoD rules;
- controlled privileged actions;
- protection against client-side permission manipulation;
- server-side authorization checks on every protected operation.

Verification shall include tests attempting unauthorized actions through:
- direct API calls;
- manipulated request parameters;
- altered client-side state;
- role combinations;
- expired/disabled assignments;
- cross-TestInstance actions;
- administrative-role abuse;
- concurrent/session scenarios.

A passing UI-level test alone is insufficient evidence of authorization control.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q705. What is the authoritative list of hard-blocked same-TestInstance combinations?

**Reconciled Answer:** The authoritative hard-blocked same-TestInstance SoD matrix shall include, at minimum:
**- Analyst → Review: BLOCK**
**- Analyst → Verification: BLOCK**
**- Analyst → Approval: BLOCK**
**- Reviewer → Technical Verification: BLOCK**

These blocks apply regardless of emergency status, alternate-approver mechanisms, or additional roles.
Additional hard blocks may be defined by the approved SoD Matrix, but shall not be inferred during implementation.
The restriction is evaluated per TestInstance; the same user may perform otherwise permitted actions on different TestInstances.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q706. What is the authoritative list of policy-controlled combinations?

**Reconciled Answer:** Policy-controlled combinations shall be explicitly listed in the effective-dated SoD Matrix rather than inferred from general role permissions.
At minimum, **Technical Reviewer → Approval on the same TestInstance** shall be policy-controlled, with BLOCK as the default unless an approved rule explicitly permits the combination.
Other combinations involving Reopen, Correction Approval, Report Reissue, Configuration Approval, or emergency/exception actions shall likewise be explicitly classified as:
- permitted;
- blocked; or
- permitted only under defined conditions/exception.

No action shall be considered policy-controlled merely because the UI exposes it.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q707. What exactly does “policy-controlled” mean operationally?

**Reconciled Answer:** A **policy-controlled** action is an action whose legality depends on an explicit approved policy rule in addition to ordinary role permission.

The rule shall define:
- applicable role/action combination;
- applicable object/context;
- whether the action is normally allowed;
- required competence;
- required independent stage/person;
- permitted exceptions;
- evidence/countersignature requirements;
- effective period;
- applicable policy version.

A policy-controlled action is therefore not an informal administrator decision or a UI setting.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q708. Is a policy-controlled action allowed automatically, conditionally, or only with an explicit exception?

**Reconciled Answer:** A policy-controlled action shall not be treated as automatically permitted merely because the user possesses the relevant roles.

**- The SoD Matrix shall explicitly classify the combination as:**
**- normally allowed subject to stated conditions;**
**- conditionally allowed;**
**- exception-only; or**
**- blocked.**

For example, Technical Reviewer → Approval on the same TestInstance shall remain blocked unless an approved policy explicitly permits it.
Emergency handling may apply only where the policy-controlled combination explicitly permits an emergency exception.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q709. Where is the policy stored?

**Reconciled Answer:** The authoritative SoD policy shall be stored as controlled, versioned configuration within the LIMS governance model and represented by the SoD Matrix.

Each policy version shall have:
- unique identity/version;
- effective date/time;
- approval evidence;
- proposer/approver;
- controlled rules;
- status;
- supersession history.

The applicable policy version shall be reconstructable for historical Review, Verification, Approval, correction, reopen, report reissue, and configuration actions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q710. Who can change the policy?

**Reconciled Answer:** Changes to the SoD policy shall require controlled proposal and approval.

For v1:
- the **Laboratory Quality Authority + Project Owner** shall approve SoD policy changes;
- Technical Authority shall review implementability where necessary;
- proposer and approver shall not be the same person for controlled changes;
- the implementation shall be separately executed and verified;
- the effective date/time shall be explicit;
- the prior policy version shall remain historically preserved.

Emergency changes shall follow the approved emergency configuration governance and shall never bypass hard SoD blocks.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q711. Does policy change require proposal and approval?

**Reconciled Answer:** Yes. SoD policy changes shall require a formal proposal and approval process.

The proposal shall identify:
- current and proposed rule;
- reason for change;
- affected roles/actions;
- affected workflows;
- impact on existing work;
- effective date/time;
- implementation/verification requirements.

The approved change shall become effective only after the required authorization and verification steps are complete.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q712. When does a policy change become effective?

**Reconciled Answer:** A new SoD policy version shall become effective only after:
1. proposal;
2. review;
3. required approval;
4. implementation/activation readiness verification;
5. defined effective date/time.

The policy shall not become effective merely because the database record has been entered.
Actions occurring before and after the effective point shall be evaluated against the corresponding policy version.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q713. Is policy versioning required?

**Reconciled Answer:** Yes. SoD policy versioning is mandatory.

Each approved change shall create a distinct policy version with its own:
- identity;
- content;
- effective interval;
- approval evidence;
- implementation evidence.

Previous versions shall remain immutable and available for historical reconstruction.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q714. Must a historical approval reconstruct the SoD policy version in effect at that time?

**Reconciled Answer:** Yes. Historical approval/review/verification actions shall be reconstructable against the **SoD policy version that was effective when the action occurred**.

The relevant approval-chain event shall therefore identify or allow deterministic resolution of:
- policy version;
- effective date/time;
- actor;
- role/authorization context;
- TestInstance;
- action/stage;
- outcome.

Later SoD policy changes shall not retroactively rewrite the authorization basis of historical actions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q715. How are cross-TestInstance actions handled?

**Reconciled Answer:** SoD shall be evaluated **per TestInstance**.
An action performed on one TestInstance shall not automatically create an SoD conflict on another TestInstance.

For example, the same user may:
- perform Analysis on TestInstance A;
- perform Review on TestInstance B;
- perform Verification on TestInstance C;
where otherwise authorized.

The hard same-TestInstance restrictions remain applicable independently to each TestInstance.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q716. Can the same user review one TestInstance and analyze another?

**Reconciled Answer:** Yes. A user may review one TestInstance and analyze another.
The system shall evaluate authorization and SoD against the specific TestInstance on which the action is being performed.

The user shall still satisfy all applicable:
- role/permission requirements;
- competence requirements;
- workflow-state requirements;
- TestDefinition requirements;
- effective authorization;
- other SoD rules.

Same-user participation across different TestInstances shall not be treated as a global historical conflict unless an explicitly approved laboratory policy states otherwise.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q717. What happens when a user performs an action before an SoD policy change and another after the change?

**Reconciled Answer:** An SoD policy change shall apply according to its defined effective date/time.
Actions completed before the new policy becomes effective shall remain governed by the prior policy version. Actions performed after the effective point shall be evaluated against the new policy version.
Historical approval-chain events shall preserve or deterministically identify the applicable policy version so that later policy changes cannot rewrite historical authorization decisions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q718. Are emergency SoD exceptions allowed?

**Reconciled Answer:** Emergency SoD exceptions may be permitted only for **policy-controlled** combinations where the approved laboratory policy explicitly allows them.
Emergency handling shall never bypass absolute hard blocks, including the defined hard-blocked same-TestInstance Analyst/Reviewer combinations.
Any permitted emergency exception shall be bounded, visibly identified, authorized, independently countersigned where required, fully audited, and retrospectively reviewed.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q719. What evidence is required for an exception?

**Reconciled Answer:** An SoD exception shall preserve sufficient evidence to establish what exception occurred and why.

At minimum, the evidence shall identify:
- affected TestInstance;
- role/action combination;
- normal SoD rule;
- reason;
- actor;
- authorizer;
- countersigner where required;
- date/time;
- applicable SoD policy version;
- supporting evidence;
- resulting action/outcome;
- retrospective review where required.

Hard SoD blocks shall not be made valid merely by creating exception evidence.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q720. How is exception frequency monitored?

**Reconciled Answer:** Emergency SoD-exception frequency shall be monitored through an auditable operational report.

The report should identify, at minimum:
- period;
- exception count;
- TestInstance(s);
- user/role;
- action/SoD rule;
- reason;
- authorizer;
- applicable policy version;
- outcome.

Emergency frequency shall be reviewed at least monthly, with immediate review of significant/high-risk events.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q721. What constitutes excessive emergency use?

**Reconciled Answer:** Emergency use shall be considered excessive when it demonstrates repeated reliance on the emergency path rather than the approved normal configuration/change process.
As the operational default, **more than 2 emergency configuration/authorization uses in a calendar month**, or any repeated use of the same emergency mechanism for substantially the same underlying problem, shall trigger documented Quality/Technical review.
Any single high-risk emergency may also trigger immediate review regardless of frequency.
The threshold is a monitoring/escalation control and does not permit any emergency action that would violate a hard SoD restriction.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q722. Who reviews emergency-use reports?

**Reconciled Answer:** Emergency-use reports shall be reviewed by the **Laboratory Quality Authority together with the relevant Technical/Operations Authority**.
Where an emergency involved security or system-access controls, the responsible System/Security authority shall also participate.
The review shall assess frequency, reasons, repeated patterns, policy compliance, effectiveness of controls, and whether a recurring emergency indicates the need for a normal controlled change.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q723. Which configuration items are controlled?

**Reconciled Answer:** Controlled configuration includes methods, MethodVersions, TestDefinitions, parameters, formulas, constants, lookup tables, QC rules, equipment requirements/eligibility, accreditation scope, report templates/rules, workflows, numbering rules, rates, TAT rules, SoD policy, controlled document settings and other settings capable of affecting controlled laboratory operation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q724. Which configuration items are ordinary administrative settings?

**Reconciled Answer:** Ordinary administrative settings include non-controlled UI preferences, display preferences, user-specific dashboard settings and other settings that cannot alter controlled technical records, authorization, reports or compliance behavior.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q725. Which configuration items affect technical records?

**Reconciled Answer:** Any configuration capable of changing the meaning, validity, traceability or lifecycle of a technical record is controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q726. Which configuration items affect report output?

**Reconciled Answer:** Any configuration affecting report content, calculation, wording, layout, accreditation representation, revision behavior or issuance is controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q727. Which configuration items affect authorization?

**Reconciled Answer:** Any configuration affecting permissions, roles, authentication or SoD is controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q728. Which configuration items affect accreditation representation?

**Reconciled Answer:** Accreditation configuration is controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q729. Which configuration items affect QC?

**Reconciled Answer:** QC rules/limits/failure actions are controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q730. Which configuration items affect equipment enforcement?

**Reconciled Answer:** Equipment requirements and blocking/warning eligibility rules are controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q731. Which configuration items affect numbering?

**Reconciled Answer:** Business numbering rules are controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q732. Which configuration items affect workflows?

**Reconciled Answer:** Workflow states, transitions and transition authorization are controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q733. Which configuration items require proposal and approval?

**Reconciled Answer:** All configuration that can affect controlled laboratory behavior requires proposal and approval.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q734. Which configuration items may be changed immediately by an authorized administrator?

**Reconciled Answer:** Only genuinely non-controlled administrative settings may be changed immediately by an authorized administrator/user

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q735. What is the exact lifecycle of a configuration proposal?

**Reconciled Answer:** Recommended lifecycle: DRAFT → SUBMITTED → UNDER_REVIEW → APPROVED → VERIFIED/READY → EFFECTIVE → SUPERSEDED/RETIRED; alternative outcomes: REJECTED, CANCELLED.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q736. Can a proposal be edited after review starts?

**Reconciled Answer:** A proposal may be edited until review formally begins. Once review begins, the submitted content is frozen. Further changes create a new proposal/revision.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q737. Can a proposal be rejected and resubmitted?

**Reconciled Answer:** Yes. Rejected proposals may be resubmitted as a new proposal referencing the prior proposal/reason.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q738. Can proposals be cancelled?

**Reconciled Answer:** Yes. Proposals can be cancelled before becoming effective, with reason and audit.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q739. Who can approve a proposal?

**Reconciled Answer:** Configuration approver is determined by configuration type; authority is deployment-configured. Technical/Quality/Business authority varies by domain.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q740. Must proposer and approver be different users?

**Reconciled Answer:** Yes for controlled changes. Proposer and approver must be different users.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q741. What is the normal alternate-approver rule?

**Reconciled Answer:** Primary approver unavailable → pre-designated competent alternate approver; no ad-hoc substitution.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q742. What is the emergency configuration path?

**Reconciled Answer:** Emergency: declare → authorize alternate → implement bounded change → verify → countersign/evidence → retrospective review.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q743. What makes an emergency change valid?

**Reconciled Answer:** Emergency is valid only where immediate action is necessary to protect data integrity, security, report correctness, laboratory operation or recoverability and normal approval cannot safely be completed in time.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q744. What is the maximum emergency validity period?

**Reconciled Answer:** A temporary emergency configuration or exception shall have a maximum validity of **24 hours**, unless a separately approved higher-level continuity/recovery procedure explicitly establishes a different controlled period.
The emergency record shall contain its activation time and automatic expiry time.
Emergency validity shall never convert a prohibited hard SoD relationship into an allowed one.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q745. Does an emergency configuration automatically expire?

**Reconciled Answer:** Yes. Emergency configuration shall have an explicit expiry timestamp and shall **automatically cease to be effective at expiry** unless it has been replaced by an independently approved normal configuration.
The system shall not silently extend an emergency configuration.
Expiry shall generate an auditable event, and an expired emergency configuration shall not affect subsequent controlled actions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q746. What happens if it is not retrospectively reviewed?

**Reconciled Answer:** Failure to complete the required retrospective review shall create a controlled compliance/operations exception.
The emergency action shall remain historically recorded and shall not be erased or rewritten. The relevant Quality/Technical authority shall be notified/escalated, and subsequent use of the same emergency mechanism may be restricted until review is completed.
Retrospective review failure shall not invalidate previously legitimate business records automatically, but it shall remain an unresolved control deficiency requiring documented disposition.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q747. How are emergency changes countersigned?

**Reconciled Answer:** Countersigning is an explicit separate approval/acknowledgement event by the designated alternate/independent authority; it is not merely a comment.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q748. What evidence proves the emergency change was visible to the required people?

**Reconciled Answer:** System records named recipients, notification/event timestamp, acknowledgement/countersignature and policy/emergency ID.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q749. How are emergency-use frequencies reported?

**Reconciled Answer:** Automatic monthly emergency-use report, with trend indicators by user, rule, configuration type and reason.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q750. Can an unapproved configuration ever be testable without affecting live behavior?

**Reconciled Answer:** Yes. An unapproved configuration may be tested without affecting live behavior only in an explicitly isolated draft/test context.
The configuration shall not become effective merely because it exists in the system and shall not influence live controlled behavior until it has passed the required approval and activation process.
The Configuration History and Capture Matrix shall define the relationship between draft/test configuration, approved configuration, effective configuration, and historical configuration used by in-progress work.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q751. Is a staging/draft environment required inside the application for configuration review?

**Reconciled Answer:** A permanently separate staging environment inside the application is **not required for v1**.
The application shall nevertheless provide a controlled draft/review mechanism for configuration proposals where practical, so that unapproved configuration can be evaluated without affecting live behavior.
The approved production configuration shall remain isolated from draft/test configuration, and no unapproved configuration shall influence controlled laboratory operation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q752. How are approved configurations promoted to effective status?

**Reconciled Answer:** Approved configuration shall become effective only through a controlled promotion/activation process.

The process shall include:
**Draft → Review → Approval → Verification/Ready → Effective**
with the applicable effective date/time recorded.

Activation shall create an auditable configuration event and shall use the exact approved configuration version.
Unapproved or superseded configuration shall not become effective through ordinary editing or deployment-side manipulation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q753. Must configuration changes be effective-dated?

**Reconciled Answer:** Yes. Controlled configuration changes shall be effective-dated where their behavior or applicability can change over time.
Each version shall have a defined effective-from date/time and, where applicable, effective-to date/time.
The system shall prevent ambiguous overlapping effective configurations unless the approved configuration type explicitly permits scoped coexistence.
Historical work shall remain associated with the configuration applicable at the relevant point in time.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q754. How are historical configurations reconstructed for old TestInstances?

**Reconciled Answer:** Historical configuration for an old TestInstance shall be reconstructed using the configuration version applicable to the relevant date/time and any required explicit snapshot/reference captured by the TestInstance, Result, CalculationRun, or ReportRevision.
The system shall not rely solely on the current configuration.

The Configuration History and Capture Matrix shall define for each controlled configuration object whether historical reconstruction uses:
- effective-dated reference;
- immutable snapshot;
- or another explicitly approved capture mechanism.

The selected mechanism shall allow reconstruction even after later configuration versions become effective.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q755. For MethodVersion, what is the business key for temporal uniqueness?

**Reconciled Answer:** The MethodVersion business identity shall be:
**Method ID + controlled Version Designation**

For example, the stable Method may have version designations such as `2026.1`, `Rev-03`, or another approved laboratory convention.
Database uniqueness shall prevent two MethodVersions for the same Method from having the same version designation.
Temporal applicability is a separate concern from identity. Effective-from/effective-to information determines when a MethodVersion may be used; it does not redefine the MethodVersion's identity.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q756. Can two MethodVersions for the same Method be effective simultaneously?

**Reconciled Answer:** No. For a given Method and applicability context, **two MethodVersions shall not be effective simultaneously**.
The preferred temporal model uses non-overlapping validity intervals. A MethodVersion may end at the exact instant another begins.
Historical TestInstances remain linked to the MethodVersion actually used, so later replacement does not affect historical reconstruction.
If a genuine parallel technical regime is required for different matrices/disciplines or other applicability dimensions, those dimensions must be explicitly modeled rather than permitting ambiguous temporal overlap.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q757. For Rate, can overlapping rates exist for the same scope?

**Reconciled Answer:** Charge calculation is **deferred from v1**. Therefore no v1 overlapping-Rate rule is required. A future commercial implementation shall use controlled effective-dated rate versions and deterministic non-overlap rules for each approved business scope.

**Revision 0.8 Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record / Database Contract

### Q758. For CustomerRate, can overlapping customer rates exist?

**Reconciled Answer:** Customer-specific charging is **deferred from v1**. No v1 CustomerRate overlap rule is required. If charge calculation is later approved, customer-specific rates shall be effective-dated, versioned, and governed so that concurrent effective rates are deterministic for an identical commercial scope.

**Revision 0.8 Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record / Database Contract

### Q759. For UserRoleAssignment, can overlapping assignments exist?

**Reconciled Answer:** UserRoleAssignments may overlap when they represent different valid roles/assignments. The same role assignment for the same user and scope must not overlap.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q760. For AccreditationScope, can overlapping records exist?

**Reconciled Answer:** For a given AccreditationScope applicability target and effective context, overlapping active records shall **not be permitted** unless the data model explicitly distinguishes non-conflicting scopes.
The frozen accreditation model already requires deterministic temporal resolution.

Therefore, for the same:
* MethodVersion default scope target; or
* TestDefinition override target;
there shall be at most one applicable scope state at any instant.

Overlaps that represent genuinely different non-conflicting applicability dimensions must be modeled explicitly rather than resolved by arbitrary ordering.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q761. For each temporal entity, what defines the “current” record?

**Reconciled Answer:** For every effective-dated entity, the “current” record shall be the record whose validity interval contains the evaluation instant.

The platform-wide temporal convention shall be:
**`effective_from <= evaluation_time < effective_to`**
where `effective_to = NULL` means no defined end.

The current record therefore must be determined from stored effective timestamps and applicable scope, not merely from a mutable `is_current` flag.
A cached/current flag may be used for performance only if it is derived and protected against divergence from the authoritative temporal data.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q762. Can validity periods be open-ended?

**Reconciled Answer:** Yes. Open-ended validity periods shall be supported.
An open-ended record shall use `effective_to = NULL` to mean that the record remains effective until explicitly superseded/ended.
There shall be at most one open-ended effective record for the same unique business scope where the entity's temporal rules prohibit overlap.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q763. How is an end date/time represented?

**Reconciled Answer:** An end date/time shall be represented as an **instant in UTC**, with NULL meaning open-ended.
The temporal model shall use timestamps rather than ambiguous local date strings when the entity represents an exact effective moment.
For user-facing screens, the timestamp shall be displayed in the laboratory's configured timezone, while the stored authoritative value remains UTC.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q764. Can an effective period end exactly when another begins?

**Reconciled Answer:** Yes. One effective period may end exactly when another begins.
With the platform convention `[effective_from, effective_to)`, the first record is effective up to but not including its end instant, while the second becomes effective at that exact instant.

Example:
`Version A: 2026-01-01 00:00 → 2026-07-01 00:00`
`Version B: 2026-07-01 00:00 → open`

There is no overlap and no gap.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q765. Are boundary timestamps inclusive or exclusive?

**Reconciled Answer:** Temporal boundaries shall use a consistent **start-inclusive, end-exclusive** convention:
**`[effective_from, effective_to)`**

Therefore:
* `effective_from` is inclusive;
* `effective_to` is exclusive;
* Adjacent records may share the same boundary instant;
* Two records cannot both be effective at the boundary;
* NULL `effective_to` represents open-ended validity.

This convention shall be frozen in the Temporal Governance Matrix and applied consistently across all effective-dated entities unless a documented domain-specific exception is approved.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q766. How is time-zone handling defined for effective dates?

**Reconciled Answer:** Effective timestamps shall be stored internally in **UTC**.
The laboratory's normal user/report display timezone shall be **Asia/Kolkata**, using the IANA identifier `Asia/Kolkata`.
Temporal comparisons and database rules shall operate on the UTC instant, not on displayed local time.
Date-only business values shall remain date-only and must not be converted into artificial timestamps merely to fit the temporal model.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q767. Can a future record be entered in advance?

**Reconciled Answer:** Yes. Future-dated records shall be allowed when the entity's governance rules permit them.
A future record may be prepared, reviewed, approved, and stored before its effective time, but it must not influence live behavior before that effective timestamp.
For high-impact configuration, future activation shall require the complete approved configuration lifecycle and an exact effective timestamp.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q768. Can a past-dated record be inserted?

**Reconciled Answer:** Past-dated records may be inserted **only through a controlled retrospective process**.
They shall not be created by ordinary users simply by changing an effective date into the past.

A retrospective temporal insertion requires:
* Structured reason;
* Evidence;
* Authorized approval;
* Impact assessment;
* Conflict/overlap validation;
* Historical-effect analysis;
* Audit evidence;
* Independent verification where risk warrants it.

The original prior configuration/history must remain reconstructable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q769. Can a past-dated change be made after newer records already exist?

**Reconciled Answer:** Yes, a past-dated change may be made after newer records exist, but only through the same controlled retrospective-governance process.
The application shall recalculate the affected temporal intervals and identify impacted historical records, TestInstances, results, reports, permissions, or other dependent behavior.
The system must not silently rewrite history.
Where historical records were already finalized using the previous configuration, the retrospective change shall trigger an impact assessment and controlled corrective process rather than silently applying the new state retroactively.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q770. What approval is required for retrospective temporal changes?

**Reconciled Answer:** A retrospective temporal change shall require:
* Formal change/proposal record;
* Reason and supporting evidence;
* Technical assessment;
* Laboratory Quality/Technical approval appropriate to the affected entity;
* Impact assessment;
* Conflict/overlap validation;
* Independent verification for high-risk changes;
* Effective timestamp;
* Complete audit trail.

For configuration affecting accreditation, SoD, workflows, calculations, reporting, or other high-risk controlled behavior, the applicable specialized approval and verification controls shall also apply.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q771. How are historical reconstructions protected from later temporal edits?

**Reconciled Answer:** Historical reconstruction shall never depend solely on the current temporal configuration.

Protection shall use:
* Immutable versioned records;
* Effective-dated configuration;
* Exact configuration references where required;
* Frozen snapshots for report-visible/approval-critical information;
* Immutable audit/history;
* ResultRevision and CalculationRun provenance;
* ReportResultSnapshot and ApprovalSnapshot;
* Controlled retrospective-change records.

Where historical behavior cannot safely be derived from temporal references alone, the affected configuration identity/state shall be captured as an immutable snapshot.
Later configuration changes must therefore not alter the meaning of an already completed TestInstance or previously issued report.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q772. Which business identifiers need dedicated sequences?

**Reconciled Answer:** Dedicated system-controlled sequences shall be used for business identifiers whose identity must be stable, unique, human-operable, and independently traceable.

The v1 numbering matrix should cover at least:
* Sample ID;
* TestInstance ID;
* Report ID;
* Customer ID;
* Project/Contract ID where separately numbered;
* Request ID;
* Controlled Document ID where a human-facing document number is required.

Internal database primary keys shall remain independent from human/business identifiers.
Each identifier class shall have its own allocation rule; one global sequence shall not be reused merely because it is technically convenient.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q773. Is there a sample number sequence?

**Reconciled Answer:** Yes. Samples shall have a dedicated controlled Sample ID sequence.

Recommended baseline:
`SAM-00000001`

The exact prefix and width shall be frozen in the Numbering and Identifier Allocation Matrix.
Sample IDs shall be globally unique within the LabNexus deployment, never reused, and allocated through the authoritative sample-registration transaction.
A damaged label does not cause a new Sample ID to be issued; the same identifier may be reprinted after identity verification.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q774. Is there a TestInstance number sequence?

**Reconciled Answer:** Yes. TestInstances shall have a dedicated system-controlled TestInstance identifier/sequence.
A TestInstance represents a distinct execution occurrence and therefore needs an independently traceable identifier.
The identifier shall not be reused when a TestInstance is cancelled, rejected, failed, corrected, reworked, or otherwise terminated.
Repeat/retest/new-execution semantics remain separate from identifier allocation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q775. Is there a report number sequence?

**Reconciled Answer:** Yes. Reports shall have a dedicated report-number sequence.

The Report Number identifies the logical report and shall remain distinct from:
* ReportRevision number;
* ResultRevision;
* PDF artifact identity.

Recommended human format is along the lines of:
`RPT-00012345`
with the exact prefix/width governed by the Numbering Matrix.

A revised/reissued report normally retains the same logical Report Number and receives a new ReportRevision.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q776. Is there a customer/project/request number sequence?

**Reconciled Answer:** Yes, where a controlled business identifier is needed, Customer, Project/Contract, and Request shall have **separate identifier namespaces**.

For example:
* Customer: `CUS-...`
* Project/Contract: `PRJ-...`
* Request: `REQ-...`

The precise prefixes and whether every entity receives a human-facing number shall be frozen before implementation.
Internal primary keys remain independent from these business identifiers.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q777. Is there a document number sequence?

**Reconciled Answer:** A controlled Document entity should have a dedicated logical document identifier where the laboratory needs human-facing document control.

For example:
`DOC-00012345`

DocumentVersion shall not receive an unrelated independent business identity; the Document ID identifies the logical document and its version designation identifies the controlled version.
Where a document is merely an internal attachment and does not require controlled-document numbering, an internal immutable ID may be sufficient.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q778. Are sequences global or per discipline/site/year?

**Reconciled Answer:** For the v1 single-laboratory deployment, sequences shall be **global within the deployment**, not separately reset by discipline, room, or site.
Different entity types have separate namespaces.
The system shall not reset a sequence annually merely for presentation convenience.
Future independent laboratory deployments shall have their own independent sequences because they are independent LIMS deployments.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q779. Is year embedded in identifiers?

**Reconciled Answer:** Year should **not be embedded as a mandatory component of the core identifier**.
The identifier should remain stable across calendar years.
Year may be displayed separately or included in a controlled human-facing report/document format where there is a genuine reporting requirement, but changing the calendar year must not require restarting or changing the underlying sequence semantics.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q780. Is prefix embedded in identifiers?

**Reconciled Answer:** Yes. Controlled human-facing identifiers should use an **approved stable prefix** to make the entity type immediately recognizable.

Examples:
`SAM-00000001`
`TI-00000001`
`RPT-00000001`
`REQ-00000001`

Prefixes are presentation/identifier-format controls, not substitutes for actual database type identity or foreign-key relationships.
Prefixes shall be versioned through controlled numbering configuration and must not be changed casually after production records exist.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q781. Are sequence values zero-padded?

**Reconciled Answer:** Yes. Sequence values should use **fixed zero-padding** according to the approved numbering format.
The exact width shall be established in the Numbering Matrix based on realistic expected capacity and future growth.

For example, an eight-digit sequence provides a format such as:
`SAM-00000001`

Zero-padding is presentation formatting; it does not change numeric ordering or uniqueness.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q782. When is a number allocated: draft creation, registration, approval, or issue?

**Reconciled Answer:** Numbers shall be allocated at the **business event that establishes the authoritative identity of the entity**, not merely when a temporary browser draft exists.

Recommended triggers:
* Sample ID: authoritative sample registration;
* TestInstance ID: authoritative TestInstance creation;
* Report Number: creation of the logical Report entity;
* Customer/Project/Request ID: authoritative creation of that business entity;
* Document Number: creation of the controlled logical Document where numbering is required.

The allocation event shall occur inside the transaction that establishes the entity identity.
Human/business identifiers shall not be allocated to unsaved browser drafts.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q783. Are numbers allowed to be reserved and later abandoned?

**Reconciled Answer:** Numbers may be allocated and subsequently abandoned because of cancellation, transaction failure, system recovery, or other controlled circumstances.
**Gaps are acceptable.**
A number that has been allocated shall never later be silently reused for a different record.
The system does not need to guarantee gapless numbering unless a separately approved external requirement explicitly requires it.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q784. If a transaction rolls back after number allocation, is the gap acceptable?

**Reconciled Answer:** Yes. A sequence gap resulting from a transaction rollback or failed allocation is acceptable.

The sequence mechanism shall prioritize:
* Uniqueness;
* No reuse;
* Concurrency safety;
* Transactional correctness;
* Recoverability.

Attempting to guarantee gapless numbering through complicated rollback/reuse mechanisms would introduce avoidable integrity and concurrency risk.
Unexplained material gaps may nevertheless be available for controlled audit/reconciliation where the entity type requires such monitoring.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q785. Can issued numbers ever be reused?

**Reconciled Answer:** No. **Issued/allocated business identifiers shall never be reused.**

This applies even when a record is:
* Cancelled;
* Rejected;
* Withdrawn;
* Destroyed after retention;
* Created incorrectly;
* Superseded;
* Abandoned following a failed transaction after allocation.

The identifier remains part of historical traceability.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q786. Can a sequence be changed after production records exist?

**Reconciled Answer:** A numbering format or sequence configuration shall not be changed casually after production records exist.

A future controlled configuration change may alter presentation format or start a new sequence policy only after:
* Impact assessment;
* Approval;
* Effective date;
* Verification;
* Historical compatibility assessment;
* Preservation of the old numbering rule.

Existing identifiers shall never be renumbered.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q787. Who can configure numbering?

**Reconciled Answer:** Numbering configuration shall be managed by the **authorized configuration administration role**, but production activation shall require the approved configuration-governance process.
The person technically entering the configuration should not automatically be the sole authority approving the change.
Numbering configuration changes shall be auditable and versioned.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q788. Must numbering configuration be controlled and approved?

**Reconciled Answer:** Yes. Numbering configuration is controlled configuration and shall follow the same governance model:
**Propose → Review → Approve → Verify/Ready → Effective**

The exact format, prefix, width, allocation trigger, sequence behavior, and future effective date shall be preserved as configuration history.
Unapproved numbering configuration shall not affect live production identifiers.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q789. How is concurrency handled for multiple writers?

**Reconciled Answer:** Sequence allocation shall be concurrency-safe and transactional.

For the SQLite deployment, the application shall use:
* Short write transactions;
* Appropriate SQLite locking/WAL behavior;
* Busy timeout;
* Application-level retry/backoff where appropriate;
* Atomic sequence allocation;
* Uniqueness constraints;
* No client-side “read current max + 1” logic.

Two simultaneous writers must never receive the same business identifier.
A failed transaction may consume a number and produce a gap; it must not produce duplicate identity.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q790. What happens if the sequence reaches its configured limit?

**Reconciled Answer:** When a sequence approaches or reaches its configured capacity, the system shall **stop unsafe allocation rather than wrap around or reuse identifiers**.

The controlled response shall be:
* Detect capacity before unsafe overflow;
* Block new allocation for that sequence;
* Raise an operational/configuration condition;
* Approve a controlled extension of sequence width/capacity or a new numbering policy;
* Preserve all historical identifiers;
* Verify the resulting configuration before activation.

The system shall never silently roll a sequence back to zero or begin reusing previous identifiers.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q791. What is the root storage location on the Windows host?

**Reconciled Answer:** Root storage location is deployment-configured. Recommend a dedicated local fixed-disk volume such as D:\LabNexus\.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q792. Which folders store live documents?

**Reconciled Answer:** Persisted controlled documents use an application-managed document store under the configured storage root.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q793. Which folders store generated PDFs?

**Reconciled Answer:** Generated issued PDFs are stored through the same controlled document system; a logical issued-reports area may be used operationally.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q794. Which folders store attachments?

**Reconciled Answer:** Attachments use the same controlled storage system, separated logically from generated reports.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q795. Which folders store temporary files?

**Reconciled Answer:** Temporary files go to a dedicated temp directory and are never treated as authoritative records.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q796. Which folders store backups?

**Reconciled Answer:** Backups go to locations outside the live-data root; preferably a separate physical volume/device.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q797. Are backup folders on the same physical disk as the live database?

**Reconciled Answer:** No. The authoritative backup must not be on the same physical disk as the live database.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q798. Which backup destinations are local?

**Reconciled Answer:** Recommended local backup = separate fixed physical disk or storage device.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q799. Which backup destinations are removable/offline?

**Reconciled Answer:** Recommended offline backup = removable encrypted HDD/SSD, rotated and physically disconnected when not in use.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q800. Are network paths allowed only for backup copies?

**Reconciled Answer:** Yes. Network paths may be used for backup copies only; never for the live SQLite database.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q801. Which Windows accounts/services need filesystem access?

**Reconciled Answer:** Dedicated Windows service identities: application service, backup service, and Caddy/reverse-proxy service as appropriate.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q802. What NTFS permissions will protect the storage directories?

**Reconciled Answer:** NTFS ACLs use least privilege: app service gets required DB/document access, Caddy gets only its required files, backup service gets read/write access necessary for backup, lab users get no direct storage access.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q803. Who has administrative access to the host?

**Reconciled Answer:** Host administrators are designated IT/System Administration personnel. Their OS privileges remain part of the trusted operational boundary.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q804. How are filesystem permissions documented?

**Reconciled Answer:** NTFS permissions must be documented as part of deployment/operations documentation and verified during deployment.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q805. Can ordinary laboratory users access the storage directories directly?

**Reconciled Answer:** No. Ordinary laboratory users never access document/database directories directly.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q806. How are generated PDFs protected from direct modification?

**Reconciled Answer:** Issued PDFs are protected through NTFS permissions, application-only access, controlled DocumentVersion records and hash verification.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q807. Is file hashing required for documents and PDFs?

**Reconciled Answer:** Yes. SHA-256 hash required for persisted controlled documents/PDFs.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q808. How will hash verification be performed?

**Reconciled Answer:** Hash verification compares stored SHA-256 against the actual file during integrity checks.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q809. How are missing/corrupted files detected?

**Reconciled Answer:** Periodic integrity checks and on-access checks for critical artifacts detect missing/corrupted files.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q810. What happens if a file exists but its database record is missing?

**Reconciled Answer:** Orphan file is quarantined/flagged; no automatic deletion. Investigation determines whether it is recoverable or erroneous.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q811. What happens if a database record points to a missing file?

**Reconciled Answer:** Database reference to missing file creates a storage-integrity incident; application marks artifact unavailable and initiates controlled recovery.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q812. How are orphaned files detected?

**Reconciled Answer:** Scheduled storage-integrity scan compares database-referenced artifacts with physical storage.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q813. Who can repair storage inconsistencies?

**Reconciled Answer:** Only authorized System Administrator/Operations authority may repair storage inconsistencies; repair itself is audited and evidenced.

---

# 29. SQLite Operational Requirements

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q814. What exact SQLite version will be used in production?

**Reconciled Answer:** The production SQLite version shall be a **controlled, pinned, validated release**, not an automatically updated dependency.

The exact production SQLite library version shall be recorded in the Technical Environment / Release Baseline together with:
* Python runtime version;
* `sqlite3.sqlite_version` actually used by the production application;
* SQLAlchemy version;
* Alembic version;
* Windows version/build;
* application release identifier;
* SQLite compile/runtime characteristics relevant to the application.

The application shall not automatically upgrade SQLite or the Python runtime in production.

A SQLite version change shall be treated as a controlled technical change requiring regression testing of:
* migrations;
* foreign-key behavior;
* WAL operation;
* transaction/concurrency behavior;
* backup/restore;
* calculation/result integrity;
* report/history reconstruction;
* critical queries;
* application compatibility.

The exact numeric SQLite version is therefore frozen **at the validated production-release baseline**, rather than arbitrarily selected now without the final runtime/deployment build.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q815. What runtime/library version is approved?

**Reconciled Answer:** Use the SQLite library shipped with/pinned to the approved Python runtime environment; record the exact SQLite library version at installation and in diagnostics.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q816. What PRAGMA settings are mandatory at every connection?

**Reconciled Answer:** Mandatory connection settings: PRAGMA foreign_keys=ON;, PRAGMA journal_mode=WAL;, PRAGMA synchronous=FULL;, PRAGMA busy_timeout=5000;. Other pragmas should be explicitly justified/tested.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q817. How is foreign_keys=ON enforced and verified?

**Reconciled Answer:** Application connection factory executes and verifies foreign_keys=ON on every connection.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q818. How is WAL mode enforced and verified?

**Reconciled Answer:** Database startup/health checks verify journal_mode=WAL.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q819. What busy_timeout value is appropriate for the workload?

**Reconciled Answer:** Recommend 5000 ms busy timeout initially.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q820. What write transaction duration is considered acceptable?

**Reconciled Answer:** Write transactions shall be designed to remain **short and bounded**, with the target that ordinary controlled business writes complete within approximately **500 ms at p95** under the approved normal-workload test environment.
Transactions exceeding the normal target shall be investigated where they materially affect concurrency or operator experience.

The acceptance test shall measure:
* transaction duration;
* p50/p95/p99 where useful;
* number of concurrent writers;
* database size;
* representative business operation;
* audit-row creation;
* associated document/configuration writes where applicable;
* WAL/busy-timeout behavior;
* retry behavior.

This is an **acceptance target for the validated deployment**, not a universal SQLite performance guarantee.
Long-running operations such as PDF generation, bulk integrity verification, backup, migration, or large exports shall not be kept inside ordinary business write transactions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q821. What operations must never happen inside long transactions?

**Reconciled Answer:** Never hold a write transaction across PDF rendering, filesystem I/O, network I/O, long calculations, user interaction, external processes, or lengthy batch processing.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q822. What retry/backoff rules are required for SQLITE_BUSY or SQLITE_LOCKED?

**Reconciled Answer:** Use bounded retry/backoff for transient SQLITE_BUSY/eligible lock-contention conditions, e.g. short exponential delays up to a few seconds; never blindly retry all database errors.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q823. Which operations use read-only access where practical?

**Reconciled Answer:** Use read-only/read-optimized connections/transactions where practical, but do not create a second database or bypass application integrity rules.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q824. How are migrations executed safely with SQLite constraints?

**Reconciled Answer:** SQLite migrations run in controlled maintenance/quiesce mode using Alembic and SQLite-safe migration patterns; protected tables/triggers must survive the migration.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q825. How is database integrity checked before deployment?

**Reconciled Answer:** Before deployment: backup → schema/version validation → integrity_check → foreign_key_check → migration preflight.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q826. How is database integrity checked after backup?

**Reconciled Answer:** After backup: validate backup opens successfully, run integrity checks and verify expected schema/version and critical record counts/metadata.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q827. How is database integrity checked after restore?

**Reconciled Answer:** After restore: integrity_check, foreign_key_check, schema/version check, application startup and smoke-test/recovery verification.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q828. What is the policy for WAL files during backup?

**Reconciled Answer:** Do not independently copy the live .db while treating the WAL as irrelevant. Use SQLite's Online Backup API or another SQLite-consistent backup mechanism that captures a coherent database snapshot.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q829. How is database backup performed consistently while the application is live?

**Reconciled Answer:** Preferred live backup = SQLite Online Backup API; documents/files are copied using controlled file-copy/hash procedure.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q830. What is the approved quiesce method before backup or migration?

**Reconciled Answer:** For migration: enter application maintenance mode → stop new work → drain active writes → stop application → perform migration → validate → restart.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q831. Can backups run without stopping the application?

**Reconciled Answer:** Yes, backups can run while the application remains live using the SQLite Online Backup API. SQLite documents this explicitly.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q832. What happens if the database becomes locked unexpectedly?

**Reconciled Answer:** Detect lock contention → bounded retry → user-friendly temporary-busy message if exhausted → log/monitor the event.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q833. What is the operator procedure for database corruption?

**Reconciled Answer:** Stop/quiesce → preserve original DB/WAL/SHM as evidence → assess integrity → restore last known-good validated backup → verify → investigate/recover missing transactions. Never experiment on the original corrupted database.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q834. What is the approved maximum database size for v1 operations?

**Reconciled Answer:** No hard absolute DB-size limit should be frozen now. Operational ceiling must come from workload testing. SQLite's theoretical limit is vastly beyond this application's needs and should not be treated as an operational target.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q835. What monitoring will show database size/growth?

**Reconciled Answer:** Monitor database file size, WAL size, free disk space, daily growth rate, backup duration and backup size.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q836. When will archival/maintenance be required?

**Reconciled Answer:** Maintenance/archival is triggered by measured operational thresholds, retention policy, backup/restore duration, disk capacity, query performance or integrity/operational requirements—not simply because a particular age was reached.

---

# 30. LAN, Windows, and Network Operation

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q837. What Windows edition/server version is the production target?

**Reconciled Answer:** Production target: Windows 11 Pro on the laboratory's existing mini PC. Windows Server is not required for v1.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q838. What Windows version is the development/test target?

**Reconciled Answer:** Development/test target: Windows 11 Pro is the preferred reference environment for v1. Development may also occur on another supported Windows machine, provided the final build is validated on the production environment.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q839. What host hardware will be used?

**Reconciled Answer:** Host hardware: existing laboratory mini PC.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q840. What CPU, RAM, and storage are available?

**Reconciled Answer:** CPU: Intel Core i3-9100; RAM: 8 GB. Storage: to be recorded from the actual mini PC before deployment. Do not invent a storage capacity.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q841. Is the host a dedicated machine?

**Reconciled Answer:** The mini PC should be treated as the dedicated LabNexus production host. It performs the server role even though it is not server-class hardware.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q842. Is the host also used for unrelated workloads?

**Reconciled Answer:** No unrelated workloads should routinely run on the host. LabNexus should have priority on the machine.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q843. What is the server hostname?

**Reconciled Answer:** Deployment-specific hostname. The actual hostname is a laboratory infrastructure input and should not be hard-coded into LabNexus.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q844. What is the static IP or DNS name?

**Reconciled Answer:** Deployment-specific static IP or DNS name. Prefer a stable hostname with a static IP or DHCP reservation. Actual value remains a deployment input.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q845. Is DNS available on the LAN?

**Reconciled Answer:** LAN DNS availability is a deployment input. If laboratory DNS is available, use it; otherwise stable local hostname/IP resolution must be provided by the deployment.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q846. What URL should users open?

**Reconciled Answer:** Deployment-specific HTTPS URL, for example https://lims.<laboratory-internal-domain>. The actual URL must be configurable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q847. Is HTTPS mandatory on the LAN?

**Reconciled Answer:** Yes. HTTPS is mandatory even on the laboratory LAN.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q848. How will the local TLS certificate be created and renewed offline?

**Reconciled Answer:** Use a local/private CA or Caddy's controlled internal CA for the deployment. Certificate issuance/renewal must work without Internet access and must be documented.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q849. Is an internal CA available?

**Reconciled Answer:** Deployment input: determine whether the laboratory already has an internal CA. If not, the v1 deployment may use a controlled LabNexus/Caddy local CA arrangement.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q850. How are client machines trusted?

**Reconciled Answer:** Client machines must trust the CA that issued the LabNexus certificate. Trust should be established through the laboratory's controlled Windows trust mechanism; users should not be instructed to bypass certificate warnings.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q851. Is the application accessible only on the laboratory LAN?

**Reconciled Answer:** Yes. V1 is LAN-only. LabNexus shall not be publicly accessible.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q852. Is remote access required?

**Reconciled Answer:** No remote access is required for v1.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q853. If remote access is required, what approved secure mechanism will be used?

**Reconciled Answer:** Not applicable for v1. Any future remote access shall use an approved VPN-based mechanism; direct Internet exposure is prohibited.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q854. Is Internet access blocked from the server?

**Reconciled Answer:** Core LabNexus does not require Internet access. Routine outbound Internet access from the production host should be blocked or otherwise restricted according to laboratory policy.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q855. Must core application functions continue when Internet connectivity is absent?

**Reconciled Answer:** Yes. Core application functions must continue normally when Internet connectivity is absent.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q856. Which features, if any, may degrade without Internet?

**Reconciled Answer:** Only explicitly optional external functions may degrade, such as future email delivery, external integrations, or update-related functions. Core sample/test/result/review/verification/approval/reporting operations shall not depend on Internet access.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q857. Are email, external APIs, remote licensing, or update checks allowed?

**Reconciled Answer:** External Internet-dependent services are not required for v1. Email, external APIs, remote licensing, and online update checks must not be dependencies for core operation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q858. Are automatic software updates allowed on the host?

**Reconciled Answer:** No automatic LabNexus software updates. Releases shall be deliberately installed through a controlled maintenance/release process.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q859. How are OS updates scheduled?

**Reconciled Answer:** OS updates shall be applied during planned maintenance windows, after compatibility/risk review and with an appropriate backup/recovery point.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q860. How are application updates scheduled?

**Reconciled Answer:** Application updates shall use a controlled release process: validated build → backup → maintenance window → installation/migration → verification → rollback/recovery procedure if required.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q861. How are Chromium updates controlled so PDF rendering remains stable?

**Reconciled Answer:** Chromium used for PDF rendering shall be pinned to a validated version/build. Updates occur only through a controlled LabNexus release process with PDF regression testing.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q862. How are browsers on client PCs supported?

**Reconciled Answer:** Client PCs shall use supported, maintained browsers and need not match the production host hardware.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q863. What browsers are officially supported?

**Reconciled Answer:** Record actual browser versions validated for each release.
**Revision 0.8 Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Test / Validation Environment Baseline

### Q864. What happens if a user loses LAN connectivity during a transaction?

**Reconciled Answer:** If LAN connectivity is lost during a transaction, the server-side transaction shall either commit completely or roll back; partial database writes must not occur. The client must clearly indicate that the operation's final status is uncertain until confirmed. Critical commands should use idempotency/command identifiers where retry could otherwise duplicate an action.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q865. What should users see when the application is unreachable?

**Reconciled Answer:** When the application is unreachable, users should see a clear operational error/status page, not a raw server traceback. It should indicate that LabNexus cannot currently be reached and advise the user to check LAN connectivity or contact the responsible administrator.

---

# 31. Deployment and Release Management

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q866. What is the approved production installation method?

**Reconciled Answer:** Approved production installation method: controlled installation from a versioned LabNexus release bundle containing application build, dependency manifest, migration package, configuration template, release notes, checksums, and deployment instructions/scripts. No ad-hoc file copying or direct source-code deployment.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q867. Is there a development environment separate from validation/UAT?

**Reconciled Answer:** Yes. Development must be separate from validation/UAT. Development changes must not be tested directly against production.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q868. Is there a staging environment?

**Reconciled Answer:** A permanently separate staging environment is not required for v1. The validation/UAT environment will serve as the controlled pre-production environment.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q869. Is a validation environment required?

**Reconciled Answer:** Yes. A validation environment is required before production release.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q870. Where will each environment run?

**Reconciled Answer:** Development: developer machine(s). Validation/UAT: separate Windows machine/environment from production where practical. Production: laboratory's dedicated mini PC.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q871. How is configuration kept separate between environments?

**Reconciled Answer:** Environment configuration must be separate. Each environment has its own database, file/document root, configuration, certificates, and environment-specific settings. Production configuration must never be copied into development/test.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q872. How are secrets stored per environment?

**Reconciled Answer:** Secrets must be stored separately per environment and never committed to source control. Production secrets shall be protected by OS-level access controls and encrypted/protected storage.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q873. Who can deploy to each environment?

**Reconciled Answer:** Developers may deploy to development. Authorized technical/project personnel may deploy to validation. Production deployment is restricted to the designated LIMS System Administrator/deployment authority.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q874. Who can approve production deployment?

**Reconciled Answer:** Production deployment requires approval by the designated Project/Laboratory authority after validation evidence is complete. The person who executes deployment should not be the sole approver of that deployment.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q875. What exact pre-deployment checks are mandatory?

**Reconciled Answer:** Mandatory checks: approved release version; validation/UAT passed; release checksum verified; production backup completed and validated; sufficient disk space; maintenance window confirmed; active writes stopped; migration package verified; rollback/recovery path available; deployment evidence record opened.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q876. What exact backup must be created before migration?

**Reconciled Answer:** Before any database migration, create a validated pre-deployment recovery set containing the SQLite database, associated documents/attachments, controlled configuration, and deployment manifest/metadata.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q877. How is the backup validated before proceeding?

**Reconciled Answer:** Validate the backup by opening the backup copy, running SQLite integrity checks and foreign-key checks, confirming schema/version metadata, expected record counts/metadata, verifying document hashes, and confirming the recovery-set manifest.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q878. What does “stop/quiesce” mean operationally?

**Reconciled Answer:** “Stop/quiesce” means: stop creation of new writes; prevent new transactions from starting; allow already-running requests to finish; confirm no active write operations remain; place application into maintenance mode; then stop application services before migration.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q879. How is active user activity checked before migration?

**Reconciled Answer:** Active activity shall be checked through application session/activity status plus confirmation that no write transaction is in progress. New writes must be blocked before the final migration step.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q880. How is Alembic migration executed in production?

**Reconciled Answer:** Alembic production migration shall run only during the approved maintenance window, against the validated production database, using the exact release's pinned environment and migration revision. Migration logs must be captured.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q881. What happens if migration fails halfway?

**Reconciled Answer:** If migration fails: stop immediately, preserve the original database/WAL/SHM and logs, do not continue blindly, declare deployment failure, and recover using the approved rollback mechanism.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q882. Is the database restored from backup or migrated back through downgrade?

**Reconciled Answer:** Production recovery shall use the pre-migration validated backup/recovery set, not an attempted downgrade of a partially migrated production database.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q883. Which rollback mechanism is actually approved?

**Reconciled Answer:** Approved production rollback mechanism = restore the validated pre-deployment recovery set. Alembic downgrade is not the primary production rollback mechanism.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q884. Are Alembic downgrades maintained/tested for all migrations?

**Reconciled Answer:** Alembic downgrades should be maintained and tested where technically safe and useful, but they are not relied upon for production recovery.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q885. What is the failed-upgrade recovery procedure?

**Reconciled Answer:** Failed-upgrade recovery: stop services → preserve failed state/evidence → confirm failure → restore pre-deployment database/documents/configuration as applicable → validate restored state → deploy known-good release → smoke test → record incident/deployment failure.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q886. What smoke tests are mandatory after deployment?

**Reconciled Answer:** Mandatory post-deployment smoke tests: service starts; HTTPS access works; login works; database connectivity works; schema revision matches release; role enforcement works; sample/test/report retrieval works; document access works; PDF generation works; audit/event recording works; backup subsystem is operational.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q887. What does “resume” mean after deployment?

**Reconciled Answer:** “Resume” means maintenance mode is removed, normal user access is restored, smoke tests have passed, monitoring is normal, and users are formally informed that production use may continue.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q888. Who records deployment evidence?

**Reconciled Answer:** The System Administrator/deployment executor records deployment evidence. The designated approver/reviewer verifies completeness.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q889. What exact evidence is retained per release?

**Reconciled Answer:** Retain: release ID; package checksum; date/time; host/environment; operator; approver; pre-check results; backup ID/hash; migration revision and logs; smoke-test results; final status; rollback details if applicable; incidents/deviations.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q890. How are release versions identified?

**Reconciled Answer:** Release versions should use a stable semantic version such as MAJOR.MINOR.PATCH, with an optional build identifier. Example: 1.0.0.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q891. How are deployed software version and database schema version linked?

**Reconciled Answer:** Each deployment record shall capture LabNexus application release version + exact Alembic schema revision. The release manifest explicitly links the two.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q892. How are release notes stored?

**Reconciled Answer:** Release notes shall be stored as controlled repository documentation under a versioned release record and included with the release bundle.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q893. How are failed releases marked?

**Reconciled Answer:** A failed release is recorded explicitly as FAILED, linked to its deployment/evidence record and any incident/corrective action. It must never be silently overwritten as successful.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q894. How is production deployment prevented if validation evidence is incomplete?

**Reconciled Answer:** Production deployment shall be blocked by the deployment checklist/process when mandatory validation evidence, backup validation, approval, or required preconditions are incomplete.

---

# 32. Backup and Recovery

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q895. What is the target Recovery Point Objective (RPO)?

**Reconciled Answer:** The v1 Recovery Point Objective shall be **24 hours maximum for ordinary operational data**, with a more stringent target of **4 hours** where the laboratory has operational capability to perform additional backup cycles.

The recommended acceptance baseline is therefore:
**Target RPO: ≤ 4 hours**
**Maximum permitted operational RPO: ≤ 24 hours**

RPO shall apply to the complete recoverable set, not merely the SQLite database. The recovery set must include the database plus controlled document/attachment data and the configuration/evidence necessary to restore an operationally coherent state.
The final RPO shall be validated against actual backup frequency, media handling, restore capability, and laboratory operating needs before production acceptance.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q896. What is the target Recovery Time Objective (RTO)?

**Reconciled Answer:** The v1 Recovery Time Objective shall be established as:

**Target RTO: ≤ 8 hours for restoration of the core LIMS service**
The RTO measurement shall start from a defined recovery declaration point and end when the validated LIMS environment is operational and capable of performing controlled core operations.

The RTO shall include, as applicable:
* replacement/recovery host preparation;
* application deployment;
* database restoration;
* document/attachment restoration;
* configuration recovery;
* integrity checks;
* service startup;
* smoke testing;
* critical functional verification;
* authorization/session verification.

The RTO is a **validated recovery acceptance target**, not a guaranteed response time under every possible disaster scenario.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q897. How frequently must the database be backed up?

**Reconciled Answer:** The recommended v1 backup schedule is:
**Database:** at least daily, with additional backup points sufficient to meet the approved RPO target.
**Operational backup target:** database backup at least every **4 hours** during normal laboratory operation where practical.

A daily backup alone does not satisfy a 4-hour RPO.

The backup schedule shall distinguish:
* routine scheduled backup;
* pre-maintenance/pre-migration backup;
* controlled on-demand backup;
* pre-restore safety backup where applicable;
* backup validation.

The laboratory shall document which backup classes are retained and how they map to the RPO.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q898. How frequently must documents/attachments be backed up?

**Reconciled Answer:** Documents and attachments shall be backed up on a schedule that is **no less protective than the database backup strategy**.
The preferred v1 approach is to include changed/new controlled documents and attachments in the recovery sets generated at least every **4 hours**, with a complete backup cycle at least daily.
Document backup shall not rely only on periodic manual copying because that can produce a database/document mismatch.
A recovery point must therefore be capable of identifying the corresponding database and document state.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q899. Must database and document backups be consistent to the same point in time?

**Reconciled Answer:** Yes. Database and document backups shall be **coherent to the same recovery point** to the extent required for reliable reconstruction.

The preferred model is a logical **Recovery Set** containing:
* Database backup;
* Corresponding controlled document/attachment state;
* Relevant configuration/change state;
* Consistency marker or recovery-set identifier;
* Application/release/schema identity;
* Integrity hashes/checks;
* Backup creation/validation evidence.

Where filesystem-level capture cannot be literally instantaneous with SQLite state, the application shall use a controlled quiesce/snapshot/backup procedure that establishes a known consistency boundary.
A database backup without its corresponding document state shall not be treated as a complete recoverable LIMS backup.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q900. How many backup copies are retained?

**Reconciled Answer:** The operational backup policy shall maintain **at least 3 independently retained Recovery Set copies** covering the approved backup rotation.
At least one retained copy shall be physically separate from the live LIMS host, and the rotation shall ensure that a single host failure, filesystem failure, or local incident does not destroy every available Recovery Set.
The three-copy minimum is an operational baseline, not a substitute for backup validation and restore testing.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q901. What is the retention period for backups?

**Reconciled Answer:** Use a two-tier operational policy:
* **Daily/rolling Recovery Sets:** retain for at least **30 days**.
* **Monthly Recovery Sets:** retain for at least **12 months**.

Longer retention may be applied where required by the laboratory's approved recovery, legal, quality, or business policy.
Backup retention is distinct from the **10-year controlled laboratory-record retention requirement**. Backup copies are recovery media and do not replace preservation of the authoritative laboratory record.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q902. How many removable/offline backup copies are maintained?

**Reconciled Answer:** Maintain **at least 2 rotating removable/offline Recovery Set copies**.
The copies shall be rotated so that at least one is available as a controlled recovery source while another can remain physically separate from the production host.
Where practical, one copy should be stored at a physically separate approved location.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q903. Where are offline backups physically stored?

**Reconciled Answer:** Offline backup media shall be stored in a **restricted, controlled location physically separate from the LIMS host**, protected against unauthorized access, environmental damage, and casual loss.
At least one rotated offline copy should, where practical, be maintained at a **physically separate approved location** from the production host.
The exact storage location shall be documented in the backup custody record and shall not be exposed to ordinary LIMS users.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q904. Who controls offline backup media?

**Reconciled Answer:** Offline backup media shall be controlled by the designated **System Administrator / Backup Operations authority**, with laboratory management/Quality oversight.

Media movement shall be documented sufficiently to establish:
* media identity;
* Recovery Set identity;
* date/time;
* person releasing/receiving custody;
* storage location;
* integrity/validation status;
* return or disposal status.

Ordinary laboratory users shall not have unrestricted physical or technical control of backup media.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q905. How is backup media labelled?

**Reconciled Answer:** Each removable/offline backup medium shall have a unique controlled identifier and shall be associated with:
* Recovery Set identifier;
* backup date/time;
* media sequence/rotation identifier;
* retention/destruction date where applicable;
* encryption status;
* validation status.

Labels shall avoid exposing unnecessary sensitive laboratory information.
The authoritative detailed metadata shall also exist in the controlled backup record; the physical label alone shall not be the complete record.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q906. How is backup media integrity checked?

**Reconciled Answer:** Backup integrity shall be verified using a combination of:
* controlled backup manifest;
* cryptographic hashes for backed-up files/artifacts where applicable;
* SQLite/database integrity validation;
* successful readability/access checks;
* Recovery Set completeness checks;
* periodic actual restore testing.

A backup shall not be classified as **Restorable** merely because a file was successfully copied.
The controlled states remain distinct: Backup Created → Validated → Restorable → Restore Tested → Recovery Procedure Verified.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q907. Are backups encrypted?

**Reconciled Answer:** Yes. Removable/offline backups containing laboratory records, reports, customer information, or other controlled data shall be **encrypted using an approved encryption mechanism**.
Encryption shall apply to the backup medium or protected backup container rather than relying solely on Windows filesystem permissions.
Encryption is an additional protection layer and does not replace physical custody controls, integrity verification, or restore testing.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q908. If yes, where are encryption keys stored?

**Reconciled Answer:** Backup encryption keys shall be stored **separately from the encrypted backup media**, under restricted technical custody.
Keys shall not be stored unprotected on the same removable medium as the encrypted backup and shall not be embedded in the LIMS database or frontend.
A controlled offline recovery record shall identify how authorized recovery personnel can obtain the required key without requiring Internet access.
The number of authorized persons with key-recovery access shall be minimized, and key recovery shall itself be controlled and auditable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q909. Who may restore a backup?

**Reconciled Answer:** Only authorized **System Administrators or explicitly designated recovery personnel** may execute production backup restoration.
Laboratory Analysts, Reviewers, Verifiers, Approvers, and ordinary application administrators shall not have restore authority.

Restore authorization shall be separate from ordinary laboratory technical authority and shall require:
* Controlled recovery reason;
* Identified recovery set;
* Authorization;
* Pre-restore backup/safety point where applicable;
* Restore execution evidence;
* Post-restore verification.

A restore operation shall never be used as an ordinary record-correction mechanism.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q910. Who may inspect backup contents?

**Reconciled Answer:** Backup contents may be inspected only by authorized personnel whose duties require such access.

Access shall be separated into:
* **Operational/recovery inspection:** System Administrator/recovery personnel;
* **Technical/quality verification:** authorized Quality/Technical personnel where needed;
* **Sensitive-content inspection:** limited to personnel with the appropriate record confidentiality authorization.

Backup inspection must not become an uncontrolled route to bypass LabNexus RBAC.
All access to sensitive backup contents should be treated as privileged activity, with access/download auditing where technically appropriate.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q911. What exactly is included in a backup?

**Reconciled Answer:** A complete v1 Recovery Set shall include, as applicable:
* SQLite database;
* Application-controlled documents;
* Attachments;
* Issued PDFs;
* Controlled configuration required to interpret the data;
* Required deployment configuration;
* Migration/configuration history necessary for reconstruction;
* Schema/release identity;
* Backup manifest;
* Integrity hashes/checks;
* Recovery-set consistency metadata.

The backup shall not require copying transient cache, temporary files, browser data, generated intermediate artifacts, or other disposable runtime material.
The authoritative backup contract shall distinguish **recoverable business data** from **reproducibly deployable software**.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q912. What is excluded from backups?

**Reconciled Answer:** The following should normally be excluded from the authoritative business backup unless separately required:
* Temporary files;
* Browser cache;
* Application cache;
* Build intermediates;
* Test data;
* Development environments;
* Uncommitted source-tree artifacts;
* Transient Chromium/rendering files;
* OS temporary files;
* Disposable logs outside the approved evidence-retention policy.

Security/operational logs that are required as evidence shall be retained through their separate controlled mechanism.
Production source code need not be treated as irreplaceable backup content if the approved release is reproducibly obtainable from the authoritative Git/release repository and deployment artifacts.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q913. Are application binaries backed up or reproducibly redeployed?

**Reconciled Answer:** Production software shall be **reproducibly redeployed from controlled release artifacts**, with an additional ability to retain the exact production release package where operationally appropriate.

The recovery baseline shall therefore identify:
* Application release/tag;
* Backend/frontend build artifacts;
* Python dependency lock/baseline;
* Frontend dependency lock/build;
* Migration version;
* Chromium version;
* Windows/deployment prerequisites;
* Configuration schema/version.

The system should not rely exclusively on a copied production application directory as its only software recovery mechanism.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q914. Are configuration files backed up?

**Reconciled Answer:** Yes. Production configuration required to recreate the validated environment shall be backed up or otherwise recoverably recorded.

This includes, as applicable:
* Caddy configuration;
* Application deployment configuration;
* Storage-root configuration;
* controlled rendering configuration;
* database connection/runtime configuration;
* approved operational settings;
* deployment-specific certificates/configuration metadata where appropriate;
* non-secret configuration.

Secrets shall be handled separately under the secret-management/recovery procedure and shall not be copied into ordinary configuration backups in plaintext.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q915. Are TLS certificates/keys backed up?

**Reconciled Answer:** Yes, the recovery process shall preserve the ability to recover required **TLS certificates and private keys**, but secret/private-key material shall be handled separately from ordinary data backups.

The recovery design shall maintain:
* Certificate identity;
* Certificate chain where required;
* Private-key recovery mechanism;
* Expiry information;
* Trust/CA configuration;
* Protected storage/access;
* Recovery testing.

Private keys shall not be stored in ordinary unencrypted application backups.
For the offline local/private-CA model, the CA/private-key recovery procedure is part of deployment recovery evidence.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q916. Are secrets backed up?

**Reconciled Answer:** Secrets shall **not be treated as ordinary database/application backups**.

The recovery design shall instead maintain a protected secret-recovery mechanism for:
* Application/session secret material;
* Backup-encryption keys where used;
* TLS private keys;
* Service credentials where required;
* Approved external credentials where applicable.

Secrets may be backed up or escrowed only in an approved protected form and separately from ordinary business-data backups.
The recovery procedure must establish that a host-loss recovery can obtain the necessary secrets without exposing them to ordinary users.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q917. How are secrets recovered after host loss?

**Reconciled Answer:** After host loss, secrets shall be recovered through a **controlled offline secret-recovery procedure**.

The procedure shall define:
* Authorized recovery personnel;
* Secret inventory;
* Protected secret location/custody;
* Authentication/authorization required to retrieve it;
* Backup-encryption-key recovery;
* TLS/CA-key recovery where applicable;
* Application-secret recovery;
* Secret rotation after suspected compromise;
* Evidence of recovery use.

Secret values shall never be copied into ordinary recovery documentation, logs, Git, or incident reports.
A recovery test must demonstrate that the designated personnel can actually reconstruct the application securely.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q918. How is a backup marked “validated”?

**Reconciled Answer:** A backup shall be marked **Validated** only after successful non-destructive integrity checks appropriate to its contents.

Validation shall include, as applicable:
* Backup file/media readability;
* Hash/checksum verification;
* Database structural/integrity check;
* Expected document/attachment count checks;
* Manifest/control-total comparison;
* Recovery-set consistency verification;
* Successful completion of the backup job;
* Absence of unexplained missing/corrupt artifacts.

`Backup Created` and `Backup Validated` are separate statuses.
A file-copy success message alone shall never establish validation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q919. How is a backup marked “restorable”?

**Reconciled Answer:** A backup shall be marked **Restorable** only after the organization has demonstrated that the backup can actually be used to construct a functioning recovery environment.
`Restorable` therefore requires more than integrity verification.

The restore test shall demonstrate:
* Database restoration;
* Document/attachment restoration;
* Required configuration restoration;
* Application startup;
* Schema/migration compatibility;
* Critical record retrieval;
* Report/PDF retrieval;
* Authentication;
* Representative core workflow access;
* Integrity verification after restoration.

A backup may be Validated without yet being classified Restorable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q920. What test proves a restore is successful?

**Reconciled Answer:** A restore shall be considered successful only when the restored environment passes a defined **Recovery Verification Test**.

At minimum:
* Database integrity succeeds;
* Expected schema/migration version is present;
* Representative Samples/TestInstances/Results are retrievable;
* Historical ResultRevision/ApprovalSnapshot relationships remain intact;
* Representative issued PDFs/documents open and pass hash/integrity checks;
* Application starts correctly;
* Authentication and authorization function;
* Critical read/write smoke tests succeed;
* Audit trail operates;
* No required recovery component is missing.

The successful restore test must be independently reviewed and recorded as evidence.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q921. How often must restore testing occur?

**Reconciled Answer:** A complete Recovery Set restore test shall be performed **at least quarterly**.

Additional restore testing shall occur after:
* a material backup/recovery procedure change;
* a major infrastructure/storage change;
* a material LIMS deployment change affecting recovery;
* detection of a backup-integrity deficiency;
* a significant recovery incident.

Quarterly frequency is the minimum operational baseline; more frequent testing may be required by risk or observed failure trends.
A successful file copy or database integrity check alone does not satisfy the restore-test requirement.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q922. Must restore testing use production-like hardware?

**Reconciled Answer:** Restore testing shall use hardware that is **representative of the production recovery environment**, but does not have to be literally identical to production hardware.

The test environment shall be sufficiently representative of:
* CPU/memory/storage characteristics relevant to recovery;
* Windows version;
* SQLite/application runtime;
* document storage structure;
* Chromium/reporting environment;
* network/LAN configuration where relevant.

The laboratory shall record material differences between the test and production recovery environment and assess whether they could invalidate the recovery evidence.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q923. What constitutes “Recovery Procedure Verified”?

**Reconciled Answer:** `Recovery Procedure Verified` shall mean that the **documented recovery procedure has actually been executed successfully** using a controlled Recovery Set and has produced an operational environment meeting the approved recovery acceptance criteria.

It requires:
* Defined recovery scenario;
* Identified backup/recovery set;
* Actual execution;
* Recorded timestamps;
* Expected/actual results;
* Integrity verification;
* Functional verification;
* Recovery-duration evidence;
* Deviations/defects;
* Independent review;
* Formal acceptance.

Merely reviewing the written recovery procedure does not establish verification.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q924. What evidence is kept from restore tests?

**Reconciled Answer:** Restore-test evidence shall include:
* Recovery-test ID;
* Date/time;
* Recovery scenario;
* Recovery Set ID;
* Backup version/date;
* Source environment;
* Target recovery environment;
* Software/release/schema versions;
* Restore procedure/version;
* Start/end times;
* RPO/RTO measurements;
* Integrity checks;
* Functional test results;
* PDF/document verification;
* Defects/deviations;
* Corrective actions;
* Reviewer/verifier;
* Acceptance/disposition.

The evidence package shall be sufficient for an independent reviewer to understand what was actually tested.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q925. What happens if restore testing fails?

**Reconciled Answer:** A failed restore test shall immediately trigger a **recovery deficiency**.

The affected backup shall not be classified Restorable.

The response shall include:
* Record the failure;
* Identify failed recovery component;
* Preserve evidence;
* Assess impact on current recovery capability;
* Determine whether another Recovery Set is usable;
* Correct the recovery/backup defect;
* Repeat the restore test;
* Reassess RPO/RTO capability;
* Escalate material deficiencies through the Quality/Technical change or risk process.

A known failed restore test shall not be hidden by simply marking the backup as validated.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q926. How are backup failures alerted to operators?

**Reconciled Answer:** Backup failures shall produce an **in-application operational alert** and an audit/evidence record.
Where the laboratory has an approved local notification mechanism, the failure may additionally be surfaced to designated operational personnel.
Because email/SMS are not mandatory v1 dependencies, backup-failure monitoring must work without Internet connectivity.

The alert should identify:
* Backup type;
* Intended schedule;
* Failure time;
* Failure reason;
* Last successful validated backup;
* Current RPO exposure;
* Required operator action.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q927. Who reviews backup status?

**Reconciled Answer:** Backup status shall be reviewed by the **designated System Administrator/Backup Operations role**, with Laboratory Quality/Management visibility for material recovery deficiencies.

The operational dashboard should expose at least:
* Last successful backup;
* Last validated backup;
* Last restorable/tested backup;
* Backup age;
* Failed/missed backups;
* Recovery-set status;
* Storage warnings.

Periodic review evidence should be retained according to the laboratory's operational/QMS requirements.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q928. How is a missed backup handled?

**Reconciled Answer:** A missed backup shall trigger an operational exception.

The system shall:
1. Detect the missed schedule where monitoring is available;
2. Record the failure/miss;
3. Identify the last successful validated backup;
4. Attempt the next controlled backup;
5. Assess current RPO exposure;
6. Escalate when the approved RPO threshold is threatened or exceeded;
7. Record corrective action.

A missed backup must not be silently treated as successful simply because a previous backup exists.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q929. How is backup corruption detected?

**Reconciled Answer:** Backup corruption shall be detected through multiple controls:
* Cryptographic hash/checksum verification;
* Backup-manifest/control-total validation;
* Database integrity checks;
* File readability checks;
* Periodic restore testing;
* Storage/media health checks where available.

A backup that passes file-level hashing but fails actual database/document restore shall be considered **not restorable**.
Restore testing therefore provides the strongest practical evidence that backups are usable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q930. How is a disaster involving total host loss handled?

**Reconciled Answer:** Total host loss shall be handled through the controlled **disaster recovery procedure**.

The recovery sequence shall be:
**Secure replacement/recovery host → prepare validated Windows environment → deploy exact LabNexus release → restore protected configuration/secrets → restore Recovery Set → verify database/documents → verify integrity → smoke test → recover services → record evidence → resume controlled operation**

The recovery plan shall identify:
* Replacement-host requirements;
* Software/release baseline;
* Backup/recovery location;
* Secret/certificate recovery;
* Storage configuration;
* Network/Caddy configuration;
* Recovery roles;
* Verification criteria;
* RPO/RTO measurement.

The original failed host shall not be assumed trustworthy merely because it can be restarted.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q931. How is a disaster involving only database corruption handled?

**Reconciled Answer:** Database-only corruption shall use a controlled database-recovery path:
1. Quiesce application writes;
2. Preserve the corrupt database as evidence;
3. Identify the latest validated coherent Recovery Set;
4. Restore the database;
5. Restore corresponding documents/configuration where required;
6. Run SQLite/database integrity checks;
7. Verify migrations/schema;
8. Verify representative historical records/results/audit;
9. Verify reports and documents;
10. Perform smoke testing;
11. Record recovery evidence;
12. Resume operations only after acceptance.

The corrupt original must not simply be overwritten before preservation/evidence requirements are satisfied.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q932. How is a disaster involving missing documents handled?

**Reconciled Answer:** Missing documents shall be treated as an **artifact-integrity/recovery incident**, not as a reason to regenerate historical PDFs from current mutable data.

The procedure shall:
* Identify missing/corrupt artifacts;
* Identify affected Document/ReportRevision records;
* Compare stored hash/identity;
* Retrieve from the appropriate validated backup;
* Restore the exact artifact;
* Recalculate/verify the SHA-256 hash;
* Confirm the restored bytes match the recorded identity;
* Record the recovery event;
* Escalate unresolved losses through nonconformance/recovery governance.

Where an exact issued PDF cannot be recovered, the loss shall remain explicitly documented rather than silently replaced with a newly generated PDF.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q933. How is simultaneous database-and-document restore validated?

**Reconciled Answer:** Simultaneous database-and-document restore shall be validated as a **single coherent recovery scenario**.

The verification shall prove:
* Database belongs to the identified Recovery Set;
* Document/attachment store belongs to the same Recovery Set;
* Expected document references resolve;
* ReportResultSnapshots point to the correct historical data;
* ReportRevisions resolve to the intended DocumentVersions/PDF artifacts;
* Stored PDF hashes match recovered bytes;
* Representative technical records and issued reports reconstruct correctly;
* No unexplained orphaned/missing relationships remain.

This is the preferred final acceptance test for the complete LIMS recovery boundary.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q934. What system health information must be visible to administrators?

**Reconciled Answer:** Administrators need visibility of: service status, application version, DB/schema version, DB health, document-store health, free disk space, backup freshness/status, failed jobs, PDF failures, certificate expiry, active maintenance state, and recent critical errors.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q935. Must the application expose a health check endpoint?

**Reconciled Answer:** Yes. LabNexus shall expose an internal health-check endpoint.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q936. Must the health check verify database connectivity?

**Reconciled Answer:** Yes. Health check must verify database connectivity and required DB state.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q937. Must the health check verify document storage access?

**Reconciled Answer:** Yes. It must verify required document storage is accessible and writable where appropriate.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q938. Must the health check verify report rendering availability?

**Reconciled Answer:** Yes. It must verify the report/PDF rendering subsystem is available.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q939. Must the health check verify backup subsystem status?

**Reconciled Answer:** Yes. It must report backup subsystem status/freshness and most recent backup result.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q940. What warnings should be shown to operators?

**Reconciled Answer:** Warnings should include stale/failed backup, low disk space, document-store failure, DB/storage problem, failed PDF generation, failed scheduled job, certificate expiry approaching, unexpected service state, maintenance mode, and integrity/recovery-test failure.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q941. How are low-disk-space conditions detected?

**Reconciled Answer:** Low disk space detected by periodic health checks/service monitoring on all relevant volumes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q942. What threshold should trigger a warning?

**Reconciled Answer:** For the LIMS host's application-controlled storage, issue an operational warning when available free space falls below **20% of the relevant volume capacity or 20 GiB, whichever condition is reached first**.
The warning shall be persistent enough to attract operator attention and shall identify the affected storage resource and current free-space condition.
The threshold is an operational warning control and shall be validated against the actual production host.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q943. What threshold should block risky operations?

**Reconciled Answer:** Risky write operations shall be blocked when available free space falls below **10% of the relevant volume capacity or 10 GiB, whichever condition is reached first**, subject to controlled recovery/administration exceptions.
Risky operations include activities that could materially consume additional storage or create an incomplete controlled artifact, such as large document ingestion or report issuance where sufficient storage cannot be guaranteed.
Ordinary read-only access should remain available where technically safe.
The system shall provide a clear controlled error rather than allowing an operation to fail unpredictably because the filesystem becomes full.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q944. How is database growth monitored?

**Reconciled Answer:** Monitor DB size and growth rate at least daily; retain historical size measurements sufficient to identify abnormal growth.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q945. How are document storage growth and capacity monitored?

**Reconciled Answer:** Monitor document storage size/free space and growth rate at least daily.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q946. How are failed PDF generations monitored?

**Reconciled Answer:** Failed PDF generation recorded as a structured operational error containing relevant Report/Revision identifiers, error category, time, and retry status.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q947. How are failed background/maintenance jobs recorded, if any?

**Reconciled Answer:** Any scheduled/background job failure must create a structured operational event with job name, timestamp, status, error category, and retry/result.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q948. Are scheduled tasks required?

**Reconciled Answer:** Yes. Scheduled tasks are required for backups, health checks, cleanup/retention tasks where applicable, and other controlled maintenance operations.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q949. Which operational tasks are automated versus manual?

**Reconciled Answer:** Automated: backups, routine integrity checks, health checks, disk monitoring, job monitoring. Manual/authorized: restore, production release, migration approval, configuration approval, incident recovery, controlled archival.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q950. What logs are retained?

**Reconciled Answer:** Retain application operational logs, security/authentication logs, error logs, service/deployment logs, backup/restore logs, and scheduled-job logs. Controlled technical audit history remains in the application database.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q951. Who can access application logs?

**Reconciled Answer:** Application logs accessible primarily to System Administrators; authorized quality/technical personnel may receive read access where needed for investigation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q952. Do logs contain sensitive information?

**Reconciled Answer:** Logs must be treated as potentially sensitive because they may contain identifiers and operational context. They should not contain unnecessary test-result or customer data.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q953. How is sensitive information prevented from entering logs?

**Reconciled Answer:** Structured logging with an allow-list of safe fields; never log passwords, tokens, session identifiers, secrets, private keys, or full sensitive request payloads.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q954. How are log files rotated?

**Reconciled Answer:** Logs shall rotate automatically by date and/or size, with bounded retention so the host cannot fill its disk from logs.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q955. What is the retention period for operational logs?

**Reconciled Answer:** Routine application/operational logs shall be retained for **12 months** under controlled rotation.
This retention period is distinct from the laboratory audit trail and the 10-year controlled-record retention requirement.
Logs associated with security incidents, data-integrity incidents, serious operational failures, validation evidence, or other controlled investigations shall be preserved as incident evidence for the applicable longer retention period, with **10 years as the current minimum where such evidence forms part of the controlled laboratory record**, unless a longer hold applies.
Routine technical logs shall be rotated in a way that does not exhaust the LIMS host's storage.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q956. Is centralized monitoring intentionally out of scope?

**Reconciled Answer:** Yes. Centralized enterprise monitoring is intentionally out of scope for v1.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q957. What is the minimal operator dashboard needed for v1?

**Reconciled Answer:** Minimal v1 administrator dashboard: service/health status; DB health; disk; document storage; last successful/validated backup; backup age; failed jobs/PDFs; certificate status; application/schema version; maintenance/recovery warnings.

---

# 34. Error Handling and User-Facing Failure Rules

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q958. What errors must be shown to users as friendly messages?

**Reconciled Answer:** Friendly messages required for validation failures, business-rule failures, authorization/SoD blocks, workflow errors, duplicate identifiers, stale data, concurrency conflicts, storage failures, report failures, unavailable service, and interrupted operations.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q959. Which technical details must never be shown?

**Reconciled Answer:** Never expose raw stack traces, SQL statements, internal exception details, secrets, tokens, server filesystem paths, or sensitive debugging information to normal users.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q960. How are database constraint errors translated into useful user messages?

**Reconciled Answer:** Database constraint errors shall be translated into domain-specific messages such as “Sample ID already exists” or “This action cannot be completed because the referenced record is no longer available.” Technical error details are logged internally.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q961. How are authorization failures shown?

**Reconciled Answer:** Show a generic authorization message: “You are not authorized to perform this action.” Do not disclose unnecessary permission structure or protected information.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q962. How are SoD blocks shown?

**Reconciled Answer:** Show that the action is blocked by role-separation/SoD policy, identify the affected controlled record where appropriate, and tell the user what authorized role must perform the next step.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q963. How are workflow transition failures shown?

**Reconciled Answer:** Show the current workflow state and explain that the requested transition is not permitted from that state.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q964. How are concurrent-edit conflicts shown?

**Reconciled Answer:** Concurrent-edit conflict: inform the user that the record changed elsewhere, do not silently overwrite it, and require refresh/reconciliation before saving.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q965. How are stale-page/stale-data conflicts handled?

**Reconciled Answer:** Stale-page/stale-data condition: detect revision mismatch, notify the user, refresh the authoritative record, and prevent silent overwrite.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q966. What happens when a save fails after the user entered many values?

**Reconciled Answer:** Sensitive controlled drafts must not be persisted in browser localStorage/IndexedDB unless separately approved.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q967. Can drafts be recovered after a failed save?

**Reconciled Answer:** Sensitive controlled drafts must not be persisted in browser localStorage/IndexedDB unless separately approved.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q968. What happens when a PDF generation fails?

**Reconciled Answer:** PDF failure: report remains unissued; no false “Issued” state is created; technical error is logged; user may retry after correction.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q969. What happens when document storage fails?

**Reconciled Answer:** Document-storage failure: report/document operation does not complete as successful; database state must not claim that the artifact was stored when it was not.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q970. What happens when backup fails?

**Reconciled Answer:** Backup failure generates an administrator alert and remains visible until resolved. Core laboratory operation may continue only while the backup state remains within the approved RPO; migration/other risky operations must be blocked when required backup protection is unavailable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q971. What happens when the server becomes unavailable during approval?

**Reconciled Answer:** If the server becomes unavailable during approval, the client must treat the result as status unknown, not failed or successful. On reconnection the authoritative server state is checked before any retry.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q972. How does the system avoid duplicate submissions after retry?

**Reconciled Answer:** Duplicate submissions prevented through idempotency/command identifiers for critical commands plus unique business constraints and authoritative server responses.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q973. Are operations required to be idempotent in any areas?

**Reconciled Answer:** Yes. Idempotency is required particularly for Approval, Verification, Report Issue/Reissue, controlled Result Correction, critical workflow transitions, and other commands where a retry could duplicate a business event.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q974. What user-visible status appears after an interrupted operation?

**Reconciled Answer:** User-visible state after interruption: “Operation status could not be confirmed. Do not resubmit yet. Reconnect and check the record status.”

---

# 35. Search, Queues, and Usability

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q975. What are the most common searches users perform?

**Reconciled Answer:** Most common searches: Sample ID; customer; external/customer sample ID; Request ID; TestInstance ID; test; status; date range; analyst/assignee; report ID; project where applicable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q976. Which fields must be searchable for samples?

**Reconciled Answer:** Samples searchable by: internal Sample ID; external/customer sample ID; Customer; receipt date; sample/matrix classification; status; Request/Project reference; storage/location where applicable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q977. Which fields must be searchable for TestInstances?

**Reconciled Answer:** TestInstances searchable by: TI ID; Sample ID; Test Code/name; Method/MethodVersion; status; analyst/assignee; priority; due date/TAT; Customer/Request; stage.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q978. Which fields must be searchable for reports?

**Reconciled Answer:** Reports searchable by: Report ID; Sample ID; Customer; report date; report status; revision; Request/Project; report type.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q979. Which fields must be searchable for customers?

**Reconciled Answer:** Customers searchable by: Customer ID; customer name; status; external reference/contact identifier where configured.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q980. Which fields must be searchable for equipment?

**Reconciled Answer:** Equipment searchable by: Equipment ID/asset ID; equipment name; type; serial number; status; location; calibration/qualification status; next due date.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q981. Which filters are required on laboratory queues?

**Reconciled Answer:** Queue filters: status/stage; assigned/unassigned; analyst; priority; due date; overdue; test; method; customer/project; hold/rework; date range.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q982. Which queues are required by role?

**Reconciled Answer:** Role-specific queues: Analyst work queue; Reviewer queue; Verification queue; Approval queue; Unassigned/assignment queue; Administrator/operational exceptions queue.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q983. What is the default sort order of each queue?

**Reconciled Answer:** Default queue sort: priority → overdue/due-soon status → due date ascending → received/created date ascending.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q984. Can users save personal search filters?

**Reconciled Answer:** Yes. Personal saved search/filter configurations should be supported.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q985. Are shared saved filters required?

**Reconciled Answer:** Yes. Shared saved filters are useful for standard laboratory queues and should be controlled/managed rather than freely edited by everyone.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q986. Are dashboards required in v1?

**Reconciled Answer:** Full analytics dashboards are not required for v1. A minimal operational dashboard is required as defined in Q957.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q987. Which metrics must appear on dashboards?

**Reconciled Answer:** Metrics: samples received/current by status; TestInstances pending by stage; overdue/due-soon work; pending Review/Verification/Approval; failed PDF jobs; backup age/status; disk/storage warnings.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q988. Are keyboard-first workflows important for sample registration or result entry?

**Reconciled Answer:** Yes. Keyboard-first operation is important, particularly for sample registration, allocation, repetitive result entry, review queues, and navigation through controlled forms.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q989. Are barcode-scanner workflows required?

**Reconciled Answer:** Yes. Barcode-scanner workflow should be supported in v1. USB HID barcode scanners should work without requiring a special network service.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q990. Which screens must support fast repetitive data entry?

**Reconciled Answer:** Fast repetitive entry is especially important for: sample registration; barcode capture; sample allocation; TestInstance result entry; review/check workflows; label printing.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q991. Are bulk actions required?

**Reconciled Answer:** Limited bulk actions are required, but only where the action is low-risk and auditable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q992. Which bulk actions are safe and permitted?

**Reconciled Answer:** Safe bulk actions may include: bulk label printing; bulk export of already-authorized search results; limited controlled assignment of unstarted work where policy permits; non-technical queue/filter operations. Each affected record must still be traceable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q993. Which actions must always remain one-record-at-a-time?

**Reconciled Answer:** Always one-record-at-a-time: result correction; Review; Verification; Approval; report issue/reissue; controlled sample identity correction; sample rejection/conditional acceptance; other high-risk technical/state-changing actions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q994. Are accessibility requirements defined?

**Reconciled Answer:** Yes. LabNexus v1 shall adopt **WCAG 2.1 Level AA as the accessibility design target for the user interface**, proportionate to the desktop/browser-based laboratory environment.

At minimum, the implementation shall support:
* keyboard-accessible core workflows;
* visible focus state;
* meaningful labels and control names;
* readable validation/error messages;
* sufficient text/control contrast;
* non-color-only status indication;
* accessible form validation;
* logical heading/landmark structure where applicable;
* browser zoom without loss of access to core functions.

Accessibility shall be included in UI verification and UAT rather than treated solely as a documentation requirement.
This is a design/acceptance target, not a claim of formal accessibility certification.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q995. What minimum browser viewport should be supported?

**Reconciled Answer:** The supported minimum primary desktop browser viewport shall be **1280 × 720 CSS pixels**.
The application shall remain usable at smaller viewport sizes where practical, but **1280 × 720 shall be the formal baseline for layout/performance acceptance**.
Core functions shall not rely on hidden controls, horizontal scrolling for ordinary desktop workflows, or inaccessible modal content at the supported baseline viewport.
The tested browser version, operating-system scaling, and display scaling assumptions shall be recorded in UI verification evidence.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q996. Are touchscreen devices used?

**Reconciled Answer:** Touchscreen support is not required for v1 unless the laboratory has identified touchscreen hardware as an operational requirement.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q997. Are thermal label printers required?

**Reconciled Answer:** Thermal barcode label printing is recommended/expected for v1 if the laboratory will generate physical Sample labels from LabNexus. Exact printer/interface remains a deployment input.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q998. Are A4 office printers required?

**Reconciled Answer:** A4 office-printer support is required for laboratories that print reports, but physical printing must not be a dependency for electronic report issuance/storage.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q999. What physical label sizes are used?

**Reconciled Answer:** Not yet defined. The laboratory must specify the physical Sample-label size(s) based on containers, barcode type, printer, and required human-readable fields. Do not hard-code a label size into the core.

---

# 36. Barcode and Identification

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1000. What identifiers will use Code 128?

**Reconciled Answer:** Code 128 should be the primary linear barcode for business identifiers that need fast scanner entry, especially Sample ID. The exact identifier classes using Code 128 remain configurable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1001. What identifiers will use QR?

**Reconciled Answer:** QR should be available where higher payload capacity or camera-based identification is useful, primarily for Sample ID and optionally other controlled identifiers.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1002. What information should be encoded in each barcode/QR type?

**Reconciled Answer:** Barcode/QR payloads should contain opaque LIMS-controlled identifiers, normally the business ID such as SAM-00000001. They should not contain sensitive customer data, test results, passwords, or other mutable technical data.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1003. Should QR codes encode only an internal identifier or more information?

**Reconciled Answer:** Yes — QR should primarily encode the internal identifier or an opaque lookup token. It should not become a second uncontrolled data store. Additional payload is allowed only through controlled configuration.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1004. Must barcodes be printable from the LIMS?

**Reconciled Answer:** Yes. LabNexus shall support printing controlled labels directly from the application.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1005. Which label printers are supported?

**Reconciled Answer:** Printer support should use standard Windows printer mechanisms initially. The exact thermal-printer make/model is a deployment input and should be validated before go-live.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1006. What label formats are required?

**Reconciled Answer:** Label format/size must be configurable. V1 should support at least one approved Sample label format and allow future formats without code changes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1007. Can users scan a sample directly into the browser application?

**Reconciled Answer:** Yes. A USB barcode scanner operating as a keyboard/HID device should work directly in browser fields. Camera-based browser scanning is not required for v1.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1008. What happens if a barcode is duplicated?

**Reconciled Answer:** A duplicate controlled identifier must be blocked. The system shall not silently create or reuse a conflicting identifier.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1009. What happens if a barcode is damaged/unreadable?

**Reconciled Answer:** A damaged/unreadable barcode may be reprinted using the same identifier after identity verification. A replacement identifier must not be generated merely because the physical label is damaged.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1010. Are manual entry fallbacks required?

**Reconciled Answer:** Yes. Manual identifier entry is required as a fallback, with validation and appropriate confirmation/verification for high-risk actions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1011. Are barcodes used for reports/documents/equipment as well as samples?

**Reconciled Answer:** Barcodes may also be used for equipment, reports/documents, and other controlled objects, but Sample identification is the primary v1 use case. Object-specific usage remains configurable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1012. Must barcode scans enforce state/workflow validity?

**Reconciled Answer:** Yes. Scanning an identifier must not bypass business rules. The system must check that the scanned object exists, belongs to the expected object type, and is in a state where the requested action is permitted.

---

# 37. Notifications and Communication

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1013. Are in-app notifications required?

**Reconciled Answer:** Yes. **In-app notifications are required only for explicitly approved operational workflows**, not as a general replacement for authoritative state/queue information.

For v1, the notification mechanism should be limited to operationally useful events such as:
* overdue work;
* QC failures;
* pending Review/Verification/Approval;
* backup/recovery failures;
* important system/operational alerts.

Notifications shall remain subordinate to the authoritative underlying event/state.

Each notification shall have:
* Event/source reference;
* Recipient;
* Severity;
* Created time;
* Read/acknowledged state where applicable;
* Expiry;
* Deduplication behavior;
* Link to the authoritative record/event.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1014. Are email notifications required?

**Reconciled Answer:** Email notifications shall **not be required for v1**.
The application shall remain fully operational without Internet access or an SMTP service.
Where email is later approved, it shall be an asynchronous delivery channel subordinate to the authoritative LabNexus business event. Failure to deliver an email must never change the underlying laboratory workflow state.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1015. Are SMS/WhatsApp notifications required or explicitly out of scope?

**Reconciled Answer:** SMS/WhatsApp notifications are **out of scope for v1**.
They introduce external service dependencies and are not necessary for the core offline-first workflow.
A future messaging integration would require separate approval covering provider, credentials, availability, confidentiality, failure handling, auditability, and offline behavior.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1016. Which events require notifications?

**Reconciled Answer:** The v1 notification event set shall be intentionally small and controlled.

Recommended initial events:
* TestInstance approaching/ exceeding controlled due-date threshold;
* QC failure requiring attention;
* TestInstance pending Review;
* TestInstance pending Verification;
* TestInstance pending Approval;
* Backup failure or missed backup;
* Recovery/integrity failure;
* Significant system operational fault;
* Security/authorization event requiring operator attention.

Routine record changes shall not automatically generate notifications.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1017. Who receives overdue-test notifications?

**Reconciled Answer:** Overdue-test notifications shall go to the **responsible operational/coordinator role and the designated supervisory/technical role** according to the approved escalation matrix.
The performing analyst does not need to receive every escalation unless the laboratory policy identifies the analyst as an action owner.
The notification shall identify the TestInstance, due date, current state, responsible assignment, and required action without exposing unrelated confidential information.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1018. Who receives QC-failure notifications?

**Reconciled Answer:** QC-failure notifications shall go to the **designated Technical/QC responsible role**, with escalation to Quality where the configured failure is quality-significant or blocking.
The analyst who performed the affected work may receive the notification as an operational task, but notification recipients shall be governed by approved responsibility rules.
The notification must link to the authoritative QC failure/nonconformance record rather than become the primary evidence of the failure.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1019. Who receives approval-pending notifications?

**Reconciled Answer:** Approval-pending notifications shall go to the **authorized approver role/person responsible for the affected TestInstance**, subject to the approved assignment/escalation model.
Where an approval remains pending beyond a configured threshold, an escalation notification may go to the designated supervisory/Quality/Technical authority.
The notification shall not bypass SoD; an unqualified or blocked user shall not receive the action merely because they received the notification.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1020. Who receives backup-failure notifications?

**Reconciled Answer:** Backup-failure notifications shall go to the **System Administrator/Backup Operations role** and, for material or persistent failures, the designated Technical/Operations and Quality authority.

The notification shall contain:
* Backup type;
* Failure/missed-run timestamp;
* Last successful backup;
* Current recovery-point age;
* Current RPO exposure;
* Required corrective action.

No Internet-based notification channel is required for this to operate.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1021. Can notifications work without Internet?

**Reconciled Answer:** Yes. **Core in-app notifications shall work entirely without Internet connectivity.**
Notifications shall be stored locally in LabNexus and generated from authoritative internal events.

No Internet service, cloud messaging provider, or external notification gateway shall be required for:
* overdue work;
* QC failures;
* pending approvals;
* backup failures;
* operational alerts.

Email/SMS/WhatsApp remain optional future delivery channels and do not form part of the core event model.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1022. If email is required, is there an approved local SMTP server?

**Reconciled Answer:** No approved local SMTP server is required for v1 because **email notification is out of scope for the core release**.
If email is later approved, the deployment must identify an approved SMTP service that is accessible under the laboratory's actual network/offline operating model.
Email credentials shall use the protected secret-management mechanism defined in the Security Baseline.
SMTP failure shall never block or alter the authoritative laboratory workflow.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1023. Are external customer notifications sent by the LIMS or manually by staff?

**Reconciled Answer:** For v1, external customer notifications shall be **manual and controlled by laboratory staff**, except for any future explicitly approved integration.
LabNexus shall record the underlying report/communication event where such tracking is required, but it shall not assume that successful LIMS report issuance means successful customer receipt.
A future automated customer notification mechanism requires separate approval for confidentiality, recipient control, delivery evidence, failure handling, and offline behavior.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1024. Are notifications themselves controlled records?

**Reconciled Answer:** Yes, selected notifications shall be treated as **controlled operational records/evidence**, but the notification itself is not the authoritative laboratory record.
The authoritative source remains the underlying Sample, TestInstance, QC, Approval, Backup, or other business/security event.

The notification record should preserve:
* Notification/event ID;
* Source event/reference;
* Recipient;
* Creation time;
* Severity;
* Delivery/read/acknowledgement state where applicable;
* Expiry;
* Deduplication relationship.

Notification history shall be retained sufficiently to explain significant operational escalation, while routine notification records need not become a second copy of the full laboratory audit trail.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1025. What counts as nonconforming work in the laboratory?

**Reconciled Answer:** Nonconforming work means work that does not conform to approved requirements, method, procedure, equipment condition, sample condition, QC requirements, authorization, workflow, or other controlled laboratory requirements. Exact taxonomy is configurable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1026. Who can declare nonconforming work?

**Reconciled Answer:** Authorized laboratory personnel who detect or are responsible for the issue may declare nonconforming work.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1027. What events can trigger nonconforming-work handling?

**Reconciled Answer:** Triggers may include failed QC; incorrect sample identity; unsuitable sample condition; equipment failure; method/procedure deviation; unauthorized work; environmental condition failure; calculation/data error; report error; workflow breach; or other configured triggers.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1028. Does nonconforming work block specific TestInstances?

**Reconciled Answer:** Nonconforming work shall identify the specific affected records and control their disposition.
Where a nonconformance affects a TestInstance, Sample, Result, Report, EquipmentUse, or related record, the system shall explicitly link the affected record to the nonconformance.
The applicable affected record shall be placed on hold or otherwise restricted where required to prevent inappropriate continuation or approval.
The relationship between the nonconformance, affected work, investigation, disposition, corrective action, and resulting report/result impact shall remain traceable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1029. Can one issue affect multiple samples/TestInstances?

**Reconciled Answer:** Yes. One nonconformance may affect multiple Samples and/or TestInstances.
The nonconformance model shall support explicit many-to-many or otherwise appropriate affected-record relationships.
Each affected record shall remain individually identifiable so that the impact assessment can determine whether the required disposition is the same or different for each record.
A nonconformance shall not be represented as affecting an entire batch merely through an unsupported blanket flag.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1030. What statuses exist for nonconforming work?

**Reconciled Answer:** The v1 nonconformance lifecycle shall use controlled states such as:
**OPEN → UNDER_INVESTIGATION → DISPOSITION_REQUIRED → ACTION_IN_PROGRESS → CLOSED**
with appropriate alternatives such as:
- ON_HOLD;
- REJECTED/INVALIDATED where applicable;
- CANCELLED where legitimately permitted.

Exact state names may be refined in the Nonconformance / Affected Record Impact Model, but the lifecycle shall distinguish discovery, investigation, disposition, action, and closure.
A closed nonconformance shall remain historically preserved.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1031. Who investigates it?

**Reconciled Answer:** Nonconformance investigation shall be performed by an authorized competent person designated according to the issue type.
The investigator shall not approve their own controlled disposition where SoD or laboratory policy requires independent review.
For technical nonconformance, the Laboratory Technical Authority shall be involved as appropriate; Quality Authority shall be involved where QMS/nonconformance governance requires it.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1032. Who can close it?

**Reconciled Answer:** Nonconformance closure shall require an authorized Quality/Technical authority according to the nature and severity of the issue.

Closure shall confirm:
- investigation completed;
- affected records identified;
- required disposition completed;
- corrective action completed where required;
- customer/report impacts addressed where applicable;
- required evidence present;
- required independent review/approval complete.

The investigator shall not automatically have unilateral closure authority.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1033. Must customer notification be recorded?

**Reconciled Answer:** Yes. Where a nonconformance requires customer notification, the notification shall be recorded as part of the controlled nonconformance evidence.

The record shall identify, where applicable:
- affected customer;
- reason for notification;
- date/time;
- communication method/reference;
- person responsible;
- outcome/acknowledgement;
- related report or TestInstance.

Customer notification shall not itself replace technical or quality disposition.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1034. Must affected reports be identified?

**Reconciled Answer:** Yes. The system shall identify affected reports where a nonconformance may affect reportable work.
Affected Report/ReportRevision relationships shall be traceable from the nonconformance and the affected Result/TestInstance.
The impact assessment shall determine whether the report requires no action, correction, reissue, withdrawal, or another controlled disposition.
Already issued reports shall never be silently modified.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1035. Can nonconforming work require re-testing?

**Reconciled Answer:** Yes. Nonconforming work may require retesting where the approved technical/quality disposition determines that retesting is necessary.
Retesting shall create a distinct TestInstance where it represents a new execution.
The original TestInstance and its nonconformance shall remain preserved, and the new TestInstance shall reference the originating work and reason.
Retesting shall not automatically invalidate the prior result unless the authorized disposition determines that it should be treated as invalid.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1036. Can rework create a new TestInstance or modify the current one?

**Reconciled Answer:** Where rework represents a distinct new execution, it shall create a new TestInstance linked to the originating TestInstance.
Where the laboratory procedure permits correction of the current execution without creating a distinct execution occurrence, the current TestInstance may proceed through controlled rework.
The governing rule shall be explicit in the Execution Semantics Decision Table.
In both cases, the original history shall remain preserved and the reason, actor, authorization, and relationships shall be auditable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1037. Which path preserves the original history most clearly?

**Reconciled Answer:** The clearest historical-preservation path is to retain the original TestInstance and create a distinct linked TestInstance whenever a genuinely new execution occurs.
The original record shall never be overwritten.
Rework, retest, repeat, correction, or other disposition shall be explicitly classified and linked so that the complete chain of work can be reconstructed.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1038. Are CAPA records required in the LIMS?

**Reconciled Answer:** CAPA capability in v1 shall remain limited to the minimum controlled functionality required by the laboratory's approved QMS/nonconformance process.
Where an investigation requires corrective or preventive action, the LIMS shall support controlled linkage to the relevant action/evidence.
A general enterprise CAPA subsystem shall not be introduced without a separately approved requirement.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1039. Are root-cause classifications required?

**Reconciled Answer:** Yes. Root-cause classification shall be supported where required by the laboratory's approved nonconformance/CAPA process.
Root-cause categories shall be controlled configuration rather than unrestricted free text, with an explanatory narrative available where required.
The laboratory shall define the actual root-cause taxonomy; LabNexus shall not invent technical cause categories as laboratory policy.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1040. Are effectiveness checks required?

**Reconciled Answer:** Effectiveness checks shall be supported where required by the laboratory's approved corrective-action/CAPA process.

Where an effectiveness check is required, the system shall preserve:
- action being evaluated;
- effectiveness criterion;
- evaluation date/time;
- evaluator;
- evidence;
- outcome;
- follow-up/disposition.

Effectiveness checking shall not be universally mandatory unless the approved laboratory procedure requires it.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1041. What are the valid reasons for sample rejection?

**Reconciled Answer:** Sample rejection reasons should be controlled, e.g. identity issue, insufficient quantity, unsuitable condition, container/packaging problem, preservation/handling issue, leakage/damage, requested test not possible, missing required information, expired/invalid sample, customer instruction, plus controlled “Other” with justification.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1042. What are the valid reasons for TestInstance cancellation?

**Reconciled Answer:** TestInstance cancellation reasons should be controlled, e.g. customer cancellation, duplicate request, sample unavailable/invalid, method unavailable, administrative error, safety restriction, nonconformance, not required, plus justified Other.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1043. What are the valid reasons for TestInstance reopening?

**Reconciled Answer:** Reopening reasons should include result correction, workflow correction, report-impact correction, failed/invalid review/verification, approved rework, nonconformance investigation, plus controlled Other.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1044. What are the valid reasons for result correction?

**Reconciled Answer:** Result-correction reasons should be controlled, such as transcription error, calculation error, wrong parameter/unit, instrument/data-entry error, sample identity correction, method/configuration issue, approved technical correction, plus justified Other.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1045. Who may perform each action?

**Reconciled Answer:** Each action is permission-controlled: intake/sample rejection by authorized intake/technical users; cancellation by authorized operational users; reopening/correction by specifically authorized roles; approval by designated approver roles.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1046. Which actions require second-person approval?

**Reconciled Answer:** Actions requiring second-person approval shall be defined in the machine-readable Nonconformance / Affected Record Impact Model + SoD Matrix.

At minimum, independent authorization shall be required where the action:
- changes an approved technical result;
- reopens approved work;
- changes or reissues an issued report;
- overrides a configured blocking control;
- authorizes an exceptional disposition;
- otherwise falls under an approved two-person-control rule.

The exact action × role × stage requirements shall be defined in the authoritative SoD Matrix.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1047. Can cancelled records be restored?

**Reconciled Answer:** Cancelled records are not restored by deletion/undelete. A controlled new action may reopen/recreate work where policy allows, preserving cancellation history.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1048. Can rejected samples later be accepted?

**Reconciled Answer:** Yes. A rejected Sample may later be accepted only through a controlled acceptance decision with reason/evidence and retained rejection history.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1049. Can a cancelled TestInstance ever be restarted?

**Reconciled Answer:** A cancelled TestInstance may not simply resume invisibly. Where work needs to continue, policy determines whether controlled reopening is permitted or a new TestInstance is required.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1050. If work resumes after cancellation, is a new TestInstance required?

**Reconciled Answer:** Yes. Where cancellation terminated the execution and work genuinely starts again, a new TestInstance is required.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1051. Does reopening always require a reason?

**Reconciled Answer:** Yes. Reopening always requires a controlled reason and audit event.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1052. Does reopening invalidate previous review/verification/approval states?

**Reconciled Answer:** Yes. Reopening an approved TestInstance moves it out of its previous approved state and requires the affected Review/Verification/Approval path to be performed again.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1053. Does reopening create a new result revision?

**Reconciled Answer:** Reopening itself does not automatically create a ResultRevision. A technical result change creates the appropriate ResultRevision. The reopen event is separately recorded.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1054. What exactly happens to prior ApprovalSnapshots?

**Reconciled Answer:** Prior ApprovalSnapshots remain immutable historical evidence. They are not deleted or rewritten. The newly corrected state requires a new review/verification/approval and therefore a new ApprovalSnapshot.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1055. What exactly happens to existing report revisions?

**Reconciled Answer:** Existing ReportRevisions remain immutable. A correction triggers report impact assessment; if report content changes, a new ReportRevision is issued/released through the controlled process.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1056. Can approval happen again after correction?

**Reconciled Answer:** Yes. A corrected/reopened TestInstance may be approved again after required Review and Verification.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1057. What distinguishes reapproval from a first approval?

**Reconciled Answer:** Reapproval refers to a previously approved controlled record that was subsequently reopened/corrected/reworked. It must retain links to the prior approval and the reason for the new approval.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1058. Must reapproval create a distinct event type?

**Reconciled Answer:** Yes. Reapproval shall create a distinct approval-chain event classification so historical reviewers can distinguish initial approval from approval after correction/rework/reopening.

---

# 40. Retention and Archive

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1059. What records must be retained?

**Reconciled Answer:** Retain controlled laboratory records including Samples, Requests, TestInstances, Results/ResultRevisions, Review/Verification/Approval history, Reports/ReportRevisions/PDFs, audit records, QC, nonconformance/CAPA, equipment, methods, configurations, controlled documents, and relevant migration/provenance evidence.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1060. What is the retention period for samples?

**Reconciled Answer:** Physical sample retention is not automatically 10 years. Sample custody/identity records are controlled records and follow the 10-year record requirement; physical-material retention shall be defined by sample/method/customer/legal requirements.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1061. What is the retention period for results?

**Reconciled Answer:** Controlled results and ResultRevision history: 10 years minimum.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1062. What is the retention period for reports?

**Reconciled Answer:** Reports, ReportRevisions, and issued PDFs: 10 years minimum.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1063. What is the retention period for audit history?

**Reconciled Answer:** Audit history: 10 years minimum, and preferably retained for the full life of the corresponding controlled records.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1064. What is the retention period for equipment records?

**Reconciled Answer:** Equipment records: 10 years minimum or longer where required by applicable laboratory policy/regulation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1065. What is the retention period for QC records?

**Reconciled Answer:** QC records: 10 years minimum.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1066. What is the retention period for configuration history?

**Reconciled Answer:** Configuration history: 10 years minimum and must remain sufficient to reconstruct historical decisions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1067. What is the retention period for controlled documents?

**Reconciled Answer:** Controlled documents: 10 years minimum or longer where the document's governing policy requires it.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1068. Can records be archived without being deleted?

**Reconciled Answer:** Yes. Records shall be capable of being **archived without being deleted**.

For LabNexus, Archive shall be a controlled retention state rather than a synonym for destruction. Archiving shall preserve:
* The complete controlled record/history;
* ReportRevisions and exact issued PDFs;
* Audit/history;
* Relevant configuration and provenance;
* Document/attachment relationships;
* Integrity hashes where applicable;
* Retention metadata and archive status.

Archived records shall remain retrievable according to authorized access, but they shall not participate in ordinary active laboratory workflows.
Archiving shall therefore be logically distinct from:
**Active → Archived → Eligible for Destruction → Destroyed**

Destruction shall occur only through the separately controlled retention/destruction process.
PDF/A remains a separate technical decision and is not required merely because records are archived.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1069. What does “Archive” mean operationally?

**Reconciled Answer:** For LabNexus, **Archive** shall mean a controlled state in which a record is retained for historical/reference purposes after it is no longer part of ordinary active operational processing.

An archived record shall:
* Remain preserved and retrievable;
* Retain its original identity and historical relationships;
* Remain integrity-verifiable;
* Preserve audit and revision history;
* Retain the exact issued artifacts required for reconstruction;
* Be excluded from ordinary active queues/workflows;
* Be protected from ordinary editing.

Archiving shall not mean moving data to an uncontrolled folder or simply marking a database row inactive.
Archive status shall be recorded explicitly and, where practical, effective-dated.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1070. Are archived records still searchable?

**Reconciled Answer:** Yes. Archived records shall remain **searchable by authorized users**, subject to archive-specific access controls and system capability.

Archived search should support the key historical identifiers required for retrieval, such as:
* Sample ID;
* Customer;
* Project/Contract;
* Request;
* TestInstance;
* Report number/revision;
* Date/time;
* Document/report identifiers;
* Other approved historical reference fields.

Search results shall clearly distinguish archived records from active records.
Archived records shall not automatically appear in normal operational queues or worklists unless an explicitly authorized historical view is being used.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1071. Are archived records read-only?

**Reconciled Answer:** Yes. Archived controlled records shall be **read-only under normal application operation**.
Ordinary users shall not edit, delete, approve, recalculate, reissue, or otherwise alter archived records.
Where a genuine historical correction, legal requirement, recovery operation, or other exceptional action is necessary, it shall use a separately authorized controlled process that preserves the original archived state and records the reason, authority, actor, timestamp, and resulting action.
Archive status must therefore protect historical evidence while still allowing controlled administrative/recovery procedures where legitimately required.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1072. Can archived records be restored to active use?

**Reconciled Answer:** Archived records shall **not normally be restored to ordinary active use**.

The preferred v1 rule is:
**Archive is a retention state, not a workflow state.**

If an archived record must be used as the basis for new laboratory work, the preferred approach is to create a new active record/workflow linked to the historical archived record.
A controlled archive restoration/reopening mechanism may exist for exceptional administrative or recovery purposes, but it shall not silently convert historical data back into an active record or alter its historical meaning.
Where restoration is technically necessary, the action shall preserve the archived copy and create a full audit trail.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1073. Who can authorize restoration from archive?

**Reconciled Answer:** Restoration from archive shall require authorization by a **designated Laboratory Quality/Records Authority or Technical Authority**, depending on the reason for restoration.

Recommended control:
* Quality/Records Authority: archive/retention/records decisions;
* Technical Authority: technical recovery or investigation where technical interpretation is involved;
* System Administrator: performs the technical restoration operation;
* Independent verification: required where restoration affects controlled technical records or recovery integrity.

The person technically executing the restoration should not automatically be the person approving the underlying laboratory decision.
Restoration shall require a structured reason, affected records, authorization, execution evidence, and verification where applicable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1074. Are archival actions audited?

**Reconciled Answer:** Yes. **All material archival actions shall be audited.**

At minimum the audit history shall cover:
* Record/archive object;
* Action type;
* Previous state;
* New state;
* Actor;
* Date/time;
* Reason;
* Authorization;
* Restoration event where applicable;
* Relevant evidence/reference;
* Resulting disposition.

The following should be auditable where they occur:
**Archive, archive reversal/restoration, retention-hold placement/removal, exceptional correction, destruction authorization, and destruction.**

Routine read/search access to archived records does not necessarily require a separate audit event for every ordinary view, but access to particularly sensitive archived material may be audited according to the approved access/audit policy.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1075. Are archived PDFs stored in the same storage hierarchy?

**Reconciled Answer:** Archived PDFs should remain in the **same application-controlled storage architecture and logical document-management model**, while being distinguishable through archive/retention metadata.
They should not be moved into an uncontrolled external filesystem hierarchy merely because they are old.
The exact issued PDF shall remain linked to its immutable ReportRevision and retain its SHA-256 hash and document/artifact identity.

Physical storage can later be separated into an archive tier, removable/offline medium, or other controlled storage arrangement, but any such migration must preserve:
* Exact PDF bytes;
* Hash;
* ReportRevision relationship;
* DocumentVersion relationship where applicable;
* Retention metadata;
* Retrieval capability;
* Backup/recovery coverage;
* Access controls.

Thus, the logical document model remains consistent even if the physical storage tier changes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1076. Are cold/offline archives required?

**Reconciled Answer:** Cold/offline archives should be **supported as an approved operational option but not made mandatory for every archived record in v1**.

The v1 baseline should distinguish:

**Online controlled archive:**
Retained within the normal application-controlled storage/retrieval environment.

**Offline/cold archive:**
Retained on controlled removable/offline media or another approved archival storage tier for records where long-term retention, storage resilience, capacity, or risk policy justifies it.
The laboratory shall decide which record classes require cold/offline archival through the Retention / Archive Matrix.

Where cold/offline archival is used, it must have:
* Controlled media identification;
* Defined retention period;
* Appropriate confidentiality/access protection;
* Integrity verification;
* Backup/redundancy strategy;
* Controlled custody;
* Retrieval procedure;
* Periodic readability/restorability verification;
* Documented destruction/disposition at end of retention.

Cold archive shall not become a second uncontrolled record system. The LIMS shall retain the authoritative metadata and location/reference needed to establish where the archived artifact belongs and how it can be retrieved.
PDF/A is **not automatically required** as a consequence of choosing cold/offline archival; that remains a separate controlled report-archival decision.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1077. What is the approved destruction process after retention expires?

**Reconciled Answer:** After retention expiry and absent legal/customer hold, destruction requires an approved retention check, authorized decision, controlled deletion/destruction, and destruction record.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1078. Who authorizes destruction?

**Reconciled Answer:** Destruction authorized by the designated laboratory management/quality authority, with technical execution by the authorized administrator.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1079. What destruction evidence is required?

**Reconciled Answer:** Evidence: record/category; retention rule; expiry date; hold check; authorization; destruction date/time; operator; scope/count; storage/archive location; resulting destruction certificate/event.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1080. Are legal holds or customer holds required?

**Reconciled Answer:** Legal/customer holds should be supported as a generic mechanism, but exact legal-hold policy is a laboratory owner decision.

---

# 41. Data Import and Migration

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1081. Which spreadsheets or existing databases contain source records?

**Reconciled Answer:** Legacy source discovery shall identify all potentially relevant spreadsheets, databases, paper registers, scanned records, exported reports, and other historical sources before migration decisions are finalized.

For each source, the Migration Assessment shall record, where applicable:
- source type;
- location;
- owner/custodian;
- date/period covered;
- record category;
- apparent completeness;
- provenance/reliability;
- format;
- estimated volume;
- accessibility;
- migration suitability;
- assessment result.

Only discovered and assessed sources may become candidates for controlled migration.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1082. Which data sets are candidates for migration?

**Reconciled Answer:** Candidate migration datasets shall be determined from the documented legacy discovery and Migration Assessment.
Candidates may include historical Samples, Requests, TestInstances, Results, reports/PDFs, customer/project references, equipment records, or other records where migration provides approved operational, traceability, quality, contractual, legal, or historical value.
A dataset shall not become a migration candidate merely because it exists.
Each candidate dataset shall have an explicit migration decision: migrate, retain outside LIMS, or reject as unsuitable/unneeded.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1083. Who owns the source data?

**Reconciled Answer:** Source-data ownership shall remain with the laboratory or other organization that legitimately controls the original records.
The Migration Assessment shall identify the source owner/custodian for each migration dataset.
Source ownership does not transfer to the migration executor merely because the data is imported into LabNexus.
Where ownership or authority is unclear, the dataset shall not be treated as approved for migration until the issue is resolved

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1084. Which source fields map to LIMS fields?

**Reconciled Answer:** Source-to-LIMS mapping shall be defined through a controlled migration mapping specification.

For each migrated field, the mapping shall identify, where applicable:
- source field;
- source meaning;
- target entity/field;
- target meaning;
- transformation;
- unit conversion;
- controlled-value mapping;
- default handling;
- missing-value handling;
- validation rule;
- exception handling.

Where a source field cannot be mapped without unsupported interpretation, the mapping shall be rejected or explicitly classified as requiring authorized transformation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1085. Which source values are ambiguous?

**Reconciled Answer:** Ambiguous source values shall be explicitly identified during migration assessment and shall not be silently interpreted.

Examples include:
- unclear dates;
- ambiguous Sample IDs;
- unclear units;
- inconsistent terminology;
- illegible/incomplete values;
- conflicting source records;
- uncertain technical meaning.

The migration record shall preserve the original source value and ambiguity status.
An ambiguous value may be migrated only where an authorized assessment establishes a controlled interpretation; otherwise it shall remain outside LIMS or be recorded with the approved uncertainty/provenance representation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1086. How are duplicate historical records detected?

**Reconciled Answer:** Duplicate historical records shall be identified using controlled matching/reconciliation rules appropriate to the source.

Matching may consider, where applicable:
- source identifier;
- date/period;
- customer/project;
- Sample identity;
- TestInstance/test;
- report number;
- source file/record location;
- other reliable provenance attributes.

Potential duplicates shall be flagged for assessment rather than automatically merged.
Where duplicates are intentionally retained because they are distinct source records, their separate provenance shall be preserved.
No migration process shall silently collapse historical records into a single record without evidence and authorization.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1087. How are missing historical values represented?

**Reconciled Answer:** Missing historical values shall be represented as genuinely missing/unknown rather than fabricated.

The migration process shall preserve the distinction between:
- unknown/not recorded;
- not applicable;
- not performed;
- not detected;
- blank/empty source value;
- value genuinely unavailable.

A missing value shall not be replaced with zero, a guessed value, or a fabricated date merely to satisfy a required LIMS field.
Where a mandatory LIMS field has no valid historical source value, the migration specification shall define an approved historical representation or classify the record as unsuitable for migration.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1088. How are source documents migrated?

**Reconciled Answer:** Source documents shall be migrated only through the controlled migration procedure. Each migrated source document must retain its original bytes where practicable, original filename and source reference, document date/version where known, source record linkage, migration batch/reference, and SHA-256 hash of the imported file.
Migrated documents shall be stored as immutable historical document/attachment records. If a document requires interpretation, conversion, OCR, renaming, or other transformation, the original source artifact must remain preserved and the transformation must be recorded.
No migrated document shall silently become an active controlled document merely because it was imported. Its status and intended use must be explicitly established through the migration assessment and document-control rules.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1089. How are historical report PDFs linked?

**Reconciled Answer:** Historical report PDFs shall be migrated as exact historical artifacts, not regenerated from current LIMS data. Each imported PDF shall retain its original bytes, SHA-256 hash, original report number/revision where available, issue date/time where available, source reference, migration batch/reference, and linkage to the corresponding historical customer/sample/report record.
Where the historical source structure does not permit creation of a complete current Report entity, the PDF may be retained as a controlled historical document linked to the migrated historical record. The imported PDF must remain distinguishable from a report natively issued by LabNexus.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1090. How is provenance of migrated data recorded?

**Reconciled Answer:** Every migrated record shall carry sufficient provenance to reconstruct what was imported, from where, when, by whom, and how it was transformed.
At minimum the migration provenance shall include: original source system/file/document; original source record identifier; source date/time or period and its precision; LIMS migration timestamp; migration executor; migration batch/reference; migration tool/procedure version; source-to-target mapping; transformations and controlled interpretations; original source value where transformed; verification status; verifier; approval/evidence reference; exceptions/ambiguities; and migration disposition.
Migration provenance is historical evidence and must not be overwritten by later normal record editing.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1091. Is migrated data treated as historical technical records or as newly entered LIMS records?

**Reconciled Answer:** Migrated data shall be treated as **historical technical records or historical supporting records**, not as newly performed LIMS work.
The system shall distinguish the original laboratory event date/time and source provenance from the date/time on which the information was entered into LabNexus. A migrated historical result must not imply that the laboratory performed that historical test using LabNexus.
Historical imported data shall be read-only by default and governed by the Migration Provenance Contract.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1092. Can historical imported data enter current workflows?

**Reconciled Answer:** Historical imported data shall **not automatically enter current operational workflows**.
Imported records may be searched, reviewed, reported as historical information, and referenced for traceability. They must not automatically become current TestInstances, current work queues, current approvals, or active technical records.
A controlled exceptional process may create a new current LIMS workflow when there is a legitimate business or technical need. In that case the new activity must be explicitly identified as a new LIMS event and must retain the historical source relationship.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1093. Are migrated records editable?

**Reconciled Answer:** Migrated records shall be **read-only by default**.

Direct editing of imported historical technical content shall not be permitted through ordinary operational screens. If a historical record contains an identified error or requires an approved correction, the original migrated representation must remain preserved and a controlled historical correction mechanism shall record the reason, authority, evidence, changed representation, actor, timestamp, and verification.

No correction may silently convert historical information into a new unqualified LIMS record.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1094. Who validates migrated data?

**Reconciled Answer:** Migrated data shall be validated by an **independent verifier** who did not perform the migration execution for the records being verified.
Validation shall involve the appropriate combination of Migration Assessor, Technical Authority, Quality/Business Authority, and Independent Verifier according to the Migration Authority Matrix. The verifier shall confirm completeness, field mapping, critical identity/provenance, transformation correctness, document integrity, exceptions, and reconciliation evidence.
Final migration acceptance shall be recorded separately from migration execution.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1095. What sample size is used for migration verification?

**Reconciled Answer:** Migration verification shall use a **risk-based verification strategy**, not an arbitrary universal percentage.
At minimum, migration verification shall include 100% reconciliation of source-to-target record/control totals and verification of all critical identity and provenance controls. Individual record-content verification shall use a documented stratified sample covering representative record types, source qualities, transformations, boundary cases, ambiguities, missing values, and high-risk records.
Where the migration population is small enough, 100% record-level verification may be required. The final sample size and selection method shall be defined in the approved Migration Verification Plan before migration execution.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1096. What reconciliation report proves migration completeness?

**Reconciled Answer:** The migration reconciliation report shall demonstrate, at minimum:
- source population and source control totals;
- records assessed as eligible;
- records migrated;
- records excluded, rejected, or retained outside LIMS;
- duplicate candidates and their dispositions;
- missing/ambiguous records or fields;
- migrated documents and attachment counts;
- document/file integrity checks and hashes where applicable;
- source-to-target reconciliation results;
- critical-field verification results;
- exceptions and corrective actions;
- final migration disposition and acceptance.

The report must provide enough evidence to demonstrate both completeness and controlled treatment of records that were not migrated.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1097. What is the rollback plan for a failed migration?

**Reconciled Answer:** A failed migration shall not leave an uncontrolled partial live state.
Before migration, the controlled database and document/attachment stores shall have a verified recovery point. Migration shall execute as a controlled batch with identifiable migration references. If migration fails, the migration shall be stopped, the failure preserved as evidence, and the environment restored to the pre-migration baseline using the approved recovery procedure where necessary.
The failed migration's logs, evidence, source data, attempted mappings, exceptions, and disposition must be retained. A subsequent attempt shall use a new controlled migration batch/version and shall not silently continue from an unknown partial state.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1098. Is migration a one-time activity or an ongoing import feature?

**Reconciled Answer:** Migration is a **controlled one-time v1 activity**, not a generic ongoing spreadsheet/import feature.
Any additional historical migration after the initial migration shall be treated as a new controlled migration activity with its own source assessment, mapping, batch identification, verification, acceptance, and evidence.
Generic post-go-live CSV/Excel-to-database import is not part of v1 unless separately approved as a controlled capability.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1099. Are CSV/Excel imports required after go-live?

**Reconciled Answer:** Imports are controlled by explicit approved types; no generic spreadsheet-to-database bypass.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Import Control / Migration Provenance Contract

### Q1100. If imports are allowed, which import types are controlled and validated?

**Reconciled Answer:** Imports are controlled by explicit approved types; no generic spreadsheet-to-database bypass.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Import Control / Migration Provenance Contract

### Q1101. Which fields are mandatory at each workflow stage?

**Reconciled Answer:** Mandatory fields are stage-specific, not universally mandatory. Intake, allocation, execution, Review, Verification, Approval, and Report Issue each enforce their own required-field set.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1102. Which values have controlled vocabularies?

**Reconciled Answer:** Controlled vocabularies include statuses, roles, matrix/sample types, test codes, units, methods, result qualifiers, reasons, locations, equipment states, QC classifications, rejection/cancellation/correction reasons, etc.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1103. Which fields require uniqueness?

**Reconciled Answer:** Uniqueness is required for identifiers that are defined as globally unique, including Customer ID, Sample ID, TestInstance ID, Report ID, Test Code, Method ID/Version identifiers, Parameter IDs, and configured external identifiers.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1104. Which fields require normalization?

**Reconciled Answer:** Normalization applies to controlled identifiers, whitespace, structured codes, unit representation, and master-data references. Free-text narrative should not be over-normalized.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1105. How are spelling/abbreviation variations handled?

**Reconciled Answer:** Variations are handled through controlled aliases/codes, not by silently changing source meaning.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1106. Are master-data values case-sensitive?

**Reconciled Answer:** Controlled codes/identifiers are generally case-insensitive for uniqueness/search where appropriate, while stored canonical representation is controlled. Free text retains entered case.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1107. Are leading/trailing spaces normalized?

**Reconciled Answer:** Leading/trailing whitespace is normalized/removed for structured text fields. Meaningful internal spaces are retained.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1108. Are Unicode and multilingual values required?

**Reconciled Answer:** Yes. Unicode must be supported.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1109. Is local-language data required?

**Reconciled Answer:** Local-language UI/data entry is not required for v1, but Unicode capability must allow local-language names/text when legitimately needed.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1110. Are decimals stored consistently using a defined numeric representation?

**Reconciled Answer:** Numeric laboratory values shall use a defined database numeric representation such as fixed-precision decimal where exact decimal semantics matter; floating-point must not be used casually for controlled laboratory calculations.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1111. Are dates stored consistently?

**Reconciled Answer:** Dates use ISO-style database representations and controlled application serialization.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1112. Are times stored consistently?

**Reconciled Answer:** Times use timezone-aware date/time handling at application boundaries and UTC internally.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1113. What timestamp standard is used internally?

**Reconciled Answer:** Internal timestamp standard: UTC.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1114. How are missing values represented?

**Reconciled Answer:** Missing value = structured NULL/unknown, not an arbitrary text value such as -, NA, or 0.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1115. How are “not applicable”, “not detected”, “below LOQ”, and “not performed” distinguished?

**Reconciled Answer:** Not Applicable, Not Detected, Below LOQ, and Not Performed must be separate structured states/qualifiers, never inferred from free text alone.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1116. Which fields allow free text?

**Reconciled Answer:** Free text allowed for controlled notes/comments, sample observations, investigation narratives, reasons/justifications, report comments, and other explicitly designated narrative fields.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1117. Where is free text prohibited?

**Reconciled Answer:** Free text prohibited where machine-readable controlled values are required: identifiers, statuses, units, workflow states, approval identity, method/version, QC disposition, and similar structured fields.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1118. How are invalid master-data references handled?

**Reconciled Answer:** Invalid master-data references must be rejected at validation/database levels. Historical references remain valid through versioned/master-history mechanisms.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1119. What data-quality checks run before approval?

**Reconciled Answer:** Before Approval: completeness, required parameters, validity/units, calculation status, method/version, QC requirements, authorization/SoD, workflow state, unresolved holds/nonconformance, and data consistency.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1120. What data-quality checks run before report issue?

**Reconciled Answer:** Before Report Issue: approved result state, exact approved ResultRevision/ApprovalSnapshot, report completeness, correct customer/sample/report identifiers, method/accreditation representation, document-generation success, artifact hash/storage, and no blocking report-impact issue.

---

# 43. API and Internal Service Boundaries

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1121. What are the major domain modules inside the modular monolith?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1122. What responsibilities belong to each module?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1123. What module dependencies are permitted?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1124. Which modules may access which repositories?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1125. Are direct cross-module database writes prohibited?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1126. What is the authoritative application write path for controlled records?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1127. Which business rules must live in domain services rather than routers/UI?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1128. Which operations must be atomic across multiple entities?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1129. Which operations need explicit transactional boundaries?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1130. Which operations require optimistic concurrency control?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1131. Which APIs are internal-only?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1132. Is a public API explicitly prohibited in v1?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1133. Are browser APIs versioned?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1134. What error format will the backend expose?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1135. What validation error format is required?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1136. How are authorization errors represented?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1137. How are state-transition errors represented?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1138. How are concurrency conflicts represented?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1139. Which API responses must never expose sensitive fields?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1140. What pagination rules are required?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1141. What filtering/sorting semantics are required?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1142. What maximum page sizes are permitted?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1143. Is API request id/correlation id required?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1144. Are audit event IDs returned to clients where useful?

**Reconciled Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1145. What are the mandatory v1 screens?

**Reconciled Answer:** Mandatory v1 screens: Login; Home/Dashboard; Customer; Request; Sample Registration/Intake; Sample Detail; Test Queue; TestInstance Detail; Result Entry; Review Queue; Verification Queue; Approval Queue; Result/History; Report List/Detail; Report Preview/Issue/Reissue; Equipment; Methods/Test Definitions; QC/Nonconformance; Configuration; Audit/History; Administration/Operational Health.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1146. What are the mandatory screens for each role?

**Reconciled Answer:** Each role gets only the screens/actions appropriate to its permissions. Analyst: intake/assigned work/result entry; Reviewer: review; Verification: verification; Approver: approval; Quality/Technical: quality/configuration oversight; Admin: technical administration without technical approval authority.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1147. What is the primary navigation structure?

**Reconciled Answer:** Primary navigation should be organized around Work, Records, Reports, Quality, Master Data, Administration, with role-based visibility.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1148. Which screens are task-oriented queues versus master-data screens?

**Reconciled Answer:** Queues: Sample/Intake, Assignment, Analyst Work, Review, Verification, Approval, Exceptions/Nonconformance, Operational Alerts. Master-data screens: Customer, Equipment, Methods, TestDefinitions, Parameters, Configuration.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1149. Which screens require split view/detail panels?

**Reconciled Answer:** Yes. Queue/detail pages should support split-view or fast drill-down where it materially improves repetitive operational work.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1150. Which forms require autosave?

**Reconciled Answer:** Sensitive controlled drafts must not be persisted in browser localStorage/IndexedDB unless separately approved.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1151. Which forms must use explicit Save?

**Reconciled Answer:** Controlled forms shall use explicit Save, Submit, or equivalent authoritative actions.
Result entry, configuration changes, corrections, Review, Verification, Approval, report issue/reissue, and other controlled actions shall not depend on implicit browser autosave as the authoritative write mechanism.
Where drafts are permitted, the explicit Save action creates the draft state; Submit or the applicable workflow action advances the record. Browser-side transient data must not be treated as authoritative laboratory evidence.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1152. Which forms can be left as drafts?

**Reconciled Answer:** Drafts allowed for appropriate non-final forms, configuration proposals, report drafts, and other explicitly draft-capable entities. Controlled technical approval states are never “draft.”

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1153. Which workflows require confirmation dialogs?

**Reconciled Answer:** Confirmation required for state-changing operations, assignment changes where consequential, rejection, cancellation, reopening, report issue/reissue, approval, and other configured high-risk actions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1154. Which destructive or irreversible actions require strong confirmation?

**Reconciled Answer:** Destructive/irreversible operations such as permanent deletion where exceptionally permitted, retention destruction, database restore, and similar operations require strong confirmation and authorization.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1155. Which high-risk actions require showing the exact record/stage before confirmation?

**Reconciled Answer:** Yes. High-risk confirmation should display the exact record identity, current state, intended action, and material consequence before confirmation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1156. How are workflow states visually represented?

**Reconciled Answer:** Workflow states should be visually represented with consistent controlled status labels, badges, and state history; color must not be the only indicator.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1157. How are SoD blocks displayed?

**Reconciled Answer:** SoD blocks should clearly say that the requested action is blocked by role separation and identify the next authorized stage/role where appropriate.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1158. How are validation errors displayed?

**Reconciled Answer:** Validation errors appear inline at field level plus a clear summary for multi-error forms.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1159. How are required fields indicated?

**Reconciled Answer:** Required fields indicated consistently with label markers and accessible explanatory text.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1160. How are audit/history views presented?

**Reconciled Answer:** Audit/history presented as a chronological, immutable event/revision view with actor, timestamp, reason, event type, and related evidence.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1161. How are revision comparisons displayed?

**Reconciled Answer:** Revision comparison should show what changed, old value, new value, actor, timestamp, reason, and revision/event linkage.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1162. Must users be able to compare current Result versus historical ResultRevision?

**Reconciled Answer:** Yes. Users with permission must be able to compare current Result state with historical ResultRevision.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1163. Must users be able to compare ReportRevision versions?

**Reconciled Answer:** Yes. Authorized users must be able to compare ReportRevision versions, including issue/reissue history.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1164. How are documents/PDFs previewed?

**Reconciled Answer:** Documents/PDFs should support in-browser preview where feasible, with controlled download/print access according to permissions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1165. Must users be able to print labels directly from workflow screens?

**Reconciled Answer:** Yes. Users should be able to print labels directly from applicable workflow screens.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1166. Which screens must support barcode scanners without mouse use?

**Reconciled Answer:** Sample intake/registration and repetitive identification workflows must support scanner entry without requiring mouse interaction.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1167. Which screens must be optimized for data-entry speed?

**Reconciled Answer:** Optimize for speed: Sample Intake, Sample Allocation, Analyst Result Entry, Review, Verification, Approval, and Label Printing.

---

# 45. Report Rendering and Browser/Chromium Stability

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1168. Which Chromium version is approved for production PDF rendering?

**Reconciled Answer:** The production PDF-rendering environment shall use a controlled, validated Chromium version recorded in the Report Rendering / PDF Validation Baseline.

The approved Chromium version shall be selected based on the version that has successfully passed the laboratory's report-rendering validation suite. The baseline shall record at minimum:
- Chromium product/version/build;
- installation/package source;
- operating environment;
- rendering configuration relevant to reproducibility;
- validation date and evidence;
- approved status;
- replacement/rollback version where applicable.

Chromium shall not be updated automatically in production without controlled assessment. An update shall require rendering regression testing using representative report templates and difficult cases, including page breaks, tables, long results, Unicode content, headers/footers, report revisions, attachments where applicable, and final PDF integrity/hash behavior.
The approved production Chromium version shall therefore be treated as a controlled deployment dependency rather than an incidental browser installation. Historical issued PDFs remain authoritative regardless of later Chromium changes; a renderer update must never regenerate or replace previously issued report artifacts.
The Report Rendering / PDF Validation Baseline shall also define the controlled procedure for approving, deploying, validating, and, where necessary, rolling back Chromium updates.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1169. How is Chromium installed and updated?

**Reconciled Answer:** Chromium shall be installed as a controlled production dependency on the designated rendering environment.
The approved Chromium version shall be recorded in the deployment/rendering baseline, installed from a controlled package or approved distribution method, and operated without requiring Internet access during normal report generation.
Chromium updates shall be treated as controlled maintenance changes. The previous approved version and rollback/recovery path shall remain known until the updated version has passed the required rendering verification.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1170. How is PDF rendering tested after a Chromium update?

**Reconciled Answer:** After every approved Chromium update, the system shall execute a controlled PDF rendering regression suite using representative approved report templates and difficult cases.
Testing shall cover, at minimum: page count, page breaks, headers/footers, fonts, tables, long values, abnormal results, attachments, special characters, report revision identifiers, hashes, and overall technical/report content.
A renderer update shall not become production-effective until required regression results are reviewed and accepted. Material rendering changes shall be treated as a release/validation issue rather than silently accepted because the PDF still opens.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1171. Must fonts be bundled locally for offline stability?

**Reconciled Answer:** Yes. Approved report fonts shall be **bundled locally and controlled** for production PDF rendering.
This avoids dependence on Internet availability or uncontrolled host-font substitution and improves rendering reproducibility. The exact font package, version, licensing basis, and supported scripts shall be recorded in the Report Rendering / PDF Validation Baseline.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1172. Which fonts are approved for reports?

**Reconciled Answer:** v1 shall use a **small controlled font set**, with one approved primary report family and only the additional script-specific fonts actually required.
A practical recommended baseline is the **Noto Sans family**, supplemented by the required Noto script variant(s) where non-Latin report content is actually needed. The final approved font names and versions shall be frozen in the Report Rendering / PDF Validation Baseline.
The renderer must not silently substitute arbitrary host fonts for controlled report rendering.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1173. Are non-Latin scripts required?

**Reconciled Answer:** The application and report pipeline shall support Unicode, and non-Latin scripts shall be rendered correctly when such data is legitimately required.
The v1 validation baseline shall therefore include representative Unicode/non-Latin test data at least for stored names, metadata, and any approved report-visible fields. If a specific non-Latin script is required in issued reports, an approved locally bundled font supporting that script shall be included and validated.
The system shall not claim broad script coverage that has not been tested.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1174. How are page breaks controlled?

**Reconciled Answer:** Page breaks shall be controlled through the approved report template/CSS rules and validated against representative report data.
Section headings should remain with their associated content where practicable. Tables and structured result blocks must have controlled page-break behavior. Important sections shall not be split unpredictably, and blank/near-empty pages caused by rendering rules shall be treated as defects.
Long reports must be tested explicitly rather than relying on the renderer's default pagination.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1175. How are tables split across pages?

**Reconciled Answer:** Tables shall use controlled paginated-report behavior.
Table headers shall repeat on continuation pages. Rows should remain together where practicable, while genuinely large content may continue across pages under controlled rendering rules. Columns must not be clipped or silently omitted.
Long-text result cells, notes, and comments shall wrap or continue predictably, and the resulting PDF shall remain readable and reconstructable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1176. How are headers/footers handled?

**Reconciled Answer:** Headers and footers shall be defined by the controlled report template and applied consistently to every applicable page.
They shall support the approved report identity and page-control requirements, including the report number/revision and page numbering where required. Any issue/revision/status representation shall follow the Report Lifecycle and Composition rules.
Headers and footers must not depend on uncontrolled host configuration or manually inserted text.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1177. How are long results handled?

**Reconciled Answer:** Long results shall never be truncated or silently replaced because they do not fit the expected layout.
The report template shall provide controlled wrapping, continuation, row expansion, or page continuation. Long values and narratives shall be tested using realistic boundary cases.
Where a value cannot be rendered safely within the approved layout, report generation shall fail visibly and controllably rather than issuing an incomplete or misleading PDF.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1178. How are abnormal values displayed?

**Reconciled Answer:** Abnormal values shall preserve the **actual result value and its structured qualifier/status**, with any report flagging applied according to the approved reporting rules.
Visual emphasis may be used, but color alone must never be the only indication of an abnormal condition. The underlying structured value, qualifier, unit, and applicable reference/specification context remain authoritative.
The report must not invent an abnormal classification merely because a value appears unusual.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1179. How are report attachments handled in rendering?

**Reconciled Answer:** Report attachments shall be rendered or packaged only when explicitly included by the approved Report Composition rules.
When included, the exact approved DocumentVersion/file shall be used and its identity, ordering, and integrity shall remain frozen with the ReportRevision. Attachments shall not be silently converted, altered, or replaced merely to make rendering easier.
Where an attachment is not intended to be flattened into the primary report PDF, it shall remain a separately identified report-package artifact linked to the exact issued revision.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1180. Are PDF/A or other archival PDF standards required?

**Reconciled Answer:** PDF/A is **not required for v1 unless separately approved by the laboratory**.
The v1 archival control shall instead rely on preservation of the exact issued PDF bytes, immutable ReportRevision linkage, SHA-256 hash, controlled storage/retention, and verified backup/recovery.
PDF/A or another archival PDF standard may be introduced later through a controlled architectural/report-rendering change if a documented requirement establishes the need.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1181. Must PDF metadata include author/laboratory/report number?

**Reconciled Answer:** The PDF shall contain controlled metadata appropriate to the issued report, including at minimum the laboratory identity and report number/revision where technically supported and useful.
Additional metadata such as author, title, creation timestamp, subject, or keywords may be included where approved. Metadata must not contain unnecessary sensitive information.
The authoritative report identity remains the persisted ReportRevision/report artifact relationship, not PDF metadata alone.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1182. Must a content hash be stored?

**Reconciled Answer:** Yes. The exact issued PDF bytes shall have a **SHA-256 content hash** stored with the corresponding report artifact.
The hash shall be generated from the final persisted PDF bytes and used for integrity verification, backup/restore checking, artifact identity, and evidentiary reconstruction.
Any changed PDF bytes necessarily represent a different artifact and must not overwrite the previously issued artifact.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1183. Is digital signing of PDFs required?

**Reconciled Answer:** Cryptographic digital signing of PDFs is **not required for v1** unless separately approved.
The authoritative approval evidence shall remain the controlled application-side approval chain, linked to the exact ResultRevision/ApprovalSnapshot and ReportRevision. A visible signature representation may be included in the PDF according to approved report policy, but that is distinct from cryptographic PDF signing.
Introducing cryptographic signing later would require a controlled architecture, security, key-management, validation, and operational decision.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1184. Is watermarking required for drafts or superseded reports?

**Reconciled Answer:** Watermark behavior for draft, not-issued, superseded or withdrawn report artifacts is not yet approved. The report-control authority must define the rule. The renderer must not invent it. Cryptographic PDF signing remains separately out of scope for v1.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1185. What distinguishes a draft PDF from an issued PDF?

**Reconciled Answer:** A **draft PDF** is a non-issued rendering associated with a draft or pre-issuance ReportRevision and is not an authoritative issued laboratory report.
An **issued PDF** exists only when the applicable report workflow is complete, the exact artifact has been persisted, its hash has been recorded, artifact integrity has been verified, and the issuance event has been authorized and recorded.
An issued PDF and its ReportRevision shall not be converted back into a draft or silently regenerated in place.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1186. Does the laboratory require electronic signatures in the system?

**Reconciled Answer:** Yes. LabNexus shall support controlled electronic approval/signing evidence for high-risk workflow actions, particularly Review, Technical Verification, Approval, report issuance where applicable, and other actions identified by the Authorization Matrix.

For v1, “electronic signature” shall mean a controlled electronic approval action in LabNexus that:
Occurs under an authenticated user identity;
Re-validates authorization and SoD at the transaction boundary;
Is linked to the exact TestInstance and applicable ResultRevision;
Is linked to the exact ApprovalSnapshot where approval is involved;
Records actor, role, date/time, action, reason where applicable, and applicable policy/configuration context;
Produces an immutable approval-chain event;
Cannot be silently deleted, rewritten, or reassigned to another person.

This does not by itself claim that the LabNexus approval mechanism is a legally qualified digital signature under any particular external law or regulatory framework. Any such legal designation must be separately established by the laboratory's applicable requirements

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1187. What legal/quality meaning should an electronic signature have?

**Reconciled Answer:** The electronic signature shall have the following **quality and operational meaning**:
It constitutes evidence that the identified authorized person performed the specified controlled action on the identified record at the recorded time, after the system verified the applicable authorization, competence/context, workflow state, and SoD requirements.
For Approval, the signature evidence means that the authorized approver approved the exact controlled ResultRevision/ApprovalSnapshot presented by the system.
The signature shall therefore be evidence of a controlled laboratory decision, not merely an indication that someone was logged into the application.
LabNexus shall not claim a stronger legal meaning, such as a qualified electronic signature or statutory digital-signature status, unless the laboratory has separately established that requirement and approved an implementation satisfying it.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1188. Is authenticated session identity sufficient for signature evidence?

**Reconciled Answer:** An authenticated session identity alone is **not sufficient for the highest-risk signing/approval transaction**.

The session shall establish the user's authenticated identity, but at the signing transaction the server shall additionally revalidate:
* User account status;
* Current role/permission;
* Effective authorization;
* Competence requirements where applicable;
* TestInstance context;
* Current workflow state;
* Exact ResultRevision/ApprovalSnapshot;
* Applicable SoD rule;
* Configuration/policy version;
* Any required second-person authorization.

For high-risk Approval/signing actions, v1 should also require **fresh re-authentication** immediately before the transaction, using the user's password or another separately approved authentication factor.
This provides stronger evidence that the person who initiated the approval transaction is the person whose identity is recorded in the approval event, rather than relying indefinitely on an old browser session.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1189. Is password re-entry required for signing?

**Reconciled Answer:** Yes. **Password re-entry should be required for high-risk electronic approval/signing actions in v1.**

The re-entry shall:
* Occur through a dedicated secure transaction step;
* Be validated server-side;
* Never be stored or logged;
* Re-evaluate authorization and SoD after successful authentication;
* Be bound to the exact transaction being approved;
* Expire if the approval transaction is abandoned or materially changes.

The re-authentication requirement should apply to Approval and other actions explicitly classified as requiring strong electronic approval evidence.
Routine navigation and ordinary record viewing shall not require password re-entry.
A future multi-factor authentication mechanism may be introduced through a controlled security change, but it is not required to establish the v1 decision.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1190. Is signature data stored separately from approval_chain_event?

**Reconciled Answer:** The authoritative signing/approval evidence shall remain in the **`approval_chain_event` model**, rather than creating an independent uncontrolled signature history.
A separate signature-evidence structure may be used where technically useful, but it must be directly linked to the corresponding approval-chain event and must not become a competing source of truth.

The approval event should preserve, as applicable:
* Approval event ID;
* TestInstance;
* ResultRevision;
* ApprovalSnapshot;
* Actor/user ID;
* Historical display name;
* Role at time of action;
* Action/event type;
* Timestamp;
* Authentication/re-authentication evidence class;
* Applicable authorization/SoD policy version;
* Reason where required;
* Second-person authorization/countersignature where required;
* Related ReportRevision where applicable.

The authoritative business meaning remains the immutable approval-chain event.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1191. Must the displayed signature include name, role, date, and time?

**Reconciled Answer:** Yes. The displayed electronic approval/signature representation should include, at minimum:
* Signatory's controlled name;
* Signatory's role at the time of approval;
* Approval/signing action;
* Date;
* Time;
* Report/TestInstance context where appropriate.

Where useful and approved, the display may also include the approval status and identification of the relevant report revision.
The displayed identity shall come from the **historical approval evidence**, not from the user's current mutable profile. Thus, later changes to a user's name, role, or authorization must not rewrite what was displayed or recorded for a historical approval.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1192. Must the PDF contain a visible signature representation?

**Reconciled Answer:** Yes. The issued PDF should contain a **controlled visible representation of the applicable approval/signature evidence** where the laboratory's approved report format requires it.
The visible representation should normally identify the approving person, role, and approval date/time in a controlled report section.
This visible representation is presentation evidence only. The authoritative approval remains the application-side `approval_chain_event` and linked ApprovalSnapshot/ResultRevision.
The PDF must not be treated as the sole source of approval evidence, and changing the visible representation shall never alter the underlying approval history.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1193. Is cryptographic PDF signing required?

**Reconciled Answer:** No. **Cryptographic PDF signing is not required for v1.**

The v1 integrity model shall instead use:
* Controlled authenticated approval;
* Server-side transaction revalidation;
* Immutable approval-chain events;
* Exact ResultRevision/ApprovalSnapshot linkage;
* Immutable ReportRevision;
* Persisted exact PDF artifact;
* SHA-256 hash of the final PDF bytes;
* Controlled storage and backup;
* Audit/history.

Cryptographic PDF signing may be introduced later only through an approved architecture/security change addressing certificates, private-key custody, certificate lifecycle, signing infrastructure, PDF validation, revocation, recovery, and operational procedures.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1194. Is cryptographic signing intentionally out of scope?

**Reconciled Answer:** Yes. Cryptographic PDF signing is **intentionally out of scope for v1**.

The distinction shall be explicit:
**v1 electronic approval:**
Controlled authenticated application action producing authoritative approval evidence.

**v1 PDF integrity:**
Exact persisted PDF + SHA-256 hash + ReportRevision linkage + controlled storage/backup.

**Cryptographic PDF signature:**
Not implemented in v1 and must not be implied by the visible approval/signature representation.

This prevents the application from accidentally making a legal or technical claim that its visual report signature is a cryptographic digital signature.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1195. What happens if a signatory account is later disabled?

**Reconciled Answer:** If a signatory's account is later disabled, the system shall **not retroactively erase or invalidate historical approval evidence merely because the account is now disabled**.
Historical approval remains evidence of the action performed at the time, provided that the account was authorized and valid when the action occurred.

After disablement:
* The user cannot perform new controlled approval/signing actions;
* Active sessions are invalidated;
* New authorization checks fail;
* Historical approval events remain immutable;
* Historical signer identity remains reconstructable;
* Any later investigation can assess whether the signer was valid at the time of the original action.

If a security investigation establishes that the historical approval itself may have been compromised or improperly authorized, the affected approval/result/report shall be handled through the controlled correction/reopen/nonconformance process. The original approval event must still remain preserved.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1196. How is historical signature identity preserved?

**Reconciled Answer:** Historical signature identity shall be preserved **inside the immutable approval evidence**, independently of the user's current profile.

At minimum, the historical approval record shall preserve:
* Immutable user/account identifier;
* Signer's display name as recorded at the time;
* Role applicable at the time;
* Approval/signing action;
* Date/time in UTC;
* Laboratory display timezone representation where required;
* ResultRevision/ApprovalSnapshot;
* TestInstance;
* ReportRevision where applicable;
* Authorization/SoD policy version;
* Authentication/re-authentication evidence class;
* Related audit/event identifier.

The system must not reconstruct a historical signature by looking up the user's current name or current role.
Therefore, even if the user is later renamed, reassigned, disabled, deleted from ordinary active-user lists, or otherwise changed, the historical approval shall remain independently reconstructable.
Historical signature evidence shall be retained for the applicable controlled-record retention period and preserved together with the associated result/report history.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1197. What timezone is the laboratory's official timezone?

**Reconciled Answer:** The laboratory's official display timezone shall be **Asia/Kolkata (India Standard Time, IST)**.
All instant timestamps shall be stored internally as UTC, with Asia/Kolkata used for normal user-facing and report-facing display unless a controlled view explicitly calls for another representation.
The IANA timezone identifier `Asia/Kolkata` shall be the controlled timezone configuration rather than a manually applied fixed offset.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1198. Is all server-side storage in UTC?

**Reconciled Answer:** Yes for **instant timestamps**: server-side/application timestamps shall be stored in UTC.
Date-only values, such as a contractual date or a calendar due date where the business meaning is date-only, shall remain date values rather than being converted into UTC timestamps artificially.
The system shall never store ambiguous naive date-times as though their timezone were known.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1199. What timezone is displayed to users?

**Reconciled Answer:** Normal user-facing timestamps shall be displayed in **Asia/Kolkata**.
Reports, audit/history views, workflow timestamps, and operational records should use the laboratory timezone by default, while UTC may remain available in technical/system views where useful for diagnostics and interoperability.
The displayed timezone shall be explicit where timestamp interpretation could otherwise be ambiguous.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1200. How are daylight-saving changes handled if relevant to any environment?

**Reconciled Answer:** The production laboratory environment shall use `Asia/Kolkata`, so daylight-saving transitions are not expected in the normal v1 operating environment.
The implementation shall nevertheless use timezone-aware conversion through the IANA timezone database rather than hard-coding a numerical offset. This preserves correct behavior if the deployment environment is later changed or if another timezone is formally configured.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1201. Is the Windows host time synchronized automatically?

**Reconciled Answer:** Yes. The Windows host clock shall be synchronized automatically against an **approved time source** where an operationally suitable source is available.
The synchronization method may use the organization's Windows/domain time service or an approved local/on-site time source. Internet access must not be a mandatory dependency.
The synchronization state and significant clock anomalies shall be part of operational health/evidence.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1202. Is Internet time synchronization available?

**Reconciled Answer:** Internet time synchronization shall **not be required** for LabNexus.
The system is offline-first and shall remain operational without Internet connectivity. Where Internet-based synchronization is available, it may be used as an approved time source, but the production baseline shall define a local/domain/on-site alternative.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1203. If Internet is unavailable, what time source is used?

**Reconciled Answer:** When Internet connectivity is unavailable, the Windows host shall use the approved local/domain/on-site time source defined by the deployment baseline.
If no automatic trusted source is available, an authorized administrator shall perform the controlled time-verification/time-setting procedure, with the event recorded as operational evidence.
Approval and report issuance shall not rely on an unknowable or silently drifting system clock.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1204. Who can change the Windows server clock?

**Reconciled Answer:** Only an authorized **Windows/System Administrator** shall be permitted to change the production server clock.
Laboratory users, analysts, reviewers, verifiers, approvers, and ordinary application administrators shall not have operating-system clock-change authority.
Clock changes shall be treated as privileged operational events, with the available Windows/host audit evidence retained and significant changes surfaced to the LabNexus operational monitoring process.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1205. What happens if the system clock is incorrect?

**Reconciled Answer:** If the system clock is detected as incorrect or materially outside the approved tolerance, the event shall be recorded and high-risk timestamp-dependent operations shall be blocked or placed on hold according to the Time Integrity Baseline.
The system shall not silently rewrite timestamps that were already recorded. Existing historical events remain historical; any identified timing anomaly is documented and investigated.
After correction, normal operation may resume only after the approved time-integrity check succeeds.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1206. Are time anomalies detected or logged?

**Reconciled Answer:** Yes. Time anomalies shall be detected and logged.
The operational-health mechanism should detect significant backward or forward clock changes, failed synchronization, loss of the configured time source, and clock state outside the approved tolerance where such comparison is available.
Each material anomaly shall record detection time, observed condition, affected host/environment, disposition, and corrective action where required.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1207. Is trusted time evidence required for approval/report issuance?

**Reconciled Answer:** Yes, but v1 should use **controlled host-time integrity evidence rather than a mandatory external trusted-timestamp service**.
Before Approval and Report Issuance, LabNexus shall rely on a healthy, authorized system time source and a server-side timestamp generated at the controlled transaction boundary. If the host clock/time-integrity condition is outside the approved tolerance or otherwise unresolved, the affected high-risk action shall be blocked.
The exact clock-drift tolerance and trusted-time evidence procedure shall be frozen in the Time Integrity / Operational Environment Baseline.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1208. What response time is acceptable for normal page loads?

**Reconciled Answer:** The v1 normal-page-load acceptance target shall be:
**p95 ≤ 2 seconds** for representative normal operational pages, excluding intentionally long-running operations.

The measurement environment shall define:
* Approved hardware;
* Browser/version;
* Dataset size;
* LAN conditions;
* Concurrent users;
* Authentication state;
* Whether server and network time are included.

Pages containing large reports, heavy exports, PDF rendering, large document previews, or deliberately expensive queries shall have separate acceptance criteria.
The value is a **measured acceptance target**, not a guarantee for every page or future deployment.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1209. What response time is acceptable for sample search?

**Reconciled Answer:** Sample search shall target:
**p95 ≤ 1.5 seconds** for normal indexed searches over the representative validation dataset.

Acceptance shall include:
* Common Sample ID search;
* Customer/sample identifier search;
* Date/status filtering;
* Combined filters;
* Representative historical dataset size.

Search results shall be paginated and appropriately indexed.
The acceptance test shall identify both p95 and any materially high worst-case result so that pathological queries are not hidden by averages.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1210. What response time is acceptable for result save?

**Reconciled Answer:** A normal result-save transaction, including required audit/business persistence, shall target:
**p95 ≤ 1 second** under the approved normal concurrency scenario.
The measurement shall include the authoritative backend transaction and its required audit writes, not merely frontend button-response time.
Where result saving triggers an intentionally expensive calculation or PDF/report-generation process, that work should be separated from the ordinary save transaction where architecturally appropriate.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1211. What response time is acceptable for queue loading?

**Reconciled Answer:** Operational queue loading shall target:
**p95 ≤ 2 seconds** for the normal laboratory queue dataset and approved concurrent-writer workload.

Queue acceptance testing shall include:
* Analyst queue;
* Review queue;
* Verification queue;
* Approval queue;
* Exception/nonconformance queue where applicable;
* Due-date/priority sorting;
* Pagination/filtering.

The system shall avoid loading an unnecessarily large unpaginated dataset merely to construct a queue.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1212. What report-generation time is acceptable for a typical report?

**Reconciled Answer:** A typical laboratory report shall target:
**p95 ≤ 5 seconds** from report-generation request to successfully persisted/verified PDF artifact under the approved test environment.
The timing must include the controlled PDF-generation process, not just HTML template generation.
Typical-report acceptance data shall represent the normal expected report size and content.
PDF issuance still requires artifact persistence, hashing, verification, and the appropriate authorization controls.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1213. What report-generation time is acceptable for a large report?

**Reconciled Answer:** A large report shall target:
**p95 ≤ 15 seconds** from generation request to persisted/verified PDF artifact under the approved validation environment.
“Large report” shall be defined by a representative controlled test case, such as high TestInstance/result count, multiple pages, long textual fields, tables, and approved attachments where applicable.
The threshold is an acceptance target rather than a universal promise. If the report exceeds the target, the evidence shall identify whether the constraint arises from database retrieval, application rendering, Chromium rendering, storage, or another component.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1214. What number of simultaneous writers must be supported?

**Reconciled Answer:** The v1 performance/capacity acceptance baseline shall support:
**1–3 simultaneous operational writers as the normal concurrency scenario**, consistent with the laboratory's stated operating profile.
In addition, formal testing shall include a **5-writer stress/concurrency scenario** to verify that the system behaves safely at the upper expected writer range.

The acceptance criteria shall assess:
* Successful commits;
* No duplicate identifiers;
* No lost updates;
* No transaction corruption;
* No unauthorized state changes;
* Acceptable busy/retry behavior;
* Queue/search/result-save performance;
* Audit completeness.

The 5-writer scenario is a validation/stress condition, not a claim that 5 simultaneous writers are the absolute system capacity. Any capacity beyond this shall be established by measurement.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1215. What number of read-only users must be supported?

**Reconciled Answer:** The performance acceptance baseline shall support **7 simultaneous read-only users in addition to the normal 1–3 simultaneous writers**, giving a normal mixed-workload target of up to approximately **10 active browser users**.
A separate read-heavy test may exercise **10 simultaneous read-only users** to confirm that ordinary searching, dashboards, queues, record viewing, and report retrieval remain usable without writer starvation.
These figures are **validated workload targets, not an absolute system capacity guarantee**. The acceptance record shall identify the tested concurrency, dataset size, hardware, software versions, and observed latency/error results.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1216. What sample count must the system support before re-evaluation?

**Reconciled Answer:** The initial technical performance baseline shall be validated at **250,000 Samples**.
This is a capacity-re-evaluation threshold, not a statement that the system becomes unusable at that point. Before production data approaches this threshold, the laboratory shall perform a documented performance/capacity re-evaluation using the then-current production-like database and hardware.
The longer-term planning reference shall also consider the projected retention workload derived from the approved operating baseline of approximately 100 Samples/day. The projected 10-year count shall be treated as a planning input requiring later validation rather than as an already-proven capacity guarantee.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1217. What TestInstance count must the system support?

**Reconciled Answer:** The initial technical performance baseline shall be validated at **12.5 million TestInstances**, corresponding to 250,000 Samples at the approved peak planning assumption of up to 50 tests per Sample.
The TestInstance acceptance test shall include realistic mixtures of active, completed, corrected, reviewed, verified, approved, and archived records, together with the associated audit, calculation, QC, equipment, and report relationships.
Approaching this threshold shall trigger a documented capacity re-evaluation. The system shall not claim unlimited SQLite capacity or infer long-term capacity solely from row-count arithmetic.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1218. What report/document count must the system support?

**Reconciled Answer:** The initial technical performance baseline shall be validated at **250,000 controlled report/document records**, with the test dataset including Report, ReportRevision, ReportResultSnapshot, DocumentVersion, and issued-PDF relationships as applicable.
The test shall not treat every document as a trivial empty record. Representative document metadata, revision history, report snapshots, and stored issued artifacts shall be present so that retrieval and indexing behavior are meaningful.
Approaching this threshold shall trigger a documented capacity re-evaluation rather than an automatic assumption that additional capacity is guaranteed.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1219. What database size should be tested?

**Reconciled Answer:** The initial database performance baseline shall be validated with a SQLite database reaching approximately **5 GiB**, measured using the actual production database format and representative business/audit data.
A database size approaching **10 GiB** shall trigger formal capacity re-evaluation before relying on the earlier performance evidence for continued operation.
The tested database shall contain representative indexed transactional data rather than being artificially enlarged with irrelevant padding. Evidence shall record database size, SQLite version, application version, operating system, storage medium, workload, and observed performance.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1220. What attachment storage size should be tested?

**Reconciled Answer:** The initial document-storage performance baseline shall be validated with approximately **25 GiB of controlled application-managed attachments and issued artifacts**, including realistic mixtures of PDFs and other approved document types.
Approaching **50 GiB** of application document storage shall trigger a documented storage/performance/recovery re-evaluation.
The test shall cover file creation, retrieval, integrity verification, report artifact lookup, backup, and restore rather than measuring only raw filesystem throughput. The application shall continue to expose documents through the controlled document model rather than direct arbitrary filesystem paths.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1221. What backup duration is acceptable?

**Reconciled Answer:** The operational performance target for a normal full Recovery Set backup shall be **no more than 30 minutes at p95** under the validated normal workload and production-like storage environment.
The measurement shall cover the complete controlled backup operation required for the Recovery Set, including the SQLite database and controlled document/attachment content required for coherent recovery, together with integrity/manifest work that is part of the normal backup procedure.
A backup completing within the target but producing an invalid or incomplete Recovery Set is a failure. Backup duration shall therefore always be evaluated together with backup integrity and recoverability.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1222. What restore duration is acceptable?

**Reconciled Answer:** The technical target for restoration of a complete validated Recovery Set shall be **no more than 4 hours** from authorized recovery start until the restored system is ready for formal smoke testing.
This is intentionally more stringent than the approved **8-hour overall RTO**, leaving the remaining recovery window for application deployment, integrity checks, authentication verification, report/document verification, and operational acceptance.
The measured restore duration shall be recorded under the actual tested recovery hardware and dataset. It shall not be presented as a universal guarantee across materially different hardware or storage conditions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1223. What performance degradation is acceptable during backup?

**Reconciled Answer:** During a normal backup, the principal interactive transaction performance measures shall remain within **125% of their pre-backup baseline p95 latency**, unless a separately documented short quiescence interval is explicitly part of the controlled backup procedure.
For example, a 1.0-second normal p95 transaction baseline would permit no more than approximately 1.25 seconds p95 during the measured backup workload.
Backup operation shall not cause unauthorized partial writes, lost audit events, corrupted document references, inconsistent Recovery Sets, or controlled workflow bypass. Any temporary operational impact shall be measured and documented rather than described qualitatively as "minimal."

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1224. What concurrency scenarios require formal testing?

**Reconciled Answer:** Formal performance testing shall include at least these mixed scenarios:
1. **Normal workload:** 1–3 simultaneous writers with up to 7 simultaneous read-only users.
2. **Stress workload:** 5 simultaneous writers with 5 simultaneous read-only users.
3. **Mixed transactional workload:** Sample/TestInstance updates, result persistence, review/verification/approval actions, searches, queues, and audit writes occurring together.
4. **Report workload:** normal transactional activity occurring while one or more report-generation operations execute.
5. **Backup concurrency:** approved normal workload occurring during backup.
6. **Burst workload:** concentrated creation/update activity representing operational peaks rather than evenly distributed transactions.

Restore testing shall be treated separately because restoration is a controlled recovery activity performed against a quiesced environment, not an ordinary concurrent-production workload.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1225. What hardware configuration will be used for performance testing?

**Reconciled Answer:** Performance and capacity evidence shall use either the actual proposed production host or a formally documented production-equivalent test host.
The minimum technical reference class for the baseline test shall be a **Windows 11 Pro or Windows Server host with at least 4 logical CPU cores, 16 GiB RAM, and local fixed SSD storage**, unless the approved production host is materially stronger and is used directly for acceptance.
The exact CPU model, RAM, storage model/type, free disk space, Windows version/build, power mode where relevant, and virtualization status if applicable shall be recorded in the evidence.
The LIMS software stack shall remain materially identical to the intended production release, including Caddy, FastAPI application, SQLite version, document storage arrangement, and reporting runtime.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1226. What representative data set will be used?

**Reconciled Answer:** The representative performance dataset shall model the approved operating profile and shall contain, at minimum:
* approximately **250,000 Samples**;
* up to approximately **12.5 million TestInstances**;
* approximately **250,000 Report/ReportRevision-level records**;
* approximately **5 GiB SQLite database content**;
* approximately **25 GiB controlled document/attachment content**.

The dataset shall include representative lifecycle distribution rather than only newly created active records. It shall include completed and archived work, result revisions, approval history, report snapshots, audit events, configuration references, QC/equipment relationships, and realistic indexing/selectivity.
Where real laboratory data is unsuitable for testing, controlled synthetic or appropriately anonymized data shall be used. The dataset-generation method and version shall itself be recorded so that the test can be reproduced.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1227. What measurements will count as evidence?

**Reconciled Answer:** Performance evidence shall include measured **p50, p95, and p99 latency where meaningful**, transaction/error counts, concurrency, dataset size, database size, document-store size, CPU utilization, memory utilization, disk utilization, and relevant storage throughput.
The evidence shall separately measure the previously approved acceptance targets for page response, sample search, result save, queue retrieval, normal report generation, large report generation, backup, and restore.
Every performance record shall identify the test date, application/release identifier, database/schema version, SQLite version, operating system, hardware, dataset version/hash where applicable, workload scenario, number of concurrent users, measurement duration, and pass/fail interpretation.
A single favorable measurement is insufficient. Acceptance evidence shall demonstrate the defined scenario over a repeatable test run.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1228. Who accepts the performance results?

**Reconciled Answer:** The **Technical Authority** shall review and technically accept the performance/capacity evidence.
The **Quality Authority** shall verify that the evidence is complete, traceable, repeatable, and consistent with the approved acceptance criteria.
The **Project Owner / Laboratory Business Owner** shall make the final project-level acceptance decision for release or operational use after technical and quality review.
Any failed criterion shall be recorded as a deficiency or exception with documented disposition; it shall not be silently accepted merely because the overall application appears usable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1229. What is the complete test pyramid for v1?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1230. Which rules must have unit tests?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1231. Which rules must have integration tests?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1232. Which database constraints must have direct tests?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1233. Which workflow transitions must have tests?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1234. Which SoD rules must have tests?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1235. Which authorization rules must have tests?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1236. Which calculation formulas must have golden test cases?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1237. Which report templates must have visual/regression tests?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1238. Which PDF artifacts must be compared for stability?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1239. Which migration paths must be tested?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1240. Which backup/restore scenarios must be tested automatically?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1241. Which browser workflows must have Playwright coverage?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1242. What is the minimum required test coverage for critical modules?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1243. Is code coverage a metric, and what is its role?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1244. Which tests are mandatory before a checkpoint can be VERIFIED?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1245. Which tests are mandatory before a checkpoint can be ACCEPTED?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1246. How are test data fixtures controlled?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1247. How are sensitive production data prevented from entering test environments?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1248. Is synthetic data required for validation?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1249. Who defines expected results for critical laboratory calculations?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1250. What exactly must be verified for each major requirement?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1251. What is the difference between implementation testing and formal verification for this project?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1252. Who performs verification?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1253. Who performs system validation?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1254. Who performs UAT?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1255. What evidence format is required for verification?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1256. What evidence format is required for UAT?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1257. What constitutes an acceptable validation deviation?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1258. How are deviations recorded and resolved?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1259. Can a checkpoint be accepted with known minor defects?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1260. If yes, what conditions apply?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1261. What evidence must exist before production deployment?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1262. Which requirements are designated high risk?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1263. What traceability links are required from requirement to test to evidence?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1264. Who owns the traceability matrix?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1265. How are validation changes handled after go-live?

**Reconciled Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Revision 0.8 Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix

### Q1266. Which external requirements are explicitly in scope?

**Reconciled Answer:** The Regulatory / External Source Applicability Register shall contain only external requirements that have an identified authoritative source and an approved applicability determination.

For v1, the register should include, as applicable to the laboratory's actual scope and contractual obligations:
* the current accreditation certificate and scope;
* applicable NABL policies, criteria, and controlled external documents identified by the laboratory Quality/Accreditation Authority;
* applicable customer/contractual requirements that affect records, reporting, traceability, or workflow;
* any other external requirement formally identified by the laboratory as applicable.

LabNexus shall not invent regulatory applicability or assume that every external rule requires software support. Each entry shall identify the source, version/effective date, applicable scope, interpretation, and approval.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1267. Which laboratory procedures must the software support?

**Reconciled Answer:** The software shall support laboratory procedures that directly govern controlled LIMS records and workflow, including at minimum:
* sample receipt, acceptance/rejection, and registration;
* sample identification and allocation;
* TestRequest and TestInstance creation/assignment;
* test execution, observations, calculations, and results;
* Review, Verification, Approval, correction, reopen, rework, and related controlled exceptions;
* report preparation, issuance, reissue, withdrawal, and historical reconstruction;
* equipment eligibility and relevant equipment controls;
* QC and nonconforming-work handling;
* user access, RBAC, competence/authorization, and SoD;
* controlled configuration and change management;
* document/record control;
* audit/history;
* backup, restore, recovery, and operational continuity;
* approved historical migration activities.

The LIMS shall support these procedures without attempting to replace unrelated physical laboratory procedures.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1268. Which laboratory procedures remain outside the software?

**Reconciled Answer:** Procedures that remain outside the v1 LIMS unless separately approved include physical laboratory work that has no required system transaction, detailed instrument operating procedures, field sampling/collection workflows, general procurement/accounting/payroll/HR processes, and broader QMS activities that do not require LIMS-controlled records.
The boundary shall be defined from the laboratory's actual SOP/process inventory rather than from a generic assumption about what a LIMS should contain.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1269. Which requirements are mandatory because of accreditation or contractual obligations?

**Reconciled Answer:** Requirements shall be classified as mandatory because of accreditation or contractual obligations only when an authoritative applicability record establishes the relationship.
The Applicability Register shall identify the specific source requirement, effective version/date, affected LIMS behavior or evidence, affected scope, and approving authority.
The system shall not label a requirement “regulatory” merely because it is considered good practice or desirable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1270. Which requirements are laboratory policy choices rather than external requirements?

**Reconciled Answer:** Laboratory policy choices are requirements adopted by the laboratory that are not being claimed as externally mandated.
Examples include laboratory retention periods where chosen as policy, specific SoD hard blocks, required reasons for exceptional actions, workflow conventions, numbering formats, backup schedules, operational escalation rules, and local approval arrangements.
Each such rule should be identified as a Laboratory Policy in the requirements/decision register so that policy is not confused with external compliance.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1271. Which requirements are technical implementation choices?

**Reconciled Answer:** Technical implementation choices are decisions made to implement the approved laboratory requirements and policies.
Examples include the frozen React/TypeScript/Vite/MUI frontend, FastAPI/Python backend, SQLAlchemy, SQLite, Alembic, secure server-side sessions, Caddy, Jinja2/Chromium report rendering, and the modular-monolith architecture.
Technical choices must not silently redefine laboratory policy or external requirements. Where a technical constraint materially changes behavior, it requires the appropriate change/decision process.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1272. What is the source document for each important laboratory rule?

**Reconciled Answer:** Every important laboratory rule shall have a traceable authoritative source in the Regulatory / External Source Applicability Register or the applicable controlled internal requirements/policy register.

Each entry should identify:
* rule/requirement ID;
* source type;
* document title and controlled identifier;
* version/revision and effective date;
* clause/section/page or equivalent reference where available;
* applicable laboratory scope;
* local interpretation;
* resulting LIMS requirement;
* approving authority;
* related SOP/policy/ADR where applicable.

The objective is to make the basis of each important rule reconstructable rather than relying on memory or undocumented interpretation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1273. Which procedures need to be revised because of the LIMS?

**Reconciled Answer:** LIMS introduction should trigger a controlled review of procedures whose execution, records, responsibilities, or evidence change because of the system.
The likely affected procedures include sample receipt/registration, sample allocation, TestInstance execution, result recording, Review/Verification/Approval, result correction/reopen, report issuance/reissue, equipment/QC controls, nonconforming work, user access/SoD, configuration/change control, document/record control, backup/recovery, and historical migration where applicable.
The exact SOP list shall come from the laboratory's controlled QMS document inventory; the system must not invent document numbers or claim revisions that have not been approved.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1274. Who approves those procedural changes?

**Reconciled Answer:** Procedural changes shall be approved through the laboratory's established document/QMS authority.
For laboratory technical procedures, the responsible Laboratory Technical Authority shall provide technical concurrence as required. The Laboratory Quality Authority/Document Control function shall approve controlled procedural changes according to the laboratory's governance.
System administrators or developers may implement approved changes in the LIMS, but technical/software implementation authority does not itself authorize a change to laboratory procedure.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1275. Which controlled SOPs must exist before go-live?

**Reconciled Answer:** Before go-live, the laboratory shall have approved controlled SOPs/work instructions covering all LIMS-controlled operational behaviors needed for safe use.
At minimum this should cover the laboratory's actual procedures for sample intake/registration, TestInstance execution, result entry, Review/Verification/Approval, corrections/reopen/rework, reporting, QC/nonconforming work, user access and SoD, configuration/change control, document/record retention, backup/recovery, and any approved migration activity.
Only the procedures actually applicable to the laboratory need to be included; the requirement is completeness of the controlled operational boundary, not creation of unnecessary documents.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1276. Which work instructions must exist for LIMS users?

**Reconciled Answer:** Role-specific LIMS work instructions shall exist for the controlled activities users must perform.

At minimum, the laboratory shall maintain approved work instructions covering, as applicable:
* Login/session and user-account use;
* Sample receipt, acceptance/rejection, and registration;
* Sample identification, barcode handling, and allocation;
* TestInstance assignment and execution;
* Observation and result entry;
* Review;
* Technical Verification;
* Approval;
* Result correction, reopen, rework, retest, repeat, and other controlled exceptions;
* Report preview, issue, reissue, withdrawal, and retrieval;
* QC and nonconforming-work actions;
* Controlled document use;
* User access/role administration where applicable;
* Backup, restore, recovery, and other privileged operational procedures where applicable.

Laboratory-user work instructions and privileged technical/administrative work instructions should be separated where their responsibilities differ.
The approved work instructions must correspond to the actual implemented LabNexus behavior. A software screen or feature must not become the de facto laboratory procedure without the corresponding controlled documentation being reviewed and approved.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1277. Which records must be retained as quality evidence outside the application itself?

**Reconciled Answer:** Records that remain outside LabNexus shall be identified in a controlled **Quality Evidence / Record Retention Matrix** rather than assumed to be part of the application.

Examples may include:
* Original paper records that were not selected for migration;
* Controlled laboratory notebooks or worksheets retained as physical originals;
* Original external certificates or reports received from third parties where the original artifact is retained outside LabNexus;
* Controlled QMS documents whose authoritative copy is maintained outside the LIMS document store;
* Training/competence records where the laboratory's approved competence process remains external;
* Infrastructure/Windows/security evidence that is generated and retained through host-level administrative controls;
* Physical equipment records or other evidence specifically assigned by laboratory policy to an external record system/location;
* Source records used for historical migration where the original source must remain preserved outside the LIMS.

For every such category, the laboratory shall define the authoritative location, owner/custodian, retention period, retrieval method, relationship to LabNexus records, and applicable access controls.
LabNexus should contain a controlled reference or evidence linkage where the external record is relevant to a LIMS-controlled activity. The system must not claim that an external record is retained inside LabNexus when it is not.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1278. Is a validation master plan required?

**Reconciled Answer:** A **Validation Master Plan or equivalent controlled validation plan is required for v1**, provided that the laboratory's final QMS terminology permits either the formal VMP name or an equivalent controlled validation-planning document.
The plan shall define the overall validation strategy, scope, responsibilities, lifecycle, risk basis, required testing/verification/validation activities, acceptance criteria, evidence requirements, deviation handling, traceability, approval, and maintenance after go-live.

The VMP shall cover the computerized system as a whole while allowing detailed subordinate plans/protocols for areas such as:
* Requirements and design verification;
* Database/data-integrity controls;
* Authorization and SoD;
* Workflow/state transitions;
* Calculations/formulas;
* Reports/PDF rendering;
* Equipment/QC controls where software-enforced;
* Audit/history;
* Migration;
* Backup/restore/recovery;
* Security;
* Performance/capacity;
* System validation and UAT.

The exact VMP structure and terminology shall follow the laboratory's controlled QMS rather than being imposed by the software.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1279. Is a computerized-system validation package required by laboratory policy?

**Reconciled Answer:** The laboratory should maintain a **controlled computerized-system validation package** for LabNexus as the consolidated evidence set demonstrating that the system is fit for its intended use.

The package should include, as applicable:
* Approved intended-use/scope statement;
* Requirements and traceability;
* Risk assessment;
* Architecture/design baseline;
* Controlled test/verification protocols and results;
* Validation evidence;
* UAT evidence;
* Critical calculation/formula verification;
* Workflow/authorization/SoD verification;
* Report/PDF validation;
* Migration validation where applicable;
* Backup/restore and recovery evidence;
* Security evidence;
* Deviations/defects and their dispositions;
* Final validation summary and approval;
* Version/release identification of the validated system.

This package is evidence of the laboratory's validation of its computerized system; LabNexus itself does not claim regulatory or accreditation status merely because the package exists.
The laboratory's Quality Authority shall determine the authoritative QMS structure, required signatures, retention, and approval criteria for this validation package.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1280. Are risk assessments required?

**Reconciled Answer:** Yes. **Risk assessments are required** for LabNexus and shall be part of the controlled project and validation evidence.

Risk assessment shall be proportionate to the actual risks of the system and should cover, at minimum:
* Data integrity and historical reconstruction;
* Sample identity/traceability;
* Result/calculation integrity;
* Review/Verification/Approval;
* SoD and authorization;
* Report issuance and correction/reissue;
* QC and nonconforming work;
* Equipment eligibility where software-enforced;
* Audit/history;
* Migration;
* Backup/restore/recovery;
* Security and confidentiality;
* Availability/offline operation;
* Configuration/change control;
* Time integrity;
* Critical external dependencies.

Risk controls shall map to requirements, design controls, procedures, tests, and verification evidence where applicable.
Risk assessments shall be versioned and revisited when material changes occur, including changes to architecture, workflow, authorization/SoD, calculations, reporting, accreditation representation, security, or recovery arrangements.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1281. Who signs off the compliance mapping?

**Reconciled Answer:** Compliance mapping shall be approved by the **Laboratory Quality/Accreditation Authority**, with Technical Authority concurrence where the mapping involves technical or method-specific interpretation.
The software developer, System Administrator, or ordinary configuration administrator shall not be the final authority for declaring that an external laboratory requirement has been satisfied.

The compliance mapping approval record shall identify:
* Requirement/source;
* Source version/effective date;
* Applicable laboratory scope;
* Local interpretation;
* Related LIMS requirement/control;
* Supporting SOP/policy where applicable;
* Verification/validation evidence;
* Outstanding limitations or exclusions;
* Approver;
* Technical concurrence where required;
* Approval date/effective status.

Where an external requirement is ambiguous, the mapping shall record the laboratory's approved interpretation rather than silently converting an uncertain interpretation into a software rule.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1282. What are the primary security threats for this deployment?

**Reconciled Answer:** The primary security threats for the v1 deployment are:
* Unauthorized application access through compromised or misused user credentials;
* Privilege escalation or inappropriate role/permission assignment;
* Unauthorized direct access to the SQLite database or document storage;
* Unauthorized Windows/local-administrator access to the host;
* Compromise of privileged administrator accounts;
* Malware/ransomware affecting the host, database, documents, or backups;
* Unauthorized removable-media use or compromise of backup media;
* Accidental or malicious alteration/deletion of files or database content;
* Credential/session theft or misuse;
* Unauthorized export, download, or disclosure of confidential laboratory records;
* Tampering with configuration, workflow, SoD, report, or formula definitions;
* Clock/time manipulation affecting auditability and controlled timestamps;
* Denial of service or host/storage failure;
* Failure or corruption of backups;
* Physical theft, loss, or unauthorized access to the server or backup media.

The Security Baseline shall classify these threats by applicable control layer: application, database, operating system, filesystem, network, physical environment, backup/recovery, and operational procedure.
Security controls shall remain proportionate to the single-site/offline deployment. v1 does not require enterprise SIEM, HSM infrastructure, cloud security services, or speculative distributed-security architecture.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1283. Is the server physically secured?

**Reconciled Answer:** Yes. The production Windows host shall be physically secured in a location accessible only to authorized personnel.

The physical-security baseline should include:
* Restricted access to the server/host location;
* Protection against unauthorized removal or tampering;
* Controlled access to removable backup media;
* Appropriate protection against accidental power loss and environmental hazards;
* Physical access restricted to authorized technical/operational personnel;
* A documented procedure for physical access where the laboratory's QMS requires such evidence.

The exact room, lock, access-control mechanism, UPS capacity, and environmental provisions are deployment inputs and shall be recorded in the Deployment/Operational Security Baseline rather than invented by the software.
Physical security remains part of the LabNexus security boundary; application controls alone cannot protect a host that is physically unrestricted.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1284. Who can log into Windows on the host?

**Reconciled Answer:** Windows interactive login to the production host shall be restricted to **authorized technical/system-administration personnel**.
Ordinary laboratory users shall operate LabNexus through the browser and shall not require Windows login access to the production server merely to perform laboratory work.
The Windows access list shall be separately controlled from LabNexus application roles. Possession of a LabNexus laboratory role shall not automatically grant Windows host access.
Service accounts used by application components shall not be used as ordinary human login accounts.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1285. Who has local administrator privileges?

**Reconciled Answer:** Local Administrator privileges shall be limited to the **designated System Administrator(s)** and only where technically required.

The baseline should use:
* Least privilege;
* Separate named administrative identities rather than shared administrator accounts where practicable;
* No local-administrator rights for ordinary laboratory users;
* No assumption that application administration equals Windows administration;
* Controlled approval for adding/removing local administrators;
* Auditable administrative changes.

The number of privileged Windows administrators shall be kept to the minimum operationally necessary, with an approved backup/alternate administrator where required for recoverability.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1286. Are laboratory users prevented from using Windows administrator accounts?

**Reconciled Answer:** Yes. Laboratory users shall use **standard Windows/user identities** and shall not routinely operate the production host under Windows Administrator accounts.
The LIMS application must not depend on laboratory users having local administrative privileges.
This separation is important because application RBAC/SoD and Windows host privilege are different control layers. A user being authorized to perform technical laboratory work in LabNexus does not authorize direct operating-system administration.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1287. Can users access the SQLite file directly?

**Reconciled Answer:** Ordinary users shall **not have direct access to the SQLite database file**.

The authoritative access path shall be:
**Browser → Caddy → FastAPI application → SQLAlchemy/SQLite**

Direct opening, editing, copying, replacing, or modifying the live SQLite database by ordinary users is prohibited.
Authorized System Administrators may have controlled filesystem access for backup, recovery, maintenance, or incident handling where required, but direct manipulation of production records outside the application shall not be a normal operational method.
The security baseline shall explicitly acknowledge that LabNexus cannot guarantee protection against a person who already has unrestricted Windows/filesystem access. Host permissions therefore form part of the overall security boundary.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1288. Can users access the document storage directories directly?

**Reconciled Answer:** Ordinary users shall **not have direct filesystem access to the application-controlled document/attachment storage directories**.
Documents shall be accessed through authorized LabNexus workflows. The application shall resolve internal document identities to storage objects and shall not expose arbitrary filesystem paths.
Direct filesystem access shall be restricted to authorized technical/administrative personnel for controlled backup, recovery, maintenance, or incident handling.
The storage hierarchy shall not be treated as a user-facing document repository whose files can be freely renamed, replaced, or deleted outside the application.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1289. Is remote desktop allowed to the server?

**Reconciled Answer:** Remote Desktop should be **disabled for ordinary laboratory use** and allowed only where a documented technical/administrative need exists.

Recommended v1 policy:
* No RDP access for ordinary laboratory users;
* RDP permitted only for authorized System Administrators/technical maintainers;
* Access restricted to the approved LAN/administrative environment;
* Strong Windows authentication and account controls;
* RDP activity covered by the host security baseline;
* Temporary exceptional access explicitly authorized and documented where required.

Remote administration must not become a substitute for application workflows or create an undocumented secondary administrative pathway.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1290. Who is allowed to use remote desktop?

**Reconciled Answer:** RDP access shall be limited to designated **System Administrators and, where separately approved, authorized technical maintainers** whose duties require host administration.
Laboratory Analysts, Reviewers, Verifiers, Approvers, Quality users, and ordinary application administrators shall not receive RDP rights merely because they hold those LabNexus roles.
RDP authorization shall be independently managed at the Windows/network security layer and should be reviewed periodically.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1291. Is removable media access restricted on the server?

**Reconciled Answer:** Yes. Removable-media access on the production server shall be **restricted and controlled**, but not necessarily prohibited because the approved operating model includes offline/removable backup capability.

Controls shall include:
* Only approved removable media;
* Controlled authorization for connecting/use;
* Malware scanning;
* Encryption where appropriate for backup/confidential data;
* Controlled custody and storage;
* Identification of backup media;
* Safe eject/removal procedures;
* Recording of significant backup/restore media operations where required.

Unapproved USB storage devices shall not be treated as a routine operational mechanism.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1292. Are USB devices used for backup?

**Reconciled Answer:** Yes. USB/removable media may be used for **controlled offline backup and recovery activities**, consistent with the approved Backup/Recovery Baseline.

The process shall distinguish:
**Backup Created → Backup Validated → Backup Stored → Backup Restorable → Restore Tested**

Backup media shall not be treated as trustworthy merely because the file was successfully copied.
Each backup medium should have controlled identification, integrity verification, retention/disposition rules, appropriate confidentiality protection, and documented custody.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1293. What malware/antivirus controls are available?

**Reconciled Answer:** The production Windows host shall use the organization's **approved local Windows malware/antivirus protection**, with Microsoft Defender/Windows Security being the expected v1 baseline where that is the organization's approved Windows security control.

The security baseline shall define:
* Real-time protection behavior;
* Scheduled/on-demand scanning;
* Malware detection/quarantine handling;
* Treatment of database/document storage;
* Removable-media scanning;
* Application-upload scanning where supported;
* Definition/signature update procedure, including offline update handling where Internet is unavailable;
* Response when the antivirus service is disabled, unhealthy, or unavailable.

LabNexus shall not claim malware protection merely because antivirus software is installed; its operational status must be part of host/security health checks where practicable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1294. Can antivirus quarantine or lock database/document files?

**Reconciled Answer:** Yes. Antivirus software may quarantine or temporarily lock files required by LabNexus, including database/document files, and the deployment must account for that possibility.

The system shall therefore:
* Monitor relevant security/operational failures where practicable;
* Avoid unsafe assumptions that files are always immediately available;
* Use short database write transactions and retry behavior appropriate to transient file/database contention;
* Treat quarantine or file-access failure as an operational incident requiring controlled investigation;
* Never silently replace or reconstruct a protected file merely because antivirus access failed.

Any antivirus exclusion shall be a separately controlled decision under Q1295.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1295. How will database/file exclusions be handled safely, if required?

**Reconciled Answer:** Security exclusions shall **not be used by default**.

Where an exclusion is technically necessary and has been validated, it shall follow least privilege:
* Exact path/process scope rather than broad disk-level exclusions;
* Documented technical reason;
* Risk assessment;
* Security/technical approval;
* Verification that the exclusion does not unnecessarily disable protection of unrelated data;
* Periodic review;
* Removal when no longer required.

The entire application directory, entire system drive, or broad database/document storage hierarchy must not be excluded merely as a convenience.
Any required exclusion shall be documented in the Deployment Security Baseline and validated with the actual Windows/antivirus configuration before production use.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1296. How are secrets protected?

**Reconciled Answer:** Production secrets shall be protected using **OS-controlled access and a protected deployment secret mechanism**, not source code, Git, ordinary configuration files, or database tables containing plaintext secrets.

Secrets shall be:
* Stored outside the repository;
* Restricted to the process/administrative identities that require them;
* Protected by Windows filesystem/OS controls and, where practical, Windows DPAPI or an equivalent OS-protected mechanism;
* Never displayed through the ordinary LabNexus UI;
* Excluded from logs, error responses, audit payloads, and diagnostic dumps;
* Backed up/recovered only through a controlled secret-recovery procedure where necessary.

No HSM is required for v1.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1297. Which secrets exist in v1?

**Reconciled Answer:** The v1 secret inventory shall be limited to actual secrets required by the implementation.

Expected categories include:
* Session/application secret material;
* CSRF or equivalent application security secret material if separately required by implementation;
* SMTP credentials only if email is implemented;
* Backup-encryption key material if encrypted backups are implemented;
* Any Windows/service credentials required by deployment;
* Other external-system credentials only if separately approved integrations exist.

User passwords shall never be stored as plaintext; LabNexus stores Argon2id password hashes and associated password-verification data.
Ordinary identifiers, report numbers, user IDs, role names, configuration IDs, and other non-secret values shall not be treated as secrets unnecessarily.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1298. Where are session secrets stored?

**Reconciled Answer:** Session secret material shall be stored in the **protected deployment secret mechanism on the production host**, accessible to the LabNexus application process but not to ordinary laboratory users.
The preferred v1 implementation is an OS-protected secret/configuration mechanism using Windows filesystem ACLs and, where appropriate, Windows DPAPI protection.
Session secrets shall not be stored in the SQLite database, committed to Git, embedded in frontend JavaScript, or exposed through API responses.
Changing the session secret shall be treated as a controlled security operation because it may invalidate existing sessions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1299. Where are SMTP credentials stored if email is implemented?

**Reconciled Answer:** If SMTP/email functionality is not implemented in v1, **no SMTP credentials shall exist in the system**.
If email is later approved and implemented, SMTP credentials shall be stored using the same protected secret mechanism as other production secrets.

The credentials shall never appear in:
* Source code;
* Git history;
* Frontend code;
* Database business records;
* Application logs;
* Error responses;
* Diagnostic exports.

Email functionality remains subordinate to the offline-first architecture; no mandatory Internet-based mail service shall be introduced without separate approval.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1300. How are backup encryption keys stored?

**Reconciled Answer:** Backup encryption keys shall be protected **separately from the backup media they protect**.

The v1 key-management procedure shall provide:
* Unique controlled encryption key/material for the approved encrypted backup scheme;
* Restricted access;
* Separate custody from the encrypted backup media;
* A documented recovery/escrow procedure;
* Key identification/versioning;
* Controlled rotation/replacement;
* Evidence that the recovery procedure has actually been tested.

A backup whose encryption key is stored only on the same removable media does not provide adequate recovery assurance.
HSM infrastructure is not required for v1; key custody shall use proportionate protected storage and controlled offline recovery evidence.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1301. How are secrets rotated?

**Reconciled Answer:** Secret rotation shall be **event-driven and policy-controlled**, rather than based on an arbitrary universal interval.

Rotation shall occur at minimum when:
* A secret may have been exposed;
* A privileged person with secret access leaves or loses authorization;
* An administrator/service identity is compromised;
* An external credential is changed or revoked;
* Backup-encryption-key replacement is required by policy or incident;
* A planned security-maintenance cycle requires rotation.

Different secret classes may have different rotation procedures.
Rotation must preserve operational continuity and recoverability. For example, changing the application session secret may invalidate active sessions and therefore requires an explicit operational procedure.
All material secret rotations shall generate appropriate security/change evidence without recording the secret value itself.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1302. Who can read production secrets?

**Reconciled Answer:** Production secrets shall be readable only by the **minimum technical identities required to operate or recover the system**.

The preferred access model is:
* LabNexus application/service identity: runtime use without human display;
* Authorized System Administrator: controlled maintenance/recovery access where operationally necessary;
* Designated technical maintainer: access only where explicitly required and authorized;
* Ordinary laboratory users: no access;
* Application administrators: no secret visibility merely because they administer LabNexus roles.

The system shall avoid a design in which any person who can administer ordinary laboratory configuration can read production secrets.
Secret retrieval/use shall be logged where practicable, but the secret value itself shall never be logged.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1303. Are security logs separate from laboratory audit records?

**Reconciled Answer:** Yes. **Security/operational logs and laboratory audit records shall remain distinct evidence classes**, while allowing controlled cross-reference.

Laboratory audit records remain authoritative for application business events such as:
* Result changes;
* Review/Verification/Approval;
* Configuration changes;
* Access/role changes;
* Report issue/reissue;
* Controlled exceptions.

Host/security evidence may include:
* Windows authentication events;
* Privileged account activity;
* RDP activity;
* Antivirus events;
* File/OS security events;
* Service failures;
* Backup/restore operations.

The two evidence classes should be correlated through timestamps, actors, host/service identifiers, and incident/change references where appropriate.
Security logs shall not be treated as a replacement for the application audit trail, and the application audit trail shall not be treated as a complete record of unrestricted OS-level activity.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1304. What incident-response steps apply to suspected compromise?

**Reconciled Answer:** Suspected compromise shall trigger a controlled incident-response procedure:
1. **Detect and classify** the suspected event.
2. **Contain** the affected account, host, session, service, or network path as appropriate.
3. **Preserve evidence** before unnecessary cleanup or overwriting where practicable.
4. **Disable/revoke affected credentials and sessions.**
5. **Protect the database, documents, configuration, and backups** from further modification.
6. **Assess integrity and scope**, including application audit history, host/security evidence, configuration, files, database state, and backup integrity.
7. **Determine whether the system can be trusted** or must be restored from a known-good recovery point.
8. **Rotate affected secrets/credentials.**
9. **Restore and validate** where restoration is necessary.
10. **Perform security and laboratory-impact assessment** before resuming controlled operation.
11. **Record the incident, decisions, evidence, corrective actions, and approval to resume.**

A suspected security incident that may have affected technical records shall also trigger assessment of affected laboratory records, reports, approvals, audit integrity, and confidentiality.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1305. What happens if an administrator account is compromised?

**Reconciled Answer:** If a Windows/System Administrator account is compromised, treat the event as a **high-severity privileged security incident**.

The immediate response shall include:
* Disable or isolate the compromised administrative identity;
* Revoke active sessions/remote access as applicable;
* Prevent further privileged access;
* Preserve available Windows/security/application evidence;
* Assess whether the attacker could access or modify the SQLite database, documents, configuration, backups, or secrets;
* Assess whether audit/history integrity may have been affected;
* Rotate potentially exposed secrets;
* Review administrator and configuration changes;
* Validate the host and application environment;
* Restore from a known-good backup/recovery point when integrity cannot be established;
* Perform full post-recovery verification before controlled resumption.

The incident must not be considered resolved merely because the administrator password was changed.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1306. What happens if a user's password is compromised?

**Reconciled Answer:** If a user's password is suspected to be compromised, the account shall be **immediately contained through application access controls**.

The minimum response shall be:
* Disable or suspend the affected user account where compromise is credible;
* Invalidate active application sessions;
* Reset the password through the controlled account-management procedure;
* Require the user to authenticate again;
* Review recent access and high-risk actions associated with the account;
* Determine whether any technical records, reports, configuration, or confidential information may have been affected;
* Escalate to security incident handling when the account had privileged or sensitive access.

For privileged users, the response shall also consider whether related credentials or secrets may have been exposed.
Password compromise shall not result in deletion or alteration of historical audit records.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1307. Is account disablement an immediate action?

**Reconciled Answer:** Yes. **Application account disablement shall take effect immediately for new and subsequent controlled actions**, subject only to the technical timing required to terminate active sessions reliably.

When a user is disabled, the system shall:
* Mark the account inactive/disabled;
* Reject subsequent authentication;
* Invalidate active sessions;
* Block new controlled business actions;
* Re-evaluate authorization at the backend for sensitive transactions;
* Preserve all previously recorded history.

A user who was authorized yesterday must not remain capable of performing new Approval, Verification, Correction, Configuration, or other controlled actions merely because an old browser session remains open.
Windows-account disablement shall be handled by the OS administration procedure and should be performed immediately where a host-level account compromise or personnel-security event requires it.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1308. Is security incident evidence retained?

**Reconciled Answer:** Yes. Security-incident evidence shall be **retained as controlled evidence**, especially where the incident affects laboratory records, confidentiality, authorization, system integrity, or recovery.

The retained incident package should include, as applicable:
* Incident identifier;
* Detection date/time;
* Affected user/account/host/service;
* Nature and classification of the incident;
* Containment actions;
* Relevant application audit references;
* Relevant Windows/security/antivirus evidence;
* Configuration/change evidence;
* Affected records or record-impact assessment;
* Backup/recovery assessment;
* Credential/secret-rotation evidence without exposing secret values;
* Corrective and preventive actions;
* Verification/validation before service restoration;
* Approval to resume operation;
* Closure decision.

Where the incident relates to controlled laboratory records, associated evidence shall be retained for at least the applicable **10-year laboratory retention period**, unless a longer applicable requirement or hold applies.
Raw operational/security logs that have no continuing evidentiary relevance may have a separately approved shorter retention period, but an incident record itself shall preserve the evidence necessary to reconstruct the event and its impact.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1309. What customer information is confidential?

**Reconciled Answer:** For v1, the following shall be treated as **laboratory-confidential customer information unless explicitly designated otherwise under an approved policy**:
* Customer legal/business identity;
* Customer contacts and contact details;
* Addresses and communication information;
* Customer/project/contract information;
* Sample identity and source information;
* Test requests and requested services;
* Technical results, observations, calculations, and related records;
* Reports and report history;
* Customer-provided documents and confidential attachments;
* Commercial/pricing information maintained in LabNexus;
* Other customer-provided information that the laboratory has a confidentiality obligation to protect.

Access shall follow the principle of minimum necessary access and the approved authorization matrix.
Confidentiality classification shall not create a second uncontrolled authorization system. Ordinary confidentiality shall be handled through RBAC, workflow context, permissions, and controlled exports/downloads. Any customer-specific restriction that requires access to vary by customer/project/record shall be introduced only through an explicitly approved authorization extension.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1310. What personal information is stored about users?

**Reconciled Answer:** User data should be minimized to what is operationally required: name, username, role/authorization, staff ID where applicable, contact information if required, competence/training references, and audit identity.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1311. What personal information is stored about customer contacts?

**Reconciled Answer:** Customer-contact data should be limited to information actually needed for communication/customer records.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1312. Is personal data minimization required?

**Reconciled Answer:** Yes. Data minimization is required.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1313. Which roles may see customer contact information?

**Reconciled Answer:** Customer contact information visible only to roles that require it, primarily authorized administrative/customer-management and relevant supervisory roles.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1314. Which roles may see technical results?

**Reconciled Answer:** Technical results visible to authorized technical/operational roles; access must be role- and workflow-controlled.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1315. Are there confidentiality classifications for samples/results/reports?

**Reconciled Answer:** Yes. LabNexus shall support a **controlled confidentiality classification for samples, results, and reports only where the laboratory has an approved operational requirement**.

For v1, the recommended baseline is:

**1. Normal Laboratory Confidential**
The default classification for customer, sample, TestInstance, result, report, and related technical records. Access follows the ordinary RBAC, workflow, and minimum-necessary access rules.

**2. Restricted / Special Confidentiality**
An optional controlled classification for records subject to an approved customer-specific, contractual, commercial, or other special confidentiality requirement.

The restricted classification shall not be freely assigned by ordinary users. Its use shall require:
* An approved classification type;
* An authorized person who may assign it;
* Reason/justification;
* Effective date/time;
* Applicable record scope;
* Authorized roles/users or access rule;
* Export/download/printing implications where applicable;
* Audit of assignment and subsequent changes;
* Historical treatment of classification changes.

The classification shall apply consistently to the relevant controlled objects, including Sample, TestInstance/Result, ReportRevision, and associated documents where required.

Confidentiality classification must **not** override:
* Hard authorization/SoD controls;
* Technical result integrity;
* Review/Verification/Approval requirements;
* Retention requirements;
* Audit/history preservation;
* Controlled report-revision history.

The system should therefore avoid arbitrary per-record permission programming in v1. Instead, approved confidentiality classifications should be implemented through a small, versioned policy model that adds an additional authorization condition where required.
Unless the laboratory explicitly approves a more granular model, **Normal Laboratory Confidential shall remain the default**, with Restricted/Special Confidentiality used only for identified cases.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1316. Are any results commercially sensitive beyond ordinary laboratory confidentiality?

**Reconciled Answer:** Yes. The laboratory should support the classification of some results as **commercially sensitive beyond ordinary laboratory confidentiality**, but the classification must be explicitly defined by laboratory policy rather than inferred by the application.
Examples may include results that could materially affect a customer's commercial position, contractual negotiations, product release decisions, proprietary process information, or other specifically designated business-sensitive information.

For v1, however, commercially sensitive classification should be implemented only where the laboratory has identified a real operational requirement and approved the additional authorization model.

Where such classification is adopted, the controlled model should define:
* Classification/category;
* Who may designate it;
* Scope of application;
* Authorized viewers;
* Export/download restrictions;
* Whether printing is restricted;
* Customer/project applicability;
* Effective date;
* Review/expiry where applicable;
* Audit requirements;
* Historical treatment of classification changes.

The classification must not alter the underlying technical result or report history. It controls authorized access and handling of the information.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1317. Are special customer restrictions required?

**Reconciled Answer:** Special customer restrictions shall be **supported only through an explicitly approved customer-specific confidentiality/access policy**; they shall not be assumed for every customer.

A supported restriction may define, for example:
* Customer/project-specific access restrictions;
* Named-role restrictions;
* Restricted result/report visibility;
* Export/download restrictions;
* Printing restrictions;
* Controlled external disclosure;
* Effective dates and expiry/review;
* Authorized approver;
* Audit requirements;
* Treatment of historical records and previously issued reports.

For v1, the preferred approach is to keep this capability **bounded and policy-driven** rather than introducing a broad arbitrary per-customer access-control engine.
A customer-specific restriction must never override hard workflow/SoD controls, data-integrity rules, retention requirements, or the authoritative technical record.
Where no approved special restriction exists, the normal laboratory confidentiality and RBAC model applies.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1318. Are report downloads audited?

**Reconciled Answer:** Yes. Report downloads should be auditable where the application controls the download.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1319. Are exports audited?

**Reconciled Answer:** Yes. Exports should be auditable, including user, time, export type/filter context where appropriate.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1320. How are printed reports controlled?

**Reconciled Answer:** Printed reports must be controlled through role authorization and report issuance status; the application should record printing where technically observable through the controlled workflow, but cannot guarantee physical handling after printing.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1321. How are backup copies protected from unauthorized access?

**Reconciled Answer:** Backup media protected through encryption, access control, physical security, separated storage, and controlled custody.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1322. What is the approved process for removing personal data where legally required, if ever?

**Reconciled Answer:** Any legally required removal/minimization of personal data must use a controlled privacy/legal process and must not casually delete immutable laboratory history.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1323. How does that interact with immutable laboratory history?

**Reconciled Answer:** Immutable laboratory history remains authoritative. Where privacy law requires alteration/removal, the system must use a controlled/redaction/anonymization mechanism that preserves necessary audit/history integrity and records why the change occurred.

---

# 54. Export, Import, and Reporting Outside the LIMS

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1324. What data may be exported?

**Reconciled Answer:** Bulk export is privileged/high-impact and must be authorization- and audit-controlled.
**Revision 0.8 Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Security Baseline

### Q1325. Who may export it?

**Reconciled Answer:** Bulk export is privileged/high-impact and must be authorization- and audit-controlled.
**Revision 0.8 Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Security Baseline

### Q1326. Which formats are required: CSV, Excel, PDF, other?

**Reconciled Answer:** Bulk export is privileged/high-impact and must be authorization- and audit-controlled.
**Revision 0.8 Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Security Baseline

### Q1327. Are exports filtered by user permission?

**Reconciled Answer:** Bulk export is privileged/high-impact and must be authorization- and audit-controlled.
**Revision 0.8 Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Security Baseline

### Q1328. Must exports include audit/provenance metadata?

**Reconciled Answer:** Bulk export is privileged/high-impact and must be authorization- and audit-controlled.
**Revision 0.8 Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Security Baseline

### Q1329. Are bulk exports required?

**Reconciled Answer:** Bulk export is privileged/high-impact and must be authorization- and audit-controlled.
**Revision 0.8 Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Security Baseline

### Q1330. Are bulk exports audited?

**Reconciled Answer:** Bulk export is privileged/high-impact and must be authorization- and audit-controlled.
**Revision 0.8 Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Security Baseline

### Q1331. Is direct database export prohibited for ordinary users?

**Reconciled Answer:** Bulk export is privileged/high-impact and must be authorization- and audit-controlled.
**Revision 0.8 Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Security Baseline

### Q1332. Is an administrator data export function required?

**Reconciled Answer:** Bulk export is privileged/high-impact and must be authorization- and audit-controlled.
**Revision 0.8 Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Security Baseline

### Q1333. Is there a controlled import function after go-live?

**Reconciled Answer:** Bulk export is privileged/high-impact and must be authorization- and audit-controlled.
**Revision 0.8 Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Security Baseline

### Q1334. How are imported records validated?

**Reconciled Answer:** Imports are controlled by explicit approved types; no generic spreadsheet-to-database bypass.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Import Control / Migration Provenance Contract

### Q1335. How are external IDs mapped to internal IDs?

**Reconciled Answer:** Imports are controlled by explicit approved types; no generic spreadsheet-to-database bypass.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Import Control / Migration Provenance Contract

### Q1336. Is charge calculation definitely required in v1?

**Reconciled Answer:** Charge calculation is **not required for v1**. It may be introduced later through an approved commercial work package. Invoicing, accounts receivable, payments, and tax/accounting remain external.

**Revision 0.8 Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record

### Q1337. Which chargeable units exist?

**Reconciled Answer:** No v1 chargeable-unit model is required because charge calculation is deferred. A future commercial decision shall define the unit basis before implementation.

**Revision 0.8 Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record

### Q1338. Is pricing per test, sample, request, report, or another basis?

**Reconciled Answer:** Pricing basis (test/sample/request/report/other) is **deferred from v1**. No commercial charging logic shall be implemented by inference.

**Revision 0.8 Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record

### Q1339. Are rates customer-specific?

**Reconciled Answer:** Customer-specific rates are **deferred from v1**. Future customer pricing shall require an approved commercial decision and controlled effective-dated configuration.

**Revision 0.8 Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record

### Q1340. Are rates method-specific?

**Reconciled Answer:** Method-specific rates are **deferred from v1**. No method/rate linkage is required in the controlled v1 LIMS baseline.

**Revision 0.8 Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record

### Q1341. Are rates discipline-specific?

**Reconciled Answer:** Discipline-specific rates are **deferred from v1**. No discipline/rate linkage is required in the controlled v1 LIMS baseline.

**Revision 0.8 Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record

### Q1342. Are rates effective-dated?

**Reconciled Answer:** Effective-dated rates are not required in v1 because rates themselves are deferred. Any future rate implementation shall use effective-dated versioning.

**Revision 0.8 Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record

### Q1343. Can discounts be applied?

**Reconciled Answer:** Discounts are **out of v1 scope**. No discount engine or discount configuration shall be implemented.

**Revision 0.8 Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record

### Q1344. Who approves discounts?

**Reconciled Answer:** Discount approval is **out of v1 scope**. No discount-approval workflow is required.

**Revision 0.8 Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record

### Q1345. Can charges be overridden?

**Reconciled Answer:** Charge overrides are **out of v1 scope**. No commercial override mechanism shall be implemented.

**Revision 0.8 Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record

### Q1346. What audit evidence is required for price overrides?

**Reconciled Answer:** Price-override audit evidence is **out of v1 scope** because price overrides are not implemented. If later approved, override actor, reason, authorization, previous value, new value, timestamp, and effective scope shall be auditable.

**Revision 0.8 Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record

### Q1347. Are taxes calculated inside LIMS or outside?

**Reconciled Answer:** Tax calculation remains **external to LabNexus v1**. The LIMS shall not become the authoritative tax/accounting system.

**Revision 0.8 Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record

### Q1348. Is a tax rate merely displayed or legally calculated?

**Reconciled Answer:** No legally authoritative tax calculation is performed in LabNexus v1. Any future display-only tax information shall be explicitly classified as reference data and not represented as accounting authority.

**Revision 0.8 Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record

### Q1349. Is invoicing intentionally external?

**Reconciled Answer:** Yes. Invoicing is intentionally **external to the v1 LIMS**. The LIMS may later store controlled external invoice references if separately approved.

**Revision 0.8 Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record

### Q1350. Is invoice number stored for reference only?

**Reconciled Answer:** An invoice number is not required in the v1 controlled laboratory model. A future external-invoice reference field may be added through controlled change without making LabNexus the invoicing system.

**Revision 0.8 Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record

### Q1351. Is payment status stored?

**Reconciled Answer:** Payment status is **out of v1 scope**. Payment processing and accounts receivable remain external.

**Revision 0.8 Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record

### Q1352. Is that information read-only/reference-only from an external system?

**Reconciled Answer:** Any future invoice/payment information presented in LabNexus shall be reference-only data from the approved external business system unless a separate scope change is authorized.

**Revision 0.8 Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record

### Q1353. Are commercial calculations part of the report?

**Reconciled Answer:** Commercial calculations are **not part of the v1 technical report authority**. Issued reports shall remain focused on controlled laboratory results and approved report content; commercial information may be introduced later only by explicit report-content approval.

**Revision 0.8 Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record

### Q1354. Which user groups require training?

**Reconciled Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model

### Q1355. Who will train users?

**Reconciled Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model

### Q1356. What training records must be retained?

**Reconciled Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model

### Q1357. Must users pass a competency assessment before using the LIMS for controlled work?

**Reconciled Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model

### Q1358. Which roles require role-specific competency?

**Reconciled Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model

### Q1359. Must user competency be linked to system permissions?

**Reconciled Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model

### Q1360. What happens when a user is not competent or their training expires?

**Reconciled Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model

### Q1361. Can an inactive/expired competency automatically block specific actions?

**Reconciled Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model

### Q1362. Who updates training/competency records?

**Reconciled Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model

### Q1363. Are training records managed inside the LIMS or outside?

**Reconciled Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model

### Q1364. Is user documentation required in the application?

**Reconciled Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model

### Q1365. Are tooltips/help text required?

**Reconciled Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model

### Q1366. Is a local user manual required before go-live?

**Reconciled Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Revision 0.8 Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model

### Q1367. Who maintains the system after go-live?

**Reconciled Answer:** Post-go-live maintenance: designated LIMS technical maintainer/developer + System Administrator, with Laboratory Quality/Technical Authority governing laboratory configuration changes.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1368. Who owns bug fixes?

**Reconciled Answer:** Bug fixes owned by the software technical maintainer/developer. Laboratory policy defects remain laboratory-owned requirements.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1369. Who owns security updates?

**Reconciled Answer:** Security updates owned by the technical maintainer/System Administrator, with vulnerability assessment and controlled release.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1370. Who owns database migrations?

**Reconciled Answer:** Database migrations owned by the technical maintainer and executed by the authorized System Administrator through controlled deployment.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1371. Who approves production changes?

**Reconciled Answer:** Production changes require approval by the appropriate authority: technical changes by designated technical/project authority; laboratory-rule changes by Laboratory Quality/Technical Authority; high-impact changes may require joint approval.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1372. What is the maintenance window?

**Reconciled Answer:** Maintenance window: planned and communicated, preferably outside active laboratory operating periods. Exact clock/date is deployment-specific.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1373. How are emergency fixes handled?

**Reconciled Answer:** Separate emergency software/security fixes, emergency laboratory configuration changes and emergency operational recovery; every emergency change is explicitly authorized and evidenced.
**Revision 0.8 Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Change / Release Governance

### Q1374. How are normal fixes handled?

**Reconciled Answer:** Separate emergency software/security fixes, emergency laboratory configuration changes and emergency operational recovery; every emergency change is explicitly authorized and evidenced.
**Revision 0.8 Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Change / Release Governance

### Q1375. Must every production change use the Phase → Work Package → Task → Evidence model?

**Reconciled Answer:** Separate emergency software/security fixes, emergency laboratory configuration changes and emergency operational recovery; every emergency change is explicitly authorized and evidenced.
**Revision 0.8 Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Change / Release Governance

### Q1376. How are changes to frozen architecture approved?

**Reconciled Answer:** Frozen architecture changes require formal change request, impact assessment, ADR, risk assessment, affected requirements/traceability review, approval, testing, and updated architecture baseline.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1377. How are schema changes reviewed?

**Reconciled Answer:** Schema changes require migration design, compatibility analysis, backup/recovery assessment, migration tests, rollback/recovery plan, affected-report/history assessment, and verification.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1378. How are report-template changes reviewed?

**Reconciled Answer:** Report-template changes require template versioning, content/configuration review, sample PDF regression, impact assessment on issued/historical reports, approval, and release.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1379. How are workflow changes reviewed?

**Reconciled Answer:** Workflow changes require state-model impact analysis, SoD/authorization analysis, historical-state compatibility analysis, automated tests, UAT, approval, and release.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1380. How are permission changes reviewed?

**Reconciled Answer:** Permission changes require authorization-matrix impact review, SoD review, security testing, approval, and audit of the effective change.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1381. How are formula changes reviewed?

**Reconciled Answer:** Formula changes require new FormulaVersion, technical review, golden test cases, controlled effective date, provenance, approval, and impact assessment on future vs historical calculations.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1382. How are accreditation changes reviewed?

**Reconciled Answer:** Accreditation changes require configuration/version update, effective dates, scope mapping, impact assessment, report-impact analysis, and technical/quality approval.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1383. How are backup/recovery changes reviewed?

**Reconciled Answer:** Backup/recovery changes require risk assessment, backup/restore testing, validation of RPO/RTO, documentation update, and approval before production use.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1384. How are changes validated before release?

**Reconciled Answer:** All production changes must be validated at the appropriate test level before deployment. Critical changes require full regression/validation proportional to risk.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1385. How are old migrations retained?

**Reconciled Answer:** Old migrations remain permanently retained in the repository/release history and are never rewritten after production use.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1386. How is backward compatibility handled for report/history reconstruction?

**Reconciled Answer:** Historical reconstruction remains supported through immutable revisions, versioned configurations, frozen ReportResultSnapshots, ApprovalSnapshots, DocumentVersions, and migration history. Changes must not make prior reports dependent on current mutable configuration.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1387. How is long-term Chromium/browser compatibility managed?

**Reconciled Answer:** Maintain Chromium compatibility through controlled version pinning, regression testing, and explicit supported-version records.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1388. How is Python dependency maintenance managed?

**Reconciled Answer:** Python dependencies are pinned/locked, security-reviewed, upgraded in controlled maintenance work, regression-tested, and released only after validation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1389. How is frontend dependency maintenance managed?

**Reconciled Answer:** Frontend dependencies are pinned/locked and upgraded through controlled dependency-maintenance tasks with browser/UI regression testing.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1390. How are security vulnerabilities assessed and patched offline?

**Reconciled Answer:** Security vulnerabilities assessed from vendor advisories/security databases available to the maintenance team; fixes obtained through approved offline transfer where Internet is unavailable; severity/risk assessed and patches tested before deployment.

---

# 58. Repository and Documentation Contract

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1391. What is the exact repository structure at project start?

**Reconciled Answer:** The controlled project repository baseline for implementation is:
```
project/
├── constitution.md
├── requirements.md
├── scope.md
├── architecture.md
├── domain-model.md
├── security.md
├── roadmap.md
├── current-state.md
├── active-task.md
├── handoff.md
├── open-items.md
├── traceability.md
├── work/
└── checkpoints/
```
The repository shall also contain the applicable database contract, API contract, UI contract, ADRs, work-package/task records, and checkpoint evidence required by Main_Prompt.md. This question is closed as the approved Phase 0 repository-control baseline.

**Revision 0.8 Status:** CLOSED — BASELINE — REPOSITORY CONTROL
**Primary Closure Artifact / Decision Record:** Repository / Deployment Baseline

### Q1392. Which project documents already exist?

**Reconciled Answer:** Known governing material includes the LabNexus Master Project Prompt and the defined project-control/baseline record set. Actual filesystem contents should be verified against the repository rather than assumed.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1393. Which project documents must be created before coding?

**Reconciled Answer:** Before coding: Project Charter; Roadmap; Architecture Baseline; Requirements/operating-model baseline; Active Task; Decision Register; Change Register; Risk Register; Traceability Matrix; Checkpoint Register; database/API/UI contracts at the level required for implementation; and applicable validation/test strategy.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1394. Which document is authoritative for requirements?

**Reconciled Answer:** Requirements authority: controlled Requirements Baseline / Requirements Specification. Individual source documents remain source evidence, but approved project requirements are authoritative for implementation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1395. Which document is authoritative for architecture?

**Reconciled Answer:** Architecture authority: ARCHITECTURE_BASELINE.md plus approved ADRs referenced by it.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1396. Which document is authoritative for the database contract?

**Reconciled Answer:** Database authority: controlled Database Contract / Data Model Specification, with migration scripts as the executable implementation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1397. Which document is authoritative for the API contract?

**Reconciled Answer:** API authority: controlled API Contract/OpenAPI specification generated and/or maintained from the approved backend contract.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1398. Which document is authoritative for the UI contract?

**Reconciled Answer:** UI authority: controlled UI/UX Contract and Screen Specification, supported by approved wireframes/screen definitions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1399. Which document is authoritative for current state?

**Reconciled Answer:** Current state authority: PROJECT_STATE.md.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1400. Which document is authoritative for active task?

**Reconciled Answer:** Active task authority: ACTIVE_TASK.md.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1401. Which document is authoritative for open items?

**Reconciled Answer:** Open items authority: controlled Open Items / Decision Queue register, linked to Decision/Change records.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1402. Which document is authoritative for checkpoints?

**Reconciled Answer:** Checkpoint authority: CHECKPOINT_REGISTER.md.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1403. Which document is authoritative for traceability?

**Reconciled Answer:** Traceability authority: TRACEABILITY_MATRIX.md.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1404. What is the exact naming convention for repository documents?

**Reconciled Answer:** Repository documents should use stable UPPER_SNAKE_CASE.md for top-level control documents, versioned descriptive names for specifications, and unique IDs for WPs, Tasks, Decisions, Evidence, and Checkpoints.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1405. What is the exact format for ADRs?

**Reconciled Answer:** ADR format: ADR ID; title; status; date; context; decision; alternatives considered; consequences; risks; affected components; related requirements/tasks; approval; supersedes/superseded-by.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1406. What is the exact format for work packages?

**Reconciled Answer:** Work Package format: WP ID; phase; objective; scope; exclusions; inputs; outputs/deliverables; dependencies; acceptance criteria; tasks; risks; evidence; checkpoint; owner; status.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1407. What is the exact format for tasks?

**Reconciled Answer:** Task format: Task ID; parent WP; objective; scope; prerequisites; authorized work; implementation steps; acceptance criteria; tests; evidence; dependencies; status; completion record.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1408. What is the exact format for evidence records?

**Reconciled Answer:** Evidence record: Evidence ID; source task/requirement; environment/version; date/time; actor; procedure/test; expected; actual; artifact references; result; reviewer; disposition.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1409. What is the exact format for checkpoints?

**Reconciled Answer:** Checkpoint record: Checkpoint ID; scope; inputs; required deliverables; evidence summary; defects/deviations; traceability status; decision; approver; date; resulting project state/baseline.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1410. What is the exact status vocabulary used in project records?

**Reconciled Answer:** Keep project/task progression, document/configuration lifecycle and approval disposition as separate vocabularies.
**Revision 0.8 Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Project Control Model

### Q1411. Who may edit controlled project documents?

**Reconciled Answer:** Controlled project documents editable only by authorized project contributors; approval authority is separate where independence is required.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1412. How are document changes reviewed and approved?

**Reconciled Answer:** Material document changes require review, version/history, approval where controlled, and linkage to the relevant Task/Decision/Change record.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1413. Is Git the authoritative version-control system?

**Reconciled Answer:** Yes. Git is the authoritative version-control system for project source and controlled repository documents.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1414. What branch/merge policy is used?

**Reconciled Answer:** Recommended policy: protected main as authoritative; short-lived task/feature branches; merge only after required tests/review; no direct production changes outside repository control.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1415. Are commits required to reference Task IDs?

**Reconciled Answer:** Yes. Commits for controlled work should reference the relevant Task ID.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1416. Are release tags required?

**Reconciled Answer:** Yes. Release tags are required for production releases.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1417. Is a changelog required?

**Reconciled Answer:** Yes. A changelog/release-notes record is required.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1418. Is an ADR required for every material architectural decision?

**Reconciled Answer:** Yes. Every material architectural decision requires an ADR. Minor implementation details do not require ADRs unless they materially alter an existing architectural decision.

---

# 59. Phase and Work-Package Readiness

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1419. What exactly must be completed in Phase 0 before Phase 1 can start?

**Reconciled Answer:** Before Phase 1 starts, Phase 0/project-control prerequisites must include: project charter/control rules; governance/roles; roadmap; repository contract; baseline status model; decision/change/risk registers; task authorization rules; traceability approach; and explicit project scope/exclusions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1420. What exact deliverables define completion of each phase?

**Reconciled Answer:** Each phase is complete only when its defined deliverables + acceptance criteria + tests/evidence + verification + approved checkpoint + baseline update are complete.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1421. What dependencies cross phase boundaries?

**Reconciled Answer:** Cross-phase dependencies must be explicitly recorded in roadmap/WP records and traceability; later phases cannot silently assume unresolved predecessor decisions.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1422. Which phases may overlap safely?

**Reconciled Answer:** Documentation, governance, test preparation, security review, and some technical foundation work may overlap when their dependencies are satisfied.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1423. Which phases must remain strictly sequential?

**Reconciled Answer:** Requirements that establish foundational behavior, architecture, data integrity, workflow/state semantics, and critical security controls should remain sequential before dependent implementation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1424. What makes a Work Package ready for task refinement?

**Reconciled Answer:** WP ready for task refinement when objective, scope, exclusions, inputs, outputs, dependencies, acceptance criteria, risks, and required decisions are sufficiently specified.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1425. What makes a Task ready for authorization?

**Reconciled Answer:** Task ready for authorization when scope and acceptance criteria are clear, dependencies resolved, required inputs available, risks understood, and implementation can proceed without material ambiguity.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1426. Who authorizes a Task?

**Reconciled Answer:** Task authorized by the designated Project/Technical authority, according to project governance. The authorization does not substitute for laboratory approval of laboratory-specific technical rules.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1427. What evidence must exist before a Task can be marked complete?

**Reconciled Answer:** Task completion requires implementation evidence, test evidence, documentation updates, traceability updates, defect/deviation disposition, and reviewer/verification evidence appropriate to the task.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1428. What evidence must exist before a Work Package can be closed?

**Reconciled Answer:** WP closure requires all tasks complete/accepted, deliverables complete, evidence indexed, open issues dispositioned, risks updated, traceability complete, and WP acceptance recorded.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1429. What evidence must exist before a Phase checkpoint can be accepted?

**Reconciled Answer:** Phase checkpoint requires accepted phase deliverables, verification evidence, traceability, risk/decision/change updates, reproducible baseline bundle, and formal checkpoint decision.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1430. Which known open questions block coding?

**Reconciled Answer:** Coding blockers include unresolved decisions affecting data identity, workflow/state model, authorization/SoD, result/revision semantics, launch tests/methods/parameters/formulas, report content, critical QC rules, retention, security model, and other behavior that cannot safely be inferred.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1431. Which open questions can safely be deferred?

**Reconciled Answer:** Safe deferrals include future disciplines, optional email/SMS, advanced BI, public API, mobile workflow, enterprise integrations, advanced inventory, and other explicitly excluded v1 functionality.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1432. What is the maximum acceptable unresolved decision debt before implementation begins?

**Reconciled Answer:** No arbitrary percentage. Material unresolved decision debt must be zero for the requirements that a coding task depends upon. Project-wide decision debt may remain only where it is explicitly classified as deferred and cannot affect current implementation.

---

# 60. State and Completion Semantics

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1433. What exactly does SPECIFIED mean for this project?

**Reconciled Answer:** SPECIFIED = requirement/scope is sufficiently defined and approved for planning; required assumptions/open decisions are resolved to the level needed for the next step. No implementation authorization is implied.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1434. What exactly does PLANNED mean?

**Reconciled Answer:** PLANNED = work has been decomposed and scheduled/placed in the roadmap/WP/task structure, but coding or execution is not authorized.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1435. What exactly does AUTHORIZED mean?

**Reconciled Answer:** AUTHORIZED = a specific Task or controlled action is formally authorized to proceed. Authorization must identify scope, owner, and applicable acceptance criteria.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1436. What exactly does IN PROGRESS mean?

**Reconciled Answer:** IN_PROGRESS = authorized work has actually started and remains unfinished.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1437. What exactly does IMPLEMENTED mean?

**Reconciled Answer:** IMPLEMENTED = scoped implementation has been completed and is ready for testing; it is not yet necessarily verified or accepted.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1438. What exactly does TESTED mean?

**Reconciled Answer:** TESTED = required tests have been executed and results recorded; successful testing alone does not equal formal verification.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1439. What exactly does VERIFIED mean?

**Reconciled Answer:** VERIFIED = objective evidence has been independently evaluated against the acceptance criteria and found satisfactory.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1440. What exactly does ACCEPTED mean?

**Reconciled Answer:** ACCEPTED = authorized acceptance authority has accepted the verified deliverables, including approved deviations where applicable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1441. What exactly does RELEASED mean?

**Reconciled Answer:** RELEASED = an accepted software/document/configuration package has been formally versioned and approved for deployment/use.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1442. What exactly does DEPLOYED mean?

**Reconciled Answer:** DEPLOYED = the released version has actually been installed/configured in the target environment.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1443. What exactly does HEALTH VERIFIED mean?

**Reconciled Answer:** HEALTH_VERIFIED = post-deployment health/smoke/operational checks demonstrate that the deployed environment is functioning as required.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1444. Can a state be skipped?

**Reconciled Answer:** A state may be skipped only when it is genuinely not applicable, and the omission must be explicit and evidenced. Required verification/acceptance states cannot be bypassed merely for convenience.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1445. Who may transition each state?

**Reconciled Answer:** Project-control state transitions are made by the designated task/WP/phase authority according to governance; technical status changes by technical owners must not create false acceptance.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1446. What evidence is required for each transition?

**Reconciled Answer:** Every transition requires the evidence appropriate to that state, recorded in the task/WP/checkpoint record.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1447. Can a state be reverted?

**Reconciled Answer:** A state may be superseded/reopened through a controlled action, but historical state transitions are never erased.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1448. What happens when a checkpoint is REJECTED?

**Reconciled Answer:** REJECTED checkpoint: acceptance denied; deficiencies recorded; corrective work defined; predecessor/target state remains clear; new evidence required before resubmission.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1449. What happens when a checkpoint is BLOCKED?

**Reconciled Answer:** BLOCKED checkpoint: work cannot proceed due to an unresolved dependency/decision/risk; blocker is explicitly recorded and no false completion state is assigned.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1450. How are exceptions recorded without falsely marking work complete?

**Reconciled Answer:** Exceptions are recorded as deviations/issues/change records and linked to affected tasks/evidence. They do not change the underlying completion state unless formally accepted.

---

# 61. Historical Reconstruction Test — Exact Acceptance Questions

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1451. Can the system identify the exact Customer for a TestInstance?

**Reconciled Answer:** Yes. Historical reconstruction shall identify the exact Customer through immutable relational identity, not through the Customer's current display values alone.
The TestInstance shall remain traceable through its TestRequest/Project relationship to the exact Customer record. Where report-visible Customer information may subsequently change, the required historical display representation shall also be captured in the applicable controlled report snapshot or equivalent historical record.
Changing a customer's current name, address, or contact details shall therefore not rewrite the historical identity presented by an already-issued report.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1452. Can the system identify the exact Project/Request?

**Reconciled Answer:** Yes. The reconstruction chain shall retain the exact Project/Contract and Request identities associated with the TestInstance.
The implementation shall distinguish stable relational identity from mutable descriptive fields. Required historical report-visible representations shall be frozen in the appropriate snapshot so that later renaming or administrative edits cannot alter the reconstruction of an earlier issued state.
Historical reconstruction shall use the exact identifiers and effective historical relationships that existed for the event being reconstructed.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1453. Can the system identify the exact Sample and sample identity history?

**Reconciled Answer:** Yes. The reconstruction shall identify the exact Sample record and its controlled identity history.
Sample identifiers, laboratory numbering, customer-provided identifiers, aliases, relabeling events, corrections, and other identity changes shall be represented through controlled historical records rather than destructive overwriting.
The reconstruction shall be able to show which Sample identity applied at the relevant stage and which representation was used on the relevant report or controlled record.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1454. Can the system identify the exact TestDefinition?

**Reconciled Answer:** Yes. Each TestInstance shall retain an explicit reference to the exact TestDefinition used for the work.
A later change to the technical meaning, parameter set, reporting behavior, or workflow semantics of a TestDefinition shall not silently alter the historical interpretation of an existing TestInstance. Such changes shall be handled through controlled versioning, effective dating, or creation of a new controlled definition as required by the governing configuration model.
The report snapshot shall preserve the report-visible TestDefinition identity/name required for historical reconstruction.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1455. Can the system identify the exact MethodVersion?

**Reconciled Answer:** Yes. The exact MethodVersion applicable to the TestInstance shall be deterministically identifiable and preserved.
The TestInstance shall derive its technical method through the approved relationship to TestDefinition and MethodVersion rather than relying on the Method's current "latest" state.
MethodVersion changes shall be controlled and effective-dated. Historical records shall continue to resolve to the MethodVersion that actually governed the work.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1456. Can the system identify the exact ParameterDefinitions used?

**Reconciled Answer:** Yes. Each calculation/result pathway shall be able to identify the exact controlled ParameterDefinitions that supplied the technical meaning of the parameters used.
Parameter identity shall not depend solely on current labels or mutable names. Where the definition's meaning, unit semantics, validation behavior, or reporting significance changes, the applicable controlled definition/version shall be identifiable as part of the historical configuration.
Calculation evidence and report reconstruction shall therefore be based on the parameter definitions actually used, not whatever parameter configuration happens to be current at the time of reconstruction.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1457. Can the system identify the exact analyst(s)?

**Reconciled Answer:** Yes. Analyst identity shall be captured by stable user identity linked to the relevant TestInstance/assignment/execution evidence.
Historical reconstruction shall not depend on the current name, role, status, or active/inactive state of the user account. The historical event shall preserve the identity of the person who performed the action together with its timestamp and authorization context.
Where a visible human-readable name or role is required for historical rendering, that historical representation shall be preserved as part of the appropriate evidence/snapshot rather than reconstructed from mutable current user-profile data.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1458. Can the system identify the exact equipment used?

**Reconciled Answer:** Yes. Each equipment use relevant to controlled testing shall be explicitly attributable to the exact Equipment identity.
Equipment records shall remain stable even when equipment undergoes calibration, maintenance, relocation, qualification, status changes, or retirement.
Historical TestInstance reconstruction shall identify the equipment actually associated with the work and the relevant evidence of its status and eligibility at the time of use.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1459. Can the system determine equipment eligibility as-of the test activity?

**Reconciled Answer:** Yes. Eligibility shall be determined against the historical state applicable at the **actual test activity timestamp**, not against the equipment's present-day state.
The determination shall consider the controlled effective histories relevant to the laboratory policy, including applicable calibration, maintenance, qualification, verification, status, authorization, and any method/test-specific equipment restrictions.
The system shall preserve sufficient evidence to reproduce the eligibility decision, including the effective historical records or an explicit recorded eligibility evaluation where required. A currently calibrated or currently authorized equipment record shall never be used to retroactively justify an earlier activity.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1460. Can the system identify every observation used?

**Reconciled Answer:** Yes. Each observation participating in a result or calculation shall be independently identifiable and traceable to its TestInstance/parameter context.
The calculation pathway shall reference the exact observation records or immutable observation snapshots used. Corrections shall preserve prior observation history rather than replacing the evidence needed to explain an earlier calculation.
Historical reconstruction shall therefore be able to distinguish the observations used in the original result from observations introduced by subsequent correction or rework.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1461. Can the system identify every calculation input?

**Reconciled Answer:** Yes. Every CalculationRun shall preserve a controlled input snapshot sufficient to reconstruct the inputs actually supplied to the calculation engine.
The snapshot shall identify the contributing observations/values, units and relevant normalized representations, parameter identities, constants or dependencies, and any other controlled input that materially affected the calculation.
The system shall not rely on rereading the current state of source records to infer what was calculated previously.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1462. Can the system identify the exact FormulaVersion?

**Reconciled Answer:** Yes. Every CalculationRun shall reference the exact immutable FormulaVersion used.
A FormulaVersion shall never be edited in place when the technical calculation behavior changes. A new controlled FormulaVersion shall be created and linked to the effective configuration.
Historical reconstruction shall therefore use the exact FormulaVersion identifier stored by the CalculationRun, together with its controlled definition and engine compatibility information.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1463. Can the system identify the exact CalculationRun?

**Reconciled Answer:** Yes. Every persisted calculated result shall be traceable to its exact CalculationRun.
The CalculationRun shall act as the immutable evidence boundary for the calculation event, including input snapshot, FormulaVersion, dependencies, calculation engine/version information, execution time, actor/process identity, and resulting output linkage.
A recalculation shall create a distinct CalculationRun rather than silently modifying the prior calculation evidence.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1464. Can the system identify the exact ResultRevision?

**Reconciled Answer:** Yes. Historical result reconstruction shall identify the precise ResultRevision associated with the state being reconstructed.
Correction revisions and ApprovalSnapshot revisions shall remain explicitly typed and separately attributable. The current live Result state shall not be treated as sufficient historical evidence.
Where a report was issued from an approved result, its ReportResultSnapshot shall reference the exact Result and ResultRevision used for that report state.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1465. Can the system identify the exact review event?

**Reconciled Answer:** Yes. The exact review action shall be represented by the authoritative approval/workflow event structure.
The event shall preserve the affected TestInstance/record identity, actor, action, timestamp, resulting workflow state, relevant authorization context, and associated controlled evidence.
Historical reconstruction shall identify the actual review event that applied to the relevant result state, rather than inferring review from the fact that a record is currently marked reviewed.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1466. Can the system identify the exact verification event?

**Reconciled Answer:** Yes. The exact verification event shall be independently attributable and linked to the controlled record and workflow state it verified.
The reconstruction shall identify the verifier, event timestamp, affected TestInstance/result state, authorization context, and any required decision/evidence metadata.
A later verification shall not overwrite the evidence of an earlier verification event.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1467. Can the system identify the exact approval event?

**Reconciled Answer:** Yes. The **approval_chain_event** remains the authoritative source of approval history.
The reconstruction shall identify the exact approval event, the approved record/state, authorized signatory identity, approval timestamp, relevant authentication/reauthentication evidence, and resulting state transition.
Current user-account status shall not determine whether a historical approval existed. Disabling an account later shall not erase or invalidate the historical event.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1468. Can the system identify the exact ApprovalSnapshot?

**Reconciled Answer:** Yes. Every successful Approval shall create an immutable **ApprovalSnapshot** representing the approved technical/result state at that time.
The ApprovalSnapshot shall be independently identifiable and linked to the approval event and applicable ResultRevision(s). It shall preserve the state required to establish exactly what was approved, rather than relying on the later live Result.
Historical report and result reconstruction shall use the specific ApprovalSnapshot associated with the relevant approval path.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1469. Can the system identify the accreditation-scope state that applied?

**Reconciled Answer:** Yes. The reconstruction shall identify the exact accreditation-scope determination applicable to the work at the relevant time.
The determination shall preserve whether scope was resolved from the MethodVersion default or a TestDefinition override, the applicable effective interval/version, the resolved accreditation representation, and the source of that determination.
The report-visible representation shall be frozen in the relevant snapshot. Later changes to accreditation-scope configuration shall not silently change the historical classification of an issued report.
LabNexus shall represent the laboratory's approved accreditation data and process; it shall not itself be represented as conferring accreditation.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1470. Can the system identify the exact ReportRevision?

**Reconciled Answer:** Yes. Every report state that becomes part of controlled report history shall have an explicit ReportRevision identity.
The reconstruction shall identify the exact revision number/identity, associated report snapshots, approval/result basis, document version, artifact state, issuance status, and relevant audit history.
The system shall not rebuild a historical ReportRevision merely by rerendering the current report template against current data.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1471. Can the system identify every ReportResultSnapshot?

**Reconciled Answer:** Yes. Every report-visible result included in a ReportRevision shall be represented by an explicit ReportResultSnapshot.
The snapshot shall retain the exact `report_revision_id`, `result_id`, and `result_revision_id`, together with the report-visible value, unit, TestDefinition representation, accreditation representation, analyst representation, approval timestamp, and other frozen fields required by report policy.
This makes the report state independent of later corrections to the underlying live Result.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1472. Can the system identify the exact DocumentVersion?

**Reconciled Answer:** Yes. A controlled report/document shall reference the exact DocumentVersion used for the applicable report revision or controlled document state.
DocumentVersion identity shall be immutable after publication. Updating a controlled document shall create a new version rather than editing the content in place.
Historical reconstruction shall therefore resolve the precise version that governed the document/report state at the relevant time.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1473. Can the system retrieve the exact issued PDF?

**Reconciled Answer:** Yes. The exact issued PDF shall be retained as the authoritative historical artifact.
The stored artifact shall have a SHA-256 hash and controlled document/artifact identity sufficient to retrieve and verify the exact bytes that were issued.
Historical reconstruction shall retrieve the preserved PDF rather than silently regenerating it from the current template, current Chromium runtime, or current data. Rerendering may be used for comparison/testing but is not the source of truth for the original issued artifact.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1474. Can the system identify the relevant audit events?

**Reconciled Answer:** Yes. Relevant audit events shall be traceable through the controlled entity/action/reference relationships associated with the reconstructed record.
The audit trail shall include the material lifecycle events needed to explain creation, assignment, execution, correction, review, verification, approval, report generation/issuance, configuration impact, and other controlled changes.
Routine reads need not automatically create audit entries unless specifically classified as sensitive/auditable access. Where a read/download/export is designated auditable, the resulting event shall remain linked to the relevant resource.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1475. Can the complete reconstruction be produced without relying on current mutable state?

**Reconciled Answer:** Yes. This is a mandatory architectural invariant.
Historical reconstruction shall use immutable identifiers, effective-dated configuration, immutable workflow/audit events, calculation evidence, ResultRevision records, ApprovalSnapshots, ReportResultSnapshots, controlled DocumentVersions, and preserved issued artifacts.
Current mutable user profiles, current configuration, current method versions, current accreditation settings, current equipment status, or current report templates shall not be required to reproduce an already-issued historical state.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1476. Can the reconstruction distinguish the original issued state from later corrections?

**Reconciled Answer:** Yes. The distinction shall be explicit through ResultRevision, ApprovalSnapshot, ReportRevision, ReportResultSnapshot, workflow/audit events, and preserved PDF artifacts.
A later correction shall create a controlled new result state and follow the required review/verification/approval process. It shall not rewrite the original approved or issued state.
The system shall therefore be able to show both the earlier issued state and the later corrected/reapproved state, including the relationship between them.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1477. Can ReportRevision 1 still be reconstructed after later result correction and reapproval?

**Reconciled Answer:** Yes. This shall be an explicit verification requirement.
The reconstruction test shall create and issue ReportRevision 1, subsequently correct a relevant result, complete the required review/verification/approval workflow, and create a later report revision.
After the correction, the system shall still reproduce ReportRevision 1 from its own snapshots and preserved PDF without consulting the later live Result state. The original artifact hash shall remain unchanged.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1478. Can ReportRevision 2 be reconstructed independently?

**Reconciled Answer:** Yes. ReportRevision 2 shall have its own complete report-result snapshot state and exact document/artifact linkage.
Its reconstruction shall depend on the controlled state intentionally included in Revision 2, not on mutable current fields or an assumption that the report can be recomputed from today's data.
The evidence shall demonstrate that Revision 1 and Revision 2 can each be reconstructed independently and that the two states remain distinguishable.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1479. What is the formal test procedure for this reconstruction?

**Reconciled Answer:** The formal verification procedure shall use at least the following sequence:
1. Create a controlled Sample/TestInstance and complete the required execution, calculation, review, verification, and approval workflow.
2. Issue ReportRevision 1 and record its ReportRevision identity, ReportResultSnapshots, DocumentVersion, PDF hash, approval events, and relevant audit events.
3. Change a result through the approved correction/reopen process.
4. Recalculate as required, creating a new CalculationRun and ResultRevision.
5. Complete new review, verification, and approval steps and issue ReportRevision 2.
6. Reconstruct Revision 1 from stored historical state and verify its frozen values, relationships, visible configuration, and exact PDF hash.
7. Reconstruct Revision 2 independently and verify its own frozen state and artifact hash.
8. Change current mutable customer/user/configuration data and repeat the reconstruction; the historical results must remain unchanged.
9. Verify that prohibited destructive edits or missing historical dependencies cause the verification to fail rather than being silently substituted.

The procedure shall produce a controlled verification record with expected results, actual results, evidence references, anomalies, tester identity, and independent acceptance.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1480. Who accepts the reconstruction evidence?

**Reconciled Answer:** The **Technical Authority** shall review the technical correctness of the reconstruction.
The **Quality Authority** shall verify the integrity, completeness, traceability, and adequacy of the evidence as a controlled quality/validation record.
The **Project Owner / Laboratory Business Owner** shall provide final project-level acceptance where the reconstruction test forms part of release or validation acceptance.
The person executing the test shall not be the sole authority for accepting the evidence.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1481. What laboratory policy is currently unknown?

**Reconciled Answer:** No additional laboratory policy shall be invented to close this question.
The technical decision is that any laboratory-policy dependency not already explicitly approved in the project baseline shall be recorded as an **unresolved policy input** with an owner, required decision authority, and affected system behavior.
Coding may proceed only where the implementation is independent of that unresolved policy. Where behavior would materially differ according to the missing laboratory policy, the affected behavior shall remain non-deployable until the policy is approved.
This prevents a developer-selected default from becoming an uncontrolled laboratory rule.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1482. What workflow rule is currently unknown?

**Reconciled Answer:** The common controlled workflow already forms the baseline, but any unconfirmed exceptional workflow rule shall remain explicitly unresolved.
Examples include method-specific rework, retest, reopening, cancellation, nonconforming-work disposition, or unusual approval transitions where the governing laboratory procedure has not yet been finalized.
Until such a rule is approved, the implementation shall not silently infer a permissive transition. Existing hard controls, including authorization and hard same-TestInstance SoD restrictions, remain mandatory. Policy-dependent transitions shall default to **blocked/not activatable** rather than being improvised.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1483. What approval rule is currently unknown?

**Reconciled Answer:** Any approval prerequisite or authority detail not already established by the approved baseline shall remain an explicit controlled dependency.
The baseline approval model remains authoritative: approval must be attributable to an authorized person, linked to the exact record/state, recorded in the approval chain, and subject to the approved SoD rules.
Where a laboratory-specific approval condition is still unknown, LabNexus shall not invent it or allow a generic bypass. The missing rule shall be captured as a decision item and incorporated through controlled configuration after approval and verification.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1484. What SoD rule is currently unknown?

**Reconciled Answer:** The already-approved hard SoD rules remain fixed and shall not be weakened by this unresolved-item category.
The unresolved portion is limited to **policy-controlled** relationships or exceptional approval arrangements that the laboratory has not yet explicitly decided.
Until such a rule is approved, the conservative behavior shall be **BLOCK** for the potentially conflicting transition. No user interface, administrative override, emergency path, or generic configuration shall convert a hard-block conflict into an allowed action.
Approved policy-controlled exceptions shall be represented through the effective-dated SoD Matrix with competence, authority, independence, justification, and evidence requirements.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1485. What accreditation rule is currently unknown?

**Reconciled Answer:** No unsupported accreditation rule shall be inferred.
The technical baseline already defines the mechanism: MethodVersion carries the normal accreditation-scope default, an approved TestDefinition override may apply where authorized, precedence is deterministic, effective dating is explicit, and the resolved representation is preserved for historical reconstruction.
Any laboratory-specific rule about which methods/tests are included in the accredited scope must come from the approved accreditation/scope information supplied by the laboratory. Until such information exists for a given configuration, the affected scope state shall not be assumed to be accredited merely because the method or test exists in LabNexus.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1486. What calculation rule is currently unknown?

**Reconciled Answer:** No calculation behavior shall be invented when the laboratory-approved technical rule is absent.
Calculation execution shall require a controlled FormulaVersion and its approved technical inputs, including applicable units, constants, transformations, precision/rounding behavior, validation rules, and invalid-input handling where those behaviors materially affect the result.
Where a required calculation rule is not yet approved, the corresponding FormulaVersion shall remain unavailable for controlled production use. A developer-selected formula, rounding rule, unit conversion, or exception behavior shall not become the de facto laboratory method.
Each activated calculation rule shall therefore have an explicit technical owner, controlled version, verification evidence, and traceable linkage to the TestDefinition/MethodVersion it governs.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1487. What report-content rule is currently unknown?

**Reconciled Answer:** Report content shall be governed by a **controlled ReportDefinition/ReportTemplate and ReportRevision model**, rather than by mutable application code or ad-hoc template behavior.

For each controlled report type, the approved definition shall establish, as applicable:
* report identity and revision structure;
* required customer/project/sample/test identification;
* TestDefinition and MethodVersion representation;
* parameter/result presentation;
* units and approved formatting;
* analyst and approval representations;
* accreditation representation;
* required disclaimers/notes;
* report numbering and revision numbering;
* issuance/withdrawal rules;
* controlled PDF generation behavior.

Any item that materially affects the technical or contractual meaning of an issued report shall be version-controlled and historically reconstructable.
Where a report-content requirement has not yet been approved for a particular report type, that element shall not be invented by the implementation team. The report type shall either use an already-approved default or remain unavailable for controlled issuance until its content definition is approved.
Every issued report shall retain the exact ReportRevision, ReportResultSnapshots, DocumentVersion, and issued PDF artifact required to reconstruct what was actually issued.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1488. What QC rule is currently unknown?

**Reconciled Answer:** QC behavior shall be controlled through the approved QC configuration model and shall not be embedded as undocumented application assumptions.

For each applicable QC rule, the controlled definition shall identify, as required:
* QC type and applicability;
* acceptance criteria;
* required parameters/limits;
* evaluation method;
* effective date/version;
* failure state;
* blocking or non-blocking behavior;
* required investigation/disposition;
* escalation/notification requirements;
* evidence and approval requirements.

The already-approved baseline permits QC failures to affect workflow where the configured rule requires blocking or controlled disposition. The exact laboratory acceptance limits and test-specific QC requirements must come from the laboratory's approved procedures/methods.
Where a QC rule has not yet been supplied or approved for a particular test/method, the system shall not invent an acceptance criterion. The affected QC control shall remain inactive or the affected workflow shall remain blocked from controlled production use, depending on the risk and applicability.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1489. What equipment-enforcement rule is currently unknown?

**Reconciled Answer:** Equipment enforcement shall be implemented as a **controlled, configurable policy**, while preserving a mandatory technical baseline.

The system shall be able to determine whether equipment was eligible for a TestInstance based on the applicable historical state, including where relevant:
* equipment status;
* calibration validity;
* maintenance state;
* qualification/verification state;
* authorized-user restrictions;
* method/test-specific applicability;
* effective dates;
* any laboratory-approved blocking condition.

For each applicable equipment rule, the configuration shall explicitly define whether a failed eligibility condition:
* blocks assignment;
* blocks execution;
* permits execution with documented exception;
* requires supervisor/technical authorization;
* creates a mandatory investigation/disposition record.

No unapproved implementation default shall silently determine laboratory policy.
The mandatory baseline remains that the system must not represent equipment as eligible solely because its **current** state is valid. Historical eligibility must be evaluated as-of the relevant activity timestamp.
Where the laboratory has not yet selected the enforcement level for a particular equipment category or method, the safest controlled behavior shall be to prevent the affected controlled action until the applicable policy is approved, unless an already-approved laboratory procedure expressly provides an alternate path.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1490. What record-retention rule is currently unknown?

**Reconciled Answer:** The current retention baseline is **10 years for controlled laboratory records, audit records, and issued reports/PDFs**, followed by controlled archival rather than automatic deletion.

The technical implementation shall therefore support:

* retention classification;
* retention start/reference event;
* effective retention period;
* archive state;
* controlled retrieval;
* read-only archived records;
* preservation of issued PDFs and associated evidence;
* auditability of material archive actions;
* legal/quality hold capability where separately required;
* controlled destruction only after the applicable retention and hold conditions are satisfied.

Retention must apply to the complete record set needed for reconstruction, not merely the primary database row. This includes relevant audit history, result/revision history, approval evidence, report snapshots, controlled document versions, and issued artifacts.

The system shall not automatically destroy records merely because a nominal retention period has elapsed if a documented legal hold, investigation, quality requirement, or other approved preservation condition applies.

Any future change to the laboratory's retention period shall be a controlled policy/configuration change with an effective date. It shall not retroactively alter the retention history of previously governed records or permit historical issued artifacts to be silently removed.

The technical design shall remain independent of the eventual physical archive tier: archived information may remain in the active controlled store or move to an approved offline/cold archival medium, provided identity, integrity, custody, and retrievability are preserved.

**Revision 0.8 Status:** CLOSED — RECONCILED BASELINE

### Q1491. What backup/recovery rule is currently unknown?

**Reconciled Answer:** Core backup/recovery policy is resolved for v1: controlled Recovery Sets, at least three retained copies, at least two rotating removable/offline copies, encryption for removable/offline backups, quarterly restore testing, and defined RPO/RTO targets. Remaining machine-specific paths, schedules, media serial numbers, and custodial details are deployment inputs and may be finalized in Phase 17 without reopening the architecture.

**Revision 0.8 Status:** CLOSED — GOVERNANCE CLASSIFICATION

### Q1492. What permission rule is currently unknown?

**Reconciled Answer:** The permission model baseline is resolved as RBAC plus backend authorization plus per-TestInstance SoD, with hard blocks having no bypass. The detailed role/permission matrix is a Phase 6 controlled artifact and must be accepted before affected production workflows are enabled.

**Revision 0.8 Status:** CLOSED — GOVERNANCE CLASSIFICATION

### Q1493. What configuration-governance rule is currently unknown?

**Reconciled Answer:** Configuration governance is resolved as typed relational configuration with proposal → approval → effective configuration, plus the bounded visible/countersigned emergency path with expiry and retrospective review. Individual configuration-object definitions may be finalized by their relevant work package.

**Revision 0.8 Status:** CLOSED — GOVERNANCE CLASSIFICATION

### Q1494. What user-training rule is currently unknown?

**Reconciled Answer:** User training is a deployment/validation requirement, not a pre-coding architecture blocker. Training scope, competency evidence, role-specific curricula, and training records shall be defined before production use and verified during validation/deployment.

**Revision 0.8 Status:** CLOSED — GOVERNANCE CLASSIFICATION

### Q1495. What security rule is currently unknown?

**Reconciled Answer:** The core v1 security baseline is resolved: Argon2id, server-side sessions, secure cookies, CSRF protection, session lifecycle controls, backend authorization, SoD, controlled secrets, host/filesystem protection, backup encryption, and incident controls. Detailed host-hardening and deployment-security procedures are Phase 18/19 work.

**Revision 0.8 Status:** CLOSED — GOVERNANCE CLASSIFICATION

### Q1496. What deployment/operations rule is currently unknown?

**Reconciled Answer:** Deployment and operations are controlled by the approved Windows single-host topology, local SQLite rules, Caddy/FastAPI/React stack, controlled update sequence, backup/recovery model, and Phase 17–19 procedures. Exact host names, paths, service accounts, scheduled-task identities, and production filesystem locations are deployment inputs.

**Revision 0.8 Status:** CLOSED — GOVERNANCE CLASSIFICATION

### Q1497. Which unknowns may be safely deferred?

**Reconciled Answer:** The following may safely be deferred without reopening the core architecture: deployment-specific paths/host details; exact training schedules; future discipline rules not required at launch; future commercial charging; future integration details; non-v1 reporting features; and other explicitly marked Phase 17–20 operational details, provided no safety/integrity control is weakened.

**Revision 0.8 Status:** CLOSED — GOVERNANCE CLASSIFICATION

### Q1498. Which unknowns would make coding unsafe or ambiguous?

**Reconciled Answer:** Coding is unsafe or ambiguous when an unresolved item would change data integrity, authorization, hard SoD, historical reconstruction, report authority, calculation meaning, accreditation representation, mandatory QC/equipment blocking, security boundary, or controlled retention behavior. Such items must remain blocked until formally decided.

**Revision 0.8 Status:** CLOSED — GOVERNANCE CLASSIFICATION

### Q1499. Which unknowns require a formal ADR?

**Reconciled Answer:** A formal ADR is required for an architectural or cross-cutting technical decision that changes a frozen baseline, creates a new invariant, changes a security/data-integrity boundary, or resolves a significant implementation alternative with long-term consequences.

**Revision 0.8 Status:** CLOSED — GOVERNANCE CLASSIFICATION

### Q1500. Which unknowns require a Laboratory Decision record?

**Reconciled Answer:** A Laboratory Decision record is required when the unresolved matter is a laboratory policy, workflow, acceptance criterion, approval authority, QC rule, equipment-enforcement policy, confidentiality/retention policy, or other domain rule owned by laboratory management/quality/technical authority.

**Revision 0.8 Status:** CLOSED — GOVERNANCE CLASSIFICATION

### Q1501. Which unknowns require a Technical Decision record?

**Reconciled Answer:** A Technical Decision record is required when the unresolved matter concerns implementation behavior, schema/invariant choice, security mechanism, performance target, deployment mechanism, software/runtime baseline, or other technical behavior requiring explicit engineering acceptance.

**Revision 0.8 Status:** CLOSED — GOVERNANCE CLASSIFICATION

### Q1502. Which unknowns require joint approval?

**Reconciled Answer:** Joint approval is required where a decision simultaneously affects laboratory policy and technical implementation, especially accreditation representation, SoD policy, controlled workflow, QC/equipment enforcement, report authority, retention/recovery, or security controls. Such decisions require the relevant Laboratory/Quality/Technical authority plus the responsible project/technical authority before becoming effective controlled behavior.

**Revision 0.8 Status:** CLOSED — GOVERNANCE CLASSIFICATION

## Validation

Questions: **1502/1502**
Answers: **1502/1502**
Revision 0.8 explicit statuses: **1502/1502**
Implementation blockers remaining in this pre-coding question set: **0**
Unresolved conflict statuses remaining: **0**
Unresolved proposed-default statuses remaining: **0**
Unresolved laboratory-decision statuses remaining: **0**
Unresolved technical-decision statuses remaining: **0**
Unresolved deployment-input statuses remaining: **0**

### R0.8 Acceptance Statement

Revision 0.8 is the **accepted pre-coding decision baseline** for the 1,502-question reconciliation set.

It closes the remaining decision blockers identified in the prior working baseline and establishes explicit treatment of items that are safely deferred to later phases.

This document does **not** itself authorize implementation. Implementation remains governed by Main_Prompt.md and requires the controlled sequence:

```
PROJECT
→ PHASE
→ WORK PACKAGE
→ AUTHORIZED TASK
→ IMPLEMENTATION
→ TEST
→ VERIFICATION
→ EVIDENCE
→ CHECKPOINT
```

Any later change to an R0.8 decision must be processed through the applicable controlled change / ADR / Laboratory Decision / Technical Decision / joint approval mechanism and must not silently alter effective controlled behavior.
