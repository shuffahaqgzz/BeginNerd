# BeginNerd — Public Release Readiness

**Status:** WORKING CHECKLIST / NOT RELEASE READY. Repository GitHub sudah publik; checklist ini membahas publikasi **versi rilis framework** yang terverifikasi, bukan perubahan visibility.

## Release exit criteria (no auto-PASS)
| Area | Minimum evidence | Status at 27 Oct 2026 |
|---|---|---|
| MIT License | Owner D2, LICENSE committed/merged and copyright holder reviewed | SOURCE INTEGRATED / COPYRIGHT REVIEW OPEN |
| Skill package conformance | All 8 installable skills have self-contained SKILL.md, references and assets, real validation results | SOURCE: 8 candidates; RUNTIME: NOT VERIFIED |
| 32 workflow contracts | Behavior and ownership mapped from approved BN-DEC baseline to implemented skills | DESIGN APPROVED, implementation pending |
| Phase 1 H02-03 / H01 / H03 | Verified runtime fixes, safe negative cases and authorized file persistence | PARTIAL/BLOCKED; PR #7 source merged, runtime retest pending |
| Companion providers | Graphify project-isolated read/freshness, Hindsight consented retain→ack→recall→readback | UNVERIFIED |
| Phase 2–6 acceptance | Per-phase real runtime cases and representative working product | NOT EXECUTED |
| Supply chain & licensing | Dependency inventory, third-party license compatibility, secret scanning | NOT VERIFIED |
| Public security contact | Private vulnerability reporting route configured and tested | PENDING OWNER SETUP |
| Portable install/upgrade | Skills CLI discovery, isolated install, idempotence, rollback, no duplicate installs | PARTIAL / NOT FULLY VERIFIED |
| Docs/examples | Quickstart, scope, prereqs, limitations, representative case and sanitized evidence | PARTIAL |
| Version/release tag | Immutable source version, release notes and release readiness | SOURCE PUBLICATION AUTHORIZED; STABLE v1.0 NOT READY |
| Deployment / operational readiness | Scoped deployment, rollback, monitoring and incident exercises on permitted environment | NOT EXECUTED |

## Acceptance procedure
1. Reconcile merged sources, installed SHA and current evidence; avoid reusing historical PASS outside its bounded scope.
2. Run static validators and provider-safe activation/behavioral tests in Codex on a controlled test fixture; log **attempted** forbidden tool use (not just provider denial).
3. Exercise one real-world greenfield product end-to-end through Phase 1–6 and one independent brownfield/reuse test where practical. Owner's A2 study case is not yet chosen.
4. Resolve critical vulnerabilities/authorization violations and track remaining risk honestly. No automatic third remediation after two separately authorized failed attempts.
5. Verify license notice and third-party obligations, publish private vulnerability reporting instructions, create sanitized release notes and a versioned source/tag **only after owner approval**.

**A CI SUCCESS, drafted checklist, pre-existing public repository or successful skill discovery is NOT a framework release verdict.** `LICENSE`, `CONTRIBUTING.md` and this checklist improve public repository hygiene but do not authorize tagging or release.
