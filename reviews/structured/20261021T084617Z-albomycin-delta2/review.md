# Albomycin δ2: missing SMILES imine geometry and active-fragment scope

- Review: 20261021T084617Z-albomycin-delta2
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:35:27Z
- Finished UTC: 2026-10-21T08:46:17Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Ferric δ2 identity, parent and antibacterial classification are supported. One major internal defect: native SMILES omits imine geometry specified in retained InChI/key. Primary evidence distinguishes intact ferric/aluminium complexes from the potent cleaved SerRS inhibitor;2018 quantitative transfer remains form-qualified.

## Scope And Provenance

Whole-record review of exact ferric albomycin δ2.

Selection: Queue083; CHEBI:83215 in isolated batch009.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:83215 | data/antibiotics/antibacterial/albomycin-δ2.yaml | generated | albomycin δ2 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | CHEBI:83215 | Actual command passed. |
| Focused strict | passed | True | CHEBI:83215 | Actual command passed. |
| Independent structure consistency | failed | True | CHEBI:83215 | SMILES regenerated full key differs only at missing imine geometry from retained InChI/key. |
| Structured source applicability | not_applicable | False | CHEBI:83215 | No native named gene, protein, pathway, regulator, stress-response or dataset. No expression-module evidence is used to establish the source-discovered SerRS mechanism. |
| Authoritative full QC | failed | True | CHEBI:83215 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:83215 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:83215 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:83215 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:83215 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:83215 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:83215 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:83215 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:83215 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Ferric δ2 entity

identity: supported. Targets: CHEBI:83215.

Label, ferric definition, formula, mass, charge and retained InChI/key identify the exact congener across independent authorities.

### Inconsistent imine stereochemistry

consistency: concern. Targets: CHEBI:83215.

Native SMILES omits a geometric configuration specified in native InChI/key. Exact scratch repair demonstrates the discrepancy independently.

### Broader parent and antibacterial roles

grounding: supported. Targets: CHEBI:83215.

Parent is broader and the2000 isolated ferric δ2 has direct antibacterial fraction-tracking evidence.

### Prodrug versus active SerRS inhibitor

evidence: supported. Targets: CHEBI:83215.

Inspected primary source distinguishes ferric intact drug from potent SB-217452 inhibition and proposes cleavage after transport. No native direct target claim is present; future annotations must preserve this distinction.

### Quantitative assay form

evidence: unknown. Targets: CHEBI:83215.

2018 tables give useful strain/medium-qualified observations, but final ligand characterization versus ferric main drawing requires adjudication before exact ferric MIC attachment.

### Producer evidence and MIBiG exclusion

provenance: supported. Targets: CHEBI:83215.

Two adopted primary sources support ATCC700974 production. Native producer absence is understandable from the raw MIBiG form mismatch and is not a bad producer assertion. Any future annotation belongs in the actual native record via validated writer/history.

### Mechanism and clinical context boundaries

scope: unknown. Targets: CHEBI:83215.

Biosynthetic self-protection and study-specific MICs do not establish universal resistance determinants, clinical breakpoints or approved δ2 therapy; no such claims are native.

### Optional annotations and exact source disposition

completeness: unknown. Targets: CHEBI:83215.

Specific primary activity, producer and active-fragment evidence can be curated after structural/form adjudication. Blank optional slots alone are not the finding.

### Generated ownership and history

provenance: supported. Targets: CHEBI:83215.

Raw source, mint and three events agree. The imported source also carries the geometry omission; status remains SEEDED.

### Focused validators

schema: supported. Targets: CHEBI:83215.

Schema and strict gates pass; independent chemistry reports a separate material defect.

## Findings

### F1: Make the SMILES specify the imine geometry retained in InChI

major / open / confirmed; issue key: chebi-83215-smiles-imine-stereo-omission.

Native SMILES produces full key RQZRKFJHRUDTLB-DFBZBFILSA-N, while native InChI and stored key specify RQZRKFJHRUDTLB-IDJYBIRTSA-N. The missing carbamoylimino C=N geometry is inherited from ChEBI/raw. GSRS and a scratch-only stereo completion independently reproduce the retained exact structure.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate and correct the imported SMILES imine geometry against the independently verified retained exact InChI/key.

