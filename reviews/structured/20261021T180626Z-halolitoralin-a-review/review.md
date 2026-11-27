# Review of halolitoralin A

- Review: 20261021T180626Z-halolitoralin-a-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T17:48:31Z
- Finished UTC: 2026-10-21T18:06:26Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native peptide graph, formula and source-minted identifier are reproducible and agree with current chemical authorities, with an explicitly unresolved isoleucine side-chain centre. Original synthesis experiments support the stated biological activities, but the native definition cites a secondary review that does not contain the bacterial/earthworm claims. Correct that bounded provenance defect while preserving assay scope and the unresolved biosynthetic and stereochemical details.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position 522; original13 hashes preserved and three actual ARO/PubChem owner inputs appended before scientific assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-12bdf3352c | data/antibiotics/antibacterial/halolitoralin-a.yaml | generated | halolitoralin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-12bdf3352c | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-12bdf3352c | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-12bdf3352c | Actual focused execution exited 0. |
| Structured iModulonDB discovery before optional mechanism follow-up | passed | False | antibioticmech:aro-12bdf3352c | Actual command exited0; ClpC1 gene returned, zero module hits. |
| Structured iModulonDB discovery before optional mechanism follow-up | passed | False | antibioticmech:aro-12bdf3352c | Actual command exited0; ClpC1 gene returned, zero module hits. |
| Initial unnormalized authority graph comparison | failed | False | antibioticmech:aro-12bdf3352c | Initial helper version expected direct amide/imidic-acid substructure equivalence and failed; failed output retained522-authority-check-initial-failed.log. Helper was subsequently refined; this historical command is not claimed reproducible with its later contents. |
| Stereo-preserving authority comparison | passed | False | antibioticmech:aro-12bdf3352c | Eight native/authority encodings retain the same full key/formula and converge after stereo-preserving tautomer normalization; raw comparisons and normalization warnings are retained. |
| Input, citation, term and history audit | passed | False | antibioticmech:aro-12bdf3352c | All16 inputs unchanged, original13 preserved; one adopted review read at exact section and three ordered history events checked. |
| Authoritative full QC | failed | True | antibioticmech:aro-12bdf3352c | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-12bdf3352c | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-12bdf3352c | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-12bdf3352c | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-12bdf3352c | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-12bdf3352c | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-12bdf3352c | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-12bdf3352c | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-12bdf3352c | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Peptide constitution and source stereochemistry

identity: unknown. Targets: antibioticmech:aro-12bdf3352c.

Neutral six-residue constitution and configured alpha centres agree. The unassigned Ile beta centre is preserved as a bounded question; no mixture or wrong configured stereoisomer is demonstrated.

### Exact xrefs and minted provenance

grounding: supported. Targets: antibioticmech:aro-12bdf3352c.

ARO, two-star ChEBI and PubChem identify the same source representation; the missing adopted ChEBI row explains the minted source identifier. No automatic status promotion is justified.

### Definition-source attribution

provenance: concern. Targets: antibioticmech:aro-12bdf3352c.

The imported review PMID does not support the complete definition. The inspected2007 original supplies the actual synthetic-material bacterial, fungal and earthworm evidence.

### Biological activity and assay limits

quantity: supported. Targets: antibioticmech:aro-12bdf3352c.

The2007 primary supports the reported panel activity for synthetic compound8. Disk-diffusion zones and earthworm times remain their original endpoints; no MIC, clinical susceptibility or all-taxa preference is inferred.

### Nonribosomal peptide parent

scope: unknown. Targets: antibioticmech:aro-12bdf3352c.

The parent is broader and reproducible, but ARO itself qualifies the biosynthetic assignment as likely and unknown BGC. No specific NRPS or strain biosynthesis mechanism was verified; retain this distinction.

### ClpC1 functional enrichment

completeness: supported. Targets: antibioticmech:aro-12bdf3352c.

No native mechanism is asserted. Later purified-protein functional stimulation is useful optional evidence, while direct binding, inhibition and cellular killing must not be invented.

## Findings

### F1: Definition citation does not support its bacterial and earthworm claims

