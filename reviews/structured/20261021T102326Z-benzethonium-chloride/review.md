# Benzethonium chloride: exact salt and antibacterial activity supported; repair numeric document cross-reference

- Review: 20261021T102326Z-benzethonium-chloride
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:53:29Z
- Finished UTC: 2026-10-21T10:23:26Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact benzethonium chloride salt, parent classes, source roles and antibacterial inclusion are supported. One minor document-reference error remains: wikipedia.en:3898548 resolves to a nonexistent title, while the number is independently listed as a Beilstein/Reaxys identifier. One informational follow-up concerns qualified primary activity evidence. Host receptor inhibition, urine-protein assays, grapefruit-product contamination and combination activity must remain distinct from exact antibacterial target claims.

## Scope And Provenance

Whole ChEBI record, including exact chloride salt, all synonyms, chemical/drug/document xrefs, three parents, four activity roles, ten adopted citation leads, source mint and four history events.

Selection: Queue 152; exact CHEBI31264 path from preserved initial capture.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:31264 | data/antibiotics/antibacterial/benzethonium-chloride.yaml | generated | benzethonium chloride |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:31264 | Actual focused command exited 0. |
| strict | passed | True | CHEBI:31264 | Actual focused command exited 0. |
| chemistry | failed | False | CHEBI:31264 | Actual focused command exited 1. The custom diagnostic fails literal formula equality only: native dotted-salt C27H42NO2.Cl and RDKit Hill C27H42ClNO2 encode the same composition. The separate composition-aware diagnostic passes; no structure, charge or mass mismatch is concealed. |
| Independent composition-aware salt diagnostic | passed | False | CHEBI:31264 | Exited 0. Both structures have matching exact key, element counts, +1/-1 fragments, net zero charge and reported masses. The source mint also reproduces in the retained initial diagnostic. |
| Authoritative full QC | failed | True | CHEBI:31264 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:31264 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:31264 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:31264 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:31264 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:31264 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:31264 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:31264 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:31264 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Defined achiral chloride salt

identity: supported. Targets: CHEBI:31264.

Native ChEBI salt, current PubChem and KEGG agree in exact key, composition, counterion and charge. Patent Example 11 corroborates the synthetic scaffold.

### Exact source, parents and class priority

grounding: supported. Targets: CHEBI:31264.

CHEBI31264 is exact. Parents are chemical supersets and antibacterial classification follows explicit source-role priority. Omitted out-of-scope application roles do not constitute errors.

### Chemical, drug and documentary references

provenance: concern. Targets: CHEBI:31264.

CAS and KEGG identifiers agree; patent and named Wikipedia page are relevant documentary references. Numeric Wikipedia 3898548 is a nonresolving/misclassified document link, independently identified as a registry number by a manufacturer.

### Antimicrobial activity and breadth

evidence: supported. Targets: CHEBI:31264.

Source authority attests all imported roles and exact primary studies support antibacterial activity. This bounded pass did not independently verify every fungal/mould/viral class in the broad source definition. Combination effects remain qualified.

### All ten adopted citation dispositions

provenance: supported. Targets: CHEBI:31264.

Seven source abstracts and metadata for three no-abstract letters were inspected. Analytical methods, host toxicity/receptors and synthetic extract contamination remain contextual rather than antibacterial mechanism evidence.

### Optional target and response evidence

completeness: unknown. Targets: CHEBI:31264.

No exact directly measured antibacterial molecular target was established from inspected sources. Membrane discussion, host receptor inhibition and gene-carriage associations do not justify a protein target or causal graph.

### Synthetic substance in commercial plant products

scope: supported. Targets: CHEBI:31264.

No native producer is asserted. Commercial grapefruit extract detection is not biosynthetic proof and cannot justify a plant producer entry.

### Maintained-source and curator ownership

ownership: supported. Targets: CHEBI:31264.

ChEBI row/config/extractor/seeder own the inherited document reference. Optional primary scientific additions belong to the actual record through validated curation and history.

### Focused gates and explicit formula diagnostic

schema: supported. Targets: CHEBI:31264.

Required focused validation passes; the optional literal-formula failure is transparently resolved by composition equality.

## Findings

### F1: Correct the inherited numeric Wikipedia document reference

minor / open / confirmed; issue key: benzethonium-numeric-wikipedia-3898548-misclassified.

wikipedia.en:3898548 expands to a nonresolving article title. Current ChEBI carries the same numeric link, whereas the exact chemical manufacturer identifies 3898548 as a Beilstein/Reaxys number. The valid named Wikipedia reference is already present. This documentary metadata problem does not invalidate the independent chemical identity or experimental antibacterial evidence.

### F2: Add qualified primary activity evidence without transferring mixture or host claims

informational / open / confirmed; issue key: benzethonium-qualified-primary-activity-enrichment.

Optional primary AST and activity evidence could strengthen the source-only record. Relevant studies exist, but panel endpoints, combination results and reporting inconsistencies require explicit qualification. Missing optional target, resistance or producer fields are not themselves errors.

## Recommended Actions And Acceptance Checks

### A1

Normalize the exact documentary xref at its maintained source owner.

- Confirm the source namespace error and suppress or correct only the numeric Wikipedia reference through a maintained source adjudication. Keep the already valid named Wikipedia document link.
- Do not silently recast the number as an exact chemical xref without verifying the registry identity under its own namespace. Manufacturer metadata supports the likely origin, but subscription Reaxys content was not inspected here.
- Regenerate through the documented pipeline during separately authorized curation and confirm correct document/chemical xref separation and resolvability. Run focused strict/reference/history and shared checks.

### A2

Curate exact primary activity with endpoint and experimental scope intact.