- Both final encodings regenerate RQZRKFJHRUDTLB-IDJYBIRTSA-N including /b43-24+; do not erase geometry from the InChI to manufacture agreement.
- Preserve all10 tetrahedral centres, ferric-complex stoichiometry, formula and charge. Scratch083-stereo-repair-check.json supplies a tested candidate but is not a native edit.
- Apply the maintained source correction and run chemistry consistency, schema, strict, source reproduction and history gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/albomycin-δ2.yaml; Entire YAML | supports | Read exact δ2 label, ferric-hydroxamate definition, three synonyms, parent, roles, all chemical fields, source/mint and three history events. No native xrefs, quantitative assay, producer, molecular target, resistance, clinical or graph claim. |
| owner | data/raw/chebi_antimicrobials.tsv; Row2200; PATHS2442; extractor/seeder | supports | Imported row repeats native encodings and supplies PMID11217799 and22704654. Maintained ChEBI raw/extractor/seeder owns the structural correction. MIBiG row1052 has different neutral-ligand-plus-Fe key XEGJEKIQLBLKHJ-IDJYBIRTSA-N, so exact-key-only seeder does not attach it to this ferric record; that omission is not an invalid native producer claim. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:83215; Full current entry | partial | Current ChEBI matches native label, ferric definition, formula, masses, parent and roles, but repeats the internal SMILES/InChI geometry inconsistency. The retained InChI contains /b43-24+ while SMILES lacks corresponding bond stereo. |
| parent | https://www.ebi.ac.uk/chebi/CHEBI:28163; Official definition | supports | Iron(III) hydroxamate is a broader structural class; the native ligand and ferric component satisfy it. |
| chemistry | Independent RDKit calculations; Native SMILES versus native InChI | refutes | SMILES generates RQZRKFJHRUDTLB-DFBZBFILSA-N; InChI regenerates stored RQZRKFJHRUDTLB-IDJYBIRTSA-N. Difference is the exocyclic carbamoylimino C=N geometry, not metal disconnection or tetrahedral configuration. Both match C37H57FeN12O18S, charge0, mass1045.841, exact1045.298386484 and10 tetrahedral centres. |
| repair-check | Independent scratch-only repair calculation; GSRS SMILES and native candidate with only imine bond stereo supplied | supports | Official GSRS stereo-encoded SMILES regenerates stored full InChI/key. A scratch candidate adding the corresponding slash/backslash geometry to native SMILES also regenerates the exact retained InChI/key without changing connectivity, formula, charge or tetrahedral centres. No native edit occurred. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/90479121; Exact full-key lookup | supports | CID90479121 matches the retained specified-geometry InChI/key and compatible formula/charge/masses. |
| gsrs | https://gsrs.ncats.nih.gov/api/v1/substances/H76824799X?view=full; Full chemical record, structure and codes | supports | Official δ2 record has the retained exact InChI/key and a SMILES that specifies the missing imine geometry. CAS34755-52-7 and PubChem90479121 are additional exact-form leads, not already native xrefs. |
| primary2000 | PMID:11217799; DOI10.7164/antibiotics.53.1346; original pp1346–1353 | supports | ATCC700974 fermentation yielded ferric metaboliteA and aluminium metaboliteB, separated chromatographically. Mass before/after acidification and X-ray energy spectroscopy distinguish metals. Ferric δ2 was tracked using E.coli ESS agar activity. Isolated SB-217452, the seryl nucleoside, inhibits S.aureus/rat SerRS near8nM; intact complexes had no such inhibition. Aminoacylation used crude enzyme and radiolabeled serine. The proposed intracellular cleavage mechanism must distinguish parent from active fragment. |
| primary2012 | PMID:22704654; DOI10.1021/cb300173x; complete primary body, genetic and purification sections | supports | ATCC700974 produces δ2; gene deletion/complementation supports the abm cluster. Purification and shunt-product experiments distinguish δ2 from δ1 and descarbamoyl-desmethyl analogs. Detailed pathway arrows include author hypotheses, not all directly demonstrated transformations. This is producer/biosynthetic context, not direct δ2 binding to every biosynthetic enzyme. |
| assay2018 | PMID:30181560; DOI10.1038/s41467-018-05821-1; Tables1–3 and Methods | partial | Synthetic1b has strain-resolved activity, including S.aureus USA300 NRS384 MIC0.125µg/mL and S.pneumoniae ATCC49619 MIC0.0625µg/mL in the reported media. Iron-depleted medium changes selected pneumococcal responses. These are study-specific observations, not established clinical breakpoints, and the exact dosing-form qualification in the supplement applies. |
| form2018 | https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-018-05821-1/MediaObjects/41467_2018_5821_MOESM1_ESM.pdf; Physical p79, compound1b; main Fig1 inspected separately | context_only | Synthetic1b final characterization gives metal-free ligand HRMS C37H60N12NaO18S+ [M+Na]+1015.3761 and no iron-addition step. Main Fig1 depicts ferric albomycin. Preserve this discrepancy before transferring exact ferric MICs; ambient medium iron alone does not identify the preparation. |
| gates | just validate; just validate-strict; Actual focused commands | supports | Both exit0; one record and zero strict ERROR rows. Deterministic gates did not catch the chemical stereo mismatch. |
| search | CultureBotAI/AntibioticMech; Ignored-inclusive local search and free primary discovery | context_only | Exact ID,label,slug and raw/PATHS/configuration were searched including ignored files. The primary2000 PDF and2012 full text were read;2018 main text, relevant supplement and ferric figure were inspected. No family or fragment assay was silently transferred to intact ferric δ2. |