minor / open / confirmed; issue key: halolitoralin-a-definition-cites-incomplete-review-source.

PMID34677431 supplies only a secondary fungal halolitoralin paragraph and does not contain the imported bacterial/earthworm statements. The actual original2007 synthesis paper DOI10.2298/JSC0702101D contains those experiments. Correct the definition reference and scope without claiming that the activities are disproved.

## Recommended Actions And Acceptance Checks

### A1

Correct the maintained ARO definition_refs input through a reproducible source-specific correction/transform, then reseed definition_source to the inspected2007 primary DOI. Qualify activity as the synthetic compound8 panel under the reported disk-diffusion and earthworm assays; retain fungal2002 evidence separately if used. Preserve original source provenance, and do not convert zones to MIC or the conditional Ile candidate into a verified correction.

- The definition_source resolves to an inspected source supporting each retained material/activity statement.
- Disk-diffusion zones, earthworm endpoints, unspecified strains and assay limits are accurately distinguished.
- The source-minted identifier and original exact chemical representation are preserved unless a separately sourced stereo curation resolves the Ile centre.
- Focused schema/strict plus actual shared source/reference/history and full QC gates are rerun for any eventual native change.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/halolitoralin-a.yaml; Entire native, all three xrefs, source concept and three history events | supports | The ARO-derived SEEDED/MINTED record contains a neutral cyclic hexapeptide graph, an antibacterial filing and a nonribosomal peptide class. It has no native target, MIC, resistance, structured producer, clinical or causal-graph assertion. Its definition_source is PMID34677431. |
| identity | ARO:3007780;CHEBI:207984;pubchem.compound:139588131;NPA018093; 522-authority-chemistry.json;522-chebi.json/.mol;522-pubchem.json;522-npatlas.json | supports | Native SMILES/InChI, current ChEBI SMILES/InChI/molfile, PubChem SMILES/InChI and supplemental NPAtlas SMILES retain SXVHYPUSAGNSMU-HXZOEFROSA-N and C27H48N6O6. Six alpha centres are configured S and the Ile side-chain centre is unspecified. InChI reconstructs imidic-acid tautomers; normalization retaining sp3/bond stereochemistry yields matching atom-mapped graphs. No mixture or opposite configured isomer follows from the unspecified centre. |
| aro | ARO:3007780;ARO:3007779;ARO:3009657; 522-aro-blocks.json; official426-current-aro.obo SHA d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4 | supports | Current ARO reproduces the exact definition and chemical xrefs. Its family parent calls nonribosomal origin likely and says the biosynthetic cluster is unknown, while the class definition specifically concerns NRPS biosynthesis. The class is a reproducible database assertion; exact NRPS origin is not experimentally established by the inspected papers. |
| adopted | PMID:34677431;DOI:10.3390/md19100530; 522-PMC8539464.xml; exact halolitoralin paragraph, Figure8 locator and reference142;522-source-audit.json | refutes | This adopted publication is a secondary review. Its relevant paragraph discusses C. albicans and T. rubrum and does not contain the native T. mentagrophytes, bacterial or earthworm claims. Its reference142 is a2001 review of marine sponge cyclic peptides, not the2002 isolation or2007 synthesis paper. The PMID resolves, but does not support the full imported definition. |
| isolation | DOI:10.1016/S0040-4039(02)01458-2; Original publisher abstract and graphical-abstract prose;522-2002-openalex.json metadata; direct full-text403 | supports | The original abstract reports A/B/C isolated from Halobacillus litoralis YS3106 fermentation broth and hydrophobic L-amino-acid residues, with family-level moderate antifungal and weak antitumor activity. Full natural-product structural workup and congener assay table were not available; no exact quantitative or beta-stereo assignment is inferred from an unread table. |
| synthesis | DOI:10.2298/JSC0702101D; 522-synthesis2007-publisher.pdf; entire7-page main; actual printed102 TablesI/II,103 Scheme1 and104 L-amino-acid methods visually inspected | supports | The original synthesis uses stated L-amino-acid reagents and cyclizes Leu-Ala-Leu-Ala-Ile-Ala to compound8. Modified Kirby–Bauer testing reports zones at50µg/mL, including22/24mm for E. coli/P. aeruginosa and28/25mm for C. albicans/T. mentagrophytes. These are not MICs or taxon-wide susceptibility. Earthworm paralysis/death tests support the reported anthelmintic observation; strains and full antimicrobial conditions are not specified. The paper contains a strain-number typo and an erroneous seven-residue phrase despite its six-residue scheme. |
| stereo | Conditional L-isoleucine candidate;DOI:10.2298/JSC0702101D; 522-authority-chemistry.json conditional_L_Ile_candidate; native atom2; original Scheme1 and methods | unknown | A conditional beta-S Ile candidate has key SXVHYPUSAGNSMU-BPSSIEEOSA-N. It follows ordinary L-Ile reagent interpretation, but both inspected drawings omit explicit side-chain wedge notation and the original2002 workup was not read. All current authorities inspected retain the unspecified centre. This is a bounded identity question, not a demonstrated wrong isomer or an instruction to overwrite the source structure. |
| mechanism | PMID:38338462;DOI:10.3390/molecules29030720; 522-PMC10856564.xml/.txt; entire main and references; actual522-2024-fig2.jpg and522-2024-fig5.jpg visually inspected | supports | The original isolates halolitoralin A as compound3 from Streptomyces aureus VTCC43181 and tests recombinant M. tuberculosis ClpC1. Figure5 and Results show mild ATPase stimulation, not inhibition, although the title uses inhibition. Methods measure released phosphate with BIOMOL Green; the Results radioactive-ATP description differs. No direct binding-site assay, cellular TB MIC or proteolysis assay for halolitoralin A is demonstrated. The abstract misnumbers it as compound1; main/figures consistently identify3. |
| adapter | kg-microbe-sources imodulondb; 522-adapter-datasets.json;522-adapter-clpc1.txt | supports | Before reading the optional ClpC1 original, datasets and m_tuberculosis/modulome clpC1 searches returned0. Gene Rv3596c is catalogued, with zero matching modules; no module summary was applicable. Catalog membership is not target binding or an antibacterial phenotype. |
| owners | data/raw/aro_antibiotics.tsv;data/raw/pubchem_structures.tsv;scripts/enrich_pubchem_structures.py;scripts/extract_source_inventory.py;scripts/seed_from_sources.py; 522-raw-rows.json;522-source-audit.json;522-owners-search.json; resolve_identity and definition_refs projection | supports | The native definition/reference are copied from the ARO row and structure from PubChem enrichment. The exact minted ARO hash reproduces. An ignored-inclusive search found no adopted ChEBI207984 row or curator override, explaining MINTED despite a current two-star external ChEBI record. Actual owners were captured before assessment and all16 hashes remain unchanged. |
| search | Public halolitoralin original-literature search; 522-discovery.json;522-fetch*.json;522-source-audit.json | supports | All nine EuropePMC discovery titles were screened; the adopted review, original2007 synthesis and original2024 functional study were inspected at declared depth. Original2002 full text remained inaccessible. This bounded search does not establish that no additional natural-product stereo or biosynthesis evidence exists. |

