# Bacilysocin: source-supported identity and activity with unresolved antimicrobial mode

- Review: 20261021T100520Z-bacilysocin
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:37:20Z
- Finished UTC: 2026-10-21T10:05:20Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

No confirmed scientific finding. Identity,explicitly unresolved stereochemistry,producer definition and both activity roles are source-supported. Focused gates and chemistry pass. Antimicrobial mode/direct target and independent proprietary Reaxys verification remain limited;native SEEDED is retained. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole-record scientific review of bacilysocin CHEBI71621.

Selection: Queue138 in isolated batch014.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:71621 | data/antibiotics/antibacterial/bacilysocin.yaml | generated | bacilysocin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | CHEBI:71621 | Actual command passed. |
| Focused strict | passed | True | CHEBI:71621 | Actual command passed. |
| Internal chemical consistency and mint | passed | True | CHEBI:71621 | Both encodings,formula,charge,masses and actual ChEBI mint agree. |
| Authoritative full QC | failed | True | CHEBI:71621 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:71621 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:71621 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:71621 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:71621 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:71621 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:71621 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:71621 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:71621 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact source entity and stereo granularity

identity: supported. Targets: CHEBI:71621.

Native represents the discovered bacilysocin connectivity with explicitly unresolved carbon stereochemistry. Current authorities and primary source agree; no forced stereochemical refinement is warranted.

### Structure,producer and qualified fungal activity

evidence: supported. Targets: CHEBI:71621.

All substantive definition clauses match the source at their stated scope. The inherited word acide is a spelling blemish,not a scientific identity defect.

### Parents,roles and filing

grounding: supported. Targets: CHEBI:71621.

Three parents are broader chemical classes. Antibacterial filing retains antifungal activity and follows repository priority;it does not claim uniform bacterial susceptibility.

### Reaxys registry identifier

provenance: unknown. Targets: CHEBI:71621.

Current ChEBI reproduces Reaxys10044462;the proprietary registry record was not independently opened. No contradictory identity evidence was found in the inspected sources.

### Bacterial and fungal observations

evidence: supported. Targets: CHEBI:71621.

Purified-compound strain-level measurements support both activity roles. The optional activity_spectrum block can be curated later with exact media and qualifiers.

### B.subtilis168 origin

evidence: supported. Targets: CHEBI:71621.

Definition producer is established by isolation and characterization. Structured producer annotation would be a useful optional addition with this primary citation.

### Antimicrobial target versus biosynthesis

evidence: unknown. Targets: CHEBI:71621.

Inspected primary work does not establish a direct target or defined antimicrobial mode. YtpA is biosynthetic evidence and must not be imported as the attacked protein.

### Source metadata and history

provenance: supported. Targets: CHEBI:71621.

Adopted source,exact grounding and three seed events are coherent. Review does not promote native SEEDED.

### Optional evidence additions

completeness: unknown. Targets: CHEBI:71621.

Direct primary activity and producer facts are available for later curation. Their absence is not a required-schema defect;unknown antimicrobial mode remains a scientific sign-off limit.

### Resistance,clinical,dataset and graph fields

scope: not_applicable. Targets: CHEBI:71621.

No populated claims in these native blocks. No clinical or resistance inference is drawn from producer genetics.

### Focused checks

schema: supported. Targets: CHEBI:71621.

