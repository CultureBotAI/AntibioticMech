# Cefazedone: exact neutral identity and qualified primary antibacterial evidence

- Review: 20261021T111112Z-cefazedone
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:55:27Z
- Finished UTC: 2026-10-21T11:11:12Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

No confirmed native defect. The exact neutral cefazedone structure, source mints, chemical parents, first-generation cephalosporin class and antibacterial roles are supported. Primary antibacterial abstracts identify the exact compound, while the inspected full clinical PK/PD paper concerns cefazedone sodium and selected susceptible isolates. These sources offer bounded optional enrichment without proving a cefazedone-specific PBP mechanism or supporting unqualified transfer of salt/formulation measurements. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole-record review of exact neutral cefazedone.

Selection: Queue 213 in isolated batch 022; original capture retained and actual ARO source owner appended before detailed judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:131731 | data/antibiotics/antibacterial/cefazedone.yaml | generated | cefazedone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | CHEBI:131731 | Actual focused command passed with zero errors. |
| Focused strict | passed | True | CHEBI:131731 | Actual focused command passed with zero errors. |
| Independent molecular encodings and source mints | passed | True | CHEBI:131731 | SMILES/InChI, full key, formula, charge, masses, two R centres and both source mints agree. |
| Authoritative full QC | failed | True | CHEBI:131731 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:131731 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:131731 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:131731 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:131731 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:131731 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:131731 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:131731 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:131731 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral cefazedone

identity: supported. Targets: CHEBI:131731.

Native identity, graph, stereochemistry, masses and both mints agree with current authorities and independent structure databases. Sodium formulations and patent salts are not conflated with the acid.

### Chemical parents and antibacterial role

grounding: supported. Targets: CHEBI:131731.

The graph satisfies all broader chemical parents, and source-supported first-generation cephalosporin/antibiotic context is consistent with direct antibacterial studies. Filing does not depend merely on family membership.

### Exact, drug and document references

grounding: unknown. Targets: CHEBI:131731.

Public exact mappings agree; drug and document references resolve within their permitted scope. Reaxys 5399221 remains authority-asserted without independent registry detail.

### Structural description

evidence: supported. Targets: CHEBI:131731.

Native substituent positions and chemical groups agree with the molecular graph and authority. The native definition does not assert a taxon-specific PBP or clinical outcome.

### Optional compound-specific PBP mechanism

evidence: unknown. Targets: CHEBI:131731.

ARO/KEGG provide a class-consistent PBP/cell-wall description, but inspected primary abstracts and full CAP study do not measure cefazedone binding or cross-linking. No native structured mechanism is asserted; a direct source is needed before primary annotation.

### Primary antibacterial and formulation scope

evidence: supported. Targets: CHEBI:131731.

Historical primary assays establish cefazedone antibacterial activity. The full CAP paper concerns sodium-form treatment and preselected susceptible clinical isolates; neither its small panel nor older pooled abstract ranges justify a universal species spectrum.

### Susceptibility versus resistance mechanism

evidence: unknown. Targets: CHEBI:131731.

The gonococcal abstract includes penicillin-resistant beta-lactamase-producing isolates, but this does not identify a cefazedone resistance determinant or establish universal stability to beta-lactamases. Native resistance fields are empty.

### Clinical study versus regulatory assertion

scope: supported. Targets: CHEBI:131731.

The primary sodium-treatment study supports historical clinical investigation only. It is uncontrolled and small; no current regulatory jurisdiction or universal treatment recommendation is inferred. Native has no clinical-status claim.

### Adapters, natural production and causal graphs

scope: not_applicable. Targets: CHEBI:131731.

Native has no named protein/gene/pathway, natural producer, dataset or graph claim. Synthetic patent processes do not establish natural production.

### Source ownership and seeded history

provenance: supported. Targets: CHEBI:131731.

Both source concepts and four seed events are coherent. The actual ARO owner was captured before judgment; SEEDED remains unchanged.

### Bounded enrichment opportunities

completeness: supported. Targets: CHEBI:131731.

Primary abstracts and the full sodium study provide optional activity leads, with clear form and protocol limits. Empty optional fields alone do not create a defect.

### Focused gates

schema: supported. Targets: CHEBI:131731.

Schema, strict and independent structure/mint checks pass; source review provides the separate scientific assessment.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optionally curate primary antibacterial observations after exact assay/material resolution.