## Limits And Additional Notes

- The2002 discovery original was available only as publisher abstract/graphical-abstract prose; full main and natural-product stereochemical workup were not read.
- Current ChEBI, PubChem and NPAtlas all omit the Ile beta configuration. L-Ile synthesis wording motivates a conditional beta-S candidate but does not independently validate the natural material or compel a graph edit.
- The2007 main and rendered tables/scheme were read. Antimicrobial strain identifiers, complete incubation/inoculum details and replicate/error reporting are absent from the inspected assay section; zones are not MICs. Source typos are not silently propagated.
- Only the exact relevant paragraph/reference of the broad adopted2021 review was read beyond its complete abstract. Its reference142 mismatch and missing bacterial/earthworm statements are preserved.
- The2024 main and actualFigures2/5 were read, not the supplement. Source numbering and ATP-assay-description inconsistencies prevent overstating binding, whole-cell killing or a complete causal mechanism.
- The initial unnormalized chemistry helper failed on amide/imidic-acid graph representations; refined stereo-preserving normalization resolves all compared graphs. Enumeration reached a transform limit for some inputs, so convergence of these encodings is reported rather than an exhaustive tautomer search.
- Nonribosomal biosynthetic origin remains a database inference; exact biosynthetic genes were not established in the inspected sources.
- Required shared corpus checks and the platform SciPy QC failure are integrated by the coordinating finalizer; focused passes do not substitute for the full failed gate.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native record, source inventory or saved bundle was edited. Scratch draft and evidence are handed to the independent coordinating reviewer for final saving.
- Standalone chemistry used019 against053; schema/strict, ledger and contract used053. Initial13 inputs were preserved and three actual owner inputs appended.
- Temporary helper imports of unavailable bs4 failed; standard-library XML processing succeeded. Public PDF retrieval timed out at DOISerbia but succeeded at the official journal archive.
- The structured adapter ran before inspecting the discovered ClpC1 primary mechanism; gene catalog output was not treated as an experiment.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T180626Z-halolitoralin-a-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of halolitoralin A
started_at: '2026-10-21T17:48:31Z'
finished_at: '2026-10-21T18:06:26Z'
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
summary: The native peptide graph, formula and source-minted identifier are reproducible
  and agree with current chemical authorities, with an explicitly unresolved isoleucine
  side-chain centre. Original synthesis experiments support the stated biological
  activities, but the native definition cites a secondary review that does not contain
  the bacterial/earthworm claims. Correct that bounded provenance defect while preserving
  assay scope and the unresolved biosynthetic and stereochemical details.
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
  - path: data/antibiotics/antibacterial/halolitoralin-a.yaml
    sha256: 7fe9bcec20d07373de60320c50eaab2ea436d037e6fef7359fd91efb08d9ac9a
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
targets:
- target_id: antibioticmech:aro-12bdf3352c
  path: data/antibiotics/antibacterial/halolitoralin-a.yaml
  label: halolitoralin A
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, definition, class and equivalence
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact chemical representation
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Native generation and identity resolution
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Source and class policy
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion decisions
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position 522; original13 hashes preserved and
    three actual ARO/PubChem owner inputs appended before scientific assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-12bdf3352c
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-12bdf3352c
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    522
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-12bdf3352c
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/halolitoralin-a.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-12bdf3352c
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/halolitoralin-a.yaml --out /private/tmp/am-review-session/522-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-datasets
  name: Structured iModulonDB discovery before optional mechanism follow-up
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Actual command exited0; ClpC1 gene returned, zero module hits.
  target_ids:
  - antibioticmech:aro-12bdf3352c
