# Review of CHEBI:171656 (3-methylarginine)

- Review: 20261021T073738Z-chebi-171656-3-methylarginine-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T07:25:11Z
- Finished UTC: 2026-10-21T07:37:38Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The neutral, stereochemically unspecified ChEBI structure is internally consistent and the antibacterial role has primary support. One minor evidence-completeness finding identifies bounded activity, producer and mechanistic-context curation. Arginine rescue does not identify a molecular target; biosynthetic enzymes must not be represented as antibiotic targets. Exact MetaCyc form equivalence remains unresolved. Native REVIEWED mechanism requirements are not met.

## Scope And Provenance

Entire record, source row and owner, all ontology identifiers and structure fields, primary discovery abstract and supplement, full biosynthesis paper, activity and mechanism scope, and external cross-reference boundary.

Selection: Path-ordered unreviewed queue index 034; exactly one record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:171656 | data/antibiotics/antibacterial/3-methylarginine.yaml | generated | 3-methylarginine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented per-record LinkML validation | passed | True | CHEBI:171656 | Exit 0; No issues found. |
| Documented per-record closed-schema validation | passed | True | CHEBI:171656 | Exit 0; one file, zero ERROR rows. |
| Independent structure and minted-identifier comparison | passed | False | CHEBI:171656 | Both structure encodings and all stored molecular metadata agree. |
| Current source term, parent, role and structure comparison | passed | False | CHEBI:171656 | Assertions pass for current official identifiers and representations; this does not independently resolve MetaCyc exact-form scope. |
| Structured expression-module adapter applicability | not_applicable | False | CHEBI:171656 | The current record names no gene, protein, regulator, pathway, stress response or transcriptomic dataset. A chemical name and producer species do not supply a gene/module query. Biosynthetic genes encountered in the paper are uncurated research context. |
| Authoritative full QC | failed | True | CHEBI:171656 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:171656 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:171656 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:171656 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:171656 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:171656 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:171656 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:171656 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:171656 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Neutral constitution and stereochemical scope

identity: supported. Targets: CHEBI:171656.

The record is internally consistent with its generic ChEBI source concept and is not N-methylarginine, a peptide, or an assigned stereoisomer. Exact source grounding does not establish which stereoisomer was isolated.

### Ontology parents, aliases and source identity

grounding: supported. Targets: CHEBI:171656.

All current parents and the antibacterial role resolve and fit the represented functional groups. Systematic aliases describe the same constitution.

### MetaCyc exact-form equivalence

grounding: unknown. Targets: CHEBI:171656.

The imported CPD-12429 link is reproduced by ChEBI, but direct target data were inaccessible and a charged stereospecific ChEBI child shares it. Verify exact charge and stereochemical scope before treating this as independently confirmed identity.

### Antibacterial classification and source scope

evidence: supported. Targets: CHEBI:171656.

The discovery study supports bacterial growth inhibition by the free amino acid. Neither broader species-wide potency nor clinical efficacy is asserted or established.

### Available primary evidence and assay context

completeness: concern. Targets: CHEBI:171656.

A concrete primary-evidence enrichment can distinguish the sensitive indicator, bioassay conditions and rescue phenotype. Empty optional fields alone are not errors.

### Molecular target and native REVIEWED eligibility

scope: unknown. Targets: CHEBI:171656.

Arginine rescue supports a qualified pathway hypothesis, not a direct target. MrsA is biosynthetic, and nitric-oxide inhibition is inferred from a different analogue. A defensible explicit mechanism and native REVIEWED gate remain unresolved.

### Producer strain versus whole pathovar

representation: supported. Targets: CHEBI:171656.

Production is demonstrated for P. syringae pv. syringae 22d/93, with genetic and chemical evidence. Do not generalize production to every strain: the 2010 study reports no MeArg from B728a despite homologous genes.

### Resistance, clinical, causal graph and dataset fields

representation: not_applicable. Targets: CHEBI:171656.

