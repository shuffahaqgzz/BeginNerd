#!/usr/bin/env python3
"""Read-only, scoped manifest for comparing actual workspace files including untracked/ignored."""
import argparse
import hashlib
import json
import os
from pathlib import Path


def snapshot(root):
    root = Path(root).resolve()
    if not root.is_dir():
        raise ValueError(f"not a directory: {root}")
    inventory = {}
    for directory, folders, filenames in os.walk(root, topdown=True, followlinks=False):
        folders[:] = sorted(folder for folder in folders if folder != ".git")
        for name in sorted(filenames + [x for x in folders if (Path(directory) / x).is_symlink()]):
            path = Path(directory) / name
            rel = path.relative_to(root).as_posix()
            if path.is_symlink():
                inventory[rel] = {"kind": "symlink"}  # Do not follow or leak link target
            elif path.is_file():
                try:
                    digest = hashlib.sha256()
                    with path.open("rb") as fp:
                        for chunk in iter(lambda: fp.read(1024 * 1024), b""):
                            digest.update(chunk)
                    inventory[rel] = {"kind": "file", "sha256": digest.hexdigest(),
                                      "bytes": path.stat().st_size}
                except OSError as exc:
                    inventory[rel] = {"kind": "unreadable", "error_type": type(exc).__name__}
        folders[:] = [folder for folder in folders if not (Path(directory) / folder).is_symlink()]
    return inventory


def compare(before, after):
    added = sorted(after.keys() - before.keys())
    removed = sorted(before.keys() - after.keys())
    changed = sorted(p for p in before.keys() & after.keys() if before[p] != after[p])
    return {"added": added, "removed": removed, "changed": changed}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Workspace root to inspect read-only")
    parser.add_argument("--compare", type=Path, help="Pre-run JSON manifest saved outside observed workspace")
    args = parser.parse_args()
    try:
        current = snapshot(args.root)
        if args.compare:
            baseline = json.loads(args.compare.read_text(encoding="utf-8"))
            if not isinstance(baseline, dict) or "files" not in baseline:
                raise ValueError("invalid baseline manifest")
            result = compare(baseline["files"], current)
            print(json.dumps({"comparison": result, "counts": {k: len(v) for k,v in result.items()}},
                             indent=2, sort_keys=True))
            return 1 if any(result.values()) else 0
        print(json.dumps({"format": "BeginNerd-workspace-manifest-v1", "files": current},
                         indent=2, sort_keys=True))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.exit(2, f"WORKSPACE MANIFEST: UNVERIFIED — {type(exc).__name__}: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
