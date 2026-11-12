# Bromophycolide A: exact identity and preparation-scoped activity review

- Review: 20261021T103157Z-bromophycolide-a
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:11:06Z
- Finished UTC: 2026-10-21T10:31:57Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Identity, five-centre structure, parents and four antimicrobial roles are supported. One minor inherited spelling error remains in the apoptosis definition. Primary exact-compound activity and malaria-specific heme evidence are scoped separately; Reaxys identity and original supplementary assay detail remain unverified. Focused gates pass.

## Scope And Provenance

Whole-record review of bromophycolide A.

Selection: Queue173 in isolated batch018; root initial capture preserved.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65525 | data/antibiotics/antibacterial/bromophycolide-a.yaml | generated | bromophycolide A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | CHEBI:65525 | Actual focused command passed. |
| Focused strict | passed | True | CHEBI:65525 | Actual focused command passed. |
| Independent molecular encoding and mint check | passed | True | CHEBI:65525 | Both encodings, five configurations, formula/charge/masses and CHEBI mint agree. |
| Authoritative full QC | failed | True | CHEBI:65525 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65525 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65525 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65525 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65525 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65525 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65525 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65525 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65525 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### One exact natural macrolide

identity: supported. Targets: CHEBI:65525.

Native exact grounding and structure agree with current ChEBI/ChemSpider, independent encodings and primary isolation/X-ray framework.

### Broader chemical classes and antimicrobial filing

grounding: supported. Targets: CHEBI:65525.

All five parents are strictly broader compatible classes. Four supported antimicrobial roles are preserved, and ANTIBACTERIAL follows configured class priority.

### Exact external identity

grounding: unknown. Targets: CHEBI:65525.

ChemSpider is exact; Reaxys is source-asserted but independently inaccessible. No defect is inferred from403.

### Isolation, cell phenotype and roles

evidence: concern. Targets: CHEBI:65525.

The substantive definition is supported by primary isolation, activity and cancer-cell assays. The inherited word apotopic is a transcription error for apoptotic. Cancer apoptosis is not generalized to bacterial killing.

### Compound-specific measured endpoints

evidence: supported. Targets: CHEBI:65525.

Original exact-compound MIC and fungal/HIV IC50 values support roles. Malaria assays support that additional role. Strain scope, endpoint and units must be retained; extract tables and derivative assays remain separate.

### Checked malaria mechanism, unresolved bacterial mode

evidence: unknown. Targets: CHEBI:65525.

Primary heme experiments provide a useful antimalarial mechanism candidate, but no bacterial molecular mechanism was established in this inspected set. Blank optional mechanism/target fields are not a defect.

### Unpopulated optional domains and structured adapter

scope: not_applicable. Targets: CHEBI:65525.

No native named protein/gene/locus/regulator/pathway or transcriptomics dataset triggers a relevant iModulonDB query. Resistance, clinical, producer, datasets and graphs have no populated native blocks; source isolation is evaluated in the definition.

### Seed ownership and audit

provenance: supported. Targets: CHEBI:65525.

Mint, exact source concept and three seed events are coherent. Captured bytes are unchanged; native remains SEEDED.

### Bounded future enrichment

completeness: supported. Targets: CHEBI:65525.

Activity and malaria-specific heme evidence are useful optional curation candidates. No requirement to populate every optional field or infer protein targets follows from these sources.

### Deterministic validation

schema: supported. Targets: CHEBI:65525.

Focused schema/strict and internal chemical checks pass. Shared corpus checks are coordinated separately.

## Findings

### F1: Correct the inherited cell-death terminology

minor / open / confirmed; issue key: bromophycolide-a-definition-apotopic-typo.

The generated definition says apotopic cell death. The cited primary paper describes apoptotic cell death and measures apoptosis in A2780 human ovarian cells. Correct the spelling through the maintained source path without implying a bacterial apoptosis mechanism.

## Recommended Actions And Acceptance Checks

### A1

Correct apotopic to apoptotic through the maintained ChEBI harmonization path.

- Retain the human tumour-cell scope and primary source meaning.
- Regenerate the record and confirm source reproducibility, schema/strict and history checks.

### A2

Optionally curate exact activity and malaria-specific heme evidence after preparation and method review.

