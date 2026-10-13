"""Historical RNA leads and taxonomy name matches are not experimental IDs."""
import copy
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

ROOT = Path(__file__).resolve().parents[1]
CONTEXT = ROOT / "research/2026-10-13-rrna-context.json"
NAMES = ("Tetrahymena thermophila", "Halobacterium halobium", "Halobacterium cutirubrum")
PAPERS = {"3562233": "10.1093/nar/15.6.2431", "1631155": "10.1073/pnas.89.14.6535",
          "2004706": "10.1093/genetics/127.2.327", "9611204": "10.1093/genetics/149.2.937"}
HITS = ({5911, 312017, 175564, 175565, 452467, 875914, 595534},
        {2242, 33003, 33004, 33005, 12453, 64091, 69527}, {2242, 69528, 69525})


def read(path=CONTEXT):
    return json.loads(path.read_bytes())


def pinned(pin):
    payload = (ROOT / pin["path"]).read_bytes()
    assert hashlib.sha256(payload).hexdigest() == pin["sha256"]
    return json.loads(payload)


def check_scope(context):
    assert context["scope"] == "RNA_LEAD_AND_TAXON_NAME_REVIEW_NOT_RESISTANCE_CURATION"
    assert context["record"]["identifier"] == "CHEBI:338412"
    assert context["record"]["standard_inchi_key"] == "YKJYKKNCCRKFSL-RDBSUJKOSA-N"
    assert context["record"]["complete_collection_aware_record_loaded"]
    assert len(context["papers"]) == len(PAPERS)
    assert {p["discovery_metadata"]["pmid"] for p in context["papers"]} == set(PAPERS)
    for paper in context["papers"]:
        metadata = paper["discovery_metadata"]
        assert metadata["doi"] == paper["doi"] == PAPERS[metadata["pmid"]]
        assert "rna" in paper["rna_class"].lower()
        assert paper["uniprot_protein_mapping"] == "NOT_APPLICABLE_TO_RNA_LOCUS"
        assert paper["curation_disposition"] == "HOLD_PRIMARY_RESULTS_AND_SUBJECT_CONTEXT"
        assert not paper["native_full_text_reviewed"]
        assert not paper["native_figures_or_tables_reviewed"] and not paper["experimental_allele_assigned"]
        for field in ("experimental_taxon_id", "experimental_strain_taxon_id", "exact_gene_locus_id",
                      "experimental_protein_accession", "experimental_genome_accession"):
            assert paper[field] is None
        assert not {"sequence", "variant", "alteration", "mic", "protein_accession"}.intersection(paper)
    lookups = context["taxonomy_lookups"]
    assert [v["source_name"] for v in lookups] == list(NAMES)
    by_name = {}
    for query, name, expected in zip(lookups, NAMES, HITS, strict=True):
        request = query["request"]
        assert request["status"] == 200 and request["release"] == "2026_03"
        assert request["pagination_complete"] and request["total_results"] == len(expected)
        url = urlsplit(request["url"])
        assert url.hostname == "rest.uniprot.org" and url.path == "/taxonomy/search"
        assert parse_qs(url.query) == {"query": ['"' + name + '"'], "format": ["json"], "size": ["50"]}
        assert query["scope"] == "NAME_SEARCH_NOT_EXPERIMENTAL_TAXON_ASSIGNMENT"
        hits = {h["taxon_id"]: h for h in query["hits"]}
        assert len(hits) == len(query["hits"]) and set(hits) == {"NCBITaxon:" + str(i) for i in expected}
        assert all(not h["experimental_subject_assigned"] for h in hits.values())
        by_name[name] = hits
    halo = by_name[NAMES[1]]["NCBITaxon:2242"]
    cuti = by_name[NAMES[2]]["NCBITaxon:2242"]
    assert NAMES[1] in halo["synonyms"] and NAMES[2] in cuti["matching_other_names"]
    assert halo["rank"] == cuti["rank"] == "species"
    contexts = context["name_reference_context"]
    assert [c["taxon_id"] for c in contexts] == ["NCBITaxon:2242", "NCBITaxon:5911"]
    assert all(not c["experimental_subject_assigned"] and c["rank"] == "species" for c in contexts)
    for row in context["do_not_collapse"]:
        hit, = [h for q in lookups for h in q["hits"] if h["taxon_id"] == row["taxon_id"]]
        assert hit["scientific_name"] == row["scientific_name"]
        assert row["source_name"] in [hit["scientific_name"], *hit["matching_other_names"]]
    assert {r["taxon_id"] for r in context["do_not_collapse"]} == {
        "NCBITaxon:69527", "NCBITaxon:69528", "NCBITaxon:69525", "NCBITaxon:12453"}
    references = context["reference_examples_not_assigned"]
    assert [(r["taxon_id"], r["rank"], r["parent_taxon_id"]) for r in references] == [
        ("NCBITaxon:312017", "strain", "NCBITaxon:5911"),
        ("NCBITaxon:64091", "no rank", "NCBITaxon:2886895")]
    for row in references:
        hit, = [h for q in lookups for h in q["hits"] if h["taxon_id"] == row["taxon_id"]]
        assert all(row[k] == hit[k] for k in row)
    limits = context["limits"]
    assert limits["records_in_scope"] == 2939 and limits["whole_corpus_status"] == "OPEN"
    assert limits["issue_1040"] == "DEFERRED"
    assert all(not v for k, v in limits.items()
               if k not in {"records_in_scope", "whole_corpus_status", "issue_1040"})
    access = context["access_limitations"]
    assert access["local_europepmc_fetch"] == "REJECTED_BY_AUTO_REVIEW_BEFORE_EXECUTION_AS_DENIED_FETCH_RETRY"
    assert access["local_europepmc_response_status"] is None
    assert not access["download_retried_after_rejection"]
    assert access["native_primary_assets_cached_this_checkpoint"] == 0


