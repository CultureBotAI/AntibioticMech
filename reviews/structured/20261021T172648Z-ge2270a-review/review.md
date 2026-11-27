# GE2270A: stereochemical xref and enterococcal resistance evidence require curation

- Review: 20261021T172648Z-ge2270a-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T17:15:08Z
- Finished UTC: 2026-10-21T17:26:48Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native graph is internally coherent and agrees with current ChEBI/PubChem, but the exact ChEMBL xref assigns six stereocentres absent from the native graph. The imported E. faecium mutant claim is not supported by its adopted primary paper, which tests other elfamycins and an E. hirae mutant. Original GE2270A isolation and EF-Tu studies support antibacterial identity and mechanism with material, organism and access boundaries.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 491; original thirteen input hashes preserved within twenty-nine captured inputs, with actual source owners and local review context appended before detailed assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:29584 | data/antibiotics/antibacterial/ge2270a.yaml | generated | GE2270A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:29584 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:29584 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:29584 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:29584 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:29584 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:29584 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:29584 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:29584 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:29584 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:29584 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:29584 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:29584 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact graph and natural material

identity: unknown. Targets: CHEBI:29584.

Native connectivity, formula, charge and masses are coherent and agree with ChEBI/PubChem. The six-centre-unassigned graph does not record even the original proline/serine assignment; complete natural stereochemistry remains a bounded curation question. No racemate or specific wrong enantiomer is inferred.

### Exact ChEMBL equivalence versus parent class

grounding: concern. Targets: CHEBI:29584.

ChEMBL has six defined centres absent from the native exact graph, violating exact xref semantics. ARO elfamycin is a broader functional class and the molecule/target terms resolve.

### Antibacterial eligibility and assay boundaries

evidence: supported. Targets: CHEBI:29584.

Original purified GE2270A isolation and compound-specific antibacterial experiments support the filing class. Assays, strains, congener boundaries and primary numerical units are retained. No native MIC requires correction.

### EF-Tu binding and protein synthesis inhibition

evidence: supported. Targets: CHEBI:29584.

Native target is honestly database-tier. Original crystallographic abstracts establish direct EF-Tu binding in E. coli and T. thermophilus complexes; original cell-free and intact-cell work supports protein-synthesis inhibition. Missing optional mode/graph is not a schema error.

### Organism, inhibitor and mutant specificity

evidence: concern. Targets: CHEBI:29584.

The E. faecium imported mutant assertion lacks support in its only linked primary paper. P. rosea intrinsic EF-Tu resistance is supported at whole-protein level, with untested candidate substitutions and an abstract-only access boundary. Neither claim can be promoted to a specific proven allele.

### Producer and ribosomal biosynthesis

evidence: supported. Targets: CHEBI:29584.

P. rosea production and ribosomally encoded post-translational maturation are supported by original isolation and subsequent cluster work. The conflicting source strain numbers remain explicit; native asserts no strain.

### Full native claims and all five adopted leads

completeness: unknown. Targets: CHEBI:29584.

All five adopted references and the resistance-term leads were inspected at stated depths. No clinical product, activity collection, graph or dataset is asserted. Optional mechanism/activity enrichment should follow exact stereochemical adjudication and retain strain/material boundaries.

### Actual ARO/ChEBI owners and four events

provenance: supported. Targets: CHEBI:29584.

The original thirteen hashes are preserved within twenty-nine captures. Complete native/source rows, actual imports and all four seed/reseed history events were read; no REVIEWED claim is made.

### Focused deterministic gates

schema: supported. Targets: CHEBI:29584.

Chemistry/schema/strict pass; scientific xref and evidence defects remain independent of those gates.

## Findings

### F1: Exact ChEMBL xref assigns stereochemistry absent from the native graph

major / open / confirmed; issue key: ge2270a-chembl-exact-stereo-mismatch.

Native xrefs[1] asserts CHEMBL1766417 as the same structure. Current ChEMBL specifies six centres (JMDULECOHIXMNX-MZHFYNGJSA-N); native, ChEBI29584 and PubChem16129640 leave all six unassigned (JMDULECOHIXMNX-UHFFFAOYSA-N). Stereo stripping demonstrates shared connectivity, not exact stereochemical identity. Natural-material configuration should be adjudicated before any authority replacement; this review does not declare the all-S ChEMBL graph the final natural standard.

### F2: The E. faecium mutant claim is not supported by its primary citation

major / open / confirmed; issue key: ge2270a-efae-mutant-claim-wrong-primary-scope.

The ARO3003438 source points to PMID7989561. Direct inspection of all three original pages shows kirromycin/aurodox/efrotomycin susceptibility testing and selection of E. hirae ATCC 8043 derivative G1679 on kirromycin. It does not establish GE2270A-resistant E. faecium mutants or a causal EF-Tu allele. The resistance evidence contains only the generic database-assertion note and has no evidence_type, confidence, evidence_status or claim-specific limitation. PRIMARY_EVIDENCE_NEEDED occurs only on the separate molecular target. Database provenance is correctly marked, but the unsupported organism/inhibitor/mutant combination needs explicit qualification or source correction; this is not a universal assertion that such mutants cannot exist.

## Recommended Actions And Acceptance Checks

### A1

Reconcile exact ChEMBL equivalence and natural stereochemical ownership through source harmonization.

- Verify all six natural stereocentres using primary configuration/synthesis evidence, retaining the original two-centre assignment and 1994 connectivity revision. Do not copy a database graph merely by name.
- Retain only graph-equivalent exact xrefs for the adjudicated structure; a less-specified chemical entry may be retained only in an appropriate non-equivalence context.
- Re-seed via maintained inputs and run chemical/xref, schema/strict, reference/history, corpus reproduction and QC gates.

### A2

Qualify or correct the imported E. faecium resistance assertion at its maintained evidence owner.

