"""Source-name taxonomy must not rewrite gene identity or experimental scope."""

import copy
import csv
import hashlib
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_demethylase_taxa as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("network forbidden in taxonomy audit tests")

    monkeypatch.setattr(requests.sessions.Session, "request", forbidden)
    monkeypatch.setattr(socket.socket, "connect", forbidden)
    monkeypatch.setattr(socket, "create_connection", forbidden)


@pytest.fixture
def taxon():
    parent = {"taxonId": 4751, "scientificName": "Fungi", "rank": "kingdom"}
    return {
        "taxonId": 123,
        "scientificName": "Synthetic fungus",
        "rank": "species",
        "active": True,
        "synonyms": ["Earlier name"],
        "otherNames": ["Other name"],
        "lineage": [parent],
        "parent": parent,
    }


@pytest.mark.parametrize(
    ("label", "name", "gene", "kind"),
    [
        ("Candida albicans ERG11 with mutations", "Candida albicans", "ERG11", "BINOMIAL"),
        ("Aspergillus flavus Cyp51B with mutations", "Aspergillus flavus", "Cyp51B", "BINOMIAL"),
        ("Aspergillus flavus Cyp51c with mutations", "Aspergillus flavus", "Cyp51c", "BINOMIAL"),
        (
            "Pyricularia graminis-tritici Cyp51A with mutations",
            "Pyricularia graminis-tritici",
            "Cyp51A",
            "BINOMIAL",
        ),
        (
            "Blumeria graminis f. sp. hordei cyp51 with mutations",
            "Blumeria graminis f. sp. hordei",
            "cyp51",
            "QUALIFIED_NAME",
        ),
        ("Candida spp. ERG11 with mutations", "Candida spp.", "ERG11", "GENUS_GROUP"),
    ],
)
def test_source_parsing_retains_gene_paralog_case_and_organism_scope(label, name, gene, kind):
    result = audit.source_identity(label)
    assert result == {
        "source_organism_name": name,
        "source_gene_label": gene,
        "source_name_kind": kind,
        "source_claim_wording": "with mutations",
    }


@pytest.mark.parametrize(
    "label",
    [
        "Candida albicans FKS1 with mutations",
        "Candida ERG11 with mutations",
        "Unknown spp. ERG11 with mutations",
        "Candida albicans ERG11",
        "Blumeria graminis f. sp. other CYP51 with mutations",
    ],
)
def test_unreviewed_source_syntax_is_not_guessed(label):
    with pytest.raises(ValueError):
        audit.source_identity(label)


def test_name_matches_have_no_experimental_or_allele_assignment(taxon):
    result = audit.resolve_name(taxon, "Synthetic fungus", "BINOMIAL")
    assert result["status"] == "EXACT_NATIVE_NAME_REFERENCE"
    assert result["selected_taxon"]["taxon_id"] == "NCBITaxon:123"
    assert result["selected_taxon"]["matching_fields"] == ["scientificName"]
    assert result["selected_taxon"]["species_ancestor"]["taxonId"] == 123
    assert result["experimental_subject_assignment"] is False
    assert result["protein_or_allele_assignment"] is None
    assert result["unresolved_name_is_biological_absence"] is False
    synonym = audit.resolve_name(taxon, "Earlier name", "BINOMIAL")
    assert synonym["selected_taxon"]["matching_fields"] == ["synonyms"]


@pytest.mark.parametrize(
    "name", ["Other name", "Synthetic", "synthetic fungus", "Earlier", "Unmatched fungus"]
)
def test_othernames_substrings_case_and_unmatched_names_do_not_resolve(taxon, name):
    result = audit.resolve_name(taxon, name, "BINOMIAL")
    assert result["selected_taxon"] is None
    assert result["status"] == "NO_EXACT_ACTIVE_NAME_AT_SUPPORTED_RANK"
    assert result["candidates"][0]["other_name_match_only"] is (name == "Other name")


