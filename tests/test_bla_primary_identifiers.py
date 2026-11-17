"""Adversarial checks for paper identifiers and non-equivalent taxon names."""

import copy
import hashlib
import json
import socket
import sys
from pathlib import Path
from urllib.parse import urlencode

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_bla_primary_identifiers as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline identifier audit attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)


@pytest.fixture
def checkpoint():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_public_checkpoint_preserves_all_memberships(checkpoint):
    assert checkpoint["summary"] == {
        "complete_target_records_read": 12,
        "current_record_hashes_verified": 2939,
        "source_claims_bound": 18,
        "terms_investigated": 3,
        "species_names_grounded": 3,
        "distinct_native_taxonomy_nodes": 4,
        "new_selected_proteins": 0,
        "whole_record_primary_signoffs": 0,
    }
    index = audit.read_json(ROOT, checkpoint["inputs"]["current_index"])
    definitions = audit.read_json(ROOT, checkpoint["inputs"]["definition_citations"])
    assert len(checkpoint["records"]) == 12
    assert len(checkpoint["claims"]) == 18
    for term, row in checkpoint["terms"].items():
        assert row["record_memberships"] == index["terms"][term]["record_memberships"]
        assert (
            sorted(c["record_identifier"] for c in checkpoint["claims"] if c["aro_id"] == term)
            == row["record_memberships"]
        )
        assert definitions["terms"][term]["definition_citation_ids"] == ["PMID:" + row["paper"]["pmid"]]
        assert row["reference_accessions"] == []
        assert row["experimental_allele_assignment"] is None
        assert row["experimental_protein_assignment"] is None
        assert row["experimental_genome_assignment"] is None
        assert row["whole_record_primary_review"] == "OPEN"
    assert checkpoint["constraints"]["ncbi_requests"] == 0
    assert checkpoint["constraints"]["issue_1040"] == "DEFERRED"
    assert checkpoint["constraints"]["full_investigation_complete"] is False


def test_taxon_name_mapping_is_not_a_strain_join(checkpoint):
    expected = {
        "ARO:3007437": "NCBITaxon:1628248",
        "ARO:3007085": "NCBITaxon:2906062",
        "ARO:3007648": "NCBITaxon:92488",
    }
    for term, row in checkpoint["terms"].items():
        context = row["taxonomy_context"]
        rebuilt = audit.taxonomy_context(
            context["native_nodes"],
            row["paper"]["source_organism"],
            "Pantoea sp. X85" if term == "ARO:3007648" else None,
        )
        assert rebuilt == context
        assert context["source_name_match"]["taxon_id"] == expected[term]
        assert context["experimental_taxon_assignment"] is None
    alternate = checkpoint["terms"]["ARO:3007648"]["taxonomy_context"]["alternate_context"]
    assert alternate == [
        {
            "taxon_id": "NCBITaxon:3037258",
            "scientific_name": "Pantoea sp. X85",
            "rank": "species",
            "source_species_in_native_lineage": False,
            "assigned_as_source_strain": False,
            "same_subject_crosswalk_verified": False,
        }
    ]


@pytest.mark.parametrize("change", ["inactive", "wrong_rank", "different_name", "duplicate", "extra"])
def test_taxonomy_rejects_unsupported_name_resolution(checkpoint, change):
    row = checkpoint["terms"]["ARO:3007437"]
    entries = copy.deepcopy(row["taxonomy_context"]["native_nodes"])
    if change == "inactive":
        entries[0]["active"] = False
    elif change == "wrong_rank":
        entries[0]["rank"] = "strain"
    elif change == "different_name":
        entries[0]["scientificName"] = "Different species"
    elif change == "duplicate":
        entries.append(copy.deepcopy(entries[0]))
    else:
        extra = copy.deepcopy(entries[0])
        extra.update(taxonId=999, scientificName="Different species")
        entries.append(extra)
    with pytest.raises(ValueError):
        audit.taxonomy_context(entries, row["paper"]["source_organism"])


@pytest.fixture
def response():
    query = audit.PROTEIN_QUERIES["ebr5"]
    url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
        {"query": query, "format": "json", "size": "500", "fields": audit.FIELDS}
    )
    plan = {"requests": {"ebr5": {"query": query, "url": url}}, "release": "2026_03", "max_bytes": 10000}
    attempt = {"url": url, "key": "ebr5", "retries": 0, "redirects_followed": 0}
    body = json.dumps({"results": [], "suggestions": [{"query": "gene_exact:similar", "hits": 1}]}).encode()
    receipt = {
        **attempt,
        "status": 200,
        "bytes": len(body),
        "body": {"sha256": hashlib.sha256(body).hexdigest()},
        "headers": {
            "x-uniprot-release": "2026_03",
            "content-type": "application/json",
            "x-total-results": "0",
        },
    }
    return plan, "ebr5", receipt, attempt, body


def test_suggestions_do_not_become_candidates(response):
    entries, suggestions = audit.validate_response(*response)
    assert entries == []
    assert len(suggestions) == 1


@pytest.mark.parametrize("kind", ["duplicate", "sequence"])
def test_rejects_duplicate_or_nonmetadata_results(response, kind):
    plan, key, receipt, attempt, _ = response
    entries = [{"primaryAccession": "EXAMPLE"}]
    if kind == "duplicate":
        entries.append(copy.deepcopy(entries[0]))
    else:
        entries[0]["sequence"] = {"value": "NOT_REQUESTED"}
    body = json.dumps({"results": entries}).encode()
    receipt["bytes"] = len(body)
    receipt["body"]["sha256"] = hashlib.sha256(body).hexdigest()
    receipt["headers"]["x-total-results"] = str(len(entries))
    with pytest.raises(ValueError):
        audit.validate_response(plan, key, receipt, attempt, body)


@pytest.mark.parametrize(
    "change",
    ["denial", "pagination", "release", "count", "hash", "redirect", "retry", "domain", "extra_fields"],
)
def test_response_rejects_partial_or_changed_sources(response, change):
    plan, key, receipt, attempt, body = copy.deepcopy(response)
    if change == "denial":
        receipt["status"] = 403
    elif change == "pagination":
        receipt["headers"]["link"] = "next"
    elif change == "release":
        receipt["headers"]["x-uniprot-release"] = "different"
    elif change == "count":
        receipt["headers"]["x-total-results"] = "1"
    elif change == "hash":
        receipt["body"]["sha256"] = "changed"
    elif change == "redirect":
        receipt["headers"]["location"] = "https://example.com"
    elif change == "retry":
        attempt["retries"] = 1
    elif change == "domain":
        plan["requests"][key]["url"] = plan["requests"][key]["url"].replace("rest.uniprot.org", "example.com")
    else:
        plan["requests"][key]["url"] += "&sequence=true"
    with pytest.raises(ValueError):
        audit.validate_response(plan, key, receipt, attempt, body)
