# Deoxyherqueinone(1−): consistent exact ion with bounded microspecies provenance

- Review: 20261021T143246Z-deoxyherqueinone-1-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:11:39Z
- Finished UTC: 2026-10-21T14:32:46Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The exact 4-olate graph, assigned R centre and source import are consistent. One informational follow-up concerns the provenance of the pH 7.3 major-microspecies statement and exact-ion activity scope: the inspected primary work supports the neutral parent and biosynthesis, not a measured distribution or ion-specific antibacterial assay. No corrective structural defect is established. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record: definition and source, both synonym types, parent, antibacterial role, complete chemical representation, source concept and mint, source version, grounding/status and all three history events; sole adopted citation assessed.

Selection: Queue position 355; all thirteen original input hashes verified before assessment and preserved. The captured ChEBI extraction and seeding inputs are the actual owners.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:145874 | data/antibiotics/antibacterial/deoxyherqueinone-1.yaml | generated | deoxyherqueinone(1−) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:145874 | Actual focused schema validation found no issues. |
| strict | passed | True | CHEBI:145874 | Actual strict validation scanned one file with zero errors. |
| initial-chemistry | failed | False | CHEBI:145874 | The original helper returned 1 solely because RDKit includes the negative charge suffix in C20H19O6-, while the native schema stores elemental formula C20H19O6 and charge -1 separately. Both structures parsed and reproduced the key, masses, R centre and mint. The retained failure is superseded by the charge-aware comparison below, not a native-data failure. |
| charge-aware-chemistry | passed | False | CHEBI:145874 | Independent native SMILES, native InChI and current ChEBI SMILES agree in full key, elemental formula, formal charge, masses and R centre. Formula and charge are tested separately. The additional PubChem tautomer comparison is contextual, not a new exact xref. |
| Authoritative full QC | failed | True | CHEBI:145874 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:145874 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:145874 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:145874 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:145874 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:145874 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:145874 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:145874 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:145874 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact protonation, stereochemistry, names and registry scope

identity: supported. Targets: CHEBI:145874.

The explicit 4-olate graph, charge, formula, masses and assigned R centre agree with current ChEBI and the native systematic name. Its parent label is deliberately related, not an exact equivalence. Do not merge it with the neutral record.

### Antibacterial role and exact experimental material

evidence: unknown. Targets: CHEBI:145874.

The native antibacterial role is a faithful ChEBI assertion. Original positive data concern named parent deoxyherqueinone; the inspected studies do not establish a separately tested 4-olate reagent, its fraction in assay medium or an ion-specific potency. This limits independent exact-form support without proving the role false.

### Microspecies statement, fungal provenance and biosynthetic context

evidence: unknown. Targets: CHEBI:145874.

The pH 7.3 statement is source-attested but was not independently verified. The sole adopted 2017 paper and inspected supplement concern neutral-product biosynthesis and a different precursor pKa. They do not identify an antimicrobial target or establish exact-ion speciation.

### Generated ownership, source history, citation disposition and optional fields

provenance: supported. Targets: CHEBI:145874.

The entire record and actual maintained row/code were inspected. Original hashes and seed history are preserved; source mints reproduce. Missing optional quantitative activity, producer object, molecular target, resistance, clinical status or graph is not a defect by itself. No scientific-status promotion follows from passing checks.

## Findings

### F1: Trace the exact 4-olate microspecies provenance before treating parent data as ion-specific evidence

informational / open / confirmed; issue key: deoxyherqueinone-4-olate-microspecies-evidence-scope.

The native definition faithfully repeats ChEBI that this 4-olate is the major microspecies at pH 7.3. The sole adopted paper instead predicts a pKa for precursor 6a and depicts neutral deoxyherqueinone 10 in biosynthesis. The additional antibacterial papers concern the named parent without separately established ionic material or assay speciation. This identifies the inspected evidence boundary, not a demonstrated error in the ChEBI prediction or proof of inactivity. A traceable exact-structure model or measurement would resolve the question.

## Recommended Actions And Acceptance Checks

