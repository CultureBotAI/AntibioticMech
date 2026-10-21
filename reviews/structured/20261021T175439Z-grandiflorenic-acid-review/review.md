# Grandiflorenic acid: corroborated diterpenoid identity and bounded biological claims

- Review: 20261021T175439Z-grandiflorenic-acid-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T17:38:02Z
- Finished UTC: 2026-10-21T17:54:39Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The configured native diterpenoid agrees with ChEBI, PubChem and the asserted ChemSpider record. Original indexed antibacterial and antileishmanial studies support the activity roles; cell-culture and rat-ointment studies support preclinical wound/anti-inflammatory wording. No confirmed native defect was found; detailed activity and molecular-target enrichment remain limited by source access and assay scope. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position514; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:141130 | data/antibiotics/antibacterial/grandiflorenic-acid.yaml | generated | grandiflorenic acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:141130 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:141130 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:141130 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:141130 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:141130 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:141130 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:141130 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:141130 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:141130 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:141130 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:141130 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:141130 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Source reproducibility and scientific status

ownership: supported. Targets: CHEBI:141130.

Original captured inputs, native history and actual source owners are preserved. Saving a review does not promote native curation status.

### Exact structure, names and parent compatibility

identity: supported. Targets: CHEBI:141130.

Seven encodings across native, ChEBI, PubChem and asserted ChemSpider agree. The graph and source-specific names support one configured diterpenoid, rather than a generic kaurane or hydroxylated derivative.

### Antibacterial/antileishmanial roles and preclinical definition

evidence: supported. Targets: CHEBI:141130.

Exact-compound original abstracts support both microbial roles. Host-cell and rat-ointment experiments support preclinical anti-inflammatory/wound activity without establishing human therapeutic efficacy.

### Mechanistic and quantitative enrichment

completeness: unknown. Targets: CHEBI:141130.

No native direct target is asserted. ROS, macrophage responses, plant biosynthesis and derivative cytotoxicity require separate causal interpretation; full antimicrobial methods and source quantity ambiguities constrain optional enrichment.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

If enriching activity, obtain full original assay methods and preserve material/endpoint scope.

