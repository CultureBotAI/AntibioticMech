# DHMBA: exact identity, quantitative activity and fungal producer evidence

- Review: 20261021T070455Z-2-4-dihydroxy-3-methyl-6-2-oxopropyl-benzaldehyde
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T06:56:30Z
- Finished UTC: 2026-10-21T07:04:55Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact identity and seeded provenance are coherent. Two minor, evidence-specific opportunities concern quantitative antibacterial activity and fungal production. A source-internal disk-dose discrepancy is documented; neither biosynthetic enzymes nor related tropolones establish this compound’s antibacterial target.

## Scope And Provenance

Complete one-record assessment with bounded exact-compound primary-source research.

Selection: Queue index014, exactly CHEBI:155860.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:155860 | data/antibiotics/antibacterial/2-4-dihydroxy-3-methyl-6-2-oxopropyl-benzaldehyde.yaml | generated | 2,4-dihydroxy-3-methyl-6-(2-oxopropyl)benzaldehyde |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Single-record LinkML schema | passed | True | CHEBI:155860 | Focused gate passed with no errors. |
| Single-record strict validation | passed | True | CHEBI:155860 | Focused gate passed with no errors. |
| Official identity and ontology verification | passed | True | CHEBI:155860 | Exact structure, neutral charge, parents and configured antibacterial role agree. |
| Expression-module adapter applicability | not_applicable | False | CHEBI:155860 | No native expression or drug-target claim. Biosynthetic expression experiments do not create a pharmacological target object. |
| Authoritative full QC | failed | True | CHEBI:155860 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:155860 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:155860 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:155860 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:155860 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:155860 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:155860 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:155860 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:155860 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral compound

identity: supported. Targets: CHEBI:155860.

Official structure and primary Figure3B agree; chemical parents are appropriately broader classifications. Acronym alone is not an identity match.

### Antibacterial filing

grounding: supported. Targets: CHEBI:155860.

Official role and direct exact-compound activity justify ANTIBACTERIAL. The bounded assay does not establish broad clinical or species-wide efficacy.

### Source-specific assay enrichment

completeness: concern. Targets: CHEBI:155860.

A directly inspected source provides a quantitative activity observation suitable for scoped curation. Disk concentration inconsistency must be preserved or resolved independently.

### Fungal production evidence

completeness: concern. Targets: CHEBI:155860.

Primary isolation and later production experiments provide an actionable producer annotation. Preserve engineered or induced culture context; do not treat biosynthetic enzymes as drug targets.

### Antibacterial molecular mechanism

evidence: unknown. Targets: CHEBI:155860.

The inspected material supports activity and biosynthesis. It does not establish an antibacterial molecular target for exact DHMBA. Tropolone mechanisms cannot be transferred to this precursor; this bounded search does not prove no mechanism literature exists.

### Other optional scientific objects

evidence: not_applicable. Targets: CHEBI:155860.

No native resistance, clinical-use, dataset, causal-graph or protein-example assertions need correction. Their empty slots are not assigned blanket defects.

### Generated ownership and native status

provenance: supported. Targets: CHEBI:155860.

Source identity and history agree, and SEEDED is appropriate. Citation leads require claim-level review before promotion.

### Focused validation

schema: supported. Targets: CHEBI:155860.

Both focused validation gates pass.

## Findings

### F1: The exact-compound microplate result is available for scoped activity curation

minor / open / confirmed; issue key: chebi-155860-primary-activity-enrichment.

The inspected primary paper supplies a concrete activity observation, while the current seed contains no activity_spectrum. This is an evidence-specific enrichment opportunity, not invalid optional-field absence. The conflicting disk concentrations preclude silently standardizing disk loading.

### F2: Primary isolation and induced-production data support producer annotation

minor / open / confirmed; issue key: chebi-155860-producer-enrichment.

The seed lacks producer context despite directly inspected exact-compound biosynthesis evidence. Record the producing fungus with the experimental context; do not infer that a co-cultured bacterium produces this molecule or that a biosynthetic protein is its antibacterial target.

## Recommended Actions And Acceptance Checks

### A1