### A1

Resolve the exact-structure microspecies provenance in the maintained source qualification before adding ion-specific mechanism or activity evidence.

- Identify the actual prediction or measurement for the native 4-olate and neutral parent, recording structural tautomer, protonation site, conditions and method/version. Do not reuse the 2017 precursor 6a pKa as a result for compound 10.
- If adding antibacterial evidence, preserve tested material, assay pH and any measured or modeled speciation; do not relabel parent MICs as separately measured 4-olate activity.
- Retain the source-attested claim with explicit provenance while uncertainty persists. Only qualify or correct generated wording if additional exact evidence warrants it, then rerun focused schema, strict and charge-aware chemistry checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/deoxyherqueinone-1.yaml; Entire native YAML and independently parsed chemical representation. | supports | CHEBI:145874 is the explicit 4-olate, C20H19O6 with charge -1 and key VZWSSCQUCMSKLE-MRVPVSSYSA-M. The systematic exact synonym agrees with its R centre; unqualified deoxyherqueinone is correctly RELATED_SYNONYM. There are no exact xrefs. The record remains SEEDED and EXACT, with no primary assay, target, mechanism, resistance, clinical status or producer object asserted. |
| owners | data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; curation/decisions.tsv; Complete exact ChEBI row 2685 and relevant role filtering, extraction, source-concept minting and seeding code; exact decision/curator follow-up. | supports | The maintained row reproduces the native definition, identity, structure, aliases, parent terms and antibacterial role. The source version is 2026-08-30; all three history entries are seed/reseed events. The source mint independently reproduces. The extractor restricts exported roles to configured antimicrobial roots; omission of a generic fungal-metabolite role is intentional. The citation inventory is discovery provenance, not automatic claim-level primary evidence. No exact curator or decision override was found in the ignored-inclusive search. |
| authority | CHEBI:145874; Current complete official ChEBI entry, names, structure, relations and cross-references; independent native/authority parsing. | supports | Current ChEBI confirms the exact 4-olate structure, single R centre, masses, parent phenolate anion CHEBI:50525 and antibacterial role CHEBI:33282. It repeats the major-microspecies-at-pH-7.3 definition. This verifies faithful database provenance, not an independent pKa determination. |
| chemistry | 355356-chemistry-check.json; 355-chemistry.json; Independent full native/current-ChEBI SMILES and InChI comparisons; source mint and PubChem name-query context. | supports | Native and current ChEBI graphs agree exactly. Both adjacent records have the same R centre and differ in protonation/charge. PubChem name result CID26322709 has key KMPAOJFBQSXEAI-MRVPVSSYSA-N, a different keto/enol representation, not the native full key. Independent canonical tautomer enumeration converges; the original 2001 paper discusses tautomerism. PubChem is not an asserted native exact xref, so this is not a cross-reference defect or reason to overwrite the native form. Exact-key API queries returned 404, which is not proof of chemical absence. |
| antibacterial1965 | PMID:5870759; DOI:10.1007/BF02139744; Entire one-page original communication on page 376, including its table, visually inspected; adjacent thiopental article excluded. | context_only | The named deoxyherqueinone, prepared from herqueinone, has reported MICs of 20 micrograms/mL for B. mycoides, 18 for B. subtilis, 35 for S. lutea and 20 for S. aureus. The resistant subtilis-group and penicillin-resistant S. aureus entries are 18 and 20. K. pneumoniae is described as inactive without a stated ceiling. These are parent-compound results; the short report omits medium, pH, inoculum, incubation, strain accession and analytical purity. Its stronger atrovenetin values do not belong to deoxyherqueinone. No separate 4-olate material or mechanistic target is tested. |
| isolation2001 | PMID:11676006; DOI:10.1271/bbb.65.1965; All five scanned original pages 1965–1969 visually read, including Figures 1–2, tables and experimental methods. | context_only | Activity-guided Penicillium isolate A-23-2 yields 50 mg compound 2 from 2 L culture; MS, NMR and diacetyl-derivative comparison identify deoxyherqueinone. The authors explain NMR discrepancies by tautomerism. Culture/disc and TLC bioautography concern B. subtilis, Brevibacterium ammoniagenes and Arthrobacter simplex; these are not new purified-compound MIC measurements. The producing isolate is identified at genus level, not proven P. herquei. Figure 2 does not independently establish absolute configuration. Neither exact-ion antibacterial activity nor a pH 7.3 distribution is measured. |
| origin1972 | PMID:4113758; DOI:10.7164/antibiotics.25.155; Complete original main text pages 155–162, including experimental section and Table 1, read. | context_only | P. herquei strain I, PRL1838, produces a mixture containing deoxyherqueinone and atrovenetin. The authors could not isolate the free components separately by crystallization or chromatography, but recovered and identified diacetyldeoxyherqueinone after acetylation. This is qualified natural-occurrence support. The 1 microgram/mL antibacterial result in this paper belongs to herqueichrysin, not deoxyherqueinone. Herqueichrysin is a constitutional isomer and its biological results are not transferred. |
| biosynthesis2017 | PMID:28240554; DOI:10.1021/jacs.7b01089; PMC5474393; Complete original main text and Figure 2 read; main Figure 2 visually inspected. | supports | The P. herquei NRRL1040 pathway and yeast reconstitution place deoxyherqueinone at compound 10, produced by PhnC methylation and converted onward by PhnG. The drawn R-configured neutral product supports the natural-parent identity. These enzymes concern biosynthesis, not antibacterial drug targets. The reported predicted pKa of 6.9 belongs to a phenol on prenylated precursor 6a, not deoxyherqueinone 10. No direct antibacterial assay or measured major-microspecies fraction for the native 4-olate is reported. |
| biosynthesis-si | DOI:10.1021/jacs.7b01089.s001; https://api.figshare.com/v2/articles/4707601; Verified publisher Figshare PDF: selected methods S4–S7 and Figures S4/S34 on S20/S50 read; both figure pages visually inspected. | supports | S4 shows P. herquei chemical-complementation and yeast gene-combination product profiles, including compound 10. S34 is PhnH kinetics and pH response using precursor 6; panel D explicitly assigns calculator-derived pKa values to precursor tautomers 6a/6b. Neither panel establishes the native deoxyherqueinone 4-olate fraction at pH 7.3. The complete supporting PDF was downloaded, but only the specified sections and figures were assessed; no claim of complete spectral reprocessing is made. |
| search | 355356-inclusive-hits.txt; public exact-name/identifier literature search; Gitignore-independent local search and bounded public primary/official follow-up. | context_only | The exact source/native rows and expected queue entries were found. Hidden and ignored files were included when checking for exact maintained decisions and curator additions. Searches did not establish an independently sourced exact 4-olate pKa or physiological microspecies fraction; this is a bounded search result, not proof no such evidence exists. Both records lack native protein, pathway, regulator or transcriptomic assertions, so the structured iModulonDB adapter is not applicable. Biosynthetic genes found in newly inspected papers are not converted to drug-target assertions. |
| validation | 355-schema.log;355-strict.log;355-chemistry.json;355356-chemistry-check.json; Actual focused validation outputs and unchanged input-byte verification. | supports | Schema and strict checks exit 0. The explicit charge-aware chemistry comparison exits 0. The original thirteen captured input hashes remain unchanged. The anion generic-helper failure is retained with its corrected interpretation; the neutral generic helper passes. These deterministic results do not establish biological mechanism or clinical efficacy. |

