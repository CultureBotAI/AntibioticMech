# Ebselen: two imported viral assay annotations require correction

- Review: 20261021T152057Z-ebselen-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:52:15Z
- Finished UTC: 2026-10-21T15:20:57Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The neutral ebselen identity, antibacterial and antifungal roles and bounded viral enzyme activity are supported. Two major source-level errors remain: the HCV 1.4 micromolar result is fluorescence polarization rather than EMSA, and the cited 80 nM coronavirus measurement belongs to tideglusib in the original figure and supporting table. The independent 670 nM and no-DTT 30 nM ebselen measurements remain supported at their stated experimental scope.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 389; one exact record. Original 13 input hashes preserved within 23 expanded inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:77543 | data/antibiotics/antibacterial/ebselen.yaml | generated | ebselen |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Structured-source catalog before protein research | passed | False | CHEBI:77543 | The live catalog has no matching viral dataset. Initial sandbox DNS failed; the same escalated public catalog read succeeded before open research. |
| Focused chemistry verification | passed | False | CHEBI:77543 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:77543 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:77543 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:77543 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:77543 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:77543 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:77543 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:77543 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:77543 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:77543 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:77543 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:77543 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral ebselen identity

identity: supported. Targets: CHEBI:77543.

All native graph encodings, formula, masses and source mint agree. Current ChEBI, ChemSpider, PubChem and DrugBank support the same structure. No salt, stereoisomer or selenium mass defect was established.

### Chemical groundings and broader parent

grounding: supported. Targets: CHEBI:77543.

CAS, ChemSpider, DrugBank, current ChEBI and the broader benzoselenazole parent resolve at the correct scope. LINCS and Reaxys remain explicitly unverified legacy links, not confirmed false equivalences.

### Definition and code-name synonyms

evidence: supported. Targets: CHEBI:77543.

The benzoselenazole substitution pattern is chemically correct and original GPx-like activity supports the definition. Investigational code names are not automatically mislabeled commercial brands. All adopted source leads have explicit reading-depth dispositions.

### Antibacterial filing, fungal/viral roles and mode

scope: supported. Targets: CHEBI:77543.

Exact ebselen has original bacterial and fungal growth activity and qualified viral protease inhibition. The native mode notes already separate antiviral mechanism from antibacterial filing. HCV NS3 helicase inhibition is not NS3 protease inhibition, and the viral mode is not presented as the established antibacterial mechanism.

### Four quantitative viral associations

evidence: concern. Targets: CHEBI:77543.

The 1400 nM value is supported but its EMSA method assignment is wrong. The 80 nM source assignment is contradicted by original compound-specific figures and published SI. The 670 nM and no-DTT 30 nM ebselen values are supported as enzyme inhibition endpoints, with thiol sensitivity and cell-assay limits retained.

### Imported viral protein examples

grounding: supported. Targets: CHEBI:77543.

Both accessions resolve with the stated taxon and reviewed/unreviewed status. Actual assays used the NS3 helicase domain or Mpro, not every function of the named polyproteins. The exact HCV example-to-Con1 sequence mapping remains unverified; no unsupported specific sequence-equivalence conclusion is made.

### Optional activity_spectrum and antibacterial mechanism

completeness: unknown. Targets: CHEBI:77543.

Primary broth MIC and fungal experiments offer bounded enrichment leads. Optional absence is not a schema defect. Bacterial precursor-incorporation results do not yet justify adding an exact ribosomal/protein target or importing viral enzyme IC50s into antibacterial MIC rows.

### Resistance, clinical products, producer, causal graph and datasets

scope: not_applicable. Targets: CHEBI:77543.

No native assertion occurs in these domains. Host enzyme inhibition, prospective therapy, combination-cell results, comparator resistance and the incidental cryptic UUID hit do not create such assertions.

### Actual owners, source history and status

provenance: supported. Targets: CHEBI:77543.

The native fields faithfully reproduce the inspected sources and seven seed/reseed events, but source faithfulness does not resolve the two scientific errors. Original thirteen hashes are preserved within twenty-three captured inputs. Scientific status remains SEEDED.

### Focused native gates

schema: supported. Targets: CHEBI:77543.

Chemistry, schema and strict checks pass; these deterministic gates do not test the original figure-to-assay or compound-to-value mapping that produced the findings.

## Findings

### F1: The HCV IC50 is attached to the wrong experimental method

major / open / confirmed; issue key: ebselen-hcv-ic50-fp-mislabeled-emsa.

Original Figure 4 assigns ebselen IC50 1.4 ±0.2 micromolar to fluorescence-polarization NS3h–DNA displacement. The native EMSA name and detailed EMSA protocol describe a separate qualitative confirmation, copied from current BindingDB. Preserve the supported numerical value, but correct its method and condition mapping through the maintained source path.

### F2: The cited 80 nM result belongs to tideglusib

major / open / confirmed; issue key: ebselen-80nm-mpro-value-belongs-to-tideglusib.

BindingDB reactant902201 and the native record assign 80 nM to ebselen. Actual original preprint Figure 3, the published Figure 3 and exact published Table S3 compound rows assign 0.08 micromolar to tideglusib and 0.03 micromolar to ebselen. Adjudicate or retract/reassign this source measurement while preserving the separate supported 30 nM and 670 nM ebselen data and their assay qualifications.

## Recommended Actions And Acceptance Checks

### A1

Correct the HCV measurement method and its experimental-condition mapping.

- Map the retained 1.4 micromolar value to original Figure 4 fluorescence polarization and the corresponding FP Methods.
- Keep qualitative EMSA evidence separate; do not retain EMSA-specific reagent concentrations or incubation times as the quantitative FP protocol.
- Preserve NS3 helicase-domain, thiol-sensitivity and assay endpoint qualifications without labeling this NS3 protease inhibition.
- Regenerate through maintained sources and run focused schema/strict, provenance and corpus reproduction checks.

### A2

Adjudicate the erroneous 80 nM compound assignment in the maintained BindingDB import.

