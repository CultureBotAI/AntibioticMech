# Fasamycin B: exact planar identity and antibacterial evidence supported

- Review: 20261021T160817Z-fasamycin-b-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T15:38:20Z
- Finished UTC: 2026-10-21T16:08:17Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The entire seeded fasamycin B record is consistent with its actual ARO and PubChem inputs. Current authority graphs and the original discovery and mechanism drawings agree on the dichlorinated congener. Exact-compound antibacterial assays and functional FabF evidence support the family-history definition. No confirmed defect was identified. Axial stereochemistry is not encoded, and the newer family-wide stereochemical proposal is kept distinct from a direct assignment of this exact congener. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 427; one complete exact native record. All thirteen initial source-input hashes were verified and retained before assessment. Actual ARO, PubChem and PubChem-enrichment owners were appended, bringing the capture to sixteen unchanged inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-a1068a1a74 | data/antibiotics/antibacterial/fasamycin-b.yaml | generated | fasamycin B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema verification | passed | True | antibioticmech:aro-a1068a1a74 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-a1068a1a74 | Actual focused execution exited 0. |
| Focused chemistry verification | failed | False | antibioticmech:aro-a1068a1a74 | The optional diagnostic exited 1 solely at its fixed average-mass rounding comparison: RDKit calculates 527.356, while native and current PubChem both report 527.3. All graph, formula, charge, exact-mass and minted-ID comparisons pass. The failed output is preserved, not relabeled as a successful execution. |
| Independent exact-authority graph comparison | passed | False | antibioticmech:aro-a1068a1a74 | Native SMILES, native InChI, current PubChem SMILES and current PubChem InChI independently reproduce the complete native key. |
| Authoritative full QC | failed | True | antibioticmech:aro-a1068a1a74 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-a1068a1a74 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-a1068a1a74 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-a1068a1a74 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-a1068a1a74 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-a1068a1a74 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-a1068a1a74 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-a1068a1a74 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-a1068a1a74 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact congener constitution and represented stereochemical scope

identity: supported. Targets: antibioticmech:aro-a1068a1a74.

Native fasamycin B has the correct distinct halogenation pattern, formula and exact PubChem/ARO groundings. Original 2011/2012 drawings and independent encoding comparisons agree. The representation does not assign axial geometry, and no racemate or opposite atropisomer is inferred.

### Antibacterial filing and experimental scope

evidence: supported. Targets: antibioticmech:aro-a1068a1a74.

The exact isolated congener has primary strain-specific Gram-positive MICs, supporting ANTIBACTERIAL and the broader polyketide-antibiotic class. Negative yeast/Gram-negative results retain their assay concentrations and do not become universal inactivity claims.

### Family naming statement and FabF mechanism

evidence: supported. Targets: antibioticmech:aro-a1068a1a74.

The cited 2023 Introduction supports the exact family-history statement, and the original 2012 functional experiments support FabF involvement for this congener with the stated evidence depth. Native does not assert a direct binding relation, affinity, protein accession or causal graph.

### Axial assignment beyond the stored planar graph

identity: unknown. Targets: antibioticmech:aro-a1068a1a74.

The newer Sa proposal is based on measured other congeners plus biosynthetic reasoning. An exact A/B experimental axial assignment was not independently established in this bounded review. This limits full stereochemical sign-off without demonstrating that the stored structure denotes a mixture or an opposite enantiomer.

### Optional activity, mechanism, producer and other biological fields

completeness: supported. Targets: antibioticmech:aro-a1068a1a74.

The record is honestly SEEDED. Exact literature supports optional MIC and functional-target enrichment, but the checklist does not require every optional slot. Heterologous S. albus expression is separate from identifying the original natural producer; no unsupported source organism, clinical status, resistance route or expression dataset is currently asserted.

### Actual source ownership, all adopted leads and history

provenance: supported. Targets: antibioticmech:aro-a1068a1a74.

The sole adopted PMID was read at the stated scope and followed to the original A/B experiments. Every native field, actual source row, classifier, identifier and history event was assessed. The documented source captures remain unchanged, and no native status promotion is implied.

### Average molecular mass precision and independent diagnostic

consistency: unknown. Targets: antibioticmech:aro-a1068a1a74.