- check_id: adapter-clpc1
  name: Structured iModulonDB discovery before optional mechanism follow-up
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism m_tuberculosis --dataset modulome --query
    clpC1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Actual command exited0; ClpC1 gene returned, zero module hits.
  target_ids:
  - antibioticmech:aro-12bdf3352c
- check_id: authority-initial
  name: Initial unnormalized authority graph comparison
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/522-authority-check.py
    > /private/tmp/am-review-session/522-authority-check.log 2>&1
  status: failed
  required: false
  exit_code: 1
  expected_exit_code: 0
  summary: Initial helper version expected direct amide/imidic-acid substructure equivalence
    and failed; failed output retained522-authority-check-initial-failed.log. Helper
    was subsequently refined; this historical command is not claimed reproducible
    with its later contents.
  target_ids:
  - antibioticmech:aro-12bdf3352c
- check_id: authority
  name: Stereo-preserving authority comparison
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/522-authority-check.py
    > /private/tmp/am-review-session/522-authority-check.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Eight native/authority encodings retain the same full key/formula and converge
    after stereo-preserving tautomer normalization; raw comparisons and normalization
    warnings are retained.
  target_ids:
  - antibioticmech:aro-12bdf3352c
- check_id: ledger
  name: Input, citation, term and history audit
  command: .venv/bin/python /private/tmp/am-review-session/522-ledger.py > /private/tmp/am-review-session/522-ledger.log
    2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: All16 inputs unchanged, original13 preserved; one adopted review read at
    exact section and three ordered history events checked.
  target_ids:
  - antibioticmech:aro-12bdf3352c
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-12bdf3352c
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
  - antibioticmech:aro-12bdf3352c
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
  - antibioticmech:aro-12bdf3352c
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
  - antibioticmech:aro-12bdf3352c
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
  - antibioticmech:aro-12bdf3352c
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
  - antibioticmech:aro-12bdf3352c
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
  - antibioticmech:aro-12bdf3352c
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
  - antibioticmech:aro-12bdf3352c
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
  - antibioticmech:aro-12bdf3352c
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/halolitoralin-a.yaml
  locator: Entire native, all three xrefs, source concept and three history events
  accessed_at: '2026-10-21T18:02:35Z'
  support: supports
  summary: The ARO-derived SEEDED/MINTED record contains a neutral cyclic hexapeptide
    graph, an antibacterial filing and a nonribosomal peptide class. It has no native
    target, MIC, resistance, structured producer, clinical or causal-graph assertion.
    Its definition_source is PMID34677431.
