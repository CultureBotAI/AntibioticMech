# Erdasporine B: supported activity and precursor identity with an invalid imported SMILES

- Review: 20261021T154240Z-erdasporine-b-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T15:13:51Z
- Finished UTC: 2026-10-21T15:42:40Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Original erdasporine B is independently mapped to compound 2 in the 2013 discovery paper and compound 8 in the 2015 comparison. The valid native InChI, current ChEBI molfile and adopted MIBiG graph agree, but the imported SMILES cannot be parsed because its pyrrolic N–H notation is missing. One major representation correction is needed. No unestablished kinase or topoisomerase mechanism is transferred from neighboring indolocarbazole classes.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 409; one whole native record. All thirteen initial hashes were verified before judgment and retained, with actual MIBiG table and extractor owners appended to give fifteen captured inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:156314 | data/antibiotics/antibacterial/erdasporine-b.yaml | generated | erdasporine B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema verification | passed | True | CHEBI:156314 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:156314 | Actual focused execution exited 0. |
| Focused chemistry verification | failed | False | CHEBI:156314 | Actual focused execution exited 1. |
| authority-map | passed | False | CHEBI:156314 | The native InChI, official molfile and adopted MIBiG SMILES independently produce the same full key. |
| adapter-catalog | passed | False | CHEBI:156314 | Catalog inspected before mechanistic follow-up; no exact environmental producer or endogenous gene mapping was available. |
| Authoritative full QC | failed | True | CHEBI:156314 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:156314 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:156314 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:156314 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:156314 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:156314 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:156314 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:156314 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:156314 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact B structure and classification

identity: concern. Targets: CHEBI:156314.

The valid native encoding, official molfile, MIBiG graph and independently mapped original figures agree. Four parents are broader and the antibacterial role is supported. The unusable imported SMILES is the confirmed defect.

### Separate discovery MIC and later IC50 assays

evidence: supported. Targets: CHEBI:156314.

The 2013 exact B experiment supports antibacterial classification and the bounded definition. The 2015 comparator supports a separate cellular activity profile, with a Gram-positive species conflict in its own methods/caption retained. No numeric native object is inferred.

### Environmental origin and precursor transformation

evidence: supported. Targets: CHEBI:156314.

The environmental esp cluster and engineered expression yield B, which can undergo enzymatic hydroxylation to A or spontaneous oxidation to C. These transformations are not natural-producer taxonomy or microbial-target evidence.

### Optional mechanism and biological fields

completeness: supported. Targets: CHEBI:156314.

The inspected 2015 overview explicitly leaves the carboxy-indolocarbazole target unknown. Empty mode, target, resistance, producer, clinical, activity, graph and dataset fields are not required-field defects. Scaffold analogies cannot supply a target.

### All adopted leads and maintained generation path

provenance: supported. Targets: CHEBI:156314.

Both adopted primary leads and every native field were assessed. Actual owners were captured before judgment while retaining all original input hashes. SEEDED status and source-only definition provenance remain honest.

## Findings

### F1: Repair the imported pyrrolic nitrogen encoding in SMILES

major / open / confirmed; issue key: erdasporine-b-invalid-aromatic-nh-smiles.

The native SMILES has bare aromatic n at all three pyrrolic nitrogens and fails kekulization. The native InChI, official ChEBI molfile, adopted MIBiG structure and original compound 2 drawing consistently require three N–H groups. Current ChEBI repeats the invalid text. Repair the maintained encoding without substituting erdasporine A, C or another indolocarbazole.

## Recommended Actions And Acceptance Checks

### A1

Correct the source-owned SMILES and regenerate the record through the maintained source path.

