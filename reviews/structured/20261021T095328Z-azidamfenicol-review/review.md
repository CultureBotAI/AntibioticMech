# Azidamfenicol: qualify one stereochemically broader ChEMBL xref and retain database evidence limits

- Review: 20261021T095328Z-azidamfenicol-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:24:42Z
- Finished UTC: 2026-10-21T09:53:28Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact R,R azidamfenicol chemistry and ChEBI grounding are corroborated. CHEMBL278788 lacks both stereocentre assignments, whereas CHEMBL3989525 matches exactly. Native resistance/target annotations honestly retain database scope. An original dehydrogenase study supplies a compound-specific inactivation lead, with supplementary assays and exact preparation still to inspect.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position132; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:135238 | data/antibiotics/antibacterial/azidamfenicol.yaml | generated | azidamfenicol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:135238 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:135238 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:135238 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:135238 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:135238 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:135238 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:135238 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:135238 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:135238 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:135238 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:135238 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:135238 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Source reproduction, ownership and native status

provenance: supported. Targets: CHEBI:135238.

Captured maintained inputs remain unchanged. Source extraction and seeding explain native fields; structured review does not change SEEDED status.

### Focused validation

schema: supported. Targets: CHEBI:135238.

Schema and strict checks pass. Internal validity does not establish exact equivalence of every external cross-reference or prove all biological claims.

### Native R,R identity and retained ChEMBL mapping

identity: concern. Targets: CHEBI:135238.

Exact graph agrees with ChEBI/PubChem/one ChEMBL record, but the second ChEMBL xref lacks stereo assignments.

### Source slice and class

grounding: supported. Targets: CHEBI:135238.

ARO-to-ChEBI exact structure grounding and phenicol classification reproduce; out-of-role-scope source handling explains omitted standalone ChEBI source concept.

### Database target and resistance scope

evidence: supported. Targets: CHEBI:135238.

No source assertion is mislabeled as an exact-compound primary experiment. Current categories align with determinant functions; source-specific evidence must be retained until primary assay verification.

### Shared phenicol mode and solubility wording

evidence: unknown. Targets: CHEBI:135238.

The source review supports class context; exact compound solubility measurement and23S interaction experiments were not independently recovered. This is a primary-evidence limitation rather than a demonstrated false statement.

### Exact oxidative inactivation lead

completeness: unknown. Targets: CHEBI:135238.

Purified-enzyme oxidation evidence is available for azidamfenicol. Supplementary activity, preparation and protein accessions require verification before organism-specific resistance or causal annotation.

## Findings

### F1: Remove or qualify the ChEMBL cross-reference that lacks both stereo assignments

major / open / confirmed; issue key: azidamfenicol-chembl278788-stereo-scope.

CHEMBL278788 represents stereochemically unspecified connectivity, while native R,R azidamfenicol agrees exactly with CHEMBL3989525. Keep the correct graph and exact link; do not present both entries as interchangeable exact chemical identifiers.

### F2: Curate exact inactivation evidence separately from broad phenicol source assertions

informational / open / confirmed; issue key: azidamfenicol-qualified-oxidative-inactivation-enrichment.

The2023 original study includes exact azidamfenicol oxidation experiments. Verify supplementary inactivation and preparation details before primary evidence is added; do not promote every chloramphenicol-family edge merely from shared scaffold.

## Recommended Actions And Acceptance Checks

### A1

Correct the maintained cross-reference mapping while preserving exact chemistry.

- Compare full InChIs and both centres; retain CHEMBL3989525 and the native full key.
- Remove or qualify278788 through supported source/xref policy, keeping provenance and avoiding an unsupported racemate assertion.
- Regenerate and run exact-identity plus focused/schema/reference gates; no direct generated-only patch.

### A2

Verify original compound-specific experiments before optional evidence upgrades.

