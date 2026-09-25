# LabNexus Controlled Security Baseline

## Status
**CONTROLLED BASELINE — CONSOLIDATION COMPLETE; IMPLEMENTATION / VERIFICATION REMAIN PHASE-GOVERNED**

This document consolidates the security requirements from the governing Master Prompt and the approved pre-coding security decisions. It is a controlled baseline, not an implementation specification by itself.

## Authority and source relationship
- Governing project baseline: `../Main_Prompt.md` §§6, 7, 19 and 26.
- Reconciliation source: `../Decision_register.md` PCD-01, PCD-15, PCD-19, PCD-20 and PCD-21, including SB-AMEND-001.
- Living decision index: `project/decision-register.md`.
- Broader requirements and V&V history remain in `../PreCoding_Questions_v0.8.md`.

Where an older PQ answer conflicts with a later PCD decision, the later accepted PCD position governs the current baseline while the historical source remains preserved.

## Security objectives
LabNexus security is proportional to the approved single-site, Windows, LAN-capable, offline-first deployment. The security boundary is formed by:

```text
Authentication
+
Session security
+
RBAC
+
server-side authorization
+
per-TestInstance SoD
+
application/database access boundary
+
append-only audit controls
+
OS/filesystem protection
+
controlled operational mechanisms
```

The software must protect confidentiality, authorization integrity, auditability and historical reconstructability without adding enterprise security infrastructure that is outside the approved v1 architecture.

## 1. Authentication and password controls

### Password hashing
- Argon2id is mandatory.
- Plaintext passwords must never be stored or logged.

### Password baseline — PCD-01 / SB-AMEND-001
- Minimum password length: **8 characters**.
- Maximum accepted length: at least **64 characters**.
- Paste is supported.
- No mandatory composition rules.
- No periodic password expiry.
- Offline blocklist is mandatory, covering approximately the 10,000 most common passwords plus the username, laboratory name and `labnexus` variants.
- Lockout: 5 failed attempts → 15 minutes.
- Per-IP throttling is required.
- Password history: 5 previous passwords.
- MFA is **not required in v1**.

### Risk acceptance
The Project Owner's 24 September 2026 risk acceptance of the 8-character minimum is preserved from SB-AMEND-001. It acknowledges that the minimum is below current NIST guidance and relies on the compensating controls above together with the single-site/LAN/offline deployment boundary.

### Open password decision
A 12-character minimum for Approver, Authorized Signatory and System Administrator accounts remains an open project option. Until formally decided, the controlled default is 8 characters for all roles.

## 2. Session security

- Use secure server-side sessions; JWT is not the approved authentication architecture.
- Use secure cookie handling.
- Apply CSRF protection to state-changing browser actions as applicable to the chosen session/cookie design.
- Enforce the approved session lifecycle, including 30-minute idle timeout and 12-hour absolute session lifetime.
- Server-side authorization is authoritative; client/UI state is never a security boundary.
- Client clocks are not trusted for security decisions.

## 3. Authorization and segregation of duties

RBAC determines what a user may do in general. Per-TestInstance SoD determines whether that user may perform the action on the specific controlled record.

Mandatory hard blocks:

```text
Analyst → Review, same TestInstance       BLOCK
Analyst → Verification, same TestInstance BLOCK
Analyst → Approval, same TestInstance     BLOCK
```

The Technical Reviewer → Approval combination is policy-controlled. The Reviewer → Technical Verification classification remains explicitly governed by the current SoD decision record.

Rules:
- Hard SoD blocks have no bypass.
- Policy-controlled combinations require governed configuration and appropriate audit evidence.
- Backend/domain enforcement is authoritative. UI-only blocking is invalid.
- The System Administrator cannot approve technical results merely because the account may also hold another business role.

The formal SoD sign-off remains an open acceptance item under PCD-03.

## 4. Re-authentication and electronic-signature controls

### Fresh password re-entry — PCD-15
Fresh password re-entry is required for:

- Approval
- Reapproval
- Approval revocation
- Reopening an approved TestInstance
- Correction approval
- Report issue, reissue and withdrawal
- Controlled configuration approval, especially accreditation, SoD and formulas
- Role-assignment approval
- Emergency declaration and countersign
- Database restore

Review and Verification do **not** require fresh password re-entry, but they require full attributable electronic-signature evidence and server-side revalidation.

Approval may batch the full result set of one TestInstance in one controlled action.

Any future re-authentication window must be introduced by controlled change/UAT evidence; it is not an implementation assumption.

## 5. Database and filesystem security boundary

- Clients must never access SQLite directly.
- The database is accessed only through the application.
- The live SQLite database remains on local fixed disk; it must never be placed on NAS/SMB/network storage.
- Host filesystem permissions are part of the operational security boundary.
- Application errors must not expose SQL, stack traces, internal filesystem paths, secrets or credential material.
- Schema-level protections must not be represented as protection against a person with unrestricted access to the SQLite file or host filesystem.

## 6. Audit architecture — PCD-21 / Main Prompt §19

Audit is append-only from the application's perspective and protected at the database layer where the approved schema specifies trigger protection.

Authoritative write pattern:

```text
Application Service
→ assemble business change + audit event
→ repository persists both atomically
```

