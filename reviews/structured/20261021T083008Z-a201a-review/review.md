# Review of A201A

- Review: 20261021T083008Z-a201a-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:18:55Z
- Finished UTC: 2026-10-21T08:30:08Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

A201A identity and antibacterial mechanism are supported, but its PubChem-derived encodings omit all 12 tetrahedral configurations. Current external representations conflict, so the repair requires primary structure reconciliation. A minor finding recommends precise tRNA-accommodation wording and claim-level primary evidence; imported resistance assertions retain their database qualification.

## Scope And Provenance

Whole exact A201A record; ARO/PubChem source ownership; all xrefs, class and three resistance determinants; every adopted PMID lead; primary structural, ribosome and resistance experiments.

Selection: Path-ordered unreviewed queue index 073; exactly one record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-e83eaf8a8a | data/antibiotics/antibacterial/a201a.yaml | generated | A201A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented per-record LinkML validation | passed | True | antibioticmech:aro-e83eaf8a8a | Exit 0; No issues found. |
| Documented closed-schema validation | passed | True | antibioticmech:aro-e83eaf8a8a | Exit 0; one record and zero ERROR rows. |
| Native structure and external stereochemistry comparison | failed | False | antibioticmech:aro-e83eaf8a8a | Exit 1: internal formula/key/masses and deterministic mint agree, but all 12 native tetrahedral centres are unspecified. Source candidates conflict and are not approved replacements. |
| Exact ARO term and resistance-edge assertions | passed | False | antibioticmech:aro-e83eaf8a8a | Exit 0: six terms including direct/broader classes and all three exact edges are consistent; current CARD page corroborates labels. |
| Structured-source catalog before web research | passed | False | antibioticmech:aro-e83eaf8a8a | Exit 0; inspected covered organism/dataset keys. |
| Structured-source vmlR lookup before web research | passed | False | antibioticmech:aro-e83eaf8a8a | Exit 0; one gene key and no iModulon hit. No module summary was warranted. |
| Authoritative full QC | failed | True | antibioticmech:aro-e83eaf8a8a | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-e83eaf8a8a | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-e83eaf8a8a | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-e83eaf8a8a | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-e83eaf8a8a | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-e83eaf8a8a | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-e83eaf8a8a | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-e83eaf8a8a | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-e83eaf8a8a | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact natural-product stereochemistry

identity: concern. Targets: antibioticmech:aro-e83eaf8a8a.

The intended A201A is clear, but native encodings denote its stereo-unspecified structure and omit all 12 tetrahedral configurations.

### Class, mint and source xrefs

grounding: supported. Targets: antibioticmech:aro-e83eaf8a8a.

Valid broader nucleoside class and deterministic ARO mint. Current ChEBI is a 2_STAR comparison term; changing native grounding is not implied.

### Cross-authority structure conflict

consistency: concern. Targets: antibioticmech:aro-e83eaf8a8a.

Native CID, partial-stereo ChEMBL/CARD and fully assigned ChEBI/PubChem candidates cannot be treated as identical stereochemical encodings.

### Initial binding versus full accommodation

scope: concern. Targets: antibioticmech:aro-e83eaf8a8a.

Broad translation/PTC mechanism is supported, but the final definition sentence needs the CCA-end/full-accommodation qualification.

### Three qualified database assertions

evidence: supported. Targets: antibioticmech:aro-e83eaf8a8a.

All exact ARO assertions reproduce; 2023 primary data independently support their resistance potential with host-specific limits.

### Available primary annotation

completeness: concern. Targets: antibioticmech:aro-e83eaf8a8a.

Concrete primary mechanism, susceptibility and resistance evidence can be annotated; optional emptiness alone is not the finding.

### Producer, clinical, causal graph and datasets

representation: not_applicable. Targets: antibioticmech:aro-e83eaf8a8a.

No such native assertions require correction; source-producer history and candidate graphs need separate claim-level curation.

### Generated fields and history

ownership: supported. Targets: antibioticmech:aro-e83eaf8a8a.

Actual ARO/PubChem owners captured before judgment; all 19 input hashes remain unchanged and seed/reseed history is coherent.

### Focused native gates

schema: supported. Targets: antibioticmech:aro-e83eaf8a8a.

Documented per-record validators pass; supplemental chemistry finds a semantic defect they do not cover.

## Findings

### F1: A201A native structure leaves all 12 tetrahedral centres unspecified

major / open / confirmed; issue key: aro-3007639-a201a-tetrahedral-stereochemistry-underidentified.

The source-derived structure agrees internally but cannot represent the specific natural-product stereochemistry established by primary chemistry. Candidate authority encodings also disagree; repairing only the displayed SMILES or blindly adopting a new xref would leave an inconsistent record.

### F2: Clarify tRNA accommodation and annotate available claim-level primary evidence

minor / open / confirmed; issue key: aro-3007639-a201a-primary-mechanism-qualification.