- Read original supplementary assay details before extracting complete MIC observations; do not copy extract or analogue rows.
- Keep malaria heme association/crystallization evidence distinct from unverified bacterial mode and from derivative15 localization.
- Do not force a protein target or extrapolate failed pull-down to absence of targets; retain assay solvent/model conditions.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/bromophycolide-a.yaml; Entire YAML | supports | Read exact CHEBI65525 identity, definition, five parents, four antimicrobial roles, complete molecular fields, two xrefs, source concept and three seed events. No populated mechanism, target, resistance, activity, producer, clinical or graph blocks. |
| owners | data/raw/chebi_antimicrobials.tsv; Row1212; role names and source priority config | supports | The complete ChEBI row owns identity, five-centre structure, definition typo, roles and citation leads PMID16268553/21309525/22214291. Extractor/seeder and decisions control future generated corrections; no curator addition was found by ignored-inclusive search. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:65525; Live complete compound page | supports | Current ChEBI reproduces native molecular fields and all parent/role CURIEs: diterpenoid, macrolide, organobromine, phenol and tertiary alcohol; antibacterial, antifungal, antimalarial and anti-HIV roles. It associates isolation with Callophycus serratus and PMID16268553. The same apotopic typo remains upstream. |
| chemistry | Independent RDKit encoding and mint checks; Complete native chemical_structure and source_concepts | supports | Both encodings yield SKIHYPQTROYIIT-VHXXJFIISA-N, neutral C27H37Br3O4, one fragment, consistent masses, five assigned tetrahedral centres and no unassigned centres. CHEBI mint matches. |
| chemspider | https://www.chemspider.com/Chemical-Structure.10480986.html; Visible compound page and embedded standard InChI/key | supports | The exact ChemSpider xref resolves to the same Standard InChI and key, formula, masses and five defined stereocentres. Nonstandard identifier variants in page data were not substituted for its explicit standard key. |
| reaxys | https://www.reaxys.com/reaxys/secured/compound.do?substanceId=10220528; Current official endpoint attempt and ChEBI manual registry link | unknown | Reaxys10220528 is retained on current ChEBI, but the destination returned403. Exact independent Reaxys structure verification remains unavailable; no mismatch is inferred. |
| isolation | https://doi.org/10.1021/ol052121f; PMID16268553 / PMC3374863; full main text, Tables2–3 and Figure1 | supports | The original2005 study isolates compound1 from Fijian Callophycus serratus and establishes a tribrominated15-membered macrolide by X-ray/NMR/MS; refined Flack parameter supports absolute configuration. Table2 reports MIC5.9µM for both MRSA and VREF, antifungal IC50 49µM against amphotericin-B-resistant Candida albicans, and HIV-1 IC50 9.8/9.1µM for96USHIPS7/UG92/029. In A2780 cells,24h exposure caused G1 arrest and apoptosis; this cancer phenotype is not an antibacterial mechanism. Methods in inaccessible supplementary PDF were not independently read. |
| figure | https://pmc.ncbi.nlm.nih.gov/articles/PMC3374863/figure/F1/; Original Figure1 compound1; visual inspection | supports | The published drawing distinguishes bromophycolide A from B and debromophycolide A and shows its five specified centres. This visual check supports the native connectivity/stereo framework alongside current authority and encoding checks. |
| synthesis | https://doi.org/10.1021/ol200099n; PMID21309525 / PMC3065244; main text and conclusion | context_only | This2011 route prepares the bromophycolide D ring system and discusses further transformation to A/D; it is not a total synthesis or antibacterial mechanism experiment for pure natural A. It is a relevant structural lead, not assay proof. |
| imaging | https://doi.org/10.1186/1471-2334-12-1; PMID22214291 / PMC3268092; Methods and purified-compound verification | supports | Pure bromophycolide A at IC80 2.8µM was tested in synchronized P.falciparum3D7 cultures, with dosing at0/8/16h and imaging at24h. Cell-cycle arrest, enlarged vacuoles and altered hemozoin were observed. Broad extract antibacterial tables were not transferred to pure A; decreased RNA-probe intensity does not prove direct RNA attack. |
| heme | https://doi.org/10.1002/cmdc.201100252; PMID21732541 / PMC3381860; Tables1–2 and experimental-results paragraphs | supports | Natural A inhibited P.falciparum3D7/Dd2/HB3 at499±51/377±92/493±44nM. Cell-free heme crystallization IC50 was2.5±0.13mol equivalents to heme. Spectroscopy supports heme association (logK4.52±0.18 under a1:1 model,40%DMSO/20mMHEPES,pH7.4); this is not a protein target. Localization used fluorescent derivative15. Failed probe protein pull-down does not prove absence of protein targets. The evidence supports a malaria-specific heme-crystallization mechanism, not the antibacterial mode. |
| search | Ignored-inclusive repository and free public source search; Exact ID/label/key; three adopted PMIDs and primary cited heme work | context_only | Search included ignored and hidden files outside.git/.venv and found the native/raw owners and generated projections; no additional maintained exact-compound annotation was identified. All three adopted leads were resolved and inspected in full main text. Mechanism scope was bounded to the organisms and preparations actually tested. |
| gates | just validate; just validate-strict; Actual focused commands in isolated batch018 | supports | Schema and strict commands exited0; strict scanned one file with zero errors. Molecular consistency also passes. |

