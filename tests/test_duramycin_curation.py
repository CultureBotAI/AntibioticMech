"""Keep duramycin evidence separate from reference and experimental identities."""

import hashlib
import json
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import write_validated_antibiotic

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "research/2026-10-09-duramycin"


@pytest.fixture(scope="module")
def curation():
    return json.loads(Path(str(PREFIX) + "-curation.json").read_bytes())


@pytest.fixture(scope="module")
def context():
    return json.loads(Path(str(PREFIX) + "-reference-context.json").read_bytes())


def test_two_claims_one_record_roundtrip(curation, tmp_path):
    path = ROOT / curation["record"]["path"]
    record = load_record(path)
    assert record["identifier"] == curation["identifier"] == "CHEBI:77834"
    assert record["chemical_structure"]["standard_inchi_key"] == "SFWLDKQAUHFCBS-WWXQEMPQSA-N"
    assert record["curation_status"] == curation["curation_status"] == "SEEDED"
    assert record["resistance_mechanisms"] == curation["claims"]
    assert record["curation_history"][-1] == curation["curation_event"]
    assert curation["records_changed"] == curation["history_events_added"] == 1
    assert curation["claims_added"] == 2
    assert curation["all_other_fields_preserved"] and curation["original_bytes_preserved_as_prefix"]
    assert not record.get("activity_spectrum")
    output = tmp_path / path.name
    write_validated_antibiotic(record, output)
    assert output.read_bytes() == path.read_bytes()


def test_compound_identity_retains_stereochemical_limit(context):
    chemical = context["chemical_identity"]
    assert chemical["existing_exact_synonym"] == {
        "source": "chebi", "synonym_text": "Duramycin", "synonym_type": "EXACT_SYNONYM"}
    assert chemical["current_name_and_key_agree"] and chemical["local_inchi_recomputes_key"]
    assert chemical["both_smiles_parse"]
    assert chemical["unassigned_tetrahedral_centers_local_and_current"] == [1, 1]
    assert not chemical["complete_stereochemistry_established"]
    assert not chemical["source_structure_repaired"]
    assert context["primary_paper"]["tested_antibiotic"] == "duramycin"
    assert not context["primary_paper"]["direct_cinnamycin_ast"]


def test_heterologous_comparators_are_derivatives(curation):
    claim = curation["claims"][0]
    assert claim["gene_families"] == ["cinorf10"]
    assert claim["taxon_id"] == "NCBITaxon:1916"
    assert claim["taxon_label"] == "Streptomyces lividans"
    for phrase in ("Both compared subjects are laboratory derivatives", "vector control",
                   "gene presence alone did not predict", "background, not either derivative",
                   "reference-only", "differs from the study's"):
        assert phrase in claim["note"]


def test_native_perturbations_do_not_establish_resistant_alleles(curation):
    claim = curation["claims"][1]
    assert claim["gene_families"] == ["cinorf10", "cinK", "cinR"]
    assert claim["taxon_id"] == "NCBITaxon:53446"
    assert claim["taxon_label"] == "Streptomyces cinnamoneus"
    for phrase in ("Separate laboratory derivatives", "loss-of-protection evidence",
                   "not resistant alterations or individual gene sufficiency",
                   "Production-indicator assays are distinct", "do not establish direct CinK ligand binding"):
        assert phrase in claim["note"]


def test_no_reference_or_association_promoted(curation, context):
    for claim in curation["claims"]:
        assert claim["mechanism_type"] == "UNKNOWN"
        assert claim["evidence"][0]["reference"] == "PMID:27858169"
        assert not {"protein_accession", "gene_id", "alteration", "source", "aro_id",
                    "strain", "strain_taxon_id"} & claim.keys()
        assert "not direct cinnamycin AST" in claim["note"]
    assert context["reference_selection"] is None
    assert context["exact_experimental_protein_assignments"] == 0
    assert context["experimental_genome_assignments"] == 0


def test_versioned_uniprot_references_retain_all_contexts(context):
    proteins = context["proteins"]
    assert set(proteins) == {"Q83VX7", "Q83VX8", "Q83VX9"}
    for accession, version in {"Q83VX7": 59, "Q83VX8": 74, "Q83VX9": 110}.items():
        row = proteins[accession]
        assert row["entry_audit"] == {"entryVersion": version, "sequenceVersion": 1}
        assert not row["experimental_assignment"]
        assert row["organism"]["taxonId"] == 53446
        assert row["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
    assert {r["id"] for r in proteins["Q83VX9"]["archive_references"]} == {"AJ536588", "BMVB01000001"}
    strains = {r["value"] for c in proteins["Q83VX9"]["citation_contexts"] for r in c["context"]}
    assert strains == {"Type strain DSM 40005", "JCM 4633"}
    assert any("PMID:25193709" in note and "inconsistency" in note for note in context["reference_limits"])
    request = context["uniprot_request"]
    assert request["complete_for_query"] and request["result_count"] == 2
    assert request["release"] == "2026_03"


def test_taxonomy_does_not_conflate_background_or_collection_number(context):
    taxa = context["taxonomy"]
    assert taxa["1916"]["rank"] == taxa["53446"]["rank"] == "species"
    assert taxa["1200984"]["rank"] == "strain"
    assert taxa["1200984"]["parent"]["taxonId"] == 1916
    assert taxa["1200984"]["scope"] == "BACKGROUND_ONLY_NOT_EXPERIMENTAL_DERIVATIVE"
    assert taxa["457428"]["scope"] == "NOT_SELECTED_DIFFERENT_BACKGROUND"
    assert context["rejected_taxonomy_match"]["scientificName"] == "Myriopteris scabra"
    assert context["dsm40646_strain_taxon_assignment"] is None
    request = context["taxonomy_searches"]["exact_collection_phrase"]
    assert request["result_count"] == 0 and request["complete_for_query"]
    assert not request["establishes_biological_absence"]


def test_primary_review_scope_and_negative_findings(context):
    primary = context["primary_paper"]
    assert primary["figures_visually_inspected"] == [3, 4, 5]
    assert primary["relevant_results_text_inspected"]
    assert not primary["whole_paper_review_complete"] and not primary["supplement_inspected"]
    assert primary["license"] == "CC BY 4.0"
    for figure in primary["figures"].values():
        assert figure["visually_inspected"] and figure["actual_format"] == "PNG"
        assert figure["url_suffix"] == ".gif" and not figure["redistributed"]
    limits = " ".join(context["interpretation_limits"])
    for phrase in ("negative, expression-context-dependent", "CinR1 is not CinR",
                   "cinL heading", "pmtA", "not Bacillus subtilis resistance",
                   "not identification of every peak", "No global supplement-absence"):
        assert phrase in limits


def test_public_dossier_pins_and_review_remains_open(context, curation):
    for key in ("prior_context", "curation"):
        row = context[key]
        assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["sha256"]
    assert context["scope"]["corpus_records"] == 2939
    assert context["scope"]["full_corpus_primary_review"] == "OPEN"
    assert context["scope"]["whole_records_completed"] == 0
    assert not curation["whole_record_review_complete"]


def test_no_operational_experimental_exports(context, curation):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    prohibited = {"sequence", "variants", "alteration", "constructs", "primers", "protocol",
                  "coordinates", "mic", "measurement_value", "headers"}
    assert not set(keys(context)) & prohibited
    assert not set(keys(curation)) & prohibited
    for dossier in (context, curation):
        assert all(dossier[k] == 0 for k in ("ncbi_endpoint_requests", "github_mutations",
                                            "source_adoptions", "numerical_ast_added"))
