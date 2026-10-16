"""Public and synthetic checks for primary identity and evidence boundaries."""

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
import audit_aph_mph_primary as audit  # noqa: E402


@pytest.fixture(autouse=True)
def offline(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline audit attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)


@pytest.fixture
def checkpoint():
    return json.loads((ROOT / (audit.PREFIX + ".json")).read_bytes())


@pytest.fixture
def assessment():
    return json.loads((ROOT / (audit.PREFIX + "-assessment.json")).read_bytes())


def test_all_memberships_and_open_scope(checkpoint):
    index = json.loads((ROOT / "research/2026-10-15-card-current-references.json").read_bytes())
    rows, claims = audit.bind_current(ROOT, index, set(checkpoint["terms"]))
    assert rows == checkpoint["records"] and claims == checkpoint["claims"]
    assert len(rows) == 11 and len(claims) == 18
    for term, row in checkpoint["terms"].items():
        assert (
            sorted(c["record_identifier"] for c in claims if c["aro_id"] == term) == row["record_memberships"]
        )
        assert row["reference_candidates"] == []
        assert row["experimental_allele_assignment"] is None
        assert row["experimental_strain_taxon_assignment"] is None
        assert row["whole_record_primary_review"] == "OPEN"
    assert checkpoint["constraints"]["ncbi_requests"] == 0
    assert checkpoint["constraints"]["issue_1040"] == "DEFERRED"
    assert checkpoint["constraints"]["full_corpus_goal"] == "OPEN"


def test_native_rank_and_uncultured_limits(checkpoint):
    terms = checkpoint["terms"]
    assert terms["ARO:3003071"]["source_taxonomy_context"] is None
    for term in ("ARO:3003072", "ARO:3003767"):
        assert terms[term]["source_taxonomy_context"]["taxon_id"] == "NCBITaxon:1396"
    context = terms["ARO:3003991"]["source_taxonomy_context"]
    assert context["taxon_id"] == "NCBITaxon:1120679" and context["rank"] == "species"
    assert context["native_name_matches"] == [{"field": "otherNames", "value": "Paenibacillus sp. LC231"}]
    assert terms["ARO:3004543"]["source_taxonomy_context"]["taxon_id"] == "NCBITaxon:173362"


def test_aph_hold_and_spelling_are_not_resolved(checkpoint):
    hold = checkpoint["primary_access_hold"]
    assert hold["http_status"] == 403
    assert hold["retry_or_alternate_route"] is False
    assert hold["native_synonym"] == "apaA15"
    assert hold["synonym_corrected_to_source_label"] is False
    assert hold["selected_as_aphA15"] is False


@pytest.fixture
def table_words(assessment):
    labels = [
        "MphA",
        "MphB",
        "MphC",
        "MphE",
        "MphFb",
        "MphG",
        "MphHc",
        "MphI",
        "MphJ",
        "MphK",
        "MphL",
        "MphM",
        "MphN",
        "MphOc",
    ]
    source = {v["source_label"].lower(): v for v in assessment["terms"].values()}
    words = []
    for i, label in enumerate(labels):
        y = 151 + 11.5 * i if label != "MphOc" else 306.5
        row = source.get(label[:4].lower(), {})
        words.append((77, y, 104, y + 10, label))
        if row.get("previous_name"):
            words.append((122, y, 205, y + 10, row["previous_name"]))
        if label == "MphOc":
            words.extend([(211, 301, 330, 311, "Brachybacterium"), (211, 312, 330, 322, "paraconglomeratum")])
        else:
            words.append((211, y, 330, y + 10, row.get("source_organism", "Example")))
        words.append((340, y, 405, y + 10, row.get("source_accession", "EXAMPLE")))
        words.append((416, y, 422, y + 10, "9"))
    words.append((211, 323, 330, 333, "FOOTNOTE_NOT_A_SPECIES"))
    return words


