"""Native qualitative evidence must not assign experimental alleles or genomes."""

import copy
import hashlib
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_formaldehyde_efga as audit  # noqa: E402

from antibioticmech.activity_collections import load_record  # noqa: E402
from antibioticmech.curate.curation_event import record_curation_event  # noqa: E402
from antibioticmech.validation.write_validated import write_validated_antibiotic  # noqa: E402


def context():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def reference_pair():
    name = "Methylorubrum extorquens (strain PA1)"
    entry = {
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "primaryAccession": "P0DX96",
        "entryAudit": {"entryVersion": 8, "sequenceVersion": 1},
        "genes": [{"geneName": {"value": "efgA"}, "orderedLocusNames": [{"value": "Mext_4158"}]}],
        "organism": {"taxonId": 419610, "scientificName": name},
        "proteinDescription": {"recommendedName": {"fullName": {"value": "Reference protein"}}},
    }
    taxonomy = {
        "taxonId": 419610,
        "scientificName": name,
        "active": True,
        "rank": "strain",
        "lineage": [{"taxonId": 408, "rank": "species", "scientificName": "Methylorubrum extorquens"}],
    }
    return entry, taxonomy


@pytest.mark.parametrize(
    "change",
    [
        "accession",
        "gene",
        "locus",
        "entry_version",
        "sequence_version",
        "taxon",
        "name",
        "rank",
        "active",
        "lineage",
        "review",
        "sequence",
        "features",
        "comments",
    ],
)
def test_reference_identity_and_payload_are_guarded(change):
    entry, tax = reference_pair()
    if change == "accession":
        entry["primaryAccession"] = "OTHER"
    elif change == "gene":
        entry["genes"][0]["geneName"]["value"] = "efgB"
    elif change == "locus":
        entry["genes"][0]["orderedLocusNames"][0]["value"] = "OTHER"
    elif change in {"entry_version", "sequence_version"}:
        entry["entryAudit"]["entryVersion" if change == "entry_version" else "sequenceVersion"] += 1
    elif change == "taxon":
        entry["organism"]["taxonId"] = 408
    elif change == "name":
        tax["scientificName"] = "OTHER"
    elif change in {"rank", "active"}:
        tax[change] = "species" if change == "rank" else False
    elif change == "lineage":
        tax["lineage"][0]["taxonId"] = 1
    elif change == "review":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    else:
        entry[change] = []
    with pytest.raises(ValueError):
        audit.efga_reference(entry, tax)


def test_reference_is_not_the_experimental_subject():
    ref = audit.efga_reference(*reference_pair())
    assert ref["protein_accession"] == "UniProtKB:P0DX96"
    assert ref["reference_taxon_id"] == "NCBITaxon:419610"
    assert ref["source_species_taxon_id"] == "NCBITaxon:408"
    assert ref["experimental_subject_assignment"] is False
    assert ref["reference_assigned_to_experimental_allele"] is False
    assert ref["experimental_genome_assignment"] is None


@pytest.mark.parametrize(
    "field,value",
    [
        ("taxonId", 419610),
        ("rank", "strain"),
        ("active", False),
        ("scientificName", "OTHER"),
        ("synonyms", []),
    ],
)
def test_species_identity_not_reference_strain(field, value):
    tax = {
        "taxonId": 408,
        "rank": "species",
        "active": True,
        "scientificName": "Methylorubrum extorquens",
        "synonyms": ["Methylobacterium extorquens"],
    }
    assert audit.species_context(tax)["taxon_id"] == "NCBITaxon:408"
    tax[field] = value
    with pytest.raises(ValueError, match="species identity"):
        audit.species_context(tax)


def test_empty_queries_do_not_use_fuzzy_suggestions():
    result = audit.empty_reference({"results": [], "suggestions": [{"value": "unrelated"}]})
    assert result["suggestions_used"] is False
    assert result["protein_accession_assigned"] is None
    assert "NOT_PROTEIN_ABSENCE" in result["scope"]
    with pytest.raises(ValueError, match="empty EfgB"):
        audit.empty_reference({"results": [{}]})