## Limits And Additional Notes

- Independent chemistry failed because SMILES lacks imine geometry; schema/strict success does not resolve that defect.
- 2018 synthetic final products have desferri HRMS formulas despite ferric drawings. Exact ferric assay transfer requires material adjudication.
- The2000 paper reports intact-complex non-inhibition without a detailed numerical complex IC50 ceiling; do not invent one.
- No full-corpus inference of missing evidence follows from this bounded one-record search.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All22 captured input hashes rechecked unchanged; no native record or status edits.
- Concrete future curation: producer and active-fragment mode may be annotated with exact primary evidence and validated history after the structural defect is resolved. Transport proteins and biosynthetic enzymes must not be mislabeled as direct antibiotic targets.
- The structure repair is demonstrated only in scratch; the source retains an independently verifiable intended geometric isomer.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T084617Z-albomycin-delta2
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Albomycin δ2: missing SMILES imine geometry and active-fragment scope'
started_at: '2026-10-21T08:35:27Z'
finished_at: '2026-10-21T08:46:17Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independently read the entire native record, raw owners, current
    authorities and primary papers; chemistry calculations used retained encodings
    and official independent structure.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'Ferric δ2 identity, parent and antibacterial classification are supported.
  One major internal defect: native SMILES omits imine geometry specified in retained
  InChI/key. Primary evidence distinguishes intact ferric/aluminium complexes from
  the potent cleaved SerRS inhibitor;2018 quantitative transfer remains form-qualified.'
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
  - path: data/antibiotics/antibacterial/albomycin-δ2.yaml
    sha256: d069099c4b398ae761d7927d60f5accd55eed2286c6da8a905b51ccb70be2d6e
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
- target_id: CHEBI:83215
  path: data/antibiotics/antibacterial/albomycin-δ2.yaml
  label: albomycin δ2
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
  description: Whole-record review of exact ferric albomycin δ2.
  selection: Queue083; CHEBI:83215 in isolated batch009.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:83215
  exclusions:
  - target: Albomycin mixture,δ1,ε,desferri ligand,aluminium complex andSB-217452
    reason: Separate forms/congeners or active fragment; results retain exact preparation
      scope.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual command passed.
  target_ids:
  - CHEBI:83215
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/albomycin-δ2.yaml
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
  - CHEBI:83215
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/albomycin-δ2.yaml --out /private/tmp/am-review-session/083-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Independent structure consistency
  status: failed
  required: true
  summary: SMILES regenerated full key differs only at missing imine geometry from
    retained InChI/key.
  target_ids:
  - CHEBI:83215
  evidence_ids:
  - chemistry
  - repair-check