The required native gates and exact graph checks pass, but the optional helper flags a 0.056 average-mass difference. Current PubChem repeats 527.3 and the official elemental table permits intervals; no wrong formula or congener follows from this small conventional-weight/rounding boundary. The failure remains explicit.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/fasamycin-b.yaml; Entire native YAML, including every structure property, source concept and curation event. | supports | The MINTED, SEEDED record has one family-history definition citing PMID37327570, ARO3005171 as broader parent and structural class, the neutral C27H20Cl2O7 graph, ARO3007576 and PubChem57404257 exact xrefs, one ARO source concept and three seed/reseed events. No synonym, additional activity role, molecular target, mode enum, numerical activity, resistance determinant, producer object, clinical assertion, expression dataset or causal graph is asserted. |
| owners | data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; scripts/extract_source_inventory.py; scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py; conf/sources.yaml; Complete exact ARO row 463, PubChem row 174, applicable extraction/enrichment and seeding functions. | supports | ARO supplies the label, family definition, cited PMID, classification and PubChem CID. PubChem supplies the structure and properties, retrieved 2026-08-29. The extractor traverses the fasamycin parent to the broader marked drug class ARO3005171; the seeder normalizes the PubChem namespace and mints the exact source identity reproducibly. The source version remains 2026-08-30. The exact-row scan found no ChEBI, imported target, resistance, FDA or MIBiG match by the inspected source IDs or full key. Original capture hashes were preserved; the default ChEBI owner was replaced in target metadata by the actual ARO ownership. |
| aro | ARO:3007576; ARO:3007573; ARO:3005171; https://purl.obolibrary.org/obo/aro.obo; Current official complete ontology fetched; exact term, immediate parent and broader marked drug-class stanzas inspected. | supports | Current ARO names fasamycin B, repeats the native PMID37327570 family-history definition and PubChem57404257, and classifies the individual as an antibiotic. Fasamycin ARO3007573 is its immediate family parent, itself below the broader polyketide-with-antibiotic-activity class ARO3005171. The native broader parent is valid even though it is not the immediate ontology parent. These database assertions are not treated as direct biochemical evidence. |
| pubchem | pubchem.compound:57404257; https://pubchem.ncbi.nlm.nih.gov/compound/57404257; Complete current PUG REST structure/property response and independent parsing of both native and authority encodings. | supports | The current response reproduces the full native SMILES, InChI, key GNOXRTCHZREFRE-UHFFFAOYSA-N, neutral C27H20Cl2O7, charge and masses. Both encodings parse as one connected molecule. Their agreement establishes the represented constitution; Standard InChI and this plain SMILES do not independently establish an atropisomer. There are no drug_xrefs or document_xrefs in this native record. |
| discovery | PMID:21768346; DOI:10.1073/pnas.1103921108; https://pmc.ncbi.nlm.nih.gov/articles/PMC3150919/; Complete original main text read, including Results, full Table 1, isolation/HRMS and bioactivity methods; Figure 2 visually inspected. | supports | The 2011 discovery calls fasamycin A compound 3 and fasamycin B compound 4. Figure 2C distinguishes R=H from R=Cl at the second halogenation position, and Figure 2B supplies NMR correlations for compound 3. Native fasamycin B agrees with the corresponding planar drawing and neutral formula. The X-ray structure in the same figure is unrelated compound 2, not either fasamycin. Heterologous S. albus carrying environmental-DNA cosmid cosAZ154 produces both isolated compounds; the authors explicitly state that metagenomics severs the link to the original source organism. This does not prove a named natural producer. Primary raw spectra in the supplementary PDF were not independently reprocessed. |
| activity | PMID:21768346 Table 1; PMID:22224500 Table 2; DOI:10.1021/ja207662w; https://pmc.ncbi.nlm.nih.gov/articles/PMC3335777/; Complete 2012 main text, complete activity Table 2, MIC methods and visual Figure 1; corresponding 2011 activity table/methods. | supports | Fasamycin B has MIC 6.25 µg/mL against E. faecalis OG1RF and EF16, B. subtilis BR151, and S. aureus 6538P and USA300. The 2012 table reports wild-type E. coli EC100, R. metallidurans CH34, B. thailandensis E264 and S. cerevisiae w303 above 100 µg/mL, while permeabilized E. coli BAS849 has MIC 25 µg/mL. The 2011 table used an upper tested concentration of 50 µg/mL, so its negative values are not conflated with the 2012 thresholds. Assays used serial dilution in LB, 30 °C, and visually absent growth at 24 h in 2012; yeast used YPD. These are strain-specific experimental MICs, not clinical breakpoints, universal species susceptibility or animal efficacy. |
| mechanism | PMID:22224500; DOI:10.1021/ja207662w; All original main Methods and Results read; Figures 3, 5 and 6 visually inspected, including every row of Figure 6b. | supports | Fasamycin B inhibits the S. aureus crude-FASII/recombinant-ACP elongation assay with reported IC50 80 µg/mL. Importantly, visually inspected Figure 6b explicitly includes B: FabF/WT MIC ratio 2.0, versus 1 with FabH. This adds compound-specific functional evidence beyond family membership. The ACP gel in Figure 5, the growth plate in Figure 6a, and the resistant-colony selection are A-specific and are not represented as experiments performed with B. The elongation assay is a multienzyme extract assay, not a purified-FabF binding measurement. Docking into E. coli FabF C163Q models a proposed malonyl-binding-site interaction; no fasamycin co-crystal, measured Kd or covalent binding is demonstrated in this paper. The functional evidence supports FabF involvement while keeping these mechanistic limits. |
| adopted-citation | PMID:37327570; DOI:10.1021/acs.jnatprod.3c00052; https://pmc.ncbi.nlm.nih.gov/articles/PMC10391614/; Complete adopted abstract, Introduction and relevant Results on glycosylated congeners independently read; original reference 3 followed to PMID22224500. | context_only | The native single adopted lead is a primary 2023 heterologous-expression study of other fasamycin congeners. Its Introduction explicitly states the family naming history reproduced in the native definition and cites the original 2012 A/B study. Its own glycosylated congeners lack antibacterial activity under the reported screening conditions; those results do not refute the independently measured aglycone A/B activity. Native wording is family history, not a claim that every congener has direct FabF binding or equal antibacterial activity. This paper was not treated as a new exact-A/B assay. |
| revision-scope | DOI:10.1021/acs.jnatprod.6c00145; https://pmc.ncbi.nlm.nih.gov/articles/PMC13532170/; Introduction, relevant structural-revision Results, axial-configuration discussion and Conclusions read; original PDF page 4 Table 2 visually inspected. | context_only | The 2026 study measures crystals of fasamycins E, L, M and P in Table 2 and proposes Sa axial chirality across the broader family using these and other enzymological/crystallographic observations. A and B are cited for discovery/target history but are not exact A/B crystal assignments in that table. The methoxy regiochemistry revisions concern other congeners; A/B have no methoxy group to relocate. This source therefore does not establish a confirmed constitutional defect in native A/B. Native axial geometry remains unspecified; neither an opposite hand nor a racemic mixture is inferred. The broader Sa proposal is a qualified follow-up lead, not silently promoted to exact-congener proof. |
| adapter | iModulonDB: e_coli/precise1k/b1095; s_aureus/staph_precise108/USA300HOU_RS04880; Complete public dataset catalog and actual FabF search outputs inspected before open-ended mechanism follow-up. | context_only | The adapter resolves E. coli b1095 and S. aureus USA300HOU_RS04880 as FabF genes, with no matching iModulon hits in these queries. E. faecalis is not a covered organism in the inspected catalog. These expression-database results supply nomenclature context only; they do not prove compound binding, the exact assay strain, growth inhibition or a negative biological result. |
| search | 427-inclusive-hits.txt; 426-fetch-results.json through 426-fetch5-results.json; Hidden- and ignored-inclusive local search and bounded public-source follow-up. | context_only | Local search used the exact source ID, minted ID, label, PubChem CID and full-key prefix across data, curation, conf, scripts, src, docs, .claude, reviews and reports. Hits identify the exact source rows, native path, PATHS entry and readiness queue, with no exact curator override or earlier retained review in that bounded surface. Public follow-up used the adopted citation, original 2011 and 2012 studies, current ARO/PubChem and the specific 2026 revision. The EPMC2011 XML route failed, but public PMC HTML supplied the full main text. The linked 2011 supplementary route returned an HTML challenge and the publisher route returned 403, so no supplementary PDF content is claimed. |
| checks | 427-focused-results.json; 427-chemistry.json; 427-authority-chemistry.json; Actual schema, strict, independent chemistry and current-authority calculations; final input-hash recheck. | supports | Schema and strict gates exit 0. Independent native/current-authority encodings and minted IDs agree. The optional chemistry helper exits 1 solely because the average-mass difference of 0.056 exceeds its fixed 0.05 precision tolerance; monoisotopic mass and every graph-identity property pass. All source-input hashes remain unchanged. The current PubChem value is independently confirmed, and the diagnostic is not evidence of a wrong congener. |
| mass-precision | https://ciaaw.org/atomic-weights.htm; pubchem.compound:57404257; Official 2024 standard atomic-weight table entries for C, H, O and Cl; current PubChem response; actual diagnostic output. | context_only | CIAAW represents the average atomic weights of all four constituent elements as intervals. The imported one-decimal value 527.3 is reproduced exactly by current PubChem, while RDKit uses its own conventional atomic weights to calculate 527.356. This near-rounding-boundary difference is retained as a computational precision limitation rather than a confirmed chemical-identity error. No particular isotopic composition or exact PubChem calculation convention was independently measured or reverse-engineered. |

