"""Citation labels and reference lineages cannot become experimental assignments."""

import copy
import csv
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import audit_card_study_context as audit  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


def entry():
    return {"references": [
        {"referenceNumber": 1,
         "citation": {"id": "111", "citationType": "journal article", "publicationDate": "2000",
                      "title": "A susceptibility study", "citationCrossReferences": [
                          {"database": "PubMed", "id": "111"}]},
         "referenceComments": [{"type": "STRAIN", "value": "A / B"},
                               {"type": "PLASMID", "value": "not exported"}],
         "referencePositions": ["NUCLEOTIDE SEQUENCE [GENOMIC DNA]", "MUTAGENESIS OF PRIVATE"]},
        {"referenceNumber": 2,
         "citation": {"id": "222", "citationType": "journal article", "publicationDate": "2001",
                      "title": "A separate paper", "citationCrossReferences": [
                          {"database": "PubMed", "id": "222"}]},
         "referenceComments": [{"type": "STRAIN", "value": "C"}, {"type": "STRAIN", "value": "D"}]},
    ]}


def taxonomy():
    return {"taxonId": 20, "active": True, "rank": "strain", "scientificName": "Reference strain",
            "lineage": [{"taxonId": 10, "rank": "species", "scientificName": "Reference species"}]}


def test_roles_are_scoped_hashes_not_variant_or_protocol_export():
    projected = audit.study_contexts(entry())
    assert [r["category"] for r in projected[0]["role_annotations"]] == ["NUCLEOTIDE SEQUENCE", "MUTAGENESIS"]
    assert projected[0]["title_mentions_susceptibility"] and not projected[1]["title_mentions_susceptibility"]
    encoded = json.dumps(projected)
    assert "PRIVATE" not in encoded and "not exported" not in encoded
    assert "A susceptibility study" not in encoded
    assert projected[0]["title_sha256"] == audit.definitions.text_hash("A susceptibility study")
    assert projected[0]["omitted_comment_types"] == ["PLASMID"]
    assert not any(r["experimental_subject_assignment"] for r in projected)


def test_strain_labels_stay_with_their_own_paper_without_splitting_or_representatives():
    contexts = audit.select_contexts(entry(), ["PMID:111"])
    assert len(contexts) == 1 and [s["value"] for s in contexts[0]["strain_annotations"]] == ["A / B"]
    assert not contexts[0]["strain_values_split_or_normalized"]
    other, = audit.select_contexts(entry(), ["PMID:222"])
    assert [s["value"] for s in other["strain_annotations"]] == ["C", "D"]
    assert not other["primary_review_completed_by_this_audit"]


@pytest.mark.parametrize("citations", [[], ["PMID:333"], ["PMID:111", "PMID:333"]])
def test_missing_citation_context_rejected(citations):
    with pytest.raises(ValueError, match="context missing"):
        audit.select_contexts(entry(), citations)


@pytest.mark.parametrize("positions", [None, "FUNCTION", [17], [" "]])
def test_malformed_role_annotations_rejected(positions):
    source = entry()
    source["references"][0]["referencePositions"] = positions
    with pytest.raises(ValueError, match="role annotation"):
        audit.study_contexts(source)


def test_unknown_role_retains_hash_without_inventing_role_or_phenotype():
    source = entry()
    source["references"][0]["referencePositions"] = ["UNRECOGNIZED DETAIL"]
    result = audit.study_contexts(source)[0]["role_annotations"]
    assert result == [{"category": "OTHER_HASH_ONLY",
                       "source_annotation_sha256": audit.definitions.text_hash("UNRECOGNIZED DETAIL")}]


def test_duplicate_reference_numbers_rejected():
    source = entry()
    source["references"][1]["referenceNumber"] = 1
    with pytest.raises(ValueError, match="reference identity"):
        audit.study_contexts(source)


