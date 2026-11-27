# Azamulin: preserve stereospecific native identity and qualify a broader ChEBI cross-reference

- Review: 20261021T095321Z-azamulin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:24:36Z
- Finished UTC: 2026-10-21T09:53:21Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native eight-centre azamulin graph agrees with PubChem and ChEMBL. CHEBI:201468 instead encodes unassigned stereochemistry and cannot be treated as exact equivalent. Antibacterial comparator evidence and human CYP studies are distinct; the historical clinical-failure explanation remains source-supported but not independently established by the inspected primary passages.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position131; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-148ae939a4 | data/antibiotics/antibacterial/azamulin.yaml | generated | azamulin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-148ae939a4 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-148ae939a4 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-148ae939a4 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | antibioticmech:aro-148ae939a4 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-148ae939a4 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-148ae939a4 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-148ae939a4 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-148ae939a4 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-148ae939a4 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-148ae939a4 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-148ae939a4 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-148ae939a4 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Source reproduction, ownership and native status

provenance: supported. Targets: antibioticmech:aro-148ae939a4.

Captured maintained inputs remain unchanged. Source extraction and seeding explain native fields; structured review does not change SEEDED status.

### Focused validation

schema: supported. Targets: antibioticmech:aro-148ae939a4.

Schema and strict checks pass. Internal validity does not establish exact equivalence of every external cross-reference or prove all biological claims.

### Exact native graph versus ChEBI xref

identity: concern. Targets: antibioticmech:aro-148ae939a4.

Native chemistry is consistent and corroborated; the current ChEBI encoded structure lacks its stereochemical assignments.

### MINTED and pleuromutilin classification

grounding: supported. Targets: antibioticmech:aro-148ae939a4.

Fallback mint is reproducible and the broad class fits. Neither a matching name nor connectivity supports automatic grounding to the less-specific ChEBI entry.

### Historical clinical statement

evidence: unknown. Targets: antibioticmech:aro-148ae939a4.

The source assertion resolves, but inspected primary material chiefly concerns human CYP inhibition. A clinical-trial or contemporaneous development source is still needed to verify the phase-I failure reason.

### Antibacterial and host-enzyme distinction

evidence: supported. Targets: antibioticmech:aro-148ae939a4.

Primary comparator abstract supports qualitative antimicrobial context. Human CYP binding/metabolism must not be recast as bacterial mechanism.

### Optional biological fields and adapter applicability

scope: not_applicable. Targets: antibioticmech:aro-148ae939a4.

Native has no gene/protein/pathway/response assertion requiring adapter lookup. Discovered human CYP work is outside the bacterial transcriptomic question; missing optional objects are not defects.

## Findings

### F1: Qualify the ChEBI cross-reference whose encoded stereo is less specific

major / open / confirmed; issue key: azamulin-chebi201468-stereo-scope.

Native eight-centre azamulin and the current ChEBI encoded structure differ in stereochemical granularity. Retain the verified native graph and correct or qualify the cross-reference through maintained source policy; do not use the broader entry to assert exact equivalence.

### F2: Resolve clinical-history evidence and exact antibacterial comparator assays

informational / open / confirmed; issue key: azamulin-primary-clinical-and-assay-scope.

The primary human CYP paper and antimicrobial comparator abstract address different questions. Complete clinical-history and exact assay evidence would strengthen the seed without inventing a drug target or clinical outcome.

## Recommended Actions And Acceptance Checks

### A1

Resolve the external ChEBI mapping through maintained identity handling.

- Compare all eight assignments across full InChIs and name/SMILES fields; preserve the independently concordant PubChem/ChEMBL native graph.
- Remove or qualify201468 as a less-specific/source-context link using supported policy; do not force EXACT grounding by name or call the unspecified entry a racemate.
- If the upstream entry is corrected, verify its complete exact key before grounding; regenerate and validate the affected record without unrelated changes.

### A2

Retrieve claim-specific clinical and antimicrobial sources before optional enrichment.

