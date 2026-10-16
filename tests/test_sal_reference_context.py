"""Adversarial tests for Sal reference identity, independent of ignored caches."""

import copy
import hashlib
import json
import socket
import sys
from pathlib import Path
from urllib.parse import urlencode

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_sal_reference_context as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline Sal audit attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)


@pytest.fixture
def checkpoint():
    return json.loads((ROOT / (audit.PREFIX + ".json")).read_bytes())


def test_public_checkpoint_memberships_and_scope(checkpoint):
    assert checkpoint["counts"] == {
        "current_corpus_hashes_checked": 2939,
        "complete_records_loaded": 5,
        "card_claims": 16,
        "terms": 4,
        "species_name_references": 4,
        "current_uniprot_crosswalks": 1,
        "inactive_deposited_accessions": 1,
    }
    index = json.loads((ROOT / "research/2026-10-15-card-current-references.json").read_bytes())
    rows, claims = audit.bind_current(ROOT, index)
    assert rows == checkpoint["records"] and claims == checkpoint["claims"]
    for term, row in checkpoint["terms"].items():
        assert (
            sorted(c["record_identifier"] for c in claims if c["aro_id"] == term) == row["record_memberships"]
        )
        assert row["experimental_allele_assignment"] is None
        assert row["experimental_strain_taxon_assignment"] is None
        assert row["whole_record_primary_review"] == "OPEN"
    assert checkpoint["constraints"]["ncbi_requests"] == 0
    assert checkpoint["constraints"]["issue_1040"] == "DEFERRED"
    assert checkpoint["constraints"]["full_corpus_goal"] == "OPEN"


def test_deleted_pdb_accession_and_ribosomes_not_selected(checkpoint):
    structure = checkpoint["structure"]
    assert structure["deposited_accession_current_status"]["entryType"] == "Inactive"
    assert structure["selected_current_reference"] is None
    assert structure["mutation_count_proves_wild_type"] is False
    assert checkpoint["prior_citation_pool"]["selected_sal_accessions"] == []
    assert checkpoint["prior_citation_pool"]["entries"] == 42
    assert (
        checkpoint["terms"]["ARO:3007028"]["reference_candidates"][0]["accession"] == "UniProtKB:A0ABQ0Y1N0"
    )
    assert all(
        not checkpoint["terms"][term]["reference_candidates"]
        for key, term in audit.TERMS.items()
        if key != "sald"
    )


@pytest.fixture
def species():
    return {
        "taxonId": 42858,
        "scientificName": "Mammaliicoccus lentus",
        "synonyms": ["Staphylococcus lentus"],
        "rank": "species",
        "active": True,
        "parent": {"taxonId": 2803850},
        "lineage": [],
    }


@pytest.mark.parametrize("field", ["synonyms", "otherNames"])
def test_native_alias_requires_exact_field(species, field):
    species[field] = species.pop("synonyms")
    result = audit.species_context([species], "Staphylococcus lentus")
    assert result["taxon_id"] == "NCBITaxon:42858"
    assert result["native_name_matches"] == [{"field": field, "value": "Staphylococcus lentus"}]
    assert result["scope"] == "SPECIES_NAME_REFERENCE_NOT_EXPERIMENTAL_ISOLATE"


@pytest.mark.parametrize("change", ["inactive", "rank", "prefix", "duplicate", "different"])
def test_taxonomy_rejects_unsupported_equivalence(species, change):
    entries = [species]
    if change == "inactive":
        species["active"] = False
    elif change == "rank":
        species["rank"] = "strain"
    elif change == "prefix":
        species["synonyms"] = ["Staphylococcus lentus strain B3"]
    elif change == "duplicate":
        entries.append(copy.deepcopy(species))
    else:
        species["synonyms"] = ["Different species"]
    with pytest.raises(ValueError):
        audit.species_context(entries, "Staphylococcus lentus")


@pytest.fixture
def refseq_entry():
    return {
        "primaryAccession": "EXAMPLE",
        "entryType": "UniProtKB unreviewed (TrEMBL)",
        "entryAudit": {"entryVersion": 4, "sequenceVersion": 1},
        "organism": {"taxonId": 1293, "scientificName": "Staphylococcus gallinarum"},
        "uniProtKBCrossReferences": [{"database": "RefSeq", "id": "WP_082039181.1"}],
    }


def test_exact_native_refseq_supports_reference_only(refseq_entry):
    (candidate,) = audit.refseq_candidates([refseq_entry], "WP_082039181.1", 1293)
    assert candidate["experimental_strain_assignment"] is None
    assert candidate["versions"] == {"entryVersion": 4, "sequenceVersion": 1}


@pytest.mark.parametrize("change", ["version", "database", "species", "inactive", "missing"])
def test_refseq_query_hit_is_not_enough(refseq_entry, change):
    if change == "version":
        refseq_entry["uniProtKBCrossReferences"][0]["id"] = "WP_082039181.2"
    elif change == "database":
        refseq_entry["uniProtKBCrossReferences"][0]["database"] = "EMBL"
    elif change == "species":
        refseq_entry["organism"]["taxonId"] = 1280
    elif change == "inactive":
        refseq_entry["entryType"] = "Inactive"
    else:
        refseq_entry["uniProtKBCrossReferences"] = []
    assert audit.refseq_candidates([refseq_entry], "WP_082039181.1", 1293) == []


