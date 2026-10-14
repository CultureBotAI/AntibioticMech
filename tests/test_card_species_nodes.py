"""A standalone species response is not an experimental isolate crosswalk."""

import copy
import csv
import hashlib
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_species_nodes as audit  # noqa: E402
from resistance_checkpoint_records import checkpoint_path  # noqa: E402


def species():
    return {"taxonId": 10, "rank": "species", "scientificName": "Reference species", "active": True,
            "parent": {"taxonId": 1, "scientificName": "Reference"},
            "lineage": [{"taxonId": 1, "rank": "genus", "scientificName": "Reference"}],
            "synonyms": ["Historical species"], "strains": [{"name": "Reference strain"}]}


def expected():
    return {"taxon_id": "NCBITaxon:10", "scientific_name": "Reference species"}


def test_species_response_does_not_turn_synonyms_or_strain_lists_into_subjects():
    result = audit.species_projection(expected(), species())
    assert result["active"] and result["rank"] == "species"
    assert result["status"] == "ACTIVE_NATIVE_RESPONSE_VERIFIED"
    assert result["previous_status"] == "LINEAGE_ANNOTATION_ONLY_NO_STANDALONE_RESPONSE_SELECTED"
    assert not result["experimental_subject_assignment"] and not result["exact_allele_assignment"]
    assert not {"synonyms", "strains", "statistics", "strain_taxon_id"}.intersection(result)


@pytest.mark.parametrize("change", ["inactive", "wrong_id", "wrong_name", "wrong_rank", "namespace",
                                    "duplicate_species", "leading_zero"])
def test_species_identity_conflicts_are_not_silently_repaired(change):
    source, target = species(), expected()
    if change == "inactive":
        source["active"] = False
    elif change == "wrong_id":
        source["taxonId"] = 11
    elif change == "wrong_name":
        source["scientificName"] = "Different species"
    elif change == "wrong_rank":
        source["rank"] = "strain"
    elif change == "namespace":
        target["taxon_id"] = "UniProtKB:10"
    elif change == "leading_zero":
        target["taxon_id"] = "NCBITaxon:010"
    else:
        source["lineage"][0]["rank"] = "species"
    with pytest.raises(ValueError):
        audit.species_projection(target, source)


@pytest.mark.parametrize("change", ["none", "ancestor_id", "ancestor_name", "ancestor_rank", "species_id"])
def test_reference_ancestry_must_match_the_standalone_species_path(change):
    source = species()
    projected = audit.species_projection(expected(), source)
    native = {"taxonId": 20, "rank": "strain", "scientificName": "Reference strain", "active": True,
              "parent": {"taxonId": 10, "scientificName": "Reference species"},
              "lineage": [*copy.deepcopy(source["lineage"]), audit.lineages.identity(source)]}
    if change == "ancestor_id":
        native["lineage"][0]["taxonId"] = 2
    elif change == "ancestor_name":
        native["lineage"][0]["scientificName"] = "Different genus"
    elif change == "ancestor_rank":
        native["lineage"][0]["rank"] = "family"
    elif change == "species_id":
        native["lineage"][-1]["taxonId"] = 11
    if change == "none":
        assert audit.ancestor_concordance(native, projected)
    else:
        with pytest.raises(ValueError):
            audit.ancestor_concordance(native, projected)


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_public_successor_is_exactly_the_prior_unverified_cohort(dossier):
    prior = json.loads(audit.reference.check_pin(ROOT, dossier["inputs"]["prior"]).read_bytes())
    selected = {key for key, row in prior["species"].items() if not row["standalone_active_verified"]}
    assert set(dossier["species"]) == set(dossier["requests"]) == selected and len(selected) == 34
    assert all(prior["species"][key]["native_sources"] == [] for key in selected)
    for key, value in dossier["species"].items():
        assert value["taxon_id"] == prior["species"][key]["taxon_id"]
        assert value["scientific_name"] == prior["species"][key]["scientific_name"]
    proteins = {acc: row for acc, row in prior["proteins"].items()
                if row["reference_species_taxon_id"].split(":")[1] in selected}
    assert dossier["proteins"] == proteins and len(proteins) == 43
    terms = {tid: row for tid, row in prior["terms"].items()
             if set(row["reference_accessions"]) & set(proteins)}
    assert dossier["terms"] == terms and len(terms) == 43
    assert len(dossier["records"]) == 65


