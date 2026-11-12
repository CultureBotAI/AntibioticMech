# Imazalil: coherent neutral graph and qualified fungal resistance association

- Review: 20261021T184524Z-imazalil-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T18:07:39Z
- Finished UTC: 2026-10-21T18:45:24Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native neutral graph agrees with current PubChem and ChEMBL, with one unspecified tetrahedral centre. Its sole adopted original was read beyond the abstract and supports the imidazole definition, while its Aspergillus fumigatus experiments must not be transferred to the separate A. flavus Cyp51C database edge. That edge is already explicitly database-qualified. Exact neutral imazalil in a later primary bacterial growth screen supports the qualitative antibacterial classification. No confirmed required correction was found; material, causal and access limits remain explicit. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Assigned queue position 548; one exact native record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-c1dea01a87 | data/antibiotics/antibacterial/imazalil.yaml | generated | imazalil |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-c1dea01a87 | Actual focused execution exited 0. Executed against 055; chemistry used the existing 019 RDKit interpreter, while schema/strict used 055. |
| Focused schema verification | passed | True | antibioticmech:aro-c1dea01a87 | Actual focused execution exited 0. Executed against 055; chemistry used the existing 019 RDKit interpreter, while schema/strict used 055. |
| Focused strict verification | passed | True | antibioticmech:aro-c1dea01a87 | Actual focused execution exited 0. Executed against 055; chemistry used the existing 019 RDKit interpreter, while schema/strict used 055. |
| Authoritative full QC | failed | True | antibioticmech:aro-c1dea01a87 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-c1dea01a87 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-c1dea01a87 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-c1dea01a87 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-c1dea01a87 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-c1dea01a87 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-c1dea01a87 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-c1dea01a87 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-c1dea01a87 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Neutral imidazole identity, unspecified stereochemistry and minted identifier

identity: supported. Targets: antibioticmech:aro-c1dea01a87.

Native formula, charge, masses, encodings and source-derived mint are coherent. Current PubChem and ChEMBL agree exactly. One unassigned tetrahedron is preserved; it does not by itself establish a racemate, individual enantiomer or sulfate salt.

### Chemical xrefs, ARO class and additional ChEBI comparators

grounding: supported. Targets: antibioticmech:aro-c1dea01a87.

Asserted accessible molecular links and the current ARO accession/class agree with the native record. CAS content remains access-limited. The additional neutral ChEBI graph matches, whereas the separately defined racemate requires its own material semantics; neither produces a forced reminting finding.

### Antibacterial eligibility and endpoint/material specificity

evidence: supported. Targets: antibioticmech:aro-c1dea01a87.

The 2025 primary library metadata resolve neutral imazalil and three significant bacterial growth-screen results under specified conditions. This supports the qualitative antibacterial category despite the molecule’s conventional antifungal use. Sulfate dose-validation, quaternary derivatives and formulated-composite endpoints are distinct and cannot supply neutral-compound MICs.

### Already-qualified A. flavus Cyp51C database association

evidence: unknown. Targets: antibioticmech:aro-c1dea01a87.

The native evidence explicitly says database assertion, not primary citation, and faithfully reproduces current ARO. The adopted paper studies A. fumigatus Cyp51A, while a separate A. flavus study provides a mutation/expression association without genetic causal proof. No unsupported upgrade is made and no new finding is inferred solely from the existing primary-evidence gap.

### Optional biological detail and all adopted leads

completeness: unknown. Targets: antibioticmech:aro-c1dea01a87.

The sole adopted citation was read beyond its abstract. Optional quantitative activity, primary fungal resistance and antifungal-role annotations could be added only with exact material, taxon and endpoint qualifiers; their absence is not a confirmed defect. No direct bacterial mechanism is established by the inspected originals.

### Actual ARO owners and unchanged native/history

provenance: supported. Targets: antibioticmech:aro-c1dea01a87.

The complete record, source concept and all three seed/reseed history events were checked against actual ARO inventories and maintained generator ownership. Original 13 and expanded 24 input hashes remain unchanged; no reviewed-status promotion or native mutation was performed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optional primary enrichment should retain the exact preparation, strain and evidence tier.