- Retrieve S24–25 and supplier/structure details for azidamfenicol; keep enzyme oxidation, loss of antibacterial activity and isolate resistance as separate endpoints.
- Resolve exact NR/NB proteins and strains before adding accessions or species-wide claims.
- Inspect exact-drug assays for each existing determinant before changing its database-only evidence; chloramphenicol results alone do not prove azidamfenicol phenotypes.
- Do not reinterpret the PA2509 catB metabolic enzyme hit as an antibiotic acetyltransferase.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/azidamfenicol.yaml; Entire YAML including24 resistance mechanisms,23S target and seed/reseed history | supports | Read the ARO-derived definition, phenicol class, exact neutral graph, five xrefs,24 determinants and23S-rRNA target. Every resistance edge is explicitly a database assertion rather than a primary citation; target scope is likewise preserved. No quantitative activity, clinical, producer or causal-graph claim is asserted. |
| source | ARO and ChEBI source inventories;CARD/ARO edge extraction; 132-raw.json;132-aro-terms.txt;build_concepts/resolve_identity and edge mapping | supports | ChEBI135238 is an adopted out-of-role-scope row used to supply structure and exact grounding to ARO3000382; it does not create a second ChEBI source concept or unrelated role parents. All24 edges and target reproduce. Acetyltransferases map to inactivation and Cfr/Clb/Cip methyltransferase families to target alteration. Source qualifiers are scientifically material. |
| identity | CHEBI:135238;PubChem CID:62858;ChEMBL:CHEMBL3989525; Current chemical resources and independently parsed ChEMBL SMILES | supports | All agree with native SGRUZFCHLOFYHZ-MWLCHTKSSA-N, C11H13N5O5, neutral charge and two R centres. The source title, CAS and phenicol scaffold agree. Exact grounding does not require the ChEBI row to be independently within the antimicrobial role seed slice. |
| xref | ChEMBL:CHEMBL278788; 132-CHEMBL278788.json;014-root-xref-checks.json | refutes | This second retained ChEMBL xref encodes SGRUZFCHLOFYHZ-UHFFFAOYSA-N and no stereocentre assignments. Independent parsing identifies two unspecified centres. Same connectivity is not exact equivalence to the native R,R drug; no racemate composition is inferred. |
| adopted | All41 ARO compound/class/target/determinant citation records; 132-adopted.json;complete available abstracts and current ARO stanzas | context_only | All associated records and available abstracts were inspected. Definition PMID15539072 is a phenicol-resistance review, not a new azidamfenicol binding experiment. Target leads PMID10445875/12860128 concern other peptidyl-transferase inhibitors including chloramphenicol;16569865 is pleuromutilin work;16257828/15700955 are reviews, the latter without an abstract. Most determinant primary abstracts concern chloramphenicol rather than exact azidamfenicol. This limits primary promotion, not the truth of the honestly labeled source assertions. |
| edge-boundary | PMID:22547628;PMID:23752511;PMID:27929110;PMID:29259290; Complete indexed original abstracts in132-adopted.json | partial | Clb-family and Cip-family papers concern23S methyltransferases;catU concerns an acetyltransferase and the later study concerns resistomes. Mechanistic categories are compatible with native source assertions. Their inspected abstracts do not supply exact azidamfenicol assays for each determinant; absence from those abstracts is not a negative susceptibility experiment. |
| oxidation | PMID:36353978;DOI:10.1002/cbic.202200632; Public UFZ accepted manuscript132-dehydrogenases-ufz.pdf/text; exact analogue Results and enzymatic-assay Methods | partial | Results explicitly include azidamfenicol oxidative inactivation. Methods test200 µM azidamfenicol with purified CAP-ADH+NR or CAP-ADH-NB in phosphate buffer, FAD and enzyme at30 C, adding DCIP for the NR enzyme and analyzing methanol-quenched samples by UPLC-HRMS. Sources are Nocardiopsis sp.RV163 and Novosphingobium sp.B225. Main chloramphenicol MIC/growth experiments must not be transferred to azidamfenicol; its supplementary S24–25 outcomes and reagent identity remain to inspect. |
| other-primary | PMID:580383;PMID:34387504;PMID:33169603; 132-discovery.json complete available abstracts | partial | The1978 Baycuten study compares a combination and individual components; abstract describes moderate antibacterial activity of acidamfenicol without recoverable strain-specific MICs. The2021 and2020 studies report enantioselective synthesis. Other search hits address host allergy or analytical combination assays and are not antimicrobial-target evidence. |
| adapter | Native iModulonDB adapter before web research; 132-imodulondb-datasets.txt; exact L.reuteri cat and P.aeruginosa catB searches | context_only | Successful catalog retry and both searches completed. L.reuteri search returned no genes/modules. P.aeruginosa catB matched PA2509 muconate cycloisomerase I, a different function, with no iModulons. This same-symbol hit was rejected; neither result establishes resistance or lack thereof. No component summary applies. |
| chemistry | Independent RDKit and source-mint checks; 132-chemistry.json;014-root-xref-checks.json | supports | Both native encodings reproduce the full key, formula, charge, one component, exact mass and source mint. Stored average masses agree within the stated decimal precision tolerance; azamulin uses a 0.1-unit tolerance for its one-decimal source value. Focused schema and strict commands exit 0. |
| search | CultureBotAI/AntibioticMech; 132-local-hits.txt;132-maintained-search.txt | context_only | Maintained exact-name/identifier/key searches found the source rows and readiness inventory, without an exact-target curator override. Azidocillin numeric search also returned an unrelated ambiguine Reaxys identifier, rejected as a substring collision. |