def test_pdf_columns_wrapping_and_footnotes(table_words, assessment):
    rows = audit.identity_rows(table_words)
    audit.check_identity_rows(rows, assessment)
    assert rows["mpho"]["source_organism"] == "Brachybacterium paraconglomeratum"
    assert rows["mphf"]["source_accession"] == "CAJ98570.1"
    assert rows["mphl"]["previous_name"] == "B. cereus Cluster A"


@pytest.mark.parametrize("change", ["nucleotide_as_protein", "version", "name", "species", "conflate"])
def test_identity_transcription_rejects_promotions(table_words, assessment, change):
    rows = audit.identity_rows(table_words)
    if change == "nucleotide_as_protein":
        assessment["terms"]["ARO:3003991"]["accession_namespace"] = "INSDC_PROTEIN"
    elif change == "version":
        rows["mphl"]["source_accession"] = "WP_001094257.2"
    elif change == "name":
        rows["mphf"]["previous_name"] = "MphA"
    elif change == "species":
        rows["mphf"]["source_organism"] = "Escherichia coli"
    else:
        rows["mpho"] = copy.deepcopy(rows["mphf"])
    with pytest.raises(ValueError):
        audit.check_identity_rows(rows, assessment)


def test_missing_identity_row_fails(table_words):
    with pytest.raises(ValueError):
        audit.identity_rows([w for w in table_words if w[4] != "MphI"])


@pytest.fixture
def response():
    query = "xref:refseq-WP_001094257.1"
    fields = audit.reference.FIELDS
    url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
        {"query": query, "format": "json", "size": "500", "fields": fields}
    )
    plan = {
        "requests": {"mphL": {"query": query, "url": url}},
        "max_bytes": 10000,
        "release": "2026_03",
        "fields": fields,
    }
    attempt = {"key": "mphL", "url": url, "retries": 0, "redirects_followed": 0}
    body = json.dumps({"results": [], "suggestions": [{"query": "unrelated", "hits": 1}]}).encode()
    receipt = {
        **attempt,
        "status": 200,
        "bytes": len(body),
        "body": {"sha256": hashlib.sha256(body).hexdigest()},
        "headers": {
            "content-type": "application/json",
            "x-uniprot-release": "2026_03",
            "x-total-results": "0",
        },
    }
    return plan, receipt, attempt, body


def test_empty_search_and_suggestions_are_not_candidates(response):
    plan, receipt, attempt, body = response
    audit.exchange(plan, "mphL", receipt, attempt, body)
    entries, suggestions = audit.metadata_response(plan, "mphL", receipt, body)
    assert entries == [] and len(suggestions) == 1


@pytest.mark.parametrize("change", ["denial", "hash", "bytes", "retry", "redirect", "url"])
def test_request_history_integrity(response, change):
    plan, receipt, attempt, body = response
    if change == "denial":
        receipt["status"] = 403
    elif change == "hash":
        receipt["body"]["sha256"] = "changed"
    elif change == "bytes":
        receipt["bytes"] += 1
    elif change == "retry":
        receipt["retries"] = attempt["retries"] = 1
    elif change == "redirect":
        receipt["headers"]["location"] = "https://example.com"
    else:
        attempt["url"] = "https://example.com"
    with pytest.raises(ValueError):
        audit.exchange(plan, "mphL", receipt, attempt, body)


@pytest.mark.parametrize("change", ["status", "release", "page", "count", "domain", "fields"])
def test_metadata_scope_integrity(response, change):
    plan, receipt, _, body = response
    if change == "status":
        receipt["status"] = 403
    elif change == "release":
        receipt["headers"]["x-uniprot-release"] = "different"
    elif change == "page":
        receipt["headers"]["link"] = "next"
    elif change == "count":
        receipt["headers"]["x-total-results"] = "1"
    elif change == "domain":
        plan["requests"]["mphL"]["url"] = plan["requests"]["mphL"]["url"].replace(
            "rest.uniprot.org", "example.com"
        )
    else:
        plan["fields"] += ",sequence"
    with pytest.raises(ValueError):
        audit.metadata_response(plan, "mphL", receipt, body)
