# Isopatulin: supported lactol identity and bounded antibacterial evidence

- Review: 20261021T190218Z-isopatulin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T18:41:49Z
- Finished UTC: 2026-10-21T19:02:18Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Native isopatulin chemistry agrees with current authorities and the original synthesis supplement. Exact primary patent experiments support antibacterial activity, independently of patulin and the pintulin derivative. One minor inherited typo remains in the definition. The unassigned lactol centre, solution equilibrium, unverified Aspergillus production scope and inaccessible historical main texts limit full scientific sign-off.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position566; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:145111 | data/antibiotics/antibacterial/isopatulin.yaml | generated | isopatulin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:145111 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:145111 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:145111 | Actual focused execution exited 0. |
| Independent authority and primary drawing comparison | passed | False | CHEBI:145111 | Six native/current authority encodings agree; independently reconstructed original supplement/patent drawing also matches the native complete key. |
| Structured-source applicability | not_applicable | False | CHEBI:145111 | The fully read native has no protein, gene, regulator, pathway, expression or mechanistic assertion. Optional PheRS work remains a scoped literature lead, not a new native target. |
| Authoritative full QC | failed | True | CHEBI:145111 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:145111 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:145111 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:145111 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:145111 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:145111 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:145111 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:145111 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:145111 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact cyclic structure with unspecified lactol stereochemistry

identity: supported. Targets: CHEBI:145111.

Independent authorities and original drawings support the native cyclic constitution and names. Dynamic solution equilibrium and unassigned configuration remain explicit; neither proves a defective native graph.

### Structural parents and chemical references

grounding: supported. Targets: CHEBI:145111.

All three structural parents fit. CAS name/key lookups agree with native; direct CAS and MetaCyc verification remain limited rather than falsely declared complete.

### Antibacterial role separated from toxin/derivative experiments

evidence: supported. Targets: CHEBI:145111.

Exact isolated compound is active in the inspected patent agar assays and is named in the later original antibacterial abstract. Patulin detection, pintulin cytotoxicity and dehydroisopatulin animal results are not transferred.

### Definition wording and producer precision

nomenclature: concern. Targets: CHEBI:145111.

The chemical description is coherent apart from the minor an/and typo. Penicillium production is supported; exact Aspergillus production remains unverified within the bounded primary audit.

### Optional biosynthetic and target enrichment

completeness: unknown. Targets: CHEBI:145111.

The native asserts no target. Patent and abstract PheRS leads do not justify a complete causal mechanism, and fungal biosynthetic enzymes are not bacterial drug targets. Original source access and solution-material boundaries constrain further enrichment.

### Source and history ownership

provenance: supported. Targets: CHEBI:145111.

All thirteen initial hashes, actual ChEBI source ownership, source mint and three history events are preserved; no native changes were made.

## Findings

### F1: Correct the inherited conjunction typo in the structural definition

minor / open / confirmed; issue key: isopatulin-definition-an-for-and-typo.

The definition says positions4 an6 rather than positions4 and6. The chemical meaning is recoverable and the graph is valid; correct the source-owned prose through maintained extraction/regeneration.

## Recommended Actions And Acceptance Checks

### A1

Correct the source definition conjunction reproducibly.

- Regenerated definition uses positions4 and6 while retaining the exact structural meaning, formula/key and source attribution.
- Apply the maintained source correction without manually patching generated YAML; pass focused schema/strict and required source/history/reproduction checks.

### A2

Retain experimental boundaries in any optional scientific enrichment.

