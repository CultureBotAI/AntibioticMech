# Gypsogenic acid: corroborated triterpene and exact oral-pathogen activity

- Review: 20261021T175759Z-gypsogenic-acid-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T17:38:05Z
- Finished UTC: 2026-10-21T17:57:59Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The configured3beta-hydroxyoleanene diacid agrees with native, ChEBI and PubChem representations and the adopted original structure figure. Exact gypsogenic acid oral-pathogen results support the antibacterial role. A separate adopted cytotoxicity study is negative at its tested limit for this compound. No confirmed native defect was found. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position519; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:71531 | data/antibiotics/antibacterial/gypsogenic-acid.yaml | generated | gypsogenic acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:71531 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:71531 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:71531 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:71531 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:71531 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:71531 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:71531 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:71531 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:71531 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:71531 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:71531 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:71531 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Source reproducibility and scientific status

ownership: supported. Targets: CHEBI:71531.

Original captured inputs, native history and actual source owners are preserved. Saving a review does not promote native curation status.

### Exact diacid structure, stereochemistry and names

identity: supported. Targets: CHEBI:71531.

All six native/authority encodings agree, and original Figure1 supports the3beta hydroxy23/28 diacid assignment. Hydroxy-carboxylic-acid and pentacyclic-triterpenoid parents are compatible.

### Pure-compound antibacterial evidence

evidence: supported. Targets: CHEBI:71531.

The original compound4 result supports antibacterial filing with exact strain, assay and endpoint scope. No relative potency of ursolic/oleanolic acids or other triterpenes is assigned to gypsogenic acid.

### Quantitative activity, mechanism and registry verification

completeness: unknown. Targets: CHEBI:71531.

Original numerical observations are available for optional curation. No direct antibacterial target is established; cancer-cell negatives and structure–activity speculation are separate evidence. Exact MetaCyc/Reaxys structures remain unverified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

If adding activity observations, curate the exact compound4 TableII data with the original assay scope.

