# Review of chloroeremomycin

- Review: 20261021T130342Z-chloroeremomycin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:48:36Z
- Finished UTC: 2026-10-21T13:03:42Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The neutral chloroeremomycin graph agrees with current ChEBI, PubChem, ChEMBL and KEGG representations. Original isolation and direct comparison support the producer and Chloroorienticin A synonym; the D-Ala-D-Ala precursor target is transparently database-only and consistent with original NMR binding evidence. No demonstrated native scientific defect was found. KNApSAcK has contradictory encodings and the legacy PDB-CCD link could not be resolved; these limitations prevent complete external-link sign-off without showing that the native structure is wrong. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire SEEDED, EXACT chloroeremomycin record, including definition, synonym, classification, neutral structure, all eight xrefs, two source concepts, one database target assertion and four history events.

Selection: Queue 291; thirteen initial hashes preserved and two actual ARO owners appended, yielding fifteen unchanged inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:29556 | data/antibiotics/antibacterial/chloroeremomycin.yaml | generated | chloroeremomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema validation | passed | True | CHEBI:29556 | Exit 0. |
| Documented strict validation | passed | True | CHEBI:29556 | Exit 0; no ERROR rows. |
| Supplemental chemistry and source comparison | passed | False | CHEBI:29556 | Exit 0. Native structure is internally consistent and agrees with four current chemical authorities. KNApSAcK internal inconsistency was reproduced; this diagnostic pass is not exact-link sign-off. |
| Initial supplemental source selector | failed | False | CHEBI:29556 | Exit 1: an initial broad all-row-text selector also included oritavancin definitions mentioning chloroeremomycin. This supplemental script was narrowed to the exact source name and rerun. |
| Corrected supplemental source reconciliation | passed | False | CHEBI:29556 | Exit 0; fifteen unchanged hashes, exact source fields, five adopted PMID dispositions and four history events reconciled. |
| Structured adapter applicability | not_applicable | False | CHEBI:29556 | The only native target is a chemical cell-wall precursor component with no organism, gene, protein, regulator or expression dataset. Biosynthetic enzymes encountered in source papers are not proposed antibacterial targets. No substitute protein or organism query was used. |
| Authoritative full QC | failed | True | CHEBI:29556 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:29556 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:29556 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:29556 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:29556 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:29556 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:29556 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:29556 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:29556 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Native graph and exact synonym

identity: supported. Targets: CHEBI:29556.

Current independent compound structures agree; original structure and paired-comparison papers support the named natural product and synonym.

### Legacy and inconsistent external references

identity: unknown. Targets: CHEBI:29556.

KNApSAcK has contradictory encodings despite a matching SMILES; VAX could not be resolved. CAS is corroborated by official chemical databases, while the proprietary Reaxys record was not independently opened. No confirmed different-compound native link is asserted.

### Classification and producer wording

grounding: supported. Targets: CHEBI:29556.

The three-sugar glycopeptide structure, original fermentation isolation and S. aureus results support the classification and producer definition.

### Precursor-component target

evidence: supported. Targets: CHEBI:29556.

Database scope is accurately labeled and original exact-compound NMR provides qualitative binding support. Detailed whole-cell causal effects remain outside this review evidence.

### Source ownership and citation disposition

provenance: supported. Targets: CHEBI:29556.

All five adopted PMID leads have explicit dispositions and actual ARO owners were captured; biosynthesis and analog activity remain separate.

### Optional primary enrichment

completeness: supported. Targets: CHEBI:29556.

Primary synonym, producer and binding evidence could enrich future curation, but omitted optional fields are not defects in this SEEDED record. Exact MIC adoption needs material and assay reconciliation.

### Focused native validity

schema: supported. Targets: CHEBI:29556.