## Limits And Additional Notes

- Reaxys returned403; current ChEBI retains the identifier, but independent exact-structure verification was unavailable.
- Original2005 supplementary PDF/CIF routes returned HTML challenge pages, not usable supplements; main text, tables and published structure drawing were inspected. Detailed original assay conditions and independent reprocessing of crystallographic coordinates were not completed.
- No exact bacterial mechanism was established in the inspected primary set; heme-crystallization evidence concerns P.falciparum and does not fill that gap.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 13 captured hashes rechecked unchanged; no native/source/status/history edits.
- No optional-empty-field or alias-only finding. The synthetic-ring-system paper is not a total synthesis or new natural-A bioassay.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T103157Z-bromophycolide-a
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Bromophycolide A: exact identity and preparation-scoped activity review'
started_at: '2026-10-21T10:11:06Z'
finished_at: '2026-10-21T10:31:57Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Whole-record and maintained-source review, independent molecular
    calculation, current authority/xref retrieval and original primary text with visual
    structure inspection.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Identity, five-centre structure, parents and four antimicrobial roles are
  supported. One minor inherited spelling error remains in the apoptosis definition.
  Primary exact-compound activity and malaria-specific heme evidence are scoped separately;
  Reaxys identity and original supplementary assay detail remain unverified. Focused
  gates pass.
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
  - path: data/antibiotics/antibacterial/bromophycolide-a.yaml
    sha256: 605b31fe8092599154925439ee397351313c3f611f2b6f294a7e645980320861
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
- target_id: CHEBI:65525
  path: data/antibiotics/antibacterial/bromophycolide-a.yaml
  label: bromophycolide A
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
  description: Whole-record review of bromophycolide A.
  selection: Queue173 in isolated batch018; root initial capture preserved.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65525
  exclusions:
  - target: Other bromophycolides, synthetic probes and algal extracts
    reason: Only source context; their assays and mechanisms are not transferred to
      exact A.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual focused command passed.
  target_ids:
  - CHEBI:65525
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/bromophycolide-a.yaml
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
  - CHEBI:65525
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/bromophycolide-a.yaml --out /private/tmp/am-review-session/173-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Independent molecular encoding and mint check
  status: passed
  required: true
  summary: Both encodings, five configurations, formula/charge/masses and CHEBI mint
    agree.
  target_ids:
  - CHEBI:65525
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
  - CHEBI:65525
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
  - CHEBI:65525
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
  - CHEBI:65525
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
  - CHEBI:65525
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
  - CHEBI:65525
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
  - CHEBI:65525
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
  - CHEBI:65525
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
  - CHEBI:65525
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
  - CHEBI:65525
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/bromophycolide-a.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T10:17:14Z'
  support: supports
  summary: Read exact CHEBI65525 identity, definition, five parents, four antimicrobial
    roles, complete molecular fields, two xrefs, source concept and three seed events.
    No populated mechanism, target, resistance, activity, producer, clinical or graph
    blocks.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Row1212; role names and source priority config
  accessed_at: '2026-10-21T10:17:14Z'
  support: supports
  summary: The complete ChEBI row owns identity, five-centre structure, definition
    typo, roles and citation leads PMID16268553/21309525/22214291. Extractor/seeder
    and decisions control future generated corrections; no curator addition was found
    by ignored-inclusive search.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:65525
  locator: Live complete compound page
  accessed_at: '2026-10-21T10:15:06Z'
  support: supports
  summary: 'Current ChEBI reproduces native molecular fields and all parent/role CURIEs:
    diterpenoid, macrolide, organobromine, phenol and tertiary alcohol; antibacterial,
    antifungal, antimalarial and anti-HIV roles. It associates isolation with Callophycus
    serratus and PMID16268553. The same apotopic typo remains upstream.'
  snapshot_sha256: c32f7e42e5f2e2711187e4ecfcdce3db45f8f1f296ab20e2aa0c112757e677be
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit encoding and mint checks
  locator: Complete native chemical_structure and source_concepts
  accessed_at: '2026-10-21T10:14:43Z'
  support: supports
  summary: Both encodings yield SKIHYPQTROYIIT-VHXXJFIISA-N, neutral C27H37Br3O4,
    one fragment, consistent masses, five assigned tetrahedral centres and no unassigned
    centres. CHEBI mint matches.
  snapshot_sha256: 3ef583e7d78d3b9f89c70d91d361a6f0330832839b7d101bc4f83033778db189