## Limits And Additional Notes

- The 1965 original paper was read completely, including its table, but reports little assay-method or material characterization detail. Its named-parent antibacterial results do not independently establish a discrete ionic reagent, modern strain-specific susceptibility or a mechanistic target.
- The 2001 paper was read completely from scanned pages. Its deoxyherqueinone assignment uses NMR, MS and derivatization; absolute configuration is not independently established by its unwedge drawing. The 1972 paper was read completely as text, but its derivative isolation does not amount to purification of the free parent from that culture.
- The 2017 main text and Figure 2 were inspected; supporting information review was limited to S4–S7, S20 and S50, with the two specified figures viewed. Raw spectra, chromatographic integrations and all calculations were not reprocessed. Initial PMC supplement access returned an HTML challenge and direct ACS returned 403; the verified public publisher Figshare PDF supplied the assessed supplement.
- No independent exact 4-olate pKa/speciation source was established in the bounded search. The pH 7.3 assertion remains ChEBI-attested; lack of an inspected primary determination is not proof it is chemically false.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Both records retain a single R stereocentre. Their principal distinction is protonation, not a stereochemical variant. Optional enrichment remains separate from corrective curation.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T143246Z-deoxyherqueinone-1-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Deoxyherqueinone(1−): consistent exact ion with bounded microspecies provenance'
started_at: '2026-10-21T14:11:39Z'
finished_at: '2026-10-21T14:32:46Z'
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
summary: 'The exact 4-olate graph, assigned R centre and source import are consistent.
  One informational follow-up concerns the provenance of the pH 7.3 major-microspecies
  statement and exact-ion activity scope: the inspected primary work supports the
  neutral parent and biosynthesis, not a measured distribution or ion-specific antibacterial
  assay. No corrective structural defect is established. Scientific assessment retains
  the stated evidence limits; full verification is blocked by the shared native-library
  failure.'
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
  - path: data/antibiotics/antibacterial/deoxyherqueinone-1.yaml
    sha256: f92269e3b6999931a86233513b8a2bfa805b94f2334141d11fcf59acc7530140
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
- target_id: CHEBI:145874
  path: data/antibiotics/antibacterial/deoxyherqueinone-1.yaml
  label: deoxyherqueinone(1−)
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
scope:
  description: 'Entire exact native record: definition and source, both synonym types,
    parent, antibacterial role, complete chemical representation, source concept and
    mint, source version, grounding/status and all three history events; sole adopted
    citation assessed.'
  selection: Queue position 355; all thirteen original input hashes verified before
    assessment and preserved. The captured ChEBI extraction and seeding inputs are
    the actual owners.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:145874
  exclusions:
  - target: Neutral deoxyherqueinone CHEBI:145901
    reason: The adjacent record is conjugate-acid/base context, not an exact interchangeable
      identity. Both retain the same R stereocentre; no merge or assay transfer is
      inferred.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Actual focused schema validation found no issues.
  target_ids:
  - CHEBI:145874
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/deoxyherqueinone-1.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Actual strict validation scanned one file with zero errors.
  target_ids:
  - CHEBI:145874
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/deoxyherqueinone-1.yaml --out /private/tmp/am-review-session/355-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: initial-chemistry
  name: initial-chemistry
  status: failed
  required: false
  summary: The original helper returned 1 solely because RDKit includes the negative
    charge suffix in C20H19O6-, while the native schema stores elemental formula C20H19O6
    and charge -1 separately. Both structures parsed and reproduced the key, masses,
    R centre and mint. The retained failure is superseded by the charge-aware comparison
    below, not a native-data failure.
  target_ids:
  - CHEBI:145874
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 355
  exit_code: 1
  expected_exit_code: 0
