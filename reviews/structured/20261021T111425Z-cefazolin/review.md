# Cefazolin: exact identity, seven verified CDC MIC observations and qualified resistance evidence

- Review: 20261021T111425Z-cefazolin
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:55:30Z
- Finished UTC: 2026-10-21T11:14:25Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

No confirmed native defect. Exact neutral cefazolin, source mints and publicly resolved structure mappings agree. All seven curator-owned CDC rows retain the correct censored MIC, modal broth method, stated 2025 interpretation and current BioSample/taxon mapping. The PBP and thirteen resistance entries are explicitly database assertions, not primary-validated claims. Inspected primary studies support several resistance mechanisms with important expression-host, porin-loss and assay boundaries; NmcA-specific cefazolin evidence and some registry detail remain unresolved. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole-record review of neutral cefazolin, including all populated activity and resistance fields.

Selection: Queue 214 in isolated batch 022; initial captures preserved and actual ARO/source/curator owners appended before detailed judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:474053 | data/antibiotics/antibacterial/cefazolin.yaml | generated | cefazolin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | CHEBI:474053 | Actual focused command passed with zero errors. |
| Focused strict | passed | True | CHEBI:474053 | Actual focused command passed with zero errors. |
| Independent molecular encodings and source mints | passed | True | CHEBI:474053 | Both molecular encodings, complete key, formula, charge, masses, two R centres and both source mints agree. |
| Authoritative full QC | failed | True | CHEBI:474053 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:474053 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:474053 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:474053 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:474053 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:474053 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:474053 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:474053 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:474053 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Neutral exact cefazolin

identity: supported. Targets: CHEBI:474053.

The exact free acid has coherent graph, stereochemistry, charge, formula/masses and source mints. Sodium formulations and database drug synonyms are not conflated with exact chemical equivalence.

### Parents, class and biological roles

grounding: supported. Targets: CHEBI:474053.

Cephalosporin, tetrazole and thiadiazole parents fit the graph. Allergen is a biological classification consistent with adopted allergy context, not a claim that all recipients react. Antibacterial activity is directly supported beyond family inference.

### Exact/drug/document placement

grounding: unknown. Targets: CHEBI:474053.

Resolved public exact mappings agree, and broader drug/document references are appropriately separated. HMDB, LINCS, Reaxys and DrugBank detail remains access-limited.

### Structural description

evidence: supported. Targets: CHEBI:474053.

The defined side-chain positions/groups and first-generation class agree with the graph and authorities. No unqualified clinical or species-wide mechanism is embedded in the definition.

### All seven censored MIC observations

evidence: supported. Targets: CHEBI:474053.

Every native CDC citation verifies the precise isolate, &gt;8 MIC, R interpretation, modal broth method and 2025 footer. BioSample/current taxonomy checks agree, including the C. freundii sample with a legacy E. coli title. These are observed isolate phenotypes, not inferred causes.

### Broad PBP target and primary status

evidence: unknown. Targets: CHEBI:474053.

The native target is an honest database assertion with PRIMARY_EVIDENCE_NEEDED and no fabricated protein/taxon. The2002 primary study links PBP expression and cefazolin efficacy but labels PBPs with other beta-lactams; its cefazolin affinity numbers are secondary citations. A direct cefazolin binding paper should be inspected before primary upgrade.

### Seven TEM/CTX-M/CMY/PDC assertions

evidence: supported. Targets: CHEBI:474053.

Experimental 2021 Table 2/Table S1 supports elevated cefazolin MIC with TEM-1, CTX-M-3, CTX-M-15, CTX-M-27, CMY-2, PDC-3 and PDC-5 in the E. coli expression host. The native database status remains appropriate and does not imply purified kinetics or a Pseudomonas clinical breakpoint.

### PRC-1, LAQ-1, CAE-1 and PSZ-1 assay scopes

evidence: supported. Targets: CHEBI:474053.

All four determinants have cefazolin-specific expression susceptibility evidence. PRC-1/LAQ-1/PSZ-1 also have purified hydrolysis evidence; CAE-1 does not. PSZ-1 kinetic text/table inconsistency precludes unqualified numeric reuse but does not refute native qualitative database context.

### Reduced permeability requires loss context

evidence: supported. Targets: CHEBI:474053.

The source-supported mechanism is combined OmpC/OmpF loss or coordinated reduction, not action of wild-type OmpC. The 1982 experiment shows isolated loss of either porin leaves cefazolin susceptibility unchanged. Native identifies a database reduced-permeability assertion and gives no claim of isolated knockout sufficiency; optional primary annotation must state the actual condition.

### NmcA exact cefazolin primary support

evidence: unknown. Targets: CHEBI:474053.

Current authority and raw exact edge support the database assertion. The inspected 1994 paper establishes NmcA/regulation mainly with carbapenem/ampicillin readouts; exact cefazolin hydrolysis/MIC support remains a bounded follow-up, not a confirmed false claim.

### Historical sodium and combination evidence

evidence: supported. Targets: CHEBI:474053.

1973 sodium assays support antibacterial eligibility. 2016 synergy, clinical cohorts and neutrophil models remain intervention/material-specific; no combination or host phenotype is misassigned as neutral cefazolin monotherapy or direct binding.

### Clinical status and production

scope: not_applicable. Targets: CHEBI:474053.

Native asserts neither current regulatory status nor a natural producer. Historical treatment reports and precursor cephalosporin C fermentation in a derivative patent do not supply those missing optional claims.

### Actual owners and fifteen history events

provenance: supported. Targets: CHEBI:474053.

Five seed/reseed events and ten curator activity/annotation events are coherent with the current record. Curated CDC claims remain owned by the actual YAML; source assertions are traced to their raw/config owners. SEEDED is retained.

### Bounded primary enrichment

completeness: supported. Targets: CHEBI:474053.

Concrete primary resistance, PBP and activity leads can enrich the record subject to exact material and assay mapping. Empty optional domains or honest PRIMARY_EVIDENCE_NEEDED status alone do not create a defect.

### Focused validation

schema: supported. Targets: CHEBI:474053.

Schema/strict/independent chemical and source-mint checks pass. Scientific evidence assessment remains separate from structural validation.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optionally promote selected resistance assertions with primary context.

- Use2021 Table S1 exact rows 32–40 for named genes; preserve E. coli BW25113/pGDP1 expression host, MIC units/qualifiers and control, and do not invent a cefazolin breakpoint for P. aeruginosa.
- For OmpC, explicitly encode coordinated porin loss/reduction and E. coli K-12 context; do not say isolated ompC loss or wild-type OmpC alone confers resistance. Keep99% colony-inhibition endpoint distinct from standard MIC.
- Distinguish cloned-gene susceptibility shifts from purified hydrolysis. CAE-1 has no successful purification/kinetic measurement in the inspected primary paper.
- Adjudicate PSZ-1Table 5 versus narrative before adopting any kinetic constant; keep PRC-1/LAQ-1 experimental MIC changes distinct from clinical resistant classification.
- Retrieve the earlier NmcA biochemical paper cited as Nordmann 1993 AAC 37:939–946 or another direct exact-drug experiment before marking NmcA cefazolin support primary-verified.
- Keep observed CDC isolate resistance distinct from assigning a particular causal determinant without matched genomic/functional evidence.

### A2

Optionally complete direct PBP evidence and access-limited identity corroboration.