- If adding bacterial observations, retain neutral catalog 32007-100MG, 20 µM, mGAM, anaerobic 37 °C for 24 h, exact culture accessions and growth-AUC endpoint; do not label this screen a MIC or bactericidal experiment.
- Keep imazalil sulfate, quaternary derivative and composite formulations separate from the neutral graph. Do not infer enantiomeric composition from an unspecified molecular representation.
- Keep A. fumigatus Cyp51A recombinant results distinct from A. flavus Cyp51C isolate associations. Do not upgrade H349R to a proven causal determinant without independent genetic evidence, and adjudicate the source’s inconsistent mutation prose first.
- If considering additional ChEBI grounding, distinguish neutral CHEBI:83829 from explicitly racemic CHEBI:81927 and apply maintained source/mint rules rather than changing identifiers from name similarity alone.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/imazalil.yaml; Entire native record, all chemical fields, four xrefs, source concept, resistance evidence and three history events | supports | The MINTED, SEEDED record denotes neutral C14H14Cl2N2O with key PZBPKYOVPCNPJY-UHFFFAOYSA-N. The one resistance entry names Aspergillus flavus Cyp51C and expressly labels the CARD/ARO relationship as a database assertion rather than primary evidence. No molecular target, activity_spectrum, causal graph, product or producer is asserted. |
| owners | data/raw/aro_antibiotics.tsv#ARO:3009554; Complete molecule row 644, resistance row 4556, readiness row 2723 and exact owner searches | context_only | The ARO molecule row supplies the definition, sole adopted PMID, parent and chemical links. The resistance row reproduces ARO:3009555 confers_resistance_to_antibiotic ARO:3009554. No exact target, ChEBI inventory, curator or decision row was found in the inspected tables. Original 13 captures were preserved and expanded to 24 actual owner/context inputs before judgment. |
| search | /private/tmp/am-review-session/548-context-search.txt; Initial and owner-follow-up searches including ignored and hidden files | context_only | Exact identifier, label, ARO IDs and source ownership were searched with ignored-inclusive coverage. Public Europe PMC discovery used exact compound and bacterial/Cyp51C terms; discovery hits were not all treated as fully adjudicated evidence. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/37175/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON; CID 37175 complete current property response | supports | Current PubChem supplies the same neutral molecular graph, full key, formula, charge, average mass and monoisotopic mass as native. It does not configure the one tetrahedral centre. |
| chembl | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL356918.json; CHEMBL356918 molecular encodings and identity | supports | The ChEMBL enilconazole record has the same neutral unspecified-stereo graph in SMILES, InChI and molfile. The different preferred label is not a chemical mismatch. |
| mapping | /private/tmp/am-review-session/548-map.py; 019 RDKit 2026.03.5 executed against 055; nine independent encodings | supports | Native SMILES/InChI, PubChem SMILES/InChI, ChEMBL SMILES/InChI/molfile and the additional unasserted CHEBI:83829 SMILES/InChI all reproduce the same full key and reciprocal chirality-aware graph matches. Each has one unspecified tetrahedron, formula C14H14Cl2N2O and zero charge. |
| chebi-comparator | https://www.ebi.ac.uk/chebi/backend/api/public/compound/83829/; Additional unasserted CHEBI:83829 identity | context_only | This systematically named imidazole has the same neutral unspecified graph. It is an additional comparator, not a native accession or an automatic instruction to remint the record. |
| racemate | https://www.ebi.ac.uk/chebi/backend/api/public/compound/81927/; Additional CHEBI:81927 definition and absence of a single default structure | context_only | ChEBI enilconazole is explicitly an equimolar R/S racemate. Native one-centre underspecification alone does not assert an equimolar mixture, and neither this racemate nor the sulfate salt is substituted automatically for the neutral native graph. |
| aro | https://purl.obolibrary.org/obo/aro.obo; Exact current terms ARO:3009554, ARO:3009555 and ARO:3007500 | supports | The official current OBO preserves the same imazalil molecule/class and Cyp51C resistance relationship. The resistance term describes fungal ergosterol biology but supplies no direct PMID in its own term block. Native already discloses the database tier, so absence of a primary citation is not itself a new major defect. |
| adapter | /private/tmp/am-review-session/548-adapter-scope.json; Structured-source applicability assessed before open literature research | context_only | The inspected iModulonDB dataset catalog contains no Aspergillus or other fungal dataset suitable for native A. flavus Cyp51C. The structured route is therefore not applicable; no unrelated bacterial homolog is substituted. This is not evidence for or against the fungal resistance association. |
| adopted | PMID:29507067; DOI:10.1128/AAC.01549-17; Sole adopted abstract and full scientific main text; Tables 1/3 text inspected | supports | The original studies agricultural imidazole resistance in A. fumigatus Cyp51A backgrounds. It supports the native imidazole definition, but does not directly validate the different A. flavus Cyp51C edge. EUCAST E.DEF9.3 testing used imazalil 0.06–32 mg/L with at least three repetitions; lot, purity and exact salt/stereochemical composition were not resolved from the inspected main. Table 2 alignment image and figure pixels were not independently inspected. |
| adopted-alleles | PMID:29507067; Original Table 3 recombinant-strain imazalil column and matching discussion | context_only | CEAΔku80 has imazalil MIC 0.125 mg/L, F495I alone 0.5 mg/L, TR34/L98H 4–8 mg/L, TR34/L98H/F495I 8 mg/L and the TR34/L98H/S297T/F495I combination 16 mg/L. The altered background matters, and the authors caution about one- or two-dilution differences and absent agricultural-azole clinical breakpoints. These findings are not generalized to Cyp51C or another Aspergillus species. |
| primary2020 | PMID:33080784; DOI:10.3390/genes11101217; Selected original Methods 2.2–2.7, Results, Tables 2/5 and complete Discussion | context_only | This A. flavus clinical-isolate study used Sigma-Aldrich imazalil at 0.06–32 mg/L under EUCAST conditions at 35 °C, with visible growth assessed at 24/48 h. CM9326 has imazalil MIC 32 mg/L and Cyp51C H349R in Table 5, together with altered expression of Cyp51A/C. The authors explicitly lack genetic-manipulation proof that this substitution causes the phenotype. This is an isolate-level association, not purified target inhibition or an isogenic causal result. |
| primary2020-limits | PMID:33080784; Table 5 versus mutation text; compound and causal boundaries | context_only | The paper contains inconsistent nucleotide-position and residue descriptions in surrounding prose; Table 5 labels H349R. Exact nucleotide/allele assertions are not imported from that inconsistency. Reagent catalog, purity and enantiomeric composition were not specified in the inspected methods. The source supports a cautious association follow-up without upgrading the existing native database claim. |
| primary2025 | PMID:41299073; DOI:10.1038/s41564-025-02182-6; Selected original library, growth-screen Methods/Results and Supplementary Data 1–4 | supports | The library screened compounds at 20 µM in mGAM, starting OD600 0.05, 1% DMSO, 37 °C and anaerobic conditions, with growth recorded for 24 h in three biological replicates. A hit required &gt;20% AUC reduction and adjusted P &lt; 0.05 in at least two replicates. This is growth inhibition, not a clinical MIC, bactericidal endpoint or bacterial target assay. |
| primary2025-material | https://static-content.springer.com/esm/art%3A10.1038%2Fs41564-025-02182-6/MediaObjects/41564_2025_2182_MOESM3_ESM.xlsx; SuppData1 rows 604/605; original workbook XML inspected | supports | Neutral IMAZALIL is item 3_D12, catalog 32007-100MG, CID 37175, with the native formula, SMILES, InChI and full key. IMAZALIL SULFATE is a separate item 12_F10, catalog 33997-100MG-R, CID 173636 and sulfuric-acid-containing formula/key. These explicitly distinct preparations are not pooled. |
| primary2025-results | https://static-content.springer.com/esm/art%3A10.1038%2Fs41564-025-02182-6/MediaObjects/41564_2025_2182_MOESM3_ESM.xlsx; SuppData3 rows 11395/14623/22155 joined to SuppData2 rows 14/17/24 | supports | Neutral item 3_D12 has three significant growth-inhibition hits among 22 tested strains: Coprococcus comes ATCC 27758 (normalized median AUC 0.07229462), Eubacterium rectale DSM 17629 (0.06067131) and Roseburia intestinalis DSM 14610 (0.7672064). The reported adjusted P values are 4.66e-52, 2.35e-14 and 2.61e-5, respectively. This directly supports bounded antibacterial activity for the neutral library material without assuming activity in all bacteria. |
| primary2025-boundary | /private/tmp/am-review-session/548-compact.py; Raw ZIP/XML extraction and exact compound/strain joins | context_only | The independent extraction finds 22 neutral imazalil screening rows, exactly three significant hits, and no neutral-imazalil rows in SuppData4 validation. All 64 imazalil-related validation rows there are sulfate. Consequently, the main-text 2.5 µM sulfate example is not transferred to neutral imazalil. Other compounds’ genetic mechanisms are not assigned to this molecule. |
| primary2022 | PMID:36364655; DOI:10.3390/nano12213879; Full scientific main read; actual Scheme 1 and SI Figure S1 viewed | context_only | The study distinguishes purchased imazalil from an N-dodecyl quaternary imidazolium derivative and its copper-framework formulation. The introduction mistakenly describes an anilinopyrimidine, whereas actual Scheme 1 depicts the correct neutral imazalil constitution. This source inconsistency is preserved. Only the panels explicitly labeled imazalil are considered supporting free-compound evidence; derivative/composite potency is not transferred. |
| primary2022-si | https://mdpi-res.com/d_attachment/nanomaterials/nanomaterials-12-03879/article_deploy/nanomaterials-12-03879-s001.zip; Extracted SI PDF page 2, actual Figure S1 panels a/b/e/f | context_only | Free-imazalil panels report concentration-dependent growth effects on P. syringae pv. lachrymans and X. campestris pv. campestris. P. syringae still grows at the highest shown 100 mg/L; X. campestris has a near-flat/declining OD trace at 200 mg/L. No exact MIC, killing claim or statistical significance is inferred from these qualitative curves. Strain accessions and reagent catalog/purity are unresolved. |
| access | /private/tmp/am-review-session/548-fetch1.json; Public retrieval logs 548-fetch1–7 and successful primary alternatives | context_only | CAS API returned 401, OLS exact new ARO terms 404 and Europe PMC’s 2018 XML route 500; the official OBO and PMC HTML supplied the relevant alternative records. A guessed supplementary host failed DNS, while the official Springer host supplied the workbook. The supplier page request failed HTTP/2; catalog identity is read from the original workbook, not claimed independently verified from the supplier. |

