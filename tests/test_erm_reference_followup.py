"""Erm reference discovery must not invent allele or phenotype assignments."""

import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-09-erm-reference-followup.json").read_bytes())


def test_prior_artifact_pins_and_complete_unlinked_cohort(dossier):
    for name in ("prior_checkpoint", "current_census", "reference_audit", "term_scope", "source_inventory"):
        pin = dossier[name]
        assert hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]
    prior = json.loads((ROOT / dossier["reference_audit"]["path"]).read_bytes())
    terms = {key: row for key, row in prior["determinants"].items()
             if any(label.lower().startswith("erm") for label in row["labels"])}
    assert len(terms) == 47
    assert {key for key, row in terms.items() if not row["candidates"]} == set(dossier["candidates"])
    assert len(dossier["candidates"]) == 6


def test_all_corpus_records_remain_in_scope(dossier):
    assert dossier["scope"] == {
        "corpus_records": 2939, "erm_terms_in_prior_audit": 47, "unlinked_erm_terms": 6,
        "selected_records": 24, "existing_assertion_memberships": 80,
        "whole_records_completed": 0, "whole_corpus_primary_review": "OPEN",
    }
    with (ROOT / dossier["current_census"]["path"]).open(newline="") as stream:
        census = {r["identifier"]: r for r in csv.DictReader(stream, delimiter="\t")}
    assert len(census) == 2939
    assert len(dossier["records"]) == 24
    for row in dossier["records"]:
        assert row["sha256"] == census[row["identifier"]]["record_sha256"]
        assert row["whole_record_review"] == "OPEN"
        assert row["complete_record_read_through_collection_loader"]
        assert row["record_action"] == "PRESERVE_NO_NEW_BIOLOGICAL_CLAIM"


def test_memberships_are_not_phenotype_expansion(dossier):
    pairs = {(r["identifier"], r["aro_id"]) for r in dossier["memberships"]}
    assert len(pairs) == len(dossier["memberships"]) == 80
    for row in dossier["records"]:
        record = load_record(ROOT / row["path"])
        assert record["identifier"] == row["identifier"]
        assert record["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"]
        expected = {aro for identifier, aro in pairs if identifier == row["identifier"]}
        assert set(row["selected_aro_ids"]) == expected
    assert sum(c["existing_assertion_memberships"] for c in dossier["candidates"].values()) == 80
    assert all(not c["explicit_aro_uniprot_cross_reference"] and not c["experimental_assignment"]
               and not c["all_family_members_enumerated"] for c in dossier["candidates"].values())


def test_uniprot_queries_are_bounded_and_sequence_free(dossier):
    assert len(dossier["requests"]) == 31
    for key, request in dossier["requests"].items():
        url = urlsplit(request["url"])
        assert url.scheme == "https" and url.hostname in {"rest.uniprot.org", "www.ebi.ac.uk"}
        assert request["status"] == 200 and len(request["sha256"]) == 64
        assert request["sha256"] == request["cache"]["sha256"]
        if key in dossier["searches"]:
            query = parse_qs(url.query)
            assert query["size"] == ["500"]
            assert "sequence" not in query["fields"][0].split(",")
            assert request["complete_for_query"] and not request["establishes_biological_absence"]
            assert request["release"] == "2026_03"
            assert request["query"] == dossier["searches"][key]["query"]
    assert dossier["query_scope"]["queries"] == 9
    assert not dossier["query_scope"]["exhaustive_gene_family_search"]


def test_alias_candidate_does_not_collapse_distinct_references(dossier):
    erm_x = dossier["candidates"]["ARO:3000596"]
    assert set(erm_x["accessions"]) == {"Q7BBX6", "Q9AG96", "Q9AG93", "J7Q2T4", "Q46484"}
    assert dossier["searches"]["ermXaliases"]["accessions"] == ["Q46484"]
    assert dossier["proteins"]["Q46484"]["gene_annotations"][0]["geneName"]["value"] == "ermCX"
    assert len(dossier["proteins"]) == 8
    assert all(not row["experimental_assignment"] for row in dossier["proteins"].values())


def test_susceptible_partial_reference_is_not_a_resistance_assignment(dossier):
    row = dossier["proteins"]["J7Q2T4"]
    assert row["role"] == "PARTIAL_REFERENCE_FROM_SUSCEPTIBLE_TYPE_STRAIN_NOT_RESISTANCE_ASSIGNMENT"
    assert row["citation_contexts"][0]["strain_annotations"] == ["Type strain: ATCC 6940"]
    assert dossier["archive_references"]["HE586307"]["partial_gene_explicitly_reported"]
    paper = dossier["primary_papers"]["22475029"]
    assert paper["relevant_results_text_inspected"]
    assert "except cefotaxime" in paper["finding"]