- Use PMID 27974958 for explicitly qualified panel MIC observations only after reconciling abstract-versus-table ranges and narrative-versus-table gene counts. Preserve medium, inoculum, exposure duration, units and panel composition; do not turn MIC50/MIC90 into individual-strain MICs or adopt the paper's susceptibility thresholds as universally accepted clinical breakpoints.
- For PMID 30410476 retain separate benzethonium and methyl benzethonium identities. The reported standalone 50 micromolar MIC is data not shown; FICi 0.63 is indifferent under the stated criterion, while ZIP results describe concentration-dependent regions. Do not attribute the two other drug combinations' biofilm reductions to benzethonium.
- Obtain exact purified-compound and organism-specific primary support before adding detailed fungal/viral spectra or a membrane causal graph. PMID 16750419 hand-rub and essential-oil combination effects cannot support benzethonium-alone numerical activity. Host nicotinic receptor inhibition is not an antibacterial target.
- Do not infer grapefruit biosynthesis from commercial extract contamination or resistance causality from gene carriage. If a future exact protein/response claim is proposed, perform the appropriate structured adapter and exact primary target/strain checks before curation.
- Use write_validated_antibiotic and record_curation_event on data/antibiotics/antibacterial/benzethonium-chloride.yaml, preserve additions across reseeding and run native validation. Keep SEEDED until all native review criteria have been met.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/benzethonium-chloride.yaml; Complete YAML including synonyms and four history events. | supports | SEEDED/EXACT ChEBI salt with source-level broad antimicrobial definition and roles. Chemical identity, KEGG drug and documentary links are separated. No molecular target, causal graph, quantitative susceptibility, resistance determinant, producer or dataset is asserted. |
| source | data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Exact row 627; reviewed role filtering, classification priority, structure import, synonyms and xref partition. | supports | The exact row reproduces the native structure, definition, synonyms, roles, parents and ten citation leads. Configured antibacterial priority explains the folder despite concurrent antiviral/antifungal/disinfectant roles. The extractor restricts role imports by configured scope and reviewed edge status; not every current ChEBI application role must appear. The seeder preserves documentary xrefs separately. All 13 original input hashes remain unchanged. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:31264; Official complete page including embedded names, definition, structure, ontology and manual xrefs. | supports | CHEBI31264 is a defined benzethonium chloride salt with full key UREZNYTWGJKWBI-UHFFFAOYSA-M, net zero charge and exact native structure/masses. Parents CHEBI23114, CHEBI35273 and CHEBI35618 mean chloride salt, quaternary ammonium salt and aromatic ether. Imported roles CHEBI22587/33282/35718/48219 are antiviral, antibacterial, antifungal and disinfectant. Synonym types and CAS121-54-0 agree. Brand terms are source annotations, not unique chemical identifiers. |
| chemistry | Independent native parsing and official PubChem CID 8478; 152-chemistry.json; 152-chemistry-composition.json; 152-pubchem.json. | supports | Both native strings parse as the same achiral, two-fragment +1 cation/-1 chloride salt with C27H42ClNO2 composition, average mass 448.091 and monoisotopic mass 447.2904073. Dotted native formula C27H42NO2.Cl is equivalent. Current PubChem CID 8478 independently matches the full key and structure; free-cation CID 2335 is distinct. The original optional failure was only literal formula ordering/notation, and the explicit follow-up passed. |
| kegg | https://rest.kegg.jp/get/C12539; https://rest.kegg.jp/get/D01140; Both complete official entries and atom/bond tables. | supports | C12539 and D01140 identify the same defined chloride salt, formula, CAS121-54-0 and CHEBI31264. D01140 is the drug context, appropriately separated from chemical xrefs. Minor average-mass precision/convention differences do not change the chemical identity. KEGG therapeutic categories are not independently reviewed current clinical efficacy claims. |
| patent | patent:US2115250; https://patents.google.com/patent/US2115250A/en; Original patent PDF, p. 4 Example 11, visually inspected in 152-patent-page4.png; patent title and description. | supports | The 1938 patent Organic nitrogen bases and their salts contains an explicit benzyl-dimethyl quaternary chloride example with the correct tert-octylphenoxyethoxyethyl substituent. Example 11 and its drawing support historical synthetic/surfactant context. This is a relevant documentary link, not a bacterial MIC or target-binding experiment. |
| document-xref | https://en.wikipedia.org/wiki/3898548; https://en.wikipedia.org/wiki/Benzethonium_chloride; https://www.sigmaaldrich.com/GY/en/product/sigma/b8879; Native schema prefix line 79; actual Wikipedia title requests; official manufacturer B8879 identifier section. | refutes | The schema expands wikipedia.en to /wiki/. The numeric title /wiki/3898548 returned HTTP404, while /wiki/Benzethonium_chloride resolved to the named article. Sigma-Aldrich B8879 explicitly lists 3898548 as the Beilstein/REAXYS number alongside the matching CAS, SMILES and full key. Current ChEBI itself carries the numeric Wikipedia link, so this is inherited source misclassification. Independent subscription Reaxys content was not inspected; the proposed remedy does not assume an automatic replacement. |
| adopted-extract | PMID:11453769; DOI:10.1021/JF010222W; PMID:17867553; Complete original abstracts, 152-epmc.json. | context_only | 11453769 identifies synthetic benzethonium chloride in commercial grapefruit seed extracts using HPLC, MS, NMR and elemental analysis. 17867553 compares commercial samples against a benzethonium standard and reports benzethonium with other synthetic additives. These demonstrate chemical content in marketed products, not plant biosynthesis or purified-compound antibacterial mechanisms. The m/z412 signal is the cation, compatible with the chloride salt losing counterion in MS. |
| adopted-handrub | PMID:16750419; DOI:10.1016/J.IJHEH.2006.04.006; Complete original abstract, 152-epmc.json. | partial | This study tests farnesol/essential-oil combinations and an alcohol-based benzethonium-containing hand rub. In vitro bacterial synergy and human-hand or viral log reductions belong to the tested combinations. They cannot be copied as benzethonium-alone potency or universal viral efficacy. |
| adopted-receptor | PMID:11606328; DOI:10.1038/SJ.BJP.0704315; Complete original abstract, PMC1573008 citation metadata. | context_only | Benzethonium inhibits recombinant human alpha7 and alpha4beta2 nicotinic receptors expressed in Xenopus oocytes, studied separately from ketamine and Ketalar. These are host-neuronal pharmacology observations, not bacterial or fungal antimicrobial targets. The oocyte is an expression system, not a natural producer. |
| adopted-toxicity | PMID:12595925; PMID:22828255; DOI:10.1097/DER.0b013e318260d78d; Complete NTP report abstract and sensitization-study abstract. | context_only | The NTP study is dermal animal toxicology and genetic toxicology; Salmonella is an Ames-test organism rather than a bacterial susceptibility panel. The sensitization study concerns human dermatitis patch testing and distinguishes benzalkonium from benzethonium. Neither establishes antimicrobial mode of action or broad-spectrum efficacy. |
| adopted-analytical | PMID:3995765; DOI:10.1093/CLINCHEM/31.6.864; Complete original abstract. | context_only | This paper adapts benzethonium chloride precipitation/absorbance to measurement of body-fluid proteins. It is analytical-method evidence, not antimicrobial target inhibition. |
| adopted-letters | PMID:2310164; DOI:10.1177/000456329002700121; PMID:2735743; DOI:10.1177/000456328902600117; PMID:3416474; DOI:10.1093/CLINCHEM/34.9.1944a; Original bibliographic metadata; no abstracts supplied and attempted DOI routes unavailable. | context_only | These three titles concern interferences/errors in benzethonium urine-protein methods. Bibliographic identities resolve, but full content was not inspected. They remain analytical-context leads and are not used as primary support for antimicrobial conclusions. |
| activity2016 | PMID:27974958; DOI:10.5001/OMJ.2016.86; Complete PMC5099399 main text including Methods, Tables 2–4 and Discussion. | supports | Sigma benzethonium chloride was tested by broth microdilution against 165 clinical staphylococcal isolates in Mueller–Hinton broth at 37 degrees C for 24 hours, with stated final inoculum 5x10^5 CFU/mL. Table 2 gives benzethonium MIC50/MIC90 of 4/16 micrograms/mL for MRSA, 1/2 for MSSA, and 4/16 for CoNS. These are panel endpoints. The abstract swaps ranges relative to Results/Table 2, and some gene counts differ between narrative and tables. Qualitative antibacterial activity is clear; exact quantitative additions need table-based reconciliation. Gene carriage associations are not direct efflux or causal knockout evidence. |
| activity2018 | PMID:30410476; DOI:10.3389/FMICB.2018.02541; Complete PMC6209680 main text including Methods, Tables 2–3 and figure captions. | supports | The Prestwick screen distinguishes benzethonium chloride from methyl benzethonium. It reports standalone benzethonium MIC of 50 micromolar against the laboratory P. aeruginosa strain in dose-response data not shown, and combination FICi 0.63 classified indifferent, despite concentration regions with ZIP synergy. The preformed-biofilm benefits belong to auranofin/colistin and clomiphene/colistin; they must not transfer to benzethonium. Membrane disruption is literature-based discussion, not directly measured here. |
| activity2023 | DOI:10.1016/J.MOLSTRUC.2023.136299; https://www.sciencedirect.com/science/article/abs/pii/S0022286023013893; Complete publisher abstract and author-deposited SSRN4377420 landing page. | partial | The paper combines benzethonium spectroscopy/physical chemistry, antibacterial testing and a proposed structure–activity mechanism. It distinguishes cation, chloride and hydrated computational models. The free SSRN PDF attempt returned 403, so strains, numerical assays and proposed mechanism were not independently checked in full text; no direct target or causal graph is inferred. |
| adapter | iModulonDB structured-source applicability; Whole native field inventory and inspected dataset catalog. | context_only | The native record names no gene, locus, protein, regulator, stress pathway or exposure dataset, so no native claim requires an iModulonDB lookup. The adopted human neuronal receptor study has no matching bacterial dataset. Optional bacterial gene-carriage papers are not promoted to mechanistic native assertions; gene presence and expression-module membership cannot prove causality or exact-compound transport. |
| search | CultureBotAI/AntibioticMech; 152-local-hits.txt; 152-maintained-search.txt; 152-numeric-xref-search.txt. | context_only | Hidden- and ignored-inclusive searches confirmed the single exact target, raw row and source owners, with no separate maintained curator mechanism/AST object found in the searched scope. The numeric document xref is inherited from the exact ChEBI row. Historical reports were leads only; bounded primary searching found clinical-panel and combination studies without importing related-compound conclusions. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; docs/HARMONIZATION.md; docs/CURATION.md; Exact forms, xref scope, primary evidence and quantitative endpoint rules. | supports | Preserve salt identity, drug/document distinctions, primary assay material and combination endpoints. Synthetic chemical contamination does not establish biosynthesis; host receptors are not antibacterial targets. Optional scientific-field absence is not a required representation failure. |
| validation | Focused gates and formula-normalized chemistry; 152-focused-results.json and 152-chemistry-composition.json. | supports | Schema and strict validation exited 0. The initial optional chemistry diagnostic exited 1 only at formula string equality; the composition-aware diagnostic exited 0. All captured input hashes were rechecked unchanged. |

