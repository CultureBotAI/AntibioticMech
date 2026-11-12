# Apigenin 7-O-beta-D-glucoside(1−): correct structure, incorrect deprotonation locant

- Review: 20261021T090211Z-apigenin-7-o-beta-d-glucoside-1-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:49:18Z
- Finished UTC: 2026-10-21T09:02:11Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact monoanion is chemically consistent and agrees with ChEBI/PubChem, but the imported definition says the glycosylated7-position loses a hydroxyl proton. Its actual structure and IUPAC name identify the5-olate. A minor definition correction is needed; neutral-compound antimicrobial studies cannot be transferred as measurements on an isolated monoanion.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position100; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:77722 | data/antibiotics/antibacterial/apigenin-7-o-β-d-glucoside-1.yaml | generated | apigenin 7-O-β-D-glucoside(1−) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:77722 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:77722 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:77722 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:77722 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:77722 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:77722 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:77722 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:77722 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:77722 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:77722 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:77722 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:77722 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact monoanion representation

identity: supported. Targets: CHEBI:77722.

Native SMILES/InChI, formula, charge, stereochemistry, mass and PubChem full key agree. Related neutral synonym is correctly scoped.

### Deprotonation site

evidence: concern. Targets: CHEBI:77722.

The7-position is glycosylated; the encoded negative oxygen is at5. Source definition and structure conflict.

### Oxoanion class and antibacterial role

grounding: supported. Targets: CHEBI:77722.

The parent is appropriate and the role is a correctly reproduced ontology classification; it is not a quantitative exact-ion assay assertion.

### Major microspecies prediction

evidence: unknown. Targets: CHEBI:77722.

Marvinv6.2.0/pH7.3 wording identifies a computational prediction; no independent pKa/speciation validation was performed.

### Exact-form primary evidence

completeness: unknown. Targets: CHEBI:77722.

Selected neutral-form studies offer assay-specific context, not direct isolated-monoanion potency or efflux-mechanism evidence. Optional native blanks are not defects.

### Structured expression applicability

scope: not_applicable. Targets: CHEBI:77722.

Native contains no gene/protein/pathway/stress/transcriptomic claim requiring a structured query.

### Generated definition correction

ownership: supported. Targets: CHEBI:77722.

Maintained ChEBI row and extractor/seeder provenance explain the wording; no native fields changed.

## Findings

### F1: Correct the deprotonation locant from7 to5

minor / open / confirmed; issue key: chebi-77722-apigenin-glucoside-anion-deprotonation-locant.

The definition says deprotonation of7-hydroxy, but position7 carries the glycosidic linkage and no OH proton. The exact IUPAC name and encoded structure identify5-olate. This source-propagated textual error does not invalidate the otherwise consistent monoanion structure.

## Recommended Actions And Acceptance Checks

### A1

Correct the source-owned definition to describe deprotonation at5 while preserving the exact monoanion and prediction qualifier.

