# Review of callophycol B

- Review: 20261021T104143Z-callophycol-b-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:21:10Z
- Finished UTC: 2026-10-21T10:41:43Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Native callophycol B correctly represents the16-chloro/17-bromo regioisomer with C16 unassigned. A 2024 primary paper assigns16R in text but labels its B Figure 1 structure16S. Preserve that unresolved conflict and the assumed absolute core hand before any structure update. Original B antimalarial activity is supported; bacterial and cancer endpoints are censored bounds, not universal negatives.

## Scope And Provenance

Entire SEEDED record and three history events; ChEBI/source identity and sole adopted PMID; original compound 10 structure, Table 3 and assays; 2024 callophycol B C16 text versus visually inspected Figure 1; bounded2009/2012 context.

Selection: Queue index188; original13 input hashes preserved; one exact target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65566 | data/antibiotics/antibacterial/callophycol-b.yaml | generated | callophycol B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema check | passed | True | CHEBI:65566 | Exit0. |
| Documented strict check | passed | True | CHEBI:65566 | Exit0; zero ERROR rows. |
| Supplemental exact graph and source checks | passed | False | CHEBI:65566 | Exit0; exact database graph agreement and unique unassigned C16 mapped. Hypothetical S/R graphs are scratch-only, not adopted corrections. |
| Structured-source applicability | not_applicable | False | CHEBI:65566 | No named microbial gene, protein, regulator, pathway or transcriptomics claim occurs in this record. Isolation, phenotypic activity and chemical stereochemistry do not trigger a gene-module query. |
| Authoritative full QC | failed | True | CHEBI:65566 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65566 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65566 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65566 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65566 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65566 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65566 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65566 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65566 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### B regioisomer and conflicted C16 source

identity: concern. Targets: CHEBI:65566.

Native regioisomer is coherent; later text16R and Figure 1S conflict. An explicit unresolved identity discussion is needed before any update.

### Chemical parents and antimalarial role

grounding: supported. Targets: CHEBI:65566.

Three parent types fit and exact B40.4micromolar antimalarial endpoint supports that role.

### Antibacterial filing and anticancer wording

evidence: unknown. Targets: CHEBI:65566.

Database classification is reproduced, but original endpoints are above limits; no universal negative or automatic role removal is inferred.

### Optional molecular target

completeness: unknown. Targets: CHEBI:65566.

Inspected original activity and later stereochemistry do not establish a molecular target; proposed biosynthetic cascades are not mechanism-of-action evidence.

### Algal isolation and taxonomy

evidence: unknown. Targets: CHEBI:65566.

Original isolation is supported; later source-species nomenclature remains unresolved at voucher level.

### Adopted source and history

provenance: supported. Targets: CHEBI:65566.

Sole adopted PMID and three history events checked; later evidence kept distinct from imported database content.

### Focused gates

schema: supported. Targets: CHEBI:65566.

Schema, strict and supplementary chemistry checks pass.

## Findings

### F1: Adjudicate conflicting text and figure before assigning C16

major / open / confirmed; issue key: chebi-65566-conflicting-c16-assignment.

Native C16 is undefined as in 2007, while the2024 exact-compound analysis repeatedly assigns16R to B but labels its Figure 1 B structure16S. The record has no discussion of this later conflict or the assumed absolute core hand. Current ChEBI/PubChem agreement does not resolve it. Preserve explicit unresolved identity evidence rather than selecting R or S from one part of the source.

## Recommended Actions And Acceptance Checks

### A1

Preserve and resolve the callophycol B C16 source conflict before changing the graph.