No such claims are present; no result was found in the inspected exact-compound papers that requires inventing these objects.

### Generated field ownership and audit trail

ownership: supported. Targets: CHEBI:171656.

The inventory and source-concept mint reproduce the seed identity. Three seed/reseed events are consistent with the captured record; no curation event was added.

### Native validators and independent consistency

schema: supported. Targets: CHEBI:171656.

Both per-record validators and independent chemical/source comparisons pass. These checks do not establish a molecular mechanism or external target-form equivalence.

## Findings

### F1: Available primary evidence can distinguish activity, production and mechanistic hypotheses

minor / open / confirmed; issue key: chebi-171656-primary-activity-producer-evidence-completeness.

The seed retains a broad source definition but no claim-level primary evidence. The identified studies permit bounded annotation of production by strain 22d/93 and antibacterial activity/rescue, while explicitly retaining an unresolved molecular target. This is a concrete enrichment opportunity, not an error caused merely by empty optional fields.

## Recommended Actions And Acceptance Checks

### A1

In a separately authorized curation pass, add narrow primary evidence for the experimentally characterized material, producer strain and agar-diffusion/rescue observations. Preserve uncertainty about exact stereochemical mapping and molecular mode.

- Inspect the complete 2008 main paper and its stereochemical conclusions before attaching stereoisomer-specific claims; preserve the neutral unspecified source identity unless a maintained source correction is justified.
- Ground the producer as strain 22d/93 using biosynthetic evidence. Preserve Psg1a/96 and assay context; do not convert toxin units, production estimates or inhibition zones into MICs.
- Represent arginine rescue only as qualified mechanistic context. Do not make MrsA/MrsB/MrsC antimicrobial targets, transfer NOS inhibition from a synthetic analogue, or infer plant-protection efficacy from the article title.
- Resolve the MetaCyc CPD-12429 charge/stereochemistry boundary against accessible authoritative target data. If a mismatch is established, repair the maintained source mapping/transform and reseed rather than hand-editing generated identity.
- Use the validated record writer and curation event, then just validate, just validate-strict, just verify-corpus --summary and just qc. Do not promote REVIEWED before its native mechanism and other criteria are met.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/3-methylarginine.yaml; Entire generated record | supports | Read definition, all five aliases, three parents, activity role, both chemical encodings, one external xref, source concept and three seed/reseed history events. No claim-level evidence, target, mode, activity observation, producer object, resistance, clinical, graph or dataset object is asserted. |
| inventory | data/raw/chebi_antimicrobials.tsv; Complete CHEBI:171656 row and header; adopted source manifest | supports | The adopted row supplies matching imported identity, structure, parents, role, CPD-12429 xref and two citation leads, PMID:18655083 and PMID:20190091. Mechanism-role data are empty. Maintained curation/conf searches found no exact-ID override. |
| ownership | scripts/extract_source_inventory.py; ChEBI extraction and citation separation; scripts/seed_from_sources.py structure_from_chebi, mint and curator merge | supports | Imported fields belong to the source inventory and seed transform. Citation leads are not automatically copied as blanket claim evidence. Scientific evidence annotations are curator-owned through the validated writer and curation history. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:171656; Native ChEBI entry; 034-chebi.html | supports | Current entry matches name, aliases, definition, neutral formula, masses, both encodings, key and CPD-12429 source xref. It represents unspecified stereochemistry, not a stated racemate. |
| ontology | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_171656; 034-ols.json, 034-parents.json and 034-has_role.json | supports | The term is current and non-obsolete. Its direct parents resolve as guanidines, polar amino acid and non-proteinogenic alpha-amino acid. The antibacterial-agent role resolves. Structure literals and synonym texts match; all aliases are chemically compatible with the represented constitution. |
| xref-boundary | https://www.ebi.ac.uk/chebi/CHEBI:229593; Child ChEBI entry; 034-child.html; two attempted MetaCyc endpoints | context_only | The more specific (3R)-3-methyl-L-arginine zwitterion entry also links CPD-12429, while encoding C7H17N4O2, charge +1 and stereochemistry. Direct MetaCyc page and XML requests returned login/subscription HTML rather than compound data. This flags a verification boundary, not proof that the inherited xref is wrong. Do not replace the neutral unspecified record with the charged stereospecific child. |
| primary2008 | PMID:18655083; DOI:10.1002/cbic.200800080; abstract in 034-primary2008.json | supports | Bioassay-guided purification with spectroscopic identification supports free 3-methylarginine from P. syringae pv. syringae 22d/93 and inhibition of P. syringae pv. glycinea. L-arginine rescue suggests a metabolic mechanism but does not identify a direct target. Lavendomycin contains the amino-acid moiety; its activity cannot be transferred to the free compound. |
| supplement2008 | https://application.wiley-vch.de/contents/jc_2268/2008/f800080_s.pdf; 034-supplement2008.pdf, pp.2-14; purification, spectroscopy, stereochemical-analysis chromatograms and mutants | supports | The authentic supplement supplies growth-inhibition calibration, mass/NMR data and a stereochemical-analysis section showing derivatized oxo-product chromatograms. It does not by itself provide a safely interpretable complete absolute-configuration conclusion. Its inhibition-zone calibration is not a broth MIC. |
| primary2010 | PMID:20190091; DOI:10.1128/AEM.00666-09; full paper 034-primary2010.pdf from https://pure.mpg.de/rest/items/item_445909_9/component/file_527138/content; Methods, Table 2, Figures 4/6/7, Discussion | supports | Mutant/complementation and heterologous-expression experiments establish production by strain 22d/93; agar diffusion uses Psg1a/96 and 0.1 mM L-arginine reverses inhibition. Table 2 values estimate toxin activity/production, not MICs. MrsA catalyzes biosynthesis, while MrsB/MrsC roles are partly inferred. The discussion explicitly leaves mode unresolved and proposes arginine-related pathways. Its nitric-oxide comparison concerns a different synthetic analogue, not direct MeArg target evidence. |
| chemistry | RDKit and hashlib local calculations; 034-chemistry.py and 034-chemistry.json | supports | Both encodings yield VRWSVIUPXSFVFZ-UHFFFAOYSA-N, C7H16N4O2, charge zero, one fragment, average mass 188.231 and exact mass 188.127325752. Two tetrahedral centres are unassigned. The minted source identifier is reproduced. |
| source-check | Focused official-source assertions; 034-source-check.py and 034-source-check.json | supports | All asserted parent and role identifiers resolve; native-page and OLS structures and metadata agree with the record. Synonym strings and inherited external xref are present in current ChEBI. Direct exact-form equivalence at MetaCyc was not established. |
| validation | just validate; just validate-strict; Actual executions in isolated batch-004 checkout; 034-strict.tsv | supports | Both documented per-record validators exited 0; strict validation scanned one record with zero ERROR rows. |
| search | Ignored-inclusive local and bounded free web discovery; 034-local-hits.txt; exact compound, stereochemistry, mechanism and primary-title searches | context_only | The inspected papers establish bounded activity and biosynthesis, but no direct antimicrobial target. A separate biocontrol paper, DOI:10.1111/j.1439-0434.2009.01612.x, was located as a follow-up lead: plant protection must not be inferred simply from the 2008 title. Its publisher retrieval failed, so no uninspected full-paper result is treated as established here. |

