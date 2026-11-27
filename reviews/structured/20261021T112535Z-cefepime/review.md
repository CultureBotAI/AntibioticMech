# Cefepime: identity and 31 isolate observations agree; retain context on imported protein associations

- Review: 20261021T112535Z-cefepime
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T11:08:24Z
- Finished UTC: 2026-10-21T11:25:35Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The exact cefepime zwitterion is chemically coherent and its official identifiers agree. All 31 native isolate observations retain the source result &gt;32 mg/L and resistant interpretation; all 28 asserted BioSamples resolve. The 13 CARD resistance associations and generic PBP target reproduce the maintained and current source and remain explicitly database assertions. Original studies support PBP interaction and several context-dependent resistance mechanisms, while hydrolysis, small MIC shifts and clinical resistance must remain distinct. No material native error was established. Two informational follow-ups concern optional primary PBP evidence and source-bound qualification of resistance context. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole CHEBI:478164 record: definition, eleven synonyms, chemical and drug xrefs, parents and roles, exact chemical descriptors, both source concepts, eleven adopted citation leads, 31 activity observations, thirteen resistance entries, the PBP target and all 25 history entries.

Selection: Queue 222. Initial capture retained; actual ARO and CARD qualification owners and six additional input hashes appended before scientific judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:478164 | data/antibiotics/antibacterial/cefepime.yaml | generated | cefepime |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:478164 | Actual focused command exited 0. |
| strict | passed | True | CHEBI:478164 | Actual focused command exited 0. |
| chemistry | passed | False | CHEBI:478164 | Actual focused command exited 0. Batch019 RDKit interpreter independently parsed the batch023 native SMILES and InChI and reproduced both source mints. |
| Authoritative full QC | failed | True | CHEBI:478164 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:478164 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:478164 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:478164 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:478164 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:478164 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:478164 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:478164 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:478164 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact zwitterion and identifiers

identity: supported. Targets: CHEBI:478164.

The native chemical graph, formula, stereo and identifiers are coherent. Salt and protonation representations in experimental or deposition contexts are explicitly distinguished.

### All 31 curated isolate observations

quantity: supported. Targets: CHEBI:478164.

Every native &gt;32 mg/L result and R interpretation agrees with its cited CDC record. Accessions and organism scope agree, including compatible narrower BioSample species labels. Source breakpoint editions are retained rather than retrospectively recalculated.

### Generic PBP target and optional primary evidence

evidence: supported. Targets: CHEBI:478164.

The present target is an honestly labeled database assertion. Original membrane competition supports PBP interaction in defined strains and a sulfate preparation; curated primary claims would require their own experimental scope and endpoint.

### Thirteen imported resistance associations

scope: supported. Targets: CHEBI:478164.

Every association reproduces current CARD and is explicitly database sourced. Inspected primary examples support context-dependent effects; biochemical hydrolysis, modest MIC increases and clinical resistance are not interchangeable. Exact quantitative support was not fully adjudicated for every edge.

### All eleven adopted citation leads

evidence: supported. Targets: CHEBI:478164.

All adopted abstracts were read and separated into review, microbiology, clinical, toxicity and pharmacokinetic contexts. None supplies an unqualified producer, exact target or clinical approval assertion.

### Optional mechanisms and primary qualifications

completeness: unknown. Targets: CHEBI:478164.

Specific primary target and resistance context can be added through the maintained curation surfaces. Absence of a graph, producer or clinical status is not an error and does not establish that such information is unavailable elsewhere.

### Source and curation ownership

ownership: supported. Targets: CHEBI:478164.

Initial input hashes remain unchanged. Actual ARO and role/qualification owners were captured before judgment. Native CDC additions and imported CARD associations have distinct maintained owners.

### Focused validation

schema: supported. Targets: CHEBI:478164.

Documented schema and strict validation and independent chemistry pass; scientific status remains SEEDED.

## Findings

### F1: Primary PBP evidence is available for a qualified future target update

informational / open / confirmed; issue key: cefepime-primary-pbp-context-enrichment.

The current generic PBP target correctly remains a database assertion with PRIMARY_EVIDENCE_NEEDED. The inspected 1991 experiment supplies membrane competition and morphology data for defined strains using cefepime sulfate. A future primary update should preserve this reagent and assay scope rather than treating competition IC50 as a binding constant or claiming an intact salt is the bound species.

### F2: Retain host, mutation and endpoint context when qualifying CARD resistance associations

informational / open / confirmed; issue key: cefepime-resistance-context-qualification.

The thirteen imported associations are reproducible and explicitly database sourced. Inspected primary studies show why a later qualification should distinguish hydrolysis, small MIC changes, loss or mutation of porins, expression-dependent efflux and clinical resistant phenotypes. In particular, LAP-1 and LAQ-1 hydrolysis and the KPC-123 clone results do not establish resistant cefepime phenotypes in every host. No edge deletion is justified solely by these bounded comparisons.

## Recommended Actions And Acceptance Checks

### A1

If adding primary PBP evidence, curate the exact reagent, organism and experimental endpoint.

- Use PMID 1804003 with its cefepime sulfate material, E. coli K-12 and P. aeruginosa SC8329 backgrounds. Keep membrane competition IC50, whole-cell MIC and morphology observations separate.
- Do not turn the generic PBP family into an unsupported exact protein accession. Inspect a primary sequence or structure mapping before adding any protein example. For PMID 29357220/PDB 5OJ0, verify the full methods, noncovalent binding interpretation and protonation context before curation.
- Attach evidence to the narrow native claim and preserve any salt-to-active-moiety qualification. Use write_validated_antibiotic and record_curation_event under a separately authorized curation task, then run focused and applicable shared gates.

### A2

If strengthening resistance evidence, add source-bound qualifications for the exact CARD rows after completing primary checks.

