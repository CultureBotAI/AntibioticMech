# Callophycoic acid D: exact double-bond regioisomer and activity

- Review: 20261021T104022Z-callophycoic-acid-d
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:21:03Z
- Finished UTC: 2026-10-21T10:40:22Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

No confirmed native defect. The exact six-centre dibrominated acid and its olefin placement agree with the original compound 4 assignment and live identity sources. Table 3 reports S. aureus MIC 26.7 µM, malaria IC50 76.1 µM and cancer-panel mean 23.2 µM. NMR/NOE inference and comparator-only crystal evidence remain explicit; Reaxys and detailed bacterial method/strain mapping are unresolved. Later producer-name reassignment remains qualified pending exact-voucher resolution. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole-record review of exact callophycoic acid D.

Selection: Queue 182 in isolated batch 019; root initial capture preserved.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65560 | data/antibiotics/antibacterial/callophycoic-acid-d.yaml | generated | callophycoic acid D |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | CHEBI:65560 | Actual focused command passed. |
| Focused strict | passed | True | CHEBI:65560 | Actual focused command passed. |
| Independent molecular encodings and source mint | passed | True | CHEBI:65560 | Both encodings, six configurations, formula/charge/masses and source mint agree. |
| Authoritative full QC | failed | True | CHEBI:65560 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65560 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65560 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65560 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65560 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65560 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65560 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65560 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65560 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact dibrominated six-centre acid

identity: supported. Targets: CHEBI:65560.

Native D encodings and six configurations match the original published D assignment and current source identities. Its shifted endocyclic olefin distinguishes D from C. The assignment is MS/NMR/NOE based; the source does not report direct D crystallography.

### Parents and filing/role preservation

grounding: supported. Targets: CHEBI:65560.

Six broader chemical parents are structurally compatible, including tertiary alcohol. ANTIBACTERIAL follows configured priority; antibacterial and antimalarial roles are preserved and supported by exact-congener assays.

### Exact cross-reference verification

grounding: unknown. Targets: CHEBI:65560.

ChemSpider exact identity is verified; Reaxys is inaccessible independently, with no positive mismatch found.

### D regiochemistry, source isolation and activities

evidence: supported. Targets: CHEBI:65560.

Detailed definition agrees with the exact D molecular graph, its regioisomer relation to C and reported Fijian algal isolation. Compound 4 assays support the three stated activity domains. The producer name is a historical attribution qualified by the separate producer-name assessment.

### Compound 4 measured endpoints

evidence: supported. Targets: CHEBI:65560.

The tested S. aureus endpoint is 26.7 µM, while E. faecium is&gt;100 µM; malaria 3D7 IC50 is 76.1 µM. D’s Candida&gt;200 µM result must not be replaced by C’s 107 µM measurement.

### No verified exact molecular mechanism

evidence: unknown. Targets: CHEBI:65560.

The paper proposes biosynthesis and reports activity but does not establish an exact microbial target. No antibacterial or antimalarial mode is inferred from the chemical family.

### Generated audit and maintained owners

provenance: supported. Targets: CHEBI:65560.

Exact source concept, mint and three seed events are coherent. No native curation or status promotion occurred.

### Unpopulated domains and structured adapters

scope: not_applicable. Targets: CHEBI:65560.

No populated resistance, clinical, producer, dataset or graph blocks, and no native named gene/protein/regulator/pathway requires an iModulonDB query. Definition isolation is assessed directly.

### Optional activity enrichment

completeness: supported. Targets: CHEBI:65560.

Primary quantitative observations can inform future strain-resolved curation after method/strain verification. Optional blanks alone are not defects; molecular mode remains honestly unresolved.

### Focused deterministic checks

schema: supported. Targets: CHEBI:65560.

Focused schema/strict and independent encoding/mint checks pass; scientific review retains the external-source limits.

### Historical source species versus later reassignment

evidence: unknown. Targets: CHEBI:65560.

Original 2007 C. serratus isolation is accurately represented as a historical attribution, but later primary literature uses C. densus and retains uncertainty. Exact original-voucher reassignment remains unresolved; this is not a confirmed native wrong-taxon finding.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optionally curate exact assay observations after verifying detailed bacterial methods and strain identifiers.