## Limits And Additional Notes

- The 2008 discovery abstract and authentic supplement were inspected; its complete main text was not retrieved. A thesis download yielded bot-challenge HTML, and search-indexed excerpts were not substituted for full source inspection. Complete stereochemical conclusions remain unverified.
- The complete 2010 primary paper was downloaded from the author institution and read as PDF text. Its EPMC XML endpoint returned HTTP 500; this did not prevent primary full-text inspection. No quantitative MIC was established by the assays inspected.
- Both direct MetaCyc requests produced login/subscription HTML, not target data. ChEBI source agreement verifies inherited provenance only; it does not settle neutral unspecified versus charged stereospecific exact equivalence.
- Bounded discovery did not establish a molecular antibacterial target. This is not a universal absence claim. Separate plant-bioconrol follow-up was located but its publisher request returned 403; no full-text conclusion was adopted.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Only scratch review artifacts were written. No native record, maintained input, generated artifact or curation history was modified.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T073738Z-chebi-171656-3-methylarginine-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of CHEBI:171656 (3-methylarginine)
started_at: '2026-10-21T07:25:11Z'
finished_at: '2026-10-21T07:37:38Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Source identity and antibacterial filing supported; primary-evidence
  enrichment, exact cross-reference scope and molecular mechanism remain
scientific_review: true
summary: The neutral, stereochemically unspecified ChEBI structure is internally consistent
  and the antibacterial role has primary support. One minor evidence-completeness
  finding identifies bounded activity, producer and mechanistic-context curation.
  Arginine rescue does not identify a molecular target; biosynthetic enzymes must
  not be represented as antibiotic targets. Exact MetaCyc form equivalence remains
  unresolved. Native REVIEWED mechanism requirements are not met.
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
  - path: data/antibiotics/antibacterial/3-methylarginine.yaml
    sha256: 373b6933abc98528a57ea1af4a1e644445f56cc630bf7f0c0949f3780e6c52b9
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
  description: Entire record, source row and owner, all ontology identifiers and structure
    fields, primary discovery abstract and supplement, full biosynthesis paper, activity
    and mechanism scope, and external cross-reference boundary.
  selection: Path-ordered unreviewed queue index 034; exactly one record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:171656
