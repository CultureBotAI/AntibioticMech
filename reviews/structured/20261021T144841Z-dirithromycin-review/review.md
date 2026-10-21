# Dirithromycin: exact structure supported; regulatory withdrawal and binding-site qualification needed

- Review: 20261021T144841Z-dirithromycin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:27:15Z
- Finished UTC: 2026-10-21T14:48:41Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact neutral dirithromycin identity is supported by independent official structure comparisons. Two major findings concern an unqualified APPROVED regulatory summary after the exact US application was formally withdrawn, and a precise P-site target grounding that conflicts with original structures locating intact dirithromycin in the nascent peptide exit tunnel. Historical approval facts and explicitly qualified CARD assertions remain valid provenance; they must not be replaced wholesale or promoted to unsupported functional claims.

## Scope And Provenance

Entire native record: prodrug/clinical definition, five synonyms, two parent terms, role, structural class, complete structure, six exact xrefs, three drug links, three document links, two source concepts/mints, all twenty-three resistance assertions, one evidence-needed molecular target, one FDA product assertion and all seven history events. The sole adopted compound-definition publication lead was resolved and read at available indexed-abstract depth; additional original chemical, structural and regulatory sources were inspected.

Selection: Queue position 368. The thirteen original input hashes were preserved; six actual ARO/FDA/mapping owners were appended before assessment, for nineteen inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:474014 | data/antibiotics/antibacterial/dirithromycin.yaml | generated | dirithromycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:474014 | Actual focused schema validation found no issues. |
| strict | passed | True | CHEBI:474014 | Actual focused strict validation scanned one file with zero errors. |
| chemistry | passed | False | CHEBI:474014 | Native SMILES and InChI reproduce full key, formula, charge, masses, twenty assigned tetrahedral centres and both source mints. |
| external-chemistry-initial | failed | False | CHEBI:474014 | The first scratch comparison selected the RCSB InChIKey row because its program column says InChI and attempted to parse the key as SMILES. The helper raised AssertionError; this is a reader defect, not a native or source structure failure. Its original code is retained as 368-xref-check-initial.py. |
| external-chemistry-corrected | passed | False | CHEBI:474014 | After selecting descriptors by their actual type, nine independently parsed encodings agree: ChEBI, PubChem, ChEMBL, KEGG drug, DrugCentral, GSRS and three stereochemical RCSB DI0 descriptors. Unspecified-stereo descriptor alternatives are not asserted as exact encodings. |
| Authoritative full QC | failed | True | CHEBI:474014 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:474014 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:474014 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:474014 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:474014 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:474014 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:474014 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:474014 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:474014 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact structure, synonyms, active metabolite and epimer boundaries

identity: supported. Targets: CHEBI:474014.

Native structure, twenty assigned centres, masses, names, two groundings and source mints are coherent. Multiple independent authorities and the structural ligand agree. Solution hydrolysis/epimerization does not make an exact parent record a mixture or justify merging with its metabolite.

### Ribosome binding and precision of imported P-site grounding

evidence: concern. Targets: CHEBI:474014.

Direct intact-parent binding is supported by two original structural studies, with the nascent peptide exit tunnel distinct from the occupied P-site. The native target is source-faithful and explicitly evidence-needed, but its precise site requires qualification against this positive structural evidence. Species-specific uL4 contacts and proposed tunnel obstruction are not universal target mechanisms.

### Twenty-three qualified CARD assertions

evidence: supported. Targets: CHEBI:474014.

All 23 exported edges match the official ontology with honest database evidence typing. Their individual functional literatures were not exhaustively reassessed, and structural binding data do not independently validate every determinant, species or allele. No unsupported activity or resistance measurements are added.

### Historical approval versus later regulatory withdrawal

evidence: concern. Targets: CHEBI:474014.

The product identity, original approval date and discontinued marketing are correct. The exact application was subsequently withdrawn in 2007; an unqualified APPROVED regulatory summary omits this controlling event. Preserve the historical facts while adding withdrawal qualification through maintained event/overlay handling. No safety-based withdrawal or worldwide status is inferred.

### Generated ownership, source citation depth and optional completeness

provenance: supported. Targets: CHEBI:474014.

All native fields and history events were assessed against their actual source owners. The only adopted compound citation is a review read at indexed-abstract depth. Primary follow-up supports chemical/activity context with stated experimental boundaries. Optional quantitative activity, producer, mode, target-scope or graph additions are not defects merely because absent.

## Findings

### F1: Qualify the regulatory summary with the exact 2007 approval withdrawal

major / open / confirmed; issue key: dirithromycin-fda-050678-withdrawn-approval-summary.

clinical_status is APPROVED without historical qualification even though the official 2007 notice withdraws NDA 50–678 for this exact Dynabac delayed-release product effective 2007-12-07. The native original 1995 approval date/AP event and discontinued/currently_marketed=false fields are correct and should remain. The seeder converts an approved original into an unqualified summary without later-event handling. This is a missing formal regulatory qualification, not an inference from off-market status or a claim of safety withdrawal. The erroneous 1997 withdrawal was corrected and is not the basis of this finding.

### F2: Reconcile the precise P-site target label with directly observed exit-tunnel binding

major / open / confirmed; issue key: dirithromycin-card-p-site-versus-npet-grounding.

The native molecular target labels the 50S P-site as the direct-binding site. It accurately states that CARD supplied this relation and that primary evidence is needed. Independently inspected intact-dirithromycin structures from T. thermophilus and E. coli instead locate the compound in the nascent peptide exit tunnel while A/P-site tRNAs remain bound. Preserve the database assertion as provenance, but qualify its precise site rather than promote it to a primary P-site observation. This finding rests on positive exact-compound localization, not merely missing evidence.

## Recommended Actions And Acceptance Checks

### A1

Add maintained application-level withdrawal/event qualification and derive the regulatory summary without erasing historical approval.

- Capture NDA 050678, Dynabac delayed-release product,2007-12-07 effective withdrawal and official E7-21886 source with separate retrieval/version provenance. Preserve original 1995-06-19 approval/AP and discontinued marketing facts.
- Distinguish the corrected 1997 erroneous withdrawal from the valid 2007 notice. Do not label this a safety/efficacy withdrawal or assume worldwide nonapproval.
- Apply an explicit maintained withdrawal overlay/event rule rather than rewriting generated YAML. Regenerate and verify summary/event consistency, focused schema/strict checks and corpus reproduction.

