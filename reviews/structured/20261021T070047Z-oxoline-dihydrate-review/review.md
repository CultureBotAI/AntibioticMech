# Oxoline dihydrate: exact hydrate identity and antimicrobial evidence boundaries

- Review: 20261021T070047Z-oxoline-dihydrate-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T06:53:18Z
- Finished UTC: 2026-10-21T07:00:47Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The exact neutral ketone hydrate, structural parents and seeded provenance are consistent. Historical nasal-ointment use is supported as context, without establishing clinical efficacy. Antibacterial classification is supported at ontology level; exact-compound experimental support remains unresolved. A discovered longevity paper conflates oxoline with a quinolone acid in background discussion and depicts the anhydrous parent, so it cannot supply this hydrate with a validated antibacterial mechanism. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire resolved record and bounded exact-structure source/evidence audit.

Selection: Eleventh initially uncovered record in sorted corpus path order; first target in batch 002. Prior task-owned batch coverage is retained separately.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:78857 | data/antibiotics/antibacterial/2-2-3-3-tetrahydroxy-2-3-dihydronaphthalene-1-4-dione.yaml | generated | 2,2,3,3-tetrahydroxy-2,3-dihydronaphthalene-1,4-dione |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema validation | passed | True | CHEBI:78857 | Target execution exited 0; no validation errors. |
| Documented strict validation | passed | True | CHEBI:78857 | Target execution exited 0; no validation errors. |
| Independent structure and minted identifier assertions | passed | False | CHEBI:78857 | Actual assertions passed. |
| Structured source applicability | not_applicable | False | CHEBI:78857 | The record names no gene, protein, regulator, pathway or expression dataset. Longevity-study context is not a record assertion or antimicrobial target. |
| Authoritative full QC | failed | True | CHEBI:78857 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:78857 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:78857 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:78857 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:78857 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:78857 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:78857 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:78857 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:78857 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### One exact covalent ketone hydrate

identity: supported. Targets: CHEBI:78857.

Stored structure, mass, formula, aliases and ChEBI identity agree. No salt, parent tetrone or oxolinic-acid structure was substituted.

### Broader parents and imported activity role

grounding: supported. Targets: CHEBI:78857.

Parent classes are broader and structurally appropriate; the antibacterial role and filing faithfully reproduce the adopted authority. No exact external chemical xrefs are asserted.

### Historical use versus clinical efficacy

evidence: supported. Targets: CHEBI:78857.

Nasal-ointment use is corroborated as historical context. The record asserts no clinical approval or quantified benefit, and the available metadata do not establish either.

### Independent exact-hydrate antimicrobial evidence

evidence: unknown. Targets: CHEBI:78857.

Classification is ontology-backed. The inspected primary leads do not establish exact-hydrate antibacterial activity; adjacent form and quinolone-acid literature cannot close that gap. This is an evidence limitation, not a proved false role.

### Topoisomerase and target boundary

completeness: unknown. Targets: CHEBI:78857.

The record appropriately leaves mechanism and targets unasserted. An unmapped generic source role and a mismatched literature reference do not justify importing a bacterial topoisomerase mechanism. Native mechanism sign-off remains unresolved.

### Quantities, resistance, producer, datasets and graph

representation: not_applicable. Targets: CHEBI:78857.

No such objects are asserted; no defect is assigned solely to empty optional fields. Longevity, antipsoriatic or quinolone pregnancy findings must retain their own identity and experimental scope.

### Generated ownership and native status

ownership: supported. Targets: CHEBI:78857.

Source row, mapping logic and three seed/reseed events support SEEDED status. Review validation does not promote the record.

## Findings

### F1: Exact-hydrate antimicrobial evidence must be separated from oxolinic acid and parent tetrone

informational / open / confirmed; issue key: chebi-78857-exact-hydrate-antimicrobial-evidence.

The current seed has valid ontology provenance but unresolved independent antibacterial support. A concrete discovered paper mixes an anhydrous oxoline drawing with quinolone-acid background. This cannot justify a new target claim or native promotion. No role correction or inactivity finding is established by the bounded search.

## Recommended Actions And Acceptance Checks

### A1

