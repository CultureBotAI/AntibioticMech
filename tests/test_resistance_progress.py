"""A completed search or identifier decision cannot complete a biological review."""

import copy
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import summarize_resistance_progress as progress  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def discovery():
    records, documents, planned, searched, expanded = {}, {}, [], [], []
    for number in (1, 2):
        identifier = f"CHEBI:{number}"
        doc = {"identifier": identifier, "label": "shared name"}
        record = {"identifier": identifier, "label": doc["label"],
                  "path": f"data/antibiotics/{number}.yaml", "class": "ANTIBACTERIAL",
                  "standard_inchi_key": f"KEY{number}", "sha256": "new"}
        records[identifier], documents[identifier] = record, doc
        names = progress.record_names(doc)
        names[0]["shared_with_record_ids"] = [f"CHEBI:{3-number}"]
        queries = progress.make_queries(names)
        old = {**record, "sha256": "old", "names": names, "queries": queries}
        planned.append(old)
        searched.append({**old, "queries": [
            {**queries[0], "hit_count": 101, "status": "TRUNCATED_REFINEMENT_REQUIRED"}],
            "searched_queries": 1, "search_status": "ALL_INITIAL_NAME_QUERIES_SEARCHED",
            "primary_review_status": "PENDING"})
        expanded.append({"identifier": identifier, "query_id": "0",
                         "query_key": progress.digest(queries[0]["query"].encode()),
                         "status": "CURSOR_TRAVERSAL_COMPLETE", "primary_review_status": "PENDING",
                         "hit_count": "102", "retained_citations": "102", "pages": "1"})
    return records, documents, {"records": planned, "corpus_sha256": "historical"}, {
        "records": searched, "corpus_sha256": "historical"}, expanded


def test_historical_hashes_and_shared_searches_do_not_merge_compounds(discovery):
    rows = progress.discovery_progress(*discovery)
    assert set(rows) == {"CHEBI:1", "CHEBI:2"}
    assert all(r["expanded_query_memberships"] == 1 for r in rows.values())
    assert all(r["record_changed_since_name_search"] for r in rows.values())
    assert all(r["name_search_status"].endswith("NOT_PRIMARY_REVIEW") for r in rows.values())
    assert discovery[2]["records"][0]["sha256"] == "old"


@pytest.mark.parametrize("change", [
    "missing_record", "duplicate_record", "structure", "new_alias", "origin", "query",
    "initial_scope", "initial_count", "historical_census", "missing_expansion", "duplicate_expansion",
    "extra_expansion", "incomplete", "count_conflict", "shared_conflict", "query_key", "review_promotion",
])
def test_discovery_drift_is_not_silently_accepted(discovery, change):
    records, docs, plan, initial, expanded = discovery
    if change == "missing_record":
        plan["records"].pop()
    elif change == "duplicate_record":
        plan["records"].append(plan["records"][0])
    elif change == "structure":
        records["CHEBI:1"]["standard_inchi_key"] = "different"
    elif change == "new_alias":
        docs["CHEBI:1"]["synonyms"] = [{"synonym_text": "new name"}]
    elif change == "origin":
        plan["records"][0]["names"][0]["origins"] = []
    elif change == "query":
        plan["records"][0]["queries"][0]["query"] = "different"
    elif change == "initial_scope":
        initial["records"][0]["search_status"] = "PENDING"
    elif change == "initial_count":
        initial["records"][0]["queries"][0]["hit_count"] = -1
    elif change == "historical_census":
        initial["corpus_sha256"] = "different"
    elif change == "missing_expansion":
        expanded.pop()
    elif change == "duplicate_expansion":
        expanded.append(expanded[0])
    elif change == "extra_expansion":
        expanded.append({**expanded[0], "identifier": "CHEBI:3"})
    elif change == "incomplete":
        expanded[0]["status"] = "CURSOR_CONFLICT_REQUIRES_RESTART"
    elif change == "count_conflict":
        expanded[0]["retained_citations"] = "1"
    elif change == "shared_conflict":
        expanded[0]["pages"] = "2"
    elif change == "query_key":
        expanded[0]["query_key"] = "wrong"
    else:
        expanded[0]["primary_review_status"] = "COMPLETE"
    with pytest.raises(ValueError):
        progress.discovery_progress(records, docs, plan, initial, expanded)


