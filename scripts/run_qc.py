#!/usr/bin/env python3
"""Run the authoritative AntibioticMech quality gate locally and in CI.

One executable definition of "green", so a passing local run and a passing CI
run mean the same thing.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

COMMANDS = [
    (
        "lint",
        [sys.executable, "-m", "ruff", "check", "."],
        "Fail fast on syntax, import, and style defects before expensive corpus checks.",
    ),
    (
        "documentation",
        [sys.executable, "scripts/check_docs.py", "--check"],
        "README's generated statistics must match the corpus a reader would download.",
    ),
    (
        "raw-data provenance",
        [sys.executable, "scripts/check_provenance.py"],
        "Every committed inventory must retain its source metadata and integrity hash.",
    ),
    (
        "source queue",
        [sys.executable, "scripts/check_source_queue.py"],
        "An ADOPTED source must be one the pipeline reads under verified redistribution terms.",
    ),
    (
        "tests",
        [sys.executable, "-m", "pytest", "-q"],
        "Tests cover harmonization rules and corpus-wide invariants per-record validation cannot see.",
    ),
    (
        "schema validation",
        [sys.executable, "scripts/validate_strict.py", "--quiet"],
        "Closed-mode validation checks every record's shape, including unknown fields.",
    ),
    (
        "corpus reproduction",
        [sys.executable, "scripts/verify_corpus.py"],
        "A schema-valid hand edit is still invalid unless the corpus reproduces from data/raw/.",
    ),
    (
        "chemical map",
        [sys.executable, "scripts/generate_chemical_map.py", "--check"],
        "The committed structure-only map must cover the corpus and retain its quality contract.",
    ),
    (
        "generated site",
        [sys.executable, "scripts/render_pages.py", "--check"],
        "The committed, published site must not drift from the corpus that generated it.",
    ),
    (
        "corpus report",
        [sys.executable, "scripts/antibiotic_report.py"],
        "Exercise the cross-corpus analyses and finish with the live curation summary.",
    ),
]


def main() -> int:
    for name, command, rationale in COMMANDS:
        print(f"\n=== qc: {name} ===", flush=True)
        print(f"why: {rationale}", flush=True)
        completed = subprocess.run(command, cwd=REPO_ROOT, check=False)
        if completed.returncode:
            print(f"qc stopped: {name} failed with exit code {completed.returncode}",
                  file=sys.stderr)
            return completed.returncode
    print("\nAll AntibioticMech quality gates passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
