"""Species corrections must not transfer reference identifiers across organisms."""

import copy
import csv
import json
import sys
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import phibase_grounding_reviews as review  # noqa: E402


@pytest.fixture
def inputs(tmp_path):
    inventory = ROOT / "data/raw/phibase_amr.tsv"
    rows = list(csv.DictReader(inventory.open(), delimiter="\t"))
    document = json.loads(review.DEFAULT_REVIEW.read_bytes())
    decision = next(d for d in document["reviews"]
                    if d["review_id"] == "xu-2019-hc30-subject-species-context")
    row = next(r for r in rows if r["pmid"] == "30732567" and r["strain_label"] == "HC30")
    path = tmp_path / "reviews.json"
    return inventory, rows, document, decision, row, path


def decisions(inputs):
    inventory, rows, document, _, _, path = inputs
    path.write_text(json.dumps(document))
    return review.load_reviews(inventory, rows, path)


def source_claim(row):
    return {
        "taxon_id": "NCBITaxon:" + row["taxon_id"], "taxon_label": row["taxon_label"],
        "strain": row["strain_label"], "protein_accession": "UniProtKB:" + row["protein_accession"],
        "strain_taxon_id": None, "gene_id": None,
        "note": "Source association.", "evidence": [],
    }


def test_subject_without_source_strain_taxid_is_supported(inputs):
    row = inputs[4]
    item = source_claim(row)
    assert review.apply_review(item, row, decisions(inputs))
    assert item["strain"] == "HC30M" and item["strain_taxon_id"] is None
    assert item["taxon_id"] == "NCBITaxon:948311"
    assert item["taxon_label"] == "Fusarium proliferatum"
    assert "protein_accession" not in item
    assert "Original source organism label: Fusarium fujikuroi." in item["note"]
    assert "Original source background label: HC30." in item["note"]
    assert "Rejected misassigned source identifiers: taxon_id=NCBITaxon:5127;" in item["note"]


@pytest.mark.parametrize("value", [
    None, True, [], {}, {"taxon_id": "948311"},
    {"taxon_id": "948311", "taxon_label": "Fusarium proliferatum", "rank": "species"},
    {"taxon_id": 948311, "taxon_label": "Fusarium proliferatum"},
    {"taxon_id": "NCBITaxon:948311", "taxon_label": "Fusarium proliferatum"},
    {"taxon_id": "0948311", "taxon_label": "Fusarium proliferatum"},
    {"taxon_id": "0", "taxon_label": "Fusarium proliferatum"},
    {"taxon_id": "948311", "taxon_label": ""},
    {"taxon_id": "948311", "taxon_label": " F. proliferatum"},
    {"taxon_id": "948311", "taxon_label": "Fusarium\nproliferatum"},
    {"taxon_id": "5127", "taxon_label": "Fusarium proliferatum"},
    {"taxon_id": "948311", "taxon_label": "Fusarium fujikuroi"},
])
def test_invalid_or_redundant_taxon_correction_fails_closed(inputs, value):
    inputs[3]["subject_taxon"] = value
    with pytest.raises(ValueError, match="subject taxon"):
        decisions(inputs)


@pytest.mark.parametrize("change", ["taxon_not_rejected", "protein_retained", "taxon_retained"])
def test_taxon_correction_requires_explicit_rejection(inputs, change):
    decision = inputs[3]
    if change == "taxon_not_rejected":
        decision["misassigned"].remove("taxon_id")
    elif change == "protein_retained":
        decision["withhold"].remove("protein_accession")
        decision["misassigned"].remove("protein_accession")
    else:
        decision["withhold"].remove("taxon_id")
        decision["misassigned"].remove("taxon_id")
    with pytest.raises(ValueError, match="subject taxon"):
        decisions(inputs)


@pytest.mark.parametrize("field,value", [
    ("taxon_label", "unexpected species"), ("strain", "unexpected subject"),
    ("strain_taxon_id", "NCBITaxon:123"), ("gene_id", "unexpected gene"),
    ("protein_accession", "UniProtKB:P00001"), ("taxon_id", "NCBITaxon:123"),
])
def test_apply_rejects_identity_drift_before_mutation(inputs, field, value):
    row = inputs[4]
    item = source_claim(row)
    item[field] = value
    before = copy.deepcopy(item)
    with pytest.raises(ValueError, match="differs from reviewed source"):
        review.apply_review(item, row, decisions(inputs))
    assert item == before


def test_species_review_cannot_keep_existing_source_gene_or_strain_id(inputs):
    _, rows, document, decision, _, path = inputs
    row = next(r for r in rows if r["pmid"] == "22314539" and r["gene_id"] and r["strain_taxon_id"])
    candidate = copy.deepcopy(decision)
    candidate["pmid"] = row["pmid"]
    candidate["subject_strain"] = "different tested subject"
    candidate["source_rows"] = [{"identifier": row["identifier"], "row_sha256": review.row_digest(row)}]
    candidate["withhold"].append("strain_taxon_id")
    document["reviews"] = [candidate]
    with pytest.raises(ValueError, match="subject taxon"):
        decisions(inputs)
    candidate["withhold"].append("gene_id")
    candidate["misassigned"].append("gene_id")
    assert review.row_digest(row) in decisions(inputs)


def test_curated_xu_subjects_do_not_inherit_reference_identifiers():
    record = load_record(ROOT / "data/antibiotics/antifungal/carbendazim.yaml")
    assert record["identifier"] == "CHEBI:3392"
    assert record["chemical_structure"]["standard_inchi_key"] == "TWFZGCMQGLPBSX-UHFFFAOYSA-N"
    assert len(record["resistance_mechanisms"]) == 19
    claims = [c for c in record["resistance_mechanisms"]
              if c["evidence"][0]["reference"] == "PMID:30732567"]
    assert len(claims) == 2
    expected = {
        "SJ51M": ("NCBITaxon:117187", "Fusarium verticillioides", "W7M0I3"),
        "HC30M": ("NCBITaxon:948311", "Fusarium proliferatum", "P53374"),
    }
    assert {c["strain"] for c in claims} == expected.keys()
    for claim in claims:
        taxon_id, label, reference = expected[claim["strain"]]
        assert claim["taxon_id"] == taxon_id and claim["taxon_label"] == label
        assert not any(claim.get(k) for k in ("protein_accession", "gene_id", "strain_taxon_id"))
        assert reference in claim["note"]
        assert "Original source background label: " + claim["strain"][:-1] + "." in claim["note"]
    assert not record.get("activity_spectrum")


def test_xu_dossier_is_metadata_only_and_keeps_reference_context():
    dossier = json.loads((ROOT / "research/2026-10-08-xu-subject-species-grounding.json").read_bytes())
    assert dossier["corpus_phi_scope"] == {
        "identifier_scoped": 176, "pending_associations": 41, "pending_papers": 19, "retained": 217,
    }
    assert dossier["changes"] == {
        "byte_identical_records": 2918, "changed_records": 21,
        "checksum_only_claims": 174, "new_scoped_claims": 2,
    }
    assert {key: value["organism"]["taxonId"] for key, value in dossier["proteins"].items()} == {
        "W7M0I3": 334819, "P53374": 5127, "A0A1L7VSA4": 1227346,
    }
    for protein in dossier["proteins"].values():
        assert "sequence" not in protein
    assert dossier["primary_request"]["sha256"] == (
        "21b5dc6a97cc32b652380a8dd1f57babbe32819342ce42ffaef0d1d480923d37")
    assert "No new variant, sequence, construct, protocol, numeric measurement or MIC was curated." in (
        dossier["limitations"])
