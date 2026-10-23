# Cefiderocol: exact zwitterion, verified CDC observations and bounded primary mechanisms

- Review: 20261021T112825Z-cefiderocol
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T11:08:26Z
- Finished UTC: 2026-10-21T11:28:25Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

No confirmed native defect. The (6R,7R), Z-oxime zwitterion is structurally coherent, exact public cross-references agree, and all ten CDC MIC observations retain correct censoring, taxa, BioSamples and source-specific breakpoint footers. Primary studies support antibacterial and siderophore properties and offer optional PBP/transport enrichment. Their membrane competition, mutant, radiotracer, assay-medium and material scopes remain distinct from the CDC observations. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole-record review of exact cefiderocol, including all ten curated activity observations.

Selection: Queue 224 in isolated batch 023; original capture preserved and actual ARO and curator-owned activity/history owners appended before judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:140376 | data/antibiotics/antibacterial/cefiderocol.yaml | generated | cefiderocol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | CHEBI:140376 | Actual focused command passed with zero errors. |
| Focused strict | passed | True | CHEBI:140376 | Actual focused command passed with zero errors. |
| Molecular encodings and source mints | passed | True | CHEBI:140376 | Both encodings reproduce the complete key, formula, net-zero charge, masses and two R centres; both source mints agree. |
| Authoritative full QC | failed | True | CHEBI:140376 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:140376 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:140376 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:140376 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:140376 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:140376 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:140376 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:140376 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:140376 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact cefiderocol zwitterion

identity: supported. Targets: CHEBI:140376.

Native chemical encodings, explicit oxime stereochemistry, complete public structure mappings and patent drawing agree. Salt/hydrate drug materials retain distinct scope.

### Structural parents and antibacterial roles

grounding: supported. Targets: CHEBI:140376.

Cephalosporin and carboxylic-acid parentage fit the graph. Primary antibacterial studies and live isolate measurements support antibiotic/antibacterial eligibility; resistant isolates do not contradict the qualified class role.

### Siderophore and resistant-pathogen wording

evidence: supported. Targets: CHEBI:140376.

The described side chains match the exact graph. Iron chelation/uptake and tested resistant-organism activity support the bounded definition, which does not assert every strain is susceptible.

### Exact, drug and document references

grounding: unknown. Targets: CHEBI:140376.

Accessible exact registries and the patent agree. Drug pages have broader formulation scope; DrugBank detailed access and independent Reaxys registry verification remain limited. Wikipedia is document context only.

### All ten curated CDC observations

evidence: supported. Targets: CHEBI:140376.

Every numeric value, censoring symbol, R interpretation, organism, BioSample and versioned/nonversioned footer matches the live source. The native assay retains modal broth microdilution; no medium protocol is inferred from unrelated papers.

### Optional PBP and transport representation

evidence: supported. Targets: CHEBI:140376.

Direct membrane PBP competition, mutant/complementation and iron-dependent uptake experiments provide concrete optional enrichment. Each measured variable, strain and material must be retained; absent optional target/graph fields are not defects.

### Resistance-associated effects and stability

evidence: supported. Targets: CHEBI:140376.

Native records resistant isolate phenotypes without inferred molecular determinants. Transporter deletions, modest porin/efflux effects and relative enzyme stability are bounded primary leads. Combination poster data and genotype-grouped MICs are not single-gene causality.

### Animal, clinical, producer and graph boundaries

scope: not_applicable. Targets: CHEBI:140376.

Native has no clinical-status, natural-producer or causal-graph claims. Animal humanized exposure and conference PK/PD models remain separate from current approval, dosing or clinical efficacy recommendations.

### Every adopted source lead

evidence: supported. Targets: CHEBI:140376.

All eight unique PMID leads and three distinct PMC conference abstracts were inspected at the stated abstract/full-text level. Review, primary research, combination work and source-internal table conflict are distinguished.

### Source owners, mints and history

provenance: supported. Targets: CHEBI:140376.

Both source mints and four seed events are coherent; two later curated events account for the ten CDC observations and BioSample fields. Actual generated and curator-owned inputs are captured, and SEEDED is unchanged.

### Optional primary enrichment

completeness: supported. Targets: CHEBI:140376.

Inspected sources offer well-defined PBP/transport evidence and explicit quantitative assay limits. No optional omission or source access failure establishes a required native correction.

### Focused native validation

schema: supported. Targets: CHEBI:140376.

Schema/strict and molecular/mint checks passed; scientific assessment remains separate from those deterministic results.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optionally curate primary PBP, uptake and transporter evidence with experiment-specific scope.

- Use Table 5 and Supplement Method 3 of DOI10.1128/AAC.01454-17 for strain-specific membrane competition IC50s; distinguish [14C]benzylpenicillin from Bocillin FL and do not equate IC50 with MIC or Kd. PBP3 is not the exclusive interacting PBP.
- Keep P. aeruginosa piuA insertion/complementation and E. coli combined cirA/fiu deletion as transport contributions. Preserve single-gene controls, growth medium and parent strain; do not label every transporter a lethal molecular target.
- Separate 2016 radiolabeled cefiderocol accumulation, unlabeled chelation/MIC assays and catechol 3-methoxy analog controls. Iron availability, reporter assay and unresolved salt/hydrate details must remain explicit.
- Map protein identifiers against the actual experimentally used strains; reference-dataset genes are not substitute strain/protein evidence.
- Run schema/strict and applicable term/reference/evidence/history/graph/corpus gates after separately authorized curation.

### A2

Preserve source distinctions when expanding activity or corroborating remaining references.