- check_id: adapter
  name: Structured source applicability
  status: not_applicable
  required: false
  summary: No native named gene, protein, pathway, regulator, stress-response or dataset.
    No expression-module evidence is used to establish the source-discovered SerRS
    mechanism.
  target_ids:
  - CHEBI:83215
  evidence_ids:
  - native
  - primary2000
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:83215
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
  - CHEBI:83215
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
  - CHEBI:83215
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
  - CHEBI:83215
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
  - CHEBI:83215
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
  - CHEBI:83215
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
  - CHEBI:83215
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
  - CHEBI:83215
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
  - CHEBI:83215
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/albomycin-δ2.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T08:37:51Z'
  support: supports
  summary: Read exact δ2 label, ferric-hydroxamate definition, three synonyms, parent,
    roles, all chemical fields, source/mint and three history events. No native xrefs,
    quantitative assay, producer, molecular target, resistance, clinical or graph
    claim.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Row2200; PATHS2442; extractor/seeder
  accessed_at: '2026-10-21T08:37:51Z'
  support: supports
  summary: Imported row repeats native encodings and supplies PMID11217799 and22704654.
    Maintained ChEBI raw/extractor/seeder owns the structural correction. MIBiG row1052
    has different neutral-ligand-plus-Fe key XEGJEKIQLBLKHJ-IDJYBIRTSA-N, so exact-key-only
    seeder does not attach it to this ferric record; that omission is not an invalid
    native producer claim.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:83215
  locator: Full current entry
  accessed_at: '2026-10-21T08:36:05Z'
  support: partial
  summary: Current ChEBI matches native label, ferric definition, formula, masses,
    parent and roles, but repeats the internal SMILES/InChI geometry inconsistency.
    The retained InChI contains /b43-24+ while SMILES lacks corresponding bond stereo.
  snapshot_sha256: ff32075f9e5596c27bbcdadd40131cc6db22a999341945835130a610bc74d447
- evidence_id: parent
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:28163
  locator: Official definition
  accessed_at: '2026-10-21T08:36:05Z'
  support: supports
  summary: Iron(III) hydroxamate is a broader structural class; the native ligand
    and ferric component satisfy it.
  snapshot_sha256: 6ae5e3a7597818a1c82d3a13271aae5f80de2f66ddd4eff0972c7e81b5650569
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit calculations
  locator: Native SMILES versus native InChI
  accessed_at: '2026-10-21T08:35:41Z'
  support: refutes
  summary: SMILES generates RQZRKFJHRUDTLB-DFBZBFILSA-N; InChI regenerates stored
    RQZRKFJHRUDTLB-IDJYBIRTSA-N. Difference is the exocyclic carbamoylimino C=N geometry,
    not metal disconnection or tetrahedral configuration. Both match C37H57FeN12O18S,
    charge0, mass1045.841, exact1045.298386484 and10 tetrahedral centres.
  snapshot_sha256: ee06b367b07f47ea4bfa6e47580fc2176af2862f8614c08a4a8a952d9f5cf3a5
- evidence_id: repair-check
  kind: validation
  reference: Independent scratch-only repair calculation
  locator: GSRS SMILES and native candidate with only imine bond stereo supplied
  accessed_at: '2026-10-21T08:36:35Z'
  support: supports
  summary: Official GSRS stereo-encoded SMILES regenerates stored full InChI/key.
    A scratch candidate adding the corresponding slash/backslash geometry to native
    SMILES also regenerates the exact retained InChI/key without changing connectivity,
    formula, charge or tetrahedral centres. No native edit occurred.
  snapshot_sha256: a91107fc52dcb0b49ec9a4f7d1d7e48c08e0d2d45c741a7a49969d94a90b467c
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/90479121
  locator: Exact full-key lookup
  accessed_at: '2026-10-21T08:36:04Z'
  support: supports
  summary: CID90479121 matches the retained specified-geometry InChI/key and compatible
    formula/charge/masses.
  snapshot_sha256: 2622f813054797a9f7aaf8d4a82b9806ff44182c90c2c67d6ff27ff710b86a49