- Use compound 4/Table 3 in µM, including S. aureus 26.7 µM and malaria 3D7 IC50 76.1 µM; do not copy C’s values.
- Reconcile original ATCC10537/12952 strain identifiers and delegated bacterial method before fully structured MIC adoption.
- Do not transfer antitubercular ≥90% inhibition criteria to the bacterial assay or infer clinical resistance.
- Keep the D-specific NMR/NOE assignment and comparator-only A crystal/C Figure 2 evidence distinct.

### A2

Resolve the original algal voucher before changing or newly grounding the producer species.

- Preserve the 2007 C. serratus attribution while documenting the later C. densus interpretation.
- Establish exact voucher/collection correspondence before a species substitution; do not transfer G-0807 identity from the 2012 study.
- Keep pure-compound antifungal results separate from mixture/fraction experiments and preserve each congener-specific endpoint.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/callophycoic-acid-d.yaml; Entire YAML | supports | Read full CHEBI:65560 record: exact D identity, six-centre definition with olefin at systematic 6/6a and regioisomer relation to C, six parents, two roles, full structure, xrefs, source concept and three events. No populated optional mechanism/activity/target/resistance/producer/clinical/graph blocks. |
| owners | data/raw/chebi_antimicrobials.tsv; ChEBI row 1230; role table and source configuration | supports | ChEBI inventory owns structure, definition, six chemical parents, two antimicrobial roles and PMID:17715978 lead. Extractor/seeder and decisions control generated corrections. Ignored-inclusive search found no exact curator addition. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:65560; Complete live page | supports | Current ChEBI reproduces the neutral C27H36Br2O4 free acid, six-centre structure, six broader chemical parents and both source antimicrobial roles; the extra tertiary-alcohol parent fits the cyclohexanol substituent. |
| chemistry | Independent RDKit encodings and CHEBI mint; Both encodings, all molecular quantities and source mint | supports | Both encodings yield JTJHSEFMUWUYLU-KXSKSBKOSA-N, neutral C27H36Br2O4, one fragment and matching masses. All six tetrahedral configurations agree with the published 6R/7S/10S/11S/14S/24S assignment, mapped to SMILES indices 0/18/22/30/26/16. The exact D mint matches. |
| chemspider | https://www.chemspider.com/Chemical-Structure.27023090.html; Current page and embedded standard identifiers | supports | ChemSpider 27023090 resolves to the same standard InChI/key and exact six-centre molecular form; nonstandard page identifiers remain separate. |
| reaxys | https://www.reaxys.com/reaxys/secured/compound.do?substanceId=11167774; Official destination request; current ChEBI retained registry link | unknown | Reaxys 11167774 is source-asserted but independently inaccessible with HTTP 403. This is an unresolved verification limit, not evidence of a mismatch. |
| primary | https://doi.org/10.1021/jo071210y; PMID:17715978 / PMC3374858; compound 4 Results, Table 3 row 4 and Experimental Section | supports | Original compound 4 is callophycoic acid D. MS/NMR establish the same molecular formula as C but Δ20,21 olefin placement, with explicit 6R/7S/10S/11S/14S/24S assignment by analogous NOE arguments. Table 3 reports S. aureus MIC 26.7 µM, E. faecium&gt;100 µM, tuberculosis&gt;100 µM, malaria IC50 76.1 µM, cancer-panel mean 23.2 µM and Candida MIC&gt;200 µM. Assay conditions and limited organism scope remain attached. |
| figure | https://pmc.ncbi.nlm.nih.gov/articles/PMC3374858/; Numbered structures compound 4 versus compounds 2/3; visual inspection | supports | Published D drawing combines the enol-ether olefin position of B with the cyclohexanol substituent of C, and matches native six-centre topology. Source A crystallography and C-specific Figure 2 NOEs are comparators, not direct D crystallography. |
| methods | https://doi.org/10.1021/jo071210y; Experimental Section Pharmacological Assays | partial | Paper names S. aureusATCC 10537 and E. faeciumATCC 12952, with bacterial procedure delegated to reference 3. Malaria assay uses 3D7, human O+ erythrocytes,2.5% hematocrit/0.5% parasitemia and 72 h incubation. The ≥90% growth-inhibition MIC definition is in the antitubercular methods paragraph and should not automatically be transferred to the bacterial assay. No direct target is measured. |
| search | Ignored-inclusive repository and public literature search; Exact D ID/label/key plus original compound 4 source | context_only | Ignored-inclusive exact D ID/label/key search found native/raw owners and generated references, without an additional exact curated annotation. Original compound 4 structure and assay data were independently assessed within the shared primary paper. |
| gates | just validate; just validate-strict; Actual focused batch 019 commands | supports | Both focused gates exit 0; one strict target with no errors. Internal molecular consistency also passes. |
| noe-figure | https://pmc.ncbi.nlm.nih.gov/articles/PMC3374858/figure/F2/; Figure 2; visual inspection of observed versus absent NOE comparisons | context_only | Figure 2 shows the C-specific cross-link NOE rationale. The D paragraph invokes analogous NOE arguments; this figure is structural context rather than a direct D experiment. |
| taxon-2009 | https://doi.org/10.1073/pnas.0812020106; PMC2678663; Results on chemotypes and identification; Figure 1 caption | partial | The 2009 study retained C. serratus for both chemotypes: morphology identified all samples as that species, while 18S sequences separated two clades matching chemistry. It does not provide a C. densus reassignment. Pure C/G/H had marine fungal activity below 300 µM; E/F were explicitly neither detected nor tested. Fraction antibacterial negatives do not establish pure-compound inactivity. |
| taxon-2012 | https://doi.org/10.1021/jo301246x; PMC3474338; Results opening morphology/genetics passages and comparison to original 2007 paper | partial | The 2012 primary paper retrospectively associates nonmacrocyclic callophycoic acids/callophycols with C. densus and macrocyclic bromophycolides with C. serratus. It describes morphological differences and cites the 2009 genetic study; the inspected text does not resolve the precise 2007 voucher. Its new G-0807 collection belongs to another Callophycus species and must not be mapped to these compounds. |
| taxon-2017 | https://doi.org/10.1021/acs.joc.7b00096; PMC5538829; proposed biosynthesis discussion around Figure 7 | partial | The 2017 paper calls the earlier source of callophycoic H and callophycols another Callophycus member, likely C. densus. Its absolute-configuration revisions concern bromophycoic structures; neither those revisions nor its new iodinated compounds are transferred to this exact callophycoic acid. |

