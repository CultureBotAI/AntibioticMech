# Fleroxacin: coherent chemistry and qualified gyrase assertions with two nomenclature corrections

- Review: 20261021T162958Z-fleroxacin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T16:12:21Z
- Finished UTC: 2026-10-21T16:29:58Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The neutral fleroxacin graph and checked exact chemical xrefs agree. Original enzyme and susceptibility results support the bacterial topoisomerase mode while leaving isolated-subunit direct-binding claims at database evidence level. Two product names are incorrectly typed as exact chemical synonyms, and one systematic synonym has a trailing hyphen.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 445; original thirteen input hashes preserved within twenty-two expanded inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:31810 | data/antibiotics/antibacterial/fleroxacin.yaml | generated | fleroxacin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:31810 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:31810 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:31810 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:31810 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:31810 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:31810 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:31810 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:31810 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:31810 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:31810 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:31810 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:31810 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Neutral achiral fleroxacin

identity: supported. Targets: CHEBI:31810.

Native graph, chemical name, formula, neutral charge and masses are coherent and agree with checked exact structure authorities. The patent hydrochloride is a separately qualified preparation.

### Chemical names versus product names

identity: concern. Targets: CHEBI:31810.

Megalocin and Quinodis are documented commercial product names, yet typed as exact chemical synonyms. The second systematic synonym also retains a stray terminal hyphen. These are bounded nomenclature problems, not a wrong molecular graph.

### Exact chemical links and broader drug associations

grounding: supported. Targets: CHEBI:31810.

PubChem, ChEMBL and KEGG compound structures match. DrugCentral/KEGG drug associations resolve; DrugBank, Reaxys and LINCS remain explicitly limited by access or incomplete snapshot coverage. No wrong-link claim is made from failed access.

### Source-derived topoisomerase mode and imported targets

evidence: supported. Targets: CHEBI:31810.

ChEBI inhibitor roles and original bacterial enzyme experiments support nucleic-acid synthesis inhibition and microbial gyrase/topoisomerase IV scope. Human tendon effects do not change the identity of these microbial enzymes. Both ARO subunit targets remain qualified database assertions; isolated-subunit binding is not promoted from complex inhibition.

### Antibacterial eligibility and spectrum

evidence: supported. Targets: CHEBI:31810.

The original antibacterial abstract and S. aureus enzyme/MIC paper support the named drug as an antibacterial. Spectrum and target preference depend on organism and assay; copper-complex, antibody and host-healing studies do not substitute for free-drug antibacterial results.

### Optional primary enrichment

completeness: unknown. Targets: CHEBI:31810.

The record lacks quantitative activity, resistance and causal collections. Available original strain/enzyme results offer future enrichment but require material and endpoint resolution; missing optional fields are not a native defect.

### Producer and clinical assertions

scope: not_applicable. Targets: CHEBI:31810.

No natural producer or clinical product assertion is present. Historical product evidence is used only to classify the two names.

### Five history events and source ownership

provenance: supported. Targets: CHEBI:31810.

All history events, raw rows and target source claims were read; actual ARO owners were appended before judgment and original hashes preserved.

### Focused native checks

schema: supported. Targets: CHEBI:31810.

All focused checks pass. The synonym semantics require source inspection beyond deterministic validation.

## Findings

### F1: Megalocin and Quinodis product names are typed as exact chemical synonyms

minor / open / confirmed; issue key: fleroxacin-megalocin-quinodis-brand-synonym-typing.

Kyorin identifies Fleroxacin (Megalocin) as its developed product; the Italian official authorization and original clinical methods identify Quinodis as a fleroxacin medicinal product. Reclassify these two names as BRAND_NAME through maintained ARO-derived synonym handling, preserving searchability and source attribution.

### F2: A systematic synonym has a stray terminal hyphen

minor / open / confirmed; issue key: fleroxacin-systematic-synonym-trailing-hyphen.

The second systematic chemical name ends in carboxylic acid- in both the adopted ChEBI row and native synonym. Remove the terminal punctuation artifact after source-owned correction; it does not denote the neutral molecule more accurately and is inconsistent with the complete acid name.

## Recommended Actions And Acceptance Checks

### A1

Correct the two documented product-name synonym types through maintained source handling.

- Megalocin and Quinodis remain searchable but have BRAND_NAME type with accurate source provenance.
- Do not infer present marketing status or convert product formulations into separate exact chemical synonyms.
- Regenerate and run synonym, schema/strict and corpus checks.

### A2

Remove the terminal hyphen from the source-derived systematic synonym.

