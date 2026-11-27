# Secoisopimaratrienoic acid: relative stereochemistry and exact assay scope

- Review: 20261021T072258Z-secoisopimaratrienoic-acid-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T07:13:16Z
- Finished UTC: 2026-10-21T07:22:58Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The stored structure consistently reproduces the ChEBI entity, but the adopted crystallographic paper establishes relative stereochemistry and explicitly leaves absolute configuration undetermined. One minor finding requires preserving that experimental boundary before assigning natural-material results to one absolute stereoisomer. An additional informational follow-up covers a newer antibacterial assay with a nonstandard approximately50-percent MIC endpoint. No direct antimicrobial target is established.

## Scope And Provenance

Entire native record, maintained seed provenance, official structure and cited primary identity/pharmacology; additional complete antibacterial paper and figure.

Selection: Twenty-fifth initially uncovered record in sorted path order; fifth in batch003.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:66459 | data/antibiotics/antibacterial/3-4-secoisopimara-4-18-7-15-triene-3-oic-acid.yaml | generated | 3,4-secoisopimara-4(18),7,15-triene-3-oic acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema validation | passed | True | CHEBI:66459 | Actual focused execution exited0 with no validation errors. |
| Documented strict validation | passed | True | CHEBI:66459 | Actual focused execution exited0 with no validation errors. |
| Independent structure and minted identity consistency | passed | False | CHEBI:66459 | All local assertions passed; this does not prove natural-isolate absolute handedness. |
| Structured source applicability | not_applicable | False | CHEBI:66459 | The record names no gene, protein, regulator, pathway, stress response or dataset. Host-pharmacology context is not an asserted antimicrobial expression claim. |
| Authoritative full QC | failed | True | CHEBI:66459 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:66459 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:66459 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:66459 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:66459 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:66459 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:66459 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:66459 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:66459 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Database structure and natural-isolate equivalence

identity: concern. Targets: CHEBI:66459.

The exact represented structure is internally and authority-consistent. The adopted experimental source establishes relative configuration; assignment of natural-isolate effects to a single absolute stereoisomer needs qualification.

### Broader parents and source registry assertion

grounding: supported. Targets: CHEBI:66459.

All three parents are broader and chemically appropriate. Registry identifier is authority-corroborated; independent registry access is limited.

### Plant isolation and host pharmacology

evidence: supported. Targets: CHEBI:66459.

Inspected primary sources support isolation and bounded antispasmodic/hypotensive observations at natural-material level. They do not establish clinical status or microbial targets.

### Antibacterial role and assay interpretation

evidence: supported. Targets: CHEBI:66459.

The imported role is faithfully retained; primary activity context exists. Exact enantiomer equivalence and author-defined assay endpoints remain explicit before numerical curation.

### Antimicrobial action versus other endpoints

completeness: unknown. Targets: CHEBI:66459.

No inspected experiment establishes a direct antibacterial target. Host smooth-muscle and antimutagenic hypotheses do not supply one.

### Producer, resistance, clinical, graph and dataset objects

representation: not_applicable. Targets: CHEBI:66459.

These optional objects are not asserted. A proposed plant biosynthetic route or extraction alone is not sufficient for a biosynthesizing-producer entry.

### Source and curation history

ownership: supported. Targets: CHEBI:66459.

SEEDED history and source ownership are consistent. Future scientific annotations and source-structure adjudication require their respective maintained owners.

## Findings

### F1: Natural-material evidence needs a relative-stereochemistry qualification

minor / open / confirmed; issue key: chebi-66459-relative-versus-absolute-experimental-scope.

The source-linked crystal study does not determine absolute handedness, while the database structure and systematic synonym specify it. Add explicit evidence scope and adjudicate any later absolute assignment before treating natural-material experiments as enantiomer-specific. This finding does not declare the database enantiomer wrong or authorize removal of all stereochemistry.

### F2: New primary activity can be curated with its explicit endpoint definition