### A2

Qualify the drug-specific imported P-site relation and, if authorized, add the exact primary ribosome target at supported scope.

- Retain the original CARD relation and evidence-needed provenance while explicitly reconciling the NPET structural evidence; do not relabel the old database citation as primary.
- Represent the 50S/23S-rRNA exit-tunnel target with claim-level 2019/2020 evidence and species/structural context. Do not promote the thermophilic uL4 side-chain contact to all bacteria or a proposed steric mechanism to a measured result.
- Use a drug-specific maintained source qualification or narrowly justified transform; a global change to ARO3000757 requires separate review of every affected record. Preserve parent/metabolite/epimer assay boundaries and validate regenerated output.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/dirithromycin.yaml; Entire native YAML, including every resistance entry, evidence qualifier, product field and history event. | supports | The record denotes neutral dirithromycin, CHEBI474014/ARO3000176, C42H78N2O14, WLOHNSSYAXHWNR-DWIOZXRMSA-N. It remains SEEDED/EXACT. Twenty-three resistance entries explicitly say database assertion, not primary citation. The direct-binding P-site entry explicitly remains PRIMARY_EVIDENCE_NEEDED. The one US product assertion retains 1995 original approval, discontinued marketing and currently_marketed=false; the standalone clinical_status is APPROVED. No quantitative activity, producer or causal graph is asserted. |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv; data/raw/aro_resistance_edges.tsv; data/raw/fda_clinical_status.tsv; conf/aro_target_roles.tsv; scripts/extract_source_inventory.py; scripts/extract_fda_clinical_status.py; scripts/seed_from_sources.py; Complete exact rows: ChEBI2970, ARO83, target 93, resistance 2254–2276, FDA3220; relevant extraction, seeding and role mapping code. | supports | All imported identity, role, target, resistance and product claims reproduce their actual owners. The source map explicitly types ARO3000757 as a ribosomal direct-binding target; seeding preserves its primary-evidence-needed status. FDA extraction selects historical ORIG/AP submissions and seeding unconditionally emits APPROVED as both summary and product status, without a later withdrawal event. Source mints and versions reproduce; no exact curator override was found. |
| identity | CHEBI:474014; PubChem:6473883; CHEMBL1237072; UNII:1801D76STL; PDB-CCD:DI0; Complete official entries and chemical descriptors; independent parsing of every specified exact graph. | supports | All five native aliases agree with the neutral twenty-centre structure, including the R-configured oxazine substituent. Current ChEBI, PubChem and ChEMBL reproduce the full native key; GSRS version 29 also matches the exact regulatory substance. RCSB DI0 stereochemical InChI and both canonical stereochemical SMILES match, linking the structural studies to this compound. CAS62013-04-1 and Beilstein 4225019 are attested in ChEBI; the paid Beilstein registry itself was not inspected. |
| classification | CHEBI:25105; CHEBI:33281; ARO:0000000; ARO:3000176; Official ChEBI parent/role definitions and current ARO blocks, with graph inspection. | supports | The macrocyclic lactone/sugar structure belongs to the broader macrolide class. The antimicrobial role is inherited and retained; filing as ANTIBACTERIAL follows the antibacterial ARO source/class. ChEBI also identifies prodrug role CHEBI50266, which is outside the configured antimicrobial-role export roots and is already described in the native definition. Its omission from activity_roles is not a defect. |
| other-links | DrugCentral:925; KEGG:D03865; DrugBank:DB00954; LINCS:LSM-5636; patent:BE840431; patent:US4048306; wikipedia.en:Dirithromycin; Complete public DrugCentral and KEGG entries plus independently parsed structures; patent bibliographic records and selected US condensation-product text; DrugBank landing resolution. | context_only | DrugCentral and KEGG drug structures match the exact native graph, while their links remain drug-level. US4048306 resolves to aldehyde–erythromycylamine condensation products; BE840431 is the corresponding erythromycin-derivative document family. These are document links, not exact compound structures; selected examples were not used to assign the exact parent or clinical efficacy. DrugBank direct access returned 403 and public web exposed only a landing shell. LINCS returned 500, so its exact accession remains ChEBI-attested only. Wikipedia is a topic link and supplies no scientific evidence. |
| card | https://raw.githubusercontent.com/arpcard/aro/master/src/ontology/aro.obo; All 26 pertinent current official ARO blocks examined: compound, class, target and 23 resistance determinants. | supports | Every native resistance identifier resolves to its expected label and has an explicit confers_resistance_to_antibiotic ARO3000176 relation. All three mph entries and twenty Erm entries agree with the inherited mechanism categories. The target block explicitly supplies targeted_by_antibiotic ARO3000176 for the P-site. This verifies source fidelity, not 23 independently tested dirithromycin-specific functional mechanisms. No borrowed producer or host taxonomy is inferred from determinant definitions. |
| adopted | PMID:7683018; DOI:10.1093/jac/31.suppl_c.1; Sole adopted ARO compound-definition lead: full available indexed abstract and publication type inspected. | context_only | This is the 1993 review Chemistry and mode of action of macrolides. The indexed abstract is expressly truncated at 250 words. It gives class/chemical-development context, not an inspected exact-compound P-site binding experiment. It is treated as a review lead, not primary evidence, and is not presented as full-text read. |
| synthesis1991 | PMID:1929252; DOI:10.1128/AAC.35.6.1116; PMC284297; Complete original abstract and selected original scanned pages 1116–1118 visually read, including synthesis, assay methods, Table 1 NMR and Figures 1–2. | supports | The original synthesis condenses 9(S)-erythromycylamine with 2-(2-methoxyethoxy)acetaldehyde and characterizes isolated dirithromycin. Named antibacterial activity and mouse protection are reported; selected methods specify Mueller-Hinton agar dilution, typical 10^4-CFU spots and 18–20 h at 37°C, with different anaerobic conditions. MIC and subculture-based MBC are distinct. The paper identifies acidic/in-vivo conversion to erythromycylamine. No new numerical native assay is imported from the unreviewed remaining result tables. |
| epimer1995 | PMID:7492081; DOI:10.1128/AAC.39.7.1436; PMC162758; Complete original indexed/PMC abstract read; full-paper PDF routes returned challenge HTML or 404. | context_only | The oxazine substituent is R in dirithromycin and S in epidirithromycin. Both interconvert toward 85:15 dirithromycin:epidirithromycin under condition-dependent solution kinetics and hydrolyze to erythromycylamine. In an experiment specifically minimizing hydrolysis and following it by HPLC, dirithromycin inhibited cell-free protein synthesis at less than 10% of erythromycylamine activity. This is a conditional experimental result, not proof intact dirithromycin never binds ribosomes, nor evidence the native exact graph denotes an 85:15 mixture. |
| ribosome2019 | PMID:30936109; DOI:10.1128/AAC.02266-18; PMC6535518; PDB:6OF1; Entire original main text read; Figures 1–2 visually inspected; original 2020 erratum PMID31988110 read completely. | supports | The 2.8 Å T. thermophilus 70S cocrystal contains intact dirithromycin in the nascent peptide exit tunnel, with tRNAs occupying A/P/E sites. It contacts 23S rRNA A2058 and a species-specific uL4 His 69 region. Crystallization uses 250 micromolar drug; the proposed side-chain interaction is structural interpretation, not a universal affinity or whole-cell resistance result. The erratum corrects funding acknowledgments only. The source distinguishes the drug pocket from the P-site tRNA location. |
| ribosome2020 | PMID:32144191; DOI:10.1261/rna.073817.119; PMC7266154; PDB:6XZ7; PDB:6XZB; PDB:6XZA; Entire original main XML text read; Figures 1–2 visually inspected; public RCSB experiment/citation metadata read. | supports | The 2.1 Å focused E. coli 50S reconstruction is PDB6XZ7 and locates intact dirithromycin in the canonical exit-tunnel pocket. The full 70S reconstruction with A/P tRNAs is PDB6XZB; PDB6XZA is the reconstruction with P-site tRNA only. These accession-specific scopes are distinguished. Competition against BODIPY-erythromycin measures apparent affinity, and cell-free luciferase translation measures inhibition; neither endpoint is a cellular MIC. Unlike the thermophilic structure, the flexible side chain makes no additional stable uL4 contact. Improved tunnel obstruction is proposed, not directly demonstrated with a sufficiently long nascent peptide. No significant PTC rearrangements occur under the tested initiation/pretranslocation conditions. The precise binding site is not the P-site. |
| fda-history | FDA NDA050678 product001; UNII1801D76STL;1997 supplemental approval letter NDA50-678/SE1-003; Complete current openFDA application JSON, exact GSRS structure, and all five pages of the historical 1997 approval-letter package visually read. | supports | The original 1995-06-19 approval, Lilly sponsor, Dynabac 250 mg delayed-release oral tablet and discontinued marketing agree with the native assertion. GSRS version 29 independently matches the exact neutral graph. The 1997 supplement approves specified short-course bronchitis and uncomplicated skin/skin-structure indications in susceptible organisms; it is historical product authorization, not current availability. The schema permits WITHDRAWN and describes clinical_status as regulatory/use status; historical AP alone cannot summarize a later approval withdrawal. |
| withdrawal | https://www.govinfo.gov/content/pkg/FR-2007-11-07/pdf/E7-21886.pdf; Official notice 72FR62858–62863: summary/effective date, exact NDA 50–678 row on 62861 and operative withdrawal text on 62862–62863 read; exact table page visually inspected. | refutes | The FDA withdraws approval of Dynabac dirithromycin delayed-release tablets USP, NDA 50–678, held by Lilly Research Laboratories, effective 2007-12-07. The notice says applicants requested withdrawal because products were no longer marketed and waived a hearing; it does not identify a safety/efficacy withdrawal. Its operative clause includes amendments and supplements. This is a regulatory event beyond marketing discontinuation and is absent from the unqualified native approval summary. |
| earlier-correction | https://www.govinfo.gov/content/pkg/FR-1997-07-21/pdf/97-19012.pdf; Complete exact correction notice on 62FR39003 read. | context_only | The 1997 notice explicitly corrects an erroneous earlier withdrawal of this same NDA and confirms approval remained in effect then. This correction is preserved and is not confused with the independently issued 2007 withdrawal. The latter is the basis of the finding. |
| adapter | Structured iModulonDB dataset catalog and searches; Adapter executed before web mechanism follow-up; S. aureus staph_precise 108 erm query and E. coli precise 1k mph query. | context_only | No matching expression module was returned. Erm substring hits were unrelated permease/spermidine products; mph hits were umpH and ampH. No relevant module warranted summarize. Native assertions are taxon-unspecified, so these bounded dataset results do not establish absence of functional resistance or direct binding. |
| search | 368-inclusive-hits.txt;368-literature.json; Ignored-inclusive local exact identifier/name/key/application search; bounded exact-compound original-literature and public-authority follow-up. | context_only | Native rows and reproducible sources were found; the curator tree contained no exact dirithromycin override outside its review queue. Public literature search found chemical/prodrug, direct structural, host-cell and pharmacokinetic studies; host-neutrophil response findings were not imported as antimicrobial targets. Regulatory searches distinguished the 1997 correction from the 2007 withdrawal. This is not an exhaustive audit of every primary paper behind 23 CARD determinants. |
| validation | 368-schema.log;368-strict.log;368-chemistry.json;368-xref-chemistry.json; Actual focused executions and nineteen-input hash recheck. | supports | Schema, strict, native chemistry and corrected external chemistry checks pass. The initial RCSB descriptor-reader failure is explicitly retained; no chemical defect follows. A first scratch metadata print used nonexistent git_commit instead of git_revision after hashing; the corrected check verified both assigned captures and all nineteen 368 inputs. The optional BeautifulSoup reader was unavailable; standard-library extraction supplied the inspected text. |
| metabolite-spelling | PMID:9184366; DOI:10.1093/jac/39.5.647; CHEBI:73708; Complete original indexed abstract and current ChEBI entry read; ignored-inclusive maintained spelling search. | context_only | The native definition uses erythromycyclamine, whereas the 1991/1995 studies use erythromycylamine. The 1997 Chlamydia pneumoniae primary abstract itself repeatedly uses erythromycyclamine for the active metabolite, and current ChEBI73708 uses the same spelling. This is an attested naming variation; the present review does not classify it as a confirmed typo or infer a different chemical identity. No activity measurement from this follow-up is transferred to the native record. |