- Resolve original preprint Figure 3 and published SI material identifiers: ebselen SPE_K29359156/CID3194 is 0.03 micromolar, while tideglusib DOM_SIM_153/CID11313622 is 0.08 micromolar.
- Remove or reassign the unsupported ebselen 80 nM assertion with an auditable source correction; do not silently discard the source provenance.
- Retain supported ebselen 30 nM without-DTT and independent 670 nM results at their original assay conditions, without treating redox sensitivity as universal inactivity.
- Verify numerical units, material mapping, duplicate handling and downstream regeneration; repeat focused and required provenance gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/ebselen.yaml; Entire native record: identity, nine synonyms, parent, roles, all four target measurements, both protein examples and seven history events | supports | The SEEDED/EXACT record represents neutral ebselen. It contains two imported viral target associations, explicitly distinguishes the antiviral mode from antibacterial filing, and has no activity_spectrum, resistance, clinical-product, producer, causal-graph or dataset assertion. |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/bindingdb_target_measurements.tsv; Exact ChEBI row 1961; exact ebselen BindingDB rows 166–174; extractor and seeder filtering | supports | The ChEBI source owns identity, roles and ten adopted literature leads. Nine exact ebselen raw target rows include review/cell endpoints filtered from the native quantitative target block; four retained rows reproduce BindingDB reactant sets 251939, 840120, 902201 and 902202. The two errors identified below are already present in current BindingDB, rather than introduced by numerical conversion in the seeder. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/77543/; Current complete CHEBI:77543 response and role/parent relations | supports | Current authority agrees with the neutral graph, key, formula, masses, synonyms and source bibliography. Antibacterial, antifungal and anticoronaviral roles and the SARS coronavirus main-proteinase inhibitor role are separately asserted; the additional broader roles in the response do not require changing the configured native role selection. |
| parent | https://www.ebi.ac.uk/chebi/backend/api/public/compound/78151/; Current CHEBI:78151 benzoselenazole class | supports | The parent denotes the benzoselenazole structural class, not an asserted exact chemical equivalent. |
| chemistry | RDKit 2026.03.5 via batch 019 interpreter against batch 039 cwd; 389-chemistry.json; native SMILES and InChI parsed independently | supports | Both native encodings reproduce DYEFUKCXAQOFHX-UHFFFAOYSA-N, C13H9NOSe, charge zero, average mass 274.181 and exact mass 274.984935208. The selenium isotope distribution permits exact mass above average mass; this is not an inconsistency. The source mint also reproduces. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/ebselen/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON; Current PubChem name resolution to CID3194 | supports | CID3194 independently matches the exact neutral ebselen graph and key. It is used here to map primary material IDs, not to introduce an unasserted native cross-reference. |
| chemspider | https://www.chemspider.com/Chemical-Structure.3082.html; Official ChemSpider3082 structured identity, InChIKey and CAS | supports | The native ChemSpider link resolves to the same neutral structure and CAS60940-34-3. |
| drugbank | https://go.drugbank.com/drugs/DB12610; Official public text retrieved through web fallback after direct HTTP 403 | supports | DrugBank12610 identifies ebselen, the matching formula, structure and CAS, and investigational status. DR3305 and SPI1005 are identified as code names. No approved product or brand identity is inferred. |
| legacy-links | https://lincs.hms.harvard.edu/db/sm/2644/; https://www.reaxys.com/; Attempted exact legacy authority links; failures recorded in 388389-fetch2.json | context_only | The official LINCS2644 endpoint returned HTTP 500 and Reaxys retrieval returned HTTP 403. Their exact chemical mapping was not independently verified. Other matching authorities are not treated as substitutes for verifying these two asserted links. |
| document | https://en.wikipedia.org/wiki/Ebselen; Ebselen article identity and bibliography only | context_only | The native document link resolves to the named compound. It is a document reference and discovery context, not the primary basis for the biological findings. |
| adapter | kg-microbe-sources imodulondb datasets; 389-adapter-catalog.json; successful escalated catalog retrieval before open protein research | context_only | The available catalog has no HCV, SARS-CoV-2 or human dataset matching the native viral targets. The adapter is therefore not applicable; catalog absence is not biological negative evidence. The initial sandbox DNS failure was resolved by the same public read with network access. |
| gpx-original | https://doi.org/10.1016/0006-2952(84)90083-2; PMID6487370 original abstract | supports | The original identifies PZ51 by the exact ebselen chemical name and reports glutathione-peroxidase-like activity in vitro, with the sulfur analogue as comparator. This supports the native GPx-mimic definition; rat microsomal antioxidant effects are not a bacterial target claim. |
| adopted-dispositions | PMID:11060699; PMID:14588151; PMID:16239596; PMID:16962325; PMID:17030476; PMID:17976864; PMID:19747949; PMID:21822642; PMID:22181350; PMC:PMC8009100; All ten adopted leads: original abstracts for nine PMIDs; specific full-source reading described separately; DOI/reading-depth ledger | partial | Every adopted lead was resolved. Reviews 11060699, 14588151 and 21822642 provide historical clinical/redox/MurA discovery context. Originals 16239596 and 16962325 do not name the exact ebselen experiment in their abstracts; reagent attribution remains unverified. PMID17030476 concerns host rat cochlear protection, and 17976864 concerns novel diaryl-isoselenazole analogues. None is transferred into an exact bacterial target or current approval claim. Three accessible originals are scoped below. |
| adopted-abstracts | https://www.ebi.ac.uk/europepmc/webservices/rest/search; 389-core.json original source abstracts and bibliographic metadata | partial | The original metadata and abstract texts corroborate the adopted DOI/PMID ledger. This is abstract-depth evidence except where a separate full text or figure is explicitly identified; it is not a claim that every adopted full paper was read. |
| tryr | https://doi.org/10.1016/j.molbiopara.2009.09.002; PMID19747949; full Table 3 and adjacent ebselen Results/Methods scope | context_only | The original compares T. brucei and T. cruzi trypanothione reductase. Its ebselen enzyme inhibition measurements are original; the listed T. brucei cell EC50 is attributed to earlier work. These are protozoal enzyme/cell contexts, not bacterial or viral-protease evidence. |
| apobec | https://doi.org/10.1021/cb200440y; PMID22181350; full Table 1 and compound-specific Results | context_only | Table 1 identifies MN18 as ebselen/CID3194, with human APOBEC3G inhibition. Detailed C321/catechol structural experiments concern other compounds and cannot be assigned to ebselen. This host-enzyme study does not establish antibacterial action. |
| nsp13-nsp14 | https://doi.org/10.1021/acsptsci.1c00022; PMID33855277/PMC8009100; full ebselen Results/Methods on nsp13, nsp14, zinc release and Vero E6 combination | context_only | Sigma ebselen was tested against SARS-CoV-2 nsp13 ATPase and nsp14 exonuclease and in remdesivir combination experiments. These independent viral contexts do not establish that every cellular effect derives from Mpro, or that combination effects are ebselen-only efficacy. Proposed resistance barriers are not measured resistance determinants. |
| hcv-original | https://doi.org/10.1021/cb500512z; PMID25126694/PMC4201343; NS3h material, FP, EMSA, thiol and protease Results/Methods; actual Figures1/4 inspected | supports | The original uses Sigma E3520 ebselen/CID3194 with Con1 genotype1b NS3 helicase domain. Figure 4 reports 1.4 ±0.2 micromolar inhibition of NS3h–DNA interaction in fluorescence polarization. EMSA is a separate qualitative confirmation. Added thiols at 50 micromolar abolish inhibition; the paper distinguishes reversible lower-dose inhibition from extensive covalent modification at high exposure. It does not demonstrate inhibition of NS3 protease at 100 micromolar. |
| hcv-figure4 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2153/4201343/f76dd66aed03/cb-2014-00512z_0004.jpg; Actual original Figure 4 table, directly viewed | refutes | The ebselen row explicitly assigns IC50 1.4 ±0.2 micromolar to the FP binding screen. Cell replicon and cytotoxicity columns are separate; neither is a binding constant or direct evidence of clinical antiviral efficacy. |
| hcv-figure1 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2153/4201343/d64aa4369a00/cb-2014-00512z_0001.jpg; Actual original Figure 1, directly viewed; panel E versus quantitative FP panels | refutes | The EMSA gel is an orthogonal experiment. The native 20 nM Cy5-dT15/200 nM NS3h protocol and two five-minute incubations belong to that experiment and must not be attached to the Figure 4 FP IC50 as if they generated it. |
| bdb-hcv | https://www.bindingdb.org/rwd/jsp/dbsearch/Summary_ki.jsp?entryid=6323&amp;reactant_set_id=251939; Current exact reactant set251939, entry6323 assay1 | partial | Current BindingDB repeats 1400 ±200 nM and labels the assay EMSA. The native record faithfully inherits this source error. The quantitative value is supported, while the method/protocol linkage is contradicted by the original. Initial incorrectly parameterized search pages returned an unrelated default result and were excluded from this comparison. |
| mpro2020 | https://doi.org/10.1038/s41586-020-2223-y; PMID32272481; complete ebselen screening Results and FRET/material Methods | supports | Purified SARS-CoV-2 Mpro with native termini was assayed with 0.2 micromolar enzyme and 20 micromolar FRET substrate across an eleven-concentration series in triplicate. Ebselen IC50 0.67 micromolar supports the native 670 nM datum. The reported N3 crystal structure is not an ebselen crystal structure; partial cysteine modification and cell antiviral activity are separately bounded observations. |
| bdb670 | https://www.bindingdb.org/rwd/jsp/dbsearch/Summary_ki.jsp?entryid=8774&amp;reactant_set_id=840120; Exact current reactant set840120, entry8774 assay1 | supports | The current 670 nM measurement and cited original match the native quantitative entry. The retained text describes an enzymatic activity assay, not a measured dissociation constant. |
| preprint | https://doi.org/10.1101/2020.12.16.422677; Original version1 full text; FRET profiling, DTT comparison and compound-specific Figure 3 | supports | The original preprint distinguishes no-DTT FRET profiling from reducing-agent controls and cell assays. Its actual Figure 3 was inspected: tideglusib is 0.08 micromolar and ebselen is 0.03 micromolar. The 60-minute preincubation and 15-minute substrate endpoint are method-specific. X-ray work in this study concerns myricetin; a generic assay description mentioning X-ray is not ebselen binding-site proof. |
| preprint-figure | https://www.biorxiv.org/content/biorxiv/early/2020/12/16/2020.12.16.422677/F4.medium.gif; Actual original Figure 3 table, directly viewed; labels and IC50 columns | refutes | The original figure assigns 0.08 micromolar to tideglusib and 0.03 micromolar to ebselen. Larger-image and supplementary-table expansion requests returned HTTP 429; the accessible original figure and full text were not replaced by an inferred database mapping. |
| published-figure | https://doi.org/10.1021/acsptsci.0c00216; Published counterpart PMID35287429; actual high-resolution Figure 3, directly viewed | refutes | The published Figure 3 independently preserves the same compound/value mapping: tideglusib 0.08 micromolar and ebselen 0.03 micromolar. This agrees with the original preprint figure rather than the 80 nM ebselen assignment in BindingDB. |
| published-si | https://ndownloader.figshare.com/files/26786317; Official ACS supporting workbook 032-pt0c00216_si_002.xlsx; Table S3 HP rows98 and71, HC material SMILES; independently reread as ZIP XML | refutes | The ebselen material SPE_K29359156/CID3194 has the exact neutral SMILES. HP row 98 gives 0.03 micromolar without DTT, DTT-sensitive classification and no reported plus-DTT IC50. Tideglusib DOM_SIM_153/CID11313622 is a different structure and HP row 71 gives 0.08 micromolar. These explicit material mappings corroborate the figure-level assignment. Published SI is identified as such, not presented as an independently downloaded preprint supplement. |
| bdb80 | https://www.bindingdb.org/rwd/jsp/dbsearch/Summary_ki.jsp?entryid=9114&amp;ki_result_id=904471&amp;reactant_set_id=902201; Exact current reactant set902201, entry9114 assay1, monomer34233 | refutes | Current BindingDB assigns 80 nM to ebselen monomer34233. This source assignment conflicts with both original Figure 3 and the exact compound row in the published SI. It requires source-level adjudication rather than treating a faithfully imported number as independently verified. |
| bdb30 | https://www.bindingdb.org/rwd/jsp/dbsearch/Summary_ki.jsp?entryid=9114&amp;ki_result_id=904472&amp;reactant_set_id=902202; Exact current reactant set902202, entry9114 assay1, monomer34233 | supports | The separate 30 nM ebselen entry matches the original figure and SI. The native assay explicitly states without DTT. Loss of inhibition with DTT qualifies the assay; it does not justify discarding the measured no-DTT result or declaring the compound universally inactive. |
| uniprot-hcv | https://rest.uniprot.org/uniprotkb/A3EZJ3.json; Current UniProtA3EZJ3 entry type, organism and sequence metadata | partial | The accession resolves as an unreviewed HCV polyprotein/NS3 fragment and matches the native status/taxon. The primary Con1 construct and this imported chain example were not independently aligned residue by residue. The database chain example is not proof that a full polyprotein was experimentally assayed. |
| uniprot-mpro | https://rest.uniprot.org/uniprotkb/P0DTD1.json; Current reviewed UniProtP0DTD1 polyprotein and nsp5 annotation | supports | The reviewed SARS-CoV-2 polyprotein accession and taxon resolve, and include the Mpro/nsp5 protein tested in the papers. Native MEASURED_TARGET_ASSOCIATION is narrower than a claim that every viral polyprotein activity is inhibited. |
| antibacterial | https://doi.org/10.1038/srep11596; PMID26111644/PMC4481386; material, broth-microdilution Methods, Tables1/2 and macromolecular-incorporation Results | supports | Adipogen ebselen was tested by broth microdilution in Mueller-Hinton broth at 37 C for at least 16 hours, in triplicate across at least two independent experiments. Table 2 includes S. aureus USA300 MIC 0.125 micrograms/mL and other MRSA strain values. Radioprecursor incorporation in S. aureus ATCC29213 supports inhibition of protein synthesis at the tested exposure, but does not identify a ribosomal binding site or a specific bacterial protein target. Resistance to comparator antibiotics is not resistance to ebselen. |
| antifungal | https://doi.org/10.1128/AAC.01084-18; PMID30104269/PMC6153848; primary screen, pharmaceutical-grade follow-up, fungal growth/biofilm Methods and ebselen Results | supports | The original Candida auris study screened a library and followed up with AdipoGen ebselen. Planktonic experiments used buffered RPMI, a defined inoculum and 35 C incubation; biofilm endpoints are separate. The exact compound inhibits fungal growth under these conditions, supporting the antifungal role without treating screen concentration as a clinical susceptibility breakpoint. |
| search | Ignored-inclusive local search and bounded Europe PMC primary discovery; 388389-all-local-paths.txt; 389-antibacterial-discovery.json | context_only | Search included the exact label, identifier, slug and structure key in hidden and ignored data, curation, source, report and review files. The cryptic_activity.tsv hit is an incidental UUID substring in a moxifloxacin row, not ebselen dataset membership. No exact curator or decision owner row was established. Primary discovery was used to select the original antibacterial/antifungal sources, not to imply exhaustive reading of every search hit. |
| gates | Focused chemistry, schema and strict execution; 389-focused-results.json | supports | All actual focused checks pass. Native validators ran in batch039; independent RDKit used the existing batch019 interpreter against batch039 cwd. |