- Preserve the six exact strains, concentrations,10% DMSO, medium, inoculum description,37°C/24h and resazurin endpoint; do not silently normalize to another standard assay.
- Keep inactive cancer-cell compound8 and potent other triterpenes separate; no inferred direct target or clinical anticaries efficacy.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/gypsogenic-acid.yaml; Entire native record including every name, parent, role, cross-reference, chemical field and three chronological history entries | supports | The SEEDED exact ChEBI record denotes gypsogenic acid, C30H46O5, full key PAIBKVQNJKUVCE-JUENUIDLSA-N. It asserts no structured molecular target, resistance mechanism, quantitative activity observation, producer object or causal graph. All three import history events were read; they are not scientific sign-off. |
| source | data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; 519-source-rows.json; applicable extraction, class precedence and emission rules | supports | The exact adopted row reproduces the imported fields. All original thirteen source/context hashes remain unchanged. Roles are source assertions; exact-compound primary support is assessed separately. Maintained source/extraction ownership controls reproducible corrections. |
| authority | CHEBI:71531; CHEBI:24669; CHEBI:25872; CHEBI:33282; 519-chebi.json; 519-term-*.json; 519-ledger.json | supports | Every asserted ChEBI parent and role resolves to the intended current term. Parent definitions were compared with the actual graph, not accepted solely because upstream repeats them. Current identity, names, formula and charge agree with the adopted row. |
| chemistry | 519-authority-chemistry.json; Independent forward parsing of native, official ChEBI and PubChem SMILES/InChI; 052-root-authorities.py | supports | Six independently parsed encodings reproduce the same full key, formula, neutral charge and masses, with 9 assigned stereocentres and matching stereochemical graph connectivity. |
| ledger | 052-root-ledger.py; 052-root-ledger.log; 519-ledger.json; original capture versus current files | supports | Thirteen original hashes are preserved and unchanged; all 2 adopted PMID records were resolved and their complete indexed abstracts read. The history is chronological. The focused schema and strict checks passed; chemistry results retain actual failures separately. |
| search | 519-local-hits.txt; 052-root-fetch1.json through 052-root-fetch6.json; Ignored-inclusive local search and bounded official-authority / adopted-PMID / original-paper follow-up | context_only | Local searches include hidden and ignored files. Retrieved PubMed name searches are discovery lists, not assertions that every result was read. Native fields contain no named gene/protein/locus/regulator/expression pathway requiring a structured transcriptomics query. Access failures and selected-section reading limits are retained. |
| oral2007 | PMID:18069238; DOI:10.1515/znc-2007-9-1007; https://www.researchgate.net/publication/5779585_Antibacterial_Activity_of_Triterpene_Acids_and_Semi-Synthetic_Derivatives_against_Oral_Pathogens; Original full main text via publisher-supplied public web rendering; isolation, Methods, TablesI–II and Discussion; raw figure pixels not inspected | supports | Gypsogenic acid4 derives from Miconia stenostachya. TableII gives MIC200,70,60,50,200,100 micrograms/mL respectively for E.faecalis4082, S.salivarius25975, S.sanguinis10556, S.mitis49456, S.mutans25275 and S.sobrinus33478, all ATCC. Triplicate broth microdilution used tryptone soya broth,20–300 micrograms/mL,10% DMSO control, reported inoculum10^8 CFU/mL,37°C/24h and resazurin readout; chlorhexidine was positive control. The more potent30–80 range belongs to ursolic/oleanolic acid. Structure–activity discussion is not direct molecular-target evidence. |
| cytotox2007 | PMID:17827765; DOI:10.1248/cpb.55.1376; https://www.jstage.jst.go.jp/article/cpb/55/9/55_9_1376/_pdf; Complete three-page original main text; actual Figure1 and Table2 page images inspected | supports | Aceriphyllum rossii voucherCNU-908 yielded15mg gypsogenic acid8; Figure1 shows3beta-hydroxy,23/28 diacid constitution. MTT experiments after48h exposure report IC50 greater than100 micromolar in both K562 and HL60 for8, unlike active27-oic-acid congeners1–6. Neither the title nor their cytotoxic/ACAT discussion supports those activities for gypsogenic acid. |
| adopted | PMID:17827765;PMID:18069238; Both complete indexed abstracts; both main originals additionally read at specified depths | supports | Both adopted papers were resolved. The oral-pathogen original supports antibacterial activity; the cancer-cell original provides exact isolation/structure and a bounded negative result. Neither supplies a native antibacterial protein target. |
| food2014 | PMID:25172756; DOI:10.1016/j.foodchem.2014.07.105; Complete indexed original abstract | supports | The Akebia trifoliata pericarp study names gypsogenic acid10 among isolated triterpenes, but its strong0.9–15.6 micrograms/mL antibacterial values are for compounds4,6,11. No compound10 potency is transferred from that abstract. |
| external | PubChem:15560324; metacyc.compound:CPD-9474; reaxys:3228938; Current exact ChEBI/PubChem entries and direct MetaCyc endpoint | supports | PubChem corroborates all nine assigned centres and the neutral diacid. MetaCyc getxml returned account/login HTML rather than an inspectable structure; direct Reaxys was not accessed. These native identifiers remain source-attributed without independent exact-registry certification. |

## Limits And Additional Notes

- The2007 antibacterial original was read through a public full-text rendering; publisher and legacy PDF routes returned challenges/HTML and direct author-copy fetching returned403. Raw structure figure pixels from that paper were not inspected.
- The separate2007 cytotoxic original PDF was read completely, with actual Figure1 and Table2 images inspected. Raw spectra were not reprocessed. The2014 Akebia paper remains abstract-level.
- A2021 phytopathogen study was discovered but its publisher route returned403; no quantitative result from a search snippet is adopted. Direct MetaCyc and proprietary Reaxys equivalence remain unresolved.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native/source bytes, source history, scientific status or earlier immutable review bundles were changed. Original thirteen hashes remain preserved.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T175759Z-gypsogenic-acid-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Gypsogenic acid: corroborated triterpene and exact oral-pathogen activity'
started_at: '2026-10-21T17:38:05Z'
finished_at: '2026-10-21T17:57:59Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the native record. The entire record
    and maintained source were read, independent chemistry calculated, asserted chemical
    groundings checked and exact-compound primary literature assessed with explicit
    access boundaries.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: The configured3beta-hydroxyoleanene diacid agrees with native, ChEBI and
  PubChem representations and the adopted original structure figure. Exact gypsogenic
  acid oral-pathogen results support the antibacterial role. A separate adopted cytotoxicity
  study is negative at its tested limit for this compound. No confirmed native defect
  was found. Scientific assessment retains the stated evidence limits; full verification
  is blocked by the shared native-library failure.
