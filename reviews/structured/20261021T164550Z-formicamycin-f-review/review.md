# Formicamycin F: exact congener and bounded family evidence

- Review: 20261021T164550Z-formicamycin-f-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T16:37:11Z
- Finished UTC: 2026-10-21T16:45:50Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The recorded formicamycin F graph agrees with all eight checked native and authority encodings and the original isolated compound 9. Its exact original antibacterial results support the filing class. The definition explicitly describes congeners; resistance selection was tested on C/J/L, not F. The 2026 singly methoxylated E-ring revisions do not establish an F defect. No corrective finding is confirmed; axial representation and later-source assay access remain limited. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire formicamycin F YAML: minted identity, family definition and sole adopted PMID, broad polyketide parent, all chemical fields and four exact xrefs, source concept, all three histories, original exact-congener identity/activity and 2026 revision scope.

Selection: Queue position 461 in isolated batch047, reviewed separately after capture. Original 13 hashes preserved and actual ARO/PubChem/enrichment/readiness inputs appended before detailed assessment, for 17 unchanged inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-d4b630f1d7 | data/antibiotics/antibacterial/formicamycin-f.yaml | generated | formicamycin F |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-d4b630f1d7 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-d4b630f1d7 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-d4b630f1d7 | Actual focused execution exited 0. |
| Independent chemical-authority comparison | passed | False | antibioticmech:aro-d4b630f1d7 | Eight encodings agree by InChIKey and reciprocal chirality-aware graph matching; pendant ring has both ortho and para methoxy groups. |
| Input, source, term and history ledger | passed | False | antibioticmech:aro-d4b630f1d7 | All 17 hashes and original 13 are intact; all source fields, exact links, sole adopted PMID and three chronological histories accounted for. |
| Structured iModulonDB catalog | passed | False | antibioticmech:aro-d4b630f1d7 | Actual catalog query succeeded; no S. formicae dataset is listed. No substitute species or phenotype inference was used. |
| Authoritative full QC | failed | True | antibioticmech:aro-d4b630f1d7 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-d4b630f1d7 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-d4b630f1d7 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-d4b630f1d7 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-d4b630f1d7 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-d4b630f1d7 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-d4b630f1d7 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-d4b630f1d7 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-d4b630f1d7 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact congener and chemical cross-references

identity: supported. Targets: antibioticmech:aro-d4b630f1d7.

All recorded graph and formula fields agree with current exact authorities and original compound9, including the F-specific chlorine pattern. No salt, family mixture or constitutional revision is substituted.

### Antibacterial filing and polyketide parent

grounding: supported. Targets: antibioticmech:aro-d4b630f1d7.

The exact isolated F compound has positive original strain-scoped MICs, and typeII polyketide biosynthesis supports the broad parent. Current source labels alone are not the activity evidence.

### Explicit family definition

scope: supported. Targets: antibioticmech:aro-d4b630f1d7.

The native subject is the congener family. Its context is traceable to the adopted source and original literature; exact F potency is separately established, while resistance selection remains limited to C/J/L. A future exact-record rewrite may make that distinction clearer without claiming a demonstrated current individual-F assertion.

### Bridgehead configuration and unencoded axis

consistency: unknown. Targets: antibioticmech:aro-d4b630f1d7.

Two R,R tetrahedral centers are supported. Standard stored encodings do not specify the biaryl Sa axis; the 2026 family inference is not converted to an F-specific crystal claim, and omission alone does not imply a mixture.

### Exact F molecular target

evidence: unknown. Targets: antibioticmech:aro-d4b630f1d7.

No native molecular target is asserted and none is established by the inspected F identity/growth experiments. Producer regulators and related fasamycin targets cannot supply an F mechanism.

### Later KIB-1414 exact assay

quantity: unknown. Targets: antibioticmech:aro-d4b630f1d7.

Public original abstract and SI support the later congener context and matching drawing; exact later F quantitative assay scope remains unverified, so no secondary numbers are adopted.

### Maintained ownership and history

provenance: supported. Targets: antibioticmech:aro-d4b630f1d7.

