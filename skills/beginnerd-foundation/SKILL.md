---
name: beginnerd-foundation
description: Gunakan untuk Phase 4 BeginNerd—repository baseline/scaffolding, development environment/runtime, code quality/tooling, agent harness configuration dan project context/knowledge readiness. Periksa existing tooling lebih dulu dan validasi Foundation Readiness tanpa membuat task atau mengubah sistem di luar scope.
---

# BeginNerd Foundation — Phase 4 Development Foundation

**Owner:** FOUNDATION-01–05 dan Foundation Readiness. Konsumsi G2+Planning Readiness+approved work structure dan teknologi. Foundation menyiapkan kondisi pengerjaan aplikasi; bukan pemilik product planning, formal task decomposition, application feature coding, atau release.

## Operating protocol
1. Jelaskan secara singkat target environment dan perubahan yang mungkin terjadi. Periksa canonical decisions, scoped task authorization, approved tech stack, current repo/host inventory sebelum melakukan instalasi atau scaffolding.
2. Single-workflow request boleh dijalankan tanpa memaksa lima workflow lainnya. Baca hanya reference relevan:
   - FOUNDATION-01 → references/repository-baseline.md
   - FOUNDATION-02 → references/runtime-environment.md
   - FOUNDATION-03 → references/code-quality.md
   - FOUNDATION-04 → references/agent-harness.md
   - FOUNDATION-05 → references/project-context.md
   - Final readiness → references/foundation-readiness.md
3. **Research/Reuse First:** bandingkan config, starter, dependency, installed skill dan host runtime. No duplicate install and no blind overwrite. Periksa compatibility, pinned versions, licenses, security, resources and existing lockfiles before installation.
4. **Authorization separation:** read-only audit allowed within scope. LOCAL_WRITE for scoped project files, PROVIDER_CONFIG for installing/changing runtimes/MCP/account, SECRET_ADMIN for secrets. Jangan menyamakan izin membuat PR dengan izin mengubah global Codex, provider Graphify/Hindsight atau host production.
5. For actual changes: snapshot existing (including ignored/untracked and modified files when authorized), approve target/diff/rollback, execute smallest changes, read-back and run actual smoke checks. Report result and affected paths. No invented test results.
6. FOUNDATION-04 menyiapkan AGENTS.md/registry/harness sesuai approved workflow, tetapi **beginnerd-setup** owns first-use preferences and installation/configuration Graphify and Hindsight. Foundation-05 may *consume* verified provider project context; do not mark setup PASS from a config file.
7. Security and quality defaults proportionate to risk, not user coding skill. No unapproved cloud provisioning or release. Adhere to references/agent-governance.md, references/research-reuse-policy.md and references/memory-knowledge-contract.md.
8. Evaluate Foundation Readiness based on real environment/repo/tool evidence. PASS only when relevant tooling works and scope/permissions accepted. PARTIAL/BLOCKED with explicit missing prereqs otherwise. Handoff to IMPLEMENT-01 on *approved* tasks only.

## Boundaries
- Do not create formal tasks/subtasks/work packages. Changes to approved plan return to PLANNING-02.
- No automatic global shell config changes, plugin registration, provider writes, secret rotation or deployment.
- Hindsight consented recall/retain with acknowledgement only if provider active; otherwise MEMORY_SYNC_PENDING or UNVERIFIED as applicable. Canonical docs supersede recall.
- Output includes source commit/runtime versions, inventory/diff, permissions, actual command/test evidence, statuses, missing tools and rollback path.
