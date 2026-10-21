# Callophycoic acid F: exact unsaturated acid and activity limits

- Review: 20261021T104043Z-callophycoic-acid-f
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:21:05Z
- Finished UTC: 2026-10-21T10:40:43Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

No confirmed native defect. The exact nonhalogenated bicyclic acid has two specified E side-chain olefins and no tetrahedral stereocentres, consistent with original compound 6 and live identity sources. The original malaria IC50 is 27.0 µM; bacterial and cancer observations are above the tested limits, leaving positive claims unresolved. Historical algal naming, inaccessible Reaxys and delegated assay methods remain qualified. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole-record review of exact callophycoic acid F.

Selection: Queue 184 in isolated batch 019; root initial capture preserved.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65562 | data/antibiotics/antibacterial/callophycoic-acid-f.yaml | generated | callophycoic acid F |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | CHEBI:65562 | Actual focused command passed. |
| Focused strict | passed | True | CHEBI:65562 | Actual focused command passed. |
| Independent molecular encodings and source mint | passed | True | CHEBI:65562 | Both encodings, both specified E olefins, formula/charge/masses and source mint agree; no tetrahedral centres exist. |
| Authoritative full QC | failed | True | CHEBI:65562 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65562 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65562 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65562 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65562 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65562 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65562 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65562 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65562 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact F skeleton and two olefin geometries

identity: supported. Targets: CHEBI:65562.

Native neutral nonhalogenated acid matches compound 6 connectivity and two E side-chain configurations. The structure has no tetrahedral centres; absence of chiral tags is therefore appropriate. The source distinguishes directly established Δ10,11 geometry from the analogous proposed Δ14,15 assignment.

### Parents and filing/role preservation

grounding: unknown. Targets: CHEBI:65562.

Four chemical parents match the graph and filing follows configured role priority. Malaria has an exact measured endpoint. Source antibacterial classification remains unresolved by the above-limit bacterial panel, which is insufficient by itself to delete eligibility.

### Exact cross-reference verification

grounding: unknown. Targets: CHEBI:65562.

ChemSpider exact identity is verified; Reaxys is inaccessible independently, with no positive mismatch found.

### F connectivity, historical producer and activity claims

evidence: unknown. Targets: CHEBI:65562.

Structural description matches source compound 6 and current molecular encodings. Malaria IC50 27.0 µM is measured, while exact positive antibacterial/cancer claims are not independently established by the inspected above-limit panel. The original algal attribution remains qualified by later species uncertainty; no confirmed correction is established.

### Original compound 6 endpoints and limits

evidence: unknown. Targets: CHEBI:65562.

Keep S. aureus MIC &gt;600 µM, E. faecium &gt;100 µM, cancer mean IC50 &gt;25 µM and malaria IC50 27.0 µM distinct. Candida MIC &gt;200 µM is also a bounded limit. The 2009 ecological study explicitly did not test F, so family antifungal observations cannot supply an F endpoint.

### No verified exact molecular mechanism

evidence: unknown. Targets: CHEBI:65562.

The paper proposes biosynthesis and reports activity but does not establish an exact microbial target. No antibacterial or antimalarial mode is inferred from the chemical family.

### Generated audit and maintained owners

provenance: supported. Targets: CHEBI:65562.

Exact source concept, mint and three seed events are coherent. No native curation or status promotion occurred.

### Unpopulated domains and structured adapters

scope: not_applicable. Targets: CHEBI:65562.

No populated resistance, clinical, producer, dataset or graph blocks, and no native named gene/protein/regulator/pathway requires an iModulonDB query. Definition isolation is assessed directly.

### Optional activity enrichment

completeness: supported. Targets: CHEBI:65562.

Optional exact assay enrichment can record measured malaria activity and comparator limits after method/strain verification. No empty optional block is a defect, and a proposed biosynthetic precursor relationship is not a microbial mechanism.

### Focused deterministic checks

schema: supported. Targets: CHEBI:65562.

Focused schema/strict and independent encoding/mint checks pass; scientific review retains the external-source limits.

### Historical source species versus later reassignment

evidence: unknown. Targets: CHEBI:65562.

Original 2007 C. serratus isolation is accurately represented as a historical attribution, but later primary literature uses C. densus and retains uncertainty. Exact original-voucher reassignment remains unresolved; this is not a confirmed native wrong-taxon finding.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optionally enrich exact F assay observations and seek exact positive antibacterial/cancer evidence without importing related compounds.