- evidence_id: identity
  kind: validation
  reference: ARO:3007780;CHEBI:207984;pubchem.compound:139588131;NPA018093
  locator: 522-authority-chemistry.json;522-chebi.json/.mol;522-pubchem.json;522-npatlas.json
  accessed_at: '2026-10-21T18:02:35Z'
  support: supports
  summary: Native SMILES/InChI, current ChEBI SMILES/InChI/molfile, PubChem SMILES/InChI
    and supplemental NPAtlas SMILES retain SXVHYPUSAGNSMU-HXZOEFROSA-N and C27H48N6O6.
    Six alpha centres are configured S and the Ile side-chain centre is unspecified.
    InChI reconstructs imidic-acid tautomers; normalization retaining sp3/bond stereochemistry
    yields matching atom-mapped graphs. No mixture or opposite configured isomer follows
    from the unspecified centre.
  snapshot_sha256: 3d1d841e2a653ff0a9761c30ba3c13eb0c5fdcaee37bb6f1720745282a9c0aaa
- evidence_id: aro
  kind: database
  reference: ARO:3007780;ARO:3007779;ARO:3009657
  locator: 522-aro-blocks.json; official426-current-aro.obo SHA d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
  accessed_at: '2026-10-21T18:02:35Z'
  support: supports
  summary: Current ARO reproduces the exact definition and chemical xrefs. Its family
    parent calls nonribosomal origin likely and says the biosynthetic cluster is unknown,
    while the class definition specifically concerns NRPS biosynthesis. The class
    is a reproducible database assertion; exact NRPS origin is not experimentally
    established by the inspected papers.
  snapshot_sha256: 8a4d58fd91111be0d9bb53447a55c47a0ccfc70d5c14a34408a86ffb67b0e158
- evidence_id: adopted
  kind: authority
  reference: PMID:34677431;DOI:10.3390/md19100530
  locator: 522-PMC8539464.xml; exact halolitoralin paragraph, Figure8 locator and
    reference142;522-source-audit.json
  accessed_at: '2026-10-21T18:02:35Z'
  support: refutes
  summary: This adopted publication is a secondary review. Its relevant paragraph
    discusses C. albicans and T. rubrum and does not contain the native T. mentagrophytes,
    bacterial or earthworm claims. Its reference142 is a2001 review of marine sponge
    cyclic peptides, not the2002 isolation or2007 synthesis paper. The PMID resolves,
    but does not support the full imported definition.
  snapshot_sha256: 40280f418211135d9c16b44d8cd4d950e58167af65b8486917c8cce8d0143457
- evidence_id: isolation
  kind: primary_source
  reference: DOI:10.1016/S0040-4039(02)01458-2
  locator: Original publisher abstract and graphical-abstract prose;522-2002-openalex.json
    metadata; direct full-text403
  accessed_at: '2026-10-21T18:02:35Z'
  support: supports
  summary: The original abstract reports A/B/C isolated from Halobacillus litoralis
    YS3106 fermentation broth and hydrophobic L-amino-acid residues, with family-level
    moderate antifungal and weak antitumor activity. Full natural-product structural
    workup and congener assay table were not available; no exact quantitative or beta-stereo
    assignment is inferred from an unread table.