- Verify the5-olate against the graph and exact IUPAC name and correct through a maintained source/curation route so reseeding does not restore the7-hydroxy error.
- Retain7-O-beta-D-glycosylation, charge−1 and the native full stereochemical identity. Do not replace with neutral CHEBI16778 or transfer neutral-form assay values as exact isolated-ion observations.
- Keep the pH7.3/Marvinv6.2.0 statement explicitly predictive unless independent experimental speciation evidence is curated; do not imply measured predominance.
- Preserve claim-level evidence, writer/history and rerun focused native validators, term/reference/history and required corpus gates after authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/apigenin-7-o-β-d-glucoside-1.yaml; Entire YAML and three seed/reseed history entries | supports | SEEDED/EXACT CHEBI77722 with one flavonoid-oxoanion parent, one antibacterial role and five specified sugar centers. Formula C21H19O10 with separate charge−1 is appropriate. Neutral apigenin7-O-glucoside is only a RELATED synonym. No adopted PMID, exact chemical xref, measured activity, target, producer or clinical assertion is present. |
| owner | data/raw/chebi_antimicrobials.tsv; 100-raw.json; extractor/seeder and accepted role source | supports | The adopted ChEBI row repeats the7-hydroxy deprotonation statement and Marvinv6.2.0 major-microspecies prediction at pH7.3. The source contains no citation lead. All thirteen captured maintained input hashes are unchanged. |
| authority | https://www.ebi.ac.uk/chebi/CHEBI:77722; 100-chebi.html/visible; definition, IUPAC, structure and ontology | refutes | Current ChEBI repeats the erroneous7-hydroxy wording but names the anion as chromen-5-olate and depicts7-O-glycosylation. That glycosidic oxygen has no hydroxyl proton to remove. The definition must say5-hydroxy deprotonation to match the encoded structure; database repetition does not remove the internal contradiction. |
| neutral | https://www.ebi.ac.uk/chebi/CHEBI:16778; 100-neutral-correct.html; complete chemical/name/ontology fields | supports | ChEBI explicitly relates the neutral conjugate acid CHEBI16778 to77722. Neutral formula C21H20O10 and key ending-N differ from the monoanion ending-M. Both retain beta-D sugar stereochemistry;7-O-glycosylation and a free5-OH in the neutral form are explicit. CHEBI60038 is the appropriate broader flavonoid-oxoanion parent. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/86289341; 100-pubchem.json | supports | Exact CID agrees on KMOUJOKENFFTPU-QNDFHXLGSA-M, charge−1 and structure. This corroborates the encoded monoanion, not experimental speciation or exact-ion biological potency. |
| chemistry | Independent RDKit calculation; 100-chemistry.json; focus010-root.py100 | supports | SMILES and InChI regenerate the full key, five assigned centers, one component, net−1, average431.373 and exact431.098370388. RDKit renders formula C21H19O10- while the native stores formula without the separately represented charge; normalized comparison passes. The source mint agrees. The initial formula-string helper failure was corrected, not treated as a native defect. |
| origanum | PMID:40457736; DOI:10.1080/13880209.2025.2511805; PMC12135086 abstract,Methods,Results,Discussion and compound2 NMR assignments | context_only | The2025 original studies neutral named apigenin7-O-glucoside isolated from Origanum majorana with1D/2D NMR. MIC is greater than100µM against E.coli ATCC25922 and MRSA ATCC43300. Crystal-violet biomass falls33.75±1.62% and42.98±2.18% for E.coli at50/100µM during biofilm formation. MRSA results are13.38±0.87% and−1.10±0.67%; authors classify it ineffective. This is not mature-biofilm eradication or bacterial killing. Compound2 does not show efflux inhibition in the ethidium-accumulation assay; arbutin results must not be transferred. |
| terminalia | PMID:40942120; DOI:10.3390/molecules30173595; PMC12430666 complete abstract,Results and Methods | context_only | The2025 Terminalia catappa paper reports a purified band assigned neutral apigenin7-O-beta-D-glucopyranoside, with MRSA1503 and clinical S.aureus MIC9.5µg/mL. Identity confidence is limited by unexplained nitrile/carboxyl interpretations absent from the proposed molecule and a stated500–1000 mass scan versus reported m/z433.11. No quantitative isolated-monoanion composition is established. These values are not imported as exact-ion measurements. |
| search | CultureBotAI/AntibioticMech; 100-local-hits.txt;099100-maintained-hits.txt;100-discovery.json | context_only | Ignored-inclusive local search found the source/queue context. Current ChEBI/PubChem and bounded neutral-compound literature were inspected; no exhaustive literature absence is claimed. The first guessed neutral ChEBI16238 page was a different entity and excluded; the verified conjugate acid is16778. |

## Limits And Additional Notes

- The native has no adopted PMID. Selected2025 primary papers were read in the explicitly listed sections, not all supplementary/raw spectral data. The Terminalia structural inconsistencies limit confident exact-material assignment and the Origanum data are bounded by strains, concentrations and endpoints.
- No experimental pKa, solution microspecies distribution or isolated-anion antimicrobial assay was established. Neutral-compound results can inform a qualified parent-moiety discussion, not automatic exact-ion activity rows.
- The initial RDKit formula comparison failed only because the helper included a charge suffix; normalization respects the schema separate charge field. Corrected chemistry and both native validators pass.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T090211Z-apigenin-7-o-beta-d-glucoside-1-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Apigenin 7-O-beta-D-glucoside(1−): correct structure, incorrect deprotonation
  locant'
