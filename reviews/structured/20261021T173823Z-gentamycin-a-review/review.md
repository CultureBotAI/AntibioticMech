# Gentamycin A: inverted gentosamine stereochemistry and incompatible ChEMBL grounding

- Review: 20261021T173823Z-gentamycin-a-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T17:15:15Z
- Finished UTC: 2026-10-21T17:38:23Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The stored structure contains an alpha-L-gentosamine sugar, whereas inspected primary chemistry and biosynthesis establish the alpha-D sugar of natural gentamicin A. Four inverted centres explain the native/current-ChEBI disagreement with PubChem and KEGG. The ChEMBL xref separately adds an oxygen, and Garamycin is an exact synonym imported from a gentamicin product context. Nineteen resistance associations remain explicitly database-derived and require exact-congener qualification before primary-evidence promotion.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 499; one exact record. Original thirteen captured input hashes were verified and retained within twenty-seven total inputs, with actual ARO owners and review context appended before detailed assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:28418 | data/antibiotics/antibacterial/gentamycin-a.yaml | generated | gentamycin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:28418 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:28418 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:28418 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:28418 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:28418 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:28418 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:28418 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:28418 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:28418 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:28418 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:28418 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:28418 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Natural gentamicin A versus stored L-gentosamine graph

identity: concern. Targets: CHEBI:28418.

Primary explicit D-gentosamine chemistry, the 1980 full-structure confirmation and 2015 Figure 1 agree. Four mapped sugar centres in the native graph encode the opposite sugar enantiomer within the same larger molecule; it is a diastereomer of natural A. Current ChEBI reproduces that error. The D candidate exactly matches PubChem/KEGG.

### Exact chemical xrefs, source mint and broader parents

grounding: concern. Targets: CHEBI:28418.

Both source mints are reproducible. PubChem/KEGG support the corrected natural D graph; their mismatch should be repaired through native identity adjudication. ChEMBL independently adds a glucosamine N-hydroxy oxygen and remains incompatible after that repair. Broader gentamycin/aminoglycoside parents resolve; CAS independent stereochemistry is limited.

### D/L systematic names and Garamycin

nomenclature: concern. Targets: CHEBI:28418.

The L-systematic synonym matches the wrong native sugar, whereas the D-systematic synonym matches primary natural identity. Correct the structure and associated systematic name coherently. Garamycin belongs to the gentamicin sulfate product context and should not remain an exact chemical synonym for A.

### Generic aminoglycoside mechanism and adopted definition sources

evidence: unknown. Targets: CHEBI:28418.

The source definition distinguishes A as part of a complex and then discusses gentamicin generically. Its two adopted reviews resolve but their full texts were inaccessible. Primary natural-A production is verified, while a direct purified-A ribosome/bactericidal experiment was not independently established here. No broad quantitative mechanism or target is added.

### Antibacterial eligibility and material-specific assays

evidence: supported. Targets: CHEBI:28418.

The isolated natural-A band is bioactive against E. coli in the 1980 source, supporting qualitative antibacterial eligibility for the intended natural compound. Analog 1/gentamicin-C MICs in 1977 and minor X-14847 MICs in 1980 are excluded from A. No activity of the native L-sugar diastereomer is claimed or disproved.

### All nineteen imported CARD associations and twenty-four adopted PMID leads

evidence: unknown. Targets: CHEBI:28418.

Every native entry explicitly identifies a database assertion, and current ARO preserves those relationships. All 24 unique adopted leads were dispositioned: abstracts/metadata for all and selected original main text/figure passages where accessible. Inspected experiments mainly name generic/clinical gentamicin; none inspected here resolves purified A. This limitation does not by itself prove every retained database association false or justify a new major for missing optional primary evidence.

### Regulator direction and exact congener scope

scope: unknown. Targets: CHEBI:28418.

Public original Fig. 3 supports effects on phenotypic variant frequency and attachment, with opposite directions for overexpression and deletion. It does not establish a generic PvrR-presence resistance mechanism or exact-A susceptibility. The native UNKNOWN mechanism and explicit database provenance remain important; additional allele/condition qualification is a bounded follow-up.

### Natural production and biosynthesis versus antimicrobial targets

scope: supported. Targets: CHEBI:28418.

Natural A is isolated from M. echinospora X-14847/NRRL B-12180 and is a biosynthetic intermediate in ATCC 15835. GenD/GenS/GenN chemistry is production/substrate context, not evidence of antimicrobial target inhibition. Producer/biosynthesis fields are optional and absent, so their omission is not a schema finding.

### Existing claim coverage and optional enrichment

completeness: unknown. Targets: CHEBI:28418.

The entire native record and actual adopted owners were inspected. Bibliography coverage includes both definition reviews, class lead and all resistance leads with explicit reading depth. Exact-A quantitative spectrum, direct target and resistance-material evidence remain bounded follow-ups after the identity correction; no optional field is called invalid merely because absent.

### Generated ownership, snapshots and history

provenance: supported. Targets: CHEBI:28418.

The original thirteen hashes are preserved in twenty-seven verified inputs. ChEBI/ARO raw rows, qualification owners, current source conflicts and all three seed/reseed history events were read. No history/status promotion is authorized by this review.

### Successful internal gates despite natural-identity error

schema: supported. Targets: CHEBI:28418.

Schema, strict and internal chemistry checks pass. They establish consistent encoding of the wrong sugar stereoisomer and do not supersede primary source adjudication.

## Findings

### F1: Four gentosamine stereocentres encode the wrong natural-product identity

blocker / open / confirmed; issue key: gentamycin-a-l-gentosamine-instead-of-natural-d.

Natural gentamicin A has alpha-D-gentosamine. The stored ChEBI-derived SMILES/InChI/key and L-systematic synonym instead encode the mirror-image sugar within an otherwise matching molecule. Original 1977 text and compound 2 drawing explicitly establish D-xylose; 1980 structure 9 and 2015 A (6) corroborate it. Native SMILES indices 5/3/2/30 map to C1″/C2″/C3″/C4″ with S/S/R/R; their inversion gives R/R/S/S and exactly the current PubChem/KEGG QVNYEEQUSA graph. This is a genuine four-centre diastereomer difference, not a CIP naming or ring-conformation change.

### F2: The exact ChEMBL xref is an oxygenated constitutional mismatch

major / open / confirmed; issue key: gentamycin-a-chembl7225-extra-oxygen.

CHEMBL7225 currently encodes C18H36N4O11 with an N-hydroxy substituent on the glucosamine residue and different/partial stereochemistry. Gentamicin A and both native/D-sugar candidate graphs are C18H36N4O10. This exact xrefs entry remains wrong even after the four-centre identity repair; the discrepancy is not a salt, solvate or tautomer.

### F3: Garamycin is a gentamicin product name rather than an exact synonym of congener A

minor / open / confirmed; issue key: gentamycin-a-garamycin-product-exact-synonym.

The imported ARO synonym marks Garamycin as EXACT_SYNONYM. Official FDA product identification associates that name with gentamicin sulfate ophthalmic product, and the official gentamicin description identifies a C-component sulfate mixture. It is not an exact chemical synonym for the free-base A congener.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate and repair the natural gentamicin-A stereochemical identity through maintained inputs.

- Use the original D-gentosamine source and explicit C1″–C4″ atom map; invert only the four implicated sugar centres and verify all other stereocentres/linkages are preserved.
- Recompute structure fields coherently and correct the alpha-L systematic synonym. The resulting candidate should reproduce QVNYEEQUSA and match current KEGG/PubChem with chirality.
- Resolve continued EXACT grounding to CHEBI:28418 if the live authority still encodes the L-sugar graph; use supported grounding/curator mechanisms rather than a silent generated edit.
- Regenerate through maintained owners, run focused schema/strict and chemistry/xref checks plus required corpus reference/history/reproduction/QC gates, and inspect the exact diff.

### A2

Remove or remap the chemically incompatible ChEMBL exact xref.

- Confirm the current CHEMBL7225 extra oxygen and stereochemistry at curation time. Do not replace it by label matching alone.
- Retain the natural-product source evidence and verify the final exact-xref set against the repaired D-sugar graph.
- Fix every contributing adopted source/transform, regenerate and run exact chemical/xref and required corpus checks.

### A3

Remove Garamycin from exact chemical synonyms for gentamicin A or retain only an explicitly justified broader product association.

- Use the official product identity and preserve A-versus-C-mixture scope. Do not claim purified A is the marketed active ingredient.
- Correct the ARO-source synonym handling reproducibly; regenerate and inspect synonym types and scientific identity checks.

### A4

Optional follow-up: qualify resistance and enrich natural-A evidence only after exact identity is repaired.

