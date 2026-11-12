# Callophycoic acid E: proposed stereochemistry and bounded activity evidence

- Review: 20261021T104032Z-callophycoic-acid-e
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:21:04Z
- Finished UTC: 2026-10-21T10:40:32Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

No confirmed native defect. Native E matches the five-centre proposed structure and current authority, including its exomethylene group. The original source could not determine the cyclohexane orientation directly; graph comparison resolves the apparent C10 S/R nomenclature difference as a ligand-priority change. Exact positive antibacterial and cancer endpoints were not verified in the bounded primary panel, which does support antimalarial activity. Producer-name, Reaxys and assay-method uncertainties remain explicit. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole-record review of exact callophycoic acid E.

Selection: Queue 183 in isolated batch 019; root initial capture preserved; D comparator captured before independent graph comparison.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65561 | data/antibiotics/antibacterial/callophycoic-acid-e.yaml | generated | callophycoic acid E |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | CHEBI:65561 | Actual focused command passed. |
| Focused strict | passed | True | CHEBI:65561 | Actual focused command passed. |
| Independent molecular encodings and source mint | passed | True | CHEBI:65561 | Both encodings, five configurations, formula/charge/masses and source mint agree; independent comparator transformation reproduces the E key. |
| Authoritative full QC | failed | True | CHEBI:65561 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65561 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65561 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65561 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65561 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65561 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65561 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65561 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65561 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact E graph versus proposed full orientation

identity: supported. Targets: CHEBI:65561.

Native E is internally consistent and matches the published proposed relative drawing and current authorities. Source C10S versus native C10R is explained by the changed ligand priorities upon exomethylene formation, with no inversion. Absolute experimental support for the ring orientation remains limited.

### Parents and filing/role preservation

grounding: unknown. Targets: CHEBI:65561.

Five chemical parents match the graph and filing follows configured role priority. The antimalarial role has an exact measured endpoint; source antibacterial classification remains unresolved by the inspected above-limit bacterial panel. This bounded negative result is not sufficient to delete a role or exclude the record.

### Exact cross-reference verification

grounding: unknown. Targets: CHEBI:65561.

ChemSpider exact identity is verified; Reaxys is inaccessible independently, with no positive mismatch found.

### Structural proposal, historical producer and stated activities

evidence: unknown. Targets: CHEBI:65561.

Structural identity agrees with the published E proposal. Exact positive antibacterial and cancer claims were not independently established by the inspected original panel, while malaria 96.2 µM and Candida 110 µM are measured. Producer attribution remains historical and qualified by later species uncertainty; no required native correction is established.

### Original compound 5 assay limits

evidence: unknown. Targets: CHEBI:65561.

Preserve MIC &gt;500 µM S. aureus and &gt;100 µM E. faecium, cancer mean IC50 &gt;25 µM and malaria IC50 96.2 µM as distinct observations. These upper-range testing limits neither verify positive antibacterial/cancer activity nor establish universal inactivity. Candida MIC 110 µM is a separate fungal observation.

### No verified exact molecular mechanism

evidence: unknown. Targets: CHEBI:65561.

The paper proposes biosynthesis and reports activity but does not establish an exact microbial target. No antibacterial or antimalarial mode is inferred from the chemical family.

### Generated audit and maintained owners

provenance: supported. Targets: CHEBI:65561.

Exact source concept, mint and three seed events are coherent. No native curation or status promotion occurred.

### Unpopulated domains and structured adapters

scope: not_applicable. Targets: CHEBI:65561.

No populated resistance, clinical, producer, dataset or graph blocks, and no native named gene/protein/regulator/pathway requires an iModulonDB query. Definition isolation is assessed directly.

### Optional activity enrichment

completeness: supported. Targets: CHEBI:65561.

Bounded exact observations and proposed-stereochemistry context can support optional enrichment. Any positive antibacterial/cancer qualification or fully resolved absolute assignment needs exact E evidence; missing optional blocks are not defects.

### Focused deterministic checks