Locate exact-hydrate antimicrobial experiments and adjudicate the authority role separately from oxolinic-acid and anhydrous-tetrone literature. Preserve a bounded unresolved mechanism rationale if no support is found. Any source-role correction must be evidence-backed and reproducible; do not copy generic topoisomerase claims.

- Each proposed activity or target claim resolves exact chemical form and experimental organism/assay.
- The 2011 background citation and 2006 quinolone study are not presented as experiments on this hydrate.
- Curator annotations use the native validated writer/event; source corrections use maintained extraction and seeding. Run strict validation, corpus reproduction and QC before native status promotion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/2-2-3-3-tetrahydroxy-2-3-dihydronaphthalene-1-4-dione.yaml; Entire generated YAML | supports | One exact ChEBI source, three synonyms, two parents, antibacterial role, neutral structure and three seeder events. No mechanism, target, activity observation, resistance, producer, clinical-status, dataset or graph object is asserted; no activity-collection reference requires expansion. |
| owner | data/raw/chebi_antimicrobials.tsv; CHEBI:78857 row; manifest, source maps and extractor/seeder ownership | supports | All seed fields match. The row cites PMID3016268 and PMID4932223, with empty mechanism_role_ids. Both configured mechanism maps lack generic CHEBI:70727; the extractor collects mapped roles only, so the missing generic topoisomerase role is not seed drift. ChEBI classification provenance is permitted without record-level primary citations. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:78857; Full entry reached from CHEBI:33282 incoming relation | supports | Official definition, three aliases, formula C10H8O6, charge 0, both structure encodings, key and masses agree. Broader parents are ketone hydrate and tetralins. The authority asserts antibacterial, antipsoriatic and generic topoisomerase-inhibitor roles; only the antibacterial role belongs in the adopted activity scope. The functional parent tetrone is not an exact xref. |
| parents | https://www.ebi.ac.uk/chebi/CHEBI:63734; Ketone-hydrate definition; https://www.ebi.ac.uk/chebi/CHEBI:36786 tetralins definition and incoming relations | supports | Both parent terms resolve as broader chemical classes. Formal water addition creates geminal diols; the representation is one covalent hydrate molecule, not a disconnected water salt. |
| mesh | https://meshb.nlm.nih.gov/record/ui?name=oxoline; C003020, notes and narrower concepts M0043933/M0308156 | supports | The NLM entry documents nasal ointment containing the dihydrate. Its parent registry number and narrower hydrate names show why a bare oxoline synonym or registry number should not replace exact structural identity. This is historical use context, not evidence of treatment efficacy. |
| primary1986 | PMID:3016268; Europe PMC core abstract and DOI10.1021/jm00158a031; also https://hero.epa.gov/reference/1469767/ | context_only | The abstract explicitly names the hydrated compound as oxoline, compound 1, while studying antipsoriatic derivatives of another lead. It establishes naming context, not an antibacterial target or MIC; lonapalene and derivative assay results cannot be transferred. |
| primary1970 | PMID:4932223; Europe PMC core title/journal metadata | context_only | The adopted citation resolves to a 1970 Russian report on oxoline prophylaxis during the 1969 influenza epidemic. No abstract was available; no numerical efficacy, assay, exact formulation or mechanism was extracted. |
| primary2011 | DOI:10.1371/journal.pone.0021922; PLOS full article, Results bacterial-growth control paragraphs, Discussion oxoline paragraph, references51–52; Figure5A image visually inspected | context_only | The longevity study depicts anhydrous naphthalenetetrone as oxoline. Its discussion calls oxoline a quinolone/topoisomerase inhibitor and cites an oxoline-acid pregnancy study. These background statements conflict with the displayed nitrogen-free structure. The experiments concern nematode longevity with FUDR and do not establish a hydrate-specific antibacterial MIC or target. |
| quinolone-reference | PMID:16643598; Europe PMC core abstract; DOI10.1111/j.1741-4520.2006.00100.x | context_only | The cited pregnancy paper explicitly describes a quinolone derivative used for urinary infection. It concerns oxolinic acid, not this nitrogen-free hydrate. This supports the reference-scope caution without establishing that all antibacterial activity of the hydrate is impossible. |
| chemistry | RDKit local calculation; /private/tmp/am-review-session/011-chemistry.py and 011-chemistry.json | supports | Both encodings reproduce CWHBUPIYFIPPRI-UHFFFAOYSA-N, C10H8O6, charge 0, one fragment, no stereocenters and masses 224.168/224.032087976. The internal identifier is reproduced from the documented hash rule. |
| search | Inclusive local search and free source searches; 011-local-hits.txt; exact identifier, label and slug; bounded source queries | context_only | Local search found the target, adopted row, source lock, generated products and discovery ledgers. Maintained decision and curator tables had no exact-ID/minted-ID match. No newly inspected exact-hydrate antibacterial experiment emerged; source-name confusion requires explicit attention, not an assertion of universal inactivity. |

