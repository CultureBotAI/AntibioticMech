"""Do not turn yeast sensitivity or conditional rescue into resistant alleles."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_eugenol_context as audit  # noqa: E402


def metadata(gene):
    canonical = "XRN1" if gene == "KEM1" else gene
    locus = audit.TABLE_GENES.get(gene, "YKR039W")
    block = {"geneName": {"value": canonical}, "orderedLocusNames": [{"value": locus}]}
    if canonical != gene:
        block["synonyms"] = [{"value": gene}]
    name = "Saccharomyces cerevisiae (strain ATCC 204508 / S288c)"
    return {
        "primaryAccession": "P08566", "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "entryAudit": {"entryVersion": 1, "sequenceVersion": 1}, "genes": [block],
        "organism": {"taxonId": 559292, "scientificName": name},
        "proteinDescription": {"recommendedName": {"fullName": {"value": "TEST REFERENCE"}}},
        "uniProtKBCrossReferences": [{"database": "SGD", "id": "S000002534"}],
    }, {
        "taxonId": 559292, "rank": "strain", "scientificName": name, "active": True,
        "lineage": [{"taxonId": 4932, "rank": "species", "scientificName": "Saccharomyces cerevisiae"}],
    }


@pytest.mark.parametrize("gene", ["ARO1", "KEM1", "GAP1"])
@pytest.mark.parametrize("change", [
    "none", "gene", "duplicate_gene", "no_locus", "no_sgd", "version", "inactive", "rank", "taxon",
    "species", "species_name", "missing_species_name", "empty_names", "sequence", "features", "comments",
])
def test_reference_identity_and_scope(gene, change):
    entry, taxonomy = metadata(gene)
    if change == "gene":
        entry["genes"][0]["geneName"]["value"] = "OTHER"
        entry["genes"][0].pop("synonyms", None)
    elif change == "duplicate_gene":
        entry["genes"].append(copy.deepcopy(entry["genes"][0]))
    elif change == "no_locus":
        entry["genes"][0].pop("orderedLocusNames")
    elif change == "no_sgd":
        entry["uniProtKBCrossReferences"] = []
    elif change == "version":
        entry["entryAudit"]["sequenceVersion"] = True
    elif change == "inactive":
        taxonomy["active"] = False
    elif change == "rank":
        taxonomy["rank"] = "species"
    elif change == "taxon":
        entry["organism"]["taxonId"] = 4932
    elif change == "species":
        taxonomy["lineage"][0]["taxonId"] = 4896
    elif change == "species_name":
        taxonomy["lineage"][0]["scientificName"] = "OTHER"
    elif change == "missing_species_name":
        taxonomy["lineage"][0].pop("scientificName")
    elif change == "empty_names":
        entry["organism"]["scientificName"] = taxonomy["scientificName"] = ""
    elif change in {"sequence", "features", "comments"}:
        entry[change] = "DO_NOT_EXPORT"
    if change != "none":
        with pytest.raises(ValueError):
            audit.project_gene(entry, gene, taxonomy)
        return
    result = audit.project_gene(entry, gene, taxonomy)
    assert result["experimental_subject_assignment"] is False
    assert result["exact_resistance_allele"] is False
    assert result["resistance_inferred_from_reference"] is False
    assert result["reference_taxon_id"] == "NCBITaxon:559292"
    assert result["source_species_taxon_id"] == "NCBITaxon:4932"
    assert result["canonical_gene"] == ("XRN1" if gene == "KEM1" else gene)


def test_source_symbol_and_locus_must_both_agree():
    entry, taxonomy = metadata("ARO1")
    entry["genes"][0]["orderedLocusNames"] = [{"value": "YGL148W"}]
    with pytest.raises(ValueError, match="gene/locus"):
        audit.project_gene(entry, "ARO1", taxonomy)


@pytest.mark.parametrize("gene", ["YDR442W", "YMR326C", "UNPLANNED"])
def test_held_or_unplanned_genes_cannot_be_projected(gene):
    entry, taxonomy = metadata("ARO1")
    with pytest.raises(ValueError, match="unplanned or held"):
        audit.project_gene(entry, gene, taxonomy)


def test_primary_direction_and_negative_comparisons():
    assert audit.evidence_roles("BAP2") == [
        {"location": "Table 1", "evidence": "SENSITIVITY_SCREEN_HIT_NOT_RESISTANCE"},
        {"location": "Figure 4", "background_gene_context": "ARO1",
         "evidence": "NO_SIGNIFICANT_RESCUE_REPORTED"},
    ]
    for gene in ("GAP1", "TAT1"):
        assert audit.evidence_roles(gene) == [{
            "location": "Figure 4", "background_gene_context": "ARO1",
            "evidence": "CONDITIONAL_PARTIAL_GROWTH_RESCUE",
        }]
    assert audit.evidence_roles("TAT2")[0]["evidence"] == "NO_SIGNIFICANT_RESCUE_REPORTED"
    with pytest.raises(ValueError):
        audit.evidence_roles("UNPLANNED")


def test_unreviewed_article_cannot_establish_primary_context():
    with pytest.raises(ValueError, match="article changed"):
        audit.primary_context(b"<html>Eugenol GAP1 TAT1</html>")


def test_all_source_panels_accounted_for_without_resistance_promotion():
    checkpoint = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert len(checkpoint["genes"]) == 35
    assert len(checkpoint["references"]) == 33
    assert {row["source_symbol"] for row in checkpoint["genes"]} == audit.GENES
    held = {row["source_symbol"] for row in checkpoint["genes"] if row["reference_accession"] is None}
    assert held == audit.HELD
    assert checkpoint["references"]["KEM1"]["canonical_gene"] == "XRN1"
    assert checkpoint["references"]["ERG2"]["protein_accession"] == "UniProtKB:P32352"
    assert all(row["resistance_category_inferred"] is False for row in checkpoint["genes"])
    assert all(row["experimental_allele_assignment"] is None for row in checkpoint["genes"])
    primary = checkpoint["primary"]
    assert primary["baseline_MIC_reported"] is True
    assert primary["baseline_MIC_is_resistant_genotype_endpoint"] is False
    assert primary["direct_binding_demonstrated"] is False
    assert primary["new_resistance_curation_supported_by_this_checkpoint"] is False
    assert primary["multidrug_resistance_deletions_excluded_from_source_hit_list"] is True
    assert checkpoint["summary"]["curated_resistance_assertions"] == 0
    assert checkpoint["summary"]["corpus_records_in_scope"] == 2939
    assert checkpoint["limits"]["issue_1040"] == "DEFERRED"
    assert checkpoint["limits"]["ncbi_requests"] == 0
    assert checkpoint["limits"]["whole_record_primary_review"] == "OPEN"


@pytest.mark.parametrize("change", ["none", "reused_release", "reused_version"])
def test_native_offline_replay(monkeypatch, change):
    directory = ROOT / audit.CACHE
    if not (directory / "reference-cohort-response.bin").exists():
        pytest.skip("optional native research cache not present")

    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted networking")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    loader = audit.load_record

    def baseline_only(path):
        assert path == directory / "baseline-record.yaml"
        return loader(path)

    monkeypatch.setattr(audit, "load_record", baseline_only)
    read_response = audit.reference.read_response

    def changed_reuse(root, directory, key, endpoint, parameters=None):
        payload, source = read_response(root, directory, key, endpoint, parameters)
        if directory == ROOT / audit.REUSE and key == "reference-canary":
            if change == "reused_release":
                source["release"] = "STALE"
            elif change == "reused_version":
                payload["results"][0]["entryAudit"]["entryVersion"] += 1
        return payload, source

    monkeypatch.setattr(audit.reference, "read_response", changed_reuse)
    if change != "none":
        with pytest.raises(ValueError, match="release|version"):
            audit.build(ROOT, directory)
        return
    payload = (
        json.dumps(audit.build(ROOT, directory), indent=2, sort_keys=True, ensure_ascii=True) + "\n"
    ).encode()
    assert payload == (ROOT / audit.OUTPUT).read_bytes()