## Limits And Additional Notes

- LINCS LSM-5636 was not independently readable (HTTP 500), so that exact cross-reference remains ChEBI-attested. Beilstein 4225019 was not checked in a paid registry. DrugBank returned 403 directly and only a landing shell via web; the drug-level link resolves but its full content was not inspected.
- The sole adopted lead 7683018 is a review; its entire available indexed abstract, marked truncated at 250 words, was read. It is not full-text primary target evidence.
- The 1991 primary paper was reviewed at complete-abstract plus selected original pages 1116–1118 depth, including synthesis, structures, NMR table and early methods. Remaining MIC/MBC and animal-result tables were not assessed, and no new numerical observation is curated. The 1995 study was read at complete-abstract depth; PMC PDF returned challenge HTML and the alternate public archive returned 404.
- The 2019 and 2020 main articles were read completely and selected main figures visually inspected; their supplementary tables, movie, raw diffraction/cryo-EM data and dose-response fits were not independently reprocessed. The 2020 apparent-affinity and luciferase assays do not by themselves isolate every hydrolysis contribution during incubation; the intact structural ligand and the earlier conditional hydrolysis-minimized experiment are kept distinct.
- The 1997 supplemental approval letter was read in full as scans and supports historical indications; the complete final printed product label was not obtained. The 2007 withdrawal notice was read at exact relevant scope and table visually inspected. The finding addresses this US application only, with no inference of safety/efficacy withdrawal or current status in other jurisdictions.
- All 23 database resistance assertions were checked against current official ARO, but individual original functional studies for all determinants were not exhaustively read. Negative structured-expression searches are not negative biological evidence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native scientific-status promotion is implied. Regulatory and target follow-up belongs to maintained source/qualification owners; optional evidence enrichment remains distinct from established findings.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T144841Z-dirithromycin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Dirithromycin: exact structure supported; regulatory withdrawal and binding-site
  qualification needed'
