"""Reference candidates and abstract-only context cannot become tested resistant alleles."""

import copy
import hashlib
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_afn1252_references as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("no network in reference tests")

    monkeypatch.setattr(requests.sessions.Session, "request", forbidden)
    monkeypatch.setattr(socket.socket, "connect", forbidden)
    monkeypatch.setattr(socket, "create_connection", forbidden)


@pytest.fixture
def protein():
    accession = "Q2FZQ3"
    taxid, name, locus, version = audit.PROTEINS[accession]
    parent = {"taxonId": 1280, "scientificName": "Staphylococcus aureus", "rank": "species"}
    taxon = {
        "taxonId": taxid,
        "scientificName": name,
        "rank": "strain",
        "active": True,
        "lineage": [parent],
        "parent": parent,
    }
    entry = {
        "primaryAccession": accession,
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "entryAudit": {"entryVersion": version, "sequenceVersion": 1},
        "organism": {"taxonId": taxid, "scientificName": name},
        "genes": [{"geneName": {"value": "fabI"}, "orderedLocusNames": [{"value": locus}]}],
        "proteinDescription": {
            "recommendedName": {"fullName": {"value": "Enoyl-[acyl-carrier-protein] reductase [NADPH] FabI"}}
        },
        "references": [],
    }
    return entry, taxon


def test_reference_identity_has_no_experimental_assignment(protein):
    result = audit.project_protein(*protein)
    assert result["protein_accession"] == "UniProtKB:Q2FZQ3"
    assert result["reference_taxon_id"] == "NCBITaxon:93061"
    assert result["reference_species_taxon_id"] == "NCBITaxon:1280"
    assert result["experimental_subject_assignment"] is False
    assert result["exact_resistance_allele"] is False
    assert result["experimental_genome_assignment"] is False
    assert result["compound_specific_resistance_verified"] is False
    assert result["other_drug_annotation_transferred"] is False
    assert result["selected_paper_bibliography_matches"] == []
    assert "bibliography" not in result


@pytest.mark.parametrize(
    "change",
    [
        "accession",
        "unreviewed",
        "entry_version",
        "sequence_version",
        "gene",
        "locus",
        "name",
        "protein_taxid",
        "protein_taxname",
        "taxid",
        "taxname",
        "rank",
        "inactive",
        "species",
        "duplicate_species",
        "parent",
        "sequence",
        "features",
        "comments",
        "selected_citation",
    ],
)
def test_reference_identity_guards(protein, change):
    entry, taxon = protein
    if change == "accession":
        entry["primaryAccession"] = "OTHER"
    elif change == "unreviewed":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif change == "entry_version":
        entry["entryAudit"]["entryVersion"] += 1
    elif change == "sequence_version":
        entry["entryAudit"]["sequenceVersion"] = 2
    elif change == "gene":
        entry["genes"][0]["geneName"]["value"] = "other"
    elif change == "locus":
        entry["genes"][0]["orderedLocusNames"] = []
    elif change == "name":
        entry["proteinDescription"]["recommendedName"]["fullName"]["value"] = "other"
    elif change == "protein_taxid":
        entry["organism"]["taxonId"] = 1280
    elif change == "protein_taxname":
        entry["organism"]["scientificName"] = "other"
    elif change == "taxid":
        taxon["taxonId"] = 1281
    elif change == "taxname":
        taxon["scientificName"] = "other"
    elif change == "rank":
        taxon["rank"] = "no rank"
    elif change == "inactive":
        taxon["active"] = False
    elif change == "species":
        taxon["lineage"][0]["scientificName"] = "other"
    elif change == "duplicate_species":
        taxon["lineage"].append(copy.deepcopy(taxon["lineage"][0]))
    elif change == "parent":
        taxon["parent"] = {"taxonId": 1, "scientificName": "different"}
    elif change in {"sequence", "features", "comments"}:
        entry[change] = []
    else:
        entry["references"] = [
            {
                "citation": {
                    "publicationDate": "2013",
                    "citationCrossReferences": [{"database": "PubMed", "id": "24189061"}],
                }
            }
        ]
    with pytest.raises(ValueError):
        audit.project_protein(*protein)


@pytest.fixture
def metadata(monkeypatch):
    abstract = "Synthetic FabI gene context, not a reviewed primary experiment."
    checksum = hashlib.sha256(abstract.encode()).hexdigest()
    monkeypatch.setattr(audit, "LEADS", {k: (*v[:3], checksum) for k, v in audit.LEADS.items()})
    leads = {
        k: {
            "id": k,
            "pmid": k,
            "source": "MED",
            "doi": v[0],
            "pmcid": v[1],
            "pubYear": v[2],
            "title": "Synthetic citation " + k,
        }
        for k, v in audit.LEADS.items()
    }
    payload = {
        "hitCount": 2,
        "request": {"queryString": audit.METADATA_QUERY, "resultType": "core", "pageSize": 2},
        "resultList": {"result": [{**v, "abstractText": abstract} for v in leads.values()]},
    }
    return payload, leads


def test_abstract_scope_and_access_holds_remain_explicit(metadata):
    papers = audit.metadata_context(*metadata)
    assert set(papers) == {"22948878", "24189061"}
    for paper in papers.values():
        assert paper["evidence_scope"] == "INDEXED_ABSTRACT_ONLY_NOT_PRIMARY_RESULTS_REVIEW"
        assert paper["primary_results_figures_supplements_reviewed"] is False
        assert paper["exact_tested_chemical_structure_or_form_verified"] is False
        assert paper["experimental_allele_strain_or_genome_assignment"] is None
        assert paper["raw_abstract_variants_numeric_AST_or_protocols_exported"] is False
        assert "abstractText" not in paper