- Inspect2024 supporting calculations, full-resolution drawings and any published correction to reconcile repeated16R text with Figure 1(S) label for compound 4. Also check the paired-analysis A numeric discrepancy and conserved-core assumption.
- Record a primary-linked unresolved identity discussion and keep SEEDED until adjudicated. Do not assign R or S solely from the abstract or diagram; scratch candidate keys are alternatives, not recommendations.
- If a configuration is defensibly resolved, update maintained source/transform, synonym, SMILES/InChI/key and exact xrefs consistently, then regenerate through validated curation. Preserve B16Cl/17Br versus A16Br/17Cl.
- Keep B40.4micromolar antimalarial activity separate from A, and retain bacterial/cancer/TB censored bounds and method/taxon limits. Mixed fractions and bromophycolide imaging do not prove B activity or a direct target.
- Run focused schema/strict, source provenance, reference/history and required full-corpus gates after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/callophycol-b.yaml; Entire YAML and three history events | supports | SEEDED/EXACT record has five configured decalin centers and one undefined side-chain C16, with dibromophenol/organochlorine/carbobicyclic parents, antibacterial and antimalarial roles. No native mechanism, target, MIC, resistance or curated producer object is asserted. |
| chemistry | CHEBI:65566;ChemSpider:27023088;PubChem:23584430; 188-chemistry.py;188-chemistry.json;188-ols.json;188-chebi.html;188-chemspider.html;188-pubchem-key.json | supports | Native neutral C26H35Br4ClO SMILES/InChI/key, masses and current external graph representations agree. B places Cl on C16 and Br on tertiary C17. Five core centers are fixed; C16 alone is undefined. Scratch alternatives holding core fixed yield R key NFMVWIXBGOEENC-SQCBNSKFSA-N or S key NFMVWIXBGOEENC-IZHJCOPISA-N; neither is adopted. |
| original | PMID:17715978; DOI:10.1021/jo071210y;179-PMC3374858.html;compound10 discussion,Table2 and original combined structure panel179-xray.jpg | supports | Original callophycol B is compound 10. C16 methine/C17 tertiary-carbon shifts support chlorine at 16 and bromine at 17, distinguishing A. Remote16 stereochemistry was explicitly unassigned. Relative decalin geometry is shared with 7–9; original direct crystal was callophycoic acid A, not B. |
| activity | PMID:17715978; Original Table3 row10 and Pharmacological Assays | partial | B antimalarial IC50 is 40.4 micromolar against P. falciparum3D7 in the 72 h SYBR Green assay. Both bacterial MICs are&gt;350 micromolar, antitubercular MIC&gt;10, and mean11-cancer-line IC50&gt;25; antifungal was not tested. Censored limits are not positive potency or universal inactivity. A35.7micromolar and G/H bacterial values are distinct. |
| assignment | PMID:38935812; DOI:10.1021/acs.joc.4c00905;185-2024.html;abstract,Results,Conclusion;187-2024-fig1.jpg | partial | The 2024 optical-superposition analysis identifies callophycol B as compound 4 and repeatedly assigns16R in text. Visually inspected Figure 1 instead labels its4 stereocenter(S), with16-epi-4 labelled(R). This is an unresolved internal conflict in the exact-compound source. The method is empirical literature-rotation analysis, with conserved core-handedness assumed, not a new crystal experiment. |
| source-caveat | PMID:38935812; 187-2024-table1.jpg;185-2024.html;original2007 compound9 optical rotation | context_only | The same2024 analysis prints A molar rotation+139.5 although its original rotation/mass yield~539 and Table 1 averages agree with539. B original+110 yields~790.5, consistent with its reported~791. The A numerical discrepancy affects the paired analysis and remains a limitation; the B text-R/figure-S conflict is independently visible. Supporting calculations were unavailable. |
| ecology | PMID:19366672; DOI:10.1073/pnas.0812020106;183-PMC2678663.html;Results,Figure1caption and Methods | context_only | Only callophycoic acids C, G, H were effective below 300micromolar in the pure-compound Lindra panel. Inhibitory mixed fractions do not demonstrate callophycol B activity; bromophycolide surface imaging is unrelated to a direct B mechanism. Morphological C. serratus identity and two18S/chemical clades remain source context. |
| taxonomy | PMID:17715978;PMID:22920243; Original Biological Material and compound10 characterization;185-2012.html taxonomic context | partial | Original B was isolated as2.2mg from morphology-identified C. serratus with deposited voucher. Later 2012 assigns the metabolite group to C. densus, while2009 retained both chemotypes as C. serratus. Exact original-voucher reidentification remains unresolved; no definitive producer replacement is inferred. |
| owners | data/raw/chebi_antimicrobials.tsv;scripts/extract_source_inventory.py;scripts/seed_from_sources.py; CHEBI65566 adopted row | supports | The adopted row reproduces identity/roles and cites17715978 only. Ignored-inclusive curation/conf/inventory searches found source/queue rows and no later exact-record stereochemical adjudication. |
| validation | Focused native gates; 188-strict.tsv | supports | Schema and strict checks pass. Supplementary chemistry assertions distinguish current database identity from the newer empirical assignment. |

## Limits And Additional Notes

