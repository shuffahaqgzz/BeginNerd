# BeginNerd — Repository and Runtime Quickstart

## Repository scope
This repository stores source and contracts for the BeginNerd framework. It does not automatically install skills in any specific runtime.

## Local review
1. Clone https://github.com/shuffahaqgzz/BeginNerd.git into an isolated workspace.
2. Check out the approved branch/commit and review README and docs/implementation/STATUS.md.
3. Run python3 -m unittest discover -s tests/contracts -p 'test_*.py' -v.
4. Run python3 scripts/validate_repository.py.
5. Only after approval, install skill directories according to the agent runtime's supported skill discovery path; do not guess the destination.
6. Compare installed beginnerd-ask and beginnerd-setup with existing copies before overwrite; preserve differences and any user configuration.
7. Run actual behavioral test scenarios (tests/behavioral/scenarios.json) and provider verification under explicit authorization.

## Setup mode
The companion starter skills describe the user-facing behavior but do not deploy Graphify or Hindsight. Provisioning requires a verified supported provider runtime, actual installation inventory, project-scoped consent and read-back tests.

## Git policy
Use PR-based integration, keep main protected according to owner preference, and never commit .env, tokens, private knowledge, or memory checkpoints. Branch protection settings require separate authorized admin configuration.
