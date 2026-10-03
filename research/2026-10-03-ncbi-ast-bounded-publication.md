# NCBI AST bounded publication audit

Date: 2026-10-03. Source status remains `EVALUATING`.

## Scope and reproducibility

PR #1027 follows the lossless activity-collection work in #1024. It replaces
unbounded activity tables with static pages, whole-compound search, on-demand
complete evidence and complete expanded-record downloads. No evaluated NCBI AST
inventory or observation was added to the committed production corpus.

The final audit ran at `624ddb2a160255d5be28494b526b799f5ba3dc0e`:

```bash
uv run python scripts/audit_ncbi_ast_publication.py \
  --activity-report reports/ncbi_ast_assay_reviewed_2026-10-03/activity.tsv \
  --output-directory reports/ncbi_ast_browser_reviewed_2026-10-03 \
  --full-site
```

The input report SHA-256 is
`9ab2302b437ae2bb5a5aeec058fd21ba4cb11e0aeab58011b50f63e3288c0a80`.
The output `audit.json` SHA-256 is
`e932c0ccd52acae7bc900ea00c4801ef0c276cdf83e5b95e62c711103d8c8a34`.
Elapsed time was 538.498 seconds. All pinned input hashes remained unchanged
during the run. Outputs are evaluation artifacts under ignored `reports/`.

The preceding full run at `62a155425eb39a27e16ed794b5285a327802e274` is retained
under `reports/ncbi_ast_browser_2026-10-03`; its audit SHA-256 is
`764dcb6ba73ad12c1b7bdfe8969943ac78a9652aa0c7edccfb684495d9bf0707`.
The final run includes both adversarial-review fixes described below.

## Verified coverage

| Check | Result |
| --- | ---: |
| Affected compounds | 32 |
| Unaffected records, unchanged | 2907 |
| AST observations | 188759 |
| Sum of AST measurement_count | 188759 |
| All activity rows on affected compounds | 190833 |
| Observations retaining paired genome contexts | 52 |
| Static activity pages for affected compounds | 1925 |
| Maximum observations per page | 100 |
| Full-site compound records | 2939 |
| Full-site activity pages, including unaffected compounds | 1970 |
| Local page/download/style/script targets checked | 261075 |
| Largest full-site activity HTML page, bytes | 119745 |

The measurement-count sum is not independent verification of distinct biological
experiments. The earlier assay, taxonomy and BioSample reviews retain their
stated scope and limitations.

For every affected compound, the audit checks the closed-schema write, complete
reload equality, unchanged reseeding, every displayed scientific cell and
ordinal anchor, each complete page-data envelope, evidence bindings, exact
search-index/browser bindings and complete expanded-record JSON equality.
The full-site overlay retains all unaffected records, compares every audited
compressed asset with its full-site counterpart, and checks local link targets.

## Size tradeoff

The following are the per-record audit artifacts; their footers omit the
full-site extraction date, matching the earlier audit's footer treatment.

| Artifact | Bytes |
| --- | ---: |
| Physical YAML plus lossless activity collections | 24863430 |
| Main record HTML, bounded previews | 2095606 |
| Static activity-page HTML | 217743824 |
| Complete expanded-record downloads | 20426752 |
| Browser search and complete page-data assets | 33142994 |
| Total affected record/publication artifacts | 298272606 |

This is 56.29% smaller than the earlier 682442946-byte affected YAML/HTML
combination. Pagination and evidence bindings increase aggregate HTML relative
to the old 120944491-byte unbounded HTML; the benefit is bounded per-page work,
complete downloads, and the large lossless record-storage reduction. This is
not a claim that pagination alone reduces aggregate HTML.

The complete evaluated site, including unaffected compounds, is 310325762 bytes.
Its filled-in footers add ten bytes per HTML page to the per-record views.

Tetracycline retains 17700 AST observations and 17720 total activity rows across
178 pages. Its full-site record page is 102628 bytes, its largest activity page
119698 bytes, and its complete-record download 1902810 bytes. The preceding
unbounded record page was 11259459 bytes.

## Browser and regression checks

Final live QA used Chrome 154.0.8037.97 against the reviewed full-site output at
1440x1000 and 390x844. Both viewports passed actual complete-record download
equality, first/last observation evidence, paired-context list structure,
cross-page accession search, activity filtering, bounded result pagination,
direct page selection, empty results and reset. There were no page errors or
document-level horizontal overflows. The scientific tables retain their named,
keyboard-focusable horizontal scroll regions.

Corrupt search data and missing evidence data both displayed retriable errors;
successful retries loaded checked data. With JavaScript disabled, static
pagination and complete/page-data downloads remained accessible.

QA output: `reports/ncbi_ast_browser_reviewed_qa_2026-10-03/browser-qa.json`,
SHA-256 `46184fe3834538ef0a30c20a98a2855c9239396b4ead49c97f916cac90fe06e9`.
The same directory contains desktop/mobile screenshots. The reproducible QA
entry point is `scripts/check_activity_browser.cjs` with Playwright on
`NODE_PATH`, the served first activity-page URL and an output directory.

The focused publication/storage/schema-boundary suite passed 120 tests.
Documentation checks passed 14 tests. All 2939 production records passed
closed-schema validation; the production site regenerated byte-identically.
Lint, source-queue and diff checks passed. Linux PR QC is tracked separately.

## Adversarial review and remaining gates

- #1028: the original audit checked the index asset but not the browser root's
  index URL and identity bindings. Negative reproductions confirmed false
  passes. The final verifier checks exactly one root and rejects incorrect,
  absent, duplicated or duplicate-attribute bindings.
- #1029: collection-only physical records could bypass the expanded-input
  precondition through the empty-list return. The guard now runs first, with a
  regression proving such records cannot silently look empty.

Both fixes are in `624ddb2a1`; valid published scientific content is unchanged.
Source adoption still needs the separately deferred source-terms decision and
a publishable source inventory. The current 103014679-byte reviewed TSV
compresses losslessly with `gzip -n` to 8228267 bytes. Compressed inventory
support must preserve the logical-content hashes used by assay/BioSample
reviews and the source-adoption gate; no compressed inventory was committed.
Quarantined assay contexts and unmapped antibiotic identities remain curation
work. These results do not independently verify phenotypes or re-identify
isolates.