Both validators and chemical consistency pass.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/bacilysocin.yaml; Entire YAML | supports | Read exact CHEBI71621 identity,definition and both synonyms,three parents,three antimicrobial roles,all chemical fields,Reaxys xref,source mint and three seed-history events. Optional mechanism,target,activity,producer,resistance,clinical,dataset and graph blocks are unpopulated. |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/chebi_role_names.tsv; conf/sources.yaml; Compound row1824 and source extraction/seeding configuration | supports | Native faithfully reproduces adopted ChEBI fields and source PMID11796336 lead. Antibacterial filing follows configured priority while retaining antifungal and general antimicrobial roles. Correct owner inputs were captured before assessment. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:71621; Current full entry,parents,roles,synonyms,chemical fields and registry mapping | supports | Live ChEBI matches native unspecified stereochemistry,formula,key,charge,masses,definition and names. Parent16961 monoacylglycerol phosphate,parent24360 glycerophosphoglycerols and parent33308 carboxylic ester are broader. All three native antimicrobial roles persist. Reaxys10044462 is retained as its registry mapping. Additional metabolite role is outside the adopted antimicrobial-role slice. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/10344650; Independent live PUG identity | supports | PubChem bacilysocin has identical Standard InChI/key,C21H43O9P and charge0. Rounded mass470.5 and exact470.26446994 are compatible with native ChEBI values. It introduces no stereochemical assignment. |
| chemistry | Independent RDKit and mint check; Native SMILES and Standard InChI | supports | Both encodings parse to one neutral fragment,C21H43O9P,key DIGHTWUQPWHBPG-UHFFFAOYSA-N; average470.540 and exact470.264469586 reproduce stored values. ChEBI mint matches. Three carbon centres remain unspecified; RDKit also flags phosphorus in the neutral graph,which is not treated as a missing natural stereochemical assignment. |
| primary | https://doi.org/10.1128/AAC.46.2.315-320.2002; PMID11796336/PMC127064; full Methods,Results structure and Table2,Discussion | supports | Original study isolated170mg purified bacilysocin from B.subtilis168,established connectivity by NMR/MS,and expressly left C2,C2-prime,C12 stereochemistry unresolved. Agar-dilution Table2 gives S.aureus FDA209P50 and Smith25micrograms/mL on Mueller-Hinton agar;S.cerevisiae IMCF7=5 and selected Candida/Cryptococcus25 on synthetic amino-acid fungal agar. Several other tested strains exceeded100. Thus both retained activity roles and the qualified fungal wording are supported. YtpA disruption/lysophospholipase experiments concern biosynthesis and sporulation,not a microbial target of the antibiotic. |
| adapter | kg-microbe-sources imodulondb search --organism b_subtilis --dataset modulome --query ytpA; Actual source-follow-up structured query;covered dataset identified by recent successful datasets retrieval | context_only | One gene hit,b_subtilis/modulome/BSU_30510,ytpA,phospholipase;zero iModulon hits. This is gene-context support for distinguishing a biosynthetic enzyme from a drug target. It does not prove expression response,causality or antimicrobial mechanism. |
| search | CultureBotAI/AntibioticMech and EuropePMC; Ignored-inclusive target search and compound literature query | context_only | Search included ignored files outside.git/.venv;native/raw/curation hits were inspected. The bounded literature search located the primary discovery study and broader secondary/producer literature. No exact-compound direct target was established in the inspected primary study. |
| literature | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=bacilysocin&amp;format=json&amp;resultType=core&amp;pageSize=50; Bounded compound-specific search snapshot | context_only | Primary citation metadata resolves correctly. Other returned studies mentioning a biosynthetic gene or annotated metabolite were discovery context,not exact purified-compound mechanism evidence. |
| gates | just validate; just validate-strict; Actual batch014 focused commands | supports | Both actual commands exit0;strict checked one file with zero errors. Independent chemistry passes. |

## Limits And Additional Notes

- Reaxys10044462 was verified as the live ChEBI mapping but not independently inspected in the proprietary registry.
- The bounded primary review does not establish bacilysocin antimicrobial mode or direct target. YtpA production genetics do not meet that requirement;passing this read-only review does not justify REVIEWED promotion.
- The discovery source leaves three carbon stereocentres unresolved,as does the native definition. No later complete stereochemical assignment was established in the bounded search.
- One PMC request returned browser verification and EuropePMC XML returned500;the alternate public PMC HTML supplied complete main text. No retrieval failure was treated as absence of literature.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All20 captured input hashes rechecked unchanged. No native/source-table,status or history edits.
- Optional activity_spectrum and producer annotations could use PMID11796336 with exact strain/media values;their absence is not a finding.
- The source-only spelling acide can be corrected editorially through maintained definition ownership in future curation;it does not change the scientific verdict.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T100520Z-bacilysocin
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Bacilysocin: source-supported identity and activity with unresolved antimicrobial
  mode'
