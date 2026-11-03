# FOUNDATION-04 — AI Agent & Harness Configuration

**Input:** Approved architecture/technology, Planning task registry, authorization boundary, current project/host evidence.
## Procedure
1. Identify supported agent runtime and existing instruction/skills directories, permissions, installed MCP registration and current project-level AGENTS.md.
2. Compare existing agent/skill install sources and versions; prevent duplicate tool or skill registration and preserve user preferences.
3. Map approved tasks, decision precedence, read/write/provide config authorizations, sandbox, delegation and bounded-recovery restrictions into agent operating context.
4. Use minimal project-scoped configuration when needed and authorized; do not change global Codex settings or first-use preference as a side effect.
5. Check fresh-session discovery, skill references, tool allowlist and refusal of unauthorized mutation; a text instruction is not technical enforcement.
6. **Safety baseline for project agent context** (canonical text: "Project safety baseline" in references/agent-governance.md). When Foundation writes or updates the project's agent instructions (AGENTS.md or the harness equivalent), include these five lines so they apply even when no BeginNerd skill is loaded: (1) report a secret found in a file by location and type only, never its value, even when it looks fake; (2) do not open credential stores or dump whole harness configuration during discovery, and never open harness configuration files with any tool, shell command or script; (3) do not call memory or knowledge providers, including built-in harness memory tools, without the user's choice and consent, since a provider switched on in harness configuration is not that choice; (4) write code only for an approved task with its design, dependencies and execution authorization, and keep a revoked folder permission revoked until the user grants it again; (5) change global or harness configuration only after the user approves that named setting and scope.

**Canonical output:** AGENTS.md or existing agent instructions, AGENT-REGISTRY.md if useful, runtime verification evidence.
**Foundation completion condition:** Agent finds approved context in actual fresh session; provider write permissions independently verified.
**Guardrails:** Before mutations require permission for exact target, preserve current settings and rollback; no duplicate tooling or unapproved formal decomposition. An artifact/checklist does not establish actual host runtime PASS.
