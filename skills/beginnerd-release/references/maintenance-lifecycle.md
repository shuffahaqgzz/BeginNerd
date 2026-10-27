# OPS-03 — Maintenance & Lifecycle Management

**Input:** Current approved decisions, source/QA/runtime environment evidence, authorized scope and risk classification.
## Procedure
1. Inventory live component versions, transitive deps, runtimes, base images, APIs, licenses, data lifecycle, costs and support status from actual environment.
2. Assess new advisory/EOL/license/API deprecation/cost/backup signal for **applicability**, exposure, exploitability, impact and compatibility before recommending change.
3. Research & Reuse First: use existing scanners/updaters/monitoring; no automatic major upgrades, service replacement or duplicative tooling because something is newer.
4. For change classify NO_ACTION_REQUIRED/MONITOR/RECOMMENDED/APPROVED_FOR_PLANNING/AUTHORIZED_FOR_EXECUTION/VERIFIED_COMPLETE/BLOCKED/REVIEW_REQUIRED.
5. OPS-03 can execute *routine* operations only inside scoped existing authorization. Code or formal tasks → PLANNING-02 and Phase5; material architecture → Phase2; incident → OPS-02.
6. Handle data retention/backups/deletion/privacy and cost with separate authority; never delete backups or resize critical capacity to save cost without explicit impact/approval.
7. Verify update compatibility/security and resulting behavior with real evidence; retain risk/decision history, avoid declaring VERIFIED_COMPLETE from successful package installation.

**Canonical output:** MAINTENANCE-RECORD.md or compatible existing tracker.
**Readiness/acceptance:** Evidence-based lifecycle disposition, no unauthorized task creation or destructive mutation.
**Safety:** Auth for deployment/secret/provider write is distinct from local coding/PR. If unavailable, propose only and label NOT_EXECUTED/UNVERIFIED; preserve rollback/evidence and route controlled changes to their owners.
