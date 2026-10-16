"""Deposited reference context cannot silently become an experimental allele."""

import builtins
import copy
import hashlib
import io
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_vmlr2_structure_context as audit  # noqa: E402

SPECIES = {"taxonId": 220686, "rank": "species", "scientificName": "Neobacillus vireti"}


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline structure audit attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket.socket, "connect_ex", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def saved():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def entries():
    current = {
        "primaryAccession": "CURRENT",
        "entryType": "UniProtKB unreviewed (TrEMBL)",
        "genes": [{"orfNames": [{"value": "locus"}]}],
        "extraAttributes": {"uniParcId": "UPI0003D5C4F7"},
    }
    old = {
        "primaryAccession": "HISTORICAL",
        "entryType": "Inactive",
        "extraAttributes": {"uniParcId": "UPI0003D5C4F7"},
    }
    return current, old


@pytest.mark.parametrize(
    "state",
    [
        "matching_orf",
        "matching_locus",
        "gene_name_only",
        "no_locus",
        "different_archive",
        "invalid_archive",
        "no_current_archive",
        "no_old_archive",
        "wrong_species",
        "missing_species",
    ],
)
def test_reference_crosswalk_needs_locus_archive_and_independent_species(state):
    current, old = entries()
    reference_species = SPECIES
    if state == "matching_locus":
        current["genes"] = [{"orderedLocusNames": [{"value": "locus"}]}]
    elif state == "gene_name_only":
        current["genes"] = [{"geneName": {"value": "locus"}}]
    elif state == "no_locus":
        current["genes"] = []
    elif state == "different_archive":
        old["extraAttributes"]["uniParcId"] = "UPI0000000000"
    elif state == "invalid_archive":
        old["extraAttributes"]["uniParcId"] = current["extraAttributes"]["uniParcId"] = "invalid"
    elif state == "no_current_archive":
        current.pop("extraAttributes")
    elif state == "no_old_archive":
        old.pop("extraAttributes")
    elif state == "wrong_species":
        reference_species = {**SPECIES, "taxonId": 1}
    elif state == "missing_species":
        reference_species = None
    result = audit.reference_link(current, old, "locus", SPECIES, reference_species)
    assert result["qualified_reference"] is state.startswith("matching_")
    assert result["official_accession_replacement_asserted"] is False
    assert result["engineered_entity_equated_to_reference"] is False
    assert result["experimental_donor_strain_assignment"] is False
    assert result["experimental_subject_assignment"] is result["exact_allele_assignment"] is False
    assert result["experimental_genome_assignment"] is None
    assert result["primary_resistance_validation"] is False


@pytest.mark.parametrize("which,state", [(0, "Inactive"), (0, "unknown"), (1, "active")])
def test_changed_reference_states_fail_closed(which, state):
    pair = entries()
    pair[which]["entryType"] = state
    with pytest.raises(ValueError, match="states"):
        audit.reference_link(*pair, "locus", SPECIES, SPECIES)


def structure_payload():
    source = saved()["structure"]
    return {
        "data": {
            "entries": [
                {
                    "rcsb_id": source["entry_id"],
                    "struct": {"title": source["title"]},
                    "rcsb_primary_citation": source["primary_citation"],
                    "polymer_entities": [source["focal_entity"]],
                }
            ]
        }
    }


def test_native_description_and_source_host_distinction_are_preserved():
    _, entity = audit.select_entity(structure_payload(), "220686", "36951104", "10.1093/nar/gkad193")
    assert entity["rcsb_polymer_entity"]["pdbx_description"] == "ExpZ"
    source = entity["entity_src_gen"][0]
    assert source["pdbx_gene_src_gene"] == "BAVI_03309"
    assert source["gene_src_strain"] is None
    assert source["pdbx_gene_src_ncbi_taxonomy_id"] == "220686"
    assert source["pdbx_host_org_ncbi_taxonomy_id"] == "224308"
    assert entity["entity_poly"]["rcsb_mutation_count"] > 0


