# Lamesticumin F: exact congener and bounded original evidence

- Review: 20261021T193151Z-lamesticumin-f-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T19:05:32Z
- Finished UTC: 2026-10-21T19:31:51Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native lamesticumin F graph is chemically valid and matches both current ChEBI and PubChem. The original abstract explicitly includes this isolated congener in antibacterial testing, and the original supplement supports its composition and depicted connectivity. No confirmed native-field defect is established. Original main-text access, exact assay conditions and the experimental basis of every absolute stereocentre remain explicit limits. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position590; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:67479 | data/antibiotics/antibacterial/lamesticumin-f.yaml | generated | lamesticumin F |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:67479 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:67479 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:67479 | Actual focused execution exited 0. |
| Independent exact structure comparison | passed | False | CHEBI:67479 | Six native/current-authority encodings reproduce the exact full key, formula and charge. Accurate CIP labels were retained separately from legacy labels to avoid an algorithm-induced stereochemical allegation. |
| Authoritative full QC | failed | True | CHEBI:67479 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:67479 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:67479 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:67479 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:67479 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:67479 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:67479 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:67479 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:67479 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact congener, structure consistency and stereo evidence

identity: unknown. Targets: CHEBI:67479.

Native constitution, formula and serializations agree with current authorities and selected original supporting data. The original main-text basis of all absolute centres was not independently verified. No opposite natural stereoisomer or invalid molecular graph is established.

### Names, chemical parents, role and sole registry xref

grounding: unknown. Targets: CHEBI:67479.

The current ChEBI source and broader structural parents agree. The native systematic name retains the current authority wording. Reaxys exact equivalence remains unverified through independent registry access.

### Twig origin and antibacterial filing

evidence: supported. Targets: CHEBI:67479.

The original abstract names exact lamesticumin F among isolated compounds1–9 and reports their Gram-positive antibacterial activity. This supports coarse filing and origin; it does not support invented strain-level MICs, a bacterial target or a clinical indication.

### Source ownership, initial captures and generated history

provenance: supported. Targets: CHEBI:67479.

Entire native/source row and actual owner paths were examined. The thirteen captured inputs, deterministic minted identity and chronological generation events remain intact; citation-lead placement is deliberate.

### Whole-record coverage and bounded follow-up

completeness: supported. Targets: CHEBI:67479.

All populated native fields are dispositioned. Missing optional mechanism/MIC/producer objects are not defects. Closed original main text, registry access and absolute-stereo evidence are explicit limitations preventing unrestricted scientific sign-off.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optional primary-evidence follow-up before scientific sign-off or enrichment.