## Limits And Additional Notes

- PMID4932223 has no abstract in the inspected Europe PMC record; its title supplies historical study context only. No clinical efficacy or antiviral mechanism is inferred.
- The 1986 source was inspected at abstract level through Europe PMC and EPA HERO. PubMed requests repeatedly returned browser challenges.
- The 2011 primary study depicts the anhydrous tetrone; its chemical-form boundary and mismatched quinolone reference preclude transferring its background topoisomerase claim to the hydrate.
- Bounded searches do not prove that antibacterial activity is absent. No native curation status or data field was changed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T070047Z-oxoline-dihydrate-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Oxoline dihydrate: exact hydrate identity and antimicrobial evidence boundaries'
started_at: '2026-10-21T06:53:18Z'
finished_at: '2026-10-21T07:00:47Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not generate or curate the target. Entire target,
    maintained inputs, official identity, primary abstracts and relevant full-paper
    sections were inspected independently.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: The exact neutral ketone hydrate, structural parents and seeded provenance
  are consistent. Historical nasal-ointment use is supported as context, without establishing
  clinical efficacy. Antibacterial classification is supported at ontology level;
  exact-compound experimental support remains unresolved. A discovered longevity paper
  conflates oxoline with a quinolone acid in background discussion and depicts the
  anhydrous parent, so it cannot supply this hydrate with a validated antibacterial
  mechanism. Scientific assessment retains the stated evidence limits; full verification
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
  - path: data/antibiotics/antibacterial/2-2-3-3-tetrahydroxy-2-3-dihydronaphthalene-1-4-dione.yaml
    sha256: b3343bfc9c3a30061b9403a6829e4a4d15f151946b82f1adbf6ce42e632ad290
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
- target_id: CHEBI:78857
  path: data/antibiotics/antibacterial/2-2-3-3-tetrahydroxy-2-3-dihydronaphthalene-1-4-dione.yaml
  label: 2,2,3,3-tetrahydroxy-2,3-dihydronaphthalene-1,4-dione
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
  description: Entire resolved record and bounded exact-structure source/evidence
    audit.
  selection: Eleventh initially uncovered record in sorted corpus path order; first
    target in batch 002. Prior task-owned batch coverage is retained separately.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:78857
checks:
- check_id: schema
  name: Documented schema validation
  status: passed
  required: true
  summary: Target execution exited 0; no validation errors.
  target_ids:
  - CHEBI:78857
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/2-2-3-3-tetrahydroxy-2-3-dihydronaphthalene-1-4-dione.yaml
  exit_code: 0
- check_id: strict
  name: Documented strict validation
  status: passed
  required: true
  summary: Target execution exited 0; no validation errors.
  target_ids:
  - CHEBI:78857
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/2-2-3-3-tetrahydroxy-2-3-dihydronaphthalene-1-4-dione.yaml
    --out /private/tmp/am-review-session/011-strict.tsv
  exit_code: 0
- check_id: chemistry
  name: Independent structure and minted identifier assertions
  status: passed
  required: false
  summary: Actual assertions passed.
  target_ids:
  - CHEBI:78857
  command: .venv/bin/python /private/tmp/am-review-session/011-chemistry.py
  exit_code: 0
  evidence_ids:
  - chemistry
