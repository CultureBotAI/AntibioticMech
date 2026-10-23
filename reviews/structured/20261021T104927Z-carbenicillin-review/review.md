# Review of carbenicillin

- Review: 20261021T104927Z-carbenicillin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:32:40Z
- Finished UTC: 2026-10-21T10:49:27Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The neutral parent structure and antibacterial filing are supported. Primary carbenicillin-bound PBP3 provides direct target evidence; WUS1 and AbuO have compound-specific functional support. The imported PvrR item needs a bounded note preserving gene-loss and phenotypic-switching context. The full original PvrR and BlaS papers were not obtained, so no new precise carbenicillin genotype/measurement claims are assigned from their abstracts.

## Scope And Provenance

Entire exact SEEDED record, five history events, all four resistance objects and the imported PBP target; maintained ChEBI/ARO rows and evidence overlays; all13 adopted compound,determinant and parent PMID leads; selected original binding/resistance studies.

Selection: Queue197; root original13 captured inputs retained, five actual ARO/evidence owner inputs appended before detailed inspection.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:3393 | data/antibiotics/antibacterial/carbenicillin.yaml | generated | carbenicillin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema check | passed | True | CHEBI:3393 | Exit0. |
| Documented strict check | passed | True | CHEBI:3393 | Exit0,zeroERRORrows. |
| Supplemental graph consistency | passed | False | CHEBI:3393 | Exit0 using019 RDKit interpreter against020 files. |
| Structured source catalog | passed | False | CHEBI:3393 | Catalog inspected before protein web follow-up. |
| Structured PvrR check | passed | False | CHEBI:3393 | No gene or component hit; no negative inference. |
| Structured AbuO check | passed | False | CHEBI:3393 | No gene or component hit; no negative inference. |
| Structured PBP context | passed | False | CHEBI:3393 | One E.coli gene hit,no component hit;context only. |
| Authoritative full QC | failed | True | CHEBI:3393 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:3393 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:3393 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:3393 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:3393 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:3393 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:3393 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:3393 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:3393 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact parent representation

identity: supported. Targets: CHEBI:3393.

Public source graphs agree; no salt/prodrug or new side-chain stereochemistry is substituted.

### Antibacterial roles and parents

grounding: supported. Targets: CHEBI:3393.

Roles/parents reproduce authorities and compound-specific binding/resistance experiments concern an antibacterial penicillin.

### PBP direct target

evidence: supported. Targets: CHEBI:3393.

Original carbenicillin acyl-enzyme structure supplies primary support for a bounded PBP example; current database status remains honest.

### WUS1/AbuO/BlaS

evidence: supported. Targets: CHEBI:3393.

WUS1 exact hydrolysis and AbuO phenotype are supported. BlaS remains a database assertion with class-level primary abstracts; no quantitative upgrade is claimed.

### PvrR direction and condition

scope: concern. Targets: CHEBI:3393.

Add loss/phenotypic-switching qualification. Exact carbenicillin perturbation details remain unresolved.

### References and history

provenance: supported. Targets: CHEBI:3393.

All13 adopted/parent PMID leads resolved at stated depths and five history events checked.

### Focused gates

schema: supported. Targets: CHEBI:3393.

Focused schema/strict and alternate-environment chemistry pass.

## Findings

### F1: Qualify PvrR with its loss and phenotypic-switching context

minor / open / confirmed; issue key: chebi-3393-pvrr-loss-variant-context.

The imported PvrR note exposes a generic resistance edge without the source gene-absence qualification. CurrentCARD and the original perturbation figure distinguish loss/variant formation from overexpression. Retain UNKNOWN and database provenance,but add the bounded direction/context note; do not invent a carbenicillin-specific deletion MIC or classify PvrR as an antibiotic efflux protein.

## Recommended Actions And Acceptance Checks

### A1

Add a source-preserving PvrR qualification through the maintained imported-evidence review.

