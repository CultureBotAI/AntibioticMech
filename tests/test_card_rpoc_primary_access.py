"""Access responses cannot become biological evidence or leak redirect values."""

import hashlib
import json
import socket
import sys
from pathlib import Path
from urllib.parse import urlencode

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_card_rpoc_primary_access as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("network forbidden in access replay")

    monkeypatch.setattr(requests.sessions.Session, "request", forbidden)
    monkeypatch.setattr(socket.socket, "connect", forbidden)
    monkeypatch.setattr(socket, "create_connection", forbidden)


def redirected_receipt():
    return {
        "status": 302,
        "redirects_followed": False,
        "manual_redirect_continuation": True,
        "credentials_supplied": False,
        "headers": {
            "Location": "https://idp.nature.com/transit?"
            + urlencode({"redirect_uri": audit.ARTICLE, "code": "private-test-code-not-for-export"})
        },
    }


def test_redirect_is_unresolved_not_access_denial_or_primary_evidence():
    result = audit.redirect_context(redirected_receipt())
    assert result["status"] == "UNRESOLVED_PUBLISHER_REDIRECT_FLOW"
    assert result["primary_results_reviewed"] is result["article_obtained"] is False
    assert result["access_denial_or_paywall_inferred"] is False
    assert result["unfollowed_destination_path"] == "/transit"
    assert result["manual_redirect_requests"] == 1
    assert "private-test-code" not in json.dumps(result)
    assert "redirect_uri=" not in json.dumps(result)


@pytest.mark.parametrize(
    "change",
    [
        "status",
        "automatic_redirect",
        "not_manual",
        "credentials",
        "missing_location",
        "duplicate_location",
        "different_host",
        "different_path",
        "wrong_article",
        "empty_code",
        "duplicate_code",
        "fragment",
    ],
)
def test_changed_redirect_scope_fails_closed(change):
    receipt = redirected_receipt()
    if change == "status":
        receipt["status"] = 200
    elif change == "automatic_redirect":
        receipt["redirects_followed"] = True
    elif change == "not_manual":
        receipt["manual_redirect_continuation"] = False
    elif change == "credentials":
        receipt["credentials_supplied"] = True
    elif change == "missing_location":
        receipt["headers"] = {}
    elif change == "duplicate_location":
        receipt["headers"]["location"] = receipt["headers"]["Location"]
    else:
        value = receipt["headers"]["Location"]
        if change == "different_host":
            value = value.replace("idp.nature.com", "other.example")
        elif change == "different_path":
            value = value.replace("/transit?", "/login?")
        elif change == "wrong_article":
            value = value.replace("33731-1", "99999-1")
        elif change == "empty_code":
            value = value.replace("private-test-code-not-for-export", "")
        elif change == "duplicate_code":
            value += "&code=second"
        elif change == "fragment":
            value += "#unexpected"
        receipt["headers"]["Location"] = value
    with pytest.raises(ValueError):
        audit.redirect_context(receipt)


def write_json(path, value):
    path.write_text(json.dumps(value), encoding="utf-8")


@pytest.fixture
def history(tmp_path):
    bibliography = {
        "23208709": {"pmid": "23208709", "pmcid": "PMC3553702", "doi": "10.1128/aac.01541-12"},
        "30337678": {"pmid": "30337678", "pmcid": "PMC6194142", "doi": "10.1038/s41598-018-33731-1"},
    }
    cohort = {"bibliography": bibliography}
    write_json(tmp_path / "cohort.json", cohort)

    def pin(name):
        return audit.reference.pin(tmp_path, tmp_path / name)

    requests_by_id = {
        "article-" + k: {
            **v,
            "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/" + v["pmcid"] + "/fullTextXML",
        }
        for k, v in bibliography.items()
    }
    write_json(
        tmp_path / "primary-plan.json",
        {
            "cohort": pin("cohort.json"),
            "requests": requests_by_id,
            "canary_request": "article-23208709",
            "canary_required_before_batch": True,
        },
    )

    def response(key, plan, url, status, body, headers, when, **extra):
        write_json(
            tmp_path / (key + "-attempt.json"),
            {"url": url, "plan_sha256": pin(plan)["sha256"], "retry_performed": False},
        )
        (tmp_path / (key + "-response.bin")).write_bytes(body)
        write_json(
            tmp_path / (key + "-receipt.json"),
            {
                "url": url,
                "status": status,
                "sha256": hashlib.sha256(body).hexdigest(),
                "bytes": len(body),
                "headers": headers,
                "retrieved_at": when,
                "retry_performed": False,
                "redirects_followed": False,
                **extra,
            },
        )

    response(
        "article-23208709",
        "primary-plan.json",
        audit.EPMC,
        500,
        json.dumps(
            {
                "status": 500,
                "error": "Internal Server Error",
                "path": "/europepmc/webservices/rest/PMC3553702/fullTextXML",
            }
        ).encode(),
        {},
        "2026-10-15T01:00:00Z",
    )
    write_json(
        tmp_path / "primary-canary-stop.json",
        {
            "plan": pin("primary-plan.json"),
            "receipt": pin("article-23208709-receipt.json"),
            "held_pmid": "23208709",
            "unrequested_pmid": "30337678",
            "unrequested_route": "EUROPE_PMC_FULLTEXT",
            "status": "HTTP_500_TECHNICAL_HOLD_NO_RETRY",
            "primary_results_reviewed": False,
            "biological_absence_inferred": False,
        },
    )
    write_json(
        tmp_path / "publisher-plan.json",
        {
            "cohort": pin("cohort.json"),
            "prior_canary_stop": pin("primary-canary-stop.json"),
            "held_first_paper_retried": False,
            "requests": {"publisher-30337678": {"url": audit.ARTICLE}},
        },
    )
    response(
        "publisher-30337678",
        "publisher-plan.json",
        audit.ARTICLE,
        303,
        b"redirect",
        {"Location": audit.COOKIE},
        "2026-10-15T01:01:00Z",
    )
    write_json(
        tmp_path / "publisher-redirect-plan.json",
        {
            "cohort": pin("cohort.json"),
            "observed_redirect_receipt": pin("publisher-30337678-receipt.json"),
            "requests": {
                "publisher-cookie-flow": {"url": audit.COOKIE},
                "publisher-article-flow": {"url": audit.ARTICLE},
            },
            "max_requests": 2,
            "held_pmid_23208709_retried": False,
            "credentials_supplied": False,
        },
    )
    response(
        "publisher-cookie-flow",
        "publisher-redirect-plan.json",
        audit.COOKIE,
        302,
        b"",
        redirected_receipt()["headers"],
        "2026-10-15T01:02:00Z",
        manual_redirect_continuation=True,
        credentials_supplied=False,
    )
    return tmp_path, cohort