- Use original compound 6/Table 3 in µM, including malaria IC50 27.0 µM and the precise &gt;600/&gt;100/&gt;25 limits.
- Resolve source-stated bacterial identifiers and delegated assay methods before structured MIC adoption.
- Do not infer universal inactivity or automatic eligibility removal from above-range results.
- Keep bromophycoic acid F, iodinated analogues and other callophycoic acids separate; the 2009 ecological study did not test F.
- Retain the original distinction between E geometry established at Δ10,11 and proposed at Δ14,15.

### A2

Resolve the original algal voucher before changing or newly grounding the producer species.

- Preserve the 2007 C. serratus attribution while documenting the later C. densus interpretation.
- Establish exact voucher/collection correspondence before a species substitution; do not transfer G-0807 identity from the 2012 study.
- Keep pure-compound antifungal results separate from mixture/fraction experiments and preserve each congener-specific endpoint.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/callophycoic-acid-f.yaml; Entire YAML | supports | Read complete CHEBI:65562 record: exact F identity and 3E/7E side-chain definition, C. serratus isolation/activity claims, four chemical parents, two roles, complete structure, two xrefs, exact source concept and three seed events. Optional mechanism/activity/target/resistance/producer/clinical/graph blocks are unpopulated. |
| owners | data/raw/chebi_antimicrobials.tsv; ChEBI row 1232; role table and source configuration | supports | The adopted ChEBI row owns exact F structure, four parents, two antimicrobial roles, definition and PMID17715978 lead. Maintained extractor/seeder/decisions own generated corrections. Ignored-inclusive exact search found no additional curator annotation; historical discovery ledgers were treated as leads only. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:65562; Complete live page | supports | Live ChEBI agrees on neutral C27H36O3, nonhalogenated bicyclic acid, two specified E side-chain bonds, no tetrahedral centres, four chemical parents and both source antimicrobial roles. Extra non-antimicrobial roles on the live page are outside the adopted antimicrobial-role scope. |
| chemistry | Independent RDKit encodings and CHEBI mint; Both encodings, all molecular quantities and source mint | supports | Native SMILES and InChI both yield URXNJUNXUWLMAY-KZVLYIKRSA-N, neutral C27H36O3, one fragment, matching masses and no tetrahedral stereocentres. Source mint matches. Independent bond inspection gives E at SMILES bonds 6–8 and 11–13; these correspond to systematic side-chain 7E and 3E/sourceΔ14,15 andΔ10,11, respectively. |
| chemspider | https://www.chemspider.com/Chemical-Structure.23076458.html; Current page and embedded standard identifiers | supports | ChemSpider 23076458 embedded standard InChI and InChIKey match native F exactly, including the two specified double-bond configurations and formula. This is identity support, not independent activity evidence. |
| reaxys | https://www.reaxys.com/reaxys/secured/compound.do?substanceId=11167776; Official destination request; current ChEBI retained registry link | unknown | Reaxys 11167776 is source-asserted but independently inaccessible with HTTP 403. This is an unresolved verification limit, not evidence of a mismatch. |
| primary | https://doi.org/10.1021/jo071210y; PMID17715978 / PMC3374858; compound 6 Results, Table 3 row 6 and Experimental Section | partial | Original compound 6 F is nonhalogenated C27H36O3 with an unsaturated seven-member ether ring (Δ6,7) and a linear prenyl side-chain. MS/NMR/COSY/HMBC establish connectivity; NOEs establish E at Δ10,11 and support a proposed E at Δ14,15. Table 3 gives S. aureus MIC &gt;600 µM, E. faecium &gt;100 µM, tuberculosis &gt;100 µM, cancer mean IC50 &gt;25 µM, malaria IC50 27.0 µM and Candida MIC &gt;200 µM. These limits do not prove universal inactivity. |
| figure | https://pmc.ncbi.nlm.nih.gov/articles/PMC3374858/; Original numbered compound 6 drawing, visually inspected; compare different A–E topologies | supports | Compound 6 drawing matches F’s bicyclic ether/benzoic acid skeleton and extended prenyl chain, with the two specified E geometries. It has no tetrahedral configurations to assign. The A crystal and other congener rings provide no independent F crystallographic evidence. |
| methods | https://doi.org/10.1021/jo071210y; Experimental Section Pharmacological Assays | partial | Paper names S. aureusATCC 10537 and E. faeciumATCC 12952, with bacterial procedure delegated to reference 3. Malaria assay uses 3D7, human O+ erythrocytes,2.5% hematocrit/0.5% parasitemia and 72 h incubation. The ≥90% growth-inhibition MIC definition is in the antitubercular methods paragraph and should not automatically be transferred to the bacterial assay. No direct target is measured. |
| search | Ignored-inclusive repository and public literature search; Exact F ID/label/key, original compound 6 and public exact-name search | context_only | Ignored-inclusive search found raw/native/generated references and historical research ledgers, without an additional exact curated annotation. EPMC exact-name results included original 2007 and unrelated caffeic/cimicifugic-acid hits; inspected later Callophycus papers distinguish other chemical classes. No verified later exact F positive antibacterial/cancer assay or molecular mechanism was established. |
| gates | just validate; just validate-strict; Actual focused batch 019 commands | supports | Both focused gates exit 0; one strict target with no errors. Internal molecular consistency also passes. |
| taxon-2009 | https://doi.org/10.1073/pnas.0812020106; PMC2678663; Results on chemotypes and identification; Figure 1 caption | partial | The 2009 study retained C. serratus for both chemotypes: morphology identified all samples as that species, while 18S sequences separated two clades matching chemistry. It does not provide a C. densus reassignment. Pure C/G/H had marine fungal activity below 300 µM; E/F were explicitly neither detected nor tested. Fraction antibacterial negatives do not establish pure-compound inactivity. |
| taxon-2012 | https://doi.org/10.1021/jo301246x; PMC3474338; Results opening morphology/genetics passages and comparison to original 2007 paper | partial | The 2012 primary paper retrospectively associates nonmacrocyclic callophycoic acids/callophycols with C. densus and macrocyclic bromophycolides with C. serratus. It describes morphological differences and cites the 2009 genetic study; the inspected text does not resolve the precise 2007 voucher. Its new G-0807 collection belongs to another Callophycus species and must not be mapped to these compounds. |
| taxon-2017 | https://doi.org/10.1021/acs.joc.7b00096; PMC5538829; proposed biosynthesis discussion around Figure 7 | partial | The 2017 paper calls the earlier source of callophycoic H and callophycols another Callophycus member, likely C. densus. Its absolute-configuration revisions concern bromophycoic structures; neither those revisions nor its new iodinated compounds are transferred to this exact callophycoic acid. |
| bond-stereo | Independent RDKit double-bond inspection; 184-bond-stereo.json; native zero-based SMILES atom indices | supports | Two eligible side-chain olefins encode E geometry. The terminal dimethyl olefin lacks E/Z isomerism, and the small endocyclic double bond has no separate SMILES stereo tag. No missing tetrahedral assignment is inferred. |

