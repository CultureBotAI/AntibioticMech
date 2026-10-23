# Flomoxef: coherent oxacephem identity with a side-chain naming correction

- Review: 20261021T163217Z-flomoxef-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T16:12:22Z
- Finished UTC: 2026-10-21T16:32:17Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact neutral flomoxef structure and checked chemical links agree. Original synthesis and susceptibility studies support antibacterial eligibility, with sodium-salt and strain-specific assay boundaries. One minor definition error adds an extra methyl unit to the side-chain name. ACC-1 and CfxA remain explicitly qualified database resistance assertions; their original experiments differ in how directly they address flomoxef.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 446; original thirteen input hashes preserved within twenty-two expanded inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:135813 | data/antibiotics/antibacterial/flomoxef.yaml | generated | flomoxef |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:135813 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:135813 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:135813 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:135813 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:135813 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:135813 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:135813 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:135813 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:135813 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:135813 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:135813 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:135813 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral 6R,7R oxacephem

identity: supported. Targets: CHEBI:135813.

Complete graph, stereochemistry, formula, charge and masses agree with checked authorities. Original synthesis distinguishes free acid from biologically tested sodium salt.

### Definition side-chain nomenclature

identity: concern. Targets: CHEBI:135813.

The extra methyl in difluoromethylthiomethylacetamido is inconsistent with the graph, systematic name and original precursor/compound drawings. The chemically correct chain is –NH–CO–CH2–S–CHF2.

### Exact structure versus drug-level associations

grounding: supported. Targets: CHEBI:135813.

Checked exact ChEBI/PubChem/ChEMBL graphs agree. KEGG and DrugCentral drug associations resolve. DrugBank and Reaxys remain bounded access limitations, not demonstrated mismatches.

### Antibacterial eligibility and spectrum

evidence: supported. Targets: CHEBI:135813.

Original synthesis and later isolated-strain experiments support antibacterial eligibility; salt, organism, MIC method and exposure regimen govern quantitative use. The RGM study and clinical cohorts prevent universal-spectrum or treatment-outcome extrapolation.

### Two imported beta-lactamase associations

evidence: unknown. Targets: CHEBI:135813.

Both entries faithfully declare database assertions. ACC-1 original cloned-host MICs provide flomoxef-specific phenotypic support without a purified flomoxef hydrolysis measurement. Inspected CfxA original tables concern other substrates and leave its exact flomoxef relationship unverified at primary-evidence depth. No confirmed false association was established.

### Oxacephem and cephalosporin relationship

scope: supported. Targets: CHEBI:135813.

The 1-oxa cephalosporin structure and antibacterial roles are coherent; the broader source class does not make this a conventional sulfur-containing cephem.

### Optional primary enrichment

completeness: unknown. Targets: CHEBI:135813.

No target, causal graph, activity or producer collection is required merely because optional fields exist. Exact primary assay and resistance enrichment is possible after preparation and endpoint adjudication. Host allergy and combined treatment cohorts do not fill direct bacterial mechanism gaps.

### Source ownership and history

provenance: supported. Targets: CHEBI:135813.

All four history events, original source rows and actual ARO owners were read; original thirteen hashes remain preserved in the expanded capture.

### Focused native checks

schema: supported. Targets: CHEBI:135813.

All focused checks pass; the definition wording defect requires chemical source inspection beyond schema validity.

## Findings

### F1: Definition adds an extra methyl unit to the side-chain name

minor / open / confirmed; issue key: flomoxef-definition-extra-thiomethyl-unit.

The definition names 2-[(difluoromethyl)thiomethyl]acetamido, whereas the native graph and complete systematic synonym encode –NH–CO–CH2–S–CHF2. Original compound 2 and precursor 4 in the 1985 synthesis confirm difluoromethylthioacetamido, equivalently 2-[(difluoromethyl)sulfanyl]acetamido. Correct the ChEBI-derived prose without changing the coherent molecular graph.

## Recommended Actions And Acceptance Checks

### A1

Correct the source-derived acetamido side-chain name.

- Use 2-[(difluoromethyl)sulfanyl]acetamido or an equivalent correct name for –NH–CO–CH2–S–CHF2.
- Preserve the existing neutral graph, stereochemistry and molecular formula.
- Regenerate through maintained source handling and run schema, strict and corpus checks.

### A2

If primary resistance or quantitative activity is curated, resolve exact preparation and endpoint scope.