Documented schema and strict checks pass.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/chloroeremomycin.yaml; Entire native record and all four history events | supports | The record contains a neutral three-sugar glycopeptide, one exact synonym and one explicitly database-only cell-wall-component target. It asserts no MIC, resistance phenotype, protein target, clinical product, structured producer or causal graph. SEEDED status does not claim completed curation. |
| chemistry | CHEBI:29556; PubChem:445806; CHEMBL1688951; KEGG:C12014; 291-chemistry.py/.json; current official compound JSON and molfile snapshots | supports | Native SMILES and InChI normalize to XJHXLMVKYIVZTE-LOALFDMRSA-N, C73H88Cl2N10O26, charge zero and the reported monoisotopic mass. Native SMILES, ChEBI molfile, PubChem SMILES, ChEMBL SMILES and KEGG molfile have identical canonical stereochemical graphs. Direct reconstruction from InChI uses a different mobile-hydrogen representation, but its round-trip standard InChI and key equal the native values; this is not evidence of a structural conflict. |
| external-links | KNApSAcK:C00017622; pdb-ccd:VAX; PDB:1GAC; 291-knapsack.html,291-chemistry.json,291-fetch.json,291-follow-fetch.json,291-third-fetch.json,291-1gac.json | context_only | KNApSAcK names the exact compound and its SMILES agrees with native, but its displayed InChI differs at one configured glucose center and recomputes to IUTPGODTSA-N; the displayed key UDEFMIKCNA-N is a third value. A single-center inversion control reproduces the InChI difference. This is an internally inconsistent external record, not proof that the native graph is wrong. VAX requests to RCSB API/CIF and PDBe API returned 404. Current1GAC identifies Chloroorienticin A through BIRD PRD_000203 and separated peptide/sugar entities; the precise VAX replacement was not verified. No arbitrary component or BIRD identifier was substituted. |
| discovery | PMID:3272137; DOI:10.7164/antibiotics.41.1506; 291-1988.pdf: complete five-page report, Figure 1 and Table 2 page 1509 visually inspected | supports | The original work isolates chloroorienticins from A. orientalis PA-45052 fermentation broth. Chloroorienticin A is distinguished by two chlorines, D-glucose and two L-4-epi-vancosamine units; NMR, degradation and conversion to orienticin/vancomycin aglycone support its structure. Table 2 reports activity against two named S. aureus strains, including methicillin-resistant 3131, supporting antibacterial classification. The characterized material is a hydrochloride hydrate, and the short report lacks a complete susceptibility protocol; its numeric MICs were not imported as neutral-compound observations. |
| synonym | PMID:2793597; DOI:10.7164/antibiotics.42.1438; 291-1989.pdf: complete three-page report, Figure 1, Table 1 and experimental hydrolysis | supports | Direct comparison of A82846B and Chloroorienticin A gives coelution of the mixed samples and matching UV profiles. Parallel selective hydrolysis relates their B/C products without identifying those products as A. This supports the exact native synonym and the A82846B name used in the binding paper. |
| target | ARO:3000720; ARO:3000184; Adopted aro_target_edges.tsv exact row;291-aro-target.json and291-aro.json | supports | The adopted exact edge is acyl-D-alanyl-D-alanine targeted by chloroeremomycin. Current OLS describes the terminal peptidoglycan-precursor group and retains the target term. The native target is correctly typed CELL_WALL_COMPONENT/ATTACKED_COMPONENT and explicitly DATABASE_ASSERTION_ONLY; no bacterial species, assay or protein identity is fabricated. The current target-term definition citation is not treated as a newly adopted exact-compound experimental citation. |
| binding | PMID:7626632; DOI:10.1021/bi00029a041; PDB:1GAC; Complete original abstract in291-extra-core.json and original deposited structural-study record291-1gac.json | supports | The original NMR study uses experimental NOESY/COSY constraints to determine A82846B asymmetric-dimer complexes with a cell-wall pentapeptide, reporting interactions at the terminal D-alanine carboxylate pocket. This supplies exact-compound physical binding context consistent with the native precursor target. The full publisher main article was not obtained; the deposited entry and complete original abstract support this qualitative statement, not an independently audited live-cell inhibition or quantitative affinity claim. |
| biosynthesis | PMID:11035791; PMID:15070728; 291-2000.html and291-2004.html: original Introduction, relevant Methods, Results and Discussion | supports | The 2000 work reconstitutes TDP-L-epivancosamine biosynthesis with purified enzymes. The 2004 work uses A. orientalis A82846 genes and sequential GtfA/GtfC reactions, HPLC and MALDI to reconstitute chloroeremomycin after prior GtfB glucosylation. These support sugar identity and producer/biosynthetic context. They do not show chloroeremomycin inhibits these biosynthetic enzymes, and derivative oritavancin activity is kept separate. |
| leads | Five adopted source PMID leads; 291-lead-dispositions.json;291-core.json | supports | All five adopted records and complete abstracts were inspected. PMID 9545426 supplies producer/alias/biosynthesis context; 11035791 has relevant full-body inspection; 11294642 concerns glycosyltransferase maturation and hybrid glycopeptides; 11942828 measures chloroeremomycin cooperativity with indole-2-carboxylic acid, not directly the native dipeptide or a live-cell MIC; 25940955 is a review. Four additional original sources have separate dispositions. No secondary review or biosynthetic substrate assay is promoted to primary antibacterial-target evidence. |
| owners | data/raw/chebi_antimicrobials.tsv;data/raw/aro_antibiotics.tsv;data/raw/aro_target_edges.tsv;scripts/extract_source_inventory.py;scripts/seed_from_sources.py; 291-source-audit.json and291-ledger-attempts.json | supports | Native structure and definition reproduce ChEBI; ARO supplies classification/links and the database target. All fifteen preserved input hashes remain unchanged and four history events are coherent. The first supplemental selector failed because it included an oritavancin row mentioning its precursor; the corrected exact-name selector passed and the failure remains in the ledger. |
| search | Exact local and public chloroeremomycin discovery; Initial ignored-inclusive local search for chloroeremomycin, CHEBI:29556 and source identifiers; public primary title/DOI, A82846B and Chloroorienticin A queries | context_only | Ignored files were included in local discovery. Original producer, synonym and binding sources were located. Search results for oritavancin, eremomycin and biosynthetic enzymes were not treated as exact antibacterial assays. Public retrieval failures are recorded in the fetch manifests. |
| validation | Documented focused validators; 291-schema.log,291-strict.log and291-strict.tsv | supports | Schema and strict validators both exit 0. Supplemental source/chemical checks are distinct from the shared full-corpus gates. |

