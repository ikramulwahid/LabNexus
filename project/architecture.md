# LabNexus Architecture Baseline Index

## Current status
The frozen architectural baseline is established in `../Main_Prompt.md` D-001…D-015 and §§5–30, with refinements in `../Decision_register.md` PCD-01…PCD-27.

## Frozen v1 stack
React + TypeScript + Vite + MUI; FastAPI + Python; SQLAlchemy 2.x; SQLite; Alembic; Argon2id + secure server-side sessions; RBAC + backend enforcement + per-TestInstance SoD; Caddy; Jinja2 + HTML/CSS + Chromium PDF rendering; pytest + Playwright; Code 128 + QR; Windows 11 Pro and/or Windows Server.

## Architectural principles
Modular monolith, single-host topology, offline-first operation, local fixed-disk live SQLite, explicit state machines, revision-aware controlled technical records, immutable audit/history, constrained calculation evaluation, historical report/result reconstruction, controlled configuration governance, and task/checkpoint-controlled implementation.

## Important reconciliations
PCD-04, PCD-05, PCD-06, PCD-10, PCD-13, PCD-14, PCD-18–21 refine the frozen baseline without reopening it. PCD-11 requires a performance spike to verify the workload premise; it does not reopen SQLite by itself.

## Phase 0 restriction
No schema, migration, API, UI, service, or application implementation is performed by the current task.