## Limits And Additional Notes

- Reaxys 11167774 returned HTTP 403; its independent molecular identity remains unverified.
- The paper delegates bacterial methods to reference 3; the inspected reference 3 main text did not supply a complete bacterial protocol. Paper-stated strain identifiers have not been independently reconciled, so exact structured MIC adoption requires follow-up.
- D stereochemistry is an MS/NMR/NOE assignment; A crystallography and C Figure 2 are contextual. Full supplementary correlations were not independently reprocessed. No exact microbial molecular mechanism was established in the inspected primary set.
- The original algal voucher was not independently reconciled with later C. densus assignments; the inspected 2009 source still used C. serratus and 2017 qualified the alternative species. This limits current producer grounding without establishing a required native correction.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 13 initial hashes rechecked unchanged; no native/source/status/history edits.
- The primary paper calls D’s Δ20,21 olefin cis while calling the analogous B olefin E elsewhere. These source descriptors were not converted into an extra native geometry finding: the depicted seven-membered-ring connectivity and exact current molecular encodings agree, and the native definition makes no separate E/Z claim at that ring bond.
- Six native centres map to primary 6R/7S/10S/11S/14S/24S. No optional-empty-field or alias-only finding.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T104022Z-callophycoic-acid-d
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Callophycoic acid D: exact double-bond regioisomer and activity'
started_at: '2026-10-21T10:21:03Z'
finished_at: '2026-10-21T10:40:22Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independent whole D native/raw-owner review, exact molecular
    checks and current source retrieval, with original compound 4 structural and assay
    passages assessed separately from C.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: No confirmed native defect. The exact six-centre dibrominated acid and its
  olefin placement agree with the original compound 4 assignment and live identity
  sources. Table 3 reports S. aureus MIC 26.7 µM, malaria IC50 76.1 µM and cancer-panel
  mean 23.2 µM. NMR/NOE inference and comparator-only crystal evidence remain explicit;
  Reaxys and detailed bacterial method/strain mapping are unresolved. Later producer-name
  reassignment remains qualified pending exact-voucher resolution. Scientific assessment
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
  - path: data/antibiotics/antibacterial/callophycoic-acid-d.yaml
    sha256: cf15703410c1e9e0882483a2bd4f93aebd0814a6584ee75c0415cf1d5626204b
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
- target_id: CHEBI:65560
  path: data/antibiotics/antibacterial/callophycoic-acid-d.yaml
  label: callophycoic acid D
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
  description: Whole-record review of exact callophycoic acid D.
  selection: Queue 182 in isolated batch 019; root initial capture preserved.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65560
  exclusions:
  - target: Other callophycoic acids, callophycols and bromophycolides
    reason: Structural comparators only; assays and mechanisms are not transferred.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual focused command passed.
  target_ids:
  - CHEBI:65560
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/callophycoic-acid-d.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: strict
  name: Focused strict
  status: passed
  required: true
  summary: Actual focused command passed.
  target_ids:
  - CHEBI:65560
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/callophycoic-acid-d.yaml --out /private/tmp/am-review-session/182-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Independent molecular encodings and source mint
  status: passed
  required: true
  summary: Both encodings, six configurations, formula/charge/masses and source mint
    agree.
  target_ids:
  - CHEBI:65560
  evidence_ids:
  - chemistry
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:65560
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
  - CHEBI:65560
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
  - CHEBI:65560
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
  - CHEBI:65560
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
  - CHEBI:65560
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
  - CHEBI:65560
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
  - CHEBI:65560
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
  - CHEBI:65560
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
  - CHEBI:65560
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/callophycoic-acid-d.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T10:24:50Z'
  support: supports
  summary: 'Read full CHEBI:65560 record: exact D identity, six-centre definition
    with olefin at systematic 6/6a and regioisomer relation to C, six parents, two
    roles, full structure, xrefs, source concept and three events. No populated optional
    mechanism/activity/target/resistance/producer/clinical/graph blocks.'
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: ChEBI row 1230; role table and source configuration
  accessed_at: '2026-10-21T10:24:50Z'
  support: supports
  summary: ChEBI inventory owns structure, definition, six chemical parents, two antimicrobial
    roles and PMID:17715978 lead. Extractor/seeder and decisions control generated
    corrections. Ignored-inclusive search found no exact curator addition.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:65560
  locator: Complete live page
  accessed_at: '2026-10-21T10:24:15Z'
  support: supports
  summary: Current ChEBI reproduces the neutral C27H36Br2O4 free acid, six-centre
    structure, six broader chemical parents and both source antimicrobial roles; the
    extra tertiary-alcohol parent fits the cyclohexanol substituent.
  snapshot_sha256: 42851d97c316c57b31ec39e84a3bcfb1cdb76f0d7d8f991f1ed19d15a34b323e
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit encodings and CHEBI mint
  locator: Both encodings, all molecular quantities and source mint
  accessed_at: '2026-10-21T10:24:11Z'
  support: supports
  summary: Both encodings yield JTJHSEFMUWUYLU-KXSKSBKOSA-N, neutral C27H36Br2O4,
    one fragment and matching masses. All six tetrahedral configurations agree with
    the published 6R/7S/10S/11S/14S/24S assignment, mapped to SMILES indices 0/18/22/30/26/16.
    The exact D mint matches.
  snapshot_sha256: 8f73a125e654c6a2a7847e514b4b128c1ee38052bd1a9ad2bc49c914b2d71403