source:
  git_revision: baf3b3203d748d098686e166cdb2a6138f47eb59
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 5e2e1f975f8aa64f92a06c134c98c750c968fd78f02620a73c9cb611ac018ed8
    role: context
  - path: conf/sources.yaml
    sha256: 4a2dcd7a3a88953b6cb35b51a48ed77b626c3af2cbb542b0d38ba10540ed7df9
    role: context
  - path: curation/curator_antibiotics.tsv
    sha256: 224cbb7261add427184b2762a29c2ff3e85c85e0a06cf22b144545346487247b
    role: context
  - path: curation/decisions.tsv
    sha256: a5834b44307b0449b0df9362c551b7fcd707f3ae51f73d429d37d51f5a169d61
    role: context
  - path: data/antibiotics/antibacterial/gypsogenic-acid.yaml
    sha256: 66fba9fa9a412b5e78a3a82546d03ec5d8d09314fe7da6f0147b58178cdb1227
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 25f0d80c0bf26da7741a1514a5e1759dde484ab054f0f56df7938bdda8383a91
    role: context
  - path: data/raw/chebi_antimicrobials.tsv
    sha256: 4c33e56c3c342be657309f720f5b5cb9cad1fae13bec202ef99e449503c32004
    role: context
  - path: data/raw/chebi_role_names.tsv
    sha256: 5c476c0aacd7c98d7241d2343a6fc41ee9eb9338077404c5b011a04bf40c6ac5
    role: context
  - path: docs/CURATION.md
    sha256: a364598a9c2bdaf9e0e71895d5b7a2fd61d3e726e0ed0da12bd895cc4c30e98c
    role: context
  - path: docs/HARMONIZATION.md
    sha256: fb8b58abca016ca5a7d856fcc6f1ec2deb210e0927394a480853830b39e1f060
    role: context
  - path: scripts/extract_source_inventory.py
    sha256: bb1606fd07cd8187640b5200a21ec090bb06683397d691e87ddd6884ea768860
    role: context
  - path: scripts/seed_from_sources.py
    sha256: be66eca74d22a3daa9ac6ff73d437c6c56e8d85b97f6877fdf3de77e2ab64680
    role: context
  - path: src/antibioticmech/schema/antibioticmech.yaml
    sha256: de62be2dd2dd55f141a0c14ff666eaa00efc6f3b431d651d0196ebcfddfbb301
    role: context