## Limits And Additional Notes

- All41 associated bibliographic records and available abstracts were read, but not all full manuscripts. The adopted definition review and older target studies remain abstract/metadata-level; no exhaustive phenicol resistance audit is claimed.
- The2023 accepted manuscript was read selectively for exact analogue results, organism context and enzymatic/growth Methods. Supplementary S24–25 and raw analytical data were not retrieved; no quantitative azidamfenicol MIC or universal inactivation claim is assigned.
- The Basel repository legacy PDF URL now returns an HTML record; Wiley direct requests returned403. The public UFZ accepted manuscript supplied the inspected source. Initial adapter DNS failure was followed by a successful authorized retry.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 21 captured maintained input hashes remain unchanged. No native record was edited. Empty optional fields are not automatically defects.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T095328Z-azidamfenicol-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Azidamfenicol: qualify one stereochemically broader ChEMBL xref and retain
  database evidence limits'
started_at: '2026-10-21T09:24:42Z'
finished_at: '2026-10-21T09:53:28Z'
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
summary: Exact R,R azidamfenicol chemistry and ChEBI grounding are corroborated. CHEMBL278788
  lacks both stereocentre assignments, whereas CHEMBL3989525 matches exactly. Native
  resistance/target annotations honestly retain database scope. An original dehydrogenase
  study supplies a compound-specific inactivation lead, with supplementary assays
  and exact preparation still to inspect.
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
  - path: data/antibiotics/antibacterial/azidamfenicol.yaml
    sha256: 75617cbdd690d915e9b4996dadcb8b413ac2becee017147d992bc49407e4965c
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
- target_id: CHEBI:135238
  path: data/antibiotics/antibacterial/azidamfenicol.yaml
  label: azidamfenicol
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
  selection: Initially uncovered queue position132; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:135238
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:135238
  command: .venv/bin/python /private/tmp/am-review-session/focus014-root.py 132
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:135238
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/azidamfenicol.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:135238
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/azidamfenicol.yaml --out /private/tmp/am-review-session/132-strict.tsv
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
  - CHEBI:135238
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
  - CHEBI:135238
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
  - CHEBI:135238
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
  - CHEBI:135238
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
  - CHEBI:135238
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
  - CHEBI:135238
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
  - CHEBI:135238
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
  - CHEBI:135238
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
  - CHEBI:135238
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/azidamfenicol.yaml
  locator: Entire YAML including24 resistance mechanisms,23S target and seed/reseed
    history
  accessed_at: '2026-10-21T09:37:08Z'
  support: supports
  summary: Read the ARO-derived definition, phenicol class, exact neutral graph, five
    xrefs,24 determinants and23S-rRNA target. Every resistance edge is explicitly
    a database assertion rather than a primary citation; target scope is likewise
    preserved. No quantitative activity, clinical, producer or causal-graph claim
    is asserted.
- evidence_id: source
  kind: record_content
  reference: ARO and ChEBI source inventories;CARD/ARO edge extraction
  locator: 132-raw.json;132-aro-terms.txt;build_concepts/resolve_identity and edge
    mapping
  accessed_at: '2026-10-21T09:37:08Z'
  support: supports
  summary: ChEBI135238 is an adopted out-of-role-scope row used to supply structure
    and exact grounding to ARO3000382; it does not create a second ChEBI source concept
    or unrelated role parents. All24 edges and target reproduce. Acetyltransferases
    map to inactivation and Cfr/Clb/Cip methyltransferase families to target alteration.
    Source qualifiers are scientifically material.
  snapshot_sha256: d51a4c983ba801f2d232e76c2d44451bf4510607f2788389232d074753920c3a