- If lawful full-main access becomes available, inspect the exact congener structure-elucidation passages and original activity row, retaining assay material, strain, method and units.
- Resolve the basis of all absolute stereochemistry and any relative-name scope before assigning a fully reviewed identity; do not infer a racemate or opposite hand from access limitations.
- Independently verify the Reaxys graph if accessible; source repetition alone is not exact-equivalence validation.
- Keep new congeners, ethanolysis products, mammalian cell assays, antimutagenicity and computational mechanisms separate from the exact antibacterial record.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/lamesticumin-f.yaml; Entire native YAML, including every name, parent, role, chemical property, exact xref, source concept and three history events. | supports | SEEDED/EXACT CHEBI:67479; neutral C30H50O3, RYDUWPYFQUMUJP-JAKYJIPASA-N. It has 4 assigned tetrahedral centres and two specified E side-chain alkenes. The definition asserts isolation from L. domesticum twigs. There are no separate structured target, resistance, activity, producer, clinical or causal-graph objects. The systematic synonym is checked below. |
| owners | data/raw/chebi_antimicrobials.tsv:1673; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Exact source row, relevant extraction and emission rules, and hidden/ignored-inclusive owner searches. | supports | The maintained ChEBI row supplies the native definition, chemistry, parents, role, names and Reaxys link. PMID:21401117 is its sole adopted citation lead; source leads are not automatically emitted as claim evidence. The stable mint independently recomputes as antibioticmech:chebi-b01551a8b2. No exact curator or decision override was found in the inspected overlays; ignored files were included. All thirteen original captured hashes remain unchanged. Three chronological seed/reseed events describe generation, not scientific sign-off. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/67479/; Complete current official JSON: default graph, names, provenance, ontology relations and sole registry accession. | supports | Current three-star ChEBI repeats the native full key, composition, definition, parents and exact Reaxys attribution. Its origin annotation names L. domesticum, twig and PMID21401117, with a 95% ethanolic extract note. That extraction note is database-tier context because the original main Methods was unavailable. Additional general metabolite/plant-metabolite roles do not establish an omitted antimicrobial role. |
| chemistry | PubChem CID53355790;059-root-chemistry.json; Both native serializations, both ChEBI strings and both official PubChem strings independently parsed. | supports | All six encodings reproduce RYDUWPYFQUMUJP-JAKYJIPASA-N, formula C30H50O3, charge zero and calculated monoisotopic mass 458.37599546; average mass agrees at native precision. F has side-chain 3E,7E geometry and the terminal secondary alcohol corresponding to original C21 is R under the accurate CIP labeler. Legacy and accurate CIP algorithms differ at certain complex ring centres in this family; the graph, full key and accurate labels are used rather than treating a legacy letter change as a physical stereoisomer. |
| terms | CHEBI:142348; CHEBI:23824; CHEBI:36130; CHEBI:36615; CHEBI:33282; Official term names/definitions and graph-functional-group comparison. | supports | The asserted parents are hexahydronaphthalenes, diol, cyclic terpene ketone, triterpenoid. Each is a broader structural class consistent with this graph; none is an exact substitute identity. The antibacterial role denotes growth inhibition or killing and is supported at original-abstract level for the named isolated material. No clinical indication is implied. |
| registry | reaxys:21534276; Native and current ChEBI registry association; no licensed registry graph inspected. | unknown | The Reaxys accession is consistently inherited from ChEBI, but its exact structure was not independently accessible. This is unresolved authority equivalence, not evidence that the accession is wrong. |
| original | PMID:21401117; DOI:10.1021/np100943x; Complete indexed original abstract, bibliographic metadata and publisher abstract; original main text unavailable. | supports | The 2011 paper isolates lamesticumin A1, its separate ethanolysis product2, B3, C4, D5, E6 and F7 together with lansic acid 3-ethyl ester8, ethyl lansiolate9 and four known analogues from L. domesticum twigs. Lamesticumin F is therefore compound7, explicitly inside the reported antibacterial set1–9. The abstract reports moderate activity against Gram-positive bacteria. It specifically mentions Snatzke assignment of F C21, without describing that procedure or giving all stereocentre assignments. No strain-specific MIC, assay medium, inoculum, purity or incubation is extracted from this abstract. |
| supplement | DOI:10.1021/np100943x.s001; https://acs.figshare.com/articles/journal_contribution/2647528; Official 62-page supplement contents and exact-congener HRESIMS page 52 viewed; selected structural pages as specified. | supports | Original compound7 is explicitly named lamesticumin F. Its positive-ion HRESIMS printout gives measured m/z 481.3640 and the corresponding sodium-adduct formula, consistent with neutral C30H50O3. The sodium-adduct ion is an analytical species, not proof that the isolated material is a sodium salt. Actual page5 Figure2 gives F7 HMBC connectivity, the two acyclic E alkenes and the depicted terminal vicinal diol. Correlation drawings are not independent proof of every absolute configuration, and no raw FID or mass data was reprocessed. |
| search | 590-local-hits.txt;590-owner-hits.txt;lam-discovery.json;059-root-fetch2.json;059-root-fetch3.json; Exact-name/adopted-DOI public searches, current authority checks, and hidden/ignored-inclusive repository/source searches. | context_only | The broad EuropePMC query returned191 hits, of which the first100 were captured and screened at title/metadata level; it includes many irrelevant records and is not191 exact-compound studies. Selected complete abstracts distinguish lamesticumin G maltase inhibition, other lansium-acid experiments, host-cell assays and in-silico onoceranoid work. None supplies an experimentally verified bacterial target for this exact congener within the inspected material. This is a bounded finding, not proof that no further mechanism exists. Native records have no asserted gene/pathway target requiring a matching structured-adapter query; that applicability decision preceded open research. |
| access | https://api.openalex.org/works/https://doi.org/10.1021/np100943x;059-root-fetch2.json; Actual publisher response, public index locations and official supplement metadata. | context_only | ACS full main returned403 and the public publisher landing page offered purchase. OpenAlex reported closed access and no repository full text in its indexed locations. ResearchGate offered request access rather than readable original text. The official ACS Figshare supplement was successfully obtained, but it contains spectral/structural support rather than the missing main activity table. No access request, paid credit or subscription bypass was used. |

