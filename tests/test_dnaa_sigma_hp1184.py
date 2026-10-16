"""Adversarial reference-identity checks without experimental allele promotion."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_dnaa_sigma_hp1184 as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("reference audit attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)


@pytest.fixture
def checkpoint():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_source_membership_and_scope(checkpoint):
    assert checkpoint["summary"] == {
        "current_corpus_hashes_verified": 2939,
        "complete_records_loaded": 8,
        "source_claims_bound": 12,
        "terms_investigated": 3,
        "reference_proteins": 4,
        "determinant_reference_contexts": 3,
        "comparators_not_resistance_determinants": 1,
        "species_nodes": 2,
        "reference_strain_nodes": 2,
        "whole_record_primary_signoffs": 0,
    }
    index = audit.read_json(ROOT, checkpoint["inputs"]["current_index"])
    for term, row in checkpoint["terms"].items():
        assert row["record_memberships"] == index["terms"][term]["record_memberships"]
        assert (
            sorted(c["record_identifier"] for c in checkpoint["claims"] if c["aro_id"] == term)
            == row["record_memberships"]
        )
        assert row["experimental_allele_assignment"] is None
        assert row["experimental_protein_assignment"] is None
        assert row["experimental_genome_assignment"] is None
        assert row["whole_record_primary_review"] == "OPEN"
        for reference in row["references"]:
            assert reference["experimental_allele_assignment"] is None
            assert reference["experimental_protein_assignment"] is None
            assert reference["experimental_strain_taxon_assignment"] is None
            assert reference["resistance_phenotype_from_protein_annotation"] is False
    assert checkpoint["constraints"]["ncbi_requests"] == 0
    assert checkpoint["constraints"]["issue_1040"] == "DEFERRED"
    assert checkpoint["constraints"]["full_investigation_complete"] is False
    assert checkpoint["primary_review"]["native_primary_body_replay_available"] is False
    assert checkpoint["primary_review"]["whole_papers_reviewed"] is False


def test_sigma_comparator_is_not_a_resistance_reference(checkpoint):
    row = checkpoint["terms"]["ARO:3000261"]
    assert row["reference_accessions"] == ["UniProtKB:P0AGB3"]
    assert row["comparator_accessions"] == ["UniProtKB:P00579"]
    refs = {r["gene_or_locus"]: r for r in row["references"]}
    assert refs["rpoD"]["role"] == "SIGMA70_COMPARATOR_NOT_RESISTANCE_DETERMINANT"
    assert refs["rpoD"]["eligible_as_determinant_reference_context"] is False
    assert refs["rpoH"]["eligible_as_determinant_reference_context"] is True


def test_hp1184_keeps_unreviewed_annotation_and_reference_strain(checkpoint):
    row = checkpoint["terms"]["ARO:3003965"]
    ref = row["references"][0]
    assert ref["accession"] == "UniProtKB:O25796"
    assert ref["gene_or_locus"] == "HP_1184"
    assert ref["reviewed"] is False
    assert ref["protein_names"] == ["Multidrug export protein MepA"]
    assert ref["reference_taxon_id"] == "NCBITaxon:85962"
    assert ref["reference_taxon_rank"] == "strain"
    assert row["primary_assessment"]["source_strains"] == ["1061", "clinical isolate cohort"]
    assert len(row["primary_assessment"]["papers"]) == 2


@pytest.fixture
def native_fixture(checkpoint):
    def make(key):
        row = checkpoint["terms"][audit.TERMS[key]]
        paper = copy.deepcopy(row["primary_assessment"])
        taxon = copy.deepcopy(checkpoint["native_taxonomy"][str(paper["reference_taxon_id"])])
        species = copy.deepcopy(checkpoint["native_taxonomy"][str(paper["reference_species_taxon_id"])])
        entries = []
        for ref in row["references"]:
            gene = (
                {"orderedLocusNames": [{"value": ref["gene_or_locus"]}]}
                if key == "hp1184"
                else {"geneName": {"value": ref["gene_or_locus"]}}
            )
            entries.append(
                {
                    "primaryAccession": ref["accession"].split(":")[1],
                    "entryType": "UniProtKB reviewed (Swiss-Prot)"
                    if ref["reviewed"]
                    else "UniProtKB unreviewed (TrEMBL)",
                    "entryAudit": {
                        "entryVersion": ref["entry_version"],
                        "sequenceVersion": ref["sequence_version"],
                    },
                    "organism": {"taxonId": taxon["taxonId"], "scientificName": taxon["scientificName"]},
                    "genes": [gene],
                    "proteinDescription": {
                        "recommendedName": {"fullName": {"value": ref["protein_names"][0]}},
                        "alternativeNames": [{"fullName": {"value": n}} for n in ref["protein_names"][1:]],
                    },
                    "references": [],
                }
            )
        return entries, taxon, species, paper

    return make


@pytest.mark.parametrize("key", ["dnaA", "sigma", "hp1184"])
def test_exact_reference_projection(native_fixture, checkpoint, key):
    expected = checkpoint["terms"][audit.TERMS[key]]["references"]
    assert audit.select_references(key, *native_fixture(key)) == expected


@pytest.mark.parametrize(
    "change",
    [
        "missing",
        "duplicate",
        "accession",
        "gene",
        "taxonomy",
        "organism_name",
        "inactive",
        "rank",
        "species",
        "parent",
        "sequence",
        "version",
        "unreviewed",
    ],
)
def test_reference_rejects_unsupported_identity(native_fixture, change):
    entries, taxon, species, paper = native_fixture("dnaA")
    if change == "missing":
        entries.clear()
    elif change == "duplicate":
        entries.append(copy.deepcopy(entries[0]))
    elif change == "accession":
        entries[0]["primaryAccession"] = "OTHER"
    elif change == "gene":
        entries[0]["genes"][0]["geneName"]["value"] = "dnaN"
    elif change == "taxonomy":
        entries[0]["organism"]["taxonId"] = 562
    elif change == "organism_name":
        entries[0]["organism"]["scientificName"] = "Different name"
    elif change == "inactive":
        taxon["active"] = False
    elif change == "rank":
        taxon["rank"] = "species"
    elif change == "species":
        species["scientificName"] = "Different species"
    elif change == "parent":
        taxon["parent"]["taxonId"] = 999
    elif change == "sequence":
        entries[0]["sequence"] = {"value": "NOT_REQUESTED"}
    elif change == "version":
        entries[0]["entryAudit"]["sequenceVersion"] = 0
    else:
        entries[0]["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    with pytest.raises(ValueError):
        audit.select_references("dnaA", entries, taxon, species, paper)


@pytest.mark.parametrize("change", ["swap", "ambiguous", "sigma_number"])
def test_sigma_rejects_component_conflation(native_fixture, change):
    entries, taxon, species, paper = native_fixture("sigma")
    by_gene = {e["genes"][0]["geneName"]["value"]: e for e in entries}
    if change == "swap":
        by_gene["rpoD"]["genes"][0]["geneName"]["value"] = "rpoH"
        by_gene["rpoH"]["genes"][0]["geneName"]["value"] = "rpoD"
    elif change == "ambiguous":
        by_gene["rpoD"]["genes"].append({"geneName": {"value": "rpoH"}})
    else:
        by_gene["rpoH"]["proteinDescription"]["alternativeNames"] = []
    with pytest.raises(ValueError):
        audit.select_references("sigma", entries, taxon, species, paper)


def test_hp_locus_does_not_match_related_gene(native_fixture):
    entries, taxon, species, paper = native_fixture("hp1184")
    entries[0]["genes"][0]["orderedLocusNames"][0]["value"] = "HP_1181"
    with pytest.raises(ValueError):
        audit.select_references("hp1184", entries, taxon, species, paper)