- evidence_id: identity
  kind: database
  reference: CHEBI:135238;PubChem CID:62858;ChEMBL:CHEMBL3989525
  locator: Current chemical resources and independently parsed ChEMBL SMILES
  accessed_at: '2026-10-21T09:37:08Z'
  support: supports
  summary: All agree with native SGRUZFCHLOFYHZ-MWLCHTKSSA-N, C11H13N5O5, neutral
    charge and two R centres. The source title, CAS and phenicol scaffold agree. Exact
    grounding does not require the ChEBI row to be independently within the antimicrobial
    role seed slice.
  snapshot_sha256: c850112033b03a4833034fbf5581c9bd5680bfcca4e6b8b7e5872666d87d5d8c
- evidence_id: xref
  kind: database
  reference: ChEMBL:CHEMBL278788
  locator: 132-CHEMBL278788.json;014-root-xref-checks.json
  accessed_at: '2026-10-21T09:37:08Z'
  support: refutes
  summary: This second retained ChEMBL xref encodes SGRUZFCHLOFYHZ-UHFFFAOYSA-N and
    no stereocentre assignments. Independent parsing identifies two unspecified centres.
    Same connectivity is not exact equivalence to the native R,R drug; no racemate
    composition is inferred.
  snapshot_sha256: e5878ab7794ad68cfb819c78d469e929d0ce363a0be4687fb2b0dfff7697fa73
- evidence_id: adopted
  kind: database
  reference: All41 ARO compound/class/target/determinant citation records
  locator: 132-adopted.json;complete available abstracts and current ARO stanzas
  accessed_at: '2026-10-21T09:37:08Z'
  support: context_only
  summary: All associated records and available abstracts were inspected. Definition
    PMID15539072 is a phenicol-resistance review, not a new azidamfenicol binding
    experiment. Target leads PMID10445875/12860128 concern other peptidyl-transferase
    inhibitors including chloramphenicol;16569865 is pleuromutilin work;16257828/15700955
    are reviews, the latter without an abstract. Most determinant primary abstracts
    concern chloramphenicol rather than exact azidamfenicol. This limits primary promotion,
    not the truth of the honestly labeled source assertions.
  snapshot_sha256: 283b4a66a2a4b4a242938c1872c6ed61be15dbe20e75c72bcdabb9c5419b0a4d
- evidence_id: edge-boundary
  kind: primary_source
  reference: PMID:22547628;PMID:23752511;PMID:27929110;PMID:29259290
  locator: Complete indexed original abstracts in132-adopted.json
  accessed_at: '2026-10-21T09:37:08Z'
  support: partial
  summary: Clb-family and Cip-family papers concern23S methyltransferases;catU concerns
    an acetyltransferase and the later study concerns resistomes. Mechanistic categories
    are compatible with native source assertions. Their inspected abstracts do not
    supply exact azidamfenicol assays for each determinant; absence from those abstracts
    is not a negative susceptibility experiment.
  snapshot_sha256: 283b4a66a2a4b4a242938c1872c6ed61be15dbe20e75c72bcdabb9c5419b0a4d
- evidence_id: oxidation
  kind: primary_source
  reference: PMID:36353978;DOI:10.1002/cbic.202200632
  locator: Public UFZ accepted manuscript132-dehydrogenases-ufz.pdf/text; exact analogue
    Results and enzymatic-assay Methods
  accessed_at: '2026-10-21T09:37:08Z'
  support: partial
  summary: Results explicitly include azidamfenicol oxidative inactivation. Methods
    test200 µM azidamfenicol with purified CAP-ADH+NR or CAP-ADH-NB in phosphate buffer,
    FAD and enzyme at30 C, adding DCIP for the NR enzyme and analyzing methanol-quenched
    samples by UPLC-HRMS. Sources are Nocardiopsis sp.RV163 and Novosphingobium sp.B225.
    Main chloramphenicol MIC/growth experiments must not be transferred to azidamfenicol;
    its supplementary S24–25 outcomes and reagent identity remain to inspect.
  snapshot_sha256: 722d7f2411b3f77a085f67be612885f30d8b91609db57ce3ff7dc554baa8d658
