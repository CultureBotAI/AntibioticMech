"""PubMed adapter using NCBI's supported E-utilities API."""

from __future__ import annotations

import json
import re
import time
import xml.etree.ElementTree as ET
from collections.abc import Callable
from datetime import date

from .http import Transport, UrllibTransport
from .models import DEFAULT_DISCOVERY_QUERY, Publication, PublicationSearchError, SearchRequest

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
MONTHS = {
    name: index
    for index, name in enumerate(
        ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"),
        1,
    )
}


def _text(element: ET.Element | None) -> str:
    return "" if element is None else "".join(element.itertext()).strip()


def _normalize_doi(value: str | None) -> str | None:
    if not value:
        return None
    normalized = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value.strip(), flags=re.I)
    return normalized.casefold() or None


def _publication_date(citation: ET.Element) -> tuple[str | None, int | None]:
    candidates = [
        citation.find("./Article/ArticleDate"),
        citation.find("./Article/Journal/JournalIssue/PubDate"),
        citation.find("./DateCompleted"),
    ]
    for candidate in candidates:
        if candidate is None:
            continue
        year_text = _text(candidate.find("Year"))
        if not year_text:
            match = re.search(r"\b(?:19|20)\d{2}\b", _text(candidate.find("MedlineDate")))
            year_text = match.group(0) if match else ""
        if not year_text.isdigit():
            continue
        year = int(year_text)
        month_text = _text(candidate.find("Month"))
        day_text = _text(candidate.find("Day"))
        month = int(month_text) if month_text.isdigit() else MONTHS.get(month_text[:3].title())
        if month and day_text.isdigit():
            return f"{year:04d}-{month:02d}-{int(day_text):02d}", year
        if month:
            return f"{year:04d}-{month:02d}", year
        return str(year), year
    return None, None


def _authors(article: ET.Element) -> list[str]:
    output = []
    for author in article.findall("./AuthorList/Author"):
        collective = _text(author.find("CollectiveName"))
        if collective:
            output.append(collective)
            continue
        name = " ".join(
            part for part in (_text(author.find("ForeName")), _text(author.find("LastName"))) if part
        )
        if name:
            output.append(name)
    return output


def parse_pubmed_xml(payload: bytes) -> list[Publication]:
    """Normalize PubMedArticle elements returned by EFetch."""
    try:
        root = ET.fromstring(payload)
    except ET.ParseError as error:
        raise PublicationSearchError("PubMed EFetch returned invalid XML") from error
    publications = []
    for item in root.findall("./PubmedArticle"):
        citation = item.find("MedlineCitation")
        if citation is None:
            continue
        article = citation.find("Article")
        pmid = _text(citation.find("PMID"))
        title = _text(article.find("ArticleTitle")) if article is not None else ""
        if not pmid or not title:
            continue
        abstract_parts = []
        if article is not None:
            for part in article.findall("./Abstract/AbstractText"):
                body = _text(part)
                label = (part.get("Label") or "").strip()
                if body:
                    abstract_parts.append(f"{label}: {body}" if label else body)
        ids = {}
        for identifier in item.findall("./PubmedData/ArticleIdList/ArticleId"):
            kind = (identifier.get("IdType") or "").casefold()
            value = _text(identifier)
            if kind and value:
                ids[kind] = value
        doi = _normalize_doi(ids.get("doi"))
        publication_date, year = _publication_date(citation)
        venue = _text(article.find("./Journal/Title")) if article is not None else ""
        publications.append(
            Publication(
                title=title,
                providers=["pubmed"],
                provider_ids={"pubmed": pmid},
                abstract="\n".join(abstract_parts) or None,
                authors=_authors(article) if article is not None else [],
                publication_date=publication_date,
                year=year,
                venue=venue or None,
                doi=doi,
                pmid=pmid,
                url=f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            )
        )
    return publications


class PubMedAdapter:
    """Search PubMed and retrieve complete citation/abstract metadata."""

    provider = "pubmed"

    def __init__(
        self,
        *,
        api_key: str | None = None,
        email: str | None = None,
        tool: str = "AntibioticMech",
        transport: Transport | None = None,
        sleeper: Callable[[float], None] = time.sleep,
    ) -> None:
        self.api_key = api_key
        self.email = email
        self.tool = tool
        self.transport = transport or UrllibTransport()
        self.sleeper = sleeper

    def _identity_params(self) -> dict[str, str]:
        params = {"tool": self.tool}
        if self.api_key:
            params["api_key"] = self.api_key
        # Contact information is transmitted only when the caller explicitly configures it.
        if self.email:
            params["email"] = self.email
        return params

    def search(self, request: SearchRequest) -> list[Publication]:
        query = request.query
        if query == DEFAULT_DISCOVERY_QUERY:
            query = f"{query} NOT review[Publication Type]"
        params: dict[str, str | int] = {
            "db": "pubmed",
            "term": query,
            "retmode": "json",
            "retmax": request.limit,
            "sort": "pub date",
            **self._identity_params(),
        }
        if request.since or request.until:
            params.update(
                {
                    "datetype": "pdat",
                    "mindate": (request.since or date(1800, 1, 1)).strftime("%Y/%m/%d"),
                    "maxdate": (request.until or date.today()).strftime("%Y/%m/%d"),
                }
            )
        raw_search = self.transport.get(f"{EUTILS}/esearch.fcgi", params=params)
        try:
            search = json.loads(raw_search)
            id_list = search["esearchresult"]["idlist"]
            if not isinstance(id_list, list):
                raise TypeError("idlist is not a list")
            ids = [str(value) for value in id_list]
        except (json.JSONDecodeError, KeyError, TypeError) as error:
            raise PublicationSearchError("PubMed ESearch returned an invalid response") from error
        if not ids:
            return []
        output = []
        interval = 0.1 if self.api_key else 1 / 3
        for start in range(0, len(ids), 200):
            # NCBI recommends GET batches no larger than a few hundred and
            # permits ten requests/second with a key, three without one.
            self.sleeper(interval)
            fetch_params: dict[str, str | int] = {
                "db": "pubmed",
                "id": ",".join(ids[start : start + 200]),
                "retmode": "xml",
                **self._identity_params(),
            }
            raw_records = self.transport.get(f"{EUTILS}/efetch.fcgi", params=fetch_params)
            output.extend(parse_pubmed_xml(raw_records))
        return output[: request.limit]
