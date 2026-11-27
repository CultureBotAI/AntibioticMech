# Review of arborcandin C

- Review: 20261021T091440Z-arborcandin-c-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:07:58Z
- Finished UTC: 2026-10-21T09:14:40Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The seeded planar structure reproduces current PubChem, but all 13 stereocenters are unset despite seven established assignments. Primary literature supports antifungal activity and distinguishes arborcandins from echinocandins, contradicting the native antibacterial filing and structural class. Exact biochemical and genetic evidence offers bounded mechanism enrichment.

## Scope And Provenance

Whole ARO-derived record, adopted definition and class citations, exact chemical identity, current source assertions, primary production/structure/target literature and all available indexed lead abstracts.

Selection: Path-ordered queue index 106; exact record and maintained ARO owners hashed before scientific judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-de2f58b0cc | data/antibiotics/antibacterial/arborcandin-c.yaml | generated | arborcandin C |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented per-record schema check | passed | True | antibioticmech:aro-de2f58b0cc | Exit 0; no issues. |
| Documented strict schema check | passed | True | antibioticmech:aro-de2f58b0cc | Exit 0; zero ERROR rows. |
| Native and PubChem chemistry | passed | False | antibioticmech:aro-de2f58b0cc | Exit 0; planar encodings, formula, mass, charge and mint agree; all 13 centers unspecified. |
| Cached ARO and current CARD/ChEBI | passed | False | antibioticmech:aro-de2f58b0cc | Exit 0; identifiers and adopted source assertions reproduce, including the scientifically problematic class. |
| Native source adapter before web | passed | False | antibioticmech:aro-de2f58b0cc | Exit 0; no fungal organism dataset available; no applicable gene query. |
| Authoritative full QC | failed | True | antibioticmech:aro-de2f58b0cc | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-de2f58b0cc | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-de2f58b0cc | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-de2f58b0cc | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-de2f58b0cc | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-de2f58b0cc | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-de2f58b0cc | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-de2f58b0cc | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-de2f58b0cc | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact natural-product representation

identity: concern. Targets: antibioticmech:aro-de2f58b0cc.

Planar identity is consistent; established partial stereochemistry is omitted.

### Activity and structural classes

grounding: concern. Targets: antibioticmech:aro-de2f58b0cc.

Fungal activity supports ANTIFUNGAL; cyclic decapeptide is not echinocandin structural identity.

### Definition and target interpretation

evidence: supported. Targets: antibioticmech:aro-de2f58b0cc.

Definition-level synthase inhibition is supported; genetics can enrich evidence without claiming direct binding.

### Adopted sources and current databases

provenance: supported. Targets: antibioticmech:aro-de2f58b0cc.

Source reproduction is transparent; upstream repetition does not override primary structure evidence.

### Primary target, producer and phenotype fields

completeness: supported. Targets: antibioticmech:aro-de2f58b0cc.

Optional primary enrichment is available; no isolated missing optional field is treated as a defect.

### Expression adapter applicability

scope: not_applicable. Targets: antibioticmech:aro-de2f58b0cc.

No fungal dataset in executed catalog.

### Focused checks

schema: supported. Targets: antibioticmech:aro-de2f58b0cc.

Native schema and strict pass.

## Findings

### F1: Antibacterial fallback conflicts with exact fungal activity

major / open / confirmed; issue key: aro-3009172-arborcandin-c-antifungal-class.

Native definition and its primary citation describe antifungal action, but no explicit adjudication prevents the default ANTIBACTERIAL filing.

### F2: Echinocandin structural class conflicts with the original structure

major / open / confirmed; issue key: aro-3009172-arborcandin-c-echinocandin-class.

Native parent and structural class reproduce an upstream assertion, but arborcandin C is a distinct cyclic decapeptide rather than the echinocandin hexapeptide scaffold. Shared glucan-synthase inhibition cannot establish structural identity.

### F3: Seven established stereocenters are omitted

major / open / confirmed; issue key: aro-3009172-arborcandin-c-known-stereochemistry-omitted.

All 13 native centers are unset. The primary structural assignment establishes five amino-acid configurations covering seven centers, while explicitly retaining uncertainty at the other six.

### F4: Exact primary mechanism and phenotype evidence can enrich the seed

informational / open / confirmed; issue key: aro-3009172-arborcandin-c-primary-enrichment.

Original fungal production, biochemical inhibition and controlled FKS1 genetics provide optional claim-level additions.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate the activity class through the existing maintained override.