- Keep grandiflorenic acid1 distinct from deltoidin A and modified derivatives. Resolve the reported antileishmanial concentration from the original before numerical curation.
- Do not promote preclinical wound, cytokine or ROS responses to approved therapy or direct antibacterial protein targeting.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/grandiflorenic-acid.yaml; Entire native record including every name, parent, role, cross-reference, chemical field and three chronological history entries | supports | The SEEDED exact ChEBI record denotes grandiflorenic acid, C20H28O2, full key RJIPNPHMQGDUBW-RFGKEDTNSA-N. It asserts no structured molecular target, resistance mechanism, quantitative activity observation, producer object or causal graph. All three import history events were read; they are not scientific sign-off. |
| source | data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; 514-source-rows.json; applicable extraction, class precedence and emission rules | supports | The exact adopted row reproduces the imported fields. All original thirteen source/context hashes remain unchanged. Roles are source assertions; exact-compound primary support is assessed separately. Maintained source/extraction ownership controls reproducible corrections. |
| authority | CHEBI:141130; CHEBI:25384; CHEBI:36760; CHEBI:52557; CHEBI:33282; CHEBI:70868; 514-chebi.json; 514-term-*.json; 514-ledger.json | supports | Every asserted ChEBI parent and role resolves to the intended current term. Parent definitions were compared with the actual graph, not accepted solely because upstream repeats them. Current identity, names, formula and charge agree with the adopted row. |
| chemistry | 514-authority-chemistry.json; Independent forward parsing of native, official ChEBI and PubChem SMILES/InChI; 052-root-authorities.py | supports | Six independently parsed encodings reproduce the same full key, formula, neutral charge and masses, with 5 assigned stereocentres and matching stereochemical graph connectivity. |
| ledger | 052-root-ledger.py; 052-root-ledger.log; 514-ledger.json; original capture versus current files | supports | Thirteen original hashes are preserved and unchanged; all 9 adopted PMID records were resolved and their complete indexed abstracts read. The history is chronological. The focused schema and strict checks passed; chemistry results retain actual failures separately. |
| search | 514-local-hits.txt; 052-root-fetch1.json through 052-root-fetch6.json; Ignored-inclusive local search and bounded official-authority / adopted-PMID / original-paper follow-up | context_only | Local searches include hidden and ignored files. Retrieved PubMed name searches are discovery lists, not assertions that every result was read. Native fields contain no named gene/protein/locus/regulator/expression pathway requiring a structured transcriptomics query. Access failures and selected-section reading limits are retained. |
| external | PubChem:12310340; chemspider:24657544; cas:22338-67-6; Official PubChem structure and ChemSpider structured identity response; CAS application route | supports | ChemSpider InChI forward-parses to the exact native key RJIPNPHMQGDUBW-RFGKEDTNSA-N, corroborating all five assigned centres. The current ChEBI source attributes CAS22338-67-6, but direct CAS rendered an application shell, not a verified entry. Native ent-kaurane, tetracyclic diterpenoid and monocarboxylic-acid parents fit. |
| adopted | PMID:15787248,19581023,20116261,29427474,30097110,577885,578433,578458,6540830; All nine complete indexed abstracts | supports | The adopted leads cover lettuce growth, Montanoa biosynthesis, modified derivatives, exact antibacterial/antileishmanial studies, three1979 metabolism/pharmacokinetic/chemical studies and1984 rat uterine responses. Derivative apoptosis potency does not describe parent grandiflorenic acid. The biosynthetic desaturase study uses isotope/oxygen/NADPH experiments; its substrate Km is not a drug-target binding constant. |
| antimicrobial | PMID:29427474; DOI:10.1002/cbdv.201700529; PMID:30097110; DOI:10.1016/j.phymed.2018.06.010; Complete original indexed abstracts; full methods not obtained | supports | Purified grandiflorenic acid is compound1 from Ageratina deltoidea and has reported S. aureus MIC31 micrograms/mL; the E. coli16 value belongs to deltoidin A. The Leishmania amazonensis paper studies parent exposure, promastigotes and macrophage-associated amastigotes, with ROS/apoptosis-like and host IL10/iron responses. Its reported25 nM wording is retained without normalization or target-binding inference. |
| host2013 | Balekar, Nakpheng and Srichana2013; Songklanakarin J Sci Technol35:537–546; https://www.researchgate.net/publication/287426990_Wound-healing_potential_of_grandiflorenic_acid_isolated_from_Wedelia_trilobata_L_leaves; Author-uploaded original abstract, isolation statement and selected fibroblast/HaCaT/scratch-assay Methods via public web text | supports | Previously isolated grandiflorenic acid was used without further repurification. The original reports fibroblast migration/collagen and reduced inflammatory cytokines in RAW264.7 cells, while HaCaT migration/TGF-beta2 did not significantly increase. These are preclinical host-response endpoints; no antibacterial target or human wound efficacy follows. The official journal PDF timed out and direct author-copy download returned403; no local full-text snapshot is claimed. |
| host2017 | DOI:10.22270/jddt.v7i7.1648; https://jddtonline.info/index.php/jddt/article/download/1648/967; All three main-text pages including Methods, Tables1–3 and Discussion; raw histology images not inspected | supports | The original compares0.5% and1% grandiflorenic-acid ointments with vehicle and povidone iodine in groups of six Wistar rats using excision, incision and dead-space wound models. It reports improved closure-related outcomes, tensile strength and hydroxyproline. Table2 labels decreasing values as percentage contraction, a source reporting ambiguity, and text/table day10 versus Methods day11 differ. No precise wound-rate conversion or clinical claim is adopted. |

## Limits And Additional Notes

- All nine adopted abstracts were read, but their full antimicrobial/isolation methods were not obtained. No complete strain, inoculum or MIC protocol is invented.
- The2013 host-cell original was read at selected abstract/Methods scope through an author-uploaded web rendering. Official PDF timeout, alternate tiny HTML response and direct author-page403 prevented a full local PDF inspection.
- The2017 three-page original was read fully as text; raw histology images were not inspected. Its Table2 contraction label and day10/11 reporting are retained as source limitations, not native errors because no quantities are stored.
- Direct CAS exact entry remains unverified; the asserted ChemSpider identity was independently forward-parsed. No raw original NMR or crystallographic data were reanalyzed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native/source bytes, source history, scientific status or earlier immutable review bundles were changed. Original thirteen hashes remain preserved.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T175439Z-grandiflorenic-acid-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Grandiflorenic acid: corroborated diterpenoid identity and bounded biological
  claims'
