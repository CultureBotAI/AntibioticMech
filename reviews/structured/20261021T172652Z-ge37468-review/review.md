# GE37468: PubChem fallback omits the methyloxazole oxygen

- Review: 20261021T172652Z-ge37468-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T17:15:10Z
- Finished UTC: 2026-10-21T17:26:52Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The stored O11 PubChem fallback is internally valid but does not represent natural GE37468A: original 1995 structure work and the adopted 2011 paper show an O12 methyloxazole-containing molecule. Current ChEBI and ChEMBL confirm that constitution but differ in stereochemical annotation. The definition also misnames post-translational maturation as post-transcription modification. Primary activity and producer evidence are retained for the correctly mapped natural material.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 492; original thirteen input hashes preserved within twenty-nine captured inputs, with actual source owners and local review context appended before detailed assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-7d06ad4acd | data/antibiotics/antibacterial/ge37468.yaml | generated | GE37468 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-7d06ad4acd | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-7d06ad4acd | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-7d06ad4acd | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | antibioticmech:aro-7d06ad4acd | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-7d06ad4acd | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-7d06ad4acd | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-7d06ad4acd | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-7d06ad4acd | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-7d06ad4acd | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-7d06ad4acd | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-7d06ad4acd | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-7d06ad4acd | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Natural GE37468A constitution versus fallback

identity: concern. Targets: antibioticmech:aro-7d06ad4acd.

The native O11 graph is the wrong constitution for the named natural antibiotic. Original 1995 MS/NMR/figures and adopted 2011 figure establish an O12 methyloxazole; current ChEBI/ChEMBL agree on that constitution. The PubChem fallback faithfully reproduces the erroneous O11 structure.

### Residual stereochemical uncertainty

identity: unknown. Targets: antibioticmech:aro-7d06ad4acd.

The native graph has4 defined/3 unassigned centres; current ChEBI0/7 and ChEMBL5/2 differ. The 2011 primary explicitly leaves mhP8 stereochemistry unassigned. Constitution can be corrected decisively, but the final stereochemical graph requires separate source adjudication, not blind authority copying.

### Mint, exact xrefs and broader class

grounding: concern. Targets: antibioticmech:aro-7d06ad4acd.

ARO mint calculation is valid and PubChem exact graph matches the native representation. ChEBI/ChEMBL exact xrefs contradict its O11 constitution. Elfamycin broader class and antibacterial eligibility are supported for the natural O12 compound.

### Post-translational biosynthesis and producer

nomenclature: concern. Targets: antibioticmech:aro-7d06ad4acd.

Source organism/strain and ribosomal preprotein biosynthesis are supported. Post-transcription modification is incorrect for the peptide maturation demonstrated by the adopted source; it should be post-translational.

### Natural-material antibacterial assays

evidence: supported. Targets: antibioticmech:aro-7d06ad4acd.

Purified original GE37468A has strain-specific MIC and experimental mouse efficacy evidence;2011 engineered/wild-type material provides additional bounded activity. These support the intended natural antibiotic, and must not be assigned to the current O11 graph until identity is repaired.

### Functional EF-Tu evidence and biosynthetic enzymes

scope: supported. Targets: antibioticmech:aro-7d06ad4acd.

Cell-free protein-synthesis inhibition, cross-resistance and extracellular EF-Tu antagonism support the natural product mechanism. GetJ and other maturation proteins are biosynthetic context, not antimicrobial targets. No native molecular target or resistance object is overclaimed.

### Sole adopted lead and optional annotations

completeness: unknown. Targets: antibioticmech:aro-7d06ad4acd.

The adopted 2011 main paper was fully read; SI remained unavailable. The 1995 original structure/isolation and1997screen were read. Optional activity/producer/target/graph fields are not required missing representations; natural-material mapping must precede enrichment.

### Actual fallback owner and three history events

provenance: supported. Targets: antibioticmech:aro-7d06ad4acd.

Twenty-nine hashes preserve the original thirteen. Source fallback, actual ARO row, absent ChEBI lookup row, current authorities and all three native history events were inspected. The minted label/source remains SEEDED.

### Internal gates versus wrong chemical identity

schema: supported. Targets: antibioticmech:aro-7d06ad4acd.

Native schema/strict/chemistry pass because all stored fields consistently encode the same wrong O11 graph. This does not overcome original chemical evidence.

## Findings

### F1: The fallback structure lacks the methyloxazole oxygen of GE37468A

blocker / open / confirmed; issue key: ge37468-pubchem-fallback-missing-methyloxazole-oxygen.

The native record encodes C59H52N14O11S5 with a five-member nitrogen/carbon ring at the chromophore position where original GE37468A has a methyl-substituted oxazole. The 1995 isolation/structure papers report C59H52N14O12S5 and explicitly establish methyloxazole by NMR; their figures and the adopted 2011 Figure 1 agree. Current ChEBI199144/ChEMBL4646154 have that O12 constitution, whereas adopted and current PubChem101808822 reproduce the erroneous O11 graph. This is not a hydration, salt or tautomer difference. The exact identity/biological material mapping is broken even though internal validators pass.

### F2: The definition misnames peptide maturation as post-transcription modification

minor / open / confirmed; issue key: ge37468-post-transcription-peptide-maturation-wording.

The adopted 2011 paper demonstrates extensive post-translational modification of a ribosomally synthesized preprotein. Native and ARO wording say post-transcription modification, which refers to a different molecular stage. Correct this localized phrase without changing the supported producer, ribosomal precursor or gene-cluster claim.

## Recommended Actions And Acceptance Checks

### A1

