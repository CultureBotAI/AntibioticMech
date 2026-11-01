# 4-Hydroxy-2-oxobutanal: coherent identity and qualified historical activity support

- Review: 20261021T074724Z-4-hydroxy-2-oxobutanal
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T07:37:35Z
- Finished UTC: 2026-10-21T07:47:24Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Identity, chemistry, broader parents and source provenance are coherent. Primary abstracts support vitamin C degradation and identify a historical bacterial-growth inhibitor as this ketoaldehyde, with identification and assay limitations retained. Focused schema, strict and chemistry pass. One informational follow-up concerns obtaining the original assay details and adding qualified evidence; no quantitative activity, mechanism or biosynthetic producer is invented. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole exact native record, maintained source ownership, all source identifiers and six primary citation abstracts; bounded attempts to retrieve original full texts.

Selection: Queue index043, CHEBI:144586 at its locked native path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:144586 | data/antibiotics/antibacterial/4-hydroxy-2-oxobutanal.yaml | generated | 4-hydroxy-2-oxobutanal |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused LinkML validation | passed | True | CHEBI:144586 | No issues found. |
| Focused strict validation | passed | True | CHEBI:144586 | Scanned one file; zero ERROR rows. |
| Independent native chemistry and minted identifier | passed | False | CHEBI:144586 | Both representations reproduce full key, formula, charge, rounded masses and mint. |
| Structured source coverage | passed | False | CHEBI:144586 | Dataset inventory request succeeded; no human, spinach or Arabidopsis dataset applies to the primary degradation/protein-repair contexts. |
| Expression-module applicability | not_applicable | False | CHEBI:144586 | The record asserts no bacterial gene, target or transcriptomic dataset. The plant enzyme in one citation is a protein-repair catalyst, not a demonstrated antimicrobial target; its heterologous E.coli expression does not create an applicable bacterial response claim. |
| Original full-text retrieval | unavailable | False | CHEBI:144586 | 1969 original scanned text could not be retrieved from PMC/PNAS/EuropePMC: browser challenge or403. The2011 full-text XML route returned500; publisher/PMC opens were blocked. Only inspected official abstracts support the bounded biological assessment. |
| Independent registry endpoint | unavailable | False | CHEBI:144586 | NIST did not yield an inspectable entry. CAS28119-61-1 is corroborated by ChEBI and official PubChem synonyms, without claiming independent CAS-registry inspection. |
| Authoritative full QC | failed | True | CHEBI:144586 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:144586 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:144586 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:144586 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:144586 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:144586 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:144586 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:144586 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:144586 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact ketoaldehyde identity

identity: supported. Targets: CHEBI:144586.

Native structure, synonyms, official ChEBI, PubChem and independent chemistry agree. Distinct dicarbonyls and analytical derivatives are kept separate.

### Broader classes and CAS

grounding: supported. Targets: CHEBI:144586.

Both parent classes fit the functionality; CAS is corroborated as a source assertion by ChEBI and PubChem, with independent registry access limited.

### Vitamin C degradation

evidence: supported. Targets: CHEBI:144586.

The exact3-deoxythreosone primary study supports the degradation-product definition; no exclusive precursor or microbial biosynthetic origin is asserted.

### Historical antibacterial role

evidence: supported. Targets: CHEBI:144586.

The primary abstract supports historical identification of a bacterial-growth inhibitor as this ketoaldehyde, qualified by derivative-based structural identification. Quantitative assay scope remains unresolved because full text was inaccessible.

### Exact antibacterial mechanism

evidence: unknown. Targets: CHEBI:144586.

The native record asserts no mechanism. Glycation, plant protein repair and activity of related dicarbonyls cannot establish its direct bacterial target.

### Producer, resistance, clinical and graph fields

representation: not_applicable. Targets: CHEBI:144586.

No native objects require correction. HeLa-culture isolation, human plasma/lens detection and degradation chemistry are not sufficient to assert biosynthetic producers or clinical efficacy.

### Qualified primary evidence opportunity

completeness: supported. Targets: CHEBI:144586.

A curator can add the historical evidence and degradation support; exact assay normalization requires the original report and possibly its cited earlier assay paper.

### Maintained source and status