informational / open / confirmed; issue key: chebi-66459-assay-endpoint-enrichment.

A specific recent assay provides an enrichment path, subject to stereochemical mapping and preservation of its nonstandard MIC definition. No quantitative activity object is currently false.

## Recommended Actions And Acceptance Checks

### A1

During separately authorized curation, document the relative-versus-absolute experimental boundary and search for a justified exact free-acid absolute assignment. If a source representation change is warranted, repair it through maintained source extraction and reseeding while preserving supported relative configuration.

- A crystallographic drawing chosen arbitrarily is not cited as an absolute determination of the natural free acid.
- Do not assign the opposite enantiomer, racemate or an entirely unstereospecified structure by assumption.
- Keep a source-backed uncertainty discussion and use validated writer/history; any imported-structure correction must reproduce through the maintained pipeline.

### A2

Match the2025 compound1 to the supported chemical scope, then add assay evidence with its author-defined endpoint, strain and conditions. Leave antibacterial mechanism unresolved unless direct primary support is found.

- Retain the approximately50-percent growth-inhibition MIC definition and separate neutralizing-agar MBC endpoint; do not infer clinical susceptibility.
- Do not assign extract negatives or compounds2/3 results to the isolated compound, or convert proposed biosynthesis into proved production.
- Run focused schema/strict validation, corpus reproduction and fullQC for native edits; retain SEEDED until native promotion criteria are met.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/3-4-secoisopimara-4-18-7-15-triene-3-oic-acid.yaml; Every field of generated YAML | supports | Read source definition, systematic absolute-stereo synonym, three parents, antibacterial role, all structure fields, one registry xref, source concept and three seed/reseed events. Native status is SEEDED/EXACT. No quantitative assay, mechanism, target, resistance, producer, clinical, dataset or graph object is asserted. |
| owner | data/raw/chebi_antimicrobials.tsv; Complete CHEBI:66459 row; manifest, role maps, extractor and seeder | supports | All imported fields match the adopted authority row. Its two PMID leads are11301863 and17978757; specific mechanism-role column is empty. Ignored-inclusive exact-ID/minted-ID searches in maintained curation tables and conf found no override. Generated identity changes belong upstream; new evidence/qualification is curator-owned. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:66459; Full official HTML fetched directly; 025-chebi.html | supports | The authority agrees on the named free acid, all four assigned centres, SMILES/InChI/key, C20H30O2, net charge0 and masses. Its parent labels are diterpenoid, monocarboxylic acid and carbobicyclic compound, all structurally broader. Reaxys22892163 and Salvia cinnabarina leaf-source metadata are present. Additional antispasmodic/metabolite/acid roles are outside the adopted antimicrobial subset. |
| chemistry | RDKit and hashlib independent calculation; 025-chemistry.py; 025-chemistry.json | supports | Both encodings agree on XQZUWQQUDZZOHA-ZULIPRJHSA-N, C20H30O2, charge0, one fragment, four assigned centres and masses302.458/302.2245802. The minted source-concept identifier is reproduced. Internal consistency does not establish the absolute configuration of a natural isolate. |
| primary2001 | PMID:11301863; Europe PMC core abstract; DOI10.1055/s-2001-11511 | context_only | The primary isolation report describes the leaf-surface exudate and NMR assignment, with spasmolytic effects in isolated guinea-pig ileum. It supports source and pharmacological context without establishing an antibacterial target or a clinical indication. |
| stereo2007 | DOI:10.3390/12102279; PMID17978757; full paper pp2279–2287, especially p2282 and X-ray methods p2285; https://pdfs.semanticscholar.org/aa46/692e760ef5253d7ebd4f5097e566f05abe0e.pdf | supports | Crystallography concerns derivative4, with relative stereochemistry inferred to persist across the acid/derivatives. The authors state that absolute configuration was not determined and that the displayed configuration was chosen arbitrarily; C5S*,C9S*,C10S*,C13S* are relative assignments. The insignificant Flack parameter does not determine handedness. Reference8 is a2003 antimicrobial proceedings report, not an assay reproduced here. |
| stereo-image | DOI:10.3390/12102279; Page2282 rendered as025-2007-page4.png and visually inspected | supports | The printed text explicitly qualifies the stereochemistry as relative. The displayed crystal structure is derivative4, not an independent absolute-configuration determination of the free acid. |
| bladder | PMID:14994202; Europe PMC core abstract; DOI10.1055/s-2004-815501 | context_only | The tested diterpenoid suppresses electrical-field-stimulated rat-bladder contractility with partial nitric-oxide involvement. This is host pharmacology, not a microbial antimicrobial mechanism. |
| bloodpressure | PMID:17357976; Europe PMC core abstract; DOI10.1002/ptr.2128 | context_only | Anaesthetized-rat experiments support hypotensive activity under their conditions. Their proposed peripheral mechanism is not clinical efficacy or an antibacterial target. |
| ames | PMID:19497346; Europe PMC core abstract; DOI10.1016/j.fct.2009.05.030 | context_only | The bacterial reverse-mutation experiment reports antimutagenicity and proposes nonspecific explanations. Fewer induced revertants are not an antibacterial MIC; hypothesized permeability effects are not a demonstrated killing target. Publisher full-text request failed. |
| assay2025 | DOI:10.1038/s41598-025-19109-0; PMID41062670; PMC12508438 full XML, Figure1, Table1, antibacterial results and Methods; 025-2025.xml | supports | Compound1 from Salvia elegans is matched by constitution/relative drawing and the original isolation citation despite abbreviated diene naming. S.aureus ATCC6538 testing reports15.6µg/mL MIC and62.5µg/mL MBC. Methods define MIC as approximately50-percent visible growth reduction in tryptic soy broth at32.5C for18±2h, and MBC by no visible growth after neutralizing-agar transfer. These author-defined endpoints must not be silently treated as conventional complete-inhibition MIC. Only compound1 was tested among the low-yield isolates; other negative screens include extracts. Biosynthesis is proposed, not experimentally demonstrated. |
| assay-drawing | DOI:10.1038/s41598-025-19109-0; Official PMC Figure1 image; 025-2025-fig1.jpg visually inspected | supports | The compound1 drawing includes the exomethylene omitted from the shortened prose name, the free acid and the secoisopimarane framework. Related hydroxylated and lactone compounds2/3 are distinct; drawing agreement alone cannot resolve the natural absolute configuration. |
| different-dimer | https://html.rhhz.net/zghxkb/20230921.htm; Flavidanolides A and B from Isodon flavidus, primary full text, identity and X-ray sections | context_only | A search lead with an absolute-configuration determination concerns a heterodimeric ester from another plant. It does not establish the absolute configuration or antimicrobial activity of this isolated free acid. |
| search | Ignored-inclusive local search and bounded free primary discovery; 025-local-hits.txt; 025-epmc.json; public full-paper retrieval | context_only | Exact searches established maintained-source reproduction and located primary stereochemistry and assay evidence. The result is an unresolved absolute-isolate boundary, not proof that the stored enantiomer is chemically impossible or universally inactive. |

