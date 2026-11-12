# Review of CHEBI:143030 (schleiferon A)

- Review: 20261021T073910Z-chebi-143030-schleiferon-a-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T07:30:49Z
- Finished UTC: 2026-10-21T07:39:10Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The neutral schleiferon A structure, source grounding and antibacterial filing agree with current ChEBI and the original structure figure. One minor completeness finding identifies compound-specific MIC and phenotype evidence for curation. Whole volatile mixtures, the oxidized B congener, and precursor-producing communities require separate scope. Direct antibacterial targets remain unresolved; the displayed Northern blot is for B, not A.

## Scope And Provenance

Entire record, maintained source/ownership, current official identifiers and chemistry, discovery paper reprint and supplement, reported MICs and signalling assays, and full extracellular-formation study.

Selection: Path-ordered unreviewed queue index 038; exactly one record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:143030 | data/antibiotics/antibacterial/3-phenethylamino-butan-2-one.yaml | generated | 3-(phenethylamino)-butan-2-one |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented per-record LinkML validation | passed | True | CHEBI:143030 | Exit 0; No issues found. |
| Documented per-record closed-schema validation | passed | True | CHEBI:143030 | Exit 0; one file, zero ERROR rows. |
| Independent structure and minted-identifier comparison | passed | False | CHEBI:143030 | Both structure encodings and all stored molecular metadata agree. |
| Current source term, parent, role and structure comparison | passed | False | CHEBI:143030 | All current source term, parent, role and structural assertions pass. |
| Structured expression-module adapter applicability | not_applicable | False | CHEBI:143030 | The current record names no gene, protein, regulator, pathway, stress response or transcriptomic dataset. The chemical identity and producer species do not supply a gene/module query; genes encountered in literature are uncurated research context. |
| Authoritative full QC | failed | True | CHEBI:143030 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:143030 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:143030 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:143030 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:143030 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:143030 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:143030 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:143030 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:143030 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Schleiferon A constitution and congener boundary

identity: supported. Targets: CHEBI:143030.

Neutral phenethylamino A is confirmed by the original drawn structure. Shortened phenylamino wording in the abstracts is inconsistent with that figure and does not justify changing the record. B is a distinct imino oxidation product; no stereochemical assignment is established.

### Current parents, aliases and source concept

grounding: supported. Targets: CHEBI:143030.

Four direct broader classes and antibacterial role resolve and fit. The source identity and mint reproduce; no external exact chemical xref is present.

### Antibacterial class and compound-specific activity

evidence: supported. Targets: CHEBI:143030.

Synthetic A inhibits growth in the primary study. Its molar MIC values are independent of whole-headspace assays and of phenotype suppression at non-growth-inhibitory concentrations.

### Available exact-compound primary evidence

completeness: concern. Targets: CHEBI:143030.

The current broad seed can be enriched with assay-resolved evidence. Missing optional fields are not intrinsically errors; this finding concerns concrete newly verified evidence.

### Phenotypic signalling changes versus direct target

scope: unknown. Targets: CHEBI:143030.

Gram-positive growth-inhibitory mechanism remains explicitly unresolved. Quorum-dependent phenotypes, mutant response and receptor assays do not justify naming a direct target. Figure 6 demonstrates B-specific blot evidence, and cannot substantiate A-specific PigP/PigS binding or expression claims. Native REVIEWED molecular-mode work remains incomplete.

### Biological source and extracellular synthesis

representation: supported. Targets: CHEBI:143030.

The definition broadly agrees with emission from S. schleiferi cultures. Any structured producer curation must preserve strain, precursor and extracellular reaction context. The two-species experiment cannot be flattened into two independent final-compound producers.

### Relative sensitivity versus acquired resistance

scope: unknown. Targets: CHEBI:143030.

Higher MIC in some producing strains supports a relative-susceptibility observation only. No clinical resistance classification or genetic self-resistance mechanism is established.