- Retrieve the original methods/tables for selected 1979 susceptibility or bactericidal papers before adopting individual MICs or MBCs; retain exact strains, material form, medium and inoculum.
- Keep sodium-form CAP treatment, model PK/PD exposure and in-vitro broth susceptibility as separate observations. Do not silently equate tested sodium/formulation material with the exact neutral acid.
- Do not infer contemporary clinical breakpoints or a species-wide activity spectrum from selected susceptible isolates or abstract-level panel ranges.
- Keep gentamicin/etimicin combination experiments separate from cefazedone monotherapy.
- Run native schema, strict, evidence/term/reference/history and applicable corpus gates after separately authorized curation.

### A2

Optionally corroborate Reaxys and direct mechanism evidence.

- Confirm Reaxys 5399221 against the complete neutral stereochemical graph when permissible registry detail is available; do not delete it based only on access limits.
- Locate compound-specific PBP or peptidoglycan experiments before adding primary-evidenced mode/target/graph claims; ARO or KEGG annotations alone do not provide experimental assay context.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/cefazedone.yaml; Entire YAML | supports | Read identity, structural definition, source synonyms, six parents, two roles, structural class, complete neutral structure, five exact xrefs, two drug xrefs, six document xrefs, both source concepts and four seed events. No populated mode, molecular_targets, activity_spectrum, resistance, producer, clinical or graph fields. |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; ChEBI row 2481, ARO row 569; actual extraction/seeding owners | supports | ChEBI supplies the exact structure/definition/roles and ten PMID leads. ARO supplies class/identity cross-references and repeats PMID 39575. Thus there are ten unique adopted leads, not eleven. Original captures and actual owner inputs were preserved before judgment. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:131731; Current identity, ontology and retained references | supports | Current ChEBI matches neutral C18H15Cl2N5O5S3 and VTLCNEGVSVJLDN-MLGOLLRUSA-N. Parent concepts are 4-pyridones, cephalosporin, carboxylic acid, thiadiazoles and semisynthetic derivative; each is broader than the exact structure. Retained antibiotic and antibacterial-drug context is coherent. |
| aro | https://card.mcmaster.ca/aro/3009110; Current cefazedone entry | supports | ARO identifies cefazedone as a semisynthetic first-generation cephalosporin and retains exact identity references. Its PBP description is database context and its PMID 39575 supports antibacterial comparison, not a directly inspected PBP binding assay. Native uses the structural ChEBI definition rather than importing that mechanism prose. |
| chemistry | Independent RDKit 2026.03.5 check; 213-chemistry.json | supports | Both encodings independently reproduce one neutral fragment, exact complete key/formula, matching average/exact masses and two R stereocentres. Both source mints match their exact source identifiers. The pyridone aromatic representation parses consistently with InChI. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/71736; Current full PUG structure | supports | CID 71736 independently matches the complete native stereochemical key and formula, including the dichloropyridone and methylthiadiazole substituents. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL2107636.json; Current exact structure | supports | CHEMBL2107636 has the same neutral formula and complete key; no exact-salt mismatch was found. |
| cas | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/56187-47-4/property/InChIKey/JSON; CAS-name query | supports | CAS 56187-47-4 resolves to CID 71736 with the exact native key. |
| reaxys | https://www.ebi.ac.uk/chebi/CHEBI:131731; Current Reaxys 5399221 mapping | partial | The mapping is retained by current ChEBI. Independent Reaxys registry contents were not inspected through free public access; no contrary identity was demonstrated. |
| kegg-drug | https://rest.kegg.jp/get/D07237; Current drug identity and class | supports | D07237 resolves to cefazedone with the neutral formula and first-generation cephalosporin drug classification. Its PBP/pathway annotation is database context, not a primary binding experiment or current approval evidence. |
| drugcentral | https://drugcentral.org/drugcard/3071; Current drug card identity | supports | DrugCentral 3071 resolves to cefazedone. Drug-reference placement is appropriate; the page is not used to assert jurisdiction-specific current approval. |
| patent-main | https://patents.google.com/patent/US4153693A/en; Description and claim 8 | context_only | The patent concerns oxopyridylacetamido cephalosporins. Claim 8 expressly names the matching dichloropyridyl/methylthiadiazolyl active moiety and allows alkali-metal salts. This is relevant document context, without treating the whole patent family or its formulations as exact structural equivalence. |
| patent-initial | https://patents.google.com/patent/DE2345402A1/en; Title and description | context_only | The retained document resolves to cephem derivatives and preparation processes, with oxopyridyl substituent chemistry. It is appropriately a document reference. |
| patent-process1 | https://patents.google.com/patent/DE2621011A1/en; Title, description and relation to DE2345402 | context_only | This resolved process document explicitly describes a supplement to the earlier cephem-derivative patent. Its broad process scope is not a cefazedone-only activity claim. |
| patent-process2 | https://patents.google.com/patent/DE2626026A1/en; Title and description | context_only | This document concerns synthesis of cephem derivatives with acyl and heteroaromatic substituent options. Document relevance is preserved without assigning all products or examples to cefazedone. |
| patent-process3 | https://patents.google.com/patent/DE2627204A1/en; Title and description | context_only | The resolved document concerns dihydro-oxopyridyl cephalosporin preparation and includes methylthiadiazolyl substituent options. It is not a native exact compound xref. |
| wiki | https://en.wikipedia.org/wiki/Cefazedone; Resolved document reference | context_only | The link resolves to cefazedone; it is not used as primary experiment evidence. |
| adopted-leads | Europe PMC MED core records; All ten unique adopted PMID titles and abstracts | context_only | PMIDs 39575 and 582713 concern antibacterial comparison/panels; 114187 gonococcal isolates; 385008 bactericidal effects; 385009 and 385010 experimental rat pyelonephritis; 546431 tissue/bile penetration; 25464101 analytical pharmacokinetics with etimicin; 25947397 sodium-form CAP PK/PD; and 29017833 an allergy review. Host disposition, combination effects, experimental infection and allergy context are not direct PBP measurements. |
| primary-antibacterial | https://pubmed.ncbi.nlm.nih.gov/114187/; Primary abstract; related primary abstracts PMIDs 39575, 582713 and 385008 | supports | The gonococcal paper explicitly identifies cefazedone by its full (6R,7R) chemical name and reports a measured MIC range across 67 historical isolates. Other primary abstracts report antibacterial or bactericidal effects in defined panels. These support compound-specific antibacterial activity, but full protocols, individual strain identities and reagent forms were not recovered for numeric row adoption. |
| primary-cap | https://doi.org/10.4103/0366-6999.156086; PMID 25947397; complete primary XML, Methods and Tables 3–4 | supports | This open-label, uncontrolled ten-patient study administers cefazedone sodium. Six baseline clinical isolates were eligible after susceptible disk tests; later broth MICs ranged 0.25–1 mg/L. Table 4 distinguishes two H. influenzae, two S. aureus, one K. pneumoniae and one S. pneumoniae observation. These are selected isolates and a sodium-form treatment study; exact AST reagent form and detailed broth conditions are insufficient for unqualified neutral-acid quantitative transfer. Clinical response and modeled free-time-above-MIC are not bacterial target assays. |
| search | Ignored-inclusive repository and public source follow-up; 213-owner-hits.txt; exact identifier, label, slug and key | context_only | Search included ignored and hidden files outside .git/.venv. Native/raw/generated references and historical review leads were distinguished; no exact curator override was identified. Native has no named gene/protein/pathway claim requiring an adapter query. |
| gates | Actual focused native checks; 213-focused-results.json; 213-validation.tsv | supports | Schema and strict pass on the exact target; source-aware chemistry passes. Expanded captured input hashes were rechecked unchanged. |

