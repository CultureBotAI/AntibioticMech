# Review of aztreonam

- Review: 20261021T100507Z-aztreonam-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:27:15Z
- Finished UTC: 2026-10-21T10:05:07Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact aztreonam graph, all 26 cited CDC MIC observations and 16 FDA assertions across seven applications are supported. The generated AmpR entry incorrectly labels a regulatory resistance route as antibiotic-target alteration. Current ChEBI SMILES and the PDB opened-form cross-reference require explicit source boundaries. All adopted ChEBI and ARO publication leads were dispositioned.

## Scope And Provenance

Entire SEEDED exact record and 24 history events; ChEBI/ARO/FDA source ownership; all 26 CDC susceptibility pages; current exact graph comparisons; adopted citation abstracts and selected primary mechanism/resistance text.

Selection: Path-ordered queue index 136 prepared and hashed before judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:161680 | data/antibiotics/antibacterial/aztreonam.yaml | generated | aztreonam |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema check | passed | True | CHEBI:161680 | Exit 0. |
| Documented strict check | passed | True | CHEBI:161680 | Exit 0; zero ERROR rows. |
| Native and PubChem exact chemistry | passed | False | CHEBI:161680 | Exit 0; native encodings, formula, charge, masses, stereo and mint agree. |
| Independent exported graph comparison | passed | False | CHEBI:161680 | Exit 0; KEGG drug/compound, DrugCentral and ChEMBL standardized keys match. |
| Supplemental current-OLS literal comparison | failed | False | CHEBI:161680 | Exit 1 at the literal SMILES assertion: current OLS omits oxime stereochemistry although its InChI matches. This failure is preserved; bounded source assessment is separate. |
| Bounded identity, ARO and clinical source assessment | passed | False | CHEBI:161680 | Exit 0 after correcting the supplemental harness to use the actual xrefs field; seven source edges and 16 clinical assertions reproduce. Scientific AmpR interpretation is reviewed separately. |
| All cited CDC MIC comparisons | passed | False | CHEBI:161680 | Exit 0 after normalizing source line breaks in organism names; 26 values/censors/organisms and 23 available BioSamples match. |
| Native iModulonDB catalog before web | passed | False | CHEBI:161680 | Exit 0; applicable organism catalogs present. |
| Native ftsI search before web | passed | False | CHEBI:161680 | Exit 0; b0084 gene match, zero iModulons. |
| Native ampR search before web | passed | False | CHEBI:161680 | Exit 0; PA4109 gene match, zero iModulons. |
| Authoritative full QC | failed | True | CHEBI:161680 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:161680 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:161680 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:161680 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:161680 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:161680 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:161680 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:161680 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:161680 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact aztreonam graph

identity: supported. Targets: CHEBI:161680.

Independent structure exports corroborate the native compound.

### Ontology and source representation

grounding: supported. Targets: CHEBI:161680.

Native parent/role claims are sound; external OLS/CCD representations have explicitly bounded scope.

### AmpR coarse resistance route

evidence: concern. Targets: CHEBI:161680.

The generated target-alteration label is not an accurate representation of the cited regulatory mechanism.

### All curated MIC observations

evidence: supported. Targets: CHEBI:161680.

Every cited CDC row was checked against its source, including censors, identifiers and edition context.

### Approval and marketing metadata

evidence: supported. Targets: CHEBI:161680.

Current FDA and GSRS records corroborate the source-dated clinical assertions.

### History, source ownership and citations

provenance: supported. Targets: CHEBI:161680.

The generation path and all adopted publication scopes were checked.

### Primary PBP evidence upgrade

completeness: unknown. Targets: CHEBI:161680.

Primary evidence can refine the deliberately provisional generic PBP target; this optional enrichment is separate from the resistance correction.

### Focused native gates

schema: supported. Targets: CHEBI:161680.

Schema and strict checks pass. The supplemental OLS literal assertion failed and is recorded explicitly.

## Findings

### F1: Correct the AmpR resistance-route classification at its generating owner

major / open / confirmed; issue key: chebi-161680-ampr-regulation-misclassified-target-alteration.