The PTC mechanism is sound but the unqualified A-site-binding sentence obscures the experimentally preserved initial binding step. Exact primary mechanism and resistance data support a bounded annotation with assay and surrogate-host scope.

## Recommended Actions And Acceptance Checks

### A1

Reconcile primary A201A stereochemistry and all source encodings, then repair the maintained structure selection and regenerate.

- Atom-map the three sugar stereochemistries and both alkene geometries against primary Figure1 and supporting chemical evidence. Resolve the assigned central-sugar conflict between ChEMBL/CARD and ChEBI/PubChem; do not approve any candidate solely from database naming.
- Represent the experimentally supported specific stereoisomer with mutually consistent isomeric SMILES, standard InChI/key and exact xref scope. Preserve amide versus normalized InChI tautomer distinctions.
- Correct the maintained ARO-to-structure selection before reseeding through scripts/seed_from_sources.py; retain provenance and avoid a generated-YAML-only patch.
- Recheck all centres, alkene geometry, source xrefs, deterministic mint, schema/strict and required corpus gates; review regeneration diff before scientific sign-off.

### A2

Curate the supported primary mechanism and resistance claims with precise scope and reproducible definition wording.

- State that A201A binds the PTC and obstructs full CCA-end accommodation and peptide-bond formation while initial ternary-complex binding can occur. Retain PMID26028538 at that claim.
- Keep 2 µM translation IC50 separate from whole-cell MIC, the 20 µM smFRET exposure, and HygA-specific values.
- Use PMID36951104 for A201A-specific VmlR/VmlR2/CplR resistance; preserve B.subtilis surrogate hosts and distinguish native-species gene origin from assay organism. Preserve inequalities and ATPase-mutant/tag controls.
- Keep the Table1 16–20 h versus generic Methods 24 h discrepancy visible if extracting MIC conditions. Do not infer clinical breakpoints, direct A201A displacement from a drug-free protection-factor structure, or an efflux mechanism for Ard1.
- Use claim-level PRIMARY_LITERATURE evidence only after exact mappings and reviewed protein examples are resolved; run all required native gates and add validated curation history before REVIEWED status.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/a201a.yaml; Entire generated record | supports | Read definition and PMID, broad nucleoside class, full chemistry, four xrefs, exact ARO mint, all three target-protection assertions and all three seed/reseed events. No separate activity, target, producer, clinical or causal-graph assertions are present. |
| inventory | data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; data/raw/aro_resistance_edges.tsv; Exact ARO:3007639 rows and maintained owner transforms | supports | Native definition/class and qualified resistance edges reproduce from ARO; the PubChem CID 6441582 row supplies the stereochemically incomplete structure. The direct ARO parent is aminonucleoside antibiotic ARO:3000080, whose nucleoside ancestor ARO:3000034 is the valid broader native class. Mint remains consistent. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/6441582; 073-pubchem.json | partial | Current CID 6441582 reproduces native HELPZWNRUYNCJQ-QWJSOBSRSA-N, C37H50N6O14 and absent tetrahedral stereochemistry. Reproducing the adopted source does not establish exact natural-product stereochemistry. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:222171; 073-chebi.html; 073-ols.json | partial | Non-obsolete 2_STAR A201A term has fully assigned InChI HELPZWNRUYNCJQ-KLBOBXLXSA-N. Its SMILES retains 12 tetrahedral assignments but omits both alkene geometries, giving HELPZWNRUYNCJQ-MJPRRRBXSA-N. Neither an automatic grounding change nor blind SMILES replacement is justified. |
| pubchem-full | https://pubchem.ncbi.nlm.nih.gov/compound/145720665; 073-pubchem-full.json | partial | This full-stereo A201A candidate agrees with the ChEBI InChI/key and assigns 12 centres. It is a comparison candidate, not an approved correction, because the ChEMBL/CARD central-sugar stereochemistry differs. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL100042.json; 073-chembl.json | partial | ChEMBL assigns 10 of 12 tetrahedral centres; two ribose centres remain unspecified. Its standard InChI/key HELPZWNRUYNCJQ-LDAKLULBSA-N differs from the fully specified ChEBI/PubChem candidate, including an assigned central-sugar centre. Keep the cross-source conflict explicit. |
| card | https://card.mcmaster.ca/ontology/46414; 073-card.html | partial | Official ARO:3007639 resolves to A201A with the same four native xrefs, definition reference and three determinant labels. Its displayed partial-stereo SMILES follows the ChEMBL candidate; database links are not uniformly exact structural equivalents. |
| structure-primary | PMID:4019309; DOI:10.7164/antibiotics.38.575; 073-primary1985.pdf pp575–580, Fig1 original pixels | supports | Primary chemical/spectroscopic work and a cyclized-derivative X-ray study establish a specific sugar stereochemistry for A201A. Figure1 depicts stereodefined ribose, central furanose and terminal D-rhamnose; compounds A201C/D/E and hydrogenated products are separate. This proves that omitting every tetrahedral assignment is materially incomplete, without endorsing an unreviewed authority candidate. |
| mechanism-primary | PMID:26028538; DOI:10.1016/j.molcel.2015.04.014; 073-primary2015.html, A201A Results/Conclusions/Methods and Fig6 | partial | T. thermophilus 70S crystallography and E. coli biochemical/smFRET experiments support PTC binding and obstruction of full A-tRNA CCA-end accommodation. Initial ternary-complex binding still occurs. A201A translation IC50 is 2 µM in a lysate GFP assay, not a whole-cell MIC. At 20 µM, reversible tRNA-selection dynamics persist about 5 s; the longer HygA delay is separate. Cfr resistance is tested in E. coli SQ110DTC ΔtolC by disc diffusion. The older Ard1 efflux description is superseded by the inspected 2023 ABCF evidence. |
| resistance-primary | PMID:36951104; DOI:10.1093/nar/gkad193; 073-primary2023.xml, Methods, Results, Table1 and footnote | supports | Table1 tests A201A in B. subtilis: 168 WT &gt;256 µg/mL, ΔvmlR 4, complemented vmlR &gt;256, ATPase-deficient vmlR EQ2 2–4; N. vireti vmlR2 expressed in ΔvmlR &gt;256; untagged C. difficile cplR expressed in ΔvmlR 16. Those last two are surrogate-host phenotypes, not native-species MICs. Ard1 expression yields 16 versus 4 for its EQ2 control, supporting a bounded enrichment opportunity. LB, 1 mM IPTG for expressed constructs and Table1 16–20 h at 37°C are explicit; generic Methods instead state 24 h, a source discrepancy to preserve. No clinical breakpoint is inferred. |
| vmlr-primary | PMID:30126986; DOI:10.1073/pnas.1808535115; 073-primary2018.xml | context_only | The VmlR cryo-EM and mutagenesis study supports ribosome-protection context but tests other PTC inhibitors, not A201A. A201A-specific resistance support comes from the 2023 paper, not automatic transfer from this earlier structural study. |
| leads | https://europepmc.org/article/MED/26028538; 073-core.json; all three unique adopted drug/determinant PMID leads | supports | Resolved and read abstracts for 26028538, 30126986 and 36951104, then inspected each full article for relevant claims. Additional primary structure PMID 4019309 was resolved and its PDF inspected. The 2014 total-synthesis abstract is only a lead; the 2017 fullTextXML fetch failed and supplies no findings. |
| chemistry | RDKit structure comparisons; 073-chemistry.py; 073-chemistry.json | supports | Native SMILES/InChI parse, match the native key/formula/masses and have 0 assigned plus 12 unassigned centres. ChEMBL has 10 assigned/2 unassigned; ChEBI and CID145720665 InChIs have 12 assigned. All stereo-stripped standard identities agree. InChI reconstruction yields an imidic-acid tautomer while source SMILES depicts the amide, so this is not a claim of literal graph equality. |
| aro | ARO cache and official CARD comparison; 073-aro-check.py; 073-aro-check.json | supports | Six labels/classes and three exact antibiotic-resistance edges verified using the read-only original ARO OBO cache, SHA256 d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4. All native resistance notes explicitly remain database assertions. Live CARD corroborates determinant labels. |
| imodulondb | iModulonDB via native kg-microbe-sources adapter; 073-imodulondb-datasets.txt; 073-imodulondb-search.txt | context_only | Before web research, the catalog and vmlR query returned gene b_subtilis/modulome/BSU_05610, labelled ABCF ATPase, with no iModulon hit. This is expression-database context only and does not establish resistance or exact compound activity. |
| validation | just validate; just validate-strict; Actual batch008 focused native executions; 073-strict.tsv | supports | Both documented focused validators exited 0; strict scanned one file with zero ERROR rows. Passing them does not resolve chemical stereochemistry. |
| search | Ignored-inclusive local and bounded public research; 073-local-hits.txt and exact source/authority queries | context_only | Local source rows and source-derived assertions were checked. Public work resolved current CARD, ChEBI, ChEMBL and PubChem plus primary structure/mechanism/resistance papers. No claim of exhaustive literature absence is made. |