- Bind any qualification to the exact source row and retain the CARD database evidence type. Distinguish observed hydrolysis from resistant whole-cell phenotypes and record host, construct, comparator, MIC inequality and source breakpoint context where applicable.
- For porins, preserve the loss, mutation or expression background rather than implying that normal OmpF/OmpK35/Omp36 presence causes resistance. For efflux, preserve the knockout, complementation or regulatory experiment and avoid assigning a regulatory protein as a drug target.
- Complete accessible exact cefepime primary checks for ACC-1, SCO-1, LAP-2 and VIM-63 before claiming universal primary support or proposing removal. Do not infer absence of activity from inaccessible full text, low activity in one assay or absence of a citation on the current CARD page.
- Keep the independently curated CDC isolate phenotypes separate from mechanism attribution. A listed genotype alone does not explain every isolate MIC or establish causation. Regenerate qualified imports and run applicable gates if future source curation is authorized.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/cefepime.yaml; Entire YAML, all fields and 25 history entries. | supports | SEEDED/EXACT record denotes cefepime as a net-neutral zwitterion. The thirteen resistance entries explicitly identify CARD database assertions. The generic PBP target has PRIMARY_EVIDENCE_NEEDED and is not presented as a primary experiment. No structured mode_of_action, causal graph, producer or clinical_status is present. Optional absence is not a schema defect. |
| source | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv; data/raw/aro_resistance_edges.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; conf/sources.yaml; ChEBI row 2973, ARO antibiotic row 44, target row 45 and resistance rows 1398–1410; extraction lines 450–530 and seeding lines 1750–1830. | supports | The source rows supply the exact identity, source aliases and citation leads, generic PBP edge and thirteen resistance associations. Extraction maps source ancestors to resistance mechanism categories. Seeding preserves database-only notes and PRIMARY_EVIDENCE_NEEDED for the target. Both source concepts and minted identifiers reproduce. Curated CDC observations are owned by the native record, not inferred from the ARO edges. |
| qualification-owner | conf/aro_target_roles.tsv; curation/card_evidence_reviews.json; scripts/card_evidence_reviews.py; PBP role mapping, complete qualification registry exact-match search, loader and qualification application code. | supports | The PBP family is mapped as a direct binding protein target. No exact cefepime qualification row was found in the maintained registry. Existing machinery binds qualifications to the exact source row hash and appends primary-source context without silently upgrading a database assertion to a primary evidence type. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:478164; Current chemical entry, identifiers, aliases, roles, parents and structures. | supports | Native definition, six ChEBI aliases, CAS 88040-23-7, formula C19H24N6O5S2, net charge 0, masses and full key HVFLCNVBZFFHBT-ZKDACBOMSA-N agree. CHEBI:23066 denotes cephalosporin and CHEBI:36816 oxime O-ether; antimicrobial and antibacterial-drug roles are consistent. Native geometry is the 6R,7R cephalosporin with a Z oxime. |
| chemical-xrefs | https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL186; https://pubchem.ncbi.nlm.nih.gov/compound/5479537; https://rest.kegg.jp/get/C08111; https://rest.kegg.jp/get/D02376; https://drugcentral.org/drugcard/535; Official property records, both KEGG entries and structure MOL, DrugCentral InChI; independent structure comparison. | supports | All independently parsed structures reproduce the native full key, formula, charge and two R stereocentres. The native KEGG compound/drug, ChEMBL, PubChem and DrugCentral identifiers resolve to cefepime. KEGG PubChem links are substance identifiers, not competing compound CIDs. DrugCentral identity data were used; its generated assistant prose was not treated as experimental evidence. |
| drugbank | https://go.drugbank.com/drugs/DB01413; Public DrugBank identity overview inspected through web retrieval after direct HTTP 403. | supports | DB01413 is cefepime and its public identity summary gives the native full InChIKey and matching structure identifiers. Restricted target or assay sections were not inspected and are not used as primary evidence. |
| patents | https://patents.google.com/patent/US4406899A/en; https://patents.google.com/patent/DE3307550A1/en; Patent metadata and selected description identifying compound Ia. | partial | Both native document identifiers resolve to the corresponding cephalosporin disclosure. Compound Ia has cefepime’s Z methoxyimino aminothiazolyl side chain and methylpyrrolidinium substituent. This supports exact synthetic-document relevance; the full claims, every example and all biological tables were not independently audited. |
| other-xrefs | https://en.wikipedia.org/wiki/Cefepime; https://www.ebi.ac.uk/chebi/CHEBI:478164; Native informational link and official xref list. | context_only | The encyclopedia link resolves to the same named drug and is used only as link context. Reaxys 7453587 and CAS 88040-23-7 are officially attested in ChEBI; subscription registry contents were not inspected. Broad brand aliases supplied by ARO are source labels, not assertions that every marketed formulation has this exact composition. |
| cdc | https://wwwn.cdc.gov/ARIsolateBank/; 222-cdc-comparison.json; 222-cdc-*.html; Each of the 31 exact native isolate pages: identity, cefepime result row, method/breakpoint footnote and asserted isolate attributes. | supports | Every native cefepime observation agrees with its cited CDC page: MIC &gt;32 micrograms/mL, equivalently &gt;32 mg/L, and source interpretation R. The inequality is preserved. All listed isolate codes, organisms and asserted metadata were compared. Breakpoint editions vary across pages: most use CLSI 2025 Supplement 35, while specified older/newer pages retain their own edition. Isolate 0033 lacks a versioned breakpoint footnote and the native record does not invent one. Propagation medium is not transferred into the susceptibility assay. The source warns of ordinary dilution-test variability; genotype listings alone do not attribute an isolate phenotype to one resistance mechanism. |
| biosamples | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample; https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy; All 28 native BioSample accessions and six taxon identifiers. | supports | Every asserted BioSample resolves and matches its CDC isolate. Taxa 562, 573, 470, 354276, 287 and 90371 resolve to the retained organisms or taxonomic scope. BioSamples for 1151, 1152 and 1160 identify Enterobacter hormaechei more narrowly than the CDC Enterobacter cloacae complex label; that compatible refinement is not a contradiction. The Salmonella BioSample uses broader species naming than CDC’s Typhimurium label. Isolates 1332–1334 do not acquire invented BioSample accessions. |
| adopted-reviews | PMID:8150771; PMID:11303846; Complete MED abstracts and publication-type metadata in 222-epmc.json. | context_only | The ARO overview, PMID 8150771, and ChEBI lead PMID 11303846 are reviews of cefepime properties. They support historical context but do not constitute new direct PBP or strain-specific primary experiments. |
| adopted-microbiology | PMID:11084674; PMID:11280610; PMID:11179650; Complete indexed primary abstracts. | partial | PMID 11084674 examines 160 imipenem-resistant Pseudomonas aeruginosa isolates by E-test; population MIC summaries are not individual observations. PMID 11280610 compares 995 clinical isolates by gradient diffusion. PMID 11179650 characterizes an altered Enterobacter cloacae AmpC with a six-residue deletion and hyperproduction, including cloning/kinetic context; it does not validate the distinct native Acinetobacter baumannii ampC association. Full methods and tables were not independently inspected for these adopted leads. |
| adopted-clinical | PMID:11191931; PMID:11260566; PMID:11306793; PMID:11431192; PMID:11328792; PMID:11442796; All six complete indexed primary abstracts. | partial | PMID 11191931 concerns encephalopathy in renal impairment, not antimicrobial mechanism. PMID 11260566 studies pediatric febrile episodes; PMID 11306793 concerns adult hematological malignancy and includes modified regimens in final outcomes. PMID 11431192 is an underpowered peritoneal-dialysis peritonitis comparison, not proof of equivalence. PMID 11328792 measures pancreatic exposure; PMID 11442796 measures pharmacokinetics in foals and dogs. Neither PK study supplies a microbial MIC, natural producer or species-specific approval. No clinical outcome is promoted to an exact molecular-target claim. |
| card | https://card.mcmaster.ca/ontology/35976; https://card.mcmaster.ca/ontology/37129; 222-card-*.html; Cefepime ARO:0000059, PBP ARO:3000749, cephalosporin ARO:0000032 and all thirteen native resistance term definitions, parent links and publication lists. | supports | Current CARD reproduces the five ARO aliases, drug class, PBP target and all thirteen resistance associations: ACC-1, K. aerogenes Omp36, E. coli ompF mutant, A. baumannii ampC, K. pneumoniae OmpK35, AxyXY-OprZ, KpnEF, LAP-1, LAP-2, SCO-1, VIM-63, KPC-123 and LAQ-1. Accessions and mapped mechanism categories agree. These are database associations, not evidence that wild-type protein presence alone establishes resistance or that every host crosses a clinical breakpoint. |
| adapter | kg-microbe-sources imodulondb; 222-imodulondb-datasets.txt; 222-imodulondb-ompF.txt; 222-imodulondb-ampC.txt; Structured dataset catalog and gene searches run before web research. | context_only | The e_coli/precise1k query ompF returns gene b0929 and no matching iModulon. The a_baumannii/precise139 query ampC returns ABUW_1194, annotated ADC-7, and no matching iModulon. The catalog supplies no matching Klebsiella or Achromobacter dataset for these assertions. These annotation hits do not identify the experimental mutant, prove a causal drug response, or establish cefepime resistance in a clinical isolate. No iModulon informed a mechanistic verdict. |
| pbp-primary | PMID:1804003; https://doi.org/10.1128/AAC.35.11.2312; https://pmc.ncbi.nlm.nih.gov/articles/PMC245377/; All six original scanned pages 2312–2317, including Methods, Table 1 and Figures 1–4, visually inspected. | supports | Pucci et al. used cefepime BMY-28142 sulfate and membrane preparations from E. coli K-12 and beta-lactamase-deficient P. aeruginosa SC8329. Competition with radiolabeled benzylpenicillin supports PBP interaction. Table 1 reports E. coli PBP3 IC50 0.03 micrograms/mL and P. aeruginosa PBP3 &lt;0.0025; those are competition endpoints, not dissociation constants or whole-cell MICs. The paper separately reports MICs 0.01 and 0.06 micrograms/mL under its broth conditions. Morphology supports cell-wall consequences but the proposed contribution of particular PBPs remains qualified. This is useful active-moiety evidence with an explicit sulfate-reagent boundary. |
| pbp-structure-lead | PMID:29357220; https://doi.org/10.1021/acschembio.7b00817; https://www.rcsb.org/structure/5OJ0; Complete indexed abstract and public PDB deposition summary. | partial | The 2018 study describes noncovalent cefepime binding to Streptococcus pneumoniae PBP2x; PDB 5OJ0 is a 2.66 Å structure. The deposited ligand has a cationic protonation representation distinct from the native zwitterion. Full publisher methods were not inspected. This is a qualified future primary lead, not an inferred covalent binding event or automatic protein-example assignment. |
| lap1-primary | PMID:17116662; https://doi.org/10.1128/AAC.01082-06; https://pmc.ncbi.nlm.nih.gov/articles/PMC1797722/; Accessible original HTML Methods and Results, Tables 1 and 2. | partial | LAP-1 hydrolyzes cefepime in the purified assay: kcat 10 s^-1 and Km 800 micromolar. The cloned E. coli DH10B construct has cefepime MIC 0.12 versus 0.06 micrograms/mL in the control. Thus biochemical inactivation and a small host-specific MIC shift are supported; these results do not establish universal clinical cefepime resistance. The clinical isolate and linked quinolone-resistance determinants cannot supply isolated LAP-1 causation for every phenotype. |
| laq1-primary | PMID:36504772; https://doi.org/10.3389/fmicb.2022.990736; https://pmc.ncbi.nlm.nih.gov/articles/PMC9727190/; Original XML Methods, relevant Results and Tables 3 and 4. | partial | The LAQ-1 clone has cefepime MIC 0.125 micrograms/mL versus &lt;0.03 for the vector control; native Lelliottia isolate P13 is 0.06. Purified LAQ-1 shows cefepime hydrolysis with reported Km 57.05 micromolar and kcat 466.64 s^-1. These data support hydrolysis and an assay-specific MIC increase, while clinical resistance requires its own organism, breakpoint and exposure context. Environmental isolation of an enzyme-bearing organism is not cefepime biosynthesis. |
| kpc123-primary | PMID:35794918; https://doi.org/10.3389/fmicb.2022.930777; https://pmc.ncbi.nlm.nih.gov/articles/PMC9251512/; Original XML susceptibility/conjugation methods, relevant Results and Table 2. | partial | The clinical Citrobacter koseri donor has cefepime MIC 16 mg/L. E. coli transconjugant and cloned KPC-123 backgrounds have 2 mg/L versus controls ≤1. The donor phenotype therefore cannot be wholly transferred to the cloned determinant, and the modest clone MIC shift is distinct from universal clinical resistance. The paper’s main ceftazidime-avibactam findings are not automatically cefepime claims; no cefepime-specific purified kinetic value is asserted here. |
| ompf-primary | PMID:10639355; https://doi.org/10.1128/AAC.44.2.311-315.2000; https://pmc.ncbi.nlm.nih.gov/articles/PMC89676/; Accessible original Methods, Results and Discussion, including MIC and uptake experiments. | supports | E. coli BZB1107 OmpF substitutions G119D/E increase cefepime MIC from 0.06 to 1 microgram/mL, while R132A/D do not. Radiolabeled cefepime uptake in a porin-deficient E. cloacae host expressing constructs supports impaired diffusion. The organism used for uptake differs from the E. coli MIC background. Mutation-dependent reduced permeability supports the native mutant association; the ordinary presence of ompF is not sufficient resistance evidence. |
| other-resistance-abstracts | PMID:10428914; PMID:28584156; PMID:15081418; PMID:23836167; PMID:27645385; PMID:16982792; PMID:17420213; PMID:17353248; PMID:20956594; Complete MED abstracts for the cited original studies. | partial | ACC-1 is characterized in a plasmid/cloning context, but its exact cefepime table was not inspected. AxyXY-OprZ regulation and KpnEF knockout/complementation support expression-dependent efflux. Omp36 mutation and OmpK35 loss/permeability studies require their mutant backgrounds; normal porins promote drug influx. LAP-1/Qnr association does not isolate all phenotypic causes. SCO-1 studies describe a narrow-spectrum enzyme with low cephalosporin activity, while a multienzyme plasmid study cannot allocate cefepime effects to SCO-1 alone. Exact quantitative cefepime support for each of these edges remains only partly adjudicated. |
| resistance-access-limits | PMID:21304033; PMID:18550213; PMID:35758752; https://doi.org/10.1128/jb.00088-22; Publication metadata, review abstract, LAP-2 letter metadata, and selected publicly indexed VIM-63 primary text. | context_only | The A. baumannii AmpC citation is a review and is not typed as a primary experiment. The LAP-2 letter has no indexed abstract and its full text was not inspected. Current CARD’s VIM-63 term lacks a linked publication; a bounded exact-variant search located PMID 35758752. Indexed original text discusses the I226L variant, a VIM-2-like clone phenotype and cefepime kinetic differences, but its complete methods and tables were not independently read. These boundaries prevent promotion of all thirteen source edges to primary support. |
| local-search | 222-local-hits.txt; 222-inclusive-file-hits.txt; Exact name, slug, CHEBI:478164 and full key across maintained and generated surfaces. | context_only | The inclusive search found source/native records, generated maps and source/queue context, including an NCBI AST drug map. That map does not own the curated CDC observations. No exact existing CARD evidence qualification was found. Whole-record inspection confirms optional-field absence. |
| validation | 222-focused-results.json; 222-chemistry.json; 222-external-chemistry.json; 222-cdc-comparison.json; Actual focused gates and independent chemical/source comparisons. | supports | Schema, strict and native chemistry commands exit 0. Native SMILES and InChI reproduce the full key, formula, net charge, both R stereocentres, average mass and monoisotopic mass; both source mints reproduce. Independent official structures agree. CDC comparison was interpreted by reading the actual result rows and footnotes, not by treating every broad text-search match as an assay result. |