## Limits And Additional Notes

- Reaxys 5399221 was corroborated as a live ChEBI mapping but its registry contents were not independently inspected.
- All ten unique adopted PMID metadata/abstract records were read; complete primary text was inspected for PMID 25947397, not every older susceptibility, tissue-penetration or animal-infection paper.
- The complete PK/PD study uses cefazedone sodium treatment and selected susceptible isolates. Its detailed AST reagent form and broth protocol are insufficient for unqualified exact-neutral-acid quantitative transfer.
- No cefazedone-specific primary PBP experiment was established in this bounded review; database mechanism context remains separate from optional primary annotation.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Initial capture preserved and actual ARO inventory added before assessment. All expanded source hashes unchanged; no native/source/status/history edits.
- Schema/strict used batch 022; chemistry used locked batch 019 RDKit 2026.03.5 against batch 022 cwd.
- All five native patent identifiers resolve as relevant chemical/process documents; their broad derivative and salt scope is not an exact structural equivalence assertion.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T111112Z-cefazedone
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cefazedone: exact neutral identity and qualified primary antibacterial evidence'
started_at: '2026-10-21T10:55:27Z'
finished_at: '2026-10-21T11:11:12Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independent complete native/actual ARO and ChEBI owner review,
    current structure/identifier checks, all ten unique adopted citation abstracts,
    relevant patent text and full 2015 cefazedone sodium primary study.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: No confirmed native defect. The exact neutral cefazedone structure, source
  mints, chemical parents, first-generation cephalosporin class and antibacterial
  roles are supported. Primary antibacterial abstracts identify the exact compound,
  while the inspected full clinical PK/PD paper concerns cefazedone sodium and selected
  susceptible isolates. These sources offer bounded optional enrichment without proving
  a cefazedone-specific PBP mechanism or supporting unqualified transfer of salt/formulation
  measurements. Scientific assessment retains the stated evidence limits; full verification
  is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/cefazedone.yaml
    sha256: 8ff10d1583f43d947ad15e844fb75909af7960e8956ce3034d8445b48077c85d
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 25f0d80c0bf26da7741a1514a5e1759dde484ab054f0f56df7938bdda8383a91
    role: context
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
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
- target_id: CHEBI:131731
  path: data/antibiotics/antibacterial/cefazedone.yaml
  label: cefazedone
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted exact ChEBI identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO class, exact identity and source citation leads
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
  description: Whole-record review of exact neutral cefazedone.
  selection: Queue 213 in isolated batch 022; original capture retained and actual
    ARO source owner appended before detailed judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:131731
  exclusions:
  - target: Cefazedone sodium, cefazolin, cephalothin, etimicin combinations and related
      patent derivatives
    reason: Distinct chemical forms, comparators or mixtures; their results retain
      exact material and treatment scope.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual focused command passed with zero errors.
  target_ids:
  - CHEBI:131731
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefazedone.yaml
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
  - CHEBI:131731
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefazedone.yaml --out /private/tmp/am-review-session/213-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Independent molecular encodings and source mints
  status: passed
  required: true
  summary: SMILES/InChI, full key, formula, charge, masses, two R centres and both
    source mints agree.
  target_ids:
  - CHEBI:131731
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/check199200.py
    213 (cwd /private/tmp/antibioticmech-record-reviews-022)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:131731
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
  - CHEBI:131731
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
  - CHEBI:131731
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
  - CHEBI:131731
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
  - CHEBI:131731
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
  - CHEBI:131731
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
  - CHEBI:131731
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
  - CHEBI:131731
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
  - CHEBI:131731
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/cefazedone.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T11:03:41Z'
  support: supports
  summary: Read identity, structural definition, source synonyms, six parents, two
    roles, structural class, complete neutral structure, five exact xrefs, two drug
    xrefs, six document xrefs, both source concepts and four seed events. No populated
    mode, molecular_targets, activity_spectrum, resistance, producer, clinical or
    graph fields.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv
  locator: ChEBI row 2481, ARO row 569; actual extraction/seeding owners
  accessed_at: '2026-10-21T11:03:41Z'
  support: supports
  summary: ChEBI supplies the exact structure/definition/roles and ten PMID leads.
    ARO supplies class/identity cross-references and repeats PMID 39575. Thus there
    are ten unique adopted leads, not eleven. Original captures and actual owner inputs
    were preserved before judgment.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:131731
  locator: Current identity, ontology and retained references
  accessed_at: '2026-10-21T11:01:14Z'
  support: supports
  summary: Current ChEBI matches neutral C18H15Cl2N5O5S3 and VTLCNEGVSVJLDN-MLGOLLRUSA-N.
    Parent concepts are 4-pyridones, cephalosporin, carboxylic acid, thiadiazoles
    and semisynthetic derivative; each is broader than the exact structure. Retained
    antibiotic and antibacterial-drug context is coherent.
  snapshot_sha256: 0ad623087b9385e2c94af45ccf6c3b1315a8a0b04e2f750d72e229e8e834c718
