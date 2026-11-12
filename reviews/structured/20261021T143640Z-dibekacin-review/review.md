# Dibekacin: exact aminoglycoside identity, qualified ARO claims and product synonym

- Review: 20261021T143640Z-dibekacin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:11:42Z
- Finished UTC: 2026-10-21T14:36:40Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The neutral dibekacin structure is coherent and matches current chemical authorities. Original synthesis, antibacterial assays and ribosomal translation experiments support eligibility and the broad mode of action. All 65 imported resistance entries retain their database status; the review does not certify every allele experimentally. One minor correction is warranted: Icacine is an injection product name, currently typed as an exact chemical synonym.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 359; one exact record. All 13 original input hashes are preserved within 31 expanded inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:37945 | data/antibiotics/antibacterial/dibekacin.yaml | generated | dibekacin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:37945 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:37945 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:37945 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:37945 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:37945 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:37945 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:37945 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:37945 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:37945 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:37945 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:37945 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:37945 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact structure and names

identity: concern. Targets: CHEBI:37945.

Chemical identity and stereochemistry are coherent. Icacine is a confirmed injection name typed as EXACT_SYNONYM; the other unusual commercial-looking names are retained as unresolved source nomenclature rather than assigned speculative corrections.

### Parents and all asserted chemical/document links

grounding: supported. Targets: CHEBI:37945.

ChEBI, ARO, PubChem, ChEMBL, KEGG and DrugCentral resolve coherently. The adopted CAS and Reaxys labels remain source authority assertions; the protected Reaxys record was not independently accessed. Both native patent references concern dibekacin.

### Eligibility, roles, mode and target scope

scope: supported. Targets: CHEBI:37945.

Compound-specific synthesis/antibacterial experiments and cell-free translation inhibition support the antibacterial role and protein-synthesis mode. HOST_SHARED_TARGET describes the general source process rather than clinical selectivity; mammalian translation comparison does not imply identical bacterial and host potency.

### Imported 16S rRNA target

evidence: supported. Targets: CHEBI:37945.

The native target remains a qualified database assertion requiring primary evidence. Original rRNA-mutant translation data support functional involvement; protein-fraction reconstitution does not supply direct isolated-protein binding. These papers do not warrant silently upgrading the source-only relation to a primary direct-binding claim.

### All 65 imported resistance claims

evidence: supported. Targets: CHEBI:37945.

Every source edge, label, mechanism type and qualification was read and reconciled. Current term definitions and bounded original enzyme evidence support retaining the database tier; the review does not claim all 65 alleles were validated in dibekacin-specific original assays.

### Optional activity_spectrum

completeness: supported. Targets: CHEBI:37945.

Exact dibekacin antibacterial measurements are available. Curation should preserve reagent-form uncertainty, selected isolate panels and original assay conditions; cell-free IC50 and ocular viability scores are separate endpoints. Optional activity absence is not a required-field defect.

### All five adopted citations

evidence: supported. Targets: CHEBI:37945.

Two original studies were assessed at full-text or abstract depth, while the three reviews were explicitly identified as secondary sources. No review metadata or precursor-production result was converted into direct dibekacin mechanism or producer evidence.

### Product names and salt boundary

scope: concern. Targets: CHEBI:37945.

The neutral chemical record is coherent, but confirmed Icacine product naming should use BRAND_NAME. Sulfate monograph and ophthalmic formulation evidence must retain their separate ingredient/material scope; no FDA product field is asserted.

### Producer, causal graph and datasets

scope: not_applicable. Targets: CHEBI:37945.

No such native assertions occur. Engineering a precursor-producing strain is not evidence that the strain produces dibekacin. No causal graph is inferred from translation inhibition alone.

### Maintained ownership and history

provenance: supported. Targets: CHEBI:37945.

The source merge, two source mints, SEEDED status and five generated events are consistent. All originally captured inputs remain unchanged; actual ARO and target-qualification owners are included.

### Focused checks

schema: supported. Targets: CHEBI:37945.

Schema, strict and chemistry pass; shared same-base corpus gates are attached separately by root.

## Findings

### F1: Icacine product name is typed as an exact chemical synonym

minor / open / confirmed; issue key: AntibioticMech.CHEBI-37945.icacine-brand-synonym.

Icacine is listed as EXACT_SYNONYM even though the official historical product list identifies it as a dibekacin injection brand. Retype this confirmed product name as BRAND_NAME while preserving the neutral compound identity and its source provenance.

## Recommended Actions And Acceptance Checks

### A1

Correct confirmed product-name typing through the maintained source/generation path.

- Regenerated Icacine uses BRAND_NAME and retains source provenance.
- Do not infer a sulfate stoichiometry, current marketing status or corrections to Panamicin/Kappati from this historical list.
- Run schema, strict and corpus-reproduction gates after authorized curation.

### A2

Optionally curate original dibekacin activity and rRNA-dependent mechanism with exact evidence placement.

