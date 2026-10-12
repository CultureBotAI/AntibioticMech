"""Separate component references from experimental resistance claims."""

import copy
import csv
import gzip
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def context():
    return json.loads((ROOT / "research/2026-10-12-emrab-context.json").read_bytes())


def assert_pin(pin):
    payload = (ROOT / pin["path"]).read_bytes()
    assert hashlib.sha256(payload).hexdigest() == pin["sha256"]
    return payload


def test_records_and_source_assertion_are_preserved(context):
    payload = assert_pin(context["preservation"]["current_census"])
    rows = list(csv.DictReader(payload.decode().splitlines(), delimiter="\t"))
    by_id = {r["identifier"]: r for r in rows}
    assert len(rows) == len(by_id) == 2939
    assert {r["identifier"] for r in context["records"]} == {"CHEBI:100147", "CHEBI:67121"}
    for member in context["records"]:
        old = by_id[member["identifier"]]
        assert (member["path"], member["sha256"], member["standard_inchi_key"]) == (
            old["path"], old["record_sha256"], old["standard_inchi_key"],
        )
        record = load_record(ROOT / member["path"])
        assert record["identifier"] == member["identifier"]
        assert record["chemical_structure"]["standard_inchi_key"] == member["standard_inchi_key"]
        claims = member["existing_emrab_assertions"]
        if member["identifier"] == "CHEBI:100147":
            claim, = claims
            assert claim["aro_id"] == "ARO:3000344" and claim in record["resistance_mechanisms"]
            assert "protein_accession" not in claim and "taxon_id" not in claim
        else:
            assert claims == []
        assert member["action"] == "PRESERVE_RECORD_NO_PRIMARY_UPGRADE"
        assert member["whole_record_review"] == "OPEN"


@pytest.mark.parametrize("gene,accession,loci,ev,sv", [
    ("emrA", "P27303", ["b2685", "JW2660"], 175, 2),
    ("emrB", "P0AEJ0", ["b2686", "JW2661"], 133, 1),
    ("tolC", "P02930", ["b3035", "JW5503"], 216, 3),
])
def test_versioned_component_queries(context, gene, accession, loci, ev, sv):
    row, = [r for r in context["reference_components"] if r["canonical_gene"] == gene]
    assert row["protein_accession"] == "UniProtKB:" + accession
    assert row["ordered_locus_names"] == loci
    assert (row["entry_version"], row["sequence_version"]) == (ev, sv)
    assert row["reviewed"] and row["reference_taxon_id"] == "NCBITaxon:83333"
    assert row["scope"] == "REFERENCE_COMPONENT_ONLY"
    assert not row["experimental_assignment"] and not row["returned_bibliography_cites_primary"]
    assert row["pdb_cross_references"] == ["PDB:8ZAL", "PDB:8ZAR"]
    request = row["request"]
    assert request["release"] == "2026_03" and request["status"] == 200
    assert request["result_count"] == request["total_results"] == 1
    assert request["pagination_complete"]
    assert request["completeness_scope"] == "EXACT_REFERENCE_GENE_QUERY_ONLY"
    url = urlsplit(request["url"])
    assert (url.scheme, url.hostname, url.path) == (
        "https", "rest.uniprot.org", "/uniprotkb/search",
    )
    params = parse_qs(url.query)
    assert params["query"] == [f"gene_exact:{gene} AND organism_id:83333 AND reviewed:true"]
    assert "sequence" not in params["fields"][0].split(",")


def test_structural_citation_bridge_is_not_a_single_protein_or_allele(context):
    assert len(context["reference_components"]) == 3
    structures = {r["identifier"]: r for r in context["structures"]}
    assert len(context["structures"]) == len(structures) == 2
    for identifier, label, resolution in [("8ZAL", "EA", 3.11), ("8ZAR", "FA", 3.59)]:
        row = structures["PDB:" + identifier]
        assert row["source_preparation_label"] == label and row["resolution_angstrom"] == resolution
        assert row["method"] == "EM" and row["protein_entity_count"] == 3
        assert row["entry_version"] == "1.2" and row["revision_date"].startswith("2026-05-13")
        assert row["primary_doi"] == context["primary"]["doi"] == "10.1038/s41467-026-70500-5"
        assert row["primary_reference"] == context["primary"]["reference"] == "PMID:41839863"
        assert not row["is_single_protein_identity"] and not row["is_experimental_allele_assignment"]
        request = row["request"]
        assert request["status"] == 200 and not request["redirects_followed"]
        assert request["content_type"] == "application/json"
        assert request["sha256"] == request["cache"]["sha256"]
        assert request["url"] == "https://data.rcsb.org/rest/v1/core/entry/" + identifier
    scope = context["structural_scope"]
    assert scope["complex_name"] == "EmrAB-TolC" and not scope["is_emrd"]
    assert not scope["single_protein_assignment_for_complex"]
    assert not scope["source_and_expression_organism_are_interchangeable"]
    assert scope["paper_abstract_resolution_angstrom"] == 3.13


