# OPERATIONS-01 — Monitoring, User Outcomes and Operational Handoff

**Trigger:** A permitted release needs monitoring, operator handoff or a review of whether the product actually helps users.

## Procedure
1. Identify service operators, critical user journeys, known outcome hypotheses, privacy constraints and any already-approved success signals.
2. Reuse existing metrics, logs, alerts and feedback mechanisms. Never create tracking or collect user data without appropriate consent, lawful scope and explicit material approval.
3. Distinguish **system health** (errors, availability, latency) from **product effectiveness** (task completion, time to achieve value, drop-off, user-reported usefulness, rework). Propose only relevant, observable measures; don't invent baselines, targets or sample sizes.
4. Verify that telemetry/feedback was actually collected and is fresh and applicable. A dashboard design does not prove a running monitor or a real user result.
5. Compare observed outcomes against the approved Product Foundation hypothesis and note confounding factors and missing data. Summarize what seems validated, invalidated or still uncertain, with evidence limits.
6. Feed material learnings back to **PRODUCT-FOUNDATION-01** (problem discovery) and **PRODUCT-FOUNDATION-03** (minimum viable product scope) for a new, approved product iteration. This stays within existing lifecycle workflows—**no new effectiveness workflow**.
7. Verify owner handoff, alerts/escalation, incident response and recovery tests where in scope; record the actual evidence and next review point.

**Output:** Operations handoff and relevant product-outcome observations, preferably in the existing runbook or tracking source.
**Evidence requirement:** Actual measured data or explicit NOT EXECUTED / UNVERIFIED. Do not label operations or product-market fit as proven from a static plan.
**Safety:** External telemetry installation, private-data collection and deployment require appropriate separate authorization.
