"""Retain genotype, dosage and paired-loss scope in the thiolutin checkpoint."""

import copy
import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import write_validated_antibiotic

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "research/2026-10-12-thiolutin"


def read(suffix):
    return json.loads(Path(str(PREFIX) + suffix).read_text())


@pytest.fixture(scope="module")
def context():
    return read("-context.json")


@pytest.fixture(scope="module")
def receipt():
    return read("-curation.json")


def test_four_qualitative_claims_reproduce_the_scoped_record_change(context, receipt, tmp_path):
    path = ROOT / receipt["record"]["path"]
    assert hashlib.sha256(path.read_bytes()).hexdigest() == receipt["record"]["sha256"]
    record = load_record(path)
    assert record["identifier"] == "CHEBI:156450"
    assert record["chemical_structure"]["standard_inchi_key"] == "MHMRAFONCSQAIA-UHFFFAOYSA-N"
    assert record["resistance_mechanisms"] == receipt["claims"] == context["qualitative_claims"]
    assert len(receipt["claims"]) == 4
    assert record["curation_history"][-1] == receipt["curation_event"]
    previous = copy.deepcopy(record)
    del previous["resistance_mechanisms"]
    previous["curation_history"].pop()
    output = tmp_path / "before.yaml"
    write_validated_antibiotic(previous, output)
    assert hashlib.sha256(output.read_bytes()).hexdigest() == context["record_before"]["sha256"]
    assert context["record_before"]["sha256"] == receipt["before"]["sha256"]
    assert not record.get("activity_spectrum")
    assert receipt["history_events_added"] == receipt["records_changed"] == 1


def test_genotypes_are_not_interchanged_and_dosage_is_not_resolved(receipt):
    by_genes = {tuple(r["gene_families"]): r for r in receipt["claims"]}
    assert set(by_genes) == {("YAP1",), ("YRR1",), ("SNQ2",), ("TRX1", "TRX2")}
    for genes in (("YAP1",), ("YRR1",)):
        note = by_genes[genes]["note"]
        assert "Mutant- or dosage-dependent" in note
        assert "Gene deletion did not reproduce" in note
        assert "distinct" in note
    snq = by_genes[("SNQ2",)]["note"]
    assert "220 and 221" in snq and "identical reported synonymous changes" in snq
    assert "not distinct protein alleles" in snq and "dosage contribution is not excluded" in snq
    assert "deletion increased sensitivity, not resistance" in snq
    paired = by_genes[("TRX1", "TRX2")]["note"]
    assert "not two independent single-gene" in paired
    assert "CKY1984 and CKY1985" in paired and "does not identify which derivative" in paired
    assert "author hypothesis" in paired
    for claim in receipt["claims"]:
        assert claim["mechanism_type"] == "UNKNOWN"
        assert claim["taxon_id"] == "NCBITaxon:4932"
        assert claim["taxon_label"] == "Saccharomyces cerevisiae"
        assert claim["assay"] == "Comparative plate growth"
        assert claim["phenotype_label"] == "Source-reported relative thiolutin resistance"
        assert claim["evidence"][0]["reference"] == "PMID:38214235"
        assert "one study" in claim["evidence"][0]["notes"]


@pytest.mark.parametrize("gene,acc,locus,sgd,entry,sequence", [
    ("YAP1", "P19880", "YML007W", "S000004466", 230, 2),
    ("YRR1", "Q12172", "YOR162C", "S000005688", 169, 1),
    ("SNQ2", "P32568", "YDR011W", "S000002418", 216, 2),
    ("TRX1", "P22217", "YLR043C", "S000004033", 219, 3),
    ("TRX2", "P22803", "YGR209C", "S000003441", 230, 3),
])
def test_five_reference_identities_are_not_experimental_proteins(
    context, gene, acc, locus, sgd, entry, sequence,
):
    row = context["reference_proteins"][gene]
    assert row["canonical_gene"] == gene and row["accession"] == "UniProtKB:" + acc
    assert (row["reference_locus"], row["sgd_id"]) == (locus, "SGD:" + sgd)
    assert (row["entry_version"], row["sequence_version"]) == (entry, sequence)
    assert row["reviewed"] and row["reference_taxon_id"] == "NCBITaxon:559292"
    assert row["scope"] == "REFERENCE_IDENTITY_ONLY" and not row["experimental_assignment"]
    assert not row["returned_bibliography_cites_qiu_2024"]