- Preserve original reagent description and unresolved salt form, strain, units and assay conditions.
- Keep translation IC50, whole-cell MIC, enzyme modification and ocular toxicity separate.
- Resolve supplemental exact allele/strain rows before adding quantitative resistance observations; do not extrapolate the ANT-I example to all alleles.
- Do not call reconstitution with S9/L6 fractions direct binding to purified proteins or use kanamycin A crystallography as dibekacin structural evidence.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/dibekacin.yaml; Entire record: 13 synonyms, two parents, two roles, mode/scope, all xrefs, 65 resistance entries, one target, two source concepts and five generated history events | supports | The SEEDED exact record denotes neutral dibekacin. Every imported resistance item explicitly says CARD/ARO database assertion; the 16S rRNA target is CARD_ARO with PRIMARY_EVIDENCE_NEEDED. There are no activity_spectrum, FDA product, producer, causal graph or dataset assertions. |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_resistance_edges.tsv; data/raw/aro_target_edges.tsv; ChEBI row766, ARO antibiotic/target row5 and all exact resistance edge rows; expanded owner captures | supports | The actual source rows reproduce the structure, synonyms, five adopted literature leads, roles and all imported mechanism claims. ChEBI classification drives the broad protein-synthesis mode; imported source assertion qualification and target-role policy were read. |
| chemistry | Independent RDKit2026.03.5 using batch019 interpreter against batch036 cwd; 359-chemistry.json;358360-xref-chemistry.json | supports | SMILES and InChI reproduce neutral C18H37N5O8, JJCQSGDBDPYCEO-XVZSLQNASA-N and 13 assigned centres. Formula, rounded masses and both source mints agree. Current ChEBI, PubChem470999, ChEMBL560976, KEGG D07811 and DrugCentral855 structures independently reproduce this exact key. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/37945/; CHEBI:37945 complete response | supports | Current identity, definition, parents, activity roles, chemical encodings and adopted cross-references agree with the neutral dideoxykanamycin B graph. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/470999/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON; CID470999 complete property response | supports | The current PubChem formula, charge, mass and stereochemical InChI agree with the native record. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL560976.json; CHEMBL560976 molecule structure | supports | The ChEMBL graph denotes the same neutral, fully specified dibekacin structure. |
| kegg | https://rest.kegg.jp/get/D07811/mol; D07811 structure; companion359-kegg.txt | supports | KEGG D07811 is the neutral dibekacin graph, not the sulfate substance. |
| drugcentral | https://drugcentral.org/drug/855/molfile; DrugCentral855 actual molfile and companion drugcard | supports | The corrected official molfile route resolves the exact native stereochemical key. The initial /mol/855 route returned404 and was not mistaken for a successful structure retrieval. |
| aro | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_0000007; ARO:0000007 term response | supports | Current ARO resolves dibekacin and the adopted source identity; nomenclature membership is database evidence, not proof that every synonym is a chemical exact name. |
| synthesis1971 | https://doi.org/10.7164/antibiotics.24.485; Original three-page synthesis letter, pages485-487; actual structure drawings and Table1 viewed | supports | Kanamycin B was selectively converted through the 3-prime,4-prime unsaturated intermediate and hydrogenated/deprotected to 3-prime,4-prime dideoxykanamycin B. The final isolated material has the expected optical rotation and analytical characterization; no sulfate is specified. Table1 reports MICs in micrograms/mL, including E. coli K-12 CS-2 at 1.56 and P. aeruginosa A3 at 3.12. The short letter does not fully specify medium/incubation, and its resistant-strain comparisons do not identify a modern resistance allele. |
| activity1981 | https://doi.org/10.1128/AAC.19.1.190; PMID6787978 / PMC181381; all three original scanned pages viewed, Methods and Tables1/2 | supports | A panel of 221 clinical isolates used USV Laboratories dibekacin standard powder, with salt unspecified. Mueller-Hinton agar and a Steers replicator delivered approximately 5×10^4 CFU per spot. Dibekacin control MICs were 1.0 micrograms/mL for E. coli ATCC25922 and P. aeruginosa ATCC27853 and at most 0.125 for S. aureus ATCC25923. Table1 specifically covers 195 gentamicin-susceptible isolates; Table2 the 26 resistant isolates. These selected panels are not a species-wide spectrum, and phenotype alone does not identify a resistance genotype. |
| activity1981-tables | https://pmc.ncbi.nlm.nih.gov/articles/PMC181381/; Original scanned pages191-192; Table1 and Table2 | supports | The complete tables were visually inspected. Historical susceptibility cutoffs and local isolate numbers must be preserved as historical assay context; neither is a current clinical breakpoint or a universal strain identifier. The paper does not establish the salt composition of its powder. |
| ribosome1981 | https://doi.org/10.7164/antibiotics.34.763; PMID6268595; full original Methods/Results/Discussion; actual Tables3/4 at page767 viewed | supports | Meiji radiolabeled dibekacin binding to E. coli Q13 ribosomes was measured by nitrocellulose filtration, using 1 micromolar ribosomes and 10 micromolar drug, 30 degrees C for 5 minutes. LiCl-treated core particles had reduced binding; addition of fractions containing S9 and L6(S3) partly restored it. This reconstitution does not prove direct drug binding to isolated S9 or L6: the authors explicitly leave the precise site unresolved. The source does not justify replacing the native 16S rRNA target with a protein target. |
| target2012 | https://doi.org/10.1128/AAC.01326-12; PMID22948879 / PMC3497201; original full Methods/Results/Discussion and Table2 | supports | ANAWA dibekacin, salt unspecified, inhibited luciferase synthesis by purified M. smegmatis ribosomes. The single-rRNA-allele system tested A1408G, G1491A and G1491C substitutions. Table2 dibekacin IC50 values are 0.02, 0.2, 1.3 and 32.3 micrograms/mL for wild type, G1491A, G1491C and A1408G respectively. These are cell-free translation endpoints, not MICs or a dibekacin crystal structure; Figure1 depicts kanamycin A. The results support rRNA-dependent drug action without independently upgrading the imported target to primary direct-binding status. |
| ant1978 | https://doi.org/10.7164/antibiotics.31.343; Original Methods/Results/Discussion and actual Table2 at page347 | supports | Purified aminoglycoside-4-prime,4-double-prime nucleotidyltransferase from S. epidermidis FK109 modifies dibekacin despite its missing 4-prime hydroxyl; the discussion identifies the 4-double-prime equatorial hydroxyl as the alternative site. Table2 reports relative adenylylation 6% versus kanamycin B 100%, dibekacin MIC 6.25 micrograms/mL and no residual antibacterial activity after modification. Biochemical substrate activity is not automatically high whole-cell resistance, nor a sequence-level confirmation of every modern ANT-I allele. |
| aro-audit | https://www.ebi.ac.uk/ols4/ontologies/aro; 359-aro-audit.json;65 separately hashed current term responses and exact adopted edge mapping | supports | All 65 native resistance entries match their adopted source edge and retain database-assertion notes. Each current identifier resolves and is nonobsolete; every retrieved definition was read. Methylation and aminoglycoside-modification routes are plausible at this source tier, but all original allele-specific experiments were not independently adjudicated. ANT(4-prime)-I should not be deleted merely because dibekacin lacks a4-prime OH; the 1978 original establishes 4-double-prime modification. The 2012 general discussion of ANT(4-prime) avoidance cannot settle each allele without its unaccessed supplemental panel. |
| ocular2010 | https://doi.org/10.2147/OPTH.S12452; Adopted PMID20922036; full original XML Methods, Table1 and Results | context_only | The paper tests commercial ophthalmic solutions in four ocular cell lines for 48 hours. Table1 names 0.5% dibekacin Panimycin (Meiji); the score 3 concerns cell viability at a tenfold dilution. It is neither a bacterial MIC nor an assay of independently characterized neutral dibekacin. The source spelling Panimycin does not by itself prove that native Panamicin is a typographic error. |
| adopted-20936279 | https://pubmed.ncbi.nlm.nih.gov/20936279/; Complete Europe PMC core metadata and available original abstract | context_only | The original abstract concerns engineered Streptomyces tenebrarius H6 and SPU314 production of kanamycin B as a precursor. It does not demonstrate natural biosynthesis of dibekacin. |
| adopted-11083623 | https://pubmed.ncbi.nlm.nih.gov/11083623/; Complete Europe PMC core metadata and available original abstract | context_only | Metadata identifies a 2000 aminoglycoside-modifying-enzyme review; no abstract is supplied. It is a discovery source, not an inspected original dibekacin experiment. |
| adopted-10103173 | https://pubmed.ncbi.nlm.nih.gov/10103173/; Complete Europe PMC core metadata and available original abstract | context_only | Metadata identifies a 1999 aminoglycoside review; no abstract is supplied. Full review text was not assessed and cannot certify the native resistance panel. |
| adopted-8385262 | https://pubmed.ncbi.nlm.nih.gov/8385262/; Complete Europe PMC core metadata and available original abstract | context_only | The original 1993 review abstract was read. General resistance discussion is contextual; it does not replace claim-specific original enzyme or strain evidence. |
| patent1 | https://patents.google.com/patent/CN101278900A/en; CN101278900A translated Description and Example3 | context_only | The sustained-release injection patent explicitly includes dibekacin; Example3 combines 30 mg drug with 70 mg polymer and discusses microsphere release. It is a relevant document cross-reference, but its formulation claims do not establish a neutral-compound MIC, exact sulfate stoichiometry or regulatory approval. |
| patent2 | https://patents.google.com/patent/CN101575354A/en; CN101575354A Background, synthetic method, Example1 step6 and subsequent arbekacin steps | context_only | This patent isolates dibekacin as an intermediate by hydrogenation of unsaturated kanamycin B followed by ion exchange, before later arbekacin synthesis. It supports document relevance; dibekacin is not interchangeable with arbekacin, and acetic-acid solvent does not establish an isolated acetate salt. |
| sulfate | https://www.mhlw.go.jp/content/11120000/000904440.pdf; Japanese Pharmacopoeia XVIII monograph Dibekacin Sulfate, printed page845 | context_only | The monograph defines C18H37N5O8·xH2SO4 and expresses potency in terms of the dibekacin moiety. This confirms the form boundary: product or standard sulfate potency does not make the neutral native graph a sulfate structure. |
| icacine | https://circulaires.ameli.fr/sites/default/files/directives/cir/1997/970922-C.PDF; French health-insurance circular1997; actual printed page32 viewed, product rows3249993 and3233963 | supports | The official historical list identifies ICACINE 25 MG and ICACINE 75 MG as dibekacin injection ampoules. This establishes a product/brand name rather than a chemical exact synonym. This source does not specify sulfate stoichiometry or establish current marketing status. |
| adapter | https://imodulondb.org/api/datasets; 358359-adapter-results.json; catalog325-adapter-catalog-network.json | context_only | Structured queries preceded protein follow-up. E. coli precise1k rrsB and armA returned no gene/component matches. The catalog does not cover all donor strains in the imported panel; no expression-module association or biological absence is inferred. |
| search | Ignored-inclusive local search and free original-source retrieval; 358360-local-focused.txt;359-discovery.json; fetch manifests | context_only | All five adopted leads were disposed by actual reading depth. Original 1971,1978 and1981 pages and the 2012 main text were accessible. The 2012 supplementary PDF/index returned HTML challenge content, and the XML endpoint failed; the supplemental exact enzyme/strain MIC rows were not inspected. The official Icacine circular was accessible while the secondary BIAM page returned 403. |
| gates | Focused native validation and standalone chemistry; 359-focused-results.json | supports | Schema, strict and chemistry all exited 0. Native validators used batch036; RDKit used the existing batch019 interpreter against batch036 cwd. |
| orbicin-boundary | https://pubmed.ncbi.nlm.nih.gov/7461562/; Original abstract PMID7461562; comparator PMID582126 in359-discovery.json | context_only | Both original abstracts explicitly pair dibekacin with the name Orbicin. PMID7461562 describes 29 surgical patients and 10 healthy volunteers; PMID582126 describes tube-dilution and cross-resistance experiments. Neither inspected abstract identifies formulation, salt, catalog or official product status. They establish historical name usage, while exact synonym-versus-brand typing remains unresolved without product documentation. No numerical endpoint is transferred. |