## Limits And Additional Notes

- The 2001 isolation paper and 2004/2007 pharmacology studies were inspected as primary abstracts. The 2007 crystallographic paper was read in full from a freely hosted copy, and its stereochemical qualification was visually confirmed on page2282.
- The 2003 antimicrobial proceedings reference was inspected only as a bibliography entry in the 2007 paper; its experimental pages were not retrieved. No MIC or target is extracted from it.
- The 2025 paper abbreviates compound1 as a diene, while Figure1 depicts the exomethylene as well as the other two alkenes. The constitution/relative drawing matches this scaffold, but that does not independently establish absolute stereochemical equivalence.
- Reaxys was corroborated through official ChEBI rather than independently inspected. Bounded searches do not prove that no later exact absolute-configuration determination exists.
- No native structure is changed or declared to be the opposite enantiomer. Any proposed representation correction requires adjudicating source identity and preserving relative stereochemical information.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T072258Z-secoisopimaratrienoic-acid-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Secoisopimaratrienoic acid: relative stereochemistry and exact assay scope'
started_at: '2026-10-21T07:13:16Z'
finished_at: '2026-10-21T07:22:58Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the target. Entire record, source ownership,
    authority identity, independent chemistry, adopted primary sources and additional
    primary experiments were inspected.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The stored structure consistently reproduces the ChEBI entity, but the adopted
  crystallographic paper establishes relative stereochemistry and explicitly leaves
  absolute configuration undetermined. One minor finding requires preserving that
  experimental boundary before assigning natural-material results to one absolute
  stereoisomer. An additional informational follow-up covers a newer antibacterial
  assay with a nonstandard approximately50-percent MIC endpoint. No direct antimicrobial
  target is established.
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
  - path: data/antibiotics/antibacterial/3-4-secoisopimara-4-18-7-15-triene-3-oic-acid.yaml
    sha256: d3761ca0b09bef163a55507e6bf56929a46e5a7e839b584c89eda2063d096cd0
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
- target_id: CHEBI:66459
  path: data/antibiotics/antibacterial/3-4-secoisopimara-4-18-7-15-triene-3-oic-acid.yaml
  label: 3,4-secoisopimara-4(18),7,15-triene-3-oic acid
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
  description: Entire native record, maintained seed provenance, official structure
    and cited primary identity/pharmacology; additional complete antibacterial paper
    and figure.
  selection: Twenty-fifth initially uncovered record in sorted path order; fifth in
    batch003.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:66459