- Normalize the actual source representation from a validated official molfile or equivalent encoding and preserve source provenance.
- Require parsed SMILES to reproduce full key POAWNROCPSHGIZ-UHFFFAOYSA-N, neutral formula C22H15N3O2 and the stored masses; independently map original compound 2 in 2013 and compound 8 in 2015.
- Regenerate through the maintained source path and pass focused schema, strict, chemistry and source-reproduction checks. Preserve native SEEDED status.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/erdasporine-b.yaml; Entire native YAML. | supports | The SEEDED, EXACT CHEBI156314 record has two systematic exact synonyms, four broader chemical parents, one antibacterial role, one ChEBI source concept and five seed/reseed events. Its neutral C22H15N3O2 structure has key POAWNROCPSHGIZ-UHFFFAOYSA-N. The definition asserts environmental-DNA gene-cluster origin and HCT116/S. aureus effects. No external xrefs, numerical activity, target, mode, resistance, clinical, producer, dataset, causal-graph or discussion object is present. |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/mibig_producers.tsv; scripts/extract_source_inventory.py; scripts/extract_mibig_producers.py; scripts/seed_from_sources.py; conf/sources.yaml; Entire exact rows and applicable extraction, generation and producer-refusal code. | supports | ChEBI row 2753 supplies the native identity and two adopted leads, PMID24171465 and PMID25872030. MIBiG row 651 is compound 2 of 3 in BGC0001336, version 5, questionable quality, not expert reviewed, with heterologous-expression/gene-expression evidence and uncultured-bacterium taxon 77133. The seeder intentionally refuses unnamed taxa; its empty producer object is not a lost named producer. No exact ARO, FDA or PubChem source row owns this record. All initial hashes and original capture files remain preserved. |
| chebi | CHEBI:156314; https://www.ebi.ac.uk/chebi/CHEBI:156314; Complete official entry, names, classifications and molecular properties. | supports | Current ChEBI agrees with the native formula, neutral charge, masses, full InChIKey and both systematic names. Broader parents are methyl ester 25248, indolocarbazole alkaloid 37697, secondary amino compound 50995 and organic heterohexacyclic compound 51914; role 33282 is antibacterial agent. The textual SMILES repeats the native invalid encoding. The incoming functional-parent relation from erdasporine C is not an exact equivalence between the two compounds. |
| structures | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/156314; MIBiG:BGC0001336; Independent parsing of the official molfile, native InChI and adopted MIBiG SMILES. | partial | All three valid representations reproduce POAWNROCPSHGIZ-UHFFFAOYSA-N, neutral C22H15N3O2, mass 353.11642672 and no stereocentres. Each has three pyrrolic N–H groups. The native/current ChEBI textual SMILES uses bare n instead of [nH] and fails kekulization. This is an unusable encoding of an otherwise independently supported exact compound, not proof of another isomer or a mixture. |
| mibig | MIBiG:BGC0001336; https://raw.githubusercontent.com/mibig-secmet/mibig-json/master/data/BGC0001336.json; Entire public legacy-schema official entry and exact erdasporine B compound object. | supports | The legacy release 3.1 entry independently corroborates the B graph, KF551865.1 environmental locus and PMID24171465, with expression-based evidence. It is older than the adopted version 5 row and does not verify every later metadata value. The expression host is not a named natural producer. |
| original2013 | PMID:24171465; DOI:10.1021/ja408683p; PMC3878720; https://pmc.ncbi.nlm.nih.gov/articles/PMC3878720/; Complete original main article, including methods and captions; Figures 2, 4 and 5 visually mapped to B. | supports | Compound 2 is erdasporine B, the unhydroxylated methyl-carboxy indolocarbazole. Refactored EspODPM expression in E. coli BL21 gives B after 12 h; 2.3 mg is purified from a 2 L culture. Extended 36 h culture or purified B left in DMSO yields the oxidized C congener; feeding B-containing broth to EspX-expressing cells yields hydroxylated A. These experiments support environmental-cluster provenance without naming a cultured natural producer. The primary drawing agrees with the valid InChI/molfile, including all three N–H groups. |
| activity2013 | PMID:24171465; DOI:10.1021/ja408683p; Figure 2 and Bioactivity assays; Original Figure 2 image read with complete assay methods. | supports | Exact compound 2 has S. aureus MIC 4.2 µM and HCT116 IC50 5.3 µM. The caption explicitly gives µM; the methods prepare serial dilutions in µg/mL. S. aureus strain 6538P is tested in LB after 10^6-fold dilution of an overnight culture, for 18 h at 30°C, with OD600 &lt; 0.05 defining MIC. HCT116 ATCC CCL247 uses 72 h crystal-violet biomass measurement. Growth inhibition is not an MBC or direct target assay, and the host-cell IC50 is not antibacterial potency. |
| adopted2015 | PMID:25872030; DOI:10.1021/jacs.5b01968; https://bradylab.rockefeller.edu/wp-content/uploads/2022/11/47.pdf; Complete indexed abstract; original author-deposited Results/Discussion and methods pp 6047–6051 read, with Figures 6/7 visually inspected. | supports | The second adopted paper studies hydroxysporine and reductasporine but also tests erdasporine B explicitly as compound 8. Figure 6 reports B IC50 4.55 µM for the panel labeled S. aureus, greater than 150 µM for E. coli and C. albicans, and 8.92 µM for HCT116. These are curve-fitted growth/biomass IC50 values, not MICs. The methods instead name B. subtilis Sr168 as their Gram-positive organism, an unresolved source inconsistency that prevents unqualified strain assignment for the S. aureus-labeled curve. Figure 7 places B in the carboxy-indolocarbazole group with target unknown; kinase/topoisomerase targets shown for other classes are not B evidence. |
| adapter | iModulonDB catalog; Actual complete catalog inspected before mechanism research. | context_only | The native environmental-DNA origin does not resolve a covered natural producer, locus or transcriptomic dataset. S. aureus and HCT116 are assay systems, and the experimentally engineered E. coli host is not evidence of an endogenous esp gene program. No applicable component summary was found or assumed. |
| search | 409-inclusive-hits.txt; 409-fetch-results.json through 409-fetch3-results.json; Ignored-inclusive repository search and bounded original-source follow-up. | context_only | The exact identifier, name and key were searched with hidden and ignored files included across data, curation, conf, scripts, src, docs, .claude, reviews and reports. Focused curation/conf/reviews/reports search finds the queue but no exact override or prior report. Both adopted leads were resolved. The 2015 PMC page returned a browser challenge and EuropePMC XML 500; the author-deposited original PDF succeeded. 2013 supplementary attempts returned non-PDF challenge/empty content or 403 and were not treated as read spectra. |
| validation | 409-schema.log; 409-strict.log; 409-chemistry.json; 409-xref-chemistry.json; Actual focused checks and unchanged-input recheck. | supports | Schema and strict validation pass, while chemistry fails because SMILES cannot parse. Native InChI reproduces the full key, formula, charge and masses; the minted ChEBI alias reproduces. Independent valid authority encodings agree. |