## Limits And Additional Notes

- The2011 original main text was unavailable despite bounded public routes. Only its complete abstract and the stated official SI pages were inspected; no full original antibacterial table or Methods verification is claimed.
- The62-page SI contents were read and the stated exact-congener mass/structure pages viewed. Unstated raw spectral pages were not individually audited and no experimental spectra were reprocessed.
- All six current structural serializations agree, but database agreement is not independent experimental proof of absolute hand. The rel- names for A/B and F-specific Snatzke mention require original experimental context before unrestricted sign-off.
- The Reaxys accession is consistently attributed but independently unverified. Bounded metadata screening does not establish literature absence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native/source/history field was modified. Public retrieval manifests and independent diagnostics remain in session scratch. Required shared full-QC disposition is attached during finalization.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T193151Z-lamesticumin-f-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Lamesticumin F: exact congener and bounded original evidence'
started_at: '2026-10-21T19:05:32Z'
finished_at: '2026-10-21T19:31:51Z'
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
summary: The native lamesticumin F graph is chemically valid and matches both current
  ChEBI and PubChem. The original abstract explicitly includes this isolated congener
  in antibacterial testing, and the original supplement supports its composition and
  depicted connectivity. No confirmed native-field defect is established. Original
  main-text access, exact assay conditions and the experimental basis of every absolute
  stereocentre remain explicit limits. Scientific assessment retains the stated evidence
  limits; full verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/lamesticumin-f.yaml
    sha256: cf49c09bd620a7b0eda21d53db1f131e1a781c6a05559780aeecfdd33ac31769
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
- target_id: CHEBI:67479
  path: data/antibiotics/antibacterial/lamesticumin-f.yaml
  label: lamesticumin F
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
  selection: Initially uncovered queue position590; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:67479
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:67479
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    590
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:67479
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/lamesticumin-f.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:67479
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/lamesticumin-f.yaml --out /private/tmp/am-review-session/590-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: independent-authority-comparison
  name: Independent exact structure comparison
  status: passed
  required: false
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/059-root-chem.py
  exit_code: 0
  expected_exit_code: 0
  summary: Six native/current-authority encodings reproduce the exact full key, formula
    and charge. Accurate CIP labels were retained separately from legacy labels to
    avoid an algorithm-induced stereochemical allegation.
  target_ids:
  - CHEBI:67479
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:67479
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
  - CHEBI:67479
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
  - CHEBI:67479
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
  - CHEBI:67479
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
  - CHEBI:67479
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
  - CHEBI:67479
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
  - CHEBI:67479
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
  - CHEBI:67479
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
  - CHEBI:67479
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/lamesticumin-f.yaml
  locator: Entire native YAML, including every name, parent, role, chemical property,
    exact xref, source concept and three history events.
  accessed_at: '2026-10-21T19:17:46Z'
  support: supports
  summary: SEEDED/EXACT CHEBI:67479; neutral C30H50O3, RYDUWPYFQUMUJP-JAKYJIPASA-N.
    It has 4 assigned tetrahedral centres and two specified E side-chain alkenes.
    The definition asserts isolation from L. domesticum twigs. There are no separate
    structured target, resistance, activity, producer, clinical or causal-graph objects.
    The systematic synonym is checked below.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv:1673; conf/sources.yaml; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: Exact source row, relevant extraction and emission rules, and hidden/ignored-inclusive
    owner searches.
  accessed_at: '2026-10-21T19:17:46Z'
  support: supports
  summary: The maintained ChEBI row supplies the native definition, chemistry, parents,
    role, names and Reaxys link. PMID:21401117 is its sole adopted citation lead;
    source leads are not automatically emitted as claim evidence. The stable mint
    independently recomputes as antibioticmech:chebi-b01551a8b2. No exact curator
    or decision override was found in the inspected overlays; ignored files were included.
    All thirteen original captured hashes remain unchanged. Three chronological seed/reseed
    events describe generation, not scientific sign-off.
  snapshot_sha256: 1001d03866f60f94c6fefb04c42040cd06182e553e524ef83d28584a99dd39ec
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/67479/
  locator: 'Complete current official JSON: default graph, names, provenance, ontology
    relations and sole registry accession.'
  accessed_at: '2026-10-21T19:17:46Z'
  support: supports
  summary: Current three-star ChEBI repeats the native full key, composition, definition,
    parents and exact Reaxys attribution. Its origin annotation names L. domesticum,
    twig and PMID21401117, with a 95% ethanolic extract note. That extraction note
    is database-tier context because the original main Methods was unavailable. Additional
    general metabolite/plant-metabolite roles do not establish an omitted antimicrobial
    role.
  snapshot_sha256: f96a7611e9f164aac49828b076d9dba2a6d839b4cb9cbb4b2bb687cb0bc2db75
