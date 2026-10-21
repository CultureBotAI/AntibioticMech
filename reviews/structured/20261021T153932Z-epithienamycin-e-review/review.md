# Epithienamycin E: sulfate ester incorrectly classified as an organosulfonic acid

- Review: 20261021T153932Z-epithienamycin-e-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T15:13:49Z
- Finished UTC: 2026-10-21T15:39:32Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact epithienamycin E graph agrees with current ChEBI, KEGG, PubChem and both parsable KNApSAcK encodings. Original structure and antibacterial papers support the compound and MM13902 correspondence. Its organosulfonic-acid parent is chemically incompatible with the sulfate ester. The KNApSAcK displayed key is internally inconsistent and is retained as a source limitation.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position405; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:91030 | data/antibiotics/antibacterial/epithienamycin-e.yaml | generated | epithienamycin E |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:91030 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:91030 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:91030 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:91030 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:91030 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:91030 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:91030 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:91030 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:91030 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:91030 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:91030 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:91030 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact compound and historical aliases

identity: supported. Targets: CHEBI:91030.

Definition, systematic synonym, graph and matched authorities agree. The primary mixed-NMR experiment directly supports MM13902/epithienamycin E correspondence. AB110D names are registry-supported, with original independent synonym-specific proof outside the inspected sources. Missing independent absolute proof in the1981 paper is preserved rather than treated as proof of wrong stereo.

### Organosulfonic-acid parent

grounding: concern. Targets: CHEBI:91030.

The carbapenem and acetamide parents fit; CHEBI33551 does not. The sulfate ester requires removal of the false parent through maintained source ownership.

### Antimicrobial roles and optional mechanism

evidence: supported. Targets: CHEBI:91030.

Original ETM-E growth inhibition supports both roles. Zones, relative potency and unpublished enzyme observations are not converted to MICs, affinities or direct protein targets.

### Exact external identifiers

grounding: unknown. Targets: CHEBI:91030.

KEGG matches completely. KNApSAcK encodings agree but its displayed key conflicts internally; CAS/name differences require source-level documentation. Reaxys6450866 was not independently inspected.

### Source concepts, histories and coverage

provenance: supported. Targets: CHEBI:91030.

All 3 native history entries and source concepts were read; generated ownership, original hashes and focused validators are coherent. Native status remains SEEDED. Optional absent evidence domains are not corrective findings.

## Findings

### F1: Remove the chemically incompatible organosulfonic-acid parent

major / open / confirmed; issue key: epithienamycin-e-sulfate-misclassified-as-sulfonic-acid.

The native sulfate monoester is connected through oxygen, while CHEBI33551 requires a sulfo group directly attached to carbon. The primary structure paper independently identifies sulfation. The source relation is reproduced correctly but scientifically wrong.

## Recommended Actions And Acceptance Checks

### A1

Correct the source-owned parent relationship and reseed the same exact compound during authorized curation.

