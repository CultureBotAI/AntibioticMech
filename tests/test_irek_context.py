"""Reference taxonomy and suggested queries cannot identify experimental alleles."""

import copy
import csv
import hashlib
import json
import sys
from pathlib import Path
from urllib.parse import urlencode

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_irek_context as audit  # noqa: E402


def taxon():
    return {"taxonId": 474186, "active": True, "rank": "strain",
            "scientificName": "Enterococcus faecalis (strain ATCC 47077 / OG1RF)",
            "parent": {"taxonId": 1351},
            "lineage": [{"rank": "species", "taxonId": 1351, "scientificName": "Enterococcus faecalis"}],
            "strains": [{"name": "ATCC 47077 / OG1RF", "synonyms": ["OG1RF"]}]}


@pytest.mark.parametrize("change", ["none", "taxon", "inactive", "rank", "species", "parent",
                                   "name", "alias", "og1_equivalence", "duplicate_species"])
def test_reference_taxon_boundaries(change):
    source = taxon()
    if change == "taxon":
        source["taxonId"] = 226185
    elif change == "inactive":
        source["active"] = False
    elif change == "rank":
        source["rank"] = "species"
    elif change == "species":
        source["lineage"][0]["taxonId"] = 1352
    elif change == "parent":
        source["parent"]["taxonId"] = 1352
    elif change == "name":
        source["scientificName"] = "Enterococcus faecalis OG1"
    elif change == "alias":
        source["strains"][0]["synonyms"] = []
    elif change == "og1_equivalence":
        source["strains"][0]["synonyms"].append("OG1")
    elif change == "duplicate_species":
        source["lineage"].append(copy.deepcopy(source["lineage"][0]))
    if change != "none":
        with pytest.raises(ValueError):
            audit.project_taxon(source)
        return
    projected = audit.project_taxon(source)
    assert projected["taxon_id"] == "NCBITaxon:474186"
    assert projected["species_lineage"]["taxon_id"] == "NCBITaxon:1351"
    assert not projected["experimental_subject_assignment"]
    assert not projected["source_og1_equated_to_og1rf"]
    assert projected["strain_annotations"][0]["name"] == "ATCC 47077 / OG1RF"


@pytest.mark.parametrize("change", ["none", "query", "fields", "hash", "bytes", "retry", "release",
                                   "pagination", "count", "results", "suggestions"])
def test_exact_empty_query_does_not_promote_suggested_hits(tmp_path, change):
    body = {"results": [], "suggestions": [{"query": "DIFFERENT_GENE_AND_TAXON", "hits": 999}]}
    params = {"query": audit.QUERIES["reference"], "fields": audit.FIELDS,
              "format": "json", "size": "50"}
    if change == "query":
        params["query"] = "DIFFERENT_GENE_AND_TAXON"
    elif change == "fields":
        params["fields"] += ",sequence"
    elif change == "results":
        body["results"] = [{"primaryAccession": "P12345"}]
    elif change == "suggestions":
        body["suggestions"] = "not a list"
    payload = json.dumps(body).encode()
    receipt = {"url": "https://rest.uniprot.org/uniprotkb/search?" + urlencode(params),
               "status": 200, "sha256": hashlib.sha256(payload).hexdigest(), "bytes": len(payload),
               "retry_performed": False, "retrieved_at": "synthetic",
               "headers": {"x-uniprot-release": "2026_03", "x-total-results": str(len(body["results"]))}}
    if change == "hash":
        receipt["sha256"] = "0" * 64
    elif change == "bytes":
        receipt["bytes"] += 1
    elif change == "retry":
        receipt["retry_performed"] = True
    elif change == "release":
        receipt["headers"]["x-uniprot-release"] = "OTHER"
    elif change == "pagination":
        receipt["headers"]["link"] = "next"
    elif change == "count":
        receipt["headers"]["x-total-results"] = "999"
    (tmp_path / "reference-response.bin").write_bytes(payload)
    (tmp_path / "reference-receipt.json").write_text(json.dumps(receipt))
    if change != "none":
        with pytest.raises(ValueError):
            audit.read_empty_query(tmp_path, tmp_path, "reference")
        return
    result = audit.read_empty_query(tmp_path, tmp_path, "reference")
    assert result["result_count"] == 0 and result["suggested_queries_excluded"] == 1
    assert "DIFFERENT_GENE_AND_TAXON" not in json.dumps(result)
    assert not result["suggestions_used_as_results"] and not result["protein_absence_inferred"]