ownership: supported. Targets: CHEBI:144586.

Source row, configuration, source transforms, mint, version and history agree; all captured hashes remain unchanged. Scientific additions belong to the actual native record, without status promotion by this review.

### Focused checks

schema: supported. Targets: CHEBI:144586.

Schema, strict and chemistry pass independently of the bounded scientific assessment.

## Findings

### F1: Historical antibacterial and degradation evidence can be added with explicit access and scope limits

informational / open / confirmed; issue key: chebi-144586-historical-assay-evidence-followup.

The seed is consistent with official identity and qualified primary-abstract support. Optional evidence is unrepresented; obtaining the1969 report and underlying assay details would permit careful activity curation. No unsupported numerical potency or direct-target assertion is presently in the record.

## Recommended Actions And Acceptance Checks

### A1

If selected for curation, retrieve the original1969 identification/assay text and add primary evidence with its exact identification and biological scope, alongside the vitamin-C-degradation support.

- Confirm exact tested preparation, bacterial species/strain, assay endpoint, dose and conditions from inspectable original text before populating quantitative activity.
- Retain the derivative-based identification qualification; distinguish the free compound from DNPH/quinoxaline derivatives and neighboring dicarbonyls.
- Do not infer direct bacterial targets from plant protein-repair or human glycation studies, or biosynthetic producers from culture/tissue isolation.
- Do not claim absent worldwide mechanism/activity evidence from these bounded retrieval limits.
- Use write_validated_antibiotic with native curation history for separately authorized scientific additions; rerun focused schema/strict and required corpus gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/4-hydroxy-2-oxobutanal.yaml; Entire YAML: definition, four synonyms, parents, role, chemistry, CAS xref, source concept and three history events. | supports | The SEEDED/EXACT record denotes one neutral achiral C4H6O3 ketoaldehyde. Its only biological assertions are antibacterial role/class and vitamin-C-degradation provenance. It asserts no quantitative activity, molecular target, producer, resistance, clinical, causal-graph or dataset objects; these optional omissions are not required-field defects. |
| owner | data/raw/chebi_antimicrobials.tsv; CHEBI:144586 row2665; raw MANIFEST and PATHS; conf/sources.yaml; ChEBI extractor and seeder source reader/build_record/mint. | supports | The adopted row matches the entire native identity and role. Six PMIDs are source leads, mechanism_role_ids is empty, and the deterministic mint antibioticmech:chebi-60da6f242a is reproduced. Version2026-08-30 and three seeder history events are coherent. All initial captured hashes were rechecked unchanged. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:144586; Complete official ChEBI page, native-source row, and PubChem CID193090 official PUG responses043-pubchem.json/043-pubchem-synonyms.json. | supports | ChEBI matches all four synonyms, neutral formula, full structure strings, key CUSSNCHZLYDUPJ-UHFFFAOYSA-N and masses. CHEBI:27659 is2-oxo aldehyde,55380 beta-hydroxy ketone and33282 antibacterial agent; the broader classes and role are correctly separated. CAS28119-61-1 is present in both ChEBI and PubChem synonyms, and PubChem reproduces the exact native InChI/key. NIST endpoint was not inspectable. |
| chemistry | RDKit native calculation; 043-chemistry.py and043-chemistry.json. | supports | SMILES and InChI independently parse to the same one-fragment, neutral achiral C4H6O3 entity, average mass102.089 and exact mass102.031694052; full key and source mint match. |
| activity | PMID:5264149; DOI:10.1073/pnas.64.3.920; official Europe PMC abstract in043-epmc.json and PubMed/PMC abstract. | supports | Sparkes and Kenny identify a bacterial-growth inhibitor from human cell cultures as a ketoaldehyde. Infrared spectra of DNPH derivatives suggested4-hydroxy-2-ketobutyraldehyde; the synthesized compound gave matching derivatives. This provides qualified historical support for the antibacterial role. The inspected abstract does not supply assay strain, dose, endpoint, direct molecular target or proof of biosynthetic origin. |
| degradation | PMID:21885436; DOI:10.1074/jbc.M111.245100; official abstract in043-epmc.json. | supports | The human-lens study identifies free/protein-bound vitamin-C-degradation products using o-phenylenediamine trapping;3-deoxythreosone is the most abundant measured water-soluble-protein-associated dicarbonyl. Its primary abstract supports the native degradation-product statement. It does not establish antibacterial mechanism or a microbial producer. |
| literature | Europe PMC official metadata and abstracts; 043-epmc.json: PMID15705060,19422225,19711949,21885436,25164824,5264149. | context_only | All six identifiers resolve and all abstracts were inspected. PMID19422225 and19711949 identify this exact compound among Maillard degradation intermediates;25164824 includes it in a plasma dicarbonyl panel. PMID15705060 concerns plant ribulosamine/erythrulosamine3-kinase and deglycation chemistry, not antibacterial target inhibition. Derivative identification, formation chemistry and human abundance do not imply direct bacterial targets. |
| access | Free official full-text routes; PMC223322 article/scannedPDF and page variants, PNAS DOI PDF, EuropePMC pdf=render and backend/ptpmcrender routes; PMC3199460 and EuropePMC fullTextXML. | context_only | Reasonable public retrieval attempts returned browser challenges,403 or500; no complete1969 or2011 full text was obtained or claimed inspected. Paid document delivery was not used. Search excerpts from full pages were treated only as leads. |
| adapter | https://imodulondb.org/api/datasets; Actual kg-microbe-sources output043-imodulondb-datasets.txt. | context_only | No covered Homo sapiens, Spinacia/spinach or Arabidopsis organism matches the cited degradation/protein-repair contexts. No native microbial expression claim is asserted; E.coli as enzyme-expression host is not evidence of antimicrobial response. No term search or component summary was warranted. |
| search | CultureBotAI/AntibioticMech; 043-local-hits.txt;043-focused-local-hits.txt; exact-name/synonym and original-paper discovery. | context_only | Inclusive repository search located native, source, generated and historical references; focused curation/reviews/historical-review/conf search returned no exact matches outside queue. Historical reports and supplier paraphrases were not used as proof. Free primary discovery was bounded and does not establish universal absence of further activity or mechanism evidence. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Native identity, evidence, activity, mechanism, producer and status rules; CURATION/HARMONIZATION. | supports | Optional omissions are not required-field defects. Source support must retain its identification and assay scope; isolation from cells is not biosynthesis proof. A protein-repair enzyme or another dicarbonyl’s activity is not the exact compound’s antibacterial target. |
| validation | Documented per-record validators; Actual worktree005 commands and043-strict.tsv. | supports | Schema and strict exited0, and independent chemistry exited0. Actual shared corpus checks are recorded separately. |