started_at: '2026-10-21T14:27:15Z'
finished_at: '2026-10-21T14:48:41Z'
reviewer:
  identity: Codex review002 subagent
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
summary: The exact neutral dirithromycin identity is supported by independent official
  structure comparisons. Two major findings concern an unqualified APPROVED regulatory
  summary after the exact US application was formally withdrawn, and a precise P-site
  target grounding that conflicts with original structures locating intact dirithromycin
  in the nascent peptide exit tunnel. Historical approval facts and explicitly qualified
  CARD assertions remain valid provenance; they must not be replaced wholesale or
  promoted to unsupported functional claims.
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
  - path: data/antibiotics/antibacterial/dirithromycin.yaml
    sha256: 59c79e64f19626ca95c5f0aa5df0045dfbd323d655c8e4294a6b2581e01af2f3
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
- target_id: CHEBI:474014
  path: data/antibiotics/antibacterial/dirithromycin.yaml
  label: dirithromycin
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
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/fda_clinical_status.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: Actual maintained source input for the record
scope:
  description: 'Entire native record: prodrug/clinical definition, five synonyms,
    two parent terms, role, structural class, complete structure, six exact xrefs,
    three drug links, three document links, two source concepts/mints, all twenty-three
    resistance assertions, one evidence-needed molecular target, one FDA product assertion
    and all seven history events. The sole adopted compound-definition publication
    lead was resolved and read at available indexed-abstract depth; additional original
    chemical, structural and regulatory sources were inspected.'
  selection: Queue position 368. The thirteen original input hashes were preserved;
    six actual ARO/FDA/mapping owners were appended before assessment, for nineteen
    inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:474014
  exclusions:
  - target: Erythromycylamine, epidirithromycin and other macrolides
    reason: Active metabolite, opposite oxazine epimer and adjacent drugs remain distinct.
      Hydrolysis and epimerization during assays can affect experimental material;
      their results are not silently exact-parent measurements.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Actual focused schema validation found no issues.
  target_ids:
  - CHEBI:474014
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/dirithromycin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Actual focused strict validation scanned one file with zero errors.
  target_ids:
  - CHEBI:474014
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/dirithromycin.yaml --out /private/tmp/am-review-session/368-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Native SMILES and InChI reproduce full key, formula, charge, masses, twenty
    assigned tetrahedral centres and both source mints.
  target_ids:
  - CHEBI:474014
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 368
  exit_code: 0
  expected_exit_code: 0
- check_id: external-chemistry-initial
  name: external-chemistry-initial
  status: failed
  required: false
  summary: The first scratch comparison selected the RCSB InChIKey row because its
    program column says InChI and attempted to parse the key as SMILES. The helper
    raised AssertionError; this is a reader defect, not a native or source structure
    failure. Its original code is retained as 368-xref-check-initial.py.
  target_ids:
  - CHEBI:474014
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/368-xref-check.py
  exit_code: 1
  expected_exit_code: 0
- check_id: external-chemistry-corrected
  name: external-chemistry-corrected
  status: passed
  required: false
  summary: 'After selecting descriptors by their actual type, nine independently parsed
    encodings agree: ChEBI, PubChem, ChEMBL, KEGG drug, DrugCentral, GSRS and three
    stereochemical RCSB DI0 descriptors. Unspecified-stereo descriptor alternatives
    are not asserted as exact encodings.'
  target_ids:
  - CHEBI:474014
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/368-xref-check.py
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
  - CHEBI:474014
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
  - CHEBI:474014
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
  - CHEBI:474014
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
  - CHEBI:474014
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
  - CHEBI:474014
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
  - CHEBI:474014
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
  - CHEBI:474014
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
  - CHEBI:474014
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
  - CHEBI:474014
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/dirithromycin.yaml
  locator: Entire native YAML, including every resistance entry, evidence qualifier,
    product field and history event.
  accessed_at: '2026-10-21T14:44:21Z'
  support: supports
  summary: The record denotes neutral dirithromycin, CHEBI474014/ARO3000176, C42H78N2O14,
    WLOHNSSYAXHWNR-DWIOZXRMSA-N. It remains SEEDED/EXACT. Twenty-three resistance
    entries explicitly say database assertion, not primary citation. The direct-binding
    P-site entry explicitly remains PRIMARY_EVIDENCE_NEEDED. The one US product assertion
    retains 1995 original approval, discontinued marketing and currently_marketed=false;
    the standalone clinical_status is APPROVED. No quantitative activity, producer
    or causal graph is asserted.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv;
    data/raw/aro_resistance_edges.tsv; data/raw/fda_clinical_status.tsv; conf/aro_target_roles.tsv;
    scripts/extract_source_inventory.py; scripts/extract_fda_clinical_status.py; scripts/seed_from_sources.py
  locator: 'Complete exact rows: ChEBI2970, ARO83, target 93, resistance 2254–2276,
    FDA3220; relevant extraction, seeding and role mapping code.'
  accessed_at: '2026-10-21T14:44:21Z'
  support: supports
  summary: All imported identity, role, target, resistance and product claims reproduce
    their actual owners. The source map explicitly types ARO3000757 as a ribosomal
    direct-binding target; seeding preserves its primary-evidence-needed status. FDA
    extraction selects historical ORIG/AP submissions and seeding unconditionally
    emits APPROVED as both summary and product status, without a later withdrawal
    event. Source mints and versions reproduce; no exact curator override was found.
  snapshot_sha256: 7c39c8405cdedad0e91b5549ae719c2ae234c8e3942afda9b1a9389aa44208f9
