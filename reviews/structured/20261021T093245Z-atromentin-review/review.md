# Atromentin: supported neutral identity and producer scope; qualify a conflicting external formula

- Review: 20261021T093245Z-atromentin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:04:56Z
- Finished UTC: 2026-10-21T09:32:45Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Neutral atromentin chemistry and qualitative antibacterial classification are supported. MIBiG producer metadata and its deliberately limited citation provenance reproduce the adopted source. KNApSAcK contains a demonstrably incorrect formula and mass alongside matching structures. Primary enzyme and growth evidence must remain distinct; optional enrichment does not require inventing a bacterial cellular mechanism. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position119; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:149660 | data/antibiotics/antibacterial/atromentin.yaml | generated | atromentin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:149660 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:149660 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:149660 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:149660 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:149660 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:149660 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:149660 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:149660 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:149660 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:149660 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:149660 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:149660 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Internal validation and native status

schema: supported. Targets: CHEBI:149660.

Focused checks pass; native SEEDED status and source history are unchanged. Review coverage does not promote native status.

### Neutral exact structure

identity: supported. Targets: CHEBI:149660.

Independent structures and total synthesis support the graph; the anion and O-alkylated products remain distinct.

### KNApSAcK descriptor reliability

evidence: concern. Targets: CHEBI:149660.

The matching full structure does not reconcile its erroneous C16 formula and mass.

### Suillus producer and citation boundaries

evidence: supported. Targets: CHEBI:149660.

Source metadata reproduce, with legacy-reference and quality limits preserved. Primary abstract independently supports GreA biosynthesis; full experimental detail remains unavailable.

### Antibacterial role and optional FabK target

evidence: supported. Targets: CHEBI:149660.

Qualitative activity and purified enzyme inhibition have primary support at abstract scope; a bacterial MIC or in-cell FabK mechanism does not follow.

### Host and historical activity wording

evidence: unknown. Targets: CHEBI:149660.

Host apoptosis is supported at abstract level; historical anticoagulant and smooth-muscle experiments were not independently read. Their title-level traceability is explicitly bounded.

### Optional clinical, resistance, mechanism, graph and omics fields

completeness: unknown. Targets: CHEBI:149660.

No unsupported native assertions occur. Biosynthetic expression studies are not drug-treatment transcriptomes, and host-cell effects do not identify antibacterial targets.

## Findings

### F1: Qualify the conflicting KNApSAcK formula and mass

minor / open / confirmed; issue key: atromentin-knapsack-formula-mass-conflict.

KNApSAcK retains the matching exact molecular graph but displays a formula missing two carbons and the correspondingly wrong mass. Preserve correct native chemistry and qualify external descriptor reliability.

### F2: Curate exact primary activity with enzyme and cell endpoints separated

informational / open / confirmed; issue key: atromentin-primary-enzyme-versus-cellular-activity.

The FabK and bacterial-growth papers offer useful enrichment, but enzyme IC50 cannot populate MIC or prove a bacterial cellular target. Full primary assay detail should precede quantitative curation.

## Recommended Actions And Acceptance Checks

### A1

Record the external descriptor conflict through maintained source ownership.

- Recheck C00036784 against the complete InChI/SMILES and C18H12O6; do not replace native chemistry with the erroneous displayed C16 formula.
- If a source qualification or cross-reference policy change is made, preserve provenance and verify reproducibility through extraction/seeding.

### A2

Optionally inspect and curate the exact antibacterial and FabK primary experiments.