- Follow Murakami 1987 AAC 31:1307–1311 cited by Bamberger 2002, or another exact cefazolin competition/acylation assay; inspect original organism, protein preparation, compound and endpoint before primary target upgrade.
- Do not treat labeled ampicillin PBP bands, synergy rationale, iModulonDB gene matches or class-level review statements as direct cefazolin binding measurements.
- Corroborate HMDB0015422,LSM-34744,Reaxys4169371 andDrugBankDB01327 when freely permissible detail is available; do not delete based on retrieval failure alone.
- For any newly curated quantitative activity, preserve sodium/formulation scope and historical medium/inoculum; maintain existing CDC censored MICs and sample provenance.
- Run applicable native schema/strict, evidence/term/reference/history and corpus gates after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/cefazolin.yaml; Entire YAML | supports | Read identity/definition, synonyms, five parents, roles, chemical graph and all exact/drug/document xrefs; seven activity_spectrum rows; thirteen resistance mechanisms; one explicitly PRIMARY_EVIDENCE_NEEDED PBP target; both source concepts; all fifteen history events. No populated producer, clinical-status, mode or causal_graph fields. |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv; data/raw/aro_resistance_edges.tsv; ChEBI row2971; ARO inventory43; target44; resistance1385–1397; conf/aro_target_roles.tsv row30 | supports | Identity and eight ChEBI PMID leads plus two ARO PMID leads match native provenance. All thirteen exact cefazolin resistance edges and the PBP edge/role match the imported database assertions. CDC rows are curator-owned within the actual record, not inferred to be generated from adjacent NCBI AST inventories. Actual owners were captured before judgment. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:474053; Current identity, chemical parents and role assertions | supports | Current ChEBI matches neutral C14H14N8O4S3 and full key MLYYVTUWGNIJIB-BXKDBHETSA-N. Chemical parents are cephalosporin, tetrazoles and thiadiazoles; beta-lactam antibiotic allergen is an additional biological classification, not a structural class. Antibiotic/antibacterial roles and the structural definition are coherent. |
| aro | https://card.mcmaster.ca/aro/0000058; Current drug identity | supports | Current ARO identifies cefazolin as a first-generation cephalosporin. Native database target/resistance status is retained; the authority is not substituted for primary assay details. |
| chemistry | Independent RDKit 2026.03.5 checks; 214-chemistry.json | supports | SMILES and InChI independently produce the same neutral single-fragment graph, complete key, formula, average/exact masses and two R centres. Both source-specific minted identifiers are correct. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/33255; Current complete PUG structure | supports | CID33255 matches the full native graph and stereochemical key, including both heterocyclic side chains. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL1435.json; Current exact molecule | supports | CHEMBL1435 matches the neutral formula and full key; no hydrate or salt conflation was found. |
| cas | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/25953-19-9/property/InChIKey/JSON; CAS-name resolution | supports | CAS25953-19-9 resolves to the exact CID33255 structure/key. |
| kegg-compound | https://rest.kegg.jp/get/C06880/mol; Current MOL independently parsed | supports | KEGG C06880 has the correct formula and its MOL generates the complete native key using the locked 019 RDKit interpreter against 022 cwd; result captured in 214-kegg-check.json. |
| vsdb | https://bioregistry.io/vsdb:1910; Resolved Veterinary Substances Database record1910 | supports | The resolved entry explicitly describes cefazolin acid and provides the exact native formula, InChI and key. Sodium pentahydrate is listed separately as a variant, so this native exact xref is not a salt mismatch. |
| registry-limits | https://www.ebi.ac.uk/chebi/CHEBI:474053; HMDB0015422, LSM-34744 and Reaxys4169371 mappings | partial | These identifiers remain live ChEBI mappings. HMDB HTML/XML returned403, the LINCS resolver failed certificate verification, and independent Reaxys contents were not recovered. These access limits leave independent exact equivalence unresolved without showing a contradiction. |
| drugcentral | https://drugcentral.org/drugcard/530; Current drug card | supports | DrugCentral530 resolves to cefazolin and the correct neutral formula. Its broader drug/synonym scope is kept in drug_xrefs, not used as proof of every formulation or current jurisdictional approval. |
| kegg-drug | https://rest.kegg.jp/get/D02299; Current drug identity | supports | D02299 resolves to cefazolin with neutral formula and the C06880 mapping. Related sodium/product forms are separately identified; no current clinical approval is inferred. |
| drugbank | https://go.drugbank.com/drugs/DB01327; Drug reference access boundary | partial | The adopted DB01327 mapping was checked against current authority context but direct DrugBank retrieval returned403; independent contents were not inspected. It remains a qualified drug-level reference. |
| patent | https://patents.google.com/patent/US3516997A/en; Description and derivative/heterocyclic side-chain preparations | context_only | The retained patent resolves to cephalosporin derivatives and salts with tetrazolyl-acetamido and heterocyclic-thiomethyl options. It is relevant synthesis/document context, not an exact xref to every product or evidence of natural cefazolin production. |
| wiki | https://en.wikipedia.org/wiki/Cefazolin; Resolved document reference | context_only | The document reference resolves to cefazolin and is not used as experimental evidence. |
| adopted-leads | Europe PMC MED core records; All ten adopted PMID titles/abstracts | context_only | PMID12569987 concerns beta-lactam IgE determinants;2083978 cephalosporin immunoassays;6176550 mouse IgE responses;28543395 cefotiam contact urticaria/cross-reactivity;29017833 is an allergy review. PMID23702270 concerns antibiotic-loaded bone-cement wear. PMID22011388 groups nafcillin/cefazolin in a retrospective MSSA comparison and24462449 is a retrospective cefazolin MSSA study. PMID27572414 is cefazolin/ertapenem synergy and4790605 the original sodium-form evaluation. Allergy, host disposition, cement mechanics and grouped treatment outcomes are not direct cefazolin PBP experiments. |
| original | https://doi.org/10.1128/aac.3.4.488; PMID4790605; original pages 488–497, especially Methods 488–489 and susceptibility results 489–493 | supports | The 1973 primary study explicitly tests cefazolin sodium against 308 isolates by broth/agar dilution and disks, with inoculum-dependent MIC/MBC differences, and treats 85 selected hospitalized patients. It establishes historical antibacterial activity without a universal modern species spectrum. Sodium-form material, media, inocula and endpoints must accompany any numeric extraction. Historical clinical response is not contemporary approval or a direct-target assay. |
| original-methods | https://pmc.ncbi.nlm.nih.gov/articles/PMC444440/; Original page 489; primary scan inspected with OCR | supports | Media vary by organism: nutrient media for Enterobacteriaceae/Pseudomonas/S. aureus and blood-supplemented Mueller-Hinton media for other tested groups. Clinical vials explicitly contain cefazolin sodium. The full page set and hashes are preserved in 214-pages-fetch-results.json; no pooled MIC/MBC range is imported as a strain-specific observation. |
| synergy | https://doi.org/10.1128/AAC.01192-16; PMID27572414; full XML Methods, Results and Tables/Figures | supports | For index MSSA rus276, the study measures cefazolin MIC 0.5 mg/L, combination checkerboard FIC 0.375 and enhanced killing with ertapenem; effects vary among MRSA strains. Pharmacokinetic models, microscopy, immune-cell assays, mouse infection and disk potentiation retain combination and host-context boundaries. Its complementary-PBP rationale is drawn from prior literature, not direct cefazolin binding measured in this study. Commercial reagent/formulation identity is not resolved to the native neutral material. |
| pbp-context | https://doi.org/10.1128/AAC.46.9.2878-2884.2002; PMID12183241; Methods PBP isolation and Results/Discussion | partial | This primary rat-abscess/isolated S. aureus study reports altered cefazolin activity after neutrophil depletion and reduced PBP2 band density after PMN exposure. PBPs are detected using labeled ampicillin or fluorescent penicillin; it does not directly measure cefazolin binding affinity. Its numerical cefazolin PBP2/PBP4 affinity statement cites Murakami 1987 rather than generating those data. It is a bounded mechanistic lead, not permission to relabel the native broad PBP assertion as primary-validated. |
| adapter | kg-microbe-sources imodulondb; 214-adapter-results.json: dataset catalog and15 searches before open-web mechanism follow-up | context_only | E. coli precise1k searches found peptidoglycan genes and ompC b2215; penicillin matched yfeW. Exact TEM/CTX-M/CMY/NmcA/PRC/LAQ/CAE/PSZ searches and P. aeruginosa precise364 PDC-3/PDC-5 searches returned no exact hits. All commands exited0, no iModulons were returned. Reference-dataset gene matches do not establish cefazolin binding/resistance and nonhits do not refute acquired determinants. |
| aro-target | https://card.mcmaster.ca/aro/3000749; Current PBP definition/publication | supports | ARO describes the taxon-dependent PBP family, transpeptidases and other PBP functions; its listed PMID3055170 is a review. Native preserves missing organism/strain/assay and PRIMARY_EVIDENCE_NEEDED, avoiding a fabricated single protein instance. |
| aro-resistance | https://card.mcmaster.ca/aro/3000873; All 13 live ARO definitions/publications;214-aro-discovery.json | supports | All native resistance concepts and exact cefazolin source edges were reviewed. Current linked primary leads were followed selectively to the original experiments; the source-specific assertions remain distinct from independently verified primary evidence. |
| tsang | https://doi.org/10.1099/mgen.0.000500; PMID33416461; Methods, Table 2 and supplementary Table S1 | supports | The paper combines genome prediction with experimental expression tests. In wild-type E. coli BW25113 carrying pGDP1, measured cefazolin MICs increase from 4 µg/mL control to &gt;256 for CMY-2/CTX-M-3/CTX-M-27 and 256 for TEM-1. This directly supports those enzyme-associated resistance claims in the expression host; it is not merely a computational association, purified-enzyme binding measurement or universal clinical-taxon prediction. |
| tsang-si | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8115898/supplementaryFiles; mgen-7-500-s002.xlsx Table S1 rows 32–40, columnsA–F | supports | Read the original XLSX raw cell values, including merged antibiotic groups: cefazolin control D32=4; CTX-M-15 D35=128; PDC-3 D38&gt;256; PDC-5 D39&gt;256µg/mL. CMY-2/CTX-M-3/CTX-M-27/TEM-1 agree with Table 2. All are E. coli BW25113 expression tests; the sheet marks Pseudomonas clinical breakpoint fields unavailable and must not supply a clinical Pseudomonas cefazolin breakpoint. Statistical weight/p-value sheets are distinct from AST Table S1. |
| ompc | https://doi.org/10.1128/aac.22.6.942; PMID6760806; original Table 3 p945, results/discussion pp944–947 | supports | In E. coli K-12, the cefazolin concentration reducing colony formation99% on Mueller-Hinton agar is2µg/mL for wild type and ompC-only or ompF-only loss,16 for ompB mutants lacking both porins, and64 for the ompF1466/ompC::Tn5 double mutant. Complementation restores susceptibility. This supports reduced permeability involving combined porin loss; it does not show wild-type OmpC or isolated ompC loss alone confers cefazolin resistance. Endpoint is99% colony inhibition, not a modern clinical breakpoint. |
| nmca | https://doi.org/10.1073/pnas.91.16.7693; PMID8052644; original pages7693–7697 | partial | This paper characterizes nmcA/nmcR from E. cloacae NOR-1, cloned constructs and regulation of carbapenem hydrolysis. Its inspected readouts focus on imipenem/ampicillin and sequence/regulation; no cefazolin-specific result was established from these pages. Reference 5, Nordmann 1993 AAC37:939–946, is a concrete earlier biochemical follow-up. Native NmcA remains an explicitly database-supported assertion, not independently primary-confirmed here. |
| prc | https://doi.org/10.3389/fmicb.2021.732932; PMID34975778; Methods and Tables3–4 | supports | PRC-1 from Pseudomonas wenzhouensis A20 increases cefazolin MIC fourfold in the E. coli DH5α expression system (4 versus1µg/mL), and purified PRC-1 hydrolyzes cefazolin. The wild isolate MIC 256 is not attributable solely to that determinant, as the paper itself notes. Experimental MIC change and hydrolysis are distinct from extrapolated clinical resistance thresholds. |
| laq | https://doi.org/10.3389/fmicb.2022.990736; PMID36504772; Methods, Tables3–4 and kinetic results | supports | LAQ-1 from Lelliottia amnigena P13 was cloned into E. coli DH5α; cefazolin MIC rises fourfold relative to the controls, and purified LAQ-1 hydrolysis is measured. Native qualitative inactivation context is supported; neither the source taxon nor catalytic efficiency makes this a species-wide clinical susceptibility claim. |
| cae | https://doi.org/10.1038/s41598-023-28312-w; PMID36869066; Methods, Table 2 and discussion | supports | CAE-1 from Comamonas aquatica SCLZS63 confers elevated cefazolin MIC in E. coli DH5α (≥64 versus≤2µg/mL vector control). Purification attempts failed, so this paper does not supply purified CAE-1 hydrolysis kinetics. The cloned determinant supports resistance with the assay boundary retained. |
| psz | https://doi.org/10.3389/fmicb.2023.1222703; PMID37529328; Table 2 and enzyme-kinetic section/Table 5 | supports | PSZ-1 from Pantoea endophytica X85 increases cefazolin MIC in E. coli DH5α from 1 to 32µg/mL and purified-enzyme assays support hydrolysis. Kinetic efficiency numbers differ between the narrative and Table 5; no disputed constant is transferred. Native contains no such quantitative datum, so this source inconsistency is not a demonstrated native defect. |
| taxa | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=562,573,548,546&amp;retmode=xml; Current taxonomy records | supports | Current IDs562,573,548,546 resolve to E. coli, K. pneumoniae, K. aerogenes and C. freundii respectively; all native activity labels agree. |
| search | Ignored-inclusive repository and public follow-up; 214-owner-hits.txt; exact label, slug, ChEBI/ARO IDs and key | context_only | Search included ignored and hidden files outside .git/.venv. Native, raw, code/config and historical leads were distinguished. Adjacent NCBI AST maps do not own the seven curated CDC observations. Relevant PBP/resistance claims received structured adapter follow-up before open-web primary retrieval. |
| gates | Actual focused native checks; 214-focused-results.json;214-validation.tsv | supports | Schema, strict and source-aware chemistry pass. All 26 expanded captured input hashes were rechecked unchanged. |
| cdc-1 | https://wwwn.cdc.gov/ARIsolateBank/Panel/Isolatedetail?IsolateID=349&amp;PanelID=10; AR Bank isolate0349;cefazolin row and susceptibility footer | supports | Live page verifies Escherichia coli, isolate0349, BioSampleSAMN11953777, cefazolin &gt;8µg/mL with R, modal broth-microdilution MIC and stated CLSI2025 M100 S35 interpretation. Native &gt;8mg/L is the identical concentration with the right-censoring qualifier preserved. |
| biosample-1 | https://www.ncbi.nlm.nih.gov/biosample/SAMN11953777; Current organism and sample/strain attributes | supports | The linked BioSample confirms current Escherichia coli and the sample/strain or study linkage for CDC isolate0349; identifiers refer to the same deposited sample rather than implying species-wide resistance. |
| cdc-2 | https://wwwn.cdc.gov/ARIsolateBank/Panel/Isolatedetail?IsolateID=497&amp;PanelID=10; AR Bank isolate0497;cefazolin row and susceptibility footer | supports | Live page verifies Klebsiella pneumoniae, isolate0497, BioSampleSAMN11953783, cefazolin &gt;8µg/mL with R, modal broth-microdilution MIC and stated CLSI2025 M100 S35 interpretation. Native &gt;8mg/L is the identical concentration with the right-censoring qualifier preserved. |
| biosample-2 | https://www.ncbi.nlm.nih.gov/biosample/SAMN11953783; Current organism and sample/strain attributes | supports | The linked BioSample confirms current Klebsiella pneumoniae and the sample/strain or study linkage for CDC isolate0497; identifiers refer to the same deposited sample rather than implying species-wide resistance. |
| cdc-3 | https://wwwn.cdc.gov/ArIsolateBank/panel/IsolateDetail?IsolateID=74&amp;PanelID=1168; AR Bank isolate0074;cefazolin row and susceptibility footer | supports | Live page verifies Klebsiella aerogenes, isolate0074, BioSampleSAMN04014915, cefazolin &gt;8µg/mL with R, modal broth-microdilution MIC and stated CLSI2025 M100 S35 interpretation. Native &gt;8mg/L is the identical concentration with the right-censoring qualifier preserved. |
| biosample-3 | https://www.ncbi.nlm.nih.gov/biosample/SAMN04014915; Current organism and sample/strain attributes | supports | The linked BioSample confirms current Klebsiella aerogenes and the sample/strain or study linkage for CDC isolate0074; identifiers refer to the same deposited sample rather than implying species-wide resistance. |
| cdc-4 | https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=346&amp;PanelID=10; AR Bank isolate0346;cefazolin row and susceptibility footer | supports | Live page verifies Escherichia coli, isolate0346, BioSampleSAMN11953774, cefazolin &gt;8µg/mL with R, modal broth-microdilution MIC and stated CLSI2025 M100 S35 interpretation. Native &gt;8mg/L is the identical concentration with the right-censoring qualifier preserved. |
| biosample-4 | https://www.ncbi.nlm.nih.gov/biosample/SAMN11953774; Current organism and sample/strain attributes | supports | The linked BioSample confirms current Escherichia coli and the sample/strain or study linkage for CDC isolate0346; identifiers refer to the same deposited sample rather than implying species-wide resistance. |
| cdc-5 | https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=10046&amp;PanelID=10; AR Bank isolate0637;cefazolin row and susceptibility footer | supports | Live page verifies Citrobacter freundii, isolate0637, BioSampleSAMN10055345, cefazolin &gt;8µg/mL with R, modal broth-microdilution MIC and stated CLSI2025 M100 S35 interpretation. Native &gt;8mg/L is the identical concentration with the right-censoring qualifier preserved. |
| biosample-5 | https://www.ncbi.nlm.nih.gov/biosample/SAMN10055345; Current organism and sample/strain attributes | supports | The linked BioSample confirms current C. freundii and sample/strain CVMN17EC0232. Its legacy title includes E. coli, but the current organism and CDC accession link agree; AR Bank0637 is a separate collection label, not a contradictory sample identity. |
| cdc-6 | https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=495&amp;PanelID=10; AR Bank isolate0495;cefazolin row and susceptibility footer | supports | Live page verifies Escherichia coli, isolate0495, BioSampleSAMN11953781, cefazolin &gt;8µg/mL with R, modal broth-microdilution MIC and stated CLSI2025 M100 S35 interpretation. Native &gt;8mg/L is the identical concentration with the right-censoring qualifier preserved. |
| biosample-6 | https://www.ncbi.nlm.nih.gov/biosample/SAMN11953781; Current organism and sample/strain attributes | supports | The linked BioSample confirms current Escherichia coli and the sample/strain or study linkage for CDC isolate0495; identifiers refer to the same deposited sample rather than implying species-wide resistance. |
| cdc-7 | https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=538&amp;PanelID=10; AR Bank isolate0538;cefazolin row and susceptibility footer | supports | Live page verifies Escherichia coli, isolate0538, BioSampleSAMN11953785, cefazolin &gt;8µg/mL with R, modal broth-microdilution MIC and stated CLSI2025 M100 S35 interpretation. Native &gt;8mg/L is the identical concentration with the right-censoring qualifier preserved. |
| biosample-7 | https://www.ncbi.nlm.nih.gov/biosample/SAMN11953785; Current organism and sample/strain attributes | supports | The linked BioSample confirms current Escherichia coli and the sample/strain or study linkage for CDC isolate0538; identifiers refer to the same deposited sample rather than implying species-wide resistance. |