- check_id: imodulondb
  name: Structured source applicability
  status: not_applicable
  required: false
  summary: The record names no gene, protein, regulator, pathway or expression dataset.
    Longevity-study context is not a record assertion or antimicrobial target.
  target_ids:
  - CHEBI:78857
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:78857
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
  - CHEBI:78857
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
  - CHEBI:78857
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
  - CHEBI:78857
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
  - CHEBI:78857
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
  - CHEBI:78857
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
  - CHEBI:78857
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
  - CHEBI:78857
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
  - CHEBI:78857
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/2-2-3-3-tetrahydroxy-2-3-dihydronaphthalene-1-4-dione.yaml
  locator: Entire generated YAML
  accessed_at: '2026-10-21T06:58:56Z'
  support: supports
  summary: One exact ChEBI source, three synonyms, two parents, antibacterial role,
    neutral structure and three seeder events. No mechanism, target, activity observation,
    resistance, producer, clinical-status, dataset or graph object is asserted; no
    activity-collection reference requires expansion.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: CHEBI:78857 row; manifest, source maps and extractor/seeder ownership
  accessed_at: '2026-10-21T06:58:56Z'
  support: supports
  summary: All seed fields match. The row cites PMID3016268 and PMID4932223, with
    empty mechanism_role_ids. Both configured mechanism maps lack generic CHEBI:70727;
    the extractor collects mapped roles only, so the missing generic topoisomerase
    role is not seed drift. ChEBI classification provenance is permitted without record-level
    primary citations.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:78857
  locator: Full entry reached from CHEBI:33282 incoming relation
  accessed_at: '2026-10-21T06:58:56Z'
  support: supports
  summary: Official definition, three aliases, formula C10H8O6, charge 0, both structure
    encodings, key and masses agree. Broader parents are ketone hydrate and tetralins.
    The authority asserts antibacterial, antipsoriatic and generic topoisomerase-inhibitor
    roles; only the antibacterial role belongs in the adopted activity scope. The
    functional parent tetrone is not an exact xref.
- evidence_id: parents
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:63734
  locator: Ketone-hydrate definition; https://www.ebi.ac.uk/chebi/CHEBI:36786 tetralins
    definition and incoming relations
  accessed_at: '2026-10-21T06:58:56Z'
  support: supports
  summary: Both parent terms resolve as broader chemical classes. Formal water addition
    creates geminal diols; the representation is one covalent hydrate molecule, not
    a disconnected water salt.
- evidence_id: mesh
  kind: database
  reference: https://meshb.nlm.nih.gov/record/ui?name=oxoline
  locator: C003020, notes and narrower concepts M0043933/M0308156
  accessed_at: '2026-10-21T06:58:56Z'
  support: supports
  summary: The NLM entry documents nasal ointment containing the dihydrate. Its parent
    registry number and narrower hydrate names show why a bare oxoline synonym or
    registry number should not replace exact structural identity. This is historical
    use context, not evidence of treatment efficacy.
- evidence_id: primary1986
  kind: primary_source
  reference: PMID:3016268
  locator: Europe PMC core abstract and DOI10.1021/jm00158a031; also https://hero.epa.gov/reference/1469767/
  accessed_at: '2026-10-21T06:58:56Z'
  support: context_only
  summary: The abstract explicitly names the hydrated compound as oxoline, compound
    1, while studying antipsoriatic derivatives of another lead. It establishes naming
    context, not an antibacterial target or MIC; lonapalene and derivative assay results
    cannot be transferred.
- evidence_id: primary1970
  kind: database
  reference: PMID:4932223
  locator: Europe PMC core title/journal metadata
  accessed_at: '2026-10-21T06:58:56Z'
  support: context_only
  summary: The adopted citation resolves to a 1970 Russian report on oxoline prophylaxis
    during the 1969 influenza epidemic. No abstract was available; no numerical efficacy,
    assay, exact formulation or mechanism was extracted.
- evidence_id: primary2011
  kind: primary_source
  reference: DOI:10.1371/journal.pone.0021922
  locator: PLOS full article, Results bacterial-growth control paragraphs, Discussion
    oxoline paragraph, references51–52; Figure5A image visually inspected
  accessed_at: '2026-10-21T06:58:56Z'
  support: context_only
  summary: The longevity study depicts anhydrous naphthalenetetrone as oxoline. Its
    discussion calls oxoline a quinolone/topoisomerase inhibitor and cites an oxoline-acid
    pregnancy study. These background statements conflict with the displayed nitrogen-free
    structure. The experiments concern nematode longevity with FUDR and do not establish
    a hydrate-specific antibacterial MIC or target.
  snapshot_sha256: dec8bcc07904cd42214b02dd1e3199b81fca8de86641b876c6b7a99a54527a49
