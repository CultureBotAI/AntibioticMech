# Ceftobiprole: active drug conflated with its medocaril prodrug in exact synonyms

- Review: 20261021T122234Z-ceftobiprole
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:02:19Z
- Finished UTC: 2026-10-21T12:22:34Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One major source-owned synonym conflation: ceftobiprole medocaril is a distinct covalent prodrug, and Zeftera/Zevtera identify prodrug products rather than exact active-drug structures. The native ceftobiprole graph, stereochemistry, formula, charge, masses and checked exact cross-references agree. The native PBP family edge is honestly qualified as database evidence. Primary PBP2a acylation and strain-dependent resistance evidence offers bounded optional enrichment, not a reason to invent missing mandatory fields.

## Scope And Provenance

Whole-record review of the exact ceftobiprole active-drug structure.

Selection: Queue 262 in isolated batch 027; original captures preserved, actual ARO inventories appended, and the discovered target-role map captured before its inspection.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:140407 | data/antibiotics/antibacterial/ceftobiprole.yaml | generated | ceftobiprole |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | CHEBI:140407 | Actual command exited 0. Schema/strict and supplemental molecular checks pass; synonym equivalence requires the independent source assessment. |
| Focused strict | passed | True | CHEBI:140407 | Actual command exited 0. Schema/strict and supplemental molecular checks pass; synonym equivalence requires the independent source assessment. |
| Focused chemistry | passed | False | CHEBI:140407 | Actual command exited 0. Schema/strict and supplemental molecular checks pass; synonym equivalence requires the independent source assessment. |
| Focused xref-comparison | passed | False | CHEBI:140407 | Actual command exited 0. Schema/strict and supplemental molecular checks pass; synonym equivalence requires the independent source assessment. |
| Authoritative full QC | failed | True | CHEBI:140407 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:140407 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:140407 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:140407 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:140407 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:140407 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:140407 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:140407 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:140407 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact active-drug structure

identity: supported. Targets: CHEBI:140407.

Native 6R,7R,3'R/Z/E graph, full InChIKey, formula, neutral charge, masses and source mints agree independently. No native structure replacement is indicated.

### Active drug versus covalent prodrug and product names

identity: concern. Targets: CHEBI:140407.

Three ARO aliases were emitted as exact synonyms. Medocaril is a distinct covalent molecule; Zeftera and Zevtera are product names with prodrug material scope. Their relationship to the active moiety is real but not exact molecular identity.

### Cephalosporin/thiadiazole parents and antibacterial role

grounding: supported. Targets: CHEBI:140407.

Native chemical class and parents fit the graph. Original antibacterial observations support the filing and antimicrobial role; population percentages remain assay-specific.

### Exact and typed drug mappings

grounding: supported. Targets: CHEBI:140407.

Checked PubChem, CAS, ChEMBL and KEGG identities agree completely. The valid active-drug xrefs should be preserved; Reaxys remains a proprietary-access limitation.

### Database family assertion and primary PBP2a evidence

evidence: supported. Targets: CHEBI:140407.

The native PBP edge correctly discloses database origin and unspecified assay. Additional original PBP2a acylation supports a separately scoped primary target item; resistant PBP2a is not automatically equated to the existing beta-lactam-sensitive family grounding.

### Causal genetic results versus clinical associations

completeness: supported. Targets: CHEBI:140407.

2015 curing/transfer experiments support a strain-dependent mecA E447K contribution. Other mutations and the African ST241 triple mutation require their association/causality boundaries. Absence of native resistance entries is an optional enrichment opportunity.

### Strain, assay and administered-material boundaries

evidence: supported. Targets: CHEBI:140407.

MIC, passage-growth concentration, animal killing, CSF exposure and thermal stability are distinct endpoints. Rabbit preparation terminology is unresolved, and abstract-only surveillance lacks full reagent specification. No quantitative native claim needs correction.

### All adopted publication leads

evidence: supported. Targets: CHEBI:140407.

All eight adopted PMIDs and the adopted PMC conference abstract were individually inspected and disposed. Three review papers remain secondary; primary abstract-only studies are not represented as fully verified methods.

### Structured query before open protein research

scope: supported. Targets: CHEBI:140407.

Covered S. aureus dataset query completed; zero iModulon hits supplies no negative biological evidence. Gene hits do not ground the recombinant experimental protein or study strains.

### Unpopulated optional domains and historical definition

scope: not_applicable. Targets: CHEBI:140407.

No native producer, clinical approval, causal graph, dataset or discussion assertion requires adjudication. The definition describes historical pneumonia development and is not read as a complete present-day indication list.

### Actual source ownership and preserved captures

provenance: supported. Targets: CHEBI:140407.

Original and expanded input captures remain unchanged; actual ARO inventories and later-discovered target-role map are separately captured. Five seed/reseed history events and SEEDED status remain intact.

### Focused actual validation

schema: supported. Targets: CHEBI:140407.

Schema, strict and complete structural comparisons pass. The exact-synonym conflation is a scientific defect those validators do not detect.

## Findings

### F1: Exact synonyms conflate the active drug with its covalent prodrug and branded products

major / open / confirmed; issue key: chebi-140407-ceftobiprole-medocaril-exact-synonyms.

synonyms[4] asserts Ceftobiprole medocaril as EXACT_SYNONYM of C20H22N8O6S2 ceftobiprole. Current independent structures and the original conversion scheme show an added covalent N-carbamate promoiety in medocaril (C26H26N8O11S2); administered sodium material is another distinct form. synonyms[5] and synonyms[6] likewise emit Zeftera/Zevtera product names as exact molecular synonyms, although official product documents identify medocaril/prodrug formulations. Preserve the active-drug graph and valid xrefs, remove or explicitly qualify the prodrug relationship, and use appropriate product/brand semantics for retained trade names through source-owned curation.

## Recommended Actions And Acceptance Checks

### A1

Correct source-owned exact synonym semantics for medocaril and the two products.

- Keep CHEBI:140407 and VOAZJEPQLGBXGO-SDAWRPRTSA-N with existing valid exact xrefs.
- Remove the medocaril exact synonym or express it as an explicitly related prodrug name where supported; do not silently replace the native structure with medocaril or sodium medocaril.
- Retain Zeftera/Zevtera only with appropriate BRAND_NAME or other supported product-context semantics and clear prodrug material scope.
- Ensure the correction survives extraction/reseeding through maintained source adjudication, then run schema/strict and applicable reference/history/corpus checks after separately authorized curation.

### A2

Optionally add primary PBP2a, activity and resistance annotations with exact endpoint and material scope.