- Verify exact Aspergillus production before adding a strain-specific producer; generic patulin-cluster membership is not a substitute for exact metabolite evidence.
- Keep patent-reported MICs, media and original units distinct from later enzyme inhibition and host cytotoxicity; resolve the patent comparator inconsistency before importing comparison claims.
- Keep cyclic isopatulin and its measured solution equilibrium, patulin and pintulin distinct; do not assert a pure enantiomer or direct cellular target from an unassigned graph or an abstract.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/isopatulin.yaml; Entire record, definition, three names, three parents, antibacterial role, full chemistry, two xrefs, source concept and all three history events. | supports | The SEEDED/EXACT entry denotes neutral C7H6O4 with key ZGBMSNKHUHZKEP-UHFFFAOYSA-N and one unassigned lactol tetrahedron. It is distinct from patulin and the substituted pintulin derivative. No quantitative activity, direct target, resistance, clinical use, structured producer or causal graph is asserted. The definition contains the inherited typo positions4 an6. |
| owners | data/raw/chebi_antimicrobials.tsv:2674;data/raw/chebi_role_names.tsv;conf/sources.yaml;scripts/extract_source_inventory.py;scripts/seed_from_sources.py; Complete exact maintained ChEBI row, initial/owner searches and extraction/role/seeding branches. | supports | The actual ChEBI row supplies all populated scientific fields and four adopted PMIDs. All thirteen original inputs already include the actual owners and remain unchanged. The source mint and three chronological seed/reseed events agree. The definition typo is source-owned, so a correction must survive regeneration. |
| chemistry | 566-chemistry.json;566-authority-chemistry.json;566-drawing-check.json; Native SMILES/InChI, current ChEBI encodings, PubChem155497 and independently typed primary drawing. | supports | Six native/authority encodings reproduce the complete native key, formula, zero charge and one unassigned centre. Formula and both masses pass. An independently typed graph from the actual original2009 supplement and patent structure matches reciprocally and by full key. No salt, open-chain equilibrium form, assigned enantiomer or patulin positional isomer is silently substituted. |
| terms | CHEBI:145111;CHEBI:37581;CHEBI:38131;CHEBI:74927;CHEBI:33282; Complete current exact entry and definitions for gamma-lactone, lactol, furopyran and antibacterial agent. | supports | The native five-membered lactone, cyclic hemiacetal and ortho-fused furan/pyran skeleton fit all three parents and the systematic names. Current ChEBI repeats the same unassigned structure and neopatulin alias. Unassigned stereochemistry alone is not proof of a racemate; solution interconversion is assessed separately. |
| xref | cas:70402-10-7;metacyc.compound:CPD-16725;PubChem155497; Current ChEBI reference attribution, exact PubChem CAS/full-key requests and direct BioCyc page. | supports | Both exact CAS and full-key queries resolve PubChem155497 with native chemistry. Direct CAS API returned401; the public shell did not supply an independently inspected registry graph. The MetaCyc page requires login, so exact CPD-16725 structure verification remains unavailable; current ChEBI repeats the accession. These are explicit access limitations rather than evidence that either native link is wrong. |
| adopted1992 | PMID:1518888; Complete indexed original abstract and metadata; original main not retrieved. | supports | The study compares patulin and five analogues including isopatulin in L1210/P388 cells and animal tumour models. Its broad animal response is specifically attributed to dehydroisopatulin, so that derivative’s dose/efficacy is not transferred to native isopatulin. This is host cytotoxicity context, not bacterial susceptibility evidence. |
| adopted1989 | PMID:2605253;DOI:10.1021/bi00449a035; Complete available indexed abstract, explicitly truncated by the provider at250 words; original main403. | supports | Penicillium patulum extracts epoxidize hydroquinone substrates and further convert phyllostine to neopatulin. Reported epoxidation kinetics concern upstream substrates, not an antibacterial target or isopatulin potency. The abstract supports biosynthetic context without reconstructing missing methods or stereochemistry. |
| adopted2019 | PMID:30680886;DOI:10.1111/1462-2920.14542; Complete original indexed abstract and metadata; publisher main403. | supports | The Penicillium expansum study dissects the15-gene patulin cluster and verifies functions for eight pathway enzymes. The accessible abstract does not establish a separate Aspergillus isopatulin isolation experiment or exact isopatulin antibacterial mechanism. No inferred enzyme target or strain-specific producer object is added. |
| synthesis | PMID:19583231;DOI:10.1021/jo900855e;DOI:10.1021/jo900855e.s001; Complete indexed abstract; verified original publisher supplement, actual pagesS14/S15 viewed and exact image drawings independently reconstructed. | supports | The synthesis routes through ascladiol oxidation to isopatulin. ActualS14 shows open-chain17-Z/17-E interconversion with cyclic isopatulin3;S15 explicitly describes the equilibrium in chloroform-d after recrystallization and displays proton/carbon spectra with the matching cyclic drawing. This supports the native constitution while limiting claims of one solution species. The main PDF remained403; raw spectral integration and a complete reassignment were not performed. |
| patent-material | https://patents.google.com/patent/CN103255061A/en; Original patent description and Examples1/2 through public Chinese text/English machine translation; actual structural image inspected. | supports | The patent isolates named isopatulin from Penicillium griseofulvum CPCC400528, deposited as CGMCC5752, as a colorless oil. The original drawing and formulaC7H6O4 match native; reported NMR text is not independently reprocessed, and no purity or enantiomeric-composition value is inferred. This is exact source material, distinct from patulin or a co-isolated derivative. |
| patent-activity | CN103255061A Example2 and Table1; Complete agar-dilution methods and both actual Table1 image panels read. | supports | The patent tests isolated material using MH or7H11 agar at pH7.2–7.4, approximately10^4 CFU per spot,37°C and16–48h for ordinary bacteria or3–4weeks for tuberculosis. MIC is complete growth inhibition. Actual Table1 reports isopatulin64 µg/mL for S.aureus ATCC29213,16 for E.coli ATCC25922 and8 for M.tuberculosis H37Rv. Its method prose names rifampicin while the table heading names levofloxacin, with rifampicin explicitly noted for H37Rv; that comparator inconsistency is retained. These are patent-reported strain-specific measurements, not independently replicated clinical efficacy or broad safety. |
| primary2016 | DOI:10.1080/23312009.2016.1181536; Original publisher-indexed abstract and exact-compound scope; direct full HTML/PDF403. | supports | The study isolates named isopatulin among six compounds from the same CPCC400528 strain and reports PheRS inhibition and moderate-to-weak H37Rv activity for selected compounds including isopatulin. Only the accessible abstract is used here: no uninspected numerical IC50, docking contact, selectivity or target causality is adopted. The native contains no molecular target, and enzyme inhibition alone would not prove the sole cellular cause of growth inhibition. |
| pintulin | PMID:8968391;DOI:10.7164/antibiotics.49.985; Original five-page main converted text read, particularly isolation/comparison discussion and biological endpoint scope; image tables not independently digitized. | supports | The paper reports co-isolation of isopatulin from Penicillium vulpinum F-4148 and compares it with the larger pintulin derivative. Its tested cytocidal and weak antimicrobial endpoints principally concern pintulin and are not transferred to isopatulin. The authors describe optical inactivity by reference to the earlier1979 report; that secondary citation does not independently establish the native sample’s enantiomeric composition. |
| producer-scope | definition;PMID:2605253;PMID:30680886;PMID:8968391;CN103255061A; Exact producer claim versus inspected original and abstract evidence. | supports | Penicillium production is directly supported. The broader Aspergillus phrase is repeated in the current source, and related patulin-cluster literature is discoverable, but an exact Aspergillus isopatulin isolation/production experiment was not independently verified within this search. This remains a bounded evidence gap; no claim is made that Aspergillus never produces it or that a patulin-producing strain proves every intermediate empirically. |
| search | 566-local-hits.txt;566-owner-hits.txt;566-discovery.json;057-root-fetch1.json through057-root-fetch4.json; Ignored/hidden-inclusive local search and bounded exact isopatulin/neopatulin literature follow-up. | context_only | All four adopted references and six indexed discovery hits were inspected at their stated depths. The2022 aptamer paper concerns patulin detection, using isopatulin as a non-cross-reacting comparator, not an antibacterial experiment; the DFT study concerns geometry, not measured antimicrobial potency. Public patent and synthesis supplement supplied exact evidence beyond abstracts. Failed publisher/CAS/BioCyc routes remain explicit; no exhaustive later-literature or registry absence claim is made. |