## Limits And Additional Notes

- All six adopted primary abstracts and identifiers were inspected. No complete1969 antibacterial paper or2011 lens-study full text was obtained after reasonable free official attempts; assay details and exact-compound antibacterial mechanism remain unresolved.
- Historical growth-inhibitor identity is based on the abstract’s derivative comparison and tentative infrared assignment, not a newly verified full modern structure/activity experiment.
- CAS is corroborated through ChEBI and official PubChem; independent NIST/CAS-registry inspection was unavailable.
- Structured adapter coverage has no matching plant/human dataset; absence from it is not negative evidence. The source search is bounded and does not establish absence of other mechanisms, activity observations or biosynthetic studies.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T074724Z-4-hydroxy-2-oxobutanal
kind: record
repository: CultureBotAI/AntibioticMech
title: '4-Hydroxy-2-oxobutanal: coherent identity and qualified historical activity
  support'
started_at: '2026-10-21T07:37:35Z'
finished_at: '2026-10-21T07:47:24Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the record. Provenance was captured
    before assessment; entire native record and maintained source row, source transforms,
    authority identifiers, all adopted primary abstracts and independent chemistry
    were inspected.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: Identity, chemistry, broader parents and source provenance are coherent.
  Primary abstracts support vitamin C degradation and identify a historical bacterial-growth
  inhibitor as this ketoaldehyde, with identification and assay limitations retained.
  Focused schema, strict and chemistry pass. One informational follow-up concerns
  obtaining the original assay details and adding qualified evidence; no quantitative
  activity, mechanism or biosynthetic producer is invented. Scientific assessment
  retains the stated evidence limits; full verification is blocked by the shared native-library
  failure.
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
  - path: data/antibiotics/antibacterial/4-hydroxy-2-oxobutanal.yaml
    sha256: 3700107476f09e5c227fa15adf2dc305af5fd21c0f765d5dfcc3db141ee01f29
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
- target_id: CHEBI:144586
  path: data/antibiotics/antibacterial/4-hydroxy-2-oxobutanal.yaml
  label: 4-hydroxy-2-oxobutanal
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
  description: Whole exact native record, maintained source ownership, all source
    identifiers and six primary citation abstracts; bounded attempts to retrieve original
    full texts.
  selection: Queue index043, CHEBI:144586 at its locked native path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:144586
  exclusions:
  - target: Threosone, 1-deoxythreosone, methylglyoxal, glyoxal, derivatized quinoxalines
      and DNPH adducts
    reason: Distinct compounds or analytical derivatives; their mechanism or activity
      is not transferred to the native free ketoaldehyde.