The project shall maintain one authoritative application audit write path.

### Transaction modes
- Normal business changes: audit event is persisted in the same transaction as the business change.
- Denied attempts: autonomous short audit transaction, because no business transaction is performed.

### Event ownership
- `approval_chain_event` records technical-record decisions: passed, failed with reason, revoked, countersigned.
- Permission denials, SoD denials and authentication denials are recorded in `audit_event`.
- Denial events are aggregated per source per minute to avoid uncontrolled audit flooding.

Important audit coverage includes authentication/security events, sample lifecycle, result submission, correction/reopen, review, verification, approval, report issue, configuration proposal/approval and accreditation-scope changes.

## 7. Controlled security mechanisms — PCD-19

### Malware / quarantine
- Uploaded files enter a quarantine area.
- Microsoft Defender `MpCmdRun.exe -Scan -File` is the approved offline-capable scan mechanism.
- Fail closed: an unscanned or failed file remains PENDING/QUARANTINED and must not enter trusted document processing.

### PDF generation
- Playwright for Python drives a pinned Chromium version shipped with the release bundle.
- The renderer operates with network access blocked and local fonts only.
- The PDF mechanism must not become an uncontrolled network/data-exfiltration path.

### Labels
- Code 128 or QR labels are generated as controlled SVG/HTML content and printed through the browser/Windows printer driver.
- No direct client access to the database is permitted for label generation.

### Windows services and scheduled operations
- WinSW hosts the approved application/Caddy services.
- Windows Task Scheduler runs backup, integrity and disk-check operations through the application CLI.
- Correctness/security decisions do not depend solely on a scheduler; time-based controls are evaluated from authoritative timestamps at read/action time.

### Runtime baseline
- SQLite runtime must be at least 3.35 and checked at startup.
- Python and the actual SQLite runtime version are recorded for the release/test environment.
- Antivirus exclusions are not created by default. If real-host testing demonstrates a need, any exclusion must be narrowly scoped, documented and limited to the database folder as approved.
- Unicode uniqueness uses normalized `*_key` values; SQLite `COLLATE NOCASE` is not used as a substitute for Unicode normalization.

## 8. Clock integrity — PCD-20

Only server time is authoritative; client clocks are ignored.

### Backward-jump guard
If the current server time is earlier than the latest recorded audit timestamp by more than 60 seconds:
- block Approval;
- block Report Issue;
- raise an alert.

### Drift guard
For the approval/report-issue actions:
- measured offset greater than 2 minutes → block;
- offset above 30 seconds → warn.

### Time source
Preferred source is Windows Time against the LAN/domain time source. A time-only outbound NTP rule may be used only if laboratory policy permits it. If no reference source is available, the administrator records a manual time check in the operations log; absence for more than 7 days produces a warning.

## 9. Security event handling and failure behavior

Security-sensitive failures must fail closed where the approved baseline requires blocking. Examples include:

- authentication failure/lockout;
- hard SoD violation;
- unauthorized action;
- invalid high-risk re-authentication;
- expired competence where the applicable domain policy blocks the action;
- untrusted/quarantined file;
- clock guard failure for Approval or Report Issue.

Denied actions must be auditable without creating unintended business-state changes.

## 10. Verification and validation expectations

Security verification will be performed in the project's controlled V&V sequence and must include, as applicable:

- password boundary and blocklist tests;
- lockout and throttling tests;
- session lifetime/expiry tests;
- authorization and SoD matrix tests;
- high-risk password re-entry tests;
- audit atomicity and denial-event tests;
- file/database access-boundary tests;
- quarantine fail-closed tests;
- clock-jump/drift guard tests;
- error-response checks ensuring secrets, SQL, stack traces and filesystem paths are not exposed.

No production security claim is made merely because a control is specified here. Implementation, test, independent verification and evidence are required before affected controls are treated as validated.

## 11. Security open items

| Item | Current status |
|---|---|
| PCD-01 privileged-role 12-character option | OPEN; current default remains 8 |
| PCD-03 SoD Matrix formal sign-off | OPEN acceptance item |
| PCD-23 named role-holder feasibility | OPEN input relevant to authorization controls |
| PCD-20 production/reference time-source selection | Controlled alternatives already defined; deployment-specific selection remains operational work |

## 12. Security boundaries and prohibited changes

This baseline does not authorize:

- JWT replacing server-side sessions;
- client-side or UI-only authorization;
- bypasses for hard SoD blocks;
- direct SQLite access from workstations;
- network-share live SQLite;
- arbitrary user code execution through formulas or document processing;
- uncontrolled external network access from the PDF renderer;
- production use of unapproved/unverified antivirus exclusions;
- speculative MFA/HSM/SIEM/Kubernetes/cloud security infrastructure outside the approved v1 scope;
- weakening audit or historical-reconstruction requirements for convenience.

## 13. Implementation boundary

This document defines the controlled security baseline. It does not itself authorize implementation. Future work remains subject to:

`PHASE → WORK PACKAGE → AUTHORIZED TASK → IMPLEMENTATION → TEST → VERIFICATION → EVIDENCE → CHECKPOINT`

Any later change to a frozen security control requires the applicable controlled change/decision process and must preserve the historical source record.
