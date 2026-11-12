# IP-antibiotic 3: exact structure, gonococcal activity and bounded follow-up evidence

- Review: 20261021T185908Z-ip-antibiotic-3-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T18:21:54Z
- Finished UTC: 2026-10-21T18:59:08Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact acetamide graph matches original compound3 and its supplementary characterization. The WHO Z MIC and reported tested-panel range are supported, as are the native rapid-killing statement. One minor defect is confirmed: a faithful curator summary occupies the verbatim snippet field. Proteomic responses and limited passage experiments do not establish direct targets or universal resistance protection.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position 557; exact whole record. Original thirteen captured inputs retained; actual curator-table ownership replaces the generic initial ChEBI owner annotation.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:curator-e8d0b1491b | data/antibiotics/antibacterial/ip-antibiotic-3.yaml | generated | IP-antibiotic 3 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:curator-e8d0b1491b | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:curator-e8d0b1491b | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:curator-e8d0b1491b | Actual focused execution exited 0. |
| Independent original-drawing reconstruction | passed | False | antibioticmech:curator-e8d0b1491b | Independent Table1 graph and exact-key ignored-inclusive owner search passed; native structure remained unchanged. |
| Structured-source applicability | not_applicable | False | antibioticmech:curator-e8d0b1491b | No native gene, regulator, target, pathway or transcriptomic assertion is present. Optional source proteomics is assessed as response evidence, without creating a molecular-target claim. |
| Authoritative full QC | failed | True | antibioticmech:curator-e8d0b1491b | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:curator-e8d0b1491b | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:curator-e8d0b1491b | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:curator-e8d0b1491b | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:curator-e8d0b1491b | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:curator-e8d0b1491b | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:curator-e8d0b1491b | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:curator-e8d0b1491b | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:curator-e8d0b1491b | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral numbered amide

identity: supported. Targets: antibioticmech:curator-e8d0b1491b.

Independent graph reconstruction, exact primary drawings, systematic name and supplementary material support the native identity and masses.

### Native WHO Z and tested-panel summary

evidence: supported. Targets: antibioticmech:curator-e8d0b1491b.

The stated WHO Z value and tested-panel range agree with the original table/prose. Exact strain values cannot be reconstructed from a reported range alone.

### Native rapid-killing activity

evidence: supported. Targets: antibioticmech:curator-e8d0b1491b.

The actual source figure and corresponding assay Methods support the native qualitative follow-up statement without equating plotted floor or relative-survival reduction with guaranteed eradication.

### Paraphrase stored as snippet

evidence: concern. Targets: antibioticmech:curator-e8d0b1491b.

The factual summary is supported but is not a verbatim quotation; move it into notes while retaining the existing structural explanation.

### Mechanism, resistance and safety boundaries

completeness: supported. Targets: antibioticmech:curator-e8d0b1491b.

No missing optional object is itself a defect. Protein-abundance changes do not prove direct targets,30-day passage does not rule out future resistance, and cell-line effects do not establish clinical safety.

### Mint, source owner and proposed status

provenance: supported. Targets: antibioticmech:curator-e8d0b1491b.

Exact DOI fragment and maintained curator row resolve the compound. Thirteen original input hashes, deterministic mint and single proposed-history event are consistent.

## Findings

### F1: Move the supported curator summary out of the verbatim snippet field

minor / open / confirmed; issue key: ip-antibiotic-3-paraphrase-in-source-snippet.

The maintained evidence_snippet combines table results and follow-up experiments in third-person curator wording. The source supports the factual claims, but this is not a verbatim passage. Use notes for the summary and preserve exact assay boundaries.

## Recommended Actions And Acceptance Checks

### A1

Correct the exact curator-row evidence placement and regenerate reproducibly.

