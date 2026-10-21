# Review of arbekacin

- Review: 20261021T091434Z-arbekacin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:03:23Z
- Finished UTC: 2026-10-21T09:14:34Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The free arbekacin structure is internally and externally consistent. Its ChEBI-derived definition omits the 3-prime,4-prime dideoxy modification and consequently describes a different oxygenation state. Original synthesis distinguishes both compounds. Exact primary ribosome and resistance studies support bounded optional enrichment of the currently database-qualified annotations.

## Scope And Provenance

Whole merged ChEBI/ARO SEEDED record; exact chemistry and structural definition, all seven ChEBI and two ARO definition leads, cited target/resistance ontology terms and their indexed literature, source ownership and primary synthesis/ribosome/resistance experiments.

Selection: Path-ordered queue index 105; exact record prepared before judgment; ARO source owners and four additional input hashes captured before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:37922 | data/antibiotics/antibacterial/arbekacin.yaml | generated | arbekacin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented per-record schema check | passed | True | CHEBI:37922 | Exit 0; no issues found. |
| Documented strict schema check | passed | True | CHEBI:37922 | Exit 0; one file and zero ERROR rows. |
| Native and source chemistry | passed | False | CHEBI:37922 | Exit 0; encodings, formula, mass, charge, mint and PubChem/KEGG/ChEMBL exact keys agree. |
| Current ChEBI/CARD and cached ARO assertions | passed | False | CHEBI:37922 | Exit 0; native source assertions reproduce; this does not validate the incorrect structural definition scientifically. |
| Native structured source catalog | passed | False | CHEBI:37922 | Exit 0 before open web research. |
| Native expression search mexY | passed | False | CHEBI:37922 | Exit 0; no genes or iModulons matched in p_aeruginosa/precise364; no component summary applicable. |
| Native expression search mexX | passed | False | CHEBI:37922 | Exit 0; no genes or iModulons matched in p_aeruginosa/precise364; no component summary applicable. |
| Native expression search rmtA | passed | False | CHEBI:37922 | Exit 0; no genes or iModulons matched in p_aeruginosa/precise364; no component summary applicable. |
| Native expression search rmtD | passed | False | CHEBI:37922 | Exit 0; no genes or iModulons matched in p_aeruginosa/precise364; no component summary applicable. |
| Native expression search rmtG | passed | False | CHEBI:37922 | Exit 0; no genes or iModulons matched in p_aeruginosa/precise364; no component summary applicable. |
| Authoritative full QC | failed | True | CHEBI:37922 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:37922 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:37922 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:37922 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:37922 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:37922 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:37922 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:37922 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:37922 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Definition versus correct molecular structure

identity: concern. Targets: CHEBI:37922.

The definition requires the dideoxy distinction; native structure and exact synonym should be preserved.

### Chemical and antibacterial classes

grounding: supported. Targets: CHEBI:37922.

Aminoglycoside/kanamycin-family membership and bacterial activity are supported.

### 16S target and translation inhibition

evidence: supported. Targets: CHEBI:37922.

Direct structural and biochemical primary evidence is available for a bounded upgrade; native database provenance is honest.

### Target alteration and efflux

evidence: supported. Targets: CHEBI:37922.

Native assertions reproduce CARD. Specific RmtC/RmtD experiments support enrichment; remaining exact-drug/strain limitations are explicit.

### Primary target/resistance evidence

completeness: supported. Targets: CHEBI:37922.

Useful optional enrichment exists without a required-field defect.

### Expression-module checks

scope: supported. Targets: CHEBI:37922.

Native adapter checks executed before web; negative query results do not constrain biology.

### Generated field repair

ownership: supported. Targets: CHEBI:37922.

Chosen definition is seeder-owned; repair maintained source/extraction or explicit supported selection then regenerate.

### Focused validators

schema: supported. Targets: CHEBI:37922.

Schema and strict validation pass.

## Findings

### F1: Structural definition omits the 3-prime,4-prime dideoxy modification

major / open / confirmed; issue key: chebi-37922-arbekacin-definition-missing-dideoxy.

Kanamycin B bearing the AHB group is the oxygenated 1-AHB-KMB compound; arbekacin is the corresponding dibekacin derivative. Omitting both deoxygenations makes the structural definition inconsistent with the correct native formula, SMILES and exact synonym.

### F2: Exact primary target and resistance evidence can enrich the qualified seed

informational / open / confirmed; issue key: chebi-37922-arbekacin-primary-target-resistance-enrichment.

