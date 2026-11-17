"""Indexed abstracts, locators and similar titles are not resistant-allele evidence."""

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
import audit_equisetin_leads as audit  # noqa: E402


@pytest.fixture(params=list(audit.METADATA))
def metadata(request):
    key = request.param
    source, identifier, doi, _ = audit.METADATA[key]
    row = {
        "id": identifier,
        "source": source,
        "title": "Synthetic title",
        "abstractText": "Synthetic source: " + "; ".join(audit.MARKERS[key]),
        "isOpenAccess": "N",
        "inEPMC": "N",
        "inPMC": "N",
    }
    if doi:
        row.update(
            {
                "pmid": identifier,
                "doi": doi,
                "fullTextUrlList": {
                    "fullTextUrl": [
                        {
                            "availability": "Subscription required",
                            "availabilityCode": "S",
                            "documentStyle": "doi",
                            "site": "DOI",
                            "url": "https://doi.org/" + doi,
                        }
                    ]
                },
            }
        )
    if key == "2026":
        row.update(
            {
                "firstPublicationDate": "2025-11-28",
                "pubYear": "2026",
                "journalInfo": {"printPublicationDate": "2026-02-01"},
            }
        )
    query = f"EXT_ID:{identifier} AND SRC:{source}"
    return key, {
        "hitCount": 1,
        "request": {"queryString": query, "internalQuery": query, "resultType": "CORE", "pageSize": 1},
        "resultList": {"result": [row]},
    }


def test_abstract_scope_never_establishes_parent_compound_resistant_alleles(metadata):
    key, payload = metadata
    row, context = audit.project_metadata(payload, key)
    assert row is payload["resultList"]["result"][0]
    assert context["scope"] == "INDEXED_ABSTRACT_ONLY_NOT_PRIMARY_RESULTS_REVIEW"
    assert context["primary_results_figures_supplements_reviewed"] is False
    assert context["uniprot_or_exact_allele_assignment"] is None
    assert "Synthetic source" not in json.dumps(context)
    if key == "2026":
        assert context["MDR_label_establishes_equisetin_resistance"] is False
        assert context["transcriptomic_response_establishes_resistant_allele"] is False
        assert context["no_induced_resistance_statement_is_universal_absence_proof"] is False
        assert context["first_publication_date"] != context["issue_date"]
    elif key == "2015":
        assert context["analogue_activity_transferred_to_parent_equisetin"] is False
        assert context["resistant_parent_compound_allele_established"] is False
    else:
        assert context["native_DOI_PMID_PMC_crosswalk_supplied"] is False
        assert context["merged_with_MED38327434_or_counted_as_independent_replication"] is False
        assert context["host_metabolism_genes_assigned_as_microbe_resistance_determinants"] is False


@pytest.mark.parametrize(
    "change",
    [
        "count",
        "boolean_count",
        "missing",
        "duplicate",
        "null_row",
        "query",
        "internal_query",
        "result_type",
        "page_size",
        "boolean_page_size",
        "cursor",
        "id",
        "source",
        "doi",
        "pmid",
        "pmcid",
        "title",
        "abstract",
        "marker",
        "locator",
        "availability",
    ],
)
def test_metadata_identity_and_completeness_guards(metadata, change):
    key, payload = metadata
    row = payload["resultList"]["result"][0]
    if change in {"count", "boolean_count"}:
        payload["hitCount"] = True if change == "boolean_count" else 2
    elif change == "missing":
        payload["resultList"]["result"] = []
    elif change == "duplicate":
        payload["resultList"]["result"].append(copy.deepcopy(row))
    elif change == "null_row":
        payload["resultList"]["result"][0] = None
    elif change in {"query", "internal_query", "result_type", "page_size", "boolean_page_size"}:
        field = {
            "query": "queryString",
            "internal_query": "internalQuery",
            "result_type": "resultType",
            "page_size": "pageSize",
            "boolean_page_size": "pageSize",
        }[change]
        payload["request"][field] = True if change == "boolean_page_size" else "OTHER"
    elif change == "cursor":
        payload["nextCursorMark"] = "more results"
    elif change in {"id", "source", "doi", "pmid", "pmcid", "title"}:
        row[change] = "" if change == "title" else "OTHER"
    elif change in {"abstract", "marker"}:
        row["abstractText"] = None if change == "abstract" else "OTHER"
    elif change == "locator":
        row["fullTextUrlList"] = {"fullTextUrl": [{"url": "https://example.invalid"}]}
    else:
        row["inEPMC"] = "Y"
    with pytest.raises(ValueError):
        audit.project_metadata(payload, key)


@pytest.mark.parametrize("field", ["firstPublicationDate", "pubYear", "printPublicationDate"])
def test_electronic_and_issue_dates_are_not_conflated(field):
    payload = (
        json.loads((ROOT / audit.CACHE / "metadata-2026-response.bin").read_bytes())
        if (ROOT / audit.CACHE / "metadata-2026-response.bin").exists()
        else None
    )
    if payload is None:
        pytest.skip("private source cache is not distributed")
    row = payload["resultList"]["result"][0]
    (row["journalInfo"] if field == "printPublicationDate" else row)[field] = "OTHER"
    with pytest.raises(ValueError, match="dates changed"):
        audit.project_metadata(payload, "2026")