Actual source/extractor/enrichment/seeder owners are captured; original 13 and all 17 total hashes remain unchanged. All asserted identifiers and adopted lead dispositions are accounted for.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/formicamycin-f.yaml; Entire native YAML | supports | One neutral formicamycin F, C30H27Cl3O8, MINTED ARO identity and two configured tetrahedral centers. No synonyms, quantitative activity, molecular targets, resistance edges, producers, clinical claims or causal graphs are present. The definition explicitly names formicamycin congeners. |
| owners | Maintained ARO/PubChem extraction and seeding lane; 461-raw-rows.json; 461-source-audit.json; actual extractor/seeder/enrichment sections | supports | The frozen ARO row supplies the family definition, PMID33440167 and broad polyketide class; PubChem CID146684586 supplies the recorded graph. The source mint is reproduced. All three chronological seeded/reseeded histories and 17 original/expanded input hashes are coherent. ChEBI is an exact external structure cross-reference, not the native PubChem owner. |
| chemistry | CHEBI:219466; PubChem CID146684586; CHEMBL4641739; 461-authority-chemistry.json; 461-chebi.json/.mol; 461-pc.json; 461-chembl.json | supports | Native SMILES/InChI, ChEBI SMILES/InChI/molfile, PubChem SMILES/InChI and ChEMBL SMILES give identical UOFYXWHFYPFLPH-HZAQMHFWSA-N, C30H27Cl3O8, charge zero and two R,R centers with reciprocal chiral graph matches. The original drawing independently matches the chlorination and two pendant methoxy groups. Native average and monoisotopic masses agree at recorded precision. |
| aro | ARO:3007589; ARO:3007574; ARO:3005171; 461-aro-blocks.json, extracted from current official 426-current-aro.obo | supports | The exact current ARO term repeats the native definition, PMID and three external links. The parent chain leads through formicamycin to polyketide with antibiotic activity. Original biosynthetic and isolated-antibacterial evidence supports that broad class. No native grounding-status promotion follows merely from present ChEBI availability. |
| identity | PMID:28507698; DOI:10.1039/c6sc04265a; Original main isolation and stereochemistry sections, Figure1 visually read; SI pp37–38 compound9 and original drawing | supports | Exact formicamycin F is compound 9, isolated as 3 mg from S. formicae KY5. The SI reports C30H27O8Cl3 and observed [M+H]+621.0848, with NMR data and optical activity. Combined family NOESY/ECD supported 10R,19R; the 2017 text explicitly withheld a definitive formicamycin axial assignment. This is an isolated single named congener, not a family mixture. |
| activity | PMID:28507698; DOI:10.1039/c6sc04265a; Original Table1 exact compound9 row and SI1g p56 | supports | F has MICs 5, 20 and 2.5 μM against the laboratory B. subtilis, hospital MRSA and VRE E. faecium B16.06226 tests, respectively. The method uses LB without NaCl, 1 mL 24-well cultures, starting OD600 0.08–0.15, 40 μL water/methanol stock and static 30°C incubation; endpoint is no observable overnight growth. The MRSA isolate and B. subtilis lack precise accession identifiers in these methods. These experimental MICs are not clinical breakpoints or universal organism susceptibility. |
| selection | PMID:28507698; Resistance-selection Results and SI1g | partial | Four- and twenty-generation MRSA passage experiments concern compounds 6, 13 and 15, corresponding to C, J and L. No MIC increase was observed under those conditions. This does not establish F-specific resistance-selection behavior; the explicitly family-worded native definition remains contextual. |
| adopted | PMID:33440167; DOI:10.1016/j.chembiol.2020.12.011; PMC8062789 complete abstract, introduction, selected regulator Results/Discussion, actual Table2 and Bioassays methods | partial | The sole adopted lead investigates regulation and increased production in S. formicae KY5. Its Table2 tests formicamycins J/R/S alongside fasamycins, not F. The family antibacterial/resistance introduction points back to Qin2017. ForJ, ForGF, ForZ and the putative exporter have producer-cell biosynthetic roles; these are not demonstrated F antibacterial targets. |
| revision | PMID:41988676; DOI:10.1021/acs.jnatprod.6c00145; 2026 exact revision paragraphs and H axial-crystallography discussion | context_only | The constitutional revisions specifically include formicamycins B, D and I with a single pendant methoxy group. F has both pendant ortho and para methoxy groups, so swapping the historical single-methoxy assignment does not alter F. The paper demonstrates Sa for sampled crystals, notably H, and proposes broader family scope. No F-specific crystal or F constitutional revision was identified in these inspected passages. |
| later-isolation | PMID:32519857; DOI:10.1021/acs.jnatprod.0c00161; Original complete publisher abstract; public SI TablesS3/S4 pS6 and FigureS1 pS7 visually read | partial | The abstract describes nine new and ten known congeners from Streptomyces sp. KIB-1414, with a family activity range. SI compound18 has the same exact F substitution pattern and two drawn core centers. The exact main-text F assay row was not inspected at this review point; secondary F potency numbers are not adopted. SI NMR/drawings do not replace the missing assay methods or table. |
| adapter | iModulonDB; 461-adapter-catalog.txt and 461-adapter-results.json | context_only | Actual dataset catalog queried before further protein-context investigation. No S. formicae dataset is present; listed S. albidoflavus/coelicolor are not substituted. Native contains no protein or pathway assertion, and lack of a matching dataset is not negative biological evidence. |
| gates | Focused native checks; 461-focused-results.json; 461-chemistry.json; 461-schema.log; 461-strict.log | supports | Native chemistry, schema and strict checks all exited zero; independent graph and source-ledger commands also exited zero. These checks neither establish a molecular target nor promote native scientific status. |
| search | Bounded exact-compound source investigation; 461-owners-search.json; 461-search.json; 461-fetch.json; exact F/KIB-1414 public search | context_only | Ignored-inclusive local searches located the actual ARO/PubChem/readiness rows. Public searches identified the original2017, adopted2021 and later2020/2026 sources. Source access and exact-table limits are preserved; no absence of an optional native collection is treated as a defect. |