## Limits And Additional Notes

- All four adopted indexed abstracts were read; the1989 abstract is provider-truncated. Original1989/2009/2019 main requests failed403, and the1992 main was not retrieved. The verified2009 original supplement was inspected only at the exact S14/S15 target pages.
- Patent text includes an English machine translation; original drawing and both assay table panels were inspected. Comparator prose/table disagreement and unverified material purity remain explicit. No clinical efficacy, treatment or safety conclusion is inferred.
- The2016 publisher main/PDF was unavailable; its accessible original abstract supplies a qualitative lead only. No detailed PheRS mechanism or numeric enzyme result is claimed.
- Raw NMR data and solution equilibrium proportions were not independently reanalysed. The1979 optical-rotation paper cited by the1996 original was not inspected.
- Exact Aspergillus isopatulin production remains unverified in this bounded audit. Direct CAS and MetaCyc structure access remain limited; no absence or incorrect-link finding follows from those access gaps.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Only scratch review artifacts were written. Original thirteen hashes, native record, maintained sources, history and status are unchanged.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T190218Z-isopatulin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Isopatulin: supported lactol identity and bounded antibacterial evidence'
started_at: '2026-10-21T18:41:49Z'
finished_at: '2026-10-21T19:02:18Z'
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
summary: Native isopatulin chemistry agrees with current authorities and the original
  synthesis supplement. Exact primary patent experiments support antibacterial activity,
  independently of patulin and the pintulin derivative. One minor inherited typo remains
  in the definition. The unassigned lactol centre, solution equilibrium, unverified
  Aspergillus production scope and inaccessible historical main texts limit full scientific
  sign-off.
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
  - path: data/antibiotics/antibacterial/isopatulin.yaml
    sha256: f9cad59d34167ef9a3c6a5e6be43c9bce4a8133eb757161ab75a118c5472359f
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
- target_id: CHEBI:145111
  path: data/antibiotics/antibacterial/isopatulin.yaml
  label: isopatulin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Source-owned identity, definition, names, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ChEBI extraction and source correction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible native field emission
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position566; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:145111
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:145111
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    566
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:145111
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/isopatulin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:145111
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/isopatulin.yaml --out /private/tmp/am-review-session/566-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: authority
  name: Independent authority and primary drawing comparison
  status: passed
  required: false
  summary: Six native/current authority encodings agree; independently reconstructed
    original supplement/patent drawing also matches the native complete key.
  target_ids:
  - CHEBI:145111
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/057-root-chemistry.py
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter
  name: Structured-source applicability
  status: not_applicable
  required: false
  summary: The fully read native has no protein, gene, regulator, pathway, expression
    or mechanistic assertion. Optional PheRS work remains a scoped literature lead,
    not a new native target.
  target_ids:
  - CHEBI:145111
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:145111
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
  - CHEBI:145111
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
  - CHEBI:145111
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
  - CHEBI:145111
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
  - CHEBI:145111
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
  - CHEBI:145111
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
  - CHEBI:145111
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
  - CHEBI:145111
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
  - CHEBI:145111
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/isopatulin.yaml
  locator: Entire record, definition, three names, three parents, antibacterial role,
    full chemistry, two xrefs, source concept and all three history events.
  accessed_at: '2026-10-21T18:50:31Z'
  support: supports
  summary: The SEEDED/EXACT entry denotes neutral C7H6O4 with key ZGBMSNKHUHZKEP-UHFFFAOYSA-N
    and one unassigned lactol tetrahedron. It is distinct from patulin and the substituted
    pintulin derivative. No quantitative activity, direct target, resistance, clinical
    use, structured producer or causal graph is asserted. The definition contains
    the inherited typo positions4 an6.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv:2674;data/raw/chebi_role_names.tsv;conf/sources.yaml;scripts/extract_source_inventory.py;scripts/seed_from_sources.py
  locator: Complete exact maintained ChEBI row, initial/owner searches and extraction/role/seeding
    branches.
  accessed_at: '2026-10-21T18:50:31Z'
  support: supports
  summary: The actual ChEBI row supplies all populated scientific fields and four
    adopted PMIDs. All thirteen original inputs already include the actual owners
    and remain unchanged. The source mint and three chronological seed/reseed events
    agree. The definition typo is source-owned, so a correction must survive regeneration.
  snapshot_sha256: 76b6064b7fd6731d4c069439b99f08025a71ac9c5325ea9bc63dddf92d088553
