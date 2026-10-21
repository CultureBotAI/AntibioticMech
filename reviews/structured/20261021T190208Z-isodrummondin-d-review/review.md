# Isodrummondin D: supported constitution and source-limited stereochemical precision

- Review: 20261021T190208Z-isodrummondin-d-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T18:41:48Z
- Finished UTC: 2026-10-21T19:02:08Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native constitutional graph, structural classes and qualitative antibacterial definition agree with the adopted source and current ChEBI. The additional PubChem name/CAS result is a different keto–enol representation, not a demonstrated constitutional conflict. The primary abstract supports the named plant and organisms, while original spectra, optical rotation and detailed assays remain inaccessible. No confirmed required correction was established within this bounded review. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position564; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65812 | data/antibiotics/antibacterial/isodrummondin-d.yaml | generated | isodrummondin D |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:65812 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:65812 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:65812 | Actual focused execution exited 0. |
| Independent native and current authority graph comparison | passed | False | CHEBI:65812 | Native and ChEBI full keys agree; the additional PubChem graph reaches the same explicitly normalized tautomer. Enumeration limits are retained and no exhaustive tautomer claim is made. |
| Structured-source applicability | not_applicable | False | CHEBI:65812 | No native gene, protein, regulator, target, pathway or expression assertion, and no molecular mechanism is inferred from the abstract. |
| Authoritative full QC | failed | True | CHEBI:65812 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65812 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65812 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65812 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65812 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65812 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65812 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65812 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65812 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Constitution, one unassigned centre and optical alias

identity: supported. Targets: CHEBI:65812.

Native and current ChEBI constitutional encodings agree. Additional PubChem keto–enol differences do not establish a different compound; natural stereochemical/rotation precision remains explicitly unresolved.

### Names, structural parents, role and CAS

grounding: supported. Targets: CHEBI:65812.

The systematic name and five structural parents fit the encoded graph. CAS is corroborated by original bibliographic indexing and current source attribution, with direct-registry access limited. The (+) alias is not independently proven by the graph.

### Plant isolation and qualitative antibacterial scope

evidence: supported. Targets: CHEBI:65812.

The exact adopted original abstract supports stems/leaves and the three named bacterial taxa. Strain-level quantitative assays and a molecular target remain unverified.

### Depth of primary characterization

completeness: unknown. Targets: CHEBI:65812.

The source main, spectra and detailed antimicrobial tables could not be inspected. No complete natural stereochemical sign-off, optical-rotation assertion, exact MIC or mechanistic conclusion is claimed. Optional enrichment is contingent on those sources.

### Maintained owner and history

provenance: supported. Targets: CHEBI:65812.

The actual ChEBI source, role policy, source mint and all three history events are coherent; all thirteen initial hashes are unchanged. No native or source mutation occurred.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optional primary enrichment requires the original compound-specific characterization and assay tables.

