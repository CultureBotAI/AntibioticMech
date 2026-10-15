"""Keep empty metadata queries and a reagent paragraph within their actual scope."""

import hashlib
import json
import socket
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest
import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_aac34_followup as audit  # noqa: E402


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("network forbidden")

    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket.socket, "connect_ex", denied)
    monkeypatch.setattr(socket, "create_connection", denied)


@pytest.mark.parametrize("reviewed", [True, False])
def test_query_is_bounded_metadata_not_a_sequence_request(reviewed):
    url = urlsplit(audit.query_url(reviewed))
    query = parse_qs(url.query)
    assert url.netloc == "rest.uniprot.org" and url.path == "/uniprotkb/search"
    assert query["query"] == [
        '(gene_exact:"aac(6\')-34" OR protein_name:"AAC(6\')-34") AND reviewed:' + str(reviewed).lower()
    ]
    assert not {"sequence", "features"} & set(query["fields"][0].split(","))
    assert query["size"] == ["500"]


@pytest.mark.parametrize("value", [None, 0, 1, "false"])
def test_query_requires_explicit_review_subset(value):
    with pytest.raises(ValueError):
        audit.query_url(value)


@pytest.fixture
def synthetic_primary(monkeypatch):
    paragraph = "General supplier statement. " + "x" * (590 - len("General supplier statement. "))
    monkeypatch.setattr(audit, "PARAGRAPH_SHA", hashlib.sha256(paragraph.encode()).hexdigest())
    return (
        "<article><front><article-meta><article-id pub-id-type='pmid'>27929110</article-id>"
        "<article-id pub-id-type='doi'>10.1038/ncomms13803</article-id></article-meta></front>"
        "<body><sec id='sec11'><title>Antibiotics and reagents</title><p>"
        + paragraph
        + "</p></sec></body></article>"
    ).encode()


def test_chemical_context_does_not_export_methods_or_assign_a_structure(synthetic_primary):
    result = audit.chemical_context(synthetic_primary)
    assert result["exact_corpus_structure_assignment"] is None
    assert result["activity_observation_curated"] is result["operational_paragraph_exported"] is False
    assert result["whole_article_or_supplement_identifier_absence_claimed"] is False
    assert "x" * 50 not in json.dumps(result)


@pytest.mark.parametrize(
    "old,new",
    [
        (b"27929110", b"1"),
        (b"ncomms13803", b"other"),
        (b"sec11", b"sec12"),
        (b"Antibiotics and reagents", b"Other section"),
        (b"<p>", b"<p>changed "),
        (b"</sec>", b"<p>Another paragraph.</p></sec>"),
    ],
)
def test_article_and_selected_paragraph_are_pinned(synthetic_primary, old, new):
    with pytest.raises(ValueError):
        audit.chemical_context(synthetic_primary.replace(old, new))


def test_saved_public_scope():
    result = json.loads((ROOT / audit.OUTPUT).read_bytes())
    assert result["scope"] == audit.SCOPE and result["source_term_id"] == audit.TERM
    assert result["summary"]["selected_reference_proteins"] == 0
    for query in [*result["name_queries"].values(), result["exact_organism_query"]]:
        assert query["result_count"] == 0 and query["complete_for_query"] is True
        assert query["biological_absence_inferred"] is False
        assert query["source"]["status"] == 200 and query["source"]["release"] == "2026_03"
    assert result["limits"]["new_network_requests"] == result["limits"]["ncbi_requests"] == 0
    assert result["limits"]["all_aliases_or_sources_searched"] is False
    assert result["chemical_context"]["exact_corpus_structure_assignment"] is None


def test_native_replay_when_cache_available():
    if not (ROOT / audit.CACHE / "cohort.json").is_file():
        pytest.skip("native research caches unavailable; public scope and synthetic guards still run")
    result = audit.build(ROOT)
    assert (json.dumps(result, sort_keys=True, indent=2) + "\n").encode() == (
        ROOT / audit.OUTPUT
    ).read_bytes()


def test_cli_checks_without_overwriting(tmp_path, monkeypatch):
    output = tmp_path / "out.json"
    monkeypatch.setattr(audit, "build", lambda root: {"summary": {}})
    monkeypatch.setattr(sys, "argv", ["audit", "--output", str(output), "--check"])
    with pytest.raises(FileNotFoundError):
        audit.main()
    assert not output.exists()
    monkeypatch.setattr(sys, "argv", ["audit", "--output", str(output)])
    audit.main()
    audit.main()
    output.write_text("different")
    with pytest.raises(ValueError, match="does not reproduce"):
        audit.main()