schema: supported. Targets: CHEBI:65561.

Focused schema/strict and independent encoding/mint checks pass; scientific review retains the external-source limits.

### Historical source species versus later reassignment

evidence: unknown. Targets: CHEBI:65561.

Original 2007 C. serratus isolation is accurately represented as a historical attribution, but later primary literature uses C. densus and retains uncertainty. Exact original-voucher reassignment remains unresolved; this is not a confirmed native wrong-taxon finding.

### Proposed ring orientation

evidence: unknown. Targets: CHEBI:65561.

Original E NOEs did not determine how its cyclohexane ring is oriented relative to the tricycle. Authors proposed the orientation by C/D analogy; current authority reproduces that exact proposal. A later direct assignment was not verified in the bounded search, so the graph is not described as independently proven.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optionally enrich E-specific assay limits and structure-evidence qualification; seek exact positive antibacterial/cancer or independent full stereochemical evidence.

- Use original compound 5/Table 3 values and inequality signs, including malaria 96.2 µM and Candida 110 µM.
- Resolve original bacterial identifiers/methods before structured MIC adoption; do not label &gt;500/&gt;100 µM as proven universal inactivity.
- Do not transfer positive C/D/G assays to E or delete eligibility solely from above-range endpoints.
- Preserve proposed ring orientation; compare atom-mapped graphs before interpreting source 10S versus modern CIP 10R as inversion.

### A2

Resolve the original algal voucher before changing or newly grounding the producer species.

