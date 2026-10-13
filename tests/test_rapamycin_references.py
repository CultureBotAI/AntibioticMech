"""An accessible reference annotation must not erase an inaccessible primary paper."""

import copy
import csv
import hashlib
import io
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_rapamycin_references as audit  # noqa: E402


@pytest.fixture
def dossier():
    return json.loads((ROOT / audit.DEFAULT_OUTPUT).read_bytes())


def test_historical_record_scope_without_reading_current_records(dossier, monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    rows = list(csv.DictReader(io.StringIO(
        audit.reference.check_pin(ROOT, dossier["inputs"]["census"]).read_text()), delimiter="\t"))
    assert len(rows) == 2939
    assert {r["identifier"] for r in dossier["records"]} == set(audit.TARGETS)
    for record in dossier["records"]:
        row, = [r for r in rows if r["identifier"] == record["identifier"]]
        assert record["sha256"] == row["record_sha256"] and record["path"] == row["path"]
        assert record["standard_inchi_key"] == audit.TARGETS[record["identifier"]]
        assert record["whole_record_review"] == "OPEN" and record["assertions_added"] == 0
        assert record["complete_collection_aware_record_loaded"]
        assert not record["tested_preparation_independently_reidentified"]


def test_checkpoint_load_uses_historical_bytes_not_live_record(dossier, tmp_path, monkeypatch):
    item, = [r for r in dossier["records"] if r["identifier"] == "CHEBI:9168"]
    original_item = copy.deepcopy(item)
    fixture = tmp_path / audit.SIROLIMUS_FIXTURE
    fixture.parent.mkdir(parents=True)
    fixture.write_bytes((ROOT / audit.SIROLIMUS_FIXTURE).read_bytes())
    live = tmp_path / item["path"]
    live.parent.mkdir(parents=True)
    live.write_text("Not the historical record.\n")
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert path != live
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    record = audit.load_checkpoint_record(tmp_path, item)
    assert record["identifier"] == item["identifier"]
    assert not record.get("resistance_mechanisms")
    assert item == original_item


@pytest.mark.parametrize("change", ["hash", "fixture", "path", "identity", "structure", "missing"])
def test_historical_record_binding_rejects_tampering(dossier, tmp_path, change):
    item = copy.deepcopy(next(r for r in dossier["records"] if r["identifier"] == "CHEBI:9168"))
    fixture = tmp_path / audit.SIROLIMUS_FIXTURE
    fixture.parent.mkdir(parents=True)
    payload = (ROOT / audit.SIROLIMUS_FIXTURE).read_bytes()
    if change == "fixture":
        payload += b"\n"
    elif change == "identity":
        payload = payload.replace(b"identifier: CHEBI:9168", b"identifier: CHEBI:68478")
        item["sha256"] = hashlib.sha256(payload).hexdigest()
    elif change == "structure":
        payload = payload.replace(audit.TARGETS["CHEBI:9168"].encode(), audit.TARGETS["CHEBI:68478"].encode())
        item["sha256"] = hashlib.sha256(payload).hexdigest()
    elif change == "hash":
        item["sha256"] = "0" * 64
    elif change == "path":
        item["path"] = "data/antibiotics/antibacterial/other.yaml"
    if change != "missing":
        fixture.write_bytes(payload)
    with pytest.raises((ValueError, FileNotFoundError)):
        audit.load_checkpoint_record(tmp_path, item)


@pytest.mark.parametrize("key,accession,version,sequence_version,locus,sgd", [
    ("tor1", "P35169", 229, 3, "YJR066W", "S000003827"),
    ("fpr1", "P20081", 220, 2, "YNL135C", "S000005079"),
])
def test_reference_versions_and_taxonomy(dossier, key, accession, version, sequence_version, locus, sgd):
    protein = dossier["reference_proteins"][key]
    assert protein["protein_accession"] == "UniProtKB:" + accession
    assert protein["entry_version"] == version and protein["sequence_version"] == sequence_version
    assert protein["ordered_locus_names"] == [locus] and protein["sgd_id"] == sgd
    assert protein["reference_taxon_id"] == "NCBITaxon:559292"
    assert protein["reference_taxon_rank"] == "strain"
    assert protein["source_species_taxon_id"] == "NCBITaxon:4932"
    assert protein["species_lineage_verified"] and not protein["exact_resistance_allele"]
    assert not protein["experimental_subject_assignment"] and not protein["focal_paper_in_bibliography"]
    assert not protein["bibliography_primary_results_reviewed"]
    assert dossier["uniprot_requests"][key]["release"] == "2026_03"
    assert dossier["uniprot_requests"][key]["reused"] == (key == "fpr1")


@pytest.fixture
def protein_fixture(dossier):
    p = dossier["reference_proteins"]["tor1"]
    entry = {"entryType": p["entry_type"], "primaryAccession": "P35169",
             "entryAudit": {"entryVersion": 229, "sequenceVersion": 3},
             "organism": {"taxonId": 559292, "scientificName": p["reference_organism_name"]},
             "proteinDescription": {"recommendedName": {"fullName": {"value": p["protein_name"]}}},
             "genes": [{"geneName": {"value": "TOR1"}, "synonyms": [{"value": "DRR1"}],
                        "orderedLocusNames": [{"value": "YJR066W"}], "orfNames": [{"value": "J1803"}]}],
             "uniProtKBCrossReferences": [{"database": "SGD", "id": "S000003827",
                                          "properties": [{"key": "GeneName", "value": "TOR1"}]}]}
    tax = {"taxonId": 559292, "rank": "strain", "active": True,
           "scientificName": p["reference_organism_name"], "lineage": [{"taxonId": 4932, "rank": "species"}]}
    return entry, tax


@pytest.mark.parametrize("change", ["none", "species", "strain", "inactive", "rank", "name",
                                      "reviewed", "sequence", "features", "version", "sgd", "duplicate_gene"])
def test_projection_boundaries(protein_fixture, change):
    entry, tax = copy.deepcopy(protein_fixture)
    if change == "species":
        tax["lineage"][0]["taxonId"] = 5476
    elif change == "strain":
        entry["organism"]["taxonId"] = tax["taxonId"] = 123
    elif change == "inactive":
        tax["active"] = False
    elif change == "rank":
        tax["rank"] = "subspecies"
    elif change == "name":
        entry["genes"][0]["geneName"]["value"] = "TOR2"
    elif change == "reviewed":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif change in {"sequence", "features"}:
        entry[change] = "NOT_FOR_EXPORT"
    elif change == "version":
        entry["entryAudit"]["sequenceVersion"] = True
    elif change == "sgd":
        entry["uniProtKBCrossReferences"][0]["properties"][0]["value"] = "TOR2"
    elif change == "duplicate_gene":
        entry["genes"].append(copy.deepcopy(entry["genes"][0]))
    if change != "none":
        with pytest.raises(ValueError):
            audit.project_protein(entry, "TOR1", tax)
        return
    result = audit.project_protein(entry, "TOR1", tax)
    assert result["gene_names"] == ["DRR1", "TOR1"]
    assert not result["exact_resistance_allele"] and not result["experimental_subject_assignment"]


def test_focal_bibliography_is_not_primary_review(protein_fixture):
    entry, tax = protein_fixture
    entry["references"] = [{"citation": {
        "citationCrossReferences": [{"database": "PubMed", "id": audit.PMID}]}}]
    result = audit.project_protein(entry, "TOR1", tax)
    assert result["focal_paper_in_bibliography"]
    assert not result["bibliography_primary_results_reviewed"]


@pytest.mark.parametrize("change", ["none", "url", "attempt", "status", "body", "bytes", "hash",
                                      "retry", "host", "scheme", "path", "fragment", "no_query"])
def test_publisher_hold_provenance(tmp_path, change):
    body = b"unexpected article" if change == "body" else b""
    (tmp_path / "article-response.bin").write_bytes(body)
    attempt = {"url": "https://example.org" if change == "attempt" else audit.URL}
    receipt = {"url": audit.URL, "status": 303, "bytes": len(body), "retry_performed": False,
               "sha256": hashlib.sha256(body).hexdigest(), "retrieved_at": "synthetic",
               "headers": {"Location": "https://idp.springer.com/authorize?token=DO_NOT_EXPORT"}}
    if change == "url":
        receipt["url"] = "https://example.org"
    elif change in {"status", "bytes", "hash", "retry"}:
        key, value = {"status": ("status", 200), "bytes": ("bytes", 1),
                      "hash": ("sha256", "0" * 64), "retry": ("retry_performed", True)}[change]
        receipt[key] = value
    elif change in {"host", "scheme", "path", "fragment", "no_query"}:
        receipt["headers"]["Location"] = {
            "host": "https://elsewhere.org/authorize?token=x", "scheme": "http://idp.springer.com/authorize?token=x",
            "path": "https://idp.springer.com/pdf?token=x", "fragment": "https://idp.springer.com/authorize?token=x#x",
            "no_query": "https://idp.springer.com/authorize"}[change]
    (tmp_path / "article-attempt.json").write_text(json.dumps(attempt))
    (tmp_path / "article-receipt.json").write_text(json.dumps(receipt))
    if change != "none":
        with pytest.raises(ValueError):
            audit.read_hold(tmp_path, tmp_path)
        return
    hold = audit.read_hold(tmp_path, tmp_path)
    assert hold["status"] == "AUTHORIZATION_REDIRECT_NOT_FOLLOWED"
    assert not hold["primary_results_reviewed"] and not hold["full_text_received"]
    assert "DO_NOT_EXPORT" not in json.dumps(hold)


def test_saved_hold_and_goal_remain_open(dossier):
    assert dossier["curation_decision"] == "HOLD_PRIMARY_EXPERIMENTAL_EVIDENCE_NOT_VERIFIED"
    assert dossier["summary"]["full_corpus_goal_status"] == "OPEN"
    assert dossier["summary"]["verified_primary_phenotypes"] == 0
    assert dossier["summary"]["whole_record_reviews_completed"] == 0
    assert dossier["constraints"]["issue_1040"] == "DEFERRED"
    assert dossier["constraints"]["ncbi_requests"] == 0
    assert dossier["constraints"]["github_mutations"] == 0
    assert not dossier["primary"]["discovery_snippets_are_primary_evidence"]
    assert not dossier["primary"]["global_unavailability_inferred"]