- Add exact ARO:3009172: ANTIFUNGAL under conf/sources.yaml aro_definition_overrides with source rationale; preserve source-priority rules.
- Reseed using maintained tooling, confirm resulting class/path and corpus reproducibility, and run required native gates.

### A2

Repair the inherited structural-class relationship reproducibly.

- Correct upstream ARO membership or implement an explicit maintained source-level exclusion/override supported by the primary cyclic-decapeptide structure. Current fetched CARD still repeats the error; a refresh alone is not a demonstrated fix.
- Keep parent_compounds and structural_class/id mutually consistent. Use a validated applicable structural term or leave unsupported class grounding unset; do not invent a CURIE or confuse common target with class.
- Re-extract/reseed and verify exact structure/class plus native schema,strict,term,reference,history and corpus checks.

### A3

Preserve known partial stereochemistry without inventing the unresolved centers.

- Map Asn-1 D, Asn-2 L, Ala D, Thr-1 D-allo and Thr-2 L from the original numbered residues onto the maintained structure input; independently verify all seven atom assignments.
- Leave gamma-hydroxy-Gln and both long-chain Xaa residues unresolved unless stronger exact-compound evidence is obtained. Unspecified is not racemic.
- Regenerate consistent SMILES/InChI/key with unchanged connectivity/formula, retain provenance and exact PubChem specificity caveat, then pass chemical and native reproducibility gates.

### A4

Optionally add narrow primary mechanism, resistance and production evidence.

- Separate enzyme inhibition from whole-cell growth and genetic resistance; FKS1 substitutions support target involvement without a direct binding-site claim.
- Preserve Candida/Aspergillus/Saccharomyces strain,medium and endpoint boundaries. Do not encode Aspergillus morphological MEC as MIC or pool family activity ranges into arborcandin C.
- Represent cultured SANK17397 fungus as producer only with defensible organism grounding; plant collection source is not plant biosynthesis.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/arborcandin-c.yaml; Whole native YAML including three seed/reseed events | supports | ARO-derived SEEDED/MINTED record has fungal definition, ANTIBACTERIAL filing, echinocandin parent/class and wholly unspecified stereochemistry. No native primary target, resistance, producer or activity objects are asserted. |
| inventory | conf/sources.yaml;scripts/seed_from_sources.py;data/raw/aro_antibiotics.tsv;data/raw/pubchem_structures.tsv; classify() and generated structural-class selection; 106 source-row JSON files | supports | ARO class and supplemental PubChem graph propagate into the seed. With no decisive roles or class map, the default files this record ANTIBACTERIAL. Existing aro_definition_overrides supports a per-compound adjudication; structural-class and chemistry repairs require maintained source/transform support. |
| sources | https://card.mcmaster.ca/ontology/48017;https://www.ebi.ac.uk/chebi/CHEBI:217490; 106-card.html;106-ols.json;106-source-check.json | supports | Fetched current CARD repeats ARO:3007496 echinocandin membership, PMID11132955 and PubChem9941831; cached ARO agrees. Current ChEBI is a nonobsolete exact-name record. Reproducing database assertions does not resolve conflicts with the original structure report. |
| chemistry | PubChem CID9941831;RDKit; 106-chemistry.py;106-chemistry.json;106-pubchem.json | supports | Native encodings and current PubChem agree on neutral C59H105N13O18 and AHATVKJRQUTSJV-UHFFFAOYSA-N, one connected molecule and all 13 tetrahedral centers unset. This validates source reproduction, not completeness of natural-product stereochemistry. |
| biology | PMID:11132955; DOI:10.7164/antibiotics.53.1108;106-primary2000.pdf complete main text and Tables1–4 | supports | Purified arborcandin C from fungal SANK17397 broth inhibits C.albicans/A.fumigatus glucan synthase noncompetitively. Candida growth inhibition and killing are distinct endpoints. A.fumigatus morphological MEC is not complete-growth MIC: the latter exceeds 64 micrograms/ml. The producing strain was isolated from a plant; that does not identify the plant as producer. The paper explicitly distinguishes the scaffold from echinocandins. |
| structure | DOI:10.7164/antibiotics.56.1024; 106-primary2003.pdf complete main text; original p1027 Figures1–2 visually inspected; pp1028–1030 assignments | refutes | NMR/MS establish the ten-residue ring and side chains. Advanced Marfey analysis plus selective Asn reduction and Thr coupling/NOE assign Asn-1 D, Asn-2 L, Ala D, Thr-1 D-allo and Thr-2 L: seven centers. The remaining centers in gamma-hydroxy-Gln, Xaa-1 and Xaa-2 are explicitly unresolved. Discussion contrasts these cyclic peptides with echinocandin hexapeptides. |
| genetics | PMID:14693557; DOI:10.1128/AAC.48.1.319-322.2004;publisher full main text and Tables1–3 inspected | supports | S.cerevisiae FKS1 N470K or L642S constructs confer selective cellular and glucan-synthase resistance to arborcandin C. Controlled fks1 deletion/FKS2 repression and replacement experiments support Fks1 involvement. Cell-growth IC50, complete-inhibition MIC and enzyme IC50 are separate. This is genetic/biochemical target evidence; direct binding and a precise contact site were left for future work. |
| leads | PMID:11132955;PMID:4613708 and indexed arborcandin literature; 106-core.json;106-literature.json;106-lead-dispositions.json | context_only | All adopted citation records and available abstracts were checked. PMID4613708 concerns echinocandin B, has no available abstract and cannot establish arborcandin identity. Ten broader search hits were individually scoped; unrelated safety/environmental studies and echinocandin-specific findings were not transferred. |
| adapter | Native iModulonDB adapter; 106-imodulondb-datasets.txt | context_only | Catalog executed before open web research; fungal organisms implicated here are outside listed dataset coverage. No applicable expression query or summary; no biological absence inference. |
| validation | Documented per-record schema and strict checks; 106-strict.tsv | supports | Both checks exit 0; scientific classification and stereochemistry concerns are not schema errors. |
| search | Ignored-inclusive exact record/owner search; 106-local-hits.txt;106-inspect.json | context_only | One exact target identified; all 16 initial input hashes unchanged. |

