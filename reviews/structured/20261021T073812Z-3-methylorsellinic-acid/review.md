# 3-Methylorsellinic acid: exact free-acid activity and scoped biosynthetic evidence

- Review: 20261021T073812Z-3-methylorsellinic-acid
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T07:26:58Z
- Finished UTC: 2026-10-21T07:38:12Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The neutral free-acid identity, provenance and antibacterial role are supported. Focused schema, strict and independent chemistry pass. One informational follow-up concerns optional exact-compound activity and qualified biosynthetic-source annotations. Neither a biosynthetic synthase nor the ester’s activity is an antibacterial molecular-target claim for this acid. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record and maintained provenance, official identity, all adopted PMID leads and a complete primary biosynthesis/activity study.

Selection: Queue index035: CHEBI:146309 at its locked native path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:146309 | data/antibiotics/antibacterial/3-methylorsellinic-acid.yaml | generated | 3-methylorsellinic acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Single-record LinkML validation | passed | True | CHEBI:146309 | No issues found. |
| Single-record strict validation | passed | True | CHEBI:146309 | Scanned1 file;0ERROR rows. |
| Independent native structure consistency | passed | False | CHEBI:146309 | SMILES and InChI reproduce the same key, formula, charge and rounded masses; no stereocentres. |
| Initial iModulonDB inventory request | failed | False | CHEBI:146309 | Initial sandboxed attempt failed DNS resolution; retained as history and followed by a successful authorized public-network retry. |
| iModulonDB inventory public-network retry | passed | False | CHEBI:146309 | Runner returned the complete inventory. It contains no Preussia or Saccharomyces dataset applicable to the biosynthetic gene/host context. |
| Expression-module applicability | not_applicable | False | CHEBI:146309 | The native record has no expression claim. The follow-up gene is a fungal biosynthetic enzyme and the demonstrated host is engineered yeast; neither organism is covered by the inspected inventory. Bacterial assay taxa alone do not create a gene/module claim. |
| Independent CAS registry access | unavailable | False | CHEBI:146309 | ChEBI records CAS4707-46-4, but direct CAS Common Chemistry was unavailable and its API returned401; no independent registry verification is claimed. |
| Authoritative full QC | failed | True | CHEBI:146309 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:146309 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:146309 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:146309 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:146309 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:146309 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:146309 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:146309 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:146309 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Free acid versus methyl ester and isomers

identity: supported. Targets: CHEBI:146309.

Native name, synonyms, definition and exact structure are coherent. Primary structure drawings agree and distinguish the ester.

### Class parents and registry assertion

grounding: supported. Targets: CHEBI:146309.

Both is_a parents are broader and appropriate. The sole CAS xref is a verified ChEBI assertion with independent registry access explicitly limited.

### Exact-compound antibacterial role

evidence: supported. Targets: CHEBI:146309.

The adopted primary abstract and complete later study support the free-acid antibacterial role. Pooled MIC ranges and later IC50 observations must remain distinct and strain-scoped.

### Biosynthetic mechanism versus antibacterial action

evidence: unknown. Targets: CHEBI:146309.

No native antibacterial mechanism is asserted. Production genetics establishes synthesis, not how the compound inhibits bacteria. Host neuroprotection and adjacent compounds provide no direct antimicrobial target.

### Optional biosynthetic production context

completeness: supported. Targets: CHEBI:146309.

Primary evidence offers a concrete production-curation path, with fungal gene origin and engineered host retained. Culture-based production and lichen-extract occurrence have different evidentiary strength.

### Resistance, clinical, graph and datasets

representation: not_applicable. Targets: CHEBI:146309.

No native objects require correction. Resistant-to-other-drug strain labels are assay context, and absent matching expression datasets do not negate synthesis or activity.

### Maintained source and native status

ownership: supported. Targets: CHEBI:146309.

Input hashes, row, version, mint and seeder history are coherent. SEEDED remains unchanged; optional evidence additions require native validated writer/history.

### Focused gates

schema: supported. Targets: CHEBI:146309.

Schema, strict and native chemistry pass; scientific evidence was assessed separately.

## Findings

### F1: Primary activity and production evidence offer optional scoped enrichment

informational / open / confirmed; issue key: chebi-146309-primary-activity-and-biosynthesis-followup.