- Obtain and inspect the original full 2006 and 1984 methods/tables before adding strain-specific numeric growth observations.
- Keep atromentin distinct from leucomelone, derivatives, extracts and the monoanion. Record FabK inhibition with its measured organism and endpoint; do not infer direct binding or an in-cell causal chain from the abstract.
- Keep fungal biosynthesis and host endocrine/apoptosis effects separate from bacterial drug action; use the maintained record writer and claim-level evidence workflow.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/atromentin.yaml; Entire YAML, including six seed/reseed events | supports | Read the definition, five synonyms, both structural parents, antibacterial role, complete chemistry, three chemical cross-references, Wikipedia document, source mint, and Suillus grevillei producer object. The producer retains MIBiG questionable quality and a legacy-reference warning. No molecular target, mode, quantified activity, resistance, clinical, graph or dataset block is asserted. |
| source | data/raw/chebi_antimicrobials.tsv; data/raw/mibig_producers.tsv; ChEBI row 2723; MIBiG row 1013; extractor and seeder ownership | supports | The adopted rows reproduce native chemistry, roles and producer fields. ChEBI supplies ten PMID leads. The MIBiG extractor takes locus-level experimental methods, and the seeder labels scope COMPOUND_SPECIFIC because this entry contains one compound. It requires complete stereo and a unique exact full-key match. The attached PMID remains explicitly a legacy reference, not silently promoted to claim-level primary proof. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:149660; Current entry, OLS parents and PubChem CID 99148 | supports | Current ChEBI and PubChem agree on neutral C18H12O6, key FKQQKMGWCJGUCS-UHFFFAOYSA-N, one fragment, no stereocentres, average mass 324.288 and exact mass 324.06339. CHEBI:132126 dihydroxy-1,4-benzoquinones and CHEBI:26195 polyphenol are appropriate broader parents. CHEBI:33282 is the accepted antibacterial role. The conjugate base CHEBI:149642 is distinct. |
| knapsack | https://www.knapsackfamily.com/knapsack_core/information.php?word=C00036784; Current entry formula, mass, InChI, key and SMILES | partial | The entry names atromentin and has matching CAS 519-67-5, full InChI/key and SMILES. Its displayed formula is C16H12O6 and mass 300.06338812, inconsistent with the C18 molecular graph and independently calculated mass 324.063388104. This is an internal external-entry conflict; it does not establish a different native chemical entity. |
| synthesis | DOI:10.1271/bbb.100451; PMID:21071857; 119-primary2010.pdf, complete main article and Experimental text, pp 2342–2344 | supports | Total synthesis and single-crystal analysis establish atromentin connectivity. Synthetic material matches the authors natural Thelephora vialis sample. Earlier NMR discrepancies are discussed explicitly, and slow exchange broadens ring resonances; the solid-state analysis supports the depicted quinone. The report separately treats O-methylatromentin and thelephantin I. It is structural evidence, not an antibacterial assay. |
| mibig | https://mibig.secondarymetabolites.org/repository/BGC0002277.2/annotations.json; Complete current version-2 annotation and rendered entry; ENA taxonomy 5382 | supports | Active entry BGC0002277 version 2 retains questionable quality and unknown completeness. Its single compound is exact neutral atromentin; the locus JQ681152.1 carries heterologous-expression and enzymatic-assay methods. Compound evidence is empty; PMID:22730234 and its DOI are legacy references, while an ATP-PPi substrate assay is separately attributed. Suillus grevillei is species taxon 5382, corroborated by ENA. The native warning accurately represents source attribution, and no reviewed status or experimental strain is invented. |
| producer-primary | PMID:22730234; DOI:10.1002/cbic.201200187; complete Europe PMC abstract | partial | GreA cloned from the Suillus grevillei genome was characterized in vitro as atromentin synthetase. This provides independent primary abstract support for the biosynthetic link. Predicted specificity residues and modeled active-site positions remain computational evidence. The full Wiley paper returned 403; detailed assay, strain and heterologous-expression conditions were not read. |
| fabk | PMID:17323650; DOI:10.1038/ja.2006.108; full abstract and publisher metadata | partial | The authors isolated atromentin and leucomelone from unidentified fungus F010248. Reported atromentin IC50 against Streptococcus pneumoniae FabK is 0.24 µM; E. coli and S. aureus FabI were not inhibited at 200 µM. This is an enzyme endpoint, not a bacterial MIC or evidence that the fungus is S. pneumoniae. Full paper retrieval was unsuccessful; no exact bacterial growth result, inhibition mechanism or cellular causality was reconstructed from the abstract. |
| antibacterial | PMID:6541963; DOI:10.1139/m84-166; complete abstract | partial | The original comparative study includes atromentin among quinones tested for bacterial growth and metabolism inhibition. It supports a qualitative antibacterial role within the tested class/material context. The abstract does not provide an atromentin-specific strain/MIC table; numeric annotations require full-paper inspection. |
| adopted | Ten ChEBI PMID leads; 119-adopted.json; every complete abstract and DOI inspected | partial | PMIDs 12872944 and 12895540 report isolation and spectroscopic identification in Thelephora aurantiotincta. PMID 18805498 characterizes Tapinella AtrA/AtrD biosynthesis; 26496685 concerns Paxillus InvA synthetases and transcriptomic/isotope experiments; 30527997 concerns host-dependent products from Aspergillus synthetases. These are distinct organisms and biosynthetic contexts. PMID 19809251 reports U937 apoptosis/caspase-associated host-cell effects, not a bacterial target. PMID 28384525 lists atromentin among 17 isolates and describes an assay panel but no compound-specific abstract results. PMID 30174092 studies weak host estrogenic activity and proposed endocrine targets. PMID 21071857 is the fully read synthesis paper, and 17323650 the bounded FabK abstract. None is automatically native claim evidence. |
| historical | PMID:5815216; PMID:5862512; PMID:4332377; Europe PMC indexed metadata, no abstracts available | context_only | Primary titles concern smooth-muscle stimulation, anticoagulant activity in Hydnellum diabolus, and occurrence in Clitocybe cultures. They make the native source wording traceable but do not permit independent verification of those historical experiments. The retained antineoplastic wording has separate U937 primary abstract support and is not a claim of clinical approval. |
| adapter | Native iModulonDB adapter; 119-imodulondb-datasets.txt; executed before public research | context_only | The catalog contains no Suillus grevillei or other fungal dataset. It cannot adjudicate this fungal biosynthetic producer claim, so no unrelated bacterial gene hit was substituted. No native expression dataset is asserted. |
| other-xrefs | Official source crosswalks; Current ChEBI; MetaCyc response | partial | CAS 519-67-5 and Wikipedia Atromentin are corroborated through ChEBI, not independently audited registry/document content. MetaCyc CPD-14619 redirects to an account-required page. No proprietary access was purchased. |
| chemistry | Independent RDKit calculations; 119-chemistry.json; actual focused schema/strict logs | supports | Both native encodings reproduce the complete key, formula, charge, masses and deterministic source mint. Actual schema and strict checks exit 0. These checks establish internal consistency, not the scope of natural-product stereochemistry or biological activity. |
| search | CultureBotAI/AntibioticMech; Initial ignored-inclusive search and 012-root-maintained-search.txt | context_only | Exact identifiers and labels identify native/source and readiness-queue context. No target-specific override was found in the named maintained search scope. This does not establish absence of literature or of files excluded from that search. |