## Limits And Additional Notes

- The whole native record and exact maintained source rows were read. All 13 original input hashes remain unchanged; six actual ARO/role/qualification inputs were appended, for 19 total input hashes.
- All eleven adopted citation abstracts were inspected. Their full primary articles were not all read. Clinical outcomes, host toxicity and pharmacokinetics were not transferred into antibacterial target or producer claims.
- All six original pages of PMID 1804003 were visually inspected. LAP-1 and OmpF primary HTML sections were inspected through successful public web retrieval; subsequent retrievals and local copies encountered challenge pages, whose hashes are not represented as primary full-text snapshots. LAQ-1 and KPC-123 inspection covered relevant Methods, Results and tables, not every genomic or discussion statement.
- Primary adjudication remains partial for several CARD edges. The A. baumannii AmpC citation is a review; LAP-2 has no indexed abstract and full text was unavailable in the bounded search. ACC-1, SCO-1, efflux and other porin studies were read at abstract level unless specifically identified otherwise. VIM-63 was followed to original indexed text, but its complete methods and tables were not inspected.
- Each CDC page was inspected for the asserted identity, cefepime result, method/breakpoint footnote and metadata. Unrelated gene inventories and all propagation instructions were not exhaustively audited. Public source interpretations were preserved; proprietary CLSI standards were not independently reconstructed.
- The structured adapter was used before web research. Gene annotation hits and absence of matching modules or datasets are contextual results, not evidence that a native mechanism is absent. No new expression-response or protein-example assertion was made.
- DrugBank public identity was accessible through web retrieval after direct 403. Reaxys and CAS Registry subscription records and full patent claim sets were not inspected. No paid access was used.
- The review supports present native assertions at their stated evidence levels and records optional evidence enrichment. It does not promote SEEDED status or claim that all thirteen resistance associations have been independently proved by exact primary experiments.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T112535Z-cefepime
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cefepime: identity and 31 isolate observations agree; retain context on imported
  protein associations'