### Clinical, graph and dataset objects

representation: not_applicable. Targets: CHEBI:143030.

No such objects are asserted. Prospective therapeutic interest does not establish clinical efficacy or require invented fields.

### Source-owned fields and audit trail

ownership: supported. Targets: CHEBI:143030.

The maintained source reproduces the seed and three history events are consistent. Evidence enrichment belongs to curator-owned annotations with proper history, not a hand-edited source identity.

### Native and independent validation

schema: supported. Targets: CHEBI:143030.

Both native validators and independent chemical/source comparisons pass. Their success does not resolve the mechanistic gap.

## Findings

### F1: Compound-specific primary activity and source context can be represented

minor / open / confirmed; issue key: chebi-143030-primary-activity-scope-evidence-completeness.

The original reprint supplies individually tested schleiferon A MICs and phenotype experiments that the broad seed does not represent. Curating this evidence would clarify assay, congener and producer scope. No incorrect structure or antibacterial filing is established.

## Recommended Actions And Acceptance Checks

### A1

In a separately authorized curation pass, attach narrow A-specific primary activity evidence and discuss phenotype/mechanism and extracellular source boundaries.

- Use Figure 2A for compound mapping and Table 1 column A for reported MICs in µM; retain strain, medium, incubation and readout. Do not conflate B, whole VOC mixtures, vapour exposure and directly added synthetic A.
- Preserve the MIC-method incubation at 37 C and the separate 30 C growth experiments; do not silently harmonize them. Do not derive clinical susceptibility categories or a universal Gram-negative inactivity claim: Table 1 reports a high but finite A MIC for S. enterica RV4.
- Describe prodigiosin/bioluminescence suppression at the measured phenotype level. Figure 6 is labelled B, not A; do not transfer its blot result to A or infer binding to PigP/PigS/Lux proteins.
- Retain S. schleiferi strain/culture context. Add producer_organisms only with appropriately scoped biosynthetic support; the 2018 split-headspace precursor producers are not individually demonstrated sources of finished A.
- Preserve unassigned stereochemistry. Apply validated writer and curation history, then just validate, just validate-strict, just verify-corpus --summary and just qc; leave native REVIEWED criteria unresolved until satisfied.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/3-phenethylamino-butan-2-one.yaml; Entire generated record | supports | Read the definition, both synonyms, four parents, role, chemical fields, one source concept and three seed/reseed events. No external chemical xrefs, primary evidence, targets, mode, activity observations, producer object, resistance, clinical, graph or dataset object is asserted. |
| inventory | data/raw/chebi_antimicrobials.tsv; Full CHEBI:143030 row, header and source manifest | supports | The adopted row matches imported identity, structure, parents and antibacterial role. It provides PMID:27720237 and PMID:30442919 citation leads and no mechanism-role data. Ignored-inclusive searches of maintained curation/conf inputs found no exact-ID or alias override. |
| ownership | scripts/extract_source_inventory.py; ChEBI extraction and scripts/seed_from_sources.py source structure, mint and curator merge | supports | Source identity belongs to the maintained inventory and generation transform; primary citations are leads rather than blanket evidence. Additional scientific annotations are curator-owned through the validated writer with history. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:143030; Current native ChEBI entry; 038-chebi.html | supports | The entry matches the label, schleiferon A alias, definition, neutral formula, masses, SMILES, InChI and key. It has one unspecified stereocentre, with no racemic composition asserted. |
| ontology | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_143030; 038-ols.json; 038-parents.json and 038-has_role.json | supports | The non-obsolete term and four direct parents resolve: volatile organic compound, benzenes, secondary amino compound and methyl ketone. The antibacterial-agent role resolves. No external exact chemical xref needs verification. |
| primary2016 | PMID:27720237; DOI:10.1016/j.syapm.2016.08.008; original journal reprint pp.503-515 within author thesis pp.69-81 at https://rosdok.uni-rostock.de/file/rosdok_disshab_0000001699/rosdok_derivate_0000036821/Dissertation_Lemfack_2017.pdf; OCR plus visual checks of pp.504/505/508/512 | supports | Figure 2A visibly identifies phenethylamino schleiferon A, distinct from imino B. Separate synthetic A experiments support Table 1 MICs: C. jeikeium V12209 and C. striatum RV2 34.8 µM, S. epidermidis RP62A 69.6 µM, and S. enterica RV4 4450 µM. MIC methods specify 4 mL cultures, initial OD600 0.005, DMSO control, 37 C incubation and 20-hour CFU/OD readout. These are distinct from volatile-mixture exposure and 30 C growth experiments. |
| mechanism2016 | PMID:27720237; Same paper pp.509-513, Figures 5/6; thesis supplemental Figures S6/S7 pp.118-120 | supports | Synthetic A reduces prodigiosin and bioluminescence endpoints. The displayed Northern blot in Figure 6 is labelled schleiferon B, despite broader caption/abstract wording; do not transfer its gene-expression result to A. Receptor/LuxU phosphorylation assays show no significant stimulation, and luxO deletion does not abolish bioluminescence inhibition. These constrain the hypothesis but establish no direct A target or Gram-positive growth-inhibition mechanism. |
| formation2018 | PMID:30442919; DOI:10.1038/s41598-018-35341-3; complete 038-primary2018.xml and corrected PDF; Results/Methods/Figure 1 | supports | GC/MS using synthetic standards detects A/B after joining separately cultivated S. plymuthica 4Rx13 and S. delphini DSMZ 20771 headspaces. Individual controls yield only respective precursors, acetoin and phenylethylamine. The work supports extracellular nonenzymatic formation, not independent production of finished A by each species, and does not itself provide a new A-specific susceptibility assay. |
| correction | PMID:30804355; https://pmc.ncbi.nlm.nih.gov/articles/PMC6389958/; DOI:10.1038/s41598-018-37081-w | context_only | Inspected correction states that erroneous symbols above Figure 2a were introduced in PDF production and corrected; the HTML was already correct. It does not retract the formation experiment. |
| chemistry | RDKit and hashlib calculations; 038-chemistry.py and 038-chemistry.json | supports | Both encodings yield WGOUDWYOCIOVMG-UHFFFAOYSA-N, C12H17NO, charge zero, one fragment, average mass 191.274 and exact mass 191.131014164; one centre is unassigned. The source-concept mint reproduces. |
| source-check | Focused official-source assertions; 038-source-check.py and 038-source-check.json | supports | Native-page SMILES and OLS InChI/SMILES/key, synonym strings and all asserted parents/role match. A charged conjugate returned among related terms was not adopted as an exact identity. |
| validation | just validate; just validate-strict; Actual isolated batch-004 executions; 038-strict.tsv | supports | Both native per-record validators exited 0; strict validation scanned one record with zero ERROR rows. |
| search | Ignored-inclusive local and bounded free web discovery; 038-local-hits.txt; official ontology, PubMed/EPMC, publisher, author-thesis and exact-compound searches | context_only | The original reprint resolves compound identity and assay mapping beyond the abstracts. No direct growth-inhibitory target for A was established in the inspected primary studies. No prediction or adjacent-compound result was adopted. |