## Limits And Additional Notes

- All adopted citation records and available abstracts plus ten indexed literature leads were inspected; PMID4613708 lacks an abstract and its full echinocandin-B paper was not read.
- The complete main texts of original 2000 biological and 2003 structural reports were read; the 2003 structure image was inspected. The2004 publisher main text and tables were read after EuropePMC XML failed HTTP500.
- Current CARD and PubChem perpetuate classification/stereochemistry limitations. A search-engine excerpt suggesting different CARD ancestry was not accepted over the actually fetched source page.
- CARD mirror retrieval failed certificate hostname verification and was not used. No insecure retrieval was attempted.
- The six unresolved natural-product stereocenters were not solved. This review proposes bounded partial specificity, not a fully assigned replacement structure.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 16 initially captured hashes remain unchanged; no native or saved-bundle edits.
- Original read-only ARO cache SHA256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T091440Z-arborcandin-c-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of arborcandin C
started_at: '2026-10-21T09:07:58Z'
finished_at: '2026-10-21T09:14:40Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Antifungal cyclic decapeptide misclassified and incompletely stereospecified
scientific_review: true
summary: The seeded planar structure reproduces current PubChem, but all 13 stereocenters
  are unset despite seven established assignments. Primary literature supports antifungal
  activity and distinguishes arborcandins from echinocandins, contradicting the native
  antibacterial filing and structural class. Exact biochemical and genetic evidence
  offers bounded mechanism enrichment.
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
  - path: data/antibiotics/antibacterial/arborcandin-c.yaml
    sha256: 6b854e87a5d833a14691ffdc54b1df9b96bbb82a66da1adf64c74b67ad08332a
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
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
scope:
  description: Whole ARO-derived record, adopted definition and class citations, exact
    chemical identity, current source assertions, primary production/structure/target
    literature and all available indexed lead abstracts.
  selection: Path-ordered queue index 106; exact record and maintained ARO owners
    hashed before scientific judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-de2f58b0cc