- Record the inspected PMID7989561 drug/taxon/selected-mutant mismatch without inventing a replacement E. faecium allele or transferring E. hirae kirromycin measurements.
- Use the existing CARD evidence-review mechanism to preserve source provenance while marking primary evidence needed, or correct the upstream relation after a valid exact source is found.
- Validate the exact source-row digest/adjudication, regenerate and run native resistance, schema/strict and corpus gates.

### A3

Optional future curator work: add exact-material target/activity evidence and clarify intrinsic producer resistance.

- Preserve E. coli GDP versus T. thermophilus GDPNP complex scope and distinguish structural binding from cell-free functional IC50 or MIC.
- For P. rosea, obtain the full 1996 article before assigning individual causal substitutions; retain intrinsic resistance rather than silently treating it as selected mutants. Resolve the historical producer strain-number discrepancy before strain-specific annotation.
- Use narrow claim-level evidence and the validated writer/history path only in separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owners | data/raw/aro_antibiotics.tsv; data/raw/chebi_antimicrobials.tsv; data/raw/pubchem_structures.tsv; Exact source rows and readiness; extractor, fallback and seeder branches | supports | Actual ARO source, chemical fallback, target/resistance owner tables and qualification configuration were captured and read. All original thirteen input hashes remain intact. Generated source provenance is retained; this review does not promote SEEDED status. |
| search | 491492-local-hits.txt; Ignored-inclusive local search across data/raw, curation, conf, docs and reports, plus initial capture search | context_only | Exact record/label/ARO/ChEBI hits and full maintained-table selections were inspected. Historical reports are discovery context only. No exact curator or grounding-decision row was found in the directly inspected complete maintained tables. Optional omissions are not schema violations. |
| chemistry | 491-chemistry.json; Both native SMILES and InChI independently parsed; formula, charge, exact/average mass, key and source mint | supports | RDKit 2026.03.5 from the existing batch019 interpreter was run with batch050 as cwd. All local chemistry assertions and calculated source mint agree. This checks internal consistency, not identity against original natural material. |
| comparison | 491492-chem-compare.json; Native versus current ChEBI, PubChem and ChEMBL graph/stereo comparison | supports | Independent parsing compares full and stereo-stripped InChIKeys, formula and assigned/unassigned stereocentres. Current external source responses are preserved separately; source name equality was not used as chemical equivalence. |
| gates | 491-focused-results.json; Actual focused chemistry, schema and strict commands executed in batch050 | supports | All three commands exited zero. Schema/strict used the batch050 frozen environment with UV_NO_SYNC=1; chemistry used the existing batch019 RDKit environment against batch050 cwd. |
| parent | https://www.ebi.ac.uk/ols4/ontologies/aro/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FARO_3001219; ARO:3001219 definition and references | supports | Elfamycins are defined by the EF-Tu target, rather than a common backbone. This is a broader functional antibiotic class and is not an exact molecular identity. PMID12370016 and PMID16876786 are mechanistic reviews, not new exact-material activity experiments. |
| access | 491492-fetch1.json through 491492-fetch6.json; Actual HTTP responses, URLs, UTC accesses and SHA-256 digests | context_only | Free official chemical databases and J-STAGE original PDFs were retrieved. Some EPMC fullTextXML routes returned 500; PMC HTML was used where available. Wiley/ACS/RSC publisher routes returned 403. The PNAS SI route returned 403 and its PMC download route returned an HTML browser challenge, not a PDF. Failed requests are retained as access limits, not read full texts. An initial guessed1991J-STAGE URL failed and was replaced by the verified DOI-derived URL. Legacy ChEBI CCD lead GEA returned404; guessed GE2 was not used as evidence. |
| native | data/antibiotics/antibacterial/ge2270a.yaml; Entire record, both resistance claims, EF-Tu target and all four history events | supports | CHEBI:29584 is SEEDED/EXACT, antibacterial, neutral C56H55N15O10S6. Six tetrahedral centres are unassigned. ARO is the adopted concept; the ChEBI lookup supplies its structure. Target evidence is explicitly CARD_ARO and PRIMARY_EVIDENCE_NEEDED. No quantitative activity, clinical product, causal graph or producer collection is asserted. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/29584/; Current CHEBI:29584 default structure and source metadata | supports | Current two-star ChEBI retains the exact native unassigned graph JMDULECOHIXMNX-UHFFFAOYSA-N, formula and charge. The chemical identifier resolves; it does not independently settle the natural stereochemistry. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/16129640/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON; CID16129640 property response | supports | Current PubChem also has the same six-centre-unassigned graph and neutral formula. It matches the asserted exact xref at the stored annotation level. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL1766417.json; CHEMBL1766417 molecule_structures | refutes | ChEMBL specifies all six tetrahedral centres, with key JMDULECOHIXMNX-MZHFYNGJSA-N. Removing stereo gives the native connectivity key. This is a different stereochemical annotation from the native all-unassigned graph; unspecified stereo does not establish a racemate. |
| aro | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3001237; ARO:3001237 definition and five adopted bibliography leads | supports | The live ARO identity and definition reproduce the adopted molecule concept and bibliography. Native definition_source keeps the first reference; all five adopted leads were inspected at the depths below. ARO is provenance, not independent experimental validation. |
| adopted | PMID:10625477; PMID:8899707; PMID:20522549; PMID:20111801; PMID:16734421; All five original abstracts/metadata; 20522549 also full PMC review text | supports | 10625477 is the E. coli EF-Tu-GDP/GE2270A 2.35 Å complex and reports direct binding/domain-II contact plus low aqueous solubility; 16734421 is the separate T. thermophilus EF-Tu-GDPNP/GE2270A 1.6 Å structure. Their abstracts distinguish GE2270A from pulvomycin. 8899707 reports intrinsic P. rosea EF-Tu resistance. 20522549 and 20111801 are biosynthesis reviews and are used only for source scope and primary discovery; they are not new GE2270A phenotype experiments. |
| resistance-terms | ARO:3003361; ARO:3003438; Both current resistance definitions and original-citation links | supports | P. rosea term cites PMID8899707 plus review PMID12370016. E. faecium term cites PMID7989561 alone. Native citations correctly identify these as database assertions, but the cited experiments must still match their organism, antibiotic and variant scope. The P. rosea authority response is separately preserved in 491-aro-3003361.json; both were read. |
| intrinsic | PMID:8899707; Original abstract; Wiley full text inaccessible | context_only | P. rosea has a single tuf gene; recombinant protein expressed as a malE fusion with an N-terminal Gly-Met extension supports poly (U)-directed poly (Phe) synthesis, fails to bind GE2270 and remains active in its presence. The authors call this intrinsic resistance. Conserved-site substitutions are candidate explanations, not experimentally proven individual mutant alleles in the inspected abstract. |
| enterococci | https://pmc.ncbi.nlm.nih.gov/articles/PMC263923/; PMID7989561, all three original scanned pages 2016–2018, Table 1 and methods | refutes | The actual agents are kirromycin, aurodox and efrotomycin. Table 1 gives kirromycin MICs for enterococcal isolates, including 79 E. faecium isolates, not GE2270A MICs. The selected resistant derivative is E. hirae ATCC 8043→G1679, selected on 100 µg/mL kirromycin. Cell-free systems compare kirromycin/efrotomycin inhibition; no E. faecium GE2270A mutant allele is established. GE2270A appears only in prior-literature citations. |
| enterococci-page2016 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/aabd/263923/b9d538b20d4b/jcm00008-0194.png; Original scanned page 2016 | refutes | Actual page image visually inspected; methods, species, agents, Table 1 and references were read directly. No OCR-only inference was used for the drug/taxon mismatch. |
| enterococci-page2017 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/aabd/263923/076aa54dccf0/jcm00008-0195.png; Original scanned page 2017 | refutes | Actual page image visually inspected; methods, species, agents, Table 1 and references were read directly. No OCR-only inference was used for the drug/taxon mismatch. |
| enterococci-page2018 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/aabd/263923/f9b7a14150bc/jcm00008-0196.png; Original scanned page 2018 | refutes | Actual page image visually inspected; methods, species, agents, Table 1 and references were read directly. No OCR-only inference was used for the drug/taxon mismatch. |
| isolation | DOI:10.7164/antibiotics.44.693; Original 1991 full paper; pp 693–695 methods, p697 producer/chemistry, pp 698–700 activity/mechanism | supports | Purified factor A was isolated from P. rosea ATCC 53773; original text also detects GE2270 in ATCC 23866. Neutral formula and sparing water solubility are supported. Broth microdilution/agar methods vary by organism, use 10^4–10^5 CFU and 18–24 h or 48 h. B. subtilis566/1 macromolecular incorporation at 2 µg/mL preferentially blocks protein synthesis; E. coli cell-free poly (Phe) IC50 is 0.34 µg/mL. The rabbit-reticulocyte comparison is bounded by solubility and does not establish universal host safety. |
| structure-original | DOI:10.7164/antibiotics.44.702; Original 1991 structure paper, stereochemistry paragraphs and hydrolysis methods | supports | The paper identifies L-proline and L-serine by chiral GC and assigns their S configuration, while expressly leaving four of six centres unresolved at that time. Its original macrocycle sequence was revised in 1994; its old complete drawing is therefore not accepted unchanged. This is evidence that the natural preparation is not established as an unspecified stereochemical mixture. |
| structure-revision | DOI:10.7164/antibiotics.47.1564; Original 1994 four-page revision; actual Fig4 p1567 viewed | supports | Controlled partial hydrolysis and fragment MS/MS reverse the earlier assigned thiazole amino-acid sequence. Fig4 shows the revised connectivity corresponding to the current GE2270A framework. The authors report hydrolysis racemization of Asn/Val thiazolyl amino acids and defer absolute configuration details; this paper alone does not assign all six centres. |
| biosynthesis | https://pmc.ncbi.nlm.nih.gov/articles/PMC3943966/; Original 2014 XML abstract/introduction and selected pbt/tufR construct and production-method sections | supports | Supports heterologous expression of the P. rosea GE2270 cluster in S. coelicolor M1146 and distinguishes A versus B1 congeners. The paper writes ATCC 53733 whereas the original 1991 isolation writes ATCC 53773; native only asserts P. rosea, so no unsupported strain replacement is proposed. Cluster/pbtR/tufR manipulations concern production and do not identify a selected GE2270A-resistant E. faecium allele. |
| comparative-activity | DOI:10.7164/antibiotics.48.780; 1995 Table 5 actual page783, methods p 781 and Table 6 p 785 | supports | GE2270A is an explicit comparator, separate from GE37468A: S. aureus Smith MIC 0.016 mg/L and E. faecalis ATCC 7080 0.008 mg/L. Table 6 gives S. aureus L165 parental 0.016 versus selected GE2270-resistant derivative&gt;128 µg/mL for GE2270A. These are strain/material-specific results, not evidence for the E. faecium ARO claim or an identified allele. |
| new-congeners | https://pmc.ncbi.nlm.nih.gov/articles/PMC9822014/; Original 2023 XML structural discussion, exact compounds 1–9, Table 3 and activity-method scope | context_only | The isolated and assayed 1–9 are GE2270 congeners, not unchanged GE2270A. GE2270A occurs in molecular-networking/literature comparisons. Their MIC 90/MBC90 values are not transferred to this record. The discussion of synthetic stereochemical confirmation is a lead rather than an independently read total-synthesis result. |
| adapter | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise1k&amp;query=tufA; Structured adapter before open mechanism research; previously inspected dataset catalog | context_only | The e_coli/precise1k query returns gene b3339 tufA and zero iModulon components. Catalog coverage does not include the named P. rosea/E. faecium resistance contexts. This is gene annotation context only, not direct binding, resistance or activity proof. Sandbox DNS failed; the authorized free public retry succeeded. |
| target-term | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3000731; Current EF-Tu term, definition and generic term bibliography | supports | ARO3000731 resolves to elongation factor Tu, required for bacterial peptide elongation. Its term citations PMID364475 and PMID9678602 do not establish GE2270A-specific binding: the former concerns pulvomycin and the latter is a structural review. Native target evidence remains honestly database-tier; original GE2270A crystallographic abstracts supply the compound-specific follow-up. |