resistance_mechanisms[6] labels ARO:3007491 as ANTIBIOTIC_TARGET_ALTERATION. AmpR is a regulator; the cited source supports a beta-lactamase-expression hypothesis, not altered drug-binding machinery. The record reproduces an ambiguous ontology-derived category and therefore misstates the biological route even though schema validation passes.

## Recommended Actions And Acceptance Checks

### A1

Correct the generated AmpR route without implying AmpR is itself a hydrolytic enzyme.

- Implement a narrowly scoped determinant override or explicit ambiguity policy for ARO:3007491 in the owning extraction/configuration path, regenerate the inventory and verify that reseeding preserves the correction. A native-only edit will be overwritten.
- Use OTHER with an explicit regulatory beta-lactamase-upregulation explanation under the current enum, or an inactivation-route representation that explicitly attributes hydrolysis to the downstream enzyme. Do not label AmpR itself ANTIBIOTIC_TARGET_ALTERATION.
- Keep the primary association and uncertainty separate from causal allele proof; preserve the database-assertion scope unless directly curating the original organism/strain-specific experiments.
- Retain all unrelated resistance entries, MIC rows, exact chemical identity, clinical assertions and provenance. Validate schema, strict/reference/history integrity and source reproducibility.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/aztreonam.yaml; Whole native YAML and 24 curation-history events | supports | SEEDED exact compound combines two source concepts, seven database-only resistance assertions, a generic PBP target explicitly awaiting primary evidence, curator-owned MIC rows and source-dated clinical status. History separates seed updates, MIC curation and BioSample additions; no new REVIEWED sign-off is asserted. |
| chemistry | PubChem CID:5742832;drugcentral:279;kegg.drug:D00240;kegg.compound:C06840;chembl:CHEMBL158; 136-chemistry.json;136-xref-check.json | supports | Native SMILES/InChI and independent exported structures resolve WZPBZJONDBGPKJ-VEHQQRBSSA-N, C13H17N5O8S2, net zero charge, two specified carbon centers and Z oxime. Native zwitterionic and neutral database encodings standardize consistently; masses and mint agree. |
| sources | CHEBI:161680; 136-ols.json;136-parents.json;136-source-assessment.json | partial | Identity, nonobsolete parents and broad antimicrobial roles agree. Current OLS InChI/key agree but its SMILES lacks the oxime direction marker and generates a different stereochemical key; its synonym array also omits aztréonam. Native exact structure is independently corroborated. The failed literal check is not treated as a native schema failure. |
| aro | data/raw/aro_resistance_edges.tsv;scripts/extract_source_inventory.py;conf/sources.yaml; mechanism_for around lines453-485;136-aro_resistance_edges.json;136-aro-stanzas.txt | context_only | All seven native resistance rows reproduce exact-aztreonam edges. The extractor walks mapped ancestors and chooses the sorted nearest hit; AmpR is emitted via ARO:0001001. The seeder copies this coarse value. An ignored-inclusive conf/scripts/tests search found no determinant-specific 3007491 override. Reproduction of a source classification does not validate its biological meaning. |
| aro-cache | ARO ontology cached download; /Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/downloads/aro.obo | context_only | Read-only cached ontology stanzas were hashed before assessment and remain unchanged. This external cache is evidence, not a repository-relative maintained input. |
| ampr | PMID:37070974; DOI:10.1128/spectrum.03080-22;136-primary-ampr.xml; full main article | refutes | Sequential P. aeruginosa ST773 isolates show aztreonam MIC 4 versus 64 mg/L and increased PDC-16 expression associated with AmpR D135G. The paper reports no PBP1-4 mutations. An AmpC inhibitor enlarged the disk zone; no allele replacement/complementation establishes D135G causality. The proposed route regulates beta-lactamase production, rather than altering the antibiotic target. |
| card | ARO:3007491; https://card.mcmaster.ca/ontology/46259;136-ampr-card.html;136-aro-stanzas.txt | context_only | Current CARD definition describes PDC-16 upregulation, while its ontology-derived mechanism display includes both antibiotic inactivation and target alteration. This explains the generated ambiguity and is not independent proof of either mechanism. |
| pbp | PMID:6180685; DOI:10.1128/AAC.21.6.950; original abstract and author-uploaded PBP Methods/Results at https://www.researchgate.net/publication/17011976_Mode_of_action_of_azthreonam | partial | The exact SQ26776 study uses membrane competition with radiolabeled penicillin, SDS-PAGE and fluorography. Low-concentration PBP3 engagement accompanies filamentation; complete competition at 0.1 micrograms/ml is not an MIC or dissociation constant. The separately reported bulk peptidoglycan-transpeptidase inhibition requires much higher concentration. Selected original text supports a species/assay-scoped primary target upgrade. |
| cdc | Cited CDC/FDA AR Isolate Bank pages; 136-cdc-check.json and all 136-cdc-*.html; each native activity_spectrum reference | supports | All 26 current cited pages agree on censored MIC, R interpretation and isolate organism; 23 available BioSample identifiers match and 3 pages explicitly lack them. Source footers retain each row’s CLSI 2025/2026 edition. Micrograms/ml equal mg/L. These observations are strain-specific phenotypes, not proof of the named resistance determinants. |
| clinical | Drugs@FDA;FDA GSRS UNII:G2B4VE5GH8; 136-fda-live.json;136-gsrs.json;136-fda-*.html;136-source-assessment.json | supports | Current official FDA product records corroborate all 16 native assertions across applications 050580,050632,050814,065286,065439,206517,207069: approval dates, sponsors, product names/numbers and marketing states. GSRS version 48 exports the exact native standardized graph. Approval remains separate from discontinued marketing; the additional combination-product application is outside this single-ingredient mapping. |
| ccd | pdb:AZR; https://data.rcsb.org/rest/v1/core/chemcomp/AZR;136-ccd-azr.json | context_only | The component is explicitly the open form, formula C13H19N5O8S2, key OEVQTUTXOVDNJO-GEEOIBTQSA-N, with protein-linked covalent-modification context. It is not the intact free-compound identity. Treat this adopted cross-reference as reaction/adduct context and qualify it if retained; do not replace native chemistry with the CCD graph. |
| leads | Ten ChEBI and thirteen ARO adopted PMID leads; 136-core.json;136-aro-core.json;136-lead-dispositions.json | context_only | All 23 adopted records and complete abstracts were inspected; the supplemental 1982 mechanism paper makes 24 dispositioned publications. Lead-specific summaries distinguish allergy, clinical lysine formulation, combination/biofilm work, pump genetics, enzyme characterization and secondary reviews. No abstract-only lead supplies new quantitative native assertions. |
| adapter | Native iModulonDB ftsI and ampR searches; 136-imodulondb-datasets.txt;136-imodulondb-ftsi.txt;136-imodulondb-ampr.txt | context_only | Exact gene matches identify contextual leads only; zero iModulons returned, so no component-summary request applies. Expression resources are not binding evidence. |
| validation | Focused native schema and strict checks; 136-strict.tsv | supports | Both documented focused checks pass despite the scientifically incorrect generated resistance category. |
| search | Ignored-inclusive local ownership search; 136-local-hits.txt;136-inspect.json | context_only | All 19 captured target/context inputs are unchanged; owners include ARO/FDA inventories, extractors, seeder and curated MIC/history. |