## Limits And Additional Notes

- Initial capture and all 13 source hashes were preserved and rechecked unchanged. The whole native record and exact maintained source row/configuration/code were inspected.
- Seven of ten adopted leads supplied original abstracts, all read. The three older urine-protein letters supplied bibliographic metadata but no abstract; attempted DOI routes did not expose their full text. They are not scientific support for the verdict.
- The two added antibacterial papers were read in complete main text including tables and figure captions. Raw assay data and all original figure images were not independently reanalyzed; source numerical/reporting inconsistencies are preserved for curator follow-up.
- The 2023 spectroscopy/activity article was read at publisher abstract scope. Author-deposited SSRN landing page was accessible, but its PDF returned 403; proposed mechanism and quantitative assay details remain unverified.
- The patent identity/context and Example 11 on p. 4 were inspected, including the original structural image. It was not treated as an antibacterial experiment or exhaustively audited for every claim.
- The native broad bacterial/fungal/mould/viral definition is faithfully source-attested. This bounded review independently inspected antibacterial experiments but did not establish a complete quantitative antifungal/antiviral spectrum or current clinical-use status.
- The numeric Wikipedia title returned 404; the named page resolved. The Wikipedia API route returned 403. Manufacturer data identifies the numeric string as Beilstein/Reaxys, but subscription registry content was not used.
- The initial custom chemistry diagnostic failure is retained; formula composition normalization explains it completely. No native formula, charge or mass edit is recommended.
- No native protein or transcriptomic assertion triggered iModulonDB. No exhaustive resistance, natural-producer or public-dataset inventory is claimed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T102326Z-benzethonium-chloride
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Benzethonium chloride: exact salt and antibacterial activity supported; repair
  numeric document cross-reference'