- evidence_id: quinolone-reference
  kind: primary_source
  reference: PMID:16643598
  locator: Europe PMC core abstract; DOI10.1111/j.1741-4520.2006.00100.x
  accessed_at: '2026-10-21T06:58:56Z'
  support: context_only
  summary: The cited pregnancy paper explicitly describes a quinolone derivative used
    for urinary infection. It concerns oxolinic acid, not this nitrogen-free hydrate.
    This supports the reference-scope caution without establishing that all antibacterial
    activity of the hydrate is impossible.
  snapshot_sha256: e57800791a12e4f752ff38ea2ddfd3a0efe228f28347c92d97ac4adf37aa0e2e
- evidence_id: chemistry
  kind: validation
  reference: RDKit local calculation
  locator: /private/tmp/am-review-session/011-chemistry.py and 011-chemistry.json
  accessed_at: '2026-10-21T06:58:56Z'
  support: supports
  summary: Both encodings reproduce CWHBUPIYFIPPRI-UHFFFAOYSA-N, C10H8O6, charge 0,
    one fragment, no stereocenters and masses 224.168/224.032087976. The internal
    identifier is reproduced from the documented hash rule.
  snapshot_sha256: 312c7e366e12bbbe480e8d4d21a68dd104b32ff313946572fd7fa8c9455c3aca
- evidence_id: search
  kind: search
  reference: Inclusive local search and free source searches
  locator: 011-local-hits.txt; exact identifier, label and slug; bounded source queries
  accessed_at: '2026-10-21T06:58:56Z'
  support: context_only
  summary: Local search found the target, adopted row, source lock, generated products
    and discovery ledgers. Maintained decision and curator tables had no exact-ID/minted-ID
    match. No newly inspected exact-hydrate antibacterial experiment emerged; source-name
    confusion requires explicit attention, not an assertion of universal inactivity.
  search_scope: rg --no-ignore --hidden -l -F exact CHEBI:78857, full label and slug
    across isolated clone except .git and .venv; whole maintained tables read/searched
    for identifier and minted key. Free web queries included oxoline dihydrate antibacterial,
    exact systematic name antiviral, oxoline topoisomerase inhibitor, oxoline bacterial
    growth, and exact titles/citations. Only inspected official/source text supports
    conclusions; snippets/vendor pages remain leads.
assessments:
- assessment_id: identity
  area: identity
  topic: One exact covalent ketone hydrate
  outcome: supported
  summary: Stored structure, mass, formula, aliases and ChEBI identity agree. No salt,
    parent tetrone or oxolinic-acid structure was substituted.
  target_ids:
  - CHEBI:78857
  evidence_ids:
  - record
  - chebi
  - parents
  - chemistry
  - mesh
- assessment_id: grounding
  area: grounding
  topic: Broader parents and imported activity role
  outcome: supported
  summary: Parent classes are broader and structurally appropriate; the antibacterial
    role and filing faithfully reproduce the adopted authority. No exact external
    chemical xrefs are asserted.
  target_ids:
  - CHEBI:78857
  evidence_ids:
  - record
  - owner
  - chebi
  - parents
- assessment_id: definition
  area: evidence
  topic: Historical use versus clinical efficacy
  outcome: supported
  summary: Nasal-ointment use is corroborated as historical context. The record asserts
    no clinical approval or quantified benefit, and the available metadata do not
    establish either.
  target_ids:
  - CHEBI:78857
  evidence_ids:
  - record
  - chebi
  - mesh
  - primary1970
- assessment_id: activity
  area: evidence
  topic: Independent exact-hydrate antimicrobial evidence
  outcome: unknown
  summary: Classification is ontology-backed. The inspected primary leads do not establish
    exact-hydrate antibacterial activity; adjacent form and quinolone-acid literature
    cannot close that gap. This is an evidence limitation, not a proved false role.
  target_ids:
  - CHEBI:78857
  evidence_ids:
  - owner
  - chebi
  - primary1986
  - primary2011
  - quinolone-reference
  - search