@pytest.mark.parametrize(
    "change",
    [
        "count",
        "boolean_count",
        "cursor",
        "duplicate",
        "query",
        "type",
        "size",
        "id",
        "doi",
        "pmcid",
        "year",
        "title",
        "abstract",
        "missing_abstract",
    ],
)
def test_metadata_identity_completeness_and_body_guards(metadata, change):
    payload, _ = metadata
    row = payload["resultList"]["result"][0]
    if change == "count":
        payload["hitCount"] = 3
    elif change == "boolean_count":
        payload["hitCount"] = True
    elif change == "cursor":
        payload["nextCursorMark"] = "next"
    elif change == "duplicate":
        payload["resultList"]["result"][1] = copy.deepcopy(row)
    elif change in {"query", "type", "size"}:
        payload["request"][{"query": "queryString", "type": "resultType", "size": "pageSize"}[change]] = (
            "wrong"
        )
    elif change == "missing_abstract":
        del row["abstractText"]
    else:
        row[{"year": "pubYear", "abstract": "abstractText"}.get(change, change)] = "changed"
    with pytest.raises(ValueError):
        audit.metadata_context(*metadata)


@pytest.fixture
def discovery():
    data = json.loads((ROOT / "research/2026-10-08-resistance-alias-discovery-candidates.json").read_bytes())
    return next(row for row in data["records"] if row["identifier"] == audit.IDENTIFIER)


def test_discovery_binds_both_completed_queries(discovery):
    assert set(audit.discovery_context(discovery)) == set(audit.LEADS)


@pytest.mark.parametrize(
    "change",
    [
        "record",
        "structure",
        "existing_claim",
        "candidate_union",
        "query_count",
        "cursor",
        "hit_count",
        "status",
        "citation",
        "duplicate",
    ],
)
def test_discovery_scope_guards(discovery, change):
    query = discovery["queries"][0]
    if change in {"record", "structure", "existing_claim", "candidate_union"}:
        discovery[
            {
                "record": "identifier",
                "structure": "standard_inchi_key",
                "existing_claim": "has_existing_resistance_evidence",
                "candidate_union": "candidate_ids",
            }[change]
        ] = "wrong"
    elif change == "query_count":
        discovery["queries"].pop()
    elif change == "cursor":
        query["next_cursor"] = "next"
    elif change == "hit_count":
        query["hit_count"] = 3
    elif change == "status":
        query["request"]["status"] = 500
    elif change == "citation":
        query["candidates"][0]["doi"] = "different"
    else:
        query["candidates"][1] = copy.deepcopy(query["candidates"][0])
    with pytest.raises(ValueError):
        audit.discovery_context(discovery)


def test_locator_success_is_not_primary_access():
    receipt = {"status": 302, "headers": {"Location": audit.PUBLISHERS["publisher-2013"][1]}}
    locator = '<input id="redirectURL" value="https%3A%2F%2Fjbc.org%2Fretrieve%2Fpii%2FS0021925820553234">'
    result = audit.publisher_chain(receipt, locator)
    assert result["primary_full_text_obtained"] is False
    assert result["publisher_locator"] == "HTTP_200_LOCATOR_NOT_PRIMARY_ARTICLE"
    for invalid in (locator.replace("jbc.org", "example.org"), locator + locator, "<p>No destination</p>"):
        with pytest.raises(ValueError):
            audit.publisher_chain(receipt, invalid)
    receipt["headers"]["Location"] = "https://example.org/"
    with pytest.raises(ValueError):
        audit.publisher_chain(receipt, locator)


@pytest.mark.parametrize("change", ["total", "link", "release", "missing_results", "extra_result"])
def test_empty_citation_query_is_complete_not_protein_absence(change):
    payload = {"results": []}
    headers = {"X-Total-Results": "0", "X-UniProt-Release": "2026_03"}
    assert audit.complete_query(payload, headers, 0) == []
    if change == "total":
        headers["X-Total-Results"] = "1"
    elif change == "link":
        headers["Link"] = "next"
    elif change == "release":
        headers["X-UniProt-Release"] = "different"
    elif change == "missing_results":
        payload = {}
    else:
        payload["results"] = [{}]
    with pytest.raises(ValueError):
        audit.complete_query(payload, headers, 0)


def test_public_checkpoint_retains_all_limits_without_private_cache():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert result["identifier"] == audit.IDENTIFIER and result["standard_inchi_key"] == audit.INCHIKEY
    assert set(result["reference_proteins"]) == set(audit.PROTEINS)
    for accession, protein in result["reference_proteins"].items():
        taxid, organism, locus, version = audit.PROTEINS[accession]
        assert protein["reference_taxon_id"] == f"NCBITaxon:{taxid}"
        assert protein["reference_species_taxon_id"] == "NCBITaxon:1280"
        assert protein["reference_organism_name"] == organism
        assert protein["ordered_locus_names"] == [locus]
        assert protein["entry_version"] == version and protein["sequence_version"] == 1
        assert protein["exact_resistance_allele"] is protein["experimental_subject_assignment"] is False
        assert protein["selected_paper_bibliography_matches"] == []
    assert result["limits"]["native_http_attempts"] == 8
    assert result["limits"]["native_http_status_counts"] == {"200": 5, "302": 1, "403": 2}
    assert result["limits"]["reused_taxonomy_responses"] == 3
    assert result["limits"]["ncbi_requests"] == result["limits"]["biological_record_changes"] == 0
    assert (
        result["limits"]["whole_record_signoffs"] == 0
        and result["limits"]["full_corpus_goal_status"] == "OPEN"
    )
    assert result["publisher_chain_2013"]["primary_full_text_obtained"] is False
    assert result["curation"]["exact_resistance_allele_assignment"] is False