## Limits And Additional Notes

- All 65 native ARO templates, adopted edges and live term definitions were read. Original experiments were assessed for a bounded subset; the report is not independent primary validation of all 65 allele-specific drug relationships.
- All five adopted leads were resolved. The 2010 ocular paper was read in full relevant sections; the biosynthesis study at original abstract depth; three reviews at metadata/available abstract depth. Their full bibliographies were not adjudicated.
- The 2012 original main text and Table2 were read, but its supplementary exact resistance/MIC panel returned challenge content. Source material salt is unspecified in several assays; no sulfate/free-base numerical conversion was invented.
- Reaxys was not independently accessed. The source names Panamicin and Kappati were not conclusively resolved to current product records. Only the confirmed Icacine typing is a finding. Orbicin was checked in original abstracts PMID7461562 and PMID582126; historical name usage is supported, but official product identity, salt and synonym typing remain unresolved.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native/source/status/history was edited. Optional links, tags and notes were checked against dibekacin.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T143640Z-dibekacin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Dibekacin: exact aminoglycoside identity, qualified ARO claims and product
  synonym'
started_at: '2026-10-21T14:11:42Z'
finished_at: '2026-10-21T14:36:40Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independent reviewer read the complete 593-line native record,
    all actual ChEBI/ARO source rows and 65 imported claim templates after verifying
    initial captures; calculated chemistry; inspected current authorities, all adopted
    literature metadata/available abstracts, and bounded original full-text experiments.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'The neutral dibekacin structure is coherent and matches current chemical
  authorities. Original synthesis, antibacterial assays and ribosomal translation
  experiments support eligibility and the broad mode of action. All 65 imported resistance
  entries retain their database status; the review does not certify every allele experimentally.
  One minor correction is warranted: Icacine is an injection product name, currently
  typed as an exact chemical synonym.'
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
  - path: data/antibiotics/antibacterial/dibekacin.yaml
    sha256: fdad190d1d11d967c216429e5f8102b3df816d2ced39980be121337668b591a6
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
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
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
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: data/raw/mibig_producers.tsv
    sha256: d55289619e77e035ed437d432dd692ab382f254c3841c9a314752ef22578a01b
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
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
  - path: scripts/extract_mibig_producers.py
    sha256: a078cdf4c9b2d09999800ab7ae03f93d3972f29b7d2f460ebbbe7d7ec6b31c53
    role: context