- Keep each CDC isolate, exact censoring and source-specific breakpoint edition, including absent edition for 0033. Retain µg/mL-to-mg/L equivalence without adding unreported iron-depleted medium.
- Do not transfer animal PK/PD, combination inhibitor experiments or aggregate clinical-panel statistics into individual CDC observations. Resolve the conference2018 table inconsistency before reusing those numeric cells.
- Corroborate DrugBank DB14879 and Reaxys 21605074 detail through permissible source access when available; failure to retrieve does not warrant deletion.
- Preserve patent Example 12 hydrate analysis and the exact Formula 89 drawing if citing synthesis or assay data; each patent compound must be mapped before numeric transfer.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/cefiderocol.yaml; Entire YAML | supports | Read exact identity, complete structural definition, parents/roles/class, all ten activity_spectrum observations and their evidence, structure, exact/drug/document xrefs, both source concepts and six history events. No populated molecular_targets, mode_of_action, resistance, producer, clinical-status or causal-graph claims. |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; ChEBI row 2600; ARO row 333; native activity/history | supports | ChEBI owns graph, definition, roles and ten adopted citation leads; ARO adds PMID29960205 and class/identity. The curated CDC observations and BioSample history are owned by the native record. Maintained owner hashes were captured before assessment. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:140376; Current structure, definition and ontology | supports | Matches C30H34ClN7O10S2, full key DBPPRLRVDVJOCL-FQRUVTKNSA-N, (6R,7R) centres, Z oxime, net-zero zwitterion, cephalosporin and carboxylic-acid parents. Antibiotic/antibacterial roles are supported by primary activity. Additional current siderophore annotation is optional enrichment, not a missing-required-field defect. |
| aro | https://card.mcmaster.ca/aro/3004474; Current cefiderocol identity | supports | ARO resolves cefiderocol/S-649266 to the matching graph and cephalosporin class. Its broad antibacterial mechanism description is database context rather than a replacement for primary experiment scope. |
| chemistry | Independent RDKit 2026.03.5 checks; 224-chemistry.json | supports | Both encodings parse to one net-neutral fragment, native complete key, formula, 752.228 average/751.14971 exact mass and two R centres. The native SMILES explicitly specifies Z oxime; standard InChI mobile-hydrogen normalization lacks a separate oxime /b layer but reproduces the retained key. Both source mints are correct. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/77843966; Complete current PUG structure | supports | CID 77843966 matches the exact zwitterionic formula and full stereochemical key; it is not a sulfate/tosylate salt record. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL3989974.json; Complete current molecule | supports | CHEMBL3989974 matches native formula, full key, (6R,7R) and explicit Z-oxime canonical SMILES. |
| cas | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/1225208-94-5/property/InChIKey/JSON; CAS identifier lookup | supports | CAS 1225208-94-5 resolves to the same complete cefiderocol key. |
| chemspider | https://www.chemspider.com/Chemical-Structure.52084902.html; Current identity, formula and verified IUPAC name | supports | ChemSpider52084902 names the matching (6R,7R), Z-oxime structure with two specified centres and the correct formula/CAS. Its approximate average mass uses a different atomic-weight convention; exact mass agrees. Full downloadable structural identifiers were not exposed in inspected text. |
| reaxys | https://www.ebi.ac.uk/chebi/CHEBI:140376; Reaxys 21605074 mapping | partial | The current exact ChEBI entry retains this registry mapping; independent Reaxys contents were not freely inspected. No identity contradiction was established. |
| drugcentral | https://drugcentral.org/drugcard/5352; Drug-level identity | supports | Resolves cefiderocol with CAS 1225208-94-5 and the neutral zwitterion formula. The page also lists sulfate/tosylate preparations among synonyms; its drug-level scope does not make those salts exact xrefs or establish formulation identity for the native graph. |
| kegg | https://rest.kegg.jp/get/D11302; KEGG drug D11302 | supports | D11302 names cefiderocol with the native formula and cephalosporin class. Its link to a separate formulated salt entry is not transferred as exact zwitterion identity. |
| drugbank | https://go.drugbank.com/drugs/DB14879; Free direct access boundary | unknown | Direct DrugBank retrieval returned HTTP403. Current ChEBI retains DB14879 as a drug mapping; its independent detailed contents were not inspected. |
| patent | https://patents.google.com/patent/EP2341053A1/en; Cephalosporin having catechol group; Example 12, paragraph 0193 | supports | The patent is relevant. Visually inspected Formula 89/Compound (I-12) has the matching aminothiazole Z-oxime, (6R,7R) cephalosporin, quaternary pyrrolidinium and chlorocatechol amide. Paragraph 0193 reports C30H34ClN7O10S2·3.8H2O, NMR and LC/MS 752. The analyzed hydrate and patent compound-series MIC tests are not silently transferred as exact anhydrous individual-strain observations. |
| patent-image | https://patentimages.storage.googleapis.com/1c/cb/00/f7a6265b2408f7/imgb0092.png; Example 12 Formula 89 drawing | supports | Direct visual inspection confirms the matching charged groups, side chains and stereochemical drawing. This supports document relevance while preserving the experimentally analyzed hydrate form. |
| wikipedia | https://en.wikipedia.org/wiki/Cefiderocol; Document identity | context_only | The native document reference resolves to cefiderocol. It is not used as primary support for antibacterial, mechanistic or current clinical claims. |
| taxa | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=470,562,573,287&amp;retmode=xml; Current exact organism identifiers | supports | 470=Acinetobacter baumannii;562=Escherichia coli;573=Klebsiella pneumoniae;287=Pseudomonas aeruginosa. These agree with all native and live source assignments. |
| cdc-audit | Ten current CDC and NCBI records; 224-cdc-verification.json | supports | All ten MIC values, greater-than qualifiers, R interpretations, source-specific CLSI footers, strain identifiers and BioSamples agree. µg/mL converts numerically 1:1 to mg/L. Retained hashes identify each inspected page. |
| mechanism-main | https://doi.org/10.1128/AAC.01454-17; PMID29061741/PMC5740388; full text, Tables 1–7 | supports | Original cefiderocol synthesized at Shionogi was tested against defined bacterial panels. Cefiderocol generally used ID-CAMHB, while comparators used CAMHB and some taxa required other media. Tables 5–7 directly test PBP affinity and transporter/porin effects. This supports antibacterial eligibility and bounded mechanism enrichment, not universal susceptibility or identity of CDC assay medium. Reagent counterion/hydration is not fully specified. |
| pbp | https://doi.org/10.1128/AAC.01454-17; Table 5; Supplement Method 3 p6 | supports | Membrane competition assays yield cefiderocol PBP3 IC50 values 0.04, 0.062, 0.06 and 0.67 µg/mL for E. coli NIHJ JC-2, K. pneumoniae SR22291, P. aeruginosa ATCC 27853 and A. baumannii ATCC 17978. Other PBPs also bind, including K. pneumoniae PBP2 at 0.063 µg/mL; PBP3 is not exclusive. These are competition IC50s, not MICs, dissociation constants or purified single-protein acylation rates. |
| pbp-method | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5740388/supplementaryFiles; Supplement Methods 1–4, especially Method 3 p6 | supports | First three membrane assays compete with [14C]benzylpenicillin 30–40 µg/mL; A. baumannii uses Bocillin FL 100 µg/mL, SDS-PAGE and fitted fluorescence. Method 4 morphology uses compound-containing Mueller-Hinton agar and 4–6 h exposure, not the same ID-CAMHB MIC assay. Method 1 documents piuA complementation and cirA/fiu deletion construction. |
| transport-mutants | https://doi.org/10.1128/AAC.01454-17; Tables 6–7 and transporter Results | supports | P. aeruginosa PAO1 cefiderocol MIC 0.125 µg/mL rises to 2 with piuA insertion; empty-vector control remains 2 and wild-type piuA complementation gives 0.063. pirA alone does not show this effect. E. coli BW25113 MIC 0.063 rises to 1 only with combined cirA/fiu loss; single losses are within twofold. K. pneumoniae ompK35/36 loss and P. aeruginosa MexAB-OprM modulation have small, strain/condition-specific effects. These are transport contributions, not equivalent primary drug targets or universal resistance determinants. |
| uptake | https://doi.org/10.1128/AAC.01405-16; PMID27736756/PMC5119021; complete Methods/Results, Tables 1–2 and Figures 2–4 text | supports | In P. aeruginosa PAO1, cefiderocol MIC changes from 0.125 µg/mL in CAMHB to 0.031 in ID-CAMHB and rises with added iron. [thiazole-14C]cefiderocol (95.8% purity) accumulation is higher after iron-depleted growth. Chrome azurol B chelation and intracellular calcein-quenching assays support iron binding/transport; the 3-methoxy catechol analog loses these effects. Radiolabeled material, altered analog and unlabeled cefiderocol have distinct assay roles. This paper does not identify a particular receptor by direct binding. |
| sar | https://doi.org/10.1016/j.ejmech.2018.06.014; Adopted PMID29960205; inspected primary abstract | partial | The SAR article identifies cefiderocol as compound 3 among catechol-containing derivatives and reports Gram-negative antibacterial activity. Full compound tables and synthesis were not inspected; observations on other derivatives cannot be transferred to cefiderocol. |
| murine-pd | https://doi.org/10.1016/j.ijantimicag.2017.10.008; Adopted PMID29111435; inspected primary abstract | partial | Dose-ranging cefiderocol was studied against eight P. aeruginosa isolates in neutropenic murine thigh infection. PK/PD exposure endpoints are animal-model evidence, not direct PBP binding, a current clinical breakpoint or unrestricted human treatment efficacy. |
| murine-humanized | https://doi.org/10.1128/AAC.01022-17; Adopted PMID28848004/PMC5655050; inspected abstract | partial | Humanized cefiderocol exposure was tested against 95 Gram-negative isolates in a murine thigh model; the abstract separates responses by MIC strata. XML retrieval failed and direct PMC HTML returned a challenge, so full protocols were not inspected. Animal humanized exposure does not establish a clinical resistance threshold. |
| allergy-review | https://doi.org/10.1016/j.jaip.2017.08.027; Adopted PMID29017833; inspected review abstract | context_only | This beta-lactam allergy review is not a primary cefiderocol mechanism or activity experiment. It is retained as contextual bibliography, not used to support direct target claims. |
| mdr-panel | https://doi.org/10.1007/s10096-017-3063-z; Adopted PMID28748397; inspected primary abstract | partial | The 753-isolate MDR Gram-negative panel reports cefiderocol susceptibility distributions and 20 strains with MIC≥8 mg/L. This supports activity against a tested resistant panel while explicitly preserving nonsusceptible examples. The isolate collection is not the CDC panel, and full methods/material details were not inspected. |
| greek-panel | https://doi.org/10.1093/jac/dkx049; Adopted PMID28369471; inspected primary abstract | partial | Broth microdilution tested 471 carbapenem-resistant Greek clinical isolates, comprising 282 Enterobacteriaceae and 189 nonfermenters. Activity against these populations supports the qualified native definition; genotype groupings do not establish isolated determinant causality or universal present-day susceptibility. |
| carbapenemases | https://doi.org/10.1128/AAC.03098-15; Adopted PMID27139465/PMC4914688; inspected primary abstract | partial | Purified-enzyme work reports comparatively low catalytic efficiency with IMP1, VIM2 and L1, slight KPC3 hydrolysis, and measurable NDM1 hydrolysis. It supports relative stability under the reported experiments, not absolute nonhydrolysability against all beta-lactamases. Full XML failed and PMC HTML was a challenge; detailed kinetic tables were not inspected. |
| conference2018 | https://doi.org/10.1093/ofid/ofy210.1182; Adopted PMC6253113; full poster 1351 text/table | partial | A conference abstract studies 834 Enterobacteriaceae with ESBL/carbapenemase characterization using iron-depleted broth and a stated trailing endpoint. Co-occurring enzyme groups are observational. The TEM/SHV-ESBL table has an internally reversed MIC50/MIC90 pair, so those figures are not adopted. This source-level conflict does not affect any native numeric observation. |
| conference-combination | https://doi.org/10.1093/ofid/ofaa439.1480; Adopted PMC7776597; full poster 1297 text | partial | Seven high-MIC A. baumannii isolates selected from 150 were tested with cefiderocol plus beta-lactamase inhibitors; six showed lower MICs in reported combinations. Combination activity is not cefiderocol monotherapy evidence. Figure-level individual results were not independently inspected and are not transferred. |
| conference-pkpd | https://doi.org/10.1093/ofid/ofaa439.1498; Adopted PMC7777002; full poster 1316 text | context_only | Model-based PK/PD analysis of CREDIBLE-CR and APEKS-NP patients found high fT&gt;MIC exposures and did not identify an exposure-outcome relationship within that range. This limited conference report does not establish a new target, molecular mechanism or present-day treatment recommendation. |
| adapter | kg-microbe-sources imodulondb; 223224-adapter-results.json; catalog and covered-organism searches | context_only | Before open-ended mechanism follow-up, peptidoglycan/siderophore queries found reference genes including e_coli/precise1k/b0084 ftsI, p_aeruginosa/precise364/PA1365 and a_baumannii/precise139/ABUW_2916 pfeA. All returned zero iModulon hits, so no component summary was applicable. These reference genes are not cefiderocol-specific causal evidence, nor is PA1365 equated to piuA without mapping. Sandbox DNS failure was resolved by permitted public retrieval. |
| search | Ignored-inclusive repository and public source follow-up; 224-local-hits.txt;224-owner-hits.txt | context_only | Exact identity, label, slug and full-key searches included ignored/hidden files outside .git/.venv. Native/raw/generated references and historical research leads were separated; actual ARO and curated activity/history ownership were appended. All adopted leads were independently disposed rather than copied from reports. |
| gates | Actual focused commands; 224-focused-results.json;224-validation.tsv | supports | Focused schema/strict and molecular/mint checks pass. All 21 expanded input hashes, including original captures, were rechecked unchanged. |
| cdc-1 | https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=33&amp;PanelID=1227; Panel 1227 isolate 0033; antimicrobial susceptibility row and footer | supports | Live Acinetobacter baumannii isolate 0033 reports cefiderocol 16 µg/mL, R; modal broth microdilution and no versioned CLSI footnote. Native mg/L value and censoring agree. No unreported iron-depletion protocol or missing breakpoint edition is invented. |
| biosample-1 | https://www.ncbi.nlm.nih.gov/biosample/SAMN04014874; SAMN04014874; sample/strain/organism fields | supports | Live BioSample identifies FDA-CDC-AR_0033, strain AR_0033, and Acinetobacter baumannii; this supports the exact native accession linkage. Missing host/geographic fields are not filled by inference. |
| cdc-2 | https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=78&amp;PanelID=1227; Panel 1227 isolate 0078; antimicrobial susceptibility row and footer | supports | Live Acinetobacter baumannii isolate 0078 reports cefiderocol 16 µg/mL, R; modal broth microdilution and CLSI 2024 M100 S34. Native mg/L value and censoring agree. No unreported iron-depletion protocol or missing breakpoint edition is invented. |
| biosample-2 | https://www.ncbi.nlm.nih.gov/biosample/SAMN04014919; SAMN04014919; sample/strain/organism fields | supports | Live BioSample identifies FDA-CDC-AR_0078, strain AR_0078, and Acinetobacter baumannii; this supports the exact native accession linkage. Missing host/geographic fields are not filled by inference. |
| cdc-3 | https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=83&amp;PanelID=1227; Panel 1227 isolate 0083; antimicrobial susceptibility row and footer | supports | Live Acinetobacter baumannii isolate 0083 reports cefiderocol &gt;32 µg/mL, R; modal broth microdilution and CLSI 2020 M100 S30. Native mg/L value and censoring agree. No unreported iron-depletion protocol or missing breakpoint edition is invented. |
| biosample-3 | https://www.ncbi.nlm.nih.gov/biosample/SAMN04014924; SAMN04014924; sample/strain/organism fields | supports | Live BioSample identifies FDA-CDC-AR_0083, strain AR_0083, and Acinetobacter baumannii; this supports the exact native accession linkage. Missing host/geographic fields are not filled by inference. |
| cdc-4 | https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=88&amp;PanelID=1227; Panel 1227 isolate 0088; antimicrobial susceptibility row and footer | supports | Live Acinetobacter baumannii isolate 0088 reports cefiderocol &gt;32 µg/mL, R; modal broth microdilution and CLSI 2024 M100 S34. Native mg/L value and censoring agree. No unreported iron-depletion protocol or missing breakpoint edition is invented. |
| biosample-4 | https://www.ncbi.nlm.nih.gov/biosample/SAMN04014929; SAMN04014929; sample/strain/organism fields | supports | Live BioSample identifies FDA-CDC-AR_0088, strain AR_0088, and Acinetobacter baumannii; this supports the exact native accession linkage. Missing host/geographic fields are not filled by inference. |
| cdc-5 | https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=118&amp;PanelID=1227; Panel 1227 isolate 0118; antimicrobial susceptibility row and footer | supports | Live Escherichia coli isolate 0118 reports cefiderocol &gt;32 µg/mL, R; modal broth microdilution and CLSI 2025 M100 S35. Native mg/L value and censoring agree. No unreported iron-depletion protocol or missing breakpoint edition is invented. |
| biosample-5 | https://www.ncbi.nlm.nih.gov/biosample/SAMN04014959; SAMN04014959; sample/strain/organism fields | supports | Live BioSample identifies FDA-CDC-AR_0118, strain AR_0118, and Escherichia coli; this supports the exact native accession linkage. Missing host/geographic fields are not filled by inference. |
| cdc-6 | https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=143&amp;PanelID=1227; Panel 1227 isolate 0143; antimicrobial susceptibility row and footer | supports | Live Klebsiella pneumoniae isolate 0143 reports cefiderocol 16 µg/mL, R; modal broth microdilution and CLSI 2025 M100 S35. Native mg/L value and censoring agree. No unreported iron-depletion protocol or missing breakpoint edition is invented. |
| biosample-6 | https://www.ncbi.nlm.nih.gov/biosample/SAMN04014984; SAMN04014984; sample/strain/organism fields | supports | Live BioSample identifies FDA-CDC-AR_0143, strain AR_0143, and Klebsiella pneumoniae; this supports the exact native accession linkage. Missing host/geographic fields are not filled by inference. |
| cdc-7 | https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=150&amp;PanelID=1227; Panel 1227 isolate 0150; antimicrobial susceptibility row and footer | supports | Live Escherichia coli isolate 0150 reports cefiderocol &gt;32 µg/mL, R; modal broth microdilution and CLSI 2025 M100 S35. Native mg/L value and censoring agree. No unreported iron-depletion protocol or missing breakpoint edition is invented. |
| biosample-7 | https://www.ncbi.nlm.nih.gov/biosample/SAMN04014991; SAMN04014991; sample/strain/organism fields | supports | Live BioSample identifies FDA-CDC-AR_0150, strain AR_0150, and Escherichia coli; this supports the exact native accession linkage. Missing host/geographic fields are not filled by inference. |
| cdc-8 | https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=151&amp;PanelID=1227; Panel 1227 isolate 0151; antimicrobial susceptibility row and footer | supports | Live Escherichia coli isolate 0151 reports cefiderocol &gt;64 µg/mL, R; modal broth microdilution and CLSI 2025 M100 S35. Native mg/L value and censoring agree. No unreported iron-depletion protocol or missing breakpoint edition is invented. |
| biosample-8 | https://www.ncbi.nlm.nih.gov/biosample/SAMN04014992; SAMN04014992; sample/strain/organism fields | supports | Live BioSample identifies FDA-CDC-AR_0151, strain AR_0151, and Escherichia coli; this supports the exact native accession linkage. Missing host/geographic fields are not filled by inference. |
| cdc-9 | https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=162&amp;PanelID=1227; Panel 1227 isolate 0162; antimicrobial susceptibility row and footer | supports | Live Escherichia coli isolate 0162 reports cefiderocol &gt;32 µg/mL, R; modal broth microdilution and CLSI 2025 M100 S35. Native mg/L value and censoring agree. No unreported iron-depletion protocol or missing breakpoint edition is invented. |
| biosample-9 | https://www.ncbi.nlm.nih.gov/biosample/SAMN04015003; SAMN04015003; sample/strain/organism fields | supports | Live BioSample identifies FDA-CDC-AR_0162, strain AR_0162, and Escherichia coli; this supports the exact native accession linkage. Missing host/geographic fields are not filled by inference. |
| cdc-10 | https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=246&amp;PanelID=1227; Panel 1227 isolate 0246; antimicrobial susceptibility row and footer | supports | Live Pseudomonas aeruginosa isolate 0246 reports cefiderocol 16 µg/mL, R; modal broth microdilution and CLSI 2025 M100 S35. Native mg/L value and censoring agree. No unreported iron-depletion protocol or missing breakpoint edition is invented. |
| biosample-10 | https://www.ncbi.nlm.nih.gov/biosample/SAMN04901636; SAMN04901636; sample/strain/organism fields | supports | Live BioSample identifies FDA-CDC-AR_0246, strain AR_0246, and Pseudomonas aeruginosa; this supports the exact native accession linkage. Missing host/geographic fields are not filled by inference. |