## Limits And Additional Notes

- All ten adopted literature leads were resolved at the stated depths. Original abstracts alone were read for the two inaccessible exact-reagent questions and the other explicitly abstract-only leads; no claim of full-text verification is made for them. Accessible HCV/Mpro papers were read at material, relevant experimental Results/Methods and actual key figures; unrelated analogue procedures and raw spectra were not independently reprocessed.
- LINCS LSM-2644 returned HTTP 500 and Reaxys returned HTTP 403. Their exact chemical mappings remain unverified. DrugBank direct retrieval failed 403, but official public text was inspected through the web fallback.
- The original preprint full text and small Figure 3 were accessible; larger figure and expanded supplement requests failed 429. The separately labeled official published SI was independently inspected, with its hash retained. Failed guessed-image and incorrectly parameterized BindingDB pages were excluded as evidence.
- Current UniProt statuses and taxa were verified, but the imported HCV example sequence was not independently aligned to the original Con1 experimental construct. Database chain context must not replace exact primary construct qualification.
- The antibacterial and antifungal originals were read at exact reagent, growth method, principal activity tables/results and the relevant mechanism experiments. This review does not exhaust every analogue, animal endpoint or discovery-search hit, establish clinical susceptibility breakpoints, or infer a unique bacterial protein target.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native, source, status or history field was edited. Optional links, tags and notes were checked against this exact ebselen review. The initial thirteen hashes were retained, and all expanded captured inputs were rechecked unchanged before draft output.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T152057Z-ebselen-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Ebselen: two imported viral assay annotations require correction'
started_at: '2026-10-21T14:52:15Z'
finished_at: '2026-10-21T15:20:57Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independent whole-record review after input capture, exact ChEBI
    and BindingDB row inspection, live authority comparison, independent chemistry,
    and original primary text, actual figure and supplementary-table comparisons.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'The neutral ebselen identity, antibacterial and antifungal roles and bounded
  viral enzyme activity are supported. Two major source-level errors remain: the HCV
  1.4 micromolar result is fluorescence polarization rather than EMSA, and the cited
  80 nM coronavirus measurement belongs to tideglusib in the original figure and supporting
  table. The independent 670 nM and no-DTT 30 nM ebselen measurements remain supported
  at their stated experimental scope.'
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
  - path: data/antibiotics/antibacterial/ebselen.yaml
    sha256: 0b9b8a9effc290726092b48186d6c28eb02a73ec688807f9c92466178b5053f2
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
  - path: data/raw/bindingdb_target_measurements.tsv
    sha256: faccfe5634f467801aeb256e6560af09d193cdb53bdbf29dea195c9c0488c480
    role: context
  - path: scripts/extract_bindingdb_targets.py
    sha256: 9914a61b93326808b9800f3680dc935af2abcfa1e9925d6c3dd39180dbc78a2d
    role: context
  - path: data/raw/cryptic_activity.tsv
    sha256: fa2fe5e5258328f10f9fe5724e4b74f354a98f5355bac68108ab28ffb17c7987
    role: context