## Limits And Additional Notes

- Required shared full-corpus checks are incorporated separately by the root reviewer before finalization; the actual focused gates are recorded here.
- PMID10625477 and PMID16734421 were read as complete original abstracts/metadata; ACS full-text retrieval returned 403. PMID8899707 was abstract-only after Wiley 403. No inaccessible full-paper measurements or mutation methods are asserted.
- PMID20522549 was read as a full review via PMC; PMID20111801 and resistance/class review leads were abstract/metadata-only. Generic target-term PMID364475 concerns pulvomycin and PMID9678602 is a structural review, so neither was treated as exact GE2270A target evidence.
- The 1991 structure paper assigns only two of six centres and the 1994 paper revises connectivity. Complete primary adjudication of the six-centre natural configuration was not completed; ChEMBL exact annotation conflict is established independently.
- Source Planobispora strain labels differ (1991 ATCC 53773, 2014 ATCC 53733); the native species-only producer wording remains supported. The 2023 congener study supplies no directly transferable GE2270A potency.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native record, source inventory, curation history, progress file or immutable review was modified. The scratch draft is handed off for root audit and ordered persistence.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T172648Z-ge2270a-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'GE2270A: stereochemical xref and enterococcal resistance evidence require
  curation'
started_at: '2026-10-21T17:15:08Z'
finished_at: '2026-10-21T17:26:48Z'
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
verdict: needs_curation
scientific_review: true
summary: The native graph is internally coherent and agrees with current ChEBI/PubChem,
  but the exact ChEMBL xref assigns six stereocentres absent from the native graph.
  The imported E. faecium mutant claim is not supported by its adopted primary paper,
  which tests other elfamycins and an E. hirae mutant. Original GE2270A isolation
  and EF-Tu studies support antibacterial identity and mechanism with material, organism
  and access boundaries.
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
  - path: data/antibiotics/antibacterial/ge2270a.yaml
    sha256: 96a0384cdf3c3474a56af128eb22fd2bad2250f530e67035b8644fc51776974f
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
- target_id: CHEBI:29584
  path: data/antibiotics/antibacterial/ge2270a.yaml
  label: GE2270A
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
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Imported resistance assertions
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Imported target assertions
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: CARD resistance evidence adjudication
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: CARD evidence qualification
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: CARD target relation mapping
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 491; original thirteen input hashes preserved within twenty-nine
    captured inputs, with actual source owners and local review context appended before
    detailed assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:29584
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:29584
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    491
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:29584
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/ge2270a.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:29584
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/ge2270a.yaml --out /private/tmp/am-review-session/491-strict.tsv
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
  - CHEBI:29584
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
  - CHEBI:29584
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
  - CHEBI:29584
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
  - CHEBI:29584
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
  - CHEBI:29584
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
  - CHEBI:29584
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
  - CHEBI:29584
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
  - CHEBI:29584
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
  - CHEBI:29584
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
  snapshot_sha256: dd5e62b7c5714ed39f82575e0566c1d57b529afab4125970d227888640cce733
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
  reference: 491-chemistry.json
  locator: Both native SMILES and InChI independently parsed; formula, charge, exact/average
    mass, key and source mint
  accessed_at: '2026-10-21T17:23:25Z'
  support: supports
  summary: RDKit 2026.03.5 from the existing batch019 interpreter was run with batch050
    as cwd. All local chemistry assertions and calculated source mint agree. This
    checks internal consistency, not identity against original natural material.
  snapshot_sha256: e288721e4204f5bbf126fa3fca6eb4397ffc3346bc0d5136ecf02d050143b11d
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
  reference: 491-focused-results.json
  locator: Actual focused chemistry, schema and strict commands executed in batch050
  accessed_at: '2026-10-21T17:23:25Z'
  support: supports
  summary: All three commands exited zero. Schema/strict used the batch050 frozen
    environment with UV_NO_SYNC=1; chemistry used the existing batch019 RDKit environment
    against batch050 cwd.
  snapshot_sha256: 39687c414c67542b2e1f4a51f8c74d5d2dabb26ab2172559015917de3c823f8a
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
  reference: data/antibiotics/antibacterial/ge2270a.yaml
  locator: Entire record, both resistance claims, EF-Tu target and all four history
    events
  accessed_at: '2026-10-21T17:23:25Z'
  support: supports
  summary: CHEBI:29584 is SEEDED/EXACT, antibacterial, neutral C56H55N15O10S6. Six
    tetrahedral centres are unassigned. ARO is the adopted concept; the ChEBI lookup
    supplies its structure. Target evidence is explicitly CARD_ARO and PRIMARY_EVIDENCE_NEEDED.
    No quantitative activity, clinical product, causal graph or producer collection
    is asserted.
  snapshot_sha256: 96a0384cdf3c3474a56af128eb22fd2bad2250f530e67035b8644fc51776974f
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/29584/
  locator: Current CHEBI:29584 default structure and source metadata
  accessed_at: '2026-10-21T17:17:27.869213Z'
  support: supports
  summary: Current two-star ChEBI retains the exact native unassigned graph JMDULECOHIXMNX-UHFFFAOYSA-N,
    formula and charge. The chemical identifier resolves; it does not independently
    settle the natural stereochemistry.
  snapshot_sha256: 32e997b0a4f392157bddca94427e3aec9333fd6c5743eb3d9b0a4c51da1ad2bb
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/16129640/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON
  locator: CID16129640 property response
  accessed_at: '2026-10-21T17:17:27.870259Z'
  support: supports
  summary: Current PubChem also has the same six-centre-unassigned graph and neutral
    formula. It matches the asserted exact xref at the stored annotation level.
  snapshot_sha256: f307df9c71796543c03a15df606d9132a29ac2910ce7143dbc5d97aeaaecb916