- check_id: charge-aware-chemistry
  name: charge-aware-chemistry
  status: passed
  required: false
  summary: Independent native SMILES, native InChI and current ChEBI SMILES agree
    in full key, elemental formula, formal charge, masses and R centre. Formula and
    charge are tested separately. The additional PubChem tautomer comparison is contextual,
    not a new exact xref.
  target_ids:
  - CHEBI:145874
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/355356-chemistry-check.py
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
  - CHEBI:145874
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
  - CHEBI:145874
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
  - CHEBI:145874
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
  - CHEBI:145874
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
  - CHEBI:145874
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
  - CHEBI:145874
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
  - CHEBI:145874
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
  - CHEBI:145874
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
  - CHEBI:145874
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/deoxyherqueinone-1.yaml
  locator: Entire native YAML and independently parsed chemical representation.
  accessed_at: '2026-10-21T14:31:47Z'
  support: supports
  summary: CHEBI:145874 is the explicit 4-olate, C20H19O6 with charge -1 and key VZWSSCQUCMSKLE-MRVPVSSYSA-M.
    The systematic exact synonym agrees with its R centre; unqualified deoxyherqueinone
    is correctly RELATED_SYNONYM. There are no exact xrefs. The record remains SEEDED
    and EXACT, with no primary assay, target, mechanism, resistance, clinical status
    or producer object asserted.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py; curation/decisions.tsv
  locator: Complete exact ChEBI row 2685 and relevant role filtering, extraction,
    source-concept minting and seeding code; exact decision/curator follow-up.
  accessed_at: '2026-10-21T14:31:47Z'
  support: supports
  summary: The maintained row reproduces the native definition, identity, structure,
    aliases, parent terms and antibacterial role. The source version is 2026-08-30;
    all three history entries are seed/reseed events. The source mint independently
    reproduces. The extractor restricts exported roles to configured antimicrobial
    roots; omission of a generic fungal-metabolite role is intentional. The citation
    inventory is discovery provenance, not automatic claim-level primary evidence.
    No exact curator or decision override was found in the ignored-inclusive search.
  snapshot_sha256: d471c7f32be9b0d260dc1cd2dee44b34be92146786546291f8d9ef3d91ccf8d6
