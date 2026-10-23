# BeginNerd Skills Inventory

Target: eight skills — two cross-phase companions plus six lifecycle skills covering exactly 32 workflow responsibilities.

| Skill | Type | Repository state |
|---|---|---|
| beginnerd-ask | Companion | Starter SKILL.md with portable generated references; runtime invocation unverified |
| beginnerd-setup | Companion | Starter SKILL.md drafted; runtime invocation unverified |
| beginnerd-product | Lifecycle Phase 1 | Design boundary only; implementation pending |
| beginnerd-solution | Lifecycle Phase 2 | Design boundary only; implementation pending |
| beginnerd-plan | Lifecycle Phase 3 | Design boundary only; implementation pending |
| beginnerd-foundation | Lifecycle Phase 4 | Design boundary only; implementation pending |
| beginnerd-implement | Lifecycle Phase 5 | Design boundary only; implementation pending |
| beginnerd-release | Lifecycle Phase 6 | Design boundary only; implementation pending |

The two companion skills bundle **generated snapshots** of their shared canonical governance and registry dependencies under `references/`. Run `python3 scripts/build_portable_references.py --check` to detect drift. See `docs/engineering/SKILL-ENGINEERING-AND-DISTRIBUTION-STANDARD.md`.

Do not use a lifecycle directory as an executable skill until its SKILL.md, references, test contracts, and runtime evidence are added.

If actual installed ask/setup files exist outside this repository, treat the starter definitions here as candidates to reconcile, not exact copies. Keep configuration and modifications made by the user.