targets:
- target_id: CHEBI:171656
  path: data/antibiotics/antibacterial/3-methylarginine.yaml
  label: 3-methylarginine
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
  - CHEBI:171656
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/3-methylarginine.yaml
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
  - CHEBI:171656
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/3-methylarginine.yaml --out /private/tmp/am-review-session/034-strict.tsv
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
  - CHEBI:171656
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/034-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: source-check
  name: Current source term, parent, role and structure comparison
  status: passed
  required: false
  summary: Assertions pass for current official identifiers and representations; this
    does not independently resolve MetaCyc exact-form scope.
  target_ids:
  - CHEBI:171656
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/034-source-check.py
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
    or transcriptomic dataset. A chemical name and producer species do not supply
    a gene/module query. Biosynthetic genes encountered in the paper are uncurated
    research context.
  target_ids:
  - CHEBI:171656
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
  - CHEBI:171656
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
  - CHEBI:171656
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
  - CHEBI:171656
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
  - CHEBI:171656
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
  - CHEBI:171656
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
  - CHEBI:171656
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
  - CHEBI:171656
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
  - CHEBI:171656
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
  - CHEBI:171656
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/3-methylarginine.yaml
  locator: Entire generated record
  accessed_at: '2026-10-21T07:30:40Z'
  support: supports
  summary: Read definition, all five aliases, three parents, activity role, both chemical
    encodings, one external xref, source concept and three seed/reseed history events.
    No claim-level evidence, target, mode, activity observation, producer object,
    resistance, clinical, graph or dataset object is asserted.
- evidence_id: inventory
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Complete CHEBI:171656 row and header; adopted source manifest
  accessed_at: '2026-10-21T07:30:40Z'
  support: supports
  summary: The adopted row supplies matching imported identity, structure, parents,
    role, CPD-12429 xref and two citation leads, PMID:18655083 and PMID:20190091.
    Mechanism-role data are empty. Maintained curation/conf searches found no exact-ID
    override.
