# BeginNerd — Public Source Preview (27 October 2026)

**Publication type:** public source on GitHub `main`, not a tagged GitHub Release and **not BeginNerd v1.0 runtime acceptance**.

## Included source
- Eight Agent Skills source packages: `beginnerd-ask`, `beginnerd-setup`, and the six lifecycle skills `beginnerd-product`, `beginnerd-solution`, `beginnerd-plan`, `beginnerd-foundation`, `beginnerd-implement`, `beginnerd-release`.
- 32 approved SDLC workflow responsibilities and portable self-contained references/templates.
- Research-First/Reuse-First, Explain/Interview/Approve/Record, Planning-owned formal task breakdown, risk-based security/QA, bounded two-attempt remediation with separate approval, scoped deployment and operations lifecycle.
- Read-only offline authorization-check scripts. **They are advisory record validators, not runtime/tool-level enforcement.**
- MIT License, contributing/security guidance and evidence-oriented quality/readiness documentation.

## Verified source evidence
- Phase 1 source changes PR #7: merged to `main`; static CI PASS.
- Phase 2–6 source PR #9: merged to `main`; static CI PASS, **57 tests** on the reviewed PR head.
- MIT/documentation PR #8: source checks must PASS before integration.
- All versions/SHA in this preview must be checked against current `main` when consumed.

## Known limitations at publication
- **Phase 1 Product runtime acceptance remains PARTIAL / NOT ACCEPTED.** H02-03 fresh runtime retest, H03-01 authorized fixture write/readback and safely mocked H01 negative cases remain pending.
- Phase 2–6 live Codex routing, behavior and E2E are **NOT EXECUTED** by publishing code.
- Graphify knowledge isolation/freshness and Hindsight consented retain/ack/recall are **NOT VERIFIED**.
- Owner-selected `srv-test01` is NOT accessed or modified by these repository PRs.
- Owner intentionally deferred the A2 real-world case; greenfield and brownfield E2E remain NOT EXECUTED.
- Provider-side tool mutation restrictions, security-disclosure private channel and copyright/third-party license assessment still require validation.
- **No hosted application, GitHub Releases tag, production runtime or version v1.0 has been published through this source-preview record.**

## Source verification (static only)
```bash
git clone https://github.com/shuffahaqgzz/BeginNerd.git
cd BeginNerd
python3 scripts/validate_repository.py
python3 scripts/build_portable_references.py --check
python3 scripts/validate_skill_packages.py
python3 -m unittest discover -s tests/contracts -p 'test_*.py' -v
```

See [real-world E2E protocol](../implementation/REAL-WORLD-E2E-VALIDATION.md) and [framework release checklist](../implementation/FRAMEWORK-RELEASE-CHECKLIST.md). Do not use the public source-preview label as evidence of secure production readiness.
