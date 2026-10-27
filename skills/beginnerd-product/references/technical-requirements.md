# PRODUCT-FOUNDATION-04 — Technical Requirements

**Trigger:** Clarify testable product-level quality requirements, technical constraints, interfaces and failure behavior before final solution design.

## Procedure
1. Read product requirements, acceptance, minimum viable product scope, user context and verified environmental constraints.
2. Define stable requirement IDs such as TECHNICAL-REQUIREMENTS-001 and links to source product requirements. Include priority, evidence or explicit assumption, observable behavior and **planned** verification.
3. Proportionately assess data handling/retention, authentication, authorization, privacy, integration, availability, consistency, performance, accessibility, platforms, operational budget and license constraints.
4. Describe negative cases: invalid input, unavailable network/provider, duplicate submissions, retries, unauthorized access, data recovery and relevant multi-device consistency.
5. If a requested number or guarantee is not evidenced, record **TBD**, its decision owner and the next validation checkpoint. Never invent service-level objectives, provider pricing, absolute safety or a "free forever" guarantee.
6. Check conflicts with approved product scope and request an informed material decision before revising any approved baseline. Technical component selection and threat modeling remain Solution ownership.
7. Produce PRODUCT.md or TECHNICAL-REQUIREMENTS-DOC.md when scoped file writes are authorized; read back the actual content and record version/provenance.

## Material requirement evidence contract
Every critical technical requirement needs:
**Product requirement ID → Technical requirement ID → Observable condition or TBD → Evidence/source → Planned verification (NOT EXECUTED) → Decision owner / handoff owner → Readiness status.**

| Product requirement link | Proposed technical requirement | Observable condition or TBD | Evidence/source | Planned verification (NOT EXECUTED) | Decision owner / handoff owner | Readiness status |
|---|---|---|---|---|---|---|
| REQUIREMENT_ID_PENDING | Private data access (PROPOSED) | Unauthorized access must be rejected; implementation controls TBD | Owner concern; controls not verified | Authorized negative access test after implementation | Product Owner for behavior, SOLUTION-07 for technical design | PROPOSED / SECURITY_UNVERIFIED |
| REQUIREMENT_ID_PENDING | Operating-cost constraint (PROPOSED) | Identify recurring cost and acceptable limit; budget TBD | User budget concern; provider terms not verified | Research hosting, network, storage and service costs | Product Owner for budget, SOLUTION-06 for feasibility | PROPOSED / COST_UNVERIFIED |

These rows are **examples**, not real approvals, prices, tests or guarantees. Reuse existing canonical IDs; if none exists, record a pending link instead of inventing acceptance.

### Proportional review

| Concern | Question to answer |
|---|---|
| Data & privacy | What data exists, who can see/change/delete it, and what recovery is needed? |
| Consistency & failure | What must happen after invalid input, outage, retry or duplicate action? |
| Availability | What user-observable behavior is expected across devices/services? |
| Performance & scale | Which user-load/capacity/latency targets are genuinely approved? |
| Accessibility | Which devices, input methods and accessibility needs are relevant? |
| Integrations | What permissions, third-party dependencies and fallback exist? |
| Security | Which product behaviors must be private, authorized and auditable? |
| Budget | Does "free" include recurring hosting, network, domains and future usage? |

**Do not merely list missing evidence.** Translate vague assurances into **PROPOSED** testable behavior with owner, evidence gaps and next decision. Ask novices about product value and tolerable constraints—not encryption algorithms or arbitrary uptime percentages.

## Separate readiness concerns
- **G1 Product Baseline**: Is the product behavior, acceptance and material scope understood and approved? Critical unresolved product conflicts prevent PASS.
- **G2 Solution Feasibility**: Can researched technology and architecture meet it? Owned by Phase 2 and not verified by this document alone.
- **Release / Operations Readiness**: Were real security controls, operating costs and deployed behavior tested? Phase 5–6 evidence is separate.

Use these distinctions internally; tell beginners the plain-language implications rather than raw gate codes. Do not claim TESTED from PLANNED verification or elevate readiness because a template exists.
