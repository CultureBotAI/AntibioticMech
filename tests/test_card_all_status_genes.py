"""All entry statuses and every cursor page remain reference-only evidence."""

import builtins
import io
import json
import socket
import sys
from pathlib import Path
from urllib.parse import urlencode

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_all_status_genes as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("offline audit attempted network")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket.socket, "connect_ex", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


def save(root, path, value):
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value))
    return audit.reference.pin(root, target)


def chain_fixture(root, mutation=None, count=501):
    params = {
        "query": "(gene_exact:foo) AND taxonomy_id:1",
        "format": "json",
        "size": "500",
        "sort": "accession asc",
        "fields": audit.prior.FIELDS,
    }
    url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(params)
    item = {"parameters": params, "url": url}
    plan = {
        "requests": {"proteins-1": item},
        "cache_directory": "cache",
        "page_size": 500,
        "max_pages_per_query": 20,
        "max_results_per_query": 10000,
        "max_response_bytes": 10000000,
        "release": "2026_03",
    }
    if mutation == "page_limit":
        plan["max_pages_per_query"] = 1
    pin = save(root, audit.PLAN, plan)
    for page in range(1, max(1, (count + 499) // 500) + 1):
        request = params if page == 1 else {**params, "cursor": "cursor-" + str(page)}
        page_url = audit.page_url(item, request, page)
        prefix = f"cache/proteins-1-page-{page:04d}"
        attempt = {
            "plan": pin,
            "key": "proteins-1",
            "page": page,
            "url": page_url,
            "retries": 0,
            "redirects_followed": 0,
        }
        rows = [
            {
                "primaryAccession": f"A{i:05d}",
                "entryType": (
                    "UniProtKB reviewed (Swiss-Prot)" if i % 2 else "UniProtKB unreviewed (TrEMBL)"
                ),
                "genes": [{"geneName": {"value": "foo"}}],
            }
            for i in range((page - 1) * 500, min(page * 500, count))
        ]
        if page == 1 and mutation in {"sequence", "features", "comments"}:
            rows[0][mutation] = []
        elif page == 1 and mutation == "entry_type":
            rows[0]["entryType"] = "unknown"
        elif page == 2 and mutation == "duplicate":
            rows[0]["primaryAccession"] = "A00000"
        elif page == 2 and mutation == "short_page":
            rows = []
        body = save(root, prefix + "-body.json", {"results": rows})
        headers = {"x-uniprot-release": "2026_03", "x-total-results": str(count)}
        if page * 500 < count:
            next_params = {**params, "cursor": "cursor-" + str(page + 1)}
            if mutation == "cursor_cycle" and page == 2:
                next_params["cursor"] = "cursor-2"
            elif mutation == "query_drift":
                next_params["query"] = "(gene_exact:bar) AND taxonomy_id:1"
            next_url = "https://rest.uniprot.org/uniprotkb/search?" + urlencode(next_params)
            if mutation == "offsite":
                next_url = next_url.replace("rest.uniprot.org", "example.org")
            headers["link"] = f'<{next_url}>; rel="next"'
        receipt = {
            "url": page_url,
            "status": 200,
            "retries": 0,
            "redirects_followed": 0,
            "headers": headers,
            "body": body,
            "bytes": (root / body["path"]).stat().st_size,
            "retrieved_at": "2026-10-15T00:00:00Z",
        }
        if page == 1:
            if mutation == "status":
                receipt["status"] = 503
            elif mutation == "release":
                headers["x-uniprot-release"] = "2026_04"
            elif mutation == "location":
                headers["location"] = "https://example.org"
            elif mutation == "retry":
                receipt["retries"] = 1
            elif mutation == "redirect":
                attempt["redirects_followed"] = 1
            elif mutation == "attempt":
                attempt["key"] = "proteins-2"
            elif mutation == "size_limit":
                headers["x-total-results"] = "10001"
            elif mutation == "bytes":
                receipt["bytes"] += 1
            elif mutation == "missing_link":
                headers.pop("link", None)
            elif mutation == "body_path":
                receipt["body"] = save(root, "other.json", {"results": rows})
        elif mutation == "total_drift":
            headers["x-total-results"] = str(count + 1)
        save(root, prefix + "-attempt.json", attempt)
        save(root, prefix + "-receipt.json", receipt)
    if mutation == "orphan":
        save(root, "cache/proteins-1-page-9999-body.json", {})
    elif mutation == "error":
        save(root, "cache/proteins-1-error.json", {"error": "failure"})
    return plan


def test_complete_chain_preserves_reviewed_and_unreviewed_entries(tmp_path):
    entries, provenance = audit.read_chain(tmp_path, chain_fixture(tmp_path), "proteins-1")
    assert len(entries) == provenance["result_count"] == 501
    assert len(provenance["pages"]) == 2 and provenance["complete_for_query"]
    assert provenance["entry_type_counts"] == {
        "UniProtKB reviewed (Swiss-Prot)": 250,
        "UniProtKB unreviewed (TrEMBL)": 251,
    }
    assert not provenance["empty_result_means_biological_absence"]


def test_complete_empty_query_is_not_biological_absence(tmp_path):
    entries, provenance = audit.read_chain(tmp_path, chain_fixture(tmp_path, count=0), "proteins-1")
    assert entries == {} and provenance["complete_for_query"] and provenance["result_count"] == 0
    assert not provenance["empty_result_means_biological_absence"]


@pytest.mark.parametrize(
    "mutation",
    [
        "page_limit",
        "sequence",
        "features",
        "comments",
        "entry_type",
        "duplicate",
        "short_page",
        "query_drift",
        "offsite",
        "status",
        "release",
        "location",
        "retry",
        "redirect",
        "attempt",
        "size_limit",
        "bytes",
        "missing_link",
        "body_path",
        "total_drift",
        "orphan",
        "error",
    ],
)
def test_incomplete_or_changed_cursor_chains_fail_closed(tmp_path, mutation):
    with pytest.raises(ValueError):
        audit.read_chain(tmp_path, chain_fixture(tmp_path, mutation), "proteins-1")


def test_cursor_cycle_does_not_repeat_a_request(tmp_path):
    with pytest.raises(ValueError, match="cursor cycle"):
        audit.read_chain(tmp_path, chain_fixture(tmp_path, "cursor_cycle", count=1001), "proteins-1")


def result():
    return json.loads((ROOT / audit.OUTPUT).read_bytes())


def test_portable_partition_preserves_all_remaining_terms_and_claims(monkeypatch):
    original = Path.open

    def guarded(path, *args, **kwargs):
        assert "/reports/" not in str(path) and "/data/antibiotics/" not in str(path)
        return original(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded)
    d = result()
    prior = audit.read_json(ROOT, d["prior"])
    remaining = {t for t, r in prior["terms"].items() if not r["qualified_reference_accessions"]}
    assert set(d["terms"]) | set(d["name_unresolved_terms"]) == remaining
    assert not set(d["terms"]) & set(d["name_unresolved_terms"])
    assert len(remaining) == 90 and len(d["terms"]) == 54 and len(d["name_unresolved_terms"]) == 36
    assert d["claims"] == [c for c in prior["claims"] if c["aro_id"] in d["terms"]]
    assert len(d["claims"]) == 85 and len(d["records"]) == 56
    for term, row in d["terms"].items():
        assert row["record_memberships"] == sorted(
            {c["record_identifier"] for c in d["claims"] if c["aro_id"] == term}
        )
        assert row["source_label"] == prior["terms"][term]["source_label"]
        assert row["whole_record_primary_review"] == "OPEN" and not row["biological_absence_inferred"]


def test_reviewed_filter_is_removed_without_excluding_unresolved_names():
    d = result()
    plan = audit.read_json(ROOT, d["plan"])
    assert plan["entry_status_filter"] is None
    assert len(plan["requests"]) == 31 and set(plan["reused_queries"]) == {"proteins-5478"}
    assert all("reviewed:" not in q["parameters"]["query"] for q in plan["requests"].values())
    assert d["summary"]["entry_type_counts"] == {"UniProtKB unreviewed (TrEMBL)": 13}
    assert sum(q["result_count"] == 0 for q in d["queries"].values()) == 23
    assert all(q["complete_for_query"] for q in d["queries"].values())
    assert d["limits"]["all_possible_gene_aliases_or_alleles_searched"] is False


def test_cached_superset_is_not_requeried_or_renamed():
    d = result()
    plan = audit.read_json(ROOT, d["plan"])
    row = plan["reused_queries"]["proteins-5478"]
    assert row["symbols"] == ["yor1"]
    assert (
        row["native_parameters"]["query"]
        == "(gene_exact:YOR1 OR gene_exact:CAGL0G00242g) AND taxonomy_id:5478"
    )
    assert d["queries"]["proteins-5478"]["reused"]
    assert d["queries"]["proteins-5478"]["result_count"] == 1
    for term in ("ARO:3009466", "ARO:3009467", "ARO:3009468"):
        assert d["terms"][term]["qualified_reference_accessions"] == ["UniProtKB:Q6FTR9"]


def test_all_candidate_links_need_native_fields_and_verified_species():
    d = result()
    for row in d["terms"].values():
        source = d["source_bindings"][row["tokens"]["species"]]["identity"]
        for c in row["reference_candidates"]:
            view = d["reference_views"][c["protein_accession"]]
            assert c["literal_native_fields"] and all(
                m["value"].casefold() == row["tokens"]["gene"].casefold() for m in c["literal_native_fields"]
            )
            assert c["disposition"] == audit.prior.disposition(source, view["reference_taxonomy"]["species"])
            assert c["qualified_reference"] is (c["disposition"] == audit.prior.QUALIFIED)
            assert not c["exact_allele_assignment"] and not c["experimental_subject_assignment"]
            bibliography = {
                "PMID:" + i["id"]
                for b in view["native_bibliography"]
                for i in b["identifiers"]
                if i["database"] == "PubMed"
            }
            assert c["own_definition_citation_overlap"] == sorted(
                bibliography & set(row["definition_citations"])
            )
            assert not c["citation_overlap_is_primary_validation"]
        assert row["qualified_reference_accessions"] == [
            c["protein_accession"] for c in row["reference_candidates"] if c["qualified_reference"]
        ]


def test_ordered_locus_remains_distinct_from_gene_name_and_allele():
    d = result()
    view = d["reference_views"]["UniProtKB:I6YDN6"]
    assert view["gene_symbols"] == ["pepQ"]
    assert "Rv2535c" in view["ordered_locus_names"]
    for term in ("ARO:3007692", "ARO:3009335"):
        row = d["terms"][term]
        assert row["qualified_reference_accessions"] == ["UniProtKB:I6YDN6"]
        (candidate,) = row["reference_candidates"]
        assert candidate["match_kind"] == "ORDERED_LOCUS_REFERENCE_NOT_GENE_RENAMING"
        assert all("orderedLocusNames" in m["field"] for m in candidate["literal_native_fields"])
    assert not view["exact_allele_assignment"]


def test_no_experimental_or_operational_fields_are_promoted():
    d = result()
    for view in d["reference_views"].values():
        assert not view["experimental_subject_assignment"] and not view["exact_allele_assignment"]
        assert view["experimental_genome_assignment"] is None and not view["new_primary_results_review"]
    assert d["limits"]["ncbi_requests"] == 0 and d["limits"]["issue_1040"] == "DEFERRED"
    assert d["limits"]["full_corpus_goal_status"] == "OPEN"

    def keys(value):
        if isinstance(value, dict):
            for key, child in value.items():
                yield key
                yield from keys(child)
        elif isinstance(value, list):
            for child in value:
                yield from keys(child)

    assert not set(keys(d)) & {"sequence", "features", "comments", "variants", "alteration", "mic", "primers"}


def test_multiple_fragment_references_are_not_collapsed_or_treated_as_complete():
    d = result()
    refs = d["terms"]["ARO:3009446"]["qualified_reference_accessions"]
    assert refs == ["UniProtKB:A0A0K2GUW8", "UniProtKB:Q9P8V2"]
    assert all(d["reference_views"][a]["native_protein_flag"] == "Fragment" for a in refs)
    assert all(not d["reference_views"][a]["unflagged_means_complete"] for a in refs)
    assert len(d["reference_views"]) == 13
    assert sum(bool(r["qualified_reference_accessions"]) for r in d["terms"].values()) == 12
    assert sum(len(r["qualified_reference_accessions"]) for r in d["terms"].values()) == 16
    assert sum(len(r["qualified_reference_accessions"]) > 1 for r in d["terms"].values()) == 4


def test_cli_creates_parent_without_overwriting_prior_output(tmp_path, monkeypatch):
    monkeypatch.setattr(audit, "build", lambda _: {"summary": {}})
    argv = ["audit", "--root", str(tmp_path), "--output", "nested/output.json"]
    monkeypatch.setattr(sys, "argv", argv)
    audit.main()
    path = tmp_path / "nested/output.json"
    before = path.stat().st_mtime_ns
    audit.main()
    assert path.stat().st_mtime_ns == before
    path.write_bytes(b"prior artifact\n")
    for args in (argv, argv + ["--check"]):
        monkeypatch.setattr(sys, "argv", args)
        with pytest.raises(ValueError, match="preserve prior output"):
            audit.main()
        assert path.read_bytes() == b"prior artifact\n"


def test_offline_replay_is_read_only(monkeypatch, pre_cdsa_qualification_root):
    d = result()
    required = [p["receipt"]["path"] for q in d["queries"].values() if "pages" in q for p in q["pages"]]
    if not all((ROOT / p).exists() for p in required):
        pytest.skip("ignored native sources unavailable; portable tests still run")

    def guard(original):
        def read_only(file, mode="r", *args, **kwargs):
            assert not any(c in mode for c in "wax+"), "audit attempted file mutation"
            return original(file, mode, *args, **kwargs)

        return read_only

    monkeypatch.setattr(builtins, "open", guard(builtins.open))
    monkeypatch.setattr(io, "open", guard(io.open))
    assert audit.build(pre_cdsa_qualification_root) == d