- evidence_id: chemistry
  kind: validation
  reference: 566-chemistry.json;566-authority-chemistry.json;566-drawing-check.json
  locator: Native SMILES/InChI, current ChEBI encodings, PubChem155497 and independently
    typed primary drawing.
  accessed_at: '2026-10-21T18:50:31Z'
  support: supports
  summary: Six native/authority encodings reproduce the complete native key, formula,
    zero charge and one unassigned centre. Formula and both masses pass. An independently
    typed graph from the actual original2009 supplement and patent structure matches
    reciprocally and by full key. No salt, open-chain equilibrium form, assigned enantiomer
    or patulin positional isomer is silently substituted.
  snapshot_sha256: dc5f6b221121b46ff3f84509abe27a4502be2b4714b489bdffabc259a14148c9
- evidence_id: terms
  kind: authority
  reference: CHEBI:145111;CHEBI:37581;CHEBI:38131;CHEBI:74927;CHEBI:33282
  locator: Complete current exact entry and definitions for gamma-lactone, lactol,
    furopyran and antibacterial agent.
  accessed_at: '2026-10-21T18:50:31Z'
  support: supports
  summary: The native five-membered lactone, cyclic hemiacetal and ortho-fused furan/pyran
    skeleton fit all three parents and the systematic names. Current ChEBI repeats
    the same unassigned structure and neopatulin alias. Unassigned stereochemistry
    alone is not proof of a racemate; solution interconversion is assessed separately.
  snapshot_sha256: cf71bb2d6126d39f710805e3f2fc1ccb24d2ec6b8d0c6ce978768e5d96c670db
