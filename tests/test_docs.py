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
             ".claude/skills/review-open-issues/SKILL.md",
             ".claude/skills/curate-yaml-record/SKILL.md"]

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
    ("docs/HARMONIZATION.md", "`MICROBIAL_TARGET` ({} records)", "microbial_target"),
    ("docs/HARMONIZATION.md", "`HOST_SHARED_TARGET` ({})", "host_shared_target"),
    # The file a curator reads to choose the next data source. Registered here,
    # not left to the tripwire below: only this table checks that a figure is
    # right FOR ITS CLAIM rather than merely equal to some quantity somewhere.
    ("curation/source_queue.tsv", "maps {} of them", "mapped_roles"),
    ("curation/source_queue.tsv", "giving {} records a mode of action", "moa_records"),
]


def _derived(repo_root):
    import yaml

    conf = yaml.safe_load((repo_root / "conf" / "sources.yaml").read_text(encoding="utf-8"))
    base = conf.get("role_to_mode_of_action") or {}
    euk = conf.get("role_to_mode_of_action_eukaryotic") or {}

    moa_records = 0
    scopes = {"MICROBIAL_TARGET": 0, "HOST_SHARED_TARGET": 0}
    for path in (repo_root / "data" / "antibiotics").rglob("*.yaml"):
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(record, dict) and record.get("mode_of_action"):
            moa_records += 1
            scope = record.get("mode_of_action_target_scope")
            if scope in scopes:
                scopes[scope] += 1

    return {"mapped_roles": len(set(base) | set(euk)), "moa_records": moa_records,
            "microbial_target": scopes["MICROBIAL_TARGET"],
            "host_shared_target": scopes["HOST_SHARED_TARGET"]}


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


def test_the_declared_class_hierarchy_governs_every_count(repo_root):
    """A hierarchy only the site honours is not a hierarchy.

    `AntimicrobialClassEnum` declares `ANTIMYCOBACTERIAL is_a ANTIBACTERIAL` —
    mycobacteria are bacteria — while filing is exclusive, so those records are
    NOT also under ANTIBACTERIAL. Every count that answers "which compounds act
    on bacteria?" therefore has to add the subclass back. Before this, the
    report and the README both said 1037 for a true 1115, and only the site's
    cross-links knew better.

    Asserts the roll-up itself, and that the two generated surfaces show it.
    """
    import subprocess
    import sys

    sys.path.insert(0, str(repo_root / "scripts"))
    sys.path.insert(0, str(repo_root / "src"))
    from seed_from_sources import class_parents, rollup_by_class

    parents = class_parents()
    assert parents, "the schema declares no class hierarchy; this test guards nothing"

    import yaml
    counts: dict[str, int] = {}
    for path in (repo_root / "data" / "antibiotics").rglob("*.yaml"):
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        cls = record.get("antimicrobial_class")
        if cls:
            counts[cls] = counts.get(cls, 0) + 1

    inclusive = rollup_by_class(counts)
    for child, parent in parents.items():
        if not counts.get(child):
            continue
        assert inclusive[parent] == counts[parent] + counts[child], (child, parent)

        # `just report` must print the inclusive figure, not the filed one.
        out = subprocess.run([sys.executable, str(repo_root / "scripts" / "antibiotic_report.py")],
                             capture_output=True, text=True, cwd=repo_root).stdout
        assert f"{parent:26s} {inclusive[parent]:>6d}   (incl. subclasses)" in out, out[:600]

        # The README table must carry it too, with the subclass marked as included.
        readme = (repo_root / "README.md").read_text(encoding="utf-8")
        assert f"| {parent} *(incl. subclasses)* | {inclusive[parent]} |" in readme
        assert f"↳ {child}" in readme and f"subclass of {parent}" in readme
        # every column rolls up, not only Records
        assert f"| {inclusive[parent]} | {inclusive[parent]} |" in readme, (
            "the SEEDED column did not roll up with Records")
        assert "already counted in X's own row" in readme