## Limits And Additional Notes

- DrugBank direct access returned 403; Reaxys detail remains current-authority corroborated without independent registry access. ChemSpider inspected text resolves the exact named stereochemical structure but did not expose its full downloadable identifiers.
- All eleven adopted citation leads were disposed. Full text was inspected for the 2017 mechanism paper and all three conference abstracts; other adopted primary/review sources were inspected at abstract level. PMC4914688/PMC5655050 XML failed and direct pages returned challenges.
- The 2016 uptake paper was read in full, and 2017 supplementary methods were inspected. Primary reagent salt/hydration is not fully resolved; radiolabeled and modified-analog controls remain distinct.
- CDC pages state modal broth microdilution but do not expose a full iron-depletion protocol. No new breakpoint is computed, and an absent versioned footer for 0033 remains absent.
- The 2018 conference table contains a source-internal MIC50/MIC90 inconsistency; those cells are not transferred. Individual figure values from the 2020 combination abstract were not independently inspected.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 21 expanded input hashes, including initial captures, unchanged. No native/source/status/history edits.
- Focused native checks used 023 own environment; chemistry used 019 locked RDKit 2026.03.5 against 023 cwd.
- Free public retrieval only. Original sandbox DNS failures are retained; permitted public-network retries resolved the structured adapter. All source snapshots are hashed with actual access timestamps.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T112825Z-cefiderocol
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cefiderocol: exact zwitterion, verified CDC observations and bounded primary
  mechanisms'
