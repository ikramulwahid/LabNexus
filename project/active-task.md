# Active Task

## Task ID
P0-TASK-001

## Title
Establish Phase 0 Project-Control Baseline

## Status
**IN PROGRESS**

## Authorization
Explicit project instruction dated 24 September 2026 authorizing Phase 0 project baselining only.

## Objective
Convert the established LabNexus source/history documents into a small, persistent project-control layer that allows a new AI agent to continue the project without relying on conversation history.

## In scope
- Establish canonical `project/` structure.
- Preserve the three original source files.
- Create concise current-state, continuity, decision-index, open-item, change, risk, traceability and checkpoint records.
- Record the relationship between original PQ answers, PCD supersessions and current authority.
- Record current Phase 0 status and known outstanding decisions/inputs.
- Record this task as the active task.

## Out of scope
- Application code.
- Database schema or migrations.
- API implementation.
- UI implementation.
- Feature development.
- Production configuration.
- Test implementation beyond documentation/state verification needed for this baseline.

## Completion conditions
1. Canonical control files exist under `project/`.
2. Original source/history files are preserved.
3. Current state is explicitly Phase 0 — IN PROGRESS.
4. Outstanding approvals/inputs/deferred decisions are recorded without inventing answers.
5. Traceability/supersession relationship is documented.
6. No application implementation is introduced.
7. Checkpoint tracking exists and shows no accepted Phase 0 checkpoint.
8. Handoff allows a new AI agent to continue without conversation history.

## Evidence
Repository inspection and the resulting control-layer file set. Because repository write permission was unavailable to this session, the prepared file set is supplied as an application package rather than represented as already committed.

## Completion state
This task may be marked complete only after the control layer is inspected in the repository. That does not close Phase 0.