def test_reciprocal_trx_alias_queries_are_not_first_hit_assignments(context):
    refs = context["reference_proteins"]
    assert refs["TRX1"]["aliases"] == ["TRX2"]
    assert refs["TRX2"]["aliases"] == ["TRX1"]
    assert refs["TRX1"]["sgd_id"] != refs["TRX2"]["sgd_id"]
    requests = {}
    for row in context["uniprot_requests"]:
        url = urlsplit(row["url"])
        assert url.hostname == "rest.uniprot.org" and row["status"] == 200
        assert row["release"] == "2026_03" and row["pagination_complete"]
        query, = parse_qs(url.query)["query"]
        requests[query] = row
    trx = [requests[f"gene_exact:{g} AND organism_id:559292 AND reviewed:true"]
           for g in ("TRX1", "TRX2")]
    assert all(r["total_results"] == 2 for r in trx)
    assert trx[0]["body_sha256"] == trx[1]["body_sha256"]
    assert len(refs) == 5 and len(context["uniprot_requests"]) == 5
    taxa = {r["taxon_id"]: r for r in context["taxonomy"]}
    assert taxa["NCBITaxon:4932"]["rank"] == "species"
    assert taxa["NCBITaxon:559292"]["scope"] == "REFERENCE_PROTEIN_TAXON_ONLY"


def assert_no_experimental_payload(claims):
    forbidden = {"alteration", "protein_accession", "strain_taxon_id", "strain",
                 "gene_id", "sequence", "variant", "mic", "mic_value", "disk_diffusion",
                 "assembly_accession", "biosample_accession", "bioproject_accession", "sra_accessions"}
    for claim in claims:
        assert not forbidden.intersection(claim)


def test_reference_evidence_is_not_subject_metadata(receipt):
    assert_no_experimental_payload(receipt["claims"])
    assert receipt["experimental_proteins_assigned"] == receipt["experimental_genomes_assigned"] == 0
    assert receipt["numerical_ast_added"] == 0 and not receipt["whole_record_review_complete"]


@pytest.mark.parametrize("field", [
    "protein_accession", "strain_taxon_id", "assembly_accession",
    "biosample_accession", "bioproject_accession", "sra_accessions", "mic", "alteration",
])
def test_unsupported_experimental_fields_are_rejected(receipt, field):
    candidate = copy.deepcopy(receipt["claims"])
    candidate[0][field] = "unsupported"
    with pytest.raises(AssertionError):
        assert_no_experimental_payload(candidate)


def test_only_one_census_row_changes_and_totals_remain_open(context, receipt):
    reconciliation = read("-reconciliation.json")
    censuses = []
    for name in ("previous_census", "current_census"):
        pin = reconciliation[name]
        path = ROOT / pin["path"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == pin["sha256"]
        with path.open() as stream:
            rows = list(csv.DictReader(stream, delimiter="\t"))
        mapping = {r["identifier"]: r for r in rows}
        assert len(mapping) == len(rows) == 2939
        censuses.append(mapping)
    before, after = censuses
    assert set(before) == set(after)
    changed = [i for i in before if before[i] != after[i]]
    assert changed == ["CHEBI:156450"]
    assert after[changed[0]] == {
        **before[changed[0]], "record_sha256": receipt["record"]["sha256"],
        "resistance_assertions": "4", "research_status": "PENDING_PRIMARY_REVIEW",
    }
    assert sum(int(r["resistance_assertions"]) for r in after.values()) == 4851
    assert sum(int(r["resistance_assertions"]) > 0 for r in after.values()) == 310
    assert reconciliation["curator_claims"] == 96 and reconciliation["curator_records"] == 42
    assert reconciliation["records_byte_identical"] == 2938
    assert reconciliation["whole_record_reviews_completed"] == 0
    assert context["scope"]["whole_corpus_primary_review"] == "OPEN"


def test_primary_scope_and_ncbi_deferral_are_retained(context):
    primary = context["primary"]
    assert primary["doi"] == "10.1093/nar/gkad1258"
    assert primary["native_figures_inspected"] == ["1", "S1", "S3"]
    assert not primary["primer_sheet_inspected"]
    assert "S1D is a diagram" in primary["source_panel_discrepancy"]
    assert "growth panel is S1E" in primary["source_panel_discrepancy"]
    assert context["identity"]["figure_1_distinguishes_holomycin"]
    assert not context["identity"]["tested_preparation_independently_reidentified"]
    assert context["discovery"]["candidate"] == "MED:38214235"
    assert any("TRR1 and PRO3" in h for h in context["holds"])
    limits = context["guardrails"]
    assert limits["issue_1040"] == "DEFERRED"
    assert limits["ncbi_requests"] == limits["ncbi_contact"] == limits["github_mutations"] == 0
    assert not limits["reuse_terms_review_resumed"] and limits["source_adoptions"] == 0
    assert not limits["raw_source_assets_redistributed"] and not limits["sequences_or_protocols_exported"]
