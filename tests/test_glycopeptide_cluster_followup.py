"""Whole clusters, ligase references, and native phenotypes must stay distinct."""

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
    return json.loads((ROOT / "research/2026-10-10-glycopeptide-clusters-context.json").read_bytes())


def test_complete_whole_cluster_cohort_and_input_pins(dossier):
    for pin in dossier["inputs"].values():
        assert hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]
    scope = json.loads((ROOT / dossier["inputs"]["term_scope"]["path"]).read_bytes())
    clusters = {k for k, v in scope["terms"].items() if v["entity_scope"] == "GENE_CLUSTER_NOT_ONE_PROTEIN"}
    assert len(clusters) == 14
    assert clusters - set(dossier["terms"]) == {"ARO:3007434"}
    assert dossier["excluded_non_glycopeptide_cluster"] == "ARO:3007434"
    assert dossier["scope"] == {
        "corpus_records": 2939, "selected_terms": 13, "selected_records": 2,
        "existing_assertion_memberships": 18, "reference_proteins": 17,
        "whole_records_completed": 0, "whole_corpus_primary_review": "OPEN",
    }


def test_source_memberships_are_not_new_phenotypes(dossier):
    pairs = {(aro, identifier) for aro, term in dossier["terms"].items()
             for identifier in term["record_memberships"]}
    assert len(pairs) == 18
    for row in dossier["records"]:
        record = load_record(ROOT / row["path"])
        assert record["identifier"] == row["identifier"]
        assert record["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"]
        assert row["complete_collection_aware_read"] and row["whole_record_review"] == "OPEN"
        existing = {c.get("aro_id") for c in record.get("resistance_mechanisms", [])}
        assert {aro for aro, identifier in pairs if identifier == row["identifier"]} <= existing
    assert all(not t["whole_cluster_uniprot_assignment"] and not t["experimental_protein_assignment"]
               for t in dossier["terms"].values())


def test_citation_queries_complete_but_not_biological_absence(dossier):
    assert len(dossier["bibliography"]) == len(dossier["literature_queries"]) == 26
    assert sum(q["reused"] for q in dossier["literature_queries"].values()) == 20
    for query in dossier["literature_queries"].values():
        assert query["complete_for_query"]
        assert not query["establishes_biological_absence"]
        assert not query["shared_citation_is_experimental_assignment"]
    assert dossier["literature_queries"]["16513756"]["result_count"] == 5014
    assert dossier["literature_queries"]["24342631"]["result_count"] == 10
    assert dossier["literature_queries"]["34505571"]["result_count"] == 0


def test_new_requests_are_sequence_free_and_do_not_contact_ncbi(dossier):
    assert len(dossier["requests"]) == 82
    searches = 0
    for row in dossier["requests"].values():
        url = urlsplit(row["url"])
        assert url.scheme == "https" and url.hostname in {"rest.uniprot.org", "www.ebi.ac.uk"}
        assert row["status"] == 200 and row["sha256"] == row["cache"]["sha256"]
        if url.path == "/uniprotkb/search":
            searches += 1
            params = parse_qs(url.query)
            assert params["size"] == ["500"]
            assert "sequence" not in params["fields"][0].split(",")
            assert row["release"] == "2026_03"
            assert row["complete_for_query"] and not row["establishes_biological_absence"]
    assert searches == 25


@pytest.mark.parametrize("key,count", [("ref-vanB-reviewed", 5), ("ref-vanI-name", 2), ("ref-vanP-name", 3)])
def test_literal_gene_homonyms_excluded(dossier, key, count):
    review = dossier["gene_name_query_review"][key]
    excluded = set(review["excluded_homonyms"])
    assert len(excluded) == count
    assert not excluded & set(dossier["reference_proteins"])
    assert {r["accession"] for r in review["entries"]} == excluded | set(
        review.get("retained_reference_accessions", []) + review.get("unverified_ligase_leads", []))


def test_vanp_empty_mapping_does_not_reclassify_borderline_phenotype(dossier):
    term = dossier["terms"]["ARO:3007187"]
    assert term["reference_candidates"] == []
    review = dossier["primary_reviews"]["34505571"]
    assert "borderline" in review["finding"]
    assert "403" in review["access_limit"] and "without bypass" in review["access_limit"]
    assert review["curation_handoff"] == "NO_BIOLOGICAL_WRITE_FROM_ABSTRACT_OR_NO_HIT"


def test_locus_crosswalk_distinguishes_two_ddl_annotations(dossier):
    proteins = dossier["reference_proteins"]
    for accession, locus in (("Q24R63", "DSY3690"), ("Q24X74", "DSY1579")):
        gene, = proteins[accession]["gene_annotations"]
        assert gene["geneName"]["value"] == "ddl"
        assert gene["orderedLocusNames"][0]["value"] == locus
        assert proteins[accession]["taxon_id"] == "NCBITaxon:138119"
    assert dossier["terms"]["ARO:3003722"]["reference_candidates"] == ["Q24R63"]
    assert proteins["Q24X74"]["role"] == "PRIMARY_BIOCHEMICAL_COMPARATOR_NOT_THE_RESISTANCE_LIGASE"
    assert not proteins["Q24R63"]["experimental_assignment"]