## Limits And Additional Notes

- All ten adopted abstracts and the GreA abstract were read; only the 2010 synthesis main paper was fully read. The FabK J-STAGE request returned 500; the Nature PDF route returned an HTML abstract page, not a PDF. The GreA Wiley page returned 403. No unavailable body is represented as read.
- The 2023 fungal synthetase article was inspected only through a bounded text search; it is not used as exact Suillus experimental proof. Raw NMR spectra and crystallographic data were not reanalyzed.
- No abstracts were available for the three historical occurrence/host-activity leads. Historical wording is source-supported but not independently revalidated experimentally. MetaCyc and proprietary registry limits are explicit.
- The current versioned MIBiG page and complete annotation were read after unversioned guessed routes returned 404. There is no assertion that the source entry is missing.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All captured input hashes were rechecked unchanged before writing the draft. No native record was edited.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T093245Z-atromentin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Atromentin: supported neutral identity and producer scope; qualify a conflicting
  external formula'
started_at: '2026-10-21T09:04:56Z'
finished_at: '2026-10-21T09:32:45Z'
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
summary: Neutral atromentin chemistry and qualitative antibacterial classification
  are supported. MIBiG producer metadata and its deliberately limited citation provenance
  reproduce the adopted source. KNApSAcK contains a demonstrably incorrect formula
  and mass alongside matching structures. Primary enzyme and growth evidence must
  remain distinct; optional enrichment does not require inventing a bacterial cellular
  mechanism. Scientific assessment retains the stated evidence limits; full verification
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
  - path: data/antibiotics/antibacterial/atromentin.yaml
    sha256: 3d761c22e4124e84ea5cf658543fac8371e9fafa3aa31051c867c9d11906d3a0
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
  - path: data/raw/mibig_producers.tsv
    sha256: d55289619e77e035ed437d432dd692ab382f254c3841c9a314752ef22578a01b
    role: context
  - path: scripts/extract_mibig_producers.py
    sha256: a078cdf4c9b2d09999800ab7ae03f93d3972f29b7d2f460ebbbe7d7ec6b31c53
    role: context