def test_empty_search_is_not_biological_absence(discovery):
    records, docs, plan, initial, _ = discovery
    for record in initial["records"]:
        record["queries"][0].update(hit_count=0, status="NO_HITS_IN_LIMITED_QUERY")
    rows = progress.discovery_progress(records, docs, plan, initial, [])
    assert all(r["expanded_query_memberships"] == 0 for r in rows.values())
    assert all(r["name_search_status"].endswith("NOT_PRIMARY_REVIEW") for r in rows.values())


@pytest.fixture
def card(monkeypatch):
    monkeypatch.setattr(progress, "is_card_sourced", lambda item: item.get("source") == "CARD")
    claims = [{"aro_id": "ARO:1", "label": "reference term", "source": "CARD"},
              {"aro_id": "ARO:2", "label": "unlinked term", "source": "CARD"}]
    record = {"identifier": "CHEBI:1", "label": "compound", "path": "one.yaml",
              "standard_inchi_key": "KEY", "resistance_mechanisms": claims}
    candidate = {"accession": "UniProtKB:P00001", "reference_taxon_id": "NCBITaxon:1",
                 "card_cross_reference": {"database": "CARD", "id": "ARO:1"},
                 "evidence_scope": "EXPLICIT_REFERENCE_LINK_NOT_EXPERIMENTAL_ALLELE_GROUNDING"}
    audit = {"determinants": {
        "ARO:1": {"candidates": [candidate], "primary_review_status": "PENDING"},
        "ARO:2": {"candidates": [], "primary_review_status": "PENDING"}},
        "summary": {"card_assertions": 2}}
    ledger = [{**{k: record[k] for k in progress.IDENTITY[:-1]}, "aro_id": m["aro_id"],
               "determinant_label": m["label"]} for m in claims]
    return {"CHEBI:1": record}, audit, ledger


def test_card_references_are_explicit_and_unlinked_terms_are_retained(card):
    row = progress.card_progress(*card)["CHEBI:1"]
    assert row["card_distinct_terms"] == 2
    assert row["card_terms_with_reference_candidates"] == 1
    assert row["card_terms_without_explicit_reference_link"] == 1
    assert row["card_reference_accessions"] == "UniProtKB:P00001"
    assert "protein_accession" not in row and "taxon_id" not in row


@pytest.mark.parametrize("change", ["link", "scope", "duplicate", "missing_term", "extra_term", "member"])
def test_card_drift_rejected(card, change):
    records, audit, ledger = card
    candidate = audit["determinants"]["ARO:1"]["candidates"][0]
    if change == "link":
        candidate["card_cross_reference"]["id"] = "ARO:2"
    elif change == "scope":
        candidate["evidence_scope"] = "EXPERIMENTAL"
    elif change == "duplicate":
        audit["determinants"]["ARO:1"]["candidates"].append(copy.deepcopy(candidate))
    elif change == "missing_term":
        del audit["determinants"]["ARO:2"]
    elif change == "extra_term":
        audit["determinants"]["ARO:3"] = audit["determinants"]["ARO:2"]
    else:
        ledger[0]["identifier"] = "CHEBI:2"
    with pytest.raises(ValueError):
        progress.card_progress(records, audit, ledger)


def test_phi_counts_identifier_decisions_not_experiments():
    rows = [{"identifier": "CHEBI:1", "pmid": "1", "row": "a"},
            {"identifier": "CHEBI:1", "pmid": "1", "row": "b"}]
    records = {"CHEBI:1": {"resistance_mechanisms": [{"source": "PHIBASE"}] * 2},
               "CHEBI:2": {"resistance_mechanisms": []}}
    reviews = {progress.row_digest(rows[0]): {"review_id": "identifier-only"}}
    result = progress.phi_progress(records, rows, reviews)
    assert result["CHEBI:1"]["phi_identifier_scoped_associations"] == 1
    assert result["CHEBI:1"]["phi_identifier_review_pending"] == 1
    assert result["CHEBI:1"]["phi_identifier_review_pending_pmids"] == "PMID:1"
    assert result["CHEBI:2"]["phi_source_associations"] == 0
    records["CHEBI:1"]["resistance_mechanisms"].pop()
    with pytest.raises(ValueError, match="assertion count"):
        progress.phi_progress(records, rows, reviews)


