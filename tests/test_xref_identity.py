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


def test_document_namespaces_live_in_document_xrefs(records):
    """A patent covers a CLASS and an article covers a topic, so neither
    identifies a structure. They were kept in `xrefs` for want of a destination
    (#136); the destination exists now, and they are there and nowhere else."""
    from seed_from_sources import DOCUMENT_XREF_PREFIXES, NON_STRUCTURE_XREF_PREFIXES

    assert {"patent", "wikipedia.en"} == DOCUMENT_XREF_PREFIXES
    assert not (DOCUMENT_XREF_PREFIXES & NON_STRUCTURE_XREF_PREFIXES)
    in_docs = {x.split(":", 1)[0] for _p, r in records for x in (r.get("document_xrefs") or [])}
    assert in_docs == DOCUMENT_XREF_PREFIXES, "moved, but not all of them, or something else came along"
    leaked = [f"{p.name}: {x}" for p, r in records
              for x in (r.get("xrefs") or []) if x.split(":", 1)[0] in DOCUMENT_XREF_PREFIXES]
    assert leaked == [], leaked[:8]
    # `pdb:` really is dropped, not moved: a macromolecular entry is not about
    # this compound at all.
    offenders = [f"{p.name}: {x}" for p, r in records for slot in ("xrefs", "drug_xrefs", "document_xrefs")
                 for x in (r.get(slot) or []) if x.split(":", 1)[0].lower() == "pdb"]
    assert offenders == [], offenders[:8]


def test_drug_namespaces_live_in_drug_xrefs_and_nothing_in_xrefs_spans_two_structures(records):
    """`xrefs` means one accession, one structure, and now it does.

    DrugBank identifies a DRUG, so `drugbank:DB00639` covering butoconazole,
    its nitrate and both enantiomers is that namespace's meaning; it lives in
    `drug_xrefs`. What stays in `xrefs` is held to the contract corpus-wide by
    the seeder: an accession landing on two InChIKeys is withheld from both.
    A "known coarse" declaration used to let 20 such accessions through as a
    listed exception (#137); the invariant is asserted instead of declared.
    """
    from seed_from_sources import DRUG_GRANULARITY_XREF_PREFIXES

    in_drug = {x.split(":", 1)[0] for _p, r in records for x in (r.get("drug_xrefs") or [])}
    assert in_drug == DRUG_GRANULARITY_XREF_PREFIXES
    leaked = [f"{p.name}: {x}" for p, r in records
              for x in (r.get("xrefs") or []) if x.split(":", 1)[0] in DRUG_GRANULARITY_XREF_PREFIXES]
    assert leaked == [], leaked[:8]

    spans = collections.defaultdict(set)
    for _p, record in records:
        key = (record.get("chemical_structure") or {}).get("standard_inchi_key")
        for xref in (record.get("xrefs") or []):
            spans[xref].add(key)
    multi = sorted(x for x, keys in spans.items() if len(keys) > 1)
    assert multi == [], f"{len(multi)} structure-exact accession(s) span two structures: {multi[:6]}"
    # And the drug slot really does span, or moving it out was theatre.
    drug_spans = collections.defaultdict(set)
    for _p, record in records:
        key = (record.get("chemical_structure") or {}).get("standard_inchi_key")
        for xref in (record.get("drug_xrefs") or []):
            drug_spans[xref].add(key)
    assert any(len(keys) > 1 for keys in drug_spans.values())


def test_withheld_accessions_are_queued_not_lost(records):
    """A refused assertion needs a destination. The queue reconstructs the
    withheld accessions from the inventories through the seeder's own spanning
    test, so it cannot disagree with what the seeder withheld."""
    from curation_worklist import xref_span_conflict_queue

    docs = [r for _p, r in records]
    queued = xref_span_conflict_queue(docs)
    accessions = {row["source_id"] for row in queued}
    assert "chembl:CHEMBL1999880" in accessions, "the narbomycin/nybomycin pair, #137's live case"
    assert "cas:69388-84-7" in accessions
    assert len(accessions) == 20, sorted(accessions)
    # An accession the per-record gate refused for another reason never reaches
    # the spanning test, in the seeder or here: CHEBI:8309 is polymyxin B1, and
    # rule 2 refuses it on polymyxin B2 as a known different structure. A queue
    # that restated the gate from the inventory listed it as spanning.
    assert "CHEBI:8309" not in accessions
    present = {x for r in docs for x in (r.get("xrefs") or [])}
    assert not (accessions & present), sorted(accessions & present)[:6]
    # Every queued record really carries one of the spanning concepts.
    assert all(any(row["key"] == r["identifier"] for r in docs) for row in queued)


def test_spanning_accessions_is_structure_exact_only():
    from seed_from_sources import spanning_accessions

    found = spanning_accessions([
        ("KEY1", "cas:1"), ("KEY2", "cas:1"),                    # spans: withheld
        ("KEY1", "drugbank:DB1"), ("KEY2", "drugbank:DB1"),      # drug slot: not this function's business
        ("KEY1", "patent:US1"), ("KEY2", "patent:US1"),          # document slot: likewise
        ("KEY1", "cas:2"), ("KEY1", "cas:2"),                    # one key twice is not a span
        (None, "cas:3"), ("KEY9", "cas:3"),                      # no key on one side: not a span
    ])
    assert found == {"cas:1": {"KEY1", "KEY2"}}


