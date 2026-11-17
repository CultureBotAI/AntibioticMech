"""Preserve unreviewed, fragment, locus and reference-genome evidence boundaries."""

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from audit_topoisomerase_references import project_reference  # noqa: E402
from audit_unreviewed_topoisomerase import SCOPE, project_proteome, proteome_link  # noqa: E402


@pytest.fixture
def entry():
    return {
        "primaryAccession": "A0A0000001",
        "entryType": "UniProtKB unreviewed (TrEMBL)",
        "entryAudit": {"entryVersion": 5, "sequenceVersion": 1},
        "organism": {"taxonId": 11, "scientificName": "Reference organism"},
        "genes": [
            {
                "geneName": {"value": "gyr A"},
                "synonyms": [{"value": "gyrA"}],
                "orderedLocusNames": [{"value": "LOCUS_A"}],
                "orfNames": [{"value": "ORF_A"}],
            }
        ],
        "proteinDescription": {
            "flag": "Fragment",
            "submissionNames": [
                {"fullName": {"value": "DNA gyrase subunit A"}},
                {"fullName": {"value": "GyrA"}},
            ],
        },
    }


@pytest.fixture
def taxonomy():
    return {
        "taxonId": 11,
        "scientificName": "Reference organism",
        "active": True,
        "rank": "strain",
        "lineage": [{"taxonId": 10, "scientificName": "Species name", "rank": "species"}],
    }


@pytest.fixture
def proteome():
    return {
        "id": "UP000000001",
        "proteomeType": "Reference proteome",
        "taxonomy": {"taxonId": 11, "scientificName": "Reference organism"},
        "genomeAssembly": {"assemblyId": "GCA_000000001.2", "source": "ENA/EMBL"},
        "components": [{"name": "Chromosome", "description": "not exported"}],
        "modified": "2026-09-02",
    }


@pytest.fixture
def cross_reference():
    return {
        "database": "Proteomes",
        "id": "UP000000001",
        "properties": [{"key": "Component", "value": "Chromosome"}],
    }


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / "research/2026-10-09-topoisomerase-unreviewed-followup.json").read_bytes())