@pytest.mark.parametrize(
    "mutation",
    [
        "graphql_error",
        "extra_entry",
        "wrong_title",
        "wrong_pmid",
        "wrong_doi",
        "duplicate_entity",
        "foreign_entity",
        "ambiguous_entity",
        "no_matching_source",
        "mixed_source",
        "renamed_source",
        "gene_source_disagrees",
        "boolean_mutation_count",
        "negative_mutation_count",
    ],
)
def test_structure_ambiguities_and_source_mismatches_fail_closed(mutation):
    payload = structure_payload()
    entry = payload["data"]["entries"][0]
    entity = entry["polymer_entities"][0]
    if mutation == "graphql_error":
        payload["errors"] = [{"message": "partial response"}]
    elif mutation == "extra_entry":
        payload["data"]["entries"].append(copy.deepcopy(entry))
    elif mutation == "wrong_title":
        entry["struct"]["title"] = "different"
    elif mutation == "wrong_pmid":
        entry["rcsb_primary_citation"]["pdbx_database_id_PubMed"] = 1
    elif mutation == "wrong_doi":
        entry["rcsb_primary_citation"]["pdbx_database_id_DOI"] = "different"
    elif mutation == "duplicate_entity":
        entry["polymer_entities"].append(copy.deepcopy(entity))
    elif mutation == "foreign_entity":
        entity["rcsb_id"] = "OTHER_51"
    elif mutation == "ambiguous_entity":
        second = copy.deepcopy(entity)
        second["rcsb_id"] = "8BUU_52"
        entry["polymer_entities"].append(second)
    elif mutation == "no_matching_source":
        entity["rcsb_entity_source_organism"][0]["ncbi_taxonomy_id"] = 224308
    elif mutation == "mixed_source":
        entity["rcsb_entity_source_organism"].append({"ncbi_taxonomy_id": 224308})
    elif mutation == "renamed_source":
        entity["rcsb_entity_source_organism"][0]["scientific_name"] = "different"
    elif mutation == "gene_source_disagrees":
        entity["entity_src_gen"][0]["pdbx_gene_src_ncbi_taxonomy_id"] = "224308"
    elif mutation == "boolean_mutation_count":
        entity["entity_poly"]["rcsb_mutation_count"] = True
    elif mutation == "negative_mutation_count":
        entity["entity_poly"]["rcsb_mutation_count"] = -1
    with pytest.raises(ValueError):
        audit.select_entity(payload, "220686", "36951104", "10.1093/nar/gkad193")


@pytest.mark.parametrize("field", sorted(audit.FORBIDDEN))
def test_operational_payload_is_rejected_even_when_nested(field):
    with pytest.raises(ValueError, match="unexpected"):
        audit.reject_operational_fields({"data": [{"nested": {field: []}}]})


@pytest.mark.parametrize("mutation", ["attempt", "receipt", "body", "error", "missing_receipt"])
def test_exact_request_history_is_required(tmp_path, mutation):
    for key in ("pdb-metadata", "uniprot-identifiers", "taxonomy-1131730"):
        for suffix in ("attempt", "receipt"):
            (tmp_path / f"{key}-{suffix}.json").write_text("{}")
    for key in ("pdb-metadata", "uniprot-identifiers"):
        (tmp_path / f"{key}-body.json").write_text("{}")
    audit.check_request_history(tmp_path)
    if mutation == "missing_receipt":
        (tmp_path / "taxonomy-1131730-receipt.json").unlink()
    else:
        (tmp_path / f"unexpected-{mutation}.json").write_text("{}")
    with pytest.raises(ValueError, match="unaccounted"):
        audit.check_request_history(tmp_path)


@pytest.mark.parametrize(
    "mutation", ["none", "plan", "status", "retry", "redirect", "link", "size", "negative_size"]
)
def test_request_receipts_require_frozen_plan_success_and_zero_retries(tmp_path, mutation):
    attempt = {"plan_sha256": "frozen", "url": "https://data.rcsb.org/graphql"}
    (tmp_path / "query-attempt.json").write_text(json.dumps(attempt))
    receipt = {
        **attempt,
        "status": 200,
        "retries": 0,
        "redirects_followed": 0,
        "headers": {},
        "bytes": 10,
    }
    if mutation == "plan":
        receipt["plan_sha256"] = "different"
    elif mutation == "status":
        receipt["status"] = 403
    elif mutation == "retry":
        receipt["retries"] = 1
    elif mutation == "redirect":
        receipt["redirects_followed"] = 1
    elif mutation == "link":
        receipt["headers"]["link"] = "next"
    elif mutation == "size":
        receipt["bytes"] = 101
    elif mutation == "negative_size":
        receipt["bytes"] = -1
    path = tmp_path / "query-receipt.json"
    path.write_text(json.dumps(receipt))
    args = (tmp_path, tmp_path, "query", audit.reference.pin(tmp_path, path), {"sha256": "frozen"}, 100)
    if mutation == "none":
        assert audit.request_receipt(*args)[0] == receipt
    else:
        with pytest.raises(ValueError, match="request history"):
            audit.request_receipt(*args)