- Remove CHEBI33551 from the regenerated parent list. Add a sulfate-ester parent only after checking its exact ontology definition and maintained extraction route.
- Preserve the supported graph, E side-chain geometry and justified stereochemical scope; keep neutral parent and sodium assay material distinct.
- Record the source correction and rerun focused schema/strict, corpus reproduction and history/reference gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/epithienamycin-e.yaml; Entire YAML including all source concepts and history | supports | Every populated field was read. Native SEEDED/EXACT status, exact neutral graph, names, broader classes, activity roles, cross-references and history remain unchanged. Missing optional quantitative activity, molecular targets, resistance, producer, clinical, graph and collection fields are not schema defects. |
| owners | 405-source-rows.json; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Exact adopted rows and generated field ownership | supports | Original thirteen inputs were captured before judgment and retained within 16 expanded unchanged inputs. The exact ChEBI row owns the structure, definition and parent relations. Readiness rows are context, not an independent source. No compound-level publication lead is present in the adopted ChEBI row; the two original 1981 papers were found by exact-name search. |
| chemistry | 041-authority-compare.json; Independent RDKit comparison, record405 | supports | Native SMILES, InChI and current ChEBI molfile agree with the stored key, formula and charge. Focused chemistry also verifies masses and deterministic source identifier. KEGG C11755, PubChem11953962 and KNApSAcK SMILES/InChI reproduce FQQFFZPBGYGDSX-NJFHWYBASA-N: 5R,6R,8S and the E acetamidoethenyl chain. |
| authority | CHEBI:91030; 405-chebi.json; current broader term definitions | supports | Current ChEBI identity, names, structure, exact identifiers, outgoing relations and bibliography were inspected. CHEBI22160 is acetamide, CHEBI46633 carbapenem and CHEBI33551 organosulfonic acid. The last explicitly requires the sulfo group attached directly to carbon, unlike the native O-sulfate linkage. |
| search | 405-local-hits.txt; 405-owners-search.json; Ignored-inclusive local search and exact authority/primary links | supports | Local source/curation/conf/script searches included hidden and gitignored files. Current authority descriptors and primary originals were sought by exact label and identifiers. No extra exact corrective overlay was established in the inspected scope. Transport failures are not biological or chemical refutation. |
| structure | DOI:10.7164/antibiotics.34.637; Entire twelve-page1981 PartII; actual Table3 and MM13902 paragraph atp647 viewed | supports | The paper establishes ETM-E as a sulfate ester atC8 with an E unsaturated N-acetylcysteamine substituent. Cis5/6 relative geometry is measured; 5R and8S are biosynthetic assignments presented in parentheses, not independent absolute determinations. A mixed300MHz NMR sample of ETM-E and Beecham MM13902 is indistinguishable from the individual samples, directly supporting their correspondence. The isolated samples are sodium salts and include residual NaCl; free-acid identity must be distinguished from assay material. Unpublished beta-lactamase potency quoted in the discussion is not independently verified primary assay data. |
| activity | DOI:10.7164/antibiotics.34.628; Original PartI pp628–635; actualp633 Tables5/6 viewed | supports | Purified epithienamycins from Streptomyces flavogriseus culture are individually compared. Table5 uses15-microlitre drops on seeded agar; the ETM-E column is20 micrograms/mL, giving measurable zones for S.aureus108, B.subtilis964 and E.coli1418. These are inhibition-zone results, not MICs. Table7 contains ETM-B MICs and must not be assigned to E. The paper supports antibacterial eligibility and a cell-wall phenotype without demonstrating direct binding to a specific PBP. |
| sulfate | CHEBI:33551; native chemical graph; 041-term-33551.json; native atom adjacency | refutes | The sulfur(VI) atom has only oxygen neighbours and is linked to the carbon scaffold through oxygen. The second sulfur is a thioether and has no sulfo oxygens. No carbon-bound sulfonic-acid group is present. CHEBI33551 explicitly requires direct sulfur–carbon attachment, so the parent is chemically false despite valid syntax. |
| knapsack | https://www.knapsackfamily.com/knapsack_core/information.php?word=C00018092; 405-knapsack.txt; independently parsed SMILES and InChI | context_only | Both complete parsable descriptors yield the native NJFHWYBASA key, but the page prints ONULJNEONA. Its CAS57459-82-2 also differs from the native79057-46-8. This is an internal source inconsistency; it is not evidence that the linked molecule is an established epimer. Current J-GLOBAL public indexed descriptors independently match the native key/CAS, though direct retrieval returned503. |
| patent | https://patents.google.com/patent/US4146610A/en; Exact MM13902 isolation Example3 and adjacent analytical material | context_only | The original patent separates MM13902 di-sodium salt from mixed antibiotic fractions. Adjacent Table10 is headed MM4550A despite surrounding MM13902 text, so its quantitative MICs are not assigned to this compound. The patent is a new contextual lead, not a native document assertion. |

## Limits And Additional Notes

- The1981 structure report assumes part of the absolute configuration by biosynthetic analogy. Its source-specific uncertainty is retained; no speculative inversion is proposed.
- The activity paper main text throughp635 and key actual tables were inspected; final reference-only material was not independently reprocessed. Raw spectra were not reanalyzed.
- KNApSAcK has a displayed-key inconsistency and different CAS. Direct J-GLOBAL returned503; its indexed public chemical descriptors were inspected. Reaxys6450866 remains independently unverified.
- The1984 biosynthesis paper was read only for its abstract, introduction and initial methods. It is contextual and no quantitative mutant or pathway conclusion is adopted. The1977 RSC structure abstract was available but its PDF returned403. The patent was read only at the stated MM13902 isolation/material scope.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Independent chemistry used the existing batch019 interpreter against batch041; native schema and strict gates ran in the batch041 environment. No native or source field was edited.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T153932Z-epithienamycin-e-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Epithienamycin E: sulfate ester incorrectly classified as an organosulfonic
  acid'