## Limits And Additional Notes

- KNApSAcK C00017622 has a native-equivalent SMILES, a single-center conflicting InChI and a third displayed key; its exact identity link needs upstream clarification. This does not establish a native stereochemical defect.
- The legacy PDB-CCD VAX routes returned 404. The inspected current 1GAC entry points to BIRD PRD_000203, but a formal VAX replacement mapping was not verified.
- The proprietary Reaxys entry was not independently accessed; CAS 118395-73-6 is corroborated by current official chemical records rather than a separate CAS structure record.
- The 1995 binding source was inspected through its complete original abstract and deposited experimental structural entry; its full main paper was not freely obtained. Detailed affinity, live-cell causality and organism-specific target claims are not inferred.
- Three adopted primary papers were inspected at complete-abstract depth; 11035791 additionally at relevant full-body depth, and 25940955 is a review. Exact source depths are listed in the lead ledger.
- The original isolation paper characterizes hydrochloride-hydrate material and provides only abbreviated MIC reporting. Its numeric values were not transferred to the neutral native representation.
- Primary structure drawings and chemical correlations were inspected; every stereocenter was not independently reconstructed from raw spectra.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native record or maintained source input was changed. All fifteen input hashes were rechecked.
- All optional tags and references concern chloroeremomycin; biosynthetic enzymes and semisynthetic oritavancin are explicitly separated.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T130342Z-chloroeremomycin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of chloroeremomycin
started_at: '2026-10-21T12:48:36Z'
finished_at: '2026-10-21T13:03:42Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Full native record inspected against preserved inputs and public
    primary evidence; actual ARO identity and target owners captured before detailed
    judgment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
native_verdict: Native identity and bounded database target supported; legacy external
  links remain unresolved
scientific_review: true
summary: The neutral chloroeremomycin graph agrees with current ChEBI, PubChem, ChEMBL
  and KEGG representations. Original isolation and direct comparison support the producer
  and Chloroorienticin A synonym; the D-Ala-D-Ala precursor target is transparently
  database-only and consistent with original NMR binding evidence. No demonstrated
  native scientific defect was found. KNApSAcK has contradictory encodings and the
  legacy PDB-CCD link could not be resolved; these limitations prevent complete external-link
  sign-off without showing that the native structure is wrong. Scientific assessment
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
  - path: data/antibiotics/antibacterial/chloroeremomycin.yaml
    sha256: 89a25d1a9b96de76420b57c114ce4d74481741b61cf16a77b58ef405967f2f5b
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
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: Adopted ARO identity and publication leads
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: Adopted acyl-D-alanyl-D-alanine target edge
scope:
  description: Entire SEEDED, EXACT chloroeremomycin record, including definition,
    synonym, classification, neutral structure, all eight xrefs, two source concepts,
    one database target assertion and four history events.
  selection: Queue 291; thirteen initial hashes preserved and two actual ARO owners
    appended, yielding fifteen unchanged inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:29556
