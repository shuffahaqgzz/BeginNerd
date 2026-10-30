# BeginNerd Setup — First Use and Reruns

## First-use conversation (short and contextual)
1. Confirm project identity, user goal, current harness and permission for read-only inspection of existing settings.
2. Apply familiarity guidance (references/familiarity-check.md): use evident familiarity as a provisional level, otherwise the supportive Level 0, and ask a familiarity question only when it materially improves the next step. Derive the guidance style — **proactive coaching** (suggest relevant next steps and teach just-in-time) or **recommendation-first** (respond mainly to the user's stated goal) — from the level instead of asking the user to pick one. Run once per project, not on every session.
3. When relevant, or immediately when the user asks, offer **optional** project knowledge and/or persistent memory: neither, Graphify, Hindsight, or both. Do not promote them in a new beginner's first reply when the user only wants to build something. Describe privacy, stored data, costs and what works with no provider. Do not preselect either tool.
4. Inspect existing skills and provider registrations before suggesting install/updates. Reuse compatible setups.
5. Recommend minimal Lean or Structured documentation depth when relevant, but leave feature priorities, architecture and formal tasks to the appropriate lifecycle owner.
6. Group related material configuration requests. Obtain explicit provider/path/secret permissions for actual changes. No consent means NOT_ENABLED—not a setup failure.

## First useful result, then familiarity guidance
Give a short safe read-only orientation or in-chat illustration before any first-use questions. Then apply familiarity guidance: if the user's own words make the level clear, state the provisional level instead of asking; otherwise continue at Level 0 and ask at most the questions that materially help. Keep the level within the conversation unless project state may be written, and store it separately from the workspace grant. If a level or style is already recorded, reuse it. Graphify/Hindsight and persistent memory remain separately opt-in before any configuration or retain.
## Optional one-time project-folder consent
After providing an immediate helpful result, if writing agreed drafts or code would materially improve progress, show one short proposal with project-root path, version-one outcome, allowed offline actions, exclusions and how to revoke. The user may accept this specific proposal with "oke/lanjutin aja" without answering several prompts. Store the consent in existing project state and reuse it only for covered tasks; do not auto-enable memory/providers or assume global write access. If not approved, proceed with in-chat help.
## Rerun
Preserve valid existing preferences and scoped installation. If the user has chosen neither provider, skip Graphify/Hindsight checks and keep setup usable. For a selected provider, verify native read/write/isolation after separately authorized configuration, report direct evidence and failures. Never claim a provider works merely because it has a config entry.

## Internal status
- PASS: selected guidance and applicable approved setup functions verified.
- PARTIAL: a chosen integration is not yet fully verified.
- BLOCKED: a critical safety or permission condition prevents the selected action.
- NOT_ENABLED: optional provider deliberately declined; no failure.
- MEMORY_SYNC_PENDING: a required, approved Hindsight retain could not be confirmed.

Explain these outcomes in normal user language; do not show raw technical status codes unless asked.

## Handoff
State the familiarity level and derived guidance style, project scope, optional integration state, authorized changes and next relevant skill. Do not create application scaffolds here.