- The corrected name ends in carboxylic acid and preserves all genuine locants and internal hyphens.
- Retain the neutral chemical graph unchanged and regenerate reproducibly.
- Run schema/strict and source-consistency checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/fleroxacin.yaml; Entire native record, both target entries and all five seed/reseed events | supports | The neutral achiral record asserts fluoroquinolone class, antibacterial roles, source-derived nucleic-acid synthesis inhibition and two explicitly database-level gyrase-subunit targets. Megalocin and Quinodis are EXACT_SYNONYM; synonym 1 ends in acid-. No curated primary target, quantitative activity, resistance or clinical product assertion is present. |
| owners | 445447-raw-rows.json; 445-inputs-expanded.json; Complete ChEBI row 662, ARO row 310 and target rows 249–250 | supports | Original hashes were verified before assessment; ARO raw identity and target owners were appended before detailed judgment. The ARO row supplies the two untyped product aliases, while ChEBI supplies the terminal-hyphen name. No exact override was identified in the searched inputs. |
| local-search | 445447-all-local-paths.txt; Ignored-inclusive label and reference search | context_only | The search included hidden and ignored files under data, curation, conf, scripts, src, reports and reviews. Exact owners and native claims were read; optional collection absence is not treated as a defect. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/31810/; Current CHEBI:31810 structure, names, parents and mechanism roles | supports | Current ChEBI reproduces the native neutral achiral C17H18F3N3O3 graph, key XBJBPGROQZJDOJ-UHFFFAOYSA-N, quinolone/piperazine/acid parents and DNA gyrase/topoisomerase IV inhibitor roles. The malformed terminal hyphen remains in the supplied synonym. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/3357/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON; PubChem CID 3357 molecular properties | supports | PubChem gives the same complete neutral graph and formula as the native record. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL6273.json; CHEMBL6273 molecular structure | supports | ChEMBL independently reproduces the native key and achiral graph. |
| kegg-compound | https://rest.kegg.jp/get/C13179; KEGG compound C13179 and associated molfile | supports | This exact compound entry resolves to fleroxacin; its molfile independently reproduces the native graph. |
| chemistry | 445-chemistry.json; 445447-xref-chemistry.json; Independent RDKit2026.03.5 through batch019 interpreter against batch045 cwd | supports | Native SMILES/InChI, formula, charge, masses and source mints agree. ChEBI, PubChem, ChEMBL and KEGG compound structures match. Broader KEGG drug, DrugCentral and supplemental GSRS structures also match, without changing their namespace semantics. |
| aro | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3004013; ARO3004013 identity and adopted definition | supports | The ARO accession resolves to fleroxacin and supplies the adopted antibacterial lead PMID2112571. Its general gyrase description is database evidence, not an exact purified-subunit experiment. |
| gyrA | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3000733; ARO3000733 gyrA target | supports | The source asserts fluoroquinolone-sensitive gyrase subunit A. The native entry accurately retains PRIMARY_EVIDENCE_NEEDED and unspecified organism/assay. |
| gyrB | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3003261; ARO3003261 gyrB target | supports | The source asserts the fluoroquinolone-sensitive beta subunit. No exact fleroxacin isolated-GyrB binding assay is supplied by this ontology statement; the native database qualifier is preserved. |
| kegg-drug | https://rest.kegg.jp/get/D01716; KEGG drug D01716 | supports | The accession resolves to fleroxacin. It is a drug-level association, not an exact equivalence requirement; the independently parsed molfile nevertheless matches. |
| drugcentral | https://drugcentral.org/drugcard/1177; DrugCentral 1177 drug card and molfile | supports | The card resolves to fleroxacin and its molfile matches the neutral structure. Displayed drug-use metadata is not imported as a new native clinical assertion. |
| drugbank-access | https://go.drugbank.com/drugs/DB04576; DrugBank DB04576 public request | unknown | The request returned 403. The exact drug-level page was not independently read; other source links do not substitute for that access limitation. |
| kyorin | https://www.kyorin-pharm.co.jp/docs/en/ir/pdf/ar/AR2023EN.pdf; Manufacturer Integrated Report 2023, printed page 4 historical product narrative | refutes | Kyorin explicitly pairs Fleroxacin with Megalocin and describes development and product launches. This supports the product-name interpretation, not a current marketing-status claim. |
| kyorin-history | https://www.kyorin-pharm.co.jp/en/company/history.shtml; Manufacturer product-history entry for 1993 | refutes | The company identifies Megalocin (FLRX) as a launched quinolone product, corroborating the original manufacturer report. |
| quinodis | https://www.gazzettaufficiale.it/atto/vediMenuHTML?atto.codiceRedazionale=097A2772&amp;atto.dataPubblicazioneGazzetta=1997-04-09&amp;tipoSerie=serie_generale&amp;tipoVigenza=originario; Italian official authorization decree dated 14 March 1997, published 9 April 1997 | refutes | The official notice names QUINODIS as a Roche medicinal specialty containing fleroxacin in tablet and infusion products. This is direct product-name evidence; it does not assert current availability. |
| quinodis-primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC2014894/?pdf=render; Original clinical pharmacokinetic study, Study protocol paragraph | context_only | The authors explicitly identify the administered commercial product as Quinodis, Roche. This corroborates brand typing; product pharmacokinetics are not pure-compound target evidence. |
| mesh | https://meshb.nlm.nih.gov/record/ui?ui=D016576; NLM MeSH D016576, Quinodis entry term | supports | The descriptor resolves the drug and labels Quinodis with trade-name lexical tag TRD. The vocabulary is used for name semantics, not as original enzyme evidence. |
| enzyme2001 | https://pmc.ncbi.nlm.nih.gov/articles/PMC90866/?pdf=render; PMID11709337 / DOI10.1128/AAC.45.12.3544-3547.2001; original Methods, complete Table 1 and relevant Results/Discussion | partial | This original tests fleroxacin among fifteen quinolones against S. aureus MS5935 and its grlA S80F/gyrA S84L derivatives, alongside reconstituted gyrase and topoisomerase IV. Fleroxacin MICs are 0.5, 4 and 0.5 µg/mL, respectively; enzyme IC50 values are 82.6 and 31.6 µg/mL for gyrase and topoisomerase IV. The paper supports inhibition of both enzyme complexes and a relative topoisomerase IV preference in this organism. It does not measure direct binding to isolated GyrA or GyrB. Drugs were synthesized at Kyorin or purchased from Sigma without compound-specific salt/purity documentation in the inspected methods; quantitative import is deferred. |
| patent | https://patents.google.com/patent/US4398029/en; US4398029A; Example 5, formula/elemental analysis, activity-table method and claim 2 | partial | The patent is relevant to fleroxacin and related quinolones. Example 5 isolates the exact fleroxacin hydrochloride and gives C17H18F3N3O3·HCl analytical composition; claim 2 also encompasses the acid, hydrates and salts. This document reference does not require that every tested preparation equal the neutral native graph. Broad analog activities and the hydrochloride material are not copied as neutral-compound MICs. |
| lead-25143490 | https://pubmed.ncbi.nlm.nih.gov/25143490/; Complete original abstract in 445-core.json | context_only | Original rat rotator-cuff study; complete abstract read. Fleroxacin exposure affected healing endpoints. These host effects are not antibacterial target evidence. |
| lead-26963935 | https://pubmed.ncbi.nlm.nih.gov/26963935/; Complete original abstract in 445-core.json | context_only | Original anti-ofloxacin antibody/Fab study; complete abstract read. The antibody target and 14-analogue recognition experiment concern analytical specificity, not bacterial gyrase. Exact fleroxacin analogue results are not established at abstract depth. |
| lead-27301999 | https://pubmed.ncbi.nlm.nih.gov/27301999/; Complete original abstract in 445-core.json | context_only | Original mixed-ligand copper(II)-fleroxacin/phenanthroline complex study; complete abstract read. Crystal structure, DNA cleavage and albumin binding concern the coordination complex, not neutral fleroxacin alone. |
| lead-3095363 | https://pubmed.ncbi.nlm.nih.gov/3095363/; Complete original abstract in 445-core.json | context_only | Original analytical pharmacokinetic method study; complete abstract read. The exact AM-833 chemical name agrees with fleroxacin; animal metabolites and their excretion are not new antibacterial mechanisms. |
| lead-2112571 | https://pubmed.ncbi.nlm.nih.gov/2112571/; Complete original abstract in 445-core.json | context_only | Original in vitro antibacterial study; complete abstract read. The named RO23-6240 preparation is active against several tested bacterial groups, with resistant exceptions among mycobacteria. The abstract does not establish an exact isolated salt, universal spectrum or purified target-binding assay. |
| lincs-access | https://lincs.hms.harvard.edu/db/sm/6633/; Exact HMS LINCS LSM-6633 public page | unknown | The direct page returned 500. The official 2020 HMS small-molecule SDF snapshot was also searched, with no exact accession/name/key/CAS match among 639 records. This bounded collection is not the entire LINCS namespace; the native link remains unresolved, not disproved. |
| hms-snapshot | https://lincs.hms.harvard.edu/_static/db/prod-20200624/small_molecules.sdf; Official HMS prod-20200624 snapshot;445447-hms-audit.json | context_only | The retained official snapshot contains 639 records. Exact fleroxacin/LSM-6633/key/CAS searches yielded no match in this snapshot only. |
| reaxys-access | https://www.reaxys.com/#/search/quick?context=R&amp;query=RX.RN%3D4300996; Exact Reaxys 4300996 public route | unknown | The request returned 403; exact registry-graph equivalence was not independently verified. |
| adapter | iModulonDB; 445447-adapter-results.json;445447-adapter-search-results.json | context_only | Before protein web follow-up, the catalog and E. coli/precise1k gyrA/gyrB searches succeeded. They identify b2231 and b3699 with no iModulon hit. This is gene context, not a fleroxacin assay or proof of native target taxon; S. aureus conclusions come from the inspected original. |
| gates | 445-focused-results.json; Actual focused checks | supports | Independent chemistry, schema and strict validation all exit 0 on the untouched record. |