- Original main text, compound 10 structure panel, Table 2, Table 3 and methods were inspected; raw spectra were not reanalyzed. Original C16 was left unassigned and complete absolute core handedness was not directly established.
- The 2024 main text, Figure 1 and Table 1 were inspected. Text repeatedly calls B16R, while its Figure 1 structure4 is labelled(S). This conflict remains unresolved; no automatic update is proposed.
- Supporting-PDF retrieval via PMC returned challenge HTML despite HTTP200; ACS returned HTTP 403. The paired-analysis A main-text molar-rotation139.5 conflicts with original-derived~539 and Table 1. B derived~790.5 agrees with reported~791.
- The empirical method assumes conserved core hand and misattributes original C crystallography where the2007 crystal wasA. These caveats are distinct from proof that the native core is wrong.
- Current public ChEBI, ChemSpider and PubChem all retain the undefined-C16 graph. Reaxys was not accessed. Hypothetical R/S candidate keys require evidence-based adjudication and full xref review before any use.
- B antibacterial&gt;350, cancermean&gt;25 and TB&gt;10micromolar are bounded results; positive malaria40.4 is separate. Quantitative adoption would require resolving original bacterial strain identifiers/protocol.
- Original C. serratus isolation naming conflicts with later C. densus group attribution; exact-voucher reidentification remains unresolved. No producer correction is asserted.
- No exact molecular target was established from inspected activity/stereochemistry studies. Native content does not trigger a protein-expression adapter; this bounded review does not claim exhaustive literature coverage or full-corpus success.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 13 repository input hashes remain unchanged; no native or saved-bundle edits.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T104143Z-callophycol-b-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of callophycol B
started_at: '2026-10-21T10:21:10Z'
finished_at: '2026-10-21T10:41:43Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Current graph reproducible; later C16 assignment is internally conflicting
  and needs explicit unresolved adjudication
scientific_review: true
summary: Native callophycol B correctly represents the16-chloro/17-bromo regioisomer
  with C16 unassigned. A 2024 primary paper assigns16R in text but labels its B Figure
  1 structure16S. Preserve that unresolved conflict and the assumed absolute core
  hand before any structure update. Original B antimalarial activity is supported;
  bacterial and cancer endpoints are censored bounds, not universal negatives.
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
  - path: data/antibiotics/antibacterial/callophycol-b.yaml
    sha256: f690820b77fedf3f281f8c8b307d59a8f61ff8826afd80ff9b16e171533c24a1
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
scope:
  description: Entire SEEDED record and three history events; ChEBI/source identity
    and sole adopted PMID; original compound 10 structure, Table 3 and assays; 2024
    callophycol B C16 text versus visually inspected Figure 1; bounded2009/2012 context.
  selection: Queue index188; original13 input hashes preserved; one exact target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65566
targets:
- target_id: CHEBI:65566
  path: data/antibiotics/antibacterial/callophycol-b.yaml
  label: callophycol B
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
checks:
- check_id: schema
  name: Documented schema check
  status: passed
  required: true
  summary: Exit0.
  target_ids:
  - CHEBI:65566
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/callophycol-b.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict check
  status: passed
  required: true
  summary: Exit0; zero ERROR rows.
  target_ids:
  - CHEBI:65566
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/callophycol-b.yaml --out /private/tmp/am-review-session/188-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Supplemental exact graph and source checks
  status: passed
  required: false
  summary: Exit0; exact database graph agreement and unique unassigned C16 mapped.
    Hypothetical S/R graphs are scratch-only, not adopted corrections.
  target_ids:
  - CHEBI:65566
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/188-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: structured-adapter
  name: Structured-source applicability
  status: not_applicable
  required: false
  summary: No named microbial gene, protein, regulator, pathway or transcriptomics
    claim occurs in this record. Isolation, phenotypic activity and chemical stereochemistry
    do not trigger a gene-module query.
  target_ids:
  - CHEBI:65566
  evidence_ids:
  - record
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:65566
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
  - CHEBI:65566
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
  - CHEBI:65566
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
  - CHEBI:65566
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
  - CHEBI:65566
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
  - CHEBI:65566
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
  - CHEBI:65566
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
  - CHEBI:65566
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
  - CHEBI:65566
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/callophycol-b.yaml
  locator: Entire YAML and three history events
  accessed_at: '2026-10-21T10:33:57Z'
  support: supports
  summary: SEEDED/EXACT record has five configured decalin centers and one undefined
    side-chain C16, with dibromophenol/organochlorine/carbobicyclic parents, antibacterial
    and antimalarial roles. No native mechanism, target, MIC, resistance or curated
    producer object is asserted.
