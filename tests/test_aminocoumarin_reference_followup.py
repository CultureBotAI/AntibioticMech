"""Reference succession must not erase organism conflicts or experimental scope."""

import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit

import pytest

from antibioticmech.activity_collections import load_record

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def dossier():
    path = ROOT / "research/2026-10-09-aminocoumarin-reference-followup.json"
    return json.loads(path.read_bytes())


def test_corpus_scope_and_historical_artifact_pins(dossier):
    for name in ("prior_checkpoint", "prior_discovery", "current_census", "citation_union"):
        expected = dossier[name]
        assert hashlib.sha256((ROOT / expected["path"]).read_bytes()).hexdigest() == expected["sha256"]
    assert dossier["scope"] == {
        "corpus_records": 2939, "selected_records": 3, "focal_existing_assertion_memberships": 4,
        "whole_records_completed": 0, "whole_corpus_primary_review": "OPEN",
    }


@pytest.mark.parametrize("label", ["novobiocin", "coumermycin A1", "clorobiocin"])
def test_selected_record_keeps_identity_and_open_scope(dossier, label):
    row, = [r for r in dossier["records"] if r["label"] == label]
    record = load_record(ROOT / row["path"])
    assert record["identifier"] == row["identifier"]
    assert record["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"]
    assert row["complete_record_read_through_collection_loader"]
    assert row["whole_record_review"] == "OPEN"
    assert row["record_action"] == "PRESERVE_NO_NEW_BIOLOGICAL_CLAIM"
    assert row["decision"] == "HOLD_EXACT_TESTED_MATERIAL_AND_EXPERIMENTAL_IDENTIFIER_ASSIGNMENT"


def test_explicit_archive_succession_is_not_experimental_allele_equivalence(dossier):
    old = dossier["archive_references"]["AF205853"]["metadata"]
    new = dossier["archive_references"]["AF235050"]["metadata"]
    assert old["version"] == 1 and old["statusDescription"] == "suppressed"
    assert old["newAccession"] == "AF235050"
    assert new["version"] == 4 and new["secondaryAccession"] == ["AF205853"]
    assert old["taxon"] == new["taxon"] == 68264
    bridge = dossier["archive_bridge"]
    assert bridge["current_protein_sequence_versions"] == {"Q83WB9": 2, "Q83WB8": 2}
    assert not bridge["experimental_allele_equivalence_established"]
    for accession in ("Q83WB9", "Q83WB8"):
        row = dossier["proteins"][accession]
        assert row["entry_audit"]["sequenceVersion"] == 2
        assert "AF235050" in {x["id"] for x in row["archive_references"]}
        assert not row["experimental_assignment"]


def test_disputed_historical_organism_is_not_silently_corrected(dossier):
    conflict, = [r for r in dossier["identity_conflicts"] if r["kind"] == "HISTORICAL_DEPOSIT_ORGANISM"]
    assert conflict["protein"] == "UniProtKB:P50074" and conflict["archive"] == "Z17304.1"
    assert conflict["uniprot_taxon"] == "NCBITaxon:193462"
    assert conflict["ena_taxon"] == "NCBITaxon:2893586"
    assert conflict["later_paper_proposed_organism"] == "Streptomyces rishiriensis"
    assert dossier["proteins"]["P50074"]["organism"]["taxonId"] == 193462
    assert dossier["archive_references"]["Z17304"]["metadata"]["taxon"] == 2893586
    assert "ATTRIBUTED_PRIMARY_HYPOTHESIS" in conflict["disposition"]


def test_current_novobiocin_references_keep_distinct_strain_labels(dossier):
    reference = dossier["proteins"]["Q83WB7"]
    assert reference["organism"]["scientificName"] == "Actinoalloteichus cyanogriseus"
    assert reference["organism"]["taxonId"] == 2893586
    conflict, = [r for r in dossier["identity_conflicts"] if r["kind"] == "NOVA_REFERENCE_STRAIN"]
    assert conflict["paper_strain"] == "NCIMB 11891" and conflict["reference_strain"] == "NCIMB 9219"
    assert not conflict["strain_equivalence_established"]
    assert dossier["proteins"]["Q9L9G7"]["entry_audit"]["sequenceVersion"] == 2
    contexts = dossier["proteins"]["Q9L9G7"]["citation_contexts"]
    assert all(c["strain_annotations"] == ["NCIMB 9219"] for c in contexts)
    assert "NCIMB 9219" in dossier["archive_references"]["AF170880"]["metadata"]["description"]


