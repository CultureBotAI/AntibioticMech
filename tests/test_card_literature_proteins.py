"""Query completeness is not proof of gene identity or a resistance phenotype."""

import hashlib
import json
import sys
from pathlib import Path
from urllib.parse import urlencode

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_literature_proteins as audit  # noqa: E402

PMID = "12345"
TID = "ARO:3002620"


def entry(accession="P00001", gene="aadA23", pmid=PMID):
    return {"primaryAccession": accession, "genes": [{"geneName": {"value": gene}}],
            "references": [{"referenceNumber": 1, "citation": {
                "citationCrossReferences": [{"database": "PubMed", "id": pmid}]}}]}


def page(root, rows, total, *, number=1, cursor=None, next_cursor=None, release="2026_03"):
    directory = root / "cache"
    directory.mkdir(exist_ok=True)
    key = "pmid-" + PMID + (f"-page-{number:03d}" if number > 1 else "")
    path, receipt_path = directory / (key + "-response.bin"), directory / (key + "-receipt.json")
    body = (json.dumps({"results": rows}) + "\n").encode()
    path.write_bytes(body)
    params = audit.parameters(PMID)
    if cursor:
        params["cursor"] = cursor
    url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(params)
    headers = {"X-Total-Results": str(total), "X-UniProt-Release": release}
    if next_cursor:
        next_params = {**audit.parameters(PMID), "cursor": next_cursor}
        headers["Link"] = ('<https://rest.uniprot.org/uniprotkb/search?'
                           + urlencode(next_params) + '>; rel="next"')
    receipt = {"url": url, "query": "lit_pubmed:" + PMID, "status": 200,
               "sha256": hashlib.sha256(body).hexdigest(), "bytes": len(body),
               "headers": headers, "retrieved_at": "fixture"}
    receipt_path.write_text(json.dumps(receipt))
    return directory, path, receipt_path


def change_receipt(path, **changes):
    data = json.loads(path.read_bytes())
    data.update(changes)
    path.write_text(json.dumps(data))


def test_complete_zero_result_is_not_biological_absence(tmp_path):
    directory, _, _ = page(tmp_path, [], 0)
    entries, result = audit.read_query(tmp_path, directory, PMID)
    assert entries == {} and result["result_count"] == 0
    assert result["complete_for_query"] is True
    assert result["establishes_biological_absence"] is False


def test_query_bound_multi_page_chain_is_complete(tmp_path):
    first = [entry(f"P{i:05d}") for i in range(500)]
    second = [entry(f"P{i:05d}") for i in range(500, 503)]
    directory, _, _ = page(tmp_path, first, 503, next_cursor="next")
    page(tmp_path, second, 503, number=2, cursor="next")
    entries, result = audit.read_query(tmp_path, directory, PMID)
    assert len(entries) == result["result_count"] == 503
    assert len(result["pages"]) == 2 and result["complete_for_query"] is True


@pytest.mark.parametrize("field,value", [("status", 503), ("sha256", "wrong"), ("bytes", 0),
                                         ("query", "lit_pubmed:999")])
def test_failed_or_different_receipt_never_becomes_a_negative_result(tmp_path, field, value):
    directory, _, receipt = page(tmp_path, [entry()], 1)
    change_receipt(receipt, **{field: value})
    with pytest.raises(ValueError, match="identity|status or digest"):
        audit.read_query(tmp_path, directory, PMID)


@pytest.mark.parametrize("url", ["https://example.org/uniprotkb/search", "http://rest.uniprot.org/uniprotkb/search",
                                "https://rest.uniprot.org/taxonomy/search"])
def test_request_endpoint_guard(tmp_path, url):
    directory, _, receipt = page(tmp_path, [], 0)
    change_receipt(receipt, url=url + "?" + urlencode(audit.parameters(PMID)))
    with pytest.raises(ValueError, match="request identity"):
        audit.read_query(tmp_path, directory, PMID)


def test_entry_must_cite_requested_paper(tmp_path):
    directory, _, _ = page(tmp_path, [entry(pmid="54321")], 1)
    with pytest.raises(ValueError, match="does not cite"):
        audit.read_query(tmp_path, directory, PMID)


@pytest.mark.parametrize("mutation", ["sequence", "duplicate", "order", "count"])
def test_entry_and_cardinality_guards(tmp_path, mutation):
    rows, total = [entry()], 1
    if mutation == "sequence":
        rows[0]["sequence"] = {"value": "PRIVATE"}
    elif mutation == "duplicate":
        rows, total = [entry(), entry()], 2
    elif mutation == "order":
        rows, total = [entry("P00002"), entry("P00001")], 2
    else:
        total = 2
    directory, _, _ = page(tmp_path, rows, total)
    with pytest.raises(ValueError, match="sequence|out-of-order|cardinality"):
        audit.read_query(tmp_path, directory, PMID)


def test_missing_continuation_is_not_complete(tmp_path):
    directory, _, _ = page(tmp_path, [entry(f"P{i:05d}") for i in range(500)], 501, next_cursor="next")
    with pytest.raises(FileNotFoundError):
        audit.read_query(tmp_path, directory, PMID)


def test_early_termination_rejected(tmp_path):
    directory, _, _ = page(tmp_path, [entry(f"P{i:05d}") for i in range(500)], 501)
    with pytest.raises(ValueError, match="termination"):
        audit.read_query(tmp_path, directory, PMID)


