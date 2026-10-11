"""Keep qualitative host findings distinct from donor, reference and allele identity."""

import csv
import hashlib
import json
from pathlib import Path

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import write_validated_antibiotic

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "research/2026-10-09-aminocoumarin-primary"


def semantic_sha(value):
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode()).hexdigest()


@pytest.fixture(scope="module")
def curation():
    return json.loads(Path(str(PREFIX) + "-curation.json").read_bytes())


@pytest.fixture(scope="module")
def context():
    return json.loads(Path(str(PREFIX) + "-context.json").read_bytes())


@pytest.mark.parametrize("identifier", ["CHEBI:28368", "CHEBI:3907"])
def test_one_claim_per_record_preserves_existing_slices(curation, identifier, tmp_path):
    row, = [r for r in curation["records"] if r["identifier"] == identifier]
    path = ROOT / row["record"]["path"]
    record = load_record(path)
    assert record["identifier"] == identifier
    assert record["chemical_structure"]["standard_inchi_key"] == row["standard_inchi_key"]
    assert record["curation_status"] == row["curation_status"]
    claims = record["resistance_mechanisms"]
    assert len(claims) == row["existing_claims_preserved"] + 1
    assert claims[-1] == row["added_claim"]
    assert semantic_sha(claims[:-1]) == row["preserved_resistance_claims_sha256"]
    assert semantic_sha(record["curation_history"][:-1]) == row["preserved_history_sha256"]
    assert record["curation_history"][-1] == row["curation_event"]
    other = {k: v for k, v in record.items() if k not in {"resistance_mechanisms", "curation_history"}}
    assert semantic_sha(other) == row["preserved_fields_sha256"]
    output = tmp_path / path.name
    write_validated_antibiotic(record, output)
    assert output.read_bytes() == path.read_bytes()


def test_host_donor_and_reference_are_not_collapsed(curation, context):
    for row in curation["records"]:
        claim = row["added_claim"]
        assert claim["mechanism_type"] == "UNKNOWN" and claim["gene_families"] == ["parYR"]
        assert claim["taxon_id"] == "NCBITaxon:1916"
        assert claim["taxon_label"] == "Streptomyces lividans"
        assert not {"strain", "strain_taxon_id", "alteration", "protein_accession",
                    "gene_id", "source", "aro_id"} & claim.keys()
        for phrase in ("laboratory derivatives", "not native-donor susceptibility",
                       "not the experimental derivative",
                       "Streptomyces rishiriensis DSM 40489", "UniProtKB:Q83WB8 is reference-only",
                       "does not establish the exact experimental allele",
                       "ParY enzymatic function unresolved"):
            assert phrase in claim["note"]
        assert claim["evidence"][0]["reference"] == "PMID:12604514"
    assert context["taxonomy"]["1916"]["rank"] == "species"
    assert context["taxonomy"]["457428"]["rank"] == "strain"
    assert context["taxonomy"]["457428"]["scope"] == "BACKGROUND_ONLY_NOT_EXPERIMENTAL_DERIVATIVE"
    reference = context["reference_protein"]
    assert reference["organism"]["taxonId"] == 68264
    assert reference["entry_audit"] == {"entryVersion": 120, "sequenceVersion": 2}
    assert not reference["experimental_assignment"]
    assert not context["archive_bridge"]["experimental_allele_equivalence_established"]


def test_chemical_join_uses_valid_inchi_without_repairing_smiles(context):
    chemical = context["chemical_identity"]
    records = {r["identifier"]: r for r in chemical["record_diagnostics"]["records"]}
    assert not records["CHEBI:3907"]["smiles_parses_strictly"]
    assert records["CHEBI:3907"]["inchi_parses_strictly"]
    for row in records.values():
        assert row["inchi_recomputed_key"] == row["standard_inchi_key"]
        assert row["unassigned_centers"] == 0
    amide = chemical["coumermycin_amide_diagnostic"]
    assert amide["amide_representation_key_matches_stored_key"]
    assert amide["transformation_scope"] == "TWO_IMIDIC_ACID_TO_AMIDE_LINKAGES_ONLY"
    assert amide["tetrahedral_centers"] == 8 and amide["unassigned_centers"] == 0
    assert not amide["unrestricted_enumerator_accepted"]
    assert not chemical["source_structure_repaired"]
    assert not chemical["physical_tested_material_reidentified"]


def test_primary_review_and_access_limits_remain_visible(context):
    primary = context["primary_paper"]
    assert primary["native_figures_visually_inspected"] == ["1A"]
    assert primary["relevant_results_text_inspected"] and primary["results_inspected_before_article_denial"]
    assert not primary["native_table2_visually_inspected"] and not primary["whole_paper_review_complete"]
    assert not primary["raw_fulltext_cache_available"]
    assert context["requests"]["figure1"]["status"] == 200
    assert context["requests"]["article"]["status"] == 403
    assert "stopped without retry or alternate access route" in primary["access_limit"]
    assert not context["figure_redistributed"]


def test_clorobiocin_remains_unchanged_without_focal_phenotype(context):
    primary = context["primary_paper"]
    assert not primary["clorobiocin_focal_susceptibility_result_verified"]
    records = context["chemical_identity"]["record_diagnostics"]["records"]
    row, = [r for r in records if r["label"] == "clorobiocin"]
    assert hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest() == row["sha256"]


def test_current_census_changes_only_two_rows(curation):
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
    assert {b["identifier"] for _, b in changed} == {"CHEBI:28368", "CHEBI:3907"}
    for a, b in changed:
        assert {k for k in a if a[k] != b[k]} == {"record_sha256", "resistance_assertions"}
        assert int(b["resistance_assertions"]) == int(a["resistance_assertions"]) + 1
    assert reconciliation["current_counts"]["resistance_assertions"] == 4804
    assert reconciliation["curator_claims"] == 49 and reconciliation["curator_records"] == 32
    assert curation["claims_added"] == curation["records_changed"] == curation["history_events_added"] == 2


def test_no_operational_export_or_claimed_corpus_completion(context, curation):
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
    assert context["scope"]["whole_records_completed"] == 0
    assert context["scope"]["whole_corpus_primary_review"] == "OPEN"
    assert curation["whole_corpus_primary_review"] == "OPEN"
    for value in (context, curation):
        assert value["numerical_ast_added"] == value["ncbi_endpoint_requests"] == 0
        assert value["github_mutations"] == 0
        assert value["source_adoptions"] == 0