- Move the summary for source DOI:10.1021/acsinfecdis.5c00812#3 from evidence_snippet into evidence_notes, preserving the original structure notes, DOI and experimental scopes.
- Retain native keyWHUQFDQKVSTVHC-UHFFFAOYSA-N, formula, charge, masses, source version and compound numbering.
- Keep WHO Z MIC distinct from the panel-level range; retain relative-survival/viable-count context for follow-up claims. A replacement snippet must be short exact primary text.
- Pass focused schema/strict and reproducibility checks without hand-editing generated YAML or rewriting native history.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/ip-antibiotic-3.yaml; Entire native YAML, definition, sole source-local alias, role, structure, source evidence and single history event. | supports | The MINTED/PROPOSED record denotes neutral compound3, a5,7-dichloro-8-hydroxyquinoline acetamide, keyWHUQFDQKVSTVHC-UHFFFAOYSA-N. It has no xrefs, parent classes, target, resistance, clinical, producer or structured activity object. The source snippet includes preliminary WHO Z MIC and the reported gonococcal-panel range, plus a bounded follow-up activity statement. |
| owners | curation/curator_antibiotics.tsv:4; scripts/seed_from_sources.py:618; scripts/seed_from_sources.py:686; Exact source row matched by full source_id equality; curator loader and build logic read. | supports | The maintained DOI:10.1021/acsinfecdis.5c00812#3 row owns structure, definition, source-local alias and source evidence. The loader copies evidence_snippet into native snippet and evidence_notes into notes. The deterministic mint, publication/structure source, retrieval/version dates and single PROPOSED_FROM_CURATOR_INVENTORY event agree. All thirteen original hashes remain unchanged. |
| chemistry | 557-chemistry.json;557-authority-chemistry.json;IP23-structure-check.py; Native chemistry and independent reconstruction from actual Table1/Scheme1. | supports | Native SMILES and InChI agree on formula, zero charge, a single molecule, masses and keyWHUQFDQKVSTVHC-UHFFFAOYSA-N. An independently encoded alternate graph from the original drawing matches reciprocally. The source compound is the acetamide, not the precursor, another amide or a salt inferred from its mass-spectral ion. |
| authority | https://pubchem.ncbi.nlm.nih.gov/compound/165348096; Official exact-key lookup and independent SMILES/InChI parsing. | supports | Current PubChem CID165348096 agrees with the exact neutral acetamide structure and systematic name. The additional corroboration is not a native asserted xref. |
| primary | PMID:41405126; DOI:10.1021/acsinfecdis.5c00812; https://pmc.ncbi.nlm.nih.gov/articles/PMC12797230/; Entire original main text, all four tables and captions; actual Scheme1/Table1 and Figures1/2 inspected. | supports | The study synthesizes twelve analogues, screens WHO Z and selects compounds2/3 for further tests. The named amides and drawings establish exact compound numbering. Methods provide synthesis/NMR/HRMS, broth MIC, time-kill, cervical-cell, cytotoxicity and SWATH-MS protocols. Primary results are distinguished from authors mechanistic and clinical extrapolations. |
| material | DOI:10.1021/acsinfecdis.5c00812.s001; https://ndownloader.figshare.com/files/60451332; Actual original supplementaryS6–S7, exact main characterization subsection and verified publisher Figshare metadata. | supports | The published proton/carbon spectra depict compound3; the negative-mode HRMS observed ion is268.9889. The main reports greater than95% purity by NMR, which was not independently recalculated from raw instrument data. The acetamide methyl, drawing and HRMS support the native C11 formula. The main HRMS sentence mistakenly repeats the C13 formula from compound2, but the drawing, stated mass and independently recomputed native formula agree; the source typo is not copied into the record. The ionized MS species is not the native formal charge. |
| mic | PMID:41405126; actual Table1 and MIC Determination Methods; Exact compound cell; complete media and susceptibility methods; corresponding panel-results paragraph. | supports | Table1 reports compound3 MIC0.078mg/L against MDR N.gonorrhoeae WHO Z. GC medium includes1% IsoVitaleX; approximately5×10^5CFU/mL adjusted inoculum,100µL suspension, serial drug dilutions and overnight37°C growth are specified. No visible turbidity defines MIC, with three experiments in triplicate. The result paragraph reports0.078–0.156mg/L for compounds2/3 across ATCC49226, MS11 and13 WHO MDR strains. That range is supported as the authors panel-level summary; individual strain-resolved values were not supplied in the inspected main tables. No added zinc is specified for this monotherapy assay. |
| kill | PMID:41405126; Figure1A and Bacterial Time-Kill Assays; Actual graph, caption, stated concentrations and corresponding Methods. | supports | WHO Z at approximately5×10^5CFU/mL was sampled at0,3,6,24h and plated for viable counts. Compound2 at0.156mg/L and compound3 at0.078mg/L reach the plotted lower boundary by3h, supporting rapid killing. A plotted zero is not proof of absolute sterilization because a formal detection limit is unstated. The actual panel shows the two analogues and control; caption/prose references to PBT2 are not treated as an independently displayed PBT2 curve. |
| cervical | PMID:41405126; Figure1C/D and Ex Vivo Treatment Assay; Actual bar plots and complete treatment/viable-count Methods. | supports | Primary human cervical epithelial cultures were infected with WHO Z for90min, washed and treated for24h with compound2 at0.078–2.34mg/L or compound3 at0.039–1.17mg/L, with0.1%DMSO vehicle and0.5mg/L ceftriaxone. Lysate plating quantifies viable bacteria relative to vehicle; three independent occasions each used triplicates. The plots support dose-related survival reduction, not a human clinical cure or universal complete eradication. Compound2 highest-dose bar is around12% survival despite a prose claim of at most10%; the native qualitative dose-dependent statement does not inherit that precise discrepancy. |
| resistance | PMID:41405126; Figure1B and associated results; Actual30-day plot and complete caption/results paragraph. | supports | The two analogue series show no rising MIC over30 serial-exposure days in WHO Z, unlike the kanamycin comparator. Exact serial-passage transfer details are not reported in the inspected Methods. The plot baseline for compound3 appears near0.156mg/L while Table1 gives0.078mg/L; no absolute passage-series value is imported. Absence of detected MIC increase in this experiment cannot establish that resistance cannot evolve or identify a resistance determinant. |
| proteomics | PMID:41405126; Figure2; SI TableS1 pagesS26–S29; Complete source SWATH-MS Methods/results, actual Figure2 and all extracted TableS1 rows. | supports | Subinhibitory exposures are PBT2 at0.156, compound2 at0.078 and compound3 at0.039mg/L. Protein-abundance responses include increased iron-transport-associated and decreased phosphate-associated proteins. TableS1 is response proteomics; its listed proteins are not direct binding targets. The main Methods uses greater-than30% abundance change with adjustedP&lt;0.05, whereas the displayed result selection describes absolute log2FC at least1. No new target, regulatory mechanism, publicly deposited raw dataset or direct metal-flux measurement is inferred from these differences. |
| host-and-spectrum | PMID:41405126; Tables2–4; Complete original tables and corresponding Methods/results. | supports | HEK293S viability IC50 is higher for compounds2/3 than PBT2, but L1210 IC50 is lower, so reduced toxicity is not universal across the two cell lines. Meningococcal and NTHi growth results are strain-specific; NTHi Table4 includes0.156 and2.5mg/L endpoints outside its simplified prose range. These optional results are not native claims and are not copied as broad safety or species-level potency conclusions. |
| role | CHEBI:33282; Current official antibacterial-agent definition. | supports | The exact growth and viable-count experiments support antibacterial filing. A clinical indication or experimentally resolved molecular target is not required for this qualitative role. |
| snippet | .claude/skills/curate-yaml-record/references/review-checklist.md:14; Entire native/source snippet versus complete original text and relevant quantitative primary evidence. | supports | The third-person Jen-and-colleagues wording combines results from a table and prose/figures into a curator summary. Its material statements are supported at their stated scope, but it is not a verbatim passage. The checklist requires summaries and interpretation to be placed in notes. |
| search | 557-local-hits.txt;557-owner-hits.txt;557-authority-chemistry.json;056-root-fetch1.json through056-root-fetch6.json; Hidden/ignored-inclusive local searches, direct DOI/PMC and exact-key authority requests, verified publisher supplement retrieval. | context_only | Exact-key searches in data/curation/conf YAML/TSV/JSON returned only the target record and curator table. Original supplement routes returned challenge HTML or403; the public publisher Figshare API resolved the same DOI and supplied the original PDF. Discovery was bounded to the named primary and authority checks, not a comprehensive later-literature survey. |