## Limits And Additional Notes

- The 2013 main article and relevant original figures were fully inspected, but supplementary NMR spectra were unavailable through bounded public routes. No independent spectral re-elucidation is claimed.
- The 2015 original was inspected in the relevant Results/Discussion, biological methods and Figures 6/7, rather than a complete supplementary audit. Its Figure 6 labels S. aureus whereas its methods name B. subtilis Sr168; exact strain assignment remains unresolved. No MIC is derived from its IC50 curve.
- The public MIBiG entry inspected is legacy release 3.1, older than adopted entry version 5; it corroborates exact structure and environmental-cluster provenance rather than every later metadata field.
- A molecular target or named cultured natural producer is not established by the inspected sources. The 2013 main article has apparent solvent-ratio and volume reporting errors, which are not silently corrected.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- The 2013 MIC and 2015 IC50 are different endpoints under distinct reported conditions; their numerical differences do not establish a conflict in the native qualitative antibacterial role.
- Three independently valid representations establish the intended B identity despite the failed SMILES. No alternate graph was written to the native corpus.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T154240Z-erdasporine-b-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Erdasporine B: supported activity and precursor identity with an invalid imported
  SMILES'
started_at: '2026-10-21T15:13:51Z'
finished_at: '2026-10-21T15:42:40Z'
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
summary: Original erdasporine B is independently mapped to compound 2 in the 2013
  discovery paper and compound 8 in the 2015 comparison. The valid native InChI, current
  ChEBI molfile and adopted MIBiG graph agree, but the imported SMILES cannot be parsed
  because its pyrrolic N–H notation is missing. One major representation correction
  is needed. No unestablished kinase or topoisomerase mechanism is transferred from
  neighboring indolocarbazole classes.
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
  - path: data/antibiotics/antibacterial/erdasporine-b.yaml
    sha256: a5d5cd5a1991ae831494226d33cef5792e6ac4f2535656bd78a0a1c52fe45c9b
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
  - path: data/raw/mibig_producers.tsv
    sha256: d55289619e77e035ed437d432dd692ab382f254c3841c9a314752ef22578a01b
    role: context
  - path: docs/CURATION.md
    sha256: a364598a9c2bdaf9e0e71895d5b7a2fd61d3e726e0ed0da12bd895cc4c30e98c
    role: context
  - path: docs/HARMONIZATION.md
    sha256: fb8b58abca016ca5a7d856fcc6f1ec2deb210e0927394a480853830b39e1f060
    role: context
  - path: scripts/extract_mibig_producers.py
    sha256: a078cdf4c9b2d09999800ab7ae03f93d3972f29b7d2f460ebbbe7d7ec6b31c53
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
- target_id: CHEBI:156314
  path: data/antibiotics/antibacterial/erdasporine-b.yaml
  label: erdasporine B
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
    path: data/raw/mibig_producers.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_mibig_producers.py
    role: Actual adopted MIBiG extraction owner
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 409; one whole native record. All thirteen initial hashes
    were verified before judgment and retained, with actual MIBiG table and extractor
    owners appended to give fifteen captured inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:156314