## Limits And Additional Notes

- All three unique adopted drug/determinant PMID leads were resolved, their abstracts read and relevant full articles inspected. The 1985 structural PDF and original Figure1 were inspected; a complete atom-by-atom reconciliation of conflicting authority stereochemistry remains for curation.
- Europe PMC fullTextXML requests for the 2015 and 2017 papers failed with HTTP500. The 2015 complete PMC HTML was successfully retrieved and inspected; the uninspected 2017 body contributes no finding.
- The 2023 susceptibility Methods and Table1 footnote differ on incubation time. Numeric results are supported by the structured primary table, but conditions must retain this discrepancy. Supplemental 2015 Cfr figure pixels were not independently reviewed, so its exact numerical inhibition-zone sizes are not proposed.
- Required shared gates are coordinated separately; native scientific status remains SEEDED and no sign-off is claimed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Only scratch review artifacts were written; all 19 captured input hashes rechecked unchanged.
- The first chemistry attempt failed at a literal stereo-stripped graph comparison because InChI reconstruction selected the imidic-acid tautomer. The final script correctly compares stereo-stripped standard identities and exits 1 for the independently confirmed missing native stereochemistry.
- iModulonDB lookup preceded open web research; its gene-only context was not promoted into resistance evidence.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T083008Z-a201a-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of A201A
started_at: '2026-10-21T08:18:55Z'
finished_at: '2026-10-21T08:30:08Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Major stereochemical underidentification; primary mechanism and resistance
  evidence support the intended compound with bounded wording and host corrections
