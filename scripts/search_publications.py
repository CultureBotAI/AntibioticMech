#!/usr/bin/env python3
"""Search publication APIs for candidate reports of newly discovered antibiotics."""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date
from pathlib import Path

from antibioticmech.publications import (
    DEFAULT_DISCOVERY_QUERY,
    GoogleScholarAdapter,
    PubMedAdapter,
    SearchRequest,
    SemanticScholarAdapter,
    search_publications,
)
from antibioticmech.publications.models import ConfigurationError, PublicationSearchError

PROVIDERS = ("pubmed", "semantic-scholar", "google-scholar")


def iso_date(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("expected an ISO date such as 2026-01-31") from error


def configured_adapters(requested: list[str], environ: dict[str, str]):
    names = list(PROVIDERS) if "all" in requested else list(dict.fromkeys(requested))
    adapters = []
    skipped = []
    for name in names:
        if name == "pubmed":
            adapters.append(
                PubMedAdapter(
                    api_key=environ.get("NCBI_API_KEY"),
                    email=environ.get("NCBI_EMAIL"),
                )
            )
        elif name == "semantic-scholar":
            adapters.append(SemanticScholarAdapter(api_key=environ.get("SEMANTIC_SCHOLAR_API_KEY")))
        elif name == "google-scholar":
            api_key = environ.get("SERPAPI_API_KEY", "")
            if api_key:
                adapters.append(GoogleScholarAdapter(api_key=api_key))
            elif "all" in requested:
                skipped.append("google-scholar (set SERPAPI_API_KEY to enable its SerpAPI adapter)")
            else:
                raise ConfigurationError(
                    "google-scholar requires SERPAPI_API_KEY; Google has no supported Scholar API"
                )
    return adapters, skipped


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--provider",
        action="append",
        choices=("all", *PROVIDERS),
        default=[],
        help="repeat to combine providers; default: PubMed and Semantic Scholar",
    )
    parser.add_argument("--query", default=DEFAULT_DISCOVERY_QUERY)
    parser.add_argument("--since", type=iso_date)
    parser.add_argument("--until", type=iso_date)
    parser.add_argument("--limit", type=int, default=50, help="maximum results requested per provider")
    parser.add_argument("--output", type=Path, help="write JSONL here instead of standard output")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None, *, environ: dict[str, str] | None = None) -> int:
    args = parse_args(argv if argv is not None else sys.argv[1:])
    requested = args.provider or ["pubmed", "semantic-scholar"]
    try:
        effective_environ = environ if environ is not None else dict(os.environ)
        adapters, skipped = configured_adapters(requested, effective_environ)
        request = SearchRequest(
            query=args.query,
            since=args.since,
            until=args.until,
            limit=args.limit,
        )
        publications = search_publications(adapters, request)
    except (ConfigurationError, PublicationSearchError, ValueError) as error:
        print(f"publication search failed: {error}", file=sys.stderr)
        return 1
    for message in skipped:
        print(f"skipped {message}", file=sys.stderr)
    rendered = "".join(json.dumps(item.as_dict(), ensure_ascii=False) + "\n" for item in publications)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
        print(f"wrote {len(publications)} candidates to {args.output}", file=sys.stderr)
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
