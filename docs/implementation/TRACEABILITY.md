# Design → Implementation → Verification Traceability

| Source decision / contract | Implementation reference | Verification reference | Runtime status |
|---|---|---|---|
| Companion ask routing | skills/beginnerd-ask/SKILL.md; references/routing.md | tests/behavioral/scenarios.json ASK-* | NOT EXECUTED |
| Companion setup and idempotence | skills/beginnerd-setup/SKILL.md; references/onboarding.md | tests/behavioral/scenarios.json SETUP-* | NOT EXECUTED |
| Graphify / Hindsight continuity | docs/governance/MEMORY-KNOWLEDGE-CONTRACT.md; setup provider-verification.md | tests/behavioral/scenarios.json MEMORY-* | NOT EXECUTED |
| Six phases / 32 workflows | docs/workflows/WORKFLOW-REGISTRY.md | tests/contracts/test_repository_contracts.py | STATIC TESTS PASS ON CANONICAL BOOTSTRAP; NEW CHANGES REQUIRE NEW CI |
| BN-DEC-009.3B decomposition | docs/governance/WORK-STRUCTURE-POLICY.md | tests/behavioral/scenarios.json GOV-* | NOT EXECUTED |
| BN-DEC-009.5M bounded recovery | docs/governance/AGENT-GOVERNANCE.md | tests/behavioral/scenarios.json GOV-* | NOT EXECUTED |
| Research/reuse | docs/governance/RESEARCH-REUSE-POLICY.md | tests/behavioral/scenarios.json REUSE-* | NOT EXECUTED |
| BN-DEC-009.6 operations | docs/architecture/FRAMEWORK-ARCHITECTURE.md | Future lifecycle acceptance | NOT IMPLEMENTED |

Record test dates, source hashes and actual environment refs when each row becomes executable. Do not pre-mark runtime tests as PASS.

## Phase 1 Product Foundation — Implementation Candidate

| Approved source | Workflow implementation | Static test / behavioral spec | Current acceptance |
|---|---|---|---|
| BN-DEC-009.1 Product Discovery | `skills/beginnerd-product/references/product-discovery.md` | `tests/contracts/test_product_skill_contracts.py`, PRODUCT-01/02 | NOT EXECUTED (runtime) |
| Product Requirements | `references/product-requirements.md` | PRODUCT-03/09, acceptance/traceability tests | NOT EXECUTED |
| MVP Definition | `references/mvp-definition.md` | PRODUCT-04/05/12 | NOT EXECUTED |
| Technical Requirements | `references/technical-requirements.md` | PRODUCT-07/08/15 | NOT EXECUTED |
| G1 Readiness | `references/g1-readiness.md` | PRODUCT-10/16, G1 static assertions | NOT EXECUTED |
| Lean/Structured naming & change control | `references/documentation-and-change-control.md`, five assets | PRODUCT-04/05/06/11 | NOT EXECUTED |

The above `references/...` paths are relative to `skills/beginnerd-product/`. Phase 1 source implementation **does not** imply G1 PASS for any consumer product.
