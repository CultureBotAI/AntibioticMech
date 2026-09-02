"""Google Scholar results via SerpAPI's documented API.

Google does not publish a supported Scholar API. This adapter deliberately uses
the explicit, authenticated SerpAPI contract instead of scraping Scholar HTML.
"""

from __future__ import annotations

import json
import re
from urllib.parse import urlsplit

from .http import Transport, UrllibTransport
from .models import ConfigurationError, Publication, PublicationSearchError, SearchRequest

SEARCH_URL = "https://serpapi.com/search.json"
YEAR = re.compile(r"\b((?:19|20)\d{2})\b")
PUBMED_PATH = re.compile(r"^/(\d+)/?$")


def _identifier_from_url(url: str | None) -> tuple[str | None, str | None]:
    if not url:
        return None, None
    parsed = urlsplit(url)
    host = parsed.netloc.casefold().removeprefix("www.")
    if host in {"doi.org", "dx.doi.org"}:
        doi = parsed.path.lstrip("/").casefold()
        return doi or None, None
    if host == "pubmed.ncbi.nlm.nih.gov":
        match = PUBMED_PATH.match(parsed.path)
        return None, match.group(1) if match else None
    return None, None


def parse_google_scholar_result(item: object) -> Publication | None:
    if not isinstance(item, dict):
        return None
    title = item.get("title")
    result_id = item.get("result_id")
    if not isinstance(title, str) or not title.strip() or not isinstance(result_id, str):
        return None
    publication_info = item.get("publication_info")
    publication_info = publication_info if isinstance(publication_info, dict) else {}
    summary = publication_info.get("summary")
    summary = summary if isinstance(summary, str) else ""
    year_match = YEAR.search(summary)
    year = int(year_match.group(1)) if year_match else None
    authors = [
        author["name"].strip()
        for author in publication_info.get("authors") or []
        if isinstance(author, dict)
        and isinstance(author.get("name"), str)
        and author["name"].strip()
    ]
    link = item.get("link") if isinstance(item.get("link"), str) else None
    doi, pmid = _identifier_from_url(link)
    cited_by = item.get("inline_links")
    cited_by = cited_by.get("cited_by") if isinstance(cited_by, dict) else None
    citation_count = cited_by.get("total") if isinstance(cited_by, dict) else None
    if not isinstance(citation_count, int):
        citation_count = None
    snippet = item.get("snippet")
    return Publication(
        title=title.strip(),
        providers=["google_scholar"],
        provider_ids={"google_scholar": result_id},
        snippet=snippet.strip() if isinstance(snippet, str) and snippet.strip() else None,
        authors=authors,
        publication_date=str(year) if year else None,
        year=year,
        # Scholar's summary combines authors, venue, year, and host; do not
        # misrepresent that compound display string as a normalized venue.
        venue=None,
        doi=doi,
        pmid=pmid,
        url=link,
        citation_count=citation_count,
    )


class GoogleScholarAdapter:
    """Search Google Scholar through SerpAPI without scraping Google pages."""

    provider = "google_scholar"

    def __init__(self, *, api_key: str, transport: Transport | None = None) -> None:
        if not api_key.strip():
            raise ConfigurationError(
                "Google Scholar search requires SERPAPI_API_KEY; Google has no supported Scholar API"
            )
        self.api_key = api_key
        self.transport = transport or UrllibTransport()

    def search(self, request: SearchRequest) -> list[Publication]:
        output = []
        offset = 0
        while len(output) < request.limit:
            page_size = min(20, request.limit - len(output))
            params: dict[str, str | int] = {
                "engine": "google_scholar",
                "q": request.query,
                "hl": "en",
                "start": offset,
                "num": page_size,
                "api_key": self.api_key,
            }
            if request.since:
                params["as_ylo"] = request.since.year
            if request.until:
                params["as_yhi"] = request.until.year
            raw = self.transport.get(SEARCH_URL, params=params)
            try:
                payload = json.loads(raw)
            except json.JSONDecodeError as error:
                raise PublicationSearchError("SerpAPI returned invalid JSON") from error
            if isinstance(payload, dict) and payload.get("error"):
                raise PublicationSearchError(f"SerpAPI Google Scholar error: {payload['error']}")
            results = payload.get("organic_results") if isinstance(payload, dict) else None
            if not isinstance(results, list):
                raise PublicationSearchError("SerpAPI response has no organic_results list")
            output.extend(
                paper for item in results if (paper := parse_google_scholar_result(item))
            )
            pagination = payload.get("serpapi_pagination", {})
            has_next = isinstance(pagination, dict) and bool(pagination.get("next"))
            if len(output) >= request.limit or len(results) < page_size or not has_next:
                break
            offset += page_size
        return output[: request.limit]