- Retain the existing database-only notes; do not promote generic gentamicin studies to exact-A primary evidence. Retrieve preparation/method details and map each enzyme, strain and allele independently.
- For PvrR distinguish overexpression from deletion and variant-frequency/attachment from drug-specific MIC. Do not import external porin wording without primary support.
- Natural-A isolated-band activity can be added qualitatively with its E. coli assay boundary; do not copy analog 1/C-complex or minor X-14847 MICs. Biosynthetic enzymes must not become antimicrobial targets.
- Any later native edits require the separate validated writer/history workflow.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/gentamycin-a.yaml; Entire native YAML, all nineteen resistance entries and three history events | supports | CHEBI:28418 is SEEDED/EXACT, antibacterial, neutral C18H36N4O10, with fourteen defined stereocentres. Its five synonyms include conflicting alpha-L/alpha-D systematic names and Garamycin. All nineteen resistance evidence notes explicitly call their ARO relationship a database assertion rather than a primary citation; none includes evidence_type, confidence or evidence_status. No molecular_targets, quantitative activity, producer or causal graph is asserted. |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_resistance_edges.tsv; Exact ChEBI row 541, ARO row 312, resistance rows 4005–4023, readiness row 1308 and maintained transforms | supports | The ChEBI row supplies the stored graph and both systematic names. ARO supplies its definition, Garamycin and imported resistance associations. The full selected rows, actual owner files and qualification configuration were inspected. No exact curator or decision row was found in the directly inspected maintained tables. |
| search | 499-local-hits.txt; 499-qualification-hits.txt; Initial ignored-inclusive search plus targeted qualification/source search | context_only | Searches included hidden and gitignored files. Local reports were discovery leads only; no historical conclusion was adopted as current evidence. Complete exact-row selections additionally checked maintained tables. |
| chemistry | 499-chemistry.json; 499-focused-results.json; Both native SMILES/InChI, composition, charge, masses, source mint and actual native validators | supports | All internal chemistry checks and both source mints agree. Focused schema and strict checks exit zero in batch050. Standalone RDKit 2026.03.5 uses the existing batch019 interpreter with batch050 cwd. Internal consistency does not validate natural stereochemical identity. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/28418/; Current CHEBI:28418 structure and synonym list | supports | Current ChEBI retains the native key LKKVGKXCMYHKSL-LLZRLKDCSA-N and the conflicting L/D sugar names. Agreement with the adopted source explains the seeded error; it does not override primary chemical evidence. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/12810388/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON; Asserted CID12810388 property record | supports | Current PubChem encodes LKKVGKXCMYHKSL-QVNYEEQUSA-N with the same formula and constitution but four inverted sugar centres relative to the native graph. This agrees with the primary-adjudicated D-gentosamine candidate. It should not be removed merely because the erroneous native graph differs. |
| kegg | https://rest.kegg.jp/get/C01917/mol; Asserted KEGG C01917 molfile and entry | supports | Current KEGG molfile independently generates the same QVNYEEQUSA key as PubChem and the D-gentosamine candidate. The exact graph comparison uses stereochemistry, not label equality. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL7225.json; Asserted CHEMBL7225 molecule_structures | refutes | ChEMBL encodes C18H36N4O11, ZOVOIJVLCGTBBF-SMCRGNSSSA-N, including N–OH instead of the glucosamine amino group and only nine assigned of fourteen centres. Its extra oxygen is a constitutional mismatch with both native O10 and natural gentamicin A; salt or stereochemical normalization cannot explain it. |
| comparison | 499-compare.json; Independent native/current-authority graph, formula and chirality comparisons | supports | Native and ChEBI match. PubChem and KEGG match each other but not the native chiral graph. ChEMBL has a different stereo-stripped connectivity key and one extra oxygen. Unassigned ChEMBL centres are not interpreted as a racemate. |
| sugar-map | 499-sugar-map.json; Explicit atom map and stereoretentive diagnostic transformation | refutes | Native SMILES indices 5/3/2/30 are gentosamine C1″/C2″/C3″/C4″, assigned S/S/R/R. Inverting only these four gives R/R/S/S and exactly QVNYEEQUSA. Replacing N-methylamino by OH and opening the sugar ring in scratch, preserving spatial chirality, gives xylose C2/C3/C4 S/R/S from native versus R/S/R from the candidate: L versus D. This is a computational nomenclature diagnostic, not a claimed experimental reaction. |
| primary1977 | https://doi.org/10.7164/antibiotics.30.836; Original p 836 introduction, compound 2 drawing; pp 837–840 structure discussion and Table 2 | refutes | The authors explicitly identify gentosamine as 3-deoxy-3-methylamino-D-xylose and depict gentamicin A as compound 2, distinct from their synthesized analog 1. Actual p 836 figure was visually read. Table 2 reports sulfate salts of analog 1 and gentamicin C complex, not gentamicin A; those MICs are not transferred. This original source directly resolves the D/L sugar designation. |
| primary1980 | https://doi.org/10.7164/antibiotics.33.1380; All three original pages1380–1382; actual p 1381 structure 9 and Table 1 | refutes | The paper confirms the full natural gentamicin A structure 9 by comparing paromamine derivatives from commercial fermentation and M. echinospora X-14847 with authentic paromomycin-derived material. Optical rotations and cuprammonium complexing address the 4/6 linkage assignment on deoxystreptamine. The depicted gentosamine agrees with the D-sugar chemistry; this paper does not revise it to the L sugar. |
| primary1980-figure | https://www.jstage.jst.go.jp/article/antibiotics1968/33/11/33_11_1380/_pdf; Actual p 1381 image, Table 1 and structure 9 | refutes | The natural gentamicin A chair drawing and linkage numbering were inspected directly. The table distinguishes commercial-fermentation and X-14847 samples; it is structural comparison, not an antibacterial MIC experiment. |
| production | https://doi.org/10.7164/antibiotics.33.1431; Original pp 1431–1436; isolation p 1434 and separate X-14847 activity p 1435 | supports | M. echinospora strain X-14847, deposited NRRL B-12180, yields gentamicin A as the major component. Two separated bands are bioactive against E. coli on neomycin assay agar; the major band is identified as A by free-base/N-acetyl TLC and matching carbon NMR. This supports qualitative antibacterial activity of natural A and producer context. The reported 0.2–1.0 mg/mL MIC range is for the separate minor aminoglycoside X-14847, not gentamicin A. |
| biosynthesis | https://pmc.ncbi.nlm.nih.gov/articles/PMC4340712/; PMID 25641167 original main text, Fig. 1 A (6), gene deletion/complementation and in-vitro methods | supports | The 2015 study uses M. echinospora ATCC 15835 and commercially obtained Toku-E gentamicin A. GenD2/GenS2/GenN convert A2 to A; GenD1 methylates A at C4″ to X2. Main-text LC-HRMS comparison with authentic A and the actually viewed Fig. 1 distinguish A (6) from A2 (3), X2 (4) and Ae (10). These enzymes are biosynthetic and substrate evidence, not antimicrobial targets or resistance determinants. Main text was read; SI was not independently reviewed. |
| biosynthesis-figure | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/17d8/4340712/7146b17282c0/gr1.jpg; Actual Figure 1, A (6) structure and numbered A2 precursor | supports | The figure depicts the same D-gentosamine configuration as the original chemical evidence. The caption has an Ae numbering typo, so compound labels in the actual figure and corresponding main text were checked rather than transferring the caption blindly. No experimental inhibition value is inferred from the biosynthetic scheme. |
| aro | https://github.com/arpcard/aro/blob/master/aro.obo; Exact compound, class and all nineteen resistance terms from current public ARO snapshot | supports | Current ARO retains the exact database relationships recorded natively and the two definition bibliography leads. These are correctly described by native notes as database assertions. The extracted terms preserve all twenty-four unique class/definition/resistance PMID leads; actual original abstracts/metadata and selected full-source passages were reviewed at the depths specified individually below. |
| parents | https://www.ebi.ac.uk/chebi/backend/api/public/compound/17833/; CHEBI:17833 broader gentamycin class and CHEBI:33281 role; ARO:0000016 class | supports | CHEBI:17833 is explicitly a group of aminoglycoside antibiotics produced by Micromonospora, with no default molecular structure. It is an appropriate broader parent rather than an exact-mixture xref. The antimicrobial-agent role and aminoglycoside class resolve and fit the intended natural compound. This does not establish activity of the incorrectly inverted native stereoisomer. |
| role | https://www.ebi.ac.uk/chebi/backend/api/public/compound/33281/; CHEBI:33281 official role record | supports | The asserted role resolves as antimicrobial agent. Its use is supported for natural gentamicin A by the qualitative isolated-band assay, without inventing target-specific potency. |
| cas-access | https://commonchemistry.cas.org/detail?cas_rn=13291-74-2; CAS detail page and public API attempt | context_only | The asserted CAS number is retained by current chemical sources. The detail page supplied an application shell and the API returned 401, so no independent CAS stereochemical validation is claimed. |
| adapter | iModulonDB p_aeruginosa/precise364 search pvrR; Structured dataset catalog checked before open protein research; corrected query exit 0 | context_only | The covered P. aeruginosa precise364 query returns zero gene and zero iModulon hits. The initial pao1-key attempt failed with sandbox DNS and is not treated as successful. No matching Micromonospora dataset was found in the catalog. Neither absence nor module membership proves resistance or chemical identity. |
| pmid-11083623 | https://pubmed.ncbi.nlm.nih.gov/11083623/; Original review metadata; no abstract in EPMC | context_only | The definition citation is an aminoglycoside mechanism/resistance review. Full text retrieval failed (EPMC 500, PMC challenge, alternative403). It is not treated as a new exact-A experiment or as fully read. |
| pmid-10103173 | https://pubmed.ncbi.nlm.nih.gov/10103173/; Original review metadata; no abstract in EPMC | context_only | Second adopted definition lead is an aminoglycoside activity/resistance review. Full text remained inaccessible through the attempted public routes; no claim of exact-A assay verification is made. |
| pmid-8385262 | https://pubmed.ncbi.nlm.nih.gov/8385262/; Original review abstract | context_only | This is a molecular-genetics review of modifying enzymes, used for the class and AAC(3)-IIIc lead. The abstract does not supply a purified gentamicin-A substrate experiment; full text was not readable through the attempted routes. |
| pmid-2833561 | https://pubmed.ncbi.nlm.nih.gov/2833561/; Original abstract | context_only | Tn4001 aacA-aphD from S. aureus is cloned and expressed in E. coli; activities and insertion-mutant domain attribution distinguish AAC and APH functions. Gentamicin is named without exact A preparation. No quantitative result is transferred. |
| pmid-10021417 | https://pubmed.ncbi.nlm.nih.gov/10021417/; Original abstract | context_only | Purified recombinant AAC(6′)-APH(2″) has broad substrate specificity and unusual modifications of other aminoglycosides. The abstract explicitly discusses therapeutic gentamicin C; it does not establish identical activity on gentamicin A. |
| pmid-11959575 | https://pubmed.ncbi.nlm.nih.gov/11959575/; Original abstract | context_only | S. marcescens SCH909 integron study characterizes the ANT(3″)-I/AAC(6′)-II fusion and associated resistance genes. Exact gentamicin A material is not identified in the inspected abstract; full-text routes failed. |
| pmid-15561846 | https://pubmed.ncbi.nlm.nih.gov/15561846/; Original abstract | context_only | P. aeruginosa 101-4704 integron includes aac(6′)-30/aac(6′)-Ib′, alongside IMP16. Detailed beta-lactamase kinetics are not aminoglycoside-A evidence. Exact-A substrate testing is unverified. |
| pmid-17030911 | https://pubmed.ncbi.nlm.nih.gov/17030911/; Original abstract | context_only | E. casseliflavus HZ95 aph(2″)-Ie-containing plasmid fragment confers gentamicin resistance in E. coli DH5alpha. The abstract does not identify purified gentamicin A and is not an assay of every congener. |
| pmid-9055984 | https://pubmed.ncbi.nlm.nih.gov/9055984/; Original abstract | context_only | E. gallinarum SF9117 aph(2″)-Ic, now ARO APH(2″)-IIIa, is cloned into E. coli; the reported gentamicin phenotype and ampicillin synergy failure are strain/assay specific. No exact-A test preparation is established. |
| pmid-9593155 | https://pubmed.ncbi.nlm.nih.gov/9593155/; Original abstract | context_only | E. casseliflavus UC73 aph(2″)-Id, now APH(2″)-IVa, confers gentamicin resistance after cloning in E. coli. Clinical detection and combination-killing observations are not purified gentamicin-A evidence. |
| pmid-17875999 | https://pubmed.ncbi.nlm.nih.gov/17875999/; Original abstract | context_only | NpmA from E. coli ARS3 modifies A1408, with 30S-subunit methylation and drug-footprinting evidence. Gentamicin is named generically; the congener is not identified. The abstract supports NpmA mechanism but not exact-A material attribution. |
| pmid-26488937 | https://pubmed.ncbi.nlm.nih.gov/26488937/; Original abstract and full-XML screening/material paragraphs | context_only | The study screens NDM1-positive P. aeruginosa isolates and identifies RmtC with RmtF co-carriage in one. Growth at 256 mg/L each amikacin/gentamicin is a screening condition, not an exact-A MIC or isolated RmtF-only causal effect. |
| pmid-22547620 | https://pubmed.ncbi.nlm.nih.gov/22547620/; Original abstract | context_only | RmtF in K. pneumoniae BM4686 resides on pIP849 and is cotranscribed with aac(6′)-Ib. The abstract establishes the methyltransferase-family context and resistance to a class, without identifying purified gentamicin A. |
| pmid-17158944 | https://pubmed.ncbi.nlm.nih.gov/17158944/; Original abstract | context_only | RmtD from Brazilian P. aeruginosa PA0905 is characterized by cloning and high-level aminoglycoside resistance. The generic gentamicin result is not a resolved exact-A assay. |
| pmid-18222955 | https://pubmed.ncbi.nlm.nih.gov/18222955/; Original metadata only; no abstract | context_only | This is the adopted K. pneumoniae RmtD report. EPMC fullTextXML500 and PMC/EuropePMC access restrictions prevented source-body inspection. Its title alone is not used to assign a strain, MIC or gentamicin-A preparation. |
| pmid-23459483 | https://pubmed.ncbi.nlm.nih.gov/23459483/; Original abstract | context_only | Eight Brazilian K. pneumoniae clinical strains include RmtD1/D2 and novel RmtG, frequently with KPC2/CTX-M. This source concerns K. pneumoniae, not the P. aeruginosa wording in the external ARO definition; the native entry itself does not assert that taxon. Exact gentamicin-A testing remains unverified. |
| pmid-23959310 | https://pubmed.ncbi.nlm.nih.gov/23959310/; Original abstract plus main HTML methods/results on APH(2″)-Ig | context_only | C. coli N29710/N29716 plasmid and transfer studies are separated from synthesized aph(2″)-Ig expression in E. coli DH5alpha. The latter increases generic gentamicin MIC 0.25→32 micrograms/mL with IPTG. Exact A is not specified; this numerical result is not attached to the native compound. |
| pmid-23478957 | https://pubmed.ncbi.nlm.nih.gov/23478957/; Original abstract and full main HTML text | context_only | RmtH from K. pneumoniae MRSN2404 is cloned in E. coli; MIC and Etest results use generic gentamicin. G1405 specificity is inferred in this paper from phenotype/alignment, not directly measured methylation. Exact A is not established. |
| pmid-11961556 | https://pubmed.ncbi.nlm.nih.gov/11961556/; Original abstract, public Fig. 3 caption and actual Fig. 3 image | context_only | PvrR regulates resistant/susceptible biofilm variants. In Fig. 3, overexpression reduces variant frequency/attachment and deletion increases variant frequency. The figure does not establish purified gentamicin-A resistance, direct target binding or a porin deletion. Full main text remained subscription-limited; native UNKNOWN/database scope is retained. |
| pmid-23129050 | https://pubmed.ncbi.nlm.nih.gov/23129050/; Original abstract | context_only | APH(2″)-If from C. jejuni prefers GTP and phosphorylates a subset of 4,6-disubstituted aminoglycosides. Generic gentamicin is included, but the inspected abstract does not identify exact A. Full text routes were unavailable. |
| pmid-21078935 | https://pubmed.ncbi.nlm.nih.gov/21078935/; Original abstract | context_only | rmtD2 is identified in Argentine Enterobacteriaceae and associated with broad clinical-aminoglycoside resistance and a conjugative element. No purified-A assay is identified in the inspected source depth. |
| pmid-20368404 | https://pubmed.ncbi.nlm.nih.gov/20368404/; Original abstract | context_only | Bovine E. coli resistance phenotyping and genetic analysis discover rmtE. Gentamicin and amikacin are reported generically, so material-specific quantitative transfer is not justified. |
| pmid-26392485 | https://pubmed.ncbi.nlm.nih.gov/26392485/; Full main HTML text; original has no abstract | context_only | Swine E. coli S68/87 carry rmtE2 with Val6Ala relative to rmtE; plasmid transfer into E. coli C600 yields aminoglycoside resistance. Generic gentamicin and amikacin MICs are reported, without identifying purified gentamicin A. |
| pmid-31578249 | https://pubmed.ncbi.nlm.nih.gov/31578249/; Original abstract; full-XML aminoglycoside results and methods | context_only | AAC(3)-IVb from C. gilardii W2-2 reduces gentamicin/tobramycin susceptibility in E. coli BW25113 constructs. Methods use Becton Dickinson disks and 100 micromolar IPTG on Mueller-Hinton agar; this is disk susceptibility, not a direct enzymatic kinetic assay or purified gentamicin-A MIC. |
| res-rmtF | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4622239/fullTextXML; Screening/material paragraphs | context_only | Read at the explicitly bounded depth recorded in the corresponding PMID evidence entry; material, organism and assay boundaries were retained. This snapshot is not used as proof of purified gentamicin-A resistance. |
| res-rmtE2 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4649190/?pdf=1; Main letter text | context_only | Read at the explicitly bounded depth recorded in the corresponding PMID evidence entry; material, organism and assay boundaries were retained. This snapshot is not used as proof of purified gentamicin-A resistance. |
| res-aphIg | https://pmc.ncbi.nlm.nih.gov/articles/PMC3811239/?pdf=1; Methods and APH(2″)-Ig cloning/result paragraphs | context_only | Read at the explicitly bounded depth recorded in the corresponding PMID evidence entry; material, organism and assay boundaries were retained. This snapshot is not used as proof of purified gentamicin-A resistance. |
| res-rmtH | https://pmc.ncbi.nlm.nih.gov/articles/PMC3632941/?pdf=1; Full main letter text | context_only | Read at the explicitly bounded depth recorded in the corresponding PMID evidence entry; material, organism and assay boundaries were retained. This snapshot is not used as proof of purified gentamicin-A resistance. |
| res-aacIVb | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6796972/fullTextXML; Aminoglycoside results and susceptibility/cloning methods | context_only | Read at the explicitly bounded depth recorded in the corresponding PMID evidence entry; material, organism and assay boundaries were retained. This snapshot is not used as proof of purified gentamicin-A resistance. |
| res-pvrR | https://media.springernature.com/lw1200/springer-static/image/art%3A10.1038%2F416740a/MediaObjects/41586_2002_Article_BF416740a_Fig3_HTML.jpg; Actual public Fig. 3, panels d–f | context_only | Read at the explicitly bounded depth recorded in the corresponding PMID evidence entry; material, organism and assay boundaries were retained. This snapshot is not used as proof of purified gentamicin-A resistance. |
| garamycin | https://www.accessdata.fda.gov/drugsatfda_docs/nda/2004/065024_S000_Gentamicin%20Ophthalmic%20Ointment_MICROR.pdf; FDA ANDA 65024 microbiology review, PDF page 19 (June 29, 2004): proprietary/non-proprietary product identity | refutes | The actual scanned page 19, headed Product Quality Microbiology Review, identifies proprietary Garamycin and non-proprietary Gentamicin Sulfate Ophthalmic Ointment USP, 0.3%. This establishes a marketed product name, not an exact chemical synonym of free-base gentamicin A. No current approval status is inferred. |
| product-mixture | https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=51a411a0-2671-4c1c-bf25-e29b32efed0c; DailyMed gentamicin sulfate ophthalmic solution description | supports | The official label describes gentamicin as a mixture of sulfate salts of C1, C2 and C1A. This corroborates the drug/product versus A-congener boundary and supplies no claim of purified-A clinical use. |
| access | 499-fetch1.json through 499-fetch5.json; Actual public retrieval URLs, timestamps, status codes and content hashes | context_only | Original J-STAGE structure/synthesis/production PDFs, chemical authorities, selected PMC texts and public Nature Fig. 3 were retrieved. Many EPMC fullTextXML requests returned 500 and PMC HTML returned browser-challenge pages despite HTTP 200. ACS 1967/1970 PDFs returned 403; a public 1970 copy could not connect. The 1970 search excerpt was a discovery lead only, not the finding basis. CAS API returned 401. Failed bodies were not treated as inspected papers. |
| garamycin-page | https://www.accessdata.fda.gov/drugsatfda_docs/nda/2004/065024_S000_Gentamicin%20Ophthalmic%20Ointment_MICROR.pdf; Actual PDF page 19 scanned image, visually inspected | refutes | The proprietary and non-proprietary product names are printed together on the inspected FDA page; the image is preserved for independent audit. |