## Limits And Additional Notes

- The sole adopted original 2018 scientific main and Tables 1/3 were read, but Table 2 alignment image and figure pixels were not independently inspected. Exact reagent lot, purity and stereochemical composition remain unresolved.
- The 2020 original was read selectively for A. flavus material, sequencing/expression, susceptibility tables and causal limitations. Source mutation-text discrepancies and absent genetic proof prevent a precise causal upgrade of the native database association.
- The 2025 study was read selectively for library identity, growth-screen methods/results and exact workbook rows. Raw OD traces and all unrelated mechanism experiments were not independently reanalysed. Neutral screen hits are not sulfate dose-validation or clinical MIC evidence.
- The 2022 scientific main, actual Scheme 1 and actual SI Figure S1 were inspected; source introduction chemistry conflicts with its drawing, and strain catalog/purity detail is limited. No derivative/composite endpoint or curve-derived MIC is transferred.
- CAS 401, exact OLS term 404 and supplier HTTP/2 access limits remain recorded. Official ARO OBO, primary HTML and the final official workbook route supplied successful alternatives where stated.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All original 13 and expanded 24 input hashes were rechecked unchanged before draft writing. No native/source/history/progress/saved-bundle/Git writes occurred.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T184524Z-imazalil-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Imazalil: coherent neutral graph and qualified fungal resistance association'
started_at: '2026-10-21T18:07:39Z'
finished_at: '2026-10-21T18:45:24Z'
reviewer:
  identity: Codex
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
summary: The native neutral graph agrees with current PubChem and ChEMBL, with one
  unspecified tetrahedral centre. Its sole adopted original was read beyond the abstract
  and supports the imidazole definition, while its Aspergillus fumigatus experiments
  must not be transferred to the separate A. flavus Cyp51C database edge. That edge
  is already explicitly database-qualified. Exact neutral imazalil in a later primary
  bacterial growth screen supports the qualitative antibacterial classification. No
  confirmed required correction was found; material, causal and access limits remain
  explicit. Scientific assessment retains the stated evidence limits; full verification
  is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/imazalil.yaml
    sha256: a21f68711db34df975cc2383bbd03647202e3dff3f84bbd9b89c53b771bc9552
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
targets:
- target_id: antibioticmech:aro-c1dea01a87
  path: data/antibiotics/antibacterial/imazalil.yaml
  label: imazalil
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual ARO molecule identity, classification, structure and citation owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Actual imported resistance assertion owner
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: ARO classification and source merge rules
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record field owner
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Assigned queue position 548; one exact native record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-c1dea01a87
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0. Executed against 055; chemistry used
    the existing 019 RDKit interpreter, while schema/strict used 055.
  target_ids:
  - antibioticmech:aro-c1dea01a87
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    548
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Executed against 055; chemistry used
    the existing 019 RDKit interpreter, while schema/strict used 055.
  target_ids:
  - antibioticmech:aro-c1dea01a87
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/imazalil.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Executed against 055; chemistry used
    the existing 019 RDKit interpreter, while schema/strict used 055.
  target_ids:
  - antibioticmech:aro-c1dea01a87
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/imazalil.yaml --out /private/tmp/am-review-session/548-strict.tsv
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
  - antibioticmech:aro-c1dea01a87
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
  - antibioticmech:aro-c1dea01a87
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
  - antibioticmech:aro-c1dea01a87
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
  - antibioticmech:aro-c1dea01a87
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
  - antibioticmech:aro-c1dea01a87
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
  - antibioticmech:aro-c1dea01a87
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
  - antibioticmech:aro-c1dea01a87
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
  - antibioticmech:aro-c1dea01a87
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
  - antibioticmech:aro-c1dea01a87
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/imazalil.yaml
  locator: Entire native record, all chemical fields, four xrefs, source concept,
    resistance evidence and three history events
  accessed_at: '2026-10-21T18:37:44Z'
  support: supports
  summary: The MINTED, SEEDED record denotes neutral C14H14Cl2N2O with key PZBPKYOVPCNPJY-UHFFFAOYSA-N.
    The one resistance entry names Aspergillus flavus Cyp51C and expressly labels
    the CARD/ARO relationship as a database assertion rather than primary evidence.
    No molecular target, activity_spectrum, causal graph, product or producer is asserted.
  snapshot_sha256: a21f68711db34df975cc2383bbd03647202e3dff3f84bbd9b89c53b771bc9552
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv#ARO:3009554
  locator: Complete molecule row 644, resistance row 4556, readiness row 2723 and
    exact owner searches
  accessed_at: '2026-10-21T18:37:44Z'
  support: context_only
  summary: The ARO molecule row supplies the definition, sole adopted PMID, parent
    and chemical links. The resistance row reproduces ARO:3009555 confers_resistance_to_antibiotic
    ARO:3009554. No exact target, ChEBI inventory, curator or decision row was found
    in the inspected tables. Original 13 captures were preserved and expanded to 24
    actual owner/context inputs before judgment.
  snapshot_sha256: e8e2bbceee97ca63f1ef15b66d9b138a9963b974e69cc5c249d003864de0ddf2