checks:
- check_id: schema
  name: Documented schema validation
  status: passed
  required: true
  summary: Actual focused execution exited0 with no validation errors.
  target_ids:
  - CHEBI:66459
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/3-4-secoisopimara-4-18-7-15-triene-3-oic-acid.yaml
  exit_code: 0
- check_id: strict
  name: Documented strict validation
  status: passed
  required: true
  summary: Actual focused execution exited0 with no validation errors.
  target_ids:
  - CHEBI:66459
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/3-4-secoisopimara-4-18-7-15-triene-3-oic-acid.yaml
    --out /private/tmp/am-review-session/025-strict.tsv
  exit_code: 0
- check_id: chemistry
  name: Independent structure and minted identity consistency
  status: passed
  required: false
  summary: All local assertions passed; this does not prove natural-isolate absolute
    handedness.
  target_ids:
  - CHEBI:66459
  command: .venv/bin/python /private/tmp/am-review-session/025-chemistry.py
  exit_code: 0
  evidence_ids:
  - chemistry
- check_id: imodulondb
  name: Structured source applicability
  status: not_applicable
  required: false
  summary: The record names no gene, protein, regulator, pathway, stress response
    or dataset. Host-pharmacology context is not an asserted antimicrobial expression
    claim.
  target_ids:
  - CHEBI:66459
  evidence_ids:
  - record
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:66459
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
  - CHEBI:66459
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
  - CHEBI:66459
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
  - CHEBI:66459
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
  - CHEBI:66459
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
  - CHEBI:66459
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
  - CHEBI:66459
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
  - CHEBI:66459
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
  - CHEBI:66459
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/3-4-secoisopimara-4-18-7-15-triene-3-oic-acid.yaml
  locator: Every field of generated YAML
  accessed_at: '2026-10-21T07:18:04Z'
  support: supports
  summary: Read source definition, systematic absolute-stereo synonym, three parents,
    antibacterial role, all structure fields, one registry xref, source concept and
    three seed/reseed events. Native status is SEEDED/EXACT. No quantitative assay,
    mechanism, target, resistance, producer, clinical, dataset or graph object is
    asserted.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Complete CHEBI:66459 row; manifest, role maps, extractor and seeder
  accessed_at: '2026-10-21T07:18:04Z'
  support: supports
  summary: All imported fields match the adopted authority row. Its two PMID leads
    are11301863 and17978757; specific mechanism-role column is empty. Ignored-inclusive
    exact-ID/minted-ID searches in maintained curation tables and conf found no override.
    Generated identity changes belong upstream; new evidence/qualification is curator-owned.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:66459
  locator: Full official HTML fetched directly; 025-chebi.html
  accessed_at: '2026-10-21T07:18:04Z'
  support: supports
  summary: The authority agrees on the named free acid, all four assigned centres,
    SMILES/InChI/key, C20H30O2, net charge0 and masses. Its parent labels are diterpenoid,
    monocarboxylic acid and carbobicyclic compound, all structurally broader. Reaxys22892163
    and Salvia cinnabarina leaf-source metadata are present. Additional antispasmodic/metabolite/acid
    roles are outside the adopted antimicrobial subset.
  snapshot_sha256: 3e2f5a8801615e44234037f764edf9494153cf890db6cdad11ae3c02178c2850