started_at: '2026-10-21T11:08:26Z'
finished_at: '2026-10-21T11:28:25Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independent entire native/ChEBI/ARO owner review, current exact
    structures, all ten live CDC/BioSample pairs, all eleven adopted citation leads,
    full original 2016 uptake and 2017 mechanism papers, 2017 supplementary methods,
    and patent Example 12 drawing.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: No confirmed native defect. The (6R,7R), Z-oxime zwitterion is structurally
  coherent, exact public cross-references agree, and all ten CDC MIC observations
  retain correct censoring, taxa, BioSamples and source-specific breakpoint footers.
  Primary studies support antibacterial and siderophore properties and offer optional
  PBP/transport enrichment. Their membrane competition, mutant, radiotracer, assay-medium
  and material scopes remain distinct from the CDC observations. Scientific assessment
  retains the stated evidence limits; full verification is blocked by the shared native-library
  failure.
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
  - path: data/antibiotics/antibacterial/cefiderocol.yaml
    sha256: 2aa500eeb7a570a41a8c2f7fddfa7c085ce0726a641085613a769d5a200fdfbb
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
- target_id: CHEBI:140376
  path: data/antibiotics/antibacterial/cefiderocol.yaml
  label: cefiderocol
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
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefiderocol.yaml
    role: Curator-owned CDC activity_spectrum observations and history
scope:
  description: Whole-record review of exact cefiderocol, including all ten curated
    activity observations.
  selection: Queue 224 in isolated batch 023; original capture preserved and actual
    ARO and curator-owned activity/history owners appended before judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:140376
  exclusions:
  - target: Cefiderocol sulfate/tosylate preparations, patent hydrate, catechol 3-methoxy
      analog, radiolabeled preparation and comparator antibiotics
    reason: Distinct materials or analogs retain their experimental roles; a drug-page
      alias does not equate their exact chemical identities.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual focused command passed with zero errors.
  target_ids:
  - CHEBI:140376
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefiderocol.yaml
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
  - CHEBI:140376
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefiderocol.yaml --out /private/tmp/am-review-session/224-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Molecular encodings and source mints
  status: passed
  required: true
  summary: Both encodings reproduce the complete key, formula, net-zero charge, masses
    and two R centres; both source mints agree.
  target_ids:
  - CHEBI:140376
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/check199200.py
    224 (cwd /private/tmp/antibioticmech-record-reviews-023)
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
  - CHEBI:140376
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
  - CHEBI:140376
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
  - CHEBI:140376
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
  - CHEBI:140376
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
  - CHEBI:140376
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
  - CHEBI:140376
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
  - CHEBI:140376
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
  - CHEBI:140376
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
  - CHEBI:140376
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/cefiderocol.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T11:21:19Z'
  support: supports
  summary: Read exact identity, complete structural definition, parents/roles/class,
    all ten activity_spectrum observations and their evidence, structure, exact/drug/document
    xrefs, both source concepts and six history events. No populated molecular_targets,
    mode_of_action, resistance, producer, clinical-status or causal-graph claims.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv
  locator: ChEBI row 2600; ARO row 333; native activity/history
  accessed_at: '2026-10-21T11:21:19Z'
  support: supports
  summary: ChEBI owns graph, definition, roles and ten adopted citation leads; ARO
    adds PMID29960205 and class/identity. The curated CDC observations and BioSample
    history are owned by the native record. Maintained owner hashes were captured
    before assessment.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:140376
  locator: Current structure, definition and ontology
  accessed_at: '2026-10-21T11:12:20Z'
  support: supports
  summary: Matches C30H34ClN7O10S2, full key DBPPRLRVDVJOCL-FQRUVTKNSA-N, (6R,7R)
    centres, Z oxime, net-zero zwitterion, cephalosporin and carboxylic-acid parents.
    Antibiotic/antibacterial roles are supported by primary activity. Additional current
    siderophore annotation is optional enrichment, not a missing-required-field defect.
  snapshot_sha256: 6da378d5251037ad9321d105de355b0514e82107fe66c7086e729e020aa3b9f6
- evidence_id: aro
  kind: authority
  reference: https://card.mcmaster.ca/aro/3004474
  locator: Current cefiderocol identity
  accessed_at: '2026-10-21T11:12:20Z'
  support: supports
  summary: ARO resolves cefiderocol/S-649266 to the matching graph and cephalosporin
    class. Its broad antibacterial mechanism description is database context rather
    than a replacement for primary experiment scope.
  snapshot_sha256: bbb41875db264107b17ba7a807cc89e44bea0f389c5bfb65151d26f32cdb44e9
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit 2026.03.5 checks
  locator: 224-chemistry.json
  accessed_at: '2026-10-21T11:12:04Z'
  support: supports
  summary: Both encodings parse to one net-neutral fragment, native complete key,
    formula, 752.228 average/751.14971 exact mass and two R centres. The native SMILES
    explicitly specifies Z oxime; standard InChI mobile-hydrogen normalization lacks
    a separate oxime /b layer but reproduces the retained key. Both source mints are
    correct.
  snapshot_sha256: 079cb26dc20411f406a07472c18a6403f26260541f7a770c37466a18b84d7756
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/77843966
  locator: Complete current PUG structure
  accessed_at: '2026-10-21T11:12:20Z'
  support: supports
  summary: CID 77843966 matches the exact zwitterionic formula and full stereochemical
    key; it is not a sulfate/tosylate salt record.
  snapshot_sha256: 68e1ca1f8ac2507d3c8a3367e9d8f379cae2bd46b12cbbd778c6c9e187c14f7d
- evidence_id: chembl
  kind: database
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL3989974.json
  locator: Complete current molecule
  accessed_at: '2026-10-21T11:12:21Z'
  support: supports
  summary: CHEMBL3989974 matches native formula, full key, (6R,7R) and explicit Z-oxime
    canonical SMILES.
  snapshot_sha256: 613a7daf8f75e26ca80f8d41b03ced7bce507c6e8b4948ac96f65d7c21813bd3
- evidence_id: cas
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/1225208-94-5/property/InChIKey/JSON
  locator: CAS identifier lookup
  accessed_at: '2026-10-21T11:12:30Z'
  support: supports
  summary: CAS 1225208-94-5 resolves to the same complete cefiderocol key.
  snapshot_sha256: 49fd62c288344748cf0405e2738fa9bb45b685d0da56b7f5175727a8a770bee1
- evidence_id: chemspider
  kind: database
  reference: https://www.chemspider.com/Chemical-Structure.52084902.html
  locator: Current identity, formula and verified IUPAC name
  accessed_at: '2026-10-21T11:12:30Z'
  support: supports
  summary: ChemSpider52084902 names the matching (6R,7R), Z-oxime structure with two
    specified centres and the correct formula/CAS. Its approximate average mass uses
    a different atomic-weight convention; exact mass agrees. Full downloadable structural
    identifiers were not exposed in inspected text.
  snapshot_sha256: 8ad3ea664e1de5faf656e4713609bc2563f6f29024d6b34aea86156f37a6e214
- evidence_id: reaxys
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:140376
  locator: Reaxys 21605074 mapping
  accessed_at: '2026-10-21T11:12:20Z'
  support: partial
  summary: The current exact ChEBI entry retains this registry mapping; independent
    Reaxys contents were not freely inspected. No identity contradiction was established.
  snapshot_sha256: 6da378d5251037ad9321d105de355b0514e82107fe66c7086e729e020aa3b9f6
- evidence_id: drugcentral
  kind: database
  reference: https://drugcentral.org/drugcard/5352
  locator: Drug-level identity
  accessed_at: '2026-10-21T11:12:21Z'
  support: supports
  summary: Resolves cefiderocol with CAS 1225208-94-5 and the neutral zwitterion formula.
    The page also lists sulfate/tosylate preparations among synonyms; its drug-level
    scope does not make those salts exact xrefs or establish formulation identity
    for the native graph.
  snapshot_sha256: 83c8532fcafb25c0fe97fd3fe5a8f5c9077eb05da16e720e14562458836171cf
- evidence_id: kegg
  kind: database
  reference: https://rest.kegg.jp/get/D11302
  locator: KEGG drug D11302
  accessed_at: '2026-10-21T11:12:21Z'
  support: supports
  summary: D11302 names cefiderocol with the native formula and cephalosporin class.
    Its link to a separate formulated salt entry is not transferred as exact zwitterion
    identity.
  snapshot_sha256: 4d712a7e3da798dda1df28d8cdbef25cd5d1687627d0d258d76fbb0b5059b298
- evidence_id: drugbank
  kind: search
  reference: https://go.drugbank.com/drugs/DB14879
  locator: Free direct access boundary
  accessed_at: '2026-10-21T11:13:16Z'
  support: unknown
  summary: Direct DrugBank retrieval returned HTTP403. Current ChEBI retains DB14879
    as a drug mapping; its independent detailed contents were not inspected.
  snapshot_sha256: d4768d374803b871498991acceb18d6e66a8ffdcac1c70af9e84e2a24f1e60cb
  search_scope: Exact cefiderocol/CHEBI:140376/ARO:3004474/full-key ignored-inclusive
    batch 023 search outside .git/.venv; structured catalog and covered-organism context;
    live public exact identifiers, all ten CDC/BioSample pairs, all adopted primary
    citation leads and mechanism follow-up on 2026-10-21.
- evidence_id: patent
  kind: primary_source
  reference: https://patents.google.com/patent/EP2341053A1/en
  locator: Cephalosporin having catechol group; Example 12, paragraph 0193
  accessed_at: '2026-10-21T11:12:21Z'
  support: supports
  summary: The patent is relevant. Visually inspected Formula 89/Compound (I-12) has
    the matching aminothiazole Z-oxime, (6R,7R) cephalosporin, quaternary pyrrolidinium
    and chlorocatechol amide. Paragraph 0193 reports C30H34ClN7O10S2·3.8H2O, NMR and
    LC/MS 752. The analyzed hydrate and patent compound-series MIC tests are not silently
    transferred as exact anhydrous individual-strain observations.
  snapshot_sha256: 186f9a7d4bedab6caf85b4735709ece37a14662cdd5308bb40b50b9523b81e8e