started_at: '2026-10-21T11:08:24Z'
finished_at: '2026-10-21T11:25:35Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author the seed or curated isolate observations. Read
    the whole native record and actual source rows/code, preserved initial hashes,
    checked each curated CDC observation and inspected original PBP scans plus selected
    resistance studies.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: The exact cefepime zwitterion is chemically coherent and its official identifiers
  agree. All 31 native isolate observations retain the source result >32 mg/L and
  resistant interpretation; all 28 asserted BioSamples resolve. The 13 CARD resistance
  associations and generic PBP target reproduce the maintained and current source
  and remain explicitly database assertions. Original studies support PBP interaction
  and several context-dependent resistance mechanisms, while hydrolysis, small MIC
  shifts and clinical resistance must remain distinct. No material native error was
  established. Two informational follow-ups concern optional primary PBP evidence
  and source-bound qualification of resistance context. Scientific assessment retains
  the stated evidence limits; full verification is blocked by the shared native-library
  failure.
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
  - path: data/antibiotics/antibacterial/cefepime.yaml
    sha256: 1b7e6c555e89446b8881dd47f4dff3cee02c5f7f5c374b694bf605d816c6c992
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
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: scripts/card_evidence_reviews.py
    sha256: f9ec8aff30066bf04b9c2757af7d6f5d179d045e57b9f3b352bbed0b851f50a8
    role: context
targets:
- target_id: CHEBI:478164
  path: data/antibiotics/antibacterial/cefepime.yaml
  label: cefepime
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
    role: Adopted ARO identity, target or resistance source
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Adopted ARO identity, target or resistance source
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Adopted ARO identity, target or resistance source
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefepime.yaml
    role: Curated CDC isolate activity and BioSample evidence
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Imported PBP target-role mapping
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Source-bound qualification of imported CARD assertions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Application of source-bound CARD qualifications
scope:
  description: 'Whole CHEBI:478164 record: definition, eleven synonyms, chemical and
    drug xrefs, parents and roles, exact chemical descriptors, both source concepts,
    eleven adopted citation leads, 31 activity observations, thirteen resistance entries,
    the PBP target and all 25 history entries.'
  selection: Queue 222. Initial capture retained; actual ARO and CARD qualification
    owners and six additional input hashes appended before scientific judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:478164
  exclusions:
  - target: Cefepime salts, hydrates, formulations and other cephalosporins
    reason: They supply qualified experimental or active-moiety context only; their
      formulation components, protonation states and product regulatory assertions
      are not automatically exact claims about this zwitterion.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Actual focused command exited 0.
  target_ids:
  - CHEBI:478164
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefepime.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Actual focused command exited 0.
  target_ids:
  - CHEBI:478164
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefepime.yaml --out /private/tmp/am-review-session/222-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Actual focused command exited 0. Batch019 RDKit interpreter independently
    parsed the batch023 native SMILES and InChI and reproduced both source mints.
  target_ids:
  - CHEBI:478164
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 222
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
  - CHEBI:478164
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
  - CHEBI:478164
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
  - CHEBI:478164
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
  - CHEBI:478164
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
  - CHEBI:478164
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
  - CHEBI:478164
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
  - CHEBI:478164
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
  - CHEBI:478164
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
  - CHEBI:478164
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/cefepime.yaml
  locator: Entire YAML, all fields and 25 history entries.
  accessed_at: '2026-10-21T11:24:23Z'
  support: supports
  summary: SEEDED/EXACT record denotes cefepime as a net-neutral zwitterion. The thirteen
    resistance entries explicitly identify CARD database assertions. The generic PBP
    target has PRIMARY_EVIDENCE_NEEDED and is not presented as a primary experiment.
    No structured mode_of_action, causal graph, producer or clinical_status is present.
    Optional absence is not a schema defect.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv;
    data/raw/aro_resistance_edges.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py;
    conf/sources.yaml
  locator: ChEBI row 2973, ARO antibiotic row 44, target row 45 and resistance rows
    1398–1410; extraction lines 450–530 and seeding lines 1750–1830.
  accessed_at: '2026-10-21T11:24:23Z'
  support: supports
  summary: The source rows supply the exact identity, source aliases and citation
    leads, generic PBP edge and thirteen resistance associations. Extraction maps
    source ancestors to resistance mechanism categories. Seeding preserves database-only
    notes and PRIMARY_EVIDENCE_NEEDED for the target. Both source concepts and minted
    identifiers reproduce. Curated CDC observations are owned by the native record,
    not inferred from the ARO edges.
  snapshot_sha256: a0acac8a8937edb91c9d876e870a416d636048d76a49b11b59f54dd5d682b2d5
- evidence_id: qualification-owner
  kind: record_content
  reference: conf/aro_target_roles.tsv; curation/card_evidence_reviews.json; scripts/card_evidence_reviews.py
  locator: PBP role mapping, complete qualification registry exact-match search, loader
    and qualification application code.
  accessed_at: '2026-10-21T11:24:23Z'
  support: supports
  summary: The PBP family is mapped as a direct binding protein target. No exact cefepime
    qualification row was found in the maintained registry. Existing machinery binds
    qualifications to the exact source row hash and appends primary-source context
    without silently upgrading a database assertion to a primary evidence type.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:478164
  locator: Current chemical entry, identifiers, aliases, roles, parents and structures.
  accessed_at: '2026-10-21T11:24:23Z'
  support: supports
  summary: Native definition, six ChEBI aliases, CAS 88040-23-7, formula C19H24N6O5S2,
    net charge 0, masses and full key HVFLCNVBZFFHBT-ZKDACBOMSA-N agree. CHEBI:23066
    denotes cephalosporin and CHEBI:36816 oxime O-ether; antimicrobial and antibacterial-drug
    roles are consistent. Native geometry is the 6R,7R cephalosporin with a Z oxime.
  snapshot_sha256: 4b7b4cf677f49eab5804f60e273ca2ec6c4944bba5f75316c66eed0246be99b6
