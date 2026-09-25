# LabNexus Domain Model Baseline Index

## Current status
No Phase 3 schema has been implemented. The domain/data architecture is to be built from the approved source baseline.

## Authoritative inputs
- `../Main_Prompt.md` §§7–23 and §39.
- `../PreCoding_Questions_v0.8.md` reconciled answers.
- `../Decision_register.md` PCD-03–08, PCD-13–17, PCD-20–22 and PCD-27.

## Key controlled concepts
Sample, TestRequest, TestInstance; Method, MethodVersion, TestDefinition, ParameterDefinition; Observation, CalculationRun, FormulaVersion, Result, ResultRevision, ApprovalSnapshot; approval-chain events; Report, ReportRevision, ReportResultSnapshot, DocumentVersion; accreditation scope; equipment eligibility; QC; competence; audit; retention/hold; migration provenance.

## Phase 0 interpretation
This file is an index, not a substitute data-model specification. Detailed entities, invariants, FK rules, lifecycle matrices and schema contracts are produced only in the authorized requirements/data-architecture work packages.

## Non-negotiable reconstruction property
A historical issued report must identify the exact result revision, report revision, configuration/scope representation and exact PDF artifact that were issued.
