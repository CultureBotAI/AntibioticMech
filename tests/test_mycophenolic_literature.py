"""Keep access metadata and canonical references below the primary-evidence gate."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_mycophenolic_literature as audit  # noqa: E402


def metadata(year):
    pmid, doi = audit.STUDIES[year]
    return {"hitCount": 1, "resultList": {"result": [{
        "id": pmid, "source": "MED", "doi": doi, "title": "TEST TITLE", "authorString": "TEST AUTHORS",
        "isOpenAccess": "N", "abstractText": "NOT EXPORTED",
        "fullTextUrlList": {"fullTextUrl": [{
            "url": "https://onlinelibrary.wiley.com/doi/pdfdirect/" + doi,
            "documentStyle": "pdf", "site": "Unpaywall", "availability": "Free", "availabilityCode": "F",
        }]},
    }]}}


@pytest.mark.parametrize("year", audit.STUDIES)
@pytest.mark.parametrize("change", [
    "none", "duplicate", "count", "boolean", "id", "doi", "source", "url", "duplicate_link",
])
def test_metadata_identity_and_access_boundary(year, change):
    data = metadata(year)
    row = data["resultList"]["result"][0]
    if change == "duplicate":
        data["resultList"]["result"].append(copy.deepcopy(row))
    elif change == "count":
        data["hitCount"] = 2
    elif change == "boolean":
        data["hitCount"] = True
    elif change in {"id", "doi", "source"}:
        row[change] = "WRONG"
    elif change == "url":
        row["fullTextUrlList"]["fullTextUrl"][0]["url"] = "https://example.org/alternate"
    elif change == "duplicate_link":
        row["fullTextUrlList"]["fullTextUrl"] *= 2
    if change != "none":
        with pytest.raises(ValueError):
            audit.project_metadata(data, year)
        return
    result = audit.project_metadata(data, year)
    assert result["primary_results_reviewed"] is False
    assert result["reuse_permission_inferred"] is False
    assert result["phenotype_or_causality_inferred"] is False
    assert "NOT EXPORTED" not in json.dumps(result)


def protein():
    name = "Saccharomyces cerevisiae (strain ATCC 204508 / S288c)"
    return {
        "entryType": "UniProtKB reviewed (Swiss-Prot)", "primaryAccession": "P54000",
        "entryAudit": {"entryVersion": 190, "sequenceVersion": 1},
        "genes": [{"geneName": {"value": "SUB1"}, "synonyms": [{"value": "TSP1"}],
                   "orderedLocusNames": [{"value": "YMR039C"}]}],
        "organism": {"taxonId": 559292, "scientificName": name},
        "proteinDescription": {"recommendedName": {"fullName": {"value": "TEST REFERENCE"}}},
        "uniProtKBCrossReferences": [{"database": "SGD", "id": "S000004642"}],
    }, {
        "taxonId": 559292, "rank": "strain", "scientificName": name, "active": True,
        "lineage": [{"taxonId": 4932, "scientificName": "Saccharomyces cerevisiae", "rank": "species"}],
    }


@pytest.mark.parametrize("change", [
    "none", "accession", "gene", "alias", "locus", "sgd", "version", "bool_version", "duplicate_gene",
    "taxon", "species", "species_name", "missing_species_name", "empty_species_name", "rank", "inactive",
    "name", "both_names_empty", "sequence", "features", "comments",
])
def test_sub1_reference_is_not_an_experimental_assignment(change):
    entry, taxonomy = protein()
    if change == "accession":
        entry["primaryAccession"] = "OTHER"
    elif change == "gene":
        entry["genes"][0]["geneName"]["value"] = "OTHER"
    elif change == "alias":
        entry["genes"][0].pop("synonyms")
    elif change == "locus":
        entry["genes"][0]["orderedLocusNames"][0]["value"] = "OTHER"
    elif change == "sgd":
        entry["uniProtKBCrossReferences"][0]["id"] = "OTHER"
    elif change == "version":
        entry["entryAudit"]["entryVersion"] += 1
    elif change == "bool_version":
        entry["entryAudit"]["sequenceVersion"] = True
    elif change == "duplicate_gene":
        entry["genes"] *= 2
    elif change == "taxon":
        entry["organism"]["taxonId"] = 4932
    elif change == "species":
        taxonomy["lineage"][0]["taxonId"] = 4896
    elif change in {"species_name", "empty_species_name"}:
        taxonomy["lineage"][0]["scientificName"] = "" if change == "empty_species_name" else "OTHER"
    elif change == "missing_species_name":
        taxonomy["lineage"][0].pop("scientificName")
    elif change == "rank":
        taxonomy["rank"] = "species"
    elif change == "inactive":
        taxonomy["active"] = False
    elif change == "name":
        taxonomy["scientificName"] = "OTHER"
    elif change == "both_names_empty":
        entry["organism"]["scientificName"] = taxonomy["scientificName"] = ""
    elif change in {"sequence", "features", "comments"}:
        entry[change] = "NOT EXPORTED"
    if change != "none":
        with pytest.raises(ValueError):
            audit.project_sub1(entry, taxonomy)
        return
    result = audit.project_sub1(entry, taxonomy)
    assert result["experimental_subject_assignment"] is False
    assert result["exact_resistance_allele"] is False
    assert result["resistance_asserted_from_reference"] is False
    assert result["selected_2008_paper_in_uniprot_bibliography"] is False


def test_bibliographic_link_would_still_not_establish_phenotype():
    entry, taxonomy = protein()
    entry["references"] = [{"citation": {
        "citationCrossReferences": [{"database": "PubMed", "id": "18823333"}],
    }}]
    result = audit.project_sub1(entry, taxonomy)
    assert result["selected_2008_paper_in_uniprot_bibliography"] is True
    assert result["resistance_asserted_from_reference"] is False
    assert result["experimental_subject_assignment"] is False


def test_checkpoint_distinguishes_denial_from_unrequested_primary():
    data = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert data["studies"]["2005"]["primary_status"] == "PUBLISHER_403_HELD_NO_RETRY"
    assert data["studies"]["2008"]["primary_status"] == "NOT_REQUESTED_AFTER_PUBLISHER_CANARY_DENIAL"
    assert data["sources"]["primary-2005"]["status"] == 403
    assert data["reference"]["protein_accession"] == "UniProtKB:P54000"
    assert data["reference"]["reference_taxon_id"] == "NCBITaxon:559292"
    assert data["reference"]["source_species_taxon_id"] == "NCBITaxon:4932"
    assert data["summary"]["corpus_records_in_scope"] == 2939
    assert data["summary"]["curated_resistance_assertions"] == 0
    assert data["summary"]["new_primary_results_reviewed"] == 0
    assert data["limits"]["ncbi_requests"] == 0
    assert data["limits"]["issue_1040"] == "DEFERRED"
    assert data["limits"]["whole_record_primary_review"] == "OPEN"


def test_native_offline_replay(monkeypatch):
    directory = ROOT / audit.CACHE
    if not (directory / "sub1-reference-response.bin").exists():
        pytest.skip("optional native research cache not present")

    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted networking")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    real_loader = audit.load_record

    def baseline_only(path):
        assert path == directory / "baseline-record.yaml"
        return real_loader(path)

    monkeypatch.setattr(audit, "load_record", baseline_only)
    result = audit.build(ROOT, directory)
    payload = (json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    assert payload == (ROOT / audit.OUTPUT).read_bytes()
