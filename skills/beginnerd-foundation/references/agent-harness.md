# FOUNDATION-04 — AI Agent & Harness Configuration

**Input:** Approved architecture/technology, Planning task registry, authorization boundary, current project/host evidence.
## Procedure
1. Identify supported agent runtime and existing instruction/skills directories, permissions, installed MCP registration and current project-level AGENTS.md.
2. Compare existing agent/skill install sources and versions; prevent duplicate tool or skill registration and preserve user preferences.
3. Map approved tasks, decision precedence, read/write/provide config authorizations, sandbox, delegation and bounded-recovery restrictions into agent operating context.
4. Use minimal project-scoped configuration when needed and authorized; do not change global Codex settings or first-use preference as a side effect.
5. Check fresh-session discovery, skill references, tool allowlist and refusal of unauthorized mutation; a text instruction is not technical enforcement.

**Canonical output:** AGENTS.md or existing agent instructions, AGENT-REGISTRY.md if useful, runtime verification evidence.
**Foundation completion condition:** Agent finds approved context in actual fresh session; provider write permissions independently verified.
**Guardrails:** Before mutations require permission for exact target, preserve current settings and rollback; no duplicate tooling or unapproved formal decomposition. An artifact/checklist does not establish actual host runtime PASS.
