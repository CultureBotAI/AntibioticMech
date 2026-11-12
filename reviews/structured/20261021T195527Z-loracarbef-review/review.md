# Loracarbef: supported carbacephem with hydrate and opened-ligand exact-reference conflicts

- Review: 20261021T195527Z-loracarbef-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T19:32:14Z
- Finished UTC: 2026-10-21T19:55:27Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native three-centre neutral carbacephem, antibacterial use and qualified PBP target are supported. Two major exact-reference defects identify a monohydrate and an opened β-lactam component instead of the intact native compound. Two minor naming defects concern a cepham-based systematic synonym and Lorabid brand typing. Primary experiments support activity and target engagement without transferring siderophore-conjugate potency, bulk hydrate identity or biochemical affinities across assays.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 608; one whole native record. All thirteen original input hashes were verified unchanged before assessment. Actual ARO inventory, target-edge and target-role owners were appended, giving sixteen captured inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:47544 | data/antibiotics/antibacterial/loracarbef.yaml | generated | loracarbef |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:47544 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:47544 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:47544 | Actual focused execution exited 0. |
| Independent exact chemical-reference comparison | passed | False | CHEBI:47544 | Native, ChEBI, PubChem, HMDB depositor and KEGG graphs agree. ChEMBL hydrate and CCD opened-form discrepancies were reproduced in all available isomeric serializations; the ChEMBL parent agrees with native. The carbacephem parent matches as a chiral substructure. |
| Authoritative full QC | failed | True | CHEBI:47544 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:47544 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:47544 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:47544 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:47544 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:47544 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:47544 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:47544 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:47544 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Native entity and chemical representations

identity: supported. Targets: CHEBI:47544.

The neutral intact three-centre native graph is valid and agrees with ChEBI, PubChem, HMDB source deposit and KEGG. Explicit neutral/zwitterion representation boundaries are preserved. Neither conflicting external graph warrants changing native chemistry.

### Exact references versus hydrate and enzyme-bound component

grounding: concern. Targets: CHEBI:47544.

ChEMBL1200610 denotes the monohydrate and CCD LOR the opened component of a covalent AmpC complex. Both violate exact structure equivalence. The matching ChEMBL parent is a supported candidate for source adjudication; drug and patent references retain broader scopes.

### Systematic synonym and brand typing

grounding: concern. Targets: CHEBI:47544.

The unqualified cepham name retains a sulfur-parent implication and should be corrected or withheld. Lorabid is explicitly a trade name. The correct first systematic name, native graph and carba definition remain consistent.

### Chemical parent, pharmacological class and roles

grounding: supported. Targets: CHEBI:47544.

The carbacephem parent structurally matches the native molecule. The broader second-generation cephalosporin grouping is conventional pharmacological usage supported by sources; it does not make the actual molecule sulfur-containing. Both antimicrobial and antibacterial-drug roles are supported.

### Synthesis, carbon replacement and infection treatment

evidence: supported. Targets: CHEBI:47544.

Original chemistry/activity, clinical trial and official historical-label evidence support the description. Broad Gram-positive/negative use does not assert every strain is susceptible or a current approval state. Patent enzyme-assisted synthesis is not a producer claim.

### PBP binding and assay scope

evidence: supported. Targets: CHEBI:47544.

The qualified family-level target is corroborated by original membrane and purified-protein competition assays. Differences among PBP species, reporter conditions and parent/conjugate forms are preserved. Optional addition of primary evidence is useful but its current absence is not a defect.

### Antibacterial experiments and exact material limits

evidence: supported. Targets: CHEBI:47544.

Exact-name studies support growth inhibition against specified Gram-positive and Gram-negative strains, with clear resistant-strain limits. Monohydrate, unspecified Kyowa material and gifted Lorabid are not automatically interchangeable bulk preparations for numerical curation.

### Source, history and adopted evidence

provenance: supported. Targets: CHEBI:47544.

Complete native and maintained source rows were inspected, all seven adopted PMIDs dispositioned, and actual source-owner hashes appended without replacing originals. Imported assertions retain correct database qualifiers.

### Optional data and inaccessible reference boundaries

completeness: unknown. Targets: CHEBI:47544.

The review covers every native field, but direct HMDB and LINCS/Reaxys current graphs remain inaccessible or uninspected. HMDB own deposit agrees. No missing optional resistance, activity, clinical, producer, dataset or graph object is scored as an error.

## Findings

### F1: Replace or qualify the monohydrate exact reference

major / open / confirmed; issue key: loracarbef-chembl1200610-monohydrate-exact-xref.

Native xrefs[6] CHEMBL1200610 has a separate water component and monohydrate formula/key in three independently parsed representations. It is not the unhydrated native chemical entity. Its explicit parent CHEMBL1013 matches native and is a concrete candidate for maintained source correction. Preserve the native graph.

### F2: Do not equate the opened CCD component with intact loracarbef

major / open / confirmed; issue key: loracarbef-ccd-lor-opened-form-exact-xref.

Native xrefs[4] LOR is officially an opened-form component in the covalently acylated AmpC complex 1FCN. It has different formula and connectivity, reproduced by its InChI and both isomeric SMILES. Preserve it only as appropriately scoped experimental/deposition context rather than exact molecular equivalence.

### F3: Use a carbacephem-consistent systematic synonym

minor / open / confirmed; issue key: loracarbef-systematic-synonym-missing-carba-replacement.

Native synonyms[2] uses a didehydrocepham parent without specifying the carbon-for-sulfur replacement. Official cepham chemistry contains sulfur, whereas the native graph and correct systematic synonym are sulfur-free. Repair or withhold this redundant name through source handling; do not change the structure.

### F4: Type Lorabid as a brand name

minor / open / confirmed; issue key: loracarbef-lorabid-brand-exact-synonym.

The FDA explicitly calls Lorabid the trade name for the oral suspension and capsule products. Native synonyms[4] must retain that product scope rather than EXACT_SYNONYM. Preserve the alias for search as BRAND_NAME.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate the two exact-reference conflicts in maintained inputs.

- Retained exact references must reproduce the intact neutral three-centre graph. Verify CHEMBL1013 as the replacement candidate and retain CHEMBL1200610 only with explicit hydrate scope if useful.
- Remove CCD LOR from exact equivalence or represent its opened covalent-complex role through an appropriate non-equivalence object. Do not silently substitute the opened graph into native chemistry.
- Regenerate from maintained source policy and rerun schema, strict, chemical identity and source-reproduction checks.

### A2

Correct the two naming scopes while preserving useful aliases.

- Withhold or correct the cepham-based name to specify the carbacephem replacement, retaining the already correct systematic name and graph.
- Emit Lorabid as BRAND_NAME with source attribution. Use existing maintained exclusions/typing or explicitly extend the mapping if needed; do not patch generated YAML.
- Verify reseeding preserves the corrected aliases and all supported roles.

### A3

Use the inspected originals for optional target and activity enrichment.