## Limits And Additional Notes

- The source-literal supplemental command was executed and failed on current OLS SMILES disagreement; the passing bounded assessment does not erase that failure. Native structure is independently corroborated.
- All 23 adopted publication abstracts were read. Only the AmpR main article and selected original 1982 PBP Methods/Results were reviewed beyond abstracts; other adopted full manuscripts and supplementary datasets were not all inspected.
- The 1982 EPMC XML request returned 500 and a guessed PMC PDF URL returned an HTML challenge, not a paper. Selected original text was subsequently read from the author-uploaded ResearchGate copy; no numerical transcription from OCR-only tables was used.
- Initial guessed CARD URLs returned 500 and one alternate hostname failed TLS validation; the correct current CARD page was retrieved without bypassing TLS.
- PDB AZR is an opened protein-linked component. The generic adopted xref is bounded as reaction context, not free-molecule equivalence; separate proprietor CAS/Reaxys registries were not queried.
- CDC references report isolate MICs and their own CLSI editions; the full CLSI manuals, susceptibility replicates and independent sequence validation of BioSamples were not reanalyzed.
- Native iModulonDB searches provided gene context but no iModulons or experimental mechanism proof.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 19 captured input hashes unchanged; no native record edits. Supplemental harness fixes normalized source organism line breaks and used the actual xrefs field; neither altered native data.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T100507Z-aztreonam-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of aztreonam
started_at: '2026-10-21T09:27:15Z'
finished_at: '2026-10-21T10:05:07Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Exact identity, MICs and approval metadata supported; generated AmpR
  resistance route misclassified