- evidence_id: search
  kind: search
  reference: /private/tmp/am-review-session/548-context-search.txt
  locator: Initial and owner-follow-up searches including ignored and hidden files
  accessed_at: '2026-10-21T18:37:44Z'
  support: context_only
  summary: Exact identifier, label, ARO IDs and source ownership were searched with
    ignored-inclusive coverage. Public Europe PMC discovery used exact compound and
    bacterial/Cyp51C terms; discovery hits were not all treated as fully adjudicated
    evidence.
  snapshot_sha256: c453654553b44dc320578b00288a9243e2ad9d45bf7b9c20eff2a0afa81b184d
  search_scope: Initial 548-local-hits.txt plus rg --no-ignore --hidden follow-up
    in worktree 055; public exact-compound searches preserved in 548-fetch1/2 manifests.
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/37175/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON
  locator: CID 37175 complete current property response
  accessed_at: '2026-10-21T18:30:15.455622Z'
  support: supports
  summary: Current PubChem supplies the same neutral molecular graph, full key, formula,
    charge, average mass and monoisotopic mass as native. It does not configure the
    one tetrahedral centre.
  snapshot_sha256: ceffb192a6f016f0233c4cf281be38137cd0c023b87e2a0acb39780ec28ba308
- evidence_id: chembl
  kind: authority
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL356918.json
  locator: CHEMBL356918 molecular encodings and identity
  accessed_at: '2026-10-21T18:30:15.455950Z'
  support: supports
  summary: The ChEMBL enilconazole record has the same neutral unspecified-stereo
    graph in SMILES, InChI and molfile. The different preferred label is not a chemical
    mismatch.
  snapshot_sha256: e00f643fc42b0033a381d0f468feb630d216147fa9e8f97390eeae68b1a3d320