- Retain ACC-1 host backgrounds and distinguish MIC increase from a contemporary resistant category or direct hydrolysis rate.
- Locate flomoxef-specific CfxA primary evidence before replacing its database qualifier.
- Keep original sodium-salt assays and unbound-exposure terminology distinct from neutral isolated reagent identity.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/flomoxef.yaml; Entire native record, both resistance entries and all four seed/reseed events | supports | The record denotes neutral (6R,7R) flomoxef, supplies antimicrobial and antibacterial roles and oxacephem/cephalosporin classification, and carries two explicitly database-level resistance assertions. The definition uses difluoromethylthiomethylacetamido while its systematic name and molecular graph have the shorter difluoromethylthioacetamido chain. No primary target, quantitative activity, producer or clinical product collection is asserted. |
| owners | 445447-raw-rows.json; 446-inputs-expanded.json; Complete ChEBI row 2566, ARO row 311 and resistance rows 4003–4004 | supports | Original input hashes were preserved and actual ARO identity/resistance owners appended before detailed judgment. The incorrect definition is ChEBI-derived; the two resistance edges are ARO-derived. |
| local-search | 445447-all-local-paths.txt; Ignored-inclusive label and reference search | context_only | Hidden and ignored files were included under data, curation, conf, scripts, src, reports and reviews. Exact native/source entries were inspected; absence of optional collections is not treated as a schema defect. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/135813/; Current CHEBI:135813 structure, systematic name, parents and roles | supports | Current ChEBI retains the exact neutral C15H18F2N6O7S2 graph, key UHRBTBZOWWGKMK-DOMZBBRYSA-N, complete 6R,7R stereochemistry and oxacephem classification. Its systematic name specifies 2-[(difluoromethyl)sulfanyl]acetamido, agreeing with the graph and original chemistry. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/65864/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON; PubChem CID 65864 molecular properties | supports | The complete neutral structure and formula match the native record. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL15413.json; CHEMBL15413 molecular structure | supports | The exact ChEMBL structure independently generates the native InChIKey. |
| aro | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3004014; ARO:3004014 source definition and identity | supports | The accession resolves to flomoxef and a cephalosporin source class. The native oxacephem is the 1-oxa cephalosporin analogue; no contradictory parent-class finding is established. Broad upstream activity wording is not promoted beyond the native claims. |
| acc-source | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3001815; ARO:3001815 ACC-1 definition and primary lead | supports | The source supplies the native inactivation association. Its beta-lactamase identity and the native database qualifier are retained; exact purified-drug kinetics require original assays. |
| cfx-source | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3003001; ARO:3003001 CfxA definition and primary lead | supports | The source supplies the native inactivation association. CfxA is the Bacteroides beta-lactamase, not an imported phenotype for every Bacteroides strain. |
| chemistry | 446-chemistry.json; 445447-xref-chemistry.json; Independent RDKit 2026.03.5 using batch019 interpreter against batch045 cwd | supports | Native SMILES/InChI, formula, charge, masses and source mints pass. Current ChEBI, PubChem and ChEMBL structures agree; KEGG drug and DrugCentral graphs also match, although drug_xrefs have broader drug-level semantics. |
| kegg-drug | https://rest.kegg.jp/get/D07963; KEGG D07963 entry and associated molfile | supports | The drug accession resolves to flomoxef and its molfile matches the neutral graph. This supports the association without imposing exact-equivalence semantics on drug_xrefs. |
| drugcentral | https://drugcentral.org/drugcard/1179; DrugCentral 1179 drug card and molfile | supports | The drug card resolves to flomoxef; the independently parsed molfile agrees with the native neutral graph. |
| drugbank-access | https://go.drugbank.com/drugs/DB11935; DrugBank DB11935 exact public request | unknown | The public request returned HTTP 403. This accession was not independently read; failure is not evidence of a wrong identifier. |
| reaxys-access | https://www.reaxys.com/#/search/quick?context=R&amp;query=RX.RN%3D6993219; Reaxys 6993219 exact public request | unknown | The public request returned HTTP 403. This accession was not independently read; failure is not evidence of a wrong identifier. |
| original1985 | https://www.jstage.jst.go.jp/article/antibiotics1968/38/4/38_4_466/_pdf; PMID 4008339 / DOI 10.7164/antibiotics.38.466; pp.466–470, actual structure of compound 2 and Scheme 1 on pp.466–467; MIC methods pp.470–471 | partial | The original explicitly depicts F2CH–S–CH2–CONH in compound 2 and F2CH–S–CH2–COOH in precursor 4. These confirm the shorter side chain and refute the extra methyl in the native definition. The free acid was prepared and then converted to sodium salt 6315-S for biological evaluation. Tables 2–3 distinguish this exact analogue from thia and side-chain comparators. MICs were measured by agar dilution in Eiken sensitivity agar, using overnight Tryptosoy culture diluted to about 10^6 cells/mL, incubation at 37°C for 18–20 h and visible-growth inhibition. Numerical sodium-salt measurements are not silently transferred to isolated neutral material. |
| acc-original | https://pmc.ncbi.nlm.nih.gov/articles/PMC89392/?pdf=1; PMID 10428914 / DOI 10.1128/AAC.43.8.1924; original Methods, full Table 2, Table 3 substrate list and relevant Results | partial | Table 2 reports flomoxef MICs of 2, 0.5, 0.06, 1 and 0.13 µg/mL for K. pneumoniae KUS, E. coli C600 transconjugant, C600 recipient, MV1190 transformant and MV1190 host, respectively. Cloned ACC-1 raises the MIC in a controlled host comparison; the clinical isolate/transconjugant also carries TEM-1. Table 3 purified-enzyme kinetics do not include flomoxef. Thus the original supports a bounded resistance-associated phenotype but does not directly quantify flomoxef hydrolysis or establish a contemporary clinical resistant breakpoint. Flomoxef was supplied by Shionogi without exact salt documentation in the inspected methods. |
| cfx-original | https://pmc.ncbi.nlm.nih.gov/articles/PMC187887/?pdf=1; PMID 8517690 / DOI 10.1128/AAC.37.5.1028; original abstract and scanned paper | partial | The original establishes CfxA-mediated cefoxitin resistance in B. vulgatus CLA341 and cloned B. fragilis backgrounds, with inactivation and gene-disruption experiments. Original scanned Methods, Tables 1–2 and relevant Discussion were read from the archived page images. Those susceptibility/substrate panels do not supply a flomoxef-specific assay; the native CfxA–flomoxef association remains at its declared database tier. This does not prove the database edge false. |
| cfx-page-1 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/30fa/187887/3b091105803a/aac00027-0130.png; p.1028 Methods | context_only | MIC methods use Wilkins-Chalgren agar dilution with results after 48 h; strain identity and source are stated. |
| cfx-page-2 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/30fa/187887/afa1f95d2be1/aac00027-0131.png; p.1029 enzymatic methods | context_only | Crude-extract substrate assays list monitored beta-lactams; no flomoxef-specific assay is described in this inspected section. |
| cfx-page-3 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/30fa/187887/44ef01db9c30/aac00027-0132.png; p.1030 Table 1 and Results | context_only | The original Table 1 compares cefoxitin and ampicillin MICs and cefoxitin degradation in donor, cloned and disrupted backgrounds. |
| cfx-page-4 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/30fa/187887/a41326331a8f/aac00027-0133.png; p.1031 Table 2 | context_only | The complete substrate panel contains cephaloridine, cephalothin, penicillin G, ampicillin, cefotaxime, cefoxitin and nitrocefin; it does not establish flomoxef kinetics. |
| cfx-page-7 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/30fa/187887/c39bec0433f9/aac00027-0136.png; p.1034 relevant Discussion | context_only | Discussion distinguishes CfxA from other Bacteroides beta-lactamases and limits the molecular conclusions to the studied systems. |
| cfx-page-8 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/30fa/187887/5572d5a0fe62/aac00027-0137.png; p.1035 Discussion | context_only | Cloning and insertional inactivation support cefoxitin resistance; this is not evidence of a flomoxef-specific quantitative endpoint. |
| original2023 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10508154/?pdf=render; PMID 37610203 / DOI 10.1128/aac.00258-23; Methods, selected-strain Results, flomoxef rows of Table 2 and Discussion | partial | The paper measures broth microdilution MICs by CLSI M07-Ed11 and humanized chemostat time-kill behavior in five selected CTX-M-producing E. coli and two K. pneumoniae strains. Selected flomoxef exposures suppress these tested strains; this is not universal ESBL susceptibility or clinical efficacy. The paper states that CLSI flomoxef breakpoints were unavailable. Its free form terminology means unbound exposure, not proof that the isolated reagent was neutral free acid. Exact reagent salt/purity was not established from the inspected methods. |
| lead-12803802 | https://pubmed.ncbi.nlm.nih.gov/12803802/; Complete adopted abstract in 446-core.json | context_only | Original serum capillary-electrophoresis analytical method; useful drug identity/assay context, not a bacterial target experiment. |
| lead-18606583 | https://pubmed.ncbi.nlm.nih.gov/18606583/; Complete adopted abstract in 446-core.json | context_only | Original broth-MIC survey of 61 rapidly growing mycobacteria. The abstract distinguishes M. abscessus MIC90 above 128 µg/mL from M. fortuitum MIC90 of 4 µg/mL and three of four M. peregrinum isolates at no more than 4 µg/mL; it does not support uniform species-wide susceptibility or exact salt assignment. |
| lead-25694055 | https://pubmed.ncbi.nlm.nih.gov/25694055/; Complete adopted abstract in 446-core.json | context_only | Original 2,955-isolate Chinese in vitro survey using agar dilution. Reported strain-panel susceptibility and historical interpretive categories are not current breakpoint guidance. |
| lead-26100708 | https://pubmed.ncbi.nlm.nih.gov/26100708/; Complete adopted abstract in 446-core.json | context_only | Retrospective ESBL bacteremia cohort compares a combined cefmetazole/flomoxef group with carbapenems. Aggregate outcomes cannot be attributed to flomoxef alone. |
| lead-26387064 | https://pubmed.ncbi.nlm.nih.gov/26387064/; Complete adopted abstract in 446-core.json | context_only | Original retrospective ESBL bacteremia comparison reports poorer flomoxef outcomes particularly at higher MICs. Clinical treatment outcomes are distinct from isolated in vitro growth inhibition. |
| lead-28543395 | https://pubmed.ncbi.nlm.nih.gov/28543395/; Complete adopted abstract in 446-core.json | context_only | Original cefotiam contact-urticaria report concerns host hypersensitivity and potential beta-lactam cross-reactivity; the complete abstract does not establish a flomoxef antibacterial mechanism. |
| lead-29017833 | https://pubmed.ncbi.nlm.nih.gov/29017833/; Complete adopted abstract in 446-core.json | context_only | A beta-lactam hypersensitivity review, used only as contextual literature; it is not original antibacterial mechanism evidence. |
| lead-37610203 | https://pubmed.ncbi.nlm.nih.gov/37610203/; Complete adopted abstract in 446-core.json | context_only | Original ESBL chemostat study, followed to its full Methods and selected-strain results in the separate evidence item. |
| lead-4008339 | https://pubmed.ncbi.nlm.nih.gov/4008339/; Complete adopted abstract in 446-core.json | context_only | Original synthesis and antibacterial evaluation, followed to original structure figures, relevant tables and MIC methods with explicit sodium-salt scope. |
| adapter | 445447-adapter-search-results.json; Catalog and ACC-1/CfxA searches before open web research | context_only | No exact source-organism dataset was available for the K. pneumoniae/B. vulgatus resistance experiments. E. coli precise1k context searches returned no corresponding ACC-1 or CfxA hit. This is not negative biological evidence. |
| gates | 446-focused-results.json; Actual focused executions | supports | Independent chemistry, own-environment schema and strict checks all exited 0 on the unchanged native record. |