## Limits And Additional Notes

- Required shared full-corpus checks are incorporated separately by the root reviewer before finalization; the actual focused gates are recorded here.
- Original 1967/1970 ACS full texts were unavailable: publisher 403 and the public 1970 mirror did not connect. The 1970 search excerpt is not evidence for the finding. The identity conclusion instead uses directly inspected 1977/1980 original PDFs, 2015 source figure and explicit graph/atom comparison.
- Of 24 adopted definition/class/resistance PMID leads, all original metadata and available abstracts were read. Selected full source text or figure passages were inspected for 26488937,26392485,23959310,23478957,31578249 and 11961556. The remaining papers were not all read in full; 11083623,10103173 and 18222955 remained metadata-only because no abstract/full text was accessible.
- Several PMC requests returned a browser challenge despite HTTP 200; EPMC fullTextXML returned 500 for many adopted papers. These were not treated as full-text access. The public Nature Fig. 3 is accessible but the full 2002 main text is subscription-limited.
- No exact-A resistance MIC or direct ribosome inhibition/bactericidal assay was established from the inspected sources. Natural-A qualitative antibacterial activity is supported, and the native L-sugar diastereomer is not assumed either active or inactive.
- CAS API access returned 401 and the page was a client shell, so CAS-specific stereochemical agreement was not independently verified. The 2015 supplementary files and every historical structure reference were not exhaustively reanalyzed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All original capture hashes are preserved. No native record, source table, curation history, progress file or immutable bundle was edited.
- Independent validation_plan review of original 1977/1980 source and four-centre graph inversion agreed with the stereochemical identity finding; this does not replace root final audit.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T173823Z-gentamycin-a-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Gentamycin A: inverted gentosamine stereochemistry and incompatible ChEMBL
  grounding'