- Keep CARD family provenance distinct from original recombinant PBP2a Ser403 acylation evidence; identify the actual protein/taxon and preserve the Y23M truncation context.
- Do not convert thermal shifts, endpoint crystal structures or proposed Michaelis-complex interactions into measured Kd, kinetic rates or observed causal steps.
- For 2015 resistance, preserve COL/SF8300 backgrounds, plasmid transfer/curing, ceftaroline-selection versus ceftobiprole readout, and the absence of whole-genome sequencing.
- Keep clinical ST241 mutation associations distinct from individual-mutation causal evidence and retain study-specific historical susceptibility interpretation.
- Resolve full assay/reagent context before importing abstract-only numerical observations; preserve rabbit medocaril/ceftobiprole terminology uncertainty and active-moiety dose equivalents.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/ceftobiprole.yaml; Entire YAML | supports | Read identifier, label, filing/status/grounding, definition, seven synonyms, three parents, role and structural class, complete structure/masses, five exact xrefs and one drug xref, two source concepts, the qualified target edge and all five history events. |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv; conf/aro_target_roles.tsv; ChEBI row 2601; ARO molecule row 46; target row 47; ARO:3000749 role-map row | supports | ChEBI supplies the active-drug structure and eight publication leads (seven PMIDs plus PMC5631058). ARO supplies the medocaril/product aliases, PMID22064544 and the PBP edge. The target-role map explicitly classifies the edge as protein/direct binding. No matched ceftobiprole resistance edge was found in an ignored-inclusive search of the actual inventory. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Identity and equivalence; source ownership; experimental evidence | supports | Exact names must agree with the individual chemical graph. Source-owned corrections need a persistent extraction/adjudication path. Optional unpopulated activity, resistance or graph fields are not mandatory schema defects. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:140407; Definition, structure, Names and outgoing ontology relations | supports | Current ChEBI matches the native active-drug graph, formula, masses and cephalosporin/thiadiazole parents. ChEBI exact systematic names preserve 6R,7R,3'R and oxime Z/side-chain E geometry; the problematic prodrug/product aliases come from ARO. Historical pneumonia-development wording is not treated as a current regulatory assertion. |
| aro | https://card.mcmaster.ca/aro/0000061; Synonyms, active-drug SMILES/xrefs, target relation and publication | partial | Current CARD repeats Ceftobiprole medocaril, Zeftera and Zevtera aliases while displaying the active-drug structure and crosswalks. Its family target is database provenance; its cited rabbit paper does not itself measure PBP binding. Broad statements in the source are not silently promoted into native quantitative evidence. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/135413542/property/InChI,InChIKey,MolecularFormula,SMILES,IUPACName/JSON; Complete CID 135413542 identity | supports | Current PubChem independently agrees on VOAZJEPQLGBXGO-SDAWRPRTSA-N, C20H22N8O6S2 and complete isomeric SMILES/systematic name. CAS 209467-52-7 resolves to this same CID in the separate captured PUG response. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL520642.json; molecule_structures and molecular formula | supports | Full ChEMBL molecular graph independently generates the native complete InChIKey; drug associations do not alter that exact molecular identity. |
| kegg | https://rest.kegg.jp/get/D08885; Name, formula, molecular structure and related drug comment | supports | D08885 denotes ceftobiprole and its molfile generates the native complete key. It explicitly refers separately to ceftobiprole medocaril D08886. The latter current entry is the sodium prodrug/product context. |
| medocaril | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/ceftobiprole%20medocaril/property/InChI,InChIKey,MolecularFormula,SMILES,IUPACName/JSON; CID 135413544 complete molecular identity | supports | Ceftobiprole medocaril is C26H26N8O11S2, HFTSMHTWUFCYMJ-YIOMYIDASA-N, with an additional covalent N-carbamate promoiety on the pyrrolidine. It cannot be an exact synonym of the native C20 active drug. This unsalted prodrug is also distinct from its administered sodium salt. |
| medocaril-sodium | https://rest.kegg.jp/get/D08886; Name, formula and product | supports | Current D08886 is ceftobiprole medocaril sodium, formula C26H25N8O11S2.Na, and lists Zevtera as a trade name. It is not substituted for the valid native D08885 drug xref. |
| zeftera | https://www.ema.europa.eu/en/medicines/human/EPAR/zeftera; Product details and historical application identity | supports | The official historical EMA page names Zeftera (previously Zevtera) and its active substance ceftobiprole medocaril. This supports product-name qualification only; the historical refusal is not extrapolated to current worldwide approval status. |
| zevtera | https://www.medicines.org.uk/emc/product/9164/smpc; SmPC sections 1, 2 and 5.2; updated 23 September 2025 | supports | The product contains 666.6 mg ceftobiprole medocaril sodium per vial, expressed as 500 mg ceftobiprole equivalents. Section 5.2 explicitly distinguishes the prodrug from active ceftobiprole. These are product/active-moiety relationships, not exact molecular synonyms. |
| chemistry | RDKit 2026.03.5 supplemental native comparison; 262-chemistry.json | supports | Both native SMILES and InChI parse and generate the retained complete key, one component, neutral formal charge and three assigned R centers. Formula and average/exact masses agree to native precision; both source mints reproduce. |
| xref-comparison | Independent complete structure comparison; 262-external-chemistry.json; compare-262.py | supports | KEGG molfile, ChEMBL SMILES, PubChem CID and CAS-resolved SMILES each independently generate VOAZJEPQLGBXGO-SDAWRPRTSA-N and C20H22N8O6S2. Proprietary Reaxys content was not independently inspected. |
| adapter | Installed kg-microbe-sources imodulondb adapter; 262-adapter-results.json; s_aureus/staph_precise165 | context_only | Before open protein research, the covered-dataset search for penicillin-binding protein completed with three gene hits and zero iModulons. Dataset selection reused the immediately preceding successful same-session dataset listing. Gene hits are context only; no module existed to summarize and no experimental target strain is inferred from USA300HOU annotations. |
| adopted-25753637 | PMID:25753637; DOI 10.1128/AAC.05004-14; PMC4394828 full text, Tables 1-6 and Fig. 1 | partial | Original 2015 study combines broth-dilution MICs, ceftaroline/ceftobiprole passage, mecA sequencing, plasmid curing and transfer in S. aureus COL and SF8300 backgrounds. Table 5 gives ceftobiprole MIC 0.5 microgram/mL for COLnex(pYK20) and 64 for COLnex carrying the SF8300 E447K mecA plasmid. Effects depend on background; no whole-genome sequencing was performed. Pbp2/Pbp4/GdpP changes in the ceftaroline-passaged COL mutant are associated changes, not individually proven causal determinants here. Exact ceftobiprole salt/hydration is not specified. |
| adopted-22064544 | PMID:22064544; DOI 10.1128/AAC.01537-10; PMC3264204 full text, Methods and Tables 1-3 | partial | Original rabbit meningitis study: Johnson &amp; Johnson ceftobiprole, CLSI broth dilution; E. coli QK-9 MIC 0.25 mg/L, K. pneumoniae 1173687 1 mg/L and two unnamed H. influenzae strains 0.5 mg/L. Rabbit IV dose was reported as 40 mg/kg; the abstract calls the drug medocaril while Methods says ceftobiprole, without resolving salt/prodrug preparation. Therefore retain the named active-drug activity with this material caveat and do not transfer dose as exact free-acid mass. Animal killing/CSF exposure is not a direct PBP assay or human meningitis efficacy proof. |
| adopted-26316697 | PMID:26316697; DOI 10.2147/DDDT.S56616; PMC4547641 pharmacology and pneumonia-trial review sections | context_only | Secondary 2015 review explicitly distinguishes medocaril prodrug from ceftobiprole and summarizes CAP/HAP development. Those sections were inspected; cited trial rates and target claims remain secondary leads rather than new original observations. Historical approval/VAP statements are not current regulatory assertions. |
| adopted-26443816 | PMID:26443816; DOI 10.1093/jac/dkv325; Europe PMC core abstract | partial | Original observational study of 60 African MRSA isolates used broth microdilution and mecA sequencing. Nine were classified ceftobiprole resistant under the study criteria; ST241 and N146K/N204K/G246E were associated with resistance. Abstract inspection does not establish individual mutation causality or precise reagent form; publisher PDF/HTML access returned 403. |
| adopted-28264613 | PMID:28264613; DOI 10.1080/17425255.2017.1303481; Europe PMC core abstract | context_only | Pharmacokinetic drug evaluation review summarizes spectrum, PK/PD and clinical studies, including VAP limitations. Evaluated at abstract depth; not an original binding or resistance experiment. |
| adopted-29017833 | PMID:29017833; DOI 10.1016/j.jaip.2017.08.027; Europe PMC core abstract | context_only | Beta-lactam allergy cross-reactivity review, evaluated at abstract depth. It does not establish ceftobiprole antibacterial mechanism or species-specific activity and is not converted into a native allergy claim. |
| adopted-29395713 | PMID:29395713; DOI 10.1016/j.diagmicrobio.2017.12.020; Europe PMC abstract and publisher abstract/highlights | partial | Original surveillance of 12,240 European isolates from 2015. Study-specific susceptibility percentages and MIC distributions support antibacterial scope; they are not universal species susceptibility. Only abstract/highlight depth reached after DOI retrieval certificate failure and web DOI access failure; material specification and full table context remain unresolved. |
| adopted-29452992 | PMID:29452992; DOI 10.1016/j.diagmicrobio.2018.01.010; Europe PMC core abstract | partial | Original study tested 196 staphylococcal isolates from musculoskeletal foreign-body infections by test strip and broth microdilution. This is isolate susceptibility testing, not direct evidence of biofilm penetration, biofilm eradication or successful implant-infection treatment. Exact reagent form unresolved at abstract depth; DOI retrieval failed. |
| adopted-PMC5631058 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5631058/fullTextXML; Complete 2017 conference abstract, Background/Methods/Results/Conclusion | partial | Abstract-only publication studied 2,787 US bloodstream isolates collected in 2016 by reference broth microdilution. It explicitly calls medocaril a prodrug; results distinguish E. faecalis activity from low E. faecium coverage. Limited methods/material detail and historical breakpoint language preclude precise assay transfer or whole-species resistance declarations. It is not a full original methods paper. |
| pbp-primary | PMID:22815485; DOI 10.1074/jbc.M112.355644; PMC3442540 full text, Experimental Procedures, Tables 1-2 and Figs.1-3 | partial | Original PBP2a structure uses Basilea ceftobiprole dissolved in DMSO/0.2% TFA, recombinant S. aureus residues 23-668 with Y23M expressed in E. coli, and overnight crystal derivatization. The 2.9-angstrom structure PDB 4DKI shows covalent acylation at Ser403. Differential scanning calorimetry gives a 1.7 degree C thermal shift, not a Kd or MIC. The authors explicitly state that only the acylation endpoint is observed; proposed Michaelis-complex details and broad susceptibility discussion should not be upgraded to directly observed steps. Solid salt/hydration and source strain are not established. |
| pbp-figures | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/56c0/3442540/604106706f3f/zbc0391222680001.jpg; Original Fig. 1; also Figs.2-3 inspected and hashed in 262-final-fetch-results.json | supports | Visual inspection confirms the active-drug structural drawing lacks the medocaril promoiety and depicts the modeled acyl-enzyme/electron density. Fig. 2 illustrates bound-state rearrangement; Fig. 3 is thermal calorimetry, not an affinity or bacterial growth curve. |
| resistance-figure | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/7a9b/4394828/403ad6902e02/zac0051539600001.jpg; Original PMC4394828 Fig. 1 | supports | Visual inspection confirms the plot shows the highest ceftobiprole or ceftaroline passage concentration supporting growth per passage day. These concentrations are not the separately determined final MIC values in Tables 3, 5 and 6. |
| prodrug-primary | PMID:15215110; DOI 10.1128/AAC.48.7.2570-2575.2004; PMC434165 Introduction, Methods and Fig. 1 | supports | Original healthy-volunteer study explicitly distinguishes administered BAL5788 sodium prodrug from active BAL9141. Analytical LC-MS/MS measures distinct analytes at precursor m/z 691 and 535; doses are expressed as active-drug equivalents. These inspected identity/analytical sections support the chemical distinction, not direct antibacterial activity of the administered prodrug or an intrinsic target of medocaril. |
| prodrug-figure | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/0c41/434165/e6db824ab9fa/zac0070441540001.jpg; Original Fig. 1, visually inspected | supports | BAL5788/001 is explicitly drawn with sodium carboxylate and covalent pyrrolidine N-carbamate promoiety. The conversion scheme yields BAL9141/000 acid with free pyrrolidine NH, plus cleavage products. This is an explicit structure-level distinction from the native active drug. |
| gates | Actual focused commands; 262-focused-results.json | supports | Schema and strict validation pass; supplemental native chemistry and independent full-xref comparison pass. These checks do not establish semantic equivalence of the source-provided synonym strings. |
| local-search | Ignored-inclusive record and source-owner search; 262-local-hits.txt; 262-owner-hits.txt | context_only | Exact name, identifier, full key and ARO identifier searched with hidden/ignored files included outside .git/.venv. Existing historical/source matches are contextual leads, not substitute primary evidence. No absence of optional fields is extrapolated to absence from all literature. |

