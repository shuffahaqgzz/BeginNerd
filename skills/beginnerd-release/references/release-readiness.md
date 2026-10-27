# Phase 6 — Release, Deployment and Operational Readiness

Differentiate separate evidence scopes:
- **RELEASE_READY:** Approved product/change scope, supported candidate build, required Phase 5 QA and security findings reconciled, license/dependency provenance, rollback/backup and user release decision evidence.
- **DEPLOYMENT_AUTHORIZED:** Explicit provider/environment/audience/version/data/rollback approval. A private deployment is still external mutation.
- **DEPLOYMENT_VERIFIED:** Actual observed rollout in allowed target with live smoke/version/data/security checks; separate from approval.
- **OPERATIONS_VERIFIED:** Real monitoring/alert ownership and service runbook, backup/restore proof where relevant, response playbooks.
- **MAINTENANCE_VERIFIED:** A specifically authorized maintenance action and postchange tests confirm acceptance. Monitoring plan ≠ scheduled monitoring.
- **UNVERIFIED / NOT_EXECUTED:** No actual provider call/host trace, stale evidence, or missing ownership. Do not claim a release just because docs are complete.

Do not add new universal quality gate. Use scoped readiness, authorization, post-deploy acceptance and operations review independently. Critical risk/authorization omission BLOCKS affected deployment. Incidents and maintenance return material tasks to PLANNING-02 or architecture to SOLUTION.