- evidence_id: ownership
  kind: record_content
  reference: scripts/extract_source_inventory.py
  locator: ChEBI extraction and citation separation; scripts/seed_from_sources.py
    structure_from_chebi, mint and curator merge
  accessed_at: '2026-10-21T07:30:40Z'
  support: supports
  summary: Imported fields belong to the source inventory and seed transform. Citation
    leads are not automatically copied as blanket claim evidence. Scientific evidence
    annotations are curator-owned through the validated writer and curation history.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:171656
  locator: Native ChEBI entry; 034-chebi.html
  accessed_at: '2026-10-21T07:30:40Z'
  support: supports
  summary: Current entry matches name, aliases, definition, neutral formula, masses,
    both encodings, key and CPD-12429 source xref. It represents unspecified stereochemistry,
    not a stated racemate.
  snapshot_sha256: bbb386e5117965366cd8dabc48f1fe7d5aaee0beb278b89c10c0dcbfeb2f1f84
- evidence_id: ontology
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_171656
  locator: 034-ols.json, 034-parents.json and 034-has_role.json
  accessed_at: '2026-10-21T07:30:40Z'
  support: supports
  summary: The term is current and non-obsolete. Its direct parents resolve as guanidines,
    polar amino acid and non-proteinogenic alpha-amino acid. The antibacterial-agent
    role resolves. Structure literals and synonym texts match; all aliases are chemically
    compatible with the represented constitution.
  snapshot_sha256: 1a41ba8084f38467ea9c5bcdbe609bfd3aca357d621d8f84f2e9a7592c0de69a
- evidence_id: xref-boundary
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:229593
  locator: Child ChEBI entry; 034-child.html; two attempted MetaCyc endpoints
  accessed_at: '2026-10-21T07:30:40Z'
  support: context_only
  summary: The more specific (3R)-3-methyl-L-arginine zwitterion entry also links
    CPD-12429, while encoding C7H17N4O2, charge +1 and stereochemistry. Direct MetaCyc
    page and XML requests returned login/subscription HTML rather than compound data.
    This flags a verification boundary, not proof that the inherited xref is wrong.
    Do not replace the neutral unspecified record with the charged stereospecific
    child.
  snapshot_sha256: 658b4e7dd7294ac74b8a26dff4c8dd0d4e03beebaa49075fb9ea3ceb51e984aa
- evidence_id: primary2008
  kind: primary_source
  reference: PMID:18655083
  locator: DOI:10.1002/cbic.200800080; abstract in 034-primary2008.json
  accessed_at: '2026-10-21T07:30:40Z'
  support: supports
  summary: Bioassay-guided purification with spectroscopic identification supports
    free 3-methylarginine from P. syringae pv. syringae 22d/93 and inhibition of P.
    syringae pv. glycinea. L-arginine rescue suggests a metabolic mechanism but does
    not identify a direct target. Lavendomycin contains the amino-acid moiety; its
    activity cannot be transferred to the free compound.
  snapshot_sha256: 1149c8a6c68d4d5be1d4946c9bf80451b5b75f704336b1413b0d61202538b029
- evidence_id: supplement2008
  kind: primary_source
  reference: https://application.wiley-vch.de/contents/jc_2268/2008/f800080_s.pdf
  locator: 034-supplement2008.pdf, pp.2-14; purification, spectroscopy, stereochemical-analysis
    chromatograms and mutants
  accessed_at: '2026-10-21T07:30:40Z'
  support: supports
  summary: The authentic supplement supplies growth-inhibition calibration, mass/NMR
    data and a stereochemical-analysis section showing derivatized oxo-product chromatograms.
    It does not by itself provide a safely interpretable complete absolute-configuration
    conclusion. Its inhibition-zone calibration is not a broth MIC.
  snapshot_sha256: 8cb388c7efbd569426018d661f695e3ecf85d58e0186e52c0fe1e043f6683df4