- Keep membrane radiobenzylpenicillin and Bocillin FL competition IC50 distinct from equilibrium Kd, direct transpeptidation rates and whole-cell MIC. Preserve organism, strain and preparation.
- Do not transfer BLOR conjugate potency or uptake properties to unconjugated loracarbef. Preserve the 1989 unspecified bulk form, 1993 monohydrate and 2025 gifted Lorabid material limitations.
- Keep clinical evaluability denominators and historical indications separate from current approval/marketing status. Do not infer a natural producer from enzyme-assisted synthetic preparation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/loracarbef.yaml; Entire native record: definition, all six synonyms, two parents/roles, eight exact references, three drug references, two patent links, source concepts, target and five history events. | supports | The SEEDED EXACT record denotes neutral C16H16ClN3O4, key JAPHQRWPEGVNBT-UTUOFQBUSA-N, with three assigned centres. The PBP family is a PROTEIN DIRECT_BINDING_TARGET, explicitly qualified as CARD/ARO evidence with PRIMARY_EVIDENCE_NEEDED and no organism or assay. No numeric activity, resistance, clinical, producer, dataset or causal-graph object is asserted. |
| owners | data/raw/chebi_antimicrobials.tsv:883; data/raw/aro_antibiotics.tsv:313; data/raw/aro_target_edges.tsv:251; conf/aro_target_roles.tsv; Complete exact source rows and relevant extraction/seeding branches; schema exact/drug reference semantics and synonym handling inspected. | supports | ChEBI supplies the graph, definition and six adopted leads; ARO adds two citation leads, one overlapping, plus the class, Lorabid alias and PBP edge. There are seven distinct adopted PMIDs. The target-role map supplies the protein/direct-binding type. The additional ChEBI zwitterion row returned by the shared-key search is contextual, not the selected source identity. Original hashes were preserved. |
| local-search | /private/tmp/am-review-session/608-local-hits.txt; Ignored-inclusive and hidden-inclusive label, slug and identifier search; complete returned path inventory read. | context_only | Native/raw/generated paths, separate loracarbef anion and zwitterion records, and historical research ledgers were found. The latter were leads only. A shared Standard InChI key does not collapse the explicit neutral/zwitterionic representation boundary. |
| native-chemistry | CHEBI:47544; PubChem:5284585; KEGG:D08143; Complete current entries and independent parsing of ChEBI SMILES/InChI/molfile, PubChem strings and KEGG molfile. | supports | All reproduce the intact neutral three-centre native graph and formula. Charge and masses agree at source precision. Public authorities corroborate CAS 76470-66-1; a licensed registry was not consulted. KEGG is correctly a drug-level reference even though its present graph matches. |
| hmdb | HMDB:HMDB0014590; PubChem Substance:348283123 version2; Official HMDB depositor metadata and SDF via PubChem, independently parsed; direct HMDB XML routes returned 403. | supports | The deposit explicitly identifies HMDB0014590 and links CID5284585. Its own structure reproduces the native full key and all three centres. This is source-deposited corroboration, not a claim that the inaccessible live HMDB page was inspected. |
| chembl-hydrate | ChEMBL:CHEMBL1200610; ChEMBL:CHEMBL1013; Complete current records, hydrate SMILES/InChI/molfile and parent strings independently parsed. | refutes | The exact native accession CHEMBL1200610 is loracarbef monohydrate, C16H18ClN3O5, key GPYKKBAAPVOCIW-HSASPSRMSA-N. Its organic component matches native; its separate water component does not. The explicitly identified parent CHEMBL1013 reproduces the neutral native graph. A parent-child drug hierarchy does not make both accessions exact equivalents. |
| ccd-open | pdb-ccd:LOR; PDB:1FCN; DOI:10.1021/ja001676x; Complete official CCD response/CIF and RCSB entry metadata; three isomeric CCD serializations independently parsed. | refutes | CCD LOR is explicitly named LORACABEF (Open form), formula C16H18ClN3O4 and key ANBZXHFIDXQFOW-JHJVBQTASA-N. Its β-lactam bond connectivity differs from the intact native compound. Entry 1FCN describes E. coli AmpC Q120L/Y150E covalently acylated with loracarbef and cites the 2000 primary study. This opened component can supply bound-state context but cannot be an exact free-compound xref. The original crystallography paper was not read in full. |
| diagnostic | /private/tmp/am-review-session/608-authority-chemistry.json; Independent graph, component and stereochemical calculations. | supports | All seventeen compared chemical serializations are valid. The hydrate discrepancy is a water component; the CCD discrepancy is opened-ring constitution. The native isomer matches the carbacephem parent as a chiral substructure after generic substituent conversion. These checks support retaining the correct native graph, not modifying it to fit either conflicting external reference. |
| scaffold-name | CHEBI:35993; CHEBI:55504; CHEBI:47544; Complete cepham and carbacephem entries, including structures and systematic names. | refutes | Cepham explicitly contains sulfur and has formula C6H9NOS. Carbacephems replace that sulfur with carbon. Native synonym[2] uses an unqualified didehydrocepham parent without the carba/dethia replacement and therefore conflicts with the sulfur-free graph and correct first systematic name. The generic carbacephem parent is appropriate. This does not imply the native structure is cefaclor. |
| aro | https://purl.obolibrary.org/obo/aro.obo; Current ARO3004016, ARO3009106, ARO0000032 and the relevant ARO3000749 definition/direct drug edge read. | supports | Current ARO reproduces the Lorabid exact alias, adopted citations, clinical second-generation cephalosporin grouping and PBP assertion. Carbacephem is the precise chemical class; conventional pharmacological cephalosporin grouping is supported by clinical sources and is not itself scored as a wrong-scaffold defect. The target remains explicitly database qualified. |
| roles | CHEBI:33281; CHEBI:36047; Official antimicrobial-agent and antibacterial-drug definitions read. | supports | The roles concern antimicrobial effects and use to treat or prevent bacterial infection. They are consistent with the original growth, mouse and clinical experiments. They do not assert universal bacterial susceptibility or a particular formulation identity. |
| brand-fda | https://www.accessdata.fda.gov/drugsatfda_docs/nda/96/050667ap.pdf; Original 1996 supplemental approval letter and selected medical-officer review pages; PDF page 7 trade-name entry viewed. | refutes | The FDA record explicitly separates generic Loracarbef from trade Lorabid oral suspension/Pulvules and identifies the carbacephem class. It documents pediatric sinusitis labeling and prior sinusitis/otitis use. This verifies brand typing and historical drug use, not present regulatory or marketing status. |
| other-drug-refs | DrugCentral:1603; DrugBank:DB00447; KEGG:D08143; LINCS:LSM-5429; Reaxys:3631282; DrugCentral identity section and complete KEGG entry read; adopted/current ChEBI associations checked for inaccessible references. | context_only | DrugCentral identifies the neutral formula and CAS while also listing hydrate and brand associations, appropriate for a drug-level reference. DrugBank returned 403, LINCS returned 500 and Reaxys was not inspected through paid access. Their current exact chemistry is not claimed independently verified. These access limits are not evidence of a mismatch. |
| patents | EP0014476A1; US4708956A; Patent descriptions of scaffold/stereochemical scope, selected exact preparations including US Example 2, and claim 9 read; not all examples or raw spectra reviewed. | context_only | Both documents concern synthetic carbacephem analogues. US Example 2 distinguishes the two ring diastereomers with an R phenylglycine sidechain and identifies the less-polar positive-rotation material as 6R,7S; the text says this absolute assignment was assumed from properties/activity. The EP source similarly states an assumed absolute configuration. These are relevant document links and synthesis context, not independent modern absolute-hand proof, nor evidence that the synthetic compound has a natural producer. |
| adapter | iModulonDB via kg-microbe-sources; Catalog and PBP/gene searches executed before open-ended mechanism follow-up; all five commands exited 0. | context_only | E. coli precise1k matches b2430 yfeW, b0635 mrdA and b0084 ftsI; S. aureus staph_precise108 returned PBP-related genes as well as beta-lactamase/regulator context. No relevant iModulon was found. These gene matches do not prove drug binding or transfer E. coli/S. aureus experiments to the taxon-agnostic family. |
| primary1989-identity | PMID:2621166; DOI:10.7164/antibiotics.42.1844; Original ten-page paper main text read; Figures 1 and 3 and Tables 1/2 viewed, with Table 3 and Table 4 text assessed. | supports | The paper explicitly identifies KT3777 as LY163892 and the carbon-for-sulfur analogue of cefaclor. Kyowa supplied synthetic material. Figure 1 depicts the intact sulfur-free scaffold but is not a complete absolute-stereo determination. The bulk hydrate and purity are not stated, so its mass-based assays should not be silently assigned to an anhydrous solid preparation. |
| primary1989-activity | PMID:2621166; DOI:10.7164/antibiotics.42.1844; Original agar-dilution Methods, Tables1-3 and Results, with time-kill and mouse Methods/Results read. | supports | Agar dilution used approximately 1e4 CFU per spot and mostly 18 h at 37°C, with organism-specific media/incubation exceptions. Table 1 gives S. aureus FDA209P JC-1 MIC 0.2 µg/mL and E. coli NIHJ JC-2 MIC 0.78 µg/mL, while MRSA J555 and P. aeruginosa No.1 exceeded 100 µg/mL. Clinical-isolate distributions and mouse protection are separate endpoints. Time-kill results are strain/concentration specific and must not be generalized into universal bactericidal efficacy. |
| primary1989-pbp | PMID:2621166; DOI:10.7164/antibiotics.42.1844; Original membrane preparation/competition Methods, Figure 3 and p1851 binding Results. | supports | E. coli NIHJ JC-2 membranes were preincubated 10 min at 30°C with drug, followed by 14C-benzylpenicillin for 10 min. Fluorographic competition IC50 values were 2.7 µg/mL for PBP1A, 18.6 for 1B, 3.6 for 3 and 2.6 for 4, with poor 2/5/6 interaction. These are inhibition of tracer labeling, not equilibrium Kd. They support PBP engagement without identifying every PBP as equally important for bacterial killing. |
| primary1993 | DOI:10.11250/chemotherapy1953.41.Supplement3_51; Selected original Japanese introduction, material/PBP Methods and binding Results, plus complete English abstract read; not the entire Japanese article. | supports | The paper explicitly names loracarbef monohydrate and uses a Kyowa synthetic reference standard. It reports E. coli NIHJ JC-2 radiobenzylpenicillin competition with the same PBP profile. This corroborates material and target scope but is not an independent proof that every earlier or later assay used the monohydrate. Its numeric tables were not all visually audited. |
| primary2025-pbp | PMID:41198856; DOI:10.1038/s42003-025-08898-9; PMC12592502; Original PBP Results, relevant preparation/assay Methods and full Discussion read; Figures 4/5 viewed; complete SI Table S8 read. | supports | Unconjugated LOR is experimentally distinct from bis-catechol-loracarbef BLOR. Apparent Bocillin FL competition IC50 was 14.9±4.3 µM for E. coli MC4100 membrane PBP3. Purified P. aeruginosa ATCC27853 PBP3 gave 8.6±3.6 µM, while its membrane assay gave &gt;50 µM. Incubation and reporter concentration differ between preparations; these values are not Kd. The large BLOR gains are not native-parent potency. |
| primary2025-material-activity | PMID:41198856; DOI:10.1038/s42003-025-08898-9; Original Introduction, selected susceptibility/beta-lactamase Results and Tables 1/3, growth/MIC Methods; SI p16 general materials and p20 BLOR synthesis read. | supports | Table 1 reports LOR MIC 3.1 µM for E. coli ATCC25922 in cation-adjusted Mueller-Hinton broth and 1.6 µM in iron-depleted broth; P. aeruginosa ATCC27853 and A. baumannii ATCC19606 exceeded 200 µM in both. SI identifies Lorabid as an Eli Lilly gift; the inspected parent material description does not independently resolve hydrate content or mass normalization. Conjugate characterization is not proof of parent purity. Beta-lactamase substrate hydrolysis is separate from the antibacterial PBP target. |
| clinical1991 | PMID:2069382; DOI:10.1128/AAC.35.4.750; PMC245091; All three original scanned pages 750–752 read, including both tables. | supports | This randomized double-blind trial enrolled 108 college women with acute urinary infections, comparing seven days of loracarbef 200 mg once daily with cefaclor 250 mg three times daily. Early bacteriological cure was 44/46 versus 46/51 among patients completing follow-up, not 96% of all randomized participants. It supports historical infection treatment, with substantial evaluability/follow-up limits and no explicit bulk hydrate identification. It does not establish broad current prescribing recommendations. |
| adopted-primary | PMID:1553350 DOI:10.1023/A:1018949709797; PMID:3501757 DOI:10.1007/BF02014248; PMID:9131470 DOI:10.1002/(SICI)1099-1352(199607)9:4&lt;287::AID-JMR340&gt;3.0.CO;2-L; All three complete indexed original abstracts read; 1987 publisher abstract also inspected, full article requires purchase. | context_only | The 1992 pharmaceutical paper explicitly studies hydrated crystalline forms and monohydrate solution properties. The 1987 original concerns beta-lactamase hydrolysis/inhibition, not direct PBP binding. The 1996 allergen paper examines cefaclor-reactive IgE and fine structural recognition; its abstract does not establish exact loracarbef antibacterial mechanism. No clinical or allergy numerical result is transferred from these abstract-only leads. |
| adopted-reviews | PMID:1621740; PMID:1621742; PMID:8453172; PMID:29017833; All four complete indexed abstracts read; publication types verified as reviews. | context_only | These cover pharmacokinetics, pooled clinical safety, therapeutic overview and beta-lactam allergy cross-reactivity. They support broad historical drug context and identify limitations in early clinical trials. They are secondary summaries, not primary proof of exact PBP binding, hydrate identity, universal susceptibility or safety for an individual patient. |
| bounded-search | Europe PMC TITLE_ABS loracarbef and LY163892/KT3777 mechanism/activity queries; official primary follow-up; First 100 of 205 loracarbef result titles read, plus all returned focused research-code abstracts; all seven adopted leads dispositioned. | context_only | Relevant originals were followed up for scaffold, susceptibility, PBP competition and clinical use. Siderophore derivatives, host MAO-B/AChE repurposing, transporter pharmacokinetics and beta-lactamase substrate studies were not collapsed into one antibacterial causal mechanism. Searches and free-access retrieval were bounded. |

