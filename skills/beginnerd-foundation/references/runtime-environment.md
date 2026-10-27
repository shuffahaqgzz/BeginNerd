# FOUNDATION-02 — Development Environment & Runtime

**Input:** Approved architecture/technology, Planning task registry, authorization boundary, current project/host evidence.
## Procedure
1. Inspect OS, CPU/memory/storage limits, language/runtime, package manager, container/services, ports, network restrictions, installed APIs/SDKs and existing env vars without printing secrets.
2. Match approved tech versions and platform compatibility; use existing runtimes if supported, avoid duplicate installation.
3. Explain changes and request PROVIDER_CONFIG permission for host/MCP/package installation, service startup or persistent config (separate from local repo writes).
4. Prepare isolated development configs with least privilege, data fixtures and rollback, never mutate production/shared UAT implicitly.
5. Run actual health/smoke/connection checks; distinguish 'installed' from 'working' and record versions, errors and evidence.

**Canonical output:** Development environment inventory and verified runtime checks.
**Foundation completion condition:** Every required local service has actual tested availability or explicit PARTIAL/BLOCKED.
**Guardrails:** Before mutations require permission for exact target, preserve current settings and rollback; no duplicate tooling or unapproved formal decomposition. An artifact/checklist does not establish actual host runtime PASS.
