# Paket 01 — Companion Skill Integration & Validation

## Scope
Validate beginnerd-ask and beginnerd-setup in an actual supported agent runtime against their declared contracts, then verify cross-skill routing and scoped Graphify/Hindsight integration.

## Stages and evidence
| Stage | Verification | Evidence |
|---|---|---|
| V01 | Inspect existing installations/configurations and source provenance | Inventory and file refs |
| V02 | Parse skill metadata, references and required repository content | Static CLI / CI output |
| V03 | Ask: project orientation without mutations | Recorded runtime prompt/output and target owner |
| V04 | Ask: ambiguous and cross-phase routing; missing context | Recorded routing cases |
| V05 | Setup: onboarding/guidance preference with explanations | Real user-facing flow transcript |
| V06 | Setup: rerun/idempotence, no duplicate install | Before/after inventory and diff |
| V07 | Graphify: scoped query, freshness and isolation | Provider-native evidence (sanitized) |
| V08 | Hindsight: recall, retain, read-back and failed-write handling | Provider-native evidence (sanitized) |
| V09 | Scoped authorization, No Overrule and no unapproved task decomposition | Adversarial behavior cases |
| V10 | Disposition/handoff and no-overclaim assertions | Matrix of actual results, blockers, current baseline |

## Safe execution
Initial audit is read-only. For provider write-tests, use a disposable project namespace after permission. Do not install, modify provider configuration, store private memory or commit test fixtures to a public repo without explicit authorization.

## Verdict logic
PASS: every applicable companion critical acceptance is verified in the actual runtime, with durable evidence; no unresolved critical blocker.
PARTIAL: useful results exist but integrations/behaviors remain unverified or pending.
BLOCKED: critical prerequisite missing or unsafe to proceed.
UNVERIFIED: claims lacking direct evidence, even when a document describes expected behavior.

CI static tests are insufficient to declare package PASS. Required proof includes actual invocation, plugin/provider behavior, and safe second-run testing.