def test_pagination_cycle_rejected_before_another_page_is_read(tmp_path):
    directory, _, _ = page(tmp_path, [entry(f"P{i:05d}") for i in range(500)], 1001, next_cursor="same")
    page(tmp_path, [entry(f"P{i:05d}") for i in range(500, 1000)], 1001,
         number=2, cursor="same", next_cursor="same")
    with pytest.raises(ValueError, match="pagination cycle"):
        audit.read_query(tmp_path, directory, PMID)


@pytest.mark.parametrize("mutation", ["host", "query"])
def test_next_link_cannot_leave_approved_query(tmp_path, mutation):
    directory, _, receipt_path = page(tmp_path, [entry(f"P{i:05d}") for i in range(500)], 501,
                                     next_cursor="next")
    receipt = json.loads(receipt_path.read_bytes())
    params = {**audit.parameters(PMID), "cursor": "next"}
    if mutation == "query":
        params["query"] = "lit_pubmed:54321"
    host = "example.org" if mutation == "host" else "rest.uniprot.org"
    receipt["headers"]["Link"] = ('<https://' + host + '/uniprotkb/search?'
                                  + urlencode(params) + '>; rel="next"')
    receipt_path.write_text(json.dumps(receipt))
    with pytest.raises(ValueError, match="pagination"):
        audit.read_query(tmp_path, directory, PMID)


@pytest.mark.parametrize("change", ["release", "total", "cursor"])
def test_continuation_identity_drift_rejected(tmp_path, change):
    directory, _, _ = page(tmp_path, [entry(f"P{i:05d}") for i in range(500)], 501, next_cursor="next")
    page(tmp_path, [entry("P00500")], 502 if change == "total" else 501, number=2,
         cursor="wrong" if change == "cursor" else "next",
         release="other" if change == "release" else "2026_03")
    with pytest.raises(ValueError, match="request identity|count or release"):
        audit.read_query(tmp_path, directory, PMID)


def test_orphaned_ignored_page_is_not_silently_accepted(tmp_path):
    directory, _, _ = page(tmp_path, [entry()], 1)
    (tmp_path / ".gitignore").write_text("cache/\n")
    page(tmp_path, [entry("P00002")], 1, number=2, cursor="orphan")
    with pytest.raises(ValueError, match="orphaned"):
        audit.read_query(tmp_path, directory, PMID)


def selected(label="aadA23"):
    return {TID: {"source_label": label, "source_label_sha256": audit.citations.text_hash(label),
                  "definition_citation_ids": ["PMID:" + PMID], "record_memberships": ["CHEBI:1"]}}


def test_same_paper_different_gene_is_not_a_reference_candidate():
    rows = {"P00001": entry(gene="dfrA15b"), "P00002": entry("P00002")}
    result = audit.derive_terms(selected(), rows, {PMID: sorted(rows)})[TID]
    candidate, = result["reference_candidates"]
    assert candidate["protein_accession"] == "UniProtKB:P00002"
    assert candidate["scope"] == "REFERENCE_CANDIDATE_NOT_EXPERIMENTAL_IDENTITY"
    assert result["nonmatching_entries"] == 1 and result["no_match_is_biological_absence"] is False


def test_alias_fields_remain_distinct_and_locus_names_do_not_match():
    data = entry(gene="canonical")
    data["genes"][0]["synonyms"] = [{"value": "AADa23"}]
    matches, direct = audit.match_entry(data, TID, "aadA23")
    assert matches == [{"field": "synonyms", "value": "AADa23"}] and direct is False
    data["genes"][0].pop("synonyms")
    data["genes"][0]["orderedLocusNames"] = [{"value": "aadA23"}]
    assert audit.match_entry(data, TID, "aadA23") == ([], False)


def test_explicit_xref_does_not_require_a_name_match_but_still_needs_citation_membership():
    data = entry(gene="different")
    data["uniProtKBCrossReferences"] = [{"database": "CARD", "id": TID}]
    row = audit.derive_terms(selected(), {"P00001": data}, {PMID: ["P00001"]})[TID]
    assert row["reference_candidates"][0]["explicit_card_xref"] is True
    assert row["reference_candidates"][0]["literal_gene_matches"] == []
    assert audit.derive_terms(selected(), {"P00001": data}, {PMID: []})[TID]["reference_candidates"] == []


def test_family_matches_keep_multiple_accessions():
    rows = {"P00001": entry(gene="cat"), "P00002": entry("P00002", gene="cat")}
    result = audit.derive_terms(selected("cat"), rows, {PMID: sorted(rows)})[TID]
    assert len(result["reference_candidates"]) == 2
    assert result["primary_review_status"] == "NOT_COMPLETED_BY_METADATA_LOOKUP"


def test_published_cohort_and_query_completeness():
    result = json.loads((ROOT / audit.DEFAULT_OUTPUT).read_bytes())
    summary = result["summary"]
    assert result["scope"] == audit.SCOPE and result["selection"] == "FULL_59_TERM_COHORT"
    assert summary["corpus_records_checked"] == 2939 and summary["selected_terms"] == 59
    assert summary["selected_records"] == 64 and summary["selected_assertion_memberships"] == 152
    assert summary["completed_queries"] == len(result["queries"]) == 111
    assert summary["paginated_queries_completed"] == 4 and summary["response_pages"] == 134
    assert all(q["complete_for_query"] and not q["establishes_biological_absence"]
               for q in result["queries"].values())
    assert summary["biological_records_changed"] == summary["exact_allele_assignments"] == 0
    assert all(not p["experimental_subject_assignment"] for p in result["proteins"].values())
    aad, = result["terms"][TID]["reference_candidates"]
    assert aad["protein_accession"] == "UniProtKB:Q6A150"
    assert aad["literal_gene_matches"] == [{"field": "geneName", "value": "aadA23"}]