## Limits And Additional Notes

- The 1989 original main text and all table text were read, with selected original pages viewed for structure, susceptibility and PBP fluorography. Not every figure or raw spectrum was independently reprocessed; its bulk hydrate/purity was unspecified.
- The 1993 original was read only in relevant material/PBP sections and its complete English abstract. The rest of the Japanese article and every numeric table were not independently audited.
- The 2025 original was read in Introduction, selected susceptibility/beta-lactamase/PBP Results, relevant Methods and full Discussion; Figures 4/5 were viewed. SI Table S8 and material/synthesis sections on pp16/20 were read. Uncropped gels, all spectra and unrelated uptake/genetic experiments were not fully audited.
- The 2025 parent material is described as gifted Lorabid. The inspected text does not independently establish hydrate content, parent purity or mass normalization. The characterized conjugate purity statement is not automatically a parent-material measurement.
- The 1991 clinical trial was read in all three scanned pages. The FDA 1996 file was read only in the approval letter and relevant medical-review sections, not as a complete current regulatory audit.
- All seven adopted citations were read at complete-abstract depth. Four are secondary reviews. The 1987 enzyme article remained purchase-gated beyond its official abstract; the 1992 pharmaceutical and 1996 IgE originals were not obtained in full.
- Patent inspection was limited to relevant descriptions, preparations and claims. Their absolute ring assignment is explicitly assumed; no independent modern crystallographic hand determination is claimed. The 2000 AmpC paper was identified through official deposition metadata but not read in full.
- Direct HMDB returned 403; its own PubChem deposit agrees with native. LINCS returned 500, DrugBank 403 and Reaxys was not accessed through paid services. Current exact chemistry for inaccessible LINCS/Reaxys remains unverified.
- The literature search was bounded and did not exhaust all 205 loracarbef results. Optional enrichment gaps are not native defects; source assertions are not upgraded solely by deterministic validation.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All thirteen initial input hashes are preserved, with actual owners appended to sixteen. Retrieval manifests retain real URLs, UTC timestamps, statuses and hashes.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T195527Z-loracarbef-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Loracarbef: supported carbacephem with hydrate and opened-ligand exact-reference
  conflicts'