targets:
- target_id: CHEBI:29556
  path: data/antibiotics/antibacterial/chloroeremomycin.yaml
  label: chloroeremomycin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI and CARD/ARO source and target extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity and publication leads
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Adopted acyl-D-alanyl-D-alanine target edge
checks:
- check_id: schema
  name: Documented schema validation
  status: passed
  required: true
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/chloroeremomycin.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0.
  target_ids:
  - CHEBI:29556
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict validation
  status: passed
  required: true
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/chloroeremomycin.yaml --out /private/tmp/am-review-session/291-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; no ERROR rows.
  target_ids:
  - CHEBI:29556
  evidence_ids:
  - validation
- check_id: chemistry
  name: Supplemental chemistry and source comparison
  status: passed
  required: false
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/291-chemistry.py
    > /private/tmp/am-review-session/291-chemistry.log
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0. Native structure is internally consistent and agrees with four
    current chemical authorities. KNApSAcK internal inconsistency was reproduced;
    this diagnostic pass is not exact-link sign-off.
  target_ids:
  - CHEBI:29556
  evidence_ids:
  - chemistry
- check_id: source-initial
  name: Initial supplemental source selector
  status: failed
  required: false
  command: .venv/bin/python /private/tmp/am-review-session/291-ledger.py
  exit_code: 1
  expected_exit_code: 0
  summary: 'Exit 1: an initial broad all-row-text selector also included oritavancin
    definitions mentioning chloroeremomycin. This supplemental script was narrowed
    to the exact source name and rerun.'
  target_ids:
  - CHEBI:29556
  evidence_ids:
  - owners
- check_id: source-reconciliation
  name: Corrected supplemental source reconciliation
  status: passed
  required: false
  command: .venv/bin/python /private/tmp/am-review-session/291-ledger.py
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; fifteen unchanged hashes, exact source fields, five adopted PMID
    dispositions and four history events reconciled.
  target_ids:
  - CHEBI:29556
  evidence_ids:
  - owners
  - leads
- check_id: structured-adapter
  name: Structured adapter applicability
  status: not_applicable
  required: false
  summary: The only native target is a chemical cell-wall precursor component with
    no organism, gene, protein, regulator or expression dataset. Biosynthetic enzymes
    encountered in source papers are not proposed antibacterial targets. No substitute
    protein or organism query was used.
  target_ids:
  - CHEBI:29556
  evidence_ids:
  - record
  - target
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:29556
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
  - CHEBI:29556
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
  - CHEBI:29556
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
  - CHEBI:29556
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
  - CHEBI:29556
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
  - CHEBI:29556
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
  - CHEBI:29556
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
  - CHEBI:29556
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
  - CHEBI:29556
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/chloroeremomycin.yaml
  locator: Entire native record and all four history events
  accessed_at: '2026-10-21T12:53:55Z'
  support: supports
  summary: The record contains a neutral three-sugar glycopeptide, one exact synonym
    and one explicitly database-only cell-wall-component target. It asserts no MIC,
    resistance phenotype, protein target, clinical product, structured producer or
    causal graph. SEEDED status does not claim completed curation.
- evidence_id: chemistry
  kind: validation
  reference: CHEBI:29556; PubChem:445806; CHEMBL1688951; KEGG:C12014
  locator: 291-chemistry.py/.json; current official compound JSON and molfile snapshots
  accessed_at: '2026-10-21T12:53:55Z'
  support: supports
  summary: Native SMILES and InChI normalize to XJHXLMVKYIVZTE-LOALFDMRSA-N, C73H88Cl2N10O26,
    charge zero and the reported monoisotopic mass. Native SMILES, ChEBI molfile,
    PubChem SMILES, ChEMBL SMILES and KEGG molfile have identical canonical stereochemical
    graphs. Direct reconstruction from InChI uses a different mobile-hydrogen representation,
    but its round-trip standard InChI and key equal the native values; this is not
    evidence of a structural conflict.
  snapshot_sha256: f5cb4a51cd8cd4bd482e74d12991376bf039965734f4d19b4fb8943af83a3c0b