## Limits And Additional Notes

- Five adopted PMIDs were evaluated at abstract depth; the two original adopted full articles and selected sections of the adopted pneumonia review were inspected. The adopted PMC5631058 publication is itself a conference abstract.
- Europe PMC XML returned 500 for three full primary papers; alternate public PMC HTML succeeded. OUP PDF/HTML returned 403; two Elsevier DOI retrievals had certificate failures and web DOI access failures, so those primary leads remain abstract-limited.
- Exact solid salt/hydration is not specified in the PBP2a and 2015 resistance papers. The rabbit paper inconsistently names medocaril in its abstract and ceftobiprole in Methods; no exact administered-form conclusion is made.
- Proprietary Reaxys content was not independently inspected. No exhaustive current regulatory or worldwide susceptibility review is claimed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 24 final input hashes rechecked unchanged; initial captures and earlier expanded captures preserved. No native/source/status/history changes.
- Native checks used the batch 027 environment; standalone RDKit 2026.03.5 used the existing batch 019 interpreter against batch 027 cwd.
- Only free public retrievals were used. Optional links, tags and notes were constructed for ceftobiprole and independently checked against this target.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T122234Z-ceftobiprole
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Ceftobiprole: active drug conflated with its medocaril prodrug in exact synonyms'
started_at: '2026-10-21T12:02:19Z'
finished_at: '2026-10-21T12:22:34Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Entire native record and actual ChEBI/ARO owners assessed independently;
    all eight adopted PMIDs and the adopted conference abstract inspected at declared
    depth; independent complete structure comparisons; original PBP2a crystallography
    and resistance full texts with figures; original prodrug scheme and analytical
    methods; official product identity documents.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'One major source-owned synonym conflation: ceftobiprole medocaril is a distinct
  covalent prodrug, and Zeftera/Zevtera identify prodrug products rather than exact
  active-drug structures. The native ceftobiprole graph, stereochemistry, formula,
  charge, masses and checked exact cross-references agree. The native PBP family edge
  is honestly qualified as database evidence. Primary PBP2a acylation and strain-dependent
  resistance evidence offers bounded optional enrichment, not a reason to invent missing
  mandatory fields.'
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
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
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
  - path: data/antibiotics/antibacterial/ceftobiprole.yaml
    sha256: 3e4e3cccfe2ee81ad19dbd23704f7e2f0acf5535fe921ad45a8a8de155815e3f
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 25f0d80c0bf26da7741a1514a5e1759dde484ab054f0f56df7938bdda8383a91
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
- target_id: CHEBI:140407
  path: data/antibiotics/antibacterial/ceftobiprole.yaml
  label: ceftobiprole
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
    role: Adopted CARD identity, bibliography, classification and crosswalks
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Adopted CARD target edge
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Bounded resistance-owner check
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Imported target type and direct-binding relation classification
scope:
  description: Whole-record review of the exact ceftobiprole active-drug structure.
  selection: Queue 262 in isolated batch 027; original captures preserved, actual
    ARO inventories appended, and the discovered target-role map captured before its
    inspection.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:140407
  exclusions:
  - target: Ceftobiprole medocaril, its sodium salt, branded formulations and comparator
      ceftaroline as exact identities
    reason: Covalent prodrug, salt, product and comparator boundaries are retained;
      active-moiety dose equivalents are not exact-form masses.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual command exited 0. Schema/strict and supplemental molecular checks
    pass; synonym equivalence requires the independent source assessment.
  target_ids:
  - CHEBI:140407
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/ceftobiprole.yaml (cwd /private/tmp/antibioticmech-record-reviews-027)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: strict
  name: Focused strict
  status: passed
  required: true
  summary: Actual command exited 0. Schema/strict and supplemental molecular checks
    pass; synonym equivalence requires the independent source assessment.
  target_ids:
  - CHEBI:140407
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/ceftobiprole.yaml --out /private/tmp/am-review-session/262-validation.tsv
    (cwd /private/tmp/antibioticmech-record-reviews-027)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Focused chemistry
  status: passed
  required: false
  summary: Actual command exited 0. Schema/strict and supplemental molecular checks
    pass; synonym equivalence requires the independent source assessment.
  target_ids:
  - CHEBI:140407
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/check199200.py
    262 (cwd /private/tmp/antibioticmech-record-reviews-027)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: xref-comparison
  name: Focused xref-comparison
  status: passed
  required: false
  summary: Actual command exited 0. Schema/strict and supplemental molecular checks
    pass; synonym equivalence requires the independent source assessment.
  target_ids:
  - CHEBI:140407
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/compare-262.py
    (cwd /private/tmp/antibioticmech-record-reviews-027)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - xref-comparison
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:140407
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
  - CHEBI:140407
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
  - CHEBI:140407
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
  - CHEBI:140407
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
  - CHEBI:140407
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
  - CHEBI:140407
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
  - CHEBI:140407
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
  - CHEBI:140407
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
  - CHEBI:140407
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/ceftobiprole.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T12:15:45Z'
  support: supports
  summary: Read identifier, label, filing/status/grounding, definition, seven synonyms,
    three parents, role and structural class, complete structure/masses, five exact
    xrefs and one drug xref, two source concepts, the qualified target edge and all
    five history events.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv;
    conf/aro_target_roles.tsv
  locator: ChEBI row 2601; ARO molecule row 46; target row 47; ARO:3000749 role-map
    row
  accessed_at: '2026-10-21T12:15:45Z'
  support: supports
  summary: ChEBI supplies the active-drug structure and eight publication leads (seven
    PMIDs plus PMC5631058). ARO supplies the medocaril/product aliases, PMID22064544
    and the PBP edge. The target-role map explicitly classifies the edge as protein/direct
    binding. No matched ceftobiprole resistance edge was found in an ignored-inclusive
    search of the actual inventory.
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Identity and equivalence; source ownership; experimental evidence
  accessed_at: '2026-10-21T12:15:45Z'
  support: supports
  summary: Exact names must agree with the individual chemical graph. Source-owned
    corrections need a persistent extraction/adjudication path. Optional unpopulated
    activity, resistance or graph fields are not mandatory schema defects.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:140407
  locator: Definition, structure, Names and outgoing ontology relations
  accessed_at: '2026-10-21T12:10:03.502549Z'
  support: supports
  summary: Current ChEBI matches the native active-drug graph, formula, masses and
    cephalosporin/thiadiazole parents. ChEBI exact systematic names preserve 6R,7R,3'R
    and oxime Z/side-chain E geometry; the problematic prodrug/product aliases come
    from ARO. Historical pneumonia-development wording is not treated as a current
    regulatory assertion.
  snapshot_sha256: 413c5ba42cf0fbfe4017b683202e0ec1f0b47477b7ae5985e66109f59bd4e80a