- evidence_id: xref
  kind: authority
  reference: cas:70402-10-7;metacyc.compound:CPD-16725;PubChem155497
  locator: Current ChEBI reference attribution, exact PubChem CAS/full-key requests
    and direct BioCyc page.
  accessed_at: '2026-10-21T18:50:31Z'
  support: supports
  summary: Both exact CAS and full-key queries resolve PubChem155497 with native chemistry.
    Direct CAS API returned401; the public shell did not supply an independently inspected
    registry graph. The MetaCyc page requires login, so exact CPD-16725 structure
    verification remains unavailable; current ChEBI repeats the accession. These are
    explicit access limitations rather than evidence that either native link is wrong.
  snapshot_sha256: 01e855bd1e67578fee5270401f5ea5b8b2a464e3e0b538852103927635159717
- evidence_id: adopted1992
  kind: primary_source
  reference: PMID:1518888
  locator: Complete indexed original abstract and metadata; original main not retrieved.
  accessed_at: '2026-10-21T18:50:31Z'
  support: supports
  summary: The study compares patulin and five analogues including isopatulin in L1210/P388
    cells and animal tumour models. Its broad animal response is specifically attributed
    to dehydroisopatulin, so that derivative’s dose/efficacy is not transferred to
    native isopatulin. This is host cytotoxicity context, not bacterial susceptibility
    evidence.
  snapshot_sha256: 350a52dd3cb3155849129d65e2ac95a9d9e72091cc51cb474d0adc87f9f315f3
- evidence_id: adopted1989
  kind: primary_source
  reference: PMID:2605253;DOI:10.1021/bi00449a035
  locator: Complete available indexed abstract, explicitly truncated by the provider
    at250 words; original main403.
  accessed_at: '2026-10-21T18:50:31Z'
  support: supports
  summary: Penicillium patulum extracts epoxidize hydroquinone substrates and further
    convert phyllostine to neopatulin. Reported epoxidation kinetics concern upstream
    substrates, not an antibacterial target or isopatulin potency. The abstract supports
    biosynthetic context without reconstructing missing methods or stereochemistry.
  snapshot_sha256: 350a52dd3cb3155849129d65e2ac95a9d9e72091cc51cb474d0adc87f9f315f3