## Limits And Additional Notes

- Independent full registry detail was unavailable for HMDB0015422, LSM-34744, Reaxys4169371 and DrugBank DB01327; current authority mappings do not remove that access limit.
- All ten adopted compound-level PMID titles/abstracts were inspected. Original 1973 pages and full 2016 primary text were read, but not every allergy/clinical/bone-cement article in full. Current ARO-linked lead metadata and selected original experiments were reviewed, not every cited enzyme paper exhaustively.
- NmcA-specific cefazolin primary assay support was not established from the inspected 1994 paper; the current exact database assertion remains qualified.
- The inspected 2002 PBP study uses labeled ampicillin/penicillin to detect proteins and cites earlier cefazolin binding data. Direct cefazolin PBP assay details remain to be independently verified before primary upgrade.
- Neutral graph identity does not establish the exact salt/hydrate of every commercial assay reagent; 1973 explicitly uses sodium and 2016 commercial preparations are not fully resolved.
- PSZ-1 kinetic text/Table 5 disagree; no conflicting numeric constant was adopted. Historical clinical and animal results do not establish present-day approval or treatment advice.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 26 expanded input hashes unchanged; initial captures retained. No native/source/status/history edits.
- Focused schema/strict used022 own locked environment. Chemistry and independent KEGG MOL used019 locked RDKit 2026.03.5 against 022 cwd.
- Free public retrieval only. SomePMC direct file routes returned challenge pages; actual2021supplements were retrieved from the EuropePMC supplementary ZIP and inspected. Challenge responses are not used as primary source text.
- The live CDC page footer itself supplies the cited2025 CLSI edition; this review does not infer it from the current calendar year.
- All source snapshots and manifests remain in session scratch; hashes and actual access timestamps are attached to evidence entries.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T111425Z-cefazolin
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cefazolin: exact identity, seven verified CDC MIC observations and qualified
  resistance evidence'