def test_unreviewed_requires_explicit_opt_in(entry, taxonomy):
    with pytest.raises(ValueError, match="review status"):
        project_reference(entry, "gyrA", 10, taxonomy)
    projected = project_reference(entry, "gyrA", 10, taxonomy, reviewed=False)
    assert projected["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
    assert projected["annotation_status"] == "UNREVIEWED_EXPERIMENTAL_IDENTITY_NOT_ESTABLISHED_BY_THIS_AUDIT"
    assert projected["protein_description_flag"] == "Fragment"
    assert [row["value"] for row in projected["protein_names"]] == ["DNA gyrase subunit A", "GyrA"]
    assert projected["gene_orf_names"] == ["ORF_A"] and projected["ordered_locus_names"] == ["LOCUS_A"]
    assert projected["gene_names"] == ["gyr A", "gyrA"]
    assert not projected["exact_resistance_allele"] and not projected["experimental_subject_assignment"]


@pytest.mark.parametrize("reviewed", [0, 1, None, "false"])
def test_truthy_or_falsy_nonboolean_review_modes_are_rejected(entry, taxonomy, reviewed):
    with pytest.raises(ValueError, match="explicit"):
        project_reference(entry, "gyrA", 10, taxonomy, reviewed=reviewed)


def test_reviewed_entry_cannot_be_relabeled_unreviewed(entry, taxonomy):
    entry["entryType"] = "UniProtKB reviewed (Swiss-Prot)"
    with pytest.raises(ValueError, match="review status"):
        project_reference(entry, "gyrA", 10, taxonomy, reviewed=False)


def test_absent_fragment_flag_is_not_completeness_evidence(entry, taxonomy):
    entry["proteinDescription"].pop("flag")
    result = project_reference(entry, "gyrA", 10, taxonomy, reviewed=False)
    assert result["protein_description_flag"] is None and not result["unflagged_means_complete"]


def test_recommended_name_does_not_make_an_entry_reviewed(entry, taxonomy):
    entry["proteinDescription"] = {"recommendedName": {"fullName": {"value": "DNA gyrase"}}}
    result = project_reference(entry, "gyrA", 10, taxonomy, reviewed=False)
    assert result["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
    assert result["protein_names"] == [{"kind": "recommendedName", "value": "DNA gyrase"}]


@pytest.mark.parametrize("change", ["gene", "species", "sequence", "names"])
def test_unreviewed_mode_does_not_relax_identity_or_export_gates(entry, taxonomy, change):
    if change == "gene":
        entry["genes"][0]["synonyms"] = []
    elif change == "species":
        taxonomy["lineage"][0]["taxonId"] = 20
    elif change == "sequence":
        entry["sequence"] = ""
    else:
        entry["proteinDescription"] = {}
    with pytest.raises(ValueError):
        project_reference(entry, "gyrA", 10, taxonomy, reviewed=False)


def test_verified_proteome_link_remains_reference_context(entry, proteome, cross_reference):
    projected = project_proteome(proteome)
    link = proteome_link(entry, cross_reference, projected)
    assert link["status"] == "REFERENCE_CONTEXT_VERIFIED"
    assert link["reference_assembly_id"] == "GCA_000000001.2"
    assert not link["experimental_genome_assignment"] and not projected["experimental_genome_assignment"]
    assert "not exported" not in json.dumps(projected)


@pytest.mark.parametrize("change", ["taxon", "component", "no_component"])
def test_unresolved_metadata_join_never_assigns_reference_assembly(entry, proteome, cross_reference, change):
    if change == "taxon":
        proteome["taxonomy"]["taxonId"] = 12
    elif change == "component":
        cross_reference["properties"][0]["value"] = "Unknown component"
    else:
        cross_reference["properties"] = []
    link = proteome_link(entry, cross_reference, project_proteome(proteome))
    assert link["status"] == "UNRESOLVED_METADATA_JOIN" and link["reference_assembly_id"] is None


@pytest.mark.parametrize("identifier", ["GCA_000000001", "UP000000001", "not-an-assembly"])
def test_assembly_identifier_must_be_versioned(proteome, identifier):
    proteome["genomeAssembly"]["assemblyId"] = identifier
    with pytest.raises(ValueError, match="assembly"):
        project_proteome(proteome)


def test_missing_assembly_stays_missing(entry, proteome, cross_reference):
    proteome.pop("genomeAssembly")
    link = proteome_link(entry, cross_reference, project_proteome(proteome))
    assert link["reference_assembly_id"] is None
    assert not link["experimental_genome_assignment"]


def test_wrong_proteome_identifier_is_not_joined(entry, proteome, cross_reference):
    cross_reference["id"] = "UP000000002"
    with pytest.raises(ValueError, match="cross-reference"):
        proteome_link(entry, cross_reference, project_proteome(proteome))


def test_entire_reviewed_no_hit_cohort_is_retained(dossier):
    prior = json.loads((ROOT / dossier["inputs"]["prior_dossier"]["path"]).read_bytes())
    expected = {
        tid
        for tid, row in prior["terms"].items()
        if row["reference_query"] is not None and not row["reference_candidates"]
    }
    assert expected == set(dossier["terms"]) and len(expected) == 16
    summary = dossier["summary"]
    assert summary["completed_unreviewed_queries"] == summary["queries_with_candidates"] == 16
    assert summary["unreviewed_proteins"] == 82 and summary["source_flagged_fragments"] == 42
    assert summary["reference_taxa"] == 34 and summary["reference_proteomes"] == 18
    assert summary["combined_topoisomerase_terms_with_candidates"] == 53
    assert summary["combined_topoisomerase_reference_candidates"] == 150
    for term in dossier["terms"].values():
        assert not term["reviewed_candidates"] and term["primary_review_status"] == "OPEN"
        assert not term["exact_allele_assignment"] and not term["experimental_subject_assignment"]
    assert all(
        row["entry_type"] == "UniProtKB unreviewed (TrEMBL)"
        for row in dossier["unreviewed_proteins"].values()
    )


def test_distinct_loci_with_shared_symbol_are_not_collapsed(dossier):
    groups = dossier["shared_symbol_in_same_proteome"]
    assert groups
    (group,) = [row for row in groups if row["gene_symbol"] == "parC" and row["proteome_id"] == "UP000003139"]
    assert set(group["accessions"]) == {"A0ABP2DN41", "A0ABM9XKB0"}
    loci = {tuple(dossier["unreviewed_proteins"][key]["gene_orf_names"]) for key in group["accessions"]}
    assert len(loci) == 2
    assert group["status"] == "MULTIPLE_ENTRIES_RETAINED_NOT_A_UNIQUE_LOCUS_ASSIGNMENT"


def test_export_keeps_reference_only_and_nonoperational_scope(dossier):
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
        "coordinates",
        "protocol",
        "primers",
        "measurement_value",
        "mic",
        "annotationScore",
    }
    assert not prohibited & set(keys(dossier))
    assert dossier["scope"] == SCOPE and dossier["whole_corpus_primary_review"] == "OPEN"
    for key in (
        "biological_records_changed",
        "exact_allele_assignments",
        "experimental_genome_assignments",
        "whole_record_reviews_completed",
    ):
        assert dossier["summary"][key] == 0
    for key in ("ncbi_endpoint_requests", "source_adoptions", "github_mutations", "outreach"):
        assert dossier[key] == 0
    assert "ncbi.nlm.nih.gov" not in json.dumps(dossier)
