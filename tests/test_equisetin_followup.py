"""Host metabolism and component references do not establish resistant alleles."""

import copy
import hashlib
import json
import socket
import sys
from pathlib import Path

import pytest
import requests
from lxml import etree

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_equisetin_followup as audit  # noqa: E402


@pytest.fixture
def references():
    entries, taxa = [], {}
    for accession, (taxid, version, seq_version, genes, loci) in audit.PROTEINS.items():
        name, rank = audit.TAXA[str(taxid)]
        taxa[str(taxid)] = {
            "taxonId": taxid,
            "scientificName": name,
            "rank": rank,
            "active": True,
            "lineage": [{"taxonId": 562, "scientificName": "Escherichia coli", "rank": "species"}],
        }
        entries.append(
            {
                "primaryAccession": accession,
                "entryType": "UniProtKB reviewed (Swiss-Prot)",
                "entryAudit": {"entryVersion": version, "sequenceVersion": seq_version},
                "organism": {"taxonId": taxid, "scientificName": name},
                "genes": [
                    {
                        "geneName": {"value": genes[0]},
                        "synonyms": [{"value": g} for g in genes[1:]],
                        "orderedLocusNames": [{"value": g} for g in loci],
                    }
                ],
                "proteinDescription": {"recommendedName": {"fullName": {"value": "Biotin carboxylase"}}},
                "references": [
                    {
                        "citation": {"citationCrossReferences": [{"database": "PubMed", "id": "1682920"}]},
                        "referencePositions": ["PRIVATE CONTEXT MUST NOT BE EXPORTED"],
                    }
                ],
            }
        )
    return {"results": entries}, {"x-total-results": "2", "x-uniprot-release": "2026_03"}, taxa


def test_two_references_are_not_one_tested_enzyme_or_resistant_allele(references):
    result = audit.project_references(*references)
    assert [r["protein_accession"] for r in result] == ["UniProtKB:P24182", "UniProtKB:Q8X9B6"]
    assert [r["reference_taxon_rank"] for r in result] == ["strain", "no rank"]
    assert result[0]["gene_names"] == ["accC", "fabG"]
    for row in result:
        assert row["reference_species_taxon_id"] == "NCBITaxon:562"
        assert row["exact_resistance_allele"] is False
        assert row["experimental_subject_assignment"] is False
        assert row["selected_pmid_in_returned_bibliography"] is False
        assert row["gene_symbol_is_verbatim_primary_paper_assignment"] is False
        assert row["bibliography"][0]["primary_results_reviewed"] is False
    assert "PRIVATE CONTEXT" not in json.dumps(result)
    assert "source_species_taxon_id" not in json.dumps(result)