## Limits And Additional Notes

- The 2017 original exact drawing, analytical entry, Table1 row, stereochemistry discussion and SI assay methods were inspected; raw NMR spectra were not reprocessed.
- The sole adopted 2021 paper was read at complete abstract and selected relevant main sections/Table2/methods depth; all sequencing and supplementary regulator data were not independently reanalyzed.
- The later 2020 complete abstract and SI were inspected, but its exact F main assay table and methods were not available to this review at draft completion. No secondary quantitative value is treated as primary evidence.
- The 2026 source supplies sampled-congener axial evidence and exact B/D/I revisions; no F-specific crystallographic result is asserted. Standard native graphs do not encode the biaryl axis.
- No exact F resistance-selection experiment or molecular target is established by the inspected sources. Absence of optional native target/producer/MIC collections is not itself a corrective finding.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Standalone chemistry used the batch019 interpreter against batch047. Native schema/strict, ledger and contract use batch047.
- Only scratch review artifacts were authored during this review; no native data, maintained source input or curation status changed.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T164550Z-formicamycin-f-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Formicamycin F: exact congener and bounded family evidence'
started_at: '2026-10-21T16:37:11Z'
finished_at: '2026-10-21T16:45:50Z'
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
summary: The recorded formicamycin F graph agrees with all eight checked native and
  authority encodings and the original isolated compound 9. Its exact original antibacterial
  results support the filing class. The definition explicitly describes congeners;
  resistance selection was tested on C/J/L, not F. The 2026 singly methoxylated E-ring
  revisions do not establish an F defect. No corrective finding is confirmed; axial
  representation and later-source assay access remain limited. Scientific assessment
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
  - path: data/antibiotics/antibacterial/formicamycin-f.yaml
    sha256: e5761d6ca3fb2e8a7edfc6235e0181faed15266d1e60ac06e12f6f259ae42f60
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
- target_id: antibioticmech:aro-d4b630f1d7
  path: data/antibiotics/antibacterial/formicamycin-f.yaml
  label: formicamycin F
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
  description: 'Entire formicamycin F YAML: minted identity, family definition and
    sole adopted PMID, broad polyketide parent, all chemical fields and four exact
    xrefs, source concept, all three histories, original exact-congener identity/activity
    and 2026 revision scope.'
  selection: Queue position 461 in isolated batch047, reviewed separately after capture.
    Original 13 hashes preserved and actual ARO/PubChem/enrichment/readiness inputs
    appended before detailed assessment, for 17 unchanged inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-d4b630f1d7
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-d4b630f1d7
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    461
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-d4b630f1d7
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/formicamycin-f.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-d4b630f1d7
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/formicamycin-f.yaml --out /private/tmp/am-review-session/461-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: authority
  name: Independent chemical-authority comparison
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/461-authority-check.py
    > /private/tmp/am-review-session/461-authority-check.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Eight encodings agree by InChIKey and reciprocal chirality-aware graph
    matching; pendant ring has both ortho and para methoxy groups.
  target_ids:
  - antibioticmech:aro-d4b630f1d7
  evidence_ids:
  - chemistry