targets:
- target_id: antibioticmech:aro-de2f58b0cc
  path: data/antibiotics/antibacterial/arborcandin-c.yaml
  label: arborcandin C
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity,definition and classification
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted supplemental structure
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: ARO definition class adjudication
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding decisions
checks:
- check_id: schema
  name: Documented per-record schema check
  status: passed
  required: true
  summary: Exit 0; no issues.
  target_ids:
  - antibioticmech:aro-de2f58b0cc
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/arborcandin-c.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict schema check
  status: passed
  required: true
  summary: Exit 0; zero ERROR rows.
  target_ids:
  - antibioticmech:aro-de2f58b0cc
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/arborcandin-c.yaml --out /private/tmp/am-review-session/106-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Native and PubChem chemistry
  status: passed
  required: false
  summary: Exit 0; planar encodings, formula, mass, charge and mint agree; all 13
    centers unspecified.
  target_ids:
  - antibioticmech:aro-de2f58b0cc
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/106-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: sources
  name: Cached ARO and current CARD/ChEBI
  status: passed
  required: false
  summary: Exit 0; identifiers and adopted source assertions reproduce, including
    the scientifically problematic class.
  target_ids:
  - antibioticmech:aro-de2f58b0cc
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/106-source-check.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - sources
- check_id: adapter-catalog
  name: Native source adapter before web
  status: passed
  required: false
  summary: Exit 0; no fungal organism dataset available; no applicable gene query.
  target_ids:
  - antibioticmech:aro-de2f58b0cc
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
  exit_code: 0
  expected_exit_code: 0
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
  - antibioticmech:aro-de2f58b0cc
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
  - antibioticmech:aro-de2f58b0cc
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
  - antibioticmech:aro-de2f58b0cc
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
  - antibioticmech:aro-de2f58b0cc
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
  - antibioticmech:aro-de2f58b0cc
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
  - antibioticmech:aro-de2f58b0cc
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
  - antibioticmech:aro-de2f58b0cc
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
  - antibioticmech:aro-de2f58b0cc
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
  - antibioticmech:aro-de2f58b0cc
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/arborcandin-c.yaml
  locator: Whole native YAML including three seed/reseed events
  accessed_at: '2026-10-21T09:12:25Z'
  support: supports
  summary: ARO-derived SEEDED/MINTED record has fungal definition, ANTIBACTERIAL filing,
    echinocandin parent/class and wholly unspecified stereochemistry. No native primary
    target, resistance, producer or activity objects are asserted.
- evidence_id: inventory
  kind: record_content
  reference: conf/sources.yaml;scripts/seed_from_sources.py;data/raw/aro_antibiotics.tsv;data/raw/pubchem_structures.tsv
  locator: classify() and generated structural-class selection; 106 source-row JSON
    files
  accessed_at: '2026-10-21T09:12:25Z'
  support: supports
  summary: ARO class and supplemental PubChem graph propagate into the seed. With
    no decisive roles or class map, the default files this record ANTIBACTERIAL. Existing
    aro_definition_overrides supports a per-compound adjudication; structural-class
    and chemistry repairs require maintained source/transform support.
- evidence_id: sources
  kind: database
  reference: https://card.mcmaster.ca/ontology/48017;https://www.ebi.ac.uk/chebi/CHEBI:217490
  locator: 106-card.html;106-ols.json;106-source-check.json
  accessed_at: '2026-10-21T09:12:25Z'
  support: supports
  summary: Fetched current CARD repeats ARO:3007496 echinocandin membership, PMID11132955
    and PubChem9941831; cached ARO agrees. Current ChEBI is a nonobsolete exact-name
    record. Reproducing database assertions does not resolve conflicts with the original
    structure report.
  snapshot_sha256: 5a89b0aa5a35a3abb8db56d0dd9f962d9351f53556b9d3ea14f223ef6bc1bf19
- evidence_id: chemistry
  kind: validation
  reference: PubChem CID9941831;RDKit
  locator: 106-chemistry.py;106-chemistry.json;106-pubchem.json
  accessed_at: '2026-10-21T09:12:25Z'
  support: supports
  summary: Native encodings and current PubChem agree on neutral C59H105N13O18 and
    AHATVKJRQUTSJV-UHFFFAOYSA-N, one connected molecule and all 13 tetrahedral centers
    unset. This validates source reproduction, not completeness of natural-product
    stereochemistry.
  snapshot_sha256: ca9e49eaa83e24c558aad15a8bf1c746e90e7905d4e7cc15fb08377c6fa296d6
- evidence_id: biology
  kind: primary_source
  reference: PMID:11132955
  locator: DOI:10.7164/antibiotics.53.1108;106-primary2000.pdf complete main text
    and Tables1–4
  accessed_at: '2026-10-21T09:12:25Z'
  support: supports
  summary: 'Purified arborcandin C from fungal SANK17397 broth inhibits C.albicans/A.fumigatus
    glucan synthase noncompetitively. Candida growth inhibition and killing are distinct
    endpoints. A.fumigatus morphological MEC is not complete-growth MIC: the latter
    exceeds 64 micrograms/ml. The producing strain was isolated from a plant; that
    does not identify the plant as producer. The paper explicitly distinguishes the
    scaffold from echinocandins.'
  snapshot_sha256: c77a2df82a16a2add2a5512d5334c96ae5b39b8cd8aee86f5b12431c27160096
