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
                   protein_accession="P9WHZ3", phenotype_id="PHIPO:0000632",
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
    assert item["protein_accession"] == row["protein_accession"]
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