started_at: '2026-10-21T17:15:15Z'
finished_at: '2026-10-21T17:38:23Z'
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
verdict: blocked
scientific_review: true
summary: The stored structure contains an alpha-L-gentosamine sugar, whereas inspected
  primary chemistry and biosynthesis establish the alpha-D sugar of natural gentamicin
  A. Four inverted centres explain the native/current-ChEBI disagreement with PubChem
  and KEGG. The ChEMBL xref separately adds an oxygen, and Garamycin is an exact synonym
  imported from a gentamicin product context. Nineteen resistance associations remain
  explicitly database-derived and require exact-congener qualification before primary-evidence
  promotion.
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
  - path: data/antibiotics/antibacterial/gentamycin-a.yaml
    sha256: 30ac6f1f487c2b3a9a3d038d50c6bc86d8cd091ccb903b2b49c0fddae9771441
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
  - path: curation/record_review_queue.tsv
    sha256: 3828a5120b892ee0ee0b776affc6c3e4f1f1a3355ec4edd30e6005762de00e70
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
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: scripts/card_evidence_reviews.py
    sha256: f9ec8aff30066bf04b9c2757af7d6f5d179d045e57b9f3b352bbed0b851f50a8
    role: context
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: context
targets:
- target_id: CHEBI:28418
  path: data/antibiotics/antibacterial/gentamycin-a.yaml
  label: gentamycin A
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: ChEBI identity, structure, roles, synonyms and xrefs
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO definition, synonyms, xrefs and bibliography
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Imported resistance associations
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: CARD evidence qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: CARD qualification transform
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI/ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding/exclusion overrides
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 499; one exact record. Original thirteen captured input
    hashes were verified and retained within twenty-seven total inputs, with actual
    ARO owners and review context appended before detailed assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:28418
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:28418
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    499
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:28418
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/gentamycin-a.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:28418
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/gentamycin-a.yaml --out /private/tmp/am-review-session/499-strict.tsv
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
  - CHEBI:28418
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
  - CHEBI:28418
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
  - CHEBI:28418
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
  - CHEBI:28418
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
  - CHEBI:28418
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
  - CHEBI:28418
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
  - CHEBI:28418
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
  - CHEBI:28418
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
  - CHEBI:28418
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/gentamycin-a.yaml
  locator: Entire native YAML, all nineteen resistance entries and three history events
  accessed_at: '2026-10-21T17:35:23Z'
  support: supports
  summary: CHEBI:28418 is SEEDED/EXACT, antibacterial, neutral C18H36N4O10, with fourteen
    defined stereocentres. Its five synonyms include conflicting alpha-L/alpha-D systematic
    names and Garamycin. All nineteen resistance evidence notes explicitly call their
    ARO relationship a database assertion rather than a primary citation; none includes
    evidence_type, confidence or evidence_status. No molecular_targets, quantitative
    activity, producer or causal graph is asserted.
  snapshot_sha256: 30ac6f1f487c2b3a9a3d038d50c6bc86d8cd091ccb903b2b49c0fddae9771441
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_resistance_edges.tsv
  locator: Exact ChEBI row 541, ARO row 312, resistance rows 4005–4023, readiness
    row 1308 and maintained transforms
  accessed_at: '2026-10-21T17:35:23Z'
  support: supports
  summary: The ChEBI row supplies the stored graph and both systematic names. ARO
    supplies its definition, Garamycin and imported resistance associations. The full
    selected rows, actual owner files and qualification configuration were inspected.
    No exact curator or decision row was found in the directly inspected maintained
    tables.
  snapshot_sha256: 255a5eec9f4f7c3e29bf9bc1c7fd34bc4d8332aff4380be5f12098683d4ca0d9
- evidence_id: search
  kind: search
  reference: 499-local-hits.txt; 499-qualification-hits.txt
  locator: Initial ignored-inclusive search plus targeted qualification/source search
  accessed_at: '2026-10-21T17:35:23Z'
  support: context_only
  summary: Searches included hidden and gitignored files. Local reports were discovery
    leads only; no historical conclusion was adopted as current evidence. Complete
    exact-row selections additionally checked maintained tables.
  snapshot_sha256: 39e5cc41287a112c4376286d36a0554b932a0492e21ce1769788935c6e13e143
  search_scope: Initial rg --no-ignore --hidden target identifier, label and slug
    search; additional ignored-inclusive ARO3004015/Garamycin/systematic-name search
    in qualification configuration, seed/extraction code and tests; complete maintained-table
    exact-row inspection.
- evidence_id: chemistry
  kind: validation
  reference: 499-chemistry.json; 499-focused-results.json
  locator: Both native SMILES/InChI, composition, charge, masses, source mint and
    actual native validators
  accessed_at: '2026-10-21T17:35:23Z'
  support: supports
  summary: All internal chemistry checks and both source mints agree. Focused schema
    and strict checks exit zero in batch050. Standalone RDKit 2026.03.5 uses the existing
    batch019 interpreter with batch050 cwd. Internal consistency does not validate
    natural stereochemical identity.
  snapshot_sha256: 59ddfd1e92a1de79c402280d7c533db2b914e887cf4097a2d6d3bcf9a467bfed
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/28418/
  locator: Current CHEBI:28418 structure and synonym list
  accessed_at: '2026-10-21T17:27:04.733895Z'
  support: supports
  summary: Current ChEBI retains the native key LKKVGKXCMYHKSL-LLZRLKDCSA-N and the
    conflicting L/D sugar names. Agreement with the adopted source explains the seeded
    error; it does not override primary chemical evidence.
  snapshot_sha256: 16640792d87f19aeb6302f2856fd601b4febd2c501ae43d6b4c4b98f152e6316
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/12810388/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON
  locator: Asserted CID12810388 property record
  accessed_at: '2026-10-21T17:27:04.734247Z'
  support: supports
  summary: Current PubChem encodes LKKVGKXCMYHKSL-QVNYEEQUSA-N with the same formula
    and constitution but four inverted sugar centres relative to the native graph.
    This agrees with the primary-adjudicated D-gentosamine candidate. It should not
    be removed merely because the erroneous native graph differs.
  snapshot_sha256: 3e94ace0526484b218ee97fa5f1672c0a9ef5a88c3a071f4948cacf9ebd1b2de
- evidence_id: kegg
  kind: authority
  reference: https://rest.kegg.jp/get/C01917/mol
  locator: Asserted KEGG C01917 molfile and entry
  accessed_at: '2026-10-21T17:27:05.113434Z'
  support: supports
  summary: Current KEGG molfile independently generates the same QVNYEEQUSA key as
    PubChem and the D-gentosamine candidate. The exact graph comparison uses stereochemistry,
    not label equality.
  snapshot_sha256: 813d0e91e6f2a292e87f85497c22b2c0d5bb679ead02ed35ffbbf48400c3427c