started_at: '2026-10-21T08:49:18Z'
finished_at: '2026-10-21T09:02:11Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the native record. The entire record
    and maintained source were read, independent chemistry calculated, asserted chemical
    groundings checked and exact-compound primary literature assessed with explicit
    access boundaries.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The exact monoanion is chemically consistent and agrees with ChEBI/PubChem,
  but the imported definition says the glycosylated7-position loses a hydroxyl proton.
  Its actual structure and IUPAC name identify the5-olate. A minor definition correction
  is needed; neutral-compound antimicrobial studies cannot be transferred as measurements
  on an isolated monoanion.
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
  - path: data/antibiotics/antibacterial/apigenin-7-o-β-d-glucoside-1.yaml
    sha256: f0156be38875f84f22b7193dee1d60feb17681b233ca9bf40c17bc4bd99a5925
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
- target_id: CHEBI:77722
  path: data/antibiotics/antibacterial/apigenin-7-o-β-d-glucoside-1.yaml
  label: apigenin 7-O-β-D-glucoside(1−)
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
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position100; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:77722
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:77722
  command: .venv/bin/python /private/tmp/am-review-session/focus010-root.py 100
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:77722
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/apigenin-7-o-β-d-glucoside-1.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:77722
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/apigenin-7-o-β-d-glucoside-1.yaml --out /private/tmp/am-review-session/100-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:77722
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
  - CHEBI:77722
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
  - CHEBI:77722
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
  - CHEBI:77722
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
  - CHEBI:77722
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
  - CHEBI:77722
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
  - CHEBI:77722
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
  - CHEBI:77722
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
  - CHEBI:77722
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/apigenin-7-o-β-d-glucoside-1.yaml
  locator: Entire YAML and three seed/reseed history entries
  accessed_at: '2026-10-21T08:57:52Z'
  support: supports
  summary: SEEDED/EXACT CHEBI77722 with one flavonoid-oxoanion parent, one antibacterial
    role and five specified sugar centers. Formula C21H19O10 with separate charge−1
    is appropriate. Neutral apigenin7-O-glucoside is only a RELATED synonym. No adopted
    PMID, exact chemical xref, measured activity, target, producer or clinical assertion
    is present.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: 100-raw.json; extractor/seeder and accepted role source
  accessed_at: '2026-10-21T08:57:52Z'
  support: supports
  summary: The adopted ChEBI row repeats the7-hydroxy deprotonation statement and
    Marvinv6.2.0 major-microspecies prediction at pH7.3. The source contains no citation
    lead. All thirteen captured maintained input hashes are unchanged.
  snapshot_sha256: 7c3cd0c1b497cdbe73796b5f79a72ef62b0becf3a0305aa14fc5510c38185603
- evidence_id: authority
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:77722
  locator: 100-chebi.html/visible; definition, IUPAC, structure and ontology
  accessed_at: '2026-10-21T08:57:52Z'
  support: refutes
  summary: Current ChEBI repeats the erroneous7-hydroxy wording but names the anion
    as chromen-5-olate and depicts7-O-glycosylation. That glycosidic oxygen has no
    hydroxyl proton to remove. The definition must say5-hydroxy deprotonation to match
    the encoded structure; database repetition does not remove the internal contradiction.
  snapshot_sha256: 1c80f57bc337a604a8afc48445c2693520a3c1acb7cc468c88434b633c42af23
