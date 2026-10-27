# Use BeginNerd with your AI agent

**BeginNerd is harness-neutral at the skill-package level.** The same eight `skills/beginnerd-*/SKILL.md` directories are meant to be consumed by any harness that implements the [Agent Skills specification](https://agentskills.io/specification). No wrapper/plugin per platform is required merely to read these skill files.

**Compatibility scope:** documented discovery/install locations, not proof of actual BeginNerd workflow execution on every agent. This document separates format support, installer support, actual host discovery, and runtime acceptance. Verified on the project source and official harness/installer documentation as of **27 October 2026**.

## Start here — one installer for supported agents

Requires a compatible Node.js runtime for the [Skills CLI](https://github.com/vercel-labs/skills); its current docs specify Node.js 22.20+.

```bash
# Read-only skill discovery from BeginNerd GitHub source; may download CLI into npm cache
npx skills@latest add shuffahaqgzz/BeginNerd --list

# Select compatible agent(s), skills, and project scope interactively
npx skills@latest add shuffahaqgzz/BeginNerd
```

You can target exactly one harness with `-a`:

```bash
# Run ONE line appropriate to your current harness
npx skills@latest add shuffahaqgzz/BeginNerd -a claude-code
npx skills@latest add shuffahaqgzz/BeginNerd -a codex
npx skills@latest add shuffahaqgzz/BeginNerd -a cursor
npx skills@latest add shuffahaqgzz/BeginNerd -a opencode
npx skills@latest add shuffahaqgzz/BeginNerd -a hermes-agent
```

The CLI's default is **project-scoped** installation; `-g` changes scope to global. Don't add `-g` unless you explicitly want it. `npx` may fetch the CLI from the network/cache, so review its source and version when relevant. Inspect existing installs before updates to avoid duplicates or overwriting personal modifications.

## Compatibility matrix

| Harness | Skills CLI `-a` | Project paths recognized / installed to | Source-level support | BeginNerd runtime acceptance |
| --- | --- | --- | --- | --- |
| **Claude Code** | `claude-code` | `.claude/skills/<name>/SKILL.md` | Agent Skills documented | Not yet verified here |
| **Codex** | `codex` | `.agents/skills/<name>/SKILL.md` via Skills CLI | Agent Skills documented | Phase 1 partial on separate pilot, not overall PASS |
| **Cursor** | `cursor` | `.agents/skills/<name>/SKILL.md` via Skills CLI; `.cursor/skills/` native | Agent Skills documented | Not yet verified here |
| **OpenCode** | `opencode` | `.agents/skills/<name>/SKILL.md` via Skills CLI; `.opencode/skills/` native | Agent Skills documented | Not yet verified here |
| **Hermes Agent** | `hermes-agent` | `.hermes/skills/<name>/SKILL.md` via Skills CLI; `~/.hermes/skills/` native | Agent Skills + Hermes Skills Hub documented | Not yet verified here |
| **Other supporting harnesses** | See [supported agent IDs](https://github.com/vercel-labs/skills/blob/main/docs/agents.md) | Follow that harness's loader rules | Conditional on Agent Skills support | Not automatically verified |

**Path caveat:** Native harnesses can scan multiple equivalent directories. The project paths above reflect the Skills CLI and official docs, not a requirement to create all variants. Choose **one canonical install per harness**, then confirm which copy wins precedence. A Codex/Claude plugin/other skill distributor can expose a duplicate name; do not blindly install twice.

Primary sources: [Skills CLI supported agents](https://github.com/vercel-labs/skills/blob/main/docs/agents.md), [Skills CLI options](https://github.com/vercel-labs/skills/blob/main/docs/commands.md), [Claude Code skill docs](https://code.claude.com/docs/en/skills), [Cursor skill docs](https://cursor.com/docs/skills), [OpenCode skill docs](https://opencode.ai/docs/skills), and [Hermes Skills System](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md).

## Hermes Agent — native alternative

Hermes supports native skill taps from a GitHub repo whose skill directories sit under `skills/`. BeginNerd already has this layout. From a Hermes installation:

```bash
hermes skills tap add shuffahaqgzz/BeginNerd
hermes skills search beginnerd
hermes skills inspect shuffahaqgzz/BeginNerd/beginnerd-ask
hermes skills install shuffahaqgzz/BeginNerd/beginnerd-ask
hermes skills list
```

This is a **separate alternative** to `npx skills ... -a hermes-agent`; do not combine both routes for the same installed skill unless you deliberately manage duplication.

Hermes can also load skills from project `.hermes/skills/` or `.agents/skills/`. To activate project-local skills the first time, Hermes requires you to **review and trust that repository** (for example `hermes skills trust` inside the project). Do not trust arbitrary repositories automatically. Project/local/external precedence and security scan/quarantine also apply.

If you share a skill path between harnesses, Hermes's external-directory feature can see the same source tree; it may be **writable** by Hermes tools unless filesystem permissions or provider controls prevent that. Avoid giving uncontrolled write access to shared skill packages.

## Other Agent Skills harnesses / manual install

For a harness with no Skills CLI adapter, review its native loader documentation first. If it supports the Agent Skills format, supply complete skill folders—not only `SKILL.md`—to the configured skills root:

```text
<your-harness-skills-root>/
  beginnerd-ask/
    SKILL.md
    references/
  beginnerd-setup/
    SKILL.md
    references/
  beginnerd-product/
    SKILL.md
    references/
    assets/
  ... six lifecycle skills in total ...
```

The source also contains optional `scripts/` and `assets/`; copy them with each package. A harness needs to:
1. Discover `SKILL.md` with `name` and `description` frontmatter.
2. Make referenced local files available when requested (progressive disclosure).
3. Respect user/project configuration, file permissions, and workflow instructions.
4. Offer an actual interface for external tools, memory and authorization when required. **Installing a skill does not install Graphify/Hindsight or provide any MCP tool automatically.**

Invocation is harness-specific: some skills are auto-selected, others can be named in chat or called with slash syntax. Never claim that `/beginnerd-ask` works on *every* tool. A portable prompt is: *“Use beginnerd-ask to orient this project and explain the next step.”*

## What to check after installation

For **each harness and an isolated test workspace**, record the following as separate results:

| Check | Expected evidence | Can static CI prove it? |
| --- | --- | --- |
| Source package | Eight local `SKILL.md`, references, no broken links | Yes: package validator |
| Discovery | Harness enumerates the eight skill names from the selected location | No |
| Activation | Positive prompts route to the correct skill; negative prompts do not | No |
| Context | Skill loads references and respects approved decision ownership | No |
| Mutation boundaries | Attempts to write/deploy without authorization are avoided; permissions enforced by tools | No |
| Provider continuity | Graphify project isolation, Hindsight consented retain/ack/recall | No |
| Full lifecycle | Phase 1–6 application acceptance against an Owner-selected real case | No |

Current baseline: portable source validation in GitHub Actions has passed; the original first acceptance environment was **Codex CLI on `srv-test01`**, a test choice **not a platform restriction**. That pilot is not complete, and no independent Claude Code/Cursor/OpenCode/Hermes acceptance has been run here. Owner has deferred the end-to-end real-world case.

## Keep installs under control

- Prefer a single, **project-scoped** copy when beginning; preserve user modifications and existing provider configs.
- Pin source revisions for reproducibility; document the installed source SHA for later retests.
- Check which skill wins when multiple roots contain the same name.
- Separate `READ`, `LOCAL_WRITE`, `PROVIDER_CONFIG`, `EXTERNAL_CREATE`, `DEPLOY_RELEASE` and secret-management permissions. No skill text enforces platform permissions by itself.
- **Do not assume memory is available.** Graphify/Hindsight are optional *at install time*, and full framework setup readiness depends on consented, verified provider calls. When unavailable, report the gap without fabricating recall/retain.

See [source checks](../../scripts/validate_skill_packages.py), [quickstart](QUICKSTART.md), and [real-world acceptance protocol](../implementation/REAL-WORLD-E2E-VALIDATION.md).
