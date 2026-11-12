# Cefotetan disodium: exact salt and a coordinate-dependent InChI normalization boundary

- Review: 20261021T113836Z-cefotetan-disodium
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T11:21:18Z
- Finished UTC: 2026-10-21T11:38:36Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

No confirmed native defect. The disodium stoichiometry, neutral total charge, formula, masses and 6R,7S core agree. The native InChI directly hashes to its stored key; a generic molecule-roundtrip key check fails because the coupled dithietane stereolayer changes on normalization. KEGG reproduces both keys solely by retaining or removing coordinates, with identical canonical isomeric SMILES and mutual chiral matches. The primary 2021 assay names a catalog code currently assigned to the exact salt and supports antibacterial activity with bounded material and isolate scope. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole-record review of cefotetan disodium, separate from neutral cefotetan and pharmaceutical products.

Selection: Queue 234 in isolated batch 024; original inspection captures preserved, actual maintained owners read before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:34617 | data/antibiotics/antibacterial/cefotetan-disodium.yaml | generated | cefotetan disodium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | CHEBI:34617 | Actual focused command passed with zero errors. |
| Focused strict | passed | True | CHEBI:34617 | Actual focused command passed with zero errors. |
| Supplemental molecular encodings and source mint | failed | False | CHEBI:34617 | Formula, charge, masses, two assigned core centres and mint agree. Stored-key comparison fails after RDKit molecule roundtrip; the coordinate experiment below bounds this as a normalization issue, not demonstrated wrong identity. |
| KEGG coordinate-removal experiment | passed | False | CHEBI:34617 | With coordinates the KEGG molfile yields the native key; removing only conformers yields the PubChem/native-SMILES key. Isomeric SMILES and mutual chirality-aware graph matches agree. |
| Authoritative full QC | failed | True | CHEBI:34617 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:34617 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:34617 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:34617 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:34617 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:34617 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:34617 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:34617 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:34617 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact disodium salt

identity: supported. Targets: CHEBI:34617.

Formula, two sodium ions, charge, masses, source identifier, 6R,7S core and exact name agree across native/current authorities. Neutral cefotetan remains separate.

### Coupled stereolayer and key normalization

identity: unknown. Targets: CHEBI:34617.

The recorded InChI hashes correctly. KEGG coordinates reproduce that exact string; removing only conformers reproduces the alternative key without a changed canonical isomeric SMILES or assigned core stereo. Record the actual failed equality check and defer any representation correction until a documented normalization policy resolves the coupled dithietane stereolayer.

### Parent and filing/role

grounding: supported. Targets: CHEBI:34617.

Organic sodium salt is strictly broader than this disodium structure. Current authority preserves antibacterial-drug role, and primary activity with a supplier-code salt match supports antibacterial filing.

### Exact versus drug-level cross-references

grounding: unknown. Targets: CHEBI:34617.

CAS resolves the same disodium formula and core within the documented normalization boundary. KEGG D02228 is explicitly the salt. Independent Beilstein contents remain uninspected.

### Exact preparation and isolate scope

evidence: supported. Targets: CHEBI:34617.

The native record has no numeric activity claim. The 2021 source offers optional primary enrichment with catalog-code salt mapping, nonrandom bloodstream-isolate selection, digital BMD and explicit breakpoints. Current catalog identity is stronger than a drug name alone; historical batch potency remains a qualification.

### No native molecular mechanism assertion

evidence: not_applicable. Targets: CHEBI:34617.

No native mode, molecular target or resistance claim is present. KEGG’s generic PBP annotation and genotype-associated MIC differences do not independently prove a specific direct-binding measurement or causal hydrolysis pathway.

### Structured-source adapter applicability

scope: not_applicable. Targets: CHEBI:34617.

The native record names no gene, protein, pathway, regulator or expression dataset. No native iModulonDB candidate exists; absence from that database is not inferred as negative evidence.

### Clinical, producer, graph and dataset scope

scope: not_applicable. Targets: CHEBI:34617.

No native assertion is made in these optional domains. Product names, historical treatment discussion and bacterial assay isolates are not transferred to approval, biosynthetic producer or causal graph claims.

### Maintained source ownership and audit trail

provenance: supported. Targets: CHEBI:34617.

ChEBI inventory owns the seeded content; mint and all four seed/reseed events are coherent. No adopted PMID leads require disposition. Original input hashes and SEEDED status are preserved.

### Bounded optional curation

completeness: supported. Targets: CHEBI:34617.