- evidence_id: external-links
  kind: authority
  reference: KNApSAcK:C00017622; pdb-ccd:VAX; PDB:1GAC
  locator: 291-knapsack.html,291-chemistry.json,291-fetch.json,291-follow-fetch.json,291-third-fetch.json,291-1gac.json
  accessed_at: '2026-10-21T12:53:55Z'
  support: context_only
  summary: KNApSAcK names the exact compound and its SMILES agrees with native, but
    its displayed InChI differs at one configured glucose center and recomputes to
    IUTPGODTSA-N; the displayed key UDEFMIKCNA-N is a third value. A single-center
    inversion control reproduces the InChI difference. This is an internally inconsistent
    external record, not proof that the native graph is wrong. VAX requests to RCSB
    API/CIF and PDBe API returned 404. Current1GAC identifies Chloroorienticin A through
    BIRD PRD_000203 and separated peptide/sugar entities; the precise VAX replacement
    was not verified. No arbitrary component or BIRD identifier was substituted.
  snapshot_sha256: a129a29ab1b6347a40409e81a219aea52bf4fb4a51df4e7af8fb5067cdc418f6
- evidence_id: discovery
  kind: primary_source
  reference: PMID:3272137; DOI:10.7164/antibiotics.41.1506
  locator: '291-1988.pdf: complete five-page report, Figure 1 and Table 2 page 1509
    visually inspected'
  accessed_at: '2026-10-21T12:53:55Z'
  support: supports
  summary: The original work isolates chloroorienticins from A. orientalis PA-45052
    fermentation broth. Chloroorienticin A is distinguished by two chlorines, D-glucose
    and two L-4-epi-vancosamine units; NMR, degradation and conversion to orienticin/vancomycin
    aglycone support its structure. Table 2 reports activity against two named S.
    aureus strains, including methicillin-resistant 3131, supporting antibacterial
    classification. The characterized material is a hydrochloride hydrate, and the
    short report lacks a complete susceptibility protocol; its numeric MICs were not
    imported as neutral-compound observations.
  snapshot_sha256: 548d3265cbdb704e3ff998089417a0117eabfd5d1bc7e67d75ee1b7fc5e0e35c
- evidence_id: synonym
  kind: primary_source
  reference: PMID:2793597; DOI:10.7164/antibiotics.42.1438
  locator: '291-1989.pdf: complete three-page report, Figure 1, Table 1 and experimental
    hydrolysis'
  accessed_at: '2026-10-21T12:53:55Z'
  support: supports
  summary: Direct comparison of A82846B and Chloroorienticin A gives coelution of
    the mixed samples and matching UV profiles. Parallel selective hydrolysis relates
    their B/C products without identifying those products as A. This supports the
    exact native synonym and the A82846B name used in the binding paper.
  snapshot_sha256: b44447716c5737194ce2b062bacfba1b15e35ea308e0ab7b825273b349249e94
- evidence_id: target
  kind: database
  reference: ARO:3000720; ARO:3000184
  locator: Adopted aro_target_edges.tsv exact row;291-aro-target.json and291-aro.json
  accessed_at: '2026-10-21T12:53:55Z'
  support: supports
  summary: The adopted exact edge is acyl-D-alanyl-D-alanine targeted by chloroeremomycin.
    Current OLS describes the terminal peptidoglycan-precursor group and retains the
    target term. The native target is correctly typed CELL_WALL_COMPONENT/ATTACKED_COMPONENT
    and explicitly DATABASE_ASSERTION_ONLY; no bacterial species, assay or protein
    identity is fabricated. The current target-term definition citation is not treated
    as a newly adopted exact-compound experimental citation.
  snapshot_sha256: 534741c5aad9c4d64d6ec6418b0b07c41719610357f1a6aec2435bb84034d992