targets:
- target_id: CHEBI:149660
  path: data/antibiotics/antibacterial/atromentin.yaml
  label: atromentin
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
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/mibig_producers.tsv
    role: Adopted biosynthetic producer and evidence-scope ownership
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_mibig_producers.py
    role: Adopted biosynthetic producer and evidence-scope ownership
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position119; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:149660
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:149660
  command: .venv/bin/python /private/tmp/am-review-session/focus011-root.py 119
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:149660
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/atromentin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:149660
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/atromentin.yaml --out /private/tmp/am-review-session/119-strict.tsv
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
  - CHEBI:149660
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
  - CHEBI:149660
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
  - CHEBI:149660
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
  - CHEBI:149660
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
  - CHEBI:149660
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
  - CHEBI:149660
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
  - CHEBI:149660
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
  - CHEBI:149660
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
  - CHEBI:149660
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/atromentin.yaml
  locator: Entire YAML, including six seed/reseed events
  accessed_at: '2026-10-21T09:13:54Z'
  support: supports
  summary: Read the definition, five synonyms, both structural parents, antibacterial
    role, complete chemistry, three chemical cross-references, Wikipedia document,
    source mint, and Suillus grevillei producer object. The producer retains MIBiG
    questionable quality and a legacy-reference warning. No molecular target, mode,
    quantified activity, resistance, clinical, graph or dataset block is asserted.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/mibig_producers.tsv
  locator: ChEBI row 2723; MIBiG row 1013; extractor and seeder ownership
  accessed_at: '2026-10-21T09:13:54Z'
  support: supports
  summary: The adopted rows reproduce native chemistry, roles and producer fields.
    ChEBI supplies ten PMID leads. The MIBiG extractor takes locus-level experimental
    methods, and the seeder labels scope COMPOUND_SPECIFIC because this entry contains
    one compound. It requires complete stereo and a unique exact full-key match. The
    attached PMID remains explicitly a legacy reference, not silently promoted to
    claim-level primary proof.
  snapshot_sha256: f0b3ac8e30137da969a8d22f12ef8777333cd578461df4a6ea8835c581cf3d86
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:149660
  locator: Current entry, OLS parents and PubChem CID 99148
  accessed_at: '2026-10-21T09:13:54Z'
  support: supports
  summary: Current ChEBI and PubChem agree on neutral C18H12O6, key FKQQKMGWCJGUCS-UHFFFAOYSA-N,
    one fragment, no stereocentres, average mass 324.288 and exact mass 324.06339.
    CHEBI:132126 dihydroxy-1,4-benzoquinones and CHEBI:26195 polyphenol are appropriate
    broader parents. CHEBI:33282 is the accepted antibacterial role. The conjugate
    base CHEBI:149642 is distinct.
  snapshot_sha256: 7d8e9d13994d5d252dfa1504ce416ebe39f2b3973664cd796729ca2695a093ff