Curate the reported microplate observation with organism grounding, endpoint, method and experimental conditions. Inspect supplemental strain metadata before assigning a strain. Retain the documented disk-dose discrepancy if adding the separate diffusion result.

- Exact compound, original units, endpoint and primary locator remain traceable; no susceptible/resistant clinical category is invented.
- Any disk loading is resolved from source evidence or explicitly left unresolved.
- Use native validated writer and curation event; run strict, reproducibility and QC gates.

### A2

Curate a source-backed Aspergillus nidulans producer entry with appropriate current taxon grounding and induced/engineered culture context. Keep biosynthetic pathway references separate from antibacterial mode and target fields.

- Producer identity and culture context are traceable to primary evidence.
- No derivative iron-chelation or biosynthetic-enzyme claim is transferred into the antibacterial mechanism.
- Use native writer/history and focused strict, reproducibility and QC gates before native status promotion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/2-4-dihydroxy-3-methyl-6-2-oxopropyl-benzaldehyde.yaml; Complete YAML including two synonyms, structure and three seeder history events | supports | Exact ChEBI-only neutral compound, ANTIBACTERIAL and SEEDED. There are no curator-owned mechanism, molecular target, activity_spectrum, resistance, producer, clinical, dataset or causal_graphs assertions, and no activity collections or external identity xrefs. |
| owner | data/raw/chebi_antimicrobials.tsv; CHEBI:155860 row2735; MANIFEST; extractor and seeder; data/antibiotics/PATHS.tsv row295 | supports | Adopted identity, aliases, three parents, antibacterial role, structure and minted concept match. The four PMID leads are discovery metadata. Seed-owned changes belong upstream; new scientific annotations belong on this actual record. Source version2026-08-30 and seeder events are coherent. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:155860; Names, structure, roles, chemical parents and species-of-origin sections | supports | Official ChEBI agrees with neutral C11H12O4, charge0, key NYFZWIIIOFTTKN-UHFFFAOYSA-N, SMILES/InChI and masses208.213/208.07356. The polyketide, dihydroxybenzaldehyde and methyl-ketone parents are chemical classifications, not identity xrefs. Both exact synonyms and antibacterial role agree. Its Aspergillus metabolite role and A.nidulans species annotation offer producer context. |
| config | conf/sources.yaml; role_to_class; role_to_mode_of_action; data/raw/chebi_role_names.tsv | supports | The antibacterial role CHEBI:33282 maps to ANTIBACTERIAL. No specific mechanism role is adopted for this compound, so the empty seeded mode is expected. Fungal metabolite roles are not automatically drug targets or antibacterial mechanism assertions. |
| local-search | CultureBotAI/AntibioticMech; Ignored-inclusive exact and expanded-alias searches | context_only | The complete target and source owners were inspected. No target-specific curator override or historical prose report was found within the queried curation/reviews/report scopes, including ignored and hidden files. No global literature absence is inferred. |
| rubric | docs/CURATION.md; Native REVIEWED criteria; claim-specific evidence; review checklist and schema | supports | Source roles can justify seed classification without per-record literature objects. Empty optional slots do not violate schema. Evidence-backed enrichment must retain exact compound and assay scope; biosynthesis proteins are not pharmacological targets. Future annotation requires native writer/history and validation. |
| gerke2012 | PMID:23001671; https://mural.maynoothuniversity.ie/id/eprint/6246/1/OB-Breaking-Silence.pdf — DOI10.1128/AEM.01808-12; pp8235,8238; Methods and Figure3; PDF text and page image inspected | supports | Purified exact DHMBA from A.nidulans dbaA-overexpression cultures inhibited M.luteus: MIC3.1 µg/mL, microplate Mueller-Hinton broth,30°C, up to24h, complete-growth-inhibition endpoint, independent triplicates. Figure3B matches the target structure; Figure3C reports a2.5cm zone. Disk concentration conflicts: Methods1mg/mL versus Figure3C1mg/µL. The strain list is supplemental and was not inspected; no M.luteus strain identifier is assigned. Production and gene-deletion results concern fungal biosynthesis, not the bacterial molecular target. |
| gerke2022 | DOI:10.3389/ffunb.2021.777474; https://www.frontiersin.org/journals/fungal-biology/articles/10.3389/ffunb.2021.777474/full — Results, Figures2/4 and Bioactivity Assays; published2022-01-03 | supports | DHMBA is compound3, detected by HRESIMS/UV in A.nidulans AGB552 co-culture with S.mobaraensis. Deleting dbaI abolishes its production. Purified growth-inhibition experiments distinguish tropolones1/2 from DHMBA3. The iron-chelation/tropolone narrative cannot establish the mechanism of DHMBA; co-culture extracts are mixtures. |
| mibig | https://mibig.secondarymetabolites.org/repository/BGC0002758.1/; Entry status, organism, compound3 and biosynthetic locus | context_only | The public entry lists DHMBA among azanidulone-cluster products in A.nidulans FGSC A4, with MS evidence and2022-paper provenance. Status is pending and completeness partial. It is a producer/biosynthetic follow-up source, not an independently established antibacterial target. |
| adopted-other | PMID:22510154; PMID:25142695; PMID:28550524; PubMed/PMC metadata and inspected abstracts; https://pmc.ncbi.nlm.nih.gov/articles/PMC4192562/ ; https://pubmed.ncbi.nlm.nih.gov/28550524/ | context_only | Ahuja2012 DOI10.1021/ja3016395 is a biosynthesis lead whose full text was blocked. Gerke/Braus2014 is a secondary review of fungal developmental regulation, not independent activity evidence. The2017 Pestalotiopsis fici abstract concerns PfCsnE regulation and named other metabolites; its abstract alone does not establish this exact compound as a P.fici product. |
| search-boundary | Exact compound and adopted citation searches; ChEBI, PubMed/PMC, publisher and institutional full text | context_only | Exact chemical name and structure were prioritized over DHMBA acronym matches. Newer benzaldehyde quorum-sensing literature was a discovery lead, but no target-specific mechanism claim is adopted from it. Commercial mechanism summaries were not used. |
| validation | just validate; just validate-strict; New isolated worktree002; /private/tmp/am-review-session/014-validation.tsv | supports | Both focused commands exited0. LinkML reported no issues; strict scanned1 target with0 ERROR rows. |