scientific_review: true
summary: The exact aztreonam graph, all 26 cited CDC MIC observations and 16 FDA assertions
  across seven applications are supported. The generated AmpR entry incorrectly labels
  a regulatory resistance route as antibiotic-target alteration. Current ChEBI SMILES
  and the PDB opened-form cross-reference require explicit source boundaries. All
  adopted ChEBI and ARO publication leads were dispositioned.
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
  - path: data/antibiotics/antibacterial/aztreonam.yaml
    sha256: a9aff230bf5f40d45a5d722c477996d8d74127dde47cfa46eeb3af3246c237a4
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
  - path: data/raw/fda_clinical_status.tsv
    sha256: a6952f85426afa53c5704c588681a078e599ce245bf18f7c9dd390d70e7bb16c
    role: context
  - path: scripts/extract_fda_clinical_status.py
    sha256: f30f385ea6d530dc1749e3d805dbcdbc8715fbc476abc510bf144ea13964e171
    role: context
scope:
  description: Entire SEEDED exact record and 24 history events; ChEBI/ARO/FDA source
    ownership; all 26 CDC susceptibility pages; current exact graph comparisons; adopted
    citation abstracts and selected primary mechanism/resistance text.
  selection: Path-ordered queue index 136 prepared and hashed before judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:161680
targets:
- target_id: CHEBI:161680
  path: data/antibiotics/antibacterial/aztreonam.yaml
  label: aztreonam
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
    role: Adopted ARO/FDA identity, edges or clinical metadata owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Adopted ARO/FDA identity, edges or clinical metadata owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Adopted ARO/FDA identity, edges or clinical metadata owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted ARO/FDA identity, edges or clinical metadata owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/fda_clinical_status.tsv
    role: Adopted ARO/FDA identity, edges or clinical metadata owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: Adopted ARO/FDA identity, edges or clinical metadata owner
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/aztreonam.yaml
    role: Curator-owned activity_spectrum and history
checks:
- check_id: schema
  name: Documented schema check
  status: passed
  required: true
  summary: Exit 0.
  target_ids:
  - CHEBI:161680
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/aztreonam.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict check
  status: passed
  required: true
  summary: Exit 0; zero ERROR rows.
  target_ids:
  - CHEBI:161680
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/aztreonam.yaml --out /private/tmp/am-review-session/136-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Native and PubChem exact chemistry
  status: passed
  required: false
  summary: Exit 0; native encodings, formula, charge, masses, stereo and mint agree.
  target_ids:
  - CHEBI:161680
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/136-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: xrefs
  name: Independent exported graph comparison
  status: passed
  required: false
  summary: Exit 0; KEGG drug/compound, DrugCentral and ChEMBL standardized keys match.
  target_ids:
  - CHEBI:161680
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/136-xref-check.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: source-literal
  name: Supplemental current-OLS literal comparison
  status: failed
  required: false
  summary: 'Exit 1 at the literal SMILES assertion: current OLS omits oxime stereochemistry
    although its InChI matches. This failure is preserved; bounded source assessment
    is separate.'
  target_ids:
  - CHEBI:161680
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/136-source-check.py
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - sources
- check_id: source-bounded
  name: Bounded identity, ARO and clinical source assessment
  status: passed
  required: false
  summary: Exit 0 after correcting the supplemental harness to use the actual xrefs
    field; seven source edges and 16 clinical assertions reproduce. Scientific AmpR
    interpretation is reviewed separately.
  target_ids:
  - CHEBI:161680
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/136-source-assessment.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - sources
  - clinical
  - aro