- evidence_id: gsrs
  kind: authority
  reference: https://gsrs.ncats.nih.gov/api/v1/substances/H76824799X?view=full
  locator: Full chemical record, structure and codes
  accessed_at: '2026-10-21T08:36:04Z'
  support: supports
  summary: Official δ2 record has the retained exact InChI/key and a SMILES that specifies
    the missing imine geometry. CAS34755-52-7 and PubChem90479121 are additional exact-form
    leads, not already native xrefs.
  snapshot_sha256: 8ef2345274ded9f115125853366284e08a057a042b6bae786e79c7099db48250
- evidence_id: primary2000
  kind: primary_source
  reference: PMID:11217799
  locator: DOI10.7164/antibiotics.53.1346; original pp1346–1353
  accessed_at: '2026-10-21T08:36:23Z'
  support: supports
  summary: ATCC700974 fermentation yielded ferric metaboliteA and aluminium metaboliteB,
    separated chromatographically. Mass before/after acidification and X-ray energy
    spectroscopy distinguish metals. Ferric δ2 was tracked using E.coli ESS agar activity.
    Isolated SB-217452, the seryl nucleoside, inhibits S.aureus/rat SerRS near8nM;
    intact complexes had no such inhibition. Aminoacylation used crude enzyme and
    radiolabeled serine. The proposed intracellular cleavage mechanism must distinguish
    parent from active fragment.
  snapshot_sha256: 5a2d4ea9e93acdbbe981b635ad744a60a192cfa2ec9a47e6f520bdb5abcc6c22
- evidence_id: primary2012
  kind: primary_source
  reference: PMID:22704654
  locator: DOI10.1021/cb300173x; complete primary body, genetic and purification sections
  accessed_at: '2026-10-21T08:32:29Z'
  support: supports
  summary: ATCC700974 produces δ2; gene deletion/complementation supports the abm
    cluster. Purification and shunt-product experiments distinguish δ2 from δ1 and
    descarbamoyl-desmethyl analogs. Detailed pathway arrows include author hypotheses,
    not all directly demonstrated transformations. This is producer/biosynthetic context,
    not direct δ2 binding to every biosynthetic enzyme.
  snapshot_sha256: 6ed17c1e1064f1bc2fdad38fbf7ae408db30be626307f97801a0ae780da0a49c
- evidence_id: assay2018
  kind: primary_source
  reference: PMID:30181560
  locator: DOI10.1038/s41467-018-05821-1; Tables1–3 and Methods
  accessed_at: '2026-10-21T08:31:45Z'
  support: partial
  summary: Synthetic1b has strain-resolved activity, including S.aureus USA300 NRS384
    MIC0.125µg/mL and S.pneumoniae ATCC49619 MIC0.0625µg/mL in the reported media.
    Iron-depleted medium changes selected pneumococcal responses. These are study-specific
    observations, not established clinical breakpoints, and the exact dosing-form
    qualification in the supplement applies.
  snapshot_sha256: 50678e14b6879bb3ad925a4909c0faf91463e2375a08a9f44c6680b410ee5275
- evidence_id: form2018
  kind: primary_source
  reference: https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-018-05821-1/MediaObjects/41467_2018_5821_MOESM1_ESM.pdf
  locator: Physical p79, compound1b; main Fig1 inspected separately
  accessed_at: '2026-10-21T08:32:40Z'
  support: context_only
  summary: Synthetic1b final characterization gives metal-free ligand HRMS C37H60N12NaO18S+
    [M+Na]+1015.3761 and no iron-addition step. Main Fig1 depicts ferric albomycin.
    Preserve this discrepancy before transferring exact ferric MICs; ambient medium
    iron alone does not identify the preparation.
  snapshot_sha256: 3bb3d6d04dc26f64143b263f4fedab624228abe42fe3035746b8873b7ce425cd