targets:
- target_id: CHEBI:71531
  path: data/antibiotics/antibacterial/gypsogenic-acid.yaml
  label: gypsogenic acid
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position519; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:71531
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:71531
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    519
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:71531
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/gypsogenic-acid.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:71531
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/gypsogenic-acid.yaml --out /private/tmp/am-review-session/519-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:71531
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just qc
  exit_code: 2
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-verify-corpus
  name: Generated corpus reproduction
  status: passed
  required: true
  summary: 2939 expected and present; zero missing, unexpected, drifted fields or
    lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic
    retained.
  target_ids:
  - CHEBI:71531
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just verify-corpus
    --summary
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-review-queue
  name: Native review-readiness inventory
  status: passed
  required: false
  summary: 2859 native unsigned readiness rows written; this status queue does not
    determine structured-review coverage.
  target_ids:
  - CHEBI:71531
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just review-queue
    --limit 0 --tsv /private/tmp/am-review-session/native-queue.tsv
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-tests-platform-partial
  name: Supplementary test suite with two unavailable modules excluded
  status: passed
  required: false
  summary: 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy
    native library were explicitly excluded; this does not replace full QC.
  target_ids:
  - CHEBI:71531
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q -ra --ignore=tests/test_chemical_embedding.py --ignore=tests/test_chemical_map_site.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-validate-all
  name: Full closed-schema validation
  status: passed
  required: true
  summary: 2939 files, zero ERROR rows.
  target_ids:
  - CHEBI:71531
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-all
    --quiet --workers 2 --out /private/tmp/am-review-session/corpus-validation.tsv
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-chemical-map-check
  name: Chemical map consistency
  status: failed
  required: false
  summary: Exited 1 on the same pinned SciPy native library import failure.
  target_ids:
  - CHEBI:71531
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just chemical-map-check
  exit_code: 1
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-render-check
  name: Generated site consistency
  status: passed
  required: false
  summary: 2939 compound pages and seven class pages current.
  target_ids:
  - CHEBI:71531
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just render-check
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-report
  name: Corpus statistics
  status: passed
  required: false
  summary: Corpus report completed successfully.
  target_ids:
  - CHEBI:71531
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just report
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
- check_id: shared-corpus-integrity
  name: Full-corpus history/evidence/reference invariants
  status: passed
  required: true
  summary: 23 full-corpus integrity tests passed, including seed history, evidence
    placement and internal references.
  target_ids:
  - CHEBI:71531
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/gypsogenic-acid.yaml
  locator: Entire native record including every name, parent, role, cross-reference,
    chemical field and three chronological history entries
  accessed_at: '2026-10-21T17:50:34Z'
  support: supports
  summary: The SEEDED exact ChEBI record denotes gypsogenic acid, C30H46O5, full key
    PAIBKVQNJKUVCE-JUENUIDLSA-N. It asserts no structured molecular target, resistance
    mechanism, quantitative activity observation, producer object or causal graph.
    All three import history events were read; they are not scientific sign-off.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: 519-source-rows.json; applicable extraction, class precedence and emission
    rules
  accessed_at: '2026-10-21T17:50:34Z'
  support: supports
  summary: The exact adopted row reproduces the imported fields. All original thirteen
    source/context hashes remain unchanged. Roles are source assertions; exact-compound
    primary support is assessed separately. Maintained source/extraction ownership
    controls reproducible corrections.
  snapshot_sha256: 5dbdcca933120c6e87aa0c3e1a3b24025158631332249d02e55e98ce511f089c
- evidence_id: authority
  kind: authority
  reference: CHEBI:71531; CHEBI:24669; CHEBI:25872; CHEBI:33282
  locator: 519-chebi.json; 519-term-*.json; 519-ledger.json
  accessed_at: '2026-10-21T17:50:34Z'
  support: supports
  summary: Every asserted ChEBI parent and role resolves to the intended current term.
    Parent definitions were compared with the actual graph, not accepted solely because
    upstream repeats them. Current identity, names, formula and charge agree with
    the adopted row.
  snapshot_sha256: e3e4c9be1cdbf0b86172c0fb722afb659f587ba7aaf29006c68382b832c19d96
- evidence_id: chemistry
  kind: validation
  reference: 519-authority-chemistry.json
  locator: Independent forward parsing of native, official ChEBI and PubChem SMILES/InChI;
    052-root-authorities.py
  accessed_at: '2026-10-21T17:50:34Z'
  support: supports
  summary: Six independently parsed encodings reproduce the same full key, formula,
    neutral charge and masses, with 9 assigned stereocentres and matching stereochemical
    graph connectivity.
  snapshot_sha256: 00438ed2c542f84836bc28cc98c416bb07c56a683fe48deee6b783db565be037
- evidence_id: ledger
  kind: validation
  reference: 052-root-ledger.py; 052-root-ledger.log
  locator: 519-ledger.json; original capture versus current files
  accessed_at: '2026-10-21T17:50:34Z'
  support: supports
  summary: Thirteen original hashes are preserved and unchanged; all 2 adopted PMID
    records were resolved and their complete indexed abstracts read. The history is
    chronological. The focused schema and strict checks passed; chemistry results
    retain actual failures separately.
  snapshot_sha256: e3e4c9be1cdbf0b86172c0fb722afb659f587ba7aaf29006c68382b832c19d96