@pytest.mark.parametrize(
    "change", ["none", "host", "path", "target", "extra", "empty_key", "duplicate", "missing", "malformed"]
)
def test_html_locator_keeps_exact_native_destination(monkeypatch, change):
    parameters = {"Redirect": audit.FINAL, "key": "synthetic-routing-key"}
    if change == "target":
        parameters["Redirect"] = "https://example.invalid"
    elif change == "extra":
        parameters["extra"] = "unexpected"
    elif change == "empty_key":
        parameters["key"] = ""
    url = "/retrieve/articleSelectSinglePerm?" + urlencode(parameters)
    if change == "host":
        url = "https://example.invalid" + url
    elif change == "path":
        url = url.replace("articleSelectSinglePerm", "OTHER")
    value = "malformed" if change == "malformed" else "2; url='" + url.replace("&", "&amp;") + "'"
    meta = '<meta http-equiv="REFRESH" content="' + value + '"/>'
    payload = (
        "<html><head>"
        + ("" if change == "missing" else meta * (2 if change == "duplicate" else 1))
        + "</head></html>"
    ).encode()
    monkeypatch.setattr(audit, "LOCATOR_SHA", hashlib.sha256(payload).hexdigest())
    if change == "none":
        assert audit.locator_destination(payload) == "https://linkinghub.elsevier.com" + url
    else:
        with pytest.raises(ValueError):
            audit.locator_destination(payload)


def test_changed_locator_cannot_reuse_manual_review():
    with pytest.raises(ValueError, match="locator body changed"):
        audit.locator_destination(b"<html>changed</html>")


@pytest.mark.parametrize("change", ["none", "id", "string_id", "name", "rank", "active"])
def test_abstract_species_does_not_assign_an_experimental_subject(change):
    taxon = {"taxonId": 1351, "scientificName": "Enterococcus faecalis", "rank": "species", "active": True}
    if change == "none":
        result = audit.ground_species(taxon)
        assert result["experimental_strain_taxon_genome_or_protein_assignment"] is None
        assert result["species_wide_or_equisetin_resistance_asserted"] is False
        return
    field, value = {
        "id": ("taxonId", 562),
        "string_id": ("taxonId", "1351"),
        "name": ("scientificName", "OTHER"),
        "rank": ("rank", "strain"),
        "active": ("active", False),
    }[change]
    taxon[field] = value
    with pytest.raises(ValueError):
        audit.ground_species(taxon)


@pytest.mark.parametrize("change", ["missing_receipt", "missing_attempt", "unresolved_attempt"])
def test_request_coverage_fails_closed(tmp_path, change):
    directory = tmp_path / "cache"
    directory.mkdir()
    keys = {"metadata-" + k for k in audit.METADATA} | {
        "primary-2026-doi",
        "primary-2026-publisher",
        "primary-2026-locator",
        "primary-2026-final",
        "primary-2015-doi",
        "primary-2015-publisher",
    }
    for key in keys:
        for suffix in ("receipt", "attempt"):
            (directory / f"{key}-{suffix}.json").touch()
    if change == "unresolved_attempt":
        (directory / "unreported-attempt.json").touch()
    else:
        (directory / f"metadata-2026-{change.removeprefix('missing_')}.json").unlink()
    with pytest.raises(ValueError, match="research request coverage"):
        audit.build(tmp_path, Path("cache"))


def test_public_checkpoint_preserves_unresolved_primary_and_identity_work():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    status = result["discovery_status"]
    assert status["initial_candidate_identities"] == len(status["initial_candidate_dispositions"]) == 8
    assert list(status["initial_candidate_dispositions"].values()).count("UNASSESSED") == 2
    assert status["initial_candidates_primary_results_unreviewed_including_held_and_abstract_only"] == 6
    assert status["initial_candidate_primary_access_holds"] == 3
    assert status["new_primary_results_reviews"] == 0
    assert result["locator_HTTP_200_is_primary_text"] is False
    for key in ("primary-2026-locator", "primary-2026-final"):
        assert "?" not in result["sources"][key]["url"]
        assert result["sources"][key]["query_retained_only_in_private_receipt"] is True
    assert result["limits"]["ncbi_requests"] == 0
    assert result["limits"]["issue_1040"] == "DEFERRED"
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"


def test_cache_replay_is_offline_and_does_not_read_live_records(monkeypatch):
    if not (ROOT / audit.CACHE / "metadata-AGR-receipt.json").exists():
        pytest.skip("private source cache is not distributed")

    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted networking")

    original_open = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.resolve().is_relative_to(ROOT / "data/antibiotics")
        return original_open(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    assert audit.build(ROOT) == json.loads((ROOT / audit.OUTPUT).read_bytes())


@pytest.mark.parametrize("change", ["cohort", "canary", "locator", "redirect", "html", "manual"])
def test_cached_plan_provenance_guards(monkeypatch, change):
    if not (ROOT / audit.CACHE / "metadata-AGR-receipt.json").exists():
        pytest.skip("private source cache is not distributed")
    original_loads = json.loads

    def altered(payload, *args, **kwargs):
        value = original_loads(payload, *args, **kwargs)
        if not isinstance(value, dict) or "requests" not in value:
            return value
        field = {
            "cohort": "cohort",
            "canary": "canary_review",
            "locator": "native_primary_locator",
            "redirect": "redirect_receipt",
            "html": "native_html_refresh",
            "manual": "manual_redirect_reviewed",
        }[change]
        if field in value:
            value[field] = False if change == "manual" else {}
        return value

    monkeypatch.setattr(json, "loads", altered)
    with pytest.raises(ValueError):
        audit.build(ROOT)
