"""Historical CRY names do not identify interchangeable proteins or tested alleles."""

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
import audit_cryptopleurine_references as audit  # noqa: E402


def leads():
    return {
        pmid: {
            "id": pmid,
            "pmid": pmid,
            "source": "MED",
            "doi": doi,
            "pmcid": pmcid,
            "pubYear": year,
            "title": "Selected paper " + pmid,
        }
        for pmid, (doi, pmcid, year) in audit.LEADS.items()
    }


def taxonomy():
    species = {"taxonId": 4932, "scientificName": "Saccharomyces cerevisiae", "rank": "species"}
    return {
        "taxonId": 559292,
        "scientificName": audit.TAXON_NAME,
        "rank": "strain",
        "active": True,
        "parent": copy.deepcopy(species),
        "lineage": [species],
    }


def entry(accession):
    gene, _, names, locus, orf, version, seqversion, protein, alternatives, pmid = audit.PROTEINS[accession]
    return {
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "primaryAccession": accession,
        "entryAudit": {"entryVersion": version, "sequenceVersion": seqversion},
        "organism": {"taxonId": 559292, "scientificName": audit.TAXON_NAME},
        "genes": [
            {
                "geneName": {"value": gene},
                "synonyms": [{"value": n} for n in names if n != gene],
                "orderedLocusNames": [{"value": locus}],
                "orfNames": [{"value": orf}],
            }
        ],
        "proteinDescription": {
            "recommendedName": {"fullName": {"value": protein}},
            "alternativeNames": [{"fullName": {"value": n}} for n in alternatives],
        },
        "references": [
            {
                "citation": {
                    "id": pmid,
                    "citationType": "journal article",
                    "title": leads()[pmid]["title"],
                    "publicationDate": audit.LEADS[pmid][2],
                    "citationCrossReferences": [
                        {"database": "PubMed", "id": pmid},
                        {"database": "DOI", "id": audit.LEADS[pmid][0]},
                    ],
                },
                "referencePositions": ["NUCLEOTIDE SEQUENCE [GENOMIC DNA]"],
            }
        ],
    }


@pytest.fixture(params=sorted(audit.PROTEINS))
def protein(request):
    return entry(request.param)


def test_reference_is_not_a_tested_allele(protein):
    result = audit.project_protein(protein, taxonomy(), leads())
    assert result["reference_taxon_id"] == "NCBITaxon:559292"
    assert result["reference_species_taxon_id"] == "NCBITaxon:4932"
    assert result["source_gene_alias"] in {"CRY1", "CRY2"}
    assert result["exact_resistance_allele"] is False
    assert result["experimental_subject_assignment"] is False
    assert result["compound_specific_resistance_verified"] is False
    assert result["experimental_genome_assignment"] is None
    assert "bibliography" not in result


def test_unselected_reference_details_are_not_exported(protein):
    protein["references"].append(
        {
            "citation": {"citationCrossReferences": [{"database": "PubMed", "id": "1"}]},
            "referencePositions": ["PRIVATE_DETAILS"],
            "referenceComments": ["PRIVATE_DETAILS"],
        }
    )
    assert "PRIVATE_" not in json.dumps(audit.project_protein(protein, taxonomy(), leads()))


