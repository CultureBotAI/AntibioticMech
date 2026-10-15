"""Primary identity text, empty identifier queries and positive controls have different scopes."""

import copy
import csv
import json
import socket
import sys
from pathlib import Path
from urllib.parse import urlencode

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_mdea_primary as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def public_result():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_portable_checkpoint_preserves_all_prior_claims_and_taxonomy(monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert "/reports/" not in str(path) and "/data/antibiotics/" not in str(path)
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    result = public_result()
    prior = audit.common.read_json(ROOT, result["prior"])
    for key in ("records", "claims", "term", "species_name_crosswalk"):
        assert result[key] == prior[key]
    assert len(result["records"]) == len(result["claims"]) == 7
    assert result["reference_candidates"] == {}
    assert result["summary"]["corpus_records_hash_checked"] == 2939
    assert result["limits"]["biological_records_changed"] == result["limits"]["ncbi_requests"] == 0
    assert (
        result["limits"]["exact_allele_assignments"]
        == result["limits"]["experimental_identity_assignments"]
        == 0
    )
    assert result["limits"]["issue_1040"] == "DEFERRED"
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"


def test_donor_reference_and_heterologous_contexts_are_not_merged():
    result = public_result()
    notes = audit.common.read_json(ROOT, result["assessment"])
    assert notes == result["primary_identity_assessment"]
    audit.validate_assessment(notes)
    assert notes["reference_strain_label"] == "UA159"
    assert notes["paper_donor_strain_labels"] == ["KCTC 3065", "ATCC 25175"]
    assert notes["paper_reference_locus_label"] == "SMU 2109"
    assert notes["reference_accession"] == "NP_722397"
    assert notes["accession_version_reported"] is notes["donor_is_reference_strain"] is False
    assert result["limits"]["full_primary_text_or_figures_replayed_offline"] is False
    assert result["web_tools"]["author_fulltext_native_body_cached"] is False
    assert result["web_tools"]["figures_or_pdf_visually_inspected"] is False
    assert (
        result["limits"]["new_primary_results_review_scope"]
        == "SELECTED_IDENTITY_CONTEXT_NOT_AST_OR_FULL_PAPER"
    )


@pytest.mark.parametrize(
    "key",
    [
        "donor_is_reference_strain",
        "sequence_comparison_independently_performed",
        "exact_experimental_accession_assigned",
        "figures_visually_reviewed",
        "table_layout_visually_verified",
        "whole_paper_signoff",
        "numeric_ast_exported",
        "ncbi_links_followed",
        "author_contacted",
    ],
)
def test_primary_context_cannot_be_promoted(key):
    notes = copy.deepcopy(public_result()["primary_identity_assessment"])
    notes[key] = True
    with pytest.raises(ValueError, match="promoted"):
        audit.validate_assessment(notes)


def crossref_fixture():
    source = public_result()["registered_source"]
    return {
        "status": "ok",
        "message-type": "work",
        "message": {
            "DOI": audit.DOI,
            "title": [
                "Gene Cloning and Characterization of MdeA, a Novel Multidrug Efflux Pump "
                "in Streptococcus mutans"
            ],
            "resource": {"primary": {"URL": source["registered_article_url"]}},
            "link": [copy.deepcopy(source["registered_pdf_link"])],
        },
    }


@pytest.mark.parametrize("change", ["doi", "title", "article_url", "pdf_url", "link_kind", "extra_link"])
def test_crossref_is_bound_to_the_selected_paper_and_link(change):
    payload = crossref_fixture()
    work = payload["message"]
    if change == "doi":
        work["DOI"] = "10.1000/example"
    elif change == "title":
        work["title"] = ["Other organism's MdeA"]
    elif change == "article_url":
        work["resource"]["primary"]["URL"] = "https://example.org"
    elif change == "pdf_url":
        work["link"][0]["URL"] = "https://example.org"
    elif change == "link_kind":
        work["link"][0]["content-version"] = "unspecified"
    else:
        work["link"].append(copy.deepcopy(work["link"][0]))
    with pytest.raises(ValueError):
        audit.project_crossref(payload)


def test_crossref_registration_does_not_grant_access_or_redistribution():
    result = audit.project_crossref(crossref_fixture())
    assert result["registered_pdf_link"]["intended-application"] == "similarity-checking"
    assert result["registration_is_access_or_redistribution_permission"] is False


def control_fixture():
    params = {**audit.query_parameters("taxonomy-control"), "cursor": "next"}
    url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(params)
    source = {
        "headers": {
            "x-uniprot-release": "2026_03",
            "x-total-results": "2451",
            "link": "<" + url + '>; rel="next"',
        }
    }
    payload = {
        "results": [
            {
                "primaryAccession": "A0A090AX29",
                "organism": {"taxonId": 1309, "scientificName": "Streptococcus mutans"},
            }
        ]
    }
    return payload, source


@pytest.mark.parametrize(
    "change", ["count", "release", "pagination", "offsite", "query", "accession", "taxon", "sequence"]
)
def test_partial_control_requires_its_exact_query_and_identity(change):
    payload, source = control_fixture()
    headers = source["headers"]
    if change == "count":
        headers["x-total-results"] = "1"
    elif change == "release":
        headers["x-uniprot-release"] = "2026_04"
    elif change == "pagination":
        headers.pop("link")
    elif change == "offsite":
        headers["link"] = '<https://example.org/next>; rel="next"'
    elif change == "query":
        headers["link"] = headers["link"].replace("1309", "562")
    elif change == "accession":
        payload["results"][0]["primaryAccession"] = "Q00001"
    elif change == "taxon":
        payload["results"][0]["organism"]["taxonId"] = 562
    else:
        payload["results"][0]["sequence"] = "unexpected"
    with pytest.raises(ValueError):
        audit.project_control(json.dumps(payload).encode(), source)


def test_partial_control_is_not_a_mdea_mapping_or_a_completed_query():
    payload, source = control_fixture()
    before = copy.deepcopy((payload, source))
    result = audit.project_control(json.dumps(payload).encode(), source)
    assert (payload, source) == before
    assert result["complete_for_query"] is result["pagination_followed"] is False
    assert result["selected_as_mdea_candidate"] is False
    assert result["declared_result_count"] == 2451 and result["entries_inspected"] == 1
    for key in ("reference", "locus"):
        row = public_result()["queries"][key]
        assert row["complete_for_exact_query"] is True and row["result_count"] == 0
        assert row["establishes_biological_absence"] is False


def test_pdf_failures_do_not_erase_the_separate_author_text_review():
    result = public_result()
    failure = result["publisher_pdf_attempt"]
    assert failure["http_status"] is None and failure["access_denial_established"] is False
    assert failure["fulltext_inspected"] is False
    assert failure["alternate_fulltext_route_requested"] is True
    assert failure["primary_identity_text_available_via_separate_author_copy"] is True
    assert result["web_tools"]["author_pdf_click_status"] == 404
    assert result["web_tools"]["author_text_read"] is True


def test_no_operational_values_exported():
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not set(keys(public_result())) & {
        "sequence",
        "features",
        "alteration",
        "variants",
        "gene_id",
        "assembly_accession",
        "biosample_accession",
        "mic_value",
        "abstractText",
    }


def test_offline_replay_when_native_cache_and_current_checkpoint_available():
    native = json.loads((ROOT / audit.PLAN).read_bytes())
    if any(not (ROOT / p["path"]).exists() for p in native["requests"].values()):
        pytest.skip("native cache unavailable; portable checks still run")
    plan = audit.common.read_json(ROOT, native["plan"])
    prior = audit.common.read_json(ROOT, plan["prior"])
    update = audit.common.read_json(ROOT, prior["inputs"]["corpus_update"])
    deltas = {d["path"]: d["after_sha256"] for d in update["record_deltas"]}
    with audit.reference.check_pin(ROOT, prior["inputs"]["census"]).open() as stream:
        census = list(csv.DictReader(stream, delimiter="\t"))
    if any(
        not (ROOT / r["path"]).exists()
        or audit.reference.digest(ROOT / r["path"]) != deltas.get(r["path"], r["record_sha256"])
        for r in census
    ):
        pytest.skip("historical record checkpoint; portable checks still run")
    assert audit.build(ROOT) == public_result()