## Limits And Additional Notes

- Entire main and actual Scheme1/Table1/Figures1/2 were read. Supplement inspection covered actualS6–S7 and extracted TableS1 text; other analogue spectra were not independently reanalysed for this target.
- Raw instrument data, assay replicates and purity were not independently reprocessed. The MIC Methods gives overnight incubation and approximate inoculum, so exact unreported duration or solvent composition is not invented.
- The main reports a tested-gonococcal panel range without individual values in its tables. Passage transfer details and a formal killing-assay detection limit are unstated. Plot/prose differences are retained rather than silently resolved.
- Proteomic response and compound-family design do not establish a direct antibacterial protein target. Source cytotoxicity and additional-species summary discrepancies limit broad extrapolation but are not defects in unasserted native claims.
- No exhaustive later-literature or registry search was undertaken. The review remains a bounded scientific assessment of the exact native record.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Native/source/history/status remain unchanged; all original thirteen hashes were preserved. Actual curator-table owner annotations replace the generic initial ChEBI owner description.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T185908Z-ip-antibiotic-3-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'IP-antibiotic 3: exact structure, gonococcal activity and bounded follow-up
  evidence'
started_at: '2026-10-21T18:21:54Z'
finished_at: '2026-10-21T18:59:08Z'
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
verdict: needs_curation
scientific_review: true
summary: 'The exact acetamide graph matches original compound3 and its supplementary
  characterization. The WHO Z MIC and reported tested-panel range are supported, as
  are the native rapid-killing statement. One minor defect is confirmed: a faithful
  curator summary occupies the verbatim snippet field. Proteomic responses and limited
  passage experiments do not establish direct targets or universal resistance protection.'
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
  - path: data/antibiotics/antibacterial/ip-antibiotic-3.yaml
    sha256: e96d752dfc152f36fe7fff989ae778f6f3ae5f716e6e6bad8020716d22275c04
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
targets:
- target_id: antibioticmech:curator-e8d0b1491b
  path: data/antibiotics/antibacterial/ip-antibiotic-3.yaml
  label: IP-antibiotic 3
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Exact publication-derived structure, definition and source evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Curator-inventory loading and generated evidence
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Optional grounding adjudication
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position 557; exact whole record. Original
    thirteen captured inputs retained; actual curator-table ownership replaces the
    generic initial ChEBI owner annotation.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:curator-e8d0b1491b
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-e8d0b1491b
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    557
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-e8d0b1491b
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/ip-antibiotic-3.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-e8d0b1491b
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/ip-antibiotic-3.yaml --out /private/tmp/am-review-session/557-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: primary-graph
  name: Independent original-drawing reconstruction
  status: passed
  required: false
  summary: Independent Table1 graph and exact-key ignored-inclusive owner search passed;
    native structure remained unchanged.
  target_ids:
  - antibioticmech:curator-e8d0b1491b
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/IP23-structure-check.py
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter
  name: Structured-source applicability
  status: not_applicable
  required: false
  summary: No native gene, regulator, target, pathway or transcriptomic assertion
    is present. Optional source proteomics is assessed as response evidence, without
    creating a molecular-target claim.
  target_ids:
  - antibioticmech:curator-e8d0b1491b
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:curator-e8d0b1491b
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
  - antibioticmech:curator-e8d0b1491b
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
  - antibioticmech:curator-e8d0b1491b
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
  - antibioticmech:curator-e8d0b1491b
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
  - antibioticmech:curator-e8d0b1491b
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
  - antibioticmech:curator-e8d0b1491b
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
  - antibioticmech:curator-e8d0b1491b
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
  - antibioticmech:curator-e8d0b1491b
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
  - antibioticmech:curator-e8d0b1491b
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/ip-antibiotic-3.yaml
  locator: Entire native YAML, definition, sole source-local alias, role, structure,
    source evidence and single history event.
  accessed_at: '2026-10-21T18:36:06Z'
  support: supports
  summary: The MINTED/PROPOSED record denotes neutral compound3, a5,7-dichloro-8-hydroxyquinoline
    acetamide, keyWHUQFDQKVSTVHC-UHFFFAOYSA-N. It has no xrefs, parent classes, target,
    resistance, clinical, producer or structured activity object. The source snippet
    includes preliminary WHO Z MIC and the reported gonococcal-panel range, plus a
    bounded follow-up activity statement.