- evidence_id: authority
  kind: authority
  reference: CHEBI:145874
  locator: Current complete official ChEBI entry, names, structure, relations and
    cross-references; independent native/authority parsing.
  accessed_at: '2026-10-21T14:24:44Z'
  support: supports
  summary: Current ChEBI confirms the exact 4-olate structure, single R centre, masses,
    parent phenolate anion CHEBI:50525 and antibacterial role CHEBI:33282. It repeats
    the major-microspecies-at-pH-7.3 definition. This verifies faithful database provenance,
    not an independent pKa determination.
  snapshot_sha256: 276351c57b1f8a0461ea868bb5693179cb31fe72d246975c751c6b7417b13e00
- evidence_id: chemistry
  kind: validation
  reference: 355356-chemistry-check.json; 355-chemistry.json
  locator: Independent full native/current-ChEBI SMILES and InChI comparisons; source
    mint and PubChem name-query context.
  accessed_at: '2026-10-21T14:31:47Z'
  support: supports
  summary: Native and current ChEBI graphs agree exactly. Both adjacent records have
    the same R centre and differ in protonation/charge. PubChem name result CID26322709
    has key KMPAOJFBQSXEAI-MRVPVSSYSA-N, a different keto/enol representation, not
    the native full key. Independent canonical tautomer enumeration converges; the
    original 2001 paper discusses tautomerism. PubChem is not an asserted native exact
    xref, so this is not a cross-reference defect or reason to overwrite the native
    form. Exact-key API queries returned 404, which is not proof of chemical absence.
  snapshot_sha256: 88aec2ebe1d20410e35ede211746a13269a1d36527c5fc09188859c7e464b574
- evidence_id: antibacterial1965
  kind: primary_source
  reference: PMID:5870759; DOI:10.1007/BF02139744
  locator: Entire one-page original communication on page 376, including its table,
    visually inspected; adjacent thiopental article excluded.
  accessed_at: '2026-10-21T14:25:20Z'
  support: context_only
  summary: The named deoxyherqueinone, prepared from herqueinone, has reported MICs
    of 20 micrograms/mL for B. mycoides, 18 for B. subtilis, 35 for S. lutea and 20
    for S. aureus. The resistant subtilis-group and penicillin-resistant S. aureus
    entries are 18 and 20. K. pneumoniae is described as inactive without a stated
    ceiling. These are parent-compound results; the short report omits medium, pH,
    inoculum, incubation, strain accession and analytical purity. Its stronger atrovenetin
    values do not belong to deoxyherqueinone. No separate 4-olate material or mechanistic
    target is tested.
  snapshot_sha256: 98a9d1036821157bb67309e25584f790a762990a4657e12ec3c627cea4dc9fa6
