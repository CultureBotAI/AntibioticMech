"""A parent cohort must not become a tested strain or a reference-protein allele."""

import copy
import csv
import hashlib
import json
import sys
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import phibase_grounding_reviews as reviews  # noqa: E402
import seed_from_sources as seed  # noqa: E402


@pytest.fixture
def review_case(tmp_path):
    rows = list(csv.DictReader((ROOT / "data/raw/phibase_amr.tsv").open(), delimiter="\t"))
    row = next(r for r in rows if r["pmid"] == "34490974")
    decision = next(d for d in json.loads(reviews.DEFAULT_REVIEW.read_bytes())["reviews"]
                    if d["pmid"] == "34490974")
    return tmp_path, copy.deepcopy(row), copy.deepcopy(decision)


def load_case(case):
    directory, row, decision = case
    inventory = directory / "inventory.tsv"
    with inventory.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(row), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerow(row)
    decision["source_rows"] = [{"identifier": row["identifier"], "row_sha256": reviews.row_digest(row)}]
    document = {"schema_version": 1,
                "source_inventory_sha256": hashlib.sha256(inventory.read_bytes()).hexdigest(),
                "reviews": [decision]}
    path = directory / "review.json"
    path.write_text(json.dumps(document))
    return reviews.load_reviews(inventory, [row], path)


def claim(row):
    return {"mechanism_type": "UNKNOWN", "strain": row["strain_label"],
            "protein_accession": "UniProtKB:" + row["protein_accession"],
            "taxon_id": "NCBITaxon:" + row["taxon_id"], "taxon_label": row["taxon_label"],
            "alteration": row["modification"], "phenotype_id": row["phenotype_id"],
            "phenotype_label": row["phenotype_label"], "assay": row["evidence_code"],
            "note": "Source claim.", "evidence": [{"reference": "PMID:" + row["pmid"]}]}


@pytest.mark.parametrize("value", [False, None, 0, 1, "true", [], {}])
def test_background_withholding_requires_explicit_boolean_true(review_case, value):
    review_case[2]["withhold_strain"] = value
    with pytest.raises(ValueError, match="background-only strain"):
        load_case(review_case)


def test_background_withholding_cannot_also_replace_subject(review_case):
    review_case[2]["subject_strain"] = "invented derivative"
    with pytest.raises(ValueError, match="background-only strain"):
        load_case(review_case)


@pytest.mark.parametrize("label", ["", "  "])
def test_background_withholding_requires_source_label(review_case, label):
    review_case[1]["strain_label"] = label
    with pytest.raises(ValueError, match="background-only strain"):
        load_case(review_case)


def test_background_withholding_cannot_leave_parent_taxid(review_case):
    review_case[1]["strain_taxon_id"] = "123"
    with pytest.raises(ValueError, match="source strain identifier"):
        load_case(review_case)


def test_background_taxid_is_withheld_when_explicitly_reviewed(review_case):
    _, row, decision = review_case
    row["strain_taxon_id"] = "123"
    decision["withhold"].append("strain_taxon_id")
    loaded = load_case(review_case)
    item = claim(row)
    item["strain_taxon_id"] = "NCBITaxon:123"
    reviews.apply_review(item, row, loaded)
    assert "strain" not in item and "strain_taxon_id" not in item
    assert "strain_taxon_id=NCBITaxon:123" in item["note"]


@pytest.mark.parametrize("change", ["label", "missing_label", "unexpected_id", "protein"])
def test_seeded_subject_drift_fails_without_partial_mutation(review_case, change):
    loaded = load_case(review_case)
    row = review_case[1]
    item = claim(row)
    if change == "label":
        item["strain"] = "different"
    elif change == "missing_label":
        del item["strain"]
    elif change == "unexpected_id":
        item["strain_taxon_id"] = "NCBITaxon:123"
    else:
        item["protein_accession"] = "UniProtKB:OTHER"
    before = copy.deepcopy(item)
    with pytest.raises(ValueError, match="seeded"):
        reviews.apply_review(item, row, loaded)
    assert item == before