## Limits And Additional Notes

- All nine adopted PMID abstracts were read in full. The 1985 original was inspected for identity figures, relevant structure/activity tables and MIC methods; every preparative experimental paragraph and analogue was not independently audited.
- The 1999 ACC-1 original was read for relevant methods, full MIC table, purified-substrate table and results; raw sequence and gel data were not independently reanalyzed.
- For the 1993 CfxA original, archived page images 1028–1031 and 1034–1035 were inspected for methods, susceptibility/substrate tables and discussion. Sequence-alignment and gel details on other pages were not independently reanalyzed, and no flomoxef-specific result was established.
- The 2023 original was inspected for methods and selected flomoxef chemostat results. All supplemental strain/analytical datasets were not independently audited; no current treatment or breakpoint guidance is claimed.
- DrugBank and Reaxys requests returned HTTP 403. An authoritative CAS registry graph was not separately obtained. Wikipedia was resolved only as a document reference.
- The 2023 phrase free form describes unbound drug exposure, not a chemically verified neutral reagent. Exact preparation certificates were not recovered for all later experiments.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Native and maintained files were not edited; original and expanded input hashes were rechecked. Optional links and tags were checked for this flomoxef target.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T163217Z-flomoxef-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Flomoxef: coherent oxacephem identity with a side-chain naming correction'
started_at: '2026-10-21T16:12:22Z'
finished_at: '2026-10-21T16:32:17Z'
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
summary: The exact neutral flomoxef structure and checked chemical links agree. Original
  synthesis and susceptibility studies support antibacterial eligibility, with sodium-salt
  and strain-specific assay boundaries. One minor definition error adds an extra methyl
  unit to the side-chain name. ACC-1 and CfxA remain explicitly qualified database
  resistance assertions; their original experiments differ in how directly they address
  flomoxef.
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
  - path: data/antibiotics/antibacterial/flomoxef.yaml
    sha256: 1e7835c7dd7da6d5e86c74eed4944e4ffbfaf080039245d87cb008d795b4148b
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
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
targets:
- target_id: CHEBI:135813
  path: data/antibiotics/antibacterial/flomoxef.yaml
  label: flomoxef
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
    path: data/raw/aro_resistance_edges.tsv
    role: Actual imported resistance assertions
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 446; original thirteen input hashes preserved within twenty-two
    expanded inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:135813
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:135813
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/445447-focused.py
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:135813
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/flomoxef.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:135813
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/flomoxef.yaml --out /private/tmp/am-review-session/446-strict.tsv
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
  - CHEBI:135813
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
  - CHEBI:135813
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
  - CHEBI:135813
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
  - CHEBI:135813
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
  - CHEBI:135813
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
  - CHEBI:135813
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
  - CHEBI:135813
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
  - CHEBI:135813
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
  - CHEBI:135813
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/flomoxef.yaml
  locator: Entire native record, both resistance entries and all four seed/reseed
    events
  accessed_at: '2026-10-21T16:31:34Z'
  support: supports
  summary: The record denotes neutral (6R,7R) flomoxef, supplies antimicrobial and
    antibacterial roles and oxacephem/cephalosporin classification, and carries two
    explicitly database-level resistance assertions. The definition uses difluoromethylthiomethylacetamido
    while its systematic name and molecular graph have the shorter difluoromethylthioacetamido
    chain. No primary target, quantitative activity, producer or clinical product
    collection is asserted.
