# OPERATIONS-02 — Incident Response & Controlled Recovery

**Input:** Current approved decisions, source/QA/runtime environment evidence, authorized scope and risk classification.
## Procedure
1. Recognize symptoms and severity, source/time and affected data/service; avoid speculation or false root-cause claim.
2. Protect evidence and restrict exposure; use only pre-authorized safe containment, and request scoped incident action approval for material mutations.
3. Isolate affected environment, assess user impact and communicate facts, unknowns, owner and fallback.
4. Diagnostic read operations differ from corrective remediation; after verification failure follow 5M per-attempt separate approvals and maximum two approaches.
5. Verify service recovery with actual checks and post-incident review; do not claim restored if only commands completed.
6. Route product/architecture/task changes back to Phase 1/2/PLANNING-02; preserve incident timeline and secrets hygiene.

**Canonical output:** INCIDENT-RECORD.md with evidence, severity, authorization, recovery and remaining risk.
**Readiness/acceptance:** Close incident only with verified recovery or Owner-approved disposition; no forbidden auto third attempt.
**Safety:** Auth for deployment/secret/provider write is distinct from local coding/PR. If unavailable, propose only and label NOT_EXECUTED/UNVERIFIED; preserve rollback/evidence and route controlled changes to their owners.
