"""Metadata concordance must preserve incomplete searches and entity boundaries."""

import copy
import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import urlencode

import pytest

from scripts import audit_card_literature_expansion as audit


def entry(accession="P00001", gene="bmr", pmid="111"):
    return {"primaryAccession": accession, "genes": [{"geneName": {"value": gene}}],
            "references": [{"referenceNumber": 1, "citation": {"citationCrossReferences": [
                {"database": "PubMed", "id": pmid}]}}]}


def page(directory, rows, *, number=1, total=None, next_page=False, status=200):
    parameters = audit.literature.parameters("111")
    if number > 1:
        parameters["cursor"] = "next"
    url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(parameters)
    name = "pmid-111" + (f"-page-{number:03d}" if number > 1 else "")
    body = json.dumps({"results": rows}).encode()
    headers = {"x-total-results": str(len(rows) if total is None else total), "x-uniprot-release": "2026_03"}
    if next_page:
        link = "https://rest.uniprot.org/uniprotkb/search?" + urlencode({**parameters, "cursor": "next"})
        headers["link"] = f'<{link}>; rel="next"'
    receipt = {"url": url, "query": "lit_pubmed:111", "status": status,
               "sha256": hashlib.sha256(body).hexdigest(), "bytes": len(body),
               "headers": headers, "retrieved_at": "2026-10-13T12:00:00Z"}
    directory.mkdir(exist_ok=True)
    raw = directory / (name + "-response.bin")
    meta = directory / (name + "-receipt.json")
    raw.write_bytes(body)
    meta.write_text(json.dumps(receipt))
    return raw, meta


def test_no_query_is_not_an_empty_success(tmp_path):
    rows, query = audit.read_query(tmp_path, tmp_path / "cache", "111")
    assert rows == {} and query == {"status": "NOT_QUERIED", "complete_for_query": False}


def test_complete_empty_query_is_not_biological_absence(tmp_path):
    page(tmp_path, [])
    rows, query = audit.read_query(tmp_path, tmp_path, "111")
    assert rows == {} and query["result_count"] == 0 and query["complete_for_query"]
    assert not query["establishes_biological_absence"]


@pytest.mark.parametrize("failure", ["orphan", "hash", "host", "query", "duplicate", "sequence", "citation"])
def test_bad_cached_evidence_is_rejected(tmp_path, failure):
    rows = [entry()]
    if failure == "duplicate":
        rows.append(entry())
    elif failure == "sequence":
        rows[0]["sequence"] = {"value": "EXCLUDED"}
    elif failure == "citation":
        rows[0] = entry(pmid="222")
    raw, meta = page(tmp_path, rows)
    if failure == "orphan":
        raw.unlink()
    elif failure == "hash":
        raw.write_bytes(raw.read_bytes() + b" ")
    elif failure in {"host", "query"}:
        receipt = json.loads(meta.read_bytes())
        receipt["url"] = receipt["url"].replace(
            "rest.uniprot.org" if failure == "host" else "111",
            "example.invalid" if failure == "host" else "222")
        meta.write_text(json.dumps(receipt))
    with pytest.raises(ValueError):
        audit.read_query(tmp_path, tmp_path, "111")


def test_source_failure_is_not_retried_or_treated_as_no_hit(tmp_path, monkeypatch):
    page(tmp_path, [], status=403)
    monkeypatch.setattr(audit.literature, "read_query", lambda *args: pytest.fail("success parser used"))
    rows, query = audit.read_query(tmp_path, tmp_path, "111")
    assert rows == {} and query["http_status"] == 403
    assert not query["complete_for_query"] and query["status"] == "SOURCE_REQUEST_FAILED"


def test_incomplete_pages_contribute_no_candidates_then_replay_completes(tmp_path):
    page(tmp_path, [entry(f"P{i:05d}") for i in range(500)], total=501, next_page=True)
    rows, query = audit.read_query(tmp_path, tmp_path, "111")
    assert rows == {} and query["status"] == "CURSOR_TRAVERSAL_PENDING"
    page(tmp_path, [entry("P00500")], number=2, total=501)
    rows, query = audit.read_query(tmp_path, tmp_path, "111")
    assert len(rows) == 501 and query["complete_for_query"] and len(query["pages"]) == 2


def test_orphan_continuation_is_rejected(tmp_path):
    page(tmp_path, [entry()])
    page(tmp_path, [entry("P00002")], number=2)
    with pytest.raises(ValueError, match="orphaned continuation"):
        audit.read_query(tmp_path, tmp_path, "111")