- evidence_id: owners
  kind: record_content
  reference: 445447-raw-rows.json; 446-inputs-expanded.json
  locator: Complete ChEBI row 2566, ARO row 311 and resistance rows 4003–4004
  accessed_at: '2026-10-21T16:31:34Z'
  support: supports
  summary: Original input hashes were preserved and actual ARO identity/resistance
    owners appended before detailed judgment. The incorrect definition is ChEBI-derived;
    the two resistance edges are ARO-derived.
  snapshot_sha256: 13d552de8b6fa684796f189c526ffb34c820d1ee4f8a85ef72edd4e4a9344a4f
- evidence_id: local-search
  kind: search
  reference: 445447-all-local-paths.txt
  locator: Ignored-inclusive label and reference search
  accessed_at: '2026-10-21T16:31:34Z'
  support: context_only
  summary: Hidden and ignored files were included under data, curation, conf, scripts,
    src, reports and reviews. Exact native/source entries were inspected; absence
    of optional collections is not treated as a schema defect.
  search_scope: rg --no-ignore --hidden -il 'fleroxacin|flomoxef|florfenicol' data
    curation conf scripts src reports reviews
  snapshot_sha256: 02ab6bf102133423d462e55ab1f710d651b6d6e91b6faf9eec666d468a4a4617
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/135813/
  locator: Current CHEBI:135813 structure, systematic name, parents and roles
  accessed_at: '2026-10-21T16:22:18.454597Z'
  support: supports
  summary: Current ChEBI retains the exact neutral C15H18F2N6O7S2 graph, key UHRBTBZOWWGKMK-DOMZBBRYSA-N,
    complete 6R,7R stereochemistry and oxacephem classification. Its systematic name
    specifies 2-[(difluoromethyl)sulfanyl]acetamido, agreeing with the graph and original
    chemistry.
  snapshot_sha256: 9f213f2eda697dc426b66912a3dffb3b1cbe32e9891aacc297e8a4b851c3a523
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/65864/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON
  locator: PubChem CID 65864 molecular properties
  accessed_at: '2026-10-21T16:22:18.733734Z'
  support: supports
  summary: The complete neutral structure and formula match the native record.
  snapshot_sha256: 6b62ead643992c17ff22b025c198c952a21a14ff6aaea7dd0b51e4b8fff43118
- evidence_id: chembl
  kind: authority
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL15413.json
  locator: CHEMBL15413 molecular structure
  accessed_at: '2026-10-21T16:22:18.735738Z'
  support: supports
  summary: The exact ChEMBL structure independently generates the native InChIKey.
  snapshot_sha256: 47064ecdc1d1dbdd53a8e24b5a5a69a64b2af62d48b24f63d6a13edf707173fe
- evidence_id: aro
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3004014
  locator: ARO:3004014 source definition and identity
  accessed_at: '2026-10-21T16:22:20.893643Z'
  support: supports
  summary: The accession resolves to flomoxef and a cephalosporin source class. The
    native oxacephem is the 1-oxa cephalosporin analogue; no contradictory parent-class
    finding is established. Broad upstream activity wording is not promoted beyond
    the native claims.
  snapshot_sha256: e1a7b46c5e01e19c9d95efcdab4169f423594b84d0b5007c733fda516520383f
- evidence_id: acc-source
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3001815
  locator: ARO:3001815 ACC-1 definition and primary lead
  accessed_at: '2026-10-21T16:22:20.951962Z'
  support: supports
  summary: The source supplies the native inactivation association. Its beta-lactamase
    identity and the native database qualifier are retained; exact purified-drug kinetics
    require original assays.
  snapshot_sha256: cda785bf59796b8a76febee5a10d8e8bea491af820c2fc1f5581670414deb957
