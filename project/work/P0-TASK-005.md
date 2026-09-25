# P0-TASK-005 — Consolidate SB-AMEND-001 into the Controlled Project Security Baseline

## Status
**COMPLETE**

## Authorization
Explicit project instruction dated 25 September 2026, conditional on successful P0-TASK-004 evidence closure.

## Objective
Consolidate the governing security requirements and approved PCD security decisions into a single controlled `project/security.md` baseline while preserving the historical source documents and their supersession history.

## Source set reconciled
- `../Main_Prompt.md` §§6, 7, 19 and 26.
- `../Decision_register.md` PCD-01, PCD-15, PCD-19, PCD-20 and PCD-21.
- SB-AMEND-001.

## Required outputs
1. Controlled `project/security.md` baseline.
2. Updated living decision/status record.
3. Updated current-state, handoff, changes and risks records.
4. Explicit security open items and implementation/verification boundary.

## Completion criteria
- [x] SB-AMEND-001 password baseline is consolidated.
- [x] PCD-15 re-authentication controls are consolidated.
- [x] PCD-19 security-relevant mechanisms are consolidated.
- [x] PCD-20 clock-integrity controls are consolidated.
- [x] PCD-21 audit write-path controls are consolidated.
- [x] Main Prompt security boundary and error-handling controls are preserved.
- [x] Historical root source documents remain unchanged.
- [x] Open security decisions are explicitly recorded.
- [x] No application/database/API/UI/schema implementation was introduced.

## Result
**Definition/consolidation complete.** The controlled security baseline is ready for its later implementation, test, verification and checkpoint stages.

## Next proposed task
P0-TASK-007 — Establish the controlled domain-model baseline for PCD-03, PCD-05, PCD-13 and PCD-14.