targets:
- target_id: CHEBI:37945
  path: data/antibiotics/antibacterial/dibekacin.yaml
  label: dibekacin
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
    role: ARO synonyms, class, xrefs and adopted citation leads
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: All source-only ARO resistance claims
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: 16S rRNA database target assertion
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Direct-target eligibility policy
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Source assertion qualification
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 359; one exact record. All 13 original input hashes are
    preserved within 31 expanded inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:37945
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:37945
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/358360-focused.py
    (cwd /private/tmp/antibioticmech-record-reviews-036)
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
  - CHEBI:37945
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/dibekacin.yaml (cwd /private/tmp/antibioticmech-record-reviews-036)
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
  - CHEBI:37945
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/dibekacin.yaml --out /private/tmp/am-review-session/359-strict.tsv
    (cwd /private/tmp/antibioticmech-record-reviews-036)
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
  - CHEBI:37945
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
  - CHEBI:37945
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
  - CHEBI:37945
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
  - CHEBI:37945
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
  - CHEBI:37945
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
  - CHEBI:37945
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
  - CHEBI:37945
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
  - CHEBI:37945
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
  - CHEBI:37945
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/dibekacin.yaml
  locator: 'Entire record: 13 synonyms, two parents, two roles, mode/scope, all xrefs,
    65 resistance entries, one target, two source concepts and five generated history
    events'
  accessed_at: '2026-10-21T14:34:34Z'
  support: supports
  summary: The SEEDED exact record denotes neutral dibekacin. Every imported resistance
    item explicitly says CARD/ARO database assertion; the 16S rRNA target is CARD_ARO
    with PRIMARY_EVIDENCE_NEEDED. There are no activity_spectrum, FDA product, producer,
    causal graph or dataset assertions.
  snapshot_sha256: 65183770d185d35acd44f87bdb34e69c10a0c21e7d5dda438d2a98e2dda0afe2
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_resistance_edges.tsv;
    data/raw/aro_target_edges.tsv
  locator: ChEBI row766, ARO antibiotic/target row5 and all exact resistance edge
    rows; expanded owner captures
  accessed_at: '2026-10-21T14:34:34Z'
  support: supports
  summary: The actual source rows reproduce the structure, synonyms, five adopted
    literature leads, roles and all imported mechanism claims. ChEBI classification
    drives the broad protein-synthesis mode; imported source assertion qualification
    and target-role policy were read.
  snapshot_sha256: 65183770d185d35acd44f87bdb34e69c10a0c21e7d5dda438d2a98e2dda0afe2
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit2026.03.5 using batch019 interpreter against batch036
    cwd
  locator: 359-chemistry.json;358360-xref-chemistry.json
  accessed_at: '2026-10-21T14:34:34Z'
  support: supports
  summary: SMILES and InChI reproduce neutral C18H37N5O8, JJCQSGDBDPYCEO-XVZSLQNASA-N
    and 13 assigned centres. Formula, rounded masses and both source mints agree.
    Current ChEBI, PubChem470999, ChEMBL560976, KEGG D07811 and DrugCentral855 structures
    independently reproduce this exact key.
  snapshot_sha256: ea8340e67a147bf1d4a1a7c3d913225d922acbdf4afb4ca4b8eaea62fd11b082
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/37945/
  locator: CHEBI:37945 complete response
  accessed_at: '2026-10-21T14:22:03.079863Z'
  support: supports
  summary: Current identity, definition, parents, activity roles, chemical encodings
    and adopted cross-references agree with the neutral dideoxykanamycin B graph.
  snapshot_sha256: a32ae3c58bd6b575393f540f4dce3b5475704c1ce7c2aa8a6f7dab7a11945a85
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/470999/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON
  locator: CID470999 complete property response
  accessed_at: '2026-10-21T14:22:03.092228Z'
  support: supports
  summary: The current PubChem formula, charge, mass and stereochemical InChI agree
    with the native record.
  snapshot_sha256: 3552600a621a4c24ad06a5dc41d4f6136b32db593ac655c994350507aa5921f2
- evidence_id: chembl
  kind: authority
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL560976.json
  locator: CHEMBL560976 molecule structure
  accessed_at: '2026-10-21T14:22:03.203218Z'
  support: supports
  summary: The ChEMBL graph denotes the same neutral, fully specified dibekacin structure.
  snapshot_sha256: 43a0a89c22a154ddca15379c3bce2114c4f38b19f5b99e83825a6ae7d58a0e96
- evidence_id: kegg
  kind: authority
  reference: https://rest.kegg.jp/get/D07811/mol
  locator: D07811 structure; companion359-kegg.txt
  accessed_at: '2026-10-21T14:22:03.614615Z'
  support: supports
  summary: KEGG D07811 is the neutral dibekacin graph, not the sulfate substance.
  snapshot_sha256: 0a53f9aa96d8aac452e6868c2233dafe368f3b96b8567f18d069bdb3b0a551d1