- evidence_id: mapping
  kind: validation
  reference: /private/tmp/am-review-session/548-map.py
  locator: 019 RDKit 2026.03.5 executed against 055; nine independent encodings
  accessed_at: '2026-10-21T18:37:44Z'
  support: supports
  summary: Native SMILES/InChI, PubChem SMILES/InChI, ChEMBL SMILES/InChI/molfile
    and the additional unasserted CHEBI:83829 SMILES/InChI all reproduce the same
    full key and reciprocal chirality-aware graph matches. Each has one unspecified
    tetrahedron, formula C14H14Cl2N2O and zero charge.
  snapshot_sha256: b1b674736ad334915c033bb66b3e2cb864ab7642136d8aa8b41f6f374ff94b95
- evidence_id: chebi-comparator
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/83829/
  locator: Additional unasserted CHEBI:83829 identity
  accessed_at: '2026-10-21T18:33:22.038681Z'
  support: context_only
  summary: This systematically named imidazole has the same neutral unspecified graph.
    It is an additional comparator, not a native accession or an automatic instruction
    to remint the record.
  snapshot_sha256: 79cdaeabf087bc1c6d2244a2f157b675826808f6ac2db679b9fdf9db04758e65
- evidence_id: racemate
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/81927/
  locator: Additional CHEBI:81927 definition and absence of a single default structure
  accessed_at: '2026-10-21T18:30:37.029469Z'
  support: context_only
  summary: ChEBI enilconazole is explicitly an equimolar R/S racemate. Native one-centre
    underspecification alone does not assert an equimolar mixture, and neither this
    racemate nor the sulfate salt is substituted automatically for the neutral native
    graph.
  snapshot_sha256: 3cce626f344f7a64c20fca00367ba494ff8576258ed32ba2801c1a340d79bd4b
- evidence_id: aro
  kind: authority
  reference: https://purl.obolibrary.org/obo/aro.obo
  locator: Exact current terms ARO:3009554, ARO:3009555 and ARO:3007500
  accessed_at: '2026-10-21T15:57:42Z'
  support: supports
  summary: The official current OBO preserves the same imazalil molecule/class and
    Cyp51C resistance relationship. The resistance term describes fungal ergosterol
    biology but supplies no direct PMID in its own term block. Native already discloses
    the database tier, so absence of a primary citation is not itself a new major
    defect.
  snapshot_sha256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
- evidence_id: adapter
  kind: search
  reference: /private/tmp/am-review-session/548-adapter-scope.json
  locator: Structured-source applicability assessed before open literature research
  accessed_at: '2026-10-21T18:37:44Z'
  support: context_only
  summary: The inspected iModulonDB dataset catalog contains no Aspergillus or other
    fungal dataset suitable for native A. flavus Cyp51C. The structured route is therefore
    not applicable; no unrelated bacterial homolog is substituted. This is not evidence
    for or against the fungal resistance association.
  snapshot_sha256: 64f6d3e6ae588ff9a2dfdc2c1148abf15de0cfec40b3b6192cc50218cbc55972
  search_scope: Preserved official catalog 456460-adapter-catalog.txt, SHA 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549;
    applicability recorded before web retrieval.
