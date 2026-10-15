"""Exact IIIb references and generic IV candidates must retain different scopes."""

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
import audit_aac3_evidence as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def taxonomy(taxid, name):
    parent = {"taxonId": 2, "scientificName": "Bacteria", "rank": "domain"}
    return {
        "taxonId": taxid,
        "scientificName": name,
        "rank": "species",
        "active": True,
        "parent": {"taxonId": 2, "scientificName": "Bacteria"},
        "lineage": [parent],
    }


@pytest.fixture
def iiib():
    entry = {
        "primaryAccession": "Q51405",
        "entryType": "UniProtKB unreviewed (TrEMBL)",
        "entryAudit": {"entryVersion": 61, "sequenceVersion": 1},
        "genes": [{"geneName": {"value": "aac(3)-IIIb"}}],
        "organism": {"taxonId": 287, "scientificName": "Pseudomonas aeruginosa"},
        "uniProtKBCrossReferences": [],
        "references": [{"citation": {"citationCrossReferences": [{"database": "PubMed", "id": "30347146"}]}}],
        "sequence": "fixture-not-exported",
        "features": ["fixture-not-exported"],
    }
    return entry, taxonomy(287, "Pseudomonas aeruginosa")


def test_exact_iiib_gene_reference_not_experimental_allele(iiib):
    result = audit.project_iiib(*iiib)
    assert result["accession"] == "UniProtKB:Q51405"
    assert result["gene_symbols"] == ["aac(3)-IIIb"]
    assert result["experimental_allele_assignment"] is None
    for key in (
        "explicit_card_xref",
        "aro_own_citation_in_native_bibliography",
        "aro_cited_tested_enzyme_equated_with_reference",
        "experimental_identity_primary_review_complete",
        "experimental_subject_assignment",
    ):
        assert result[key] is False
    assert not set(result) & {"sequence", "features", "references"}


@pytest.mark.parametrize(
    "kind",
    [
        "accession",
        "gene",
        "entry_type",
        "entry_version",
        "sequence_version",
        "taxon_id",
        "taxon_name",
        "rank",
        "inactive",
        "citation",
        "card_xref",
    ],
)
def test_iiib_identity_and_scope_drift_fail_closed(iiib, kind):
    entry, taxon = iiib
    if kind == "accession":
        entry["primaryAccession"] = "Q51406"
    elif kind == "gene":
        entry["genes"][0]["geneName"]["value"] = "aac(3)-IIIc"
    elif kind == "entry_type":
        entry["entryType"] = "UniProtKB reviewed (Swiss-Prot)"
    elif kind in {"entry_version", "sequence_version"}:
        entry["entryAudit"]["entryVersion" if kind == "entry_version" else "sequenceVersion"] += 1
    elif kind == "taxon_id":
        taxon["taxonId"] = 562
    elif kind == "taxon_name":
        taxon["scientificName"] = "other"
    elif kind == "rank":
        taxon["rank"] = "strain"
    elif kind == "inactive":
        taxon["active"] = False
    elif kind == "citation":
        entry["references"][0]["citation"]["citationCrossReferences"][0]["id"] = "20387903"
    else:
        entry["uniProtKBCrossReferences"] = [{"database": "CARD", "id": "ARO:3002537"}]
    with pytest.raises(ValueError):
        audit.project_iiib(entry, taxon)


def related(accession):
    gene, taxid, flag = audit.RELATED[accession]
    name = audit.RELATED_TAXON_NAMES[taxid]
    entry = {
        "primaryAccession": accession,
        "entryType": "fixture reference",
        "entryAudit": {"entryVersion": 1},
        "genes": [{"geneName": {"value": gene}}],
        "organism": {"taxonId": taxid, "scientificName": name},
        "proteinDescription": {"flag": flag} if flag else {},
    }
    papers = ["PMID:6318050"] if accession == "P08988" else ["PMID:19709289"]
    return entry, taxonomy(taxid, name), papers


@pytest.mark.parametrize("accession", sorted(audit.RELATED))
def test_related_iv_references_do_not_resolve_iva_suffix(accession):
    result = audit.project_related(*related(accession))
    assert result["native_fragment_flag"] == audit.RELATED[accession][2]
    assert result["experimental_allele_assignment"] is None
    for key in (
        "exact_card_term_mapping_asserted",
        "experimental_subject_assignment",
        "generic_salmonella_label_promoted_to_named_species",
        "fragment_promoted_to_complete_protein",
    ):
        assert result[key] is False


@pytest.mark.parametrize("kind", ["unrelated", "gene", "taxid", "name", "fragment", "citation", "rank"])
def test_related_identity_completeness_and_citation_binding(kind):
    entry, taxon, papers = related("Q8KMV1")
    if kind == "unrelated":
        entry["primaryAccession"] = "P00557"
    elif kind == "gene":
        entry["genes"][0]["geneName"]["value"] = "hph"
    elif kind == "taxid":
        taxon["taxonId"] = 599
    elif kind == "name":
        taxon["scientificName"] = "other"
    elif kind == "fragment":
        entry["proteinDescription"].clear()
    elif kind == "citation":
        papers = ["PMID:6318050"]
    else:
        taxon["rank"] = "strain"
    with pytest.raises(ValueError):
        audit.project_related(entry, taxon, papers)