## Limits And Additional Notes

- All five adopted PMID leads were read at complete original abstract depth. The 2001 enzyme paper was inspected for original methods, full Table 1 and relevant results/discussion; raw gels were not reanalyzed.
- The adopted copper coordination-complex, antibody and rat tendon studies were not treated as direct free-fleroxacin antibacterial mechanisms. Exact analogue/reagent details beyond the abstracts remain unresolved.
- Original patent Example 5 explicitly uses hydrochloride. Its relevant synthesis/analysis, assay-method description and claims were inspected; every analog table entry and structural image was not independently audited.
- The official manufacturer report and Italian authorization establish historical product names only. No current marketing or treatment recommendation is made.
- DrugBank and Reaxys returned 403; LINCS returned 500. The official HMS snapshot has no exact match within 639 records, which is not evidence of absence from the whole namespace.
- An authoritative CAS registry graph was not separately obtained. Wikipedia was resolved only as a document link; current chemical authorities and the exact primary systematic name support the molecular identity.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Native and maintained files were not edited; all original hashes and expanded inputs were rechecked. Optional links, tags and notes were checked specifically for fleroxacin.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T162958Z-fleroxacin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Fleroxacin: coherent chemistry and qualified gyrase assertions with two nomenclature
  corrections'
started_at: '2026-10-21T16:12:21Z'
finished_at: '2026-10-21T16:29:58Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
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
summary: The neutral fleroxacin graph and checked exact chemical xrefs agree. Original
  enzyme and susceptibility results support the bacterial topoisomerase mode while
  leaving isolated-subunit direct-binding claims at database evidence level. Two product
  names are incorrectly typed as exact chemical synonyms, and one systematic synonym
  has a trailing hyphen.
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
  - path: data/antibiotics/antibacterial/fleroxacin.yaml
    sha256: c92d8c042d12053cec9cbedffd39b5f0a7ac3c3cde7e954219952e4fb4a8cede
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
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: context
targets:
- target_id: CHEBI:31810
  path: data/antibiotics/antibacterial/fleroxacin.yaml
  label: fleroxacin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI and ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual ARO identity/classification and citation owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Actual imported gyrase target assertions
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 445; original thirteen input hashes preserved within twenty-two
    expanded inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:31810
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:31810
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/445447-focused.py
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:31810
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/fleroxacin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:31810
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/fleroxacin.yaml --out /private/tmp/am-review-session/445-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:31810
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
  - CHEBI:31810
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
  - CHEBI:31810
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
  - CHEBI:31810
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
  - CHEBI:31810
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
  - CHEBI:31810
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
  - CHEBI:31810
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
  - CHEBI:31810
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
  - CHEBI:31810
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/fleroxacin.yaml
  locator: Entire native record, both target entries and all five seed/reseed events
  accessed_at: '2026-10-21T16:25:32Z'
  support: supports
  summary: The neutral achiral record asserts fluoroquinolone class, antibacterial
    roles, source-derived nucleic-acid synthesis inhibition and two explicitly database-level
    gyrase-subunit targets. Megalocin and Quinodis are EXACT_SYNONYM; synonym 1 ends
    in acid-. No curated primary target, quantitative activity, resistance or clinical
    product assertion is present.
