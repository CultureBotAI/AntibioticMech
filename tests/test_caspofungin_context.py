"""Locus references must not become experimental alleles or causal assertions."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_caspofungin_context as audit  # noqa: E402


def reference_entry():
    return {
        "primaryAccession": "Q6FNE4",
        "entryType": "UniProtKB unreviewed (TrEMBL)",
        "entryAudit": {"entryVersion": 136, "sequenceVersion": 1},
        "genes": [{"orderedLocusNames": [{"value": "CAGL0K00605g"}]}],
        "organism": {"taxonId": 284593, "scientificName": "CBS138 reference"},
        "proteinDescription": {
            "recommendedName": {
                "fullName": {
                    "value": "Cell division control protein",
                    "evidences": [{"evidenceCode": "ECO:0000256"}],
                }
            }
        },
    }


def reference_taxon():
    return {
        "taxonId": 284593,
        "scientificName": "CBS138 reference",
        "active": True,
        "rank": "strain",
        "lineage": [{"taxonId": 5478, "scientificName": "Candida glabrata", "rank": "species"}],
    }


@pytest.mark.parametrize(
    "change",
    [
        "none",
        "reviewed",
        "sequence",
        "features",
        "wrong_locus",
        "symbol_only",
        "orf_only",
        "duplicate_block",
        "extra_block",
        "duplicate_locus",
        "gene_name",
        "synonym",
        "wrong_reference_taxon",
        "wrong_taxon",
        "inactive",
        "species_rank",
        "missing_lineage",
        "wrong_species",
        "duplicate_species",
        "wrong_species_name",
        "name_mismatch",
        "no_version",
        "bool_version",
        "zero_version",
        "no_protein_name",
    ],
)
def test_explicit_locus_projection(change):
    entry, taxon = reference_entry(), reference_taxon()
    if change == "reviewed":
        entry["entryType"] = "UniProtKB reviewed (Swiss-Prot)"
    elif change in {"sequence", "features"}:
        entry[change] = "not part of this metadata scope"
    elif change == "wrong_locus":
        entry["genes"][0]["orderedLocusNames"][0]["value"] = "CAGL0K00605g_extra"
    elif change == "symbol_only":
        entry["genes"] = [{"geneName": {"value": "CDC6"}}]
    elif change == "orf_only":
        entry["genes"] = [{"orfNames": [{"value": "CAGL0K00605g"}]}]
    elif change in {"duplicate_block", "extra_block"}:
        entry["genes"].append(copy.deepcopy(entry["genes"][0]) if change == "duplicate_block" else {})
    elif change == "duplicate_locus":
        entry["genes"][0]["orderedLocusNames"] *= 2
    elif change == "gene_name":
        entry["genes"][0]["geneName"] = {"value": "CDC6"}
    elif change == "synonym":
        entry["genes"][0]["synonyms"] = [{"value": "CDC6"}]
    elif change == "wrong_reference_taxon":
        entry["organism"]["taxonId"] = 5478
    elif change == "wrong_taxon":
        taxon["taxonId"] = 5478
    elif change == "inactive":
        taxon["active"] = False
    elif change == "species_rank":
        taxon["rank"] = "species"
    elif change == "missing_lineage":
        taxon["lineage"] = []
    elif change == "wrong_species":
        taxon["lineage"][0]["taxonId"] = 5476
    elif change == "duplicate_species":
        taxon["lineage"] *= 2
    elif change == "wrong_species_name":
        taxon["lineage"][0]["scientificName"] = "Candida albicans"
    elif change == "name_mismatch":
        entry["organism"]["scientificName"] = "Other strain"
    elif change == "no_version":
        entry["entryAudit"].pop("sequenceVersion")
    elif change == "bool_version":
        entry["entryAudit"]["sequenceVersion"] = True
    elif change == "zero_version":
        entry["entryAudit"]["entryVersion"] = 0
    elif change == "no_protein_name":
        entry["proteinDescription"] = {}
    if change != "none":
        with pytest.raises(ValueError):
            audit.project_locus(entry, taxon, "CAGL0K00605g")
        return
    result = audit.project_locus(entry, taxon, "CAGL0K00605g")
    assert result["protein_accession"] == "UniProtKB:Q6FNE4"
    assert result["reference_taxon_id"] == "NCBITaxon:284593"
    assert not result["experimental_subject_taxon_assignment"]
    assert result["experimental_allele_assignment"] is result["experimental_genome_assignment"] is None
    assert not result["paper_symbol_is_uniprot_gene_name"]
    assert not result["protein_name_is_independent_experimental_validation"]


def test_saved_evidence_distinctions():
    dossier = json.loads((ROOT / audit.OUTPUT).read_bytes())
    cdc6, mrpl11 = [dossier["terms"][key] for key in ("ARO:3009390", "ARO:3009372")]
    assert cdc6["reference"]["protein_accession"] == "UniProtKB:Q6FNE4"
    assert mrpl11["reference"]["protein_accession"] == "UniProtKB:Q6FNR2"
    assert mrpl11["reference"]["protein_name_evidence_codes"] == ["ECO:0008006"]
    assert cdc6["primary_assessment"]["evidence_type"] == "FUNCTIONAL_COMPARISON_IN_LABORATORY_BACKGROUND"
    assert (
        mrpl11["primary_assessment"]["evidence_type"]
        == "CO_OCCURRENCE_IN_CLINICAL_LINEAGE_NOT_ISOLATED_CAUSALITY"
    )
    assert not mrpl11["primary_assessment"]["direct_card_definition_primary_citation"]
    for term in (cdc6, mrpl11):
        assert [q["result_count"] for q in term["new_queries"]] == [0, 1]
        assert not term["exact_fungamr_row_crosswalk_verified"]
        assert not term["new_resistance_assertion"]
        assert not term["primary_assessment"]["direct_antibiotic_target_alteration_established"]
        assert not term["gene_id_endpoint_requested"]
    assert dossier["summary"]["biological_records_changed"] == 0
    assert dossier["summary"]["whole_record_reviews_completed"] == 0
    assert not dossier["primary"]["numeric_mic_extracted_from_heatmap"]
    assert not dossier["constraints"]["sequences_variants_protocols_exported"]
    assert dossier["constraints"]["ncbi_requests"] == 0
    assert dossier["goal_status"] == "OPEN"


@pytest.mark.parametrize("change", ["none", "status", "url", "attempt", "retry", "hash", "bytes", "body"])
def test_native_receipt_integrity_and_signed_url_redaction(tmp_path, change):
    url = "https://storage.googleapis.com/public/image.png?signature=private-value"
    body = tmp_path / "image-response.bin"
    body.write_bytes(b"native image fixture")
    attempt = {"url": url}
    receipt = {
        "url": url,
        "status": 200,
        "retry_performed": False,
        "sha256": audit.reference.digest(body),
        "bytes": body.stat().st_size,
        "retrieved_at": "2026-10-14T00:00:00Z",
    }
    if change == "status":
        receipt["status"] = 403
    elif change == "url":
        receipt["url"] = "https://example.org/other"
    elif change == "attempt":
        attempt["url"] = "https://example.org/other"
    elif change == "retry":
        receipt["retry_performed"] = True
    elif change == "hash":
        receipt["sha256"] = "0" * 64
    elif change == "bytes":
        receipt["bytes"] += 1
    elif change == "body":
        body.write_bytes(b"different image fixture")
    (tmp_path / "image-attempt.json").write_text(json.dumps(attempt))
    (tmp_path / "image-receipt.json").write_text(json.dumps(receipt))
    if change != "none":
        with pytest.raises(ValueError):
            audit.native(tmp_path, tmp_path, "image", url)
        return
    result = audit.native(tmp_path, tmp_path, "image", url)
    assert result["url"] == "https://storage.googleapis.com/public/image.png"
    assert "private-value" not in json.dumps(result)


def test_offline_replay(monkeypatch):
    if not (ROOT / audit.CACHE / "selection.json").exists():
        pytest.skip("private native-source cache is not committed")

    def denied(*args, **kwargs):
        raise AssertionError("network forbidden in replay")

    monkeypatch.setattr(socket, "socket", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    result = audit.build(ROOT, ROOT / audit.CACHE)
    assert (json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode() == (
        ROOT / audit.OUTPUT
    ).read_bytes()