## Limits And Additional Notes

- The2012 main paper and Figure3 were inspected, but supplemental strain/chemical data were not. The disk-loading discrepancy remains unresolved.
- The2012 Ahuja full text was access-limited; other adopted leads were secondary context or abstract-only. Bounded searches do not establish global absence of mechanism evidence.
- No paid research or native record edits occurred.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Provenance capture preceded assessment; expanded context preserved all initial hashes and base revision.
- Hidden and ignored files were included in all searches used to report local absence.
- The record remains SEEDED; future scientific enrichment requires native curation history and a separate readiness decision.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T070455Z-2-4-dihydroxy-3-methyl-6-2-oxopropyl-benzaldehyde
kind: record
repository: CultureBotAI/AntibioticMech
title: 'DHMBA: exact identity, quantitative activity and fungal producer evidence'
started_at: '2026-10-21T06:56:30Z'
finished_at: '2026-10-21T07:04:55Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Reviewer did not create or curate this seed and independently
    inspected current source content; agent review is not human scientific sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Exact identity and seeded provenance are coherent. Two minor, evidence-specific
  opportunities concern quantitative antibacterial activity and fungal production.
  A source-internal disk-dose discrepancy is documented; neither biosynthetic enzymes
  nor related tropolones establish this compound’s antibacterial target.
