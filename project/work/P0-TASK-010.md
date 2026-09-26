# P0-TASK-010 — Define the Controlled Phase 0 Follow-up Plan for Outstanding Dependencies

## Status
**COMPLETE — CONTROLLED FOLLOW-UP PLAN DEFINED; P0-CHECKPOINT REMAINS NOT ACCEPTED**

## Authorization
Explicit project instruction dated 26 September 2026 authorizing P0-TASK-010.

## Source state reviewed
GitHub `main` after P0-TASK-009 closeout at commit `baa4636`, including the reconciled living decision register, checkpoint register, handoff, open items, risks, changes, and `P0-CHECKPOINT-DOSSIER.md`.

Historical root sources remain controlled and unchanged:
- `Main_Prompt.md`
- `PreCoding_Questions_v0.8.md`
- `Decision_register.md`

## Objective
Convert the remaining Phase 0 authority, staffing, laboratory-input, performance-acceptance and checkpoint dependencies into an explicit controlled follow-up plan. Distinguish Phase 1 entry gates from items that are later Phase 1 assessments or implementation-specific prerequisites. Do not invent decisions or authorize implementation.

## Follow-up register

| Ref | Required authority/input | Evidence required to close | Dependency / gate | Controlled next action | Timing |
|---|---|---|---|---|---|
| PCD-03 | Quality Authority + Project Owner approval; Technical review of implementability | Signed/electronically attributable SoD Matrix v1 decision, including policy version/effective date | Required for P0 checkpoint acceptance and before affected SoD-controlled workflows become effective | Obtain and record formal sign-off; preserve matrix version/effective date | **P0 / Phase 1 entry gate** |
| PCD-06 | Quality Authority approval with Technical concurrence | Approved execution-start accreditation rule and effective-date record | Required for accreditation-controlled behavior; prerequisite to affected execution/reporting configuration | Obtain and record formal rule approval | **P0 / Phase 1 entry gate** |
| PCD-08 | Quality Authority + Project Owner approval | Approved retention start/archive rule and effective-date record | Required for retention-controlled behavior and P0 checkpoint acceptance | Obtain and record formal decision | **P0 / Phase 1 entry gate** |
| PCD-13 | Technical Authority approval of execution semantics/boundary | Signed technical decision; later detailed transition matrix may remain Phase 1–2 work | Required for controlled execution-state behavior; affected implementation blocked until accepted | Obtain technical sign-off; schedule detailed transition matrix as Phase 1–2 work with test coverage | **P0 / Phase 1 entry gate** |
| PCD-17 | Technical Authority approval | Approved competence model decision | Required before competence-controlled assignment/execution/review/verification/approval/equipment use can be activated | Obtain and record competence-model sign-off | **P0 / Phase 1 entry gate** |
| PCD-23 | Project Owner + Quality Authority; named role-holder matrix and staffing feasibility | Approved Role-Holder Matrix with named alternates and independence check | Required to demonstrate SoD/staffing feasibility and support checkpoint acceptance | Complete and approve matrix; record conflicts/insufficient staffing as controlled issues | **P0 / Phase 1 entry gate** |
| PCD-01 option | Project Owner decision on optional 12-character minimum for privileged roles | Explicit yes/no decision; absent change, existing controlled default remains 8 | Must be resolved before privileged-role password requirement is frozen for implementation; does not silently change current baseline | Obtain explicit Project Owner decision and update security/decision records | **P0 / Phase 1 identity gate** |
| PCD-11 | Applicable formal authority/checkpoint acceptance of technical disposition B | Formal acceptance/disposition record referencing technical disposition B | Required for P0 checkpoint acceptance / Phase 1 entry; B is not itself formal acceptance | Obtain and record formal acceptance or controlled alternate disposition | **P0 / Phase 1 entry gate** |
| PCD-24 | Technical Authority laboratory input | Approved Launch Test Catalogue and >=3 validated golden cases per formula for pilot scope | Required before affected TestDefinition/formula/test configuration is implemented or becomes effective | Supply, review and approve catalogue + golden cases | **Dependent Phase 1 implementation gate** |
| PCD-25 | Quality + Technical Authority laboratory input | Approved QC Matrix, NABL scope mapping, report wording/template/watermark | Required before affected QC/test/report configuration becomes effective or reports become issuable | Supply and approve controlled report/QC/scope inputs | **Dependent Phase 1 implementation gate** |
| PCD-26 | Quality/Technical Authority/IT/lab input | Approved retained-sample periods/disposal authority, label-printer choice, real host/storage details | Required before affected sample-disposal/label/storage operational controls become effective | Collect and approve operational inputs; record hardware facts | **Dependent Phase 1 operational gate** |
| PCD-22 | Migration assessment | Controlled assessment of legacy sets and explicit "No Migration Required" where applicable | Explicitly not a P0 checkpoint entry prerequisite; final assessment is required at end of Phase 1 | Perform controlled migration assessment; never fabricate historical results/approval chains | **End of Phase 1** |

## Phase 1 entry determination

The controlled project position is:

1. **P0-CHECKPOINT formal acceptance is the overall Phase 1 entry gate.** The checkpoint remains OPEN / IN PROGRESS — NOT ACCEPTED until the required acceptance record exists.
2. The following are **P0 / Phase 1-entry-gate dependencies** because they are identified as required authority decisions or formal performance acceptance needed to obtain checkpoint acceptance: PCD-03, PCD-06, PCD-08, PCD-13, PCD-17, PCD-23, PCD-11 and the PCD-01 privileged-role option decision.
3. PCD-24, PCD-25 and PCD-26 are **dependent implementation/operational gates**. Their inputs must be approved before the affected test, formula, QC, reporting, sample-disposal, label or host/storage configuration is made effective. They are not authorization to begin implementation merely by being requested.
4. PCD-22 is **later Phase 1 work** by explicit controlled decision. The final migrate / No Migration Required assessment is performed at the end of Phase 1.
5. No pending item is treated as approved merely because it has an owner or a proposed action.

## Ownership rule
Where the project records identify a role rather than a named individual, that role is the required decision owner until the laboratory supplies the named Role-Holder Matrix. No individual is invented in this task.

## Acceptance evidence packet
Each closure record should contain, as applicable:
- decision/input reference;
- responsible authority/input provider;
- date/time;
- attributable signature or equivalent controlled approval evidence;
- affected policy/configuration version and effective date;
- supporting source/evidence reference;
- decision outcome and any conditions;
- impact on open items/risks/checkpoint state.

## Checkpoint rule
**P0-CHECKPOINT remains OPEN / IN PROGRESS — NOT ACCEPTED.** This follow-up plan does not create acceptance and does not authorize Phase 1 implementation.

## Non-authorizations
No application code, database schema, migration, API, UI, calculation, feature, production configuration, UAT, validation execution, or Phase 1 implementation was performed or authorized.

## Result
**Controlled Phase 0 follow-up plan established.** Outstanding dependencies are now separated into checkpoint/Phase 1-entry gates, dependent implementation gates, and the explicit end-of-Phase-1 migration assessment.

## Next proposed task
P0-TASK-011 — Collect and record the first available authority/laboratory decision packet against the controlled follow-up register, or another explicitly authorized Phase 0 control task.