## Limits And Additional Notes

- The discovery paper was inspected as an original scanned reprint within the author institutional thesis. OCR supplied searchable text; the title/DOI, structure/Table 1, MIC methods and Figure 6 were also checked visually. The entire thesis was not treated as one primary experiment.
- The 2018 XML/PDF and its correction were read. Its formation mechanism describes extracellular chemical production, not an antimicrobial molecular target or a new compound-resolved growth assay.
- Absolute configuration of the one stereocentre was not established in the inspected sources. The record encodes unspecified stereochemistry rather than a proven racemic composition.
- The primary text sometimes generalizes across A/B, while its displayed Northern blot specifically labels B. This distinction is retained; no A-specific gene-expression or binding claim was adopted from that blot.
- Bounded searching did not establish the growth-inhibitory molecular mode. This is not a universal absence claim, and no paid provider or unpublished synthesis work was accessed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Only scratch review artifacts were written. No native record, maintained input, generated artifact or curation history was modified.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T073910Z-chebi-143030-schleiferon-a-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of CHEBI:143030 (schleiferon A)
started_at: '2026-10-21T07:30:49Z'
finished_at: '2026-10-21T07:39:10Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Identity and antibacterial activity supported; bounded primary-evidence
  enrichment remains and growth-inhibitory molecular mode is unresolved