checks:
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:156314
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/erdasporine-b.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:156314
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/erdasporine-b.yaml --out /private/tmp/am-review-session/409-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: Focused chemistry verification
  status: failed
  required: false
  summary: Actual focused execution exited 1.
  target_ids:
  - CHEBI:156314
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 409
  exit_code: 1
  expected_exit_code: 0
- check_id: authority-map
  name: authority-map
  status: passed
  required: false
  summary: The native InChI, official molfile and adopted MIBiG SMILES independently
    produce the same full key.
  target_ids:
  - CHEBI:156314
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/409-xref-check.py
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-catalog
  name: adapter-catalog
  status: passed
  required: false
  summary: Catalog inspected before mechanistic follow-up; no exact environmental
    producer or endogenous gene mapping was available.
  target_ids:
  - CHEBI:156314
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
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
  - CHEBI:156314
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
  - CHEBI:156314
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
  - CHEBI:156314
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
  - CHEBI:156314
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
  - CHEBI:156314
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
  - CHEBI:156314
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
  - CHEBI:156314
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
  - CHEBI:156314
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
  - CHEBI:156314
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/erdasporine-b.yaml
  locator: Entire native YAML.
  accessed_at: '2026-10-21T15:40:03Z'
  support: supports
  summary: The SEEDED, EXACT CHEBI156314 record has two systematic exact synonyms,
    four broader chemical parents, one antibacterial role, one ChEBI source concept
    and five seed/reseed events. Its neutral C22H15N3O2 structure has key POAWNROCPSHGIZ-UHFFFAOYSA-N.
    The definition asserts environmental-DNA gene-cluster origin and HCT116/S. aureus
    effects. No external xrefs, numerical activity, target, mode, resistance, clinical,
    producer, dataset, causal-graph or discussion object is present.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/mibig_producers.tsv; scripts/extract_source_inventory.py;
    scripts/extract_mibig_producers.py; scripts/seed_from_sources.py; conf/sources.yaml
  locator: Entire exact rows and applicable extraction, generation and producer-refusal
    code.
  accessed_at: '2026-10-21T15:40:03Z'
  support: supports
  summary: ChEBI row 2753 supplies the native identity and two adopted leads, PMID24171465
    and PMID25872030. MIBiG row 651 is compound 2 of 3 in BGC0001336, version 5, questionable
    quality, not expert reviewed, with heterologous-expression/gene-expression evidence
    and uncultured-bacterium taxon 77133. The seeder intentionally refuses unnamed
    taxa; its empty producer object is not a lost named producer. No exact ARO, FDA
    or PubChem source row owns this record. All initial hashes and original capture
    files remain preserved.
  snapshot_sha256: 1a1dda234d54ca1f5f0cd48b9bc9acd4adef2382c5d0858f24f9b5aa623cf9d6