- evidence_id: aro
  kind: authority
  reference: https://card.mcmaster.ca/aro/3009110
  locator: Current cefazedone entry
  accessed_at: '2026-10-21T11:01:14Z'
  support: supports
  summary: ARO identifies cefazedone as a semisynthetic first-generation cephalosporin
    and retains exact identity references. Its PBP description is database context
    and its PMID 39575 supports antibacterial comparison, not a directly inspected
    PBP binding assay. Native uses the structural ChEBI definition rather than importing
    that mechanism prose.
  snapshot_sha256: a5420a5c057d33d165bd899392b6bca118248b98b146972a30c9b9eb2229b919
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit 2026.03.5 check
  locator: 213-chemistry.json
  accessed_at: '2026-10-21T11:00:42Z'
  support: supports
  summary: Both encodings independently reproduce one neutral fragment, exact complete
    key/formula, matching average/exact masses and two R stereocentres. Both source
    mints match their exact source identifiers. The pyridone aromatic representation
    parses consistently with InChI.
  snapshot_sha256: e0a874ea219b3b54982b9c72c8be25eda2cf3a41c3a1c43a82e308fae3445d79
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/71736
  locator: Current full PUG structure
  accessed_at: '2026-10-21T11:01:15Z'
  support: supports
  summary: CID 71736 independently matches the complete native stereochemical key
    and formula, including the dichloropyridone and methylthiadiazole substituents.
  snapshot_sha256: a204361643d7efb9d60b24127ffeed99039734ac38a038065992dd7c7ea5f69d