Direct ribosome structures and RmtC/RmtD experiments offer scoped primary evidence for the currently database-qualified objects. Empty optional activity data and current PRIMARY_EVIDENCE_NEEDED status alone are not defects.

## Recommended Actions And Acceptance Checks

### A1

Correct the generated definition reproducibly while retaining the established exact structure.

- Define arbekacin as 1-N-[(S)-4-amino-2-hydroxybutyryl]dibekacin, or explicitly as the 3-prime,4-prime-dideoxykanamycin B derivative. Preserve the N1 attachment and S side-chain center.
- Keep the present C22H44N6O10 graph and exact key; do not add two oxygens to conform to the flawed text.
- Correct maintained ChEBI source extraction/definition selection or add an explicitly supported maintained override with primary provenance; do not imply the existing grounding decisions table already supports arbitrary definition text. Re-extract/reseed so corpus verification reproduces the repair.
- Run exact structure/definition comparison and native schema,strict,term,reference,history and required corpus checks.

### A2

Optionally curate exact primary mechanism and resistance experiments.

- Attach h44/16S direct-binding evidence with E.coli ribosome context and sulfate assay reagent; separate translocation and peptide-release effects from claims that EF-G or release factors are directly bound.
- Keep MG1655 susceptibility separate from JE-28 purified ribosomes; Methods-visible-growth MIC is not population MIC50. Distinguish reported primary binding from weak alternative-site density.
- Use cloned rmtC/rmtD strains and vector controls for causal resistance claims; retain more limited evidence scope for other determinants. Do not copy upstream RmtG organism error or generalize PA7 OprA to every P.aeruginosa strain.
- Preserve all primary chemical/salt, assay and strain boundaries and complete required curation gates before any status promotion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/arbekacin.yaml; Whole YAML including five seed/reseed events | supports | Native structure and exact systematic synonym are arbekacin, while the definition omits two deoxygenations. Nine resistance entries explicitly state CARD assertions; the 16S-rRNA target is PRIMARY_EVIDENCE_NEEDED, with no invented strain or assay. Host-shared protein-synthesis qualifier remains intact. |
| inventory | data/raw/chebi_antimicrobials.tsv;data/raw/aro_antibiotics.tsv;data/raw/aro_target_edges.tsv;data/raw/aro_resistance_edges.tsv; 105 source-row JSON files; scripts/seed_from_sources.py definition selection | supports | ChEBI owns the chosen definition; the maintained ARO row instead identifies dibekacin as parent. Source priority propagates the ChEBI omission. The definition is seeder-owned, requiring reproducible source/selection repair rather than a direct native edit. |
| sources | https://www.ebi.ac.uk/chebi/CHEBI:37922;https://card.mcmaster.ca/ontology/36998; 105-ols.json;105-parents.json;105-card.html;105-aro-terms.json;105-source-check.json | supports | Current ChEBI repeats the omission, while current CARD identifies a dibekacin derivative. Chemical parents and retained roles fit. All nine resistance accessions and the 16S target reproduce explicit nonobsolete cached ARO relationships and appear on the current CARD compound page. |
| chemistry | RDKit;PubChem CID68682;ChEMBL426926;KEGG D07462; 105-chemistry.py;105-chemistry.json;105-pubchem.json;105-chembl.json;105-kegg.mol | supports | Four exact representations agree on MKKYBZZTJQGVCD-XTCKQBCOSA-N, neutral C22H44N6O10, all 14 assigned centers and the native mint. DrugCentral 235 also resolves with matching name/formula/synonyms. DrugBank request failed HTTP403; CAS/Reaxys are corroborated rather than independently registry-resolved. |
| synthesis | PMID:4782059; DOI:10.7164/antibiotics.26.412;105-primary1973.pdf pp412–415;original p412 structure and p413 Table1 visually inspected | refutes | The original report synthesizes two distinct products: 1-AHB-kanamycin B with O12 and 1-AHB-dibekacin with O10. The latter is the arbekacin scaffold. Its figure labels the two ring-I substitutions as OH versus H. Table1 separately reports antibacterial activities; the deoxygenated column must be used. Products were characterized as dicarbonates, not an unqualified free-base assay reagent. |
| binding | PMID:40415027; DOI:10.1038/s41598-025-02391-3;105-primary2025.xml complete main text | supports | Purified E.coli JE-28 ribosomes and arbekacin sulfate support h44/16S binding and inhibition of translocation and RF-mediated peptide release. MG1655 broth assays are separate from those molecular experiments. The Methods define visible-growth MIC for one strain despite MIC50 wording elsewhere; do not infer a multi-isolate MIC50. Primary h44 density is clear; an alternative P-tRNA-adjacent site is weak, and H69 binding was not seen. |
| structure | https://www.rcsb.org/structure/9MKK;https://www.rcsb.org/structure/8IFC; 105-pdb9mkk.json;105-pdb8ifc.json;105-pdb84g.json | partial | Ligand 84G matches the native exact key. Current 9MKK supersedes 8Q4F and reports 3.2 Å, whereas the paper states 3.1 Å. Independent 8IFC (PMID38227611;DOI10.1093/jb/mvae002) supports arbekacin-bound E.coli ribosome at deposition/complete abstract scope; its full paper was not read. |
| rmtd | PMID:17158944; DOI:10.1128/AAC.01345-06;PMC1803107 Methods/Results/Table1 inspected via web | supports | CLSI agar dilution found arbekacin MIC&gt;256 micrograms/ml for P.aeruginosa PA0905 and the E.coli XL1-Blue rmtD-containing clone, versus 0.25 for vector control. This supports exact-compound resistance with clone/strain scope; beta-lactamase SPM-1 is a separate mechanism. |
| rmtc | PMID:16377684; DOI:10.1128/AAC.50.1.178-184.2006;PMC1346777 Methods/Results/Table2 inspected via web | supports | Arbekacin agar-dilution MIC increased from 0.25 in E.coli DH5alpha vector control to 512 or &gt;1024 micrograms/ml in defined rmtC constructs. Purified RmtC methylation experiments support target alteration. Neither the parental strain nor failed conjugation establishes universal transferability. |
| leads | All adopted ChEBI/ARO definition and inspected ontology citation leads; 105-core.json;105-lead-dispositions.json | context_only | All 27 indexed records and available abstracts were read: nine compound-level adopted leads plus target/class/resistance context. Clinical PK, community pharmacodynamics and engineered resistance were separated. Model-RNA analog studies were not treated as exact full-ribosome evidence. Three records have no abstract; detailed results were not invented. |
| resistance-limits | PMID:22282519;PMID:20194115;PMID:23459483;PMID:23478957; 105-core.json;105-PMC2896518.xml | partial | PA7 knockout/complementation abstract supports MexXY-OprA with strain specificity; its exact arbekacin table was unavailable. Sgm paper supports methylation but no arbekacin-specific assay was established. RmtG discovery abstract is K.pneumoniae, unlike upstream ARO description; native record does not copy that organism. RmtH abstract explicitly includes arbekacin. |
| patents | patent:DE2350169;patent:US4107424;patent:EP2199280; 105-patent-*.html; relevant descriptions and examples | context_only | DE/US patents cover multiple AHB aminoglycosides, with the dideoxy derivative distinct from oxygenated analogs. EP2199280 concerns K04-0144 compounds and uses arbekacin as a comparative control; it is contextual document evidence, not an arbekacin biosynthesis or novel-identity claim. |
| adapter | Native iModulonDB adapter; 105-imodulondb-datasets.txt;105-adapter-results.json | context_only | Catalog and five Pseudomonas gene queries preceded web research. No hit was returned for mexX,mexY,rmtA,rmtD,rmtG in precise364. This does not disprove efflux/resistance or establish absence from other strains. |
| validation | Documented schema and strict validation; 105-strict.tsv | supports | Both focused native checks exited 0; semantic definition conflict passes deterministic schema checks. |
| search | Ignored-inclusive local review search; 105-local-hits.txt;105-inspect.json | context_only | One exact merged record and maintained owners identified; all 17 captured hashes remain unchanged. |

