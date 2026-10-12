"""Keep measured laboratory phenotypes distinct from reference identities."""

import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

from antibioticmech.activity_collections import load_record
from antibioticmech.validation.write_validated import write_validated_antibiotic

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / "research/2026-10-12-blasticidin"
SUBJECTS = {"oppA": ("CAG67774", "UniProtKB:P23843"),
            "oppB": ("CAG67775", "UniProtKB:P0AFH2")}


@pytest.fixture(scope="module")
def context():
    return json.loads(Path(str(PREFIX) + "-context.json").read_bytes())


@pytest.fixture(scope="module")
def curation():
    return json.loads(Path(str(PREFIX) + "-curation.json").read_bytes())


def test_curated_evidence_remains_in_exact_record(curation, tmp_path):
    path = ROOT / curation["record"]["path"]
    record = load_record(path)
    assert record["identifier"] == "CHEBI:15353"
    assert record["chemical_structure"]["standard_inchi_key"] == "CXNPLSGKWMLZPZ-ZNIXKSQXSA-N"
    # Future curation can add evidence without invalidating this historical receipt.
    assert all(claim in record["resistance_mechanisms"] for claim in curation["claims"])
    assert all(observation in record["activity_spectrum"] for observation in curation["observations"])
    output = tmp_path / path.name
    write_validated_antibiotic(record, output)
    assert output.read_bytes() == path.read_bytes()


def test_single_gene_subjects_have_source_supported_crosswalk(context, curation):
    assert len(context["curated_subjects"]) == len(curation["claims"]) == 2
    for subject, claim in zip(context["curated_subjects"], curation["claims"], strict=True):
        gene = subject["gene"]
        strain, accession = SUBJECTS[gene]
        assert subject["source_genotype"] == f"MG1655 {gene}::FRT"
        assert subject["strain"] == claim["strain"] == strain
        assert "no cross-study join" in subject["join"]
        assert claim["gene_families"] == [gene]
        assert claim["alteration"] == f"{gene}::FRT"
        assert claim["taxon_id"] == "NCBITaxon:562"
        assert accession in claim["note"] and "reference-only" in claim["note"]


def test_reduced_uptake_is_not_direct_transport_in_each_derivative(curation, context):
    for claim in curation["claims"]:
        assert claim["mechanism_type"] == "REDUCED_PERMEABILITY"
        assert "operon-level interpretation, not direct transport" in claim["note"]
        assert {e["reference"] for e in claim["evidence"]} == {
            "PMID:27355376", "DOI:10.1371/journal.pgen.1006902",
        }
    assert "uptake proxy, not a direct drug-flux assay" in context["primary"][
        "interpretation_boundary"]


def test_mic_units_range_and_categories_remain_faithful(curation, context):
    assert len(curation["observations"]) == 2
    for claim, observation in zip(curation["claims"], curation["observations"], strict=True):
        gene, = claim["gene_families"]
        assert observation["strain"] == claim["strain"]
        assert observation["taxon_id"] == claim["taxon_id"]
        assert (observation["mic_value"], observation["mic_units"]) == (60, "mg/L")
        assert observation["source_observation_id"] == f"PMID:27355376:Table2:{gene}"
        assert "minimal medium" in observation["assay"]
        assert "below 10%" in observation["assay"]
        assert "activity" not in observation
        evidence, = observation["evidence"]
        assert evidence["reference"] == "PMID:27355376"
        assert "60 ug/mL" in evidence["notes"]
        assert "range (3-4 ug/mL), not a single value" in evidence["notes"]
    assert not context["measurement_policy"]["clinical_categories_inferred"]
    assert not context["measurement_policy"]["range_collapsed_to_point"]


def test_reference_ids_are_not_experimental_assignments(curation, context):
    for item in curation["claims"] + curation["observations"]:
        assert not {"protein_accession", "gene_id", "strain_taxon_id", "assembly_accession",
                    "biosample_accession", "bioproject_accession", "sra_accessions",
                    "source", "aro_id"} & item.keys()
    assert curation["exact_protein_alleles_assigned"] == 0
    assert curation["experimental_genomes_assigned"] == 0
    assert context["reference_genome"]["accession"] == "U00096.3"
    assert context["reference_genome"]["scope"] == "REFERENCE_GENOME_NOT_SEQUENCED_EXPERIMENTAL_DERIVATIVE"
    assert not context["reference_genome"]["assembly_accession_assigned"]
    assert context["taxonomy"]["562"]["rank"] == "species"
    assert context["taxonomy"]["511145"]["rank"] == "no rank"
    assert context["taxonomy"]["511145"]["parent"]["taxonId"] == 83333