- evidence_id: chemistry
  kind: validation
  reference: CHEBI:65566;ChemSpider:27023088;PubChem:23584430
  locator: 188-chemistry.py;188-chemistry.json;188-ols.json;188-chebi.html;188-chemspider.html;188-pubchem-key.json
  accessed_at: '2026-10-21T10:33:57Z'
  support: supports
  summary: Native neutral C26H35Br4ClO SMILES/InChI/key, masses and current external
    graph representations agree. B places Cl on C16 and Br on tertiary C17. Five core
    centers are fixed; C16 alone is undefined. Scratch alternatives holding core fixed
    yield R key NFMVWIXBGOEENC-SQCBNSKFSA-N or S key NFMVWIXBGOEENC-IZHJCOPISA-N;
    neither is adopted.
  snapshot_sha256: f8a577cf50893a0ab02874572055bc077a44d6bf2c6d47a27b9c1ef726ca645b
- evidence_id: original
  kind: primary_source
  reference: PMID:17715978
  locator: DOI:10.1021/jo071210y;179-PMC3374858.html;compound10 discussion,Table2
    and original combined structure panel179-xray.jpg
  accessed_at: '2026-10-21T10:33:57Z'
  support: supports
  summary: Original callophycol B is compound 10. C16 methine/C17 tertiary-carbon
    shifts support chlorine at 16 and bromine at 17, distinguishing A. Remote16 stereochemistry
    was explicitly unassigned. Relative decalin geometry is shared with 7–9; original
    direct crystal was callophycoic acid A, not B.
  snapshot_sha256: bcf3f54e5acf5cb0bb6c5d42bf9e5b9d99fee62da8b6fe2768f0859545f956fd
- evidence_id: activity
  kind: primary_source
  reference: PMID:17715978
  locator: Original Table3 row10 and Pharmacological Assays
  accessed_at: '2026-10-21T10:33:57Z'
  support: partial
  summary: B antimalarial IC50 is 40.4 micromolar against P. falciparum3D7 in the
    72 h SYBR Green assay. Both bacterial MICs are>350 micromolar, antitubercular
    MIC>10, and mean11-cancer-line IC50>25; antifungal was not tested. Censored limits
    are not positive potency or universal inactivity. A35.7micromolar and G/H bacterial
    values are distinct.
  snapshot_sha256: bcf3f54e5acf5cb0bb6c5d42bf9e5b9d99fee62da8b6fe2768f0859545f956fd
- evidence_id: assignment
  kind: primary_source
  reference: PMID:38935812
  locator: DOI:10.1021/acs.joc.4c00905;185-2024.html;abstract,Results,Conclusion;187-2024-fig1.jpg
  accessed_at: '2026-10-21T10:33:57Z'
  support: partial
  summary: The 2024 optical-superposition analysis identifies callophycol B as compound
    4 and repeatedly assigns16R in text. Visually inspected Figure 1 instead labels
    its4 stereocenter(S), with16-epi-4 labelled(R). This is an unresolved internal
    conflict in the exact-compound source. The method is empirical literature-rotation
    analysis, with conserved core-handedness assumed, not a new crystal experiment.
  snapshot_sha256: b85de8864853832ec9372775f0a41f801a7c7303781b0398ecd5c47ebaa4dbed
- evidence_id: source-caveat
  kind: primary_source
  reference: PMID:38935812
  locator: 187-2024-table1.jpg;185-2024.html;original2007 compound9 optical rotation
  accessed_at: '2026-10-21T10:33:57Z'
  support: context_only
  summary: The same2024 analysis prints A molar rotation+139.5 although its original
    rotation/mass yield~539 and Table 1 averages agree with539. B original+110 yields~790.5,
    consistent with its reported~791. The A numerical discrepancy affects the paired
    analysis and remains a limitation; the B text-R/figure-S conflict is independently
    visible. Supporting calculations were unavailable.
  snapshot_sha256: f1353d3190f5767779b45b38494b634feb6d4def31f638f43c892443ffe2dc4e
