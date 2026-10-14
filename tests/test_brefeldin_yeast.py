"""Species-scoped Bfr1 names are references, not interchangeable tested alleles."""

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
import audit_brefeldin_yeast as audit  # noqa: E402


def fixture(key):
    expected = audit.IDENTITIES[key]
    taxonomy = {"taxonId": expected["taxon"], "rank": "strain", "active": True,
                "scientificName": expected["species_name"] + " reference",
                "lineage": [{"taxonId": expected["species"], "rank": "species",
                             "scientificName": expected["species_name"]}]}
    selected = expected["selected_pmids"] if key == "pombe-bfr1" else ["8070655"]
    entry = {
        "primaryAccession": expected["accession"], "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "entryAudit": {"entryVersion": expected["entry_version"],
                       "sequenceVersion": expected["sequence_version"]},
        "organism": {"taxonId": expected["taxon"], "scientificName": taxonomy["scientificName"]},
        "genes": [{"geneName": {"value": expected["gene"]},
                   "orderedLocusNames": [{"value": name} for name in expected["ordered_loci"]],
                   "orfNames": [{"value": name} for name in expected["orf_names"]]}],
        "proteinDescription": {"recommendedName": {"fullName": {"value": "Reference protein"}}},
        "references": [{"referenceNumber": i + 1,
                        "citation": {"title": "Example", "citationCrossReferences": [
                            {"database": "PubMed", "id": pmid}]},
                        "referenceComments": [{"type": "STRAIN", "value": "Study / label"}],
                        "referencePositions": ["UNEXPORTED ROLE"]} for i, pmid in enumerate(selected)],
    }
    return entry, taxonomy


def test_same_symbol_does_not_merge_species_or_convert_orf_names_to_ordered_loci():
    proteins = {key: audit.project(entry, key, taxonomy)
                for key in audit.IDENTITIES for entry, taxonomy in [fixture(key)]}
    budding, fission = proteins["cerevisiae-bfr1"], proteins["pombe-bfr1"]
    assert budding["source_symbol"].casefold() == fission["source_symbol"].casefold()
    assert budding["protein_accession"] != fission["protein_accession"]
    assert budding["source_species_taxon_id"] == "NCBITaxon:4932"
    assert fission["source_species_taxon_id"] == "NCBITaxon:4896"
    assert budding["ordered_locus_names"] == ["YOR198C"] and budding["reference_orf_names"] == []
    assert fission["ordered_locus_names"] == []
    assert fission["reference_orf_names"] == ["SPCC18B5.01c", "SPCPJ732.04c"]
    for protein in proteins.values():
        assert protein["exact_resistance_allele"] is False
        assert protein["experimental_subject_assignment"] is False
        assert protein["experimental_genome_assignment"] is None
        assert protein["resistant_phenotype_inferred_from_protein_name"] is False
    assert budding["selected_pmids_not_in_returned_bibliography"] == ["11410665"]
    assert budding["missing_citation_proves_no_relationship"] is False


@pytest.mark.parametrize("change", ["accession", "organism", "species", "species_name", "taxon_name",
                                    "rank", "inactive", "version", "boolean_version", "sequence_version",
                                    "gene", "duplicate_gene", "orf", "orf_to_ordered", "ordered_locus",
                                    "sequence", "features", "comments", "citation"])
def test_reference_identity_scope_guards(change):
    key = "pombe-bfr1"
    entry, taxonomy = fixture(key)
    if change == "accession":
        entry["primaryAccession"] = "P38934"
    elif change == "organism":
        entry["organism"]["taxonId"] = 559292
    elif change == "species":
        taxonomy["lineage"][0]["taxonId"] = 4932
    elif change == "species_name":
        taxonomy["lineage"][0]["scientificName"] = "Saccharomyces cerevisiae"
    elif change == "taxon_name":
        taxonomy["scientificName"] = "Different"
    elif change == "rank":
        taxonomy["rank"] = "no rank"
    elif change == "inactive":
        taxonomy["active"] = False
    elif change == "version":
        entry["entryAudit"]["entryVersion"] += 1
    elif change == "boolean_version":
        entry["entryAudit"]["entryVersion"] = True
    elif change == "sequence_version":
        entry["entryAudit"]["sequenceVersion"] += 1
    elif change == "gene":
        entry["genes"][0]["geneName"]["value"] = "different"
    elif change == "duplicate_gene":
        entry["genes"] *= 2
    elif change == "orf":
        entry["genes"][0]["orfNames"].pop()
    elif change == "orf_to_ordered":
        entry["genes"][0]["orderedLocusNames"] = entry["genes"][0].pop("orfNames")
    elif change == "ordered_locus":
        entry["genes"][0]["orderedLocusNames"] = [{"value": "YOR198C"}]
    elif change in {"sequence", "features", "comments"}:
        entry[change] = []
    else:
        entry["references"].pop()
    with pytest.raises(ValueError):
        audit.project(entry, key, taxonomy)


def test_citation_strain_labels_are_not_split_or_promoted_to_subject_identity():
    entry, _ = fixture("pombe-bfr1")
    contexts = audit.citation_contexts(entry, ["7646493"])
    assert len(contexts) == 1 and contexts[0]["reference_number"] == 2
    assert contexts[0]["study_strain_annotations"] == ["Study / label"]
    assert contexts[0]["experimental_subject_assignment"] is False
    assert contexts[0]["primary_results_reviewed"] is False
    assert "UNEXPORTED ROLE" not in json.dumps(contexts)
    assert "referencePositions" not in json.dumps(contexts)