- evidence_id: binding
  kind: primary_source
  reference: PMID:7626632; DOI:10.1021/bi00029a041; PDB:1GAC
  locator: Complete original abstract in291-extra-core.json and original deposited
    structural-study record291-1gac.json
  accessed_at: '2026-10-21T12:53:55Z'
  support: supports
  summary: The original NMR study uses experimental NOESY/COSY constraints to determine
    A82846B asymmetric-dimer complexes with a cell-wall pentapeptide, reporting interactions
    at the terminal D-alanine carboxylate pocket. This supplies exact-compound physical
    binding context consistent with the native precursor target. The full publisher
    main article was not obtained; the deposited entry and complete original abstract
    support this qualitative statement, not an independently audited live-cell inhibition
    or quantitative affinity claim.
  snapshot_sha256: e033fb44e9a40200e39af047e45a77256e37e8d7cfa9e5680a0debf3757948e0
- evidence_id: biosynthesis
  kind: primary_source
  reference: PMID:11035791; PMID:15070728
  locator: '291-2000.html and291-2004.html: original Introduction, relevant Methods,
    Results and Discussion'
  accessed_at: '2026-10-21T12:53:55Z'
  support: supports
  summary: The 2000 work reconstitutes TDP-L-epivancosamine biosynthesis with purified
    enzymes. The 2004 work uses A. orientalis A82846 genes and sequential GtfA/GtfC
    reactions, HPLC and MALDI to reconstitute chloroeremomycin after prior GtfB glucosylation.
    These support sugar identity and producer/biosynthetic context. They do not show
    chloroeremomycin inhibits these biosynthetic enzymes, and derivative oritavancin
    activity is kept separate.
  snapshot_sha256: 95b5db28e43f4174c166e42c4decdbfde4e9da590cc0d1233fbb094cc1d49e76
- evidence_id: leads
  kind: database
  reference: Five adopted source PMID leads
  locator: 291-lead-dispositions.json;291-core.json
  accessed_at: '2026-10-21T12:53:55Z'
  support: supports
  summary: All five adopted records and complete abstracts were inspected. PMID 9545426
    supplies producer/alias/biosynthesis context; 11035791 has relevant full-body
    inspection; 11294642 concerns glycosyltransferase maturation and hybrid glycopeptides;
    11942828 measures chloroeremomycin cooperativity with indole-2-carboxylic acid,
    not directly the native dipeptide or a live-cell MIC; 25940955 is a review. Four
    additional original sources have separate dispositions. No secondary review or
    biosynthetic substrate assay is promoted to primary antibacterial-target evidence.
  snapshot_sha256: edaff7d2db57a1704fa128d0f6d358cf7f782d8f2998655e012d5b407c1fc81d
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv;data/raw/aro_antibiotics.tsv;data/raw/aro_target_edges.tsv;scripts/extract_source_inventory.py;scripts/seed_from_sources.py
  locator: 291-source-audit.json and291-ledger-attempts.json
  accessed_at: '2026-10-21T12:53:55Z'
  support: supports
  summary: Native structure and definition reproduce ChEBI; ARO supplies classification/links
    and the database target. All fifteen preserved input hashes remain unchanged and
    four history events are coherent. The first supplemental selector failed because
    it included an oritavancin row mentioning its precursor; the corrected exact-name
    selector passed and the failure remains in the ledger.
  snapshot_sha256: 1570d08f6878adbd83da58214c94aa8ddc15754f38efb298ee1efce99086c8fc
- evidence_id: search
  kind: search
  reference: Exact local and public chloroeremomycin discovery
  locator: Initial ignored-inclusive local search for chloroeremomycin, CHEBI:29556
    and source identifiers; public primary title/DOI, A82846B and Chloroorienticin
    A queries
  accessed_at: '2026-10-21T12:53:55Z'
  support: context_only
  summary: Ignored files were included in local discovery. Original producer, synonym
    and binding sources were located. Search results for oritavancin, eremomycin and
    biosynthetic enzymes were not treated as exact antibacterial assays. Public retrieval
    failures are recorded in the fetch manifests.
  search_scope: Initial ignored-inclusive local search for chloroeremomycin, CHEBI:29556
    and source identifiers; public primary title/DOI, A82846B and Chloroorienticin
    A queries