def test_background_label_moves_to_provenance_without_other_biological_changes(review_case):
    row = review_case[1]
    source_before = copy.deepcopy(row)
    item = claim(row)
    before = copy.deepcopy(item)
    assert reviews.apply_review(item, row, load_case(review_case))
    assert row == source_before
    assert set(before) - set(item) == {"strain", "protein_accession"}
    excluded = {"strain", "protein_accession", "note", "evidence"}
    assert {k: v for k, v in before.items() if k not in excluded} == {
        k: v for k, v in item.items() if k not in {"note", "evidence"}}
    assert f"Original source background label: {row['strain_label']}." in item["note"]
    assert "Reference-only source identifiers: protein_accession=UniProtKB:Q6X9S4." in item["note"]
    assert item["evidence"][:-1] == before["evidence"]


def test_fouche_source_rows_remain_distinct_and_reproduce_the_record():
    rows = list(csv.DictReader((ROOT / "data/raw/phibase_amr.tsv").open(), delimiter="\t"))
    fixture = {r["identifier"]: {"identifier": r["identifier"], "chemical_structure": {
        "standard_inchi_key": r["standard_inchi_key"]}, "curation_history": []} for r in rows}
    counts = seed.attach_phibase_resistance(fixture)
    assert counts["reviewed_identifier_context"] == 185 and counts["matched_associations"] == 217
    record = load_record(ROOT / "data/antibiotics/antifungal/fenpicoxamid.yaml")
    assert record["chemical_structure"]["standard_inchi_key"] == "QGTOTYJSCYHYFK-RBODFLQRSA-N"
    claims = record["resistance_mechanisms"]
    assert len(claims) == 2 and fixture[record["identifier"]]["resistance_mechanisms"] == claims
    source = [r for r in rows if r["pmid"] == "34490974"]
    assert {r["strain_label"] for r in source} == {"IPO323", "37-16"}
    for row, item in zip(source, claims, strict=True):
        assert not {"strain", "strain_taxon_id", "protein_accession", "gene_id"} & set(item)
        assert item["taxon_id"] == "NCBITaxon:" + row["taxon_id"] == "NCBITaxon:1047171"
        assert item["alteration"] == row["modification"]
        assert item["phenotype_id"] == row["phenotype_id"]
        assert item["phenotype_label"] == row["phenotype_label"] and item["assay"] == row["evidence_code"]
        assert f"Original source background label: {row['strain_label']}." in item["note"]
        assert "ST1/MBC" in item["note"]
        assert item["evidence"][0]["reference"] == "PMID:34490974"
        assert item["evidence"][-1]["reference"] == "DOI:10.1111/1462-2920.15760"
    assert claims[0] != claims[1]
    assert record.get("activity_spectrum", []) == []


def test_dossier_keeps_reference_and_experimental_scope_separate():
    dossier = json.loads((ROOT / "research/2026-10-09-fouche-subject-reference-grounding.json").read_bytes())
    assert dossier["corpus_phi_scope"] == {
        "identifier_scoped": 184, "pending_associations": 33, "pending_papers": 14, "retained": 217,
    }
    assert dossier["changes"] == {
        "new_scoped_claims": 2, "checksum_only_claims": 182,
        "changed_records": 22, "byte_identical_records": 2917,
    }
    assert dossier["primary_access"]["pdf"]["sha256"] == (
        "d4961ed7bd42064881e7460785f73a06815f1e4877eb88d030567457c3c2a131")
    assert dossier["primary_access"]["version"] == "ACCEPTED_MANUSCRIPT_NOT_VERSION_OF_RECORD"
    assert dossier["subject_context"]["source_background_labels"] == ["IPO323", "37-16"]
    assert dossier["subject_context"]["individual_subject_mapping"] == "UNRESOLVED"
    assert dossier["subject_context"]["experimental_accessions_assigned"] is False
    assert dossier["protein"]["primaryAccession"] == "Q6X9S4"
    assert dossier["protein"]["entryAudit"]["entryVersion"] == 84
    assert dossier["protein"]["reference_strain"] == "ST1/MBC"
    assert dossier["taxonomy"]["taxonId"] == 1047171
    assert dossier["taxonomy"]["rank"] == "species" and dossier["taxonomy"]["active"] is True
    assert not {"sequence", "features", "variants"} & set(dossier["protein"])
