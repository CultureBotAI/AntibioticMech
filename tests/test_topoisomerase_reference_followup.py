"""Reference identifiers must not become inferred experimental resistance alleles."""

import copy
import hashlib
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from audit_topoisomerase_references import SCOPE, project_reference, read_response  # noqa: E402

DOSSIER = ROOT / "research/2026-10-09-topoisomerase-reference-followup.json"


@pytest.fixture
def entry():
    return {
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "primaryAccession": "P00001",
        "entryAudit": {"entryVersion": 3, "sequenceVersion": 1},
        "organism": {"taxonId": 101, "scientificName": "Reference organism"},
        "genes": [{"geneName": {"value": "gyrA"}, "orderedLocusNames": [{"value": "LOCUS_1"}]}],
        "proteinDescription": {"recommendedName": {"fullName": {"value": "Reference protein"}}},
        "references": [
            {
                "citation": {
                    "publicationDate": "2020",
                    "citationCrossReferences": [
                        {"database": "PubMed", "id": "123"},
                        {"database": "DOI", "id": "10.1/example"},
                    ],
                },
                "referencePositions": ["REDACTED_TEST_SENTINEL"],
                "referenceComments": [{"type": "STRAIN", "value": "not-an-experimental-assignment"}],
            }
        ],
    }


@pytest.fixture
def taxonomy():
    return {
        "taxonId": 101,
        "scientificName": "Reference organism",
        "rank": "strain",
        "active": True,
        "lineage": [{"taxonId": 100, "scientificName": "Species name", "rank": "species"}],
    }


@pytest.fixture(scope="module")
def dossier():
    return json.loads(DOSSIER.read_bytes())


def test_projection_has_versions_and_species_ancestry_without_experimental_details(entry, taxonomy):
    result = project_reference(entry, "gyrA", 100, taxonomy)
    assert result["protein_accession"] == "UniProtKB:P00001"
    assert result["entry_version"] == 3 and result["sequence_version"] == 1
    assert result["reference_taxon_id"] == "NCBITaxon:101"
    assert result["source_species_taxon_id"] == "NCBITaxon:100"
    assert result["reference_taxon_rank"] == "strain"
    assert result["species_lineage_verified"]
    assert result["ordered_locus_names"] == ["LOCUS_1"]
    assert not result["exact_resistance_allele"] and not result["experimental_subject_assignment"]
    assert "REDACTED_TEST_SENTINEL" not in json.dumps(result)
    assert "not-an-experimental-assignment" not in json.dumps(result)
    assert not result["bibliography"][0]["primary_results_reviewed"]


def test_explicit_gene_synonym_can_match_but_not_a_locus_name(entry, taxonomy):
    entry["genes"][0]["geneName"]["value"] = "grlA"
    entry["genes"][0]["synonyms"] = [{"value": "parC"}]
    assert project_reference(entry, "parC", 100, taxonomy)["gene_names"] == ["grlA", "parC"]
    with pytest.raises(ValueError, match="gene name"):
        project_reference(entry, "LOCUS_1", 100, taxonomy)


@pytest.mark.parametrize(
    "change", ["unreviewed", "sequence", "wrong_gene", "duplicate_gene", "no_version", "string_version"]
)
def test_rejects_unsupported_entry_identity(entry, taxonomy, change):
    if change == "unreviewed":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif change == "sequence":
        entry["sequence"] = ""
    elif change == "wrong_gene":
        entry["genes"][0]["geneName"]["value"] = "gyrB"
    elif change == "duplicate_gene":
        entry["genes"].append(copy.deepcopy(entry["genes"][0]))
    elif change == "no_version":
        entry["entryAudit"].pop("sequenceVersion")
    else:
        entry["entryAudit"]["entryVersion"] = "3"
    with pytest.raises(ValueError):
        project_reference(entry, "gyrA", 100, taxonomy)


@pytest.mark.parametrize(
    "change", ["inactive", "wrong_reference", "wrong_species", "missing_species", "duplicate_species"]
)
def test_rejects_taxonomic_inference_from_names_alone(entry, taxonomy, change):
    if change == "inactive":
        taxonomy["active"] = False
    elif change == "wrong_reference":
        taxonomy["taxonId"] = 102
    elif change == "wrong_species":
        taxonomy["lineage"][0]["taxonId"] = 200
    elif change == "missing_species":
        taxonomy["lineage"] = []
    else:
        taxonomy["lineage"].append(copy.deepcopy(taxonomy["lineage"][0]))
    with pytest.raises(ValueError):
        project_reference(entry, "gyrA", 100, taxonomy)


def test_direct_species_and_no_rank_reference_are_not_forced_to_strain(entry, taxonomy):
    taxonomy["rank"] = "no rank"
    assert project_reference(entry, "gyrA", 100, taxonomy)["reference_taxon_rank"] == "no rank"
    entry["organism"]["taxonId"] = taxonomy["taxonId"] = 100
    taxonomy["rank"], taxonomy["lineage"] = "species", []
    assert project_reference(entry, "gyrA", 100, taxonomy)["reference_taxon_rank"] == "species"


