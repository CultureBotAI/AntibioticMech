# Albomycin ε: consistent ferric identity and unresolved activity-form scope

- Review: 20261021T084623Z-albomycin-epsilon
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:38:14Z
- Finished UTC: 2026-10-21T08:46:23Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Exact ferric ε structure, parent and generated provenance are supported, with no demonstrated native corrective defect. Imported antibacterial roles remain source-asserted:2018 has a negative ε panel but its final product characterization is metal-free despite ferric depiction. Preserve that form limitation and do not infer universal inactivity or another congener’s mechanism. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole-record review of exact ferric albomycin ε.

Selection: Queue084; CHEBI:83217 in isolated batch009.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:83217 | data/antibiotics/antibacterial/albomycin-ε.yaml | generated | albomycin ε |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | CHEBI:83217 | Actual command passed. |
| Focused strict | passed | True | CHEBI:83217 | Actual command passed. |
| Independent structure consistency | passed | True | CHEBI:83217 | Both encodings regenerate exact native full key and chemistry. |
| Structured source applicability | not_applicable | False | CHEBI:83217 | No native named gene, protein, pathway, regulator, stress response or transcriptomic dataset. No module claim is inferred from family literature. |
| Authoritative full QC | failed | True | CHEBI:83217 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:83217 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:83217 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:83217 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:83217 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:83217 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:83217 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:83217 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:83217 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact ferric ε congener

identity: supported. Targets: CHEBI:83217.

Native identity and all structure fields agree across ChEBI, independent PubChem and GSRS and chemistry calculations.

### Broader parent

grounding: supported. Targets: CHEBI:83217.

Iron(III) hydroxamate is chemically appropriate and strictly broader.

### Imported antibacterial/antimicrobial roles

evidence: unknown. Targets: CHEBI:83217.

Roles reproduce current ChEBI, but primary confirmation of exact ferric ε activity is unresolved.2018 reports a negative ε panel with a metal-free-versus-ferric preparation discrepancy; this does not prove the native role universally false or justify silent deletion.

### Negative panel and stability

scope: supported. Targets: CHEBI:83217.

The inspected source supports bounded inactivity of its tested1c preparation and instability in D2O. Quantitative data and any degradation interpretation must retain method, organism and preparation.

### Congener and active-fragment boundaries

evidence: unknown. Targets: CHEBI:83217.

No native mechanism is asserted. δ2 fragment inhibition and δ1 core binding cannot be transferred to ε without direct evidence.

### Missing exact MIBiG match

provenance: supported. Targets: CHEBI:83217.

No erroneous producer is native. The adopted MIBiG ε row is stereochemically unspecified and is correctly excluded by the exact-key policy.

### Clinical and resistance assertions

scope: not_applicable. Targets: CHEBI:83217.

No clinical approval, efficacy, resistance determinant or dataset claim is native. Family history or another congener cannot supply such exact ε assertions.

### Evidence disposition

completeness: unknown. Targets: CHEBI:83217.

A curator should adjudicate the exact ferric activity role against the negative study and original material definitions. Optional blank fields alone are not defects; no proven native corrective error follows from the unresolved source-form boundary.

### Source ownership and history

provenance: supported. Targets: CHEBI:83217.

Raw source, mint and all three seed/reseed events agree; native SEEDED status is unchanged.

### Focused validation

schema: supported. Targets: CHEBI:83217.