- Check a contemporaneous clinical/development source for trial phase and failure reason; preserve uncertainty rather than declaring the history false from abstract absence.
- Inspect the original antibacterial comparator table and preparation before adding MICs.
- Keep human CYP effects and class-analogue ribosome structures distinct from exact-azamulin bacterial mechanism.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/azamulin.yaml; Entire YAML including three seed/reseed events | supports | Read MINTED identity, pleuromutilin class, clinical-history definition and PMID14709627, all four xrefs and complete chemistry. No native activity, mode, target, resistance, producer, clinical-use or graph object is asserted. |
| source | data/raw/aro_antibiotics.tsv;data/raw/pubchem_structures.tsv; 131-raw.json; seeder build_concepts/resolve_identity and extractor nearest drug-class ancestor | supports | ARO3001316 row248 and PubChem16072188 row78 reproduce the record. No adopted ChEBI row for201468 was present in the ignored-inclusive inventory search; seeding therefore uses PubChem and retains MINTED rather than granting exact ChEBI grounding. Accurate source copying does not resolve the retained xref stereochemical scope. |
| identity | PubChem CID:16072188;ChEMBL:CHEMBL2103760; 131-pubchem.json;131-CHEMBL2103760.json;014-root-xref-checks.json | supports | Independent ChEMBL SMILES and native encodings agree on FMHQJXGMLMSMLC-WBUYAQKGSA-N, neutral C24H38N4O4S and eight assigned centres. PubChem agrees. Native average478.6 is the source one-decimal value; RDKit478.659 differs by0.059, within one unit of its displayed precision, not exact numerical equality. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:201468; 131-chebi.html and visible identity fields | refutes | The current two-star MetaboLights entry has the same connectivity/formula but key FMHQJXGMLMSMLC-UHFFFAOYSA-N; its InChI and SMILES omit all eight tetrahedral assignments even though its systematic name specifies stereochemistry. It is not exact structure equivalence to the native full key. Unassigned stereo is not proof of a racemic preparation. |
| aro | ARO:3001316;ARO:3000670; 131-aro-terms.txt extracted from official same-session aro.obo | supports | Current ARO repeats the definition and cross-references and places azamulin in the pleuromutilin antibiotic class. That is faithful provenance and chemically plausible classification, but not independent primary clinical evidence. |
| cyp | PMID:14709627;DOI:10.1124/dmd.32.1.105; Complete indexed abstract; author-posted ResearchGate original text, Introduction, selected Methods and metabolic-stability/spectral-interaction Results | partial | The original study tests azamulin as an inhibitor of human CYP isoforms using liver or recombinant microsomes. Inspected passages establish human enzyme effects and metabolism, not a bacterial ribosome target or clinical efficacy. Introduction identifies a synthetic pleuromutilin derivative and Methods identify BD Biosciences reagent. The inspected passages do not establish the source definition’s claimed phase-I failure reason; that history is unresolved here, not disproven. |
| class-leads | Other ARO compound/class citation leads; 131-adopted.json: all seven bibliographic records and available abstracts | context_only | PMID20112168 is a broad secondary review. PMID17360517 studies retapamulin/SB280080/SB571519;16569865 studies tiamulin/valnemulin footprinting;15554968 studies tiamulin;11555289 studies tiamulin/valnemulin;931799 concerns a 1976 derivative series. These class references do not independently demonstrate exact-azamulin binding, clinical failure or current approval. |
| activity | PMID:30467968;DOI:10.1002/cbdv.201800560; Complete indexed original abstract in131-discovery.json | partial | The original derivative study uses retapamulin and azamulin as antibacterial comparators and reports analogue activities comparable to them in tested Gram-positive pathogens. This supports qualitative antimicrobial context; the full table, exact reagent preparation, strain list and individual azamulin MICs were not retrieved, so no numerical assay is imported. |
| chemistry | Independent RDKit and source-mint checks; 131-chemistry.json;014-root-xref-checks.json | supports | Both native encodings reproduce the full key, formula, charge, one component, exact mass and source mint. Stored average masses agree within the stated decimal precision tolerance; azamulin uses a 0.1-unit tolerance for its one-decimal source value. Focused schema and strict commands exit 0. |
| search | CultureBotAI/AntibioticMech; 131-local-hits.txt;131-maintained-search.txt | context_only | Maintained exact-name/identifier/key searches found the source rows and readiness inventory, without an exact-target curator override. Azidocillin numeric search also returned an unrelated ambiguine Reaxys identifier, rejected as a substring collision. |