Direct exact-compound activity and experimentally supported biosynthesis are available for a future curator. The seed does not assert false measurements or targets. Keep the free acid distinct from its ester, IC50 distinct from MIC, and production genetics distinct from antibacterial mechanism.

## Recommended Actions And Acceptance Checks

### A1

If selected for curation, add exact-compound activity and source-specific production evidence, retaining unresolved antibacterial mechanism and the distinction between native fungal biosynthetic capacity and engineered production.

- Preserve endpoint, inequality/approximation, tested concentration range and organism/strain context; retrieve delegated assay details before complete quantitative normalization.
- Do not assign a pooled six-compound MIC range to this acid or turn ester antifungal activity into free-acid activity.
- Verify producer taxon/strain and gene grounding against the primary experiment; do not label wild-type yeast a natural producer from a heterologous-expression result.
- Do not assign the synthase as an antibacterial molecular target or infer acid resistance from resistance labels for other drugs.
- Use write_validated_antibiotic plus native curation event for separately authorized additions; rerun focused schema/strict and required corpus gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/3-methylorsellinic-acid.yaml; Entire YAML, including definition, three synonyms, two parents, one role, one xref, structure and three seeder history events. | supports | The exact neutral2,4-dihydroxy-3,6-dimethylbenzoic acid is SEEDED/EXACT. No native activity_spectrum, mechanism, targets, producer, resistance, clinical, dataset, causal-graph or activity-collection objects are asserted. Optional empty slots are not required-field defects. |
| owner | data/raw/chebi_antimicrobials.tsv; CHEBI:146309 row2699; MANIFEST; PATHS; conf/sources.yaml; ChEBI extractor, source reader, build_record and mint in seeder. | supports | The full adopted row matches native identity, chemical strings, broader parents, antibacterial role and CAS xref. Its six PMIDs are leads; mechanism_role_ids is empty. The2026-08-30 version, deterministic minted ID antibioticmech:chebi-41a5693328 and three seeder events are coherent. Initial input hashes were rechecked unchanged. Imported identity is source-owned; scientific additions use the actual native record owner. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:146309; Official full compound page: structure, names, relations, source metadata and registry. | supports | The authority matches C9H10O4, charge0, mass182.175, exact mass182.05791 and key VHNLJRRECIZZPX-UHFFFAOYSA-N. CHEBI:23778 dihydroxybenzoic acid and33572 resorcinols are broader classes;33282 is antibacterial role. CAS4707-46-4 is listed. Functional parent o-orsellinic acid and conjugate base3-methylorsellinate are distinct, not exact equivalents. SecondaryID144202 and fungal-source metadata add context but do not create native producer assertions. |
| cas | https://commonchemistry.cas.org/detail?cas_rn=4707-46-4; Direct page, free /api/detail endpoint, and NIST identity route attempted. | context_only | No inspectable independent registry response was obtained; the CAS API returned401. Official ChEBI provides the retained source assertion. This access limitation is not evidence that the identifier is incorrect. |
| chemistry | RDKit2026.03.5; 035-chemistry-check.py and035-chemistry.json. | supports | Both native representations independently parse as one connected neutral achiral C9H10O4 molecule with identical full InChI/key, average mass182.175 and exact mass182.0579088. |
| adopted-literature | Europe PMC official API; 035-literature.json: PMID1155879,15307685,18494879,28029061,30469376,5531675 and available DOI/abstract metadata. | context_only | All six identifiers resolve. PMID15307685 explicitly includes the exact2,4-dihydroxy-3,6-dimethyl free acid among antibacterial compounds, but its reported MIC range pools six compounds and is not an exact acid/strain value. PMID1155879 reports production by P.spinulosum grown in glucose-containing Czapek-Dox medium. PMID28029061 identifies it in a lichen extract; its biosynthesis interpretation does not by itself identify the producing symbiont. PMID18494879 concerns atranorin synthesis/intermediates, and30469376 concerns host neuroprotection; neither establishes an antibacterial mechanism here. |
| esters1970 | DOI:10.1248/yakushi1947.90.12_1517; PMID5531675; official J-STAGE English abstract and first-page text https://www.jstage.jst.go.jp/article/yakushi1947/90/12/90_12_1517/_pdf. | context_only | The sake-preservation experiments describe orsellinic and beta-orcinolcarboxylic esters and olivetonide. Their reported comparative antibacterial potency is not adopted as direct evidence for this unesterified acid. |
| preu3 | PMID:35602042; DOI:10.3389/fmicb.2022.819086; official Europe PMC fullTextXML PMC9116485, complete main text; Figure3 andFigure5 images visually inspected. | supports | Compound3 is the exact free acid; compound4 is its methyl ester. OD620 growth assays report acid IC50&lt;6.25µg/mL against MRSA and MDR S.epidermidis, with bounded/approximate Enterococcus values. These are not MICs; Figure5 depicts tested doses rather than a fitted curve. Native fungal Preu3 expression in engineered S.cerevisiae BJ5464-NpgA produces compound3 versus empty-vector control, supporting a scoped biosynthetic annotation. It does not establish native wild-type yeast production or an antimicrobial target. Table1 acid fungal MICs are &gt;100µg/mL in seven tested fungi; ester activity differs. |
| figures | DOI:10.3389/fmicb.2022.819086; 035-figure3.webp and035-figure5.webp; official Frontiers images. | context_only | The production figure distinguishes the free-acid structure and control. The antibacterial figure separates compound3 from the ester and comparator; its S.epidermidis lowest-dose bar lies near50% inhibition. Preserve the reported inequality and graphical resolution rather than asserting a precisely fitted threshold. |
| adapter | https://imodulondb.org/api/datasets; Actual kg-microbe-sources runner;035-imodulondb-datasets.stderr and successful035-imodulondb-datasets-retry.txt. | context_only | The initial request failed network resolution; the authorized retry succeeded and lists28 dataset keys from bacterial/archaeal organisms. It has no Preussia isomera or Saccharomyces cerevisiae dataset. No covered matching organism was available for the fungal biosynthetic-gene context, so no term search or module summary was warranted. This is a coverage statement, not negative biological evidence. |
| search | CultureBotAI/AntibioticMech; 035-local-hits.txt;035-focused-local-hits.txt; bounded primary discovery. | context_only | The inclusive worktree search located source/generated/index/research references. Focused curation/reviews/historical-report/conf search returned no matches. Exact free-acid literature was distinguished from ester preservatives, depsides, biosynthetic products and mixtures. The search does not establish global evidence absence. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Identity, activity, producer, mechanism, evidence and status gates; docs/CURATION.md/HARMONIZATION.md. | supports | Optional omissions are not schema errors. Producer annotations mean biosynthesis and must retain natural versus engineered context. A biosynthetic enzyme is not an antibacterial target; activity against strains resistant to other antibiotics does not establish resistance to this acid. |
| validation | Documented focused validators; Actual worktree004 commands;035-validation.tsv. | supports | Both documented focused validators and independent native chemistry passed; shared repository checks are recorded separately with their actual outcomes. |

