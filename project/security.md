# LabNexus Security Baseline Index

## Current status
The v1 security baseline is governed by `../Main_Prompt.md` §§6, 7, 19 and 26 plus SB-AMEND-001 in `../Decision_register.md`.

## Current baseline
- Argon2id password hashing.
- Secure server-side sessions and secure cookie handling.
- CSRF protection and session lifecycle controls.
- RBAC + backend authorization + per-TestInstance SoD.
- Hard SoD blocks are not bypassable.
- Password minimum 8 characters; maximum accepted at least 64; offline blocklist mandatory; no composition rules or periodic expiry.
- Lockout after 5 failures for 15 minutes; per-IP throttling; password history 5.
- Fresh password re-entry for designated high-risk actions in PCD-15.
- MFA is not required in v1.
- Controlled secrets and host/filesystem protection.
- Backup encryption for removable/offline copies.
- Security/audit events and incident controls.

The password-length risk acceptance recorded in SB-AMEND-001 remains a controlled project decision.

## Phase 0 note
A full controlled `security.md` baseline was requested by PCD-09. This file is the canonical index; merging SB-AMEND-001 into a fuller security baseline is a subsequent Phase 0 task and is not performed under this baseline-only task.