- Retrieve and inspect the exact isodrummondin D structure/characterization in PMID1800634 before assigning absolute configuration or validating optical-rotation conditions. Keep distinct numbered drummondin analogues separate.
- Retain exact organism, strain, endpoint, material and concentration units for any added susceptibility data; the abstract supports no numerical MIC or direct molecular target.
- Do not import the current ChEBI root-origin component over the primary-supported stems/leaves definition. Do not replace native chemistry merely because an additional registry uses a keto–enol alternative.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/isodrummondin-d.yaml; Entire native record, two exact names, definition, five structural parents, role, full chemistry, CAS, source concept and all three history events. | supports | The SEEDED/EXACT record denotes neutral C28H32O8, key QDEXSBYEIYRPIT-UHFFFAOYSA-N, with one unassigned tetrahedral centre. Its systematic name describes the constitutional graph. The (+) alias contains optical-rotation information that the graph alone cannot establish. The record makes no quantitative assay, direct target, resistance, clinical-use or structured producer assertion. |
| owners | data/raw/chebi_antimicrobials.tsv:1317;data/raw/chebi_role_names.tsv;conf/sources.yaml;scripts/extract_source_inventory.py;scripts/seed_from_sources.py; Complete exact source row, role filtering, extraction/seeding ownership and source-specific local search. | supports | The ChEBI inventory supplies every populated scientific field and the sole adopted PMID1800634. All thirteen original captured inputs remain unchanged and already include actual owners. Three chronological seed/reseed events and the deterministic source mint agree. Missing optional target, activity or producer objects are not source reproduction errors. |
| chemistry | 564-chemistry.json;564-authority-chemistry.json;057-root-chemistry.py; Six independent native/ChEBI/PubChem structure parses. | supports | Native SMILES and InChI agree in full key, neutral formula, charge, masses and one unassigned centre. Current ChEBI SMILES/InChI agree exactly. Additional PubChem CID132132 encodes a different keto–enol form, VVSLJOYXCCVDIR-UHFFFAOYSA-N; both canonicalize to the same scratch tautomer and reciprocal graph. The enumeration stopped at configured transform limits, so this establishes an encountered common form, not exhaustive tautomer or stereochemical coverage. No missing stereocentre is interpreted as a racemate. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/65812/; Complete current exact compound entry and five parent definitions. | supports | The current identity, names, molecular representation, sole CAS and primary citation reproduce the adopted entry. Its separate current compound-origin component says root, conflicting with its own definition and the primary abstract’s stems/leaves. Native does not contain that root-origin object; retain the supported native plant-part wording and do not import the conflicting external component. |
| classes | CHEBI:33823;CHEBI:39436;CHEBI:51689;CHEBI:51867;CHEBI:76224;CHEBI:33282; Current enol, chromenol, enone, methyl-ketone, aromatic-ketone and antibacterial-role definitions inspected. | supports | The native graph contains vinylic hydroxy groups, a hydroxylated chromene, conjugated ketone, acetyl groups and an acetyl carbonyl directly attached to an aromatic carbon. All five structural parents fit. The named bacterial inhibition result supports the qualitative antibacterial role; no clinical-use conclusion is attached. |
| cas | cas:138169-53-6;https://pubmed.ncbi.nlm.nih.gov/1800634/;PubChem CID132132; Current ChEBI mapping, original PubMed substance indexing and exact name/CAS property lookups. | supports | The original bibliographic record indexes isodrummondin D under138169-53-6. PubChem name and CAS queries resolve the same alternate-tautomer entry; exact native-key lookup returned404. Direct CAS API returned401 and its public shell supplies no inspected definitive registry graph. No exact PubChem xref is native, no key-only mismatch is promoted to a defect, and no automatic registry replacement is recommended. |
| primary | PMID:1800634;DOI:10.1021/np50077a013; Complete original indexed abstract, bibliographic metadata and compound indexing; original main retrieval attempted. | supports | The 1991 report isolates four separately named filicinic acid derivatives, including isodrummondin D, from the hexane extract of Hypericum drummondii stems and leaves. It reports activity of all four against Staphylococcus aureus, Bacillus subtilis and Mycobacterium smegmatis. This supports the qualitative native definition. It does not expose exact strains, MIC values, solvent/inoculum conditions, purity or optical rotation in the accessible abstract; no values or direct mechanism are invented. |
| precision | synonyms[1];chemical_structure;PMID:1800634; Unassigned native stereocentre versus the (+) name and inaccessible original characterization. | supports | The sign of optical rotation does not specify an R/S assignment, and an unassigned graph does not prove a racemate. The present source access cannot independently verify the reported positive sign, its conditions, enantiomeric composition or absolute configuration. This is a precision limitation requiring original characterization before enrichment, not positive evidence that the native label or constitutional graph is wrong. |
| search | 564-local-hits.txt;564-owner-hits.txt;564-discovery.json;057-root-fetch1.json;057-root-fetch2.json; Ignored/hidden-inclusive local searches; exact title/abstract and primary DOI follow-up. | context_only | The exact isodrummondin D title/abstract query returned the one adopted original. This is a bounded query, not proof there is no other literature. Publisher PDF access returned403; a publicly indexed original-PDF mirror was unreachable by direct fetch and timed out through the browser. The indexed abstract and current authorities were read; inaccessible spectra/table pages are not represented as inspected. |

## Limits And Additional Notes

- Original1991 main/spectra/assay tables were inaccessible after publisher and publicly indexed mirror attempts. The complete indexed abstract and metadata were read, without pretending full-primary depth.
- The (+) alias, exact optical-rotation conditions, enantiomeric composition and absolute configuration were not independently established. Unassigned stereochemistry is not proof of a mixture.
- The scratch tautomer enumeration reached its transform limit but encountered the same common graph from both representations. No exhaustive enumeration claim, raw spectral reassignment or structural correction is made.
- Direct CAS API was unauthorized; source indexing and attributed name/CAS lookups corroborate the mapping only at the stated depth. No comprehensive later-literature or registry absence claim is made.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Only scratch review artifacts were written. The native record, maintained source, history and status remain unchanged.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T190208Z-isodrummondin-d-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Isodrummondin D: supported constitution and source-limited stereochemical
  precision'
