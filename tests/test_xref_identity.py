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


def test_document_namespaces_are_named_even_though_they_are_kept(records):
    """A patent covers a CLASS and an article covers a topic, so neither
    identifies a structure — and both are kept anyway.

    Dropping them was tried and reverted, because measuring said the remedy cost
    more than the defect: 96% of the 709 `wikipedia.en` accessions and 97% of the
    1,027 `patent` accessions map to exactly ONE structure here, so removing
    ~1,800 links would have fixed 57 false equivalences and left 7 records with
    no cross-references at all. #92 asked for such identifiers to be MOVED, and
    the destination is a schema decision not yet taken (#136).

    So the test asserts the honest state: the namespaces are NAMED, and they are
    still present. A future PR that moves them should change this test
    deliberately rather than find it already green.
    """
    from seed_from_sources import DOCUMENT_XREF_PREFIXES, NON_STRUCTURE_XREF_PREFIXES

    assert {"patent", "wikipedia.en"} == DOCUMENT_XREF_PREFIXES
    # Named, but NOT dropped — the two sets are deliberately disjoint.
    assert not (DOCUMENT_XREF_PREFIXES & NON_STRUCTURE_XREF_PREFIXES)

    present = {x.split(":", 1)[0] for _p, r in records for x in (r.get("xrefs") or [])}
    assert present >= DOCUMENT_XREF_PREFIXES, "they were dropped without updating this test"

    # `pdb:` really is dropped: a macromolecular entry is not a compound at all,
    # which is a stronger claim than "this identifier is coarse".
    assert "pdb" in NON_STRUCTURE_XREF_PREFIXES
    offenders = [f"{p.name}: {x}" for p, r in records
                 for x in (r.get("xrefs") or []) if x.split(":", 1)[0].lower() == "pdb"]
    assert offenders == [], offenders[:8]


def test_drug_granularity_namespaces_are_named_rather_than_pretended_about(records):
    """`xrefs` cannot be read as "one accession, one structure", and saying so is
    better than implying otherwise.

    `drugbank:DB00639` legitimately covers butoconazole, butoconazole nitrate
    and both enantiomers: DrugBank identifies a DRUG. Those accessions are kept
    because they are useful, and the exception is declared in the seeder rather
    than left for a consumer to discover.
    """
    from seed_from_sources import (
        DOCUMENT_XREF_PREFIXES,
        DRUG_GRANULARITY_XREF_PREFIXES,
        KNOWN_COARSE_XREF_PREFIXES,
    )

    # The constant is a DECLARATION, not a code path — the same-structure gate
    # only compares ChEBI ids, so nothing reads it at seed time. That makes it
    # exactly the kind of comment-shaped constant that drifts into fiction, so
    # it is checked against the corpus: every prefix named must really span
    # several structures, or it is claiming a problem that does not exist.
    spans = collections.defaultdict(set)
    for _p, record in records:
        key = (record.get("chemical_structure") or {}).get("standard_inchi_key")
        if not key:
            continue
        for xref in (record.get("xrefs") or []):
            spans[xref].add(key)
    multi_prefixes = {x.split(":", 1)[0] for x, keys in spans.items() if len(keys) > 1}
    seen = {x.split(":", 1)[0] for x in spans}
    unfounded = {p for p in DRUG_GRANULARITY_XREF_PREFIXES
                 if p in seen and p not in multi_prefixes}
    assert unfounded == set(), (
        f"declared as drug-granularity but never spans two structures: {sorted(unfounded)}")

    # And a prefix the corpus does not contain AT ALL cannot be grounded either
    # way, so declaring one is speculation the check would skip in silence.
    # `unii` was declared and had zero occurrences. If such a namespace arrives
    # later and really does span structures, the undeclared assertion below
    # catches it then — which is the right moment to declare it.
    absent = {p for p in DRUG_GRANULARITY_XREF_PREFIXES if p not in seen}
    assert absent == set(), (
        f"declared as drug-granularity but absent from the corpus, so unverifiable: "
        f"{sorted(absent)}")
    assert "drugbank" in DRUG_GRANULARITY_XREF_PREFIXES

    # Nothing in a namespace we have NOT accounted for may span several
    # structures. The first version of this filtered on ("pdb", "patent",
    # "wikipedia.en") — exactly the prefixes the test above asserts are absent
    # or accounted for — so the set was empty by construction and the assertion
    # could never fail. Replacing it with `pass` left 7 tests passing.
    #
    # Blind to 22 real ones: chembl:CHEMBL134561 is asserted to be both cefdinir
    # and iclaprim, pdb-ccd:CLQ both chloroquine and its (R)-enantiomer.
    # `pdb-ccd` was kept in #92 precisely because it identifies a chemical
    # component, so those are the same defect that PR fixed, surviving under a
    # test that said it could not.
    multi = {x for x, keys in spans.items() if len(keys) > 1}
    accounted = (DRUG_GRANULARITY_XREF_PREFIXES | DOCUMENT_XREF_PREFIXES
                 | KNOWN_COARSE_XREF_PREFIXES)
    undeclared = {x for x in multi if x.split(":", 1)[0] not in accounted}
    assert undeclared == set(), (
        f"{len(undeclared)} accession(s) in namespaces claiming to be "
        f"structure-exact span several structures: {sorted(undeclared)[:6]}")