- evidence_id: cfx-source
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3003001
  locator: ARO:3003001 CfxA definition and primary lead
  accessed_at: '2026-10-21T16:22:20.971748Z'
  support: supports
  summary: The source supplies the native inactivation association. CfxA is the Bacteroides
    beta-lactamase, not an imported phenotype for every Bacteroides strain.
  snapshot_sha256: 3cd76eb4cab6b8b641073a7fa7ac7f7a3ccfea3145c03f9bc50967d32ea8d86a
- evidence_id: chemistry
  kind: record_content
  reference: 446-chemistry.json; 445447-xref-chemistry.json
  locator: Independent RDKit 2026.03.5 using batch019 interpreter against batch045
    cwd
  accessed_at: '2026-10-21T16:31:34Z'
  support: supports
  summary: Native SMILES/InChI, formula, charge, masses and source mints pass. Current
    ChEBI, PubChem and ChEMBL structures agree; KEGG drug and DrugCentral graphs also
    match, although drug_xrefs have broader drug-level semantics.
  snapshot_sha256: c329fdfb10a094a53e4f98112fdcfdecd282f524607708e5eb553c0f64c3f1ad
- evidence_id: kegg-drug
  kind: authority
  reference: https://rest.kegg.jp/get/D07963
  locator: KEGG D07963 entry and associated molfile
  accessed_at: '2026-10-21T16:22:18.975212Z'
  support: supports
  summary: The drug accession resolves to flomoxef and its molfile matches the neutral
    graph. This supports the association without imposing exact-equivalence semantics
    on drug_xrefs.
  snapshot_sha256: 47e3e771c4ca1278c89b012f95e5a8abb99baf103fe30792e4447413c95d1c64
- evidence_id: drugcentral
  kind: authority
  reference: https://drugcentral.org/drugcard/1179
  locator: DrugCentral 1179 drug card and molfile
  accessed_at: '2026-10-21T16:22:22.879075Z'
  support: supports
  summary: The drug card resolves to flomoxef; the independently parsed molfile agrees
    with the native neutral graph.
  snapshot_sha256: bfaf8eb9791e64c94c91c74dafc7877e2be86385cc94eed74c69f20836167428
- evidence_id: drugbank-access
  kind: search
  reference: https://go.drugbank.com/drugs/DB11935
  locator: DrugBank DB11935 exact public request
  accessed_at: '2026-10-21T16:22:23.200409Z'
  support: unknown
  summary: The public request returned HTTP 403. This accession was not independently
    read; failure is not evidence of a wrong identifier.
  snapshot_sha256: a701b4626e3c55b435113360e90277296548ce639a98291899b762fd58664541
  search_scope: Exact native accession through its public endpoint.
- evidence_id: reaxys-access
  kind: search
  reference: https://www.reaxys.com/#/search/quick?context=R&query=RX.RN%3D6993219
  locator: Reaxys 6993219 exact public request
  accessed_at: '2026-10-21T16:22:23.257600Z'
  support: unknown
  summary: The public request returned HTTP 403. This accession was not independently
    read; failure is not evidence of a wrong identifier.
  snapshot_sha256: 8a4f0db6295c67645b1d080b0eb13ea152f97ec46d114814f77f5e82ce21d9d9
  search_scope: Exact native accession through its public endpoint.
- evidence_id: original1985
  kind: primary_source
  reference: https://www.jstage.jst.go.jp/article/antibiotics1968/38/4/38_4_466/_pdf
  locator: PMID 4008339 / DOI 10.7164/antibiotics.38.466; pp.466–470, actual structure
    of compound 2 and Scheme 1 on pp.466–467; MIC methods pp.470–471
  accessed_at: '2026-10-21T16:26:21.385308Z'
  support: partial
  summary: The original explicitly depicts F2CH–S–CH2–CONH in compound 2 and F2CH–S–CH2–COOH
    in precursor 4. These confirm the shorter side chain and refute the extra methyl
    in the native definition. The free acid was prepared and then converted to sodium
    salt 6315-S for biological evaluation. Tables 2–3 distinguish this exact analogue
    from thia and side-chain comparators. MICs were measured by agar dilution in Eiken
    sensitivity agar, using overnight Tryptosoy culture diluted to about 10^6 cells/mL,
    incubation at 37°C for 18–20 h and visible-growth inhibition. Numerical sodium-salt
    measurements are not silently transferred to isolated neutral material.
  snapshot_sha256: 1a008c9857e1643f89a5fb0610c0645a728c07614b03241858f0c194fb1097dd
- evidence_id: acc-original
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC89392/?pdf=1
  locator: PMID 10428914 / DOI 10.1128/AAC.43.8.1924; original Methods, full Table
    2, Table 3 substrate list and relevant Results
  accessed_at: '2026-10-21T16:27:06.778124Z'
  support: partial
  summary: Table 2 reports flomoxef MICs of 2, 0.5, 0.06, 1 and 0.13 µg/mL for K.
    pneumoniae KUS, E. coli C600 transconjugant, C600 recipient, MV1190 transformant
    and MV1190 host, respectively. Cloned ACC-1 raises the MIC in a controlled host
    comparison; the clinical isolate/transconjugant also carries TEM-1. Table 3 purified-enzyme
    kinetics do not include flomoxef. Thus the original supports a bounded resistance-associated
    phenotype but does not directly quantify flomoxef hydrolysis or establish a contemporary
    clinical resistant breakpoint. Flomoxef was supplied by Shionogi without exact
    salt documentation in the inspected methods.
  snapshot_sha256: 52e9aa14eb8efb0482348c65876ef6ad185d7514432b123af941794b09eaba3f
- evidence_id: cfx-original
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC187887/?pdf=1
  locator: PMID 8517690 / DOI 10.1128/AAC.37.5.1028; original abstract and scanned
    paper
  accessed_at: '2026-10-21T16:27:06.779366Z'
  support: partial
  summary: The original establishes CfxA-mediated cefoxitin resistance in B. vulgatus
    CLA341 and cloned B. fragilis backgrounds, with inactivation and gene-disruption
    experiments. Original scanned Methods, Tables 1–2 and relevant Discussion were
    read from the archived page images. Those susceptibility/substrate panels do not
    supply a flomoxef-specific assay; the native CfxA–flomoxef association remains
    at its declared database tier. This does not prove the database edge false.
  snapshot_sha256: 08d24529a36bfd20af3843f489a277dc799dcd3bdd8576e61084703b759565ad