- Preserve the 2007 C. serratus attribution while documenting the later C. densus interpretation.
- Establish exact voucher/collection correspondence before a species substitution; do not transfer G-0807 identity from the 2012 study.
- Keep pure-compound antifungal results separate from mixture/fraction experiments and preserve each congener-specific endpoint.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/callophycoic-acid-e.yaml; Entire YAML | supports | Read complete CHEBI:65561 record: exact E identity, five-centre substituent definition and C. serratus isolation/activity claims, five parents, two roles, full structure, xrefs, source concept and three events. No populated optional mechanism/activity/target/resistance/producer/clinical/graph blocks. |
| owners | data/raw/chebi_antimicrobials.tsv; ChEBI row 1231; role table and source configuration | supports | Adopted ChEBI row owns five parents, antibacterial/antimalarial roles, structure, definition and PMID17715978 lead; generated corrections belong in source extraction/decisions or appropriate curator-owned fields. Ignored-inclusive exact search found no additional curator annotation. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:65561; Complete live page | supports | Current ChEBI reproduces neutral C27H34Br2O3, five-centre exact E structure and five broader chemical parents. Exomethylene replaces the C/D tertiary alcohol, so that parent is correctly absent. Source antibacterial and antimalarial roles are retained. |
| chemistry | Independent RDKit encodings and CHEBI mint; Both encodings, all molecular quantities and source mint | supports | Both native encodings yield PSYSMHVCBGMCIW-FBHGCBBZSA-N, neutral C27H34Br2O3, one fragment and matching masses, with five assigned centres. Native atom indices 0/18/16/22/27 map to original source-numbered C6/C7/C24/C10/C14 and modern CIP R/S/S/R/S. The exact E mint matches. |
| chemspider | https://www.chemspider.com/Chemical-Structure.27023091.html; Current page and embedded standard identifiers | supports | ChemSpider 27023091 resolves to the same standard InChI/key and five-centre exact E form; alternate page identifiers were not conflated. |
| reaxys | https://www.reaxys.com/reaxys/secured/compound.do?substanceId=11167775; Official destination request; current ChEBI retained registry link | unknown | Reaxys 11167775 is source-asserted but independently inaccessible with HTTP 403. This is an unresolved verification limit, not evidence of a mismatch. |
| primary | https://doi.org/10.1021/jo071210y; PMID17715978 / PMC3374858; compound 5 Results, Table 3 row 5 and Experimental Section | partial | Original compound 5 is E, with exomethylene Δ11,26 replacing the methyl/hydroxyl arrangement in D. The 6R/7S/24S core follows analogous NOEs, but NOEs did not resolve the cyclohexane orientation relative to the tricycle; authors proposed 10S/14S by analogy. Table 3 reports bacterial MICs &gt;500 µM S. aureus and &gt;100 µM E. faecium, tuberculosis &gt;100 µM, cancer mean IC50 &gt;25 µM, malaria IC50 96.2 µM and Candida MIC 110 µM. Above-limit results do not prove universal inactivity. |
| figure | https://pmc.ncbi.nlm.nih.gov/articles/PMC3374858/; Numbered structure 5 versus 4; visual inspection | partial | Published E drawing has the D-like tricycle and cyclohexane ring, replacing tertiary hydroxyl/methyl by exomethylene. Its relative configuration matches the native proposed graph. Figure 1 is an A crystal, not E crystallography. |
| methods | https://doi.org/10.1021/jo071210y; Experimental Section Pharmacological Assays | partial | Paper names S. aureusATCC 10537 and E. faeciumATCC 12952, with bacterial procedure delegated to reference 3. Malaria assay uses 3D7, human O+ erythrocytes,2.5% hematocrit/0.5% parasitemia and 72 h incubation. The ≥90% growth-inhibition MIC definition is in the antitubercular methods paragraph and should not automatically be transferred to the bacterial assay. No direct target is measured. |
| search | Ignored-inclusive repository and public literature search; Exact E ID/label/key and source-numbered compound 5 search | context_only | Ignored-inclusive repository search found exact native/raw/generated references without additional exact curator annotation. Public exact-name literature follow-up located original 2007, later shared-taxonomy and comparator papers; no later independently verified exact E antibacterial/cancer positive or complete absolute assignment was established. |
| gates | just validate; just validate-strict; Actual focused batch 019 commands | supports | Both focused gates exit 0; one strict target with no errors. Internal molecular consistency also passes. |
| noe-figure | https://pmc.ncbi.nlm.nih.gov/articles/PMC3374858/figure/F2/; Figure 2; visual inspection of observed versus absent NOE comparisons | context_only | C-specific Figure 2 illustrates the comparator NOE rationale. It does not supply the E ring orientation that the E paragraph explicitly says was unresolved. |
| taxon-2009 | https://doi.org/10.1073/pnas.0812020106; PMC2678663; Results on chemotypes and identification; Figure 1 caption | partial | The 2009 study retained C. serratus for both chemotypes: morphology identified all samples as that species, while 18S sequences separated two clades matching chemistry. It does not provide a C. densus reassignment. Pure C/G/H had marine fungal activity below 300 µM; E/F were explicitly neither detected nor tested. Fraction antibacterial negatives do not establish pure-compound inactivity. |
| taxon-2012 | https://doi.org/10.1021/jo301246x; PMC3474338; Results opening morphology/genetics passages and comparison to original 2007 paper | partial | The 2012 primary paper retrospectively associates nonmacrocyclic callophycoic acids/callophycols with C. densus and macrocyclic bromophycolides with C. serratus. It describes morphological differences and cites the 2009 genetic study; the inspected text does not resolve the precise 2007 voucher. Its new G-0807 collection belongs to another Callophycus species and must not be mapped to these compounds. |
| taxon-2017 | https://doi.org/10.1021/acs.joc.7b00096; PMC5538829; proposed biosynthesis discussion around Figure 7 | partial | The 2017 paper calls the earlier source of callophycoic H and callophycols another Callophycus member, likely C. densus. Its absolute-configuration revisions concern bromophycoic structures; neither those revisions nor its new iodinated compounds are transferred to this exact callophycoic acid. |
| stereo-comparison | Scratch RDKit atom-preserving D-to-E comparison; 183-stereo-comparison.json; source-number C10 mapped to retained atom 22 | supports | Remove D hydroxyl O32, convert C30-C31 to exomethylene, clear now-sp 2 C30 stereo and retain all other chirality tags. The resulting graph gives the exact native E InChIKey; C10 changes CIP S to R without inversion. This resolves the descriptor difference as ligand-priority change, not a native stereochemical error. It is a graph comparison, not synthesis or independent proof of absolute orientation. |