def test_seed_and_tsv_class_rows_label_hierarchy_and_count_scope(repo_root, tmp_path):
    import csv
    import sys

    sys.path.insert(0, str(repo_root / "scripts"))
    from antibiotic_report import load_corpus, summarize, write_class_tsv
    from seed_from_sources import class_count_rows, format_class_count_rows

    counts = {
        "ANTIBACTERIAL": 2,
        "ANTIMYCOBACTERIAL": 1,
        "ANTIFUNGAL": 3,
    }
    rows = class_count_rows(counts)
    antibacterial = next(
        row for row in rows if row["antimicrobial_class"] == "ANTIBACTERIAL"
    )
    narrower = next(
        row for row in rows if row["antimicrobial_class"] == "ANTIMYCOBACTERIAL"
    )
    assert antibacterial["records_direct"] == 2
    assert antibacterial["records_including_subclasses"] == 3
    assert narrower["parent_class"] == "ANTIBACTERIAL"
    assert rows.index(narrower) == rows.index(antibacterial) + 1
    rendered = "\n".join(format_class_count_rows(counts))
    assert "inclusive=     3 direct=     2" in rendered
    assert "subclass of ANTIBACTERIAL; included in parent total" in rendered

    destination = tmp_path / "classes.tsv"
    stats = summarize(load_corpus())
    write_class_tsv(stats, destination)
    with destination.open(encoding="utf-8", newline="") as stream:
        tsv_rows = {
            row["antimicrobial_class"]: row
            for row in csv.DictReader(stream, delimiter="\t")
        }
    parent = tsv_rows["ANTIBACTERIAL"]
    child = tsv_rows["ANTIMYCOBACTERIAL"]
    assert parent["parent_class"] == ""
    assert child["parent_class"] == "ANTIBACTERIAL"
    assert int(parent["records_direct"]) + int(child["records_direct"]) == int(
        parent["records_including_subclasses"]
    )
    assert int(parent["seeded_direct"]) + int(child["seeded_direct"]) == int(
        parent["seeded_including_subclasses"]
    )


def test_every_derived_figure_follows_the_count_it_sits_beside(repo_root):
    """Compares each figure against a value derived INDEPENDENTLY from the
    corpus, not against a relation the bug already satisfies.

    The first version asserted only `grounded <= records`. The defect it was
    written for was 798 grounded beside 1115 records — and 798 <= 1115, so it
    passed with the bug reintroduced. A guard has to know the right answer, not
    merely a property the wrong answer also has.
    """
    import re
    import sys

    import yaml

    sys.path.insert(0, str(repo_root / "scripts"))
    sys.path.insert(0, str(repo_root / "src"))
    from seed_from_sources import CLASS_DIRS, rollup_by_class

    counts: dict[str, int] = {}
    grounded: dict[str, int] = {}
    for path in (repo_root / "data" / "antibiotics").rglob("*.yaml"):
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        cls = record.get("antimicrobial_class")
        if not cls:
            continue
        counts[cls] = counts.get(cls, 0) + 1
        if record.get("grounding_status") == "EXACT":
            grounded[cls] = grounded.get(cls, 0) + 1

    total = sum(counts.values())
    inclusive = rollup_by_class(counts)
    grounded_incl = rollup_by_class({c: grounded.get(c, 0) for c in counts})
    dir_of = {d: e for e, d in CLASS_DIRS.items()}

    def rows(page):
        html = (repo_root / "pages" / f"{page}.html").read_text(encoding="utf-8")
        for row in re.findall(r"<tr[^>]*>.*?</tr>", html, re.S):
            slug = re.search(r"class/([a-z-]+)\.html", row)
            if not slug:
                continue
            yield slug.group(1), [int(n) for n in
                                  re.findall(r'class="num">(\d+)</td>', row)], row

    seen = 0
    for slug, nums, row in rows("index"):
        expected = inclusive[dir_of[slug]]
        assert nums[0] == expected, f"index {slug}: shows {nums[0]}, corpus says {expected}"
        bar = re.search(r"width:(\d+)%", row)
        assert bar and int(bar.group(1)) == round(100 * expected / total), (slug, row[:120])
        seen += 1
    assert seen >= 2, "index listed no classes; this test guards nothing"

    for slug, nums, _row in rows("browse"):
        enum = dir_of[slug]
        assert nums[0] == inclusive[enum], f"browse {slug} records"
        assert nums[1] == grounded_incl[enum], (
            f"browse {slug} grounded: shows {nums[1]}, corpus says {grounded_incl[enum]}")