- evidence_id: chebi
  kind: authority
  reference: CHEBI:156314; https://www.ebi.ac.uk/chebi/CHEBI:156314
  locator: Complete official entry, names, classifications and molecular properties.
  accessed_at: '2026-10-21T15:38:12Z'
  support: supports
  summary: Current ChEBI agrees with the native formula, neutral charge, masses, full
    InChIKey and both systematic names. Broader parents are methyl ester 25248, indolocarbazole
    alkaloid 37697, secondary amino compound 50995 and organic heterohexacyclic compound
    51914; role 33282 is antibacterial agent. The textual SMILES repeats the native
    invalid encoding. The incoming functional-parent relation from erdasporine C is
    not an exact equivalence between the two compounds.
  snapshot_sha256: bce932a5e3e764e74632226865f7b197c08af67c40ec8aa3892ea3dfcdb96ffa
- evidence_id: structures
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/156314; MIBiG:BGC0001336
  locator: Independent parsing of the official molfile, native InChI and adopted MIBiG
    SMILES.
  accessed_at: '2026-10-21T15:40:03Z'
  support: partial
  summary: All three valid representations reproduce POAWNROCPSHGIZ-UHFFFAOYSA-N,
    neutral C22H15N3O2, mass 353.11642672 and no stereocentres. Each has three pyrrolic
    N–H groups. The native/current ChEBI textual SMILES uses bare n instead of [nH]
    and fails kekulization. This is an unusable encoding of an otherwise independently
    supported exact compound, not proof of another isomer or a mixture.
  snapshot_sha256: 8bab7403546d3ff95a30e6bc466c54897326475ed4a4469d15ad57a760ab8fcd
- evidence_id: mibig
  kind: authority
  reference: MIBiG:BGC0001336; https://raw.githubusercontent.com/mibig-secmet/mibig-json/master/data/BGC0001336.json
  locator: Entire public legacy-schema official entry and exact erdasporine B compound
    object.
  accessed_at: '2026-10-21T15:33:24Z'
  support: supports
  summary: The legacy release 3.1 entry independently corroborates the B graph, KF551865.1
    environmental locus and PMID24171465, with expression-based evidence. It is older
    than the adopted version 5 row and does not verify every later metadata value.
    The expression host is not a named natural producer.
  snapshot_sha256: 4e24ce72d5a8d6e0f26c04209cb15ec599b85f349e0bbf01ad576edf4b02cfa9
- evidence_id: original2013
  kind: primary_source
  reference: PMID:24171465; DOI:10.1021/ja408683p; PMC3878720; https://pmc.ncbi.nlm.nih.gov/articles/PMC3878720/
  locator: Complete original main article, including methods and captions; Figures
    2, 4 and 5 visually mapped to B.
  accessed_at: '2026-10-21T15:33:24Z'
  support: supports
  summary: Compound 2 is erdasporine B, the unhydroxylated methyl-carboxy indolocarbazole.
    Refactored EspODPM expression in E. coli BL21 gives B after 12 h; 2.3 mg is purified
    from a 2 L culture. Extended 36 h culture or purified B left in DMSO yields the
    oxidized C congener; feeding B-containing broth to EspX-expressing cells yields
    hydroxylated A. These experiments support environmental-cluster provenance without
    naming a cultured natural producer. The primary drawing agrees with the valid
    InChI/molfile, including all three N–H groups.
  snapshot_sha256: 82b5c3c92b3de3699cc4f04829b58103c1c34247f1ce15cc8839c68f860df40b
- evidence_id: activity2013
  kind: primary_source
  reference: PMID:24171465; DOI:10.1021/ja408683p; Figure 2 and Bioactivity assays
  locator: Original Figure 2 image read with complete assay methods.
  accessed_at: '2026-10-21T15:35:24Z'
  support: supports
  summary: Exact compound 2 has S. aureus MIC 4.2 µM and HCT116 IC50 5.3 µM. The caption
    explicitly gives µM; the methods prepare serial dilutions in µg/mL. S. aureus
    strain 6538P is tested in LB after 10^6-fold dilution of an overnight culture,
    for 18 h at 30°C, with OD600 < 0.05 defining MIC. HCT116 ATCC CCL247 uses 72 h
    crystal-violet biomass measurement. Growth inhibition is not an MBC or direct
    target assay, and the host-cell IC50 is not antibacterial potency.
  snapshot_sha256: 08d4a3bc4ca6d2ce42376c066f5ee0598d8e77c1199cacf81144590a2db9adba