- evidence_id: chemical-xrefs
  kind: database
  reference: https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL186; https://pubchem.ncbi.nlm.nih.gov/compound/5479537;
    https://rest.kegg.jp/get/C08111; https://rest.kegg.jp/get/D02376; https://drugcentral.org/drugcard/535
  locator: Official property records, both KEGG entries and structure MOL, DrugCentral
    InChI; independent structure comparison.
  accessed_at: '2026-10-21T11:24:23Z'
  support: supports
  summary: All independently parsed structures reproduce the native full key, formula,
    charge and two R stereocentres. The native KEGG compound/drug, ChEMBL, PubChem
    and DrugCentral identifiers resolve to cefepime. KEGG PubChem links are substance
    identifiers, not competing compound CIDs. DrugCentral identity data were used;
    its generated assistant prose was not treated as experimental evidence.
  snapshot_sha256: c4efbad38f3d3a6380c4ae37e2e3aa9bfea66a7b46b1d3e433dab3029b3e4736
- evidence_id: drugbank
  kind: database
  reference: https://go.drugbank.com/drugs/DB01413
  locator: Public DrugBank identity overview inspected through web retrieval after
    direct HTTP 403.
  accessed_at: '2026-10-21T11:24:23Z'
  support: supports
  summary: DB01413 is cefepime and its public identity summary gives the native full
    InChIKey and matching structure identifiers. Restricted target or assay sections
    were not inspected and are not used as primary evidence.
- evidence_id: patents
  kind: primary_source
  reference: https://patents.google.com/patent/US4406899A/en; https://patents.google.com/patent/DE3307550A1/en
  locator: Patent metadata and selected description identifying compound Ia.
  accessed_at: '2026-10-21T11:24:23Z'
  support: partial
  summary: Both native document identifiers resolve to the corresponding cephalosporin
    disclosure. Compound Ia has cefepime’s Z methoxyimino aminothiazolyl side chain
    and methylpyrrolidinium substituent. This supports exact synthetic-document relevance;
    the full claims, every example and all biological tables were not independently
    audited.
  snapshot_sha256: 185834acc7de06c1cdfdc0592f4667b1b09ace45853937cf4e1218ecb76b5f47
- evidence_id: other-xrefs
  kind: database
  reference: https://en.wikipedia.org/wiki/Cefepime; https://www.ebi.ac.uk/chebi/CHEBI:478164
  locator: Native informational link and official xref list.
  accessed_at: '2026-10-21T11:24:23Z'
  support: context_only
  summary: The encyclopedia link resolves to the same named drug and is used only
    as link context. Reaxys 7453587 and CAS 88040-23-7 are officially attested in
    ChEBI; subscription registry contents were not inspected. Broad brand aliases
    supplied by ARO are source labels, not assertions that every marketed formulation
    has this exact composition.
- evidence_id: cdc
  kind: authority
  reference: https://wwwn.cdc.gov/ARIsolateBank/; 222-cdc-comparison.json; 222-cdc-*.html
  locator: 'Each of the 31 exact native isolate pages: identity, cefepime result row,
    method/breakpoint footnote and asserted isolate attributes.'
  accessed_at: '2026-10-21T11:24:23Z'
  support: supports
  summary: 'Every native cefepime observation agrees with its cited CDC page: MIC
    >32 micrograms/mL, equivalently >32 mg/L, and source interpretation R. The inequality
    is preserved. All listed isolate codes, organisms and asserted metadata were compared.
    Breakpoint editions vary across pages: most use CLSI 2025 Supplement 35, while
    specified older/newer pages retain their own edition. Isolate 0033 lacks a versioned
    breakpoint footnote and the native record does not invent one. Propagation medium
    is not transferred into the susceptibility assay. The source warns of ordinary
    dilution-test variability; genotype listings alone do not attribute an isolate
    phenotype to one resistance mechanism.'
  snapshot_sha256: 8656d026c5609d8d1cc33b8b5e10fafbecf0475f814c5197a8edf9255b18bb63
- evidence_id: biosamples
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample;
    https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy
  locator: All 28 native BioSample accessions and six taxon identifiers.
  accessed_at: '2026-10-21T11:24:23Z'
  support: supports
  summary: Every asserted BioSample resolves and matches its CDC isolate. Taxa 562,
    573, 470, 354276, 287 and 90371 resolve to the retained organisms or taxonomic
    scope. BioSamples for 1151, 1152 and 1160 identify Enterobacter hormaechei more
    narrowly than the CDC Enterobacter cloacae complex label; that compatible refinement
    is not a contradiction. The Salmonella BioSample uses broader species naming than
    CDC’s Typhimurium label. Isolates 1332–1334 do not acquire invented BioSample
    accessions.
  snapshot_sha256: 8db530221127f6d05e534dfe04d99c1036eb574000056f03c5950c88280c02fe
- evidence_id: adopted-reviews
  kind: database
  reference: PMID:8150771; PMID:11303846
  locator: Complete MED abstracts and publication-type metadata in 222-epmc.json.
  accessed_at: '2026-10-21T11:24:23Z'
  support: context_only
  summary: The ARO overview, PMID 8150771, and ChEBI lead PMID 11303846 are reviews
    of cefepime properties. They support historical context but do not constitute
    new direct PBP or strain-specific primary experiments.
  snapshot_sha256: 7a761b1ee2f0420ae0fc871553409fd549f64737916be53dfe0a1c621fc64652
- evidence_id: adopted-microbiology
  kind: primary_source
  reference: PMID:11084674; PMID:11280610; PMID:11179650
  locator: Complete indexed primary abstracts.
  accessed_at: '2026-10-21T11:24:23Z'
  support: partial
  summary: PMID 11084674 examines 160 imipenem-resistant Pseudomonas aeruginosa isolates
    by E-test; population MIC summaries are not individual observations. PMID 11280610
    compares 995 clinical isolates by gradient diffusion. PMID 11179650 characterizes
    an altered Enterobacter cloacae AmpC with a six-residue deletion and hyperproduction,
    including cloning/kinetic context; it does not validate the distinct native Acinetobacter
    baumannii ampC association. Full methods and tables were not independently inspected
    for these adopted leads.
  snapshot_sha256: 7a761b1ee2f0420ae0fc871553409fd549f64737916be53dfe0a1c621fc64652