source:
  git_revision: baf3b3203d748d098686e166cdb2a6138f47eb59
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 5e2e1f975f8aa64f92a06c134c98c750c968fd78f02620a73c9cb611ac018ed8
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: CLAUDE.md
    sha256: 36fb92f8919481cfbf3f17ddde4a1e244c81f76c64396dbbac910c4815fb9f16
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
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
  - path: data/antibiotics/PATHS.tsv
    sha256: 3b1d82d007878e4aca2c28f4001a468776b325b726da2e48abb76a3dc551cc38
    role: context
  - path: data/antibiotics/antibacterial/2-4-dihydroxy-3-methyl-6-2-oxopropyl-benzaldehyde.yaml
    sha256: eb37605ef9873389a71bbaf0a7a812b47f561c80cd6674d5e93089eaa1cdf9e7
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
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
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
- target_id: CHEBI:155860
  path: data/antibiotics/antibacterial/2-4-dihydroxy-3-methyl-6-2-oxopropyl-benzaldehyde.yaml
  label: 2,4-dihydroxy-3-methyl-6-(2-oxopropyl)benzaldehyde
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
  description: Complete one-record assessment with bounded exact-compound primary-source
    research.
  selection: Queue index014, exactly CHEBI:155860.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:155860
  exclusions:
  - target: Related tropolones, DHPDI and other DHMBA acronym expansions
    reason: Comparison or discovery context only; no independent record verdict or
      transferred mechanism.
checks:
- check_id: schema
  name: Single-record LinkML schema
  status: passed
  required: true
  summary: Focused gate passed with no errors.
  target_ids:
  - CHEBI:155860
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/2-4-dihydroxy-3-methyl-6-2-oxopropyl-benzaldehyde.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Single-record strict validation
  status: passed
  required: true
  summary: Focused gate passed with no errors.
  target_ids:
  - CHEBI:155860
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/2-4-dihydroxy-3-methyl-6-2-oxopropyl-benzaldehyde.yaml
    --out /private/tmp/am-review-session/014-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: identity
  name: Official identity and ontology verification
  status: passed
  required: true
  summary: Exact structure, neutral charge, parents and configured antibacterial role
    agree.
  target_ids:
  - CHEBI:155860
  evidence_ids:
  - chebi
  - config
- check_id: imodulondb
  name: Expression-module adapter applicability
  status: not_applicable
  required: false
  summary: No native expression or drug-target claim. Biosynthetic expression experiments
    do not create a pharmacological target object.
  target_ids:
  - CHEBI:155860
  evidence_ids:
  - record
  - gerke2022
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:155860
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
  - CHEBI:155860
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
  - CHEBI:155860
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
  - CHEBI:155860
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
  - CHEBI:155860
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
  - CHEBI:155860
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
  - CHEBI:155860
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
  - CHEBI:155860
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
  - CHEBI:155860
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/2-4-dihydroxy-3-methyl-6-2-oxopropyl-benzaldehyde.yaml
  locator: Complete YAML including two synonyms, structure and three seeder history
    events
  accessed_at: '2026-10-21T06:59:19Z'
  support: supports
  summary: Exact ChEBI-only neutral compound, ANTIBACTERIAL and SEEDED. There are
    no curator-owned mechanism, molecular target, activity_spectrum, resistance, producer,
    clinical, dataset or causal_graphs assertions, and no activity collections or
    external identity xrefs.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: CHEBI:155860 row2735; MANIFEST; extractor and seeder; data/antibiotics/PATHS.tsv
    row295
  accessed_at: '2026-10-21T06:59:19Z'
  support: supports
  summary: Adopted identity, aliases, three parents, antibacterial role, structure
    and minted concept match. The four PMID leads are discovery metadata. Seed-owned
    changes belong upstream; new scientific annotations belong on this actual record.
    Source version2026-08-30 and seeder events are coherent.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:155860
  locator: Names, structure, roles, chemical parents and species-of-origin sections
  accessed_at: '2026-10-21T06:59:19Z'
  support: supports
  summary: Official ChEBI agrees with neutral C11H12O4, charge0, key NYFZWIIIOFTTKN-UHFFFAOYSA-N,
    SMILES/InChI and masses208.213/208.07356. The polyketide, dihydroxybenzaldehyde
    and methyl-ketone parents are chemical classifications, not identity xrefs. Both
    exact synonyms and antibacterial role agree. Its Aspergillus metabolite role and
    A.nidulans species annotation offer producer context.
- evidence_id: config
  kind: record_content
  reference: conf/sources.yaml
  locator: role_to_class; role_to_mode_of_action; data/raw/chebi_role_names.tsv
  accessed_at: '2026-10-21T06:59:19Z'
  support: supports
  summary: The antibacterial role CHEBI:33282 maps to ANTIBACTERIAL. No specific mechanism
    role is adopted for this compound, so the empty seeded mode is expected. Fungal
    metabolite roles are not automatically drug targets or antibacterial mechanism
    assertions.