## Limits And Additional Notes

- The original 2011 and 2012 main articles were read completely, but the 2011 structure-elucidation supplementary PDF could not be accessed through the attempted public routes. Original NMR raw spectra and the 2012 mutant-sequence supplement were not independently reanalysed.
- The 2023 paper was read at complete-abstract, Introduction and selected relevant Results depth; its full supplementary glycoside characterization was not audited because it does not directly measure exact A/B.
- The 2026 revision was read in the specified structural and axial-scope sections and its full Table 2 was visually checked. No new calculation of absolute axial configuration, crystallographic refinement or reconstruction of every family congener is claimed. Exact natural-product axial assignment remains unresolved at this review depth.
- Functional FabF evidence is distinguished from a purified direct-binding measurement. Crude FASII IC50 values, growth/MIC changes, resistance selection and docking are not interchangeable assay types, and are not evidence of clinical efficacy.
- The optional independent chemistry helper exited 1 at the average-mass tolerance: 527.356 from RDKit versus 527.3 in both native and current PubChem. This diagnostic is preserved. Exact keys, formula, charge, monoisotopic mass, source mint and all current-authority graph comparisons agree; the precise PubChem average-weight convention was not reconstructed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No confirmed finding or mandatory corrective action is proposed. Optional future curation can add the exact congener MICs and functional FabF evidence on the narrowest supported objects, through the native validated writer and source ownership rules.
- The initial Git base and thirteen original input hashes were preserved. Actual owners were appended before scientific judgment; independent per-record review conclusions remain separate from the neighboring congener.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T160817Z-fasamycin-b-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Fasamycin B: exact planar identity and antibacterial evidence supported'
started_at: '2026-10-21T15:38:20Z'
finished_at: '2026-10-21T16:08:17Z'
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
verdict: blocked
scientific_review: true
summary: The entire seeded fasamycin B record is consistent with its actual ARO and
  PubChem inputs. Current authority graphs and the original discovery and mechanism
  drawings agree on the dichlorinated congener. Exact-compound antibacterial assays
  and functional FabF evidence support the family-history definition. No confirmed
  defect was identified. Axial stereochemistry is not encoded, and the newer family-wide
  stereochemical proposal is kept distinct from a direct assignment of this exact
  congener. Scientific assessment retains the stated evidence limits; full verification
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
  - path: data/antibiotics/antibacterial/fasamycin-b.yaml
    sha256: 871f5af3a1a7755b494006a0bddefca9308012d92922c72ca292c2340179a436
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 25f0d80c0bf26da7741a1514a5e1759dde484ab054f0f56df7938bdda8383a91
    role: context
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/chebi_antimicrobials.tsv
    sha256: 4c33e56c3c342be657309f720f5b5cb9cad1fae13bec202ef99e449503c32004
    role: context
  - path: data/raw/chebi_role_names.tsv
    sha256: 5c476c0aacd7c98d7241d2343a6fc41ee9eb9338077404c5b011a04bf40c6ac5
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: docs/CURATION.md
    sha256: a364598a9c2bdaf9e0e71895d5b7a2fd61d3e726e0ed0da12bd895cc4c30e98c
    role: context
  - path: docs/HARMONIZATION.md
    sha256: fb8b58abca016ca5a7d856fcc6f1ec2deb210e0927394a480853830b39e1f060
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
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
- target_id: antibioticmech:aro-a1068a1a74
  path: data/antibiotics/antibacterial/fasamycin-b.yaml
  label: fasamycin B
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO inventory extraction and classification owner
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
    path: data/raw/pubchem_structures.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Actual maintained source input for the record
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 427; one complete exact native record. All thirteen initial
    source-input hashes were verified and retained before assessment. Actual ARO,
    PubChem and PubChem-enrichment owners were appended, bringing the capture to sixteen
    unchanged inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-a1068a1a74
