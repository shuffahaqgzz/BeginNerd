# BeginNerd Framework v1.0 — Source & Runtime Release Checklist

**Status:** NOT RELEASE READY. This is not a new SDLC quality gate; it reconciles actual verification needed for public software distribution.

| Dimension | Acceptance evidence | Current |
|---|---|---|
| 8 skill source | SKILL.md valid, references/assets self-contained, generated snapshot parity | Candidate; static CI must be checked |
| 32 workflow boundaries | Correct routing, no owner overlap, approval behavior | DESIGN APPROVED, runtime NOT EXECUTED |
| Beginner guidance | Contextual Learning, first-use guidance interview, appropriate routing | PARTIAL |
| G1 Product | H02-03 actionable constraints retest and H01/H03 negative/authorized write coverage | PARTIAL / NOT ACCEPTED |
| G2 Solution | Real requirement→design→security/cost decision and G2 check | NOT EXECUTED |
| Phase 3 Planning | Approved Work Structure Agreement, vertical slices, DoR/DoD/test strategy | NOT EXECUTED |
| Phase 4 Foundation | Installed versions, runtime, Codex/Graphify/Hindsight scoped integration | NOT EXECUTED |
| Phase 5 Implementation | Approved tasks, QA tests, no unauthorized task split, recovery attempts | NOT EXECUTED |
| Phase 6 Release/Ops | Separately authorized deployment, actual smoke, monitoring and lifecycle | NOT EXECUTED |
| Real-world greenfield | User-selected A2 case, full lifecycle and acceptance evidence | PENDING OWNER CASE |
| Brownfield | Existing repo safe reuse, preservation, controlled change/rollback | NOT EXECUTED |
| Security | Secrets scan, external mutation denial, disclosure route enabled and verified | PARTIAL / UNVERIFIED |
| MIT License | D2 approved; LICENSE included in PR #8, but copyright-holder/third-party review remains | SOURCE PUBLISHED / LEGAL REVIEW OPEN |
| Documentation | README, quickstart, limitations, contributing, privacy and source-preview notes | SOURCE PUBLISHED / RUNTIME GAPS DISCLOSED |
| Version/tag | Immutable tag, source/QA provenance, Owner scoped release authorization | NOT AUTHORIZED |

## Release procedure
1. Merge approved PRs through normal branch protection (never automatic).
2. Verify CI at final HEAD, skills CLI discovery/installation/rollback for tagged source and fresh Codex activation.
3. Perform actual greenfield and brownfield safe tests with non-sensitive fixtures and explicit provider permissions.
4. Resolve critical behavior, provider isolation, security findings and licensing/legal status or hold release.
5. Obtain Owner's separate release/tag/publication authorization. Only then cut version, publish release notes and declare verified scope.

Repository being publicly readable, having eight SKILL.md files or static CI SUCCESS alone never means RELEASE_READY.

## Reviewer hardening evidence still outstanding
Proposed source instructions and portable snapshots are not live evidence of usability or enforceable permissions. Acceptance needs bilingual prompt-routing tests, real-user validation evidence when appropriate, measurement of approval friction, permission negative checks on each target harness, and accurate reports when optional Graphify/Hindsight are disabled. These assessments belong to existing workflows; no new SDLC workflow is created.
