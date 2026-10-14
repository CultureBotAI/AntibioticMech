#!/usr/bin/env python3
"""Validate repository history records against the vendored claw schema.

One implementation, called by both `just validate-history` and `scripts/run_qc.py`,
so the gate does not depend on the task runner being installed — CI runs qc with
uv alone, and a `just` shell-out failed there with exit 127 (CellStructureMech#54,
where this script was ported from).

    python scripts/validate_history.py                 # everything under history/
    python scripts/validate_history.py history/records/x/y.yaml
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA = REPO_ROOT / "src" / "antibioticmech" / "schema" / "history.yaml"
TARGET_CLASS = "HistoryRecord"
# Both extensions, as claw's validator does: the scaffolder writes .yaml, but a
# record saved as .yml would otherwise be skipped, and validity is the half of
# this layer that is supposed to be hard.
SUFFIXES = {".yaml", ".yml"}


def records(target: Path) -> list[Path]:
    if target.is_dir():
        return sorted(p for p in target.rglob("*") if p.suffix in SUFFIXES and p.is_file())
    return [target]


def not_a_record(path: Path) -> str | None:
    """Why a file cannot hold a HistoryRecord at all, or None.

    linkml-validate checks each instance a file holds, so a file holding none —
    empty, or an empty list — prints "No issues found" and exits 0. Checked here
    first, as claw's validator does, or a blank record passes the gate.
    """
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        return f"{type(exc).__name__}: {exc}"
    if not isinstance(data, dict):
        return f"top level must be one record (a mapping); got {type(data).__name__}"
    return None


def main() -> int:
    if len(sys.argv) > 2:
        # Refused rather than validating only the first: a gate that silently
        # skips what it was given reports green for records it never read.
        print("validate-history: pass one record or one directory", file=sys.stderr)
        return 2
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO_ROOT / "history"
    if not target.exists():
        print(f"validate-history: {target} does not exist", file=sys.stderr)
        return 2
    paths = records(target)
    if not paths:
        print(f"No history records under {target}.")
        return 0

    problems = {path: problem for path in paths if (problem := not_a_record(path))}
    for path, problem in problems.items():
        print(f"{path}: {problem}", file=sys.stderr)
    if problems:
        return 1

    # Link check first: it explains a bad URL better than the schema's uri error.
    links = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "validate_history_links.py"), str(target)],
        cwd=REPO_ROOT, check=False,
    )
    if links.returncode:
        return links.returncode

    result = subprocess.run(
        ["linkml-validate", "--schema", str(SCHEMA), "--target-class", TARGET_CLASS,
         *[str(p) for p in paths]],
        cwd=REPO_ROOT, check=False,
    )
    if result.returncode:
        return result.returncode
    print(f"{len(paths)} history record(s) valid against {SCHEMA.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