checks:
- check_id: schema
  name: Focused LinkML validation
  status: passed
  required: true
  summary: No issues found.
  target_ids:
  - CHEBI:144586
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/4-hydroxy-2-oxobutanal.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict validation
  status: passed
  required: true
  summary: Scanned one file; zero ERROR rows.
  target_ids:
  - CHEBI:144586
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/4-hydroxy-2-oxobutanal.yaml --out /private/tmp/am-review-session/043-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: Independent native chemistry and minted identifier
  status: passed
  required: false
  summary: Both representations reproduce full key, formula, charge, rounded masses
    and mint.
  target_ids:
  - CHEBI:144586
  evidence_ids:
  - chemistry
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/043-chemistry.py
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter
  name: Structured source coverage
  status: passed
  required: false
  summary: Dataset inventory request succeeded; no human, spinach or Arabidopsis dataset
    applies to the primary degradation/protein-repair contexts.
  target_ids:
  - CHEBI:144586
  evidence_ids:
  - adapter
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 datasets
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-scope
  name: Expression-module applicability
  status: not_applicable
  required: false
  summary: The record asserts no bacterial gene, target or transcriptomic dataset.
    The plant enzyme in one citation is a protein-repair catalyst, not a demonstrated
    antimicrobial target; its heterologous E.coli expression does not create an applicable
    bacterial response claim.
  target_ids:
  - CHEBI:144586
  evidence_ids:
  - adapter
  - literature
- check_id: full-text
  name: Original full-text retrieval
  status: unavailable
  required: false
  summary: '1969 original scanned text could not be retrieved from PMC/PNAS/EuropePMC:
    browser challenge or403. The2011 full-text XML route returned500; publisher/PMC
    opens were blocked. Only inspected official abstracts support the bounded biological
    assessment.'
  target_ids:
  - CHEBI:144586
  evidence_ids:
  - activity
  - degradation
  - access
- check_id: cas
  name: Independent registry endpoint
  status: unavailable
  required: false
  summary: NIST did not yield an inspectable entry. CAS28119-61-1 is corroborated
    by ChEBI and official PubChem synonyms, without claiming independent CAS-registry
    inspection.
  target_ids:
  - CHEBI:144586
  evidence_ids:
  - identity
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:144586
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
  - CHEBI:144586
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
  - CHEBI:144586
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
  - CHEBI:144586
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
  - CHEBI:144586
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
  - CHEBI:144586
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
  - CHEBI:144586
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
  - CHEBI:144586
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
  - CHEBI:144586
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/4-hydroxy-2-oxobutanal.yaml
  locator: 'Entire YAML: definition, four synonyms, parents, role, chemistry, CAS
    xref, source concept and three history events.'
  accessed_at: '2026-10-21T07:41:24Z'
  support: supports
  summary: The SEEDED/EXACT record denotes one neutral achiral C4H6O3 ketoaldehyde.
    Its only biological assertions are antibacterial role/class and vitamin-C-degradation
    provenance. It asserts no quantitative activity, molecular target, producer, resistance,
    clinical, causal-graph or dataset objects; these optional omissions are not required-field
    defects.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: CHEBI:144586 row2665; raw MANIFEST and PATHS; conf/sources.yaml; ChEBI
    extractor and seeder source reader/build_record/mint.
  accessed_at: '2026-10-21T07:41:24Z'
  support: supports
  summary: The adopted row matches the entire native identity and role. Six PMIDs
    are source leads, mechanism_role_ids is empty, and the deterministic mint antibioticmech:chebi-60da6f242a
    is reproduced. Version2026-08-30 and three seeder history events are coherent.
    All initial captured hashes were rechecked unchanged.
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:144586
  locator: Complete official ChEBI page, native-source row, and PubChem CID193090
    official PUG responses043-pubchem.json/043-pubchem-synonyms.json.
  accessed_at: '2026-10-21T07:41:24Z'
  support: supports
  summary: ChEBI matches all four synonyms, neutral formula, full structure strings,
    key CUSSNCHZLYDUPJ-UHFFFAOYSA-N and masses. CHEBI:27659 is2-oxo aldehyde,55380
    beta-hydroxy ketone and33282 antibacterial agent; the broader classes and role
    are correctly separated. CAS28119-61-1 is present in both ChEBI and PubChem synonyms,
    and PubChem reproduces the exact native InChI/key. NIST endpoint was not inspectable.