- evidence_id: neutral
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:16778
  locator: 100-neutral-correct.html; complete chemical/name/ontology fields
  accessed_at: '2026-10-21T08:57:52Z'
  support: supports
  summary: ChEBI explicitly relates the neutral conjugate acid CHEBI16778 to77722.
    Neutral formula C21H20O10 and key ending-N differ from the monoanion ending-M.
    Both retain beta-D sugar stereochemistry;7-O-glycosylation and a free5-OH in the
    neutral form are explicit. CHEBI60038 is the appropriate broader flavonoid-oxoanion
    parent.
  snapshot_sha256: e834cc45ded42d27b0636066fae6ba72cdeb45b47e64f636e73d68958b94b24e
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/86289341
  locator: 100-pubchem.json
  accessed_at: '2026-10-21T08:57:52Z'
  support: supports
  summary: Exact CID agrees on KMOUJOKENFFTPU-QNDFHXLGSA-M, charge−1 and structure.
    This corroborates the encoded monoanion, not experimental speciation or exact-ion
    biological potency.
  snapshot_sha256: 9278207d10911d2921b64ea4626153e819ad588efd1be408f8cab09a38436ba2
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit calculation
  locator: 100-chemistry.json; focus010-root.py100
  accessed_at: '2026-10-21T08:57:52Z'
  support: supports
  summary: SMILES and InChI regenerate the full key, five assigned centers, one component,
    net−1, average431.373 and exact431.098370388. RDKit renders formula C21H19O10-
    while the native stores formula without the separately represented charge; normalized
    comparison passes. The source mint agrees. The initial formula-string helper failure
    was corrected, not treated as a native defect.
  snapshot_sha256: 9609ad4a2b26a0d00113776dacf001b3e2f61f31ea6cdf034fd9cce88923626e
- evidence_id: origanum
  kind: primary_source
  reference: PMID:40457736
  locator: DOI:10.1080/13880209.2025.2511805; PMC12135086 abstract,Methods,Results,Discussion
    and compound2 NMR assignments
  accessed_at: '2026-10-21T08:57:52Z'
  support: context_only
  summary: The2025 original studies neutral named apigenin7-O-glucoside isolated from
    Origanum majorana with1D/2D NMR. MIC is greater than100µM against E.coli ATCC25922
    and MRSA ATCC43300. Crystal-violet biomass falls33.75±1.62% and42.98±2.18% for
    E.coli at50/100µM during biofilm formation. MRSA results are13.38±0.87% and−1.10±0.67%;
    authors classify it ineffective. This is not mature-biofilm eradication or bacterial
    killing. Compound2 does not show efflux inhibition in the ethidium-accumulation
    assay; arbutin results must not be transferred.
  snapshot_sha256: 4a014cd86b7dfa5b736e5eb8402a9a92734822378c0290a90d15cc11432adeac
- evidence_id: terminalia
  kind: primary_source
  reference: PMID:40942120
  locator: DOI:10.3390/molecules30173595; PMC12430666 complete abstract,Results and
    Methods
  accessed_at: '2026-10-21T08:57:52Z'
  support: context_only
  summary: The2025 Terminalia catappa paper reports a purified band assigned neutral
    apigenin7-O-beta-D-glucopyranoside, with MRSA1503 and clinical S.aureus MIC9.5µg/mL.
    Identity confidence is limited by unexplained nitrile/carboxyl interpretations
    absent from the proposed molecule and a stated500–1000 mass scan versus reported
    m/z433.11. No quantitative isolated-monoanion composition is established. These
    values are not imported as exact-ion measurements.
  snapshot_sha256: d65c10c95abdc8efba1cfa2fc04457997ad6c7cbfcd62657d0b50943b95fdb74
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 100-local-hits.txt;099100-maintained-hits.txt;100-discovery.json
  accessed_at: '2026-10-21T08:57:52Z'
  support: context_only
  summary: Ignored-inclusive local search found the source/queue context. Current
    ChEBI/PubChem and bounded neutral-compound literature were inspected; no exhaustive
    literature absence is claimed. The first guessed neutral ChEBI16238 page was a
    different entity and excluded; the verified conjugate acid is16778.
  search_scope: rg --no-ignore --hidden in isolated batch010 excluding.git/.venv;
    narrower maintained search excludes large.obo/.jsonl/.html files. EuropePMC apigenin7-O-glucoside
    antibacterial/biofilm search, selected original open papers, official ChEBI/PubChem/OLS.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact monoanion representation
  outcome: supported
  summary: Native SMILES/InChI, formula, charge, stereochemistry, mass and PubChem
    full key agree. Related neutral synonym is correctly scoped.
  target_ids:
  - CHEBI:77722
  evidence_ids:
  - native
  - chemistry
  - pubchem
  - neutral