## Limits And Additional Notes

- CAS was verified through official ChEBI; independent CAS/NIST access did not yield inspectable identity data. No contradiction was established.
- Five adopted PMID abstracts and metadata for all six were inspected; the1970 publisher abstract concerns esters. Older primary full texts and the2022 supplementary DOCX were not comprehensively reviewed.
- The2022 complete main text and Figures3/5 were inspected. Bacterial strain accessions and detailed conditions are not supplied in its main assay description, which delegates methods to an earlier paper; precise normalization needs that follow-up.
- The iModulonDB runner initially failed DNS resolution, then succeeded via public-network retry. No covered organism matched the fungal-gene/engineered-yeast context.
- The search is bounded and does not establish universal absence of an antibacterial mechanism, resistance determinant, additional producer or further activity evidence.
- No native record edits or paid research occurred. This review does not promote native scientific status.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T073812Z-3-methylorsellinic-acid
kind: record
repository: CultureBotAI/AntibioticMech
title: '3-Methylorsellinic acid: exact free-acid activity and scoped biosynthetic
  evidence'
started_at: '2026-10-21T07:26:58Z'
finished_at: '2026-10-21T07:38:12Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or curate the target. Entire record,
    maintained source, authority identifiers, chemistry and primary experiments were
    inspected independently of generated pages and historical reports.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: The neutral free-acid identity, provenance and antibacterial role are supported.
  Focused schema, strict and independent chemistry pass. One informational follow-up
  concerns optional exact-compound activity and qualified biosynthetic-source annotations.
  Neither a biosynthetic synthase nor the ester’s activity is an antibacterial molecular-target
  claim for this acid. Scientific assessment retains the stated evidence limits; full
  verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/3-methylorsellinic-acid.yaml
    sha256: 4f86982ca8fedaf64c18cbd83d43d9a3f79cfc6fadf7b5dd75b028534467c070
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
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
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
- target_id: CHEBI:146309
  path: data/antibiotics/antibacterial/3-methylorsellinic-acid.yaml
  label: 3-methylorsellinic acid
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
  description: Entire exact native record and maintained provenance, official identity,
    all adopted PMID leads and a complete primary biosynthesis/activity study.
  selection: 'Queue index035: CHEBI:146309 at its locked native path.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:146309
  exclusions:
  - target: Methyl/ethyl3-methylorsellinate,3,5-dimethylorsellinic acid,orsellinic
      acid,lecanoric acid and depsides
    reason: Different chemicals or assembled products; antibacterial, antifungal and
      mechanism claims are not transferred to the exact free acid.