Replace or re-ground the erroneous PubChem fallback using primary-adjudicated GE37468A identity.

- Use original 1995 MS/NMR/Figs 3/6 and adopted 2011 Figure 1 to establish the O12 methyloxazole constitution. Recompute SMILES/InChI/key/formula/charge/masses coherently.
- Separately adjudicate stereochemistry: the 2011 paper leaves mhP8 unassigned, and current ChEBI/ChEMBL differ. Do not blindly copy either graph or equate unassigned centres to a racemate.
- Reconcile all exact xrefs and minted-versus-ChEBI grounding after the structure decision. Do not keep PubChem101808822 as exact if it still encodes O11. Preserve source provenance and avoid transferring native measurements to a new identity silently.
- Regenerate through maintained owners, run chemical/xref, schema/strict, reference/history, reproduction and QC checks, and inspect the exact regenerated record.

### A2

Correct the ARO-derived definition to post-translational modification.

- Change the maintained source handling or upstream adopted assertion, preserve PMID21788474 and regenerate reproducibly.
- Verify the definition still identifies Streptomyces ATCC 55365 and ribosomally synthesized precursor maturation; run focused and corpus gates.

### A3

Optional later curation: record natural-material activity, producer and EF-Tu mechanism with bounded assays.

- Resolve the identity blocker before attaching1995/2011 measurements. Preserve O12 material, strain, medium, time, units and wild-type versus analog boundaries.
- Do not call the 1997 EF-Tu decoy screen a quantitative binding assay, label GetJ an antimicrobial target, or turn mouse ED50 into clinical status.
- Use primary claim-level citations and the validated writer/history process only in separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owners | data/raw/aro_antibiotics.tsv; data/raw/chebi_antimicrobials.tsv; data/raw/pubchem_structures.tsv; Exact source rows and readiness; extractor, fallback and seeder branches | supports | Actual ARO source, chemical fallback, target/resistance owner tables and qualification configuration were captured and read. All original thirteen input hashes remain intact. Generated source provenance is retained; this review does not promote SEEDED status. |
| search | 491492-local-hits.txt; Ignored-inclusive local search across data/raw, curation, conf, docs and reports, plus initial capture search | context_only | Exact record/label/ARO/ChEBI hits and full maintained-table selections were inspected. Historical reports are discovery context only. No exact curator or grounding-decision row was found in the directly inspected complete maintained tables. Optional omissions are not schema violations. |
| chemistry | 492-chemistry.json; Both native SMILES and InChI independently parsed; formula, charge, exact/average mass, key and source mint | supports | RDKit 2026.03.5 from the existing batch019 interpreter was run with batch050 as cwd. All local chemistry assertions and calculated source mint agree. This checks internal consistency, not identity against original natural material. |
| comparison | 491492-chem-compare.json; Native versus current ChEBI, PubChem and ChEMBL graph/stereo comparison | supports | Independent parsing compares full and stereo-stripped InChIKeys, formula and assigned/unassigned stereocentres. Current external source responses are preserved separately; source name equality was not used as chemical equivalence. |
| gates | 492-focused-results.json; Actual focused chemistry, schema and strict commands executed in batch050 | supports | All three commands exited zero. Schema/strict used the batch050 frozen environment with UV_NO_SYNC=1; chemistry used the existing batch019 RDKit environment against batch050 cwd. |
| parent | https://www.ebi.ac.uk/ols4/ontologies/aro/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FARO_3001219; ARO:3001219 definition and references | supports | Elfamycins are defined by the EF-Tu target, rather than a common backbone. This is a broader functional antibiotic class and is not an exact molecular identity. PMID12370016 and PMID16876786 are mechanistic reviews, not new exact-material activity experiments. |
| access | 491492-fetch1.json through 491492-fetch6.json; Actual HTTP responses, URLs, UTC accesses and SHA-256 digests | context_only | Free official chemical databases and J-STAGE original PDFs were retrieved. Some EPMC fullTextXML routes returned 500; PMC HTML was used where available. Wiley/ACS/RSC publisher routes returned 403. The PNAS SI route returned 403 and its PMC download route returned an HTML browser challenge, not a PDF. Failed requests are retained as access limits, not read full texts. An initial guessed1991J-STAGE URL failed and was replaced by the verified DOI-derived URL. Legacy ChEBI CCD lead GEA returned404; guessed GE2 was not used as evidence. |
| native | data/antibiotics/antibacterial/ge37468.yaml; Entire record and all three seed/reseed events | supports | The minted ARO3001259 record uses PubChem101808822 fallback, C59H52N14O11S5, key IZEAZUCUNIRFMQ-SBZMANJYSA-N, four assigned and three unassigned tetrahedral centres. It asserts exact ChEBI199144/ChEMBL4646154/PubChem xrefs, species/strain producer wording and one adopted PMID. No quantitative target, resistance, activity, causal, clinical product or dataset collection is asserted. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/101808822/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON; CID101808822 current properties | refutes | The current PubChem entry reproduces the exact native O11 graph, not an O12 hydrate or formula-only typo. Its five-member nitrogen/carbon ring replaces the methyloxazole at this position; the difference is constitutional and persists after stereo removal. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/199144/; CHEBI:199144 GE37468A current default structure | supports | Current ChEBI has formula C59H52N14O12S5 and key AABZZWPMCAZHFC-UHFFFAOYSA-N. Its methyloxazole matches original constitutional evidence, but all seven stereocentres are unassigned; the two-star entry is not an automatically adjudicated exact natural stereochemical standard. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL4646154.json; CHEMBL4646154 current molecule structure | supports | ChEMBL also has the O12 methyloxazole constitution, key AABZZWPMCAZHFC-GYCYHCAVSA-N, with five assigned and two unassigned centres. It cannot be claimed exact-equivalent to the native O11 graph or copied wholesale to resolve stereochemistry. |
| aro | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3001259; ARO3001259 definition, xrefs and PMID21788474 | supports | Live ARO repeats the compound/producer and post-transcription wording and points to the sole adopted primary PMID21788474. The source concept has no experimentally established O11 identity. The native fallback/source transform explains why the internally consistent wrong graph is present. |
| structure | DOI:10.7164/antibiotics.48.1304; Original 1995 full paper, pp 1304–1311; formula p 1305, NMR Table3, Fig 3 p 1308 and Fig 6 p 1310 | refutes | Purified lyophilized GE37468A from Streptomyces sp. ATCC 55365 has neutral formula C59H52N14O12S5, theoretical monoisotopic mass 1308.24927 and molecular mass 1309.48. MS losses/adducts and NMR/hydrolysis establish a methyloxazole with a methyl singlet 2.73 ppm, rather than the native carbon/nitrogen-only ring. This is an oxygen/connectivity defect, not salt, solvate or tautomer normalization. |
| structure-figure | DOI:10.7164/antibiotics.48.1304; Actual Figure3 image p 1308 visually inspected | refutes | The original figure labels and draws the methyloxazole in the chromophore. The accompanying NMR discussion expressly assigns this ring. The figure was inspected directly alongside native and authority graph renderings. |
| isolation | DOI:10.7164/antibiotics.48.780; Original 1995 full paper pp 780–786; purification/methods, actual Table 5 p 783, Table 6 p 785 | supports | Streptomyces sp. ATCC 55365 was isolated from Lamole, Italy soil. Chromatographic purification yields GE37468A white powder; p 783 independently gives O12 formula and Fig1 methyloxazole. Table 5 broth microdilution MICs include S. aureus Smith 0.016 mg/L, E. faecalis ATCC 7080 0.016 mg/L and B. fragilis ATCC 25285 4 mg/L. GE2270A is a separate comparator. Inocula10^4 CFU/mL, anaerobes10^5; incubation20–24 h, specified organisms48 h, with species-specific media/atmospheres. |
| activity-table | DOI:10.7164/antibiotics.48.780; Actual p 783 Table 5 and Figure 1 visually inspected | supports | GE37468A and GE2270A columns were distinguished directly. O12 formula and oxazole structure are visible on the same original page as the MIC table; these measurements concern the O12 natural product, not the current native O11 structure. |
| mechanism | DOI:10.7164/antibiotics.48.780; Methods p 781 and results pp 784–785, Figs2–3 and Table 6 | supports | In B. subtilis566/1,1 mg/L selectively blocks protein synthesis early; E. coli cell-free poly (Phe) IC50 is1 mg/L with little rat-liver effect through50 mg/L. S. aureus L165 GE2270-selected derivative has GE37468A MIC&gt;128 µg/mL versus parental 0.016; this is cross-resistance evidence, not an identified allele or an atomic binding experiment. IV mouse ED50 3.2 mg/kg is experimental S. aureus septicemia, not clinical approval. |
| adopted | PMID:21788474; DOI:10.1073/pnas.1110435108; Original 2011 full PMC text, all main methods/results and Figure 1 | supports | The sole adopted primary identifies a ribosomally synthesized precursor modified post-translationally, with getA–M cluster sequencing, heterologous S. lividans TK24 expression and original producer comparison. HPLC-purified wild-type material from both hosts gives MRSA MW2 activity0.047 µg/mL and the same B. subtilis168 activity; altered mhP8I/mhP8A products are distinct analogs. The main text explicitly leaves GE37468 mhP8 stereochemistry unassigned; biosynthetic analogy to thiomuracin cannot silently supply it. |
| adopted-figure | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/e1c1/3156177/7fa0a2775ac9/pnas.1110435108fig1.jpg; Actual2011 Figure 1 viewed | refutes | The adopted source draws a methyloxazole at residue2, agreeing with the original O12 constitution. Other wedge/dash information and the explicit mhP8 uncertainty must be reconciled separately before a fully stereodefined exact record is adopted. |
| screen | DOI:10.7164/antibiotics.50.22; Original 1997 full paper, methods p 23 and selection/discussion pp 24–25 | supports | Free E. coliK12 EF-Tu was used as an extracellular decoy in disc-diffusion screens against S. aureus ATCC 6538 and M. caviae ATCC 14659; buffer/BSA and DTT reactivity controls were considered. GE37468-producing broth was selected by EF-Tu antagonism. This supports the target-directed discovery context, not a purified GE37468-EF-Tu dissociation constant or new exact-material MIC. |
| adapter | 456460-adapter-catalog.txt; Structured catalog coverage inspected before mechanism follow-up | context_only | Native names no specific biosynthetic protein/locus, and catalog has no matching Streptomyces ATCC 55365 dataset. Related E. coli tufA query was performed for 491 before shared mechanism research; it is gene annotation context only and not transferred as GE37468 evidence. |