- evidence_id: owners
  kind: record_content
  reference: 445447-raw-rows.json; 445-inputs-expanded.json
  locator: Complete ChEBI row 662, ARO row 310 and target rows 249–250
  accessed_at: '2026-10-21T16:25:32Z'
  support: supports
  summary: Original hashes were verified before assessment; ARO raw identity and target
    owners were appended before detailed judgment. The ARO row supplies the two untyped
    product aliases, while ChEBI supplies the terminal-hyphen name. No exact override
    was identified in the searched inputs.
  snapshot_sha256: 13d552de8b6fa684796f189c526ffb34c820d1ee4f8a85ef72edd4e4a9344a4f
- evidence_id: local-search
  kind: search
  reference: 445447-all-local-paths.txt
  locator: Ignored-inclusive label and reference search
  accessed_at: '2026-10-21T16:25:32Z'
  support: context_only
  summary: The search included hidden and ignored files under data, curation, conf,
    scripts, src, reports and reviews. Exact owners and native claims were read; optional
    collection absence is not treated as a defect.
  search_scope: rg --no-ignore --hidden -il 'fleroxacin|flomoxef|florfenicol' data
    curation conf scripts src reports reviews
  snapshot_sha256: 02ab6bf102133423d462e55ab1f710d651b6d6e91b6faf9eec666d468a4a4617
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/31810/
  locator: Current CHEBI:31810 structure, names, parents and mechanism roles
  accessed_at: '2026-10-21T16:22:18.028044Z'
  support: supports
  summary: Current ChEBI reproduces the native neutral achiral C17H18F3N3O3 graph,
    key XBJBPGROQZJDOJ-UHFFFAOYSA-N, quinolone/piperazine/acid parents and DNA gyrase/topoisomerase
    IV inhibitor roles. The malformed terminal hyphen remains in the supplied synonym.
  snapshot_sha256: 2429b47da168f6bc54e9d204a5a4038bbe978382d3083d5a9c57be33c6b19ea8
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/3357/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON
  locator: PubChem CID 3357 molecular properties
  accessed_at: '2026-10-21T16:22:18.032896Z'
  support: supports
  summary: PubChem gives the same complete neutral graph and formula as the native
    record.
  snapshot_sha256: 2d5565ea9cee32f27696eef5a0c5366a32380d266395e1f44d1094069a55dbbe
- evidence_id: chembl
  kind: authority
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL6273.json
  locator: CHEMBL6273 molecular structure
  accessed_at: '2026-10-21T16:22:18.035246Z'
  support: supports
  summary: ChEMBL independently reproduces the native key and achiral graph.
  snapshot_sha256: 33bd78c27ed7a8d5e86a85e1406d2d6bc723d1447bb99bea1badc9e74b395a69
- evidence_id: kegg-compound
  kind: authority
  reference: https://rest.kegg.jp/get/C13179
  locator: KEGG compound C13179 and associated molfile
  accessed_at: '2026-10-21T16:22:23.384262Z'
  support: supports
  summary: This exact compound entry resolves to fleroxacin; its molfile independently
    reproduces the native graph.
  snapshot_sha256: b5f550fb3ea8ed3548714960ec9502cf53cf2793b1c0f4f8abdf731b4e4bf35d
- evidence_id: chemistry
  kind: record_content
  reference: 445-chemistry.json; 445447-xref-chemistry.json
  locator: Independent RDKit2026.03.5 through batch019 interpreter against batch045
    cwd
  accessed_at: '2026-10-21T16:25:32Z'
  support: supports
  summary: Native SMILES/InChI, formula, charge, masses and source mints agree. ChEBI,
    PubChem, ChEMBL and KEGG compound structures match. Broader KEGG drug, DrugCentral
    and supplemental GSRS structures also match, without changing their namespace
    semantics.
  snapshot_sha256: c329fdfb10a094a53e4f98112fdcfdecd282f524607708e5eb553c0f64c3f1ad