@pytest.mark.parametrize(
    "change",
    [
        "none",
        "wrong_host",
        "wrong_query",
        "bad_checksum",
        "denied",
        "paginated",
        "missing_release",
        "incomplete",
    ],
)
def test_response_provenance_gates(tmp_path, change):
    body = {"results": []}
    payload = json.dumps(body).encode()
    receipt = {
        "url": "https://rest.uniprot.org/uniprotkb/search?query=test",
        "status": 200,
        "retrieved_at": "2026-10-09T00:00:00Z",
        "sha256": hashlib.sha256(payload).hexdigest(),
        "headers": {"X-UniProt-Release": "2026_03", "X-Total-Results": "0"},
    }
    if change == "wrong_host":
        receipt["url"] = "https://example.org/uniprotkb/search?query=test"
    elif change == "wrong_query":
        receipt["url"] += "&extra=1"
    elif change == "bad_checksum":
        receipt["sha256"] = "0" * 64
    elif change == "denied":
        receipt["status"] = 403
    elif change == "paginated":
        receipt["headers"]["Link"] = "next"
    elif change == "missing_release":
        receipt["headers"].pop("X-UniProt-Release")
    elif change == "incomplete":
        receipt["headers"]["X-Total-Results"] = "1"
    (tmp_path / "test-response.bin").write_bytes(payload)
    (tmp_path / "test-receipt.json").write_text(json.dumps(receipt))
    if change == "none":
        result, request = read_response(tmp_path, tmp_path, "test", "/uniprotkb/search", {"query": ["test"]})
        assert result == body and request["release"] == "2026_03"
    else:
        with pytest.raises(ValueError):
            read_response(tmp_path, tmp_path, "test", "/uniprotkb/search", {"query": ["test"]})


def test_complete_cohort_retains_ambiguous_and_zero_hit_terms(dossier):
    assert dossier["scope"] == SCOPE and len(dossier["terms"]) == 57
    summary = dossier["summary"]
    assert summary["corpus_records"] == 2939 and summary["source_records"] == 21
    assert summary["source_assertion_memberships"] == len(dossier["memberships"]) == 332
    assert summary["terms_with_species_grounding"] == 53
    assert summary["terms_with_reviewed_candidates"] == 37
    assert summary["reviewed_protein_queries"] == 45 and summary["queries_with_no_reviewed_hit"] == 16
    assert summary["distinct_reference_proteins"] == 68 and summary["reference_taxa_verified"] == 27
    assert dossier["source_name_taxonomy"]["Salmonella serovars"]["status"] == "BROAD_SOURCE_NAME_UNRESOLVED"
    assert dossier["source_name_taxonomy"]["Salmonella isangi"]["status"] == "NO_EXACT_ACTIVE_SPECIES_NAME"
    for row in dossier["queries"].values():
        assert not row["zero_hit_is_absence"]
        if not row["accessions"]:
            assert row["status_label"] == "NO_REVIEWED_HIT_NOT_GENE_ABSENCE"


def test_all_references_and_memberships_keep_source_scope(dossier):
    for term_id, term in dossier["terms"].items():
        memberships = [row for row in dossier["memberships"] if row["aro_id"] == term_id]
        assert len(memberships) == term["source_assertion_memberships"]
        assert sorted({row["record_id"] for row in memberships}) == term["record_ids"]
        assert term["primary_review_status"] == "OPEN"
        assert not term["experimental_assignment"] and not term["exact_allele_assignment"]
        if term["reference_query"] is not None:
            assert term["reference_candidates"] == dossier["queries"][term["reference_query"]]["accessions"]
        for accession in term["reference_candidates"]:
            reference = dossier["reference_proteins"][accession]
            assert reference["species_lineage_verified"]
            assert term["source_species_taxon_id"] == reference["source_species_taxon_id"]
            assert term["source_gene_symbol"].lower() in {name.lower() for name in reference["gene_names"]}


def test_no_operational_export_or_completion_promotion(dossier):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    prohibited = {
        "sequence",
        "variants",
        "alteration",
        "referencePositions",
        "referenceComments",
        "constructs",
        "primers",
        "protocol",
        "coordinates",
        "measurement_value",
        "mic",
        "smiles",
    }
    assert not prohibited & set(keys(dossier))
    assert dossier["whole_corpus_primary_review"] == "OPEN"
    for key in (
        "biological_records_changed",
        "experimental_subject_assignments",
        "exact_allele_assignments",
        "whole_record_reviews_completed",
    ):
        assert dossier["summary"][key] == 0
    assert (
        dossier["ncbi_endpoint_requests"]
        == dossier["source_adoptions"]
        == dossier["github_mutations"]
        == dossier["outreach"]
        == 0
    )
    assert "ncbi.nlm.nih.gov" not in json.dumps(dossier)