def test_a_subclass_row_is_placed_and_labelled_under_its_own_parent(repo_root):
    """Sorted by directory name, the indented row landed after "antifungal", so
    the note saying it is "already counted in the row above it" pointed at the
    wrong row — the page asserted antimycobacterials were antifungals.

    Also asserts the relationship is in the row TEXT. An indent plus an
    aria-hidden glyph conveys nothing to a screen reader, and is wrong the
    moment the order changes again.
    """
    import re
    import sys

    sys.path.insert(0, str(repo_root / "scripts"))
    sys.path.insert(0, str(repo_root / "src"))
    from seed_from_sources import CLASS_DIRS, class_parents

    parents = {CLASS_DIRS[c]: CLASS_DIRS[p] for c, p in class_parents().items()
               if c in CLASS_DIRS and p in CLASS_DIRS}
    assert parents, "no hierarchy declared; this test guards nothing"

    for page in ("index", "browse"):
        html = (repo_root / "pages" / page).with_suffix(".html").read_text(encoding="utf-8")
        order, texts = [], {}
        for row in re.findall(r"<tr[^>]*>.*?</tr>", html, re.S):
            slug = re.search(r"class/([a-z-]+)\.html", row)
            if slug:
                order.append(slug.group(1))
                texts[slug.group(1)] = row
        for child, parent in parents.items():
            if child not in order or parent not in order:
                continue
            assert order.index(child) == order.index(parent) + 1, (
                f"{page}: {child} is not immediately after {parent} — the "
                f'"counted in the row above" note points at {order[order.index(child) - 1]}')
            assert f"subclass of {parent}" in texts[child].lower(), (
                f"{page}: {child}'s row does not say it is a subclass in its text")


# Files scanned for numeric claims about the corpus. Not only .md: the stale
# "33 roles / 433 records" that prompted this lived in a TSV, and the registry
# above is six ENTRIES across two distinct files — so the hole was wider than
# "six markdown files" suggested, and included the file a curator reads to
# choose the next data source.
CLAIM_FILES = ["README.md", "NEXT_TASKS.md", "CLAUDE.md", "docs/HARMONIZATION.md",
               "docs/CURATION.md", "ATTRIBUTION.md", "curation/source_queue.tsv"]

# A number followed by a corpus noun. Deliberately narrow: this is a tripwire for
# claims about how much the corpus holds, not a general numeral checker.
CLAIM_SHAPE = (
    r"(?<![\d,.])(\d[\d,]{1,6})\s+"
    # "32 of them", "265 of the 286 records" — the original stale figure had no
    # noun after the number at all, so requiring one let half the defect this
    # test was written for re-land undetected.
    r"(?:of\s+(?:them\b|the\s+\d[\d,]*\s+)|"
    r"(?:records?|roles?|compounds?|structures?|concepts?)\b)"
)

# Claims that are NOT statements about the corpus as it stands, each with the
# reason it is exempt. A bare allowlist of numbers would go stale silently; these
# are matched as whole phrases so a changed sentence stops being exempt.
CLAIM_EXEMPTIONS = {
    # Narrative about something that HAPPENED, not a current quantity.
    "115 record pages disappeared": "history: a past incident, not a live count",
    "57 records moved class on a single run": "history: one pipeline run's delta",
}