- evidence_id: chemistry
  kind: validation
  reference: PubChem CID53355790;059-root-chemistry.json
  locator: Both native serializations, both ChEBI strings and both official PubChem
    strings independently parsed.
  accessed_at: '2026-10-21T19:17:46Z'
  support: supports
  summary: All six encodings reproduce RYDUWPYFQUMUJP-JAKYJIPASA-N, formula C30H50O3,
    charge zero and calculated monoisotopic mass 458.37599546; average mass agrees
    at native precision. F has side-chain 3E,7E geometry and the terminal secondary
    alcohol corresponding to original C21 is R under the accurate CIP labeler. Legacy
    and accurate CIP algorithms differ at certain complex ring centres in this family;
    the graph, full key and accurate labels are used rather than treating a legacy
    letter change as a physical stereoisomer.
  snapshot_sha256: 733edaa31e17d67aef651a8fe187e14ef0ba1aab7d4a0a38b0596b3339d4b4e5
- evidence_id: terms
  kind: authority
  reference: CHEBI:142348; CHEBI:23824; CHEBI:36130; CHEBI:36615; CHEBI:33282
  locator: Official term names/definitions and graph-functional-group comparison.
  accessed_at: '2026-10-21T19:17:46Z'
  support: supports
  summary: The asserted parents are hexahydronaphthalenes, diol, cyclic terpene ketone,
    triterpenoid. Each is a broader structural class consistent with this graph; none
    is an exact substitute identity. The antibacterial role denotes growth inhibition
    or killing and is supported at original-abstract level for the named isolated
    material. No clinical indication is implied.
  snapshot_sha256: 20d92ce7e00c204b1753184671c043160821d692438278344335446aadcd5082
- evidence_id: registry
  kind: authority
  reference: reaxys:21534276
  locator: Native and current ChEBI registry association; no licensed registry graph
    inspected.
  accessed_at: '2026-10-21T19:17:46Z'
  support: unknown
  summary: The Reaxys accession is consistently inherited from ChEBI, but its exact
    structure was not independently accessible. This is unresolved authority equivalence,
    not evidence that the accession is wrong.
  snapshot_sha256: f96a7611e9f164aac49828b076d9dba2a6d839b4cb9cbb4b2bb687cb0bc2db75