## Limits And Additional Notes

- Required shared full-corpus checks are incorporated separately by the root reviewer before finalization; the actual focused gates are recorded here.
- The 2011 main text and actual structure figure were read, but SI retrieval failed (publisher 403; PMC HTML challenge). Main-text0.047 µg/mL activity is retained with serial-dilution/HPLC-purified material scope; uninspected SI media, inoculum and endpoint details are not invented.
- Absolute stereochemistry is not fully resolved by this review. The 2011 source explicitly states mhP8 had not been assigned; current authority stereo variants differ and require separate primary adjudication after the constitution correction.
- The 1995/2011 antibacterial results establish the natural O12 compound. No inspected experiment proves antibacterial activity of the stored O11 constitutional variant. The review does not claim that variant is necessarily inactive.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native record, source inventory, curation history, progress file or immutable review was modified. The scratch draft is handed off for root audit and ordered persistence.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T172652Z-ge37468-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'GE37468: PubChem fallback omits the methyloxazole oxygen'
started_at: '2026-10-21T17:15:10Z'
finished_at: '2026-10-21T17:26:52Z'
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
summary: 'The stored O11 PubChem fallback is internally valid but does not represent
  natural GE37468A: original 1995 structure work and the adopted 2011 paper show an
  O12 methyloxazole-containing molecule. Current ChEBI and ChEMBL confirm that constitution
  but differ in stereochemical annotation. The definition also misnames post-translational
  maturation as post-transcription modification. Primary activity and producer evidence
  are retained for the correctly mapped natural material.'
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
  - path: data/antibiotics/antibacterial/ge37468.yaml
    sha256: caf08bff09e514a341af31d0018ccc8ee01da663364cde608f7c7b7477e974b4
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
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
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
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
targets:
- target_id: antibioticmech:aro-7d06ad4acd
  path: data/antibiotics/antibacterial/ge37468.yaml
  label: GE37468
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity, definition, chemical cross-references and bibliography
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI structure lookup when available
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: ARO-associated PubChem fallback structures
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO and ChEBI source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem fallback retrieval
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion overrides
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 492; original thirteen input hashes preserved within twenty-nine
    captured inputs, with actual source owners and local review context appended before
    detailed assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-7d06ad4acd
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-7d06ad4acd
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    492
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-7d06ad4acd
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/ge37468.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-7d06ad4acd
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/ge37468.yaml --out /private/tmp/am-review-session/492-strict.tsv
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
  - antibioticmech:aro-7d06ad4acd
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
  - antibioticmech:aro-7d06ad4acd
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
  - antibioticmech:aro-7d06ad4acd
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
  - antibioticmech:aro-7d06ad4acd
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
  - antibioticmech:aro-7d06ad4acd
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
  - antibioticmech:aro-7d06ad4acd
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
  - antibioticmech:aro-7d06ad4acd
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
  - antibioticmech:aro-7d06ad4acd
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
  - antibioticmech:aro-7d06ad4acd
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/chebi_antimicrobials.tsv; data/raw/pubchem_structures.tsv
  locator: Exact source rows and readiness; extractor, fallback and seeder branches
  accessed_at: '2026-10-21T17:23:25Z'
  support: supports
  summary: Actual ARO source, chemical fallback, target/resistance owner tables and
    qualification configuration were captured and read. All original thirteen input
    hashes remain intact. Generated source provenance is retained; this review does
    not promote SEEDED status.
  snapshot_sha256: 17430f01c99c6bc0d427b7770c01d499f6746065eeb3bc9defab1889ce840ceb
