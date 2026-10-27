# BeginNerd Skill Source Inventory

**Approved design:** 8 skills (2 companions + 6 lifecycle) / 32 workflows. Semua 8 direktori memiliki SKILL.md pada branch source kandidat ini, namun keberadaan file bukan kelulusan runtime.

| Skill | Phase | Source status | Runtime status |
|---|---|---|---|
| beginnerd-ask | Companion navigation | Packaged | Basic invoked (Owner report); full acceptance UNVERIFIED |
| beginnerd-setup | Companion onboarding | Packaged | PARTIAL; Graphify/Hindsight not provider-verified |
| beginnerd-product | Phase 1 (PF-01–04) | Packaged (PR #4/#6) | PARTIAL / NOT ACCEPTED, H02-03 remediation in PR #7 |
| beginnerd-solution | Phase 2 (SOLUTION-01–08) | SOURCE CANDIDATE | NOT EXECUTED in Codex |
| beginnerd-plan | Phase 3 (PLANNING-01–04) | SOURCE CANDIDATE | NOT EXECUTED in Codex |
| beginnerd-foundation | Phase 4 (FOUNDATION-01–05) | SOURCE CANDIDATE | NOT EXECUTED on actual host |
| beginnerd-implement | Phase 5 (IMPLEMENT-01–05) | SOURCE CANDIDATE | NOT EXECUTED on actual app |
| beginnerd-release | Phase 6 (RELEASE-01–03/OPS-01–03) | SOURCE CANDIDATE | NOT EXECUTED against actual provider |

Portable packages have local canonical-reference snapshots under references/. Use the generated snapshot parity script to catch drift. Five lifecycle candidates cannot be called VERIFIED merely because their source is present or static CI passes.

The script examples inside beginnerd-implement and beginnerd-release perform **read-only advisory JSON checks**. They do not replace real tool-side authorization/sandbox, actual QA, deployment, or incident controls.

Do not use global installation or provider configuration without scoped approval. See distribution-readiness and validation plan. If installed copies have custom modifications, reconcile before overwrite.
