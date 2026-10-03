# NCBI AST expanded-cohort publication audit

Date: 2026-10-03

This non-publishing audit exercises the production storage, schema, merge and
rendering paths for the [expanded exact-drug cohort](2026-10-03-ncbi-ast-drug-coverage.md).
NCBI AST remains `EVALUATING`. Neither the inventory nor the staged records and
pages are adopted or committed to the production corpus.

## Inputs and reproducibility

The audit ran at `cd04b3159ce2d6f2f9781e0983b748419d8819a9` with the canonical
expanded assay and BioSample reviews. Its input manifest hashes the compressed
inventory, production records and collections, source inputs, configuration,
curation files, Python scripts, schemas, validated writer and templates. The
audit checked those files again before completing; none changed during the run.
The source-queue prose was updated only after completion. The documentation,
documentation test and optional browser-QA script changes do not alter the
audited converter, writer or renderer.

| Artifact | SHA-256 |
|---|---|
| Compressed activity inventory | `4f396c7843750066afb8225832ac6023305779a4bcd037940de8ff8d0149b4f2` |
| Expanded activity report | `bcac2fb84c9f7df5d78fab90f330738e31dcdb7b82bc3dfc7069a351edacc41a` |
| Canonical BioSample review | `4ca294f58d57e627753e033ab2d3ee29d7c54ea10111bd24b534ddde69f72fbb` |
| Production-path audit JSON | `d19e0b2d403671627023f4cc0f843a6f215b37d4c0821f84efb56a85380675f0` |
| Cefotaxime browser-QA JSON | `08b594edb565cff99423dd0be37cdd0153a73238a8ff9061f159327c2d716000` |
| Cefovecin browser-QA JSON | `8aca766f07305ae622c7c9ff6a452f4d98074913bce34525fd7f0f579d3aa01c` |
| Browser-QA script used | `069c9932f04161baeee7a68c638addc1476d231656c52cc6c6d8935506aabb9b` |

All generated artifacts remain under ignored `reports/` directories. The
compressed inventory is 8,924,250 bytes and expands to 116,223,537 exact TSV
bytes containing 213,144 reviewed source groups. Source-verified repeated-target
consolidation yields 213,082 observations; it does not drop paired genome
contexts or merge distinct assays.

```bash
.venv/bin/python3 scripts/audit_ncbi_ast_publication.py \
  --activity-report reports/ncbi_ast_drug_expanded_compressed_2026-10-03/activity.tsv.gz \
  --output-directory reports/ncbi_ast_drug_expanded_publication_2026-10-03 \
  --full-site
```

Use a fresh output directory for a repeat; the audit refuses overwrites. Old
cohorts require their matching historical review files. The live
[inventory guide](../docs/NCBI_AST_INVENTORY.md) now pins the expanded cohort and
explains that boundary; a regression test compares its stated logical checksum
with the canonical review.

## Full publication results

The complete audit finished successfully in 603.663 seconds. It covers
production merging with pre-existing evidence, closed-schema writing, complete
expanded-record reload equality, unchanged reseeding, rendered activity-cell
comparisons, complete evidence assets, search-index bindings and expanded-record
downloads. The full-site build also compares its evidence/download bytes with
the individually audited artifacts and resolves every local target.

| Check or artifact | Result |
|---|---:|
| Affected compound records | 40 |
| Unaffected records unchanged | 2,899 |
| NCBI AST observations and measurements | 213,082 |
| Observations retaining paired genome contexts | 62 |
| Total activity rows on affected records, including other sources | 215,183 |
| Affected record YAML bytes | 4,133,187 |
| Lossless collection bytes / files | 23,552,278 / 443 |
| Affected main record HTML bytes | 2,419,264 |
| Affected activity pages | 2,173 |
| Affected activity HTML bytes | 245,326,737 |
| Largest affected activity HTML file, bytes | 119,735 |
| Complete expanded-download bytes | 23,081,866 |
| Browser data bytes | 37,422,717 |
| Full-site compound pages | 2,939 |
| Full-site local targets resolved | 290,175 |

These are evaluation-snapshot quantities, not new production-corpus counts.
The audit does not independently verify submitted phenotypes, establish
species-wide resistance, resolve source terms or authorize adoption.

## Live browser verification

The staged site was served locally on port 8770. The optional Playwright check
ran against actual Chrome `154.0.8037.97` at 1440 x 1000 and 390 x 844 for
cefotaxime and cefovecin. Screenshots at both sizes were inspected: controls and
headings remain separate, and wide tables stay within their scroll containers
without horizontal document overflow.

| Record | All activity rows | Rows with no categorical call | Paired-context observations |
|---|---:|---:|---:|
| Cefotaxime (`CHEBI:204928`) | 2,023 | 88 | 2 |
| Cefovecin (`antibioticmech:aro-c73757ed91`) | 3,369 | 3,349 | 0 |

For each viewport the check verified the actual downloaded expanded JSON,
first/last observation evidence values, cross-page search reaching the final
observation, page jumping, categorical filters, result pagination, empty state
and reset. Cefotaxime additionally exercised nested paired-context evidence;
cefovecin has no such observation and does not claim that coverage.

The added missing-call regression checks the exact match count, first 50
observation identifiers and `Not reported` labels. It does not invent a
resistance call from a measured MIC. The cefotaxime count includes pre-existing
non-AST evidence as well as AST rows. Both runs also verified corrupt-search
retry, missing-evidence retry and no-JavaScript pagination/download links.

```bash
NODE_PATH=/private/tmp/antibioticmech-browser-qa/node_modules \
  node scripts/check_activity_browser.cjs \
  http://127.0.0.1:8770/antibacterial/cefotaxime/activity-1.html \
  reports/ncbi_ast_drug_expanded_browser_qa_2026-10-03/cefotaxime

NODE_PATH=/private/tmp/antibioticmech-browser-qa/node_modules \
  node scripts/check_activity_browser.cjs \
  http://127.0.0.1:8770/antibacterial/cefovecin/activity-1.html \
  reports/ncbi_ast_drug_expanded_browser_qa_2026-10-03/cefovecin
```

`NODE_PATH` identifies the local Playwright installation, not a new production
dependency. Each drug directory contains `browser-qa.json` and default-view and
missing-call-filter screenshots for both viewport widths.

## Remaining integration gates

The expanded cohort has now passed the production-path and representative
live-browser gates that previously covered only the older cohort. Required
Linux QC and adversarial review still apply to the final PR head and merge
sequence. Adoption remains separate: resolve the deferred source-terms decision,
add the source configuration and committed inventory/provenance entry, then
validate and publish the adopted corpus. Unmapped labels and quarantined assay
contexts remain curation work, not implicit resistance evidence.
