"""The organismal axis: whose organism, which strain, which allele (#94).

Resistance, production and activity are claims about ORGANISMS, and this corpus
was carrying them as prose. All 217 PHI-base associations had their taxon,
strain, protein accession, allele, phenotype and assay concatenated into a
single `note` string, which the seeder then substring-searched to recognize its
own lane. Nothing could ask "which resistance alleles are known in *Aspergillus
flavus*?" because no field held the answer.

The tests below defend the structure, not the prose. Each one is written so that
removing the fix makes it fail: the note is checked for the ABSENCE of the facts
that now live in slots, so re-inlining them fails; the schema rules are exercised
through the write gate, so relaxing them fails; and the strain splitter is
checked on the exact source strings that motivated it.
"""

from __future__ import annotations

import glob
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "src"))

from curation_worklist import activity_candidate_queue  # noqa: E402
from seed_from_sources import (  # noqa: E402
    PHIBASE_NOTE_MARKER,
    PHIBASE_RESISTANCE_SOURCE,
    attach_mibig_producers,
    attach_phibase_resistance,
    is_phibase_sourced_resistance,
    split_organism_strain,
)

from antibioticmech.validation.write_validated import (  # noqa: E402
    validate_antibiotic as validate_record,
)


def _records():
    return [yaml.safe_load(Path(p).read_text(encoding="utf-8"))
            for p in glob.glob(str(REPO_ROOT / "data" / "antibiotics" / "**" / "*.yaml"),
                               recursive=True)]


def _record_with(**fields):
    record = {
        "identifier": "CHEBI:1",
        "label": "test compound",
        "antimicrobial_class": "ANTIBACTERIAL",
        "curation_status": "SEEDED",
        "grounding_status": "EXACT",
        "chemical_structure": {"standard_inchi_key": "AAAAAAAAAAAAAA-AAAAAAAAAA-A"},
        "source_concepts": [{"source": "CHEBI", "source_id": "CHEBI:1",
                             "source_label": "test compound",
                             "minted_identifier": "antibioticmech:chebi-0000000000"}],
    }
    record.update(fields)
    return record


def _mechanism(**fields):
    item = {
        "mechanism_type": "UNKNOWN",
        "label": "an association",
        "evidence": [{"reference": "PMID:1"}],
    }
    item.update(fields)
    return item


# --------------------------------------------------------------------------
# The corpus actually carries the structure
# --------------------------------------------------------------------------

def test_every_phibase_association_names_its_organism_in_a_field():
    """The claim IS the organism, so it cannot live only in prose."""
    missing = []
    seen = 0
    for record in _records():
        for item in record.get("resistance_mechanisms") or []:
            if item.get("source") != PHIBASE_RESISTANCE_SOURCE:
                continue
            seen += 1
            for slot in ("taxon_id", "taxon_label", "alteration", "phenotype_label", "assay"):
                if not item.get(slot):
                    missing.append(f"{record['identifier']}: {item['label']!r} lacks {slot}")
    assert seen == 217, f"expected 217 PHI-base associations, found {seen}"
    assert missing == [], missing[:10]


def test_the_note_no_longer_restates_what_the_slots_hold():
    """The failure mode this fixes is prose standing in for structure.

    Re-inlining the taxon, the accession or the PHIG id into the note — the
    shape the corpus had before #94 — fails here even though every other gate
    would stay green, because a note is a valid string whatever it contains.
    """
    offenders = []
    for record in _records():
        for item in record.get("resistance_mechanisms") or []:
            if item.get("source") != PHIBASE_RESISTANCE_SOURCE:
                continue
            note = str(item.get("note") or "")
            for slot in ("taxon_label", "strain", "protein_accession", "phenotype_id"):
                value = item.get(slot)
                if value and str(value) in note:
                    offenders.append(
                        f"{record['identifier']}: note restates {slot}={value!r}")
            if PHIBASE_NOTE_MARKER in note:
                offenders.append(f"{record['identifier']}: note still carries the lane marker")
    assert offenders == [], offenders[:10]


def test_a_strain_designation_is_never_left_inside_the_species_name():
    """`NCBITaxon:1928` denotes a species; labelling it with a strain lies."""
    offenders = []
    for record in _records():
        items = (record.get("producer_organisms") or [])
        items += [i for i in (record.get("resistance_mechanisms") or []) if i.get("taxon_label")]
        for item in items:
            label = item["taxon_label"]
            if item.get("strain") and item["strain"] in label:
                offenders.append(f"{record['identifier']}: {label!r} contains its own strain")
    assert offenders == [], offenders


