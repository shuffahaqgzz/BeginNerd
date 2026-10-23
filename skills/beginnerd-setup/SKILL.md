---
name: beginnerd-setup
description: Onboard users into BeginNerd, choose guidance preferences, inspect existing configuration, and provision/verify project-scoped Graphify knowledge and Hindsight memory only with explicit authorization.
---

# BeginNerd Setup — Cross-Phase Companion

## Purpose
Prepare the BeginNerd user experience and knowledge/memory integration safely, adaptively, and without duplicating working installations. This companion does **not** own application repository scaffolding, language runtime provisioning, code quality tooling or application agent implementation; those belong to beginnerd-foundation.

## Invoke when
- First use of BeginNerd, when a new project is registered, or when the user explicitly requests setup/reconfiguration.
- A user wants to activate/deactivate project-scoped persistent memory, choose guidance style, troubleshoot Graphify/Hindsight setup, or validate cross-session continuity.
- An existing setup must be inspected or safely rerun.

## Setup contract
1. **Explain** what BeginNerd will configure, why, what may be stored or changed, and what will not be touched.
2. **Discover existing** runtime, installed skills, provider endpoints, existing memory/knowledge scope, configuration files and their provenance. Start read-only. Distinguish a valid existing setup from absent, incompatible or unverifiable.
3. **First-use interview.** On first use, ask the user to choose an AI guidance preference (actively guide versus recommendations on request) per BN-DEC-003. Apply contextual learning (BN-DEC-004). Clarify project identity/scope and preferred documentation depth only when relevant; preserve previously selected settings on rerun.
4. **Recommend** the least-change, best-fit setup, with alternatives, consequences, privacy implications and any infrastructure/configuration writes.
5. **Approve.** Get explicit scoped authorization before activation of persistent memory, provider installation/configuration, credential or filesystem write, and remote changes. A read-only audit is not approval for mutation.
6. **Configure only authorized changes.** Prefer reuse; do not reinstall, duplicate integrations, overwrite settings, expand data collection, or invent provider commands/endpoints.
7. **Functional verification.** Run the provider-native non-secret checks in references/provider-verification.md: Graphify scoped retrieval/freshness and Hindsight isolated retain→acknowledge→recall/read-back. Test safe rerun/idempotence and cross-project isolation where possible.
8. **Record result.** Report actual changed items and version refs, current guidance choice, permissions, evidence, provider readiness, unresolved issues, and PASS/PARTIAL/BLOCKED. Mark failed required memory sync MEMORY_SYNC_PENDING. A configured endpoint alone is not proof of integration.
9. **Handoff.** For application development foundation tasks, route to beginnerd-foundation. Send user intent/orientation questions to beginnerd-ask.

## Non-negotiable rules
- Existing settings are authoritative until changed by user approval.
- Graphify and Hindsight are the approved providers; do not silently substitute another provider.
- Do not write live user/project secrets or private memory into this public source repository.
- Readiness must reflect actual provider response. If required connectivity or consent is missing, do not claim full setup PASS.
- No autonomous corrective remediation beyond two separately approved attempts per issue after declared failure.
- Never claim session recall or retain when not called, inaccessible, or unacknowledged.

## References
Load references/onboarding.md when interviewing the user. Load references/provider-verification.md only when integrating or validating the providers. Follow AGENTS.md and docs/governance/MEMORY-KNOWLEDGE-CONTRACT.md.