def test_every_xref_prefix_is_declared_and_the_type_enforces_it(records, repo_root):
    """A prefix the schema cannot expand is an identifier that goes nowhere.

    8,796 of 12,419 cross-references carried one while closed validation stayed
    green, because `curie` checks shape only (#96). The `xref_curie` alternation
    is asserted equal to what the corpus carries, and the validator is shown to
    reject a prefix outside it.
    """
    import re

    import yaml

    from antibioticmech.validation.write_validated import validate_antibiotic

    schema = yaml.safe_load((repo_root / "src" / "antibioticmech" / "schema"
                             / "antibioticmech.yaml").read_text(encoding="utf-8"))
    declared = set(schema["prefixes"])
    pattern = schema["types"]["xref_curie"]["pattern"]
    allowed = {p.replace("\\", "") for p in re.match(r"\^\((.*)\):", pattern).group(1).split("|")}
    used = {x.split(":", 1)[0] for _p, r in records
            for slot in ("xrefs", "drug_xrefs", "document_xrefs") for x in (r.get(slot) or [])}
    assert used <= declared, sorted(used - declared)
    assert used == allowed, (sorted(used - allowed), sorted(allowed - used))

    doc = yaml.safe_load((repo_root / "data" / "antibiotics" / "antibacterial"
                          / "erythromycin-a.yaml").read_text(encoding="utf-8"))
    assert validate_antibiotic(doc) == []
    doc["xrefs"] = list(doc.get("xrefs") or []) + ["CHEMBL.COMPOUND:CHEMBL1"]
    assert validate_antibiotic(doc), "an undeclared prefix validated clean"


def test_the_site_links_only_namespaces_that_resolve(repo_root):
    """Deriving link templates from every schema prefix minted 404 links.

    The corpus's own w3id namespace resolves nowhere, and it appeared as a
    "resolve" link on 260 pages; three print registries have no resolver and
    appeared on 1,935. Templates are the xref namespaces plus the few labels the
    site resolves on purpose, and a base that needs a file suffix carries it.
    """
    import re

    import yaml
    from render_pages import ALSO_RESOLVED, NO_RESOLVER, XREF_URL_TEMPLATES

    schema = yaml.safe_load((repo_root / "src" / "antibioticmech" / "schema"
                             / "antibioticmech.yaml").read_text(encoding="utf-8"))
    pattern = schema["types"]["xref_curie"]["pattern"]
    xref_prefixes = {p.replace("\\", "") for p in re.match(r"\^\((.*)\):", pattern).group(1).split("|")}
    assert set(XREF_URL_TEMPLATES) == (xref_prefixes - NO_RESOLVER) | ALSO_RESOLVED
    assert "antibioticmech" not in XREF_URL_TEMPLATES
    assert all("{}" in template for template in XREF_URL_TEMPLATES.values())
    assert XREF_URL_TEMPLATES["ppdb"].endswith("{}.htm")
    assert XREF_URL_TEMPLATES["pesticides"].endswith("{}.html")


def test_withholding_strips_a_spanning_accession_from_every_record_it_spans():
    """Direct, because the committed corpus is already stripped: deleting the
    corpus-wide pass left every test green and only verify-corpus noticed."""
    from seed_from_sources import REFUSED_SPANNING_XREFS, withhold_spanning_xrefs

    records = {
        "A": {"identifier": "A", "label": "a", "chemical_structure": {"standard_inchi_key": "K1"},
              "xrefs": ["cas:1", "cas:9"], "drug_xrefs": ["drugbank:DB1"]},
        "B": {"identifier": "B", "label": "b", "chemical_structure": {"standard_inchi_key": "K2"},
              "xrefs": ["cas:1"], "drug_xrefs": ["drugbank:DB1"]},
        "C": {"identifier": "C", "label": "c", "chemical_structure": {"standard_inchi_key": "K1"},
              "xrefs": ["cas:9"]},
    }
    REFUSED_SPANNING_XREFS.clear()
    assert withhold_spanning_xrefs(records) == 2
    assert records["A"]["xrefs"] == ["cas:9"]
    assert "xrefs" not in records["B"], "an emptied slot is removed, not left as []"
    assert records["C"]["xrefs"] == ["cas:9"], "the same key twice is one structure, not a span"
    assert records["A"]["drug_xrefs"] == ["drugbank:DB1"], "drug slots are not this pass's business"
    assert {r[0] for r in REFUSED_SPANNING_XREFS} == {"A", "B"}
    assert all("(" in r[2] for r in REFUSED_SPANNING_XREFS), "records are named by label and identifier"


def test_no_record_carries_an_empty_xref_slot(records):
    empty = [f"{p.name}: {slot}" for p, r in records for slot in ("xrefs", "drug_xrefs", "document_xrefs")
             if slot in r and not r[slot]]
    assert empty == [], empty[:8]