- evidence_id: search
  kind: search
  reference: 519-local-hits.txt; 052-root-fetch1.json through 052-root-fetch6.json
  locator: Ignored-inclusive local search and bounded official-authority / adopted-PMID
    / original-paper follow-up
  accessed_at: '2026-10-21T17:50:34Z'
  support: context_only
  summary: Local searches include hidden and ignored files. Retrieved PubMed name
    searches are discovery lists, not assertions that every result was read. Native
    fields contain no named gene/protein/locus/regulator/expression pathway requiring
    a structured transcriptomics query. Access failures and selected-section reading
    limits are retained.
  search_scope: Own batch052 worktree; rg --no-ignore --hidden with exact gypsogenic
    acid and CHEBI:71531; all adopted PMIDs; EuropePMC and primary publisher/repository
    follow-up, 2026-10-21.
  snapshot_sha256: bf64bfda985c2a04a219ce7a1ce87d6cbda5136d649f11abc908cd3d67300a92
- evidence_id: oral2007
  kind: primary_source
  reference: PMID:18069238; DOI:10.1515/znc-2007-9-1007; https://www.researchgate.net/publication/5779585_Antibacterial_Activity_of_Triterpene_Acids_and_Semi-Synthetic_Derivatives_against_Oral_Pathogens
  locator: Original full main text via publisher-supplied public web rendering; isolation,
    Methods, TablesI–II and Discussion; raw figure pixels not inspected
  accessed_at: '2026-10-21T17:50:34Z'
  support: supports
  summary: Gypsogenic acid4 derives from Miconia stenostachya. TableII gives MIC200,70,60,50,200,100
    micrograms/mL respectively for E.faecalis4082, S.salivarius25975, S.sanguinis10556,
    S.mitis49456, S.mutans25275 and S.sobrinus33478, all ATCC. Triplicate broth microdilution
    used tryptone soya broth,20–300 micrograms/mL,10% DMSO control, reported inoculum10^8
    CFU/mL,37°C/24h and resazurin readout; chlorhexidine was positive control. The
    more potent30–80 range belongs to ursolic/oleanolic acid. Structure–activity discussion
    is not direct molecular-target evidence.
- evidence_id: cytotox2007
  kind: primary_source
  reference: PMID:17827765; DOI:10.1248/cpb.55.1376; https://www.jstage.jst.go.jp/article/cpb/55/9/55_9_1376/_pdf
  locator: Complete three-page original main text; actual Figure1 and Table2 page
    images inspected
  accessed_at: '2026-10-21T17:50:34Z'
  support: supports
  summary: Aceriphyllum rossii voucherCNU-908 yielded15mg gypsogenic acid8; Figure1
    shows3beta-hydroxy,23/28 diacid constitution. MTT experiments after48h exposure
    report IC50 greater than100 micromolar in both K562 and HL60 for8, unlike active27-oic-acid
    congeners1–6. Neither the title nor their cytotoxic/ACAT discussion supports those
    activities for gypsogenic acid.
  snapshot_sha256: 0b9ab94ebb444d9779ee3c59a692703170068cdc76994b5c6f2b1d2f4c0550ed
- evidence_id: adopted
  kind: database
  reference: PMID:17827765;PMID:18069238
  locator: Both complete indexed abstracts; both main originals additionally read
    at specified depths
  accessed_at: '2026-10-21T17:50:34Z'
  support: supports
  summary: Both adopted papers were resolved. The oral-pathogen original supports
    antibacterial activity; the cancer-cell original provides exact isolation/structure
    and a bounded negative result. Neither supplies a native antibacterial protein
    target.
  snapshot_sha256: 7556e5ac91dd0201efb236372b62c25bfbf52d1c3e852d86834db14d99137e9c