Schema, strict and independent chemistry checks pass.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/albomycin-ε.yaml; Entire YAML | supports | Read exact ε label, ferric hydroxamate definition, three synonyms, parent, two imported activity roles, all chemical fields, source/mint and three history events. No native quantitative assay, target, mechanism, producer, clinical, resistance, dataset or graph assertion; no native chemical xrefs. |
| owner | data/raw/chebi_antimicrobials.tsv; Row2201; PATHS2443; source configuration and seeder | supports | Raw row repeats exact identity and roles and has no PMID lead. MIBiG raw row1054 has no specified stereochemistry and key VQCJCCMAGPCDIK-UHFFFAOYSA-N, so exact-key/stereo-completeness seeding correctly does not attach that producer assertion. Both relevant raw inputs and extractor ownership were captured before assessment. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:83217; Current complete entry | supports | Official source agrees with native exact ferric ε name, both encodings, C36H56FeN11O17S, neutral total charge, masses, synonyms, parent and antibacterial/antimicrobial roles. Roles remain database assertions; this page supplies no compound-specific assay citation. |
| chemistry | Independent RDKit calculations; Native SMILES and InChI | supports | Both yield VQCJCCMAGPCDIK-DFBZBFILSA-N, C36H56FeN11O17S, charge0, mass1002.816, exact1002.292572832 and10 specified tetrahedral centres. Metal disconnection and ligand tautomer normalization in Standard InChI do not create a mismatch. Mint antibioticmech:chebi-2a0900c7f4 reproduces. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/90478363; Exact full-key PUG lookup | supports | CID90478363 matches native full InChI/key, formula, charge and compatible masses. |
| gsrs | https://gsrs.ncats.nih.gov/api/v1/substances/2FI7OQF5OS?view=full; Full chemical record and registry codes | supports | Official ε chemical UNII2FI7OQF5OS gives the exact native InChI/key, corresponding stereochemical structure, CAS12676-10-7 and PubChem90478363. The latter identifiers are additional exact-form leads, not already native xrefs. |
| parent | https://www.ebi.ac.uk/chebi/CHEBI:28163; Official parent definition | supports | Iron(III) hydroxamate is a broader complex class consistent with the ferric component and three hydroxamate groups. |
| negative-panel | PMID:30181560; DOI10.1038/s41467-018-05821-1; Table1 and Methods | partial | Synthetic ε1c has MIC&gt;512µg/mL against the six tested organisms: S.pneumoniae ATCC49619,S.aureus USA300 NRS384,B.subtilis ATCC6633,E.coli BJ5183,N.gonorrhoeae ATCC49226 and the reported S.typhi. Gonococcus used agar dilution; other tests used broth, with horse blood/CO2 for pneumococcus. This is a bounded negative panel, not universal inactivity of every ε preparation. |
| form | https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-018-05821-1/MediaObjects/41467_2018_5821_MOESM1_ESM.pdf; Physical p79, compound1c; main Fig1 visually inspected | context_only | The final synthesis gives metal-free ligand HRMS C36H59N11NaO17S+ [M+Na]+972.3703 and no iron-addition step. Main Fig1 depicts ferric1c. Exact ferric dosing-form equivalence is therefore unresolved, and negative quantitative transfer needs qualification. |
| stability | PMID:30181560; Final synthesis Results paragraph | context_only | Authors report ε slowly converts to δ1 in D2O, unlike the more stable δ2. This source observation limits interpretation of aged preparations but supplies no quantitative degradation rate or proof that every antibacterial test contained δ1. |
| biosynthetic-context | PMID:22704654; DOI10.1021/cb300173x; full article, introduction and abmE/abmI results | context_only | The introduction describes ε as a less potent minor congener lacking the carbamoyl group. The actual genetic/mass experiments predominantly establish δ2, δ1 shunt product and descarbamoyl-desmethyl analog. They do not provide an isolated ε dose-response that resolves the2018 negative panel or an ε-specific direct target. |
| mibig-boundary | https://mibig.secondarymetabolites.org/repository/BGC0002300.2/annotations.json; Version2 ε compound structure and empty compound evidence | context_only | The ε listing lacks specified stereochemistry; locus knock-out evidence is not independently attached to the compound. Native absence of a producer entry avoids upgrading this non-exact source row. |
| other-targets | PMID:11217799; DOI10.7164/antibiotics.53.1346; original paper | context_only | Potent SerRS inhibition concerns SB-217452, a δ2-derived seryl nucleoside. Ferric/aluminium δ2 complexes are distinct preparations. Neither those enzyme results nor the2020 δ1-core study establishes ε target engagement. |
| historical | https://onlinelibrary.wiley.com/doi/10.1002/anie.198205271; 1982 publisher metadata and referenced complete-manuscript DOI | context_only | The primary communication resolves to Constitution of the Deferriform of the Albomycins δ1,δ2 and ε, with full manuscript DOI10.1002/anie.198213220. Full experiment text was inaccessible; metadata does not establish exact ferric ε antimicrobial potency. |
| gates | just validate; just validate-strict; Actual focused commands in batch009 | supports | Both exit0; one record and zero strict ERROR rows. |
| search | CultureBotAI/AntibioticMech; Ignored-inclusive source and literature search | context_only | Exact native/raw/PATHS/configuration and maintained curation surfaces were checked with ignored files included. Additional free searches followed ε/epsilon, exact full key and the1982/2018 primary citations. Vendor extrapolations and family-level target claims were not treated as evidence. |

