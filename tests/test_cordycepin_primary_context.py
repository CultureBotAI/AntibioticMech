"""Preserve RNA endpoints and reference identities without promoting them to AST."""

import copy
import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/2026-10-12-cordycepin-primary-context.json"


@pytest.fixture(scope="module")
def context():
    return json.loads(PATH.read_text())


def test_historical_inputs_and_distinct_compounds_are_preserved(context):
    for pin in (context["predecessor"], context["preservation"]["committed_census"]):
        assert hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]
    old = json.loads((ROOT / context["predecessor"]["path"]).read_text())
    with (ROOT / context["preservation"]["committed_census"]["path"]).open() as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    assert len(rows) == len({r["path"] for r in rows}) == 2939
    by_id = {r["identifier"]: r for r in rows}
    assert len(by_id) == 2939
    for key, identifier, inchi_key in [
        ("compound", "CHEBI:29014", "OFEZSBMBBKLLBJ-BAJZRUMYSA-N"),
        ("distinct_metabolite", "CHEBI:52316", "NLIHPCYXRYQPSD-BAJZRUMYSA-N"),
    ]:
        row = context[key]
        assert row == old[key]
        assert row["identifier"] == identifier and row["standard_inchi_key"] == inchi_key
        assert (row["path"], row["sha256"]) == (
            by_id[identifier]["path"], by_id[identifier]["record_sha256"],
        )


def test_rna_response_is_not_imported_as_growth_resistance(context):
    assert context["curation_decision"] == "HOLD_RESISTANCE_CURATION_RNA_ENDPOINT_NOT_AST"
    assert not context["curated"] and not context["primary_review_complete"]
    rows = {r["source_gene"]: r for r in context["determinations"]}
    assert len(context["determinations"]) == len(rows) == 4
    assert set(rows) == {"ADO1", "ADK1", "NRT1", "RPB1"}
    assert all("ALTERNATIVE_POLYADENYLATION" in r["endpoint"] for r in rows.values())
    assert all(not r["growth_resistance_supported_by_this_panel"] for r in rows.values())
    assert rows["ADK1"]["evidence_type"] == "NEGATIVE_FUNCTIONAL_COMPARISON_RNA_ENDPOINT"
    assert "did not prevent" in rows["ADK1"]["finding"]
    assert "mildly" in rows["NRT1"]["finding"]
    assert not rows["NRT1"]["direct_cordycepin_transport_measured"]
    assert "Figure 6B" in rows["RPB1"]["location"]
    boundary = context["endpoint_boundaries"]
    assert boundary["growth_panel_subject"] == "BY4741"
    assert boundary["wild_type_growth_panel"] == "Figure 4 - figure supplement 2F"
    assert boundary["combination_panel"] == "Figure 6D"
    assert boundary["separate_agent_comparison_panel"] == "Figure 6G"
    for field in (
        "growth_panel_is_matched_gene_perturbation_ast", "numeric_ast_imported",
        "exposure_concentrations_converted_to_mic", "clinical_categories_inferred",
        "old_growth_findings_validated_by_later_citation",
    ):
        assert boundary[field] is False


@pytest.mark.parametrize("gene,canonical,aliases,accession,locus,sgd,ev,sv", [
    ("NRT1", "NRT1", ["THI71"], "Q08485", "YOR071C", "S000005597", 159, 1),
    ("RPB1", "RPO21", ["RPB1", "RPB220", "SUA8"], "P04050", "YDL140C", "S000002299", 255, 2),
])
def test_new_reference_aliases_and_versioned_requests(
    context, gene, canonical, aliases, accession, locus, sgd, ev, sv,
):
    row, = [r for r in context["new_reference_proteins"] if r["source_gene"] == gene]
    assert (row["canonical_gene"], row["aliases"]) == (canonical, aliases)
    assert row["protein_accession"] == "UniProtKB:" + accession
    assert (row["reference_locus"], row["sgd_id"]) == (locus, "SGD:" + sgd)
    assert (row["entry_version"], row["sequence_version"]) == (ev, sv)
    assert row["reviewed"] and row["scope"] == "REFERENCE_IDENTITY_ONLY"
    assert not row["experimental_assignment"] and not row["returned_references_cite_turner_2021"]
    assert row["reference_taxon_id"] == "NCBITaxon:559292"
    request = context["uniprot"]["requests"][row["request_index"]]
    assert request["status"] == 200 and request["release"] == "2026_03"
    assert request["total_results"] == 1 and request["pagination_complete"]
    url = urlsplit(request["url"])
    assert (url.scheme, url.hostname, url.path) == (
        "https", "rest.uniprot.org", "/uniprotkb/search",
    )
    params = parse_qs(url.query)
    assert params["query"] == [f"gene_exact:{gene} AND organism_id:559292 AND reviewed:true"]
    assert params["fields"] == [
        "accession,reviewed,protein_name,gene_names,organism_id,organism_name,"
        "xref_sgd,lit_pubmed_id,sequence_version,version",
    ]