- evidence_id: chemspider
  kind: database
  reference: https://www.chemspider.com/Chemical-Structure.10480986.html
  locator: Visible compound page and embedded standard InChI/key
  accessed_at: '2026-10-21T10:15:03Z'
  support: supports
  summary: The exact ChemSpider xref resolves to the same Standard InChI and key,
    formula, masses and five defined stereocentres. Nonstandard identifier variants
    in page data were not substituted for its explicit standard key.
  snapshot_sha256: aafe24c2bc980b2733d9088c3f4322c8aa163daf3ed98f997ec74770a0fa8a97
- evidence_id: reaxys
  kind: database
  reference: https://www.reaxys.com/reaxys/secured/compound.do?substanceId=10220528
  locator: Current official endpoint attempt and ChEBI manual registry link
  accessed_at: '2026-10-21T10:15:06Z'
  support: unknown
  summary: Reaxys10220528 is retained on current ChEBI, but the destination returned403.
    Exact independent Reaxys structure verification remains unavailable; no mismatch
    is inferred.
  snapshot_sha256: a0d9070edf7004888e687223928ec7c4659a770ef9be25e2d23c5b686e94250c
- evidence_id: isolation
  kind: primary_source
  reference: https://doi.org/10.1021/ol052121f
  locator: PMID16268553 / PMC3374863; full main text, Tables2–3 and Figure1
  accessed_at: '2026-10-21T10:15:19Z'
  support: supports
  summary: The original2005 study isolates compound1 from Fijian Callophycus serratus
    and establishes a tribrominated15-membered macrolide by X-ray/NMR/MS; refined
    Flack parameter supports absolute configuration. Table2 reports MIC5.9µM for both
    MRSA and VREF, antifungal IC50 49µM against amphotericin-B-resistant Candida albicans,
    and HIV-1 IC50 9.8/9.1µM for96USHIPS7/UG92/029. In A2780 cells,24h exposure caused
    G1 arrest and apoptosis; this cancer phenotype is not an antibacterial mechanism.
    Methods in inaccessible supplementary PDF were not independently read.
  snapshot_sha256: 88136e44e28d38dad6de9590947ce039607850d29692397a05899f9392cc5311
- evidence_id: figure
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3374863/figure/F1/
  locator: Original Figure1 compound1; visual inspection
  accessed_at: '2026-10-21T10:15:52Z'
  support: supports
  summary: The published drawing distinguishes bromophycolide A from B and debromophycolide
    A and shows its five specified centres. This visual check supports the native
    connectivity/stereo framework alongside current authority and encoding checks.
  snapshot_sha256: d2054c054cc72702202644ffb0fa9bbf40dd2f9fc1b2c835f164c86c0a0afe2c
- evidence_id: synthesis
  kind: primary_source
  reference: https://doi.org/10.1021/ol200099n
  locator: PMID21309525 / PMC3065244; main text and conclusion
  accessed_at: '2026-10-21T10:15:19Z'
  support: context_only
  summary: This2011 route prepares the bromophycolide D ring system and discusses
    further transformation to A/D; it is not a total synthesis or antibacterial mechanism
    experiment for pure natural A. It is a relevant structural lead, not assay proof.
  snapshot_sha256: 8ba9e86e799ed2dd6f1e54150b3f7a7e9b5dee44cbe416597a254b7c3bab9b36
- evidence_id: imaging
  kind: primary_source
  reference: https://doi.org/10.1186/1471-2334-12-1
  locator: PMID22214291 / PMC3268092; Methods and purified-compound verification
  accessed_at: '2026-10-21T10:15:19Z'
  support: supports
  summary: Pure bromophycolide A at IC80 2.8µM was tested in synchronized P.falciparum3D7
    cultures, with dosing at0/8/16h and imaging at24h. Cell-cycle arrest, enlarged
    vacuoles and altered hemozoin were observed. Broad extract antibacterial tables
    were not transferred to pure A; decreased RNA-probe intensity does not prove direct
    RNA attack.
  snapshot_sha256: 4f4f2f832a970de6fbb43f32303435f6326ec53b123a69dbfef3a57f5ba151d0
