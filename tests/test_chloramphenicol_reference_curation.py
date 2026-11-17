"""Keep CAT/CmlA reference identities separate from native isolate evidence."""

import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import write_validated_antibiotic

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "research/2026-10-10-chloramphenicol-references"


def semantic_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=True).encode()).hexdigest()


@pytest.fixture(scope="module")
def context():
    return json.loads(Path(str(PREFIX) + "-context.json").read_bytes())


@pytest.fixture(scope="module")
def curation():
    return json.loads(Path(str(PREFIX) + "-curation.json").read_bytes())


def test_native_association_preserves_all_prior_claims_and_fields(curation, tmp_path):
    path = ROOT / curation["record"]["path"]
    doc = load_record(path)
    assert doc["identifier"] == "CHEBI:17698"
    n = curation["existing_claims_preserved"]
    assert n == 87 and len(doc["resistance_mechanisms"]) >= n + 1
    assert doc["resistance_mechanisms"][n:n + 1] == curation["added_claims"]
    assert semantic_sha(doc["resistance_mechanisms"][:n]) == curation["preserved_resistance_claims_sha256"]
    assert doc["curation_history"].count(curation["curation_event"]) == 1
    event_index = doc["curation_history"].index(curation["curation_event"])
    assert semantic_sha(doc["curation_history"][:event_index]) == curation["preserved_history_sha256"]
    assert doc["curation_history"][event_index] == curation["curation_event"]
    other = {k: v for k, v in doc.items() if k not in {"resistance_mechanisms", "curation_history"}}
    assert semantic_sha(other) == curation["preserved_fields_sha256"]
    assert doc["curation_status"] == curation["curation_status"] == "REVIEWED"
    assert len(doc["activity_spectrum"]) == 2
    target = tmp_path / path.name
    write_validated_antibiotic(doc, target)
    assert target.read_bytes() == path.read_bytes() and load_record(target) == doc


def test_sof1_cooccurrence_is_not_exact_protein_or_individual_causation(context, curation):
    claim, = curation["added_claims"]
    assert claim["strain"] == "SOF-1" and claim["taxon_id"] == "NCBITaxon:287"
    assert claim["taxon_label"] == "Pseudomonas aeruginosa"
    assert claim["mechanism_type"] == "UNKNOWN" and claim["gene_families"] == ["cmlA-like"]
    assert claim["assay"] == "Source-reported disk diffusion"
    assert "data not shown" in claim["note"] and "not proof" in claim["note"]
    assert {e["reference"] for e in claim["evidence"]} == {"PMID:11353602"}
    assert not {"protein_accession", "alteration", "gene_id", "strain_taxon_id", "aro_id",
                "phenotype_id", "measurement_value", "assembly_accession"} & claim.keys()
    review = context["primary_reviews"]["11353602"]
    assert review["action"] == "CURATE_QUALITATIVE_NATIVE_COOCCURRENCE"
    assert review["archive"] == "AF294653.1"
    archive = context["archive_metadata"]["AF294653"]
    assert archive["version"] == 1 and archive["taxon_id"] == claim["taxon_id"]
    assert archive["sample"] is None and archive["project"] is None


def test_all_cat_references_are_preserved_without_one_representative(context):
    audit = json.loads((ROOT / context["reference_audit"]["path"]).read_bytes())
    for aro in context["selected_aro_terms"]:
        expected = {r["protein_accession"] for r in audit["terms"][aro]["reference_candidates"]}
        assert set(context["initial_term_candidates"][aro]) == expected
    assert len(context["initial_term_candidates"]["ARO:3002670"]) == 20
    assert len(context["initial_term_candidates"]["ARO:3002693"]) == 2
    assert context["extra_unsuffixed_candidates"] == ["P32482", "Q9R8B8"]
    assert len(context["reference_proteins"]) == 24
    assert context["reference_proteins"]["P20074"]["archive_links"] == []
    assert all(r["scope"] == "REFERENCE_IDENTITY_NOT_EXACT_EXPERIMENTAL_PROTEIN"
               for r in context["reference_proteins"].values())


def test_variant_cmla6_and_unsuffixed_fragment_entries_are_distinct(context):
    proteins = context["reference_proteins"]
    assert proteins["Q8GGX1"]["gene_annotations"][0]["geneName"]["value"] == "cmlA1-variant"
    assert proteins["Q933G9"]["gene_annotations"][0]["geneName"]["value"] == "CmlA6"
    assert proteins["P32482"]["gene_annotations"][0]["geneName"]["value"] == "cmlA"
    assert proteins["Q9R8B8"]["fragment"] and not proteins["P32482"]["fragment"]
    assert proteins["P32482"]["sequence_version"] == 2
    assert any(r["sequence_revision"] for r in proteins["P32482"]["citations"])
    assert context["archive_metadata"]["U12338"]["version"] == 3
    assert context["archive_metadata"]["AF078527"]["version"] == 1


def test_later_variant_submissions_do_not_inherit_ilt3_experiment(context):
    links = {r["nucleotide_accession"]: r for r in context["reference_proteins"]["Q8GGX1"]["archive_links"]}
    expected = {"AF458080": "ILT-3", "HM043570": "D-03", "HQ880266": "NF808096"}
    assert set(links) == set(expected)
    for accession, strain in expected.items():
        comments = links[accession]["strain_reference_bindings"]
        assert {c["strain"] for c in comments} == {strain}
        assert all(links[accession]["archive_protein_id"] in c["evidence_protein_ids"] for c in comments)
        if accession != "AF458080":
            assert all(c["citation_type"] == "submission" for c in comments)