## Limits And Additional Notes

- Reaxys 11167775 returned HTTP 403; its independent molecular identity remains unverified.
- The paper delegates bacterial methods to reference 3; the inspected reference 3 main text did not supply a complete bacterial protocol. Paper-stated strain identifiers have not been independently reconciled, so exact structured MIC adoption requires follow-up.
- The original algal voucher was not independently reconciled with later C. densus assignments; the inspected 2009 source still used C. serratus and 2017 qualified the alternative species. This limits current producer grounding without establishing a required native correction.
- E ring orientation relative to the tricycle was proposed by analogy, not determined from its NOEs. Exact positive antibacterial/cancer endpoints and a later independent full absolute assignment were not verified; the measured assay limits do not settle all possible activity.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Initial 13 source hashes remain unchanged; the D comparator was additionally captured before graph comparison. All 14 captured hashes rechecked. No native/source/status/history edits.
- The scratch D-to-E operation preserves chirality tags and gives the native E key; this is a molecular-graph consistency inference only.
- Source-name conflict is qualified, and no optional-empty-field, alias-only or above-limit-inactivity finding was created.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T104032Z-callophycoic-acid-e
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Callophycoic acid E: proposed stereochemistry and bounded activity evidence'
started_at: '2026-10-21T10:21:04Z'
finished_at: '2026-10-21T10:40:32Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independent full E native/raw-owner review, exact encodings
    and live identities, original compound 5 text/figure/assays, and an atom-mapped
    D-to-E graph comparison that preserves chirality tags.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: No confirmed native defect. Native E matches the five-centre proposed structure
  and current authority, including its exomethylene group. The original source could
  not determine the cyclohexane orientation directly; graph comparison resolves the
  apparent C10 S/R nomenclature difference as a ligand-priority change. Exact positive
  antibacterial and cancer endpoints were not verified in the bounded primary panel,
  which does support antimalarial activity. Producer-name, Reaxys and assay-method
  uncertainties remain explicit. Scientific assessment retains the stated evidence
  limits; full verification is blocked by the shared native-library failure.
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
    role: context
  - path: data/antibiotics/antibacterial/callophycoic-acid-e.yaml
    sha256: 9f4ed2a7c99d2c98f924abc034143f2d1070dbff536caec00a8c737b63ae8215
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
- target_id: CHEBI:65561
  path: data/antibiotics/antibacterial/callophycoic-acid-e.yaml
  label: callophycoic acid E
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
  description: Whole-record review of exact callophycoic acid E.
  selection: Queue 183 in isolated batch 019; root initial capture preserved; D comparator
    captured before independent graph comparison.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65561
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
  - CHEBI:65561
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/callophycoic-acid-e.yaml
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
  - CHEBI:65561
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/callophycoic-acid-e.yaml --out /private/tmp/am-review-session/183-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Independent molecular encodings and source mint
  status: passed
  required: true
  summary: Both encodings, five configurations, formula/charge/masses and source mint
    agree; independent comparator transformation reproduces the E key.
  target_ids:
  - CHEBI:65561
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
  - CHEBI:65561
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
  - CHEBI:65561
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
  - CHEBI:65561
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
  - CHEBI:65561
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
  - CHEBI:65561
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
  - CHEBI:65561
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
  - CHEBI:65561
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
  - CHEBI:65561
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
  - CHEBI:65561
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/callophycoic-acid-e.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T10:31:15Z'
  support: supports
  summary: 'Read complete CHEBI:65561 record: exact E identity, five-centre substituent
    definition and C. serratus isolation/activity claims, five parents, two roles,
    full structure, xrefs, source concept and three events. No populated optional
    mechanism/activity/target/resistance/producer/clinical/graph blocks.'
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: ChEBI row 1231; role table and source configuration
  accessed_at: '2026-10-21T10:31:15Z'
  support: supports
  summary: Adopted ChEBI row owns five parents, antibacterial/antimalarial roles,
    structure, definition and PMID17715978 lead; generated corrections belong in source
    extraction/decisions or appropriate curator-owned fields. Ignored-inclusive exact
    search found no additional curator annotation.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:65561
  locator: Complete live page
  accessed_at: '2026-10-21T10:25:46Z'
  support: supports
  summary: Current ChEBI reproduces neutral C27H34Br2O3, five-centre exact E structure
    and five broader chemical parents. Exomethylene replaces the C/D tertiary alcohol,
    so that parent is correctly absent. Source antibacterial and antimalarial roles
    are retained.
  snapshot_sha256: 5c710cd54b6fc781f13fa7770a884c7ea8d3b245a865cf5ab7b42c80101a62f9
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit encodings and CHEBI mint
  locator: Both encodings, all molecular quantities and source mint
  accessed_at: '2026-10-21T10:25:42Z'
  support: supports
  summary: Both native encodings yield PSYSMHVCBGMCIW-FBHGCBBZSA-N, neutral C27H34Br2O3,
    one fragment and matching masses, with five assigned centres. Native atom indices
    0/18/16/22/27 map to original source-numbered C6/C7/C24/C10/C14 and modern CIP
    R/S/S/R/S. The exact E mint matches.
  snapshot_sha256: d87df72067693f6fab03bedbf74b918b72c12bb0436fd88023fdaaae56054e49
