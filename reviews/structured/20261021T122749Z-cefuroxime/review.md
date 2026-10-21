# Cefuroxime: coherent neutral identity with one confirmed brand-synonym typing defect

- Review: 20261021T122749Z-cefuroxime
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:02:25Z
- Finished UTC: 2026-10-21T12:27:49Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native neutral cefuroxime structure, structural definition, broader classes, source concepts and resolved chemical graphs agree. The PBP and ten resistance entries accurately retain database provenance. Original studies support antibacterial activity, PBP competition and several enzyme-specific resistance mechanisms, with sodium-material and strain/assay boundaries. FDA product rows match their current official source; application-level sodium labels alone do not prove that the two neutral-named product rows were misassigned. One minor correction is confirmed: ARO-derived Zinacef is typed EXACT_SYNONYM even though the official regulator identifies it as a sodium-containing medicinal product; retain it with appropriate brand scope. This is separate from the unresolved FDA product 003/004 material question. Full primary coverage, several registry access checks and exact product/form qualification remain limited.

## Scope And Provenance

Entire YAML, including all fifteen synonyms, definition, structural and activity classifications, chemical and drug cross-references, four patent links, structure descriptors, two source concepts, ten resistance entries, PBP target, two FDA assertions and seven history events. All eleven adopted antibiotic bibliography records and all fourteen distinct resistance-linked publication records were inspected at the access depths stated below.

Selection: Queue 265. Original thirteen captured inputs preserved; six actual source/transform inputs appended before substantive judgment, for nineteen total.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:3515 | data/antibiotics/antibacterial/cefuroxime.yaml | generated | cefuroxime |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:3515 | Documented per-record schema validation: no issues found. |
| strict | passed | True | CHEBI:3515 | Documented strict validator: one file scanned, zero errors. |
| chemistry | passed | False | CHEBI:3515 | Supplementary RDKit consistency check from batch027 cwd using batch019 interpreter: both structure encodings and both source mints agree. |
| Authoritative full QC | failed | True | CHEBI:3515 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:3515 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:3515 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:3515 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:3515 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:3515 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:3515 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:3515 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:3515 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Neutral structure, names and equivalent chemical identifiers

identity: supported. Targets: CHEBI:3515.

The neutral 6R,7R/Z cefuroxime graph is coherent across inspected official structures. The definition names its exact structural substituents and the broader classes are appropriate. Drug/document links retain their own scopes, including prodrug patents and form-qualified brand context. Restricted registry access is an explicit limit, not a confirmed broken identifier. The separate Zinacef exact-synonym typing defect requires correction; the chemical graph itself remains supported.

### Antibacterial filing and assay material

scope: supported. Targets: CHEBI:3515.

Original papers support the cefuroxime active moiety as antibacterial, with sodium salt explicitly used in the 1976 experiments. No native numeric endpoint is falsely asserted for isolated neutral acid. Generic antimicrobial role alongside antibacterial filing is valid; source snapshot role differences are not corrective findings.

### Generic PBP database relation and original competition data

evidence: supported. Targets: CHEBI:3515.

The generic target honestly remains PRIMARY_EVIDENCE_NEEDED. The original 1986 membrane competition study supplies useful organism- and PBP-specific evidence, but no neutral-form dissociation constant or universal whole-cell causal chain. Host complement/macrophage and endothelial effects are not bacterial targets.

### Ten database assertions versus experimental strength

evidence: supported. Targets: CHEBI:3515.

All imported relations agree with CARD. Primary support varies from direct cefuroxime hydrolysis and cloned-gene effects to limited abstract evidence. SCO-1 in particular must not inherit the clinical multi-enzyme isolate phenotype; CAE-1 has no successful purified-enzyme assay. These limits justify preserving database provenance, not equating the entries to strong clinical resistance or removing an accurately attributed relation solely for lacking stronger optional evidence.

### FDA product semantics and exact salt boundary

evidence: unknown. Targets: CHEBI:3515.

The native approval date, product numbers, ingredient name and Prescription category match current FDA. The exact neutral GSRS join is reproducible. Sodium labels attached to the broader application do not identify the specific 003/004 solution material conclusively; no confirmed chemical misassignment is reported. Clinical status remains a source-qualified product assertion rather than evidence that free neutral acid is the formulation.

### All adopted bibliography leads and optional enrichments

completeness: unknown. Targets: CHEBI:3515.

All eleven adopted leads and fourteen resistance-linked publication records have explicit dispositions. Host adverse effects, analytical detection, observational prescribing and reviews do not add antimicrobial mechanism evidence. Missing quantitative activity, causal graph, producer and dataset objects are optional gaps, not standalone findings. Source organism names do not establish production, and RT-qPCR is not a dataset assertion.

### Actual source owners and immutable inputs

ownership: supported. Targets: CHEBI:3515.

The review distinguishes ChEBI identity, ARO database relations, FDA product extraction and curator-owned future literature claims. All nineteen input hashes remain unchanged; both original source mints reproduce. No native scientific-status promotion is implied by passing focused checks.

### Brand alias incorrectly typed as exact chemical synonym

identity: concern. Targets: CHEBI:3515.

Zinacef at synonyms[14] is explicitly EXACT_SYNONYM from ARO, while the official label identifies a sodium-containing product. Preserve the useful name as BRAND_NAME or otherwise scoped product terminology. The valid neutral structure and all verified chemical xrefs remain intact. Biofuroksym and Cefuril are bounded follow-up checks, not confirmed wrong-form findings in this review.

## Findings

### F1: Type Zinacef as a brand rather than an exact chemical synonym

minor / open / confirmed; issue key: cefuroxime-zinacef-brand-typed-as-exact-synonym.

Native synonyms[14] asserts the ARO-derived name Zinacef as EXACT_SYNONYM. HPRA explicitly identifies Zinacef as a medicinal product containing cefuroxime sodium. Its shared active moiety makes the name useful, but does not make the product name exact neutral-structure terminology. The source constructor blindly assigns EXACT_SYNONYM to ARO aliases. Preserve Zinacef with brand/product scope through the maintained normalization path; do not replace or merge the valid neutral structure with sodium. Biofuroksym and Cefuril remain product-specific follow-up candidates and are not included in the confirmed field set.

## Recommended Actions And Acceptance Checks

### A3

Correct the maintained Zinacef alias classification and separately verify other ARO product-name candidates.

- Emit Zinacef as BRAND_NAME or another explicitly product-scoped synonym, retaining its ARO provenance and the original lexical name.
- Do not apply a blanket conversion to all ARO aliases: retain actual exact chemical/INN names and abbreviations according to verified semantics. Check Biofuroksym and Cefuril against jurisdiction- and product-specific official sources before assigning their form scope.
- Preserve the neutral native graph, chemical xrefs and separate FDA product 003/004 uncertainty; the Irish brand label does not resolve those US product materials.
- Regenerate through the maintained source/seeder path and rerun focused schema/strict and applicable corpus checks, verifying that the next seed no longer restores EXACT_SYNONYM for Zinacef.

### A1

If primary target or resistance enrichment is undertaken, preserve exact material, organism and experimental endpoints beside the existing database assertions.

- Qualify the 1976 experimental material as cefuroxime sodium and do not silently import its numerical values as isolated neutral-acid measurements.
- Represent PBP competition as the measured membrane assay, not Kd; distinguish individual PBP and bacterial systems from host complement or macrophage effects.
- Keep resistance MIC shifts separate from purified-enzyme hydrolysis. Preserve inequalities, units, construct/vector controls, inducer/selection and source strain ambiguity. Do not infer SCO-1 alone explains the multi-enzyme clinical phenotype or that CAE-1 purification succeeded.
- Obtain the uninspected exact LAP-2 and other limited-access functional passages before promoting those entries to primary evidence. Optional enrichment alone is not a correction requirement.

### A2

If the FDA integration is refined, resolve the exact material of ANDA 065048 products 003/004 before changing their chemical placement.

