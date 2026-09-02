"""Semantic Scholar Academic Graph publication-search adapter."""

from __future__ import annotations

import json
import re
import time
from collections.abc import Callable

from .http import Transport, UrllibTransport
from .models import Publication, PublicationSearchError, SearchRequest

SEARCH_URL = "https://api.semanticscholar.org/graph/v1/paper/search"
FIELDS = ",".join(
    (
        "title",
        "abstract",
        "authors",
        "year",
        "publicationDate",
        "venue",
        "externalIds",
        "url",
        "citationCount",
    )
)


def _plain_text_query(value: str) -> str:
    """Translate the shared Boolean-like query for S2's plain-text endpoint."""
    value = re.sub(r"\b(?:AND|OR|NOT)\b", " ", value, flags=re.I)
    return " ".join(re.sub(r"[()\[\]{}\"']+", " ", value).split())


def _normalize_doi(value: object) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return None
    normalized = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value.strip(), flags=re.I)
    return normalized.casefold() or None


def _year(value: object) -> int | None:
    if isinstance(value, int) and 1800 <= value <= 3000:
        return value
    if isinstance(value, str) and value.isdigit() and 1800 <= int(value) <= 3000:
        return int(value)
    return None


def parse_semantic_scholar_paper(item: object) -> Publication | None:
    if not isinstance(item, dict):
        return None
    paper_id = item.get("paperId")
    title = item.get("title")
    if not isinstance(paper_id, str) or not isinstance(title, str) or not title.strip():
        return None
    external = item.get("externalIds") if isinstance(item.get("externalIds"), dict) else {}
    pmid_value = external.get("PubMed")
    pmid = str(pmid_value) if pmid_value not in (None, "") else None
    authors = [
        author["name"].strip()
        for author in item.get("authors") or []
        if isinstance(author, dict)
        and isinstance(author.get("name"), str)
        and author["name"].strip()
    ]
    citation_count = item.get("citationCount")
    if not isinstance(citation_count, int):
        citation_count = None
    publication_date = item.get("publicationDate")
    if not isinstance(publication_date, str) or not publication_date.strip():
        publication_date = None
    year = _year(item.get("year"))
    if year is None and publication_date:
        year = _year(publication_date[:4])
    return Publication(
        title=title.strip(),
        providers=["semantic_scholar"],
        provider_ids={"semantic_scholar": paper_id},
        abstract=item.get("abstract") if isinstance(item.get("abstract"), str) else None,
        authors=authors,
        publication_date=publication_date,
        year=year,
        venue=item.get("venue") if isinstance(item.get("venue"), str) else None,
        doi=_normalize_doi(external.get("DOI")),
        pmid=pmid,
        url=item.get("url") if isinstance(item.get("url"), str) else None,
        citation_count=citation_count,
    )


class SemanticScholarAdapter:
    """Search the Semantic Scholar Academic Graph API with bounded pagination."""

    provider = "semantic_scholar"

    def __init__(
        self,
        *,
        api_key: str | None = None,
        transport: Transport | None = None,
        sleeper: Callable[[float], None] = time.sleep,
    ) -> None:
        self.api_key = api_key
        self.transport = transport or UrllibTransport()
        self.sleeper = sleeper

    def search(self, request: SearchRequest) -> list[Publication]:
        headers = {"x-api-key": self.api_key} if self.api_key else {}
        output = []
        offset = 0
        while len(output) < request.limit:
            page_size = min(100, request.limit - len(output))
            params: dict[str, str | int] = {
                "query": _plain_text_query(request.query),
                "offset": offset,
                "limit": page_size,
                "fields": FIELDS,
            }
            if request.since or request.until:
                first = request.since.isoformat() if request.since else ""
                last = request.until.isoformat() if request.until else ""
                params["publicationDateOrYear"] = f"{first}:{last}"
            raw = self.transport.get(SEARCH_URL, params=params, headers=headers)
            try:
                payload = json.loads(raw)
                data = payload["data"]
            except (json.JSONDecodeError, KeyError, TypeError) as error:
                raise PublicationSearchError(
                    "Semantic Scholar search returned an invalid response"
                ) from error
            if not isinstance(data, list):
                raise PublicationSearchError("Semantic Scholar response data is not a list")
            page = [paper for item in data if (paper := parse_semantic_scholar_paper(item))]
            output.extend(page)
            if len(output) >= request.limit or len(data) < page_size:
                break
            offset += len(data)
            # The provider's introductory authenticated quota is one request
            # per second. This conservative pace is also kind to shared access.
            self.sleeper(1)
        return output[: request.limit]