def test_native_vanm_and_later_zy2_archive_contexts_do_not_mix(dossier):
    links = {r["nucleotide_accession"]: r for r in dossier["reference_proteins"]["B8XGS3"]["archive_links"]}
    assert {r["strain"] for r in links["FJ349556"]["strain_reference_bindings"]} == {"Efm-HS0661"}
    assert {r["strain"] for r in links["CP039730"]["strain_reference_bindings"]} == {"ZY2"}
    assert dossier["archive_metadata"]["FJ349556"]["sample"] is None
    assert dossier["archive_metadata"]["CP039730"]["sample"] == "SAMN10867605"
    assert "discordant teicoplanin" in dossier["primary_reviews"]["20733041"]["qualitative_comparator"]


def test_vanb_other_strain_and_unbound_comments_are_not_native_assignments(dossier):
    row = dossier["reference_proteins"]["Q06893"]
    assert row["taxon_id"] == "NCBITaxon:226185" and row["sequence_version"] == 2
    assert {c["strain"] for c in row["unbound_strain_comments_not_propagated"]} == {
        "ATCC 700802 / V583", "SF300"}
    assert all(not r["strain_reference_bindings"] for r in row["archive_links"])
    assert "NOT_BM4281" in dossier["terms"]["ARO:3000238"]["reference_disposition"]


def test_vanf_historical_name_and_second_ligase_are_not_enterococcal_vane(dossier):
    proteins = dossier["reference_proteins"]
    assert proteins["O52073"]["gene_annotations"][0]["geneName"]["value"] == "vanE"
    assert proteins["O52073"]["taxon_id"] == "NCBITaxon:78057"
    assert proteins["O52073"]["sequence_version"] == 2
    assert dossier["terms"]["ARO:3000255"]["reference_candidates"] == ["O52073"]
    assert proteins["Q9ZFK2"]["role"] == "SECOND_LIGASE_FRAGMENT_NOT_ASSIGNED_TO_VANF"
    assert "O52073" not in dossier["terms"]["ARO:3000259"]["reference_candidates"]


def test_fragments_and_unreconciled_source_strain_strings_are_preserved(dossier):
    proteins = dossier["reference_proteins"]
    assert {a for a, p in proteins.items() if p["fragment"]} == {"Q47822", "Q9S4K1", "Q9ZFK2"}
    assert "N00-410" in dossier["bibliography"]["12019119"]["title"]
    assert {c["strain"] for r in proteins["Q93A46"]["archive_links"]
            for c in r["strain_reference_bindings"]} == {"N00-0410"}
    assert {c["strain"] for r in proteins["V5KW92"]["archive_links"]
            for c in r["strain_reference_bindings"]} == {"S7B"}
    assert dossier["primary_reviews"]["24342631"]["native_subject"] == "RE-S7B"
    assert not proteins["V5KW92"]["experimental_assignment"]


def test_archive_contig_set_is_not_the_requested_contig(dossier):
    archives = dossier["archive_metadata"]
    assert len(archives) == 27
    row = archives["JARQDZ010000002"]
    assert row["requested_accession"] == "JARQDZ010000002"
    assert row["returned_accession"] == "JARQDZ010000000"
    assert row["data_type"] == "CONTIGSET"
    assert row["scope"] == "CONTIG_SET_SUMMARY_NOT_INDIVIDUAL_CONTIG"
    assert all(not r["experimental_genome_assignment"] for r in archives.values())


def test_species_and_strain_taxonomy_are_not_interchangeable(dossier):
    taxa = dossier["taxonomy"]
    assert len(taxa) == 9 and all(t["active"] for t in taxa.values())
    assert taxa["138119"]["rank"] == taxa["226185"]["rank"] == "strain"
    assert taxa["138119"]["parent"]["taxonId"] == 49338
    assert taxa["49338"]["rank"] == taxa["1352"]["rank"] == "species"
    assert taxa["43767"]["scientificName"] == "Rhodococcus hoagii"
    assert any(n.startswith("Rhodococcus equi (") for n in taxa["43767"]["other_names"])


def test_teicoplanin_component_scope_blocks_generic_assay_join(dossier):
    hold = dossier["chemical_hold"]
    assert hold["standard_inchi_key"] == "FHBQKTSCJKPYIO-OXIGXJDJSA-N"
    assert hold["source_structure_label"] == "Teicoplanin A2-5"
    assert hold["action"] == "NO_GENERIC_TEICOPLANIN_ASSAY_TO_EXACT_COMPONENT_JOIN"


def test_all_records_stay_in_scope_without_new_biological_writes(dossier):
    with (ROOT / dossier["current_census"]["path"]).open(newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    assert len(rows) == 2939
    assert dossier["preservation"] == {
        "record_hashes_verified": 2939, "ignored_files_included": True,
        "biological_record_changes": 0, "curation_events_added": 0,
    }
    assert all(dossier[key] == 0 for key in ("experimental_proteins_assigned", "exact_alleles_assigned",
        "experimental_genomes_assigned", "ncbi_endpoint_requests", "outreach", "source_adoptions",
        "github_mutations"))
    assert "full authoritative QC not rerun" in dossier["validation_scope"]


def test_nonoperational_export(dossier):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not set(keys(dossier)) & {
        "sequence", "variants", "alteration", "constructs", "primers", "protocol",
        "coordinates", "mic", "measurement_value", "smiles", "inChI", "headers",
    }
    assert all(not r["whole_paper_review_complete"] for r in dossier["primary_reviews"].values())