@pytest.mark.parametrize("change", ["rule", "region", "scope", "membership"])
def test_hivdb_identity_drift_is_not_a_completed_allele_review(change):
    record = {"identifier": "CHEBI:1", "label": "compound", "path": "one.yaml",
              "standard_inchi_key": "KEY", "score_rules": [
                  {"source": "HIVDB_HIVFACTS", "source_rule_id": "rule", "gene": "RT"}]}
    reference = {**{k: record[k] for k in progress.IDENTITY[:-1]},
                 "primary_review_status": "PENDING", "source_rule_ids": ["rule"],
                 "region_rule_counts": {"RT": 1}, "pathogen_taxon_id": "NCBITaxon:11676",
                 "status": "SOURCE_REGION_AND_TAXON_VERIFIED_NOT_EXPERIMENTAL_ALLELES"}
    audit = {"records": [reference]}
    assert progress.hivdb_progress({"CHEBI:1": record}, audit)["CHEBI:1"] == {
        "hivdb_source_rules": 1, "hivdb_reference_taxon": "NCBITaxon:11676"}
    if change == "rule":
        reference["source_rule_ids"] = ["different"]
    elif change == "region":
        reference["region_rule_counts"] = {"PR": 1}
    elif change == "scope":
        reference["primary_review_status"] = "COMPLETE"
    else:
        reference["identifier"] = "CHEBI:2"
    with pytest.raises(ValueError):
        progress.hivdb_progress({"CHEBI:1": record}, audit)


@pytest.mark.parametrize("change", ["ignored_addition", "hash", "duplicate", "evidence"])
def test_census_checks_current_records_including_ignored_files(tmp_path, monkeypatch, change):
    path = tmp_path / "data/antibiotics/one.yaml"
    path.parent.mkdir(parents=True)
    doc = {"identifier": "CHEBI:1", "label": "compound", "antimicrobial_class": "ANTIBACTERIAL",
           "chemical_structure": {"standard_inchi_key": "KEY"}}
    path.write_text(json.dumps(doc))
    monkeypatch.setattr(progress, "load_record", lambda path: json.loads(path.read_bytes()))
    record = {"identifier": "CHEBI:1", "label": "compound", "class": "ANTIBACTERIAL",
              "path": str(path.relative_to(tmp_path)), "standard_inchi_key": "KEY",
              "record_sha256": progress.digest(path.read_bytes()),
              "resistance_assertions": "0", "score_rules": "0", "activity_observations": "0"}
    census = [record]
    assert set(progress.current_records(tmp_path, census)[0]) == {"CHEBI:1"}
    if change == "ignored_addition":
        (tmp_path / ".gitignore").write_text("data/antibiotics/.ignored/\n")
        hidden = path.parent / ".ignored"
        hidden.mkdir()
        (hidden / "extra.yaml").write_text(path.read_text())
    elif change == "hash":
        path.write_text(path.read_text() + "\n")
    elif change == "duplicate":
        census.append(record)
    else:
        record["activity_observations"] = "1"
    with pytest.raises(ValueError):
        progress.current_records(tmp_path, census)


def test_live_offline_export_reproduces_and_preserves_review_boundaries(monkeypatch):
    import requests

    def forbidden(*args, **kwargs):
        pytest.fail("progress index must not contact any service")

    monkeypatch.setattr(requests.sessions.Session, "request", forbidden)
    rows, descriptor = progress.build(ROOT)
    tsv, metadata = progress.render(rows, descriptor)
    assert tsv == (ROOT / (progress.PREFIX + ".tsv")).read_bytes()
    assert metadata == (ROOT / (progress.PREFIX + ".json")).read_bytes()
    assert len(rows) == 2939 == len({r["identifier"] for r in rows})
    summary = descriptor["summary"]
    assert summary["recorded_names_searched"] == 16030
    assert summary["initial_query_memberships"] == 7469
    assert summary["expanded_query_memberships"] == 612
    assert summary["expanded_distinct_queries"] == 611
    assert summary["card_terms_with_reference_candidates"] == 978
    assert summary["card_terms_without_explicit_reference_link"] == 1024
    assert summary["phi_identifier_scoped_associations"] == 185
    assert summary["phi_identifier_review_pending"] == 32
    assert summary["hivdb_source_rules"] == 467
    assert {r["whole_record_primary_review"] for r in rows} == {"OPEN"}
    assert descriptor["scope"] == progress.SCOPE
    assert descriptor["reference_attribution"]["source"].startswith("UniProt Consortium")
    assert descriptor["reference_attribution"]["license"] == "CC BY 4.0"
    assert descriptor["card_reference_releases"] == ["2026_03"]
    assert all(not item["path"].startswith("reports/") for item in descriptor["inputs"].values())
    assert "Individual paper dossiers" in " ".join(descriptor["limitations"])
    assert not {"alteration", "sequence", "mic", "variants", "protein_accession", "taxon_id"} & rows[0].keys()
    assert json.loads(metadata)["ledger"]["sha256"] == progress.digest(tsv)