scientific_review: true
summary: A201A identity and antibacterial mechanism are supported, but its PubChem-derived
  encodings omit all 12 tetrahedral configurations. Current external representations
  conflict, so the repair requires primary structure reconciliation. A minor finding
  recommends precise tRNA-accommodation wording and claim-level primary evidence;
  imported resistance assertions retain their database qualification.
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
  - path: data/antibiotics/antibacterial/a201a.yaml
    sha256: 4d808505e3b03371f099d9ea90fd3e7cefb37556438d84a253b30a9f130d9320
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
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
scope:
  description: Whole exact A201A record; ARO/PubChem source ownership; all xrefs,
    class and three resistance determinants; every adopted PMID lead; primary structural,
    ribosome and resistance experiments.
  selection: Path-ordered unreviewed queue index 073; exactly one record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-e83eaf8a8a
targets:
- target_id: antibioticmech:aro-e83eaf8a8a
  path: data/antibiotics/antibacterial/a201a.yaml
  label: A201A
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted CARD identity, class and definition reference
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact PubChem structure
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Imported CARD resistance assertions
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Reviewed evidence qualification owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
checks:
- check_id: schema
  name: Documented per-record LinkML validation
  status: passed
  required: true
  summary: Exit 0; No issues found.
  target_ids:
  - antibioticmech:aro-e83eaf8a8a
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/a201a.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented closed-schema validation
  status: passed
  required: true
  summary: Exit 0; one record and zero ERROR rows.
  target_ids:
  - antibioticmech:aro-e83eaf8a8a
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/a201a.yaml --out /private/tmp/am-review-session/073-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Native structure and external stereochemistry comparison
  status: failed
  required: false
  summary: 'Exit 1: internal formula/key/masses and deterministic mint agree, but
    all 12 native tetrahedral centres are unspecified. Source candidates conflict
    and are not approved replacements.'
  target_ids:
  - antibioticmech:aro-e83eaf8a8a
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/073-chemistry.py
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: aro
  name: Exact ARO term and resistance-edge assertions
  status: passed
  required: false
  summary: 'Exit 0: six terms including direct/broader classes and all three exact
    edges are consistent; current CARD page corroborates labels.'
  target_ids:
  - antibioticmech:aro-e83eaf8a8a
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/073-aro-check.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - aro
- check_id: imodulondb-catalog
  name: Structured-source catalog before web research
  status: passed
  required: false
  summary: Exit 0; inspected covered organism/dataset keys.
  target_ids:
  - antibioticmech:aro-e83eaf8a8a
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - imodulondb
- check_id: imodulondb-search
  name: Structured-source vmlR lookup before web research
  status: passed
  required: false
  summary: Exit 0; one gene key and no iModulon hit. No module summary was warranted.
  target_ids:
  - antibioticmech:aro-e83eaf8a8a
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism b_subtilis --dataset modulome --query
    vmlR
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - imodulondb
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-e83eaf8a8a
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
  - antibioticmech:aro-e83eaf8a8a
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
  - antibioticmech:aro-e83eaf8a8a
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
  - antibioticmech:aro-e83eaf8a8a
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
  - antibioticmech:aro-e83eaf8a8a
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
  - antibioticmech:aro-e83eaf8a8a
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
  - antibioticmech:aro-e83eaf8a8a
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
  - antibioticmech:aro-e83eaf8a8a
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
  - antibioticmech:aro-e83eaf8a8a
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/a201a.yaml
  locator: Entire generated record
  accessed_at: '2026-10-21T08:25:02Z'
  support: supports
  summary: Read definition and PMID, broad nucleoside class, full chemistry, four
    xrefs, exact ARO mint, all three target-protection assertions and all three seed/reseed
    events. No separate activity, target, producer, clinical or causal-graph assertions
    are present.