- Find a product-number-specific label or official composition mapping for 003/004; distinguish neutral active moiety from sodium ingredient and do not infer product identity from an application-wide aggregate alone.
- Retain the verified original approval date and source Prescription status, with currently_marketed understood as the source category rather than a stock-availability claim.
- Only change the maintained join if direct product-specific evidence establishes a mismatch, then regenerate and rerun focused and applicable corpus gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/cefuroxime.yaml; Entire native record and all seven history events. | supports | SEEDED, EXACT and ANTIBACTERIAL. Native neutral cefuroxime has formula C16H16N4O8S, charge zero, two R stereocentres and key JFPVXVDWJQMJEE-IZRZKJBUSA-N. The target explicitly remains PRIMARY_EVIDENCE_NEEDED, and all resistance notes identify imported database assertions. There are no quantitative activity, causal-graph, producer or transcriptomics objects; their absence is not by itself a required-field defect. |
| source | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv; data/raw/aro_resistance_edges.tsv; data/raw/fda_clinical_status.tsv; conf/aro_target_roles.tsv; scripts/extract_source_inventory.py; scripts/extract_fda_clinical_status.py; scripts/seed_from_sources.py; Exact ChEBI row 95, ARO row 48, target row 49, resistance rows 1692–1701 and FDA rows 1410–1411; source configuration and relevant extraction/seeding logic. | supports | ChEBI supplies structural definition, identity, roles and ten publication leads. ARO supplies its aliases, class, source concept and one additional publication lead. Target/resistance transforms preserve database provenance. FDA extraction maps each eligible literal ingredient to its unique UNII, joins the GSRS full key, takes the earliest original AP approval and interprets Prescription as currently marketed. The captured rows are reproducible; their interpretation should remain product-qualified. The ARO concept constructor in scripts/seed_from_sources.py assigns EXACT_SYNONYM to every imported ARO synonym, explaining the confirmed product-name typing defect. |
| chemistry | https://www.ebi.ac.uk/chebi/CHEBI:3515; https://pubchem.ncbi.nlm.nih.gov/compound/5479529; https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL1436.json; https://rest.kegg.jp/get/C06894; https://rest.kegg.jp/get/D00262; Complete visible ChEBI names/structure/relations/xrefs; official PubChem and ChEMBL structure responses; both KEGG entries and molfiles. | supports | Native formula, charge, mass, SMILES, InChI and key agree with neutral cefuroxime. Independent parses of PubChem SMILES, ChEMBL SMILES/InChI, both KEGG molfiles and GSRS SMILES/molfile all reproduce the native full key. CAS 55268-75-2, the neutral systematic names and chemical links are publicly attested. KEGG identifies the same active moiety and separately groups sodium and axetil products. |
| classes | https://www.ebi.ac.uk/chebi/CHEBI:24129; https://www.ebi.ac.uk/chebi/CHEBI:28084; https://www.ebi.ac.uk/chebi/CHEBI:36816; https://www.ebi.ac.uk/chebi/CHEBI:33281; https://card.mcmaster.ca/aro/0000032; Official parent labels/definitions and source relations. | supports | Furans, 3-(carbamoyloxymethyl)cephalosporin and oxime O-ether are genuinely broader structural categories; antimicrobial agent is an activity role. ARO 0000032 is the broader cephalosporin class. Current ChEBI has additional roles beyond the captured antimicrobial role; a current source expansion does not prove the frozen record was wrong. |
| aliases-registry | https://www.ebi.ac.uk/chebi/CHEBI:3515; https://drugcentral.org/drugcard/565; DrugBank:DB01112; MetaCyc:CPD0-2069; Reaxys:5783190; https://en.wikipedia.org/wiki/Cefuroxime; ChEBI exact names and manual links, DrugCentral identity card, resolved encyclopedia identity; bounded access attempts for other registries. | partial | ChEBI and ARO attest the imported lexical aliases, but source attestation does not validate their native synonym types. Sharox and Zinacef Danmark are already BRAND_NAME; ARO-derived Zinacef is incorrectly EXACT_SYNONYM as confirmed by the separate official label check. Biofuroksym and Cefuril require their own product-specific verification before assigning exact form scope. DrugCentral 565 identifies cefuroxime with the neutral formula. DrugBank returned 403, MetaCyc returned a login page, and Reaxys was not accessed behind its service boundary; these identifiers are verified as public ChEBI links, not independently revalidated chemical graphs. Wikipedia is a document link and not primary mechanism support. |
| patents | https://patents.google.com/patent/DE2439880A1; https://patents.google.com/patent/DE2706413A1; https://patents.google.com/patent/US3974153A; https://patents.google.com/patent/US4267320A; Original titles and selected abstract/description passages; German descriptions inspected alongside the displayed translation. | context_only | All four patent document identifiers resolve. DE2439880 and US3974153 concern syn oxyimino/carbamoyloxymethyl cephalosporin chemistry; DE2706413 and US4267320 explicitly describe ester derivatives of the cefuroxime parent. These are relevant document references, not four assertions of exact chemical equivalence. Patent scaffold claims, ester oral exposure and Google automated chemical annotations are not transferred as measured neutral-cefuroxime activity or mechanism. |
| card | https://card.mcmaster.ca/aro/0000063; https://card.mcmaster.ca/aro/3000749; ARO:3001818; ARO:3003561; ARO:3004825; ARO:3004826; ARO:3004854; ARO:3004856; ARO:3005035; ARO:3007180; ARO:3007437; ARO:3007635; Official identity, class, relation and publication sections of all ten determinant pages, cefuroxime page and generic PBP term. | supports | ARO 0000063 is cefuroxime; ARO 3000749 is generic beta-lactam-sensitive PBP. All ten exact determinant labels and cefuroxime relations agree: ACC-4, SED-1, LAP-1, LAP-2, CMY-136, SCO-1, YRC-1, MAB, EBR-5 and CAE-1. All are classified by CARD as antibiotic inactivation. Database verification does not turn every relation into an equally strong direct biochemical or clinical-resistance claim. |
| original-activity | PMID:1259408; DOI:10.1128/AAC.9.3.520; https://pmc.ncbi.nlm.nih.gov/articles/PMC429563/; PMID:1259407; DOI:10.1128/AAC.9.3.511; https://pmc.ncbi.nlm.nih.gov/articles/PMC429562/; Adopted in-vivo abstract plus original scanned pages 520,523,525; companion in-vitro abstract/materials and pages 511–513 inspected visually. | partial | The original activity studies explicitly use cefuroxime sodium. In-vivo doses are calculated as free-acid amounts; the animal protection study supports the active moiety but is not an experiment on isolated neutral acid. The in-vitro paper uses agar dilution, specified inocula and 18-hour incubation; Table 1 reports grouped isolate geometric means rather than strain-specific MICs. Its sodium drawing is explicit. Antibacterial classification is supported, while numerical neutral-form claims require material qualification. |
| pbp-primary | https://www.jstage.jst.go.jp/article/chemotherapy1953/34/Supplement5/34_Supplement5_11/_pdf; Original 1986 paper, Methods and abstract on page 11, PBP figures 21–24 and results on page 16 inspected visually; English abstract on page 19 read. | partial | CXM is distinguished from the axetil prodrug. Bacterial membrane preparations compete with 14C-penicillin G after 10 minutes of CXM exposure at 30 degrees C; fluorography measures PBP competition in specific S. aureus, E. coli, Serratia and Proteus systems. MRSA PBP2-prime binds poorly. This supports a bounded PBP interaction, not a universal affinity value or Kd. Exact CXM counterion is not specified in the inspected material section. Complement and macrophage experiments are host-context effects, not additional bacterial molecular targets. |
| adopted-primary | PMID:11168076; PMID:11322179; PMID:11581233; PMID:12141712; PMID:12235459; PMID:12833570; PMID:12898829; PMID:15052582; Complete original indexed abstracts and bibliographic records for all eight IDs. | context_only | 11168076 tests cefuroxime/tobramycin time-kill and endotoxin release in a clinical E. coli isolate; its PBP3 wording is background, not a new binding measurement. 11322179 measures endothelial thymidine incorporation and is a host-cell study. 11581233 is hospital antibiotic-use/resistance observation, not isolated enzyme causality. 12141712 is an IgE anaphylaxis case. 12235459 describes eight pediatric neck-abscess cases. 12833570 concerns synthetic antigenic determinants and IgE recognition. 12898829 is a pediatrician prescribing/post-treatment flora survey. 15052582 validates LC-MS/MS serum/plasma quantification; its LOQ is not an MIC. All remain leads within those precise scopes. |
| adopted-reviews | PMID:14658923; DOI:10.2165/00148581-200305120-00005; PMID:15828440; DOI:10.1179/joc.2005.17.1.25; Complete indexed abstracts and publication-type records. | context_only | 14658923 is a clinical-treatment review and 15828440 is a synthesis of Turkish pneumococcal resistance evidence. They are secondary context, not newly inspected primary experiments and not independent support for a molecular causal chain. Together with the eight primary abstracts and original 1259408, this accounts for all eleven adopted bibliography leads. |
| acc-sed-lap | PMID:17664321; DOI:10.1128/AAC.00389-07; PMID:11451687; DOI:10.1128/AAC.45.8.2287-2298.2001; PMID:17116662; DOI:10.1128/AAC.01082-06; Original PMC article Methods, cefuroxime results and relevant tables inspected after ordinary ?page=1 retries; complete indexed abstracts also read. | partial | ACC-4 Table 2 compares isogenic E. coli MC4100 constructs: cefuroxime MIC greater than 512 µg/mL for ACC-4 versus 128 for ACC-1 and 1 for empty vectors. SED-1 Table 3 shows a cloned-gene susceptibility shift; Table 4 reports cefuroxime hydrolysis. LAP-1 Table 1 has 8 µg/mL for the clone versus 2 for control and Table 2 has bounded kinetic values, including kcat greater than 100 s−1 and Km greater than 2000 µM. These are distinct experimental endpoints, not universal clinical resistance or exact neutral-material measurements. |
| sco | PMID:17353248; DOI:10.1128/AAC.01439-06; PMID:17420213; DOI:10.1128/AAC.01600-06; Both original PMC texts, cloning/susceptibility methods and cefuroxime tables inspected. | partial | The E. coli SCO-1 study Table 1 has cefuroxime MIC 1 µg/mL both for the single-enzyme clone and control; its multi-enzyme plasmid carries ACC-1 and TEM-1 as well. The Acinetobacter-derived SCO-1 study Table 2 has 4 versus 2 µg/mL for clone/control; Table 3 measures weak cefuroxime hydrolysis, kcat 0.05 s−1 and Km 650 µM. Do not transfer the highly resistant clinical isolate phenotype to SCO-1 alone. The latter article inconsistently labels the cloned host TOP10 in the header and DH10B in text/footnotes; exact strain-level enrichment should preserve that unresolved source discrepancy. |
| ebr-cae | PMID:36719228; DOI:10.1128/spectrum.00039-23; https://pmc.ncbi.nlm.nih.gov/articles/PMC10101081/; PMID:36869066; DOI:10.1038/s41598-023-28312-w; https://pmc.ncbi.nlm.nih.gov/articles/PMC9984417/; Full original main-text XML for both papers read, including Methods and all activity/kinetic tables; EBR-5 capture259 reused directly as primary text. | partial | EBR-5 Table 1 gives cefuroxime 128 mg/L for E. stercoris SCVM0123, 32 for E. coli BL21 carrying pET24a-blaEBR-5 and 0.5 for empty vector, with 50 mg/L kanamycin and 0.2 mM IPTG. Table 2 directly measures cefuroxime hydrolysis, kcat 2.1 s−1 and Km 19 µM. CAE-1 Table 2 gives cefuroxime at least 64 µg/mL for the E. coli cloned construct versus 4 for empty vector. CAE-1 purification failed, so that study does not supply purified-enzyme kinetics. Material counterions remain unspecified; neither resistant isolate is a cefuroxime producer. |
| resistance-other | PMID:16982792; PMID:18550213; PMID:30788955; PMID:20956594; PMID:16553832; PMID:24132992; PMID:28096155; All seven original bibliographic records and every available complete indexed abstract;18550213 has no abstract. | partial | 16982792 is LAP-1-associated genetic prevalence, not independent cefuroxime enzyme proof. LAP-2 paper 18550213 is a brief letter without an indexed abstract; its functional table was not inspected. CMY-136 paper 30788955 explicitly reports increased cefuroxime resistance for the Y221H variant, but full assay tables were not read. SCO-1 paper 20956594 is plasmid sequencing and is not a new single-enzyme phenotype. YRC-1 paper 16553832 reports cloned/purified enzyme work but its abstract does not expose exact cefuroxime values. MAB paper 24132992 reports biochemical work without cefuroxime values in the abstract; 28096155 concerns imipenem/avibactam in macrophages and zebrafish with RT-qPCR, not a cefuroxime experiment or transcriptomics dataset. These seven plus the seven detailed original papers account for all fourteen resistance-linked records. |
| fda | https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&amp;ApplNo=065048; https://api.fda.gov/drug/drugsfda.json?search=application_number:ANDA 065048; Current official application HTML and structured response, original approval and exact product rows003/004; GSRS current record. | supports | FDA explicitly retains ANDA 065048 products 003 and 004 as CEFUROXIME, ingredient CEFUROXIME, Prescription, 1.5G/20ML and 1.5G/100ML; original AP approval is 2004-01-09. Products 001/002 are separately labeled CEFUROXIME SODIUM. GSRS O1R9FJ93ED has the matching neutral graph, now version 50 rather than the captured 47. The native fields faithfully reproduce these product rows. FDA product category is the basis for currently_marketed, not an independent inventory check. |
| fda-form-boundary | https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=19902965-d2d6-433f-982d-0095014df4e8; https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=703cc338-c0b6-4a02-b8db-c27aeff181df; Both linked SPL descriptions, ingredient tables, NDC/product form and application fields. | partial | These labels describe cefuroxime sodium powder vials, with sodium ingredient UNII R8A7M9MY61 and neutral active moiety O1R9FJ93ED. Application-level openFDA metadata likewise aggregates the sodium ingredient. The inspected labels do not directly map the specific 003/004 solution product rows to that salt material. Their shared application number is therefore insufficient to confirm a neutral-record salt misassignment; exact product/form qualification remains unresolved. |
| adapter | 265-imodulondb-datasets.txt;265-imodulondb-pbp.txt; Structured adapter catalog and penicillin query executed before open-ended web research. | context_only | e_coli/precise1k returns gene b2430/yfeW, penicillin-binding protein 4B, and zero iModulon hits. Native PBP is taxon-generic, and the catalog does not cover several named source species. There is no relevant component to summarize. This result neither proves nor refutes binding, resistance, MIC or an expression response. |
| search | 265-inclusive-hits.txt; Hidden- and ignored-inclusive exact local search and bounded public source retrieval. | context_only | The exact record, source rows, queue and generated projections were found. No exact corrective overlay or exclusion decision was found in the searched paths. The queue is a readiness lead, not evidence that a mode enum is mandatory or scientific sign-off is complete. Historical reports and search snippets were not used as primary proof. |
| validation | 265-schema.log;265-strict.log;265-strict.tsv;265-chemistry.json;265-xref-chemistry.json; Actual focused command outputs and independent official-graph parses. | supports | Schema and strict validation both exit 0. SMILES and InChI independently reproduce native composition, mass, charge and R/R centres; both source mints reproduce exactly. Seven independently parsed official encodings agree with the native key. This supports deterministic identity consistency, not universal assay or literature coverage. |
| zinacef-brand | https://assets.hpra.ie/products/Human/24420/Licence_PA23311-002-001_20052026091036.pdf; https://www.hpra.ie/find-a-medicine/for-human-use/authorised-medicines/details/24422; HPRA Summary of Product Characteristics, 20 May 2026, sections 1–3; current official 1.5 g product identity and active-substance field. | refutes | The official SmPC names Zinacef 250 mg powder for injection/infusion and specifies 250 mg cefuroxime as cefuroxime sodium per vial. The current 1.5 g product page likewise identifies cefuroxime sodium. This confirms Zinacef is a medicinal-product brand, not an exact chemical synonym for the native neutral graph. The related ChEBI alias Zinacef Danmark is already BRAND_NAME. No conclusion about FDA ANDA 065048 products 003/004 follows from these distinct Irish products. |