- evidence_id: primary2010
  kind: primary_source
  reference: PMID:20190091
  locator: DOI:10.1128/AEM.00666-09; full paper 034-primary2010.pdf from https://pure.mpg.de/rest/items/item_445909_9/component/file_527138/content;
    Methods, Table 2, Figures 4/6/7, Discussion
  accessed_at: '2026-10-21T07:30:40Z'
  support: supports
  summary: Mutant/complementation and heterologous-expression experiments establish
    production by strain 22d/93; agar diffusion uses Psg1a/96 and 0.1 mM L-arginine
    reverses inhibition. Table 2 values estimate toxin activity/production, not MICs.
    MrsA catalyzes biosynthesis, while MrsB/MrsC roles are partly inferred. The discussion
    explicitly leaves mode unresolved and proposes arginine-related pathways. Its
    nitric-oxide comparison concerns a different synthetic analogue, not direct MeArg
    target evidence.
  snapshot_sha256: 8da2360ee224ad1c043a615336b828676e23add2ad5380fe928f7ce631aaf524
- evidence_id: chemistry
  kind: validation
  reference: RDKit and hashlib local calculations
  locator: 034-chemistry.py and 034-chemistry.json
  accessed_at: '2026-10-21T07:30:40Z'
  support: supports
  summary: Both encodings yield VRWSVIUPXSFVFZ-UHFFFAOYSA-N, C7H16N4O2, charge zero,
    one fragment, average mass 188.231 and exact mass 188.127325752. Two tetrahedral
    centres are unassigned. The minted source identifier is reproduced.
  snapshot_sha256: 2ebf98af44590cc7cbab33da979b12be99763bbf6281d4d9dc6e5f3fff17cfff
- evidence_id: source-check
  kind: validation
  reference: Focused official-source assertions
  locator: 034-source-check.py and 034-source-check.json
  accessed_at: '2026-10-21T07:30:40Z'
  support: supports
  summary: All asserted parent and role identifiers resolve; native-page and OLS structures
    and metadata agree with the record. Synonym strings and inherited external xref
    are present in current ChEBI. Direct exact-form equivalence at MetaCyc was not
    established.
  snapshot_sha256: 4c66f311fa6b51605d2d84faa2ab9b6f585ca7cadc5472f34df38058a5607bad
- evidence_id: validation
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual executions in isolated batch-004 checkout; 034-strict.tsv
  accessed_at: '2026-10-21T07:30:40Z'
  support: supports
  summary: Both documented per-record validators exited 0; strict validation scanned
    one record with zero ERROR rows.
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local and bounded free web discovery
  locator: 034-local-hits.txt; exact compound, stereochemistry, mechanism and primary-title
    searches
  accessed_at: '2026-10-21T07:30:40Z'
  support: context_only
  summary: 'The inspected papers establish bounded activity and biosynthesis, but
    no direct antimicrobial target. A separate biocontrol paper, DOI:10.1111/j.1439-0434.2009.01612.x,
    was located as a follow-up lead: plant protection must not be inferred simply
    from the 2008 title. Its publisher retrieval failed, so no uninspected full-paper
    result is treated as established here.'
  search_scope: prepare.py 34 searched identifier, label and slug with rg --no-ignore
    --hidden, excluding only .git and .venv. Follow-up searches examined maintained
    curation/conf inputs. Free web queries used 3-methylarginine antibacterial, mode
    of action, stereochemistry/configuration, amino acid oxidase, exact article titles
    and DOIs. Official ChEBI/OLS, the discovery abstract/supplement and the complete
    2010 biosynthesis paper were inspected. A thesis PDF request returned a bot challenge;
    indexed excerpts were discovery leads only.
assessments:
- assessment_id: identity
  area: identity
  topic: Neutral constitution and stereochemical scope
  outcome: supported
  summary: The record is internally consistent with its generic ChEBI source concept
    and is not N-methylarginine, a peptide, or an assigned stereoisomer. Exact source
    grounding does not establish which stereoisomer was isolated.
  target_ids:
  - CHEBI:171656
  evidence_ids:
  - record
  - chebi
  - chemistry
  - supplement2008