def test_taxonomic_rank_is_not_a_species_identity_conflict(dossier):
    taxonomy = dossier["reference_taxonomy"]
    assert taxonomy["149682"]["rank"] == "subspecies"
    assert taxonomy["1352936"]["rank"] == "strain"
    assert taxonomy["1352936"]["parent"]["taxonId"] == 149682
    assert dossier["rank_resolution"]["parent_relationship_verified"]
    assert not dossier["rank_resolution"]["experimental_allele_assignment"]
    assert not dossier["rank_resolution"]["existing_producer_assertion_changed"]


def test_sensitive_comparator_and_other_hits_are_not_resistance_assignments(dossier):
    assert len(dossier["proteins"]) == 9
    comparator = dossier["proteins"]["P50075"]
    assert comparator["role"] == "SENSITIVE_REFERENCE_COMPARATOR_NOT_RESISTANCE_DETERMINANT"
    assert comparator["gene_annotations"][0]["geneName"]["value"] == "gyrBS"
    assert dossier["query_scope"] == {
        "returned_entries": 40, "focal_reference_entries": 9, "other_entries_retained_privately": 31,
        "all_returned_entries_are_resistance_determinants": False, "no_hit_is_absence": False,
    }
    assert all(not r["experimental_assignment"] for r in dossier["proteins"].values())


def test_host_results_transport_hypothesis_and_later_biochemistry_stay_separate(dossier):
    paper = dossier["primary_papers"]["12604514"]
    assert paper["relevant_results_text_inspected"]
    assert not paper["clorobiocin_focal_susceptibility_result_verified"]
    assert not paper["direct_efflux_measurement_verified"]
    assert not paper["native_producer_phenotype_inferred_from_host"]
    assert not paper["induced_point_mutant_established"]
    assert paper["selection_marker_is_not_focal_outcome"]
    assert paper["tested_material_exact_record_join"] == "PENDING_CHEMICAL_FORM_REVIEW"
    assert not dossier["primary_papers"]["14993313"]["relevant_results_text_inspected"]
    assert not dossier["primary_papers"]["8392138"]["relevant_results_text_inspected"]
    assert all(not p["whole_paper_review_complete"] for p in dossier["primary_papers"].values())


def test_literature_crosswalk_does_not_rewrite_aro_assertions(dossier):
    candidates = dossier["literature_derived_reference_candidates"]
    assert candidates["ARO:3003318"]["candidate"] == "UniProtKB:Q83WB8"
    assert "NOT_EXPLICIT_ARO_XREF_OR_EXACT_MUTANT" in candidates["ARO:3003318"]["scope"]
    assert candidates["ARO:3002522"]["candidate"] == "UniProtKB:Q9L9G7"
    assert "STRAIN_CONFLICT" in candidates["ARO:3002522"]["scope"]
    assert sum(len(r["focal_aro_assertions"]) for r in dossier["records"]) == 4


def test_access_denial_does_not_become_negative_evidence_or_retry(dossier):
    requests = dossier["requests"]
    assert len(requests) == 15
    denied, = [r for r in requests.values() if r["status"] != 200]
    assert denied["status"] == 403 and "microbiologyresearch.org" in denied["url"]
    assert "stopped without retry or bypass" in dossier["primary_papers"]["14993313"]["access_limit"]
    for request in requests.values():
        assert urlsplit(request["url"]).hostname in {
            "www.ebi.ac.uk", "rest.uniprot.org", "www.microbiologyresearch.org",
        }
    assert all(r["complete_for_query"] and not r["establishes_biological_absence"]
               for k, r in requests.items() if k.startswith("uniprot-"))


def test_research_only_preservation_and_non_operational_export(dossier):
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
    assert all(dossier[k] == 0 for k in ("ncbi_endpoint_requests", "github_mutations", "outreach",
                                        "source_adoptions", "exact_experimental_protein_assignments",
                                        "experimental_genome_assignments"))
    assert "full authoritative QC not rerun" in dossier["validation_scope"]