- evidence_id: adopted2019
  kind: primary_source
  reference: PMID:30680886;DOI:10.1111/1462-2920.14542
  locator: Complete original indexed abstract and metadata; publisher main403.
  accessed_at: '2026-10-21T18:50:31Z'
  support: supports
  summary: The Penicillium expansum study dissects the15-gene patulin cluster and
    verifies functions for eight pathway enzymes. The accessible abstract does not
    establish a separate Aspergillus isopatulin isolation experiment or exact isopatulin
    antibacterial mechanism. No inferred enzyme target or strain-specific producer
    object is added.
  snapshot_sha256: 350a52dd3cb3155849129d65e2ac95a9d9e72091cc51cb474d0adc87f9f315f3
- evidence_id: synthesis
  kind: primary_source
  reference: PMID:19583231;DOI:10.1021/jo900855e;DOI:10.1021/jo900855e.s001
  locator: Complete indexed abstract; verified original publisher supplement, actual
    pagesS14/S15 viewed and exact image drawings independently reconstructed.
  accessed_at: '2026-10-21T18:50:31Z'
  support: supports
  summary: The synthesis routes through ascladiol oxidation to isopatulin. ActualS14
    shows open-chain17-Z/17-E interconversion with cyclic isopatulin3;S15 explicitly
    describes the equilibrium in chloroform-d after recrystallization and displays
    proton/carbon spectra with the matching cyclic drawing. This supports the native
    constitution while limiting claims of one solution species. The main PDF remained403;
    raw spectral integration and a complete reassignment were not performed.
  snapshot_sha256: e0266ef09c3bff48c67201020c98375441669db2eaa84bca6a87fae6584e529e
- evidence_id: patent-material
  kind: primary_source
  reference: https://patents.google.com/patent/CN103255061A/en
  locator: Original patent description and Examples1/2 through public Chinese text/English
    machine translation; actual structural image inspected.
  accessed_at: '2026-10-21T18:50:31Z'
  support: supports
  summary: The patent isolates named isopatulin from Penicillium griseofulvum CPCC400528,
    deposited as CGMCC5752, as a colorless oil. The original drawing and formulaC7H6O4
    match native; reported NMR text is not independently reprocessed, and no purity
    or enantiomeric-composition value is inferred. This is exact source material,
    distinct from patulin or a co-isolated derivative.
  snapshot_sha256: 4032e3259dd7f6cb46242c60488fb1f01d0b9237fa338328ff17d47ed3f8ea3a
- evidence_id: patent-activity
  kind: primary_source
  reference: CN103255061A Example2 and Table1
  locator: Complete agar-dilution methods and both actual Table1 image panels read.
  accessed_at: '2026-10-21T18:50:31Z'
  support: supports
  summary: The patent tests isolated material using MH or7H11 agar at pH7.2–7.4, approximately10^4
    CFU per spot,37°C and16–48h for ordinary bacteria or3–4weeks for tuberculosis.
    MIC is complete growth inhibition. Actual Table1 reports isopatulin64 µg/mL for
    S.aureus ATCC29213,16 for E.coli ATCC25922 and8 for M.tuberculosis H37Rv. Its
    method prose names rifampicin while the table heading names levofloxacin, with
    rifampicin explicitly noted for H37Rv; that comparator inconsistency is retained.
    These are patent-reported strain-specific measurements, not independently replicated
    clinical efficacy or broad safety.
  snapshot_sha256: 0db1ac9b11d61fe0aa8a27ffc2e7301926f7742e1836448450e3ce96c26cc147
- evidence_id: primary2016
  kind: primary_source
  reference: DOI:10.1080/23312009.2016.1181536
  locator: Original publisher-indexed abstract and exact-compound scope; direct full
    HTML/PDF403.
  accessed_at: '2026-10-21T18:50:31Z'
  support: supports
  summary: 'The study isolates named isopatulin among six compounds from the same
    CPCC400528 strain and reports PheRS inhibition and moderate-to-weak H37Rv activity
    for selected compounds including isopatulin. Only the accessible abstract is used
    here: no uninspected numerical IC50, docking contact, selectivity or target causality
    is adopted. The native contains no molecular target, and enzyme inhibition alone
    would not prove the sole cellular cause of growth inhibition.'