targets:
- target_id: CHEBI:77543
  path: data/antibiotics/antibacterial/ebselen.yaml
  label: ebselen
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
    path: data/raw/bindingdb_target_measurements.tsv
    role: Imported quantitative viral target assays
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_bindingdb_targets.py
    role: BindingDB measurement extraction
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 389; one exact record. Original 13 input hashes preserved
    within 23 expanded inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:77543
checks:
- check_id: structured-adapter
  name: Structured-source catalog before protein research
  status: passed
  required: false
  target_ids:
  - CHEBI:77543
  evidence_ids:
  - adapter
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
  exit_code: 0
  expected_exit_code: 0
  summary: The live catalog has no matching viral dataset. Initial sandbox DNS failed;
    the same escalated public catalog read succeeded before open research.
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:77543
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/388389-focused.py
    (cwd /private/tmp/antibioticmech-record-reviews-039)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:77543
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/ebselen.yaml (cwd /private/tmp/antibioticmech-record-reviews-039)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:77543
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/ebselen.yaml --out /private/tmp/am-review-session/389-strict.tsv
    (cwd /private/tmp/antibioticmech-record-reviews-039)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:77543
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
  - CHEBI:77543
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
  - CHEBI:77543
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
  - CHEBI:77543
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
  - CHEBI:77543
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
  - CHEBI:77543
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
  - CHEBI:77543
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
  - CHEBI:77543
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
  - CHEBI:77543
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/ebselen.yaml
  locator: 'Entire native record: identity, nine synonyms, parent, roles, all four
    target measurements, both protein examples and seven history events'
  accessed_at: '2026-10-21T15:08:43Z'
  support: supports
  summary: The SEEDED/EXACT record represents neutral ebselen. It contains two imported
    viral target associations, explicitly distinguishes the antiviral mode from antibacterial
    filing, and has no activity_spectrum, resistance, clinical-product, producer,
    causal-graph or dataset assertion.
  snapshot_sha256: ce80a9a4a9b05a9760f5202550b62ad07c2402b7413a7100d8989b4041ac30ab
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/bindingdb_target_measurements.tsv
  locator: Exact ChEBI row 1961; exact ebselen BindingDB rows 166–174; extractor and
    seeder filtering
  accessed_at: '2026-10-21T15:08:43Z'
  support: supports
  summary: The ChEBI source owns identity, roles and ten adopted literature leads.
    Nine exact ebselen raw target rows include review/cell endpoints filtered from
    the native quantitative target block; four retained rows reproduce BindingDB reactant
    sets 251939, 840120, 902201 and 902202. The two errors identified below are already
    present in current BindingDB, rather than introduced by numerical conversion in
    the seeder.
  snapshot_sha256: ce80a9a4a9b05a9760f5202550b62ad07c2402b7413a7100d8989b4041ac30ab
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/77543/
  locator: Current complete CHEBI:77543 response and role/parent relations
  accessed_at: '2026-10-21T14:57:52.434464Z'
  support: supports
  summary: Current authority agrees with the neutral graph, key, formula, masses,
    synonyms and source bibliography. Antibacterial, antifungal and anticoronaviral
    roles and the SARS coronavirus main-proteinase inhibitor role are separately asserted;
    the additional broader roles in the response do not require changing the configured
    native role selection.
  snapshot_sha256: 6d25835e4eaf7a5962daac08c38fce31d0156e12b57a856ab75a90a16b3cc2c0
- evidence_id: parent
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/78151/
  locator: Current CHEBI:78151 benzoselenazole class
  accessed_at: '2026-10-21T14:57:52.434999Z'
  support: supports
  summary: The parent denotes the benzoselenazole structural class, not an asserted
    exact chemical equivalent.
  snapshot_sha256: 948732c19f1bd677a6e25c2e1d47dd8436dcba1298ef87a2f6ec03c50dcb65c3
- evidence_id: chemistry
  kind: validation
  reference: RDKit 2026.03.5 via batch 019 interpreter against batch 039 cwd
  locator: 389-chemistry.json; native SMILES and InChI parsed independently
  accessed_at: '2026-10-21T15:08:43Z'
  support: supports
  summary: Both native encodings reproduce DYEFUKCXAQOFHX-UHFFFAOYSA-N, C13H9NOSe,
    charge zero, average mass 274.181 and exact mass 274.984935208. The selenium isotope
    distribution permits exact mass above average mass; this is not an inconsistency.
    The source mint also reproduces.
  snapshot_sha256: 8613aef8d1cab916e24d0124a2442ad0addefe2b7bfcf30150c048eddddb7367
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/ebselen/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON
  locator: Current PubChem name resolution to CID3194
  accessed_at: '2026-10-21T14:57:53.317943Z'
  support: supports
  summary: CID3194 independently matches the exact neutral ebselen graph and key.
    It is used here to map primary material IDs, not to introduce an unasserted native
    cross-reference.
  snapshot_sha256: 0a868156206f3d9fc276176f9e622e0919581cce0d0d5fb050a0f6d1c7bd7542
- evidence_id: chemspider
  kind: authority
  reference: https://www.chemspider.com/Chemical-Structure.3082.html
  locator: Official ChemSpider3082 structured identity, InChIKey and CAS
  accessed_at: '2026-10-21T14:58:11.622014Z'
  support: supports
  summary: The native ChemSpider link resolves to the same neutral structure and CAS60940-34-3.
  snapshot_sha256: bc9468488c8daafccbc2feb7d1408082ba33f44c988a3808746da8637ead0667
- evidence_id: drugbank
  kind: authority
  reference: https://go.drugbank.com/drugs/DB12610
  locator: Official public text retrieved through web fallback after direct HTTP 403
  accessed_at: '2026-10-21T15:08:43Z'
  support: supports
  summary: DrugBank12610 identifies ebselen, the matching formula, structure and CAS,
    and investigational status. DR3305 and SPI1005 are identified as code names. No
    approved product or brand identity is inferred.
  snapshot_sha256: a34189182bce13cce04feae508a5ca6176bf1e54e8f5fa5ded0a841d4e3fdb78