- evidence_id: chembl
  kind: authority
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL7225.json
  locator: Asserted CHEMBL7225 molecule_structures
  accessed_at: '2026-10-21T17:27:04.734607Z'
  support: refutes
  summary: ChEMBL encodes C18H36N4O11, ZOVOIJVLCGTBBF-SMCRGNSSSA-N, including N–OH
    instead of the glucosamine amino group and only nine assigned of fourteen centres.
    Its extra oxygen is a constitutional mismatch with both native O10 and natural
    gentamicin A; salt or stereochemical normalization cannot explain it.
  snapshot_sha256: 81737581b97a73cb168aa329d7f9bf969b924b2d00ae0772b8d530f5ab3c1adf
- evidence_id: comparison
  kind: validation
  reference: 499-compare.json
  locator: Independent native/current-authority graph, formula and chirality comparisons
  accessed_at: '2026-10-21T17:35:23Z'
  support: supports
  summary: Native and ChEBI match. PubChem and KEGG match each other but not the native
    chiral graph. ChEMBL has a different stereo-stripped connectivity key and one
    extra oxygen. Unassigned ChEMBL centres are not interpreted as a racemate.
  snapshot_sha256: 81726a4e33c3e74cc78a4a0f89f6aede9fd33a27a34b8916986efdd59020f818
- evidence_id: sugar-map
  kind: validation
  reference: 499-sugar-map.json
  locator: Explicit atom map and stereoretentive diagnostic transformation
  accessed_at: '2026-10-21T17:35:23Z'
  support: refutes
  summary: 'Native SMILES indices 5/3/2/30 are gentosamine C1″/C2″/C3″/C4″, assigned
    S/S/R/R. Inverting only these four gives R/R/S/S and exactly QVNYEEQUSA. Replacing
    N-methylamino by OH and opening the sugar ring in scratch, preserving spatial
    chirality, gives xylose C2/C3/C4 S/R/S from native versus R/S/R from the candidate:
    L versus D. This is a computational nomenclature diagnostic, not a claimed experimental
    reaction.'
  snapshot_sha256: 297f0584e1b72130d630b06b40afd1c2dd9c5e3240c9cd97b94c30b6ceb2bf3f
- evidence_id: primary1977
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.30.836
  locator: Original p 836 introduction, compound 2 drawing; pp 837–840 structure discussion
    and Table 2
  accessed_at: '2026-10-21T17:29:02.452804Z'
  support: refutes
  summary: The authors explicitly identify gentosamine as 3-deoxy-3-methylamino-D-xylose
    and depict gentamicin A as compound 2, distinct from their synthesized analog
    1. Actual p 836 figure was visually read. Table 2 reports sulfate salts of analog
    1 and gentamicin C complex, not gentamicin A; those MICs are not transferred.
    This original source directly resolves the D/L sugar designation.
  snapshot_sha256: fe4c18c86dc11c616bd5c5c6145899d715554bf4130439bc345b7a657beba0c5
- evidence_id: primary1980
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.33.1380
  locator: All three original pages1380–1382; actual p 1381 structure 9 and Table
    1
  accessed_at: '2026-10-21T17:29:02.450029Z'
  support: refutes
  summary: The paper confirms the full natural gentamicin A structure 9 by comparing
    paromamine derivatives from commercial fermentation and M. echinospora X-14847
    with authentic paromomycin-derived material. Optical rotations and cuprammonium
    complexing address the 4/6 linkage assignment on deoxystreptamine. The depicted
    gentosamine agrees with the D-sugar chemistry; this paper does not revise it to
    the L sugar.
  snapshot_sha256: 333b5dce489db708123670f66a3dbd4849061b715b18e8ed8aaa2740c0a5cdac
- evidence_id: primary1980-figure
  kind: primary_source
  reference: https://www.jstage.jst.go.jp/article/antibiotics1968/33/11/33_11_1380/_pdf
  locator: Actual p 1381 image, Table 1 and structure 9
  accessed_at: '2026-10-21T17:35:23Z'
  support: refutes
  summary: The natural gentamicin A chair drawing and linkage numbering were inspected
    directly. The table distinguishes commercial-fermentation and X-14847 samples;
    it is structural comparison, not an antibacterial MIC experiment.
  snapshot_sha256: 8c1c9e1012356693e01ab844e5f3c1ba9224a48fed3fbc88a33bc683f82fb16d
- evidence_id: production
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.33.1431
  locator: Original pp 1431–1436; isolation p 1434 and separate X-14847 activity p
    1435
  accessed_at: '2026-10-21T17:29:33.538529Z'
  support: supports
  summary: M. echinospora strain X-14847, deposited NRRL B-12180, yields gentamicin
    A as the major component. Two separated bands are bioactive against E. coli on
    neomycin assay agar; the major band is identified as A by free-base/N-acetyl TLC
    and matching carbon NMR. This supports qualitative antibacterial activity of natural
    A and producer context. The reported 0.2–1.0 mg/mL MIC range is for the separate
    minor aminoglycoside X-14847, not gentamicin A.
  snapshot_sha256: cde54839228158325176607e44416dde08d67bd676caf6e551e68b02df2515ef
- evidence_id: biosynthesis
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4340712/
  locator: PMID 25641167 original main text, Fig. 1 A (6), gene deletion/complementation
    and in-vitro methods
  accessed_at: '2026-10-21T17:20:01.747490Z'
  support: supports
  summary: The 2015 study uses M. echinospora ATCC 15835 and commercially obtained
    Toku-E gentamicin A. GenD2/GenS2/GenN convert A2 to A; GenD1 methylates A at C4″
    to X2. Main-text LC-HRMS comparison with authentic A and the actually viewed Fig.
    1 distinguish A (6) from A2 (3), X2 (4) and Ae (10). These enzymes are biosynthetic
    and substrate evidence, not antimicrobial targets or resistance determinants.
    Main text was read; SI was not independently reviewed.
  snapshot_sha256: 21d4f7a905b7387ebdb0c2096c5a4397f5d69bdf9eceebdac6bdb8fa9627eee7
- evidence_id: biosynthesis-figure
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/17d8/4340712/7146b17282c0/gr1.jpg
  locator: Actual Figure 1, A (6) structure and numbered A2 precursor
  accessed_at: '2026-10-21T17:29:33.536237Z'
  support: supports
  summary: The figure depicts the same D-gentosamine configuration as the original
    chemical evidence. The caption has an Ae numbering typo, so compound labels in
    the actual figure and corresponding main text were checked rather than transferring
    the caption blindly. No experimental inhibition value is inferred from the biosynthetic
    scheme.
  snapshot_sha256: 13705b18010070b6d97a06c5bba76f668b221f44091bb612472a34fe09c545c3
- evidence_id: aro
  kind: database
  reference: https://github.com/arpcard/aro/blob/master/aro.obo
  locator: Exact compound, class and all nineteen resistance terms from current public
    ARO snapshot
  accessed_at: '2026-10-21T17:35:23Z'
  support: supports
  summary: Current ARO retains the exact database relationships recorded natively
    and the two definition bibliography leads. These are correctly described by native
    notes as database assertions. The extracted terms preserve all twenty-four unique
    class/definition/resistance PMID leads; actual original abstracts/metadata and
    selected full-source passages were reviewed at the depths specified individually
    below.
  snapshot_sha256: a2d06eaa58d86157201933bd401297c807a2f50ad5b754c9e075948cdc3a892a
- evidence_id: parents
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/17833/
  locator: CHEBI:17833 broader gentamycin class and CHEBI:33281 role; ARO:0000016
    class
  accessed_at: '2026-10-21T17:27:04.734132Z'
  support: supports
  summary: CHEBI:17833 is explicitly a group of aminoglycoside antibiotics produced
    by Micromonospora, with no default molecular structure. It is an appropriate broader
    parent rather than an exact-mixture xref. The antimicrobial-agent role and aminoglycoside
    class resolve and fit the intended natural compound. This does not establish activity
    of the incorrectly inverted native stereoisomer.
  snapshot_sha256: 411b17f24bc5d181a691650644f36c95b41eec9caa302883cfccfb92f4939bd6
- evidence_id: role
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/33281/
  locator: CHEBI:33281 official role record
  accessed_at: '2026-10-21T17:27:04.734196Z'
  support: supports
  summary: The asserted role resolves as antimicrobial agent. Its use is supported
    for natural gentamicin A by the qualitative isolated-band assay, without inventing
    target-specific potency.
  snapshot_sha256: 0f66df822d1a825c02531f80cc0fcc12783ac72a0c2f0482a9d9018db0dba9e1
- evidence_id: cas-access
  kind: authority
  reference: https://commonchemistry.cas.org/detail?cas_rn=13291-74-2
  locator: CAS detail page and public API attempt
  accessed_at: '2026-10-21T17:27:05.268105Z'
  support: context_only
  summary: The asserted CAS number is retained by current chemical sources. The detail
    page supplied an application shell and the API returned 401, so no independent
    CAS stereochemical validation is claimed.
  snapshot_sha256: 2f239172fc6f94cf371b6ea533370663c3b9757b0ba9f3bc83a79bf30a731989
- evidence_id: adapter
  kind: database
  reference: iModulonDB p_aeruginosa/precise364 search pvrR
  locator: Structured dataset catalog checked before open protein research; corrected
    query exit 0
  accessed_at: '2026-10-21T17:35:23Z'
  support: context_only
  summary: The covered P. aeruginosa precise364 query returns zero gene and zero iModulon
    hits. The initial pao1-key attempt failed with sandbox DNS and is not treated
    as successful. No matching Micromonospora dataset was found in the catalog. Neither
    absence nor module membership proves resistance or chemical identity.
  snapshot_sha256: 9c4f9037a8b4f4e6163053e55ad9f9e7292f870234f335be5fbe4e9bb80ddaac