def test_reference_species_lineage_is_not_a_tested_strain_assignment():
    projected = audit.reference_lineage(taxonomy())
    assert projected == {"taxon_id": "NCBITaxon:10", "scientific_name": "Reference species",
                         "rank": "species", "experimental_subject_assignment": False}
    source = taxonomy()
    source["lineage"] = []
    assert audit.reference_lineage(source) is None
    source.update(taxonId=10, rank="species", scientificName="Reference species")
    assert audit.reference_lineage(source) == projected


@pytest.mark.parametrize("change", ["inactive", "duplicate_species", "bad_taxid", "bad_parent", "blank_name"])
def test_invalid_or_ambiguous_reference_lineage_rejected(change):
    source = taxonomy()
    if change == "inactive":
        source["active"] = False
    elif change == "duplicate_species":
        source["lineage"].append(copy.deepcopy(source["lineage"][0]))
    elif change == "bad_taxid":
        source["taxonId"] = -1
    elif change == "bad_parent":
        source["lineage"][0]["taxonId"] = "10"
    else:
        source["lineage"][0]["scientificName"] = ""
    with pytest.raises(ValueError):
        audit.reference_lineage(source)


@pytest.fixture(scope="module")
def dossier():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def pin(value):
    body = (ROOT / value["path"]).read_bytes()
    assert hashlib.sha256(body).hexdigest() == value["sha256"]
    return body