- evidence_id: legacy-links
  kind: authority
  reference: https://lincs.hms.harvard.edu/db/sm/2644/; https://www.reaxys.com/
  locator: Attempted exact legacy authority links; failures recorded in 388389-fetch2.json
  accessed_at: '2026-10-21T15:08:43Z'
  support: context_only
  summary: The official LINCS2644 endpoint returned HTTP 500 and Reaxys retrieval
    returned HTTP 403. Their exact chemical mapping was not independently verified.
    Other matching authorities are not treated as substitutes for verifying these
    two asserted links.
  snapshot_sha256: 3e09793dd0f43100c06d816606d78d1694c5d422a5165084e023785467667e3e
- evidence_id: document
  kind: database
  reference: https://en.wikipedia.org/wiki/Ebselen
  locator: Ebselen article identity and bibliography only
  accessed_at: '2026-10-21T15:01:30.279823Z'
  support: context_only
  summary: The native document link resolves to the named compound. It is a document
    reference and discovery context, not the primary basis for the biological findings.
  snapshot_sha256: 970e98d887f410a00297a5199a78c10c8b0cb6c04f73fc0efb36af9e5b789823
- evidence_id: adapter
  kind: search
  reference: kg-microbe-sources imodulondb datasets
  locator: 389-adapter-catalog.json; successful escalated catalog retrieval before
    open protein research
  accessed_at: '2026-10-21T15:08:43Z'
  support: context_only
  summary: The available catalog has no HCV, SARS-CoV-2 or human dataset matching
    the native viral targets. The adapter is therefore not applicable; catalog absence
    is not biological negative evidence. The initial sandbox DNS failure was resolved
    by the same public read with network access.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  search_scope: 2026-10-21; live iModulonDB datasets catalog, checked for HCV, SARS-CoV-2
    and human organism coverage before open protein research.
- evidence_id: gpx-original
  kind: primary_source
  reference: https://doi.org/10.1016/0006-2952(84)90083-2
  locator: PMID6487370 original abstract
  accessed_at: '2026-10-21T15:01:30.288786Z'
  support: supports
  summary: The original identifies PZ51 by the exact ebselen chemical name and reports
    glutathione-peroxidase-like activity in vitro, with the sulfur analogue as comparator.
    This supports the native GPx-mimic definition; rat microsomal antioxidant effects
    are not a bacterial target claim.
  snapshot_sha256: 16d975612156881419f430e49bd101da6a10a56ae633c7ccd56930dc1aedf953
- evidence_id: adopted-dispositions
  kind: primary_source
  reference: PMID:11060699; PMID:14588151; PMID:16239596; PMID:16962325; PMID:17030476;
    PMID:17976864; PMID:19747949; PMID:21822642; PMID:22181350; PMC:PMC8009100
  locator: 'All ten adopted leads: original abstracts for nine PMIDs; specific full-source
    reading described separately; DOI/reading-depth ledger'
  accessed_at: '2026-10-21T15:08:43Z'
  support: partial
  summary: Every adopted lead was resolved. Reviews 11060699, 14588151 and 21822642
    provide historical clinical/redox/MurA discovery context. Originals 16239596 and
    16962325 do not name the exact ebselen experiment in their abstracts; reagent
    attribution remains unverified. PMID17030476 concerns host rat cochlear protection,
    and 17976864 concerns novel diaryl-isoselenazole analogues. None is transferred
    into an exact bacterial target or current approval claim. Three accessible originals
    are scoped below.
  snapshot_sha256: 2b9fa58392f3dcc04e17643776ed5ef9ae2d68e24782693439198e2d9d315672
- evidence_id: adopted-abstracts
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search
  locator: 389-core.json original source abstracts and bibliographic metadata
  accessed_at: '2026-10-21T14:57:53.269353Z'
  support: partial
  summary: The original metadata and abstract texts corroborate the adopted DOI/PMID
    ledger. This is abstract-depth evidence except where a separate full text or figure
    is explicitly identified; it is not a claim that every adopted full paper was
    read.
  snapshot_sha256: d524699aae274381431b6d279064a87c7dfac7639b2b52b1320e22b724a4cace
- evidence_id: tryr
  kind: primary_source
  reference: https://doi.org/10.1016/j.molbiopara.2009.09.002
  locator: PMID19747949; full Table 3 and adjacent ebselen Results/Methods scope
  accessed_at: '2026-10-21T15:00:50.662216Z'
  support: context_only
  summary: The original compares T. brucei and T. cruzi trypanothione reductase. Its
    ebselen enzyme inhibition measurements are original; the listed T. brucei cell
    EC50 is attributed to earlier work. These are protozoal enzyme/cell contexts,
    not bacterial or viral-protease evidence.
  snapshot_sha256: 1bf9354cbe9d5740cd3509626e68e2fcfa0fa28c1a7f5802a4f63ea6e83f0a80
- evidence_id: apobec
  kind: primary_source
  reference: https://doi.org/10.1021/cb200440y
  locator: PMID22181350; full Table 1 and compound-specific Results
  accessed_at: '2026-10-21T15:01:29.936535Z'
  support: context_only
  summary: Table 1 identifies MN18 as ebselen/CID3194, with human APOBEC3G inhibition.
    Detailed C321/catechol structural experiments concern other compounds and cannot
    be assigned to ebselen. This host-enzyme study does not establish antibacterial
    action.
  snapshot_sha256: a6d1e42e726860bd58869fc9381f10f555b16804191092ea159abf75037a8c9d
- evidence_id: nsp13-nsp14
  kind: primary_source
  reference: https://doi.org/10.1021/acsptsci.1c00022
  locator: PMID33855277/PMC8009100; full ebselen Results/Methods on nsp13, nsp14,
    zinc release and Vero E6 combination
  accessed_at: '2026-10-21T14:57:53.284339Z'
  support: context_only
  summary: Sigma ebselen was tested against SARS-CoV-2 nsp13 ATPase and nsp14 exonuclease
    and in remdesivir combination experiments. These independent viral contexts do
    not establish that every cellular effect derives from Mpro, or that combination
    effects are ebselen-only efficacy. Proposed resistance barriers are not measured
    resistance determinants.
  snapshot_sha256: 7aca1c891fdd80b5147da69eee2a6eee19d0710c339176e3b6fb958da5a3d75e
- evidence_id: hcv-original
  kind: primary_source
  reference: https://doi.org/10.1021/cb500512z
  locator: PMID25126694/PMC4201343; NS3h material, FP, EMSA, thiol and protease Results/Methods;
    actual Figures1/4 inspected
  accessed_at: '2026-10-21T14:58:10.981167Z'
  support: supports
  summary: The original uses Sigma E3520 ebselen/CID3194 with Con1 genotype1b NS3
    helicase domain. Figure 4 reports 1.4 ±0.2 micromolar inhibition of NS3h–DNA interaction
    in fluorescence polarization. EMSA is a separate qualitative confirmation. Added
    thiols at 50 micromolar abolish inhibition; the paper distinguishes reversible
    lower-dose inhibition from extensive covalent modification at high exposure. It
    does not demonstrate inhibition of NS3 protease at 100 micromolar.
  snapshot_sha256: a64ad5b464405de9415c91c25e6996c1e0bd0a56fed0e571ed865606784174f7
- evidence_id: hcv-figure4
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2153/4201343/f76dd66aed03/cb-2014-00512z_0004.jpg
  locator: Actual original Figure 4 table, directly viewed
  accessed_at: '2026-10-21T15:01:29.925046Z'
  support: refutes
  summary: The ebselen row explicitly assigns IC50 1.4 ±0.2 micromolar to the FP binding
    screen. Cell replicon and cytotoxicity columns are separate; neither is a binding
    constant or direct evidence of clinical antiviral efficacy.
  snapshot_sha256: 5ca8e9fb52cf1b008bb9dcf4aa758def0ff626228ab5aabd07d8a9d86254472a