Primary activity can be added with material and assay qualification. Empty optional fields alone do not constitute native schema defects, and this review does not confer REVIEWED status.

### Actual validation and limits

schema: supported. Targets: CHEBI:34617.

Focused schema/strict pass. The failed independent key comparison is retained alongside a successful discriminating normalization experiment; deterministic results are not substituted for source review.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Document the coupled stereolayer normalization policy before changing any exact identity field.

- Reproduce the original D02228 molfile with and without conformers, preserving core 6R,7S, two sodium ions, charge, formula, masses and exact source snapshot.
- Explain /b12-6- together with /t13? using documented InChI/toolkit semantics. A changed generated hash alone does not prove a different stereoisomer.
- Any separately authorized source correction must propagate through maintained owners/reseeding and pass schema/strict, chemical identity and applicable corpus/history checks.

### A2

Optionally add the 2021 exact-preparation activity with source-specific limits.

- Cite DOI 10.1128/spectrum.00226-21 at the activity object; retain Glentham GA5476, DMSO, CAMHB, digital BMD, inoculum and nonrandom 110 E. coli/40 K. pneumoniae isolate context.
- Keep aggregate MIC50/MIC90 distinct from single-isolate MICs. Confirm historical lot identity and potency basis before asserting unqualified mass concentrations of pure anhydrous salt.
- Preserve the paper’s 32 mg/L intermediate rule versus conflicting Results wording and resolve the ampC subgroup denominator before adding genotype-specific counts or mechanistic conclusions.
- Do not infer clinical efficacy, exact protein binding or isolated enzyme hydrolysis from this susceptibility study. Run native validation and add an accurate curation event only under separate curation authorization.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/cefotetan-disodium.yaml; Entire YAML | supports | Read identity, definition, four synonyms, organic sodium salt parent, antibacterial-drug role, complete chemical structure, two exact xrefs and one drug xref, source concept/mint and all four seed/reseed events. No native activity, mode, target, resistance, clinical, producer, dataset or causal-graph assertion is populated. |
| owners | data/raw/chebi_antimicrobials.tsv; Row 717, CHEBI:34617; actual maintained owners and source configuration | supports | The adopted ChEBI row owns identity, role, complete structure and xrefs. It contains no adopted PMID citation leads. Extractor/seeder and decision table are maintained correction routes; no generated-only repair is proposed. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:34617; Current complete structure, ontology and xrefs | supports | Current authority matches native disodium formula, charge zero, 619.596 average and 618.96603 monoisotopic mass, 6R,7S core, SMILES, InChI and stored ZQQALMSFFARWPK-GLHLDKNHSA-L. CHEBI:38700 is organic sodium salt; CHEBI:36047 is antibacterial drug. The additional current antiinfective-agent role does not require optional-field expansion. |
| chemistry | RDKit 2026.03.5 molecular checks; 234-chemistry.json | partial | Both molecular encodings parse and reproduce three fragments, two sodium counterions, net zero charge, C17H15N7Na2O8S4, matching masses and assigned core R/S. Source mint chebi-490b4b885d is correct. Molecule-roundtrip key is ZQQALMSFFARWPK-ZTQQJVKJSA-L rather than the stored GLHLDKNHSA-L; this failure is retained. |
| direct-inchi | Direct native InChI hashing and roundtrip; 234-roundtrip.json | partial | Direct InchiToInchiKey yields the retained GLHLDKNHSA-L key. The molecule roundtrip drops /b12-6- while retaining /t13?,15-,17+ and the core stereochemistry. Direct hashing and re-creating an InChI from a molecular graph are different operations. |
| kegg | https://rest.kegg.jp/get/D02228; Drug identity, formula, CAS and classification | supports | D02228 resolves cefotetan disodium/cefotetan sodium, CAS 74356-00-6, matching formula and mass. Generic penicillin-binding-protein/cell-wall annotations and product listings are database context; they are not adopted as a new primary target or current clinical-status assertion. |
| kegg-mol | https://rest.kegg.jp/get/D02228/mol; Original downloaded 2D molfile | supports | The exact disodium molfile retains the core stereobonds and coordinates. InChI generated with those coordinates reproduces the native retained InChI and key. |
| coordinates | Independent KEGG molfile normalization comparison; 234-coordinate-check.py and 234-coordinate-check.json | partial | Removing only conformers changes GLHLDKNHSA-L to ZTQQJVKJSA-L and omits /b12-6-. Both versions and native SMILES have identical canonical isomeric SMILES, matching formulas and core R/S, and mutual useChirality graph matches. This reproduces a representation-dependent coupled stereolayer boundary; it does not establish two different salt identities or justify an automatic native correction. |
| cas-pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/74356-00-6/JSON; CAS lookup; CID 53024 full structure | partial | CAS 74356-00-6 resolves cefotetan disodium CID 53024, same formula, stoichiometry and 6R,7S core. Its ZTQQJVKJSA-L key matches the normalized graph. The key difference from ChEBI is preserved explicitly rather than describing all encodings as byte-identical. |
| beilstein | https://www.ebi.ac.uk/chebi/CHEBI:34617; Registry Beilstein 5716628 | partial | Current ChEBI retains Beilstein 5716628. Independent proprietary registry contents were not inspected through free access; no contrary exact-compound mapping was demonstrated. |
| activity-primary | DOI:10.1128/spectrum.00226-21; PMID 34232101; complete main text, Table 1, Results and Materials and Methods | supports | Original 2021 digital broth-microdilution study used cefotetan powder Glentham GA5476 in DMSO, CAMHB and approximately 5×10^5 CFU/mL. Among 150 nonrandomly selected MERINO bloodstream isolates (110 E. coli, 40 K. pneumoniae), MIC50 was 0.25 and MIC90 2 mg/L, range ≤0.125–64 mg/L, with 98.7% susceptible by the paper’s stated CLSI thresholds. This is in vitro activity of the stated preparation, not clinical efficacy or a purified-enzyme causal experiment. |
| material | https://www.glentham.com/en/products/product/GA5476/; Official GA5476 identity and specifications | supports | The same catalog code named in the primary methods currently resolves cefotetan disodium salt, CAS 74356-00-6, C17H15N7Na2O8S4, with sodium identification, water ≤3% and dried-basis potency specifications. This strengthens exact-salt material mapping; the historical lot certificate and the paper’s potency/mass correction were not inspected. |
| primary-conflict | DOI:10.1128/spectrum.00226-21; Results versus Methods and Table 1 | partial | The first Results paragraph initially groups the K. pneumoniae isolate at 32 mg/L as resistant, then calls it intermediate; Methods specifies susceptible ≤16, intermediate 32 and resistant ≥64 mg/L. Retain the raw 32 mg/L and the stated intermediate threshold if curated. The paper also gives seven ampC isolates in its abstract while Table 1 separates seven ESBL+ampC and two ESBL+ampC+OXA rows; avoid silently reconciling this denominator. Neither conflict changes the broad native antibacterial-drug role. |
| older-activity | PMID:6954875; DOI 10.1128/AAC.21.3.486; inspected abstract and PMC landing text | context_only | The 1982 primary abstract describes activity against 273 clinical isolates and strong taxon-dependent differences. The scanned methods and historical reagent salt were not inspected, so this remains a contextual earlier lead and supplies no exact-salt quantitative observation here. |
| search | Ignored-inclusive local search and free Europe PMC title/activity search; 234-owner-hits.txt;234-local-hits.txt;234-primary-search.json | context_only | Searched identifier, label, slug and full key across batch 024 including ignored/hidden material outside .git/.venv; rendered/research artifacts are discovery context only. Free title searches for cefotetan/YM09330/YM-09330 and activity led to the inspected primary source. No claim of exhaustive historical literature coverage. |
| gates | Native focused validators; 234-focused-results.json | supports | Schema and strict each exit 0 with no errors. The independent generic chemistry command exits 1 solely at roundtrip key equality; native identity and an explicit normalization experiment were assessed separately. |