- evidence_id: other-primary
  kind: primary_source
  reference: PMID:580383;PMID:34387504;PMID:33169603
  locator: 132-discovery.json complete available abstracts
  accessed_at: '2026-10-21T09:37:08Z'
  support: partial
  summary: The1978 Baycuten study compares a combination and individual components;
    abstract describes moderate antibacterial activity of acidamfenicol without recoverable
    strain-specific MICs. The2021 and2020 studies report enantioselective synthesis.
    Other search hits address host allergy or analytical combination assays and are
    not antimicrobial-target evidence.
  snapshot_sha256: 876b5641a9026db38959f6fdc68e12dc8cdac660ac6d9c644881547bc9ba5970
- evidence_id: adapter
  kind: database
  reference: Native iModulonDB adapter before web research
  locator: 132-imodulondb-datasets.txt; exact L.reuteri cat and P.aeruginosa catB
    searches
  accessed_at: '2026-10-21T09:37:08Z'
  support: context_only
  summary: Successful catalog retry and both searches completed. L.reuteri search
    returned no genes/modules. P.aeruginosa catB matched PA2509 muconate cycloisomerase
    I, a different function, with no iModulons. This same-symbol hit was rejected;
    neither result establishes resistance or lack thereof. No component summary applies.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit and source-mint checks
  locator: 132-chemistry.json;014-root-xref-checks.json
  accessed_at: '2026-10-21T09:37:08Z'
  support: supports
  summary: Both native encodings reproduce the full key, formula, charge, one component,
    exact mass and source mint. Stored average masses agree within the stated decimal
    precision tolerance; azamulin uses a 0.1-unit tolerance for its one-decimal source
    value. Focused schema and strict commands exit 0.
  snapshot_sha256: 2ffae5ad490d6586674a953808983b60bd41e07daf540cfbf87947b67e72a841
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 132-local-hits.txt;132-maintained-search.txt
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
  snapshot_sha256: 3b0f7d1cb8c291db1701387a20fe8aff4c223ecbff9564f5307b7771d934e6cd
assessments:
- assessment_id: provenance
  area: provenance
  topic: Source reproduction, ownership and native status
  outcome: supported
  summary: Captured maintained inputs remain unchanged. Source extraction and seeding
    explain native fields; structured review does not change SEEDED status.
  target_ids:
  - CHEBI:135238
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
  - CHEBI:135238
  evidence_ids:
  - chemistry
- assessment_id: identity
  area: identity
  topic: Native R,R identity and retained ChEMBL mapping
  outcome: concern
  summary: Exact graph agrees with ChEBI/PubChem/one ChEMBL record, but the second
    ChEMBL xref lacks stereo assignments.
  target_ids:
  - CHEBI:135238
  evidence_ids:
  - identity
  - xref
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Source slice and class
  outcome: supported
  summary: ARO-to-ChEBI exact structure grounding and phenicol classification reproduce;
    out-of-role-scope source handling explains omitted standalone ChEBI source concept.
  target_ids:
  - CHEBI:135238
  evidence_ids:
  - source
  - identity
- assessment_id: mechanism
  area: evidence
  topic: Database target and resistance scope
  outcome: supported
  summary: No source assertion is mislabeled as an exact-compound primary experiment.
    Current categories align with determinant functions; source-specific evidence
    must be retained until primary assay verification.
  target_ids:
  - CHEBI:135238
  evidence_ids:
  - native
  - source
  - adopted
  - edge-boundary
- assessment_id: definition
  area: evidence
  topic: Shared phenicol mode and solubility wording
  outcome: unknown
  summary: The source review supports class context; exact compound solubility measurement
    and23S interaction experiments were not independently recovered. This is a primary-evidence
    limitation rather than a demonstrated false statement.
  target_ids:
  - CHEBI:135238
  evidence_ids:
  - adopted
  - other-primary