def test_research_contract_preserves_rna_and_taxonomy_boundaries():
    check_scope(read())


def test_existing_discovery_membership_not_new_experimental_evidence():
    context = read()
    discovery = pinned(context["discovery_predecessor"])
    record, = [r for r in discovery["records"] if r["identifier"] == context["record"]["identifier"]]
    assert record["standard_inchi_key"] == context["record"]["standard_inchi_key"]
    for paper in context["papers"]:
        metadata = paper["discovery_metadata"]
        assert "MED:" + metadata["pmid"] in record["candidate_ids"]
        found = [c for q in record["queries"] for c in q["candidates"] if c.get("pmid") == metadata["pmid"]]
        assert found and all(c == metadata for c in found)
    papers = {p["discovery_metadata"]["pmid"]: p for p in context["papers"]}
    assert papers["1631155"]["observation_scope"] == "EXISTING_DISCOVERY_METADATA_ONLY"
    assert "not promoted" in papers["9611204"]["interpretation"]


def test_dated_record_pin_uses_prior_receipt_not_frozen_live_record():
    context = read()
    previous = pinned(context["previous_curation"])
    item, = [r for r in previous["records"] if r["identifier"] == context["record"]["identifier"]]
    assert item["record"] == {k: context["record"][k] for k in ("path", "sha256")}


@pytest.mark.parametrize("mutation", ["protein", "experimental_taxon", "full_text", "promote_claim",
                                    "assign_hit", "erase_alias", "phage_as_species", "change_rank",
                                    "truncate_search", "ncbi_request", "complete", "new_claim"])
def test_rejects_unsupported_promotions(mutation):
    context = copy.deepcopy(read())
    if mutation == "protein":
        context["papers"][0]["experimental_protein_accession"] = "UniProtKB:P14126"
    elif mutation == "experimental_taxon":
        context["papers"][0]["experimental_taxon_id"] = "NCBITaxon:2242"
    elif mutation == "full_text":
        context["papers"][0]["native_full_text_reviewed"] = True
    elif mutation == "promote_claim":
        context["papers"][0]["curation_disposition"] = "CURATE"
    elif mutation == "assign_hit":
        context["taxonomy_lookups"][0]["hits"][0]["experimental_subject_assigned"] = True
    elif mutation == "erase_alias":
        hit, = [r for r in context["taxonomy_lookups"][2]["hits"] if r["taxon_id"] == "NCBITaxon:2242"]
        hit["matching_other_names"].remove("Halobacterium cutirubrum")
    elif mutation == "phage_as_species":
        context["name_reference_context"][0]["taxon_id"] = "NCBITaxon:12453"
    elif mutation == "change_rank":
        context["reference_examples_not_assigned"][1]["rank"] = "strain"
    elif mutation == "truncate_search":
        context["taxonomy_lookups"][0]["request"]["pagination_complete"] = False
    elif mutation == "ncbi_request":
        context["limits"]["ncbi_requests"] = 1
    elif mutation == "complete":
        context["limits"]["whole_corpus_status"] = "COMPLETE"
    else:
        context["limits"]["new_resistance_claims"] = 1
    with pytest.raises(AssertionError):
        check_scope(context)
