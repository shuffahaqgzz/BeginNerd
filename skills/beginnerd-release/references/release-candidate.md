# RELEASE-01 — Release Readiness & Candidate

**Input:** Current approved decisions, source/QA/runtime environment evidence, authorized scope and risk classification.
## Procedure
1. Verify approved scope/requirement-to-code traceability, completed task acceptance, QA/security findings, dependency/license constraints and current source SHA.
2. Choose release candidate/version and build provenance; record artifacts, integrity, changelog and compatibility impact.
3. Ensure rollback data/migration strategy, backup and any blocking critical risk review; avoid shipping unverified code based on CI alone.
4. Present release readiness matrix and unresolved risk/Owner decision; PASS only for evidence within defined target.
5. Prepare candidate for RELEASE-02; do not deploy or tag/publish release without specific authorization.

**Canonical output:** RELEASE-CANDIDATE.md and evidence references.
**Readiness/acceptance:** Candidate reviewed separately from deployment readiness; no assumption a tag proves live release.
**Safety:** Auth for deployment/secret/provider write is distinct from local coding/PR. If unavailable, propose only and label NOT_EXECUTED/UNVERIFIED; preserve rollback/evidence and route controlled changes to their owners.