def selected(scope="OTHER_TERM_ENTITY_GRANULARITY_UNRESOLVED"):
    return {"ARO:3003007": {"source_label": "bmr", "source_label_sha256": "label-hash",
            "definition_citation_ids": ["PMID:111"], "record_memberships": ["CHEBI:17939"],
            "entity_scope": scope}}


@pytest.mark.parametrize("scope", sorted(audit.NONPROTEIN))
def test_nonprotein_entities_do_not_inherit_single_proteins(scope):
    rows = audit.match_terms(selected(scope), {"P00001": entry()}, {"111": ["P00001"]},
                             {"111": {"complete_for_query": True}})
    row = rows["ARO:3003007"]
    assert not row["reference_candidates"] and len(row["entity_scope_withheld_matches"]) == 1
    assert not row["entity_scope_withheld_matches"][0]["experimental_identity_assigned"]


def test_literal_alias_match_is_only_reference_context():
    protein = entry(gene="another")
    protein["genes"][0]["synonyms"] = [{"value": "BMR"}]
    result = audit.match_terms(selected(), {"P00001": protein}, {"111": ["P00001"]},
                               {"111": {"complete_for_query": True}})["ARO:3003007"]
    match, = result["reference_candidates"]
    assert match["literal_gene_matches"] == [{"field": "synonyms", "value": "BMR"}]
    assert not match["explicit_card_xref"] and not match["experimental_identity_assigned"]
    assert result["primary_review_status"].startswith("OPEN")


def test_reviewed_protein_identity_is_not_overwritten_by_rna_ancestry():
    cohort = selected("RNA_TERM_NOT_A_PROTEIN_PRODUCT")
    reviews = {"ARO:3003007": {
        "entity_scope": "PROTEIN_PRODUCT_WITH_CONFLICTING_RNA_ANCESTRY",
        "historical_entity_scope": "RNA_TERM_NOT_A_PROTEIN_PRODUCT",
        "experimental_identity_assigned": False,
    }}
    row = audit.match_terms(cohort, {"P00001": entry()}, {"111": ["P00001"]},
                            {"111": {"complete_for_query": True}}, reviews)["ARO:3003007"]
    assert row["source_entity_scope"] == "RNA_TERM_NOT_A_PROTEIN_PRODUCT"
    assert row["entity_scope"] == "PROTEIN_PRODUCT_WITH_CONFLICTING_RNA_ANCESTRY"
    assert row["entity_scope_basis"] == "REVIEWED_IDENTITY"
    assert len(row["reference_candidates"]) == 1 and not row["entity_scope_withheld_matches"]
    assert not row["reference_candidates"][0]["experimental_identity_assigned"]
    with pytest.raises(ValueError, match="different source entity scope"):
        audit.match_terms(selected(), {}, {"111": []}, {"111": {"complete_for_query": True}}, reviews)


def test_shared_citation_or_matching_locus_is_not_matching_gene():
    protein = entry(gene="unrelated")
    protein["genes"][0]["orderedLocusNames"] = [{"value": "bmr"}]
    row = audit.match_terms(selected(), {"P00001": protein}, {"111": ["P00001"]},
                            {"111": {"complete_for_query": True}})["ARO:3003007"]
    assert not row["reference_candidates"] and not row["no_match_establishes_biological_absence"]


@pytest.mark.parametrize("citations", [[], ["DOI:10.1039/C2MD20038D"], ["PMID:111"]])
def test_no_citation_doi_only_and_pending_query_remain_open(citations):
    cohort = selected()
    cohort["ARO:3003007"]["definition_citation_ids"] = citations
    row = audit.match_terms(cohort, {}, {"111": []}, {"111": {"complete_for_query": False}})["ARO:3003007"]
    assert not row["all_source_citations_queried"] and not row["reference_candidates"]
    assert row["primary_review_status"].startswith("OPEN")


def test_selection_excludes_prior_cohort_but_retains_no_citation_terms():
    labels = {"A": "first", "B": "second", "C": "third"}
    source = {"terms": {t: {"label_sha256": audit.definitions.text_hash(label),
                           "definition_citation_ids": [], "record_memberships": ["R"]}
                        for t, label in labels.items()}}
    direct = {"determinants": {t: {"candidates": ["reference"] if t == "A" else []} for t in labels}}
    prior = {"terms": {"B": {}}}
    scopes = {"terms": {t: {"entity_scope": "unresolved"} for t in labels}}
    assert set(audit.selection(direct, source, prior, scopes, labels)) == {"C"}
    altered = copy.deepcopy(source)
    altered["terms"]["C"]["label_sha256"] = "tampered"
    with pytest.raises(ValueError, match="label digest"):
        audit.selection(direct, altered, prior, scopes, labels)