- evidence_id: aro
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3004013
  locator: ARO3004013 identity and adopted definition
  accessed_at: '2026-10-21T16:22:20.259963Z'
  support: supports
  summary: The ARO accession resolves to fleroxacin and supplies the adopted antibacterial
    lead PMID2112571. Its general gyrase description is database evidence, not an
    exact purified-subunit experiment.
  snapshot_sha256: 1a84411dd6b59455786af5d265c85d2d1e8f8bcd5379e8636a00a7673f4d3088
- evidence_id: gyrA
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3000733
  locator: ARO3000733 gyrA target
  accessed_at: '2026-10-21T16:22:20.268727Z'
  support: supports
  summary: The source asserts fluoroquinolone-sensitive gyrase subunit A. The native
    entry accurately retains PRIMARY_EVIDENCE_NEEDED and unspecified organism/assay.
  snapshot_sha256: f798d605e22cedfe4f22d4e036ab5aeec7a5756296996e45631c1a36f79633af
- evidence_id: gyrB
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3003261
  locator: ARO3003261 gyrB target
  accessed_at: '2026-10-21T16:22:20.456436Z'
  support: supports
  summary: The source asserts the fluoroquinolone-sensitive beta subunit. No exact
    fleroxacin isolated-GyrB binding assay is supplied by this ontology statement;
    the native database qualifier is preserved.
  snapshot_sha256: 81c9119a7f275e45e4ecdd759de1a4707d736ce6163701a9f6d7da3f9762e66a
- evidence_id: kegg-drug
  kind: authority
  reference: https://rest.kegg.jp/get/D01716
  locator: KEGG drug D01716
  accessed_at: '2026-10-21T16:22:18.038409Z'
  support: supports
  summary: The accession resolves to fleroxacin. It is a drug-level association, not
    an exact equivalence requirement; the independently parsed molfile nevertheless
    matches.
  snapshot_sha256: f58503a13e599dee81d182d1d3e7b7874d5d7ad5cf26e9e4297b22458ab30db4
- evidence_id: drugcentral
  kind: authority
  reference: https://drugcentral.org/drugcard/1177
  locator: DrugCentral 1177 drug card and molfile
  accessed_at: '2026-10-21T16:22:22.808616Z'
  support: supports
  summary: The card resolves to fleroxacin and its molfile matches the neutral structure.
    Displayed drug-use metadata is not imported as a new native clinical assertion.
  snapshot_sha256: a1598d0ae46ab90590147017ede15cc39bb1cb0f30a368a66fe2a74cbb8defa9
- evidence_id: drugbank-access
  kind: search
  reference: https://go.drugbank.com/drugs/DB04576
  locator: DrugBank DB04576 public request
  accessed_at: '2026-10-21T16:22:23.079373Z'
  support: unknown
  summary: The request returned 403. The exact drug-level page was not independently
    read; other source links do not substitute for that access limitation.
  snapshot_sha256: a89a016014b8228277c2d06edd0128a3226ee122d50f2f3715fe79afa0c03125
  search_scope: Exact native DrugBank accession through the public page.
- evidence_id: kyorin
  kind: authority
  reference: https://www.kyorin-pharm.co.jp/docs/en/ir/pdf/ar/AR2023EN.pdf
  locator: Manufacturer Integrated Report 2023, printed page 4 historical product
    narrative
  accessed_at: '2026-10-21T16:23:09.117270Z'
  support: refutes
  summary: Kyorin explicitly pairs Fleroxacin with Megalocin and describes development
    and product launches. This supports the product-name interpretation, not a current
    marketing-status claim.
  snapshot_sha256: d3fb5bed80d91d39294e382161d47f0b5f237299d36ea4403ab93119e6eb8656
- evidence_id: kyorin-history
  kind: authority
  reference: https://www.kyorin-pharm.co.jp/en/company/history.shtml
  locator: Manufacturer product-history entry for 1993
  accessed_at: '2026-10-21T16:23:09.115661Z'
  support: refutes
  summary: The company identifies Megalocin (FLRX) as a launched quinolone product,
    corroborating the original manufacturer report.
  snapshot_sha256: ca69b941cf3f9772ff59537733439918aea046d2f84e731d37695423c97e6afd
- evidence_id: quinodis
  kind: authority
  reference: https://www.gazzettaufficiale.it/atto/vediMenuHTML?atto.codiceRedazionale=097A2772&atto.dataPubblicazioneGazzetta=1997-04-09&tipoSerie=serie_generale&tipoVigenza=originario
  locator: Italian official authorization decree dated 14 March 1997, published 9
    April 1997
  accessed_at: '2026-10-21T16:23:09.118945Z'
  support: refutes
  summary: The official notice names QUINODIS as a Roche medicinal specialty containing
    fleroxacin in tablet and infusion products. This is direct product-name evidence;
    it does not assert current availability.
  snapshot_sha256: 153b67c6c865e804bce4d65ab3697045404ea6b9d7d209ac4c693d0a53cfeb98
- evidence_id: quinodis-primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2014894/?pdf=render
  locator: Original clinical pharmacokinetic study, Study protocol paragraph
  accessed_at: '2026-10-21T16:23:09.120788Z'
  support: context_only
  summary: The authors explicitly identify the administered commercial product as
    Quinodis, Roche. This corroborates brand typing; product pharmacokinetics are
    not pure-compound target evidence.
  snapshot_sha256: 16589f95bcc26b661d14c9b23a7c00806d84f75ebe5a228c20bb7848a7103602