started_at: '2026-10-21T10:55:30Z'
finished_at: '2026-10-21T11:14:25Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independent complete native/source-owner review; current chemical
    and taxon authorities; structured adapter before mechanism web follow-up; all
    ten adopted PMID leads; original 1973, 1982 and 1994 pages plus 2016, 2021 and
    newer primary resistance studies and supplementary data.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: No confirmed native defect. Exact neutral cefazolin, source mints and publicly
  resolved structure mappings agree. All seven curator-owned CDC rows retain the correct
  censored MIC, modal broth method, stated 2025 interpretation and current BioSample/taxon
  mapping. The PBP and thirteen resistance entries are explicitly database assertions,
  not primary-validated claims. Inspected primary studies support several resistance
  mechanisms with important expression-host, porin-loss and assay boundaries; NmcA-specific
  cefazolin evidence and some registry detail remain unresolved. Scientific assessment
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
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
    role: context
  - path: conf/sources.yaml
    sha256: 4a2dcd7a3a88953b6cb35b51a48ed77b626c3af2cbb542b0d38ba10540ed7df9
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: curation/curator_antibiotics.tsv
    sha256: 224cbb7261add427184b2762a29c2ff3e85c85e0a06cf22b144545346487247b
    role: context
  - path: curation/decisions.tsv
    sha256: a5834b44307b0449b0df9362c551b7fcd707f3ae51f73d429d37d51f5a169d61
    role: context
  - path: data/antibiotics/antibacterial/cefazolin.yaml
    sha256: f9e6d4e80b1da1e778b143d089248545ff33c884ed534ee2626b87e8dc41debc
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
  - path: scripts/card_evidence_reviews.py
    sha256: f9ec8aff30066bf04b9c2757af7d6f5d179d045e57b9f3b352bbed0b851f50a8
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
- target_id: CHEBI:474053
  path: data/antibiotics/antibacterial/cefazolin.yaml
  label: cefazolin
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
    path: data/raw/aro_target_edges.tsv
    role: Imported ARO target assertion
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Imported ARO resistance assertions
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Target role mapping
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Source claim review decisions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Maintained source claim decision application
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefazolin.yaml
    role: Curator-owned CDC activity_spectrum observations and history
scope:
  description: Whole-record review of neutral cefazolin, including all populated activity
    and resistance fields.
  selection: Queue 214 in isolated batch 022; initial captures preserved and actual
    ARO/source/curator owners appended before detailed judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:474053
  exclusions:
  - target: Cefazolin sodium/hydrates, ertapenem combinations, comparator cephalosporins
      and untested gene variants
    reason: Related materials or interventions are kept distinct from the exact neutral
      graph and from cefazolin monotherapy.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual focused command passed with zero errors.
  target_ids:
  - CHEBI:474053
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefazolin.yaml
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
  - CHEBI:474053
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefazolin.yaml --out /private/tmp/am-review-session/214-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Independent molecular encodings and source mints
  status: passed
  required: true
  summary: Both molecular encodings, complete key, formula, charge, masses, two R
    centres and both source mints agree.
  target_ids:
  - CHEBI:474053
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/check199200.py
    214 (cwd /private/tmp/antibioticmech-record-reviews-022)
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
  - CHEBI:474053
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
  - CHEBI:474053
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
  - CHEBI:474053
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
  - CHEBI:474053
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
  - CHEBI:474053
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
  - CHEBI:474053
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
  - CHEBI:474053
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
  - CHEBI:474053
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
  - CHEBI:474053
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/cefazolin.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T11:10:52Z'
  support: supports
  summary: Read identity/definition, synonyms, five parents, roles, chemical graph
    and all exact/drug/document xrefs; seven activity_spectrum rows; thirteen resistance
    mechanisms; one explicitly PRIMARY_EVIDENCE_NEEDED PBP target; both source concepts;
    all fifteen history events. No populated producer, clinical-status, mode or causal_graph
    fields.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv;
    data/raw/aro_resistance_edges.tsv
  locator: ChEBI row2971; ARO inventory43; target44; resistance1385–1397; conf/aro_target_roles.tsv
    row30
  accessed_at: '2026-10-21T11:10:52Z'
  support: supports
  summary: Identity and eight ChEBI PMID leads plus two ARO PMID leads match native
    provenance. All thirteen exact cefazolin resistance edges and the PBP edge/role
    match the imported database assertions. CDC rows are curator-owned within the
    actual record, not inferred to be generated from adjacent NCBI AST inventories.
    Actual owners were captured before judgment.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:474053
  locator: Current identity, chemical parents and role assertions
  accessed_at: '2026-10-21T11:01:16Z'
  support: supports
  summary: Current ChEBI matches neutral C14H14N8O4S3 and full key MLYYVTUWGNIJIB-BXKDBHETSA-N.
    Chemical parents are cephalosporin, tetrazoles and thiadiazoles; beta-lactam antibiotic
    allergen is an additional biological classification, not a structural class. Antibiotic/antibacterial
    roles and the structural definition are coherent.
  snapshot_sha256: a26e95e45a229fed68b67db3aaa37bd8ee66c46420eaffabde856dcb3b0126f0
- evidence_id: aro
  kind: authority
  reference: https://card.mcmaster.ca/aro/0000058
  locator: Current drug identity
  accessed_at: '2026-10-21T11:01:16Z'
  support: supports
  summary: Current ARO identifies cefazolin as a first-generation cephalosporin. Native
    database target/resistance status is retained; the authority is not substituted
    for primary assay details.
  snapshot_sha256: ae8e4f784fb2c6a4043a77842bfa379ec1b2d0eea62f3757cb7037623057751e
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit 2026.03.5 checks
  locator: 214-chemistry.json
  accessed_at: '2026-10-21T11:00:42Z'
  support: supports
  summary: SMILES and InChI independently produce the same neutral single-fragment
    graph, complete key, formula, average/exact masses and two R centres. Both source-specific
    minted identifiers are correct.
  snapshot_sha256: 3b002eadcaa3a391aa4325185b812064a1f2ff7a914bb4b5058ff32763dcf60f
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/33255
  locator: Current complete PUG structure
  accessed_at: '2026-10-21T11:01:17Z'
  support: supports
  summary: CID33255 matches the full native graph and stereochemical key, including
    both heterocyclic side chains.
  snapshot_sha256: 91ec8e4cbbb6d85428a288e44b988fccfed8984e90bafa09bda6246af384f88c
- evidence_id: chembl
  kind: database
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL1435.json
  locator: Current exact molecule
  accessed_at: '2026-10-21T11:01:17Z'
  support: supports
  summary: CHEMBL1435 matches the neutral formula and full key; no hydrate or salt
    conflation was found.
  snapshot_sha256: da5e53878f03dd34345cd7bc2b139fc6ee75da304e17f383c60b32cfc4b43843
- evidence_id: cas
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/25953-19-9/property/InChIKey/JSON
  locator: CAS-name resolution
  accessed_at: '2026-10-21T11:01:17Z'
  support: supports
  summary: CAS25953-19-9 resolves to the exact CID33255 structure/key.
  snapshot_sha256: f31211ff6a2fbc40b1d1f25a0a601543b6c9ef5902fa2296e86860b39096bc4e
- evidence_id: kegg-compound
  kind: database
  reference: https://rest.kegg.jp/get/C06880/mol
  locator: Current MOL independently parsed
  accessed_at: '2026-10-21T11:01:25Z'
  support: supports
  summary: KEGG C06880 has the correct formula and its MOL generates the complete
    native key using the locked 019 RDKit interpreter against 022 cwd; result captured
    in 214-kegg-check.json.
  snapshot_sha256: e7efeecbf333af7acad74db0d84a89c5b3aa15bd12b62553bd40f2f9e5a9712e
- evidence_id: vsdb
  kind: database
  reference: https://bioregistry.io/vsdb:1910
  locator: Resolved Veterinary Substances Database record1910
  accessed_at: '2026-10-21T11:04:11Z'
  support: supports
  summary: The resolved entry explicitly describes cefazolin acid and provides the
    exact native formula, InChI and key. Sodium pentahydrate is listed separately
    as a variant, so this native exact xref is not a salt mismatch.
  snapshot_sha256: 4f2cd159d2a8fff403ed76e07cb0ff14898d2ed1128c170ae4398b67348b7981
- evidence_id: registry-limits
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:474053
  locator: HMDB0015422, LSM-34744 and Reaxys4169371 mappings
  accessed_at: '2026-10-21T11:01:16Z'
  support: partial
  summary: These identifiers remain live ChEBI mappings. HMDB HTML/XML returned403,
    the LINCS resolver failed certificate verification, and independent Reaxys contents
    were not recovered. These access limits leave independent exact equivalence unresolved
    without showing a contradiction.
  snapshot_sha256: a26e95e45a229fed68b67db3aaa37bd8ee66c46420eaffabde856dcb3b0126f0
