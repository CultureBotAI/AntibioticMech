"""Taxonomic synonymy, protein identity and resistance evidence remain distinct."""

import copy
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_fungamr_references as audit  # noqa: E402


@pytest.mark.parametrize(
    "change",
    [
        "none",
        "scientific",
        "other_names",
        "hybrid",
        "virus",
        "inactive",
        "strain",
        "ambiguous",
        "duplicate",
        "bool_id",
        "bad_synonyms",
    ],
)
def test_species_name_scope(change):
    taxon = {
        "taxonId": 498019,
        "scientificName": "Candidozyma auris",
        "synonyms": ["Candida auris"],
        "rank": "species",
        "active": True,
    }
    body = {"results": [taxon]}
    if change == "scientific":
        taxon["scientificName"] = "Candida auris"
        taxon["synonyms"] = []
    elif change == "other_names":
        taxon["otherNames"] = taxon.pop("synonyms")
    elif change in {"hybrid", "virus"}:
        taxon["scientificName"] = (
            "Candida auris x Candida albicans" if change == "hybrid" else "Candida auris-associated virus"
        )
        taxon["synonyms"] = []
    elif change == "inactive":
        taxon["active"] = False
    elif change == "strain":
        taxon["rank"] = "strain"
    elif change in {"ambiguous", "duplicate"}:
        body["results"].append(copy.deepcopy(taxon))
        if change == "ambiguous":
            body["results"][1]["taxonId"] += 1
    elif change == "bool_id":
        taxon["taxonId"] = True
    elif change == "bad_synonyms":
        taxon["synonyms"] = "Candida auris"
    if change in {"duplicate", "bool_id", "bad_synonyms"}:
        with pytest.raises(ValueError):
            audit.exact_name(body, "Candida auris")
        return
    result = audit.exact_name(body, "Candida auris")
    assert (result["species_id"] == 498019) == (change in {"none", "scientific"})


def entry(reviewed=True):
    return {
        "primaryAccession": "TEST",
        "entryType": "UniProtKB reviewed (Swiss-Prot)" if reviewed else "UniProtKB unreviewed (TrEMBL)",
        "entryAudit": {"entryVersion": 1, "sequenceVersion": 1},
        "genes": [{"geneName": {"value": "CYP51"}, "orfNames": [{"value": "LOCUS"}]}],
        "organism": {"taxonId": 208348, "scientificName": "Puccinia triticina"},
        "proteinDescription": {"recommendedName": {"fullName": {"value": "Reference protein"}}},
    }


@pytest.mark.parametrize("reviewed", [True, False])
@pytest.mark.parametrize(
    "change",
    [
        "none",
        "review_status",
        "sequence",
        "features",
        "duplicate_entry",
        "duplicate_gene",
        "wrong_gene",
        "orf_only",
        "suggestions",
    ],
)
def test_gene_search_scope(reviewed, change):
    body = {"results": [entry(reviewed)]}
    selected = body["results"][0]
    if change == "review_status":
        selected["entryType"] = entry(not reviewed)["entryType"]
    elif change in {"sequence", "features"}:
        selected[change] = "not for export"
    elif change == "duplicate_entry":
        body["results"].append(copy.deepcopy(selected))
    elif change == "duplicate_gene":
        selected["genes"].append(copy.deepcopy(selected["genes"][0]))
    elif change == "wrong_gene":
        selected["genes"][0]["geneName"]["value"] = "CYP51B"
    elif change == "orf_only":
        selected["genes"] = [{"orfNames": [{"value": "CYP51"}]}]
    elif change == "suggestions":
        body = {"results": [], "suggestions": [{"query": "wrong taxonomy", "hits": 99}]}
    if change not in {"none", "suggestions"}:
        with pytest.raises(ValueError):
            audit.validate_gene_results(body, "CYP51", reviewed)
        return
    result = audit.validate_gene_results(body, "CYP51", reviewed)
    assert result["result_count"] == (0 if change == "suggestions" else 1)
    assert not result["zero_results_establish_absence"]


