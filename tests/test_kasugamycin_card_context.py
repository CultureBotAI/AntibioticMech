"""Keep RNA, chemical-form and experimental-subject boundaries in the CARD audit."""

import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def context():
    return json.loads((ROOT / "research/2026-10-12-kasugamycin-card-context.json").read_bytes())


def test_historical_inputs_and_three_definition_citations_are_pinned(context):
    for pin in context["inputs"].values():
        assert hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]
    citations = json.loads((ROOT / context["inputs"]["definition_citations"]["path"]).read_bytes())
    assert set(context["determinations"]) == {"ARO:3003333", "ARO:3003988", "ARO:3004628"}
    for aro, row in context["determinations"].items():
        assert row["definition_citations"] == citations["terms"][aro]["definition_citation_ids"]
        assert row["definition_citations"] == [row["reference"]]
    census = ROOT / context["inputs"]["census"]["path"]
    with census.open() as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    row, = [r for r in rows if r["identifier"] == "CHEBI:81419"]
    assert len(rows) == 2939 and row["record_sha256"] == context["record"]["sha256"]


def test_ribosomal_rna_is_not_grounded_to_ksga_or_any_other_protein(context):
    row = context["determinations"]["ARO:3003333"]
    assert row["molecule_type"] == "RIBOSOMAL_RNA_NOT_PROTEIN"
    assert row["uniprot_disposition"] == "NOT_APPLICABLE_TO_RRNA_DETERMINANT"
    assert not row["experimental_protein_assigned"]
    assert row["reference_taxon_id"] == "NCBITaxon:562"
    assert "ABSTRACT" in row["review_scope"] and "403" in row["access_limit"]
    assert row["decision"] == "HOLD_FULL_PRIMARY_AND_NUCLEOTIDE_REFERENCE_REVIEW"
    assert "KsgA" in row["findings"][1]["interpretation"]