## Limits And Additional Notes

- Whole-record coverage is complete, but scientific completion is partial: all eleven adopted bibliography entries and fourteen resistance-linked records were checked, with access depths stated individually rather than implying every paper was read in full.
- Selected original 1976 scanned pages and the 1986 PBP Methods/results/figures were inspected directly. Other animal tables and all remaining 1986 sections were not independently audited; no unsupported numeric extraction is asserted.
- ACC-4, SED-1, LAP-1 and both SCO-1 original texts were inspected for relevant methods, results and tables after ordinary PMC?page=1 retrieval succeeded. Genetic-context figures were not independently audited. EBR-5 and CAE-1 main-text XML were read; supplementary methods were not independently audited.
- LAP-2 lacks an indexed abstract; its full letter remains uninspected. CMY-136, YRC-1 and MAB biochemical evidence is bounded to complete original abstracts, with companion genetic/host studies kept in their actual scope.
- Several original papers specify sodium salt or leave counterion unspecified. Neither establishes all reported endpoints for independently isolated neutral acid. The native record currently contains no numerical activity claim needing removal on that basis.
- DrugBank returned 403; MetaCyc resolved to a login page; Reaxys was not accessed. Public ChEBI attests those identifiers, but independent exact graph confirmation in those services remains incomplete. Patent description checks verify relevant document scope, not all legal claims or every experimental example.
- Current official FDA and GSRS rows were checked; exact 003/004 solution material remains unresolved because the inspected linked SPLs describe sodium powder vials. This does not establish a confirmed wrong-form join.
- Structured expression-source search was performed before web research. Its zero module hit and absent species coverage are not biological negative evidence. No transcriptomics dataset is inferred from targeted RT-qPCR.
- The supplemental brand check confirms Zinacef from an HPRA label and current product page. Biofuroksym manufacturer retrieval returned 403, and no exact Cefuril product was independently resolved from a primary official label; discovery snippets are not treated as proof for either name. The confirmed finding is therefore limited to Zinacef.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T122749Z-cefuroxime
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cefuroxime: coherent neutral identity with one confirmed brand-synonym typing
  defect'