@pytest.mark.parametrize(
    "counts,status",
    [
        ([(True, 1)], "REVIEWED_REFERENCE"),
        ([(True, 2)], "MULTIPLE_CANDIDATES_NO_SELECTION"),
        ([(True, 0), (False, 1)], "UNREVIEWED_CANDIDATE"),
        ([(True, 0), (False, 4)], "MULTIPLE_CANDIDATES_NO_SELECTION"),
        ([(True, 0), (False, 0)], "NO_EXACT_GENE_RESULTS_NOT_ABSENCE"),
        ([(True, 0)], None),
        ([(False, 1)], None),
        ([(True, 1), (False, 1)], None),
        ([(True, 0), (True, 1)], None),
        ([(True, -1)], None),
        ([(True, True)], None),
    ],
)
def test_query_disposition(counts, status):
    queries = [{"reviewed_subset": reviewed, "result_count": count} for reviewed, count in counts]
    if status is None:
        with pytest.raises(ValueError):
            audit.disposition(queries)
    else:
        assert audit.disposition(queries) == status


@pytest.mark.parametrize("reviewed", [True, False])
@pytest.mark.parametrize("change", ["none", "taxon", "species", "inactive", "version", "review_flag"])
def test_reference_is_never_experimental_identity(reviewed, change):
    protein = entry(reviewed)
    taxon = {
        "taxonId": 208348,
        "scientificName": "Puccinia triticina",
        "active": True,
        "rank": "species",
        "lineage": [],
    }
    if change == "taxon":
        protein["organism"]["taxonId"] = 1
    elif change == "species":
        taxon["rank"] = "strain"
        taxon["lineage"] = [{"rank": "species", "taxonId": 1}]
    elif change == "inactive":
        taxon["active"] = False
    elif change == "version":
        protein["entryAudit"]["entryVersion"] = True
    elif change == "review_flag":
        reviewed = "true"
    if change != "none":
        with pytest.raises(ValueError):
            audit.project(protein, taxon, "CYP51", 208348, reviewed)
        return
    result = audit.project(protein, taxon, "CYP51", 208348, reviewed)
    assert not result["exact_resistance_allele"] and not result["experimental_subject_assignment"]
    assert not result["canonical_reference_established"] and not result["new_resistance_assertion"]
    assert result["experimental_genome_assignment"] is None
    assert result["orf_names"] == ["LOCUS"]
    assert result["role"] == ("REVIEWED_GENE_REFERENCE" if reviewed else "UNREVIEWED_REFERENCE_CANDIDATE")


@pytest.mark.parametrize("change", ["none", "accession", "archive", "protein", "molecule_type", "duplicate"])
def test_archive_reference_is_not_a_genome_assignment(change):
    protein = {
        "primaryAccession": "C6GJL4",
        "uniProtKBCrossReferences": [
            {
                "database": "EMBL",
                "id": "FJ976683",
                "properties": [
                    {"key": "ProteinId", "value": "ACS37521.1"},
                    {"key": "Status", "value": "-"},
                    {"key": "MoleculeType", "value": "mRNA"},
                ],
            }
        ],
    }
    link = protein["uniProtKBCrossReferences"][0]
    if change == "accession":
        protein["primaryAccession"] = "OTHER"
    elif change == "archive":
        link["id"] = "OTHER"
    elif change == "protein":
        link["properties"][0]["value"] = "OTHER"
    elif change == "molecule_type":
        link["properties"][2]["value"] = "Genomic_DNA"
    elif change == "duplicate":
        protein["uniProtKBCrossReferences"].append(copy.deepcopy(link))
    if change != "none":
        with pytest.raises(ValueError):
            audit.archive_crosswalk(protein)
        return
    result = audit.archive_crosswalk(protein)
    assert result["role"] == "PAPER_REFERENCE_LOCUS_NOT_GENOME_OR_TESTED_ALLELE"
    assert not result["archive_endpoint_requested"]