- evidence_id: chemistry
  kind: validation
  reference: RDKit native calculation
  locator: 043-chemistry.py and043-chemistry.json.
  accessed_at: '2026-10-21T07:41:24Z'
  support: supports
  summary: SMILES and InChI independently parse to the same one-fragment, neutral
    achiral C4H6O3 entity, average mass102.089 and exact mass102.031694052; full key
    and source mint match.
  snapshot_sha256: a9681493bdb7c10bc2b572ec7f8b49d05bcb289a3e9cd39dd8fce3445219cd20
- evidence_id: activity
  kind: primary_source
  reference: PMID:5264149
  locator: DOI:10.1073/pnas.64.3.920; official Europe PMC abstract in043-epmc.json
    and PubMed/PMC abstract.
  accessed_at: '2026-10-21T07:41:24Z'
  support: supports
  summary: Sparkes and Kenny identify a bacterial-growth inhibitor from human cell
    cultures as a ketoaldehyde. Infrared spectra of DNPH derivatives suggested4-hydroxy-2-ketobutyraldehyde;
    the synthesized compound gave matching derivatives. This provides qualified historical
    support for the antibacterial role. The inspected abstract does not supply assay
    strain, dose, endpoint, direct molecular target or proof of biosynthetic origin.
- evidence_id: degradation
  kind: primary_source
  reference: PMID:21885436
  locator: DOI:10.1074/jbc.M111.245100; official abstract in043-epmc.json.
  accessed_at: '2026-10-21T07:41:24Z'
  support: supports
  summary: The human-lens study identifies free/protein-bound vitamin-C-degradation
    products using o-phenylenediamine trapping;3-deoxythreosone is the most abundant
    measured water-soluble-protein-associated dicarbonyl. Its primary abstract supports
    the native degradation-product statement. It does not establish antibacterial
    mechanism or a microbial producer.
- evidence_id: literature
  kind: primary_source
  reference: Europe PMC official metadata and abstracts
  locator: '043-epmc.json: PMID15705060,19422225,19711949,21885436,25164824,5264149.'
  accessed_at: '2026-10-21T07:41:24Z'
  support: context_only
  summary: All six identifiers resolve and all abstracts were inspected. PMID19422225
    and19711949 identify this exact compound among Maillard degradation intermediates;25164824
    includes it in a plasma dicarbonyl panel. PMID15705060 concerns plant ribulosamine/erythrulosamine3-kinase
    and deglycation chemistry, not antibacterial target inhibition. Derivative identification,
    formation chemistry and human abundance do not imply direct bacterial targets.
  snapshot_sha256: 755c38400c13b9a45873df66feeda8cccb9f3a72e8593687deefd26c669dadf5