## Limits And Additional Notes

- All 27 indexed lead records and available abstracts were inspected; three lack abstracts. Most older primary bodies were not read. The 1973 synthesis and 2025 ribosome main text were read fully; RmtC/RmtD relevant full Methods/Results were inspected.
- RmtC/RmtD XML endpoints failed HTTP500 but PMC web text was accessible. RmtG/RmtH XML failed HTTP500 and PMC returned a browser challenge; MexXY-OprA publisher timed out. Their dispositions are explicitly abstract-only.
- Sgm full XML was inspected for exact-drug scope; it supports methyltransferase biology but not an established arbekacin susceptibility experiment here.
- The 2025 paper has nomenclature and approval statements not adopted here. Its text 3.1 Å differs from current 9MKK 3.2 Å; the primary target conclusion does not depend on resolving this metadata difference.
- DrugBank fetch failed HTTP403; CAS and proprietary Reaxys identities were corroborated through maintained/current sources rather than independently registry-verified.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 17 initial input hashes unchanged; no native or saved bundle edits. ARO cache in the original checkout was read only and is not represented as a fresh download.
- Read-only ARO cache SHA256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T091434Z-arbekacin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of arbekacin
started_at: '2026-10-21T09:03:23Z'
finished_at: '2026-10-21T09:14:34Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Correct native structure but major omission in generated structural
  definition