started_at: '2026-10-21T19:32:14Z'
finished_at: '2026-10-21T19:55:27Z'
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
summary: The native three-centre neutral carbacephem, antibacterial use and qualified
  PBP target are supported. Two major exact-reference defects identify a monohydrate
  and an opened β-lactam component instead of the intact native compound. Two minor
  naming defects concern a cepham-based systematic synonym and Lorabid brand typing.
  Primary experiments support activity and target engagement without transferring
  siderophore-conjugate potency, bulk hydrate identity or biochemical affinities across
  assays.
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
  - path: data/antibiotics/antibacterial/loracarbef.yaml
    sha256: 1c48e0f575cb6a26e023094ba7e928c6110a7c8ee79c0ba43469ca8e812f633b
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 25f0d80c0bf26da7741a1514a5e1759dde484ab054f0f56df7938bdda8383a91
    role: context
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
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
- target_id: CHEBI:47544
  path: data/antibiotics/antibacterial/loracarbef.yaml
  label: loracarbef
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI/ARO source extraction and class mapping
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Actual maintained source input for the record
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 608; one whole native record. All thirteen original input
    hashes were verified unchanged before assessment. Actual ARO inventory, target-edge
    and target-role owners were appended, giving sixteen captured inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:47544
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:47544
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    608
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:47544
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/loracarbef.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:47544
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/loracarbef.yaml --out /private/tmp/am-review-session/608-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-comparison
  name: Independent exact chemical-reference comparison
  status: passed
  required: false
  summary: Native, ChEBI, PubChem, HMDB depositor and KEGG graphs agree. ChEMBL hydrate
    and CCD opened-form discrepancies were reproduced in all available isomeric serializations;
    the ChEMBL parent agrees with native. The carbacephem parent matches as a chiral
    substructure.
  target_ids:
  - CHEBI:47544
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/608-compare.py
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
  - CHEBI:47544
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
  - CHEBI:47544
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
  - CHEBI:47544
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
  - CHEBI:47544
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
  - CHEBI:47544
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
  - CHEBI:47544
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
  - CHEBI:47544
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
  - CHEBI:47544
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
  - CHEBI:47544
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/loracarbef.yaml
  locator: 'Entire native record: definition, all six synonyms, two parents/roles,
    eight exact references, three drug references, two patent links, source concepts,
    target and five history events.'
  accessed_at: '2026-10-21T19:52:43Z'
  support: supports
  summary: The SEEDED EXACT record denotes neutral C16H16ClN3O4, key JAPHQRWPEGVNBT-UTUOFQBUSA-N,
    with three assigned centres. The PBP family is a PROTEIN DIRECT_BINDING_TARGET,
    explicitly qualified as CARD/ARO evidence with PRIMARY_EVIDENCE_NEEDED and no
    organism or assay. No numeric activity, resistance, clinical, producer, dataset
    or causal-graph object is asserted.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv:883; data/raw/aro_antibiotics.tsv:313;
    data/raw/aro_target_edges.tsv:251; conf/aro_target_roles.tsv
  locator: Complete exact source rows and relevant extraction/seeding branches; schema
    exact/drug reference semantics and synonym handling inspected.
  accessed_at: '2026-10-21T19:52:43Z'
  support: supports
  summary: ChEBI supplies the graph, definition and six adopted leads; ARO adds two
    citation leads, one overlapping, plus the class, Lorabid alias and PBP edge. There
    are seven distinct adopted PMIDs. The target-role map supplies the protein/direct-binding
    type. The additional ChEBI zwitterion row returned by the shared-key search is
    contextual, not the selected source identity. Original hashes were preserved.
  snapshot_sha256: a8559da8d6a640b7b9e67293ab53f2745a11496268e2432bbd0c8cbd6d3a0664
- evidence_id: local-search
  kind: search
  reference: /private/tmp/am-review-session/608-local-hits.txt
  locator: Ignored-inclusive and hidden-inclusive label, slug and identifier search;
    complete returned path inventory read.
  accessed_at: '2026-10-21T19:52:43Z'
  support: context_only
  summary: Native/raw/generated paths, separate loracarbef anion and zwitterion records,
    and historical research ledgers were found. The latter were leads only. A shared
    Standard InChI key does not collapse the explicit neutral/zwitterionic representation
    boundary.
  snapshot_sha256: db0bd763193cd6b51ffbaeeb73a82f94b4fe16b7fd64230f52f255115f8eb12b
  search_scope: 2026-10-21; exact loracarbef, CHEBI47544, ARO3004016, native slug/key
    and research codes LY163892/KT3777. Local search included ignored and hidden files.
    Europe PMC returned 205 loracarbef records, first 100 titles read, with focused
    code/activity/target abstracts and selected official primary follow-up.
- evidence_id: native-chemistry
  kind: database
  reference: CHEBI:47544; PubChem:5284585; KEGG:D08143
  locator: Complete current entries and independent parsing of ChEBI SMILES/InChI/molfile,
    PubChem strings and KEGG molfile.
  accessed_at: '2026-10-21T19:41:49Z'
  support: supports
  summary: All reproduce the intact neutral three-centre native graph and formula.
    Charge and masses agree at source precision. Public authorities corroborate CAS
    76470-66-1; a licensed registry was not consulted. KEGG is correctly a drug-level
    reference even though its present graph matches.
  snapshot_sha256: 7e3fd05516c98d16caf2b83cbbb68f2f09b070c0e1910ab69e25a1db370d6ebd
- evidence_id: hmdb
  kind: database
  reference: HMDB:HMDB0014590; PubChem Substance:348283123 version2
  locator: Official HMDB depositor metadata and SDF via PubChem, independently parsed;
    direct HMDB XML routes returned 403.
  accessed_at: '2026-10-21T19:48:19Z'
  support: supports
  summary: The deposit explicitly identifies HMDB0014590 and links CID5284585. Its
    own structure reproduces the native full key and all three centres. This is source-deposited
    corroboration, not a claim that the inaccessible live HMDB page was inspected.
  snapshot_sha256: 2710d8e0a03efa54015e58be1beadbc8ce97d211a915a14d9d934c58bd19070d