## Limits And Additional Notes

- Exact ferric ε positive activity was not independently verified in the bounded search. ChEBI roles are retained source assertions, not newly proven quantitative effects.
- 2018 source depicts ferric compounds but characterizes final synthetic products by desferri formulas and no iron-addition step. Its negative panel cannot be silently generalized across preparation states.
- ε instability in D2O does not determine the composition or causal reason for inactivity in every assay.
- The complete1982 manuscript was inaccessible; historical mixture and congener claims cannot replace exact ε evidence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All22 captured input hashes rechecked unchanged; no native record, history or status edits.
- Concrete follow-up: resolve the2018 dosing preparation and historical ferric ε assays, then retain, qualify or remove activity roles through maintained source/curation ownership based on exact-form evidence. Do not automatically remove roles solely from this bounded negative panel.
- A future activity_spectrum observation must preserve the &gt;512µg/mL inequality, exact tested organisms, assay method and preparation uncertainty. No clinical breakpoint or mechanism is supplied by that result.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T084623Z-albomycin-epsilon
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Albomycin ε: consistent ferric identity and unresolved activity-form scope'
started_at: '2026-10-21T08:38:14Z'
finished_at: '2026-10-21T08:46:23Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independently read whole native record, source owners and current
    authorities; inspected primary negative panel, preparation supplement and congener
    context.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: Exact ferric ε structure, parent and generated provenance are supported,
  with no demonstrated native corrective defect. Imported antibacterial roles remain
  source-asserted:2018 has a negative ε panel but its final product characterization
  is metal-free despite ferric depiction. Preserve that form limitation and do not
  infer universal inactivity or another congener’s mechanism. Scientific assessment
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
  - path: data/antibiotics/antibacterial/albomycin-ε.yaml
    sha256: 6b79d47a7b76b88f6a763290fda2c869cd1965cf393c017fb65ea55cd2b55d64
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
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
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
  - path: data/raw/mibig_producers.tsv
    sha256: d55289619e77e035ed437d432dd692ab382f254c3841c9a314752ef22578a01b
    role: context
  - path: scripts/extract_mibig_producers.py
    sha256: a078cdf4c9b2d09999800ab7ae03f93d3972f29b7d2f460ebbbe7d7ec6b31c53
    role: context
targets:
- target_id: CHEBI:83217
  path: data/antibiotics/antibacterial/albomycin-ε.yaml
  label: albomycin ε
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
  description: Whole-record review of exact ferric albomycin ε.
  selection: Queue084; CHEBI:83217 in isolated batch009.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:83217
  exclusions:
  - target: Albomycin mixture,δ1,δ2,desferri ε and separated nucleoside cores
    reason: Distinct entities or preparation states; comparator context only.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual command passed.
  target_ids:
  - CHEBI:83217
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/albomycin-ε.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: strict
  name: Focused strict
  status: passed
  required: true
  summary: Actual command passed.
  target_ids:
  - CHEBI:83217
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/albomycin-ε.yaml --out /private/tmp/am-review-session/084-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Independent structure consistency
  status: passed
  required: true
  summary: Both encodings regenerate exact native full key and chemistry.
  target_ids:
  - CHEBI:83217
  evidence_ids:
  - chemistry
  - pubchem
  - gsrs