- evidence_id: mesh
  kind: authority
  reference: https://meshb.nlm.nih.gov/record/ui?ui=D016576
  locator: NLM MeSH D016576, Quinodis entry term
  accessed_at: '2026-10-21T16:23:38.711568Z'
  support: supports
  summary: The descriptor resolves the drug and labels Quinodis with trade-name lexical
    tag TRD. The vocabulary is used for name semantics, not as original enzyme evidence.
  snapshot_sha256: 087a0f4376f336de885a1c92d4c3fe91ea40e67f8b9bd6b94665485b5f35c760
- evidence_id: enzyme2001
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC90866/?pdf=render
  locator: PMID11709337 / DOI10.1128/AAC.45.12.3544-3547.2001; original Methods, complete
    Table 1 and relevant Results/Discussion
  accessed_at: '2026-10-21T16:23:38.709326Z'
  support: partial
  summary: This original tests fleroxacin among fifteen quinolones against S. aureus
    MS5935 and its grlA S80F/gyrA S84L derivatives, alongside reconstituted gyrase
    and topoisomerase IV. Fleroxacin MICs are 0.5, 4 and 0.5 µg/mL, respectively;
    enzyme IC50 values are 82.6 and 31.6 µg/mL for gyrase and topoisomerase IV. The
    paper supports inhibition of both enzyme complexes and a relative topoisomerase
    IV preference in this organism. It does not measure direct binding to isolated
    GyrA or GyrB. Drugs were synthesized at Kyorin or purchased from Sigma without
    compound-specific salt/purity documentation in the inspected methods; quantitative
    import is deferred.
  snapshot_sha256: 8b85e50ee163c3e4165367d8262cedcb62ce46d45b3f0fd3439b459cf2272fe6
- evidence_id: patent
  kind: primary_source
  reference: https://patents.google.com/patent/US4398029/en
  locator: US4398029A; Example 5, formula/elemental analysis, activity-table method
    and claim 2
  accessed_at: '2026-10-21T16:22:19.949719Z'
  support: partial
  summary: The patent is relevant to fleroxacin and related quinolones. Example 5
    isolates the exact fleroxacin hydrochloride and gives C17H18F3N3O3·HCl analytical
    composition; claim 2 also encompasses the acid, hydrates and salts. This document
    reference does not require that every tested preparation equal the neutral native
    graph. Broad analog activities and the hydrochloride material are not copied as
    neutral-compound MICs.
  snapshot_sha256: 20ee5df96b9542026cb60d180a8474f2353a7f7f9c4133a94b7ad31331225da5
- evidence_id: lead-25143490
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/25143490/
  locator: Complete original abstract in 445-core.json
  accessed_at: '2026-10-21T16:22:18.024123Z'
  support: context_only
  summary: Original rat rotator-cuff study; complete abstract read. Fleroxacin exposure
    affected healing endpoints. These host effects are not antibacterial target evidence.
  snapshot_sha256: 46fa19a4d0799384f5933eb981bcdb5194e479c1c3c40415969149ea68e8b447
- evidence_id: lead-26963935
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/26963935/
  locator: Complete original abstract in 445-core.json
  accessed_at: '2026-10-21T16:22:18.024123Z'
  support: context_only
  summary: Original anti-ofloxacin antibody/Fab study; complete abstract read. The
    antibody target and 14-analogue recognition experiment concern analytical specificity,
    not bacterial gyrase. Exact fleroxacin analogue results are not established at
    abstract depth.
  snapshot_sha256: 46fa19a4d0799384f5933eb981bcdb5194e479c1c3c40415969149ea68e8b447
- evidence_id: lead-27301999
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/27301999/
  locator: Complete original abstract in 445-core.json
  accessed_at: '2026-10-21T16:22:18.024123Z'
  support: context_only
  summary: Original mixed-ligand copper(II)-fleroxacin/phenanthroline complex study;
    complete abstract read. Crystal structure, DNA cleavage and albumin binding concern
    the coordination complex, not neutral fleroxacin alone.
  snapshot_sha256: 46fa19a4d0799384f5933eb981bcdb5194e479c1c3c40415969149ea68e8b447
- evidence_id: lead-3095363
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/3095363/
  locator: Complete original abstract in 445-core.json
  accessed_at: '2026-10-21T16:22:18.024123Z'
  support: context_only
  summary: Original analytical pharmacokinetic method study; complete abstract read.
    The exact AM-833 chemical name agrees with fleroxacin; animal metabolites and
    their excretion are not new antibacterial mechanisms.
  snapshot_sha256: 46fa19a4d0799384f5933eb981bcdb5194e479c1c3c40415969149ea68e8b447
- evidence_id: lead-2112571
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/2112571/
  locator: Complete original abstract in 445-core.json
  accessed_at: '2026-10-21T16:22:18.024123Z'
  support: context_only
  summary: Original in vitro antibacterial study; complete abstract read. The named
    RO23-6240 preparation is active against several tested bacterial groups, with
    resistant exceptions among mycobacteria. The abstract does not establish an exact
    isolated salt, universal spectrum or purified target-binding assay.
  snapshot_sha256: 46fa19a4d0799384f5933eb981bcdb5194e479c1c3c40415969149ea68e8b447