@pytest.mark.parametrize(
    "change",
    [
        "none",
        "doi",
        "source_name",
        "target_name",
        "mb",
        "pages",
        "visual",
        "assessment",
        "taxid",
        "name",
        "rank",
        "inactive",
        "other_name",
        "hash",
    ],
)
def test_other_name_needs_the_specific_primary_assessment(tmp_path, change):
    paths = []
    for filename in ("source.pdf", "receipt.json", "page7.png", "page9.png"):
        path = tmp_path / filename
        path.write_bytes(b"synthetic transport fixture, not scientific evidence")
        paths.append(audit.reference.pin(tmp_path, path))
    review = {
        "source": paths[0],
        "receipt": paths[1],
        "rendered_pages": paths[2:],
        "doi": "10.3314/mmj.22.004",
        "source_name": "Nakaseomyces glabratus",
        "uniprot_species_name": "Candida glabrata",
        "mycobank_id_reported_by_paper": "843854",
        "nomenclatural_synonymy_verified": True,
        "native_pages_visually_inspected": True,
        "printed_pages": [126, 128],
        "zero_based_pages": [7, 9],
    }
    taxon = {
        "taxonId": 5478,
        "scientificName": "Candida glabrata",
        "active": True,
        "rank": "species",
        "otherNames": ["Nakaseomyces glabratus"],
    }
    fields = {
        "doi": "doi",
        "source_name": "source_name",
        "target_name": "uniprot_species_name",
        "mb": "mycobank_id_reported_by_paper",
    }
    if change in fields:
        review[fields[change]] = "OTHER"
    elif change == "pages":
        review["printed_pages"] = [127, 128]
    elif change == "visual":
        review["native_pages_visually_inspected"] = False
    elif change == "assessment":
        review["nomenclatural_synonymy_verified"] = False
    elif change == "taxid":
        taxon["taxonId"] = 1
    elif change == "name":
        taxon["scientificName"] = "OTHER"
    elif change == "rank":
        taxon["rank"] = "strain"
    elif change == "inactive":
        taxon["active"] = False
    elif change == "other_name":
        taxon["otherNames"] = []
    elif change == "hash":
        review["source"]["sha256"] = "0" * 64
    body = {"results": [taxon]}
    if change != "none":
        with pytest.raises(ValueError):
            audit.nomenclature(tmp_path, review, body)
        return
    assert audit.exact_name(body, "Nakaseomyces glabratus")["species_id"] is None
    resolved = audit.nomenclature(tmp_path, review, body)
    assert resolved["species_id"] == 5478
    assert not resolved["experimental_subject_assignment"]


def test_saved_checkpoint_coverage_and_limits():
    context = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert context["summary"]["term_dispositions"] == {
        "REVIEWED_REFERENCE": 3,
        "UNREVIEWED_CANDIDATE": 1,
        "MULTIPLE_CANDIDATES_NO_SELECTION": 4,
        "NO_EXACT_GENE_RESULTS_NOT_ABSENCE": 5,
    }
    assert len(context["names"]) == 10 and len(context["terms"]) == 13
    assert sum(len(t["queries"]) for t in context["terms"].values()) == 23
    assert context["summary"]["total_reviewed_reference_contexts"] == 9
    assert all(
        t["exact_allele_assignment"] is None
        and t["experimental_subject_assignment"] is None
        and not t["new_resistance_assertion"]
        for t in context["terms"].values()
    )
    assert (
        context["names"]["Nakaseomyces glabratus"]["status"] == "PRIMARY_NOMENCLATURE_PLUS_UNIPROT_TAXONOMY"
    )
    assert context["names"]["Candida auris"]["matching_field"] == "synonyms"
    assert context["puccinia_partial_primary_context"]["native_full_text_or_figures_reviewed"] is False
    assert context["summary"]["whole_record_reviews_completed"] == 0
