"""Reference identifiers and related-compound assays are not experimental joins."""

import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-09-peptide-reference-followup.json").read_bytes())


def test_historical_checkpoint_and_open_corpus_scope(dossier):
    assert dossier["scope"] == {
        "corpus_records": 2939, "record_memberships": 4,
        "whole_records_completed_by_this_review": 0, "full_corpus_primary_review": "OPEN",
    }
    for key in ("prior_biological_checkpoint", "prior_context", "current_census"):
        pin = dossier[key]
        assert hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]
    assert dossier["preservation"]["record_hashes_verified"] == 2939
    assert dossier["preservation"]["ignored_files_included"] is True
    assert dossier["preservation"]["biological_record_changes"] == 0
    assert dossier["preservation"]["curation_events_added"] == 0


@pytest.mark.parametrize("identifier", ["CHEBI:133127", "CHEBI:141991", "CHEBI:71629", "CHEBI:71658"])
def test_open_holds_preserve_compound_identity(dossier, identifier):
    row, = [r for r in dossier["records"] if r["identifier"] == identifier]
    record = load_record(ROOT / row["path"])
    assert record["identifier"] == identifier
    assert record["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"]
    assert row["decision"].startswith("HOLD_")
    assert row["whole_record_review"] == "OPEN"
    assert row["record_action"] == "PRESERVE_NO_NEW_BIOLOGICAL_CLAIM"


def test_cinnamycin_does_not_inherit_duramycin_ast_or_reference_strain(dossier):
    paper = dossier["primary_papers"]["27858169"]
    assert paper["tested_antibiotic"] == "duramycin"
    assert paper["direct_cinnamycin_ast"] is False
    assert paper["donor_label"] == "Streptomyces cinnamoneus DSM 40646"
    reference = dossier["proteins"]["Q83VX7"]
    strains = {c["value"] for r in reference["citation_contexts"]
               for c in r["context"] if c["type"] == "STRAIN"}
    assert strains == {"Type strain DSM 40005"}
    assert reference["experimental_assignment"] is False
    assert "No cinL synonym is inferred" in paper["source_heading_caution"]


def test_mersacidin_reference_revision_is_not_historical_allele(dossier):
    proteins = dossier["proteins"]
    expected = {"Q9RC25": (36, 1), "Q9RC26": (35, 2), "Q9RC27": (83, 1),
                "Q9RC28": (126, 1), "Q9RC29": (110, 1)}
    for accession, (entry_version, sequence_version) in expected.items():
        reference = proteins[accession]
        assert reference["entry_audit"] == {
            "entryVersion": entry_version, "sequenceVersion": sequence_version,
        }
        assert reference["organism"]["taxonId"] == 69002
        archive, = reference["archive_references"]
        assert archive["id"] == "AJ250862"
        assert reference["experimental_assignment"] is False
    archive = dossier["archive_references"]["AJ250862"]["reference"]
    assert archive["version"] == 2 and archive["lastUpdated"] == "17-MAR-2011"
    mrs_g, = proteins["Q9RC26"]["archive_references"]
    assert {p["value"] for p in mrs_g["properties"] if p["key"] == "ProteinId"} == {"CAB60256.2"}
    assert dossier["reference_taxonomy"]["69002"]["rank"] == "species"
    assert "strain HIL" in dossier["reference_taxonomy"]["69002"]["scientificName"]
    paper = dossier["primary_papers"]["11772616"]
    assert paper["direct_transport_measurement"] is False
    assert "residual transcription" in " ".join(paper["qualitative_findings"])
    assert "modified mersacidin" in " ".join(paper["qualitative_findings"])