- evidence_id: local-search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: Ignored-inclusive exact and expanded-alias searches
  accessed_at: '2026-10-21T06:59:19Z'
  support: context_only
  summary: The complete target and source owners were inspected. No target-specific
    curator override or historical prose report was found within the queried curation/reviews/report
    scopes, including ignored and hidden files. No global literature absence is inferred.
  search_scope: prepare.py14 used rg --no-ignore --hidden over the worktree excluding
    .git/.venv. Follow-up exact ID/key/minted searches in raw, curation, reviews and
    PATHS; expanded rg --no-ignore --hidden -n -i for DHMBA,155860,NYFZWIIIOFTTKN
    and full-name stem in curation reviews reports/yaml_record_review excluding record_review_queue.tsv.
    A BGC0002758 search in raw/curation returned no hits.
- evidence_id: rubric
  kind: record_content
  reference: docs/CURATION.md
  locator: Native REVIEWED criteria; claim-specific evidence; review checklist and
    schema
  accessed_at: '2026-10-21T06:59:19Z'
  support: supports
  summary: Source roles can justify seed classification without per-record literature
    objects. Empty optional slots do not violate schema. Evidence-backed enrichment
    must retain exact compound and assay scope; biosynthesis proteins are not pharmacological
    targets. Future annotation requires native writer/history and validation.
- evidence_id: gerke2012
  kind: primary_source
  reference: PMID:23001671
  locator: https://mural.maynoothuniversity.ie/id/eprint/6246/1/OB-Breaking-Silence.pdf
    — DOI10.1128/AEM.01808-12; pp8235,8238; Methods and Figure3; PDF text and page
    image inspected
  accessed_at: '2026-10-21T06:59:19Z'
  support: supports
  summary: 'Purified exact DHMBA from A.nidulans dbaA-overexpression cultures inhibited
    M.luteus: MIC3.1 µg/mL, microplate Mueller-Hinton broth,30°C, up to24h, complete-growth-inhibition
    endpoint, independent triplicates. Figure3B matches the target structure; Figure3C
    reports a2.5cm zone. Disk concentration conflicts: Methods1mg/mL versus Figure3C1mg/µL.
    The strain list is supplemental and was not inspected; no M.luteus strain identifier
    is assigned. Production and gene-deletion results concern fungal biosynthesis,
    not the bacterial molecular target.'
- evidence_id: gerke2022
  kind: primary_source
  reference: DOI:10.3389/ffunb.2021.777474
  locator: https://www.frontiersin.org/journals/fungal-biology/articles/10.3389/ffunb.2021.777474/full
    — Results, Figures2/4 and Bioactivity Assays; published2022-01-03
  accessed_at: '2026-10-21T06:59:19Z'
  support: supports
  summary: DHMBA is compound3, detected by HRESIMS/UV in A.nidulans AGB552 co-culture
    with S.mobaraensis. Deleting dbaI abolishes its production. Purified growth-inhibition
    experiments distinguish tropolones1/2 from DHMBA3. The iron-chelation/tropolone
    narrative cannot establish the mechanism of DHMBA; co-culture extracts are mixtures.
- evidence_id: mibig
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0002758.1/
  locator: Entry status, organism, compound3 and biosynthetic locus
  accessed_at: '2026-10-21T06:59:19Z'
  support: context_only
  summary: The public entry lists DHMBA among azanidulone-cluster products in A.nidulans
    FGSC A4, with MS evidence and2022-paper provenance. Status is pending and completeness
    partial. It is a producer/biosynthetic follow-up source, not an independently
    established antibacterial target.
- evidence_id: adopted-other
  kind: database
  reference: PMID:22510154; PMID:25142695; PMID:28550524
  locator: PubMed/PMC metadata and inspected abstracts; https://pmc.ncbi.nlm.nih.gov/articles/PMC4192562/
    ; https://pubmed.ncbi.nlm.nih.gov/28550524/
  accessed_at: '2026-10-21T06:59:19Z'
  support: context_only
  summary: Ahuja2012 DOI10.1021/ja3016395 is a biosynthesis lead whose full text was
    blocked. Gerke/Braus2014 is a secondary review of fungal developmental regulation,
    not independent activity evidence. The2017 Pestalotiopsis fici abstract concerns
    PfCsnE regulation and named other metabolites; its abstract alone does not establish
    this exact compound as a P.fici product.
