# Owner Decisions — Reviewer Feedback T1–T7 (27 October 2026)

**Status:** OWNER APPROVED FOR SOURCE HARDENING. This records the Owner's latest explicit directions and their limits. These are design/implementation decisions, not proof of runtime acceptance.

| Finding | Approved outcome | Boundary |
|---|---|---|
| T1 — Internal jargon | Full words for abbreviated workflow identifiers; maintain internal technical IDs for traceability; default user-facing explanations must avoid internal codes | Historical evidence preserved through documented aliases; 32 workflow count unchanged |
| T2 — Approval fatigue | Risk-based approval; group material decisions; routine authorized work proceeds without redundant prompts | Separate explicit consent remains for external/provider/high-impact actions and per-attempt remediation after declared failure |
| T3 — Waterfall tendency | Internal implementation steps allowed inside an approved task; only material scope/formal structure returns to PLANNING-02 | Never permit unauthorized formal task creation |
| T4 — Product discovery | Add user interview, Jobs-to-be-Done when useful, competitor/alternative review, hypotheses, lightweight experiments, success measures and feedback loop | Extend existing Product and Operations responsibilities; no additional lifecycle workflow |
| T5 — Guardrails | Use harness/provider-side permissions/hooks for high-risk actions with safe negative testing | Text-only rules and offline scripts do not become enforcement; harness setup is separate and requires authorization |
| T6 — Effectiveness | Evaluate activation, user friction, task success, error recovery and safety using **existing** workflows/scenarios | No new mandatory workflow, artificial PASS or substitute for real E2E evidence |
| T7 — Language | Source skill descriptions, runtime instructions and new canonical material authored in **native English**; outputs are contextual to the user's language | Test bilingual routing, do not infer activation gains |
| T7 — Providers | Graphify and Hindsight enabled only when chosen through beginnerd-setup | No automatic installation, configuration or memory writes; existing canonical project evidence remains available |
| T7 — Duplicate references | Keep portable canonical snapshots as-is and continue snapshot parity checks | No centralized runtime dependency that breaks standalone skill installation |

## Follow-up acceptance

Source changes require static packaging/traceability tests. Runtime skill behavior and provider hooks require independent harness tests with safe mock/denied external mutations. Published source does not prove product impact. Study case A2 remains deferred by Owner.