- evidence_id: search
  kind: search
  reference: 491492-local-hits.txt
  locator: Ignored-inclusive local search across data/raw, curation, conf, docs and
    reports, plus initial capture search
  accessed_at: '2026-10-21T17:23:25Z'
  support: context_only
  summary: Exact record/label/ARO/ChEBI hits and full maintained-table selections
    were inspected. Historical reports are discovery context only. No exact curator
    or grounding-decision row was found in the directly inspected complete maintained
    tables. Optional omissions are not schema violations.
  snapshot_sha256: a31ab188c3862bacf79ba076ff06d03a0f0f4fb1bcc2c13fb8e1de14383f1985
  search_scope: rg --no-ignore --hidden across data/raw, curation, conf, docs and
    reports for both labels and exact ARO/ChEBI identifiers; initial full-worktree
    search and complete maintained-table exact-row inspection also included.
- evidence_id: chemistry
  kind: validation
  reference: 492-chemistry.json
  locator: Both native SMILES and InChI independently parsed; formula, charge, exact/average
    mass, key and source mint
  accessed_at: '2026-10-21T17:23:25Z'
  support: supports
  summary: RDKit 2026.03.5 from the existing batch019 interpreter was run with batch050
    as cwd. All local chemistry assertions and calculated source mint agree. This
    checks internal consistency, not identity against original natural material.
  snapshot_sha256: 2d17cd45915b63467ceae0af9f11db9da46e1ad6a5b10d79a51f95c6281db116
- evidence_id: comparison
  kind: validation
  reference: 491492-chem-compare.json
  locator: Native versus current ChEBI, PubChem and ChEMBL graph/stereo comparison
  accessed_at: '2026-10-21T17:23:25Z'
  support: supports
  summary: Independent parsing compares full and stereo-stripped InChIKeys, formula
    and assigned/unassigned stereocentres. Current external source responses are preserved
    separately; source name equality was not used as chemical equivalence.
  snapshot_sha256: 565a265d0d53a5c98cbc4fd1b478dc915811d1f266dd85561424eb395ae06c3a
- evidence_id: gates
  kind: validation
  reference: 492-focused-results.json
  locator: Actual focused chemistry, schema and strict commands executed in batch050
  accessed_at: '2026-10-21T17:23:25Z'
  support: supports
  summary: All three commands exited zero. Schema/strict used the batch050 frozen
    environment with UV_NO_SYNC=1; chemistry used the existing batch019 RDKit environment
    against batch050 cwd.
  snapshot_sha256: 291e95bec463e7014d29fc0606bf97dab5c75a4456ba05c7a11c2e0dae27b4fc