- evidence_id: structure
  kind: primary_source
  reference: DOI:10.7164/antibiotics.56.1024
  locator: 106-primary2003.pdf complete main text; original p1027 Figures1–2 visually
    inspected; pp1028–1030 assignments
  accessed_at: '2026-10-21T09:12:25Z'
  support: refutes
  summary: 'NMR/MS establish the ten-residue ring and side chains. Advanced Marfey
    analysis plus selective Asn reduction and Thr coupling/NOE assign Asn-1 D, Asn-2
    L, Ala D, Thr-1 D-allo and Thr-2 L: seven centers. The remaining centers in gamma-hydroxy-Gln,
    Xaa-1 and Xaa-2 are explicitly unresolved. Discussion contrasts these cyclic peptides
    with echinocandin hexapeptides.'
  snapshot_sha256: be0b2842073b6c7a51539906b2938787160e77dff6f4be06d209eb7751fa285a
- evidence_id: genetics
  kind: primary_source
  reference: PMID:14693557
  locator: DOI:10.1128/AAC.48.1.319-322.2004;publisher full main text and Tables1–3
    inspected
  accessed_at: '2026-10-21T09:12:25Z'
  support: supports
  summary: S.cerevisiae FKS1 N470K or L642S constructs confer selective cellular and
    glucan-synthase resistance to arborcandin C. Controlled fks1 deletion/FKS2 repression
    and replacement experiments support Fks1 involvement. Cell-growth IC50, complete-inhibition
    MIC and enzyme IC50 are separate. This is genetic/biochemical target evidence;
    direct binding and a precise contact site were left for future work.
- evidence_id: leads
  kind: database
  reference: PMID:11132955;PMID:4613708 and indexed arborcandin literature
  locator: 106-core.json;106-literature.json;106-lead-dispositions.json
  accessed_at: '2026-10-21T09:12:25Z'
  support: context_only
  summary: All adopted citation records and available abstracts were checked. PMID4613708
    concerns echinocandin B, has no available abstract and cannot establish arborcandin
    identity. Ten broader search hits were individually scoped; unrelated safety/environmental
    studies and echinocandin-specific findings were not transferred.
  snapshot_sha256: 99555303dc57b213c61e2b4f4fb9000a5eda626d13fad96117215b2b6297bbc4
- evidence_id: adapter
  kind: database
  reference: Native iModulonDB adapter
  locator: 106-imodulondb-datasets.txt
  accessed_at: '2026-10-21T09:12:25Z'
  support: context_only
  summary: Catalog executed before open web research; fungal organisms implicated
    here are outside listed dataset coverage. No applicable expression query or summary;
    no biological absence inference.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: validation
  kind: validation
  reference: Documented per-record schema and strict checks
  locator: 106-strict.tsv
  accessed_at: '2026-10-21T09:12:25Z'
  support: supports
  summary: Both checks exit 0; scientific classification and stereochemistry concerns
    are not schema errors.
- evidence_id: search
  kind: search
  reference: Ignored-inclusive exact record/owner search
  locator: 106-local-hits.txt;106-inspect.json
  accessed_at: '2026-10-21T09:12:25Z'
  support: context_only
  summary: One exact target identified; all 16 initial input hashes unchanged.
  search_scope: prepare.py 106 used rg --no-ignore --hidden excluding .git/.venv.
    Additional ARO/PubChem owners hashed before judgment; negative findings are limited
    to the named paths searched with ignored files included.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact natural-product representation
  outcome: concern
  summary: Planar identity is consistent; established partial stereochemistry is omitted.
  target_ids:
  - antibioticmech:aro-de2f58b0cc
  evidence_ids:
  - chemistry
  - structure
- assessment_id: classification
  area: grounding
  topic: Activity and structural classes
  outcome: concern
  summary: Fungal activity supports ANTIFUNGAL; cyclic decapeptide is not echinocandin
    structural identity.
  target_ids:
  - antibioticmech:aro-de2f58b0cc
  evidence_ids:
  - record
  - biology
  - structure
  - sources
