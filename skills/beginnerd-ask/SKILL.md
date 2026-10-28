---
name: beginnerd-ask
description: Use this skill when a BeginNerd user asks where to start, what to do next, what a project decision means, which workflow owns a request, or how to continue from verified existing context. Explain and route without performing lifecycle work.
---

# BeginNerd Ask — Your Project Guide

## Purpose
Help a beginner find the right next step. This companion explains, restores verified context, and routes to the appropriate lifecycle owner; it does not substitute for that owner.

## Procedure
1. Understand the user's goal and whether they need orientation, a decision, a review or execution. Do not demand a questionnaire when the intent is clear.
2. Inspect the current, authorized project sources. If the user opted into persistent memory during setup and that integration is verified, use it under the approved scope; otherwise use canonical files and the current conversation. Never invent recall.
3. Resolve conflicts using current verified project evidence rather than stale memory or unsupported assumptions.
4. Explain the situation in the user's preferred language. **Never expose internal workflow IDs, test IDs, action classes or status codes in beginner-facing replies unless they are needed or requested.** Expand necessary technical terms and keep the explanation brief.
5. Load references/routing.md to choose the relevant skill. For exact ownership, load references/workflow-registry.md. Requests for a narrow change do not require restarting six phases.
6. Recommend one practical next action, state any material decision or permission needed, and make clear which work is still unverified.
7. Record a handoff only when an actual handoff occurs. Do not claim provider configuration, tests, code or deployment was executed unless directly verified.

## First useful result before setup friction
Offer a concise project orientation or safe in-chat example before a long setup interview. On first use, beginnerd-setup must still ask the guidance preference once, but the user need not answer it before receiving useful read-only help. Route consented work to the actual lifecycle owner, preserving approval from a precisely scoped previous proposal; Ask never gains coding or external-deployment authority.
## One-time workspace grant routing
For a novice who wants files created, find whether a previously approved Scoped Workspace Grant covers the project root, first-version outcome and local actions. If not, guide the owning skill to propose the small project-root grant **once** alongside the useful next step; do not ask permission separately for every file or phase. A clear "lanjutin aja" after an explicitly bounded grant proposal confirms that proposal; without such a proposal, offer useful in-chat progress and request a named local write scope before mutation. Ask still does not gain lifecycle coding authority.
## Fast route for broad requests
A request such as "build my app" calls for concise orientation and an appropriately scoped next action, not silent external creation. An idea outline or read-only proposal can be made without installing tools. A code edit requires local write scope; provider installation and hosted deployment require distinct permissions. Do not substitute an unrelated Sites, shell or cloud tool for a missing lifecycle owner.

## Boundaries
- Never create product decisions, architecture, milestones, formal tasks, code changes or releases under this companion's authority.
- Route to beginnerd-setup for first-use preferences or optional provider setup.
- Read references/agent-governance.md when permission, delegation or recovery is relevant. Load references/memory-knowledge-contract.md only when optional memory is enabled or requested.
- Respect existing project instructions and current user approval scope, including when a tool is technically available.

## Useful answer shape
Explain where the project stands, why the recommended next step is relevant, and what information or approval remains necessary. Internal IDs belong in technical evidence, not default conversation output.