def test_qualified_name_requires_its_own_exact_match(taxon):
    name = "Blumeria graminis f. sp. hordei"
    taxon["scientificName"] = "Blumeria hordei"
    taxon["synonyms"] = [name]
    result = audit.resolve_name(taxon, name, "QUALIFIED_NAME")
    assert result["selected_taxon"]["matching_fields"] == ["synonyms"]
    assert result["selected_taxon"]["scientific_name"] == "Blumeria hordei"
    assert audit.resolve_name(taxon, "Blumeria graminis", "BINOMIAL")["selected_taxon"] is None
    taxon["rank"] = "genus"
    assert audit.resolve_name(taxon, name, "QUALIFIED_NAME")["selected_taxon"] is None


def test_species_and_strain_are_not_interchangeable(taxon):
    species = {"taxonId": 124, "scientificName": "Parent fungus", "rank": "species"}
    taxon["lineage"].append(species)
    taxon["parent"] = species
    taxon["rank"] = "strain"
    assert audit.resolve_name(taxon, "Synthetic fungus", "BINOMIAL")["selected_taxon"] is None
    qualified = audit.resolve_name(taxon, "Synthetic fungus", "QUALIFIED_NAME")
    assert qualified["selected_taxon"]["rank"] == "strain"
    assert qualified["selected_taxon"]["species_ancestor"]["taxonId"] == 124


def test_ambiguity_empty_results_and_inactive_nodes_are_explicit(taxon):
    second = copy.deepcopy(taxon)
    second["taxonId"] = 125
    result = audit.resolve_name({"results": [taxon, second]}, "Synthetic fungus", "BINOMIAL")
    assert result["status"] == "AMBIGUOUS_EXACT_NATIVE_NAMES"
    assert result["selected_taxon"] is None
    assert result["exact_match_count"] == 2
    result = audit.resolve_name({"results": []}, "Synthetic fungus", "BINOMIAL")
    assert result["result_count"] == 0 and result["selected_taxon"] is None
    taxon["active"] = False
    assert audit.resolve_name(taxon, "Synthetic fungus", "BINOMIAL")["selected_taxon"] is None


@pytest.mark.parametrize(
    "change",
    [
        "taxid",
        "boolean_taxid",
        "name",
        "active",
        "rank",
        "synonyms",
        "othernames",
        "duplicate",
        "lineage",
        "parent",
        "fungal_lineage",
        "genus_group",
    ],
)
def test_taxonomy_identity_guards(taxon, change):
    payload, kind = taxon, "BINOMIAL"
    if change == "taxid":
        taxon["taxonId"] = -1
    elif change == "boolean_taxid":
        taxon["taxonId"] = True
    elif change == "name":
        taxon["scientificName"] = ""
    elif change == "active":
        taxon["active"] = "true"
    elif change == "rank":
        taxon["rank"] = ""
    elif change == "synonyms":
        taxon["synonyms"] = "Earlier name"
    elif change == "othernames":
        taxon["otherNames"] = [None]
    elif change == "duplicate":
        payload = {"results": [taxon, copy.deepcopy(taxon)]}
    elif change == "lineage":
        taxon["lineage"] = None
    elif change == "parent":
        taxon["parent"] = {"taxonId": 1, "scientificName": "Other"}
    elif change == "fungal_lineage":
        taxon["lineage"][0]["taxonId"] = 2
    else:
        kind = "GENUS_GROUP"
    with pytest.raises(ValueError):
        audit.resolve_name(payload, "Synthetic fungus", kind)