started_at: '2026-10-21T09:53:29Z'
finished_at: '2026-10-21T10:23:26Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author the record. Preserved the initial capture, read
    the entire target and maintained ChEBI row/configuration/transform, checked official
    chemical sources and each adopted citation, and inspected two original antibacterial
    papers and the referenced patent example.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'The exact benzethonium chloride salt, parent classes, source roles and antibacterial
  inclusion are supported. One minor document-reference error remains: wikipedia.en:3898548
  resolves to a nonexistent title, while the number is independently listed as a Beilstein/Reaxys
  identifier. One informational follow-up concerns qualified primary activity evidence.
  Host receptor inhibition, urine-protein assays, grapefruit-product contamination
  and combination activity must remain distinct from exact antibacterial target claims.'
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
  - path: data/antibiotics/antibacterial/benzethonium-chloride.yaml
    sha256: fa22a5e79dde7e9f25f28473635c0f7418ea1f994696f46414c9d02adac41e87
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
targets:
- target_id: CHEBI:31264
  path: data/antibiotics/antibacterial/benzethonium-chloride.yaml
  label: benzethonium chloride
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
  description: Whole ChEBI record, including exact chloride salt, all synonyms, chemical/drug/document
    xrefs, three parents, four activity roles, ten adopted citation leads, source
    mint and four history events.
  selection: Queue 152; exact CHEBI31264 path from preserved initial capture.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:31264
  exclusions:
  - target: Benzalkonium chloride, methyl benzethonium chloride, free benzethonium
      cation, commercial grapefruit extracts and multidrug hand-rub formulations as
      exact equivalents
    reason: They are distinct compounds or compositions; quantitative and mechanistic
      evidence must remain attached to the tested material.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Actual focused command exited 0.
  target_ids:
  - CHEBI:31264
  evidence_ids:
  - validation
  - chemistry
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/benzethonium-chloride.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Actual focused command exited 0.
  target_ids:
  - CHEBI:31264
  evidence_ids:
  - validation
  - chemistry
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/benzethonium-chloride.yaml --out /private/tmp/am-review-session/152-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: failed
  required: false
  summary: 'Actual focused command exited 1. The custom diagnostic fails literal formula
    equality only: native dotted-salt C27H42NO2.Cl and RDKit Hill C27H42ClNO2 encode
    the same composition. The separate composition-aware diagnostic passes; no structure,
    charge or mass mismatch is concealed.'
  target_ids:
  - CHEBI:31264
  evidence_ids:
  - validation
  - chemistry
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache .venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 152
  exit_code: 1
  expected_exit_code: 0
- check_id: chemistry-composition
  name: Independent composition-aware salt diagnostic
  status: passed
  required: false
  summary: Exited 0. Both structures have matching exact key, element counts, +1/-1
    fragments, net zero charge and reported masses. The source mint also reproduces
    in the retained initial diagnostic.
  target_ids:
  - CHEBI:31264
  evidence_ids:
  - chemistry
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache .venv/bin/python
    /private/tmp/am-review-session/152-chemistry-composition.py
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
  - CHEBI:31264
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
  - CHEBI:31264
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
  - CHEBI:31264
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
  - CHEBI:31264
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
  - CHEBI:31264
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
  - CHEBI:31264
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
  - CHEBI:31264
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
  - CHEBI:31264
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
  - CHEBI:31264
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/benzethonium-chloride.yaml
  locator: Complete YAML including synonyms and four history events.
  accessed_at: '2026-10-21T10:22:39Z'
  support: supports
  summary: SEEDED/EXACT ChEBI salt with source-level broad antimicrobial definition
    and roles. Chemical identity, KEGG drug and documentary links are separated. No
    molecular target, causal graph, quantitative susceptibility, resistance determinant,
    producer or dataset is asserted.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: Exact row 627; reviewed role filtering, classification priority, structure
    import, synonyms and xref partition.
  accessed_at: '2026-10-21T10:22:39Z'
  support: supports
  summary: The exact row reproduces the native structure, definition, synonyms, roles,
    parents and ten citation leads. Configured antibacterial priority explains the
    folder despite concurrent antiviral/antifungal/disinfectant roles. The extractor
    restricts role imports by configured scope and reviewed edge status; not every
    current ChEBI application role must appear. The seeder preserves documentary xrefs
    separately. All 13 original input hashes remain unchanged.
  snapshot_sha256: dcab291d00bc2b90c0aaaa4898e786a6feb20d51ae4ae1cab9c9fbc4ceee9772
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:31264
  locator: Official complete page including embedded names, definition, structure,
    ontology and manual xrefs.
  accessed_at: '2026-10-21T10:22:39Z'
  support: supports
  summary: CHEBI31264 is a defined benzethonium chloride salt with full key UREZNYTWGJKWBI-UHFFFAOYSA-M,
    net zero charge and exact native structure/masses. Parents CHEBI23114, CHEBI35273
    and CHEBI35618 mean chloride salt, quaternary ammonium salt and aromatic ether.
    Imported roles CHEBI22587/33282/35718/48219 are antiviral, antibacterial, antifungal
    and disinfectant. Synonym types and CAS121-54-0 agree. Brand terms are source
    annotations, not unique chemical identifiers.
  snapshot_sha256: 8266fe82af19734810280160b5c41172f0185b18a08c36530e8aca04fa12b632