- evidence_id: chembl
  kind: authority
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL1766417.json
  locator: CHEMBL1766417 molecule_structures
  accessed_at: '2026-10-21T17:17:27.876141Z'
  support: refutes
  summary: ChEMBL specifies all six tetrahedral centres, with key JMDULECOHIXMNX-MZHFYNGJSA-N.
    Removing stereo gives the native connectivity key. This is a different stereochemical
    annotation from the native all-unassigned graph; unspecified stereo does not establish
    a racemate.
  snapshot_sha256: 672ba41b652b8fae62a3ef50532a72527be19436b12ff9fff48cf764fdd47a63
- evidence_id: aro
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3001237
  locator: ARO:3001237 definition and five adopted bibliography leads
  accessed_at: '2026-10-21T17:17:27.876675Z'
  support: supports
  summary: The live ARO identity and definition reproduce the adopted molecule concept
    and bibliography. Native definition_source keeps the first reference; all five
    adopted leads were inspected at the depths below. ARO is provenance, not independent
    experimental validation.
  snapshot_sha256: 70980b1d8d1c77cc2b3ebc87923ee835f7759f996c04cbdfdeba7ead254addc9
- evidence_id: adopted
  kind: primary_source
  reference: PMID:10625477; PMID:8899707; PMID:20522549; PMID:20111801; PMID:16734421
  locator: All five original abstracts/metadata; 20522549 also full PMC review text
  accessed_at: '2026-10-21T17:17:28.801306Z'
  support: supports
  summary: 10625477 is the E. coli EF-Tu-GDP/GE2270A 2.35 Å complex and reports direct
    binding/domain-II contact plus low aqueous solubility; 16734421 is the separate
    T. thermophilus EF-Tu-GDPNP/GE2270A 1.6 Å structure. Their abstracts distinguish
    GE2270A from pulvomycin. 8899707 reports intrinsic P. rosea EF-Tu resistance.
    20522549 and 20111801 are biosynthesis reviews and are used only for source scope
    and primary discovery; they are not new GE2270A phenotype experiments.
  snapshot_sha256: c02b021234c3e09b39d252d54d8fada2e2a3b155845dced093ebf542cbb5cee1