- evidence_id: gates
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual focused commands
  accessed_at: '2026-10-21T08:35:44Z'
  support: supports
  summary: Both exit0; one record and zero strict ERROR rows. Deterministic gates
    did not catch the chemical stereo mismatch.
  snapshot_sha256: c828eb92b4ab82a76632cc6d21f054e52ca47f1fc59ce6ebf6f8e09e307e78b9
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: Ignored-inclusive local search and free primary discovery
  accessed_at: '2026-10-21T08:37:51Z'
  support: context_only
  summary: Exact ID,label,slug and raw/PATHS/configuration were searched including
    ignored files. The primary2000 PDF and2012 full text were read;2018 main text,
    relevant supplement and ferric figure were inspected. No family or fragment assay
    was silently transferred to intact ferric δ2.
  search_scope: 'prepare.py83: rg --no-ignore --hidden across batch009 excluding.git/.venv;
    targeted source-owner/curation and full-key checks. Free official ChEBI,PubChem,GSRS,MIBiG
    and J-STAGE/PMC. Initial J-STAGE issue11 URL failed; bibliographic metadata resolved
    correct issue12 PDF.'
assessments:
- assessment_id: identity
  area: identity
  topic: Ferric δ2 entity
  outcome: supported
  summary: Label, ferric definition, formula, mass, charge and retained InChI/key
    identify the exact congener across independent authorities.
  target_ids:
  - CHEBI:83215
  evidence_ids:
  - native
  - pubchem
  - gsrs
- assessment_id: structure
  area: consistency
  topic: Inconsistent imine stereochemistry
  outcome: concern
  summary: Native SMILES omits a geometric configuration specified in native InChI/key.
    Exact scratch repair demonstrates the discrepancy independently.
  target_ids:
  - CHEBI:83215
  evidence_ids:
  - chemistry
  - repair-check
  - chebi
  - gsrs
- assessment_id: grounding
  area: grounding
  topic: Broader parent and antibacterial roles
  outcome: supported
  summary: Parent is broader and the2000 isolated ferric δ2 has direct antibacterial
    fraction-tracking evidence.
  target_ids:
  - CHEBI:83215
  evidence_ids:
  - parent
  - primary2000
  - chebi
- assessment_id: mechanism
  area: evidence
  topic: Prodrug versus active SerRS inhibitor
  outcome: supported
  summary: Inspected primary source distinguishes ferric intact drug from potent SB-217452
    inhibition and proposes cleavage after transport. No native direct target claim
    is present; future annotations must preserve this distinction.
  target_ids:
  - CHEBI:83215
  evidence_ids:
  - primary2000
  - native
- assessment_id: activity
  area: evidence
  topic: Quantitative assay form
  outcome: unknown
  summary: 2018 tables give useful strain/medium-qualified observations, but final
    ligand characterization versus ferric main drawing requires adjudication before
    exact ferric MIC attachment.
  target_ids:
  - CHEBI:83215
  evidence_ids:
  - assay2018
  - form2018
- assessment_id: producer
  area: provenance
  topic: Producer evidence and MIBiG exclusion
  outcome: supported
  summary: Two adopted primary sources support ATCC700974 production. Native producer
    absence is understandable from the raw MIBiG form mismatch and is not a bad producer
    assertion. Any future annotation belongs in the actual native record via validated
    writer/history.
  target_ids:
  - CHEBI:83215
  evidence_ids:
  - primary2000
  - primary2012
  - owner
- assessment_id: resistance
  area: scope
  topic: Mechanism and clinical context boundaries
  outcome: unknown
  summary: Biosynthetic self-protection and study-specific MICs do not establish universal
    resistance determinants, clinical breakpoints or approved δ2 therapy; no such
    claims are native.
  target_ids:
  - CHEBI:83215
  evidence_ids:
  - native
  - primary2012
  - assay2018