def test_reused_taxonomy_does_not_assign_experimental_strains(context):
    taxa = {r["taxon_id"]: r for r in context["taxonomy"]}
    assert set(taxa) == {"NCBITaxon:562", "NCBITaxon:83333"}
    assert taxa["NCBITaxon:83333"]["rank"] == "strain"
    assert taxa["NCBITaxon:83333"]["parent_taxon_id"] == "NCBITaxon:562"
    assert taxa["NCBITaxon:562"]["rank"] == "species"
    for row in taxa.values():
        assert row["active"] and row["reused_cache"]
        assert row["request"]["url"] == (
            "https://rest.uniprot.org/taxonomy/" + row["taxon_id"].split(":")[1] + ".json"
        )
        assert row["request"]["status"] == 200 and row["request"]["release"] == "2026_03"
    for predecessor in context["taxonomy_predecessors"]:
        assert_pin(predecessor)
    subject = context["subject_scope"]
    assert subject["species_taxon_id"] == "NCBITaxon:562"
    assert "C43(DE3)" in subject["paper_background_label"]
    assert not subject["reference_taxon_is_experimental_strain"]
    assert not any(value for key, value in subject.items() if key.endswith("_assigned"))


def test_inaccessible_native_assets_and_distinct_endpoints(context):
    primary = context["primary"]
    assert primary["text_review_scope"] == "SELECTED_RESULTS_AND_CAPTIONS_FROM_WEB_EXTRACTION"
    for field in ("native_figures_inspected", "supplements_inspected", "whole_paper_review_complete"):
        assert primary[field] is False
    access = primary["access"]
    assert not access["native_pdf_cached"] and access["institution_pdf_status"] == 403
    failed = access["failed_download"]
    assert failed["status"] == 303 and not failed["is_pdf"]
    assert failed["content_type"].startswith("text/html") and not failed["redirects_followed"]
    assert failed["sha256"] == failed["cache"]["sha256"]
    findings = primary["text_findings_pending_native_review"]
    assert all(r["location"] and r["evidence_type"] for r in findings)
    assert "lacks the tested resistance activity" in findings[1]["finding"]
    assert "CHH" in findings[2]["finding"] and "CCCP" in findings[2]["finding"]
    decision = context["disposition"]
    assert decision["decision"] == "REFERENCE_CROSSWALK_VERIFIED_PHENOTYPE_CURATION_HELD"
    assert not decision["plate_concentrations_converted_to_mic"]
    assert not decision["exact_compound_preparations_verified"]


def test_compressed_discovery_search_is_bounded_and_reproducible(context):
    discovery = context["discovery"]
    assert len(discovery["searched_exports"]) == 9 and discovery["ignored_files_included"]
    for pin in discovery["searched_exports"]:
        serialized = json.dumps(json.loads(gzip.decompress(assert_pin(pin))))
        assert "41839863" not in serialized and "10.1038/s41467-026-70500-5" not in serialized
        assert not pin["pmid_present"] and not pin["doi_present"]
    assert not discovery["candidate_retained_in_these_exports"]
    assert not discovery["query_miss_cause_established"]
    assert not discovery["historical_searches_modified"]


def assert_no_experimental_payload(value):
    forbidden = {"sequence", "variant", "alteration", "construct", "primer", "mic",
                 "mic_value", "strain_taxon_id", "assembly_accession", "biosample_accession",
                 "bioproject_accession", "sra_accessions", "experimental_protein_accession"}
    if isinstance(value, dict):
        assert not forbidden.intersection(value)
        for child in value.values():
            assert_no_experimental_payload(child)
    elif isinstance(value, list):
        for child in value:
            assert_no_experimental_payload(child)


def test_no_payload_or_completion_inflation(context):
    assert_no_experimental_payload(context)
    preservation = context["preservation"]
    assert preservation["records_checked"] == preservation["records_unchanged"] == 2939
    assert preservation["ignored_files_included"] and preservation["earlier_thiolutin_changes_preserved"]
    assert preservation["whole_corpus_status"] == "OPEN"
    for key in ("records_curated", "new_resistance_claims", "new_measurements",
                "curation_events_added", "whole_records_completed"):
        assert context["disposition"][key] == 0
    assert context["limits"]["issue_1040"] == "DEFERRED"
    assert all(value is False for key, value in context["limits"].items() if key != "issue_1040")


@pytest.mark.parametrize("field", ["mic", "strain_taxon_id", "experimental_protein_accession",
                                   "assembly_accession", "alteration", "sequence"])
def test_export_guard_rejects_unsupported_fields(context, field):
    candidate = copy.deepcopy(context)
    candidate["subject_scope"][field] = "unsupported"
    with pytest.raises(AssertionError):
        assert_no_experimental_payload(candidate)