- evidence_id: resistance-terms
  kind: database
  reference: ARO:3003361; ARO:3003438
  locator: Both current resistance definitions and original-citation links
  accessed_at: '2026-10-21T17:17:30.209957Z'
  support: supports
  summary: P. rosea term cites PMID8899707 plus review PMID12370016. E. faecium term
    cites PMID7989561 alone. Native citations correctly identify these as database
    assertions, but the cited experiments must still match their organism, antibiotic
    and variant scope. The P. rosea authority response is separately preserved in
    491-aro-3003361.json; both were read.
  snapshot_sha256: a81289b9c5a1986fb10192c149ef765f4afab951e682ead5ccde59c313d08684
- evidence_id: intrinsic
  kind: primary_source
  reference: PMID:8899707
  locator: Original abstract; Wiley full text inaccessible
  accessed_at: '2026-10-21T17:17:28.801306Z'
  support: context_only
  summary: P. rosea has a single tuf gene; recombinant protein expressed as a malE
    fusion with an N-terminal Gly-Met extension supports poly (U)-directed poly (Phe)
    synthesis, fails to bind GE2270 and remains active in its presence. The authors
    call this intrinsic resistance. Conserved-site substitutions are candidate explanations,
    not experimentally proven individual mutant alleles in the inspected abstract.
  snapshot_sha256: c02b021234c3e09b39d252d54d8fada2e2a3b155845dced093ebf542cbb5cee1
- evidence_id: enterococci
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC263923/
  locator: PMID7989561, all three original scanned pages 2016–2018, Table 1 and methods
  accessed_at: '2026-10-21T17:18:20.208181Z'
  support: refutes
  summary: The actual agents are kirromycin, aurodox and efrotomycin. Table 1 gives
    kirromycin MICs for enterococcal isolates, including 79 E. faecium isolates, not
    GE2270A MICs. The selected resistant derivative is E. hirae ATCC 8043→G1679, selected
    on 100 µg/mL kirromycin. Cell-free systems compare kirromycin/efrotomycin inhibition;
    no E. faecium GE2270A mutant allele is established. GE2270A appears only in prior-literature
    citations.
  snapshot_sha256: 906d4ddfb8abef816adc9d293db2f491e9e40247b38860a44add2036d5fc869f
- evidence_id: enterococci-page2016
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/aabd/263923/b9d538b20d4b/jcm00008-0194.png
  locator: Original scanned page 2016
  accessed_at: '2026-10-21T17:18:51.658626Z'
  support: refutes
  summary: Actual page image visually inspected; methods, species, agents, Table 1
    and references were read directly. No OCR-only inference was used for the drug/taxon
    mismatch.
  snapshot_sha256: bfb219f6cdd6f3dcbd3bf87ac030e8af3c039d612c50fd55d532749d9252cecb