- evidence_id: adopted
  kind: primary_source
  reference: PMID:29507067; DOI:10.1128/AAC.01549-17
  locator: Sole adopted abstract and full scientific main text; Tables 1/3 text inspected
  accessed_at: '2026-10-21T18:31:03.676352Z'
  support: supports
  summary: The original studies agricultural imidazole resistance in A. fumigatus
    Cyp51A backgrounds. It supports the native imidazole definition, but does not
    directly validate the different A. flavus Cyp51C edge. EUCAST E.DEF9.3 testing
    used imazalil 0.06–32 mg/L with at least three repetitions; lot, purity and exact
    salt/stereochemical composition were not resolved from the inspected main. Table
    2 alignment image and figure pixels were not independently inspected.
  snapshot_sha256: ee8385133222d01d3acca44af7fe3e0fb3f6e8a2c87d249cd9e4dd059e458d68
- evidence_id: adopted-alleles
  kind: primary_source
  reference: PMID:29507067
  locator: Original Table 3 recombinant-strain imazalil column and matching discussion
  accessed_at: '2026-10-21T18:31:03.676352Z'
  support: context_only
  summary: CEAΔku80 has imazalil MIC 0.125 mg/L, F495I alone 0.5 mg/L, TR34/L98H 4–8
    mg/L, TR34/L98H/F495I 8 mg/L and the TR34/L98H/S297T/F495I combination 16 mg/L.
    The altered background matters, and the authors caution about one- or two-dilution
    differences and absent agricultural-azole clinical breakpoints. These findings
    are not generalized to Cyp51C or another Aspergillus species.
  snapshot_sha256: ee8385133222d01d3acca44af7fe3e0fb3f6e8a2c87d249cd9e4dd059e458d68
- evidence_id: primary2020
  kind: primary_source
  reference: PMID:33080784; DOI:10.3390/genes11101217
  locator: Selected original Methods 2.2–2.7, Results, Tables 2/5 and complete Discussion
  accessed_at: '2026-10-21T18:30:47.928583Z'
  support: context_only
  summary: This A. flavus clinical-isolate study used Sigma-Aldrich imazalil at 0.06–32
    mg/L under EUCAST conditions at 35 °C, with visible growth assessed at 24/48 h.
    CM9326 has imazalil MIC 32 mg/L and Cyp51C H349R in Table 5, together with altered
    expression of Cyp51A/C. The authors explicitly lack genetic-manipulation proof
    that this substitution causes the phenotype. This is an isolate-level association,
    not purified target inhibition or an isogenic causal result.
  snapshot_sha256: 27a34924777ec7dba67d7c39abd51a1c220aedcccb90bfaf4e8a3bdd5a8bcb59
- evidence_id: primary2020-limits
  kind: primary_source
  reference: PMID:33080784
  locator: Table 5 versus mutation text; compound and causal boundaries
  accessed_at: '2026-10-21T18:30:47.928583Z'
  support: context_only
  summary: The paper contains inconsistent nucleotide-position and residue descriptions
    in surrounding prose; Table 5 labels H349R. Exact nucleotide/allele assertions
    are not imported from that inconsistency. Reagent catalog, purity and enantiomeric
    composition were not specified in the inspected methods. The source supports a
    cautious association follow-up without upgrading the existing native database
    claim.
  snapshot_sha256: 27a34924777ec7dba67d7c39abd51a1c220aedcccb90bfaf4e8a3bdd5a8bcb59
- evidence_id: primary2025
  kind: primary_source
  reference: PMID:41299073; DOI:10.1038/s41564-025-02182-6
  locator: Selected original library, growth-screen Methods/Results and Supplementary
    Data 1–4
  accessed_at: '2026-10-21T18:30:47.930441Z'
  support: supports
  summary: The library screened compounds at 20 µM in mGAM, starting OD600 0.05, 1%
    DMSO, 37 °C and anaerobic conditions, with growth recorded for 24 h in three biological
    replicates. A hit required >20% AUC reduction and adjusted P < 0.05 in at least
    two replicates. This is growth inhibition, not a clinical MIC, bactericidal endpoint
    or bacterial target assay.
  snapshot_sha256: 65b5d6fe9d6c442a6b4eb90ca03e7fe0e45d6f603e81caa1addd7464a6ee1194
- evidence_id: primary2025-material
  kind: primary_source
  reference: https://static-content.springer.com/esm/art%3A10.1038%2Fs41564-025-02182-6/MediaObjects/41564_2025_2182_MOESM3_ESM.xlsx
  locator: SuppData1 rows 604/605; original workbook XML inspected
  accessed_at: '2026-10-21T18:32:21.160534Z'
  support: supports
  summary: Neutral IMAZALIL is item 3_D12, catalog 32007-100MG, CID 37175, with the
    native formula, SMILES, InChI and full key. IMAZALIL SULFATE is a separate item
    12_F10, catalog 33997-100MG-R, CID 173636 and sulfuric-acid-containing formula/key.
    These explicitly distinct preparations are not pooled.
  snapshot_sha256: dcd793f288a84cf7cf1ebe4458bbf0c580e61d8bfb8e916ef470de733651505f