started_at: '2026-10-21T09:37:20Z'
finished_at: '2026-10-21T10:05:20Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Full native/source-owner read,current chemical authorities,independent
    chemistry and original purified-compound primary study.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: No confirmed scientific finding. Identity,explicitly unresolved stereochemistry,producer
  definition and both activity roles are source-supported. Focused gates and chemistry
  pass. Antimicrobial mode/direct target and independent proprietary Reaxys verification
  remain limited;native SEEDED is retained. Scientific assessment retains the stated
  evidence limits; full verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/bacilysocin.yaml
    sha256: c6c929acb8bc2d50c2b97188b7835154250bc43ea737478b144103b3849e9f63
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
  - path: CLAUDE.md
    sha256: 36fb92f8919481cfbf3f17ddde4a1e244c81f76c64396dbbac910c4815fb9f16
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
    role: context
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
targets:
- target_id: CHEBI:71621
  path: data/antibiotics/antibacterial/bacilysocin.yaml
  label: bacilysocin
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
  description: Whole-record scientific review of bacilysocin CHEBI71621.
  selection: Queue138 in isolated batch014.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:71621
  exclusions:
  - target: Producer strains,other phospholipids and mixed extracts as separate records
    reason: Only context for exact native structure and evidence boundaries.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual command passed.
  target_ids:
  - CHEBI:71621
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/bacilysocin.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: strict
  name: Focused strict
  status: passed
  required: true
  summary: Actual command passed.
  target_ids:
  - CHEBI:71621
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/bacilysocin.yaml --out /private/tmp/am-review-session/138-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Internal chemical consistency and mint
  status: passed
  required: true
  summary: Both encodings,formula,charge,masses and actual ChEBI mint agree.
  target_ids:
  - CHEBI:71621
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
  - CHEBI:71621
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
  - CHEBI:71621
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
  - CHEBI:71621
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
  - CHEBI:71621
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
  - CHEBI:71621
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
  - CHEBI:71621
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
  - CHEBI:71621
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
  - CHEBI:71621
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
  - CHEBI:71621
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/bacilysocin.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T09:39:49Z'
  support: supports
  summary: Read exact CHEBI71621 identity,definition and both synonyms,three parents,three
    antimicrobial roles,all chemical fields,Reaxys xref,source mint and three seed-history
    events. Optional mechanism,target,activity,producer,resistance,clinical,dataset
    and graph blocks are unpopulated.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/chebi_role_names.tsv; conf/sources.yaml
  locator: Compound row1824 and source extraction/seeding configuration
  accessed_at: '2026-10-21T09:39:49Z'
  support: supports
  summary: Native faithfully reproduces adopted ChEBI fields and source PMID11796336
    lead. Antibacterial filing follows configured priority while retaining antifungal
    and general antimicrobial roles. Correct owner inputs were captured before assessment.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:71621
  locator: Current full entry,parents,roles,synonyms,chemical fields and registry
    mapping
  accessed_at: '2026-10-21T09:37:36Z'
  support: supports
  summary: Live ChEBI matches native unspecified stereochemistry,formula,key,charge,masses,definition
    and names. Parent16961 monoacylglycerol phosphate,parent24360 glycerophosphoglycerols
    and parent33308 carboxylic ester are broader. All three native antimicrobial roles
    persist. Reaxys10044462 is retained as its registry mapping. Additional metabolite
    role is outside the adopted antimicrobial-role slice.
  snapshot_sha256: fe270c9e2145990920267a4061555542ab4d1f39a3f090eaa1a8a7a42a0f2b79
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/10344650
  locator: Independent live PUG identity
  accessed_at: '2026-10-21T09:37:35Z'
  support: supports
  summary: PubChem bacilysocin has identical Standard InChI/key,C21H43O9P and charge0.
    Rounded mass470.5 and exact470.26446994 are compatible with native ChEBI values.
    It introduces no stereochemical assignment.
  snapshot_sha256: 7fa6ad28e0e2acfc07d6841567a1f3b20e5cb700a5747cdcfffc26583170b4fd
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit and mint check
  locator: Native SMILES and Standard InChI
  accessed_at: '2026-10-21T09:37:33Z'
  support: supports
  summary: Both encodings parse to one neutral fragment,C21H43O9P,key DIGHTWUQPWHBPG-UHFFFAOYSA-N;
    average470.540 and exact470.264469586 reproduce stored values. ChEBI mint matches.
    Three carbon centres remain unspecified; RDKit also flags phosphorus in the neutral
    graph,which is not treated as a missing natural stereochemical assignment.
  snapshot_sha256: c7910159932f53562910d5cf4c5db29a6d704704b9c24aeffaedad0a3bc7cfd3