- evidence_id: chemspider
  kind: database
  reference: https://www.chemspider.com/Chemical-Structure.27023090.html
  locator: Current page and embedded standard identifiers
  accessed_at: '2026-10-21T10:24:15Z'
  support: supports
  summary: ChemSpider 27023090 resolves to the same standard InChI/key and exact six-centre
    molecular form; nonstandard page identifiers remain separate.
  snapshot_sha256: 75686f5391b1fadad7aa1fec61a0d54bd512df4f9d362af7eb402d2c8f304412
- evidence_id: reaxys
  kind: database
  reference: https://www.reaxys.com/reaxys/secured/compound.do?substanceId=11167774
  locator: Official destination request; current ChEBI retained registry link
  accessed_at: '2026-10-21T10:24:15Z'
  support: unknown
  summary: Reaxys 11167774 is source-asserted but independently inaccessible with
    HTTP 403. This is an unresolved verification limit, not evidence of a mismatch.
  snapshot_sha256: d2662da37e5614e32bf8094cc5f79f73d0d65b514a797885e2cdba556684cd4e
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1021/jo071210y
  locator: PMID:17715978 / PMC3374858; compound 4 Results, Table 3 row 4 and Experimental
    Section
  accessed_at: '2026-10-21T10:17:41Z'
  support: supports
  summary: Original compound 4 is callophycoic acid D. MS/NMR establish the same molecular
    formula as C but Δ20,21 olefin placement, with explicit 6R/7S/10S/11S/14S/24S
    assignment by analogous NOE arguments. Table 3 reports S. aureus MIC 26.7 µM,
    E. faecium>100 µM, tuberculosis>100 µM, malaria IC50 76.1 µM, cancer-panel mean
    23.2 µM and Candida MIC>200 µM. Assay conditions and limited organism scope remain
    attached.
  snapshot_sha256: bcf3f54e5acf5cb0bb6c5d42bf9e5b9d99fee62da8b6fe2768f0859545f956fd