- evidence_id: ecology
  kind: primary_source
  reference: PMID:19366672
  locator: DOI:10.1073/pnas.0812020106;183-PMC2678663.html;Results,Figure1caption
    and Methods
  accessed_at: '2026-10-21T10:33:57Z'
  support: context_only
  summary: Only callophycoic acids C, G, H were effective below 300micromolar in the
    pure-compound Lindra panel. Inhibitory mixed fractions do not demonstrate callophycol
    B activity; bromophycolide surface imaging is unrelated to a direct B mechanism.
    Morphological C. serratus identity and two18S/chemical clades remain source context.
  snapshot_sha256: a5ebe2957910dffee14703083186dee433a28ce6eb60a4e845ff9a692c0a00d3
- evidence_id: taxonomy
  kind: primary_source
  reference: PMID:17715978;PMID:22920243
  locator: Original Biological Material and compound10 characterization;185-2012.html
    taxonomic context
  accessed_at: '2026-10-21T10:33:57Z'
  support: partial
  summary: Original B was isolated as2.2mg from morphology-identified C. serratus
    with deposited voucher. Later 2012 assigns the metabolite group to C. densus,
    while2009 retained both chemotypes as C. serratus. Exact original-voucher reidentification
    remains unresolved; no definitive producer replacement is inferred.
  snapshot_sha256: c8ea74b2bbc981d5c1416b43200921cecbcd1f63f471b5dfe3beae1901cae82b
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv;scripts/extract_source_inventory.py;scripts/seed_from_sources.py
  locator: CHEBI65566 adopted row
  accessed_at: '2026-10-21T10:33:57Z'
  support: supports
  summary: The adopted row reproduces identity/roles and cites17715978 only. Ignored-inclusive
    curation/conf/inventory searches found source/queue rows and no later exact-record
    stereochemical adjudication.
  search_scope: rg --no-ignore --hidden exact65566,label andslug over curation,conf,data/raw/chebi_antimicrobials.tsv.
- evidence_id: validation
  kind: validation
  reference: Focused native gates
  locator: 188-strict.tsv
  accessed_at: '2026-10-21T10:33:57Z'
  support: supports
  summary: Schema and strict checks pass. Supplementary chemistry assertions distinguish
    current database identity from the newer empirical assignment.
assessments:
- assessment_id: identity
  area: identity
  topic: B regioisomer and conflicted C16 source
  outcome: concern
  summary: Native regioisomer is coherent; later text16R and Figure 1S conflict. An
    explicit unresolved identity discussion is needed before any update.
  target_ids:
  - CHEBI:65566
  evidence_ids:
  - chemistry
  - original
  - assignment
  - source-caveat
- assessment_id: grounding
  area: grounding
  topic: Chemical parents and antimalarial role
  outcome: supported
  summary: Three parent types fit and exact B40.4micromolar antimalarial endpoint
    supports that role.
  target_ids:
  - CHEBI:65566
  evidence_ids:
  - chemistry
  - activity
- assessment_id: bacterial-cancer
  area: evidence
  topic: Antibacterial filing and anticancer wording
  outcome: unknown
  summary: Database classification is reproduced, but original endpoints are above
    limits; no universal negative or automatic role removal is inferred.
  target_ids:
  - CHEBI:65566
  evidence_ids:
  - activity
  - owners
- assessment_id: mechanism
  area: completeness
  topic: Optional molecular target
  outcome: unknown
  summary: Inspected original activity and later stereochemistry do not establish
    a molecular target; proposed biosynthetic cascades are not mechanism-of-action
    evidence.
  target_ids:
  - CHEBI:65566
  evidence_ids:
  - original
  - assignment
- assessment_id: producer
  area: evidence
  topic: Algal isolation and taxonomy
  outcome: unknown
  summary: Original isolation is supported; later source-species nomenclature remains
    unresolved at voucher level.
  target_ids:
  - CHEBI:65566
  evidence_ids:
  - taxonomy
  - ecology
- assessment_id: provenance
  area: provenance
  topic: Adopted source and history
  outcome: supported
  summary: Sole adopted PMID and three history events checked; later evidence kept
    distinct from imported database content.
  target_ids:
  - CHEBI:65566
  evidence_ids:
  - record
  - owners
- assessment_id: schema
  area: schema
  topic: Focused gates
  outcome: supported
  summary: Schema, strict and supplementary chemistry checks pass.
  target_ids:
  - CHEBI:65566
  evidence_ids:
  - validation
  - chemistry