- evidence_id: knapsack
  kind: database
  reference: https://www.knapsackfamily.com/knapsack_core/information.php?word=C00036784
  locator: Current entry formula, mass, InChI, key and SMILES
  accessed_at: '2026-10-21T09:13:54Z'
  support: partial
  summary: The entry names atromentin and has matching CAS 519-67-5, full InChI/key
    and SMILES. Its displayed formula is C16H12O6 and mass 300.06338812, inconsistent
    with the C18 molecular graph and independently calculated mass 324.063388104.
    This is an internal external-entry conflict; it does not establish a different
    native chemical entity.
  snapshot_sha256: 4ad44d6e1a40c4a1d77ad46ec585c341f1edeb1065207043337be17fd7796892
- evidence_id: synthesis
  kind: primary_source
  reference: DOI:10.1271/bbb.100451
  locator: PMID:21071857; 119-primary2010.pdf, complete main article and Experimental
    text, pp 2342–2344
  accessed_at: '2026-10-21T09:13:54Z'
  support: supports
  summary: Total synthesis and single-crystal analysis establish atromentin connectivity.
    Synthetic material matches the authors natural Thelephora vialis sample. Earlier
    NMR discrepancies are discussed explicitly, and slow exchange broadens ring resonances;
    the solid-state analysis supports the depicted quinone. The report separately
    treats O-methylatromentin and thelephantin I. It is structural evidence, not an
    antibacterial assay.
  snapshot_sha256: 3639df45f5016474ada7cf812772b9cd5441eac1e6bac79669852d202329114e
- evidence_id: mibig
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0002277.2/annotations.json
  locator: Complete current version-2 annotation and rendered entry; ENA taxonomy
    5382
  accessed_at: '2026-10-21T09:13:54Z'
  support: supports
  summary: Active entry BGC0002277 version 2 retains questionable quality and unknown
    completeness. Its single compound is exact neutral atromentin; the locus JQ681152.1
    carries heterologous-expression and enzymatic-assay methods. Compound evidence
    is empty; PMID:22730234 and its DOI are legacy references, while an ATP-PPi substrate
    assay is separately attributed. Suillus grevillei is species taxon 5382, corroborated
    by ENA. The native warning accurately represents source attribution, and no reviewed
    status or experimental strain is invented.
- evidence_id: producer-primary
  kind: primary_source
  reference: PMID:22730234
  locator: DOI:10.1002/cbic.201200187; complete Europe PMC abstract
  accessed_at: '2026-10-21T09:13:54Z'
  support: partial
  summary: GreA cloned from the Suillus grevillei genome was characterized in vitro
    as atromentin synthetase. This provides independent primary abstract support for
    the biosynthetic link. Predicted specificity residues and modeled active-site
    positions remain computational evidence. The full Wiley paper returned 403; detailed
    assay, strain and heterologous-expression conditions were not read.
  snapshot_sha256: 7dad73a236e7df1c4bdf456ee694c0936d841e2a36f7a906db1ab9d25fa45e21
- evidence_id: fabk
  kind: primary_source
  reference: PMID:17323650
  locator: DOI:10.1038/ja.2006.108; full abstract and publisher metadata
  accessed_at: '2026-10-21T09:13:54Z'
  support: partial
  summary: The authors isolated atromentin and leucomelone from unidentified fungus
    F010248. Reported atromentin IC50 against Streptococcus pneumoniae FabK is 0.24
    µM; E. coli and S. aureus FabI were not inhibited at 200 µM. This is an enzyme
    endpoint, not a bacterial MIC or evidence that the fungus is S. pneumoniae. Full
    paper retrieval was unsuccessful; no exact bacterial growth result, inhibition
    mechanism or cellular causality was reconstructed from the abstract.
  snapshot_sha256: 7dad73a236e7df1c4bdf456ee694c0936d841e2a36f7a906db1ab9d25fa45e21