@pytest.mark.parametrize("key", ["paper2021", "paper2023"])
@pytest.mark.parametrize("change", ["none", "url", "attempt", "retry", "status", "body"])
def test_transport_and_http_holds_remain_distinct(tmp_path, key, change):
    url = audit.SOURCES[key]["url"]
    attempt = {"url": url, "started_at": "synthetic"}
    receipt = {"url": url, "retry_performed": False}
    if key == "paper2021":
        receipt["error_type"] = "ConnectionError"
    else:
        body = b"Access hold."
        (tmp_path / f"{key}-response.bin").write_bytes(body)
        receipt.update(status=403, sha256=hashlib.sha256(body).hexdigest(), bytes=len(body))
    if change == "url":
        receipt["url"] = "https://example.org"
    elif change == "attempt":
        attempt["url"] = "https://example.org"
    elif change == "retry":
        receipt["retry_performed"] = True
    elif change == "status":
        receipt["status"] = 200
    elif change == "body":
        (tmp_path / f"{key}-response.bin").write_bytes(b"Not the recorded response.")
    (tmp_path / f"{key}-attempt.json").write_text(json.dumps(attempt))
    (tmp_path / f"{key}-receipt.json").write_text(json.dumps(receipt))
    if change != "none":
        with pytest.raises(ValueError):
            audit.primary_hold(tmp_path, tmp_path, key)
        return
    result = audit.primary_hold(tmp_path, tmp_path, key)
    assert result["http_status"] == (None if key == "paper2021" else 403)
    assert not result["full_text_reviewed"] and not result["global_unavailability_inferred"]
    assert not result["alternate_route_attempted"]


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_historical_scope_without_freezing_live_corpus(dossier, monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    census = audit.reference.check_pin(ROOT, dossier["inputs"]["census"])
    rows = list(csv.DictReader(census.read_text().splitlines(), delimiter="\t"))
    assert len(rows) == 2939
    row, = [r for r in rows if r["identifier"] == "CHEBI:29007"]
    assert dossier["record"]["sha256"] == row["record_sha256"]
    assert dossier["record"]["standard_inchi_key"] == row["standard_inchi_key"]
    assert dossier["record"]["source_assertions"] == 23
    assert dossier["record"]["whole_record_review"] == "OPEN"
    assert not dossier["record"]["source_route_newly_confirmed"]


def test_three_strain_labels_and_primary_gaps_are_not_collapsed(dossier):
    protein = dossier["reused_reference_protein"]
    assert protein["accession"] == "UniProtKB:Q820A8"
    assert protein["reference_taxon_id"] == "NCBITaxon:226185"
    assert protein["entry_version"] == 142 and protein["sequence_version"] == 1
    focal, = [c for c in dossier["focal_citation_contexts"] if "PMID:34672600" in c["citation_identifiers"]]
    assert [a["value"] for a in focal["strain_annotations"]] == ["OG1"]
    assert not focal["experimental_subject_assignment"]
    assert dossier["separate_og1rf_reference_taxonomy"]["taxon_id"] == "NCBITaxon:474186"
    assert not dossier["separate_og1rf_reference_taxonomy"]["experimental_subject_assignment"]
    assert {q["result_count"] for q in dossier["queries"].values()} == {0}
    assert dossier["summary"]["suggested_queries_excluded"] == 6
    assert dossier["summary"]["new_primary_results_reviewed"] == 0
    assert dossier["summary"]["biological_records_changed"] == 0
    assert dossier["summary"]["full_corpus_goal_status"] == "OPEN"
    assert dossier["constraints"]["ncbi_requests"] == dossier["constraints"]["github_mutations"] == 0
    assert dossier["constraints"]["issue_1040"] == "DEFERRED"