- evidence_id: chembl-hydrate
  kind: database
  reference: ChEMBL:CHEMBL1200610; ChEMBL:CHEMBL1013
  locator: Complete current records, hydrate SMILES/InChI/molfile and parent strings
    independently parsed.
  accessed_at: '2026-10-21T19:41:50Z'
  support: refutes
  summary: The exact native accession CHEMBL1200610 is loracarbef monohydrate, C16H18ClN3O5,
    key GPYKKBAAPVOCIW-HSASPSRMSA-N. Its organic component matches native; its separate
    water component does not. The explicitly identified parent CHEMBL1013 reproduces
    the neutral native graph. A parent-child drug hierarchy does not make both accessions
    exact equivalents.
  snapshot_sha256: a887895de601bd77a487347f7d017321db6f00f84407e6423af3797d758ea27e
- evidence_id: ccd-open
  kind: database
  reference: pdb-ccd:LOR; PDB:1FCN; DOI:10.1021/ja001676x
  locator: Complete official CCD response/CIF and RCSB entry metadata; three isomeric
    CCD serializations independently parsed.
  accessed_at: '2026-10-21T19:46:48Z'
  support: refutes
  summary: CCD LOR is explicitly named LORACABEF (Open form), formula C16H18ClN3O4
    and key ANBZXHFIDXQFOW-JHJVBQTASA-N. Its β-lactam bond connectivity differs from
    the intact native compound. Entry 1FCN describes E. coli AmpC Q120L/Y150E covalently
    acylated with loracarbef and cites the 2000 primary study. This opened component
    can supply bound-state context but cannot be an exact free-compound xref. The
    original crystallography paper was not read in full.
  snapshot_sha256: 66c9ea9f656b9e11103f9bb7bbbfdbd47f87b1a4d55b5568ae88c1110fb4a930
- evidence_id: diagnostic
  kind: validation
  reference: /private/tmp/am-review-session/608-authority-chemistry.json
  locator: Independent graph, component and stereochemical calculations.
  accessed_at: '2026-10-21T19:52:43Z'
  support: supports
  summary: All seventeen compared chemical serializations are valid. The hydrate discrepancy
    is a water component; the CCD discrepancy is opened-ring constitution. The native
    isomer matches the carbacephem parent as a chiral substructure after generic substituent
    conversion. These checks support retaining the correct native graph, not modifying
    it to fit either conflicting external reference.
  snapshot_sha256: a690ced15fbe9e40fdc9b825dfbe2e41cf00aa7703db650b7fc3451fa7877bbf
- evidence_id: scaffold-name
  kind: authority
  reference: CHEBI:35993; CHEBI:55504; CHEBI:47544
  locator: Complete cepham and carbacephem entries, including structures and systematic
    names.
  accessed_at: '2026-10-21T19:46:48Z'
  support: refutes
  summary: Cepham explicitly contains sulfur and has formula C6H9NOS. Carbacephems
    replace that sulfur with carbon. Native synonym[2] uses an unqualified didehydrocepham
    parent without the carba/dethia replacement and therefore conflicts with the sulfur-free
    graph and correct first systematic name. The generic carbacephem parent is appropriate.
    This does not imply the native structure is cefaclor.
  snapshot_sha256: 5916f9183cf896bdb282a24fabfaa5ba9403f4cc5ae5d0a0e6b1307f3f90496f
- evidence_id: aro
  kind: database
  reference: https://purl.obolibrary.org/obo/aro.obo
  locator: Current ARO3004016, ARO3009106, ARO0000032 and the relevant ARO3000749
    definition/direct drug edge read.
  accessed_at: '2026-10-21T15:57:42Z'
  support: supports
  summary: Current ARO reproduces the Lorabid exact alias, adopted citations, clinical
    second-generation cephalosporin grouping and PBP assertion. Carbacephem is the
    precise chemical class; conventional pharmacological cephalosporin grouping is
    supported by clinical sources and is not itself scored as a wrong-scaffold defect.
    The target remains explicitly database qualified.
  snapshot_sha256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
- evidence_id: roles
  kind: database
  reference: CHEBI:33281; CHEBI:36047
  locator: Official antimicrobial-agent and antibacterial-drug definitions read.
  accessed_at: '2026-10-21T19:46:49Z'
  support: supports
  summary: The roles concern antimicrobial effects and use to treat or prevent bacterial
    infection. They are consistent with the original growth, mouse and clinical experiments.
    They do not assert universal bacterial susceptibility or a particular formulation
    identity.
  snapshot_sha256: cd02b5e95a759d9be8d1b3a51657d5d536a2f53d43647448b69caf4de6bd737f
- evidence_id: brand-fda
  kind: authority
  reference: https://www.accessdata.fda.gov/drugsatfda_docs/nda/96/050667ap.pdf
  locator: Original 1996 supplemental approval letter and selected medical-officer
    review pages; PDF page 7 trade-name entry viewed.
  accessed_at: '2026-10-21T19:52:43Z'
  support: refutes
  summary: The FDA record explicitly separates generic Loracarbef from trade Lorabid
    oral suspension/Pulvules and identifies the carbacephem class. It documents pediatric
    sinusitis labeling and prior sinusitis/otitis use. This verifies brand typing
    and historical drug use, not present regulatory or marketing status.
  snapshot_sha256: 10054a516d881e74f8084b080c0e8a467a82e3fa4e6c42a7ccb95104852f8319
- evidence_id: other-drug-refs
  kind: database
  reference: DrugCentral:1603; DrugBank:DB00447; KEGG:D08143; LINCS:LSM-5429; Reaxys:3631282
  locator: DrugCentral identity section and complete KEGG entry read; adopted/current
    ChEBI associations checked for inaccessible references.
  accessed_at: '2026-10-21T19:41:56Z'
  support: context_only
  summary: DrugCentral identifies the neutral formula and CAS while also listing hydrate
    and brand associations, appropriate for a drug-level reference. DrugBank returned
    403, LINCS returned 500 and Reaxys was not inspected through paid access. Their
    current exact chemistry is not claimed independently verified. These access limits
    are not evidence of a mismatch.
  snapshot_sha256: f0b248885a7e1912fe7915bbaf49436e1153d19692c387b8f725a363624f9f59
- evidence_id: patents
  kind: primary_source
  reference: EP0014476A1; US4708956A
  locator: Patent descriptions of scaffold/stereochemical scope, selected exact preparations
    including US Example 2, and claim 9 read; not all examples or raw spectra reviewed.
  accessed_at: '2026-10-21T19:41:56Z'
  support: context_only
  summary: Both documents concern synthetic carbacephem analogues. US Example 2 distinguishes
    the two ring diastereomers with an R phenylglycine sidechain and identifies the
    less-polar positive-rotation material as 6R,7S; the text says this absolute assignment
    was assumed from properties/activity. The EP source similarly states an assumed
    absolute configuration. These are relevant document links and synthesis context,
    not independent modern absolute-hand proof, nor evidence that the synthetic compound
    has a natural producer.
  snapshot_sha256: 7e49dd9c3eabcd106e1ef9ed3330f1577eba830255b43e8fc3e36643f3d84e41
- evidence_id: adapter
  kind: database
  reference: iModulonDB via kg-microbe-sources
  locator: Catalog and PBP/gene searches executed before open-ended mechanism follow-up;
    all five commands exited 0.
  accessed_at: '2026-10-21T19:46:14Z'
  support: context_only
  summary: E. coli precise1k matches b2430 yfeW, b0635 mrdA and b0084 ftsI; S. aureus
    staph_precise108 returned PBP-related genes as well as beta-lactamase/regulator
    context. No relevant iModulon was found. These gene matches do not prove drug
    binding or transfer E. coli/S. aureus experiments to the taxon-agnostic family.
  snapshot_sha256: a305f1e5492f0a371ee9936711d8a2f2288569028ee6c68ca4f1061226a070fc