- evidence_id: synthesis
  kind: primary_source
  reference: DOI:10.2298/JSC0702101D
  locator: 522-synthesis2007-publisher.pdf; entire7-page main; actual printed102 TablesI/II,103
    Scheme1 and104 L-amino-acid methods visually inspected
  accessed_at: '2026-10-21T18:02:35Z'
  support: supports
  summary: The original synthesis uses stated L-amino-acid reagents and cyclizes Leu-Ala-Leu-Ala-Ile-Ala
    to compound8. Modified Kirby–Bauer testing reports zones at50µg/mL, including22/24mm
    for E. coli/P. aeruginosa and28/25mm for C. albicans/T. mentagrophytes. These
    are not MICs or taxon-wide susceptibility. Earthworm paralysis/death tests support
    the reported anthelmintic observation; strains and full antimicrobial conditions
    are not specified. The paper contains a strain-number typo and an erroneous seven-residue
    phrase despite its six-residue scheme.
  snapshot_sha256: 2b25f82da7fc5a0e1e649db1f7da4ee1c481a688c167072da462d1ecfa017d4f
- evidence_id: stereo
  kind: validation
  reference: Conditional L-isoleucine candidate;DOI:10.2298/JSC0702101D
  locator: 522-authority-chemistry.json conditional_L_Ile_candidate; native atom2;
    original Scheme1 and methods
  accessed_at: '2026-10-21T18:02:35Z'
  support: unknown
  summary: A conditional beta-S Ile candidate has key SXVHYPUSAGNSMU-BPSSIEEOSA-N.
    It follows ordinary L-Ile reagent interpretation, but both inspected drawings
    omit explicit side-chain wedge notation and the original2002 workup was not read.
    All current authorities inspected retain the unspecified centre. This is a bounded
    identity question, not a demonstrated wrong isomer or an instruction to overwrite
    the source structure.
  snapshot_sha256: 3d1d841e2a653ff0a9761c30ba3c13eb0c5fdcaee37bb6f1720745282a9c0aaa
- evidence_id: mechanism
  kind: primary_source
  reference: PMID:38338462;DOI:10.3390/molecules29030720
  locator: 522-PMC10856564.xml/.txt; entire main and references; actual522-2024-fig2.jpg
    and522-2024-fig5.jpg visually inspected
  accessed_at: '2026-10-21T18:02:35Z'
  support: supports
  summary: The original isolates halolitoralin A as compound3 from Streptomyces aureus
    VTCC43181 and tests recombinant M. tuberculosis ClpC1. Figure5 and Results show
    mild ATPase stimulation, not inhibition, although the title uses inhibition. Methods
    measure released phosphate with BIOMOL Green; the Results radioactive-ATP description
    differs. No direct binding-site assay, cellular TB MIC or proteolysis assay for
    halolitoralin A is demonstrated. The abstract misnumbers it as compound1; main/figures
    consistently identify3.
  snapshot_sha256: e7c6687b069b1825ef9e057a8c0252a75f4c66b67c881170068444f1b059c842
- evidence_id: adapter
  kind: search
  reference: kg-microbe-sources imodulondb
  locator: 522-adapter-datasets.json;522-adapter-clpc1.txt
  accessed_at: '2026-10-21T18:02:35Z'
  support: supports
  summary: Before reading the optional ClpC1 original, datasets and m_tuberculosis/modulome
    clpC1 searches returned0. Gene Rv3596c is catalogued, with zero matching modules;
    no module summary was applicable. Catalog membership is not target binding or
    an antibacterial phenotype.
  search_scope: Covered M. tuberculosis/modulome dataset, exact clpC1 query after
    dataset discovery.
  snapshot_sha256: e1af3c57901a343d421e6966295927e60cdb24e3d5aee99db36206b46db9cda7