- evidence_id: chemistry
  kind: validation
  reference: Independent native parsing and official PubChem CID 8478
  locator: 152-chemistry.json; 152-chemistry-composition.json; 152-pubchem.json.
  accessed_at: '2026-10-21T10:22:39Z'
  support: supports
  summary: Both native strings parse as the same achiral, two-fragment +1 cation/-1
    chloride salt with C27H42ClNO2 composition, average mass 448.091 and monoisotopic
    mass 447.2904073. Dotted native formula C27H42NO2.Cl is equivalent. Current PubChem
    CID 8478 independently matches the full key and structure; free-cation CID 2335
    is distinct. The original optional failure was only literal formula ordering/notation,
    and the explicit follow-up passed.
  snapshot_sha256: 9658064110ba7f7675318c7914b6e0c93a9fe6fdf236f7455076ed2e62f79f0c
- evidence_id: kegg
  kind: database
  reference: https://rest.kegg.jp/get/C12539; https://rest.kegg.jp/get/D01140
  locator: Both complete official entries and atom/bond tables.
  accessed_at: '2026-10-21T10:22:39Z'
  support: supports
  summary: C12539 and D01140 identify the same defined chloride salt, formula, CAS121-54-0
    and CHEBI31264. D01140 is the drug context, appropriately separated from chemical
    xrefs. Minor average-mass precision/convention differences do not change the chemical
    identity. KEGG therapeutic categories are not independently reviewed current clinical
    efficacy claims.
  snapshot_sha256: 4b28f0a6ced12b1b2a46416b8b39bcec5bacfaf6650d3aa7fd7bdb065051657b
- evidence_id: patent
  kind: primary_source
  reference: patent:US2115250; https://patents.google.com/patent/US2115250A/en
  locator: Original patent PDF, p. 4 Example 11, visually inspected in 152-patent-page4.png;
    patent title and description.
  accessed_at: '2026-10-21T10:22:39Z'
  support: supports
  summary: The 1938 patent Organic nitrogen bases and their salts contains an explicit
    benzyl-dimethyl quaternary chloride example with the correct tert-octylphenoxyethoxyethyl
    substituent. Example 11 and its drawing support historical synthetic/surfactant
    context. This is a relevant documentary link, not a bacterial MIC or target-binding
    experiment.
  snapshot_sha256: d40c6f2355ab980dd9e084743cf71836747c795400e02b9b256fbc854dc90366
- evidence_id: document-xref
  kind: authority
  reference: https://en.wikipedia.org/wiki/3898548; https://en.wikipedia.org/wiki/Benzethonium_chloride;
    https://www.sigmaaldrich.com/GY/en/product/sigma/b8879
  locator: Native schema prefix line 79; actual Wikipedia title requests; official
    manufacturer B8879 identifier section.
  accessed_at: '2026-10-21T10:22:39Z'
  support: refutes
  summary: The schema expands wikipedia.en to /wiki/. The numeric title /wiki/3898548
    returned HTTP404, while /wiki/Benzethonium_chloride resolved to the named article.
    Sigma-Aldrich B8879 explicitly lists 3898548 as the Beilstein/REAXYS number alongside
    the matching CAS, SMILES and full key. Current ChEBI itself carries the numeric
    Wikipedia link, so this is inherited source misclassification. Independent subscription
    Reaxys content was not inspected; the proposed remedy does not assume an automatic
    replacement.
  snapshot_sha256: 8266fe82af19734810280160b5c41172f0185b18a08c36530e8aca04fa12b632
- evidence_id: adopted-extract
  kind: primary_source
  reference: PMID:11453769; DOI:10.1021/JF010222W; PMID:17867553
  locator: Complete original abstracts, 152-epmc.json.
  accessed_at: '2026-10-21T10:22:39Z'
  support: context_only
  summary: 11453769 identifies synthetic benzethonium chloride in commercial grapefruit
    seed extracts using HPLC, MS, NMR and elemental analysis. 17867553 compares commercial
    samples against a benzethonium standard and reports benzethonium with other synthetic
    additives. These demonstrate chemical content in marketed products, not plant
    biosynthesis or purified-compound antibacterial mechanisms. The m/z412 signal
    is the cation, compatible with the chloride salt losing counterion in MS.
  snapshot_sha256: e67f12588b46d50bec0484b791ffff26b639e282059f55d12f7aba5e3214dbc5
- evidence_id: adopted-handrub
  kind: primary_source
  reference: PMID:16750419; DOI:10.1016/J.IJHEH.2006.04.006
  locator: Complete original abstract, 152-epmc.json.
  accessed_at: '2026-10-21T10:22:39Z'
  support: partial
  summary: This study tests farnesol/essential-oil combinations and an alcohol-based
    benzethonium-containing hand rub. In vitro bacterial synergy and human-hand or
    viral log reductions belong to the tested combinations. They cannot be copied
    as benzethonium-alone potency or universal viral efficacy.
  snapshot_sha256: e67f12588b46d50bec0484b791ffff26b639e282059f55d12f7aba5e3214dbc5
- evidence_id: adopted-receptor
  kind: primary_source
  reference: PMID:11606328; DOI:10.1038/SJ.BJP.0704315
  locator: Complete original abstract, PMC1573008 citation metadata.
  accessed_at: '2026-10-21T10:22:39Z'
  support: context_only
  summary: Benzethonium inhibits recombinant human alpha7 and alpha4beta2 nicotinic
    receptors expressed in Xenopus oocytes, studied separately from ketamine and Ketalar.
    These are host-neuronal pharmacology observations, not bacterial or fungal antimicrobial
    targets. The oocyte is an expression system, not a natural producer.
  snapshot_sha256: e67f12588b46d50bec0484b791ffff26b639e282059f55d12f7aba5e3214dbc5
