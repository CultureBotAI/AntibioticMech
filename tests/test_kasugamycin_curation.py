"""Retain genotype and compound boundaries in the kasugamycin table curation."""

import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import write_validated_antibiotic

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "research/2026-10-12-kasugamycin"


@pytest.fixture(scope="module")
def context():
    return json.loads(Path(str(PREFIX) + "-context.json").read_bytes())


@pytest.fixture(scope="module")
def curation():
    return json.loads(Path(str(PREFIX) + "-curation.json").read_bytes())


def test_current_record_retains_curated_and_source_evidence(curation, tmp_path):
    path = ROOT / curation["record"]["path"]
    record = load_record(path)
    assert record["identifier"] == "CHEBI:81419"
    assert record["chemical_structure"]["standard_inchi_key"] == "PVTHJAPFENJVNC-MHRBZPPQSA-N"
    assert len(curation["preserved_card_assertions"]) == 3
    for claim in curation["preserved_card_assertions"] + curation["claims"]:
        assert claim in record["resistance_mechanisms"]
    assert all(row in record["activity_spectrum"] for row in curation["observations"])
    # Additional future evidence need not alter this historical curation receipt.
    output = tmp_path / path.name
    write_validated_antibiotic(record, output)
    assert output.read_bytes() == path.read_bytes()


def test_source_genotypes_have_one_to_one_within_study_subjects(context, curation):
    subjects = context["curated_subjects"]
    assert len(subjects) == len(curation["claims"]) == 6
    assert {s["strain"] for s in subjects} == {
        "CAG67776", "CAG67774", "CAG67775", "CAG67781", "CAG67780", "CAG67788",
    }
    for subject, claim in zip(subjects, curation["claims"], strict=True):
        assert claim["strain"] == subject["strain"]
        assert subject["source_genotype"] == "MG1655 " + claim["alteration"]
        assert claim["alteration"] == " ".join(s + "::FRT" for s in subject["symbols"])
        assert "within the same study" in subject["join"]
        assert claim["taxon_id"] == "NCBITaxon:562"


def test_operons_and_combined_genotypes_are_not_single_gene_effects(context, curation):
    for subject, claim in zip(context["curated_subjects"], curation["claims"], strict=True):
        scope = subject["genotype_scope"]
        if "OPERON" in scope:
            assert "gene_families" not in claim
            assert "not single-gene or single-protein assignments" in claim["note"]
        else:
            assert claim["gene_families"] == subject["symbols"]
            assert "reference-only" in claim["note"]
        if scope.startswith("COMBINED"):
            assert "no component is assigned its full effect" in claim["note"]
    assert not context["measurement_policy"]["combined_effect_assigned_to_single_component"]


def test_all_seven_mic_rows_keep_units_endpoint_and_comparator(curation, context):
    rows = curation["observations"]
    assert len(rows) == 7
    assert [r["mic_value"] for r in rows] == [50, 100, 100, 100, 200, 200, 200]
    assert rows[0]["strain"] == context["comparator"]["strain"] == "CAG454"
    assert "not a resistance claim" in rows[0]["evidence"][0]["notes"]
    assert "CAG454" not in {c["strain"] for c in curation["claims"]}
    for row in rows:
        assert row["mic_units"] == "mg/L" and "activity" not in row
        assert row["taxon_id"] == "NCBITaxon:562"
        assert "minimal medium" in row["assay"] and "below 10%" in row["assay"]
        assert "ug/mL" in row["evidence"][0]["notes"]
        assert row["evidence"][0]["reference"] == "PMID:27355376"
    assert not context["measurement_policy"]["clinical_categories_inferred"]


def test_observation_locators_do_not_collide_across_compounds(curation):
    identifiers = [r["source_observation_id"] for r in curation["observations"]]
    assert len(set(identifiers)) == 7
    assert all(value.startswith("PMID:27355376:Table2:kasugamycin:") for value in identifiers)
    prior = json.loads((ROOT / "research/2026-10-12-blasticidin-curation.json").read_bytes())
    assert not set(identifiers) & {r["source_observation_id"] for r in prior["observations"]}


def test_reference_taxonomy_and_genome_are_not_derivative_assignments(curation, context):
    for row in curation["claims"] + curation["observations"]:
        assert not {"protein_accession", "gene_id", "strain_taxon_id", "assembly_accession",
                    "biosample_accession", "bioproject_accession", "sra_accessions", "source",
                    "aro_id"} & row.keys()
    assert context["taxonomy"]["562"]["rank"] == "species"
    assert context["taxonomy"]["511145"]["rank"] == "no rank"
    assert context["taxonomy"]["511145"]["parent"]["taxonId"] == 83333
    assert context["reference_genome"]["accession"] == "U00096.3"
    assert context["reference_genome"]["scope"] == "REFERENCE_GENOME_NOT_SEQUENCED_EXPERIMENTAL_DERIVATIVE"
    assert curation["exact_protein_alleles_assigned"] == curation["experimental_genomes_assigned"] == 0