- evidence_id: parent
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/ontologies/aro/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FARO_3001219
  locator: ARO:3001219 definition and references
  accessed_at: '2026-10-21T17:17:29.629997Z'
  support: supports
  summary: Elfamycins are defined by the EF-Tu target, rather than a common backbone.
    This is a broader functional antibiotic class and is not an exact molecular identity.
    PMID12370016 and PMID16876786 are mechanistic reviews, not new exact-material
    activity experiments.
  snapshot_sha256: 062102bcad4324c79e0f537e00f5eddaa8dd2933038cd2597518306ca426058e
- evidence_id: access
  kind: validation
  reference: 491492-fetch1.json through 491492-fetch6.json
  locator: Actual HTTP responses, URLs, UTC accesses and SHA-256 digests
  accessed_at: '2026-10-21T17:23:25Z'
  support: context_only
  summary: Free official chemical databases and J-STAGE original PDFs were retrieved.
    Some EPMC fullTextXML routes returned 500; PMC HTML was used where available.
    Wiley/ACS/RSC publisher routes returned 403. The PNAS SI route returned 403 and
    its PMC download route returned an HTML browser challenge, not a PDF. Failed requests
    are retained as access limits, not read full texts. An initial guessed1991J-STAGE
    URL failed and was replaced by the verified DOI-derived URL. Legacy ChEBI CCD
    lead GEA returned404; guessed GE2 was not used as evidence.
  snapshot_sha256: 1e5cf8759b098adf72cf8ae51f6e5076eece2493ae618663d2e9b2525fb54860
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/ge37468.yaml
  locator: Entire record and all three seed/reseed events
  accessed_at: '2026-10-21T17:23:25Z'
  support: supports
  summary: The minted ARO3001259 record uses PubChem101808822 fallback, C59H52N14O11S5,
    key IZEAZUCUNIRFMQ-SBZMANJYSA-N, four assigned and three unassigned tetrahedral
    centres. It asserts exact ChEBI199144/ChEMBL4646154/PubChem xrefs, species/strain
    producer wording and one adopted PMID. No quantitative target, resistance, activity,
    causal, clinical product or dataset collection is asserted.
  snapshot_sha256: caf08bff09e514a341af31d0018ccc8ee01da663364cde608f7c7b7477e974b4
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/101808822/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON
  locator: CID101808822 current properties
  accessed_at: '2026-10-21T17:17:28.254991Z'
  support: refutes
  summary: The current PubChem entry reproduces the exact native O11 graph, not an
    O12 hydrate or formula-only typo. Its five-member nitrogen/carbon ring replaces
    the methyloxazole at this position; the difference is constitutional and persists
    after stereo removal.
  snapshot_sha256: 15444446548a1a55439d507284387eec99f5fa540f50c766b0f79f8c3c7222d8
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/199144/
  locator: CHEBI:199144 GE37468A current default structure
  accessed_at: '2026-10-21T17:17:27.885544Z'
  support: supports
  summary: Current ChEBI has formula C59H52N14O12S5 and key AABZZWPMCAZHFC-UHFFFAOYSA-N.
    Its methyloxazole matches original constitutional evidence, but all seven stereocentres
    are unassigned; the two-star entry is not an automatically adjudicated exact natural
    stereochemical standard.
  snapshot_sha256: c751f267b4be549fe8e16da081e506d34280d1f039cb308a8aebc3f4786dd5e6
- evidence_id: chembl
  kind: authority
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL4646154.json
  locator: CHEMBL4646154 current molecule structure
  accessed_at: '2026-10-21T17:17:28.592828Z'
  support: supports
  summary: ChEMBL also has the O12 methyloxazole constitution, key AABZZWPMCAZHFC-GYCYHCAVSA-N,
    with five assigned and two unassigned centres. It cannot be claimed exact-equivalent
    to the native O11 graph or copied wholesale to resolve stereochemistry.
  snapshot_sha256: 539367e14475d95d05852c146ca179a3b45ed87ce4dc56a86e7a936332b66b8c
- evidence_id: aro
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3001259
  locator: ARO3001259 definition, xrefs and PMID21788474
  accessed_at: '2026-10-21T17:17:28.646297Z'
  support: supports
  summary: Live ARO repeats the compound/producer and post-transcription wording and
    points to the sole adopted primary PMID21788474. The source concept has no experimentally
    established O11 identity. The native fallback/source transform explains why the
    internally consistent wrong graph is present.
  snapshot_sha256: 068eac9ca67df326be45e69720743675a65ed58b0da85b880e551c1ecb09644a
- evidence_id: structure
  kind: primary_source
  reference: DOI:10.7164/antibiotics.48.1304
  locator: Original 1995 full paper, pp 1304–1311; formula p 1305, NMR Table3, Fig
    3 p 1308 and Fig 6 p 1310
  accessed_at: '2026-10-21T17:18:08.637624Z'
  support: refutes
  summary: Purified lyophilized GE37468A from Streptomyces sp. ATCC 55365 has neutral
    formula C59H52N14O12S5, theoretical monoisotopic mass 1308.24927 and molecular
    mass 1309.48. MS losses/adducts and NMR/hydrolysis establish a methyloxazole with
    a methyl singlet 2.73 ppm, rather than the native carbon/nitrogen-only ring. This
    is an oxygen/connectivity defect, not salt, solvate or tautomer normalization.
  snapshot_sha256: ee98e8e6c72dae82a6714ce613a16df3444ac1cf54e72f374e18a7d6fc1d9950