- evidence_id: identity
  kind: authority
  reference: CHEBI:474014; PubChem:6473883; CHEMBL1237072; UNII:1801D76STL; PDB-CCD:DI0
  locator: Complete official entries and chemical descriptors; independent parsing
    of every specified exact graph.
  accessed_at: '2026-10-21T14:33:01Z'
  support: supports
  summary: All five native aliases agree with the neutral twenty-centre structure,
    including the R-configured oxazine substituent. Current ChEBI, PubChem and ChEMBL
    reproduce the full native key; GSRS version 29 also matches the exact regulatory
    substance. RCSB DI0 stereochemical InChI and both canonical stereochemical SMILES
    match, linking the structural studies to this compound. CAS62013-04-1 and Beilstein
    4225019 are attested in ChEBI; the paid Beilstein registry itself was not inspected.
  snapshot_sha256: 1ec799c02b5c0f83261f7e3f9521b0f5c5f5867c976de246642a5d74c292ce7f
- evidence_id: classification
  kind: authority
  reference: CHEBI:25105; CHEBI:33281; ARO:0000000; ARO:3000176
  locator: Official ChEBI parent/role definitions and current ARO blocks, with graph
    inspection.
  accessed_at: '2026-10-21T14:33:01Z'
  support: supports
  summary: The macrocyclic lactone/sugar structure belongs to the broader macrolide
    class. The antimicrobial role is inherited and retained; filing as ANTIBACTERIAL
    follows the antibacterial ARO source/class. ChEBI also identifies prodrug role
    CHEBI50266, which is outside the configured antimicrobial-role export roots and
    is already described in the native definition. Its omission from activity_roles
    is not a defect.
  snapshot_sha256: 957190ce7737ea57b16a0ce99e5e7ca8c53ba1f0f5b6a62d144820ef43238ee9
- evidence_id: other-links
  kind: database
  reference: DrugCentral:925; KEGG:D03865; DrugBank:DB00954; LINCS:LSM-5636; patent:BE840431;
    patent:US4048306; wikipedia.en:Dirithromycin
  locator: Complete public DrugCentral and KEGG entries plus independently parsed
    structures; patent bibliographic records and selected US condensation-product
    text; DrugBank landing resolution.
  accessed_at: '2026-10-21T14:33:02Z'
  support: context_only
  summary: DrugCentral and KEGG drug structures match the exact native graph, while
    their links remain drug-level. US4048306 resolves to aldehyde–erythromycylamine
    condensation products; BE840431 is the corresponding erythromycin-derivative document
    family. These are document links, not exact compound structures; selected examples
    were not used to assign the exact parent or clinical efficacy. DrugBank direct
    access returned 403 and public web exposed only a landing shell. LINCS returned
    500, so its exact accession remains ChEBI-attested only. Wikipedia is a topic
    link and supplies no scientific evidence.
  snapshot_sha256: 8596bfa6a8ec7d1545c615b1a647b497069b2119af7fa9a1873739d2fee423dc
- evidence_id: card
  kind: database
  reference: https://raw.githubusercontent.com/arpcard/aro/master/src/ontology/aro.obo
  locator: 'All 26 pertinent current official ARO blocks examined: compound, class,
    target and 23 resistance determinants.'
  accessed_at: '2026-10-21T14:33:03Z'
  support: supports
  summary: Every native resistance identifier resolves to its expected label and has
    an explicit confers_resistance_to_antibiotic ARO3000176 relation. All three mph
    entries and twenty Erm entries agree with the inherited mechanism categories.
    The target block explicitly supplies targeted_by_antibiotic ARO3000176 for the
    P-site. This verifies source fidelity, not 23 independently tested dirithromycin-specific
    functional mechanisms. No borrowed producer or host taxonomy is inferred from
    determinant definitions.
  snapshot_sha256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
- evidence_id: adopted
  kind: database
  reference: PMID:7683018; DOI:10.1093/jac/31.suppl_c.1
  locator: 'Sole adopted ARO compound-definition lead: full available indexed abstract
    and publication type inspected.'
  accessed_at: '2026-10-21T14:33:03Z'
  support: context_only
  summary: This is the 1993 review Chemistry and mode of action of macrolides. The
    indexed abstract is expressly truncated at 250 words. It gives class/chemical-development
    context, not an inspected exact-compound P-site binding experiment. It is treated
    as a review lead, not primary evidence, and is not presented as full-text read.
  snapshot_sha256: 18ea2f2336398043b6fd63e48896630497848074afa004b42a913014ca41edee
- evidence_id: synthesis1991
  kind: primary_source
  reference: PMID:1929252; DOI:10.1128/AAC.35.6.1116; PMC284297
  locator: Complete original abstract and selected original scanned pages 1116–1118
    visually read, including synthesis, assay methods, Table 1 NMR and Figures 1–2.
  accessed_at: '2026-10-21T14:35:50Z'
  support: supports
  summary: The original synthesis condenses 9(S)-erythromycylamine with 2-(2-methoxyethoxy)acetaldehyde
    and characterizes isolated dirithromycin. Named antibacterial activity and mouse
    protection are reported; selected methods specify Mueller-Hinton agar dilution,
    typical 10^4-CFU spots and 18–20 h at 37°C, with different anaerobic conditions.
    MIC and subculture-based MBC are distinct. The paper identifies acidic/in-vivo
    conversion to erythromycylamine. No new numerical native assay is imported from
    the unreviewed remaining result tables.
  snapshot_sha256: 33aade5023947b3acc3dafe4f5488b2866163958e081956b8b196ed52a95870e