- evidence_id: chemspider
  kind: database
  reference: https://www.chemspider.com/Chemical-Structure.27023091.html
  locator: Current page and embedded standard identifiers
  accessed_at: '2026-10-21T10:25:46Z'
  support: supports
  summary: ChemSpider 27023091 resolves to the same standard InChI/key and five-centre
    exact E form; alternate page identifiers were not conflated.
  snapshot_sha256: 219b10c0b28f83e48b22705ebb31f74748e659d5264a6c91770791fe4b9a8731
- evidence_id: reaxys
  kind: database
  reference: https://www.reaxys.com/reaxys/secured/compound.do?substanceId=11167775
  locator: Official destination request; current ChEBI retained registry link
  accessed_at: '2026-10-21T10:25:46Z'
  support: unknown
  summary: Reaxys 11167775 is source-asserted but independently inaccessible with
    HTTP 403. This is an unresolved verification limit, not evidence of a mismatch.
  snapshot_sha256: 95ff6b75d5489ef4f994311bb91b169844d90db7c10b4984596cf9a7b96f931c
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1021/jo071210y
  locator: PMID17715978 / PMC3374858; compound 5 Results, Table 3 row 5 and Experimental
    Section
  accessed_at: '2026-10-21T10:17:41Z'
  support: partial
  summary: Original compound 5 is E, with exomethylene Δ11,26 replacing the methyl/hydroxyl
    arrangement in D. The 6R/7S/24S core follows analogous NOEs, but NOEs did not
    resolve the cyclohexane orientation relative to the tricycle; authors proposed
    10S/14S by analogy. Table 3 reports bacterial MICs >500 µM S. aureus and >100
    µM E. faecium, tuberculosis >100 µM, cancer mean IC50 >25 µM, malaria IC50 96.2
    µM and Candida MIC 110 µM. Above-limit results do not prove universal inactivity.
  snapshot_sha256: bcf3f54e5acf5cb0bb6c5d42bf9e5b9d99fee62da8b6fe2768f0859545f956fd