- evidence_id: drugcentral
  kind: database
  reference: https://drugcentral.org/drugcard/530
  locator: Current drug card
  accessed_at: '2026-10-21T11:01:17Z'
  support: supports
  summary: DrugCentral530 resolves to cefazolin and the correct neutral formula. Its
    broader drug/synonym scope is kept in drug_xrefs, not used as proof of every formulation
    or current jurisdictional approval.
  snapshot_sha256: c5c28652da662ed7304389590e5ac059d015d03da57a1062e9c2792f9e6a4cdf
- evidence_id: kegg-drug
  kind: database
  reference: https://rest.kegg.jp/get/D02299
  locator: Current drug identity
  accessed_at: '2026-10-21T11:01:17Z'
  support: supports
  summary: D02299 resolves to cefazolin with neutral formula and the C06880 mapping.
    Related sodium/product forms are separately identified; no current clinical approval
    is inferred.
  snapshot_sha256: b6f583c21c97cc41af2618d65ed4af0d437b1ea066dc14d7d170a13c6f84e39f
- evidence_id: drugbank
  kind: authority
  reference: https://go.drugbank.com/drugs/DB01327
  locator: Drug reference access boundary
  accessed_at: '2026-10-21T11:01:25Z'
  support: partial
  summary: The adopted DB01327 mapping was checked against current authority context
    but direct DrugBank retrieval returned403; independent contents were not inspected.
    It remains a qualified drug-level reference.
  snapshot_sha256: fd3e5f7c9afdae0c7f4b78a1b409382b4d5659eb3d1cb1c10885f9f8ab16bcbe
- evidence_id: patent
  kind: primary_source
  reference: https://patents.google.com/patent/US3516997A/en
  locator: Description and derivative/heterocyclic side-chain preparations
  accessed_at: '2026-10-21T11:01:18Z'
  support: context_only
  summary: The retained patent resolves to cephalosporin derivatives and salts with
    tetrazolyl-acetamido and heterocyclic-thiomethyl options. It is relevant synthesis/document
    context, not an exact xref to every product or evidence of natural cefazolin production.
  snapshot_sha256: 7a0059abff80b4ceed972bde52e7d9841a0f61fd115be37da48a4ab3ae32eff3
- evidence_id: wiki
  kind: database
  reference: https://en.wikipedia.org/wiki/Cefazolin
  locator: Resolved document reference
  accessed_at: '2026-10-21T11:01:18Z'
  support: context_only
  summary: The document reference resolves to cefazolin and is not used as experimental
    evidence.
  snapshot_sha256: 9c99d575ffccfa7142ffb429f14a86941089c79afc4f6e804f8c554e0c0dd996
- evidence_id: adopted-leads
  kind: database
  reference: Europe PMC MED core records
  locator: All ten adopted PMID titles/abstracts
  accessed_at: '2026-10-21T11:01:14Z'
  support: context_only
  summary: PMID12569987 concerns beta-lactam IgE determinants;2083978 cephalosporin
    immunoassays;6176550 mouse IgE responses;28543395 cefotiam contact urticaria/cross-reactivity;29017833
    is an allergy review. PMID23702270 concerns antibiotic-loaded bone-cement wear.
    PMID22011388 groups nafcillin/cefazolin in a retrospective MSSA comparison and24462449
    is a retrospective cefazolin MSSA study. PMID27572414 is cefazolin/ertapenem synergy
    and4790605 the original sodium-form evaluation. Allergy, host disposition, cement
    mechanics and grouped treatment outcomes are not direct cefazolin PBP experiments.
  snapshot_sha256: b71939c98bfcab688c680d7a3e51534a2ab767036c758bbdd58e89e56785486d
- evidence_id: original
  kind: primary_source
  reference: https://doi.org/10.1128/aac.3.4.488
  locator: PMID4790605; original pages 488–497, especially Methods 488–489 and susceptibility
    results 489–493
  accessed_at: '2026-10-21T11:06:44Z'
  support: supports
  summary: The 1973 primary study explicitly tests cefazolin sodium against 308 isolates
    by broth/agar dilution and disks, with inoculum-dependent MIC/MBC differences,
    and treats 85 selected hospitalized patients. It establishes historical antibacterial
    activity without a universal modern species spectrum. Sodium-form material, media,
    inocula and endpoints must accompany any numeric extraction. Historical clinical
    response is not contemporary approval or a direct-target assay.
  snapshot_sha256: 7382cd0243c8035d212246284ee37dc4b1cdc1e889f522a0b18497df42e1c945
- evidence_id: original-methods
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC444440/
  locator: Original page 489; primary scan inspected with OCR
  accessed_at: '2026-10-21T11:06:44Z'
  support: supports
  summary: 'Media vary by organism: nutrient media for Enterobacteriaceae/Pseudomonas/S.
    aureus and blood-supplemented Mueller-Hinton media for other tested groups. Clinical
    vials explicitly contain cefazolin sodium. The full page set and hashes are preserved
    in 214-pages-fetch-results.json; no pooled MIC/MBC range is imported as a strain-specific
    observation.'
  snapshot_sha256: 4df86cc268cc40bdfdffc70b0cc9c048bdf3e68fbe4c22557e44e5798fc290e5
- evidence_id: synergy
  kind: primary_source
  reference: https://doi.org/10.1128/AAC.01192-16
  locator: PMID27572414; full XML Methods, Results and Tables/Figures
  accessed_at: '2026-10-21T11:02:06Z'
  support: supports
  summary: For index MSSA rus276, the study measures cefazolin MIC 0.5 mg/L, combination
    checkerboard FIC 0.375 and enhanced killing with ertapenem; effects vary among
    MRSA strains. Pharmacokinetic models, microscopy, immune-cell assays, mouse infection
    and disk potentiation retain combination and host-context boundaries. Its complementary-PBP
    rationale is drawn from prior literature, not direct cefazolin binding measured
    in this study. Commercial reagent/formulation identity is not resolved to the
    native neutral material.
  snapshot_sha256: 3e127c3cd8785427cea43f91a20ae6bf8169840f462105964a6d4848369f9452
- evidence_id: pbp-context
  kind: primary_source
  reference: https://doi.org/10.1128/AAC.46.9.2878-2884.2002
  locator: PMID12183241; Methods PBP isolation and Results/Discussion
  accessed_at: '2026-10-21T11:08:03Z'
  support: partial
  summary: This primary rat-abscess/isolated S. aureus study reports altered cefazolin
    activity after neutrophil depletion and reduced PBP2 band density after PMN exposure.
    PBPs are detected using labeled ampicillin or fluorescent penicillin; it does
    not directly measure cefazolin binding affinity. Its numerical cefazolin PBP2/PBP4
    affinity statement cites Murakami 1987 rather than generating those data. It is
    a bounded mechanistic lead, not permission to relabel the native broad PBP assertion
    as primary-validated.
  snapshot_sha256: c0e5b746052171d7d0fa9f1c2dac7dc069171ff102af1116d638ab5f0944be98
- evidence_id: adapter
  kind: search
  reference: kg-microbe-sources imodulondb
  locator: '214-adapter-results.json: dataset catalog and15 searches before open-web
    mechanism follow-up'
  accessed_at: '2026-10-21T11:00:47Z'
  support: context_only
  summary: E. coli precise1k searches found peptidoglycan genes and ompC b2215; penicillin
    matched yfeW. Exact TEM/CTX-M/CMY/NmcA/PRC/LAQ/CAE/PSZ searches and P. aeruginosa
    precise364 PDC-3/PDC-5 searches returned no exact hits. All commands exited0,
    no iModulons were returned. Reference-dataset gene matches do not establish cefazolin
    binding/resistance and nonhits do not refute acquired determinants.
  snapshot_sha256: eb17ef333d00f48dbaf2f784d052f90bbdce3706aada231849bd4c877ff5ba85
  search_scope: Live iModulonDB catalog; E. coli precise1k searches for penicillin,
    peptidoglycan, OmpC and exact named enzymes; P. aeruginosa precise364 PDC-3/PDC-5
    searches on 2026-10-21. All commands and output captured in 214-adapter-results.json.
- evidence_id: aro-target
  kind: authority
  reference: https://card.mcmaster.ca/aro/3000749
  locator: Current PBP definition/publication
  accessed_at: '2026-10-21T11:01:24Z'
  support: supports
  summary: ARO describes the taxon-dependent PBP family, transpeptidases and other
    PBP functions; its listed PMID3055170 is a review. Native preserves missing organism/strain/assay
    and PRIMARY_EVIDENCE_NEEDED, avoiding a fabricated single protein instance.
  snapshot_sha256: 93a272f1d7ffe47e4c8a1d8e6490bc4b765f791f22029090c6b0f4e877f97ec1
- evidence_id: aro-resistance
  kind: authority
  reference: https://card.mcmaster.ca/aro/3000873
  locator: All 13 live ARO definitions/publications;214-aro-discovery.json
  accessed_at: '2026-10-21T11:02:04Z'
  support: supports
  summary: All native resistance concepts and exact cefazolin source edges were reviewed.
    Current linked primary leads were followed selectively to the original experiments;
    the source-specific assertions remain distinct from independently verified primary
    evidence.
  snapshot_sha256: abbb2bf38967778379d67be2fb15964cc6185e0cb1f13b94a83d1dd90477871b
- evidence_id: tsang
  kind: primary_source
  reference: https://doi.org/10.1099/mgen.0.000500
  locator: PMID33416461; Methods, Table 2 and supplementary Table S1
  accessed_at: '2026-10-21T11:04:10Z'
  support: supports
  summary: The paper combines genome prediction with experimental expression tests.
    In wild-type E. coli BW25113 carrying pGDP1, measured cefazolin MICs increase
    from 4 µg/mL control to >256 for CMY-2/CTX-M-3/CTX-M-27 and 256 for TEM-1. This
    directly supports those enzyme-associated resistance claims in the expression
    host; it is not merely a computational association, purified-enzyme binding measurement
    or universal clinical-taxon prediction.
  snapshot_sha256: 20de54b193f86d76e5985b4aadbe8442d7ded8a30d6a15f0050c7e1d76f8dd18
