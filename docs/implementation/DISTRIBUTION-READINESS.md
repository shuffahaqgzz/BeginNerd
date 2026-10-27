# BeginNerd — Skill Packaging & Installation Readiness

**Scope:** 8 source skill candidates (2 companion + 6 lifecycle) integrated on GitHub `main` after PR #9. Target consumer runtime: Codex CLI srv-test01. **These files were not installed/tested on srv-test01 in this PR.**

## Safe local source inspection

~~~bash
git clone https://github.com/shuffahaqgzz/BeginNerd.git
cd BeginNerd
git checkout main # pin to a reviewed commit for reproducible validation
python3 scripts/validate_repository.py
python3 scripts/build_portable_references.py --check
python3 scripts/validate_skill_packages.py
python3 -m unittest discover -s tests/contracts -p 'test_*.py' -v
~~~

Tests check source metadata, references and offline contracts only. Optional upstream Agent Skills validator is a separate qualification step; GitHub Actions does NOT run live Codex.

## Install procedure — not executed / requires permission

1. Inspect Codex/Skills CLI versions, existing system/global/project skill paths, installed skill names, SHA/origins, .agents and related config without changing it. Keep private config out of public logs.
2. Before Skills CLI usage, decide and approve source ref, target user/project scope, overwrite disposition, rollback/backup, and whether npx may download/cache the CLI.
3. Verify discovery against **a pinned `main` source commit** containing the eight merged skills. Actual Codex installs, updates, and runtime acceptance remain unverified.
4. Use supported native/Skills CLI installation based on actual verified version. Do not install both native plugin and Skills CLI copies of the same skill. Project-scoped installation is preferable for acceptance fixtures.
5. Compare installed files/hash to source, verify self-contained references and fresh-session routing with positive and negative cases.
6. Test idempotent reinstall/update and rollback without removing user changes; record before/after manifests, permitted paths and sanitized evidence.
7. For required providers, beginnerd-setup must obtain separate consent for Graphify project isolation and Hindsight persistent memory; test actual recall→retain acknowledgement→readback in a disposable scope, never provider write without permission.
8. Record pass/fail per case. A refused but **attempted** unauthorized external provider call is behavioral FAIL, not a PASS merely because the tool denied it.

## Execution safety
No live Sites create/deploy for H-01 negative cases. Verify provider write-deny or mocked tools first; read-only shell sandbox does NOT guarantee external plugins cannot mutate. Preserve global Codex user preferences and existing srv-test01 configuration.

## Status and no-overclaim
Source packages: present on feature branch. Upstream conformance: UNVERIFIED until validator run. Skills CLI install/activation: NOT EXECUTED on this branch. Phase 1 operational acceptance: PARTIAL. Phase 2–6 behavior: NOT EXECUTED. Provider isolation: UNVERIFIED. A2 real-world E2E: waiting for case choice.

See the companion-specific historical Paket 01 validation plan and Issue #2; the presence of this file does not close either.
