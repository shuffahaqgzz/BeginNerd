---
name: beginnerd-foundation
description: Use this skill to inspect and prepare an approved project's repository, development runtime, quality tooling, coding-agent harness and project context, and to verify Foundation Readiness without modifying unrelated global settings.
---

# BeginNerd Foundation — Development Foundation

## Ownership and workflow references
- FOUNDATION-01: references/repository-baseline.md — repository and minimal scaffolding.
- FOUNDATION-02: references/runtime-environment.md — development environment.
- FOUNDATION-03: references/code-quality.md — standards, tests and tools.
- FOUNDATION-04: references/agent-harness.md — agent and harness configuration.
- FOUNDATION-05: references/project-context.md — project knowledge and source index.
- Read references/foundation-readiness.md for a requested readiness review.

## Procedure
1. Discover the existing repository, active branch, worktree modifications, runtime versions, environment, installed skills, tools, dependencies and project instructions **before** proposing changes.
2. Read the approved architecture/technology and Planning task registry. Reuse existing solutions rather than scaffolding or reinstalling duplicate tools.
3. Explain the smallest safe changes and any meaningful risks. Routine operations may use previously approved project/path/batch permissions; new provider installs, credentials, global configuration or externally hosted resources require their own approval.
4. Snapshot in-scope files (including permitted untracked and ignored paths), preserve rollback, and apply only the approved changes.
5. Verify actual startup/build/lint/tests and installed-skill discovery as applicable; report versions, logs, changed paths and gaps. Presence of config files is not proof that a tool is working.
6. FOUNDATION-04 manages **project coding-agent context**. First-use preferences and **optional Graphify/Hindsight installation** belong to beginnerd-setup. FOUNDATION-05 uses only providers that the user enabled and the runtime verified; otherwise rely on project files.
7. Handoff verified environment and project context to authorized implementation without treating Foundation Readiness as feature QA or deployment permission.

## Boundaries
Formal task creation belongs to PLANNING-02; changes to architecture belong to Solution. Never overwrite global harness settings or providers without separate consent. Never claim a shell sandbox protects an external plugin without verification. Explain internal codes as plain-language decisions for beginners. See references/agent-governance.md for action scopes.

## Authorized foundation progress and credential hygiene
Within an existing approved project/path/action batch, complete safe, reversible scaffolding and local checks without requesting approval for each internal step. Do not assume local writes, package installs, global harness changes, migrations or tests with external effects are automatically authorized. Inspect ignored/untracked files and existing tools. If a fixture contains a live token, reusable plaintext admin credential or genuine customer data, avoid copying/logging the value, stop risky exposure and recommend a separately approved rotation or secure-storage remediation. Never claim the provider credential was rotated until verified.

## Scoped workspace grant at Development Foundation
Check for the existing project-root grant, its owner-confirmed purpose and allowed local actions before scaffolding. Within approved foundation/tasks, reuse it for non-destructive local files and safe offline tests; do not ask again to create every config or source file. If none exists, propose a single root-scoped grant with rollback/exclusions instead of a chain of per-command approvals. Provider installation, global runtime configuration, external package downloads, data deletion and secrets operations are **not** covered by an ordinary local grant. Reuse existing tools and verify that no unrelated user files changed.