def test_public_census_binding_without_freezing_live_records(dossier, monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    text = audit.reference.check_pin(ROOT, dossier["inputs"]["census"]).read_text()
    census = {row["identifier"]: row for row in csv.DictReader(text.splitlines(), delimiter="\t")}
    assert len(census) == 2939
    for record in dossier["records"]:
        assert record["sha256"] == census[record["identifier"]]["record_sha256"]
        assert record["whole_record_primary_review"] == "OPEN"


def test_public_summary_closes_only_reference_taxonomy_gap(dossier):
    summary = dossier["summary"]
    assert summary["species_with_standalone_responses_after"] == summary["total_species_nodes"] == 288
    assert summary["remaining_lineage_only_species"] == 0
    assert summary["total_direct_reference_proteins"] == 979
    assert summary["label_warning_nodes_retained"] == 25
    assert summary["biological_record_changes"] == summary["experimental_assignments"] == 0
    assert summary["whole_record_signoffs"] == 0
    assert all(node["ancestor_lineage_concordant"] for node in dossier["reference_taxa"].values())
    assert dossier["constraints"]["new_network_requests"] == 34
    assert dossier["constraints"]["ncbi_requests"] == dossier["constraints"]["held_source_retries"] == 0
    assert dossier["constraints"]["full_corpus_goal_status"] == "OPEN"


def test_offline_native_replay(dossier, monkeypatch):
    if not (ROOT / audit.CACHE / "cohort.json").exists():
        pytest.skip("optional native taxonomy cache not available")

    def denied(*args, **kwargs):
        raise AssertionError("offline taxonomy replay attempted a network request")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    assert audit.build(ROOT, record_resolver=checkpoint_path) == dossier


@pytest.mark.parametrize("change", ["none", "plan_url", "attempt_url", "receipt_url", "redirects",
                                    "limit", "retry", "bytes", "timing", "release"])
def test_single_attempt_transport_provenance(tmp_path, change):
    url = "https://rest.uniprot.org/taxonomy/10"
    body = json.dumps(species()).encode()
    plan = {"url": url, "redirects_followed": False, "max_bytes": 500_000}
    attempt = {"url": url, "started_at": "2026-10-14T00:00:00+00:00"}
    receipt = {"url": url, "status": 200, "bytes": len(body), "retry_performed": False,
               "retrieved_at": "2026-10-14T00:00:01+00:00", "sha256": hashlib.sha256(body).hexdigest(),
               "headers": {"X-UniProt-Release": "2026_03"}}
    if change.endswith("_url"):
        {"plan": plan, "attempt": attempt, "receipt": receipt}[change.split("_")[0]]["url"] += ".json"
    elif change == "redirects":
        plan["redirects_followed"] = True
    elif change == "limit":
        plan["max_bytes"] += 1
    elif change == "retry":
        receipt["retry_performed"] = True
    elif change == "bytes":
        receipt["bytes"] += 1
    elif change == "timing":
        attempt["started_at"] = "2026-10-14T00:00:02+00:00"
    elif change == "release":
        receipt["headers"]["X-UniProt-Release"] = "changed"
    for kind, value in (("plan", plan), ("attempt", attempt), ("receipt", receipt)):
        (tmp_path / f"species-10-{kind}.json").write_text(json.dumps(value))
    (tmp_path / "species-10-response.bin").write_bytes(body)
    cohort = {"species": {"10": {"url": url}}, "release": "2026_03"}
    if change == "none":
        native, evidence = audit.read_request(tmp_path, tmp_path, "10", cohort)
        assert native == species() and not evidence["retry_performed"]
    else:
        with pytest.raises(ValueError):
            audit.read_request(tmp_path, tmp_path, "10", cohort)