started_at: '2026-10-21T12:02:25Z'
finished_at: '2026-10-21T12:27:49Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author the seed. Read the entire record and actual source
    rows, inspected official chemical and regulatory sources and original scientific
    text, and executed focused validation independently. Initial provenance was captured
    by root before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'The native neutral cefuroxime structure, structural definition, broader
  classes, source concepts and resolved chemical graphs agree. The PBP and ten resistance
  entries accurately retain database provenance. Original studies support antibacterial
  activity, PBP competition and several enzyme-specific resistance mechanisms, with
  sodium-material and strain/assay boundaries. FDA product rows match their current
  official source; application-level sodium labels alone do not prove that the two
  neutral-named product rows were misassigned. One minor correction is confirmed:
  ARO-derived Zinacef is typed EXACT_SYNONYM even though the official regulator identifies
  it as a sodium-containing medicinal product; retain it with appropriate brand scope.
  This is separate from the unresolved FDA product 003/004 material question. Full
  primary coverage, several registry access checks and exact product/form qualification
  remain limited.'
source:
  git_revision: baf3b3203d748d098686e166cdb2a6138f47eb59
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 5e2e1f975f8aa64f92a06c134c98c750c968fd78f02620a73c9cb611ac018ed8
    role: context
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
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
  - path: data/antibiotics/antibacterial/cefuroxime.yaml
    sha256: 633e9f37482c6b643158430610d339544eee02cfd4b2b390ad41c1305078e713
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
  - path: data/raw/fda_clinical_status.tsv
    sha256: a6952f85426afa53c5704c588681a078e599ce245bf18f7c9dd390d70e7bb16c
    role: context
  - path: docs/CURATION.md
    sha256: a364598a9c2bdaf9e0e71895d5b7a2fd61d3e726e0ed0da12bd895cc4c30e98c
    role: context
  - path: docs/HARMONIZATION.md
    sha256: fb8b58abca016ca5a7d856fcc6f1ec2deb210e0927394a480853830b39e1f060
    role: context
  - path: scripts/extract_fda_clinical_status.py
    sha256: f30f385ea6d530dc1749e3d805dbcdbc8715fbc476abc510bf144ea13964e171
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
- target_id: CHEBI:3515
  path: data/antibiotics/antibacterial/cefuroxime.yaml
  label: cefuroxime
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI and ARO source normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO aliases, cephalosporin class and source concept
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Imported PBP target assertion owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Ten imported antibiotic-inactivation assertion owners
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/fda_clinical_status.tsv
    role: Two imported FDA product assertions
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Target relation and evidence-status policy
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: FDA ingredient-to-UNII identity join and original-approval/marketing interpretation
scope:
  description: Entire YAML, including all fifteen synonyms, definition, structural
    and activity classifications, chemical and drug cross-references, four patent
    links, structure descriptors, two source concepts, ten resistance entries, PBP
    target, two FDA assertions and seven history events. All eleven adopted antibiotic
    bibliography records and all fourteen distinct resistance-linked publication records
    were inspected at the access depths stated below.
  selection: Queue 265. Original thirteen captured inputs preserved; six actual source/transform
    inputs appended before substantive judgment, for nineteen total.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:3515
  exclusions:
  - target: Cefuroxime sodium, cefuroxime axetil, combination treatments and other
      cephalosporins
    reason: They inform active-moiety or comparator context but are not silently substituted
      for the exact neutral structure or its measurements.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: 'Documented per-record schema validation: no issues found.'
  target_ids:
  - CHEBI:3515
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefuroxime.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: 'Documented strict validator: one file scanned, zero errors.'
  target_ids:
  - CHEBI:3515
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefuroxime.yaml --out /private/tmp/am-review-session/265-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: 'Supplementary RDKit consistency check from batch027 cwd using batch019
    interpreter: both structure encodings and both source mints agree.'
  target_ids:
  - CHEBI:3515
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 265
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
  - CHEBI:3515
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
  - CHEBI:3515
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
  - CHEBI:3515
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
  - CHEBI:3515
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
  - CHEBI:3515
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
  - CHEBI:3515
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
  - CHEBI:3515
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
  - CHEBI:3515
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
  - CHEBI:3515
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/cefuroxime.yaml
  locator: Entire native record and all seven history events.
  accessed_at: '2026-10-21T12:20:51Z'
  support: supports
  summary: SEEDED, EXACT and ANTIBACTERIAL. Native neutral cefuroxime has formula
    C16H16N4O8S, charge zero, two R stereocentres and key JFPVXVDWJQMJEE-IZRZKJBUSA-N.
    The target explicitly remains PRIMARY_EVIDENCE_NEEDED, and all resistance notes
    identify imported database assertions. There are no quantitative activity, causal-graph,
    producer or transcriptomics objects; their absence is not by itself a required-field
    defect.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv;
    data/raw/aro_resistance_edges.tsv; data/raw/fda_clinical_status.tsv; conf/aro_target_roles.tsv;
    scripts/extract_source_inventory.py; scripts/extract_fda_clinical_status.py; scripts/seed_from_sources.py
  locator: Exact ChEBI row 95, ARO row 48, target row 49, resistance rows 1692–1701
    and FDA rows 1410–1411; source configuration and relevant extraction/seeding logic.
  accessed_at: '2026-10-21T12:20:51Z'
  support: supports
  summary: ChEBI supplies structural definition, identity, roles and ten publication
    leads. ARO supplies its aliases, class, source concept and one additional publication
    lead. Target/resistance transforms preserve database provenance. FDA extraction
    maps each eligible literal ingredient to its unique UNII, joins the GSRS full
    key, takes the earliest original AP approval and interprets Prescription as currently
    marketed. The captured rows are reproducible; their interpretation should remain
    product-qualified. The ARO concept constructor in scripts/seed_from_sources.py
    assigns EXACT_SYNONYM to every imported ARO synonym, explaining the confirmed
    product-name typing defect.
  snapshot_sha256: f12a961c5dfc7f459b67697dc1d8202a37aff83b3da426091e885235ee3ae6be