checks:
- check_id: schema
  name: Single-record LinkML validation
  status: passed
  required: true
  summary: No issues found.
  target_ids:
  - CHEBI:146309
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/3-methylorsellinic-acid.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Single-record strict validation
  status: passed
  required: true
  summary: Scanned1 file;0ERROR rows.
  target_ids:
  - CHEBI:146309
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/3-methylorsellinic-acid.yaml --out /private/tmp/am-review-session/035-validation.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: Independent native structure consistency
  status: passed
  required: false
  summary: SMILES and InChI reproduce the same key, formula, charge and rounded masses;
    no stereocentres.
  target_ids:
  - CHEBI:146309
  evidence_ids:
  - chemistry
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/035-chemistry-check.py
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-initial
  name: Initial iModulonDB inventory request
  status: failed
  required: false
  summary: Initial sandboxed attempt failed DNS resolution; retained as history and
    followed by a successful authorized public-network retry.
  target_ids:
  - CHEBI:146309
  evidence_ids:
  - adapter
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 datasets
  exit_code: 2
  expected_exit_code: 0
- check_id: adapter-retry
  name: iModulonDB inventory public-network retry
  status: passed
  required: false
  summary: Runner returned the complete inventory. It contains no Preussia or Saccharomyces
    dataset applicable to the biosynthetic gene/host context.
  target_ids:
  - CHEBI:146309
  evidence_ids:
  - adapter
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 datasets
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-scope
  name: Expression-module applicability
  status: not_applicable
  required: false
  summary: The native record has no expression claim. The follow-up gene is a fungal
    biosynthetic enzyme and the demonstrated host is engineered yeast; neither organism
    is covered by the inspected inventory. Bacterial assay taxa alone do not create
    a gene/module claim.
  target_ids:
  - CHEBI:146309
  evidence_ids:
  - adapter
  - preu3
- check_id: cas
  name: Independent CAS registry access
  status: unavailable
  required: false
  summary: ChEBI records CAS4707-46-4, but direct CAS Common Chemistry was unavailable
    and its API returned401; no independent registry verification is claimed.
  target_ids:
  - CHEBI:146309
  evidence_ids:
  - chebi
  - cas
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:146309
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
  - CHEBI:146309
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
  - CHEBI:146309
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
  - CHEBI:146309
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
  - CHEBI:146309
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
  - CHEBI:146309
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
  - CHEBI:146309
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
  - CHEBI:146309
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
  - CHEBI:146309
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/3-methylorsellinic-acid.yaml
  locator: Entire YAML, including definition, three synonyms, two parents, one role,
    one xref, structure and three seeder history events.
  accessed_at: '2026-10-21T07:30:43Z'
  support: supports
  summary: The exact neutral2,4-dihydroxy-3,6-dimethylbenzoic acid is SEEDED/EXACT.
    No native activity_spectrum, mechanism, targets, producer, resistance, clinical,
    dataset, causal-graph or activity-collection objects are asserted. Optional empty
    slots are not required-field defects.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: CHEBI:146309 row2699; MANIFEST; PATHS; conf/sources.yaml; ChEBI extractor,
    source reader, build_record and mint in seeder.
  accessed_at: '2026-10-21T07:30:43Z'
  support: supports
  summary: The full adopted row matches native identity, chemical strings, broader
    parents, antibacterial role and CAS xref. Its six PMIDs are leads; mechanism_role_ids
    is empty. The2026-08-30 version, deterministic minted ID antibioticmech:chebi-41a5693328
    and three seeder events are coherent. Initial input hashes were rechecked unchanged.
    Imported identity is source-owned; scientific additions use the actual native
    record owner.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:146309
  locator: 'Official full compound page: structure, names, relations, source metadata
    and registry.'
  accessed_at: '2026-10-21T07:30:43Z'
  support: supports
  summary: The authority matches C9H10O4, charge0, mass182.175, exact mass182.05791
    and key VHNLJRRECIZZPX-UHFFFAOYSA-N. CHEBI:23778 dihydroxybenzoic acid and33572
    resorcinols are broader classes;33282 is antibacterial role. CAS4707-46-4 is listed.
    Functional parent o-orsellinic acid and conjugate base3-methylorsellinate are
    distinct, not exact equivalents. SecondaryID144202 and fungal-source metadata
    add context but do not create native producer assertions.