- check_id: cdc
  name: All cited CDC MIC comparisons
  status: passed
  required: false
  summary: Exit 0 after normalizing source line breaks in organism names; 26 values/censors/organisms
    and 23 available BioSamples match.
  target_ids:
  - CHEBI:161680
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/136-cdc-check.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - cdc
- check_id: adapter
  name: Native iModulonDB catalog before web
  status: passed
  required: false
  summary: Exit 0; applicable organism catalogs present.
  target_ids:
  - CHEBI:161680
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-ftsi
  name: Native ftsI search before web
  status: passed
  required: false
  summary: Exit 0; b0084 gene match, zero iModulons.
  target_ids:
  - CHEBI:161680
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset modulome --query ftsI
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-ampr
  name: Native ampR search before web
  status: passed
  required: false
  summary: Exit 0; PA4109 gene match, zero iModulons.
  target_ids:
  - CHEBI:161680
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism p_aeruginosa --dataset precise364 --query
    ampR
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
  - CHEBI:161680
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
  - CHEBI:161680
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
  - CHEBI:161680
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
  - CHEBI:161680
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
  - CHEBI:161680
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
  - CHEBI:161680
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
  - CHEBI:161680
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
  - CHEBI:161680
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
  - CHEBI:161680
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/aztreonam.yaml
  locator: Whole native YAML and 24 curation-history events
  accessed_at: '2026-10-21T09:34:57Z'
  support: supports
  summary: SEEDED exact compound combines two source concepts, seven database-only
    resistance assertions, a generic PBP target explicitly awaiting primary evidence,
    curator-owned MIC rows and source-dated clinical status. History separates seed
    updates, MIC curation and BioSample additions; no new REVIEWED sign-off is asserted.
- evidence_id: chemistry
  kind: validation
  reference: PubChem CID:5742832;drugcentral:279;kegg.drug:D00240;kegg.compound:C06840;chembl:CHEMBL158
  locator: 136-chemistry.json;136-xref-check.json
  accessed_at: '2026-10-21T09:34:57Z'
  support: supports
  summary: Native SMILES/InChI and independent exported structures resolve WZPBZJONDBGPKJ-VEHQQRBSSA-N,
    C13H17N5O8S2, net zero charge, two specified carbon centers and Z oxime. Native
    zwitterionic and neutral database encodings standardize consistently; masses and
    mint agree.
  snapshot_sha256: 8bd6c1fc6eed1dc4c9c5fc7f5fe9853e9ede8ddf3a121f8cb9b90eb17e3e6c6c
- evidence_id: sources
  kind: database
  reference: CHEBI:161680
  locator: 136-ols.json;136-parents.json;136-source-assessment.json
  accessed_at: '2026-10-21T09:34:57Z'
  support: partial
  summary: Identity, nonobsolete parents and broad antimicrobial roles agree. Current
    OLS InChI/key agree but its SMILES lacks the oxime direction marker and generates
    a different stereochemical key; its synonym array also omits aztréonam. Native
    exact structure is independently corroborated. The failed literal check is not
    treated as a native schema failure.
  snapshot_sha256: d094e501d84ac0f0efbc0f91c01919d7cfbb7e2096294710118ed79c4efc2da4
- evidence_id: aro
  kind: record_content
  reference: data/raw/aro_resistance_edges.tsv;scripts/extract_source_inventory.py;conf/sources.yaml
  locator: mechanism_for around lines453-485;136-aro_resistance_edges.json;136-aro-stanzas.txt
  accessed_at: '2026-10-21T09:34:57Z'
  support: context_only
  summary: All seven native resistance rows reproduce exact-aztreonam edges. The extractor
    walks mapped ancestors and chooses the sorted nearest hit; AmpR is emitted via
    ARO:0001001. The seeder copies this coarse value. An ignored-inclusive conf/scripts/tests
    search found no determinant-specific 3007491 override. Reproduction of a source
    classification does not validate its biological meaning.
  snapshot_sha256: 795658e5e08ebf438c07352215a3ff3a9e335f0b7ab6a0543b3ef4db1152bb9e
- evidence_id: aro-cache
  kind: database
  reference: ARO ontology cached download
  locator: /Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/downloads/aro.obo
  accessed_at: '2026-10-21T09:34:57Z'
  support: context_only
  summary: Read-only cached ontology stanzas were hashed before assessment and remain
    unchanged. This external cache is evidence, not a repository-relative maintained
    input.
  snapshot_sha256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