scientific_review: true
summary: The neutral schleiferon A structure, source grounding and antibacterial filing
  agree with current ChEBI and the original structure figure. One minor completeness
  finding identifies compound-specific MIC and phenotype evidence for curation. Whole
  volatile mixtures, the oxidized B congener, and precursor-producing communities
  require separate scope. Direct antibacterial targets remain unresolved; the displayed
  Northern blot is for B, not A.
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
  - path: data/antibiotics/antibacterial/3-phenethylamino-butan-2-one.yaml
    sha256: 05aeb9ed670553c30298c47a43fc7759e36c52c3ba0fa496727e8fcfc7b9ccb2
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
  description: Entire record, maintained source/ownership, current official identifiers
    and chemistry, discovery paper reprint and supplement, reported MICs and signalling
    assays, and full extracellular-formation study.
  selection: Path-ordered unreviewed queue index 038; exactly one record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:143030
targets:
- target_id: CHEBI:143030
  path: data/antibiotics/antibacterial/3-phenethylamino-butan-2-one.yaml
  label: 3-(phenethylamino)-butan-2-one
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
  name: Documented per-record LinkML validation
  status: passed
  required: true
  summary: Exit 0; No issues found.
  target_ids:
  - CHEBI:143030
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/3-phenethylamino-butan-2-one.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented per-record closed-schema validation
  status: passed
  required: true
  summary: Exit 0; one file, zero ERROR rows.
  target_ids:
  - CHEBI:143030
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/3-phenethylamino-butan-2-one.yaml --out /private/tmp/am-review-session/038-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Independent structure and minted-identifier comparison
  status: passed
  required: false
  summary: Both structure encodings and all stored molecular metadata agree.
  target_ids:
  - CHEBI:143030
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/038-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: source-check
  name: Current source term, parent, role and structure comparison
  status: passed
  required: false
  summary: All current source term, parent, role and structural assertions pass.
  target_ids:
  - CHEBI:143030
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/038-source-check.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ontology
  - source-check
- check_id: imodulondb
  name: Structured expression-module adapter applicability
  status: not_applicable
  required: false
  summary: The current record names no gene, protein, regulator, pathway, stress response
    or transcriptomic dataset. The chemical identity and producer species do not supply
    a gene/module query; genes encountered in literature are uncurated research context.
  target_ids:
  - CHEBI:143030
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
  - CHEBI:143030
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
  - CHEBI:143030
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
  - CHEBI:143030
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
  - CHEBI:143030
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
  - CHEBI:143030
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
  - CHEBI:143030
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
  - CHEBI:143030
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
  - CHEBI:143030
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
  - CHEBI:143030
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/3-phenethylamino-butan-2-one.yaml
  locator: Entire generated record
  accessed_at: '2026-10-21T07:34:10Z'
  support: supports
  summary: Read the definition, both synonyms, four parents, role, chemical fields,
    one source concept and three seed/reseed events. No external chemical xrefs, primary
    evidence, targets, mode, activity observations, producer object, resistance, clinical,
    graph or dataset object is asserted.