def test_lugdunin_genome_is_background_not_tested_derivative(dossier):
    archive = dossier["archive_references"]["CP063143"]
    assert archive["scope"] == "BACKGROUND_CHROMOSOME_NOT_EXPERIMENTAL_DERIVATIVE"
    assert archive["experimental_genome_assignment"] is False
    assert archive["reference"]["version"] == 1
    assert archive["reference"]["project"] == "PRJNA669000"
    assert archive["reference"]["sample"] == "SAMN16428309"
    assert archive["reference"]["taxon"] == 28035
    assert dossier["reference_taxonomy"]["28035"]["rank"] == "species"
    row, = [r for r in dossier["records"] if r["identifier"] == "CHEBI:133127"]
    assert row["reference_candidates"] == []
    paper = dossier["primary_papers"]["33106269"]
    assert paper["background_genome_reference"] == "CP063143"
    assert paper["exact_experimental_protein_assignment"] is False


def test_nisin_archive_and_taxon_rank_are_reference_context(dossier):
    archive = dossier["archive_references"]["L16226"]
    assert archive["reference"]["taxon"] == 1358
    assert archive["scope"] == "REFERENCE_GENE_CLUSTER_NOT_GENOME_ASSEMBLY"
    assert dossier["proteins"]["P42708"]["organism"]["taxonId"] == 1360
    assert dossier["reference_taxonomy"]["1360"]["parent"]["taxonId"] == 1358
    searches = {r["query"]: r for r in dossier["nisin_taxonomy_searches"]}
    assert {r["taxonId"] for r in searches["MG1614"]["candidates"]} == {1359, 1729979}
    assert searches["NZ9700"]["result_count"] == 0
    for query in searches.values():
        assert query["complete_for_query"]
        assert query["experimental_strain_assigned"] is False
        assert query["establishes_biological_absence"] is False


def test_structure_checks_do_not_repair_or_prove_tested_material(dossier):
    checks = {r["identifier"]: r for r in dossier["chemical_identity_checks"]}
    for row in checks.values():
        assert row["rdkit_version"] == "2026.03.5"
        assert row["current_chebi_key_matches_record"]
        assert row["stored_standard_inchi_parses"] and row["recomputed_key_matches_record"]
        assert row["source_owned_structure_changed"] is False
        assert "not proof" in row["interpretation"]
    for identifier in ("CHEBI:71629", "CHEBI:133127"):
        assert checks[identifier]["stored_smiles_parses_strictly"] is False
        assert checks[identifier]["current_chebi_smiles_parses_strictly"] is False
        assert checks[identifier]["unassigned_tetrahedral_centers"] == 1
    assert checks["CHEBI:71658"]["smiles_key_matches_record"]
    assert checks["CHEBI:71658"]["unassigned_tetrahedral_centers"] == 1
    assert checks["CHEBI:141991"]["unassigned_tetrahedral_centers"] == 0


def test_query_completeness_and_error_are_not_biological_absence(dossier):
    queries = dossier["uniprot_requests"]
    assert len(queries) == 6
    assert sorted(r["result_count"] for r in queries) == [0, 0, 0, 0, 1, 96]
    assert all(r["complete_for_query"] and not r["establishes_biological_absence"] for r in queries)
    assert all(r["release"] == "2026_03" for r in queries)
    error, = dossier["query_failures"]
    assert error["status"] == 400
    assert error["query"] == "citation:27858169"
    assert "NOT_A_NEGATIVE_RESULT" in error["disposition"]
    selection = dossier["reference_selection"]
    assert selection["mrs_gene_query_results"] == 96
    assert selection["selected_mersacidin_references"] == 5
    assert selection["unselected_results"] == 91
    assert selection["unselected_results_are_not_resistance_assignments"]
    for request in queries + dossier["bibliographic_requests"]:
        assert urlsplit(request["url"]).hostname in {"rest.uniprot.org", "www.ebi.ac.uk"}