- check_id: ledger
  name: Input, source, term and history ledger
  command: .venv/bin/python /private/tmp/am-review-session/461-ledger.py > /private/tmp/am-review-session/461-ledger.log
    2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: All 17 hashes and original 13 are intact; all source fields, exact links,
    sole adopted PMID and three chronological histories accounted for.
  target_ids:
  - antibioticmech:aro-d4b630f1d7
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
  summary: Actual catalog query succeeded; no S. formicae dataset is listed. No substitute
    species or phenotype inference was used.
  target_ids:
  - antibioticmech:aro-d4b630f1d7
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
  - antibioticmech:aro-d4b630f1d7
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
  - antibioticmech:aro-d4b630f1d7
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
  - antibioticmech:aro-d4b630f1d7
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
  - antibioticmech:aro-d4b630f1d7
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
  - antibioticmech:aro-d4b630f1d7
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
  - antibioticmech:aro-d4b630f1d7
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
  - antibioticmech:aro-d4b630f1d7
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
  - antibioticmech:aro-d4b630f1d7
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
  - antibioticmech:aro-d4b630f1d7
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/formicamycin-f.yaml
  locator: Entire native YAML
  accessed_at: '2026-10-21T16:41:03Z'
  support: supports
  summary: One neutral formicamycin F, C30H27Cl3O8, MINTED ARO identity and two configured
    tetrahedral centers. No synonyms, quantitative activity, molecular targets, resistance
    edges, producers, clinical claims or causal graphs are present. The definition
    explicitly names formicamycin congeners.
- evidence_id: owners
  kind: database
  reference: Maintained ARO/PubChem extraction and seeding lane
  locator: 461-raw-rows.json; 461-source-audit.json; actual extractor/seeder/enrichment
    sections
  accessed_at: '2026-10-21T16:41:03Z'
  support: supports
  summary: The frozen ARO row supplies the family definition, PMID33440167 and broad
    polyketide class; PubChem CID146684586 supplies the recorded graph. The source
    mint is reproduced. All three chronological seeded/reseeded histories and 17 original/expanded
    input hashes are coherent. ChEBI is an exact external structure cross-reference,
    not the native PubChem owner.
  snapshot_sha256: e35881a1bd729f202c499788bfcb151a9fda91d5fb3b36f8dc8ed59b17f34b59
- evidence_id: chemistry
  kind: validation
  reference: CHEBI:219466; PubChem CID146684586; CHEMBL4641739
  locator: 461-authority-chemistry.json; 461-chebi.json/.mol; 461-pc.json; 461-chembl.json
  accessed_at: '2026-10-21T16:41:03Z'
  support: supports
  summary: Native SMILES/InChI, ChEBI SMILES/InChI/molfile, PubChem SMILES/InChI and
    ChEMBL SMILES give identical UOFYXWHFYPFLPH-HZAQMHFWSA-N, C30H27Cl3O8, charge
    zero and two R,R centers with reciprocal chiral graph matches. The original drawing
    independently matches the chlorination and two pendant methoxy groups. Native
    average and monoisotopic masses agree at recorded precision.
  snapshot_sha256: df2f310ace3c0a3a681f32c71396c8d173e7e86297cd8f138f7e9fae20ab0982
