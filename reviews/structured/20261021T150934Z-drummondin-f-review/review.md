# Drummondin F: coherent tautomeric identity with unresolved stereochemistry

- Review: 20261021T150934Z-drummondin-f-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:52:07Z
- Finished UTC: 2026-10-21T15:09:34Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native neutral graph is coherent and matches current ChEBI and the named PubChem structure after an explicit keto–enol comparison. Original 1989 and 1991 indexed abstracts support isolation and antibacterial activity. One stereocentre and full primary characterization remain unresolved; no confirmed native correction is established. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position381; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65811 | data/antibiotics/antibacterial/drummondin-f.yaml | generated | drummondin F |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:65811 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:65811 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:65811 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:65811 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65811 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65811 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65811 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65811 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65811 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65811 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65811 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65811 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Neutral connectivity and tautomerism

identity: supported. Targets: CHEBI:65811.

Five chemical encodings agree after explicit atom mapping and stereo-preserving tautomer handling. No salt, hydrate, different composition or positional isomer is substituted.

### Unassigned centre and positive-rotation name

identity: unknown. Targets: CHEBI:65811.

The graph has one unspecified centre. The original full characterization and rotation conditions were not recovered, so neither R/S assignment, wrong epimer nor racemic state is established.

### Chemical classes and CAS provenance

grounding: supported. Targets: CHEBI:65811.

Five broader classes match the graph. Registry association is corroborated through authority and primary indexing without claiming proprietary-registry access.

### Plant origin and antibacterial scope

evidence: supported. Targets: CHEBI:65811.

The adopted original abstract supports stems/leaves and the named bacteria; the earlier original independently reports compound F antibacterial activity with cytotoxicity. Exact strain and assay details remain unavailable.

### Mechanism and optional evidence objects

completeness: unknown. Targets: CHEBI:65811.

No native target claim requires correction. Neighboring D/E docking cannot be transferred to F, and absent optional fields do not establish a defect. No native gene, regulator or transcriptomic claim requires a structured gene adapter.

### Resistance, clinical status and causal graph

scope: not_applicable. Targets: CHEBI:65811.

No such native assertion is populated. Natural plant origin does not establish a microbial producer or clinical efficacy.

### Source ownership and history

provenance: supported. Targets: CHEBI:65811.

All fourteen captured inputs, deterministic identifier and ordered history remain consistent. The adopted citation and additional original source have explicit access boundaries.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optionally recover both original characterization reports before curating stereochemistry, quantitative potency or an assignment chronology.

