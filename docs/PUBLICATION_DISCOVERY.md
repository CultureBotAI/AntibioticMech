# Publication discovery adapters

`just search-publications` searches for candidate papers reporting newly
discovered antibiotics and emits normalized JSON Lines. Search hits are leads,
not evidence that a compound is novel or antimicrobial; a curator must verify
the paper before adding a claim to the corpus.

The adapters use supported APIs:

- PubMed uses the NCBI E-utilities
  [ESearch and EFetch contract](https://www.ncbi.nlm.nih.gov/books/NBK25499/).
  `NCBI_API_KEY` is optional at the public request rate. `NCBI_EMAIL` is also
  optional and is transmitted only when the caller explicitly sets it.
- Semantic Scholar uses the
  [Academic Graph API](https://www.semanticscholar.org/product/api).
  `SEMANTIC_SCHOLAR_API_KEY` is optional for public endpoints and recommended
  by the provider for stable rate limits.
- Google does not expose a supported Google Scholar API. The Google Scholar
  adapter therefore uses SerpAPI's documented
  [Google Scholar engine](https://serpapi.com/google-scholar-api), requires
  `SERPAPI_API_KEY`, and never scrapes Scholar HTML directly.

Examples:

```bash
# The default uses only PubMed and Semantic Scholar.
just search-publications --since 2026-01-01 --limit 50

# One provider and a custom discovery query.
just search-publications --provider pubmed \
  --query '"new antibiotic" AND Streptomyces' \
  --output /tmp/antibiotic-publications.jsonl

# Google Scholar is never implicit because SerpAPI searches may be billable.
just search-publications --provider google-scholar --since 2026-01-01 --limit 20
```

Each result keeps provider identifiers and normalizes title, abstract versus
search snippet, authors, publication date, venue, DOI, PMID, URL, and citation
count where the provider supplies them. Cross-provider results are merged by
DOI, then PMID, then normalized title plus year. Conflicting DOI or PMID values
are never merged solely because their titles match. The shared default query
uses Boolean syntax understood by PubMed and Google Scholar; the Semantic
Scholar adapter converts it to the plain-text form required by its relevance
endpoint while retaining the search terms.

Limits are per provider. PubMed retrieval is batched and paced to NCBI's public
or API-key request rate, and Semantic Scholar pagination is paced to its
documented introductory key rate. A Google Scholar request uses one SerpAPI
search for each results page, so larger limits can consume multiple paid API
searches.