started_at: '2026-10-21T18:41:48Z'
finished_at: '2026-10-21T19:02:08Z'
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
summary: The native constitutional graph, structural classes and qualitative antibacterial
  definition agree with the adopted source and current ChEBI. The additional PubChem
  name/CAS result is a different keto–enol representation, not a demonstrated constitutional
  conflict. The primary abstract supports the named plant and organisms, while original
  spectra, optical rotation and detailed assays remain inaccessible. No confirmed
  required correction was established within this bounded review. Scientific assessment
  retains the stated evidence limits; full verification is blocked by the shared native-library
  failure.
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
  - path: data/antibiotics/antibacterial/isodrummondin-d.yaml
    sha256: 59ae18b5896971f70dfcee72bf5c9cd283888e7b5332ced745831947467827d8
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
- target_id: CHEBI:65812
  path: data/antibiotics/antibacterial/isodrummondin-d.yaml
  label: isodrummondin D
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
  selection: Initially uncovered queue position564; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65812
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65812
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    564
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65812
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/isodrummondin-d.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65812
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/isodrummondin-d.yaml --out /private/tmp/am-review-session/564-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: authority
  name: Independent native and current authority graph comparison
  status: passed
  required: false
  summary: Native and ChEBI full keys agree; the additional PubChem graph reaches
    the same explicitly normalized tautomer. Enumeration limits are retained and no
    exhaustive tautomer claim is made.
  target_ids:
  - CHEBI:65812
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/057-root-chemistry.py
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter
  name: Structured-source applicability
  status: not_applicable
  required: false
  summary: No native gene, protein, regulator, target, pathway or expression assertion,
    and no molecular mechanism is inferred from the abstract.
  target_ids:
  - CHEBI:65812
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:65812
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
  - CHEBI:65812
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
  - CHEBI:65812
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
  - CHEBI:65812
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
  - CHEBI:65812
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
  - CHEBI:65812
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
  - CHEBI:65812
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
  - CHEBI:65812
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
  - CHEBI:65812
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/isodrummondin-d.yaml
  locator: Entire native record, two exact names, definition, five structural parents,
    role, full chemistry, CAS, source concept and all three history events.
  accessed_at: '2026-10-21T18:47:58Z'
  support: supports
  summary: The SEEDED/EXACT record denotes neutral C28H32O8, key QDEXSBYEIYRPIT-UHFFFAOYSA-N,
    with one unassigned tetrahedral centre. Its systematic name describes the constitutional
    graph. The (+) alias contains optical-rotation information that the graph alone
    cannot establish. The record makes no quantitative assay, direct target, resistance,
    clinical-use or structured producer assertion.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv:1317;data/raw/chebi_role_names.tsv;conf/sources.yaml;scripts/extract_source_inventory.py;scripts/seed_from_sources.py
  locator: Complete exact source row, role filtering, extraction/seeding ownership
    and source-specific local search.
  accessed_at: '2026-10-21T18:47:58Z'
  support: supports
  summary: The ChEBI inventory supplies every populated scientific field and the sole
    adopted PMID1800634. All thirteen original captured inputs remain unchanged and
    already include actual owners. Three chronological seed/reseed events and the
    deterministic source mint agree. Missing optional target, activity or producer
    objects are not source reproduction errors.
  snapshot_sha256: 46fef6ed11063f7627d5815601d56a7689dadcba4f620a6c42a5e097ce3e046d
