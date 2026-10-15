"""Keep screen direction, citation absence, species and exact-strain scope separate."""

import copy
import hashlib
import json
import socket
import sys
from html import escape
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_ciclopirox_primary as audit  # noqa: E402


def lead():
    return {
        "source": "MED",
        "id": audit.PMID,
        "pmid": audit.PMID,
        "doi": audit.DOI,
        "pmcid": "PMC6329577",
        "pubYear": "2019",
        "title": "Selected primary study.",
    }


def previous():
    return {
        "discovery": [
            {"records": [{"identifier": "CHEBI:453011", "queries": [{"candidates": [lead()]}]}]}
            for _ in range(2)
        ]
    }


def test_discovery_memberships_are_one_publication():
    result = audit.selected_lead(previous(), lead())
    assert result["query_memberships"] == 2
    assert result["independent_publications"] == 1


@pytest.mark.parametrize("change", ["duplicate", "missing", "salt", "doi", "pmid", "pmcid", "pubYear"])
def test_discovery_guards(change):
    old, selected = previous(), lead()
    if change == "duplicate":
        old["discovery"].append(copy.deepcopy(old["discovery"][0]))
    elif change == "missing":
        old["discovery"].pop()
    elif change == "salt":
        old["discovery"][0]["records"][0]["identifier"] = "CHEBI:31398"
    else:
        selected[change] = "OTHER"
    with pytest.raises(ValueError):
        audit.selected_lead(old, selected)


def article():
    meta = {"citation_title": lead()["title"], "citation_doi": audit.DOI, "citation_date": "Jan 11, 2019"}
    return (
        "<html><head>"
        + "".join(f'<meta name="{k}" content="{escape(v)}">' for k, v in meta.items())
        + '</head><body><div id="artText">'
        + "".join(f"<p>{escape(marker)}</p>" for marker in audit.MARKERS.values())
        + "</div></body></html>"
    ).encode()


def test_primary_screen_is_not_resistant_allele_curation(monkeypatch):
    payload = article()
    monkeypatch.setattr(audit, "ARTICLE_SHA", hashlib.sha256(payload).hexdigest())
    result = audit.primary_context(payload, lead())
    assert result["phenotype_direction"] == "INCREASED_SUSCEPTIBILITY_NOT_INCREASED_RESISTANCE"
    assert result["screened_deletion_strains"] == 96
    assert result["direct_target_established_by_screen"] is False
    assert result["numeric_AST_exported_or_converted"] is False
    assert result["per_gene_or_allele_signoff"] is False
    assert result["experimental_genome_assignment"] is None
    assert set(result["locations"]) == set(audit.MARKERS)
    assert all("normalized_text_sha256" in row and "text" not in row for row in result["locations"].values())


@pytest.mark.parametrize("change", ["sha", "doi", "date", "title", "duplicate_meta", "missing", "duplicate"])
def test_primary_identity_and_location_guards(monkeypatch, change):
    payload = article()
    if change in {"doi", "date", "title"}:
        text = {"doi": audit.DOI, "date": "Jan 11, 2019", "title": lead()["title"]}[change]
        payload = payload.replace(text.encode(), b"OTHER")
    elif change == "duplicate_meta":
        payload = payload.replace(
            b"</head>", f'<meta name="citation_doi" content="{audit.DOI}"></head>'.encode()
        )
    elif change == "missing":
        payload = payload.replace(next(iter(audit.MARKERS.values())).encode(), b"OTHER")
    elif change == "duplicate":
        payload = payload.replace(
            b"</div>", ("<p>" + next(iter(audit.MARKERS.values())) + "</p></div>").encode()
        )
    monkeypatch.setattr(
        audit, "ARTICLE_SHA", "OTHER" if change == "sha" else hashlib.sha256(payload).hexdigest()
    )
    with pytest.raises(ValueError):
        audit.primary_context(payload, lead())


def taxon():
    species = {"taxonId": 562, "scientificName": "Escherichia coli", "rank": "species"}
    return {
        "taxonId": 83333,
        "scientificName": "Escherichia coli (strain K12)",
        "rank": "strain",
        "active": True,
        "parent": species,
        "lineage": [species],
        "strains": [{"name": "K12 / BW25113"}, {"name": "K12 / MG1655"}],
    }


def test_taxonomy_does_not_assign_exact_experimental_strain():
    result = audit.species_context(taxon())
    assert result["species_taxon_id"] == "NCBITaxon:562"
    assert result["reference_lists_BW25113"] is True
    assert result["reference_taxon_uniquely_identifies_BW25113"] is False
    assert result["experimental_derivative_taxon_id"] is None
    assert result["experimental_genome_assignment"] is None


@pytest.mark.parametrize(
    "change", ["taxid", "name", "rank", "active", "species", "parent", "missing_strain", "duplicate_strain"]
)
def test_taxonomy_scope_guards(change):
    value = taxon()
    if change in {"taxid", "name", "rank", "active"}:
        key = {"taxid": "taxonId", "name": "scientificName", "rank": "rank", "active": "active"}[change]
        value[key] = False if change == "active" else "OTHER"
    elif change == "species":
        value["lineage"][0]["taxonId"] = 999
    elif change == "parent":
        value["parent"] = {"taxonId": 999, "scientificName": "OTHER"}
    elif change == "missing_strain":
        value["strains"].pop(0)
    elif change == "duplicate_strain":
        value["strains"].append(copy.deepcopy(value["strains"][0]))
    with pytest.raises(ValueError):
        audit.species_context(value)


def test_empty_citation_query_is_not_protein_absence():
    result = audit.citation_context({"results": []}, {"X-Total-Results": "0", "X-UniProt-Release": "2026_03"})
    assert result["query_complete"] is True
    assert result["protein_absence_or_lack_of_function_inferred"] is False
    assert result["gene_name_or_locus_queries_performed"] is False
    assert result["allele_or_protein_assignment"] is None


@pytest.mark.parametrize("change", ["results", "count", "pagination", "release"])
def test_empty_query_completeness_guards(change):
    payload, headers = {"results": []}, {"X-Total-Results": "0", "X-UniProt-Release": "2026_03"}
    if change == "results":
        payload["results"] = [{}]
    else:
        headers[
            {"count": "X-Total-Results", "pagination": "Link", "release": "X-UniProt-Release"}[change]
        ] = "OTHER"
    with pytest.raises(ValueError):
        audit.citation_context(payload, headers)


def test_unplanned_request_rejected(tmp_path):
    directory = tmp_path / audit.CACHE
    directory.mkdir(parents=True)
    (directory / "unplanned-attempt.json").write_text("{}")
    with pytest.raises(ValueError, match="request inventory"):
        audit.build(tmp_path)


def test_native_checkpoint_replays_offline(monkeypatch):
    if not (ROOT / audit.CACHE / "cohort.json").is_file():
        pytest.skip("private native research cache is unavailable")

    def forbidden(*args, **kwargs):
        raise AssertionError("network forbidden in native replay")

    monkeypatch.setattr(requests.sessions.Session, "request", forbidden)
    monkeypatch.setattr(socket.socket, "connect", forbidden)
    monkeypatch.setattr(socket, "create_connection", forbidden)
    result = audit.build(ROOT)
    assert result == json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert result["limits"]["scientific_http_attempts"] == 2
    assert result["limits"]["ncbi_requests"] == 0
    assert result["limits"]["biological_records_changed"] == 0
    assert result["chemical_scope"]["compound_record_assignment"] is None