- evidence_id: adopted-clinical
  kind: primary_source
  reference: PMID:11191931; PMID:11260566; PMID:11306793; PMID:11431192; PMID:11328792;
    PMID:11442796
  locator: All six complete indexed primary abstracts.
  accessed_at: '2026-10-21T11:24:23Z'
  support: partial
  summary: PMID 11191931 concerns encephalopathy in renal impairment, not antimicrobial
    mechanism. PMID 11260566 studies pediatric febrile episodes; PMID 11306793 concerns
    adult hematological malignancy and includes modified regimens in final outcomes.
    PMID 11431192 is an underpowered peritoneal-dialysis peritonitis comparison, not
    proof of equivalence. PMID 11328792 measures pancreatic exposure; PMID 11442796
    measures pharmacokinetics in foals and dogs. Neither PK study supplies a microbial
    MIC, natural producer or species-specific approval. No clinical outcome is promoted
    to an exact molecular-target claim.
  snapshot_sha256: 7a761b1ee2f0420ae0fc871553409fd549f64737916be53dfe0a1c621fc64652
- evidence_id: card
  kind: database
  reference: https://card.mcmaster.ca/ontology/35976; https://card.mcmaster.ca/ontology/37129;
    222-card-*.html
  locator: Cefepime ARO:0000059, PBP ARO:3000749, cephalosporin ARO:0000032 and all
    thirteen native resistance term definitions, parent links and publication lists.
  accessed_at: '2026-10-21T11:24:23Z'
  support: supports
  summary: 'Current CARD reproduces the five ARO aliases, drug class, PBP target and
    all thirteen resistance associations: ACC-1, K. aerogenes Omp36, E. coli ompF
    mutant, A. baumannii ampC, K. pneumoniae OmpK35, AxyXY-OprZ, KpnEF, LAP-1, LAP-2,
    SCO-1, VIM-63, KPC-123 and LAQ-1. Accessions and mapped mechanism categories agree.
    These are database associations, not evidence that wild-type protein presence
    alone establishes resistance or that every host crosses a clinical breakpoint.'
  snapshot_sha256: 75751f62ba64f4bbe5add37b207393468b194094e90b3df78ac230c8138f804a
- evidence_id: adapter
  kind: database
  reference: kg-microbe-sources imodulondb; 222-imodulondb-datasets.txt; 222-imodulondb-ompF.txt;
    222-imodulondb-ampC.txt
  locator: Structured dataset catalog and gene searches run before web research.
  accessed_at: '2026-10-21T11:24:23Z'
  support: context_only
  summary: The e_coli/precise1k query ompF returns gene b0929 and no matching iModulon.
    The a_baumannii/precise139 query ampC returns ABUW_1194, annotated ADC-7, and
    no matching iModulon. The catalog supplies no matching Klebsiella or Achromobacter
    dataset for these assertions. These annotation hits do not identify the experimental
    mutant, prove a causal drug response, or establish cefepime resistance in a clinical
    isolate. No iModulon informed a mechanistic verdict.
  snapshot_sha256: 3120df94c27d2f88360984e42ed0f7a1393b38a480f95cf991c2d5a29b000785
- evidence_id: pbp-primary
  kind: primary_source
  reference: PMID:1804003; https://doi.org/10.1128/AAC.35.11.2312; https://pmc.ncbi.nlm.nih.gov/articles/PMC245377/
  locator: All six original scanned pages 2312–2317, including Methods, Table 1 and
    Figures 1–4, visually inspected.
  accessed_at: '2026-10-21T11:24:23Z'
  support: supports
  summary: Pucci et al. used cefepime BMY-28142 sulfate and membrane preparations
    from E. coli K-12 and beta-lactamase-deficient P. aeruginosa SC8329. Competition
    with radiolabeled benzylpenicillin supports PBP interaction. Table 1 reports E.
    coli PBP3 IC50 0.03 micrograms/mL and P. aeruginosa PBP3 <0.0025; those are competition
    endpoints, not dissociation constants or whole-cell MICs. The paper separately
    reports MICs 0.01 and 0.06 micrograms/mL under its broth conditions. Morphology
    supports cell-wall consequences but the proposed contribution of particular PBPs
    remains qualified. This is useful active-moiety evidence with an explicit sulfate-reagent
    boundary.
  snapshot_sha256: af1f8c840b99a638652a3dcc8abfe5d128e2016cc0c29fcf940f03530e72a156
- evidence_id: pbp-structure-lead
  kind: primary_source
  reference: PMID:29357220; https://doi.org/10.1021/acschembio.7b00817; https://www.rcsb.org/structure/5OJ0
  locator: Complete indexed abstract and public PDB deposition summary.
  accessed_at: '2026-10-21T11:24:23Z'
  support: partial
  summary: The 2018 study describes noncovalent cefepime binding to Streptococcus
    pneumoniae PBP2x; PDB 5OJ0 is a 2.66 Å structure. The deposited ligand has a cationic
    protonation representation distinct from the native zwitterion. Full publisher
    methods were not inspected. This is a qualified future primary lead, not an inferred
    covalent binding event or automatic protein-example assignment.
  snapshot_sha256: fa1ef02b4894f343175761552176f6b1a510570637007d6cf145979a37e9af3f
- evidence_id: lap1-primary
  kind: primary_source
  reference: PMID:17116662; https://doi.org/10.1128/AAC.01082-06; https://pmc.ncbi.nlm.nih.gov/articles/PMC1797722/
  locator: Accessible original HTML Methods and Results, Tables 1 and 2.
  accessed_at: '2026-10-21T11:24:23Z'
  support: partial
  summary: 'LAP-1 hydrolyzes cefepime in the purified assay: kcat 10 s^-1 and Km 800
    micromolar. The cloned E. coli DH10B construct has cefepime MIC 0.12 versus 0.06
    micrograms/mL in the control. Thus biochemical inactivation and a small host-specific
    MIC shift are supported; these results do not establish universal clinical cefepime
    resistance. The clinical isolate and linked quinolone-resistance determinants
    cannot supply isolated LAP-1 causation for every phenotype.'
- evidence_id: laq1-primary
  kind: primary_source
  reference: PMID:36504772; https://doi.org/10.3389/fmicb.2022.990736; https://pmc.ncbi.nlm.nih.gov/articles/PMC9727190/
  locator: Original XML Methods, relevant Results and Tables 3 and 4.
  accessed_at: '2026-10-21T11:24:23Z'
  support: partial
  summary: The LAQ-1 clone has cefepime MIC 0.125 micrograms/mL versus <0.03 for the
    vector control; native Lelliottia isolate P13 is 0.06. Purified LAQ-1 shows cefepime
    hydrolysis with reported Km 57.05 micromolar and kcat 466.64 s^-1. These data
    support hydrolysis and an assay-specific MIC increase, while clinical resistance
    requires its own organism, breakpoint and exposure context. Environmental isolation
    of an enzyme-bearing organism is not cefepime biosynthesis.
  snapshot_sha256: 50ce65bce662993c908c2bc201beefcc6583b435d3784a20a3c2ee39990ee2df
- evidence_id: kpc123-primary
  kind: primary_source
  reference: PMID:35794918; https://doi.org/10.3389/fmicb.2022.930777; https://pmc.ncbi.nlm.nih.gov/articles/PMC9251512/
  locator: Original XML susceptibility/conjugation methods, relevant Results and Table
    2.
  accessed_at: '2026-10-21T11:24:23Z'
  support: partial
  summary: The clinical Citrobacter koseri donor has cefepime MIC 16 mg/L. E. coli
    transconjugant and cloned KPC-123 backgrounds have 2 mg/L versus controls ≤1.
    The donor phenotype therefore cannot be wholly transferred to the cloned determinant,
    and the modest clone MIC shift is distinct from universal clinical resistance.
    The paper’s main ceftazidime-avibactam findings are not automatically cefepime
    claims; no cefepime-specific purified kinetic value is asserted here.
  snapshot_sha256: 9e8e88b5f20902bc7c8ad0ea6326edb0f9776b316cd2ff7fba6ec7026e14454c