## Limits And Additional Notes

- Generic RDKit roundtrip key equality fails. The coordinate experiment identifies a reproducible normalization boundary but does not establish which coupled-stereochemistry representation should be canonical for future source harmonization.
- Independent Beilstein registry contents were not inspected through free access. Current supplier catalog mapping does not replace the historical assay-lot certificate or an explicit potency correction.
- The 2021 study is a nonrandom isolate-panel experiment, not a clinical-efficacy or purified-target experiment. Its Results wording at 32 mg/L and ampC subgroup counts contain bounded internal discrepancies.
- The additional 1982 source was inspected at abstract/landing-page level only; scanned methods and exact preparation remain unresolved. Literature discovery was bounded, not an exhaustive historical review.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 20 captured input hashes unchanged, preserving the original inspection captures. No native/source/status/history edits.
- Native schema/strict used the batch 024 environment. Chemistry used the existing batch 019 locked RDKit 2026.03.5 interpreter against batch 024 cwd; no new toolkit installation.
- Free public retrieval only. EPMC full XML for the 1982 paper returned 500; its accessible PMC landing text and abstract were retained only as a limited lead.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T113836Z-cefotetan-disodium
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cefotetan disodium: exact salt and a coordinate-dependent InChI normalization
  boundary'
started_at: '2026-10-21T11:21:18Z'
finished_at: '2026-10-21T11:38:36Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independent entire native/maintained owner review; current ChEBI,
    CAS/PubChem, KEGG and supplier records; molecular checks plus a coordinate-removal
    experiment; complete 2021 primary text and assay table.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: No confirmed native defect. The disodium stoichiometry, neutral total charge,
  formula, masses and 6R,7S core agree. The native InChI directly hashes to its stored
  key; a generic molecule-roundtrip key check fails because the coupled dithietane
  stereolayer changes on normalization. KEGG reproduces both keys solely by retaining
  or removing coordinates, with identical canonical isomeric SMILES and mutual chiral
  matches. The primary 2021 assay names a catalog code currently assigned to the exact
  salt and supports antibacterial activity with bounded material and isolate scope.
  Scientific assessment retains the stated evidence limits; full verification is blocked
  by the shared native-library failure.