started_at: '2026-10-21T17:38:02Z'
finished_at: '2026-10-21T17:54:39Z'
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
summary: The configured native diterpenoid agrees with ChEBI, PubChem and the asserted
  ChemSpider record. Original indexed antibacterial and antileishmanial studies support
  the activity roles; cell-culture and rat-ointment studies support preclinical wound/anti-inflammatory
  wording. No confirmed native defect was found; detailed activity and molecular-target
  enrichment remain limited by source access and assay scope. Scientific assessment
  retains the stated evidence limits; full verification is blocked by the shared native-library
  failure.
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
  - path: data/antibiotics/antibacterial/grandiflorenic-acid.yaml
    sha256: 6e8d62bac8921ca64dde46b21e3fcc86db98d0ec498305678d1b348caf6c51ac
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
- target_id: CHEBI:141130
  path: data/antibiotics/antibacterial/grandiflorenic-acid.yaml
  label: grandiflorenic acid
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
  selection: Initially uncovered queue position514; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:141130
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:141130
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    514
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:141130
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/grandiflorenic-acid.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:141130
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/grandiflorenic-acid.yaml --out /private/tmp/am-review-session/514-strict.tsv
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
  - CHEBI:141130
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
  - CHEBI:141130
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
  - CHEBI:141130
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
  - CHEBI:141130
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
  - CHEBI:141130
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
  - CHEBI:141130
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
  - CHEBI:141130
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
  - CHEBI:141130
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
  - CHEBI:141130
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/grandiflorenic-acid.yaml
  locator: Entire native record including every name, parent, role, cross-reference,
    chemical field and three chronological history entries
  accessed_at: '2026-10-21T17:50:34Z'
  support: supports
  summary: The SEEDED exact ChEBI record denotes grandiflorenic acid, C20H28O2, full
    key RJIPNPHMQGDUBW-RFGKEDTNSA-N. It asserts no structured molecular target, resistance
    mechanism, quantitative activity observation, producer object or causal graph.
    All three import history events were read; they are not scientific sign-off.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: 514-source-rows.json; applicable extraction, class precedence and emission
    rules
  accessed_at: '2026-10-21T17:50:34Z'
  support: supports
  summary: The exact adopted row reproduces the imported fields. All original thirteen
    source/context hashes remain unchanged. Roles are source assertions; exact-compound
    primary support is assessed separately. Maintained source/extraction ownership
    controls reproducible corrections.
  snapshot_sha256: a5745c2a8839e504419bcb48ca7fd0ed2d2c944fe3cd6967708e821596ef6d94
- evidence_id: authority
  kind: authority
  reference: CHEBI:141130; CHEBI:25384; CHEBI:36760; CHEBI:52557; CHEBI:33282; CHEBI:70868
  locator: 514-chebi.json; 514-term-*.json; 514-ledger.json
  accessed_at: '2026-10-21T17:50:34Z'
  support: supports
  summary: Every asserted ChEBI parent and role resolves to the intended current term.
    Parent definitions were compared with the actual graph, not accepted solely because
    upstream repeats them. Current identity, names, formula and charge agree with
    the adopted row.
  snapshot_sha256: abf47c9d55a5614c5eb9f7d2b8caaf6cb3b2432e61e91615b1ad5015b48b6767
- evidence_id: chemistry
  kind: validation
  reference: 514-authority-chemistry.json
  locator: Independent forward parsing of native, official ChEBI and PubChem SMILES/InChI;
    052-root-authorities.py
  accessed_at: '2026-10-21T17:50:34Z'
  support: supports
  summary: Six independently parsed encodings reproduce the same full key, formula,
    neutral charge and masses, with 5 assigned stereocentres and matching stereochemical
    graph connectivity.
  snapshot_sha256: 787f774ee3c7285ad10c9ec9b43c2ea42bc50e5607ffd781ea2b8c58ec0e3ece
- evidence_id: ledger
  kind: validation
  reference: 052-root-ledger.py; 052-root-ledger.log
  locator: 514-ledger.json; original capture versus current files
  accessed_at: '2026-10-21T17:50:34Z'
  support: supports
  summary: Thirteen original hashes are preserved and unchanged; all 9 adopted PMID
    records were resolved and their complete indexed abstracts read. The history is
    chronological. The focused schema and strict checks passed; chemistry results
    retain actual failures separately.
  snapshot_sha256: abf47c9d55a5614c5eb9f7d2b8caaf6cb3b2432e61e91615b1ad5015b48b6767