- evidence_id: original
  kind: primary_source
  reference: PMID:21401117; DOI:10.1021/np100943x
  locator: Complete indexed original abstract, bibliographic metadata and publisher
    abstract; original main text unavailable.
  accessed_at: '2026-10-21T19:17:46Z'
  support: supports
  summary: The 2011 paper isolates lamesticumin A1, its separate ethanolysis product2,
    B3, C4, D5, E6 and F7 together with lansic acid 3-ethyl ester8, ethyl lansiolate9
    and four known analogues from L. domesticum twigs. Lamesticumin F is therefore
    compound7, explicitly inside the reported antibacterial set1–9. The abstract reports
    moderate activity against Gram-positive bacteria. It specifically mentions Snatzke
    assignment of F C21, without describing that procedure or giving all stereocentre
    assignments. No strain-specific MIC, assay medium, inoculum, purity or incubation
    is extracted from this abstract.
  snapshot_sha256: 9d68dbae37dc628a060cb0827d8cac9639a3b77e0393a3cb02cc47b695862b01
- evidence_id: supplement
  kind: primary_source
  reference: DOI:10.1021/np100943x.s001; https://acs.figshare.com/articles/journal_contribution/2647528
  locator: Official 62-page supplement contents and exact-congener HRESIMS page 52
    viewed; selected structural pages as specified.
  accessed_at: '2026-10-21T19:17:46Z'
  support: supports
  summary: Original compound7 is explicitly named lamesticumin F. Its positive-ion
    HRESIMS printout gives measured m/z 481.3640 and the corresponding sodium-adduct
    formula, consistent with neutral C30H50O3. The sodium-adduct ion is an analytical
    species, not proof that the isolated material is a sodium salt. Actual page5 Figure2
    gives F7 HMBC connectivity, the two acyclic E alkenes and the depicted terminal
    vicinal diol. Correlation drawings are not independent proof of every absolute
    configuration, and no raw FID or mass data was reprocessed.
  snapshot_sha256: 9118904a9e8cc7f4ab3d63537aff1be87c58aeeb7fb9f43631918118dacb4800
- evidence_id: search
  kind: search
  reference: 590-local-hits.txt;590-owner-hits.txt;lam-discovery.json;059-root-fetch2.json;059-root-fetch3.json
  locator: Exact-name/adopted-DOI public searches, current authority checks, and hidden/ignored-inclusive
    repository/source searches.
  accessed_at: '2026-10-21T19:17:46Z'
  support: context_only
  summary: The broad EuropePMC query returned191 hits, of which the first100 were
    captured and screened at title/metadata level; it includes many irrelevant records
    and is not191 exact-compound studies. Selected complete abstracts distinguish
    lamesticumin G maltase inhibition, other lansium-acid experiments, host-cell assays
    and in-silico onoceranoid work. None supplies an experimentally verified bacterial
    target for this exact congener within the inspected material. This is a bounded
    finding, not proof that no further mechanism exists. Native records have no asserted
    gene/pathway target requiring a matching structured-adapter query; that applicability
    decision preceded open research.
  search_scope: 2026-10-21; lamesticumin F, CHEBI:67479, full key, PMID21401117 and
    DOI; public primary follow-ups and ignored-inclusive local searches.
  snapshot_sha256: 66f1dec2da77ef5aca12d6c3542a2e2bdc924171316a699754e9806e08b2c4e5
- evidence_id: access
  kind: validation
  reference: https://api.openalex.org/works/https://doi.org/10.1021/np100943x;059-root-fetch2.json
  locator: Actual publisher response, public index locations and official supplement
    metadata.
  accessed_at: '2026-10-21T19:17:46Z'
  support: context_only
  summary: ACS full main returned403 and the public publisher landing page offered
    purchase. OpenAlex reported closed access and no repository full text in its indexed
    locations. ResearchGate offered request access rather than readable original text.
    The official ACS Figshare supplement was successfully obtained, but it contains
    spectral/structural support rather than the missing main activity table. No access
    request, paid credit or subscription bypass was used.
  snapshot_sha256: 401259ff5c6e5d375bfe801dcc5501fcf2f021dc4488836328e4f28199ca7a77