def test_cj_reference_pairing_is_from_databases_not_caption_order(dossier):
    limit, = [x for x in dossier["identity_limits"] if x["kind"] == "DISTINCT_STRAIN_REFERENCES"]
    assert limit["database_pairs"] == {
        "Q9AG96": {"archive": "AF338705", "strain": "CJ21"},
        "Q9AG93": {"archive": "AF338706", "strain": "CJ12"},
    }
    assert limit["disposition"] == "KEEP_SEPARATE_NO_POSITIONAL_CAPTION_CROSSWALK"
    for accession, pair in limit["database_pairs"].items():
        row = dossier["proteins"][accession]
        assert row["citation_contexts"][0]["strain_annotations"] == [pair["strain"]]
        assert pair["archive"] in {r["id"] for r in row["archive_references"]}
    assert "without an explicit per-item mapping" in dossier["primary_papers"]["11408212"]["finding"]


def test_source_definition_conflict_is_not_an_alias(dossier):
    limit, = [x for x in dossier["identity_limits"] if x["kind"] == "SOURCE_LABEL_DEFINITION_CONFLICT"]
    assert limit["aro_id"] == "ARO:3000605"
    assert limit["source_label"] == "Erm(36)" and limit["definition_names"] == "ErmD"
    assert limit["disposition"] == "PRESERVE_SOURCE_AND_FLAG_CONFLICT_NOT_AN_ERMD_ALIAS"
    assert dossier["candidates"]["ARO:3000605"]["accessions"] == ["Q8VQ13"]
    assert dossier["proteins"]["Q8VQ13"]["entry_audit"] == {"entryVersion": 87, "sequenceVersion": 1}


def test_taxon_synonyms_and_historical_label_conflict_are_distinct(dossier):
    taxonomy = dossier["reference_taxonomy"]
    assert len(taxonomy) == 8
    assert all(row["rank"] == "species" and row["active"] for row in taxonomy.values())
    assert "Mycobacterium chelonae" in taxonomy["1774"]["synonyms"]
    assert "Propionibacterium acnes" in taxonomy["1747"]["synonyms"]
    conflict, = [x for x in dossier["identity_limits"] if x["kind"] == "HISTORICAL_ORGANISM_LABEL"]
    assert conflict["protein"] == "Q46484"
    assert not conflict["historical_reidentification_verified"]
    assert "WITHOUT_ASSUMING_SPECIES_SYNONYMY" in conflict["disposition"]


@pytest.mark.parametrize("key,aro,deposits", [
    ("erm55", "ARO:3009647", ["OQ656455", "OQ656456", "OQ656457"]),
    ("erm56", "ARO:3007654", ["OQ326498"]),
])
def test_no_hit_retains_verified_deposits_without_inventing_uniprot(dossier, key, aro, deposits):
    assert dossier["candidates"][aro]["accessions"] == []
    assert dossier["candidates"][aro]["published_deposits"] == deposits
    for query in (key, key + "archive"):
        assert dossier["searches"][query]["result_count"] == 0
        assert not dossier["searches"][query]["no_hit_is_absence"]
    for accession in deposits:
        ref = dossier["archive_references"][accession]
        assert ref["metadata"]["version"] == 1 and ref["metadata"]["statusDescription"] == "public"
        assert not ref["experimental_assignment"]


def test_shared_deposits_and_multiple_strains_do_not_make_exact_alleles(dossier):
    contexts = dossier["proteins"]["Q46194"]["citation_contexts"]
    assert contexts[0]["strain_annotations"] == ["JIR100"]
    assert contexts[1]["strain_annotations"] == ["SC4-C13"]
    assert dossier["proteins"]["Q54386"]["citation_contexts"][0]["strain_annotations"] == ["TK21"]
    assert len(dossier["archive_references"]) == 14
    assert dossier["archive_references"]["KC005723"]["metadata"]["sample"] == "SAMN14225896"
    assert all(not r["experimental_assignment"] for r in dossier["archive_references"].values())


def test_primary_inspection_limits_and_negative_comparator_are_retained(dossier):
    papers = dossier["primary_papers"]
    assert len(papers) == 7 and all(not p["whole_paper_review_complete"] for p in papers.values())
    assert all(not p["native_tables_inspected"] for p in papers.values())
    assert "stopped without retry or bypass" in papers["1761231"]["access_limit"]
    assert "without an HTTP status" in papers["12177341"]["access_limit"]
    assert "inconclusive" in papers["37417762"]["finding"]
    assert not papers["37417762"]["numerical_results_exported"]
    assert all(p["exact_compound_record_join"] == "PENDING_TESTED_CHEMICAL_FORM_AND_SUBJECT_REVIEW"
               for p in papers.values())


def test_non_operational_export_and_no_biological_writes(dossier):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    forbidden = {"sequence", "variants", "alteration", "constructs", "primers", "protocol",
                 "coordinates", "mic", "measurement_value", "headers", "smiles", "inChI"}
    assert not set(keys(dossier)) & forbidden
    assert dossier["preservation"] == {
        "record_hashes_verified": 2939, "ignored_files_included": True,
        "biological_record_changes": 0, "curation_events_added": 0,
    }
    assert all(dossier[key] == 0 for key in ("ncbi_endpoint_requests", "outreach", "github_mutations",
        "source_adoptions", "exact_experimental_protein_assignments", "experimental_genome_assignments"))
    assert "full authoritative QC not rerun" in dossier["validation_scope"]