- evidence_id: chemistry
  kind: validation
  reference: RDKit and hashlib independent calculation
  locator: 025-chemistry.py; 025-chemistry.json
  accessed_at: '2026-10-21T07:18:04Z'
  support: supports
  summary: Both encodings agree on XQZUWQQUDZZOHA-ZULIPRJHSA-N, C20H30O2, charge0,
    one fragment, four assigned centres and masses302.458/302.2245802. The minted
    source-concept identifier is reproduced. Internal consistency does not establish
    the absolute configuration of a natural isolate.
  snapshot_sha256: 2b33a0170956d1815694b5ef4267be29cdcdea1cdfd9e9c89c5486a44bd05196
- evidence_id: primary2001
  kind: primary_source
  reference: PMID:11301863
  locator: Europe PMC core abstract; DOI10.1055/s-2001-11511
  accessed_at: '2026-10-21T07:18:04Z'
  support: context_only
  summary: The primary isolation report describes the leaf-surface exudate and NMR
    assignment, with spasmolytic effects in isolated guinea-pig ileum. It supports
    source and pharmacological context without establishing an antibacterial target
    or a clinical indication.
- evidence_id: stereo2007
  kind: primary_source
  reference: DOI:10.3390/12102279
  locator: PMID17978757; full paper pp2279–2287, especially p2282 and X-ray methods
    p2285; https://pdfs.semanticscholar.org/aa46/692e760ef5253d7ebd4f5097e566f05abe0e.pdf
  accessed_at: '2026-10-21T07:18:04Z'
  support: supports
  summary: Crystallography concerns derivative4, with relative stereochemistry inferred
    to persist across the acid/derivatives. The authors state that absolute configuration
    was not determined and that the displayed configuration was chosen arbitrarily;
    C5S*,C9S*,C10S*,C13S* are relative assignments. The insignificant Flack parameter
    does not determine handedness. Reference8 is a2003 antimicrobial proceedings report,
    not an assay reproduced here.
  snapshot_sha256: 039af41754ca2f38bbccee18cc69360f04be5575e5c925f5a3acf9d8f1c85d26
- evidence_id: stereo-image
  kind: primary_source
  reference: DOI:10.3390/12102279
  locator: Page2282 rendered as025-2007-page4.png and visually inspected
  accessed_at: '2026-10-21T07:18:04Z'
  support: supports
  summary: The printed text explicitly qualifies the stereochemistry as relative.
    The displayed crystal structure is derivative4, not an independent absolute-configuration
    determination of the free acid.
  snapshot_sha256: 72f41c4ca17dbe3ff5d831d4fe5ef1d3515dd99e14a45301e9b65d6be3db733f
- evidence_id: bladder
  kind: primary_source
  reference: PMID:14994202
  locator: Europe PMC core abstract; DOI10.1055/s-2004-815501
  accessed_at: '2026-10-21T07:18:04Z'
  support: context_only
  summary: The tested diterpenoid suppresses electrical-field-stimulated rat-bladder
    contractility with partial nitric-oxide involvement. This is host pharmacology,
    not a microbial antimicrobial mechanism.