- evidence_id: search-boundary
  kind: search
  reference: Exact compound and adopted citation searches
  locator: ChEBI, PubMed/PMC, publisher and institutional full text
  accessed_at: '2026-10-21T06:59:19Z'
  support: context_only
  summary: Exact chemical name and structure were prioritized over DHMBA acronym matches.
    Newer benzaldehyde quorum-sensing literature was a discovery lead, but no target-specific
    mechanism claim is adopted from it. Commercial mechanism summaries were not used.
  search_scope: Exact full name, DHMBA plus antibacterial/mechanism, four adopted
    PMIDs, DOI10.1128/AEM.01808-12 and later dba biosynthesis papers. No paid research
    used.
- evidence_id: validation
  kind: validation
  reference: just validate; just validate-strict
  locator: New isolated worktree002; /private/tmp/am-review-session/014-validation.tsv
  accessed_at: '2026-10-21T06:59:19Z'
  support: supports
  summary: Both focused commands exited0. LinkML reported no issues; strict scanned1
    target with0 ERROR rows.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral compound
  outcome: supported
  summary: Official structure and primary Figure3B agree; chemical parents are appropriately
    broader classifications. Acronym alone is not an identity match.
  target_ids:
  - CHEBI:155860
  evidence_ids:
  - record
  - chebi
  - gerke2012
- assessment_id: classification
  area: grounding
  topic: Antibacterial filing
  outcome: supported
  summary: Official role and direct exact-compound activity justify ANTIBACTERIAL.
    The bounded assay does not establish broad clinical or species-wide efficacy.
  target_ids:
  - CHEBI:155860
  evidence_ids:
  - config
  - chebi
  - gerke2012
- assessment_id: activity
  area: completeness
  topic: Source-specific assay enrichment
  outcome: concern
  summary: A directly inspected source provides a quantitative activity observation
    suitable for scoped curation. Disk concentration inconsistency must be preserved
    or resolved independently.
  target_ids:
  - CHEBI:155860
  evidence_ids:
  - record
  - gerke2012
  - rubric
- assessment_id: producer
  area: completeness
  topic: Fungal production evidence
  outcome: concern
  summary: Primary isolation and later production experiments provide an actionable
    producer annotation. Preserve engineered or induced culture context; do not treat
    biosynthetic enzymes as drug targets.
  target_ids:
  - CHEBI:155860
  evidence_ids:
  - record
  - gerke2012
  - gerke2022
  - mibig
- assessment_id: mechanism
  area: evidence
  topic: Antibacterial molecular mechanism
  outcome: unknown
  summary: The inspected material supports activity and biosynthesis. It does not
    establish an antibacterial molecular target for exact DHMBA. Tropolone mechanisms
    cannot be transferred to this precursor; this bounded search does not prove no
    mechanism literature exists.
  target_ids:
  - CHEBI:155860
  evidence_ids:
  - record
  - gerke2012
  - gerke2022
  - search-boundary
- assessment_id: optional
  area: evidence
  topic: Other optional scientific objects
  outcome: not_applicable
  summary: No native resistance, clinical-use, dataset, causal-graph or protein-example
    assertions need correction. Their empty slots are not assigned blanket defects.
  target_ids:
  - CHEBI:155860
  evidence_ids:
  - record
  - rubric
- assessment_id: provenance
  area: provenance
  topic: Generated ownership and native status
  outcome: supported
  summary: Source identity and history agree, and SEEDED is appropriate. Citation
    leads require claim-level review before promotion.
  target_ids:
  - CHEBI:155860
  evidence_ids:
  - record
  - owner
  - rubric
