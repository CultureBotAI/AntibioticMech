# 5-Hydroxy-7,2',4',5'-tetramethoxyflavone: exact identity and primary evidence scope

- Review: 20261021T075915Z-5-hydroxy-7-2-4-5-tetramethoxyflavone
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T07:49:11Z
- Finished UTC: 2026-10-21T07:59:15Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Exact positional identity, broad antibacterial classification, plant-isolation wording, generated provenance and focused validation are supported. No corrective finding is established. Original assay details and direct registry verification remain unavailable; no potency, target or biosynthetic-producer claim is inferred. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Full one-record identity, evidence placement and bounded scientific review.

Selection: Queue index051; exactly CHEBI:66040 in isolated batch006.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:66040 | data/antibiotics/antibacterial/5-hydroxy-7-2-4-5-tetramethoxyflavone.yaml | generated | 5-hydroxy-7,2',4',5'-tetramethoxyflavone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema validation | passed | True | CHEBI:66040 | Actual focused execution passed with zero errors. |
| Focused strict validation | passed | True | CHEBI:66040 | Actual focused execution passed with zero errors. |
| Exact positional structure and source identity | passed | True | CHEBI:66040 | Native structure, current authorities, primary synthesis and independent calculation agree. |
| Direct registry substance detail | unavailable | False | CHEBI:66040 | Reaxys detail unavailable; official source assertion inspected. |
| Structured expression-source applicability | not_applicable | False | CHEBI:66040 | No native gene, protein, regulator, pathway, stress response, trait dataset or transcriptomic dataset is named. Exact small-molecule identity and plant isolation do not supply an applicable expression-module query. |
| Authoritative full QC | failed | True | CHEBI:66040 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:66040 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:66040 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:66040 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:66040 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:66040 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:66040 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:66040 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:66040 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact hydroxy/methoxy positions

identity: supported. Targets: CHEBI:66040.

The native structure is the exact five-substituent flavone. Current ChEBI/PubChem, independent chemistry and the primary synthesis agree. Compound2 in1994 is compound1 in1995; numbering is paper-specific.

### Broader parents and antibacterial role

grounding: supported. Targets: CHEBI:66040.

Both structural parents and the antibacterial role are appropriate. Registry detail remains source-asserted and unavailable independently.

### Natural isolation and broad antibacterial classification

evidence: supported. Targets: CHEBI:66040.

The original abstract supports isolation from Calliandra californica and antibacterial activity of the exact compound; the follow-up synthesis confirms identity and distinguishes the nonhydroxylated companion. Native broad wording is appropriately bounded.

### Strain-resolved activity and mechanism

evidence: unknown. Targets: CHEBI:66040.

The inspected original abstract lacks strain names, assay protocol and numbers. The synthesis paper provides no new microbiological endpoint or direct target. No quantitative activity or mechanism is asserted natively, and neither MeSH nor other-flavone studies can fill those gaps.

### Plant isolation versus biosynthetic production

completeness: unknown. Targets: CHEBI:66040.

Plant isolation is already represented in the definition. Exact tissue/voucher and biosynthetic source were not independently verified in the original main text, so the lack of a structured producer assertion is not made a defect.

### Resistance, clinical status and datasets

scope: not_applicable. Targets: CHEBI:66040.

No native assertions require adjudication in these fields. The inspected primary studies do not establish resistance determinants, clinical product status or transcriptomic datasets.

### Generated field ownership and history

provenance: supported. Targets: CHEBI:66040.

Raw source, minted identifier, source version and three seed/reseed events agree. Native SEEDED status is retained; a scientific review is not curation sign-off.

### Focused native gates

schema: supported. Targets: CHEBI:66040.