- evidence_id: aro
  kind: authority
  reference: ARO:3007589; ARO:3007574; ARO:3005171
  locator: 461-aro-blocks.json, extracted from current official 426-current-aro.obo
  accessed_at: '2026-10-21T16:41:03Z'
  support: supports
  summary: The exact current ARO term repeats the native definition, PMID and three
    external links. The parent chain leads through formicamycin to polyketide with
    antibiotic activity. Original biosynthetic and isolated-antibacterial evidence
    supports that broad class. No native grounding-status promotion follows merely
    from present ChEBI availability.
  snapshot_sha256: e5a3dd1ff7896498c876db73f6614bd984536e406fbe2d19e5b7e7d26da83029
- evidence_id: identity
  kind: primary_source
  reference: PMID:28507698; DOI:10.1039/c6sc04265a
  locator: Original main isolation and stereochemistry sections, Figure1 visually
    read; SI pp37–38 compound9 and original drawing
  accessed_at: '2026-10-21T16:41:03Z'
  support: supports
  summary: Exact formicamycin F is compound 9, isolated as 3 mg from S. formicae KY5.
    The SI reports C30H27O8Cl3 and observed [M+H]+621.0848, with NMR data and optical
    activity. Combined family NOESY/ECD supported 10R,19R; the 2017 text explicitly
    withheld a definitive formicamycin axial assignment. This is an isolated single
    named congener, not a family mixture.
  snapshot_sha256: c30ad317fb5a4e00f304850ff2bd67d2960f7643f468e35a913bda99aca2f70d
- evidence_id: activity
  kind: primary_source
  reference: PMID:28507698; DOI:10.1039/c6sc04265a
  locator: Original Table1 exact compound9 row and SI1g p56
  accessed_at: '2026-10-21T16:41:03Z'
  support: supports
  summary: F has MICs 5, 20 and 2.5 μM against the laboratory B. subtilis, hospital
    MRSA and VRE E. faecium B16.06226 tests, respectively. The method uses LB without
    NaCl, 1 mL 24-well cultures, starting OD600 0.08–0.15, 40 μL water/methanol stock
    and static 30°C incubation; endpoint is no observable overnight growth. The MRSA
    isolate and B. subtilis lack precise accession identifiers in these methods. These
    experimental MICs are not clinical breakpoints or universal organism susceptibility.
  snapshot_sha256: 741a682eefa78fdbcfb69b76eddd1d23df3e5bffbb60b2c7df34b51d923083d5
- evidence_id: selection
  kind: primary_source
  reference: PMID:28507698
  locator: Resistance-selection Results and SI1g
  accessed_at: '2026-10-21T16:41:03Z'
  support: partial
  summary: Four- and twenty-generation MRSA passage experiments concern compounds
    6, 13 and 15, corresponding to C, J and L. No MIC increase was observed under
    those conditions. This does not establish F-specific resistance-selection behavior;
    the explicitly family-worded native definition remains contextual.
  snapshot_sha256: 741a682eefa78fdbcfb69b76eddd1d23df3e5bffbb60b2c7df34b51d923083d5
- evidence_id: adopted
  kind: primary_source
  reference: PMID:33440167; DOI:10.1016/j.chembiol.2020.12.011
  locator: PMC8062789 complete abstract, introduction, selected regulator Results/Discussion,
    actual Table2 and Bioassays methods
  accessed_at: '2026-10-21T16:41:03Z'
  support: partial
  summary: The sole adopted lead investigates regulation and increased production
    in S. formicae KY5. Its Table2 tests formicamycins J/R/S alongside fasamycins,
    not F. The family antibacterial/resistance introduction points back to Qin2017.
    ForJ, ForGF, ForZ and the putative exporter have producer-cell biosynthetic roles;
    these are not demonstrated F antibacterial targets.
  snapshot_sha256: e55b2fd0ccc375fd9d04e77b0102d8588ed7bab670427d6124477a3d2c38cdae