- check_id: adapter
  name: Structured source applicability
  status: not_applicable
  required: false
  summary: No native named gene, protein, pathway, regulator, stress response or transcriptomic
    dataset. No module claim is inferred from family literature.
  target_ids:
  - CHEBI:83217
  evidence_ids:
  - native
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:83217
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
  - CHEBI:83217
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
  - CHEBI:83217
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
  - CHEBI:83217
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
  - CHEBI:83217
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
  - CHEBI:83217
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
  - CHEBI:83217
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
  - CHEBI:83217
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
  - CHEBI:83217
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/albomycin-ε.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T08:41:20Z'
  support: supports
  summary: Read exact ε label, ferric hydroxamate definition, three synonyms, parent,
    two imported activity roles, all chemical fields, source/mint and three history
    events. No native quantitative assay, target, mechanism, producer, clinical, resistance,
    dataset or graph assertion; no native chemical xrefs.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Row2201; PATHS2443; source configuration and seeder
  accessed_at: '2026-10-21T08:41:20Z'
  support: supports
  summary: Raw row repeats exact identity and roles and has no PMID lead. MIBiG raw
    row1054 has no specified stereochemistry and key VQCJCCMAGPCDIK-UHFFFAOYSA-N,
    so exact-key/stereo-completeness seeding correctly does not attach that producer
    assertion. Both relevant raw inputs and extractor ownership were captured before
    assessment.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:83217
  locator: Current complete entry
  accessed_at: '2026-10-21T08:39:01Z'
  support: supports
  summary: Official source agrees with native exact ferric ε name, both encodings,
    C36H56FeN11O17S, neutral total charge, masses, synonyms, parent and antibacterial/antimicrobial
    roles. Roles remain database assertions; this page supplies no compound-specific
    assay citation.
  snapshot_sha256: 973fa30ee5e921b2af5a526c5eef7df1ceade96379029b37dd51d8b7a2aeb3e3
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit calculations
  locator: Native SMILES and InChI
  accessed_at: '2026-10-21T08:38:43Z'
  support: supports
  summary: Both yield VQCJCCMAGPCDIK-DFBZBFILSA-N, C36H56FeN11O17S, charge0, mass1002.816,
    exact1002.292572832 and10 specified tetrahedral centres. Metal disconnection and
    ligand tautomer normalization in Standard InChI do not create a mismatch. Mint
    antibioticmech:chebi-2a0900c7f4 reproduces.
  snapshot_sha256: 6813885bb7c35a9a03692512b355ba3173a231d750cb7c936220a6caaf2d87cd
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/90478363
  locator: Exact full-key PUG lookup
  accessed_at: '2026-10-21T08:38:53Z'
  support: supports
  summary: CID90478363 matches native full InChI/key, formula, charge and compatible
    masses.
  snapshot_sha256: 01846a2c4a020c7d7eaee38355ace0aa4754d2c357ffe9670097a849ac1e0484
- evidence_id: gsrs
  kind: authority
  reference: https://gsrs.ncats.nih.gov/api/v1/substances/2FI7OQF5OS?view=full
  locator: Full chemical record and registry codes
  accessed_at: '2026-10-21T08:38:53Z'
  support: supports
  summary: Official ε chemical UNII2FI7OQF5OS gives the exact native InChI/key, corresponding
    stereochemical structure, CAS12676-10-7 and PubChem90478363. The latter identifiers
    are additional exact-form leads, not already native xrefs.
  snapshot_sha256: 2293e4b8fa1c420b1c12e6e36b6e80a0ebaf7a7fe9dc9e9297a0638497f71ccf
- evidence_id: parent
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:28163
  locator: Official parent definition
  accessed_at: '2026-10-21T08:36:05Z'
  support: supports
  summary: Iron(III) hydroxamate is a broader complex class consistent with the ferric
    component and three hydroxamate groups.
  snapshot_sha256: 6ae5e3a7597818a1c82d3a13271aae5f80de2f66ddd4eff0972c7e81b5650569
- evidence_id: negative-panel
  kind: primary_source
  reference: PMID:30181560
  locator: DOI10.1038/s41467-018-05821-1; Table1 and Methods
  accessed_at: '2026-10-21T08:31:45Z'
  support: partial
  summary: 'Synthetic ε1c has MIC>512µg/mL against the six tested organisms: S.pneumoniae
    ATCC49619,S.aureus USA300 NRS384,B.subtilis ATCC6633,E.coli BJ5183,N.gonorrhoeae
    ATCC49226 and the reported S.typhi. Gonococcus used agar dilution; other tests
    used broth, with horse blood/CO2 for pneumococcus. This is a bounded negative
    panel, not universal inactivity of every ε preparation.'
  snapshot_sha256: 50678e14b6879bb3ad925a4909c0faf91463e2375a08a9f44c6680b410ee5275
- evidence_id: form
  kind: primary_source
  reference: https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-018-05821-1/MediaObjects/41467_2018_5821_MOESM1_ESM.pdf
  locator: Physical p79, compound1c; main Fig1 visually inspected
  accessed_at: '2026-10-21T08:32:40Z'
  support: context_only
  summary: The final synthesis gives metal-free ligand HRMS C36H59N11NaO17S+ [M+Na]+972.3703
    and no iron-addition step. Main Fig1 depicts ferric1c. Exact ferric dosing-form
    equivalence is therefore unresolved, and negative quantitative transfer needs
    qualification.
  snapshot_sha256: 3bb3d6d04dc26f64143b263f4fedab624228abe42fe3035746b8873b7ce425cd