source:
  git_revision: baf3b3203d748d098686e166cdb2a6138f47eb59
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 5e2e1f975f8aa64f92a06c134c98c750c968fd78f02620a73c9cb611ac018ed8
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: CLAUDE.md
    sha256: 36fb92f8919481cfbf3f17ddde4a1e244c81f76c64396dbbac910c4815fb9f16
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
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
  - path: data/antibiotics/antibacterial/cefotetan-disodium.yaml
    sha256: 26a28d6f74420538832a7d477ea066a7c610564e582864ac4bf1b444641da72a
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
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
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
- target_id: CHEBI:34617
  path: data/antibiotics/antibacterial/cefotetan-disodium.yaml
  label: cefotetan disodium
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted exact ChEBI identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding and exclusion overrides
scope:
  description: Whole-record review of cefotetan disodium, separate from neutral cefotetan
    and pharmaceutical products.
  selection: Queue 234 in isolated batch 024; original inspection captures preserved,
    actual maintained owners read before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:34617
  exclusions:
  - target: Neutral cefotetan, other salts, formulation/excipient mixtures and isomers
    reason: Different form or material scope; activity and clinical claims require
      exact preparation mapping.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual focused command passed with zero errors.
  target_ids:
  - CHEBI:34617
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefotetan-disodium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: strict
  name: Focused strict
  status: passed
  required: true
  summary: Actual focused command passed with zero errors.
  target_ids:
  - CHEBI:34617
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefotetan-disodium.yaml --out /private/tmp/am-review-session/234-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Supplemental molecular encodings and source mint
  status: failed
  required: false
  summary: Formula, charge, masses, two assigned core centres and mint agree. Stored-key
    comparison fails after RDKit molecule roundtrip; the coordinate experiment below
    bounds this as a normalization issue, not demonstrated wrong identity.
  target_ids:
  - CHEBI:34617
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/check199200.py
    234 (cwd /private/tmp/antibioticmech-record-reviews-024)
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - chemistry
  - coordinates
- check_id: coordinate-normalization
  name: KEGG coordinate-removal experiment
  status: passed
  required: false
  summary: With coordinates the KEGG molfile yields the native key; removing only
    conformers yields the PubChem/native-SMILES key. Isomeric SMILES and mutual chirality-aware
    graph matches agree.
  target_ids:
  - CHEBI:34617
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/234-coordinate-check.py
    (cwd /private/tmp/antibioticmech-record-reviews-024)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - coordinates
  - kegg-mol
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:34617
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
  - CHEBI:34617
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
  - CHEBI:34617
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
  - CHEBI:34617
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
  - CHEBI:34617
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
  - CHEBI:34617
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
  - CHEBI:34617
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
  - CHEBI:34617
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
  - CHEBI:34617
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/cefotetan-disodium.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T11:34:03Z'
  support: supports
  summary: Read identity, definition, four synonyms, organic sodium salt parent, antibacterial-drug
    role, complete chemical structure, two exact xrefs and one drug xref, source concept/mint
    and all four seed/reseed events. No native activity, mode, target, resistance,
    clinical, producer, dataset or causal-graph assertion is populated.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Row 717, CHEBI:34617; actual maintained owners and source configuration
  accessed_at: '2026-10-21T11:34:03Z'
  support: supports
  summary: The adopted ChEBI row owns identity, role, complete structure and xrefs.
    It contains no adopted PMID citation leads. Extractor/seeder and decision table
    are maintained correction routes; no generated-only repair is proposed.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:34617
  locator: Current complete structure, ontology and xrefs
  accessed_at: '2026-10-21T11:23:17Z'
  support: supports
  summary: Current authority matches native disodium formula, charge zero, 619.596
    average and 618.96603 monoisotopic mass, 6R,7S core, SMILES, InChI and stored
    ZQQALMSFFARWPK-GLHLDKNHSA-L. CHEBI:38700 is organic sodium salt; CHEBI:36047 is
    antibacterial drug. The additional current antiinfective-agent role does not require
    optional-field expansion.
  snapshot_sha256: bdf1dba88a54044386345f73581d532a5d38fbc5b3633d171177337a61e6e80d