def test_public_snapshot_binds_both_complete_candidate_cohorts_without_live_freeze(dossier, monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(ROOT / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    expected_terms, proteins = {}, {}
    for name in ("earlier", "expansion"):
        source = json.loads(pin(dossier["inputs"][name]))
        for tid, term in source["terms"].items():
            if not term["reference_candidates"]:
                continue
            assert tid not in expected_terms
            expected_terms[tid] = term
            assert dossier["terms"][tid]["source_audit"] == name
            actual = dossier["terms"][tid]
            for key in ("record_memberships", "definition_citation_ids"):
                assert actual[key] == term[key]
            assert len(actual["reference_candidates"]) == len(term["reference_candidates"])
            for candidate, expected in zip(
                    actual["reference_candidates"], term["reference_candidates"], strict=True):
                assert all(candidate[k] == v for k, v in expected.items())
                accession = candidate["protein_accession"]
                proteins[accession] = source["proteins"][accession]
                assert all(dossier["proteins"][accession][k] == v for k, v in proteins[accession].items())
                assert not candidate["experimental_subject_assignment"]
                assert not candidate["exact_allele_assignment"]
    assert set(dossier["terms"]) == set(expected_terms) and len(expected_terms) == 49
    assert set(dossier["proteins"]) == set(proteins) and len(proteins) == 76
    census = {r["identifier"]: r for r in csv.DictReader(
        pin(dossier["inputs"]["census"]).decode().splitlines(), delimiter="\t")}
    expected_ids = {i for t in expected_terms.values() for i in t["record_memberships"]}
    assert len(census) == 2939 and len(expected_ids) == 63
    assert {r["identifier"] for r in dossier["records"]} == expected_ids
    for row in dossier["records"]:
        assert row["sha256"] == census[row["identifier"]]["record_sha256"]
        assert row["standard_inchi_key"] == census[row["identifier"]]["standard_inchi_key"]
        assert row["whole_record_primary_review"] == "OPEN"


def test_summary_counts_metadata_links_not_experiments(dossier):
    all_contexts = [r for p in dossier["proteins"].values() for r in p["reference_contexts"]]
    matched = [r for t in dossier["terms"].values() for c in t["reference_candidates"]
               for r in c["matched_study_contexts"]]
    summary = dossier["summary"]
    assert len(all_contexts) == summary["citation_contexts"] == 246
    assert len(matched) == summary["matched_study_context_links"] == 81
    assert sum(bool(r["strain_annotations"]) for r in matched) == 58
    assert sum(len(r["strain_annotations"]) > 1 for r in matched) == 3
    ranks = Counter(p["taxonomy_rank"] for p in dossier["proteins"].values())
    assert ranks == summary["reference_taxonomy_ranks"]
    assert summary["experimental_subject_or_allele_assignments"] == 0
    assert summary["whole_record_reviews_completed"] == 0
    assert summary["full_corpus_goal_status"] == "OPEN"


def test_irek_reference_and_study_strain_remain_distinct(dossier):
    protein = dossier["proteins"]["UniProtKB:Q820A8"]
    assert protein["reference_taxon_id"] == "NCBITaxon:226185"
    assert "V583" in protein["reference_organism_name"]
    study, = [r for r in protein["reference_contexts"] if "PMID:34672600" in r["citation_identifiers"]]
    assert [a["value"] for a in study["strain_annotations"]] == ["OG1"]
    assert not study["experimental_subject_assignment"]


def test_nime_susceptibility_title_is_only_a_review_flag(dossier):
    term = dossier["terms"]["ARO:3007107"]
    candidate, = [c for c in term["reference_candidates"] if c["protein_accession"] == "UniProtKB:Q6PV97"]
    study, = candidate["matched_study_contexts"]
    assert "PMID:15273153" in study["citation_identifiers"] and study["title_mentions_susceptibility"]
    assert not study["primary_review_completed_by_this_audit"]
    assert candidate["experimental_subject_assignment"] is False


def test_multiple_strain_annotations_and_bmr_slash_label_are_not_collapsed(dossier):
    for accession, pmid, values in (
        ("UniProtKB:E1A0W6", "21830908", ["S08-IJ52", "S08-KM17"]),
        ("UniProtKB:B7TCJ0", "19131424", ["P126.11.99.C1", "P475.10.99.C3"]),
        ("UniProtKB:A0A0C6ET92", "25313205", ["NTUH-2239-1", "NTUH-6123"]),
        ("UniProtKB:P33449", "1675788", ["168 / BD170"]),
    ):
        candidates = [r for r in dossier["proteins"][accession]["reference_contexts"]
                      if "PMID:" + pmid in r["citation_identifiers"]]
        assert len(candidates) == 1
        assert [a["value"] for a in candidates[0]["strain_annotations"]] == values
        assert not candidates[0]["strain_values_split_or_normalized"]


def test_primary_holds_do_not_become_negative_evidence(dossier):
    hold = dossier["bmr_primary_hold"]
    assert hold["http_status"] == 403 and hold["pmid"] == "9079903"
    assert hold["prior_distinct_paper_hold"]["source_pmid"] == "1675788"
    for key in ("full_text_received", "primary_results_reviewed", "alternate_route_attempted",
                "absence_or_global_unavailability_inferred"):
        assert hold[key] is False
    assert dossier["constraints"]["ncbi_requests"] == dossier["constraints"]["github_mutations"] == 0
    assert dossier["constraints"]["issue_1040"] == "DEFERRED"


def test_all_matched_contexts_bind_exact_papers_and_keep_missing_papers_explicit(dossier):
    for term in dossier["terms"].values():
        linked = set()
        for candidate in term["reference_candidates"]:
            contexts = dossier["proteins"][candidate["protein_accession"]]["reference_contexts"]
            selected = [c for c in contexts
                        if set(c["citation_identifiers"]) & set(candidate["source_citation_ids"])]
            assert candidate["matched_study_contexts"] == selected
            linked.update(candidate["source_citation_ids"])
            for citation in candidate["source_citation_ids"]:
                key = term["source_audit"] + ":" + citation.removeprefix("PMID:")
                assert dossier["queries"][key]["complete_for_query"]
                assert dossier["queries"][key]["result_count"] > 0
        assert term["source_citations_without_candidate_context"] == sorted(
            set(term["definition_citation_ids"]) - linked)
    assert dossier["terms"]["ARO:3003007"]["source_citations_without_candidate_context"] == ["PMID:9079903"]


def test_public_export_has_no_raw_role_details_or_experimental_assignments(dossier):
    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert dossier["scope"] == audit.SCOPE
    assert not set(keys(dossier)) & {"sequence", "features", "variants", "alteration", "title",
                                   "referencePositions", "strain_taxon_id", "assembly_accession",
                                   "biosample_accession", "mic", "protocol", "primers"}
    assert all(not p["experimental_subject_assignment"] for p in dossier["proteins"].values())