@pytest.mark.parametrize(
    "change",
    [
        "accession",
        "review",
        "version",
        "sequence_version",
        "boolean_version",
        "primary_gene",
        "alias",
        "locus",
        "orf",
        "protein_name",
        "alternative_name",
        "duplicate_gene",
        "taxon_id",
        "taxon_name",
        "active",
        "rank",
        "species",
        "duplicate_species",
        "sequence",
        "features",
        "comments",
        "citation_doi",
        "citation_pmid",
        "citation_title",
        "citation_year",
        "citation_scope",
        "citation_comment",
        "duplicate_citation",
        "split_identifiers",
    ],
)
def test_reference_identity_guards(protein, change):
    taxon = taxonomy()
    item = protein["references"][0]
    citation = item["citation"]
    if change == "accession":
        protein["primaryAccession"] = "P00001"
    elif change == "review":
        protein["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif change in {"version", "sequence_version", "boolean_version"}:
        protein["entryAudit"]["sequenceVersion" if change == "sequence_version" else "entryVersion"] = (
            True if change == "boolean_version" else 999
        )
    elif change == "primary_gene":
        protein["genes"][0]["geneName"]["value"] = "OTHER"
    elif change in {"alias", "locus", "orf"}:
        protein["genes"][0][{"alias": "synonyms", "locus": "orderedLocusNames", "orf": "orfNames"}[change]][
            0
        ]["value"] = "OTHER"
    elif change == "protein_name":
        protein["proteinDescription"]["recommendedName"]["fullName"]["value"] = "OTHER"
    elif change == "alternative_name":
        protein["proteinDescription"]["alternativeNames"][0]["fullName"]["value"] = "OTHER"
    elif change == "duplicate_gene":
        protein["genes"].append(copy.deepcopy(protein["genes"][0]))
    elif change in {"taxon_id", "taxon_name"}:
        protein["organism"]["taxonId" if change == "taxon_id" else "scientificName"] = "OTHER"
    elif change == "active":
        taxon["active"] = False
    elif change == "rank":
        taxon["rank"] = "species"
    elif change == "species":
        taxon["lineage"][0]["taxonId"] = 999
    elif change == "duplicate_species":
        taxon["lineage"].append(copy.deepcopy(taxon["lineage"][0]))
    elif change in {"sequence", "features", "comments"}:
        protein[change] = []
    elif change in {"citation_doi", "citation_pmid"}:
        citation["citationCrossReferences"][1 if change == "citation_doi" else 0]["id"] = "OTHER"
    elif change in {"citation_title", "citation_year"}:
        citation["title" if change == "citation_title" else "publicationDate"] = "OTHER"
    elif change == "citation_scope":
        item["referencePositions"] = ["FUNCTION"]
    elif change == "citation_comment":
        item["referenceComments"] = ["PRIVATE_DETAILS"]
    elif change == "duplicate_citation":
        protein["references"].append(copy.deepcopy(item))
    elif change == "split_identifiers":
        doi = citation["citationCrossReferences"].pop()
        protein["references"].append({"citation": {"citationCrossReferences": [doi]}})
    with pytest.raises(ValueError):
        audit.project_protein(protein, taxon, leads())


@pytest.mark.parametrize(
    "change", ["other_paralog", "missing", "duplicate", "total", "pagination", "release"]
)
def test_query_completeness_and_paralog_substitution(change):
    payload = {"results": [entry("P06367")]}
    headers = {"X-Total-Results": "1", "X-UniProt-Release": "2026_03"}
    if change == "other_paralog":
        payload["results"] = [entry("P39516")]
    elif change == "missing":
        payload["results"] = []
    elif change == "duplicate":
        payload["results"].append(copy.deepcopy(payload["results"][0]))
    else:
        headers[
            {"total": "X-Total-Results", "pagination": "Link", "release": "X-UniProt-Release"}[change]
        ] = "OTHER"
    with pytest.raises(ValueError):
        audit.project_query(payload, headers, taxonomy(), leads(), "P06367")


def metadata(monkeypatch):
    abstract = "CRY1 CRY2 cryptopleurine Saccharomyces cerevisiae"
    monkeypatch.setattr(audit, "ABSTRACT_SHA", hashlib.sha256(abstract.encode()).hexdigest())
    row = {**leads()["8293976"], "abstractText": abstract, "isOpenAccess": "N", "inEPMC": "Y", "inPMC": "Y"}
    return {
        "hitCount": 1,
        "request": {
            "queryString": audit.METADATA_QUERY,
            "internalQuery": audit.METADATA_QUERY,
            "resultType": "CORE",
            "pageSize": 1,
        },
        "resultList": {"result": [row]},
    }


def test_abstract_scope_retained(monkeypatch):
    result = audit.metadata_context(metadata(monkeypatch), leads()["8293976"])
    assert result["primary_results_figures_supplements_reviewed"] is False
    assert result["tested_chemical_structure_or_form_verified"] is False
    assert result["single_gene_effect_inferred_from_combined_background"] is False
    assert result["experimental_allele_strain_or_genome_assignment"] is None
    assert "abstractText" not in result


@pytest.mark.parametrize(
    "change",
    [
        "count",
        "boolean_count",
        "query",
        "cursor",
        "size",
        "doi",
        "pmcid",
        "title",
        "abstract",
        "availability",
        "duplicate",
    ],
)
def test_metadata_guards(monkeypatch, change):
    value = metadata(monkeypatch)
    row = value["resultList"]["result"][0]
    if change in {"count", "boolean_count"}:
        value["hitCount"] = True if change == "boolean_count" else 2
    elif change == "query":
        value["request"]["queryString"] = "OTHER"
    elif change == "cursor":
        value["nextCursorMark"] = "NEXT"
    elif change == "size":
        value["request"]["pageSize"] = True
    elif change == "duplicate":
        value["resultList"]["result"].append(copy.deepcopy(row))
    else:
        row[
            {
                "doi": "doi",
                "pmcid": "pmcid",
                "title": "title",
                "abstract": "abstractText",
                "availability": "isOpenAccess",
            }[change]
        ] = "OTHER"
    with pytest.raises(ValueError):
        audit.metadata_context(value, leads()["8293976"])


def test_unplanned_request_rejected(tmp_path):
    directory = tmp_path / audit.CACHE
    directory.mkdir(parents=True)
    (directory / "unplanned-attempt.json").write_text("{}")
    with pytest.raises(ValueError, match="request inventory"):
        audit.build(tmp_path)


def test_native_checkpoint_replays_offline(monkeypatch):
    if not (ROOT / audit.CACHE / "cohort.json").is_file():
        pytest.skip("private native research cache is unavailable")

    def forbidden(*args, **kwargs):
        raise AssertionError("network forbidden in native replay")

    monkeypatch.setattr(requests.sessions.Session, "request", forbidden)
    monkeypatch.setattr(socket.socket, "connect", forbidden)
    monkeypatch.setattr(socket, "create_connection", forbidden)
    result = audit.build(ROOT)
    assert result == json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert len(result["reference_proteins"]) == 2
    assert result["limits"]["ncbi_requests"] == 0
    assert result["limits"]["biological_records_changed"] == 0
    assert result["limits"]["primary_results_reviews"] == 0
    assert result["paralogs_equated_or_substituted"] is False
