#!/usr/bin/env python3
"""Static repository contract validation. NOT a runtime behavioral test."""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMPANIONS = ("beginnerd-ask", "beginnerd-setup")
LIFECYCLE = ("beginnerd-solution", "beginnerd-plan",
             "beginnerd-foundation", "beginnerd-implement", "beginnerd-release")
COUNTS = {"PRODUCT-FOUNDATION": 4, "SOLUTION": 8, "PLANNING": 4,
          "FOUNDATION": 5, "IMPLEMENTATION": 5, "RELEASE": 3, "OPERATIONS": 3}
REQUIRED = (
    "README.md", "AGENTS.md", "docs/architecture/FRAMEWORK-ARCHITECTURE.md",
    "docs/decisions/DECISION-REGISTER.md",
    "docs/decisions/BN-DEC-009-APPROVED-DETAILS.md",
    "docs/architecture/ARTIFACT-AND-READINESS-CONTRACT.md",
    "docs/workflows/WORKFLOW-REGISTRY.md",
    "docs/governance/AGENT-GOVERNANCE.md",
    "docs/governance/MEMORY-KNOWLEDGE-CONTRACT.md",
    "docs/governance/RESEARCH-REUSE-POLICY.md",
    "docs/governance/WORK-STRUCTURE-POLICY.md",
    "docs/implementation/STATUS.md",
    "docs/implementation/PHASE-1-PRODUCT-IMPLEMENTATION-CONTRACT.md",
    "skills/beginnerd-product/SKILL.md",
    "skills/beginnerd-product/references/g1-readiness.md",
    "tests/behavioral/scenarios.json",
    "tests/activation/queries.json",
    "docs/engineering/SKILL-ENGINEERING-AND-DISTRIBUTION-STANDARD.md",
    "docs/implementation/DISTRIBUTION-READINESS.md",
    "scripts/build_portable_references.py",
    "scripts/validate_skill_packages.py",
)
ROW = re.compile(r"^\|\s*(PRODUCT-FOUNDATION|SOLUTION|PLANNING|FOUNDATION|IMPLEMENTATION|RELEASE|OPERATIONS)-(\d{2})\s*\|", re.M)

def validate():
    errors = []
    for path in REQUIRED:
        if not (ROOT / path).is_file():
            errors.append("missing required file: " + path)

    for name in COMPANIONS:
        skill = ROOT / "skills" / name / "SKILL.md"
        if not skill.is_file():
            errors.append("missing companion skill: " + name)
            continue
        contents = skill.read_text(encoding="utf-8")
        if not contents.startswith("---\n"):
            errors.append("missing YAML frontmatter: " + name)
            continue
        end = contents.find("\n---\n", 4)
        if end < 0:
            errors.append("unclosed YAML frontmatter: " + name)
            continue
        front = contents[4:end]
        if not re.search(r"^name:\s*" + re.escape(name) + r"\s*$", front, re.M):
            errors.append("skill name mismatch: " + name)
        if not re.search(r"^description:\s*\S", front, re.M):
            errors.append("missing description: " + name)

    for name in LIFECYCLE:
        folder = ROOT / "skills" / name
        if not (folder / "README.md").is_file():
            errors.append("missing lifecycle boundary: " + name)
        if not (folder / "SKILL.md").is_file():
            errors.append("missing lifecycle SKILL.md source candidate: " + name)

    reg = ROOT / "docs/workflows/WORKFLOW-REGISTRY.md"
    if reg.is_file():
        ids = [f"{phase}-{number}" for phase, number in ROW.findall(reg.read_text(encoding="utf-8"))]
        if len(ids) != 32 or len(set(ids)) != 32:
            errors.append(f"expected 32 unique workflow IDs, got {len(ids)} rows and {len(set(ids))} unique")
        phases = Counter(item.rsplit("-", 1)[0] for item in ids)
        if phases != Counter(COUNTS):
            errors.append(f"workflow counts differ: {dict(phases)}")

    scenarios = ROOT / "tests/behavioral/scenarios.json"
    if scenarios.is_file():
        try:
            items = json.loads(scenarios.read_text(encoding="utf-8"))
            if not isinstance(items, list) or len(items) < 16:
                errors.append("behavioral scenarios require >=16 defined cases")
            else:
                ids = [item.get("id") for item in items]
                if len(set(ids)) != len(ids):
                    errors.append("duplicate scenario IDs")
                categories = {item.get("category") for item in items}
                if not {"ask", "setup", "memory", "governance", "reuse"} <= categories:
                    errors.append("behavioral category coverage incomplete")
                for item in items:
                    if item.get("execution_status") != "NOT_EXECUTED":
                        errors.append("a scenario was preclaimed as executed: " + str(item.get("id")))
                    if not all(item.get(key) for key in ("id", "prompt", "expected_behaviors", "must_not")):
                        errors.append("incomplete behavioral case: " + str(item.get("id")))
        except (ValueError, TypeError) as ex:
            errors.append(f"invalid scenario JSON: {ex}")

    return errors

def main():
    errors = validate()
    if errors:
        print("BeginNerd STATIC CONTRACT CHECK: FAIL")
        for item in errors:
            print(" - " + item)
        return 1
    print("BeginNerd STATIC CONTRACT CHECK: PASS")
    print("Validated repository files, 8 source skill packages (6 lifecycle and 2 companion),")
    print("32 workflow IDs and behavioral scenario definitions.")
    print("NOT VERIFIED: agent runtime execution, Graphify/Hindsight integration, E2E.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