- evidence_id: revision
  kind: primary_source
  reference: PMID:41988676; DOI:10.1021/acs.jnatprod.6c00145
  locator: 2026 exact revision paragraphs and H axial-crystallography discussion
  accessed_at: '2026-10-21T16:41:03Z'
  support: context_only
  summary: The constitutional revisions specifically include formicamycins B, D and
    I with a single pendant methoxy group. F has both pendant ortho and para methoxy
    groups, so swapping the historical single-methoxy assignment does not alter F.
    The paper demonstrates Sa for sampled crystals, notably H, and proposes broader
    family scope. No F-specific crystal or F constitutional revision was identified
    in these inspected passages.
  snapshot_sha256: 55796020973e571658d3a02c0080a44cff02e2bd6113dbfe0c942357eb04354d
- evidence_id: later-isolation
  kind: primary_source
  reference: PMID:32519857; DOI:10.1021/acs.jnatprod.0c00161
  locator: Original complete publisher abstract; public SI TablesS3/S4 pS6 and FigureS1
    pS7 visually read
  accessed_at: '2026-10-21T16:41:03Z'
  support: partial
  summary: The abstract describes nine new and ten known congeners from Streptomyces
    sp. KIB-1414, with a family activity range. SI compound18 has the same exact F
    substitution pattern and two drawn core centers. The exact main-text F assay row
    was not inspected at this review point; secondary F potency numbers are not adopted.
    SI NMR/drawings do not replace the missing assay methods or table.
  snapshot_sha256: 541af1eb06e40a6048ad327ca0c61a7eae45200a93c2541e98ee7a6a444c6d9b
- evidence_id: adapter
  kind: database
  reference: iModulonDB
  locator: 461-adapter-catalog.txt and 461-adapter-results.json
  accessed_at: '2026-10-21T16:41:03Z'
  support: context_only
  summary: Actual dataset catalog queried before further protein-context investigation.
    No S. formicae dataset is present; listed S. albidoflavus/coelicolor are not substituted.
    Native contains no protein or pathway assertion, and lack of a matching dataset
    is not negative biological evidence.
  snapshot_sha256: c699dc2b41711d1d20635d5941bd524d8caf61ddcdf5199d182d2c293aa3d370
- evidence_id: gates
  kind: validation
  reference: Focused native checks
  locator: 461-focused-results.json; 461-chemistry.json; 461-schema.log; 461-strict.log
  accessed_at: '2026-10-21T16:41:03Z'
  support: supports
  summary: Native chemistry, schema and strict checks all exited zero; independent
    graph and source-ledger commands also exited zero. These checks neither establish
    a molecular target nor promote native scientific status.
  snapshot_sha256: 8e070fa5cb8746710705920310dc8d81d96a373a03488e49d09c09c286dda44a
- evidence_id: search
  kind: search
  reference: Bounded exact-compound source investigation
  locator: 461-owners-search.json; 461-search.json; 461-fetch.json; exact F/KIB-1414
    public search
  accessed_at: '2026-10-21T16:41:03Z'
  support: context_only
  summary: Ignored-inclusive local searches located the actual ARO/PubChem/readiness
    rows. Public searches identified the original2017, adopted2021 and later2020/2026
    sources. Source access and exact-table limits are preserved; no absence of an
    optional native collection is treated as a defect.
  search_scope: rg --no-ignore --hidden over data/raw, curation, conf and scripts
    using exact label, ARO, CID and minted identifier; free exact-name literature
    and official chemical sources.
  snapshot_sha256: f882ce61e88958c8b4e8691b6f934b245de33b5c7873841ad3c12dd7e3dbbca6
assessments:
- assessment_id: identity
  area: identity
  topic: Exact congener and chemical cross-references
  outcome: supported
  summary: All recorded graph and formula fields agree with current exact authorities
    and original compound9, including the F-specific chlorine pattern. No salt, family
    mixture or constitutional revision is substituted.
  target_ids:
  - antibioticmech:aro-d4b630f1d7
  evidence_ids:
  - record
  - identity
  - chemistry
  - revision