- evidence_id: drugcentral
  kind: authority
  reference: https://drugcentral.org/drug/855/molfile
  locator: DrugCentral855 actual molfile and companion drugcard
  accessed_at: '2026-10-21T14:24:00.503769Z'
  support: supports
  summary: The corrected official molfile route resolves the exact native stereochemical
    key. The initial /mol/855 route returned404 and was not mistaken for a successful
    structure retrieval.
  snapshot_sha256: 297e258d6358ba4cea65c275bc2c8843af079268fd9d346658fa4820fff4bed4
- evidence_id: aro
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_0000007
  locator: ARO:0000007 term response
  accessed_at: '2026-10-21T14:22:03.818166Z'
  support: supports
  summary: Current ARO resolves dibekacin and the adopted source identity; nomenclature
    membership is database evidence, not proof that every synonym is a chemical exact
    name.
  snapshot_sha256: 0fccc007e15f6abefa9920f3d5e4f5e19ec5b2c1655e9835cbded47dd4268e3e
- evidence_id: synthesis1971
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.24.485
  locator: Original three-page synthesis letter, pages485-487; actual structure drawings
    and Table1 viewed
  accessed_at: '2026-10-21T14:28:08.047775Z'
  support: supports
  summary: Kanamycin B was selectively converted through the 3-prime,4-prime unsaturated
    intermediate and hydrogenated/deprotected to 3-prime,4-prime dideoxykanamycin
    B. The final isolated material has the expected optical rotation and analytical
    characterization; no sulfate is specified. Table1 reports MICs in micrograms/mL,
    including E. coli K-12 CS-2 at 1.56 and P. aeruginosa A3 at 3.12. The short letter
    does not fully specify medium/incubation, and its resistant-strain comparisons
    do not identify a modern resistance allele.
  snapshot_sha256: bcd424d50d01aaae8b9f0a45d0a31a67492218205ae41035a91d7476fdb7b1ba
- evidence_id: activity1981
  kind: primary_source
  reference: https://doi.org/10.1128/AAC.19.1.190
  locator: PMID6787978 / PMC181381; all three original scanned pages viewed, Methods
    and Tables1/2
  accessed_at: '2026-10-21T14:23:25.516603Z'
  support: supports
  summary: A panel of 221 clinical isolates used USV Laboratories dibekacin standard
    powder, with salt unspecified. Mueller-Hinton agar and a Steers replicator delivered
    approximately 5×10^4 CFU per spot. Dibekacin control MICs were 1.0 micrograms/mL
    for E. coli ATCC25922 and P. aeruginosa ATCC27853 and at most 0.125 for S. aureus
    ATCC25923. Table1 specifically covers 195 gentamicin-susceptible isolates; Table2
    the 26 resistant isolates. These selected panels are not a species-wide spectrum,
    and phenotype alone does not identify a resistance genotype.
  snapshot_sha256: 0a9fe1fc040d1a291c9ef723c3dd4cfd47fae17527e9f876139c9e2fc87e740f
- evidence_id: activity1981-tables
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC181381/
  locator: Original scanned pages191-192; Table1 and Table2
  accessed_at: '2026-10-21T14:23:25.630976Z'
  support: supports
  summary: The complete tables were visually inspected. Historical susceptibility
    cutoffs and local isolate numbers must be preserved as historical assay context;
    neither is a current clinical breakpoint or a universal strain identifier. The
    paper does not establish the salt composition of its powder.
  snapshot_sha256: 47207840844dcc2720f477de79ff3d95b87e89250ba579d3333679137e9010ef
- evidence_id: ribosome1981
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.34.763
  locator: PMID6268595; full original Methods/Results/Discussion; actual Tables3/4
    at page767 viewed
  accessed_at: '2026-10-21T14:22:50.453757Z'
  support: supports
  summary: 'Meiji radiolabeled dibekacin binding to E. coli Q13 ribosomes was measured
    by nitrocellulose filtration, using 1 micromolar ribosomes and 10 micromolar drug,
    30 degrees C for 5 minutes. LiCl-treated core particles had reduced binding; addition
    of fractions containing S9 and L6(S3) partly restored it. This reconstitution
    does not prove direct drug binding to isolated S9 or L6: the authors explicitly
    leave the precise site unresolved. The source does not justify replacing the native
    16S rRNA target with a protein target.'
  snapshot_sha256: b0bc99473fb7f409a3600f03805a69857b3e07b1c32acb3f6da1bbdbb4528f00
- evidence_id: target2012
  kind: primary_source
  reference: https://doi.org/10.1128/AAC.01326-12
  locator: PMID22948879 / PMC3497201; original full Methods/Results/Discussion and
    Table2
  accessed_at: '2026-10-21T14:28:50.991610Z'
  support: supports
  summary: ANAWA dibekacin, salt unspecified, inhibited luciferase synthesis by purified
    M. smegmatis ribosomes. The single-rRNA-allele system tested A1408G, G1491A and
    G1491C substitutions. Table2 dibekacin IC50 values are 0.02, 0.2, 1.3 and 32.3
    micrograms/mL for wild type, G1491A, G1491C and A1408G respectively. These are
    cell-free translation endpoints, not MICs or a dibekacin crystal structure; Figure1
    depicts kanamycin A. The results support rRNA-dependent drug action without independently
    upgrading the imported target to primary direct-binding status.
  snapshot_sha256: fcb9088f1c37b1e0e45db989fda5134e9da41140226eacb6806c74118a8c9097
- evidence_id: ant1978
  kind: primary_source
  reference: https://doi.org/10.7164/antibiotics.31.343
  locator: Original Methods/Results/Discussion and actual Table2 at page347
  accessed_at: '2026-10-21T14:23:25.515945Z'
  support: supports
  summary: Purified aminoglycoside-4-prime,4-double-prime nucleotidyltransferase from
    S. epidermidis FK109 modifies dibekacin despite its missing 4-prime hydroxyl;
    the discussion identifies the 4-double-prime equatorial hydroxyl as the alternative
    site. Table2 reports relative adenylylation 6% versus kanamycin B 100%, dibekacin
    MIC 6.25 micrograms/mL and no residual antibacterial activity after modification.
    Biochemical substrate activity is not automatically high whole-cell resistance,
    nor a sequence-level confirmation of every modern ANT-I allele.
  snapshot_sha256: 32895953cf3f48a5cdf9cd7153126639764a551eddd9f2a315c9444e84c1a0c1