- assessment_id: completeness
  area: completeness
  topic: Optional annotations and exact source disposition
  outcome: unknown
  summary: Specific primary activity, producer and active-fragment evidence can be
    curated after structural/form adjudication. Blank optional slots alone are not
    the finding.
  target_ids:
  - CHEBI:83215
  evidence_ids:
  - primary2000
  - primary2012
  - form2018
- assessment_id: history
  area: provenance
  topic: Generated ownership and history
  outcome: supported
  summary: Raw source, mint and three events agree. The imported source also carries
    the geometry omission; status remains SEEDED.
  target_ids:
  - CHEBI:83215
  evidence_ids:
  - native
  - owner
  - chebi
- assessment_id: schema
  area: schema
  topic: Focused validators
  outcome: supported
  summary: Schema and strict gates pass; independent chemistry reports a separate
    material defect.
  target_ids:
  - CHEBI:83215
  evidence_ids:
  - gates
  - chemistry
findings:
- finding_id: F1
  issue_key: chebi-83215-smiles-imine-stereo-omission
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Make the SMILES specify the imine geometry retained in InChI
  description: Native SMILES produces full key RQZRKFJHRUDTLB-DFBZBFILSA-N, while
    native InChI and stored key specify RQZRKFJHRUDTLB-IDJYBIRTSA-N. The missing carbamoylimino
    C=N geometry is inherited from ChEBI/raw. GSRS and a scratch-only stereo completion
    independently reproduce the retained exact structure.
  target_ids:
  - CHEBI:83215
  field_paths:
  - chemical_structure.smiles
  - chemical_structure.standard_inchi
  - chemical_structure.standard_inchi_key
  evidence_ids:
  - native
  - owner
  - chemistry
  - repair-check
  - chebi
  - gsrs
  - pubchem
  rule_id: native-review-checklist:Structure-consistency
  native_severity: major stereochemical representation mismatch
  normalization_reason: The congener remains identifiable and tetrahedral centres
    agree, but one representation loses stereochemical specificity. This material
    consistency defect is not a mere optional-field gap.
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
actions:
- action_id: A1
  description: Adjudicate and correct the imported SMILES imine geometry against the
    independently verified retained exact InChI/key.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:83215
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
  generator: scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  acceptance_checks:
  - Both final encodings regenerate RQZRKFJHRUDTLB-IDJYBIRTSA-N including /b43-24+;
    do not erase geometry from the InChI to manufacture agreement.
  - Preserve all10 tetrahedral centres, ferric-complex stoichiometry, formula and
    charge. Scratch083-stereo-repair-check.json supplies a tested candidate but is
    not a native edit.
  - Apply the maintained source correction and run chemistry consistency, schema,
    strict, source reproduction and history gates.
limitations:
- Independent chemistry failed because SMILES lacks imine geometry; schema/strict
  success does not resolve that defect.
- 2018 synthetic final products have desferri HRMS formulas despite ferric drawings.
  Exact ferric assay transfer requires material adjudication.
- The2000 paper reports intact-complex non-inhibition without a detailed numerical
  complex IC50 ceiling; do not invent one.
- No full-corpus inference of missing evidence follows from this bounded one-record
  search.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All22 captured input hashes rechecked unchanged; no native record or status edits.
- 'Concrete future curation: producer and active-fragment mode may be annotated with
  exact primary evidence and validated history after the structural defect is resolved.
  Transport proteins and biosynthetic enzymes must not be mislabeled as direct antibiotic
  targets.'
- The structure repair is demonstrated only in scratch; the source retains an independently
  verifiable intended geometric isomer.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:83215
- https://gsrs.ncats.nih.gov/api/v1/substances/H76824799X?view=full
- https://www.jstage.jst.go.jp/article/antibiotics1968/53/12/53_12_1346/_pdf
- https://pmc.ncbi.nlm.nih.gov/articles/PMC3448783/
tags:
- antibacterial
- ferric-complex
- stereochemistry
- active-fragment
```