def test_reused_references_and_taxonomy_are_not_experimental_alleles(context):
    old = json.loads((ROOT / context["predecessor"]["path"]).read_text())
    assert context["reused_reference_proteins"] == old["reference_proteins"]
    assert context["taxonomy"] == old["taxonomy"]
    previous = old["uniprot"]["request"]
    for key in ("path", "sha256", "body_sha256", "url", "retrieved_at", "status"):
        assert context["uniprot"]["reused_request"][key] == previous[key]
    subject = context["subject_context"]
    assert subject["species_taxon_id"] == "NCBITaxon:4932"
    assert subject["paper_background_labels"] == ["BY4741", "W303"]
    assert subject["focal_genes_checked_in_table_1"] == ["ADO1", "ADK1", "NRT1"]
    for field in (
        "reference_strain_is_experimental_subject", "focal_gene_rows_present_in_table_1",
        "exact_experimental_proteins_assigned", "exact_experimental_alleles_assigned",
        "experimental_genome_or_sample_ids_assigned",
    ):
        assert subject[field] is False
    discrepancy = subject["source_label_discrepancy"]
    assert (discrepancy["strain_column"], discrepancy["body_and_genotype_column"]) == (
        "rbp1-1", "rpb1-1",
    )
    assert discrepancy["resolution"].startswith("UNRESOLVED_")


def test_native_assets_and_visual_review_scope_are_explicit(context):
    primary = context["primary"]
    assert primary["doi"] == "10.7554/eLife.65331"
    expected = {
        "elife-65331-v1.pdf": "242ad1fa407ea1858b9131e64521edfc9519c30dc400dabbea587d41f4a5ad7e",
        "elife-65331-v1.xml": "469d4dc296c8c27c34bbda6f8d80a2cbbc89351cd64422754fb928676a638d7f",
        "elife-65331-fig4-figsupp2-v1.tif": (
            "3de99cb52a226879315de7e7d1d5203ca81c6c032a22a18adb278287db7bc6f3"
        ),
    }
    assert {Path(a["path"]).name: a["sha256"] for a in primary["assets"]} == expected
    for asset in primary["assets"]:
        assert asset["status"] == 200 and not asset["redirects_followed"]
        assert urlsplit(asset["url"]).hostname in {
            "cdn.elifesciences.org", "raw.githubusercontent.com",
        }
    assert primary["pdf_pages"] == 35
    assert primary["pdf_pages_visually_inspected_one_based"] == [10, 13]
    assert primary["supplement_figure_visually_inspected"] == "Figure 4 - figure supplement 2"
    assert "Pillow" in primary["rendering_note"] and "rejected" in primary["rendering_note"]
    assert "micro sign" in primary["extraction_note"]
    for field in ("whole_paper_review_complete", "whole_supplement_review_complete",
                  "source_workbooks_inspected"):
        assert primary[field] is False
    earlier = {r["year"]: r for r in context["earlier_primary_leads"]}
    assert earlier[2001]["reference"] == "PMID:11223943"
    assert earlier[2001]["review_scope"] == "ABSTRACT_ONLY"
    assert earlier[2009]["decision"] == "PREDECESSOR_HOLD_UNCHANGED"
    assert all(not r["primary_figures_verified"] for r in earlier.values())


def assert_no_experimental_payload(value):
    forbidden = {
        "sequence", "features", "variant", "alteration", "construct", "primer",
        "mic", "mic_value", "disk_diffusion", "strain_taxon_id",
        "assembly_accession", "biosample_accession", "bioproject_accession",
        "sra_accessions", "experimental_protein_accession",
    }
    if isinstance(value, dict):
        assert not forbidden.intersection(value)
        for child in value.values():
            assert_no_experimental_payload(child)
    elif isinstance(value, list):
        for child in value:
            assert_no_experimental_payload(child)


def test_reference_only_export_has_no_experimental_payload(context):
    assert_no_experimental_payload(context)
    assert not context["uniprot"]["sequence_or_variant_data_exported"]


@pytest.mark.parametrize("field", [
    "assembly_accession", "biosample_accession", "bioproject_accession", "sra_accessions",
    "mic", "strain_taxon_id", "experimental_protein_accession",
])
def test_reference_only_guard_rejects_canonical_experimental_fields(context, field):
    candidate = copy.deepcopy(context)
    candidate["subject_context"][field] = "unsupported"
    with pytest.raises(AssertionError):
        assert_no_experimental_payload(candidate)


def test_scope_and_deferrals_are_unchanged(context):
    preservation = context["preservation"]
    assert preservation["base_commit"] == "18165f54cc13f9321330e34bdab71fd5bc03b05b"
    assert preservation["records_checked"] == preservation["records_unchanged"] == 2939
    assert preservation["ignored_files_included"]
    for field in ("records_curated", "new_resistance_claims", "new_activity_observations",
                  "primary_reviews_completed"):
        assert preservation[field] == 0
    assert preservation["whole_corpus_status"] == "OPEN"
    limits = context["limits"]
    assert limits["issue_1040"] == "DEFERRED"
    for field in ("ncbi_requests_made", "ncbi_contact_made", "reuse_terms_review_resumed",
                  "source_adopted", "github_mutated", "full_source_assets_redistributed",
                  "new_full_qc_run"):
        assert limits[field] is False
