# OPS-01 — Monitoring & Operational Handoff

**Input:** Current approved decisions, source/QA/runtime environment evidence, authorized scope and risk classification.
## Procedure
1. Identify service owners/operators, critical user functions, expected service levels, logs/metrics/health and retention.
2. Reuse existing monitors/alerts before installing new observability tools; choose signals and thresholds proportionate to risk, never invent SLOs.
3. Verify telemetry freshness and alert delivery when configured; distinguish planned dashboard from active monitoring.
4. Plan/run authorized backup and recovery checks as appropriate; document escalation, contacts/roles, manual procedures and limitations.
5. Record operational handoff acceptance or gaps, with action owners and next review trigger.

**Canonical output:** OPERATIONS-HANDOFF.md or existing runbook plus monitoring evidence.
**Readiness/acceptance:** OPERATIONS_VERIFIED requires observed signals, alert/restore evidence where in scope.
**Safety:** Auth for deployment/secret/provider write is distinct from local coding/PR. If unavailable, propose only and label NOT_EXECUTED/UNVERIFIED; preserve rollback/evidence and route controlled changes to their owners.