started_at: '2026-10-21T15:13:49Z'
finished_at: '2026-10-21T15:39:32Z'
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
summary: The exact epithienamycin E graph agrees with current ChEBI, KEGG, PubChem
  and both parsable KNApSAcK encodings. Original structure and antibacterial papers
  support the compound and MM13902 correspondence. Its organosulfonic-acid parent
  is chemically incompatible with the sulfate ester. The KNApSAcK displayed key is
  internally inconsistent and is retained as a source limitation.
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
  - path: data/antibiotics/antibacterial/epithienamycin-e.yaml
    sha256: 07a41d909647d213195a03cf8ad14ad0d9251a8a13bc7053a53247bc98b0bc08
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
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: context
  - path: curation/record_review_queue.tsv
    sha256: 3828a5120b892ee0ee0b776affc6c3e4f1f1a3355ec4edd30e6005762de00e70
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
targets:
- target_id: CHEBI:91030
  path: data/antibiotics/antibacterial/epithienamycin-e.yaml
  label: epithienamycin E
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
  selection: Initially uncovered queue position405; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:91030
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:91030
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    405
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:91030
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/epithienamycin-e.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:91030
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/epithienamycin-e.yaml --out /private/tmp/am-review-session/405-strict.tsv
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
  - CHEBI:91030
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
  - CHEBI:91030
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
  - CHEBI:91030
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
  - CHEBI:91030
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
  - CHEBI:91030
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
  - CHEBI:91030
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
  - CHEBI:91030
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
  - CHEBI:91030
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
  - CHEBI:91030
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/epithienamycin-e.yaml
  locator: Entire YAML including all source concepts and history
  accessed_at: '2026-10-21T15:30:21Z'
  support: supports
  summary: Every populated field was read. Native SEEDED/EXACT status, exact neutral
    graph, names, broader classes, activity roles, cross-references and history remain
    unchanged. Missing optional quantitative activity, molecular targets, resistance,
    producer, clinical, graph and collection fields are not schema defects.
- evidence_id: owners
  kind: record_content
  reference: 405-source-rows.json; scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  locator: Exact adopted rows and generated field ownership
  accessed_at: '2026-10-21T15:30:21Z'
  support: supports
  summary: Original thirteen inputs were captured before judgment and retained within
    16 expanded unchanged inputs. The exact ChEBI row owns the structure, definition
    and parent relations. Readiness rows are context, not an independent source. No
    compound-level publication lead is present in the adopted ChEBI row; the two original
    1981 papers were found by exact-name search.
  snapshot_sha256: b444f16f38e420a1434210ef2539833816bffddc3f4dd68deee71456f8900a86
- evidence_id: chemistry
  kind: validation
  reference: 041-authority-compare.json
  locator: Independent RDKit comparison, record405
  accessed_at: '2026-10-21T15:30:21Z'
  support: supports
  summary: 'Native SMILES, InChI and current ChEBI molfile agree with the stored key,
    formula and charge. Focused chemistry also verifies masses and deterministic source
    identifier. KEGG C11755, PubChem11953962 and KNApSAcK SMILES/InChI reproduce FQQFFZPBGYGDSX-NJFHWYBASA-N:
    5R,6R,8S and the E acetamidoethenyl chain.'
  snapshot_sha256: 888ed975fd7b3f58fc069b58117d5bd400fa28653b2ac08c928bcb15ed6ab91c
- evidence_id: authority
  kind: authority
  reference: CHEBI:91030
  locator: 405-chebi.json; current broader term definitions
  accessed_at: '2026-10-21T15:30:21Z'
  support: supports
  summary: Current ChEBI identity, names, structure, exact identifiers, outgoing relations
    and bibliography were inspected. CHEBI22160 is acetamide, CHEBI46633 carbapenem
    and CHEBI33551 organosulfonic acid. The last explicitly requires the sulfo group
    attached directly to carbon, unlike the native O-sulfate linkage.
  snapshot_sha256: 2ad31ab6b5cc314c0667f2327278e70a309aa722a7ac6d261bb6a7b93f211f3d
- evidence_id: search
  kind: search
  reference: 405-local-hits.txt; 405-owners-search.json
  locator: Ignored-inclusive local search and exact authority/primary links
  accessed_at: '2026-10-21T15:30:21Z'
  support: supports
  summary: Local source/curation/conf/script searches included hidden and gitignored
    files. Current authority descriptors and primary originals were sought by exact
    label and identifiers. No extra exact corrective overlay was established in the
    inspected scope. Transport failures are not biological or chemical refutation.
  search_scope: rg --no-ignore --hidden exact names/identifiers over own checkout
    data, curation, conf, scripts and .claude; bounded original journal/authority
    retrieval
  snapshot_sha256: 6bb20f0e9cd728a87a8f516f83343bb6c55726c5649af02cbc9280bd307cfac1
