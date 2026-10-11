"""Primary context must preserve negative results and reference/subject boundaries."""

import json
from pathlib import Path
from urllib.parse import urlsplit

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-09-transport-primary-context.json").read_bytes())


@pytest.mark.parametrize("accession,symbol,locus,taxon,version", [
    ("P38124", "FLR1", "YBR008C", "559292", (171, 1)),
    ("P19880", "YAP1", "YML007W", "559292", (230, 2)),
    ("P39109", "YCF1", "YDR135C", "559292", (236, 2)),
    ("P53047", "RTA1", "YGR213C", "559292", (148, 1)),
    ("O06967", "bmrA", "BSU34820", "224308", (169, 1)),
])
def test_reference_identifiers_are_not_experimental_assignments(
    dossier, accession, symbol, locus, taxon, version,
):
    row, = [r for r in dossier["reference_proteins"] if r["accession"] == "UniProtKB:" + accession]
    assert row["gene_symbol"] == symbol and row["reference_loci"] == [locus]
    assert row["reference_taxon_id"] == "NCBITaxon:" + taxon
    assert (row["entry_audit"]["entryVersion"], row["entry_audit"]["sequenceVersion"]) == version
    assert row["experimental_assignment"] is False
    assert row["entry_type"] == "UniProtKB reviewed (Swiss-Prot)"


def context(dossier, pmid):
    row, = [r for r in dossier["primary_contexts"] if r["reference"] == "PMID:" + pmid]
    return row


def test_canthi_primary_figures_and_negative_comparison(dossier):
    row = context(dossier, "23912082")
    assert row["medium"] == "PRIMARY_PAPER_REPRINT_IN_AUTHOR_UNIVERSITY_THESIS"
    assert row["paper_pdf_pages_one_based"] == list(range(68, 75))
    assert row["figures_visually_inspected"] == [1, 3, 4, 5]
    assert row["background_labels"] == ["G175-W303", "BY4742 / EUROSCARF Y10000", "YPH250"]
    findings = " ".join(row["findings"])
    assert "YCF1 does not explain" in findings and "basal FLR1 comparison was negative" in findings
    assert "Baseline growth complicates" in findings
    ycf1, = [r for r in dossier["reference_proteins"] if r["gene_symbol"] == "YCF1"]
    assert ycf1["role"] == "NEGATIVE_COMPARISON_REFERENCE"
    assert row["curation_disposition"] == "READY_FOR_QUALITATIVE_GENE_ASSOCIATION_CURATION"
    assert row["exact_experimental_allele"] == "UNRESOLVED" and row["numeric_ast_curated"] is False


def test_conflicting_source_locus_label_is_not_an_alias(dossier):
    caveat = context(dossier, "23912082")["locus_label_caveat"]
    assert caveat == {"gene": "FLR1", "table_1": "YBR008C", "table_2": "YRR008C",
                      "uniprot_reference_locus": "YBR008C", "alias_created": False}
    assert not any("YRR008C" in r["reference_loci"] for r in dossier["reference_proteins"])


def test_rta1_historical_deposit_and_citation_strain_are_separate(dossier):
    primary = context(dossier, "8660468")
    assert primary["medium"] == "PUBLISHER_ABSTRACT_ONLY"
    assert primary["original_deposit"] == {
        "database": "EMBL", "accession": "X84736", "protein_id": "CAA59227.1",
        "uniprot_reference": "UniProtKB:P53047"}
    protein, = [r for r in dossier["reference_proteins"] if r["gene_symbol"] == "RTA1"]
    assert protein["focal_citation_context"] == [{
        "reference": "PMID:8660468", "strain_comments": ["ATCC 28383 / FL100 / VTT C-80102"]}]
    assert protein["reference_taxon_id"] == "NCBITaxon:559292"
    assert "S288c" in protein["reference_organism"]
    assert protein["focal_papers_not_in_entry_references"] == ["PMID:22129104"]
    assert primary["curation_disposition"].startswith("PRIMARY_RESULTS_PENDING")


def test_rta1_primary_context_does_not_invent_efflux_or_join_subjects(dossier):
    row = context(dossier, "22129104")
    assert [r["figure"] for r in row["figures_visually_inspected"]] == [2, 7]
    assert all(r["visually_inspected"] for r in row["figures_visually_inspected"])
    text = " ".join(row["findings"])
    assert "not established as drug efflux" in text and "RSB1" in text
    assert "JD52" in text and "FY wild type" in text
    assert "Do not combine" in text
    assert "stereospecific" in row["compound_scope"]