- evidence_id: pintulin
  kind: primary_source
  reference: PMID:8968391;DOI:10.7164/antibiotics.49.985
  locator: Original five-page main converted text read, particularly isolation/comparison
    discussion and biological endpoint scope; image tables not independently digitized.
  accessed_at: '2026-10-21T18:50:31Z'
  support: supports
  summary: The paper reports co-isolation of isopatulin from Penicillium vulpinum
    F-4148 and compares it with the larger pintulin derivative. Its tested cytocidal
    and weak antimicrobial endpoints principally concern pintulin and are not transferred
    to isopatulin. The authors describe optical inactivity by reference to the earlier1979
    report; that secondary citation does not independently establish the native sample’s
    enantiomeric composition.
  snapshot_sha256: 059f50916526cc9955982c8d306ae8a7c08fe6d98b0906248d9899e9ee9a8520
- evidence_id: producer-scope
  kind: validation
  reference: definition;PMID:2605253;PMID:30680886;PMID:8968391;CN103255061A
  locator: Exact producer claim versus inspected original and abstract evidence.
  accessed_at: '2026-10-21T18:50:31Z'
  support: supports
  summary: Penicillium production is directly supported. The broader Aspergillus phrase
    is repeated in the current source, and related patulin-cluster literature is discoverable,
    but an exact Aspergillus isopatulin isolation/production experiment was not independently
    verified within this search. This remains a bounded evidence gap; no claim is
    made that Aspergillus never produces it or that a patulin-producing strain proves
    every intermediate empirically.
- evidence_id: search
  kind: search
  reference: 566-local-hits.txt;566-owner-hits.txt;566-discovery.json;057-root-fetch1.json
    through057-root-fetch4.json
  locator: Ignored/hidden-inclusive local search and bounded exact isopatulin/neopatulin
    literature follow-up.
  accessed_at: '2026-10-21T18:50:31Z'
  support: context_only
  summary: All four adopted references and six indexed discovery hits were inspected
    at their stated depths. The2022 aptamer paper concerns patulin detection, using
    isopatulin as a non-cross-reacting comparator, not an antibacterial experiment;
    the DFT study concerns geometry, not measured antimicrobial potency. Public patent
    and synthesis supplement supplied exact evidence beyond abstracts. Failed publisher/CAS/BioCyc
    routes remain explicit; no exhaustive later-literature or registry absence claim
    is made.
  search_scope: 2026-10-21; rg --no-ignore --hidden native identifiers/labels/key/CAS;
    exact EuropePMC title/abstract isopatulin or neopatulin; original DOI, publisher
    supplement API and public patent follow-up.
  snapshot_sha256: 3dae579f814cf031ac6af8046a0e5444421b9ae433066e6bb45519959ccee7cc
assessments:
- assessment_id: identity
  area: identity
  topic: Exact cyclic structure with unspecified lactol stereochemistry
  outcome: supported
  summary: Independent authorities and original drawings support the native cyclic
    constitution and names. Dynamic solution equilibrium and unassigned configuration
    remain explicit; neither proves a defective native graph.
  target_ids:
  - CHEBI:145111
  evidence_ids:
  - native
  - chemistry
  - terms
  - synthesis
  - patent-material
- assessment_id: groundings
  area: grounding
  topic: Structural parents and chemical references
  outcome: supported
  summary: All three structural parents fit. CAS name/key lookups agree with native;
    direct CAS and MetaCyc verification remain limited rather than falsely declared
    complete.
  target_ids:
  - CHEBI:145111
  evidence_ids:
  - terms
  - xref
  - chemistry
- assessment_id: activity
  area: evidence
  topic: Antibacterial role separated from toxin/derivative experiments
  outcome: supported
  summary: Exact isolated compound is active in the inspected patent agar assays and
    is named in the later original antibacterial abstract. Patulin detection, pintulin
    cytotoxicity and dehydroisopatulin animal results are not transferred.
  target_ids:
  - CHEBI:145111
  evidence_ids:
  - patent-activity
  - primary2016
  - adopted1992
  - pintulin
  - search