- evidence_id: chemistry
  kind: validation
  reference: RDKit 2026.03.5 molecular checks
  locator: 234-chemistry.json
  accessed_at: '2026-10-21T11:22:40Z'
  support: partial
  summary: Both molecular encodings parse and reproduce three fragments, two sodium
    counterions, net zero charge, C17H15N7Na2O8S4, matching masses and assigned core
    R/S. Source mint chebi-490b4b885d is correct. Molecule-roundtrip key is ZQQALMSFFARWPK-ZTQQJVKJSA-L
    rather than the stored GLHLDKNHSA-L; this failure is retained.
  snapshot_sha256: 37d0aeb37a116d0f2f856bf9782ffa3ac5b39f22b7d140aa0764b4261fd3b930
- evidence_id: direct-inchi
  kind: validation
  reference: Direct native InChI hashing and roundtrip
  locator: 234-roundtrip.json
  accessed_at: '2026-10-21T11:23:18Z'
  support: partial
  summary: Direct InchiToInchiKey yields the retained GLHLDKNHSA-L key. The molecule
    roundtrip drops /b12-6- while retaining /t13?,15-,17+ and the core stereochemistry.
    Direct hashing and re-creating an InChI from a molecular graph are different operations.
  snapshot_sha256: e23f9820fc49d2aaa5d8df78425abd40d88774994f0dedb3b8af51c9034b040c
- evidence_id: kegg
  kind: database
  reference: https://rest.kegg.jp/get/D02228
  locator: Drug identity, formula, CAS and classification
  accessed_at: '2026-10-21T11:23:18Z'
  support: supports
  summary: D02228 resolves cefotetan disodium/cefotetan sodium, CAS 74356-00-6, matching
    formula and mass. Generic penicillin-binding-protein/cell-wall annotations and
    product listings are database context; they are not adopted as a new primary target
    or current clinical-status assertion.
  snapshot_sha256: 139451a8c0e23f8bf51edae3e56d64ca90c7139b61dd8698efae242fcb396a0f
- evidence_id: kegg-mol
  kind: database
  reference: https://rest.kegg.jp/get/D02228/mol
  locator: Original downloaded 2D molfile
  accessed_at: '2026-10-21T11:31:57Z'
  support: supports
  summary: The exact disodium molfile retains the core stereobonds and coordinates.
    InChI generated with those coordinates reproduces the native retained InChI and
    key.
  snapshot_sha256: 79b5d65c2fa814c124e2293c54671349400845f95c00d67fac9ac8b08843bf4a
- evidence_id: coordinates
  kind: validation
  reference: Independent KEGG molfile normalization comparison
  locator: 234-coordinate-check.py and 234-coordinate-check.json
  accessed_at: '2026-10-21T11:32:22Z'
  support: partial
  summary: Removing only conformers changes GLHLDKNHSA-L to ZTQQJVKJSA-L and omits
    /b12-6-. Both versions and native SMILES have identical canonical isomeric SMILES,
    matching formulas and core R/S, and mutual useChirality graph matches. This reproduces
    a representation-dependent coupled stereolayer boundary; it does not establish
    two different salt identities or justify an automatic native correction.
  snapshot_sha256: a30f4b31ef1363e90fb1be0bfb7860e02b3af357774cca6eed3d9b7a503d55f5
- evidence_id: cas-pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/74356-00-6/JSON
  locator: CAS lookup; CID 53024 full structure
  accessed_at: '2026-10-21T11:23:17Z'
  support: partial
  summary: CAS 74356-00-6 resolves cefotetan disodium CID 53024, same formula, stoichiometry
    and 6R,7S core. Its ZTQQJVKJSA-L key matches the normalized graph. The key difference
    from ChEBI is preserved explicitly rather than describing all encodings as byte-identical.
  snapshot_sha256: 38a192bdbae32c5849015e8ff2a6ef4d81f2006d56c94fafc908991fda1642cf