- evidence_id: adopted-toxicity
  kind: primary_source
  reference: PMID:12595925; PMID:22828255; DOI:10.1097/DER.0b013e318260d78d
  locator: Complete NTP report abstract and sensitization-study abstract.
  accessed_at: '2026-10-21T10:22:39Z'
  support: context_only
  summary: The NTP study is dermal animal toxicology and genetic toxicology; Salmonella
    is an Ames-test organism rather than a bacterial susceptibility panel. The sensitization
    study concerns human dermatitis patch testing and distinguishes benzalkonium from
    benzethonium. Neither establishes antimicrobial mode of action or broad-spectrum
    efficacy.
  snapshot_sha256: e67f12588b46d50bec0484b791ffff26b639e282059f55d12f7aba5e3214dbc5
- evidence_id: adopted-analytical
  kind: primary_source
  reference: PMID:3995765; DOI:10.1093/CLINCHEM/31.6.864
  locator: Complete original abstract.
  accessed_at: '2026-10-21T10:22:39Z'
  support: context_only
  summary: This paper adapts benzethonium chloride precipitation/absorbance to measurement
    of body-fluid proteins. It is analytical-method evidence, not antimicrobial target
    inhibition.
  snapshot_sha256: e67f12588b46d50bec0484b791ffff26b639e282059f55d12f7aba5e3214dbc5
- evidence_id: adopted-letters
  kind: database
  reference: PMID:2310164; DOI:10.1177/000456329002700121; PMID:2735743; DOI:10.1177/000456328902600117;
    PMID:3416474; DOI:10.1093/CLINCHEM/34.9.1944a
  locator: Original bibliographic metadata; no abstracts supplied and attempted DOI
    routes unavailable.
  accessed_at: '2026-10-21T10:22:39Z'
  support: context_only
  summary: These three titles concern interferences/errors in benzethonium urine-protein
    methods. Bibliographic identities resolve, but full content was not inspected.
    They remain analytical-context leads and are not used as primary support for antimicrobial
    conclusions.
  snapshot_sha256: e67f12588b46d50bec0484b791ffff26b639e282059f55d12f7aba5e3214dbc5
- evidence_id: activity2016
  kind: primary_source
  reference: PMID:27974958; DOI:10.5001/OMJ.2016.86
  locator: Complete PMC5099399 main text including Methods, Tables 2–4 and Discussion.
  accessed_at: '2026-10-21T10:22:39Z'
  support: supports
  summary: Sigma benzethonium chloride was tested by broth microdilution against 165
    clinical staphylococcal isolates in Mueller–Hinton broth at 37 degrees C for 24
    hours, with stated final inoculum 5x10^5 CFU/mL. Table 2 gives benzethonium MIC50/MIC90
    of 4/16 micrograms/mL for MRSA, 1/2 for MSSA, and 4/16 for CoNS. These are panel
    endpoints. The abstract swaps ranges relative to Results/Table 2, and some gene
    counts differ between narrative and tables. Qualitative antibacterial activity
    is clear; exact quantitative additions need table-based reconciliation. Gene carriage
    associations are not direct efflux or causal knockout evidence.
  snapshot_sha256: 66f149710d842590b9429bf95a80f53a03d80eaf8df757297cea8ed92497e825
- evidence_id: activity2018
  kind: primary_source
  reference: PMID:30410476; DOI:10.3389/FMICB.2018.02541
  locator: Complete PMC6209680 main text including Methods, Tables 2–3 and figure
    captions.
  accessed_at: '2026-10-21T10:22:39Z'
  support: supports
  summary: The Prestwick screen distinguishes benzethonium chloride from methyl benzethonium.
    It reports standalone benzethonium MIC of 50 micromolar against the laboratory
    P. aeruginosa strain in dose-response data not shown, and combination FICi 0.63
    classified indifferent, despite concentration regions with ZIP synergy. The preformed-biofilm
    benefits belong to auranofin/colistin and clomiphene/colistin; they must not transfer
    to benzethonium. Membrane disruption is literature-based discussion, not directly
    measured here.
  snapshot_sha256: f9564725f99f572c3e6981dbd6997cee83ff3b9a68fe2ad6ef85e7593597c597
- evidence_id: activity2023
  kind: primary_source
  reference: DOI:10.1016/J.MOLSTRUC.2023.136299; https://www.sciencedirect.com/science/article/abs/pii/S0022286023013893
  locator: Complete publisher abstract and author-deposited SSRN4377420 landing page.
  accessed_at: '2026-10-21T10:22:39Z'
  support: partial
  summary: The paper combines benzethonium spectroscopy/physical chemistry, antibacterial
    testing and a proposed structure–activity mechanism. It distinguishes cation,
    chloride and hydrated computational models. The free SSRN PDF attempt returned
    403, so strains, numerical assays and proposed mechanism were not independently
    checked in full text; no direct target or causal graph is inferred.