- evidence_id: enterococci-page2017
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/aabd/263923/076aa54dccf0/jcm00008-0195.png
  locator: Original scanned page 2017
  accessed_at: '2026-10-21T17:18:51.658746Z'
  support: refutes
  summary: Actual page image visually inspected; methods, species, agents, Table 1
    and references were read directly. No OCR-only inference was used for the drug/taxon
    mismatch.
  snapshot_sha256: 0f549c3479253c9d70cc3cbf45cf88ac5f420992d91f5250b6bf65e825535b33
- evidence_id: enterococci-page2018
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/aabd/263923/f9b7a14150bc/jcm00008-0196.png
  locator: Original scanned page 2018
  accessed_at: '2026-10-21T17:18:51.662564Z'
  support: refutes
  summary: Actual page image visually inspected; methods, species, agents, Table 1
    and references were read directly. No OCR-only inference was used for the drug/taxon
    mismatch.
  snapshot_sha256: d2c1ae3faaca0771ba1a9125457cb6273d9724d89ad7670d7ca64dec37ce1bb6
- evidence_id: isolation
  kind: primary_source
  reference: DOI:10.7164/antibiotics.44.693
  locator: Original 1991 full paper; pp 693–695 methods, p697 producer/chemistry,
    pp 698–700 activity/mechanism
  accessed_at: '2026-10-21T17:18:20.203087Z'
  support: supports
  summary: Purified factor A was isolated from P. rosea ATCC 53773; original text
    also detects GE2270 in ATCC 23866. Neutral formula and sparing water solubility
    are supported. Broth microdilution/agar methods vary by organism, use 10^4–10^5
    CFU and 18–24 h or 48 h. B. subtilis566/1 macromolecular incorporation at 2 µg/mL
    preferentially blocks protein synthesis; E. coli cell-free poly (Phe) IC50 is
    0.34 µg/mL. The rabbit-reticulocyte comparison is bounded by solubility and does
    not establish universal host safety.
  snapshot_sha256: 13b910824e287a8ba2f25697abb9c418f0b937860d08ec2d9b412e94c8dbe330
- evidence_id: structure-original
  kind: primary_source
  reference: DOI:10.7164/antibiotics.44.702
  locator: Original 1991 structure paper, stereochemistry paragraphs and hydrolysis
    methods
  accessed_at: '2026-10-21T17:18:20.202852Z'
  support: supports
  summary: The paper identifies L-proline and L-serine by chiral GC and assigns their
    S configuration, while expressly leaving four of six centres unresolved at that
    time. Its original macrocycle sequence was revised in 1994; its old complete drawing
    is therefore not accepted unchanged. This is evidence that the natural preparation
    is not established as an unspecified stereochemical mixture.
  snapshot_sha256: 1809d39dde0e93fb144fa0005aab059095d7e017ae455afd024c2a2ffba01668
- evidence_id: structure-revision
  kind: primary_source
  reference: DOI:10.7164/antibiotics.47.1564
  locator: Original 1994 four-page revision; actual Fig4 p1567 viewed
  accessed_at: '2026-10-21T17:18:51.658159Z'
  support: supports
  summary: Controlled partial hydrolysis and fragment MS/MS reverse the earlier assigned
    thiazole amino-acid sequence. Fig4 shows the revised connectivity corresponding
    to the current GE2270A framework. The authors report hydrolysis racemization of
    Asn/Val thiazolyl amino acids and defer absolute configuration details; this paper
    alone does not assign all six centres.
  snapshot_sha256: bd4722ce17a7f7c8abea5394e85649327f377195f4ebab3783cf8fa7dffe14fd
- evidence_id: biosynthesis
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3943966/
  locator: Original 2014 XML abstract/introduction and selected pbt/tufR construct
    and production-method sections
  accessed_at: '2026-10-21T17:18:08.637804Z'
  support: supports
  summary: Supports heterologous expression of the P. rosea GE2270 cluster in S. coelicolor
    M1146 and distinguishes A versus B1 congeners. The paper writes ATCC 53733 whereas
    the original 1991 isolation writes ATCC 53773; native only asserts P. rosea, so
    no unsupported strain replacement is proposed. Cluster/pbtR/tufR manipulations
    concern production and do not identify a selected GE2270A-resistant E. faecium
    allele.
  snapshot_sha256: 45ed99c6e7749793ba3178fa6e4d0d762726b0d1fef72a71cd9fc174520154e5
- evidence_id: comparative-activity
  kind: primary_source
  reference: DOI:10.7164/antibiotics.48.780
  locator: 1995 Table 5 actual page783, methods p 781 and Table 6 p 785
  accessed_at: '2026-10-21T17:18:08.637337Z'
  support: supports
  summary: 'GE2270A is an explicit comparator, separate from GE37468A: S. aureus Smith
    MIC 0.016 mg/L and E. faecalis ATCC 7080 0.008 mg/L. Table 6 gives S. aureus L165
    parental 0.016 versus selected GE2270-resistant derivative>128 µg/mL for GE2270A.
    These are strain/material-specific results, not evidence for the E. faecium ARO
    claim or an identified allele.'
  snapshot_sha256: 3d86c61cc6227e96a8747ee50bf523dc44639954118576046c6314082e13bd06