@pytest.mark.parametrize("field", [
    "assembly_accession", "biosample_accession", "bioproject_accession", "sra_accessions",
])
def test_reference_identity_guard_rejects_canonical_sample_fields(curation, context, field):
    curation["observations"][0][field] = ["unexpected"] if field == "sra_accessions" else "unexpected"
    with pytest.raises(AssertionError):
        test_reference_ids_are_not_experimental_assignments(curation, context)


def test_versioned_protein_context_is_complete_for_reference_queries(context):
    expected = {"oppA": ("P23843", 171, 2), "oppB": ("P0AFH2", 126, 1),
                "oppC": ("P0AFH6", 130, 1), "oppD": ("P76027", 179, 2),
                "oppF": ("P77737", 169, 1)}
    assert context["reference_release"] == "2026_03"
    assert set(context["reference_proteins"]) == set(expected)
    for gene, (accession, entry, sequence) in expected.items():
        protein = context["reference_proteins"][gene]
        assert protein["accession"] == f"UniProtKB:{accession}"
        assert (protein["entry_version"], protein["sequence_version"]) == (entry, sequence)
        assert protein["reference_taxon_id"] == "NCBITaxon:83333"
        assert protein["scope"] == "REFERENCE_ONLY_NOT_EXPERIMENTAL_ALLELE"
        assert protein["entry_type"] == "UniProtKB reviewed (Swiss-Prot)"
    queries = []
    for request in context["uniprot_requests"]:
        parsed = urlsplit(request["url"])
        assert parsed.hostname == "rest.uniprot.org"
        assert request["status"] == 200 and request["release"] == "2026_03"
        assert len(request["sha256"]) == len(request["cache"]["sha256"]) == 64
        if parsed.path == "/uniprotkb/search":
            params = parse_qs(parsed.query)
            assert "sequence" not in params["fields"][0].split(",")
            assert request["complete_for_requested_reference_query"]
            queries.append(request["result_count"])
    assert queries == [1, 4]


def test_correction_and_compound_identity_limits_are_explicit(context):
    primary = context["primary"]
    assert primary["correction_inspected"]
    assert primary["correction_doi"] == "10.1371/journal.pgen.1006902"
    assert "Table 2 and Table S2 were not replaced" in primary["correction_scope"]
    assert primary["native_visual_review"] == [
        "Corrected Figure 3", "Original Figure 4", "Original Table 2",
    ]
    assert primary["structured_supplement_review"] == "Table S2, Word XML table rows"
    chemical = context["chemical_identity"]
    assert chemical["smiles_inchi_key_agree"]
    assert chemical["molecular_formula"] == "C17H26N8O5"
    assert "CHEBI:57289 (1+) remains separate" in chemical["primary_identity_location"]
    assert not chemical["tested_preparation_independently_reidentified"]


def test_receipt_and_historical_census_integrity(curation, context):
    pin = curation["context"]
    assert hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]
    reconciliation = json.loads(Path(str(PREFIX) + "-reconciliation.json").read_bytes())
    for key, expected_record_pin in (("previous_census", context["record_before"]),
                                     ("current_census", curation["record"])):
        pin = reconciliation[key]
        payload = (ROOT / pin["path"]).read_bytes()
        assert hashlib.sha256(payload).hexdigest() == pin["sha256"]
        rows = csv.DictReader(payload.decode().splitlines(), delimiter="\t")
        row, = [r for r in rows if r["identifier"] == "CHEBI:15353"]
        assert row["record_sha256"] == expected_record_pin["sha256"]
    assert reconciliation["records"] == 2939
    assert reconciliation["records_byte_identical"] == 2938
    assert reconciliation["resistance_assertions"] == 4841
    assert curation["records_changed"] == curation["curation_events_added"] == 1
    assert curation["claims_added"] == curation["measurements_added"] == 2
    assert reconciliation["whole_record_reviews_completed"] == 0
    assert not context["whole_record_review_complete"]
    assert context["whole_corpus_primary_review"] == "OPEN"


def test_source_assets_use_permitted_hosts_and_no_operational_payload(context):
    for asset in context["source_assets"]:
        assert urlsplit(asset["url"]).hostname in {"www.ebi.ac.uk", "journals.plos.org"}
        assert asset["size_bytes"] > 0 and len(asset["cache"]["sha256"]) == 64

    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not set(keys(context)) & {"sequence", "primers", "protocol", "constructs", "headers"}