## Limits And Additional Notes

- Reaxys 11167776 returned HTTP 403; its independent molecular identity remains unverified.
- The paper delegates bacterial methods to reference 3; the inspected reference 3 main text did not supply a complete bacterial protocol. Paper-stated strain identifiers have not been independently reconciled, so exact structured MIC adoption requires follow-up.
- The original algal voucher was not independently reconciled with later C. densus assignments; the inspected 2009 source still used C. serratus and 2017 qualified the alternative species. This limits current producer grounding without establishing a required native correction.
- No later verified exact F positive antibacterial/cancer result or microbial molecular mechanism was established in the bounded primary search. Above-range original endpoints leave those domains unresolved; F was not tested in the 2009 ecological study.
- Full supplementary raw correlations were not independently reprocessed; the original paper describes one side-chain E assignment as proposed on analogous NOE arguments.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 13 initial hashes rechecked unchanged; no native/source/status/history edits.
- The original probable biosynthetic precursor relationship for F is separate from its pharmacological mode of action.
- No optional-empty-field, alias-only or above-limit-inactivity finding was created.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T104043Z-callophycoic-acid-f
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Callophycoic acid F: exact unsaturated acid and activity limits'
started_at: '2026-10-21T10:21:05Z'
finished_at: '2026-10-21T10:40:43Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independent full F native/raw-owner review, both molecular encodings
    and live identities, original compound 6 structure/NOE evidence, exact Table 3
    row and later source-taxonomy boundaries.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: No confirmed native defect. The exact nonhalogenated bicyclic acid has two
  specified E side-chain olefins and no tetrahedral stereocentres, consistent with
  original compound 6 and live identity sources. The original malaria IC50 is 27.0
  µM; bacterial and cancer observations are above the tested limits, leaving positive
  claims unresolved. Historical algal naming, inaccessible Reaxys and delegated assay
  methods remain qualified. Scientific assessment retains the stated evidence limits;
  full verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/callophycoic-acid-f.yaml
    sha256: 79df2557b2612db41d475ef98485580a660c39b7edbef7f74e0a7f3b89f7a277
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
- target_id: CHEBI:65562
  path: data/antibiotics/antibacterial/callophycoic-acid-f.yaml
  label: callophycoic acid F
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
  description: Whole-record review of exact callophycoic acid F.
  selection: Queue 184 in isolated batch 019; root initial capture preserved.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65562
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
  - CHEBI:65562
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/callophycoic-acid-f.yaml
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
  - CHEBI:65562
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/callophycoic-acid-f.yaml --out /private/tmp/am-review-session/184-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Independent molecular encodings and source mint
  status: passed
  required: true
  summary: Both encodings, both specified E olefins, formula/charge/masses and source
    mint agree; no tetrahedral centres exist.
  target_ids:
  - CHEBI:65562
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
  - CHEBI:65562
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
  - CHEBI:65562
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
  - CHEBI:65562
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
  - CHEBI:65562
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
  - CHEBI:65562
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
  - CHEBI:65562
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
  - CHEBI:65562
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
  - CHEBI:65562
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
  - CHEBI:65562
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/callophycoic-acid-f.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T10:33:00Z'
  support: supports
  summary: 'Read complete CHEBI:65562 record: exact F identity and 3E/7E side-chain
    definition, C. serratus isolation/activity claims, four chemical parents, two
    roles, complete structure, two xrefs, exact source concept and three seed events.
    Optional mechanism/activity/target/resistance/producer/clinical/graph blocks are
    unpopulated.'
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: ChEBI row 1232; role table and source configuration
  accessed_at: '2026-10-21T10:33:00Z'
  support: supports
  summary: The adopted ChEBI row owns exact F structure, four parents, two antimicrobial
    roles, definition and PMID17715978 lead. Maintained extractor/seeder/decisions
    own generated corrections. Ignored-inclusive exact search found no additional
    curator annotation; historical discovery ledgers were treated as leads only.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:65562
  locator: Complete live page
  accessed_at: '2026-10-21T10:31:36Z'
  support: supports
  summary: Live ChEBI agrees on neutral C27H36O3, nonhalogenated bicyclic acid, two
    specified E side-chain bonds, no tetrahedral centres, four chemical parents and
    both source antimicrobial roles. Extra non-antimicrobial roles on the live page
    are outside the adopted antimicrobial-role scope.
  snapshot_sha256: 88c8e71ced978e54e79cd496a5f256dae315423fc336b16437815afd01c2ccc0
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit encodings and CHEBI mint
  locator: Both encodings, all molecular quantities and source mint
  accessed_at: '2026-10-21T10:31:27Z'
  support: supports
  summary: Native SMILES and InChI both yield URXNJUNXUWLMAY-KZVLYIKRSA-N, neutral
    C27H36O3, one fragment, matching masses and no tetrahedral stereocentres. Source
    mint matches. Independent bond inspection gives E at SMILES bonds 6–8 and 11–13;
    these correspond to systematic side-chain 7E and 3E/sourceΔ14,15 andΔ10,11, respectively.
  snapshot_sha256: b9cf67c0412553387d0a65be9e1384e833b9e9720f3fa3fa403a581a02e47606
