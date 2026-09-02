"""Cross-provider publication discovery and conservative deduplication."""

from __future__ import annotations

import re
from collections.abc import Iterable, Sequence

from .models import (
    Publication,
    PublicationAdapter,
    PublicationSearchError,
    PublicationSearchOutcome,
    SearchRequest,
)


def _normalized_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def _identity_keys(publication: Publication) -> list[tuple[str, str]]:
    keys = []
    if publication.doi:
        keys.append(("doi", publication.doi.casefold()))
    if publication.pmid:
        keys.append(("pmid", publication.pmid))
    title = _normalized_title(publication.title)
    if title and publication.year is not None:
        keys.append(("title_year", f"{title}:{publication.year or ''}"))
    return keys


def _longer(left: str | None, right: str | None) -> str | None:
    return max((value for value in (left, right) if value), key=len, default=None)


def _compatible(left: Publication, right: Publication) -> bool:
    if left.doi and right.doi and left.doi.casefold() != right.doi.casefold():
        return False
    return not (left.pmid and right.pmid and left.pmid != right.pmid)


def _merge(left: Publication, right: Publication) -> Publication:
    """Merge provider metadata without turning a snippet into an abstract."""
    publication_date = left.publication_date or right.publication_date
    if left.publication_date and right.publication_date:
        publication_date = max((left.publication_date, right.publication_date), key=len)
    return Publication(
        title=_longer(left.title, right.title) or left.title,
        providers=list(dict.fromkeys([*left.providers, *right.providers])),
        provider_ids={**right.provider_ids, **left.provider_ids},
        abstract=_longer(left.abstract, right.abstract),
        snippet=_longer(left.snippet, right.snippet),
        authors=max((left.authors, right.authors), key=len),
        publication_date=publication_date,
        year=left.year or right.year,
        venue=left.venue or right.venue,
        doi=left.doi or right.doi,
        pmid=left.pmid or right.pmid,
        url=left.url or right.url,
        citation_count=max(
            (value for value in (left.citation_count, right.citation_count) if value is not None),
            default=None,
        ),
    )


def deduplicate_publications(publications: Iterable[Publication]) -> list[Publication]:
    """Deduplicate by DOI, PMID, then normalized title plus publication year."""
    output: list[Publication] = []
    key_to_index: dict[tuple[str, str], int] = {}
    for publication in publications:
        keys = _identity_keys(publication)
        matches = {
            key_to_index[key]
            for key in keys
            if key in key_to_index and _compatible(output[key_to_index[key]], publication)
        }
        if not matches:
            index = len(output)
            output.append(publication)
        else:
            index = min(matches)
            output[index] = _merge(output[index], publication)
            for duplicate_index in sorted(matches - {index}, reverse=True):
                output[index] = _merge(output[index], output[duplicate_index])
                output.pop(duplicate_index)
                key_to_index = {
                    key: old_index - 1 if old_index > duplicate_index else old_index
                    for key, old_index in key_to_index.items()
                    if old_index != duplicate_index
                }
        for key in _identity_keys(output[index]):
            key_to_index[key] = index
    return output


def search_publications(
    adapters: Sequence[PublicationAdapter], request: SearchRequest
) -> PublicationSearchOutcome:
    """Search providers independently and retain successful partial results."""
    if not adapters:
        raise ValueError("at least one publication adapter is required")
    results = []
    succeeded = []
    errors = {}
    for adapter in adapters:
        try:
            results.extend(adapter.search(request))
            succeeded.append(adapter.provider)
        except PublicationSearchError as error:
            errors[adapter.provider] = str(error)
    return PublicationSearchOutcome(
        publications=deduplicate_publications(results),
        succeeded_providers=succeeded,
        provider_errors=errors,
    )