- evidence_id: chemistry
  kind: validation
  reference: 564-chemistry.json;564-authority-chemistry.json;057-root-chemistry.py
  locator: Six independent native/ChEBI/PubChem structure parses.
  accessed_at: '2026-10-21T18:47:58Z'
  support: supports
  summary: Native SMILES and InChI agree in full key, neutral formula, charge, masses
    and one unassigned centre. Current ChEBI SMILES/InChI agree exactly. Additional
    PubChem CID132132 encodes a different keto–enol form, VVSLJOYXCCVDIR-UHFFFAOYSA-N;
    both canonicalize to the same scratch tautomer and reciprocal graph. The enumeration
    stopped at configured transform limits, so this establishes an encountered common
    form, not exhaustive tautomer or stereochemical coverage. No missing stereocentre
    is interpreted as a racemate.
  snapshot_sha256: a2e74e61b1aaddad49d5f3567d20ba85d111d891a02053914123682b06838fdd
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/65812/
  locator: Complete current exact compound entry and five parent definitions.
  accessed_at: '2026-10-21T18:47:58Z'
  support: supports
  summary: The current identity, names, molecular representation, sole CAS and primary
    citation reproduce the adopted entry. Its separate current compound-origin component
    says root, conflicting with its own definition and the primary abstract’s stems/leaves.
    Native does not contain that root-origin object; retain the supported native plant-part
    wording and do not import the conflicting external component.
  snapshot_sha256: 096ed063d1576031b94ac73e8fb0dda1d85f7b28d1d217a82fb7b8c937add43c
- evidence_id: classes
  kind: authority
  reference: CHEBI:33823;CHEBI:39436;CHEBI:51689;CHEBI:51867;CHEBI:76224;CHEBI:33282
  locator: Current enol, chromenol, enone, methyl-ketone, aromatic-ketone and antibacterial-role
    definitions inspected.
  accessed_at: '2026-10-21T18:47:58Z'
  support: supports
  summary: The native graph contains vinylic hydroxy groups, a hydroxylated chromene,
    conjugated ketone, acetyl groups and an acetyl carbonyl directly attached to an
    aromatic carbon. All five structural parents fit. The named bacterial inhibition
    result supports the qualitative antibacterial role; no clinical-use conclusion
    is attached.
- evidence_id: cas
  kind: authority
  reference: cas:138169-53-6;https://pubmed.ncbi.nlm.nih.gov/1800634/;PubChem CID132132
  locator: Current ChEBI mapping, original PubMed substance indexing and exact name/CAS
    property lookups.
  accessed_at: '2026-10-21T18:47:58Z'
  support: supports
  summary: The original bibliographic record indexes isodrummondin D under138169-53-6.
    PubChem name and CAS queries resolve the same alternate-tautomer entry; exact
    native-key lookup returned404. Direct CAS API returned401 and its public shell
    supplies no inspected definitive registry graph. No exact PubChem xref is native,
    no key-only mismatch is promoted to a defect, and no automatic registry replacement
    is recommended.
  snapshot_sha256: f46a5ed5055d9674fff9450bd43d04a2d23c86cace19aa782e5f52d6f44d0206
- evidence_id: primary
  kind: primary_source
  reference: PMID:1800634;DOI:10.1021/np50077a013
  locator: Complete original indexed abstract, bibliographic metadata and compound
    indexing; original main retrieval attempted.
  accessed_at: '2026-10-21T18:47:58Z'
  support: supports
  summary: The 1991 report isolates four separately named filicinic acid derivatives,
    including isodrummondin D, from the hexane extract of Hypericum drummondii stems
    and leaves. It reports activity of all four against Staphylococcus aureus, Bacillus
    subtilis and Mycobacterium smegmatis. This supports the qualitative native definition.
    It does not expose exact strains, MIC values, solvent/inoculum conditions, purity
    or optical rotation in the accessible abstract; no values or direct mechanism
    are invented.
  snapshot_sha256: 7baee73ccab325ea12ed136e58c4a4c3b3242abf34d55ae9c411622b6959104b
- evidence_id: precision
  kind: validation
  reference: synonyms[1];chemical_structure;PMID:1800634
  locator: Unassigned native stereocentre versus the (+) name and inaccessible original
    characterization.
  accessed_at: '2026-10-21T18:47:58Z'
  support: supports
  summary: The sign of optical rotation does not specify an R/S assignment, and an
    unassigned graph does not prove a racemate. The present source access cannot independently
    verify the reported positive sign, its conditions, enantiomeric composition or
    absolute configuration. This is a precision limitation requiring original characterization
    before enrichment, not positive evidence that the native label or constitutional
    graph is wrong.