- evidence_id: tsang-si
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8115898/supplementaryFiles
  locator: mgen-7-500-s002.xlsx Table S1 rows 32–40, columnsA–F
  accessed_at: '2026-10-21T11:07:05Z'
  support: supports
  summary: 'Read the original XLSX raw cell values, including merged antibiotic groups:
    cefazolin control D32=4; CTX-M-15 D35=128; PDC-3 D38>256; PDC-5 D39>256µg/mL.
    CMY-2/CTX-M-3/CTX-M-27/TEM-1 agree with Table 2. All are E. coli BW25113 expression
    tests; the sheet marks Pseudomonas clinical breakpoint fields unavailable and
    must not supply a clinical Pseudomonas cefazolin breakpoint. Statistical weight/p-value
    sheets are distinct from AST Table S1.'
  snapshot_sha256: f9f50b217f59adce0f8270496d0b54ec52eaa4aaad45b24d6d383336d34639da
- evidence_id: ompc
  kind: primary_source
  reference: https://doi.org/10.1128/aac.22.6.942
  locator: PMID6760806; original Table 3 p945, results/discussion pp944–947
  accessed_at: '2026-10-21T11:06:45Z'
  support: supports
  summary: In E. coli K-12, the cefazolin concentration reducing colony formation99%
    on Mueller-Hinton agar is2µg/mL for wild type and ompC-only or ompF-only loss,16
    for ompB mutants lacking both porins, and64 for the ompF1466/ompC::Tn5 double
    mutant. Complementation restores susceptibility. This supports reduced permeability
    involving combined porin loss; it does not show wild-type OmpC or isolated ompC
    loss alone confers cefazolin resistance. Endpoint is99% colony inhibition, not
    a modern clinical breakpoint.
  snapshot_sha256: c873e025b14dd953e87f28429fa16ee5a0909fccce00b2a6d4fdf3057a31f0c9
- evidence_id: nmca
  kind: primary_source
  reference: https://doi.org/10.1073/pnas.91.16.7693
  locator: PMID8052644; original pages7693–7697
  accessed_at: '2026-10-21T11:06:45Z'
  support: partial
  summary: This paper characterizes nmcA/nmcR from E. cloacae NOR-1, cloned constructs
    and regulation of carbapenem hydrolysis. Its inspected readouts focus on imipenem/ampicillin
    and sequence/regulation; no cefazolin-specific result was established from these
    pages. Reference 5, Nordmann 1993 AAC37:939–946, is a concrete earlier biochemical
    follow-up. Native NmcA remains an explicitly database-supported assertion, not
    independently primary-confirmed here.
  snapshot_sha256: 89265b0b0d402aa105c668ca3496ee99711e125e9e26dad60a4bba73cf9aa3ef
- evidence_id: prc
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2021.732932
  locator: PMID34975778; Methods and Tables3–4
  accessed_at: '2026-10-21T11:04:10Z'
  support: supports
  summary: PRC-1 from Pseudomonas wenzhouensis A20 increases cefazolin MIC fourfold
    in the E. coli DH5α expression system (4 versus1µg/mL), and purified PRC-1 hydrolyzes
    cefazolin. The wild isolate MIC 256 is not attributable solely to that determinant,
    as the paper itself notes. Experimental MIC change and hydrolysis are distinct
    from extrapolated clinical resistance thresholds.
  snapshot_sha256: eb7f65de5054a781295c7716f69206e3ecfd56998768a957fd23b44822c6d7e6
- evidence_id: laq
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2022.990736
  locator: PMID36504772; Methods, Tables3–4 and kinetic results
  accessed_at: '2026-10-21T11:04:10Z'
  support: supports
  summary: LAQ-1 from Lelliottia amnigena P13 was cloned into E. coli DH5α; cefazolin
    MIC rises fourfold relative to the controls, and purified LAQ-1 hydrolysis is
    measured. Native qualitative inactivation context is supported; neither the source
    taxon nor catalytic efficiency makes this a species-wide clinical susceptibility
    claim.
  snapshot_sha256: 50ce65bce662993c908c2bc201beefcc6583b435d3784a20a3c2ee39990ee2df
- evidence_id: cae
  kind: primary_source
  reference: https://doi.org/10.1038/s41598-023-28312-w
  locator: PMID36869066; Methods, Table 2 and discussion
  accessed_at: '2026-10-21T11:04:10Z'
  support: supports
  summary: CAE-1 from Comamonas aquatica SCLZS63 confers elevated cefazolin MIC in
    E. coli DH5α (≥64 versus≤2µg/mL vector control). Purification attempts failed,
    so this paper does not supply purified CAE-1 hydrolysis kinetics. The cloned determinant
    supports resistance with the assay boundary retained.
  snapshot_sha256: ed309640fafcce7ec4bd7846dd93742f6b867dd477cd1c6e66d7e2c15348e971
- evidence_id: psz
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2023.1222703
  locator: PMID37529328; Table 2 and enzyme-kinetic section/Table 5
  accessed_at: '2026-10-21T11:04:11Z'
  support: supports
  summary: PSZ-1 from Pantoea endophytica X85 increases cefazolin MIC in E. coli DH5α
    from 1 to 32µg/mL and purified-enzyme assays support hydrolysis. Kinetic efficiency
    numbers differ between the narrative and Table 5; no disputed constant is transferred.
    Native contains no such quantitative datum, so this source inconsistency is not
    a demonstrated native defect.
  snapshot_sha256: b369c8cd9258c2355f354e8ae9259990f76befb99034b0ef43a67a2f3d4b03fb
- evidence_id: taxa
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=562,573,548,546&retmode=xml
  locator: Current taxonomy records
  accessed_at: '2026-10-21T11:04:11Z'
  support: supports
  summary: Current IDs562,573,548,546 resolve to E. coli, K. pneumoniae, K. aerogenes
    and C. freundii respectively; all native activity labels agree.
  snapshot_sha256: ec29b638d9d86a602f4115b03b31bac9411782bdc0a7e6111b34271986ffc4da
- evidence_id: search
  kind: search
  reference: Ignored-inclusive repository and public follow-up
  locator: 214-owner-hits.txt; exact label, slug, ChEBI/ARO IDs and key
  accessed_at: '2026-10-21T11:00:21Z'
  support: context_only
  summary: Search included ignored and hidden files outside .git/.venv. Native, raw,
    code/config and historical leads were distinguished. Adjacent NCBI AST maps do
    not own the seven curated CDC observations. Relevant PBP/resistance claims received
    structured adapter follow-up before open-web primary retrieval.
  snapshot_sha256: 7af36bd102cd3a0a1e0f7ece02aa9b3e8771279d39cd7b39db240ea442da6d29
  search_scope: rg --no-ignore --hidden across isolated batch 022 outside .git/.venv;
    exact cefazolin/CHEBI:474053/ARO:0000058/full-key search. Public ChEBI/ARO/PubChem/ChEMBL/KEGG/VSDB/CDC/NCBI/EuropePMC/PMC
    and structured iModulonDB followed on 2026-10-21.
- evidence_id: gates
  kind: validation
  reference: Actual focused native checks
  locator: 214-focused-results.json;214-validation.tsv
  accessed_at: '2026-10-21T11:00:42Z'
  support: supports
  summary: Schema, strict and source-aware chemistry pass. All 26 expanded captured
    input hashes were rechecked unchanged.
  snapshot_sha256: a55aeb9b4a6662984cf0ce28cbab1031be86fb760011c0bb680c08f6484e3844
- evidence_id: cdc-1
  kind: database
  reference: https://wwwn.cdc.gov/ARIsolateBank/Panel/Isolatedetail?IsolateID=349&PanelID=10
  locator: AR Bank isolate0349;cefazolin row and susceptibility footer
  accessed_at: '2026-10-21T11:01:18Z'
  support: supports
  summary: Live page verifies Escherichia coli, isolate0349, BioSampleSAMN11953777,
    cefazolin >8µg/mL with R, modal broth-microdilution MIC and stated CLSI2025 M100
    S35 interpretation. Native >8mg/L is the identical concentration with the right-censoring
    qualifier preserved.
  snapshot_sha256: dab6e7a6e6e4f9efd5cbff6551634ee2dfaec1bfc338c4d11737caac0ca742b5
- evidence_id: biosample-1
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/biosample/SAMN11953777
  locator: Current organism and sample/strain attributes
  accessed_at: '2026-10-21T11:01:18Z'
  support: supports
  summary: The linked BioSample confirms current Escherichia coli and the sample/strain
    or study linkage for CDC isolate0349; identifiers refer to the same deposited
    sample rather than implying species-wide resistance.
  snapshot_sha256: 47beabfba5dc7403d66eacdb32ceedfa1577421cb300c0fb9d8e06ddb2c6e569
- evidence_id: cdc-2
  kind: database
  reference: https://wwwn.cdc.gov/ARIsolateBank/Panel/Isolatedetail?IsolateID=497&PanelID=10
  locator: AR Bank isolate0497;cefazolin row and susceptibility footer
  accessed_at: '2026-10-21T11:01:18Z'
  support: supports
  summary: Live page verifies Klebsiella pneumoniae, isolate0497, BioSampleSAMN11953783,
    cefazolin >8µg/mL with R, modal broth-microdilution MIC and stated CLSI2025 M100
    S35 interpretation. Native >8mg/L is the identical concentration with the right-censoring
    qualifier preserved.
  snapshot_sha256: e8cf81e47272a937bfcf872c829274a09834fbe2dcc3df1f0e8c54d4d08ca43a
