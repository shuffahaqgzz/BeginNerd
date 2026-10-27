---
name: beginnerd-release
description: Gunakan untuk Phase 6 BeginNerd: release readiness/candidate, rencana dan otorisasi deployment, controlled deployment/acceptance, monitoring, incident response, maintenance dan lifecycle governance. Wajib mendapat scoped release authorization sebelum mengubah hosting/provider bahkan untuk deployment privat.
---

# BeginNerd Release — Phase 6 Release & Operations

**Ownership:** RELEASE-01–03 and OPS-01–03. Design Phase 6 approved, but actual deployment/operations **must be independently verified**. This skill does not bypass G1/G2/Planning/Phase5 acceptance.

## Operating protocol
1. Explain before execute: clarify release candidate, environment, provider, audience/exposure, data/credentials, cost, potential impact, rollback and expected evidence. Check current canonical decisions + Phase 5 completion and risk disposition.
2. Choose relevant reference only:
   - RELEASE-01 → references/release-candidate.md
   - RELEASE-02 → references/deployment-authorization.md
   - RELEASE-03 → references/controlled-deployment.md
   - OPS-01 → references/monitoring-handoff.md
   - OPS-02 → references/incident-response.md
   - OPS-03 → references/maintenance-lifecycle.md
   - Overall release/ops review → references/release-readiness.md.
3. **Authorization:** Phase 5 code/PR approvals do NOT authorize a release. Any EXTERNAL_CREATE, DEPLOY_RELEASE, remote secrets changes or destructive operations require explicit scoped Owner permission naming provider/target, environment, audience, data, cost, change, rollback and time window if material. A private deployment still counts as deployment. Use scripts/verify_release_contract.py as read-only diagnostic; it does not enforce provider controls.
4. **Risk-based deployment:** select no deployment, isolated test, staging, controlled/gradual rollout or production based on approved risk and actual architecture, not user coding experience. Never assume network exposure or port use is safe. Preserve source/version and rollback evidence.
5. **Verify reality:** POST deployment checks must use actual host/provider evidence (version, endpoints, authorization, data integrity, monitoring and smoke). Planning, mocked check or CI PASS cannot establish actual deployment success. If no external runtime access or permission, status NOT_EXECUTED/UNVERIFIED.
6. **Operational handoff:** real monitoring, alert thresholds and ownership, backup/restore expectations, incident escalation and dependency lifecycle. Do not claim monitoring active just because a dashboard diagram exists.
7. **Incident/maintenance governance:** incident response OPS-02 and maintenance OPS-03 follow least authority, preserved evidence and extended bounded recovery BN-DEC-009.5M—separate Owner approval per corrective remediation attempt, max two, HARD STOP thereafter. OPS-03 may assess advisories, cost, license/EOL/data lifecycle but cannot create new formal tasks or change technology alone; route material code to PLANNING-02 and architecture to SOLUTION.
8. Hindsight session recall/retain only if verified and consented, canonical docs prevail; MEMORY_SYNC_PENDING if retain unacknowledged. No persistent memory containing secrets.
9. Final report distinguishes RELEASE_READY, DEPLOYMENT_VERIFIED, OPERATIONS_VERIFIED and MAINTENANCE_VERIFIED based on separate evidence; do not claim framework v1.0 release ready from this SKILL.md.

## Governance boundary
No Overclaim, Research & Reuse First, material user approval, stable task history, authorized rollback, no secret leakage or unauthorized external effects. references/agent-governance.md, references/research-reuse-policy.md and references/work-structure-policy.md apply.