- evidence_id: chemistry
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:3515; https://pubchem.ncbi.nlm.nih.gov/compound/5479529;
    https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL1436.json; https://rest.kegg.jp/get/C06894;
    https://rest.kegg.jp/get/D00262
  locator: Complete visible ChEBI names/structure/relations/xrefs; official PubChem
    and ChEMBL structure responses; both KEGG entries and molfiles.
  accessed_at: '2026-10-21T12:20:51Z'
  support: supports
  summary: Native formula, charge, mass, SMILES, InChI and key agree with neutral
    cefuroxime. Independent parses of PubChem SMILES, ChEMBL SMILES/InChI, both KEGG
    molfiles and GSRS SMILES/molfile all reproduce the native full key. CAS 55268-75-2,
    the neutral systematic names and chemical links are publicly attested. KEGG identifies
    the same active moiety and separately groups sodium and axetil products.
  snapshot_sha256: ce1e42bc08ec506bc1260a2bddfd66177e85b25897942ec97fad517140e06659
- evidence_id: classes
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:24129; https://www.ebi.ac.uk/chebi/CHEBI:28084;
    https://www.ebi.ac.uk/chebi/CHEBI:36816; https://www.ebi.ac.uk/chebi/CHEBI:33281;
    https://card.mcmaster.ca/aro/0000032
  locator: Official parent labels/definitions and source relations.
  accessed_at: '2026-10-21T12:13:25Z'
  support: supports
  summary: Furans, 3-(carbamoyloxymethyl)cephalosporin and oxime O-ether are genuinely
    broader structural categories; antimicrobial agent is an activity role. ARO 0000032
    is the broader cephalosporin class. Current ChEBI has additional roles beyond
    the captured antimicrobial role; a current source expansion does not prove the
    frozen record was wrong.
  snapshot_sha256: b4eeef154afe2816cca0d13e7dddefb8b61bec1423a8359b58c17550d23852d3
- evidence_id: aliases-registry
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:3515; https://drugcentral.org/drugcard/565;
    DrugBank:DB01112; MetaCyc:CPD0-2069; Reaxys:5783190; https://en.wikipedia.org/wiki/Cefuroxime
  locator: ChEBI exact names and manual links, DrugCentral identity card, resolved
    encyclopedia identity; bounded access attempts for other registries.
  accessed_at: '2026-10-21T12:13:21Z'
  support: partial
  summary: ChEBI and ARO attest the imported lexical aliases, but source attestation
    does not validate their native synonym types. Sharox and Zinacef Danmark are already
    BRAND_NAME; ARO-derived Zinacef is incorrectly EXACT_SYNONYM as confirmed by the
    separate official label check. Biofuroksym and Cefuril require their own product-specific
    verification before assigning exact form scope. DrugCentral 565 identifies cefuroxime
    with the neutral formula. DrugBank returned 403, MetaCyc returned a login page,
    and Reaxys was not accessed behind its service boundary; these identifiers are
    verified as public ChEBI links, not independently revalidated chemical graphs.
    Wikipedia is a document link and not primary mechanism support.
  snapshot_sha256: a497bfec06ac62f6d1bac2733c02de83a6f95eea57497e489de24ac4ef0f5a32
- evidence_id: patents
  kind: primary_source
  reference: https://patents.google.com/patent/DE2439880A1; https://patents.google.com/patent/DE2706413A1;
    https://patents.google.com/patent/US3974153A; https://patents.google.com/patent/US4267320A
  locator: Original titles and selected abstract/description passages; German descriptions
    inspected alongside the displayed translation.
  accessed_at: '2026-10-21T12:13:27Z'
  support: context_only
  summary: All four patent document identifiers resolve. DE2439880 and US3974153 concern
    syn oxyimino/carbamoyloxymethyl cephalosporin chemistry; DE2706413 and US4267320
    explicitly describe ester derivatives of the cefuroxime parent. These are relevant
    document references, not four assertions of exact chemical equivalence. Patent
    scaffold claims, ester oral exposure and Google automated chemical annotations
    are not transferred as measured neutral-cefuroxime activity or mechanism.
  snapshot_sha256: ef375dee3e94580dce132aecc2807dcbc69aa8b51fdca11f1bb3595c9be91fd8
- evidence_id: card
  kind: database
  reference: https://card.mcmaster.ca/aro/0000063; https://card.mcmaster.ca/aro/3000749;
    ARO:3001818; ARO:3003561; ARO:3004825; ARO:3004826; ARO:3004854; ARO:3004856;
    ARO:3005035; ARO:3007180; ARO:3007437; ARO:3007635
  locator: Official identity, class, relation and publication sections of all ten
    determinant pages, cefuroxime page and generic PBP term.
  accessed_at: '2026-10-21T12:13:21Z'
  support: supports
  summary: 'ARO 0000063 is cefuroxime; ARO 3000749 is generic beta-lactam-sensitive
    PBP. All ten exact determinant labels and cefuroxime relations agree: ACC-4, SED-1,
    LAP-1, LAP-2, CMY-136, SCO-1, YRC-1, MAB, EBR-5 and CAE-1. All are classified
    by CARD as antibiotic inactivation. Database verification does not turn every
    relation into an equally strong direct biochemical or clinical-resistance claim.'
  snapshot_sha256: 90e84e42cea05a5e38b36bf2e675f8608461029d5927a6226cbcf3d288a74e74
- evidence_id: original-activity
  kind: primary_source
  reference: PMID:1259408; DOI:10.1128/AAC.9.3.520; https://pmc.ncbi.nlm.nih.gov/articles/PMC429563/;
    PMID:1259407; DOI:10.1128/AAC.9.3.511; https://pmc.ncbi.nlm.nih.gov/articles/PMC429562/
  locator: Adopted in-vivo abstract plus original scanned pages 520,523,525; companion
    in-vitro abstract/materials and pages 511–513 inspected visually.
  accessed_at: '2026-10-21T12:15:58Z'
  support: partial
  summary: The original activity studies explicitly use cefuroxime sodium. In-vivo
    doses are calculated as free-acid amounts; the animal protection study supports
    the active moiety but is not an experiment on isolated neutral acid. The in-vitro
    paper uses agar dilution, specified inocula and 18-hour incubation; Table 1 reports
    grouped isolate geometric means rather than strain-specific MICs. Its sodium drawing
    is explicit. Antibacterial classification is supported, while numerical neutral-form
    claims require material qualification.
  snapshot_sha256: 8021f33d850ef1e98e2a7f2feff989d75d4d5c89b31795d476f0cf407f514f12
- evidence_id: pbp-primary
  kind: primary_source
  reference: https://www.jstage.jst.go.jp/article/chemotherapy1953/34/Supplement5/34_Supplement5_11/_pdf
  locator: Original 1986 paper, Methods and abstract on page 11, PBP figures 21–24
    and results on page 16 inspected visually; English abstract on page 19 read.
  accessed_at: '2026-10-21T12:14:38Z'
  support: partial
  summary: CXM is distinguished from the axetil prodrug. Bacterial membrane preparations
    compete with 14C-penicillin G after 10 minutes of CXM exposure at 30 degrees C;
    fluorography measures PBP competition in specific S. aureus, E. coli, Serratia
    and Proteus systems. MRSA PBP2-prime binds poorly. This supports a bounded PBP
    interaction, not a universal affinity value or Kd. Exact CXM counterion is not
    specified in the inspected material section. Complement and macrophage experiments
    are host-context effects, not additional bacterial molecular targets.
  snapshot_sha256: d85f9ab3d10d2afa5c45af843c773243acfe35f3b19b64844778588a7d0930bf