- assessment_id: grounding
  area: grounding
  topic: Ontology parents, aliases and source identity
  outcome: supported
  summary: All current parents and the antibacterial role resolve and fit the represented
    functional groups. Systematic aliases describe the same constitution.
  target_ids:
  - CHEBI:171656
  evidence_ids:
  - ontology
  - source-check
  - chemistry
- assessment_id: xref
  area: grounding
  topic: MetaCyc exact-form equivalence
  outcome: unknown
  summary: The imported CPD-12429 link is reproduced by ChEBI, but direct target data
    were inaccessible and a charged stereospecific ChEBI child shares it. Verify exact
    charge and stereochemical scope before treating this as independently confirmed
    identity.
  target_ids:
  - CHEBI:171656
  evidence_ids:
  - xref-boundary
  - record
- assessment_id: classification
  area: evidence
  topic: Antibacterial classification and source scope
  outcome: supported
  summary: The discovery study supports bacterial growth inhibition by the free amino
    acid. Neither broader species-wide potency nor clinical efficacy is asserted or
    established.
  target_ids:
  - CHEBI:171656
  evidence_ids:
  - primary2008
  - primary2010
  - record
- assessment_id: activity
  area: completeness
  topic: Available primary evidence and assay context
  outcome: concern
  summary: A concrete primary-evidence enrichment can distinguish the sensitive indicator,
    bioassay conditions and rescue phenotype. Empty optional fields alone are not
    errors.
  target_ids:
  - CHEBI:171656
  evidence_ids:
  - record
  - primary2008
  - primary2010
- assessment_id: mechanism
  area: scope
  topic: Molecular target and native REVIEWED eligibility
  outcome: unknown
  summary: Arginine rescue supports a qualified pathway hypothesis, not a direct target.
    MrsA is biosynthetic, and nitric-oxide inhibition is inferred from a different
    analogue. A defensible explicit mechanism and native REVIEWED gate remain unresolved.
  target_ids:
  - CHEBI:171656
  evidence_ids:
  - primary2008
  - primary2010
  - search
- assessment_id: producer
  area: representation
  topic: Producer strain versus whole pathovar
  outcome: supported
  summary: 'Production is demonstrated for P. syringae pv. syringae 22d/93, with genetic
    and chemical evidence. Do not generalize production to every strain: the 2010
    study reports no MeArg from B728a despite homologous genes.'
  target_ids:
  - CHEBI:171656
  evidence_ids:
  - primary2010
  - record
- assessment_id: optional
  area: representation
  topic: Resistance, clinical, causal graph and dataset fields
  outcome: not_applicable
  summary: No such claims are present; no result was found in the inspected exact-compound
    papers that requires inventing these objects.
  target_ids:
  - CHEBI:171656
  evidence_ids:
  - record
  - primary2008
  - primary2010
- assessment_id: provenance
  area: ownership
  topic: Generated field ownership and audit trail
  outcome: supported
  summary: The inventory and source-concept mint reproduce the seed identity. Three
    seed/reseed events are consistent with the captured record; no curation event
    was added.
  target_ids:
  - CHEBI:171656
  evidence_ids:
  - record
  - inventory
  - ownership
  - chemistry
- assessment_id: schema-assessment
  area: schema
  topic: Native validators and independent consistency
  outcome: supported
  summary: Both per-record validators and independent chemical/source comparisons
    pass. These checks do not establish a molecular mechanism or external target-form
    equivalence.
  target_ids:
  - CHEBI:171656
  evidence_ids:
  - validation
  - chemistry
  - source-check