- evidence_id: owners
  kind: record_content
  reference: curation/curator_antibiotics.tsv:4; scripts/seed_from_sources.py:618;
    scripts/seed_from_sources.py:686
  locator: Exact source row matched by full source_id equality; curator loader and
    build logic read.
  accessed_at: '2026-10-21T18:36:06Z'
  support: supports
  summary: The maintained DOI:10.1021/acsinfecdis.5c00812#3 row owns structure, definition,
    source-local alias and source evidence. The loader copies evidence_snippet into
    native snippet and evidence_notes into notes. The deterministic mint, publication/structure
    source, retrieval/version dates and single PROPOSED_FROM_CURATOR_INVENTORY event
    agree. All thirteen original hashes remain unchanged.
  snapshot_sha256: 041a53e0a964a0b7c70cdd4e91c58f4a11d18d46c2f3fada6356db4f40670bba
- evidence_id: chemistry
  kind: validation
  reference: 557-chemistry.json;557-authority-chemistry.json;IP23-structure-check.py
  locator: Native chemistry and independent reconstruction from actual Table1/Scheme1.
  accessed_at: '2026-10-21T18:36:06Z'
  support: supports
  summary: Native SMILES and InChI agree on formula, zero charge, a single molecule,
    masses and keyWHUQFDQKVSTVHC-UHFFFAOYSA-N. An independently encoded alternate
    graph from the original drawing matches reciprocally. The source compound is the
    acetamide, not the precursor, another amide or a salt inferred from its mass-spectral
    ion.
  snapshot_sha256: 87c4cb33d03d9dd20f1b33af5fcc41620ca47d26f2403e7f3564b824d631c9e7