def test_ten_versioned_reference_components_retain_dpp_alias(context):
    proteins = context["reference_proteins"]
    assert set(proteins) == {prefix + suffix for prefix in ("opp", "dpp") for suffix in "ABCDF"}
    expected = {"dppA": ("P23847", 195, "b3544"), "dppB": ("P0AEF8", 136, "b3543"),
                "dppC": ("P0AEG1", 133, "b3542"), "dppD": ("P0AAG0", 147, "b3541"),
                "dppF": ("P37313", 182, "b3540")}
    for gene, (accession, entry, locus) in expected.items():
        row = proteins[gene]
        assert (row["accession"], row["entry_version"], row["sequence_version"]) == (
            "UniProtKB:" + accession, entry, 1,
        )
        assert locus in row["loci"]
    assert proteins["dppF"]["synonyms"] == ["dppE"]
    for protein in proteins.values():
        assert protein["reference_taxon_id"] == "NCBITaxon:83333"
        assert protein["scope"] == "REFERENCE_ONLY_NOT_EXPERIMENTAL_ALLELE"
        assert protein["entry_type"] == "UniProtKB reviewed (Swiss-Prot)"


def test_permitted_identifier_queries_are_complete_only_at_requested_scope(context):
    assert len(context["uniprot_requests"]) == 6
    counts = []
    for request in context["uniprot_requests"]:
        parsed = urlsplit(request["url"])
        assert parsed.hostname == "rest.uniprot.org" and request["status"] == 200
        assert request["release"] == context["reference_release"] == "2026_03"
        assert len(request["sha256"]) == len(request["cache"]["sha256"]) == 64
        if parsed.path == "/uniprotkb/search":
            assert "sequence" not in parse_qs(parsed.query)["fields"][0].split(",")
            assert request["complete_for_requested_reference_query"]
            counts.append(request["result_count"])
    assert sorted(counts) == [1, 1, 4, 4]


def test_primary_scope_retains_correction_and_indirect_binding_limit(context, curation):
    primary = context["primary"]
    assert primary["correction_inspected"]
    assert "Table 2 and Table S2 were not replaced" in primary["correction_scope"]
    assert "Original Figure 5" in primary["native_visual_review"]
    assert "Word XML strain rows" in primary["structured_supplement_review"]
    assert "do not exclude an indirect effect" in primary["interpretation_boundary"]
    for claim in curation["claims"]:
        assert claim["mechanism_type"] == "REDUCED_PERMEABILITY"
        assert "not direct drug flux" in claim["note"]
        assert {e["reference"] for e in claim["evidence"]} == {
            "PMID:27355376", "DOI:10.1371/journal.pgen.1006902",
        }
    assert "no exact MIC is inferred" in " ".join(context["limitations"])


def test_chemical_identity_does_not_claim_physical_reidentification(context):
    chemical = context["chemical_identity"]
    assert chemical["molecular_formula"] == "C14H25N3O9"
    assert chemical["standard_inchi_key"] == "PVTHJAPFENJVNC-MHRBZPPQSA-N"
    assert chemical["smiles_inchi_key_agree"]
    assert not chemical["tested_preparation_independently_reidentified"]


def test_historical_census_and_reused_primary_pins(context, curation):
    for pin in (curation["context"], context["reused_primary_context"], context["baseline_census"]):
        assert hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]
    reconciliation = json.loads(Path(str(PREFIX) + "-reconciliation.json").read_bytes())
    for key, expected_pin in (("previous_census", context["record_before"]),
                              ("current_census", curation["record"])):
        pin = reconciliation[key]
        payload = (ROOT / pin["path"]).read_bytes()
        assert hashlib.sha256(payload).hexdigest() == pin["sha256"]
        row, = [r for r in csv.DictReader(payload.decode().splitlines(), delimiter="\t")
                if r["identifier"] == "CHEBI:81419"]
        assert row["record_sha256"] == expected_pin["sha256"]
    assert reconciliation["records"] == 2939 and reconciliation["records_byte_identical"] == 2938
    assert reconciliation["resistance_assertions"] == 4847
    assert reconciliation["activity_observations"] == 4504
    assert curation["claims_added"] == 6 and curation["measurements_added"] == 7


def test_table_completion_is_not_whole_record_review(context):
    coverage = context["table_coverage"]
    assert coverage["kasugamycin_rows"] == coverage["curated_mic_rows"] == 7
    assert coverage["derivative_claims"] == 6 and coverage["other_drug_rows_imported"] == 0
    assert not coverage["whole_record_complete"] and not context["whole_record_review_complete"]
    assert context["whole_corpus_primary_review"] == "OPEN"
    assert "CARD assertions are preserved" in " ".join(context["limitations"])
    assert len(context["source_assets"]) == 7
    for asset in context["source_assets"]:
        assert urlsplit(asset["url"]).hostname in {"www.ebi.ac.uk", "journals.plos.org"}