- evidence_id: chemspider
  kind: database
  reference: https://www.chemspider.com/Chemical-Structure.23076458.html
  locator: Current page and embedded standard identifiers
  accessed_at: '2026-10-21T10:31:35Z'
  support: supports
  summary: ChemSpider 23076458 embedded standard InChI and InChIKey match native F
    exactly, including the two specified double-bond configurations and formula. This
    is identity support, not independent activity evidence.
  snapshot_sha256: 17e8cf0b1ac2a9809a66eaeb310c122be7a6a0e32913b4d52fbd89944a249d7e
- evidence_id: reaxys
  kind: database
  reference: https://www.reaxys.com/reaxys/secured/compound.do?substanceId=11167776
  locator: Official destination request; current ChEBI retained registry link
  accessed_at: '2026-10-21T10:31:36Z'
  support: unknown
  summary: Reaxys 11167776 is source-asserted but independently inaccessible with
    HTTP 403. This is an unresolved verification limit, not evidence of a mismatch.
  snapshot_sha256: 437eaacdc080eae07c21b0e0249cf816e700a9a13e59ca4a707c52bcc8566d8f
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1021/jo071210y
  locator: PMID17715978 / PMC3374858; compound 6 Results, Table 3 row 6 and Experimental
    Section
  accessed_at: '2026-10-21T10:17:41Z'
  support: partial
  summary: Original compound 6 F is nonhalogenated C27H36O3 with an unsaturated seven-member
    ether ring (Δ6,7) and a linear prenyl side-chain. MS/NMR/COSY/HMBC establish connectivity;
    NOEs establish E at Δ10,11 and support a proposed E at Δ14,15. Table 3 gives S.
    aureus MIC >600 µM, E. faecium >100 µM, tuberculosis >100 µM, cancer mean IC50
    >25 µM, malaria IC50 27.0 µM and Candida MIC >200 µM. These limits do not prove
    universal inactivity.
  snapshot_sha256: bcf3f54e5acf5cb0bb6c5d42bf9e5b9d99fee62da8b6fe2768f0859545f956fd