- evidence_id: aro
  kind: authority
  reference: https://card.mcmaster.ca/aro/0000061
  locator: Synonyms, active-drug SMILES/xrefs, target relation and publication
  accessed_at: '2026-10-21T12:10:04.206975Z'
  support: partial
  summary: Current CARD repeats Ceftobiprole medocaril, Zeftera and Zevtera aliases
    while displaying the active-drug structure and crosswalks. Its family target is
    database provenance; its cited rabbit paper does not itself measure PBP binding.
    Broad statements in the source are not silently promoted into native quantitative
    evidence.
  snapshot_sha256: b0f8aa5171764c788333facc86d9da36e5a83bdcaa44bc1198c373107db65604
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/135413542/property/InChI,InChIKey,MolecularFormula,SMILES,IUPACName/JSON
  locator: Complete CID 135413542 identity
  accessed_at: '2026-10-21T12:10:03.503437Z'
  support: supports
  summary: Current PubChem independently agrees on VOAZJEPQLGBXGO-SDAWRPRTSA-N, C20H22N8O6S2
    and complete isomeric SMILES/systematic name. CAS 209467-52-7 resolves to this
    same CID in the separate captured PUG response.
  snapshot_sha256: 119d2e8d1c4200752b832e19378bd080d9db0e4f508565c5e0362cc0c38eb3b5