- evidence_id: structure
  kind: primary_source
  reference: DOI:10.7164/antibiotics.34.637
  locator: Entire twelve-page1981 PartII; actual Table3 and MM13902 paragraph atp647
    viewed
  accessed_at: '2026-10-21T15:30:21Z'
  support: supports
  summary: The paper establishes ETM-E as a sulfate ester atC8 with an E unsaturated
    N-acetylcysteamine substituent. Cis5/6 relative geometry is measured; 5R and8S
    are biosynthetic assignments presented in parentheses, not independent absolute
    determinations. A mixed300MHz NMR sample of ETM-E and Beecham MM13902 is indistinguishable
    from the individual samples, directly supporting their correspondence. The isolated
    samples are sodium salts and include residual NaCl; free-acid identity must be
    distinguished from assay material. Unpublished beta-lactamase potency quoted in
    the discussion is not independently verified primary assay data.
  snapshot_sha256: 27c0ea05f426c2ce91f5d7426c1188d985d05ed2d2e000ffaf42bc5171cb251b
- evidence_id: activity
  kind: primary_source
  reference: DOI:10.7164/antibiotics.34.628
  locator: Original PartI pp628–635; actualp633 Tables5/6 viewed
  accessed_at: '2026-10-21T15:30:21Z'
  support: supports
  summary: Purified epithienamycins from Streptomyces flavogriseus culture are individually
    compared. Table5 uses15-microlitre drops on seeded agar; the ETM-E column is20
    micrograms/mL, giving measurable zones for S.aureus108, B.subtilis964 and E.coli1418.
    These are inhibition-zone results, not MICs. Table7 contains ETM-B MICs and must
    not be assigned to E. The paper supports antibacterial eligibility and a cell-wall
    phenotype without demonstrating direct binding to a specific PBP.
  snapshot_sha256: f75a96d251cb8e542194caf7d5d97c8bc5c594a43253405dfb4a38a2883dee67
- evidence_id: sulfate
  kind: authority
  reference: CHEBI:33551; native chemical graph
  locator: 041-term-33551.json; native atom adjacency
  accessed_at: '2026-10-21T15:30:21Z'
  support: refutes
  summary: The sulfur(VI) atom has only oxygen neighbours and is linked to the carbon
    scaffold through oxygen. The second sulfur is a thioether and has no sulfo oxygens.
    No carbon-bound sulfonic-acid group is present. CHEBI33551 explicitly requires
    direct sulfur–carbon attachment, so the parent is chemically false despite valid
    syntax.
  snapshot_sha256: 55d43c0d293d8db13d8227646d843d1d4ba457fde5570cedd8ef0362e09912c7
- evidence_id: knapsack
  kind: authority
  reference: https://www.knapsackfamily.com/knapsack_core/information.php?word=C00018092
  locator: 405-knapsack.txt; independently parsed SMILES and InChI
  accessed_at: '2026-10-21T15:30:21Z'
  support: context_only
  summary: Both complete parsable descriptors yield the native NJFHWYBASA key, but
    the page prints ONULJNEONA. Its CAS57459-82-2 also differs from the native79057-46-8.
    This is an internal source inconsistency; it is not evidence that the linked molecule
    is an established epimer. Current J-GLOBAL public indexed descriptors independently
    match the native key/CAS, though direct retrieval returned503.
  snapshot_sha256: 7be9eebf5322a72a8843233a6ed0d3e8711f458c41f331442fe7eb81276bdb6f
- evidence_id: patent
  kind: primary_source
  reference: https://patents.google.com/patent/US4146610A/en
  locator: Exact MM13902 isolation Example3 and adjacent analytical material
  accessed_at: '2026-10-21T15:30:21Z'
  support: context_only
  summary: The original patent separates MM13902 di-sodium salt from mixed antibiotic
    fractions. Adjacent Table10 is headed MM4550A despite surrounding MM13902 text,
    so its quantitative MICs are not assigned to this compound. The patent is a new
    contextual lead, not a native document assertion.
  snapshot_sha256: 395f1499fdf2431014b11028719a04315d28d527fba78d450c5d3dfbcfdc3119
