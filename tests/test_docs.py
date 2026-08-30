"""Documentation claims that are checkable, checked.

A stale command or a script path that no longer exists is the kind of error a
reader hits before anyone else does.
"""

from __future__ import annotations

import re
import subprocess
import sys

DOC_FILES = ["README.md", "CLAUDE.md", "pyproject.toml", "docs/HARMONIZATION.md",
             "docs/CURATION.md", "NEXT_TASKS.md"]

SCRIPT_REF = re.compile(r"scripts/[a-z_]+\.py")
JUST_REF = re.compile(r"just ([a-z][a-z-]*)")


def test_every_referenced_script_exists(repo_root):
    missing = set()
    for name in DOC_FILES:
        path = repo_root / name
        for ref in SCRIPT_REF.findall(path.read_text(encoding="utf-8")):
            if not (repo_root / ref).exists():
                missing.add(f"{name}: {ref}")
    assert missing == set(), sorted(missing)


def test_every_referenced_just_target_exists(repo_root):
    """`just --list` is the authority on what the justfile offers."""
    listed = subprocess.run(["just", "--summary"], cwd=repo_root,
                            capture_output=True, text=True)
    if listed.returncode != 0:
        import pytest
        pytest.skip("just is not installed")
    targets = set(listed.stdout.split())
    missing = set()
    for name in DOC_FILES:
        for ref in JUST_REF.findall((repo_root / name).read_text(encoding="utf-8")):
            if ref not in targets:
                missing.add(f"{name}: just {ref}")
    assert missing == set(), sorted(missing)


def test_the_readme_statistics_block_is_current(repo_root):
    result = subprocess.run([sys.executable, "scripts/check_docs.py", "--check"],
                            cwd=repo_root, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
