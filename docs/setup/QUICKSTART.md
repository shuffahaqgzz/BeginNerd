# BeginNerd — Quickstart

BeginNerd is **Agent Skills–based, not Codex-only**. Start with the [multi-harness guide](MULTI-HARNESS-ADOPTION.md) for Claude Code, Codex, Cursor, OpenCode, Hermes Agent, or other compatible harnesses.

## 1. Discover and choose your agent

```bash
npx skills@latest add shuffahaqgzz/BeginNerd --list
npx skills@latest add shuffahaqgzz/BeginNerd
```

Skills CLI requires a compatible Node.js version; inspect project/global installs and choose one install route per harness. See [supported agent IDs](https://github.com/vercel-labs/skills/blob/main/docs/agents.md) and [Hermes native alternative](MULTI-HARNESS-ADOPTION.md#hermes-agent--native-alternative).

## 2. Test the portable source

On a clean checkout of the revision you intend to use (Python 3.11+):

```bash
python3 scripts/validate_repository.py
python3 scripts/build_portable_references.py --check
python3 scripts/validate_skill_packages.py
python3 -m unittest discover -s tests/contracts -p 'test_*.py' -v
```

These tests verify package references and offline repository contracts only—not installed skills or runtime behavior.

## 3. Verify your own harness

- Inventory installed skill locations and duplicates, and honor local project/global settings before edits.
- Check fresh-session discovery and activation (including near-miss cases). In Hermes, project skill trust may be required after inspection.
- Validate tool write boundaries independently. A shell sandbox does not guarantee external provider plugins cannot mutate.
- Graphify/Hindsight are distinct provider setup tasks requiring authorization, not installed merely by adding BeginNerd.
- Capture what really happened: source SHA, harness version, expected/observed, attempted actions, actual files changed and sanitized evidence.

**Existing pilot:** Owner's initial evaluation environment was `srv-test01` with Codex CLI. That is not an architectural requirement and does not prove compatibility on other harnesses. BeginNerd's real-world A2 acceptance case remains deferred.

## 4. When building a real application

Product G1 → Solution G2 → Planning → Foundation → Implementation/QA → separately authorized Release/Operations. You can invoke a single relevant workflow rather than regenerating every phase.

More detail: [multi-harness installation](MULTI-HARNESS-ADOPTION.md), [status & open gaps](../implementation/STATUS.md), [real-world E2E protocol](../implementation/REAL-WORLD-E2E-VALIDATION.md).