- evidence_id: inventory
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Full CHEBI:143030 row, header and source manifest
  accessed_at: '2026-10-21T07:34:10Z'
  support: supports
  summary: The adopted row matches imported identity, structure, parents and antibacterial
    role. It provides PMID:27720237 and PMID:30442919 citation leads and no mechanism-role
    data. Ignored-inclusive searches of maintained curation/conf inputs found no exact-ID
    or alias override.
- evidence_id: ownership
  kind: record_content
  reference: scripts/extract_source_inventory.py
  locator: ChEBI extraction and scripts/seed_from_sources.py source structure, mint
    and curator merge
  accessed_at: '2026-10-21T07:34:10Z'
  support: supports
  summary: Source identity belongs to the maintained inventory and generation transform;
    primary citations are leads rather than blanket evidence. Additional scientific
    annotations are curator-owned through the validated writer with history.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:143030
  locator: Current native ChEBI entry; 038-chebi.html
  accessed_at: '2026-10-21T07:34:10Z'
  support: supports
  summary: The entry matches the label, schleiferon A alias, definition, neutral formula,
    masses, SMILES, InChI and key. It has one unspecified stereocentre, with no racemic
    composition asserted.
  snapshot_sha256: 129d24f6b958c60eddd0f741bac3c1ca023098608af62f14b8659b32c1773c94
- evidence_id: ontology
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_143030
  locator: 038-ols.json; 038-parents.json and 038-has_role.json
  accessed_at: '2026-10-21T07:34:10Z'
  support: supports
  summary: 'The non-obsolete term and four direct parents resolve: volatile organic
    compound, benzenes, secondary amino compound and methyl ketone. The antibacterial-agent
    role resolves. No external exact chemical xref needs verification.'
  snapshot_sha256: c4fc521e70b1a25daaf0b8249b8800ca63c03d8afe0497f7cda42c338d5fed07
- evidence_id: primary2016
  kind: primary_source
  reference: PMID:27720237
  locator: DOI:10.1016/j.syapm.2016.08.008; original journal reprint pp.503-515 within
    author thesis pp.69-81 at https://rosdok.uni-rostock.de/file/rosdok_disshab_0000001699/rosdok_derivate_0000036821/Dissertation_Lemfack_2017.pdf;
    OCR plus visual checks of pp.504/505/508/512
  accessed_at: '2026-10-21T07:34:10Z'
  support: supports
  summary: 'Figure 2A visibly identifies phenethylamino schleiferon A, distinct from
    imino B. Separate synthetic A experiments support Table 1 MICs: C. jeikeium V12209
    and C. striatum RV2 34.8 µM, S. epidermidis RP62A 69.6 µM, and S. enterica RV4
    4450 µM. MIC methods specify 4 mL cultures, initial OD600 0.005, DMSO control,
    37 C incubation and 20-hour CFU/OD readout. These are distinct from volatile-mixture
    exposure and 30 C growth experiments.'
  snapshot_sha256: be3c37722d28437a8f5aa03f6ebe27da28567442f5cfa3ad3ce7f60faddbdce9
- evidence_id: mechanism2016
  kind: primary_source
  reference: PMID:27720237
  locator: Same paper pp.509-513, Figures 5/6; thesis supplemental Figures S6/S7 pp.118-120
  accessed_at: '2026-10-21T07:34:10Z'
  support: supports
  summary: Synthetic A reduces prodigiosin and bioluminescence endpoints. The displayed
    Northern blot in Figure 6 is labelled schleiferon B, despite broader caption/abstract
    wording; do not transfer its gene-expression result to A. Receptor/LuxU phosphorylation
    assays show no significant stimulation, and luxO deletion does not abolish bioluminescence
    inhibition. These constrain the hypothesis but establish no direct A target or
    Gram-positive growth-inhibition mechanism.