- evidence_id: structure-figure
  kind: primary_source
  reference: DOI:10.7164/antibiotics.48.1304
  locator: Actual Figure3 image p 1308 visually inspected
  accessed_at: '2026-10-21T17:23:25Z'
  support: refutes
  summary: The original figure labels and draws the methyloxazole in the chromophore.
    The accompanying NMR discussion expressly assigns this ring. The figure was inspected
    directly alongside native and authority graph renderings.
  snapshot_sha256: 2deaa73eb7c7fea8f3b0917677882a13f8a7beace17eaef7982a8192ccd2701c
- evidence_id: isolation
  kind: primary_source
  reference: DOI:10.7164/antibiotics.48.780
  locator: Original 1995 full paper pp 780–786; purification/methods, actual Table
    5 p 783, Table 6 p 785
  accessed_at: '2026-10-21T17:18:08.637337Z'
  support: supports
  summary: Streptomyces sp. ATCC 55365 was isolated from Lamole, Italy soil. Chromatographic
    purification yields GE37468A white powder; p 783 independently gives O12 formula
    and Fig1 methyloxazole. Table 5 broth microdilution MICs include S. aureus Smith
    0.016 mg/L, E. faecalis ATCC 7080 0.016 mg/L and B. fragilis ATCC 25285 4 mg/L.
    GE2270A is a separate comparator. Inocula10^4 CFU/mL, anaerobes10^5; incubation20–24
    h, specified organisms48 h, with species-specific media/atmospheres.
  snapshot_sha256: 3d86c61cc6227e96a8747ee50bf523dc44639954118576046c6314082e13bd06
- evidence_id: activity-table
  kind: primary_source
  reference: DOI:10.7164/antibiotics.48.780
  locator: Actual p 783 Table 5 and Figure 1 visually inspected
  accessed_at: '2026-10-21T17:23:25Z'
  support: supports
  summary: GE37468A and GE2270A columns were distinguished directly. O12 formula and
    oxazole structure are visible on the same original page as the MIC table; these
    measurements concern the O12 natural product, not the current native O11 structure.
  snapshot_sha256: 65c5e2e356c85a82976e22a38606187afd6f1400a0dacef753913531f501e04d
- evidence_id: mechanism
  kind: primary_source
  reference: DOI:10.7164/antibiotics.48.780
  locator: Methods p 781 and results pp 784–785, Figs2–3 and Table 6
  accessed_at: '2026-10-21T17:18:08.637337Z'
  support: supports
  summary: In B. subtilis566/1,1 mg/L selectively blocks protein synthesis early;
    E. coli cell-free poly (Phe) IC50 is1 mg/L with little rat-liver effect through50
    mg/L. S. aureus L165 GE2270-selected derivative has GE37468A MIC>128 µg/mL versus
    parental 0.016; this is cross-resistance evidence, not an identified allele or
    an atomic binding experiment. IV mouse ED50 3.2 mg/kg is experimental S. aureus
    septicemia, not clinical approval.
  snapshot_sha256: 3d86c61cc6227e96a8747ee50bf523dc44639954118576046c6314082e13bd06
- evidence_id: adopted
  kind: primary_source
  reference: PMID:21788474; DOI:10.1073/pnas.1110435108
  locator: Original 2011 full PMC text, all main methods/results and Figure 1
  accessed_at: '2026-10-21T17:18:20.203210Z'
  support: supports
  summary: The sole adopted primary identifies a ribosomally synthesized precursor
    modified post-translationally, with getA–M cluster sequencing, heterologous S.
    lividans TK24 expression and original producer comparison. HPLC-purified wild-type
    material from both hosts gives MRSA MW2 activity0.047 µg/mL and the same B. subtilis168
    activity; altered mhP8I/mhP8A products are distinct analogs. The main text explicitly
    leaves GE37468 mhP8 stereochemistry unassigned; biosynthetic analogy to thiomuracin
    cannot silently supply it.
  snapshot_sha256: 0bfb635721febfe225939feeeaa59ddaa14e4f50efbc7e05fc409d2068a95489
- evidence_id: adopted-figure
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/e1c1/3156177/7fa0a2775ac9/pnas.1110435108fig1.jpg
  locator: Actual2011 Figure 1 viewed
  accessed_at: '2026-10-21T17:18:51.663236Z'
  support: refutes
  summary: The adopted source draws a methyloxazole at residue2, agreeing with the
    original O12 constitution. Other wedge/dash information and the explicit mhP8
    uncertainty must be reconciled separately before a fully stereodefined exact record
    is adopted.
  snapshot_sha256: 86df7fa6b9576116d80b798efd4de4d76851c9ebb3792dc0d735d9fad93839a9
- evidence_id: screen
  kind: primary_source
  reference: DOI:10.7164/antibiotics.50.22
  locator: Original 1997 full paper, methods p 23 and selection/discussion pp 24–25
  accessed_at: '2026-10-21T17:19:26.347180Z'
  support: supports
  summary: Free E. coliK12 EF-Tu was used as an extracellular decoy in disc-diffusion
    screens against S. aureus ATCC 6538 and M. caviae ATCC 14659; buffer/BSA and DTT
    reactivity controls were considered. GE37468-producing broth was selected by EF-Tu
    antagonism. This supports the target-directed discovery context, not a purified
    GE37468-EF-Tu dissociation constant or new exact-material MIC.
  snapshot_sha256: 02b5b23fa8b3c376f965ab9cc40b38aeaa2f0a6a38b420ea7e84b86239270ac8