- Bind the qualification to the exactARO3003688/carbenicillin source-row SHA and CHEBI3393 fullstructurekey; preserve CARD citation and UNKNOWN rather than fabricating a primary mechanism.
- Explain source loss/phenotypic-switching context and original Fig3 direction; explicitly leave exact carbenicillin-specific genotype/measurement support unresolved until the complete original experiment is inspected.
- Regenerate through the existing evidence-review merge path and confirm the intended note survives; run focused schema/strict and required reference/history,source and full-corpus gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/carbenicillin.yaml; Entire YAML;five history events | supports | Neutral carbenicillin is EXACT/SEEDED with three fixed penam stereocenters and one unspecified side-chain center. Four resistance items cite ARO as database assertions. The family-level PBP direct-binding target explicitly retains PRIMARY_EVIDENCE_NEEDED; no native MIC,causal graph or curated producer is asserted. |
| chemistry | CHEBI:3393;PubChem:20824;CHEMBL1214;KEGG:C06869; 197-chemistry.py/.json;current197-ols.json,197-pubchem.json,197-chembl.json,197-kegg.mol | supports | SMILES/InChI/fullkey FPPNZSSZRUTDAP-UWFZAAFLSA-N,neutral C17H18N2O6S,masses and configured/unspecified stereochemistry agree. Parent penicillin/penicillin-allergen terms and native roles reproduce ChEBI. Neutral parent is distinct from disodium salt and indanyl prodrug; no side-chain enantiomer is newly imposed. |
| xrefs | KEGG:C06869;KEGG:D07614;DrugCentral:492;patent:US3142673; 197-kegg.txt;197-drugcentral.html;197-chebi.html;197-patent.html | partial | KEGG compound and drug records resolve carbenicillin with matching parent chemistry; DrugCentral492 resolves the active drug with neutral formula/CAS and includes salt synonyms in drug context. Patent resolves as a penicillin document and remains document_xrefs,not exact identity. Current ChEBI retains HMDB/DrugBank/Reaxys mappings; direct HMDB and DrugBank retrievals failed403 and Reaxys was not accessed. |
| binding | PMID:20974151; DOI:10.1016/j.jmb.2010.10.024;197-pbp.xml full mainMethods/Results;PDB3OCL | supports | P.aeruginosa PAO1 PBP3(ftsI),expressed as soluble residues35–579,forms a crystallographically observed carbenicillin acyl-enzyme at Ser294. This supports direct PBP binding at an exact organism/protein example while preserving the native family target. The opened beta-lactam adduct is not an exact chemical xref to free carbenicillin; neither binding nor thermal shift is a clinical susceptibility claim. |
| wus | PMID:36532482; DOI:10.3389/fmicb.2022.1059997;197-wus.xml mainMethods/Results andTables3–4 | supports | Myroides albus P34 WUS1 expressed in E.coli DH5alpha raises agar-dilution carbenicillin MIC from4 to1024mg/L. Purified WUS1 hydrolyzes carbenicillin(kcat/Km1.93per micromolar per second),supporting ANTIBIOTIC_INACTIVATION. Native-host resistance also has other determinants; the recombinant comparison does not establish WUS1 as the sole cause of P34 resistance. |
| abuo | PMID:25512405; DOI:10.1128/AAC.03626-14;151-PMC4335886.html independently reread;Methods,Results,Table1;197-reused-abuo.json | supports | A.baumannii AYE carbenicillin E-strip MIC is&gt;512micrograms/mL in WT,128 in the abuO mutant and&gt;256 in complemented cells. This supports AbuO-associated resistance and an efflux-component interpretation. Fluorescent accumulation uses ethidium/ciprofloxacin,not direct purified carbenicillin transport; qPCR and broad physiology changes do not prove that AbuO alone exports this drug. |
| pvrr | PMID:11961556; DOI:10.1038/416740a;complete abstract197-core.json;originalFig3 caption197-pvrr-fig3.html andvisual197-pvrr-fig3.jpg | partial | The abstract describes a regulator of switching between resistant and susceptible phenotypes. OriginalFig3 shows PvrR overexpression reducing variant frequency and deletion increasing it. The retrieved caption/figure does not independently supply a carbenicillin-specific deletion MIC or a porin mechanism; those details must not be invented from the abstract. |
| pvrr-authority | ARO:3003688; 197-aro-stanzas.txt;currentCARD https://card.csu.mcmaster.ca/ontology/40325 | partial | The source defines a phenotypic-variant regulator and currentCARD includes gene conferring resistance via absence. The native imported note retains only a generic confers_resistance_to_antibiotic edge,so a qualification should preserve the loss/variant context instead of implying that increased wild-type PvrR necessarily confers resistance. |
| blas | PMID:9103972;PMID:15699201; 197-core.json complete abstracts;publisher2005 abstract | partial | The1997 study purifies the M.smegmatis classA beta-lactamase;2005 deletion studies show BlaS contributes to beta-lactam susceptibility in M.smegmatis PM274/PM759. Full2005 compound-specific table was not accessible,so the native carbenicillin edge remains honestly database-supported without an independently extracted exact MIC or allele-specific kinetic value. |
| other-leads | PMID:12569987;22648337;6176550;11585791;15673804;4248289;3055170;3889939; 197-core.json;197-lead-dispositions.json | context_only | The three ChEBI leads concern beta-lactam IgE recognition,two-drug cross-reactivity and an analytical carbenicillin sensor; they are not antimicrobial-target experiments. ARO compound leads include two beta-lactamase reviews and1970 carbenicillin chemistry/mode-of-action metadata. PBP/penicillin-class references are reviews. All resolve;12569987,22648337,6176550,11585791 and3055170 complete abstracts were read;15673804,4248289 and3889939 have no indexed abstracts. |
| adapter | iModulonDB; 197-imodulondb-datasets.txt;197-imodulondb-pvrr.txt;197-imodulondb-abuo.txt;197-imodulondb-pbp.txt | context_only | Native protein/regulator context was queried before literature follow-up. PvrR and AbuO returned no hits; generic penicillin search identified e_coli/modulome/b2430 yfeW,PBP4B. No component was returned,so no summarize call was applicable. This neither supports nor refutes drug binding/resistance and is not transferred to the P.aeruginosa PBP3 experiment. |
| owners | data/raw/aro_resistance_edges.tsv;data/raw/aro_target_edges.tsv;curation/card_evidence_reviews.json; Adopted exact rows,extractor/seeder and maintained evidence-review mechanism | supports | Four resistance rows and the target reproduce source inventories; no existing exact qualification was found in the ignored-inclusive curation/conf search. Imported evidence notes can be qualified through card_evidence_reviews.json with the exactsource-row hash and target structure; no native-only patch is needed. |
| validation | Focused schema/strict/chemistry; 197-strict.tsv;197-chemistry.json | supports | Native schema/strict exit0;019 RDKit command against020 files exit0;required shared corpus gates are distinct. |