@pytest.mark.parametrize(
    "change",
    [
        "member",
        "duplicate",
        "not_dict",
        "sequence",
        "features",
        "comments",
        "unreviewed",
        "version",
        "sequence_version",
        "boolean_version",
        "gene",
        "alias",
        "locus",
        "protein_name",
        "organism_id",
        "organism_name",
        "taxon_id",
        "taxon_name",
        "taxon_rank",
        "inactive",
        "lineage",
        "duplicate_species",
        "paper_citation",
    ],
)
def test_reference_identity_scope_and_lineage_guards(references, change):
    payload, headers, taxa = references
    entry = payload["results"][0]
    taxon = taxa["83333"]
    if change == "member":
        entry["primaryAccession"] = "OTHER"
    elif change == "duplicate":
        payload["results"][1] = copy.deepcopy(entry)
    elif change == "not_dict":
        payload["results"][0] = None
    elif change in {"sequence", "features", "comments"}:
        entry[change] = []
    elif change == "unreviewed":
        entry["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    elif change in {"version", "sequence_version", "boolean_version"}:
        entry["entryAudit"]["sequenceVersion" if change == "sequence_version" else "entryVersion"] = (
            True if change == "boolean_version" else 999
        )
    elif change == "gene":
        entry["genes"][0]["geneName"]["value"] = "OTHER"
    elif change == "alias":
        entry["genes"][0]["synonyms"] = []
    elif change == "locus":
        entry["genes"][0]["orderedLocusNames"].pop()
    elif change == "protein_name":
        entry["proteinDescription"]["recommendedName"]["fullName"]["value"] = "OTHER"
    elif change in {"organism_id", "organism_name"}:
        entry["organism"]["taxonId" if change == "organism_id" else "scientificName"] = "OTHER"
    elif change in {"taxon_id", "taxon_name", "taxon_rank"}:
        taxon[{"taxon_id": "taxonId", "taxon_name": "scientificName", "taxon_rank": "rank"}[change]] = "OTHER"
    elif change == "inactive":
        taxon["active"] = False
    elif change == "lineage":
        taxon["lineage"][0]["taxonId"] = 1280
    elif change == "duplicate_species":
        taxon["lineage"].append(copy.deepcopy(taxon["lineage"][0]))
    else:
        entry["references"][0]["citation"]["citationCrossReferences"][0]["id"] = "32470050"
    with pytest.raises(ValueError):
        audit.project_references(payload, headers, taxa)


@pytest.mark.parametrize("count", [0, 2])
@pytest.mark.parametrize(
    "change", ["missing", "null", "count", "header", "release", "pagination", "not_dict"]
)
def test_complete_query_requires_complete_results_and_release(count, change):
    payload = {"results": [{} for _ in range(count)]}
    headers = {"x-total-results": str(count), "x-uniprot-release": "2026_03"}
    if change == "missing":
        payload.pop("results")
    elif change == "null":
        payload["results"] = None
    elif change == "count":
        payload["results"].append({})
    elif change == "header":
        headers["x-total-results"] = "not a count"
    elif change == "release":
        headers["x-uniprot-release"] = "OTHER"
    elif change == "pagination":
        headers["link"] = "next"
    else:
        payload = []
    with pytest.raises(ValueError, match="incomplete or malformed"):
        audit.complete_query(payload, headers, count)


def test_empty_query_suggestion_is_not_a_result():
    assert (
        audit.complete_query(
            {"results": [], "suggestions": [{"query": "lit_pubmed:3227050", "hits": 0}]},
            {"X-Total-Results": "0", "X-UniProt-Release": "2026_03"},
            0,
        )
        == []
    )


@pytest.fixture(params=["2024", "2020"])
def article(request):
    year = request.param
    root = etree.Element("article")
    meta = etree.SubElement(etree.SubElement(root, "front"), "article-meta")
    for kind, value in zip(("pmid", "pmcid", "doi"), audit.ARTICLES[year][:3], strict=True):
        etree.SubElement(meta, "article-id", {"pub-id-type": kind}).text = value
    etree.SubElement(meta, "abstract")
    body = etree.SubElement(root, "body")
    for _ in range(3):
        section = etree.SubElement(body, "sec")
        for _ in range(7):
            etree.SubElement(section, "p")
        for _ in range(7):
            subsection = etree.SubElement(section, "sec")
            for _ in range(2):
                etree.SubElement(subsection, "p")
            etree.SubElement(etree.SubElement(subsection, "fig"), "caption")
    for xpath, marker in audit.LOCATIONS[year].values():
        nodes = root.xpath(xpath)
        for extra in nodes[1:]:
            extra.getparent().remove(extra)
        nodes[0].text = "Synthetic fixture: " + marker
    return year, root


def project_article(article, monkeypatch):
    year, root = article
    payload = etree.tostring(root)
    monkeypatch.setitem(
        audit.ARTICLES, year, (*audit.ARTICLES[year][:3], hashlib.sha256(payload).hexdigest())
    )
    return audit.article_context(payload, year)[1]


def test_primary_evidence_scope_is_not_resistance_curation(article, monkeypatch):
    year, _ = article
    context = project_article(article, monkeypatch)
    assert context["scope"] == "SELECTED_PRIMARY_TEXT_NOT_COMPLETE_FIGURE_OR_SUPPLEMENT_REVIEW"
    if year == "2024":
        assert context["host_AMPK_results_are_antibiotic_resistance_evidence"] is False
        assert context["culture_antibiotics_are_susceptibility_observations"] is False
        assert context["source_use"] == "REFERENCE_ONLY_NO_SOURCE_DATA_ADOPTION"
        assert context["source_text_or_figures_redistributed"] is False
    else:
        assert context["donor_strain_resolved"] is False
        assert context["source_IC90_converted_to_MIC"] is False
        assert context["PYRC_transcriptomics_transferred_to_equisetin"] is False
        assert context["other_ACC_inhibitor_alleles_transferred_to_equisetin"] is False
        assert context["resistance_to_other_antibiotics_transferred_to_equisetin"] is False
        assert context["TA289_or_pyrrolocin_C_equated_to_equisetin"] is False
        assert context["complete_common_mechanism_or_genetic_causality_established"] is False
    assert "Synthetic fixture" not in json.dumps(context)


@pytest.mark.parametrize("change", ["pmid", "doi", "pmcid", "marker", "missing", "duplicate", "bytes"])
def test_primary_review_cannot_follow_changed_source(article, monkeypatch, change):
    year, root = article
    if change == "bytes":
        with pytest.raises(ValueError, match="article changed"):
            audit.article_context(etree.tostring(root), year)
        return
    if change in {"pmid", "doi", "pmcid"}:
        root.xpath(f'./front/article-meta/article-id[@pub-id-type="{change}"]')[0].text = "OTHER"
    else:
        xpath, _ = audit.LOCATIONS[year]["host_pathway" if year == "2024" else "figure8_caption"]
        node = root.xpath(xpath)[0]
        if change == "marker":
            node.text = "OTHER"
        elif change == "missing":
            node.getparent().remove(node)
        else:
            node.getparent().append(copy.deepcopy(node))
    with pytest.raises(ValueError):
        project_article(article, monkeypatch)


@pytest.fixture
def bibliography():
    root = etree.Element("article")
    ref = etree.SubElement(root, "ref", id="bib24")
    for kind, value in zip(("pmid", "pmcid", "doi"), audit.ARTICLES["2020"][:3], strict=True):
        etree.SubElement(
            ref, "ext-link", {"ext-link-type": kind, "{http://www.w3.org/1999/xlink}href": value}
        )
    return root


@pytest.mark.parametrize(
    "change", ["none", "missing_ref", "duplicate_ref", "missing_id", "duplicate_id", "wrong_id"]
)
def test_bibliography_requires_three_unique_native_identifiers(bibliography, change):
    ref = bibliography[0]
    if change == "none":
        assert audit.bibliography_lead(bibliography)["pmid"] == "32470050"
        return
    if change == "missing_ref":
        bibliography.remove(ref)
    elif change == "duplicate_ref":
        bibliography.append(copy.deepcopy(ref))
    elif change == "missing_id":
        ref.remove(ref[0])
    elif change == "duplicate_id":
        ref.append(copy.deepcopy(ref[0]))
    else:
        ref[0].set("{http://www.w3.org/1999/xlink}href", "OTHER")
    with pytest.raises(ValueError):
        audit.bibliography_lead(bibliography)


@pytest.mark.parametrize("change", ["none", "missing", "duplicate", "term", "label", "query_term"])
def test_official_search_configuration_does_not_conflate_fields(change):
    fields = [
        {"label": "Organism [OS]", "term": "organism_name", "autoCompleteQueryTerm": "organism_id"},
        {"label": "Taxonomy [OC]", "term": "taxonomy_name", "autoCompleteQueryTerm": "taxonomy_id"},
    ]
    if change == "none":
        assert audit.search_fields({"groups": [{"fields": fields}]}) == fields
        return
    if change == "missing":
        fields.pop()
    elif change == "duplicate":
        fields.append(copy.deepcopy(fields[0]))
    else:
        fields[0]["autoCompleteQueryTerm" if change == "query_term" else change] = "OTHER"
    with pytest.raises(ValueError):
        audit.search_fields({"groups": [{"fields": fields}]})


@pytest.mark.parametrize("change", ["missing_receipt", "missing_attempt", "unresolved_attempt"])
def test_request_coverage_fails_closed(tmp_path, change):
    directory = tmp_path / "cache"
    directory.mkdir()
    for key in {"primary-doi", "primary-publisher", "article-2024", "article-2020", "search-fields"} | set(
        audit.QUERIES
    ):
        for suffix in ("receipt", "attempt"):
            (directory / f"{key}-{suffix}.json").touch()
    if change == "unresolved_attempt":
        (directory / "unreported-attempt.json").touch()
    else:
        (directory / f"primary-doi-{change.removeprefix('missing_')}.json").unlink()
    with pytest.raises(ValueError, match="research request coverage"):
        audit.build(tmp_path, Path("cache"))


def test_public_dispositions_do_not_count_access_hold_as_primary_review():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    status = result["discovery_status"]
    dispositions = status["initial_candidate_dispositions"]
    assert len(dispositions) == status["initial_candidate_identities"] == 8
    assert (
        list(dispositions.values()).count("UNASSESSED")
        == status["initial_candidates_without_followup_disposition"]
        == 5
    )
    assert dispositions["MED:23715404"] == "ACCESS_HOLD_PRIMARY_RESULTS_UNREVIEWED"
    assert status["initial_candidates_primary_results_unreviewed_including_held"] == 6
    assert status["additional_primary_bibliography_leads"] == 1
    assert result["TA289"]["primary_results_reviewed"] is False
    assert result["query_interpretation"]["empty_queries_establish_protein_absence"] is False
    assert result["limits"]["biological_records_changed"] == 0
    assert result["limits"]["ncbi_requests"] == 0
    assert result["limits"]["issue_1040"] == "DEFERRED"
    assert result["limits"]["whole_record_primary_review"] == "OPEN"
    assert result["limits"]["full_corpus_goal_status"] == "OPEN"


def test_cache_replay_is_offline_and_does_not_read_live_records(monkeypatch):
    if not (ROOT / audit.CACHE / "reference-taxonomy-receipt.json").exists():
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
    [
        "manual_redirect",
        "redirect_binding",
        "distinct_study",
        "bibliography_binding",
        "canary_binding",
        "primary_review_binding",
        "alternate_pmid",
        "field_configuration",
        "retry_claim",
    ],
)
def test_cached_request_provenance_guards(monkeypatch, change):
    if not (ROOT / audit.CACHE / "reference-taxonomy-receipt.json").exists():
        pytest.skip("private source cache is not distributed")
    original_loads = json.loads

    def altered(payload, *args, **kwargs):
        value = original_loads(payload, *args, **kwargs)
        if not isinstance(value, dict):
            return value
        if change == "manual_redirect" and "manual_redirect_reviewed" in value:
            value["manual_redirect_reviewed"] = False
        elif change == "redirect_binding" and "redirect_receipt" in value:
            value["redirect_receipt"] = {}
        elif change == "distinct_study" and "not_alternate_route_for_held_TA289_paper" in value:
            value["not_alternate_route_for_held_TA289_paper"] = False
        elif change == "bibliography_binding" and "bibliography_source" in value:
            value["bibliography_source"] = {}
        elif change == "canary_binding" and "canary_review" in value:
            value["canary_review"] = {}
        elif change == "primary_review_binding" and "primary_review" in value:
            value["primary_review"] = {}
        elif change == "alternate_pmid" and "provider_alternate_PMID_suggestion_followed" in value:
            value["provider_alternate_PMID_suggestion_followed"] = True
        elif change == "field_configuration" and "field_configuration" in value:
            value["field_configuration"] = {}
        elif change == "retry_claim" and "network_attempts_created_by_failed_plan_command" in value:
            value["request_retried"] = True
        return value

    monkeypatch.setattr(json, "loads", altered)
    with pytest.raises(ValueError):
        audit.build(ROOT)