- evidence_id: adopted-primary
  kind: primary_source
  reference: PMID:11168076; PMID:11322179; PMID:11581233; PMID:12141712; PMID:12235459;
    PMID:12833570; PMID:12898829; PMID:15052582
  locator: Complete original indexed abstracts and bibliographic records for all eight
    IDs.
  accessed_at: '2026-10-21T12:13:25Z'
  support: context_only
  summary: 11168076 tests cefuroxime/tobramycin time-kill and endotoxin release in
    a clinical E. coli isolate; its PBP3 wording is background, not a new binding
    measurement. 11322179 measures endothelial thymidine incorporation and is a host-cell
    study. 11581233 is hospital antibiotic-use/resistance observation, not isolated
    enzyme causality. 12141712 is an IgE anaphylaxis case. 12235459 describes eight
    pediatric neck-abscess cases. 12833570 concerns synthetic antigenic determinants
    and IgE recognition. 12898829 is a pediatrician prescribing/post-treatment flora
    survey. 15052582 validates LC-MS/MS serum/plasma quantification; its LOQ is not
    an MIC. All remain leads within those precise scopes.
  snapshot_sha256: a1dd977912d5e152bb8e18725129bc6562a57f7351e9573c8cd0e504194c80d4
- evidence_id: adopted-reviews
  kind: database
  reference: PMID:14658923; DOI:10.2165/00148581-200305120-00005; PMID:15828440; DOI:10.1179/joc.2005.17.1.25
  locator: Complete indexed abstracts and publication-type records.
  accessed_at: '2026-10-21T12:13:25Z'
  support: context_only
  summary: 14658923 is a clinical-treatment review and 15828440 is a synthesis of
    Turkish pneumococcal resistance evidence. They are secondary context, not newly
    inspected primary experiments and not independent support for a molecular causal
    chain. Together with the eight primary abstracts and original 1259408, this accounts
    for all eleven adopted bibliography leads.
  snapshot_sha256: a1dd977912d5e152bb8e18725129bc6562a57f7351e9573c8cd0e504194c80d4
- evidence_id: acc-sed-lap
  kind: primary_source
  reference: PMID:17664321; DOI:10.1128/AAC.00389-07; PMID:11451687; DOI:10.1128/AAC.45.8.2287-2298.2001;
    PMID:17116662; DOI:10.1128/AAC.01082-06
  locator: Original PMC article Methods, cefuroxime results and relevant tables inspected
    after ordinary ?page=1 retries; complete indexed abstracts also read.
  accessed_at: '2026-10-21T12:18:30Z'
  support: partial
  summary: 'ACC-4 Table 2 compares isogenic E. coli MC4100 constructs: cefuroxime
    MIC greater than 512 µg/mL for ACC-4 versus 128 for ACC-1 and 1 for empty vectors.
    SED-1 Table 3 shows a cloned-gene susceptibility shift; Table 4 reports cefuroxime
    hydrolysis. LAP-1 Table 1 has 8 µg/mL for the clone versus 2 for control and Table
    2 has bounded kinetic values, including kcat greater than 100 s−1 and Km greater
    than 2000 µM. These are distinct experimental endpoints, not universal clinical
    resistance or exact neutral-material measurements.'
  snapshot_sha256: 0d6c1c51c7c3cb3216008c2d76cfe2247224055df58af4d15567b718ada91153
- evidence_id: sco
  kind: primary_source
  reference: PMID:17353248; DOI:10.1128/AAC.01439-06; PMID:17420213; DOI:10.1128/AAC.01600-06
  locator: Both original PMC texts, cloning/susceptibility methods and cefuroxime
    tables inspected.
  accessed_at: '2026-10-21T12:18:30Z'
  support: partial
  summary: The E. coli SCO-1 study Table 1 has cefuroxime MIC 1 µg/mL both for the
    single-enzyme clone and control; its multi-enzyme plasmid carries ACC-1 and TEM-1
    as well. The Acinetobacter-derived SCO-1 study Table 2 has 4 versus 2 µg/mL for
    clone/control; Table 3 measures weak cefuroxime hydrolysis, kcat 0.05 s−1 and
    Km 650 µM. Do not transfer the highly resistant clinical isolate phenotype to
    SCO-1 alone. The latter article inconsistently labels the cloned host TOP10 in
    the header and DH10B in text/footnotes; exact strain-level enrichment should preserve
    that unresolved source discrepancy.
  snapshot_sha256: 754d957bae77af259e81f9cf25e721e039b3b36091a2a034f573f5bacb0d9487
- evidence_id: ebr-cae
  kind: primary_source
  reference: PMID:36719228; DOI:10.1128/spectrum.00039-23; https://pmc.ncbi.nlm.nih.gov/articles/PMC10101081/;
    PMID:36869066; DOI:10.1038/s41598-023-28312-w; https://pmc.ncbi.nlm.nih.gov/articles/PMC9984417/
  locator: Full original main-text XML for both papers read, including Methods and
    all activity/kinetic tables; EBR-5 capture259 reused directly as primary text.
  accessed_at: '2026-10-21T12:15:29Z'
  support: partial
  summary: EBR-5 Table 1 gives cefuroxime 128 mg/L for E. stercoris SCVM0123, 32 for
    E. coli BL21 carrying pET24a-blaEBR-5 and 0.5 for empty vector, with 50 mg/L kanamycin
    and 0.2 mM IPTG. Table 2 directly measures cefuroxime hydrolysis, kcat 2.1 s−1
    and Km 19 µM. CAE-1 Table 2 gives cefuroxime at least 64 µg/mL for the E. coli
    cloned construct versus 4 for empty vector. CAE-1 purification failed, so that
    study does not supply purified-enzyme kinetics. Material counterions remain unspecified;
    neither resistant isolate is a cefuroxime producer.
  snapshot_sha256: ed309640fafcce7ec4bd7846dd93742f6b867dd477cd1c6e66d7e2c15348e971
- evidence_id: resistance-other
  kind: primary_source
  reference: PMID:16982792; PMID:18550213; PMID:30788955; PMID:20956594; PMID:16553832;
    PMID:24132992; PMID:28096155
  locator: All seven original bibliographic records and every available complete indexed
    abstract;18550213 has no abstract.
  accessed_at: '2026-10-21T12:14:38Z'
  support: partial
  summary: 16982792 is LAP-1-associated genetic prevalence, not independent cefuroxime
    enzyme proof. LAP-2 paper 18550213 is a brief letter without an indexed abstract;
    its functional table was not inspected. CMY-136 paper 30788955 explicitly reports
    increased cefuroxime resistance for the Y221H variant, but full assay tables were
    not read. SCO-1 paper 20956594 is plasmid sequencing and is not a new single-enzyme
    phenotype. YRC-1 paper 16553832 reports cloned/purified enzyme work but its abstract
    does not expose exact cefuroxime values. MAB paper 24132992 reports biochemical
    work without cefuroxime values in the abstract; 28096155 concerns imipenem/avibactam
    in macrophages and zebrafish with RT-qPCR, not a cefuroxime experiment or transcriptomics
    dataset. These seven plus the seven detailed original papers account for all fourteen
    resistance-linked records.
  snapshot_sha256: 108be71cfde73d3b09fb342117671effad964563d6c067eb19a3ad6af28ac524
- evidence_id: fda
  kind: authority
  reference: https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=065048;
    https://api.fda.gov/drug/drugsfda.json?search=application_number:ANDA 065048
  locator: Current official application HTML and structured response, original approval
    and exact product rows003/004; GSRS current record.
  accessed_at: '2026-10-21T12:13:26Z'
  support: supports
  summary: FDA explicitly retains ANDA 065048 products 003 and 004 as CEFUROXIME,
    ingredient CEFUROXIME, Prescription, 1.5G/20ML and 1.5G/100ML; original AP approval
    is 2004-01-09. Products 001/002 are separately labeled CEFUROXIME SODIUM. GSRS
    O1R9FJ93ED has the matching neutral graph, now version 50 rather than the captured
    47. The native fields faithfully reproduce these product rows. FDA product category
    is the basis for currently_marketed, not an independent inventory check.
  snapshot_sha256: b3ecadc078829fd7fa9c2403cb7ac7cb0614e1a544b65b2733ad7b7ce1da1f62