- evidence_id: search
  kind: search
  reference: 514-local-hits.txt; 052-root-fetch1.json through 052-root-fetch6.json
  locator: Ignored-inclusive local search and bounded official-authority / adopted-PMID
    / original-paper follow-up
  accessed_at: '2026-10-21T17:50:34Z'
  support: context_only
  summary: Local searches include hidden and ignored files. Retrieved PubMed name
    searches are discovery lists, not assertions that every result was read. Native
    fields contain no named gene/protein/locus/regulator/expression pathway requiring
    a structured transcriptomics query. Access failures and selected-section reading
    limits are retained.
  search_scope: Own batch052 worktree; rg --no-ignore --hidden with exact grandiflorenic
    acid and CHEBI:141130; all adopted PMIDs; EuropePMC and primary publisher/repository
    follow-up, 2026-10-21.
  snapshot_sha256: 804848ca4d23145894409556c390a9ff8da259e706d8aae52becae45b5c88312
- evidence_id: external
  kind: authority
  reference: PubChem:12310340; chemspider:24657544; cas:22338-67-6
  locator: Official PubChem structure and ChemSpider structured identity response;
    CAS application route
  accessed_at: '2026-10-21T17:50:34Z'
  support: supports
  summary: ChemSpider InChI forward-parses to the exact native key RJIPNPHMQGDUBW-RFGKEDTNSA-N,
    corroborating all five assigned centres. The current ChEBI source attributes CAS22338-67-6,
    but direct CAS rendered an application shell, not a verified entry. Native ent-kaurane,
    tetracyclic diterpenoid and monocarboxylic-acid parents fit.
  snapshot_sha256: 3daabae7505ef21035ab07baee1b57c9eaa5237a5fa61018d2352cf9b57dd0e8
- evidence_id: adopted
  kind: database
  reference: PMID:15787248,19581023,20116261,29427474,30097110,577885,578433,578458,6540830
  locator: All nine complete indexed abstracts
  accessed_at: '2026-10-21T17:50:34Z'
  support: supports
  summary: The adopted leads cover lettuce growth, Montanoa biosynthesis, modified
    derivatives, exact antibacterial/antileishmanial studies, three1979 metabolism/pharmacokinetic/chemical
    studies and1984 rat uterine responses. Derivative apoptosis potency does not describe
    parent grandiflorenic acid. The biosynthetic desaturase study uses isotope/oxygen/NADPH
    experiments; its substrate Km is not a drug-target binding constant.
  snapshot_sha256: 8dff29f74951606c5881efa134430c65ced7edc4b3a79fe19d6490e1acbc987d
- evidence_id: antimicrobial
  kind: primary_source
  reference: PMID:29427474; DOI:10.1002/cbdv.201700529; PMID:30097110; DOI:10.1016/j.phymed.2018.06.010
  locator: Complete original indexed abstracts; full methods not obtained
  accessed_at: '2026-10-21T17:50:34Z'
  support: supports
  summary: Purified grandiflorenic acid is compound1 from Ageratina deltoidea and
    has reported S. aureus MIC31 micrograms/mL; the E. coli16 value belongs to deltoidin
    A. The Leishmania amazonensis paper studies parent exposure, promastigotes and
    macrophage-associated amastigotes, with ROS/apoptosis-like and host IL10/iron
    responses. Its reported25 nM wording is retained without normalization or target-binding
    inference.
  snapshot_sha256: 8dff29f74951606c5881efa134430c65ced7edc4b3a79fe19d6490e1acbc987d
- evidence_id: host2013
  kind: primary_source
  reference: Balekar, Nakpheng and Srichana2013; Songklanakarin J Sci Technol35:537–546;
    https://www.researchgate.net/publication/287426990_Wound-healing_potential_of_grandiflorenic_acid_isolated_from_Wedelia_trilobata_L_leaves
  locator: Author-uploaded original abstract, isolation statement and selected fibroblast/HaCaT/scratch-assay
    Methods via public web text
  accessed_at: '2026-10-21T17:50:34Z'
  support: supports
  summary: Previously isolated grandiflorenic acid was used without further repurification.
    The original reports fibroblast migration/collagen and reduced inflammatory cytokines
    in RAW264.7 cells, while HaCaT migration/TGF-beta2 did not significantly increase.
    These are preclinical host-response endpoints; no antibacterial target or human
    wound efficacy follows. The official journal PDF timed out and direct author-copy
    download returned403; no local full-text snapshot is claimed.