def test_primary_review_medium_and_coverage_are_explicit(dossier):
    papers = dossier["primary_papers"]
    assert set(papers) == {"7689965", "8161176", "10376839", "11772616", "27858169", "33106269"}
    for pmid in ("7689965", "10376839"):
        assert papers[pmid]["review_medium"] == "PUBLISHER_VERSION_IN_INSTITUTIONAL_REPOSITORY"
        assert papers[pmid]["figures_visually_inspected"]
        assert papers[pmid]["visually_reviewed_pdf_pages_zero_based"]
        assert "PRIVATE_READING_ONLY" in papers[pmid]["reuse"]
    assert papers["8161176"]["relevant_results_text_inspected"] is False
    for pmid in ("27858169", "33106269"):
        assert papers[pmid]["review_medium"] == "PRIMARY_FULLTEXT_XML_RELEVANT_SECTIONS"
        assert papers[pmid]["license"] == "CC BY 4.0"
        assert papers[pmid]["relevant_results_text_inspected"]
        assert papers[pmid]["figures_visually_inspected"] is False
    assert papers["11772616"]["epmc_open_access_flag"] == "N"
    assert papers["11772616"]["review_medium"] == "PUBLIC_INDEXED_AUTHOR_UPLOADED_PRIMARY_TEXT_TRANSCRIPTION"
    assert all(not p["supplement_inspected"] and not p["whole_paper_review_complete"]
               for p in papers.values())


def test_export_is_non_operational_and_does_not_claim_new_full_qc(dossier):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    prohibited = {"sequence", "variants", "alteration", "constructs", "primers", "protocol",
                  "coordinates", "mic", "measurement_value", "headers", "smiles", "inChI"}
    assert not set(keys(dossier)) & prohibited
    assert "full authoritative QC not rerun" in dossier["validation_scope"]
    assert all(dossier[k] == 0 for k in ("ncbi_endpoint_requests", "github_mutations", "source_adoptions",
                                        "numerical_ast_added", "experimental_genome_assignments",
                                        "exact_experimental_protein_assignments"))
    assert dossier["new_reference_proteins"] == 6
    assert dossier["previous_reference_proteins_reused"] == 1
    assert all(not p["experimental_assignment"] for p in dossier["proteins"].values())


@pytest.fixture(scope="module")
def vocabulary_gap():
    return json.loads((ROOT / "research/2026-10-09-peptide-discovery-vocabulary-gap.json").read_bytes())


@pytest.mark.parametrize("identifier", ["CHEBI:133127", "CHEBI:141991"])
def test_known_paper_probes_use_production_search_settings(vocabulary_gap, identifier):
    case, = [r for r in vocabulary_gap["cases"] if r["identifier"] == identifier]
    old = vocabulary_gap["requests"][case["old_clause_probe"]]
    complementary = vocabulary_gap["requests"][case["complementary_probe"]]
    assert old["hit_count"] == 0
    assert complementary["candidate_ids"] == [case["reference"].replace("PMID:", "MED:")]
    for request in (old, complementary):
        assert request["complete_for_query"] and not request["establishes_biological_absence"]
        assert request["params"]["synonym"] == "false"
        assert request["params"]["resultType"] == "lite"
        assert request["params"]["cursorMark"] == "*"
        assert urlsplit(request["url"]).hostname == "www.ebi.ac.uk"
    assert case["known_primary_present_in_initial_snapshot"] is False
    assert case["biological_conclusion"] == "NONE; search recall only"


def test_vocabulary_gap_preserves_history_and_does_not_claim_fix(vocabulary_gap):
    source = vocabulary_gap["initial_candidates"]
    assert hashlib.sha256((ROOT / source["path"]).read_bytes()).hexdigest() == source["sha256"]
    assert vocabulary_gap["criteria_at_review"].endswith("-v1")
    assert vocabulary_gap["scope"] == "TWO_KNOWN_PAPER_FILTER_COUNTEREXAMPLES_NOT_CORPUS_RECALL_ESTIMATE"
    for key in ("historical_snapshots_rewritten", "discovery_code_changed",
                "full_corpus_supplemental_search_run"):
        assert vocabulary_gap[key] is False
    assert len(vocabulary_gap["requests"]) == 4