- evidence_id: food2014
  kind: primary_source
  reference: PMID:25172756; DOI:10.1016/j.foodchem.2014.07.105
  locator: Complete indexed original abstract
  accessed_at: '2026-10-21T17:50:34Z'
  support: supports
  summary: The Akebia trifoliata pericarp study names gypsogenic acid10 among isolated
    triterpenes, but its strong0.9–15.6 micrograms/mL antibacterial values are for
    compounds4,6,11. No compound10 potency is transferred from that abstract.
  snapshot_sha256: 7e7ac3867ce9971dc34a45a57a4e8b26be4b1de98963a480a714937d6262b173
- evidence_id: external
  kind: authority
  reference: PubChem:15560324; metacyc.compound:CPD-9474; reaxys:3228938
  locator: Current exact ChEBI/PubChem entries and direct MetaCyc endpoint
  accessed_at: '2026-10-21T17:50:34Z'
  support: supports
  summary: PubChem corroborates all nine assigned centres and the neutral diacid.
    MetaCyc getxml returned account/login HTML rather than an inspectable structure;
    direct Reaxys was not accessed. These native identifiers remain source-attributed
    without independent exact-registry certification.
  snapshot_sha256: 385fd1f98685f2c60871bbf71973a35a971183e5c280e829d5fa98a424d849dc
assessments:
- assessment_id: ownership
  area: ownership
  topic: Source reproducibility and scientific status
  outcome: supported
  summary: Original captured inputs, native history and actual source owners are preserved.
    Saving a review does not promote native curation status.
  target_ids:
  - CHEBI:71531
  evidence_ids:
  - native
  - source
  - ledger
- assessment_id: identity
  area: identity
  topic: Exact diacid structure, stereochemistry and names
  outcome: supported
  summary: All six native/authority encodings agree, and original Figure1 supports
    the3beta hydroxy23/28 diacid assignment. Hydroxy-carboxylic-acid and pentacyclic-triterpenoid
    parents are compatible.
  target_ids:
  - CHEBI:71531
  evidence_ids:
  - native
  - chemistry
  - authority
  - cytotox2007
- assessment_id: activity
  area: evidence
  topic: Pure-compound antibacterial evidence
  outcome: supported
  summary: The original compound4 result supports antibacterial filing with exact
    strain, assay and endpoint scope. No relative potency of ursolic/oleanolic acids
    or other triterpenes is assigned to gypsogenic acid.
  target_ids:
  - CHEBI:71531
  evidence_ids:
  - oral2007
  - adopted
  - food2014
- assessment_id: optional
  area: completeness
  topic: Quantitative activity, mechanism and registry verification
  outcome: unknown
  summary: Original numerical observations are available for optional curation. No
    direct antibacterial target is established; cancer-cell negatives and structure–activity
    speculation are separate evidence. Exact MetaCyc/Reaxys structures remain unverified.
  target_ids:
  - CHEBI:71531
  evidence_ids:
  - oral2007
  - cytotox2007
  - external
  - search
findings: []
actions:
- action_id: A1
  description: If adding activity observations, curate the exact compound4 TableII
    data with the original assay scope.
  finding_ids: []
  target_ids:
  - CHEBI:71531
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/gypsogenic-acid.yaml
    role: Optional primary activity evidence
  acceptance_checks:
  - Preserve the six exact strains, concentrations,10% DMSO, medium, inoculum description,37°C/24h
    and resazurin endpoint; do not silently normalize to another standard assay.
  - Keep inactive cancer-cell compound8 and potent other triterpenes separate; no
    inferred direct target or clinical anticaries efficacy.
limitations:
- The2007 antibacterial original was read through a public full-text rendering; publisher
  and legacy PDF routes returned challenges/HTML and direct author-copy fetching returned403.
  Raw structure figure pixels from that paper were not inspected.
- The separate2007 cytotoxic original PDF was read completely, with actual Figure1
  and Table2 images inspected. Raw spectra were not reprocessed. The2014 Akebia paper
  remains abstract-level.
- A2021 phytopathogen study was discovered but its publisher route returned403; no
  quantitative result from a search snippet is adopted. Direct MetaCyc and proprietary
  Reaxys equivalence remain unresolved.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native/source bytes, source history, scientific status or earlier immutable review
  bundles were changed. Original thirteen hashes remain preserved.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