- evidence_id: primary
  kind: primary_source
  reference: https://doi.org/10.1128/AAC.46.2.315-320.2002
  locator: PMID11796336/PMC127064; full Methods,Results structure and Table2,Discussion
  accessed_at: '2026-10-21T09:38:09Z'
  support: supports
  summary: Original study isolated170mg purified bacilysocin from B.subtilis168,established
    connectivity by NMR/MS,and expressly left C2,C2-prime,C12 stereochemistry unresolved.
    Agar-dilution Table2 gives S.aureus FDA209P50 and Smith25micrograms/mL on Mueller-Hinton
    agar;S.cerevisiae IMCF7=5 and selected Candida/Cryptococcus25 on synthetic amino-acid
    fungal agar. Several other tested strains exceeded100. Thus both retained activity
    roles and the qualified fungal wording are supported. YtpA disruption/lysophospholipase
    experiments concern biosynthesis and sporulation,not a microbial target of the
    antibiotic.
  snapshot_sha256: 62a0e7919b9dfcfc07633682bd9ea5e1debce8bf9f34b9e631328fe1085d4af3
- evidence_id: adapter
  kind: database
  reference: kg-microbe-sources imodulondb search --organism b_subtilis --dataset
    modulome --query ytpA
  locator: Actual source-follow-up structured query;covered dataset identified by
    recent successful datasets retrieval
  accessed_at: '2026-10-21T09:38:43Z'
  support: context_only
  summary: One gene hit,b_subtilis/modulome/BSU_30510,ytpA,phospholipase;zero iModulon
    hits. This is gene-context support for distinguishing a biosynthetic enzyme from
    a drug target. It does not prove expression response,causality or antimicrobial
    mechanism.
  snapshot_sha256: 736ca7cecf6c406d92174e692e954b0b53c2c85876111fbc7c7272ca369ef04c
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech and EuropePMC
  locator: Ignored-inclusive target search and compound literature query
  accessed_at: '2026-10-21T09:37:21Z'
  support: context_only
  summary: Search included ignored files outside.git/.venv;native/raw/curation hits
    were inspected. The bounded literature search located the primary discovery study
    and broader secondary/producer literature. No exact-compound direct target was
    established in the inspected primary study.
  search_scope: prepare.py138 rg --no-ignore --hidden identifier,label,slug;exact
    raw/curation searches;EuropePMC bacilysocin core query;current ChEBI and PubChem;full
    primary study.
  snapshot_sha256: f6414ed61129617cac3bdb490fe0d57a6c0a584311a9c7d23d28292b193b91df
- evidence_id: literature
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=bacilysocin&format=json&resultType=core&pageSize=50
  locator: Bounded compound-specific search snapshot
  accessed_at: '2026-10-21T09:37:38Z'
  support: context_only
  summary: Primary citation metadata resolves correctly. Other returned studies mentioning
    a biosynthetic gene or annotated metabolite were discovery context,not exact purified-compound
    mechanism evidence.
  search_scope: EuropePMC bacilysocin query,up to50 core results;not an exhaustive
    systematic literature review.
  snapshot_sha256: 88dc049057eec776d319cdcdff7653506938763b0dc76f33c92fc0c2c143afdb
- evidence_id: gates
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual batch014 focused commands
  accessed_at: '2026-10-21T09:39:49Z'
  support: supports
  summary: Both actual commands exit0;strict checked one file with zero errors. Independent
    chemistry passes.
  snapshot_sha256: 274b82cd7f4250dc9c82c59da790b770e488d0d1c5b6a727d92c3e93a2a8f386
assessments:
- assessment_id: identity
  area: identity
  topic: Exact source entity and stereo granularity
  outcome: supported
  summary: Native represents the discovered bacilysocin connectivity with explicitly
    unresolved carbon stereochemistry. Current authorities and primary source agree;
    no forced stereochemical refinement is warranted.
  target_ids:
  - CHEBI:71621
  evidence_ids:
  - native
  - chebi
  - pubchem
  - chemistry
  - primary
- assessment_id: definition
  area: evidence
  topic: Structure,producer and qualified fungal activity
  outcome: supported
  summary: All substantive definition clauses match the source at their stated scope.
    The inherited word acide is a spelling blemish,not a scientific identity defect.
  target_ids:
  - CHEBI:71621
  evidence_ids:
  - native
  - chebi
  - primary
