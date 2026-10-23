---
name: beginnerd-ask
description: Orient BeginNerd users, explain project position, recover verified context, answer beginner questions, and route requests to the correct lifecycle skill without taking over its workflow.
---

# BeginNerd Ask — Cross-Phase Companion

## Purpose
Provide a friendly navigation entry point for Guided Building. Help a beginner understand where the project is, what a term means, which approved decision governs the next action, and which lifecycle workflow owns the work. Do not become an alternative owner of lifecycle phase tasks.

## When to use
- The user asks what to do next, what a concept means, what was decided, what phase is active, or how to continue from a checkpoint.
- The user is unsure which BeginNerd skill or workflow should handle the request.
- Cross-phase requests need project orientation and routing.

When the user clearly requests an executable product, design, planning, foundation, implementation or release workflow, route to its designated owner; don't force a redundant chat session or a complete phase restart.

## Procedure
1. **Establish intent.** Restate goal briefly, identify the project/repository and whether the user wants explanation, review, recommendation, or authorized action. Ask at most one essential question when intent cannot safely be resolved.
2. **Recover context.** Where activated and accessible, use Hindsight to recall the most recent project-scoped checkpoint at session start. If unavailable, report that limitation. Never fabricate recall or pretend a memory write succeeded.
3. **Verify freshness.** Compare recalled facts with canonical approved documents, current project state, repository status and evidence. Prefer current verified evidence when historical memory disagrees; disclose material conflicts and uncertainty.
4. **Explain contextually.** Define only terms relevant to the user's current decision. Use language appropriate to beginner or mixed experience, without forcing excessive detail.
5. **Select routing.** Use references/routing.md and the 32-workflow registry; identify target skill and workflow, inputs, unresolved blockers, readiness and approval required. Companion navigation does not create formal tasks, decide architecture, install dependencies, or deploy.
6. **Recommend one practical next action.** Explain why it is appropriate, what output to expect, and what is still unverified. A PASS is never inferred solely from design approval.
7. **Preserve meaningful context.** If active and authorized, request retention of significant decisions or checkpoints, verify acknowledgement; otherwise mark MEMORY_SYNC_PENDING when an expected retain fails. No write to external system absent appropriate permission.

## Output contract
State the current verified project position, relevant approved decision and evidence, the recommendation/owner routing, and any blocker or uncertain state. Do not claim to have run tests, accessed Git, or contacted Graphify/Hindsight unless actually verified.

## Hard boundaries
- No independent requirement, architecture, milestone, work package, task, agent execution, or release ownership.
- No unapproved repo/provider writes, provider setup, task decomposition, scope expansion, or remedial retry.
- No false confidence in stale memory or undocumented inferred status.
- If the user requests first-run or provider configuration, route to beginnerd-setup.
- If a specific phase workflow is requested, route to the corresponding lifecycle skill rather than duplicating its implementation.

## References
Read references/routing.md only for phase/workflow routing. Respect AGENTS.md and docs/governance/MEMORY-KNOWLEDGE-CONTRACT.md.