- evidence_id: adopted2015
  kind: primary_source
  reference: PMID:25872030; DOI:10.1021/jacs.5b01968; https://bradylab.rockefeller.edu/wp-content/uploads/2022/11/47.pdf
  locator: Complete indexed abstract; original author-deposited Results/Discussion
    and methods pp 6047–6051 read, with Figures 6/7 visually inspected.
  accessed_at: '2026-10-21T15:38:41Z'
  support: supports
  summary: The second adopted paper studies hydroxysporine and reductasporine but
    also tests erdasporine B explicitly as compound 8. Figure 6 reports B IC50 4.55
    µM for the panel labeled S. aureus, greater than 150 µM for E. coli and C. albicans,
    and 8.92 µM for HCT116. These are curve-fitted growth/biomass IC50 values, not
    MICs. The methods instead name B. subtilis Sr168 as their Gram-positive organism,
    an unresolved source inconsistency that prevents unqualified strain assignment
    for the S. aureus-labeled curve. Figure 7 places B in the carboxy-indolocarbazole
    group with target unknown; kinase/topoisomerase targets shown for other classes
    are not B evidence.
  snapshot_sha256: bc93f4d65ebed359a1bc4e660e0a674b875a87cc2d2e2401b0fb537f1a45105c
- evidence_id: adapter
  kind: database
  reference: iModulonDB catalog
  locator: Actual complete catalog inspected before mechanism research.
  accessed_at: '2026-10-21T15:40:03Z'
  support: context_only
  summary: The native environmental-DNA origin does not resolve a covered natural
    producer, locus or transcriptomic dataset. S. aureus and HCT116 are assay systems,
    and the experimentally engineered E. coli host is not evidence of an endogenous
    esp gene program. No applicable component summary was found or assumed.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: search
  kind: search
  reference: 409-inclusive-hits.txt; 409-fetch-results.json through 409-fetch3-results.json
  locator: Ignored-inclusive repository search and bounded original-source follow-up.
  accessed_at: '2026-10-21T15:40:03Z'
  support: context_only
  summary: The exact identifier, name and key were searched with hidden and ignored
    files included across data, curation, conf, scripts, src, docs, .claude, reviews
    and reports. Focused curation/conf/reviews/reports search finds the queue but
    no exact override or prior report. Both adopted leads were resolved. The 2015
    PMC page returned a browser challenge and EuropePMC XML 500; the author-deposited
    original PDF succeeded. 2013 supplementary attempts returned non-PDF challenge/empty
    content or 403 and were not treated as read spectra.
  search_scope: '2026-10-21: exact CHEBI:156314, erdasporine B/name/slug and POAWNROCPSHGIZ
    searches with rg --no-ignore --hidden across the stated repository paths; current
    official chemical entries, adopted PMIDs and public original publisher/author
    routes. No paid source used.'
  snapshot_sha256: 2ddaf2b33dab69fd2875bb6113e99c0fea4990e7a9985b90e90a8637430b4d39
- evidence_id: validation
  kind: validation
  reference: 409-schema.log; 409-strict.log; 409-chemistry.json; 409-xref-chemistry.json
  locator: Actual focused checks and unchanged-input recheck.
  accessed_at: '2026-10-21T15:40:03Z'
  support: supports
  summary: Schema and strict validation pass, while chemistry fails because SMILES
    cannot parse. Native InChI reproduces the full key, formula, charge and masses;
    the minted ChEBI alias reproduces. Independent valid authority encodings agree.
  snapshot_sha256: bbecf732348172dd1991ed5710be05a234e6d4f70f09cafef3a0879073684465
assessments:
- assessment_id: identity
  area: identity
  topic: Exact B structure and classification
  outcome: concern
  summary: The valid native encoding, official molfile, MIBiG graph and independently
    mapped original figures agree. Four parents are broader and the antibacterial
    role is supported. The unusable imported SMILES is the confirmed defect.
  target_ids:
  - CHEBI:156314
  evidence_ids:
  - native
  - chebi
  - structures
  - original2013
- assessment_id: activity
  area: evidence
  topic: Separate discovery MIC and later IC50 assays
  outcome: supported
  summary: The 2013 exact B experiment supports antibacterial classification and the
    bounded definition. The 2015 comparator supports a separate cellular activity
    profile, with a Gram-positive species conflict in its own methods/caption retained.
    No numeric native object is inferred.
  target_ids:
  - CHEBI:156314
  evidence_ids:
  - activity2013
  - adopted2015
  - original2013