- evidence_id: antibacterial
  kind: primary_source
  reference: PMID:6541963
  locator: DOI:10.1139/m84-166; complete abstract
  accessed_at: '2026-10-21T09:13:54Z'
  support: partial
  summary: The original comparative study includes atromentin among quinones tested
    for bacterial growth and metabolism inhibition. It supports a qualitative antibacterial
    role within the tested class/material context. The abstract does not provide an
    atromentin-specific strain/MIC table; numeric annotations require full-paper inspection.
  snapshot_sha256: c2cdf43f5244856d5d382ae777f48654f97b80ce935b25ca57e86b19db89b9e2
- evidence_id: adopted
  kind: primary_source
  reference: Ten ChEBI PMID leads
  locator: 119-adopted.json; every complete abstract and DOI inspected
  accessed_at: '2026-10-21T09:13:54Z'
  support: partial
  summary: PMIDs 12872944 and 12895540 report isolation and spectroscopic identification
    in Thelephora aurantiotincta. PMID 18805498 characterizes Tapinella AtrA/AtrD
    biosynthesis; 26496685 concerns Paxillus InvA synthetases and transcriptomic/isotope
    experiments; 30527997 concerns host-dependent products from Aspergillus synthetases.
    These are distinct organisms and biosynthetic contexts. PMID 19809251 reports
    U937 apoptosis/caspase-associated host-cell effects, not a bacterial target. PMID
    28384525 lists atromentin among 17 isolates and describes an assay panel but no
    compound-specific abstract results. PMID 30174092 studies weak host estrogenic
    activity and proposed endocrine targets. PMID 21071857 is the fully read synthesis
    paper, and 17323650 the bounded FabK abstract. None is automatically native claim
    evidence.
  snapshot_sha256: 7dad73a236e7df1c4bdf456ee694c0936d841e2a36f7a906db1ab9d25fa45e21
- evidence_id: historical
  kind: database
  reference: PMID:5815216; PMID:5862512; PMID:4332377
  locator: Europe PMC indexed metadata, no abstracts available
  accessed_at: '2026-10-21T09:13:54Z'
  support: context_only
  summary: Primary titles concern smooth-muscle stimulation, anticoagulant activity
    in Hydnellum diabolus, and occurrence in Clitocybe cultures. They make the native
    source wording traceable but do not permit independent verification of those historical
    experiments. The retained antineoplastic wording has separate U937 primary abstract
    support and is not a claim of clinical approval.
  snapshot_sha256: c2cdf43f5244856d5d382ae777f48654f97b80ce935b25ca57e86b19db89b9e2
