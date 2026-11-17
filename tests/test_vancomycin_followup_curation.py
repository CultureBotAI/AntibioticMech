"""Keep native evidence strength, archive succession and reference scope distinct."""

import csv
import hashlib
import json
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import write_validated_antibiotic

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "research/2026-10-10-vancomycin-followup"


def semantic_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=True).encode()).hexdigest()


@pytest.fixture(scope="module")
def context():
    return json.loads(Path(str(PREFIX) + "-context.json").read_bytes())


@pytest.fixture(scope="module")
def curation():
    return json.loads(Path(str(PREFIX) + "-curation.json").read_bytes())


def test_current_claims_preserve_the_prior_record_and_roundtrip(curation, tmp_path):
    path = ROOT / curation["record"]["path"]
    doc = load_record(path)
    n = curation["existing_claims_preserved"]
    assert n == 22 and len(doc["resistance_mechanisms"]) >= n + 5
    assert semantic_sha(doc["resistance_mechanisms"][:n]) == curation["preserved_resistance_claims_sha256"]
    assert doc["resistance_mechanisms"][n:n + 5] == curation["added_claims"]
    history_index = curation["prior_history_events"]
    assert history_index == 15
    assert semantic_sha(doc["curation_history"][:history_index]) == curation["preserved_history_sha256"]
    assert doc["curation_history"][history_index] == curation["curation_event"]
    other = {k: v for k, v in doc.items() if k not in {"resistance_mechanisms", "curation_history"}}
    assert semantic_sha(other) == curation["preserved_fields_sha256"]
    assert doc["curation_status"] == "SEEDED"
    target = tmp_path / path.name
    write_validated_antibiotic(doc, target)
    assert target.read_bytes() == path.read_bytes() and load_record(target) == doc


@pytest.mark.parametrize("strain,taxid,gene,pmid,precursors", [
    ("BM4405", "1351", "vanE", "10471558", True),
    ("N00-410", "1351", "vanE", "12019119", False),
    ("N06-0364", "1351", "vanL", "18458129", False),
    ("UCN71", "1352", "vanN", "21807981", True),
    ("10/96A", "1352", "vanD", "12499162", True),
])
def test_native_subject_and_evidence_scope(context, curation, strain, taxid, gene, pmid, precursors):
    claim, = [c for c in curation["added_claims"] if c["strain"] == strain]
    assert claim["taxon_id"] == "NCBITaxon:" + taxid and claim["gene_families"] == [gene]
    assert {e["reference"] for e in claim["evidence"]} == {"PMID:" + pmid}
    assert context["primary_sources"][pmid]["native_precursor_evidence"] == precursors
    assert not context["primary_sources"][pmid]["isolated_ligase_causation_asserted"]
    assert claim["mechanism_type"] == ("ANTIBIOTIC_TARGET_ALTERATION" if precursors else "UNKNOWN")


def test_vanl_cooccurrence_is_not_functional_validation(curation):
    claim, = [c for c in curation["added_claims"] if c["strain"] == "N06-0364"]
    assert claim["mechanism_type"] == "UNKNOWN" and "co-occurrence" in claim["label"]
    assert "explicitly leaves functionality unproven" in claim["note"]
    assert "not a demonstrated biochemical route or a new clinical category" in claim["note"]
    assert claim["assay"] == "Broth microdilution and Etest"


def test_archive_replacement_is_explicit_and_bidirectional(context):
    archive = context["archive_replacement"]
    old, new = archive["archive_summary"], archive["replacement_metadata"]
    assert old["accession"] == "AF430807" and old["statusDescription"] == "suppressed"
    assert old["newAccession"] == new["accession"] == "FJ872411"
    assert new["statusDescription"] == "public" and "AF430807" in new["secondaryAccession"]
    assert all(r["taxon"] == 1351 and {"source": "PUBMED", "pId": "12019119"} in r["publications"]
               for r in (old, new))
    assert archive["disposition"] == "EXPLICIT_ARCHIVE_REPLACEMENT_AND_SECONDARY_ACCESSION_RELATION"
    assert any("not proof of unchanged sequence" in note for note in archive["limits"])


def test_vane_subject_labels_and_fragments_remain_distinct(context, curation):
    assert context["reference_proteins"]["Q9S4K1"]["fragment"]
    source, = [c for c in curation["added_claims"] if c["strain"] == "N00-410"]
    assert "without transferring BM4405 precursor findings" in source["note"]
    assert "Source N00-410 and reference N00-0410" in source["note"]
    bindings = context["reference_proteins"]["Q93A46"]["archive_links"][0]["strain_reference_bindings"]
    assert {b["strain"] for b in bindings} == {"N00-0410"}


def test_vann_reference_entry_does_not_merge_different_isolates(context, curation):
    links = {r["nucleotide_accession"]: r for r in context["reference_proteins"]["G4XFK8"]["archive_links"]}
    assert {b["strain"] for b in links["JF802084"]["strain_reference_bindings"]} == {"UCN71"}
    assert {b["strain"] for b in links["AB701345"]["strain_reference_bindings"]} == {"121.1"}
    claim, = [c for c in curation["added_claims"] if c["strain"] == "UCN71"]
    assert "it is not assigned to UCN72" in claim["note"]
    assert "UCN72" not in {c["strain"] for c in curation["added_claims"]}