def test_iia_archive_join_keeps_protein_version_and_fragment_scope(context):
    row = context["determinations"]["ARO:3004628"]["reference_grounding"]
    assert (row["accession"], row["entry_version"], row["sequence_version"]) == (
        "UniProtKB:I4DEC2", 26, 1,
    )
    assert row["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
    assert (row["archive_accession"], row["archive_protein_id"]) == ("AB669090", "BAM16262.1")
    assert row["paper_source_strain"] == "5091"
    assert row["archive_scope"] == "SOURCE_REPORTED_GENOMIC_FRAGMENT_NOT_ASSEMBLY"
    assert not row["archive_version_supplied"]
    assert not row["experimental_protein_assigned"] and not row["experimental_genome_assigned"]
    taxon = context["taxonomy"]["337"]
    assert taxon["scientificName"] == "Burkholderia glumae" and taxon["rank"] == "species"
    old = json.loads((ROOT / context["inputs"]["prior_reference_candidates"]["path"]).read_bytes())
    candidate, = old["determinants"]["ARO:3004628"]["candidates"]
    assert candidate["accession"] == row["accession"]
    assert candidate["entry_audit"]["entryVersion"] == row["entry_version"]


def test_salt_and_unresolved_preparation_do_not_become_neutral_mics(context):
    assert context["record"]["chemical_form"] == "NEUTRAL"
    iia = context["determinations"]["ARO:3004628"]["chemical_identity"]
    assert iia["source_preparation"] == "kasugamycin hydrochloride"
    assert iia["decision"] == "SALT_NOT_IDENTICAL_TO_NEUTRAL_RECORD"
    assert not iia["neutral_mass_conversion_inferred"]
    assert not context["determinations"]["ARO:3003988"]["chemical_identity"]["preparation_form_resolved"]
    policy = context["measurement_policy"]
    assert policy["preferred_mic_units"] == "mg/L" and policy["ug_per_ml_factor"] == 1
    assert policy["censored_values_remain_censored"]
    assert not policy["clinical_categories_inferred"] and policy["numeric_observations_imported"] == 0
    assert not policy["salt_to_neutral_mass_conversion_inferred"]


def test_iib_taxonomy_keeps_returned_rank_and_no_wrong_organism_protein(context):
    row = context["determinations"]["ARO:3003988"]["reference_grounding"]
    assert row["taxon_id"] == "NCBITaxon:1120679"
    assert row["taxonomy_rank"] == context["taxonomy"]["1120679"]["rank"] == "species"
    assert "Paenibacillus sp. LC231" in context["taxonomy"]["1120679"]["otherNames"]
    assert row["uniprot_exact_taxon_result_count"] == 0
    assert row["name_query_result_count"] == 24 and row["other_taxon_candidates_assigned"] == 0
    assert row["uniprot_disposition"].endswith("NOT_GLOBAL_ABSENCE")
    assert row["source_wgs_project"] == "JFOM00000000"
    assert row["source_determinant_accession_range"] == ["KX531043", "KX531056"]
    assert not row["specific_determinant_accession_assigned"]
    assert "NOT_ASSEMBLY_OR_ALLELE_ASSIGNMENT" in row["scope"]


def test_native_negative_and_label_discrepancy_are_not_erased_by_biochemistry(context):
    row = context["determinations"]["ARO:3003988"]
    supplement = row["supplement"]
    assert supplement["pages"] == 17
    assert supplement["native_pages_reviewed_one_based"] == [6, 7, 8, 9]
    assert not supplement["whole_supplement_review_complete"]
    findings = {r["evidence_type"]: r for r in row["findings"]}
    assert "reported as No" in findings["NATIVE_ISOLATE_OBSERVATION"]["interpretation"]
    assert "IIa" in findings["NATIVE_ISOLATE_OBSERVATION"]["interpretation"]
    assert "IIb" in findings["NATIVE_ISOLATE_OBSERVATION"]["interpretation"]
    assert "not measure each determinant" in findings["HETEROLOGOUS_HOST_EXPERIMENT"]["interpretation"]
    assert "eightfold" in findings["CENSORED_PHENOTYPE_COMPARISON"]["interpretation"]
    assert "does not erase" in findings["BIOCHEMICAL_EVIDENCE"]["interpretation"]
    assert "not the focal" in findings["HOMOLOG_COMPARISON_NOT_IDENTITY"]["interpretation"]


def test_requested_uniprot_scope_is_complete_but_never_a_global_search(context):
    queries = {}
    assert len(context["uniprot_requests"]) == 5
    for request in context["uniprot_requests"]:
        parsed = urlsplit(request["url"])
        assert parsed.hostname == "rest.uniprot.org" and request["status"] == 200
        assert request["release"] == context["uniprot_release"] == "2026_03"
        assert len(request["sha256"]) == len(request["cache"]["sha256"]) == 64
        if parsed.path.endswith("/search"):
            assert request["result_count"] == request["total_results"]
            assert not request["next_page_present"] and request["complete_for_requested_query_only"]
            queries[request["query"]] = request["result_count"]
        if parsed.path == "/uniprotkb/search":
            assert "sequence" not in parse_qs(parsed.query)["fields"][0].split(",")
    assert queries == {"accession:I4DEC2": 1, "LC231": 1, "organism_id:1120679": 0,
                       "protein_name:kasugamycin AND taxonomy_name:Paenibacillus": 24}


def test_access_and_name_search_limits_remain_explicit(context):
    failed, = [r for r in context["primary_assets"] if r["status"] != 200]
    assert failed["status"] == 500 and failed["scope"] == "FAILED_REQUEST_NO_CONTENT_REVIEW"
    for request in context["primary_assets"]:
        assert urlsplit(request["url"]).hostname == "www.ebi.ac.uk"
    search = context["local_name_search"]
    assert search["ignored_files_included"] and search["records_inspected"] == 2939
    assert search["matching_identifiers"] == ["CHEBI:81419"]
    assert "not a structural proof" in search["limit"]
    assert "not proof that no correction exists" in " ".join(context["limitations"])


@pytest.mark.parametrize("key", [
    "records_changed", "new_claims", "new_measurements", "curation_events_added",
    "experimental_proteins_assigned", "experimental_genomes_assigned", "whole_records_completed",
])
def test_partial_source_review_does_not_promote_unresolved_findings(context, key):
    assert context["disposition"][key] == 0
    assert context["disposition"]["whole_corpus_primary_review"] == "OPEN"
    assert context["record"]["whole_record_review"] == "OPEN"
    assert "#1040" in " ".join(context["limitations"])