- evidence_id: adapter
  kind: database
  reference: 456460-adapter-catalog.txt
  locator: Structured catalog coverage inspected before mechanism follow-up
  accessed_at: '2026-10-21T17:23:25Z'
  support: context_only
  summary: Native names no specific biosynthetic protein/locus, and catalog has no
    matching Streptomyces ATCC 55365 dataset. Related E. coli tufA query was performed
    for 491 before shared mechanism research; it is gene annotation context only and
    not transferred as GE37468 evidence.
  snapshot_sha256: 9380340a2e0f964d45a17286996f765b36339f7a2288faf5096be4913c8d694a
assessments:
- assessment_id: identity
  area: identity
  topic: Natural GE37468A constitution versus fallback
  outcome: concern
  summary: The native O11 graph is the wrong constitution for the named natural antibiotic.
    Original 1995 MS/NMR/figures and adopted 2011 figure establish an O12 methyloxazole;
    current ChEBI/ChEMBL agree on that constitution. The PubChem fallback faithfully
    reproduces the erroneous O11 structure.
  target_ids:
  - antibioticmech:aro-7d06ad4acd
  evidence_ids:
  - native
  - pubchem
  - structure
  - structure-figure
  - adopted-figure
  - comparison
- assessment_id: stereo
  area: identity
  topic: Residual stereochemical uncertainty
  outcome: unknown
  summary: The native graph has4 defined/3 unassigned centres; current ChEBI0/7 and
    ChEMBL5/2 differ. The 2011 primary explicitly leaves mhP8 stereochemistry unassigned.
    Constitution can be corrected decisively, but the final stereochemical graph requires
    separate source adjudication, not blind authority copying.
  target_ids:
  - antibioticmech:aro-7d06ad4acd
  evidence_ids:
  - comparison
  - chebi
  - chembl
  - adopted
- assessment_id: grounding
  area: grounding
  topic: Mint, exact xrefs and broader class
  outcome: concern
  summary: ARO mint calculation is valid and PubChem exact graph matches the native
    representation. ChEBI/ChEMBL exact xrefs contradict its O11 constitution. Elfamycin
    broader class and antibacterial eligibility are supported for the natural O12
    compound.
  target_ids:
  - antibioticmech:aro-7d06ad4acd
  evidence_ids:
  - owners
  - chemistry
  - aro
  - parent
  - chebi
  - chembl
  - isolation
- assessment_id: definition
  area: nomenclature
  topic: Post-translational biosynthesis and producer
  outcome: concern
  summary: Source organism/strain and ribosomal preprotein biosynthesis are supported.
    Post-transcription modification is incorrect for the peptide maturation demonstrated
    by the adopted source; it should be post-translational.
  target_ids:
  - antibioticmech:aro-7d06ad4acd
  evidence_ids:
  - aro
  - adopted
  - isolation
- assessment_id: activity
  area: evidence
  topic: Natural-material antibacterial assays
  outcome: supported
  summary: Purified original GE37468A has strain-specific MIC and experimental mouse
    efficacy evidence;2011 engineered/wild-type material provides additional bounded
    activity. These support the intended natural antibiotic, and must not be assigned
    to the current O11 graph until identity is repaired.
  target_ids:
  - antibioticmech:aro-7d06ad4acd
  evidence_ids:
  - isolation
  - activity-table
  - mechanism
  - adopted
- assessment_id: mechanism-scope
  area: scope
  topic: Functional EF-Tu evidence and biosynthetic enzymes
  outcome: supported
  summary: Cell-free protein-synthesis inhibition, cross-resistance and extracellular
    EF-Tu antagonism support the natural product mechanism. GetJ and other maturation
    proteins are biosynthetic context, not antimicrobial targets. No native molecular
    target or resistance object is overclaimed.
  target_ids:
  - antibioticmech:aro-7d06ad4acd
  evidence_ids:
  - mechanism
  - screen
  - adopted
  - adapter
- assessment_id: completeness
  area: completeness
  topic: Sole adopted lead and optional annotations
  outcome: unknown
  summary: The adopted 2011 main paper was fully read; SI remained unavailable. The
    1995 original structure/isolation and1997screen were read. Optional activity/producer/target/graph
    fields are not required missing representations; natural-material mapping must
    precede enrichment.
  target_ids:
  - antibioticmech:aro-7d06ad4acd
  evidence_ids:
  - native
  - adopted
  - access
  - structure
  - screen
- assessment_id: provenance
  area: provenance
  topic: Actual fallback owner and three history events
  outcome: supported
  summary: Twenty-nine hashes preserve the original thirteen. Source fallback, actual
    ARO row, absent ChEBI lookup row, current authorities and all three native history
    events were inspected. The minted label/source remains SEEDED.
  target_ids:
  - antibioticmech:aro-7d06ad4acd
  evidence_ids:
  - owners
  - native
  - search
- assessment_id: validation
  area: schema
  topic: Internal gates versus wrong chemical identity
  outcome: supported
  summary: Native schema/strict/chemistry pass because all stored fields consistently
    encode the same wrong O11 graph. This does not overcome original chemical evidence.
  target_ids:
  - antibioticmech:aro-7d06ad4acd
  evidence_ids:
  - gates
  - chemistry
  - structure
  - comparison