- evidence_id: isolation2001
  kind: primary_source
  reference: PMID:11676006; DOI:10.1271/bbb.65.1965
  locator: All five scanned original pages 1965–1969 visually read, including Figures
    1–2, tables and experimental methods.
  accessed_at: '2026-10-21T14:25:46Z'
  support: context_only
  summary: Activity-guided Penicillium isolate A-23-2 yields 50 mg compound 2 from
    2 L culture; MS, NMR and diacetyl-derivative comparison identify deoxyherqueinone.
    The authors explain NMR discrepancies by tautomerism. Culture/disc and TLC bioautography
    concern B. subtilis, Brevibacterium ammoniagenes and Arthrobacter simplex; these
    are not new purified-compound MIC measurements. The producing isolate is identified
    at genus level, not proven P. herquei. Figure 2 does not independently establish
    absolute configuration. Neither exact-ion antibacterial activity nor a pH 7.3
    distribution is measured.
  snapshot_sha256: 01c6f217bf84b3a8ba643e0dd95444d349632e8cbf6a6b34e0d7530994d7fed9
- evidence_id: origin1972
  kind: primary_source
  reference: PMID:4113758; DOI:10.7164/antibiotics.25.155
  locator: Complete original main text pages 155–162, including experimental section
    and Table 1, read.
  accessed_at: '2026-10-21T14:25:45Z'
  support: context_only
  summary: P. herquei strain I, PRL1838, produces a mixture containing deoxyherqueinone
    and atrovenetin. The authors could not isolate the free components separately
    by crystallization or chromatography, but recovered and identified diacetyldeoxyherqueinone
    after acetylation. This is qualified natural-occurrence support. The 1 microgram/mL
    antibacterial result in this paper belongs to herqueichrysin, not deoxyherqueinone.
    Herqueichrysin is a constitutional isomer and its biological results are not transferred.
  snapshot_sha256: 58a57c6774119df0d20e135216a5cccbfeb5f48ec62df384fe03062692a28969
- evidence_id: biosynthesis2017
  kind: primary_source
  reference: PMID:28240554; DOI:10.1021/jacs.7b01089; PMC5474393
  locator: Complete original main text and Figure 2 read; main Figure 2 visually inspected.
  accessed_at: '2026-10-21T14:25:45Z'
  support: supports
  summary: The P. herquei NRRL1040 pathway and yeast reconstitution place deoxyherqueinone
    at compound 10, produced by PhnC methylation and converted onward by PhnG. The
    drawn R-configured neutral product supports the natural-parent identity. These
    enzymes concern biosynthesis, not antibacterial drug targets. The reported predicted
    pKa of 6.9 belongs to a phenol on prenylated precursor 6a, not deoxyherqueinone
    10. No direct antibacterial assay or measured major-microspecies fraction for
    the native 4-olate is reported.
  snapshot_sha256: 84f68ff839fac62f5bf6231ba69cde8cacc21ea15496c69f9ec940f07a913d40
- evidence_id: biosynthesis-si
  kind: primary_source
  reference: DOI:10.1021/jacs.7b01089.s001; https://api.figshare.com/v2/articles/4707601
  locator: 'Verified publisher Figshare PDF: selected methods S4–S7 and Figures S4/S34
    on S20/S50 read; both figure pages visually inspected.'
  accessed_at: '2026-10-21T14:27:43Z'
  support: supports
  summary: S4 shows P. herquei chemical-complementation and yeast gene-combination
    product profiles, including compound 10. S34 is PhnH kinetics and pH response
    using precursor 6; panel D explicitly assigns calculator-derived pKa values to
    precursor tautomers 6a/6b. Neither panel establishes the native deoxyherqueinone
    4-olate fraction at pH 7.3. The complete supporting PDF was downloaded, but only
    the specified sections and figures were assessed; no claim of complete spectral
    reprocessing is made.
  snapshot_sha256: 27b387bb1eea01dff894c87b448bea2d2fabd2c36f937a3d5c4a4c9b007b6580