- evidence_id: cfx-page-1
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/30fa/187887/3b091105803a/aac00027-0130.png
  locator: p.1028 Methods
  accessed_at: '2026-10-21T16:29:55.059309Z'
  support: context_only
  summary: MIC methods use Wilkins-Chalgren agar dilution with results after 48 h;
    strain identity and source are stated.
  snapshot_sha256: 2d58f7059a8052164c32a147302eeaaeaa6161c90d198603f1160c00f8069b76
- evidence_id: cfx-page-2
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/30fa/187887/afa1f95d2be1/aac00027-0131.png
  locator: p.1029 enzymatic methods
  accessed_at: '2026-10-21T16:29:55.062750Z'
  support: context_only
  summary: Crude-extract substrate assays list monitored beta-lactams; no flomoxef-specific
    assay is described in this inspected section.
  snapshot_sha256: 72ffac86afbbfba989d7f820c3ef59ec734d631e107416b961e4d639a51bd6ed
- evidence_id: cfx-page-3
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/30fa/187887/44ef01db9c30/aac00027-0132.png
  locator: p.1030 Table 1 and Results
  accessed_at: '2026-10-21T16:29:55.073531Z'
  support: context_only
  summary: The original Table 1 compares cefoxitin and ampicillin MICs and cefoxitin
    degradation in donor, cloned and disrupted backgrounds.
  snapshot_sha256: 2d18f3088dd0c19303d7b9b57b860cb11c7c45c270d1bc0248c27b70cc7c866a
- evidence_id: cfx-page-4
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/30fa/187887/a41326331a8f/aac00027-0133.png
  locator: p.1031 Table 2
  accessed_at: '2026-10-21T16:29:55.078988Z'
  support: context_only
  summary: The complete substrate panel contains cephaloridine, cephalothin, penicillin
    G, ampicillin, cefotaxime, cefoxitin and nitrocefin; it does not establish flomoxef
    kinetics.
  snapshot_sha256: 21dcc024237a8d1ce5ad63e2b1ce467d00377bfe89bd08d95adbfab486befe6c
- evidence_id: cfx-page-7
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/30fa/187887/c39bec0433f9/aac00027-0136.png
  locator: p.1034 relevant Discussion
  accessed_at: '2026-10-21T16:29:55.354889Z'
  support: context_only
  summary: Discussion distinguishes CfxA from other Bacteroides beta-lactamases and
    limits the molecular conclusions to the studied systems.
  snapshot_sha256: 817f3bb66b0f9f8a2177583b4a5dd18987271b6d383140f6bc6c83d6aadfc424
- evidence_id: cfx-page-8
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/30fa/187887/5572d5a0fe62/aac00027-0137.png
  locator: p.1035 Discussion
  accessed_at: '2026-10-21T16:29:55.357699Z'
  support: context_only
  summary: Cloning and insertional inactivation support cefoxitin resistance; this
    is not evidence of a flomoxef-specific quantitative endpoint.
  snapshot_sha256: 23a06c3efc0fbd238fc35b694af5c3651a2e9056eb96b9e6b2344af37f38c49a
- evidence_id: original2023
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC10508154/?pdf=render
  locator: PMID 37610203 / DOI 10.1128/aac.00258-23; Methods, selected-strain Results,
    flomoxef rows of Table 2 and Discussion
  accessed_at: '2026-10-21T16:26:21.387908Z'
  support: partial
  summary: The paper measures broth microdilution MICs by CLSI M07-Ed11 and humanized
    chemostat time-kill behavior in five selected CTX-M-producing E. coli and two
    K. pneumoniae strains. Selected flomoxef exposures suppress these tested strains;
    this is not universal ESBL susceptibility or clinical efficacy. The paper states
    that CLSI flomoxef breakpoints were unavailable. Its free form terminology means
    unbound exposure, not proof that the isolated reagent was neutral free acid. Exact
    reagent salt/purity was not established from the inspected methods.
  snapshot_sha256: cca38b2035defdd56d06537b9b0fd859af7f345f26e82eeca9353a207fb434b6
- evidence_id: lead-12803802
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/12803802/
  locator: Complete adopted abstract in 446-core.json
  accessed_at: '2026-10-21T16:22:18.050191Z'
  support: context_only
  summary: Original serum capillary-electrophoresis analytical method; useful drug
    identity/assay context, not a bacterial target experiment.
  snapshot_sha256: 560ceeadac81d8df52c2ef14bbe83f86f9287fb8c70557c7aa82f8fa360ce22b
- evidence_id: lead-18606583
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/18606583/
  locator: Complete adopted abstract in 446-core.json
  accessed_at: '2026-10-21T16:22:18.050191Z'
  support: context_only
  summary: Original broth-MIC survey of 61 rapidly growing mycobacteria. The abstract
    distinguishes M. abscessus MIC90 above 128 µg/mL from M. fortuitum MIC90 of 4
    µg/mL and three of four M. peregrinum isolates at no more than 4 µg/mL; it does
    not support uniform species-wide susceptibility or exact salt assignment.
  snapshot_sha256: 560ceeadac81d8df52c2ef14bbe83f86f9287fb8c70557c7aa82f8fa360ce22b
- evidence_id: lead-25694055
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/25694055/
  locator: Complete adopted abstract in 446-core.json
  accessed_at: '2026-10-21T16:22:18.050191Z'
  support: context_only
  summary: Original 2,955-isolate Chinese in vitro survey using agar dilution. Reported
    strain-panel susceptibility and historical interpretive categories are not current
    breakpoint guidance.
  snapshot_sha256: 560ceeadac81d8df52c2ef14bbe83f86f9287fb8c70557c7aa82f8fa360ce22b