- evidence_id: lincs-access
  kind: search
  reference: https://lincs.hms.harvard.edu/db/sm/6633/
  locator: Exact HMS LINCS LSM-6633 public page
  accessed_at: '2026-10-21T16:22:23.322507Z'
  support: unknown
  summary: The direct page returned 500. The official 2020 HMS small-molecule SDF
    snapshot was also searched, with no exact accession/name/key/CAS match among 639
    records. This bounded collection is not the entire LINCS namespace; the native
    link remains unresolved, not disproved.
  snapshot_sha256: 7f314a5a38afc71f2dab1e127b2dba22c744f5b2f180a8dfcb47514bcd5a8059
  search_scope: Direct LSM-6633 page and official HMS prod-20200624 small_molecules.sdf;
    exact identity terms only.
- evidence_id: hms-snapshot
  kind: database
  reference: https://lincs.hms.harvard.edu/_static/db/prod-20200624/small_molecules.sdf
  locator: Official HMS prod-20200624 snapshot;445447-hms-audit.json
  accessed_at: '2026-10-21T16:23:09.121288Z'
  support: context_only
  summary: The retained official snapshot contains 639 records. Exact fleroxacin/LSM-6633/key/CAS
    searches yielded no match in this snapshot only.
  snapshot_sha256: 07d0f372f351425b90c0d264e4b68e05cb57d8ec75d6c5beba4d77d2a3b3a33e
- evidence_id: reaxys-access
  kind: search
  reference: https://www.reaxys.com/#/search/quick?context=R&query=RX.RN%3D4300996
  locator: Exact Reaxys 4300996 public route
  accessed_at: '2026-10-21T16:22:23.255700Z'
  support: unknown
  summary: The request returned 403; exact registry-graph equivalence was not independently
    verified.
  snapshot_sha256: 7f982c0b8bb7293b32982847389b5a941823112419beb60ac4021c2aef3885f6
  search_scope: Exact native Reaxys accession through public access.
- evidence_id: adapter
  kind: database
  reference: iModulonDB
  locator: 445447-adapter-results.json;445447-adapter-search-results.json
  accessed_at: '2026-10-21T16:25:32Z'
  support: context_only
  summary: Before protein web follow-up, the catalog and E. coli/precise1k gyrA/gyrB
    searches succeeded. They identify b2231 and b3699 with no iModulon hit. This is
    gene context, not a fleroxacin assay or proof of native target taxon; S. aureus
    conclusions come from the inspected original.
  snapshot_sha256: 6cb72373a60d6274d0f36d88e2dd7faed5c00019d0841d1204d1c367d19ecd1a
- evidence_id: gates
  kind: record_content
  reference: 445-focused-results.json
  locator: Actual focused checks
  accessed_at: '2026-10-21T16:25:32Z'
  support: supports
  summary: Independent chemistry, schema and strict validation all exit 0 on the untouched
    record.
  snapshot_sha256: 5fe308cfdf46085ff5e7ac89e3aee9dd95fb2b2b4cb8a57a7b78b5723f9e7f40
assessments:
- assessment_id: identity
  area: identity
  topic: Neutral achiral fleroxacin
  outcome: supported
  summary: Native graph, chemical name, formula, neutral charge and masses are coherent
    and agree with checked exact structure authorities. The patent hydrochloride is
    a separately qualified preparation.
  target_ids:
  - CHEBI:31810
  evidence_ids:
  - native
  - chebi
  - pubchem
  - chembl
  - kegg-compound
  - chemistry
  - patent
- assessment_id: names
  area: identity
  topic: Chemical names versus product names
  outcome: concern
  summary: Megalocin and Quinodis are documented commercial product names, yet typed
    as exact chemical synonyms. The second systematic synonym also retains a stray
    terminal hyphen. These are bounded nomenclature problems, not a wrong molecular
    graph.
  target_ids:
  - CHEBI:31810
  evidence_ids:
  - native
  - owners
  - chebi
  - kyorin
  - kyorin-history
  - quinodis
  - quinodis-primary
  - mesh
- assessment_id: grounding
  area: grounding
  topic: Exact chemical links and broader drug associations
  outcome: supported
  summary: PubChem, ChEMBL and KEGG compound structures match. DrugCentral/KEGG drug
    associations resolve; DrugBank, Reaxys and LINCS remain explicitly limited by
    access or incomplete snapshot coverage. No wrong-link claim is made from failed
    access.
  target_ids:
  - CHEBI:31810
  evidence_ids:
  - pubchem
  - chembl
  - kegg-compound
  - drugcentral
  - kegg-drug
  - drugbank-access
  - reaxys-access
  - lincs-access
  - chemistry
- assessment_id: mechanism
  area: evidence
  topic: Source-derived topoisomerase mode and imported targets
  outcome: supported
  summary: ChEBI inhibitor roles and original bacterial enzyme experiments support
    nucleic-acid synthesis inhibition and microbial gyrase/topoisomerase IV scope.
    Human tendon effects do not change the identity of these microbial enzymes. Both
    ARO subunit targets remain qualified database assertions; isolated-subunit binding
    is not promoted from complex inhibition.
  target_ids:
  - CHEBI:31810
  evidence_ids:
  - chebi
  - gyrA
  - gyrB
  - enzyme2001
  - lead-25143490
  - adapter
- assessment_id: activity
  area: evidence
  topic: Antibacterial eligibility and spectrum
  outcome: supported
  summary: The original antibacterial abstract and S. aureus enzyme/MIC paper support
    the named drug as an antibacterial. Spectrum and target preference depend on organism
    and assay; copper-complex, antibody and host-healing studies do not substitute
    for free-drug antibacterial results.
  target_ids:
  - CHEBI:31810
  evidence_ids:
  - lead-2112571
  - enzyme2001
  - lead-27301999
  - lead-26963935
  - lead-25143490