- evidence_id: inventory
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; data/raw/aro_resistance_edges.tsv
  locator: Exact ARO:3007639 rows and maintained owner transforms
  accessed_at: '2026-10-21T08:25:02Z'
  support: supports
  summary: Native definition/class and qualified resistance edges reproduce from ARO;
    the PubChem CID 6441582 row supplies the stereochemically incomplete structure.
    The direct ARO parent is aminonucleoside antibiotic ARO:3000080, whose nucleoside
    ancestor ARO:3000034 is the valid broader native class. Mint remains consistent.
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/6441582
  locator: 073-pubchem.json
  accessed_at: '2026-10-21T08:25:02Z'
  support: partial
  summary: Current CID 6441582 reproduces native HELPZWNRUYNCJQ-QWJSOBSRSA-N, C37H50N6O14
    and absent tetrahedral stereochemistry. Reproducing the adopted source does not
    establish exact natural-product stereochemistry.
  snapshot_sha256: a17cbca7e187b1bc05755acc9c0b29b6e8efac5881d8d712fe37ed72b3af57f9
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:222171
  locator: 073-chebi.html; 073-ols.json
  accessed_at: '2026-10-21T08:25:02Z'
  support: partial
  summary: Non-obsolete 2_STAR A201A term has fully assigned InChI HELPZWNRUYNCJQ-KLBOBXLXSA-N.
    Its SMILES retains 12 tetrahedral assignments but omits both alkene geometries,
    giving HELPZWNRUYNCJQ-MJPRRRBXSA-N. Neither an automatic grounding change nor
    blind SMILES replacement is justified.
  snapshot_sha256: 24bb1a12a20eeec7a94934aac7a71ce6191dd73003c7d795cb753dfd937cc452
- evidence_id: pubchem-full
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/145720665
  locator: 073-pubchem-full.json
  accessed_at: '2026-10-21T08:25:02Z'
  support: partial
  summary: This full-stereo A201A candidate agrees with the ChEBI InChI/key and assigns
    12 centres. It is a comparison candidate, not an approved correction, because
    the ChEMBL/CARD central-sugar stereochemistry differs.
  snapshot_sha256: b7e19db07b32a7fca7a8cce72f2061573bad4cdc8f4c84a45e3414e14109d412
- evidence_id: chembl
  kind: database
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL100042.json
  locator: 073-chembl.json
  accessed_at: '2026-10-21T08:25:02Z'
  support: partial
  summary: ChEMBL assigns 10 of 12 tetrahedral centres; two ribose centres remain
    unspecified. Its standard InChI/key HELPZWNRUYNCJQ-LDAKLULBSA-N differs from the
    fully specified ChEBI/PubChem candidate, including an assigned central-sugar centre.
    Keep the cross-source conflict explicit.
  snapshot_sha256: f8a19fb9c392951dae2d0defbcb454f09de0148491d731b293997370cb033b09
- evidence_id: card
  kind: database
  reference: https://card.mcmaster.ca/ontology/46414
  locator: 073-card.html
  accessed_at: '2026-10-21T08:25:02Z'
  support: partial
  summary: Official ARO:3007639 resolves to A201A with the same four native xrefs,
    definition reference and three determinant labels. Its displayed partial-stereo
    SMILES follows the ChEMBL candidate; database links are not uniformly exact structural
    equivalents.
  snapshot_sha256: 1fc47b3c4dbdbab4f1e02d5b582f4608dd321d1e12387842708d82468638cbb0
- evidence_id: structure-primary
  kind: primary_source
  reference: PMID:4019309
  locator: DOI:10.7164/antibiotics.38.575; 073-primary1985.pdf pp575–580, Fig1 original
    pixels
  accessed_at: '2026-10-21T08:25:02Z'
  support: supports
  summary: Primary chemical/spectroscopic work and a cyclized-derivative X-ray study
    establish a specific sugar stereochemistry for A201A. Figure1 depicts stereodefined
    ribose, central furanose and terminal D-rhamnose; compounds A201C/D/E and hydrogenated
    products are separate. This proves that omitting every tetrahedral assignment
    is materially incomplete, without endorsing an unreviewed authority candidate.
  snapshot_sha256: 58e1ea49d6a94f3352a7a7ce212f8f9481a56806b71864600ac14aea784746f0
- evidence_id: mechanism-primary
  kind: primary_source
  reference: PMID:26028538
  locator: DOI:10.1016/j.molcel.2015.04.014; 073-primary2015.html, A201A Results/Conclusions/Methods
    and Fig6
  accessed_at: '2026-10-21T08:25:02Z'
  support: partial
  summary: T. thermophilus 70S crystallography and E. coli biochemical/smFRET experiments
    support PTC binding and obstruction of full A-tRNA CCA-end accommodation. Initial
    ternary-complex binding still occurs. A201A translation IC50 is 2 µM in a lysate
    GFP assay, not a whole-cell MIC. At 20 µM, reversible tRNA-selection dynamics
    persist about 5 s; the longer HygA delay is separate. Cfr resistance is tested
    in E. coli SQ110DTC ΔtolC by disc diffusion. The older Ard1 efflux description
    is superseded by the inspected 2023 ABCF evidence.
  snapshot_sha256: 3186e40b48364d568cb9683e51ebfa220454a097dde2e24f78381ba57ced5299
