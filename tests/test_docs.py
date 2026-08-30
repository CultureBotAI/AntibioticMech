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


# Every numeric claim in prose that can be re-derived, with the derivation that
# produces it. Keyed by the phrase as it appears, so the assertion message names
# the exact words to edit.
#
# This exists because the stale-figure defect recurred FIVE times (#68 and its
# predecessors): a commit updates one count and leaves its neighbour standing —
# "translate 33 of them" two lines above a corrected "416". Prose is where a
# reader forms their model of the corpus, and a wrong number there is a claim
# the repo makes and does not keep. Gating paths and just targets never caught
# these, because the rot is in the digits, not the identifiers.
#
# To add a claim: write the sentence with a {} where the number goes.
NUMERIC_CLAIMS = [
    ("docs/HARMONIZATION.md", "translate {} of them", "mapped_roles"),
    ("NEXT_TASKS.md", "beyond the {} records ChEBI's roles reach", "moa_records"),
    ("NEXT_TASKS.md", "{} curated roles now map", "mapped_roles"),
    ("NEXT_TASKS.md", "the {}-role map", "mapped_roles"),
]


def _derived(repo_root):
    import yaml

    conf = yaml.safe_load((repo_root / "conf" / "sources.yaml").read_text(encoding="utf-8"))
    base = conf.get("role_to_mode_of_action") or {}
    euk = conf.get("role_to_mode_of_action_eukaryotic") or {}

    moa_records = 0
    for path in (repo_root / "data" / "antibiotics").rglob("*.yaml"):
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(record, dict) and record.get("mode_of_action"):
            moa_records += 1

    return {"mapped_roles": len(set(base) | set(euk)), "moa_records": moa_records}


def test_numeric_claims_in_prose_match_the_corpus(repo_root):
    """Re-derives each figure from conf/ and the records themselves.

    A number in prose is an assertion about the data. Deriving it here means the
    docs cannot drift from the corpus silently: the commit that changes the map
    or the seeding either updates the sentence or fails the gate.
    """
    derived = _derived(repo_root)
    wrong, absent = [], []
    for name, template, key in NUMERIC_CLAIMS:
        text = (repo_root / name).read_text(encoding="utf-8")
        expected = template.format(derived[key])
        if expected in text:
            continue
        pattern = re.escape(template).replace(r"\{\}", r"(\d+)")
        found = re.findall(pattern, text)
        if found:
            wrong.append(f"{name}: {template.format(found[0])!r} -> should be {expected!r}")
        else:
            # The sentence was reworded. That is fine, but the entry here is now
            # dead and must be updated or dropped, or it guards nothing.
            absent.append(f"{name}: no longer contains {template!r}")
    assert wrong == [], wrong
    assert absent == [], absent
