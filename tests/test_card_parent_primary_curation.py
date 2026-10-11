"""Native isolates, cohort subgroups and reference deposits are not interchangeable."""

import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import write_validated_antibiotic

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "research/2026-10-10-card-parent-primary"
STRAINS = {"5334", "5790", "5840", "6468"}


def semantic_sha(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    ).hexdigest()


@pytest.fixture(scope="module")
def context():
    return json.loads(Path(str(PREFIX) + "-context.json").read_bytes())


@pytest.fixture(scope="module")
def curation():
    return json.loads(Path(str(PREFIX) + "-curation.json").read_bytes())


@pytest.mark.parametrize(
    "identifier,previous,status", [("CHEBI:17698", 88, "REVIEWED"), ("CHEBI:87185", 11, "SEEDED")]
)
def test_current_claims_preserve_all_previous_fields(curation, tmp_path, identifier, previous, status):
    row = curation["records"][identifier]
    path = ROOT / row["record"]["path"]
    doc = load_record(path)
    assert row["existing_claims_preserved"] == previous
    assert len(doc["resistance_mechanisms"]) >= previous + 5
    assert semantic_sha(doc["resistance_mechanisms"][:previous]) == row["preserved_resistance_claims_sha256"]
    assert doc["resistance_mechanisms"][previous : previous + 5] == row["added_claims"]
    h = row["prior_history_events"]
    assert semantic_sha(doc["curation_history"][:h]) == row["preserved_history_sha256"]
    assert doc["curation_history"][h] == row["curation_event"]
    assert (
        semantic_sha({k: v for k, v in doc.items() if k not in {"resistance_mechanisms", "curation_history"}})
        == row["preserved_fields_sha256"]
    )
    assert doc["curation_status"] == status == row["curation_status"]
    target = tmp_path / path.name
    write_validated_antibiotic(doc, target)
    assert target.read_bytes() == path.read_bytes() and load_record(target) == doc


@pytest.mark.parametrize("identifier", ["CHEBI:17698", "CHEBI:87185"])
def test_named_avian_subjects_do_not_become_a_single_allele(curation, identifier):
    claims = curation["records"][identifier]["added_claims"]
    native = [c for c in claims if "strain" in c]
    assert {c["strain"] for c in native} == STRAINS and len(native) == 4
    for claim in native:
        assert claim["mechanism_type"] == "UNKNOWN"
        assert claim["taxon_id"] == "NCBITaxon:562" and claim["taxon_label"] == "Escherichia coli"
        assert claim["assay"] == "Source-reported disk diffusion"
        assert claim["gene_families"] == (["flo", "cmlA"] if claim["strain"] == "6468" else ["flo"])
        assert {e["reference"] for e in claim["evidence"]} == {"PMID:10639375"}
        assert "not isolated-gene causation" in claim["note"]
        assert "not assigned to these avian isolates" in claim["note"]


@pytest.mark.parametrize("identifier", ["CHEBI:17698", "CHEBI:87185"])
def test_bovine_subgroup_is_not_every_isolate_or_ec56(curation, identifier):
    (claim,) = [c for c in curation["records"][identifier]["added_claims"] if "strain" not in c]
    assert claim["gene_families"] == ["flo", "cmlA"] and claim["mechanism_type"] == "UNKNOWN"
    assert claim["assay"] == "NCCLS broth microdilution"
    assert {e["reference"] for e in claim["evidence"]} == {"PMID:11101601"}
    assert "not sole-gene causation or an assertion about every study isolate" in claim["note"]
    assert "EC56 belongs to a later submission" in claim["note"]
    assert "no E. coli clinical breakpoint is inferred" in claim["note"]
    assert "Discordant source subgroups are not merged" in claim["note"]