- evidence_id: primary1989-identity
  kind: primary_source
  reference: PMID:2621166; DOI:10.7164/antibiotics.42.1844
  locator: Original ten-page paper main text read; Figures 1 and 3 and Tables 1/2
    viewed, with Table 3 and Table 4 text assessed.
  accessed_at: '2026-10-21T19:48:19Z'
  support: supports
  summary: The paper explicitly identifies KT3777 as LY163892 and the carbon-for-sulfur
    analogue of cefaclor. Kyowa supplied synthetic material. Figure 1 depicts the
    intact sulfur-free scaffold but is not a complete absolute-stereo determination.
    The bulk hydrate and purity are not stated, so its mass-based assays should not
    be silently assigned to an anhydrous solid preparation.
  snapshot_sha256: 32f8df18c9147612efc5bef8241f226aa7be7c1ad88d83b1ae1cc4dc5ab35c2a
- evidence_id: primary1989-activity
  kind: primary_source
  reference: PMID:2621166; DOI:10.7164/antibiotics.42.1844
  locator: Original agar-dilution Methods, Tables1-3 and Results, with time-kill and
    mouse Methods/Results read.
  accessed_at: '2026-10-21T19:52:43Z'
  support: supports
  summary: Agar dilution used approximately 1e4 CFU per spot and mostly 18 h at 37°C,
    with organism-specific media/incubation exceptions. Table 1 gives S. aureus FDA209P
    JC-1 MIC 0.2 µg/mL and E. coli NIHJ JC-2 MIC 0.78 µg/mL, while MRSA J555 and P.
    aeruginosa No.1 exceeded 100 µg/mL. Clinical-isolate distributions and mouse protection
    are separate endpoints. Time-kill results are strain/concentration specific and
    must not be generalized into universal bactericidal efficacy.
  snapshot_sha256: 356643f02d21665b5a85ba0abdb332c89452ddd66b4e977b528bafe93e910f85
- evidence_id: primary1989-pbp
  kind: primary_source
  reference: PMID:2621166; DOI:10.7164/antibiotics.42.1844
  locator: Original membrane preparation/competition Methods, Figure 3 and p1851 binding
    Results.
  accessed_at: '2026-10-21T19:52:43Z'
  support: supports
  summary: E. coli NIHJ JC-2 membranes were preincubated 10 min at 30°C with drug,
    followed by 14C-benzylpenicillin for 10 min. Fluorographic competition IC50 values
    were 2.7 µg/mL for PBP1A, 18.6 for 1B, 3.6 for 3 and 2.6 for 4, with poor 2/5/6
    interaction. These are inhibition of tracer labeling, not equilibrium Kd. They
    support PBP engagement without identifying every PBP as equally important for
    bacterial killing.
  snapshot_sha256: 0480185dbbb870f21dcce49dedf3a286dd6089777dfb1bc605403f9ad39d857c
- evidence_id: primary1993
  kind: primary_source
  reference: DOI:10.11250/chemotherapy1953.41.Supplement3_51
  locator: Selected original Japanese introduction, material/PBP Methods and binding
    Results, plus complete English abstract read; not the entire Japanese article.
  accessed_at: '2026-10-21T19:46:48Z'
  support: supports
  summary: The paper explicitly names loracarbef monohydrate and uses a Kyowa synthetic
    reference standard. It reports E. coli NIHJ JC-2 radiobenzylpenicillin competition
    with the same PBP profile. This corroborates material and target scope but is
    not an independent proof that every earlier or later assay used the monohydrate.
    Its numeric tables were not all visually audited.
  snapshot_sha256: d2561585a005a9b92a423829249f72ece38c3d37c8e46eba15a7a1ecbb5f87a0
- evidence_id: primary2025-pbp
  kind: primary_source
  reference: PMID:41198856; DOI:10.1038/s42003-025-08898-9; PMC12592502
  locator: Original PBP Results, relevant preparation/assay Methods and full Discussion
    read; Figures 4/5 viewed; complete SI Table S8 read.
  accessed_at: '2026-10-21T19:47:46Z'
  support: supports
  summary: Unconjugated LOR is experimentally distinct from bis-catechol-loracarbef
    BLOR. Apparent Bocillin FL competition IC50 was 14.9±4.3 µM for E. coli MC4100
    membrane PBP3. Purified P. aeruginosa ATCC27853 PBP3 gave 8.6±3.6 µM, while its
    membrane assay gave >50 µM. Incubation and reporter concentration differ between
    preparations; these values are not Kd. The large BLOR gains are not native-parent
    potency.
  snapshot_sha256: b3ed86664db4f5c55a1e3417bc26f13f0f11d56d1004e096e6983a9d9a26f202
- evidence_id: primary2025-material-activity
  kind: primary_source
  reference: PMID:41198856; DOI:10.1038/s42003-025-08898-9
  locator: Original Introduction, selected susceptibility/beta-lactamase Results and
    Tables 1/3, growth/MIC Methods; SI p16 general materials and p20 BLOR synthesis
    read.
  accessed_at: '2026-10-21T19:48:19Z'
  support: supports
  summary: Table 1 reports LOR MIC 3.1 µM for E. coli ATCC25922 in cation-adjusted
    Mueller-Hinton broth and 1.6 µM in iron-depleted broth; P. aeruginosa ATCC27853
    and A. baumannii ATCC19606 exceeded 200 µM in both. SI identifies Lorabid as an
    Eli Lilly gift; the inspected parent material description does not independently
    resolve hydrate content or mass normalization. Conjugate characterization is not
    proof of parent purity. Beta-lactamase substrate hydrolysis is separate from the
    antibacterial PBP target.
  snapshot_sha256: aaa7db46cc448e9557e75084cb4eb211a16be0fba008f0c65f718e370d5dd7e0
- evidence_id: clinical1991
  kind: primary_source
  reference: PMID:2069382; DOI:10.1128/AAC.35.4.750; PMC245091
  locator: All three original scanned pages 750–752 read, including both tables.
  accessed_at: '2026-10-21T19:49:43Z'
  support: supports
  summary: This randomized double-blind trial enrolled 108 college women with acute
    urinary infections, comparing seven days of loracarbef 200 mg once daily with
    cefaclor 250 mg three times daily. Early bacteriological cure was 44/46 versus
    46/51 among patients completing follow-up, not 96% of all randomized participants.
    It supports historical infection treatment, with substantial evaluability/follow-up
    limits and no explicit bulk hydrate identification. It does not establish broad
    current prescribing recommendations.
  snapshot_sha256: 4ca43fd06525d109656b39d13f0c3982613a9e88e1ae9edc1541cdb64e0e539f
- evidence_id: adopted-primary
  kind: primary_source
  reference: PMID:1553350 DOI:10.1023/A:1018949709797; PMID:3501757 DOI:10.1007/BF02014248;
    PMID:9131470 DOI:10.1002/(SICI)1099-1352(199607)9:4<287::AID-JMR340>3.0.CO;2-L
  locator: All three complete indexed original abstracts read; 1987 publisher abstract
    also inspected, full article requires purchase.
  accessed_at: '2026-10-21T19:41:50Z'
  support: context_only
  summary: The 1992 pharmaceutical paper explicitly studies hydrated crystalline forms
    and monohydrate solution properties. The 1987 original concerns beta-lactamase
    hydrolysis/inhibition, not direct PBP binding. The 1996 allergen paper examines
    cefaclor-reactive IgE and fine structural recognition; its abstract does not establish
    exact loracarbef antibacterial mechanism. No clinical or allergy numerical result
    is transferred from these abstract-only leads.
  snapshot_sha256: 4578943c996a7e4adb198c0d2c5c904dcf96fc8dea6e97afde600c044041a49a