- evidence_id: figure
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3374858/
  locator: Numbered structures compound 4 versus compounds 2/3; visual inspection
  accessed_at: '2026-10-21T10:18:16Z'
  support: supports
  summary: Published D drawing combines the enol-ether olefin position of B with the
    cyclohexanol substituent of C, and matches native six-centre topology. Source
    A crystallography and C-specific Figure 2 NOEs are comparators, not direct D crystallography.
  snapshot_sha256: e345b6e7eff021b23a970f18818e3bef36cfa92afae864a683a48f15aa9c8781
- evidence_id: methods
  kind: primary_source
  reference: https://doi.org/10.1021/jo071210y
  locator: Experimental Section Pharmacological Assays
  accessed_at: '2026-10-21T10:17:41Z'
  support: partial
  summary: Paper names S. aureusATCC 10537 and E. faeciumATCC 12952, with bacterial
    procedure delegated to reference 3. Malaria assay uses 3D7, human O+ erythrocytes,2.5%
    hematocrit/0.5% parasitemia and 72 h incubation. The ≥90% growth-inhibition MIC
    definition is in the antitubercular methods paragraph and should not automatically
    be transferred to the bacterial assay. No direct target is measured.
  snapshot_sha256: bcf3f54e5acf5cb0bb6c5d42bf9e5b9d99fee62da8b6fe2768f0859545f956fd
- evidence_id: search
  kind: search
  reference: Ignored-inclusive repository and public literature search
  locator: Exact D ID/label/key plus original compound 4 source
  accessed_at: '2026-10-21T10:24:09Z'
  support: context_only
  summary: Ignored-inclusive exact D ID/label/key search found native/raw owners and
    generated references, without an additional exact curated annotation. Original
    compound 4 structure and assay data were independently assessed within the shared
    primary paper.
  search_scope: rg --no-ignore --hidden CHEBI:65560/callophycoic-acid-D/JTJHSEFMUWUYLU
    outside.git/.venv; current ChEBI/ChemSpider/Reaxys; original PMID17715978 compound
    4 text and Table 3, accessed 2026-10-21.
  snapshot_sha256: c4ee8f3a8ec4891ad5b204146c3d301337d2460fe4d6b95d3e62f6bc78a8dac0
- evidence_id: gates
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual focused batch 019 commands
  accessed_at: '2026-10-21T10:24:50Z'
  support: supports
  summary: Both focused gates exit 0; one strict target with no errors. Internal molecular
    consistency also passes.
  snapshot_sha256: bf842ea0b16b9e34f9d7e88b9b04eb9b92558a9e4231bd57edd8a4f177ac62a1
- evidence_id: noe-figure
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3374858/figure/F2/
  locator: Figure 2; visual inspection of observed versus absent NOE comparisons
  accessed_at: '2026-10-21T10:22:21Z'
  support: context_only
  summary: Figure 2 shows the C-specific cross-link NOE rationale. The D paragraph
    invokes analogous NOE arguments; this figure is structural context rather than
    a direct D experiment.
  snapshot_sha256: c3788ba85ff034040245db400dcb41cf99d710eba021ed54589b76136b6d2b9d
- evidence_id: taxon-2009
  kind: primary_source
  reference: https://doi.org/10.1073/pnas.0812020106
  locator: PMC2678663; Results on chemotypes and identification; Figure 1 caption
  accessed_at: '2026-10-21T10:29:30Z'
  support: partial
  summary: 'The 2009 study retained C. serratus for both chemotypes: morphology identified
    all samples as that species, while 18S sequences separated two clades matching
    chemistry. It does not provide a C. densus reassignment. Pure C/G/H had marine
    fungal activity below 300 µM; E/F were explicitly neither detected nor tested.
    Fraction antibacterial negatives do not establish pure-compound inactivity.'
  snapshot_sha256: a5ebe2957910dffee14703083186dee433a28ce6eb60a4e845ff9a692c0a00d3