- evidence_id: resistance-primary
  kind: primary_source
  reference: PMID:36951104
  locator: DOI:10.1093/nar/gkad193; 073-primary2023.xml, Methods, Results, Table1
    and footnote
  accessed_at: '2026-10-21T08:25:02Z'
  support: supports
  summary: 'Table1 tests A201A in B. subtilis: 168 WT >256 µg/mL, ΔvmlR 4, complemented
    vmlR >256, ATPase-deficient vmlR EQ2 2–4; N. vireti vmlR2 expressed in ΔvmlR >256;
    untagged C. difficile cplR expressed in ΔvmlR 16. Those last two are surrogate-host
    phenotypes, not native-species MICs. Ard1 expression yields 16 versus 4 for its
    EQ2 control, supporting a bounded enrichment opportunity. LB, 1 mM IPTG for expressed
    constructs and Table1 16–20 h at 37°C are explicit; generic Methods instead state
    24 h, a source discrepancy to preserve. No clinical breakpoint is inferred.'
  snapshot_sha256: 3433769330015b23a70824a247fc231c552bae65a61749b745c44c25a6839766
- evidence_id: vmlr-primary
  kind: primary_source
  reference: PMID:30126986
  locator: DOI:10.1073/pnas.1808535115; 073-primary2018.xml
  accessed_at: '2026-10-21T08:25:02Z'
  support: context_only
  summary: The VmlR cryo-EM and mutagenesis study supports ribosome-protection context
    but tests other PTC inhibitors, not A201A. A201A-specific resistance support comes
    from the 2023 paper, not automatic transfer from this earlier structural study.
  snapshot_sha256: 581d4e9dc7f50a263b993226140fb34fcc544752b57f7ed92f32683e0da749d5
- evidence_id: leads
  kind: database
  reference: https://europepmc.org/article/MED/26028538
  locator: 073-core.json; all three unique adopted drug/determinant PMID leads
  accessed_at: '2026-10-21T08:25:02Z'
  support: supports
  summary: Resolved and read abstracts for 26028538, 30126986 and 36951104, then inspected
    each full article for relevant claims. Additional primary structure PMID 4019309
    was resolved and its PDF inspected. The 2014 total-synthesis abstract is only
    a lead; the 2017 fullTextXML fetch failed and supplies no findings.
  snapshot_sha256: fadd9c4ce2d9c8cbef67371a83f20190bad4665e45a50b9ca14ca06d88009911
- evidence_id: chemistry
  kind: validation
  reference: RDKit structure comparisons
  locator: 073-chemistry.py; 073-chemistry.json
  accessed_at: '2026-10-21T08:25:02Z'
  support: supports
  summary: Native SMILES/InChI parse, match the native key/formula/masses and have
    0 assigned plus 12 unassigned centres. ChEMBL has 10 assigned/2 unassigned; ChEBI
    and CID145720665 InChIs have 12 assigned. All stereo-stripped standard identities
    agree. InChI reconstruction yields an imidic-acid tautomer while source SMILES
    depicts the amide, so this is not a claim of literal graph equality.
  snapshot_sha256: f691d8afc3f0e981772a02f36e0421d9945b854d511a6d2b260c49cd96fb08ad
- evidence_id: aro
  kind: validation
  reference: ARO cache and official CARD comparison
  locator: 073-aro-check.py; 073-aro-check.json
  accessed_at: '2026-10-21T08:25:02Z'
  support: supports
  summary: Six labels/classes and three exact antibiotic-resistance edges verified
    using the read-only original ARO OBO cache, SHA256 d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4.
    All native resistance notes explicitly remain database assertions. Live CARD corroborates
    determinant labels.
  snapshot_sha256: fd9f9297106cb95ac4326a205294de40f1fbaaa3b0587a3ac4b8bf9ba19d583b
- evidence_id: imodulondb
  kind: database
  reference: iModulonDB via native kg-microbe-sources adapter
  locator: 073-imodulondb-datasets.txt; 073-imodulondb-search.txt
  accessed_at: '2026-10-21T08:25:02Z'
  support: context_only
  summary: Before web research, the catalog and vmlR query returned gene b_subtilis/modulome/BSU_05610,
    labelled ABCF ATPase, with no iModulon hit. This is expression-database context
    only and does not establish resistance or exact compound activity.
  snapshot_sha256: 5ed5f2e9b2a85fece724071c854e1236017c892e952c7c4fdbe97e230bff2554
- evidence_id: validation
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual batch008 focused native executions; 073-strict.tsv
  accessed_at: '2026-10-21T08:25:02Z'
  support: supports
  summary: Both documented focused validators exited 0; strict scanned one file with
    zero ERROR rows. Passing them does not resolve chemical stereochemistry.
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local and bounded public research
  locator: 073-local-hits.txt and exact source/authority queries
  accessed_at: '2026-10-21T08:25:02Z'
  support: context_only
  summary: Local source rows and source-derived assertions were checked. Public work
    resolved current CARD, ChEBI, ChEMBL and PubChem plus primary structure/mechanism/resistance
    papers. No claim of exhaustive literature absence is made.
  search_scope: prepare.py 73 ran rg --no-ignore --hidden, excluding only .git and
    .venv, before judgment; exact A201A, ARO:3007639, native key and primary PMID
    searches followed.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact natural-product stereochemistry
  outcome: concern
  summary: The intended A201A is clear, but native encodings denote its stereo-unspecified
    structure and omit all 12 tetrahedral configurations.
  target_ids:
  - antibioticmech:aro-e83eaf8a8a
  evidence_ids:
  - record
  - structure-primary
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Class, mint and source xrefs
  outcome: supported
  summary: Valid broader nucleoside class and deterministic ARO mint. Current ChEBI
    is a 2_STAR comparison term; changing native grounding is not implied.
  target_ids:
  - antibioticmech:aro-e83eaf8a8a
  evidence_ids:
  - inventory
  - aro
  - chebi