- evidence_id: chembl
  kind: authority
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL520642.json
  locator: molecule_structures and molecular formula
  accessed_at: '2026-10-21T12:10:03.503618Z'
  support: supports
  summary: Full ChEMBL molecular graph independently generates the native complete
    InChIKey; drug associations do not alter that exact molecular identity.
  snapshot_sha256: 99d617e14a9cd283de936ea005432f3fac82c5299e771319308dbb4ff2c48a5d
- evidence_id: kegg
  kind: authority
  reference: https://rest.kegg.jp/get/D08885
  locator: Name, formula, molecular structure and related drug comment
  accessed_at: '2026-10-21T12:10:03.503710Z'
  support: supports
  summary: D08885 denotes ceftobiprole and its molfile generates the native complete
    key. It explicitly refers separately to ceftobiprole medocaril D08886. The latter
    current entry is the sodium prodrug/product context.
  snapshot_sha256: ad73cbc5bd4573d7e424b8b602358e7fff27438690fb8a6c400048ddb10faeb6
- evidence_id: medocaril
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/ceftobiprole%20medocaril/property/InChI,InChIKey,MolecularFormula,SMILES,IUPACName/JSON
  locator: CID 135413544 complete molecular identity
  accessed_at: '2026-10-21T12:11:41.690694Z'
  support: supports
  summary: Ceftobiprole medocaril is C26H26N8O11S2, HFTSMHTWUFCYMJ-YIOMYIDASA-N, with
    an additional covalent N-carbamate promoiety on the pyrrolidine. It cannot be
    an exact synonym of the native C20 active drug. This unsalted prodrug is also
    distinct from its administered sodium salt.
  snapshot_sha256: a2822625a1d2edccfc11faf5c4074c03631a26bd4ca62ca3f0bd798b6fb91178
- evidence_id: medocaril-sodium
  kind: authority
  reference: https://rest.kegg.jp/get/D08886
  locator: Name, formula and product
  accessed_at: '2026-10-21T12:11:41.431327Z'
  support: supports
  summary: Current D08886 is ceftobiprole medocaril sodium, formula C26H25N8O11S2.Na,
    and lists Zevtera as a trade name. It is not substituted for the valid native
    D08885 drug xref.
  snapshot_sha256: e98339158903fc4643643bae02463f804192654d699d1f4a20c36d487dd90344
- evidence_id: zeftera
  kind: authority
  reference: https://www.ema.europa.eu/en/medicines/human/EPAR/zeftera
  locator: Product details and historical application identity
  accessed_at: '2026-10-21T12:12:35.846839Z'
  support: supports
  summary: The official historical EMA page names Zeftera (previously Zevtera) and
    its active substance ceftobiprole medocaril. This supports product-name qualification
    only; the historical refusal is not extrapolated to current worldwide approval
    status.
  snapshot_sha256: 1ada458670b1c856ab40a8c9239753846f78cd99800fecd1ebe8371ccf29b1cc
- evidence_id: zevtera
  kind: authority
  reference: https://www.medicines.org.uk/emc/product/9164/smpc
  locator: SmPC sections 1, 2 and 5.2; updated 23 September 2025
  accessed_at: '2026-10-21T12:12:35.846954Z'
  support: supports
  summary: The product contains 666.6 mg ceftobiprole medocaril sodium per vial, expressed
    as 500 mg ceftobiprole equivalents. Section 5.2 explicitly distinguishes the prodrug
    from active ceftobiprole. These are product/active-moiety relationships, not exact
    molecular synonyms.
  snapshot_sha256: 90673d888797100ba66b5492ad0b2a4d2d07316f82136f769ebea98787e07656
- evidence_id: chemistry
  kind: validation
  reference: RDKit 2026.03.5 supplemental native comparison
  locator: 262-chemistry.json
  accessed_at: '2026-10-21T12:10:04Z'
  support: supports
  summary: Both native SMILES and InChI parse and generate the retained complete key,
    one component, neutral formal charge and three assigned R centers. Formula and
    average/exact masses agree to native precision; both source mints reproduce.
  snapshot_sha256: fb4231d69a63b9d9055ddc07b11048af5c6d46e4ec176ec906ab0c751efc88c7
- evidence_id: xref-comparison
  kind: validation
  reference: Independent complete structure comparison
  locator: 262-external-chemistry.json; compare-262.py
  accessed_at: '2026-10-21T12:11:36Z'
  support: supports
  summary: KEGG molfile, ChEMBL SMILES, PubChem CID and CAS-resolved SMILES each independently
    generate VOAZJEPQLGBXGO-SDAWRPRTSA-N and C20H22N8O6S2. Proprietary Reaxys content
    was not independently inspected.
  snapshot_sha256: efe769af6943c6b078b5ef02f071291012f63a66cfbd9aff5da7b1d1a3d78753
- evidence_id: adapter
  kind: search
  reference: Installed kg-microbe-sources imodulondb adapter
  locator: 262-adapter-results.json; s_aureus/staph_precise165
  accessed_at: '2026-10-21T12:09:51Z'
  support: context_only
  summary: Before open protein research, the covered-dataset search for penicillin-binding
    protein completed with three gene hits and zero iModulons. Dataset selection reused
    the immediately preceding successful same-session dataset listing. Gene hits are
    context only; no module existed to summarize and no experimental target strain
    is inferred from USA300HOU annotations.
  snapshot_sha256: f774def6764cf645efa9d42d427f43427fab1d33fb968462834973d5ca96a991
  search_scope: 2026-10-21; batch 027 rg --no-ignore --hidden outside .git/.venv;
    structured adapter before protein web follow-up; official identities, eight adopted
    PMID abstracts and conference abstract, selected full primary articles and original
    figures.
- evidence_id: adopted-25753637
  kind: primary_source
  reference: PMID:25753637
  locator: DOI 10.1128/AAC.05004-14; PMC4394828 full text, Tables 1-6 and Fig. 1
  accessed_at: '2026-10-21T12:11:59.531083Z'
  support: partial
  summary: Original 2015 study combines broth-dilution MICs, ceftaroline/ceftobiprole
    passage, mecA sequencing, plasmid curing and transfer in S. aureus COL and SF8300
    backgrounds. Table 5 gives ceftobiprole MIC 0.5 microgram/mL for COLnex(pYK20)
    and 64 for COLnex carrying the SF8300 E447K mecA plasmid. Effects depend on background;
    no whole-genome sequencing was performed. Pbp2/Pbp4/GdpP changes in the ceftaroline-passaged
    COL mutant are associated changes, not individually proven causal determinants
    here. Exact ceftobiprole salt/hydration is not specified.
  snapshot_sha256: bf1bd2a63a2ccbd6cd715c45d598789417277d783d1b5bae25666c02819aa8bc
