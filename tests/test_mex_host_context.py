"""Do not transfer heterologous-host results onto reference proteins or donor taxa."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_mex_host_context as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def public_result():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def assessment():
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    return audit.read_json(ROOT, plan["assessment"])


@pytest.mark.parametrize("key", audit.FALSE_FIELDS)
def test_primary_scope_cannot_be_promoted(key):
    notes = assessment()
    notes[key] = True
    with pytest.raises(ValueError, match="promoted"):
        audit.validate_assessment(notes)


@pytest.mark.parametrize("change", ["donor", "host", "paper", "qualification", "duplicate", "alias", "ncbi"])
def test_changed_primary_identity_and_qualifications_rejected(change):
    notes = assessment()
    if change == "donor":
        notes["source_species_name"] = notes["assay_host_species_name"]
    elif change == "host":
        notes["assay_host_species_name"] = notes["source_species_name"]
    elif change == "paper":
        notes["pmid"] = "8849250"
    elif change == "qualification":
        notes["claim_qualifications"][0]["status"] = "VERIFIED_NATIVE_RESISTANCE"
    elif change == "duplicate":
        notes["claim_qualifications"][1] = copy.deepcopy(notes["claim_qualifications"][0])
    elif change == "alias":
        notes["source_reported_host_alias"]["strain_taxon_id_assigned"] = True
    else:
        notes["access"]["ncbi_endpoints_opened"] = 1
    with pytest.raises(ValueError):
        audit.validate_assessment(notes)


def taxon_fixture():
    return {
        "taxonId": 562,
        "rank": "species",
        "scientificName": "Escherichia coli",
        "active": True,
        "parent": {"taxonId": 561, "scientificName": "Escherichia"},
        "lineage": [{"taxonId": 561, "rank": "genus", "scientificName": "Escherichia"}],
    }


def test_species_crosswalk_is_not_experimental_strain_identity():
    result = audit.species_context(taxon_fixture(), "Escherichia coli")
    assert result["taxon_id"] == "NCBITaxon:562"
    assert result["experimental_strain_taxon_assigned"] is False
    assert result["reference_protein_assigned_to_host"] is False


@pytest.mark.parametrize(
    "key,value", [("scientificName", "Pseudomonas aeruginosa"), ("rank", "strain"), ("active", False)]
)
def test_species_crosswalk_rejects_wrong_identity_or_rank(key, value):
    taxon = taxon_fixture()
    taxon[key] = value
    with pytest.raises(ValueError):
        audit.species_context(taxon, "Escherichia coli")


def test_portable_artifact_preserves_complete_claim_and_reference_context(monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert "/reports/" not in str(path) and "/data/antibiotics/" not in str(path)
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    result = public_result()
    prior = audit.read_json(ROOT, result["prior_members"])
    mex = audit.read_json(ROOT, result["prior_mex"])
    audit.read_json(ROOT, result["plan"])
    notes = audit.read_json(ROOT, result["assessment"])
    audit.validate_assessment(notes)
    assert result["claims"] == [c for c in prior["claims"] if c["aro_id"] in audit.TERMS]
    assert result["claims"] == [c for c in mex["claims"] if c["aro_id"] in audit.TERMS]
    ids = {c["record_identifier"] for c in result["claims"]}
    assert result["records"] == [r for r in prior["records"] if r["identifier"] in ids]
    assert len(ids) == 17 and len(result["claims"]) == 22
    assert result["claim_dispositions"] == audit.claim_dispositions(
        result["claims"], result["records"], notes
    )
    assert sum(r["selected_primary_qualification"] is not None for r in result["claim_dispositions"]) == 6
    for row in result["claim_dispositions"]:
        assert row["whole_claim_primary_signoff"] is row["source_claim_removed"] is False
        assert row["exact_chemical_form_verified"] is row["experimental_allele_assigned"] is False
    for accession, row in result["component_references"].items():
        assert row == mex["reference_candidates"][accession]
        assert row["reference_taxonomy"]["taxon_id"] == "NCBITaxon:208964"
    for accession, row in result["member_reference_views"].items():
        assert row == prior["reference_proteins"][accession]
    assert len(set(result["component_references"]) | set(result["member_reference_views"])) == 7
    assert result["source_species"]["taxon_id"] == "NCBITaxon:287"
    assert result["assay_host_species"]["taxon_id"] == "NCBITaxon:562"
    assert result["own_citation_query"]["result_count"] == 0
    assert result["own_citation_query"]["establishes_biological_absence"] is False
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"
    assert result["limits"]["biological_records_changed"] == result["limits"]["ncbi_requests"] == 0
    assert result["limits"]["issue_1040"] == "DEFERRED"


def test_qualification_must_bind_a_selected_source_claim():
    result = public_result()
    remaining = [c for c in result["claims"] if c["record_identifier"] != "CHEBI:28368"]
    with pytest.raises(ValueError, match="does not bind"):
        audit.claim_dispositions(remaining, result["records"], assessment())


def test_distinct_mexd_entries_not_collapsed():
    result = public_result()
    old = result["member_reference_views"]["UniProtKB:Q51396"]
    pao1 = result["component_references"]["UniProtKB:Q9HVI9"]
    assert old["gene_symbols"] == pao1["gene_symbols"] == ["mexD"]
    assert old["reference_taxonomy"]["native_rank"] == "species"
    assert pao1["reference_taxonomy"]["native_rank"] == "strain"
    assert result["distinct_mexd_references"]["same_experimental_allele_established"] is False


def test_no_operational_or_ast_values_exported():
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    forbidden = {
        "sequence",
        "features",
        "variants",
        "alteration",
        "assembly_accession",
        "biosample_accession",
        "mic_value",
        "primers",
        "coordinates",
        "protocol",
    }
    assert not set(keys(public_result())) & forbidden
    assert not set(keys(assessment())) & forbidden


def test_offline_replay_when_native_cache_available(monkeypatch):
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    if not (ROOT / plan["host_species_taxonomy"]["receipt"]["path"]).exists():
        pytest.skip("native cache unavailable; portable checks still run")
    original = Path.open

    def read_only(path, mode="r", *args, **kwargs):
        assert not set(mode) & set("wax+"), "offline replay attempted file write"
        return original(path, mode, *args, **kwargs)

    monkeypatch.setattr(Path, "open", read_only)
    assert audit.build(ROOT) == public_result()