- evidence_id: bloodpressure
  kind: primary_source
  reference: PMID:17357976
  locator: Europe PMC core abstract; DOI10.1002/ptr.2128
  accessed_at: '2026-10-21T07:18:04Z'
  support: context_only
  summary: Anaesthetized-rat experiments support hypotensive activity under their
    conditions. Their proposed peripheral mechanism is not clinical efficacy or an
    antibacterial target.
- evidence_id: ames
  kind: primary_source
  reference: PMID:19497346
  locator: Europe PMC core abstract; DOI10.1016/j.fct.2009.05.030
  accessed_at: '2026-10-21T07:18:04Z'
  support: context_only
  summary: The bacterial reverse-mutation experiment reports antimutagenicity and
    proposes nonspecific explanations. Fewer induced revertants are not an antibacterial
    MIC; hypothesized permeability effects are not a demonstrated killing target.
    Publisher full-text request failed.
- evidence_id: assay2025
  kind: primary_source
  reference: DOI:10.1038/s41598-025-19109-0
  locator: PMID41062670; PMC12508438 full XML, Figure1, Table1, antibacterial results
    and Methods; 025-2025.xml
  accessed_at: '2026-10-21T07:18:04Z'
  support: supports
  summary: Compound1 from Salvia elegans is matched by constitution/relative drawing
    and the original isolation citation despite abbreviated diene naming. S.aureus
    ATCC6538 testing reports15.6µg/mL MIC and62.5µg/mL MBC. Methods define MIC as
    approximately50-percent visible growth reduction in tryptic soy broth at32.5C
    for18±2h, and MBC by no visible growth after neutralizing-agar transfer. These
    author-defined endpoints must not be silently treated as conventional complete-inhibition
    MIC. Only compound1 was tested among the low-yield isolates; other negative screens
    include extracts. Biosynthesis is proposed, not experimentally demonstrated.
  snapshot_sha256: 45be78739a3b4a305b3916c0e8197511d2e8d8efd8bdd6ab829a9512d5939455
- evidence_id: assay-drawing
  kind: primary_source
  reference: DOI:10.1038/s41598-025-19109-0
  locator: Official PMC Figure1 image; 025-2025-fig1.jpg visually inspected
  accessed_at: '2026-10-21T07:18:04Z'
  support: supports
  summary: The compound1 drawing includes the exomethylene omitted from the shortened
    prose name, the free acid and the secoisopimarane framework. Related hydroxylated
    and lactone compounds2/3 are distinct; drawing agreement alone cannot resolve
    the natural absolute configuration.
  snapshot_sha256: e34261dfc5d003f02bc298bc6743386c233adca206f3b96518d473b8c24ba6e8
- evidence_id: different-dimer
  kind: primary_source
  reference: https://html.rhhz.net/zghxkb/20230921.htm
  locator: Flavidanolides A and B from Isodon flavidus, primary full text, identity
    and X-ray sections
  accessed_at: '2026-10-21T07:18:04Z'
  support: context_only
  summary: A search lead with an absolute-configuration determination concerns a heterodimeric
    ester from another plant. It does not establish the absolute configuration or
    antimicrobial activity of this isolated free acid.
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local search and bounded free primary discovery
  locator: 025-local-hits.txt; 025-epmc.json; public full-paper retrieval
  accessed_at: '2026-10-21T07:18:04Z'
  support: context_only
  summary: Exact searches established maintained-source reproduction and located primary
    stereochemistry and assay evidence. The result is an unresolved absolute-isolate
    boundary, not proof that the stored enantiomer is chemically impossible or universally
    inactive.
  search_scope: rg --no-ignore --hidden exact identifier, full label and slug across
    batch003 except .git and .venv; separately searched curation/decisions.tsv, curation/curator_antibiotics.tsv
    and conf for CHEBI66459 and minted ID. Free web queries combined secoisopimara
    with antibacterial, antimicrobial2003 and absolute configuration. Official ChEBI,
    five primary abstract records, the complete2007 PDF and2025 XML/figure were inspected.
    No paid access or author contact occurred.
