"""Publication adapters normalize provider responses without making live calls."""

from __future__ import annotations

import json
from datetime import date

import pytest

from antibioticmech.publications import (
    GoogleScholarAdapter,
    Publication,
    PubMedAdapter,
    SearchRequest,
    SemanticScholarAdapter,
    deduplicate_publications,
)
from antibioticmech.publications.google_scholar import SEARCH_URL as GOOGLE_URL
from antibioticmech.publications.models import ConfigurationError
from antibioticmech.publications.pubmed import EUTILS
from antibioticmech.publications.semantic_scholar import SEARCH_URL as SEMANTIC_URL
from scripts import search_publications as cli


class FakeTransport:
    def __init__(self, *responses: bytes | dict):
        self.responses = [
            json.dumps(response).encode() if isinstance(response, dict) else response
            for response in responses
        ]
        self.calls = []

    def get(self, url, *, params, headers=None):
        self.calls.append((url, dict(params), dict(headers or {})))
        return self.responses.pop(0)


def test_search_request_rejects_unbounded_or_reversed_input():
    with pytest.raises(ValueError, match="must not be empty"):
        SearchRequest(query=" ")
    with pytest.raises(ValueError, match="between 1 and 1000"):
        SearchRequest(limit=0)
    with pytest.raises(ValueError, match="must not follow"):
        SearchRequest(since=date(2026, 2, 1), until=date(2026, 1, 1))


def test_pubmed_uses_esearch_then_efetch_and_parses_structured_xml():
    xml = b"""<?xml version="1.0"?>
    <PubmedArticleSet><PubmedArticle><MedlineCitation>
      <PMID>12345</PMID><DateCompleted><Year>2026</Year><Month>02</Month><Day>03</Day></DateCompleted>
      <Article><ArticleTitle>A <i>new</i> antibiotic</ArticleTitle>
        <Abstract><AbstractText Label="RESULTS">Compound X inhibited bacteria.</AbstractText></Abstract>
        <AuthorList><Author><ForeName>Ada</ForeName><LastName>Lovelace</LastName></Author></AuthorList>
        <Journal><JournalIssue><PubDate><Year>2026</Year><Month>Jan</Month></PubDate></JournalIssue>
          <Title>Journal of Antibiotics</Title></Journal>
      </Article></MedlineCitation><PubmedData><ArticleIdList>
        <ArticleId IdType="pubmed">12345</ArticleId><ArticleId IdType="doi">10.1/ABC</ArticleId>
      </ArticleIdList></PubmedData></PubmedArticle></PubmedArticleSet>"""
    transport = FakeTransport({"esearchresult": {"idlist": ["12345"]}}, xml)
    adapter = PubMedAdapter(
        api_key="ncbi-secret",
        email="curator@example.org",
        transport=transport,
        sleeper=lambda _: None,
    )
    papers = adapter.search(
        SearchRequest(since=date(2026, 1, 1), until=date(2026, 12, 31), limit=5)
    )

    assert len(papers) == 1
    paper = papers[0]
    assert paper.title == "A new antibiotic"
    assert paper.abstract == "RESULTS: Compound X inhibited bacteria."
    assert paper.authors == ["Ada Lovelace"]
    assert paper.publication_date == "2026-01"
    assert paper.doi == "10.1/abc"
    assert paper.pmid == "12345"
    assert transport.calls[0][0] == f"{EUTILS}/esearch.fcgi"
    assert transport.calls[0][1]["term"].endswith("NOT review[Publication Type]")
    assert transport.calls[0][1]["mindate"] == "2026/01/01"
    assert transport.calls[0][1]["email"] == "curator@example.org"
    assert transport.calls[1][0] == f"{EUTILS}/efetch.fcgi"
    assert transport.calls[1][1]["id"] == "12345"


def test_pubmed_empty_search_does_not_call_efetch_or_send_unset_contact_data():
    transport = FakeTransport({"esearchresult": {"idlist": []}})
    assert (
        PubMedAdapter(transport=transport, sleeper=lambda _: None).search(SearchRequest(limit=1))
        == []
    )
    assert len(transport.calls) == 1
    assert "email" not in transport.calls[0][1]
    assert "api_key" not in transport.calls[0][1]


def semantic_item(index: int) -> dict:
    return {
        "paperId": f"S2-{index}",
        "title": f"Novel antibiotic {index}",
        "abstract": f"Abstract {index}",
        "authors": [{"authorId": "A1", "name": "Grace Hopper"}],
        "year": 2026,
        "publicationDate": "2026-04-05",
        "venue": "Nature Chemistry",
        "externalIds": {"DOI": f"10.2/{index}", "PubMed": str(2000 + index)},
        "url": f"https://www.semanticscholar.org/paper/S2-{index}",
        "citationCount": index,
    }