- evidence_id: aro-audit
  kind: database
  reference: https://www.ebi.ac.uk/ols4/ontologies/aro
  locator: 359-aro-audit.json;65 separately hashed current term responses and exact
    adopted edge mapping
  accessed_at: '2026-10-21T14:34:34Z'
  support: supports
  summary: All 65 native resistance entries match their adopted source edge and retain
    database-assertion notes. Each current identifier resolves and is nonobsolete;
    every retrieved definition was read. Methylation and aminoglycoside-modification
    routes are plausible at this source tier, but all original allele-specific experiments
    were not independently adjudicated. ANT(4-prime)-I should not be deleted merely
    because dibekacin lacks a4-prime OH; the 1978 original establishes 4-double-prime
    modification. The 2012 general discussion of ANT(4-prime) avoidance cannot settle
    each allele without its unaccessed supplemental panel.
  snapshot_sha256: 12901b481f672873b564b1af1c2ce9d5eba286c460bef25d5795785239926bd3
- evidence_id: ocular2010
  kind: primary_source
  reference: https://doi.org/10.2147/OPTH.S12452
  locator: Adopted PMID20922036; full original XML Methods, Table1 and Results
  accessed_at: '2026-10-21T14:22:50.377510Z'
  support: context_only
  summary: The paper tests commercial ophthalmic solutions in four ocular cell lines
    for 48 hours. Table1 names 0.5% dibekacin Panimycin (Meiji); the score 3 concerns
    cell viability at a tenfold dilution. It is neither a bacterial MIC nor an assay
    of independently characterized neutral dibekacin. The source spelling Panimycin
    does not by itself prove that native Panamicin is a typographic error.
  snapshot_sha256: aaa00133766267c520d0c745919dbfa243ec48f03b49b99aa61a48794cd09c3c
- evidence_id: adopted-20936279
  kind: database
  reference: https://pubmed.ncbi.nlm.nih.gov/20936279/
  locator: Complete Europe PMC core metadata and available original abstract
  accessed_at: '2026-10-21T14:22:05.022868Z'
  support: context_only
  summary: The original abstract concerns engineered Streptomyces tenebrarius H6 and
    SPU314 production of kanamycin B as a precursor. It does not demonstrate natural
    biosynthesis of dibekacin.
  snapshot_sha256: e2468558b61644ea491f7aa8db66ebe97ddd91039c1a71a082b339a295bdf289
- evidence_id: adopted-11083623
  kind: database
  reference: https://pubmed.ncbi.nlm.nih.gov/11083623/
  locator: Complete Europe PMC core metadata and available original abstract
  accessed_at: '2026-10-21T14:22:05.022868Z'
  support: context_only
  summary: Metadata identifies a 2000 aminoglycoside-modifying-enzyme review; no abstract
    is supplied. It is a discovery source, not an inspected original dibekacin experiment.
  snapshot_sha256: e2468558b61644ea491f7aa8db66ebe97ddd91039c1a71a082b339a295bdf289
- evidence_id: adopted-10103173
  kind: database
  reference: https://pubmed.ncbi.nlm.nih.gov/10103173/
  locator: Complete Europe PMC core metadata and available original abstract
  accessed_at: '2026-10-21T14:22:05.022868Z'
  support: context_only
  summary: Metadata identifies a 1999 aminoglycoside review; no abstract is supplied.
    Full review text was not assessed and cannot certify the native resistance panel.
  snapshot_sha256: e2468558b61644ea491f7aa8db66ebe97ddd91039c1a71a082b339a295bdf289
- evidence_id: adopted-8385262
  kind: database
  reference: https://pubmed.ncbi.nlm.nih.gov/8385262/
  locator: Complete Europe PMC core metadata and available original abstract
  accessed_at: '2026-10-21T14:22:05.022868Z'
  support: context_only
  summary: The original 1993 review abstract was read. General resistance discussion
    is contextual; it does not replace claim-specific original enzyme or strain evidence.
  snapshot_sha256: e2468558b61644ea491f7aa8db66ebe97ddd91039c1a71a082b339a295bdf289
- evidence_id: patent1
  kind: primary_source
  reference: https://patents.google.com/patent/CN101278900A/en
  locator: CN101278900A translated Description and Example3
  accessed_at: '2026-10-21T14:22:03.781088Z'
  support: context_only
  summary: The sustained-release injection patent explicitly includes dibekacin; Example3
    combines 30 mg drug with 70 mg polymer and discusses microsphere release. It is
    a relevant document cross-reference, but its formulation claims do not establish
    a neutral-compound MIC, exact sulfate stoichiometry or regulatory approval.
  snapshot_sha256: be6713e512370cee1f2a7f7acdc9fb391bde95871f164a119eb6281f25bccf30
- evidence_id: patent2
  kind: primary_source
  reference: https://patents.google.com/patent/CN101575354A/en
  locator: CN101575354A Background, synthetic method, Example1 step6 and subsequent
    arbekacin steps
  accessed_at: '2026-10-21T14:22:03.796351Z'
  support: context_only
  summary: This patent isolates dibekacin as an intermediate by hydrogenation of unsaturated
    kanamycin B followed by ion exchange, before later arbekacin synthesis. It supports
    document relevance; dibekacin is not interchangeable with arbekacin, and acetic-acid
    solvent does not establish an isolated acetate salt.
  snapshot_sha256: 3eedac9d416c225697f6b46e5f8733e20b2021aa62e3d27ac45d9917baa5cc1a
- evidence_id: sulfate
  kind: authority
  reference: https://www.mhlw.go.jp/content/11120000/000904440.pdf
  locator: Japanese Pharmacopoeia XVIII monograph Dibekacin Sulfate, printed page845
  accessed_at: '2026-10-21T14:28:08.055191Z'
  support: context_only
  summary: 'The monograph defines C18H37N5O8·xH2SO4 and expresses potency in terms
    of the dibekacin moiety. This confirms the form boundary: product or standard
    sulfate potency does not make the neutral native graph a sulfate structure.'
  snapshot_sha256: 2a3d28b73c4b1d24d4195e377a99b8025d8d8b0e0765b4765729bf6e6ba1af5c
