# BeginNerd Skills Inventory

Target: eight skills — two cross-phase companions plus six lifecycle skills covering exactly 32 workflow responsibilities.

| Skill | Type | Repository state |
|---|---|---|
| beginnerd-ask | Companion | Source installed; basic invocation reported on srv-test01; broader behavior unverified |
| beginnerd-setup | Companion | Source installed; read-only assessment reported on srv-test01; provider integration partial |
| beginnerd-product | Lifecycle Phase 1 | Source SKILL.md + PF references merged in PR #4/#6; runtime PARTIAL, NOT ACCEPTED |
| beginnerd-solution | Lifecycle Phase 2 | Design boundary only; implementation pending |
| beginnerd-plan | Lifecycle Phase 3 | Design boundary only; implementation pending |
| beginnerd-foundation | Lifecycle Phase 4 | Design boundary only; implementation pending |
| beginnerd-implement | Lifecycle Phase 5 | Design boundary only; implementation pending |
| beginnerd-release | Lifecycle Phase 6 | Design boundary only; implementation pending |

The two companion skills and product candidate bundle **generated snapshots** of relevant canonical governance, knowledge/memory, and/or readiness contracts under `references/`. Run `python3 scripts/build_portable_references.py --check` to detect drift. See `docs/engineering/SKILL-ENGINEERING-AND-DISTRIBUTION-STANDARD.md`.

Five lifecycle directories are still **NOT IMPLEMENTED**; do not count them as installable. Having a `SKILL.md` in `beginnerd-product` proves source availability, not runtime validation.

If actual installed ask/setup files exist outside this repository, treat the starter definitions here as candidates to reconcile, not exact copies. Keep configuration and modifications made by the user.
