# Formicamycin H: exact congener and resolved axial assignment

- Review: 20261021T164648Z-formicamycin-h-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T16:37:15Z
- Finished UTC: 2026-10-21T16:46:48Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native formicamycin H graph agrees with seven checked encodings, original compound 11 and the congener-specific 2026 natural-product crystal. That crystal confirms Sa axial configuration after the 2024 synthesis raised a tentative concern using model compounds. Original H B. subtilis inhibition supports the filing class; MRSA/VRE were not tested for H in 2017. No corrective finding is confirmed, while the native standard encodings leave the experimentally supported axis unrepresented. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact H record: minted identity, family definition/sole adopted PMID, broad parent, all chemical fields and three exact xrefs, source concept and three histories; exact original activity, 2024 synthesis concern and 2026 crystal/NMR reconciliation.

Selection: Queue position 463 in isolated batch047, reviewed separately after capture. Original 13 hashes preserved and actual ARO/PubChem/enrichment/readiness inputs appended before detailed assessment, for 17 unchanged inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-19df9f1f8a | data/antibiotics/antibacterial/formicamycin-h.yaml | generated | formicamycin H |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-19df9f1f8a | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-19df9f1f8a | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-19df9f1f8a | Actual focused execution exited 0. |
| Independent chemical-authority comparison | passed | False | antibioticmech:aro-19df9f1f8a | Seven encodings agree by InChIKey and reciprocal chirality-aware graph matching; both pendant O groups are methylated. |
| Input, source, term and history ledger | passed | False | antibioticmech:aro-19df9f1f8a | All 17 hashes and original 13 are intact; all source fields, exact links, sole adopted PMID and three chronological histories accounted for. |
| Structured iModulonDB catalog | passed | False | antibioticmech:aro-19df9f1f8a | Reused actual 461 catalog query for the identical producer context; no separate H-specific execution claimed. |
| Authoritative full QC | failed | True | antibioticmech:aro-19df9f1f8a | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-19df9f1f8a | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-19df9f1f8a | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-19df9f1f8a | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-19df9f1f8a | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-19df9f1f8a | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-19df9f1f8a | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-19df9f1f8a | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-19df9f1f8a | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact congener and chemical cross-references

identity: supported. Targets: antibioticmech:aro-19df9f1f8a.

Original H compound 11, current authority graphs and the exact 2026 natural H crystal agree. The chlorine pattern distinguishes H from same-formula F/G; no salt, synthetic model or neighboring congener is substituted.

### Antibacterial filing and polyketide parent

grounding: supported. Targets: antibioticmech:aro-19df9f1f8a.

The isolated H has positive original B. subtilis growth inhibition and a type II polyketide origin. Its 2017 MRSA/VRE assays were not performed; that is not evidence of inactivity.

### Explicit family definition

scope: supported. Targets: antibioticmech:aro-19df9f1f8a.

Native wording explicitly describes the formicamycin family. Its context does not establish exact H MRSA/VRE or resistance-selection measurements; the original H row and C/J/L passage panel remain distinct.

### Bridgehead configuration and unencoded axis

consistency: unknown. Targets: antibioticmech:aro-19df9f1f8a.

The 2026 natural H crystal supports Sa and 10R,19R, addressing the 2024 tentative model-based concern. Native graphs correctly encode the tetrahedral centers but omit the biaryl axis. No mixture, opposite atropisomer or core inversion follows from that format limitation.

### Exact H molecular target

evidence: unknown. Targets: antibioticmech:aro-19df9f1f8a.

No native target is asserted. Inspected H growth inhibition, synthesis and producer-regulation experiments do not establish a direct antibacterial target. Related fasamycin FabF evidence is not transferred to H.

### 2024 concern resolved by 2026 natural-product evidence

consistency: supported. Targets: antibioticmech:aro-19df9f1f8a.

The 2024 authors explicitly left axial revision uncertain because only model compounds crystallized. The 2026 natural H structure directly supports Sa; the earlier concern is preserved at its original scope, not treated as a current proven native identity defect.

### Maintained ownership and history

provenance: supported. Targets: antibioticmech:aro-19df9f1f8a.