- evidence_id: stability
  kind: primary_source
  reference: PMID:30181560
  locator: Final synthesis Results paragraph
  accessed_at: '2026-10-21T08:31:45Z'
  support: context_only
  summary: Authors report ε slowly converts to δ1 in D2O, unlike the more stable δ2.
    This source observation limits interpretation of aged preparations but supplies
    no quantitative degradation rate or proof that every antibacterial test contained
    δ1.
  snapshot_sha256: 50678e14b6879bb3ad925a4909c0faf91463e2375a08a9f44c6680b410ee5275
- evidence_id: biosynthetic-context
  kind: primary_source
  reference: PMID:22704654
  locator: DOI10.1021/cb300173x; full article, introduction and abmE/abmI results
  accessed_at: '2026-10-21T08:32:29Z'
  support: context_only
  summary: The introduction describes ε as a less potent minor congener lacking the
    carbamoyl group. The actual genetic/mass experiments predominantly establish δ2,
    δ1 shunt product and descarbamoyl-desmethyl analog. They do not provide an isolated
    ε dose-response that resolves the2018 negative panel or an ε-specific direct target.
  snapshot_sha256: 6ed17c1e1064f1bc2fdad38fbf7ae408db30be626307f97801a0ae780da0a49c
- evidence_id: mibig-boundary
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0002300.2/annotations.json
  locator: Version2 ε compound structure and empty compound evidence
  accessed_at: '2026-10-21T08:33:44Z'
  support: context_only
  summary: The ε listing lacks specified stereochemistry; locus knock-out evidence
    is not independently attached to the compound. Native absence of a producer entry
    avoids upgrading this non-exact source row.
  snapshot_sha256: 0597f1ddaf9166fe2df27080d0a3b6db0991e3e66fa7ac8b9f581998dd3bd1a3
- evidence_id: other-targets
  kind: primary_source
  reference: PMID:11217799
  locator: DOI10.7164/antibiotics.53.1346; original paper
  accessed_at: '2026-10-21T08:36:23Z'
  support: context_only
  summary: Potent SerRS inhibition concerns SB-217452, a δ2-derived seryl nucleoside.
    Ferric/aluminium δ2 complexes are distinct preparations. Neither those enzyme
    results nor the2020 δ1-core study establishes ε target engagement.
  snapshot_sha256: 5a2d4ea9e93acdbbe981b635ad744a60a192cfa2ec9a47e6f520bdb5abcc6c22
- evidence_id: historical
  kind: primary_source
  reference: https://onlinelibrary.wiley.com/doi/10.1002/anie.198205271
  locator: 1982 publisher metadata and referenced complete-manuscript DOI
  accessed_at: '2026-10-21T08:41:20Z'
  support: context_only
  summary: The primary communication resolves to Constitution of the Deferriform of
    the Albomycins δ1,δ2 and ε, with full manuscript DOI10.1002/anie.198213220. Full
    experiment text was inaccessible; metadata does not establish exact ferric ε antimicrobial
    potency.
- evidence_id: gates
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual focused commands in batch009
  accessed_at: '2026-10-21T08:38:49Z'
  support: supports
  summary: Both exit0; one record and zero strict ERROR rows.
  snapshot_sha256: 9562819f72443a38a2cfbf48f82b99bad9eca302ef69103a715fa91f5d427961
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: Ignored-inclusive source and literature search
  accessed_at: '2026-10-21T08:41:20Z'
  support: context_only
  summary: Exact native/raw/PATHS/configuration and maintained curation surfaces were
    checked with ignored files included. Additional free searches followed ε/epsilon,
    exact full key and the1982/2018 primary citations. Vendor extrapolations and family-level
    target claims were not treated as evidence.
  search_scope: prepare.py84 used rg --no-ignore --hidden for ID,label,slug across
    batch009 excluding.git/.venv; full-key/raw follow-up. Primary2018 text/supplement/figure
    and2012/2000 texts inspected;1982 complete manuscript inaccessible. No exact ferric
    ε positive quantitative experiment was verified within this bounded search.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact ferric ε congener
  outcome: supported
  summary: Native identity and all structure fields agree across ChEBI, independent
    PubChem and GSRS and chemistry calculations.
  target_ids:
  - CHEBI:83217
  evidence_ids:
  - native
  - chebi
  - chemistry
  - pubchem
  - gsrs