- evidence_id: beilstein
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:34617
  locator: Registry Beilstein 5716628
  accessed_at: '2026-10-21T11:23:17Z'
  support: partial
  summary: Current ChEBI retains Beilstein 5716628. Independent proprietary registry
    contents were not inspected through free access; no contrary exact-compound mapping
    was demonstrated.
  snapshot_sha256: bdf1dba88a54044386345f73581d532a5d38fbc5b3633d171177337a61e6e80d
- evidence_id: activity-primary
  kind: primary_source
  reference: DOI:10.1128/spectrum.00226-21
  locator: PMID 34232101; complete main text, Table 1, Results and Materials and Methods
  accessed_at: '2026-10-21T11:25:29Z'
  support: supports
  summary: Original 2021 digital broth-microdilution study used cefotetan powder Glentham
    GA5476 in DMSO, CAMHB and approximately 5×10^5 CFU/mL. Among 150 nonrandomly selected
    MERINO bloodstream isolates (110 E. coli, 40 K. pneumoniae), MIC50 was 0.25 and
    MIC90 2 mg/L, range ≤0.125–64 mg/L, with 98.7% susceptible by the paper’s stated
    CLSI thresholds. This is in vitro activity of the stated preparation, not clinical
    efficacy or a purified-enzyme causal experiment.
  snapshot_sha256: dd2e927acfe6585606f3cbfa5df4fdfb61c020633210c5d8c8c17f2f69ee51ba
- evidence_id: material
  kind: authority
  reference: https://www.glentham.com/en/products/product/GA5476/
  locator: Official GA5476 identity and specifications
  accessed_at: '2026-10-21T11:26:20Z'
  support: supports
  summary: The same catalog code named in the primary methods currently resolves cefotetan
    disodium salt, CAS 74356-00-6, C17H15N7Na2O8S4, with sodium identification, water
    ≤3% and dried-basis potency specifications. This strengthens exact-salt material
    mapping; the historical lot certificate and the paper’s potency/mass correction
    were not inspected.
  snapshot_sha256: a731a82d4351c7c5b6d27d40ac95f43bbe4c5eeaed8ba0544fdecdc577bbc7d4
- evidence_id: primary-conflict
  kind: primary_source
  reference: DOI:10.1128/spectrum.00226-21
  locator: Results versus Methods and Table 1
  accessed_at: '2026-10-21T11:25:29Z'
  support: partial
  summary: The first Results paragraph initially groups the K. pneumoniae isolate
    at 32 mg/L as resistant, then calls it intermediate; Methods specifies susceptible
    ≤16, intermediate 32 and resistant ≥64 mg/L. Retain the raw 32 mg/L and the stated
    intermediate threshold if curated. The paper also gives seven ampC isolates in
    its abstract while Table 1 separates seven ESBL+ampC and two ESBL+ampC+OXA rows;
    avoid silently reconciling this denominator. Neither conflict changes the broad
    native antibacterial-drug role.
  snapshot_sha256: dd2e927acfe6585606f3cbfa5df4fdfb61c020633210c5d8c8c17f2f69ee51ba
- evidence_id: older-activity
  kind: primary_source
  reference: PMID:6954875
  locator: DOI 10.1128/AAC.21.3.486; inspected abstract and PMC landing text
  accessed_at: '2026-10-21T11:24:39Z'
  support: context_only
  summary: The 1982 primary abstract describes activity against 273 clinical isolates
    and strong taxon-dependent differences. The scanned methods and historical reagent
    salt were not inspected, so this remains a contextual earlier lead and supplies
    no exact-salt quantitative observation here.
  snapshot_sha256: c4eaca502fc27e963b34770f0a6995837c6469b479f5527368439910645b8986
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local search and free Europe PMC title/activity search
  locator: 234-owner-hits.txt;234-local-hits.txt;234-primary-search.json
  accessed_at: '2026-10-21T11:24:39Z'
  support: context_only
  summary: Searched identifier, label, slug and full key across batch 024 including
    ignored/hidden material outside .git/.venv; rendered/research artifacts are discovery
    context only. Free title searches for cefotetan/YM09330/YM-09330 and activity
    led to the inspected primary source. No claim of exhaustive historical literature
    coverage.
  snapshot_sha256: c4eaca502fc27e963b34770f0a6995837c6469b479f5527368439910645b8986
  search_scope: Batch 024 rg --no-ignore --hidden, excluding .git/.venv; exact CHEBI:34617,
    cefotetan disodium, cefotetan-disodium and stored full key. Free Europe PMC title/activity
    and YM-09330 follow-up on 2026-10-21, with current ChEBI/CAS/KEGG and supplier
    records.