- evidence_id: figure
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3374858/
  locator: Numbered structure 5 versus 4; visual inspection
  accessed_at: '2026-10-21T10:18:16Z'
  support: partial
  summary: Published E drawing has the D-like tricycle and cyclohexane ring, replacing
    tertiary hydroxyl/methyl by exomethylene. Its relative configuration matches the
    native proposed graph. Figure 1 is an A crystal, not E crystallography.
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
  locator: Exact E ID/label/key and source-numbered compound 5 search
  accessed_at: '2026-10-21T10:25:40Z'
  support: context_only
  summary: Ignored-inclusive repository search found exact native/raw/generated references
    without additional exact curator annotation. Public exact-name literature follow-up
    located original 2007, later shared-taxonomy and comparator papers; no later independently
    verified exact E antibacterial/cancer positive or complete absolute assignment
    was established.
  search_scope: rg --no-ignore --hidden exact CHEBI:65561/label/key outside .git/.venv;
    current ChEBI/ChemSpider/Reaxys; EPMC exact-name query and web exact-name primary
    leads through 2026-10-21.
  snapshot_sha256: bf4c95ea21f042827289dd40cae613dc398f053659e4bcdfa5f1ddd5c00b80f1
- evidence_id: gates
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual focused batch 019 commands
  accessed_at: '2026-10-21T10:31:15Z'
  support: supports
  summary: Both focused gates exit 0; one strict target with no errors. Internal molecular
    consistency also passes.
  snapshot_sha256: 501f319ead37b8a2c16302764fa1a9392b5c06f4ed4825fad7c0a2966f193d6d
- evidence_id: noe-figure
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3374858/figure/F2/
  locator: Figure 2; visual inspection of observed versus absent NOE comparisons
  accessed_at: '2026-10-21T10:22:21Z'
  support: context_only
  summary: C-specific Figure 2 illustrates the comparator NOE rationale. It does not
    supply the E ring orientation that the E paragraph explicitly says was unresolved.
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
- evidence_id: stereo-comparison
  kind: validation
  reference: Scratch RDKit atom-preserving D-to-E comparison
  locator: 183-stereo-comparison.json; source-number C10 mapped to retained atom 22
  accessed_at: '2026-10-21T10:26:02Z'
  support: supports
  summary: Remove D hydroxyl O32, convert C30-C31 to exomethylene, clear now-sp 2
    C30 stereo and retain all other chirality tags. The resulting graph gives the
    exact native E InChIKey; C10 changes CIP S to R without inversion. This resolves
    the descriptor difference as ligand-priority change, not a native stereochemical
    error. It is a graph comparison, not synthesis or independent proof of absolute
    orientation.
  snapshot_sha256: d8caf9de4f37ce4ef35d1b3564f98658dc009a3cf93399c68387f0070107b317
assessments:
- assessment_id: identity
  area: identity
  topic: Exact E graph versus proposed full orientation
  outcome: supported
  summary: Native E is internally consistent and matches the published proposed relative
    drawing and current authorities. Source C10S versus native C10R is explained by
    the changed ligand priorities upon exomethylene formation, with no inversion.
    Absolute experimental support for the ring orientation remains limited.
  target_ids:
  - CHEBI:65561
  evidence_ids:
  - native
  - chebi
  - chemistry
  - chemspider
  - primary
  - figure
  - stereo-comparison
- assessment_id: grounding
  area: grounding
  topic: Parents and filing/role preservation
  outcome: unknown
  summary: Five chemical parents match the graph and filing follows configured role
    priority. The antimalarial role has an exact measured endpoint; source antibacterial
    classification remains unresolved by the inspected above-limit bacterial panel.
    This bounded negative result is not sufficient to delete a role or exclude the
    record.
  target_ids:
  - CHEBI:65561
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
  - CHEBI:65561
  evidence_ids:
  - chemspider
  - reaxys
- assessment_id: definition
  area: evidence
  topic: Structural proposal, historical producer and stated activities
  outcome: unknown
  summary: Structural identity agrees with the published E proposal. Exact positive
    antibacterial and cancer claims were not independently established by the inspected
    original panel, while malaria 96.2 µM and Candida 110 µM are measured. Producer
    attribution remains historical and qualified by later species uncertainty; no
    required native correction is established.
  target_ids:
  - CHEBI:65561
  evidence_ids:
  - primary
  - methods
  - figure
  - chemistry
  - stereo-comparison
  - taxon-2012