## Limits And Additional Notes

- The author-posted2004 original was inspected selectively through public indexed text; raw figures, all enzyme tables and complete discussion were not audited. Direct publisher and local author-copy requests encountered403/429; no access failure means the source does not exist.
- The2019 comparator paper remains abstract-only. Secondary reviews gave differing bioavailability descriptions and were treated solely as leads; no clinical trial source was retrieved.
- No exhaustive activity, clinical-development or resistance census was attempted. No assigned producer is inferred from the fungal origin of parent pleuromutilin.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 21 captured maintained input hashes remain unchanged. No native record was edited. Empty optional fields are not automatically defects.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T095321Z-azamulin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Azamulin: preserve stereospecific native identity and qualify a broader ChEBI
  cross-reference'
started_at: '2026-10-21T09:24:36Z'
finished_at: '2026-10-21T09:53:21Z'
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
summary: The native eight-centre azamulin graph agrees with PubChem and ChEMBL. CHEBI:201468
  instead encodes unassigned stereochemistry and cannot be treated as exact equivalent.
  Antibacterial comparator evidence and human CYP studies are distinct; the historical
  clinical-failure explanation remains source-supported but not independently established
  by the inspected primary passages.
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
  - path: data/antibiotics/antibacterial/azamulin.yaml
    sha256: 793ab04ccade1f247c059605c80c7d23e7d089380807bb157ccb8db1fc4ad5fb
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
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: context
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: context
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: scripts/card_evidence_reviews.py
    sha256: f9ec8aff30066bf04b9c2757af7d6f5d179d045e57b9f3b352bbed0b851f50a8
    role: context
targets:
- target_id: antibioticmech:aro-148ae939a4
  path: data/antibiotics/antibacterial/azamulin.yaml
  label: azamulin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, definition, chemical and literature links
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI fields or source grounding where applicable
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Fallback PubChem chemistry where applicable
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Fallback structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated fields and exact grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained grounding/exclusion policy
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position131; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-148ae939a4
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-148ae939a4
  command: .venv/bin/python /private/tmp/am-review-session/focus014-root.py 131
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-148ae939a4
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/azamulin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-148ae939a4
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/azamulin.yaml --out /private/tmp/am-review-session/131-strict.tsv
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
  - antibioticmech:aro-148ae939a4
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
  - antibioticmech:aro-148ae939a4
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
  - antibioticmech:aro-148ae939a4
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
  - antibioticmech:aro-148ae939a4
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
  - antibioticmech:aro-148ae939a4
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
  - antibioticmech:aro-148ae939a4
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
  - antibioticmech:aro-148ae939a4
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
  - antibioticmech:aro-148ae939a4
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
  - antibioticmech:aro-148ae939a4
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/azamulin.yaml
  locator: Entire YAML including three seed/reseed events
  accessed_at: '2026-10-21T09:37:08Z'
  support: supports
  summary: Read MINTED identity, pleuromutilin class, clinical-history definition
    and PMID14709627, all four xrefs and complete chemistry. No native activity, mode,
    target, resistance, producer, clinical-use or graph object is asserted.
- evidence_id: source
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv;data/raw/pubchem_structures.tsv
  locator: 131-raw.json; seeder build_concepts/resolve_identity and extractor nearest
    drug-class ancestor
  accessed_at: '2026-10-21T09:37:08Z'
  support: supports
  summary: ARO3001316 row248 and PubChem16072188 row78 reproduce the record. No adopted
    ChEBI row for201468 was present in the ignored-inclusive inventory search; seeding
    therefore uses PubChem and retains MINTED rather than granting exact ChEBI grounding.
    Accurate source copying does not resolve the retained xref stereochemical scope.
  snapshot_sha256: ea8796691a67b1282b1fd39a05870a6a587422bc200f5e54ecb1e64bb1a23e25