- evidence_id: patent-image
  kind: primary_source
  reference: https://patentimages.storage.googleapis.com/1c/cb/00/f7a6265b2408f7/imgb0092.png
  locator: Example 12 Formula 89 drawing
  accessed_at: '2026-10-21T11:18:29Z'
  support: supports
  summary: Direct visual inspection confirms the matching charged groups, side chains
    and stereochemical drawing. This supports document relevance while preserving
    the experimentally analyzed hydrate form.
  snapshot_sha256: 3410d3cadd27a81fbb9a072a0b1976d4e88d6e1ca27a79ce84a37828eead6d69
- evidence_id: wikipedia
  kind: database
  reference: https://en.wikipedia.org/wiki/Cefiderocol
  locator: Document identity
  accessed_at: '2026-10-21T11:12:22Z'
  support: context_only
  summary: The native document reference resolves to cefiderocol. It is not used as
    primary support for antibacterial, mechanistic or current clinical claims.
  snapshot_sha256: e961322a550d4ffa2fa4c2ff9badbb82028436186cfbbf110e113ffdbc4e6c8a
- evidence_id: taxa
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=470,562,573,287&retmode=xml
  locator: Current exact organism identifiers
  accessed_at: '2026-10-21T11:12:31Z'
  support: supports
  summary: 470=Acinetobacter baumannii;562=Escherichia coli;573=Klebsiella pneumoniae;287=Pseudomonas
    aeruginosa. These agree with all native and live source assignments.
  snapshot_sha256: 085b868566949b013af5083f358d5cc1ad34056c0d5ba336704a7f715cf199c4
- evidence_id: cdc-audit
  kind: validation
  reference: Ten current CDC and NCBI records
  locator: 224-cdc-verification.json
  accessed_at: '2026-10-21T11:15:51Z'
  support: supports
  summary: All ten MIC values, greater-than qualifiers, R interpretations, source-specific
    CLSI footers, strain identifiers and BioSamples agree. µg/mL converts numerically
    1:1 to mg/L. Retained hashes identify each inspected page.
  snapshot_sha256: f1deaf83955cfb3a73e7e6a7e7bafa258da2e03b37d7911f434462a5c1e32bbc
- evidence_id: mechanism-main
  kind: primary_source
  reference: https://doi.org/10.1128/AAC.01454-17
  locator: PMID29061741/PMC5740388; full text, Tables 1–7
  accessed_at: '2026-10-21T11:13:14Z'
  support: supports
  summary: Original cefiderocol synthesized at Shionogi was tested against defined
    bacterial panels. Cefiderocol generally used ID-CAMHB, while comparators used
    CAMHB and some taxa required other media. Tables 5–7 directly test PBP affinity
    and transporter/porin effects. This supports antibacterial eligibility and bounded
    mechanism enrichment, not universal susceptibility or identity of CDC assay medium.
    Reagent counterion/hydration is not fully specified.
  snapshot_sha256: 5aa29a2efaf579b4bf237f23d65f03b7323adf5ef68d3d9fe7581545247792de
- evidence_id: pbp
  kind: primary_source
  reference: https://doi.org/10.1128/AAC.01454-17
  locator: Table 5; Supplement Method 3 p6
  accessed_at: '2026-10-21T11:13:14Z'
  support: supports
  summary: Membrane competition assays yield cefiderocol PBP3 IC50 values 0.04, 0.062,
    0.06 and 0.67 µg/mL for E. coli NIHJ JC-2, K. pneumoniae SR22291, P. aeruginosa
    ATCC 27853 and A. baumannii ATCC 17978. Other PBPs also bind, including K. pneumoniae
    PBP2 at 0.063 µg/mL; PBP3 is not exclusive. These are competition IC50s, not MICs,
    dissociation constants or purified single-protein acylation rates.
  snapshot_sha256: 5aa29a2efaf579b4bf237f23d65f03b7323adf5ef68d3d9fe7581545247792de
- evidence_id: pbp-method
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5740388/supplementaryFiles
  locator: Supplement Methods 1–4, especially Method 3 p6
  accessed_at: '2026-10-21T11:15:41Z'
  support: supports
  summary: First three membrane assays compete with [14C]benzylpenicillin 30–40 µg/mL;
    A. baumannii uses Bocillin FL 100 µg/mL, SDS-PAGE and fitted fluorescence. Method
    4 morphology uses compound-containing Mueller-Hinton agar and 4–6 h exposure,
    not the same ID-CAMHB MIC assay. Method 1 documents piuA complementation and cirA/fiu
    deletion construction.
  snapshot_sha256: 26b56f93caa715163524a7af1ee05cb88b79120518c90fc39d6a588683900af6
- evidence_id: transport-mutants
  kind: primary_source
  reference: https://doi.org/10.1128/AAC.01454-17
  locator: Tables 6–7 and transporter Results
  accessed_at: '2026-10-21T11:13:14Z'
  support: supports
  summary: P. aeruginosa PAO1 cefiderocol MIC 0.125 µg/mL rises to 2 with piuA insertion;
    empty-vector control remains 2 and wild-type piuA complementation gives 0.063.
    pirA alone does not show this effect. E. coli BW25113 MIC 0.063 rises to 1 only
    with combined cirA/fiu loss; single losses are within twofold. K. pneumoniae ompK35/36
    loss and P. aeruginosa MexAB-OprM modulation have small, strain/condition-specific
    effects. These are transport contributions, not equivalent primary drug targets
    or universal resistance determinants.
  snapshot_sha256: 5aa29a2efaf579b4bf237f23d65f03b7323adf5ef68d3d9fe7581545247792de
- evidence_id: uptake
  kind: primary_source
  reference: https://doi.org/10.1128/AAC.01405-16
  locator: PMID27736756/PMC5119021; complete Methods/Results, Tables 1–2 and Figures
    2–4 text
  accessed_at: '2026-10-21T11:18:29Z'
  support: supports
  summary: In P. aeruginosa PAO1, cefiderocol MIC changes from 0.125 µg/mL in CAMHB
    to 0.031 in ID-CAMHB and rises with added iron. [thiazole-14C]cefiderocol (95.8%
    purity) accumulation is higher after iron-depleted growth. Chrome azurol B chelation
    and intracellular calcein-quenching assays support iron binding/transport; the
    3-methoxy catechol analog loses these effects. Radiolabeled material, altered
    analog and unlabeled cefiderocol have distinct assay roles. This paper does not
    identify a particular receptor by direct binding.
  snapshot_sha256: 1487b1ade25d7baa9abc94f84ecaee48dda480be4f971878304fb8810878c4c6
- evidence_id: sar
  kind: primary_source
  reference: https://doi.org/10.1016/j.ejmech.2018.06.014
  locator: Adopted PMID29960205; inspected primary abstract
  accessed_at: '2026-10-21T11:12:19Z'
  support: partial
  summary: The SAR article identifies cefiderocol as compound 3 among catechol-containing
    derivatives and reports Gram-negative antibacterial activity. Full compound tables
    and synthesis were not inspected; observations on other derivatives cannot be
    transferred to cefiderocol.
  snapshot_sha256: d4147821d5b0da1724f530e909ee64a1696166df02da619033fa00a5af73a5f2
- evidence_id: murine-pd
  kind: primary_source
  reference: https://doi.org/10.1016/j.ijantimicag.2017.10.008
  locator: Adopted PMID29111435; inspected primary abstract
  accessed_at: '2026-10-21T11:12:19Z'
  support: partial
  summary: Dose-ranging cefiderocol was studied against eight P. aeruginosa isolates
    in neutropenic murine thigh infection. PK/PD exposure endpoints are animal-model
    evidence, not direct PBP binding, a current clinical breakpoint or unrestricted
    human treatment efficacy.
  snapshot_sha256: d4147821d5b0da1724f530e909ee64a1696166df02da619033fa00a5af73a5f2
- evidence_id: murine-humanized
  kind: primary_source
  reference: https://doi.org/10.1128/AAC.01022-17
  locator: Adopted PMID28848004/PMC5655050; inspected abstract
  accessed_at: '2026-10-21T11:12:19Z'
  support: partial
  summary: Humanized cefiderocol exposure was tested against 95 Gram-negative isolates
    in a murine thigh model; the abstract separates responses by MIC strata. XML retrieval
    failed and direct PMC HTML returned a challenge, so full protocols were not inspected.
    Animal humanized exposure does not establish a clinical resistance threshold.
  snapshot_sha256: d4147821d5b0da1724f530e909ee64a1696166df02da619033fa00a5af73a5f2
- evidence_id: allergy-review
  kind: database
  reference: https://doi.org/10.1016/j.jaip.2017.08.027
  locator: Adopted PMID29017833; inspected review abstract
  accessed_at: '2026-10-21T11:12:19Z'
  support: context_only
  summary: This beta-lactam allergy review is not a primary cefiderocol mechanism
    or activity experiment. It is retained as contextual bibliography, not used to
    support direct target claims.
  snapshot_sha256: d4147821d5b0da1724f530e909ee64a1696166df02da619033fa00a5af73a5f2