- evidence_id: adopted-reviews
  kind: database
  reference: PMID:1621740; PMID:1621742; PMID:8453172; PMID:29017833
  locator: All four complete indexed abstracts read; publication types verified as
    reviews.
  accessed_at: '2026-10-21T19:41:50Z'
  support: context_only
  summary: These cover pharmacokinetics, pooled clinical safety, therapeutic overview
    and beta-lactam allergy cross-reactivity. They support broad historical drug context
    and identify limitations in early clinical trials. They are secondary summaries,
    not primary proof of exact PBP binding, hydrate identity, universal susceptibility
    or safety for an individual patient.
  snapshot_sha256: 4578943c996a7e4adb198c0d2c5c904dcf96fc8dea6e97afde600c044041a49a
- evidence_id: bounded-search
  kind: search
  reference: Europe PMC TITLE_ABS loracarbef and LY163892/KT3777 mechanism/activity
    queries; official primary follow-up
  locator: First 100 of 205 loracarbef result titles read, plus all returned focused
    research-code abstracts; all seven adopted leads dispositioned.
  accessed_at: '2026-10-21T19:41:51Z'
  support: context_only
  summary: Relevant originals were followed up for scaffold, susceptibility, PBP competition
    and clinical use. Siderophore derivatives, host MAO-B/AChE repurposing, transporter
    pharmacokinetics and beta-lactamase substrate studies were not collapsed into
    one antibacterial causal mechanism. Searches and free-access retrieval were bounded.
  snapshot_sha256: 8f67b5a7895406662519e784322c80594a7813100422b1cb19ab681fc61ff358
  search_scope: 2026-10-21; exact loracarbef, CHEBI47544, ARO3004016, native slug/key
    and research codes LY163892/KT3777. Local search included ignored and hidden files.
    Europe PMC returned 205 loracarbef records, first 100 titles read, with focused
    code/activity/target abstracts and selected official primary follow-up.
assessments:
- assessment_id: identity
  area: identity
  topic: Native entity and chemical representations
  outcome: supported
  summary: The neutral intact three-centre native graph is valid and agrees with ChEBI,
    PubChem, HMDB source deposit and KEGG. Explicit neutral/zwitterion representation
    boundaries are preserved. Neither conflicting external graph warrants changing
    native chemistry.
  target_ids:
  - CHEBI:47544
  evidence_ids:
  - native-chemistry
  - hmdb
  - diagnostic
  - primary1989-identity
- assessment_id: xref
  area: grounding
  topic: Exact references versus hydrate and enzyme-bound component
  outcome: concern
  summary: ChEMBL1200610 denotes the monohydrate and CCD LOR the opened component
    of a covalent AmpC complex. Both violate exact structure equivalence. The matching
    ChEMBL parent is a supported candidate for source adjudication; drug and patent
    references retain broader scopes.
  target_ids:
  - CHEBI:47544
  evidence_ids:
  - chembl-hydrate
  - ccd-open
  - diagnostic
  - other-drug-refs
  - patents
- assessment_id: names
  area: grounding
  topic: Systematic synonym and brand typing
  outcome: concern
  summary: The unqualified cepham name retains a sulfur-parent implication and should
    be corrected or withheld. Lorabid is explicitly a trade name. The correct first
    systematic name, native graph and carba definition remain consistent.
  target_ids:
  - CHEBI:47544
  evidence_ids:
  - scaffold-name
  - brand-fda
  - native
- assessment_id: class
  area: grounding
  topic: Chemical parent, pharmacological class and roles
  outcome: supported
  summary: The carbacephem parent structurally matches the native molecule. The broader
    second-generation cephalosporin grouping is conventional pharmacological usage
    supported by sources; it does not make the actual molecule sulfur-containing.
    Both antimicrobial and antibacterial-drug roles are supported.
  target_ids:
  - CHEBI:47544
  evidence_ids:
  - scaffold-name
  - aro
  - roles
  - diagnostic
  - brand-fda
- assessment_id: definition
  area: evidence
  topic: Synthesis, carbon replacement and infection treatment
  outcome: supported
  summary: Original chemistry/activity, clinical trial and official historical-label
    evidence support the description. Broad Gram-positive/negative use does not assert
    every strain is susceptible or a current approval state. Patent enzyme-assisted
    synthesis is not a producer claim.
  target_ids:
  - CHEBI:47544
  evidence_ids:
  - primary1989-identity
  - primary1989-activity
  - clinical1991
  - brand-fda
  - patents
- assessment_id: target
  area: evidence
  topic: PBP binding and assay scope
  outcome: supported
  summary: The qualified family-level target is corroborated by original membrane
    and purified-protein competition assays. Differences among PBP species, reporter
    conditions and parent/conjugate forms are preserved. Optional addition of primary
    evidence is useful but its current absence is not a defect.
  target_ids:
  - CHEBI:47544
  evidence_ids:
  - aro
  - adapter
  - primary1989-pbp
  - primary1993
  - primary2025-pbp
- assessment_id: activity
  area: evidence
  topic: Antibacterial experiments and exact material limits
  outcome: supported
  summary: Exact-name studies support growth inhibition against specified Gram-positive
    and Gram-negative strains, with clear resistant-strain limits. Monohydrate, unspecified
    Kyowa material and gifted Lorabid are not automatically interchangeable bulk preparations
    for numerical curation.
  target_ids:
  - CHEBI:47544
  evidence_ids:
  - primary1989-activity
  - primary1993
  - primary2025-material-activity
  - clinical1991
- assessment_id: provenance
  area: provenance
  topic: Source, history and adopted evidence
  outcome: supported
  summary: Complete native and maintained source rows were inspected, all seven adopted
    PMIDs dispositioned, and actual source-owner hashes appended without replacing
    originals. Imported assertions retain correct database qualifiers.
  target_ids:
  - CHEBI:47544
  evidence_ids:
  - native
  - owners
  - aro
  - adopted-primary
  - adopted-reviews
  - local-search
- assessment_id: completeness
  area: completeness
  topic: Optional data and inaccessible reference boundaries
  outcome: unknown
  summary: The review covers every native field, but direct HMDB and LINCS/Reaxys
    current graphs remain inaccessible or uninspected. HMDB own deposit agrees. No
    missing optional resistance, activity, clinical, producer, dataset or graph object
    is scored as an error.
  target_ids:
  - CHEBI:47544
  evidence_ids:
  - other-drug-refs
  - hmdb
  - bounded-search
  - native
findings:
- finding_id: F1
  issue_key: loracarbef-chembl1200610-monohydrate-exact-xref
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Replace or qualify the monohydrate exact reference
  description: Native xrefs[6] CHEMBL1200610 has a separate water component and monohydrate
    formula/key in three independently parsed representations. It is not the unhydrated
    native chemical entity. Its explicit parent CHEMBL1013 matches native and is a
    concrete candidate for maintained source correction. Preserve the native graph.
  target_ids:
  - CHEBI:47544
  field_paths:
  - xrefs[6]
  evidence_ids:
  - chembl-hydrate
  - diagnostic
  - native-chemistry
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Imported ChEMBL exact reference and Lorabid alias
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO exact-reference and alias extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Exact-reference and synonym emission
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained source-scoped adjudication
  rule_id: Exact chemical references and names must preserve entity scope
  native_severity: major
  normalization_reason: Positive full-entity disagreement makes this an exact-reference
    error. The native identity is independently sound, so no blocker is assigned.
