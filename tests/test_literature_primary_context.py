"""Keep archive identity, cited evidence and experimental subjects distinct."""

import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-09-literature-primary-context.json").read_bytes())


def test_scope_is_a_followup_not_whole_record_completion(dossier):
    assert len(dossier["terms"]) == 3 and len(dossier["records"]) == 5
    assert sum(len(t["record_memberships"]) for t in dossier["terms"].values()) == 6
    assert dossier["summary"]["whole_corpus_primary_review"] == "OPEN"
    assert dossier["summary"]["whole_records_completed"] == 0
    assert dossier["summary"]["biological_records_changed"] == 0
    assert all(r["complete_collection_aware_record_read"] for r in dossier["records"])
    assert all(not r["tested_preparation_exact_structure_independently_established"]
               for r in dossier["records"])


def test_reference_projections_reproduce_prior_public_audit(dossier):
    pinned = dossier["inputs"]["literature_audit"]
    raw = (ROOT / pinned["path"]).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == pinned["sha256"]
    previous = json.loads(raw)
    for acc, item in dossier["proteins"].items():
        assert item["reference"] == previous["proteins"][acc]
        assert not item["reference"]["exact_allele_assignment"]
        assert not item["reference"]["experimental_subject_assignment"]
        term = dossier["terms"][item["source_term"]]
        assert term["reference_candidate"] == acc
        assert term["record_memberships"] == previous["terms"][item["source_term"]]["record_memberships"]


@pytest.mark.parametrize("acc,taxid,rank", [
    ("Q6A150", "58095", "no rank"), ("D8L9Z0", "32019", "subspecies"), ("F2RC64", "953739", "strain")])
def test_reference_taxonomy_rank_is_preserved(dossier, acc, taxid, rank):
    protein = dossier["proteins"]["UniProtKB:" + acc]["reference"]
    archive = dossier["reference_archives"]["UniProtKB:" + acc]
    assert protein["reference_taxon_id"] == archive["reference_taxon_id"] == "NCBITaxon:" + taxid
    assert protein["taxonomy_rank"] == archive["reference_taxonomy_rank"] == rank


def test_archive_accessions_are_not_automatically_assemblies_or_tested_genomes(dossier):
    expected = {"Q6A150": ("AJ809407", "CAH10847.1"), "D8L9Z0": ("FN594949", "CBH51824.1"),
                "F2RC64": ("FR845719", "CCA59315.1")}
    for acc, (nucleotide, protein) in expected.items():
        row = dossier["reference_archives"]["UniProtKB:" + acc]
        assert row["uniprot_nucleotide_xref"] == row["ena_sequence_accession"] == nucleotide
        assert row["ena_sequence_version"] == 1 and row["archive_protein_id"] == protein
        assert row["assembly_accession_reported_by_summary"] is None
        assert row["experimental_genome_assignment"] is False
    genome = dossier["reference_archives"]["UniProtKB:F2RC64"]
    assert genome["description_indicates_complete_genome"] is True
    assert genome["reference_project"] == "PRJNA62209" and genome["reference_sample"] == "SAMEA3138410"
    assert genome["source_definition_pmid_in_archive"] is False
    assert "PMID:21463507" in genome["archive_publication_ids"]
    assert "PMID:35907401" not in genome["archive_publication_ids"]


def test_reference_strains_are_bound_to_each_citation(dossier):
    rows = dossier["proteins"]["UniProtKB:F2RC64"]["citation_scoped_strains"]
    by_pmid = {identifier: row["strain_annotations"] for row in rows for identifier in row["citation_ids"]
               if identifier.startswith("PMID:")}
    assert by_pmid["PMID:34964291"] == []
    assert by_pmid["PMID:35907401"] == [
        "ATCC 10712 / CBS 650.69 / DSM 40230 / JCM 4526 / NBRC 13096 / PD 04745"]
    assert all(not p["reference_strain_annotations_are_experimental_assignments"]
               for p in dossier["proteins"].values())


def test_aada_abstract_is_not_primary_results_review(dossier):
    row = dossier["primary_review"]["PMID:15761062"]
    assert row["source_isolate_label"] == row["reference_citation_strain_label"] == "231"
    assert row["scope"] == "PUBLISHER_ABSTRACT_ONLY"
    assert not row["primary_results_reviewed"] and not row["exact_experimental_protein_assignment"]
    assert "242" in row["finding"]


def test_ant_context_does_not_merge_labels_or_infer_measured_biochemistry(dossier):
    row = dossier["primary_review"]["PMID:20479200"]
    assert row["primary_results_reviewed"] is True and row["whole_paper_review_complete"] is False
    assert row["source_donor_strain"] == "IMD523-06" and row["source_assay_host_strain"] == "1516477"
    assert row["reference_citation_strain_label"] == "IMD 523"
    assert not row["strain_label_equivalence_independently_established"]
    assert not row["native_reference_is_exact_experimental_protein"]
    assert "homology-based" in row["finding"] and "not a direct biochemical measurement" in row["finding"]
    archive = dossier["reference_archives"]["UniProtKB:D8L9Z0"]
    assert row["paper_reported_nucleotide_accession"] == archive["ena_sequence_accession"]
    assert row["source_archive_link_verified"] is True
    assert archive["source_definition_pmid_in_archive"] is True


def test_held_locus_evidence_is_not_an_independent_resistance_experiment(dossier):
    row = dossier["primary_review"]["PMID:34964291"]
    assert row["reference_locus"] == "SVEN_6029" and row["locus_crosswalk"] == "UniProtKB:F2RC64"
    assert dossier["proteins"][row["locus_crosswalk"]]["ordered_locus_names"] == [row["reference_locus"]]
    assert row["cited_resistance_study"] == {
        "pmid": "PMID:35907401", "doi": "DOI:10.1016/j.molcel.2022.06.019",
        "xml_reference_id": "mbo31251-bib-0055", "is_independent_phenotype_replicate": False}
    assert row["repository_xml_status"] == "HTTP_200_OPEN_ACCESS_COPY"
    assert row["repository_license"] == "CC-BY-4.0"
    assert row["primary_results_reviewed"] is True
    assert row["whole_paper_review_complete"] is False and row["figures_visually_reviewed"] is False
    assert dossier["primary_review"]["PMID:35907401"]["primary_results_reviewed"] is False


def test_provider_and_access_failures_remain_explicit(dossier):
    for pmid in ("PMID:35907401", "PMID:34964291"):
        status = dossier["primary_review"][pmid]["publisher_access_status"]
        assert status == "HTTP_403_NOT_RETRIED_OR_BYPASSED"
    for row in dossier["bibliography"].values():
        assert urlparse(row["url"]).netloc == "www.ebi.ac.uk" and row["status"] == 200
        assert row["primary_results_established_by_metadata"] is False
    for row in dossier["reference_archives"].values():
        assert urlparse(row["url"]).netloc == "www.ebi.ac.uk" and row["status"] == 200
    for row in dossier["proteins"].values():
        assert urlparse(row["request"]["url"]).netloc == "rest.uniprot.org"
        assert row["request"]["release"] == "2026_03"


def test_public_export_omits_sequence_and_operational_fields(dossier):
    forbidden = {"sequence", "sequenceLength", "referencePositions", "abstractText", "mic", "primers",
                 "constructs"}

    def visit(value):
        if isinstance(value, dict):
            assert not forbidden.intersection(value)
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)

    visit(dossier)
    assert dossier["summary"]["exact_experimental_allele_assignments"] == 0
    assert dossier["summary"]["experimental_genome_assignments"] == 0