- evidence_id: identity
  kind: database
  reference: PubChem CID:16072188;ChEMBL:CHEMBL2103760
  locator: 131-pubchem.json;131-CHEMBL2103760.json;014-root-xref-checks.json
  accessed_at: '2026-10-21T09:37:08Z'
  support: supports
  summary: Independent ChEMBL SMILES and native encodings agree on FMHQJXGMLMSMLC-WBUYAQKGSA-N,
    neutral C24H38N4O4S and eight assigned centres. PubChem agrees. Native average478.6
    is the source one-decimal value; RDKit478.659 differs by0.059, within one unit
    of its displayed precision, not exact numerical equality.
  snapshot_sha256: 2abf397a22e07bde48a655ffaf45cad2b20696bc783fba504718a1f12ddf7d7e
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:201468
  locator: 131-chebi.html and visible identity fields
  accessed_at: '2026-10-21T09:37:08Z'
  support: refutes
  summary: The current two-star MetaboLights entry has the same connectivity/formula
    but key FMHQJXGMLMSMLC-UHFFFAOYSA-N; its InChI and SMILES omit all eight tetrahedral
    assignments even though its systematic name specifies stereochemistry. It is not
    exact structure equivalence to the native full key. Unassigned stereo is not proof
    of a racemic preparation.
  snapshot_sha256: 4de12bf54d153b45cf67618c99c7adb6bf2bbdc6f67f19ca944a29ea4260f53b
- evidence_id: aro
  kind: authority
  reference: ARO:3001316;ARO:3000670
  locator: 131-aro-terms.txt extracted from official same-session aro.obo
  accessed_at: '2026-10-21T09:37:08Z'
  support: supports
  summary: Current ARO repeats the definition and cross-references and places azamulin
    in the pleuromutilin antibiotic class. That is faithful provenance and chemically
    plausible classification, but not independent primary clinical evidence.
  snapshot_sha256: c4d065a7982c4470006fe5d778f35c98eedb095612af4703214c64d216545664
- evidence_id: cyp
  kind: primary_source
  reference: PMID:14709627;DOI:10.1124/dmd.32.1.105
  locator: Complete indexed abstract; author-posted ResearchGate original text, Introduction,
    selected Methods and metabolic-stability/spectral-interaction Results
  accessed_at: '2026-10-21T09:37:08Z'
  support: partial
  summary: The original study tests azamulin as an inhibitor of human CYP isoforms
    using liver or recombinant microsomes. Inspected passages establish human enzyme
    effects and metabolism, not a bacterial ribosome target or clinical efficacy.
    Introduction identifies a synthetic pleuromutilin derivative and Methods identify
    BD Biosciences reagent. The inspected passages do not establish the source definition’s
    claimed phase-I failure reason; that history is unresolved here, not disproven.
  snapshot_sha256: c953688a6bb2c1ecc60f923b03f9d25ea7cac51166ee90c95ddd547e76b64726
- evidence_id: class-leads
  kind: primary_source
  reference: Other ARO compound/class citation leads
  locator: '131-adopted.json: all seven bibliographic records and available abstracts'
  accessed_at: '2026-10-21T09:37:08Z'
  support: context_only
  summary: PMID20112168 is a broad secondary review. PMID17360517 studies retapamulin/SB280080/SB571519;16569865
    studies tiamulin/valnemulin footprinting;15554968 studies tiamulin;11555289 studies
    tiamulin/valnemulin;931799 concerns a 1976 derivative series. These class references
    do not independently demonstrate exact-azamulin binding, clinical failure or current
    approval.
  snapshot_sha256: c953688a6bb2c1ecc60f923b03f9d25ea7cac51166ee90c95ddd547e76b64726