- evidence_id: mdr-panel
  kind: primary_source
  reference: https://doi.org/10.1007/s10096-017-3063-z
  locator: Adopted PMID28748397; inspected primary abstract
  accessed_at: '2026-10-21T11:12:19Z'
  support: partial
  summary: The 753-isolate MDR Gram-negative panel reports cefiderocol susceptibility
    distributions and 20 strains with MIC≥8 mg/L. This supports activity against a
    tested resistant panel while explicitly preserving nonsusceptible examples. The
    isolate collection is not the CDC panel, and full methods/material details were
    not inspected.
  snapshot_sha256: d4147821d5b0da1724f530e909ee64a1696166df02da619033fa00a5af73a5f2
- evidence_id: greek-panel
  kind: primary_source
  reference: https://doi.org/10.1093/jac/dkx049
  locator: Adopted PMID28369471; inspected primary abstract
  accessed_at: '2026-10-21T11:12:19Z'
  support: partial
  summary: Broth microdilution tested 471 carbapenem-resistant Greek clinical isolates,
    comprising 282 Enterobacteriaceae and 189 nonfermenters. Activity against these
    populations supports the qualified native definition; genotype groupings do not
    establish isolated determinant causality or universal present-day susceptibility.
  snapshot_sha256: d4147821d5b0da1724f530e909ee64a1696166df02da619033fa00a5af73a5f2
- evidence_id: carbapenemases
  kind: primary_source
  reference: https://doi.org/10.1128/AAC.03098-15
  locator: Adopted PMID27139465/PMC4914688; inspected primary abstract
  accessed_at: '2026-10-21T11:12:19Z'
  support: partial
  summary: Purified-enzyme work reports comparatively low catalytic efficiency with
    IMP1, VIM2 and L1, slight KPC3 hydrolysis, and measurable NDM1 hydrolysis. It
    supports relative stability under the reported experiments, not absolute nonhydrolysability
    against all beta-lactamases. Full XML failed and PMC HTML was a challenge; detailed
    kinetic tables were not inspected.
  snapshot_sha256: d4147821d5b0da1724f530e909ee64a1696166df02da619033fa00a5af73a5f2
- evidence_id: conference2018
  kind: primary_source
  reference: https://doi.org/10.1093/ofid/ofy210.1182
  locator: Adopted PMC6253113; full poster 1351 text/table
  accessed_at: '2026-10-21T11:12:31Z'
  support: partial
  summary: A conference abstract studies 834 Enterobacteriaceae with ESBL/carbapenemase
    characterization using iron-depleted broth and a stated trailing endpoint. Co-occurring
    enzyme groups are observational. The TEM/SHV-ESBL table has an internally reversed
    MIC50/MIC90 pair, so those figures are not adopted. This source-level conflict
    does not affect any native numeric observation.
  snapshot_sha256: 1164f8ddd5e9aa001c73e1aad6e75bdda7f068bd63ada2c6468f8b84d65c6b6f
- evidence_id: conference-combination
  kind: primary_source
  reference: https://doi.org/10.1093/ofid/ofaa439.1480
  locator: Adopted PMC7776597; full poster 1297 text
  accessed_at: '2026-10-21T11:12:31Z'
  support: partial
  summary: Seven high-MIC A. baumannii isolates selected from 150 were tested with
    cefiderocol plus beta-lactamase inhibitors; six showed lower MICs in reported
    combinations. Combination activity is not cefiderocol monotherapy evidence. Figure-level
    individual results were not independently inspected and are not transferred.
  snapshot_sha256: d8765e1977c8f406c8d578720e37a27defe517133bd0f69a59918b5167177f0f
- evidence_id: conference-pkpd
  kind: primary_source
  reference: https://doi.org/10.1093/ofid/ofaa439.1498
  locator: Adopted PMC7777002; full poster 1316 text
  accessed_at: '2026-10-21T11:12:31Z'
  support: context_only
  summary: Model-based PK/PD analysis of CREDIBLE-CR and APEKS-NP patients found high
    fT>MIC exposures and did not identify an exposure-outcome relationship within
    that range. This limited conference report does not establish a new target, molecular
    mechanism or present-day treatment recommendation.
  snapshot_sha256: 8e60386885b007f8c5be41ef398c8f38048986830e7132b29eaa8ec7dc17f582
- evidence_id: adapter
  kind: search
  reference: kg-microbe-sources imodulondb
  locator: 223224-adapter-results.json; catalog and covered-organism searches
  accessed_at: '2026-10-21T11:12:41Z'
  support: context_only
  summary: Before open-ended mechanism follow-up, peptidoglycan/siderophore queries
    found reference genes including e_coli/precise1k/b0084 ftsI, p_aeruginosa/precise364/PA1365
    and a_baumannii/precise139/ABUW_2916 pfeA. All returned zero iModulon hits, so
    no component summary was applicable. These reference genes are not cefiderocol-specific
    causal evidence, nor is PA1365 equated to piuA without mapping. Sandbox DNS failure
    was resolved by permitted public retrieval.
  snapshot_sha256: 33ea81c2f7029ab07aa0557fececec513a06197690c835a240d0d96719d0a034
  search_scope: Exact cefiderocol/CHEBI:140376/ARO:3004474/full-key ignored-inclusive
    batch 023 search outside .git/.venv; structured catalog and covered-organism context;
    live public exact identifiers, all ten CDC/BioSample pairs, all adopted primary
    citation leads and mechanism follow-up on 2026-10-21.
- evidence_id: search
  kind: search
  reference: Ignored-inclusive repository and public source follow-up
  locator: 224-local-hits.txt;224-owner-hits.txt
  accessed_at: '2026-10-21T11:12:00Z'
  support: context_only
  summary: Exact identity, label, slug and full-key searches included ignored/hidden
    files outside .git/.venv. Native/raw/generated references and historical research
    leads were separated; actual ARO and curated activity/history ownership were appended.
    All adopted leads were independently disposed rather than copied from reports.
  snapshot_sha256: fe9c0e3ed2bb7ab382ccf07666cafdd17e3fe05ff9cf9e1dce809c075ddd33ec
  search_scope: Exact cefiderocol/CHEBI:140376/ARO:3004474/full-key ignored-inclusive
    batch 023 search outside .git/.venv; structured catalog and covered-organism context;
    live public exact identifiers, all ten CDC/BioSample pairs, all adopted primary
    citation leads and mechanism follow-up on 2026-10-21.
- evidence_id: gates
  kind: validation
  reference: Actual focused commands
  locator: 224-focused-results.json;224-validation.tsv
  accessed_at: '2026-10-21T11:12:04Z'
  support: supports
  summary: Focused schema/strict and molecular/mint checks pass. All 21 expanded input
    hashes, including original captures, were rechecked unchanged.
  snapshot_sha256: a95fbaa1fd346469c27ba1ed846bab8637ade2d2c787a911b865d661bd5e6246
- evidence_id: cdc-1
  kind: primary_source
  reference: https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=33&PanelID=1227
  locator: Panel 1227 isolate 0033; antimicrobial susceptibility row and footer
  accessed_at: '2026-10-21T11:12:22Z'
  support: supports
  summary: Live Acinetobacter baumannii isolate 0033 reports cefiderocol 16 µg/mL,
    R; modal broth microdilution and no versioned CLSI footnote. Native mg/L value
    and censoring agree. No unreported iron-depletion protocol or missing breakpoint
    edition is invented.
  snapshot_sha256: 3ba7cc974cceecc69554db25912fa5d7ac36f7fb98e5c6e3d693daf8915317a4
- evidence_id: biosample-1
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/biosample/SAMN04014874
  locator: SAMN04014874; sample/strain/organism fields
  accessed_at: '2026-10-21T11:12:22Z'
  support: supports
  summary: Live BioSample identifies FDA-CDC-AR_0033, strain AR_0033, and Acinetobacter
    baumannii; this supports the exact native accession linkage. Missing host/geographic
    fields are not filled by inference.
  snapshot_sha256: 70da53a72d4632f4c0f4a60dc96b7ae157122b723b6f4c8c9f079670f51150f3
- evidence_id: cdc-2
  kind: primary_source
  reference: https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=78&PanelID=1227
  locator: Panel 1227 isolate 0078; antimicrobial susceptibility row and footer
  accessed_at: '2026-10-21T11:12:22Z'
  support: supports
  summary: Live Acinetobacter baumannii isolate 0078 reports cefiderocol 16 µg/mL,
    R; modal broth microdilution and CLSI 2024 M100 S34. Native mg/L value and censoring
    agree. No unreported iron-depletion protocol or missing breakpoint edition is
    invented.
  snapshot_sha256: 1e8cc78c9c4f93fb8c8ad6f2c1829e06cd67ec61c7aa1e36f3765cf95e05656a
- evidence_id: biosample-2
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/biosample/SAMN04014919
  locator: SAMN04014919; sample/strain/organism fields
  accessed_at: '2026-10-21T11:12:22Z'
  support: supports
  summary: Live BioSample identifies FDA-CDC-AR_0078, strain AR_0078, and Acinetobacter
    baumannii; this supports the exact native accession linkage. Missing host/geographic
    fields are not filled by inference.
  snapshot_sha256: 702d48317a6092e13d2157d9e05e722f4bf8479143a48f413219e1e55ef8303f
- evidence_id: cdc-3
  kind: primary_source
  reference: https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=83&PanelID=1227
  locator: Panel 1227 isolate 0083; antimicrobial susceptibility row and footer
  accessed_at: '2026-10-21T11:12:23Z'
  support: supports
  summary: Live Acinetobacter baumannii isolate 0083 reports cefiderocol >32 µg/mL,
    R; modal broth microdilution and CLSI 2020 M100 S30. Native mg/L value and censoring
    agree. No unreported iron-depletion protocol or missing breakpoint edition is
    invented.
  snapshot_sha256: ae57182dc6633864533b55b69e3e4840ea624af0e19d7ffc93d30bfe593bebbd