- finding_id: F2
  issue_key: loracarbef-ccd-lor-opened-form-exact-xref
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Do not equate the opened CCD component with intact loracarbef
  description: Native xrefs[4] LOR is officially an opened-form component in the covalently
    acylated AmpC complex 1FCN. It has different formula and connectivity, reproduced
    by its InChI and both isomeric SMILES. Preserve it only as appropriately scoped
    experimental/deposition context rather than exact molecular equivalence.
  target_ids:
  - CHEBI:47544
  field_paths:
  - xrefs[4]
  evidence_ids:
  - ccd-open
  - diagnostic
  - native-chemistry
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Imported names and CCD exact reference
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source chemical-reference and name extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Exact-reference and synonym emission
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained source-scoped adjudication
  rule_id: Exact chemical references and names must preserve entity scope
  native_severity: major
  normalization_reason: An enzyme-bound representation can be useful evidence but
    is positively not the same free structure. The correct native β-lactam remains
    supported.
- finding_id: F3
  issue_key: loracarbef-systematic-synonym-missing-carba-replacement
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Use a carbacephem-consistent systematic synonym
  description: Native synonyms[2] uses a didehydrocepham parent without specifying
    the carbon-for-sulfur replacement. Official cepham chemistry contains sulfur,
    whereas the native graph and correct systematic synonym are sulfur-free. Repair
    or withhold this redundant name through source handling; do not change the structure.
  target_ids:
  - CHEBI:47544
  field_paths:
  - synonyms[2]
  evidence_ids:
  - scaffold-name
  - native-chemistry
  - primary1989-identity
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Imported names and CCD exact reference
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source chemical-reference and name extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Exact-reference and synonym emission
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained source-scoped adjudication
  rule_id: Exact chemical references and names must preserve entity scope
  native_severity: minor
  normalization_reason: This is a localized non-blocking nomenclature error. The label,
    definition, other systematic name and exact native graph identify loracarbef correctly.
- finding_id: F4
  issue_key: loracarbef-lorabid-brand-exact-synonym
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Type Lorabid as a brand name
  description: The FDA explicitly calls Lorabid the trade name for the oral suspension
    and capsule products. Native synonyms[4] must retain that product scope rather
    than EXACT_SYNONYM. Preserve the alias for search as BRAND_NAME.
  target_ids:
  - CHEBI:47544
  field_paths:
  - synonyms[4]
  evidence_ids:
  - brand-fda
  - chembl-hydrate
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Imported ChEMBL exact reference and Lorabid alias
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO exact-reference and alias extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Exact-reference and synonym emission
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained source-scoped adjudication
  rule_id: Exact chemical references and names must preserve entity scope
  native_severity: minor
  normalization_reason: The brand association is useful and correct, but its synonym
    type overstates chemical equivalence.
actions:
- action_id: A1
  description: Adjudicate the two exact-reference conflicts in maintained inputs.
  finding_ids:
  - F1
  - F2
  target_ids:
  - CHEBI:47544
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Imported ChEMBL exact reference and Lorabid alias
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO exact-reference and alias extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Exact-reference and synonym emission
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained source-scoped adjudication
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Imported names and CCD exact reference
  acceptance_checks:
  - Retained exact references must reproduce the intact neutral three-centre graph.
    Verify CHEMBL1013 as the replacement candidate and retain CHEMBL1200610 only with
    explicit hydrate scope if useful.
  - Remove CCD LOR from exact equivalence or represent its opened covalent-complex
    role through an appropriate non-equivalence object. Do not silently substitute
    the opened graph into native chemistry.
  - Regenerate from maintained source policy and rerun schema, strict, chemical identity
    and source-reproduction checks.
- action_id: A2
  description: Correct the two naming scopes while preserving useful aliases.
  finding_ids:
  - F3
  - F4
  target_ids:
  - CHEBI:47544
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Imported names and CCD exact reference
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source chemical-reference and name extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Exact-reference and synonym emission
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Maintained source-scoped adjudication
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Imported ChEMBL exact reference and Lorabid alias
  acceptance_checks:
  - Withhold or correct the cepham-based name to specify the carbacephem replacement,
    retaining the already correct systematic name and graph.
  - Emit Lorabid as BRAND_NAME with source attribution. Use existing maintained exclusions/typing
    or explicitly extend the mapping if needed; do not patch generated YAML.
  - Verify reseeding preserves the corrected aliases and all supported roles.
- action_id: A3
  description: Use the inspected originals for optional target and activity enrichment.
  finding_ids: []
  target_ids:
  - CHEBI:47544
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/loracarbef.yaml
    role: Curator-owned primary target and activity evidence through the validated
      writer
  acceptance_checks:
  - Keep membrane radiobenzylpenicillin and Bocillin FL competition IC50 distinct
    from equilibrium Kd, direct transpeptidation rates and whole-cell MIC. Preserve
    organism, strain and preparation.
  - Do not transfer BLOR conjugate potency or uptake properties to unconjugated loracarbef.
    Preserve the 1989 unspecified bulk form, 1993 monohydrate and 2025 gifted Lorabid
    material limitations.
  - Keep clinical evaluability denominators and historical indications separate from
    current approval/marketing status. Do not infer a natural producer from enzyme-assisted
    synthetic preparation.
limitations:
- The 1989 original main text and all table text were read, with selected original
  pages viewed for structure, susceptibility and PBP fluorography. Not every figure
  or raw spectrum was independently reprocessed; its bulk hydrate/purity was unspecified.
- The 1993 original was read only in relevant material/PBP sections and its complete
  English abstract. The rest of the Japanese article and every numeric table were
  not independently audited.
- The 2025 original was read in Introduction, selected susceptibility/beta-lactamase/PBP
  Results, relevant Methods and full Discussion; Figures 4/5 were viewed. SI Table
  S8 and material/synthesis sections on pp16/20 were read. Uncropped gels, all spectra
  and unrelated uptake/genetic experiments were not fully audited.
- The 2025 parent material is described as gifted Lorabid. The inspected text does
  not independently establish hydrate content, parent purity or mass normalization.
  The characterized conjugate purity statement is not automatically a parent-material
  measurement.
- The 1991 clinical trial was read in all three scanned pages. The FDA 1996 file was
  read only in the approval letter and relevant medical-review sections, not as a
  complete current regulatory audit.
- All seven adopted citations were read at complete-abstract depth. Four are secondary
  reviews. The 1987 enzyme article remained purchase-gated beyond its official abstract;
  the 1992 pharmaceutical and 1996 IgE originals were not obtained in full.
- Patent inspection was limited to relevant descriptions, preparations and claims.
  Their absolute ring assignment is explicitly assumed; no independent modern crystallographic
  hand determination is claimed. The 2000 AmpC paper was identified through official
  deposition metadata but not read in full.
- Direct HMDB returned 403; its own PubChem deposit agrees with native. LINCS returned
  500, DrugBank 403 and Reaxys was not accessed through paid services. Current exact
  chemistry for inaccessible LINCS/Reaxys remains unverified.
- The literature search was bounded and did not exhaust all 205 loracarbef results.
  Optional enrichment gaps are not native defects; source assertions are not upgraded
  solely by deterministic validation.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All thirteen initial input hashes are preserved, with actual owners appended to
  sixteen. Retrieval manifests retain real URLs, UTC timestamps, statuses and hashes.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