findings:
- finding_id: F1
  issue_key: ge37468-pubchem-fallback-missing-methyloxazole-oxygen
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: The fallback structure lacks the methyloxazole oxygen of GE37468A
  description: The native record encodes C59H52N14O11S5 with a five-member nitrogen/carbon
    ring at the chromophore position where original GE37468A has a methyl-substituted
    oxazole. The 1995 isolation/structure papers report C59H52N14O12S5 and explicitly
    establish methyloxazole by NMR; their figures and the adopted 2011 Figure 1 agree.
    Current ChEBI199144/ChEMBL4646154 have that O12 constitution, whereas adopted
    and current PubChem101808822 reproduce the erroneous O11 graph. This is not a
    hydration, salt or tautomer difference. The exact identity/biological material
    mapping is broken even though internal validators pass.
  target_ids:
  - antibioticmech:aro-7d06ad4acd
  field_paths:
  - chemical_structure
  - grounding_status
  - xrefs[1]
  - xrefs[2]
  - xrefs[3]
  - source_concepts[0]
  evidence_ids:
  - native
  - owners
  - pubchem
  - chebi
  - chembl
  - comparison
  - structure
  - structure-figure
  - adopted-figure
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO identity, definition and chemical cross-reference owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted PubChem fallback structure
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem fallback retrieval
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Chemical lookup inventory if exact ChEBI mapping is adopted
  rule_id: review-yaml-record:Workflow:identity
  native_severity: blocker
  normalization_reason: The native rubric makes a wrong molecular constitution a blocker.
    Original primary structure evidence establishes the missing oxygen and different
    ring connectivity; this is stronger than a database disagreement alone.
- finding_id: F2
  issue_key: ge37468-post-transcription-peptide-maturation-wording
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: The definition misnames peptide maturation as post-transcription modification
  description: The adopted 2011 paper demonstrates extensive post-translational modification
    of a ribosomally synthesized preprotein. Native and ARO wording say post-transcription
    modification, which refers to a different molecular stage. Correct this localized
    phrase without changing the supported producer, ribosomal precursor or gene-cluster
    claim.
  target_ids:
  - antibioticmech:aro-7d06ad4acd
  field_paths:
  - definition
  evidence_ids:
  - native
  - aro
  - adopted
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO identity, definition and chemical cross-reference owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  rule_id: review-checklist:Mode-of-action
  native_severity: minor
  normalization_reason: A localized biochemical wording error is minor here; the independently
    confirmed wrong-constitution defect is classified separately as blocker.
actions:
- action_id: A1
  description: Replace or re-ground the erroneous PubChem fallback using primary-adjudicated
    GE37468A identity.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-7d06ad4acd
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO identity, definition and chemical cross-reference owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted PubChem fallback structure
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem fallback retrieval
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Potential exact ChEBI structure lookup
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Publication-backed exact structure if required
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding/exclusion decision rather than direct structure override
  acceptance_checks:
  - Use original 1995 MS/NMR/Figs 3/6 and adopted 2011 Figure 1 to establish the O12
    methyloxazole constitution. Recompute SMILES/InChI/key/formula/charge/masses coherently.
  - 'Separately adjudicate stereochemistry: the 2011 paper leaves mhP8 unassigned,
    and current ChEBI/ChEMBL differ. Do not blindly copy either graph or equate unassigned
    centres to a racemate.'
  - Reconcile all exact xrefs and minted-versus-ChEBI grounding after the structure
    decision. Do not keep PubChem101808822 as exact if it still encodes O11. Preserve
    source provenance and avoid transferring native measurements to a new identity
    silently.
  - Regenerate through maintained owners, run chemical/xref, schema/strict, reference/history,
    reproduction and QC checks, and inspect the exact regenerated record.
  generator: scripts/seed_from_sources.py
- action_id: A2
  description: Correct the ARO-derived definition to post-translational modification.
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:aro-7d06ad4acd
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO identity, definition and chemical cross-reference owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  acceptance_checks:
  - Change the maintained source handling or upstream adopted assertion, preserve
    PMID21788474 and regenerate reproducibly.
  - Verify the definition still identifies Streptomyces ATCC 55365 and ribosomally
    synthesized precursor maturation; run focused and corpus gates.
  generator: scripts/seed_from_sources.py
- action_id: A3
  description: 'Optional later curation: record natural-material activity, producer
    and EF-Tu mechanism with bounded assays.'
  finding_ids: []
  target_ids:
  - antibioticmech:aro-7d06ad4acd
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/ge37468.yaml
    role: Future curator-owned activity_spectrum, molecular_targets, producer and
      discussion annotations
  acceptance_checks:
  - Resolve the identity blocker before attaching1995/2011 measurements. Preserve
    O12 material, strain, medium, time, units and wild-type versus analog boundaries.
  - Do not call the 1997 EF-Tu decoy screen a quantitative binding assay, label GetJ
    an antimicrobial target, or turn mouse ED50 into clinical status.
  - Use primary claim-level citations and the validated writer/history process only
    in separately authorized curation.
limitations:
- Required shared full-corpus checks are incorporated separately by the root reviewer
  before finalization; the actual focused gates are recorded here.
- The 2011 main text and actual structure figure were read, but SI retrieval failed
  (publisher 403; PMC HTML challenge). Main-text0.047 µg/mL activity is retained with
  serial-dilution/HPLC-purified material scope; uninspected SI media, inoculum and
  endpoint details are not invented.
- Absolute stereochemistry is not fully resolved by this review. The 2011 source explicitly
  states mhP8 had not been assigned; current authority stereo variants differ and
  require separate primary adjudication after the constitution correction.
- The 1995/2011 antibacterial results establish the natural O12 compound. No inspected
  experiment proves antibacterial activity of the stored O11 constitutional variant.
  The review does not claim that variant is necessarily inactive.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native record, source inventory, curation history, progress file or immutable
  review was modified. The scratch draft is handed off for root audit and ordered
  persistence.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
tags:
- record-review
- queue-492
- read-only
```