- evidence_id: biosample-3
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/biosample/SAMN04014924
  locator: SAMN04014924; sample/strain/organism fields
  accessed_at: '2026-10-21T11:12:23Z'
  support: supports
  summary: Live BioSample identifies FDA-CDC-AR_0083, strain AR_0083, and Acinetobacter
    baumannii; this supports the exact native accession linkage. Missing host/geographic
    fields are not filled by inference.
  snapshot_sha256: e9216932286ce8a45a9974172b7a83898a4c58f5717c25996950353523452156
- evidence_id: cdc-4
  kind: primary_source
  reference: https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=88&PanelID=1227
  locator: Panel 1227 isolate 0088; antimicrobial susceptibility row and footer
  accessed_at: '2026-10-21T11:12:24Z'
  support: supports
  summary: Live Acinetobacter baumannii isolate 0088 reports cefiderocol >32 µg/mL,
    R; modal broth microdilution and CLSI 2024 M100 S34. Native mg/L value and censoring
    agree. No unreported iron-depletion protocol or missing breakpoint edition is
    invented.
  snapshot_sha256: e650cd1b9a5caa81b48df9dfb291408f6765c1d9c3021a42b10344377f24cdd7
- evidence_id: biosample-4
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/biosample/SAMN04014929
  locator: SAMN04014929; sample/strain/organism fields
  accessed_at: '2026-10-21T11:12:24Z'
  support: supports
  summary: Live BioSample identifies FDA-CDC-AR_0088, strain AR_0088, and Acinetobacter
    baumannii; this supports the exact native accession linkage. Missing host/geographic
    fields are not filled by inference.
  snapshot_sha256: 9cdf36b692733c488b9b1cc2e2bdc3e2e7d6e5d41c5d7474e03c13315c3ab313
- evidence_id: cdc-5
  kind: primary_source
  reference: https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=118&PanelID=1227
  locator: Panel 1227 isolate 0118; antimicrobial susceptibility row and footer
  accessed_at: '2026-10-21T11:12:24Z'
  support: supports
  summary: Live Escherichia coli isolate 0118 reports cefiderocol >32 µg/mL, R; modal
    broth microdilution and CLSI 2025 M100 S35. Native mg/L value and censoring agree.
    No unreported iron-depletion protocol or missing breakpoint edition is invented.
  snapshot_sha256: 7848751c0f1eb2f615062ea2a702f6092f75457f0fc4ad71e7008d4270a6a3af
- evidence_id: biosample-5
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/biosample/SAMN04014959
  locator: SAMN04014959; sample/strain/organism fields
  accessed_at: '2026-10-21T11:12:25Z'
  support: supports
  summary: Live BioSample identifies FDA-CDC-AR_0118, strain AR_0118, and Escherichia
    coli; this supports the exact native accession linkage. Missing host/geographic
    fields are not filled by inference.
  snapshot_sha256: f3ad8d3c060e57c3cac203934e8ac001c8564d773339e89370e5bb74e091bede
- evidence_id: cdc-6
  kind: primary_source
  reference: https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=143&PanelID=1227
  locator: Panel 1227 isolate 0143; antimicrobial susceptibility row and footer
  accessed_at: '2026-10-21T11:12:25Z'
  support: supports
  summary: Live Klebsiella pneumoniae isolate 0143 reports cefiderocol 16 µg/mL, R;
    modal broth microdilution and CLSI 2025 M100 S35. Native mg/L value and censoring
    agree. No unreported iron-depletion protocol or missing breakpoint edition is
    invented.
  snapshot_sha256: c2b7b6f6887f9beefbc812b4e1b140c17c7308a947ed0b36f240a8116574423a
- evidence_id: biosample-6
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/biosample/SAMN04014984
  locator: SAMN04014984; sample/strain/organism fields
  accessed_at: '2026-10-21T11:12:25Z'
  support: supports
  summary: Live BioSample identifies FDA-CDC-AR_0143, strain AR_0143, and Klebsiella
    pneumoniae; this supports the exact native accession linkage. Missing host/geographic
    fields are not filled by inference.
  snapshot_sha256: daba7b6996dbcf73149115c958a1064d751a9732bc9f2efb41ba8be3f0a88308
- evidence_id: cdc-7
  kind: primary_source
  reference: https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=150&PanelID=1227
  locator: Panel 1227 isolate 0150; antimicrobial susceptibility row and footer
  accessed_at: '2026-10-21T11:12:26Z'
  support: supports
  summary: Live Escherichia coli isolate 0150 reports cefiderocol >32 µg/mL, R; modal
    broth microdilution and CLSI 2025 M100 S35. Native mg/L value and censoring agree.
    No unreported iron-depletion protocol or missing breakpoint edition is invented.
  snapshot_sha256: 1c92e3bbcdfe31947d512317d4a14cf292ae1842f61da30197253a5c024407a8
- evidence_id: biosample-7
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/biosample/SAMN04014991
  locator: SAMN04014991; sample/strain/organism fields
  accessed_at: '2026-10-21T11:12:27Z'
  support: supports
  summary: Live BioSample identifies FDA-CDC-AR_0150, strain AR_0150, and Escherichia
    coli; this supports the exact native accession linkage. Missing host/geographic
    fields are not filled by inference.
  snapshot_sha256: 075e5442b839a5b9e985f0a0895d0cda1e2cf7bee2db382a49515a958fec1e19
- evidence_id: cdc-8
  kind: primary_source
  reference: https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=151&PanelID=1227
  locator: Panel 1227 isolate 0151; antimicrobial susceptibility row and footer
  accessed_at: '2026-10-21T11:12:28Z'
  support: supports
  summary: Live Escherichia coli isolate 0151 reports cefiderocol >64 µg/mL, R; modal
    broth microdilution and CLSI 2025 M100 S35. Native mg/L value and censoring agree.
    No unreported iron-depletion protocol or missing breakpoint edition is invented.
  snapshot_sha256: a4300e29fe055e4c338b0a6d4a010cf899a94bec199be6d201bafae066f8c5ed
- evidence_id: biosample-8
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/biosample/SAMN04014992
  locator: SAMN04014992; sample/strain/organism fields
  accessed_at: '2026-10-21T11:12:28Z'
  support: supports
  summary: Live BioSample identifies FDA-CDC-AR_0151, strain AR_0151, and Escherichia
    coli; this supports the exact native accession linkage. Missing host/geographic
    fields are not filled by inference.
  snapshot_sha256: f27bb0bff13104704bf2b231c31018ae71ed27f50cf2b76e455f7d288add2a35
- evidence_id: cdc-9
  kind: primary_source
  reference: https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=162&PanelID=1227
  locator: Panel 1227 isolate 0162; antimicrobial susceptibility row and footer
  accessed_at: '2026-10-21T11:12:28Z'
  support: supports
  summary: Live Escherichia coli isolate 0162 reports cefiderocol >32 µg/mL, R; modal
    broth microdilution and CLSI 2025 M100 S35. Native mg/L value and censoring agree.
    No unreported iron-depletion protocol or missing breakpoint edition is invented.
  snapshot_sha256: 5a93402322abb4fa1a8594bb4bd68c8c147e5213fc03e0e724758053c4a28eaa
- evidence_id: biosample-9
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/biosample/SAMN04015003
  locator: SAMN04015003; sample/strain/organism fields
  accessed_at: '2026-10-21T11:12:28Z'
  support: supports
  summary: Live BioSample identifies FDA-CDC-AR_0162, strain AR_0162, and Escherichia
    coli; this supports the exact native accession linkage. Missing host/geographic
    fields are not filled by inference.
  snapshot_sha256: a5b39df7e12ff58808d40e55a1dad4ce51915cdd566fd9f31dcd5f39e2e78c03
- evidence_id: cdc-10
  kind: primary_source
  reference: https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=246&PanelID=1227
  locator: Panel 1227 isolate 0246; antimicrobial susceptibility row and footer
  accessed_at: '2026-10-21T11:12:29Z'
  support: supports
  summary: Live Pseudomonas aeruginosa isolate 0246 reports cefiderocol 16 µg/mL,
    R; modal broth microdilution and CLSI 2025 M100 S35. Native mg/L value and censoring
    agree. No unreported iron-depletion protocol or missing breakpoint edition is
    invented.
  snapshot_sha256: e9d39aa834a718c77a30893790f21fa5a7a3e8daf9e351b12f941666df8cce80
- evidence_id: biosample-10
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/biosample/SAMN04901636
  locator: SAMN04901636; sample/strain/organism fields
  accessed_at: '2026-10-21T11:12:30Z'
  support: supports
  summary: Live BioSample identifies FDA-CDC-AR_0246, strain AR_0246, and Pseudomonas
    aeruginosa; this supports the exact native accession linkage. Missing host/geographic
    fields are not filled by inference.
  snapshot_sha256: 7abbdadd54a0b5e9eb0ab3d4b21823cdc39780bbc82f850b73dc0e055ca25dca
assessments:
- assessment_id: identity
  area: identity
  topic: Exact cefiderocol zwitterion
  outcome: supported
  summary: Native chemical encodings, explicit oxime stereochemistry, complete public
    structure mappings and patent drawing agree. Salt/hydrate drug materials retain
    distinct scope.
  target_ids:
  - CHEBI:140376
  evidence_ids:
  - native
  - chebi
  - chemistry
  - pubchem
  - chembl
  - cas
  - chemspider
  - patent
  - patent-image