- assessment_id: completeness
  area: completeness
  topic: Optional primary enrichment
  outcome: unknown
  summary: The record lacks quantitative activity, resistance and causal collections.
    Available original strain/enzyme results offer future enrichment but require material
    and endpoint resolution; missing optional fields are not a native defect.
  target_ids:
  - CHEBI:31810
  evidence_ids:
  - native
  - local-search
  - enzyme2001
- assessment_id: other-domains
  area: scope
  topic: Producer and clinical assertions
  outcome: not_applicable
  summary: No natural producer or clinical product assertion is present. Historical
    product evidence is used only to classify the two names.
  target_ids:
  - CHEBI:31810
  evidence_ids:
  - native
  - quinodis
  - kyorin
- assessment_id: provenance
  area: provenance
  topic: Five history events and source ownership
  outcome: supported
  summary: All history events, raw rows and target source claims were read; actual
    ARO owners were appended before judgment and original hashes preserved.
  target_ids:
  - CHEBI:31810
  evidence_ids:
  - native
  - owners
  - gates
- assessment_id: validation
  area: schema
  topic: Focused native checks
  outcome: supported
  summary: All focused checks pass. The synonym semantics require source inspection
    beyond deterministic validation.
  target_ids:
  - CHEBI:31810
  evidence_ids:
  - gates
  - chemistry
findings:
- finding_id: F1
  issue_key: fleroxacin-megalocin-quinodis-brand-synonym-typing
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: Megalocin and Quinodis product names are typed as exact chemical synonyms
  description: Kyorin identifies Fleroxacin (Megalocin) as its developed product;
    the Italian official authorization and original clinical methods identify Quinodis
    as a fleroxacin medicinal product. Reclassify these two names as BRAND_NAME through
    maintained ARO-derived synonym handling, preserving searchability and source attribution.
  target_ids:
  - CHEBI:31810
  field_paths:
  - synonyms[5].synonym_type
  - synonyms[6].synonym_type
  evidence_ids:
  - native
  - owners
  - kyorin
  - kyorin-history
  - quinodis
  - quinodis-primary
  - mesh
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction and alias handling
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual ARO identity/classification and citation owner
  rule_id: review-checklist:Nomenclature
  native_severity: minor
  normalization_reason: Chemical identity remains coherent; the error is a bounded
    product-versus-chemical name classification.
- finding_id: F2
  issue_key: fleroxacin-systematic-synonym-trailing-hyphen
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: A systematic synonym has a stray terminal hyphen
  description: The second systematic chemical name ends in carboxylic acid- in both
    the adopted ChEBI row and native synonym. Remove the terminal punctuation artifact
    after source-owned correction; it does not denote the neutral molecule more accurately
    and is inconsistent with the complete acid name.
  target_ids:
  - CHEBI:31810
  field_paths:
  - synonyms[1].synonym_text
  evidence_ids:
  - native
  - owners
  - chebi
  - chemistry
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
  rule_id: review-checklist:Nomenclature
  native_severity: minor
  normalization_reason: Non-blocking punctuation defect in an otherwise chemically
    coherent synonym.
actions:
- action_id: A1
  description: Correct the two documented product-name synonym types through maintained
    source handling.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:31810
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction and alias handling
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual ARO identity/classification and citation owner
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Megalocin and Quinodis remain searchable but have BRAND_NAME type with accurate
    source provenance.
  - Do not infer present marketing status or convert product formulations into separate
    exact chemical synonyms.
  - Regenerate and run synonym, schema/strict and corpus checks.
- action_id: A2
  description: Remove the terminal hyphen from the source-derived systematic synonym.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:31810
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
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - The corrected name ends in carboxylic acid and preserves all genuine locants and
    internal hyphens.
  - Retain the neutral chemical graph unchanged and regenerate reproducibly.
  - Run schema/strict and source-consistency checks.
limitations:
- All five adopted PMID leads were read at complete original abstract depth. The 2001
  enzyme paper was inspected for original methods, full Table 1 and relevant results/discussion;
  raw gels were not reanalyzed.
- The adopted copper coordination-complex, antibody and rat tendon studies were not
  treated as direct free-fleroxacin antibacterial mechanisms. Exact analogue/reagent
  details beyond the abstracts remain unresolved.
- Original patent Example 5 explicitly uses hydrochloride. Its relevant synthesis/analysis,
  assay-method description and claims were inspected; every analog table entry and
  structural image was not independently audited.
- The official manufacturer report and Italian authorization establish historical
  product names only. No current marketing or treatment recommendation is made.
- DrugBank and Reaxys returned 403; LINCS returned 500. The official HMS snapshot
  has no exact match within 639 records, which is not evidence of absence from the
  whole namespace.
- An authoritative CAS registry graph was not separately obtained. Wikipedia was resolved
  only as a document link; current chemical authorities and the exact primary systematic
  name support the molecular identity.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Native and maintained files were not edited; all original hashes and expanded inputs
  were rechecked. Optional links, tags and notes were checked specifically for fleroxacin.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://doi.org/10.1128/AAC.45.12.3544-3547.2001
- https://www.kyorin-pharm.co.jp/docs/en/ir/pdf/ar/AR2023EN.pdf
- https://patents.google.com/patent/US4398029A/en
tags:
- fleroxacin
- fluoroquinolone
- brand-synonyms
- gyrase
```