- evidence_id: figure
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3374858/
  locator: Original numbered compound 6 drawing, visually inspected; compare different
    A–E topologies
  accessed_at: '2026-10-21T10:33:00Z'
  support: supports
  summary: Compound 6 drawing matches F’s bicyclic ether/benzoic acid skeleton and
    extended prenyl chain, with the two specified E geometries. It has no tetrahedral
    configurations to assign. The A crystal and other congener rings provide no independent
    F crystallographic evidence.
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
  locator: Exact F ID/label/key, original compound 6 and public exact-name search
  accessed_at: '2026-10-21T10:31:25Z'
  support: context_only
  summary: Ignored-inclusive search found raw/native/generated references and historical
    research ledgers, without an additional exact curated annotation. EPMC exact-name
    results included original 2007 and unrelated caffeic/cimicifugic-acid hits; inspected
    later Callophycus papers distinguish other chemical classes. No verified later
    exact F positive antibacterial/cancer assay or molecular mechanism was established.
  search_scope: rg --no-ignore --hidden CHEBI:65562/exactlabel/URXNJUNXUWLMAY outside
    .git/.venv; current ChEBI/ChemSpider/Reaxys; EPMC and web exact-name searches
    through 2026-10-21. Bromophycoic acid F is a different compound.
  snapshot_sha256: 8a3fca85c77abff59e4439d80b91af11578482ed6ac72ee16bc50a0f6aa83719
- evidence_id: gates
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual focused batch 019 commands
  accessed_at: '2026-10-21T10:33:00Z'
  support: supports
  summary: Both focused gates exit 0; one strict target with no errors. Internal molecular
    consistency also passes.
  snapshot_sha256: 4e1c93650616e4ee1b041a4a66b0d5e0387463de9c544411f652e3b0792c42f4
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
- evidence_id: bond-stereo
  kind: validation
  reference: Independent RDKit double-bond inspection
  locator: 184-bond-stereo.json; native zero-based SMILES atom indices
  accessed_at: '2026-10-21T10:32:10Z'
  support: supports
  summary: Two eligible side-chain olefins encode E geometry. The terminal dimethyl
    olefin lacks E/Z isomerism, and the small endocyclic double bond has no separate
    SMILES stereo tag. No missing tetrahedral assignment is inferred.
  snapshot_sha256: 1d3e701045c550230289b31d922fe8480912599a153d9061e649cd0a8f94e1ea
assessments:
- assessment_id: identity
  area: identity
  topic: Exact F skeleton and two olefin geometries
  outcome: supported
  summary: Native neutral nonhalogenated acid matches compound 6 connectivity and
    two E side-chain configurations. The structure has no tetrahedral centres; absence
    of chiral tags is therefore appropriate. The source distinguishes directly established
    Δ10,11 geometry from the analogous proposed Δ14,15 assignment.
  target_ids:
  - CHEBI:65562
  evidence_ids:
  - native
  - chebi
  - chemistry
  - chemspider
  - primary
  - figure
  - bond-stereo
- assessment_id: grounding
  area: grounding
  topic: Parents and filing/role preservation
  outcome: unknown
  summary: Four chemical parents match the graph and filing follows configured role
    priority. Malaria has an exact measured endpoint. Source antibacterial classification
    remains unresolved by the above-limit bacterial panel, which is insufficient by
    itself to delete eligibility.
  target_ids:
  - CHEBI:65562
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
  - CHEBI:65562
  evidence_ids:
  - chemspider
  - reaxys
