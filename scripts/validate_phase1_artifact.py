#!/usr/bin/env python3
"""Static Lean PRODUCT.md integrity checks. No runtime, approval or G1 certification."""
import argparse
import re
from pathlib import Path

ID = {
    "req": re.compile(r"^\|\s*(REQUIREMENTS-\d{3})\s*\|", re.M),
    "ac": re.compile(r"^\|\s*(ACCEPTANCE-CRITERIA-\d{3})\s*\|", re.M),
    "tech": re.compile(r"^\|\s*(TECHNICAL-REQUIREMENTS-\d{3})\s*\|", re.M),
}
REF = {
    "req": re.compile(r"(?<![A-Z0-9-])REQUIREMENTS-\d{3}\b"),
    "ac": re.compile(r"(?<![A-Z0-9-])ACCEPTANCE-CRITERIA-\d{3}\b"),
    "tech": re.compile(r"(?<![A-Z0-9-])TECHNICAL-REQUIREMENTS-\d{3}\b"),
}
PROPOSAL = re.compile(r"\bPROPOSAL-\d{3}\b")
G1 = re.compile(r"\bG1\s*:\s*(PASS|PARTIAL|BLOCKED|UNVERIFIED)\b", re.I)


def unique_definitions(text, kind, issues):
    ids = ID[kind].findall(text)
    duplicates = sorted({v for v in ids if ids.count(v) > 1})
    if duplicates:
        issues.append(f"duplicate {kind} definitions: {', '.join(duplicates)}")
    if not ids:
        issues.append(f"no {kind} table definitions found")
    return set(ids)


def validate(text):
    """Return (issues, counts). Checks only structural integrity, not evidence validity."""
    issues = []
    req = unique_definitions(text, "req", issues)
    ac = unique_definitions(text, "ac", issues)
    tech = unique_definitions(text, "tech", issues)
    req_rows = {r.split("|")[1].strip(): r for r in text.splitlines()
                if ID["req"].match(r)}
    ac_rows = {r.split("|")[1].strip(): r for r in text.splitlines()
               if ID["ac"].match(r)}
    tech_rows = {r.split("|")[1].strip(): r for r in text.splitlines()
                 if ID["tech"].match(r)}

    for rid, row in req_rows.items():
        links = set(REF["ac"].findall(row))
        if not links:
            issues.append(f"{rid}: missing acceptance link")
        for aid in sorted(links - ac):
            issues.append(f"{rid}: unknown acceptance {aid}")

    linked_ac = set()
    for row in req_rows.values():
        linked_ac.update(REF["ac"].findall(row))
    for aid in sorted(ac - linked_ac):
        row = ac_rows[aid]
        if not (set(REF["req"].findall(row)) & req):
            issues.append(f"{aid}: not linked from/to any requirement")

    for tid, row in tech_rows.items():
        links = set(REF["req"].findall(row))
        if not links:
            issues.append(f"{tid}: missing product requirement link")
        for rid in sorted(links - req):
            issues.append(f"{tid}: unknown product requirement {rid}")
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if len(cells) < 4 or not cells[3] or cells[3].upper() in ("TBD", "N/A"):
            issues.append(f"{tid}: missing useful verification plan")

    # Missing proposal decision state is an integrity gap; not all proposals need a row.
    if PROPOSAL.search(text) and not re.search(r"PROPOSED|belum disetujui", text, re.I):
        issues.append("proposals found but no explicit proposed/unapproved status")

    status = G1.findall(text)
    if len(status) != 1:
        issues.append("expected exactly one explicit G1: PASS/PARTIAL/BLOCKED/UNVERIFIED declaration")
    if re.search(r"\bAPPROVED\b", text, re.I) and not re.search(
        r"bukti persetujuan|approved by|approval reference|approval evidence|persetujuan pengguna|disetujui pengguna", text, re.I
    ):
        issues.append("APPROVED label missing approval provenance narrative")

    return issues, {"requirements": len(req), "acceptance": len(ac),
                    "technical": len(tech), "g1": status[0].upper() if len(status) == 1 else "UNVERIFIED"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Lean PRODUCT.md to inspect (read-only)")
    args = parser.parse_args()
    try:
        issues, counts = validate(args.path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as exc:
        parser.exit(2, f"STATIC ARTIFACT CHECK: UNVERIFIED — {exc}\n")
    print("STATIC ARTIFACT CHECK:", "FAIL" if issues else "PASS", counts)
    for issue in issues:
        print(" - " + issue)
    print("NOT VERIFIED: actual approval, failure-case completeness, product G1, runtime tests or unrelated-file preservation")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