def test_every_producer_claim_carries_evidence_with_the_basis_it_rests_on():
    """A scalar reference could not say what the reference was cited FOR."""
    offenders = []
    seen = 0
    for record in _records():
        for item in record.get("producer_organisms") or []:
            seen += 1
            if "reference" in item:
                offenders.append(f"{record['identifier']}: scalar `reference` survives")
            evidence = item.get("evidence") or []
            if not evidence:
                offenders.append(f"{record['identifier']}: producer has no evidence")
            for entry in evidence:
                if not entry.get("reference") or not entry.get("notes"):
                    offenders.append(f"{record['identifier']}: evidence without a basis note")
    assert seen, "no producer organisms in the corpus to check"
    assert offenders == [], offenders


# --------------------------------------------------------------------------
# The write gate refuses the shapes that would undo it
# --------------------------------------------------------------------------

def _errors(**fields):
    """Error-severity results from the write gate.

    `validate_antibiotic` RETURNS its errors rather than raising, so a test that
    wrapped it in `pytest.raises` would pass on a schema whose rules had been
    deleted. Asserting on the returned messages is what actually holds.
    """
    return [str(r.message) for r in validate_record(_record_with(**fields))]


def test_an_allele_with_no_organism_is_refused():
    """`cyp51B(H399P)` with no taxon is a string, not an observation."""
    errors = _errors(resistance_mechanisms=[
        _mechanism(alteration="cyp51B(H399P) (amino acid mutation)")])
    assert any("taxon_label" in e for e in errors), errors


def test_a_taxon_curie_with_no_name_is_refused():
    errors = _errors(resistance_mechanisms=[_mechanism(taxon_id="NCBITaxon:318829")])
    assert any("taxon_label" in e for e in errors), errors


def test_a_strain_curie_with_no_strain_designation_is_refused():
    errors = _errors(resistance_mechanisms=[
        _mechanism(taxon_id="NCBITaxon:1773", taxon_label="Mycobacterium tuberculosis",
                   strain_taxon_id="NCBITaxon:83332")])
    assert any("'strain'" in e for e in errors), errors


def test_a_fully_specified_association_is_accepted():
    """The rules must reject the bad shape without rejecting the real one."""
    assert _errors(resistance_mechanisms=[
        _mechanism(taxon_id="NCBITaxon:1773", taxon_label="Mycobacterium tuberculosis",
                   strain="H37Rv", strain_taxon_id="NCBITaxon:83332",
                   alteration="Ppe44+ (wild type) [Overexpression]",
                   protein_accession="UniProtKB:P9WHZ3", phenotype_id="PHIPO:0000632",
                   phenotype_label="resistance to hydrogen peroxide",
                   assay="Cell growth assay", source=PHIBASE_RESISTANCE_SOURCE)]) == []


def test_a_route_level_mechanism_still_needs_no_organism():
    """CARD asserts routes, which are organism-independent by construction."""
    assert _errors(resistance_mechanisms=[
        _mechanism(mechanism_type="ANTIBIOTIC_EFFLUX", label="AcrAB-TolC efflux")]) == []


# --------------------------------------------------------------------------
# The strain splitter, on the strings that motivated it
# --------------------------------------------------------------------------

@pytest.mark.parametrize("label,expected", [
    ("Streptomyces rochei NBRC 12908", ("Streptomyces rochei", "NBRC 12908")),
    ("Streptomyces mirabilis strain P8-A", ("Streptomyces mirabilis", "P8-A")),
    ("Francisella tularensis subsp. tularensis SCHU S4",
     ("Francisella tularensis subsp. tularensis", "SCHU S4")),
    ("Streptomyces sp. BC16019", ("Streptomyces sp.", "BC16019")),
    ("Amycolatopsis orientalis HCCB10007 (ATCC43491)",
     ("Amycolatopsis orientalis", "HCCB10007 (ATCC43491)")),
    ("Corallococcus coralloides 1071", ("Corallococcus coralloides", "1071")),
    # Nothing to split: a bare binomial, and a name this parser does not
    # understand. Both must come back whole rather than truncated on a guess.
    ("Lyngbya majuscula", ("Lyngbya majuscula", None)),
    ("Candida", ("Candida", None)),
    ("unclassified Streptomyces", ("unclassified Streptomyces", None)),
])
def test_split_organism_strain(label, expected):
    assert split_organism_strain(label) == expected


