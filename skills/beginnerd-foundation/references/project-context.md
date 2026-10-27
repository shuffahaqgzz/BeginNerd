# FOUNDATION-05 — Project Context & Knowledge Base

**Input:** Approved architecture/technology, Planning task registry, authorization boundary, current project/host evidence.
## Procedure
1. Inventory canonical documents, decision register, requirement/task/test references, owner approvals and current project status.
2. Build a compact index referencing authoritative current paths/commit rather than copying every document into a new knowledge store.
3. Verify freshness, source provenance, cross-project isolation and read scope if Graphify is available; setup and registration belong to beginnerd-setup.
4. At session start Hindsight recall only when consented and functional; verify against Git/canonical docs; retain meaningful changes and final checkpoint only when authorized.
5. If Graphify/Hindsight are absent, stale, cross-project leaking or unreachable, stop affected integration, mark PARTIAL/BLOCKED/MEMORY_SYNC_PENDING rather than claiming provider-ready.

**Canonical output:** PROJECT-STATE.md and knowledge pointers/manifest only if necessary.
**Foundation completion condition:** Knowledge is retrievable with verified scope; canonical docs remain source of truth.
**Guardrails:** Before mutations require permission for exact target, preserve current settings and rollback; no duplicate tooling or unapproved formal decomposition. An artifact/checklist does not establish actual host runtime PASS.
