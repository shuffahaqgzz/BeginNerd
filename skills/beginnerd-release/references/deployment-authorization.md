# RELEASE-02 — Deployment Planning & Authorization

**Input:** Current approved decisions, source/QA/runtime environment evidence, authorized scope and risk classification.
## Procedure
1. Inventory destination/provider, environment, network exposure, audience, DNS/ports, secrets, data, dependencies, operational cost and target runtime.
2. Compare low-risk options (isolated, staging, phased, production) and readiness/test evidence; define preflight checks, rollback/restore and abort triggers.
3. Explain expected effects and request explicit scoped Owner release authorization for provider, target, audience, data/cost, version, time/window and destructive steps if relevant.
4. Preserve baseline and least privilege; do not treat LOCAL_WRITE, PR approval, private visibility or action availability as deployment consent.
5. Confirm role permissions, provider technical deny/allowlist and backups when relevant. Missing approval → NOT_AUTHORIZED / HOLD.

## Default recommendation and inactive deployment preparation
When hosting is undecided, research one best-fit host/default based on approved architecture, self-hosting requirements, current cost/limits, data region, operational effort and rollback capability. Compare one short alternative; label unverified pricing and availability explicitly. Prepare a non-activating deployment checklist and placeholder config within authorized scope; do **not** create a live account, call the provider, push or deploy until specific separate RED authorization (provider/target/audience/data/cost/rollback). Deployment readiness is not deployment verification.
**Canonical output:** DEPLOYMENT-PLAN.md with exact scope authorization or PROPOSED status.
**Readiness/acceptance:** Approved plan does not imply deployment happened.
**Safety:** Auth for deployment/secret/provider write is distinct from local coding/PR. If unavailable, propose only and label NOT_EXECUTED/UNVERIFIED; preserve rollback/evidence and route controlled changes to their owners.