checks:
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-a1068a1a74
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/fasamycin-b.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-a1068a1a74
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/fasamycin-b.yaml --out /private/tmp/am-review-session/427-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: Focused chemistry verification
  status: failed
  required: false
  summary: 'The optional diagnostic exited 1 solely at its fixed average-mass rounding
    comparison: RDKit calculates 527.356, while native and current PubChem both report
    527.3. All graph, formula, charge, exact-mass and minted-ID comparisons pass.
    The failed output is preserved, not relabeled as a successful execution.'
  target_ids:
  - antibioticmech:aro-a1068a1a74
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 427
  exit_code: 1
  expected_exit_code: 0
- check_id: authority-chemistry
  name: Independent exact-authority graph comparison
  status: passed
  required: false
  summary: Native SMILES, native InChI, current PubChem SMILES and current PubChem
    InChI independently reproduce the complete native key.
  target_ids:
  - antibioticmech:aro-a1068a1a74
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/426427-authority-check.py 427
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
  - antibioticmech:aro-a1068a1a74
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
  - antibioticmech:aro-a1068a1a74
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
  - antibioticmech:aro-a1068a1a74
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
  - antibioticmech:aro-a1068a1a74
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
  - antibioticmech:aro-a1068a1a74
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
  - antibioticmech:aro-a1068a1a74
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
  - antibioticmech:aro-a1068a1a74
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
  - antibioticmech:aro-a1068a1a74
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
  - antibioticmech:aro-a1068a1a74
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/fasamycin-b.yaml
  locator: Entire native YAML, including every structure property, source concept
    and curation event.
  accessed_at: '2026-10-21T16:02:05Z'
  support: supports
  summary: The MINTED, SEEDED record has one family-history definition citing PMID37327570,
    ARO3005171 as broader parent and structural class, the neutral C27H20Cl2O7 graph,
    ARO3007576 and PubChem57404257 exact xrefs, one ARO source concept and three seed/reseed
    events. No synonym, additional activity role, molecular target, mode enum, numerical
    activity, resistance determinant, producer object, clinical assertion, expression
    dataset or causal graph is asserted.
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; scripts/extract_source_inventory.py;
    scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py; conf/sources.yaml
  locator: Complete exact ARO row 463, PubChem row 174, applicable extraction/enrichment
    and seeding functions.
  accessed_at: '2026-10-21T16:02:05Z'
  support: supports
  summary: ARO supplies the label, family definition, cited PMID, classification and
    PubChem CID. PubChem supplies the structure and properties, retrieved 2026-08-29.
    The extractor traverses the fasamycin parent to the broader marked drug class
    ARO3005171; the seeder normalizes the PubChem namespace and mints the exact source
    identity reproducibly. The source version remains 2026-08-30. The exact-row scan
    found no ChEBI, imported target, resistance, FDA or MIBiG match by the inspected
    source IDs or full key. Original capture hashes were preserved; the default ChEBI
    owner was replaced in target metadata by the actual ARO ownership.
  snapshot_sha256: 698d99a0f8b0183bc8c3d54bc67560073ee9d2ca9a9e14ade03f609e1695b232
