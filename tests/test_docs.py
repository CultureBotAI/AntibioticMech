"""Documentation claims that are checkable, checked.

A stale command or a script path that no longer exists is the kind of error a
reader hits before anyone else does.
"""

from __future__ import annotations

import re
import subprocess
import sys

DOC_FILES = ["README.md", "CLAUDE.md", "pyproject.toml", "docs/HARMONIZATION.md",
             "docs/CURATION.md", "NEXT_TASKS.md",
             # Skills are instructions an agent will follow literally, so a
             # command that does not exist is worse here than in prose.
             ".claude/skills/source-queue/SKILL.md",
             ".claude/skills/review-open-issues/SKILL.md"]

SCRIPT_REF = re.compile(r"scripts/[a-z_]+\.py")
JUST_REF = re.compile(r"just ([a-z][a-z-]*)")


def test_every_skill_declares_the_frontmatter_the_loader_needs(repo_root):
    """A skill with a missing name or description is invisible to the model that
    would have used it."""
    import yaml

    for path in sorted((repo_root / ".claude" / "skills").glob("*/SKILL.md")):
        text = path.read_text(encoding="utf-8")
        assert text.startswith("---\n"), path
        front = yaml.safe_load(text.split("---")[1])
        assert front.get("name") == path.parent.name, path
        assert front.get("description", "").strip(), path


def test_every_referenced_script_exists(repo_root):
    missing = set()
    for name in DOC_FILES:
        path = repo_root / name
        for ref in SCRIPT_REF.findall(path.read_text(encoding="utf-8")):
            if not (repo_root / ref).exists():
                missing.add(f"{name}: {ref}")
    assert missing == set(), sorted(missing)


# A recipe header: a name, optional parameters, then a colon at end of line.
# `:=` (a variable assignment) and `set …` are excluded, or `just corpus` would
# look like a valid target because `corpus := "data/antibiotics"` exists.
RECIPE = re.compile(r"^([a-z][a-z0-9-]*)(?:\s+[^:=\n]*)?:(?!=)\s*$", re.MULTILINE)


def test_every_referenced_just_target_exists(repo_root):
    """Parsed from the justfile rather than from `just --summary`: CI runners do
    not have `just` installed, and a test that needs a tool the gate does not
    install is a test that fails for the wrong reason."""
    justfile = (repo_root / "justfile").read_text(encoding="utf-8")
    targets = set(RECIPE.findall(justfile))
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


def test_the_source_queue_is_consistent_with_the_repository(repo_root):
    """The queue ranks sources we might adopt. Left unchecked it drifts into
    wishful thinking — a source marked ADOPTED that nothing reads, or a licence
    left unverified under data the corpus redistributes."""
    result = subprocess.run([sys.executable, "scripts/check_source_queue.py"],
                            cwd=repo_root, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_no_document_quotes_a_stale_record_count(repo_root):
    """Figures drift here faster than prose does — the corpus went 2,603 to
    2,469 to 2,923 inside one working session as a trust filter tightened and a
    scope decision widened. A document asserting a record count that is no longer
    true is the most common way this repository misleads a reader."""
    import glob
    import re

    actual = len(glob.glob(str(repo_root / "data" / "antibiotics" / "*" / "*.yaml")))
    if not actual:
        import pytest
        pytest.skip("no corpus")

    pattern = re.compile(r"([\d,]{3,})\s+(?:of\s+the\s+)?records\b")
    stale = []
    for name in DOC_FILES + ["ATTRIBUTION.md"]:
        path = repo_root / name
        if not path.exists():
            continue
        for match in pattern.finditer(path.read_text(encoding="utf-8")):
            value = int(match.group(1).replace(",", ""))
            # A count is either the corpus total or a documented subset; only a
            # claim about the whole corpus can be checked mechanically.
            if 2000 < value < 10000 and value != actual:
                stale.append(f"{name}: {match.group(0)!r} but the corpus holds {actual}")
    assert stale == [], stale