- assessment_id: biosynthesis
  area: evidence
  topic: Environmental origin and precursor transformation
  outcome: supported
  summary: The environmental esp cluster and engineered expression yield B, which
    can undergo enzymatic hydroxylation to A or spontaneous oxidation to C. These
    transformations are not natural-producer taxonomy or microbial-target evidence.
  target_ids:
  - CHEBI:156314
  evidence_ids:
  - owners
  - mibig
  - original2013
  - adapter
- assessment_id: coverage
  area: completeness
  topic: Optional mechanism and biological fields
  outcome: supported
  summary: The inspected 2015 overview explicitly leaves the carboxy-indolocarbazole
    target unknown. Empty mode, target, resistance, producer, clinical, activity,
    graph and dataset fields are not required-field defects. Scaffold analogies cannot
    supply a target.
  target_ids:
  - CHEBI:156314
  evidence_ids:
  - native
  - adopted2015
  - search
- assessment_id: provenance
  area: provenance
  topic: All adopted leads and maintained generation path
  outcome: supported
  summary: Both adopted primary leads and every native field were assessed. Actual
    owners were captured before judgment while retaining all original input hashes.
    SEEDED status and source-only definition provenance remain honest.
  target_ids:
  - CHEBI:156314
  evidence_ids:
  - owners
  - chebi
  - validation
  - search
findings:
- finding_id: F1
  issue_key: erdasporine-b-invalid-aromatic-nh-smiles
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Repair the imported pyrrolic nitrogen encoding in SMILES
  description: The native SMILES has bare aromatic n at all three pyrrolic nitrogens
    and fails kekulization. The native InChI, official ChEBI molfile, adopted MIBiG
    structure and original compound 2 drawing consistently require three N–H groups.
    Current ChEBI repeats the invalid text. Repair the maintained encoding without
    substituting erdasporine A, C or another indolocarbazole.
  target_ids:
  - CHEBI:156314
  field_paths:
  - chemical_structure.smiles
  evidence_ids:
  - native
  - chebi
  - structures
  - original2013
  - validation
  rule_id: Structure encodings must parse and denote the same exact molecule
  native_severity: major
  normalization_reason: A required molecular representation is unusable, but independent
    valid encodings and original primary structure establish the intended exact molecule.
    This is not a demonstrated wrong compound identity.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted invalid textual SMILES
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ChEBI structure extraction and normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated molecular representation
actions:
- action_id: A1
  description: Correct the source-owned SMILES and regenerate the record through the
    maintained source path.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:156314
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted invalid textual SMILES
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ChEBI structure extraction and normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated molecular representation
  acceptance_checks:
  - Normalize the actual source representation from a validated official molfile or
    equivalent encoding and preserve source provenance.
  - Require parsed SMILES to reproduce full key POAWNROCPSHGIZ-UHFFFAOYSA-N, neutral
    formula C22H15N3O2 and the stored masses; independently map original compound
    2 in 2013 and compound 8 in 2015.
  - Regenerate through the maintained source path and pass focused schema, strict,
    chemistry and source-reproduction checks. Preserve native SEEDED status.
limitations:
- The 2013 main article and relevant original figures were fully inspected, but supplementary
  NMR spectra were unavailable through bounded public routes. No independent spectral
  re-elucidation is claimed.
- The 2015 original was inspected in the relevant Results/Discussion, biological methods
  and Figures 6/7, rather than a complete supplementary audit. Its Figure 6 labels
  S. aureus whereas its methods name B. subtilis Sr168; exact strain assignment remains
  unresolved. No MIC is derived from its IC50 curve.
- The public MIBiG entry inspected is legacy release 3.1, older than adopted entry
  version 5; it corroborates exact structure and environmental-cluster provenance
  rather than every later metadata field.
- A molecular target or named cultured natural producer is not established by the
  inspected sources. The 2013 main article has apparent solvent-ratio and volume reporting
  errors, which are not silently corrected.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- The 2013 MIC and 2015 IC50 are different endpoints under distinct reported conditions;
  their numerical differences do not establish a conflict in the native qualitative
  antibacterial role.
- Three independently valid representations establish the intended B identity despite
  the failed SMILES. No alternate graph was written to the native corpus.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