- evidence_id: activity
  kind: primary_source
  reference: PMID:30467968;DOI:10.1002/cbdv.201800560
  locator: Complete indexed original abstract in131-discovery.json
  accessed_at: '2026-10-21T09:37:08Z'
  support: partial
  summary: The original derivative study uses retapamulin and azamulin as antibacterial
    comparators and reports analogue activities comparable to them in tested Gram-positive
    pathogens. This supports qualitative antimicrobial context; the full table, exact
    reagent preparation, strain list and individual azamulin MICs were not retrieved,
    so no numerical assay is imported.
  snapshot_sha256: c84c269a8df5638cce59c1d8cb8420c1c9d5755f87829e2e422b4b6e68095a62
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit and source-mint checks
  locator: 131-chemistry.json;014-root-xref-checks.json
  accessed_at: '2026-10-21T09:37:08Z'
  support: supports
  summary: Both native encodings reproduce the full key, formula, charge, one component,
    exact mass and source mint. Stored average masses agree within the stated decimal
    precision tolerance; azamulin uses a 0.1-unit tolerance for its one-decimal source
    value. Focused schema and strict commands exit 0.
  snapshot_sha256: 43d4431a9fd52656090eced747e22b369d59a08296bd673bce3d9f70fb4e73cd
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 131-local-hits.txt;131-maintained-search.txt
  accessed_at: '2026-10-21T09:37:08Z'
  support: context_only
  summary: Maintained exact-name/identifier/key searches found the source rows and
    readiness inventory, without an exact-target curator override. Azidocillin numeric
    search also returned an unrelated ambiguine Reaxys identifier, rejected as a substring
    collision.
  search_scope: rg --no-ignore --hidden in the isolated checkout excluding .git/.venv;
    additional same-mode search across curation, conf, scripts, data/raw, src, reports
    and reviews. Current official chemical and ARO sources, adopted citation metadata/available
    abstracts and bounded free primary literature follow-up.
  snapshot_sha256: f9d7bd41888927b580f9b9bb6b7941daf27d6d2a4416f2589a2ed6ab32d8b0fd
assessments:
- assessment_id: provenance
  area: provenance
  topic: Source reproduction, ownership and native status
  outcome: supported
  summary: Captured maintained inputs remain unchanged. Source extraction and seeding
    explain native fields; structured review does not change SEEDED status.
  target_ids:
  - antibioticmech:aro-148ae939a4
  evidence_ids:
  - native
  - source
  - chemistry
- assessment_id: schema
  area: schema
  topic: Focused validation
  outcome: supported
  summary: Schema and strict checks pass. Internal validity does not establish exact
    equivalence of every external cross-reference or prove all biological claims.
  target_ids:
  - antibioticmech:aro-148ae939a4
  evidence_ids:
  - chemistry
- assessment_id: identity
  area: identity
  topic: Exact native graph versus ChEBI xref
  outcome: concern
  summary: Native chemistry is consistent and corroborated; the current ChEBI encoded
    structure lacks its stereochemical assignments.
  target_ids:
  - antibioticmech:aro-148ae939a4
  evidence_ids:
  - identity
  - chebi
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: MINTED and pleuromutilin classification
  outcome: supported
  summary: Fallback mint is reproducible and the broad class fits. Neither a matching
    name nor connectivity supports automatic grounding to the less-specific ChEBI
    entry.
  target_ids:
  - antibioticmech:aro-148ae939a4
  evidence_ids:
  - source
  - aro
  - chebi
- assessment_id: definition
  area: evidence
  topic: Historical clinical statement
  outcome: unknown
  summary: The source assertion resolves, but inspected primary material chiefly concerns
    human CYP inhibition. A clinical-trial or contemporaneous development source is
    still needed to verify the phase-I failure reason.
  target_ids:
  - antibioticmech:aro-148ae939a4
  evidence_ids:
  - aro
  - cyp
- assessment_id: activity
  area: evidence
  topic: Antibacterial and host-enzyme distinction
  outcome: supported
  summary: Primary comparator abstract supports qualitative antimicrobial context.
    Human CYP binding/metabolism must not be recast as bacterial mechanism.
  target_ids:
  - antibioticmech:aro-148ae939a4
  evidence_ids:
  - activity
  - cyp
  - class-leads
- assessment_id: optional
  area: scope
  topic: Optional biological fields and adapter applicability
  outcome: not_applicable
  summary: Native has no gene/protein/pathway/response assertion requiring adapter
    lookup. Discovered human CYP work is outside the bacterial transcriptomic question;
    missing optional objects are not defects.
  target_ids:
  - antibioticmech:aro-148ae939a4
  evidence_ids:
  - native
  - cyp
