# Product Baseline Readiness — Internal G1 Review

**When:** The user requests a full Product Foundation readiness review or Phase 2 handoff. A single discovery/requirement question does not trigger an entire phase gate.

## Evidence criteria
1. The product problem, target people, outcomes and constraints are explicit and traceable to the source available.
2. Critical requirements have stable IDs, priorities and observable acceptance; missing user evidence is labeled **hypothesis**, not fact.
3. The minimum viable product identifies essential, deferred and excluded scope, including the riskiest assumption and proportionate learning/measurement plan.
4. Product-level technical requirements cover relevant reliability, data, privacy, access and cost constraints, with critical gaps assigned an owner.
5. Material product choices have explicit informed approval; there is one current canonical source per decision, not conflicting documents.
6. Risks, deferred hypotheses, unknowns and follow-up checkpoints remain visible.
7. No unresolved *critical* contradiction makes the approved product baseline unusable for the next design step.

## Distinguish product readiness from market evidence
Product Baseline Readiness can PASS for a clearly defined, approved design-ready product **even when market hypotheses are still to be tested**, provided those uncertainties and next validation steps are explicit and do not disguise a critical missing product decision. Never claim customer validation, product-market fit or experiment success without real evidence.

| Internal verdict | Interpretation | Handoff |
|---|---|---|
| PASS | Relevant product scope/decisions documented and supported, no blocking contradiction | Solution design may use the approved baseline |
| PARTIAL | Some scope usable, with open noncritical material choices or evidence gaps | State exactly which design exploration can proceed safely |
| BLOCKED | Critical product ambiguity, contradiction or unmitigated risk | Hold affected scope until owner review |

No template, document existence or static validator produces PASS by itself. A product-only approval does not authorize coding, provider installation or deployment.

## Review output
Provide criteria-to-requirement/evidence/status mapping for technical records; for novice conversation, summarize what is clear, what remains uncertain and the one practical next step. Use references/documentation-and-change-control.md when artifacts are persisted and verify real read-back. Distinguish Product Baseline, Solution Feasibility and Release / Operations Readiness—none implies the others.

If optional memory is disabled, the check uses canonical project evidence normally; absence of a provider is not a product blocker.
