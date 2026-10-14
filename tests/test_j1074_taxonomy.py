"""Species grounding cannot turn a background chromosome into an experimental genome."""

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
import audit_j1074_taxonomy as audit  # noqa: E402
from seed_from_sources import merge_with_existing  # noqa: E402


def background():
    return [{"accession": "CP004370", "sequence_version": "1", "tax_id": "1886",
             "scientific_name": "Streptomyces albidoflavus", "strain": "J1074",
             "description": "Streptomyces albidoflavus strain J1074, complete genome.",
             "study_accession": "PRJNA180996", "sample_accession": "SAMN02603310",
             "first_public": "2013-04-10", "last_updated": "2018-11-09"}], [
        {"taxonId": 1886, "scientificName": "Streptomyces albidoflavus", "rank": "species", "active": True},
        {"taxonId": 1477431, "scientificName": "Streptomyces albidoflavus group", "rank": "species group"},
    ]


@pytest.mark.parametrize("change", [
    "none", *audit.ENA_FIELDS.split(","), "sequence", "empty", "duplicate", "taxon", "name",
    "rank", "inactive", "duplicate_species", "duplicate_name",
])
def test_exact_metadata_and_species_agreement(change):
    rows, taxa = background()
    if change in rows[0]:
        rows[0][change] = "WRONG"
    elif change == "sequence":
        rows[0]["sequence"] = "NOT REQUESTED"
    elif change == "empty":
        rows.clear()
    elif change == "duplicate":
        rows *= 2
    elif change == "taxon":
        taxa[0]["taxonId"] = 1888
    elif change == "name":
        taxa[0]["scientificName"] = "Streptomyces albus"
    elif change == "rank":
        taxa[0]["rank"] = "strain"
    elif change == "inactive":
        taxa[0]["active"] = False
    elif change == "duplicate_species":
        taxa.append(copy.deepcopy(taxa[0]))
    elif change == "duplicate_name":
        taxa.append({**taxa[0], "taxonId": 999})
    if change != "none":
        with pytest.raises(ValueError):
            audit.project_background(rows, taxa)
        return
    result = audit.project_background(rows, taxa)
    assert result["current_species"] == audit.SPECIES
    assert result["experimental_genome_assignment"] is None
    assert result["experimental_sample_assignment"] is None
    assert result["experimental_allele_assignment"] is None
    assert result["chromosome_is_assembly_accession"] is False
    assert result["resistance_inferred_from_chromosome"] is False


def test_verified_sources_reproduce_offline(monkeypatch):
    if not (ROOT / audit.CACHE / "cohort.json").exists():
        pytest.skip("private native-source cache unavailable")

    def fail(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(socket.socket, "connect", fail)
    monkeypatch.setattr(socket, "create_connection", fail)
    monkeypatch.setattr(requests.sessions.Session, "request", fail)
    assert audit.build(ROOT, ROOT / audit.CACHE) == json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_primary_payload_drift_is_rejected():
    with pytest.raises(ValueError, match="article changed"):
        audit.primary_locations(b"changed")


def test_public_context_keeps_legacy_nodes_and_donor_boundaries():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert {t["taxonId"] for t in result["historical_name_search"]["candidates"]} == {1962, 457425, 3466461}
    assert result["historical_name_candidates_selected_as_experimental_taxa"] == []
    assert result["host_taxonomy_is_donor_taxonomy"] is False
    assert result["donor_reference_proteins_preserved"] == ["UniProtKB:D8L2W8", "UniProtKB:Q70HZ0"]
    assert result["modern_name_is_formal_taxonomic_reclassification_study"] is False
    assert result["limits"]["ncbi_requests"] == 0
    assert result["curation_scope"]["full_corpus_records_in_scope"] == 2939
    assert result["curation_scope"]["new_resistance_claims"] == 0


@pytest.mark.parametrize("change", ["record", "gene", "taxon", "protein", "source", "reference", "host"])
def test_claim_scope_drift_is_not_automatically_grounded(change):
    identifier = "CHEBI:78661"
    claim = {"gene_families": ["borO"], "taxon_label": "Streptomyces albus",
             "label": "Streptomyces albus", "note": "J1074", "evidence": [{"reference": "PMID:15112998"}]}
    if change == "record":
        identifier = "CHEBI:1"
    elif change == "gene":
        claim["gene_families"] = ["OTHER"]
    elif change == "taxon":
        claim["taxon_id"] = "NCBITaxon:1888"
    elif change == "protein":
        claim["protein_accession"] = "UniProtKB:Q70HZ0"
    elif change == "source":
        claim["source"] = "PHIBASE"
    elif change == "reference":
        claim["evidence"] = [{"reference": "PMID:1"}]
    elif change == "host":
        claim["note"] = "Other host"
    with pytest.raises(ValueError):
        audit.grounded_claims(identifier, [claim])


def test_live_curation_changes_species_context_only():
    receipt = json.loads((ROOT / "research/2026-10-14-j1074-curation.json").read_bytes())
    assert receipt["records_changed"] == 3 and receipt["claims_grounded"] == 5
    for row in receipt["records"]:
        before = load_record(ROOT / row["fixture"]["path"])
        after = load_record(ROOT / row["after"]["path"])
        expected = audit.grounded_claims(row["identifier"], before["resistance_mechanisms"])
        assert after["resistance_mechanisms"] == expected
        assert after["curation_history"] == [*before["curation_history"], row["curation_event"]]
        other = set(before) - {"resistance_mechanisms", "curation_history"}
        assert {k: before[k] for k in other} == {k: after[k] for k in other}
        for old, new in zip(before["resistance_mechanisms"], expected, strict=True):
            changed = {"taxon_id", "taxon_label", "label", "note", "evidence"}
            assert {k: v for k, v in old.items() if k not in changed} == {
                k: v for k, v in new.items() if k not in changed}
            assert new["taxon_id"] == "NCBITaxon:1886"
            assert new["taxon_label"] == "Streptomyces albidoflavus"
            assert "historical reference context" in new["note"]
            assert not {"protein_accession", "strain_taxon_id", "alteration"}.intersection(new)
        seeded = copy.deepcopy(after)
        seeded.pop("resistance_mechanisms")
        assert merge_with_existing(seeded, after)["resistance_mechanisms"] == expected