scientific_review: true
summary: The free arbekacin structure is internally and externally consistent. Its
  ChEBI-derived definition omits the 3-prime,4-prime dideoxy modification and consequently
  describes a different oxygenation state. Original synthesis distinguishes both compounds.
  Exact primary ribosome and resistance studies support bounded optional enrichment
  of the currently database-qualified annotations.
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
  - path: data/antibiotics/antibacterial/arbekacin.yaml
    sha256: 82e2ca6542db3e7db78632465b48c436e4b9a53030e09186a19605c3382d1483
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
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
scope:
  description: Whole merged ChEBI/ARO SEEDED record; exact chemistry and structural
    definition, all seven ChEBI and two ARO definition leads, cited target/resistance
    ontology terms and their indexed literature, source ownership and primary synthesis/ribosome/resistance
    experiments.
  selection: Path-ordered queue index 105; exact record prepared before judgment;
    ARO source owners and four additional input hashes captured before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:37922
targets:
- target_id: CHEBI:37922
  path: data/antibiotics/antibacterial/arbekacin.yaml
  label: arbekacin
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
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, target/resistance or supplemental structure input
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Adopted ARO identity, target/resistance or supplemental structure input
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Adopted ARO identity, target/resistance or supplemental structure input
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted ARO identity, target/resistance or supplemental structure input
checks:
- check_id: schema
  name: Documented per-record schema check
  status: passed
  required: true
  summary: Exit 0; no issues found.
  target_ids:
  - CHEBI:37922
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/arbekacin.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict schema check
  status: passed
  required: true
  summary: Exit 0; one file and zero ERROR rows.
  target_ids:
  - CHEBI:37922
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/arbekacin.yaml --out /private/tmp/am-review-session/105-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Native and source chemistry
  status: passed
  required: false
  summary: Exit 0; encodings, formula, mass, charge, mint and PubChem/KEGG/ChEMBL
    exact keys agree.
  target_ids:
  - CHEBI:37922
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/105-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: sources
  name: Current ChEBI/CARD and cached ARO assertions
  status: passed
  required: false
  summary: Exit 0; native source assertions reproduce; this does not validate the
    incorrect structural definition scientifically.
  target_ids:
  - CHEBI:37922
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/105-source-check.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - sources
- check_id: adapter-catalog
  name: Native structured source catalog
  status: passed
  required: false
  summary: Exit 0 before open web research.
  target_ids:
  - CHEBI:37922
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-mexy
  name: Native expression search mexY
  status: passed
  required: false
  summary: Exit 0; no genes or iModulons matched in p_aeruginosa/precise364; no component
    summary applicable.
  target_ids:
  - CHEBI:37922
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism p_aeruginosa --dataset precise364 --query
    mexY
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-mexx
  name: Native expression search mexX
  status: passed
  required: false
  summary: Exit 0; no genes or iModulons matched in p_aeruginosa/precise364; no component
    summary applicable.
  target_ids:
  - CHEBI:37922
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism p_aeruginosa --dataset precise364 --query
    mexX
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-rmta
  name: Native expression search rmtA
  status: passed
  required: false
  summary: Exit 0; no genes or iModulons matched in p_aeruginosa/precise364; no component
    summary applicable.
  target_ids:
  - CHEBI:37922
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism p_aeruginosa --dataset precise364 --query
    rmtA
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-rmtd
  name: Native expression search rmtD
  status: passed
  required: false
  summary: Exit 0; no genes or iModulons matched in p_aeruginosa/precise364; no component
    summary applicable.
  target_ids:
  - CHEBI:37922
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism p_aeruginosa --dataset precise364 --query
    rmtD
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-rmtg
  name: Native expression search rmtG
  status: passed
  required: false
  summary: Exit 0; no genes or iModulons matched in p_aeruginosa/precise364; no component
    summary applicable.
  target_ids:
  - CHEBI:37922
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism p_aeruginosa --dataset precise364 --query
    rmtG
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
  - CHEBI:37922
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
  - CHEBI:37922
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
  - CHEBI:37922
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
  - CHEBI:37922
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
  - CHEBI:37922
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
  - CHEBI:37922
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
  - CHEBI:37922
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
  - CHEBI:37922
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
  - CHEBI:37922
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/arbekacin.yaml
  locator: Whole YAML including five seed/reseed events
  accessed_at: '2026-10-21T09:07:40Z'
  support: supports
  summary: Native structure and exact systematic synonym are arbekacin, while the
    definition omits two deoxygenations. Nine resistance entries explicitly state
    CARD assertions; the 16S-rRNA target is PRIMARY_EVIDENCE_NEEDED, with no invented
    strain or assay. Host-shared protein-synthesis qualifier remains intact.
