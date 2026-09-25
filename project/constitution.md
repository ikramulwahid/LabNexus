# LabNexus Project Constitution

## Status
Phase 0 — IN PROGRESS.

This document is the project-control charter/index. It does not duplicate the full technical requirements in the source files.

## Authority and source hierarchy
1. `Main_Prompt.md` — governing project prompt, frozen architecture, development-control principles, roadmap, quality boundary.
2. `PreCoding_Questions_v0.8.md` — reconciled requirements/question history and R0.8 acceptance baseline.
3. `Decision_register.md` — pre-coding reconciliation decisions PCD-01…PCD-27 and their supersession/amendment records.
4. `project/` — living project-control layer created from those sources. It records current state, active work, open items, changes, risks, traceability and checkpoints and indexes the source material without replacing its historical record.
5. Approved ADRs, requirements, contracts, work packages/tasks, evidence and checkpoints become authoritative for their respective subjects once created and accepted under the project's control process.

A later accepted decision may supersede an earlier one only through the documented change/ADR/Laboratory Decision/Technical Decision/joint-approval mechanism. Historical source files are retained; supersession does not erase history.

## Development control
No implementation is authorized by a roadmap entry alone. Work follows:

`PROJECT → PHASE → WORK PACKAGE → AUTHORIZED TASK → IMPLEMENTATION → TEST → VERIFICATION → EVIDENCE → CHECKPOINT`

Current work is limited to Phase 0 project baselining. No application, database, API, UI, or feature implementation is authorized by this document.

## Control principles
- Do not invent laboratory policy, technical formulas, accreditation rules, QC criteria, or approval rules.
- Preserve historical reconstructability.
- Keep authoritative state in the repository, not in conversation history.
- Keep controlled documentation concise and reference source/history rather than duplicating it.
- Do not silently weaken frozen architecture, authorization, SoD, audit, integrity, or recovery controls.