def test_cervimycin_reference_genome_is_not_an_experimental_deposit(dossier):
    row = context(dossier, "21077936")
    assert row["source_subject_labels"] == ["8R", "IR"]
    assert row["source_parent"] == "Bacillus subtilis 168"
    assert row["source_species_taxon"] == "NCBITaxon:1423"
    assert row["paper_reference_genome"] == "AL009126.3"
    assert row["experimental_genome_accessions"] == []
    assert row["figures_visually_inspected"] == [] and row["supplement_inspected"] is False
    assert "unpublished" in " ".join(row["findings"])
    assert row["medium"] == "INDEXED_PRIMARY_RESULTS_TEXT_DIRECT_PDF_ACCESS_FAILED"


@pytest.mark.parametrize("taxid,name,rank,parent", [
    ("4932", "Saccharomyces cerevisiae", "species", 4930),
    ("559292", "Saccharomyces cerevisiae (strain ATCC 204508 / S288c)", "strain", 4932),
    ("1423", "Bacillus subtilis", "species", 653685),
    ("224308", "Bacillus subtilis (strain 168)", "strain", 135461),
])
def test_taxonomy_rank_and_lineage(dossier, taxid, name, rank, parent):
    row = dossier["taxonomy"][taxid]
    assert row["active"] is True and row["scientificName"] == name
    assert row["rank"] == rank and row["parent"]["taxonId"] == parent
    assert 4932 in dossier["taxonomy"]["559292"]["lineage_taxids"]
    assert 1423 in dossier["taxonomy"]["224308"]["lineage_taxids"]


def test_bounded_metadata_queries_and_access_failures_are_auditable(dossier):
    receipts = dossier["uniprot_requests"]
    assert len(receipts) == 7
    assert all(r["release"] == "2026_03" for r in receipts)
    assert all(urlsplit(r["url"]).hostname == "rest.uniprot.org" for r in receipts)
    assert sorted(r["results"] for r in receipts if "query" in r) == [1, 1, 3]
    assert all(r["complete_for_query"] and not r["biological_absence_inferred"]
               for r in receipts if "query" in r)
    assert [r["status"] for r in dossier["retrieval_attempts"]] == [403, 301, 200, 403, 200]
    assert dossier["retrieval_attempts"][2]["is_pdf"] is True
    assert all(len(r["cache"]["sha256"]) == 64 for r in receipts)


@pytest.mark.parametrize("identifier", ["CHEBI:3363", "CHEBI:77845", "antibioticmech:aro-72f1180eb7"])
def test_exact_record_membership_remains_current(dossier, identifier):
    row, = [r for r in dossier["records"] if r["identifier"] == identifier]
    doc = load_record(ROOT / row["path"])
    assert doc["identifier"] == identifier
    assert doc["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"]
    assert len(row["record_sha256"]) == 64


def test_primary_review_backlog_and_corpus_scope_remain_open(dossier):
    pending = dossier["pending_discovery_candidates"]
    assert {r["citation"]["pmid"] for r in pending} == {
        "41108078", "36364991", "26518191", "38722162", "36173303"}
    assert {r["primary_review_status"] for r in pending} == {"PENDING_NOT_REJECTED_BY_TITLE"}
    assert dossier["scope"] == {
        "corpus_records": 2939, "record_memberships": 3, "primary_publications_considered": 4,
        "reference_proteins": 5, "whole_records_completed": 0, "full_corpus_primary_review": "OPEN"}
    assert dossier["preservation"]["record_hashes_verified"] == 2939
    assert dossier["preservation"]["ignored_files_included"] is True
    assert dossier["preservation"]["biological_record_changes"] == 0
    assert dossier["preservation"]["curation_events_added"] == 0


def test_export_omits_experimental_specifications(dossier):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not set(keys(dossier)) & {
        "sequence", "variants", "alteration", "constructs", "protocol", "primers",
        "coordinates", "measurement_value", "mic", "resistance_mechanisms", "activity_spectrum"}
    assert "CC BY 4.0" in dossier["attribution"]
    assert "No NCBI request" in " ".join(dossier["limitations"])