findings:
- finding_id: F1
  issue_key: azamulin-chebi201468-stereo-scope
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Qualify the ChEBI cross-reference whose encoded stereo is less specific
  description: Native eight-centre azamulin and the current ChEBI encoded structure
    differ in stereochemical granularity. Retain the verified native graph and correct
    or qualify the cross-reference through maintained source policy; do not use the
    broader entry to assert exact equivalence.
  target_ids:
  - antibioticmech:aro-148ae939a4
  field_paths:
  - xrefs
  - grounding_status
  evidence_ids:
  - identity
  - chebi
  - source
  rule_id: 'native-review-checklist: Exact identity, evidence scope and completeness'
  native_severity: major
  normalization_reason: Native eight-centre azamulin and the current ChEBI encoded
    structure differ in stereochemical granularity. Retain the verified native graph
    and correct or qualify the cross-reference through maintained source policy; do
    not use the broader entry to assert exact equivalence.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, definition, chemical and literature links
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI fields or source grounding where applicable
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Fallback PubChem chemistry where applicable
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Fallback structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated fields and exact grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained grounding/exclusion policy
- finding_id: F2
  issue_key: azamulin-primary-clinical-and-assay-scope
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Resolve clinical-history evidence and exact antibacterial comparator assays
  description: The primary human CYP paper and antimicrobial comparator abstract address
    different questions. Complete clinical-history and exact assay evidence would
    strengthen the seed without inventing a drug target or clinical outcome.
  target_ids:
  - antibioticmech:aro-148ae939a4
  field_paths:
  - definition_source
  - evidence
  - activity_spectrum
  - discussions
  evidence_ids:
  - cyp
  - activity
  - class-leads
  rule_id: 'native-review-checklist: Exact identity, evidence scope and completeness'
  native_severity: informational
  normalization_reason: The primary human CYP paper and antimicrobial comparator abstract
    address different questions. Complete clinical-history and exact assay evidence
    would strengthen the seed without inventing a drug target or clinical outcome.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, definition, chemical and literature links
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI fields or source grounding where applicable
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Fallback PubChem chemistry where applicable
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Fallback structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated fields and exact grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained grounding/exclusion policy
actions:
- action_id: A1
  description: Resolve the external ChEBI mapping through maintained identity handling.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-148ae939a4
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, definition, chemical and literature links
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI fields or source grounding where applicable
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Fallback PubChem chemistry where applicable
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Fallback structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated fields and exact grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained grounding/exclusion policy
  acceptance_checks:
  - Compare all eight assignments across full InChIs and name/SMILES fields; preserve
    the independently concordant PubChem/ChEMBL native graph.
  - Remove or qualify201468 as a less-specific/source-context link using supported
    policy; do not force EXACT grounding by name or call the unspecified entry a racemate.
  - If the upstream entry is corrected, verify its complete exact key before grounding;
    regenerate and validate the affected record without unrelated changes.
- action_id: A2
  description: Retrieve claim-specific clinical and antimicrobial sources before optional
    enrichment.
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:aro-148ae939a4
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, definition, chemical and literature links
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI fields or source grounding where applicable
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Fallback PubChem chemistry where applicable
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Fallback structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated fields and exact grounding
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained grounding/exclusion policy
  acceptance_checks:
  - Check a contemporaneous clinical/development source for trial phase and failure
    reason; preserve uncertainty rather than declaring the history false from abstract
    absence.
  - Inspect the original antibacterial comparator table and preparation before adding
    MICs.
  - Keep human CYP effects and class-analogue ribosome structures distinct from exact-azamulin
    bacterial mechanism.
limitations:
- The author-posted2004 original was inspected selectively through public indexed
  text; raw figures, all enzyme tables and complete discussion were not audited. Direct
  publisher and local author-copy requests encountered403/429; no access failure means
  the source does not exist.
- The2019 comparator paper remains abstract-only. Secondary reviews gave differing
  bioavailability descriptions and were treated solely as leads; no clinical trial
  source was retrieved.
- No exhaustive activity, clinical-development or resistance census was attempted.
  No assigned producer is inferred from the fungal origin of parent pleuromutilin.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 21 captured maintained input hashes remain unchanged. No native record was edited.
  Empty optional fields are not automatically defects.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:201468
- https://pubchem.ncbi.nlm.nih.gov/compound/16072188
- https://doi.org/10.1124/dmd.32.1.105
- https://doi.org/10.1002/cbdv.201800560
```