- evidence_id: adapter
  kind: database
  reference: Native iModulonDB adapter
  locator: 119-imodulondb-datasets.txt; executed before public research
  accessed_at: '2026-10-21T09:13:54Z'
  support: context_only
  summary: The catalog contains no Suillus grevillei or other fungal dataset. It cannot
    adjudicate this fungal biosynthetic producer claim, so no unrelated bacterial
    gene hit was substituted. No native expression dataset is asserted.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: other-xrefs
  kind: database
  reference: Official source crosswalks
  locator: Current ChEBI; MetaCyc response
  accessed_at: '2026-10-21T09:13:54Z'
  support: partial
  summary: CAS 519-67-5 and Wikipedia Atromentin are corroborated through ChEBI, not
    independently audited registry/document content. MetaCyc CPD-14619 redirects to
    an account-required page. No proprietary access was purchased.
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit calculations
  locator: 119-chemistry.json; actual focused schema/strict logs
  accessed_at: '2026-10-21T09:13:54Z'
  support: supports
  summary: Both native encodings reproduce the complete key, formula, charge, masses
    and deterministic source mint. Actual schema and strict checks exit 0. These checks
    establish internal consistency, not the scope of natural-product stereochemistry
    or biological activity.
  snapshot_sha256: d1e1b28652caba376f25cc806dba764f972c1991c19c4d695bc2be7a15736020
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: Initial ignored-inclusive search and 012-root-maintained-search.txt
  accessed_at: '2026-10-21T09:13:54Z'
  support: context_only
  summary: Exact identifiers and labels identify native/source and readiness-queue
    context. No target-specific override was found in the named maintained search
    scope. This does not establish absence of literature or of files excluded from
    that search.
  search_scope: rg --no-ignore --hidden across curation, conf, scripts, src and data/raw;
    exact names, ChEBI IDs and full-key stems; excluded .git, .venv and .obo/.jsonl/.html
    files in the bounded maintained pass. Initial prepare search also included ignored
    files. Free official database, Europe PMC and primary publisher searches.
  snapshot_sha256: 80838d5ef4c016780141b1f7ed126dd26d66a75824e8c6e38a1070f856bd652b
assessments:
- assessment_id: schema
  area: schema
  topic: Internal validation and native status
  outcome: supported
  summary: Focused checks pass; native SEEDED status and source history are unchanged.
    Review coverage does not promote native status.
  target_ids:
  - CHEBI:149660
  evidence_ids:
  - chemistry
  - native
- assessment_id: identity
  area: identity
  topic: Neutral exact structure
  outcome: supported
  summary: Independent structures and total synthesis support the graph; the anion
    and O-alkylated products remain distinct.
  target_ids:
  - CHEBI:149660
  evidence_ids:
  - identity
  - chemistry
  - synthesis
- assessment_id: xref
  area: evidence
  topic: KNApSAcK descriptor reliability
  outcome: concern
  summary: The matching full structure does not reconcile its erroneous C16 formula
    and mass.
  target_ids:
  - CHEBI:149660
  evidence_ids:
  - knapsack
  - identity
  - chemistry
- assessment_id: producer
  area: evidence
  topic: Suillus producer and citation boundaries
  outcome: supported
  summary: Source metadata reproduce, with legacy-reference and quality limits preserved.
    Primary abstract independently supports GreA biosynthesis; full experimental detail
    remains unavailable.
  target_ids:
  - CHEBI:149660
  evidence_ids:
  - source
  - mibig
  - producer-primary
  - adapter
- assessment_id: activity
  area: evidence
  topic: Antibacterial role and optional FabK target
  outcome: supported
  summary: Qualitative activity and purified enzyme inhibition have primary support
    at abstract scope; a bacterial MIC or in-cell FabK mechanism does not follow.
  target_ids:
  - CHEBI:149660
  evidence_ids:
  - antibacterial
  - fabk
- assessment_id: definition
  area: evidence
  topic: Host and historical activity wording
  outcome: unknown
  summary: Host apoptosis is supported at abstract level; historical anticoagulant
    and smooth-muscle experiments were not independently read. Their title-level traceability
    is explicitly bounded.
  target_ids:
  - CHEBI:149660
  evidence_ids:
  - adopted
  - historical
- assessment_id: other
  area: completeness
  topic: Optional clinical, resistance, mechanism, graph and omics fields
  outcome: unknown
  summary: No unsupported native assertions occur. Biosynthetic expression studies
    are not drug-treatment transcriptomes, and host-cell effects do not identify antibacterial
    targets.
  target_ids:
  - CHEBI:149660
  evidence_ids:
  - native
  - adopted
  - fabk