- evidence_id: inventory
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv;data/raw/aro_antibiotics.tsv;data/raw/aro_target_edges.tsv;data/raw/aro_resistance_edges.tsv
  locator: 105 source-row JSON files; scripts/seed_from_sources.py definition selection
  accessed_at: '2026-10-21T09:07:40Z'
  support: supports
  summary: ChEBI owns the chosen definition; the maintained ARO row instead identifies
    dibekacin as parent. Source priority propagates the ChEBI omission. The definition
    is seeder-owned, requiring reproducible source/selection repair rather than a
    direct native edit.
- evidence_id: sources
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:37922;https://card.mcmaster.ca/ontology/36998
  locator: 105-ols.json;105-parents.json;105-card.html;105-aro-terms.json;105-source-check.json
  accessed_at: '2026-10-21T09:07:40Z'
  support: supports
  summary: Current ChEBI repeats the omission, while current CARD identifies a dibekacin
    derivative. Chemical parents and retained roles fit. All nine resistance accessions
    and the 16S target reproduce explicit nonobsolete cached ARO relationships and
    appear on the current CARD compound page.
  snapshot_sha256: 7f4f3dc39979ec06d99b97e2c454805bd32e7690e02fc5db48101bac67ace24c
- evidence_id: chemistry
  kind: validation
  reference: RDKit;PubChem CID68682;ChEMBL426926;KEGG D07462
  locator: 105-chemistry.py;105-chemistry.json;105-pubchem.json;105-chembl.json;105-kegg.mol
  accessed_at: '2026-10-21T09:07:40Z'
  support: supports
  summary: Four exact representations agree on MKKYBZZTJQGVCD-XTCKQBCOSA-N, neutral
    C22H44N6O10, all 14 assigned centers and the native mint. DrugCentral 235 also
    resolves with matching name/formula/synonyms. DrugBank request failed HTTP403;
    CAS/Reaxys are corroborated rather than independently registry-resolved.
  snapshot_sha256: e1d8cdafb5b489e7354ca5aeeda2cfa20feadb951a411988f9b63a6f49238b33
- evidence_id: synthesis
  kind: primary_source
  reference: PMID:4782059
  locator: DOI:10.7164/antibiotics.26.412;105-primary1973.pdf pp412–415;original p412
    structure and p413 Table1 visually inspected
  accessed_at: '2026-10-21T09:07:40Z'
  support: refutes
  summary: 'The original report synthesizes two distinct products: 1-AHB-kanamycin
    B with O12 and 1-AHB-dibekacin with O10. The latter is the arbekacin scaffold.
    Its figure labels the two ring-I substitutions as OH versus H. Table1 separately
    reports antibacterial activities; the deoxygenated column must be used. Products
    were characterized as dicarbonates, not an unqualified free-base assay reagent.'
  snapshot_sha256: a7fd4100db245726e605a22e807bdfe9b6f085fe001f773b90206f53220e56f9
- evidence_id: binding
  kind: primary_source
  reference: PMID:40415027
  locator: DOI:10.1038/s41598-025-02391-3;105-primary2025.xml complete main text
  accessed_at: '2026-10-21T09:07:40Z'
  support: supports
  summary: Purified E.coli JE-28 ribosomes and arbekacin sulfate support h44/16S binding
    and inhibition of translocation and RF-mediated peptide release. MG1655 broth
    assays are separate from those molecular experiments. The Methods define visible-growth
    MIC for one strain despite MIC50 wording elsewhere; do not infer a multi-isolate
    MIC50. Primary h44 density is clear; an alternative P-tRNA-adjacent site is weak,
    and H69 binding was not seen.
  snapshot_sha256: 8cd088c96681e0f105875aaa264c4b5c71170a6be6227c22268555648f2e9692