def test_laboratory_archive_is_not_native_genome(context):
    row = context["archive_metadata"]["X51450"]
    assert row["scope"] == "LABORATORY_MATERIAL_NOT_NATIVE_GENOME"
    assert row["taxon_id"] == "NCBITaxon:31790"
    protein = context["reference_proteins"]["P00485"]
    assert protein["taxon_id"] == "NCBITaxon:1280"
    link, = [r for r in protein["archive_links"] if r["nucleotide_accession"] == "X51450"]
    assert link["molecule_type"] == "Other_DNA" and not link["archive_taxon_matches_uniprot"]
    assert not row["experimental_genome_assignment"]


@pytest.mark.parametrize("taxid,rank", [("176299", "strain"), ("889971", "strain"),
                                        ("107673", "subspecies"), ("42897", "serotype"),
                                        ("90370", "no rank"), ("79880", "species")])
def test_taxonomic_ranks_are_not_silently_promoted_to_species(context, taxid, rank):
    assert context["taxonomy"][taxid]["rank"] == rank
    assert context["taxonomy"][taxid]["active"]


def test_historical_names_and_archive_ranks_are_preserved(context):
    assert "Bacillus clausii" in context["taxonomy"]["79880"]["other_names"]
    assert "Bacillus clausii" not in context["taxonomy"]["79880"]["synonyms"]
    assert context["reference_proteins"]["P62578"]["taxon_id"] == "NCBITaxon:107673"
    assert context["archive_metadata"]["M37690"]["taxon_id"] == "NCBITaxon:471"
    assert context["reference_proteins"]["P62579"]["taxon_id"] == "NCBITaxon:470"
    assert context["reference_proteins"]["P62580"]["taxon_id"] == "NCBITaxon:90370"
    assert context["archive_metadata"]["AL513383"]["taxon_id"] == "NCBITaxon:220341"


def test_abstracts_and_comment_relations_do_not_become_primary_curation(context):
    reviews = context["primary_reviews"]
    assert reviews["19459958"]["inspection"] == "PUBLISHER_ABSTRACT_ONLY"
    assert reviews["19459958"]["action"] == "RETAIN_LEAD_NO_BIOLOGICAL_WRITE"
    assert reviews["12019143"]["relation"] == "COMMENT_ON"
    assert reviews["12019143"]["related_pmid"] == "11600350"
    assert "not a chloramphenicol allele correction" in reviews["12019143"]["finding"]
    assert not any(r["whole_paper_review_complete"] for r in reviews.values())


def test_request_scope_is_sequence_free_and_ncbi_deferred(context):
    assert len(context["requests"]) == 95 and len(context["bibliography"]) == 32
    assert len(context["archive_metadata"]) == 35
    for key, row in context["requests"].items():
        url = urlsplit(row["url"])
        assert url.hostname in {"rest.uniprot.org", "www.ebi.ac.uk"} and url.scheme == "https"
        assert row["status"] == 200 and row["sha256"] == row["cache"]["sha256"]
        if key.startswith("protein-"):
            assert "sequence" not in parse_qs(url.query)["fields"][0].split(",")
        if key.startswith("ena-"):
            assert url.path.startswith("/ena/browser/api/summary/")
    assert context["reference_release"] == "2026_03"


def test_census_changes_only_chloramphenicol():
    reconciliation = json.loads(Path(str(PREFIX) + "-checkpoint-reconciliation.json").read_bytes())
    ledgers = []
    for key in ("previous_ledger", "current_ledger"):
        pin = reconciliation[key]
        path = ROOT / pin["path"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == pin["sha256"]
        with path.open(newline="") as stream:
            ledgers.append(list(csv.DictReader(stream, delimiter="\t")))
    old, new = ledgers
    assert len(old) == len(new) == 2939
    changed = [(a, b) for a, b in zip(old, new, strict=True) if a != b]
    assert len(changed) == 1
    a, b = changed[0]
    assert b["identifier"] == "CHEBI:17698"
    assert {key for key in a if a[key] != b[key]} == {"record_sha256", "resistance_assertions"}
    assert int(b["resistance_assertions"]) == int(a["resistance_assertions"]) + 1
    assert reconciliation["current_counts"]["resistance_assertions"] == 4821
    assert reconciliation["curator_claims"] == 66 and reconciliation["curator_records"] == 36


def test_chemical_identity_embeddings_and_export_scope(context, curation):
    assert context["chemical_identity"]["standard_inchi_key"] == "WIIZWVCIJKGZOK-RKDXNWHRSA-N"
    assert context["chemical_identity"]["key_matches_smiles_and_inchi"]
    assert not context["chemical_identity"]["tested_preparation_independently_reidentified"]
    assert curation["embedding_documents_changed"] == 0
    assert curation["embedding_fingerprint"] == "18ff581531b8bd9d"
    assert context["scope"]["corpus_records"] == 2939 and context["scope"]["whole_records_completed"] == 0
    assert curation["whole_corpus_primary_review"] == "OPEN"
    for value in (context, curation):
        assert all(value[key] == 0 for key in (
            "experimental_proteins_assigned", "exact_alleles_assigned", "assembly_accessions_assigned",
            "numerical_ast_added", "ncbi_endpoint_requests", "source_adoptions", "github_mutations"))

    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    forbidden = {"sequence", "variants", "alteration", "constructs", "primers", "protocol",
                 "coordinates", "mic", "measurement_value", "smiles", "standard_inchi"}
    assert not forbidden & set(keys(context))
    assert not forbidden & set(keys(curation))