- evidence_id: aro
  kind: authority
  reference: ARO:3007576; ARO:3007573; ARO:3005171; https://purl.obolibrary.org/obo/aro.obo
  locator: Current official complete ontology fetched; exact term, immediate parent
    and broader marked drug-class stanzas inspected.
  accessed_at: '2026-10-21T15:57:42Z'
  support: supports
  summary: Current ARO names fasamycin B, repeats the native PMID37327570 family-history
    definition and PubChem57404257, and classifies the individual as an antibiotic.
    Fasamycin ARO3007573 is its immediate family parent, itself below the broader
    polyketide-with-antibiotic-activity class ARO3005171. The native broader parent
    is valid even though it is not the immediate ontology parent. These database assertions
    are not treated as direct biochemical evidence.
  snapshot_sha256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
- evidence_id: pubchem
  kind: authority
  reference: pubchem.compound:57404257; https://pubchem.ncbi.nlm.nih.gov/compound/57404257
  locator: Complete current PUG REST structure/property response and independent parsing
    of both native and authority encodings.
  accessed_at: '2026-10-21T15:59:04Z'
  support: supports
  summary: The current response reproduces the full native SMILES, InChI, key GNOXRTCHZREFRE-UHFFFAOYSA-N,
    neutral C27H20Cl2O7, charge and masses. Both encodings parse as one connected
    molecule. Their agreement establishes the represented constitution; Standard InChI
    and this plain SMILES do not independently establish an atropisomer. There are
    no drug_xrefs or document_xrefs in this native record.
  snapshot_sha256: 9f99f42afb33106ade7f2d2c8ba456e638f1b226240f37d924578cacd086f9c6
- evidence_id: discovery
  kind: primary_source
  reference: PMID:21768346; DOI:10.1073/pnas.1103921108; https://pmc.ncbi.nlm.nih.gov/articles/PMC3150919/
  locator: Complete original main text read, including Results, full Table 1, isolation/HRMS
    and bioactivity methods; Figure 2 visually inspected.
  accessed_at: '2026-10-21T15:57:42Z'
  support: supports
  summary: The 2011 discovery calls fasamycin A compound 3 and fasamycin B compound
    4. Figure 2C distinguishes R=H from R=Cl at the second halogenation position,
    and Figure 2B supplies NMR correlations for compound 3. Native fasamycin B agrees
    with the corresponding planar drawing and neutral formula. The X-ray structure
    in the same figure is unrelated compound 2, not either fasamycin. Heterologous
    S. albus carrying environmental-DNA cosmid cosAZ154 produces both isolated compounds;
    the authors explicitly state that metagenomics severs the link to the original
    source organism. This does not prove a named natural producer. Primary raw spectra
    in the supplementary PDF were not independently reprocessed.
  snapshot_sha256: 7c4a1b576310c9b68efac8c99ef666c5d8044156f15792c3201b682e9452b47c