- evidence_id: search
  kind: search
  reference: 564-local-hits.txt;564-owner-hits.txt;564-discovery.json;057-root-fetch1.json;057-root-fetch2.json
  locator: Ignored/hidden-inclusive local searches; exact title/abstract and primary
    DOI follow-up.
  accessed_at: '2026-10-21T18:47:58Z'
  support: context_only
  summary: The exact isodrummondin D title/abstract query returned the one adopted
    original. This is a bounded query, not proof there is no other literature. Publisher
    PDF access returned403; a publicly indexed original-PDF mirror was unreachable
    by direct fetch and timed out through the browser. The indexed abstract and current
    authorities were read; inaccessible spectra/table pages are not represented as
    inspected.
  search_scope: 2026-10-21; rg --no-ignore --hidden exact label/identifier/key/CAS
    across source and context inputs; EuropePMC exact title/abstract query, publisher
    DOI and publicly indexed original-PDF follow-up.
  snapshot_sha256: 3dae579f814cf031ac6af8046a0e5444421b9ae433066e6bb45519959ccee7cc
assessments:
- assessment_id: identity
  area: identity
  topic: Constitution, one unassigned centre and optical alias
  outcome: supported
  summary: Native and current ChEBI constitutional encodings agree. Additional PubChem
    keto–enol differences do not establish a different compound; natural stereochemical/rotation
    precision remains explicitly unresolved.
  target_ids:
  - CHEBI:65812
  evidence_ids:
  - native
  - chemistry
  - chebi
  - precision
- assessment_id: groundings
  area: grounding
  topic: Names, structural parents, role and CAS
  outcome: supported
  summary: The systematic name and five structural parents fit the encoded graph.
    CAS is corroborated by original bibliographic indexing and current source attribution,
    with direct-registry access limited. The (+) alias is not independently proven
    by the graph.
  target_ids:
  - CHEBI:65812
  evidence_ids:
  - classes
  - cas
  - chebi
  - precision
- assessment_id: evidence
  area: evidence
  topic: Plant isolation and qualitative antibacterial scope
  outcome: supported
  summary: The exact adopted original abstract supports stems/leaves and the three
    named bacterial taxa. Strain-level quantitative assays and a molecular target
    remain unverified.
  target_ids:
  - CHEBI:65812
  evidence_ids:
  - primary
  - native
  - search
- assessment_id: completeness
  area: completeness
  topic: Depth of primary characterization
  outcome: unknown
  summary: The source main, spectra and detailed antimicrobial tables could not be
    inspected. No complete natural stereochemical sign-off, optical-rotation assertion,
    exact MIC or mechanistic conclusion is claimed. Optional enrichment is contingent
    on those sources.
  target_ids:
  - CHEBI:65812
  evidence_ids:
  - primary
  - precision
  - search
- assessment_id: provenance
  area: provenance
  topic: Maintained owner and history
  outcome: supported
  summary: The actual ChEBI source, role policy, source mint and all three history
    events are coherent; all thirteen initial hashes are unchanged. No native or source
    mutation occurred.
  target_ids:
  - CHEBI:65812
  evidence_ids:
  - owners
  - native
findings: []
actions:
- action_id: A1
  description: Optional primary enrichment requires the original compound-specific
    characterization and assay tables.
  finding_ids: []
  target_ids:
  - CHEBI:65812
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/isodrummondin-d.yaml
    role: Future validated curator-owned scientific annotations
  acceptance_checks:
  - Retrieve and inspect the exact isodrummondin D structure/characterization in PMID1800634
    before assigning absolute configuration or validating optical-rotation conditions.
    Keep distinct numbered drummondin analogues separate.
  - Retain exact organism, strain, endpoint, material and concentration units for
    any added susceptibility data; the abstract supports no numerical MIC or direct
    molecular target.
  - Do not import the current ChEBI root-origin component over the primary-supported
    stems/leaves definition. Do not replace native chemistry merely because an additional
    registry uses a keto–enol alternative.
limitations:
- Original1991 main/spectra/assay tables were inaccessible after publisher and publicly
  indexed mirror attempts. The complete indexed abstract and metadata were read, without
  pretending full-primary depth.
- The (+) alias, exact optical-rotation conditions, enantiomeric composition and absolute
  configuration were not independently established. Unassigned stereochemistry is
  not proof of a mixture.
- The scratch tautomer enumeration reached its transform limit but encountered the
  same common graph from both representations. No exhaustive enumeration claim, raw
  spectral reassignment or structural correction is made.
- Direct CAS API was unauthorized; source indexing and attributed name/CAS lookups
  corroborate the mapping only at the stated depth. No comprehensive later-literature
  or registry absence claim is made.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Only scratch review artifacts were written. The native record, maintained source,
  history and status remain unchanged.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