def test_the_splitter_never_drops_characters_it_does_not_return():
    """A split must be lossless: name + strain reconstructs the source string."""
    import csv
    rows = csv.DictReader((REPO_ROOT / "data" / "raw" / "mibig_producers.tsv")
                          .read_text(encoding="utf-8").splitlines(), delimiter="\t")
    for row in rows:
        label = row["taxon_label"]
        name, strain = split_organism_strain(label)
        rebuilt = f"{name} {strain}" if strain else name
        assert rebuilt == label or rebuilt == label.replace(" strain ", " "), label


# --------------------------------------------------------------------------
# Lane ownership, including the migration
# --------------------------------------------------------------------------

def test_ownership_recognizes_both_the_new_and_the_pre_94_shape():
    """Recognizing only the new shape would DUPLICATE all 217 on re-seed.

    A checkout written before #94 carries the marker in `note` and no `source`.
    If the predicate missed those, the merge would read them as curator-written,
    keep them, and append a structured copy beside each one.
    """
    assert is_phibase_sourced_resistance({"source": PHIBASE_RESISTANCE_SOURCE})
    assert is_phibase_sourced_resistance({"note": f"{PHIBASE_NOTE_MARKER} PHIG:1; ..."})
    assert not is_phibase_sourced_resistance({"note": "a curator wrote this"})
    assert not is_phibase_sourced_resistance({"source": "CARD"})


# --------------------------------------------------------------------------
# The activity queue asserts nothing
# --------------------------------------------------------------------------

def _queue_hint(definition):
    rows = activity_candidate_queue([{
        "identifier": "CHEBI:1", "label": "x", "definition": definition,
        "source_concepts": [{"source": "CHEBI"}],
    }])
    return rows[0]["hint"] if rows else None


def test_an_indication_is_never_offered_as_a_tested_organism():
    """"Used to treat tuberculosis" is a disease, not an assay subject."""
    hint = _queue_hint("A drug used to treat tuberculosis.")
    assert "INDICATION" in hint, hint


def test_a_group_is_offered_as_a_group_and_not_as_a_binomial():
    hint = _queue_hint("It is active against Gram-positive bacteria.")
    assert "Gram-positive" in hint and "activity stated" in hint, hint


def test_a_conjunction_is_never_offered_as_a_species_epithet():
    """"active against Staphylococci and Streptococci" once yielded
    "Staphylococci and" as a candidate species."""
    hint = _queue_hint("It is active against Staphylococci and Streptococci.")
    assert " and" not in hint.split("—")[0], hint


def test_a_record_that_already_has_activity_is_not_queued():
    rows = activity_candidate_queue([{
        "identifier": "CHEBI:1", "label": "x",
        "definition": "It is active against Escherichia coli.",
        "activity_spectrum": [{"taxon_label": "Escherichia coli",
                               "evidence": [{"reference": "PMID:1"}]}],
        "source_concepts": [{"source": "CHEBI"}],
    }])
    assert rows == []


# --------------------------------------------------------------------------
# The BUILDERS, not just the committed corpus
# --------------------------------------------------------------------------
#
# Every test above this line reads records off disk, and a record on disk does
# not change when code changes. Deleting the structured emission entirely leaves
# all of them green until someone re-seeds. These two run the extractor lanes in
# process, against the real committed inventories, so a regression in the code
# fails here on the same commit that introduces it.

def _seed_one(inchikey, identifier="CHEBI:X"):
    return {identifier: {"identifier": identifier, "label": "t",
                         "chemical_structure": {"standard_inchi_key": inchikey},
                         "curation_history": []}}


def _first_inventory_row(name):
    import csv
    return next(iter(csv.DictReader(
        (REPO_ROOT / "data" / "raw" / f"{name}.tsv").read_text(encoding="utf-8").splitlines(),
        delimiter="\t")))


def _first_accepted_mibig_row():
    import csv
    for row in csv.DictReader(
        (REPO_ROOT / "data" / "raw" / "mibig_producers.tsv").read_text(
            encoding="utf-8").splitlines(), delimiter="\t"):
        if row["reviewed"] == "true" and row["stereo_complete"] == "true":
            return row
    raise AssertionError("no MIBiG row passes the lane's own filters")