## Limits And Additional Notes

- PvrR full2002 text was not obtained: publisher .pdf returned HTML and third-party full-text route challenged. Complete abstract and originalFig3/caption were inspected; no carbenicillin-specific PvrR MIC is independently verified.
- BlaS1997/2005 complete abstracts were read; the2005 fulltext/PDF routes returned403. Exact carbenicillin table remains unextracted. This does not refute the honestly labelled CARD edge.
- All13 adopted compound/determinant/parent PMID records were resolved. Three lacked indexed abstracts; several other papers were abstract-only. Sensor/IgE studies were not repurposed as antibacterial mechanism experiments.
- PBP and WUS1 original mainMethods/Results and relevant tables were inspected; raw diffraction data and raw enzyme traces were not reprocessed. PBP3 direct binding is one organism/protein example,not proof that allPBPs or bacterial strains are equally affected.
- AbuO original cachedHTML from review151 was independently reread and hashed; new EuropePMC XML retrieval failed500. Direct transport measurements used fluorescent probe drugs rather than carbenicillin.
- HMDB andDrugBank direct requests failed403; Reaxys was not accessed. Their mappings are retained as unverified direct-registry comparisons despite currentChEBI provenance. DrugCentral includes salt/product context and does not change the neutral native structure.
- 020 lacksRDKit; chemistry used019 interpreter against020 files. Native schema/strict passed in020. No exhaustive clinical,allergy,stereoisomer or resistance survey was undertaken; no native status promotion is implied.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 18 repository input hashes plus externalARO cache remain unchanged; no native or saved-bundle changes.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T104927Z-carbenicillin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of carbenicillin
started_at: '2026-10-21T10:32:40Z'
finished_at: '2026-10-21T10:49:27Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Identity and PBP target supported; minor PvrR direction/context qualification
scientific_review: true
summary: The neutral parent structure and antibacterial filing are supported. Primary
  carbenicillin-bound PBP3 provides direct target evidence; WUS1 and AbuO have compound-specific
  functional support. The imported PvrR item needs a bounded note preserving gene-loss
  and phenotypic-switching context. The full original PvrR and BlaS papers were not
  obtained, so no new precise carbenicillin genotype/measurement claims are assigned
  from their abstracts.
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
  - path: data/antibiotics/antibacterial/carbenicillin.yaml
    sha256: 7426826434cd0b44e86b4ab46436e3c4ddc3e88ce06e506a145f2fc70f17f1c6
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
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: scripts/card_evidence_reviews.py
    sha256: f9ec8aff30066bf04b9c2757af7d6f5d179d045e57b9f3b352bbed0b851f50a8
    role: context
