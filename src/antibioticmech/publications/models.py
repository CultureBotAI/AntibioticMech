"""Provider-neutral publication search types."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import date
from typing import Any, Protocol

DEFAULT_DISCOVERY_QUERY = (
    '(("novel antibiotic" OR "new antibiotic" OR "new antibacterial compound" OR '
    '"novel antibacterial compound") AND (discovery OR discovered OR isolation OR '
    'isolated OR identified OR characterized OR "we report"))'
)


class PublicationSearchError(RuntimeError):
    """A publication provider rejected or could not satisfy a search."""


class ConfigurationError(PublicationSearchError):
    """A provider is missing required local configuration."""


@dataclass(frozen=True, slots=True)
class SearchRequest:
    """A bounded publication search shared by all providers."""

    query: str = DEFAULT_DISCOVERY_QUERY
    since: date | None = None
    until: date | None = None
    limit: int = 50

    def __post_init__(self) -> None:
        if not self.query.strip():
            raise ValueError("publication query must not be empty")
        if not 1 <= self.limit <= 1_000:
            raise ValueError("publication limit must be between 1 and 1000")
        if self.since and self.until and self.since > self.until:
            raise ValueError("publication since date must not follow until date")


@dataclass(slots=True)
class Publication:
    """Normalized candidate publication; discovery is not evidence of a claim."""

    title: str
    providers: list[str]
    provider_ids: dict[str, str] = field(default_factory=dict)
    abstract: str | None = None
    snippet: str | None = None
    authors: list[str] = field(default_factory=list)
    publication_date: str | None = None
    year: int | None = None
    venue: str | None = None
    doi: str | None = None
    pmid: str | None = None
    url: str | None = None
    citation_count: int | None = None

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class PublicationSearchOutcome:
    """Successful provider results plus isolated, observable provider errors."""

    publications: list[Publication]
    succeeded_providers: list[str]
    provider_errors: dict[str, str]


class PublicationAdapter(Protocol):
    """Interface implemented by each publication provider."""

    provider: str

    def search(self, request: SearchRequest) -> list[Publication]: ...
