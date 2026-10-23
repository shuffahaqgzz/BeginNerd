# Design → Implementation → Verification Traceability

| Source decision / contract | Implementation reference | Verification reference | Runtime status |
|---|---|---|---|
| Companion ask routing | skills/beginnerd-ask/SKILL.md; references/routing.md | tests/behavioral/scenarios.json ASK-* | NOT EXECUTED |
| Companion setup and idempotence | skills/beginnerd-setup/SKILL.md; references/onboarding.md | tests/behavioral/scenarios.json SETUP-* | NOT EXECUTED |
| Graphify / Hindsight continuity | docs/governance/MEMORY-KNOWLEDGE-CONTRACT.md; setup provider-verification.md | tests/behavioral/scenarios.json MEMORY-* | NOT EXECUTED |
| Six phases / 32 workflows | docs/workflows/WORKFLOW-REGISTRY.md | tests/contracts/test_repository_contracts.py | STATIC TEST PENDING |
| BN-DEC-009.3B decomposition | docs/governance/WORK-STRUCTURE-POLICY.md | tests/behavioral/scenarios.json GOV-* | NOT EXECUTED |
| BN-DEC-009.5M bounded recovery | docs/governance/AGENT-GOVERNANCE.md | tests/behavioral/scenarios.json GOV-* | NOT EXECUTED |
| Research/reuse | docs/governance/RESEARCH-REUSE-POLICY.md | tests/behavioral/scenarios.json REUSE-* | NOT EXECUTED |
| BN-DEC-009.6 operations | docs/architecture/FRAMEWORK-ARCHITECTURE.md | Future lifecycle acceptance | NOT IMPLEMENTED |

Record test dates, source hashes and actual environment refs when each row becomes executable. Do not pre-mark runtime tests as PASS.