Both focused validators pass.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/5-hydroxy-7-2-4-5-tetramethoxyflavone.yaml; Entire native YAML | supports | Read the exact ANTIBACTERIAL, SEEDED, EXACT record: definition, both systematic synonyms, two broader parents, antibacterial role, full structure, Reaxys xref, source concept and all three seed/reseed events. No target, mechanism, quantitative activity, resistance, clinical, dataset, structured producer or causal graph assertion is present. |
| owner | data/raw/chebi_antimicrobials.tsv; CHEBI:66040 row1401; PATHS.tsv row1654; source configuration, MANIFEST, extractor and seeder | supports | Raw identity and structure agree with the seed, source version2026-08-30 and minted identifier antibioticmech:chebi-a29c438029. Adopted primary lead is PMID:7798967. Antimicrobial role extraction does not require copying the separate generic metabolite role into activity_roles. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:66040; Official visible identity, structures, names, ontology, registry and species-of-metabolite fields | supports | The native OH5 and methoxy7,2-prime,4-prime,5-prime structure, key JZIWGWPCBNNLJD-UHFFFAOYSA-N, C19H18O7, charge0, average mass358.346 and monoisotopic358.10525 agree. ChEBI supports both names, parents and antibacterial role and asserts Reaxys7313462. Its Calliandra californica/root provenance cites PMID7798967; this is database provenance, not an independently inspected plant-organ experiment. |
| parent-38687 | https://www.ebi.ac.uk/chebi/CHEBI:38687; Official definition and child relation | supports | The parent resolves to monohydroxyflavone and is a broader structural class applicable to the exact structure. Class membership does not imply a shared molecular target. |
| parent-76875 | https://www.ebi.ac.uk/chebi/CHEBI:76875; Official definition and child relation | supports | The parent resolves to tetramethoxyflavone and is a broader structural class applicable to the exact structure. Class membership does not imply a shared molecular target. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/10428459; PUG View identity and computed structure fields | supports | PubChem CID10428459 independently provides the same complete Standard InChI, InChIKey, formula and charge, with compatible masses and a valid equivalent Kekule SMILES. Source-derived description is not an independent antimicrobial experiment. |
| chemistry | RDKit structure calculation; Native SMILES and Standard InChI separately parsed from batch006 record | supports | Both encodings give the full native key, formula C19H18O7, neutral charge, one fragment, average mass358.346 and exact mass358.105252916. Calculation was run with the batch005 locked interpreter while cwd was batch006 because RDKit had not yet been installed in batch006; the coordinator subsequently installed it locally. |
| primary | PMID:7798967; DOI10.1021/np50111a023; Europe PMC core primary abstract | supports | The1994 primary abstract maps the exact hydroxyflavone to compound2, isolated from Calliandra californica, structurally characterized and synthesized. It explicitly reports antimicrobial activity for two test bacterial strains. It does not name strains, provide assay methods or numeric endpoints, or establish a target. MeSH organism tags are indexing, not compound-specific positive assay results. |
| synthesis | https://actachemscand.ki.ku.dk/pdf/acta_vol_49_p0357-0360.pdf; DOI10.3891/acta.chem.scand.49-0357; complete four-page paper, pp357-360; compound map and Tables1-2 on p358; exact synthesis p360 | supports | The1995 primary paper confirms synthesis and characterization of this exact hydroxyflavone, numbered1 in this paper, and reports identity with the natural material. Its introduction distinguishes the inactive nonhydroxylated companion from the antibacterial hydroxyflavone, citing the1994 study. The inspected paper supplies chemical synthesis/NMR evidence, not new organism-specific assay measurements or an antibacterial molecular mechanism. Pages357,358 and360 were visually inspected; all four pages were read including OCR of the scanned text. |
| registry | https://www.reaxys.com/reaxys/secured/search.do?searchType=quick&amp;rid=7313462; Direct registry detail attempt | partial | Direct Reaxys substance detail was inaccessible. The xref is verified only as the current official ChEBI assertion, with no independently inspected registry structure. |
| search | CultureBotAI/AntibioticMech; Ignored-inclusive local references and bounded free primary discovery | context_only | Local source and PATHS agree. Readiness material was only a discovery lead. Free discovery located the1994 primary abstract and the complete1995 synthesis paper. ACS main text was unavailable, and the ACS Figshare resource-DOI query returned an empty list. Other positional isomers, the nonhydroxylated companion and whole-plant/extract activity were not transferred. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Exact-compound, activity, producer and mechanism rules | supports | Optional blanks alone are not defects. Chemical synthesis, plant isolation, antibacterial growth inhibition and molecular mechanism are distinct claims. A whole-plant isolation record does not establish a specific biosynthetic producer process or permit transfer from related flavones. |
| validation | just validate; just validate-strict; Actual batch006 focused executions; 051-validation.tsv | supports | LinkML validation exited0 with no issues. Strict validation scanned one target and exited0 with no ERROR rows. |