- evidence_id: epimer1995
  kind: primary_source
  reference: PMID:7492081; DOI:10.1128/AAC.39.7.1436; PMC162758
  locator: Complete original indexed/PMC abstract read; full-paper PDF routes returned
    challenge HTML or 404.
  accessed_at: '2026-10-21T14:34:50Z'
  support: context_only
  summary: The oxazine substituent is R in dirithromycin and S in epidirithromycin.
    Both interconvert toward 85:15 dirithromycin:epidirithromycin under condition-dependent
    solution kinetics and hydrolyze to erythromycylamine. In an experiment specifically
    minimizing hydrolysis and following it by HPLC, dirithromycin inhibited cell-free
    protein synthesis at less than 10% of erythromycylamine activity. This is a conditional
    experimental result, not proof intact dirithromycin never binds ribosomes, nor
    evidence the native exact graph denotes an 85:15 mixture.
  snapshot_sha256: bf005ce6aff98dec17b5ace6a09c71e2be8059c418439e66bd1f582c428ca278
- evidence_id: ribosome2019
  kind: primary_source
  reference: PMID:30936109; DOI:10.1128/AAC.02266-18; PMC6535518; PDB:6OF1
  locator: Entire original main text read; Figures 1–2 visually inspected; original
    2020 erratum PMID31988110 read completely.
  accessed_at: '2026-10-21T14:34:50Z'
  support: supports
  summary: The 2.8 Å T. thermophilus 70S cocrystal contains intact dirithromycin in
    the nascent peptide exit tunnel, with tRNAs occupying A/P/E sites. It contacts
    23S rRNA A2058 and a species-specific uL4 His 69 region. Crystallization uses
    250 micromolar drug; the proposed side-chain interaction is structural interpretation,
    not a universal affinity or whole-cell resistance result. The erratum corrects
    funding acknowledgments only. The source distinguishes the drug pocket from the
    P-site tRNA location.
  snapshot_sha256: 323e7802c8dc37bedfb7cc4c3393a0988e671518a4812ceca62255d8d7002c5c
- evidence_id: ribosome2020
  kind: primary_source
  reference: PMID:32144191; DOI:10.1261/rna.073817.119; PMC7266154; PDB:6XZ7; PDB:6XZB;
    PDB:6XZA
  locator: Entire original main XML text read; Figures 1–2 visually inspected; public
    RCSB experiment/citation metadata read.
  accessed_at: '2026-10-21T14:33:46Z'
  support: supports
  summary: The 2.1 Å focused E. coli 50S reconstruction is PDB6XZ7 and locates intact
    dirithromycin in the canonical exit-tunnel pocket. The full 70S reconstruction
    with A/P tRNAs is PDB6XZB; PDB6XZA is the reconstruction with P-site tRNA only.
    These accession-specific scopes are distinguished. Competition against BODIPY-erythromycin
    measures apparent affinity, and cell-free luciferase translation measures inhibition;
    neither endpoint is a cellular MIC. Unlike the thermophilic structure, the flexible
    side chain makes no additional stable uL4 contact. Improved tunnel obstruction
    is proposed, not directly demonstrated with a sufficiently long nascent peptide.
    No significant PTC rearrangements occur under the tested initiation/pretranslocation
    conditions. The precise binding site is not the P-site.
  snapshot_sha256: 5c0adedc79646625e9a303aecaa6b50d241731118f0c34eb6b298bed42b992d2
- evidence_id: fda-history
  kind: authority
  reference: FDA NDA050678 product001; UNII1801D76STL;1997 supplemental approval letter
    NDA50-678/SE1-003
  locator: Complete current openFDA application JSON, exact GSRS structure, and all
    five pages of the historical 1997 approval-letter package visually read.
  accessed_at: '2026-10-21T14:33:03Z'
  support: supports
  summary: The original 1995-06-19 approval, Lilly sponsor, Dynabac 250 mg delayed-release
    oral tablet and discontinued marketing agree with the native assertion. GSRS version
    29 independently matches the exact neutral graph. The 1997 supplement approves
    specified short-course bronchitis and uncomplicated skin/skin-structure indications
    in susceptible organisms; it is historical product authorization, not current
    availability. The schema permits WITHDRAWN and describes clinical_status as regulatory/use
    status; historical AP alone cannot summarize a later approval withdrawal.
  snapshot_sha256: 542cb5d4f0df65a20575caa368a721094540082027e8215e407bc8823d64a76c
- evidence_id: withdrawal
  kind: authority
  reference: https://www.govinfo.gov/content/pkg/FR-2007-11-07/pdf/E7-21886.pdf
  locator: 'Official notice 72FR62858–62863: summary/effective date, exact NDA 50–678
    row on 62861 and operative withdrawal text on 62862–62863 read; exact table page
    visually inspected.'
  accessed_at: '2026-10-21T14:33:48Z'
  support: refutes
  summary: The FDA withdraws approval of Dynabac dirithromycin delayed-release tablets
    USP, NDA 50–678, held by Lilly Research Laboratories, effective 2007-12-07. The
    notice says applicants requested withdrawal because products were no longer marketed
    and waived a hearing; it does not identify a safety/efficacy withdrawal. Its operative
    clause includes amendments and supplements. This is a regulatory event beyond
    marketing discontinuation and is absent from the unqualified native approval summary.
  snapshot_sha256: dcdd49e13243da43b6a71b1e8c7b81a18a6a2465606e09f50180eb5f843fa142
- evidence_id: earlier-correction
  kind: authority
  reference: https://www.govinfo.gov/content/pkg/FR-1997-07-21/pdf/97-19012.pdf
  locator: Complete exact correction notice on 62FR39003 read.
  accessed_at: '2026-10-21T14:33:35Z'
  support: context_only
  summary: The 1997 notice explicitly corrects an erroneous earlier withdrawal of
    this same NDA and confirms approval remained in effect then. This correction is
    preserved and is not confused with the independently issued 2007 withdrawal. The
    latter is the basis of the finding.
  snapshot_sha256: 46ee46083006f989583679259c46c31543a45fa5b126e804a94e146dc02bd53e