def test_no_exact_experimental_protein_or_new_numerical_ast(curation):
    forbidden = {
        "protein_accession",
        "alteration",
        "gene_id",
        "strain_taxon_id",
        "aro_id",
        "source",
        "measurement_value",
        "mic_value",
        "mic_units",
        "assembly_accession",
        "biosample_accession",
    }
    for row in curation["records"].values():
        for claim in row["added_claims"]:
            assert not forbidden & claim.keys()
            assert (
                "No exact experimental protein, allele, strain TaxID or genome is assigned." in claim["note"]
            )
    assert (
        curation["claims_added"] == 10
        and curation["records_changed"] == curation["history_events_added"] == 2
    )
    assert all(
        curation[k] == 0
        for k in (
            "experimental_proteins_assigned",
            "exact_alleles_assigned",
            "experimental_genomes_assigned",
            "numerical_ast_added",
            "ncbi_endpoint_requests",
            "source_adoptions",
            "github_mutations",
        )
    )


def test_reference_proteins_remain_source_bound(context):
    assert set(context["reference_proteins"]) == {"Q9XB24", "Q9F0D9"}
    for row in context["reference_proteins"].values():
        assert not row["experimental_assignment"] and not row["exact_allele_assignment"]
        assert row["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
        assert row["sequence_version"] == 1
        assert "sequence" not in row


def test_acc1_kus_reference_is_not_slk54_or_slk55(context):
    protein = context["reference_proteins"]["Q9XB24"]
    links = {r["nucleotide_accession"]: r for r in protein["archive_links"]}
    assert links["AJ133121"]["archive_protein_id"] == "CAB46491.1"
    assert {(r["strain"], r["citation_id"]) for r in links["AJ133121"]["strain_reference_bindings"]} == {
        ("KUS", "10428914")
    }
    assert {r["strain"] for r in links["AJ270942"]["strain_reference_bindings"]} == {"KP SLK54"}
    assert {r["strain"] for r in links["AJ870922"]["strain_reference_bindings"]} == {"SLK55"}
    assert links["AJ133121"]["archive_summary_verified"]
    assert not links["AJ270942"]["archive_summary_verified"]


def test_bovine_flo_deposit_is_not_later_ec56_submission(context):
    links = {r["nucleotide_accession"]: r for r in context["reference_proteins"]["Q9F0D9"]["archive_links"]}
    assert set(links) == {"AF252855", "AY775258"}
    assert links["AF252855"]["archive_protein_id"] == "AAG21808.1"
    assert links["AF252855"]["strain_reference_bindings"] == []
    (later,) = links["AY775258"]["strain_reference_bindings"]
    assert later["strain"] == "EC56" and later["citation_type"] == "submission"
    assert later["evidence_protein_ids"] == ["AAW02923.1"]
    assert not links["AY775258"]["archive_summary_verified"]


@pytest.mark.parametrize(
    "accession,pmid,taxid", [("AJ133121", "10428914", "573"), ("AF252855", "11101601", "562")]
)
def test_archive_metadata_is_not_an_experimental_genome(context, accession, pmid, taxid):
    row = context["archive_metadata"][accession]
    assert row["version"] == 1 and row["taxon_id"] == "NCBITaxon:" + taxid
    assert row["citations"] == ["PMID:" + pmid] and row["status"] == "public"
    assert row["data_type"] == "SEQUENCE" and row["data_class"] == "STD"
    assert row["sample"] is None and row["project"] is None
    assert not row["experimental_genome_assignment"]


@pytest.mark.parametrize("taxid,name", [("562", "Escherichia coli"), ("573", "Klebsiella pneumoniae")])
def test_species_rank_is_explicit(context, taxid, name):
    row = context["taxonomy"][taxid]
    assert row == {"taxonId": int(taxid), "scientificName": name, "rank": "species", "active": True}


def test_secondary_review_is_not_another_primary_experiment(context):
    review = context["primary_reviews"]["15914491"]
    assert review["scope"] == "SECONDARY_REVIEW"
    assert review["action"] == "DO_NOT_PROMOTE_REVIEW_TO_PRIMARY_EVIDENCE"
    assert "Review" in context["bibliography"]["15914491"]["pubTypeList"]["pubType"]
    assert all(not r["whole_paper_review_complete"] for r in context["primary_reviews"].values())


def test_acc1_records_are_unchanged_and_native_host_not_promoted(context):
    review = context["primary_reviews"]["10428914"]
    assert review["action"] == "REFERENCE_CROSSWALK_AND_SCOPE_HOLD_NO_BIOLOGICAL_WRITE"
    assert (
        review["source_isolate"] == "KUS"
        and review["scope"] == "NATIVE_ISOLATE_AND_LABORATORY_HOSTS_KEPT_SEPARATE"
    )
    held = [r for r in context["records_at_start"] if r["identifier"] not in {"CHEBI:17698", "CHEBI:87185"}]
    assert len(held) == 9
    assert all(hashlib.sha256((ROOT / r["path"]).read_bytes()).hexdigest() == r["sha256"] for r in held)


def test_cefotetan_identity_discrepancy_is_a_hold_not_a_silent_repair(context):
    identities = context["chemical_identities"]
    assert {key for key, value in identities.items() if not value["record_structure_verified"]} == {
        "CHEBI:3499"
    }
    row = identities["CHEBI:3499"]
    assert row["standard_inchi_key"] == row["key_from_inchi"] == "SRZNHPXWXCNNDU-IXOPCIAXSA-N"
    assert row["key_from_smiles"] == "SRZNHPXWXCNNDU-RHBCBLIFSA-N"
    assert row["action"] == "HOLD_CHEMICAL_IDENTITY_DISCREPANCY"
    for key in ("CHEBI:17698", "CHEBI:87185"):
        assert identities[key]["record_structure_verified"]
        assert not identities[key]["tested_preparation_independently_reidentified"]


def test_metadata_requests_are_bounded_and_ncbi_free(context):
    assert len(context["requests"]) == 8 and context["reference_release"] == "2026_03"
    for key, row in context["requests"].items():
        url = urlsplit(row["url"])
        assert url.hostname in {"rest.uniprot.org", "www.ebi.ac.uk"} and url.scheme == "https"
        assert row["status"] == 200 and row["cache"]["sha256"] == row["sha256"]
        if key.startswith("protein-"):
            assert "sequence" not in parse_qs(url.query)["fields"][0].split(",")
        if key.startswith("ena-"):
            assert url.path.startswith("/ena/browser/api/summary/")


def test_census_changes_only_the_two_curated_compounds():
    data = json.loads(Path(str(PREFIX) + "-checkpoint-reconciliation.json").read_bytes())
    ledgers = []
    for key in ("previous_ledger", "current_ledger"):
        row = data[key]
        path = ROOT / row["path"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == row["sha256"]
        with path.open(newline="") as stream:
            ledgers.append(list(csv.DictReader(stream, delimiter="\t")))
    old, new = ledgers
    assert len(old) == len(new) == 2939
    changed = [(a, b) for a, b in zip(old, new, strict=True) if a != b]
    assert {b["identifier"] for _, b in changed} == {"CHEBI:17698", "CHEBI:87185"}
    for a, b in changed:
        assert {k for k in a if a[k] != b[k]} == {"record_sha256", "resistance_assertions"}
        assert int(b["resistance_assertions"]) == int(a["resistance_assertions"]) + 5
    assert data["current_counts"]["resistance_assertions"] == 4838
    assert data["curator_claims"] == 83 and data["curator_records"] == 38


def test_scope_and_embedding_claims_remain_bounded(context, curation):
    assert context["scope"]["records_investigated"] == 11
    assert context["scope"]["whole_record_reviews_completed"] == 0
    assert (
        context["scope"]["whole_corpus_primary_review"] == curation["whole_corpus_primary_review"] == "OPEN"
    )
    assert not curation["whole_record_review_complete"]
    assert curation["embedding_fingerprint"] == "18ff581531b8bd9d"
