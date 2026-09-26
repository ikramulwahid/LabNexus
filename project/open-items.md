# LabNexus Open Items

| Ref | Open item | Required authority/input | Effect |
|---|---|---|---|
| P0-CHECKPOINT | Phase 0 formal checkpoint acceptance | Required project/authority acceptance record | Phase 0 remains open; implementation gate is not opened by documentation alone |
| PCD-03 | Detailed SoD Matrix v1 formal sign-off | Quality Authority + Project Owner; Technical review | Affected controlled workflows remain non-deployable until accepted |
| PCD-06 | Execution-start accreditation rule sign-off | Quality Authority + Technical concurrence | Affected accreditation behavior remains non-deployable until accepted |
| PCD-08 | Retention start/archive rule sign-off | Quality Authority + Project Owner | Retention-controlled behavior remains non-deployable until accepted |
| PCD-13 | Rework/retest/correction boundary and state-transition sign-off | Technical Authority | Affected execution states remain blocked from uncontrolled activation |
| PCD-17 | Competence model sign-off | Technical Authority | Competence-controlled actions remain dependent on acceptance |
| PCD-23 | Named Role-Holder Matrix | Project Owner + Quality Authority | Staffing/approval feasibility not yet confirmed |
| PCD-01 option | Privileged roles 12-character minimum: yes/no | Project Owner | Current controlled default remains 8 |
| PCD-24 | Launch Test Catalogue + golden cases | Technical Authority | No production formula/test configuration may be invented |
| PCD-25 | QC Matrix, NABL scope mapping, wording/report template/watermark | Quality + Technical Authority | Affected controlled tests/reports remain non-deployable |
| PCD-26 | Retained-sample period, disposal authority, label printer, host/storage details | Quality/Technical Authority/IT | Affected operational controls remain input-dependent |
| PCD-22 | Final migrate / No Migration Required assessment | Phase 1 migration assessment | No fabricated historical result/TestInstance migration |
| PCD-11 | Formal acceptance of technical disposition B | Applicable project/technical authority/checkpoint | SQLite baseline remains technically supported but not formally accepted |

## P0-TASK-011 decision-packet review — 26 September 2026

No new attributable authority acceptance or approved laboratory input was identified in the current GitHub `main` state or searchable repository issues/pull requests. All outstanding items therefore retain their prior controlled status.

No absence-of-record condition has been interpreted as approval.

## Security baseline note
PCD-01 privileged-role password length remains the principal security-specific open decision. PCD-03 and PCD-23 remain authorization/staffing acceptance dependencies.

## Domain-model note
PCD-05 and PCD-14 are confirmed controlled decisions. PCD-03 and PCD-13 remain subject to their stated authority sign-offs; the detailed PCD-13 transition matrix is a later Phase 1–2 deliverable.
