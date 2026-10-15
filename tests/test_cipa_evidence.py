"""An unavailable cipA paper cannot ground a homolog, protein or organism."""

import hashlib
import json
import socket
import sys
from pathlib import Path

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_cipa_evidence as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


@pytest.fixture
def metadata(monkeypatch):
    abstract = "Fixture describing distinct homologous enzyme classes."
    monkeypatch.setattr(audit, "ABSTRACT_SHA", hashlib.sha256(abstract.encode()).hexdigest())
    return {
        "hitCount": 1,
        "request": {
            "queryString": "EXT_ID:" + audit.PMID + " AND SRC:MED",
            "resultType": "CORE",
            "pageSize": 1,
        },
        "resultList": {
            "result": [
                {
                    **audit.PUBLICATION,
                    "id": audit.PMID,
                    "pmid": audit.PMID,
                    "source": "MED",
                    "abstractText": abstract,
                    "fullTextUrlList": {
                        "fullTextUrl": [
                            {"url": audit.ARTICLE, "availability": "Free", "documentStyle": "html"}
                        ]
                    },
                }
            ]
        },
    }


def test_metadata_neither_grounding_nor_access_denial(metadata):
    result = audit.project_metadata(metadata)
    assert result["isOpenAccess"] == "N" and result["inEPMC"] == "Y"
    assert result["literal_cipa_abstract_matches"] == 0
    for key in (
        "literal_nonmatch_establishes_absence",
        "cfr_or_rlmn_assigned_as_cipa",
        "primary_results_reviewed",
        "non_oa_flag_is_global_access_denial",
    ):
        assert result[key] is False
    assert "abstractText" not in result


@pytest.mark.parametrize("key,value", [("hitCount", True), ("hitCount", 2), ("nextCursorMark", "next")])
def test_metadata_completeness(metadata, key, value):
    metadata[key] = value
    with pytest.raises(ValueError, match="query scope"):
        audit.project_metadata(metadata)


@pytest.mark.parametrize(
    "key,value", [("queryString", "other"), ("pageSize", True), ("pageSize", 2), ("resultType", "lite")]
)
def test_metadata_query_identity(metadata, key, value):
    metadata["request"][key] = value
    with pytest.raises(ValueError, match="query scope"):
        audit.project_metadata(metadata)


@pytest.mark.parametrize(
    "key,value",
    [
        ("id", "1"),
        ("pmid", "1"),
        ("source", "PMC"),
        ("doi", "other"),
        ("pmcid", "PMC1"),
        ("title", "other"),
        ("pubYear", "2014"),
        ("abstractText", "changed"),
        ("isOpenAccess", "Y"),
        ("inEPMC", "N"),
    ],
)
def test_metadata_native_identity(metadata, key, value):
    metadata["resultList"]["result"][0][key] = value
    with pytest.raises(ValueError, match="publication identity"):
        audit.project_metadata(metadata)


@pytest.mark.parametrize("change", ["url", "availability", "format", "duplicate"])
def test_primary_route_bound_to_metadata(metadata, change):
    rows = metadata["resultList"]["result"][0]["fullTextUrlList"]["fullTextUrl"]
    if change == "duplicate":
        rows.append(dict(rows[0]))
    else:
        key, value = {
            "url": ("url", "https://example.org/"),
            "availability": ("availability", "Subscription required"),
            "format": ("documentStyle", "pdf"),
        }[change]
        rows[0][key] = value
    with pytest.raises(ValueError, match="primary route"):
        audit.project_metadata(metadata)


def test_new_literal_abstract_mention_requires_review(metadata, monkeypatch):
    row = metadata["resultList"]["result"][0]
    row["abstractText"] += " CipA"
    monkeypatch.setattr(audit, "ABSTRACT_SHA", hashlib.sha256(row["abstractText"].encode()).hexdigest())
    with pytest.raises(ValueError, match="new literal"):
        audit.project_metadata(metadata)


@pytest.fixture
def held(monkeypatch):
    payload = b"<html><head><title>Just a moment...</title></head><body>Challenge fixture</body></html>"
    monkeypatch.setitem(audit.BODY_SHA, "primary", hashlib.sha256(payload).hexdigest())
    receipt = {
        "url": audit.ARTICLE,
        "status": 403,
        "headers": {"CF-Mitigated": "challenge"},
        "retry_performed": False,
        "redirects_followed": False,
    }
    return receipt, payload


def test_challenge_never_becomes_primary_or_biological_negative(held):
    result = audit.project_hold(*held)
    assert result["http_status"] == 403
    assert result["revisit_requires"] == "USER_SUPPLIED_PRIMARY_COPY_OR_NEW_EXPLICIT_DIRECTION"
    for key in (
        "retrieved_primary_text",
        "challenge_treated_as_primary",
        "primary_results_reviewed",
        "retry_performed",
        "alternate_route_used",
        "hold_is_biological_negative_result",
        "metadata_free_flag_overrules_denial",
        "global_paywall_or_permanent_unavailability_inferred",
    ):
        assert result[key] is False


@pytest.mark.parametrize(
    "change", ["url", "status", "retry", "redirect", "header", "body", "title", "citation"]
)
def test_hold_identity_and_content_pinned(held, monkeypatch, change):
    receipt, payload = held
    if change in ("url", "status", "retry", "redirect"):
        key, value = {
            "url": ("url", "https://example.org/"),
            "status": ("status", 200),
            "retry": ("retry_performed", True),
            "redirect": ("redirects_followed", True),
        }[change]
        receipt[key] = value
    elif change == "header":
        receipt["headers"].clear()
    elif change == "body":
        payload += b" "
    else:
        payload = (
            payload.replace(b"Just a moment...", b"Primary")
            if change == "title"
            else payload.replace(b"</head>", b'<meta name="citation_doi" content="other"></head>')
        )
        monkeypatch.setitem(audit.BODY_SHA, "primary", hashlib.sha256(payload).hexdigest())
    with pytest.raises(ValueError):
        audit.project_hold(receipt, payload)


