# Activity publication

The renderer consumes fully expanded records, including external activity
collections resolved by `load_record`. Storage layout never limits publication
coverage. `scripts/activity_pages.py` owns the activity assets and views;
`scripts/render_pages.py` includes every generated path in its pruning set and
every activity HTML page in the sitemap.

## Views

- Record pages show all activity rows up to the page bound, or a small preview
  with an explicit total and a link to the complete activity browser.
- Activity pages contain at most 100 observations in original record order.
  Static first/previous/next/last links work without JavaScript. Row anchors use
  the one-based position in the complete expanded activity list.
- Search covers the whole compound, not just the current page. It includes
  taxon, strain, assay, source observation identity and all singleton and paired
  genome accessions. Activity and source filters preserve unreported values as
  a separate option. Search results are paged at 50 rows.
- Each evidence disclosure loads a complete observation on demand, including
  provenance, evidence notes and paired contexts. Source strings are rendered
  as text, not HTML. The page-data download remains accessible without scripts.

## Downloads

Each activity directory contains deterministic gzip-compressed UTF-8 JSON.
Filenames end in the SHA-256 of the compressed bytes. Gzip timestamps and
filenames are omitted so regeneration is byte-identical.

- `record-<sha256>.json.gz`: the complete expanded record, including every
  activity and every non-activity field. There are no external collection
  references to resolve after download.
- `activity-N-<sha256>.json.gz`: an envelope with format
  `antibioticmech-activity-page-v1`, record identifier, Standard InChIKey, total
  observations, zero-based offset and complete observations for that page.
- `search-<sha256>.json.gz`: an `antibioticmech-activity-index-v1` envelope with
  the same identity and total. Rows contain ordinal, taxon label, taxon CURIE,
  strain, activity, source, accessions and normalized search text.

The browser checks compressed hashes, envelope identity and row coverage before
displaying downloaded data. Compressed and expanded browser payloads are bounded
at 16 MiB; generation fails rather than silently truncating an oversized index
or evidence page. The complete-record download is not subject to the browser
payload bound and is not loaded by the browsing UI. Browsers without gzip-stream
or cryptographic digest support retain static pagination and downloads.

## Verification

`tests/test_activity_pages.py` checks page boundaries, complete download equality,
paired-context search coverage, corrupt/missing data, generated-file pruning and
sitemap coverage. Its Node regression also exercises browser payload validation,
filtering, request caching and retry behavior.

The NCBI publication audit checks every scientific cell, row anchor, evidence
binding, compressed page, search row and complete record. `--full-site` also
renders the full corpus with audited records overlaid, compares all audited
compressed assets, and checks local page, download, stylesheet and script links.
This remains an evaluation under `reports/`, not source adoption.

Optional live-browser QA uses `scripts/check_activity_browser.cjs` with Playwright
on `NODE_PATH`, a local first activity-page URL and an output directory. It
records desktop/mobile screenshots and checks search, evidence, navigation,
filters, bounded result pagination, retry states and no-JavaScript access.