scope:
  description: Entire exact SEEDED record, five history events, all four resistance
    objects and the imported PBP target; maintained ChEBI/ARO rows and evidence overlays;
    all13 adopted compound,determinant and parent PMID leads; selected original binding/resistance
    studies.
  selection: Queue197; root original13 captured inputs retained, five actual ARO/evidence
    owner inputs appended before detailed inspection.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:3393
targets:
- target_id: CHEBI:3393
  path: data/antibiotics/antibacterial/carbenicillin.yaml
  label: carbenicillin
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
    role: Adopted ARO claim owner or evidence review override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Adopted ARO claim owner or evidence review override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Adopted ARO claim owner or evidence review override
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Maintained imported evidence review
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Maintained imported evidence review
checks:
- check_id: schema
  name: Documented schema check
  status: passed
  required: true
  summary: Exit0.
  target_ids:
  - CHEBI:3393
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/carbenicillin.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict check
  status: passed
  required: true
  summary: Exit0,zeroERRORrows.
  target_ids:
  - CHEBI:3393
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/carbenicillin.yaml --out /private/tmp/am-review-session/197-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Supplemental graph consistency
  status: passed
  required: false
  summary: Exit0 using019 RDKit interpreter against020 files.
  target_ids:
  - CHEBI:3393
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/197-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: adapter-catalog
  name: Structured source catalog
  status: passed
  required: false
  summary: Catalog inspected before protein web follow-up.
  target_ids:
  - CHEBI:3393
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets > /private/tmp/am-review-session/197-imodulondb-datasets.txt
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-pvrr
  name: Structured PvrR check
  status: passed
  required: false
  summary: No gene or component hit; no negative inference.
  target_ids:
  - CHEBI:3393
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism p_aeruginosa --dataset precise364 --query
    PvrR > /private/tmp/am-review-session/197-imodulondb-pvrr.txt
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-abuo
  name: Structured AbuO check
  status: passed
  required: false
  summary: No gene or component hit; no negative inference.
  target_ids:
  - CHEBI:3393
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism a_baumannii --dataset precise139 --query
    AbuO > /private/tmp/am-review-session/197-imodulondb-abuo.txt
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-pbp
  name: Structured PBP context
  status: passed
  required: false
  summary: One E.coli gene hit,no component hit;context only.
  target_ids:
  - CHEBI:3393
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset modulome --query penicillin
    > /private/tmp/am-review-session/197-imodulondb-pbp.txt
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
  - CHEBI:3393
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
  - CHEBI:3393
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
  - CHEBI:3393
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
  - CHEBI:3393
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
  - CHEBI:3393
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
  - CHEBI:3393
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
  - CHEBI:3393
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
  - CHEBI:3393
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
  - CHEBI:3393
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/carbenicillin.yaml
  locator: Entire YAML;five history events
  accessed_at: '2026-10-21T10:46:45Z'
  support: supports
  summary: Neutral carbenicillin is EXACT/SEEDED with three fixed penam stereocenters
    and one unspecified side-chain center. Four resistance items cite ARO as database
    assertions. The family-level PBP direct-binding target explicitly retains PRIMARY_EVIDENCE_NEEDED;
    no native MIC,causal graph or curated producer is asserted.