- evidence_id: heme
  kind: primary_source
  reference: https://doi.org/10.1002/cmdc.201100252
  locator: PMID21732541 / PMC3381860; Tables1–2 and experimental-results paragraphs
  accessed_at: '2026-10-21T10:15:43Z'
  support: supports
  summary: Natural A inhibited P.falciparum3D7/Dd2/HB3 at499±51/377±92/493±44nM. Cell-free
    heme crystallization IC50 was2.5±0.13mol equivalents to heme. Spectroscopy supports
    heme association (logK4.52±0.18 under a1:1 model,40%DMSO/20mMHEPES,pH7.4); this
    is not a protein target. Localization used fluorescent derivative15. Failed probe
    protein pull-down does not prove absence of protein targets. The evidence supports
    a malaria-specific heme-crystallization mechanism, not the antibacterial mode.
  snapshot_sha256: 916349b99113bd9c6453262d99a23747e97118296a56d50f45d7423c82645340
- evidence_id: search
  kind: search
  reference: Ignored-inclusive repository and free public source search
  locator: Exact ID/label/key; three adopted PMIDs and primary cited heme work
  accessed_at: '2026-10-21T10:14:40Z'
  support: context_only
  summary: Search included ignored and hidden files outside.git/.venv and found the
    native/raw owners and generated projections; no additional maintained exact-compound
    annotation was identified. All three adopted leads were resolved and inspected
    in full main text. Mechanism scope was bounded to the organisms and preparations
    actually tested.
  search_scope: rg --no-ignore --hidden exact CHEBI65525/bromophycolide-A/InChIKey;
    current ChEBI/ChemSpider and Reaxys attempt; EPMC metadata and PMC full primary
    papers, accessed2026-10-21.
  snapshot_sha256: 45dd46459ffa4dc33accc8d8412dd28ab25032e9aafa3343e3a642649d3b0bf5
- evidence_id: gates
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual focused commands in isolated batch018
  accessed_at: '2026-10-21T10:17:07Z'
  support: supports
  summary: Schema and strict commands exited0; strict scanned one file with zero errors.
    Molecular consistency also passes.
  snapshot_sha256: bf842ea0b16b9e34f9d7e88b9b04eb9b92558a9e4231bd57edd8a4f177ac62a1
assessments:
- assessment_id: identity
  area: identity
  topic: One exact natural macrolide
  outcome: supported
  summary: Native exact grounding and structure agree with current ChEBI/ChemSpider,
    independent encodings and primary isolation/X-ray framework.
  target_ids:
  - CHEBI:65525
  evidence_ids:
  - native
  - chebi
  - chemistry
  - chemspider
  - isolation
  - figure
- assessment_id: parents
  area: grounding
  topic: Broader chemical classes and antimicrobial filing
  outcome: supported
  summary: All five parents are strictly broader compatible classes. Four supported
    antimicrobial roles are preserved, and ANTIBACTERIAL follows configured class
    priority.
  target_ids:
  - CHEBI:65525
  evidence_ids:
  - owners
  - chebi
  - isolation
  - imaging
  - heme
- assessment_id: xrefs
  area: grounding
  topic: Exact external identity
  outcome: unknown
  summary: ChemSpider is exact; Reaxys is source-asserted but independently inaccessible.
    No defect is inferred from403.
  target_ids:
  - CHEBI:65525
  evidence_ids:
  - chemspider
  - reaxys
- assessment_id: definition
  area: evidence
  topic: Isolation, cell phenotype and roles
  outcome: concern
  summary: The substantive definition is supported by primary isolation, activity
    and cancer-cell assays. The inherited word apotopic is a transcription error for
    apoptotic. Cancer apoptosis is not generalized to bacterial killing.
  target_ids:
  - CHEBI:65525
  evidence_ids:
  - native
  - isolation
  - imaging
- assessment_id: activity
  area: evidence
  topic: Compound-specific measured endpoints
  outcome: supported
  summary: Original exact-compound MIC and fungal/HIV IC50 values support roles. Malaria
    assays support that additional role. Strain scope, endpoint and units must be
    retained; extract tables and derivative assays remain separate.
  target_ids:
  - CHEBI:65525
  evidence_ids:
  - isolation
  - imaging
  - heme