- evidence_id: cas
  kind: database
  reference: https://commonchemistry.cas.org/detail?cas_rn=4707-46-4
  locator: Direct page, free /api/detail endpoint, and NIST identity route attempted.
  accessed_at: '2026-10-21T07:30:43Z'
  support: context_only
  summary: No inspectable independent registry response was obtained; the CAS API
    returned401. Official ChEBI provides the retained source assertion. This access
    limitation is not evidence that the identifier is incorrect.
- evidence_id: chemistry
  kind: validation
  reference: RDKit2026.03.5
  locator: 035-chemistry-check.py and035-chemistry.json.
  accessed_at: '2026-10-21T07:30:43Z'
  support: supports
  summary: Both native representations independently parse as one connected neutral
    achiral C9H10O4 molecule with identical full InChI/key, average mass182.175 and
    exact mass182.0579088.
  snapshot_sha256: b9a670c9ff38f55c3e7d0d1850bfd91e07b2dc961cb041b30879fe4c63badc7f
- evidence_id: adopted-literature
  kind: primary_source
  reference: Europe PMC official API
  locator: '035-literature.json: PMID1155879,15307685,18494879,28029061,30469376,5531675
    and available DOI/abstract metadata.'
  accessed_at: '2026-10-21T07:30:43Z'
  support: context_only
  summary: All six identifiers resolve. PMID15307685 explicitly includes the exact2,4-dihydroxy-3,6-dimethyl
    free acid among antibacterial compounds, but its reported MIC range pools six
    compounds and is not an exact acid/strain value. PMID1155879 reports production
    by P.spinulosum grown in glucose-containing Czapek-Dox medium. PMID28029061 identifies
    it in a lichen extract; its biosynthesis interpretation does not by itself identify
    the producing symbiont. PMID18494879 concerns atranorin synthesis/intermediates,
    and30469376 concerns host neuroprotection; neither establishes an antibacterial
    mechanism here.
- evidence_id: esters1970
  kind: primary_source
  reference: DOI:10.1248/yakushi1947.90.12_1517
  locator: PMID5531675; official J-STAGE English abstract and first-page text https://www.jstage.jst.go.jp/article/yakushi1947/90/12/90_12_1517/_pdf.
  accessed_at: '2026-10-21T07:30:43Z'
  support: context_only
  summary: The sake-preservation experiments describe orsellinic and beta-orcinolcarboxylic
    esters and olivetonide. Their reported comparative antibacterial potency is not
    adopted as direct evidence for this unesterified acid.
- evidence_id: preu3
  kind: primary_source
  reference: PMID:35602042
  locator: DOI:10.3389/fmicb.2022.819086; official Europe PMC fullTextXML PMC9116485,
    complete main text; Figure3 andFigure5 images visually inspected.
  accessed_at: '2026-10-21T07:30:43Z'
  support: supports
  summary: Compound3 is the exact free acid; compound4 is its methyl ester. OD620
    growth assays report acid IC50<6.25µg/mL against MRSA and MDR S.epidermidis, with
    bounded/approximate Enterococcus values. These are not MICs; Figure5 depicts tested
    doses rather than a fitted curve. Native fungal Preu3 expression in engineered
    S.cerevisiae BJ5464-NpgA produces compound3 versus empty-vector control, supporting
    a scoped biosynthetic annotation. It does not establish native wild-type yeast
    production or an antimicrobial target. Table1 acid fungal MICs are >100µg/mL in
    seven tested fungi; ester activity differs.
  snapshot_sha256: cec04ce9aad06f4e31568feebbf08cd951546af8213aec38093a9d6e798cd256