- evidence_id: host2017
  kind: primary_source
  reference: DOI:10.22270/jddt.v7i7.1648; https://jddtonline.info/index.php/jddt/article/download/1648/967
  locator: All three main-text pages including Methods, Tables1–3 and Discussion;
    raw histology images not inspected
  accessed_at: '2026-10-21T17:50:34Z'
  support: supports
  summary: The original compares0.5% and1% grandiflorenic-acid ointments with vehicle
    and povidone iodine in groups of six Wistar rats using excision, incision and
    dead-space wound models. It reports improved closure-related outcomes, tensile
    strength and hydroxyproline. Table2 labels decreasing values as percentage contraction,
    a source reporting ambiguity, and text/table day10 versus Methods day11 differ.
    No precise wound-rate conversion or clinical claim is adopted.
  snapshot_sha256: fc23feaa133cdda3bd5905e4e60543ed917917c288b5db620a02322c91951922
assessments:
- assessment_id: ownership
  area: ownership
  topic: Source reproducibility and scientific status
  outcome: supported
  summary: Original captured inputs, native history and actual source owners are preserved.
    Saving a review does not promote native curation status.
  target_ids:
  - CHEBI:141130
  evidence_ids:
  - native
  - source
  - ledger
- assessment_id: identity
  area: identity
  topic: Exact structure, names and parent compatibility
  outcome: supported
  summary: Seven encodings across native, ChEBI, PubChem and asserted ChemSpider agree.
    The graph and source-specific names support one configured diterpenoid, rather
    than a generic kaurane or hydroxylated derivative.
  target_ids:
  - CHEBI:141130
  evidence_ids:
  - native
  - chemistry
  - external
  - authority
- assessment_id: activity
  area: evidence
  topic: Antibacterial/antileishmanial roles and preclinical definition
  outcome: supported
  summary: Exact-compound original abstracts support both microbial roles. Host-cell
    and rat-ointment experiments support preclinical anti-inflammatory/wound activity
    without establishing human therapeutic efficacy.
  target_ids:
  - CHEBI:141130
  evidence_ids:
  - antimicrobial
  - host2013
  - host2017
- assessment_id: optional
  area: completeness
  topic: Mechanistic and quantitative enrichment
  outcome: unknown
  summary: No native direct target is asserted. ROS, macrophage responses, plant biosynthesis
    and derivative cytotoxicity require separate causal interpretation; full antimicrobial
    methods and source quantity ambiguities constrain optional enrichment.
  target_ids:
  - CHEBI:141130
  evidence_ids:
  - adopted
  - antimicrobial
  - host2017
  - search
findings: []
actions:
- action_id: A1
  description: If enriching activity, obtain full original assay methods and preserve
    material/endpoint scope.
  finding_ids: []
  target_ids:
  - CHEBI:141130
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/grandiflorenic-acid.yaml
    role: Optional evidence-backed activity curation
  acceptance_checks:
  - Keep grandiflorenic acid1 distinct from deltoidin A and modified derivatives.
    Resolve the reported antileishmanial concentration from the original before numerical
    curation.
  - Do not promote preclinical wound, cytokine or ROS responses to approved therapy
    or direct antibacterial protein targeting.
limitations:
- All nine adopted abstracts were read, but their full antimicrobial/isolation methods
  were not obtained. No complete strain, inoculum or MIC protocol is invented.
- The2013 host-cell original was read at selected abstract/Methods scope through an
  author-uploaded web rendering. Official PDF timeout, alternate tiny HTML response
  and direct author-page403 prevented a full local PDF inspection.
- The2017 three-page original was read fully as text; raw histology images were not
  inspected. Its Table2 contraction label and day10/11 reporting are retained as source
  limitations, not native errors because no quantities are stored.
- Direct CAS exact entry remains unverified; the asserted ChemSpider identity was
  independently forward-parsed. No raw original NMR or crystallographic data were
  reanalyzed.
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
