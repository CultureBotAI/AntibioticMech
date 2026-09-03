"""What the same-structure gate could not check, and what it does about it (#164).

`xrefs` means THE SAME STRUCTURE, and the gate enforces that by comparing
InChIKeys — which needs a structure on both sides. When the target had none the
comparison was skipped and the xref published unexamined, so the check did
nothing on exactly the inputs most likely to be wrong. That is how `cefdinir`
carried `CHEBI:131724`, which is *iclaprim*, an unrelated antibacterial.

The fix is not "drop what we cannot verify" — the corpus deliberately keeps
unverified source assertions rather than discarding them. It is that "cannot
compare structures" is not "no evidence": the inventory knows the target's NAME
even when it has no structure, and a name matching nothing is a contradiction
rather than an absence. So refusal happens on evidence, and only on evidence.
"""

from __future__ import annotations

import csv
import glob
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "src"))

from curation_worklist import xref_name_conflict_queue, xref_unverified_queue  # noqa: E402
from seed_from_sources import (  # noqa: E402
    structureless_xref_conflict,
    xref_names,
)


def _records():
    return [yaml.safe_load(Path(p).read_text(encoding="utf-8"))
            for p in glob.glob(str(REPO_ROOT / "data" / "antibiotics" / "**" / "*.yaml"),
                               recursive=True)]


def _inventory():
    with (REPO_ROOT / "data" / "raw" / "chebi_antimicrobials.tsv").open(encoding="utf-8") as fh:
        return {row["chebi_id"]: row for row in csv.DictReader(fh, delimiter="\t")}


# --------------------------------------------------------------------------
# The corpus no longer publishes the false equivalence
# --------------------------------------------------------------------------

def test_cefdinir_no_longer_claims_to_be_iclaprim():
    """The case #164 was filed for, named so a regression is unmistakable."""
    record = next(r for r in _records() if r["identifier"] == "CHEBI:3485")
    assert "CHEBI:131724" not in (record.get("xrefs") or []), record.get("xrefs")


def test_no_published_xref_points_at_a_structureless_term_of_another_name():
    """The general form: every surviving structureless target shares a name."""
    inventory = _inventory()
    offenders = []
    for record in _records():
        own = {" ".join((record.get("label") or "").lower().split())}
        own |= {" ".join((s.get("name") or "").lower().split())
                for s in (record.get("synonyms") or [])}
        for xref in record.get("xrefs") or []:
            row = inventory.get(xref)
            if row is None or row.get("standard_inchi_key"):
                continue
            if not (own & xref_names(row)):
                offenders.append(f"{record['label']} -> {xref} ({row['name']})")
    assert offenders == [], offenders


# --------------------------------------------------------------------------
# The rule refuses on evidence, never on ignorance
# --------------------------------------------------------------------------

def test_a_comparable_target_is_left_to_the_structure_gate():
    assert structureless_xref_conflict({"x"}, "CHEBI:1", "SOMEKEY-AAAAAAAAAA-A", {"y"}) is None


def test_a_target_absent_from_the_inventory_is_never_refused():
    """Absence of evidence is not evidence. 102 xrefs depend on this."""
    assert structureless_xref_conflict({"x"}, "CHEBI:1", "", set()) is None


def test_a_matching_name_is_never_refused():
    assert structureless_xref_conflict({"nystatin"}, "CHEBI:1", "", {"nystatin"}) is None


def test_a_wholly_non_matching_name_is_refused():
    reason = structureless_xref_conflict({"cefdinir"}, "CHEBI:131724", "", {"iclaprim"})
    assert reason and "CHEBI:131724" in reason and "iclaprim" in reason, reason


def test_a_synonym_match_counts_as_agreement():
    """`gentamicin C -> CHEBI:75616` survives on the target's UniProt synonym.

    Refusing it would be refusing on a PARSING failure rather than on evidence:
    the inventory writes synonyms as `TYPE=value`, and comparing the raw strings
    makes every synonym unmatchable.
    """
    inventory = _inventory()
    assert "gentamicin c" in xref_names(inventory["CHEBI:75616"])
    record = next((r for r in _records()
                   if "CHEBI:75616" in (r.get("xrefs") or [])), None)
    assert record is not None, "the gentamicin C xref was refused, not spared"


# --------------------------------------------------------------------------
# Refusals have a destination, and it agrees with the gate
# --------------------------------------------------------------------------

def test_every_refusal_is_reachable_on_the_worklist():
    """#136's lesson: a dropped source assertion needs a destination."""
    rows = xref_name_conflict_queue(_records())
    assert rows, "the queue is empty; a refusal that nobody can see is a deletion"
    assert any(r["key"] == "CHEBI:3485" and r["source_id"] == "CHEBI:131724" for r in rows), rows


def test_the_queue_reports_exactly_what_the_gate_refused():
    """A queue that drifts from the gate either hides or invents refusals.

    It over-reported by three before honouring the gate's precedence:
    erythromycin A, lividomycin A and mycinamicin IV carry their parent in both
    `parent_compounds` and `xrefs`, and are removed as BROADER before the naming
    rule is ever consulted.
    """
    records = _records()
    queued = {(r["key"], r["source_id"]) for r in xref_name_conflict_queue(records)}
    for identifier, xref in queued:
        record = next(r for r in records if r["identifier"] == identifier)
        assert xref not in (record.get("xrefs") or []), (
            f"{identifier} still publishes {xref}, so it was not refused")
        assert xref not in (record.get("parent_compounds") or []), (
            f"{identifier}: {xref} is a BROADER removal, not a naming refusal")


def test_the_unverified_queue_distinguishes_unknown_from_structureless():
    """One number for two situations told a curator nothing actionable."""
    hints = " ".join(r["hint"] for r in xref_unverified_queue(_records()))
    assert "absent from the inventory" in hints
    assert "no structure" in hints