- evidence_id: primary2025-results
  kind: primary_source
  reference: https://static-content.springer.com/esm/art%3A10.1038%2Fs41564-025-02182-6/MediaObjects/41564_2025_2182_MOESM3_ESM.xlsx
  locator: SuppData3 rows 11395/14623/22155 joined to SuppData2 rows 14/17/24
  accessed_at: '2026-10-21T18:32:21.160534Z'
  support: supports
  summary: 'Neutral item 3_D12 has three significant growth-inhibition hits among
    22 tested strains: Coprococcus comes ATCC 27758 (normalized median AUC 0.07229462),
    Eubacterium rectale DSM 17629 (0.06067131) and Roseburia intestinalis DSM 14610
    (0.7672064). The reported adjusted P values are 4.66e-52, 2.35e-14 and 2.61e-5,
    respectively. This directly supports bounded antibacterial activity for the neutral
    library material without assuming activity in all bacteria.'
  snapshot_sha256: dcd793f288a84cf7cf1ebe4458bbf0c580e61d8bfb8e916ef470de733651505f
- evidence_id: primary2025-boundary
  kind: validation
  reference: /private/tmp/am-review-session/548-compact.py
  locator: Raw ZIP/XML extraction and exact compound/strain joins
  accessed_at: '2026-10-21T18:37:44Z'
  support: context_only
  summary: The independent extraction finds 22 neutral imazalil screening rows, exactly
    three significant hits, and no neutral-imazalil rows in SuppData4 validation.
    All 64 imazalil-related validation rows there are sulfate. Consequently, the main-text
    2.5 µM sulfate example is not transferred to neutral imazalil. Other compounds’
    genetic mechanisms are not assigned to this molecule.
  snapshot_sha256: fa04eba09aa60cfb681e23f054061a479262f4cf733cafadbfe7c17d05f641a5
- evidence_id: primary2022
  kind: primary_source
  reference: PMID:36364655; DOI:10.3390/nano12213879
  locator: Full scientific main read; actual Scheme 1 and SI Figure S1 viewed
  accessed_at: '2026-10-21T18:30:47.930133Z'
  support: context_only
  summary: The study distinguishes purchased imazalil from an N-dodecyl quaternary
    imidazolium derivative and its copper-framework formulation. The introduction
    mistakenly describes an anilinopyrimidine, whereas actual Scheme 1 depicts the
    correct neutral imazalil constitution. This source inconsistency is preserved.
    Only the panels explicitly labeled imazalil are considered supporting free-compound
    evidence; derivative/composite potency is not transferred.
  snapshot_sha256: 3fd21e8fb7a26a60372c91a7ebc5cefe4fe3eb794d190aaf67ae889afab83523
- evidence_id: primary2022-si
  kind: primary_source
  reference: https://mdpi-res.com/d_attachment/nanomaterials/nanomaterials-12-03879/article_deploy/nanomaterials-12-03879-s001.zip
  locator: Extracted SI PDF page 2, actual Figure S1 panels a/b/e/f
  accessed_at: '2026-10-21T18:32:09.076620Z'
  support: context_only
  summary: Free-imazalil panels report concentration-dependent growth effects on P.
    syringae pv. lachrymans and X. campestris pv. campestris. P. syringae still grows
    at the highest shown 100 mg/L; X. campestris has a near-flat/declining OD trace
    at 200 mg/L. No exact MIC, killing claim or statistical significance is inferred
    from these qualitative curves. Strain accessions and reagent catalog/purity are
    unresolved.
  snapshot_sha256: 0a1b817b049fd2260992963d3fc2fad380f1306699da414e1dfb82380d697af8
- evidence_id: access
  kind: validation
  reference: /private/tmp/am-review-session/548-fetch1.json
  locator: Public retrieval logs 548-fetch1–7 and successful primary alternatives
  accessed_at: '2026-10-21T18:37:44Z'
  support: context_only
  summary: CAS API returned 401, OLS exact new ARO terms 404 and Europe PMC’s 2018
    XML route 500; the official OBO and PMC HTML supplied the relevant alternative
    records. A guessed supplementary host failed DNS, while the official Springer
    host supplied the workbook. The supplier page request failed HTTP/2; catalog identity
    is read from the original workbook, not claimed independently verified from the
    supplier.
  snapshot_sha256: d3d3c4ab672672b9e9175f821fda3fb9ae546246fdeb0244c56c52bf12b1a878
assessments:
- assessment_id: identity
  area: identity
  topic: Neutral imidazole identity, unspecified stereochemistry and minted identifier
  outcome: supported
  summary: Native formula, charge, masses, encodings and source-derived mint are coherent.
    Current PubChem and ChEMBL agree exactly. One unassigned tetrahedron is preserved;
    it does not by itself establish a racemate, individual enantiomer or sulfate salt.
  target_ids:
  - antibioticmech:aro-c1dea01a87
  evidence_ids:
  - native
  - owners
  - pubchem
  - chembl
  - mapping
  - racemate
- assessment_id: grounding
  area: grounding
  topic: Chemical xrefs, ARO class and additional ChEBI comparators
  outcome: supported
  summary: Asserted accessible molecular links and the current ARO accession/class
    agree with the native record. CAS content remains access-limited. The additional
    neutral ChEBI graph matches, whereas the separately defined racemate requires
    its own material semantics; neither produces a forced reminting finding.
  target_ids:
  - antibioticmech:aro-c1dea01a87
  evidence_ids:
  - pubchem
  - chembl
  - mapping
  - aro
  - chebi-comparator
  - racemate
  - access
