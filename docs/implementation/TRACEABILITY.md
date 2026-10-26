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

## Phase 1 Hardening H-01/H-02/H-03 (26 Oct 2026)
| Contract / finding | Source implementation | Verification | Current evidence disposition |
|---|---|---|---|
| BN-H01-001 / BN-H01-002 lifecycle/release permission | PR #5, canonical agent governance + Ask/Product/Setup | H01-01..06 specifications | H01-01 retest BEHAVIORAL PASS on user-provided trace; H01-02..06 NOT EXECUTED |
| H-02 PF-04 complete evidence and error states | Product PF-04 reference and Lean/Structured templates (PR #6) | tests/contracts/test_phase1_hardening.py, H02-01..03 | STATIC CI pending PR-specific source acceptance; runtime NOT EXECUTED |
| H-03 scoped file write/readback | Product documentation-and-change-control reference; scripts/validate_phase1_artifact.py | H03-01/H03-03 and synthetic static fixtures | B-03 PASS QUALIFIED; full runtime regression NOT EXECUTED |
| H-03 workspace isolation evidence | scripts/audit_workspace_manifest.py | H03-02 and before/after manifest synthetic fixture | STATIC validation only; actual before/after in consumer workspace UNVERIFIED |
| BN-H01-004 external tool credential | Provider-side Sites operations, NOT BeginNerd source | Sanitized provider remediation evidence (unavailable) | EXTERNAL / OPEN; do not echo secrets |

Scenarios declared NOT_EXECUTED in tests/behavioral/scenarios.json remain specifications. Direct user-run behavioral evidence is recorded separately; the repository must not falsely relabel fixture definitions as executed.