Actual source/extractor/enrichment/seeder owners are captured; original 13 and all 17 total hashes remain unchanged. All asserted identifiers and adopted lead dispositions are accounted for.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/formicamycin-h.yaml; Entire native YAML | supports | One neutral formicamycin H, C30H27Cl3O8, with MINTED ARO identity and two configured tetrahedral centers. No synonyms, quantitative assays, target, resistance, producer, clinical or causal-graph assertions are present. The definition explicitly names formicamycin congeners. |
| owners | Maintained ARO/PubChem extraction and seeding lane; 463-raw-rows.json; 463-source-audit.json; actual extractor/seeder/enrichment sections | supports | The frozen ARO row supplies the family definition, PMID33440167 and broad polyketide class; PubChem CID146684588 supplies the recorded graph. The source mint is reproduced. All three chronological seeded/reseeded histories and 17 original/expanded input hashes are coherent. ChEBI is an exact external structure cross-reference, not the native PubChem owner. |
| chemistry | CHEBI:219476; PubChem CID146684588; 463-authority-chemistry.json; 463-chebi.json/.mol; 463-pc.json | supports | Native SMILES/InChI, ChEBI SMILES/InChI/molfile and PubChem SMILES/InChI agree by WITUCWDZFNOOOS-BJLXPSRBSA-N, formula C30H27Cl3O8, charge zero and reciprocal chirality-aware matching. Both encoded tetrahedral centers are R. The original H drawing independently matches chlorine at positions 2, 14 and 16 and both pendant methoxy groups. Average and monoisotopic masses agree at recorded precision. There is no native ChEMBL cross-reference. |
| aro | ARO:3007594; ARO:3007574; ARO:3005171; 463-aro-blocks.json, extracted from current official 426-current-aro.obo | supports | The exact current ARO term repeats the definition, sole PMID and ChEBI/PubChem links. Its parent chain through formicamycin leads to polyketide with antibiotic activity, consistent with original biosynthetic and antibacterial evidence. Present ChEBI availability does not itself change the frozen MINTED status. |
| identity | PMID:28507698; DOI:10.1039/c6sc04265a; Original isolation/stereochemistry sections and Figure 1; SI pp42–43 compound 11, drawing and analytical entry visually inspected | supports | Original H is compound 11, isolated as 0.3 mg from S. formicae KY5. SI reports C30H27O8Cl3 and observed [M+H]+ 621.0829, with proton/NOESY data. Original main NOESY/ECD supported 10R,19R while explicitly withholding definitive formicamycin axial assignment. The H-specific chlorine pattern distinguishes it from same-formula F/G. Source culture antifungal extracts are separate from exact H antibacterial material. |
| activity | PMID:28507698; DOI:10.1039/c6sc04265a; Original Table 1 exact compound 11 row and SI 1g p56 | supports | H has a B. subtilis MIC of 10 μM; its MRSA/VRE entries explicitly say not tested. The method uses LB without NaCl, 1 mL 24-well cultures, starting OD600 of 0.08–0.15, 40 μL water/methanol stock and static 30°C incubation, with no observable overnight growth as endpoint. The laboratory B. subtilis has no precise strain accession in the inspected method. Not-tested MRSA/VRE cells are not negative susceptibility measurements. |
| selection | PMID:28507698; Resistance-selection Results and SI 1g | partial | The four- and twenty-generation MRSA passage experiments test compounds 6, 13, 15, corresponding to C, J and L, not H. No MIC increase occurred under those reported conditions. Native wording explicitly describes congeners; no individual-H resistance-selection or resistance-proof assertion is inferred. |
| adopted | PMID:33440167; DOI:10.1016/j.chembiol.2020.12.011; PMC8062789 complete abstract, introduction, selected regulator Results/Discussion, actual Table 2 and Bioassays methods | partial | The sole adopted PMID33440167 studies producer regulation and increased production. Its actual Table 2 assays formicamycins J/R/S alongside fasamycins, not H. Its family antibacterial and resistance background refers to Qin 2017. ForJ/ForGF/ForZ and the putative exporter are producer-cell biosynthetic components, not demonstrated antibacterial targets of H. |
| revision | PMID:41988676; DOI:10.1021/acs.jnatprod.6c00145; 2026 H-specific Results, actual Table 1 H (1) row, Crystallographic Data for 1 and SI Tables S1/S2 pp3–4 | supports | The natural H crystal diffracted to 0.76 Å and unambiguously supports Sa, with Flack 0.032(7); the formicamycin framework is 10R,19R. Table 1 retains the H structure as published. CCDC2498172 is reported for a crystal modeled with one DMSO and two waters per parent, not a redefinition of native neutral H as a hydrate/solvate. SI compares natural versus synthetic H proton/carbon NMR in CDCl3. This direct natural-product evidence resolves the earlier tentative model-compound concern; H is not one of the B/D/I constitutional revisions. |
| synthesis | PMID:39265189; DOI:10.1021/jacs.4c09068; 463-synthesis-pmc.html: complete abstract, models 12/13 discussion, final coupling paragraph and conclusion | context_only | The 2024 original total synthesis reports matching spectral data but explicitly says H itself did not yield diffraction data. Crystals of model compounds 12/13 suggested possible opposite axial configuration; the authors state that revision could not be made with certainty. This is a qualified concern rather than a demonstrated Ra identity for natural H. No exact H antibacterial mechanism or new H MIC assay was inspected in the synthesis sections. |
| adapter | iModulonDB; 461-adapter-catalog.txt and 461-adapter-results.json, reused actual catalog query during the adjacent exact-record review | context_only | The actual 461 catalog query is reused for the same S. formicae producer context. No matching S. formicae dataset is listed. No protein/pathway is asserted in native H, and no neighboring Streptomyces species or expression membership is treated as antibacterial target evidence. |
| gates | Focused native checks; 463-focused-results.json; 463-chemistry.json; 463-schema.log; 463-strict.log | supports | Native chemistry, schema and strict checks all exited zero; independent graph and source-ledger commands also exited zero. These checks neither establish a molecular target nor promote native scientific status. |
| search | Bounded exact-compound source investigation; 463-owners-search.json; 463-search.json; 463-fetch.json; 463-synthesis-fetch.json and 463-synthesis-fetch2.json | context_only | Ignored-inclusive local exact-name/identifier searches locate actual ARO/PubChem/readiness owners. Exact H public searches identify the 2024 synthesis and 2026 resolution. EuropePMC original 2024 XML returned 500 and ACS returned 403; a subsequent official PMC HTML request with report=xml successfully returned the complete article. The failed routes are not described as missing primary evidence after that successful retrieval. |