- evidence_id: owners
  kind: validation
  reference: data/raw/aro_antibiotics.tsv;data/raw/pubchem_structures.tsv;scripts/enrich_pubchem_structures.py;scripts/extract_source_inventory.py;scripts/seed_from_sources.py
  locator: 522-raw-rows.json;522-source-audit.json;522-owners-search.json; resolve_identity
    and definition_refs projection
  accessed_at: '2026-10-21T18:02:35Z'
  support: supports
  summary: The native definition/reference are copied from the ARO row and structure
    from PubChem enrichment. The exact minted ARO hash reproduces. An ignored-inclusive
    search found no adopted ChEBI207984 row or curator override, explaining MINTED
    despite a current two-star external ChEBI record. Actual owners were captured
    before assessment and all16 hashes remain unchanged.
  snapshot_sha256: 4752cfea121dbb73ca2aa93f0b68543473f7c1d1231c7060980fe5973ddf31e5
- evidence_id: search
  kind: search
  reference: Public halolitoralin original-literature search
  locator: 522-discovery.json;522-fetch*.json;522-source-audit.json
  accessed_at: '2026-10-21T18:02:35Z'
  support: supports
  summary: All nine EuropePMC discovery titles were screened; the adopted review,
    original2007 synthesis and original2024 functional study were inspected at declared
    depth. Original2002 full text remained inaccessible. This bounded search does
    not establish that no additional natural-product stereo or biosynthesis evidence
    exists.
  search_scope: Ignored-inclusive local raw/curation/conf/scripts/src; EuropePMC halolitoralin
    query9 hits; public publisher/OpenAlex and official journal/PMC follow-up for2002,2007,2024.
  snapshot_sha256: 4752cfea121dbb73ca2aa93f0b68543473f7c1d1231c7060980fe5973ddf31e5
assessments:
- assessment_id: structure
  area: identity
  topic: Peptide constitution and source stereochemistry
  outcome: unknown
  summary: Neutral six-residue constitution and configured alpha centres agree. The
    unassigned Ile beta centre is preserved as a bounded question; no mixture or wrong
    configured stereoisomer is demonstrated.
  target_ids:
  - antibioticmech:aro-12bdf3352c
  evidence_ids:
  - identity
  - synthesis
  - stereo
  - isolation
- assessment_id: grounding
  area: grounding
  topic: Exact xrefs and minted provenance
  outcome: supported
  summary: ARO, two-star ChEBI and PubChem identify the same source representation;
    the missing adopted ChEBI row explains the minted source identifier. No automatic
    status promotion is justified.
  target_ids:
  - antibioticmech:aro-12bdf3352c
  evidence_ids:
  - identity
  - aro
  - owners
- assessment_id: citation
  area: provenance
  topic: Definition-source attribution
  outcome: concern
  summary: The imported review PMID does not support the complete definition. The
    inspected2007 original supplies the actual synthetic-material bacterial, fungal
    and earthworm evidence.
  target_ids:
  - antibioticmech:aro-12bdf3352c
  evidence_ids:
  - record
  - adopted
  - synthesis
  - owners
- assessment_id: activity
  area: quantity
  topic: Biological activity and assay limits
  outcome: supported
  summary: The2007 primary supports the reported panel activity for synthetic compound8.
    Disk-diffusion zones and earthworm times remain their original endpoints; no MIC,
    clinical susceptibility or all-taxa preference is inferred.
  target_ids:
  - antibioticmech:aro-12bdf3352c
  evidence_ids:
  - synthesis
  - record
- assessment_id: biosynthesis
  area: scope
  topic: Nonribosomal peptide parent
  outcome: unknown
  summary: The parent is broader and reproducible, but ARO itself qualifies the biosynthetic
    assignment as likely and unknown BGC. No specific NRPS or strain biosynthesis
    mechanism was verified; retain this distinction.
  target_ids:
  - antibioticmech:aro-12bdf3352c
  evidence_ids:
  - aro
  - isolation
  - mechanism
- assessment_id: optional-target
  area: completeness
  topic: ClpC1 functional enrichment
  outcome: supported
  summary: No native mechanism is asserted. Later purified-protein functional stimulation
    is useful optional evidence, while direct binding, inhibition and cellular killing
    must not be invented.
  target_ids:
  - antibioticmech:aro-12bdf3352c
  evidence_ids:
  - mechanism
  - adapter
  - record
