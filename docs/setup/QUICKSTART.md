# BeginNerd — Repository & Runtime Quickstart

**Scope:** source inspection for eight skill candidates; this is not automatic installation or provider provisioning.

## Repository review
1. Identify base branch, source commit, expected changes and current project instructions.
2. On a **local, isolated checkout of the intended branch/commit**, run:

~~~bash
python3 scripts/validate_repository.py
python3 scripts/build_portable_references.py --check
python3 scripts/validate_skill_packages.py
python3 -m unittest discover -s tests/contracts -p 'test_*.py' -v
~~~

3. Inspect results, source and portable references. Confirm that all tests that passed were **static/offline**; do not call them runtime acceptance.
4. Check validation documents for known blocked/partial cases before requesting changes.

## Codex runtime use — requires separate scoped consent
- Target selected by Owner: srv-test01 Codex CLI, but this source work did **not** access that host. Do not infer CLI version, skill path or installed providers.
- Inventory existing skills/Graphify/Hindsight and global/project configs before changes, no duplicate install.
- For each install/overwrite use project/target permission; retain user preferences, backup and rollback. Never assume repo PR approval grants provider config or persistent memory writes.
- Perform fresh-session skill routing checks (positive and negative) and behavioral tests with sanitized tool traces; retain Hindsight only with consent and verified acknowledgement.
- Test H01 external-mutation refusal only with verified mocks/denial; do not create real Sites resources.

## Suggested phase test order
H02-03 remedial retest and Phase 1 acceptance → SOLUTION G2 → PLANNING approved Work Structure Agreement → FOUNDATION readiness → IMPLEMENT approved task QA → RELEASE separately authorized deployment + OPS evidence.

As A2 real-world case is deferred, use source static fixtures for now and preserve E2E as NOT EXECUTED. Learn more: docs/implementation/REAL-WORLD-E2E-VALIDATION.md.
