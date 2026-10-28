# BeginNerd

**Start with a vibe. Build with a plan. Learn along the way.**

*Guided Building for people who want to create software with an AI coding agent—and understand what they're building.*

**Your agent. Your project. Your decisions.** BeginNerd uses the open [Agent Skills](https://agentskills.io) format. Bring it to **Claude Code, Codex, Cursor, OpenCode, Hermes Agent**, or any harness that can load compatible skill folders.

[Get started](#get-started) · [Meet the skills](#meet-the-skills) · [Why BeginNerd](#why-beginnerd) · [Compatibility](docs/setup/MULTI-HARNESS-ADOPTION.md)

[![Source checks](https://github.com/shuffahaqgzz/BeginNerd/actions/workflows/validate.yml/badge.svg)](https://github.com/shuffahaqgzz/BeginNerd/actions/workflows/validate.yml) [![MIT License](https://img.shields.io/badge/license-MIT-24292f)](LICENSE)

## The idea is easy. Knowing what to build is harder.

You ask an AI agent to *"build me an app."* Code starts appearing. Then come the real questions:

Who needs this? What problem are we solving? Which features actually matter? Why use that technology? And how do we know the result works?

**BeginNerd helps with the part between a good idea and a product you can stand behind.**

It isn't autopilot for your decisions. It isn't a programming course you have to finish first. It's a set of skills that help your agent **discover, explain, recommend, plan, build, test, and learn** alongside you.

## Get started

Use the [Skills CLI](https://github.com/vercel-labs/skills) with a supported coding agent. Current CLI documentation specifies Node.js 22.20+.

**1. See what's available—without installing**

```bash
npx skills@latest add shuffahaqgzz/BeginNerd --list
```

**2. Install into the project you actually use**

```bash
npx skills@latest add shuffahaqgzz/BeginNerd
```

Choose your agent and the skills you want. Project-scoped installation is the default. Already installed BeginNerd? Check the existing skill copies before updating or overwriting anything.

Want to specify a harness directly? Pick **one** option:

| Agent | Install option |
|---|---|
| Claude Code | `-a claude-code` |
| Codex | `-a codex` |
| Cursor | `-a cursor` |
| OpenCode | `-a opencode` |
| Hermes Agent | `-a hermes-agent` |

For example:

```bash
npx skills@latest add shuffahaqgzz/BeginNerd -a opencode
```

Hermes has its own Skills Hub too. See the [native Hermes setup](docs/setup/MULTI-HARNESS-ADOPTION.md#hermes-agent--native-alternative) if you'd rather use its GitHub taps. Use **one installation route** per agent to avoid duplicate skills.

**3. Start a conversation**

> "I have an app idea, but I'm not sure what matters most. Use BeginNerd to help me understand the real problem first."

Already have a project?

> "Use beginnerd-ask to review the existing project and recommend the next useful step. Don't make me start from scratch."

On first use, BeginNerd gives you something useful first, then adjusts how much it explains based on what you already know (it may ask up to three simple questions if it can't tell). **Graphify and Hindsight are optional**, enabled only if you choose them and authorize setup. You can use the six development phases without either provider.

## Meet the skills

**Two companions**, available whenever you need them:

- [`beginnerd-ask`](skills/beginnerd-ask/SKILL.md) — Figure out where you are and what comes next.
- [`beginnerd-setup`](skills/beginnerd-setup/SKILL.md) — Choose how you want to be guided and whether to set up optional knowledge or memory.

**Six lifecycle skills** to make progress from an idea to a maintained product:

| Skill | What it helps you answer |
|---|---|
| [`beginnerd-product`](skills/beginnerd-product/SKILL.md) | Who is this for? How do we know the problem is real? What is worth testing first? |
| [`beginnerd-solution`](skills/beginnerd-solution/SKILL.md) | How should the experience, architecture, data, and security work? |
| [`beginnerd-plan`](skills/beginnerd-plan/SKILL.md) | What should we work on next, and how will we know it's done? |
| [`beginnerd-foundation`](skills/beginnerd-foundation/SKILL.md) | Is the repository, environment, and agent setup actually ready? |
| [`beginnerd-implement`](skills/beginnerd-implement/SKILL.md) | How do we build and test the work we've agreed on? |
| [`beginnerd-release`](skills/beginnerd-release/SKILL.md) | How do we release safely, learn from real use, and maintain the product? |

You **don't** need to run all six phases for every small change. Use the part that fits your current problem. BeginNerd keeps formal project records in the background; it shouldn't make beginners memorize workflow IDs.

## Why BeginNerd?

**Understand before building.** Spend just enough time confirming the problem, rather than shipping features nobody needed.

**Recommend, don't overwhelm.** Get a clear recommendation and useful trade-offs—not a wall of acronyms or endless approval prompts.

**Research and reuse first.** A good existing solution beats reinventing one just because the agent can generate it.

**Build while learning.** Learn through decisions and work that matter right now.

**Iterate, don't restart.** Small technical discoveries are part of coding. Formal replanning is for genuine changes in scope, architecture or acceptance.

**Verify, don't just generate.** A passing static check doesn't prove a user's problem is solved—or that a deployment is safe.

We call that **Guided Building**.

## Where it stands

BeginNerd is currently a **public source preview**. The eight skill packages and 32 workflow responsibilities are available in the repository, and static validation is in place. Real-world effectiveness, cross-harness behavior, optional provider integrations and enforceable tool permissions **still require independent runtime evidence**.

Read the [implementation status](docs/implementation/STATUS.md), [multi-harness guide](docs/setup/MULTI-HARNESS-ADOPTION.md), or [real-world test plan](docs/implementation/REAL-WORLD-E2E-VALIDATION.md) for the exact boundaries.

## Go deeper

[How the framework works](docs/architecture/FRAMEWORK-ARCHITECTURE.md) · [Workflow responsibilities](docs/workflows/WORKFLOW-REGISTRY.md) · [Security and permissions](docs/governance/AGENT-GOVERNANCE.md) · [Contributing](CONTRIBUTING.md)

BeginNerd is open source under the [MIT License](LICENSE). For security concerns, see [SECURITY.md](SECURITY.md).
