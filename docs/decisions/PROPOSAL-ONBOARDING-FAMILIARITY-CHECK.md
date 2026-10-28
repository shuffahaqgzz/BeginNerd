# Proposal — Onboarding Familiarity Check (28 October 2026)

**Status:** Owner design direction accepted with required changes (**ACCEPT DESIGN DIRECTION — CHANGES REQUIRED**, FC-01–FC-09). Source changes pending repository validation, CI and merge. Runtime behavior NOT VERIFIED. **Baseline:** `c3d74e9`. **Decision:** revises BN-DEC-003; see [Decision Register](DECISION-REGISTER.md).

## Problem
BeginNerd's intent is to guide users with no software-engineering background, and first use is meant to adapt guidance to what the user already knows. The baseline source does not do that:
- Onboarding asks the user to **choose** a guidance style (proactive coaching or recommendation-first). A beginner cannot judge that choice; in the reviewer's re-evaluation the persona answered "gue gak terlalu ngerti istilah-istilahnya, jadi ikut rekomendasi lo aja".
- Nothing establishes how familiar the user is with terminals, code hosting or putting software online, so explanation depth is never deliberately calibrated.
- The style question and the optional Graphify/Hindsight offer appeared only when the agent happened to route through setup, not when another lifecycle skill was invoked first.
- Reviewer re-evaluation of `c3d74e9` (24 sessions, blind; reviewer-reported, not independently reproduced) judged first replies heavy for a beginner.

## Accepted change
- One canonical contract, [Familiarity Guidance](../governance/FAMILIARITY-GUIDANCE-CONTRACT.md), generated into `references/familiarity-check.md` of all eight skills, so each independently installed skill applies it without another package (7 canonical sources, 46 portable copies).
- Help first; use evident familiarity as a provisional level, otherwise the supportive Level 0; familiarity questions zero by default, one when needed, at most three; answers never required.
- Three levels govern explanation, user-facing steps and choices presented, never the number of authorized internal operations. Guidance style is derived from the level; explicit user override always wins; topic-specific adaptation without global relabelling on a single weak signal.
- Minimal project-scoped guidance preference, stored separately from workspace authorization only where project state may be written; never in a memory provider without opt-in.
- Familiarity never changes authorization, security, ownership or verification.
- Graphify/Hindsight not promoted in a new beginner's first reply unless the user asks.

## Change request traceability
| ID | Requirement | Where addressed |
|---|---|---|
| FC-01 | Reconcile BN-DEC-003 with provenance | Decision Register, this record |
| FC-02 | First-use flow and conditional questions | Canonical contract; setup SKILL.md and onboarding |
| FC-03 | Portable contract in eight skills | Canonical contract, generator, portability test |
| FC-04 | Familiarity is not permission | Canonical contract; lifecycle SKILL.md paragraphs |
| FC-05 | Provisional, topic-specific and override adaptation | Canonical contract |
| FC-06 | Separate, minimal preference storage | Canonical contract; onboarding |
| FC-07 | Synchronize old tests and add regression coverage | SETUP-01, REVAL-13, REVAL-21–30, contract tests |
| FC-08 | Provider opt-in and documentation consistency | Memory contract, setup, README |
| FC-09 | Validators, unit tests, CI | Pre-merge evidence in the PR |

## Verification
Static contracts: `tests/contracts/test_onboarding_familiarity_check.py` and the updated portability test. Behavioral definitions SETUP-01, REVAL-13 and REVAL-21–30 remain **NOT_EXECUTED** until a matched multi-turn run in which the novice persona can answer familiarity questions, scored with an added rubric item: "was the user's familiarity established and then used to adapt the replies?"
