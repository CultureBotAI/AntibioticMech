"""Induction citations must not silently become resistance or subject assignments."""

import copy
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_ciclopirox_context as audit  # noqa: E402


def leads():
    return {
        pmid: {
            "id": pmid,
            "pmid": pmid,
            "source": "MED",
            "doi": doi,
            "pmcid": pmcid,
            "title": "Selected study " + pmid,
            "pubYear": "2003" if pmid == "12760852" else "2005",
        }
        for pmid, (doi, pmcid) in audit.LEADS.items()
    }


def taxonomy():
    return {
        "taxonId": 237561,
        "scientificName": audit.TAXON_NAME,
        "rank": "strain",
        "active": True,
        "lineage": [{"taxonId": 5476, "scientificName": "Candida albicans", "rank": "species"}],
    }


def entry(accession):
    gene, version, seqversion, names, locus, orfs, protein, pmids = audit.PROTEINS[accession]
    return {
        "primaryAccession": accession,
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "entryAudit": {"entryVersion": version, "sequenceVersion": seqversion},
        "organism": {"taxonId": 237561, "scientificName": audit.TAXON_NAME},
        "proteinDescription": {"recommendedName": {"fullName": {"value": protein}}},
        "genes": [
            {
                "geneName": {"value": gene},
                "synonyms": [{"value": n} for n in names if n != gene],
                "orderedLocusNames": [{"value": locus}],
                "orfNames": [{"value": n} for n in orfs],
            }
        ],
        "references": [
            {
                "citation": {
                    "id": pmid,
                    "citationType": "journal article",
                    "title": leads()[pmid]["title"],
                    "publicationDate": leads()[pmid]["pubYear"],
                    "citationCrossReferences": [
                        {"database": "PubMed", "id": pmid},
                        {"database": "DOI", "id": audit.LEADS[pmid][0]},
                    ],
                },
                "referencePositions": ["INDUCTION"],
            }
            for pmid in sorted(pmids)
        ],
    }


@pytest.fixture(params=sorted(audit.PROTEINS))
def example(request):
    return entry(request.param), taxonomy()


def test_reference_is_not_an_experimental_identity(example):
    protein, taxon = example
    result = audit.project_reference(protein, taxon, leads())
    assert result["reference_taxon_id"] == "NCBITaxon:237561"
    assert result["reference_taxon_rank"] == "strain"
    assert result["reference_species_taxon_id"] == "NCBITaxon:5476"
    assert result["experimental_subject_assignment"] is False
    assert result["exact_resistance_allele"] is False
    assert result["compound_specific_resistance_verified"] is False
    assert result["experimental_genome_assignment"] is None
    assert result["database_review_status_is_primary_review"] is False
    assert all(c["database_reference_scope"] == "INDUCTION" for c in result["selected_citations"])
    assert "source_species_taxon_id" not in result


def test_unselected_annotation_text_is_not_exported(example):
    protein, taxon = example
    protein["references"].append(
        {
            "citation": {"citationCrossReferences": [{"database": "PubMed", "id": "1"}]},
            "referencePositions": ["PRIVATE_OPERATIONAL_CONTEXT"],
            "referenceComments": [{"value": "PRIVATE_EXPERIMENTAL_DETAILS"}],
        }
    )
    assert "PRIVATE_" not in json.dumps(audit.project_reference(protein, taxon, leads()))