assessments:
- assessment_id: identity
  area: identity
  topic: Exact congener, structure consistency and stereo evidence
  outcome: unknown
  summary: Native constitution, formula and serializations agree with current authorities
    and selected original supporting data. The original main-text basis of all absolute
    centres was not independently verified. No opposite natural stereoisomer or invalid
    molecular graph is established.
  target_ids:
  - CHEBI:67479
  evidence_ids:
  - native
  - chemistry
  - original
  - supplement
- assessment_id: grounding
  area: grounding
  topic: Names, chemical parents, role and sole registry xref
  outcome: unknown
  summary: The current ChEBI source and broader structural parents agree. The native
    systematic name retains the current authority wording. Reaxys exact equivalence
    remains unverified through independent registry access.
  target_ids:
  - CHEBI:67479
  evidence_ids:
  - chebi
  - terms
  - registry
  - chemistry
- assessment_id: evidence
  area: evidence
  topic: Twig origin and antibacterial filing
  outcome: supported
  summary: The original abstract names exact lamesticumin F among isolated compounds1–9
    and reports their Gram-positive antibacterial activity. This supports coarse filing
    and origin; it does not support invented strain-level MICs, a bacterial target
    or a clinical indication.
  target_ids:
  - CHEBI:67479
  evidence_ids:
  - original
  - supplement
  - terms
- assessment_id: provenance
  area: provenance
  topic: Source ownership, initial captures and generated history
  outcome: supported
  summary: Entire native/source row and actual owner paths were examined. The thirteen
    captured inputs, deterministic minted identity and chronological generation events
    remain intact; citation-lead placement is deliberate.
  target_ids:
  - CHEBI:67479
  evidence_ids:
  - native
  - owners
  - chebi
- assessment_id: completeness
  area: completeness
  topic: Whole-record coverage and bounded follow-up
  outcome: supported
  summary: All populated native fields are dispositioned. Missing optional mechanism/MIC/producer
    objects are not defects. Closed original main text, registry access and absolute-stereo
    evidence are explicit limitations preventing unrestricted scientific sign-off.
  target_ids:
  - CHEBI:67479
  evidence_ids:
  - native
  - search
  - access
  - registry
  - supplement
findings: []
actions:
- action_id: A1
  description: Optional primary-evidence follow-up before scientific sign-off or enrichment.
  finding_ids: []
  target_ids:
  - CHEBI:67479
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Maintained identity/source evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible generated field owner
  acceptance_checks:
  - If lawful full-main access becomes available, inspect the exact congener structure-elucidation
    passages and original activity row, retaining assay material, strain, method and
    units.
  - Resolve the basis of all absolute stereochemistry and any relative-name scope
    before assigning a fully reviewed identity; do not infer a racemate or opposite
    hand from access limitations.
  - Independently verify the Reaxys graph if accessible; source repetition alone is
    not exact-equivalence validation.
  - Keep new congeners, ethanolysis products, mammalian cell assays, antimutagenicity
    and computational mechanisms separate from the exact antibacterial record.
limitations:
- The2011 original main text was unavailable despite bounded public routes. Only its
  complete abstract and the stated official SI pages were inspected; no full original
  antibacterial table or Methods verification is claimed.
- The62-page SI contents were read and the stated exact-congener mass/structure pages
  viewed. Unstated raw spectral pages were not individually audited and no experimental
  spectra were reprocessed.
- All six current structural serializations agree, but database agreement is not independent
  experimental proof of absolute hand. The rel- names for A/B and F-specific Snatzke
  mention require original experimental context before unrestricted sign-off.
- The Reaxys accession is consistently attributed but independently unverified. Bounded
  metadata screening does not establish literature absence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native/source/history field was modified. Public retrieval manifests and independent
  diagnostics remain in session scratch. Required shared full-QC disposition is attached
  during finalization.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