- evidence_id: hcv-figure1
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2153/4201343/d64aa4369a00/cb-2014-00512z_0001.jpg
  locator: Actual original Figure 1, directly viewed; panel E versus quantitative
    FP panels
  accessed_at: '2026-10-21T15:01:29.928788Z'
  support: refutes
  summary: The EMSA gel is an orthogonal experiment. The native 20 nM Cy5-dT15/200
    nM NS3h protocol and two five-minute incubations belong to that experiment and
    must not be attached to the Figure 4 FP IC50 as if they generated it.
  snapshot_sha256: 5c8771e380160be1a42c8a37e8c8748f1ea5f57101b6bb8cf8694d18c5772353
- evidence_id: bdb-hcv
  kind: database
  reference: https://www.bindingdb.org/rwd/jsp/dbsearch/Summary_ki.jsp?entryid=6323&reactant_set_id=251939
  locator: Current exact reactant set251939, entry6323 assay1
  accessed_at: '2026-10-21T15:02:26.131484Z'
  support: partial
  summary: Current BindingDB repeats 1400 ±200 nM and labels the assay EMSA. The native
    record faithfully inherits this source error. The quantitative value is supported,
    while the method/protocol linkage is contradicted by the original. Initial incorrectly
    parameterized search pages returned an unrelated default result and were excluded
    from this comparison.
  snapshot_sha256: 04a85cd47fdf5995a65c2cb7bf1b549c3a20c00cf6ef3c7998b8bcee3844cdad
- evidence_id: mpro2020
  kind: primary_source
  reference: https://doi.org/10.1038/s41586-020-2223-y
  locator: PMID32272481; complete ebselen screening Results and FRET/material Methods
  accessed_at: '2026-10-21T14:58:10.984169Z'
  support: supports
  summary: Purified SARS-CoV-2 Mpro with native termini was assayed with 0.2 micromolar
    enzyme and 20 micromolar FRET substrate across an eleven-concentration series
    in triplicate. Ebselen IC50 0.67 micromolar supports the native 670 nM datum.
    The reported N3 crystal structure is not an ebselen crystal structure; partial
    cysteine modification and cell antiviral activity are separately bounded observations.
  snapshot_sha256: 11ff7f0c03631222fc87cc49b2c1cceb3ec10b061aa2fcf7011e9971c5a9bf27
- evidence_id: bdb670
  kind: database
  reference: https://www.bindingdb.org/rwd/jsp/dbsearch/Summary_ki.jsp?entryid=8774&reactant_set_id=840120
  locator: Exact current reactant set840120, entry8774 assay1
  accessed_at: '2026-10-21T15:02:26.212185Z'
  support: supports
  summary: The current 670 nM measurement and cited original match the native quantitative
    entry. The retained text describes an enzymatic activity assay, not a measured
    dissociation constant.
  snapshot_sha256: 2ca1e2662553df240ef53fe60e61d154e2f530ddf4bf55de344dbe4bc7e9aff7
- evidence_id: preprint
  kind: primary_source
  reference: https://doi.org/10.1101/2020.12.16.422677
  locator: Original version1 full text; FRET profiling, DTT comparison and compound-specific
    Figure 3
  accessed_at: '2026-10-21T15:01:29.939016Z'
  support: supports
  summary: 'The original preprint distinguishes no-DTT FRET profiling from reducing-agent
    controls and cell assays. Its actual Figure 3 was inspected: tideglusib is 0.08
    micromolar and ebselen is 0.03 micromolar. The 60-minute preincubation and 15-minute
    substrate endpoint are method-specific. X-ray work in this study concerns myricetin;
    a generic assay description mentioning X-ray is not ebselen binding-site proof.'
  snapshot_sha256: 9b4d3896718b93086d21e3ea9cd990cbc2a0f9a5d36205b757855609ec925541
- evidence_id: preprint-figure
  kind: primary_source
  reference: https://www.biorxiv.org/content/biorxiv/early/2020/12/16/2020.12.16.422677/F4.medium.gif
  locator: Actual original Figure 3 table, directly viewed; labels and IC50 columns
  accessed_at: '2026-10-21T15:02:47.164784Z'
  support: refutes
  summary: The original figure assigns 0.08 micromolar to tideglusib and 0.03 micromolar
    to ebselen. Larger-image and supplementary-table expansion requests returned HTTP
    429; the accessible original figure and full text were not replaced by an inferred
    database mapping.
  snapshot_sha256: 3791fb1d74b4fcc07a70537c2111f9697a29b9bfe07d42ffb3fc05a5f9f92753
- evidence_id: published-figure
  kind: primary_source
  reference: https://doi.org/10.1021/acsptsci.0c00216
  locator: Published counterpart PMID35287429; actual high-resolution Figure 3, directly
    viewed
  accessed_at: '2026-10-21T15:03:14.645898Z'
  support: refutes
  summary: 'The published Figure 3 independently preserves the same compound/value
    mapping: tideglusib 0.08 micromolar and ebselen 0.03 micromolar. This agrees with
    the original preprint figure rather than the 80 nM ebselen assignment in BindingDB.'
  snapshot_sha256: ec36beaf3a2c2c7d24409b831fd844ab76b2757acc29c699efec51cdab3b8af7
- evidence_id: published-si
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/26786317
  locator: Official ACS supporting workbook 032-pt0c00216_si_002.xlsx; Table S3 HP
    rows98 and71, HC material SMILES; independently reread as ZIP XML
  accessed_at: '2026-10-21T15:08:43Z'
  support: refutes
  summary: The ebselen material SPE_K29359156/CID3194 has the exact neutral SMILES.
    HP row 98 gives 0.03 micromolar without DTT, DTT-sensitive classification and
    no reported plus-DTT IC50. Tideglusib DOM_SIM_153/CID11313622 is a different structure
    and HP row 71 gives 0.08 micromolar. These explicit material mappings corroborate
    the figure-level assignment. Published SI is identified as such, not presented
    as an independently downloaded preprint supplement.
  snapshot_sha256: 173015ca26d387d7ad27d69adccc356d74be6ace3bd34ff302a08276dacdd78a
- evidence_id: bdb80
  kind: database
  reference: https://www.bindingdb.org/rwd/jsp/dbsearch/Summary_ki.jsp?entryid=9114&ki_result_id=904471&reactant_set_id=902201
  locator: Exact current reactant set902201, entry9114 assay1, monomer34233
  accessed_at: '2026-10-21T15:02:26.125243Z'
  support: refutes
  summary: Current BindingDB assigns 80 nM to ebselen monomer34233. This source assignment
    conflicts with both original Figure 3 and the exact compound row in the published
    SI. It requires source-level adjudication rather than treating a faithfully imported
    number as independently verified.
  snapshot_sha256: c05c140b713f2daacc1498ed7a20bc875617b2b7aa7e3143182f4d5fd216ac27
- evidence_id: bdb30
  kind: database
  reference: https://www.bindingdb.org/rwd/jsp/dbsearch/Summary_ki.jsp?entryid=9114&ki_result_id=904472&reactant_set_id=902202
  locator: Exact current reactant set902202, entry9114 assay1, monomer34233
  accessed_at: '2026-10-21T15:02:26.128915Z'
  support: supports
  summary: The separate 30 nM ebselen entry matches the original figure and SI. The
    native assay explicitly states without DTT. Loss of inhibition with DTT qualifies
    the assay; it does not justify discarding the measured no-DTT result or declaring
    the compound universally inactive.
  snapshot_sha256: bc50deefffff42452d9aed0522521ec86bf8acce12c57f0194385e36170c5840