- assessment_id: definition
  area: evidence
  topic: Deprotonation site
  outcome: concern
  summary: The7-position is glycosylated; the encoded negative oxygen is at5. Source
    definition and structure conflict.
  target_ids:
  - CHEBI:77722
  evidence_ids:
  - authority
  - neutral
  - owner
- assessment_id: class
  area: grounding
  topic: Oxoanion class and antibacterial role
  outcome: supported
  summary: The parent is appropriate and the role is a correctly reproduced ontology
    classification; it is not a quantitative exact-ion assay assertion.
  target_ids:
  - CHEBI:77722
  evidence_ids:
  - native
  - authority
  - owner
- assessment_id: speciation
  area: evidence
  topic: Major microspecies prediction
  outcome: unknown
  summary: Marvinv6.2.0/pH7.3 wording identifies a computational prediction; no independent
    pKa/speciation validation was performed.
  target_ids:
  - CHEBI:77722
  evidence_ids:
  - owner
  - authority
- assessment_id: biology
  area: completeness
  topic: Exact-form primary evidence
  outcome: unknown
  summary: Selected neutral-form studies offer assay-specific context, not direct
    isolated-monoanion potency or efflux-mechanism evidence. Optional native blanks
    are not defects.
  target_ids:
  - CHEBI:77722
  evidence_ids:
  - origanum
  - terminalia
  - native
- assessment_id: adapter
  area: scope
  topic: Structured expression applicability
  outcome: not_applicable
  summary: Native contains no gene/protein/pathway/stress/transcriptomic claim requiring
    a structured query.
  target_ids:
  - CHEBI:77722
  evidence_ids:
  - native
- assessment_id: ownership
  area: ownership
  topic: Generated definition correction
  outcome: supported
  summary: Maintained ChEBI row and extractor/seeder provenance explain the wording;
    no native fields changed.
  target_ids:
  - CHEBI:77722
  evidence_ids:
  - owner
  - search
findings:
- finding_id: F1
  issue_key: chebi-77722-apigenin-glucoside-anion-deprotonation-locant
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the deprotonation locant from7 to5
  description: The definition says deprotonation of7-hydroxy, but position7 carries
    the glycosidic linkage and no OH proton. The exact IUPAC name and encoded structure
    identify5-olate. This source-propagated textual error does not invalidate the
    otherwise consistent monoanion structure.
  target_ids:
  - CHEBI:77722
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - authority
  - neutral
  - chemistry
  - owner
  rule_id: 'native-review-checklist: Definition and Structure consistency'
  native_severity: minor atom-locant error in definition
  normalization_reason: Identity, formula, charge and stereo are already consistent;
    a localized definition correction resolves the contradiction.
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
  description: Correct the source-owned definition to describe deprotonation at5 while
    preserving the exact monoanion and prediction qualifier.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:77722
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
  - Verify the5-olate against the graph and exact IUPAC name and correct through a
    maintained source/curation route so reseeding does not restore the7-hydroxy error.
  - Retain7-O-beta-D-glycosylation, charge−1 and the native full stereochemical identity.
    Do not replace with neutral CHEBI16778 or transfer neutral-form assay values as
    exact isolated-ion observations.
  - Keep the pH7.3/Marvinv6.2.0 statement explicitly predictive unless independent
    experimental speciation evidence is curated; do not imply measured predominance.
  - Preserve claim-level evidence, writer/history and rerun focused native validators,
    term/reference/history and required corpus gates after authorized curation.
limitations:
- The native has no adopted PMID. Selected2025 primary papers were read in the explicitly
  listed sections, not all supplementary/raw spectral data. The Terminalia structural
  inconsistencies limit confident exact-material assignment and the Origanum data
  are bounded by strains, concentrations and endpoints.
- No experimental pKa, solution microspecies distribution or isolated-anion antimicrobial
  assay was established. Neutral-compound results can inform a qualified parent-moiety
  discussion, not automatic exact-ion activity rows.
- The initial RDKit formula comparison failed only because the helper included a charge
  suffix; normalization respects the schema separate charge field. Corrected chemistry
  and both native validators pass.
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