- evidence_id: pmid-11083623
  kind: database
  reference: https://pubmed.ncbi.nlm.nih.gov/11083623/
  locator: Original review metadata; no abstract in EPMC
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: The definition citation is an aminoglycoside mechanism/resistance review.
    Full text retrieval failed (EPMC 500, PMC challenge, alternative403). It is not
    treated as a new exact-A experiment or as fully read.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: pmid-10103173
  kind: database
  reference: https://pubmed.ncbi.nlm.nih.gov/10103173/
  locator: Original review metadata; no abstract in EPMC
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: Second adopted definition lead is an aminoglycoside activity/resistance
    review. Full text remained inaccessible through the attempted public routes; no
    claim of exact-A assay verification is made.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: pmid-8385262
  kind: database
  reference: https://pubmed.ncbi.nlm.nih.gov/8385262/
  locator: Original review abstract
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: This is a molecular-genetics review of modifying enzymes, used for the
    class and AAC(3)-IIIc lead. The abstract does not supply a purified gentamicin-A
    substrate experiment; full text was not readable through the attempted routes.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: pmid-2833561
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/2833561/
  locator: Original abstract
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: Tn4001 aacA-aphD from S. aureus is cloned and expressed in E. coli; activities
    and insertion-mutant domain attribution distinguish AAC and APH functions. Gentamicin
    is named without exact A preparation. No quantitative result is transferred.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: pmid-10021417
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/10021417/
  locator: Original abstract
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: Purified recombinant AAC(6′)-APH(2″) has broad substrate specificity and
    unusual modifications of other aminoglycosides. The abstract explicitly discusses
    therapeutic gentamicin C; it does not establish identical activity on gentamicin
    A.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: pmid-11959575
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/11959575/
  locator: Original abstract
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: S. marcescens SCH909 integron study characterizes the ANT(3″)-I/AAC(6′)-II
    fusion and associated resistance genes. Exact gentamicin A material is not identified
    in the inspected abstract; full-text routes failed.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: pmid-15561846
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/15561846/
  locator: Original abstract
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: P. aeruginosa 101-4704 integron includes aac(6′)-30/aac(6′)-Ib′, alongside
    IMP16. Detailed beta-lactamase kinetics are not aminoglycoside-A evidence. Exact-A
    substrate testing is unverified.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: pmid-17030911
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/17030911/
  locator: Original abstract
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: E. casseliflavus HZ95 aph(2″)-Ie-containing plasmid fragment confers gentamicin
    resistance in E. coli DH5alpha. The abstract does not identify purified gentamicin
    A and is not an assay of every congener.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: pmid-9055984
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/9055984/
  locator: Original abstract
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: E. gallinarum SF9117 aph(2″)-Ic, now ARO APH(2″)-IIIa, is cloned into E.
    coli; the reported gentamicin phenotype and ampicillin synergy failure are strain/assay
    specific. No exact-A test preparation is established.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: pmid-9593155
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/9593155/
  locator: Original abstract
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: E. casseliflavus UC73 aph(2″)-Id, now APH(2″)-IVa, confers gentamicin resistance
    after cloning in E. coli. Clinical detection and combination-killing observations
    are not purified gentamicin-A evidence.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: pmid-17875999
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/17875999/
  locator: Original abstract
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: NpmA from E. coli ARS3 modifies A1408, with 30S-subunit methylation and
    drug-footprinting evidence. Gentamicin is named generically; the congener is not
    identified. The abstract supports NpmA mechanism but not exact-A material attribution.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: pmid-26488937
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/26488937/
  locator: Original abstract and full-XML screening/material paragraphs
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: The study screens NDM1-positive P. aeruginosa isolates and identifies RmtC
    with RmtF co-carriage in one. Growth at 256 mg/L each amikacin/gentamicin is a
    screening condition, not an exact-A MIC or isolated RmtF-only causal effect.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: pmid-22547620
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/22547620/
  locator: Original abstract
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: RmtF in K. pneumoniae BM4686 resides on pIP849 and is cotranscribed with
    aac(6′)-Ib. The abstract establishes the methyltransferase-family context and
    resistance to a class, without identifying purified gentamicin A.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: pmid-17158944
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/17158944/
  locator: Original abstract
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: RmtD from Brazilian P. aeruginosa PA0905 is characterized by cloning and
    high-level aminoglycoside resistance. The generic gentamicin result is not a resolved
    exact-A assay.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: pmid-18222955
  kind: database
  reference: https://pubmed.ncbi.nlm.nih.gov/18222955/
  locator: Original metadata only; no abstract
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: This is the adopted K. pneumoniae RmtD report. EPMC fullTextXML500 and
    PMC/EuropePMC access restrictions prevented source-body inspection. Its title
    alone is not used to assign a strain, MIC or gentamicin-A preparation.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: pmid-23459483
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/23459483/
  locator: Original abstract
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: Eight Brazilian K. pneumoniae clinical strains include RmtD1/D2 and novel
    RmtG, frequently with KPC2/CTX-M. This source concerns K. pneumoniae, not the
    P. aeruginosa wording in the external ARO definition; the native entry itself
    does not assert that taxon. Exact gentamicin-A testing remains unverified.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: pmid-23959310
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/23959310/
  locator: Original abstract plus main HTML methods/results on APH(2″)-Ig
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: C. coli N29710/N29716 plasmid and transfer studies are separated from synthesized
    aph(2″)-Ig expression in E. coli DH5alpha. The latter increases generic gentamicin
    MIC 0.25→32 micrograms/mL with IPTG. Exact A is not specified; this numerical
    result is not attached to the native compound.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: pmid-23478957
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/23478957/
  locator: Original abstract and full main HTML text
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: RmtH from K. pneumoniae MRSN2404 is cloned in E. coli; MIC and Etest results
    use generic gentamicin. G1405 specificity is inferred in this paper from phenotype/alignment,
    not directly measured methylation. Exact A is not established.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: pmid-11961556
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/11961556/
  locator: Original abstract, public Fig. 3 caption and actual Fig. 3 image
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: PvrR regulates resistant/susceptible biofilm variants. In Fig. 3, overexpression
    reduces variant frequency/attachment and deletion increases variant frequency.
    The figure does not establish purified gentamicin-A resistance, direct target
    binding or a porin deletion. Full main text remained subscription-limited; native
    UNKNOWN/database scope is retained.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: pmid-23129050
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/23129050/
  locator: Original abstract
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: APH(2″)-If from C. jejuni prefers GTP and phosphorylates a subset of 4,6-disubstituted
    aminoglycosides. Generic gentamicin is included, but the inspected abstract does
    not identify exact A. Full text routes were unavailable.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: pmid-21078935
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/21078935/
  locator: Original abstract
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: rmtD2 is identified in Argentine Enterobacteriaceae and associated with
    broad clinical-aminoglycoside resistance and a conjugative element. No purified-A
    assay is identified in the inspected source depth.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: pmid-20368404
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/20368404/
  locator: Original abstract
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: Bovine E. coli resistance phenotyping and genetic analysis discover rmtE.
    Gentamicin and amikacin are reported generically, so material-specific quantitative
    transfer is not justified.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: pmid-26392485
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/26392485/
  locator: Full main HTML text; original has no abstract
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: Swine E. coli S68/87 carry rmtE2 with Val6Ala relative to rmtE; plasmid
    transfer into E. coli C600 yields aminoglycoside resistance. Generic gentamicin
    and amikacin MICs are reported, without identifying purified gentamicin A.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: pmid-31578249
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/31578249/
  locator: Original abstract; full-XML aminoglycoside results and methods
  accessed_at: '2026-10-21T17:27:05.416828Z'
  support: context_only
  summary: AAC(3)-IVb from C. gilardii W2-2 reduces gentamicin/tobramycin susceptibility
    in E. coli BW25113 constructs. Methods use Becton Dickinson disks and 100 micromolar
    IPTG on Mueller-Hinton agar; this is disk susceptibility, not a direct enzymatic
    kinetic assay or purified gentamicin-A MIC.
  snapshot_sha256: 7e13e3d39c9403a75e45d345d2bc54d68a74140ebce5758f671e1af8bade5841
- evidence_id: res-rmtF
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4622239/fullTextXML
  locator: Screening/material paragraphs
  accessed_at: '2026-10-21T17:29:03.122312Z'
  support: context_only
  summary: Read at the explicitly bounded depth recorded in the corresponding PMID
    evidence entry; material, organism and assay boundaries were retained. This snapshot
    is not used as proof of purified gentamicin-A resistance.
  snapshot_sha256: fd6dede13aadb5fa0f508225dcdf0b091245423af5237065028ab83c825a4446
- evidence_id: res-rmtE2
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4649190/?pdf=1
  locator: Main letter text
  accessed_at: '2026-10-21T17:29:33.617059Z'
  support: context_only
  summary: Read at the explicitly bounded depth recorded in the corresponding PMID
    evidence entry; material, organism and assay boundaries were retained. This snapshot
    is not used as proof of purified gentamicin-A resistance.
  snapshot_sha256: 981c56277ae28933b79b31712dd477a56ab1fab73aa197fb762dd8447c748efd
- evidence_id: res-aphIg
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3811239/?pdf=1
  locator: Methods and APH(2″)-Ig cloning/result paragraphs
  accessed_at: '2026-10-21T17:29:33.943411Z'
  support: context_only
  summary: Read at the explicitly bounded depth recorded in the corresponding PMID
    evidence entry; material, organism and assay boundaries were retained. This snapshot
    is not used as proof of purified gentamicin-A resistance.
  snapshot_sha256: f44aa29a228e3369d5b57360243c1437519a557f3983d9e3d377a87edc17b4fe
- evidence_id: res-rmtH
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3632941/?pdf=1
  locator: Full main letter text
  accessed_at: '2026-10-21T17:29:33.993856Z'
  support: context_only
  summary: Read at the explicitly bounded depth recorded in the corresponding PMID
    evidence entry; material, organism and assay boundaries were retained. This snapshot
    is not used as proof of purified gentamicin-A resistance.
  snapshot_sha256: 389c9f2a5a971d1f5755670e60543abcbe5b058a3ad45e8d484afebff00481e9