- evidence_id: new-congeners
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC9822014/
  locator: Original 2023 XML structural discussion, exact compounds 1–9, Table 3 and
    activity-method scope
  accessed_at: '2026-10-21T17:17:53.982859Z'
  support: context_only
  summary: The isolated and assayed 1–9 are GE2270 congeners, not unchanged GE2270A.
    GE2270A occurs in molecular-networking/literature comparisons. Their MIC 90/MBC90
    values are not transferred to this record. The discussion of synthetic stereochemical
    confirmation is a lead rather than an independently read total-synthesis result.
  snapshot_sha256: 3ddef1bc5be72d6627cc7f598d17bee2ab9eb80e38a07192ba44987f424c6435
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=tufA
  locator: Structured adapter before open mechanism research; previously inspected
    dataset catalog
  accessed_at: '2026-10-21T17:23:25Z'
  support: context_only
  summary: The e_coli/precise1k query returns gene b3339 tufA and zero iModulon components.
    Catalog coverage does not include the named P. rosea/E. faecium resistance contexts.
    This is gene annotation context only, not direct binding, resistance or activity
    proof. Sandbox DNS failed; the authorized free public retry succeeded.
  snapshot_sha256: 9380340a2e0f964d45a17286996f765b36339f7a2288faf5096be4913c8d694a
- evidence_id: target-term
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FARO_3000731
  locator: Current EF-Tu term, definition and generic term bibliography
  accessed_at: '2026-10-21T17:17:29.901560Z'
  support: supports
  summary: 'ARO3000731 resolves to elongation factor Tu, required for bacterial peptide
    elongation. Its term citations PMID364475 and PMID9678602 do not establish GE2270A-specific
    binding: the former concerns pulvomycin and the latter is a structural review.
    Native target evidence remains honestly database-tier; original GE2270A crystallographic
    abstracts supply the compound-specific follow-up.'
  snapshot_sha256: fba024a2dea1bba4b8690be4ce5e89e4a8d0473d44d13cdcc31a2d7d233e7cca
assessments:
- assessment_id: identity
  area: identity
  topic: Exact graph and natural material
  outcome: unknown
  summary: Native connectivity, formula, charge and masses are coherent and agree
    with ChEBI/PubChem. The six-centre-unassigned graph does not record even the original
    proline/serine assignment; complete natural stereochemistry remains a bounded
    curation question. No racemate or specific wrong enantiomer is inferred.
  target_ids:
  - CHEBI:29584
  evidence_ids:
  - native
  - chemistry
  - chebi
  - pubchem
  - structure-original
  - structure-revision
- assessment_id: grounding
  area: grounding
  topic: Exact ChEMBL equivalence versus parent class
  outcome: concern
  summary: ChEMBL has six defined centres absent from the native exact graph, violating
    exact xref semantics. ARO elfamycin is a broader functional class and the molecule/target
    terms resolve.
  target_ids:
  - CHEBI:29584
  evidence_ids:
  - chembl
  - comparison
  - aro
  - parent
- assessment_id: activity
  area: evidence
  topic: Antibacterial eligibility and assay boundaries
  outcome: supported
  summary: Original purified GE2270A isolation and compound-specific antibacterial
    experiments support the filing class. Assays, strains, congener boundaries and
    primary numerical units are retained. No native MIC requires correction.
  target_ids:
  - CHEBI:29584
  evidence_ids:
  - isolation
  - comparative-activity
  - new-congeners
- assessment_id: mechanism
  area: evidence
  topic: EF-Tu binding and protein synthesis inhibition
  outcome: supported
  summary: Native target is honestly database-tier. Original crystallographic abstracts
    establish direct EF-Tu binding in E. coli and T. thermophilus complexes; original
    cell-free and intact-cell work supports protein-synthesis inhibition. Missing
    optional mode/graph is not a schema error.
  target_ids:
  - CHEBI:29584
  evidence_ids:
  - adopted
  - isolation
  - adapter
  - target-term
- assessment_id: resistance
  area: evidence
  topic: Organism, inhibitor and mutant specificity
  outcome: concern
  summary: The E. faecium imported mutant assertion lacks support in its only linked
    primary paper. P. rosea intrinsic EF-Tu resistance is supported at whole-protein
    level, with untested candidate substitutions and an abstract-only access boundary.
    Neither claim can be promoted to a specific proven allele.
  target_ids:
  - CHEBI:29584
  evidence_ids:
  - resistance-terms
  - enterococci
  - intrinsic
- assessment_id: producer
  area: evidence
  topic: Producer and ribosomal biosynthesis
  outcome: supported
  summary: P. rosea production and ribosomally encoded post-translational maturation
    are supported by original isolation and subsequent cluster work. The conflicting
    source strain numbers remain explicit; native asserts no strain.
  target_ids:
  - CHEBI:29584
  evidence_ids:
  - isolation
  - biosynthesis
  - adopted
- assessment_id: completeness
  area: completeness
  topic: Full native claims and all five adopted leads
  outcome: unknown
  summary: All five adopted references and the resistance-term leads were inspected
    at stated depths. No clinical product, activity collection, graph or dataset is
    asserted. Optional mechanism/activity enrichment should follow exact stereochemical
    adjudication and retain strain/material boundaries.
  target_ids:
  - CHEBI:29584
  evidence_ids:
  - native
  - adopted
  - access
  - new-congeners
- assessment_id: provenance
  area: provenance
  topic: Actual ARO/ChEBI owners and four events
  outcome: supported
  summary: The original thirteen hashes are preserved within twenty-nine captures.
    Complete native/source rows, actual imports and all four seed/reseed history events
    were read; no REVIEWED claim is made.
  target_ids:
  - CHEBI:29584
  evidence_ids:
  - owners
  - native
  - search
- assessment_id: validation
  area: schema
  topic: Focused deterministic gates
  outcome: supported
  summary: Chemistry/schema/strict pass; scientific xref and evidence defects remain
    independent of those gates.
  target_ids:
  - CHEBI:29584
  evidence_ids:
  - gates
  - chemistry
  - comparison