- evidence_id: chemistry
  kind: validation
  reference: CHEBI:3393;PubChem:20824;CHEMBL1214;KEGG:C06869
  locator: 197-chemistry.py/.json;current197-ols.json,197-pubchem.json,197-chembl.json,197-kegg.mol
  accessed_at: '2026-10-21T10:46:45Z'
  support: supports
  summary: SMILES/InChI/fullkey FPPNZSSZRUTDAP-UWFZAAFLSA-N,neutral C17H18N2O6S,masses
    and configured/unspecified stereochemistry agree. Parent penicillin/penicillin-allergen
    terms and native roles reproduce ChEBI. Neutral parent is distinct from disodium
    salt and indanyl prodrug; no side-chain enantiomer is newly imposed.
  snapshot_sha256: 36eae23b12f8a13eb91ca6b19b982bab7182ea2d47cd67b3b3eb2eb4363c9e22
- evidence_id: xrefs
  kind: database
  reference: KEGG:C06869;KEGG:D07614;DrugCentral:492;patent:US3142673
  locator: 197-kegg.txt;197-drugcentral.html;197-chebi.html;197-patent.html
  accessed_at: '2026-10-21T10:46:45Z'
  support: partial
  summary: KEGG compound and drug records resolve carbenicillin with matching parent
    chemistry; DrugCentral492 resolves the active drug with neutral formula/CAS and
    includes salt synonyms in drug context. Patent resolves as a penicillin document
    and remains document_xrefs,not exact identity. Current ChEBI retains HMDB/DrugBank/Reaxys
    mappings; direct HMDB and DrugBank retrievals failed403 and Reaxys was not accessed.
  snapshot_sha256: 21a451fbd652e264b2e072c30fa3a607b9d3c3b9eb5d9a8af6543f7fbac0e9c3
- evidence_id: binding
  kind: primary_source
  reference: PMID:20974151
  locator: DOI:10.1016/j.jmb.2010.10.024;197-pbp.xml full mainMethods/Results;PDB3OCL
  accessed_at: '2026-10-21T10:46:45Z'
  support: supports
  summary: P.aeruginosa PAO1 PBP3(ftsI),expressed as soluble residues35–579,forms
    a crystallographically observed carbenicillin acyl-enzyme at Ser294. This supports
    direct PBP binding at an exact organism/protein example while preserving the native
    family target. The opened beta-lactam adduct is not an exact chemical xref to
    free carbenicillin; neither binding nor thermal shift is a clinical susceptibility
    claim.
  snapshot_sha256: 75026b59acb4240144eb8e071588cf57fa73146d6b9d45ca705a999948a91f98
- evidence_id: wus
  kind: primary_source
  reference: PMID:36532482
  locator: DOI:10.3389/fmicb.2022.1059997;197-wus.xml mainMethods/Results andTables3–4
  accessed_at: '2026-10-21T10:46:45Z'
  support: supports
  summary: Myroides albus P34 WUS1 expressed in E.coli DH5alpha raises agar-dilution
    carbenicillin MIC from4 to1024mg/L. Purified WUS1 hydrolyzes carbenicillin(kcat/Km1.93per
    micromolar per second),supporting ANTIBIOTIC_INACTIVATION. Native-host resistance
    also has other determinants; the recombinant comparison does not establish WUS1
    as the sole cause of P34 resistance.
  snapshot_sha256: 05b441d27596cffdf0eb93057a45e09ac6ba7c3b54e30ced7aafdfa3776ff5a7