- evidence_id: chembl
  kind: database
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL2107636.json
  locator: Current exact structure
  accessed_at: '2026-10-21T11:01:15Z'
  support: supports
  summary: CHEMBL2107636 has the same neutral formula and complete key; no exact-salt
    mismatch was found.
  snapshot_sha256: 47f39a3ad4f2357ecddd96c4e8fc6a15d14c041b23d9b01cdb9627f3b0c016ee
- evidence_id: cas
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/56187-47-4/property/InChIKey/JSON
  locator: CAS-name query
  accessed_at: '2026-10-21T11:01:15Z'
  support: supports
  summary: CAS 56187-47-4 resolves to CID 71736 with the exact native key.
  snapshot_sha256: 7744b7df7cacc5760fef750e4764718ee9a5b14dd91ffcc188390d12c8dc811c
- evidence_id: reaxys
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:131731
  locator: Current Reaxys 5399221 mapping
  accessed_at: '2026-10-21T11:01:14Z'
  support: partial
  summary: The mapping is retained by current ChEBI. Independent Reaxys registry contents
    were not inspected through free public access; no contrary identity was demonstrated.
  snapshot_sha256: 0ad623087b9385e2c94af45ccf6c3b1315a8a0b04e2f750d72e229e8e834c718
- evidence_id: kegg-drug
  kind: database
  reference: https://rest.kegg.jp/get/D07237
  locator: Current drug identity and class
  accessed_at: '2026-10-21T11:01:15Z'
  support: supports
  summary: D07237 resolves to cefazedone with the neutral formula and first-generation
    cephalosporin drug classification. Its PBP/pathway annotation is database context,
    not a primary binding experiment or current approval evidence.
  snapshot_sha256: 7579264591343807eb14b6034bb6afbfb3a4955719958a3366e7447915cea93c
- evidence_id: drugcentral
  kind: database
  reference: https://drugcentral.org/drugcard/3071
  locator: Current drug card identity
  accessed_at: '2026-10-21T11:01:15Z'
  support: supports
  summary: DrugCentral 3071 resolves to cefazedone. Drug-reference placement is appropriate;
    the page is not used to assert jurisdiction-specific current approval.
  snapshot_sha256: 84f6edc119e749785bc23eaf4deab09488dd9ab88126eb11156171746c71baad
- evidence_id: patent-main
  kind: primary_source
  reference: https://patents.google.com/patent/US4153693A/en
  locator: Description and claim 8
  accessed_at: '2026-10-21T11:01:16Z'
  support: context_only
  summary: The patent concerns oxopyridylacetamido cephalosporins. Claim 8 expressly
    names the matching dichloropyridyl/methylthiadiazolyl active moiety and allows
    alkali-metal salts. This is relevant document context, without treating the whole
    patent family or its formulations as exact structural equivalence.
  snapshot_sha256: eaed47af810598b1def5263423a7defcf732527e1cd72b60a11a441388332fda
- evidence_id: patent-initial
  kind: primary_source
  reference: https://patents.google.com/patent/DE2345402A1/en
  locator: Title and description
  accessed_at: '2026-10-21T11:01:15Z'
  support: context_only
  summary: The retained document resolves to cephem derivatives and preparation processes,
    with oxopyridyl substituent chemistry. It is appropriately a document reference.
  snapshot_sha256: 7f107cafc750e4d6ae6a094ca3d701f1aa929a472909d24096c63a210b6f8857
- evidence_id: patent-process1
  kind: primary_source
  reference: https://patents.google.com/patent/DE2621011A1/en
  locator: Title, description and relation to DE2345402
  accessed_at: '2026-10-21T11:01:16Z'
  support: context_only
  summary: This resolved process document explicitly describes a supplement to the
    earlier cephem-derivative patent. Its broad process scope is not a cefazedone-only
    activity claim.
  snapshot_sha256: 6783444fe30e23e3404a11296b8388a64244bbc70e1a0b5dae0ac1bd8c50418d