findings:
- finding_id: F1
  issue_key: chebi-65566-conflicting-c16-assignment
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Adjudicate conflicting text and figure before assigning C16
  description: Native C16 is undefined as in 2007, while the2024 exact-compound analysis
    repeatedly assigns16R to B but labels its Figure 1 B structure16S. The record
    has no discussion of this later conflict or the assumed absolute core hand. Current
    ChEBI/PubChem agreement does not resolve it. Preserve explicit unresolved identity
    evidence rather than selecting R or S from one part of the source.
  target_ids:
  - CHEBI:65566
  field_paths:
  - chemical_structure
  - synonyms
  - grounding_status
  - discussions
  evidence_ids:
  - record
  - chemistry
  - original
  - assignment
  - source-caveat
  - owners
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Source-owned exact structure and synonym
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reproducible source reconciliation if adopted identity changes
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding/exclusion adjudication if source uncertainty cannot be represented
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Regeneration preserving curated uncertainty discussion
  rule_id: 'review-checklist: exact stereo identity; preserve conflicts; native REVIEWED
    identity gate'
  native_severity: major unresolved exact-identity representation
  normalization_reason: The native undefined center is not falsely assigned; the major
    concern is an unresolved exact-identity conflict absent from its scientific qualification.
    No wrong-enantiomer blocker or automatic R/S replacement is claimed.
actions:
- action_id: A1
  description: Preserve and resolve the callophycol B C16 source conflict before changing
    the graph.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:65566
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Source-owned exact structure and synonym
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reproducible source reconciliation if adopted identity changes
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding/exclusion adjudication if source uncertainty cannot be represented
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Regeneration preserving curated uncertainty discussion
  acceptance_checks:
  - Inspect2024 supporting calculations, full-resolution drawings and any published
    correction to reconcile repeated16R text with Figure 1(S) label for compound 4.
    Also check the paired-analysis A numeric discrepancy and conserved-core assumption.
  - Record a primary-linked unresolved identity discussion and keep SEEDED until adjudicated.
    Do not assign R or S solely from the abstract or diagram; scratch candidate keys
    are alternatives, not recommendations.
  - If a configuration is defensibly resolved, update maintained source/transform,
    synonym, SMILES/InChI/key and exact xrefs consistently, then regenerate through
    validated curation. Preserve B16Cl/17Br versus A16Br/17Cl.
  - Keep B40.4micromolar antimalarial activity separate from A, and retain bacterial/cancer/TB
    censored bounds and method/taxon limits. Mixed fractions and bromophycolide imaging
    do not prove B activity or a direct target.
  - Run focused schema/strict, source provenance, reference/history and required full-corpus
    gates after separately authorized curation.
limitations:
- Original main text, compound 10 structure panel, Table 2, Table 3 and methods were
  inspected; raw spectra were not reanalyzed. Original C16 was left unassigned and
  complete absolute core handedness was not directly established.
- The 2024 main text, Figure 1 and Table 1 were inspected. Text repeatedly calls B16R,
  while its Figure 1 structure4 is labelled(S). This conflict remains unresolved;
  no automatic update is proposed.
- Supporting-PDF retrieval via PMC returned challenge HTML despite HTTP200; ACS returned
  HTTP 403. The paired-analysis A main-text molar-rotation139.5 conflicts with original-derived~539
  and Table 1. B derived~790.5 agrees with reported~791.
- The empirical method assumes conserved core hand and misattributes original C crystallography
  where the2007 crystal wasA. These caveats are distinct from proof that the native
  core is wrong.
- Current public ChEBI, ChemSpider and PubChem all retain the undefined-C16 graph.
  Reaxys was not accessed. Hypothetical R/S candidate keys require evidence-based
  adjudication and full xref review before any use.
- B antibacterial>350, cancermean>25 and TB>10micromolar are bounded results; positive
  malaria40.4 is separate. Quantitative adoption would require resolving original
  bacterial strain identifiers/protocol.
- Original C. serratus isolation naming conflicts with later C. densus group attribution;
  exact-voucher reidentification remains unresolved. No producer correction is asserted.
- No exact molecular target was established from inspected activity/stereochemistry
  studies. Native content does not trigger a protein-expression adapter; this bounded
  review does not claim exhaustive literature coverage or full-corpus success.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 13 repository input hashes remain unchanged; no native or saved-bundle edits.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://doi.org/10.1021/jo071210y
- https://doi.org/10.1021/acs.joc.4c00905
- https://www.ebi.ac.uk/chebi/CHEBI:65566
tags:
- record-review
- callophycol-b
- stereochemistry
```