def test_vand_archive_citations_stay_source_bound(context, curation):
    links = {r["nucleotide_accession"]: r for r in context["reference_proteins"]["Q9EZQ9"]["archive_links"]}
    assert {b["citation_id"] for b in links["AF277571"]["strain_reference_bindings"]} == {"11083656"}
    assert {b["citation_id"] for b in links["AY082011"]["strain_reference_bindings"]} == {"12499162"}
    claim, = [c for c in curation["added_claims"] if c["strain"] == "10/96A"]
    assert claim["assay"] == "MIC determination (Steers et al. method)"
    assert "Other native strains and laboratory-host findings are not merged" in claim["note"]


def test_reference_projection_preserves_prior_metadata(context):
    pin = context["reference_dossier"]
    path = ROOT / pin["path"]
    assert hashlib.sha256(path.read_bytes()).hexdigest() == pin["sha256"]
    original = json.loads(path.read_bytes())
    assert len(context["reference_proteins"]) == 5
    for accession, row in context["reference_proteins"].items():
        assert row == original["reference_proteins"][accession]
        assert not row["experimental_assignment"] and not row["whole_cluster_assignment"]
        assert context["reference_requests"][row["query_key"]] == original["requests"][row["query_key"]]
    for key, row in context["archive_context"].items():
        assert row == original["archive_metadata"][key] and not row["experimental_genome_assignment"]


@pytest.mark.parametrize("taxid,species", [
    ("1351", "Enterococcus faecalis"), ("1352", "Enterococcus faecium")])
def test_species_grounding_does_not_mint_strain_taxids(context, curation, taxid, species):
    taxon = context["taxonomy"][taxid]
    assert taxon["active"] and taxon["rank"] == "species" and taxon["scientificName"] == species
    selected = [c for c in curation["added_claims"] if c["taxon_id"] == "NCBITaxon:" + taxid]
    assert selected and all(c["taxon_label"] == species and "strain_taxon_id" not in c for c in selected)


def test_no_exact_experimental_protein_allele_or_new_ast(curation):
    forbidden = {"protein_accession", "alteration", "assembly_accession", "biosample_accession",
                 "bioproject_accession", "phenotype_id", "measurement_value", "mic_value", "mic_units"}
    for claim in curation["added_claims"]:
        assert not forbidden & claim.keys()
        assert "No exact experimental protein, allele or genome is assigned." in claim["note"]
    doc = load_record(ROOT / curation["record"]["path"])
    assert len(doc["activity_spectrum"]) == 3
    assert {r["strain"] for r in doc["activity_spectrum"]} == {"0781", "0782", "0783"}
    assert all("mic_value" in r for r in doc["activity_spectrum"])


def test_teicoplanin_and_primary_discrepancies_are_not_silently_resolved(context):
    pin = context["teicoplanin_at_start"]
    assert hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]
    assert context["teicoplanin_disposition"]["source_structure_label"] == "Teicoplanin A2-5"
    assert "caption misnames" in context["source_discrepancies"]["21807981"]
    assert "wording differs" in context["source_discrepancies"]["12499162"]
    assert set(context["deferred_native_reviews"]) == {"10817725", "11036060", "15980329"}


def test_census_only_updates_the_vancomycin_claim_count_and_hash():
    reconciliation = json.loads(Path(str(PREFIX) + "-checkpoint-reconciliation.json").read_bytes())
    ledgers = []
    for name in ("previous_ledger", "current_ledger"):
        pin = reconciliation[name]
        path = ROOT / pin["path"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == pin["sha256"]
        with path.open(newline="") as stream:
            ledgers.append(list(csv.DictReader(stream, delimiter="\t")))
    old, new = ledgers
    assert len(old) == len(new) == 2939
    (a, b), = [(a, b) for a, b in zip(old, new, strict=True) if a != b]
    assert b["identifier"] == "CHEBI:28001"
    assert {k for k in a if a[k] != b[k]} == {"record_sha256", "resistance_assertions"}
    assert int(b["resistance_assertions"]) == int(a["resistance_assertions"]) + 5
    assert reconciliation["current_counts"]["resistance_assertions"] == 4828
    assert reconciliation["curator_claims"] == 73 and reconciliation["curator_records"] == 37


def test_unchanged_embeddings_and_open_corpus_scope(context, curation):
    assert curation["embedding_documents_changed"] == 0
    assert curation["embedding_fingerprint"] == "18ff581531b8bd9d"
    assert context["scope"]["corpus_records"] == 2939 and context["scope"]["whole_records_completed"] == 0
    assert curation["whole_corpus_primary_review"] == "OPEN"
    for value in (context, curation):
        assert all(value[k] == 0 for k in ("experimental_proteins_assigned", "exact_alleles_assigned",
                                          "experimental_genomes_assigned", "numerical_ast_added",
                                          "ncbi_endpoint_requests", "source_adoptions", "github_mutations"))