- evidence_id: adapter
  kind: database
  reference: iModulonDB structured-source applicability
  locator: Whole native field inventory and inspected dataset catalog.
  accessed_at: '2026-10-21T10:22:39Z'
  support: context_only
  summary: The native record names no gene, locus, protein, regulator, stress pathway
    or exposure dataset, so no native claim requires an iModulonDB lookup. The adopted
    human neuronal receptor study has no matching bacterial dataset. Optional bacterial
    gene-carriage papers are not promoted to mechanistic native assertions; gene presence
    and expression-module membership cannot prove causality or exact-compound transport.
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 152-local-hits.txt; 152-maintained-search.txt; 152-numeric-xref-search.txt.
  accessed_at: '2026-10-21T10:22:39Z'
  support: context_only
  summary: Hidden- and ignored-inclusive searches confirmed the single exact target,
    raw row and source owners, with no separate maintained curator mechanism/AST object
    found in the searched scope. The numeric document xref is inherited from the exact
    ChEBI row. Historical reports were leads only; bounded primary searching found
    clinical-panel and combination studies without importing related-compound conclusions.
  snapshot_sha256: 69c2c3dcdc10ce4ce592e2f629af377b2eb0219a1aef32f01175e3bd6cb4fb41
  search_scope: rg --no-ignore --hidden for benzethonium, slug, CHEBI:31264, UREZNYTWGJKWBI
    and numeric 3898548 across batch016 excluding .git/.venv; focused curation/conf/scripts/data/raw/src/reports/reviews.
    Official ChEBI, PubChem, KEGG, patent, PubMed/Europe PMC and publisher original
    papers; exact benzethonium chloride activity/mechanism queries.
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md; docs/HARMONIZATION.md;
    docs/CURATION.md
  locator: Exact forms, xref scope, primary evidence and quantitative endpoint rules.
  accessed_at: '2026-10-21T10:22:39Z'
  support: supports
  summary: Preserve salt identity, drug/document distinctions, primary assay material
    and combination endpoints. Synthetic chemical contamination does not establish
    biosynthesis; host receptors are not antibacterial targets. Optional scientific-field
    absence is not a required representation failure.
- evidence_id: validation
  kind: validation
  reference: Focused gates and formula-normalized chemistry
  locator: 152-focused-results.json and 152-chemistry-composition.json.
  accessed_at: '2026-10-21T10:22:39Z'
  support: supports
  summary: Schema and strict validation exited 0. The initial optional chemistry diagnostic
    exited 1 only at formula string equality; the composition-aware diagnostic exited
    0. All captured input hashes were rechecked unchanged.
  snapshot_sha256: f62133296ad27c6bda4854ed88997cbfbe11862ee5be6455cef410d81d2686bf
assessments:
- assessment_id: identity
  area: identity
  topic: Defined achiral chloride salt
  outcome: supported
  summary: Native ChEBI salt, current PubChem and KEGG agree in exact key, composition,
    counterion and charge. Patent Example 11 corroborates the synthetic scaffold.
  target_ids:
  - CHEBI:31264
  evidence_ids:
  - chebi
  - chemistry
  - kegg
  - patent
- assessment_id: grounding
  area: grounding
  topic: Exact source, parents and class priority
  outcome: supported
  summary: CHEBI31264 is exact. Parents are chemical supersets and antibacterial classification
    follows explicit source-role priority. Omitted out-of-scope application roles
    do not constitute errors.
  target_ids:
  - CHEBI:31264
  evidence_ids:
  - source
  - chebi
  - rubric
- assessment_id: xref
  area: provenance
  topic: Chemical, drug and documentary references
  outcome: concern
  summary: CAS and KEGG identifiers agree; patent and named Wikipedia page are relevant
    documentary references. Numeric Wikipedia 3898548 is a nonresolving/misclassified
    document link, independently identified as a registry number by a manufacturer.
  target_ids:
  - CHEBI:31264
  evidence_ids:
  - chebi
  - kegg
  - patent
  - document-xref
- assessment_id: activity
  area: evidence
  topic: Antimicrobial activity and breadth
  outcome: supported
  summary: Source authority attests all imported roles and exact primary studies support
    antibacterial activity. This bounded pass did not independently verify every fungal/mould/viral
    class in the broad source definition. Combination effects remain qualified.
  target_ids:
  - CHEBI:31264
  evidence_ids:
  - chebi
  - activity2016
  - activity2018
  - activity2023
  - adopted-handrub
- assessment_id: citations
  area: provenance
  topic: All ten adopted citation dispositions
  outcome: supported
  summary: Seven source abstracts and metadata for three no-abstract letters were
    inspected. Analytical methods, host toxicity/receptors and synthetic extract contamination
    remain contextual rather than antibacterial mechanism evidence.
  target_ids:
  - CHEBI:31264
  evidence_ids:
  - adopted-extract
  - adopted-handrub
  - adopted-receptor
  - adopted-toxicity
  - adopted-analytical
  - adopted-letters
- assessment_id: mechanism
  area: completeness
  topic: Optional target and response evidence
  outcome: unknown
  summary: No exact directly measured antibacterial molecular target was established
    from inspected sources. Membrane discussion, host receptor inhibition and gene-carriage
    associations do not justify a protein target or causal graph.
  target_ids:
  - CHEBI:31264
  evidence_ids:
  - activity2018
  - adopted-receptor
  - activity2016
  - adapter
  - rubric
- assessment_id: producer
  area: scope
  topic: Synthetic substance in commercial plant products
  outcome: supported
  summary: No native producer is asserted. Commercial grapefruit extract detection
    is not biosynthetic proof and cannot justify a plant producer entry.
  target_ids:
  - CHEBI:31264
  evidence_ids:
  - record
  - adopted-extract
  - patent
- assessment_id: ownership
  area: ownership
  topic: Maintained-source and curator ownership
  outcome: supported
  summary: ChEBI row/config/extractor/seeder own the inherited document reference.
    Optional primary scientific additions belong to the actual record through validated
    curation and history.
  target_ids:
  - CHEBI:31264
  evidence_ids:
  - source
  - rubric
- assessment_id: schema
  area: schema
  topic: Focused gates and explicit formula diagnostic
  outcome: supported
  summary: Required focused validation passes; the optional literal-formula failure
    is transparently resolved by composition equality.
  target_ids:
  - CHEBI:31264
  evidence_ids:
  - validation
  - chemistry