- evidence_id: patent-process2
  kind: primary_source
  reference: https://patents.google.com/patent/DE2626026A1/en
  locator: Title and description
  accessed_at: '2026-10-21T11:01:16Z'
  support: context_only
  summary: This document concerns synthesis of cephem derivatives with acyl and heteroaromatic
    substituent options. Document relevance is preserved without assigning all products
    or examples to cefazedone.
  snapshot_sha256: e8f87e8736f5183c26ae1e70cd9000a3975649bc443c7e84efb03b448c7b500b
- evidence_id: patent-process3
  kind: primary_source
  reference: https://patents.google.com/patent/DE2627204A1/en
  locator: Title and description
  accessed_at: '2026-10-21T11:01:16Z'
  support: context_only
  summary: The resolved document concerns dihydro-oxopyridyl cephalosporin preparation
    and includes methylthiadiazolyl substituent options. It is not a native exact
    compound xref.
  snapshot_sha256: d471a8c5bdf34b39dfc1e87c4849bddc6a4ddb87088758916a0dfef105c928b9
- evidence_id: wiki
  kind: database
  reference: https://en.wikipedia.org/wiki/Cefazedone
  locator: Resolved document reference
  accessed_at: '2026-10-21T11:01:16Z'
  support: context_only
  summary: The link resolves to cefazedone; it is not used as primary experiment evidence.
  snapshot_sha256: 806f5aaa493ebeeeff806143cb733c6e82afd1f3500c46cac8dba697db4a4e2c
- evidence_id: adopted-leads
  kind: database
  reference: Europe PMC MED core records
  locator: All ten unique adopted PMID titles and abstracts
  accessed_at: '2026-10-21T11:01:14Z'
  support: context_only
  summary: PMIDs 39575 and 582713 concern antibacterial comparison/panels; 114187
    gonococcal isolates; 385008 bactericidal effects; 385009 and 385010 experimental
    rat pyelonephritis; 546431 tissue/bile penetration; 25464101 analytical pharmacokinetics
    with etimicin; 25947397 sodium-form CAP PK/PD; and 29017833 an allergy review.
    Host disposition, combination effects, experimental infection and allergy context
    are not direct PBP measurements.
  snapshot_sha256: f6026f46ad2befce8673fb311c8646afec6777ef0255bd1805a08214ea78cf38
- evidence_id: primary-antibacterial
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/114187/
  locator: Primary abstract; related primary abstracts PMIDs 39575, 582713 and 385008
  accessed_at: '2026-10-21T11:01:14Z'
  support: supports
  summary: The gonococcal paper explicitly identifies cefazedone by its full (6R,7R)
    chemical name and reports a measured MIC range across 67 historical isolates.
    Other primary abstracts report antibacterial or bactericidal effects in defined
    panels. These support compound-specific antibacterial activity, but full protocols,
    individual strain identities and reagent forms were not recovered for numeric
    row adoption.
  snapshot_sha256: f6026f46ad2befce8673fb311c8646afec6777ef0255bd1805a08214ea78cf38
- evidence_id: primary-cap
  kind: primary_source
  reference: https://doi.org/10.4103/0366-6999.156086
  locator: PMID 25947397; complete primary XML, Methods and Tables 3–4
  accessed_at: '2026-10-21T11:02:06Z'
  support: supports
  summary: This open-label, uncontrolled ten-patient study administers cefazedone
    sodium. Six baseline clinical isolates were eligible after susceptible disk tests;
    later broth MICs ranged 0.25–1 mg/L. Table 4 distinguishes two H. influenzae,
    two S. aureus, one K. pneumoniae and one S. pneumoniae observation. These are
    selected isolates and a sodium-form treatment study; exact AST reagent form and
    detailed broth conditions are insufficient for unqualified neutral-acid quantitative
    transfer. Clinical response and modeled free-time-above-MIC are not bacterial
    target assays.
  snapshot_sha256: e598c0c4627d7e8a521f9db09ee82f51ef855c851a1654c28de6c207eacd2981