- evidence_id: adopted-22064544
  kind: primary_source
  reference: PMID:22064544
  locator: DOI 10.1128/AAC.01537-10; PMC3264204 full text, Methods and Tables 1-3
  accessed_at: '2026-10-21T12:11:59.531216Z'
  support: partial
  summary: 'Original rabbit meningitis study: Johnson & Johnson ceftobiprole, CLSI
    broth dilution; E. coli QK-9 MIC 0.25 mg/L, K. pneumoniae 1173687 1 mg/L and two
    unnamed H. influenzae strains 0.5 mg/L. Rabbit IV dose was reported as 40 mg/kg;
    the abstract calls the drug medocaril while Methods says ceftobiprole, without
    resolving salt/prodrug preparation. Therefore retain the named active-drug activity
    with this material caveat and do not transfer dose as exact free-acid mass. Animal
    killing/CSF exposure is not a direct PBP assay or human meningitis efficacy proof.'
  snapshot_sha256: be78c05fe36b4f52550304175e86a576e7542b474f7a32c4af67ff2d7c3fe670
- evidence_id: adopted-26316697
  kind: authority
  reference: PMID:26316697
  locator: DOI 10.2147/DDDT.S56616; PMC4547641 pharmacology and pneumonia-trial review
    sections
  accessed_at: '2026-10-21T12:11:40.755993Z'
  support: context_only
  summary: Secondary 2015 review explicitly distinguishes medocaril prodrug from ceftobiprole
    and summarizes CAP/HAP development. Those sections were inspected; cited trial
    rates and target claims remain secondary leads rather than new original observations.
    Historical approval/VAP statements are not current regulatory assertions.
  snapshot_sha256: 9fad7b39881982c981bf4f7d262c162f2cc2fff5a0cf94ca7cd41d0d53482ad0
- evidence_id: adopted-26443816
  kind: primary_source
  reference: PMID:26443816
  locator: DOI 10.1093/jac/dkv325; Europe PMC core abstract
  accessed_at: '2026-10-21T12:10:04.712055Z'
  support: partial
  summary: Original observational study of 60 African MRSA isolates used broth microdilution
    and mecA sequencing. Nine were classified ceftobiprole resistant under the study
    criteria; ST241 and N146K/N204K/G246E were associated with resistance. Abstract
    inspection does not establish individual mutation causality or precise reagent
    form; publisher PDF/HTML access returned 403.
  snapshot_sha256: 24f85f0fc7f13ea937b1a061eebdbf36bbe042ebf2a62439f563a5caefe82ebd
- evidence_id: adopted-28264613
  kind: authority
  reference: PMID:28264613
  locator: DOI 10.1080/17425255.2017.1303481; Europe PMC core abstract
  accessed_at: '2026-10-21T12:10:04.712055Z'
  support: context_only
  summary: Pharmacokinetic drug evaluation review summarizes spectrum, PK/PD and clinical
    studies, including VAP limitations. Evaluated at abstract depth; not an original
    binding or resistance experiment.
  snapshot_sha256: 24f85f0fc7f13ea937b1a061eebdbf36bbe042ebf2a62439f563a5caefe82ebd
- evidence_id: adopted-29017833
  kind: authority
  reference: PMID:29017833
  locator: DOI 10.1016/j.jaip.2017.08.027; Europe PMC core abstract
  accessed_at: '2026-10-21T12:10:04.712055Z'
  support: context_only
  summary: Beta-lactam allergy cross-reactivity review, evaluated at abstract depth.
    It does not establish ceftobiprole antibacterial mechanism or species-specific
    activity and is not converted into a native allergy claim.
  snapshot_sha256: 24f85f0fc7f13ea937b1a061eebdbf36bbe042ebf2a62439f563a5caefe82ebd
- evidence_id: adopted-29395713
  kind: primary_source
  reference: PMID:29395713
  locator: DOI 10.1016/j.diagmicrobio.2017.12.020; Europe PMC abstract and publisher
    abstract/highlights
  accessed_at: '2026-10-21T12:10:04.712055Z'
  support: partial
  summary: Original surveillance of 12,240 European isolates from 2015. Study-specific
    susceptibility percentages and MIC distributions support antibacterial scope;
    they are not universal species susceptibility. Only abstract/highlight depth reached
    after DOI retrieval certificate failure and web DOI access failure; material specification
    and full table context remain unresolved.
  snapshot_sha256: 24f85f0fc7f13ea937b1a061eebdbf36bbe042ebf2a62439f563a5caefe82ebd
- evidence_id: adopted-29452992
  kind: primary_source
  reference: PMID:29452992
  locator: DOI 10.1016/j.diagmicrobio.2018.01.010; Europe PMC core abstract
  accessed_at: '2026-10-21T12:10:04.712055Z'
  support: partial
  summary: Original study tested 196 staphylococcal isolates from musculoskeletal
    foreign-body infections by test strip and broth microdilution. This is isolate
    susceptibility testing, not direct evidence of biofilm penetration, biofilm eradication
    or successful implant-infection treatment. Exact reagent form unresolved at abstract
    depth; DOI retrieval failed.
  snapshot_sha256: 24f85f0fc7f13ea937b1a061eebdbf36bbe042ebf2a62439f563a5caefe82ebd
- evidence_id: adopted-PMC5631058
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5631058/fullTextXML
  locator: Complete 2017 conference abstract, Background/Methods/Results/Conclusion
  accessed_at: '2026-10-21T12:10:04.309587Z'
  support: partial
  summary: Abstract-only publication studied 2,787 US bloodstream isolates collected
    in 2016 by reference broth microdilution. It explicitly calls medocaril a prodrug;
    results distinguish E. faecalis activity from low E. faecium coverage. Limited
    methods/material detail and historical breakpoint language preclude precise assay
    transfer or whole-species resistance declarations. It is not a full original methods
    paper.
  snapshot_sha256: 7ba291deb114f5e17fa9bf6e00e135e9f36a8abd89e6ae654f91b7c7ce13d3f1
- evidence_id: pbp-primary
  kind: primary_source
  reference: PMID:22815485
  locator: DOI 10.1074/jbc.M112.355644; PMC3442540 full text, Experimental Procedures,
    Tables 1-2 and Figs.1-3
  accessed_at: '2026-10-21T12:11:59.530636Z'
  support: partial
  summary: Original PBP2a structure uses Basilea ceftobiprole dissolved in DMSO/0.2%
    TFA, recombinant S. aureus residues 23-668 with Y23M expressed in E. coli, and
    overnight crystal derivatization. The 2.9-angstrom structure PDB 4DKI shows covalent
    acylation at Ser403. Differential scanning calorimetry gives a 1.7 degree C thermal
    shift, not a Kd or MIC. The authors explicitly state that only the acylation endpoint
    is observed; proposed Michaelis-complex details and broad susceptibility discussion
    should not be upgraded to directly observed steps. Solid salt/hydration and source
    strain are not established.
  snapshot_sha256: 08365fa20d975afa144f4f28f7d44264c2b922a8174a02651a28235f538e5488
- evidence_id: pbp-figures
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/56c0/3442540/604106706f3f/zbc0391222680001.jpg
  locator: Original Fig. 1; also Figs.2-3 inspected and hashed in 262-final-fetch-results.json
  accessed_at: '2026-10-21T12:12:35.847043Z'
  support: supports
  summary: Visual inspection confirms the active-drug structural drawing lacks the
    medocaril promoiety and depicts the modeled acyl-enzyme/electron density. Fig.
    2 illustrates bound-state rearrangement; Fig. 3 is thermal calorimetry, not an
    affinity or bacterial growth curve.
  snapshot_sha256: 32ca49e9ddefab83b97ccfb97c7eb6512bdacc25a9e4f8f6fcbd3c964dc5abb7