- Read the original structure drawings, spectral data, optical rotation and exact assay conditions.
- Preserve keto–enol equivalence and do not infer R/S from a (+) name.
- Keep drummondin D/E docking and whole-extract data separate from exact drummondin F.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/drummondin-f.yaml; Entire YAML including definition, two names, five parents, all chemical fields, CAS, source and three history events | supports | The SEEDED/EXACT record has C28H34O8, neutral charge and WWTZMJRKACJQRR-UHFFFAOYSA-N. It describes filicinic-acid derivation, H. drummondii stems/leaves and activity against S. aureus, B. subtilis and M. smegmatis. No quantitative observations, molecular targets, resistance, clinical assertions, structured producer or causal graph are populated. |
| owners | data/raw/chebi_antimicrobials.tsv; scripts/seed_from_sources.py; Source row1316; readiness row1076;381-source-rows.json; initial thirteen inputs and appended readiness file | supports | All seeded fields reproduce the adopted ChEBI row. Its only PMID lead is1800634. Fourteen captured hashes remain unchanged and the deterministic source mint and three ordered seed histories agree. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/65811/; Complete current entry: names, structural fields, ontology relations, identifiers and origin metadata | supports | Current ChEBI matches the native structure, names, CAS and structural classes. Its definition supports stems/leaves; separate compound-origin metadata says root, contrary to that definition and the1991 original abstract. Root is not a native assertion and is not substituted for supported stem/leaf origin. |
| chemistry | Independent RDKit2026.03.5 / InChI1.07.3; 381-authority-chemistry.py and381-authority-chemistry-extended.py; five encodings and exact bond mapping | supports | Native SMILES/InChI and current ChEBI molfile match. PubChem129595 uses IDWYGCPWMNLBEA-UHFFFAOYSA-N, a different keto–enol representation: heavy-atom topology, formula and charge agree, with four mapped bond-order changes. Reciprocal chirality-aware canonical-tautomer matching agrees with stereo removal disabled. Every original graph retains one unassigned stereocentre. Initial enumeration hit a transform limit despite matching; the extended100000-transform/10000-tautomer run also exited0 without that warning. |
| aliases | PubChem129595 synonyms; original PubMed1800634 chemical indexing; 381-pubchem-synonyms.json and381-leads.json complete relevant names/indexing | supports | Both systematic representations, (+)-drummondin F and CAS122127-73-5 are associated with the named compound. Original chemical indexing independently associates that CAS with drummondin F. No proprietary CAS record was accessed; positive rotation does not establish absolute R/S configuration. |
| parents | CHEBI:22707; CHEBI:33823; CHEBI:51689; CHEBI:51867; CHEBI:76224; CHEBI:71593; 039-parent-22707.json and previously inspected379380 parent definitions; graph-level comparison | supports | The benzene ring bears three hydroxyl groups, fitting benzenetriol. Enol, enone, methyl ketone and aromatic ketone classes also fit. Filicinic acid is a functional parent, distinct from a broader structural-class assertion. |
| primary1991 | https://doi.org/10.1021/np50077a013; PMID1800634 complete original indexed abstract and chemical indexing | supports | The adopted paper identifies drummondin F among isolated H. drummondii stem/leaf hexane constituents, reports spectroscopic characterization and antibacterial activity against the three named species. It supplies no compound-specific strain, MIC, assay conditions or absolute stereochemistry at abstract depth. |
| primary1989 | https://doi.org/10.1021/np50062a018; PMID2746258 complete original indexed abstract | supports | The earlier original explicitly names drummondin F as compound4 among bioassay-fractionated H. drummondii constituents. It reports antibacterial activity and cytotoxicity in cultured cancer cells, with no cell-type selectivity. Abstract-level characterization does not independently adjudicate the relationship between the1989 and1991 structural assignments. Broad activity is supported; exact numerical potency and safety are not imported. |
| related-docking | https://doi.org/10.3390/antibiotics5030030; PMC5039526 exact drummondin Results paragraph | context_only | The inspected paragraph reports UGM docking for drummondin D and E, not F. Those neighboring compounds do not provide a direct molecular-target result for this record. No mechanistic claim is transferred. |
| access | Public chemical authorities and exact original-paper discovery; 039-root-fetch manifests1–7;381-owners-search.json;381-discovery.json; original DOI requests | supports | Publisher full texts for both original papers returned403. The publicly indexed1991 PDF-copy retrieval failed with network-unreachable; it was not read. Broad drummondin search returned529 hits with100 returned; relevant inspected abstracts are identified individually rather than claiming an exhaustive literature review. |

## Limits And Additional Notes

- Both original papers were read at complete indexed-abstract depth. Neither full primary structural characterization nor antibacterial tables were retrieved; no numerical potency or absolute stereochemistry is certified.
- The 1989 abstract already names F whereas the1991 abstract includes F among four new derivatives. Their detailed assignment chronology remains unresolved without the full papers.
- Initial tautomer enumeration emitted a transform-limit warning; the extended run retained the same equivalence without that warning. No stereochemical assignment was introduced.
- Current ChEBI root metadata conflicts with its own definition and the original abstract; native stem/leaf wording remains supported.
- The broad529-hit search was not an exhaustive review. Only explicitly cited source portions were inspected; proprietary CAS was not accessed.
- No native data, maintained source, status or history was edited; shared validation limitations are integrated separately.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T150934Z-drummondin-f-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Drummondin F: coherent tautomeric identity with unresolved stereochemistry'
started_at: '2026-10-21T14:52:07Z'
finished_at: '2026-10-21T15:09:34Z'
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
verdict: blocked
scientific_review: true
summary: The native neutral graph is coherent and matches current ChEBI and the named
  PubChem structure after an explicit keto–enol comparison. Original 1989 and 1991
  indexed abstracts support isolation and antibacterial activity. One stereocentre
  and full primary characterization remain unresolved; no confirmed native correction
  is established. Scientific assessment retains the stated evidence limits; full verification
  is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/drummondin-f.yaml
    sha256: 602f8517431b998555064b282d51d71fa5a7345bc76590743431ec6815ffbc48
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
  - path: curation/record_review_queue.tsv
    sha256: 3828a5120b892ee0ee0b776affc6c3e4f1f1a3355ec4edd30e6005762de00e70
    role: context