- evidence_id: search
  kind: search
  reference: Ignored-inclusive repository and public source follow-up
  locator: 213-owner-hits.txt; exact identifier, label, slug and key
  accessed_at: '2026-10-21T11:00:21Z'
  support: context_only
  summary: Search included ignored and hidden files outside .git/.venv. Native/raw/generated
    references and historical review leads were distinguished; no exact curator override
    was identified. Native has no named gene/protein/pathway claim requiring an adapter
    query.
  snapshot_sha256: 29952090a1ea30ab8c52bcedd3756736adaf7792940fd1c0984dc5ae4aba1b15
  search_scope: rg --no-ignore --hidden across isolated batch 022 outside .git/.venv;
    exact cefazedone/CHEBI:131731/ARO:3009110/full-key search; public ChEBI/ARO/ChEMBL/PubChem/KEGG/DrugCentral,
    patent text and EPMC abstract/full XML follow-up accessed 2026-10-21.
- evidence_id: gates
  kind: validation
  reference: Actual focused native checks
  locator: 213-focused-results.json; 213-validation.tsv
  accessed_at: '2026-10-21T11:00:42Z'
  support: supports
  summary: Schema and strict pass on the exact target; source-aware chemistry passes.
    Expanded captured input hashes were rechecked unchanged.
  snapshot_sha256: ddf63b82202d2a6e28926f3ab16f4e5586f3fb395bb3759256c0945aeb9cc3a3
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral cefazedone
  outcome: supported
  summary: Native identity, graph, stereochemistry, masses and both mints agree with
    current authorities and independent structure databases. Sodium formulations and
    patent salts are not conflated with the acid.
  target_ids:
  - CHEBI:131731
  evidence_ids:
  - native
  - chebi
  - aro
  - chemistry
  - pubchem
  - chembl
  - cas
  - patent-main
- assessment_id: classification
  area: grounding
  topic: Chemical parents and antibacterial role
  outcome: supported
  summary: The graph satisfies all broader chemical parents, and source-supported
    first-generation cephalosporin/antibiotic context is consistent with direct antibacterial
    studies. Filing does not depend merely on family membership.
  target_ids:
  - CHEBI:131731
  evidence_ids:
  - chebi
  - aro
  - kegg-drug
  - primary-antibacterial
  - primary-cap
- assessment_id: xref
  area: grounding
  topic: Exact, drug and document references
  outcome: unknown
  summary: Public exact mappings agree; drug and document references resolve within
    their permitted scope. Reaxys 5399221 remains authority-asserted without independent
    registry detail.
  target_ids:
  - CHEBI:131731
  evidence_ids:
  - pubchem
  - chembl
  - cas
  - reaxys
  - kegg-drug
  - drugcentral
  - patent-main
  - patent-initial
  - patent-process1
  - patent-process2
  - patent-process3
  - wiki
- assessment_id: definition
  area: evidence
  topic: Structural description
  outcome: supported
  summary: Native substituent positions and chemical groups agree with the molecular
    graph and authority. The native definition does not assert a taxon-specific PBP
    or clinical outcome.
  target_ids:
  - CHEBI:131731
  evidence_ids:
  - native
  - chebi
  - chemistry
- assessment_id: mechanism
  area: evidence
  topic: Optional compound-specific PBP mechanism
  outcome: unknown
  summary: ARO/KEGG provide a class-consistent PBP/cell-wall description, but inspected
    primary abstracts and full CAP study do not measure cefazedone binding or cross-linking.
    No native structured mechanism is asserted; a direct source is needed before primary
    annotation.
  target_ids:
  - CHEBI:131731
  evidence_ids:
  - aro
  - kegg-drug
  - adopted-leads
  - primary-cap
- assessment_id: activity
  area: evidence
  topic: Primary antibacterial and formulation scope
  outcome: supported
  summary: Historical primary assays establish cefazedone antibacterial activity.
    The full CAP paper concerns sodium-form treatment and preselected susceptible
    clinical isolates; neither its small panel nor older pooled abstract ranges justify
    a universal species spectrum.
  target_ids:
  - CHEBI:131731
  evidence_ids:
  - primary-antibacterial
  - primary-cap
- assessment_id: resistance
  area: evidence
  topic: Susceptibility versus resistance mechanism
  outcome: unknown
  summary: The gonococcal abstract includes penicillin-resistant beta-lactamase-producing
    isolates, but this does not identify a cefazedone resistance determinant or establish
    universal stability to beta-lactamases. Native resistance fields are empty.
  target_ids:
  - CHEBI:131731
  evidence_ids:
  - primary-antibacterial
  - native