- evidence_id: resistance-figure
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/7a9b/4394828/403ad6902e02/zac0051539600001.jpg
  locator: Original PMC4394828 Fig. 1
  accessed_at: '2026-10-21T12:12:36.300278Z'
  support: supports
  summary: Visual inspection confirms the plot shows the highest ceftobiprole or ceftaroline
    passage concentration supporting growth per passage day. These concentrations
    are not the separately determined final MIC values in Tables 3, 5 and 6.
  snapshot_sha256: 6ad469b1610747837b932197b7e02babf3d2d6f10014f126a8523a42ac589665
- evidence_id: prodrug-primary
  kind: primary_source
  reference: PMID:15215110
  locator: DOI 10.1128/AAC.48.7.2570-2575.2004; PMC434165 Introduction, Methods and
    Fig. 1
  accessed_at: '2026-10-21T12:12:35.846404Z'
  support: supports
  summary: Original healthy-volunteer study explicitly distinguishes administered
    BAL5788 sodium prodrug from active BAL9141. Analytical LC-MS/MS measures distinct
    analytes at precursor m/z 691 and 535; doses are expressed as active-drug equivalents.
    These inspected identity/analytical sections support the chemical distinction,
    not direct antibacterial activity of the administered prodrug or an intrinsic
    target of medocaril.
  snapshot_sha256: 14c22445f04e562b8fe150f1354ef9ee24351ba81171cc62d57594ee5baee0ee
- evidence_id: prodrug-figure
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/0c41/434165/e6db824ab9fa/zac0070441540001.jpg
  locator: Original Fig. 1, visually inspected
  accessed_at: '2026-10-21T12:13:05.249827Z'
  support: supports
  summary: BAL5788/001 is explicitly drawn with sodium carboxylate and covalent pyrrolidine
    N-carbamate promoiety. The conversion scheme yields BAL9141/000 acid with free
    pyrrolidine NH, plus cleavage products. This is an explicit structure-level distinction
    from the native active drug.
  snapshot_sha256: 8df85a7b4eef199b7bac9cdaddb91d568c9d86f03443fa30b975f070c34691e7
- evidence_id: gates
  kind: validation
  reference: Actual focused commands
  locator: 262-focused-results.json
  accessed_at: '2026-10-21T12:10:04Z'
  support: supports
  summary: Schema and strict validation pass; supplemental native chemistry and independent
    full-xref comparison pass. These checks do not establish semantic equivalence
    of the source-provided synonym strings.
  snapshot_sha256: 9459b08598f0ce0e371c0c3a99783c7da5bd5365951b704fa86ac3465de1b5ff
- evidence_id: local-search
  kind: search
  reference: Ignored-inclusive record and source-owner search
  locator: 262-local-hits.txt; 262-owner-hits.txt
  accessed_at: '2026-10-21T12:09:50Z'
  support: context_only
  summary: Exact name, identifier, full key and ARO identifier searched with hidden/ignored
    files included outside .git/.venv. Existing historical/source matches are contextual
    leads, not substitute primary evidence. No absence of optional fields is extrapolated
    to absence from all literature.
  snapshot_sha256: ccc826a34b0a326beb186fe11ea3f661c7e87fec065f3bb09736b8b5c641d283
  search_scope: 2026-10-21; batch 027 rg --no-ignore --hidden outside .git/.venv;
    structured adapter before protein web follow-up; official identities, eight adopted
    PMID abstracts and conference abstract, selected full primary articles and original
    figures.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact active-drug structure
  outcome: supported
  summary: Native 6R,7R,3'R/Z/E graph, full InChIKey, formula, neutral charge, masses
    and source mints agree independently. No native structure replacement is indicated.
  target_ids:
  - CHEBI:140407
  evidence_ids:
  - native
  - chemistry
  - xref-comparison
- assessment_id: synonyms
  area: identity
  topic: Active drug versus covalent prodrug and product names
  outcome: concern
  summary: Three ARO aliases were emitted as exact synonyms. Medocaril is a distinct
    covalent molecule; Zeftera and Zevtera are product names with prodrug material
    scope. Their relationship to the active moiety is real but not exact molecular
    identity.
  target_ids:
  - CHEBI:140407
  evidence_ids:
  - aro
  - medocaril
  - medocaril-sodium
  - zeftera
  - zevtera
  - prodrug-figure
- assessment_id: classification
  area: grounding
  topic: Cephalosporin/thiadiazole parents and antibacterial role
  outcome: supported
  summary: Native chemical class and parents fit the graph. Original antibacterial
    observations support the filing and antimicrobial role; population percentages
    remain assay-specific.
  target_ids:
  - CHEBI:140407
  evidence_ids:
  - chebi
  - native
  - adopted-25753637
  - adopted-22064544
  - adopted-29395713
- assessment_id: xref
  area: grounding
  topic: Exact and typed drug mappings
  outcome: supported
  summary: Checked PubChem, CAS, ChEMBL and KEGG identities agree completely. The
    valid active-drug xrefs should be preserved; Reaxys remains a proprietary-access
    limitation.
  target_ids:
  - CHEBI:140407
  evidence_ids:
  - pubchem
  - chembl
  - kegg
  - xref-comparison
- assessment_id: target
  area: evidence
  topic: Database family assertion and primary PBP2a evidence
  outcome: supported
  summary: The native PBP edge correctly discloses database origin and unspecified
    assay. Additional original PBP2a acylation supports a separately scoped primary
    target item; resistant PBP2a is not automatically equated to the existing beta-lactam-sensitive
    family grounding.
  target_ids:
  - CHEBI:140407
  evidence_ids:
  - native
  - owners
  - aro
  - pbp-primary
  - pbp-figures
- assessment_id: resistance
  area: completeness
  topic: Causal genetic results versus clinical associations
  outcome: supported
  summary: 2015 curing/transfer experiments support a strain-dependent mecA E447K
    contribution. Other mutations and the African ST241 triple mutation require their
    association/causality boundaries. Absence of native resistance entries is an optional
    enrichment opportunity.
  target_ids:
  - CHEBI:140407
  evidence_ids:
  - adopted-25753637
  - resistance-figure
  - adopted-26443816
- assessment_id: activity
  area: evidence
  topic: Strain, assay and administered-material boundaries
  outcome: supported
  summary: MIC, passage-growth concentration, animal killing, CSF exposure and thermal
    stability are distinct endpoints. Rabbit preparation terminology is unresolved,
    and abstract-only surveillance lacks full reagent specification. No quantitative
    native claim needs correction.
  target_ids:
  - CHEBI:140407
  evidence_ids:
  - adopted-22064544
  - adopted-25753637
  - adopted-29452992
  - adopted-PMC5631058
  - pbp-primary