- evidence_id: res-aacIVb
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6796972/fullTextXML
  locator: Aminoglycoside results and susceptibility/cloning methods
  accessed_at: '2026-10-21T17:29:02.936857Z'
  support: context_only
  summary: Read at the explicitly bounded depth recorded in the corresponding PMID
    evidence entry; material, organism and assay boundaries were retained. This snapshot
    is not used as proof of purified gentamicin-A resistance.
  snapshot_sha256: 468c4d41174ac9d1a403153bd9f129bfa55aff80a608b34b7a01f9b4d3cc4909
- evidence_id: res-pvrR
  kind: primary_source
  reference: https://media.springernature.com/lw1200/springer-static/image/art%3A10.1038%2F416740a/MediaObjects/41586_2002_Article_BF416740a_Fig3_HTML.jpg
  locator: Actual public Fig. 3, panels d–f
  accessed_at: '2026-10-21T17:32:01.555375Z'
  support: context_only
  summary: Read at the explicitly bounded depth recorded in the corresponding PMID
    evidence entry; material, organism and assay boundaries were retained. This snapshot
    is not used as proof of purified gentamicin-A resistance.
  snapshot_sha256: f99750aae651cb8b925bf4a7878ed5453b6976648c21fadb453e4b9666ff724a
- evidence_id: garamycin
  kind: authority
  reference: https://www.accessdata.fda.gov/drugsatfda_docs/nda/2004/065024_S000_Gentamicin%20Ophthalmic%20Ointment_MICROR.pdf
  locator: 'FDA ANDA 65024 microbiology review, PDF page 19 (June 29, 2004): proprietary/non-proprietary
    product identity'
  accessed_at: '2026-10-21T17:32:01.555708Z'
  support: refutes
  summary: The actual scanned page 19, headed Product Quality Microbiology Review,
    identifies proprietary Garamycin and non-proprietary Gentamicin Sulfate Ophthalmic
    Ointment USP, 0.3%. This establishes a marketed product name, not an exact chemical
    synonym of free-base gentamicin A. No current approval status is inferred.
  snapshot_sha256: 199e786fe96faed1fe09980e906c4ee6bbd5a820caf8acb6901f7cc3bcfb7d42
- evidence_id: product-mixture
  kind: authority
  reference: https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=51a411a0-2671-4c1c-bf25-e29b32efed0c
  locator: DailyMed gentamicin sulfate ophthalmic solution description
  accessed_at: '2026-10-21T17:29:02.463280Z'
  support: supports
  summary: The official label describes gentamicin as a mixture of sulfate salts of
    C1, C2 and C1A. This corroborates the drug/product versus A-congener boundary
    and supplies no claim of purified-A clinical use.
  snapshot_sha256: c15f713bfb9d95ce8a0883cd1aef8122d5829d8b96ab7ae41561c308fbde9b55
- evidence_id: access
  kind: validation
  reference: 499-fetch1.json through 499-fetch5.json
  locator: Actual public retrieval URLs, timestamps, status codes and content hashes
  accessed_at: '2026-10-21T17:35:23Z'
  support: context_only
  summary: Original J-STAGE structure/synthesis/production PDFs, chemical authorities,
    selected PMC texts and public Nature Fig. 3 were retrieved. Many EPMC fullTextXML
    requests returned 500 and PMC HTML returned browser-challenge pages despite HTTP
    200. ACS 1967/1970 PDFs returned 403; a public 1970 copy could not connect. The
    1970 search excerpt was a discovery lead only, not the finding basis. CAS API
    returned 401. Failed bodies were not treated as inspected papers.
  snapshot_sha256: 176d8e216b03ff985a23e7c12e2dfd7eecbab9b015d3020e17af082783a7262f
- evidence_id: garamycin-page
  kind: authority
  reference: https://www.accessdata.fda.gov/drugsatfda_docs/nda/2004/065024_S000_Gentamicin%20Ophthalmic%20Ointment_MICROR.pdf
  locator: Actual PDF page 19 scanned image, visually inspected
  accessed_at: '2026-10-21T17:32:01.555708Z'
  support: refutes
  summary: The proprietary and non-proprietary product names are printed together
    on the inspected FDA page; the image is preserved for independent audit.
  snapshot_sha256: e1c854245873fda23c45c66a04b1ea66dff3b23f676959ff3e54c731dc878bbc
assessments:
- assessment_id: identity
  area: identity
  topic: Natural gentamicin A versus stored L-gentosamine graph
  outcome: concern
  summary: Primary explicit D-gentosamine chemistry, the 1980 full-structure confirmation
    and 2015 Figure 1 agree. Four mapped sugar centres in the native graph encode
    the opposite sugar enantiomer within the same larger molecule; it is a diastereomer
    of natural A. Current ChEBI reproduces that error. The D candidate exactly matches
    PubChem/KEGG.
  target_ids:
  - CHEBI:28418
  evidence_ids:
  - native
  - primary1977
  - primary1980
  - primary1980-figure
  - biosynthesis-figure
  - sugar-map
  - comparison
- assessment_id: grounding
  area: grounding
  topic: Exact chemical xrefs, source mint and broader parents
  outcome: concern
  summary: Both source mints are reproducible. PubChem/KEGG support the corrected
    natural D graph; their mismatch should be repaired through native identity adjudication.
    ChEMBL independently adds a glucosamine N-hydroxy oxygen and remains incompatible
    after that repair. Broader gentamycin/aminoglycoside parents resolve; CAS independent
    stereochemistry is limited.
  target_ids:
  - CHEBI:28418
  evidence_ids:
  - chemistry
  - chebi
  - pubchem
  - kegg
  - chembl
  - comparison
  - parents
  - cas-access
- assessment_id: synonyms
  area: nomenclature
  topic: D/L systematic names and Garamycin
  outcome: concern
  summary: The L-systematic synonym matches the wrong native sugar, whereas the D-systematic
    synonym matches primary natural identity. Correct the structure and associated
    systematic name coherently. Garamycin belongs to the gentamicin sulfate product
    context and should not remain an exact chemical synonym for A.
  target_ids:
  - CHEBI:28418
  evidence_ids:
  - native
  - sugar-map
  - primary1977
  - garamycin
  - product-mixture
- assessment_id: definition
  area: evidence
  topic: Generic aminoglycoside mechanism and adopted definition sources
  outcome: unknown
  summary: The source definition distinguishes A as part of a complex and then discusses
    gentamicin generically. Its two adopted reviews resolve but their full texts were
    inaccessible. Primary natural-A production is verified, while a direct purified-A
    ribosome/bactericidal experiment was not independently established here. No broad
    quantitative mechanism or target is added.
  target_ids:
  - CHEBI:28418
  evidence_ids:
  - native
  - pmid-11083623
  - pmid-10103173
  - production
  - biosynthesis
- assessment_id: activity
  area: evidence
  topic: Antibacterial eligibility and material-specific assays
  outcome: supported
  summary: The isolated natural-A band is bioactive against E. coli in the 1980 source,
    supporting qualitative antibacterial eligibility for the intended natural compound.
    Analog 1/gentamicin-C MICs in 1977 and minor X-14847 MICs in 1980 are excluded
    from A. No activity of the native L-sugar diastereomer is claimed or disproved.
  target_ids:
  - CHEBI:28418
  evidence_ids:
  - production
  - primary1977
  - primary1980
  - native
- assessment_id: resistance
  area: evidence
  topic: All nineteen imported CARD associations and twenty-four adopted PMID leads
  outcome: unknown
  summary: 'Every native entry explicitly identifies a database assertion, and current
    ARO preserves those relationships. All 24 unique adopted leads were dispositioned:
    abstracts/metadata for all and selected original main text/figure passages where
    accessible. Inspected experiments mainly name generic/clinical gentamicin; none
    inspected here resolves purified A. This limitation does not by itself prove every
    retained database association false or justify a new major for missing optional
    primary evidence.'
  target_ids:
  - CHEBI:28418
  evidence_ids:
  - native
  - aro
  - adapter
  - pmid-11083623
  - pmid-10103173
  - pmid-8385262
  - pmid-2833561
  - pmid-10021417
  - pmid-11959575
  - pmid-15561846
  - pmid-17030911
  - pmid-9055984
  - pmid-9593155
  - pmid-17875999
  - pmid-26488937
  - pmid-22547620
  - pmid-17158944
  - pmid-18222955
  - pmid-23459483
  - pmid-23959310
  - pmid-23478957
  - pmid-11961556
  - pmid-23129050
  - pmid-21078935
  - pmid-20368404
  - pmid-26392485
  - pmid-31578249
- assessment_id: pvrR
  area: scope
  topic: Regulator direction and exact congener scope
  outcome: unknown
  summary: Public original Fig. 3 supports effects on phenotypic variant frequency
    and attachment, with opposite directions for overexpression and deletion. It does
    not establish a generic PvrR-presence resistance mechanism or exact-A susceptibility.
    The native UNKNOWN mechanism and explicit database provenance remain important;
    additional allele/condition qualification is a bounded follow-up.
  target_ids:
  - CHEBI:28418
  evidence_ids:
  - native
  - pmid-11961556
  - res-pvrR
  - adapter
- assessment_id: producer
  area: scope
  topic: Natural production and biosynthesis versus antimicrobial targets
  outcome: supported
  summary: Natural A is isolated from M. echinospora X-14847/NRRL B-12180 and is a
    biosynthetic intermediate in ATCC 15835. GenD/GenS/GenN chemistry is production/substrate
    context, not evidence of antimicrobial target inhibition. Producer/biosynthesis
    fields are optional and absent, so their omission is not a schema finding.
  target_ids:
  - CHEBI:28418
  evidence_ids:
  - production
  - biosynthesis
  - biosynthesis-figure