@pytest.mark.parametrize(
    "change", [None, "status", "redirect", "retry", "hash", "release", "pagination", "count", "url", "plan"]
)
def test_native_request_provenance_and_completeness(tmp_path, taxon, change):
    directory = tmp_path / "cache"
    directory.mkdir()
    key = "canary"
    url = audit.query_url("Synthetic fungus", "BINOMIAL")
    plan = {"requests": {key: {"url": url, "name": "Synthetic fungus", "kind": "BINOMIAL"}}}
    plan_path = directory / "taxonomy-plan.json"
    plan_path.write_text(json.dumps(plan))
    body_path = directory / "canary-response.bin"
    body_path.write_text(json.dumps({"results": [taxon]}))
    receipt = {
        "url": url,
        "status": 200,
        "bytes": body_path.stat().st_size,
        "sha256": audit.reference.digest(body_path),
        "retrieved_at": "2026-10-14T00:00:00Z",
        "retry_performed": False,
        "redirects_followed": False,
        "headers": {"X-Total-Results": "1", "X-UniProt-Release": "2026_03"},
    }
    attempt = {"url": url, "plan_sha256": audit.reference.digest(plan_path), "retry_performed": False}
    if change == "status":
        receipt["status"] = 500
    elif change == "redirect":
        receipt["redirects_followed"] = True
    elif change == "retry":
        receipt["retry_performed"] = True
    elif change == "hash":
        receipt["sha256"] = "wrong"
    elif change == "release":
        receipt["headers"]["X-UniProt-Release"] = "other"
    elif change == "pagination":
        receipt["headers"]["Link"] = "next"
    elif change == "count":
        receipt["headers"]["X-Total-Results"] = "2"
    elif change == "url":
        receipt["url"] = "https://www.ncbi.nlm.nih.gov/"
    elif change == "plan":
        attempt["plan_sha256"] = "wrong"
    (directory / "canary-receipt.json").write_text(json.dumps(receipt))
    (directory / "canary-attempt.json").write_text(json.dumps(attempt))
    if change is None:
        result, _ = audit.read_new(tmp_path, Path("cache"), key, plan)
        assert result["selected_taxon"]["taxon_id"] == "NCBITaxon:123"
    else:
        with pytest.raises(ValueError):
            audit.read_new(tmp_path, Path("cache"), key, plan)


def test_public_checkpoint_accounts_for_every_source_term_and_claim():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    with (ROOT / "data/raw/aro_resistance_edges.tsv").open() as stream:
        labels = {r["determinant_id"]: r["determinant_name"] for r in csv.DictReader(stream, delimiter="\t")}
    index = json.loads((ROOT / result["inputs"]["index"]["path"]).read_bytes())
    expected = {tid for tid in index["terms"] if audit.GENE.search(labels[tid])}
    assert set(result["terms"]) == expected
    assert len(expected) == 137 and len(result["claims"]) == 141 and len(result["records"]) == 31
    for tid, term in result["terms"].items():
        assert term["source_label"] == labels[tid]
        assert term["source_label_sha256"] == hashlib.sha256(labels[tid].encode()).hexdigest()
        assert term["record_memberships"] == index["terms"][tid]["record_memberships"]
        assert {k: term[k] for k in audit.source_identity(labels[tid])} == audit.source_identity(labels[tid])
        assert term["experimental_subject_assignment"] is False
        assert term["exact_allele_assignment"] is False
        assert term["protein_reference_assignment"] is None
        assert term["primary_review_status"] == "OPEN"
    assert sorted(t for v in result["gene_name_contexts"].values() for t in v["terms"]) == sorted(expected)
    assert len(result["gene_name_contexts"]) == 45
    assert result["summary"]["distinct_selected_taxa"] == 31
    assert result["summary"]["term_name_status_counts"] == {
        "EXACT_NATIVE_NAME_REFERENCE": 128,
        "GENUS_GROUP_NOT_ONE_ORGANISM": 2,
        "NO_EXACT_ACTIVE_NAME_AT_SUPPORTED_RANK": 7,
    }
    qualified = result["names"]["Blumeria graminis f. sp. hordei"]["selected_taxon"]
    assert qualified["taxon_id"] == "NCBITaxon:2867405" and qualified["matching_fields"] == ["synonyms"]
    assert result["constraints"]["ncbi_requests"] == 0
    assert result["constraints"]["issue_1040"] == "DEFERRED"
    assert result["constraints"]["full_corpus_goal_status"] == "OPEN"