- evidence_id: activity
  kind: primary_source
  reference: PMID:21768346 Table 1; PMID:22224500 Table 2; DOI:10.1021/ja207662w;
    https://pmc.ncbi.nlm.nih.gov/articles/PMC3335777/
  locator: Complete 2012 main text, complete activity Table 2, MIC methods and visual
    Figure 1; corresponding 2011 activity table/methods.
  accessed_at: '2026-10-21T15:50:36.813741Z'
  support: supports
  summary: Fasamycin B has MIC 6.25 µg/mL against E. faecalis OG1RF and EF16, B. subtilis
    BR151, and S. aureus 6538P and USA300. The 2012 table reports wild-type E. coli
    EC100, R. metallidurans CH34, B. thailandensis E264 and S. cerevisiae w303 above
    100 µg/mL, while permeabilized E. coli BAS849 has MIC 25 µg/mL. The 2011 table
    used an upper tested concentration of 50 µg/mL, so its negative values are not
    conflated with the 2012 thresholds. Assays used serial dilution in LB, 30 °C,
    and visually absent growth at 24 h in 2012; yeast used YPD. These are strain-specific
    experimental MICs, not clinical breakpoints, universal species susceptibility
    or animal efficacy.
  snapshot_sha256: 2f8c8c12dbb28d3f9a66043a4cb1d48cc62d84bb0cf2ca1b8f4f4eb52acbb9ad
- evidence_id: mechanism
  kind: primary_source
  reference: PMID:22224500; DOI:10.1021/ja207662w
  locator: All original main Methods and Results read; Figures 3, 5 and 6 visually
    inspected, including every row of Figure 6b.
  accessed_at: '2026-10-21T15:50:36.813741Z'
  support: supports
  summary: 'Fasamycin B inhibits the S. aureus crude-FASII/recombinant-ACP elongation
    assay with reported IC50 80 µg/mL. Importantly, visually inspected Figure 6b explicitly
    includes B: FabF/WT MIC ratio 2.0, versus 1 with FabH. This adds compound-specific
    functional evidence beyond family membership. The ACP gel in Figure 5, the growth
    plate in Figure 6a, and the resistant-colony selection are A-specific and are
    not represented as experiments performed with B. The elongation assay is a multienzyme
    extract assay, not a purified-FabF binding measurement. Docking into E. coli FabF
    C163Q models a proposed malonyl-binding-site interaction; no fasamycin co-crystal,
    measured Kd or covalent binding is demonstrated in this paper. The functional
    evidence supports FabF involvement while keeping these mechanistic limits.'
  snapshot_sha256: 2f8c8c12dbb28d3f9a66043a4cb1d48cc62d84bb0cf2ca1b8f4f4eb52acbb9ad
- evidence_id: adopted-citation
  kind: primary_source
  reference: PMID:37327570; DOI:10.1021/acs.jnatprod.3c00052; https://pmc.ncbi.nlm.nih.gov/articles/PMC10391614/
  locator: Complete adopted abstract, Introduction and relevant Results on glycosylated
    congeners independently read; original reference 3 followed to PMID22224500.
  accessed_at: '2026-10-21T15:49:43.170958Z'
  support: context_only
  summary: The native single adopted lead is a primary 2023 heterologous-expression
    study of other fasamycin congeners. Its Introduction explicitly states the family
    naming history reproduced in the native definition and cites the original 2012
    A/B study. Its own glycosylated congeners lack antibacterial activity under the
    reported screening conditions; those results do not refute the independently measured
    aglycone A/B activity. Native wording is family history, not a claim that every
    congener has direct FabF binding or equal antibacterial activity. This paper was
    not treated as a new exact-A/B assay.
  snapshot_sha256: f6b5f4419134d9a03d48c4d1ac156ce39bd8bf09434d9f18a6da504ec28e23a2
- evidence_id: revision-scope
  kind: primary_source
  reference: DOI:10.1021/acs.jnatprod.6c00145; https://pmc.ncbi.nlm.nih.gov/articles/PMC13532170/
  locator: Introduction, relevant structural-revision Results, axial-configuration
    discussion and Conclusions read; original PDF page 4 Table 2 visually inspected.
  accessed_at: '2026-10-21T15:52:55.182195Z'
  support: context_only
  summary: The 2026 study measures crystals of fasamycins E, L, M and P in Table 2
    and proposes Sa axial chirality across the broader family using these and other
    enzymological/crystallographic observations. A and B are cited for discovery/target
    history but are not exact A/B crystal assignments in that table. The methoxy regiochemistry
    revisions concern other congeners; A/B have no methoxy group to relocate. This
    source therefore does not establish a confirmed constitutional defect in native
    A/B. Native axial geometry remains unspecified; neither an opposite hand nor a
    racemic mixture is inferred. The broader Sa proposal is a qualified follow-up
    lead, not silently promoted to exact-congener proof.
  snapshot_sha256: 90857b1e07c581a6d6e7d070379cc74778d702d35fd0648b30ff8a2589c575d7
