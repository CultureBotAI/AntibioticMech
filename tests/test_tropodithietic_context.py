"""Bibliography matches and retrieval failures must not become resistance claims."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_tropodithietic_context as audit  # noqa: E402


def headers(total, link=None):
    result = {"X-UniProt-Release": "2026_03", "X-Total-Results": str(total)}
    if link:
        result["Link"] = link
    return result


@pytest.mark.parametrize(
    "payload",
    [None, [], {}, {"results": None}, {"results": {}}, {"results": ""}, {"results": 0}, {"results": False}],
)
def test_malformed_empty_is_not_negative_evidence(payload):
    with pytest.raises(ValueError, match="malformed"):
        audit.search_scope(payload, headers(0))


def test_partial_page_is_never_a_complete_query():
    data = {"results": [{}, {}]}
    with pytest.raises(ValueError, match="completeness"):
        audit.search_scope(data, headers(3, "next"))
    result = audit.search_scope(data, headers(3, "next"), partial=True)
    assert result["complete"] is False and result["unretrieved_entries"] == 1
    assert result["empty_query_proves_protein_absence"] is False
    assert audit.search_scope({"results": []}, headers(0))["complete"] is True


@pytest.mark.parametrize(
    "changes",
    [
        {"X-UniProt-Release": "OTHER"},
        {"X-Total-Results": "invalid"},
        {"X-Total-Results": "-1"},
        {"Link": "next"},
    ],
)
def test_release_and_page_totals_fail_closed(changes):
    with pytest.raises(ValueError):
        audit.search_scope({"results": []}, {**headers(0), **changes}, partial=True)


def sample():
    taxonomy = {
        "taxonId": 1844006,
        "scientificName": "Phaeobacter porticola",
        "rank": "species",
        "active": True,
    }
    row = {
        "primaryAccession": "EXAMPLE",
        "entryAudit": {"entryVersion": 1, "sequenceVersion": 1},
        "entryType": "UniProtKB unreviewed (TrEMBL)",
        "organism": {"taxonId": 1844006, "scientificName": "Phaeobacter porticola"},
        "proteinDescription": {"recommendedName": {"fullName": {"value": "Reference enzyme"}}},
        "genes": [{"geneName": {"value": "example"}}],
        "references": [
            {
                "citation": {
                    "citationType": "submission",
                    "title": "Phaeobacter portensis sp. nov., a tropodithietic acid producing bacterium "
                    "isolated from a German harbor.",
                }
            }
        ],
    }
    return row, taxonomy


def test_submission_title_is_not_resistance_or_experimental_identity():
    row, tax = sample()
    result = audit.bibliography_page([row], tax)
    assert result["entries_with_compound_in_submission_title"] == 1
    assert result["resistance_determinants_assigned"] == 0
    assert result["reference_taxon_assigned_as_experimental_subject"] is False
    assert result["submission_label_accepted_as_synonym"] is False
    assert result["all_provider_matches_explained"] is False
    assert result["unretrieved_pages_assessed"] is False


@pytest.mark.parametrize(
    "change",
    [
        "sequence",
        "features",
        "comments",
        "taxon",
        "name",
        "reviewed",
        "version",
        "gene",
        "protein",
        "citation",
        "duplicate",
    ],
)
def test_reference_page_rejects_mutated_scope(change):
    row, tax = sample()
    rows = [row]
    if change in {"sequence", "features", "comments"}:
        row[change] = []
    elif change == "taxon":
        row["organism"]["taxonId"] = 221822
    elif change == "name":
        row["organism"]["scientificName"] = "Phaeobacter inhibens"
    elif change == "reviewed":
        row["entryType"] = "UniProtKB reviewed (Swiss-Prot)"
    elif change == "version":
        row["entryAudit"]["entryVersion"] = 0
    elif change == "gene":
        row["genes"][0]["geneName"]["value"] = "tropodithietic"
    elif change == "protein":
        row["proteinDescription"]["recommendedName"]["fullName"]["value"] = "Tropodithietic protein"
    elif change == "citation":
        row["references"][0]["citation"]["citationType"] = "journal article"
    else:
        rows.append(copy.deepcopy(row))
    with pytest.raises(ValueError):
        audit.bibliography_page(rows, tax)


@pytest.mark.parametrize(
    "field,value",
    [
        ("active", False),
        ("rank", "strain"),
        ("taxonId", 221822),
        ("taxonId", 1844006.0),
        ("scientificName", "Phaeobacter portensis"),
    ],
)
def test_reference_species_cannot_be_replaced_by_producer_or_submission_label(field, value):
    row, tax = sample()
    tax[field] = value
    with pytest.raises(ValueError, match="reference species"):
        audit.bibliography_page([row], tax)


def test_public_checkpoint_does_not_promote_partial_or_held_evidence():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    citations = result["citation_cohort"]
    assert len(citations["combined_ids"]) == 24
    assert len(citations["discovery_ids"]) == 15
    assert len(citations["chebi_ids"]) == 10
    assert citations["primary_results_reviewed"] == 0
    assert citations["other_candidates_unreviewed"] == 22
    assert {r["status"] for r in result["primary_holds"].values()} == {403, 500}
    broad = result["reference_queries"]["compound-references"]
    assert broad["returned_entries"] == 500 and broad["reported_total"] == 3932
    assert broad["complete"] is False and broad["unretrieved_entries"] == 3432
    assert result["producer_taxonomy"]["named_organism_taxon_id"] == "NCBITaxon:221822"
    assert result["producer_taxonomy"]["resistance_inferred"] is False
    assert result["limits"]["biological_records_changed"] == 0
    assert result["limits"]["issue_1040"] == "DEFERRED"
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"


def test_private_cache_replay_is_offline_and_historical(monkeypatch):
    if not (ROOT / audit.CACHE / "producer-taxonomy-receipt.json").exists():
        pytest.skip("private reference response cache not present")

    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted networking")

    original = Path.open
    live = ROOT / "data/antibiotics/antibacterial/tropodithietic-acid.yaml"

    def guarded(path, *args, **kwargs):
        assert path.resolve() != live
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    assert audit.build(ROOT) == json.loads((ROOT / audit.OUTPUT).read_bytes())