- evidence_id: uniprot-hcv
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/A3EZJ3.json
  locator: Current UniProtA3EZJ3 entry type, organism and sequence metadata
  accessed_at: '2026-10-21T14:57:53.443001Z'
  support: partial
  summary: The accession resolves as an unreviewed HCV polyprotein/NS3 fragment and
    matches the native status/taxon. The primary Con1 construct and this imported
    chain example were not independently aligned residue by residue. The database
    chain example is not proof that a full polyprotein was experimentally assayed.
  snapshot_sha256: 07135f33cc75b5d3f1c6565881323286e18673fbf4eeedab264a591b2c503225
- evidence_id: uniprot-mpro
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0DTD1.json
  locator: Current reviewed UniProtP0DTD1 polyprotein and nsp5 annotation
  accessed_at: '2026-10-21T14:57:53.653615Z'
  support: supports
  summary: The reviewed SARS-CoV-2 polyprotein accession and taxon resolve, and include
    the Mpro/nsp5 protein tested in the papers. Native MEASURED_TARGET_ASSOCIATION
    is narrower than a claim that every viral polyprotein activity is inhibited.
  snapshot_sha256: 7366d4fea701dfccea0226cbe43850961d5192cad95d0e7644cc0c16dec7e642
- evidence_id: antibacterial
  kind: primary_source
  reference: https://doi.org/10.1038/srep11596
  locator: PMID26111644/PMC4481386; material, broth-microdilution Methods, Tables1/2
    and macromolecular-incorporation Results
  accessed_at: '2026-10-21T15:01:29.931794Z'
  support: supports
  summary: Adipogen ebselen was tested by broth microdilution in Mueller-Hinton broth
    at 37 C for at least 16 hours, in triplicate across at least two independent experiments.
    Table 2 includes S. aureus USA300 MIC 0.125 micrograms/mL and other MRSA strain
    values. Radioprecursor incorporation in S. aureus ATCC29213 supports inhibition
    of protein synthesis at the tested exposure, but does not identify a ribosomal
    binding site or a specific bacterial protein target. Resistance to comparator
    antibiotics is not resistance to ebselen.
  snapshot_sha256: 80a852c4bb5df097f345d26a17cc991ba5c6952b665f9548a77a6b907cd369c4
- evidence_id: antifungal
  kind: primary_source
  reference: https://doi.org/10.1128/AAC.01084-18
  locator: PMID30104269/PMC6153848; primary screen, pharmaceutical-grade follow-up,
    fungal growth/biofilm Methods and ebselen Results
  accessed_at: '2026-10-21T15:02:26.123026Z'
  support: supports
  summary: The original Candida auris study screened a library and followed up with
    AdipoGen ebselen. Planktonic experiments used buffered RPMI, a defined inoculum
    and 35 C incubation; biofilm endpoints are separate. The exact compound inhibits
    fungal growth under these conditions, supporting the antifungal role without treating
    screen concentration as a clinical susceptibility breakpoint.
  snapshot_sha256: 84865cdfe9f13326a170a775a8e87ac8238f84bdd3d27cffadffa47702ca485c
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local search and bounded Europe PMC primary discovery
  locator: 388389-all-local-paths.txt; 389-antibacterial-discovery.json
  accessed_at: '2026-10-21T14:58:10.987275Z'
  support: context_only
  summary: Search included the exact label, identifier, slug and structure key in
    hidden and ignored data, curation, source, report and review files. The cryptic_activity.tsv
    hit is an incidental UUID substring in a moxifloxacin row, not ebselen dataset
    membership. No exact curator or decision owner row was established. Primary discovery
    was used to select the original antibacterial/antifungal sources, not to imply
    exhaustive reading of every search hit.
  snapshot_sha256: 843e40cf3d68ebdb462a430cab99f33848b6e565e0f06bb9be948d6dd86ff248
  search_scope: 2026-10-21; rg --no-ignore --hidden across data,curation,conf,scripts,src,reports,reviews;
    Europe PMC exact adopted references and bounded ebselen antimicrobial discovery.
- evidence_id: gates
  kind: validation
  reference: Focused chemistry, schema and strict execution
  locator: 389-focused-results.json
  accessed_at: '2026-10-21T15:08:43Z'
  support: supports
  summary: All actual focused checks pass. Native validators ran in batch039; independent
    RDKit used the existing batch019 interpreter against batch039 cwd.
  snapshot_sha256: 32bbfe857a86826b232eb8aadb89201cd0706b51f3d0f2cdd9583c5773028f4d
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral ebselen identity
  outcome: supported
  summary: All native graph encodings, formula, masses and source mint agree. Current
    ChEBI, ChemSpider, PubChem and DrugBank support the same structure. No salt, stereoisomer
    or selenium mass defect was established.
  target_ids:
  - CHEBI:77543
  evidence_ids:
  - native
  - chebi
  - chemistry
  - chemspider
  - pubchem
  - drugbank
- assessment_id: grounding
  area: grounding
  topic: Chemical groundings and broader parent
  outcome: supported
  summary: CAS, ChemSpider, DrugBank, current ChEBI and the broader benzoselenazole
    parent resolve at the correct scope. LINCS and Reaxys remain explicitly unverified
    legacy links, not confirmed false equivalences.
  target_ids:
  - CHEBI:77543
  evidence_ids:
  - chebi
  - parent
  - chemspider
  - drugbank
  - legacy-links
- assessment_id: definition
  area: evidence
  topic: Definition and code-name synonyms
  outcome: supported
  summary: The benzoselenazole substitution pattern is chemically correct and original
    GPx-like activity supports the definition. Investigational code names are not
    automatically mislabeled commercial brands. All adopted source leads have explicit
    reading-depth dispositions.
  target_ids:
  - CHEBI:77543
  evidence_ids:
  - gpx-original
  - chemistry
  - drugbank
  - adopted-dispositions
  - adopted-abstracts
- assessment_id: classification
  area: scope
  topic: Antibacterial filing, fungal/viral roles and mode
  outcome: supported
  summary: Exact ebselen has original bacterial and fungal growth activity and qualified
    viral protease inhibition. The native mode notes already separate antiviral mechanism
    from antibacterial filing. HCV NS3 helicase inhibition is not NS3 protease inhibition,
    and the viral mode is not presented as the established antibacterial mechanism.
  target_ids:
  - CHEBI:77543
  evidence_ids:
  - native
  - antibacterial
  - antifungal
  - mpro2020
  - preprint
  - hcv-original
- assessment_id: targets
  area: evidence
  topic: Four quantitative viral associations
  outcome: concern
  summary: The 1400 nM value is supported but its EMSA method assignment is wrong.
    The 80 nM source assignment is contradicted by original compound-specific figures
    and published SI. The 670 nM and no-DTT 30 nM ebselen values are supported as
    enzyme inhibition endpoints, with thiol sensitivity and cell-assay limits retained.
  target_ids:
  - CHEBI:77543
  evidence_ids:
  - hcv-original
  - hcv-figure4
  - hcv-figure1
  - bdb-hcv
  - mpro2020
  - bdb670
  - preprint-figure
  - published-si
  - bdb80
  - bdb30
- assessment_id: proteins
  area: grounding
  topic: Imported viral protein examples
  outcome: supported
  summary: Both accessions resolve with the stated taxon and reviewed/unreviewed status.
    Actual assays used the NS3 helicase domain or Mpro, not every function of the
    named polyproteins. The exact HCV example-to-Con1 sequence mapping remains unverified;
    no unsupported specific sequence-equivalence conclusion is made.
  target_ids:
  - CHEBI:77543
  evidence_ids:
  - uniprot-hcv
  - uniprot-mpro
  - hcv-original
  - mpro2020
  - adapter