- evidence_id: access
  kind: search
  reference: Free official full-text routes
  locator: PMC223322 article/scannedPDF and page variants, PNAS DOI PDF, EuropePMC
    pdf=render and backend/ptpmcrender routes; PMC3199460 and EuropePMC fullTextXML.
  accessed_at: '2026-10-21T07:41:24Z'
  support: context_only
  summary: Reasonable public retrieval attempts returned browser challenges,403 or500;
    no complete1969 or2011 full text was obtained or claimed inspected. Paid document
    delivery was not used. Search excerpts from full pages were treated only as leads.
  search_scope: Free PMC223322 and PMC3199460 article/page/PDF variants, PNAS DOI
    PDF, Europe PMC PDF/backend and fullTextXML routes; no paid or authenticated sources.
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Actual kg-microbe-sources output043-imodulondb-datasets.txt.
  accessed_at: '2026-10-21T07:41:24Z'
  support: context_only
  summary: No covered Homo sapiens, Spinacia/spinach or Arabidopsis organism matches
    the cited degradation/protein-repair contexts. No native microbial expression
    claim is asserted; E.coli as enzyme-expression host is not evidence of antimicrobial
    response. No term search or component summary was warranted.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 043-local-hits.txt;043-focused-local-hits.txt; exact-name/synonym and original-paper
    discovery.
  accessed_at: '2026-10-21T07:41:24Z'
  support: context_only
  summary: Inclusive repository search located native, source, generated and historical
    references; focused curation/reviews/historical-review/conf search returned no
    exact matches outside queue. Historical reports and supplier paraphrases were
    not used as proof. Free primary discovery was bounded and does not establish universal
    absence of further activity or mechanism evidence.
  search_scope: rg --no-ignore --hidden identifier,label,slug across worktree005 excluding.git/.venv;
    focused CHEBI:144586,CUSSNCHZLYDUPJ,4-hydroxy-2-oxobutanal,3-deoxythreosone,4-hydroxy-2-ketobutyraldehyde
    in curation,reviews,reports/yaml_record_review,conf excluding record_review_queue.tsv.
    Ignored files included. Public exact-name/antibacterial and historical title/author
    searches.
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Native identity, evidence, activity, mechanism, producer and status rules;
    CURATION/HARMONIZATION.
  accessed_at: '2026-10-21T07:41:24Z'
  support: supports
  summary: Optional omissions are not required-field defects. Source support must
    retain its identification and assay scope; isolation from cells is not biosynthesis
    proof. A protein-repair enzyme or another dicarbonyl’s activity is not the exact
    compound’s antibacterial target.
- evidence_id: validation
  kind: validation
  reference: Documented per-record validators
  locator: Actual worktree005 commands and043-strict.tsv.
  accessed_at: '2026-10-21T07:41:24Z'
  support: supports
  summary: Schema and strict exited0, and independent chemistry exited0. Actual shared
    corpus checks are recorded separately.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact ketoaldehyde identity
  outcome: supported
  summary: Native structure, synonyms, official ChEBI, PubChem and independent chemistry
    agree. Distinct dicarbonyls and analytical derivatives are kept separate.
  target_ids:
  - CHEBI:144586
  evidence_ids:
  - record
  - identity
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Broader classes and CAS
  outcome: supported
  summary: Both parent classes fit the functionality; CAS is corroborated as a source
    assertion by ChEBI and PubChem, with independent registry access limited.
  target_ids:
  - CHEBI:144586
  evidence_ids:
  - identity
- assessment_id: definition
  area: evidence
  topic: Vitamin C degradation
  outcome: supported
  summary: The exact3-deoxythreosone primary study supports the degradation-product
    definition; no exclusive precursor or microbial biosynthetic origin is asserted.
  target_ids:
  - CHEBI:144586
  evidence_ids:
  - record
  - degradation
  - literature
- assessment_id: activity
  area: evidence
  topic: Historical antibacterial role
  outcome: supported
  summary: The primary abstract supports historical identification of a bacterial-growth
    inhibitor as this ketoaldehyde, qualified by derivative-based structural identification.
    Quantitative assay scope remains unresolved because full text was inaccessible.
  target_ids:
  - CHEBI:144586
  evidence_ids:
  - activity
  - access
- assessment_id: mechanism
  area: evidence
  topic: Exact antibacterial mechanism
  outcome: unknown
  summary: The native record asserts no mechanism. Glycation, plant protein repair
    and activity of related dicarbonyls cannot establish its direct bacterial target.
  target_ids:
  - CHEBI:144586
  evidence_ids:
  - record
  - literature
  - adapter
  - rubric