## Limits And Additional Notes

- The1994 primary main text was unavailable through attempted free routes. Its abstract supports the exact compound and broad antibacterial activity, but named strains, assay endpoints, quantities and tissue/voucher details were not verified.
- The1995 full synthesis paper supplies chemical identity evidence and retrospectively discusses antibacterial activity; it is not a new microbiological assay or mechanism study.
- Direct Reaxys detail was unavailable, so the xref is verified only as an official ChEBI assertion.
- Bounded primary discovery does not establish absence of further exact-compound studies. Optional unpopulated fields were not treated as errors.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Initial capture preceded judgment; all original input hashes and Git base were retained in the expanded20-input provenance.
- The independent chemistry calculation used the batch005 environment with batch006 cwd; later installation of batch006 RDKit did not change the assessed native inputs.
- Ignored and hidden files were included in local searches. No native content or scientific status was changed.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T075915Z-5-hydroxy-7-2-4-5-tetramethoxyflavone
kind: record
repository: CultureBotAI/AntibioticMech
title: '5-Hydroxy-7,2'',4'',5''-tetramethoxyflavone: exact identity and primary evidence
  scope'
started_at: '2026-10-21T07:49:11Z'
finished_at: '2026-10-21T07:59:15Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Reviewer did not create the seed and independently read the
    complete native record, current authorities, primary abstract and follow-up synthesis
    paper.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: Exact positional identity, broad antibacterial classification, plant-isolation
  wording, generated provenance and focused validation are supported. No corrective
  finding is established. Original assay details and direct registry verification
  remain unavailable; no potency, target or biosynthetic-producer claim is inferred.
  Scientific assessment retains the stated evidence limits; full verification is blocked
  by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/5-hydroxy-7-2-4-5-tetramethoxyflavone.yaml
    sha256: 3a139eab029d571b68ba00e720e805112b5e36a9ef6473591fd8f946cf445a89
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
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: data/antibiotics/PATHS.tsv
    sha256: 3b1d82d007878e4aca2c28f4001a468776b325b726da2e48abb76a3dc551cc38
    role: context
targets:
- target_id: CHEBI:66040
  path: data/antibiotics/antibacterial/5-hydroxy-7-2-4-5-tetramethoxyflavone.yaml
  label: 5-hydroxy-7,2',4',5'-tetramethoxyflavone
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
  description: Full one-record identity, evidence placement and bounded scientific
    review.
  selection: Queue index051; exactly CHEBI:66040 in isolated batch006.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:66040
  exclusions:
  - target: Nonhydroxylated companion, other positional flavone isomers and whole-plant
      extracts
    reason: Identity and experiment boundaries only; activities and mechanisms are
      not transferred.
checks:
- check_id: schema
  name: Focused schema validation
  status: passed
  required: true
  summary: Actual focused execution passed with zero errors.
  target_ids:
  - CHEBI:66040
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/5-hydroxy-7-2-4-5-tetramethoxyflavone.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Focused strict validation
  status: passed
  required: true
  summary: Actual focused execution passed with zero errors.
  target_ids:
  - CHEBI:66040
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/5-hydroxy-7-2-4-5-tetramethoxyflavone.yaml --out
    /private/tmp/am-review-session/051-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: identity
  name: Exact positional structure and source identity
  status: passed
  required: true
  summary: Native structure, current authorities, primary synthesis and independent
    calculation agree.
  target_ids:
  - CHEBI:66040
  evidence_ids:
  - chebi
  - pubchem
  - chemistry
  - synthesis
- check_id: registry
  name: Direct registry substance detail
  status: unavailable
  required: false
  summary: Reaxys detail unavailable; official source assertion inspected.
  target_ids:
  - CHEBI:66040
  evidence_ids:
  - registry