- evidence_id: search
  kind: search
  reference: 355356-inclusive-hits.txt; public exact-name/identifier literature search
  locator: Gitignore-independent local search and bounded public primary/official
    follow-up.
  accessed_at: '2026-10-21T14:31:47Z'
  support: context_only
  summary: The exact source/native rows and expected queue entries were found. Hidden
    and ignored files were included when checking for exact maintained decisions and
    curator additions. Searches did not establish an independently sourced exact 4-olate
    pKa or physiological microspecies fraction; this is a bounded search result, not
    proof no such evidence exists. Both records lack native protein, pathway, regulator
    or transcriptomic assertions, so the structured iModulonDB adapter is not applicable.
    Biosynthetic genes found in newly inspected papers are not converted to drug-target
    assertions.
  search_scope: 2026-10-21; rg --no-ignore --hidden across data, curation, conf, scripts,
    src, docs, .claude, reviews and reports for deoxyherqueinone, CHEBI:145874, CHEBI:145901
    and VZWSSCQUCMSKLE. Public PubMed exact adopted IDs, ChEBI exact entries, PubChem
    full keys/name, original DOI/PMC/author/publisher routes; web exact queries "deoxyherqueinone"
    "pKa" and "deoxyherqueinone" "pH 7.3". Search snippets were not treated as experimental
    proof.
  snapshot_sha256: 8f08334df9735e5b830dfdc48732e94d1003d792c10572f0f03b4ddb2ead42aa
- evidence_id: validation
  kind: validation
  reference: 355-schema.log;355-strict.log;355-chemistry.json;355356-chemistry-check.json
  locator: Actual focused validation outputs and unchanged input-byte verification.
  accessed_at: '2026-10-21T14:31:47Z'
  support: supports
  summary: Schema and strict checks exit 0. The explicit charge-aware chemistry comparison
    exits 0. The original thirteen captured input hashes remain unchanged. The anion
    generic-helper failure is retained with its corrected interpretation; the neutral
    generic helper passes. These deterministic results do not establish biological
    mechanism or clinical efficacy.
  snapshot_sha256: 8e032a75193627d684ba5879667880dd57a6240a86788f6761eb9ecb5f143a42
assessments:
- assessment_id: identity
  area: identity
  topic: Exact protonation, stereochemistry, names and registry scope
  outcome: supported
  summary: The explicit 4-olate graph, charge, formula, masses and assigned R centre
    agree with current ChEBI and the native systematic name. Its parent label is deliberately
    related, not an exact equivalence. Do not merge it with the neutral record.
  target_ids:
  - CHEBI:145874
  evidence_ids:
  - native
  - authority
  - chemistry
  - validation
- assessment_id: activity
  area: evidence
  topic: Antibacterial role and exact experimental material
  outcome: unknown
  summary: The native antibacterial role is a faithful ChEBI assertion. Original positive
    data concern named parent deoxyherqueinone; the inspected studies do not establish
    a separately tested 4-olate reagent, its fraction in assay medium or an ion-specific
    potency. This limits independent exact-form support without proving the role false.
  target_ids:
  - CHEBI:145874
  evidence_ids:
  - authority
  - antibacterial1965
  - isolation2001
  - origin1972
- assessment_id: mechanism
  area: evidence
  topic: Microspecies statement, fungal provenance and biosynthetic context
  outcome: unknown
  summary: The pH 7.3 statement is source-attested but was not independently verified.
    The sole adopted 2017 paper and inspected supplement concern neutral-product biosynthesis
    and a different precursor pKa. They do not identify an antimicrobial target or
    establish exact-ion speciation.
  target_ids:
  - CHEBI:145874
  evidence_ids:
  - authority
  - origin1972
  - biosynthesis2017
  - biosynthesis-si
  - isolation2001