- evidence_id: fda-form-boundary
  kind: authority
  reference: https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=19902965-d2d6-433f-982d-0095014df4e8;
    https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=703cc338-c0b6-4a02-b8db-c27aeff181df
  locator: Both linked SPL descriptions, ingredient tables, NDC/product form and application
    fields.
  accessed_at: '2026-10-21T12:14:38Z'
  support: partial
  summary: These labels describe cefuroxime sodium powder vials, with sodium ingredient
    UNII R8A7M9MY61 and neutral active moiety O1R9FJ93ED. Application-level openFDA
    metadata likewise aggregates the sodium ingredient. The inspected labels do not
    directly map the specific 003/004 solution product rows to that salt material.
    Their shared application number is therefore insufficient to confirm a neutral-record
    salt misassignment; exact product/form qualification remains unresolved.
  snapshot_sha256: baec5e45068ffbab7681c022d6d9f15534ff12e4dea552fcc772589e562a4676
- evidence_id: adapter
  kind: database
  reference: 265-imodulondb-datasets.txt;265-imodulondb-pbp.txt
  locator: Structured adapter catalog and penicillin query executed before open-ended
    web research.
  accessed_at: '2026-10-21T12:20:51Z'
  support: context_only
  summary: e_coli/precise1k returns gene b2430/yfeW, penicillin-binding protein 4B,
    and zero iModulon hits. Native PBP is taxon-generic, and the catalog does not
    cover several named source species. There is no relevant component to summarize.
    This result neither proves nor refutes binding, resistance, MIC or an expression
    response.
  snapshot_sha256: b0f3ec2d7316806c534510fc9e133a264a0079b8388c2e423af73d3f40edf70a
- evidence_id: search
  kind: search
  reference: 265-inclusive-hits.txt
  locator: Hidden- and ignored-inclusive exact local search and bounded public source
    retrieval.
  accessed_at: '2026-10-21T12:20:51Z'
  support: context_only
  summary: The exact record, source rows, queue and generated projections were found.
    No exact corrective overlay or exclusion decision was found in the searched paths.
    The queue is a readiness lead, not evidence that a mode enum is mandatory or scientific
    sign-off is complete. Historical reports and search snippets were not used as
    primary proof.
  snapshot_sha256: 2d98533a52134ceab17399d68902cbd4ad1fa7c725fa624fb61b0db05a88bd49
  search_scope: rg --no-ignore --hidden -n -F for CHEBI:3515, cefuroxime, full InChIKey
    and source mint across data, curation, conf, scripts, src, docs, .claude, reviews
    and reports; public exact-identity, adopted-PMID, PBP and official-product retrieval
    on 2026-10-21.
- evidence_id: validation
  kind: validation
  reference: 265-schema.log;265-strict.log;265-strict.tsv;265-chemistry.json;265-xref-chemistry.json
  locator: Actual focused command outputs and independent official-graph parses.
  accessed_at: '2026-10-21T12:20:51Z'
  support: supports
  summary: Schema and strict validation both exit 0. SMILES and InChI independently
    reproduce native composition, mass, charge and R/R centres; both source mints
    reproduce exactly. Seven independently parsed official encodings agree with the
    native key. This supports deterministic identity consistency, not universal assay
    or literature coverage.
  snapshot_sha256: 3b9fc97e74916125e52e0f105e1a5e1a37ce9f69cee27fb5f54b3fc19d325919
- evidence_id: zinacef-brand
  kind: authority
  reference: https://assets.hpra.ie/products/Human/24420/Licence_PA23311-002-001_20052026091036.pdf;
    https://www.hpra.ie/find-a-medicine/for-human-use/authorised-medicines/details/24422
  locator: HPRA Summary of Product Characteristics, 20 May 2026, sections 1–3; current
    official 1.5 g product identity and active-substance field.
  accessed_at: '2026-10-21T12:25:35Z'
  support: refutes
  summary: The official SmPC names Zinacef 250 mg powder for injection/infusion and
    specifies 250 mg cefuroxime as cefuroxime sodium per vial. The current 1.5 g product
    page likewise identifies cefuroxime sodium. This confirms Zinacef is a medicinal-product
    brand, not an exact chemical synonym for the native neutral graph. The related
    ChEBI alias Zinacef Danmark is already BRAND_NAME. No conclusion about FDA ANDA
    065048 products 003/004 follows from these distinct Irish products.
  snapshot_sha256: 5a9e9ad9530810008e819a75416f4814ce4342b8d888d97b20eb190853901134
assessments:
- assessment_id: identity
  area: identity
  topic: Neutral structure, names and equivalent chemical identifiers
  outcome: supported
  summary: The neutral 6R,7R/Z cefuroxime graph is coherent across inspected official
    structures. The definition names its exact structural substituents and the broader
    classes are appropriate. Drug/document links retain their own scopes, including
    prodrug patents and form-qualified brand context. Restricted registry access is
    an explicit limit, not a confirmed broken identifier. The separate Zinacef exact-synonym
    typing defect requires correction; the chemical graph itself remains supported.
  target_ids:
  - CHEBI:3515
  evidence_ids:
  - record
  - chemistry
  - classes
  - aliases-registry
  - patents
  - validation
- assessment_id: activity
  area: scope
  topic: Antibacterial filing and assay material
  outcome: supported
  summary: Original papers support the cefuroxime active moiety as antibacterial,
    with sodium salt explicitly used in the 1976 experiments. No native numeric endpoint
    is falsely asserted for isolated neutral acid. Generic antimicrobial role alongside
    antibacterial filing is valid; source snapshot role differences are not corrective
    findings.
  target_ids:
  - CHEBI:3515
  evidence_ids:
  - source
  - classes
  - original-activity
  - adopted-primary
- assessment_id: target
  area: evidence
  topic: Generic PBP database relation and original competition data
  outcome: supported
  summary: The generic target honestly remains PRIMARY_EVIDENCE_NEEDED. The original
    1986 membrane competition study supplies useful organism- and PBP-specific evidence,
    but no neutral-form dissociation constant or universal whole-cell causal chain.
    Host complement/macrophage and endothelial effects are not bacterial targets.
  target_ids:
  - CHEBI:3515
  evidence_ids:
  - record
  - card
  - pbp-primary
  - adopted-primary
  - adapter
- assessment_id: resistance
  area: evidence
  topic: Ten database assertions versus experimental strength
  outcome: supported
  summary: All imported relations agree with CARD. Primary support varies from direct
    cefuroxime hydrolysis and cloned-gene effects to limited abstract evidence. SCO-1
    in particular must not inherit the clinical multi-enzyme isolate phenotype; CAE-1
    has no successful purified-enzyme assay. These limits justify preserving database
    provenance, not equating the entries to strong clinical resistance or removing
    an accurately attributed relation solely for lacking stronger optional evidence.
  target_ids:
  - CHEBI:3515
  evidence_ids:
  - card
  - acc-sed-lap
  - sco
  - ebr-cae
  - resistance-other
- assessment_id: regulatory
  area: evidence
  topic: FDA product semantics and exact salt boundary
  outcome: unknown
  summary: The native approval date, product numbers, ingredient name and Prescription
    category match current FDA. The exact neutral GSRS join is reproducible. Sodium
    labels attached to the broader application do not identify the specific 003/004
    solution material conclusively; no confirmed chemical misassignment is reported.
    Clinical status remains a source-qualified product assertion rather than evidence
    that free neutral acid is the formulation.
  target_ids:
  - CHEBI:3515
  evidence_ids:
  - source
  - fda
  - fda-form-boundary