findings:
- finding_id: F1
  issue_key: chebi-171656-primary-activity-producer-evidence-completeness
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Available primary evidence can distinguish activity, production and mechanistic
    hypotheses
  description: The seed retains a broad source definition but no claim-level primary
    evidence. The identified studies permit bounded annotation of production by strain
    22d/93 and antibacterial activity/rescue, while explicitly retaining an unresolved
    molecular target. This is a concrete enrichment opportunity, not an error caused
    merely by empty optional fields.
  target_ids:
  - CHEBI:171656
  field_paths:
  - evidence
  - activity_spectrum
  - producer_organisms
  - discussions
  - mode_of_action_notes
  evidence_ids:
  - record
  - primary2008
  - supplement2008
  - primary2010
  rule_id: 'review-checklist: Evidence standard, Activity, Producer, Mode of action
    and Audit'
  native_severity: minor primary-evidence completeness gap
  normalization_reason: No incorrect structure or antibacterial role is demonstrated.
    A specific primary source supports useful curator-owned enrichment; speculative
    mechanisms and numerical MIC conversion are excluded.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/3-methylarginine.yaml
    role: Curator-owned evidence, activity context, producer annotation and discussion
      through the validated writer and curation history; imported identity and xrefs
      remain source-owned
actions:
- action_id: A1
  description: In a separately authorized curation pass, add narrow primary evidence
    for the experimentally characterized material, producer strain and agar-diffusion/rescue
    observations. Preserve uncertainty about exact stereochemical mapping and molecular
    mode.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:171656
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/3-methylarginine.yaml
    role: Curator-owned evidence, activity context, producer annotation and discussion
      through the validated writer and curation history; imported identity and xrefs
      remain source-owned
  acceptance_checks:
  - Inspect the complete 2008 main paper and its stereochemical conclusions before
    attaching stereoisomer-specific claims; preserve the neutral unspecified source
    identity unless a maintained source correction is justified.
  - Ground the producer as strain 22d/93 using biosynthetic evidence. Preserve Psg1a/96
    and assay context; do not convert toxin units, production estimates or inhibition
    zones into MICs.
  - Represent arginine rescue only as qualified mechanistic context. Do not make MrsA/MrsB/MrsC
    antimicrobial targets, transfer NOS inhibition from a synthetic analogue, or infer
    plant-protection efficacy from the article title.
  - Resolve the MetaCyc CPD-12429 charge/stereochemistry boundary against accessible
    authoritative target data. If a mismatch is established, repair the maintained
    source mapping/transform and reseed rather than hand-editing generated identity.
  - Use the validated record writer and curation event, then just validate, just validate-strict,
    just verify-corpus --summary and just qc. Do not promote REVIEWED before its native
    mechanism and other criteria are met.
limitations:
- The 2008 discovery abstract and authentic supplement were inspected; its complete
  main text was not retrieved. A thesis download yielded bot-challenge HTML, and search-indexed
  excerpts were not substituted for full source inspection. Complete stereochemical
  conclusions remain unverified.
- The complete 2010 primary paper was downloaded from the author institution and read
  as PDF text. Its EPMC XML endpoint returned HTTP 500; this did not prevent primary
  full-text inspection. No quantitative MIC was established by the assays inspected.
- Both direct MetaCyc requests produced login/subscription HTML, not target data.
  ChEBI source agreement verifies inherited provenance only; it does not settle neutral
  unspecified versus charged stereospecific exact equivalence.
- Bounded discovery did not establish a molecular antibacterial target. This is not
  a universal absence claim. Separate plant-bioconrol follow-up was located but its
  publisher request returned 403; no full-text conclusion was adopted.
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
- https://www.ebi.ac.uk/chebi/CHEBI:171656
- https://www.ebi.ac.uk/chebi/CHEBI:229593
- https://pubmed.ncbi.nlm.nih.gov/18655083/
- https://doi.org/10.1002/cbic.200800080
- https://application.wiley-vch.de/contents/jc_2268/2008/f800080_s.pdf
- https://doi.org/10.1128/AEM.00666-09
- https://pure.mpg.de/rest/items/item_445909_9/component/file_527138/content
tags:
- record-review
- nonproteinogenic-amino-acid
- assay-scope
- biosynthesis-versus-target
- cross-reference-scope
```