- evidence_id: ompf-primary
  kind: primary_source
  reference: PMID:10639355; https://doi.org/10.1128/AAC.44.2.311-315.2000; https://pmc.ncbi.nlm.nih.gov/articles/PMC89676/
  locator: Accessible original Methods, Results and Discussion, including MIC and
    uptake experiments.
  accessed_at: '2026-10-21T11:24:23Z'
  support: supports
  summary: E. coli BZB1107 OmpF substitutions G119D/E increase cefepime MIC from 0.06
    to 1 microgram/mL, while R132A/D do not. Radiolabeled cefepime uptake in a porin-deficient
    E. cloacae host expressing constructs supports impaired diffusion. The organism
    used for uptake differs from the E. coli MIC background. Mutation-dependent reduced
    permeability supports the native mutant association; the ordinary presence of
    ompF is not sufficient resistance evidence.
- evidence_id: other-resistance-abstracts
  kind: primary_source
  reference: PMID:10428914; PMID:28584156; PMID:15081418; PMID:23836167; PMID:27645385;
    PMID:16982792; PMID:17420213; PMID:17353248; PMID:20956594
  locator: Complete MED abstracts for the cited original studies.
  accessed_at: '2026-10-21T11:24:23Z'
  support: partial
  summary: ACC-1 is characterized in a plasmid/cloning context, but its exact cefepime
    table was not inspected. AxyXY-OprZ regulation and KpnEF knockout/complementation
    support expression-dependent efflux. Omp36 mutation and OmpK35 loss/permeability
    studies require their mutant backgrounds; normal porins promote drug influx. LAP-1/Qnr
    association does not isolate all phenotypic causes. SCO-1 studies describe a narrow-spectrum
    enzyme with low cephalosporin activity, while a multienzyme plasmid study cannot
    allocate cefepime effects to SCO-1 alone. Exact quantitative cefepime support
    for each of these edges remains only partly adjudicated.
  snapshot_sha256: c19c051077ee44664aa1cf0c9eb67daeade12062a2ffacf331c27f431e0395a7
- evidence_id: resistance-access-limits
  kind: database
  reference: PMID:21304033; PMID:18550213; PMID:35758752; https://doi.org/10.1128/jb.00088-22
  locator: Publication metadata, review abstract, LAP-2 letter metadata, and selected
    publicly indexed VIM-63 primary text.
  accessed_at: '2026-10-21T11:24:23Z'
  support: context_only
  summary: The A. baumannii AmpC citation is a review and is not typed as a primary
    experiment. The LAP-2 letter has no indexed abstract and its full text was not
    inspected. Current CARD’s VIM-63 term lacks a linked publication; a bounded exact-variant
    search located PMID 35758752. Indexed original text discusses the I226L variant,
    a VIM-2-like clone phenotype and cefepime kinetic differences, but its complete
    methods and tables were not independently read. These boundaries prevent promotion
    of all thirteen source edges to primary support.
- evidence_id: local-search
  kind: search
  reference: 222-local-hits.txt; 222-inclusive-file-hits.txt
  locator: Exact name, slug, CHEBI:478164 and full key across maintained and generated
    surfaces.
  accessed_at: '2026-10-21T11:24:23Z'
  support: context_only
  summary: The inclusive search found source/native records, generated maps and source/queue
    context, including an NCBI AST drug map. That map does not own the curated CDC
    observations. No exact existing CARD evidence qualification was found. Whole-record
    inspection confirms optional-field absence.
  snapshot_sha256: d5accd407723f167f9d46c88ced0af96ca86843ab05697cdf4b89fd075841bc6
  search_scope: rg --no-ignore --hidden across data, curation, conf, scripts, src,
    docs, .claude, reviews and reports; ignored and hidden files included, excluding
    .git and .venv internals.
- evidence_id: validation
  kind: validation
  reference: 222-focused-results.json; 222-chemistry.json; 222-external-chemistry.json;
    222-cdc-comparison.json
  locator: Actual focused gates and independent chemical/source comparisons.
  accessed_at: '2026-10-21T11:24:23Z'
  support: supports
  summary: Schema, strict and native chemistry commands exit 0. Native SMILES and
    InChI reproduce the full key, formula, net charge, both R stereocentres, average
    mass and monoisotopic mass; both source mints reproduce. Independent official
    structures agree. CDC comparison was interpreted by reading the actual result
    rows and footnotes, not by treating every broad text-search match as an assay
    result.
  snapshot_sha256: 960a4520b9caf54429babff66f1b33ba7686538a76c117f9bc9ab0380b41d9d4
assessments:
- assessment_id: identity
  area: identity
  topic: Exact zwitterion and identifiers
  outcome: supported
  summary: The native chemical graph, formula, stereo and identifiers are coherent.
    Salt and protonation representations in experimental or deposition contexts are
    explicitly distinguished.
  target_ids:
  - CHEBI:478164
  evidence_ids:
  - chebi
  - chemical-xrefs
  - drugbank
  - patents
  - validation
- assessment_id: activity
  area: quantity
  topic: All 31 curated isolate observations
  outcome: supported
  summary: Every native >32 mg/L result and R interpretation agrees with its cited
    CDC record. Accessions and organism scope agree, including compatible narrower
    BioSample species labels. Source breakpoint editions are retained rather than
    retrospectively recalculated.
  target_ids:
  - CHEBI:478164
  evidence_ids:
  - cdc
  - biosamples
  - record
- assessment_id: target
  area: evidence
  topic: Generic PBP target and optional primary evidence
  outcome: supported
  summary: The present target is an honestly labeled database assertion. Original
    membrane competition supports PBP interaction in defined strains and a sulfate
    preparation; curated primary claims would require their own experimental scope
    and endpoint.
  target_ids:
  - CHEBI:478164
  evidence_ids:
  - card
  - pbp-primary
  - pbp-structure-lead
  - adapter
- assessment_id: resistance
  area: scope
  topic: Thirteen imported resistance associations
  outcome: supported
  summary: Every association reproduces current CARD and is explicitly database sourced.
    Inspected primary examples support context-dependent effects; biochemical hydrolysis,
    modest MIC increases and clinical resistance are not interchangeable. Exact quantitative
    support was not fully adjudicated for every edge.
  target_ids:
  - CHEBI:478164
  evidence_ids:
  - card
  - lap1-primary
  - laq1-primary
  - kpc123-primary
  - ompf-primary
  - other-resistance-abstracts
  - resistance-access-limits
- assessment_id: citations
  area: evidence
  topic: All eleven adopted citation leads
  outcome: supported
  summary: All adopted abstracts were read and separated into review, microbiology,
    clinical, toxicity and pharmacokinetic contexts. None supplies an unqualified
    producer, exact target or clinical approval assertion.
  target_ids:
  - CHEBI:478164
  evidence_ids:
  - adopted-reviews
  - adopted-microbiology
  - adopted-clinical
- assessment_id: completeness
  area: completeness
  topic: Optional mechanisms and primary qualifications
  outcome: unknown
  summary: Specific primary target and resistance context can be added through the
    maintained curation surfaces. Absence of a graph, producer or clinical status
    is not an error and does not establish that such information is unavailable elsewhere.
  target_ids:
  - CHEBI:478164
  evidence_ids:
  - record
  - pbp-primary
  - qualification-owner
  - local-search