targets:
- target_id: CHEBI:65811
  path: data/antibiotics/antibacterial/drummondin-f.yaml
  label: drummondin F
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
  selection: Initially uncovered queue position381; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65811
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65811
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    381
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65811
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/drummondin-f.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65811
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/drummondin-f.yaml --out /private/tmp/am-review-session/381-strict.tsv
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
  - CHEBI:65811
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
  - CHEBI:65811
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
  - CHEBI:65811
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
  - CHEBI:65811
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
  - CHEBI:65811
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
  - CHEBI:65811
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
  - CHEBI:65811
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
  - CHEBI:65811
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
  - CHEBI:65811
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/drummondin-f.yaml
  locator: Entire YAML including definition, two names, five parents, all chemical
    fields, CAS, source and three history events
  accessed_at: '2026-10-21T14:57:44Z'
  support: supports
  summary: The SEEDED/EXACT record has C28H34O8, neutral charge and WWTZMJRKACJQRR-UHFFFAOYSA-N.
    It describes filicinic-acid derivation, H. drummondii stems/leaves and activity
    against S. aureus, B. subtilis and M. smegmatis. No quantitative observations,
    molecular targets, resistance, clinical assertions, structured producer or causal
    graph are populated.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; scripts/seed_from_sources.py
  locator: Source row1316; readiness row1076;381-source-rows.json; initial thirteen
    inputs and appended readiness file
  accessed_at: '2026-10-21T14:57:44Z'
  support: supports
  summary: All seeded fields reproduce the adopted ChEBI row. Its only PMID lead is1800634.
    Fourteen captured hashes remain unchanged and the deterministic source mint and
    three ordered seed histories agree.
  snapshot_sha256: 6f9567c8cb68b897003e40bf2d9743ad8338a64d1787739506044be185560ef0
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/65811/
  locator: 'Complete current entry: names, structural fields, ontology relations,
    identifiers and origin metadata'
  accessed_at: '2026-10-21T14:57:44Z'
  support: supports
  summary: Current ChEBI matches the native structure, names, CAS and structural classes.
    Its definition supports stems/leaves; separate compound-origin metadata says root,
    contrary to that definition and the1991 original abstract. Root is not a native
    assertion and is not substituted for supported stem/leaf origin.
  snapshot_sha256: c1f8445ed18ccb98f52622c0b56a7e2ee281270c7bf0e3ab4df81ec8af2ec8c4
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit2026.03.5 / InChI1.07.3
  locator: 381-authority-chemistry.py and381-authority-chemistry-extended.py; five
    encodings and exact bond mapping
  accessed_at: '2026-10-21T14:57:44Z'
  support: supports
  summary: 'Native SMILES/InChI and current ChEBI molfile match. PubChem129595 uses
    IDWYGCPWMNLBEA-UHFFFAOYSA-N, a different keto–enol representation: heavy-atom
    topology, formula and charge agree, with four mapped bond-order changes. Reciprocal
    chirality-aware canonical-tautomer matching agrees with stereo removal disabled.
    Every original graph retains one unassigned stereocentre. Initial enumeration
    hit a transform limit despite matching; the extended100000-transform/10000-tautomer
    run also exited0 without that warning.'
  snapshot_sha256: af2006294b3e324a2e1741d7f126702cd5d2397c071bf44fbe6038b45597becf