findings:
- finding_id: F1
  issue_key: benzethonium-numeric-wikipedia-3898548-misclassified
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the inherited numeric Wikipedia document reference
  description: wikipedia.en:3898548 expands to a nonresolving article title. Current
    ChEBI carries the same numeric link, whereas the exact chemical manufacturer identifies
    3898548 as a Beilstein/Reaxys number. The valid named Wikipedia reference is already
    present. This documentary metadata problem does not invalidate the independent
    chemical identity or experimental antibacterial evidence.
  target_ids:
  - CHEBI:31264
  field_paths:
  - document_xrefs[1]
  evidence_ids:
  - source
  - chebi
  - document-xref
  - search
  rule_id: 'native-review-checklist: resolvable and correctly namespaced external
    references'
  native_severity: minor nonessential documentary provenance error
  normalization_reason: The erroneous link is a redundant, nonessential document pointer
    rather than the grounding or a primary evidence reference; chemical identity and
    supporting scientific references remain intact.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Inherited numeric document xref
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained exact source-xref normalization or exclusion policy
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Validate source xref namespaces
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Preserve corrected document-versus-chemical mapping across reseeding
- finding_id: F2
  issue_key: benzethonium-qualified-primary-activity-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Add qualified primary activity evidence without transferring mixture or host
    claims
  description: Optional primary AST and activity evidence could strengthen the source-only
    record. Relevant studies exist, but panel endpoints, combination results and reporting
    inconsistencies require explicit qualification. Missing optional target, resistance
    or producer fields are not themselves errors.
  target_ids:
  - CHEBI:31264
  field_paths:
  - activity_spectrum
  - evidence
  - mode_of_action
  - resistance_mechanisms
  evidence_ids:
  - activity2016
  - activity2018
  - adopted-handrub
  - adopted-extract
  - adopted-receptor
  - rubric
  rule_id: 'native-review-checklist: exact-material and narrow claim evidence'
  native_severity: informational optional enrichment
  normalization_reason: Antibacterial inclusion is supported and no unsupported native
    protein mechanism is asserted.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/benzethonium-chloride.yaml
    role: Optional primary activity/evidence additions using validated writer and
      history
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Preserve curated additions across reseeding
actions:
- action_id: A1
  description: Normalize the exact documentary xref at its maintained source owner.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:31264
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Inherited numeric document xref
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained exact source-xref normalization or exclusion policy
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Validate source xref namespaces
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Preserve corrected document-versus-chemical mapping across reseeding
  acceptance_checks:
  - Confirm the source namespace error and suppress or correct only the numeric Wikipedia
    reference through a maintained source adjudication. Keep the already valid named
    Wikipedia document link.
  - Do not silently recast the number as an exact chemical xref without verifying
    the registry identity under its own namespace. Manufacturer metadata supports
    the likely origin, but subscription Reaxys content was not inspected here.
  - Regenerate through the documented pipeline during separately authorized curation
    and confirm correct document/chemical xref separation and resolvability. Run focused
    strict/reference/history and shared checks.
- action_id: A2
  description: Curate exact primary activity with endpoint and experimental scope
    intact.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:31264
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/benzethonium-chloride.yaml
    role: Optional primary activity/evidence additions using validated writer and
      history
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Preserve curated additions across reseeding
  acceptance_checks:
  - Use PMID 27974958 for explicitly qualified panel MIC observations only after reconciling
    abstract-versus-table ranges and narrative-versus-table gene counts. Preserve
    medium, inoculum, exposure duration, units and panel composition; do not turn
    MIC50/MIC90 into individual-strain MICs or adopt the paper's susceptibility thresholds
    as universally accepted clinical breakpoints.
  - For PMID 30410476 retain separate benzethonium and methyl benzethonium identities.
    The reported standalone 50 micromolar MIC is data not shown; FICi 0.63 is indifferent
    under the stated criterion, while ZIP results describe concentration-dependent
    regions. Do not attribute the two other drug combinations' biofilm reductions
    to benzethonium.
  - Obtain exact purified-compound and organism-specific primary support before adding
    detailed fungal/viral spectra or a membrane causal graph. PMID 16750419 hand-rub
    and essential-oil combination effects cannot support benzethonium-alone numerical
    activity. Host nicotinic receptor inhibition is not an antibacterial target.
  - Do not infer grapefruit biosynthesis from commercial extract contamination or
    resistance causality from gene carriage. If a future exact protein/response claim
    is proposed, perform the appropriate structured adapter and exact primary target/strain
    checks before curation.
  - Use write_validated_antibiotic and record_curation_event on data/antibiotics/antibacterial/benzethonium-chloride.yaml,
    preserve additions across reseeding and run native validation. Keep SEEDED until
    all native review criteria have been met.
limitations:
- Initial capture and all 13 source hashes were preserved and rechecked unchanged.
  The whole native record and exact maintained source row/configuration/code were
  inspected.
- Seven of ten adopted leads supplied original abstracts, all read. The three older
  urine-protein letters supplied bibliographic metadata but no abstract; attempted
  DOI routes did not expose their full text. They are not scientific support for the
  verdict.
- The two added antibacterial papers were read in complete main text including tables
  and figure captions. Raw assay data and all original figure images were not independently
  reanalyzed; source numerical/reporting inconsistencies are preserved for curator
  follow-up.
- The 2023 spectroscopy/activity article was read at publisher abstract scope. Author-deposited
  SSRN landing page was accessible, but its PDF returned 403; proposed mechanism and
  quantitative assay details remain unverified.
- The patent identity/context and Example 11 on p. 4 were inspected, including the
  original structural image. It was not treated as an antibacterial experiment or
  exhaustively audited for every claim.
- The native broad bacterial/fungal/mould/viral definition is faithfully source-attested.
  This bounded review independently inspected antibacterial experiments but did not
  establish a complete quantitative antifungal/antiviral spectrum or current clinical-use
  status.
- The numeric Wikipedia title returned 404; the named page resolved. The Wikipedia
  API route returned 403. Manufacturer data identifies the numeric string as Beilstein/Reaxys,
  but subscription registry content was not used.
- The initial custom chemistry diagnostic failure is retained; formula composition
  normalization explains it completely. No native formula, charge or mass edit is
  recommended.
- No native protein or transcriptomic assertion triggered iModulonDB. No exhaustive
  resistance, natural-producer or public-dataset inventory is claimed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