- assessment_id: activity
  area: grounding
  topic: Antibacterial filing and polyketide parent
  outcome: supported
  summary: The exact isolated F compound has positive original strain-scoped MICs,
    and typeII polyketide biosynthesis supports the broad parent. Current source labels
    alone are not the activity evidence.
  target_ids:
  - antibioticmech:aro-d4b630f1d7
  evidence_ids:
  - activity
  - identity
  - aro
  - adopted
- assessment_id: definition
  area: scope
  topic: Explicit family definition
  outcome: supported
  summary: The native subject is the congener family. Its context is traceable to
    the adopted source and original literature; exact F potency is separately established,
    while resistance selection remains limited to C/J/L. A future exact-record rewrite
    may make that distinction clearer without claiming a demonstrated current individual-F
    assertion.
  target_ids:
  - antibioticmech:aro-d4b630f1d7
  evidence_ids:
  - adopted
  - selection
  - activity
- assessment_id: stereo
  area: consistency
  topic: Bridgehead configuration and unencoded axis
  outcome: unknown
  summary: Two R,R tetrahedral centers are supported. Standard stored encodings do
    not specify the biaryl Sa axis; the 2026 family inference is not converted to
    an F-specific crystal claim, and omission alone does not imply a mixture.
  target_ids:
  - antibioticmech:aro-d4b630f1d7
  evidence_ids:
  - chemistry
  - identity
  - revision
- assessment_id: mechanism
  area: evidence
  topic: Exact F molecular target
  outcome: unknown
  summary: No native molecular target is asserted and none is established by the inspected
    F identity/growth experiments. Producer regulators and related fasamycin targets
    cannot supply an F mechanism.
  target_ids:
  - antibioticmech:aro-d4b630f1d7
  evidence_ids:
  - record
  - adopted
  - adapter
- assessment_id: later-assay
  area: quantity
  topic: Later KIB-1414 exact assay
  outcome: unknown
  summary: Public original abstract and SI support the later congener context and
    matching drawing; exact later F quantitative assay scope remains unverified, so
    no secondary numbers are adopted.
  target_ids:
  - antibioticmech:aro-d4b630f1d7
  evidence_ids:
  - later-isolation
- assessment_id: provenance
  area: provenance
  topic: Maintained ownership and history
  outcome: supported
  summary: Actual source/extractor/enrichment/seeder owners are captured; original
    13 and all 17 total hashes remain unchanged. All asserted identifiers and adopted
    lead dispositions are accounted for.
  target_ids:
  - antibioticmech:aro-d4b630f1d7
  evidence_ids:
  - owners
  - aro
  - gates
findings: []
actions: []
limitations:
- The 2017 original exact drawing, analytical entry, Table1 row, stereochemistry discussion
  and SI assay methods were inspected; raw NMR spectra were not reprocessed.
- The sole adopted 2021 paper was read at complete abstract and selected relevant
  main sections/Table2/methods depth; all sequencing and supplementary regulator data
  were not independently reanalyzed.
- The later 2020 complete abstract and SI were inspected, but its exact F main assay
  table and methods were not available to this review at draft completion. No secondary
  quantitative value is treated as primary evidence.
- The 2026 source supplies sampled-congener axial evidence and exact B/D/I revisions;
  no F-specific crystallographic result is asserted. Standard native graphs do not
  encode the biaryl axis.
- No exact F resistance-selection experiment or molecular target is established by
  the inspected sources. Absence of optional native target/producer/MIC collections
  is not itself a corrective finding.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Standalone chemistry used the batch019 interpreter against batch047. Native schema/strict,
  ledger and contract use batch047.
- Only scratch review artifacts were authored during this review; no native data,
  maintained source input or curation status changed.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://doi.org/10.1039/c6sc04265a
- https://doi.org/10.1016/j.chembiol.2020.12.011
- https://doi.org/10.1021/acs.jnatprod.0c00161
- https://doi.org/10.1021/acs.jnatprod.6c00145
```