def test_the_phibase_lane_emits_structure_rather_than_prose():
    row = _first_inventory_row("phibase_amr")
    records = _seed_one(row["standard_inchi_key"], row["identifier"])
    attach_phibase_resistance(records)
    items = records[row["identifier"]]["resistance_mechanisms"]
    assert items, "the lane matched nothing; the fixture is wrong, not the code"
    item = items[0]
    assert item["source"] == PHIBASE_RESISTANCE_SOURCE
    assert item["taxon_label"] == row["taxon_label"]
    assert item["alteration"] == row["modification"]
    assert item["strain"] == row["strain_label"]
    assert item["protein_accession"] == f"UniProtKB:{row['protein_accession']}"
    # And the facts are NOT also in the note, which is the regression that
    # started #94: prose standing in for structure.
    assert row["taxon_label"] not in item["note"]
    assert row["strain_label"] not in item["note"]
    assert PHIBASE_NOTE_MARKER not in item["note"]


def test_the_mibig_lane_splits_the_strain_and_says_what_the_citation_supports():
    # The first row the lane would ACCEPT: it rejects unreviewed entries and
    # incomplete stereochemistry before it ever builds an item, so the first row
    # of the file is not necessarily one that reaches the code under test.
    row = _first_accepted_mibig_row()
    records = _seed_one(row["standard_inchi_key"])
    attach_mibig_producers(records, "4.0.1")
    items = records["CHEBI:X"].get("producer_organisms")
    assert items, "the lane matched nothing; the fixture is wrong, not the code"
    item = items[0]
    name, strain = split_organism_strain(row["taxon_label"])
    assert item["taxon_label"] == name
    assert item.get("strain") == strain
    assert "reference" not in item
    assert item["evidence"][0]["reference"] == row["primary_reference"]
    assert item["evidence"][0]["notes"], "a producer citation must say what it supports"


def test_no_producer_label_still_carries_a_collection_number():
    """Guards the split itself, not merely that `strain` is absent from it.

    Checking only "strain not in taxon_label" passes vacuously when the splitter
    stops splitting, because then there is no strain to find.
    """
    import re
    offenders = []
    for record in _records():
        for item in record.get("producer_organisms") or []:
            label = item["taxon_label"]
            if re.search(r"\d", label) or re.search(r"\b[A-Z]{3,}\b", label):
                offenders.append(f"{record['identifier']}: {label!r} looks strain-level")
    assert offenders == [], offenders


# --------------------------------------------------------------------------
# Findings from this PR's own review (#179-#185)
# --------------------------------------------------------------------------

def test_uniprot_accessions_use_one_notation_everywhere():  # #180
    """`ProteinExample` requires the prefix; `protein_accession` must match it."""
    offenders = []
    for record in _records():
        for item in record.get("resistance_mechanisms") or []:
            accession = item.get("protein_accession")
            if accession and not accession.startswith("UniProtKB:"):
                offenders.append(f"{record['identifier']}: {accession!r}")
    assert offenders == [], offenders[:10]


def test_a_malformed_protein_accession_is_refused():  # #180
    """A bare accession used to validate; so did 'see supplementary table 3'."""
    for bad in ("P9WHZ3", "see supplementary table 3", "UniProtKB:"):
        errors = _errors(resistance_mechanisms=[
            _mechanism(taxon_id="NCBITaxon:1773", taxon_label="M. tuberculosis",
                       protein_accession=bad)])
        assert any("protein_accession" in e or "does not match" in e
                   for e in errors), (bad, errors)


def test_every_curie_prefix_the_corpus_emits_is_declared():  # #183
    """PHIPO was emitted for all 217 associations and declared nowhere."""
    schema = yaml.safe_load((REPO_ROOT / "src" / "antibioticmech" / "schema"
                             / "antibioticmech.yaml").read_text(encoding="utf-8"))
    declared = set(schema.get("prefixes") or {})
    undeclared = set()
    for record in _records():
        for item in record.get("resistance_mechanisms") or []:
            for slot in ("taxon_id", "strain_taxon_id", "protein_accession",
                         "phenotype_id", "aro_id"):
                value = item.get(slot)
                if value and ":" in value:
                    prefix = value.split(":", 1)[0]
                    if prefix not in declared:
                        undeclared.add(f"{prefix} (in {slot})")
    assert undeclared == set(), sorted(undeclared)


def test_the_site_resolves_every_prefix_the_resistance_table_shows():  # #183
    from render_pages import XREF_URL_TEMPLATES
    for prefix in ("NCBITaxon", "PHIPO", "UniProtKB"):
        assert prefix in XREF_URL_TEMPLATES, prefix