def test_record_summary_includes_records_outside_the_cohort_without_completing_them():
    census = [{"identifier": i, "path": i + ".yaml", "record_sha256": "hash",
               "standard_inchi_key": "identity"} for i in ("CHEBI:17939", "OTHER")]
    terms = audit.match_terms(selected(), {}, {"111": []}, {"111": {"complete_for_query": False}})
    rows = audit.record_summary(census, terms)
    assert len(rows) == 2 and rows[0]["pending_citation_terms"] == ["ARO:3003007"]
    assert rows[1]["cohort_terms"] == []
    assert {r["whole_record_primary_review"] for r in rows} == {"OPEN"}
    terms["ARO:3003007"]["record_memberships"].append("CHEBI:17939")
    repeated = audit.record_summary(census, terms)[0]
    assert repeated["cohort_terms"] == ["ARO:3003007"] and repeated["cohort_assertion_memberships"] == 2
    with pytest.raises(ValueError, match="outside the census"):
        audit.record_summary(census[1:], terms)
    with pytest.raises(ValueError, match="duplicate record"):
        audit.record_summary(census + census, terms)


def test_public_snapshot_covers_the_complement_without_freezing_live_records(monkeypatch):
    root = Path(__file__).resolve().parents[1]
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert not path.is_relative_to(root / "data/antibiotics")
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    result = json.loads((root / audit.OUTPUT).read_bytes())
    inputs = {}
    for key in ("direct", "definitions", "prior_literature", "term_scope", "census", "identity_review"):
        pin = result["inputs"][key]
        raw = (root / pin["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == pin["sha256"]
        inputs[key] = (list(csv.DictReader(raw.decode().splitlines(), delimiter="\t"))
                       if key == "census" else json.loads(raw))
    labels = {tid: row["labels"][0] for tid, row in inputs["direct"]["determinants"].items()}
    expected = audit.selection(inputs["direct"], inputs["definitions"], inputs["prior_literature"],
                               inputs["term_scope"], labels)
    assert set(result["terms"]) == set(expected) and len(expected) == 965
    reviews = audit.scope_reviews(root, result["inputs"]["term_scope"])
    assert result["inputs"]["identity_review"] == audit.IDENTITY_REVIEW
    for tid, row in result["terms"].items():
        for key in ("source_label_sha256", "definition_citation_ids", "record_memberships"):
            assert row[key] == expected[tid][key]
        assert row["source_entity_scope"] == expected[tid]["entity_scope"]
        assert row["entity_identity_review"] == reviews.get(tid)
        assert row["entity_scope"] == (reviews[tid]["entity_scope"] if tid in reviews
                                        else expected[tid]["entity_scope"])
        assert row["entity_scope_basis"] == ("REVIEWED_IDENTITY" if tid in reviews
                                              else "ONTOLOGY_ANCESTRY_ONLY")
        assert not row["no_match_establishes_biological_absence"]
        assert row["primary_review_status"].startswith("OPEN")
        if row["entity_scope"] in audit.NONPROTEIN:
            assert not row["reference_candidates"]
        for match in row["reference_candidates"]:
            assert match["protein_accession"] in result["proteins"]
            assert not match["experimental_identity_assigned"]
    pmids = {c.removeprefix("PMID:") for row in expected.values()
             for c in row["definition_citation_ids"] if c.startswith("PMID:")}
    assert set(result["queries"]) == pmids and len(pmids) == 825
    assert all(q["complete_for_query"] and not q["establishes_biological_absence"]
               for q in result["queries"].values())
    assert result["records"] == audit.record_summary(inputs["census"], result["terms"])
    assert len(result["records"]) == 2939
    assert {r["whole_record_primary_review"] for r in result["records"]} == {"OPEN"}
    for protein in result["proteins"].values():
        assert protein["taxonomy_identity_verified"]
        assert protein["reference_taxon_id"].startswith("NCBITaxon:")
        assert not protein["experimental_subject_assignment"] and not protein["exact_allele_assignment"]