def test_complete_request_history_preserves_failed_canary_and_bounded_flow(history):
    root, cohort = history
    sources, states = audit.request_context(root, root, cohort)
    assert len(sources) == 3
    assert states["PMID:23208709"]["status"] == "TECHNICAL_HTTP_500_HOLD"
    assert states["PMID:23208709"]["negative_biological_evidence"] is False
    assert states["PMID:30337678"]["final_article_request_performed"] is False
    assert "private-test-code" not in json.dumps(states)


@pytest.mark.parametrize(
    "change",
    [
        "extra_request",
        "retry",
        "redirect_followed",
        "wrong_url",
        "body_drift",
        "wrong_status",
        "stale_plan",
        "chronology",
        "primary_review_promoted",
        "second_epmc_requested",
    ],
)
def test_request_history_guards(history, change):
    root, cohort = history
    key = "article-23208709"
    if change in {"extra_request", "second_epmc_requested"}:
        name = "extra" if change == "extra_request" else "article-30337678"
        write_json(root / (name + "-attempt.json"), {})
    elif change == "body_drift":
        (root / (key + "-response.bin")).write_bytes(b"changed")
    elif change == "stale_plan":
        write_json(root / "primary-plan.json", {})
    elif change == "primary_review_promoted":
        path = root / "primary-canary-stop.json"
        value = json.loads(path.read_bytes())
        value["primary_results_reviewed"] = True
        write_json(path, value)
    else:
        path = root / (key + "-receipt.json")
        value = json.loads(path.read_bytes())
        field, new_value = {
            "retry": ("retry_performed", True),
            "redirect_followed": ("redirects_followed", True),
            "wrong_url": ("url", "https://other.example/article"),
            "wrong_status": ("status", 200),
            "chronology": ("retrieved_at", "2026-10-15T02:00:00Z"),
        }[change]
        value[field] = new_value
        write_json(path, value)
    with pytest.raises((ValueError, KeyError)):
        audit.request_context(root, root, cohort)


@pytest.mark.parametrize("check", [False, True])
def test_cli_does_not_overwrite_historical_checkpoint(tmp_path, monkeypatch, check):
    path = tmp_path / "checkpoint.json"
    path.write_bytes(b"historical bytes\n")
    monkeypatch.setattr(audit, "OUTPUT", path)
    monkeypatch.setattr(audit, "build", lambda root: {"summary": {}})
    monkeypatch.setattr(sys, "argv", ["audit"] + (["--check"] if check else []))
    with pytest.raises(ValueError, match="does not reproduce"):
        audit.main()
    assert path.read_bytes() == b"historical bytes\n"


def test_public_checkpoint_does_not_adjudicate_causality_or_assign_subjects():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert result["summary"]["source_assertions"] == 4
    assert result["summary"]["source_records"] == 2
    assert result["summary"]["primary_articles_obtained"] == 0
    for term in result["term_contexts"].values():
        assert term["primary_review_status"] == "OPEN"
        assert term["source_claim_corrected"] is term["experimental_subject_assignment"] is False
        assert term["exact_resistant_allele"] is term["experimental_genome_assignment"] is None
    named, generic = (result["term_contexts"][tid] for tid in ("ARO:3004994", "ARO:3004995"))
    assert named["named_reference_taxon_id"] == "NCBITaxon:1773"
    assert len(named["reference_protein_candidates"]) == 6
    assert not generic["reference_protein_candidates"] and generic["named_reference_taxon_id"] is None
    assert generic["definition_citation_ids"] == []
    assert result["constraints"]["ncbi_requests"] == 0
    assert result["constraints"]["full_corpus_goal_status"] == "OPEN"


@pytest.mark.skipif(not (ROOT / audit.CACHE / "cohort.json").exists(), reason="private native cache absent")
def test_native_replay_offline():
    result = audit.build(ROOT)
    assert (json.dumps(result, indent=2, sort_keys=True) + "\n").encode() == (
        ROOT / audit.OUTPUT
    ).read_bytes()