- evidence_id: lead-26100708
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/26100708/
  locator: Complete adopted abstract in 446-core.json
  accessed_at: '2026-10-21T16:22:18.050191Z'
  support: context_only
  summary: Retrospective ESBL bacteremia cohort compares a combined cefmetazole/flomoxef
    group with carbapenems. Aggregate outcomes cannot be attributed to flomoxef alone.
  snapshot_sha256: 560ceeadac81d8df52c2ef14bbe83f86f9287fb8c70557c7aa82f8fa360ce22b
- evidence_id: lead-26387064
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/26387064/
  locator: Complete adopted abstract in 446-core.json
  accessed_at: '2026-10-21T16:22:18.050191Z'
  support: context_only
  summary: Original retrospective ESBL bacteremia comparison reports poorer flomoxef
    outcomes particularly at higher MICs. Clinical treatment outcomes are distinct
    from isolated in vitro growth inhibition.
  snapshot_sha256: 560ceeadac81d8df52c2ef14bbe83f86f9287fb8c70557c7aa82f8fa360ce22b
- evidence_id: lead-28543395
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/28543395/
  locator: Complete adopted abstract in 446-core.json
  accessed_at: '2026-10-21T16:22:18.050191Z'
  support: context_only
  summary: Original cefotiam contact-urticaria report concerns host hypersensitivity
    and potential beta-lactam cross-reactivity; the complete abstract does not establish
    a flomoxef antibacterial mechanism.
  snapshot_sha256: 560ceeadac81d8df52c2ef14bbe83f86f9287fb8c70557c7aa82f8fa360ce22b
- evidence_id: lead-29017833
  kind: search
  reference: https://pubmed.ncbi.nlm.nih.gov/29017833/
  locator: Complete adopted abstract in 446-core.json
  accessed_at: '2026-10-21T16:22:18.050191Z'
  support: context_only
  summary: A beta-lactam hypersensitivity review, used only as contextual literature;
    it is not original antibacterial mechanism evidence.
  snapshot_sha256: 560ceeadac81d8df52c2ef14bbe83f86f9287fb8c70557c7aa82f8fa360ce22b
  search_scope: Disposition of an adopted secondary review after reading its complete
    abstract.
- evidence_id: lead-37610203
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/37610203/
  locator: Complete adopted abstract in 446-core.json
  accessed_at: '2026-10-21T16:22:18.050191Z'
  support: context_only
  summary: Original ESBL chemostat study, followed to its full Methods and selected-strain
    results in the separate evidence item.
  snapshot_sha256: 560ceeadac81d8df52c2ef14bbe83f86f9287fb8c70557c7aa82f8fa360ce22b
- evidence_id: lead-4008339
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/4008339/
  locator: Complete adopted abstract in 446-core.json
  accessed_at: '2026-10-21T16:22:18.050191Z'
  support: context_only
  summary: Original synthesis and antibacterial evaluation, followed to original structure
    figures, relevant tables and MIC methods with explicit sodium-salt scope.
  snapshot_sha256: 560ceeadac81d8df52c2ef14bbe83f86f9287fb8c70557c7aa82f8fa360ce22b
- evidence_id: adapter
  kind: search
  reference: 445447-adapter-search-results.json
  locator: Catalog and ACC-1/CfxA searches before open web research
  accessed_at: '2026-10-21T16:31:34Z'
  support: context_only
  summary: No exact source-organism dataset was available for the K. pneumoniae/B.
    vulgatus resistance experiments. E. coli precise1k context searches returned no
    corresponding ACC-1 or CfxA hit. This is not negative biological evidence.
  search_scope: Structured iModulonDB catalog followed by e_coli/precise1k ACC-1 and
    CfxA queries before open-ended protein research.
  snapshot_sha256: 6cb72373a60d6274d0f36d88e2dd7faed5c00019d0841d1204d1c367d19ecd1a
- evidence_id: gates
  kind: validation
  reference: 446-focused-results.json
  locator: Actual focused executions
  accessed_at: '2026-10-21T16:31:34Z'
  support: supports
  summary: Independent chemistry, own-environment schema and strict checks all exited
    0 on the unchanged native record.
  snapshot_sha256: e3888e74a4437c02210b24c70cc35506020e639102aa560e717913907939981c
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral 6R,7R oxacephem
  outcome: supported
  summary: Complete graph, stereochemistry, formula, charge and masses agree with
    checked authorities. Original synthesis distinguishes free acid from biologically
    tested sodium salt.
  target_ids:
  - CHEBI:135813
  evidence_ids:
  - native
  - chebi
  - pubchem
  - chembl
  - chemistry
  - original1985
- assessment_id: names
  area: identity
  topic: Definition side-chain nomenclature
  outcome: concern
  summary: The extra methyl in difluoromethylthiomethylacetamido is inconsistent with
    the graph, systematic name and original precursor/compound drawings. The chemically
    correct chain is –NH–CO–CH2–S–CHF2.
  target_ids:
  - CHEBI:135813
  evidence_ids:
  - native
  - chebi
  - chemistry
  - original1985
- assessment_id: grounding
  area: grounding
  topic: Exact structure versus drug-level associations
  outcome: supported
  summary: Checked exact ChEBI/PubChem/ChEMBL graphs agree. KEGG and DrugCentral drug
    associations resolve. DrugBank and Reaxys remain bounded access limitations, not
    demonstrated mismatches.
  target_ids:
  - CHEBI:135813
  evidence_ids:
  - chebi
  - pubchem
  - chembl
  - kegg-drug
  - drugcentral
  - drugbank-access
  - reaxys-access
  - chemistry