- evidence_id: aliases
  kind: authority
  reference: PubChem129595 synonyms; original PubMed1800634 chemical indexing
  locator: 381-pubchem-synonyms.json and381-leads.json complete relevant names/indexing
  accessed_at: '2026-10-21T14:57:44Z'
  support: supports
  summary: Both systematic representations, (+)-drummondin F and CAS122127-73-5 are
    associated with the named compound. Original chemical indexing independently associates
    that CAS with drummondin F. No proprietary CAS record was accessed; positive rotation
    does not establish absolute R/S configuration.
  snapshot_sha256: 0294d4c56c7e53bdf7d9d4db8f5012b84f6acfbf9b88c7f327dde745dc5bc394
- evidence_id: parents
  kind: authority
  reference: CHEBI:22707; CHEBI:33823; CHEBI:51689; CHEBI:51867; CHEBI:76224; CHEBI:71593
  locator: 039-parent-22707.json and previously inspected379380 parent definitions;
    graph-level comparison
  accessed_at: '2026-10-21T14:57:44Z'
  support: supports
  summary: The benzene ring bears three hydroxyl groups, fitting benzenetriol. Enol,
    enone, methyl ketone and aromatic ketone classes also fit. Filicinic acid is a
    functional parent, distinct from a broader structural-class assertion.
  snapshot_sha256: eb88136fe2adc6f03af1c8712a0269431ce2b52a1c22c4db4a45b8de8844066b
- evidence_id: primary1991
  kind: primary_source
  reference: https://doi.org/10.1021/np50077a013
  locator: PMID1800634 complete original indexed abstract and chemical indexing
  accessed_at: '2026-10-21T14:57:44Z'
  support: supports
  summary: The adopted paper identifies drummondin F among isolated H. drummondii
    stem/leaf hexane constituents, reports spectroscopic characterization and antibacterial
    activity against the three named species. It supplies no compound-specific strain,
    MIC, assay conditions or absolute stereochemistry at abstract depth.
  snapshot_sha256: e9a07ef060cd8dc42e7476e300add99a98ebfeb973f1694465a92a759e05977c
- evidence_id: primary1989
  kind: primary_source
  reference: https://doi.org/10.1021/np50062a018
  locator: PMID2746258 complete original indexed abstract
  accessed_at: '2026-10-21T14:57:44Z'
  support: supports
  summary: The earlier original explicitly names drummondin F as compound4 among bioassay-fractionated
    H. drummondii constituents. It reports antibacterial activity and cytotoxicity
    in cultured cancer cells, with no cell-type selectivity. Abstract-level characterization
    does not independently adjudicate the relationship between the1989 and1991 structural
    assignments. Broad activity is supported; exact numerical potency and safety are
    not imported.
  snapshot_sha256: d4337124c67c83146d8bb63a6d8776a37ca99ee2634bfcc194236d938069fa07
- evidence_id: related-docking
  kind: primary_source
  reference: https://doi.org/10.3390/antibiotics5030030
  locator: PMC5039526 exact drummondin Results paragraph
  accessed_at: '2026-10-21T14:57:44Z'
  support: context_only
  summary: The inspected paragraph reports UGM docking for drummondin D and E, not
    F. Those neighboring compounds do not provide a direct molecular-target result
    for this record. No mechanistic claim is transferred.
  snapshot_sha256: 80c5a65ef46bda6664afd765d3ba70a6f1d2ebae2c8b3f6c7a6f2cdb0306c84b
- evidence_id: access
  kind: search
  reference: Public chemical authorities and exact original-paper discovery
  locator: 039-root-fetch manifests1–7;381-owners-search.json;381-discovery.json;
    original DOI requests
  accessed_at: '2026-10-21T14:57:44Z'
  support: supports
  summary: Publisher full texts for both original papers returned403. The publicly
    indexed1991 PDF-copy retrieval failed with network-unreachable; it was not read.
    Broad drummondin search returned529 hits with100 returned; relevant inspected
    abstracts are identified individually rather than claiming an exhaustive literature
    review.
  search_scope: 2026-10-21 exact name, CHEBI65811, full InChIKey and original citations;
    rg --no-ignore --hidden across curation, conf, scripts, data/raw and .claude includes
    ignored files.
  snapshot_sha256: 98ba9c96d721484d07ad7f988e6c1b46045cb385523edff0de0897adb0c26797