- evidence_id: icacine
  kind: authority
  reference: https://circulaires.ameli.fr/sites/default/files/directives/cir/1997/970922-C.PDF
  locator: French health-insurance circular1997; actual printed page32 viewed, product
    rows3249993 and3233963
  accessed_at: '2026-10-21T14:28:50.991864Z'
  support: supports
  summary: The official historical list identifies ICACINE 25 MG and ICACINE 75 MG
    as dibekacin injection ampoules. This establishes a product/brand name rather
    than a chemical exact synonym. This source does not specify sulfate stoichiometry
    or establish current marketing status.
  snapshot_sha256: 16aa6d51f631a9e44846d4c972df4ec82172c0970e61d8a533b4ef6f12de3e48
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: 358359-adapter-results.json; catalog325-adapter-catalog-network.json
  accessed_at: '2026-10-21T14:34:34Z'
  support: context_only
  summary: Structured queries preceded protein follow-up. E. coli precise1k rrsB and
    armA returned no gene/component matches. The catalog does not cover all donor
    strains in the imported panel; no expression-module association or biological
    absence is inferred.
  snapshot_sha256: 40b08605e857ca5cd8c4ce00031fecfe236a176bab2a9df96019cf67b0027584
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local search and free original-source retrieval
  locator: 358360-local-focused.txt;359-discovery.json; fetch manifests
  accessed_at: '2026-10-21T14:22:05.498701Z'
  support: context_only
  summary: All five adopted leads were disposed by actual reading depth. Original
    1971,1978 and1981 pages and the 2012 main text were accessible. The 2012 supplementary
    PDF/index returned HTML challenge content, and the XML endpoint failed; the supplemental
    exact enzyme/strain MIC rows were not inspected. The official Icacine circular
    was accessible while the secondary BIAM page returned 403.
  snapshot_sha256: 115281ee074f8620d5d85543558c5521fc30716617bc4bf9f4349c18b58188c3
  search_scope: 2026-10-21; dibekacin, dideoxykanamycin B, CHEBI:37945, ARO:0000007,
    Icacine and every adopted PMID. Local exact-reference search included ignored
    and hidden files. Primary follow-up covered exact identity, activity, ribosome
    experiments and the ANT(4-prime) substrate question; this is not an exhaustive
    review of all aminoglycoside alleles.
- evidence_id: gates
  kind: validation
  reference: Focused native validation and standalone chemistry
  locator: 359-focused-results.json
  accessed_at: '2026-10-21T14:34:34Z'
  support: supports
  summary: Schema, strict and chemistry all exited 0. Native validators used batch036;
    RDKit used the existing batch019 interpreter against batch036 cwd.
  snapshot_sha256: 25ef07ab014f5c3930b2a6e08bde8a38ce2e5722570240faeff434ac1d872711
- evidence_id: orbicin-boundary
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/7461562/
  locator: Original abstract PMID7461562; comparator PMID582126 in359-discovery.json
  accessed_at: '2026-10-21T14:22:05.498701Z'
  support: context_only
  snapshot_sha256: 115281ee074f8620d5d85543558c5521fc30716617bc4bf9f4349c18b58188c3
  summary: Both original abstracts explicitly pair dibekacin with the name Orbicin.
    PMID7461562 describes 29 surgical patients and 10 healthy volunteers; PMID582126
    describes tube-dilution and cross-resistance experiments. Neither inspected abstract
    identifies formulation, salt, catalog or official product status. They establish
    historical name usage, while exact synonym-versus-brand typing remains unresolved
    without product documentation. No numerical endpoint is transferred.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact structure and names
  outcome: concern
  summary: Chemical identity and stereochemistry are coherent. Icacine is a confirmed
    injection name typed as EXACT_SYNONYM; the other unusual commercial-looking names
    are retained as unresolved source nomenclature rather than assigned speculative
    corrections.
  target_ids:
  - CHEBI:37945
  evidence_ids:
  - chemistry
  - chebi
  - synthesis1971
  - icacine
- assessment_id: grounding
  area: grounding
  topic: Parents and all asserted chemical/document links
  outcome: supported
  summary: ChEBI, ARO, PubChem, ChEMBL, KEGG and DrugCentral resolve coherently. The
    adopted CAS and Reaxys labels remain source authority assertions; the protected
    Reaxys record was not independently accessed. Both native patent references concern
    dibekacin.
  target_ids:
  - CHEBI:37945
  evidence_ids:
  - chebi
  - aro
  - pubchem
  - chembl
  - kegg
  - drugcentral
  - patent1
  - patent2
- assessment_id: classification
  area: scope
  topic: Eligibility, roles, mode and target scope
  outcome: supported
  summary: Compound-specific synthesis/antibacterial experiments and cell-free translation
    inhibition support the antibacterial role and protein-synthesis mode. HOST_SHARED_TARGET
    describes the general source process rather than clinical selectivity; mammalian
    translation comparison does not imply identical bacterial and host potency.
  target_ids:
  - CHEBI:37945
  evidence_ids:
  - synthesis1971
  - activity1981
  - target2012
  - owners
- assessment_id: target
  area: evidence
  topic: Imported 16S rRNA target
  outcome: supported
  summary: The native target remains a qualified database assertion requiring primary
    evidence. Original rRNA-mutant translation data support functional involvement;
    protein-fraction reconstitution does not supply direct isolated-protein binding.
    These papers do not warrant silently upgrading the source-only relation to a primary
    direct-binding claim.
  target_ids:
  - CHEBI:37945
  evidence_ids:
  - native
  - target2012
  - ribosome1981
- assessment_id: resistance
  area: evidence
  topic: All 65 imported resistance claims
  outcome: supported
  summary: Every source edge, label, mechanism type and qualification was read and
    reconciled. Current term definitions and bounded original enzyme evidence support
    retaining the database tier; the review does not claim all 65 alleles were validated
    in dibekacin-specific original assays.
  target_ids:
  - CHEBI:37945
  evidence_ids:
  - aro-audit
  - ant1978
  - target2012
  - owners