- assessment_id: mechanism
  area: completeness
  topic: Topoisomerase and target boundary
  outcome: unknown
  summary: The record appropriately leaves mechanism and targets unasserted. An unmapped
    generic source role and a mismatched literature reference do not justify importing
    a bacterial topoisomerase mechanism. Native mechanism sign-off remains unresolved.
  target_ids:
  - CHEBI:78857
  evidence_ids:
  - record
  - owner
  - chebi
  - primary2011
  - quinolone-reference
- assessment_id: optional
  area: representation
  topic: Quantities, resistance, producer, datasets and graph
  outcome: not_applicable
  summary: No such objects are asserted; no defect is assigned solely to empty optional
    fields. Longevity, antipsoriatic or quinolone pregnancy findings must retain their
    own identity and experimental scope.
  target_ids:
  - CHEBI:78857
  evidence_ids:
  - record
  - primary1986
  - primary2011
  - quinolone-reference
- assessment_id: provenance
  area: ownership
  topic: Generated ownership and native status
  outcome: supported
  summary: Source row, mapping logic and three seed/reseed events support SEEDED status.
    Review validation does not promote the record.
  target_ids:
  - CHEBI:78857
  evidence_ids:
  - record
  - owner
  - chemistry
findings:
- finding_id: F1
  issue_key: chebi-78857-exact-hydrate-antimicrobial-evidence
  category: evidence
  severity: informational
  status: open
  certainty: confirmed
  title: Exact-hydrate antimicrobial evidence must be separated from oxolinic acid
    and parent tetrone
  description: The current seed has valid ontology provenance but unresolved independent
    antibacterial support. A concrete discovered paper mixes an anhydrous oxoline
    drawing with quinolone-acid background. This cannot justify a new target claim
    or native promotion. No role correction or inactivity finding is established by
    the bounded search.
  target_ids:
  - CHEBI:78857
  field_paths:
  - activity_roles
  - mode_of_action
  - evidence
  - discussions
  evidence_ids:
  - record
  - chebi
  - primary1986
  - primary2011
  - quinolone-reference
  - search
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2-2-3-3-tetrahydroxy-2-3-dihydronaphthalene-1-4-dione.yaml
    role: Future curator-owned evidence and qualification through validated writer
      and curation event
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity and role assertions; any source correction requires maintained
      extraction/reseeding
  rule_id: 'native-review-checklist: Identity, Evidence standard and Mode of action'
  native_severity: informational source-scope follow-up
  normalization_reason: The existing record does not assert the problematic target
    or clinical claims. Source-backed classification is allowed; unresolved literature
    support is retained as a bounded follow-up rather than an unsupported major error.
actions:
- action_id: A1
  description: Locate exact-hydrate antimicrobial experiments and adjudicate the authority
    role separately from oxolinic-acid and anhydrous-tetrone literature. Preserve
    a bounded unresolved mechanism rationale if no support is found. Any source-role
    correction must be evidence-backed and reproducible; do not copy generic topoisomerase
    claims.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:78857
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2-2-3-3-tetrahydroxy-2-3-dihydronaphthalene-1-4-dione.yaml
    role: Future curator-owned evidence and qualification through validated writer
      and curation event
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity and role assertions; any source correction requires maintained
      extraction/reseeding
  acceptance_checks:
  - Each proposed activity or target claim resolves exact chemical form and experimental
    organism/assay.
  - The 2011 background citation and 2006 quinolone study are not presented as experiments
    on this hydrate.
  - Curator annotations use the native validated writer/event; source corrections
    use maintained extraction and seeding. Run strict validation, corpus reproduction
    and QC before native status promotion.
limitations:
- PMID4932223 has no abstract in the inspected Europe PMC record; its title supplies
  historical study context only. No clinical efficacy or antiviral mechanism is inferred.
- The 1986 source was inspected at abstract level through Europe PMC and EPA HERO.
  PubMed requests repeatedly returned browser challenges.
- The 2011 primary study depicts the anhydrous tetrone; its chemical-form boundary
  and mismatched quinolone reference preclude transferring its background topoisomerase
  claim to the hydrate.
- Bounded searches do not prove that antibacterial activity is absent. No native curation
  status or data field was changed.
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