- assessment_id: definition
  area: evidence
  topic: F connectivity, historical producer and activity claims
  outcome: unknown
  summary: Structural description matches source compound 6 and current molecular
    encodings. Malaria IC50 27.0 µM is measured, while exact positive antibacterial/cancer
    claims are not independently established by the inspected above-limit panel. The
    original algal attribution remains qualified by later species uncertainty; no
    confirmed correction is established.
  target_ids:
  - CHEBI:65562
  evidence_ids:
  - primary
  - methods
  - figure
  - chemistry
  - bond-stereo
  - taxon-2012
- assessment_id: activity
  area: evidence
  topic: Original compound 6 endpoints and limits
  outcome: unknown
  summary: Keep S. aureus MIC >600 µM, E. faecium >100 µM, cancer mean IC50 >25 µM
    and malaria IC50 27.0 µM distinct. Candida MIC >200 µM is also a bounded limit.
    The 2009 ecological study explicitly did not test F, so family antifungal observations
    cannot supply an F endpoint.
  target_ids:
  - CHEBI:65562
  evidence_ids:
  - primary
  - methods
  - taxon-2009
- assessment_id: mechanism
  area: evidence
  topic: No verified exact molecular mechanism
  outcome: unknown
  summary: The paper proposes biosynthesis and reports activity but does not establish
    an exact microbial target. No antibacterial or antimalarial mode is inferred from
    the chemical family.
  target_ids:
  - CHEBI:65562
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
  - CHEBI:65562
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
  - CHEBI:65562
  evidence_ids:
  - native
- assessment_id: completeness
  area: completeness
  topic: Optional activity enrichment
  outcome: supported
  summary: Optional exact assay enrichment can record measured malaria activity and
    comparator limits after method/strain verification. No empty optional block is
    a defect, and a proposed biosynthetic precursor relationship is not a microbial
    mechanism.
  target_ids:
  - CHEBI:65562
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
  - CHEBI:65562
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
  - CHEBI:65562
  evidence_ids:
  - primary
  - taxon-2009
  - taxon-2012
  - taxon-2017
findings: []
actions:
- action_id: A1
  description: Optionally enrich exact F assay observations and seek exact positive
    antibacterial/cancer evidence without importing related compounds.
  finding_ids: []
  target_ids:
  - CHEBI:65562
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/callophycoic-acid-f.yaml
    role: Future curator-owned activity observations through validated writer
  acceptance_checks:
  - Use original compound 6/Table 3 in µM, including malaria IC50 27.0 µM and the
    precise >600/>100/>25 limits.
  - Resolve source-stated bacterial identifiers and delegated assay methods before
    structured MIC adoption.
  - Do not infer universal inactivity or automatic eligibility removal from above-range
    results.
  - Keep bromophycoic acid F, iodinated analogues and other callophycoic acids separate;
    the 2009 ecological study did not test F.
  - Retain the original distinction between E geometry established at Δ10,11 and proposed
    at Δ14,15.
- action_id: A2
  description: Resolve the original algal voucher before changing or newly grounding
    the producer species.
  finding_ids: []
  target_ids:
  - CHEBI:65562
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
- Reaxys 11167776 returned HTTP 403; its independent molecular identity remains unverified.
- The paper delegates bacterial methods to reference 3; the inspected reference 3
  main text did not supply a complete bacterial protocol. Paper-stated strain identifiers
  have not been independently reconciled, so exact structured MIC adoption requires
  follow-up.
- The original algal voucher was not independently reconciled with later C. densus
  assignments; the inspected 2009 source still used C. serratus and 2017 qualified
  the alternative species. This limits current producer grounding without establishing
  a required native correction.
- No later verified exact F positive antibacterial/cancer result or microbial molecular
  mechanism was established in the bounded primary search. Above-range original endpoints
  leave those domains unresolved; F was not tested in the 2009 ecological study.
- Full supplementary raw correlations were not independently reprocessed; the original
  paper describes one side-chain E assignment as proposed on analogous NOE arguments.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 13 initial hashes rechecked unchanged; no native/source/status/history edits.
- The original probable biosynthetic precursor relationship for F is separate from
  its pharmacological mode of action.
- No optional-empty-field, alias-only or above-limit-inactivity finding was created.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:65562
- https://doi.org/10.1021/jo071210y
tags:
- callophycoic-acid-f
- marine-natural-product
- olefin-geometry
- assay-scope
```