- evidence_id: gates
  kind: validation
  reference: Native focused validators
  locator: 234-focused-results.json
  accessed_at: '2026-10-21T11:22:40Z'
  support: supports
  summary: Schema and strict each exit 0 with no errors. The independent generic chemistry
    command exits 1 solely at roundtrip key equality; native identity and an explicit
    normalization experiment were assessed separately.
  snapshot_sha256: dd7cb109e51a0088299e68fc74fc60130c4cf0a3e7caea1cc6efe6da8a2ed693
assessments:
- assessment_id: identity
  area: identity
  topic: Exact disodium salt
  outcome: supported
  summary: Formula, two sodium ions, charge, masses, source identifier, 6R,7S core
    and exact name agree across native/current authorities. Neutral cefotetan remains
    separate.
  target_ids:
  - CHEBI:34617
  evidence_ids:
  - native
  - chebi
  - chemistry
  - kegg
  - cas-pubchem
- assessment_id: normalization
  area: identity
  topic: Coupled stereolayer and key normalization
  outcome: unknown
  summary: The recorded InChI hashes correctly. KEGG coordinates reproduce that exact
    string; removing only conformers reproduces the alternative key without a changed
    canonical isomeric SMILES or assigned core stereo. Record the actual failed equality
    check and defer any representation correction until a documented normalization
    policy resolves the coupled dithietane stereolayer.
  target_ids:
  - CHEBI:34617
  evidence_ids:
  - chemistry
  - direct-inchi
  - coordinates
  - kegg-mol
  - cas-pubchem
- assessment_id: grounding
  area: grounding
  topic: Parent and filing/role
  outcome: supported
  summary: Organic sodium salt is strictly broader than this disodium structure. Current
    authority preserves antibacterial-drug role, and primary activity with a supplier-code
    salt match supports antibacterial filing.
  target_ids:
  - CHEBI:34617
  evidence_ids:
  - chebi
  - kegg
  - activity-primary
  - material
- assessment_id: xrefs
  area: grounding
  topic: Exact versus drug-level cross-references
  outcome: unknown
  summary: CAS resolves the same disodium formula and core within the documented normalization
    boundary. KEGG D02228 is explicitly the salt. Independent Beilstein contents remain
    uninspected.
  target_ids:
  - CHEBI:34617
  evidence_ids:
  - cas-pubchem
  - kegg
  - beilstein
  - coordinates
- assessment_id: activity
  area: evidence
  topic: Exact preparation and isolate scope
  outcome: supported
  summary: The native record has no numeric activity claim. The 2021 source offers
    optional primary enrichment with catalog-code salt mapping, nonrandom bloodstream-isolate
    selection, digital BMD and explicit breakpoints. Current catalog identity is stronger
    than a drug name alone; historical batch potency remains a qualification.
  target_ids:
  - CHEBI:34617
  evidence_ids:
  - native
  - activity-primary
  - material
  - primary-conflict
- assessment_id: mechanism
  area: evidence
  topic: No native molecular mechanism assertion
  outcome: not_applicable
  summary: No native mode, molecular target or resistance claim is present. KEGG’s
    generic PBP annotation and genotype-associated MIC differences do not independently
    prove a specific direct-binding measurement or causal hydrolysis pathway.
  target_ids:
  - CHEBI:34617
  evidence_ids:
  - native
  - kegg
  - activity-primary
- assessment_id: adapter
  area: scope
  topic: Structured-source adapter applicability
  outcome: not_applicable
  summary: The native record names no gene, protein, pathway, regulator or expression
    dataset. No native iModulonDB candidate exists; absence from that database is
    not inferred as negative evidence.
  target_ids:
  - CHEBI:34617
  evidence_ids:
  - native
- assessment_id: other-fields
  area: scope
  topic: Clinical, producer, graph and dataset scope
  outcome: not_applicable
  summary: No native assertion is made in these optional domains. Product names, historical
    treatment discussion and bacterial assay isolates are not transferred to approval,
    biosynthetic producer or causal graph claims.
  target_ids:
  - CHEBI:34617
  evidence_ids:
  - native
  - kegg
  - activity-primary