- assessment_id: mechanism
  area: evidence
  topic: Definition and target interpretation
  outcome: supported
  summary: Definition-level synthase inhibition is supported; genetics can enrich
    evidence without claiming direct binding.
  target_ids:
  - antibioticmech:aro-de2f58b0cc
  evidence_ids:
  - biology
  - genetics
- assessment_id: provenance
  area: provenance
  topic: Adopted sources and current databases
  outcome: supported
  summary: Source reproduction is transparent; upstream repetition does not override
    primary structure evidence.
  target_ids:
  - antibioticmech:aro-de2f58b0cc
  evidence_ids:
  - sources
  - inventory
  - leads
- assessment_id: optional
  area: completeness
  topic: Primary target, producer and phenotype fields
  outcome: supported
  summary: Optional primary enrichment is available; no isolated missing optional
    field is treated as a defect.
  target_ids:
  - antibioticmech:aro-de2f58b0cc
  evidence_ids:
  - biology
  - genetics
- assessment_id: adapter
  area: scope
  topic: Expression adapter applicability
  outcome: not_applicable
  summary: No fungal dataset in executed catalog.
  target_ids:
  - antibioticmech:aro-de2f58b0cc
  evidence_ids:
  - adapter
- assessment_id: validation
  area: schema
  topic: Focused checks
  outcome: supported
  summary: Native schema and strict pass.
  target_ids:
  - antibioticmech:aro-de2f58b0cc
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: aro-3009172-arborcandin-c-antifungal-class
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Antibacterial fallback conflicts with exact fungal activity
  description: Native definition and its primary citation describe antifungal action,
    but no explicit adjudication prevents the default ANTIBACTERIAL filing.
  target_ids:
  - antibioticmech:aro-de2f58b0cc
  field_paths:
  - antimicrobial_class
  - definition
  evidence_ids:
  - record
  - inventory
  - biology
  rule_id: 'review-checklist: exact identity, source scope and maintained ownership'
  native_severity: major
  normalization_reason: Major activity classification error; not a claim that no possible
    antibacterial effect exists.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity,definition and classification
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted supplemental structure
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: ARO definition class adjudication
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding decisions
- finding_id: F2
  issue_key: aro-3009172-arborcandin-c-echinocandin-class
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Echinocandin structural class conflicts with the original structure
  description: Native parent and structural class reproduce an upstream assertion,
    but arborcandin C is a distinct cyclic decapeptide rather than the echinocandin
    hexapeptide scaffold. Shared glucan-synthase inhibition cannot establish structural
    identity.
  target_ids:
  - antibioticmech:aro-de2f58b0cc
  field_paths:
  - parent_compounds
  - structural_class
  - structural_class_id
  evidence_ids:
  - record
  - sources
  - structure
  - biology
  rule_id: 'review-checklist: exact identity, source scope and maintained ownership'
  native_severity: major
  normalization_reason: Major wrong structural grounding with a coherent compound
    identity.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity,definition and classification
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted supplemental structure
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: ARO definition class adjudication
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding decisions
- finding_id: F3
  issue_key: aro-3009172-arborcandin-c-known-stereochemistry-omitted
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Seven established stereocenters are omitted
  description: All 13 native centers are unset. The primary structural assignment
    establishes five amino-acid configurations covering seven centers, while explicitly
    retaining uncertainty at the other six.
  target_ids:
  - antibioticmech:aro-de2f58b0cc
  field_paths:
  - chemical_structure.smiles
  - chemical_structure.standard_inchi
  - chemical_structure.standard_inchi_key
  evidence_ids:
  - chemistry
  - structure
  rule_id: 'review-checklist: exact identity, source scope and maintained ownership'
  native_severity: major
  normalization_reason: Major loss of known identity specificity; unresolved centers
    must remain unspecified.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity,definition and classification
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted supplemental structure
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: ARO definition class adjudication
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding decisions
- finding_id: F4
  issue_key: aro-3009172-arborcandin-c-primary-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Exact primary mechanism and phenotype evidence can enrich the seed
  description: Original fungal production, biochemical inhibition and controlled FKS1
    genetics provide optional claim-level additions.
  target_ids:
  - antibioticmech:aro-de2f58b0cc
  field_paths:
  - molecular_targets
  - resistance_mechanisms
  - activity_spectrum
  - evidence
  - discussions
  evidence_ids:
  - biology
  - genetics
  rule_id: 'review-checklist: exact identity, source scope and maintained ownership'
  native_severity: informational
  normalization_reason: Existing empty optional fields do not constitute a demonstrated
    defect.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/arborcandin-c.yaml
    role: Curator-owned claim-level evidence and discussions
