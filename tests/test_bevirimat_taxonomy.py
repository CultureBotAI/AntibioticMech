"""Taxonomic lineage does not identify a laboratory derivative or patient allele."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_bevirimat_taxonomy as audit  # noqa: E402
from seed_from_sources import merge_with_existing  # noqa: E402


def taxa():
    species = {"taxonId": 3418650, "scientificName": "Lentivirus humimdef1", "rank": "species",
               "active": True, "parent": {"taxonId": 11646, "scientificName": "Lentivirus"}}
    parent = {"taxonId": 11676, "scientificName": "Human immunodeficiency virus type 1",
              "commonName": "HIV-1", "rank": "no rank", "active": True,
              "parent": {"taxonId": 3418650, "scientificName": "Lentivirus humimdef1"},
              "lineage": [{"taxonId": 3418650, "scientificName": "Lentivirus humimdef1", "rank": "species"}]}
    return parent, species


@pytest.mark.parametrize("change", [
    "none", "parent_id", "parent_rank", "parent_active", "parent_name", "parent_common_name",
    "species_id", "species_name", "species_rank", "species_active", "genus", "edge",
    "lineage_id", "lineage_name", "lineage_missing", "lineage_duplicate",
])
def test_species_and_source_context_ranks(change):
    parent, species = taxa()
    if change.startswith("parent_"):
        key = {"parent_id": "taxonId", "parent_rank": "rank", "parent_active": "active",
               "parent_name": "scientificName", "parent_common_name": "commonName"}[change]
        parent[key] = "WRONG"
    elif change.startswith("species_"):
        key = {"species_id": "taxonId", "species_name": "scientificName", "species_rank": "rank",
               "species_active": "active"}[change]
        species[key] = "WRONG"
    elif change == "genus":
        species["parent"]["taxonId"] = 1
    elif change == "edge":
        parent["parent"]["taxonId"] = 1
    elif change == "lineage_id":
        parent["lineage"][0]["taxonId"] = 1
    elif change == "lineage_name":
        parent["lineage"][0]["scientificName"] = "WRONG"
    elif change == "lineage_missing":
        parent["lineage"] = []
    elif change == "lineage_duplicate":
        parent["lineage"] *= 2
    if change != "none":
        with pytest.raises(ValueError):
            audit.project_taxonomy(parent, species)
        return
    result = audit.project_taxonomy(parent, species)
    assert result["species"] == audit.SPECIES
    assert result["source_context_rank"] == "no rank"
    assert result["species_rank"] == "species"
    for field in ("experimental_allele_assignment", "experimental_genome_assignment",
                  "experimental_strain_taxon_assignment", "protein_accession_assignment"):
        assert result[field] is None


@pytest.mark.parametrize("change", [
    "record", "claim_count", "source", "taxon_id", "note", "protein_accession",
])
def test_curation_requires_exact_historical_claim(change):
    before = load_record(ROOT / "tests/fixtures/bevirimat-before-2026-10-14.yaml")
    identifier, claims = before["identifier"], before["resistance_mechanisms"]
    if change == "record":
        identifier = "CHEBI:1"
    elif change == "claim_count":
        claims *= 2
    else:
        claims[0][change] = "CHANGED"
    with pytest.raises(ValueError, match="changed"):
        audit.grounded_claims(identifier, claims)


def test_public_context_does_not_promote_empty_queries_or_background_ids():
    doc = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert doc["primary"]["source_organism_label"] == "HIV-1"
    assert doc["primary"]["native_images_visually_inspected"] is False
    assert doc["primary"]["exact_compound_form_newly_resolved"] is False
    assert doc["limits"]["primary_2009_results_reviewed_in_this_checkpoint"] is False
    assert doc["limits"]["all_inherited_variant_claims_revalidated"] is False
    assert doc["limits"]["ncbi_requests"] == 0
    assert doc["limits"]["issue_1040"] == "DEFERRED"
    for query in doc["queries"].values():
        assert query["result_count"] == 0 and query["complete_for_query"] is True
        assert query["zero_results_establish_absence"] is False
        assert query["alternate_reference_selected"] is False


def test_unreviewed_primary_payload_rejected():
    with pytest.raises(ValueError, match="primary article changed"):
        audit.primary_context(b"HIV-1 NL4-3")


def test_offline_native_replay(monkeypatch):
    if not (ROOT / audit.CACHE / "primary-2010-response.bin").exists():
        pytest.skip("optional native research cache not available")

    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted network access")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    assert audit.build(ROOT, ROOT / audit.CACHE) == json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_live_curation_preserves_every_other_field():
    receipt = json.loads((ROOT / "research/2026-10-14-bevirimat-curation.json").read_bytes())
    before = load_record(ROOT / receipt["fixture"]["path"])
    after = load_record(ROOT / receipt["after"]["path"])
    expected = audit.grounded_claims(before["identifier"], before["resistance_mechanisms"])
    assert after["resistance_mechanisms"] == expected
    assert after["curation_history"] == [*before["curation_history"], receipt["curation_event"]]
    other = set(before) - {"resistance_mechanisms", "curation_history"}
    assert {k: before[k] for k in other} == {k: after[k] for k in other}
    allowed = {"taxon_id", "taxon_label", "note", "evidence"}
    old, new = before["resistance_mechanisms"][0], expected[0]
    assert {k: v for k, v in old.items() if k not in allowed} == {
        k: v for k, v in new.items() if k not in allowed}
    assert new["evidence"][:-1] == old["evidence"]
    assert new["note"].startswith(old["note"])
    assert new["taxon_id"] == "NCBITaxon:3418650"
    assert not {"strain", "strain_taxon_id", "protein_accession", "alteration", "gene_id"}.intersection(new)
    seeded = copy.deepcopy(after)
    seeded.pop("resistance_mechanisms")
    assert merge_with_existing(seeded, after)["resistance_mechanisms"] == expected