## Limits And Additional Notes

- Original 2017 H isolation/drawing, proton/NOESY analytical data, exact Table 1 row and SI 1g methods were inspected; raw spectra were not reprocessed.
- The sole adopted 2021 paper was read at complete abstract and selected relevant Results/Table 2/methods depth; its formicamycin activity panel is J/R/S rather than H.
- The 2024 full article was successfully retrieved after failed XML/publisher routes; the abstract and relevant synthesis/stereochemistry/conclusion passages were inspected, not every reaction optimization or raw SI dataset.
- The 2026 direct H crystal, exact Table 1 row and SI natural/synthetic NMR comparisons were read. Raw diffraction data were not reprocessed, and the native standard structures still omit the experimentally supported biaryl axis.
- No H-specific MRSA/VRE observation, resistance-selection experiment or direct antibacterial target is established by the inspected original 2017/2021 evidence. Optional native collections are not required solely because the schema permits them.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Standalone chemistry used batch019 against batch047; schema/strict, ledger and contract use batch047. The actual 461 adapter catalog is explicitly reused for the identical producer context.
- No native or maintained source bytes or scientific status were changed.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T164648Z-formicamycin-h-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Formicamycin H: exact congener and resolved axial assignment'
started_at: '2026-10-21T16:37:15Z'
finished_at: '2026-10-21T16:46:48Z'
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
summary: The native formicamycin H graph agrees with seven checked encodings, original
  compound 11 and the congener-specific 2026 natural-product crystal. That crystal
  confirms Sa axial configuration after the 2024 synthesis raised a tentative concern
  using model compounds. Original H B. subtilis inhibition supports the filing class;
  MRSA/VRE were not tested for H in 2017. No corrective finding is confirmed, while
  the native standard encodings leave the experimentally supported axis unrepresented.
  Scientific assessment retains the stated evidence limits; full verification is blocked
  by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/formicamycin-h.yaml
    sha256: b3197b2a95247f4b1b629ce95913a8fae963ab03735e6efcc4d189be64562aed
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
  - path: curation/record_review_queue.tsv
    sha256: 3828a5120b892ee0ee0b776affc6c3e4f1f1a3355ec4edd30e6005762de00e70
    role: context