- evidence_id: authority
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/165348096
  locator: Official exact-key lookup and independent SMILES/InChI parsing.
  accessed_at: '2026-10-21T18:36:06Z'
  support: supports
  summary: Current PubChem CID165348096 agrees with the exact neutral acetamide structure
    and systematic name. The additional corroboration is not a native asserted xref.
  snapshot_sha256: 59025f06234f02aa65dda0a3f71285ac4529948bf7e1e8983fc40037a20e84d2
- evidence_id: primary
  kind: primary_source
  reference: PMID:41405126; DOI:10.1021/acsinfecdis.5c00812; https://pmc.ncbi.nlm.nih.gov/articles/PMC12797230/
  locator: Entire original main text, all four tables and captions; actual Scheme1/Table1
    and Figures1/2 inspected.
  accessed_at: '2026-10-21T18:36:06Z'
  support: supports
  summary: The study synthesizes twelve analogues, screens WHO Z and selects compounds2/3
    for further tests. The named amides and drawings establish exact compound numbering.
    Methods provide synthesis/NMR/HRMS, broth MIC, time-kill, cervical-cell, cytotoxicity
    and SWATH-MS protocols. Primary results are distinguished from authors mechanistic
    and clinical extrapolations.
  snapshot_sha256: 2a99c3f72244f2e8a63dd207e623081cb3e00101c49502b9043ce4ff4b584fab
- evidence_id: material
  kind: primary_source
  reference: DOI:10.1021/acsinfecdis.5c00812.s001; https://ndownloader.figshare.com/files/60451332
  locator: Actual original supplementaryS6–S7, exact main characterization subsection
    and verified publisher Figshare metadata.
  accessed_at: '2026-10-21T18:36:06Z'
  support: supports
  summary: The published proton/carbon spectra depict compound3; the negative-mode
    HRMS observed ion is268.9889. The main reports greater than95% purity by NMR,
    which was not independently recalculated from raw instrument data. The acetamide
    methyl, drawing and HRMS support the native C11 formula. The main HRMS sentence
    mistakenly repeats the C13 formula from compound2, but the drawing, stated mass
    and independently recomputed native formula agree; the source typo is not copied
    into the record. The ionized MS species is not the native formal charge.
  snapshot_sha256: 1b130403095d4518fbc3a59edf57c3ed7753d47b6beb2f16c21d46c6efe583b8
