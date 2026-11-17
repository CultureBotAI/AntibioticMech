"""Do not promote yeast reference metadata or mixed assay readouts to alleles."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_mycophenolic_context as audit  # noqa: E402


def metadata(gene):
    accession, canonical, locus, sgd, version, sequence_version = audit.REFERENCES[gene]
    organism = "Saccharomyces cerevisiae (strain ATCC 204508 / S288c)"
    block = {"geneName": {"value": canonical}, "orderedLocusNames": [{"value": locus}]}
    if gene != canonical:
        block["synonyms"] = [{"value": gene}]
    return {
        "primaryAccession": accession,
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "entryAudit": {"entryVersion": version, "sequenceVersion": sequence_version},
        "genes": [block],
        "organism": {"taxonId": 559292, "scientificName": organism},
        "proteinDescription": {"recommendedName": {"fullName": {"value": "TEST REFERENCE"}}},
        "uniProtKBCrossReferences": [{"database": "SGD", "id": sgd}],
    }, {
        "taxonId": 559292,
        "scientificName": organism,
        "rank": "strain",
        "active": True,
        "lineage": [{"taxonId": 4932, "scientificName": "Saccharomyces cerevisiae", "rank": "species"}],
    }


@pytest.mark.parametrize("gene", list(audit.REFERENCES))
@pytest.mark.parametrize(
    "change",
    [
        "none",
        "accession",
        "canonical",
        "locus",
        "sgd",
        "taxon",
        "version",
        "sequence_version",
        "duplicate_gene",
        "sequence",
        "features",
        "comments",
    ],
)
def test_only_exact_reference_metadata_is_projected(gene, change):
    entry, taxonomy = metadata(gene)
    if change == "accession":
        entry["primaryAccession"] = "OTHER"
    elif change == "canonical":
        entry["genes"][0]["geneName"]["value"] = "OTHER"
    elif change == "locus":
        entry["genes"][0]["orderedLocusNames"][0]["value"] = "OTHER"
    elif change == "sgd":
        entry["uniProtKBCrossReferences"][0]["id"] = "OTHER"
    elif change == "taxon":
        entry["organism"]["taxonId"] = 4932
    elif change == "version":
        entry["entryAudit"]["entryVersion"] = True
    elif change == "sequence_version":
        entry["entryAudit"]["sequenceVersion"] += 1
    elif change == "duplicate_gene":
        entry["genes"].append(copy.deepcopy(entry["genes"][0]))
    elif change in {"sequence", "features", "comments"}:
        entry[change] = "DO_NOT_EXPORT"
    if change != "none":
        with pytest.raises(ValueError):
            audit.project_protein(entry, gene, taxonomy)
        return
    result = audit.project_protein(entry, gene, taxonomy)
    assert result["experimental_subject_assignment"] is False
    assert result["exact_resistance_allele"] is False
    assert result["resistance_asserted_from_reference"] is False
    assert result["reference_taxon_id"] == "NCBITaxon:559292"
    assert result["source_species_taxon_id"] == "NCBITaxon:4932"


def test_rpb1_alias_cannot_be_inferred_from_locus():
    entry, taxonomy = metadata("RPB1")
    entry["genes"][0].pop("synonyms")
    with pytest.raises(ValueError, match="gene name"):
        audit.project_protein(entry, "RPB1", taxonomy)


@pytest.mark.parametrize("change", ["species", "rank", "inactive", "name"])
def test_taxonomy_is_reference_scope_not_subject_identity(change):
    entry, taxonomy = metadata("IMD2")
    if change == "species":
        taxonomy["lineage"][0]["taxonId"] = 4896
    elif change == "rank":
        taxonomy["rank"] = "species"
    elif change == "inactive":
        taxonomy["active"] = False
    else:
        taxonomy["scientificName"] = "OTHER"
    with pytest.raises(ValueError):
        audit.project_protein(entry, "IMD2", taxonomy)


@pytest.mark.parametrize("gene", list(audit.REFERENCES))
@pytest.mark.parametrize("name", [None, "", "INCONSISTENT SPECIES LABEL"])
def test_species_identifier_requires_consistent_lineage_name(gene, name):
    entry, taxonomy = metadata(gene)
    if name is None:
        taxonomy["lineage"][0].pop("scientificName")
    else:
        taxonomy["lineage"][0]["scientificName"] = name
    with pytest.raises(ValueError, match="species lineage name"):
        audit.project_protein(entry, gene, taxonomy)


def test_unreviewed_primary_bytes_are_refused():
    with pytest.raises(ValueError, match="primary article changed"):
        audit.primary_context(b"<html>IMD2</html>")


def test_public_checkpoint_preserves_evidence_boundaries():
    data = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert set(data["references"]) == set(audit.REFERENCES)
    assert data["references"]["RPB1"]["canonical_gene"] == "RPO21"
    assert data["summary"] == {
        "corpus_records_in_scope": 2939,
        "records_in_this_checkpoint": 1,
        "versioned_reference_proteins": 5,
        "primary_access_holds": 2,
        "curated_resistance_assertions": 0,
        "whole_record_primary_signoffs": 0,
    }
    assert data["record_before"]["identifier"] == "CHEBI:168396"
    assert data["primary"]["experimental_allele_assignment"] is None
    assert data["primary"]["experimental_strain_taxon_assignment"] is None
    assert data["primary"]["experimental_genome_assignment"] is None
    assert data["primary"]["supplement_subject_crosswalk"].startswith("PENDING_")
    assert set(data["primary"]["visually_reviewed_figures"]) == {"2", "5"}
    contexts = {x["gene"]: x for x in data["primary"]["gene_context"]}
    assert "not uniquely IMD2" in contexts["IMD2"]["limit"]
    assert "Not a direction of effect shared" in contexts["RPB1"]["limit"]
    for key in ("primary-2002", "primary-2003"):
        assert data["sources"][key]["status"] == 403
    assert data["sources"]["primary-2012"]["status"] == 200
    assert data["limits"]["issue_1040"] == "DEFERRED"
    assert data["limits"]["ncbi_requests"] == 0
    for key in (
        "variants_exported",
        "sequences_exported",
        "numeric_ast_exported",
        "reference_strain_is_experimental_subject",
        "clinical_category_inferred",
    ):
        assert data["limits"][key] is False
    for key in ("figure2-storage", "figure5-storage"):
        assert "?" not in data["sources"][key]["url"]


def test_native_offline_replay_uses_immutable_snapshot(monkeypatch):
    directory = ROOT / audit.CACHE
    if not (directory / "reviewed.json").exists():
        pytest.skip("private native research cache not present")

    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted networking")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    real_loader = audit.load_record

    def snapshot_only(path):
        assert path == directory / "baseline-record.yaml"
        return real_loader(path)

    monkeypatch.setattr(audit, "load_record", snapshot_only)
    expected = (ROOT / audit.OUTPUT).read_bytes()
    actual = (
        json.dumps(audit.build(ROOT, directory), indent=2, sort_keys=True, ensure_ascii=True) + "\n"
    ).encode()
    assert actual == expected