assessments:
- assessment_id: identity
  area: identity
  topic: Database structure and natural-isolate equivalence
  outcome: concern
  summary: The exact represented structure is internally and authority-consistent.
    The adopted experimental source establishes relative configuration; assignment
    of natural-isolate effects to a single absolute stereoisomer needs qualification.
  target_ids:
  - CHEBI:66459
  evidence_ids:
  - record
  - chebi
  - chemistry
  - stereo2007
  - stereo-image
- assessment_id: grounding
  area: grounding
  topic: Broader parents and source registry assertion
  outcome: supported
  summary: All three parents are broader and chemically appropriate. Registry identifier
    is authority-corroborated; independent registry access is limited.
  target_ids:
  - CHEBI:66459
  evidence_ids:
  - record
  - chebi
- assessment_id: definition
  area: evidence
  topic: Plant isolation and host pharmacology
  outcome: supported
  summary: Inspected primary sources support isolation and bounded antispasmodic/hypotensive
    observations at natural-material level. They do not establish clinical status
    or microbial targets.
  target_ids:
  - CHEBI:66459
  evidence_ids:
  - record
  - primary2001
  - bladder
  - bloodpressure
- assessment_id: activity
  area: evidence
  topic: Antibacterial role and assay interpretation
  outcome: supported
  summary: The imported role is faithfully retained; primary activity context exists.
    Exact enantiomer equivalence and author-defined assay endpoints remain explicit
    before numerical curation.
  target_ids:
  - CHEBI:66459
  evidence_ids:
  - chebi
  - stereo2007
  - assay2025
  - assay-drawing
- assessment_id: mechanism
  area: completeness
  topic: Antimicrobial action versus other endpoints
  outcome: unknown
  summary: No inspected experiment establishes a direct antibacterial target. Host
    smooth-muscle and antimutagenic hypotheses do not supply one.
  target_ids:
  - CHEBI:66459
  evidence_ids:
  - record
  - bladder
  - bloodpressure
  - ames
  - assay2025
- assessment_id: optional
  area: representation
  topic: Producer, resistance, clinical, graph and dataset objects
  outcome: not_applicable
  summary: These optional objects are not asserted. A proposed plant biosynthetic
    route or extraction alone is not sufficient for a biosynthesizing-producer entry.
  target_ids:
  - CHEBI:66459
  evidence_ids:
  - record
  - assay2025
- assessment_id: provenance
  area: ownership
  topic: Source and curation history
  outcome: supported
  summary: SEEDED history and source ownership are consistent. Future scientific annotations
    and source-structure adjudication require their respective maintained owners.
  target_ids:
  - CHEBI:66459
  evidence_ids:
  - record
  - owner
findings:
- finding_id: F1
  issue_key: chebi-66459-relative-versus-absolute-experimental-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Natural-material evidence needs a relative-stereochemistry qualification
  description: The source-linked crystal study does not determine absolute handedness,
    while the database structure and systematic synonym specify it. Add explicit evidence
    scope and adjudicate any later absolute assignment before treating natural-material
    experiments as enantiomer-specific. This finding does not declare the database
    enantiomer wrong or authorize removal of all stereochemistry.
  target_ids:
  - CHEBI:66459
  field_paths:
  - chemical_structure
  - synonyms
  - evidence
  - discussions
  evidence_ids:
  - record
  - chebi
  - stereo2007
  - stereo-image
  - assay2025
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/3-4-secoisopimara-4-18-7-15-triene-3-oic-acid.yaml
    role: Curator-owned evidence and uncertainty discussion through the validated
      writer and a curation event
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Source structure and nomenclature; any correction requires maintained extraction
      and reseeding
  rule_id: 'native-review-checklist: Identity, Chemical structure and Evidence standard'
  native_severity: minor source-to-experiment stereochemical qualification gap
  normalization_reason: Authority identity and encodings agree, and no opposite enantiomer
    has been proved. The confirmed gap is experimental support for absolute natural-isolate
    mapping; it warrants qualification before exact-entity assay transfer.