- check_id: structured-adapter
  name: Structured expression-source applicability
  status: not_applicable
  required: false
  summary: No native gene, protein, regulator, pathway, stress response, trait dataset
    or transcriptomic dataset is named. Exact small-molecule identity and plant isolation
    do not supply an applicable expression-module query.
  target_ids:
  - CHEBI:66040
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
  - CHEBI:66040
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
  - CHEBI:66040
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
  - CHEBI:66040
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
  - CHEBI:66040
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
  - CHEBI:66040
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
  - CHEBI:66040
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
  - CHEBI:66040
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
  - CHEBI:66040
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
  - CHEBI:66040
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/5-hydroxy-7-2-4-5-tetramethoxyflavone.yaml
  locator: Entire native YAML
  accessed_at: '2026-10-21T07:53:07Z'
  support: supports
  summary: 'Read the exact ANTIBACTERIAL, SEEDED, EXACT record: definition, both systematic
    synonyms, two broader parents, antibacterial role, full structure, Reaxys xref,
    source concept and all three seed/reseed events. No target, mechanism, quantitative
    activity, resistance, clinical, dataset, structured producer or causal graph assertion
    is present.'
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: CHEBI:66040 row1401; PATHS.tsv row1654; source configuration, MANIFEST,
    extractor and seeder
  accessed_at: '2026-10-21T07:53:07Z'
  support: supports
  summary: Raw identity and structure agree with the seed, source version2026-08-30
    and minted identifier antibioticmech:chebi-a29c438029. Adopted primary lead is
    PMID:7798967. Antimicrobial role extraction does not require copying the separate
    generic metabolite role into activity_roles.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:66040
  locator: Official visible identity, structures, names, ontology, registry and species-of-metabolite
    fields
  accessed_at: '2026-10-21T07:49:49Z'
  support: supports
  summary: The native OH5 and methoxy7,2-prime,4-prime,5-prime structure, key JZIWGWPCBNNLJD-UHFFFAOYSA-N,
    C19H18O7, charge0, average mass358.346 and monoisotopic358.10525 agree. ChEBI
    supports both names, parents and antibacterial role and asserts Reaxys7313462.
    Its Calliandra californica/root provenance cites PMID7798967; this is database
    provenance, not an independently inspected plant-organ experiment.
  snapshot_sha256: c802165a01cd5ef04d888a9c3a664fe71d071cd4465fe8b96b524bd91fdfeee9
- evidence_id: parent-38687
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:38687
  locator: Official definition and child relation
  accessed_at: '2026-10-21T07:49:52Z'
  support: supports
  summary: The parent resolves to monohydroxyflavone and is a broader structural class
    applicable to the exact structure. Class membership does not imply a shared molecular
    target.
  snapshot_sha256: 090a0b9a4ceba36d6e2abc0b46d5c6a2d3659bb358dc5a80f9a6235baf2d178e
- evidence_id: parent-76875
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:76875
  locator: Official definition and child relation
  accessed_at: '2026-10-21T07:49:54Z'
  support: supports
  summary: The parent resolves to tetramethoxyflavone and is a broader structural
    class applicable to the exact structure. Class membership does not imply a shared
    molecular target.
  snapshot_sha256: e43a5b69ec63e9634055b6486cc0fd1161daffa6a334a5dfb216d9adc14af559
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/10428459
  locator: PUG View identity and computed structure fields
  accessed_at: '2026-10-21T07:49:51Z'
  support: supports
  summary: PubChem CID10428459 independently provides the same complete Standard InChI,
    InChIKey, formula and charge, with compatible masses and a valid equivalent Kekule
    SMILES. Source-derived description is not an independent antimicrobial experiment.
  snapshot_sha256: 4b6a74c75a5ae702e660d0419ec114d1ceba9b33762d90c78644c942af0b6f95
- evidence_id: chemistry
  kind: validation
  reference: RDKit structure calculation
  locator: Native SMILES and Standard InChI separately parsed from batch006 record
  accessed_at: '2026-10-21T07:49:48Z'
  support: supports
  summary: Both encodings give the full native key, formula C19H18O7, neutral charge,
    one fragment, average mass358.346 and exact mass358.105252916. Calculation was
    run with the batch005 locked interpreter while cwd was batch006 because RDKit
    had not yet been installed in batch006; the coordinator subsequently installed
    it locally.
  snapshot_sha256: a8a5c8da632c6120f879aecdee6dd74fb56f37802a7ec2f685f816211b54e2ca
