"""Keep the historical chemical conflict separate from exact resistance claims."""

import csv
import hashlib
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def context():
    return json.loads((ROOT / "research/2026-10-12-tetracenomycin-context.json").read_bytes())


def test_historical_identity_uses_census_not_a_frozen_live_record(context):
    pin = context["baseline_census"]
    payload = (ROOT / pin["path"]).read_bytes()
    assert hashlib.sha256(payload).hexdigest() == pin["sha256"]
    rows = {r["identifier"]: r for r in csv.DictReader(payload.decode().splitlines(), delimiter="\t")}
    assert len(rows) == 2939
    assert {r["identifier"] for r in context["records"]} == {"CHEBI:9470", "CHEBI:32209"}
    for record in context["records"]:
        old = rows[record["identifier"]]
        assert (old["path"], old["record_sha256"], old["standard_inchi_key"]) == (
            record["path"], record["review_time_sha256"], record["standard_inchi_key"],
        )
        assert record["whole_record_review"] == "OPEN"


def test_conflicting_structures_do_not_become_a_silent_replacement(context):
    identity = context["chemical_identity"]
    before, ligand = identity["review_time_structure"], identity["paper_ligand"]
    assert (before["molecular_formula"], before["standard_inchi_key"]) == (
        "C24H20O11", "CCDBRFCICQZPPE-DNQXCXABSA-N",
    )
    assert (ligand["molecular_formula"], ligand["standard_inchi_key"]) == (
        "C24H22O11", "QSPIPUXWSNFXCK-AGILITTLSA-N",
    )
    assert (ligand["identifier"], ligand["entry"], ligand["entity_id"]) == ("PDB:OCW", "PDB:6Y69", "55")
    assert identity["decision"] == "HOLD_EXACT_STRUCTURE_CLAIM_TRANSFER"
    assert identity["source_owner"] == "data/raw/chebi_antimicrobials.tsv"
    assert not identity["replacement_structure_assigned"] and not identity["cause_established"]
    assert "pre-existing" in identity["existing_claim_scope"]


@pytest.mark.parametrize("name", ["review_time_structure", "paper_ligand"])
def test_both_chemical_graphs_reproduce_when_rdkit_available(context, name):
    chem = pytest.importorskip("rdkit.Chem")
    descriptors = pytest.importorskip("rdkit.Chem.rdMolDescriptors")
    row = context["chemical_identity"][name]
    molecule = chem.MolFromSmiles(row["smiles"])
    assert molecule is not None
    assert chem.MolToInchiKey(molecule) == row["standard_inchi_key"]
    assert descriptors.CalcMolFormula(molecule) == row["molecular_formula"]
    assert len(molecule.GetSubstructMatches(chem.MolFromSmarts("[OX2H]"))) == row["hydroxyl_count"]
    assert len(molecule.GetSubstructMatches(chem.MolFromSmarts("[CX3]=[OX1]"))) == (
        row["carbonyl_count_including_ester"]
    )
    assert len(chem.FindMolChiralCenters(molecule, includeUnassigned=True)) == row["chiral_center_count"]


def test_native_review_and_failed_download_remain_distinct(context):
    primary = context["primary_review"]
    assert primary["reference"] == "PMID:32601485"
    assert primary["doi"] == "10.1038/s41589-020-0578-x"
    assert primary["visually_inspected_pages_one_based"] == [164, 165]
    assert primary["pdf_pages"] == 177
    assert "not a protein" in primary["rna_boundary"]
    assert not primary["whole_paper_review_complete"] and not primary["measurements_imported"]
    assert not primary["source_assets_redistributed"]
    limits = context["access_limits"]
    assert limits["primary_1992_download_status"] == 403
    assert not limits["primary_1992_download_is_pdf"] and not limits["access_bypass_or_outreach"]
    thesis, = [s for s in context["sources"] if s["cache_name"] == "wieland-thesis.pdf"]
    assert thesis["repository_md5_verified"] == "e99235c75870d7915a20b29b4d2e1f1c"
    assert len(thesis["sha256"]) == 64


def test_reference_genes_do_not_identify_experimental_subjects(context):
    ref = context["tetracenomycin_c_reference_context"]
    assert ref["producer_species"] == "NCBITaxon:1907"
    assert ref["heterologous_host_species"] == "NCBITaxon:1916"
    assert not ref["experimental_protein_or_genome_assigned"]
    assert ref["reference_scope"] == "REFERENCE_ONLY_NOT_EXPERIMENTAL_ALLELES"
    assert ref["release"] == "2026_03" and ref["results_per_query"] == 1
    assert ref["pagination_complete"] and not ref["historical_card_direct_link_counts_changed"]
    assert [(r["gene"], r["accession"], r["entry_version"], r["sequence_version"])
            for r in ref["references"]] == [
        ("tcmA", "UniProtKB:P39886", 106, 1), ("tcmR", "UniProtKB:P39885", 97, 1),
    ]
    assert all("PMID:1592819" in r["returned_citations"] for r in ref["references"])


def test_no_curation_or_completion_inflation(context):
    for key, value in context["disposition"].items():
        assert value == ("OPEN" if key == "whole_corpus_review" else 0)
    limits = context["access_limits"]
    assert limits["ncbi_endpoint_requests"] == limits["ncbi_contact"] == limits["source_adoptions"] == 0
    assert limits["issue_1040"] == "DEFERRED" and not limits["reuse_terms_review_resumed"]