- evidence_id: adapter
  kind: database
  reference: Structured iModulonDB dataset catalog and searches
  locator: Adapter executed before web mechanism follow-up; S. aureus staph_precise
    108 erm query and E. coli precise 1k mph query.
  accessed_at: '2026-10-21T14:44:21Z'
  support: context_only
  summary: No matching expression module was returned. Erm substring hits were unrelated
    permease/spermidine products; mph hits were umpH and ampH. No relevant module
    warranted summarize. Native assertions are taxon-unspecified, so these bounded
    dataset results do not establish absence of functional resistance or direct binding.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: search
  kind: search
  reference: 368-inclusive-hits.txt;368-literature.json
  locator: Ignored-inclusive local exact identifier/name/key/application search; bounded
    exact-compound original-literature and public-authority follow-up.
  accessed_at: '2026-10-21T14:44:21Z'
  support: context_only
  summary: Native rows and reproducible sources were found; the curator tree contained
    no exact dirithromycin override outside its review queue. Public literature search
    found chemical/prodrug, direct structural, host-cell and pharmacokinetic studies;
    host-neutrophil response findings were not imported as antimicrobial targets.
    Regulatory searches distinguished the 1997 correction from the 2007 withdrawal.
    This is not an exhaustive audit of every primary paper behind 23 CARD determinants.
  search_scope: 2026-10-21; rg --no-ignore --hidden across data, curation, conf, scripts,
    src, docs, .claude, reviews and reports for dirithromycin, CHEBI:474014, ARO:3000176,
    WLOHNSSYAXHWNR and 050678. Ignored files included. EuropePMC exact dirithromycin
    with ribosome, erythromycylamine, phosphotransferase or mechanism; official FDA/GovInfo
    exact application and drug-name withdrawal queries; exact chemical authority IDs
    and adopted PMID.
  snapshot_sha256: 0361c3c071fe0ec4153b51b1462bebbbfbef427926fa097b98f5a429086f44dc
- evidence_id: validation
  kind: validation
  reference: 368-schema.log;368-strict.log;368-chemistry.json;368-xref-chemistry.json
  locator: Actual focused executions and nineteen-input hash recheck.
  accessed_at: '2026-10-21T14:44:21Z'
  support: supports
  summary: Schema, strict, native chemistry and corrected external chemistry checks
    pass. The initial RCSB descriptor-reader failure is explicitly retained; no chemical
    defect follows. A first scratch metadata print used nonexistent git_commit instead
    of git_revision after hashing; the corrected check verified both assigned captures
    and all nineteen 368 inputs. The optional BeautifulSoup reader was unavailable;
    standard-library extraction supplied the inspected text.
  snapshot_sha256: f683738b568305da76f6223e3b8758687d0ecc7b8fb31f4d019e6fc054f1b3ba
- evidence_id: metabolite-spelling
  kind: primary_source
  reference: PMID:9184366; DOI:10.1093/jac/39.5.647; CHEBI:73708
  locator: Complete original indexed abstract and current ChEBI entry read; ignored-inclusive
    maintained spelling search.
  accessed_at: '2026-10-21T14:44:10Z'
  support: context_only
  summary: The native definition uses erythromycyclamine, whereas the 1991/1995 studies
    use erythromycylamine. The 1997 Chlamydia pneumoniae primary abstract itself repeatedly
    uses erythromycyclamine for the active metabolite, and current ChEBI73708 uses
    the same spelling. This is an attested naming variation; the present review does
    not classify it as a confirmed typo or infer a different chemical identity. No
    activity measurement from this follow-up is transferred to the native record.
  snapshot_sha256: ee881b54626122b4b5ad32604a0e5ac5c4ae1f7a37c50dec6b397d0c58bb8616
assessments:
- assessment_id: identity
  area: identity
  topic: Exact structure, synonyms, active metabolite and epimer boundaries
  outcome: supported
  summary: Native structure, twenty assigned centres, masses, names, two groundings
    and source mints are coherent. Multiple independent authorities and the structural
    ligand agree. Solution hydrolysis/epimerization does not make an exact parent
    record a mixture or justify merging with its metabolite.
  target_ids:
  - CHEBI:474014
  evidence_ids:
  - native
  - identity
  - classification
  - other-links
  - synthesis1991
  - epimer1995
  - validation
  - metabolite-spelling
- assessment_id: mechanism
  area: evidence
  topic: Ribosome binding and precision of imported P-site grounding
  outcome: concern
  summary: Direct intact-parent binding is supported by two original structural studies,
    with the nascent peptide exit tunnel distinct from the occupied P-site. The native
    target is source-faithful and explicitly evidence-needed, but its precise site
    requires qualification against this positive structural evidence. Species-specific
    uL4 contacts and proposed tunnel obstruction are not universal target mechanisms.
  target_ids:
  - CHEBI:474014
  evidence_ids:
  - card
  - owners
  - ribosome2019
  - ribosome2020
  - epimer1995
  - adapter
- assessment_id: resistance
  area: evidence
  topic: Twenty-three qualified CARD assertions
  outcome: supported
  summary: All 23 exported edges match the official ontology with honest database
    evidence typing. Their individual functional literatures were not exhaustively
    reassessed, and structural binding data do not independently validate every determinant,
    species or allele. No unsupported activity or resistance measurements are added.
  target_ids:
  - CHEBI:474014
  evidence_ids:
  - native
  - owners
  - card
  - search
  - adapter
- assessment_id: clinical
  area: evidence
  topic: Historical approval versus later regulatory withdrawal
  outcome: concern
  summary: The product identity, original approval date and discontinued marketing
    are correct. The exact application was subsequently withdrawn in 2007; an unqualified
    APPROVED regulatory summary omits this controlling event. Preserve the historical
    facts while adding withdrawal qualification through maintained event/overlay handling.
    No safety-based withdrawal or worldwide status is inferred.
  target_ids:
  - CHEBI:474014
  evidence_ids:
  - fda-history
  - withdrawal
  - earlier-correction
  - owners
- assessment_id: provenance
  area: provenance
  topic: Generated ownership, source citation depth and optional completeness
  outcome: supported
  summary: All native fields and history events were assessed against their actual
    source owners. The only adopted compound citation is a review read at indexed-abstract
    depth. Primary follow-up supports chemical/activity context with stated experimental
    boundaries. Optional quantitative activity, producer, mode, target-scope or graph
    additions are not defects merely because absent.
  target_ids:
  - CHEBI:474014
  evidence_ids:
  - owners
  - adopted
  - synthesis1991
  - search
  - validation