- assessment_id: completeness
  area: completeness
  topic: Existing claim coverage and optional enrichment
  outcome: unknown
  summary: The entire native record and actual adopted owners were inspected. Bibliography
    coverage includes both definition reviews, class lead and all resistance leads
    with explicit reading depth. Exact-A quantitative spectrum, direct target and
    resistance-material evidence remain bounded follow-ups after the identity correction;
    no optional field is called invalid merely because absent.
  target_ids:
  - CHEBI:28418
  evidence_ids:
  - native
  - owners
  - search
  - aro
  - access
- assessment_id: provenance
  area: provenance
  topic: Generated ownership, snapshots and history
  outcome: supported
  summary: The original thirteen hashes are preserved in twenty-seven verified inputs.
    ChEBI/ARO raw rows, qualification owners, current source conflicts and all three
    seed/reseed history events were read. No history/status promotion is authorized
    by this review.
  target_ids:
  - CHEBI:28418
  evidence_ids:
  - owners
  - native
  - chemistry
  - search
- assessment_id: validation
  area: schema
  topic: Successful internal gates despite natural-identity error
  outcome: supported
  summary: Schema, strict and internal chemistry checks pass. They establish consistent
    encoding of the wrong sugar stereoisomer and do not supersede primary source adjudication.
  target_ids:
  - CHEBI:28418
  evidence_ids:
  - chemistry
  - sugar-map
  - primary1977
findings:
- finding_id: F1
  issue_key: gentamycin-a-l-gentosamine-instead-of-natural-d
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Four gentosamine stereocentres encode the wrong natural-product identity
  description: Natural gentamicin A has alpha-D-gentosamine. The stored ChEBI-derived
    SMILES/InChI/key and L-systematic synonym instead encode the mirror-image sugar
    within an otherwise matching molecule. Original 1977 text and compound 2 drawing
    explicitly establish D-xylose; 1980 structure 9 and 2015 A (6) corroborate it.
    Native SMILES indices 5/3/2/30 map to C1″/C2″/C3″/C4″ with S/S/R/R; their inversion
    gives R/R/S/S and exactly the current PubChem/KEGG QVNYEEQUSA graph. This is a
    genuine four-centre diastereomer difference, not a CIP naming or ring-conformation
    change.
  target_ids:
  - CHEBI:28418
  field_paths:
  - chemical_structure
  - grounding_status
  - synonyms[0]
  - source_concepts[1]
  evidence_ids:
  - native
  - chebi
  - primary1977
  - primary1980
  - biosynthesis-figure
  - sugar-map
  - comparison
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: ChEBI structure, synonyms and chemical xrefs
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated chemical field owner
  rule_id: review-yaml-record:Workflow:identity
  native_severity: blocker
  normalization_reason: The native rubric classifies a record denoting the wrong stereochemical
    identity as blocker. Primary source text, drawings and explicit atom mapping support
    this beyond a database disagreement.
- finding_id: F2
  issue_key: gentamycin-a-chembl7225-extra-oxygen
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: The exact ChEMBL xref is an oxygenated constitutional mismatch
  description: CHEMBL7225 currently encodes C18H36N4O11 with an N-hydroxy substituent
    on the glucosamine residue and different/partial stereochemistry. Gentamicin A
    and both native/D-sugar candidate graphs are C18H36N4O10. This exact xrefs entry
    remains wrong even after the four-centre identity repair; the discrepancy is not
    a salt, solvate or tautomer.
  target_ids:
  - CHEBI:28418
  field_paths:
  - xrefs[3]
  evidence_ids:
  - chembl
  - comparison
  - native
  - primary1980
  - biosynthesis
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: ChEBI structure, synonyms and chemical xrefs
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated chemical field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO synonym and cross-reference assertions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  rule_id: review-yaml-record:Workflow:identity
  native_severity: major
  normalization_reason: An exact chemical cross-reference to a different molecular
    constitution is major. The separate native natural-identity failure is classified
    as blocker.
- finding_id: F3
  issue_key: gentamycin-a-garamycin-product-exact-synonym
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: Garamycin is a gentamicin product name rather than an exact synonym of congener
    A
  description: The imported ARO synonym marks Garamycin as EXACT_SYNONYM. Official
    FDA product identification associates that name with gentamicin sulfate ophthalmic
    product, and the official gentamicin description identifies a C-component sulfate
    mixture. It is not an exact chemical synonym for the free-base A congener.
  target_ids:
  - CHEBI:28418
  field_paths:
  - synonyms[4]
  evidence_ids:
  - native
  - aro
  - garamycin
  - product-mixture
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO synonym and cross-reference assertions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  rule_id: review-yaml-record:Workflow:identity
  native_severity: minor
  normalization_reason: This is a localized synonym scope/typing correction; it does
    not independently alter the already assessed molecular graph.
actions:
- action_id: A1
  description: Adjudicate and repair the natural gentamicin-A stereochemical identity
    through maintained inputs.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:28418
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: ChEBI structure, synonyms and chemical xrefs
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated chemical field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Publication-backed exact structure if an override is needed
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding decision if current ChEBI cannot represent the curated identity
  acceptance_checks:
  - Use the original D-gentosamine source and explicit C1″–C4″ atom map; invert only
    the four implicated sugar centres and verify all other stereocentres/linkages
    are preserved.
  - Recompute structure fields coherently and correct the alpha-L systematic synonym.
    The resulting candidate should reproduce QVNYEEQUSA and match current KEGG/PubChem
    with chirality.
  - Resolve continued EXACT grounding to CHEBI:28418 if the live authority still encodes
    the L-sugar graph; use supported grounding/curator mechanisms rather than a silent
    generated edit.
  - Regenerate through maintained owners, run focused schema/strict and chemistry/xref
    checks plus required corpus reference/history/reproduction/QC gates, and inspect
    the exact diff.
  generator: scripts/seed_from_sources.py
- action_id: A2
  description: Remove or remap the chemically incompatible ChEMBL exact xref.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:28418
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: ChEBI structure, synonyms and chemical xrefs
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated chemical field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO synonym and cross-reference assertions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  acceptance_checks:
  - Confirm the current CHEMBL7225 extra oxygen and stereochemistry at curation time.
    Do not replace it by label matching alone.
  - Retain the natural-product source evidence and verify the final exact-xref set
    against the repaired D-sugar graph.
  - Fix every contributing adopted source/transform, regenerate and run exact chemical/xref
    and required corpus checks.
  generator: scripts/seed_from_sources.py
- action_id: A3
  description: Remove Garamycin from exact chemical synonyms for gentamicin A or retain
    only an explicitly justified broader product association.
  finding_ids:
  - F3
  target_ids:
  - CHEBI:28418
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO synonym and cross-reference assertions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  acceptance_checks:
  - Use the official product identity and preserve A-versus-C-mixture scope. Do not
    claim purified A is the marketed active ingredient.
  - Correct the ARO-source synonym handling reproducibly; regenerate and inspect synonym
    types and scientific identity checks.
  generator: scripts/seed_from_sources.py
- action_id: A4
  description: 'Optional follow-up: qualify resistance and enrich natural-A evidence
    only after exact identity is repaired.'
  finding_ids: []
  target_ids:
  - CHEBI:28418
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Imported resistance association
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Claim-level CARD qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Qualification transform
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated resistance claim owner
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/gentamycin-a.yaml
    role: Future curator-owned activity, producer and target annotations
  acceptance_checks:
  - Retain the existing database-only notes; do not promote generic gentamicin studies
    to exact-A primary evidence. Retrieve preparation/method details and map each
    enzyme, strain and allele independently.
  - For PvrR distinguish overexpression from deletion and variant-frequency/attachment
    from drug-specific MIC. Do not import external porin wording without primary support.
  - Natural-A isolated-band activity can be added qualitatively with its E. coli assay
    boundary; do not copy analog 1/C-complex or minor X-14847 MICs. Biosynthetic enzymes
    must not become antimicrobial targets.
  - Any later native edits require the separate validated writer/history workflow.
limitations:
- Required shared full-corpus checks are incorporated separately by the root reviewer
  before finalization; the actual focused gates are recorded here.
- 'Original 1967/1970 ACS full texts were unavailable: publisher 403 and the public
  1970 mirror did not connect. The 1970 search excerpt is not evidence for the finding.
  The identity conclusion instead uses directly inspected 1977/1980 original PDFs,
  2015 source figure and explicit graph/atom comparison.'
- Of 24 adopted definition/class/resistance PMID leads, all original metadata and
  available abstracts were read. Selected full source text or figure passages were
  inspected for 26488937,26392485,23959310,23478957,31578249 and 11961556. The remaining
  papers were not all read in full; 11083623,10103173 and 18222955 remained metadata-only
  because no abstract/full text was accessible.
- Several PMC requests returned a browser challenge despite HTTP 200; EPMC fullTextXML
  returned 500 for many adopted papers. These were not treated as full-text access.
  The public Nature Fig. 3 is accessible but the full 2002 main text is subscription-limited.
- No exact-A resistance MIC or direct ribosome inhibition/bactericidal assay was established
  from the inspected sources. Natural-A qualitative antibacterial activity is supported,
  and the native L-sugar diastereomer is not assumed either active or inactive.
- CAS API access returned 401 and the page was a client shell, so CAS-specific stereochemical
  agreement was not independently verified. The 2015 supplementary files and every
  historical structure reference were not exhaustively reanalyzed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All original capture hashes are preserved. No native record, source table, curation
  history, progress file or immutable bundle was edited.
- Independent validation_plan review of original 1977/1980 source and four-centre
  graph inversion agreed with the stereochemical identity finding; this does not replace
  root final audit.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
tags:
- record-review
- queue-499
- gentamicin-A
- read-only
```