@pytest.mark.parametrize(
    "change",
    [
        "accession",
        "review",
        "version",
        "boolean_version",
        "sequence_version",
        "primary_gene",
        "synonym",
        "duplicate_gene",
        "locus",
        "orf",
        "organism_id",
        "organism_name",
        "active",
        "rank",
        "species_id",
        "species_name",
        "duplicate_species",
        "sequence",
        "features",
        "comments",
        "citation_doi",
        "citation_pmid",
        "citation_title",
        "citation_year",
        "citation_type",
        "citation_scope",
        "citation_comment",
        "citation_duplicate",
        "split_identifiers",
    ],
)
def test_reference_and_citation_guards(example, change):
    protein, taxon = example
    item = protein["references"][0]
    citation = item["citation"]
    if change == "accession":
        protein["primaryAccession"] = "P00001"
    elif change == "review":
        protein["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif change in {"version", "boolean_version", "sequence_version"}:
        protein["entryAudit"]["sequenceVersion" if change == "sequence_version" else "entryVersion"] = (
            True if change == "boolean_version" else 999
        )
    elif change == "primary_gene":
        protein["genes"][0]["synonyms"].append(protein["genes"][0]["geneName"])
        protein["genes"][0]["geneName"] = {"value": "OTHER"}
    elif change == "synonym":
        protein["genes"][0]["synonyms"].append({"value": "OTHER"})
    elif change == "duplicate_gene":
        protein["genes"].append(copy.deepcopy(protein["genes"][0]))
    elif change in {"locus", "orf"}:
        protein["genes"][0]["orderedLocusNames" if change == "locus" else "orfNames"][0]["value"] = "OTHER"
    elif change in {"organism_id", "organism_name"}:
        protein["organism"]["taxonId" if change == "organism_id" else "scientificName"] = (
            5476 if change == "organism_id" else "OTHER"
        )
    elif change == "active":
        taxon["active"] = False
    elif change == "rank":
        taxon["rank"] = "species"
    elif change in {"species_id", "species_name"}:
        taxon["lineage"][0]["taxonId" if change == "species_id" else "scientificName"] = (
            4932 if change == "species_id" else "OTHER"
        )
    elif change == "duplicate_species":
        taxon["lineage"].append(copy.deepcopy(taxon["lineage"][0]))
    elif change in {"sequence", "features", "comments"}:
        protein[change] = []
    elif change in {"citation_doi", "citation_pmid"}:
        citation["citationCrossReferences"][1 if change == "citation_doi" else 0]["id"] = "OTHER"
    elif change in {"citation_title", "citation_year", "citation_type"}:
        citation[
            {"citation_title": "title", "citation_year": "publicationDate", "citation_type": "citationType"}[
                change
            ]
        ] = "OTHER"
    elif change == "citation_scope":
        item["referencePositions"] = ["FUNCTION"]
    elif change == "citation_comment":
        item["referenceComments"] = [{"value": "UNREVIEWED_CONTEXT"}]
    elif change == "citation_duplicate":
        protein["references"].append(copy.deepcopy(item))
    elif change == "split_identifiers":
        doi = citation["citationCrossReferences"].pop()
        protein["references"].append({"citation": {"citationCrossReferences": [doi]}})
    with pytest.raises(ValueError):
        audit.project_reference(protein, taxon, leads())


def query_inputs():
    payloads, headers = {}, {}
    for key, (_, _, expected) in audit.QUERIES.items():
        payloads[key] = {"results": [entry(accession) for accession in sorted(expected)]}
        headers[key] = {"X-Total-Results": str(len(expected)), "X-UniProt-Release": "2026_03"}
    return payloads, headers


def test_query_deduplication_and_order_independence():
    payloads, headers = query_inputs()
    expected = audit.project_queries(payloads, headers, taxonomy(), leads())
    assert expected["query_result_memberships"] == 6
    assert expected["distinct_reference_proteins"] == 5
    assert expected["repeated_accessions_are_independent_proteins_or_experiments"] is False
    for payload in payloads.values():
        payload["results"].reverse()
    assert audit.project_queries(payloads, headers, taxonomy(), leads()) == expected


@pytest.mark.parametrize(
    "change", ["missing", "extra", "duplicate", "total", "pagination", "release", "inconsistent"]
)
def test_query_completeness_and_duplicate_identity(change):
    payloads, headers = query_inputs()
    key = "reference-2005-oxygen"
    if change == "missing":
        payloads[key]["results"].pop()
    elif change == "extra":
        payloads[key]["results"].append(entry("Q59UT4"))
    elif change == "duplicate":
        payloads[key]["results"][1] = copy.deepcopy(payloads[key]["results"][0])
    elif change in {"total", "pagination", "release"}:
        headers[key][
            {"total": "X-Total-Results", "pagination": "Link", "release": "X-UniProt-Release"}[change]
        ] = "OTHER"
    elif change == "inconsistent":
        payloads["reference-2003"]["results"][0]["entryAudit"]["entryVersion"] += 1
    with pytest.raises(ValueError):
        audit.project_queries(payloads, headers, taxonomy(), leads())


def discovery_inputs():
    sources = []
    for counts in ({"CHEBI:31398": 15, "CHEBI:453011": 34}, {"CHEBI:31398": 28, "CHEBI:453011": 81}):
        rows = []
        for identifier, count in counts.items():
            candidates = list(leads().values()) + [{"source": "MED", "id": str(i)} for i in range(count - 3)]
            queries = [
                {
                    "candidates": candidates,
                    "hit_count": count,
                    "next_cursor": None,
                    "request": {"status": 200},
                }
            ]
            queries += [
                {"candidates": [], "hit_count": 0, "next_cursor": None, "request": {"status": 200}}
                for _ in range(3 if identifier == "CHEBI:31398" else 1)
            ]
            rows.append(
                {
                    "identifier": identifier,
                    "candidate_ids": ["MED:" + c["id"] for c in candidates],
                    "queries": queries,
                }
            )
        sources.append({"input": {"path": "synthetic"}, "records": rows})
    return sources


def test_discovery_preserves_both_compounds_and_unreviewed_candidates():
    result = audit.discovery_context(discovery_inputs())
    assert len(result["checkpoints"]) == 2
    assert result["all_candidates_primary_reviewed"] is False
    assert set(result["selected_leads"]) == set(audit.LEADS)


@pytest.mark.parametrize(
    "change",
    [
        "source",
        "record",
        "identifier",
        "ids",
        "candidate",
        "count",
        "boolean_count",
        "cursor",
        "status",
        "doi",
        "pmcid",
        "union",
    ],
)
def test_discovery_does_not_overstate_complete_queries(change):
    sources = discovery_inputs()
    row = sources[0]["records"][0]
    query = row["queries"][0]
    if change == "source":
        sources.pop()
    elif change == "record":
        sources[0]["records"].pop()
    elif change == "identifier":
        row["identifier"] = "OTHER"
    elif change == "ids":
        row["candidate_ids"][0] = row["candidate_ids"][1]
    elif change == "candidate":
        query["candidates"][0] = copy.deepcopy(query["candidates"][1])
    elif change in {"count", "boolean_count"}:
        query["hit_count"] = True if change == "boolean_count" else 999
    elif change == "cursor":
        query["next_cursor"] = "NEXT"
    elif change == "status":
        query["request"]["status"] = 500
    elif change in {"doi", "pmcid"}:
        query["candidates"][0][change] = "OTHER"
    elif change == "union":
        row["candidate_ids"][0] = "MED:OTHER"
    with pytest.raises(ValueError):
        audit.discovery_context(sources)


def test_unknown_request_is_rejected_before_replay(tmp_path):
    directory = tmp_path / audit.CACHE
    directory.mkdir(parents=True)
    (directory / "unplanned-attempt.json").write_text("{}")
    with pytest.raises(ValueError, match="request inventory"):
        audit.build(tmp_path)


def test_native_checkpoint_replays_without_network(monkeypatch):
    if not (ROOT / audit.CACHE / "cohort.json").is_file():
        pytest.skip("private native research cache is unavailable")

    def forbidden(*args, **kwargs):
        raise AssertionError("network is forbidden during native replay")

    monkeypatch.setattr(requests.sessions.Session, "request", forbidden)
    monkeypatch.setattr(socket.socket, "connect", forbidden)
    monkeypatch.setattr(socket, "create_connection", forbidden)
    result = audit.build(ROOT)
    assert result == json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert result["corpus_records_hash_checked_at_preflight"] == 2939
    assert result["limits"]["http_status_counts"] == {"200": 3, "500": 1}
    assert result["limits"]["biological_records_changed"] == 0
    assert result["limits"]["primary_results_reviews"] == 0
    assert result["limits"]["ncbi_requests"] == 0
    assert result["chemical_scope"]["neutral_and_olamine_records_kept_distinct"] is True