- assessment_id: mechanism
  area: evidence
  topic: Checked malaria mechanism, unresolved bacterial mode
  outcome: unknown
  summary: Primary heme experiments provide a useful antimalarial mechanism candidate,
    but no bacterial molecular mechanism was established in this inspected set. Blank
    optional mechanism/target fields are not a defect.
  target_ids:
  - CHEBI:65525
  evidence_ids:
  - heme
  - isolation
  - synthesis
- assessment_id: other
  area: scope
  topic: Unpopulated optional domains and structured adapter
  outcome: not_applicable
  summary: No native named protein/gene/locus/regulator/pathway or transcriptomics
    dataset triggers a relevant iModulonDB query. Resistance, clinical, producer,
    datasets and graphs have no populated native blocks; source isolation is evaluated
    in the definition.
  target_ids:
  - CHEBI:65525
  evidence_ids:
  - native
- assessment_id: history
  area: provenance
  topic: Seed ownership and audit
  outcome: supported
  summary: Mint, exact source concept and three seed events are coherent. Captured
    bytes are unchanged; native remains SEEDED.
  target_ids:
  - CHEBI:65525
  evidence_ids:
  - native
  - owners
  - chemistry
- assessment_id: complete
  area: completeness
  topic: Bounded future enrichment
  outcome: supported
  summary: Activity and malaria-specific heme evidence are useful optional curation
    candidates. No requirement to populate every optional field or infer protein targets
    follows from these sources.
  target_ids:
  - CHEBI:65525
  evidence_ids:
  - isolation
  - imaging
  - heme
- assessment_id: schema
  area: schema
  topic: Deterministic validation
  outcome: supported
  summary: Focused schema/strict and internal chemical checks pass. Shared corpus
    checks are coordinated separately.
  target_ids:
  - CHEBI:65525
  evidence_ids:
  - gates
  - chemistry
findings:
- finding_id: F1
  issue_key: bromophycolide-a-definition-apotopic-typo
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the inherited cell-death terminology
  description: The generated definition says apotopic cell death. The cited primary
    paper describes apoptotic cell death and measures apoptosis in A2780 human ovarian
    cells. Correct the spelling through the maintained source path without implying
    a bacterial apoptosis mechanism.
  target_ids:
  - CHEBI:65525
  field_paths:
  - definition
  evidence_ids:
  - native
  - owners
  - chebi
  - isolation
  rule_id: native-review-checklist:Evidence standard and field accuracy
  native_severity: minor wording
  normalization_reason: A bounded source-inherited transcription error; identity and
    antimicrobial eligibility remain supported.
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
actions:
- action_id: A1
  description: Correct apotopic to apoptotic through the maintained ChEBI harmonization
    path.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:65525
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
  acceptance_checks:
  - Retain the human tumour-cell scope and primary source meaning.
  - Regenerate the record and confirm source reproducibility, schema/strict and history
    checks.
- action_id: A2
  description: Optionally curate exact activity and malaria-specific heme evidence
    after preparation and method review.
  finding_ids: []
  target_ids:
  - CHEBI:65525
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/bromophycolide-a.yaml
    role: Future curator-owned activity/mechanism claims through validated writer
  acceptance_checks:
  - Read original supplementary assay details before extracting complete MIC observations;
    do not copy extract or analogue rows.
  - Keep malaria heme association/crystallization evidence distinct from unverified
    bacterial mode and from derivative15 localization.
  - Do not force a protein target or extrapolate failed pull-down to absence of targets;
    retain assay solvent/model conditions.
limitations:
- Reaxys returned403; current ChEBI retains the identifier, but independent exact-structure
  verification was unavailable.
- Original2005 supplementary PDF/CIF routes returned HTML challenge pages, not usable
  supplements; main text, tables and published structure drawing were inspected. Detailed
  original assay conditions and independent reprocessing of crystallographic coordinates
  were not completed.
- No exact bacterial mechanism was established in the inspected primary set; heme-crystallization
  evidence concerns P.falciparum and does not fill that gap.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 13 captured hashes rechecked unchanged; no native/source/status/history edits.
- No optional-empty-field or alias-only finding. The synthetic-ring-system paper is
  not a total synthesis or new natural-A bioassay.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:65525
- https://doi.org/10.1021/ol052121f
- https://doi.org/10.1002/cmdc.201100252
tags:
- bromophycolide-a
- marine-natural-product
- assay-scope
- heme-crystallization
```