findings:
- finding_id: F1
  issue_key: atromentin-knapsack-formula-mass-conflict
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify the conflicting KNApSAcK formula and mass
  description: KNApSAcK retains the matching exact molecular graph but displays a
    formula missing two carbons and the correspondingly wrong mass. Preserve correct
    native chemistry and qualify external descriptor reliability.
  target_ids:
  - CHEBI:149660
  field_paths:
  - xrefs
  evidence_ids:
  - knapsack
  - identity
  - chemistry
  rule_id: 'native-review-checklist: Identity, Equivalence, Evidence and Completeness'
  native_severity: minor
  normalization_reason: KNApSAcK retains the matching exact molecular graph but displays
    a formula missing two carbons and the correspondingly wrong mass. Preserve correct
    native chemistry and qualify external descriptor reliability.
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
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/mibig_producers.tsv
    role: Adopted biosynthetic producer and evidence-scope ownership
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_mibig_producers.py
    role: Adopted biosynthetic producer and evidence-scope ownership
- finding_id: F2
  issue_key: atromentin-primary-enzyme-versus-cellular-activity
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Curate exact primary activity with enzyme and cell endpoints separated
  description: The FabK and bacterial-growth papers offer useful enrichment, but enzyme
    IC50 cannot populate MIC or prove a bacterial cellular target. Full primary assay
    detail should precede quantitative curation.
  target_ids:
  - CHEBI:149660
  field_paths:
  - molecular_targets
  - activity_spectrum
  - evidence
  - discussions
  evidence_ids:
  - fabk
  - antibacterial
  - adopted
  rule_id: 'native-review-checklist: Identity, Equivalence, Evidence and Completeness'
  native_severity: informational
  normalization_reason: The FabK and bacterial-growth papers offer useful enrichment,
    but enzyme IC50 cannot populate MIC or prove a bacterial cellular target. Full
    primary assay detail should precede quantitative curation.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/atromentin.yaml
    role: Curator-owned primary evidence, targets and activity
actions:
- action_id: A1
  description: Record the external descriptor conflict through maintained source ownership.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:149660
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
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/mibig_producers.tsv
    role: Adopted biosynthetic producer and evidence-scope ownership
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_mibig_producers.py
    role: Adopted biosynthetic producer and evidence-scope ownership
  acceptance_checks:
  - Recheck C00036784 against the complete InChI/SMILES and C18H12O6; do not replace
    native chemistry with the erroneous displayed C16 formula.
  - If a source qualification or cross-reference policy change is made, preserve provenance
    and verify reproducibility through extraction/seeding.
- action_id: A2
  description: Optionally inspect and curate the exact antibacterial and FabK primary
    experiments.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:149660
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/atromentin.yaml
    role: Curator-owned primary evidence, targets and activity
  acceptance_checks:
  - Obtain and inspect the original full 2006 and 1984 methods/tables before adding
    strain-specific numeric growth observations.
  - Keep atromentin distinct from leucomelone, derivatives, extracts and the monoanion.
    Record FabK inhibition with its measured organism and endpoint; do not infer direct
    binding or an in-cell causal chain from the abstract.
  - Keep fungal biosynthesis and host endocrine/apoptosis effects separate from bacterial
    drug action; use the maintained record writer and claim-level evidence workflow.
limitations:
- All ten adopted abstracts and the GreA abstract were read; only the 2010 synthesis
  main paper was fully read. The FabK J-STAGE request returned 500; the Nature PDF
  route returned an HTML abstract page, not a PDF. The GreA Wiley page returned 403.
  No unavailable body is represented as read.
- The 2023 fungal synthetase article was inspected only through a bounded text search;
  it is not used as exact Suillus experimental proof. Raw NMR spectra and crystallographic
  data were not reanalyzed.
- No abstracts were available for the three historical occurrence/host-activity leads.
  Historical wording is source-supported but not independently revalidated experimentally.
  MetaCyc and proprietary registry limits are explicit.
- The current versioned MIBiG page and complete annotation were read after unversioned
  guessed routes returned 404. There is no assertion that the source entry is missing.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All captured input hashes were rechecked unchanged before writing the draft. No
  native record was edited.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