- assessment_id: leads
  area: evidence
  topic: All adopted publication leads
  outcome: supported
  summary: All eight adopted PMIDs and the adopted PMC conference abstract were individually
    inspected and disposed. Three review papers remain secondary; primary abstract-only
    studies are not represented as fully verified methods.
  target_ids:
  - CHEBI:140407
  evidence_ids:
  - adopted-25753637
  - adopted-26316697
  - adopted-26443816
  - adopted-28264613
  - adopted-29017833
  - adopted-29395713
  - adopted-29452992
  - adopted-22064544
  - adopted-PMC5631058
- assessment_id: adapter
  area: scope
  topic: Structured query before open protein research
  outcome: supported
  summary: Covered S. aureus dataset query completed; zero iModulon hits supplies
    no negative biological evidence. Gene hits do not ground the recombinant experimental
    protein or study strains.
  target_ids:
  - CHEBI:140407
  evidence_ids:
  - adapter
- assessment_id: optional
  area: scope
  topic: Unpopulated optional domains and historical definition
  outcome: not_applicable
  summary: No native producer, clinical approval, causal graph, dataset or discussion
    assertion requires adjudication. The definition describes historical pneumonia
    development and is not read as a complete present-day indication list.
  target_ids:
  - CHEBI:140407
  evidence_ids:
  - native
  - chebi
  - adopted-26316697
- assessment_id: provenance
  area: provenance
  topic: Actual source ownership and preserved captures
  outcome: supported
  summary: Original and expanded input captures remain unchanged; actual ARO inventories
    and later-discovered target-role map are separately captured. Five seed/reseed
    history events and SEEDED status remain intact.
  target_ids:
  - CHEBI:140407
  evidence_ids:
  - native
  - owners
  - rubric
- assessment_id: validation
  area: schema
  topic: Focused actual validation
  outcome: supported
  summary: Schema, strict and complete structural comparisons pass. The exact-synonym
    conflation is a scientific defect those validators do not detect.
  target_ids:
  - CHEBI:140407
  evidence_ids:
  - gates
  - chemistry
  - xref-comparison
findings:
- finding_id: F1
  issue_key: chebi-140407-ceftobiprole-medocaril-exact-synonyms
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Exact synonyms conflate the active drug with its covalent prodrug and branded
    products
  description: synonyms[4] asserts Ceftobiprole medocaril as EXACT_SYNONYM of C20H22N8O6S2
    ceftobiprole. Current independent structures and the original conversion scheme
    show an added covalent N-carbamate promoiety in medocaril (C26H26N8O11S2); administered
    sodium material is another distinct form. synonyms[5] and synonyms[6] likewise
    emit Zeftera/Zevtera product names as exact molecular synonyms, although official
    product documents identify medocaril/prodrug formulations. Preserve the active-drug
    graph and valid xrefs, remove or explicitly qualify the prodrug relationship,
    and use appropriate product/brand semantics for retained trade names through source-owned
    curation.
  target_ids:
  - CHEBI:140407
  field_paths:
  - synonyms[4].synonym_text
  - synonyms[4].synonym_type
  - synonyms[5].synonym_type
  - synonyms[6].synonym_type
  evidence_ids:
  - native
  - owners
  - aro
  - medocaril
  - medocaril-sodium
  - zeftera
  - zevtera
  - prodrug-primary
  - prodrug-figure
  rule_id: native-review-checklist:Identity and Equivalence
  native_severity: major false exact molecular equivalence
  normalization_reason: The covalent prodrug has a different formula and full molecular
    graph and can wrongly merge structure-specific assays or administered masses.
    The primary native graph is coherent, so no wrong-structure blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Source-owned prodrug and product aliases
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: CARD/ARO synonym extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated synonym types and merged exact identity
actions:
- action_id: A1
  description: Correct source-owned exact synonym semantics for medocaril and the
    two products.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:140407
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Source-owned prodrug and product aliases
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: CARD/ARO synonym extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated synonym types and merged exact identity
  acceptance_checks:
  - Keep CHEBI:140407 and VOAZJEPQLGBXGO-SDAWRPRTSA-N with existing valid exact xrefs.
  - Remove the medocaril exact synonym or express it as an explicitly related prodrug
    name where supported; do not silently replace the native structure with medocaril
    or sodium medocaril.
  - Retain Zeftera/Zevtera only with appropriate BRAND_NAME or other supported product-context
    semantics and clear prodrug material scope.
  - Ensure the correction survives extraction/reseeding through maintained source
    adjudication, then run schema/strict and applicable reference/history/corpus checks
    after separately authorized curation.
- action_id: A2
  description: Optionally add primary PBP2a, activity and resistance annotations with
    exact endpoint and material scope.
  finding_ids: []
  target_ids:
  - CHEBI:140407
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/ceftobiprole.yaml
    role: Curator-owned molecular_targets, activity_spectrum and resistance_mechanisms
      via validated writer
  acceptance_checks:
  - Keep CARD family provenance distinct from original recombinant PBP2a Ser403 acylation
    evidence; identify the actual protein/taxon and preserve the Y23M truncation context.
  - Do not convert thermal shifts, endpoint crystal structures or proposed Michaelis-complex
    interactions into measured Kd, kinetic rates or observed causal steps.
  - For 2015 resistance, preserve COL/SF8300 backgrounds, plasmid transfer/curing,
    ceftaroline-selection versus ceftobiprole readout, and the absence of whole-genome
    sequencing.
  - Keep clinical ST241 mutation associations distinct from individual-mutation causal
    evidence and retain study-specific historical susceptibility interpretation.
  - Resolve full assay/reagent context before importing abstract-only numerical observations;
    preserve rabbit medocaril/ceftobiprole terminology uncertainty and active-moiety
    dose equivalents.
limitations:
- Five adopted PMIDs were evaluated at abstract depth; the two original adopted full
  articles and selected sections of the adopted pneumonia review were inspected. The
  adopted PMC5631058 publication is itself a conference abstract.
- Europe PMC XML returned 500 for three full primary papers; alternate public PMC
  HTML succeeded. OUP PDF/HTML returned 403; two Elsevier DOI retrievals had certificate
  failures and web DOI access failures, so those primary leads remain abstract-limited.
- Exact solid salt/hydration is not specified in the PBP2a and 2015 resistance papers.
  The rabbit paper inconsistently names medocaril in its abstract and ceftobiprole
  in Methods; no exact administered-form conclusion is made.
- Proprietary Reaxys content was not independently inspected. No exhaustive current
  regulatory or worldwide susceptibility review is claimed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 24 final input hashes rechecked unchanged; initial captures and earlier expanded
  captures preserved. No native/source/status/history changes.
- Native checks used the batch 027 environment; standalone RDKit 2026.03.5 used the
  existing batch 019 interpreter against batch 027 cwd.
- Only free public retrievals were used. Optional links, tags and notes were constructed
  for ceftobiprole and independently checked against this target.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:140407
- https://pmc.ncbi.nlm.nih.gov/articles/PMC3442540/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC4394828/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC434165/
tags:
- ceftobiprole
- prodrug-boundary
- exact-synonym
- PBP2a
- strain-specific-resistance
```