- assessment_id: clinical
  area: scope
  topic: Clinical study versus regulatory assertion
  outcome: supported
  summary: The primary sodium-treatment study supports historical clinical investigation
    only. It is uncontrolled and small; no current regulatory jurisdiction or universal
    treatment recommendation is inferred. Native has no clinical-status claim.
  target_ids:
  - CHEBI:131731
  evidence_ids:
  - primary-cap
  - native
- assessment_id: optional-domains
  area: scope
  topic: Adapters, natural production and causal graphs
  outcome: not_applicable
  summary: Native has no named protein/gene/pathway, natural producer, dataset or
    graph claim. Synthetic patent processes do not establish natural production.
  target_ids:
  - CHEBI:131731
  evidence_ids:
  - native
  - patent-main
  - search
- assessment_id: provenance
  area: provenance
  topic: Source ownership and seeded history
  outcome: supported
  summary: Both source concepts and four seed events are coherent. The actual ARO
    owner was captured before judgment; SEEDED remains unchanged.
  target_ids:
  - CHEBI:131731
  evidence_ids:
  - owners
  - native
  - chemistry
- assessment_id: completeness
  area: completeness
  topic: Bounded enrichment opportunities
  outcome: supported
  summary: Primary abstracts and the full sodium study provide optional activity leads,
    with clear form and protocol limits. Empty optional fields alone do not create
    a defect.
  target_ids:
  - CHEBI:131731
  evidence_ids:
  - primary-antibacterial
  - primary-cap
- assessment_id: schema
  area: schema
  topic: Focused gates
  outcome: supported
  summary: Schema, strict and independent structure/mint checks pass; source review
    provides the separate scientific assessment.
  target_ids:
  - CHEBI:131731
  evidence_ids:
  - gates
  - chemistry
findings: []
actions:
- action_id: A1
  description: Optionally curate primary antibacterial observations after exact assay/material
    resolution.
  finding_ids: []
  target_ids:
  - CHEBI:131731
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefazedone.yaml
    role: Curator-owned activity_spectrum and evidence via validated writer
  acceptance_checks:
  - Retrieve the original methods/tables for selected 1979 susceptibility or bactericidal
    papers before adopting individual MICs or MBCs; retain exact strains, material
    form, medium and inoculum.
  - Keep sodium-form CAP treatment, model PK/PD exposure and in-vitro broth susceptibility
    as separate observations. Do not silently equate tested sodium/formulation material
    with the exact neutral acid.
  - Do not infer contemporary clinical breakpoints or a species-wide activity spectrum
    from selected susceptible isolates or abstract-level panel ranges.
  - Keep gentamicin/etimicin combination experiments separate from cefazedone monotherapy.
  - Run native schema, strict, evidence/term/reference/history and applicable corpus
    gates after separately authorized curation.
- action_id: A2
  description: Optionally corroborate Reaxys and direct mechanism evidence.
  finding_ids: []
  target_ids:
  - CHEBI:131731
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Source-owned exact registry mapping
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefazedone.yaml
    role: Curator-owned molecular mechanism evidence
  acceptance_checks:
  - Confirm Reaxys 5399221 against the complete neutral stereochemical graph when
    permissible registry detail is available; do not delete it based only on access
    limits.
  - Locate compound-specific PBP or peptidoglycan experiments before adding primary-evidenced
    mode/target/graph claims; ARO or KEGG annotations alone do not provide experimental
    assay context.
limitations:
- Reaxys 5399221 was corroborated as a live ChEBI mapping but its registry contents
  were not independently inspected.
- All ten unique adopted PMID metadata/abstract records were read; complete primary
  text was inspected for PMID 25947397, not every older susceptibility, tissue-penetration
  or animal-infection paper.
- The complete PK/PD study uses cefazedone sodium treatment and selected susceptible
  isolates. Its detailed AST reagent form and broth protocol are insufficient for
  unqualified exact-neutral-acid quantitative transfer.
- No cefazedone-specific primary PBP experiment was established in this bounded review;
  database mechanism context remains separate from optional primary annotation.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Initial capture preserved and actual ARO inventory added before assessment. All
  expanded source hashes unchanged; no native/source/status/history edits.
- Schema/strict used batch 022; chemistry used locked batch 019 RDKit 2026.03.5 against
  batch 022 cwd.
- All five native patent identifiers resolve as relevant chemical/process documents;
  their broad derivative and salt scope is not an exact structural equivalence assertion.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:131731
- https://pubmed.ncbi.nlm.nih.gov/114187/
- https://doi.org/10.4103/0366-6999.156086
tags:
- cefazedone
- exact-identity
- primary-antibacterial
- salt-material-scope
```
