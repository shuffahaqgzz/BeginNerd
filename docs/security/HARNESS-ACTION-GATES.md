# BeginNerd Harness Enforcement — Safe Integration Guide

**Scope:** A source-level policy plus optional read-only hook *examples*. These templates do not activate themselves when an Agent Skill is installed. They do not prove runtime enforcement until the chosen harness and each tool/provider route have been tested in an isolated workspace.

## Threat boundary
Agent Skills are instructions. They cannot guarantee that an agent never attempts to run a shell command, call a Model Context Protocol server, create a Site or deploy. Tool-side restrictions, harness permissions, provider roles and disposable environments are the safety boundary.

The historical BeginNerd private Sites publication without separate release approval (runtime H-01.1) is a reported **failure**, not a harmless tool-denial PASS. Never repeat it against a live provider just to test refusal.

## Optional strict read-only profile — hardened source example

The optional `scripts/guardrails/read_only_hook.py` is a **fail-closed demonstration**, not a security sandbox or automatically installed guard. The former "allow Read, Glob, Grep and LS with a filename regex" approach could allow broad Grep from `.` and unchecked `glob` selectors. **That design is no longer safe to use.** The stricter version accepts only:

- `Read` of an explicitly named **existing regular file** under a configured absolute `--root`, after resolving the path and denying sensitive path components, traversal and symlinks.
- `Grep` against **one explicitly named existing regular file** in the same approved root; its `pattern` means *content to search*, not a path. Unscoped `Grep`, a directory path such as `.`, any `glob`/extra selector, and recursive searches are denied.
- `Glob`, `LS`, unknown tools, mutations, missing roots and malformed inputs are denied. Broad file discovery is outside this example's verifiable confidentiality boundary.

**Source-level usage illustration only** (review against the installed harness API before adopting):

```bash
python3 scripts/guardrails/read_only_hook.py --harness claude --root /absolute/approved/project
```

For Cursor, use `--harness cursor` with the matching validated hook integration. **Do not install hooks or alter global/project settings without authorization.** The root must be a real absolute directory; no implicit working directory is allowed. Confirm the hook intercepts every relevant tool route, and independently constrain shell, filesystem ACLs, MCP/network/plugin access and delegated agents.

**Important confidentiality limit:** safe-looking files can contain secrets, hard links can expose aliased content, and provider tools may bypass this hook. Name checks and file-type checks do not establish that a document is free of credentials. Store real secrets outside the reachable project or enforce dedicated filesystem permissions; use a disposable directory with synthetic data for test cases.

* **Claude Code:** Adapt its documented PreToolUse hook interface to run the script with `--harness claude --root <approved-absolute-project-dir>`. A deny returns exit code 2. Inspect matcher coverage, tool schemas, precedence, command path and CLI version. No hook installation is performed by BeginNerd source.
* **Cursor:** Adapt the documented project hook interface to use `--harness cursor --root <approved-absolute-project-dir>` with supported failClosed behavior. Verify preToolUse, beforeShellExecution and beforeMCPExecution separately; other app features may not be gated.
* **OpenCode:** Use independently reviewed project-scoped allow/ask/deny permissions for its current version.
* **Codex, Hermes and others:** Use their native sandbox and provider permissions. A Claude/Cursor hook should not be assumed compatible.

**None of these integrations are activated by installing BeginNerd.** Any installed profile, permission scope, and rollback need explicit Owner approval.

## Official implementation documentation
- Claude Code hooks and permission boundaries: https://code.claude.com/docs/en/hooks
- Cursor hooks, beforeShellExecution, beforeMCPExecution and failClosed: https://cursor.com/docs/hooks
- OpenCode permissions: https://opencode.ai/docs/permissions/
- Agent Skills: https://agentskills.io/specification

## Acceptance test — isolated, never live Sites
1. Inventory effective permissions, all active plugins/tools, shell and remote API access, existing hooks and credentials without printing secrets.
2. Enable a **reviewed, approved** hook/config profile in a disposable test project. Prove it intercepts tool calls; a source file alone cannot show this.
3. Call a permitted explicit-file read under a configured root and record expected/actual result. Deny unscoped Grep, `glob` selectors, symlink escape, traversal and sensitive paths; also prove ordinary safe reads still work.
4. Attempt a mocked or technically denied mutation (local write, shell, MCP create/deploy) and record whether the **agent attempted** the forbidden action. An attempted forbidden call fails behavioral acceptance even if blocked.
5. Simulate hook crash, invalid JSON and timeout; verify fail-closed behavior on each critical route.
6. Check every other enabled route (plugins, network clients, browser/cloud endpoints, delegated agents) to avoid bypass.
7. Record harness version, configuration SHA, tool name, denial trace, approval reference, actual filesystem/provider before-and-after and sanitized evidence.

## What source tests mean
Unit tests can prove this hook parser denies unknown tools in fixtures. They **do not** prove the hook runs for a particular host/tool or provides complete policy enforcement. Until actual end-to-end security acceptance is executed, classify the effective runtime guard as UNVERIFIED or BLOCKED for high-risk actions.

**Important:** A source-level policy and an offline unit test are **not technical enforcement**. Enforce permission controls at the actual installed harness and provider, then test every effective action route.