targets:
- target_id: antibioticmech:aro-19df9f1f8a
  path: data/antibiotics/antibacterial/formicamycin-h.yaml
  label: formicamycin H
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, family definition, class, literature lead and xrefs
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact PubChem molecular structure
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: CARD/ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated native fields
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding and exclusion overrides
  - repository: CultureBotAI/AntibioticMech
    path: curation/record_review_queue.tsv
    role: Source literature readiness leads
scope:
  description: 'Entire exact H record: minted identity, family definition/sole adopted
    PMID, broad parent, all chemical fields and three exact xrefs, source concept
    and three histories; exact original activity, 2024 synthesis concern and 2026
    crystal/NMR reconciliation.'
  selection: Queue position 463 in isolated batch047, reviewed separately after capture.
    Original 13 hashes preserved and actual ARO/PubChem/enrichment/readiness inputs
    appended before detailed assessment, for 17 unchanged inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-19df9f1f8a
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-19df9f1f8a
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    463
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-19df9f1f8a
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/formicamycin-h.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-19df9f1f8a
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/formicamycin-h.yaml --out /private/tmp/am-review-session/463-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: authority
  name: Independent chemical-authority comparison
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/463-authority-check.py
    > /private/tmp/am-review-session/463-authority-check.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Seven encodings agree by InChIKey and reciprocal chirality-aware graph
    matching; both pendant O groups are methylated.
  target_ids:
  - antibioticmech:aro-19df9f1f8a
  evidence_ids:
  - chemistry
- check_id: ledger
  name: Input, source, term and history ledger
  command: .venv/bin/python /private/tmp/am-review-session/463-ledger.py > /private/tmp/am-review-session/463-ledger.log
    2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: All 17 hashes and original 13 are intact; all source fields, exact links,
    sole adopted PMID and three chronological histories accounted for.
  target_ids:
  - antibioticmech:aro-19df9f1f8a
  evidence_ids:
  - owners
- check_id: adapter
  name: Structured iModulonDB catalog
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Reused actual 461 catalog query for the identical producer context; no
    separate H-specific execution claimed.
  target_ids:
  - antibioticmech:aro-19df9f1f8a
  evidence_ids:
  - adapter
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-19df9f1f8a
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
  - antibioticmech:aro-19df9f1f8a
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
  - antibioticmech:aro-19df9f1f8a
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
  - antibioticmech:aro-19df9f1f8a
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
  - antibioticmech:aro-19df9f1f8a
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
  - antibioticmech:aro-19df9f1f8a
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
  - antibioticmech:aro-19df9f1f8a
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
  - antibioticmech:aro-19df9f1f8a
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
  - antibioticmech:aro-19df9f1f8a
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/formicamycin-h.yaml
  locator: Entire native YAML
  accessed_at: '2026-10-21T16:45:04Z'
  support: supports
  summary: One neutral formicamycin H, C30H27Cl3O8, with MINTED ARO identity and two
    configured tetrahedral centers. No synonyms, quantitative assays, target, resistance,
    producer, clinical or causal-graph assertions are present. The definition explicitly
    names formicamycin congeners.
- evidence_id: owners
  kind: database
  reference: Maintained ARO/PubChem extraction and seeding lane
  locator: 463-raw-rows.json; 463-source-audit.json; actual extractor/seeder/enrichment
    sections
  accessed_at: '2026-10-21T16:45:04Z'
  support: supports
  summary: The frozen ARO row supplies the family definition, PMID33440167 and broad
    polyketide class; PubChem CID146684588 supplies the recorded graph. The source
    mint is reproduced. All three chronological seeded/reseeded histories and 17 original/expanded
    input hashes are coherent. ChEBI is an exact external structure cross-reference,
    not the native PubChem owner.
  snapshot_sha256: 4905dee44d424346295e5713ee7c8da57e1fa88bdcc9bc50228c592a048e2f1f
- evidence_id: chemistry
  kind: validation
  reference: CHEBI:219476; PubChem CID146684588
  locator: 463-authority-chemistry.json; 463-chebi.json/.mol; 463-pc.json
  accessed_at: '2026-10-21T16:45:04Z'
  support: supports
  summary: Native SMILES/InChI, ChEBI SMILES/InChI/molfile and PubChem SMILES/InChI
    agree by WITUCWDZFNOOOS-BJLXPSRBSA-N, formula C30H27Cl3O8, charge zero and reciprocal
    chirality-aware matching. Both encoded tetrahedral centers are R. The original
    H drawing independently matches chlorine at positions 2, 14 and 16 and both pendant
    methoxy groups. Average and monoisotopic masses agree at recorded precision. There
    is no native ChEMBL cross-reference.
  snapshot_sha256: c5c81f9df002298e8c06b2af8df2109949713edd2dea68de6bc4ba14e698b276
