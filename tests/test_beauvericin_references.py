"""Reference metadata must not become primary evidence or experimental alleles."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_beauvericin_references as audit  # noqa: E402


@pytest.fixture(params=list(audit.PROTEINS))
def reference(request):
    accession = request.param
    gene, reviewed, version, loci, name = audit.PROTEINS[accession]
    description = (
        {"recommendedName": {"fullName": {"value": name}}}
        if reviewed
        else {
            "submissionNames": [{"fullName": {"value": name}}],
        }
    )
    taxon = {
        "taxonId": 237561,
        "scientificName": audit.TAXON_NAME,
        "rank": "strain",
        "active": True,
        "lineage": [{"taxonId": 5476, "scientificName": "Candida albicans", "rank": "species"}],
    }
    entry = {
        "primaryAccession": accession,
        "entryType": "UniProtKB reviewed (Swiss-Prot)" if reviewed else "UniProtKB unreviewed (TrEMBL)",
        "entryAudit": {"entryVersion": version, "sequenceVersion": 1},
        "organism": {"taxonId": 237561, "scientificName": audit.TAXON_NAME},
        "proteinDescription": description,
        "genes": [{"geneName": {"value": gene}, "orderedLocusNames": [{"value": x} for x in loci]}],
        "references": [
            {
                "citation": {
                    "citationCrossReferences": [
                        {"database": "PubMed", "id": "27736764" if reviewed else "15123810"}
                    ]
                },
                "referencePositions": ["PRIVATE_OPERATIONAL_CONTEXT"],
            }
        ],
    }
    return entry, taxon


def test_versioned_reference_scope_is_explicit(reference):
    entry, taxon = reference
    result = audit.project_reference(entry, taxon)
    reviewed = audit.PROTEINS[entry["primaryAccession"]][1]
    assert result["protein_accession"] == "UniProtKB:" + entry["primaryAccession"]
    assert result["reference_taxon_id"] == "NCBITaxon:237561"
    assert result["reference_species_taxon_id"] == "NCBITaxon:5476"
    assert result["reference_taxon_rank"] == "strain"
    assert result["exact_resistance_allele"] is False
    assert result["experimental_subject_assignment"] is False
    assert result["experimental_role_or_resistance_allele_established"] is False
    assert result["database_review_status_is_primary_results_review"] is False
    assert result["selected_publication_citations"] == (["PMID:27736764"] if reviewed else [])
    assert result["discovery_basis"] == (
        "PUBLICATION_CITATION" if reviewed else "TITLE_GENE_NAME_AND_SPECIES"
    )
    if not reviewed:
        assert result["annotation_status"] == "UNREVIEWED_EXPERIMENTAL_IDENTITY_NOT_ESTABLISHED_BY_THIS_AUDIT"
        assert result["unflagged_means_complete"] is False
    assert "PRIVATE_OPERATIONAL_CONTEXT" not in json.dumps(result)
    assert "source_species_taxon_id" not in result


@pytest.mark.parametrize(
    "change",
    [
        "accession",
        "review_status",
        "version",
        "boolean_version",
        "sequence_version",
        "gene",
        "locus",
        "sequence",
        "features",
        "comments",
        "organism_id",
        "organism_name",
        "citation",
        "protein_name",
    ],
)
def test_reference_identity_review_status_and_scope_guards(reference, change):
    entry, taxon = reference
    if change == "accession":
        entry["primaryAccession"] = "OTHER"
    elif change == "review_status":
        entry["entryType"] = "OTHER"
    elif change in {"version", "boolean_version", "sequence_version"}:
        entry["entryAudit"]["sequenceVersion" if change == "sequence_version" else "entryVersion"] = (
            True if change == "boolean_version" else 999
        )
    elif change == "gene":
        entry["genes"][0]["geneName"]["value"] = "OTHER"
    elif change == "locus":
        entry["genes"][0]["orderedLocusNames"].pop()
    elif change in {"sequence", "features", "comments"}:
        entry[change] = []
    elif change in {"organism_id", "organism_name"}:
        entry["organism"]["taxonId" if change == "organism_id" else "scientificName"] = "OTHER"
    elif change == "citation":
        entry["references"][0]["citation"]["citationCrossReferences"][0]["id"] = "30249688"
    else:
        description = entry["proteinDescription"]
        name = (
            description["recommendedName"]
            if "recommendedName" in description
            else description["submissionNames"][0]
        )
        name["fullName"]["value"] = "OTHER"
    with pytest.raises(ValueError):
        audit.project_reference(entry, taxon)


@pytest.mark.parametrize("change", ["id", "rank", "name", "inactive", "species", "duplicate_species"])
def test_taxonomy_does_not_substitute_a_different_strain_or_species(reference, change):
    entry, taxon = reference
    if change == "id":
        taxon["taxonId"] = 559292
    elif change == "rank":
        taxon["rank"] = "species"
    elif change == "name":
        taxon["scientificName"] = "OTHER"
    elif change == "inactive":
        taxon["active"] = False
    elif change == "species":
        taxon["lineage"][0]["taxonId"] = 4932
    else:
        taxon["lineage"].append(copy.deepcopy(taxon["lineage"][0]))
    with pytest.raises(ValueError):
        audit.project_reference(entry, taxon)


@pytest.mark.parametrize("count", [0, 1, 2])
@pytest.mark.parametrize("change", ["none", "null", "wrong_count", "header", "release", "pagination"])
def test_complete_queries_include_scoped_empty_results(count, change):
    payload = {"results": [{} for _ in range(count)]}
    headers = {"X-Total-Results": str(count), "X-UniProt-Release": "2026_03"}
    if change == "none":
        assert audit.complete_query(payload, headers, count) == payload["results"]
        return
    if change == "null":
        payload["results"] = None
    elif change == "wrong_count":
        payload["results"].append({})
    elif change == "header":
        headers["X-Total-Results"] = "OTHER"
    elif change == "release":
        headers["X-UniProt-Release"] = "OTHER"
    else:
        headers["Link"] = "next"
    with pytest.raises(ValueError):
        audit.complete_query(payload, headers, count)


@pytest.fixture
def discovery():
    entries = [
        {"id": pmid, "source": "MED", "pmid": pmid, "doi": doi, "pmcid": pmcid}
        for pmid, (doi, pmcid) in audit.LEADS.items()
    ]
    entries.extend({"id": str(900000 + i), "source": "MED"} for i in range(55))
    query = {"hit_count": 58, "next_cursor": None, "request": {"status": 200}, "candidates": entries}
    return {
        "identifier": "CHEBI:3000",
        "candidate_ids": ["MED:" + e["id"] for e in entries],
        "queries": [query, copy.deepcopy(query)],
    }


def test_failed_primary_request_does_not_complete_discovery(discovery):
    result = audit.discovery_context(discovery)
    assert result["candidate_identities"] == result["primary_results_unreviewed_candidates"] == 58
    assert result["primary_candidates_not_requested_this_pass"] == 57
    assert result["primary_results_reviews"] == 0
    assert result["duplicate_query_memberships_are_independent_evidence"] is False
    assert result["selected_leads"]["27736764"]["primary_review_status"] == "TECHNICAL_HTTP_500_HOLD"
    assert (
        result["selected_leads"]["30249688"]["primary_review_status"]
        == "UNREQUESTED_AFTER_PRIMARY_CANARY_ERROR"
    )


@pytest.mark.parametrize(
    "change",
    [
        "record",
        "duplicate_id",
        "query_count",
        "hit_count",
        "cursor",
        "failed",
        "member",
        "metadata",
        "citation",
    ],
)
def test_discovery_membership_and_selected_identity_guards(discovery, change):
    if change == "record":
        discovery["identifier"] = "OTHER"
    elif change == "duplicate_id":
        discovery["candidate_ids"][-1] = discovery["candidate_ids"][0]
    elif change == "query_count":
        discovery["queries"].pop()
    else:
        query = discovery["queries"][0]
        if change == "hit_count":
            query["hit_count"] = 59
        elif change == "cursor":
            query["next_cursor"] = "more"
        elif change == "failed":
            query["request"]["status"] = 500
        elif change == "member":
            query["candidates"].pop()
        elif change == "metadata":
            query["candidates"][0]["title"] = "Different"
        else:
            for query in discovery["queries"]:
                query["candidates"][0]["doi"] = "OTHER"
    with pytest.raises(ValueError):
        audit.discovery_context(discovery)


@pytest.mark.parametrize("change", ["missing_receipt", "missing_attempt", "unresolved_attempt"])
def test_request_coverage_fails_closed(tmp_path, change):
    directory = tmp_path / "cache"
    directory.mkdir()
    for key in {"article-2016"} | set(audit.QUERIES):
        for suffix in ("receipt", "attempt"):
            (directory / f"{key}-{suffix}.json").touch()
    if change == "unresolved_attempt":
        (directory / "unreported-attempt.json").touch()
    else:
        (directory / f"article-2016-{change.removeprefix('missing_')}.json").unlink()
    with pytest.raises(ValueError, match="research request coverage"):
        audit.build(tmp_path, Path("cache"))


def test_public_checkpoint_keeps_review_status_and_primary_hold_visible():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert result["query_interpretation"]["complete_result_counts"] == {
        "reference-2016": 1,
        "reference-2018": 0,
        "reference-names": 0,
        "reference-inclusive": 2,
    }
    assert len(result["reference_proteins"]) == 3
    assert (
        result["query_interpretation"]["empty_citation_or_reviewed_query_establishes_gene_absence"] is False
    )
    assert result["limits"]["primary_results_reviews"] == 0
    assert result["limits"]["primary_2016_disposition"] == "TECHNICAL_HTTP_500_HOLD"
    assert result["limits"]["primary_2018_and_other_2016_study_requested"] is False
    assert result["limits"]["ncbi_requests"] == 0
    assert result["limits"]["issue_1040"] == "DEFERRED"
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"


def test_cache_replay_is_offline_and_does_not_read_live_records(monkeypatch):
    if not (ROOT / audit.CACHE / "reference-inclusive-receipt.json").exists():
        pytest.skip("private source cache is not distributed")

    def denied(*args, **kwargs):
        raise AssertionError("offline replay attempted networking")

    original_open = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.resolve().is_relative_to(ROOT / "data/antibiotics")
        return original_open(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    assert audit.build(ROOT) == json.loads((ROOT / audit.OUTPUT).read_bytes())


@pytest.mark.parametrize(
    "change",
    ["cohort", "hold", "primary_review", "canary", "citation_query", "reviewed_query", "species_scope"],
)
def test_cached_hold_and_followup_provenance_guards(monkeypatch, change):
    if not (ROOT / audit.CACHE / "reference-inclusive-receipt.json").exists():
        pytest.skip("private source cache is not distributed")
    original_loads = json.loads

    def altered(payload, *args, **kwargs):
        value = original_loads(payload, *args, **kwargs)
        if not isinstance(value, dict):
            return value
        if (
            change == "primary_review"
            and "local_XML_inspection_of_error_body_failed_without_any_primary_content" in value
        ):
            value["primary_results_reviewed"] = True
        elif "requests" in value:
            field = {
                "cohort": "cohort",
                "hold": "primary_access_hold",
                "canary": "canary_review",
                "citation_query": "completed_citation_query",
                "reviewed_query": "completed_reviewed_only_query",
                "species_scope": "prior_other_species_YOR1_queries_not_retried_or_substituted",
            }.get(change)
            if field in value:
                value[field] = False if change == "species_scope" else {}
        return value

    monkeypatch.setattr(json, "loads", altered)
    with pytest.raises(ValueError):
        audit.build(ROOT)