- assessment_id: other
  area: representation
  topic: Producer, resistance, clinical and graph fields
  outcome: not_applicable
  summary: No native objects require correction. HeLa-culture isolation, human plasma/lens
    detection and degradation chemistry are not sufficient to assert biosynthetic
    producers or clinical efficacy.
  target_ids:
  - CHEBI:144586
  evidence_ids:
  - record
  - activity
  - degradation
  - literature
  - rubric
- assessment_id: completeness
  area: completeness
  topic: Qualified primary evidence opportunity
  outcome: supported
  summary: A curator can add the historical evidence and degradation support; exact
    assay normalization requires the original report and possibly its cited earlier
    assay paper.
  target_ids:
  - CHEBI:144586
  evidence_ids:
  - activity
  - degradation
  - access
- assessment_id: provenance
  area: ownership
  topic: Maintained source and status
  outcome: supported
  summary: Source row, configuration, source transforms, mint, version and history
    agree; all captured hashes remain unchanged. Scientific additions belong to the
    actual native record, without status promotion by this review.
  target_ids:
  - CHEBI:144586
  evidence_ids:
  - owner
  - record
  - rubric
- assessment_id: schema
  area: schema
  topic: Focused checks
  outcome: supported
  summary: Schema, strict and chemistry pass independently of the bounded scientific
    assessment.
  target_ids:
  - CHEBI:144586
  evidence_ids:
  - validation
  - chemistry
findings:
- finding_id: F1
  issue_key: chebi-144586-historical-assay-evidence-followup
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Historical antibacterial and degradation evidence can be added with explicit
    access and scope limits
  description: The seed is consistent with official identity and qualified primary-abstract
    support. Optional evidence is unrepresented; obtaining the1969 report and underlying
    assay details would permit careful activity curation. No unsupported numerical
    potency or direct-target assertion is presently in the record.
  target_ids:
  - CHEBI:144586
  field_paths:
  - evidence
  - activity_spectrum
  - mode_of_action_notes
  evidence_ids:
  - record
  - activity
  - degradation
  - access
  - rubric
  rule_id: 'native-review-checklist: Activity and Evidence'
  native_severity: informational optional enrichment and bounded evidence-access gap
  normalization_reason: No current false quantitative claim, wrong structure or missing
    required field is established.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/4-hydroxy-2-oxobutanal.yaml
    role: Curator-owned scientific additions through write_validated_antibiotic and
      native curation history
actions:
- action_id: A1
  description: If selected for curation, retrieve the original1969 identification/assay
    text and add primary evidence with its exact identification and biological scope,
    alongside the vitamin-C-degradation support.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:144586
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/4-hydroxy-2-oxobutanal.yaml
    role: Curator-owned scientific additions through write_validated_antibiotic and
      native curation history
  acceptance_checks:
  - Confirm exact tested preparation, bacterial species/strain, assay endpoint, dose
    and conditions from inspectable original text before populating quantitative activity.
  - Retain the derivative-based identification qualification; distinguish the free
    compound from DNPH/quinoxaline derivatives and neighboring dicarbonyls.
  - Do not infer direct bacterial targets from plant protein-repair or human glycation
    studies, or biosynthetic producers from culture/tissue isolation.
  - Do not claim absent worldwide mechanism/activity evidence from these bounded retrieval
    limits.
  - Use write_validated_antibiotic with native curation history for separately authorized
    scientific additions; rerun focused schema/strict and required corpus gates.
limitations:
- All six adopted primary abstracts and identifiers were inspected. No complete1969
  antibacterial paper or2011 lens-study full text was obtained after reasonable free
  official attempts; assay details and exact-compound antibacterial mechanism remain
  unresolved.
- Historical growth-inhibitor identity is based on the abstract’s derivative comparison
  and tentative infrared assignment, not a newly verified full modern structure/activity
  experiment.
- CAS is corroborated through ChEBI and official PubChem; independent NIST/CAS-registry
  inspection was unavailable.
- Structured adapter coverage has no matching plant/human dataset; absence from it
  is not negative evidence. The source search is bounded and does not establish absence
  of other mechanisms, activity observations or biosynthetic studies.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