- evidence_id: mic
  kind: primary_source
  reference: PMID:41405126; actual Table1 and MIC Determination Methods
  locator: Exact compound cell; complete media and susceptibility methods; corresponding
    panel-results paragraph.
  accessed_at: '2026-10-21T18:36:06Z'
  support: supports
  summary: Table1 reports compound3 MIC0.078mg/L against MDR N.gonorrhoeae WHO Z.
    GC medium includes1% IsoVitaleX; approximately5×10^5CFU/mL adjusted inoculum,100µL
    suspension, serial drug dilutions and overnight37°C growth are specified. No visible
    turbidity defines MIC, with three experiments in triplicate. The result paragraph
    reports0.078–0.156mg/L for compounds2/3 across ATCC49226, MS11 and13 WHO MDR strains.
    That range is supported as the authors panel-level summary; individual strain-resolved
    values were not supplied in the inspected main tables. No added zinc is specified
    for this monotherapy assay.
  snapshot_sha256: 67e867b42477bf51aa785476377153818c3e9d95041fa4d8e8acdf9e84fd7ff0
- evidence_id: kill
  kind: primary_source
  reference: PMID:41405126; Figure1A and Bacterial Time-Kill Assays
  locator: Actual graph, caption, stated concentrations and corresponding Methods.
  accessed_at: '2026-10-21T18:36:06Z'
  support: supports
  summary: WHO Z at approximately5×10^5CFU/mL was sampled at0,3,6,24h and plated for
    viable counts. Compound2 at0.156mg/L and compound3 at0.078mg/L reach the plotted
    lower boundary by3h, supporting rapid killing. A plotted zero is not proof of
    absolute sterilization because a formal detection limit is unstated. The actual
    panel shows the two analogues and control; caption/prose references to PBT2 are
    not treated as an independently displayed PBT2 curve.
  snapshot_sha256: dcf8239a6e6628d784a488de975a886e0521cbb59d061b2e829e965230898609
- evidence_id: cervical
  kind: primary_source
  reference: PMID:41405126; Figure1C/D and Ex Vivo Treatment Assay
  locator: Actual bar plots and complete treatment/viable-count Methods.
  accessed_at: '2026-10-21T18:36:06Z'
  support: supports
  summary: Primary human cervical epithelial cultures were infected with WHO Z for90min,
    washed and treated for24h with compound2 at0.078–2.34mg/L or compound3 at0.039–1.17mg/L,
    with0.1%DMSO vehicle and0.5mg/L ceftriaxone. Lysate plating quantifies viable
    bacteria relative to vehicle; three independent occasions each used triplicates.
    The plots support dose-related survival reduction, not a human clinical cure or
    universal complete eradication. Compound2 highest-dose bar is around12% survival
    despite a prose claim of at most10%; the native qualitative dose-dependent statement
    does not inherit that precise discrepancy.
  snapshot_sha256: dcf8239a6e6628d784a488de975a886e0521cbb59d061b2e829e965230898609
- evidence_id: resistance
  kind: primary_source
  reference: PMID:41405126; Figure1B and associated results
  locator: Actual30-day plot and complete caption/results paragraph.
  accessed_at: '2026-10-21T18:36:06Z'
  support: supports
  summary: The two analogue series show no rising MIC over30 serial-exposure days
    in WHO Z, unlike the kanamycin comparator. Exact serial-passage transfer details
    are not reported in the inspected Methods. The plot baseline for compound3 appears
    near0.156mg/L while Table1 gives0.078mg/L; no absolute passage-series value is
    imported. Absence of detected MIC increase in this experiment cannot establish
    that resistance cannot evolve or identify a resistance determinant.
  snapshot_sha256: dcf8239a6e6628d784a488de975a886e0521cbb59d061b2e829e965230898609
- evidence_id: proteomics
  kind: primary_source
  reference: PMID:41405126; Figure2; SI TableS1 pagesS26–S29
  locator: Complete source SWATH-MS Methods/results, actual Figure2 and all extracted
    TableS1 rows.
  accessed_at: '2026-10-21T18:36:06Z'
  support: supports
  summary: Subinhibitory exposures are PBT2 at0.156, compound2 at0.078 and compound3
    at0.039mg/L. Protein-abundance responses include increased iron-transport-associated
    and decreased phosphate-associated proteins. TableS1 is response proteomics; its
    listed proteins are not direct binding targets. The main Methods uses greater-than30%
    abundance change with adjustedP<0.05, whereas the displayed result selection describes
    absolute log2FC at least1. No new target, regulatory mechanism, publicly deposited
    raw dataset or direct metal-flux measurement is inferred from these differences.
  snapshot_sha256: 1b130403095d4518fbc3a59edf57c3ed7753d47b6beb2f16c21d46c6efe583b8
