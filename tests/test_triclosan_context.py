"""Keep systematic locus references, complexes and experimental subjects distinct."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_triclosan_context as audit  # noqa: E402


def metadata(locus="PA0156"):
    _, accession, version, protein = audit.LOCI[locus]
    entry = {
        "primaryAccession": accession, "entryType": "UniProtKB unreviewed (TrEMBL)",
        "entryAudit": {"entryVersion": version, "sequenceVersion": 1},
        "genes": [{"orderedLocusNames": [{"value": locus}]}],
        "organism": {"scientificName": audit.PAO1_NAME, "taxonId": 208964},
        "proteinDescription": {"submissionNames": [{"fullName": {"value": "TEST REFERENCE"}}]},
        "uniProtKBCrossReferences": [{"database": "EMBL", "id": "AE004091", "properties": [
            {"key": "ProteinId", "value": protein}]}],
        "references": [{"citation": {"citationCrossReferences": [
            {"database": "PubMed", "id": pmid}, {"database": "DOI", "id": doi}]},
            "referencePositions": ["DO_NOT_EXPORT"],
            "evidences": [{"source": "PDB", "id": "6VEJ"}] if pmid == "32966762" else []}
            for pmid, doi in [("10984043", "10.1038/35023079"),
                              ("32966762", "10.1016/j.str.2020.09.001")]],
    }
    taxonomy = {
        "taxonId": 208964, "rank": "strain", "active": True, "scientificName": audit.PAO1_NAME,
        "lineage": [{"taxonId": 287, "rank": "species", "scientificName": "Pseudomonas aeruginosa"}],
    }
    return entry, taxonomy


@pytest.mark.parametrize("locus", audit.LOCI)
@pytest.mark.parametrize("change", [
    "none", "accession", "reviewed", "version", "boolean_version", "gene", "duplicate_gene", "locus",
    "alias", "rank", "taxon", "inactive", "species", "species_name", "duplicate_species", "taxon_name",
    "protein_name", "no_embl", "embl_protein", "citation", "structure", "sequence", "features", "comments",
])
def test_explicit_reference_identity(locus, change):
    entry, taxonomy = metadata(locus)
    if change == "accession":
        entry["primaryAccession"] = "P00000"
    elif change == "reviewed":
        entry["entryType"] = "UniProtKB reviewed (Swiss-Prot)"
    elif change == "version":
        entry["entryAudit"]["entryVersion"] += 1
    elif change == "boolean_version":
        entry["entryAudit"]["sequenceVersion"] = True
    elif change == "gene":
        entry["genes"][0]["geneName"] = {"value": "INFERRED"}
    elif change == "duplicate_gene":
        entry["genes"].append(copy.deepcopy(entry["genes"][0]))
    elif change == "locus":
        entry["genes"][0]["orderedLocusNames"] = [{"value": "OTHER"}]
    elif change == "alias":
        entry["genes"][0]["synonyms"] = [{"value": "INFERRED"}]
    elif change == "rank":
        taxonomy["rank"] = "species"
    elif change == "taxon":
        entry["organism"]["taxonId"] = 287
    elif change == "inactive":
        taxonomy["active"] = False
    elif change == "species":
        taxonomy["lineage"][0]["taxonId"] = 1
    elif change == "species_name":
        taxonomy["lineage"][0]["scientificName"] = "OTHER"
    elif change == "duplicate_species":
        taxonomy["lineage"].append(copy.deepcopy(taxonomy["lineage"][0]))
    elif change == "taxon_name":
        entry["organism"]["scientificName"] = taxonomy["scientificName"] = "OTHER PAO1"
    elif change == "protein_name":
        entry["proteinDescription"] = {}
    elif change == "no_embl":
        entry["uniProtKBCrossReferences"] = []
    elif change == "embl_protein":
        entry["uniProtKBCrossReferences"][0]["properties"][0]["value"] = "OTHER"
    elif change == "citation":
        entry["references"][1]["citation"]["citationCrossReferences"][0]["id"] = "17720796"
    elif change == "structure":
        entry["references"][1]["evidences"] = []
    elif change in {"sequence", "features", "comments"}:
        entry[change] = "DO_NOT_EXPORT"
    if change != "none":
        with pytest.raises(ValueError):
            audit.project_locus(entry, taxonomy, locus)
        return
    result = audit.project_locus(entry, taxonomy, locus)
    assert result["protein_accession"] == "UniProtKB:" + audit.LOCI[locus][1]
    assert result["paper_gene_symbol_is_entry_gene_name"] is False
    assert result["experimental_allele_assignment"] is None
    assert result["experimental_genome_assignment"] is None
    assert result["experimental_subject_taxon_assignment"] is False
    assert result["new_resistance_assertion"] is False
    assert result["reference_taxon_id"] == "NCBITaxon:208964"
    assert result["species_taxon_id"] == "NCBITaxon:287"
    assert "DO_NOT_EXPORT" not in json.dumps(result)
    assert "referencePositions" not in json.dumps(result)


def test_unplanned_locus_cannot_be_assigned():
    entry, taxonomy = metadata()
    with pytest.raises(ValueError, match="unplanned"):
        audit.project_locus(entry, taxonomy, "opmH")


def structure():
    return {"data": {"entries": [{
        "rcsb_id": "6VEJ",
        "rcsb_accession_info": {"major_revision": 1, "minor_revision": 3,
                                "revision_date": "2024-10-23T00:00:00Z"},
        "rcsb_primary_citation": {"pdbx_database_id_PubMed": 32966762,
                                  "pdbx_database_id_DOI": "10.1016/j.str.2020.09.001", "year": 2021},
        "polymer_entities": [{
            "rcsb_id": "6VEJ_" + suffix,
            "rcsb_polymer_entity_container_identifiers": {"reference_sequence_identifiers": [
                {"database_name": "UniProt", "database_accession": accession} for accession in accessions]},
            "rcsb_entity_source_organism": [
                {"ncbi_taxonomy_id": 287, "scientific_name": "Pseudomonas aeruginosa"}
                for accession in accessions],
        } for suffix, accessions in [("2", ["Q9I6X5", "Q9I6X6"]), ("1", ["Q9I6X4"])]],
    }]}}


@pytest.mark.parametrize("change", [
    "none", "graphql_error", "no_entry", "duplicate_entry", "wrong_entry", "duplicate_entity",
    "single_representative", "other_species", "missing_source", "wrong_citation", "revision",
])
def test_structure_preserves_entity_granularity(change):
    payload = structure()
    entry = payload["data"]["entries"][0]
    entity = entry["polymer_entities"][0]
    if change == "graphql_error":
        payload["errors"] = [{"message": "Partial result"}]
    elif change == "no_entry":
        payload["data"]["entries"] = [None]
    elif change == "duplicate_entry":
        payload["data"]["entries"].append(copy.deepcopy(entry))
    elif change == "wrong_entry":
        entry["rcsb_id"] = "OTHER"
    elif change == "duplicate_entity":
        entry["polymer_entities"].append(copy.deepcopy(entity))
    elif change == "single_representative":
        entity["rcsb_polymer_entity_container_identifiers"]["reference_sequence_identifiers"].pop()
    elif change == "other_species":
        entity["rcsb_entity_source_organism"][0]["ncbi_taxonomy_id"] = 208964
    elif change == "missing_source":
        entity["rcsb_entity_source_organism"] = []
    elif change == "wrong_citation":
        entry["rcsb_primary_citation"]["pdbx_database_id_PubMed"] = 17720796
    elif change == "revision":
        entry["rcsb_accession_info"]["minor_revision"] += 1
    if change != "none":
        with pytest.raises(ValueError):
            audit.project_structure(payload)
        return
    result = audit.project_structure(payload)
    assert result["entities"][1]["reference_accessions"] == ["UniProtKB:Q9I6X5", "UniProtKB:Q9I6X6"]
    assert len(result["entities"][1]["source_organisms"]) == 2
    assert result["single_representative_selected"] is False
    assert result["entity_architecture_or_experimental_allele_inferred"] is False
    assert result["original_2007_subject_resolved"] is False


def test_checkpoint_has_no_new_resistance_or_experimental_assignments():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert len(result["references"]) == 3
    assert len(result["source_owned_assertions"]) == 10
    assert result["summary"]["corpus_records_in_scope"] == 2939
    assert result["summary"]["curated_resistance_assertions"] == 0
    assert result["summary"]["whole_record_primary_signoffs"] == 0
    assert result["primary"]["primary_results_figures_or_supplements_reviewed"] is False
    assert result["primary"]["individual_TriABC_symbol_mapping_inferred"] is False
    assert result["primary"]["full_text_status"] == "HTTP_403_HELD_NO_RETRY_OR_ALTERNATE_ROUTE"
    assert result["sources"]["held_pdf"]["status"] == 403
    assert result["limits"]["ncbi_requests"] == 0
    assert result["limits"]["issue_1040"] == "DEFERRED"
    assert result["limits"]["whole_record_primary_review"] == "OPEN"
    for key in ("opmh-reference", "opmh-species-reference"):
        query = result["queries"][key]
        assert query["result_count"] == 0
        assert query["complete_for_query"] is True
        assert query["zero_result_establishes_absence"] is False
        assert query["automatic_suggestions_followed"] is False


@pytest.mark.parametrize("change", ["none", "release", "taxonomy_release"])
def test_native_replay_offline(monkeypatch, change, pre_card_qualification_root):
    root = pre_card_qualification_root
    directory = root / audit.CACHE
    if not (directory / "pdb-6vej-response.bin").exists():
        pytest.skip("optional native research cache not present")

    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted networking")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    read = audit.reference.read_response

    def changed(root, directory, key, endpoint, parameters=None):
        payload, source = read(root, directory, key, endpoint, parameters)
        if (change == "release" and key == "pa0157-reference") or (
            change == "taxonomy_release" and key == "reference-tax-208964"
        ):
            source["release"] = "STALE"
        return payload, source

    monkeypatch.setattr(audit.reference, "read_response", changed)
    if change != "none":
        with pytest.raises(ValueError, match="release|taxonomy"):
            audit.build(root, directory)
        return
    payload = (
        json.dumps(audit.build(root, directory), indent=2, sort_keys=True, ensure_ascii=True) + "\n"
    ).encode()
    assert payload == (ROOT / audit.OUTPUT).read_bytes()


@pytest.mark.parametrize("change", ["none", "status", "retry", "url", "bytes", "redirect", "late", "body"])
def test_planned_native_cache_integrity(tmp_path, change):
    key = "triabc-primary-pdf"
    directory = ROOT / audit.CACHE
    if not (directory / (key + "-response.bin")).exists():
        pytest.skip("optional native research cache not present")
    for suffix in ("plan.json", "attempt.json", "receipt.json", "response.bin"):
        (tmp_path / (key + "-" + suffix)).write_bytes((directory / (key + "-" + suffix)).read_bytes())
    receipt_path = tmp_path / (key + "-receipt.json")
    receipt = json.loads(receipt_path.read_bytes())
    if change in {"status", "retry", "url", "bytes"}:
        key_name, value = {"status": ("status", 200), "retry": ("retry_performed", True),
                           "url": ("url", "https://example.com"), "bytes": ("bytes", 0)}[change]
        receipt[key_name] = value
        receipt_path.write_text(json.dumps(receipt))
    elif change == "redirect":
        path = tmp_path / (key + "-plan.json")
        plan = json.loads(path.read_bytes())
        plan["redirects_followed"] = True
        path.write_text(json.dumps(plan))
    elif change == "late":
        path = tmp_path / (key + "-attempt.json")
        attempt = json.loads(path.read_bytes())
        attempt["started_at"] = "2099-01-01T00:00:00+00:00"
        path.write_text(json.dumps(attempt))
    elif change == "body":
        (tmp_path / (key + "-response.bin")).write_bytes(b"CHANGED")
    if change != "none":
        with pytest.raises(ValueError):
            audit.planned_native(tmp_path, tmp_path, key, audit.PDF, (403,))
        return
    assert audit.planned_native(tmp_path, tmp_path, key, audit.PDF, (403,))["status"] == 403