- finding_id: F2
  issue_key: chebi-66459-assay-endpoint-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: New primary activity can be curated with its explicit endpoint definition
  description: A specific recent assay provides an enrichment path, subject to stereochemical
    mapping and preservation of its nonstandard MIC definition. No quantitative activity
    object is currently false.
  target_ids:
  - CHEBI:66459
  field_paths:
  - activity_spectrum
  - evidence
  - mode_of_action_notes
  evidence_ids:
  - record
  - assay2025
  - assay-drawing
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/3-4-secoisopimara-4-18-7-15-triene-3-oic-acid.yaml
    role: Curator-owned evidence and uncertainty discussion through the validated
      writer and a curation event
  rule_id: 'native-review-checklist: Activity and Mode of action'
  native_severity: informational optional evidence enrichment
  normalization_reason: Optional omissions are not schema defects; the follow-up is
    concrete but requires bounded interpretation.
actions:
- action_id: A1
  description: During separately authorized curation, document the relative-versus-absolute
    experimental boundary and search for a justified exact free-acid absolute assignment.
    If a source representation change is warranted, repair it through maintained source
    extraction and reseeding while preserving supported relative configuration.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:66459
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/3-4-secoisopimara-4-18-7-15-triene-3-oic-acid.yaml
    role: Curator-owned evidence and uncertainty discussion through the validated
      writer and a curation event
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Source structure and nomenclature; any correction requires maintained extraction
      and reseeding
  acceptance_checks:
  - A crystallographic drawing chosen arbitrarily is not cited as an absolute determination
    of the natural free acid.
  - Do not assign the opposite enantiomer, racemate or an entirely unstereospecified
    structure by assumption.
  - Keep a source-backed uncertainty discussion and use validated writer/history;
    any imported-structure correction must reproduce through the maintained pipeline.
- action_id: A2
  description: Match the2025 compound1 to the supported chemical scope, then add assay
    evidence with its author-defined endpoint, strain and conditions. Leave antibacterial
    mechanism unresolved unless direct primary support is found.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:66459
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/3-4-secoisopimara-4-18-7-15-triene-3-oic-acid.yaml
    role: Curator-owned evidence and uncertainty discussion through the validated
      writer and a curation event
  acceptance_checks:
  - Retain the approximately50-percent growth-inhibition MIC definition and separate
    neutralizing-agar MBC endpoint; do not infer clinical susceptibility.
  - Do not assign extract negatives or compounds2/3 results to the isolated compound,
    or convert proposed biosynthesis into proved production.
  - Run focused schema/strict validation, corpus reproduction and fullQC for native
    edits; retain SEEDED until native promotion criteria are met.
limitations:
- The 2001 isolation paper and 2004/2007 pharmacology studies were inspected as primary
  abstracts. The 2007 crystallographic paper was read in full from a freely hosted
  copy, and its stereochemical qualification was visually confirmed on page2282.
- The 2003 antimicrobial proceedings reference was inspected only as a bibliography
  entry in the 2007 paper; its experimental pages were not retrieved. No MIC or target
  is extracted from it.
- The 2025 paper abbreviates compound1 as a diene, while Figure1 depicts the exomethylene
  as well as the other two alkenes. The constitution/relative drawing matches this
  scaffold, but that does not independently establish absolute stereochemical equivalence.
- Reaxys was corroborated through official ChEBI rather than independently inspected.
  Bounded searches do not prove that no later exact absolute-configuration determination
  exists.
- No native structure is changed or declared to be the opposite enantiomer. Any proposed
  representation correction requires adjudicating source identity and preserving relative
  stereochemical information.
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
