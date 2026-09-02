"""Publication discovery adapters for antimicrobial curation."""

from .discovery import deduplicate_publications, search_publications
from .google_scholar import GoogleScholarAdapter
from .models import DEFAULT_DISCOVERY_QUERY, Publication, SearchRequest
from .pubmed import PubMedAdapter
from .semantic_scholar import SemanticScholarAdapter

__all__ = [
    "DEFAULT_DISCOVERY_QUERY",
    "GoogleScholarAdapter",
    "Publication",
    "PubMedAdapter",
    "SearchRequest",
    "SemanticScholarAdapter",
    "deduplicate_publications",
    "search_publications",
]