- assessment_id: activity
  area: completeness
  topic: Optional activity_spectrum
  outcome: supported
  summary: Exact dibekacin antibacterial measurements are available. Curation should
    preserve reagent-form uncertainty, selected isolate panels and original assay
    conditions; cell-free IC50 and ocular viability scores are separate endpoints.
    Optional activity absence is not a required-field defect.
  target_ids:
  - CHEBI:37945
  evidence_ids:
  - activity1981
  - activity1981-tables
  - synthesis1971
  - target2012
  - ocular2010
- assessment_id: adopted
  area: evidence
  topic: All five adopted citations
  outcome: supported
  summary: Two original studies were assessed at full-text or abstract depth, while
    the three reviews were explicitly identified as secondary sources. No review metadata
    or precursor-production result was converted into direct dibekacin mechanism or
    producer evidence.
  target_ids:
  - CHEBI:37945
  evidence_ids:
  - ocular2010
  - adopted-20936279
  - adopted-11083623
  - adopted-10103173
  - adopted-8385262
- assessment_id: clinical
  area: scope
  topic: Product names and salt boundary
  outcome: concern
  summary: The neutral chemical record is coherent, but confirmed Icacine product
    naming should use BRAND_NAME. Sulfate monograph and ophthalmic formulation evidence
    must retain their separate ingredient/material scope; no FDA product field is
    asserted.
  target_ids:
  - CHEBI:37945
  evidence_ids:
  - icacine
  - sulfate
  - ocular2010
  - orbicin-boundary
- assessment_id: other
  area: scope
  topic: Producer, causal graph and datasets
  outcome: not_applicable
  summary: No such native assertions occur. Engineering a precursor-producing strain
    is not evidence that the strain produces dibekacin. No causal graph is inferred
    from translation inhibition alone.
  target_ids:
  - CHEBI:37945
  evidence_ids:
  - native
  - adopted-20936279
  - target2012
- assessment_id: provenance
  area: provenance
  topic: Maintained ownership and history
  outcome: supported
  summary: The source merge, two source mints, SEEDED status and five generated events
    are consistent. All originally captured inputs remain unchanged; actual ARO and
    target-qualification owners are included.
  target_ids:
  - CHEBI:37945
  evidence_ids:
  - owners
  - native
  - chemistry
- assessment_id: schema
  area: schema
  topic: Focused checks
  outcome: supported
  summary: Schema, strict and chemistry pass; shared same-base corpus gates are attached
    separately by root.
  target_ids:
  - CHEBI:37945
  evidence_ids:
  - gates
findings:
- finding_id: F1
  issue_key: AntibioticMech.CHEBI-37945.icacine-brand-synonym
  category: identity
  severity: minor
  status: open
  certainty: confirmed
  target_ids:
  - CHEBI:37945
  field_paths:
  - synonyms[10].synonym_type
  evidence_ids:
  - native
  - icacine
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted Icacine name
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source synonym extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Synonym-type emission
  description: Icacine is listed as EXACT_SYNONYM even though the official historical
    product list identifies it as a dibekacin injection brand. Retype this confirmed
    product name as BRAND_NAME while preserving the neutral compound identity and
    its source provenance.
  title: Icacine product name is typed as an exact chemical synonym
  native_severity: minor
  normalization_reason: 'Native review-checklist Identity and Clinical status rules:
    a bounded nomenclature typing error; it does not alter the exact graph or invalidate
    antibacterial eligibility.'
actions:
- action_id: A1
  description: Correct confirmed product-name typing through the maintained source/generation
    path.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:37945
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted Icacine name
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source synonym extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Synonym-type emission
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Regenerated Icacine uses BRAND_NAME and retains source provenance.
  - Do not infer a sulfate stoichiometry, current marketing status or corrections
    to Panamicin/Kappati from this historical list.
  - Run schema, strict and corpus-reproduction gates after authorized curation.
- action_id: A2
  description: Optionally curate original dibekacin activity and rRNA-dependent mechanism
    with exact evidence placement.
  finding_ids: []
  target_ids:
  - CHEBI:37945
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/dibekacin.yaml
    role: Curator-owned primary evidence/history
  acceptance_checks:
  - Preserve original reagent description and unresolved salt form, strain, units
    and assay conditions.
  - Keep translation IC50, whole-cell MIC, enzyme modification and ocular toxicity
    separate.
  - Resolve supplemental exact allele/strain rows before adding quantitative resistance
    observations; do not extrapolate the ANT-I example to all alleles.
  - Do not call reconstitution with S9/L6 fractions direct binding to purified proteins
    or use kanamycin A crystallography as dibekacin structural evidence.
limitations:
- All 65 native ARO templates, adopted edges and live term definitions were read.
  Original experiments were assessed for a bounded subset; the report is not independent
  primary validation of all 65 allele-specific drug relationships.
- All five adopted leads were resolved. The 2010 ocular paper was read in full relevant
  sections; the biosynthesis study at original abstract depth; three reviews at metadata/available
  abstract depth. Their full bibliographies were not adjudicated.
- The 2012 original main text and Table2 were read, but its supplementary exact resistance/MIC
  panel returned challenge content. Source material salt is unspecified in several
  assays; no sulfate/free-base numerical conversion was invented.
- Reaxys was not independently accessed. The source names Panamicin and Kappati were
  not conclusively resolved to current product records. Only the confirmed Icacine
  typing is a finding. Orbicin was checked in original abstracts PMID7461562 and PMID582126;
  historical name usage is supported, but official product identity, salt and synonym
  typing remain unresolved.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native/source/status/history was edited. Optional links, tags and notes were
  checked against dibekacin.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:37945
- https://doi.org/10.7164/antibiotics.24.485
- https://doi.org/10.1128/AAC.01326-12
- https://doi.org/10.7164/antibiotics.31.343
tags:
- dibekacin
- aminoglycoside
- 16S-rRNA
- database-evidence
- brand-synonym
```