- assessment_id: coverage
  area: completeness
  topic: All adopted bibliography leads and optional enrichments
  outcome: unknown
  summary: All eleven adopted leads and fourteen resistance-linked publication records
    have explicit dispositions. Host adverse effects, analytical detection, observational
    prescribing and reviews do not add antimicrobial mechanism evidence. Missing quantitative
    activity, causal graph, producer and dataset objects are optional gaps, not standalone
    findings. Source organism names do not establish production, and RT-qPCR is not
    a dataset assertion.
  target_ids:
  - CHEBI:3515
  evidence_ids:
  - adopted-primary
  - adopted-reviews
  - original-activity
  - resistance-other
  - ebr-cae
- assessment_id: ownership
  area: ownership
  topic: Actual source owners and immutable inputs
  outcome: supported
  summary: The review distinguishes ChEBI identity, ARO database relations, FDA product
    extraction and curator-owned future literature claims. All nineteen input hashes
    remain unchanged; both original source mints reproduce. No native scientific-status
    promotion is implied by passing focused checks.
  target_ids:
  - CHEBI:3515
  evidence_ids:
  - source
  - record
  - search
  - validation
- assessment_id: brand-synonym
  area: identity
  topic: Brand alias incorrectly typed as exact chemical synonym
  outcome: concern
  summary: Zinacef at synonyms[14] is explicitly EXACT_SYNONYM from ARO, while the
    official label identifies a sodium-containing product. Preserve the useful name
    as BRAND_NAME or otherwise scoped product terminology. The valid neutral structure
    and all verified chemical xrefs remain intact. Biofuroksym and Cefuril are bounded
    follow-up checks, not confirmed wrong-form findings in this review.
  target_ids:
  - CHEBI:3515
  evidence_ids:
  - record
  - source
  - zinacef-brand
findings:
- finding_id: F1
  issue_key: cefuroxime-zinacef-brand-typed-as-exact-synonym
  category: identity
  severity: minor
  status: open
  certainty: confirmed
  title: Type Zinacef as a brand rather than an exact chemical synonym
  description: Native synonyms[14] asserts the ARO-derived name Zinacef as EXACT_SYNONYM.
    HPRA explicitly identifies Zinacef as a medicinal product containing cefuroxime
    sodium. Its shared active moiety makes the name useful, but does not make the
    product name exact neutral-structure terminology. The source constructor blindly
    assigns EXACT_SYNONYM to ARO aliases. Preserve Zinacef with brand/product scope
    through the maintained normalization path; do not replace or merge the valid neutral
    structure with sodium. Biofuroksym and Cefuril remain product-specific follow-up
    candidates and are not included in the confirmed field set.
  target_ids:
  - CHEBI:3515
  field_paths:
  - synonyms[14].synonym_type
  evidence_ids:
  - record
  - source
  - zinacef-brand
  rule_id: 'native-review-checklist: Identity and Equivalence; SynonymTypeEnum distinguishes
    BRAND_NAME from EXACT_SYNONYM'
  native_severity: minor
  normalization_reason: A bounded semantic typing/provenance defect in a useful drug
    alias. The neutral structure and stable exact chemical identifiers remain correct,
    so this does not warrant a structural blocker or wholesale identity change.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Imported lexical synonym source
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained synonym normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: ARO alias typing and generated synonym emission
actions:
- action_id: A3
  description: Correct the maintained Zinacef alias classification and separately
    verify other ARO product-name candidates.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:3515
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Imported lexical synonym source
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained synonym normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: ARO alias typing and generated synonym emission
  acceptance_checks:
  - Emit Zinacef as BRAND_NAME or another explicitly product-scoped synonym, retaining
    its ARO provenance and the original lexical name.
  - 'Do not apply a blanket conversion to all ARO aliases: retain actual exact chemical/INN
    names and abbreviations according to verified semantics. Check Biofuroksym and
    Cefuril against jurisdiction- and product-specific official sources before assigning
    their form scope.'
  - Preserve the neutral native graph, chemical xrefs and separate FDA product 003/004
    uncertainty; the Irish brand label does not resolve those US product materials.
  - Regenerate through the maintained source/seeder path and rerun focused schema/strict
    and applicable corpus checks, verifying that the next seed no longer restores
    EXACT_SYNONYM for Zinacef.
- action_id: A1
  description: If primary target or resistance enrichment is undertaken, preserve
    exact material, organism and experimental endpoints beside the existing database
    assertions.
  finding_ids: []
  target_ids:
  - CHEBI:3515
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefuroxime.yaml
    role: Curator-owned claim-specific primary literature additions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Preservation of imported database provenance during regeneration
  acceptance_checks:
  - Qualify the 1976 experimental material as cefuroxime sodium and do not silently
    import its numerical values as isolated neutral-acid measurements.
  - Represent PBP competition as the measured membrane assay, not Kd; distinguish
    individual PBP and bacterial systems from host complement or macrophage effects.
  - Keep resistance MIC shifts separate from purified-enzyme hydrolysis. Preserve
    inequalities, units, construct/vector controls, inducer/selection and source strain
    ambiguity. Do not infer SCO-1 alone explains the multi-enzyme clinical phenotype
    or that CAE-1 purification succeeded.
  - Obtain the uninspected exact LAP-2 and other limited-access functional passages
    before promoting those entries to primary evidence. Optional enrichment alone
    is not a correction requirement.
- action_id: A2
  description: If the FDA integration is refined, resolve the exact material of ANDA
    065048 products 003/004 before changing their chemical placement.
  finding_ids: []
  target_ids:
  - CHEBI:3515
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/fda_clinical_status.tsv
    role: Exact source product assertions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: Product ingredient, active-moiety and salt join policy
  acceptance_checks:
  - Find a product-number-specific label or official composition mapping for 003/004;
    distinguish neutral active moiety from sodium ingredient and do not infer product
    identity from an application-wide aggregate alone.
  - Retain the verified original approval date and source Prescription status, with
    currently_marketed understood as the source category rather than a stock-availability
    claim.
  - Only change the maintained join if direct product-specific evidence establishes
    a mismatch, then regenerate and rerun focused and applicable corpus gates.
limitations:
- 'Whole-record coverage is complete, but scientific completion is partial: all eleven
  adopted bibliography entries and fourteen resistance-linked records were checked,
  with access depths stated individually rather than implying every paper was read
  in full.'
- Selected original 1976 scanned pages and the 1986 PBP Methods/results/figures were
  inspected directly. Other animal tables and all remaining 1986 sections were not
  independently audited; no unsupported numeric extraction is asserted.
- ACC-4, SED-1, LAP-1 and both SCO-1 original texts were inspected for relevant methods,
  results and tables after ordinary PMC?page=1 retrieval succeeded. Genetic-context
  figures were not independently audited. EBR-5 and CAE-1 main-text XML were read;
  supplementary methods were not independently audited.
- LAP-2 lacks an indexed abstract; its full letter remains uninspected. CMY-136, YRC-1
  and MAB biochemical evidence is bounded to complete original abstracts, with companion
  genetic/host studies kept in their actual scope.
- Several original papers specify sodium salt or leave counterion unspecified. Neither
  establishes all reported endpoints for independently isolated neutral acid. The
  native record currently contains no numerical activity claim needing removal on
  that basis.
- DrugBank returned 403; MetaCyc resolved to a login page; Reaxys was not accessed.
  Public ChEBI attests those identifiers, but independent exact graph confirmation
  in those services remains incomplete. Patent description checks verify relevant
  document scope, not all legal claims or every experimental example.
- Current official FDA and GSRS rows were checked; exact 003/004 solution material
  remains unresolved because the inspected linked SPLs describe sodium powder vials.
  This does not establish a confirmed wrong-form join.
- Structured expression-source search was performed before web research. Its zero
  module hit and absent species coverage are not biological negative evidence. No
  transcriptomics dataset is inferred from targeted RT-qPCR.
- The supplemental brand check confirms Zinacef from an HPRA label and current product
  page. Biofuroksym manufacturer retrieval returned 403, and no exact Cefuril product
  was independently resolved from a primary official label; discovery snippets are
  not treated as proof for either name. The confirmed finding is therefore limited
  to Zinacef.
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