- assessment_id: xref-scope
  area: consistency
  topic: Cross-authority structure conflict
  outcome: concern
  summary: Native CID, partial-stereo ChEMBL/CARD and fully assigned ChEBI/PubChem
    candidates cannot be treated as identical stereochemical encodings.
  target_ids:
  - antibioticmech:aro-e83eaf8a8a
  evidence_ids:
  - chemistry
  - pubchem
  - pubchem-full
  - chembl
  - card
- assessment_id: mechanism
  area: scope
  topic: Initial binding versus full accommodation
  outcome: concern
  summary: Broad translation/PTC mechanism is supported, but the final definition
    sentence needs the CCA-end/full-accommodation qualification.
  target_ids:
  - antibioticmech:aro-e83eaf8a8a
  evidence_ids:
  - record
  - mechanism-primary
- assessment_id: resistance
  area: evidence
  topic: Three qualified database assertions
  outcome: supported
  summary: All exact ARO assertions reproduce; 2023 primary data independently support
    their resistance potential with host-specific limits.
  target_ids:
  - antibioticmech:aro-e83eaf8a8a
  evidence_ids:
  - aro
  - resistance-primary
  - vmlr-primary
- assessment_id: completeness
  area: completeness
  topic: Available primary annotation
  outcome: concern
  summary: Concrete primary mechanism, susceptibility and resistance evidence can
    be annotated; optional emptiness alone is not the finding.
  target_ids:
  - antibioticmech:aro-e83eaf8a8a
  evidence_ids:
  - record
  - mechanism-primary
  - resistance-primary
- assessment_id: optional
  area: representation
  topic: Producer, clinical, causal graph and datasets
  outcome: not_applicable
  summary: No such native assertions require correction; source-producer history and
    candidate graphs need separate claim-level curation.
  target_ids:
  - antibioticmech:aro-e83eaf8a8a
  evidence_ids:
  - record
- assessment_id: ownership
  area: ownership
  topic: Generated fields and history
  outcome: supported
  summary: Actual ARO/PubChem owners captured before judgment; all 19 input hashes
    remain unchanged and seed/reseed history is coherent.
  target_ids:
  - antibioticmech:aro-e83eaf8a8a
  evidence_ids:
  - inventory
  - record
- assessment_id: schema
  area: schema
  topic: Focused native gates
  outcome: supported
  summary: Documented per-record validators pass; supplemental chemistry finds a semantic
    defect they do not cover.
  target_ids:
  - antibioticmech:aro-e83eaf8a8a
  evidence_ids:
  - validation
  - chemistry
findings:
- finding_id: F1
  issue_key: aro-3007639-a201a-tetrahedral-stereochemistry-underidentified
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: A201A native structure leaves all 12 tetrahedral centres unspecified
  description: The source-derived structure agrees internally but cannot represent
    the specific natural-product stereochemistry established by primary chemistry.
    Candidate authority encodings also disagree; repairing only the displayed SMILES
    or blindly adopting a new xref would leave an inconsistent record.
  target_ids:
  - antibioticmech:aro-e83eaf8a8a
  field_paths:
  - chemical_structure.smiles
  - chemical_structure.standard_inchi
  - chemical_structure.standard_inchi_key
  - xrefs
  evidence_ids:
  - record
  - structure-primary
  - chemistry
  - chebi
  - chembl
  - pubchem-full
  rule_id: 'review-checklist: Identity and chemical structure'
  native_severity: major semantic underidentification with source disagreement
  normalization_reason: Intended compound remains clear, so this is a major representation
    defect rather than a wrong-target blocker.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Maintained ARO-to-PubChem structure row
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Source selection and structure extraction
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Source xrefs and adopted definition
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated representation
- finding_id: F2
  issue_key: aro-3007639-a201a-primary-mechanism-qualification
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Clarify tRNA accommodation and annotate available claim-level primary evidence
  description: The PTC mechanism is sound but the unqualified A-site-binding sentence
    obscures the experimentally preserved initial binding step. Exact primary mechanism
    and resistance data support a bounded annotation with assay and surrogate-host
    scope.
  target_ids:
  - antibioticmech:aro-e83eaf8a8a
  field_paths:
  - definition
  - evidence
  - mode_of_action
  - mode_of_action_notes
  - molecular_targets
  - resistance_mechanisms
  - activity_spectrum
  evidence_ids:
  - record
  - mechanism-primary
  - resistance-primary
  - vmlr-primary
  rule_id: 'review-checklist: Evidence standard, Mechanism and Resistance'
  native_severity: minor wording and actionable primary-evidence enrichment
  normalization_reason: The broad existing mechanism and qualified database edges
    are supported; the correction refines the step and enriches concrete evidence
    without penalizing empty optional fields.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/a201a.yaml
    role: Curator-owned claim-level evidence, mode_of_action, mode_of_action_notes,
      molecular_targets and resistance_mechanisms via validated writer/history
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Maintained reviewed CARD evidence qualifications
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted definition and primary reference
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO definition extraction owner
actions:
- action_id: A1
  description: Reconcile primary A201A stereochemistry and all source encodings, then
    repair the maintained structure selection and regenerate.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-e83eaf8a8a
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Maintained ARO-to-PubChem structure row
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Source selection and structure extraction
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Source xrefs and adopted definition
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated representation
  acceptance_checks:
  - Atom-map the three sugar stereochemistries and both alkene geometries against
    primary Figure1 and supporting chemical evidence. Resolve the assigned central-sugar
    conflict between ChEMBL/CARD and ChEBI/PubChem; do not approve any candidate solely
    from database naming.
  - Represent the experimentally supported specific stereoisomer with mutually consistent
    isomeric SMILES, standard InChI/key and exact xref scope. Preserve amide versus
    normalized InChI tautomer distinctions.
  - Correct the maintained ARO-to-structure selection before reseeding through scripts/seed_from_sources.py;
    retain provenance and avoid a generated-YAML-only patch.
  - Recheck all centres, alkene geometry, source xrefs, deterministic mint, schema/strict
    and required corpus gates; review regeneration diff before scientific sign-off.