- assessment_id: activity-completeness
  area: completeness
  topic: Optional activity_spectrum and antibacterial mechanism
  outcome: unknown
  summary: Primary broth MIC and fungal experiments offer bounded enrichment leads.
    Optional absence is not a schema defect. Bacterial precursor-incorporation results
    do not yet justify adding an exact ribosomal/protein target or importing viral
    enzyme IC50s into antibacterial MIC rows.
  target_ids:
  - CHEBI:77543
  evidence_ids:
  - native
  - antibacterial
  - antifungal
  - hcv-original
  - preprint
- assessment_id: other-domains
  area: scope
  topic: Resistance, clinical products, producer, causal graph and datasets
  outcome: not_applicable
  summary: No native assertion occurs in these domains. Host enzyme inhibition, prospective
    therapy, combination-cell results, comparator resistance and the incidental cryptic
    UUID hit do not create such assertions.
  target_ids:
  - CHEBI:77543
  evidence_ids:
  - native
  - adopted-dispositions
  - nsp13-nsp14
  - search
- assessment_id: provenance
  area: provenance
  topic: Actual owners, source history and status
  outcome: supported
  summary: The native fields faithfully reproduce the inspected sources and seven
    seed/reseed events, but source faithfulness does not resolve the two scientific
    errors. Original thirteen hashes are preserved within twenty-three captured inputs.
    Scientific status remains SEEDED.
  target_ids:
  - CHEBI:77543
  evidence_ids:
  - native
  - owners
  - bdb-hcv
  - bdb80
  - gates
- assessment_id: validation
  area: schema
  topic: Focused native gates
  outcome: supported
  summary: Chemistry, schema and strict checks pass; these deterministic gates do
    not test the original figure-to-assay or compound-to-value mapping that produced
    the findings.
  target_ids:
  - CHEBI:77543
  evidence_ids:
  - gates
  - chemistry
  - hcv-figure4
  - published-si
findings:
- finding_id: F1
  issue_key: ebselen-hcv-ic50-fp-mislabeled-emsa
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The HCV IC50 is attached to the wrong experimental method
  description: Original Figure 4 assigns ebselen IC50 1.4 ±0.2 micromolar to fluorescence-polarization
    NS3h–DNA displacement. The native EMSA name and detailed EMSA protocol describe
    a separate qualitative confirmation, copied from current BindingDB. Preserve the
    supported numerical value, but correct its method and condition mapping through
    the maintained source path.
  target_ids:
  - CHEBI:77543
  field_paths:
  - molecular_targets[0].measurements[0].assay_name
  - molecular_targets[0].measurements[0].assay_description
  evidence_ids:
  - native
  - owners
  - hcv-original
  - hcv-figure4
  - hcv-figure1
  - bdb-hcv
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/bindingdb_target_measurements.tsv
    role: Imported quantitative viral target assays
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_bindingdb_targets.py
    role: BindingDB measurement extraction
  rule_id: review-checklist:Evidence/Targets
  native_severity: major
  normalization_reason: Confirmed wrong primary experimental attribution materially
    changes the meaning and reproducibility of the quantitative measurement.
- finding_id: F2
  issue_key: ebselen-80nm-mpro-value-belongs-to-tideglusib
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The cited 80 nM result belongs to tideglusib
  description: BindingDB reactant902201 and the native record assign 80 nM to ebselen.
    Actual original preprint Figure 3, the published Figure 3 and exact published
    Table S3 compound rows assign 0.08 micromolar to tideglusib and 0.03 micromolar
    to ebselen. Adjudicate or retract/reassign this source measurement while preserving
    the separate supported 30 nM and 670 nM ebselen data and their assay qualifications.
  target_ids:
  - CHEBI:77543
  field_paths:
  - molecular_targets[1].measurements[1]
  evidence_ids:
  - native
  - owners
  - preprint
  - preprint-figure
  - published-figure
  - published-si
  - bdb80
  - bdb30
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/bindingdb_target_measurements.tsv
    role: Imported quantitative viral target assays
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_bindingdb_targets.py
    role: BindingDB measurement extraction
  rule_id: review-checklist:Evidence/Targets
  native_severity: major
  normalization_reason: Confirmed cross-compound transfer of a quantitative target
    result; the neutral ebselen identity itself remains correct.
actions:
- action_id: A1
  description: Correct the HCV measurement method and its experimental-condition mapping.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:77543
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/bindingdb_target_measurements.tsv
    role: Imported quantitative viral target assays
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_bindingdb_targets.py
    role: BindingDB measurement extraction
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Map the retained 1.4 micromolar value to original Figure 4 fluorescence polarization
    and the corresponding FP Methods.
  - Keep qualitative EMSA evidence separate; do not retain EMSA-specific reagent concentrations
    or incubation times as the quantitative FP protocol.
  - Preserve NS3 helicase-domain, thiol-sensitivity and assay endpoint qualifications
    without labeling this NS3 protease inhibition.
  - Regenerate through maintained sources and run focused schema/strict, provenance
    and corpus reproduction checks.
- action_id: A2
  description: Adjudicate the erroneous 80 nM compound assignment in the maintained
    BindingDB import.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:77543
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/bindingdb_target_measurements.tsv
    role: Imported quantitative viral target assays
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_bindingdb_targets.py
    role: BindingDB measurement extraction
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - 'Resolve original preprint Figure 3 and published SI material identifiers: ebselen
    SPE_K29359156/CID3194 is 0.03 micromolar, while tideglusib DOM_SIM_153/CID11313622
    is 0.08 micromolar.'
  - Remove or reassign the unsupported ebselen 80 nM assertion with an auditable source
    correction; do not silently discard the source provenance.
  - Retain supported ebselen 30 nM without-DTT and independent 670 nM results at their
    original assay conditions, without treating redox sensitivity as universal inactivity.
  - Verify numerical units, material mapping, duplicate handling and downstream regeneration;
    repeat focused and required provenance gates.
limitations:
- All ten adopted literature leads were resolved at the stated depths. Original abstracts
  alone were read for the two inaccessible exact-reagent questions and the other explicitly
  abstract-only leads; no claim of full-text verification is made for them. Accessible
  HCV/Mpro papers were read at material, relevant experimental Results/Methods and
  actual key figures; unrelated analogue procedures and raw spectra were not independently
  reprocessed.
- LINCS LSM-2644 returned HTTP 500 and Reaxys returned HTTP 403. Their exact chemical
  mappings remain unverified. DrugBank direct retrieval failed 403, but official public
  text was inspected through the web fallback.
- The original preprint full text and small Figure 3 were accessible; larger figure
  and expanded supplement requests failed 429. The separately labeled official published
  SI was independently inspected, with its hash retained. Failed guessed-image and
  incorrectly parameterized BindingDB pages were excluded as evidence.
- Current UniProt statuses and taxa were verified, but the imported HCV example sequence
  was not independently aligned to the original Con1 experimental construct. Database
  chain context must not replace exact primary construct qualification.
- The antibacterial and antifungal originals were read at exact reagent, growth method,
  principal activity tables/results and the relevant mechanism experiments. This review
  does not exhaust every analogue, animal endpoint or discovery-search hit, establish
  clinical susceptibility breakpoints, or infer a unique bacterial protein target.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native, source, status or history field was edited. Optional links, tags and
  notes were checked against this exact ebselen review. The initial thirteen hashes
  were retained, and all expanded captured inputs were rechecked unchanged before
  draft output.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:77543
- https://doi.org/10.1021/cb500512z
- https://doi.org/10.1101/2020.12.16.422677
- https://doi.org/10.1021/acsptsci.0c00216
tags:
- ebselen
- bindingdb
- assay-attribution
- compound-mapping
```