- assessment_id: provenance
  area: provenance
  topic: Generated ownership, source history, citation disposition and optional fields
  outcome: supported
  summary: The entire record and actual maintained row/code were inspected. Original
    hashes and seed history are preserved; source mints reproduce. Missing optional
    quantitative activity, producer object, molecular target, resistance, clinical
    status or graph is not a defect by itself. No scientific-status promotion follows
    from passing checks.
  target_ids:
  - CHEBI:145874
  evidence_ids:
  - native
  - owners
  - search
  - validation
findings:
- finding_id: F1
  issue_key: deoxyherqueinone-4-olate-microspecies-evidence-scope
  category: evidence
  severity: informational
  status: open
  certainty: confirmed
  title: Trace the exact 4-olate microspecies provenance before treating parent data
    as ion-specific evidence
  description: The native definition faithfully repeats ChEBI that this 4-olate is
    the major microspecies at pH 7.3. The sole adopted paper instead predicts a pKa
    for precursor 6a and depicts neutral deoxyherqueinone 10 in biosynthesis. The
    additional antibacterial papers concern the named parent without separately established
    ionic material or assay speciation. This identifies the inspected evidence boundary,
    not a demonstrated error in the ChEBI prediction or proof of inactivity. A traceable
    exact-structure model or measurement would resolve the question.
  target_ids:
  - CHEBI:145874
  field_paths:
  - definition
  - activity_roles
  evidence_ids:
  - authority
  - biosynthesis2017
  - biosynthesis-si
  - antibacterial1965
  - search
  rule_id: Review checklist exact chemical form and claim-specific evidence; database
    assertions retain their provenance
  native_severity: informational
  normalization_reason: The chemical identity and faithful source import are supported.
    No inspected source positively contradicts the claimed microspecies predominance,
    so a bounded provenance question does not justify a corrective major or automatic
    exclusion.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted microspecies definition and role
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Exact ChEBI definition and citation extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible generated definition and source qualification
actions:
- action_id: A1
  description: Resolve the exact-structure microspecies provenance in the maintained
    source qualification before adding ion-specific mechanism or activity evidence.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:145874
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted microspecies definition and role
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Exact ChEBI definition and citation extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible generated definition and source qualification
  acceptance_checks:
  - Identify the actual prediction or measurement for the native 4-olate and neutral
    parent, recording structural tautomer, protonation site, conditions and method/version.
    Do not reuse the 2017 precursor 6a pKa as a result for compound 10.
  - If adding antibacterial evidence, preserve tested material, assay pH and any measured
    or modeled speciation; do not relabel parent MICs as separately measured 4-olate
    activity.
  - Retain the source-attested claim with explicit provenance while uncertainty persists.
    Only qualify or correct generated wording if additional exact evidence warrants
    it, then rerun focused schema, strict and charge-aware chemistry checks.
limitations:
- The 1965 original paper was read completely, including its table, but reports little
  assay-method or material characterization detail. Its named-parent antibacterial
  results do not independently establish a discrete ionic reagent, modern strain-specific
  susceptibility or a mechanistic target.
- The 2001 paper was read completely from scanned pages. Its deoxyherqueinone assignment
  uses NMR, MS and derivatization; absolute configuration is not independently established
  by its unwedge drawing. The 1972 paper was read completely as text, but its derivative
  isolation does not amount to purification of the free parent from that culture.
- The 2017 main text and Figure 2 were inspected; supporting information review was
  limited to S4–S7, S20 and S50, with the two specified figures viewed. Raw spectra,
  chromatographic integrations and all calculations were not reprocessed. Initial
  PMC supplement access returned an HTML challenge and direct ACS returned 403; the
  verified public publisher Figshare PDF supplied the assessed supplement.
- No independent exact 4-olate pKa/speciation source was established in the bounded
  search. The pH 7.3 assertion remains ChEBI-attested; lack of an inspected primary
  determination is not proof it is chemically false.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Both records retain a single R stereocentre. Their principal distinction is protonation,
  not a stereochemical variant. Optional enrichment remains separate from corrective
  curation.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