@pytest.mark.parametrize("number", [1, True, 0])
def test_duplicate_or_invalid_citation_number_is_rejected(number):
    entry, _ = fixture("pombe-bfr1")
    entry["references"][1]["referenceNumber"] = number
    with pytest.raises(ValueError):
        audit.citation_contexts(entry, ["7646493"])


@pytest.mark.parametrize("change", ["none", "url", "plan_digest", "status", "body_digest", "retry",
                                    "redirect"])
def test_native_access_hold_is_pinned_not_retried_or_promoted(tmp_path, change):
    key = "bfr1-cerevisiae-primary"
    url = audit.FIXED_URLS[key]
    plan = {"requests": {key: {"url": url}}}
    if change == "url":
        plan["requests"][key]["url"] = "https://www.ncbi.nlm.nih.gov/"
    path = tmp_path / "plan.json"
    path.write_text(json.dumps(plan))
    attempt = {"url": url, "plan_sha256": audit.reference.digest(path)}
    body = b"technical response"
    receipt = {"url": url, "status": 500, "retry_performed": False, "redirects_followed": False,
               "sha256": hashlib.sha256(body).hexdigest(), "bytes": len(body), "retrieved_at": "2026-10-14"}
    if change == "plan_digest":
        attempt["plan_sha256"] = "0" * 64
    elif change == "status":
        receipt["status"] = 200
    elif change == "body_digest":
        receipt["sha256"] = "0" * 64
    elif change == "retry":
        receipt["retry_performed"] = True
    elif change == "redirect":
        receipt["redirects_followed"] = True
    (tmp_path / (key + "-attempt.json")).write_text(json.dumps(attempt))
    (tmp_path / (key + "-receipt.json")).write_text(json.dumps(receipt))
    (tmp_path / (key + "-response.bin")).write_bytes(body)
    if change == "none":
        assert audit.planned_source(tmp_path, tmp_path, key, "plan.json", (500,))["status"] == 500
    else:
        with pytest.raises(ValueError):
            audit.planned_source(tmp_path, tmp_path, key, "plan.json", (500,))


def test_public_checkpoint_keeps_reference_and_primary_review_boundaries():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert result["record"]["identifier"] == "CHEBI:48080"
    assert result["record"]["standard_inchi_key"] == "KQNZDYYTLMIZCT-KQPMLPITSA-N"
    assert len(result["proteins"]) == 2
    assert result["identity_decisions"]["whole_record_primary_review"] == "OPEN"
    assert result["limits"]["biological_changes"] == result["limits"]["whole_record_primary_signoffs"] == 0
    assert result["limits"]["new_experimental_allele_or_genome_assignments"] == 0
    assert result["limits"]["ncbi_requests"] == 0 and result["limits"]["issue_1040"] == "DEFERRED"
    assert result["primary_status"]["PMID:11410665"].startswith("TECHNICAL_HTTP_500")
    assert result["primary_status"]["PMID:8070655"].startswith("PUBLISHER_HTTP_403")
    assert all(result["primary_status"][key] == "NOT_REQUESTED_AFTER_EBI_CANARY_FAILURE"
               for key in ("PMID:7883711", "PMID:7646493"))
    budding = result["proteins"]["cerevisiae-bfr1"]
    assert budding["selected_citation_contexts"][0]["study_strain_annotations"] == [
        "ATCC 28383 / FL100 / VTT C-80102"]


def test_offline_native_replay_does_not_read_mutable_live_record(monkeypatch):
    if not (ROOT / audit.CACHE / "cohort.json").exists():
        pytest.skip("optional native research cache not available")

    def denied(*args, **kwargs):
        raise AssertionError("offline Bfr1 replay attempted network access")

    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(Path, "open", guarded)
    monkeypatch.chdir(ROOT)
    monkeypatch.setattr(sys, "argv", ["audit_brefeldin_yeast.py", "--check"])
    audit.main()


def test_unrelated_study_context_is_not_selected():
    entry, _ = fixture("cerevisiae-bfr1")
    unrelated = copy.deepcopy(entry["references"][0])
    unrelated["referenceNumber"] = 9
    unrelated["citation"]["citationCrossReferences"][0]["id"] = "999999"
    entry["references"].append(unrelated)
    assert len(audit.citation_contexts(entry, ["8070655"])) == 1


@pytest.mark.parametrize("change", ["none", "candidate_id", "title", "source_digest", "body_digest",
                                    "status", "host", "duplicate", "no_source"])
def test_discovery_candidates_bind_to_successful_native_cache(tmp_path, change):
    metadata = {"source": "MED", "id": "1", "title": "Example", "doi": "10.1/example"}
    rows = [copy.deepcopy(metadata)]
    if change == "duplicate":
        rows *= 2
    body = json.dumps({"resultList": {"result": rows}})
    receipt = {"url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=example",
               "status": 200, "body": body, "sha256": hashlib.sha256(body.encode()).hexdigest()}
    if change == "body_digest":
        receipt["sha256"] = "0" * 64
    elif change == "status":
        receipt["status"] = 500
    elif change == "host":
        receipt["url"] = "https://www.ncbi.nlm.nih.gov/search"
    path = tmp_path / "response.json"
    path.write_text(json.dumps(receipt))
    pin = audit.reference.pin(tmp_path, path)
    if change == "source_digest":
        pin["sha256"] = "0" * 64
    elif change == "candidate_id":
        metadata["id"] = "2"
    elif change == "title":
        metadata["title"] = "Other"
    discovery = {"candidates": {"MED:1": {"metadata": metadata, "sources": [pin]}}}
    if change == "no_source":
        discovery["candidates"]["MED:1"]["sources"] = []
    if change == "none":
        assert audit.validate_discovery(tmp_path, discovery) == 1
    else:
        with pytest.raises(ValueError):
            audit.validate_discovery(tmp_path, discovery)