- evidence_id: taxon-2012
  kind: primary_source
  reference: https://doi.org/10.1021/jo301246x
  locator: PMC3474338; Results opening morphology/genetics passages and comparison
    to original 2007 paper
  accessed_at: '2026-10-21T10:28:14Z'
  support: partial
  summary: The 2012 primary paper retrospectively associates nonmacrocyclic callophycoic
    acids/callophycols with C. densus and macrocyclic bromophycolides with C. serratus.
    It describes morphological differences and cites the 2009 genetic study; the inspected
    text does not resolve the precise 2007 voucher. Its new G-0807 collection belongs
    to another Callophycus species and must not be mapped to these compounds.
  snapshot_sha256: c8ea74b2bbc981d5c1416b43200921cecbcd1f63f471b5dfe3beae1901cae82b
- evidence_id: taxon-2017
  kind: primary_source
  reference: https://doi.org/10.1021/acs.joc.7b00096
  locator: PMC5538829; proposed biosynthesis discussion around Figure 7
  accessed_at: '2026-10-21T10:30:00Z'
  support: partial
  summary: The 2017 paper calls the earlier source of callophycoic H and callophycols
    another Callophycus member, likely C. densus. Its absolute-configuration revisions
    concern bromophycoic structures; neither those revisions nor its new iodinated
    compounds are transferred to this exact callophycoic acid.
  snapshot_sha256: 57cedac94bfb491cfab33e4c138571ed4586538a72dae1dfda1fc2adb013b16c
assessments:
- assessment_id: identity
  area: identity
  topic: Exact dibrominated six-centre acid
  outcome: supported
  summary: Native D encodings and six configurations match the original published
    D assignment and current source identities. Its shifted endocyclic olefin distinguishes
    D from C. The assignment is MS/NMR/NOE based; the source does not report direct
    D crystallography.
  target_ids:
  - CHEBI:65560
  evidence_ids:
  - native
  - chebi
  - chemistry
  - chemspider
  - primary
  - figure
  - noe-figure
- assessment_id: grounding
  area: grounding
  topic: Parents and filing/role preservation
  outcome: supported
  summary: Six broader chemical parents are structurally compatible, including tertiary
    alcohol. ANTIBACTERIAL follows configured priority; antibacterial and antimalarial
    roles are preserved and supported by exact-congener assays.
  target_ids:
  - CHEBI:65560
  evidence_ids:
  - owners
  - chebi
  - primary
- assessment_id: xref
  area: grounding
  topic: Exact cross-reference verification
  outcome: unknown
  summary: ChemSpider exact identity is verified; Reaxys is inaccessible independently,
    with no positive mismatch found.
  target_ids:
  - CHEBI:65560
  evidence_ids:
  - chemspider
  - reaxys
- assessment_id: definition
  area: evidence
  topic: D regiochemistry, source isolation and activities
  outcome: supported
  summary: Detailed definition agrees with the exact D molecular graph, its regioisomer
    relation to C and reported Fijian algal isolation. Compound 4 assays support the
    three stated activity domains. The producer name is a historical attribution qualified
    by the separate producer-name assessment.
  target_ids:
  - CHEBI:65560
  evidence_ids:
  - primary
  - methods
  - figure
  - chemistry
  - taxon-2012
- assessment_id: activity
  area: evidence
  topic: Compound 4 measured endpoints
  outcome: supported
  summary: The tested S. aureus endpoint is 26.7 µM, while E. faecium is>100 µM; malaria
    3D7 IC50 is 76.1 µM. D’s Candida>200 µM result must not be replaced by C’s 107
    µM measurement.
  target_ids:
  - CHEBI:65560
  evidence_ids:
  - primary
  - methods
- assessment_id: mechanism
  area: evidence
  topic: No verified exact molecular mechanism
  outcome: unknown
  summary: The paper proposes biosynthesis and reports activity but does not establish
    an exact microbial target. No antibacterial or antimalarial mode is inferred from
    the chemical family.
  target_ids:
  - CHEBI:65560
  evidence_ids:
  - primary
  - methods
  - search
- assessment_id: history
  area: provenance
  topic: Generated audit and maintained owners
  outcome: supported
  summary: Exact source concept, mint and three seed events are coherent. No native
    curation or status promotion occurred.
  target_ids:
  - CHEBI:65560
  evidence_ids:
  - native
  - owners
  - chemistry