- evidence_id: host-and-spectrum
  kind: primary_source
  reference: PMID:41405126; Tables2–4
  locator: Complete original tables and corresponding Methods/results.
  accessed_at: '2026-10-21T18:36:06Z'
  support: supports
  summary: HEK293S viability IC50 is higher for compounds2/3 than PBT2, but L1210
    IC50 is lower, so reduced toxicity is not universal across the two cell lines.
    Meningococcal and NTHi growth results are strain-specific; NTHi Table4 includes0.156
    and2.5mg/L endpoints outside its simplified prose range. These optional results
    are not native claims and are not copied as broad safety or species-level potency
    conclusions.
  snapshot_sha256: 2a99c3f72244f2e8a63dd207e623081cb3e00101c49502b9043ce4ff4b584fab
- evidence_id: role
  kind: authority
  reference: CHEBI:33282
  locator: Current official antibacterial-agent definition.
  accessed_at: '2026-10-21T18:36:06Z'
  support: supports
  summary: The exact growth and viable-count experiments support antibacterial filing.
    A clinical indication or experimentally resolved molecular target is not required
    for this qualitative role.
  snapshot_sha256: 20d92ce7e00c204b1753184671c043160821d692438278344335446aadcd5082
- evidence_id: snippet
  kind: validation
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md:14
  locator: Entire native/source snippet versus complete original text and relevant
    quantitative primary evidence.
  accessed_at: '2026-10-21T18:36:06Z'
  support: supports
  summary: The third-person Jen-and-colleagues wording combines results from a table
    and prose/figures into a curator summary. Its material statements are supported
    at their stated scope, but it is not a verbatim passage. The checklist requires
    summaries and interpretation to be placed in notes.
- evidence_id: search
  kind: search
  reference: 557-local-hits.txt;557-owner-hits.txt;557-authority-chemistry.json;056-root-fetch1.json
    through056-root-fetch6.json
  locator: Hidden/ignored-inclusive local searches, direct DOI/PMC and exact-key authority
    requests, verified publisher supplement retrieval.
  accessed_at: '2026-10-21T18:36:06Z'
  support: context_only
  summary: Exact-key searches in data/curation/conf YAML/TSV/JSON returned only the
    target record and curator table. Original supplement routes returned challenge
    HTML or403; the public publisher Figshare API resolved the same DOI and supplied
    the original PDF. Discovery was bounded to the named primary and authority checks,
    not a comprehensive later-literature survey.
  search_scope: 2026-10-21; hidden/ignored-inclusive exact label,identifier,key and
    slug searches; full-key data/curation/conf query; exact primary DOI/PMC and publisher
    supplement identity.
  snapshot_sha256: ecbe481459b2f09814f234caed349854a89c497196f85f7752551f0030c6f5c8
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral numbered amide
  outcome: supported
  summary: Independent graph reconstruction, exact primary drawings, systematic name
    and supplementary material support the native identity and masses.
  target_ids:
  - antibioticmech:curator-e8d0b1491b
  evidence_ids:
  - native
  - owners
  - chemistry
  - primary
  - material
  - authority
- assessment_id: activity
  area: evidence
  topic: Native WHO Z and tested-panel summary
  outcome: supported
  summary: The stated WHO Z value and tested-panel range agree with the original table/prose.
    Exact strain values cannot be reconstructed from a reported range alone.
  target_ids:
  - antibioticmech:curator-e8d0b1491b
  evidence_ids:
  - mic
  - primary
  - role
- assessment_id: followup
  area: evidence
  topic: Native rapid-killing activity
  outcome: supported
  summary: The actual source figure and corresponding assay Methods support the native
    qualitative follow-up statement without equating plotted floor or relative-survival
    reduction with guaranteed eradication.
  target_ids:
  - antibioticmech:curator-e8d0b1491b
  evidence_ids:
  - kill
  - cervical