- evidence_id: ampr
  kind: primary_source
  reference: PMID:37070974
  locator: DOI:10.1128/spectrum.03080-22;136-primary-ampr.xml; full main article
  accessed_at: '2026-10-21T09:34:57Z'
  support: refutes
  summary: Sequential P. aeruginosa ST773 isolates show aztreonam MIC 4 versus 64
    mg/L and increased PDC-16 expression associated with AmpR D135G. The paper reports
    no PBP1-4 mutations. An AmpC inhibitor enlarged the disk zone; no allele replacement/complementation
    establishes D135G causality. The proposed route regulates beta-lactamase production,
    rather than altering the antibiotic target.
  snapshot_sha256: 65f9f64ee184ee08dd96a6887016a5442785f15444bca32ebfc056d77178e2e1
- evidence_id: card
  kind: database
  reference: ARO:3007491
  locator: https://card.mcmaster.ca/ontology/46259;136-ampr-card.html;136-aro-stanzas.txt
  accessed_at: '2026-10-21T09:34:57Z'
  support: context_only
  summary: Current CARD definition describes PDC-16 upregulation, while its ontology-derived
    mechanism display includes both antibiotic inactivation and target alteration.
    This explains the generated ambiguity and is not independent proof of either mechanism.
  snapshot_sha256: de46a111b4d3300367ff76fd2a8425f6a8ed543ba16487975d4887af43195aa3
- evidence_id: pbp
  kind: primary_source
  reference: PMID:6180685
  locator: DOI:10.1128/AAC.21.6.950; original abstract and author-uploaded PBP Methods/Results
    at https://www.researchgate.net/publication/17011976_Mode_of_action_of_azthreonam
  accessed_at: '2026-10-21T09:34:57Z'
  support: partial
  summary: The exact SQ26776 study uses membrane competition with radiolabeled penicillin,
    SDS-PAGE and fluorography. Low-concentration PBP3 engagement accompanies filamentation;
    complete competition at 0.1 micrograms/ml is not an MIC or dissociation constant.
    The separately reported bulk peptidoglycan-transpeptidase inhibition requires
    much higher concentration. Selected original text supports a species/assay-scoped
    primary target upgrade.
- evidence_id: cdc
  kind: database
  reference: Cited CDC/FDA AR Isolate Bank pages
  locator: 136-cdc-check.json and all 136-cdc-*.html; each native activity_spectrum
    reference
  accessed_at: '2026-10-21T09:34:57Z'
  support: supports
  summary: All 26 current cited pages agree on censored MIC, R interpretation and
    isolate organism; 23 available BioSample identifiers match and 3 pages explicitly
    lack them. Source footers retain each row’s CLSI 2025/2026 edition. Micrograms/ml
    equal mg/L. These observations are strain-specific phenotypes, not proof of the
    named resistance determinants.
  snapshot_sha256: 82fe6968fcd09daa2219f2e2afdf1ed221bfcd08a79be24cbb571ed84f2de370
- evidence_id: clinical
  kind: database
  reference: Drugs@FDA;FDA GSRS UNII:G2B4VE5GH8
  locator: 136-fda-live.json;136-gsrs.json;136-fda-*.html;136-source-assessment.json
  accessed_at: '2026-10-21T09:34:57Z'
  support: supports
  summary: 'Current official FDA product records corroborate all 16 native assertions
    across applications 050580,050632,050814,065286,065439,206517,207069: approval
    dates, sponsors, product names/numbers and marketing states. GSRS version 48 exports
    the exact native standardized graph. Approval remains separate from discontinued
    marketing; the additional combination-product application is outside this single-ingredient
    mapping.'
  snapshot_sha256: d094e501d84ac0f0efbc0f91c01919d7cfbb7e2096294710118ed79c4efc2da4
- evidence_id: ccd
  kind: database
  reference: pdb:AZR
  locator: https://data.rcsb.org/rest/v1/core/chemcomp/AZR;136-ccd-azr.json
  accessed_at: '2026-10-21T09:34:57Z'
  support: context_only
  summary: The component is explicitly the open form, formula C13H19N5O8S2, key OEVQTUTXOVDNJO-GEEOIBTQSA-N,
    with protein-linked covalent-modification context. It is not the intact free-compound
    identity. Treat this adopted cross-reference as reaction/adduct context and qualify
    it if retained; do not replace native chemistry with the CCD graph.
  snapshot_sha256: c863b020796dbb119b1224397431aae14deabea7308868d88b83afbc9ba790ea
