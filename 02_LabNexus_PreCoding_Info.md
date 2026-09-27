# LabNexus Pre-Coding Questions — Complete Q1–Q1502

**Compilation status:** COMPLETE SOURCE-BASED RECONCILIATION AND DECISION CLOSURE

**Baseline:** Accepted pre-coding decision baseline — ready for Phase 0 baseline / authorized-task creation

**Historical source:** Earlier working baselines remain preserved in repository history; this document is the current consolidated question/answer presentation.

The original question wording and numbering are preserved.  controls supersede contradictory or incomplete source answers for affected questions; unaffected questions retain their source answers.

## Decision Closure Register

The controlling decision register closes the identified pre-coding contradictions and ambiguities and defines the current treatment of controlled deferrals and authority-owned inputs.

### Closure rules

1. Every Q1–Q1502 has an answer and an explicit status.
2. No question remains in an unresolved **LABORATORY DECISION REQUIRED**, **TECHNICAL DECISION REQUIRED**, **PROPOSED DEFAULT — PENDING APPROVAL**, **CONFLICT — REQUIRES RESOLUTION**, or **DEPLOYMENT INPUT** state.
3. Questions governed by later project phases are treated as controlled deferrals rather than missing decisions.
4. Commercial charge calculation is explicitly deferred from v1; invoicing, accounts receivable, payments, and tax/accounting remain external.
5. The approved security defaults are now controlled baseline decisions.
6. Equipment-status vocabulary and transition semantics are now controlled baseline decisions.
7. Repository-control structure is established as the mandatory Phase 0 target baseline.
8. This document is an accepted **pre-coding decision baseline**. It does **not** itself authorize implementation. Coding remains subject to the Main_Prompt development-control chain:
   PROJECT → PHASE → WORK PACKAGE → AUTHORIZED TASK → IMPLEMENTATION → TEST → VERIFICATION → EVIDENCE → CHECKPOINT.



### Q1. What exact legal/business name should appear in the LIMS, reports, documents, and configuration?

**Answer:** Capture at deployment as controlled laboratory identity data. Any later change must be controlled, effective-dated, and must not alter historical reports/records.
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

**Status:** CLOSED — RECONCILED BASELINE



### Q2. What exact laboratory/site name should appear in records and reports?

**Answer:** Same treatment as #1. Historical report identity must remain reconstructable.

**Status:** CLOSED — RECONCILED BASELINE



### Q3. Is v1 for exactly one physical laboratory/site?

**Answer:** v1 represents exactly one physical laboratory/site.

**Status:** CLOSED — RECONCILED BASELINE



### Q4. Are there any satellite rooms, sample collection points, field teams, branches, or temporary locations that v1 must represent?

**Answer:** Out of v1 scope.

**Status:** CLOSED — RECONCILED BASELINE



### Q5. If multiple physical locations exist, are they part of the same laboratory or separate entities?

**Answer:** No multi-location model required for v1.

**Status:** CLOSED — RECONCILED BASELINE



### Q6. Is the intended v1 user population still approximately 1–10 named users?

**Answer:** Design baseline remains approximately 1–10 named users.

**Status:** CLOSED — RECONCILED BASELINE



### Q7. Is the expected simultaneous writer count still approximately 1–5 users?

**Answer:** Use 1–3 normal concurrent writers for operational workload testing; retain the stated higher stress scenario where appropriate.

**Status:** CLOSED — RECONCILED BASELINE



### Q8. What is the expected number of samples per day, week, and month at launch?

**Answer:** The launch workload shall be based on 100 samples per day as the approved launch workload baseline.

This operating workload shall remain distinct from:
- supported technical capacity;
- normal operating peak;
- stress-test workload; and
- supported concurrency.

The applicable operating-calendar assumption shall be documented separately so that daily, weekly, and monthly workload figures remain internally consistent.

**Status:** CLOSED — RECONCILED BASELINE



### Q9. What is the expected number of test instances per sample?

**Answer:** The normal launch expectation is approximately **3–5 tests per sample**. For architectural design, the controlled baseline is **50 tests per sample**; **80 tests per sample is a stretch case**, not an acceptance target. Actual capacity and performance acceptance must come from the authorized performance spike on the target environment.

**Status:** CLOSED — RECONCILED BASELINE



### Q10. What is the expected number of reports per day, week, and month?

**Answer:** 1 report/sample should be the normal launch assumption, but the system should not structurally require exactly one report per sample because later report revisions/reissues/partial or grouped reporting may differ.

**Status:** CLOSED — RECONCILED BASELINE



### Q11. What peak workload should the system be designed and tested for?

**Answer:** The controlled design workload is **100 samples/day with 50 tests/sample**. The 80-tests-per-sample case is a stretch scenario, not a normal acceptance target. Capacity, latency and throughput acceptance are measured on the defined workload/environment rather than treated as universal guarantees.

**Status:** CLOSED — RECONCILED BASELINE



### Q12. What data-retention period is required for controlled laboratory records?

**Answer:** The current controlled retention baseline is **10 years minimum**. Retention starts from the applicable controlled retention-start event; the general baseline uses the later of the last ReportRevision issue date and record closure unless the approved Retention Matrix defines a different record-class-specific event. Archive is controlled, retrievable and integrity-preserved; it is not deletion, and v1 has no automatic destruction workflow.

**Status:** CLOSED — RECONCILED BASELINE



### Q13. What data-retention period is required for audit records?

**Answer:** Audit records follow the controlled retention baseline and remain linked to the technical records they explain. The minimum retention period is **10 years**, with the applicable retention start defined in the controlled Retention Matrix. Archived audit history remains retrievable and historically reconstructable.

**Status:** CLOSED — RECONCILED BASELINE



### Q14. What data-retention period is required for reports and issued PDFs?

**Answer:** Issued reports and exact issued PDFs follow the **10-year minimum** retention baseline and must remain retrievable and verifiable. The preserved PDF, SHA-256 hash, ReportRevision, ReportResultSnapshots, DocumentVersion, approval evidence and relevant audit history must support reconstruction. Archival does not mean deletion.

**Status:** CLOSED — RECONCILED BASELINE



### Q15. What historical paper/spreadsheet records must be migrated into v1?

**Answer:** LabNexus shall support controlled, selective migration of approved historical paper/spreadsheet records where the laboratory determines that migration provides operational, traceability, quality, contractual, legal, or historical value.

Legacy records shall undergo documented discovery and assessment before migration. Only records approved for migration shall be migrated.

If the assessment determines that no suitable historical records require migration, the project shall formally record **No Migration Required.**

Historical data shall never be fabricated, reconstructed without evidence, or entered merely to satisfy a migration requirement.

**Status:** CLOSED — RECONCILED BASELINE



### Q16. Which historical records will remain outside the LIMS?

**Answer:** Historical records not approved for migration shall remain outside the LIMS under the laboratory's applicable controlled retention and document-management arrangements.
The Migration Assessment shall identify the record sets or categories remaining outside LabNexus and, where appropriate, their source location or reference.
Remaining outside the LIMS does not mean uncontrolled, unretained, or disposable.

**Status:** CLOSED — RECONCILED BASELINE



### Q17. Is historical migration required before go-live, after go-live, or optional?

**Answer:** Historical migration shall be performed through a controlled phased process.
Historical records required for safe operational continuity, necessary traceability, or another formally approved go-live requirement shall be migrated before the affected operational use begins.
Additional approved historical migration may occur after go-live using the same controlled migration procedure.
Historical migration shall not silently convert historical records into ordinary contemporaneous LIMS records.

**Status:** CLOSED — RECONCILED BASELINE



### Q18. Who decides whether an old paper/spreadsheet record is trustworthy enough to migrate?

**Answer:** Migration suitability shall be governed as follows:
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

**Status:** CLOSED — RECONCILED BASELINE



### Q19. Must the LIMS support retrospective entry of historical records?

**Answer:** LabNexus shall support controlled retrospective entry of approved historical information where required.
Retrospective entry shall distinguish the **historical event date/time** from the **actual LIMS entry timestamp** and shall preserve source/provenance, entering user, verification status, and applicable approval/evidence.
Ordinary users shall not be able to bypass workflow controls merely by entering a historical date.

**Status:** CLOSED — RECONCILED BASELINE



### Q20. If historical records are entered, how will their original date, source, and provenance be recorded?

**Answer:** A historical record shall preserve, where known/applicable:
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

**Status:** CLOSED — RECONCILED BASELINE



### Q21. What functionality is explicitly outside v1 even if it might be useful later?

**Answer:** The following explicitly outside v1 unless a later approved requirement changes scope:
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

**Status:** CLOSED — RECONCILED BASELINE



### Q22. What future capabilities must be architecturally possible but not implemented in v1?

**Answer:** Category A - Laboratory expansion
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

**Status:** CLOSED — RECONCILED BASELINE



### Q23. Are there any regulatory, contractual, customer, or business requirements not represented in the Master Prompt?

**Answer:** Accreditation and QMS
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

**Status:** CLOSED — RECONCILED BASELINE



### Q24. Who has final authority to accept the scope baseline?

**Answer:** Project owner.

## 1.2 Future disciplines

**Status:** CLOSED — RECONCILED BASELINE



### Q25. Which disciplines are definitely required at launch?

**Answer:** - Solid Fuel (Coal)
	- Solid Biofuel

**Status:** CLOSED — RECONCILED BASELINE



### Q26. Which disciplines are only future possibilities?

**Answer:** - Air
	- Water
	- Soil
	- Noise
	- Stack/Emissions
	- Other laboratory disciplines as requirements arise

**Status:** CLOSED — RECONCILED BASELINE



### Q27. Is Solid Fuel required in v1 from day one?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q28. Is Solid Biofuel required in v1 from day one?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q29. Which future discipline should be used for the first extensibility-validation exercise?

**Answer:** Water

**Status:** CLOSED — RECONCILED BASELINE



### Q30. What real future test/method scenario should be used to prove that the core architecture is reusable?

**Answer:** Water — Total Suspended Solids (TSS), using the laboratory-approved applicable method; IS 3025 (Part 17):2022 is a concrete Indian-standard example.

**Status:** CLOSED — RECONCILED BASELINE



### Q31. Are there discipline-specific workflows that are already known to differ from the common workflow?

**Answer:** No specific divergence should be assumed at present. Design around a common workflow plus configurable/controlled extensions.

**Status:** CLOSED — RECONCILED BASELINE



### Q32. Are there discipline-specific regulatory or reporting requirements that must be modeled now?

**Answer:** Only the reusable mechanisms, not future discipline-specific rules.

**Status:** CLOSED — RECONCILED BASELINE



### Q33. Are field sampling workflows required for any future discipline?

**Answer:** Not for v1. Architecturally possible later.

**Status:** CLOSED — RECONCILED BASELINE



### Q34. Are environmental monitoring programs required now or later?

**Answer:** Later, unless a specific current laboratory requirement says otherwise.

---

# 2. Laboratory Governance and Decision Ownership

**Status:** CLOSED — RECONCILED BASELINE



### Q35. Who is the final business owner of the LIMS?

**Answer:** The lims app name is LabNexus, the final business owner of the LIMS is the Project Owner / Laboratory Business Owner using it.

**Status:** CLOSED — RECONCILED BASELINE



### Q36. Who is the laboratory quality authority for the LIMS?

**Answer:** Laboratory Quality Authority, normally the Quality Manager or equivalent person formally responsible for the QMS.

**Status:** CLOSED — RECONCILED BASELINE



### Q37. Who is the technical authority for methods and results?

**Answer:** Laboratory Technical Authority, normally Technical Manager/Technical Head or equivalent competent person.

**Status:** CLOSED — RECONCILED BASELINE



### Q38. Who is the system administrator?

**Answer:** Designated LIMS System Administrator.

**Status:** CLOSED — RECONCILED BASELINE



### Q39. Who can approve controlled configuration changes?

**Answer:** Authorized Configuration Approver, with domain-appropriate Quality/Technical approval; proposer and implementer should not approve their own change.

**Status:** CLOSED — RECONCILED BASELINE



### Q40. Who can approve emergency configuration changes?

**Answer:** Pre-designated Alternate Emergency Approver with appropriate authority and competence.

**Status:** CLOSED — RECONCILED BASELINE



### Q41. Who can approve production deployment?

**Answer:** Designated Production/Release Authority, after successful verification/acceptance; business release authorization from Project Owner or delegate.

**Status:** CLOSED — RECONCILED BASELINE



### Q42. Who can approve rollback or recovery after a failed update?

**Answer:** Technical/Operations Authority may authorize immediate rollback to restore controlled operation; required business/quality review follows.

**Status:** CLOSED — RECONCILED BASELINE



### Q43. Who can accept validation/UAT results?

**Answer:** Project Owner / Laboratory Business Owner, with Quality Authority verifying validation evidence.

**Status:** CLOSED — RECONCILED BASELINE



### Q44. Who can approve creation of new users?

**Answer:** User Access Approver designated by laboratory management, typically Project Owner/Lab Head or delegate.

**Status:** CLOSED — RECONCILED BASELINE



### Q45. Who can disable users?

**Answer:** System Administrator executes; authorized management/quality/security authority may order immediate disablement.

**Status:** CLOSED — RECONCILED BASELINE



### Q46. Who can assign roles?

**Answer:** System Administrator executes only approved role assignments; approval comes from User Access Approver.

**Status:** CLOSED — RECONCILED BASELINE



### Q47. Who can approve changes to SoD policy?

**Answer:** Laboratory Quality Authority + Project Owner, with Technical Authority review of implementability.

**Status:** CLOSED — RECONCILED BASELINE



### Q48. Who can approve accreditation-scope configuration?

**Answer:** Laboratory Quality Authority as final approval, with Technical Authority concurrence.

**Status:** CLOSED — RECONCILED BASELINE



### Q49. Who can approve report templates?

**Answer:** Technical Authority for technical correctness and Quality Authority for controlled-document approval.

**Status:** CLOSED — RECONCILED BASELINE



### Q50. Who owns the retention policy?

**Answer:** Laboratory Quality Authority, with Project Owner/business authority for final policy acceptance.

**Status:** CLOSED — RECONCILED BASELINE



### Q51. Who owns backup/recovery procedures?

**Answer:** Technical/Operations Authority; System Administrator executes the procedures.

**Status:** CLOSED — RECONCILED BASELINE



### Q52. Who owns the controlled project documents?

**Answer:** Project Owner owns the project baseline; a designated Document/Project Controller maintains repository state.

**Status:** CLOSED — RECONCILED BASELINE



### Q53. What happens if the designated approver is unavailable?

**Answer:** Use the pre-approved alternate-approver path. No ad-hoc substitution.

**Status:** CLOSED — RECONCILED BASELINE



### Q54. What is the approved alternate-approver path?

**Answer:** Named alternate with equivalent authority/competence, active authority period, no prohibited conflict, and full audit trail.

**Status:** CLOSED — RECONCILED BASELINE



### Q55. What counts as an emergency for configuration or operational decisions?

**Answer:** A situation requiring immediate action to protect data integrity, security, controlled laboratory operation, report correctness, or recovery from a failed/unsafe change where normal approval cannot be completed in time.

**Status:** CLOSED — RECONCILED BASELINE



### Q56. Who is permitted to declare an emergency?

**Answer:** Designated Emergency Authority; recommend Quality Authority or Technical/System Authority depending on the emergency type.

**Status:** CLOSED — RECONCILED BASELINE



### Q57. What must be documented when an emergency path is used?

**Answer:** Reason, urgency, unavailable normal path, affected object/configuration, risk, authorizer, executor, exact change, start/end time, evidence, post-change verification, expiry, and retrospective review.

**Status:** CLOSED — RECONCILED BASELINE



### Q58. Who performs retrospective review of emergency actions?

**Answer:** Quality Authority + relevant Technical Authority; security incidents additionally reviewed by the responsible system/security authority.

**Status:** CLOSED — RECONCILED BASELINE



### Q59. How often must emergency use be reviewed?

**Answer:** Monthly operational review, plus immediate review of any high-risk event; periodic management trend review can be quarterly.

---

# 3. Frozen Architecture — Confirmation Questions

These are not intended to reopen the baseline. They are confirmation questions to detect contradictions before coding starts.

**Status:** CLOSED — RECONCILED BASELINE



### Q60. Is React + TypeScript + Vite + MUI still the approved frontend stack?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q61. Is FastAPI + Python still the approved backend stack?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q62. Is SQLAlchemy 2.x still the approved ORM?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q63. Is SQLite still the approved v1 database?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q64. Is Alembic still the approved migration tool?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q65. Is Argon2id plus server-side sessions still the approved authentication architecture?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q66. Is RBAC plus backend authorization plus per-TestInstance SoD still the approved authorization model?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q67. Is Caddy still the approved reverse proxy?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q68. Is Jinja2 plus HTML/CSS plus Chromium still the approved reporting pipeline?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q69. Are pytest and Playwright still the approved testing tools?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q70. Are Code 128 and QR still the approved barcode formats?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q71. Is Windows 11 Pro and/or Windows Server still the approved deployment target?

**Answer:** Yes — Windows 11 Pro and Windows Server are approved deployment targets; exact production OS is selected during deployment planning.

**Status:** CLOSED — RECONCILED BASELINE



### Q72. Is the modular-monolith architecture still approved?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q73. Is the single-host architecture still approved?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q74. Is offline-first operation still mandatory?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q75. Is the rule that the live SQLite database must remain on local fixed storage still mandatory?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q76. Is the rule against NAS/SMB live-database hosting still mandatory?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q77. Is the no-cloud-dependency requirement still mandatory?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q78. Is the no-multi-tenancy decision still valid for v1?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q79. Is the no-public-API boundary still valid for v1?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q80. Is the commercial boundary still limited to charge calculation inside LIMS, with invoicing/accounting/payments outside the system?

**Answer:** Charge calculation is **out of v1**. No Rate, CustomerRate, charge snapshot, discount, override, tax calculation, invoice, accounts-receivable, payment or accounting subsystem is implemented. TestRequest remains a technical request-line without pricing. Reintroduction requires a later approved commercial scope decision and controlled work package.

**Status:** CLOSED — RECONCILED BASELINE



### Q81. Is documentation-as-code still mandatory?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q82. Is the repository the authoritative source of project state?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q83. Is explicit task authorization before coding still mandatory?

**Answer:** Yes

**Status:** CLOSED — RECONCILED BASELINE



### Q84. Is the frozen architecture change process agreed and operationally understood?

**Answer:** Yes — the architecture-change process is agreed and understood; any approved change must be recorded in the authoritative repository and affected baselines/contracts updated before implementation.

---

# 4. Laboratory Operating Model

## 4.1 Daily operation

**Status:** CLOSED — RECONCILED BASELINE



### Q85. What does a normal working day in the laboratory look like?

**Answer:** Receipt → Registration → Identification → Test Allocation → Testing → Observations → Calculation → Review → Verification → Approval → Report → Delivery → Retention/Archive.

**Status:** CLOSED — RECONCILED BASELINE



### Q86. Who receives samples?

**Answer:** Authorized Sample Receiving/Laboratory User.

**Status:** CLOSED — RECONCILED BASELINE



### Q87. Who registers samples?

**Answer:** Authorized Sample Receiving/Registration User.

**Status:** CLOSED — RECONCILED BASELINE



### Q88. Who identifies or labels samples?

**Answer:** Authorized Sample Receiving/Registration User.

**Status:** CLOSED — RECONCILED BASELINE



### Q89. Who allocates samples to tests?

**Answer:** Authorized Laboratory Coordinator/Technical User.

**Status:** CLOSED — RECONCILED BASELINE



### Q90. Who performs tests?

**Answer:** Authorized Analyst

**Status:** CLOSED — RECONCILED BASELINE



### Q91. Who records observations?

**Answer:** Analyst performing the TestInstance.

**Status:** CLOSED — RECONCILED BASELINE



### Q92. Who performs calculations?

**Answer:** Controlled LIMS calculation engine using approved FormulaVersions; analyst supplies/reviews required inputs.

**Status:** CLOSED — RECONCILED BASELINE



### Q93. Who reviews results?

**Answer:** Authorized Technical Reviewer

**Status:** CLOSED — RECONCILED BASELINE



### Q94. Who verifies results?

**Answer:** Authorized Technical Verifier

**Status:** CLOSED — RECONCILED BASELINE



### Q95. Who approves results?

**Answer:** Authorized Approver / Authorized Signatory

**Status:** CLOSED — RECONCILED BASELINE



### Q96. Who issues reports?

**Answer:** Authorized Report-Issuing User after approval

**Status:** CLOSED — RECONCILED BASELINE



### Q97. Who delivers reports?

**Answer:** Authorized Report/Administrative User

**Status:** CLOSED — RECONCILED BASELINE



### Q98. Who performs archival/retention activities?

**Answer:** Designated Records/Quality User

**Status:** CLOSED — RECONCILED BASELINE



### Q99. Can one person perform multiple roles on the same day?

**Answer:** Permitted, subject to authorization and TestInstance-level SoD.

**Status:** CLOSED — RECONCILED BASELINE



### Q100. Can the same person perform multiple stages on different TestInstances?

**Answer:** Permitted, subject to authorization and policy.

**Status:** CLOSED — RECONCILED BASELINE



### Q101. Which actions require two-person control?

**Answer:** Required for designated high-risk controlled decisions and wherever approved laboratory SoD/QMS policy requires independent control.

**Status:** CLOSED — RECONCILED BASELINE



### Q102. Which actions can be performed by one authorized person?

**Answer:** Ordinary authorized actions where no SoD or two-person requirement applies.

**Status:** CLOSED — RECONCILED BASELINE



### Q103. Which actions must never be performed by the same person on the same TestInstance?

**Answer:** Analyst + Review
    Analyst + Verification
    Analyst + Approval.
    Other combinations are policy-controlled unless explicitly blocked.

**Status:** CLOSED — RECONCILED BASELINE



### Q104. Are there informal laboratory practices that must be made explicit in the system?

**Answer:** At minimum, an Analyst shall not Review, Verify, or Approve the same TestInstance. Other combinations shall be determined by the approved TestInstance-level SoD policy. Hard blocks cannot be bypassed.

**Status:** CLOSED — RECONCILED BASELINE



### Q105. Are there paper forms or registers that remain legally or operationally required after go-live?

**Answer:** Paper forms/registers may remain after go-live only where required by law, accreditation/QMS procedure, technical method, operational necessity, or an approved business decision. Where an existing paper control is replaced by LIMS, the electronic control must be formally assessed and validated as the replacement.

**Status:** CLOSED — RECONCILED BASELINE



### Q106. Which existing manual controls must be preserved or replaced with equivalent electronic controls?

**Answer:** Must be mapped to equivalent or stronger electronic controls before replacement.
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

**Status:** CLOSED — RECONCILED BASELINE



### Q107. Are samples collected by the laboratory?

**Answer:** No field-sampling workflow in v1. Samples are received by the laboratory from customers/authorized external sources unless a specific launch requirement says otherwise.

**Status:** CLOSED — RECONCILED BASELINE



### Q108. Are samples collected by customers or third parties?

**Answer:** Yes, this should be supported as the normal v1 assumption.

**Status:** CLOSED — RECONCILED BASELINE



### Q109. Are field observations or field measurements required?

**Answer:** No, not in v1.

**Status:** CLOSED — RECONCILED BASELINE



### Q110. Must field activity be recorded in the LIMS?

**Answer:** No field-activity module in v1.

**Status:** CLOSED — RECONCILED BASELINE



### Q111. Is offline/mobile field entry required in v1?

**Answer:** No, not in v1.

**Status:** CLOSED — RECONCILED BASELINE



### Q112. Are chain-of-custody records required?

**Answer:** Not assumed as a universal v1 requirement; determine based on actual sample/customer/QMS requirements.

**Status:** CLOSED — RECONCILED BASELINE



### Q113. Are sample transport conditions required to be captured?

**Answer:** Capture where relevant to sample integrity/method/customer requirements.

**Status:** CLOSED — RECONCILED BASELINE



### Q114. Are receipt temperatures or other transport conditions required?

**Answer:** Configurable/capturable where applicable; do not require universally.

**Status:** CLOSED — RECONCILED BASELINE



### Q115. Are sample containers or preservation conditions relevant?

**Answer:** Yes, the data model should be capable of recording them where applicable, but not every Solid Fuel/Solid Biofuel sample needs those fields.

---

# 5. Customer, Project, Contract, and Request Model

**Status:** CLOSED — RECONCILED BASELINE



### Q116. What is the exact definition of a Customer?

**Answer:** A Customer is the external person or legal/business entity that requests, contracts for, or receives laboratory services and to whom the laboratory's commercial/administrative relationship belongs.

**Status:** CLOSED — RECONCILED BASELINE



### Q117. Can one Customer have multiple sites or addresses?

**Answer:** Yes. One Customer can have multiple sites/locations and addresses.

**Status:** CLOSED — RECONCILED BASELINE



### Q118. Can one Customer have multiple contacts?

**Answer:** Yes. One Customer can have multiple contacts, with contact roles/statuses.

**Status:** CLOSED — RECONCILED BASELINE



### Q119. What customer fields are mandatory?

**Answer:** Customer ID, customer/legal name, active/inactive status, and minimum identity/address information required by the laboratory. Other commercial/contact fields should be conditional.

**Status:** CLOSED — RECONCILED BASELINE



### Q120. Are customer identifiers internally assigned or externally supplied?

**Answer:** Internal Customer ID assigned by LIMS. External customer codes/IDs may also be stored separately.

**Status:** CLOSED — RECONCILED BASELINE



### Q121. Can customer names be changed after records exist?

**Answer:** Yes, but as a controlled master-data change; do not overwrite the historical identity used by issued records.

**Status:** CLOSED — RECONCILED BASELINE



### Q122. If a customer name changes, should historical reports preserve the original displayed name?

**Answer:** Yes, absolutely.

**Status:** CLOSED — RECONCILED BASELINE



### Q123. What is the definition of a Project?

**Answer:** Project is a controlled grouping of related laboratory work undertaken for a Customer, normally representing a defined engagement, contract, job, program, or continuing body of work.

**Status:** CLOSED — RECONCILED BASELINE



### Q124. Is a Project always linked to a Customer?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q125. Can one Project have multiple samples?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q126. Can one Project contain multiple requests?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q127. Can one Customer have multiple contracts?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q128. Can a Contract exist without a Project?

**Answer:** Yes. A Contract may exist independently and support one or more Projects/Requests.

**Status:** CLOSED — RECONCILED BASELINE



### Q129. What commercial information must the LIMS keep?

**Answer:** V1 does **not** implement charge calculation. Rate/CustomerRate, pricing, charge snapshots and discounts are outside the current v1 commercial scope. Commercial information that remains relevant to laboratory administration may be retained as non-calculating reference data only where explicitly required; no pricing logic or charge fields should be implemented by inference.

**Status:** CLOSED — RECONCILED BASELINE



### Q130. What information stays outside the LIMS?

**Answer:** Invoices, accounts receivable, payments, banking, tax/accounting ledger and full financial accounting remain **outside LabNexus v1**. The system is not an accounting subsystem.

**Status:** CLOSED — RECONCILED BASELINE



### Q131. Is pricing required at request time, test time, report time, or invoice time?

**Answer:** There is no v1 pricing event because charge calculation is deferred. No rate is selected at request, test, report or invoice time in the controlled v1 application.

**Status:** CLOSED — RECONCILED BASELINE



### Q132. How are rates selected?

**Answer:** There is no v1 rate-selection precedence because Rate/CustomerRate are excluded from the v1 scope. A future commercial work package must define precedence, effective dating and historical snapshots before implementation.

**Status:** CLOSED — RECONCILED BASELINE



### Q133. Are rates effective-dated?

**Answer:** Rate effective dating is not implemented in v1 because pricing/rate calculation is out of scope. Future commercial behavior must use controlled effective-dated configuration if later approved.

**Status:** CLOSED — RECONCILED BASELINE



### Q134. Are customer-specific rates required?

**Answer:** Customer-specific rates are not implemented in v1. A future commercial scope decision may define them, but no customer-specific pricing behavior is assumed now.

**Status:** CLOSED — RECONCILED BASELINE



### Q135. Who can change rates?

**Answer:** There is no v1 rate-change workflow. A future rate-management capability would require controlled authority, proposal/approval, effective dating, audit history and historical protection.

**Status:** CLOSED — RECONCILED BASELINE



### Q136. Can rates be overridden for a specific request?

**Answer:** There is no v1 request-level rate override. A future commercial scope decision would have to define who may approve overrides, the reason/evidence requirements and historical snapshot behavior.

**Status:** CLOSED — RECONCILED BASELINE



### Q137. If rates change later, must historical charges remain unchanged?

**Answer:** Historical charges are not a v1 feature because charge calculation itself is deferred. A future commercial implementation must preserve the historical commercial state associated with already-processed work rather than recalculating it from later rates.

**Status:** CLOSED — RECONCILED BASELINE



### Q138. What is the exact definition of a Request?

**Answer:** A Request is a customer's controlled instruction/order for one or more laboratory services on one or more samples, including requested tests and applicable commercial/technical information.

**Status:** CLOSED — RECONCILED BASELINE



### Q139. Can one request contain multiple samples?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q140. Can one request contain multiple TestDefinitions?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q141. Can a request be cancelled after work starts?

**Answer:** Yes, through controlled cancellation. It must not erase started/completed TestInstances or historical records.

**Status:** CLOSED — RECONCILED BASELINE



### Q142. What happens to charges when a request is cancelled?

**Answer:** Retain charges already legitimately incurred; unstarted work is cancelled; cancellation fees/other commercial rules depend on approved policy.

**Status:** CLOSED — RECONCILED BASELINE



### Q143. Can a customer request a specific method?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q144. Can the laboratory substitute an approved method?

**Answer:** Yes, only under controlled technical rules and where permitted by applicable requirements/accreditation/customer agreement.

**Status:** CLOSED — RECONCILED BASELINE



### Q145. Who can approve method substitution?

**Answer:** Laboratory Technical Authority, with Quality/customer approval where the governing requirement requires it.

**Status:** CLOSED — RECONCILED BASELINE



### Q146. Must the original customer request remain visible after changes?

**Answer:** Yes. Original request and subsequent amendments must remain reconstructable.

---

# 6. Sample Intake and Sample Identity

**Status:** CLOSED — RECONCILED BASELINE



### Q147. What is the exact definition of a Sample?

**Answer:** A uniquely identified physical/material specimen received or otherwise placed under the laboratory's responsibility for one or more laboratory activities.

**Status:** CLOSED — RECONCILED BASELINE



### Q148. What makes a Sample uniquely identifiable?

**Answer:** LIMS-generated immutable Sample ID is the authoritative identity.

**Status:** CLOSED — RECONCILED BASELINE



### Q149. What is the internal sample number format?

**Answer:** Business identifiers use a centralized `number_sequence` registry with controlled prefix, padding, increment and reset policy. Allocation is atomic; gaps are acceptable; identifiers are not reset by calendar year. A representative Sample ID is `SAM-00000001`; year may be displayed separately where needed.

**Status:** CLOSED — RECONCILED BASELINE



### Q150. What is the external/customer sample identifier format?

**Answer:** The **internal LIMS Sample ID (`SAM-…`) is the authoritative globally unique Sample identity**. The customer/external Sample ID is a customer-supplied reference and is controlled for uniqueness **per customer** after normalization (trim + Unicode casefold) among current authoritative values. Historical or superseded external values remain provenance-only.

**Status:** CLOSED — RECONCILED BASELINE



### Q151. Which identifier is printed on the physical sample label?

**Answer:** The physical sample label and barcode shall print the **internal authoritative LIMS Sample ID (`SAM-…`)**. The customer/external ID may be displayed as reference information but does not replace the LIMS identity.

**Status:** CLOSED — RECONCILED BASELINE



### Q152. Can the customer supply duplicate sample identifiers?

**Answer:** Duplicate external identifiers are permitted across different customers. Within one customer, the current authoritative external ID must be unique after normalization. Historical/superseded submissions are retained only as provenance and are not treated as live identifiers.

**Status:** CLOSED — RECONCILED BASELINE



### Q153. How are duplicate external identifiers handled?

**Answer:** Duplicate handling uses normalized external ID uniqueness **per customer**. Cross-customer duplicates are allowed with a search warning. The internal `SAM-…` ID remains the global authoritative identifier.

**Status:** CLOSED — RECONCILED BASELINE



### Q154. What information must be captured at receipt?

**Answer:** Customer/source, external ID, receiving date/time, received-by user, packaging/container condition, physical condition, quantity where relevant, accompanying documents, apparent sample description, deviations, receipt decision.

**Status:** CLOSED — RECONCILED BASELINE



### Q155. What information must be captured at registration?

**Answer:** Internal Sample ID, customer/project/request link, sample description/matrix, external ID, receipt data, required tests/request links, acceptance status, storage requirements/location where applicable.

**Status:** CLOSED — RECONCILED BASELINE



### Q156. Is sample receipt date/time mandatory?

**Answer:** Mandatory

**Status:** CLOSED — RECONCILED BASELINE



### Q157. Is sample collection date/time mandatory?

**Answer:** Conditional mandatory where supplied, technically required, or relevant to method/holding-time requirements

**Status:** CLOSED — RECONCILED BASELINE



### Q158. Is sample receipt condition mandatory?

**Answer:** Mandatory assessment, with detailed condition data conditional

**Status:** CLOSED — RECONCILED BASELINE



### Q159. Which rejection reasons are required?

**Answer:** - Unidentified / ambiguous identity
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

**Status:** CLOSED — RECONCILED BASELINE



### Q160. Who may reject a sample?

**Answer:** Sample rejection may be performed by an authorized Sample Receiving user when a predefined objective rejection criterion is met; technical/discretionary rejection should require appropriate technical authority.

**Status:** CLOSED — RECONCILED BASELINE



### Q161. What happens after sample rejection?

**Answer:** Rejected sample is placed in a controlled Rejected state; reason, evidence, actor, date/time and customer communication/decision are retained. No downstream testing may proceed unless a permitted controlled disposition changes the status.

**Status:** CLOSED — RECONCILED BASELINE



### Q162. Can a rejected sample be re-opened?

**Answer:** Yes, but only through a controlled review/disposition process; not by simply changing Rejected back to Accepted.

**Status:** CLOSED — RECONCILED BASELINE



### Q163. Can a sample be conditionally accepted?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q164. Who can approve conditional acceptance?

**Answer:** Conditional acceptance should require an authorized person with the competence/authority defined by laboratory policy, normally the Technical Authority or designated sample-acceptance authority.

**Status:** CLOSED — RECONCILED BASELINE



### Q165. What sample condition checks are required?

**Answer:** - Identity/label
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

**Status:** CLOSED — RECONCILED BASELINE



### Q166. Are sample quantity/volume/mass requirements enforced?

**Answer:** Yes, where required.

**Status:** CLOSED — RECONCILED BASELINE



### Q167. Are sample preservation requirements enforced?

**Answer:** Yes, where applicable.

**Status:** CLOSED — RECONCILED BASELINE



### Q168. Are container requirements enforced?

**Answer:** Yes, where applicable.

**Status:** CLOSED — RECONCILED BASELINE



### Q169. Are sample storage locations tracked?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q170. Are sample storage conditions tracked?

**Answer:** Yes, where applicable.

**Status:** CLOSED — RECONCILED BASELINE



### Q171. Is sample disposal tracked?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q172. Who authorizes disposal?

**Answer:** Sample disposal requires a controlled authorization and execution workflow. The **Technical Authority or designated Sample Custodian** authorizes disposal; an authorized Sample Receiving user may execute it, with a witness where required. Disposal is blocked until all related TestInstances are Approved or Cancelled, the discipline-specific retained-sample period has elapsed, and no legal/quality hold applies. Evidence must record authority, executor, reason, date/time and disposition.

**Status:** CLOSED — RECONCILED BASELINE



### Q173. What evidence is retained for disposal?

**Answer:** - Sample ID
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

**Status:** CLOSED — RECONCILED BASELINE



### Q174. Are sample portions/aliquots/sub-samples required?

**Answer:** Yes — the architecture should support them.

**Status:** CLOSED — RECONCILED BASELINE



### Q175. If yes, how are portions linked to the parent sample?

**Answer:** SamplePortion.parent_sample_id → Sample.id

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

**Status:** CLOSED — RECONCILED BASELINE



### Q176. Are sample splits or composites required?

**Answer:** Sample splits, composites, and derived-sample lineage are not required for v1 and are out of v1 scope.
V1 shall support the required physical sample identity and traceability model without implementing split/composite workflows.
Any future introduction of splits, composites, derived samples, relabelling lineage, or related identity transformations shall be handled as a controlled architectural change.

**Status:** CLOSED — RECONCILED BASELINE



### Q177. If a composite sample is created, how are source samples recorded?

**Answer:** Composite samples are out of v1 scope.
V1 shall not implement composite-sample creation or source-sample lineage.
If composites are introduced in a future controlled change, the source-sample lineage model shall be formally defined and approved before implementation.

**Status:** CLOSED — RECONCILED BASELINE



### Q178. Can one physical sample map to multiple Sample records?

**Answer:** V1 shall not provide sample-lineage capability in which one physical sample maps to multiple Sample records.
V1 does not implement sample splitting, derived samples, or one-to-many physical-sample lineage.
The v1 Sample model shall maintain the defined physical sample identity without introducing implicit multiple-record mappings.
Any future requirement for such mappings shall be addressed through a controlled architectural change.

**Status:** CLOSED — RECONCILED BASELINE



### Q179. How are relabeling and identity corrections handled?

**Answer:** V1 does not implement split/composite or broader physical-sample lineage.
Identity corrections and relabelling, where required by the v1 sample workflow, shall be handled through controlled correction and audit mechanisms without silently replacing historical identity information.
Any future requirement for lineage-aware relabelling or identity transformation shall require a controlled architectural change.

**Status:** CLOSED — RECONCILED BASELINE



### Q180. What is the process when a sample identity is discovered to be wrong after testing begins?

**Answer:** If a sample identity is suspected to be incorrect after testing has started, the system shall trigger a controlled investigation and immediately pause all affected tests.
The affected work shall remain blocked pending authorized investigation and disposition.
The original recorded identity, evidence, discovery event, actors, affected TestInstances, and subsequent disposition shall remain historically traceable.
No user shall resolve the issue by silently editing the original Sample identity.

**Status:** CLOSED — RECONCILED BASELINE



### Q181. What sample fields are allowed to change after registration?

**Answer:** Generally editable under normal rules until they become operationally relied upon, for example:
	- Non-critical description
	- Administrative notes
	- Internal handling notes
	- Planned storage location
	- Non-critical customer contact information
	- Some scheduling/administrative metadata
	subject to audit where appropriate.

**Status:** CLOSED — RECONCILED BASELINE



### Q182. Which sample fields become immutable after a defined stage?

**Answer:** - Internal Sample ID
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

**Status:** CLOSED — RECONCILED BASELINE



### Q183. Which changes require correction/reopen rather than normal editing?

**Answer:** - Sample identity
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

**Status:** CLOSED — RECONCILED BASELINE



### Q184. Is internal sample allocation required?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q185. What exactly is being allocated: physical sample, aliquot, portion, or TestInstance?

**Answer:** Primarily a Sample or SamplePortion to a TestInstance. Allocation is a laboratory work-control relationship, not necessarily a physical transfer.

**Status:** CLOSED — RECONCILED BASELINE



### Q186. Must each allocation be traceable to a person, location, and time?

**Answer:** Yes. Allocation and significant physical movement should record actor, timestamp and location/state.

**Status:** CLOSED — RECONCILED BASELINE



### Q187. Are sample transfers between rooms or storage locations required?

**Answer:** Yes, where applicable.

**Status:** CLOSED — RECONCILED BASELINE



### Q188. Are custody handovers required?

**Answer:** Supported, but not mandatory for every internal movement.

**Status:** CLOSED — RECONCILED BASELINE



### Q189. Is chain-of-custody legally or procedurally required for any test type?

**Answer:** Not established as a universal v1 requirement. Must be determined per applicable test/customer/regulatory requirement.

**Status:** CLOSED — RECONCILED BASELINE



### Q190. What events constitute a custody transfer?

**Answer:** A controlled change in the person/organizational responsibility for the physical sample/portion, or an externally relevant handover. Mere movement within the same person's control is not necessarily a custody transfer.

**Status:** CLOSED — RECONCILED BASELINE



### Q191. Who can record a transfer?

**Answer:** Authorized users responsible for sample handling/transfer.

**Status:** CLOSED — RECONCILED BASELINE



### Q192. Who can receive custody?

**Answer:** Authorized users designated for the receiving location/activity.

**Status:** CLOSED — RECONCILED BASELINE



### Q193. What happens if custody is interrupted or undocumented?

**Answer:** Mark the chain/transfer as exceptional or unresolved, prevent affected controlled use where integrity could be affected, investigate and document disposition.

**Status:** CLOSED — RECONCILED BASELINE



### Q194. Are storage locations controlled master data?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q195. Must the system prevent use of a sample that is not in an eligible state/location?

**Answer:** Yes, where the configured business rule requires it. Backend must enforce it.

---

# 8. Test Request, Test Assignment, and TestInstance

**Status:** CLOSED — RECONCILED BASELINE



### Q196. What is the exact business meaning of a TestRequest?

**Answer:** A requested laboratory service/test representing what the customer/laboratory has requested for a Sample.

**Status:** CLOSED — RECONCILED BASELINE



### Q197. What is the exact business meaning of a TestInstance?

**Answer:** A specific controlled execution occurrence of a TestDefinition against a Sample/Portion, with its own assignment, execution, observations, calculations, result, review, verification and approval history.

**Status:** CLOSED — RECONCILED BASELINE



### Q198. Can one TestRequest create multiple TestInstances?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q199. Under what conditions are repeat TestInstances created?

**Answer:** A new TestInstance represents a **distinct execution occurrence**. REPEAT, RETEST and other re-execution events create a new TestInstance with a traceable origin. Eligible pre-approval REWORK uses the same TestInstance only for data, calculation or transcription fixes that do not rerun the analysis. Post-approval CORRECTION uses controlled Reopen of the same TestInstance with a new Correction revision. The prior history is never overwritten.

**Status:** CLOSED — RECONCILED BASELINE



### Q200. How are repeats distinguished from corrections?

**Answer:** A **repeat** represents a new execution of the test because another measurement/execution is required under an approved laboratory rule. It creates a distinct TestInstance and preserves the prior execution.
A **correction** represents a controlled correction to an existing technical record/result or its provenance because the existing record is determined to be incorrect or incomplete.
A correction shall not be represented merely as an ordinary repeat, and a repeat shall not overwrite the original TestInstance/result history.
The reason classification shall be mandatory where the distinction affects workflow, review, verification, approval, reporting, or traceability.

**Status:** CLOSED — RECONCILED BASELINE



### Q201. How are re-tests distinguished from routine replicate measurements?

**Answer:** A **replicate** is an additional observation within the same TestInstance. A **retest** is a new TestInstance, reason RETEST, linked to the originating execution because the analysis must be run again under an approved reason. Replicates and retests must remain separately classified and traceable.

**Status:** CLOSED — RECONCILED BASELINE



### Q202. Can a TestInstance be cancelled independently of the Sample?

**Answer:** Yes. A TestInstance may be cancelled independently of the Sample.

**Status:** CLOSED — RECONCILED BASELINE



### Q203. Can a Sample remain active while one TestInstance is cancelled?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q204. Can a TestInstance be reopened after approval?

**Answer:** Approved work may leave the Approved state only through a controlled Reopen. Reopen requires authorization, documented reason, preservation of the prior approved state and downstream impact assessment. Eligible post-approval corrections use a new Correction revision on the same TestInstance; if the analysis itself must be rerun, a new TestInstance is created. Affected work undergoes renewed Review, Verification and Approval as required.

**Status:** CLOSED — RECONCILED BASELINE



### Q205. Who may create a TestInstance?

**Answer:** TestInstance creation should be system-controlled and permitted to authorized users/services when a valid TestRequest and TestDefinition exist.

**Status:** CLOSED — RECONCILED BASELINE



### Q206. Who may assign a TestInstance to an analyst?

**Answer:** Authorized Laboratory Coordinator/Technical User may assign a TestInstance to an eligible analyst.

**Status:** CLOSED — RECONCILED BASELINE



### Q207. Can an analyst assign work to themselves?

**Answer:** An analyst may assign work to themselves only if the laboratory's policy explicitly permits self-assignment and doing so does not create a prohibited SoD condition.

**Status:** CLOSED — RECONCILED BASELINE



### Q208. Can a TestInstance have multiple analysts?

**Answer:** Yes, a TestInstance may have multiple analysts where the approved test procedure requires/permits multiple responsible performers.

**Status:** CLOSED — RECONCILED BASELINE



### Q209. Is there one primary analyst or multiple responsible analysts?

**Answer:** Recommend one primary responsible analyst, with zero or more additional contributors/participants.

**Status:** CLOSED — RECONCILED BASELINE



### Q210. Can assignment be changed after execution begins?

**Answer:** Assignment may be changed before or during execution under controlled conditions. Changes after execution begins must retain history and reason.

**Status:** CLOSED — RECONCILED BASELINE



### Q211. What happens to previous assignment history?

**Answer:** Previous assignment history remains permanently traceable; it is never overwritten.

**Status:** CLOSED — RECONCILED BASELINE



### Q212. Are assignment queues required?

**Answer:** Yes, assignment/work queues are required.

**Status:** CLOSED — RECONCILED BASELINE



### Q213. How is workload prioritized?

**Answer:** Workload is prioritized using controlled priority + due date + operational rules; priority must not be an arbitrary analyst decision.

**Status:** CLOSED — RECONCILED BASELINE



### Q214. Is due date tracking required?

**Answer:** Yes, due-date tracking is required.

**Status:** CLOSED — RECONCILED BASELINE



### Q215. Are turnaround-time rules required?

**Answer:** Yes, TAT rules are required.

**Status:** CLOSED — RECONCILED BASELINE



### Q216. What events pause or restart turnaround time?

**Answer:** TAT starts/stops from controlled lifecycle events; pauses occur for configured external/customer/laboratory hold conditions and resume on the defined release event.

**Status:** CLOSED — RECONCILED BASELINE



### Q217. Are overdue TestInstances escalated?

**Answer:** Yes, overdue TestInstances should be visibly escalated.

**Status:** CLOSED — RECONCILED BASELINE



### Q218. Who can change priority?

**Answer:** Priority may be changed only by authorized users; reason and audit history required for significant changes.

**Status:** CLOSED — RECONCILED BASELINE



### Q219. Are customer priority requests supported?

**Answer:** Yes, customer priority requests may be captured, but they do not automatically override laboratory priority or technical controls.

**Status:** CLOSED — RECONCILED BASELINE



### Q220. What is the exact lifecycle of a TestInstance?

**Answer:** The TestInstance is a controlled state machine. Normal path: **Created → Assigned → In Execution → Result Ready → PendingReview → Reviewed → PendingVerification → Verified → PendingApproval → Approved**. Exceptional states include Hold, Rework, Cancelled and Reopened. Repeat/Retest/re-execution create new TestInstances; eligible pre-approval Rework remains on the same TestInstance; post-approval Correction uses controlled Reopen and a Correction revision. Unlisted transitions are forbidden.

**Status:** CLOSED — RECONCILED BASELINE



### Q221. What transitions are legal?

**Answer:** A transition is legal only when explicitly listed in the authoritative state/transition matrix and all guards pass, including actor authorization, active competence where required, required data/calculations, SoD, reason/evidence and applicable TestDefinition/workflow rules. Backend/domain logic is authoritative for enforcement.

**Status:** CLOSED — RECONCILED BASELINE



### Q222. What transitions are forbidden?

**Answer:** Any transition not explicitly listed as legal is forbidden. The system must not bypass Review/Verification/Approval, bypass hard SoD, alter an Approved state in place, create a result without required inputs, or convert a cancelled/exceptional execution into normal completion without controlled disposition.

**Status:** CLOSED — RECONCILED BASELINE



### Q223. Which transitions require a reason?

**Answer:** A reason shall be mandatory for transitions that represent an exception, deviation, reversal, cancellation, correction, or other non-routine action.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q224. Which transitions require another authorized person?

**Answer:** The Master State / Transition Matrix + Execution Semantics Decision Table shall identify transitions that require another authorized person.

At minimum, a second authorized person shall be required where the transition involves:
- Review, Verification, or Approval under the approved SoD policy;
- reopening an approved TestInstance;
- correction approval where the correction affects an approved technical result;
- exceptional or policy-controlled SoD actions requiring independent authorization;
- emergency exceptions to policy-controlled actions, where such exceptions are permitted.

Routine workflow transitions shall not require unnecessary dual approval unless the approved workflow or SoD policy explicitly requires it.

The required second person, authorization level, independence requirement, and applicable SoD restriction shall be explicitly defined in the authoritative matrix.

**Status:** CLOSED — RECONCILED BASELINE



### Q225. Which transitions generate audit events?

**Answer:** The audit write path is centralized in one `AuditService`/repository. Normal business changes write audit data in the same transaction. Authentication, permission and SoD denied attempts use a short autonomous transaction because there is no business change to attach. Denials belong in `audit_event`; technical approval-chain decisions belong in `approval_chain_event`.

**Status:** CLOSED — RECONCILED BASELINE



### Q226. Which states are terminal?

**Answer:** Approved is the **normal forward terminal state**. Only the controlled Reopen path may leave Approved, and reopening preserves the earlier approved state and triggers the required correction/review/verification/approval controls.

**Status:** CLOSED — RECONCILED BASELINE



### Q227. Which states allow rework?

**Answer:** Controlled rework shall be permitted only from states where the technical work may legitimately require correction or additional execution.
At minimum, rework shall be available for applicable execution and failed-review/failed-verification conditions where the underlying work can be corrected without creating an uncontrolled history change.
Post-approval changes shall not use ordinary rework. They shall proceed through the controlled **Reopen / Correction process.**
Rework shall preserve the prior state, reason, actor, timestamp, affected records, and subsequent re-execution history.

**Status:** CLOSED — RECONCILED BASELINE



### Q228. Which states allow reopening?

**Answer:** Reopening shall be a controlled exceptional transition rather than a general backward status change.
For v1, the primary reopening state shall be **Approved.**
A TestInstance may move from Approved into the authorized correction/rework path only through a controlled reopen process with reason, authorization, audit, and preservation of the prior approved state.
Pre-approval problems shall normally use the applicable rework/correction transition rather than the formal Reopen transition.

**Status:** CLOSED — RECONCILED BASELINE



### Q229. Which states allow cancellation?

**Answer:** TestInstance cancellation shall be a controlled transition available only while the TestInstance has not reached an approved final state and where cancellation is permitted by the applicable workflow.

Cancellation may be permitted from appropriate pre-approval states such as:
- Created/Planned;
- Assigned;
- In Execution;
- Hold;
- Rework;
- other explicitly authorized pre-approval states.

Cancellation after execution has begun shall preserve all work already performed and require a reason and appropriate authorization.

An Approved TestInstance shall not be returned to Cancelled through an ordinary cancellation transition; any post-approval disposition shall use the controlled reopen/correction/report-governance path.

**Status:** CLOSED — RECONCILED BASELINE



### Q230. Which state transitions are reversible?

**Answer:** A TestInstance transition shall be considered reversible only where the Master State / Transition Matrix explicitly defines a valid controlled return path.

Reversibility shall not mean editing the previous state or deleting the transition history.

Examples of controlled reversible behavior may include:
- Hold → permitted working state;
- failed Review/Verification → controlled Rework/Correction path;
- controlled assignment changes;
- other explicitly approved workflow returns.

Approved, Cancelled, or other normal forward terminal states shall not be reversed by simply editing the status.

**Status:** CLOSED — RECONCILED BASELINE



### Q231. Which transitions are irreversible?

**Answer:** A transition shall be considered irreversible at the historical-event level once recorded: prior transition events shall never be deleted or rewritten.

At the workflow level, the following shall be treated as normal forward terminal states for v1:
- Approved;
- Cancelled, where the applicable cancellation path has completed.

Neither state may be changed directly into an earlier ordinary workflow state.

Where a later action is legitimately required, it shall use the appropriate controlled mechanism such as Reopen, Correction, or a new TestInstance rather than reversing the historical event.

**Status:** CLOSED — RECONCILED BASELINE



### Q232. What is the definition of a Method?

**Answer:** Method is the stable identity of a defined laboratory analytical or testing methodology, independent of the specific revision or edition used at a particular point in time.

**Status:** CLOSED — RECONCILED BASELINE



### Q233. What is the definition of a MethodVersion?

**Answer:** MethodVersion is a controlled technical version of a Method that defines the exact method reference, edition/revision, laboratory implementation, technical instructions, applicability, and effective period under which laboratory work may be performed.

**Status:** CLOSED — RECONCILED BASELINE



### Q234. What identifies one Method uniquely?

**Answer:** Globally unique internal Method ID; additionally a controlled human-readable Method Code.

**Status:** CLOSED — RECONCILED BASELINE



### Q235. What identifies one MethodVersion uniquely?

**Answer:** Globally unique internal MethodVersion ID plus unique version designation within its Method.

**Status:** CLOSED — RECONCILED BASELINE



### Q236. Which fields belong to Method versus MethodVersion?

**Answer:** Method and MethodVersion shall have clearly separated responsibilities.

**Method** represents the stable identity of the laboratory methodology, independent of a particular edition/revision.

**MethodVersion** represents the controlled technical version actually applicable to laboratory work. It contains the exact edition/revision, technical implementation, applicability, effective period, approval/evidence references, and other version-specific attributes.

The authoritative relationship is:
**Method → MethodVersion**

Method shall not contain mutable fields that actually describe one specific technical revision. MethodVersion shall contain the properties whose meaning may change between controlled revisions.
Do not add redundant predecessor/successor/version-history columns merely for convenience. Historical relationships shall be reconstructed through the version records and effective history.

**Status:** CLOSED — RECONCILED BASELINE



### Q237. How is an external standard/method reference represented?

**Answer:** Structured fields: issuing organization, standard/method number, title, edition/year, amendment/corrigendum, relevant section/clause, source/document reference.

**Status:** CLOSED — RECONCILED BASELINE



### Q238. How is a method edition or revision represented?

**Answer:** Represented explicitly on MethodVersion, never by overwriting the previous edition.

**Status:** CLOSED — RECONCILED BASELINE



### Q239. When does a method change require a new MethodVersion?

**Answer:** Any controlled technical change that can affect how the laboratory performs the method, evaluates data, calculates results, interprets results, determines applicability, uses required equipment/materials, or meets defined performance requirements shall create a new MethodVersion. When there is doubt whether a change affects technical meaning, treat it as a new MethodVersion.

**Status:** CLOSED — RECONCILED BASELINE



### Q240. Can a MethodVersion be edited after it is effective?

**Answer:** No substantive editing. Effective technical content is immutable. Controlled correction requires a new version or formally controlled administrative correction where technically harmless.

**Status:** CLOSED — RECONCILED BASELINE



### Q241. What happens when a MethodVersion is retired?

**Answer:** The MethodVersion is no longer permitted for new TestInstances after its retirement/effective-end point, but remains permanently available for historical reconstruction.

**Status:** CLOSED — RECONCILED BASELINE



### Q242. Can historical TestInstances use a retired MethodVersion?

**Answer:** Yes. Always preserve the original MethodVersion used.

**Status:** CLOSED — RECONCILED BASELINE



### Q243. How is method status represented?

**Answer:** Method and MethodVersion status should be represented separately.

**Status:** CLOSED — RECONCILED BASELINE



### Q244. What states can a MethodVersion have?

**Answer:** Draft → Under Review → Approved → Effective → Retired/Superseded.

**Status:** CLOSED — RECONCILED BASELINE



### Q245. Who approves a new MethodVersion?

**Answer:** Laboratory Technical Authority, with Quality involvement where QMS/accreditation control requires it.

**Status:** CLOSED — RECONCILED BASELINE



### Q246. Who approves method revisions?

**Answer:** Same technical authority; Quality approval where the revision affects controlled QMS/accreditation/reporting requirements

**Status:** CLOSED — RECONCILED BASELINE



### Q247. Is method validation/verification evidence stored in the LIMS?

**Answer:** Yes. Evidence records and/or controlled documents must be linked to the specific MethodVersion.

**Status:** CLOSED — RECONCILED BASELINE



### Q248. Is a method allowed to become effective before approval evidence is attached?

**Answer:** No. Required verification/validation and approval evidence must exist before the version becomes effective.

**Status:** CLOSED — RECONCILED BASELINE



### Q249. Are method documents linked to MethodVersion?

**Answer:** Yes, to MethodVersion through exact DocumentVersion.

**Status:** CLOSED — RECONCILED BASELINE



### Q250. Are internal laboratory SOP versions linked to MethodVersion?

**Answer:** Yes, exact SOP/document version linked to the MethodVersion.

**Status:** CLOSED — RECONCILED BASELINE



### Q251. What happens if an external method standard changes?

**Answer:** Review impact → create/adopt appropriate MethodVersion → verify again → approve → make effective.

**Status:** CLOSED — RECONCILED BASELINE



### Q252. Does the system need to track obsolete/superseded methods?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q253. Must method applicability be effective-dated?

**Answer:** Yes.

---

# 10. TestDefinition

**Status:** CLOSED — RECONCILED BASELINE



### Q254. What exactly is a TestDefinition?

**Answer:** TestDefinition is the controlled definition of a laboratory test or service that may be requested and executed for a Sample, specifying its technical method relationship, required parameters, prerequisites, equipment requirements, applicable rules, and reporting representation.

**Status:** CLOSED — RECONCILED BASELINE



### Q255. What identifies a TestDefinition uniquely?

**Answer:** `TestDefinition` is versioned by row using `test_code` plus `version_no`, with `UNIQUE(test_code, version_no)`. Each version belongs to exactly one MethodVersion. Effective periods for a test code must not overlap, and historical TestInstances retain the exact version they used.

**Status:** CLOSED — RECONCILED BASELINE



### Q256. Can one MethodVersion contain multiple TestDefinitions?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q257. Can one TestDefinition ever reference more than one MethodVersion?

**Answer:** A semantic change or a change of MethodVersion association creates a **new TestDefinition version** with controlled approval/effective dating. An existing production TestDefinition row is never repointed to a different MethodVersion because that would damage historical reconstruction.

**Status:** CLOSED — RECONCILED BASELINE



### Q258. What descriptive fields are required for a TestDefinition?

**Answer:** TestDefinition ID, code, technical name, customer-facing name, status, description, discipline/matrix applicability, MethodVersion, and relevant configuration references.

**Status:** CLOSED — RECONCILED BASELINE



### Q259. Is there a customer-facing test name separate from the technical test name?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q260. Is a test code required?

**Answer:** The logical test code may recur across versions; uniqueness is enforced at `(test_code, version_no)`. This permits controlled evolution while preserving exact historical TestDefinition identity.

**Status:** CLOSED — RECONCILED BASELINE



### Q261. Are synonyms or aliases required?

**Answer:** Yes, where useful for search/customer terminology; the controlled Test Code remains authoritative.

**Status:** CLOSED — RECONCILED BASELINE



### Q262. Can a TestDefinition be active/inactive/retired?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q263. Can a TestDefinition be changed after use?

**Answer:** Yes for controlled non-semantic metadata; no silent modification of technical meaning.

**Status:** CLOSED — RECONCILED BASELINE



### Q264. Which TestDefinition changes require versioning instead of editing?

**Answer:** A MethodVersion change that affects the technical meaning of a test requires a new TestDefinition version. Historical TestInstances remain linked to their original TestDefinition/MethodVersion chain.

**Status:** CLOSED — RECONCILED BASELINE



### Q265. Can TestDefinition requirements vary by sample matrix or discipline?

**Answer:** Yes. Test-specific rules may vary by matrix/discipline through controlled configuration.

**Status:** CLOSED — RECONCILED BASELINE



### Q266. Are test prerequisites required?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q267. Are required equipment types defined at TestDefinition level?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q268. Are required parameters defined at TestDefinition level?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q269. Are report display rules defined at TestDefinition level?

**Answer:** Yes, but detailed template/document versioning remains separate.

**Status:** CLOSED — RECONCILED BASELINE



### Q270. Is accreditation override defined at TestDefinition level exactly as specified?

**Answer:** Yes. TestDefinition-specific override targets the applicable MethodVersion and takes precedence over its default.

---

# 11. ParameterDefinition

**Status:** CLOSED — RECONCILED BASELINE



### Q271. What is a ParameterDefinition?

**Answer:** ParameterDefinition is a controlled definition of a data element required or permitted for a TestDefinition, including its semantic meaning, data type, unit rules, validation rules, precision, applicability, and reporting behavior.

**Status:** CLOSED — RECONCILED BASELINE



### Q272. What uniquely identifies a ParameterDefinition?

**Answer:** Globally unique internal ParameterDefinition ID + stable Parameter Code.

**Status:** CLOSED — RECONCILED BASELINE



### Q273. Which parameter data types are required?

**Answer:** Numeric decimal, integer, text, boolean, date, datetime, controlled single-selection; multi-selection only where a genuine multi-valued concept exists.

**Status:** CLOSED — RECONCILED BASELINE



### Q274. Are parameters numeric, text, boolean, date/time, selection, or other types?

**Answer:** Support numeric, text, boolean, date/time and controlled selections; avoid arbitrary JSON/EAV types.

**Status:** CLOSED — RECONCILED BASELINE



### Q275. Which result values can have units?

**Answer:** Primarily numeric measurement/calculation quantities.

**Status:** CLOSED — RECONCILED BASELINE



### Q276. Are units centrally controlled?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q277. Are parameter units versioned?

**Answer:** Unit definitions should be controlled/immutable; don't version every use. A materially different unit definition gets a new controlled unit.

**Status:** CLOSED — RECONCILED BASELINE



### Q278. Can one parameter have multiple allowed units?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q279. Is unit conversion required?

**Answer:** Yes, with a canonical unit and controlled conversion rules.

**Status:** CLOSED — RECONCILED BASELINE



### Q280. Who defines allowed input ranges?

**Answer:** Laboratory Technical Authority/method owner, based on the approved method and laboratory policy.

**Status:** CLOSED — RECONCILED BASELINE



### Q281. Are warning limits different from hard acceptance limits?

**Answer:** Yes, distinctly modeled.

**Status:** CLOSED — RECONCILED BASELINE



### Q282. Are decimal precision and display precision distinct?

**Answer:** Yes, distinct.

**Status:** CLOSED — RECONCILED BASELINE



### Q283. Is rounding applied during calculation or only display?

**Answer:** Calculation only where method explicitly requires it; otherwise preserve precision internally and round for controlled final reporting/display.

**Status:** CLOSED — RECONCILED BASELINE



### Q284. Must the unrounded value be preserved?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q285. Are significant figures required?

**Answer:** Support as method/configuration-specific; not universally mandatory.

**Status:** CLOSED — RECONCILED BASELINE



### Q286. Are below-detection-limit values required?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q287. How are non-detects represented?

**Answer:** Structured qualifier + detection limit/decision value where applicable; never rely on text such as "<0.1" as the underlying value.

**Status:** CLOSED — RECONCILED BASELINE



### Q288. How are less-than/greater-than qualifiers stored?

**Answer:** Store as structured qualifiers, separately from the numeric value.

**Status:** CLOSED — RECONCILED BASELINE



### Q289. Are qualitative result categories required?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q290. Are reference ranges required?

**Answer:** Yes, where applicable, but distinguish them from acceptance/specification limits.

**Status:** CLOSED — RECONCILED BASELINE



### Q291. Are customer-specific reference ranges required?

**Answer:** The data model distinguishes **reference intervals**, **specification/acceptance limits**, and **customer display preferences**. They have different semantics and must not be conflated in result interpretation, workflow or reporting.

**Status:** CLOSED — RECONCILED BASELINE



### Q292. Are matrix-specific parameter rules required?

**Answer:** Yes.

**Status:** CLOSED — RECONCILED BASELINE



### Q293. Are parameter comments/remarks required?

**Answer:** Yes, but comments cannot replace structured technical fields.

**Status:** CLOSED — RECONCILED BASELINE



### Q294. Are required parameters mandatory before result submission?

**Answer:** Yes before result submission, unless explicitly marked Not Applicable through a controlled rule.

**Status:** CLOSED — RECONCILED BASELINE



### Q295. Can a parameter be not applicable for a specific TestInstance?

**Answer:** Yes, where permitted by configuration, with reason.

**Status:** CLOSED — RECONCILED BASELINE



### Q296. Who can override a parameter-level validation rule?

**Answer:** Ordinary analysts should not bypass hard validation. Warnings may be acknowledged; hard business/technical constraints require controlled policy/configuration or authorized technical disposition.

---

# 12. Formula and Calculation Engine

**Status:** CLOSED — RECONCILED BASELINE



### Q297. Which tests require calculated results?

**Answer:** Laboratory-configurable. The laboratory defines through controlled configuration which TestDefinitions produce calculated results. No test is assumed to require calculation unless configured and approved.

**Status:** CLOSED — RECONCILED BASELINE



### Q298. What formulas are currently used by the laboratory?

**Answer:** Laboratory-configurable. Authorized laboratory technical personnel enter or define formulas through a controlled FormulaVersion mechanism. Approved laboratory methods/SOPs remain the authoritative source for the formula; LabNexus does not invent formulas.

**Status:** CLOSED — RECONCILED BASELINE



### Q299. Which formulas depend on other results?

**Answer:** Each CalculationRun preserves deterministic provenance sufficient to reconstruct the calculation: exact FormulaVersion, input snapshot, parameter identities/units, constants or controlled lookup dependencies, engine/runtime identity, execution timestamp and output linkage. Historical calculations never depend on rereading current mutable configuration.

**Status:** CLOSED — RECONCILED BASELINE



### Q300. Which formulas depend on sample metadata?

**Answer:** Yes. A formula may use configured Sample/Request/TestInstance metadata where the selected method requires it. The laboratory selects which metadata fields are valid inputs.

**Status:** CLOSED — RECONCILED BASELINE



### Q301. Which formulas depend on equipment values?

**Answer:** Yes. Formulas may use controlled equipment values, such as approved calibration/correction values. The laboratory configures which equipment values are inputs.

**Status:** CLOSED — RECONCILED BASELINE



### Q302. Which formulas depend on environmental conditions?

**Answer:** Yes. Environmental-condition values may be used where applicable. The laboratory defines whether they are required for a particular test/formula.

**Status:** CLOSED — RECONCILED BASELINE



### Q303. Which formulas depend on constants or correction factors?

**Answer:** Yes. Constants and correction factors are controlled configuration objects with their own values, units, effective dates, approval and history.

**Status:** CLOSED — RECONCILED BASELINE



### Q304. Which formulas require conditional logic?

**Answer:** Yes. Conditional logic is supported through a restricted expression mechanism. The laboratory configures the conditions; arbitrary programming is prohibited.

**Status:** CLOSED — RECONCILED BASELINE



### Q305. Which formulas require lookup tables?

**Answer:** Yes. Controlled lookup tables are supported and configured by the laboratory. Lookup-table versions used by a calculation are preserved.

**Status:** CLOSED — RECONCILED BASELINE



### Q306. Which formulas require averaging?

**Answer:** Yes. Averaging/aggregation functions are engine capabilities; the laboratory determines where and how they are used.

**Status:** CLOSED — RECONCILED BASELINE



### Q307. Which formulas require replicate handling?

**Answer:** Yes. Replicate handling is supported as a configured rule. The laboratory defines how replicate observations are combined for each applicable test.

**Status:** CLOSED — RECONCILED BASELINE



### Q308. Which formulas require blank correction?

**Answer:** Yes. Blank correction is a reusable engine capability. The laboratory configures whether and how a particular test uses it.

**Status:** CLOSED — RECONCILED BASELINE



### Q309. Which formulas require recovery correction?

**Answer:** Yes. Recovery correction is supported as a reusable capability and configured only where required.

**Status:** CLOSED — RECONCILED BASELINE



### Q310. Which formulas require moisture/dry-basis conversion?

**Answer:** Yes. Moisture/dry-basis conversion is supported as a reusable calculation mechanism; the laboratory defines which basis conversions each test requires.

**Status:** CLOSED — RECONCILED BASELINE



### Q311. Which formulas require unit conversion?

**Answer:** Yes. Unit conversion is a core engine capability; allowed units and conversion paths are controlled configuration.

**Status:** CLOSED — RECONCILED BASELINE



### Q312. Which formulas require significant-figure rules?

**Answer:** Yes. Significant-figure rules are configurable per applicable test/result/parameter.

**Status:** CLOSED — RECONCILED BASELINE



### Q313. Which formulas require rounding at intermediate steps?

**Answer:** Yes. Intermediate rounding is configurable, but only the approved formula/method can require it.

**Status:** CLOSED — RECONCILED BASELINE



### Q314. Which formulas require rounding only at final output?

**Answer:** Yes. Final-output rounding can be configured by the laboratory.

**Status:** CLOSED — RECONCILED BASELINE



### Q315. What formula language/expression syntax should be supported?

**Answer:** Use a restricted declarative formula language provided by LabNexus. The laboratory enters formulas using that language; it does not write Python/JavaScript/SQL.

**Status:** CLOSED — RECONCILED BASELINE



### Q316. What operations are allowed in the constrained evaluator?

**Answer:** The evaluator should support controlled arithmetic, comparison, Boolean logic, approved functions, conditionals, parameter references and controlled lookups.

**Status:** CLOSED — RECONCILED BASELINE



### Q317. What operations are prohibited?

**Answer:** Arbitrary code execution, imports, file/network access, SQL, OS commands, dynamic execution, reflection and mutation are prohibited.

**Status:** CLOSED — RECONCILED BASELINE



### Q318. Are functions such as sqrt, log, exp, min, max, abs, round required?

**Answer:** The engine should provide a controlled function library such as ABS, MIN, MAX, SQRT, ROUND; additional functions such as LOG, LOG10, EXP, POW can be enabled in the platform when genuinely required. The laboratory does not create arbitrary functions.

**Status:** CLOSED — RECONCILED BASELINE



### Q319. Are conditional expressions required?

**Answer:** Yes. Conditional expressions are supported through the restricted formula language.

**Status:** CLOSED — RECONCILED BASELINE



### Q320. Are loops or recursion forbidden explicitly?

**Answer:** Yes. Explicitly forbidden. No loops or recursion.

**Status:** CLOSED — RECONCILED BASELINE



### Q321. How are formula inputs named?

**Answer:** Formula inputs use stable Parameter Codes and other controlled tokens/namespaces, not raw database IDs or arbitrary field names.

**Status:** CLOSED — RECONCILED BASELINE



### Q322. How are missing inputs handled?

**Answer:** Missing required inputs must block calculation unless the applicable configured rule explicitly permits absence. Missing, zero, N/A and non-detect remain distinct states.

**Status:** CLOSED — RECONCILED BASELINE



### Q323. How are divide-by-zero or invalid-input conditions handled?

**Answer:** Divide-by-zero, invalid units, missing dependencies and other invalid conditions cause a controlled calculation failure; they never silently become zero, null or another fabricated value.

**Status:** CLOSED — RECONCILED BASELINE



### Q324. How are calculation failures presented to users?

**Answer:** The user sees a clear business/technical message; detailed diagnostics remain in controlled technical evidence/logging and are not exposed as raw stack traces.

**Status:** CLOSED — RECONCILED BASELINE



### Q325. Who can define formulas?

**Answer:** Authorized laboratory technical users define formulas through the application. They do not modify source code.

**Status:** CLOSED — RECONCILED BASELINE



### Q326. Who can approve a FormulaVersion?

**Answer:** Authorized Laboratory Technical Authority approves FormulaVersion. Quality involvement is added where the formula affects controlled QMS/accreditation/reporting requirements.

**Status:** CLOSED — RECONCILED BASELINE



### Q327. Can formulas be changed after use?

**Answer:** A FormulaVersion shall never be changed in place after it has been used for an authoritative CalculationRun.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q328. What makes a new FormulaVersion necessary?

**Answer:** Yes. Every authoritative CalculationRun shall store the **exact FormulaVersion** used.
The relationship shall be explicit and immutable.
A CalculationRun shall not merely store the current formula ID because that would make later formula changes capable of changing historical interpretation.
The FormulaVersion reference shall identify the exact controlled formula version effective for that calculation.

**Status:** CLOSED — RECONCILED BASELINE



### Q329. Must each calculation run store the formula version used?

**Answer:** Yes. Every authoritative CalculationRun shall preserve an **input snapshot sufficient to reproduce and audit the calculation**.
The snapshot shall include the actual values used, not merely references to mutable current values.
Where an input is itself a controlled result/configuration, the snapshot shall also retain its historical identity/version reference.
The objective is deterministic historical reconstruction without depending on current mutable state.

**Status:** CLOSED — RECONCILED BASELINE



### Q330. Must each calculation run store input snapshots?

**Answer:** Yes. The calculation engine shall have deterministic behavior for a given CalculationRun, controlled FormulaVersion, input snapshot, and relevant configuration/version context.
Historical results must not become dependent on whichever future software version happens to recalculate them.
Where calculation-engine behavior changes materially, the engine/version identity shall change and existing CalculationRuns shall remain associated with the engine version under which they were originally performed.
Historical calculations shall not be silently recomputed merely because the calculation engine was upgraded.

**Status:** CLOSED — RECONCILED BASELINE



### Q331. Must the calculation engine be deterministic across future software versions?

**Answer:** The calculation engine version shall be recorded explicitly for every authoritative CalculationRun.

The recorded engine identity should include sufficient information to distinguish materially different execution behavior, such as:
* Application/release version;
* Calculation-engine version;
* Formula-evaluation implementation version where separately controlled.

The exact implementation need not reproduce the entire application package inside every CalculationRun, but it must provide an immutable reference to the controlled software version capable of identifying the relevant execution behavior.

**Status:** CLOSED — RECONCILED BASELINE



### Q332. How is calculation engine version tracked?

**Answer:** Each CalculationRun shall retain a deterministic evidence bundle containing, as applicable:
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

**Status:** CLOSED — RECONCILED BASELINE



### Q333. What evidence is retained for a calculation run?

**Answer:** A completed calculation shall produce an immutable CalculationRun record.
Failed execution shall also be preserved as an execution event/evidence record where required for auditability.
The CalculationRun shall be linked to the resulting ResultRevision where a result was produced. Re-execution after correction or controlled change shall create a new CalculationRun rather than overwrite the earlier one.

**Status:** CLOSED — RECONCILED BASELINE



### Q334. How are manually entered versus automatically calculated values distinguished?

**Answer:** Yes. Observed, calculated, imported and explicitly adjusted values are distinguished by provenance metadata.

**Status:** CLOSED — RECONCILED BASELINE



### Q335. Can an authorized user override a calculated result?

**Answer:** Yes, manual calculation adjustment may exist only where explicitly enabled/approved for named tests/parameters and must preserve the calculated provenance.

**Status:** CLOSED — RECONCILED BASELINE



### Q336. If yes, under what conditions and with what evidence?

**Answer:** Where manual calculation adjustment is permitted, all of the following conditions shall apply:
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

**Status:** CLOSED — RECONCILED BASELINE



### Q337. Can a calculated result be manually corrected after approval?

**Answer:** Yes, but only through controlled reopen/correction. An approved calculated result is never edited in place. A new CalculationRun/ResultRevision is created where appropriate, followed by required review/verification/approval.

**Status:** CLOSED — RECONCILED BASELINE



### Q338. Which calculation outputs are reportable?

**Answer:** Configurable. The laboratory defines which outputs are reportable. Intermediate calculations and internal inputs remain in the technical record unless explicitly configured for reporting.

---

# 13. Result Model and Revision Rules

**Status:** CLOSED — RECONCILED BASELINE



### Q339. What exactly is the current live Result state?

**Answer:** Historical result state is represented through immutable ResultRevision records rather than a mutable pointer on Result. The current live Result is not a substitute for historical evidence.

**Status:** CLOSED — RECONCILED BASELINE



### Q340. Which values belong to Result versus ResultRevision?

**Answer:** Result holds stable identity and current-state representation; ResultRevision holds immutable historical snapshots of technical result state, including revision type and provenance.

**Status:** CLOSED — RECONCILED BASELINE



### Q341. Which fields are immutable after result submission?

**Answer:** Result identity, TestInstance linkage, and historical revision records become immutable after controlled creation; technical values cannot be silently overwritten after submission.

**Status:** CLOSED — RECONCILED BASELINE



### Q342. Which fields may be edited before review?

**Answer:** Before Review, permitted technical fields may be edited according to TestDefinition/workflow configuration, with audit history.

**Status:** CLOSED — RECONCILED BASELINE



### Q343. Which fields may be edited after review?

**Answer:** After Review, ordinary editing is blocked; changes require controlled rework/correction according to the affected field and workflow state.

**Status:** CLOSED — RECONCILED BASELINE



### Q344. Which fields may be edited after verification?

**Answer:** After Verification, ordinary editing is blocked; changes require controlled reopening/rework/correction and renewed verification where applicable.

**Status:** CLOSED — RECONCILED BASELINE



### Q345. Which fields may be edited after approval?

**Answer:** After Approval, no ordinary editing is permitted. Changes require controlled reopen/correction and a new approval cycle.

**Status:** CLOSED — RECONCILED BASELINE



### Q346. What exactly triggers a Correction revision?

**Answer:** `ResultRevision` is append-only and its revision type is limited to **Correction** and **ApprovalSnapshot**. Generic Void/Superseded revision types are not introduced by inference. Revision numbers are sequential per Result across both types.

**Status:** CLOSED — RECONCILED BASELINE



### Q347. What exactly triggers an ApprovalSnapshot revision?

**Answer:** An **ApprovalSnapshot ResultRevision** shall be created when an approved technical state must be frozen as the authoritative approved result representation.
Each approval shall be associated with the exact approved ResultRevision and shall produce the corresponding immutable ApprovalSnapshot.
The snapshot shall preserve the result information necessary to reconstruct exactly what was approved, including applicable result value/qualifier/unit, TestDefinition/MethodVersion representation, relevant analyst/approval identity, accreditation representation, timestamps, and associated calculation/result provenance as required.
An ApprovalSnapshot must never be rewritten after approval.

**Status:** CLOSED — RECONCILED BASELINE



### Q348. Must every approved result create an ApprovalSnapshot?

**Answer:** Yes. **Every successful Approval of a technical Result shall create an ApprovalSnapshot.**
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

**Status:** CLOSED — RECONCILED BASELINE



### Q349. Can an ApprovalSnapshot exist without an approval event?

**Answer:** An ApprovalSnapshot and its successful approval-chain event are created atomically. A partial uniqueness rule ensures a snapshot cannot acquire multiple successful approval events, and verification must find zero orphan snapshots.

**Status:** CLOSED — RECONCILED BASELINE



### Q350. Can a Correction exist without a formal reopen/correction event?

**Answer:** The ApprovalSnapshot freezes the technical state that was approved, including value, qualifier, unit, rounded value, TestDefinition/MethodVersion representation, analyst representation, resolved accreditation and approval time. It is immutable evidence of the approved state.

**Status:** CLOSED — RECONCILED BASELINE



### Q351. How are revision numbers assigned?

**Answer:** ResultRevision numbers are assigned by the system, sequentially per Result, within the transaction that creates the revision.

**Status:** CLOSED — RECONCILED BASELINE



### Q352. Are revision numbers strictly sequential?

**Answer:** Yes. Revision numbers are strictly sequential per Result: 1, 2, 3… with no reused number.

**Status:** CLOSED — RECONCILED BASELINE



### Q353. Can revisions ever be deleted?

**Answer:** No revisions may ever be deleted.

**Status:** CLOSED — RECONCILED BASELINE



### Q354. Can revisions ever be voided?

**Answer:** Pre-review edits are audited without creating ResultRevision rows. The first successful approval creates revision 1 as an ApprovalSnapshot; later controlled correction creates the next revision. Revision history is append-only and historically reconstructable.

**Status:** CLOSED — RECONCILED BASELINE



### Q355. If a correction is rejected, is a revision created anyway or only an event recorded?

**Answer:** If a correction request is rejected, no Correction ResultRevision is created; the request/rejection itself is preserved as an event/audit record.

**Status:** CLOSED — RECONCILED BASELINE



### Q356. How are correction reasons classified?

**Answer:** Separate technical-result correction from report/document correction and report representation errors.

**Status:** CLOSED — RECONCILED BASELINE



### Q357. Who may request a correction?

**Answer:** Authorized laboratory users who identify a problem may request a correction; ordinary users do not automatically receive approval authority.

**Status:** CLOSED — RECONCILED BASELINE



### Q358. Who may approve a correction?

**Answer:** Correction approval should be performed by the authorized Technical Authority or designated correction approver, with Quality involvement where required.

**Status:** CLOSED — RECONCILED BASELINE



### Q359. Does correction require technical review again?

**Answer:** Yes, where the correction could affect technical validity.

**Status:** CLOSED — RECONCILED BASELINE



### Q360. Does correction require verification again?

**Answer:** Yes, where the correction affects the verified technical content.

**Status:** CLOSED — RECONCILED BASELINE



### Q361. Does correction require a new approval?

**Answer:** Yes. Any correction that changes an already approved result requires new approval before re-release.

**Status:** CLOSED — RECONCILED BASELINE



### Q362. What happens to previously issued reports after a correction?

**Answer:** Separate technical-result correction from report/document correction and report representation errors.

**Status:** CLOSED — RECONCILED BASELINE



### Q363. Must a correction automatically identify affected reports?

**Answer:** Separate technical-result correction from report/document correction and report representation errors.

**Status:** CLOSED — RECONCILED BASELINE



### Q364. What report/revision consequences are mandatory after correction?

**Answer:** Separate technical-result correction from report/document correction and report representation errors.

**Status:** CLOSED — RECONCILED BASELINE



### Q365. Can a result be corrected without changing the report?

**Answer:** Separate technical-result correction from report/document correction and report representation errors.

**Status:** CLOSED — RECONCILED BASELINE



### Q366. What conditions permit or prohibit that?

**Answer:** Separate technical-result correction from report/document correction and report representation errors.

**Status:** CLOSED — RECONCILED BASELINE



### Q367. How is the current result identified when multiple historical revisions exist?

**Answer:** There is **no mutable `current_revision_id` stored on Result**. Historical revision is identified through immutable ResultRevision rows; the latest revision is derived from the maximum revision number.

**Status:** CLOSED — RECONCILED BASELINE



### Q368. How is a historical result revision reconstructed?

**Answer:** Historical ResultRevision reconstruction uses the immutable revision snapshot, its revision number/type, associated correction/reopen/approval event, and linked CalculationRun/ReportSnapshot data.

---

# 14. Review, Verification, and Approval

**Status:** CLOSED — RECONCILED BASELINE



### Q369. What exactly does Review mean in laboratory practice?

**Answer:** Review = technical examination of the completed test work/result for completeness, consistency, calculations, required observations, QC status, method compliance and obvious issues before verification.

**Status:** CLOSED — RECONCILED BASELINE



### Q370. What exactly does Verification mean?

**Answer:** Verification = independent confirmation that the result/test record satisfies defined technical and acceptance requirements and is suitable to proceed to Approval.

**Status:** CLOSED — RECONCILED BASELINE



### Q371. What exactly does Approval mean?

**Answer:** Approval = formal authorization that the verified result is approved for controlled reporting/release, creating the ApprovalSnapshot.

**Status:** CLOSED — RECONCILED BASELINE



### Q372. Who may perform Review?

**Answer:** Review is performed by an authorized Technical Reviewer.

**Status:** CLOSED — RECONCILED BASELINE



### Q373. Who may perform Verification?

**Answer:** Verification is performed by an authorized Technical Verifier.

**Status:** CLOSED — RECONCILED BASELINE



### Q374. Who may perform Approval?

**Answer:** Approval is performed by an authorized Approver/Authorized Signatory.

**Status:** CLOSED — RECONCILED BASELINE



### Q375. Are different roles required for the three stages?

**Answer:** The roles are logically distinct. Whether different individuals are always required is governed by the approved SoD policy; the hard Analyst restrictions remain mandatory.

**Status:** CLOSED — RECONCILED BASELINE



### Q376. What qualifications are required for each stage?

**Answer:** Each stage requires defined competence/authority appropriate to the activity.

**Status:** CLOSED — RECONCILED BASELINE



### Q377. Are qualifications represented in the LIMS?

**Answer:** Yes. Relevant competence/authorization status should be represented or referenced in LIMS.

**Status:** CLOSED — RECONCILED BASELINE



### Q378. What happens when a qualified person is unavailable?

**Answer:** Use the approved alternate-approver/authorized substitute path; never use an ad-hoc substitute.

**Status:** CLOSED — RECONCILED BASELINE



### Q379. What alternate-approver process is allowed?

**Answer:** Alternate must be predesignated, competent, authorized and not prohibited by SoD.

**Status:** CLOSED — RECONCILED BASELINE



### Q380. Exactly which combinations are hard-blocked by SoD?

**Answer:** Hard blocks: Analyst→Review, Analyst→Verification, Analyst→Approval on the same TestInstance.

**Status:** CLOSED — RECONCILED BASELINE



### Q381. Is Analyst → Review always blocked on the same TestInstance?

**Answer:** Always blocked.

**Status:** CLOSED — RECONCILED BASELINE



### Q382. Is Analyst → Verification always blocked on the same TestInstance?

**Answer:** Always blocked.

**Status:** CLOSED — RECONCILED BASELINE



### Q383. Is Analyst → Approval always blocked on the same TestInstance?

**Answer:** Always blocked.

**Status:** CLOSED — RECONCILED BASELINE



### Q384. What is the approved Reviewer → Technical Verification rule?

**Answer:** The v1 SoD Matrix is explicit, versioned and effective-dated. **Analyst→Review, Analyst→Verification and Analyst→Approval are hard BLOCKs; Reviewer→Verification is also a hard BLOCK.** Reviewer→Approval and Verifier→Approval are policy-controlled and default to BLOCK; any allowed exception requires the approved exception mechanism. Emergencies never bypass hard blocks.

**Status:** CLOSED — RECONCILED BASELINE



### Q385. Is Technical Reviewer → Approval allowed normally, blocked normally, or policy-controlled?

**Answer:** The earlier blanket/recommendation answer is superseded by the explicit SoD Matrix. Unlisted role/action combinations default to BLOCK unless the approved matrix defines an allowed transition.

**Status:** CLOSED — RECONCILED BASELINE



### Q386. What exact policy controls Technical Reviewer → Approval?

**Answer:** SoD is evaluated **per TestInstance** using the user's recorded actions, not merely by the roles a person possesses. Holding multiple roles is not itself a violation; performing a prohibited action combination on the same TestInstance is.

**Status:** CLOSED — RECONCILED BASELINE



### Q387. Which SoD combinations require countersigned exception evidence?

**Answer:** The normal controlled workflow must have enough distinct competent people to satisfy the approved Analyst/Reviewer/Verifier/Approver separation. Staffing feasibility is demonstrated through the controlled Role-Holder Matrix before affected workflows are activated.

**Status:** CLOSED — RECONCILED BASELINE



### Q388. Are there any legitimate emergency exceptions to policy-controlled combinations?

**Answer:** Any permitted SoD exception is effective-dated, attributable, independently justified and recorded with the SoD policy version used. A hard BLOCK can never be converted to ALLOW by an emergency flag.

**Status:** CLOSED — RECONCILED BASELINE



### Q389. What does the system do when an actor loses authorization between stages?

**Answer:** If an actor loses required authorization between workflow stages:
- the actor's next controlled action shall be blocked;
- previously completed and valid actions shall remain historical;
- the TestInstance shall remain in its current controlled state unless the loss of authorization itself requires a separate disposition;
- another currently authorized person may continue the workflow where permitted;
- the authorization change and blocked/continued workflow actions shall remain auditable.

The system shall not automatically invalidate previously recorded Review, Verification, or Approval events solely because the actor later lost authorization, unless an authorized policy/process determines that retrospective impact assessment is required.

**Status:** CLOSED — RECONCILED BASELINE



### Q390. Can an approval be revoked?

**Answer:** Approval may be revoked only through controlled revocation/reopen governance; never by deleting or editing the approval event.

**Status:** CLOSED — RECONCILED BASELINE



### Q391. If approval is revoked, what state follows?

**Answer:** Revocation leads to a controlled state such as ApprovalRevoked / ReopenedForCorrection, according to the reason and procedure.

**Status:** CLOSED — RECONCILED BASELINE



### Q392. Can a verified result be re-opened?

**Answer:** A verified result may be reopened only through authorized rework/correction procedure.

**Status:** CLOSED — RECONCILED BASELINE



### Q393. Can an approved result be re-opened?

**Answer:** An approved result may be reopened only through controlled correction/reopen procedure.

**Status:** CLOSED — RECONCILED BASELINE



### Q394. Who may reopen an approved TestInstance?

**Answer:** Reopening an approved TestInstance requires authorized Technical/Quality authority according to the reason and policy.

**Status:** CLOSED — RECONCILED BASELINE



### Q395. What reason is required for reopening?

**Answer:** Mandatory structured reason, explanation, impact assessment and authorizer.

**Status:** CLOSED — RECONCILED BASELINE



### Q396. Does reopening create an audit event, result revision, or both?

**Answer:** Reopening creates both an audit event and, where the technical Result changes, the appropriate ResultRevision; reopening itself is always audited.

**Status:** CLOSED — RECONCILED BASELINE



### Q397. What exactly is recorded in approval_chain_event?

**Answer:** approval_chain_event records each review/verification/approval/rejection/revocation/attempt event, with TestInstance, stage, actor, timestamp, outcome, reason/comments, authorization context and relevant ResultRevision/ApprovalSnapshot references.

**Status:** CLOSED — RECONCILED BASELINE



### Q398. Can the same stage be performed more than once?

**Answer:** Yes. A stage may be performed more than once, especially after rework/reopen.

**Status:** CLOSED — RECONCILED BASELINE



### Q399. If so, how are repeated attempts represented?

**Answer:** Each attempt is a separate immutable approval_chain_event with sequence/order information and outcome; successful completion advances the lifecycle.

**Status:** CLOSED — RECONCILED BASELINE



### Q400. How are rejected/failed review attempts preserved?

**Answer:** Failed Review attempts are preserved as events with outcome and reason/comments.

**Status:** CLOSED — RECONCILED BASELINE



### Q401. How are rejected/failed verification attempts preserved?

**Answer:** Failed Verification attempts are preserved similarly.

**Status:** CLOSED — RECONCILED BASELINE



### Q402. How are rejected/failed approval attempts preserved?

**Answer:** Failed Approval attempts are preserved similarly.

**Status:** CLOSED — RECONCILED BASELINE



### Q403. Are comments mandatory for failed stages?

**Answer:** Yes. Comments/reason are mandatory for failed/negative outcomes.

**Status:** CLOSED — RECONCILED BASELINE



### Q404. Are electronic acknowledgements/signatures required?

**Answer:** Yes. Controlled electronic acknowledgement/signature evidence should be required for Review, Verification and Approval according to the laboratory's approved policy.

**Status:** CLOSED — RECONCILED BASELINE



### Q405. If yes, what is the exact meaning of the electronic signature?

**Answer:** An electronic signature means a controlled, attributable act by an authenticated authorized user indicating that they performed the specified stage and accepted the recorded outcome at that time.

**Status:** CLOSED — RECONCILED BASELINE



### Q406. Is the secure user session sufficient evidence of user identity, or is re-authentication required for approval?

**Answer:** Fresh password re-entry is required for Approval/Reapproval, approval revocation, Reopen of an approved TestInstance, correction approval, report issue/reissue/withdrawal, controlled configuration approval, role-assignment approval, emergency declaration/countersign and database restore. Review and Verification require attributable server-side evidence but not password re-entry.

**Status:** CLOSED — RECONCILED BASELINE



### Q407. Is a second-factor or password re-entry required for high-risk actions?

**Answer:** Re-entry is an action-level server control, not merely a browser prompt. The server validates the fresh credential evidence in the same controlled transaction as the protected action and records the applicable evidence class. Any future re-authentication window must be introduced by controlled change and validation.

**Status:** CLOSED — RECONCILED BASELINE



### Q408. Must approval require a current password or session re-authentication?

**Answer:** Approval of a TestInstance's applicable result set is an atomic controlled decision linked to authorization, competence, SoD checks, re-entry evidence, ApprovalSnapshot and approval-chain event. A future short re-authentication window is not an unapproved default.

**Status:** CLOSED — RECONCILED BASELINE



### Q409. What constitutes an approval snapshot as distinct from a normal revision?

**Answer:** The ApprovalSnapshot is the immutable frozen approved state; the successful approval-chain event points to it. The snapshot does not point back to the event, avoiding circular foreign-key dependency.

**Status:** CLOSED — RECONCILED BASELINE



### Q410. What data must be frozen at approval?

**Answer:** Freeze all report/technical data needed to reconstruct exactly what was approved: Result value, qualifier, unit, precision/rounded value, TestDefinition representation, MethodVersion, relevant analyst representation, approval actor/time, applicable accreditation representation, calculation/result references and other required report-visible technical attributes.

---

# 15. Accreditation Scope

**Status:** CLOSED — RECONCILED BASELINE



### Q411. Which methods are currently within NABL scope?

**Answer:** Not hard-coded. At deployment, the laboratory imports/enters its current approved accreditation scope and maps applicable methods to its controlled MethodVersions.

**Status:** CLOSED — RECONCILED BASELINE



### Q412. Which MethodVersions are currently in scope?

**Answer:** Determined by the laboratory's configured accreditation-scope records and evidence. No MethodVersion is assumed accredited by LabNexus.

**Status:** CLOSED — RECONCILED BASELINE



### Q413. Which TestDefinitions are currently in scope?

**Answer:** Determined through the deployment's controlled scope configuration, including any TestDefinition-specific override.

**Status:** CLOSED — RECONCILED BASELINE



### Q414. Are all tests under a method automatically accredited unless overridden?

**Answer:** Not as a universal LabNexus assumption. The deployment may configure a MethodVersion-level default applicability, and a TestDefinition override may supersede it, exactly as your frozen hybrid architecture specifies.

**Status:** CLOSED — RECONCILED BASELINE



### Q415. Which tests require a non-accredited override?

**Answer:** The laboratory configures the specific TestDefinitions that must be treated as non-accredited despite the MethodVersion default.

**Status:** CLOSED — RECONCILED BASELINE



### Q416. Which tests require an accredited override?

**Answer:** The laboratory configures specific TestDefinitions as accredited where the approved scope warrants an override against the MethodVersion default.

**Status:** CLOSED — RECONCILED BASELINE



### Q417. Is the override always specific to a MethodVersion?

**Answer:** Yes. The TestDefinition override must belong to and explicitly identify the MethodVersion whose default it overrides.

**Status:** CLOSED — RECONCILED BASELINE



### Q418. What is the business meaning of an accreditation-scope record?

**Answer:** A controlled, effective-dated statement of the accreditation applicability configured for a specific deployment, framework, and MethodVersion/TestDefinition target, supported by evidence.

**Status:** CLOSED — RECONCILED BASELINE



### Q419. What fields are needed to display accreditation status on a report?

**Answer:** Resolved accreditation status, accreditation framework/body, applicable scope representation, target MethodVersion/TestDefinition, effective applicability, approved report wording/mark configuration, and required evidence/reference identifiers.

**Status:** CLOSED — RECONCILED BASELINE



### Q420. What effective date/time should scope changes use?

**Answer:** The laboratory enters the effective date/time from its approved accreditation evidence/decision. LabNexus stores it precisely for deterministic historical resolution.

**Status:** CLOSED — RECONCILED BASELINE



### Q421. Who can propose a scope change?

**Answer:** Accreditation applicability is resolved at the TestInstance's **execution start**, defined as the first transition to In Execution. The resolved state is preserved in the ApprovalSnapshot and ReportResultSnapshot and is not silently recomputed from later scope configuration.

**Status:** CLOSED — RECONCILED BASELINE



### Q422. Who can approve a scope change?

**Answer:** Accreditation-scope changes shall be approved by the designated Laboratory Quality Authority, with Technical Authority concurrence where the change affects technical method applicability.

The approval shall confirm:
- the supporting accreditation evidence;
- affected MethodVersion/TestDefinition records;
- effective date/time;
- applicability boundaries;
- impact on existing work;
- required report representation;
- any required controlled follow-up.

System administrators or implementation personnel shall not independently approve accreditation scope.

**Status:** CLOSED — RECONCILED BASELINE



### Q423. What evidence supports a scope change?

**Answer:** Evidence supporting an accreditation-scope change shall be linked to the controlled scope record and shall be sufficient to establish the authority, applicability, and effective date of the change.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q424. Can scope status be changed retrospectively?

**Answer:** Historical accreditation representation uses the scope record/version and resolution rule applicable at execution start. Later configuration changes do not alter the historical classification of work already started.

**Status:** CLOSED — RECONCILED BASELINE



### Q425. If yes, under what controlled process?

**Answer:** A retrospective accreditation correction requires controlled impact analysis and correction of the affected record/report path. The prior representation is retained; an issued report is never silently rewritten.

**Status:** CLOSED — RECONCILED BASELINE



### Q426. How are conflicting temporal scope records resolved?

**Answer:** Conflicting temporal accreditation-scope records shall not be resolved by arbitrary precedence or by mutable current state.

The applicable scope shall be determined by:
- identifying the relevant MethodVersion/TestDefinition target;
- resolving the effective-date/time intervals;
- applying the approved temporal-boundary rule;
- rejecting or flagging overlapping records where the overlap is not explicitly permitted;
- requiring controlled correction where conflicting records represent an invalid configuration.

A valid active scope state shall be deterministic for any given applicable date/time.
Historical TestInstances and reports shall resolve against the scope record that was effective for the relevant historical event according to the approved applicability rule.
No later scope configuration may silently rewrite the historical accreditation representation.

**Status:** CLOSED — RECONCILED BASELINE



### Q427. What happens when a MethodVersion expires or is retired?

**Answer:** When a MethodVersion expires or is retired, it shall no longer be available for new TestInstances after its effective end/retirement point.
Existing TestInstances that legitimately reference the MethodVersion shall retain that original MethodVersion and remain historically reconstructable.
Retirement shall not delete, alter, or invalidate historical method or accreditation records.
Where retirement affects an in-progress TestInstance, the applicable disposition shall be determined through controlled laboratory/technical rules rather than by automatically replacing the MethodVersion.

**Status:** CLOSED — RECONCILED BASELINE



### Q428. What happens to existing TestInstances when scope changes after testing?

**Answer:** A change in accreditation scope after testing has begun shall not automatically rewrite the accreditation status of an existing TestInstance.

The system shall preserve the scope state applicable to the relevant historical activity and shall identify the impact of any later scope change on:
- existing TestInstances;
- results;
- approvals;
- report revisions;
- issued reports.

Where the scope change affects work that has not yet reached the relevant controlled stage, the applicable current scope may be used according to the approved temporal rule.
Where already completed or issued work is affected, a controlled impact assessment and correction/reissue process shall apply where required.

**Status:** CLOSED — RECONCILED BASELINE



### Q429. Is accreditation status determined at test execution time, approval time, report time, or by a specific policy?

**Answer:** The single applicability instant is **execution start**. If scope was accredited at execution start but is suspended/withdrawn at issue time, report issuance is blocked and routed to the Quality Authority. If no approved scope record applies, the work is non-accredited and no accreditation claim is rendered.

**Status:** CLOSED — RECONCILED BASELINE



### Q430. Which historical scope value must an issued report preserve?

**Answer:** An issued report shall preserve the exact historical accreditation state that applied to the reportable work.

At minimum, the report snapshot shall preserve:
- resolved accreditation status;
- applicable accreditation framework/body representation;
- relevant MethodVersion/TestDefinition applicability;
- effective scope reference;
- approved report wording/mark representation where applicable;
- the evidence/reference used to resolve the scope.

A later accreditation-scope change shall not alter the historical accreditation representation of an already issued report.

**Status:** CLOSED — RECONCILED BASELINE



### Q431. Are accreditation symbols, marks, logos, or wording required on reports?

**Answer:** Accreditation symbols, marks, logos, and/or wording shall be treated as controlled report content.
Whether such elements appear, where they appear, and for which reportable work they may be used shall be determined by the laboratory's approved accreditation and reporting requirements.
LabNexus shall not independently infer or create an accreditation claim merely because a MethodVersion is configured as accredited.
Accreditation marks and wording shall therefore be governed through controlled report configuration and approval.

**Status:** CLOSED — RECONCILED BASELINE



### Q432. What exact wording is approved for accredited versus non-accredited work?

**Answer:** The exact wording used for accredited and non-accredited work shall be provided and approved by the laboratory through controlled report configuration.

LabNexus shall support separate controlled representations for:
- accredited work;
- non-accredited work;
- mixed reports where permitted;
- any required qualification, limitation, disclaimer, or scope wording.

The system shall not invent regulatory or accreditation wording.
Any change to approved accreditation wording shall follow controlled report/configuration change governance.

**Status:** CLOSED — RECONCILED BASELINE



### Q433. Are there tests that can never display an accreditation claim even if the method is in scope?

**Answer:** Yes. The laboratory may identify TestDefinitions that shall not display an accreditation claim even where the associated MethodVersion has an accredited default.

Such exclusions shall be explicitly configured and approved at the TestDefinition level, consistent with the frozen accreditation precedence:
**TestDefinition override > MethodVersion default**

The exclusion shall be effective-dated and historically reconstructable.
No report shall display an accreditation claim solely because the underlying MethodVersion has an accredited default when an approved TestDefinition-specific exclusion applies.

**Status:** CLOSED — RECONCILED BASELINE



### Q434. Who validates accreditation configuration before it becomes effective?

**Answer:** Accreditation is represented from approved laboratory scope data. MethodVersion provides the normal scope default and an approved TestDefinition override may apply. Precedence and effective dating are deterministic and historically captured. LabNexus does not confer accreditation.

**Status:** CLOSED — RECONCILED BASELINE



### Q435. What equipment categories are required?

**Answer:** Equipment categories should be configurable. Core categories: measuring instruments, test instruments/apparatus, sample-preparation equipment, temperature/environment-control equipment, support equipment, reference/monitoring equipment. Actual launch inventory comes from the laboratory.

**Status:** CLOSED — RECONCILED BASELINE



### Q436. What uniquely identifies an equipment item?

**Answer:** Each Equipment item has a globally unique internal Equipment ID, system-generated, immutable and never reused.

**Status:** CLOSED — RECONCILED BASELINE



### Q437. Which equipment fields are mandatory?

**Answer:** Mandatory fields: Equipment ID, equipment type/category, name/description, manufacturer, model/type where applicable, unique/serial identification, status, current location, ownership/source as relevant, and applicable validity/control information.

**Status:** CLOSED — RECONCILED BASELINE



### Q438. Are serial numbers mandatory?

**Answer:** Serial number is mandatory where the manufacturer provides one; where absent, another controlled unique identifier is required.

**Status:** CLOSED — RECONCILED BASELINE



### Q439. Are manufacturer and model mandatory?

**Answer:** Manufacturer and model/type should be mandatory for equipment where those attributes exist.

**Status:** CLOSED — RECONCILED BASELINE



### Q440. Are equipment locations tracked?

**Answer:** Yes. Current equipment location is required and location history should be retained where operationally significant.

**Status:** CLOSED — RECONCILED BASELINE



### Q441. Are equipment ownership/custody details required?

**Answer:** Ownership/custody should be captured where relevant, but it need not be mandatory for every laboratory item.

**Status:** CLOSED — RECONCILED BASELINE



### Q442. What equipment statuses exist?

**Answer:** Equipment status vocabulary and transition semantics are controlled baseline behavior. Equipment eligibility is evaluated at the **actual activity timestamp** using applicable status, calibration, maintenance, qualification/verification, authorization and method/test restrictions. The system does not invent new statuses or silently select an unapproved enforcement level.

**Status:** CLOSED — LABORATORY DECISION
**Primary Closure Artifact / Decision Record:** Equipment Eligibility / Activity Rule



### Q443. What status blocks use?

**Answer:** At minimum, Out of Service, Quarantined, Retired and any other configured non-operational status must block use.

**Status:** CLOSED — RECONCILED BASELINE



### Q444. What is the definition of calibration-valid?

**Answer:** Calibration-valid = required calibration is current, evidence exists, acceptance criteria were met, and the calibration is within its approved validity interval.

**Status:** CLOSED — RECONCILED BASELINE



### Q445. What is the definition of qualification-valid?

**Answer:** Qualification-valid = required qualification has been completed, accepted and remains within its configured validity period/conditions. Where qualification is not applicable, status is N/A rather than failed.

**Status:** CLOSED — RECONCILED BASELINE



### Q446. What is the definition of verification-valid?

**Answer:** Verification-valid = required verification has been performed, accepted and remains within its configured validity period/conditions.

**Status:** CLOSED — RECONCILED BASELINE



### Q447. What is the definition of maintenance-valid?

**Answer:** Maintenance-valid = no overdue mandatory maintenance that the laboratory has defined as affecting fitness for use; routine maintenance must have documented status.

**Status:** CLOSED — RECONCILED BASELINE



### Q448. Which validity conditions must be checked before TestInstance execution?

**Answer:** Before TestInstance execution, the system shall determine equipment eligibility using the controlled Equipment Eligibility / Activity Rule applicable to the TestDefinition, equipment, user, and relevant activity date/time.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q449. Which checks are blocking?

**Answer:** Equipment eligibility checks shall be classified explicitly as blocking or warning-only in the Equipment Eligibility / Activity Rule.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q450. Which checks are warning-only?

**Answer:** Warning-only equipment conditions shall be limited to conditions that the laboratory explicitly determines do not automatically make the equipment unsuitable for the affected activity.

Examples may include:
- a non-critical maintenance condition;
- an informational status;
- a condition requiring operator attention but not immediate blocking;
- another approved non-blocking equipment control.

Warnings shall be visible and auditable.
A warning shall not silently permit use where the approved rule defines the condition as blocking.
The laboratory shall define the blocking/warning classification through the controlled Equipment Eligibility / Activity Rule.

**Status:** CLOSED — RECONCILED BASELINE



### Q451. Can a test use equipment with an expired calibration under any approved exception?

**Answer:** Use of equipment with expired calibration shall normally be **blocked** where calibration validity is required for the affected TestInstance.
An exception may be permitted only where the laboratory has an approved controlled rule allowing such exceptional use for the applicable circumstance.
The exception shall not bypass other mandatory equipment or technical controls and shall not retroactively make the equipment normally eligible.
Any work performed under an approved exception shall remain explicitly identifiable for subsequent review and impact assessment.

**Status:** CLOSED — RECONCILED BASELINE



### Q452. If yes, how is the exception approved and recorded?

**Answer:** An expired-calibration exception shall require a controlled authorization and documented evidence.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q453. Can equipment be temporarily unavailable?

**Answer:** Equipment may be temporarily unavailable.
Temporary unavailability shall be represented as a controlled equipment state or condition and shall prevent use where the applicable eligibility rule requires blocking.

The record shall preserve, as appropriate:
- reason;
- start date/time;
- expected/actual return-to-service information;
- affected equipment;
- responsible actor;
- related maintenance/repair/qualification/verification evidence.

Returning equipment to service shall require the applicable controlled checks before it becomes eligible again.

**Status:** CLOSED — RECONCILED BASELINE



### Q454. Can equipment be reserved or booked?

**Answer:** Equipment reservation/booking may be supported where operationally useful, but reservation shall not itself establish technical eligibility.

A reservation shall identify, where applicable:
- equipment;
- intended TestInstance/work;
- reserved period;
- reserving user;
- status;
- conflicts.

Reservation logic shall prevent or flag conflicting bookings according to the approved equipment-use rule.
Technical eligibility, calibration/qualification/verification status, and authorization remain independent controls.

**Status:** CLOSED — RECONCILED BASELINE



### Q455. Can multiple TestInstances use the same equipment at the same time?

**Answer:** Multiple TestInstances may use the same equipment at the same time only where the equipment and laboratory procedure permit concurrent use.
The system shall not assume that every equipment item is single-use or mutually exclusive.

Concurrency shall be governed by configurable equipment-use rules, which may define:
- single-user/single-TestInstance operation;
- permitted concurrent users;
- permitted concurrent TestInstances;
- exclusive-use periods;
- required reservation;
- other applicable operational restrictions.

Actual EquipmentUse/activity shall remain historically traceable for each TestInstance.

**Status:** CLOSED — RECONCILED BASELINE



### Q456. Is equipment scheduling required?

**Answer:** Equipment scheduling shall be supported only to the extent required by the approved v1 operational rules.

At minimum, LabNexus shall support controlled equipment availability/use information sufficient to:
- identify unavailable equipment;
- prevent prohibited use;
- identify conflicts where applicable;
- support reservations/bookings where approved;
- maintain actual equipment-use history.

A full enterprise resource scheduling subsystem is not required for v1 unless separately approved.

**Status:** CLOSED — RECONCILED BASELINE



### Q457. How are equipment users authorized?

**Answer:** Equipment users shall be authorized through controlled user/equipment eligibility rules.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q458. Are user qualifications linked to equipment?

**Answer:** Yes. Where equipment requires specific competence or authorization, the user's qualification/competence shall be linked to the applicable equipment type and/or equipment item.
The eligibility determination shall consider whether the qualification was valid for the relevant date/time.
Historical EquipmentUse records shall preserve the user, equipment, activity, and applicable authorization/qualification context needed for later reconstruction.
Where no equipment-specific qualification is required, no artificial qualification requirement shall be imposed.

**Status:** CLOSED — RECONCILED BASELINE



### Q459. How is as-of eligibility determined for historical reconstruction?

**Answer:** Historical equipment eligibility shall be determined as-of the relevant date/time of the TestInstance activity, using the controlled equipment state, validity records, authorization/qualification records, and explicit EquipmentUse/activity evidence applicable at that time.
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

**Status:** CLOSED — RECONCILED BASELINE



### Q460. How are calibration certificates linked?

**Answer:** Calibration certificates must be linked to the specific Equipment item and calibration event.

**Status:** CLOSED — RECONCILED BASELINE



### Q461. Are calibration certificates stored in the document system?

**Answer:** Yes. Controlled calibration certificates should be stored/referenced through the Document/DocumentVersion system.

**Status:** CLOSED — RECONCILED BASELINE



### Q462. How are equipment repairs represented?

**Answer:** Repairs are immutable history events linked to the Equipment item, including description, dates, affected condition, action, service provider/actor, evidence and return-to-service decision.

**Status:** CLOSED — RECONCILED BASELINE



### Q463. How are equipment modifications represented?

**Answer:** Modifications require controlled equipment-history records and an impact/verification assessment where relevant.

**Status:** CLOSED — RECONCILED BASELINE



### Q464. How are maintenance events represented?

**Answer:** Maintenance events are recorded as dated controlled events, including planned/completed status, work performed, actor/provider and next-due information where applicable.

**Status:** CLOSED — RECONCILED BASELINE



### Q465. How are verification records represented?

**Answer:** Verification records are controlled records linked to the equipment, verification event, criteria, results, outcome, assessor and evidence.

**Status:** CLOSED — RECONCILED BASELINE



### Q466. What happens to historical TestInstances if equipment status is later corrected?

**Answer:** If equipment status is later corrected, the correction shall not rewrite historical TestInstance eligibility or equipment use.
Historical TestInstances shall retain the exact EquipmentUse/activity record identifying the equipment actually used and the applicable date/time.
Where the corrected equipment status indicates that the equipment may have been ineligible at the time of use, the system shall identify the affected TestInstances and initiate the controlled equipment/nonconformance impact process.
The impact assessment shall determine, as applicable, whether affected work requires review, retest, rework, result correction, report correction/reissue, or other controlled disposition.
The historical equipment status correction, impact assessment, disposition, and resulting actions shall remain fully traceable.

**Status:** CLOSED — RECONCILED BASELINE



### Q467. How are equipment-related nonconformities handled?

**Answer:** For equipment issues, the controlled path is: affected equipment state → identify potentially affected TestInstances → assess technical/report impact → determine retest/rework/correction or other disposition → record nonconformance/corrective action → authorized return to service. Affected reports may not remain silently inconsistent.

**Status:** CLOSED — RECONCILED BASELINE



### Q468. Which QC types are actually used by the laboratory today?

**Answer:** Generic QC mechanisms may be implemented independently, but no launch-specific Solid Fuel/Solid Biofuel QC behavior becomes effective until the corresponding Launch QC Matrix is approved. Every effective TestDefinition has an explicit QC configuration record, including a controlled statement that no QC is required where that is the approved decision.

**Status:** CLOSED — RECONCILED BASELINE



### Q469. Which tests require blanks?

**Answer:** Which tests require blanks shall be defined in the approved Launch QC / QC Configuration Matrix.

For each applicable TestDefinition, the matrix shall identify whether blanks are:
- required;
- optional;
- not applicable;
together with the required frequency, acceptance criteria, failure handling, and relationship to result approval where applicable.

No test shall be assumed to require a blank merely because a generic blank capability exists.

**Status:** CLOSED — RECONCILED BASELINE



### Q470. Which tests require duplicates?

**Answer:** Which tests require duplicates shall be defined in the approved **Launch QC / QC Configuration Matrix.**
The matrix shall identify applicable TestDefinitions, duplicate frequency/conditions, acceptance criteria, failure handling, and whether the duplicate affects result release or approval.
Duplicate requirements shall remain controlled technical configuration rather than arbitrary analyst decisions.

**Status:** CLOSED — RECONCILED BASELINE



### Q471. Which tests require replicates?

**Answer:** Which tests require replicates shall be defined in the approved Launch QC / QC Configuration Matrix and applicable laboratory methods/SOPs.

The matrix shall define:
- applicable tests;
- replicate requirements;
- number/frequency where applicable;
- how replicate observations are identified;
- how they contribute to calculations/results;
- acceptance criteria;
- failure/disposition rules.

Replicate execution shall remain distinguishable from ordinary retest or correction activity.

**Status:** CLOSED — RECONCILED BASELINE



### Q472. Which tests require spikes?

**Answer:** Which tests require spikes shall be defined in the approved **Launch QC / QC Configuration Matrix** and supported by the applicable laboratory method/SOP.
For each applicable test, the matrix shall define the spike requirement, frequency, applicable acceptance criteria, calculation/interpretation rules, and failure handling.
No spike requirement shall be inferred solely from generic QC capability.

**Status:** CLOSED — RECONCILED BASELINE



### Q473. Which tests use reference materials or CRMs?

**Answer:** Use of reference materials or CRMs shall be defined by the approved **Launch QC / QC Configuration Matrix** and applicable laboratory methods/SOPs.

The matrix shall identify:
- applicable TestDefinitions;
- material/reference identity;
- frequency or use condition;
- acceptance criteria;
- result interpretation;
- failure handling;
- required evidence and traceability.

CRM/reference-material use shall remain linked to the relevant QC event and affected work where applicable.

**Status:** CLOSED — RECONCILED BASELINE



### Q474. Which tests require calibration checks?

**Answer:** Calibration-check requirements shall be defined in the approved **Launch QC / QC Configuration Matrix** and applicable equipment/method controls.

The matrix shall identify:
- applicable tests/equipment;
- when calibration checks are required;
- acceptance criteria;
- actions when the check fails;
- whether affected TestInstances are blocked;
- required investigation or disposition.

Generic calibration-check capability may be implemented, but launch-specific rules require approved laboratory configuration.

**Status:** CLOSED — RECONCILED BASELINE



### Q475. What acceptance criteria apply to each QC type?

**Answer:** Acceptance criteria for each QC type shall be defined in the approved **Launch QC / QC Configuration Matrix**, based on the applicable laboratory method, SOP, equipment requirement, technical procedure, or other authoritative laboratory source.

Each QC rule shall identify, where applicable:
- the criterion;
- units/data type;
- calculation or comparison method;
- tolerance/limit;
- pass/fail interpretation;
- blocking or warning consequence;
- required disposition when failed.

LabNexus shall not invent technical QC acceptance limits.

**Status:** CLOSED — RECONCILED BASELINE



### Q476. Are QC criteria numeric, categorical, or formula-based?

**Answer:** QC criteria may be numeric, categorical, formula-based, or a controlled combination of these, according to the applicable laboratory rule.

The QC configuration model shall therefore support:
- numeric limits and ranges;
- categorical outcomes;
- Boolean pass/fail rules;
- formula-based evaluation;
- controlled lookup/reference criteria.

The applicable QC Matrix shall identify the evaluation type for each QC rule.

**Status:** CLOSED — RECONCILED BASELINE



### Q477. Which QC failures block result approval?

**Answer:** Which QC failures block result approval shall be defined explicitly in the approved **Launch QC / QC Configuration Matrix.**
A QC failure shall block approval where the approved laboratory rule determines that the affected result cannot proceed without investigation, correction, retest, rework, or authorized disposition.
The system shall enforce configured blocking rules at the backend/domain level.
No QC failure shall be treated as automatically blocking unless the approved QC rule says so.

**Status:** CLOSED — RECONCILED BASELINE



### Q478. Which QC failures allow documented acceptance with justification?

**Answer:** A QC failure may permit documented acceptance with justification only where the approved laboratory QC rule explicitly allows such disposition.

The disposition shall require, as applicable:
- identified QC failure;
- affected TestInstance/result;
- reason and justification;
- authorized decision-maker;
- impact assessment where required;
- required review/verification/approval;
- complete audit evidence.

An analyst shall not bypass a configured blocking QC rule through an ordinary acceptance action.

**Status:** CLOSED — RECONCILED BASELINE



### Q479. Who decides whether a QC failure blocks work?

**Answer:** The authority to determine whether a QC failure blocks work shall be the **Laboratory Technical Authority**, with Quality involvement where the laboratory's QMS or controlled QC governance requires it.
The resulting rule shall be captured in the approved **Launch QC / QC Configuration Matrix** and controlled through configuration governance.
System administrators shall implement approved QC rules but shall not independently decide the technical blocking criteria.

**Status:** CLOSED — RECONCILED BASELINE



### Q480. Must QC failures automatically open an investigation?

**Answer:** A blocking QC failure creates or links to a controlled Nonconformance investigation. The NC is the investigation/disposition record and is closed by the Technical or Quality Authority as applicable. CAPA may be linked where required. V1 does not implement general control charts, Westgard rules or other advanced statistical QC unless separately approved.

### Q481. What is an investigation record?

**Answer:** Keep minimum controlled investigation/CAPA linkage; do not create a general enterprise CAPA subsystem without approved need.
**Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Quality Management / NC-CAPA Boundary



### Q482. Who can investigate a QC failure?

**Answer:** Keep minimum controlled investigation/CAPA linkage; do not create a general enterprise CAPA subsystem without approved need.
**Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Quality Management / NC-CAPA Boundary



### Q483. Who can close a QC investigation?

**Answer:** Keep minimum controlled investigation/CAPA linkage; do not create a general enterprise CAPA subsystem without approved need.
**Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Quality Management / NC-CAPA Boundary



### Q484. What corrective-action linkage is required?

**Answer:** Keep minimum controlled investigation/CAPA linkage; do not create a general enterprise CAPA subsystem without approved need.
**Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Quality Management / NC-CAPA Boundary



### Q485. What preventive-action linkage is required, if any?

**Answer:** Keep minimum controlled investigation/CAPA linkage; do not create a general enterprise CAPA subsystem without approved need.
**Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Quality Management / NC-CAPA Boundary



### Q486. Are CAPA records required in v1?

**Answer:** Keep minimum controlled investigation/CAPA linkage; do not create a general enterprise CAPA subsystem without approved need.
**Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Quality Management / NC-CAPA Boundary



### Q487. Are control charts required?

**Answer:** Keep minimum controlled investigation/CAPA linkage; do not create a general enterprise CAPA subsystem without approved need.
**Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Quality Management / NC-CAPA Boundary



### Q488. Are trend charts required?

**Answer:** Keep minimum controlled investigation/CAPA linkage; do not create a general enterprise CAPA subsystem without approved need.
**Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Quality Management / NC-CAPA Boundary



### Q489. Are Westgard or similar rules required?

**Answer:** Keep minimum controlled investigation/CAPA linkage; do not create a general enterprise CAPA subsystem without approved need.
**Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Quality Management / NC-CAPA Boundary



### Q490. Are statistical QC calculations required?

**Answer:** QC criteria, frequency, blocking/warning behavior and disposition are controlled laboratory data. If required criteria have not been supplied/approved, the affected QC behavior remains inactive and the associated controlled workflow remains non-deployable rather than using a developer assumption.

### Q491. Which QC capabilities are explicitly out of scope?

**Answer:** A QC failure classified as blocking prevents approval until the controlled investigation/disposition is resolved. The failure, affected technical record, decision, evidence and any linked CAPA remain traceable.

### Q492. Must QC records be linked to the exact TestInstance?

**Answer:** Yes. QC records shall be linked to the exact **TestInstance** whenever the QC activity is performed for, associated with, or used to determine the validity of a specific execution.
Where QC is broader than one TestInstance, such as an equipment-level, batch-level, run-level, or environmental QC event, the QC record shall retain the appropriate higher-level context and explicit links to affected TestInstances where applicable.

QC records shall never be stored as untraceable standalone pass/fail values.

**Status:** CLOSED — RECONCILED BASELINE



### Q493. Must QC records be linked to equipment or MethodVersion?

**Answer:** Yes. Where relevant, QC records shall be linked to the exact **Equipment** and/or **MethodVersion** involved.

The applicable linkage shall depend on the QC type and shall preserve sufficient context to reconstruct:
- which QC was performed;
- for which TestDefinition/TestInstance or work group;
- using which Equipment;
- under which MethodVersion;
- at what date/time;
- by whom;
- under which applicable QC configuration.

The Launch QC / QC Configuration Matrix shall define which relationships are mandatory for each QC type.

**Status:** CLOSED — RECONCILED BASELINE



### Q494. Must failed QC history be preserved even when the result is later accepted?

**Answer:** Yes. Failed QC history shall always be preserved, even when the affected result is later accepted through an authorized disposition.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q495. What report types are required in v1?

**Answer:** The v1 report types shall be frozen through the approved **Report Lifecycle, Composition and Issuance Model** and the laboratory's controlled report requirements.
At minimum, v1 shall support the laboratory's approved primary issued laboratory report format for completed work.
Additional report types, such as separate certificates or specialized reports, shall be included only where an actual v1 laboratory, customer, contractual, or technical requirement exists.
The report model shall not structurally assume that every Sample has exactly one report.

**Status:** CLOSED — RECONCILED BASELINE



### Q496. Are reports called reports, test reports, certificates, or multiple document types?

**Answer:** The laboratory shall approve the controlled terminology used for its issued reporting documents.

For v1, LabNexus shall support the approved report/document type(s), whether the laboratory uses terms such as:
- Laboratory Report;
- Test Report;
- Certificate;
- another controlled document type.

Where multiple document types are required, each shall have its own controlled identity, lifecycle, composition, and issuance rules.
The system shall not treat differing terminology as different technical concepts unless the laboratory's reporting requirements require distinct document types.

**Status:** CLOSED — RECONCILED BASELINE



### Q497. Which report layouts are required?

**Answer:** Required report layouts shall be defined through controlled report templates and the approved **Report Lifecycle, Composition and Issuance Model.**
The v1 report layout shall support the laboratory-approved primary report format and shall preserve the required technical, customer, traceability, approval, and accreditation information.
Where multiple layouts are genuinely required, each shall be separately controlled and versioned.
Report layout changes shall follow controlled report/template governance and shall not silently alter previously issued PDFs.

**Status:** CLOSED — RECONCILED BASELINE



### Q498. What is the laboratory's official report format?

**Answer:** The laboratory's official report format shall be the approved controlled report template/document version adopted for LabNexus.
The exact visual layout, wording, field placement, logos/marks, signatures/representations, disclaimers, and other presentation rules shall be derived from the laboratory's approved controlled reporting format rather than invented by the software project.
The exact approved template/document version shall be linked to each ReportRevision so that historical reports remain reconstructable.

**Status:** CLOSED — RECONCILED BASELINE



### Q499. Which fields appear in the report header?

**Answer:** The report header shall contain the laboratory-approved identity and report-control information required for the issued report.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q500. Which customer information appears on reports?

**Answer:** Customer information shown on reports shall be limited to the laboratory-approved reporting fields required for identification, communication, contractual requirements, and traceability.

The controlled report model should support, where applicable:
- customer legal/business name;
- customer code/reference;
- customer address or contact information where required;
- customer-specific reference/order identifier.

The exact customer information displayed shall be determined by the approved report template and customer/reporting requirements.
Historical reports shall preserve the customer representation used at issuance.

**Status:** CLOSED — RECONCILED BASELINE



### Q501. Which project/contract information appears on reports?

**Answer:** Project/Contract information shall appear on reports where required for traceability, contractual identification, or customer reporting.

The report model should support, where applicable:
- Project identifier/name;
- Contract/reference number;
- Request identifier;
- customer order/reference;
- other approved engagement identifiers.

Only fields approved for reporting shall be rendered.
The exact values used in an issued report shall be frozen within the ReportRevision/report snapshot rather than taken from later mutable master data.

**Status:** CLOSED — RECONCILED BASELINE



### Q502. Which sample identification fields appear on reports?

**Answer:** Reports shall display the laboratory-approved Sample identification fields necessary for unambiguous sample traceability.
At minimum, the report model shall support the authoritative internal Sample ID and the approved customer/external Sample ID where applicable.
Additional sample information such as sample description, matrix, receipt/collection information, or other identifiers shall be included where required by the approved report template or applicable technical/customer requirements.
Historical report snapshots shall preserve the exact sample identity representation used at issuance.

**Status:** CLOSED — RECONCILED BASELINE



### Q503. Which test/method fields appear on reports?

**Answer:** Reports shall display the TestDefinition and method information required by the laboratory's approved reporting requirements.

The report model shall support, where applicable:
- Test name;
- Test Code;
- Method/MethodVersion reference;
- applicable method edition/revision;
- required technical test description;
- other approved technical identifiers.

The exact method representation shall be frozen in the ReportResultSnapshot/ReportRevision rather than regenerated from mutable current configuration.

**Status:** CLOSED — RECONCILED BASELINE



### Q504. Which result fields appear on reports?

**Answer:** Reports shall display the approved reportable result fields for each applicable TestDefinition.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q505. Which units appear on reports?

**Answer:** Units displayed on reports shall come from controlled unit definitions and the approved TestDefinition/Parameter configuration.
The report shall use the unit applicable to the reportable result and shall not derive a different unit from mutable current configuration after issuance.
Where unit conversion is performed, the result and conversion/provenance shall remain traceable to the underlying controlled calculation/result.

**Status:** CLOSED — RECONCILED BASELINE



### Q506. Which qualifiers appear on reports?

**Answer:** Result qualifiers shall be displayed where required by the approved parameter/result configuration and applicable reporting rules.

The model shall support structured qualifiers such as, where applicable:
- less-than;
- greater-than;
- non-detect;
- estimated/qualified result;
- other approved result qualifiers.

Qualifiers shall remain distinct from the underlying numeric/text result value and shall be rendered according to the controlled report template.

**Status:** CLOSED — RECONCILED BASELINE



### Q507. Which uncertainty information is required, if any?

**Answer:** Uncertainty information shall be displayed only where required by the applicable laboratory method, technical procedure, customer requirement, accreditation/reporting rule, or approved report template.
The system shall support controlled uncertainty representation where applicable, including the appropriate value/unit or associated statement.
LabNexus shall not invent uncertainty values or assume that every reported result requires uncertainty.
The reporting requirement shall be defined per applicable TestDefinition/Parameter where necessary.

**Status:** CLOSED — RECONCILED BASELINE



### Q508. Which detection-limit information is required, if any?

**Answer:** Detection-limit information shall be included where required by the applicable method, parameter definition, laboratory reporting rule, customer requirement, or approved report template.
Where applicable, the report shall distinguish the relevant detection/decision limit information from the actual result and qualifier.
The underlying structured detection-limit information shall not be represented only as free text.
Exact terminology and reporting representation shall be controlled by the applicable technical/reporting configuration.

**Status:** CLOSED — RECONCILED BASELINE



### Q509. Which method references appear on reports?

**Answer:** Method references appearing on reports shall come from the controlled Method/MethodVersion configuration applicable to the TestInstance.
The report shall preserve the exact method reference/edition used for the reported work, including any approved laboratory implementation representation required by the report.
A later method revision shall not change the method reference shown on a previously issued report.

**Status:** CLOSED — RECONCILED BASELINE



### Q510. Which accreditation representation appears on reports?

**Answer:** Accreditation representation on reports shall be determined from the resolved, effective accreditation scope applicable to the reportable work and the approved report template/configuration.

The report shall preserve the exact historical accreditation representation used at issuance, including where applicable:
- accredited/non-accredited status;
- applicable scope representation;
- approved wording;
- approved accreditation mark/logo;
- required limitations or qualifications.

LabNexus shall not independently create an accreditation claim.

**Status:** CLOSED — RECONCILED BASELINE



### Q511. Which analyst information appears on reports?

**Answer:** Analyst information displayed on reports shall follow the laboratory's approved reporting requirements.
Where analyst identity is required, the report should preserve the approved representation of the responsible analyst or analysts, based on the TestInstance record and controlled report snapshot.
The exact historical identity displayed shall remain reconstructable even if the user's name, role, or account information changes later.

**Status:** CLOSED — RECONCILED BASELINE



### Q512. Which reviewer/verifier/approver information appears on reports?

**Answer:** Reviewer, Verifier, and Approver information displayed on reports shall be governed by the approved report template and laboratory reporting policy.

Where required, the report shall preserve the approved representation of:
- reviewer;
- verifier;
- approver/authorized signatory;
- relevant approval date/time.

The report shall derive these values from the controlled approval history and ReportRevision snapshot rather than mutable current user-role data.

**Status:** CLOSED — RECONCILED BASELINE



### Q513. Are signatures printed, rendered, represented by names, or handled another way?

**Answer:** Signature representation on reports shall follow the laboratory's approved controlled reporting policy.

The system shall support the approved representation, which may include:
- printed name;
- role/title;
- controlled electronic signature representation;
- signature image where specifically approved;
- another controlled representation.

The report's displayed signature representation shall correspond to the underlying attributable approval event and shall not create an independent or misleading signature record.

**Status:** CLOSED — RECONCILED BASELINE



### Q514. Are electronic signatures required on the PDF itself?

**Answer:** Electronic signatures shall be supported according to the laboratory's approved electronic-signature policy.
Whether the PDF itself contains a cryptographic/electronic signature or instead contains a controlled visual representation of an application-recorded electronic approval shall be explicitly decided before report implementation.
The underlying authoritative approval event remains the application approval record, and the exact PDF/report representation shall be frozen with the issued ReportRevision.

**Status:** CLOSED — RECONCILED BASELINE



### Q515. Are report page numbers required?

**Answer:** Issued reports shall use controlled page numbering where required by the laboratory's approved report format.
The report rendering system should support page numbering and total-page representation so that the issued PDF provides a stable document boundary.
Exact page-number format shall be controlled by the approved report template.

**Status:** CLOSED — RECONCILED BASELINE



### Q516. Are document numbers required?

**Answer:** A controlled report/document number shall be assigned to each issued report where required by the laboratory's numbering policy.

The report number shall be:
- system-controlled;
- unique within the deployment;
- immutable after issuance;
- historically reconstructable;
- distinct from the ReportRevision number where both are required.

The exact numbering format shall be defined in the approved Numbering and Identifier Allocation Matrix.

**Status:** CLOSED — RECONCILED BASELINE



### Q517. Are report revision numbers displayed?

**Answer:** Report revision numbers shall be controlled and shall be displayed where required by the approved report format.
Where revision numbering is displayed, each ReportRevision shall have a unique sequential revision designation and shall preserve its relationship to the underlying Report.
A later revision shall not overwrite the historical revision number or issued report artifact.

**Status:** CLOSED — RECONCILED BASELINE



### Q518. Is issue date required?

**Answer:** An issue date shall be required for an issued report.
The issue date shall represent the controlled date on which the particular ReportRevision was formally issued.
The issued date shall be preserved in the ReportRevision/snapshot and shall not change if the report is later superseded or corrected.

**Status:** CLOSED — RECONCILED BASELINE



### Q519. Is issue time required?

**Answer:** An issue time shall be recorded for an issued report to provide precise issuance traceability.
The issue timestamp shall be system-recorded using the approved laboratory time-zone convention and shall be preserved with the ReportRevision and issuance audit event.
The timestamp shall not be replaced by a later regeneration time.

**Status:** CLOSED — RECONCILED BASELINE



### Q520. Is reissue/correction status displayed?

**Answer:** Yes. Where a report is a correction, reissue, replacement, withdrawal-related revision, or other non-original report state, that status shall be clearly represented according to the approved report lifecycle.
The report shall identify its current revision/status and preserve the relationship to prior ReportRevisions.
The exact customer-facing wording shall be controlled by the approved report template.

**Status:** CLOSED — RECONCILED BASELINE



### Q521. How is a revised report identified to customers?

**Answer:** A revised report shall be identifiable through a combination of controlled report number, ReportRevision, issue date, and approved revision/reissue wording.
Where required by laboratory policy, the revised report shall explicitly state that it supersedes or revises a previous report.
The identification shall allow the customer and internal staff to distinguish the revised report from the earlier issued artifact without ambiguity.

**Status:** CLOSED — RECONCILED BASELINE



### Q522. Must the previous report number be referenced in a revised report?

**Answer:** Where a revised report replaces or corrects an earlier issued report, the revised ReportRevision shall retain an explicit relationship to the previous ReportRevision.
Where required by the laboratory's approved reporting policy, the previous report number/revision shall be displayed on the revised report.
The historical relationship shall always be retained internally even if the previous report number is not displayed to the customer.

**Status:** CLOSED — RECONCILED BASELINE



### Q523. What statement explains corrections or reissues?

**Answer:** The correction/reissue statement shall be controlled through the approved report template and report lifecycle policy.

It shall clearly identify, where applicable:
- that the report is revised/corrected;
- the affected report/revision;
- the reason or category of correction where required;
- the issue/revision date;
- any required statement regarding supersession of the previous report.

LabNexus shall not invent regulatory correction wording; the exact approved wording shall be supplied through controlled configuration.

**Status:** CLOSED — RECONCILED BASELINE



### Q524. What statement explains accreditation status?

**Answer:** The accreditation statement on a report shall be derived from the resolved accreditation configuration and approved report wording.
It shall accurately distinguish accredited and non-accredited work and shall use only laboratory-approved wording/marks.
The wording shall remain historically frozen in each issued ReportRevision.

**Status:** CLOSED — RECONCILED BASELINE



### Q525. Are disclaimers or laboratory notes required?

**Answer:** Disclaimers and laboratory notes shall be supported where they are required by the approved report template, laboratory policy, customer requirements, method requirements, or accreditation/reporting rules.

Controlled notes shall be distinguishable from:
- technical result values;
- regulatory/accreditation claims;
- correction statements;
- ordinary report narrative.

Required controlled disclaimers shall be versioned with the report template and historically preserved in issued reports.

**Status:** CLOSED — RECONCILED BASELINE



### Q526. Are customer-specific report formats required?

**Answer:** Customer-specific report formats may be supported where there is an approved v1 customer or contractual requirement.
Such formats shall be implemented as controlled report templates/configurations and shall not require bespoke code for each customer where the requirement can be represented through the approved report-template model.
Customer-specific formatting shall not be permitted to alter controlled technical meaning, approval, accreditation, or traceability rules.
Each approved customer-specific format shall have explicit ownership, versioning, approval, and historical applicability.

**Status:** CLOSED — RECONCILED BASELINE



### Q527. Are discipline-specific report templates required?

**Answer:** Discipline-specific report templates shall be supported where genuinely required by approved laboratory or reporting requirements.
The v1 architecture shall permit different controlled templates for Solid Fuel, Solid Biofuel, and other approved disciplines without changing the underlying report lifecycle or result-snapshot model.
Discipline-specific templates shall be versioned, approved, effective-dated, and historically reconstructable.
No discipline-specific template shall introduce uncontrolled technical or accreditation behavior outside the approved configuration model.

**Status:** CLOSED — RECONCILED BASELINE



### Q528. Are attachments part of issued reports?

**Answer:** Attachments shall be part of issued reports only where explicitly included by the approved report composition/configuration.
The ReportRevision shall identify which attachments, if any, form part of the issued report package and shall preserve their exact DocumentVersion/file identity and integrity information.
An attachment shall not be considered part of an issued report merely because it happens to exist in the LIMS.
Where attachments form part of the issued report package, their inclusion, ordering, identity, and integrity shall be frozen and reconstructable with the ReportRevision.
Unattached or independently retained source documents shall remain separate controlled records unless explicitly incorporated into the issued report package.

**Status:** CLOSED — RECONCILED BASELINE



### Q529. Are raw data or worksheets ever included with reports?

**Answer:** Raw data and worksheets may be included with a report where required by the approved laboratory, customer, contractual, technical, or regulatory reporting requirement.
Where included, each raw-data/worksheet attachment shall be treated as a controlled report component with explicit identity, DocumentVersion, integrity information, and relationship to the relevant ReportRevision.
Raw data or worksheets shall not be included merely because they exist in the LIMS.
Where they are part of an issued report package, their exact inclusion and version shall be frozen and historically reconstructable.

**Status:** CLOSED — RECONCILED BASELINE



### Q530. Is a certificate separate from the main report for any test type?

**Answer:** A certificate may be represented as a separate controlled report/document type where an approved laboratory, customer, contractual, or technical requirement requires it.
Where a certificate is functionally part of the laboratory's normal test-report output, it may instead be represented through the primary Report/ReportRevision model.
The exact v1 document types shall be approved through the Report Lifecycle, Composition and Issuance Model.
Separate certificate types shall have controlled identity, lifecycle, template/version, approval, issuance, and historical reconstruction rules.

**Status:** CLOSED — RECONCILED BASELINE



### Q531. Which report elements are frozen in ReportResultSnapshot?

**Answer:** The ReportResultSnapshot shall freeze every report-visible result attribute needed to reconstruct exactly what was reported.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q532. Which elements are generated dynamically at report rendering time?

**Answer:** Only genuinely presentation-time information may be generated dynamically during report rendering.

Dynamic rendering may include deterministic presentation elements such as:
- page numbers;
- page count;
- document rendering layout;
- approved static headers/footers;
- other non-technical presentation elements explicitly allowed by the report model.

Technical, approval, accreditation, identity, and report-visible result information shall be frozen before issuance and shall not be resolved from mutable current data at rendering time.
The rendered PDF itself shall then be persisted, hashed, verified, and linked to the ReportRevision.

**Status:** CLOSED — RECONCILED BASELINE



### Q533. Must reports be reproducible byte-for-byte, or only semantically equivalent?

**Answer:** A ReportRevision cannot reach `ISSUED` unless its exact PDF bytes have been persisted, linked, SHA-256 hashed and verified. If issuance fails, the report remains non-issued and safe retry must be possible without corrupting the audit/history.

**Status:** CLOSED — RECONCILED BASELINE



### Q534. Must the exact PDF file hash be stored?

**Answer:** Yes. The exact issued PDF bytes shall have a **SHA-256 hash** recorded in the report artifact metadata.
The hash shall be calculated from the final persisted PDF bytes.

The system shall use the hash for:
* Integrity verification;
* Backup/restore verification;
* Artifact identification;
* Detection of unintended modification;
* Historical evidence.

A changed hash means changed PDF bytes. The prior artifact must never be silently overwritten.

**Status:** CLOSED — RECONCILED BASELINE



### Q535. What PDF metadata must be stored?

**Answer:** Issued PDF metadata shall include controlled non-sensitive information appropriate to the artifact, including where technically supported:
* Laboratory identity;
* Report number;
* Report revision;
* Report title/type;
* Issue date/time;
* Author/issuer representation where approved;
* PDF creation metadata where useful.

The authoritative report identity remains the LabNexus ReportRevision and persisted artifact record, not PDF metadata alone.
Metadata shall not contain unnecessary confidential information, passwords, internal secrets, or uncontrolled implementation details.

**Status:** CLOSED — RECONCILED BASELINE



### Q536. What file naming convention is required for issued PDFs?

**Answer:** Issued PDF filenames shall be generated by the system and shall not be the authoritative identifier.

Recommended format:
`<ReportNumber>-R<Revision>.pdf`

For example:
`RPT-00012345-R1.pdf`

Where necessary, an internal immutable artifact identifier may be used in the physical storage path to avoid collisions and filesystem-name dependencies.
The filename shall be deterministic enough for human handling while remaining subordinate to the ReportRevision/artifact identity.
Issued files shall never be renamed by ordinary users through direct filesystem access.

**Status:** CLOSED — RECONCILED BASELINE



### Q537. How are report files delivered?

**Answer:** LabNexus shall support controlled report delivery through:
* Browser-controlled download;
* Controlled printing;
* Manual transfer/export where authorized.

Electronic delivery through email shall **not be a mandatory v1 dependency** because the system is offline-first.
Where email is later approved, delivery shall be treated as a separate controlled event and shall not redefine the authoritative issued report.
Delivery records should identify ReportRevision, recipient/destination where applicable, actor/system, timestamp, delivery method, and outcome.

**Status:** CLOSED — RECONCILED BASELINE



### Q538. Is email delivery required in v1?

**Answer:** No. **Email delivery is not required for v1.**

The core report lifecycle shall work completely offline:
**Approved → PDF generated → persisted → hashed → verified → issued → authorized download/print/manual delivery**

No report shall depend on SMTP, Internet connectivity, cloud email, or an external messaging service.
Email delivery may be added later as a controlled integration without changing the authoritative report/issuance model.

**Status:** CLOSED — RECONCILED BASELINE



### Q539. Is printer output required?

**Answer:** Yes, controlled printer output shall be supported where the laboratory needs physical reports.
Printing shall be a delivery/presentation function and shall not be required for report issuance.
The authoritative issued record remains the persisted ReportRevision/PDF artifact. A failed printer operation must not change report issuance status or require re-approval.
Where technically observable, application-controlled printing may be recorded as a delivery event.

**Status:** CLOSED — RECONCILED BASELINE



### Q540. Is manual download/USB delivery required?

**Answer:** Yes. Authorized users shall be able to **manually download/copy an issued report for controlled delivery**, including transfer through approved removable media where the laboratory's operational procedure permits it.
Manual delivery shall remain subject to authorization and confidentiality controls.
The application shall record the controlled download/export event where the delivery occurs through LabNexus.
The LIMS cannot guarantee physical handling after a file leaves the application's controlled environment, so the laboratory's external delivery/custody procedure remains part of the control boundary.

**Status:** CLOSED — RECONCILED BASELINE



### Q541. Who can issue a report?

**Answer:** Only an authorized **Authorized Signatory/report issuer** shall be permitted to issue a report.
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

**Status:** CLOSED — RECONCILED BASELINE



### Q542. Who can reissue a report?

**Answer:** Report reissue shall require a dedicated **Report Reissue** permission and shall be available only to authorized report issuers/signatories or explicitly designated Quality/Technical authority according to the report governance policy.
A reissue shall never modify the original issued ReportRevision.
Where technical/report content changes, the reissue shall create a new ReportRevision with explicit linkage to the previous revision and the reason for reissue.

**Status:** CLOSED — RECONCILED BASELINE



### Q543. Who can void a report?

**Answer:** There shall be **no generic destructive `Void` operation for issued reports**.

Where an issued report must be invalidated, the approved v1 mechanism shall be **controlled withdrawal** with:
* Authorized actor;
* Reason;
* Timestamp;
* Impact assessment;
* Customer/recipient notification where required;
* Link to any replacement ReportRevision;
* Preservation of the original issued PDF and history.

Thus, no ordinary user is given a `Void Report` operation that removes the report from history.

**Status:** CLOSED — RECONCILED BASELINE



### Q544. Can an issued report ever be deleted?

**Answer:** No. **An issued report shall never be deleted through normal application operation.**
Its ReportRevision, ReportResultSnapshots, approval relationships, exact issued PDF, hash, delivery history, and audit history shall remain preserved for the applicable retention period.
Destruction after retention expiry is a separate controlled records-destruction process and must not be confused with report deletion.

**Status:** CLOSED — RECONCILED BASELINE



### Q545. What happens when a report was generated but not issued?

**Answer:** A generated but not-yet-issued report shall remain in a **non-issued ReportRevision/artifact state**.

The system shall clearly distinguish:
* Generated;
* Persisted;
* Verified;
* Issued.

A generated PDF that has not completed issuance controls is not an issued laboratory report.
It may be retained as a draft/non-issued artifact for troubleshooting or workflow continuation, subject to controlled access. It must not be presented as an authoritative issued report.

**Status:** CLOSED — RECONCILED BASELINE



### Q546. What happens when report generation fails?

**Answer:** If PDF generation fails:
* The ReportRevision shall not enter `ISSUED`;
* The failure shall be recorded;
* No partial PDF shall become authoritative;
* Technical diagnostic information shall be retained in controlled evidence without exposing internals to ordinary users;
* The report shall enter an appropriate failure/recovery state;
* Authorized personnel may retry generation after the cause is addressed.

A failed rendering attempt shall not modify the underlying approved result or ApprovalSnapshot.

**Status:** CLOSED — RECONCILED BASELINE



### Q547. What happens when PDF storage fails after approval?

**Answer:** If PDF storage fails after approval, the report shall **remain non-issued**.
Approval of the technical result is not sufficient to declare the report issued.
The system shall retain the approved Result/ApprovalSnapshot and ReportRevision while the artifact remains in a recovery-required/non-issued state.
After storage is successfully completed, the exact bytes shall be hashed and verified before issuance.
No partially written or unverified PDF may receive `ISSUED` status.

**Status:** CLOSED — RECONCILED BASELINE



### Q548. Must report issuance be atomic with snapshot creation and artifact recording?

**Answer:** Yes, report issuance shall have **logical atomicity**, but it cannot depend on a literal single ACID transaction spanning SQLite and the filesystem.

The controlled issuance protocol shall be:
**Prepare ReportRevision → create/freeze snapshots → render → persist exact PDF → calculate hash → verify artifact → commit authoritative issuance state → record issuance event**

If any required step fails, the ReportRevision shall remain non-issued/recovery-required.
A database transaction shall atomically commit the database-side state and issuance event. The application shall use explicit recovery/verification logic to bridge the database/filesystem boundary.
This prevents the system from claiming `ISSUED` when the exact PDF does not exist, cannot be verified, or is not linked correctly.

**Status:** CLOSED — RECONCILED BASELINE



### Q549. What event creates a new ReportRevision?

**Answer:** A new ReportRevision shall be created whenever a new reportable state must be preserved as a distinct report revision, including:
- initial report preparation where a report revision is established;
- a corrected/revised report;
- a reissued report containing changed report-visible content;
- another controlled report change requiring historical preservation.

A new ReportRevision shall not be created merely because the PDF is regenerated without any change to the approved report state.
The exact ReportRevision creation triggers shall be defined in the Report Lifecycle, Composition and Issuance Model.

**Status:** CLOSED — RECONCILED BASELINE



### Q550. Is every issuance a new ReportRevision?

**Answer:** Not every issuance event necessarily creates a new ReportRevision.
A ReportRevision represents a distinct controlled report state. Issuance is an event/lifecycle transition applied to that revision.
If the same already-prepared ReportRevision is issued after successful verification of the exact persisted artifact, no additional revision is required merely because the issuance action occurred.
A new ReportRevision is required when the report-visible content/state changes and must be preserved as a separate revision.

**Status:** CLOSED — RECONCILED BASELINE



### Q551. Is a corrected report always a new ReportRevision?

**Answer:** Yes. A corrected report shall always be represented as a new ReportRevision.
The previous issued ReportRevision and PDF shall remain historically intact.
The new revision shall identify its relationship to the prior revision and shall preserve the reason, correction/reissue history, new report snapshot, approval state, and exact issued PDF.
A correction shall never overwrite an existing issued ReportRevision.

**Status:** CLOSED — RECONCILED BASELINE



### Q552. Can a ReportRevision be drafted without being issued?

**Answer:** Yes. A ReportRevision may exist in a controlled draft/pre-issuance state.
A draft ReportRevision shall not be treated as issued and shall not become the authoritative issued report until the required workflow, approval, PDF generation, persistence, integrity verification, and issuance controls are completed.
Draft revisions shall remain distinguishable from issued revisions and shall not be visible as authoritative issued reports.

**Status:** CLOSED — RECONCILED BASELINE



### Q553. What status values exist for ReportRevision?

**Answer:** ReportRevision shall use a controlled lifecycle. At minimum, the model should support:

**DRAFT → READY_FOR_ISSUANCE → ARTIFACT_PERSISTED → ARTIFACT_VERIFIED → ISSUED**

with controlled exceptional states such as:
- GENERATING;
- ISSUANCE_FAILED;
- RECOVERY_REQUIRED;
- WITHDRAWN;
- SUPERSEDED where required by the approved report model.

A ReportRevision shall not be ISSUED unless the exact PDF artifact has been persisted, hashed, verified, and linked.

**Status:** CLOSED — RECONCILED BASELINE



### Q554. Can an issued ReportRevision ever return to draft?

**Answer:** No. An issued ReportRevision shall never return to Draft.
If changes are required after issuance, the system shall create a new ReportRevision through the approved correction/reissue/replacement process.
The previously issued revision and artifact shall remain historically preserved.

**Status:** CLOSED — RECONCILED BASELINE



### Q555. Who may create a ReportRevision?

**Answer:** A ReportRevision may be created only by an authorized user or controlled system workflow with the appropriate report permissions.
Creation of a draft ReportRevision does not itself constitute approval or issuance.
The actor, timestamp, source report/revision where applicable, and applicable authorization context shall be recorded.

**Status:** CLOSED — RECONCILED BASELINE



### Q556. Who may issue it?

**Answer:** Only an authorized report issuer/Authorized Signatory may issue a report.
Issuance shall require all applicable technical Review, Verification, Approval, report checks, and artifact-integrity controls to have been satisfied.
The issuing action shall generate an immutable issuance event linked to the exact ReportRevision and persisted PDF artifact.

**Status:** CLOSED — RECONCILED BASELINE



### Q557. Can a ReportRevision contain a mixture of current and historical ResultRevisions?

**Answer:** A ReportRevision shall not contain an uncontrolled mixture of mutable current results and historical ResultRevisions.
Each ReportResultSnapshot shall refer to the exact ResultRevision used for that report state.
A report may legitimately contain different ResultRevisions for different results where those exact revisions were approved for inclusion in that ReportRevision, but every included result shall have an explicit historical reference.

**Status:** CLOSED — RECONCILED BASELINE



### Q558. Must every ReportResultSnapshot refer to an exact ResultRevision?

**Answer:** Yes. Every ReportResultSnapshot shall refer to the exact ResultRevision represented in that ReportRevision.
The relationship shall be explicit and immutable after the report revision is finalized.
A ReportResultSnapshot shall not rely on the current live Result alone because later corrections must not alter the meaning of an earlier issued report.

**Status:** CLOSED — RECONCILED BASELINE



### Q559. What other report-level snapshots are required?

**Answer:** In addition to Result snapshots, the ReportRevision shall freeze all report-level information necessary for historical reconstruction.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q560. Must customer/project/sample metadata also be frozen?

**Answer:** Yes. Customer, project, contract, request, and sample information that appears in a report shall be frozen in the ReportRevision/report snapshot as report-visible historical data.
This prevents later master-data changes from altering the historical meaning of an issued report.
The snapshot shall preserve the exact representation used at issuance rather than merely referencing current Customer/Project/Sample data.

**Status:** CLOSED — RECONCILED BASELINE



### Q561. Must method and accreditation metadata be frozen?

**Answer:** Yes. Method and accreditation metadata that is report-visible shall be frozen in the ReportRevision/report snapshot.

This shall preserve, where applicable:
- Method/MethodVersion representation;
- method edition/revision;
- resolved accreditation status;
- applicable scope representation;
- approved accreditation wording/mark information.

Later method or accreditation configuration changes shall not alter an issued report's historical representation.

**Status:** CLOSED — RECONCILED BASELINE



### Q562. Must analyst/approver identity be frozen?

**Answer:** Yes. Analyst and approval-chain identities that are displayed or otherwise required for report reconstruction shall be frozen in the ReportRevision/report snapshot.
The snapshot shall preserve the identity representation used at issuance, including the relevant role/title and approval relationship where applicable.
Later changes to user name, role, authorization, or account status shall not alter the historical report.

**Status:** CLOSED — RECONCILED BASELINE



### Q563. Must timestamps be frozen?

**Answer:** Yes. Report-relevant timestamps shall be frozen.

This includes, where applicable:
- report creation/preparation timestamp;
- approval timestamp;
- issue timestamp;
- relevant sample/test dates displayed on the report;
- revision timestamp;
- other report-visible controlled dates/times.

The canonical internal timestamp shall remain UTC, with the approved laboratory timezone used for user-facing representation where applicable.

**Status:** CLOSED — RECONCILED BASELINE



### Q564. Must document version and PDF hash be frozen?

**Answer:** Yes. The exact controlled DocumentVersion/template and exact issued PDF artifact shall be frozen and linked to the ReportRevision.
The issued PDF shall have an integrity hash and sufficient metadata to identify the exact persisted artifact.
A later template change, document change, or PDF regeneration shall not alter the historical association of the issued ReportRevision.

**Status:** CLOSED — RECONCILED BASELINE



### Q565. What happens if the source result changes after report creation but before issuance?

**Answer:** Report issue, reissue and withdrawal are Report/ReportRevision events plus audit evidence. They are not `approval_chain_event` records because approval-chain events are TestInstance-scoped. Re-authentication evidence is retained for the protected report action.

**Status:** CLOSED — RECONCILED BASELINE



### Q566. What happens if the source result changes after issuance?

**Answer:** If the source result changes after a report has been issued, the issued ReportRevision shall remain unchanged.
The corrected Result/ResultRevision shall trigger a controlled impact assessment to identify affected reports.
Where the correction affects an issued report, a new ReportRevision shall be created through the controlled correction/reissue process.
The original issued PDF shall remain preserved and identifiable as the earlier issued state.

**Status:** CLOSED — RECONCILED BASELINE



### Q567. How are affected report revisions found?

**Answer:** Affected report revisions shall be identified through explicit ReportResultSnapshot relationships linking each ReportRevision to the exact ResultRevision represented in that report.
A result correction shall therefore allow the system to query all ReportRevisions containing the affected Result/ResultRevision.
The relationship shall also support identification of issued PDFs and downstream report revisions requiring assessment.
Affected-report discovery shall not depend on comparing rendered PDF text.

**Status:** CLOSED — RECONCILED BASELINE



### Q568. What is the formal process for corrected reports?

**Answer:** The formal corrected-report process shall be:
**Identify correction → identify affected ResultRevision/report revisions → assess impact → authorize correction → create corrected ResultRevision where applicable → complete required Review/Verification/Approval → create new ReportRevision → freeze new snapshots → generate/persist/verify exact PDF → issue corrected report → preserve prior issued report.**
The original report shall never be overwritten.
The new report shall clearly identify its correction/revision relationship according to the approved report policy.

**Status:** CLOSED — RECONCILED BASELINE



### Q569. What is the formal process for withdrawing/recalling an issued report?

**Answer:** Withdrawal/recall of an issued report shall be a controlled event.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q570. Is report withdrawal allowed?

**Answer:** Yes. Report withdrawal shall be supported as a controlled lifecycle action where the laboratory determines that an issued report must no longer be treated as the current valid report.
Withdrawal shall require authorization and documented reason.
The withdrawn report remains permanently retrievable as historical evidence and shall be clearly identified as withdrawn.

**Status:** CLOSED — RECONCILED BASELINE



### Q571. If withdrawal is allowed, what status and evidence are required?

**Answer:** A withdrawn report shall have a distinct controlled status such as **WITHDRAWN** or another approved equivalent.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q572. Can customers see report revision history through the system?

**Answer:** Customer access to report revision history shall be controlled and shall not automatically expose the full internal revision/audit history.
The system shall support a defined customer-facing representation where the laboratory chooses to provide prior report revisions.
The customer-visible history shall include only the information approved for external disclosure.
Internal historical reconstruction shall remain available to authorized laboratory personnel independently of customer-facing visibility.

**Status:** CLOSED — RECONCILED BASELINE



### Q573. Must internal staff see all report revisions?

**Answer:** Authorized internal staff shall have access to the report history required for their role and responsibilities.
Users shall not automatically receive unrestricted access merely because they are staff.
Access shall be controlled by role/permission and confidentiality requirements, while privileged Quality/Technical/administrative roles may access the complete report revision history needed for investigation, audit, correction, and reconstruction.

**Status:** CLOSED — RECONCILED BASELINE



### Q574. What is the retention requirement for superseded PDFs?

**Answer:** Superseded and withdrawn PDFs shall remain retained for the same controlled retention period applicable to issued reports, unless a formally approved retention rule establishes a longer or otherwise specific requirement.
The exact issued PDF shall remain retrievable and integrity-verifiable throughout its required retention/archive period.
Superseded PDFs shall never be deleted merely because a newer report revision exists.

**Status:** CLOSED — RECONCILED BASELINE



### Q575. What document types must the system support?

**Answer:** The v1 document system shall support a controlled, typed set of document types rather than unrestricted arbitrary document relationships.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q576. What is the difference between Document and Attachment in laboratory practice?

**Answer:** A **Document** is a controlled logical document identity/versioned record maintained by the LIMS, such as an SOP, method document, certificate, report artifact, or other controlled document.
An **Attachment** is a file or supporting document associated with another controlled business record and does not necessarily have an independent controlled-document lifecycle.
Where an attachment itself requires controlled versioning, approval, retention, or historical identity, it shall be represented through the appropriate Document/DocumentVersion model rather than treated as an arbitrary file.

**Status:** CLOSED — RECONCILED BASELINE



### Q577. What documents are controlled documents?

**Answer:** Controlled documents are documents whose content, version, approval, effective status, applicability, or retention is subject to the laboratory's document-control process.

Examples include:
- quality-system documents;
- SOPs;
- methods and method-support documents;
- controlled forms;
- controlled work instructions;
- approved report templates;
- other laboratory documents explicitly designated as controlled.

Controlled documents shall have appropriate versioning, approval, effective dates, and historical retention.

**Status:** CLOSED — RECONCILED BASELINE



### Q578. What documents are technical records?

**Answer:** Technical records are records that provide evidence of laboratory work, observations, calculations, results, equipment use, QC, review/verification/approval, or related technical activity.
A technical record may be structured data, an immutable event/snapshot, or a controlled document/attachment.
Documents that provide evidence of technical work may therefore be both documentary objects and technical records, but the classification and retention meaning shall remain explicit.

**Status:** CLOSED — RECONCILED BASELINE



### Q579. Which documents require version control?

**Answer:** Documents requiring version control include all controlled documents and any other documents whose historical content can affect laboratory work, technical interpretation, authorization, reporting, accreditation representation, or traceability.

Examples include:
- SOPs;
- method documents;
- controlled forms;
- report templates;
- approved configuration-support documents;
- accreditation-supporting documents.

Ordinary non-controlled administrative files need not use controlled DocumentVersion semantics unless required.

**Status:** CLOSED — RECONCILED BASELINE



### Q580. Which documents require approval before use?

**Answer:** Documents requiring approval before use shall be those whose content affects controlled laboratory operation, technical work, QMS requirements, authorization, accreditation representation, calculation/reporting behavior, or other controlled processes.
At minimum, controlled SOPs, methods, report templates, controlled technical procedures, and equivalent QMS-controlled documents shall not become effective until required approval is complete.
Approval requirements shall be defined by document type.

**Status:** CLOSED — RECONCILED BASELINE



### Q581. Which documents require effective dates?

**Answer:** Effective dates shall be required for controlled documents whose applicability changes over time or whose historical use must be reconstructable.

Effective dating shall be used, where applicable, for:
- SOPs;
- methods/supporting controlled documents;
- report templates;
- controlled procedures;
- other effective-dated laboratory controls.

Documents that are purely informational and have no controlled applicability period do not require artificial effective dates.

**Status:** CLOSED — RECONCILED BASELINE



### Q582. Which documents require expiry/review dates?

**Answer:** Expiry/review dates shall be required where the laboratory's document-control process requires periodic review or a defined validity period.

The document model shall support:
- next-review date;
- expiry/end date where applicable;
- review status;
- reviewer/approver;
- extension/revision action;
- retirement/supersession.

A document should not silently remain effective after an applicable mandatory expiry without an approved disposition.

**Status:** CLOSED — RECONCILED BASELINE



### Q583. Who can upload documents?

**Answer:** Document uploads shall be permitted only to authorized users according to document type and the user's role/permission.

Upload permission shall be distinct from:
- approval;
- activation/effectivity;
- retirement;
- deletion/voiding.

A user who uploads a controlled document shall not thereby gain authority to approve or make it effective unless the approved role permits both actions and the applicable SoD rules are satisfied.
All uploads shall be audited.

**Status:** CLOSED — RECONCILED BASELINE



### Q584. Who can approve document versions?

**Answer:** Document versions shall be approved by the designated authority appropriate to the document type.

Typical authority shall include:
- Quality Authority for QMS-controlled documents;
- Technical Authority for technical methods/procedures;
- designated report authority for controlled report templates;
- other formally assigned authority where required.

The proposer/uploader and approver should be different users for controlled documents where the applicable SoD policy requires independence.
Approval shall be recorded against the exact DocumentVersion.

**Status:** CLOSED — RECONCILED BASELINE



### Q585. Who can retire document versions?

**Answer:** Document versions shall be retired by an authorized document-control/Quality authority according to the document type and governing policy.

Retirement shall preserve:
- the exact DocumentVersion;
- effective period;
- retirement reason;
- actor;
- date/time;
- superseding DocumentVersion where applicable;
- affected links/uses where required.

Retirement shall not delete the historical document version.

**Status:** CLOSED — RECONCILED BASELINE



### Q586. Can a document have multiple simultaneous active versions?

**Answer:** No. A single controlled document identity shall not have multiple simultaneously effective versions for the same scope.
One approved version shall be the effective version for a given scope/time interval.
A draft or future version may coexist with the current effective version, but overlapping effective versions shall be prevented unless the document's controlled scope explicitly distinguishes them.
Historical versions remain available for reconstruction.

**Status:** CLOSED — RECONCILED BASELINE



### Q587. Can a draft version exist while another version is effective?

**Answer:** Yes. A draft DocumentVersion may exist while another DocumentVersion is currently effective.
The draft shall remain non-effective until review/approval and its effective date are satisfied.
The current effective version shall continue governing live controlled behavior until the new version becomes effective.

**Status:** CLOSED — RECONCILED BASELINE



### Q588. What file types are allowed?

**Answer:** V1 shall use a controlled allowlist of permitted file types rather than unrestricted file upload.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q589. What maximum file sizes are allowed?

**Answer:** A maximum attachment size shall be enforced at the application level and through the reverse proxy/storage boundary.
For v1, a **50 MB maximum per uploaded file** is recommended as the default planning limit, with the ability to configure a lower limit where operationally appropriate.
Larger files shall not silently bypass the limit; they shall require a separately approved mechanism if a genuine laboratory requirement arises.
The limit shall apply consistently to uploads through all supported application paths.

**Status:** CLOSED — RECONCILED BASELINE



### Q590. Are attachments virus/malware scanned locally?

**Answer:** Controlled file uploads use an offline quarantine/malware-scan gate. V1 uses Microsoft Defender `MpCmdRun.exe -Scan -File`; unscanned or failed files remain PENDING/QUARANTINED and are not trusted by the application.

**Status:** CLOSED — RECONCILED BASELINE



### Q591. Is antivirus integration required?

**Answer:** The upload trust gate must work without Internet dependency; cloud reputation/scanning is not required for the controlled v1 upload path.

**Status:** CLOSED — RECONCILED BASELINE



### Q592. How are files named and stored?

**Answer:** Files shall be stored using application-controlled, non-user-selectable internal storage paths.
The logical Document/Attachment identity shall be stored in the database, while the physical file location shall remain an internal implementation detail.
File naming shall use collision-resistant system-generated identifiers rather than user-supplied filenames as the physical storage key.
The original filename may be retained as metadata for display and provenance.
Users shall never receive arbitrary filesystem paths as the storage mechanism.

**Status:** CLOSED — RECONCILED BASELINE



### Q593. How are file hashes stored?

**Answer:** Each stored file shall have an integrity hash, using a cryptographically appropriate hash such as **SHA-256**.
The hash shall be calculated from the exact persisted file bytes and stored with the corresponding Document/Attachment record.
The system shall use the hash for integrity verification, duplicate detection where applicable, backup/restore verification, and exact-artifact verification.
A changed file shall produce a different hash and shall not silently replace an existing controlled artifact.

**Status:** CLOSED — RECONCILED BASELINE



### Q594. Are duplicate files permitted?

**Answer:** Exact duplicate files shall not create uncontrolled duplicate content.
The system should detect identical file content using the stored content hash.
Where the same binary file is legitimately required in multiple controlled contexts, the system may allow multiple logical DocumentLink relationships while retaining one exact content identity where appropriate.
A duplicate upload shall not overwrite an existing controlled file or create ambiguous versions.

**Status:** CLOSED — RECONCILED BASELINE



### Q595. Are documents immutable after approval?

**Answer:** Yes. An approved DocumentVersion shall be immutable.
After approval/effectivity, its file content shall not be edited or replaced in place.
Any substantive correction shall create a new DocumentVersion while preserving the previous version.
Only non-substantive administrative metadata changes that do not affect the document's content, meaning, applicability, approval, or historical interpretation may be handled through controlled metadata correction, with audit evidence.

**Status:** CLOSED — RECONCILED BASELINE



### Q596. What corrections to controlled documents require a new version?

**Answer:** Any substantive correction to an approved controlled document shall require a new DocumentVersion.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q597. What document metadata is mandatory?

**Answer:** Mandatory document metadata shall include, as applicable:
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

**Status:** CLOSED — RECONCILED BASELINE



### Q598. What document link types are required?

**Answer:** DocumentLink shall use a controlled, typed set of relationship types rather than unrestricted free-text or arbitrary relationships.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q599. Which entities may legally have attached documents?

**Answer:** Only approved laboratory entities shall be permitted to have Document/Attachment relationships.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q600. What is the closed set of allowed polymorphic DocumentLink entity types?

**Answer:** The polymorphic DocumentLink target shall use a **closed, explicitly controlled entity-type set**.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q601. Can users delete attachments?

**Answer:** Users shall not directly delete controlled attachments or documents after they become part of the controlled record.

Where a file is erroneously uploaded:
- the original upload remains auditable;
- the file may be marked invalid/void/unusable through a controlled process;
- a replacement file, where required, is uploaded as a new controlled object/version;
- the reason, actor, timestamp, and disposition are retained.

Physical deletion may occur only where separately authorized by the applicable retention/disposition rule and shall never be used to rewrite required historical evidence.

**Status:** CLOSED — RECONCILED BASELINE



### Q602. If deletion is not allowed, how are erroneous uploads handled?

**Answer:** Erroneous uploads shall be handled through controlled invalidation/voiding rather than silent deletion.
The system shall retain the original upload's identity, metadata, hash, uploader, timestamp, reason, and disposition.
A corrected document shall be stored as a new upload or DocumentVersion as appropriate.
The invalid upload shall no longer be used as the effective document, but its historical existence shall remain traceable.

**Status:** CLOSED — RECONCILED BASELINE



### Q603. What happens when the underlying file is missing or corrupted?

**Answer:** If an underlying file is missing, unreadable, or fails integrity verification:
1. the Document/Attachment shall be marked as integrity-failed or unavailable;
2. the stored hash and expected artifact identity shall be retained;
3. the event shall be audited;
4. affected records shall be identified where the file is operationally or historically significant;
5. restoration from a validated backup shall be attempted through the controlled recovery procedure;
6. the restored file shall be rehashed and independently verified;
7. unresolved loss shall be escalated as a documented recovery/nonconformance event.

The system shall never silently substitute an unverified file for the original artifact.

**Status:** CLOSED — RECONCILED BASELINE



### Q604. Must storage integrity be periodically verified?

**Answer:** Document/storage integrity checks hash-verify a rotating **1/7 slice weekly**, a **full pass monthly**, and a **full pass after every restore or deployment**. Hash mismatch triggers controlled incident/recovery handling and affected use is blocked as appropriate.

### Q605. What events must always create audit records?

**Answer:** All controlled state changes, security events, workflow decisions, report/document issuance, configuration changes and significant operational failures always create audit events.

**Status:** CLOSED — RECONCILED BASELINE



### Q606. Which read events, if any, must be audited?

**Answer:** Read/access events shall be audited for categories where access itself is security-, confidentiality-, integrity-, or disclosure-significant.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q607. Which authentication events must be audited?

**Answer:** Log login success/failure, logout, session creation/expiry/revocation, password changes/resets, account lockout and other authentication/security events.

**Status:** CLOSED — RECONCILED BASELINE



### Q608. Which authorization failures must be audited?

**Answer:** Authorization failures must always be audited.

**Status:** CLOSED — RECONCILED BASELINE



### Q609. Which sample events must be audited?

**Answer:** Audit receipt, registration, identification, acceptance/rejection, conditional acceptance, allocation, movement, storage, disposal, identity correction and sample status changes.

**Status:** CLOSED — RECONCILED BASELINE



### Q610. Which TestInstance events must be audited?

**Answer:** Audit TestInstance creation, assignment, reassignment, start/stop, hold, rework, retest, cancellation, reopening and state transitions.

**Status:** CLOSED — RECONCILED BASELINE



### Q611. Which result events must be audited?

**Answer:** Audit result creation, submission, revision, correction, reopen and status changes.

**Status:** CLOSED — RECONCILED BASELINE



### Q612. Which calculation events must be audited?

**Answer:** Audit CalculationRun creation/execution/failure and exact FormulaVersion/engine version references.

**Status:** CLOSED — RECONCILED BASELINE



### Q613. Which review/verification/approval events must be audited?

**Answer:** Audit every Review/Verification/Approval attempt, success/failure/revocation/reopen.

**Status:** CLOSED — RECONCILED BASELINE



### Q614. Which report events must be audited?

**Answer:** Audit report generation, revision creation, issue, amendment, reissue, withdrawal, void, failed generation and delivery events.

**Status:** CLOSED — RECONCILED BASELINE



### Q615. Which configuration events must be audited?

**Answer:** Audit controlled configuration proposal, approval, rejection, implementation, activation, retirement and emergency change events.

**Status:** CLOSED — RECONCILED BASELINE



### Q616. Which accreditation changes must be audited?

**Answer:** Audit every accreditation-scope proposal/change/approval/effective-date change/reversal.

**Status:** CLOSED — RECONCILED BASELINE



### Q617. Which user/role changes must be audited?

**Answer:** Audit user creation, disabling, reactivation, password/security changes, role assignment/removal and authorization changes.

**Status:** CLOSED — RECONCILED BASELINE



### Q618. Which document events must be audited?

**Answer:** Audit document upload, approval, activation, retirement, supersession, voiding, link/unlink, download of sensitive controlled documents and integrity failures.

**Status:** CLOSED — RECONCILED BASELINE



### Q619. Which backup/restore events must be audited?

**Answer:** Audit backup creation, validation, failure, restore, recovery test, migration and recovery verification.

**Status:** CLOSED — RECONCILED BASELINE



### Q620. What actor information is required in each audit event?

**Answer:** Each audit event requires event ID, timestamp, actor/system, event type, target entity/record, outcome and relevant before/after/change context.

**Status:** CLOSED — RECONCILED BASELINE



### Q621. Is user ID sufficient, or must role/session/device information also be stored?

**Answer:** User ID alone is insufficient for high-risk events. Store actor ID, effective role/authorization context, session ID, source host/IP where available, authentication context, and system/service identity where applicable.

**Status:** CLOSED — RECONCILED BASELINE



### Q622. What timestamp standard will be used?

**Answer:** Use UTC as the internal canonical timestamp.

**Status:** CLOSED — RECONCILED BASELINE



### Q623. Is UTC required internally?

**Answer:** Yes. UTC should be stored internally.

**Status:** CLOSED — RECONCILED BASELINE



### Q624. What timezone should be displayed to users?

**Answer:** User-facing time uses the deployment's configured laboratory timezone; this should not be hard-coded to India in the reusable product.

**Status:** CLOSED — RECONCILED BASELINE



### Q625. How are old audit records retained?

**Answer:** Audit records follow the laboratory's configured retention policy; your current baseline is 10 years active retention followed by controlled archival.

**Status:** CLOSED — RECONCILED BASELINE



### Q626. Can audit events ever be archived separately?

**Answer:** Yes. Audit records may be archived separately, provided linkage, integrity, retrievability and retention remain intact.

**Status:** CLOSED — RECONCILED BASELINE



### Q627. Can an audit record ever be corrected?

**Answer:** No direct correction. An existing audit event is immutable.

**Status:** CLOSED — RECONCILED BASELINE



### Q628. If an audit record is wrong, how is the correction represented without rewriting history?

**Answer:** A correction is represented by a new compensating/correction event referring to the original event; original audit content remains unchanged.

**Status:** CLOSED — RECONCILED BASELINE



### Q629. Who can view audit records?

**Answer:** Only authorized roles should view audit records.

**Status:** CLOSED — RECONCILED BASELINE



### Q630. Are audit records visible to all administrators or only selected roles?

**Answer:** Not every administrator automatically gets unrestricted audit access. Audit access should be a specific privileged permission.

**Status:** CLOSED — RECONCILED BASELINE



### Q631. Are audit searches/filtering required?

**Answer:** Yes. Audit search/filtering is required.

**Status:** CLOSED — RECONCILED BASELINE



### Q632. Must audit records be exportable?

**Answer:** Yes. Authorized users may export audit records in a controlled format.

**Status:** CLOSED — RECONCILED BASELINE



### Q633. Are audit exports themselves audited?

**Answer:** Yes. Audit exports must themselves generate audit events.

**Status:** CLOSED — RECONCILED BASELINE



### Q634. What database trigger protections are required exactly?

**Answer:** Append-only controlled event tables require DB-level UPDATE/DELETE protection using SQLite triggers that abort unauthorized changes.

**Status:** CLOSED — RECONCILED BASELINE



### Q635. Which tables are append-only?

**Answer:** At minimum: audit_event, approval_chain_event, result_revision, report_result_snapshot, calculation_run, and other historical event/snapshot tables designated append-only by the schema contract.

**Status:** CLOSED — RECONCILED BASELINE



### Q636. Which tables require database-level protection against UPDATE/DELETE?

**Answer:** All append-only historical/event/snapshot tables require database-level protection against UPDATE/DELETE; current-state tables use appropriate controls according to their lifecycle.

**Status:** CLOSED — RECONCILED BASELINE



### Q637. What is the approved behavior if trigger protection conflicts with a migration?

**Answer:** Migrations that affect protected tables must use an explicitly designed/tested migration path that preserves all data and recreates protections. No ad-hoc trigger disabling in ordinary operation.

**Status:** CLOSED — RECONCILED BASELINE



### Q638. How is audit atomicity tested?

**Answer:** Test transaction atomicity using failure injection, rollback tests, concurrency tests, audit/business-write consistency checks and database-integrity checks.

---

# 22. Authentication and Account Security

**Status:** CLOSED — RECONCILED BASELINE



### Q639. What are the exact user account fields?

**Answer:** User account contains: immutable internal User ID, unique username, legal/display name, staff/employee ID where applicable, email/phone if supplied, status, password/authenticator metadata, creation/activation/deactivation data, and security/session metadata. Roles are assigned through separate role-assignment records.

**Status:** CLOSED — RECONCILED BASELINE



### Q640. Is a unique username required?

**Answer:** Yes. Username must be globally unique within the deployment.

**Status:** CLOSED — RECONCILED BASELINE



### Q641. Is email required?

**Answer:** No. Email is optional unless a deployment-specific workflow requires it. Core authentication cannot depend on email because the system is offline-first.

**Status:** CLOSED — RECONCILED BASELINE



### Q642. Is phone number required?

**Answer:** No. Phone is optional.

**Status:** CLOSED — RECONCILED BASELINE



### Q643. Is employee/staff ID required?

**Answer:** Yes for laboratory staff where an official employee/staff ID exists. It is an identity/provenance attribute, not the login credential.

**Status:** CLOSED — RECONCILED BASELINE



### Q644. How are disabled users represented?

**Answer:** Separate ACTIVE, PENDING, DISABLED, SUSPENDED/LOCKED status concepts. Temporary lockout must not be confused with deliberate account disabling.

**Status:** CLOSED — RECONCILED BASELINE



### Q645. What password policy is required?

**Answer:** Password minimum is **8 characters**; passwords of at least 64 characters are accepted. No composition rules and no periodic expiry. A mandatory offline blocklist covers common passwords plus username/laboratory-name/`labnexus` variants. Argon2id, 5-failure/15-minute lockout, per-IP throttling and password history of 5 are mandatory.

**Status:** CLOSED — APPROVED SECURITY BASELINE
**Primary Closure Artifact / Decision Record:** Security Baseline



### Q646. What is the minimum password length?

**Answer:** The approved v1 minimum is **8**, not 12 or 15. The Project Owner has accepted the associated risk for the single-site, LAN-only, offline deployment. A 12-character privileged-role minimum remains an explicit option, not the default.

**Status:** CLOSED — RECONCILED BASELINE



### Q647. Are password complexity rules required?

**Answer:** The offline password blocklist is mandatory and local. Passwords matching the controlled common-password set or the username, laboratory name or `labnexus` variants are rejected.

**Status:** CLOSED — RECONCILED BASELINE



### Q648. How long is password history retained?

**Answer:** Password history prevents reuse of the most recent **5** passwords and is enforced server-side without administrator/UI bypass.

**Status:** CLOSED — APPROVED SECURITY BASELINE
**Primary Closure Artifact / Decision Record:** Security Baseline



### Q649. How often must passwords be changed, if at all?

**Answer:** No periodic password expiry. Force change when compromised, explicitly reset, or otherwise required by security incident.

**Status:** CLOSED — RECONCILED BASELINE



### Q650. Are forced password changes required after administrative reset?

**Answer:** Yes. Administrative password reset must force a new password at next authentication.

**Status:** CLOSED — RECONCILED BASELINE



### Q651. Who can reset passwords?

**Answer:** Authorized System Administrator/User Access Administrator may initiate reset after identity verification. The reset itself is audited.

**Status:** CLOSED — RECONCILED BASELINE



### Q652. Does a password reset invalidate existing sessions?

**Answer:** Yes. Password reset invalidates all existing sessions for the user.

**Status:** CLOSED — RECONCILED BASELINE



### Q653. How are failed login attempts handled?

**Answer:** Failed logins are rate-limited, recorded, and subject to progressive delay/temporary lockout.

**Status:** CLOSED — RECONCILED BASELINE



### Q654. Is account lockout required?

**Answer:** Yes, temporary account lockout/protection is required, combined with throttling so attackers cannot trivially lock out users indefinitely.

**Status:** CLOSED — RECONCILED BASELINE



### Q655. If lockout is required, what threshold and duration apply?

**Answer:** Authentication failure handling is **5 failures → 15-minute lockout**, plus per-IP throttling. The control is server-side and is not bypassed by refreshing or restarting the browser.

**Status:** CLOSED — APPROVED SECURITY BASELINE
**Primary Closure Artifact / Decision Record:** Security Baseline



### Q656. Is IP-based throttling required?

**Answer:** Yes. Apply IP/source-based throttling in addition to per-account throttling.

**Status:** CLOSED — RECONCILED BASELINE



### Q657. Is session timeout fixed or configurable?

**Answer:** Session timeout should be deployment-configurable within platform-defined safe bounds.

**Status:** CLOSED — RECONCILED BASELINE



### Q658. What is the idle timeout?

**Answer:** Session policy is **30 minutes idle timeout and 12 hours absolute lifetime**. Server-side sessions are invalidated appropriately on logout, expiry, disablement and security events; high-risk actions additionally require fresh password re-entry.

**Status:** CLOSED — APPROVED SECURITY BASELINE
**Primary Closure Artifact / Decision Record:** Security Baseline



### Q659. What is the absolute session lifetime?

**Answer:** MFA is not required in v1. The approved baseline instead relies on Argon2id, server-side sessions, secure cookies, CSRF protection, lockout/throttling, password history, high-risk re-entry and backend authorization.

**Status:** CLOSED — APPROVED SECURITY BASELINE
**Primary Closure Artifact / Decision Record:** Security Baseline



### Q660. What happens when a user logs out?

**Answer:** Logout immediately invalidates the server-side session and clears the browser authentication state.

**Status:** CLOSED — RECONCILED BASELINE



### Q661. How are all sessions revoked for a user?

**Answer:** Server-side session revocation by user/session/all-session scope; revoke all sessions is required.

**Status:** CLOSED — RECONCILED BASELINE



### Q662. Must administrators be able to terminate sessions?

**Answer:** Yes. Authorized administrators can terminate selected or all sessions.

**Status:** CLOSED — RECONCILED BASELINE



### Q663. What cookie security flags are mandatory?

**Answer:** Session cookie: Secure, HttpOnly, SameSite=Strict, Path=/, preferably __Host- prefix, no sensitive data in cookie. OWASP recommends these protections.

**Status:** CLOSED — RECONCILED BASELINE



### Q664. What CSRF protection approach is approved?

**Answer:** Use server-side synchronizer CSRF tokens tied to the authenticated session, plus Origin/Referer validation as defense in depth.

**Status:** CLOSED — RECONCILED BASELINE



### Q665. Is HTTPS mandatory even on the LAN?

**Answer:** Yes. HTTPS is mandatory even on the LAN. OWASP explicitly recommends TLS for the entire authenticated session.

**Status:** CLOSED — RECONCILED BASELINE



### Q666. How will certificates be managed offline?

**Answer:** Use an offline local/private CA. For the small deployment, Caddy's internal CA is a practical baseline; install/trust the CA certificate on authorized workstations. Manage renewal without Internet dependency.

**Status:** CLOSED — RECONCILED BASELINE



### Q667. Is HTTP allowed only during initial setup or never?

**Answer:** No HTTP over the LAN. Production application access is HTTPS-only. A loopback-only bootstrap/maintenance endpoint may exist if technically necessary, but must not be exposed to LAN clients.

**Status:** CLOSED — RECONCILED BASELINE



### Q668. Are local host-only administrative endpoints required?

**Answer:** Yes. Host-only operational endpoints may exist for health, controlled maintenance, migration/recovery and bootstrap, but they are not authorization bypasses and should not expose normal laboratory data operations.

**Status:** CLOSED — RECONCILED BASELINE



### Q669. Is concurrent login from multiple workstations allowed?

**Answer:** Concurrent sessions from multiple workstations are **permitted for an individual named user**, subject to the approved account/session policy. Shared user accounts remain prohibited. Each session remains independently attributable, and high-risk actions require fresh authentication.

**Status:** CLOSED — APPROVED SECURITY BASELINE
**Primary Closure Artifact / Decision Record:** Security Baseline



### Q670. Is concurrent login from multiple browsers allowed?

**Answer:** Concurrent sessions from multiple browsers are **permitted for an individual named user**, subject to the approved account/session policy. Shared accounts are prohibited. Session identifiers are independent and high-risk actions require fresh password re-entry.

**Status:** CLOSED — APPROVED SECURITY BASELINE
**Primary Closure Artifact / Decision Record:** Security Baseline



### Q671. Are shared user accounts prohibited?

**Answer:** Yes. Shared user accounts are prohibited.

**Status:** CLOSED — RECONCILED BASELINE



### Q672. How is user identity verified before account creation?

**Answer:** Account creation requires identity verification by an authorized person using the laboratory's staff identity/onboarding evidence.

**Status:** CLOSED — RECONCILED BASELINE



### Q673. What happens to audit history when a user is disabled or renamed?

**Answer:** Audit history remains associated with the immutable internal User ID. Disabling a user never removes or rewrites historical actor references.

**Status:** CLOSED — RECONCILED BASELINE



### Q674. Can usernames be changed?

**Answer:** Username changes may be permitted as a controlled administrative operation, but the immutable internal User ID never changes and the old username is retained in history.

**Status:** CLOSED — RECONCILED BASELINE



### Q675. What happens if a user leaves the laboratory?

**Answer:** Disable the account immediately; revoke all sessions; remove future access; retain all historical records/audit attribution under the original User ID.

---

# 23. RBAC and Permission Model

**Status:** CLOSED — RECONCILED BASELINE



### Q676. What roles are needed at launch?

**Answer:** Role possession alone is not an SoD violation. Each protected action is evaluated against permission, competence, workflow state, scope and recorded TestInstance action history. Prohibited action combinations remain blocked regardless of other roles held.

**Status:** CLOSED — RECONCILED BASELINE



### Q677. What permissions are needed at launch?

**Answer:** Launch permissions shall cover at minimum:
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

**Status:** CLOSED — RECONCILED BASELINE



### Q678. What is the smallest meaningful permission unit?

**Answer:** The smallest meaningful permission unit shall be a controlled **action on a defined resource within an applicable context**.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q679. Are permissions action-based, entity-based, workflow-based, or a combination?

**Answer:** Permissions shall use a combination of:
- action-based permissions;
- resource/entity scope;
- workflow/state conditions;
- competence/authorization;
- TestInstance-specific SoD;
- effective-dated role assignments;
- other controlled contextual restrictions where necessary.

RBAC provides the base authorization model, while backend/domain rules determine whether the requested action is actually permitted in the current context.

**Status:** CLOSED — RECONCILED BASELINE



### Q680. Are permissions separated for create/read/update/delete/approve/issue/export actions?

**Answer:** Yes. Permissions shall distinguish materially different actions such as:
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

**Status:** CLOSED — RECONCILED BASELINE



### Q681. Are view permissions different from action permissions?

**Answer:** Yes. View/read permissions shall be distinct from action permissions.
A user may have permission to view a record without having permission to modify, approve, issue, export, correct, or otherwise act upon it.
Sensitive document/report/audit access may have additional read/export restrictions.

**Status:** CLOSED — RECONCILED BASELINE



### Q682. Who can manage roles?

**Answer:** Role creation, modification, retirement, and permission assignment shall be restricted to authorized system/user-access administrators under controlled governance.
Changing role definitions shall be treated as a controlled authorization change and shall require appropriate approval.
Ordinary laboratory users shall not manage role definitions.

**Status:** CLOSED — RECONCILED BASELINE



### Q683. Who can assign roles to users?

**Answer:** Role assignment shall be executed by an authorized System/User Access Administrator only after approval by the designated User Access Approver.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q684. Can a user have multiple roles?

**Answer:** Yes. A user may hold multiple roles.
Having multiple roles is not by itself an SoD violation.

The system shall evaluate the actual action against:
- the user's effective permissions;
- competence/authorization;
- workflow state;
- TestInstance history;
- hard SoD rules;
- policy-controlled SoD rules.

**Status:** CLOSED — RECONCILED BASELINE



### Q685. If multiple roles grant permissions, are permissions additive?

**Answer:** Yes. Where multiple valid roles apply, their permissions are generally additive.

However, additive permission does not override:
- workflow restrictions;
- competence requirements;
- effective dates;
- TestInstance-level SoD;
- hard authorization blocks;
- other domain rules.

A role cannot grant an action that the domain state or hard SoD rules prohibit.

**Status:** CLOSED — RECONCILED BASELINE



### Q686. Can a role deny a permission granted by another role?

**Answer:** No general role-level explicit-deny mechanism is required for v1.

The authoritative model should use:
**default deny + explicit grant + domain/SoD enforcement.**

Where two roles provide overlapping permissions, the effective permission is additive unless a higher-priority domain rule prevents the action.
Hard prohibitions shall be enforced independently of role grants and cannot be overridden by adding another role.

**Status:** CLOSED — RECONCILED BASELINE



### Q687. Is explicit deny required?

**Answer:** No separate general-purpose explicit-deny permission layer is required for v1.
An action is permitted only when an applicable permission exists and all contextual/domain conditions are satisfied.
Hard-blocked actions shall remain blocked regardless of the user's other roles or permissions.
This keeps authorization deterministic and avoids contradictory grant/deny combinations.

**Status:** CLOSED — RECONCILED BASELINE



### Q688. Are permissions scoped by discipline, site, or TestInstance?

**Answer:** Yes. Permissions shall support controlled contextual scope.

For v1 this may include:
- discipline/TestDefinition scope;
- workflow action;
- TestInstance;
- equipment or document type where applicable;
- administrative scope;
- effective role assignment.

V1 has exactly one physical laboratory/site, so a multi-site permission model is not required.
TestInstance-specific SoD shall be evaluated independently for each TestInstance.

**Status:** CLOSED — RECONCILED BASELINE



### Q689. Are permissions time-limited?

**Answer:** Yes. Role/authorization assignments shall be capable of being effective-dated.

The system shall support:
- effective-from;
- effective-to where applicable;
- current status;
- historical assignment;
- future assignment where approved.

The authorization applicable at the time of an action shall remain historically reconstructable.

**Status:** CLOSED — RECONCILED BASELINE



### Q690. Are temporary role assignments required?

**Answer:** Yes. Temporary role assignments shall be supported where operationally required.

Temporary assignments shall have:
- defined scope;
- effective start;
- effective end;
- approving authority;
- reason where applicable;
- audit history.

They shall automatically cease to grant authority after their effective period expires.

**Status:** CLOSED — RECONCILED BASELINE



### Q691. Are role assignments effective-dated?

**Answer:** Yes. Role assignments shall be effective-dated.
A role assignment shall have a defined period of validity, allowing the system to determine which authorization was effective at a particular date/time.
Historical actions shall be attributable to the authorization state that applied when the action occurred.

**Status:** CLOSED — RECONCILED BASELINE



### Q692. Can a role assignment overlap another assignment?

**Answer:** Role assignments may overlap where they represent different valid roles or scopes.
However, the same user shall not have overlapping assignments for the **same role and same scope** unless the overlap is explicitly meaningful and governed.
Conflicting or ambiguous overlapping assignments shall be rejected or require controlled resolution before becoming effective.

**Status:** CLOSED — RECONCILED BASELINE



### Q693. What is the rule for conflicting role assignments?

**Answer:** Conflicting role assignments shall be resolved by the Authorization Matrix and role-assignment governance rather than by arbitrary permission precedence.

Where assignments create an impermissible authorization or SoD combination:
- the conflicting assignment shall not become effective;
- the system shall identify the conflict;
- the assigning/approving authority shall resolve it through role/scope changes or approved policy;
- hard SoD restrictions shall remain absolute.

Permissible multiple-role combinations shall remain allowed where they do not create a prohibited action.

**Status:** CLOSED — RECONCILED BASELINE



### Q694. Are inactive users automatically denied all actions?

**Answer:** Yes. Inactive, disabled, or suspended users shall be denied normal application actions.
The denial shall apply regardless of previously assigned roles.
Any host/system recovery functions are outside ordinary laboratory-user authorization and shall remain separately controlled.
Historical records and audit attribution associated with the user shall remain intact.

**Status:** CLOSED — RECONCILED BASELINE



### Q695. Does deactivation terminate existing sessions immediately?

**Answer:** Yes. User deactivation shall immediately terminate the user's active application sessions and prevent creation/use of new sessions.
Any existing session shall be invalidated server-side rather than being allowed to continue until its ordinary timeout.
The deactivation event and resulting session revocation shall be audited.

**Status:** CLOSED — RECONCILED BASELINE



### Q696. Are special permissions needed for emergency configuration changes?

**Answer:** Yes. Emergency configuration changes shall require a specific controlled permission that is distinct from ordinary configuration administration.

The permission shall not by itself bypass:
- proposal/authorization requirements;
- hard SoD blocks;
- evidence/countersigning;
- post-change verification;
- retrospective review.

Emergency configuration authority shall be granted only to designated competent users.

**Status:** CLOSED — RECONCILED BASELINE



### Q697. Are special permissions needed for report reissue?

**Answer:** Yes. Report reissue shall require a distinct controlled permission.

Reissue shall be subject to:
- affected-report identification;
- authorized reason/process;
- required technical/quality approval;
- correct ReportRevision creation;
- exact snapshot preservation;
- PDF integrity/issuance controls;
- applicable SoD.

Possession of ordinary report-view or report-generation permission shall not imply reissue authority.

**Status:** CLOSED — RECONCILED BASELINE



### Q698. Are special permissions needed for result correction?

**Answer:** Yes. Result correction shall require a distinct controlled permission and correction workflow.

Correction authority shall be evaluated together with:
- correction reason;
- current TestInstance/Result state;
- required authorization;
- SoD;
- Review/Verification/Approval consequences;
- Report impact;
- ResultRevision requirements.

Ordinary result-edit permission shall not allow correction of an already approved result.

**Status:** CLOSED — RECONCILED BASELINE



### Q699. Are special permissions needed for reopening?

**Answer:** Yes. Reopening shall require a distinct controlled permission.
Reopen authority shall be limited to designated competent Technical/Quality authority according to the approved workflow and SoD policy.
A Reopen permission shall not itself permit direct editing of approved records; the resulting work must follow the controlled Reopen → Correction/Rework → Review/Verification/Approval path as applicable.

**Status:** CLOSED — RECONCILED BASELINE



### Q700. Are special permissions needed for backup/restore operations?

**Answer:** Yes. Backup/restore operations shall require privileged operational permissions separate from laboratory technical permissions.

Backup and restore authority shall be limited to designated Technical/Operations/System Administration personnel and shall include:
- backup creation;
- backup validation;
- restore execution;
- recovery testing;
- recovery verification.

Restore operations shall not provide a hidden mechanism for bypassing application authorization or controlled audit requirements.
All backup/restore activity shall be audited.

**Status:** CLOSED — RECONCILED BASELINE



### Q701. Are administrator permissions intentionally separated from laboratory technical permissions?

**Answer:** Yes. System/administrative permissions shall be intentionally separated from laboratory technical permissions.
System administrators manage the application infrastructure, accounts, configuration implementation, deployment, backup/recovery, and related operational functions according to their authority.
Laboratory technical roles perform and approve laboratory work.
Administrative privileges shall not automatically grant technical Review, Verification, Approval, result correction, or other laboratory decision-making authority.

**Status:** CLOSED — RECONCILED BASELINE



### Q702. Must system administrators be prevented from approving technical laboratory results?

**Answer:** The System Administrator may perform system administration but **cannot approve technical laboratory results** merely because the same individual also holds the Project Owner role. Result approval remains subject to the technical authorization, competence and SoD rules.

**Status:** CLOSED — RECONCILED BASELINE



### Q703. Must database/server administrators be prevented from changing records through the application?

**Answer:** Yes. Database/server administrators shall not be able to modify laboratory records **through the LabNexus application** merely because they possess infrastructure privileges.
The application shall authorize all normal record changes through the domain/application layer.
Direct filesystem/database access is outside the LIMS application authorization boundary and shall instead be controlled by the Windows/host security boundary, operational procedures, and restricted administrative access.
The system shall not claim that application authorization prevents a person who has unrestricted operating-system/database access from directly manipulating the underlying SQLite file.

**Status:** CLOSED — RECONCILED BASELINE



### Q704. How is privilege escalation prevented and tested?

**Answer:** Privilege escalation shall be prevented through:
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

**Status:** CLOSED — RECONCILED BASELINE



### Q705. What is the authoritative list of hard-blocked same-TestInstance combinations?

**Answer:** The SoD rules are explicit per TestInstance: Analyst→Review/Verification/Approval and Reviewer→Verification are hard BLOCKs; Reviewer→Approval and Verifier→Approval default to BLOCK and require an approved, countersigned exception mechanism where policy permits. Emergencies never bypass hard blocks.

**Status:** CLOSED — RECONCILED BASELINE



### Q706. What is the authoritative list of policy-controlled combinations?

**Answer:** Policy-controlled combinations shall be explicitly listed in the effective-dated SoD Matrix rather than inferred from general role permissions.
At minimum, **Technical Reviewer → Approval on the same TestInstance** shall be policy-controlled, with BLOCK as the default unless an approved rule explicitly permits the combination.
Other combinations involving Reopen, Correction Approval, Report Reissue, Configuration Approval, or emergency/exception actions shall likewise be explicitly classified as:
- permitted;
- blocked; or
- permitted only under defined conditions/exception.

No action shall be considered policy-controlled merely because the UI exposes it.

**Status:** CLOSED — RECONCILED BASELINE



### Q707. What exactly does “policy-controlled” mean operationally?

**Answer:** A **policy-controlled** action is an action whose legality depends on an explicit approved policy rule in addition to ordinary role permission.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q708. Is a policy-controlled action allowed automatically, conditionally, or only with an explicit exception?

**Answer:** A policy-controlled action shall not be treated as automatically permitted merely because the user possesses the relevant roles.

**- The SoD Matrix shall explicitly classify the combination as:**
**- normally allowed subject to stated conditions;**
**- conditionally allowed;**
**- exception-only; or**
**- blocked.**

For example, Technical Reviewer → Approval on the same TestInstance shall remain blocked unless an approved policy explicitly permits it.
Emergency handling may apply only where the policy-controlled combination explicitly permits an emergency exception.

**Status:** CLOSED — RECONCILED BASELINE



### Q709. Where is the policy stored?

**Answer:** The authoritative SoD policy shall be stored as controlled, versioned configuration within the LIMS governance model and represented by the SoD Matrix.

Each policy version shall have:
- unique identity/version;
- effective date/time;
- approval evidence;
- proposer/approver;
- controlled rules;
- status;
- supersession history.

The applicable policy version shall be reconstructable for historical Review, Verification, Approval, correction, reopen, report reissue, and configuration actions.

**Status:** CLOSED — RECONCILED BASELINE



### Q710. Who can change the policy?

**Answer:** Changes to the SoD policy shall require controlled proposal and approval.

For v1:
- the **Laboratory Quality Authority + Project Owner** shall approve SoD policy changes;
- Technical Authority shall review implementability where necessary;
- proposer and approver shall not be the same person for controlled changes;
- the implementation shall be separately executed and verified;
- the effective date/time shall be explicit;
- the prior policy version shall remain historically preserved.

Emergency changes shall follow the approved emergency configuration governance and shall never bypass hard SoD blocks.

**Status:** CLOSED — RECONCILED BASELINE



### Q711. Does policy change require proposal and approval?

**Answer:** Yes. SoD policy changes shall require a formal proposal and approval process.

The proposal shall identify:
- current and proposed rule;
- reason for change;
- affected roles/actions;
- affected workflows;
- impact on existing work;
- effective date/time;
- implementation/verification requirements.

The approved change shall become effective only after the required authorization and verification steps are complete.

**Status:** CLOSED — RECONCILED BASELINE



### Q712. When does a policy change become effective?

**Answer:** A new SoD policy version shall become effective only after:
1. proposal;
2. review;
3. required approval;
4. implementation/activation readiness verification;
5. defined effective date/time.

The policy shall not become effective merely because the database record has been entered.
Actions occurring before and after the effective point shall be evaluated against the corresponding policy version.

**Status:** CLOSED — RECONCILED BASELINE



### Q713. Is policy versioning required?

**Answer:** Yes. SoD policy versioning is mandatory.

Each approved change shall create a distinct policy version with its own:
- identity;
- content;
- effective interval;
- approval evidence;
- implementation evidence.

Previous versions shall remain immutable and available for historical reconstruction.

**Status:** CLOSED — RECONCILED BASELINE



### Q714. Must a historical approval reconstruct the SoD policy version in effect at that time?

**Answer:** Yes. Historical approval/review/verification actions shall be reconstructable against the **SoD policy version that was effective when the action occurred**.

The relevant approval-chain event shall therefore identify or allow deterministic resolution of:
- policy version;
- effective date/time;
- actor;
- role/authorization context;
- TestInstance;
- action/stage;
- outcome.

Later SoD policy changes shall not retroactively rewrite the authorization basis of historical actions.

**Status:** CLOSED — RECONCILED BASELINE



### Q715. How are cross-TestInstance actions handled?

**Answer:** SoD shall be evaluated **per TestInstance**.
An action performed on one TestInstance shall not automatically create an SoD conflict on another TestInstance.

For example, the same user may:
- perform Analysis on TestInstance A;
- perform Review on TestInstance B;
- perform Verification on TestInstance C;
where otherwise authorized.

The hard same-TestInstance restrictions remain applicable independently to each TestInstance.

**Status:** CLOSED — RECONCILED BASELINE



### Q716. Can the same user review one TestInstance and analyze another?

**Answer:** Yes. A user may review one TestInstance and analyze another.
The system shall evaluate authorization and SoD against the specific TestInstance on which the action is being performed.

The user shall still satisfy all applicable:
- role/permission requirements;
- competence requirements;
- workflow-state requirements;
- TestDefinition requirements;
- effective authorization;
- other SoD rules.

Same-user participation across different TestInstances shall not be treated as a global historical conflict unless an explicitly approved laboratory policy states otherwise.

**Status:** CLOSED — RECONCILED BASELINE



### Q717. What happens when a user performs an action before an SoD policy change and another after the change?

**Answer:** An SoD policy change shall apply according to its defined effective date/time.
Actions completed before the new policy becomes effective shall remain governed by the prior policy version. Actions performed after the effective point shall be evaluated against the new policy version.
Historical approval-chain events shall preserve or deterministically identify the applicable policy version so that later policy changes cannot rewrite historical authorization decisions.

**Status:** CLOSED — RECONCILED BASELINE



### Q718. Are emergency SoD exceptions allowed?

**Answer:** Emergency SoD exceptions may be permitted only for **policy-controlled** combinations where the approved laboratory policy explicitly allows them.
Emergency handling shall never bypass absolute hard blocks, including the defined hard-blocked same-TestInstance Analyst/Reviewer combinations.
Any permitted emergency exception shall be bounded, visibly identified, authorized, independently countersigned where required, fully audited, and retrospectively reviewed.

**Status:** CLOSED — RECONCILED BASELINE



### Q719. What evidence is required for an exception?

**Answer:** An SoD exception shall preserve sufficient evidence to establish what exception occurred and why.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q720. How is exception frequency monitored?

**Answer:** Emergency SoD-exception frequency shall be monitored through an auditable operational report.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q721. What constitutes excessive emergency use?

**Answer:** Emergency configuration is a bounded, visible and attributable path with reason, authorizer, executor, exact change, risk, timing, evidence, expiry and retrospective review. Emergency status cannot bypass hard SoD.

**Status:** CLOSED — RECONCILED BASELINE



### Q722. Who reviews emergency-use reports?

**Answer:** Emergency-use reports shall be reviewed by the **Laboratory Quality Authority together with the relevant Technical/Operations Authority**.
Where an emergency involved security or system-access controls, the responsible System/Security authority shall also participate.
The review shall assess frequency, reasons, repeated patterns, policy compliance, effectiveness of controls, and whether a recurring emergency indicates the need for a normal controlled change.

**Status:** CLOSED — RECONCILED BASELINE



### Q723. Which configuration items are controlled?

**Answer:** Controlled configuration includes methods, MethodVersions, TestDefinitions, parameters, formulas, constants, lookup tables, QC rules, equipment requirements/eligibility, accreditation scope, report templates/rules, workflows, numbering rules, rates, TAT rules, SoD policy, controlled document settings and other settings capable of affecting controlled laboratory operation.

**Status:** CLOSED — RECONCILED BASELINE



### Q724. Which configuration items are ordinary administrative settings?

**Answer:** Ordinary administrative settings include non-controlled UI preferences, display preferences, user-specific dashboard settings and other settings that cannot alter controlled technical records, authorization, reports or compliance behavior.

**Status:** CLOSED — RECONCILED BASELINE



### Q725. Which configuration items affect technical records?

**Answer:** Any configuration capable of changing the meaning, validity, traceability or lifecycle of a technical record is controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q726. Which configuration items affect report output?

**Answer:** Any configuration affecting report content, calculation, wording, layout, accreditation representation, revision behavior or issuance is controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q727. Which configuration items affect authorization?

**Answer:** Any configuration affecting permissions, roles, authentication or SoD is controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q728. Which configuration items affect accreditation representation?

**Answer:** Accreditation configuration is controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q729. Which configuration items affect QC?

**Answer:** QC rules/limits/failure actions are controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q730. Which configuration items affect equipment enforcement?

**Answer:** Equipment requirements and blocking/warning eligibility rules are controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q731. Which configuration items affect numbering?

**Answer:** Business numbering rules are controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q732. Which configuration items affect workflows?

**Answer:** Workflow states, transitions and transition authorization are controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q733. Which configuration items require proposal and approval?

**Answer:** All configuration that can affect controlled laboratory behavior requires proposal and approval.

**Status:** CLOSED — RECONCILED BASELINE



### Q734. Which configuration items may be changed immediately by an authorized administrator?

**Answer:** Only genuinely non-controlled administrative settings may be changed immediately by an authorized administrator/user

**Status:** CLOSED — RECONCILED BASELINE



### Q735. What is the exact lifecycle of a configuration proposal?

**Answer:** Recommended lifecycle: DRAFT → SUBMITTED → UNDER_REVIEW → APPROVED → VERIFIED/READY → EFFECTIVE → SUPERSEDED/RETIRED; alternative outcomes: REJECTED, CANCELLED.

**Status:** CLOSED — RECONCILED BASELINE



### Q736. Can a proposal be edited after review starts?

**Answer:** A proposal may be edited until review formally begins. Once review begins, the submitted content is frozen. Further changes create a new proposal/revision.

**Status:** CLOSED — RECONCILED BASELINE



### Q737. Can a proposal be rejected and resubmitted?

**Answer:** Yes. Rejected proposals may be resubmitted as a new proposal referencing the prior proposal/reason.

**Status:** CLOSED — RECONCILED BASELINE



### Q738. Can proposals be cancelled?

**Answer:** Yes. Proposals can be cancelled before becoming effective, with reason and audit.

**Status:** CLOSED — RECONCILED BASELINE



### Q739. Who can approve a proposal?

**Answer:** Configuration approver is determined by configuration type; authority is deployment-configured. Technical/Quality/Business authority varies by domain.

**Status:** CLOSED — RECONCILED BASELINE



### Q740. Must proposer and approver be different users?

**Answer:** Yes for controlled changes. Proposer and approver must be different users.

**Status:** CLOSED — RECONCILED BASELINE



### Q741. What is the normal alternate-approver rule?

**Answer:** Primary approver unavailable → pre-designated competent alternate approver; no ad-hoc substitution.

**Status:** CLOSED — RECONCILED BASELINE



### Q742. What is the emergency configuration path?

**Answer:** Emergency: declare → authorize alternate → implement bounded change → verify → countersign/evidence → retrospective review.

**Status:** CLOSED — RECONCILED BASELINE



### Q743. What makes an emergency change valid?

**Answer:** Emergency is valid only where immediate action is necessary to protect data integrity, security, report correctness, laboratory operation or recoverability and normal approval cannot safely be completed in time.

**Status:** CLOSED — RECONCILED BASELINE



### Q744. What is the maximum emergency validity period?

**Answer:** A temporary emergency configuration or exception shall have a maximum validity of **24 hours**, unless a separately approved higher-level continuity/recovery procedure explicitly establishes a different controlled period.
The emergency record shall contain its activation time and automatic expiry time.
Emergency validity shall never convert a prohibited hard SoD relationship into an allowed one.

**Status:** CLOSED — RECONCILED BASELINE



### Q745. Does an emergency configuration automatically expire?

**Answer:** Yes. Emergency configuration shall have an explicit expiry timestamp and shall **automatically cease to be effective at expiry** unless it has been replaced by an independently approved normal configuration.
The system shall not silently extend an emergency configuration.
Expiry shall generate an auditable event, and an expired emergency configuration shall not affect subsequent controlled actions.

**Status:** CLOSED — RECONCILED BASELINE



### Q746. What happens if it is not retrospectively reviewed?

**Answer:** Failure to complete the required retrospective review shall create a controlled compliance/operations exception.
The emergency action shall remain historically recorded and shall not be erased or rewritten. The relevant Quality/Technical authority shall be notified/escalated, and subsequent use of the same emergency mechanism may be restricted until review is completed.
Retrospective review failure shall not invalidate previously legitimate business records automatically, but it shall remain an unresolved control deficiency requiring documented disposition.

**Status:** CLOSED — RECONCILED BASELINE



### Q747. How are emergency changes countersigned?

**Answer:** Countersigning is an explicit separate approval/acknowledgement event by the designated alternate/independent authority; it is not merely a comment.

**Status:** CLOSED — RECONCILED BASELINE



### Q748. What evidence proves the emergency change was visible to the required people?

**Answer:** System records named recipients, notification/event timestamp, acknowledgement/countersignature and policy/emergency ID.

**Status:** CLOSED — RECONCILED BASELINE



### Q749. How are emergency-use frequencies reported?

**Answer:** Automatic monthly emergency-use report, with trend indicators by user, rule, configuration type and reason.

**Status:** CLOSED — RECONCILED BASELINE



### Q750. Can an unapproved configuration ever be testable without affecting live behavior?

**Answer:** Material controlled configuration is versioned/effective-dated and retains proposer, approver, approval event, effective interval and capture point. Historical records must be able to reconstruct which configuration applied; later changes do not silently retarget in-progress/historical technical state.

**Status:** CLOSED — RECONCILED BASELINE



### Q751. Is a staging/draft environment required inside the application for configuration review?

**Answer:** A permanently separate staging environment inside the application is **not required for v1**.
The application shall nevertheless provide a controlled draft/review mechanism for configuration proposals where practical, so that unapproved configuration can be evaluated without affecting live behavior.
The approved production configuration shall remain isolated from draft/test configuration, and no unapproved configuration shall influence controlled laboratory operation.

**Status:** CLOSED — RECONCILED BASELINE



### Q752. How are approved configurations promoted to effective status?

**Answer:** Approved configuration shall become effective only through a controlled promotion/activation process.

The process shall include:
**Draft → Review → Approval → Verification/Ready → Effective**
with the applicable effective date/time recorded.

Activation shall create an auditable configuration event and shall use the exact approved configuration version.
Unapproved or superseded configuration shall not become effective through ordinary editing or deployment-side manipulation.

**Status:** CLOSED — RECONCILED BASELINE



### Q753. Must configuration changes be effective-dated?

**Answer:** Yes. Controlled configuration changes shall be effective-dated where their behavior or applicability can change over time.
Each version shall have a defined effective-from date/time and, where applicable, effective-to date/time.
The system shall prevent ambiguous overlapping effective configurations unless the approved configuration type explicitly permits scoped coexistence.
Historical work shall remain associated with the configuration applicable at the relevant point in time.

**Status:** CLOSED — RECONCILED BASELINE



### Q754. How are historical configurations reconstructed for old TestInstances?

**Answer:** Historical configuration for an old TestInstance shall be reconstructed using the configuration version applicable to the relevant date/time and any required explicit snapshot/reference captured by the TestInstance, Result, CalculationRun, or ReportRevision.
The system shall not rely solely on the current configuration.

The Configuration History and Capture Matrix shall define for each controlled configuration object whether historical reconstruction uses:
- effective-dated reference;
- immutable snapshot;
- or another explicitly approved capture mechanism.

The selected mechanism shall allow reconstruction even after later configuration versions become effective.

**Status:** CLOSED — RECONCILED BASELINE



### Q755. For MethodVersion, what is the business key for temporal uniqueness?

**Answer:** The MethodVersion business identity shall be:
**Method ID + controlled Version Designation**

For example, the stable Method may have version designations such as `2026.1`, `Rev-03`, or another approved laboratory convention.
Database uniqueness shall prevent two MethodVersions for the same Method from having the same version designation.
Temporal applicability is a separate concern from identity. Effective-from/effective-to information determines when a MethodVersion may be used; it does not redefine the MethodVersion's identity.

**Status:** CLOSED — RECONCILED BASELINE



### Q756. Can two MethodVersions for the same Method be effective simultaneously?

**Answer:** No. For a given Method and applicability context, **two MethodVersions shall not be effective simultaneously**.
The preferred temporal model uses non-overlapping validity intervals. A MethodVersion may end at the exact instant another begins.
Historical TestInstances remain linked to the MethodVersion actually used, so later replacement does not affect historical reconstruction.
If a genuine parallel technical regime is required for different matrices/disciplines or other applicability dimensions, those dimensions must be explicitly modeled rather than permitting ambiguous temporal overlap.

**Status:** CLOSED — RECONCILED BASELINE



### Q757. For Rate, can overlapping rates exist for the same scope?

**Answer:** Rate/CustomerRate are **out of v1**. There is no approved v1 pricing key because charge calculation is not implemented. A future commercial work package must define its business keys and temporal/snapshot rules before any charging schema is introduced.

**Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record / Database Contract



### Q758. For CustomerRate, can overlapping customer rates exist?

**Answer:** V1 has no rate selection or charge calculation. Future charging requires controlled commercial scope approval before implementation.

**Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record / Database Contract



### Q759. For UserRoleAssignment, can overlapping assignments exist?

**Answer:** UserRoleAssignments may overlap when they represent different valid roles/assignments. The same role assignment for the same user and scope must not overlap.

**Status:** CLOSED — RECONCILED BASELINE



### Q760. For AccreditationScope, can overlapping records exist?

**Answer:** Temporal governance applies to approved effective-dated technical/laboratory entities such as MethodVersion, TestDefinition versions, UserRoleAssignment and AccreditationScope. Rate/CustomerRate are excluded because charging is out of v1.

**Status:** CLOSED — RECONCILED BASELINE



### Q761. For each temporal entity, what defines the “current” record?

**Answer:** For every effective-dated entity, the “current” record shall be the record whose validity interval contains the evaluation instant.

The platform-wide temporal convention shall be:
**`effective_from <= evaluation_time < effective_to`**
where `effective_to = NULL` means no defined end.

The current record therefore must be determined from stored effective timestamps and applicable scope, not merely from a mutable `is_current` flag.
A cached/current flag may be used for performance only if it is derived and protected against divergence from the authoritative temporal data.

**Status:** CLOSED — RECONCILED BASELINE



### Q762. Can validity periods be open-ended?

**Answer:** Yes. Open-ended validity periods shall be supported.
An open-ended record shall use `effective_to = NULL` to mean that the record remains effective until explicitly superseded/ended.
There shall be at most one open-ended effective record for the same unique business scope where the entity's temporal rules prohibit overlap.

**Status:** CLOSED — RECONCILED BASELINE



### Q763. How is an end date/time represented?

**Answer:** An end date/time shall be represented as an **instant in UTC**, with NULL meaning open-ended.
The temporal model shall use timestamps rather than ambiguous local date strings when the entity represents an exact effective moment.
For user-facing screens, the timestamp shall be displayed in the laboratory's configured timezone, while the stored authoritative value remains UTC.

**Status:** CLOSED — RECONCILED BASELINE



### Q764. Can an effective period end exactly when another begins?

**Answer:** Yes. One effective period may end exactly when another begins.
With the platform convention `[effective_from, effective_to)`, the first record is effective up to but not including its end instant, while the second becomes effective at that exact instant.

Example:
`Version A: 2026-01-01 00:00 → 2026-07-01 00:00`
`Version B: 2026-07-01 00:00 → open`

There is no overlap and no gap.

**Status:** CLOSED — RECONCILED BASELINE



### Q765. Are boundary timestamps inclusive or exclusive?

**Answer:** Temporal boundaries shall use a consistent **start-inclusive, end-exclusive** convention:
**`[effective_from, effective_to)`**

Therefore:
* `effective_from` is inclusive;
* `effective_to` is exclusive;
* Adjacent records may share the same boundary instant;
* Two records cannot both be effective at the boundary;
* NULL `effective_to` represents open-ended validity.

This convention shall be frozen in the Temporal Governance Matrix and applied consistently across all effective-dated entities unless a documented domain-specific exception is approved.

**Status:** CLOSED — RECONCILED BASELINE



### Q766. How is time-zone handling defined for effective dates?

**Answer:** Effective timestamps shall be stored internally in **UTC**.
The laboratory's normal user/report display timezone shall be **Asia/Kolkata**, using the IANA identifier `Asia/Kolkata`.
Temporal comparisons and database rules shall operate on the UTC instant, not on displayed local time.
Date-only business values shall remain date-only and must not be converted into artificial timestamps merely to fit the temporal model.

**Status:** CLOSED — RECONCILED BASELINE



### Q767. Can a future record be entered in advance?

**Answer:** Yes. Future-dated records shall be allowed when the entity's governance rules permit them.
A future record may be prepared, reviewed, approved, and stored before its effective time, but it must not influence live behavior before that effective timestamp.
For high-impact configuration, future activation shall require the complete approved configuration lifecycle and an exact effective timestamp.

**Status:** CLOSED — RECONCILED BASELINE



### Q768. Can a past-dated record be inserted?

**Answer:** Past-dated records may be inserted **only through a controlled retrospective process**.
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

**Status:** CLOSED — RECONCILED BASELINE



### Q769. Can a past-dated change be made after newer records already exist?

**Answer:** Yes, a past-dated change may be made after newer records exist, but only through the same controlled retrospective-governance process.
The application shall recalculate the affected temporal intervals and identify impacted historical records, TestInstances, results, reports, permissions, or other dependent behavior.
The system must not silently rewrite history.
Where historical records were already finalized using the previous configuration, the retrospective change shall trigger an impact assessment and controlled corrective process rather than silently applying the new state retroactively.

**Status:** CLOSED — RECONCILED BASELINE



### Q770. What approval is required for retrospective temporal changes?

**Answer:** A retrospective temporal change shall require:
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

**Status:** CLOSED — RECONCILED BASELINE



### Q771. How are historical reconstructions protected from later temporal edits?

**Answer:** Historical reconstruction shall never depend solely on the current temporal configuration.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q772. Which business identifiers need dedicated sequences?

**Answer:** Business identifiers are allocated by the controlled numbering service at the authoritative creation event, inside the transaction that establishes the entity identity. Browser drafts do not consume business numbers; gaps are allowed and numbers are never reused.

**Status:** CLOSED — RECONCILED BASELINE



### Q773. Is there a sample number sequence?

**Answer:** Yes. Samples shall have a dedicated controlled Sample ID sequence.

Recommended baseline:
`SAM-00000001`

The exact prefix and width shall be frozen in the Numbering and Identifier Allocation Matrix.
Sample IDs shall be globally unique within the LabNexus deployment, never reused, and allocated through the authoritative sample-registration transaction.
A damaged label does not cause a new Sample ID to be issued; the same identifier may be reprinted after identity verification.

**Status:** CLOSED — RECONCILED BASELINE



### Q774. Is there a TestInstance number sequence?

**Answer:** Yes. TestInstances shall have a dedicated system-controlled TestInstance identifier/sequence.
A TestInstance represents a distinct execution occurrence and therefore needs an independently traceable identifier.
The identifier shall not be reused when a TestInstance is cancelled, rejected, failed, corrected, reworked, or otherwise terminated.
Repeat/retest/new-execution semantics remain separate from identifier allocation.

**Status:** CLOSED — RECONCILED BASELINE



### Q775. Is there a report number sequence?

**Answer:** Yes. Reports shall have a dedicated report-number sequence.

The Report Number identifies the logical report and shall remain distinct from:
* ReportRevision number;
* ResultRevision;
* PDF artifact identity.

Recommended human format is along the lines of:
`RPT-00012345`
with the exact prefix/width governed by the Numbering Matrix.

A revised/reissued report normally retains the same logical Report Number and receives a new ReportRevision.

**Status:** CLOSED — RECONCILED BASELINE



### Q776. Is there a customer/project/request number sequence?

**Answer:** Yes, where a controlled business identifier is needed, Customer, Project/Contract, and Request shall have **separate identifier namespaces**.

For example:
* Customer: `CUS-...`
* Project/Contract: `PRJ-...`
* Request: `REQ-...`

The precise prefixes and whether every entity receives a human-facing number shall be frozen before implementation.
Internal primary keys remain independent from these business identifiers.

**Status:** CLOSED — RECONCILED BASELINE



### Q777. Is there a document number sequence?

**Answer:** A controlled Document entity should have a dedicated logical document identifier where the laboratory needs human-facing document control.

For example:
`DOC-00012345`

DocumentVersion shall not receive an unrelated independent business identity; the Document ID identifies the logical document and its version designation identifies the controlled version.
Where a document is merely an internal attachment and does not require controlled-document numbering, an internal immutable ID may be sufficient.

**Status:** CLOSED — RECONCILED BASELINE



### Q778. Are sequences global or per discipline/site/year?

**Answer:** For the v1 single-laboratory deployment, sequences shall be **global within the deployment**, not separately reset by discipline, room, or site.
Different entity types have separate namespaces.
The system shall not reset a sequence annually merely for presentation convenience.
Future independent laboratory deployments shall have their own independent sequences because they are independent LIMS deployments.

**Status:** CLOSED — RECONCILED BASELINE



### Q779. Is year embedded in identifiers?

**Answer:** Year is not a mandatory component of core identifiers and does not reset the sequence. The year may be presented separately where required.

**Status:** CLOSED — RECONCILED BASELINE



### Q780. Is prefix embedded in identifiers?

**Answer:** Yes. Controlled human-facing identifiers should use an **approved stable prefix** to make the entity type immediately recognizable.

Examples:
`SAM-00000001`
`TI-00000001`
`RPT-00000001`
`REQ-00000001`

Prefixes are presentation/identifier-format controls, not substitutes for actual database type identity or foreign-key relationships.
Prefixes shall be versioned through controlled numbering configuration and must not be changed casually after production records exist.

**Status:** CLOSED — RECONCILED BASELINE



### Q781. Are sequence values zero-padded?

**Answer:** Yes. Sequence values should use **fixed zero-padding** according to the approved numbering format.
The exact width shall be established in the Numbering Matrix based on realistic expected capacity and future growth.

For example, an eight-digit sequence provides a format such as:
`SAM-00000001`

Zero-padding is presentation formatting; it does not change numeric ordering or uniqueness.

**Status:** CLOSED — RECONCILED BASELINE



### Q782. When is a number allocated: draft creation, registration, approval, or issue?

**Answer:** Numbers shall be allocated at the **business event that establishes the authoritative identity of the entity**, not merely when a temporary browser draft exists.

Recommended triggers:
* Sample ID: authoritative sample registration;
* TestInstance ID: authoritative TestInstance creation;
* Report Number: creation of the logical Report entity;
* Customer/Project/Request ID: authoritative creation of that business entity;
* Document Number: creation of the controlled logical Document where numbering is required.

The allocation event shall occur inside the transaction that establishes the entity identity.
Human/business identifiers shall not be allocated to unsaved browser drafts.

**Status:** CLOSED — RECONCILED BASELINE



### Q783. Are numbers allowed to be reserved and later abandoned?

**Answer:** Numbers may be allocated and subsequently abandoned because of cancellation, transaction failure, system recovery, or other controlled circumstances.
**Gaps are acceptable.**
A number that has been allocated shall never later be silently reused for a different record.
The system does not need to guarantee gapless numbering unless a separately approved external requirement explicitly requires it.

**Status:** CLOSED — RECONCILED BASELINE



### Q784. If a transaction rolls back after number allocation, is the gap acceptable?

**Answer:** Yes. If a transaction rolls back after number allocation, the gap is acceptable and the allocated number is never reused.

**Status:** CLOSED — RECONCILED BASELINE



### Q785. Can issued numbers ever be reused?

**Answer:** No. **Issued/allocated business identifiers shall never be reused.**

This applies even when a record is:
* Cancelled;
* Rejected;
* Withdrawn;
* Destroyed after retention;
* Created incorrectly;
* Superseded;
* Abandoned following a failed transaction after allocation.

The identifier remains part of historical traceability.

**Status:** CLOSED — RECONCILED BASELINE



### Q786. Can a sequence be changed after production records exist?

**Answer:** A numbering format or sequence configuration shall not be changed casually after production records exist.

A future controlled configuration change may alter presentation format or start a new sequence policy only after:
* Impact assessment;
* Approval;
* Effective date;
* Verification;
* Historical compatibility assessment;
* Preservation of the old numbering rule.

Existing identifiers shall never be renumbered.

**Status:** CLOSED — RECONCILED BASELINE



### Q787. Who can configure numbering?

**Answer:** Numbering configuration shall be managed by the **authorized configuration administration role**, but production activation shall require the approved configuration-governance process.
The person technically entering the configuration should not automatically be the sole authority approving the change.
Numbering configuration changes shall be auditable and versioned.

**Status:** CLOSED — RECONCILED BASELINE



### Q788. Must numbering configuration be controlled and approved?

**Answer:** Yes. Numbering configuration is controlled configuration and shall follow the same governance model:
**Propose → Review → Approve → Verify/Ready → Effective**

The exact format, prefix, width, allocation trigger, sequence behavior, and future effective date shall be preserved as configuration history.
Unapproved numbering configuration shall not affect live production identifiers.

**Status:** CLOSED — RECONCILED BASELINE



### Q789. How is concurrency handled for multiple writers?

**Answer:** Sequence allocation shall be concurrency-safe and transactional.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q790. What happens if the sequence reaches its configured limit?

**Answer:** When a sequence approaches or reaches its configured capacity, the system shall **stop unsafe allocation rather than wrap around or reuse identifiers**.

The controlled response shall be:
* Detect capacity before unsafe overflow;
* Block new allocation for that sequence;
* Raise an operational/configuration condition;
* Approve a controlled extension of sequence width/capacity or a new numbering policy;
* Preserve all historical identifiers;
* Verify the resulting configuration before activation.

The system shall never silently roll a sequence back to zero or begin reusing previous identifiers.

**Status:** CLOSED — RECONCILED BASELINE



### Q791. What is the root storage location on the Windows host?

**Answer:** Root storage location is deployment-configured. Recommend a dedicated local fixed-disk volume such as D:\LabNexus\.

**Status:** CLOSED — RECONCILED BASELINE



### Q792. Which folders store live documents?

**Answer:** Persisted controlled documents use an application-managed document store under the configured storage root.

**Status:** CLOSED — RECONCILED BASELINE



### Q793. Which folders store generated PDFs?

**Answer:** Generated issued PDFs are stored through the same controlled document system; a logical issued-reports area may be used operationally.

**Status:** CLOSED — RECONCILED BASELINE



### Q794. Which folders store attachments?

**Answer:** Attachments use the same controlled storage system, separated logically from generated reports.

**Status:** CLOSED — RECONCILED BASELINE



### Q795. Which folders store temporary files?

**Answer:** Temporary files go to a dedicated temp directory and are never treated as authoritative records.

**Status:** CLOSED — RECONCILED BASELINE



### Q796. Which folders store backups?

**Answer:** Backups go to locations outside the live-data root; preferably a separate physical volume/device.

**Status:** CLOSED — RECONCILED BASELINE



### Q797. Are backup folders on the same physical disk as the live database?

**Answer:** No. The authoritative backup must not be on the same physical disk as the live database.

**Status:** CLOSED — RECONCILED BASELINE



### Q798. Which backup destinations are local?

**Answer:** Recommended local backup = separate fixed physical disk or storage device.

**Status:** CLOSED — RECONCILED BASELINE



### Q799. Which backup destinations are removable/offline?

**Answer:** Recommended offline backup = removable encrypted HDD/SSD, rotated and physically disconnected when not in use.

**Status:** CLOSED — RECONCILED BASELINE



### Q800. Are network paths allowed only for backup copies?

**Answer:** Yes. Network paths may be used for backup copies only; never for the live SQLite database.

**Status:** CLOSED — RECONCILED BASELINE



### Q801. Which Windows accounts/services need filesystem access?

**Answer:** Dedicated Windows service identities: application service, backup service, and Caddy/reverse-proxy service as appropriate.

**Status:** CLOSED — RECONCILED BASELINE



### Q802. What NTFS permissions will protect the storage directories?

**Answer:** NTFS ACLs use least privilege: app service gets required DB/document access, Caddy gets only its required files, backup service gets read/write access necessary for backup, lab users get no direct storage access.

**Status:** CLOSED — RECONCILED BASELINE



### Q803. Who has administrative access to the host?

**Answer:** Host administrators are designated IT/System Administration personnel. Their OS privileges remain part of the trusted operational boundary.

**Status:** CLOSED — RECONCILED BASELINE



### Q804. How are filesystem permissions documented?

**Answer:** NTFS permissions must be documented as part of deployment/operations documentation and verified during deployment.

**Status:** CLOSED — RECONCILED BASELINE



### Q805. Can ordinary laboratory users access the storage directories directly?

**Answer:** No. Ordinary laboratory users never access document/database directories directly.

**Status:** CLOSED — RECONCILED BASELINE



### Q806. How are generated PDFs protected from direct modification?

**Answer:** Issued PDFs are protected through NTFS permissions, application-only access, controlled DocumentVersion records and hash verification.

**Status:** CLOSED — RECONCILED BASELINE



### Q807. Is file hashing required for documents and PDFs?

**Answer:** Yes. SHA-256 hash required for persisted controlled documents/PDFs.

**Status:** CLOSED — RECONCILED BASELINE



### Q808. How will hash verification be performed?

**Answer:** Hash verification compares stored SHA-256 against the actual file during integrity checks.

**Status:** CLOSED — RECONCILED BASELINE



### Q809. How are missing/corrupted files detected?

**Answer:** Periodic integrity checks and on-access checks for critical artifacts detect missing/corrupted files.

**Status:** CLOSED — RECONCILED BASELINE



### Q810. What happens if a file exists but its database record is missing?

**Answer:** Orphan file is quarantined/flagged; no automatic deletion. Investigation determines whether it is recoverable or erroneous.

**Status:** CLOSED — RECONCILED BASELINE



### Q811. What happens if a database record points to a missing file?

**Answer:** Database reference to missing file creates a storage-integrity incident; application marks artifact unavailable and initiates controlled recovery.

**Status:** CLOSED — RECONCILED BASELINE



### Q812. How are orphaned files detected?

**Answer:** Scheduled storage-integrity scan compares database-referenced artifacts with physical storage.

**Status:** CLOSED — RECONCILED BASELINE



### Q813. Who can repair storage inconsistencies?

**Answer:** Only authorized System Administrator/Operations authority may repair storage inconsistencies; repair itself is audited and evidenced.

---

# 29. SQLite Operational Requirements

**Status:** CLOSED — RECONCILED BASELINE



### Q814. What exact SQLite version will be used in production?

**Answer:** SQLite must be **at least 3.35** and the application shall refuse startup on an older runtime because required SQL behavior depends on it. Python and other runtime dependencies are pinned by the validated release baseline, and actual runtime versions are recorded in release/validation evidence.

**Status:** CLOSED — RECONCILED BASELINE



### Q815. What runtime/library version is approved?

**Answer:** Use the SQLite library shipped with/pinned to the approved Python runtime environment; record the exact SQLite library version at installation and in diagnostics.

**Status:** CLOSED — RECONCILED BASELINE



### Q816. What PRAGMA settings are mandatory at every connection?

**Answer:** Mandatory connection settings: PRAGMA foreign_keys=ON;, PRAGMA journal_mode=WAL;, PRAGMA synchronous=FULL;, PRAGMA busy_timeout=5000;. Other pragmas should be explicitly justified/tested.

**Status:** CLOSED — RECONCILED BASELINE



### Q817. How is foreign_keys=ON enforced and verified?

**Answer:** Application connection factory executes and verifies foreign_keys=ON on every connection.

**Status:** CLOSED — RECONCILED BASELINE



### Q818. How is WAL mode enforced and verified?

**Answer:** Database startup/health checks verify journal_mode=WAL.

**Status:** CLOSED — RECONCILED BASELINE



### Q819. What busy_timeout value is appropriate for the workload?

**Answer:** Recommend 5000 ms busy timeout initially.

**Status:** CLOSED — RECONCILED BASELINE



### Q820. What write transaction duration is considered acceptable?

**Answer:** Performance claims are measured acceptance criteria for defined workloads and environments, using objective percentile/upper-bound metrics and explicit inclusion of database commit/audit behavior. Any failed accepted target requires controlled technical investigation/ADR rather than silent relaxation.

**Status:** CLOSED — RECONCILED BASELINE



### Q821. What operations must never happen inside long transactions?

**Answer:** Never hold a write transaction across PDF rendering, filesystem I/O, network I/O, long calculations, user interaction, external processes, or lengthy batch processing.

**Status:** CLOSED — RECONCILED BASELINE



### Q822. What retry/backoff rules are required for SQLITE_BUSY or SQLITE_LOCKED?

**Answer:** Use bounded retry/backoff for transient SQLITE_BUSY/eligible lock-contention conditions, e.g. short exponential delays up to a few seconds; never blindly retry all database errors.

**Status:** CLOSED — RECONCILED BASELINE



### Q823. Which operations use read-only access where practical?

**Answer:** Use read-only/read-optimized connections/transactions where practical, but do not create a second database or bypass application integrity rules.

**Status:** CLOSED — RECONCILED BASELINE



### Q824. How are migrations executed safely with SQLite constraints?

**Answer:** SQLite migrations run in controlled maintenance/quiesce mode using Alembic and SQLite-safe migration patterns; protected tables/triggers must survive the migration.

**Status:** CLOSED — RECONCILED BASELINE



### Q825. How is database integrity checked before deployment?

**Answer:** Before deployment: backup → schema/version validation → integrity_check → foreign_key_check → migration preflight.

**Status:** CLOSED — RECONCILED BASELINE



### Q826. How is database integrity checked after backup?

**Answer:** After backup: validate backup opens successfully, run integrity checks and verify expected schema/version and critical record counts/metadata.

**Status:** CLOSED — RECONCILED BASELINE



### Q827. How is database integrity checked after restore?

**Answer:** After restore: integrity_check, foreign_key_check, schema/version check, application startup and smoke-test/recovery verification.

**Status:** CLOSED — RECONCILED BASELINE



### Q828. What is the policy for WAL files during backup?

**Answer:** Do not independently copy the live .db while treating the WAL as irrelevant. Use SQLite's Online Backup API or another SQLite-consistent backup mechanism that captures a coherent database snapshot.

**Status:** CLOSED — RECONCILED BASELINE



### Q829. How is database backup performed consistently while the application is live?

**Answer:** Preferred live backup = SQLite Online Backup API; documents/files are copied using controlled file-copy/hash procedure.

**Status:** CLOSED — RECONCILED BASELINE



### Q830. What is the approved quiesce method before backup or migration?

**Answer:** For migration: enter application maintenance mode → stop new work → drain active writes → stop application → perform migration → validate → restart.

**Status:** CLOSED — RECONCILED BASELINE



### Q831. Can backups run without stopping the application?

**Answer:** Yes, backups can run while the application remains live using the SQLite Online Backup API. SQLite documents this explicitly.

**Status:** CLOSED — RECONCILED BASELINE



### Q832. What happens if the database becomes locked unexpectedly?

**Answer:** Detect lock contention → bounded retry → user-friendly temporary-busy message if exhausted → log/monitor the event.

**Status:** CLOSED — RECONCILED BASELINE



### Q833. What is the operator procedure for database corruption?

**Answer:** Stop/quiesce → preserve original DB/WAL/SHM as evidence → assess integrity → restore last known-good validated backup → verify → investigate/recover missing transactions. Never experiment on the original corrupted database.

**Status:** CLOSED — RECONCILED BASELINE



### Q834. What is the approved maximum database size for v1 operations?

**Answer:** No hard absolute DB-size limit should be frozen now. Operational ceiling must come from workload testing. SQLite's theoretical limit is vastly beyond this application's needs and should not be treated as an operational target.

**Status:** CLOSED — RECONCILED BASELINE



### Q835. What monitoring will show database size/growth?

**Answer:** Monitor database file size, WAL size, free disk space, daily growth rate, backup duration and backup size.

**Status:** CLOSED — RECONCILED BASELINE



### Q836. When will archival/maintenance be required?

**Answer:** Maintenance/archival is triggered by measured operational thresholds, retention policy, backup/restore duration, disk capacity, query performance or integrity/operational requirements—not simply because a particular age was reached.

---

# 30. LAN, Windows, and Network Operation

**Status:** CLOSED — RECONCILED BASELINE



### Q837. What Windows edition/server version is the production target?

**Answer:** Production target: Windows 11 Pro on the laboratory's existing mini PC. Windows Server is not required for v1.

**Status:** CLOSED — RECONCILED BASELINE



### Q838. What Windows version is the development/test target?

**Answer:** Development/test target: Windows 11 Pro is the preferred reference environment for v1. Development may also occur on another supported Windows machine, provided the final build is validated on the production environment.

**Status:** CLOSED — RECONCILED BASELINE



### Q839. What host hardware will be used?

**Answer:** Host hardware: existing laboratory mini PC.

**Status:** CLOSED — RECONCILED BASELINE



### Q840. What CPU, RAM, and storage are available?

**Answer:** CPU: Intel Core i3-9100; RAM: 8 GB. Storage: to be recorded from the actual mini PC before deployment. Do not invent a storage capacity.

**Status:** CLOSED — RECONCILED BASELINE



### Q841. Is the host a dedicated machine?

**Answer:** The mini PC should be treated as the dedicated LabNexus production host. It performs the server role even though it is not server-class hardware.

**Status:** CLOSED — RECONCILED BASELINE



### Q842. Is the host also used for unrelated workloads?

**Answer:** No unrelated workloads should routinely run on the host. LabNexus should have priority on the machine.

**Status:** CLOSED — RECONCILED BASELINE



### Q843. What is the server hostname?

**Answer:** Deployment-specific hostname. The actual hostname is a laboratory infrastructure input and should not be hard-coded into LabNexus.

**Status:** CLOSED — RECONCILED BASELINE



### Q844. What is the static IP or DNS name?

**Answer:** Deployment-specific static IP or DNS name. Prefer a stable hostname with a static IP or DHCP reservation. Actual value remains a deployment input.

**Status:** CLOSED — RECONCILED BASELINE



### Q845. Is DNS available on the LAN?

**Answer:** LAN DNS availability is a deployment input. If laboratory DNS is available, use it; otherwise stable local hostname/IP resolution must be provided by the deployment.

**Status:** CLOSED — RECONCILED BASELINE



### Q846. What URL should users open?

**Answer:** Deployment-specific HTTPS URL, for example https://lims.<laboratory-internal-domain>. The actual URL must be configurable.

**Status:** CLOSED — RECONCILED BASELINE



### Q847. Is HTTPS mandatory on the LAN?

**Answer:** Yes. HTTPS is mandatory even on the laboratory LAN.

**Status:** CLOSED — RECONCILED BASELINE



### Q848. How will the local TLS certificate be created and renewed offline?

**Answer:** Use a local/private CA or Caddy's controlled internal CA for the deployment. Certificate issuance/renewal must work without Internet access and must be documented.

**Status:** CLOSED — RECONCILED BASELINE



### Q849. Is an internal CA available?

**Answer:** Deployment input: determine whether the laboratory already has an internal CA. If not, the v1 deployment may use a controlled LabNexus/Caddy local CA arrangement.

**Status:** CLOSED — RECONCILED BASELINE



### Q850. How are client machines trusted?

**Answer:** Client machines must trust the CA that issued the LabNexus certificate. Trust should be established through the laboratory's controlled Windows trust mechanism; users should not be instructed to bypass certificate warnings.

**Status:** CLOSED — RECONCILED BASELINE



### Q851. Is the application accessible only on the laboratory LAN?

**Answer:** Yes. V1 is LAN-only. LabNexus shall not be publicly accessible.

**Status:** CLOSED — RECONCILED BASELINE



### Q852. Is remote access required?

**Answer:** No remote access is required for v1.

**Status:** CLOSED — RECONCILED BASELINE



### Q853. If remote access is required, what approved secure mechanism will be used?

**Answer:** Not applicable for v1. Any future remote access shall use an approved VPN-based mechanism; direct Internet exposure is prohibited.

**Status:** CLOSED — RECONCILED BASELINE



### Q854. Is Internet access blocked from the server?

**Answer:** Core LabNexus does not require Internet access. Routine outbound Internet access from the production host should be blocked or otherwise restricted according to laboratory policy.

**Status:** CLOSED — RECONCILED BASELINE



### Q855. Must core application functions continue when Internet connectivity is absent?

**Answer:** Yes. Core application functions must continue normally when Internet connectivity is absent.

**Status:** CLOSED — RECONCILED BASELINE



### Q856. Which features, if any, may degrade without Internet?

**Answer:** Only explicitly optional external functions may degrade, such as future email delivery, external integrations, or update-related functions. Core sample/test/result/review/verification/approval/reporting operations shall not depend on Internet access.

**Status:** CLOSED — RECONCILED BASELINE



### Q857. Are email, external APIs, remote licensing, or update checks allowed?

**Answer:** External Internet-dependent services are not required for v1. Email, external APIs, remote licensing, and online update checks must not be dependencies for core operation.

**Status:** CLOSED — RECONCILED BASELINE



### Q858. Are automatic software updates allowed on the host?

**Answer:** No automatic LabNexus software updates. Releases shall be deliberately installed through a controlled maintenance/release process.

**Status:** CLOSED — RECONCILED BASELINE



### Q859. How are OS updates scheduled?

**Answer:** OS updates shall be applied during planned maintenance windows, after compatibility/risk review and with an appropriate backup/recovery point.

**Status:** CLOSED — RECONCILED BASELINE



### Q860. How are application updates scheduled?

**Answer:** Application updates shall use a controlled release process: validated build → backup → maintenance window → installation/migration → verification → rollback/recovery procedure if required.

**Status:** CLOSED — RECONCILED BASELINE



### Q861. How are Chromium updates controlled so PDF rendering remains stable?

**Answer:** Chromium used for PDF rendering shall be pinned to a validated version/build. Updates occur only through a controlled LabNexus release process with PDF regression testing.

**Status:** CLOSED — RECONCILED BASELINE



### Q862. How are browsers on client PCs supported?

**Answer:** Client PCs shall use supported, maintained browsers and need not match the production host hardware.

**Status:** CLOSED — RECONCILED BASELINE



### Q863. What browsers are officially supported?

**Answer:** The supported browser baseline is current stable **Microsoft Edge and Google Chrome**, with actual validated versions recorded for each release. Firefox is not a v1 target unless separately validated and approved.

### Q864. What happens if a user loses LAN connectivity during a transaction?

**Answer:** If LAN connectivity is lost during a transaction, the server-side transaction shall either commit completely or roll back; partial database writes must not occur. The client must clearly indicate that the operation's final status is uncertain until confirmed. Critical commands should use idempotency/command identifiers where retry could otherwise duplicate an action.

**Status:** CLOSED — RECONCILED BASELINE



### Q865. What should users see when the application is unreachable?

**Answer:** When the application is unreachable, users should see a clear operational error/status page, not a raw server traceback. It should indicate that LabNexus cannot currently be reached and advise the user to check LAN connectivity or contact the responsible administrator.

---

# 31. Deployment and Release Management

**Status:** CLOSED — RECONCILED BASELINE



### Q866. What is the approved production installation method?

**Answer:** Approved production installation method: controlled installation from a versioned LabNexus release bundle containing application build, dependency manifest, migration package, configuration template, release notes, checksums, and deployment instructions/scripts. No ad-hoc file copying or direct source-code deployment.

**Status:** CLOSED — RECONCILED BASELINE



### Q867. Is there a development environment separate from validation/UAT?

**Answer:** Yes. Development must be separate from validation/UAT. Development changes must not be tested directly against production.

**Status:** CLOSED — RECONCILED BASELINE



### Q868. Is there a staging environment?

**Answer:** A permanently separate staging environment is not required for v1. The validation/UAT environment will serve as the controlled pre-production environment.

**Status:** CLOSED — RECONCILED BASELINE



### Q869. Is a validation environment required?

**Answer:** Yes. A validation environment is required before production release.

**Status:** CLOSED — RECONCILED BASELINE



### Q870. Where will each environment run?

**Answer:** Development: developer machine(s). Validation/UAT: separate Windows machine/environment from production where practical. Production: laboratory's dedicated mini PC.

**Status:** CLOSED — RECONCILED BASELINE



### Q871. How is configuration kept separate between environments?

**Answer:** Environment configuration must be separate. Each environment has its own database, file/document root, configuration, certificates, and environment-specific settings. Production configuration must never be copied into development/test.

**Status:** CLOSED — RECONCILED BASELINE



### Q872. How are secrets stored per environment?

**Answer:** Secrets must be stored separately per environment and never committed to source control. Production secrets shall be protected by OS-level access controls and encrypted/protected storage.

**Status:** CLOSED — RECONCILED BASELINE



### Q873. Who can deploy to each environment?

**Answer:** Developers may deploy to development. Authorized technical/project personnel may deploy to validation. Production deployment is restricted to the designated LIMS System Administrator/deployment authority.

**Status:** CLOSED — RECONCILED BASELINE



### Q874. Who can approve production deployment?

**Answer:** Production deployment requires approval by the designated Project/Laboratory authority after validation evidence is complete. The person who executes deployment should not be the sole approver of that deployment.

**Status:** CLOSED — RECONCILED BASELINE



### Q875. What exact pre-deployment checks are mandatory?

**Answer:** Mandatory checks: approved release version; validation/UAT passed; release checksum verified; production backup completed and validated; sufficient disk space; maintenance window confirmed; active writes stopped; migration package verified; rollback/recovery path available; deployment evidence record opened.

**Status:** CLOSED — RECONCILED BASELINE



### Q876. What exact backup must be created before migration?

**Answer:** Before any database migration, create a validated pre-deployment recovery set containing the SQLite database, associated documents/attachments, controlled configuration, and deployment manifest/metadata.

**Status:** CLOSED — RECONCILED BASELINE



### Q877. How is the backup validated before proceeding?

**Answer:** Validate the backup by opening the backup copy, running SQLite integrity checks and foreign-key checks, confirming schema/version metadata, expected record counts/metadata, verifying document hashes, and confirming the recovery-set manifest.

**Status:** CLOSED — RECONCILED BASELINE



### Q878. What does “stop/quiesce” mean operationally?

**Answer:** “Stop/quiesce” means: stop creation of new writes; prevent new transactions from starting; allow already-running requests to finish; confirm no active write operations remain; place application into maintenance mode; then stop application services before migration.

**Status:** CLOSED — RECONCILED BASELINE



### Q879. How is active user activity checked before migration?

**Answer:** Active activity shall be checked through application session/activity status plus confirmation that no write transaction is in progress. New writes must be blocked before the final migration step.

**Status:** CLOSED — RECONCILED BASELINE



### Q880. How is Alembic migration executed in production?

**Answer:** Alembic production migration shall run only during the approved maintenance window, against the validated production database, using the exact release's pinned environment and migration revision. Migration logs must be captured.

**Status:** CLOSED — RECONCILED BASELINE



### Q881. What happens if migration fails halfway?

**Answer:** If migration fails: stop immediately, preserve the original database/WAL/SHM and logs, do not continue blindly, declare deployment failure, and recover using the approved rollback mechanism.

**Status:** CLOSED — RECONCILED BASELINE



### Q882. Is the database restored from backup or migrated back through downgrade?

**Answer:** Production recovery shall use the pre-migration validated backup/recovery set, not an attempted downgrade of a partially migrated production database.

**Status:** CLOSED — RECONCILED BASELINE



### Q883. Which rollback mechanism is actually approved?

**Answer:** Approved production rollback mechanism = restore the validated pre-deployment recovery set. Alembic downgrade is not the primary production rollback mechanism.

**Status:** CLOSED — RECONCILED BASELINE



### Q884. Are Alembic downgrades maintained/tested for all migrations?

**Answer:** Alembic downgrades should be maintained and tested where technically safe and useful, but they are not relied upon for production recovery.

**Status:** CLOSED — RECONCILED BASELINE



### Q885. What is the failed-upgrade recovery procedure?

**Answer:** Failed-upgrade recovery: stop services → preserve failed state/evidence → confirm failure → restore pre-deployment database/documents/configuration as applicable → validate restored state → deploy known-good release → smoke test → record incident/deployment failure.

**Status:** CLOSED — RECONCILED BASELINE



### Q886. What smoke tests are mandatory after deployment?

**Answer:** Mandatory post-deployment smoke tests: service starts; HTTPS access works; login works; database connectivity works; schema revision matches release; role enforcement works; sample/test/report retrieval works; document access works; PDF generation works; audit/event recording works; backup subsystem is operational.

**Status:** CLOSED — RECONCILED BASELINE



### Q887. What does “resume” mean after deployment?

**Answer:** “Resume” means maintenance mode is removed, normal user access is restored, smoke tests have passed, monitoring is normal, and users are formally informed that production use may continue.

**Status:** CLOSED — RECONCILED BASELINE



### Q888. Who records deployment evidence?

**Answer:** The System Administrator/deployment executor records deployment evidence. The designated approver/reviewer verifies completeness.

**Status:** CLOSED — RECONCILED BASELINE



### Q889. What exact evidence is retained per release?

**Answer:** Retain: release ID; package checksum; date/time; host/environment; operator; approver; pre-check results; backup ID/hash; migration revision and logs; smoke-test results; final status; rollback details if applicable; incidents/deviations.

**Status:** CLOSED — RECONCILED BASELINE



### Q890. How are release versions identified?

**Answer:** Release versions should use a stable semantic version such as MAJOR.MINOR.PATCH, with an optional build identifier. Example: 1.0.0.

**Status:** CLOSED — RECONCILED BASELINE



### Q891. How are deployed software version and database schema version linked?

**Answer:** Each deployment record shall capture LabNexus application release version + exact Alembic schema revision. The release manifest explicitly links the two.

**Status:** CLOSED — RECONCILED BASELINE



### Q892. How are release notes stored?

**Answer:** Release notes shall be stored as controlled repository documentation under a versioned release record and included with the release bundle.

**Status:** CLOSED — RECONCILED BASELINE



### Q893. How are failed releases marked?

**Answer:** A failed release is recorded explicitly as FAILED, linked to its deployment/evidence record and any incident/corrective action. It must never be silently overwritten as successful.

**Status:** CLOSED — RECONCILED BASELINE



### Q894. How is production deployment prevented if validation evidence is incomplete?

**Answer:** Production deployment shall be blocked by the deployment checklist/process when mandatory validation evidence, backup validation, approval, or required preconditions are incomplete.

---

# 32. Backup and Recovery

**Status:** CLOSED — RECONCILED BASELINE



### Q895. What is the target Recovery Point Objective (RPO)?

**Answer:** A Recovery Set is a coherent logical recovery point containing the database and the required linked document/configuration evidence, integrity manifest, consistency marker and release/schema identity. It is controlled evidence, not an ad-hoc file copy.

**Status:** CLOSED — RECONCILED BASELINE



### Q896. What is the target Recovery Time Objective (RTO)?

**Answer:** The v1 Recovery Time Objective shall be established as:

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

**Status:** CLOSED — RECONCILED BASELINE



### Q897. How frequently must the database be backed up?

**Answer:** The recommended v1 backup schedule is:
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

**Status:** CLOSED — RECONCILED BASELINE



### Q898. How frequently must documents/attachments be backed up?

**Answer:** Documents and attachments shall be backed up on a schedule that is **no less protective than the database backup strategy**.
The preferred v1 approach is to include changed/new controlled documents and attachments in the recovery sets generated at least every **4 hours**, with a complete backup cycle at least daily.
Document backup shall not rely only on periodic manual copying because that can produce a database/document mismatch.
A recovery point must therefore be capable of identifying the corresponding database and document state.

**Status:** CLOSED — RECONCILED BASELINE



### Q899. Must database and document backups be consistent to the same point in time?

**Answer:** Yes. Database and document backups shall be **coherent to the same recovery point** to the extent required for reliable reconstruction.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q900. How many backup copies are retained?

**Answer:** The recovery design supports tiered copies: a separate physical-disk local copy, an encrypted offline copy and off-site rotation. Exact media identities and deployment custody details are recorded as operational evidence.

**Status:** CLOSED — RECONCILED BASELINE



### Q901. What is the retention period for backups?

**Answer:** Use a two-tier operational policy:
* **Daily/rolling Recovery Sets:** retain for at least **30 days**.
* **Monthly Recovery Sets:** retain for at least **12 months**.

Longer retention may be applied where required by the laboratory's approved recovery, legal, quality, or business policy.
Backup retention is distinct from the **10-year controlled laboratory-record retention requirement**. Backup copies are recovery media and do not replace preservation of the authoritative laboratory record.

**Status:** CLOSED — RECONCILED BASELINE



### Q902. How many removable/offline backup copies are maintained?

**Answer:** Maintain **at least 2 rotating removable/offline Recovery Set copies**.
The copies shall be rotated so that at least one is available as a controlled recovery source while another can remain physically separate from the production host.
Where practical, one copy should be stored at a physically separate approved location.

**Status:** CLOSED — RECONCILED BASELINE



### Q903. Where are offline backups physically stored?

**Answer:** Offline backup media shall be stored in a **restricted, controlled location physically separate from the LIMS host**, protected against unauthorized access, environmental damage, and casual loss.
At least one rotated offline copy should, where practical, be maintained at a **physically separate approved location** from the production host.
The exact storage location shall be documented in the backup custody record and shall not be exposed to ordinary LIMS users.

**Status:** CLOSED — RECONCILED BASELINE



### Q904. Who controls offline backup media?

**Answer:** Offline backup media shall be controlled by the designated **System Administrator / Backup Operations authority**, with laboratory management/Quality oversight.

Media movement shall be documented sufficiently to establish:
* media identity;
* Recovery Set identity;
* date/time;
* person releasing/receiving custody;
* storage location;
* integrity/validation status;
* return or disposal status.

Ordinary laboratory users shall not have unrestricted physical or technical control of backup media.

**Status:** CLOSED — RECONCILED BASELINE



### Q905. How is backup media labelled?

**Answer:** Each removable/offline backup medium shall have a unique controlled identifier and shall be associated with:
* Recovery Set identifier;
* backup date/time;
* media sequence/rotation identifier;
* retention/destruction date where applicable;
* encryption status;
* validation status.

Labels shall avoid exposing unnecessary sensitive laboratory information.
The authoritative detailed metadata shall also exist in the controlled backup record; the physical label alone shall not be the complete record.

**Status:** CLOSED — RECONCILED BASELINE



### Q906. How is backup media integrity checked?

**Answer:** Backup integrity shall be verified using a combination of:
* controlled backup manifest;
* cryptographic hashes for backed-up files/artifacts where applicable;
* SQLite/database integrity validation;
* successful readability/access checks;
* Recovery Set completeness checks;
* periodic actual restore testing.

A backup shall not be classified as **Restorable** merely because a file was successfully copied.
The controlled states remain distinct: Backup Created → Validated → Restorable → Restore Tested → Recovery Procedure Verified.

**Status:** CLOSED — RECONCILED BASELINE



### Q907. Are backups encrypted?

**Answer:** Yes. Removable/offline backups containing laboratory records, reports, customer information, or other controlled data shall be **encrypted using an approved encryption mechanism**.
Encryption shall apply to the backup medium or protected backup container rather than relying solely on Windows filesystem permissions.
Encryption is an additional protection layer and does not replace physical custody controls, integrity verification, or restore testing.

**Status:** CLOSED — RECONCILED BASELINE



### Q908. If yes, where are encryption keys stored?

**Answer:** The tiered recovery baseline targets **RPO ≤4 hours** for the separate-disk local copy, **RPO ≤24 hours** for the encrypted offline copy, with off-site rotation covering site-loss scenarios.

**Status:** CLOSED — RECONCILED BASELINE



### Q909. Who may restore a backup?

**Answer:** Only authorized **System Administrators or explicitly designated recovery personnel** may execute production backup restoration.
Laboratory Analysts, Reviewers, Verifiers, Approvers, and ordinary application administrators shall not have restore authority.

Restore authorization shall be separate from ordinary laboratory technical authority and shall require:
* Controlled recovery reason;
* Identified recovery set;
* Authorization;
* Pre-restore backup/safety point where applicable;
* Restore execution evidence;
* Post-restore verification.

A restore operation shall never be used as an ordinary record-correction mechanism.

**Status:** CLOSED — RECONCILED BASELINE



### Q910. Who may inspect backup contents?

**Answer:** Backup contents may be inspected only by authorized personnel whose duties require such access.

Access shall be separated into:
* **Operational/recovery inspection:** System Administrator/recovery personnel;
* **Technical/quality verification:** authorized Quality/Technical personnel where needed;
* **Sensitive-content inspection:** limited to personnel with the appropriate record confidentiality authorization.

Backup inspection must not become an uncontrolled route to bypass LabNexus RBAC.
All access to sensitive backup contents should be treated as privileged activity, with access/download auditing where technically appropriate.

**Status:** CLOSED — RECONCILED BASELINE



### Q911. What exactly is included in a backup?

**Answer:** A complete v1 Recovery Set shall include, as applicable:
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

**Status:** CLOSED — RECONCILED BASELINE



### Q912. What is excluded from backups?

**Answer:** The following should normally be excluded from the authoritative business backup unless separately required:
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

**Status:** CLOSED — RECONCILED BASELINE



### Q913. Are application binaries backed up or reproducibly redeployed?

**Answer:** Production software shall be **reproducibly redeployed from controlled release artifacts**, with an additional ability to retain the exact production release package where operationally appropriate.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q914. Are configuration files backed up?

**Answer:** Yes. Production configuration required to recreate the validated environment shall be backed up or otherwise recoverably recorded.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q915. Are TLS certificates/keys backed up?

**Answer:** Yes, the recovery process shall preserve the ability to recover required **TLS certificates and private keys**, but secret/private-key material shall be handled separately from ordinary data backups.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q916. Are secrets backed up?

**Answer:** Secrets shall **not be treated as ordinary database/application backups**.

The recovery design shall instead maintain a protected secret-recovery mechanism for:
* Application/session secret material;
* Backup-encryption keys where used;
* TLS private keys;
* Service credentials where required;
* Approved external credentials where applicable.

Secrets may be backed up or escrowed only in an approved protected form and separately from ordinary business-data backups.
The recovery procedure must establish that a host-loss recovery can obtain the necessary secrets without exposing them to ordinary users.

**Status:** CLOSED — RECONCILED BASELINE



### Q917. How are secrets recovered after host loss?

**Answer:** After host loss, secrets shall be recovered through a **controlled offline secret-recovery procedure**.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q918. How is a backup marked “validated”?

**Answer:** A backup shall be marked **Validated** only after successful non-destructive integrity checks appropriate to its contents.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q919. How is a backup marked “restorable”?

**Answer:** A backup shall be marked **Restorable** only after the organization has demonstrated that the backup can actually be used to construct a functioning recovery environment.
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

**Status:** CLOSED — RECONCILED BASELINE



### Q920. What test proves a restore is successful?

**Answer:** A restore shall be considered successful only when the restored environment passes a defined **Recovery Verification Test**.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q921. How often must restore testing occur?

**Answer:** Restore validation covers the complete Recovery Set: database integrity/foreign keys, linked document hashes, configuration/release identity, expected metadata/counts, application startup and representative transactions. The baseline uses quarterly restore testing; exact operational scheduling remains controlled and evidenced.

**Status:** CLOSED — RECONCILED BASELINE



### Q922. Must restore testing use production-like hardware?

**Answer:** Restore testing shall use hardware that is **representative of the production recovery environment**, but does not have to be literally identical to production hardware.

The test environment shall be sufficiently representative of:
* CPU/memory/storage characteristics relevant to recovery;
* Windows version;
* SQLite/application runtime;
* document storage structure;
* Chromium/reporting environment;
* network/LAN configuration where relevant.

The laboratory shall record material differences between the test and production recovery environment and assess whether they could invalidate the recovery evidence.

**Status:** CLOSED — RECONCILED BASELINE



### Q923. What constitutes “Recovery Procedure Verified”?

**Answer:** `Recovery Procedure Verified` shall mean that the **documented recovery procedure has actually been executed successfully** using a controlled Recovery Set and has produced an operational environment meeting the approved recovery acceptance criteria.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q924. What evidence is kept from restore tests?

**Answer:** Restore-test evidence shall include:
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

**Status:** CLOSED — RECONCILED BASELINE



### Q925. What happens if restore testing fails?

**Answer:** A failed restore test shall immediately trigger a **recovery deficiency**.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q926. How are backup failures alerted to operators?

**Answer:** Backup failures shall produce an **in-application operational alert** and an audit/evidence record.
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

**Status:** CLOSED — RECONCILED BASELINE



### Q927. Who reviews backup status?

**Answer:** Backup status shall be reviewed by the **designated System Administrator/Backup Operations role**, with Laboratory Quality/Management visibility for material recovery deficiencies.

The operational dashboard should expose at least:
* Last successful backup;
* Last validated backup;
* Last restorable/tested backup;
* Backup age;
* Failed/missed backups;
* Recovery-set status;
* Storage warnings.

Periodic review evidence should be retained according to the laboratory's operational/QMS requirements.

**Status:** CLOSED — RECONCILED BASELINE



### Q928. How is a missed backup handled?

**Answer:** A missed backup shall trigger an operational exception.

The system shall:
1. Detect the missed schedule where monitoring is available;
2. Record the failure/miss;
3. Identify the last successful validated backup;
4. Attempt the next controlled backup;
5. Assess current RPO exposure;
6. Escalate when the approved RPO threshold is threatened or exceeded;
7. Record corrective action.

A missed backup must not be silently treated as successful simply because a previous backup exists.

**Status:** CLOSED — RECONCILED BASELINE



### Q929. How is backup corruption detected?

**Answer:** Backup corruption shall be detected through multiple controls:
* Cryptographic hash/checksum verification;
* Backup-manifest/control-total validation;
* Database integrity checks;
* File readability checks;
* Periodic restore testing;
* Storage/media health checks where available.

A backup that passes file-level hashing but fails actual database/document restore shall be considered **not restorable**.
Restore testing therefore provides the strongest practical evidence that backups are usable.

**Status:** CLOSED — RECONCILED BASELINE



### Q930. How is a disaster involving total host loss handled?

**Answer:** Total host loss shall be handled through the controlled **disaster recovery procedure**.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q931. How is a disaster involving only database corruption handled?

**Answer:** Database-only corruption shall use a controlled database-recovery path:
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

**Status:** CLOSED — RECONCILED BASELINE



### Q932. How is a disaster involving missing documents handled?

**Answer:** Missing documents shall be treated as an **artifact-integrity/recovery incident**, not as a reason to regenerate historical PDFs from current mutable data.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q933. How is simultaneous database-and-document restore validated?

**Answer:** Simultaneous database-and-document restore shall be validated as a **single coherent recovery scenario**.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q934. What system health information must be visible to administrators?

**Answer:** Administrators need visibility of: service status, application version, DB/schema version, DB health, document-store health, free disk space, backup freshness/status, failed jobs, PDF failures, certificate expiry, active maintenance state, and recent critical errors.

**Status:** CLOSED — RECONCILED BASELINE



### Q935. Must the application expose a health check endpoint?

**Answer:** Yes. LabNexus shall expose an internal health-check endpoint.

**Status:** CLOSED — RECONCILED BASELINE



### Q936. Must the health check verify database connectivity?

**Answer:** Yes. Health check must verify database connectivity and required DB state.

**Status:** CLOSED — RECONCILED BASELINE



### Q937. Must the health check verify document storage access?

**Answer:** Yes. It must verify required document storage is accessible and writable where appropriate.

**Status:** CLOSED — RECONCILED BASELINE



### Q938. Must the health check verify report rendering availability?

**Answer:** Yes. It must verify the report/PDF rendering subsystem is available.

**Status:** CLOSED — RECONCILED BASELINE



### Q939. Must the health check verify backup subsystem status?

**Answer:** Yes. It must report backup subsystem status/freshness and most recent backup result.

**Status:** CLOSED — RECONCILED BASELINE



### Q940. What warnings should be shown to operators?

**Answer:** Warnings should include stale/failed backup, low disk space, document-store failure, DB/storage problem, failed PDF generation, failed scheduled job, certificate expiry approaching, unexpected service state, maintenance mode, and integrity/recovery-test failure.

**Status:** CLOSED — RECONCILED BASELINE



### Q941. How are low-disk-space conditions detected?

**Answer:** Low disk space detected by periodic health checks/service monitoring on all relevant volumes.

**Status:** CLOSED — RECONCILED BASELINE



### Q942. What threshold should trigger a warning?

**Answer:** Disk-space controls warn below the **smaller of 20% or 20 GiB**, block risky writes below the **smaller of 10% or 10 GiB**, and alert when projected time-to-full is below 30 days.

**Status:** CLOSED — RECONCILED BASELINE



### Q943. What threshold should block risky operations?

**Answer:** The same disk thresholds are part of production health and recovery preconditions; low disk space must not silently compromise risky writes or coherent Recovery Set creation.

**Status:** CLOSED — RECONCILED BASELINE



### Q944. How is database growth monitored?

**Answer:** Monitor DB size and growth rate at least daily; retain historical size measurements sufficient to identify abnormal growth.

**Status:** CLOSED — RECONCILED BASELINE



### Q945. How are document storage growth and capacity monitored?

**Answer:** Monitor document storage size/free space and growth rate at least daily.

**Status:** CLOSED — RECONCILED BASELINE



### Q946. How are failed PDF generations monitored?

**Answer:** Failed PDF generation recorded as a structured operational error containing relevant Report/Revision identifiers, error category, time, and retry status.

**Status:** CLOSED — RECONCILED BASELINE



### Q947. How are failed background/maintenance jobs recorded, if any?

**Answer:** Any scheduled/background job failure must create a structured operational event with job name, timestamp, status, error category, and retry/result.

**Status:** CLOSED — RECONCILED BASELINE



### Q948. Are scheduled tasks required?

**Answer:** Yes. Scheduled tasks are required for backups, health checks, cleanup/retention tasks where applicable, and other controlled maintenance operations.

**Status:** CLOSED — RECONCILED BASELINE



### Q949. Which operational tasks are automated versus manual?

**Answer:** Automated: backups, routine integrity checks, health checks, disk monitoring, job monitoring. Manual/authorized: restore, production release, migration approval, configuration approval, incident recovery, controlled archival.

**Status:** CLOSED — RECONCILED BASELINE



### Q950. What logs are retained?

**Answer:** Retain application operational logs, security/authentication logs, error logs, service/deployment logs, backup/restore logs, and scheduled-job logs. Controlled technical audit history remains in the application database.

**Status:** CLOSED — RECONCILED BASELINE



### Q951. Who can access application logs?

**Answer:** Application logs accessible primarily to System Administrators; authorized quality/technical personnel may receive read access where needed for investigation.

**Status:** CLOSED — RECONCILED BASELINE



### Q952. Do logs contain sensitive information?

**Answer:** Logs must be treated as potentially sensitive because they may contain identifiers and operational context. They should not contain unnecessary test-result or customer data.

**Status:** CLOSED — RECONCILED BASELINE



### Q953. How is sensitive information prevented from entering logs?

**Answer:** Structured logging with an allow-list of safe fields; never log passwords, tokens, session identifiers, secrets, private keys, or full sensitive request payloads.

**Status:** CLOSED — RECONCILED BASELINE



### Q954. How are log files rotated?

**Answer:** Logs shall rotate automatically by date and/or size, with bounded retention so the host cannot fill its disk from logs.

**Status:** CLOSED — RECONCILED BASELINE



### Q955. What is the retention period for operational logs?

**Answer:** Operational logs must remain sufficient to reconstruct backup, restore, deployment and integrity-check activity. The retention period for this log class follows the approved records/retention matrix rather than an unapproved hard-coded assumption.

**Status:** CLOSED — RECONCILED BASELINE



### Q956. Is centralized monitoring intentionally out of scope?

**Answer:** Yes. Centralized enterprise monitoring is intentionally out of scope for v1.

**Status:** CLOSED — RECONCILED BASELINE



### Q957. What is the minimal operator dashboard needed for v1?

**Answer:** Minimal v1 administrator dashboard: service/health status; DB health; disk; document storage; last successful/validated backup; backup age; failed jobs/PDFs; certificate status; application/schema version; maintenance/recovery warnings.

---

# 34. Error Handling and User-Facing Failure Rules

**Status:** CLOSED — RECONCILED BASELINE



### Q958. What errors must be shown to users as friendly messages?

**Answer:** Friendly messages required for validation failures, business-rule failures, authorization/SoD blocks, workflow errors, duplicate identifiers, stale data, concurrency conflicts, storage failures, report failures, unavailable service, and interrupted operations.

**Status:** CLOSED — RECONCILED BASELINE



### Q959. Which technical details must never be shown?

**Answer:** Never expose raw stack traces, SQL statements, internal exception details, secrets, tokens, server filesystem paths, or sensitive debugging information to normal users.

**Status:** CLOSED — RECONCILED BASELINE



### Q960. How are database constraint errors translated into useful user messages?

**Answer:** Database constraint errors shall be translated into domain-specific messages such as “Sample ID already exists” or “This action cannot be completed because the referenced record is no longer available.” Technical error details are logged internally.

**Status:** CLOSED — RECONCILED BASELINE



### Q961. How are authorization failures shown?

**Answer:** Show a generic authorization message: “You are not authorized to perform this action.” Do not disclose unnecessary permission structure or protected information.

**Status:** CLOSED — RECONCILED BASELINE



### Q962. How are SoD blocks shown?

**Answer:** Show that the action is blocked by role-separation/SoD policy, identify the affected controlled record where appropriate, and tell the user what authorized role must perform the next step.

**Status:** CLOSED — RECONCILED BASELINE



### Q963. How are workflow transition failures shown?

**Answer:** Show the current workflow state and explain that the requested transition is not permitted from that state.

**Status:** CLOSED — RECONCILED BASELINE



### Q964. How are concurrent-edit conflicts shown?

**Answer:** Concurrent-edit conflict: inform the user that the record changed elsewhere, do not silently overwrite it, and require refresh/reconciliation before saving.

**Status:** CLOSED — RECONCILED BASELINE



### Q965. How are stale-page/stale-data conflicts handled?

**Answer:** Stale-page/stale-data condition: detect revision mismatch, notify the user, refresh the authoritative record, and prevent silent overwrite.

**Status:** CLOSED — RECONCILED BASELINE



### Q966. What happens when a save fails after the user entered many values?

**Answer:** Sensitive controlled draft state is not persisted in browser localStorage or IndexedDB in v1. React application memory may hold unsaved form state. Server-side persistence uses controlled transactions and retry/idempotency handling.

**Status:** CLOSED — RECONCILED BASELINE



### Q967. Can drafts be recovered after a failed save?

**Answer:** The same no-localStorage/no-IndexedDB rule applies to sensitive controlled forms unless a future security/change decision explicitly approves another mechanism.

**Status:** CLOSED — RECONCILED BASELINE



### Q968. What happens when a PDF generation fails?

**Answer:** PDF failure: report remains unissued; no false “Issued” state is created; technical error is logged; user may retry after correction.

**Status:** CLOSED — RECONCILED BASELINE



### Q969. What happens when document storage fails?

**Answer:** Document-storage failure: report/document operation does not complete as successful; database state must not claim that the artifact was stored when it was not.

**Status:** CLOSED — RECONCILED BASELINE



### Q970. What happens when backup fails?

**Answer:** Backup failure generates an administrator alert and remains visible until resolved. Core laboratory operation may continue only while the backup state remains within the approved RPO; migration/other risky operations must be blocked when required backup protection is unavailable.

**Status:** CLOSED — RECONCILED BASELINE



### Q971. What happens when the server becomes unavailable during approval?

**Answer:** If the server becomes unavailable during approval, the client must treat the result as status unknown, not failed or successful. On reconnection the authoritative server state is checked before any retry.

**Status:** CLOSED — RECONCILED BASELINE



### Q972. How does the system avoid duplicate submissions after retry?

**Answer:** Duplicate submissions prevented through idempotency/command identifiers for critical commands plus unique business constraints and authoritative server responses.

**Status:** CLOSED — RECONCILED BASELINE



### Q973. Are operations required to be idempotent in any areas?

**Answer:** Yes. Idempotency is required particularly for Approval, Verification, Report Issue/Reissue, controlled Result Correction, critical workflow transitions, and other commands where a retry could duplicate a business event.

**Status:** CLOSED — RECONCILED BASELINE



### Q974. What user-visible status appears after an interrupted operation?

**Answer:** User-visible state after interruption: “Operation status could not be confirmed. Do not resubmit yet. Reconnect and check the record status.”

---

# 35. Search, Queues, and Usability

**Status:** CLOSED — RECONCILED BASELINE



### Q975. What are the most common searches users perform?

**Answer:** Most common searches: Sample ID; customer; external/customer sample ID; Request ID; TestInstance ID; test; status; date range; analyst/assignee; report ID; project where applicable.

**Status:** CLOSED — RECONCILED BASELINE



### Q976. Which fields must be searchable for samples?

**Answer:** Samples searchable by: internal Sample ID; external/customer sample ID; Customer; receipt date; sample/matrix classification; status; Request/Project reference; storage/location where applicable.

**Status:** CLOSED — RECONCILED BASELINE



### Q977. Which fields must be searchable for TestInstances?

**Answer:** TestInstances searchable by: TI ID; Sample ID; Test Code/name; Method/MethodVersion; status; analyst/assignee; priority; due date/TAT; Customer/Request; stage.

**Status:** CLOSED — RECONCILED BASELINE



### Q978. Which fields must be searchable for reports?

**Answer:** Reports searchable by: Report ID; Sample ID; Customer; report date; report status; revision; Request/Project; report type.

**Status:** CLOSED — RECONCILED BASELINE



### Q979. Which fields must be searchable for customers?

**Answer:** Customers searchable by: Customer ID; customer name; status; external reference/contact identifier where configured.

**Status:** CLOSED — RECONCILED BASELINE



### Q980. Which fields must be searchable for equipment?

**Answer:** Equipment searchable by: Equipment ID/asset ID; equipment name; type; serial number; status; location; calibration/qualification status; next due date.

**Status:** CLOSED — RECONCILED BASELINE



### Q981. Which filters are required on laboratory queues?

**Answer:** Queue filters: status/stage; assigned/unassigned; analyst; priority; due date; overdue; test; method; customer/project; hold/rework; date range.

**Status:** CLOSED — RECONCILED BASELINE



### Q982. Which queues are required by role?

**Answer:** Role-specific queues: Analyst work queue; Reviewer queue; Verification queue; Approval queue; Unassigned/assignment queue; Administrator/operational exceptions queue.

**Status:** CLOSED — RECONCILED BASELINE



### Q983. What is the default sort order of each queue?

**Answer:** Default queue sort: priority → overdue/due-soon status → due date ascending → received/created date ascending.

**Status:** CLOSED — RECONCILED BASELINE



### Q984. Can users save personal search filters?

**Answer:** Yes. Personal saved search/filter configurations should be supported.

**Status:** CLOSED — RECONCILED BASELINE



### Q985. Are shared saved filters required?

**Answer:** Yes. Shared saved filters are useful for standard laboratory queues and should be controlled/managed rather than freely edited by everyone.

**Status:** CLOSED — RECONCILED BASELINE



### Q986. Are dashboards required in v1?

**Answer:** Full analytics dashboards are not required for v1. A minimal operational dashboard is required as defined in Q957.

**Status:** CLOSED — RECONCILED BASELINE



### Q987. Which metrics must appear on dashboards?

**Answer:** Metrics: samples received/current by status; TestInstances pending by stage; overdue/due-soon work; pending Review/Verification/Approval; failed PDF jobs; backup age/status; disk/storage warnings.

**Status:** CLOSED — RECONCILED BASELINE



### Q988. Are keyboard-first workflows important for sample registration or result entry?

**Answer:** Yes. Keyboard-first operation is important, particularly for sample registration, allocation, repetitive result entry, review queues, and navigation through controlled forms.

**Status:** CLOSED — RECONCILED BASELINE



### Q989. Are barcode-scanner workflows required?

**Answer:** Yes. Barcode-scanner workflow should be supported in v1. USB HID barcode scanners should work without requiring a special network service.

**Status:** CLOSED — RECONCILED BASELINE



### Q990. Which screens must support fast repetitive data entry?

**Answer:** Fast repetitive entry is especially important for: sample registration; barcode capture; sample allocation; TestInstance result entry; review/check workflows; label printing.

**Status:** CLOSED — RECONCILED BASELINE



### Q991. Are bulk actions required?

**Answer:** Limited bulk actions are required, but only where the action is low-risk and auditable.

**Status:** CLOSED — RECONCILED BASELINE



### Q992. Which bulk actions are safe and permitted?

**Answer:** Safe bulk actions may include: bulk label printing; bulk export of already-authorized search results; limited controlled assignment of unstarted work where policy permits; non-technical queue/filter operations. Each affected record must still be traceable.

**Status:** CLOSED — RECONCILED BASELINE



### Q993. Which actions must always remain one-record-at-a-time?

**Answer:** Always one-record-at-a-time: result correction; Review; Verification; Approval; report issue/reissue; controlled sample identity correction; sample rejection/conditional acceptance; other high-risk technical/state-changing actions.

**Status:** CLOSED — RECONCILED BASELINE



### Q994. Are accessibility requirements defined?

**Answer:** Accessibility and viewport targets are controlled validation criteria. Exact numeric targets are established in the UI validation contract rather than silently treating an earlier proposal as approved.

**Status:** CLOSED — RECONCILED BASELINE



### Q995. What minimum browser viewport should be supported?

**Answer:** The supported minimum primary desktop browser viewport shall be **1280 × 720 CSS pixels**.
The application shall remain usable at smaller viewport sizes where practical, but **1280 × 720 shall be the formal baseline for layout/performance acceptance**.
Core functions shall not rely on hidden controls, horizontal scrolling for ordinary desktop workflows, or inaccessible modal content at the supported baseline viewport.
The tested browser version, operating-system scaling, and display scaling assumptions shall be recorded in UI verification evidence.

**Status:** CLOSED — RECONCILED BASELINE



### Q996. Are touchscreen devices used?

**Answer:** Touchscreen support is not required for v1 unless the laboratory has identified touchscreen hardware as an operational requirement.

**Status:** CLOSED — RECONCILED BASELINE



### Q997. Are thermal label printers required?

**Answer:** Thermal barcode label printing is recommended/expected for v1 if the laboratory will generate physical Sample labels from LabNexus. Exact printer/interface remains a deployment input.

**Status:** CLOSED — RECONCILED BASELINE



### Q998. Are A4 office printers required?

**Answer:** A4 office-printer support is required for laboratories that print reports, but physical printing must not be a dependency for electronic report issuance/storage.

**Status:** CLOSED — RECONCILED BASELINE



### Q999. What physical label sizes are used?

**Answer:** Not yet defined. The laboratory must specify the physical Sample-label size(s) based on containers, barcode type, printer, and required human-readable fields. Do not hard-code a label size into the core.

---

# 36. Barcode and Identification

**Status:** CLOSED — RECONCILED BASELINE



### Q1000. What identifiers will use Code 128?

**Answer:** Code 128 should be the primary linear barcode for business identifiers that need fast scanner entry, especially Sample ID. The exact identifier classes using Code 128 remain configurable.

**Status:** CLOSED — RECONCILED BASELINE



### Q1001. What identifiers will use QR?

**Answer:** QR should be available where higher payload capacity or camera-based identification is useful, primarily for Sample ID and optionally other controlled identifiers.

**Status:** CLOSED — RECONCILED BASELINE



### Q1002. What information should be encoded in each barcode/QR type?

**Answer:** Barcode/QR payloads should contain opaque LIMS-controlled identifiers, normally the business ID such as SAM-00000001. They should not contain sensitive customer data, test results, passwords, or other mutable technical data.

**Status:** CLOSED — RECONCILED BASELINE



### Q1003. Should QR codes encode only an internal identifier or more information?

**Answer:** Yes — QR should primarily encode the internal identifier or an opaque lookup token. It should not become a second uncontrolled data store. Additional payload is allowed only through controlled configuration.

**Status:** CLOSED — RECONCILED BASELINE



### Q1004. Must barcodes be printable from the LIMS?

**Answer:** Yes. LabNexus shall support printing controlled labels directly from the application.

**Status:** CLOSED — RECONCILED BASELINE



### Q1005. Which label printers are supported?

**Answer:** Printer support should use standard Windows printer mechanisms initially. The exact thermal-printer make/model is a deployment input and should be validated before go-live.

**Status:** CLOSED — RECONCILED BASELINE



### Q1006. What label formats are required?

**Answer:** Label format/size must be configurable. V1 should support at least one approved Sample label format and allow future formats without code changes.

**Status:** CLOSED — RECONCILED BASELINE



### Q1007. Can users scan a sample directly into the browser application?

**Answer:** Yes. A USB barcode scanner operating as a keyboard/HID device should work directly in browser fields. Camera-based browser scanning is not required for v1.

**Status:** CLOSED — RECONCILED BASELINE



### Q1008. What happens if a barcode is duplicated?

**Answer:** A duplicate controlled identifier must be blocked. The system shall not silently create or reuse a conflicting identifier.

**Status:** CLOSED — RECONCILED BASELINE



### Q1009. What happens if a barcode is damaged/unreadable?

**Answer:** A damaged/unreadable barcode may be reprinted using the same identifier after identity verification. A replacement identifier must not be generated merely because the physical label is damaged.

**Status:** CLOSED — RECONCILED BASELINE



### Q1010. Are manual entry fallbacks required?

**Answer:** Yes. Manual identifier entry is required as a fallback, with validation and appropriate confirmation/verification for high-risk actions.

**Status:** CLOSED — RECONCILED BASELINE



### Q1011. Are barcodes used for reports/documents/equipment as well as samples?

**Answer:** Barcodes may also be used for equipment, reports/documents, and other controlled objects, but Sample identification is the primary v1 use case. Object-specific usage remains configurable.

**Status:** CLOSED — RECONCILED BASELINE



### Q1012. Must barcode scans enforce state/workflow validity?

**Answer:** Yes. Scanning an identifier must not bypass business rules. The system must check that the scanned object exists, belongs to the expected object type, and is in a state where the requested action is permitted.

---

# 37. Notifications and Communication

**Status:** CLOSED — RECONCILED BASELINE



### Q1013. Are in-app notifications required?

**Answer:** In-app notifications are subordinate to authoritative business events and exist only for explicitly approved workflows. Where persisted, they identify recipient, severity, state, expiry and source event; they never replace the authoritative technical/business record.

**Status:** CLOSED — RECONCILED BASELINE



### Q1014. Are email notifications required?

**Answer:** Email notifications shall **not be required for v1**.
The application shall remain fully operational without Internet access or an SMTP service.
Where email is later approved, it shall be an asynchronous delivery channel subordinate to the authoritative LabNexus business event. Failure to deliver an email must never change the underlying laboratory workflow state.

**Status:** CLOSED — RECONCILED BASELINE



### Q1015. Are SMS/WhatsApp notifications required or explicitly out of scope?

**Answer:** SMS/WhatsApp notifications are **out of scope for v1**.
They introduce external service dependencies and are not necessary for the core offline-first workflow.
A future messaging integration would require separate approval covering provider, credentials, availability, confidentiality, failure handling, auditability, and offline behavior.

**Status:** CLOSED — RECONCILED BASELINE



### Q1016. Which events require notifications?

**Answer:** The v1 notification event set shall be intentionally small and controlled.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1017. Who receives overdue-test notifications?

**Answer:** Overdue-test notifications shall go to the **responsible operational/coordinator role and the designated supervisory/technical role** according to the approved escalation matrix.
The performing analyst does not need to receive every escalation unless the laboratory policy identifies the analyst as an action owner.
The notification shall identify the TestInstance, due date, current state, responsible assignment, and required action without exposing unrelated confidential information.

**Status:** CLOSED — RECONCILED BASELINE



### Q1018. Who receives QC-failure notifications?

**Answer:** QC-failure notifications shall go to the **designated Technical/QC responsible role**, with escalation to Quality where the configured failure is quality-significant or blocking.
The analyst who performed the affected work may receive the notification as an operational task, but notification recipients shall be governed by approved responsibility rules.
The notification must link to the authoritative QC failure/nonconformance record rather than become the primary evidence of the failure.

**Status:** CLOSED — RECONCILED BASELINE



### Q1019. Who receives approval-pending notifications?

**Answer:** Approval-pending notifications shall go to the **authorized approver role/person responsible for the affected TestInstance**, subject to the approved assignment/escalation model.
Where an approval remains pending beyond a configured threshold, an escalation notification may go to the designated supervisory/Quality/Technical authority.
The notification shall not bypass SoD; an unqualified or blocked user shall not receive the action merely because they received the notification.

**Status:** CLOSED — RECONCILED BASELINE



### Q1020. Who receives backup-failure notifications?

**Answer:** Backup-failure notifications shall go to the **System Administrator/Backup Operations role** and, for material or persistent failures, the designated Technical/Operations and Quality authority.

The notification shall contain:
* Backup type;
* Failure/missed-run timestamp;
* Last successful backup;
* Current recovery-point age;
* Current RPO exposure;
* Required corrective action.

No Internet-based notification channel is required for this to operate.

**Status:** CLOSED — RECONCILED BASELINE



### Q1021. Can notifications work without Internet?

**Answer:** Yes. **Core in-app notifications shall work entirely without Internet connectivity.**
Notifications shall be stored locally in LabNexus and generated from authoritative internal events.

No Internet service, cloud messaging provider, or external notification gateway shall be required for:
* overdue work;
* QC failures;
* pending approvals;
* backup failures;
* operational alerts.

Email/SMS/WhatsApp remain optional future delivery channels and do not form part of the core event model.

**Status:** CLOSED — RECONCILED BASELINE



### Q1022. If email is required, is there an approved local SMTP server?

**Answer:** No approved local SMTP server is required for v1 because **email notification is out of scope for the core release**.
If email is later approved, the deployment must identify an approved SMTP service that is accessible under the laboratory's actual network/offline operating model.
Email credentials shall use the protected secret-management mechanism defined in the Security Baseline.
SMTP failure shall never block or alter the authoritative laboratory workflow.

**Status:** CLOSED — RECONCILED BASELINE



### Q1023. Are external customer notifications sent by the LIMS or manually by staff?

**Answer:** For v1, external customer notifications shall be **manual and controlled by laboratory staff**, except for any future explicitly approved integration.
LabNexus shall record the underlying report/communication event where such tracking is required, but it shall not assume that successful LIMS report issuance means successful customer receipt.
A future automated customer notification mechanism requires separate approval for confidentiality, recipient control, delivery evidence, failure handling, and offline behavior.

**Status:** CLOSED — RECONCILED BASELINE



### Q1024. Are notifications themselves controlled records?

**Answer:** Yes, selected notifications shall be treated as **controlled operational records/evidence**, but the notification itself is not the authoritative laboratory record.
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

**Status:** CLOSED — RECONCILED BASELINE



### Q1025. What counts as nonconforming work in the laboratory?

**Answer:** Nonconforming work means work that does not conform to approved requirements, method, procedure, equipment condition, sample condition, QC requirements, authorization, workflow, or other controlled laboratory requirements. Exact taxonomy is configurable.

**Status:** CLOSED — RECONCILED BASELINE



### Q1026. Who can declare nonconforming work?

**Answer:** Authorized laboratory personnel who detect or are responsible for the issue may declare nonconforming work.

**Status:** CLOSED — RECONCILED BASELINE



### Q1027. What events can trigger nonconforming-work handling?

**Answer:** Triggers may include failed QC; incorrect sample identity; unsuitable sample condition; equipment failure; method/procedure deviation; unauthorized work; environmental condition failure; calculation/data error; report error; workflow breach; or other configured triggers.

**Status:** CLOSED — RECONCILED BASELINE



### Q1028. Does nonconforming work block specific TestInstances?

**Answer:** Nonconformance affected-record information and two-person-control action lists are machine-readable and aligned with the authorization/SoD model, identifying affected Samples, TestInstances, Results/Reports and required dispositions where applicable.

**Status:** CLOSED — RECONCILED BASELINE



### Q1029. Can one issue affect multiple samples/TestInstances?

**Answer:** Yes. One nonconformance may affect multiple Samples and/or TestInstances.
The nonconformance model shall support explicit many-to-many or otherwise appropriate affected-record relationships.
Each affected record shall remain individually identifiable so that the impact assessment can determine whether the required disposition is the same or different for each record.
A nonconformance shall not be represented as affecting an entire batch merely through an unsupported blanket flag.

**Status:** CLOSED — RECONCILED BASELINE



### Q1030. What statuses exist for nonconforming work?

**Answer:** The v1 nonconformance lifecycle shall use controlled states such as:
**OPEN → UNDER_INVESTIGATION → DISPOSITION_REQUIRED → ACTION_IN_PROGRESS → CLOSED**
with appropriate alternatives such as:
- ON_HOLD;
- REJECTED/INVALIDATED where applicable;
- CANCELLED where legitimately permitted.

Exact state names may be refined in the Nonconformance / Affected Record Impact Model, but the lifecycle shall distinguish discovery, investigation, disposition, action, and closure.
A closed nonconformance shall remain historically preserved.

**Status:** CLOSED — RECONCILED BASELINE



### Q1031. Who investigates it?

**Answer:** Nonconformance investigation shall be performed by an authorized competent person designated according to the issue type.
The investigator shall not approve their own controlled disposition where SoD or laboratory policy requires independent review.
For technical nonconformance, the Laboratory Technical Authority shall be involved as appropriate; Quality Authority shall be involved where QMS/nonconformance governance requires it.

**Status:** CLOSED — RECONCILED BASELINE



### Q1032. Who can close it?

**Answer:** Nonconformance closure shall require an authorized Quality/Technical authority according to the nature and severity of the issue.

Closure shall confirm:
- investigation completed;
- affected records identified;
- required disposition completed;
- corrective action completed where required;
- customer/report impacts addressed where applicable;
- required evidence present;
- required independent review/approval complete.

The investigator shall not automatically have unilateral closure authority.

**Status:** CLOSED — RECONCILED BASELINE



### Q1033. Must customer notification be recorded?

**Answer:** Two-person control is a server-enforced action rule. The system verifies distinct eligible actors and records both the protected action and independent second-party evidence.

**Status:** CLOSED — RECONCILED BASELINE



### Q1034. Must affected reports be identified?

**Answer:** Yes. The system shall identify affected reports where a nonconformance may affect reportable work.
Affected Report/ReportRevision relationships shall be traceable from the nonconformance and the affected Result/TestInstance.
The impact assessment shall determine whether the report requires no action, correction, reissue, withdrawal, or another controlled disposition.
Already issued reports shall never be silently modified.

**Status:** CLOSED — RECONCILED BASELINE



### Q1035. Can nonconforming work require re-testing?

**Answer:** Yes. Nonconforming work may require retesting where the approved technical/quality disposition determines that retesting is necessary.
Retesting shall create a distinct TestInstance where it represents a new execution.
The original TestInstance and its nonconformance shall remain preserved, and the new TestInstance shall reference the originating work and reason.
Retesting shall not automatically invalidate the prior result unless the authorized disposition determines that it should be treated as invalid.

**Status:** CLOSED — RECONCILED BASELINE



### Q1036. Can rework create a new TestInstance or modify the current one?

**Answer:** Where rework represents a distinct new execution, it shall create a new TestInstance linked to the originating TestInstance.
Where the laboratory procedure permits correction of the current execution without creating a distinct execution occurrence, the current TestInstance may proceed through controlled rework.
The governing rule shall be explicit in the Execution Semantics Decision Table.
In both cases, the original history shall remain preserved and the reason, actor, authorization, and relationships shall be auditable.

**Status:** CLOSED — RECONCILED BASELINE



### Q1037. Which path preserves the original history most clearly?

**Answer:** The clearest historical-preservation path is to retain the original TestInstance and create a distinct linked TestInstance whenever a genuinely new execution occurs.
The original record shall never be overwritten.
Rework, retest, repeat, correction, or other disposition shall be explicitly classified and linked so that the complete chain of work can be reconstructed.

**Status:** CLOSED — RECONCILED BASELINE



### Q1038. Are CAPA records required in the LIMS?

**Answer:** CAPA capability in v1 shall remain limited to the minimum controlled functionality required by the laboratory's approved QMS/nonconformance process.
Where an investigation requires corrective or preventive action, the LIMS shall support controlled linkage to the relevant action/evidence.
A general enterprise CAPA subsystem shall not be introduced without a separately approved requirement.

**Status:** CLOSED — RECONCILED BASELINE



### Q1039. Are root-cause classifications required?

**Answer:** Yes. Root-cause classification shall be supported where required by the laboratory's approved nonconformance/CAPA process.
Root-cause categories shall be controlled configuration rather than unrestricted free text, with an explanatory narrative available where required.
The laboratory shall define the actual root-cause taxonomy; LabNexus shall not invent technical cause categories as laboratory policy.

**Status:** CLOSED — RECONCILED BASELINE



### Q1040. Are effectiveness checks required?

**Answer:** Effectiveness checks shall be supported where required by the laboratory's approved corrective-action/CAPA process.

Where an effectiveness check is required, the system shall preserve:
- action being evaluated;
- effectiveness criterion;
- evaluation date/time;
- evaluator;
- evidence;
- outcome;
- follow-up/disposition.

Effectiveness checking shall not be universally mandatory unless the approved laboratory procedure requires it.

**Status:** CLOSED — RECONCILED BASELINE



### Q1041. What are the valid reasons for sample rejection?

**Answer:** Sample rejection reasons should be controlled, e.g. identity issue, insufficient quantity, unsuitable condition, container/packaging problem, preservation/handling issue, leakage/damage, requested test not possible, missing required information, expired/invalid sample, customer instruction, plus controlled “Other” with justification.

**Status:** CLOSED — RECONCILED BASELINE



### Q1042. What are the valid reasons for TestInstance cancellation?

**Answer:** TestInstance cancellation reasons should be controlled, e.g. customer cancellation, duplicate request, sample unavailable/invalid, method unavailable, administrative error, safety restriction, nonconformance, not required, plus justified Other.

**Status:** CLOSED — RECONCILED BASELINE



### Q1043. What are the valid reasons for TestInstance reopening?

**Answer:** Reopening reasons should include result correction, workflow correction, report-impact correction, failed/invalid review/verification, approved rework, nonconformance investigation, plus controlled Other.

**Status:** CLOSED — RECONCILED BASELINE



### Q1044. What are the valid reasons for result correction?

**Answer:** Result-correction reasons should be controlled, such as transcription error, calculation error, wrong parameter/unit, instrument/data-entry error, sample identity correction, method/configuration issue, approved technical correction, plus justified Other.

**Status:** CLOSED — RECONCILED BASELINE



### Q1045. Who may perform each action?

**Answer:** Each action is permission-controlled: intake/sample rejection by authorized intake/technical users; cancellation by authorized operational users; reopening/correction by specifically authorized roles; approval by designated approver roles.

**Status:** CLOSED — RECONCILED BASELINE



### Q1046. Which actions require second-person approval?

**Answer:** Affected-record and two-person-control definitions are controlled/effective-dated where policy can change. Hard SoD restrictions remain non-bypassable.

**Status:** CLOSED — RECONCILED BASELINE



### Q1047. Can cancelled records be restored?

**Answer:** Cancelled records are not restored by deletion/undelete. A controlled new action may reopen/recreate work where policy allows, preserving cancellation history.

**Status:** CLOSED — RECONCILED BASELINE



### Q1048. Can rejected samples later be accepted?

**Answer:** Yes. A rejected Sample may later be accepted only through a controlled acceptance decision with reason/evidence and retained rejection history.

**Status:** CLOSED — RECONCILED BASELINE



### Q1049. Can a cancelled TestInstance ever be restarted?

**Answer:** A cancelled TestInstance may not simply resume invisibly. Where work needs to continue, policy determines whether controlled reopening is permitted or a new TestInstance is required.

**Status:** CLOSED — RECONCILED BASELINE



### Q1050. If work resumes after cancellation, is a new TestInstance required?

**Answer:** Yes. Where cancellation terminated the execution and work genuinely starts again, a new TestInstance is required.

**Status:** CLOSED — RECONCILED BASELINE



### Q1051. Does reopening always require a reason?

**Answer:** Yes. Reopening always requires a controlled reason and audit event.

**Status:** CLOSED — RECONCILED BASELINE



### Q1052. Does reopening invalidate previous review/verification/approval states?

**Answer:** Yes. Reopening an approved TestInstance moves it out of its previous approved state and requires the affected Review/Verification/Approval path to be performed again.

**Status:** CLOSED — RECONCILED BASELINE



### Q1053. Does reopening create a new result revision?

**Answer:** Reopening itself does not automatically create a ResultRevision. A technical result change creates the appropriate ResultRevision. The reopen event is separately recorded.

**Status:** CLOSED — RECONCILED BASELINE



### Q1054. What exactly happens to prior ApprovalSnapshots?

**Answer:** Prior ApprovalSnapshots remain immutable historical evidence. They are not deleted or rewritten. The newly corrected state requires a new review/verification/approval and therefore a new ApprovalSnapshot.

**Status:** CLOSED — RECONCILED BASELINE



### Q1055. What exactly happens to existing report revisions?

**Answer:** Existing ReportRevisions remain immutable. A correction triggers report impact assessment; if report content changes, a new ReportRevision is issued/released through the controlled process.

**Status:** CLOSED — RECONCILED BASELINE



### Q1056. Can approval happen again after correction?

**Answer:** Yes. A corrected/reopened TestInstance may be approved again after required Review and Verification.

**Status:** CLOSED — RECONCILED BASELINE



### Q1057. What distinguishes reapproval from a first approval?

**Answer:** Reapproval refers to a previously approved controlled record that was subsequently reopened/corrected/reworked. It must retain links to the prior approval and the reason for the new approval.

**Status:** CLOSED — RECONCILED BASELINE



### Q1058. Must reapproval create a distinct event type?

**Answer:** Yes. Reapproval shall create a distinct approval-chain event classification so historical reviewers can distinguish initial approval from approval after correction/rework/reopening.

---

# 40. Retention and Archive

**Status:** CLOSED — RECONCILED BASELINE



### Q1059. What records must be retained?

**Answer:** Retain controlled laboratory records including Samples, Requests, TestInstances, Results/ResultRevisions, Review/Verification/Approval history, Reports/ReportRevisions/PDFs, audit records, QC, nonconformance/CAPA, equipment, methods, configurations, controlled documents, and relevant migration/provenance evidence.

**Status:** CLOSED — RECONCILED BASELINE



### Q1060. What is the retention period for samples?

**Answer:** Physical sample retention is not automatically 10 years. Sample custody/identity records are controlled records and follow the 10-year record requirement; physical-material retention shall be defined by sample/method/customer/legal requirements.

**Status:** CLOSED — RECONCILED BASELINE



### Q1061. What is the retention period for results?

**Answer:** Controlled results and ResultRevision history: 10 years minimum.

**Status:** CLOSED — RECONCILED BASELINE



### Q1062. What is the retention period for reports?

**Answer:** Reports, ReportRevisions, and issued PDFs: 10 years minimum.

**Status:** CLOSED — RECONCILED BASELINE



### Q1063. What is the retention period for audit history?

**Answer:** Audit history: 10 years minimum, and preferably retained for the full life of the corresponding controlled records.

**Status:** CLOSED — RECONCILED BASELINE



### Q1064. What is the retention period for equipment records?

**Answer:** Equipment records: 10 years minimum or longer where required by applicable laboratory policy/regulation.

**Status:** CLOSED — RECONCILED BASELINE



### Q1065. What is the retention period for QC records?

**Answer:** QC records: 10 years minimum.

**Status:** CLOSED — RECONCILED BASELINE



### Q1066. What is the retention period for configuration history?

**Answer:** Configuration history: 10 years minimum and must remain sufficient to reconstruct historical decisions.

**Status:** CLOSED — RECONCILED BASELINE



### Q1067. What is the retention period for controlled documents?

**Answer:** Controlled documents: 10 years minimum or longer where the document's governing policy requires it.

**Status:** CLOSED — RECONCILED BASELINE



### Q1068. Can records be archived without being deleted?

**Answer:** Archive is a controlled historical state: read-only and searchable according to permissions, not a path back into ordinary active execution. V1 does not require PDF/A unless separately approved; the preserved issued PDF is authoritative.

**Status:** CLOSED — RECONCILED BASELINE



### Q1069. What does “Archive” mean operationally?

**Answer:** For LabNexus, **Archive** shall mean a controlled state in which a record is retained for historical/reference purposes after it is no longer part of ordinary active operational processing.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1070. Are archived records still searchable?

**Answer:** Yes. Archived records shall remain **searchable by authorized users**, subject to archive-specific access controls and system capability.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1071. Are archived records read-only?

**Answer:** Yes. Archived controlled records shall be **read-only under normal application operation**.
Ordinary users shall not edit, delete, approve, recalculate, reissue, or otherwise alter archived records.
Where a genuine historical correction, legal requirement, recovery operation, or other exceptional action is necessary, it shall use a separately authorized controlled process that preserves the original archived state and records the reason, authority, actor, timestamp, and resulting action.
Archive status must therefore protect historical evidence while still allowing controlled administrative/recovery procedures where legitimately required.

**Status:** CLOSED — RECONCILED BASELINE



### Q1072. Can archived records be restored to active use?

**Answer:** Archived records shall **not normally be restored to ordinary active use**.

The preferred v1 rule is:
**Archive is a retention state, not a workflow state.**

If an archived record must be used as the basis for new laboratory work, the preferred approach is to create a new active record/workflow linked to the historical archived record.
A controlled archive restoration/reopening mechanism may exist for exceptional administrative or recovery purposes, but it shall not silently convert historical data back into an active record or alter its historical meaning.
Where restoration is technically necessary, the action shall preserve the archived copy and create a full audit trail.

**Status:** CLOSED — RECONCILED BASELINE



### Q1073. Who can authorize restoration from archive?

**Answer:** Restoration from archive shall require authorization by a **designated Laboratory Quality/Records Authority or Technical Authority**, depending on the reason for restoration.

Recommended control:
* Quality/Records Authority: archive/retention/records decisions;
* Technical Authority: technical recovery or investigation where technical interpretation is involved;
* System Administrator: performs the technical restoration operation;
* Independent verification: required where restoration affects controlled technical records or recovery integrity.

The person technically executing the restoration should not automatically be the person approving the underlying laboratory decision.
Restoration shall require a structured reason, affected records, authorization, execution evidence, and verification where applicable.

**Status:** CLOSED — RECONCILED BASELINE



### Q1074. Are archival actions audited?

**Answer:** Yes. **All material archival actions shall be audited.**

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1075. Are archived PDFs stored in the same storage hierarchy?

**Answer:** Archived PDFs should remain in the **same application-controlled storage architecture and logical document-management model**, while being distinguishable through archive/retention metadata.
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

**Status:** CLOSED — RECONCILED BASELINE



### Q1076. Are cold/offline archives required?

**Answer:** Cold/offline archives should be **supported as an approved operational option but not made mandatory for every archived record in v1**.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1077. What is the approved destruction process after retention expires?

**Answer:** After retention expiry and absent legal/customer hold, destruction requires an approved retention check, authorized decision, controlled deletion/destruction, and destruction record.

**Status:** CLOSED — RECONCILED BASELINE



### Q1078. Who authorizes destruction?

**Answer:** Destruction authorized by the designated laboratory management/quality authority, with technical execution by the authorized administrator.

**Status:** CLOSED — RECONCILED BASELINE



### Q1079. What destruction evidence is required?

**Answer:** Evidence: record/category; retention rule; expiry date; hold check; authorization; destruction date/time; operator; scope/count; storage/archive location; resulting destruction certificate/event.

**Status:** CLOSED — RECONCILED BASELINE



### Q1080. Are legal holds or customer holds required?

**Answer:** Physical sample disposal is separate from record retention and requires the approved disposal authority, completed TestInstance dispositions, expiration of any retained-sample period and absence of applicable holds. The discipline-specific retained-sample period is laboratory policy, not a developer default.

---

# 41. Data Import and Migration

**Status:** CLOSED — RECONCILED BASELINE



### Q1081. Which spreadsheets or existing databases contain source records?

**Answer:** Historical migration is conditional on controlled discovery and assessment. V1 default migration is approved customer master data and historical issued report PDFs as read-only historical material with provenance; historical result/TestInstance approval chains are not fabricated into live technical records.

**Status:** CLOSED — RECONCILED BASELINE



### Q1082. Which data sets are candidates for migration?

**Answer:** Candidate migration datasets shall be determined from the documented legacy discovery and Migration Assessment.
Candidates may include historical Samples, Requests, TestInstances, Results, reports/PDFs, customer/project references, equipment records, or other records where migration provides approved operational, traceability, quality, contractual, legal, or historical value.
A dataset shall not become a migration candidate merely because it exists.
Each candidate dataset shall have an explicit migration decision: migrate, retain outside LIMS, or reject as unsuitable/unneeded.

**Status:** CLOSED — RECONCILED BASELINE



### Q1083. Who owns the source data?

**Answer:** Source-data ownership shall remain with the laboratory or other organization that legitimately controls the original records.
The Migration Assessment shall identify the source owner/custodian for each migration dataset.
Source ownership does not transfer to the migration executor merely because the data is imported into LabNexus.
Where ownership or authority is unclear, the dataset shall not be treated as approved for migration until the issue is resolved

**Status:** CLOSED — RECONCILED BASELINE



### Q1084. Which source fields map to LIMS fields?

**Answer:** Source-to-LIMS mapping shall be defined through a controlled migration mapping specification.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1085. Which source values are ambiguous?

**Answer:** Ambiguous source values shall be explicitly identified during migration assessment and shall not be silently interpreted.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1086. How are duplicate historical records detected?

**Answer:** Duplicate historical records shall be identified using controlled matching/reconciliation rules appropriate to the source.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1087. How are missing historical values represented?

**Answer:** Missing historical values shall be represented as genuinely missing/unknown rather than fabricated.

The migration process shall preserve the distinction between:
- unknown/not recorded;
- not applicable;
- not performed;
- not detected;
- blank/empty source value;
- value genuinely unavailable.

A missing value shall not be replaced with zero, a guessed value, or a fabricated date merely to satisfy a required LIMS field.
Where a mandatory LIMS field has no valid historical source value, the migration specification shall define an approved historical representation or classify the record as unsuitable for migration.

**Status:** CLOSED — RECONCILED BASELINE



### Q1088. How are source documents migrated?

**Answer:** Source documents shall be migrated only through the controlled migration procedure. Each migrated source document must retain its original bytes where practicable, original filename and source reference, document date/version where known, source record linkage, migration batch/reference, and SHA-256 hash of the imported file.
Migrated documents shall be stored as immutable historical document/attachment records. If a document requires interpretation, conversion, OCR, renaming, or other transformation, the original source artifact must remain preserved and the transformation must be recorded.
No migrated document shall silently become an active controlled document merely because it was imported. Its status and intended use must be explicitly established through the migration assessment and document-control rules.

**Status:** CLOSED — RECONCILED BASELINE



### Q1089. How are historical report PDFs linked?

**Answer:** The default migration scope is customer master data and historical issued report PDFs, linked to customer/legacy sample references as read-only history. No historical results/TestInstances are imported into live technical tables merely to make the system look complete.

**Status:** CLOSED — RECONCILED BASELINE



### Q1090. How is provenance of migrated data recorded?

**Answer:** Every migrated record shall carry sufficient provenance to reconstruct what was imported, from where, when, by whom, and how it was transformed.
At minimum the migration provenance shall include: original source system/file/document; original source record identifier; source date/time or period and its precision; LIMS migration timestamp; migration executor; migration batch/reference; migration tool/procedure version; source-to-target mapping; transformations and controlled interpretations; original source value where transformed; verification status; verifier; approval/evidence reference; exceptions/ambiguities; and migration disposition.
Migration provenance is historical evidence and must not be overwritten by later normal record editing.

**Status:** CLOSED — RECONCILED BASELINE



### Q1091. Is migrated data treated as historical technical records or as newly entered LIMS records?

**Answer:** Migrated data shall be treated as **historical technical records or historical supporting records**, not as newly performed LIMS work.
The system shall distinguish the original laboratory event date/time and source provenance from the date/time on which the information was entered into LabNexus. A migrated historical result must not imply that the laboratory performed that historical test using LabNexus.
Historical imported data shall be read-only by default and governed by the Migration Provenance Contract.

**Status:** CLOSED — RECONCILED BASELINE



### Q1092. Can historical imported data enter current workflows?

**Answer:** Historical imported data shall **not automatically enter current operational workflows**.
Imported records may be searched, reviewed, reported as historical information, and referenced for traceability. They must not automatically become current TestInstances, current work queues, current approvals, or active technical records.
A controlled exceptional process may create a new current LIMS workflow when there is a legitimate business or technical need. In that case the new activity must be explicitly identified as a new LIMS event and must retain the historical source relationship.

**Status:** CLOSED — RECONCILED BASELINE



### Q1093. Are migrated records editable?

**Answer:** Migrated records shall be **read-only by default**.

Direct editing of imported historical technical content shall not be permitted through ordinary operational screens. If a historical record contains an identified error or requires an approved correction, the original migrated representation must remain preserved and a controlled historical correction mechanism shall record the reason, authority, evidence, changed representation, actor, timestamp, and verification.

No correction may silently convert historical information into a new unqualified LIMS record.

**Status:** CLOSED — RECONCILED BASELINE



### Q1094. Who validates migrated data?

**Answer:** Migrated data shall be validated by an **independent verifier** who did not perform the migration execution for the records being verified.
Validation shall involve the appropriate combination of Migration Assessor, Technical Authority, Quality/Business Authority, and Independent Verifier according to the Migration Authority Matrix. The verifier shall confirm completeness, field mapping, critical identity/provenance, transformation correctness, document integrity, exceptions, and reconciliation evidence.
Final migration acceptance shall be recorded separately from migration execution.

**Status:** CLOSED — RECONCILED BASELINE



### Q1095. What sample size is used for migration verification?

**Answer:** Migration verification shall use a **risk-based verification strategy**, not an arbitrary universal percentage.
At minimum, migration verification shall include 100% reconciliation of source-to-target record/control totals and verification of all critical identity and provenance controls. Individual record-content verification shall use a documented stratified sample covering representative record types, source qualities, transformations, boundary cases, ambiguities, missing values, and high-risk records.
Where the migration population is small enough, 100% record-level verification may be required. The final sample size and selection method shall be defined in the approved Migration Verification Plan before migration execution.

**Status:** CLOSED — RECONCILED BASELINE



### Q1096. What reconciliation report proves migration completeness?

**Answer:** The migration reconciliation report shall demonstrate, at minimum:
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

**Status:** CLOSED — RECONCILED BASELINE



### Q1097. What is the rollback plan for a failed migration?

**Answer:** A failed migration shall not leave an uncontrolled partial live state.
Before migration, the controlled database and document/attachment stores shall have a verified recovery point. Migration shall execute as a controlled batch with identifiable migration references. If migration fails, the migration shall be stopped, the failure preserved as evidence, and the environment restored to the pre-migration baseline using the approved recovery procedure where necessary.
The failed migration's logs, evidence, source data, attempted mappings, exceptions, and disposition must be retained. A subsequent attempt shall use a new controlled migration batch/version and shall not silently continue from an unknown partial state.

**Status:** CLOSED — RECONCILED BASELINE



### Q1098. Is migration a one-time activity or an ongoing import feature?

**Answer:** Migration is a **controlled one-time v1 activity**, not a generic ongoing spreadsheet/import feature.
Any additional historical migration after the initial migration shall be treated as a new controlled migration activity with its own source assessment, mapping, batch identification, verification, acceptance, and evidence.
Generic post-go-live CSV/Excel-to-database import is not part of v1 unless separately approved as a controlled capability.

**Status:** CLOSED — RECONCILED BASELINE



### Q1099. Are CSV/Excel imports required after go-live?

**Answer:** There is no generic spreadsheet-to-database import in v1. The controlled import boundary is approved go-live master-data seeding through the validated/audited administration path plus controlled migration batches.

### Q1100. If imports are allowed, which import types are controlled and validated?

**Answer:** Imported historical content carries origin/provenance metadata distinguishing migrated history from native v1 records. External identifiers remain reference data and do not replace authoritative internal identity.

### Q1101. Which fields are mandatory at each workflow stage?

**Answer:** Mandatory fields are stage-specific, not universally mandatory. Intake, allocation, execution, Review, Verification, Approval, and Report Issue each enforce their own required-field set.

**Status:** CLOSED — RECONCILED BASELINE



### Q1102. Which values have controlled vocabularies?

**Answer:** Controlled vocabularies include statuses, roles, matrix/sample types, test codes, units, methods, result qualifiers, reasons, locations, equipment states, QC classifications, rejection/cancellation/correction reasons, etc.

**Status:** CLOSED — RECONCILED BASELINE



### Q1103. Which fields require uniqueness?

**Answer:** Uniqueness is required for identifiers that are defined as globally unique, including Customer ID, Sample ID, TestInstance ID, Report ID, Test Code, Method ID/Version identifiers, Parameter IDs, and configured external identifiers.

**Status:** CLOSED — RECONCILED BASELINE



### Q1104. Which fields require normalization?

**Answer:** Normalization applies to controlled identifiers, whitespace, structured codes, unit representation, and master-data references. Free-text narrative should not be over-normalized.

**Status:** CLOSED — RECONCILED BASELINE



### Q1105. How are spelling/abbreviation variations handled?

**Answer:** Variations are handled through controlled aliases/codes, not by silently changing source meaning.

**Status:** CLOSED — RECONCILED BASELINE



### Q1106. Are master-data values case-sensitive?

**Answer:** Controlled codes/identifiers are generally case-insensitive for uniqueness/search where appropriate, while stored canonical representation is controlled. Free text retains entered case.

**Status:** CLOSED — RECONCILED BASELINE



### Q1107. Are leading/trailing spaces normalized?

**Answer:** Leading/trailing whitespace is normalized/removed for structured text fields. Meaningful internal spaces are retained.

**Status:** CLOSED — RECONCILED BASELINE



### Q1108. Are Unicode and multilingual values required?

**Answer:** Yes. Unicode must be supported.

**Status:** CLOSED — RECONCILED BASELINE



### Q1109. Is local-language data required?

**Answer:** Local-language UI/data entry is not required for v1, but Unicode capability must allow local-language names/text when legitimately needed.

**Status:** CLOSED — RECONCILED BASELINE



### Q1110. Are decimals stored consistently using a defined numeric representation?

**Answer:** Numeric laboratory values shall use a defined database numeric representation such as fixed-precision decimal where exact decimal semantics matter; floating-point must not be used casually for controlled laboratory calculations.

**Status:** CLOSED — RECONCILED BASELINE



### Q1111. Are dates stored consistently?

**Answer:** Dates use ISO-style database representations and controlled application serialization.

**Status:** CLOSED — RECONCILED BASELINE



### Q1112. Are times stored consistently?

**Answer:** Times use timezone-aware date/time handling at application boundaries and UTC internally.

**Status:** CLOSED — RECONCILED BASELINE



### Q1113. What timestamp standard is used internally?

**Answer:** Internal timestamp standard: UTC.

**Status:** CLOSED — RECONCILED BASELINE



### Q1114. How are missing values represented?

**Answer:** Missing value = structured NULL/unknown, not an arbitrary text value such as -, NA, or 0.

**Status:** CLOSED — RECONCILED BASELINE



### Q1115. How are “not applicable”, “not detected”, “below LOQ”, and “not performed” distinguished?

**Answer:** Not Applicable, Not Detected, Below LOQ, and Not Performed must be separate structured states/qualifiers, never inferred from free text alone.

**Status:** CLOSED — RECONCILED BASELINE



### Q1116. Which fields allow free text?

**Answer:** Free text allowed for controlled notes/comments, sample observations, investigation narratives, reasons/justifications, report comments, and other explicitly designated narrative fields.

**Status:** CLOSED — RECONCILED BASELINE



### Q1117. Where is free text prohibited?

**Answer:** Free text prohibited where machine-readable controlled values are required: identifiers, statuses, units, workflow states, approval identity, method/version, QC disposition, and similar structured fields.

**Status:** CLOSED — RECONCILED BASELINE



### Q1118. How are invalid master-data references handled?

**Answer:** Invalid master-data references must be rejected at validation/database levels. Historical references remain valid through versioned/master-history mechanisms.

**Status:** CLOSED — RECONCILED BASELINE



### Q1119. What data-quality checks run before approval?

**Answer:** Before Approval: completeness, required parameters, validity/units, calculation status, method/version, QC requirements, authorization/SoD, workflow state, unresolved holds/nonconformance, and data consistency.

**Status:** CLOSED — RECONCILED BASELINE



### Q1120. What data-quality checks run before report issue?

**Answer:** Before Report Issue: approved result state, exact approved ResultRevision/ApprovalSnapshot, report completeness, correct customer/sample/report identifiers, method/accreditation representation, document-generation success, artifact hash/storage, and no blocking report-impact issue.

---

# 43. API and Internal Service Boundaries

**Status:** CLOSED — RECONCILED BASELINE



### Q1121. What are the major domain modules inside the modular monolith?

**Answer:** The v1 internal module set is `identity_access`, `audit`, `numbering`, `master_data`, `sample`, `test_execution`, `method_config`, `review_approval`, `equipment_qc`, `quality`, `documents`, `reporting`, `ops`. Application layers are router → application service → domain → repository; cross-module repository access is prohibited.

**Status:** CLOSED — RECONCILED BASELINE



### Q1122. What responsibilities belong to each module?

**Answer:** The application contract is REST/JSON under `/api/v1` with OpenAPI generation. Endpoints call application services and cannot bypass domain rules or repository controls.

**Status:** CLOSED — RECONCILED BASELINE



### Q1123. What module dependencies are permitted?

**Answer:** API errors use RFC 7807-compatible problem details with stable `code`, `message`, `correlation_id` and structured `field_errors` where applicable.

**Status:** CLOSED — RECONCILED BASELINE



### Q1124. Which modules may access which repositories?

**Answer:** Controlled mutable rows use optimistic concurrency such as `row_version`; conflicting updates return the controlled conflict/precondition response rather than silently overwriting another user.

**Status:** CLOSED — RECONCILED BASELINE



### Q1125. Are direct cross-module database writes prohibited?

**Answer:** Command endpoints use `Idempotency-Key` where retries could duplicate a business action; idempotency is enforced server-side.

**Status:** CLOSED — RECONCILED BASELINE



### Q1126. What is the authoritative application write path for controlled records?

**Answer:** `X-Request-ID`/correlation identity is retained in relevant audit events so a request can be traced through the controlled write path.

**Status:** CLOSED — RECONCILED BASELINE



### Q1127. Which business rules must live in domain services rather than routers/UI?

**Answer:** List endpoints use pagination with a default size of 50 and maximum 200; audit and queue resources use cursor pagination; sort fields are whitelisted.

**Status:** CLOSED — RECONCILED BASELINE



### Q1128. Which operations must be atomic across multiple entities?

**Answer:** API responses do not expose hashes, secrets or physical filesystem paths merely because those values exist in internal records.

**Status:** CLOSED — RECONCILED BASELINE



### Q1129. Which operations need explicit transactional boundaries?

**Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q1130. Which operations require optimistic concurrency control?

**Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q1131. Which APIs are internal-only?

**Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q1132. Is a public API explicitly prohibited in v1?

**Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q1133. Are browser APIs versioned?

**Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q1134. What error format will the backend expose?

**Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q1135. What validation error format is required?

**Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q1136. How are authorization errors represented?

**Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q1137. How are state-transition errors represented?

**Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q1138. How are concurrency conflicts represented?

**Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q1139. Which API responses must never expose sensitive fields?

**Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q1140. What pagination rules are required?

**Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q1141. What filtering/sorting semantics are required?

**Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q1142. What maximum page sizes are permitted?

**Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q1143. Is API request id/correlation id required?

**Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q1144. Are audit event IDs returned to clients where useful?

**Answer:** Internal application boundaries are service/domain boundaries, not a public API ecosystem; authoritative write path remains application-service controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q1145. What are the mandatory v1 screens?

**Answer:** Mandatory v1 screens: Login; Home/Dashboard; Customer; Request; Sample Registration/Intake; Sample Detail; Test Queue; TestInstance Detail; Result Entry; Review Queue; Verification Queue; Approval Queue; Result/History; Report List/Detail; Report Preview/Issue/Reissue; Equipment; Methods/Test Definitions; QC/Nonconformance; Configuration; Audit/History; Administration/Operational Health.

**Status:** CLOSED — RECONCILED BASELINE



### Q1146. What are the mandatory screens for each role?

**Answer:** Each role gets only the screens/actions appropriate to its permissions. Analyst: intake/assigned work/result entry; Reviewer: review; Verification: verification; Approver: approval; Quality/Technical: quality/configuration oversight; Admin: technical administration without technical approval authority.

**Status:** CLOSED — RECONCILED BASELINE



### Q1147. What is the primary navigation structure?

**Answer:** Primary navigation should be organized around Work, Records, Reports, Quality, Master Data, Administration, with role-based visibility.

**Status:** CLOSED — RECONCILED BASELINE



### Q1148. Which screens are task-oriented queues versus master-data screens?

**Answer:** Queues: Sample/Intake, Assignment, Analyst Work, Review, Verification, Approval, Exceptions/Nonconformance, Operational Alerts. Master-data screens: Customer, Equipment, Methods, TestDefinitions, Parameters, Configuration.

**Status:** CLOSED — RECONCILED BASELINE



### Q1149. Which screens require split view/detail panels?

**Answer:** Yes. Queue/detail pages should support split-view or fast drill-down where it materially improves repetitive operational work.

**Status:** CLOSED — RECONCILED BASELINE



### Q1150. Which forms require autosave?

**Answer:** Sensitive in-progress form state remains in React application memory only in v1; no localStorage or IndexedDB persistence. Retry behavior uses server-side transaction state and idempotency controls.

**Status:** CLOSED — RECONCILED BASELINE



### Q1151. Which forms must use explicit Save?

**Answer:** Controlled forms shall use explicit Save, Submit, or equivalent authoritative actions.
Result entry, configuration changes, corrections, Review, Verification, Approval, report issue/reissue, and other controlled actions shall not depend on implicit browser autosave as the authoritative write mechanism.
Where drafts are permitted, the explicit Save action creates the draft state; Submit or the applicable workflow action advances the record. Browser-side transient data must not be treated as authoritative laboratory evidence.

**Status:** CLOSED — RECONCILED BASELINE



### Q1152. Which forms can be left as drafts?

**Answer:** Drafts allowed for appropriate non-final forms, configuration proposals, report drafts, and other explicitly draft-capable entities. Controlled technical approval states are never “draft.”

**Status:** CLOSED — RECONCILED BASELINE



### Q1153. Which workflows require confirmation dialogs?

**Answer:** Confirmation required for state-changing operations, assignment changes where consequential, rejection, cancellation, reopening, report issue/reissue, approval, and other configured high-risk actions.

**Status:** CLOSED — RECONCILED BASELINE



### Q1154. Which destructive or irreversible actions require strong confirmation?

**Answer:** Destructive/irreversible operations such as permanent deletion where exceptionally permitted, retention destruction, database restore, and similar operations require strong confirmation and authorization.

**Status:** CLOSED — RECONCILED BASELINE



### Q1155. Which high-risk actions require showing the exact record/stage before confirmation?

**Answer:** Yes. High-risk confirmation should display the exact record identity, current state, intended action, and material consequence before confirmation.

**Status:** CLOSED — RECONCILED BASELINE



### Q1156. How are workflow states visually represented?

**Answer:** Workflow states should be visually represented with consistent controlled status labels, badges, and state history; color must not be the only indicator.

**Status:** CLOSED — RECONCILED BASELINE



### Q1157. How are SoD blocks displayed?

**Answer:** SoD blocks should clearly say that the requested action is blocked by role separation and identify the next authorized stage/role where appropriate.

**Status:** CLOSED — RECONCILED BASELINE



### Q1158. How are validation errors displayed?

**Answer:** Validation errors appear inline at field level plus a clear summary for multi-error forms.

**Status:** CLOSED — RECONCILED BASELINE



### Q1159. How are required fields indicated?

**Answer:** Required fields indicated consistently with label markers and accessible explanatory text.

**Status:** CLOSED — RECONCILED BASELINE



### Q1160. How are audit/history views presented?

**Answer:** Audit/history presented as a chronological, immutable event/revision view with actor, timestamp, reason, event type, and related evidence.

**Status:** CLOSED — RECONCILED BASELINE



### Q1161. How are revision comparisons displayed?

**Answer:** Revision comparison should show what changed, old value, new value, actor, timestamp, reason, and revision/event linkage.

**Status:** CLOSED — RECONCILED BASELINE



### Q1162. Must users be able to compare current Result versus historical ResultRevision?

**Answer:** Yes. Users with permission must be able to compare current Result state with historical ResultRevision.

**Status:** CLOSED — RECONCILED BASELINE



### Q1163. Must users be able to compare ReportRevision versions?

**Answer:** Yes. Authorized users must be able to compare ReportRevision versions, including issue/reissue history.

**Status:** CLOSED — RECONCILED BASELINE



### Q1164. How are documents/PDFs previewed?

**Answer:** Documents/PDFs should support in-browser preview where feasible, with controlled download/print access according to permissions.

**Status:** CLOSED — RECONCILED BASELINE



### Q1165. Must users be able to print labels directly from workflow screens?

**Answer:** Yes. Users should be able to print labels directly from applicable workflow screens.

**Status:** CLOSED — RECONCILED BASELINE



### Q1166. Which screens must support barcode scanners without mouse use?

**Answer:** Sample intake/registration and repetitive identification workflows must support scanner entry without requiring mouse interaction.

**Status:** CLOSED — RECONCILED BASELINE



### Q1167. Which screens must be optimized for data-entry speed?

**Answer:** Optimize for speed: Sample Intake, Sample Allocation, Analyst Result Entry, Review, Verification, Approval, and Label Printing.

---

# 45. Report Rendering and Browser/Chromium Stability

**Status:** CLOSED — RECONCILED BASELINE



### Q1168. Which Chromium version is approved for production PDF rendering?

**Answer:** The production PDF-rendering environment shall use a controlled, validated Chromium version recorded in the Report Rendering / PDF Validation Baseline.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1169. How is Chromium installed and updated?

**Answer:** Chromium shall be installed as a controlled production dependency on the designated rendering environment.
The approved Chromium version shall be recorded in the deployment/rendering baseline, installed from a controlled package or approved distribution method, and operated without requiring Internet access during normal report generation.
Chromium updates shall be treated as controlled maintenance changes. The previous approved version and rollback/recovery path shall remain known until the updated version has passed the required rendering verification.

**Status:** CLOSED — RECONCILED BASELINE



### Q1170. How is PDF rendering tested after a Chromium update?

**Answer:** After every approved Chromium update, the system shall execute a controlled PDF rendering regression suite using representative approved report templates and difficult cases.
Testing shall cover, at minimum: page count, page breaks, headers/footers, fonts, tables, long values, abnormal results, attachments, special characters, report revision identifiers, hashes, and overall technical/report content.
A renderer update shall not become production-effective until required regression results are reviewed and accepted. Material rendering changes shall be treated as a release/validation issue rather than silently accepted because the PDF still opens.

**Status:** CLOSED — RECONCILED BASELINE



### Q1171. Must fonts be bundled locally for offline stability?

**Answer:** Yes. Approved report fonts shall be **bundled locally and controlled** for production PDF rendering.
This avoids dependence on Internet availability or uncontrolled host-font substitution and improves rendering reproducibility. The exact font package, version, licensing basis, and supported scripts shall be recorded in the Report Rendering / PDF Validation Baseline.

**Status:** CLOSED — RECONCILED BASELINE



### Q1172. Which fonts are approved for reports?

**Answer:** v1 shall use a **small controlled font set**, with one approved primary report family and only the additional script-specific fonts actually required.
A practical recommended baseline is the **Noto Sans family**, supplemented by the required Noto script variant(s) where non-Latin report content is actually needed. The final approved font names and versions shall be frozen in the Report Rendering / PDF Validation Baseline.
The renderer must not silently substitute arbitrary host fonts for controlled report rendering.

**Status:** CLOSED — RECONCILED BASELINE



### Q1173. Are non-Latin scripts required?

**Answer:** The application and report pipeline shall support Unicode, and non-Latin scripts shall be rendered correctly when such data is legitimately required.
The v1 validation baseline shall therefore include representative Unicode/non-Latin test data at least for stored names, metadata, and any approved report-visible fields. If a specific non-Latin script is required in issued reports, an approved locally bundled font supporting that script shall be included and validated.
The system shall not claim broad script coverage that has not been tested.

**Status:** CLOSED — RECONCILED BASELINE



### Q1174. How are page breaks controlled?

**Answer:** Page breaks shall be controlled through the approved report template/CSS rules and validated against representative report data.
Section headings should remain with their associated content where practicable. Tables and structured result blocks must have controlled page-break behavior. Important sections shall not be split unpredictably, and blank/near-empty pages caused by rendering rules shall be treated as defects.
Long reports must be tested explicitly rather than relying on the renderer's default pagination.

**Status:** CLOSED — RECONCILED BASELINE



### Q1175. How are tables split across pages?

**Answer:** Tables shall use controlled paginated-report behavior.
Table headers shall repeat on continuation pages. Rows should remain together where practicable, while genuinely large content may continue across pages under controlled rendering rules. Columns must not be clipped or silently omitted.
Long-text result cells, notes, and comments shall wrap or continue predictably, and the resulting PDF shall remain readable and reconstructable.

**Status:** CLOSED — RECONCILED BASELINE



### Q1176. How are headers/footers handled?

**Answer:** Headers and footers shall be defined by the controlled report template and applied consistently to every applicable page.
They shall support the approved report identity and page-control requirements, including the report number/revision and page numbering where required. Any issue/revision/status representation shall follow the Report Lifecycle and Composition rules.
Headers and footers must not depend on uncontrolled host configuration or manually inserted text.

**Status:** CLOSED — RECONCILED BASELINE



### Q1177. How are long results handled?

**Answer:** Long results shall never be truncated or silently replaced because they do not fit the expected layout.
The report template shall provide controlled wrapping, continuation, row expansion, or page continuation. Long values and narratives shall be tested using realistic boundary cases.
Where a value cannot be rendered safely within the approved layout, report generation shall fail visibly and controllably rather than issuing an incomplete or misleading PDF.

**Status:** CLOSED — RECONCILED BASELINE



### Q1178. How are abnormal values displayed?

**Answer:** Abnormal values shall preserve the **actual result value and its structured qualifier/status**, with any report flagging applied according to the approved reporting rules.
Visual emphasis may be used, but color alone must never be the only indication of an abnormal condition. The underlying structured value, qualifier, unit, and applicable reference/specification context remain authoritative.
The report must not invent an abnormal classification merely because a value appears unusual.

**Status:** CLOSED — RECONCILED BASELINE



### Q1179. How are report attachments handled in rendering?

**Answer:** Report attachments shall be rendered or packaged only when explicitly included by the approved Report Composition rules.
When included, the exact approved DocumentVersion/file shall be used and its identity, ordering, and integrity shall remain frozen with the ReportRevision. Attachments shall not be silently converted, altered, or replaced merely to make rendering easier.
Where an attachment is not intended to be flattened into the primary report PDF, it shall remain a separately identified report-package artifact linked to the exact issued revision.

**Status:** CLOSED — RECONCILED BASELINE



### Q1180. Are PDF/A or other archival PDF standards required?

**Answer:** PDF/A is **not required for v1 unless separately approved by the laboratory**.
The v1 archival control shall instead rely on preservation of the exact issued PDF bytes, immutable ReportRevision linkage, SHA-256 hash, controlled storage/retention, and verified backup/recovery.
PDF/A or another archival PDF standard may be introduced later through a controlled architectural/report-rendering change if a documented requirement establishes the need.

**Status:** CLOSED — RECONCILED BASELINE



### Q1181. Must PDF metadata include author/laboratory/report number?

**Answer:** The PDF shall contain controlled metadata appropriate to the issued report, including at minimum the laboratory identity and report number/revision where technically supported and useful.
Additional metadata such as author, title, creation timestamp, subject, or keywords may be included where approved. Metadata must not contain unnecessary sensitive information.
The authoritative report identity remains the persisted ReportRevision/report artifact relationship, not PDF metadata alone.

**Status:** CLOSED — RECONCILED BASELINE



### Q1182. Must a content hash be stored?

**Answer:** Yes. The exact issued PDF bytes shall have a **SHA-256 content hash** stored with the corresponding report artifact.
The hash shall be generated from the final persisted PDF bytes and used for integrity verification, backup/restore checking, artifact identity, and evidentiary reconstruction.
Any changed PDF bytes necessarily represent a different artifact and must not overwrite the previously issued artifact.

**Status:** CLOSED — RECONCILED BASELINE



### Q1183. Is digital signing of PDFs required?

**Answer:** Cryptographic digital signing of PDFs is **not required for v1** unless separately approved.
The authoritative approval evidence shall remain the controlled application-side approval chain, linked to the exact ResultRevision/ApprovalSnapshot and ReportRevision. A visible signature representation may be included in the PDF according to approved report policy, but that is distinct from cryptographic PDF signing.
Introducing cryptographic signing later would require a controlled architecture, security, key-management, validation, and operational decision.

**Status:** CLOSED — RECONCILED BASELINE



### Q1184. Is watermarking required for drafts or superseded reports?

**Answer:** Draft/non-issued reports carry the controlled watermark **“DRAFT – NOT ISSUED”**. Issued PDFs are never altered merely because they later become superseded/withdrawn; status is communicated by application state and/or replacement report. Cryptographic PDF signing is not required in v1 unless separately approved.

**Status:** CLOSED — RECONCILED BASELINE



### Q1185. What distinguishes a draft PDF from an issued PDF?

**Answer:** A **draft PDF** is a non-issued rendering associated with a draft or pre-issuance ReportRevision and is not an authoritative issued laboratory report.
An **issued PDF** exists only when the applicable report workflow is complete, the exact artifact has been persisted, its hash has been recorded, artifact integrity has been verified, and the issuance event has been authorized and recorded.
An issued PDF and its ReportRevision shall not be converted back into a draft or silently regenerated in place.

**Status:** CLOSED — RECONCILED BASELINE



### Q1186. Does the laboratory require electronic signatures in the system?

**Answer:** Electronic approval evidence is revalidated server-side in the protected transaction and linked to the exact technical state. Actor, role/competence, timestamp, authentication/reauthentication evidence class and approval-chain event remain reconstructable.

**Status:** CLOSED — RECONCILED BASELINE



### Q1187. What legal/quality meaning should an electronic signature have?

**Answer:** The browser cannot authorize a protected approval by itself. Server-side permission, competence, SoD, timestamp integrity and required evidence must pass; otherwise the action fails closed.

**Status:** CLOSED — RECONCILED BASELINE



### Q1188. Is authenticated session identity sufficient for signature evidence?

**Answer:** An authenticated session identity alone is **not sufficient for the highest-risk signing/approval transaction**.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1189. Is password re-entry required for signing?

**Answer:** Yes. **Password re-entry should be required for high-risk electronic approval/signing actions in v1.**

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1190. Is signature data stored separately from approval_chain_event?

**Answer:** The authoritative signing/approval evidence shall remain in the **`approval_chain_event` model**, rather than creating an independent uncontrolled signature history.
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

**Status:** CLOSED — RECONCILED BASELINE



### Q1191. Must the displayed signature include name, role, date, and time?

**Answer:** Yes. The displayed electronic approval/signature representation should include, at minimum:
* Signatory's controlled name;
* Signatory's role at the time of approval;
* Approval/signing action;
* Date;
* Time;
* Report/TestInstance context where appropriate.

Where useful and approved, the display may also include the approval status and identification of the relevant report revision.
The displayed identity shall come from the **historical approval evidence**, not from the user's current mutable profile. Thus, later changes to a user's name, role, or authorization must not rewrite what was displayed or recorded for a historical approval.

**Status:** CLOSED — RECONCILED BASELINE



### Q1192. Must the PDF contain a visible signature representation?

**Answer:** Yes. The issued PDF should contain a **controlled visible representation of the applicable approval/signature evidence** where the laboratory's approved report format requires it.
The visible representation should normally identify the approving person, role, and approval date/time in a controlled report section.
This visible representation is presentation evidence only. The authoritative approval remains the application-side `approval_chain_event` and linked ApprovalSnapshot/ResultRevision.
The PDF must not be treated as the sole source of approval evidence, and changing the visible representation shall never alter the underlying approval history.

**Status:** CLOSED — RECONCILED BASELINE



### Q1193. Is cryptographic PDF signing required?

**Answer:** Approval/signing evidence remains controlled historical evidence and is not invalidated or erased merely because a user account is later disabled.

**Status:** CLOSED — RECONCILED BASELINE



### Q1194. Is cryptographic signing intentionally out of scope?

**Answer:** Yes. Cryptographic PDF signing is **intentionally out of scope for v1**.

The distinction shall be explicit:
**v1 electronic approval:**
Controlled authenticated application action producing authoritative approval evidence.

**v1 PDF integrity:**
Exact persisted PDF + SHA-256 hash + ReportRevision linkage + controlled storage/backup.

**Cryptographic PDF signature:**
Not implemented in v1 and must not be implied by the visible approval/signature representation.

This prevents the application from accidentally making a legal or technical claim that its visual report signature is a cryptographic digital signature.

**Status:** CLOSED — RECONCILED BASELINE



### Q1195. What happens if a signatory account is later disabled?

**Answer:** If a signatory's account is later disabled, the system shall **not retroactively erase or invalidate historical approval evidence merely because the account is now disabled**.
Historical approval remains evidence of the action performed at the time, provided that the account was authorized and valid when the action occurred.

After disablement:
* The user cannot perform new controlled approval/signing actions;
* Active sessions are invalidated;
* New authorization checks fail;
* Historical approval events remain immutable;
* Historical signer identity remains reconstructable;
* Any later investigation can assess whether the signer was valid at the time of the original action.

If a security investigation establishes that the historical approval itself may have been compromised or improperly authorized, the affected approval/result/report shall be handled through the controlled correction/reopen/nonconformance process. The original approval event must still remain preserved.

**Status:** CLOSED — RECONCILED BASELINE



### Q1196. How is historical signature identity preserved?

**Answer:** Historical signature identity shall be preserved **inside the immutable approval evidence**, independently of the user's current profile.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1197. What timezone is the laboratory's official timezone?

**Answer:** Controlled event times are stored in UTC for ordering; user-facing laboratory displays use **Asia/Kolkata**. Client clocks are not authoritative.

**Status:** CLOSED — RECONCILED BASELINE



### Q1198. Is all server-side storage in UTC?

**Answer:** Yes for **instant timestamps**: server-side/application timestamps shall be stored in UTC.
Date-only values, such as a contractual date or a calendar due date where the business meaning is date-only, shall remain date values rather than being converted into UTC timestamps artificially.
The system shall never store ambiguous naive date-times as though their timezone were known.

**Status:** CLOSED — RECONCILED BASELINE



### Q1199. What timezone is displayed to users?

**Answer:** Normal user-facing timestamps shall be displayed in **Asia/Kolkata**.
Reports, audit/history views, workflow timestamps, and operational records should use the laboratory timezone by default, while UTC may remain available in technical/system views where useful for diagnostics and interoperability.
The displayed timezone shall be explicit where timestamp interpretation could otherwise be ambiguous.

**Status:** CLOSED — RECONCILED BASELINE



### Q1200. How are daylight-saving changes handled if relevant to any environment?

**Answer:** The production laboratory environment shall use `Asia/Kolkata`, so daylight-saving transitions are not expected in the normal v1 operating environment.
The implementation shall nevertheless use timezone-aware conversion through the IANA timezone database rather than hard-coding a numerical offset. This preserves correct behavior if the deployment environment is later changed or if another timezone is formally configured.

**Status:** CLOSED — RECONCILED BASELINE



### Q1201. Is the Windows host time synchronized automatically?

**Answer:** Yes. The Windows host clock shall be synchronized automatically against an **approved time source** where an operationally suitable source is available.
The synchronization method may use the organization's Windows/domain time service or an approved local/on-site time source. Internet access must not be a mandatory dependency.
The synchronization state and significant clock anomalies shall be part of operational health/evidence.

**Status:** CLOSED — RECONCILED BASELINE



### Q1202. Is Internet time synchronization available?

**Answer:** Internet time synchronization shall **not be required** for LabNexus.
The system is offline-first and shall remain operational without Internet connectivity. Where Internet-based synchronization is available, it may be used as an approved time source, but the production baseline shall define a local/domain/on-site alternative.

**Status:** CLOSED — RECONCILED BASELINE



### Q1203. If Internet is unavailable, what time source is used?

**Answer:** When Internet connectivity is unavailable, the Windows host shall use the approved local/domain/on-site time source defined by the deployment baseline.
If no automatic trusted source is available, an authorized administrator shall perform the controlled time-verification/time-setting procedure, with the event recorded as operational evidence.
Approval and report issuance shall not rely on an unknowable or silently drifting system clock.

**Status:** CLOSED — RECONCILED BASELINE



### Q1204. Who can change the Windows server clock?

**Answer:** Only an authorized **Windows/System Administrator** shall be permitted to change the production server clock.
Laboratory users, analysts, reviewers, verifiers, approvers, and ordinary application administrators shall not have operating-system clock-change authority.
Clock changes shall be treated as privileged operational events, with the available Windows/host audit evidence retained and significant changes surfaced to the LabNexus operational monitoring process.

**Status:** CLOSED — RECONCILED BASELINE



### Q1205. What happens if the system clock is incorrect?

**Answer:** If server time moves backward by more than **60 seconds** relative to the latest recorded audit timestamp, approval and report issuance are blocked and an alert is raised.

**Status:** CLOSED — RECONCILED BASELINE



### Q1206. Are time anomalies detected or logged?

**Answer:** Approval and report issuance are blocked when measured clock offset against the approved reference exceeds **2 minutes**; warn above **30 seconds**. The reference is the permitted Windows/LAN source or approved time-only NTP method.

**Status:** CLOSED — RECONCILED BASELINE



### Q1207. Is trusted time evidence required for approval/report issuance?

**Answer:** Only server time is stored for controlled events. Where no permitted automated reference exists, an administrator records a controlled manual check; a warning is raised if no such check exists within 7 days.

**Status:** CLOSED — RECONCILED BASELINE



### Q1208. What response time is acceptable for normal page loads?

**Answer:** Performance acceptance uses defined percentile/upper-bound criteria, controlled workload/concurrency/dataset/environment definitions and explicit inclusion of transaction/audit commit behavior. Evidence must be repeatable.

**Status:** CLOSED — RECONCILED BASELINE



### Q1209. What response time is acceptable for sample search?

**Answer:** Sample search shall target:
**p95 ≤ 1.5 seconds** for normal indexed searches over the representative validation dataset.

Acceptance shall include:
* Common Sample ID search;
* Customer/sample identifier search;
* Date/status filtering;
* Combined filters;
* Representative historical dataset size.

Search results shall be paginated and appropriately indexed.
The acceptance test shall identify both p95 and any materially high worst-case result so that pathological queries are not hidden by averages.

**Status:** CLOSED — RECONCILED BASELINE



### Q1210. What response time is acceptable for result save?

**Answer:** A normal result-save transaction, including required audit/business persistence, shall target:
**p95 ≤ 1 second** under the approved normal concurrency scenario.
The measurement shall include the authoritative backend transaction and its required audit writes, not merely frontend button-response time.
Where result saving triggers an intentionally expensive calculation or PDF/report-generation process, that work should be separated from the ordinary save transaction where architecturally appropriate.

**Status:** CLOSED — RECONCILED BASELINE



### Q1211. What response time is acceptable for queue loading?

**Answer:** Operational queue loading shall target:
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

**Status:** CLOSED — RECONCILED BASELINE



### Q1212. What report-generation time is acceptable for a typical report?

**Answer:** A typical laboratory report shall target:
**p95 ≤ 5 seconds** from report-generation request to successfully persisted/verified PDF artifact under the approved test environment.
The timing must include the controlled PDF-generation process, not just HTML template generation.
Typical-report acceptance data shall represent the normal expected report size and content.
PDF issuance still requires artifact persistence, hashing, verification, and the appropriate authorization controls.

**Status:** CLOSED — RECONCILED BASELINE



### Q1213. What report-generation time is acceptable for a large report?

**Answer:** A large report shall target:
**p95 ≤ 15 seconds** from generation request to persisted/verified PDF artifact under the approved validation environment.
“Large report” shall be defined by a representative controlled test case, such as high TestInstance/result count, multiple pages, long textual fields, tables, and approved attachments where applicable.
The threshold is an acceptance target rather than a universal promise. If the report exceeds the target, the evidence shall identify whether the constraint arises from database retrieval, application rendering, Chromium rendering, storage, or another component.

**Status:** CLOSED — RECONCILED BASELINE



### Q1214. What number of simultaneous writers must be supported?

**Answer:** The v1 performance/capacity acceptance baseline shall support:
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

**Status:** CLOSED — RECONCILED BASELINE



### Q1215. What number of read-only users must be supported?

**Answer:** The performance acceptance baseline shall support **7 simultaneous read-only users in addition to the normal 1–3 simultaneous writers**, giving a normal mixed-workload target of up to approximately **10 active browser users**.
A separate read-heavy test may exercise **10 simultaneous read-only users** to confirm that ordinary searching, dashboards, queues, record viewing, and report retrieval remain usable without writer starvation.
These figures are **validated workload targets, not an absolute system capacity guarantee**. The acceptance record shall identify the tested concurrency, dataset size, hardware, software versions, and observed latency/error results.

**Status:** CLOSED — RECONCILED BASELINE



### Q1216. What sample count must the system support before re-evaluation?

**Answer:** The initial technical performance baseline shall be validated at **250,000 Samples**.
This is a capacity-re-evaluation threshold, not a statement that the system becomes unusable at that point. Before production data approaches this threshold, the laboratory shall perform a documented performance/capacity re-evaluation using the then-current production-like database and hardware.
The longer-term planning reference shall also consider the projected retention workload derived from the approved operating baseline of approximately 100 Samples/day. The projected 10-year count shall be treated as a planning input requiring later validation rather than as an already-proven capacity guarantee.

**Status:** CLOSED — RECONCILED BASELINE



### Q1217. What TestInstance count must the system support?

**Answer:** The initial technical performance baseline shall be validated at **12.5 million TestInstances**, corresponding to 250,000 Samples at the approved peak planning assumption of up to 50 tests per Sample.
The TestInstance acceptance test shall include realistic mixtures of active, completed, corrected, reviewed, verified, approved, and archived records, together with the associated audit, calculation, QC, equipment, and report relationships.
Approaching this threshold shall trigger a documented capacity re-evaluation. The system shall not claim unlimited SQLite capacity or infer long-term capacity solely from row-count arithmetic.

**Status:** CLOSED — RECONCILED BASELINE



### Q1218. What report/document count must the system support?

**Answer:** The initial technical performance baseline shall be validated at **250,000 controlled report/document records**, with the test dataset including Report, ReportRevision, ReportResultSnapshot, DocumentVersion, and issued-PDF relationships as applicable.
The test shall not treat every document as a trivial empty record. Representative document metadata, revision history, report snapshots, and stored issued artifacts shall be present so that retrieval and indexing behavior are meaningful.
Approaching this threshold shall trigger a documented capacity re-evaluation rather than an automatic assumption that additional capacity is guaranteed.

**Status:** CLOSED — RECONCILED BASELINE



### Q1219. What database size should be tested?

**Answer:** The nominal **5 GiB** database target is not a fixed acceptance constraint. Capacity is established from the authorized performance spike using realistic and stress datasets plus measured database growth, latency, throughput and backup behavior.

**Status:** CLOSED — RECONCILED BASELINE



### Q1220. What attachment storage size should be tested?

**Answer:** The initial document-storage performance baseline shall be validated with approximately **25 GiB of controlled application-managed attachments and issued artifacts**, including realistic mixtures of PDFs and other approved document types.
Approaching **50 GiB** of application document storage shall trigger a documented storage/performance/recovery re-evaluation.
The test shall cover file creation, retrieval, integrity verification, report artifact lookup, backup, and restore rather than measuring only raw filesystem throughput. The application shall continue to expose documents through the controlled document model rather than direct arbitrary filesystem paths.

**Status:** CLOSED — RECONCILED BASELINE



### Q1221. What backup duration is acceptable?

**Answer:** The operational performance target for a normal full Recovery Set backup shall be **no more than 30 minutes at p95** under the validated normal workload and production-like storage environment.
The measurement shall cover the complete controlled backup operation required for the Recovery Set, including the SQLite database and controlled document/attachment content required for coherent recovery, together with integrity/manifest work that is part of the normal backup procedure.
A backup completing within the target but producing an invalid or incomplete Recovery Set is a failure. Backup duration shall therefore always be evaluated together with backup integrity and recoverability.

**Status:** CLOSED — RECONCILED BASELINE



### Q1222. What restore duration is acceptable?

**Answer:** The technical target for restoration of a complete validated Recovery Set shall be **no more than 4 hours** from authorized recovery start until the restored system is ready for formal smoke testing.
This is intentionally more stringent than the approved **8-hour overall RTO**, leaving the remaining recovery window for application deployment, integrity checks, authentication verification, report/document verification, and operational acceptance.
The measured restore duration shall be recorded under the actual tested recovery hardware and dataset. It shall not be presented as a universal guarantee across materially different hardware or storage conditions.

**Status:** CLOSED — RECONCILED BASELINE



### Q1223. What performance degradation is acceptable during backup?

**Answer:** During a normal backup, the principal interactive transaction performance measures shall remain within **125% of their pre-backup baseline p95 latency**, unless a separately documented short quiescence interval is explicitly part of the controlled backup procedure.
For example, a 1.0-second normal p95 transaction baseline would permit no more than approximately 1.25 seconds p95 during the measured backup workload.
Backup operation shall not cause unauthorized partial writes, lost audit events, corrupted document references, inconsistent Recovery Sets, or controlled workflow bypass. Any temporary operational impact shall be measured and documented rather than described qualitatively as "minimal."

**Status:** CLOSED — RECONCILED BASELINE



### Q1224. What concurrency scenarios require formal testing?

**Answer:** Formal performance testing shall include at least these mixed scenarios:
1. **Normal workload:** 1–3 simultaneous writers with up to 7 simultaneous read-only users.
2. **Stress workload:** 5 simultaneous writers with 5 simultaneous read-only users.
3. **Mixed transactional workload:** Sample/TestInstance updates, result persistence, review/verification/approval actions, searches, queues, and audit writes occurring together.
4. **Report workload:** normal transactional activity occurring while one or more report-generation operations execute.
5. **Backup concurrency:** approved normal workload occurring during backup.
6. **Burst workload:** concentrated creation/update activity representing operational peaks rather than evenly distributed transactions.

Restore testing shall be treated separately because restoration is a controlled recovery activity performed against a quiesced environment, not an ordinary concurrent-production workload.

**Status:** CLOSED — RECONCILED BASELINE



### Q1225. What hardware configuration will be used for performance testing?

**Answer:** Performance targets are measured criteria for the defined workload/environment, not universal guarantees. Failed targets require technical investigation and controlled disposition/ADR.

**Status:** CLOSED — RECONCILED BASELINE



### Q1226. What representative data set will be used?

**Answer:** The representative performance dataset shall model the approved operating profile and shall contain, at minimum:
* approximately **250,000 Samples**;
* up to approximately **12.5 million TestInstances**;
* approximately **250,000 Report/ReportRevision-level records**;
* approximately **5 GiB SQLite database content**;
* approximately **25 GiB controlled document/attachment content**.

The dataset shall include representative lifecycle distribution rather than only newly created active records. It shall include completed and archived work, result revisions, approval history, report snapshots, audit events, configuration references, QC/equipment relationships, and realistic indexing/selectivity.
Where real laboratory data is unsuitable for testing, controlled synthetic or appropriately anonymized data shall be used. The dataset-generation method and version shall itself be recorded so that the test can be reproduced.

**Status:** CLOSED — RECONCILED BASELINE



### Q1227. What measurements will count as evidence?

**Answer:** Performance evidence shall include measured **p50, p95, and p99 latency where meaningful**, transaction/error counts, concurrency, dataset size, database size, document-store size, CPU utilization, memory utilization, disk utilization, and relevant storage throughput.
The evidence shall separately measure the previously approved acceptance targets for page response, sample search, result save, queue retrieval, normal report generation, large report generation, backup, and restore.
Every performance record shall identify the test date, application/release identifier, database/schema version, SQLite version, operating system, hardware, dataset version/hash where applicable, workload scenario, number of concurrent users, measurement duration, and pass/fail interpretation.
A single favorable measurement is insufficient. Acceptance evidence shall demonstrate the defined scenario over a repeatable test run.

**Status:** CLOSED — RECONCILED BASELINE



### Q1228. Who accepts the performance results?

**Answer:** The **Technical Authority** shall review and technically accept the performance/capacity evidence.
The **Quality Authority** shall verify that the evidence is complete, traceable, repeatable, and consistent with the approved acceptance criteria.
The **Project Owner / Laboratory Business Owner** shall make the final project-level acceptance decision for release or operational use after technical and quality review.
Any failed criterion shall be recorded as a deficiency or exception with documented disposition; it shall not be silently accepted merely because the overall application appears usable.

**Status:** CLOSED — RECONCILED BASELINE



### Q1229. What is the complete test pyramid for v1?

**Answer:** Validation is layered: unit tests → integration tests with real temporary SQLite → API/contract tests → Playwright end-to-end → non-functional performance/recovery → validation → UAT.

### Q1230. Which rules must have unit tests?

**Answer:** Every state-matrix row and every SoD cell is tested. High-risk logic areas target at least 90% branch coverage for SoD, state machine, formula evaluator, numbering and audit; overall coverage is informational.

### Q1231. Which rules must have integration tests?

**Answer:** Only seeded synthetic data is used in test/validation environments. Production data is not copied into them.

### Q1232. Which database constraints must have direct tests?

**Answer:** Verification is independent of implementation. The verifier differs from the implementer; Technical and Quality Authorities validate controlled evidence; laboratory users execute scripted UAT.

### Q1233. Which workflow transitions must have tests?

**Answer:** Evidence includes controlled Markdown records and pytest/Playwright machine-readable reports under the evidence area, with environment, tester, expected/actual result and disposition.

### Q1234. Which SoD rules must have tests?

**Answer:** A checkpoint cannot be accepted with an open defect touching a high-risk requirement; minor deviations require an owner and due date and remain traceable.

### Q1235. Which authorization rules must have tests?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1236. Which calculation formulas must have golden test cases?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1237. Which report templates must have visual/regression tests?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1238. Which PDF artifacts must be compared for stability?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1239. Which migration paths must be tested?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1240. Which backup/restore scenarios must be tested automatically?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1241. Which browser workflows must have Playwright coverage?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1242. What is the minimum required test coverage for critical modules?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1243. Is code coverage a metric, and what is its role?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1244. Which tests are mandatory before a checkpoint can be VERIFIED?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1245. Which tests are mandatory before a checkpoint can be ACCEPTED?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1246. How are test data fixtures controlled?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1247. How are sensitive production data prevented from entering test environments?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1248. Is synthetic data required for validation?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1249. Who defines expected results for critical laboratory calculations?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1250. What exactly must be verified for each major requirement?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1251. What is the difference between implementation testing and formal verification for this project?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1252. Who performs verification?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1253. Who performs system validation?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1254. Who performs UAT?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1255. What evidence format is required for verification?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1256. What evidence format is required for UAT?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1257. What constitutes an acceptable validation deviation?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1258. How are deviations recorded and resolved?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1259. Can a checkpoint be accepted with known minor defects?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1260. If yes, what conditions apply?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1261. What evidence must exist before production deployment?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1262. Which requirements are designated high risk?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1263. What traceability links are required from requirement to test to evidence?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1264. Who owns the traceability matrix?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1265. How are validation changes handled after go-live?

**Answer:** Testing, verification and validation remain distinct; acceptance evidence and high-risk requirements require explicit traceability.
**Status:** CLOSED — BASELINE / JOINT GOVERNANCE
**Primary Closure Artifact / Decision Record:** V&V Plan / Traceability Matrix



### Q1266. Which external requirements are explicitly in scope?

**Answer:** Accreditation scope and clauses must come from controlled laboratory source evidence. LabNexus does not infer accreditation from the existence of a Method/TestDefinition or from developer assumptions.

**Status:** CLOSED — RECONCILED BASELINE



### Q1267. Which laboratory procedures must the software support?

**Answer:** The software shall support laboratory procedures that directly govern controlled LIMS records and workflow, including at minimum:
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

**Status:** CLOSED — RECONCILED BASELINE



### Q1268. Which laboratory procedures remain outside the software?

**Answer:** Procedures that remain outside the v1 LIMS unless separately approved include physical laboratory work that has no required system transaction, detailed instrument operating procedures, field sampling/collection workflows, general procurement/accounting/payroll/HR processes, and broader QMS activities that do not require LIMS-controlled records.
The boundary shall be defined from the laboratory's actual SOP/process inventory rather than from a generic assumption about what a LIMS should contain.

**Status:** CLOSED — RECONCILED BASELINE



### Q1269. Which requirements are mandatory because of accreditation or contractual obligations?

**Answer:** Requirements shall be classified as mandatory because of accreditation or contractual obligations only when an authoritative applicability record establishes the relationship.
The Applicability Register shall identify the specific source requirement, effective version/date, affected LIMS behavior or evidence, affected scope, and approving authority.
The system shall not label a requirement “regulatory” merely because it is considered good practice or desirable.

**Status:** CLOSED — RECONCILED BASELINE



### Q1270. Which requirements are laboratory policy choices rather than external requirements?

**Answer:** Laboratory policy choices are requirements adopted by the laboratory that are not being claimed as externally mandated.
Examples include laboratory retention periods where chosen as policy, specific SoD hard blocks, required reasons for exceptional actions, workflow conventions, numbering formats, backup schedules, operational escalation rules, and local approval arrangements.
Each such rule should be identified as a Laboratory Policy in the requirements/decision register so that policy is not confused with external compliance.

**Status:** CLOSED — RECONCILED BASELINE



### Q1271. Which requirements are technical implementation choices?

**Answer:** Technical implementation choices are decisions made to implement the approved laboratory requirements and policies.
Examples include the frozen React/TypeScript/Vite/MUI frontend, FastAPI/Python backend, SQLAlchemy, SQLite, Alembic, secure server-side sessions, Caddy, Jinja2/Chromium report rendering, and the modular-monolith architecture.
Technical choices must not silently redefine laboratory policy or external requirements. Where a technical constraint materially changes behavior, it requires the appropriate change/decision process.

**Status:** CLOSED — RECONCILED BASELINE



### Q1272. What is the source document for each important laboratory rule?

**Answer:** Every important laboratory rule shall have a traceable authoritative source in the Regulatory / External Source Applicability Register or the applicable controlled internal requirements/policy register.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1273. Which procedures need to be revised because of the LIMS?

**Answer:** LIMS introduction should trigger a controlled review of procedures whose execution, records, responsibilities, or evidence change because of the system.
The likely affected procedures include sample receipt/registration, sample allocation, TestInstance execution, result recording, Review/Verification/Approval, result correction/reopen, report issuance/reissue, equipment/QC controls, nonconforming work, user access/SoD, configuration/change control, document/record control, backup/recovery, and historical migration where applicable.
The exact SOP list shall come from the laboratory's controlled QMS document inventory; the system must not invent document numbers or claim revisions that have not been approved.

**Status:** CLOSED — RECONCILED BASELINE



### Q1274. Who approves those procedural changes?

**Answer:** Procedural changes shall be approved through the laboratory's established document/QMS authority.
For laboratory technical procedures, the responsible Laboratory Technical Authority shall provide technical concurrence as required. The Laboratory Quality Authority/Document Control function shall approve controlled procedural changes according to the laboratory's governance.
System administrators or developers may implement approved changes in the LIMS, but technical/software implementation authority does not itself authorize a change to laboratory procedure.

**Status:** CLOSED — RECONCILED BASELINE



### Q1275. Which controlled SOPs must exist before go-live?

**Answer:** Before go-live, the laboratory shall have approved controlled SOPs/work instructions covering all LIMS-controlled operational behaviors needed for safe use.
At minimum this should cover the laboratory's actual procedures for sample intake/registration, TestInstance execution, result entry, Review/Verification/Approval, corrections/reopen/rework, reporting, QC/nonconforming work, user access and SoD, configuration/change control, document/record retention, backup/recovery, and any approved migration activity.
Only the procedures actually applicable to the laboratory need to be included; the requirement is completeness of the controlled operational boundary, not creation of unnecessary documents.

**Status:** CLOSED — RECONCILED BASELINE



### Q1276. Which work instructions must exist for LIMS users?

**Answer:** Role-specific LIMS work instructions shall exist for the controlled activities users must perform.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1277. Which records must be retained as quality evidence outside the application itself?

**Answer:** Records that remain outside LabNexus shall be identified in a controlled **Quality Evidence / Record Retention Matrix** rather than assumed to be part of the application.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1278. Is a validation master plan required?

**Answer:** A **Validation Master Plan or equivalent controlled validation plan is required for v1**, provided that the laboratory's final QMS terminology permits either the formal VMP name or an equivalent controlled validation-planning document.
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

**Status:** CLOSED — RECONCILED BASELINE



### Q1279. Is a computerized-system validation package required by laboratory policy?

**Answer:** The laboratory should maintain a **controlled computerized-system validation package** for LabNexus as the consolidated evidence set demonstrating that the system is fit for its intended use.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1280. Are risk assessments required?

**Answer:** Yes. **Risk assessments are required** for LabNexus and shall be part of the controlled project and validation evidence.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1281. Who signs off the compliance mapping?

**Answer:** Compliance mapping shall be approved by the **Laboratory Quality/Accreditation Authority**, with Technical Authority concurrence where the mapping involves technical or method-specific interpretation.
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

**Status:** CLOSED — RECONCILED BASELINE



### Q1282. What are the primary security threats for this deployment?

**Answer:** The v1 security architecture remains offline-capable. Exact fixed security values are those explicitly controlled in the security baseline; any future changes require controlled approval and validation.

**Status:** CLOSED — RECONCILED BASELINE



### Q1283. Is the server physically secured?

**Answer:** Yes. The production Windows host shall be physically secured in a location accessible only to authorized personnel.

The physical-security baseline should include:
* Restricted access to the server/host location;
* Protection against unauthorized removal or tampering;
* Controlled access to removable backup media;
* Appropriate protection against accidental power loss and environmental hazards;
* Physical access restricted to authorized technical/operational personnel;
* A documented procedure for physical access where the laboratory's QMS requires such evidence.

The exact room, lock, access-control mechanism, UPS capacity, and environmental provisions are deployment inputs and shall be recorded in the Deployment/Operational Security Baseline rather than invented by the software.
Physical security remains part of the LabNexus security boundary; application controls alone cannot protect a host that is physically unrestricted.

**Status:** CLOSED — RECONCILED BASELINE



### Q1284. Who can log into Windows on the host?

**Answer:** Windows interactive login to the production host shall be restricted to **authorized technical/system-administration personnel**.
Ordinary laboratory users shall operate LabNexus through the browser and shall not require Windows login access to the production server merely to perform laboratory work.
The Windows access list shall be separately controlled from LabNexus application roles. Possession of a LabNexus laboratory role shall not automatically grant Windows host access.
Service accounts used by application components shall not be used as ordinary human login accounts.

**Status:** CLOSED — RECONCILED BASELINE



### Q1285. Who has local administrator privileges?

**Answer:** Local Administrator privileges shall be limited to the **designated System Administrator(s)** and only where technically required.

The baseline should use:
* Least privilege;
* Separate named administrative identities rather than shared administrator accounts where practicable;
* No local-administrator rights for ordinary laboratory users;
* No assumption that application administration equals Windows administration;
* Controlled approval for adding/removing local administrators;
* Auditable administrative changes.

The number of privileged Windows administrators shall be kept to the minimum operationally necessary, with an approved backup/alternate administrator where required for recoverability.

**Status:** CLOSED — RECONCILED BASELINE



### Q1286. Are laboratory users prevented from using Windows administrator accounts?

**Answer:** Yes. Laboratory users shall use **standard Windows/user identities** and shall not routinely operate the production host under Windows Administrator accounts.
The LIMS application must not depend on laboratory users having local administrative privileges.
This separation is important because application RBAC/SoD and Windows host privilege are different control layers. A user being authorized to perform technical laboratory work in LabNexus does not authorize direct operating-system administration.

**Status:** CLOSED — RECONCILED BASELINE



### Q1287. Can users access the SQLite file directly?

**Answer:** Ordinary users shall **not have direct access to the SQLite database file**.

The authoritative access path shall be:
**Browser → Caddy → FastAPI application → SQLAlchemy/SQLite**

Direct opening, editing, copying, replacing, or modifying the live SQLite database by ordinary users is prohibited.
Authorized System Administrators may have controlled filesystem access for backup, recovery, maintenance, or incident handling where required, but direct manipulation of production records outside the application shall not be a normal operational method.
The security baseline shall explicitly acknowledge that LabNexus cannot guarantee protection against a person who already has unrestricted Windows/filesystem access. Host permissions therefore form part of the overall security boundary.

**Status:** CLOSED — RECONCILED BASELINE



### Q1288. Can users access the document storage directories directly?

**Answer:** Ordinary users shall **not have direct filesystem access to the application-controlled document/attachment storage directories**.
Documents shall be accessed through authorized LabNexus workflows. The application shall resolve internal document identities to storage objects and shall not expose arbitrary filesystem paths.
Direct filesystem access shall be restricted to authorized technical/administrative personnel for controlled backup, recovery, maintenance, or incident handling.
The storage hierarchy shall not be treated as a user-facing document repository whose files can be freely renamed, replaced, or deleted outside the application.

**Status:** CLOSED — RECONCILED BASELINE



### Q1289. Is remote desktop allowed to the server?

**Answer:** Remote Desktop should be **disabled for ordinary laboratory use** and allowed only where a documented technical/administrative need exists.

Recommended v1 policy:
* No RDP access for ordinary laboratory users;
* RDP permitted only for authorized System Administrators/technical maintainers;
* Access restricted to the approved LAN/administrative environment;
* Strong Windows authentication and account controls;
* RDP activity covered by the host security baseline;
* Temporary exceptional access explicitly authorized and documented where required.

Remote administration must not become a substitute for application workflows or create an undocumented secondary administrative pathway.

**Status:** CLOSED — RECONCILED BASELINE



### Q1290. Who is allowed to use remote desktop?

**Answer:** RDP access shall be limited to designated **System Administrators and, where separately approved, authorized technical maintainers** whose duties require host administration.
Laboratory Analysts, Reviewers, Verifiers, Approvers, Quality users, and ordinary application administrators shall not receive RDP rights merely because they hold those LabNexus roles.
RDP authorization shall be independently managed at the Windows/network security layer and should be reviewed periodically.

**Status:** CLOSED — RECONCILED BASELINE



### Q1291. Is removable media access restricted on the server?

**Answer:** Yes. Removable-media access on the production server shall be **restricted and controlled**, but not necessarily prohibited because the approved operating model includes offline/removable backup capability.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1292. Are USB devices used for backup?

**Answer:** Yes. USB/removable media may be used for **controlled offline backup and recovery activities**, consistent with the approved Backup/Recovery Baseline.

The process shall distinguish:
**Backup Created → Backup Validated → Backup Stored → Backup Restorable → Restore Tested**

Backup media shall not be treated as trustworthy merely because the file was successfully copied.
Each backup medium should have controlled identification, integrity verification, retention/disposition rules, appropriate confidentiality protection, and documented custody.

**Status:** CLOSED — RECONCILED BASELINE



### Q1293. What malware/antivirus controls are available?

**Answer:** The production Windows host shall use the organization's **approved local Windows malware/antivirus protection**, with Microsoft Defender/Windows Security being the expected v1 baseline where that is the organization's approved Windows security control.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1294. Can antivirus quarantine or lock database/document files?

**Answer:** Yes. Antivirus software may quarantine or temporarily lock files required by LabNexus, including database/document files, and the deployment must account for that possibility.

The system shall therefore:
* Monitor relevant security/operational failures where practicable;
* Avoid unsafe assumptions that files are always immediately available;
* Use short database write transactions and retry behavior appropriate to transient file/database contention;
* Treat quarantine or file-access failure as an operational incident requiring controlled investigation;
* Never silently replace or reconstruct a protected file merely because antivirus access failed.

Any antivirus exclusion shall be a separately controlled decision under Q1295.

**Status:** CLOSED — RECONCILED BASELINE



### Q1295. How will database/file exclusions be handled safely, if required?

**Answer:** Security exclusions shall **not be used by default**.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1296. How are secrets protected?

**Answer:** Production secrets shall be protected using **OS-controlled access and a protected deployment secret mechanism**, not source code, Git, ordinary configuration files, or database tables containing plaintext secrets.

Secrets shall be:
* Stored outside the repository;
* Restricted to the process/administrative identities that require them;
* Protected by Windows filesystem/OS controls and, where practical, Windows DPAPI or an equivalent OS-protected mechanism;
* Never displayed through the ordinary LabNexus UI;
* Excluded from logs, error responses, audit payloads, and diagnostic dumps;
* Backed up/recovered only through a controlled secret-recovery procedure where necessary.

No HSM is required for v1.

**Status:** CLOSED — RECONCILED BASELINE



### Q1297. Which secrets exist in v1?

**Answer:** The v1 secret inventory shall be limited to actual secrets required by the implementation.

Expected categories include:
* Session/application secret material;
* CSRF or equivalent application security secret material if separately required by implementation;
* SMTP credentials only if email is implemented;
* Backup-encryption key material if encrypted backups are implemented;
* Any Windows/service credentials required by deployment;
* Other external-system credentials only if separately approved integrations exist.

User passwords shall never be stored as plaintext; LabNexus stores Argon2id password hashes and associated password-verification data.
Ordinary identifiers, report numbers, user IDs, role names, configuration IDs, and other non-secret values shall not be treated as secrets unnecessarily.

**Status:** CLOSED — RECONCILED BASELINE



### Q1298. Where are session secrets stored?

**Answer:** Session secret material shall be stored in the **protected deployment secret mechanism on the production host**, accessible to the LabNexus application process but not to ordinary laboratory users.
The preferred v1 implementation is an OS-protected secret/configuration mechanism using Windows filesystem ACLs and, where appropriate, Windows DPAPI protection.
Session secrets shall not be stored in the SQLite database, committed to Git, embedded in frontend JavaScript, or exposed through API responses.
Changing the session secret shall be treated as a controlled security operation because it may invalidate existing sessions.

**Status:** CLOSED — RECONCILED BASELINE



### Q1299. Where are SMTP credentials stored if email is implemented?

**Answer:** If SMTP/email functionality is not implemented in v1, **no SMTP credentials shall exist in the system**.
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

**Status:** CLOSED — RECONCILED BASELINE



### Q1300. How are backup encryption keys stored?

**Answer:** Backup encryption keys shall be protected **separately from the backup media they protect**.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1301. How are secrets rotated?

**Answer:** Secret rotation shall be **event-driven and policy-controlled**, rather than based on an arbitrary universal interval.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1302. Who can read production secrets?

**Answer:** Production secrets shall be readable only by the **minimum technical identities required to operate or recover the system**.

The preferred access model is:
* LabNexus application/service identity: runtime use without human display;
* Authorized System Administrator: controlled maintenance/recovery access where operationally necessary;
* Designated technical maintainer: access only where explicitly required and authorized;
* Ordinary laboratory users: no access;
* Application administrators: no secret visibility merely because they administer LabNexus roles.

The system shall avoid a design in which any person who can administer ordinary laboratory configuration can read production secrets.
Secret retrieval/use shall be logged where practicable, but the secret value itself shall never be logged.

**Status:** CLOSED — RECONCILED BASELINE



### Q1303. Are security logs separate from laboratory audit records?

**Answer:** Yes. **Security/operational logs and laboratory audit records shall remain distinct evidence classes**, while allowing controlled cross-reference.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1304. What incident-response steps apply to suspected compromise?

**Answer:** Suspected compromise shall trigger a controlled incident-response procedure:
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

**Status:** CLOSED — RECONCILED BASELINE



### Q1305. What happens if an administrator account is compromised?

**Answer:** If a Windows/System Administrator account is compromised, treat the event as a **high-severity privileged security incident**.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1306. What happens if a user's password is compromised?

**Answer:** If a user's password is suspected to be compromised, the account shall be **immediately contained through application access controls**.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1307. Is account disablement an immediate action?

**Answer:** Yes. **Application account disablement shall take effect immediately for new and subsequent controlled actions**, subject only to the technical timing required to terminate active sessions reliably.

When a user is disabled, the system shall:
* Mark the account inactive/disabled;
* Reject subsequent authentication;
* Invalidate active sessions;
* Block new controlled business actions;
* Re-evaluate authorization at the backend for sensitive transactions;
* Preserve all previously recorded history.

A user who was authorized yesterday must not remain capable of performing new Approval, Verification, Correction, Configuration, or other controlled actions merely because an old browser session remains open.
Windows-account disablement shall be handled by the OS administration procedure and should be performed immediately where a host-level account compromise or personnel-security event requires it.

**Status:** CLOSED — RECONCILED BASELINE



### Q1308. Is security incident evidence retained?

**Answer:** Yes. Security-incident evidence shall be **retained as controlled evidence**, especially where the incident affects laboratory records, confidentiality, authorization, system integrity, or recovery.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1309. What customer information is confidential?

**Answer:** For v1, the following shall be treated as **laboratory-confidential customer information unless explicitly designated otherwise under an approved policy**:
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

**Status:** CLOSED — RECONCILED BASELINE



### Q1310. What personal information is stored about users?

**Answer:** User data should be minimized to what is operationally required: name, username, role/authorization, staff ID where applicable, contact information if required, competence/training references, and audit identity.

**Status:** CLOSED — RECONCILED BASELINE



### Q1311. What personal information is stored about customer contacts?

**Answer:** Customer-contact data should be limited to information actually needed for communication/customer records.

**Status:** CLOSED — RECONCILED BASELINE



### Q1312. Is personal data minimization required?

**Answer:** Yes. Data minimization is required.

**Status:** CLOSED — RECONCILED BASELINE



### Q1313. Which roles may see customer contact information?

**Answer:** Customer contact information visible only to roles that require it, primarily authorized administrative/customer-management and relevant supervisory roles.

**Status:** CLOSED — RECONCILED BASELINE



### Q1314. Which roles may see technical results?

**Answer:** Technical results visible to authorized technical/operational roles; access must be role- and workflow-controlled.

**Status:** CLOSED — RECONCILED BASELINE



### Q1315. Are there confidentiality classifications for samples/results/reports?

**Answer:** Customer-specific confidentiality restrictions are an additional authorization axis and are included in v1 only where explicitly approved. They must combine with role/permission without weakening core SoD.

**Status:** CLOSED — RECONCILED BASELINE



### Q1316. Are any results commercially sensitive beyond ordinary laboratory confidentiality?

**Answer:** Yes. The laboratory should support the classification of some results as **commercially sensitive beyond ordinary laboratory confidentiality**, but the classification must be explicitly defined by laboratory policy rather than inferred by the application.
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

**Status:** CLOSED — RECONCILED BASELINE



### Q1317. Are special customer restrictions required?

**Answer:** Special customer restrictions shall be **supported only through an explicitly approved customer-specific confidentiality/access policy**; they shall not be assumed for every customer.

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

**Status:** CLOSED — RECONCILED BASELINE



### Q1318. Are report downloads audited?

**Answer:** Yes. Report downloads should be auditable where the application controls the download.

**Status:** CLOSED — RECONCILED BASELINE



### Q1319. Are exports audited?

**Answer:** Yes. Exports should be auditable, including user, time, export type/filter context where appropriate.

**Status:** CLOSED — RECONCILED BASELINE



### Q1320. How are printed reports controlled?

**Answer:** Printed reports must be controlled through role authorization and report issuance status; the application should record printing where technically observable through the controlled workflow, but cannot guarantee physical handling after printing.

**Status:** CLOSED — RECONCILED BASELINE



### Q1321. How are backup copies protected from unauthorized access?

**Answer:** Backup media protected through encryption, access control, physical security, separated storage, and controlled custody.

**Status:** CLOSED — RECONCILED BASELINE



### Q1322. What is the approved process for removing personal data where legally required, if ever?

**Answer:** Any legally required removal/minimization of personal data must use a controlled privacy/legal process and must not casually delete immutable laboratory history.

**Status:** CLOSED — RECONCILED BASELINE



### Q1323. How does that interact with immutable laboratory history?

**Answer:** Immutable laboratory history remains authoritative. Where privacy law requires alteration/removal, the system must use a controlled/redaction/anonymization mechanism that preserves necessary audit/history integrity and records why the change occurred.

---

# 54. Export, Import, and Reporting Outside the LIMS

**Status:** CLOSED — RECONCILED BASELINE



### Q1324. What data may be exported?

**Answer:** Bulk export is a privileged/high-impact action: permission-controlled, filtered and audited. Lists use CSV/XLSX and reports use PDF. Each export records scope/filter context and row count; raw table-dump endpoints are prohibited.

### Q1325. Who may export it?

**Answer:** Bulk export is privileged/high-impact and must be authorization- and audit-controlled.
**Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Security Baseline



### Q1326. Which formats are required: CSV, Excel, PDF, other?

**Answer:** Bulk export is privileged/high-impact and must be authorization- and audit-controlled.
**Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Security Baseline



### Q1327. Are exports filtered by user permission?

**Answer:** Bulk export is privileged/high-impact and must be authorization- and audit-controlled.
**Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Security Baseline



### Q1328. Must exports include audit/provenance metadata?

**Answer:** Bulk export is privileged/high-impact and must be authorization- and audit-controlled.
**Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Security Baseline



### Q1329. Are bulk exports required?

**Answer:** Bulk export is privileged/high-impact and must be authorization- and audit-controlled.
**Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Security Baseline



### Q1330. Are bulk exports audited?

**Answer:** Bulk export is privileged/high-impact and must be authorization- and audit-controlled.
**Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Security Baseline



### Q1331. Is direct database export prohibited for ordinary users?

**Answer:** Bulk export is privileged/high-impact and must be authorization- and audit-controlled.
**Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Security Baseline



### Q1332. Is an administrator data export function required?

**Answer:** Bulk export is privileged/high-impact and must be authorization- and audit-controlled.
**Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Security Baseline



### Q1333. Is there a controlled import function after go-live?

**Answer:** Bulk export requires a dedicated permission where classified as high impact and records who exported what scope and when, subject to confidentiality and authorization controls.

### Q1334. How are imported records validated?

**Answer:** Imports are controlled by explicit approved types; no generic spreadsheet-to-database bypass.
**Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Import Control / Migration Provenance Contract



### Q1335. How are external IDs mapped to internal IDs?

**Answer:** Imports are controlled by explicit approved types; no generic spreadsheet-to-database bypass.
**Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Import Control / Migration Provenance Contract



### Q1336. Is charge calculation definitely required in v1?

**Answer:** The v1 commercial boundary excludes charge calculation and pricing/rate behavior. No Rate/CustomerRate entities or charge fields are implemented unless a later approved commercial scope change authorizes them.

**Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record



### Q1337. Which chargeable units exist?

**Answer:** No v1 chargeable-unit model is required because charge calculation is deferred. A future commercial decision shall define the unit basis before implementation.

**Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record



### Q1338. Is pricing per test, sample, request, report, or another basis?

**Answer:** Pricing basis (test/sample/request/report/other) is **deferred from v1**. No commercial charging logic shall be implemented by inference.

**Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record



### Q1339. Are rates customer-specific?

**Answer:** Customer-specific rates are **deferred from v1**. Future customer pricing shall require an approved commercial decision and controlled effective-dated configuration.

**Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record



### Q1340. Are rates method-specific?

**Answer:** Invoices, accounts receivable, payments, banking and tax/accounting remain outside LabNexus.

**Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record



### Q1341. Are rates discipline-specific?

**Answer:** Discipline-specific rates are **deferred from v1**. No discipline/rate linkage is required in the controlled v1 LIMS baseline.

**Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record



### Q1342. Are rates effective-dated?

**Answer:** Effective-dated rates are not required in v1 because rates themselves are deferred. Any future rate implementation shall use effective-dated versioning.

**Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record



### Q1343. Can discounts be applied?

**Answer:** Discounts are **out of v1 scope**. No discount engine or discount configuration shall be implemented.

**Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record



### Q1344. Who approves discounts?

**Answer:** Discount approval is **out of v1 scope**. No discount-approval workflow is required.

**Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record



### Q1345. Can charges be overridden?

**Answer:** Charge overrides are **out of v1 scope**. No commercial override mechanism shall be implemented.

**Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record



### Q1346. What audit evidence is required for price overrides?

**Answer:** Price-override audit evidence is **out of v1 scope** because price overrides are not implemented. If later approved, override actor, reason, authorization, previous value, new value, timestamp, and effective scope shall be auditable.

**Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record



### Q1347. Are taxes calculated inside LIMS or outside?

**Answer:** Tax calculation remains **external to LabNexus v1**. The LIMS shall not become the authoritative tax/accounting system.

**Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record



### Q1348. Is a tax rate merely displayed or legally calculated?

**Answer:** No legally authoritative tax calculation is performed in LabNexus v1. Any future display-only tax information shall be explicitly classified as reference data and not represented as accounting authority.

**Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record



### Q1349. Is invoicing intentionally external?

**Answer:** Yes. Invoicing is intentionally **external to the v1 LIMS**. The LIMS may later store controlled external invoice references if separately approved.

**Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record



### Q1350. Is invoice number stored for reference only?

**Answer:** An invoice number is not required in the v1 controlled laboratory model. A future external-invoice reference field may be added through controlled change without making LabNexus the invoicing system.

**Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record



### Q1351. Is payment status stored?

**Answer:** Payment status is **out of v1 scope**. Payment processing and accounts receivable remain external.

**Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record



### Q1352. Is that information read-only/reference-only from an external system?

**Answer:** Any future invoice/payment information presented in LabNexus shall be reference-only data from the approved external business system unless a separate scope change is authorized.

**Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record



### Q1353. Are commercial calculations part of the report?

**Answer:** Commercial calculations are **not part of the v1 technical report authority**. Issued reports shall remain focused on controlled laboratory results and approved report content; commercial information may be introduced later only by explicit report-content approval.

**Status:** CLOSED — SAFE TO DEFER — COMMERCIAL OUT OF V1
**Primary Closure Artifact / Decision Record:** Commercial Scope Decision Record



### Q1354. Which user groups require training?

**Answer:** Training and competence are deployment/validation responsibilities, not an HR subsystem. Required competency evidence is represented through the controlled competence model where applicable; detailed training records remain external/referenceable.

### Q1355. Who will train users?

**Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model



### Q1356. What training records must be retained?

**Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model



### Q1357. Must users pass a competency assessment before using the LIMS for controlled work?

**Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model



### Q1358. Which roles require role-specific competency?

**Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model



### Q1359. Must user competency be linked to system permissions?

**Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model



### Q1360. What happens when a user is not competent or their training expires?

**Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model



### Q1361. Can an inactive/expired competency automatically block specific actions?

**Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model



### Q1362. Who updates training/competency records?

**Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model



### Q1363. Are training records managed inside the LIMS or outside?

**Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model



### Q1364. Is user documentation required in the application?

**Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model



### Q1365. Are tooltips/help text required?

**Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model



### Q1366. Is a local user manual required before go-live?

**Answer:** Retain minimum LIMS-relevant training/competence evidence; do not build full HR/training management without separate approval.
**Status:** CLOSED — SCOPE GUARDRAIL
**Primary Closure Artifact / Decision Record:** Competence / Authorization Model



### Q1367. Who maintains the system after go-live?

**Answer:** Post-go-live maintenance: designated LIMS technical maintainer/developer + System Administrator, with Laboratory Quality/Technical Authority governing laboratory configuration changes.

**Status:** CLOSED — RECONCILED BASELINE



### Q1368. Who owns bug fixes?

**Answer:** Bug fixes owned by the software technical maintainer/developer. Laboratory policy defects remain laboratory-owned requirements.

**Status:** CLOSED — RECONCILED BASELINE



### Q1369. Who owns security updates?

**Answer:** Security updates owned by the technical maintainer/System Administrator, with vulnerability assessment and controlled release.

**Status:** CLOSED — RECONCILED BASELINE



### Q1370. Who owns database migrations?

**Answer:** Database migrations owned by the technical maintainer and executed by the authorized System Administrator through controlled deployment.

**Status:** CLOSED — RECONCILED BASELINE



### Q1371. Who approves production changes?

**Answer:** Production changes require approval by the appropriate authority: technical changes by designated technical/project authority; laboratory-rule changes by Laboratory Quality/Technical Authority; high-impact changes may require joint approval.

**Status:** CLOSED — RECONCILED BASELINE



### Q1372. What is the maintenance window?

**Answer:** Maintenance window: planned and communicated, preferably outside active laboratory operating periods. Exact clock/date is deployment-specific.

**Status:** CLOSED — RECONCILED BASELINE



### Q1373. How are emergency fixes handled?

**Answer:** Every production change follows Task → test → evidence → release. Emergency software changes, laboratory configuration changes and operational recovery are separately classified but all require explicit authorization, risk/scope documentation, appropriate pre-change protection, verification and retrospective review.

### Q1374. How are normal fixes handled?

**Answer:** Separate emergency software/security fixes, emergency laboratory configuration changes and emergency operational recovery; every emergency change is explicitly authorized and evidenced.
**Status:** CLOSED — SOURCE CORRECTION
**Primary Closure Artifact / Decision Record:** Change / Release Governance



### Q1375. Must every production change use the Phase → Work Package → Task → Evidence model?

**Answer:** Emergency changes cannot bypass hard SoD, erase audit history or silently alter controlled behavior. The resulting state must be reconciled to the normal controlled baseline through the applicable change/decision process.

### Q1376. How are changes to frozen architecture approved?

**Answer:** Frozen architecture changes require formal change request, impact assessment, ADR, risk assessment, affected requirements/traceability review, approval, testing, and updated architecture baseline.

**Status:** CLOSED — RECONCILED BASELINE



### Q1377. How are schema changes reviewed?

**Answer:** Schema changes require migration design, compatibility analysis, backup/recovery assessment, migration tests, rollback/recovery plan, affected-report/history assessment, and verification.

**Status:** CLOSED — RECONCILED BASELINE



### Q1378. How are report-template changes reviewed?

**Answer:** Report-template changes require template versioning, content/configuration review, sample PDF regression, impact assessment on issued/historical reports, approval, and release.

**Status:** CLOSED — RECONCILED BASELINE



### Q1379. How are workflow changes reviewed?

**Answer:** Workflow changes require state-model impact analysis, SoD/authorization analysis, historical-state compatibility analysis, automated tests, UAT, approval, and release.

**Status:** CLOSED — RECONCILED BASELINE



### Q1380. How are permission changes reviewed?

**Answer:** Permission changes require authorization-matrix impact review, SoD review, security testing, approval, and audit of the effective change.

**Status:** CLOSED — RECONCILED BASELINE



### Q1381. How are formula changes reviewed?

**Answer:** Formula changes require new FormulaVersion, technical review, golden test cases, controlled effective date, provenance, approval, and impact assessment on future vs historical calculations.

**Status:** CLOSED — RECONCILED BASELINE



### Q1382. How are accreditation changes reviewed?

**Answer:** Accreditation changes require configuration/version update, effective dates, scope mapping, impact assessment, report-impact analysis, and technical/quality approval.

**Status:** CLOSED — RECONCILED BASELINE



### Q1383. How are backup/recovery changes reviewed?

**Answer:** Backup/recovery changes require risk assessment, backup/restore testing, validation of RPO/RTO, documentation update, and approval before production use.

**Status:** CLOSED — RECONCILED BASELINE



### Q1384. How are changes validated before release?

**Answer:** All production changes must be validated at the appropriate test level before deployment. Critical changes require full regression/validation proportional to risk.

**Status:** CLOSED — RECONCILED BASELINE



### Q1385. How are old migrations retained?

**Answer:** Old migrations remain permanently retained in the repository/release history and are never rewritten after production use.

**Status:** CLOSED — RECONCILED BASELINE



### Q1386. How is backward compatibility handled for report/history reconstruction?

**Answer:** Historical reconstruction remains supported through immutable revisions, versioned configurations, frozen ReportResultSnapshots, ApprovalSnapshots, DocumentVersions, and migration history. Changes must not make prior reports dependent on current mutable configuration.

**Status:** CLOSED — RECONCILED BASELINE



### Q1387. How is long-term Chromium/browser compatibility managed?

**Answer:** Maintain Chromium compatibility through controlled version pinning, regression testing, and explicit supported-version records.

**Status:** CLOSED — RECONCILED BASELINE



### Q1388. How is Python dependency maintenance managed?

**Answer:** Python dependencies are pinned/locked, security-reviewed, upgraded in controlled maintenance work, regression-tested, and released only after validation.

**Status:** CLOSED — RECONCILED BASELINE



### Q1389. How is frontend dependency maintenance managed?

**Answer:** Frontend dependencies are pinned/locked and upgraded through controlled dependency-maintenance tasks with browser/UI regression testing.

**Status:** CLOSED — RECONCILED BASELINE



### Q1390. How are security vulnerabilities assessed and patched offline?

**Answer:** Security vulnerabilities assessed from vendor advisories/security databases available to the maintenance team; fixes obtained through approved offline transfer where Internet is unavailable; severity/risk assessed and patches tested before deployment.

---

# 58. Repository and Documentation Contract

**Status:** CLOSED — RECONCILED BASELINE



### Q1391. What is the exact repository structure at project start?

**Answer:** The canonical project-control structure is `constitution.md`, `requirements.md`, `scope.md`, `architecture.md`, `domain-model.md`, `security.md`, `roadmap.md`, `current-state.md`, `active-task.md`, `handoff.md`, `open-items.md`, `traceability.md`, `decision-register.md`, `risks.md`, `changes.md`, `adr/`, `contracts/`, `evidence/`, `work/`, and `checkpoints/` with `checkpoints/checkpoint-register.md`. Control files use kebab-case; UPPER_CASE is reserved for generated register exports.

**Status:** CLOSED — BASELINE — REPOSITORY CONTROL
**Primary Closure Artifact / Decision Record:** Repository / Deployment Baseline



### Q1392. Which project documents already exist?

**Answer:** Known governing material includes the LabNexus Master Project Prompt and the defined project-control/baseline record set. Actual filesystem contents should be verified against the repository rather than assumed.

**Status:** CLOSED — RECONCILED BASELINE



### Q1393. Which project documents must be created before coding?

**Answer:** Before coding: Project Charter; Roadmap; Architecture Baseline; Requirements/operating-model baseline; Active Task; Decision Register; Change Register; Risk Register; Traceability Matrix; Checkpoint Register; database/API/UI contracts at the level required for implementation; and applicable validation/test strategy.

**Status:** CLOSED — RECONCILED BASELINE



### Q1394. Which document is authoritative for requirements?

**Answer:** Requirements authority: controlled Requirements Baseline / Requirements Specification. Individual source documents remain source evidence, but approved project requirements are authoritative for implementation.

**Status:** CLOSED — RECONCILED BASELINE



### Q1395. Which document is authoritative for architecture?

**Answer:** Architecture authority: ARCHITECTURE_BASELINE.md plus approved ADRs referenced by it.

**Status:** CLOSED — RECONCILED BASELINE



### Q1396. Which document is authoritative for the database contract?

**Answer:** Database authority: controlled Database Contract / Data Model Specification, with migration scripts as the executable implementation.

**Status:** CLOSED — RECONCILED BASELINE



### Q1397. Which document is authoritative for the API contract?

**Answer:** API authority: controlled API Contract/OpenAPI specification generated and/or maintained from the approved backend contract.

**Status:** CLOSED — RECONCILED BASELINE



### Q1398. Which document is authoritative for the UI contract?

**Answer:** UI authority: controlled UI/UX Contract and Screen Specification, supported by approved wireframes/screen definitions.

**Status:** CLOSED — RECONCILED BASELINE



### Q1399. Which document is authoritative for current state?

**Answer:** Current state authority: PROJECT_STATE.md.

**Status:** CLOSED — RECONCILED BASELINE



### Q1400. Which document is authoritative for active task?

**Answer:** Active task authority: ACTIVE_TASK.md.

**Status:** CLOSED — RECONCILED BASELINE



### Q1401. Which document is authoritative for open items?

**Answer:** Open items authority: controlled Open Items / Decision Queue register, linked to Decision/Change records.

**Status:** CLOSED — RECONCILED BASELINE



### Q1402. Which document is authoritative for checkpoints?

**Answer:** Checkpoint authority: CHECKPOINT_REGISTER.md.

**Status:** CLOSED — RECONCILED BASELINE



### Q1403. Which document is authoritative for traceability?

**Answer:** Traceability authority: TRACEABILITY_MATRIX.md.

**Status:** CLOSED — RECONCILED BASELINE



### Q1404. What is the exact naming convention for repository documents?

**Answer:** Repository documents should use stable UPPER_SNAKE_CASE.md for top-level control documents, versioned descriptive names for specifications, and unique IDs for WPs, Tasks, Decisions, Evidence, and Checkpoints.

**Status:** CLOSED — RECONCILED BASELINE



### Q1405. What is the exact format for ADRs?

**Answer:** ADR format: ADR ID; title; status; date; context; decision; alternatives considered; consequences; risks; affected components; related requirements/tasks; approval; supersedes/superseded-by.

**Status:** CLOSED — RECONCILED BASELINE



### Q1406. What is the exact format for work packages?

**Answer:** Work Package format: WP ID; phase; objective; scope; exclusions; inputs; outputs/deliverables; dependencies; acceptance criteria; tasks; risks; evidence; checkpoint; owner; status.

**Status:** CLOSED — RECONCILED BASELINE



### Q1407. What is the exact format for tasks?

**Answer:** Task format: Task ID; parent WP; objective; scope; prerequisites; authorized work; implementation steps; acceptance criteria; tests; evidence; dependencies; status; completion record.

**Status:** CLOSED — RECONCILED BASELINE



### Q1408. What is the exact format for evidence records?

**Answer:** Evidence record: Evidence ID; source task/requirement; environment/version; date/time; actor; procedure/test; expected; actual; artifact references; result; reviewer; disposition.

**Status:** CLOSED — RECONCILED BASELINE



### Q1409. What is the exact format for checkpoints?

**Answer:** Checkpoint record: Checkpoint ID; scope; inputs; required deliverables; evidence summary; defects/deviations; traceability status; decision; approver; date; resulting project state/baseline.

**Status:** CLOSED — RECONCILED BASELINE



### Q1410. What is the exact status vocabulary used in project records?

**Answer:** Project/task progression, document/configuration lifecycle, and approval disposition remain separate controlled vocabularies. One vocabulary must not be reused to represent another merely for convenience.

### Q1411. Who may edit controlled project documents?

**Answer:** Controlled project documents editable only by authorized project contributors; approval authority is separate where independence is required.

**Status:** CLOSED — RECONCILED BASELINE



### Q1412. How are document changes reviewed and approved?

**Answer:** Material document changes require review, version/history, approval where controlled, and linkage to the relevant Task/Decision/Change record.

**Status:** CLOSED — RECONCILED BASELINE



### Q1413. Is Git the authoritative version-control system?

**Answer:** Yes. Git is the authoritative version-control system for project source and controlled repository documents.

**Status:** CLOSED — RECONCILED BASELINE



### Q1414. What branch/merge policy is used?

**Answer:** Recommended policy: protected main as authoritative; short-lived task/feature branches; merge only after required tests/review; no direct production changes outside repository control.

**Status:** CLOSED — RECONCILED BASELINE



### Q1415. Are commits required to reference Task IDs?

**Answer:** Yes. Commits for controlled work should reference the relevant Task ID.

**Status:** CLOSED — RECONCILED BASELINE



### Q1416. Are release tags required?

**Answer:** Yes. Release tags are required for production releases.

**Status:** CLOSED — RECONCILED BASELINE



### Q1417. Is a changelog required?

**Answer:** Yes. A changelog/release-notes record is required.

**Status:** CLOSED — RECONCILED BASELINE



### Q1418. Is an ADR required for every material architectural decision?

**Answer:** Yes. Every material architectural decision requires an ADR. Minor implementation details do not require ADRs unless they materially alter an existing architectural decision.

---

# 59. Phase and Work-Package Readiness

**Status:** CLOSED — RECONCILED BASELINE



### Q1419. What exactly must be completed in Phase 0 before Phase 1 can start?

**Answer:** Before Phase 1 starts, Phase 0/project-control prerequisites must include: project charter/control rules; governance/roles; roadmap; repository contract; baseline status model; decision/change/risk registers; task authorization rules; traceability approach; and explicit project scope/exclusions.

**Status:** CLOSED — RECONCILED BASELINE



### Q1420. What exact deliverables define completion of each phase?

**Answer:** Each phase is complete only when its defined deliverables + acceptance criteria + tests/evidence + verification + approved checkpoint + baseline update are complete.

**Status:** CLOSED — RECONCILED BASELINE



### Q1421. What dependencies cross phase boundaries?

**Answer:** Cross-phase dependencies must be explicitly recorded in roadmap/WP records and traceability; later phases cannot silently assume unresolved predecessor decisions.

**Status:** CLOSED — RECONCILED BASELINE



### Q1422. Which phases may overlap safely?

**Answer:** Documentation, governance, test preparation, security review, and some technical foundation work may overlap when their dependencies are satisfied.

**Status:** CLOSED — RECONCILED BASELINE



### Q1423. Which phases must remain strictly sequential?

**Answer:** Requirements that establish foundational behavior, architecture, data integrity, workflow/state semantics, and critical security controls should remain sequential before dependent implementation.

**Status:** CLOSED — RECONCILED BASELINE



### Q1424. What makes a Work Package ready for task refinement?

**Answer:** WP ready for task refinement when objective, scope, exclusions, inputs, outputs, dependencies, acceptance criteria, risks, and required decisions are sufficiently specified.

**Status:** CLOSED — RECONCILED BASELINE



### Q1425. What makes a Task ready for authorization?

**Answer:** Task ready for authorization when scope and acceptance criteria are clear, dependencies resolved, required inputs available, risks understood, and implementation can proceed without material ambiguity.

**Status:** CLOSED — RECONCILED BASELINE



### Q1426. Who authorizes a Task?

**Answer:** Task authorized by the designated Project/Technical authority, according to project governance. The authorization does not substitute for laboratory approval of laboratory-specific technical rules.

**Status:** CLOSED — RECONCILED BASELINE



### Q1427. What evidence must exist before a Task can be marked complete?

**Answer:** Task completion requires implementation evidence, test evidence, documentation updates, traceability updates, defect/deviation disposition, and reviewer/verification evidence appropriate to the task.

**Status:** CLOSED — RECONCILED BASELINE



### Q1428. What evidence must exist before a Work Package can be closed?

**Answer:** WP closure requires all tasks complete/accepted, deliverables complete, evidence indexed, open issues dispositioned, risks updated, traceability complete, and WP acceptance recorded.

**Status:** CLOSED — RECONCILED BASELINE



### Q1429. What evidence must exist before a Phase checkpoint can be accepted?

**Answer:** Phase checkpoint requires accepted phase deliverables, verification evidence, traceability, risk/decision/change updates, reproducible baseline bundle, and formal checkpoint decision.

**Status:** CLOSED — RECONCILED BASELINE



### Q1430. Which known open questions block coding?

**Answer:** Coding blockers include unresolved decisions affecting data identity, workflow/state model, authorization/SoD, result/revision semantics, launch tests/methods/parameters/formulas, report content, critical QC rules, retention, security model, and other behavior that cannot safely be inferred.

**Status:** CLOSED — RECONCILED BASELINE



### Q1431. Which open questions can safely be deferred?

**Answer:** Safe deferrals include future disciplines, optional email/SMS, advanced BI, public API, mobile workflow, enterprise integrations, advanced inventory, and other explicitly excluded v1 functionality.

**Status:** CLOSED — RECONCILED BASELINE



### Q1432. What is the maximum acceptable unresolved decision debt before implementation begins?

**Answer:** No arbitrary percentage. Material unresolved decision debt must be zero for the requirements that a coding task depends upon. Project-wide decision debt may remain only where it is explicitly classified as deferred and cannot affect current implementation.

---

# 60. State and Completion Semantics

**Status:** CLOSED — RECONCILED BASELINE



### Q1433. What exactly does SPECIFIED mean for this project?

**Answer:** SPECIFIED = requirement/scope is sufficiently defined and approved for planning; required assumptions/open decisions are resolved to the level needed for the next step. No implementation authorization is implied.

**Status:** CLOSED — RECONCILED BASELINE



### Q1434. What exactly does PLANNED mean?

**Answer:** PLANNED = work has been decomposed and scheduled/placed in the roadmap/WP/task structure, but coding or execution is not authorized.

**Status:** CLOSED — RECONCILED BASELINE



### Q1435. What exactly does AUTHORIZED mean?

**Answer:** AUTHORIZED = a specific Task or controlled action is formally authorized to proceed. Authorization must identify scope, owner, and applicable acceptance criteria.

**Status:** CLOSED — RECONCILED BASELINE



### Q1436. What exactly does IN PROGRESS mean?

**Answer:** IN_PROGRESS = authorized work has actually started and remains unfinished.

**Status:** CLOSED — RECONCILED BASELINE



### Q1437. What exactly does IMPLEMENTED mean?

**Answer:** IMPLEMENTED = scoped implementation has been completed and is ready for testing; it is not yet necessarily verified or accepted.

**Status:** CLOSED — RECONCILED BASELINE



### Q1438. What exactly does TESTED mean?

**Answer:** TESTED = required tests have been executed and results recorded; successful testing alone does not equal formal verification.

**Status:** CLOSED — RECONCILED BASELINE



### Q1439. What exactly does VERIFIED mean?

**Answer:** VERIFIED = objective evidence has been independently evaluated against the acceptance criteria and found satisfactory.

**Status:** CLOSED — RECONCILED BASELINE



### Q1440. What exactly does ACCEPTED mean?

**Answer:** ACCEPTED = authorized acceptance authority has accepted the verified deliverables, including approved deviations where applicable.

**Status:** CLOSED — RECONCILED BASELINE



### Q1441. What exactly does RELEASED mean?

**Answer:** RELEASED = an accepted software/document/configuration package has been formally versioned and approved for deployment/use.

**Status:** CLOSED — RECONCILED BASELINE



### Q1442. What exactly does DEPLOYED mean?

**Answer:** DEPLOYED = the released version has actually been installed/configured in the target environment.

**Status:** CLOSED — RECONCILED BASELINE



### Q1443. What exactly does HEALTH VERIFIED mean?

**Answer:** HEALTH_VERIFIED = post-deployment health/smoke/operational checks demonstrate that the deployed environment is functioning as required.

**Status:** CLOSED — RECONCILED BASELINE



### Q1444. Can a state be skipped?

**Answer:** A state may be skipped only when it is genuinely not applicable, and the omission must be explicit and evidenced. Required verification/acceptance states cannot be bypassed merely for convenience.

**Status:** CLOSED — RECONCILED BASELINE



### Q1445. Who may transition each state?

**Answer:** Project-control state transitions are made by the designated task/WP/phase authority according to governance; technical status changes by technical owners must not create false acceptance.

**Status:** CLOSED — RECONCILED BASELINE



### Q1446. What evidence is required for each transition?

**Answer:** Every transition requires the evidence appropriate to that state, recorded in the task/WP/checkpoint record.

**Status:** CLOSED — RECONCILED BASELINE



### Q1447. Can a state be reverted?

**Answer:** A state may be superseded/reopened through a controlled action, but historical state transitions are never erased.

**Status:** CLOSED — RECONCILED BASELINE



### Q1448. What happens when a checkpoint is REJECTED?

**Answer:** REJECTED checkpoint: acceptance denied; deficiencies recorded; corrective work defined; predecessor/target state remains clear; new evidence required before resubmission.

**Status:** CLOSED — RECONCILED BASELINE



### Q1449. What happens when a checkpoint is BLOCKED?

**Answer:** BLOCKED checkpoint: work cannot proceed due to an unresolved dependency/decision/risk; blocker is explicitly recorded and no false completion state is assigned.

**Status:** CLOSED — RECONCILED BASELINE



### Q1450. How are exceptions recorded without falsely marking work complete?

**Answer:** Exceptions are recorded as deviations/issues/change records and linked to affected tasks/evidence. They do not change the underlying completion state unless formally accepted.

---

# 61. Historical Reconstruction Test — Exact Acceptance Questions

**Status:** CLOSED — RECONCILED BASELINE



### Q1451. Can the system identify the exact Customer for a TestInstance?

**Answer:** Historical reconstruction is a mandatory architectural invariant using immutable identifiers, effective-dated configuration, immutable workflow/audit events, calculation evidence, ResultRevision, ApprovalSnapshot, ReportResultSnapshot, DocumentVersion and preserved issued artifacts rather than current mutable state.

**Status:** CLOSED — RECONCILED BASELINE



### Q1452. Can the system identify the exact Project/Request?

**Answer:** Yes. The reconstruction chain shall retain the exact Project/Contract and Request identities associated with the TestInstance.
The implementation shall distinguish stable relational identity from mutable descriptive fields. Required historical report-visible representations shall be frozen in the appropriate snapshot so that later renaming or administrative edits cannot alter the reconstruction of an earlier issued state.
Historical reconstruction shall use the exact identifiers and effective historical relationships that existed for the event being reconstructed.

**Status:** CLOSED — RECONCILED BASELINE



### Q1453. Can the system identify the exact Sample and sample identity history?

**Answer:** Yes. The reconstruction shall identify the exact Sample record and its controlled identity history.
Sample identifiers, laboratory numbering, customer-provided identifiers, aliases, relabeling events, corrections, and other identity changes shall be represented through controlled historical records rather than destructive overwriting.
The reconstruction shall be able to show which Sample identity applied at the relevant stage and which representation was used on the relevant report or controlled record.

**Status:** CLOSED — RECONCILED BASELINE



### Q1454. Can the system identify the exact TestDefinition?

**Answer:** Yes. Each TestInstance shall retain an explicit reference to the exact TestDefinition used for the work.
A later change to the technical meaning, parameter set, reporting behavior, or workflow semantics of a TestDefinition shall not silently alter the historical interpretation of an existing TestInstance. Such changes shall be handled through controlled versioning, effective dating, or creation of a new controlled definition as required by the governing configuration model.
The report snapshot shall preserve the report-visible TestDefinition identity/name required for historical reconstruction.

**Status:** CLOSED — RECONCILED BASELINE



### Q1455. Can the system identify the exact MethodVersion?

**Answer:** Yes. The exact MethodVersion applicable to the TestInstance shall be deterministically identifiable and preserved.
The TestInstance shall derive its technical method through the approved relationship to TestDefinition and MethodVersion rather than relying on the Method's current "latest" state.
MethodVersion changes shall be controlled and effective-dated. Historical records shall continue to resolve to the MethodVersion that actually governed the work.

**Status:** CLOSED — RECONCILED BASELINE



### Q1456. Can the system identify the exact ParameterDefinitions used?

**Answer:** Yes. Each calculation/result pathway shall be able to identify the exact controlled ParameterDefinitions that supplied the technical meaning of the parameters used.
Parameter identity shall not depend solely on current labels or mutable names. Where the definition's meaning, unit semantics, validation behavior, or reporting significance changes, the applicable controlled definition/version shall be identifiable as part of the historical configuration.
Calculation evidence and report reconstruction shall therefore be based on the parameter definitions actually used, not whatever parameter configuration happens to be current at the time of reconstruction.

**Status:** CLOSED — RECONCILED BASELINE



### Q1457. Can the system identify the exact analyst(s)?

**Answer:** Yes. Analyst identity shall be captured by stable user identity linked to the relevant TestInstance/assignment/execution evidence.
Historical reconstruction shall not depend on the current name, role, status, or active/inactive state of the user account. The historical event shall preserve the identity of the person who performed the action together with its timestamp and authorization context.
Where a visible human-readable name or role is required for historical rendering, that historical representation shall be preserved as part of the appropriate evidence/snapshot rather than reconstructed from mutable current user-profile data.

**Status:** CLOSED — RECONCILED BASELINE



### Q1458. Can the system identify the exact equipment used?

**Answer:** Yes. Each equipment use relevant to controlled testing shall be explicitly attributable to the exact Equipment identity.
Equipment records shall remain stable even when equipment undergoes calibration, maintenance, relocation, qualification, status changes, or retirement.
Historical TestInstance reconstruction shall identify the equipment actually associated with the work and the relevant evidence of its status and eligibility at the time of use.

**Status:** CLOSED — RECONCILED BASELINE



### Q1459. Can the system determine equipment eligibility as-of the test activity?

**Answer:** Yes. Eligibility shall be determined against the historical state applicable at the **actual test activity timestamp**, not against the equipment's present-day state.
The determination shall consider the controlled effective histories relevant to the laboratory policy, including applicable calibration, maintenance, qualification, verification, status, authorization, and any method/test-specific equipment restrictions.
The system shall preserve sufficient evidence to reproduce the eligibility decision, including the effective historical records or an explicit recorded eligibility evaluation where required. A currently calibrated or currently authorized equipment record shall never be used to retroactively justify an earlier activity.

**Status:** CLOSED — RECONCILED BASELINE



### Q1460. Can the system identify every observation used?

**Answer:** Yes. Each observation participating in a result or calculation shall be independently identifiable and traceable to its TestInstance/parameter context.
The calculation pathway shall reference the exact observation records or immutable observation snapshots used. Corrections shall preserve prior observation history rather than replacing the evidence needed to explain an earlier calculation.
Historical reconstruction shall therefore be able to distinguish the observations used in the original result from observations introduced by subsequent correction or rework.

**Status:** CLOSED — RECONCILED BASELINE



### Q1461. Can the system identify every calculation input?

**Answer:** Yes. Every CalculationRun shall preserve a controlled input snapshot sufficient to reconstruct the inputs actually supplied to the calculation engine.
The snapshot shall identify the contributing observations/values, units and relevant normalized representations, parameter identities, constants or dependencies, and any other controlled input that materially affected the calculation.
The system shall not rely on rereading the current state of source records to infer what was calculated previously.

**Status:** CLOSED — RECONCILED BASELINE



### Q1462. Can the system identify the exact FormulaVersion?

**Answer:** Every CalculationRun identifies the exact immutable FormulaVersion used. FormulaVersion changes create new versions; prior calculations are never rebound to later definitions.

**Status:** CLOSED — RECONCILED BASELINE



### Q1463. Can the system identify the exact CalculationRun?

**Answer:** Yes. Every persisted calculated result shall be traceable to its exact CalculationRun.
The CalculationRun shall act as the immutable evidence boundary for the calculation event, including input snapshot, FormulaVersion, dependencies, calculation engine/version information, execution time, actor/process identity, and resulting output linkage.
A recalculation shall create a distinct CalculationRun rather than silently modifying the prior calculation evidence.

**Status:** CLOSED — RECONCILED BASELINE



### Q1464. Can the system identify the exact ResultRevision?

**Answer:** Yes. Historical result reconstruction shall identify the precise ResultRevision associated with the state being reconstructed.
Correction revisions and ApprovalSnapshot revisions shall remain explicitly typed and separately attributable. The current live Result state shall not be treated as sufficient historical evidence.
Where a report was issued from an approved result, its ReportResultSnapshot shall reference the exact Result and ResultRevision used for that report state.

**Status:** CLOSED — RECONCILED BASELINE



### Q1465. Can the system identify the exact review event?

**Answer:** Yes. The exact review action shall be represented by the authoritative approval/workflow event structure.
The event shall preserve the affected TestInstance/record identity, actor, action, timestamp, resulting workflow state, relevant authorization context, and associated controlled evidence.
Historical reconstruction shall identify the actual review event that applied to the relevant result state, rather than inferring review from the fact that a record is currently marked reviewed.

**Status:** CLOSED — RECONCILED BASELINE



### Q1466. Can the system identify the exact verification event?

**Answer:** Yes. The exact verification event shall be independently attributable and linked to the controlled record and workflow state it verified.
The reconstruction shall identify the verifier, event timestamp, affected TestInstance/result state, authorization context, and any required decision/evidence metadata.
A later verification shall not overwrite the evidence of an earlier verification event.

**Status:** CLOSED — RECONCILED BASELINE



### Q1467. Can the system identify the exact approval event?

**Answer:** Yes. The **approval_chain_event** remains the authoritative source of approval history.
The reconstruction shall identify the exact approval event, the approved record/state, authorized signatory identity, approval timestamp, relevant authentication/reauthentication evidence, and resulting state transition.
Current user-account status shall not determine whether a historical approval existed. Disabling an account later shall not erase or invalidate the historical event.

**Status:** CLOSED — RECONCILED BASELINE



### Q1468. Can the system identify the exact ApprovalSnapshot?

**Answer:** Yes. Every successful Approval shall create an immutable **ApprovalSnapshot** representing the approved technical/result state at that time.
The ApprovalSnapshot shall be independently identifiable and linked to the approval event and applicable ResultRevision(s). It shall preserve the state required to establish exactly what was approved, rather than relying on the later live Result.
Historical report and result reconstruction shall use the specific ApprovalSnapshot associated with the relevant approval path.

**Status:** CLOSED — RECONCILED BASELINE



### Q1469. Can the system identify the accreditation-scope state that applied?

**Answer:** Yes. The reconstruction shall identify the exact accreditation-scope determination applicable to the work at the relevant time.
The determination shall preserve whether scope was resolved from the MethodVersion default or a TestDefinition override, the applicable effective interval/version, the resolved accreditation representation, and the source of that determination.
The report-visible representation shall be frozen in the relevant snapshot. Later changes to accreditation-scope configuration shall not silently change the historical classification of an issued report.
LabNexus shall represent the laboratory's approved accreditation data and process; it shall not itself be represented as conferring accreditation.

**Status:** CLOSED — RECONCILED BASELINE



### Q1470. Can the system identify the exact ReportRevision?

**Answer:** Yes. Every report state that becomes part of controlled report history shall have an explicit ReportRevision identity.
The reconstruction shall identify the exact revision number/identity, associated report snapshots, approval/result basis, document version, artifact state, issuance status, and relevant audit history.
The system shall not rebuild a historical ReportRevision merely by rerendering the current report template against current data.

**Status:** CLOSED — RECONCILED BASELINE



### Q1471. Can the system identify every ReportResultSnapshot?

**Answer:** Yes. Every report-visible result included in a ReportRevision shall be represented by an explicit ReportResultSnapshot.
The snapshot shall retain the exact `report_revision_id`, `result_id`, and `result_revision_id`, together with the report-visible value, unit, TestDefinition representation, accreditation representation, analyst representation, approval timestamp, and other frozen fields required by report policy.
This makes the report state independent of later corrections to the underlying live Result.

**Status:** CLOSED — RECONCILED BASELINE



### Q1472. Can the system identify the exact DocumentVersion?

**Answer:** Yes. A controlled report/document shall reference the exact DocumentVersion used for the applicable report revision or controlled document state.
DocumentVersion identity shall be immutable after publication. Updating a controlled document shall create a new version rather than editing the content in place.
Historical reconstruction shall therefore resolve the precise version that governed the document/report state at the relevant time.

**Status:** CLOSED — RECONCILED BASELINE



### Q1473. Can the system retrieve the exact issued PDF?

**Answer:** The exact issued PDF is the authoritative historical artifact, retained with controlled identity and SHA-256 hash. Reconstruction retrieves preserved bytes rather than rerendering against current templates/runtime/data.

**Status:** CLOSED — RECONCILED BASELINE



### Q1474. Can the system identify the relevant audit events?

**Answer:** Yes. Relevant audit events shall be traceable through the controlled entity/action/reference relationships associated with the reconstructed record.
The audit trail shall include the material lifecycle events needed to explain creation, assignment, execution, correction, review, verification, approval, report generation/issuance, configuration impact, and other controlled changes.
Routine reads need not automatically create audit entries unless specifically classified as sensitive/auditable access. Where a read/download/export is designated auditable, the resulting event shall remain linked to the relevant resource.

**Status:** CLOSED — RECONCILED BASELINE



### Q1475. Can the complete reconstruction be produced without relying on current mutable state?

**Answer:** Complete reconstruction without current mutable state is mandatory. Historical reconstruction uses immutable identifiers, versioned configuration, immutable events, result/report snapshots, DocumentVersions and preserved artifacts.

**Status:** CLOSED — RECONCILED BASELINE



### Q1476. Can the reconstruction distinguish the original issued state from later corrections?

**Answer:** Yes. The distinction shall be explicit through ResultRevision, ApprovalSnapshot, ReportRevision, ReportResultSnapshot, workflow/audit events, and preserved PDF artifacts.
A later correction shall create a controlled new result state and follow the required review/verification/approval process. It shall not rewrite the original approved or issued state.
The system shall therefore be able to show both the earlier issued state and the later corrected/reapproved state, including the relationship between them.

**Status:** CLOSED — RECONCILED BASELINE



### Q1477. Can ReportRevision 1 still be reconstructed after later result correction and reapproval?

**Answer:** Yes. This shall be an explicit verification requirement.
The reconstruction test shall create and issue ReportRevision 1, subsequently correct a relevant result, complete the required review/verification/approval workflow, and create a later report revision.
After the correction, the system shall still reproduce ReportRevision 1 from its own snapshots and preserved PDF without consulting the later live Result state. The original artifact hash shall remain unchanged.

**Status:** CLOSED — RECONCILED BASELINE



### Q1478. Can ReportRevision 2 be reconstructed independently?

**Answer:** Yes. ReportRevision 2 shall have its own complete report-result snapshot state and exact document/artifact linkage.
Its reconstruction shall depend on the controlled state intentionally included in Revision 2, not on mutable current fields or an assumption that the report can be recomputed from today's data.
The evidence shall demonstrate that Revision 1 and Revision 2 can each be reconstructed independently and that the two states remain distinguishable.

**Status:** CLOSED — RECONCILED BASELINE



### Q1479. What is the formal test procedure for this reconstruction?

**Answer:** The formal verification procedure shall use at least the following sequence:
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

**Status:** CLOSED — RECONCILED BASELINE



### Q1480. Who accepts the reconstruction evidence?

**Answer:** The **Technical Authority** shall review the technical correctness of the reconstruction.
The **Quality Authority** shall verify the integrity, completeness, traceability, and adequacy of the evidence as a controlled quality/validation record.
The **Project Owner / Laboratory Business Owner** shall provide final project-level acceptance where the reconstruction test forms part of release or validation acceptance.
The person executing the test shall not be the sole authority for accepting the evidence.

**Status:** CLOSED — RECONCILED BASELINE



### Q1481. What laboratory policy is currently unknown?

**Answer:** No additional laboratory policy shall be invented to close this question.
The technical decision is that any laboratory-policy dependency not already explicitly approved in the project baseline shall be recorded as an **unresolved policy input** with an owner, required decision authority, and affected system behavior.
Coding may proceed only where the implementation is independent of that unresolved policy. Where behavior would materially differ according to the missing laboratory policy, the affected behavior shall remain non-deployable until the policy is approved.
This prevents a developer-selected default from becoming an uncontrolled laboratory rule.

**Status:** CLOSED — RECONCILED BASELINE



### Q1482. What workflow rule is currently unknown?

**Answer:** The common controlled workflow already forms the baseline, but any unconfirmed exceptional workflow rule shall remain explicitly unresolved.
Examples include method-specific rework, retest, reopening, cancellation, nonconforming-work disposition, or unusual approval transitions where the governing laboratory procedure has not yet been finalized.
Until such a rule is approved, the implementation shall not silently infer a permissive transition. Existing hard controls, including authorization and hard same-TestInstance SoD restrictions, remain mandatory. Policy-dependent transitions shall default to **blocked/not activatable** rather than being improvised.

**Status:** CLOSED — RECONCILED BASELINE



### Q1483. What approval rule is currently unknown?

**Answer:** Any approval prerequisite or authority detail not already established by the approved baseline shall remain an explicit controlled dependency.
The baseline approval model remains authoritative: approval must be attributable to an authorized person, linked to the exact record/state, recorded in the approval chain, and subject to the approved SoD rules.
Where a laboratory-specific approval condition is still unknown, LabNexus shall not invent it or allow a generic bypass. The missing rule shall be captured as a decision item and incorporated through controlled configuration after approval and verification.

**Status:** CLOSED — RECONCILED BASELINE



### Q1484. What SoD rule is currently unknown?

**Answer:** The already-approved hard SoD rules remain fixed and shall not be weakened by this unresolved-item category.
The unresolved portion is limited to **policy-controlled** relationships or exceptional approval arrangements that the laboratory has not yet explicitly decided.
Until such a rule is approved, the conservative behavior shall be **BLOCK** for the potentially conflicting transition. No user interface, administrative override, emergency path, or generic configuration shall convert a hard-block conflict into an allowed action.
Approved policy-controlled exceptions shall be represented through the effective-dated SoD Matrix with competence, authority, independence, justification, and evidence requirements.

**Status:** CLOSED — RECONCILED BASELINE



### Q1485. What accreditation rule is currently unknown?

**Answer:** No unsupported accreditation rule may be inferred. MethodVersion supplies the normal scope default and an approved TestDefinition override may apply; precedence/effective dating are deterministic. Without approved laboratory scope evidence, the method/test is not assumed accredited merely because it exists.

**Status:** CLOSED — RECONCILED BASELINE



### Q1486. What calculation rule is currently unknown?

**Answer:** No calculation rule may be invented. Controlled production calculation requires an approved FormulaVersion and its units, constants, transformations, precision/rounding, validation and invalid-input behavior. Missing technical rules keep the formula unavailable for controlled production use.

**Status:** CLOSED — RECONCILED BASELINE



### Q1487. What report-content rule is currently unknown?

**Answer:** Report content is controlled through approved ReportDefinition/ReportTemplate and ReportRevision structures. Technical or contractual meaning is versioned and historically reconstructable; unapproved report elements are not invented.

**Status:** CLOSED — RECONCILED BASELINE



### Q1488. What QC rule is currently unknown?

**Answer:** QC is controlled by approved configuration for each applicable test, including whether QC is required, criteria, frequency, evaluation and blocking/warning/disposition. Missing laboratory criteria keep the QC control inactive or the affected workflow blocked.

**Status:** CLOSED — RECONCILED BASELINE



### Q1489. What equipment-enforcement rule is currently unknown?

**Answer:** Equipment eligibility is evaluated against historical state at the actual TestInstance activity timestamp, including status, calibration, maintenance, qualification/verification, authorization and method/test restrictions. Unapproved enforcement levels remain blocked.

**Status:** CLOSED — RECONCILED BASELINE



### Q1490. What record-retention rule is currently unknown?

**Answer:** Retention is 10 years minimum for controlled records and issued reports, with controlled archival rather than automatic deletion. Retention covers the reconstructable record set and respects legal/quality holds; v1 has no automatic destruction workflow.

**Status:** CLOSED — RECONCILED BASELINE



### Q1491. What backup/recovery rule is currently unknown?

**Answer:** Backup/recovery uses coherent Recovery Sets, multiple retained copies, offline/encrypted protection and restore validation. The tiered baseline supports a separate-disk local copy, encrypted offline copy and off-site rotation; exact machine/media details are deployment inputs.

**Status:** CLOSED — GOVERNANCE CLASSIFICATION



### Q1492. What permission rule is currently unknown?

**Answer:** The permission baseline is RBAC + backend authorization + per-TestInstance SoD, with hard blocks having no bypass. The detailed role/permission matrix is a controlled work artifact and must be accepted before affected production workflows are enabled.

**Status:** CLOSED — GOVERNANCE CLASSIFICATION



### Q1493. What configuration-governance rule is currently unknown?

**Answer:** Configuration governance is typed/effective-dated controlled configuration using proposal → approval → effective state, plus a bounded visible/countersigned emergency path with expiry and retrospective review.

**Status:** CLOSED — GOVERNANCE CLASSIFICATION



### Q1494. What user-training rule is currently unknown?

**Answer:** Training is a deployment/validation requirement, not an HR subsystem. Required role-specific competence evidence must be satisfied before applicable controlled actions are enabled.

**Status:** CLOSED — GOVERNANCE CLASSIFICATION



### Q1495. What security rule is currently unknown?

**Answer:** The core v1 security baseline includes Argon2id, server-side sessions, secure cookies, CSRF protection, backend authorization, SoD, controlled secrets, host/filesystem protection, encrypted removable/offline backups and incident controls, together with the controlled password/session rules.

**Status:** CLOSED — GOVERNANCE CLASSIFICATION



### Q1496. What deployment/operations rule is currently unknown?

**Answer:** Deployment follows the approved Windows single-host topology and the controlled React/FastAPI/SQLite/Caddy release model, including pinned runtime/PDF environment, backup/recovery controls and validated updates. Host names, paths and service identities are deployment inputs.

**Status:** CLOSED — GOVERNANCE CLASSIFICATION



### Q1497. Which unknowns may be safely deferred?

**Answer:** Safe deferrals include deployment-specific host/path details, exact training schedules, future disciplines/rules not required at launch, future commercial charging, future integrations and explicitly later-phase operational details, provided no safety, integrity, authorization, historical-reconstruction or security control is weakened.

**Status:** CLOSED — GOVERNANCE CLASSIFICATION



### Q1498. Which unknowns would make coding unsafe or ambiguous?

**Answer:** Coding is unsafe or ambiguous when an unresolved item would materially change data integrity, authorization, hard SoD, historical reconstruction, report authority, calculation meaning, accreditation representation, mandatory QC/equipment enforcement, security boundaries or controlled retention. Such behavior remains blocked until the governing decision is approved.

**Status:** CLOSED — GOVERNANCE CLASSIFICATION



### Q1499. Which unknowns require a formal ADR?

**Answer:** A formal ADR is required for an architectural or cross-cutting technical decision that changes a frozen baseline, introduces a new invariant, changes a security/data-integrity boundary or selects a significant long-term implementation alternative.

**Status:** CLOSED — GOVERNANCE CLASSIFICATION



### Q1500. Which unknowns require a Laboratory Decision record?

**Answer:** A Laboratory Decision record is required for laboratory policy, workflow, acceptance criteria, approval authority, QC/equipment policy, confidentiality/retention policy or other domain rules owned by laboratory governance.

**Status:** CLOSED — GOVERNANCE CLASSIFICATION



### Q1501. Which unknowns require a Technical Decision record?

**Answer:** A Technical Decision record is required for implementation behavior, schema/invariant choices, security mechanism, performance target, deployment mechanism, software/runtime baseline or other technical behavior requiring engineering acceptance.

**Status:** CLOSED — GOVERNANCE CLASSIFICATION



### Q1502. Which unknowns require joint approval?

**Answer:** Joint approval is required when a decision crosses laboratory policy and technical implementation, especially accreditation, SoD, controlled workflow, QC/equipment enforcement, report authority, retention/recovery or security controls. The relevant laboratory/quality/technical authority and responsible project/technical authority must accept it before it becomes effective behavior.

**Status:** CLOSED — GOVERNANCE CLASSIFICATION

## Validation

Questions: **1502/1502**
Answers: **1502/1502**
Explicit statuses: **1502/1502**
Implementation blockers remaining in this pre-coding question set: **0**
Unresolved conflict statuses remaining: **0**
Unresolved proposed-default statuses remaining: **0**
Unresolved laboratory-decision statuses remaining: **0**
Unresolved technical-decision statuses remaining: **0**
Unresolved deployment-input statuses remaining: **0**

### Acceptance Statement

This 1,502-question document is the **consolidated pre-coding decision baseline** for the current project state.

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

Any later change to a controlled decision in this document must be processed through the applicable controlled change / ADR / Laboratory Decision / Technical Decision / joint approval mechanism and must not silently alter effective controlled behavior.


# Controlling Decision Register — Integrated Current Decisions

This section consolidates the current controlling decisions represented by the repository decision register. Where a question answer in the historical source differed, the applicable PCD below controls current behavior; the original question numbering and history remain preserved above.

| ID | Decision | Type | Status |
|---|---|---|---|
| PCD-01 | Password minimum 8; maximum accepted at least 64; mandatory offline blocklist; Argon2id; 5-failure/15-minute lockout; per-IP throttling; history 5; high-risk re-entry. Privileged 12-character minimum remains an open option, not the default. | TD | Confirmed; option open |
| PCD-02 | Charge calculation, Rate/CustomerRate, pricing snapshots, discounts/overrides, tax and invoicing are out of v1. | CSR | Confirmed |
| PCD-03 | Explicit versioned/effective-dated per-TestInstance SoD matrix; hard blocks for Analyst→Review/Verification/Approval and Reviewer→Verification; policy exceptions default to BLOCK; emergency never bypasses hard blocks. | JA | Confirmed; authority sign-off required |
| PCD-04 | TestDefinition and ParameterDefinition are versioned; TestDefinition key is `(test_code, version_no)` and each version binds to exactly one MethodVersion; historical rows are never repointed. | TD | Confirmed |
| PCD-05 | One append-only ResultRevision model with Correction and ApprovalSnapshot types; sequential revision numbers; no mutable `current_revision_id`; approval snapshot and approval event are atomically linked. | TD | Confirmed |
| PCD-06 | Accreditation applicability is resolved at execution start (first In Execution); state is frozen in ApprovalSnapshot/ReportResultSnapshot; later suspension/withdrawal can block issuance. | JA | Confirmed; authority sign-off required |
| PCD-07 | Internal `SAM-…` is the authoritative global Sample ID and is printed on labels/barcodes; customer external ID is unique per customer after normalization and historical values are provenance-only. | TD | Confirmed |
| PCD-08 | 10-year minimum controlled retention; defined retention-start rule; read-only searchable archive; no v1 automatic destruction. | LD | Confirmed; authority sign-off required |
| PCD-09 | Canonical project-control structure and kebab-case naming are controlled repository requirements; `decision-register.md` is the living index. | TD | Confirmed |
| PCD-10 | SQLite decimal values are canonical TEXT through SQLAlchemy Decimal mapping; no REAL/Numeric; rounding is per FormulaVersion. | TD | Confirmed |
| PCD-11 | 50 tests/sample is the design baseline; 80 is stretch; capacity/performance are established by an authorized spike on the actual target environment. | TD | Confirmed; spike evidence required |
| PCD-12 | Phase 0 is in progress; no Phase 3 schema exists; data architecture is built anew from the approved baseline. | TD | Confirmed |
| PCD-13 | Repeat/Retest/re-execution create new TestInstances; eligible pre-approval Rework stays on the same TestInstance; post-approval Correction uses Reopen + Correction revision; unlisted transitions are forbidden. | JA | Confirmed; Technical Authority sign-off required |
| PCD-14 | ReportRevision snapshots are created at freeze; stale revisions are replaced by new revisions; one open revision per Report; exact PDF linkage and issuance state are controlled. | TD | Confirmed |
| PCD-15 | Fresh password re-entry is required for high-risk approval, reopen, correction approval, report issue/reissue/withdrawal, configuration/role approvals, emergency declaration/countersign and restore; Review/Verification use attributable evidence without re-entry. | TD | Confirmed |
| PCD-16 | Core entities/relationships are controlled, including Customer/Project/Contract/Request, Sample→Request, TestRequest→TestInstance and SamplePortion; splits/composites/derived samples remain out of v1. | TD | Confirmed |
| PCD-17 | Controlled `user_competence` with active competence required at action timestamp; expiry blocks; Technical Authority approves competence; no HR module. | JA | Confirmed; Technical Authority sign-off required |
| PCD-18 | Tiered Recovery Sets, coherent DB/document verification, separate-disk local copy, encrypted offline copy, off-site rotation and disk thresholds using the smaller of percentage/GiB limits. | TD | Confirmed |
| PCD-19 | Offline Defender quarantine scan; Code 128/QR labels; pinned shipped Chromium for PDF; Windows service/task model; SQLite ≥3.35; normalized-key Unicode uniqueness. | TD | Confirmed |
| PCD-20 | Server-time integrity: >60s backward jump or >2min reference drift blocks approval/report issue; warn above 30s; client clocks are not authoritative. | TD | Confirmed |
| PCD-21 | Single AuditService/repository write path; normal audits are transactional; denied auth/permission/SoD events use autonomous short transactions; technical approvals use approval-chain events. | TD | Confirmed |
| PCD-22 | Controlled migration default: approved customer master data and historical issued report PDFs as read-only history; no fabricated historical result/TestInstance approval chains. | TD | Confirmed |
| PCD-23 | Functional role groups plus named Role-Holder Matrix/alternates; staffing must demonstrate sufficient independent competent people before affected workflows are activated. | JA | Confirmed; named inputs/sign-off required |
| PCD-24 | Launch Test Catalogue and golden cases required; formulas, units, rounding, constants, ranges and reportable outputs come from approved technical laboratory inputs; implementation must not invent them. | LD | Lab input required |
| PCD-25 | Launch QC Matrix, NABL scope, report wording/format and watermark require approved laboratory/quality/technical inputs; no launch-specific QC/report claim is invented. | LD | Lab input required |
| PCD-26 | Disposal authority, retained-sample period, legal hold, label printer and physical storage details are controlled laboratory/deployment inputs; disposal is blocked until prerequisites are satisfied. | LD | Lab/deployment inputs required |
| PCD-27 | Boilerplate question answers are dispositioned into explicit controlled behavior, including architecture boundaries, V&V, export controls, competence/training, migration and change/release governance. | TD | Confirmed |

## Authority, status and change control

The governing order is: **Main Prompt → consolidated Q1–Q1502 baseline → controlling decision register → future accepted ADR/Laboratory Decision/Technical Decision/joint approval**. Historical text is not erased by supersession. This document does not independently authorize implementation. The controlled delivery sequence remains:

`PROJECT → PHASE → WORK PACKAGE → AUTHORIZED TASK → IMPLEMENTATION → TEST → VERIFICATION → EVIDENCE → CHECKPOINT`

### Current authority/laboratory dependencies

PCD-03, PCD-06, PCD-08, PCD-13, PCD-17 and PCD-23 require their identified laboratory/quality/technical sign-off or named-role input. PCD-24 requires the Launch Test Catalogue and golden formula cases. PCD-25 requires the QC Matrix, NABL scope mapping, report wording/format/watermark inputs. PCD-26 requires the retained-sample period, disposal authority, label printer and actual host/storage details. PCD-22 requires the formal migration assessment outcome. The optional privileged-role 12-character password rule remains a Project Owner choice and is not adopted by default.

Until the applicable authority/input is supplied and accepted, affected controlled behavior remains non-deployable and must not be invented by implementation.