- assessment_id: grounding
  area: grounding
  topic: Structural parents and antibacterial roles
  outcome: supported
  summary: Cephalosporin and carboxylic-acid parentage fit the graph. Primary antibacterial
    studies and live isolate measurements support antibiotic/antibacterial eligibility;
    resistant isolates do not contradict the qualified class role.
  target_ids:
  - CHEBI:140376
  evidence_ids:
  - chebi
  - aro
  - mechanism-main
  - uptake
  - cdc-audit
- assessment_id: definition
  area: evidence
  topic: Siderophore and resistant-pathogen wording
  outcome: supported
  summary: The described side chains match the exact graph. Iron chelation/uptake
    and tested resistant-organism activity support the bounded definition, which does
    not assert every strain is susceptible.
  target_ids:
  - CHEBI:140376
  evidence_ids:
  - chemistry
  - patent-image
  - uptake
  - mechanism-main
  - mdr-panel
  - greek-panel
- assessment_id: xrefs
  area: grounding
  topic: Exact, drug and document references
  outcome: unknown
  summary: Accessible exact registries and the patent agree. Drug pages have broader
    formulation scope; DrugBank detailed access and independent Reaxys registry verification
    remain limited. Wikipedia is document context only.
  target_ids:
  - CHEBI:140376
  evidence_ids:
  - pubchem
  - chembl
  - cas
  - chemspider
  - aro
  - reaxys
  - drugbank
  - drugcentral
  - kegg
  - patent
  - wikipedia
- assessment_id: activity
  area: evidence
  topic: All ten curated CDC observations
  outcome: supported
  summary: Every numeric value, censoring symbol, R interpretation, organism, BioSample
    and versioned/nonversioned footer matches the live source. The native assay retains
    modal broth microdilution; no medium protocol is inferred from unrelated papers.
  target_ids:
  - CHEBI:140376
  evidence_ids:
  - cdc-audit
  - taxa
  - cdc-1
  - cdc-2
  - cdc-3
  - cdc-4
  - cdc-5
  - cdc-6
  - cdc-7
  - cdc-8
  - cdc-9
  - cdc-10
  - biosample-1
  - biosample-2
  - biosample-3
  - biosample-4
  - biosample-5
  - biosample-6
  - biosample-7
  - biosample-8
  - biosample-9
  - biosample-10
- assessment_id: mechanism
  area: evidence
  topic: Optional PBP and transport representation
  outcome: supported
  summary: Direct membrane PBP competition, mutant/complementation and iron-dependent
    uptake experiments provide concrete optional enrichment. Each measured variable,
    strain and material must be retained; absent optional target/graph fields are
    not defects.
  target_ids:
  - CHEBI:140376
  evidence_ids:
  - pbp
  - pbp-method
  - transport-mutants
  - uptake
  - adapter
- assessment_id: resistance
  area: evidence
  topic: Resistance-associated effects and stability
  outcome: supported
  summary: Native records resistant isolate phenotypes without inferred molecular
    determinants. Transporter deletions, modest porin/efflux effects and relative
    enzyme stability are bounded primary leads. Combination poster data and genotype-grouped
    MICs are not single-gene causality.
  target_ids:
  - CHEBI:140376
  evidence_ids:
  - native
  - transport-mutants
  - carbapenemases
  - conference2018
  - conference-combination
- assessment_id: clinical-producer
  area: scope
  topic: Animal, clinical, producer and graph boundaries
  outcome: not_applicable
  summary: Native has no clinical-status, natural-producer or causal-graph claims.
    Animal humanized exposure and conference PK/PD models remain separate from current
    approval, dosing or clinical efficacy recommendations.
  target_ids:
  - CHEBI:140376
  evidence_ids:
  - native
  - murine-pd
  - murine-humanized
  - conference-pkpd
- assessment_id: citations
  area: evidence
  topic: Every adopted source lead
  outcome: supported
  summary: All eight unique PMID leads and three distinct PMC conference abstracts
    were inspected at the stated abstract/full-text level. Review, primary research,
    combination work and source-internal table conflict are distinguished.
  target_ids:
  - CHEBI:140376
  evidence_ids:
  - sar
  - murine-pd
  - murine-humanized
  - allergy-review
  - mechanism-main
  - mdr-panel
  - greek-panel
  - carbapenemases
  - conference2018
  - conference-combination
  - conference-pkpd
- assessment_id: provenance
  area: provenance
  topic: Source owners, mints and history
  outcome: supported
  summary: Both source mints and four seed events are coherent; two later curated
    events account for the ten CDC observations and BioSample fields. Actual generated
    and curator-owned inputs are captured, and SEEDED is unchanged.
  target_ids:
  - CHEBI:140376
  evidence_ids:
  - native
  - owners
  - chemistry
- assessment_id: completeness
  area: completeness
  topic: Optional primary enrichment
  outcome: supported
  summary: Inspected sources offer well-defined PBP/transport evidence and explicit
    quantitative assay limits. No optional omission or source access failure establishes
    a required native correction.
  target_ids:
  - CHEBI:140376
  evidence_ids:
  - pbp
  - pbp-method
  - transport-mutants
  - uptake
- assessment_id: schema
  area: schema
  topic: Focused native validation
  outcome: supported
  summary: Schema/strict and molecular/mint checks passed; scientific assessment remains
    separate from those deterministic results.
  target_ids:
  - CHEBI:140376
  evidence_ids:
  - gates
  - chemistry
findings: []
actions:
- action_id: A1
  description: Optionally curate primary PBP, uptake and transporter evidence with
    experiment-specific scope.
  finding_ids: []
  target_ids:
  - CHEBI:140376
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefiderocol.yaml
    role: Curator-owned molecular_targets, mode_of_action, evidence and causal_graphs
      via validated writer
  acceptance_checks:
  - Use Table 5 and Supplement Method 3 of DOI10.1128/AAC.01454-17 for strain-specific
    membrane competition IC50s; distinguish [14C]benzylpenicillin from Bocillin FL
    and do not equate IC50 with MIC or Kd. PBP3 is not the exclusive interacting PBP.
  - Keep P. aeruginosa piuA insertion/complementation and E. coli combined cirA/fiu
    deletion as transport contributions. Preserve single-gene controls, growth medium
    and parent strain; do not label every transporter a lethal molecular target.
  - Separate 2016 radiolabeled cefiderocol accumulation, unlabeled chelation/MIC assays
    and catechol 3-methoxy analog controls. Iron availability, reporter assay and
    unresolved salt/hydrate details must remain explicit.
  - Map protein identifiers against the actual experimentally used strains; reference-dataset
    genes are not substitute strain/protein evidence.
  - Run schema/strict and applicable term/reference/evidence/history/graph/corpus
    gates after separately authorized curation.
- action_id: A2
  description: Preserve source distinctions when expanding activity or corroborating
    remaining references.
  finding_ids: []
  target_ids:
  - CHEBI:140376
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefiderocol.yaml
    role: Curator-owned activity_spectrum and evidence
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Source-owned registry and document mappings
  acceptance_checks:
  - Keep each CDC isolate, exact censoring and source-specific breakpoint edition,
    including absent edition for 0033. Retain µg/mL-to-mg/L equivalence without adding
    unreported iron-depleted medium.
  - Do not transfer animal PK/PD, combination inhibitor experiments or aggregate clinical-panel
    statistics into individual CDC observations. Resolve the conference2018 table
    inconsistency before reusing those numeric cells.
  - Corroborate DrugBank DB14879 and Reaxys 21605074 detail through permissible source
    access when available; failure to retrieve does not warrant deletion.
  - Preserve patent Example 12 hydrate analysis and the exact Formula 89 drawing if
    citing synthesis or assay data; each patent compound must be mapped before numeric
    transfer.
limitations:
- DrugBank direct access returned 403; Reaxys detail remains current-authority corroborated
  without independent registry access. ChemSpider inspected text resolves the exact
  named stereochemical structure but did not expose its full downloadable identifiers.
- All eleven adopted citation leads were disposed. Full text was inspected for the
  2017 mechanism paper and all three conference abstracts; other adopted primary/review
  sources were inspected at abstract level. PMC4914688/PMC5655050 XML failed and direct
  pages returned challenges.
- The 2016 uptake paper was read in full, and 2017 supplementary methods were inspected.
  Primary reagent salt/hydration is not fully resolved; radiolabeled and modified-analog
  controls remain distinct.
- CDC pages state modal broth microdilution but do not expose a full iron-depletion
  protocol. No new breakpoint is computed, and an absent versioned footer for 0033
  remains absent.
- The 2018 conference table contains a source-internal MIC50/MIC90 inconsistency;
  those cells are not transferred. Individual figure values from the 2020 combination
  abstract were not independently inspected.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 21 expanded input hashes, including initial captures, unchanged. No native/source/status/history
  edits.
- Focused native checks used 023 own environment; chemistry used 019 locked RDKit
  2026.03.5 against 023 cwd.
- Free public retrieval only. Original sandbox DNS failures are retained; permitted
  public-network retries resolved the structured adapter. All source snapshots are
  hashed with actual access timestamps.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:140376
- https://doi.org/10.1128/AAC.01454-17
- https://doi.org/10.1128/AAC.01405-16
- https://patents.google.com/patent/EP2341053A1/en
tags:
- cefiderocol
- exact-identity
- siderophore
- cdc-isolates
- primary-mechanism
```