@pytest.mark.parametrize(
    "group", ["record", "primary", "reference_protein", "subject_species", "efgb_queries"]
)
def test_incomplete_or_mutated_claim_scope_rejected(group):
    original = context()
    data = copy.deepcopy(original)
    del data[group]
    with pytest.raises(ValueError, match="scope changed"):
        audit.claims(data)
    # Mutate every guarded context field, including negative results and opposing effects.
    ignored = {
        "record": {"path", "sha256"},
        "primary": {
            "locations",
            "native_species",
            "background",
            "heterologous_host",
            "endpoints",
            "numeric_AST_exported",
            "supplement_tables_reviewed",
            "whole_record_primary_review",
            "crystal_density_identifies_unmodified_formaldehyde_unambiguously",
        },
        "reference_protein": {
            "entry_type",
            "gene_names",
            "reference_organism_name",
            "reference_taxon_id",
            "reference_taxon_rank",
            "reference_taxon_scientific_name",
            "species_lineage_verified",
            "protein_name",
        },
    }
    for key in original[group].keys() - ignored.get(group, set()):
        data = copy.deepcopy(original)
        data[group][key] = "UNSUPPORTED"
        with pytest.raises(ValueError, match="scope changed"):
            audit.claims(data)


def test_claims_preserve_context_and_unresolved_identity():
    first, second = audit.claims(context())
    assert (first["gene_id"], second["gene_id"]) == ("Mext_4158", "Mext_0606")
    for claim in (first, second):
        assert claim["taxon_id"] == "NCBITaxon:408"
        assert {"protein_accession", "strain", "strain_taxon_id", "alteration", "source"}.isdisjoint(claim)
        assert "PMID:34038406" in {item["reference"] for item in claim["evidence"]}
    assert "beneficial under endogenous" in first["note"]
    assert "not unmodified PA1" in first["note"]
    assert "alone did not confer" in second["note"]
    assert "putative, not demonstrated" in second["note"]
    assert "UniProtKB:P0DX96" in {item["reference"] for item in first["evidence"]}
    assert context()["limits"]["issue_1040"] == "DEFERRED"


def test_unreviewed_primary_bytes_refused():
    with pytest.raises(ValueError, match="primary article changed"):
        audit.primary_context(b"different document")


def test_historical_curation_preserves_other_fields(tmp_path):
    receipt = json.loads((ROOT / "research/2026-10-14-formaldehyde-curation.json").read_bytes())
    before = load_record(ROOT / audit.FIXTURE)
    assert hashlib.sha256((ROOT / audit.FIXTURE).read_bytes()).hexdigest() == receipt["before"]["sha256"]
    after = copy.deepcopy(before)
    assert not after.get("resistance_mechanisms")
    after["resistance_mechanisms"] = audit.claims(context())
    record_curation_event(after, **receipt["curation_event"])
    assert after["curation_history"][:-1] == before["curation_history"]
    fields = set(before) - {"curation_history", "resistance_mechanisms"}
    assert {k: after[k] for k in fields} == {k: before[k] for k in fields}
    target = tmp_path / "record.yaml"
    write_validated_antibiotic(after, target)
    payload = target.read_bytes()
    assert hashlib.sha256(payload).hexdigest() == receipt["record"]["sha256"]
    write_validated_antibiotic(load_record(target), target)
    assert target.read_bytes() == payload


def test_cached_replay_never_reads_live_record_or_network(monkeypatch):
    if not (ROOT / audit.CACHE / "reviewed-assets.json").exists():
        pytest.skip("private native evidence cache not present")

    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted networking")

    original_open = Path.open

    def guarded_open(path, *args, **kwargs):
        assert path.resolve() != ROOT / audit.RECORD, "replay read mutable live record"
        return original_open(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded_open)
    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    assert audit.build(ROOT) == context()