- evidence_id: aro
  kind: authority
  reference: ARO:3007594; ARO:3007574; ARO:3005171
  locator: 463-aro-blocks.json, extracted from current official 426-current-aro.obo
  accessed_at: '2026-10-21T16:45:04Z'
  support: supports
  summary: The exact current ARO term repeats the definition, sole PMID and ChEBI/PubChem
    links. Its parent chain through formicamycin leads to polyketide with antibiotic
    activity, consistent with original biosynthetic and antibacterial evidence. Present
    ChEBI availability does not itself change the frozen MINTED status.
  snapshot_sha256: 39a1e8b824e23cd92ef8134c1542b913c933af6d628e1780fe37672950f4725a
- evidence_id: identity
  kind: primary_source
  reference: PMID:28507698; DOI:10.1039/c6sc04265a
  locator: Original isolation/stereochemistry sections and Figure 1; SI pp42–43 compound
    11, drawing and analytical entry visually inspected
  accessed_at: '2026-10-21T16:45:04Z'
  support: supports
  summary: Original H is compound 11, isolated as 0.3 mg from S. formicae KY5. SI
    reports C30H27O8Cl3 and observed [M+H]+ 621.0829, with proton/NOESY data. Original
    main NOESY/ECD supported 10R,19R while explicitly withholding definitive formicamycin
    axial assignment. The H-specific chlorine pattern distinguishes it from same-formula
    F/G. Source culture antifungal extracts are separate from exact H antibacterial
    material.
  snapshot_sha256: c30ad317fb5a4e00f304850ff2bd67d2960f7643f468e35a913bda99aca2f70d
- evidence_id: activity
  kind: primary_source
  reference: PMID:28507698; DOI:10.1039/c6sc04265a
  locator: Original Table 1 exact compound 11 row and SI 1g p56
  accessed_at: '2026-10-21T16:45:04Z'
  support: supports
  summary: H has a B. subtilis MIC of 10 μM; its MRSA/VRE entries explicitly say not
    tested. The method uses LB without NaCl, 1 mL 24-well cultures, starting OD600
    of 0.08–0.15, 40 μL water/methanol stock and static 30°C incubation, with no observable
    overnight growth as endpoint. The laboratory B. subtilis has no precise strain
    accession in the inspected method. Not-tested MRSA/VRE cells are not negative
    susceptibility measurements.
  snapshot_sha256: 741a682eefa78fdbcfb69b76eddd1d23df3e5bffbb60b2c7df34b51d923083d5
- evidence_id: selection
  kind: primary_source
  reference: PMID:28507698
  locator: Resistance-selection Results and SI 1g
  accessed_at: '2026-10-21T16:45:04Z'
  support: partial
  summary: The four- and twenty-generation MRSA passage experiments test compounds
    6, 13, 15, corresponding to C, J and L, not H. No MIC increase occurred under
    those reported conditions. Native wording explicitly describes congeners; no individual-H
    resistance-selection or resistance-proof assertion is inferred.
  snapshot_sha256: 741a682eefa78fdbcfb69b76eddd1d23df3e5bffbb60b2c7df34b51d923083d5
- evidence_id: adopted
  kind: primary_source
  reference: PMID:33440167; DOI:10.1016/j.chembiol.2020.12.011
  locator: PMC8062789 complete abstract, introduction, selected regulator Results/Discussion,
    actual Table 2 and Bioassays methods
  accessed_at: '2026-10-21T16:45:04Z'
  support: partial
  summary: The sole adopted PMID33440167 studies producer regulation and increased
    production. Its actual Table 2 assays formicamycins J/R/S alongside fasamycins,
    not H. Its family antibacterial and resistance background refers to Qin 2017.
    ForJ/ForGF/ForZ and the putative exporter are producer-cell biosynthetic components,
    not demonstrated antibacterial targets of H.
  snapshot_sha256: e55b2fd0ccc375fd9d04e77b0102d8588ed7bab670427d6124477a3d2c38cdae