- evidence_id: structure
  kind: database
  reference: https://www.rcsb.org/structure/9MKK;https://www.rcsb.org/structure/8IFC
  locator: 105-pdb9mkk.json;105-pdb8ifc.json;105-pdb84g.json
  accessed_at: '2026-10-21T09:07:40Z'
  support: partial
  summary: Ligand 84G matches the native exact key. Current 9MKK supersedes 8Q4F and
    reports 3.2 Å, whereas the paper states 3.1 Å. Independent 8IFC (PMID38227611;DOI10.1093/jb/mvae002)
    supports arbekacin-bound E.coli ribosome at deposition/complete abstract scope;
    its full paper was not read.
  snapshot_sha256: e239a1b714c50218db4f9b578b4418f629d01242cd0c834e88c8d2b477f4dcf3
- evidence_id: rmtd
  kind: primary_source
  reference: PMID:17158944
  locator: DOI:10.1128/AAC.01345-06;PMC1803107 Methods/Results/Table1 inspected via
    web
  accessed_at: '2026-10-21T09:07:40Z'
  support: supports
  summary: CLSI agar dilution found arbekacin MIC>256 micrograms/ml for P.aeruginosa
    PA0905 and the E.coli XL1-Blue rmtD-containing clone, versus 0.25 for vector control.
    This supports exact-compound resistance with clone/strain scope; beta-lactamase
    SPM-1 is a separate mechanism.
- evidence_id: rmtc
  kind: primary_source
  reference: PMID:16377684
  locator: DOI:10.1128/AAC.50.1.178-184.2006;PMC1346777 Methods/Results/Table2 inspected
    via web
  accessed_at: '2026-10-21T09:07:40Z'
  support: supports
  summary: Arbekacin agar-dilution MIC increased from 0.25 in E.coli DH5alpha vector
    control to 512 or >1024 micrograms/ml in defined rmtC constructs. Purified RmtC
    methylation experiments support target alteration. Neither the parental strain
    nor failed conjugation establishes universal transferability.
- evidence_id: leads
  kind: database
  reference: All adopted ChEBI/ARO definition and inspected ontology citation leads
  locator: 105-core.json;105-lead-dispositions.json
  accessed_at: '2026-10-21T09:07:40Z'
  support: context_only
  summary: 'All 27 indexed records and available abstracts were read: nine compound-level
    adopted leads plus target/class/resistance context. Clinical PK, community pharmacodynamics
    and engineered resistance were separated. Model-RNA analog studies were not treated
    as exact full-ribosome evidence. Three records have no abstract; detailed results
    were not invented.'
  snapshot_sha256: 95945757c09608ef318bc5d49e4f7ff285b7cab8631bbe534c9b122b8d9fa9f3
- evidence_id: resistance-limits
  kind: primary_source
  reference: PMID:22282519;PMID:20194115;PMID:23459483;PMID:23478957
  locator: 105-core.json;105-PMC2896518.xml
  accessed_at: '2026-10-21T09:07:40Z'
  support: partial
  summary: PA7 knockout/complementation abstract supports MexXY-OprA with strain specificity;
    its exact arbekacin table was unavailable. Sgm paper supports methylation but
    no arbekacin-specific assay was established. RmtG discovery abstract is K.pneumoniae,
    unlike upstream ARO description; native record does not copy that organism. RmtH
    abstract explicitly includes arbekacin.
- evidence_id: patents
  kind: primary_source
  reference: patent:DE2350169;patent:US4107424;patent:EP2199280
  locator: 105-patent-*.html; relevant descriptions and examples
  accessed_at: '2026-10-21T09:07:40Z'
  support: context_only
  summary: DE/US patents cover multiple AHB aminoglycosides, with the dideoxy derivative
    distinct from oxygenated analogs. EP2199280 concerns K04-0144 compounds and uses
    arbekacin as a comparative control; it is contextual document evidence, not an
    arbekacin biosynthesis or novel-identity claim.