- evidence_id: leads
  kind: database
  reference: Ten ChEBI and thirteen ARO adopted PMID leads
  locator: 136-core.json;136-aro-core.json;136-lead-dispositions.json
  accessed_at: '2026-10-21T09:34:57Z'
  support: context_only
  summary: All 23 adopted records and complete abstracts were inspected; the supplemental
    1982 mechanism paper makes 24 dispositioned publications. Lead-specific summaries
    distinguish allergy, clinical lysine formulation, combination/biofilm work, pump
    genetics, enzyme characterization and secondary reviews. No abstract-only lead
    supplies new quantitative native assertions.
  snapshot_sha256: a1b2694559a1f6152f6f26f3eab7f5dbf94f61b46e601b728a7ac4e7a4e542d2
- evidence_id: adapter
  kind: database
  reference: Native iModulonDB ftsI and ampR searches
  locator: 136-imodulondb-datasets.txt;136-imodulondb-ftsi.txt;136-imodulondb-ampr.txt
  accessed_at: '2026-10-21T09:34:57Z'
  support: context_only
  summary: Exact gene matches identify contextual leads only; zero iModulons returned,
    so no component-summary request applies. Expression resources are not binding
    evidence.
  snapshot_sha256: 641e04b0dcac543dbd9b60789e77e1f34526fae13452bf4443d0204d0607d0d6
- evidence_id: validation
  kind: validation
  reference: Focused native schema and strict checks
  locator: 136-strict.tsv
  accessed_at: '2026-10-21T09:34:57Z'
  support: supports
  summary: Both documented focused checks pass despite the scientifically incorrect
    generated resistance category.
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local ownership search
  locator: 136-local-hits.txt;136-inspect.json
  accessed_at: '2026-10-21T09:34:57Z'
  support: context_only
  summary: All 19 captured target/context inputs are unchanged; owners include ARO/FDA
    inventories, extractors, seeder and curated MIC/history.
  search_scope: prepare.py 136 used rg --no-ignore --hidden excluding .git/.venv;
    exact-compound sources, all cited CDC pages, all adopted publication abstracts
    and selected primary mechanism/resistance text. Not an exhaustive resistance-variant
    or clinical-trial survey.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact aztreonam graph
  outcome: supported
  summary: Independent structure exports corroborate the native compound.
  target_ids:
  - CHEBI:161680
  evidence_ids:
  - chemistry
  - clinical
- assessment_id: grounding
  area: grounding
  topic: Ontology and source representation
  outcome: supported
  summary: Native parent/role claims are sound; external OLS/CCD representations have
    explicitly bounded scope.
  target_ids:
  - CHEBI:161680
  evidence_ids:
  - sources
  - ccd
- assessment_id: resistance
  area: evidence
  topic: AmpR coarse resistance route
  outcome: concern
  summary: The generated target-alteration label is not an accurate representation
    of the cited regulatory mechanism.
  target_ids:
  - CHEBI:161680
  evidence_ids:
  - aro
  - ampr
  - card
- assessment_id: activity
  area: evidence
  topic: All curated MIC observations
  outcome: supported
  summary: Every cited CDC row was checked against its source, including censors,
    identifiers and edition context.
  target_ids:
  - CHEBI:161680
  evidence_ids:
  - cdc
- assessment_id: clinical
  area: evidence
  topic: Approval and marketing metadata
  outcome: supported
  summary: Current FDA and GSRS records corroborate the source-dated clinical assertions.
  target_ids:
  - CHEBI:161680
  evidence_ids:
  - clinical
- assessment_id: provenance
  area: provenance
  topic: History, source ownership and citations
  outcome: supported
  summary: The generation path and all adopted publication scopes were checked.
  target_ids:
  - CHEBI:161680
  evidence_ids:
  - record
  - leads
  - aro
- assessment_id: completeness
  area: completeness
  topic: Primary PBP evidence upgrade
  outcome: unknown
  summary: Primary evidence can refine the deliberately provisional generic PBP target;
    this optional enrichment is separate from the resistance correction.
  target_ids:
  - CHEBI:161680
  evidence_ids:
  - pbp
  - adapter