def test_native_salmonella_punctuation_not_species_inference():
    entry, taxon, papers = related("P08988")
    entry["organism"]["scientificName"] = "Salmonella sp"
    result = audit.project_related(entry, taxon, papers)
    assert result["source_organism_label"] == "Salmonella sp"
    assert result["reference_taxonomy"]["scientific_name"] == "Salmonella sp."
    assert result["generic_salmonella_label_promoted_to_named_species"] is False


@pytest.fixture
def metadata():
    expected = {
        "identity": {"id": "20387903", "doi": "fixture", "title": "Fixture title"},
        "abstract_sha256": hashlib.sha256(b"Fixture abstract").hexdigest(),
        "primary_link": [],
    }
    row = {
        **expected["identity"],
        "pmid": "20387903",
        "source": "MED",
        "abstractText": "Fixture abstract",
        "fullTextUrlList": {"fullTextUrl": []},
    }
    data = {
        "hitCount": 1,
        "request": {"queryString": "EXT_ID:20387903 AND SRC:MED", "resultType": "CORE", "pageSize": 1},
        "resultList": {"result": [row]},
    }
    return data, expected


def test_metadata_is_not_primary_or_access_denial(metadata):
    data, expected = metadata
    result = audit.project_metadata(data, "20387903", expected)
    assert result["primary_results_reviewed"] is False
    assert result["non_oa_metadata_is_access_denial"] is False
    assert "abstractText" not in result


@pytest.mark.parametrize(
    "kind",
    [
        "count",
        "boolean_count",
        "page_size",
        "boolean_page_size",
        "cursor",
        "query",
        "result_type",
        "pmid",
        "doi",
        "abstract",
        "links",
    ],
)
def test_metadata_scope_and_identity(metadata, kind):
    data, expected = metadata
    row = data["resultList"]["result"][0]
    if kind == "count":
        data["hitCount"] = 2
    elif kind == "boolean_count":
        data["hitCount"] = True
    elif kind in {"page_size", "boolean_page_size"}:
        data["request"]["pageSize"] = 2 if kind == "page_size" else True
    elif kind == "cursor":
        data["nextCursorMark"] = "next"
    elif kind in {"query", "result_type"}:
        data["request"]["queryString" if kind == "query" else "resultType"] = "other"
    elif kind == "links":
        row["fullTextUrlList"]["fullTextUrl"] = [{"url": "other"}]
    else:
        row[{"pmid": "pmid", "doi": "doi", "abstract": "abstractText"}[kind]] = "other"
    with pytest.raises(ValueError):
        audit.project_metadata(data, "20387903", expected)


def test_query_builder_bounds():
    assert "reviewed%3Atrue" in audit.gene_url(True)
    assert "reviewed%3Afalse" in audit.gene_url(False)
    with pytest.raises(ValueError):
        audit.gene_url(1)
    with pytest.raises(ValueError):
        audit.metadata_url("unknown")


def test_saved_dossier_reference_membership_not_biological_curation():
    saved = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert saved["scope"] == audit.SCOPE
    assert len(saved["records"]) == 14 and len(saved["claims"]) == 29
    assert len(saved["new_gene_reference_memberships"]) == 9
    assert saved["new_iiib_gene_reference"]["accession"] == "UniProtKB:Q51405"
    assert not any(saved["disposition"].values())
    assert len(saved["type_iv_related_references"]) == 3
    assert len(saved["incidental_citation_hits_not_selected"]) == 15
    assert saved["constraints"]["ncbi_requests"] == 0
    assert saved["constraints"]["full_corpus_goal_status"] == "OPEN"


def test_projectors_do_not_mutate_input(iiib):
    before = copy.deepcopy(iiib)
    audit.project_iiib(*iiib)
    assert iiib == before


@pytest.fixture
def landing():
    return b"""<html><head>
      <meta name="citation_doi" content="10.1021/acs.jmedchem.8b01393">
      <meta name="citation_title" content="Encoding of Promiscuity in an Aminoglycoside Acetyltransferase">
      <meta name="citation_pdf_url" content="https://www.osti.gov/servlets/purl/1484803">
      </head><body><a href="/servlets/purl/1484803">View Accepted Manuscript (DOE)</a></body></html>"""


def test_osti_landing_not_primary_text(landing):
    result = audit.project_landing(landing)
    assert result["bibliographic_page_is_primary_text"] is False
    assert result["access_gate_bypassed"] is False


@pytest.mark.parametrize(
    "before,after",
    [
        (b"10.1021/acs.jmedchem.8b01393", b"other"),
        (b"Encoding of Promiscuity", b"Other title"),
        (b"https://www.osti.gov/servlets/purl/1484803", b"https://example.org/other"),
        (b"View Accepted Manuscript (DOE)", b"Unrelated link"),
    ],
)
def test_native_landing_identity_and_pdf_link(landing, before, after):
    with pytest.raises(ValueError):
        audit.project_landing(landing.replace(before, after))