- evidence_id: figures
  kind: primary_source
  reference: DOI:10.3389/fmicb.2022.819086
  locator: 035-figure3.webp and035-figure5.webp; official Frontiers images.
  accessed_at: '2026-10-21T07:30:43Z'
  support: context_only
  summary: The production figure distinguishes the free-acid structure and control.
    The antibacterial figure separates compound3 from the ester and comparator; its
    S.epidermidis lowest-dose bar lies near50% inhibition. Preserve the reported inequality
    and graphical resolution rather than asserting a precisely fitted threshold.
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Actual kg-microbe-sources runner;035-imodulondb-datasets.stderr and successful035-imodulondb-datasets-retry.txt.
  accessed_at: '2026-10-21T07:30:43Z'
  support: context_only
  summary: The initial request failed network resolution; the authorized retry succeeded
    and lists28 dataset keys from bacterial/archaeal organisms. It has no Preussia
    isomera or Saccharomyces cerevisiae dataset. No covered matching organism was
    available for the fungal biosynthetic-gene context, so no term search or module
    summary was warranted. This is a coverage statement, not negative biological evidence.
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 035-local-hits.txt;035-focused-local-hits.txt; bounded primary discovery.
  accessed_at: '2026-10-21T07:30:43Z'
  support: context_only
  summary: The inclusive worktree search located source/generated/index/research references.
    Focused curation/reviews/historical-report/conf search returned no matches. Exact
    free-acid literature was distinguished from ester preservatives, depsides, biosynthetic
    products and mixtures. The search does not establish global evidence absence.
  search_scope: rg --no-ignore --hidden exact identifier,label,slug across worktree004
    except .git/.venv; focused146309,VHNLJRRECIZZPX,3-methylorsellinic,orcinolcarboxylic
    in curation reviews reports/yaml_record_review conf excluding queue/lockfiles.
    Public exact-name and beta-orcinolcarboxylic acid antibacterial/mechanism searches;
    all six source PMIDs and full2022 primary. Ignored files included.
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Identity, activity, producer, mechanism, evidence and status gates; docs/CURATION.md/HARMONIZATION.md.
  accessed_at: '2026-10-21T07:30:43Z'
  support: supports
  summary: Optional omissions are not schema errors. Producer annotations mean biosynthesis
    and must retain natural versus engineered context. A biosynthetic enzyme is not
    an antibacterial target; activity against strains resistant to other antibiotics
    does not establish resistance to this acid.
- evidence_id: validation
  kind: validation
  reference: Documented focused validators
  locator: Actual worktree004 commands;035-validation.tsv.
  accessed_at: '2026-10-21T07:30:43Z'
  support: supports
  summary: Both documented focused validators and independent native chemistry passed;
    shared repository checks are recorded separately with their actual outcomes.
assessments:
- assessment_id: identity
  area: identity
  topic: Free acid versus methyl ester and isomers
  outcome: supported
  summary: Native name, synonyms, definition and exact structure are coherent. Primary
    structure drawings agree and distinguish the ester.
  target_ids:
  - CHEBI:146309
  evidence_ids:
  - record
  - chebi
  - chemistry
  - preu3
  - figures
- assessment_id: grounding
  area: grounding
  topic: Class parents and registry assertion
  outcome: supported
  summary: Both is_a parents are broader and appropriate. The sole CAS xref is a verified
    ChEBI assertion with independent registry access explicitly limited.
  target_ids:
  - CHEBI:146309
  evidence_ids:
  - chebi
  - cas
- assessment_id: activity
  area: evidence
  topic: Exact-compound antibacterial role
  outcome: supported
  summary: The adopted primary abstract and complete later study support the free-acid
    antibacterial role. Pooled MIC ranges and later IC50 observations must remain
    distinct and strain-scoped.
  target_ids:
  - CHEBI:146309
  evidence_ids:
  - adopted-literature
  - preu3
  - esters1970
- assessment_id: mechanism
  area: evidence
  topic: Biosynthetic mechanism versus antibacterial action
  outcome: unknown
  summary: No native antibacterial mechanism is asserted. Production genetics establishes
    synthesis, not how the compound inhibits bacteria. Host neuroprotection and adjacent
    compounds provide no direct antimicrobial target.
  target_ids:
  - CHEBI:146309
  evidence_ids:
  - record
  - preu3
  - adopted-literature
  - rubric