findings:
- finding_id: F1
  issue_key: halolitoralin-a-definition-cites-incomplete-review-source
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Definition citation does not support its bacterial and earthworm claims
  description: PMID34677431 supplies only a secondary fungal halolitoralin paragraph
    and does not contain the imported bacterial/earthworm statements. The actual original2007
    synthesis paper DOI10.2298/JSC0702101D contains those experiments. Correct the
    definition reference and scope without claiming that the activities are disproved.
  target_ids:
  - antibioticmech:aro-12bdf3352c
  field_paths:
  - definition_source
  - definition
  evidence_ids:
  - record
  - adopted
  - synthesis
  - owners
  rule_id: 'review-checklist: nearest source must support exact claim and material'
  normalization_reason: 'Minor non-blocking provenance defect: original experiments
    support the activity, but the imported citation does not; no wrong chemical identity
    is established.'
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted definition and definition_refs
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reproducible ARO definition-reference extraction or source-specific correction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition_source projection
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-12bdf3352c
  description: Correct the maintained ARO definition_refs input through a reproducible
    source-specific correction/transform, then reseed definition_source to the inspected2007
    primary DOI. Qualify activity as the synthetic compound8 panel under the reported
    disk-diffusion and earthworm assays; retain fungal2002 evidence separately if
    used. Preserve original source provenance, and do not convert zones to MIC or
    the conditional Ile candidate into a verified correction.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted definition and definition_refs
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reproducible ARO definition-reference extraction or source-specific correction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition_source projection
  generator: scripts/extract_source_inventory.py and scripts/seed_from_sources.py
  acceptance_checks:
  - The definition_source resolves to an inspected source supporting each retained
    material/activity statement.
  - Disk-diffusion zones, earthworm endpoints, unspecified strains and assay limits
    are accurately distinguished.
  - The source-minted identifier and original exact chemical representation are preserved
    unless a separately sourced stereo curation resolves the Ile centre.
  - Focused schema/strict plus actual shared source/reference/history and full QC
    gates are rerun for any eventual native change.
limitations:
- The2002 discovery original was available only as publisher abstract/graphical-abstract
  prose; full main and natural-product stereochemical workup were not read.
- Current ChEBI, PubChem and NPAtlas all omit the Ile beta configuration. L-Ile synthesis
  wording motivates a conditional beta-S candidate but does not independently validate
  the natural material or compel a graph edit.
- The2007 main and rendered tables/scheme were read. Antimicrobial strain identifiers,
  complete incubation/inoculum details and replicate/error reporting are absent from
  the inspected assay section; zones are not MICs. Source typos are not silently propagated.
- Only the exact relevant paragraph/reference of the broad adopted2021 review was
  read beyond its complete abstract. Its reference142 mismatch and missing bacterial/earthworm
  statements are preserved.
- The2024 main and actualFigures2/5 were read, not the supplement. Source numbering
  and ATP-assay-description inconsistencies prevent overstating binding, whole-cell
  killing or a complete causal mechanism.
- The initial unnormalized chemistry helper failed on amide/imidic-acid graph representations;
  refined stereo-preserving normalization resolves all compared graphs. Enumeration
  reached a transform limit for some inputs, so convergence of these encodings is
  reported rather than an exhaustive tautomer search.
- Nonribosomal biosynthetic origin remains a database inference; exact biosynthetic
  genes were not established in the inspected sources.
- Required shared corpus checks and the platform SciPy QC failure are integrated by
  the coordinating finalizer; focused passes do not substitute for the full failed
  gate.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native record, source inventory or saved bundle was edited. Scratch draft and
  evidence are handed to the independent coordinating reviewer for final saving.
- Standalone chemistry used019 against053; schema/strict, ledger and contract used053.
  Initial13 inputs were preserved and three actual owner inputs appended.
- Temporary helper imports of unavailable bs4 failed; standard-library XML processing
  succeeded. Public PDF retrieval timed out at DOISerbia but succeeded at the official
  journal archive.
- The structured adapter ran before inspecting the discovered ClpC1 primary mechanism;
  gene catalog output was not treated as an experiment.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