- assessment_id: activity
  area: evidence
  topic: Antibacterial eligibility and endpoint/material specificity
  outcome: supported
  summary: The 2025 primary library metadata resolve neutral imazalil and three significant
    bacterial growth-screen results under specified conditions. This supports the
    qualitative antibacterial category despite the molecule’s conventional antifungal
    use. Sulfate dose-validation, quaternary derivatives and formulated-composite
    endpoints are distinct and cannot supply neutral-compound MICs.
  target_ids:
  - antibioticmech:aro-c1dea01a87
  evidence_ids:
  - primary2025
  - primary2025-material
  - primary2025-results
  - primary2025-boundary
  - primary2022
  - primary2022-si
- assessment_id: resistance
  area: evidence
  topic: Already-qualified A. flavus Cyp51C database association
  outcome: unknown
  summary: The native evidence explicitly says database assertion, not primary citation,
    and faithfully reproduces current ARO. The adopted paper studies A. fumigatus
    Cyp51A, while a separate A. flavus study provides a mutation/expression association
    without genetic causal proof. No unsupported upgrade is made and no new finding
    is inferred solely from the existing primary-evidence gap.
  target_ids:
  - antibioticmech:aro-c1dea01a87
  evidence_ids:
  - native
  - aro
  - adopted
  - adopted-alleles
  - primary2020
  - primary2020-limits
  - adapter
- assessment_id: completeness
  area: completeness
  topic: Optional biological detail and all adopted leads
  outcome: unknown
  summary: The sole adopted citation was read beyond its abstract. Optional quantitative
    activity, primary fungal resistance and antifungal-role annotations could be added
    only with exact material, taxon and endpoint qualifiers; their absence is not
    a confirmed defect. No direct bacterial mechanism is established by the inspected
    originals.
  target_ids:
  - antibioticmech:aro-c1dea01a87
  evidence_ids:
  - adopted
  - primary2020
  - primary2025-boundary
  - primary2022
- assessment_id: provenance
  area: provenance
  topic: Actual ARO owners and unchanged native/history
  outcome: supported
  summary: The complete record, source concept and all three seed/reseed history events
    were checked against actual ARO inventories and maintained generator ownership.
    Original 13 and expanded 24 input hashes remain unchanged; no reviewed-status
    promotion or native mutation was performed.
  target_ids:
  - antibioticmech:aro-c1dea01a87
  evidence_ids:
  - native
  - owners
  - search
findings: []
actions:
- action_id: A1
  description: Optional primary enrichment should retain the exact preparation, strain
    and evidence tier.
  finding_ids: []
  target_ids:
  - antibioticmech:aro-c1dea01a87
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/imazalil.yaml
    role: Future validated curator-owned primary activity or resistance annotations
  acceptance_checks:
  - If adding bacterial observations, retain neutral catalog 32007-100MG, 20 µM, mGAM,
    anaerobic 37 °C for 24 h, exact culture accessions and growth-AUC endpoint; do
    not label this screen a MIC or bactericidal experiment.
  - Keep imazalil sulfate, quaternary derivative and composite formulations separate
    from the neutral graph. Do not infer enantiomeric composition from an unspecified
    molecular representation.
  - Keep A. fumigatus Cyp51A recombinant results distinct from A. flavus Cyp51C isolate
    associations. Do not upgrade H349R to a proven causal determinant without independent
    genetic evidence, and adjudicate the source’s inconsistent mutation prose first.
  - If considering additional ChEBI grounding, distinguish neutral CHEBI:83829 from
    explicitly racemic CHEBI:81927 and apply maintained source/mint rules rather than
    changing identifiers from name similarity alone.
limitations:
- The sole adopted original 2018 scientific main and Tables 1/3 were read, but Table
  2 alignment image and figure pixels were not independently inspected. Exact reagent
  lot, purity and stereochemical composition remain unresolved.
- The 2020 original was read selectively for A. flavus material, sequencing/expression,
  susceptibility tables and causal limitations. Source mutation-text discrepancies
  and absent genetic proof prevent a precise causal upgrade of the native database
  association.
- The 2025 study was read selectively for library identity, growth-screen methods/results
  and exact workbook rows. Raw OD traces and all unrelated mechanism experiments were
  not independently reanalysed. Neutral screen hits are not sulfate dose-validation
  or clinical MIC evidence.
- The 2022 scientific main, actual Scheme 1 and actual SI Figure S1 were inspected;
  source introduction chemistry conflicts with its drawing, and strain catalog/purity
  detail is limited. No derivative/composite endpoint or curve-derived MIC is transferred.
- CAS 401, exact OLS term 404 and supplier HTTP/2 access limits remain recorded. Official
  ARO OBO, primary HTML and the final official workbook route supplied successful
  alternatives where stated.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All original 13 and expanded 24 input hashes were rechecked unchanged before draft
  writing. No native/source/history/progress/saved-bundle/Git writes occurred.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