- evidence_id: primary
  kind: primary_source
  reference: PMID:7798967
  locator: DOI10.1021/np50111a023; Europe PMC core primary abstract
  accessed_at: '2026-10-21T07:49:50Z'
  support: supports
  summary: The1994 primary abstract maps the exact hydroxyflavone to compound2, isolated
    from Calliandra californica, structurally characterized and synthesized. It explicitly
    reports antimicrobial activity for two test bacterial strains. It does not name
    strains, provide assay methods or numeric endpoints, or establish a target. MeSH
    organism tags are indexing, not compound-specific positive assay results.
  snapshot_sha256: 128e62aeafe713bdc4474b31268d5e73bcf0873c878d4395fc09c176bedaa284
- evidence_id: synthesis
  kind: primary_source
  reference: https://actachemscand.ki.ku.dk/pdf/acta_vol_49_p0357-0360.pdf
  locator: DOI10.3891/acta.chem.scand.49-0357; complete four-page paper, pp357-360;
    compound map and Tables1-2 on p358; exact synthesis p360
  accessed_at: '2026-10-21T07:51:47Z'
  support: supports
  summary: The1995 primary paper confirms synthesis and characterization of this exact
    hydroxyflavone, numbered1 in this paper, and reports identity with the natural
    material. Its introduction distinguishes the inactive nonhydroxylated companion
    from the antibacterial hydroxyflavone, citing the1994 study. The inspected paper
    supplies chemical synthesis/NMR evidence, not new organism-specific assay measurements
    or an antibacterial molecular mechanism. Pages357,358 and360 were visually inspected;
    all four pages were read including OCR of the scanned text.
  snapshot_sha256: 1dc295839ff50ba4a594abe65b13ce9d82f1478619e4ee1f467272b6a23f0cc7
- evidence_id: registry
  kind: authority
  reference: https://www.reaxys.com/reaxys/secured/search.do?searchType=quick&rid=7313462
  locator: Direct registry detail attempt
  accessed_at: '2026-10-21T07:53:07Z'
  support: partial
  summary: Direct Reaxys substance detail was inaccessible. The xref is verified only
    as the current official ChEBI assertion, with no independently inspected registry
    structure.
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: Ignored-inclusive local references and bounded free primary discovery
  accessed_at: '2026-10-21T07:53:07Z'
  support: context_only
  summary: Local source and PATHS agree. Readiness material was only a discovery lead.
    Free discovery located the1994 primary abstract and the complete1995 synthesis
    paper. ACS main text was unavailable, and the ACS Figshare resource-DOI query
    returned an empty list. Other positional isomers, the nonhydroxylated companion
    and whole-plant/extract activity were not transferred.
  search_scope: prepare.py51 used rg --no-ignore --hidden across batch006 excluding
    .git/.venv; follow-up searches included curation, conf, reviews, reports and PATHS
    for exact label, CHEBI66040, full key, minted identifier, PMID7798967 and Reaxys7313462.
    Hidden and ignored files were included. Web queries used the exact compound name,
    DOI10.1021/np50111a023, synthesis1995 and antibacterial terms; primary abstract
    was inspected via PubMed and Europe PMC, and the1995 primary PDF through the University
    of Copenhagen Acta archive.
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Exact-compound, activity, producer and mechanism rules
  accessed_at: '2026-10-21T07:53:07Z'
  support: supports
  summary: Optional blanks alone are not defects. Chemical synthesis, plant isolation,
    antibacterial growth inhibition and molecular mechanism are distinct claims. A
    whole-plant isolation record does not establish a specific biosynthetic producer
    process or permit transfer from related flavones.
- evidence_id: validation
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual batch006 focused executions; 051-validation.tsv
  accessed_at: '2026-10-21T07:49:27Z'
  support: supports
  summary: LinkML validation exited0 with no issues. Strict validation scanned one
    target and exited0 with no ERROR rows.
  snapshot_sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