- evidence_id: validation
  kind: validation
  reference: Documented focused validators
  locator: 291-schema.log,291-strict.log and291-strict.tsv
  accessed_at: '2026-10-21T12:53:55Z'
  support: supports
  summary: Schema and strict validators both exit 0. Supplemental source/chemical
    checks are distinct from the shared full-corpus gates.
assessments:
- assessment_id: identity
  area: identity
  topic: Native graph and exact synonym
  outcome: supported
  summary: Current independent compound structures agree; original structure and paired-comparison
    papers support the named natural product and synonym.
  target_ids:
  - CHEBI:29556
  evidence_ids:
  - chemistry
  - discovery
  - synonym
- assessment_id: external
  area: identity
  topic: Legacy and inconsistent external references
  outcome: unknown
  summary: KNApSAcK has contradictory encodings despite a matching SMILES; VAX could
    not be resolved. CAS is corroborated by official chemical databases, while the
    proprietary Reaxys record was not independently opened. No confirmed different-compound
    native link is asserted.
  target_ids:
  - CHEBI:29556
  evidence_ids:
  - external-links
  - chemistry
- assessment_id: class
  area: grounding
  topic: Classification and producer wording
  outcome: supported
  summary: The three-sugar glycopeptide structure, original fermentation isolation
    and S. aureus results support the classification and producer definition.
  target_ids:
  - CHEBI:29556
  evidence_ids:
  - discovery
  - biosynthesis
  - chemistry
- assessment_id: mechanism
  area: evidence
  topic: Precursor-component target
  outcome: supported
  summary: Database scope is accurately labeled and original exact-compound NMR provides
    qualitative binding support. Detailed whole-cell causal effects remain outside
    this review evidence.
  target_ids:
  - CHEBI:29556
  evidence_ids:
  - target
  - binding
  - leads
- assessment_id: sources
  area: provenance
  topic: Source ownership and citation disposition
  outcome: supported
  summary: All five adopted PMID leads have explicit dispositions and actual ARO owners
    were captured; biosynthesis and analog activity remain separate.
  target_ids:
  - CHEBI:29556
  evidence_ids:
  - owners
  - leads
- assessment_id: completeness
  area: completeness
  topic: Optional primary enrichment
  outcome: supported
  summary: Primary synonym, producer and binding evidence could enrich future curation,
    but omitted optional fields are not defects in this SEEDED record. Exact MIC adoption
    needs material and assay reconciliation.
  target_ids:
  - CHEBI:29556
  evidence_ids:
  - record
  - discovery
  - binding
- assessment_id: schema
  area: schema
  topic: Focused native validity
  outcome: supported
  summary: Documented schema and strict checks pass.
  target_ids:
  - CHEBI:29556
  evidence_ids:
  - validation
findings: []
actions: []
limitations:
- KNApSAcK C00017622 has a native-equivalent SMILES, a single-center conflicting InChI
  and a third displayed key; its exact identity link needs upstream clarification.
  This does not establish a native stereochemical defect.
- The legacy PDB-CCD VAX routes returned 404. The inspected current 1GAC entry points
  to BIRD PRD_000203, but a formal VAX replacement mapping was not verified.
- The proprietary Reaxys entry was not independently accessed; CAS 118395-73-6 is
  corroborated by current official chemical records rather than a separate CAS structure
  record.
- The 1995 binding source was inspected through its complete original abstract and
  deposited experimental structural entry; its full main paper was not freely obtained.
  Detailed affinity, live-cell causality and organism-specific target claims are not
  inferred.
- Three adopted primary papers were inspected at complete-abstract depth; 11035791
  additionally at relevant full-body depth, and 25940955 is a review. Exact source
  depths are listed in the lead ledger.
- The original isolation paper characterizes hydrochloride-hydrate material and provides
  only abbreviated MIC reporting. Its numeric values were not transferred to the neutral
  native representation.
- Primary structure drawings and chemical correlations were inspected; every stereocenter
  was not independently reconstructed from raw spectra.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native record or maintained source input was changed. All fifteen input hashes
  were rechecked.
- All optional tags and references concern chloroeremomycin; biosynthetic enzymes
  and semisynthetic oritavancin are explicitly separated.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links: []
tags:
- record-review
- chloroeremomycin
- glycopeptide
- source-scope
```