- evidence_id: biosample-2
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/biosample/SAMN11953783
  locator: Current organism and sample/strain attributes
  accessed_at: '2026-10-21T11:01:18Z'
  support: supports
  summary: The linked BioSample confirms current Klebsiella pneumoniae and the sample/strain
    or study linkage for CDC isolate0497; identifiers refer to the same deposited
    sample rather than implying species-wide resistance.
  snapshot_sha256: 5bc3cb4d741ee88770cbe313af83284b5c4a5dbfebbb39fbf4a80e8c5e5bfaaa
- evidence_id: cdc-3
  kind: database
  reference: https://wwwn.cdc.gov/ArIsolateBank/panel/IsolateDetail?IsolateID=74&PanelID=1168
  locator: AR Bank isolate0074;cefazolin row and susceptibility footer
  accessed_at: '2026-10-21T11:01:18Z'
  support: supports
  summary: Live page verifies Klebsiella aerogenes, isolate0074, BioSampleSAMN04014915,
    cefazolin >8µg/mL with R, modal broth-microdilution MIC and stated CLSI2025 M100
    S35 interpretation. Native >8mg/L is the identical concentration with the right-censoring
    qualifier preserved.
  snapshot_sha256: 2b49086b1126607d7f88de85908c61bfb214f65eaa866a6be920a8c132839d44
- evidence_id: biosample-3
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/biosample/SAMN04014915
  locator: Current organism and sample/strain attributes
  accessed_at: '2026-10-21T11:01:18Z'
  support: supports
  summary: The linked BioSample confirms current Klebsiella aerogenes and the sample/strain
    or study linkage for CDC isolate0074; identifiers refer to the same deposited
    sample rather than implying species-wide resistance.
  snapshot_sha256: 2beb5ab4c27d808379dca9ee262f6f3ff16b14413c59ecde3c0196d431836c51
- evidence_id: cdc-4
  kind: database
  reference: https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=346&PanelID=10
  locator: AR Bank isolate0346;cefazolin row and susceptibility footer
  accessed_at: '2026-10-21T11:01:18Z'
  support: supports
  summary: Live page verifies Escherichia coli, isolate0346, BioSampleSAMN11953774,
    cefazolin >8µg/mL with R, modal broth-microdilution MIC and stated CLSI2025 M100
    S35 interpretation. Native >8mg/L is the identical concentration with the right-censoring
    qualifier preserved.
  snapshot_sha256: 7c916ba78fcc44cbd4b2d20a688cb8943391ace307918eb28ac0de801b24a202
- evidence_id: biosample-4
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/biosample/SAMN11953774
  locator: Current organism and sample/strain attributes
  accessed_at: '2026-10-21T11:01:19Z'
  support: supports
  summary: The linked BioSample confirms current Escherichia coli and the sample/strain
    or study linkage for CDC isolate0346; identifiers refer to the same deposited
    sample rather than implying species-wide resistance.
  snapshot_sha256: 5d17372341d56e6aa4c90b3153a1d76016c2a5a1a5402ab0a5e761b125567795
- evidence_id: cdc-5
  kind: database
  reference: https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=10046&PanelID=10
  locator: AR Bank isolate0637;cefazolin row and susceptibility footer
  accessed_at: '2026-10-21T11:01:19Z'
  support: supports
  summary: Live page verifies Citrobacter freundii, isolate0637, BioSampleSAMN10055345,
    cefazolin >8µg/mL with R, modal broth-microdilution MIC and stated CLSI2025 M100
    S35 interpretation. Native >8mg/L is the identical concentration with the right-censoring
    qualifier preserved.
  snapshot_sha256: 59dd11f04c0e99241d4d2ea9551fb08b331441ad6ba1eeb88bcf16e4d98f8e70
- evidence_id: biosample-5
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/biosample/SAMN10055345
  locator: Current organism and sample/strain attributes
  accessed_at: '2026-10-21T11:01:19Z'
  support: supports
  summary: The linked BioSample confirms current C. freundii and sample/strain CVMN17EC0232.
    Its legacy title includes E. coli, but the current organism and CDC accession
    link agree; AR Bank0637 is a separate collection label, not a contradictory sample
    identity.
  snapshot_sha256: 7f0f65bf2080d7f72f59ad213137e70601cc68c3deb9e21be5e2494b6fe1811d
- evidence_id: cdc-6
  kind: database
  reference: https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=495&PanelID=10
  locator: AR Bank isolate0495;cefazolin row and susceptibility footer
  accessed_at: '2026-10-21T11:01:19Z'
  support: supports
  summary: Live page verifies Escherichia coli, isolate0495, BioSampleSAMN11953781,
    cefazolin >8µg/mL with R, modal broth-microdilution MIC and stated CLSI2025 M100
    S35 interpretation. Native >8mg/L is the identical concentration with the right-censoring
    qualifier preserved.
  snapshot_sha256: d4991adc8dbdcefb77052178f02d9f709f3029fd9e8edfd2b17dc97f45fa6751
- evidence_id: biosample-6
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/biosample/SAMN11953781
  locator: Current organism and sample/strain attributes
  accessed_at: '2026-10-21T11:01:19Z'
  support: supports
  summary: The linked BioSample confirms current Escherichia coli and the sample/strain
    or study linkage for CDC isolate0495; identifiers refer to the same deposited
    sample rather than implying species-wide resistance.
  snapshot_sha256: 4a526646f481e3047c951252609a3c4aeeaf6e5e46792954acaf9b99e26dbf6e
- evidence_id: cdc-7
  kind: database
  reference: https://wwwn.cdc.gov/ARIsolateBank/Panel/IsolateDetail.aspx?IsolateID=538&PanelID=10
  locator: AR Bank isolate0538;cefazolin row and susceptibility footer
  accessed_at: '2026-10-21T11:01:19Z'
  support: supports
  summary: Live page verifies Escherichia coli, isolate0538, BioSampleSAMN11953785,
    cefazolin >8µg/mL with R, modal broth-microdilution MIC and stated CLSI2025 M100
    S35 interpretation. Native >8mg/L is the identical concentration with the right-censoring
    qualifier preserved.
  snapshot_sha256: d3f7041b5731b26ba326c7bb7dd5d1c940d238371247d2277d58fafe82a5c01f
- evidence_id: biosample-7
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/biosample/SAMN11953785
  locator: Current organism and sample/strain attributes
  accessed_at: '2026-10-21T11:01:20Z'
  support: supports
  summary: The linked BioSample confirms current Escherichia coli and the sample/strain
    or study linkage for CDC isolate0538; identifiers refer to the same deposited
    sample rather than implying species-wide resistance.
  snapshot_sha256: e620ecb6f6a352265ef4cdd6eb3de7a080614cf153a3a8765df4bf346acb8f3e
assessments:
- assessment_id: identity
  area: identity
  topic: Neutral exact cefazolin
  outcome: supported
  summary: The exact free acid has coherent graph, stereochemistry, charge, formula/masses
    and source mints. Sodium formulations and database drug synonyms are not conflated
    with exact chemical equivalence.
  target_ids:
  - CHEBI:474053
  evidence_ids:
  - native
  - chebi
  - aro
  - chemistry
  - pubchem
  - chembl
  - cas
  - kegg-compound
  - vsdb
- assessment_id: grounding
  area: grounding
  topic: Parents, class and biological roles
  outcome: supported
  summary: Cephalosporin, tetrazole and thiadiazole parents fit the graph. Allergen
    is a biological classification consistent with adopted allergy context, not a
    claim that all recipients react. Antibacterial activity is directly supported
    beyond family inference.
  target_ids:
  - CHEBI:474053
  evidence_ids:
  - chebi
  - aro
  - adopted-leads
  - original
- assessment_id: xrefs
  area: grounding
  topic: Exact/drug/document placement
  outcome: unknown
  summary: Resolved public exact mappings agree, and broader drug/document references
    are appropriately separated. HMDB, LINCS, Reaxys and DrugBank detail remains access-limited.
  target_ids:
  - CHEBI:474053
  evidence_ids:
  - pubchem
  - chembl
  - cas
  - kegg-compound
  - vsdb
  - registry-limits
  - drugcentral
  - kegg-drug
  - drugbank
  - patent
  - wiki
- assessment_id: definition
  area: evidence
  topic: Structural description
  outcome: supported
  summary: The defined side-chain positions/groups and first-generation class agree
    with the graph and authorities. No unqualified clinical or species-wide mechanism
    is embedded in the definition.
  target_ids:
  - CHEBI:474053
  evidence_ids:
  - native
  - chebi
  - chemistry
- assessment_id: cdc
  area: evidence
  topic: All seven censored MIC observations
  outcome: supported
  summary: Every native CDC citation verifies the precise isolate, >8 MIC, R interpretation,
    modal broth method and 2025 footer. BioSample/current taxonomy checks agree, including
    the C. freundii sample with a legacy E. coli title. These are observed isolate
    phenotypes, not inferred causes.
  target_ids:
  - CHEBI:474053
  evidence_ids:
  - taxa
  - cdc-1
  - cdc-2
  - cdc-3
  - cdc-4
  - cdc-5
  - cdc-6
  - cdc-7
  - biosample-1
  - biosample-2
  - biosample-3
  - biosample-4
  - biosample-5
  - biosample-6
  - biosample-7