- assessment_id: activity
  area: evidence
  topic: Antibacterial eligibility and spectrum
  outcome: supported
  summary: Original synthesis and later isolated-strain experiments support antibacterial
    eligibility; salt, organism, MIC method and exposure regimen govern quantitative
    use. The RGM study and clinical cohorts prevent universal-spectrum or treatment-outcome
    extrapolation.
  target_ids:
  - CHEBI:135813
  evidence_ids:
  - original1985
  - original2023
  - lead-18606583
  - lead-25694055
  - lead-26100708
  - lead-26387064
- assessment_id: resistance
  area: evidence
  topic: Two imported beta-lactamase associations
  outcome: unknown
  summary: Both entries faithfully declare database assertions. ACC-1 original cloned-host
    MICs provide flomoxef-specific phenotypic support without a purified flomoxef
    hydrolysis measurement. Inspected CfxA original tables concern other substrates
    and leave its exact flomoxef relationship unverified at primary-evidence depth.
    No confirmed false association was established.
  target_ids:
  - CHEBI:135813
  evidence_ids:
  - native
  - acc-source
  - cfx-source
  - acc-original
  - cfx-original
  - cfx-page-3
  - cfx-page-4
  - adapter
- assessment_id: classification
  area: scope
  topic: Oxacephem and cephalosporin relationship
  outcome: supported
  summary: The 1-oxa cephalosporin structure and antibacterial roles are coherent;
    the broader source class does not make this a conventional sulfur-containing cephem.
  target_ids:
  - CHEBI:135813
  evidence_ids:
  - native
  - aro
  - chebi
  - original1985
- assessment_id: completeness
  area: completeness
  topic: Optional primary enrichment
  outcome: unknown
  summary: No target, causal graph, activity or producer collection is required merely
    because optional fields exist. Exact primary assay and resistance enrichment is
    possible after preparation and endpoint adjudication. Host allergy and combined
    treatment cohorts do not fill direct bacterial mechanism gaps.
  target_ids:
  - CHEBI:135813
  evidence_ids:
  - native
  - local-search
  - original1985
  - original2023
  - lead-28543395
  - lead-29017833
- assessment_id: provenance
  area: provenance
  topic: Source ownership and history
  outcome: supported
  summary: All four history events, original source rows and actual ARO owners were
    read; original thirteen hashes remain preserved in the expanded capture.
  target_ids:
  - CHEBI:135813
  evidence_ids:
  - native
  - owners
  - gates
- assessment_id: validation
  area: schema
  topic: Focused native checks
  outcome: supported
  summary: All focused checks pass; the definition wording defect requires chemical
    source inspection beyond schema validity.
  target_ids:
  - CHEBI:135813
  evidence_ids:
  - gates
  - chemistry
findings:
- finding_id: F1
  issue_key: flomoxef-definition-extra-thiomethyl-unit
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: Definition adds an extra methyl unit to the side-chain name
  description: The definition names 2-[(difluoromethyl)thiomethyl]acetamido, whereas
    the native graph and complete systematic synonym encode –NH–CO–CH2–S–CHF2. Original
    compound 2 and precursor 4 in the 1985 synthesis confirm difluoromethylthioacetamido,
    equivalently 2-[(difluoromethyl)sulfanyl]acetamido. Correct the ChEBI-derived
    prose without changing the coherent molecular graph.
  target_ids:
  - CHEBI:135813
  field_paths:
  - definition
  evidence_ids:
  - native
  - chebi
  - chemistry
  - original1985
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI source definition extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  rule_id: review-checklist:Nomenclature
  native_severity: minor
  normalization_reason: The exact molecular identity and structure remain coherent;
    the defect is a localized definition naming error.
actions:
- action_id: A1
  description: Correct the source-derived acetamido side-chain name.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:135813
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI source definition extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Use 2-[(difluoromethyl)sulfanyl]acetamido or an equivalent correct name for –NH–CO–CH2–S–CHF2.
  - Preserve the existing neutral graph, stereochemistry and molecular formula.
  - Regenerate through maintained source handling and run schema, strict and corpus
    checks.
- action_id: A2
  description: If primary resistance or quantitative activity is curated, resolve
    exact preparation and endpoint scope.
  finding_ids: []
  target_ids:
  - CHEBI:135813
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Actual imported resistance assertions
  acceptance_checks:
  - Retain ACC-1 host backgrounds and distinguish MIC increase from a contemporary
    resistant category or direct hydrolysis rate.
  - Locate flomoxef-specific CfxA primary evidence before replacing its database qualifier.
  - Keep original sodium-salt assays and unbound-exposure terminology distinct from
    neutral isolated reagent identity.
limitations:
- All nine adopted PMID abstracts were read in full. The 1985 original was inspected
  for identity figures, relevant structure/activity tables and MIC methods; every
  preparative experimental paragraph and analogue was not independently audited.
- The 1999 ACC-1 original was read for relevant methods, full MIC table, purified-substrate
  table and results; raw sequence and gel data were not independently reanalyzed.
- For the 1993 CfxA original, archived page images 1028–1031 and 1034–1035 were inspected
  for methods, susceptibility/substrate tables and discussion. Sequence-alignment
  and gel details on other pages were not independently reanalyzed, and no flomoxef-specific
  result was established.
- The 2023 original was inspected for methods and selected flomoxef chemostat results.
  All supplemental strain/analytical datasets were not independently audited; no current
  treatment or breakpoint guidance is claimed.
- DrugBank and Reaxys requests returned HTTP 403. An authoritative CAS registry graph
  was not separately obtained. Wikipedia was resolved only as a document reference.
- The 2023 phrase free form describes unbound drug exposure, not a chemically verified
  neutral reagent. Exact preparation certificates were not recovered for all later
  experiments.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Native and maintained files were not edited; original and expanded input hashes
  were rechecked. Optional links and tags were checked for this flomoxef target.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://doi.org/10.7164/antibiotics.38.466
- https://doi.org/10.1128/AAC.43.8.1924
- https://doi.org/10.1128/aac.00258-23
tags:
- flomoxef
- oxacephem
- beta-lactamase
- definition-nomenclature
```