- evidence_id: revision
  kind: primary_source
  reference: PMID:41988676; DOI:10.1021/acs.jnatprod.6c00145
  locator: 2026 H-specific Results, actual Table 1 H (1) row, Crystallographic Data
    for 1 and SI Tables S1/S2 pp3–4
  accessed_at: '2026-10-21T16:45:04Z'
  support: supports
  summary: The natural H crystal diffracted to 0.76 Å and unambiguously supports Sa,
    with Flack 0.032(7); the formicamycin framework is 10R,19R. Table 1 retains the
    H structure as published. CCDC2498172 is reported for a crystal modeled with one
    DMSO and two waters per parent, not a redefinition of native neutral H as a hydrate/solvate.
    SI compares natural versus synthetic H proton/carbon NMR in CDCl3. This direct
    natural-product evidence resolves the earlier tentative model-compound concern;
    H is not one of the B/D/I constitutional revisions.
  snapshot_sha256: 55796020973e571658d3a02c0080a44cff02e2bd6113dbfe0c942357eb04354d
- evidence_id: synthesis
  kind: primary_source
  reference: PMID:39265189; DOI:10.1021/jacs.4c09068
  locator: '463-synthesis-pmc.html: complete abstract, models 12/13 discussion, final
    coupling paragraph and conclusion'
  accessed_at: '2026-10-21T16:45:04Z'
  support: context_only
  summary: The 2024 original total synthesis reports matching spectral data but explicitly
    says H itself did not yield diffraction data. Crystals of model compounds 12/13
    suggested possible opposite axial configuration; the authors state that revision
    could not be made with certainty. This is a qualified concern rather than a demonstrated
    Ra identity for natural H. No exact H antibacterial mechanism or new H MIC assay
    was inspected in the synthesis sections.
  snapshot_sha256: 031c08a14acaf9371f2e2ab0a687b06c3eb5bdd1097ba20b6f50d58dbbdd6ecc
- evidence_id: adapter
  kind: database
  reference: iModulonDB
  locator: 461-adapter-catalog.txt and 461-adapter-results.json, reused actual catalog
    query during the adjacent exact-record review
  accessed_at: '2026-10-21T16:45:04Z'
  support: context_only
  summary: The actual 461 catalog query is reused for the same S. formicae producer
    context. No matching S. formicae dataset is listed. No protein/pathway is asserted
    in native H, and no neighboring Streptomyces species or expression membership
    is treated as antibacterial target evidence.
  snapshot_sha256: c699dc2b41711d1d20635d5941bd524d8caf61ddcdf5199d182d2c293aa3d370
- evidence_id: gates
  kind: validation
  reference: Focused native checks
  locator: 463-focused-results.json; 463-chemistry.json; 463-schema.log; 463-strict.log
  accessed_at: '2026-10-21T16:45:04Z'
  support: supports
  summary: Native chemistry, schema and strict checks all exited zero; independent
    graph and source-ledger commands also exited zero. These checks neither establish
    a molecular target nor promote native scientific status.
  snapshot_sha256: 8853db83de657ea2179b26a41c6d3a5e8b553cbd2b3ecb48eedf9f5040dd80ac
- evidence_id: search
  kind: search
  reference: Bounded exact-compound source investigation
  locator: 463-owners-search.json; 463-search.json; 463-fetch.json; 463-synthesis-fetch.json
    and 463-synthesis-fetch2.json
  accessed_at: '2026-10-21T16:45:04Z'
  support: context_only
  summary: Ignored-inclusive local exact-name/identifier searches locate actual ARO/PubChem/readiness
    owners. Exact H public searches identify the 2024 synthesis and 2026 resolution.
    EuropePMC original 2024 XML returned 500 and ACS returned 403; a subsequent official
    PMC HTML request with report=xml successfully returned the complete article. The
    failed routes are not described as missing primary evidence after that successful
    retrieval.
  search_scope: rg --no-ignore --hidden over data/raw, curation, conf and scripts
    using exact label, ARO, CID and minted identifier; free exact-name literature
    and official chemical sources.
  snapshot_sha256: 4dd5f3eadeb7f633110cac6ac4f9579eb3fa3e9434a9b582cbee9ca44d5a2306
assessments:
- assessment_id: identity
  area: identity
  topic: Exact congener and chemical cross-references
  outcome: supported
  summary: Original H compound 11, current authority graphs and the exact 2026 natural
    H crystal agree. The chlorine pattern distinguishes H from same-formula F/G; no
    salt, synthetic model or neighboring congener is substituted.
  target_ids:
  - antibioticmech:aro-19df9f1f8a
  evidence_ids:
  - record
  - identity
  - chemistry
  - revision