- evidence_id: adapter
  kind: database
  reference: Native iModulonDB adapter
  locator: 105-imodulondb-datasets.txt;105-adapter-results.json
  accessed_at: '2026-10-21T09:07:40Z'
  support: context_only
  summary: Catalog and five Pseudomonas gene queries preceded web research. No hit
    was returned for mexX,mexY,rmtA,rmtD,rmtG in precise364. This does not disprove
    efflux/resistance or establish absence from other strains.
  snapshot_sha256: 2b7d2916e64bfc19e063fd5a18bf5f6cc6cd5d9770250f8617441bdaf5f0c25d
- evidence_id: validation
  kind: validation
  reference: Documented schema and strict validation
  locator: 105-strict.tsv
  accessed_at: '2026-10-21T09:07:40Z'
  support: supports
  summary: Both focused native checks exited 0; semantic definition conflict passes
    deterministic schema checks.
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local review search
  locator: 105-local-hits.txt;105-inspect.json
  accessed_at: '2026-10-21T09:07:40Z'
  support: context_only
  summary: One exact merged record and maintained owners identified; all 17 captured
    hashes remain unchanged.
  search_scope: prepare.py 105 used rg --no-ignore --hidden excluding .git/.venv.
    Additional ARO owner files were hashed before scientific assessment. Negative
    local findings are limited to paths searched with ignored files included.
assessments:
- assessment_id: identity
  area: identity
  topic: Definition versus correct molecular structure
  outcome: concern
  summary: The definition requires the dideoxy distinction; native structure and exact
    synonym should be preserved.
  target_ids:
  - CHEBI:37922
  evidence_ids:
  - record
  - synthesis
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Chemical and antibacterial classes
  outcome: supported
  summary: Aminoglycoside/kanamycin-family membership and bacterial activity are supported.
  target_ids:
  - CHEBI:37922
  evidence_ids:
  - sources
  - synthesis
  - leads
- assessment_id: mechanism
  area: evidence
  topic: 16S target and translation inhibition
  outcome: supported
  summary: Direct structural and biochemical primary evidence is available for a bounded
    upgrade; native database provenance is honest.
  target_ids:
  - CHEBI:37922
  evidence_ids:
  - binding
  - structure
  - record
- assessment_id: resistance
  area: evidence
  topic: Target alteration and efflux
  outcome: supported
  summary: Native assertions reproduce CARD. Specific RmtC/RmtD experiments support
    enrichment; remaining exact-drug/strain limitations are explicit.
  target_ids:
  - CHEBI:37922
  evidence_ids:
  - sources
  - rmtd
  - rmtc
  - resistance-limits
- assessment_id: optional
  area: completeness
  topic: Primary target/resistance evidence
  outcome: supported
  summary: Useful optional enrichment exists without a required-field defect.
  target_ids:
  - CHEBI:37922
  evidence_ids:
  - binding
  - rmtd
  - rmtc
- assessment_id: adapter
  area: scope
  topic: Expression-module checks
  outcome: supported
  summary: Native adapter checks executed before web; negative query results do not
    constrain biology.
  target_ids:
  - CHEBI:37922
  evidence_ids:
  - adapter
- assessment_id: ownership
  area: ownership
  topic: Generated field repair
  outcome: supported
  summary: Chosen definition is seeder-owned; repair maintained source/extraction
    or explicit supported selection then regenerate.
  target_ids:
  - CHEBI:37922
  evidence_ids:
  - inventory
- assessment_id: schema
  area: schema
  topic: Focused validators
  outcome: supported
  summary: Schema and strict validation pass.
  target_ids:
  - CHEBI:37922
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: chebi-37922-arbekacin-definition-missing-dideoxy
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Structural definition omits the 3-prime,4-prime dideoxy modification
  description: Kanamycin B bearing the AHB group is the oxygenated 1-AHB-KMB compound;
    arbekacin is the corresponding dibekacin derivative. Omitting both deoxygenations
    makes the structural definition inconsistent with the correct native formula,
    SMILES and exact synonym.
  target_ids:
  - CHEBI:37922
  field_paths:
  - definition
  - definition_source
  - chemical_structure
  evidence_ids:
  - record
  - inventory
  - sources
  - synthesis
  - chemistry
  rule_id: 'review-checklist: Structure and Equivalence; exact structural definitions'
  native_severity: major wrong structural description
  normalization_reason: Native exact identifiers and graph remain coherent, so this
    is a major definition error rather than a wrong-record blocker.
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
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, target/resistance or supplemental structure input
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Adopted ARO identity, target/resistance or supplemental structure input
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Adopted ARO identity, target/resistance or supplemental structure input
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted ARO identity, target/resistance or supplemental structure input
- finding_id: F2
  issue_key: chebi-37922-arbekacin-primary-target-resistance-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Exact primary target and resistance evidence can enrich the qualified seed
  description: Direct ribosome structures and RmtC/RmtD experiments offer scoped primary
    evidence for the currently database-qualified objects. Empty optional activity
    data and current PRIMARY_EVIDENCE_NEEDED status alone are not defects.
  target_ids:
  - CHEBI:37922
  field_paths:
  - molecular_targets
  - resistance_mechanisms
  - activity_spectrum
  - evidence
  - discussions
  evidence_ids:
  - binding
  - structure
  - rmtd
  - rmtc
  - resistance-limits
  rule_id: 'review-checklist: narrowest claim-level primary evidence'
  native_severity: informational optional enrichment
  normalization_reason: Current provenance explicitly distinguishes database assertion
    from primary review.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/arbekacin.yaml
    role: Curator-owned evidence,targets,resistance and discussions