- assessment_id: evidence-placement
  area: evidence
  topic: Paraphrase stored as snippet
  outcome: concern
  summary: The factual summary is supported but is not a verbatim quotation; move
    it into notes while retaining the existing structural explanation.
  target_ids:
  - antibioticmech:curator-e8d0b1491b
  evidence_ids:
  - snippet
  - native
  - owners
  - mic
  - kill
  - cervical
- assessment_id: optional
  area: completeness
  topic: Mechanism, resistance and safety boundaries
  outcome: supported
  summary: No missing optional object is itself a defect. Protein-abundance changes
    do not prove direct targets,30-day passage does not rule out future resistance,
    and cell-line effects do not establish clinical safety.
  target_ids:
  - antibioticmech:curator-e8d0b1491b
  evidence_ids:
  - proteomics
  - resistance
  - host-and-spectrum
- assessment_id: provenance
  area: provenance
  topic: Mint, source owner and proposed status
  outcome: supported
  summary: Exact DOI fragment and maintained curator row resolve the compound. Thirteen
    original input hashes, deterministic mint and single proposed-history event are
    consistent.
  target_ids:
  - antibioticmech:curator-e8d0b1491b
  evidence_ids:
  - owners
  - chemistry
  - native
  - search
findings:
- finding_id: F1
  issue_key: ip-antibiotic-3-paraphrase-in-source-snippet
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Move the supported curator summary out of the verbatim snippet field
  description: The maintained evidence_snippet combines table results and follow-up
    experiments in third-person curator wording. The source supports the factual claims,
    but this is not a verbatim passage. Use notes for the summary and preserve exact
    assay boundaries.
  target_ids:
  - antibioticmech:curator-e8d0b1491b
  field_paths:
  - source_concepts[0].evidence[0].snippet
  evidence_ids:
  - native
  - owners
  - snippet
  - mic
  - kill
  - cervical
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Exact publication-derived structure, definition and source evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Curator-inventory loading and generated evidence
  rule_id: 'review-checklist: Evidence standard, verbatim snippet versus curator notes'
  native_severity: minor
  normalization_reason: The error is bounded evidence placement, not an unsupported
    identity or activity claim.
actions:
- action_id: A1
  description: Correct the exact curator-row evidence placement and regenerate reproducibly.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:curator-e8d0b1491b
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Exact publication-derived structure, definition and source evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Curator-inventory loading and generated evidence
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Move the summary for source DOI:10.1021/acsinfecdis.5c00812#3 from evidence_snippet
    into evidence_notes, preserving the original structure notes, DOI and experimental
    scopes.
  - Retain native keyWHUQFDQKVSTVHC-UHFFFAOYSA-N, formula, charge, masses, source
    version and compound numbering.
  - Keep WHO Z MIC distinct from the panel-level range; retain relative-survival/viable-count
    context for follow-up claims. A replacement snippet must be short exact primary
    text.
  - Pass focused schema/strict and reproducibility checks without hand-editing generated
    YAML or rewriting native history.
limitations:
- Entire main and actual Scheme1/Table1/Figures1/2 were read. Supplement inspection
  covered actualS6–S7 and extracted TableS1 text; other analogue spectra were not
  independently reanalysed for this target.
- Raw instrument data, assay replicates and purity were not independently reprocessed.
  The MIC Methods gives overnight incubation and approximate inoculum, so exact unreported
  duration or solvent composition is not invented.
- The main reports a tested-gonococcal panel range without individual values in its
  tables. Passage transfer details and a formal killing-assay detection limit are
  unstated. Plot/prose differences are retained rather than silently resolved.
- Proteomic response and compound-family design do not establish a direct antibacterial
  protein target. Source cytotoxicity and additional-species summary discrepancies
  limit broad extrapolation but are not defects in unasserted native claims.
- No exhaustive later-literature or registry search was undertaken. The review remains
  a bounded scientific assessment of the exact native record.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Native/source/history/status remain unchanged; all original thirteen hashes were
  preserved. Actual curator-table owner annotations replace the generic initial ChEBI
  owner description.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