- assessment_id: activity
  area: grounding
  topic: Antibacterial filing and polyketide parent
  outcome: supported
  summary: The isolated H has positive original B. subtilis growth inhibition and
    a type II polyketide origin. Its 2017 MRSA/VRE assays were not performed; that
    is not evidence of inactivity.
  target_ids:
  - antibioticmech:aro-19df9f1f8a
  evidence_ids:
  - activity
  - identity
  - aro
  - adopted
- assessment_id: definition
  area: scope
  topic: Explicit family definition
  outcome: supported
  summary: Native wording explicitly describes the formicamycin family. Its context
    does not establish exact H MRSA/VRE or resistance-selection measurements; the
    original H row and C/J/L passage panel remain distinct.
  target_ids:
  - antibioticmech:aro-19df9f1f8a
  evidence_ids:
  - adopted
  - selection
  - activity
- assessment_id: stereo
  area: consistency
  topic: Bridgehead configuration and unencoded axis
  outcome: unknown
  summary: The 2026 natural H crystal supports Sa and 10R,19R, addressing the 2024
    tentative model-based concern. Native graphs correctly encode the tetrahedral
    centers but omit the biaryl axis. No mixture, opposite atropisomer or core inversion
    follows from that format limitation.
  target_ids:
  - antibioticmech:aro-19df9f1f8a
  evidence_ids:
  - chemistry
  - identity
  - revision
  - synthesis
- assessment_id: mechanism
  area: evidence
  topic: Exact H molecular target
  outcome: unknown
  summary: No native target is asserted. Inspected H growth inhibition, synthesis
    and producer-regulation experiments do not establish a direct antibacterial target.
    Related fasamycin FabF evidence is not transferred to H.
  target_ids:
  - antibioticmech:aro-19df9f1f8a
  evidence_ids:
  - record
  - adopted
  - adapter
- assessment_id: source-conflict
  area: consistency
  topic: 2024 concern resolved by 2026 natural-product evidence
  outcome: supported
  summary: The 2024 authors explicitly left axial revision uncertain because only
    model compounds crystallized. The 2026 natural H structure directly supports Sa;
    the earlier concern is preserved at its original scope, not treated as a current
    proven native identity defect.
  target_ids:
  - antibioticmech:aro-19df9f1f8a
  evidence_ids:
  - synthesis
  - revision
- assessment_id: provenance
  area: provenance
  topic: Maintained ownership and history
  outcome: supported
  summary: Actual source/extractor/enrichment/seeder owners are captured; original
    13 and all 17 total hashes remain unchanged. All asserted identifiers and adopted
    lead dispositions are accounted for.
  target_ids:
  - antibioticmech:aro-19df9f1f8a
  evidence_ids:
  - owners
  - aro
  - gates
findings: []
actions: []
limitations:
- Original 2017 H isolation/drawing, proton/NOESY analytical data, exact Table 1 row
  and SI 1g methods were inspected; raw spectra were not reprocessed.
- The sole adopted 2021 paper was read at complete abstract and selected relevant
  Results/Table 2/methods depth; its formicamycin activity panel is J/R/S rather than
  H.
- The 2024 full article was successfully retrieved after failed XML/publisher routes;
  the abstract and relevant synthesis/stereochemistry/conclusion passages were inspected,
  not every reaction optimization or raw SI dataset.
- The 2026 direct H crystal, exact Table 1 row and SI natural/synthetic NMR comparisons
  were read. Raw diffraction data were not reprocessed, and the native standard structures
  still omit the experimentally supported biaryl axis.
- No H-specific MRSA/VRE observation, resistance-selection experiment or direct antibacterial
  target is established by the inspected original 2017/2021 evidence. Optional native
  collections are not required solely because the schema permits them.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Standalone chemistry used batch019 against batch047; schema/strict, ledger and contract
  use batch047. The actual 461 adapter catalog is explicitly reused for the identical
  producer context.
- No native or maintained source bytes or scientific status were changed.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://doi.org/10.1039/c6sc04265a
- https://doi.org/10.1016/j.chembiol.2020.12.011
- https://doi.org/10.1021/jacs.4c09068
- https://doi.org/10.1021/acs.jnatprod.6c00145
```