- evidence_id: adapter
  kind: database
  reference: 'iModulonDB: e_coli/precise1k/b1095; s_aureus/staph_precise108/USA300HOU_RS04880'
  locator: Complete public dataset catalog and actual FabF search outputs inspected
    before open-ended mechanism follow-up.
  accessed_at: '2026-10-21T16:02:05Z'
  support: context_only
  summary: The adapter resolves E. coli b1095 and S. aureus USA300HOU_RS04880 as FabF
    genes, with no matching iModulon hits in these queries. E. faecalis is not a covered
    organism in the inspected catalog. These expression-database results supply nomenclature
    context only; they do not prove compound binding, the exact assay strain, growth
    inhibition or a negative biological result.
  snapshot_sha256: 9208915c33e73f36e3e38af2ad6d5c8c27b46d44a93a7304e4c37b6ee1bcc34a
- evidence_id: search
  kind: search
  reference: 427-inclusive-hits.txt; 426-fetch-results.json through 426-fetch5-results.json
  locator: Hidden- and ignored-inclusive local search and bounded public-source follow-up.
  accessed_at: '2026-10-21T16:02:05Z'
  support: context_only
  summary: Local search used the exact source ID, minted ID, label, PubChem CID and
    full-key prefix across data, curation, conf, scripts, src, docs, .claude, reviews
    and reports. Hits identify the exact source rows, native path, PATHS entry and
    readiness queue, with no exact curator override or earlier retained review in
    that bounded surface. Public follow-up used the adopted citation, original 2011
    and 2012 studies, current ARO/PubChem and the specific 2026 revision. The EPMC2011
    XML route failed, but public PMC HTML supplied the full main text. The linked
    2011 supplementary route returned an HTML challenge and the publisher route returned
    403, so no supplementary PDF content is claimed.
  search_scope: 2026-10-21, rg --no-ignore --hidden for ARO:3007576, fasamycin B,
    GNOXRTCHZREFRE, 57404257 and the minted identifier across the stated local paths.
    Exact-name/DOI web queries searched fasamycin A/B discovery, FabF and axial stereochemistry.
    Search results were leads only; inspected originals support the conclusions.
  snapshot_sha256: 0e8dc7629c479e1d19b5efd5039fa90c4ada77d088f54570452dfe1bde2e7a0b
- evidence_id: checks
  kind: validation
  reference: 427-focused-results.json; 427-chemistry.json; 427-authority-chemistry.json
  locator: Actual schema, strict, independent chemistry and current-authority calculations;
    final input-hash recheck.
  accessed_at: '2026-10-21T16:02:05Z'
  support: supports
  summary: Schema and strict gates exit 0. Independent native/current-authority encodings
    and minted IDs agree. The optional chemistry helper exits 1 solely because the
    average-mass difference of 0.056 exceeds its fixed 0.05 precision tolerance; monoisotopic
    mass and every graph-identity property pass. All source-input hashes remain unchanged.
    The current PubChem value is independently confirmed, and the diagnostic is not
    evidence of a wrong congener.
  snapshot_sha256: 0d79b72a94826b8e2984362a574145891b33f343bb4b38b48b5b8539a5cb4c35
- evidence_id: mass-precision
  kind: authority
  reference: https://ciaaw.org/atomic-weights.htm; pubchem.compound:57404257
  locator: Official 2024 standard atomic-weight table entries for C, H, O and Cl;
    current PubChem response; actual diagnostic output.
  accessed_at: '2026-10-21T16:01:46Z'
  support: context_only
  summary: CIAAW represents the average atomic weights of all four constituent elements
    as intervals. The imported one-decimal value 527.3 is reproduced exactly by current
    PubChem, while RDKit uses its own conventional atomic weights to calculate 527.356.
    This near-rounding-boundary difference is retained as a computational precision
    limitation rather than a confirmed chemical-identity error. No particular isotopic
    composition or exact PubChem calculation convention was independently measured
    or reverse-engineered.
  snapshot_sha256: b48282594b1fb01eee3cbc9d469ce5e3483b628157ea1b09ede33e3476895cf2
assessments:
- assessment_id: identity
  area: identity
  topic: Exact congener constitution and represented stereochemical scope
  outcome: supported
  summary: Native fasamycin B has the correct distinct halogenation pattern, formula
    and exact PubChem/ARO groundings. Original 2011/2012 drawings and independent
    encoding comparisons agree. The representation does not assign axial geometry,
    and no racemate or opposite atropisomer is inferred.
  target_ids:
  - antibioticmech:aro-a1068a1a74
  evidence_ids:
  - native
  - pubchem
  - aro
  - discovery
  - revision-scope
  - checks