- evidence_id: abuo
  kind: primary_source
  reference: PMID:25512405
  locator: DOI:10.1128/AAC.03626-14;151-PMC4335886.html independently reread;Methods,Results,Table1;197-reused-abuo.json
  accessed_at: '2026-10-21T10:46:45Z'
  support: supports
  summary: A.baumannii AYE carbenicillin E-strip MIC is>512micrograms/mL in WT,128
    in the abuO mutant and>256 in complemented cells. This supports AbuO-associated
    resistance and an efflux-component interpretation. Fluorescent accumulation uses
    ethidium/ciprofloxacin,not direct purified carbenicillin transport; qPCR and broad
    physiology changes do not prove that AbuO alone exports this drug.
  snapshot_sha256: 9f5bfc6250b80c8d0538a9d6f28401f3e41d1f9246530acccf1cf130a4d80c9e
- evidence_id: pvrr
  kind: primary_source
  reference: PMID:11961556
  locator: DOI:10.1038/416740a;complete abstract197-core.json;originalFig3 caption197-pvrr-fig3.html
    andvisual197-pvrr-fig3.jpg
  accessed_at: '2026-10-21T10:46:45Z'
  support: partial
  summary: The abstract describes a regulator of switching between resistant and susceptible
    phenotypes. OriginalFig3 shows PvrR overexpression reducing variant frequency
    and deletion increasing it. The retrieved caption/figure does not independently
    supply a carbenicillin-specific deletion MIC or a porin mechanism; those details
    must not be invented from the abstract.
  snapshot_sha256: f99750aae651cb8b925bf4a7878ed5453b6976648c21fadb453e4b9666ff724a
- evidence_id: pvrr-authority
  kind: authority
  reference: ARO:3003688
  locator: 197-aro-stanzas.txt;currentCARD https://card.csu.mcmaster.ca/ontology/40325
  accessed_at: '2026-10-21T10:46:45Z'
  support: partial
  summary: The source defines a phenotypic-variant regulator and currentCARD includes
    gene conferring resistance via absence. The native imported note retains only
    a generic confers_resistance_to_antibiotic edge,so a qualification should preserve
    the loss/variant context instead of implying that increased wild-type PvrR necessarily
    confers resistance.
  snapshot_sha256: 739de517f4d064390f11dc6003e59cfc47660dc45a6fbcc1e46f4f2fcc4546eb
- evidence_id: blas
  kind: primary_source
  reference: PMID:9103972;PMID:15699201
  locator: 197-core.json complete abstracts;publisher2005 abstract
  accessed_at: '2026-10-21T10:46:45Z'
  support: partial
  summary: The1997 study purifies the M.smegmatis classA beta-lactamase;2005 deletion
    studies show BlaS contributes to beta-lactam susceptibility in M.smegmatis PM274/PM759.
    Full2005 compound-specific table was not accessible,so the native carbenicillin
    edge remains honestly database-supported without an independently extracted exact
    MIC or allele-specific kinetic value.
  snapshot_sha256: e4b2fee2f793a0cc9780775adc41461ff70047e890f9ed73b3e11192f45787f7
- evidence_id: other-leads
  kind: database
  reference: PMID:12569987;22648337;6176550;11585791;15673804;4248289;3055170;3889939
  locator: 197-core.json;197-lead-dispositions.json
  accessed_at: '2026-10-21T10:46:45Z'
  support: context_only
  summary: The three ChEBI leads concern beta-lactam IgE recognition,two-drug cross-reactivity
    and an analytical carbenicillin sensor; they are not antimicrobial-target experiments.
    ARO compound leads include two beta-lactamase reviews and1970 carbenicillin chemistry/mode-of-action
    metadata. PBP/penicillin-class references are reviews. All resolve;12569987,22648337,6176550,11585791
    and3055170 complete abstracts were read;15673804,4248289 and3889939 have no indexed
    abstracts.
  snapshot_sha256: e4b2fee2f793a0cc9780775adc41461ff70047e890f9ed73b3e11192f45787f7