@pytest.fixture
def structure(checkpoint):
    context = checkpoint["structure"]
    return [
        {
            "rcsb_id": "7P48",
            "rcsb_primary_citation": context["citation"],
            "rcsb_accession_info": context["revision"],
            "polymer_entities": [
                copy.deepcopy(context["focal_entity"]),
                {
                    "rcsb_id": "7P48_1",
                    "rcsb_polymer_entity_container_identifiers": {
                        "reference_sequence_identifiers": [
                            {"database_name": "UniProt", "database_accession": "RIBOSOME"}
                        ]
                    },
                },
            ],
        }
    ]


def test_structure_reference_is_component_specific(structure):
    result = audit.focal_structure(structure)
    assert result["ribosomal_entities_not_assigned"] == 1
    assert result["experimental_allele_assignment"] is None
    assert result["mutation_count_proves_wild_type"] is False


@pytest.mark.parametrize("change", ["paper", "entity", "host", "source", "locus", "xref", "duplicate"])
def test_structure_rejects_wrong_context(structure, change):
    entry = structure[0]
    entity = entry["polymer_entities"][0]
    if change == "paper":
        entry["rcsb_primary_citation"]["pdbx_database_id_PubMed"] = 1
    elif change == "entity":
        entity["rcsb_id"] = "7P48_7"
    elif change == "host":
        entity["entity_src_gen"][0]["pdbx_host_org_ncbi_taxonomy_id"] = "42858"
    elif change == "source":
        entity["entity_src_gen"][0]["pdbx_gene_src_ncbi_taxonomy_id"] = "1280"
    elif change == "locus":
        entity["entity_src_gen"][0]["pdbx_gene_src_gene"] = "H3V22_031700"
    elif change == "xref":
        entity["rcsb_polymer_entity_container_identifiers"]["reference_sequence_identifiers"] = []
    else:
        entry["polymer_entities"].append(copy.deepcopy(entity))
    with pytest.raises(ValueError):
        audit.focal_structure(structure)


@pytest.fixture
def response():
    query = audit.QUERIES["salb"]
    fields = audit.reference.FIELDS
    url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(
        {"query": query, "format": "json", "size": "500", "fields": fields}
    )
    plan = {
        "requests": {"salb": {"query": query, "url": url}},
        "release": "2026_03",
        "max_bytes": 10000,
        "fields": fields,
    }
    attempt = {"url": url, "key": "salb", "retries": 0, "redirects_followed": 0}
    body = json.dumps({"results": [], "suggestions": [{"query": "gene_exact:similar", "hits": 1}]}).encode()
    receipt = {
        **attempt,
        "status": 200,
        "bytes": len(body),
        "body": {"sha256": hashlib.sha256(body).hexdigest()},
        "headers": {
            "x-uniprot-release": "2026_03",
            "content-type": "application/json",
            "x-total-results": "0",
        },
    }
    return plan, "salb", receipt, attempt, body


def test_suggestions_not_selected(response):
    entries, suggestions = audit.validate_response(*response)
    assert entries == [] and len(suggestions) == 1


@pytest.mark.parametrize(
    "change", ["denial", "pagination", "release", "count", "hash", "redirect", "retry", "domain", "fields"]
)
def test_response_integrity(response, change):
    plan, key, receipt, attempt, body = response
    if change == "denial":
        receipt["status"] = 403
    elif change == "pagination":
        receipt["headers"]["link"] = "next"
    elif change == "release":
        receipt["headers"]["x-uniprot-release"] = "different"
    elif change == "count":
        receipt["headers"]["x-total-results"] = "1"
    elif change == "hash":
        receipt["body"]["sha256"] = "changed"
    elif change == "redirect":
        receipt["headers"]["location"] = "https://example.com"
    elif change == "retry":
        attempt["retries"] = 1
    elif change == "domain":
        plan["requests"][key]["url"] = plan["requests"][key]["url"].replace("rest.uniprot.org", "example.com")
    else:
        plan["fields"] += ",sequence"
    with pytest.raises(ValueError):
        audit.validate_response(plan, key, receipt, attempt, body)


@pytest.mark.parametrize(
    "key", ["sequence", "features", "comments", "pdbx_seq_one_letter_code", "entity_poly_seq"]
)
def test_nested_nonmetadata_rejected(key):
    with pytest.raises(ValueError, match="non-metadata"):
        audit.metadata_only({"data": [{"entity": {key: "not permitted"}}]})


def test_duplicate_results_rejected(response):
    plan, key, receipt, attempt, _ = response
    body = json.dumps({"results": [{"primaryAccession": "EXAMPLE"}] * 2}).encode()
    receipt["bytes"] = len(body)
    receipt["body"]["sha256"] = hashlib.sha256(body).hexdigest()
    receipt["headers"]["x-total-results"] = "2"
    with pytest.raises(ValueError, match="duplicate"):
        audit.validate_response(plan, key, receipt, attempt, body)