actions:
- action_id: A1
  description: Adjudicate the activity class through the existing maintained override.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-de2f58b0cc
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity,definition and classification
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted supplemental structure
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: ARO definition class adjudication
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding decisions
  acceptance_checks:
  - 'Add exact ARO:3009172: ANTIFUNGAL under conf/sources.yaml aro_definition_overrides
    with source rationale; preserve source-priority rules.'
  - Reseed using maintained tooling, confirm resulting class/path and corpus reproducibility,
    and run required native gates.
- action_id: A2
  description: Repair the inherited structural-class relationship reproducibly.
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:aro-de2f58b0cc
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity,definition and classification
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted supplemental structure
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: ARO definition class adjudication
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding decisions
  acceptance_checks:
  - Correct upstream ARO membership or implement an explicit maintained source-level
    exclusion/override supported by the primary cyclic-decapeptide structure. Current
    fetched CARD still repeats the error; a refresh alone is not a demonstrated fix.
  - Keep parent_compounds and structural_class/id mutually consistent. Use a validated
    applicable structural term or leave unsupported class grounding unset; do not
    invent a CURIE or confuse common target with class.
  - Re-extract/reseed and verify exact structure/class plus native schema,strict,term,reference,history
    and corpus checks.
- action_id: A3
  description: Preserve known partial stereochemistry without inventing the unresolved
    centers.
  finding_ids:
  - F3
  target_ids:
  - antibioticmech:aro-de2f58b0cc
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity,definition and classification
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted supplemental structure
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: ARO definition class adjudication
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding decisions
  acceptance_checks:
  - Map Asn-1 D, Asn-2 L, Ala D, Thr-1 D-allo and Thr-2 L from the original numbered
    residues onto the maintained structure input; independently verify all seven atom
    assignments.
  - Leave gamma-hydroxy-Gln and both long-chain Xaa residues unresolved unless stronger
    exact-compound evidence is obtained. Unspecified is not racemic.
  - Regenerate consistent SMILES/InChI/key with unchanged connectivity/formula, retain
    provenance and exact PubChem specificity caveat, then pass chemical and native
    reproducibility gates.
- action_id: A4
  description: Optionally add narrow primary mechanism, resistance and production
    evidence.
  finding_ids:
  - F4
  target_ids:
  - antibioticmech:aro-de2f58b0cc
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/arborcandin-c.yaml
    role: Curator-owned claim-level evidence and discussions
  acceptance_checks:
  - Separate enzyme inhibition from whole-cell growth and genetic resistance; FKS1
    substitutions support target involvement without a direct binding-site claim.
  - Preserve Candida/Aspergillus/Saccharomyces strain,medium and endpoint boundaries.
    Do not encode Aspergillus morphological MEC as MIC or pool family activity ranges
    into arborcandin C.
  - Represent cultured SANK17397 fungus as producer only with defensible organism
    grounding; plant collection source is not plant biosynthesis.
limitations:
- All adopted citation records and available abstracts plus ten indexed literature
  leads were inspected; PMID4613708 lacks an abstract and its full echinocandin-B
  paper was not read.
- The complete main texts of original 2000 biological and 2003 structural reports
  were read; the 2003 structure image was inspected. The2004 publisher main text and
  tables were read after EuropePMC XML failed HTTP500.
- Current CARD and PubChem perpetuate classification/stereochemistry limitations.
  A search-engine excerpt suggesting different CARD ancestry was not accepted over
  the actually fetched source page.
- CARD mirror retrieval failed certificate hostname verification and was not used.
  No insecure retrieval was attempted.
- The six unresolved natural-product stereocenters were not solved. This review proposes
  bounded partial specificity, not a fully assigned replacement structure.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 16 initially captured hashes remain unchanged; no native or saved-bundle edits.
- 'Original read-only ARO cache SHA256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4'
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://card.mcmaster.ca/ontology/48017
- https://doi.org/10.7164/antibiotics.53.1108
- https://doi.org/10.7164/antibiotics.56.1024
- https://doi.org/10.1128/AAC.48.1.319-322.2004
tags:
- record-review
- arborcandin-c
- antifungal
- stereochemistry
- classification
```