- evidence_id: adapter
  kind: database
  reference: iModulonDB
  locator: 197-imodulondb-datasets.txt;197-imodulondb-pvrr.txt;197-imodulondb-abuo.txt;197-imodulondb-pbp.txt
  accessed_at: '2026-10-21T10:46:45Z'
  support: context_only
  summary: Native protein/regulator context was queried before literature follow-up.
    PvrR and AbuO returned no hits; generic penicillin search identified e_coli/modulome/b2430
    yfeW,PBP4B. No component was returned,so no summarize call was applicable. This
    neither supports nor refutes drug binding/resistance and is not transferred to
    the P.aeruginosa PBP3 experiment.
  snapshot_sha256: 98627808541dbd07b37e85a4bfb692fc0fe8a0a9564839813c9f2f9ac41a4a10
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_resistance_edges.tsv;data/raw/aro_target_edges.tsv;curation/card_evidence_reviews.json
  locator: Adopted exact rows,extractor/seeder and maintained evidence-review mechanism
  accessed_at: '2026-10-21T10:46:45Z'
  support: supports
  summary: Four resistance rows and the target reproduce source inventories; no existing
    exact qualification was found in the ignored-inclusive curation/conf search. Imported
    evidence notes can be qualified through card_evidence_reviews.json with the exactsource-row
    hash and target structure; no native-only patch is needed.
  search_scope: rg --no-ignore --hidden for3003688,3004578,3005111,3007435,CHEBI:3393,ARO:0000043
    over curation/conf; card_evidence_reviews.json searched for applicable entries.
- evidence_id: validation
  kind: validation
  reference: Focused schema/strict/chemistry
  locator: 197-strict.tsv;197-chemistry.json
  accessed_at: '2026-10-21T10:46:45Z'
  support: supports
  summary: Native schema/strict exit0;019 RDKit command against020 files exit0;required
    shared corpus gates are distinct.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact parent representation
  outcome: supported
  summary: Public source graphs agree; no salt/prodrug or new side-chain stereochemistry
    is substituted.
  target_ids:
  - CHEBI:3393
  evidence_ids:
  - chemistry
  - xrefs
- assessment_id: class
  area: grounding
  topic: Antibacterial roles and parents
  outcome: supported
  summary: Roles/parents reproduce authorities and compound-specific binding/resistance
    experiments concern an antibacterial penicillin.
  target_ids:
  - CHEBI:3393
  evidence_ids:
  - chemistry
  - binding
  - wus
- assessment_id: target
  area: evidence
  topic: PBP direct target
  outcome: supported
  summary: Original carbenicillin acyl-enzyme structure supplies primary support for
    a bounded PBP example; current database status remains honest.
  target_ids:
  - CHEBI:3393
  evidence_ids:
  - binding
  - record
- assessment_id: resistance
  area: evidence
  topic: WUS1/AbuO/BlaS
  outcome: supported
  summary: WUS1 exact hydrolysis and AbuO phenotype are supported. BlaS remains a
    database assertion with class-level primary abstracts; no quantitative upgrade
    is claimed.
  target_ids:
  - CHEBI:3393
  evidence_ids:
  - wus
  - abuo
  - blas
- assessment_id: pvrr
  area: scope
  topic: PvrR direction and condition
  outcome: concern
  summary: Add loss/phenotypic-switching qualification. Exact carbenicillin perturbation
    details remain unresolved.
  target_ids:
  - CHEBI:3393
  evidence_ids:
  - pvrr
  - pvrr-authority
- assessment_id: provenance
  area: provenance
  topic: References and history
  outcome: supported
  summary: All13 adopted/parent PMID leads resolved at stated depths and five history
    events checked.
  target_ids:
  - CHEBI:3393
  evidence_ids:
  - other-leads
  - owners
  - record
