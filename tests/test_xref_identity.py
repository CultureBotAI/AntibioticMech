"""`xrefs` means the same chemical structure. Enforced, not just documented.

docs/CURATION.md and the schema both define `xrefs` as identifiers for the SAME
structure, with anything strictly broader belonging in `parent_compounds`. Three
kinds of violation reached the corpus anyway, with every gate green (#92):
a macromolecular PDB entry, a ChEBI term with a different InChIKey, and
identifiers listed in both `xrefs` and `parent_compounds` at once.
"""

from __future__ import annotations

import collections
import csv
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "src"))


def _chebi_keys() -> dict[str, str]:
    with (REPO_ROOT / "data" / "raw" / "chebi_antimicrobials.tsv").open(encoding="utf-8") as fh:
        return {r["chebi_id"]: r["standard_inchi_key"]
                for r in csv.DictReader(fh, delimiter="\t") if r.get("standard_inchi_key")}


def test_no_xref_names_a_different_structure(records):
    """The polymyxin case: B2 listed CHEBI:8309, which is polymyxin B1.

    Only checks pairs where BOTH InChIKeys are known — the rest are unverifiable
    from the committed inventory and are queued instead, deliberately.
    """
    keys = _chebi_keys()
    wrong = []
    for path, record in records:
        own = (record.get("chemical_structure") or {}).get("standard_inchi_key")
        if not own:
            continue
        for xref in (record.get("xrefs") or []):
            other = keys.get(xref)
            if other and other != own:
                wrong.append(f"{path.name}: {xref} is {other}, record is {own}")
    assert wrong == [], wrong[:10]


def test_no_identifier_is_both_an_xref_and_a_parent(records):
    """`parent_compounds` means STRICTLY broader; `xrefs` means the same
    structure. An identifier in both asserts two things that cannot both hold —
    erythromycin A, lividomycin A and mycinamicin IV each did."""
    both = []
    for path, record in records:
        overlap = set(record.get("xrefs") or []) & set(record.get("parent_compounds") or [])
        if overlap:
            both.append(f"{path.name}: {sorted(overlap)}")
    assert both == [], both[:10]


def test_no_macromolecular_accession_is_a_chemical_xref(records):
    """A PDB accession identifies a structure ENTRY, not a chemical identity.

    Ampicillin carried pdb:1H8S — an anti-ampicillin ANTIBODY complex — and
    alsterpaullone carried pdb:1Q3W, a human GSK3beta complex. `pdb-ccd` is a
    ligand chemical component and is a legitimate chemical identifier, so the
    rule is namespace-specific rather than a blanket ban on "pdb".
    """
    offenders = []
    for path, record in records:
        for xref in (record.get("xrefs") or []):
            prefix = xref.split(":", 1)[0]
            if prefix.lower() == "pdb":
                offenders.append(f"{path.name}: {xref}")
    assert offenders == [], offenders[:10]
    # And the legitimate neighbour is not collateral damage.
    assert any(x.startswith("pdb-ccd:")
               for _p, r in records for x in (r.get("xrefs") or [])), \
        "pdb-ccd disappeared entirely; the rule is too broad"


def test_the_gate_keeps_what_it_cannot_check_and_queues_it(records):
    """Dropping a source assertion because it cannot be verified is a worse
    error than carrying one unverified — but carrying it SILENTLY is the error
    this queue removes."""
    from curation_worklist import xref_unverified_queue

    keys = _chebi_keys()
    docs = [r for _p, r in records]
    unchecked = {r["identifier"] for r in docs
                 if any(x.startswith("CHEBI:") and x not in keys
                        for x in (r.get("xrefs") or []))}
    assert unchecked, "no unverifiable ChEBI xref remains; this test guards nothing"
    queued = {row["key"] for row in xref_unverified_queue(docs)}
    assert unchecked == queued, sorted(unchecked ^ queued)[:10]


def test_the_gate_is_load_bearing():
    """Each of the three rules must change an answer, or it is decoration."""
    from seed_from_sources import NON_STRUCTURE_XREF_PREFIXES, XREF_PREFIX, normalize_xref

    # PDB is no longer a mapped chemical prefix, and is named as non-structural.
    assert "PDB" not in XREF_PREFIX
    assert "pdb" in NON_STRUCTURE_XREF_PREFIXES
    # A raw PDB xref no longer normalises to a chemical identifier...
    assert normalize_xref("PDB:1H8S") is None
    # ...while pdb-ccd still does, being a ligand chemical component.
    assert normalize_xref("pdb-ccd:AMP") == "pdb-ccd:AMP"


def test_a_document_namespace_is_not_a_chemical_xref(records):
    """A patent covers a CLASS of compounds and a Wikipedia article covers a
    topic; neither identifies a structure.

    `patent:WO2011108759` sat on both ametoctradin and silthiofam — two
    unrelated fungicides — which is the opposite of what an xref asserts. Same
    argument that removed `pdb:`, applied to the namespaces where it also holds.
    """
    from seed_from_sources import NON_STRUCTURE_XREF_PREFIXES

    assert {"patent", "wikipedia.en", "pdb"} <= NON_STRUCTURE_XREF_PREFIXES
    offenders = [f"{p.name}: {x}" for p, r in records
                 for x in (r.get("xrefs") or [])
                 if x.split(":", 1)[0] in ("patent", "wikipedia.en", "pdb")]
    assert offenders == [], offenders[:8]


def test_drug_granularity_namespaces_are_named_rather_than_pretended_about(records):
    """`xrefs` cannot be read as "one accession, one structure", and saying so is
    better than implying otherwise.

    `drugbank:DB00639` legitimately covers butoconazole, butoconazole nitrate and
    both enantiomers: DrugBank identifies a DRUG. Those accessions are kept
    because they are useful, but the exception is declared in the seeder rather
    than left for a consumer to discover.
    """
    from seed_from_sources import DRUG_GRANULARITY_XREF_PREFIXES

    # The constant is a DECLARATION, not a code path — the same-structure gate
    # only compares ChEBI ids, so nothing reads it at seed time. That makes it
    # exactly the kind of comment-shaped constant that drifts into fiction, so
    # it is checked against the corpus: every prefix named here must really
    # span several structures, or the declaration is claiming a problem that
    # does not exist.
    spans = collections.defaultdict(set)
    for _p, record in records:
        key = (record.get("chemical_structure") or {}).get("standard_inchi_key")
        if not key:
            continue
        for xref in (record.get("xrefs") or []):
            spans[xref].add(key)
    multi_prefixes = {x.split(":", 1)[0] for x, keys in spans.items() if len(keys) > 1}
    unfounded = {p for p in DRUG_GRANULARITY_XREF_PREFIXES if p in
                 {x.split(":", 1)[0] for x in spans} and p not in multi_prefixes}
    assert unfounded == set(), (
        f"declared as drug-granularity but never spans two structures: {sorted(unfounded)}")
    assert "drugbank" in DRUG_GRANULARITY_XREF_PREFIXES

    multi = {x for x, keys in spans.items() if len(keys) > 1}
    # Every remaining multi-structure accession must be in a namespace we have
    # declared works at drug granularity, or in one whose semantics we have not
    # yet settled — never in a namespace claiming to be structure-exact.
    undeclared = {x for x in multi
                  if x.split(":", 1)[0] in ("pdb", "patent", "wikipedia.en")}
    assert undeclared == set(), sorted(undeclared)[:8]
