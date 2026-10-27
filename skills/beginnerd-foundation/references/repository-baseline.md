# FOUNDATION-01 — Repository Baseline & Scaffolding

**Input:** Approved architecture/technology, Planning task registry, authorization boundary, current project/host evidence.
## Procedure
1. Confirm repository identity, canonical branch, commit, clean/dirty state, existing files/CI/lockfiles and approved scope; flag unrelated changes.
2. Inspect existing skeleton/starter/dependencies; compare reuse versus new scaffolding and preserve established layout.
3. Explain proposed directory/module changes and compatibility/security/license risks; obtain LOCAL_WRITE for explicit project paths.
4. Make only approved minimal scaffold, with rollback/reference to previous HEAD and before/after manifest, without overwriting local edits.
5. Read back files, verify expected entrypoints/versioning and report hidden/untracked changes as far as inventory proves.

**Canonical output:** WORKSPACE-MANIFEST.md or current repo inventory plus applied baseline references.
**Foundation completion condition:** Repository skeleton runnable/testable when scope requires; no claim all features are done.
**Guardrails:** Before mutations require permission for exact target, preserve current settings and rollback; no duplicate tooling or unapproved formal decomposition. An artifact/checklist does not establish actual host runtime PASS.