assessments:
- assessment_id: identity
  area: identity
  topic: Neutral connectivity and tautomerism
  outcome: supported
  summary: Five chemical encodings agree after explicit atom mapping and stereo-preserving
    tautomer handling. No salt, hydrate, different composition or positional isomer
    is substituted.
  target_ids:
  - CHEBI:65811
  evidence_ids:
  - native
  - chemistry
  - chebi
  - aliases
- assessment_id: stereo
  area: identity
  topic: Unassigned centre and positive-rotation name
  outcome: unknown
  summary: The graph has one unspecified centre. The original full characterization
    and rotation conditions were not recovered, so neither R/S assignment, wrong epimer
    nor racemic state is established.
  target_ids:
  - CHEBI:65811
  evidence_ids:
  - chemistry
  - aliases
  - primary1989
  - primary1991
  - access
- assessment_id: classes
  area: grounding
  topic: Chemical classes and CAS provenance
  outcome: supported
  summary: Five broader classes match the graph. Registry association is corroborated
    through authority and primary indexing without claiming proprietary-registry access.
  target_ids:
  - CHEBI:65811
  evidence_ids:
  - parents
  - aliases
  - chebi
- assessment_id: activity
  area: evidence
  topic: Plant origin and antibacterial scope
  outcome: supported
  summary: The adopted original abstract supports stems/leaves and the named bacteria;
    the earlier original independently reports compound F antibacterial activity with
    cytotoxicity. Exact strain and assay details remain unavailable.
  target_ids:
  - CHEBI:65811
  evidence_ids:
  - primary1991
  - primary1989
  - chebi
- assessment_id: mechanism
  area: completeness
  topic: Mechanism and optional evidence objects
  outcome: unknown
  summary: No native target claim requires correction. Neighboring D/E docking cannot
    be transferred to F, and absent optional fields do not establish a defect. No
    native gene, regulator or transcriptomic claim requires a structured gene adapter.
  target_ids:
  - CHEBI:65811
  evidence_ids:
  - native
  - related-docking
  - access
- assessment_id: other
  area: scope
  topic: Resistance, clinical status and causal graph
  outcome: not_applicable
  summary: No such native assertion is populated. Natural plant origin does not establish
    a microbial producer or clinical efficacy.
  target_ids:
  - CHEBI:65811
  evidence_ids:
  - native
  - primary1989
  - primary1991
- assessment_id: provenance
  area: provenance
  topic: Source ownership and history
  outcome: supported
  summary: All fourteen captured inputs, deterministic identifier and ordered history
    remain consistent. The adopted citation and additional original source have explicit
    access boundaries.
  target_ids:
  - CHEBI:65811
  evidence_ids:
  - owners
  - access
findings: []
actions:
- action_id: A1
  description: Optionally recover both original characterization reports before curating
    stereochemistry, quantitative potency or an assignment chronology.
  finding_ids: []
  target_ids:
  - CHEBI:65811
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/drummondin-f.yaml
    role: Future curator evidence and history
  acceptance_checks:
  - Read the original structure drawings, spectral data, optical rotation and exact
    assay conditions.
  - Preserve keto–enol equivalence and do not infer R/S from a (+) name.
  - Keep drummondin D/E docking and whole-extract data separate from exact drummondin
    F.
limitations:
- Both original papers were read at complete indexed-abstract depth. Neither full
  primary structural characterization nor antibacterial tables were retrieved; no
  numerical potency or absolute stereochemistry is certified.
- The 1989 abstract already names F whereas the1991 abstract includes F among four
  new derivatives. Their detailed assignment chronology remains unresolved without
  the full papers.
- Initial tautomer enumeration emitted a transform-limit warning; the extended run
  retained the same equivalence without that warning. No stereochemical assignment
  was introduced.
- Current ChEBI root metadata conflicts with its own definition and the original abstract;
  native stem/leaf wording remains supported.
- The broad529-hit search was not an exhaustive review. Only explicitly cited source
  portions were inspected; proprietary CAS was not accessed.
- No native data, maintained source, status or history was edited; shared validation
  limitations are integrated separately.
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