- assessment_id: activity
  area: evidence
  topic: Antibacterial filing and experimental scope
  outcome: supported
  summary: The exact isolated congener has primary strain-specific Gram-positive MICs,
    supporting ANTIBACTERIAL and the broader polyketide-antibiotic class. Negative
    yeast/Gram-negative results retain their assay concentrations and do not become
    universal inactivity claims.
  target_ids:
  - antibioticmech:aro-a1068a1a74
  evidence_ids:
  - activity
  - discovery
  - aro
- assessment_id: definition
  area: evidence
  topic: Family naming statement and FabF mechanism
  outcome: supported
  summary: The cited 2023 Introduction supports the exact family-history statement,
    and the original 2012 functional experiments support FabF involvement for this
    congener with the stated evidence depth. Native does not assert a direct binding
    relation, affinity, protein accession or causal graph.
  target_ids:
  - antibioticmech:aro-a1068a1a74
  evidence_ids:
  - adopted-citation
  - mechanism
  - adapter
- assessment_id: stereo
  area: identity
  topic: Axial assignment beyond the stored planar graph
  outcome: unknown
  summary: The newer Sa proposal is based on measured other congeners plus biosynthetic
    reasoning. An exact A/B experimental axial assignment was not independently established
    in this bounded review. This limits full stereochemical sign-off without demonstrating
    that the stored structure denotes a mixture or an opposite enantiomer.
  target_ids:
  - antibioticmech:aro-a1068a1a74
  evidence_ids:
  - pubchem
  - discovery
  - revision-scope
- assessment_id: completeness
  area: completeness
  topic: Optional activity, mechanism, producer and other biological fields
  outcome: supported
  summary: The record is honestly SEEDED. Exact literature supports optional MIC and
    functional-target enrichment, but the checklist does not require every optional
    slot. Heterologous S. albus expression is separate from identifying the original
    natural producer; no unsupported source organism, clinical status, resistance
    route or expression dataset is currently asserted.
  target_ids:
  - antibioticmech:aro-a1068a1a74
  evidence_ids:
  - native
  - discovery
  - mechanism
  - adopted-citation
- assessment_id: provenance
  area: provenance
  topic: Actual source ownership, all adopted leads and history
  outcome: supported
  summary: The sole adopted PMID was read at the stated scope and followed to the
    original A/B experiments. Every native field, actual source row, classifier, identifier
    and history event was assessed. The documented source captures remain unchanged,
    and no native status promotion is implied.
  target_ids:
  - antibioticmech:aro-a1068a1a74
  evidence_ids:
  - owners
  - native
  - aro
  - search
  - checks
- assessment_id: mass-precision
  area: consistency
  topic: Average molecular mass precision and independent diagnostic
  outcome: unknown
  summary: The required native gates and exact graph checks pass, but the optional
    helper flags a 0.056 average-mass difference. Current PubChem repeats 527.3 and
    the official elemental table permits intervals; no wrong formula or congener follows
    from this small conventional-weight/rounding boundary. The failure remains explicit.
  target_ids:
  - antibioticmech:aro-a1068a1a74
  evidence_ids:
  - pubchem
  - checks
  - mass-precision
findings: []
actions: []
limitations:
- The original 2011 and 2012 main articles were read completely, but the 2011 structure-elucidation
  supplementary PDF could not be accessed through the attempted public routes. Original
  NMR raw spectra and the 2012 mutant-sequence supplement were not independently reanalysed.
- The 2023 paper was read at complete-abstract, Introduction and selected relevant
  Results depth; its full supplementary glycoside characterization was not audited
  because it does not directly measure exact A/B.
- The 2026 revision was read in the specified structural and axial-scope sections
  and its full Table 2 was visually checked. No new calculation of absolute axial
  configuration, crystallographic refinement or reconstruction of every family congener
  is claimed. Exact natural-product axial assignment remains unresolved at this review
  depth.
- Functional FabF evidence is distinguished from a purified direct-binding measurement.
  Crude FASII IC50 values, growth/MIC changes, resistance selection and docking are
  not interchangeable assay types, and are not evidence of clinical efficacy.
- 'The optional independent chemistry helper exited 1 at the average-mass tolerance:
  527.356 from RDKit versus 527.3 in both native and current PubChem. This diagnostic
  is preserved. Exact keys, formula, charge, monoisotopic mass, source mint and all
  current-authority graph comparisons agree; the precise PubChem average-weight convention
  was not reconstructed.'
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No confirmed finding or mandatory corrective action is proposed. Optional future
  curation can add the exact congener MICs and functional FabF evidence on the narrowest
  supported objects, through the native validated writer and source ownership rules.
- The initial Git base and thirteen original input hashes were preserved. Actual owners
  were appended before scientific judgment; independent per-record review conclusions
  remain separate from the neighboring congener.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