@pytest.mark.parametrize("mutation", ["none", "hash", "provider", "doi", "duplicate"])
def test_publication_metadata_is_identifier_bound(mutation):
    row = saved()["publication_metadata"]
    if mutation == "doi":
        row["doi"] = "different"
    body = json.dumps({"resultList": {"result": [row, row] if mutation == "duplicate" else [row]}})
    wrapper = {
        "status": 200,
        "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/search",
        "body": body,
        "sha256": hashlib.sha256(body.encode()).hexdigest(),
    }
    if mutation == "hash":
        wrapper["sha256"] = "invalid"
    elif mutation == "provider":
        wrapper["url"] = "https://unverified.example/"
    if mutation == "none":
        assert audit.publication_metadata(wrapper) == row
    else:
        with pytest.raises(ValueError):
            audit.publication_metadata(wrapper)


def test_claim_pointers_resolve_and_coverage_remains_bounded():
    d = saved()
    for claim in d["claims"]:
        node = d
        for key in claim["term_pointer"].lstrip("/").split("/"):
            node = node[key]
        assert node["aro_id"] == claim["aro_id"]
        assert claim["record_identifier"] in node["record_memberships"]
    assert d["summary"]["complete_records_read"] == d["summary"]["source_claims"] == 6
    assert d["summary"]["combined_qualified_terms"] == 105
    assert d["summary"]["combined_remaining_terms"] == 73
    assert d["coverage"]["new_qualified_terms"] == ["ARO:3007646"]
    assert d["coverage"]["whole_corpus_completion"] is False
    assert d["summary"]["ncbi_requests"] == d["summary"]["biological_record_writes"] == 0


def test_native_reference_scope_keeps_access_hold_and_missing_experimental_identifiers():
    d = saved()
    term = d["terms"]["ARO:3007646"]
    assert term["qualified_reference_accessions"] == ["UniProtKB:A0AB94ITE9"]
    assert term["whole_record_primary_review"] == "OPEN"
    assert term["reference_link"]["exact_allele_assignment"] is False
    assert term["reference_link"]["native_locus_or_orf_matches"] == [
        {"field": "genes/0/orfNames/0", "value": "BAVI_03309"}
    ]
    assert d["structure"]["entity_count_inspected"] == 51
    assert d["structure"]["focal_entity_selection_is_documented_inference"] is True
    assert d["structure"]["engineered_entity_is_reference_protein_or_resistant_allele"] is False
    assert d["primary_access_review"]["primary_document_review"] == "NOT_COMPLETED_ACCESS_HELD"
    assert d["primary_access_review"]["alternate_article_copies_requested_after_denial"] == 0
    assert d["native_pdb_cross_references_in_current_response"] == []
    assert d["summary"]["new_primary_results_reviews"] == 0
    assert d["reused_gene_query"]["headers"]["x-total-results"] == "0"
    assert d["reused_gene_query"]["empty_result_means_biological_absence"] is False
    assert d["reused_own_citation_query"]["result_count"] == 0
    assert any("not biological absence" in limit for limit in d["limits"])
    audit.reject_operational_fields(d)


def test_offline_replay_is_read_only(monkeypatch, pre_cdsa_qualification_root):
    d = saved()
    plan = json.loads((ROOT / audit.PLAN).read_bytes())
    if not (ROOT / plan["inputs"]["canary"]["path"]).exists():
        pytest.skip("ignored native cache unavailable; portable artifact tests still run")

    def guard(original):
        def read_only(file, mode="r", *args, **kwargs):
            assert not any(c in mode for c in "wax+"), "audit attempted file mutation"
            return original(file, mode, *args, **kwargs)

        return read_only

    monkeypatch.setattr(builtins, "open", guard(builtins.open))
    monkeypatch.setattr(io, "open", guard(io.open))
    assert audit.build(pre_cdsa_qualification_root) == d


def test_cli_nested_output_is_immutable(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "build", lambda root: {"summary": {}})
    output = tmp_path / "nested" / "audit.json"
    monkeypatch.setattr(sys, "argv", ["audit", "--root", str(tmp_path), "--output", str(output)])
    audit.main()
    audit.main()
    output.write_text("{}")
    with pytest.raises(ValueError, match="differs"):
        audit.main()
    assert output.read_text() == "{}"


def test_cli_check_cannot_create_output(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "build", lambda root: {"summary": {}})
    output = tmp_path / "missing" / "audit.json"
    monkeypatch.setattr(sys, "argv", ["audit", "--root", str(tmp_path), "--output", str(output), "--check"])
    with pytest.raises(FileNotFoundError):
        audit.main()
    assert not output.parent.exists()