- assessment_id: producer
  area: completeness
  topic: Optional biosynthetic production context
  outcome: supported
  summary: Primary evidence offers a concrete production-curation path, with fungal
    gene origin and engineered host retained. Culture-based production and lichen-extract
    occurrence have different evidentiary strength.
  target_ids:
  - CHEBI:146309
  evidence_ids:
  - record
  - adopted-literature
  - preu3
  - rubric
- assessment_id: other
  area: representation
  topic: Resistance, clinical, graph and datasets
  outcome: not_applicable
  summary: No native objects require correction. Resistant-to-other-drug strain labels
    are assay context, and absent matching expression datasets do not negate synthesis
    or activity.
  target_ids:
  - CHEBI:146309
  evidence_ids:
  - record
  - adapter
  - rubric
- assessment_id: provenance
  area: ownership
  topic: Maintained source and native status
  outcome: supported
  summary: Input hashes, row, version, mint and seeder history are coherent. SEEDED
    remains unchanged; optional evidence additions require native validated writer/history.
  target_ids:
  - CHEBI:146309
  evidence_ids:
  - record
  - owner
  - rubric
- assessment_id: schema
  area: schema
  topic: Focused gates
  outcome: supported
  summary: Schema, strict and native chemistry pass; scientific evidence was assessed
    separately.
  target_ids:
  - CHEBI:146309
  evidence_ids:
  - validation
  - chemistry
findings:
- finding_id: F1
  issue_key: chebi-146309-primary-activity-and-biosynthesis-followup
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Primary activity and production evidence offer optional scoped enrichment
  description: Direct exact-compound activity and experimentally supported biosynthesis
    are available for a future curator. The seed does not assert false measurements
    or targets. Keep the free acid distinct from its ester, IC50 distinct from MIC,
    and production genetics distinct from antibacterial mechanism.
  target_ids:
  - CHEBI:146309
  field_paths:
  - activity_spectrum
  - producer_organisms
  - evidence
  - mode_of_action_notes
  evidence_ids:
  - record
  - adopted-literature
  - preu3
  - figures
  - rubric
  rule_id: 'native-review-checklist: Activity, Producers and Mode of action'
  native_severity: informational optional evidence enrichment
  normalization_reason: No required-field omission or false current quantitative/mechanistic
    claim is established.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/3-methylorsellinic-acid.yaml
    role: Curator-owned scientific additions through write_validated_antibiotic and
      a native curation event
actions:
- action_id: A1
  description: If selected for curation, add exact-compound activity and source-specific
    production evidence, retaining unresolved antibacterial mechanism and the distinction
    between native fungal biosynthetic capacity and engineered production.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:146309
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/3-methylorsellinic-acid.yaml
    role: Curator-owned scientific additions through write_validated_antibiotic and
      a native curation event
  acceptance_checks:
  - Preserve endpoint, inequality/approximation, tested concentration range and organism/strain
    context; retrieve delegated assay details before complete quantitative normalization.
  - Do not assign a pooled six-compound MIC range to this acid or turn ester antifungal
    activity into free-acid activity.
  - Verify producer taxon/strain and gene grounding against the primary experiment;
    do not label wild-type yeast a natural producer from a heterologous-expression
    result.
  - Do not assign the synthase as an antibacterial molecular target or infer acid
    resistance from resistance labels for other drugs.
  - Use write_validated_antibiotic plus native curation event for separately authorized
    additions; rerun focused schema/strict and required corpus gates.
limitations:
- CAS was verified through official ChEBI; independent CAS/NIST access did not yield
  inspectable identity data. No contradiction was established.
- Five adopted PMID abstracts and metadata for all six were inspected; the1970 publisher
  abstract concerns esters. Older primary full texts and the2022 supplementary DOCX
  were not comprehensively reviewed.
- The2022 complete main text and Figures3/5 were inspected. Bacterial strain accessions
  and detailed conditions are not supplied in its main assay description, which delegates
  methods to an earlier paper; precise normalization needs that follow-up.
- The iModulonDB runner initially failed DNS resolution, then succeeded via public-network
  retry. No covered organism matched the fungal-gene/engineered-yeast context.
- The search is bounded and does not establish universal absence of an antibacterial
  mechanism, resistance determinant, additional producer or further activity evidence.
- No native record edits or paid research occurred. This review does not promote native
  scientific status.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
