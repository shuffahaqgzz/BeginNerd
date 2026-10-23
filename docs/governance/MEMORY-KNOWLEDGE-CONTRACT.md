# Graphify & Hindsight — Knowledge and Memory Contract

## Design requirements
- **Graphify** is the selected required knowledge provider for relationships and cross-artifact discovery.
- **Hindsight** is the selected required persistent-memory provider for decision/context continuity.
- Canonical documents, Git and verified project evidence remain authoritative. Knowledge and recalled memory are secondary context, not authority.
- Existing provider instances should be inspected before any setup. Never duplicate installation or override current configuration without consent.
- Provider names are design choices; they do not imply local installation, credentials, availability, or successful integration.

## Every session (when configured and authorized)
1. Identify project identity and permitted memory/knowledge scope.
2. Recall the project checkpoint at session start via Hindsight. If unavailable, state it and continue only from verified canonical evidence.
3. Cross-check recalled details against approved documents, current repository, recent test evidence and timestamps; surface disagreements.
4. Retain meaningful decisions or state transitions as they occur.
5. Before session handoff or closure, retain an updated checkpoint and check provider acknowledgement.
6. If retention cannot be confirmed, report **MEMORY_SYNC_PENDING** rather than claiming success.

## Checkpoint fields
Project/work identity, objective, active scope, authorization, approved decisions, progress, references to evidence, unresolved blockers, next actions, update time and provider acknowledgement reference. Do not store credentials, secrets, or unneeded sensitive data.

## Setup verification matrix
- Provider discovery and existing-state inventory: MUST be executed, not inferred.
- Graphify project-scope retrieval: prove query returns expected seeded/non-sensitive test relation; verify scope isolation.
- Hindsight recall: prove saved disposable checkpoint can be recalled.
- Hindsight retain: verify acknowledgement and read-back in the same authorized project scope.
- Session continuity: compare refreshed context to canonical artifact and report conflicts.
- Failure handling: demonstrate honest PARTIAL / BLOCKED / MEMORY_SYNC_PENDING without fabricated provider success.

Use ephemeral test identifiers and approved environments; do not modify actual user history for test fixtures. Activation of persistent memory and any external provider writes require explicit authorization.

## Fallback
If required integration cannot be verified, setup verdict is PARTIAL or BLOCKED with clear affected behavior. Product documentation remains usable; never silently substitute Graphify/Hindsight with an unapproved provider.