- assessment_id: definition
  area: nomenclature
  topic: Definition wording and producer precision
  outcome: concern
  summary: The chemical description is coherent apart from the minor an/and typo.
    Penicillium production is supported; exact Aspergillus production remains unverified
    within the bounded primary audit.
  target_ids:
  - CHEBI:145111
  evidence_ids:
  - native
  - owners
  - terms
  - producer-scope
- assessment_id: mechanism
  area: completeness
  topic: Optional biosynthetic and target enrichment
  outcome: unknown
  summary: The native asserts no target. Patent and abstract PheRS leads do not justify
    a complete causal mechanism, and fungal biosynthetic enzymes are not bacterial
    drug targets. Original source access and solution-material boundaries constrain
    further enrichment.
  target_ids:
  - CHEBI:145111
  evidence_ids:
  - adopted1989
  - adopted2019
  - primary2016
  - synthesis
- assessment_id: provenance
  area: provenance
  topic: Source and history ownership
  outcome: supported
  summary: All thirteen initial hashes, actual ChEBI source ownership, source mint
    and three history events are preserved; no native changes were made.
  target_ids:
  - CHEBI:145111
  evidence_ids:
  - owners
  - native
findings:
- finding_id: F1
  issue_key: isopatulin-definition-an-for-and-typo
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the inherited conjunction typo in the structural definition
  description: The definition says positions4 an6 rather than positions4 and6. The
    chemical meaning is recoverable and the graph is valid; correct the source-owned
    prose through maintained extraction/regeneration.
  target_ids:
  - CHEBI:145111
  field_paths:
  - definition
  evidence_ids:
  - native
  - owners
  - terms
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Source-owned identity, definition, names, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ChEBI extraction and source correction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible native field emission
  rule_id: 'review-checklist: accurate and unambiguous nomenclature'
  native_severity: minor
  normalization_reason: A bounded spelling defect in otherwise understandable structural
    prose; identity and antibacterial eligibility are supported.
actions:
- action_id: A1
  description: Correct the source definition conjunction reproducibly.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:145111
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Source-owned identity, definition, names, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ChEBI extraction and source correction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible native field emission
  acceptance_checks:
  - Regenerated definition uses positions4 and6 while retaining the exact structural
    meaning, formula/key and source attribution.
  - Apply the maintained source correction without manually patching generated YAML;
    pass focused schema/strict and required source/history/reproduction checks.
- action_id: A2
  description: Retain experimental boundaries in any optional scientific enrichment.
  finding_ids: []
  target_ids:
  - CHEBI:145111
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/isopatulin.yaml
    role: Future validated curator-owned scientific annotations
  acceptance_checks:
  - Verify exact Aspergillus production before adding a strain-specific producer;
    generic patulin-cluster membership is not a substitute for exact metabolite evidence.
  - Keep patent-reported MICs, media and original units distinct from later enzyme
    inhibition and host cytotoxicity; resolve the patent comparator inconsistency
    before importing comparison claims.
  - Keep cyclic isopatulin and its measured solution equilibrium, patulin and pintulin
    distinct; do not assert a pure enantiomer or direct cellular target from an unassigned
    graph or an abstract.
limitations:
- All four adopted indexed abstracts were read; the1989 abstract is provider-truncated.
  Original1989/2009/2019 main requests failed403, and the1992 main was not retrieved.
  The verified2009 original supplement was inspected only at the exact S14/S15 target
  pages.
- Patent text includes an English machine translation; original drawing and both assay
  table panels were inspected. Comparator prose/table disagreement and unverified
  material purity remain explicit. No clinical efficacy, treatment or safety conclusion
  is inferred.
- The2016 publisher main/PDF was unavailable; its accessible original abstract supplies
  a qualitative lead only. No detailed PheRS mechanism or numeric enzyme result is
  claimed.
- Raw NMR data and solution equilibrium proportions were not independently reanalysed.
  The1979 optical-rotation paper cited by the1996 original was not inspected.
- Exact Aspergillus isopatulin production remains unverified in this bounded audit.
  Direct CAS and MetaCyc structure access remain limited; no absence or incorrect-link
  finding follows from those access gaps.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Only scratch review artifacts were written. Original thirteen hashes, native record,
  maintained sources, history and status are unchanged.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
