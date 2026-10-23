#!/usr/bin/env python3
"""Validate BeginNerd's currently distributable companions, without side effects.

This intentionally checks a simple flat YAML frontmatter subset used by BeginNerd,
and portable file references. It is NOT a full YAML parser or agent runtime test.
Run upstream agentskills skills-ref separately when available and provenance verified.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACTIVE = ("beginnerd-ask", "beginnerd-setup", "beginnerd-product")
LIFECYCLE = (
    "beginnerd-solution", "beginnerd-plan",
    "beginnerd-foundation", "beginnerd-implement", "beginnerd-release",
)
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
PATH = re.compile(r"(?<![\w/])(?:references|scripts|assets)/[A-Za-z0-9_./-]+")
MARKDOWN_LINK = re.compile(r"\]\(([^)#]+)(?:#[^)]*)?\)")
HEADINGS = ("name", "description", "license", "compatibility", "allowed-tools")


def parse_frontmatter(text: str, root_label: str) -> tuple[dict, list[str]]:
    errors = []
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        return {}, [f"{root_label}: absent or unterminated YAML frontmatter"]
    front = text[4:text.index("\n---\n", 4)]
    metadata = {}
    for line in front.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")):
            errors.append(f"{root_label}: nested frontmatter not supported by internal subset validator")
            continue
        if ":" not in line:
            errors.append(f"{root_label}: invalid frontmatter line")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        if key not in HEADINGS:
            errors.append(f"{root_label}: frontmatter key needs upstream validation: {key}")
        if key in metadata:
            errors.append(f"{root_label}: duplicate frontmatter key: {key}")
        metadata[key] = value.strip().strip("'\"")
    return metadata, errors


def check_references(skill: Path) -> list[str]:
    errors = []
    for md in [skill / "SKILL.md", *sorted((skill / "references").rglob("*.md"))]:
        if not md.is_file():
            continue
        body = md.read_text(encoding="utf-8")
        for candidate in PATH.findall(body):
            candidate = candidate.rstrip(".,:;)]}'\"")
            target = (skill / candidate).resolve()
            if not target.is_relative_to(skill.resolve()):
                errors.append(f"{skill.name}: path escapes skill root: {candidate}")
            elif not target.is_file():
                errors.append(f"{skill.name}: missing packaged resource {candidate}")
        for raw in MARKDOWN_LINK.findall(body):
            if raw.startswith(("http:", "https:", "mailto:", "/", "#")):
                continue
            target = (md.parent / raw).resolve()
            if not target.is_relative_to(skill.resolve()):
                errors.append(f"{skill.name}: external package dependency {raw}")
            elif not target.is_file():
                errors.append(f"{skill.name}: broken relative link {raw}")
    return errors


def validate_skill(skill: Path) -> list[str]:
    errors = []
    md = skill / "SKILL.md"
    if not md.is_file():
        return [f"{skill.name}: missing SKILL.md"]
    body = md.read_text(encoding="utf-8")
    meta, errs = parse_frontmatter(body, skill.name)
    errors.extend(errs)
    name = meta.get("name", "")
    description = meta.get("description", "")
    if not (1 <= len(name) <= 64 and NAME.fullmatch(name) and name == skill.name):
        errors.append(f"{skill.name}: invalid/mismatched name")
    if not 1 <= len(description) <= 1024:
        errors.append(f"{skill.name}: description must be 1–1024 characters")
    if meta.get("compatibility") and len(meta["compatibility"]) > 500:
        errors.append(f"{skill.name}: compatibility exceeds 500 characters")
    if len(body.splitlines()) > 500:
        errors.append(f"{skill.name}: SKILL.md exceeds recommended 500-line authoring budget")
    errors.extend(check_references(skill))
    return errors


def validate(root: Path = ROOT, *, require_lifecycle_boundaries: bool = True) -> list[str]:
    errors = []
    # Lifecycle README-only directories are not installable skills.
    expected = set(ACTIVE)
    actual = {p.parent.name for p in (root / "skills").glob("*/SKILL.md")}
    if actual != expected:
        errors.append(f"distributable set differs: expected {sorted(expected)}, actual {sorted(actual)}")
    for name in ACTIVE:
        errors.extend(validate_skill(root / "skills" / name))
    if require_lifecycle_boundaries:
        for name in LIFECYCLE:
            folder = root / "skills" / name
            if not (folder / "README.md").is_file() or (folder / "SKILL.md").exists():
                errors.append(f"lifecycle boundary mismatch: {name}")
    evals = root / "tests" / "activation" / "queries.json"
    if evals.is_file():
        try:
            data = json.loads(evals.read_text(encoding="utf-8"))
            if len(data) < 12:
                errors.append("insufficient activation cases (at least 12)")
            ids = [x["id"] for x in data]
            if len(ids) != len(set(ids)):
                errors.append("duplicate activation case IDs")
            for skill in ACTIVE:
                subset = [x for x in data if x.get("skill") == skill]
                if not subset or not any(x.get("should_trigger") is True for x in subset) or not any(x.get("should_trigger") is False for x in subset):
                    errors.append(f"missing positive/negative activation cases: {skill}")
            for entry in data:
                if not isinstance(entry.get("should_trigger"), bool) or not entry.get("query"):
                    errors.append(f"invalid activation case: {entry.get('id')}")
                if entry.get("execution_status") != "NOT_EXECUTED":
                    errors.append(f"activation case preclaimed executed: {entry.get('id')}")
        except (ValueError, KeyError, TypeError) as exc:
            errors.append(f"invalid activation JSON: {exc}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("SKILL PACKAGE STATIC CHECK: FAIL")
        for error in errors:
            print(" - " + error)
        return 1
    print("SKILL PACKAGE STATIC CHECK: PASS")
    print("Validated 2 companion + 1 product skill metadata and packaged refs; 5 lifecycle skills pending.")
    print("NOT VERIFIED: full upstream YAML spec, Skills CLI install, runtime triggering, providers.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