- evidence_id: formation2018
  kind: primary_source
  reference: PMID:30442919
  locator: DOI:10.1038/s41598-018-35341-3; complete 038-primary2018.xml and corrected
    PDF; Results/Methods/Figure 1
  accessed_at: '2026-10-21T07:34:10Z'
  support: supports
  summary: GC/MS using synthetic standards detects A/B after joining separately cultivated
    S. plymuthica 4Rx13 and S. delphini DSMZ 20771 headspaces. Individual controls
    yield only respective precursors, acetoin and phenylethylamine. The work supports
    extracellular nonenzymatic formation, not independent production of finished A
    by each species, and does not itself provide a new A-specific susceptibility assay.
  snapshot_sha256: 760df2339486cd7b8bbe37010ad8dd9b2c5159ab3985904ac188c303209c65b3
- evidence_id: correction
  kind: primary_source
  reference: PMID:30804355
  locator: https://pmc.ncbi.nlm.nih.gov/articles/PMC6389958/; DOI:10.1038/s41598-018-37081-w
  accessed_at: '2026-10-21T07:34:10Z'
  support: context_only
  summary: Inspected correction states that erroneous symbols above Figure 2a were
    introduced in PDF production and corrected; the HTML was already correct. It does
    not retract the formation experiment.
- evidence_id: chemistry
  kind: validation
  reference: RDKit and hashlib calculations
  locator: 038-chemistry.py and 038-chemistry.json
  accessed_at: '2026-10-21T07:34:10Z'
  support: supports
  summary: Both encodings yield WGOUDWYOCIOVMG-UHFFFAOYSA-N, C12H17NO, charge zero,
    one fragment, average mass 191.274 and exact mass 191.131014164; one centre is
    unassigned. The source-concept mint reproduces.
  snapshot_sha256: e72d3ae949c25074472f74dbe138edbd11282e9034ceefaf4bb1a168c488f3ee
- evidence_id: source-check
  kind: validation
  reference: Focused official-source assertions
  locator: 038-source-check.py and 038-source-check.json
  accessed_at: '2026-10-21T07:34:10Z'
  support: supports
  summary: Native-page SMILES and OLS InChI/SMILES/key, synonym strings and all asserted
    parents/role match. A charged conjugate returned among related terms was not adopted
    as an exact identity.
  snapshot_sha256: baed3f0da795f5a5aff289eab8883ee23d9cc04907d939aea40d70efcb9fa6ca
- evidence_id: validation
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual isolated batch-004 executions; 038-strict.tsv
  accessed_at: '2026-10-21T07:34:10Z'
  support: supports
  summary: Both native per-record validators exited 0; strict validation scanned one
    record with zero ERROR rows.
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local and bounded free web discovery
  locator: 038-local-hits.txt; official ontology, PubMed/EPMC, publisher, author-thesis
    and exact-compound searches
  accessed_at: '2026-10-21T07:34:10Z'
  support: context_only
  summary: The original reprint resolves compound identity and assay mapping beyond
    the abstracts. No direct growth-inhibitory target for A was established in the
    inspected primary studies. No prediction or adjacent-compound result was adopted.
  search_scope: prepare.py 38 searched identifier, label and slug using rg --no-ignore
    --hidden, excluding only .git and .venv. Follow-up searches examined maintained
    tables/conf and legacy review directory for CHEBI:143030, its minted ID and schleiferon.
    Free web queries included schleiferon A antibacterial mechanism, exact systematic
    name, PMID:27720237 and the interspecific-formation correction. Current ChEBI/OLS,
    discovery metadata, author-hosted reprint and supplement, full 2018 XML/PDF and
    2019 correction were inspected.