- assessment_id: completeness
  area: completeness
  topic: Exact oxidative inactivation lead
  outcome: unknown
  summary: Purified-enzyme oxidation evidence is available for azidamfenicol. Supplementary
    activity, preparation and protein accessions require verification before organism-specific
    resistance or causal annotation.
  target_ids:
  - CHEBI:135238
  evidence_ids:
  - oxidation
  - adapter
findings:
- finding_id: F1
  issue_key: azidamfenicol-chembl278788-stereo-scope
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Remove or qualify the ChEMBL cross-reference that lacks both stereo assignments
  description: CHEMBL278788 represents stereochemically unspecified connectivity,
    while native R,R azidamfenicol agrees exactly with CHEMBL3989525. Keep the correct
    graph and exact link; do not present both entries as interchangeable exact chemical
    identifiers.
  target_ids:
  - CHEBI:135238
  field_paths:
  - xrefs
  evidence_ids:
  - identity
  - xref
  - source
  rule_id: 'native-review-checklist: Exact identity, evidence scope and completeness'
  native_severity: major
  normalization_reason: CHEMBL278788 represents stereochemically unspecified connectivity,
    while native R,R azidamfenicol agrees exactly with CHEMBL3989525. Keep the correct
    graph and exact link; do not present both entries as interchangeable exact chemical
    identifiers.
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
  issue_key: azidamfenicol-qualified-oxidative-inactivation-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Curate exact inactivation evidence separately from broad phenicol source
    assertions
  description: The2023 original study includes exact azidamfenicol oxidation experiments.
    Verify supplementary inactivation and preparation details before primary evidence
    is added; do not promote every chloramphenicol-family edge merely from shared
    scaffold.
  target_ids:
  - CHEBI:135238
  field_paths:
  - resistance_mechanisms
  - molecular_targets
  - evidence
  - discussions
  evidence_ids:
  - oxidation
  - adopted
  - edge-boundary
  - adapter
  rule_id: 'native-review-checklist: Exact identity, evidence scope and completeness'
  native_severity: informational
  normalization_reason: The2023 original study includes exact azidamfenicol oxidation
    experiments. Verify supplementary inactivation and preparation details before
    primary evidence is added; do not promote every chloramphenicol-family edge merely
    from shared scaffold.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/azidamfenicol.yaml
    role: Curator-owned primary evidence and optional resistance/target context
actions:
- action_id: A1
  description: Correct the maintained cross-reference mapping while preserving exact
    chemistry.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:135238
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
  - Compare full InChIs and both centres; retain CHEMBL3989525 and the native full
    key.
  - Remove or qualify278788 through supported source/xref policy, keeping provenance
    and avoiding an unsupported racemate assertion.
  - Regenerate and run exact-identity plus focused/schema/reference gates; no direct
    generated-only patch.
- action_id: A2
  description: Verify original compound-specific experiments before optional evidence
    upgrades.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:135238
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/azidamfenicol.yaml
    role: Curator-owned primary evidence and optional resistance/target context
  acceptance_checks:
  - Retrieve S24–25 and supplier/structure details for azidamfenicol; keep enzyme
    oxidation, loss of antibacterial activity and isolate resistance as separate endpoints.
  - Resolve exact NR/NB proteins and strains before adding accessions or species-wide
    claims.
  - Inspect exact-drug assays for each existing determinant before changing its database-only
    evidence; chloramphenicol results alone do not prove azidamfenicol phenotypes.
  - Do not reinterpret the PA2509 catB metabolic enzyme hit as an antibiotic acetyltransferase.
limitations:
- All41 associated bibliographic records and available abstracts were read, but not
  all full manuscripts. The adopted definition review and older target studies remain
  abstract/metadata-level; no exhaustive phenicol resistance audit is claimed.
- The2023 accepted manuscript was read selectively for exact analogue results, organism
  context and enzymatic/growth Methods. Supplementary S24–25 and raw analytical data
  were not retrieved; no quantitative azidamfenicol MIC or universal inactivation
  claim is assigned.
- The Basel repository legacy PDF URL now returns an HTML record; Wiley direct requests
  returned403. The public UFZ accepted manuscript supplied the inspected source. Initial
  adapter DNS failure was followed by a successful authorized retry.
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
- https://www.ebi.ac.uk/chebi/CHEBI:135238
- https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL278788
- https://doi.org/10.1002/cbic.202200632
```