- assessment_id: parentage
  area: grounding
  topic: Broader parent
  outcome: supported
  summary: Iron(III) hydroxamate is chemically appropriate and strictly broader.
  target_ids:
  - CHEBI:83217
  evidence_ids:
  - parent
  - chemistry
- assessment_id: roles
  area: evidence
  topic: Imported antibacterial/antimicrobial roles
  outcome: unknown
  summary: Roles reproduce current ChEBI, but primary confirmation of exact ferric
    ε activity is unresolved.2018 reports a negative ε panel with a metal-free-versus-ferric
    preparation discrepancy; this does not prove the native role universally false
    or justify silent deletion.
  target_ids:
  - CHEBI:83217
  evidence_ids:
  - chebi
  - negative-panel
  - form
  - biosynthetic-context
- assessment_id: activity
  area: scope
  topic: Negative panel and stability
  outcome: supported
  summary: The inspected source supports bounded inactivity of its tested1c preparation
    and instability in D2O. Quantitative data and any degradation interpretation must
    retain method, organism and preparation.
  target_ids:
  - CHEBI:83217
  evidence_ids:
  - negative-panel
  - form
  - stability
- assessment_id: mechanism
  area: evidence
  topic: Congener and active-fragment boundaries
  outcome: unknown
  summary: No native mechanism is asserted. δ2 fragment inhibition and δ1 core binding
    cannot be transferred to ε without direct evidence.
  target_ids:
  - CHEBI:83217
  evidence_ids:
  - native
  - other-targets
  - biosynthetic-context
- assessment_id: producer
  area: provenance
  topic: Missing exact MIBiG match
  outcome: supported
  summary: No erroneous producer is native. The adopted MIBiG ε row is stereochemically
    unspecified and is correctly excluded by the exact-key policy.
  target_ids:
  - CHEBI:83217
  evidence_ids:
  - owner
  - mibig-boundary
- assessment_id: clinical
  area: scope
  topic: Clinical and resistance assertions
  outcome: not_applicable
  summary: No clinical approval, efficacy, resistance determinant or dataset claim
    is native. Family history or another congener cannot supply such exact ε assertions.
  target_ids:
  - CHEBI:83217
  evidence_ids:
  - native
  - negative-panel
  - other-targets
- assessment_id: completeness
  area: completeness
  topic: Evidence disposition
  outcome: unknown
  summary: A curator should adjudicate the exact ferric activity role against the
    negative study and original material definitions. Optional blank fields alone
    are not defects; no proven native corrective error follows from the unresolved
    source-form boundary.
  target_ids:
  - CHEBI:83217
  evidence_ids:
  - chebi
  - negative-panel
  - form
  - historical
  - search
- assessment_id: history
  area: provenance
  topic: Source ownership and history
  outcome: supported
  summary: Raw source, mint and all three seed/reseed events agree; native SEEDED
    status is unchanged.
  target_ids:
  - CHEBI:83217
  evidence_ids:
  - native
  - owner
  - chemistry
- assessment_id: schema
  area: schema
  topic: Focused validation
  outcome: supported
  summary: Schema, strict and independent chemistry checks pass.
  target_ids:
  - CHEBI:83217
  evidence_ids:
  - gates
  - chemistry
findings: []
actions: []
limitations:
- Exact ferric ε positive activity was not independently verified in the bounded search.
  ChEBI roles are retained source assertions, not newly proven quantitative effects.
- 2018 source depicts ferric compounds but characterizes final synthetic products
  by desferri formulas and no iron-addition step. Its negative panel cannot be silently
  generalized across preparation states.
- ε instability in D2O does not determine the composition or causal reason for inactivity
  in every assay.
- The complete1982 manuscript was inaccessible; historical mixture and congener claims
  cannot replace exact ε evidence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All22 captured input hashes rechecked unchanged; no native record, history or status
  edits.
- 'Concrete follow-up: resolve the2018 dosing preparation and historical ferric ε
  assays, then retain, qualify or remove activity roles through maintained source/curation
  ownership based on exact-form evidence. Do not automatically remove roles solely
  from this bounded negative panel.'
- A future activity_spectrum observation must preserve the >512µg/mL inequality, exact
  tested organisms, assay method and preparation uncertainty. No clinical breakpoint
  or mechanism is supplied by that result.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:83217
- https://gsrs.ncats.nih.gov/api/v1/substances/2FI7OQF5OS?view=full
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6123416/
tags:
- antibacterial
- ferric-complex
- negative-assay
- exact-congener
- source-form-limit
```