- assessment_id: schema
  area: schema
  topic: Focused validation
  outcome: supported
  summary: Both focused validation gates pass.
  target_ids:
  - CHEBI:155860
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: chebi-155860-primary-activity-enrichment
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: The exact-compound microplate result is available for scoped activity curation
  description: The inspected primary paper supplies a concrete activity observation,
    while the current seed contains no activity_spectrum. This is an evidence-specific
    enrichment opportunity, not invalid optional-field absence. The conflicting disk
    concentrations preclude silently standardizing disk loading.
  target_ids:
  - CHEBI:155860
  field_paths:
  - activity_spectrum
  evidence_ids:
  - record
  - gerke2012
  - rubric
  rule_id: native-review-checklist:Activity and evidence scope
  native_severity: minor evidence-specific readiness gap
  normalization_reason: The current record asserts no false assay; a directly inspected
    source enables useful enrichment.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2-4-dihydroxy-3-methyl-6-2-oxopropyl-benzaldehyde.yaml
    role: Curator-owned scientific annotations; use native validated writer and curation
      event
- finding_id: F2
  issue_key: chebi-155860-producer-enrichment
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Primary isolation and induced-production data support producer annotation
  description: The seed lacks producer context despite directly inspected exact-compound
    biosynthesis evidence. Record the producing fungus with the experimental context;
    do not infer that a co-cultured bacterium produces this molecule or that a biosynthetic
    protein is its antibacterial target.
  target_ids:
  - CHEBI:155860
  field_paths:
  - producer_organisms
  evidence_ids:
  - record
  - gerke2012
  - gerke2022
  - chebi
  rule_id: native-review-checklist:Producer organisms
  native_severity: minor evidence-specific readiness gap
  normalization_reason: A specific producer enrichment is supported; no incorrect
    native producer claim is present.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2-4-dihydroxy-3-methyl-6-2-oxopropyl-benzaldehyde.yaml
    role: Curator-owned scientific annotations; use native validated writer and curation
      event
actions:
- action_id: A1
  description: Curate the reported microplate observation with organism grounding,
    endpoint, method and experimental conditions. Inspect supplemental strain metadata
    before assigning a strain. Retain the documented disk-dose discrepancy if adding
    the separate diffusion result.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:155860
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2-4-dihydroxy-3-methyl-6-2-oxopropyl-benzaldehyde.yaml
    role: Curator-owned scientific annotations; use native validated writer and curation
      event
  acceptance_checks:
  - Exact compound, original units, endpoint and primary locator remain traceable;
    no susceptible/resistant clinical category is invented.
  - Any disk loading is resolved from source evidence or explicitly left unresolved.
  - Use native validated writer and curation event; run strict, reproducibility and
    QC gates.
- action_id: A2
  description: Curate a source-backed Aspergillus nidulans producer entry with appropriate
    current taxon grounding and induced/engineered culture context. Keep biosynthetic
    pathway references separate from antibacterial mode and target fields.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:155860
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2-4-dihydroxy-3-methyl-6-2-oxopropyl-benzaldehyde.yaml
    role: Curator-owned scientific annotations; use native validated writer and curation
      event
  acceptance_checks:
  - Producer identity and culture context are traceable to primary evidence.
  - No derivative iron-chelation or biosynthetic-enzyme claim is transferred into
    the antibacterial mechanism.
  - Use native writer/history and focused strict, reproducibility and QC gates before
    native status promotion.
limitations:
- The2012 main paper and Figure3 were inspected, but supplemental strain/chemical
  data were not. The disk-loading discrepancy remains unresolved.
- The2012 Ahuja full text was access-limited; other adopted leads were secondary context
  or abstract-only. Bounded searches do not establish global absence of mechanism
  evidence.
- No paid research or native record edits occurred.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Provenance capture preceded assessment; expanded context preserved all initial hashes
  and base revision.
- Hidden and ignored files were included in all searches used to report local absence.
- The record remains SEEDED; future scientific enrichment requires native curation
  history and a separate readiness decision.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:155860
- https://mural.maynoothuniversity.ie/id/eprint/6246/1/OB-Breaking-Silence.pdf
- https://www.frontiersin.org/journals/fungal-biology/articles/10.3389/ffunb.2021.777474/full
tags:
- antibacterial
- polyketide
- seeded
- primary-activity
```