- action_id: A2
  description: Curate the supported primary mechanism and resistance claims with precise
    scope and reproducible definition wording.
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:aro-e83eaf8a8a
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/a201a.yaml
    role: Curator-owned claim-level evidence, mode_of_action, mode_of_action_notes,
      molecular_targets and resistance_mechanisms via validated writer/history
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Maintained reviewed CARD evidence qualifications
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted definition and primary reference
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO definition extraction owner
  acceptance_checks:
  - State that A201A binds the PTC and obstructs full CCA-end accommodation and peptide-bond
    formation while initial ternary-complex binding can occur. Retain PMID26028538
    at that claim.
  - Keep 2 µM translation IC50 separate from whole-cell MIC, the 20 µM smFRET exposure,
    and HygA-specific values.
  - Use PMID36951104 for A201A-specific VmlR/VmlR2/CplR resistance; preserve B.subtilis
    surrogate hosts and distinguish native-species gene origin from assay organism.
    Preserve inequalities and ATPase-mutant/tag controls.
  - Keep the Table1 16–20 h versus generic Methods 24 h discrepancy visible if extracting
    MIC conditions. Do not infer clinical breakpoints, direct A201A displacement from
    a drug-free protection-factor structure, or an efflux mechanism for Ard1.
  - Use claim-level PRIMARY_LITERATURE evidence only after exact mappings and reviewed
    protein examples are resolved; run all required native gates and add validated
    curation history before REVIEWED status.
limitations:
- All three unique adopted drug/determinant PMID leads were resolved, their abstracts
  read and relevant full articles inspected. The 1985 structural PDF and original
  Figure1 were inspected; a complete atom-by-atom reconciliation of conflicting authority
  stereochemistry remains for curation.
- Europe PMC fullTextXML requests for the 2015 and 2017 papers failed with HTTP500.
  The 2015 complete PMC HTML was successfully retrieved and inspected; the uninspected
  2017 body contributes no finding.
- The 2023 susceptibility Methods and Table1 footnote differ on incubation time. Numeric
  results are supported by the structured primary table, but conditions must retain
  this discrepancy. Supplemental 2015 Cfr figure pixels were not independently reviewed,
  so its exact numerical inhibition-zone sizes are not proposed.
- Required shared gates are coordinated separately; native scientific status remains
  SEEDED and no sign-off is claimed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Only scratch review artifacts were written; all 19 captured input hashes rechecked
  unchanged.
- The first chemistry attempt failed at a literal stereo-stripped graph comparison
  because InChI reconstruction selected the imidic-acid tautomer. The final script
  correctly compares stereo-stripped standard identities and exits 1 for the independently
  confirmed missing native stereochemistry.
- iModulonDB lookup preceded open web research; its gene-only context was not promoted
  into resistance evidence.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://doi.org/10.7164/antibiotics.38.575
- https://doi.org/10.1016/j.molcel.2015.04.014
- https://doi.org/10.1093/nar/gkad193
- https://doi.org/10.1073/pnas.1808535115
- https://card.mcmaster.ca/ontology/46414
- https://www.ebi.ac.uk/chebi/CHEBI:222171
tags:
- record-review
- a201a
- stereochemistry
- ribosome
- surrogate-host-resistance
```