- assessment_id: activity
  area: evidence
  topic: Original compound 5 assay limits
  outcome: unknown
  summary: Preserve MIC >500 µM S. aureus and >100 µM E. faecium, cancer mean IC50
    >25 µM and malaria IC50 96.2 µM as distinct observations. These upper-range testing
    limits neither verify positive antibacterial/cancer activity nor establish universal
    inactivity. Candida MIC 110 µM is a separate fungal observation.
  target_ids:
  - CHEBI:65561
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
  - CHEBI:65561
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
  - CHEBI:65561
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
  - CHEBI:65561
  evidence_ids:
  - native
- assessment_id: completeness
  area: completeness
  topic: Optional activity enrichment
  outcome: supported
  summary: Bounded exact observations and proposed-stereochemistry context can support
    optional enrichment. Any positive antibacterial/cancer qualification or fully
    resolved absolute assignment needs exact E evidence; missing optional blocks are
    not defects.
  target_ids:
  - CHEBI:65561
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
  - CHEBI:65561
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
  - CHEBI:65561
  evidence_ids:
  - primary
  - taxon-2009
  - taxon-2012
  - taxon-2017
- assessment_id: stereo-evidence
  area: evidence
  topic: Proposed ring orientation
  outcome: unknown
  summary: Original E NOEs did not determine how its cyclohexane ring is oriented
    relative to the tricycle. Authors proposed the orientation by C/D analogy; current
    authority reproduces that exact proposal. A later direct assignment was not verified
    in the bounded search, so the graph is not described as independently proven.
  target_ids:
  - CHEBI:65561
  evidence_ids:
  - primary
  - figure
  - stereo-comparison
  - search
findings: []
actions:
- action_id: A1
  description: Optionally enrich E-specific assay limits and structure-evidence qualification;
    seek exact positive antibacterial/cancer or independent full stereochemical evidence.
  finding_ids: []
  target_ids:
  - CHEBI:65561
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/callophycoic-acid-e.yaml
    role: Future curator-owned activity observations through validated writer
  acceptance_checks:
  - Use original compound 5/Table 3 values and inequality signs, including malaria
    96.2 µM and Candida 110 µM.
  - Resolve original bacterial identifiers/methods before structured MIC adoption;
    do not label >500/>100 µM as proven universal inactivity.
  - Do not transfer positive C/D/G assays to E or delete eligibility solely from above-range
    endpoints.
  - Preserve proposed ring orientation; compare atom-mapped graphs before interpreting
    source 10S versus modern CIP 10R as inversion.
- action_id: A2
  description: Resolve the original algal voucher before changing or newly grounding
    the producer species.
  finding_ids: []
  target_ids:
  - CHEBI:65561
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
- Reaxys 11167775 returned HTTP 403; its independent molecular identity remains unverified.
- The paper delegates bacterial methods to reference 3; the inspected reference 3
  main text did not supply a complete bacterial protocol. Paper-stated strain identifiers
  have not been independently reconciled, so exact structured MIC adoption requires
  follow-up.
- The original algal voucher was not independently reconciled with later C. densus
  assignments; the inspected 2009 source still used C. serratus and 2017 qualified
  the alternative species. This limits current producer grounding without establishing
  a required native correction.
- E ring orientation relative to the tricycle was proposed by analogy, not determined
  from its NOEs. Exact positive antibacterial/cancer endpoints and a later independent
  full absolute assignment were not verified; the measured assay limits do not settle
  all possible activity.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Initial 13 source hashes remain unchanged; the D comparator was additionally captured
  before graph comparison. All 14 captured hashes rechecked. No native/source/status/history
  edits.
- The scratch D-to-E operation preserves chirality tags and gives the native E key;
  this is a molecular-graph consistency inference only.
- Source-name conflict is qualified, and no optional-empty-field, alias-only or above-limit-inactivity
  finding was created.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:65561
- https://doi.org/10.1021/jo071210y
tags:
- callophycoic-acid-e
- marine-natural-product
- stereochemistry
- assay-scope
```
