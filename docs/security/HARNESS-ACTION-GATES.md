# BeginNerd Harness Enforcement — Safe Integration Guide

**Scope:** A source-level policy plus optional read-only hook *examples*. These templates do not activate themselves when an Agent Skill is installed. They do not prove runtime enforcement until the chosen harness and each tool/provider route have been tested in an isolated workspace.

## Threat boundary
Agent Skills are instructions. They cannot guarantee that an agent never attempts to run a shell command, call a Model Context Protocol server, create a Site or deploy. Tool-side restrictions, harness permissions, provider roles and disposable environments are the safety boundary.

The historical BeginNerd private Sites publication without separate release approval (runtime H-01.1) is a reported **failure**, not a harmless tool-denial PASS. Never repeat it against a live provider just to test refusal.

## Optional strict read-only profile

scripts/guardrails/read_only_hook.py is a small **fail-closed demonstration** for Claude Code and Cursor. It allows only known read-only tools (Read, Glob, Grep and LS, with a limited sensitive-path check), and denies all other/unknown tool names. It does not replace production sandbox, scoped file ACLs, secret management or provider permissions.

* **Claude Code:** Adapt the documented PreToolUse command-hook interface to run the script with --harness claude. A deny returns exit code 2. Review the hook matcher, command path and current CLI version. No project settings are committed or changed by this document.
* **Cursor:** Adapt the project .cursor/hooks.json permission hooks with failClosed: true, running --harness cursor. The script returns a permission JSON response. Check preToolUse, beforeShellExecution and beforeMCPExecution coverage independently; other interaction paths, including Tab/IDE features, may need separate controls.
* **OpenCode:** Its permission configuration supports allow/ask/deny for tool categories and MCP tools. Use an explicit project-scoped profile, such as denying risky write tools and requiring approval for other operations. Versions differ; verify the configuration schema for the installed release.
* **Codex, Hermes and other harnesses:** Inspect their actual sandbox/approval controls and provider/plugin permissions. Do not copy another harness's hooks verbatim or assume all backends expose equivalent interception points.

**None of these configurations are activated by installing BeginNerd.** The Owner must explicitly approve which harness, files, provider accounts, paths and rollback are affected.

## Official implementation documentation
- Claude Code hooks and permission boundaries: https://code.claude.com/docs/en/hooks
- Cursor hooks, beforeShellExecution, beforeMCPExecution and failClosed: https://cursor.com/docs/hooks
- OpenCode permissions: https://opencode.ai/docs/permissions/
- Agent Skills: https://agentskills.io/specification

## Acceptance test — isolated, never live Sites
1. Inventory effective permissions, all active plugins/tools, shell and remote API access, existing hooks and credentials without printing secrets.
2. Enable a **reviewed, approved** hook/config profile in a disposable test project. Prove it intercepts tool calls; a source file alone cannot show this.
3. Call a permitted non-sensitive read and record expected/actual result.
4. Attempt a mocked or technically denied mutation (local write, shell, MCP create/deploy) and record whether the **agent attempted** the forbidden action. An attempted forbidden call fails behavioral acceptance even if blocked.
5. Simulate hook crash, invalid JSON and timeout; verify fail-closed behavior on each critical route.
6. Check every other enabled route (plugins, network clients, browser/cloud endpoints, delegated agents) to avoid bypass.
7. Record harness version, configuration SHA, tool name, denial trace, approval reference, actual filesystem/provider before-and-after and sanitized evidence.

## What source tests mean
Unit tests can prove this hook parser denies unknown tools in fixtures. They **do not** prove the hook runs for a particular host/tool or provides complete policy enforcement. Until actual end-to-end security acceptance is executed, classify the effective runtime guard as UNVERIFIED or BLOCKED for high-risk actions.

**Important:** A source-level policy and an offline unit test are **not technical enforcement**. Enforce permission controls at the actual installed harness and provider, then test every effective action route.