- assessment_id: other
  area: scope
  topic: Unpopulated domains and structured adapters
  outcome: not_applicable
  summary: No populated resistance, clinical, producer, dataset or graph blocks, and
    no native named gene/protein/regulator/pathway requires an iModulonDB query. Definition
    isolation is assessed directly.
  target_ids:
  - CHEBI:65560
  evidence_ids:
  - native
- assessment_id: completeness
  area: completeness
  topic: Optional activity enrichment
  outcome: supported
  summary: Primary quantitative observations can inform future strain-resolved curation
    after method/strain verification. Optional blanks alone are not defects; molecular
    mode remains honestly unresolved.
  target_ids:
  - CHEBI:65560
  evidence_ids:
  - primary
  - methods
- assessment_id: schema
  area: schema
  topic: Focused deterministic checks
  outcome: supported
  summary: Focused schema/strict and independent encoding/mint checks pass; scientific
    review retains the external-source limits.
  target_ids:
  - CHEBI:65560
  evidence_ids:
  - gates
  - chemistry
- assessment_id: producer-name
  area: evidence
  topic: Historical source species versus later reassignment
  outcome: unknown
  summary: Original 2007 C. serratus isolation is accurately represented as a historical
    attribution, but later primary literature uses C. densus and retains uncertainty.
    Exact original-voucher reassignment remains unresolved; this is not a confirmed
    native wrong-taxon finding.
  target_ids:
  - CHEBI:65560
  evidence_ids:
  - primary
  - taxon-2009
  - taxon-2012
  - taxon-2017
findings: []
actions:
- action_id: A1
  description: Optionally curate exact assay observations after verifying detailed
    bacterial methods and strain identifiers.
  finding_ids: []
  target_ids:
  - CHEBI:65560
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/callophycoic-acid-d.yaml
    role: Future curator-owned activity observations through validated writer
  acceptance_checks:
  - Use compound 4/Table 3 in µM, including S. aureus 26.7 µM and malaria 3D7 IC50
    76.1 µM; do not copy C’s values.
  - Reconcile original ATCC10537/12952 strain identifiers and delegated bacterial
    method before fully structured MIC adoption.
  - Do not transfer antitubercular ≥90% inhibition criteria to the bacterial assay
    or infer clinical resistance.
  - Keep the D-specific NMR/NOE assignment and comparator-only A crystal/C Figure
    2 evidence distinct.
- action_id: A2
  description: Resolve the original algal voucher before changing or newly grounding
    the producer species.
  finding_ids: []
  target_ids:
  - CHEBI:65560
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Maintained source definition through extractor or source correction
  acceptance_checks:
  - Preserve the 2007 C. serratus attribution while documenting the later C. densus
    interpretation.
  - Establish exact voucher/collection correspondence before a species substitution;
    do not transfer G-0807 identity from the 2012 study.
  - Keep pure-compound antifungal results separate from mixture/fraction experiments
    and preserve each congener-specific endpoint.
limitations:
- Reaxys 11167774 returned HTTP 403; its independent molecular identity remains unverified.
- The paper delegates bacterial methods to reference 3; the inspected reference 3
  main text did not supply a complete bacterial protocol. Paper-stated strain identifiers
  have not been independently reconciled, so exact structured MIC adoption requires
  follow-up.
- D stereochemistry is an MS/NMR/NOE assignment; A crystallography and C Figure 2
  are contextual. Full supplementary correlations were not independently reprocessed.
  No exact microbial molecular mechanism was established in the inspected primary
  set.
- The original algal voucher was not independently reconciled with later C. densus
  assignments; the inspected 2009 source still used C. serratus and 2017 qualified
  the alternative species. This limits current producer grounding without establishing
  a required native correction.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 13 initial hashes rechecked unchanged; no native/source/status/history edits.
- 'The primary paper calls D’s Δ20,21 olefin cis while calling the analogous B olefin
  E elsewhere. These source descriptors were not converted into an extra native geometry
  finding: the depicted seven-membered-ring connectivity and exact current molecular
  encodings agree, and the native definition makes no separate E/Z claim at that ring
  bond.'
- Six native centres map to primary 6R/7S/10S/11S/14S/24S. No optional-empty-field
  or alias-only finding.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:65560
- https://doi.org/10.1021/jo071210y
tags:
- callophycoic-acid-d
- marine-natural-product
- regioisomer
- assay-scope
```