assessments:
- assessment_id: identity
  area: identity
  topic: Schleiferon A constitution and congener boundary
  outcome: supported
  summary: Neutral phenethylamino A is confirmed by the original drawn structure.
    Shortened phenylamino wording in the abstracts is inconsistent with that figure
    and does not justify changing the record. B is a distinct imino oxidation product;
    no stereochemical assignment is established.
  target_ids:
  - CHEBI:143030
  evidence_ids:
  - record
  - chebi
  - primary2016
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Current parents, aliases and source concept
  outcome: supported
  summary: Four direct broader classes and antibacterial role resolve and fit. The
    source identity and mint reproduce; no external exact chemical xref is present.
  target_ids:
  - CHEBI:143030
  evidence_ids:
  - ontology
  - source-check
  - chemistry
- assessment_id: classification
  area: evidence
  topic: Antibacterial class and compound-specific activity
  outcome: supported
  summary: Synthetic A inhibits growth in the primary study. Its molar MIC values
    are independent of whole-headspace assays and of phenotype suppression at non-growth-inhibitory
    concentrations.
  target_ids:
  - CHEBI:143030
  evidence_ids:
  - primary2016
  - mechanism2016
- assessment_id: activity
  area: completeness
  topic: Available exact-compound primary evidence
  outcome: concern
  summary: The current broad seed can be enriched with assay-resolved evidence. Missing
    optional fields are not intrinsically errors; this finding concerns concrete newly
    verified evidence.
  target_ids:
  - CHEBI:143030
  evidence_ids:
  - record
  - primary2016
- assessment_id: mechanism
  area: scope
  topic: Phenotypic signalling changes versus direct target
  outcome: unknown
  summary: Gram-positive growth-inhibitory mechanism remains explicitly unresolved.
    Quorum-dependent phenotypes, mutant response and receptor assays do not justify
    naming a direct target. Figure 6 demonstrates B-specific blot evidence, and cannot
    substantiate A-specific PigP/PigS binding or expression claims. Native REVIEWED
    molecular-mode work remains incomplete.
  target_ids:
  - CHEBI:143030
  evidence_ids:
  - mechanism2016
  - search
- assessment_id: producer
  area: representation
  topic: Biological source and extracellular synthesis
  outcome: supported
  summary: The definition broadly agrees with emission from S. schleiferi cultures.
    Any structured producer curation must preserve strain, precursor and extracellular
    reaction context. The two-species experiment cannot be flattened into two independent
    final-compound producers.
  target_ids:
  - CHEBI:143030
  evidence_ids:
  - record
  - primary2016
  - formation2018
- assessment_id: resistance
  area: scope
  topic: Relative sensitivity versus acquired resistance
  outcome: unknown
  summary: Higher MIC in some producing strains supports a relative-susceptibility
    observation only. No clinical resistance classification or genetic self-resistance
    mechanism is established.
  target_ids:
  - CHEBI:143030
  evidence_ids:
  - primary2016
- assessment_id: optional
  area: representation
  topic: Clinical, graph and dataset objects
  outcome: not_applicable
  summary: No such objects are asserted. Prospective therapeutic interest does not
    establish clinical efficacy or require invented fields.
  target_ids:
  - CHEBI:143030
  evidence_ids:
  - record
  - primary2016
- assessment_id: provenance
  area: ownership
  topic: Source-owned fields and audit trail
  outcome: supported
  summary: The maintained source reproduces the seed and three history events are
    consistent. Evidence enrichment belongs to curator-owned annotations with proper
    history, not a hand-edited source identity.
  target_ids:
  - CHEBI:143030
  evidence_ids:
  - record
  - inventory
  - ownership
- assessment_id: schema-assessment
  area: schema
  topic: Native and independent validation
  outcome: supported
  summary: Both native validators and independent chemical/source comparisons pass.
    Their success does not resolve the mechanistic gap.
  target_ids:
  - CHEBI:143030
  evidence_ids:
  - validation
  - chemistry
  - source-check