findings:
- finding_id: F1
  issue_key: dirithromycin-fda-050678-withdrawn-approval-summary
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Qualify the regulatory summary with the exact 2007 approval withdrawal
  description: clinical_status is APPROVED without historical qualification even though
    the official 2007 notice withdraws NDA 50–678 for this exact Dynabac delayed-release
    product effective 2007-12-07. The native original 1995 approval date/AP event
    and discontinued/currently_marketed=false fields are correct and should remain.
    The seeder converts an approved original into an unqualified summary without later-event
    handling. This is a missing formal regulatory qualification, not an inference
    from off-market status or a claim of safety withdrawal. The erroneous 1997 withdrawal
    was corrected and is not the basis of this finding.
  target_ids:
  - CHEBI:474014
  field_paths:
  - clinical_status
  - clinical_status_assertions[0]
  evidence_ids:
  - fda-history
  - withdrawal
  - earlier-correction
  - owners
  rule_id: 'Clinical-status checklist: jurisdiction/product regulatory facts and provenance;
    ClinicalStatusEnum WITHDRAWN; clinical_status regulatory/use semantics'
  native_severity: major
  normalization_reason: A positively verified later withdrawal of the exact application
    makes the standalone regulatory summary materially incomplete. Historical approval
    evidence remains accurate and must not be replaced wholesale.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/fda_clinical_status.tsv
    role: Reproducible approved-original product inventory
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: Historical approval selection and regulatory event/withdrawal handling
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Clinical summary and product assertion generation
- finding_id: F2
  issue_key: dirithromycin-card-p-site-versus-npet-grounding
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile the precise P-site target label with directly observed exit-tunnel
    binding
  description: The native molecular target labels the 50S P-site as the direct-binding
    site. It accurately states that CARD supplied this relation and that primary evidence
    is needed. Independently inspected intact-dirithromycin structures from T. thermophilus
    and E. coli instead locate the compound in the nascent peptide exit tunnel while
    A/P-site tRNAs remain bound. Preserve the database assertion as provenance, but
    qualify its precise site rather than promote it to a primary P-site observation.
    This finding rests on positive exact-compound localization, not merely missing
    evidence.
  target_ids:
  - CHEBI:474014
  field_paths:
  - molecular_targets[0].target_id
  - molecular_targets[0].target_label
  - molecular_targets[0].experimental_context
  evidence_ids:
  - native
  - owners
  - card
  - ribosome2019
  - ribosome2020
  - identity
  rule_id: Review checklist exact target grounding, direct evidence and preservation
    of source conflicts
  native_severity: major
  normalization_reason: The claimed site is more specific than the 50S complex and
    differs from two directly observed exact-drug binding locations. Existing evidence-needed
    qualification prevents false primary attribution, but does not remove the positive
    site-grounding conflict.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Imported drug-specific target relation
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Target relation/type interpretation
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible source qualification and curated target merge
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/dirithromycin.yaml
    role: Curator-owned exact primary target evidence additions
actions:
- action_id: A1
  description: Add maintained application-level withdrawal/event qualification and
    derive the regulatory summary without erasing historical approval.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:474014
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/fda_clinical_status.tsv
    role: Reproducible approved-original product inventory
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: Historical approval selection and regulatory event/withdrawal handling
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Clinical summary and product assertion generation
  acceptance_checks:
  - Capture NDA 050678, Dynabac delayed-release product,2007-12-07 effective withdrawal
    and official E7-21886 source with separate retrieval/version provenance. Preserve
    original 1995-06-19 approval/AP and discontinued marketing facts.
  - Distinguish the corrected 1997 erroneous withdrawal from the valid 2007 notice.
    Do not label this a safety/efficacy withdrawal or assume worldwide nonapproval.
  - Apply an explicit maintained withdrawal overlay/event rule rather than rewriting
    generated YAML. Regenerate and verify summary/event consistency, focused schema/strict
    checks and corpus reproduction.
- action_id: A2
  description: Qualify the drug-specific imported P-site relation and, if authorized,
    add the exact primary ribosome target at supported scope.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:474014
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Imported drug-specific target relation
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Target relation/type interpretation
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible source qualification and curated target merge
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/dirithromycin.yaml
    role: Curator-owned exact primary target evidence additions
  acceptance_checks:
  - Retain the original CARD relation and evidence-needed provenance while explicitly
    reconciling the NPET structural evidence; do not relabel the old database citation
    as primary.
  - Represent the 50S/23S-rRNA exit-tunnel target with claim-level 2019/2020 evidence
    and species/structural context. Do not promote the thermophilic uL4 side-chain
    contact to all bacteria or a proposed steric mechanism to a measured result.
  - Use a drug-specific maintained source qualification or narrowly justified transform;
    a global change to ARO3000757 requires separate review of every affected record.
    Preserve parent/metabolite/epimer assay boundaries and validate regenerated output.
limitations:
- LINCS LSM-5636 was not independently readable (HTTP 500), so that exact cross-reference
  remains ChEBI-attested. Beilstein 4225019 was not checked in a paid registry. DrugBank
  returned 403 directly and only a landing shell via web; the drug-level link resolves
  but its full content was not inspected.
- The sole adopted lead 7683018 is a review; its entire available indexed abstract,
  marked truncated at 250 words, was read. It is not full-text primary target evidence.
- The 1991 primary paper was reviewed at complete-abstract plus selected original
  pages 1116–1118 depth, including synthesis, structures, NMR table and early methods.
  Remaining MIC/MBC and animal-result tables were not assessed, and no new numerical
  observation is curated. The 1995 study was read at complete-abstract depth; PMC
  PDF returned challenge HTML and the alternate public archive returned 404.
- The 2019 and 2020 main articles were read completely and selected main figures visually
  inspected; their supplementary tables, movie, raw diffraction/cryo-EM data and dose-response
  fits were not independently reprocessed. The 2020 apparent-affinity and luciferase
  assays do not by themselves isolate every hydrolysis contribution during incubation;
  the intact structural ligand and the earlier conditional hydrolysis-minimized experiment
  are kept distinct.
- The 1997 supplemental approval letter was read in full as scans and supports historical
  indications; the complete final printed product label was not obtained. The 2007
  withdrawal notice was read at exact relevant scope and table visually inspected.
  The finding addresses this US application only, with no inference of safety/efficacy
  withdrawal or current status in other jurisdictions.
- All 23 database resistance assertions were checked against current official ARO,
  but individual original functional studies for all determinants were not exhaustively
  read. Negative structured-expression searches are not negative biological evidence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native scientific-status promotion is implied. Regulatory and target follow-up
  belongs to maintained source/qualification owners; optional evidence enrichment
  remains distinct from established findings.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
