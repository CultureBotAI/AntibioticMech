"""Keep FR171456 gene-level evidence distinct from reference alleles."""

import copy
import hashlib
import json
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import write_validated_antibiotic

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "research/2026-10-11-fr171456"


@pytest.fixture(scope="module")
def context():
    return json.loads(Path(str(PREFIX) + "-context.json").read_bytes())


@pytest.fixture(scope="module")
def curation():
    return json.loads(Path(str(PREFIX) + "-curation.json").read_bytes())


def test_validated_record_preserves_original_fields(curation, tmp_path):
    path = ROOT / curation["record"]["path"]
    doc = load_record(path)
    assert doc["identifier"] == "CHEBI:88298"
    assert doc["curation_status"] == "SEEDED"
    assert doc["resistance_mechanisms"] == [curation["claim"]]
    assert curation["records_changed"] == curation["history_events_added"] == 1
    output = tmp_path / path.name
    write_validated_antibiotic(doc, output)
    assert output.read_bytes() == path.read_bytes()
    before = copy.deepcopy(doc)
    before.pop("resistance_mechanisms")
    event = before["curation_history"].pop()
    assert event["action"] == "CURATED_RESISTANCE_EVIDENCE" and event["llm_assisted"]
    write_validated_antibiotic(before, output)
    assert hashlib.sha256(output.read_bytes()).hexdigest() == curation["before"]["sha256"]


def test_claim_scope_does_not_assign_reference_allele(curation):
    claim = curation["claim"]
    assert claim["gene_families"] == ["ERG26"]
    assert claim["mechanism_type"] == "ANTIBIOTIC_TARGET_ALTERATION"
    assert claim["taxon_id"] == "NCBITaxon:4932"
    assert claim["taxon_label"] == "Saccharomyces cerevisiae"
    assert not {"protein_accession", "strain", "strain_taxon_id", "alteration", "gene_id",
                "mic_value", "assembly_accession", "source", "aro_id"} & claim.keys()
    assert claim["evidence"][0]["reference"] == "PMID:26456460"
    for qualifier in ("not a clinical or species-wide phenotype", "remain unexplained",
                      "reference context, not an experimental allele"):
        assert qualifier in claim["note"]
    assert curation["experimental_alleles_assigned"] == curation["experimental_genomes_assigned"] == 0
    assert curation["numerical_ast_added"] == 0


@pytest.mark.parametrize("accession,gene,locus,version", [
    ("P53199", "ERG26", "YGL001C", 201),
    ("P12683", "HMG1", "YML075C", 231),
    ("P12684", "HMG2", "YLR450W", 217),
    ("P53049", "YOR1", "YGR281W", 218),
])
def test_reference_proteins_remain_separate(context, accession, gene, locus, version):
    protein = context["reference_proteins"][accession]
    assert protein["accession"] == "UniProtKB:" + accession
    assert protein["gene_names"] == [gene] and protein["loci"] == [locus]
    assert protein["entry_type"] == "UniProtKB reviewed (Swiss-Prot)"
    assert protein["entry_version"] == version and protein["sequence_version"] == 1
    assert not protein["experimental_assignment"] and not protein["exact_allele_assignment"]
    assert protein["reference_taxon_id"] == "NCBITaxon:559292"
    assert protein["focal_paper_cited"] == (accession == "P53199")
    assert context["reference_release"] == "2026_03"


def test_taxonomy_ranks_and_chemical_identity(context):
    assert context["taxonomy"]["4932"]["rank"] == "species"
    assert context["taxonomy"]["559292"]["rank"] == "strain"
    assert context["taxonomy"]["559292"]["parent"]["taxonId"] == 4932
    assert context["chemical_identity"]["standard_inchi_key"] == "JAHGNOXPMXOEJS-BSPLYONXSA-N"
    assert context["chemical_identity"]["smiles_inchi_key_agree"]
    assert not context["chemical_identity"]["tested_preparation_independently_reidentified"]


def test_native_evidence_and_unresolved_holds(context):
    assert context["primary"]["native_figures_inspected"] == ["2", "3"]
    assert context["primary"]["supplement_pages_visually_inspected"] == [6, 9, 13]
    assert {row["scope"] for row in context["holds"]} == {
        "YPR090w / YPL090w", "HMG1 / HMG2 / YOR1", "Experimental identifiers"}
    assert context["scope"]["corpus_records"] == 2939
    assert context["scope"]["whole_record_reviews_completed"] == 0
    assert context["scope"]["whole_corpus_primary_review"] == "OPEN"
    assert context["ncbi_endpoint_requests"] == context["source_adoptions"] == 0
    assert context["github_mutations"] == 0
    assert not context["access_history"]["publisher_credentials_used"]
    assert not context["access_history"]["paywall_bypass"]


def test_public_projection_omits_raw_biological_payloads(context):
    forbidden = {"sequence", "features", "variants", "protocol", "primers", "constructs", "mic_value"}

    def walk(value):
        if isinstance(value, dict):
            assert not forbidden & value.keys()
            for nested in value.values():
                walk(nested)
        elif isinstance(value, list):
            for nested in value:
                walk(nested)

    walk(context)