findings:
- finding_id: F1
  issue_key: chebi-143030-primary-activity-scope-evidence-completeness
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Compound-specific primary activity and source context can be represented
  description: The original reprint supplies individually tested schleiferon A MICs
    and phenotype experiments that the broad seed does not represent. Curating this
    evidence would clarify assay, congener and producer scope. No incorrect structure
    or antibacterial filing is established.
  target_ids:
  - CHEBI:143030
  field_paths:
  - evidence
  - activity_spectrum
  - discussions
  - mode_of_action_notes
  evidence_ids:
  - record
  - primary2016
  - mechanism2016
  - formation2018
  rule_id: 'review-checklist: Evidence standard, Activity, Producer, Mode of action
    and Audit'
  native_severity: minor actionable primary-evidence completeness gap
  normalization_reason: A concrete source-backed enrichment is available, while the
    present seed does not assert a false target or numerical endpoint. Empty optional
    fields alone do not warrant a major finding.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/3-phenethylamino-butan-2-one.yaml
    role: Curator-owned evidence, activity observations and discussions through validated
      writer and curation history; imported source fields remain source-owned
actions:
- action_id: A1
  description: In a separately authorized curation pass, attach narrow A-specific
    primary activity evidence and discuss phenotype/mechanism and extracellular source
    boundaries.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:143030
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/3-phenethylamino-butan-2-one.yaml
    role: Curator-owned evidence, activity observations and discussions through validated
      writer and curation history; imported source fields remain source-owned
  acceptance_checks:
  - Use Figure 2A for compound mapping and Table 1 column A for reported MICs in µM;
    retain strain, medium, incubation and readout. Do not conflate B, whole VOC mixtures,
    vapour exposure and directly added synthetic A.
  - 'Preserve the MIC-method incubation at 37 C and the separate 30 C growth experiments;
    do not silently harmonize them. Do not derive clinical susceptibility categories
    or a universal Gram-negative inactivity claim: Table 1 reports a high but finite
    A MIC for S. enterica RV4.'
  - Describe prodigiosin/bioluminescence suppression at the measured phenotype level.
    Figure 6 is labelled B, not A; do not transfer its blot result to A or infer binding
    to PigP/PigS/Lux proteins.
  - Retain S. schleiferi strain/culture context. Add producer_organisms only with
    appropriately scoped biosynthetic support; the 2018 split-headspace precursor
    producers are not individually demonstrated sources of finished A.
  - Preserve unassigned stereochemistry. Apply validated writer and curation history,
    then just validate, just validate-strict, just verify-corpus --summary and just
    qc; leave native REVIEWED criteria unresolved until satisfied.
limitations:
- The discovery paper was inspected as an original scanned reprint within the author
  institutional thesis. OCR supplied searchable text; the title/DOI, structure/Table
  1, MIC methods and Figure 6 were also checked visually. The entire thesis was not
  treated as one primary experiment.
- The 2018 XML/PDF and its correction were read. Its formation mechanism describes
  extracellular chemical production, not an antimicrobial molecular target or a new
  compound-resolved growth assay.
- Absolute configuration of the one stereocentre was not established in the inspected
  sources. The record encodes unspecified stereochemistry rather than a proven racemic
  composition.
- The primary text sometimes generalizes across A/B, while its displayed Northern
  blot specifically labels B. This distinction is retained; no A-specific gene-expression
  or binding claim was adopted from that blot.
- Bounded searching did not establish the growth-inhibitory molecular mode. This is
  not a universal absence claim, and no paid provider or unpublished synthesis work
  was accessed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Only scratch review artifacts were written. No native record, maintained input,
  generated artifact or curation history was modified.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:143030
- https://doi.org/10.1016/j.syapm.2016.08.008
- https://rosdok.uni-rostock.de/file/rosdok_disshab_0000001699/rosdok_derivate_0000036821/Dissertation_Lemfack_2017.pdf
- https://doi.org/10.1038/s41598-018-35341-3
- https://doi.org/10.1038/s41598-018-37081-w
tags:
- record-review
- volatile-antibiotic
- congener-scope
- primary-activity-evidence
- extracellular-formation
```
