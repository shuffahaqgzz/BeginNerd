# BeginNerd Decision Register — Known Approved Baseline

See [BN-DEC-009 Approved Details](BN-DEC-009-APPROVED-DETAILS.md) for explicit 5A–N, 6A–F, phase boundaries, and addenda.

This register captures decisions supported by the supplied BeginNerd source discussions. Do not invent absent decisions or treat historical proposals as new approvals. The canonical decision evidence should eventually be consolidated and versioned; source transcripts are not committed wholesale to this public repository.

| Decision | Recorded outcome | Status |
|---|---|---|
| BN-DEC-003 (historical) | Ask guidance preference at first use | APPROVED — DESIGN; SUPERSEDED FOR FIRST-USE BEHAVIOR by BN-DEC-003 revised, 28 October 2026 |
| BN-DEC-003 revised | Adaptive First-Use Guidance: help first, infer support needs, familiarity questions only when needed; familiarity never affects authorization, security, ownership or verification | OWNER DIRECTION APPROVED; SOURCE ACCEPTED — PR #15 MERGED (30 October 2026); RUNTIME NOT VERIFIED |
| BN-DEC-004 | Contextual Learning | APPROVED — DESIGN |
| BN-DEC-009.1 | Product Foundation, Hybrid Modular | CLOSED — DESIGN |
| BN-DEC-009.2 | UX & Solution Architecture, Hybrid Modular; Adaptive Visual Review, Best-Fit Recommendation, Adaptive Security Baseline | CLOSED — DESIGN |
| BN-DEC-009.3 | Planning & Control, Hybrid Modular; Adaptive Work Structure Brainstorming as PLANNING-02 addendum | CLOSED — DESIGN |
| BN-DEC-009.4 | Development Foundation, Hybrid Modular | CLOSED — DESIGN |
| BN-DEC-009.5A–N | Implementation & QA governance; 5M Extended Bounded Recovery with separately approved maximum two attempts | CLOSED — DESIGN |
| BN-DEC-009.6A–F | Release & Operations; Scoped Authorization, Adaptive Risk-Based Deployment, Operational Readiness, Incident Response, Lifecycle Governance | CLOSED — DESIGN |
| BN-DEC-009 cross-phase addendum | Research-First & Reuse-First, without new workflow | APPROVED — DESIGN |
| Companion skills | beginnerd-ask, beginnerd-setup across all phases | APPROVED — DESIGN |
| Knowledge & Memory (historical) | Graphify and Hindsight originally selected as required setup providers | SUPERSEDED FOR DEFAULT ONBOARDING by Owner T7, 27 October 2026 |
| Knowledge & Memory (current) | Graphify and Hindsight separately optional, opt-in through beginnerd-setup; enabled providers retain scoped recall/retain/isolation verification | APPROVED — CURRENT |

## Reviewer evaluation adaptation — 28 October 2026
Owner approved one scoped source-hardening batch in response to the beginner usability review of commit `78dd897`. Adopt bounded action lights without automatic local-write authorization, preserve phase ownership and separately approved two-attempt remediation, simplify artifacts, promote authorized task continuity and inactive deployment preparation, and add source regression cases. This is source change authorization via one PR, **not** runtime/provider/deployment/release approval or evidence that the review was independently reproduced. See [adaptation record](REVIEW-EVAL-2026-10-28-ADAPTATION.md).

## BN-DEC-003 revised — Adaptive First-Use Guidance (28 October 2026)
Owner decision on the familiarity-check proposal: **ACCEPT DESIGN DIRECTION — CHANGES REQUIRED** (change request FC-01 to FC-09). BeginNerd helps the user first, estimates the support needed from available context, and asks familiarity questions only when genuinely needed. Users are not required to choose a guidance mode to start and can change the explanation style at any time. Familiarity does not affect authorization, security, workflow ownership or verification. The original BN-DEC-003 approval remains part of the record; only its first-use mechanism (asking the user to choose a guidance preference) is superseded. The canonical contract is [Familiarity Guidance](../governance/FAMILIARITY-GUIDANCE-CONTRACT.md); see the [proposal record](PROPOSAL-ONBOARDING-FAMILIARITY-CHECK.md). Source acceptance **CLOSED** after validated merge of [PR #15](https://github.com/shuffahaqgzz/BeginNerd/pull/15) on 30 October 2026 (squash `30c094b`); runtime behavior remains **NOT VERIFIED** until executed scenarios have evidence.

## Public repository license decision
Owner choice **D2 — MIT License** on 27 October 2026. The license notice and public contribution guideline are included for source publication in PR #8; the selected license is MIT, without automatically implying runtime acceptance. This is a distribution/license decision; it does not amend BN-DEC-009 SDLC/skill ownership or validate third-party licenses. Confirm copyright holder and dependency-license obligations before an actual v1.0 release.

## Incomplete provenance
BN-DEC-001, BN-DEC-002, BN-DEC-005 through BN-DEC-008, and full supporting approval references are **NOT RECONCILED** in this bootstrap. No conclusions are invented for them. Use source records and owner review before claiming a complete decision register.

## Change control
For a material proposed change: identify affected requirements, skills, workflows and security, explain impact, interview the owner, record approval or rejection, update canonical references, then validate. A new implementation does not amend an approved design automatically.

## Repository status
Acceptance scenarios in docs and tests are specifications until a real agent/runtime executes them with evidence. The existence of SKILL.md is not proof of live invocation.

## Reviewer T1–T7 — Explicit Owner decisions, 27 October 2026
The Owner approved the source-hardening outcomes covering full-length workflow IDs, separation of internal identifiers from beginner-facing language, proportional approvals and iteration, product-validation techniques inside Product Foundation, harness-specific enforcement plans, evaluation through existing workflows, native-English source instructions, optional provider choice through beginnerd-setup and unchanged portable duplicate references. The canonical detailed record is [REVIEW-T1-T7-OWNER-DECISIONS.md](REVIEW-T1-T7-OWNER-DECISIONS.md). This is **not** evidence of live runtime acceptance or permission to deploy.