def test_a_candidate_species_name_is_never_cut_in_half():  # #181
    """"Staphylococcus aureu" was offered to a curator seven times."""
    from curation_worklist import _tail_after
    # The guarantee is that the window never ENDS mid-token. A name still gets
    # cut off when it starts near the edge -- but then it fails to match as a
    # binomial and the row reports no subject, which is a true answer. What
    # must never happen is a partial token that still looks like a name.
    for width in range(1, 120):
        definition = "x" * 85 + " Staphylococcus aureus and others"
        tail = _tail_after(definition, 0, width)
        assert definition.startswith(tail)
        assert len(tail) == len(definition) or definition[len(tail)].isspace(), (
            width, repr(tail[-24:]))


def test_the_corpus_no_longer_offers_a_truncated_species_name():  # #181
    from curation_worklist import corpus_records
    offenders = [row for row in activity_candidate_queue(corpus_records())
                 if row["source_id"].endswith(("aureu", "aure"))]
    assert offenders == [], offenders


def test_no_activity_row_names_a_subject_while_claiming_none():  # #182
    """The claim column and the subject column must not contradict."""
    from curation_worklist import corpus_records
    for row in activity_candidate_queue(corpus_records()):
        if "no organism named" in row["hint"]:
            assert row["source_id"] == "(no subject named)", row


def test_activity_phrases_stay_in_strength_order():  # #182
    """First match wins, so the list order IS the precedence.

    Reordering `ACTIVITY_PHRASES` so that a weaker claim precedes a stronger one
    would silently file "broad-spectrum ... active against E. coli" as
    spectrum-only. Nothing else in the module would notice.
    """
    from curation_worklist import ACTIVITY_PHRASES
    strength = {"activity stated": 0, "SPECTRUM stated": 1}
    ranks = [strength.get(claim.split(" —")[0], 2) for _, _, claim in ACTIVITY_PHRASES]
    assert ranks == sorted(ranks), list(zip(ranks, [p[0] for p in ACTIVITY_PHRASES], strict=True))


def test_the_strongest_claim_in_a_definition_wins():  # #182
    """"Broad-spectrum ... active against X" is an activity claim, not a spectrum."""
    hint = _queue_hint("A broad-spectrum agent active against Escherichia coli.")
    assert "activity stated" in hint and "Escherichia coli" in hint, hint


def test_the_compounds_own_name_is_never_its_candidate_organism():  # #182
    """"Cefacetrile binds ..." was offered as a candidate binomial."""
    rows = activity_candidate_queue([{
        "identifier": "CHEBI:1", "label": "cefacetrile",
        # The compound name must fall AFTER the matched phrase, which is where
        # the real corpus row put it -- otherwise the tail never contains it and
        # the test passes without exercising the exclusion at all.
        "definition": "A broad-spectrum cephalosporin. Cefacetrile binds "
                      "penicillin-binding proteins.",
        "source_concepts": [{"source": "CHEBI"}],
    }])
    assert "Cefacetrile" not in rows[0]["source_id"], rows[0]


def test_each_taxon_curie_renders_beside_the_name_it_denotes():  # #179
    """The page printed "strain PH-1 NCBITaxon:5518", a SPECIES id."""
    from render_pages import build_record
    doc = {"identifier": "CHEBI:1", "label": "x", "antimicrobial_class": "ANTIBACTERIAL",
           "resistance_mechanisms": [{
               "mechanism_type": "UNKNOWN", "label": "a",
               "taxon_id": "NCBITaxon:5518", "taxon_label": "Fusarium graminearum",
               "strain": "PH-1", "strain_taxon_id": "NCBITaxon:229533",
               "protein_accession": "UniProtKB:I1S9X9", "phenotype_id": "PHIPO:0000632",
               "evidence": [{"reference": "PMID:1"}]}]}
    row = build_record(REPO_ROOT / "data/antibiotics/antibacterial/x.yaml",
                       doc, {}, "/")
    cell = row["resistance_groups"][0]["rows"][0]
    assert cell["taxon_id"]["id"] == "NCBITaxon:5518"
    assert cell["strain_taxon_id"]["id"] == "NCBITaxon:229533"
    # Both must be resolvable, or the split is invisible to a reader.
    assert cell["taxon_id"]["href"] and cell["strain_taxon_id"]["href"]
    assert cell["protein_accession"]["href"] and cell["phenotype_id"]["href"]