assessments:
- assessment_id: identity
  area: identity
  topic: Exact compound and historical aliases
  outcome: supported
  summary: Definition, systematic synonym, graph and matched authorities agree. The
    primary mixed-NMR experiment directly supports MM13902/epithienamycin E correspondence.
    AB110D names are registry-supported, with original independent synonym-specific
    proof outside the inspected sources. Missing independent absolute proof in the1981
    paper is preserved rather than treated as proof of wrong stereo.
  target_ids:
  - CHEBI:91030
  evidence_ids:
  - native
  - chemistry
  - authority
  - structure
- assessment_id: class
  area: grounding
  topic: Organosulfonic-acid parent
  outcome: concern
  summary: The carbapenem and acetamide parents fit; CHEBI33551 does not. The sulfate
    ester requires removal of the false parent through maintained source ownership.
  target_ids:
  - CHEBI:91030
  evidence_ids:
  - sulfate
  - structure
  - authority
- assessment_id: activity
  area: evidence
  topic: Antimicrobial roles and optional mechanism
  outcome: supported
  summary: Original ETM-E growth inhibition supports both roles. Zones, relative potency
    and unpublished enzyme observations are not converted to MICs, affinities or direct
    protein targets.
  target_ids:
  - CHEBI:91030
  evidence_ids:
  - activity
  - structure
  - patent
- assessment_id: xref
  area: grounding
  topic: Exact external identifiers
  outcome: unknown
  summary: KEGG matches completely. KNApSAcK encodings agree but its displayed key
    conflicts internally; CAS/name differences require source-level documentation.
    Reaxys6450866 was not independently inspected.
  target_ids:
  - CHEBI:91030
  evidence_ids:
  - chemistry
  - knapsack
  - authority
- assessment_id: provenance
  area: provenance
  topic: Source concepts, histories and coverage
  outcome: supported
  summary: All 3 native history entries and source concepts were read; generated ownership,
    original hashes and focused validators are coherent. Native status remains SEEDED.
    Optional absent evidence domains are not corrective findings.
  target_ids:
  - CHEBI:91030
  evidence_ids:
  - native
  - owners
  - chemistry
  - search
findings:
- finding_id: F1
  issue_key: epithienamycin-e-sulfate-misclassified-as-sulfonic-acid
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Remove the chemically incompatible organosulfonic-acid parent
  description: The native sulfate monoester is connected through oxygen, while CHEBI33551
    requires a sulfo group directly attached to carbon. The primary structure paper
    independently identifies sulfation. The source relation is reproduced correctly
    but scientifically wrong.
  target_ids:
  - CHEBI:91030
  field_paths:
  - parent_compounds[1]
  evidence_ids:
  - native
  - sulfate
  - structure
  - owners
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
  rule_id: Review exact chemical-class semantics against the molecular graph
  native_severity: Major chemical-class correction
  normalization_reason: The relation misclassifies a functional group; the exact compound
    structure remains coherent.
actions:
- action_id: A1
  description: Correct the source-owned parent relationship and reseed the same exact
    compound during authorized curation.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:91030
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
  acceptance_checks:
  - Remove CHEBI33551 from the regenerated parent list. Add a sulfate-ester parent
    only after checking its exact ontology definition and maintained extraction route.
  - Preserve the supported graph, E side-chain geometry and justified stereochemical
    scope; keep neutral parent and sodium assay material distinct.
  - Record the source correction and rerun focused schema/strict, corpus reproduction
    and history/reference gates.
limitations:
- The1981 structure report assumes part of the absolute configuration by biosynthetic
  analogy. Its source-specific uncertainty is retained; no speculative inversion is
  proposed.
- The activity paper main text throughp635 and key actual tables were inspected; final
  reference-only material was not independently reprocessed. Raw spectra were not
  reanalyzed.
- KNApSAcK has a displayed-key inconsistency and different CAS. Direct J-GLOBAL returned503;
  its indexed public chemical descriptors were inspected. Reaxys6450866 remains independently
  unverified.
- The1984 biosynthesis paper was read only for its abstract, introduction and initial
  methods. It is contextual and no quantitative mutant or pathway conclusion is adopted.
  The1977 RSC structure abstract was available but its PDF returned403. The patent
  was read only at the stated MM13902 isolation/material scope.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Independent chemistry used the existing batch019 interpreter against batch041; native
  schema and strict gates ran in the batch041 environment. No native or source field
  was edited.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