assessments:
- assessment_id: identity
  area: identity
  topic: Exact hydroxy/methoxy positions
  outcome: supported
  summary: The native structure is the exact five-substituent flavone. Current ChEBI/PubChem,
    independent chemistry and the primary synthesis agree. Compound2 in1994 is compound1
    in1995; numbering is paper-specific.
  target_ids:
  - CHEBI:66040
  evidence_ids:
  - record
  - chebi
  - pubchem
  - chemistry
  - primary
  - synthesis
- assessment_id: grounding
  area: grounding
  topic: Broader parents and antibacterial role
  outcome: supported
  summary: Both structural parents and the antibacterial role are appropriate. Registry
    detail remains source-asserted and unavailable independently.
  target_ids:
  - CHEBI:66040
  evidence_ids:
  - chebi
  - parent-38687
  - parent-76875
  - registry
  - primary
- assessment_id: definition
  area: evidence
  topic: Natural isolation and broad antibacterial classification
  outcome: supported
  summary: The original abstract supports isolation from Calliandra californica and
    antibacterial activity of the exact compound; the follow-up synthesis confirms
    identity and distinguishes the nonhydroxylated companion. Native broad wording
    is appropriately bounded.
  target_ids:
  - CHEBI:66040
  evidence_ids:
  - record
  - primary
  - synthesis
- assessment_id: activity
  area: evidence
  topic: Strain-resolved activity and mechanism
  outcome: unknown
  summary: The inspected original abstract lacks strain names, assay protocol and
    numbers. The synthesis paper provides no new microbiological endpoint or direct
    target. No quantitative activity or mechanism is asserted natively, and neither
    MeSH nor other-flavone studies can fill those gaps.
  target_ids:
  - CHEBI:66040
  evidence_ids:
  - record
  - primary
  - synthesis
  - rubric
- assessment_id: producer
  area: completeness
  topic: Plant isolation versus biosynthetic production
  outcome: unknown
  summary: Plant isolation is already represented in the definition. Exact tissue/voucher
    and biosynthetic source were not independently verified in the original main text,
    so the lack of a structured producer assertion is not made a defect.
  target_ids:
  - CHEBI:66040
  evidence_ids:
  - record
  - primary
  - chebi
  - rubric
- assessment_id: other
  area: scope
  topic: Resistance, clinical status and datasets
  outcome: not_applicable
  summary: No native assertions require adjudication in these fields. The inspected
    primary studies do not establish resistance determinants, clinical product status
    or transcriptomic datasets.
  target_ids:
  - CHEBI:66040
  evidence_ids:
  - record
  - primary
  - synthesis
- assessment_id: provenance
  area: provenance
  topic: Generated field ownership and history
  outcome: supported
  summary: Raw source, minted identifier, source version and three seed/reseed events
    agree. Native SEEDED status is retained; a scientific review is not curation sign-off.
  target_ids:
  - CHEBI:66040
  evidence_ids:
  - record
  - owner
  - rubric
- assessment_id: schema
  area: schema
  topic: Focused native gates
  outcome: supported
  summary: Both focused validators pass.
  target_ids:
  - CHEBI:66040
  evidence_ids:
  - validation
findings: []
actions: []
limitations:
- The1994 primary main text was unavailable through attempted free routes. Its abstract
  supports the exact compound and broad antibacterial activity, but named strains,
  assay endpoints, quantities and tissue/voucher details were not verified.
- The1995 full synthesis paper supplies chemical identity evidence and retrospectively
  discusses antibacterial activity; it is not a new microbiological assay or mechanism
  study.
- Direct Reaxys detail was unavailable, so the xref is verified only as an official
  ChEBI assertion.
- Bounded primary discovery does not establish absence of further exact-compound studies.
  Optional unpopulated fields were not treated as errors.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Initial capture preceded judgment; all original input hashes and Git base were retained
  in the expanded20-input provenance.
- The independent chemistry calculation used the batch005 environment with batch006
  cwd; later installation of batch006 RDKit did not change the assessed native inputs.
- Ignored and hidden files were included in local searches. No native content or scientific
  status was changed.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:66040
- https://doi.org/10.1021/np50111a023
- https://doi.org/10.3891/acta.chem.scand.49-0357
tags:
- antibacterial
- flavone
- exact-positional-identity
- seeded
```