def test_no_unregistered_numeric_claim_about_the_corpus(repo_root):
    """A tripwire for figures nobody registered.

    `NUMERIC_CLAIMS` only catches a claim someone remembered to add to it, which
    is exactly how `curation/source_queue.tsv` came to say the map covers "33
    roles" giving "433 records a mode of action" while the corpus held 32 and
    417 — in the file a curator reads to choose the next data source, unguarded
    because the registry lists markdown by name.

    This asserts the complement: every number-plus-corpus-noun in the scanned
    files must equal something the corpus can actually produce, or be exempt
    with a stated reason.

    WHAT IT CANNOT DO, stated because the first version of this docstring
    oversold it. Membership is tested against the UNION of the derived
    quantities, so a wrong figure that happens to equal an unrelated one passes:
    "giving 2,923 records a mode of action" is wrong and would survive, because
    2,923 is the record total. This is a TRIPWIRE for figures that match nothing,
    not a verifier. Checking a figure against the quantity its sentence actually
    asserts needs NUMERIC_CLAIMS above, which is why the two source_queue claims
    are registered there rather than left to this.
    """
    import re
    import sys

    import yaml

    sys.path.insert(0, str(repo_root / "scripts"))
    sys.path.insert(0, str(repo_root / "src"))

    records = [yaml.safe_load(p.read_text(encoding="utf-8"))
               for p in (repo_root / "data" / "antibiotics").rglob("*.yaml")]
    conf = yaml.safe_load((repo_root / "conf" / "sources.yaml").read_text(encoding="utf-8"))

    from collections import Counter
    classes = Counter(r["antimicrobial_class"] for r in records)
    scopes = Counter(r.get("mode_of_action_target_scope")
                     for r in records if r.get("mode_of_action"))

    derivable = {len(records), len(classes)}
    derivable |= set(classes.values()) | set(scopes.values())
    derivable.add(sum(1 for r in records if r.get("mode_of_action")))
    derivable.add(len(set(conf.get("role_to_mode_of_action") or {})
                      | set(conf.get("role_to_mode_of_action_eukaryotic") or {})))
    for field in ("molecular_targets", "resistance_mechanisms", "producer_organisms",
                  "activity_spectrum", "causal_graphs", "evidence", "discussions"):
        derivable.add(sum(1 for r in records if r.get(field)))
    for status in ("EXACT", "MINTED"):
        derivable.add(sum(1 for r in records if r.get("grounding_status") == status))
    # Records carrying CARD-SOURCED mechanism evidence — the README's own
    # definition, which is narrower than "has any mechanism item".
    card_marker = "CARD/ARO asserts"

    def card_sourced(record):
        for field in ("molecular_targets", "resistance_mechanisms"):
            for item in (record.get(field) or []):
                for evidence in (item.get("evidence") or []):
                    if card_marker in str(evidence.get("notes") or ""):
                        return True
        return False

    derivable.add(sum(1 for r in records if card_sourced(r)))
    derivable.add(sum(1 for r in records
                      if r.get("molecular_targets") or r.get("resistance_mechanisms")))
    derivable.add(sum(1 for r in records
                      if "belongs to an" in str(r.get("mode_of_action_notes") or "")))
    # Records in a class that carry no general antibacterial role — the
    # "76 of the 78" claim about antimycobacterials.
    for klass in classes:
        derivable.add(sum(1 for r in records if r["antimicrobial_class"] == klass
                          and "CHEBI:33282" not in (r.get("activity_roles") or [])))
    # Inventory sizes, and the structureless concepts the worklist reports.
    for name in ("aro_antibiotics", "chebi_antimicrobials", "chebi_role_names",
                 "aro_resistance_edges", "aro_target_edges"):
        path = repo_root / "data" / "raw" / f"{name}.tsv"
        if path.exists():
            derivable.add(sum(1 for _ in path.open(encoding="utf-8")) - 1)
    from curation_worklist import no_structure_queue, producer_candidate_queue
    derivable.add(len(no_structure_queue()))
    # The producer-candidate queue's size, quoted in docs/HARMONIZATION.md.
    derivable.add(len(producer_candidate_queue(records)))
    # ...and the subset whose phrase is followed by a parseable binomial.
    derivable.add(sum(1 for row in producer_candidate_queue(records)
                      if "(no binomial)" not in row["hint"]))

    unregistered: list[str] = []
    used_exemptions: set[str] = set()
    for name in CLAIM_FILES:
        path = repo_root / name
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for match in re.finditer(CLAIM_SHAPE, text):
            # The surrounding line, so an exemption is tied to ITS sentence. The
            # first version compared only the matched "57 records", so
            # `phrase in ex` exempted that number in ANY sentence in ANY scanned
            # file — the opposite of the phrase-matching it claimed.
            line_start = text.rfind("\n", 0, match.start()) + 1
            line_end = text.find("\n", match.end())
            line = re.sub(r"\s+", " ", text[line_start:line_end if line_end != -1 else None])
            if any(ex in line for ex in CLAIM_EXEMPTIONS):
                used_exemptions.update(ex for ex in CLAIM_EXEMPTIONS if ex in line)
                continue
            value = int(match.group(1).replace(",", ""))
            if value not in derivable:
                phrase = re.sub(r"\s+", " ", match.group(0))
                unregistered.append(
                    f"{name}: {phrase!r} in {line.strip()[:90]!r} — "
                    f"no derived quantity equals {value}")
    assert unregistered == [], unregistered

    # A dead exemption is a rule nobody can see is gone, the way a dead
    # NUMERIC_CLAIMS row would be.
    dead = sorted(set(CLAIM_EXEMPTIONS) - used_exemptions)
    assert dead == [], f"exemptions that match nothing any more: {dead}"