@pytest.fixture
def request_cache(tmp_path, monkeypatch):
    def save(name, data):
        path = tmp_path / name
        path.write_text(json.dumps(data, sort_keys=True) + "\n")
        return audit.reference.pin(tmp_path, path)

    cohort = save("cohort.json", {})
    specs = [
        ("metadata-" + audit.PMID, "metadata-plan.json", audit.metadata_url(), 200),
        ("primary", "primary-plan.json", audit.ARTICLE, 403),
    ]
    sources = {}
    for i, (key, filename, url, status) in enumerate(specs):
        plan = save(
            filename,
            {
                "cohort": cohort,
                "requests": {key: {"url": url}},
                "automatic_redirects": False,
                "retry_performed": False,
                "ncbi_requests": 0,
            },
        )
        monkeypatch.setitem(audit.PLAN_SHA, filename, plan["sha256"])
        body = save(key + "-response.bin", {})
        monkeypatch.setitem(audit.BODY_SHA, key, body["sha256"])
        attempt = save(
            key + "-attempt.json",
            {
                "url": url,
                "plan_sha256": plan["sha256"],
                "started_at": f"2026-10-15T07:00:0{i * 2}+00:00",
                "retry_performed": False,
            },
        )
        receipt = save(
            key + "-receipt.json",
            {
                "url": url,
                "status": status,
                "sha256": body["sha256"],
                "bytes": (tmp_path / body["path"]).stat().st_size,
                "retrieved_at": f"2026-10-15T07:00:0{i * 2 + 1}+00:00",
                "retry_performed": False,
                "redirects_followed": False,
            },
        )
        sources[key] = {"plan": plan, "body": body, "attempt": attempt, "receipt": receipt}
    save(
        "metadata-canary-review.json",
        {
            **sources["metadata-" + audit.PMID],
            "identity_checked": True,
            "primary_results_reviewed": False,
            "cfr_homology_is_cipa_identity": False,
        },
    )
    return tmp_path, save


def test_request_replay_without_ignored_cache(request_cache):
    root, _ = request_cache
    sources = audit.request_context(root, root)
    assert len(sources) == 2 and sources["primary"]["status"] == 403


@pytest.mark.parametrize(
    "change", ["alternate", "plan", "body", "canary", "chronology", "redirect", "retry", "status", "bytes"]
)
def test_request_tampering_fails_closed(request_cache, change):
    root, save = request_cache
    if change == "alternate":
        save("alternate-attempt.json", {})
    elif change == "plan":
        save("primary-plan.json", {})
    elif change == "body":
        save("primary-response.bin", {"changed": True})
    elif change == "canary":
        row = json.loads((root / "metadata-canary-review.json").read_bytes())
        row["cfr_homology_is_cipa_identity"] = True
        save("metadata-canary-review.json", row)
    else:
        row = json.loads((root / "primary-receipt.json").read_bytes())
        key, value = {
            "chronology": ("retrieved_at", "2026-10-15T06:00:00+00:00"),
            "redirect": ("redirects_followed", True),
            "retry": ("retry_performed", True),
            "status": ("status", 200),
            "bytes": ("bytes", 1),
        }[change]
        row[key] = value
        save("primary-receipt.json", row)
    with pytest.raises(ValueError):
        audit.request_context(root, root)


def test_cli_no_overwrite(tmp_path, monkeypatch):
    output = tmp_path / "output.json"
    monkeypatch.setattr(audit, "OUTPUT", output)
    monkeypatch.setattr(audit, "build", lambda root: {"result": 1})
    monkeypatch.setattr(sys, "argv", ["audit", "--check"])
    with pytest.raises(FileNotFoundError):
        audit.main()
    monkeypatch.setattr(sys, "argv", ["audit"])
    audit.main()
    audit.main()
    output.write_text("old\n")
    with pytest.raises(ValueError, match="does not reproduce"):
        audit.main()
    assert output.read_text() == "old\n"


def test_saved_claims_preserve_prior_memberships_and_scope():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    index = json.loads((ROOT / result["inputs"]["index"]["path"]).read_bytes())
    expected = [
        {
            "record_identifier": c["record_identifier"],
            "position": c["resistance_index"],
            "aro_id": c["aro_id"],
            "claim_sha256": c["claim_sha256"],
        }
        for c in index["claims"]
        if c["aro_id"] == audit.TERM
    ]

    def order(claim):
        return claim["record_identifier"], claim["position"]

    assert sorted(result["claims"], key=order) == sorted(expected, key=order)
    assert result["source_term"] == index["terms"][audit.TERM]
    assert len(result["records"]) == len(result["claims"]) == 10
    for key in (
        "protein_accession_assigned",
        "taxon_id_assigned",
        "strain_taxon_id_assigned",
        "experimental_allele_assigned",
        "experimental_genome_assigned",
    ):
        assert result["disposition"][key] is None
    assert result["summary"]["biological_records_changed"] == 0
    assert result["constraints"]["ncbi_requests"] == 0
    assert result["constraints"]["issue_1040"] == "DEFERRED"
    assert result["constraints"]["full_corpus_goal_status"] == "OPEN"