actions:
- action_id: A1
  description: Correct the generated definition reproducibly while retaining the established
    exact structure.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:37922
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
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, target/resistance or supplemental structure input
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Adopted ARO identity, target/resistance or supplemental structure input
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Adopted ARO identity, target/resistance or supplemental structure input
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted ARO identity, target/resistance or supplemental structure input
  acceptance_checks:
  - Define arbekacin as 1-N-[(S)-4-amino-2-hydroxybutyryl]dibekacin, or explicitly
    as the 3-prime,4-prime-dideoxykanamycin B derivative. Preserve the N1 attachment
    and S side-chain center.
  - Keep the present C22H44N6O10 graph and exact key; do not add two oxygens to conform
    to the flawed text.
  - Correct maintained ChEBI source extraction/definition selection or add an explicitly
    supported maintained override with primary provenance; do not imply the existing
    grounding decisions table already supports arbitrary definition text. Re-extract/reseed
    so corpus verification reproduces the repair.
  - Run exact structure/definition comparison and native schema,strict,term,reference,history
    and required corpus checks.
- action_id: A2
  description: Optionally curate exact primary mechanism and resistance experiments.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:37922
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/arbekacin.yaml
    role: Curator-owned evidence,targets,resistance and discussions
  acceptance_checks:
  - Attach h44/16S direct-binding evidence with E.coli ribosome context and sulfate
    assay reagent; separate translocation and peptide-release effects from claims
    that EF-G or release factors are directly bound.
  - Keep MG1655 susceptibility separate from JE-28 purified ribosomes; Methods-visible-growth
    MIC is not population MIC50. Distinguish reported primary binding from weak alternative-site
    density.
  - Use cloned rmtC/rmtD strains and vector controls for causal resistance claims;
    retain more limited evidence scope for other determinants. Do not copy upstream
    RmtG organism error or generalize PA7 OprA to every P.aeruginosa strain.
  - Preserve all primary chemical/salt, assay and strain boundaries and complete required
    curation gates before any status promotion.
limitations:
- All 27 indexed lead records and available abstracts were inspected; three lack abstracts.
  Most older primary bodies were not read. The 1973 synthesis and 2025 ribosome main
  text were read fully; RmtC/RmtD relevant full Methods/Results were inspected.
- RmtC/RmtD XML endpoints failed HTTP500 but PMC web text was accessible. RmtG/RmtH
  XML failed HTTP500 and PMC returned a browser challenge; MexXY-OprA publisher timed
  out. Their dispositions are explicitly abstract-only.
- Sgm full XML was inspected for exact-drug scope; it supports methyltransferase biology
  but not an established arbekacin susceptibility experiment here.
- The 2025 paper has nomenclature and approval statements not adopted here. Its text
  3.1 Å differs from current 9MKK 3.2 Å; the primary target conclusion does not depend
  on resolving this metadata difference.
- DrugBank fetch failed HTTP403; CAS and proprietary Reaxys identities were corroborated
  through maintained/current sources rather than independently registry-verified.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 17 initial input hashes unchanged; no native or saved bundle edits. ARO cache
  in the original checkout was read only and is not represented as a fresh download.
- 'Read-only ARO cache SHA256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4'
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:37922
- https://card.mcmaster.ca/ontology/36998
- https://doi.org/10.7164/antibiotics.26.412
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12104382/
- https://www.rcsb.org/structure/9MKK
tags:
- record-review
- arbekacin
- definition
- ribosome
- resistance
```