- assessment_id: grounding
  area: grounding
  topic: Parents,roles and filing
  outcome: supported
  summary: Three parents are broader chemical classes. Antibacterial filing retains
    antifungal activity and follows repository priority;it does not claim uniform
    bacterial susceptibility.
  target_ids:
  - CHEBI:71621
  evidence_ids:
  - owners
  - chebi
  - primary
- assessment_id: xref
  area: provenance
  topic: Reaxys registry identifier
  outcome: unknown
  summary: Current ChEBI reproduces Reaxys10044462;the proprietary registry record
    was not independently opened. No contradictory identity evidence was found in
    the inspected sources.
  target_ids:
  - CHEBI:71621
  evidence_ids:
  - chebi
  - pubchem
- assessment_id: activity
  area: evidence
  topic: Bacterial and fungal observations
  outcome: supported
  summary: Purified-compound strain-level measurements support both activity roles.
    The optional activity_spectrum block can be curated later with exact media and
    qualifiers.
  target_ids:
  - CHEBI:71621
  evidence_ids:
  - primary
- assessment_id: producer
  area: evidence
  topic: B.subtilis168 origin
  outcome: supported
  summary: Definition producer is established by isolation and characterization. Structured
    producer annotation would be a useful optional addition with this primary citation.
  target_ids:
  - CHEBI:71621
  evidence_ids:
  - primary
- assessment_id: mechanism
  area: evidence
  topic: Antimicrobial target versus biosynthesis
  outcome: unknown
  summary: Inspected primary work does not establish a direct target or defined antimicrobial
    mode. YtpA is biosynthetic evidence and must not be imported as the attacked protein.
  target_ids:
  - CHEBI:71621
  evidence_ids:
  - primary
  - adapter
- assessment_id: history
  area: provenance
  topic: Source metadata and history
  outcome: supported
  summary: Adopted source,exact grounding and three seed events are coherent. Review
    does not promote native SEEDED.
  target_ids:
  - CHEBI:71621
  evidence_ids:
  - native
  - owners
- assessment_id: completeness
  area: completeness
  topic: Optional evidence additions
  outcome: unknown
  summary: Direct primary activity and producer facts are available for later curation.
    Their absence is not a required-schema defect;unknown antimicrobial mode remains
    a scientific sign-off limit.
  target_ids:
  - CHEBI:71621
  evidence_ids:
  - primary
  - search
- assessment_id: other
  area: scope
  topic: Resistance,clinical,dataset and graph fields
  outcome: not_applicable
  summary: No populated claims in these native blocks. No clinical or resistance inference
    is drawn from producer genetics.
  target_ids:
  - CHEBI:71621
  evidence_ids:
  - native
  - primary
- assessment_id: schema
  area: schema
  topic: Focused checks
  outcome: supported
  summary: Both validators and chemical consistency pass.
  target_ids:
  - CHEBI:71621
  evidence_ids:
  - gates
  - chemistry
findings: []
actions: []
limitations:
- Reaxys10044462 was verified as the live ChEBI mapping but not independently inspected
  in the proprietary registry.
- The bounded primary review does not establish bacilysocin antimicrobial mode or
  direct target. YtpA production genetics do not meet that requirement;passing this
  read-only review does not justify REVIEWED promotion.
- The discovery source leaves three carbon stereocentres unresolved,as does the native
  definition. No later complete stereochemical assignment was established in the bounded
  search.
- One PMC request returned browser verification and EuropePMC XML returned500;the
  alternate public PMC HTML supplied complete main text. No retrieval failure was
  treated as absence of literature.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All20 captured input hashes rechecked unchanged. No native/source-table,status or
  history edits.
- Optional activity_spectrum and producer annotations could use PMID11796336 with
  exact strain/media values;their absence is not a finding.
- The source-only spelling acide can be corrected editorially through maintained definition
  ownership in future curation;it does not change the scientific verdict.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:71621
- https://pubchem.ncbi.nlm.nih.gov/compound/10344650
- https://doi.org/10.1128/AAC.46.2.315-320.2002
tags:
- bacilysocin
- phospholipid
- stereochemistry
- primary-evidence
```