- assessment_id: schema
  area: schema
  topic: Focused gates
  outcome: supported
  summary: Focused schema/strict and alternate-environment chemistry pass.
  target_ids:
  - CHEBI:3393
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: chebi-3393-pvrr-loss-variant-context
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify PvrR with its loss and phenotypic-switching context
  description: The imported PvrR note exposes a generic resistance edge without the
    source gene-absence qualification. CurrentCARD and the original perturbation figure
    distinguish loss/variant formation from overexpression. Retain UNKNOWN and database
    provenance,but add the bounded direction/context note; do not invent a carbenicillin-specific
    deletion MIC or classify PvrR as an antibiotic efflux protein.
  target_ids:
  - CHEBI:3393
  field_paths:
  - resistance_mechanisms[0].evidence[0].notes
  evidence_ids:
  - pvrr
  - pvrr-authority
  - owners
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Curated qualification of exact imported resistance row
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Evidence-review validation and application
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Adopted PvrR carbenicillin edge
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Regenerate qualified imported claim
  rule_id: 'review-checklist: resistance direction,context and honest imported evidence'
  native_severity: minor non-blocking source-context omission
  normalization_reason: The record already labels the routeUNKNOWN and cites database
    provenance; the missing condition can mislead interpretation but does not assert
    a specific contrary perturbation experiment.
actions:
- action_id: A1
  description: Add a source-preserving PvrR qualification through the maintained imported-evidence
    review.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:3393
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Curated qualification of exact imported resistance row
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Evidence-review validation and application
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Adopted PvrR carbenicillin edge
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Regenerate qualified imported claim
  acceptance_checks:
  - Bind the qualification to the exactARO3003688/carbenicillin source-row SHA and
    CHEBI3393 fullstructurekey; preserve CARD citation and UNKNOWN rather than fabricating
    a primary mechanism.
  - Explain source loss/phenotypic-switching context and original Fig3 direction;
    explicitly leave exact carbenicillin-specific genotype/measurement support unresolved
    until the complete original experiment is inspected.
  - Regenerate through the existing evidence-review merge path and confirm the intended
    note survives; run focused schema/strict and required reference/history,source
    and full-corpus gates.
limitations:
- 'PvrR full2002 text was not obtained: publisher .pdf returned HTML and third-party
  full-text route challenged. Complete abstract and originalFig3/caption were inspected;
  no carbenicillin-specific PvrR MIC is independently verified.'
- BlaS1997/2005 complete abstracts were read; the2005 fulltext/PDF routes returned403.
  Exact carbenicillin table remains unextracted. This does not refute the honestly
  labelled CARD edge.
- All13 adopted compound/determinant/parent PMID records were resolved. Three lacked
  indexed abstracts; several other papers were abstract-only. Sensor/IgE studies were
  not repurposed as antibacterial mechanism experiments.
- PBP and WUS1 original mainMethods/Results and relevant tables were inspected; raw
  diffraction data and raw enzyme traces were not reprocessed. PBP3 direct binding
  is one organism/protein example,not proof that allPBPs or bacterial strains are
  equally affected.
- AbuO original cachedHTML from review151 was independently reread and hashed; new
  EuropePMC XML retrieval failed500. Direct transport measurements used fluorescent
  probe drugs rather than carbenicillin.
- HMDB andDrugBank direct requests failed403; Reaxys was not accessed. Their mappings
  are retained as unverified direct-registry comparisons despite currentChEBI provenance.
  DrugCentral includes salt/product context and does not change the neutral native
  structure.
- 020 lacksRDKit; chemistry used019 interpreter against020 files. Native schema/strict
  passed in020. No exhaustive clinical,allergy,stereoisomer or resistance survey was
  undertaken; no native status promotion is implied.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 18 repository input hashes plus externalARO cache remain unchanged; no native
  or saved-bundle changes.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://doi.org/10.1016/j.jmb.2010.10.024
- https://doi.org/10.1038/416740a
- https://doi.org/10.3389/fmicb.2022.1059997
tags:
- record-review
- carbenicillin
- resistance-context
```