- assessment_id: pbp
  area: evidence
  topic: Broad PBP target and primary status
  outcome: unknown
  summary: The native target is an honest database assertion with PRIMARY_EVIDENCE_NEEDED
    and no fabricated protein/taxon. The2002 primary study links PBP expression and
    cefazolin efficacy but labels PBPs with other beta-lactams; its cefazolin affinity
    numbers are secondary citations. A direct cefazolin binding paper should be inspected
    before primary upgrade.
  target_ids:
  - CHEBI:474053
  evidence_ids:
  - native
  - aro-target
  - adapter
  - pbp-context
  - synergy
- assessment_id: common-enzymes
  area: evidence
  topic: Seven TEM/CTX-M/CMY/PDC assertions
  outcome: supported
  summary: Experimental 2021 Table 2/Table S1 supports elevated cefazolin MIC with
    TEM-1, CTX-M-3, CTX-M-15, CTX-M-27, CMY-2, PDC-3 and PDC-5 in the E. coli expression
    host. The native database status remains appropriate and does not imply purified
    kinetics or a Pseudomonas clinical breakpoint.
  target_ids:
  - CHEBI:474053
  evidence_ids:
  - aro-resistance
  - tsang
  - tsang-si
- assessment_id: new-enzymes
  area: evidence
  topic: PRC-1, LAQ-1, CAE-1 and PSZ-1 assay scopes
  outcome: supported
  summary: All four determinants have cefazolin-specific expression susceptibility
    evidence. PRC-1/LAQ-1/PSZ-1 also have purified hydrolysis evidence; CAE-1 does
    not. PSZ-1 kinetic text/table inconsistency precludes unqualified numeric reuse
    but does not refute native qualitative database context.
  target_ids:
  - CHEBI:474053
  evidence_ids:
  - prc
  - laq
  - cae
  - psz
- assessment_id: ompc
  area: evidence
  topic: Reduced permeability requires loss context
  outcome: supported
  summary: The source-supported mechanism is combined OmpC/OmpF loss or coordinated
    reduction, not action of wild-type OmpC. The 1982 experiment shows isolated loss
    of either porin leaves cefazolin susceptibility unchanged. Native identifies a
    database reduced-permeability assertion and gives no claim of isolated knockout
    sufficiency; optional primary annotation must state the actual condition.
  target_ids:
  - CHEBI:474053
  evidence_ids:
  - native
  - aro-resistance
  - ompc
  - adapter
- assessment_id: nmca
  area: evidence
  topic: NmcA exact cefazolin primary support
  outcome: unknown
  summary: Current authority and raw exact edge support the database assertion. The
    inspected 1994 paper establishes NmcA/regulation mainly with carbapenem/ampicillin
    readouts; exact cefazolin hydrolysis/MIC support remains a bounded follow-up,
    not a confirmed false claim.
  target_ids:
  - CHEBI:474053
  evidence_ids:
  - aro-resistance
  - nmca
- assessment_id: other-activity
  area: evidence
  topic: Historical sodium and combination evidence
  outcome: supported
  summary: 1973 sodium assays support antibacterial eligibility. 2016 synergy, clinical
    cohorts and neutrophil models remain intervention/material-specific; no combination
    or host phenotype is misassigned as neutral cefazolin monotherapy or direct binding.
  target_ids:
  - CHEBI:474053
  evidence_ids:
  - original
  - original-methods
  - synergy
  - pbp-context
  - adopted-leads
- assessment_id: clinical-producer
  area: scope
  topic: Clinical status and production
  outcome: not_applicable
  summary: Native asserts neither current regulatory status nor a natural producer.
    Historical treatment reports and precursor cephalosporin C fermentation in a derivative
    patent do not supply those missing optional claims.
  target_ids:
  - CHEBI:474053
  evidence_ids:
  - native
  - patent
  - adopted-leads
- assessment_id: provenance
  area: provenance
  topic: Actual owners and fifteen history events
  outcome: supported
  summary: Five seed/reseed events and ten curator activity/annotation events are
    coherent with the current record. Curated CDC claims remain owned by the actual
    YAML; source assertions are traced to their raw/config owners. SEEDED is retained.
  target_ids:
  - CHEBI:474053
  evidence_ids:
  - native
  - owners
  - chemistry
- assessment_id: completeness
  area: completeness
  topic: Bounded primary enrichment
  outcome: supported
  summary: Concrete primary resistance, PBP and activity leads can enrich the record
    subject to exact material and assay mapping. Empty optional domains or honest
    PRIMARY_EVIDENCE_NEEDED status alone do not create a defect.
  target_ids:
  - CHEBI:474053
  evidence_ids:
  - tsang-si
  - ompc
  - prc
  - laq
  - cae
  - psz
  - pbp-context
  - nmca
- assessment_id: schema
  area: schema
  topic: Focused validation
  outcome: supported
  summary: Schema/strict/independent chemical and source-mint checks pass. Scientific
    evidence assessment remains separate from structural validation.
  target_ids:
  - CHEBI:474053
  evidence_ids:
  - gates
  - chemistry
findings: []
actions:
- action_id: A1
  description: Optionally promote selected resistance assertions with primary context.
  finding_ids: []
  target_ids:
  - CHEBI:474053
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Maintained source claim adjudication
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefazolin.yaml
    role: Curator-owned primary evidence and assay qualifiers via validated writer
  acceptance_checks:
  - Use2021 Table S1 exact rows 32–40 for named genes; preserve E. coli BW25113/pGDP1
    expression host, MIC units/qualifiers and control, and do not invent a cefazolin
    breakpoint for P. aeruginosa.
  - For OmpC, explicitly encode coordinated porin loss/reduction and E. coli K-12
    context; do not say isolated ompC loss or wild-type OmpC alone confers resistance.
    Keep99% colony-inhibition endpoint distinct from standard MIC.
  - Distinguish cloned-gene susceptibility shifts from purified hydrolysis. CAE-1
    has no successful purification/kinetic measurement in the inspected primary paper.
  - Adjudicate PSZ-1Table 5 versus narrative before adopting any kinetic constant;
    keep PRC-1/LAQ-1 experimental MIC changes distinct from clinical resistant classification.
  - Retrieve the earlier NmcA biochemical paper cited as Nordmann 1993 AAC 37:939–946
    or another direct exact-drug experiment before marking NmcA cefazolin support
    primary-verified.
  - Keep observed CDC isolate resistance distinct from assigning a particular causal
    determinant without matched genomic/functional evidence.
- action_id: A2
  description: Optionally complete direct PBP evidence and access-limited identity
    corroboration.
  finding_ids: []
  target_ids:
  - CHEBI:474053
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefazolin.yaml
    role: Curator-owned molecular target/evidence context
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Source-owned exact xref mappings
  acceptance_checks:
  - Follow Murakami 1987 AAC 31:1307–1311 cited by Bamberger 2002, or another exact
    cefazolin competition/acylation assay; inspect original organism, protein preparation,
    compound and endpoint before primary target upgrade.
  - Do not treat labeled ampicillin PBP bands, synergy rationale, iModulonDB gene
    matches or class-level review statements as direct cefazolin binding measurements.
  - Corroborate HMDB0015422,LSM-34744,Reaxys4169371 andDrugBankDB01327 when freely
    permissible detail is available; do not delete based on retrieval failure alone.
  - For any newly curated quantitative activity, preserve sodium/formulation scope
    and historical medium/inoculum; maintain existing CDC censored MICs and sample
    provenance.
  - Run applicable native schema/strict, evidence/term/reference/history and corpus
    gates after separately authorized curation.
limitations:
- Independent full registry detail was unavailable for HMDB0015422, LSM-34744, Reaxys4169371
  and DrugBank DB01327; current authority mappings do not remove that access limit.
- All ten adopted compound-level PMID titles/abstracts were inspected. Original 1973
  pages and full 2016 primary text were read, but not every allergy/clinical/bone-cement
  article in full. Current ARO-linked lead metadata and selected original experiments
  were reviewed, not every cited enzyme paper exhaustively.
- NmcA-specific cefazolin primary assay support was not established from the inspected
  1994 paper; the current exact database assertion remains qualified.
- The inspected 2002 PBP study uses labeled ampicillin/penicillin to detect proteins
  and cites earlier cefazolin binding data. Direct cefazolin PBP assay details remain
  to be independently verified before primary upgrade.
- Neutral graph identity does not establish the exact salt/hydrate of every commercial
  assay reagent; 1973 explicitly uses sodium and 2016 commercial preparations are
  not fully resolved.
- PSZ-1 kinetic text/Table 5 disagree; no conflicting numeric constant was adopted.
  Historical clinical and animal results do not establish present-day approval or
  treatment advice.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 26 expanded input hashes unchanged; initial captures retained. No native/source/status/history
  edits.
- Focused schema/strict used022 own locked environment. Chemistry and independent
  KEGG MOL used019 locked RDKit 2026.03.5 against 022 cwd.
- Free public retrieval only. SomePMC direct file routes returned challenge pages;
  actual2021supplements were retrieved from the EuropePMC supplementary ZIP and inspected.
  Challenge responses are not used as primary source text.
- The live CDC page footer itself supplies the cited2025 CLSI edition; this review
  does not infer it from the current calendar year.
- All source snapshots and manifests remain in session scratch; hashes and actual
  access timestamps are attached to evidence entries.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:474053
- https://doi.org/10.1099/mgen.0.000500
- https://doi.org/10.1128/aac.22.6.942
- https://doi.org/10.1128/AAC.01192-16
tags:
- cefazolin
- exact-identity
- cdc-mic
- resistance-evidence
- porin-condition
```