findings:
- finding_id: F1
  issue_key: ge2270a-chembl-exact-stereo-mismatch
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Exact ChEMBL xref assigns stereochemistry absent from the native graph
  description: Native xrefs[1] asserts CHEMBL1766417 as the same structure. Current
    ChEMBL specifies six centres (JMDULECOHIXMNX-MZHFYNGJSA-N); native, ChEBI29584
    and PubChem16129640 leave all six unassigned (JMDULECOHIXMNX-UHFFFAOYSA-N). Stereo
    stripping demonstrates shared connectivity, not exact stereochemical identity.
    Natural-material configuration should be adjudicated before any authority replacement;
    this review does not declare the all-S ChEMBL graph the final natural standard.
  target_ids:
  - CHEBI:29584
  field_paths:
  - xrefs[1]
  evidence_ids:
  - native
  - owners
  - chembl
  - comparison
  - chebi
  - pubchem
  - structure-original
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
  rule_id: review-checklist:Equivalence
  native_severity: major
  normalization_reason: An exact-equivalence xref to a differently stereospecified
    molecular graph is major. The field is xrefs, not broad drug_xrefs; unassigned
    stereo is not a racemate.
- finding_id: F2
  issue_key: ge2270a-efae-mutant-claim-wrong-primary-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The E. faecium mutant claim is not supported by its primary citation
  description: The ARO3003438 source points to PMID7989561. Direct inspection of all
    three original pages shows kirromycin/aurodox/efrotomycin susceptibility testing
    and selection of E. hirae ATCC 8043 derivative G1679 on kirromycin. It does not
    establish GE2270A-resistant E. faecium mutants or a causal EF-Tu allele. The resistance
    evidence contains only the generic database-assertion note and has no evidence_type,
    confidence, evidence_status or claim-specific limitation. PRIMARY_EVIDENCE_NEEDED
    occurs only on the separate molecular target. Database provenance is correctly
    marked, but the unsupported organism/inhibitor/mutant combination needs explicit
    qualification or source correction; this is not a universal assertion that such
    mutants cannot exist.
  target_ids:
  - CHEBI:29584
  field_paths:
  - resistance_mechanisms[1]
  evidence_ids:
  - resistance-terms
  - enterococci
  - enterococci-page2016
  - enterococci-page2017
  - enterococci-page2018
  - owners
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Imported ARO resistance assertion
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Claim-specific primary-source qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: CARD evidence adjudication transform
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated resistance claim owner
  rule_id: review-checklist:Resistance
  native_severity: major
  normalization_reason: A compound/taxon/variant-specific resistance assertion supported
    by a mismatched primary source is major scope inflation, even when database provenance
    is retained.
actions:
- action_id: A1
  description: Reconcile exact ChEMBL equivalence and natural stereochemical ownership
    through source harmonization.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:29584
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
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted structure lookup
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Publication-backed exact identity if required
  acceptance_checks:
  - Verify all six natural stereocentres using primary configuration/synthesis evidence,
    retaining the original two-centre assignment and 1994 connectivity revision. Do
    not copy a database graph merely by name.
  - Retain only graph-equivalent exact xrefs for the adjudicated structure; a less-specified
    chemical entry may be retained only in an appropriate non-equivalence context.
  - Re-seed via maintained inputs and run chemical/xref, schema/strict, reference/history,
    corpus reproduction and QC gates.
  generator: scripts/seed_from_sources.py
- action_id: A2
  description: Qualify or correct the imported E. faecium resistance assertion at
    its maintained evidence owner.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:29584
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Imported ARO resistance assertion
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Claim-specific primary-source qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: CARD evidence adjudication transform
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated resistance claim owner
  acceptance_checks:
  - Record the inspected PMID7989561 drug/taxon/selected-mutant mismatch without inventing
    a replacement E. faecium allele or transferring E. hirae kirromycin measurements.
  - Use the existing CARD evidence-review mechanism to preserve source provenance
    while marking primary evidence needed, or correct the upstream relation after
    a valid exact source is found.
  - Validate the exact source-row digest/adjudication, regenerate and run native resistance,
    schema/strict and corpus gates.
  generator: scripts/seed_from_sources.py
- action_id: A3
  description: 'Optional future curator work: add exact-material target/activity evidence
    and clarify intrinsic producer resistance.'
  finding_ids: []
  target_ids:
  - CHEBI:29584
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/ge2270a.yaml
    role: Future curator-owned primary target, activity_spectrum, producer and discussion
      annotations
  acceptance_checks:
  - Preserve E. coli GDP versus T. thermophilus GDPNP complex scope and distinguish
    structural binding from cell-free functional IC50 or MIC.
  - For P. rosea, obtain the full 1996 article before assigning individual causal
    substitutions; retain intrinsic resistance rather than silently treating it as
    selected mutants. Resolve the historical producer strain-number discrepancy before
    strain-specific annotation.
  - Use narrow claim-level evidence and the validated writer/history path only in
    separately authorized curation.
limitations:
- Required shared full-corpus checks are incorporated separately by the root reviewer
  before finalization; the actual focused gates are recorded here.
- PMID10625477 and PMID16734421 were read as complete original abstracts/metadata;
  ACS full-text retrieval returned 403. PMID8899707 was abstract-only after Wiley
  403. No inaccessible full-paper measurements or mutation methods are asserted.
- PMID20522549 was read as a full review via PMC; PMID20111801 and resistance/class
  review leads were abstract/metadata-only. Generic target-term PMID364475 concerns
  pulvomycin and PMID9678602 is a structural review, so neither was treated as exact
  GE2270A target evidence.
- The 1991 structure paper assigns only two of six centres and the 1994 paper revises
  connectivity. Complete primary adjudication of the six-centre natural configuration
  was not completed; ChEMBL exact annotation conflict is established independently.
- Source Planobispora strain labels differ (1991 ATCC 53773, 2014 ATCC 53733); the
  native species-only producer wording remains supported. The 2023 congener study
  supplies no directly transferable GE2270A potency.
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
- queue-491
- read-only
```