- assessment_id: provenance
  area: ownership
  topic: Source and curation ownership
  outcome: supported
  summary: Initial input hashes remain unchanged. Actual ARO and role/qualification
    owners were captured before judgment. Native CDC additions and imported CARD associations
    have distinct maintained owners.
  target_ids:
  - CHEBI:478164
  evidence_ids:
  - source
  - qualification-owner
  - local-search
- assessment_id: gates
  area: schema
  topic: Focused validation
  outcome: supported
  summary: Documented schema and strict validation and independent chemistry pass;
    scientific status remains SEEDED.
  target_ids:
  - CHEBI:478164
  evidence_ids:
  - validation
  - record
findings:
- finding_id: F1
  issue_key: cefepime-primary-pbp-context-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Primary PBP evidence is available for a qualified future target update
  description: The current generic PBP target correctly remains a database assertion
    with PRIMARY_EVIDENCE_NEEDED. The inspected 1991 experiment supplies membrane
    competition and morphology data for defined strains using cefepime sulfate. A
    future primary update should preserve this reagent and assay scope rather than
    treating competition IC50 as a binding constant or claiming an intact salt is
    the bound species.
  target_ids:
  - CHEBI:478164
  field_paths:
  - molecular_targets
  - mode_of_action
  - evidence
  evidence_ids:
  - record
  - card
  - pbp-primary
  - pbp-structure-lead
  rule_id: 'native-review-checklist: attach primary support to the narrow experimental
    claim'
  native_severity: informational
  normalization_reason: This is optional enrichment of an explicitly qualified seed,
    not a false existing primary-evidence assertion.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefepime.yaml
    role: Future claim-level primary target or activity curation
- finding_id: F2
  issue_key: cefepime-resistance-context-qualification
  category: evidence
  severity: informational
  status: open
  certainty: confirmed
  title: Retain host, mutation and endpoint context when qualifying CARD resistance
    associations
  description: The thirteen imported associations are reproducible and explicitly
    database sourced. Inspected primary studies show why a later qualification should
    distinguish hydrolysis, small MIC changes, loss or mutation of porins, expression-dependent
    efflux and clinical resistant phenotypes. In particular, LAP-1 and LAQ-1 hydrolysis
    and the KPC-123 clone results do not establish resistant cefepime phenotypes in
    every host. No edge deletion is justified solely by these bounded comparisons.
  target_ids:
  - CHEBI:478164
  field_paths:
  - resistance_mechanisms
  evidence_ids:
  - card
  - lap1-primary
  - laq1-primary
  - kpc123-primary
  - ompf-primary
  - other-resistance-abstracts
  - resistance-access-limits
  - qualification-owner
  rule_id: 'native-review-checklist: keep resistance mechanism, genotype association
    and phenotype distinct'
  native_severity: informational
  normalization_reason: Existing notes already identify database assertions. The finding
    records an evidence-strength follow-up rather than asserting that source associations
    are scientifically false.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Source-bound primary qualification of imported CARD associations
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Adopted exact CARD association source rows
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Reproducible qualification application
actions:
- action_id: A1
  description: If adding primary PBP evidence, curate the exact reagent, organism
    and experimental endpoint.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:478164
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefepime.yaml
    role: Future claim-level primary target or activity curation
  acceptance_checks:
  - Use PMID 1804003 with its cefepime sulfate material, E. coli K-12 and P. aeruginosa
    SC8329 backgrounds. Keep membrane competition IC50, whole-cell MIC and morphology
    observations separate.
  - Do not turn the generic PBP family into an unsupported exact protein accession.
    Inspect a primary sequence or structure mapping before adding any protein example.
    For PMID 29357220/PDB 5OJ0, verify the full methods, noncovalent binding interpretation
    and protonation context before curation.
  - Attach evidence to the narrow native claim and preserve any salt-to-active-moiety
    qualification. Use write_validated_antibiotic and record_curation_event under
    a separately authorized curation task, then run focused and applicable shared
    gates.
- action_id: A2
  description: If strengthening resistance evidence, add source-bound qualifications
    for the exact CARD rows after completing primary checks.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:478164
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Source-bound primary qualification of imported CARD associations
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Adopted exact CARD association source rows
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Reproducible qualification application
  acceptance_checks:
  - Bind any qualification to the exact source row and retain the CARD database evidence
    type. Distinguish observed hydrolysis from resistant whole-cell phenotypes and
    record host, construct, comparator, MIC inequality and source breakpoint context
    where applicable.
  - For porins, preserve the loss, mutation or expression background rather than implying
    that normal OmpF/OmpK35/Omp36 presence causes resistance. For efflux, preserve
    the knockout, complementation or regulatory experiment and avoid assigning a regulatory
    protein as a drug target.
  - Complete accessible exact cefepime primary checks for ACC-1, SCO-1, LAP-2 and
    VIM-63 before claiming universal primary support or proposing removal. Do not
    infer absence of activity from inaccessible full text, low activity in one assay
    or absence of a citation on the current CARD page.
  - Keep the independently curated CDC isolate phenotypes separate from mechanism
    attribution. A listed genotype alone does not explain every isolate MIC or establish
    causation. Regenerate qualified imports and run applicable gates if future source
    curation is authorized.
limitations:
- The whole native record and exact maintained source rows were read. All 13 original
  input hashes remain unchanged; six actual ARO/role/qualification inputs were appended,
  for 19 total input hashes.
- All eleven adopted citation abstracts were inspected. Their full primary articles
  were not all read. Clinical outcomes, host toxicity and pharmacokinetics were not
  transferred into antibacterial target or producer claims.
- All six original pages of PMID 1804003 were visually inspected. LAP-1 and OmpF primary
  HTML sections were inspected through successful public web retrieval; subsequent
  retrievals and local copies encountered challenge pages, whose hashes are not represented
  as primary full-text snapshots. LAQ-1 and KPC-123 inspection covered relevant Methods,
  Results and tables, not every genomic or discussion statement.
- Primary adjudication remains partial for several CARD edges. The A. baumannii AmpC
  citation is a review; LAP-2 has no indexed abstract and full text was unavailable
  in the bounded search. ACC-1, SCO-1, efflux and other porin studies were read at
  abstract level unless specifically identified otherwise. VIM-63 was followed to
  original indexed text, but its complete methods and tables were not inspected.
- Each CDC page was inspected for the asserted identity, cefepime result, method/breakpoint
  footnote and metadata. Unrelated gene inventories and all propagation instructions
  were not exhaustively audited. Public source interpretations were preserved; proprietary
  CLSI standards were not independently reconstructed.
- The structured adapter was used before web research. Gene annotation hits and absence
  of matching modules or datasets are contextual results, not evidence that a native
  mechanism is absent. No new expression-response or protein-example assertion was
  made.
- DrugBank public identity was accessible through web retrieval after direct 403.
  Reaxys and CAS Registry subscription records and full patent claim sets were not
  inspected. No paid access was used.
- The review supports present native assertions at their stated evidence levels and
  records optional evidence enrichment. It does not promote SEEDED status or claim
  that all thirteen resistance associations have been independently proved by exact
  primary experiments.
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
