# RELEASE-03 — Controlled Deployment & Acceptance

**Input:** Current approved decisions, source/QA/runtime environment evidence, authorized scope and risk classification.
## Procedure
1. Recheck current scoped release authorization, approved source SHA/version, required QA, host isolation, data protection and rollback evidence immediately before execution.
2. Execute only allowed rollout actions against named environment; log change/version/provider response without leaking credentials.
3. Verify actual endpoint/version/critical user flows, authorization, data integrity, performance/availability signals and errors using relevant real smoke tests.
4. If smoke fails, halt or roll back according to approved procedure and authorization. Corrective repair follows separate Owner-approved 5M attempts; never auto redeploy repeatedly.
5. Record before/after, outcome and lessons; notify Owner of PARTIAL/BLOCKED instead of hiding failure.

**Canonical output:** DEPLOYMENT-EVIDENCE.md with rollout/rollback and acceptance refs.
**Readiness/acceptance:** DEPLOYMENT_VERIFIED only when live provider proof exists; CI/preview is insufficient.
**Safety:** Auth for deployment/secret/provider write is distinct from local coding/PR. If unavailable, propose only and label NOT_EXECUTED/UNVERIFIED; preserve rollback/evidence and route controlled changes to their owners.