def test_semantic_scholar_paginates_and_sends_key_in_header():
    first = [semantic_item(index) for index in range(100)]
    transport = FakeTransport({"total": 101, "data": first}, {"total": 101, "data": [semantic_item(100)]})
    sleeps = []
    papers = SemanticScholarAdapter(
        api_key="s2-secret", transport=transport, sleeper=sleeps.append
    ).search(
        SearchRequest(since=date(2025, 1, 1), limit=101)
    )

    assert len(papers) == 101
    assert papers[-1].provider_ids == {"semantic_scholar": "S2-100"}
    assert papers[-1].citation_count == 100
    assert transport.calls[0][0] == SEMANTIC_URL
    assert transport.calls[0][1]["publicationDateOrYear"] == "2025-01-01:"
    assert "OR" not in transport.calls[0][1]["query"]
    assert transport.calls[0][2] == {"x-api-key": "s2-secret"}
    assert transport.calls[1][1]["offset"] == 100
    assert sleeps == [1]


def google_item(index: int) -> dict:
    return {
        "result_id": f"GS-{index}",
        "title": f"A new antibiotic {index}",
        "link": f"https://doi.org/10.3/NEW-{index}",
        "snippet": f"Discovery snippet {index}",
        "publication_info": {
            "summary": "G Hopper - Example Journal, 2026 - example.org",
            "authors": [{"name": "G Hopper"}],
        },
        "inline_links": {"cited_by": {"total": index}},
    }


def test_google_scholar_uses_serpapi_contract_and_paginates():
    transport = FakeTransport(
        {
            "organic_results": [google_item(index) for index in range(20)],
            "serpapi_pagination": {"next": "https://serpapi.com/search?start=20"},
        },
        {"organic_results": [google_item(20)]},
    )
    papers = GoogleScholarAdapter(api_key="serp-secret", transport=transport).search(
        SearchRequest(since=date(2026, 1, 1), until=date(2026, 12, 31), limit=21)
    )

    assert len(papers) == 21
    assert papers[0].doi == "10.3/new-0"
    assert papers[0].abstract is None
    assert papers[0].snippet == "Discovery snippet 0"
    assert papers[0].citation_count == 0
    assert transport.calls[0][0] == GOOGLE_URL
    assert transport.calls[0][1]["engine"] == "google_scholar"
    assert transport.calls[0][1]["as_ylo"] == 2026
    assert transport.calls[1][1]["start"] == 20


def test_google_scholar_requires_explicit_third_party_api_configuration():
    with pytest.raises(ConfigurationError, match="SERPAPI_API_KEY"):
        GoogleScholarAdapter(api_key="")


def test_google_scholar_does_not_spend_an_extra_search_without_next_page():
    transport = FakeTransport({"organic_results": [google_item(index) for index in range(20)]})
    papers = GoogleScholarAdapter(api_key="serp-secret", transport=transport).search(
        SearchRequest(limit=21)
    )
    assert len(papers) == 20
    assert len(transport.calls) == 1


def test_cross_provider_dedup_keeps_rich_fields_and_all_provenance():
    pubmed = Publication(
        title="Discovery of compound X",
        providers=["pubmed"],
        provider_ids={"pubmed": "10"},
        abstract="Long primary abstract",
        year=2026,
        doi="10.4/x",
        pmid="10",
    )
    semantic = Publication(
        title="Discovery of Compound X",
        providers=["semantic_scholar"],
        provider_ids={"semantic_scholar": "S2-X"},
        authors=["A Curator"],
        year=2026,
        doi="10.4/X",
        citation_count=7,
    )
    google = Publication(
        title="Discovery of compound X",
        providers=["google_scholar"],
        provider_ids={"google_scholar": "GS-X"},
        snippet="Search snippet",
        year=2026,
    )

    merged = deduplicate_publications([pubmed, semantic, google])
    assert len(merged) == 1
    assert merged[0].providers == ["pubmed", "semantic_scholar", "google_scholar"]
    assert merged[0].provider_ids == {
        "pubmed": "10",
        "semantic_scholar": "S2-X",
        "google_scholar": "GS-X",
    }
    assert merged[0].abstract == "Long primary abstract"
    assert merged[0].snippet == "Search snippet"
    assert merged[0].citation_count == 7


def test_conflicting_dois_are_not_merged_by_title_and_year():
    left = Publication(title="Same title", providers=["a"], year=2026, doi="10.5/a")
    right = Publication(title="Same title", providers=["b"], year=2026, doi="10.5/b")
    assert len(deduplicate_publications([left, right])) == 2


def test_cli_default_uses_only_nonbilling_public_apis(capsys, monkeypatch):
    captured = {}

    def fake_search(adapters, request):
        captured["providers"] = [adapter.provider for adapter in adapters]
        captured["request"] = request
        return [Publication(title="Candidate paper", providers=["pubmed"], pmid="42")]

    monkeypatch.setattr(cli, "search_publications", fake_search)
    assert cli.main(["--limit", "2"], environ={}) == 0
    output = capsys.readouterr()
    assert captured["providers"] == ["pubmed", "semantic_scholar"]
    assert captured["request"].limit == 2
    assert json.loads(output.out)["pmid"] == "42"
    assert output.err == ""


def test_cli_explicit_all_skips_unconfigured_google(capsys, monkeypatch):
    monkeypatch.setattr(cli, "search_publications", lambda adapters, request: [])
    assert cli.main(["--provider", "all", "--limit", "1"], environ={}) == 0
    assert "skipped google-scholar" in capsys.readouterr().err


def test_cli_explicit_google_provider_requires_key(capsys):
    assert cli.main(["--provider", "google-scholar"], environ={}) == 1
    assert "SERPAPI_API_KEY" in capsys.readouterr().err