- assessment_id: provenance
  area: provenance
  topic: Maintained source ownership and audit trail
  outcome: supported
  summary: ChEBI inventory owns the seeded content; mint and all four seed/reseed
    events are coherent. No adopted PMID leads require disposition. Original input
    hashes and SEEDED status are preserved.
  target_ids:
  - CHEBI:34617
  evidence_ids:
  - native
  - owners
  - chemistry
- assessment_id: completeness
  area: completeness
  topic: Bounded optional curation
  outcome: supported
  summary: Primary activity can be added with material and assay qualification. Empty
    optional fields alone do not constitute native schema defects, and this review
    does not confer REVIEWED status.
  target_ids:
  - CHEBI:34617
  evidence_ids:
  - native
  - activity-primary
  - material
- assessment_id: schema
  area: schema
  topic: Actual validation and limits
  outcome: supported
  summary: Focused schema/strict pass. The failed independent key comparison is retained
    alongside a successful discriminating normalization experiment; deterministic
    results are not substituted for source review.
  target_ids:
  - CHEBI:34617
  evidence_ids:
  - gates
  - chemistry
  - coordinates
findings: []
actions:
- action_id: A1
  description: Document the coupled stereolayer normalization policy before changing
    any exact identity field.
  finding_ids: []
  target_ids:
  - CHEBI:34617
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Source-owned molecular encodings
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction and any future normalization policy
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated structure owner
  acceptance_checks:
  - Reproduce the original D02228 molfile with and without conformers, preserving
    core 6R,7S, two sodium ions, charge, formula, masses and exact source snapshot.
  - Explain /b12-6- together with /t13? using documented InChI/toolkit semantics.
    A changed generated hash alone does not prove a different stereoisomer.
  - Any separately authorized source correction must propagate through maintained
    owners/reseeding and pass schema/strict, chemical identity and applicable corpus/history
    checks.
- action_id: A2
  description: Optionally add the 2021 exact-preparation activity with source-specific
    limits.
  finding_ids: []
  target_ids:
  - CHEBI:34617
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefotetan-disodium.yaml
    role: Curator-owned activity_spectrum and evidence via validated writer
  acceptance_checks:
  - Cite DOI 10.1128/spectrum.00226-21 at the activity object; retain Glentham GA5476,
    DMSO, CAMHB, digital BMD, inoculum and nonrandom 110 E. coli/40 K. pneumoniae
    isolate context.
  - Keep aggregate MIC50/MIC90 distinct from single-isolate MICs. Confirm historical
    lot identity and potency basis before asserting unqualified mass concentrations
    of pure anhydrous salt.
  - Preserve the paper’s 32 mg/L intermediate rule versus conflicting Results wording
    and resolve the ampC subgroup denominator before adding genotype-specific counts
    or mechanistic conclusions.
  - Do not infer clinical efficacy, exact protein binding or isolated enzyme hydrolysis
    from this susceptibility study. Run native validation and add an accurate curation
    event only under separate curation authorization.
limitations:
- Generic RDKit roundtrip key equality fails. The coordinate experiment identifies
  a reproducible normalization boundary but does not establish which coupled-stereochemistry
  representation should be canonical for future source harmonization.
- Independent Beilstein registry contents were not inspected through free access.
  Current supplier catalog mapping does not replace the historical assay-lot certificate
  or an explicit potency correction.
- The 2021 study is a nonrandom isolate-panel experiment, not a clinical-efficacy
  or purified-target experiment. Its Results wording at 32 mg/L and ampC subgroup
  counts contain bounded internal discrepancies.
- The additional 1982 source was inspected at abstract/landing-page level only; scanned
  methods and exact preparation remain unresolved. Literature discovery was bounded,
  not an exhaustive historical review.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 20 captured input hashes unchanged, preserving the original inspection captures.
  No native/source/status/history edits.
- Native schema/strict used the batch 024 environment. Chemistry used the existing
  batch 019 locked RDKit 2026.03.5 interpreter against batch 024 cwd; no new toolkit
  installation.
- Free public retrieval only. EPMC full XML for the 1982 paper returned 500; its accessible
  PMC landing text and abstract were retained only as a limited lead.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:34617
- https://rest.kegg.jp/get/D02228/mol
- https://doi.org/10.1128/spectrum.00226-21
- https://www.glentham.com/en/products/product/GA5476/
tags:
- cefotetan-disodium
- exact-salt
- inchi-normalization
- primary-activity
```