- assessment_id: validation
  area: schema
  topic: Focused native gates
  outcome: supported
  summary: Schema and strict checks pass. The supplemental OLS literal assertion failed
    and is recorded explicitly.
  target_ids:
  - CHEBI:161680
  evidence_ids:
  - validation
  - sources
findings:
- finding_id: F1
  issue_key: chebi-161680-ampr-regulation-misclassified-target-alteration
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Correct the AmpR resistance-route classification at its generating owner
  description: resistance_mechanisms[6] labels ARO:3007491 as ANTIBIOTIC_TARGET_ALTERATION.
    AmpR is a regulator; the cited source supports a beta-lactamase-expression hypothesis,
    not altered drug-binding machinery. The record reproduces an ambiguous ontology-derived
    category and therefore misstates the biological route even though schema validation
    passes.
  target_ids:
  - CHEBI:161680
  field_paths:
  - resistance_mechanisms[6].mechanism_type
  - resistance_mechanisms[6].evidence
  evidence_ids:
  - aro
  - ampr
  - card
  rule_id: 'review-checklist: distinguish resistance route from target alteration'
  native_severity: major incorrect structured mechanism
  normalization_reason: A machine-readable resistance mechanism is scientifically
    misclassified; this is not an optional missing-literature enrichment.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO determinant mechanism extraction
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: ARO coarse-mechanism mapping policy
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Regenerated exact source edge
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated resistance object ownership
actions:
- action_id: A1
  description: Correct the generated AmpR route without implying AmpR is itself a
    hydrolytic enzyme.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:161680
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO determinant mechanism extraction
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: ARO coarse-mechanism mapping policy
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Regenerated exact source edge
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated resistance object ownership
  acceptance_checks:
  - Implement a narrowly scoped determinant override or explicit ambiguity policy
    for ARO:3007491 in the owning extraction/configuration path, regenerate the inventory
    and verify that reseeding preserves the correction. A native-only edit will be
    overwritten.
  - Use OTHER with an explicit regulatory beta-lactamase-upregulation explanation
    under the current enum, or an inactivation-route representation that explicitly
    attributes hydrolysis to the downstream enzyme. Do not label AmpR itself ANTIBIOTIC_TARGET_ALTERATION.
  - Keep the primary association and uncertainty separate from causal allele proof;
    preserve the database-assertion scope unless directly curating the original organism/strain-specific
    experiments.
  - Retain all unrelated resistance entries, MIC rows, exact chemical identity, clinical
    assertions and provenance. Validate schema, strict/reference/history integrity
    and source reproducibility.
limitations:
- The source-literal supplemental command was executed and failed on current OLS SMILES
  disagreement; the passing bounded assessment does not erase that failure. Native
  structure is independently corroborated.
- All 23 adopted publication abstracts were read. Only the AmpR main article and selected
  original 1982 PBP Methods/Results were reviewed beyond abstracts; other adopted
  full manuscripts and supplementary datasets were not all inspected.
- The 1982 EPMC XML request returned 500 and a guessed PMC PDF URL returned an HTML
  challenge, not a paper. Selected original text was subsequently read from the author-uploaded
  ResearchGate copy; no numerical transcription from OCR-only tables was used.
- Initial guessed CARD URLs returned 500 and one alternate hostname failed TLS validation;
  the correct current CARD page was retrieved without bypassing TLS.
- PDB AZR is an opened protein-linked component. The generic adopted xref is bounded
  as reaction context, not free-molecule equivalence; separate proprietor CAS/Reaxys
  registries were not queried.
- CDC references report isolate MICs and their own CLSI editions; the full CLSI manuals,
  susceptibility replicates and independent sequence validation of BioSamples were
  not reanalyzed.
- Native iModulonDB searches provided gene context but no iModulons or experimental
  mechanism proof.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 19 captured input hashes unchanged; no native record edits. Supplemental harness
  fixes normalized source organism line breaks and used the actual xrefs field; neither
  altered native data.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:161680
- https://doi.org/10.1128/spectrum.03080-22
- https://card.mcmaster.ca/ontology/46259
- https://doi.org/10.1128/AAC.21.6.950
- https://www.rcsb.org/ligand/AZR
tags:
- record-review
- aztreonam
- ampr
- resistance-route
```
