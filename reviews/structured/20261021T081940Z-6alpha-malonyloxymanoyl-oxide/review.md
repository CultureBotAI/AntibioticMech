# 6α-malonyloxymanoyl oxide: supported exact compound with bounded assay-access limitations

- Review: 20261021T081940Z-6alpha-malonyloxymanoyl-oxide
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:12:17Z
- Finished UTC: 2026-10-21T08:19:40Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Exact native chemistry and the antibacterial/source-origin assertions are supported by official identity records and the adopted original abstract. One informational follow-up concerns claim-level assay enrichment after the complete original methods become available; no identity, role or required-field error was found. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, maintained source row and ownership, all adopted citation metadata/abstract, official chemical identities and bounded free full-text search.

Selection: Queue index064, CHEBI:66662 at its locked path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:66662 | data/antibiotics/antibacterial/6α-malonyloxymanoyl-oxide.yaml | generated | 6α-malonyloxymanoyl oxide |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:66662 | Focused LinkML validation exited0. |
| strict | passed | True | CHEBI:66662 | Focused one-record strict scan has zero ERROR rows. |
| chemistry | passed | False | CHEBI:66662 | Independent native SMILES/InChI parsing matches full stereochemical key, formula, masses, charge and source mint. |
| structured-context | not_applicable | False | CHEBI:66662 | Native record and inspected exact-compound primary abstract name no gene, protein target, pathway, transcriptomics dataset or stress-response claim. No relevant structured-adapter search or component summary applies. |
| full-primary | unavailable | False | CHEBI:66662 | Full2008 article and SI publisher requests returned403; institutional repository explicitly lists restricted access and no attached file; ResearchGate is request-only. No paid access or contact used. |
| reaxys | unavailable | False | CHEBI:66662 | Reaxys19154464 is corroborated in current ChEBI but not independently inspected through free registry access. |
| Authoritative full QC | failed | True | CHEBI:66662 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:66662 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:66662 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:66662 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:66662 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:66662 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:66662 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:66662 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:66662 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact form and synonym

identity: supported. Targets: CHEBI:66662.

Official full chemical structures, masses and internal parsing agree on the specified neutral malonate ester. The primary abstract names the exact compound2.

### Parents and registry

grounding: supported. Targets: CHEBI:66662.

Three parents are chemically broader; external Reaxys link remains corroborated only in ChEBI.

### Antibacterial definition and filing

evidence: supported. Targets: CHEBI:66662.

Adopted original abstract directly supports antibacterial activity for compound2 and the broad role. Per-strain values and experimental details require the full article.

### Plant extraction source

evidence: supported. Targets: CHEBI:66662.

The exact original abstract supports the native aerial-parts isolation statement. No biosynthetic producer or BGC is inferred.

### Mode, targets and causal scope

completeness: unknown. Targets: CHEBI:66662.

No exact-compound mechanism was established in inspected material. Absence of optional mechanism/graph fields is appropriate at this evidence boundary and is not a defect.

### Activity enrichment

completeness: unknown. Targets: CHEBI:66662.

The published MIC range provides a concrete enrichment lead, but numerical structured entries need original method and strain mapping. Clinical,resistance,dataset and producer claims are unasserted rather than erroneous.

### Maintained provenance/status

ownership: supported. Targets: CHEBI:66662.

Source row and generated field ownership are clear; all13 initial hashes remain unchanged and no scientific status or history was altered.

### Focused validators

schema: supported. Targets: CHEBI:66662.

Schema,strict and independent chemistry pass.

## Findings

### F1: Retrieve original assay details before quantitative enrichment

informational / open / confirmed; issue key: chebi-66662-primary-assay-enrichment-followup.

The accessible adopted abstract directly supports compound2 antibacterial activity and the7–20µg/mL range. Optional activity observations can be added once the full table/method supports each organism, strain, endpoint and assay condition. No mechanism or producer claim should be supplied merely from labdane family or plant isolation.

## Recommended Actions And Acceptance Checks

### A1

When a legitimate free full copy is available, inspect compound2 structure characterization and original assay methods/table before optional enrichment.

- Map compound2 to the exact neutral malonate ester, retaining six-centre stereochemical scope; keep acetate1 and n-butyl ester3 separate.
- Capture individual organism/strain,MIC,units,qualifier,method,medium,inoculum,incubation and controls from inspected primary text. Do not assign the abstract range to every strain.
- Keep aerial-parts isolation as source evidence; a future producer/BGC assertion needs actual biosynthesis evidence. Do not infer a target from labdane analogues or absence in a bounded search.
- Write any authorized additions with write_validated_antibiotic and record_curation_event at the actual native path, then focused schema/strict plus required corpus/shared checks. No generated identity correction is currently justified.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/6α-malonyloxymanoyl-oxide.yaml; Entire native YAML read after064 initial capture. | supports | The SEEDED/EXACT antibacterial record has a malonate-labdane definition, specific aerial-parts isolation claim, one exact systematic synonym, three chemical parents, role33282, neutral six-stereocentre structure, Reaxys19154464, one source concept and three seed/reseed events. No optional evidence, activity_spectrum, mechanism, targets, producer, resistance, clinical status or graph objects are asserted. |
| source | data/raw/chebi_antimicrobials.tsv; Row1619 in064-raw.json; conf/sources.yaml; extractor176–339 and seeder790–809,1483–1570; MANIFEST. | supports | The record reproduces the maintained ChEBI row. Sole adopted citationPMID18582112 is deliberately stored as a research lead rather than auto-seeded claim evidence. Mechanism_role_ids is empty. Source version2026-08-30 and native seed/reseed history agree. All13 initial captured input hashes remain unchanged. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:66662; Complete official064-chebi.html/txt; PubChem CID24970705 property response064-pubchem.json. | supports | ChEBI and PubChem agree on full keyJZRGFUZJIZSKTF-ALFLKXBZSA-N, native full InChI, C23H36O5, neutral charge and six specified stereocentres. The systematic synonym is coherent with the structure. Parents36770 labdane diterpenoid,37407 cyclic ether,38083 malonate ester are broader.33282 is antibacterial agent. Reaxys19154464 remains source-asserted. Current ChEBI links the aerial part of Stemodia foliosa to the same2008 PMID. |
| chemistry | Independent RDKit calculation; 064-chemistry.json/log and inspectedchem005.py. | supports | SMILES and InChI each parse to the same full key, C23H36O5, one neutral fragment, average mass392.536 and exact mass392.256274252. All six stereocentres are specified. Repository SHA256 source mint antibioticmech:chebi-99bfe821e3 matches. These checks establish internal/database consistency, not an independent proof of the original absolute-stereochemistry experiment. |
| primary | PMID:18582112; DOI:10.1021/np800106x; complete original abstract and bibliographic metadata in064-epmc.json; official PubMed/ACS and author-institution abstract. | supports | The2008 original report explicitly names6alpha-malonyloxymanoyl oxide as compound2, separately from acetate1 and n-butyl ester3. It reports isolation from Stemodia foliosa aerial parts and structure characterization by HRESIMS and1D/2D NMR. Compound2 showed moderate antibacterial activity, MIC range7–20µg/mL, in a panel of S.aureus,B.cereus,B.subtilis,B.anthracis,Micrococcus luteus,M.smegmatis,M.phlei. The accessible abstract does not map numerical endpoints to individual strains or give medium, incubation, inoculum or assay method; it states no molecular target. |
| access | https://acervodigital.unesp.br/handle/11449/26081; Inspected institutional item lines79–121; ACS full/abstract/PDF/SI routes; ResearchGate publication5274331. | context_only | The institution confirms title, authors,2008 journal volume71 pages1291–1293, DOI and full abstract, but marks restricted access and no attached file. ACS abstracts were indexed/read, while mainPDF and SI returned403. ResearchGate explicitly offered only an author request. These limits prevent inspecting assay tables and original stereochemical argument, not using the accessible exact-compound abstract for its broad assertions. |
| search | CultureBotAI/AntibioticMech; 064-local-hits.txt;064-maintained-search.txt; bounded exact-identity web search. | context_only | Ignored-inclusive focused search found no target-specific maintained decision, overlay or prior review in the searched paths. Exact-name/DOI searches recovered the adopted paper and secondary labdane summaries, not an inspected exact-compound target mechanism. A separate isolation/thesis lead and metabolomics annotations do not independently establish biosynthesis or new activity here. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Whole-record identity, evidence, exact compound form, optional fields and producer scope; CURATION/HARMONIZATION. | supports | Optional claim collections are not mandatory. Every quantitative activity needs method/units and claim evidence; do not invent strain-specific endpoints from an abstract range or derive mechanism from chemical family. Isolation source alone does not establish a biosynthetic producer or BGC. |
| validation | Documented focused native checks; 064-focused-results.json;064-schema.log,064-strict.log/tsv,064-chemistry.json/log. | supports | Focused schema,strict and chemistry commands each exited0. Actual shared gate outcomes are recorded separately in this bundle. |

## Limits And Additional Notes

- Only the complete abstract of the sole adopted2008 citation was accessible. Full main text and SI returned403; the institutional repository lists restricted access/no attached file and ResearchGate is request-only.
- Per-strainMICs,assay methods,voucher details and original absolute-stereochemical reasoning are therefore unverified. Official structure consistency and broad abstract support are not substitutes for those details.
- Reaxys19154464 was corroborated in current ChEBI but not independently inspected. No gene/target/dataset context in the exact record or accessible original abstract made a structured adapter search applicable. All13 captured hashes remain unchanged.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T081940Z-6alpha-malonyloxymanoyl-oxide
kind: record
repository: CultureBotAI/AntibioticMech
title: '6α-malonyloxymanoyl oxide: supported exact compound with bounded assay-access
  limitations'
started_at: '2026-10-21T08:12:17Z'
finished_at: '2026-10-21T08:19:40Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author the record. Captured exact target before judgment,
    read the entire native record and maintained source row, and inspected official
    chemistry plus original biological sources independently.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: Exact native chemistry and the antibacterial/source-origin assertions are
  supported by official identity records and the adopted original abstract. One informational
  follow-up concerns claim-level assay enrichment after the complete original methods
  become available; no identity, role or required-field error was found. Scientific
  assessment retains the stated evidence limits; full verification is blocked by the
  shared native-library failure.
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
  - path: data/antibiotics/antibacterial/6α-malonyloxymanoyl-oxide.yaml
    sha256: af9af215cb57b36189ae45b0ef90395dbe72358f430d1c700d4ace0967f82562
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
- target_id: CHEBI:66662
  path: data/antibiotics/antibacterial/6α-malonyloxymanoyl-oxide.yaml
  label: 6α-malonyloxymanoyl oxide
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
  description: Entire exact native record, maintained source row and ownership, all
    adopted citation metadata/abstract, official chemical identities and bounded free
    full-text search.
  selection: Queue index064, CHEBI:66662 at its locked path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:66662
  exclusions:
  - target: Acetoxy analogue1, n-butyl ester3, other manoyl/labdane compounds, extracts
      and untargeted metabolomics annotations
    reason: Distinct structures, mixtures or uncertain identifications; do not transfer
      their biological mechanisms or activity.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Focused LinkML validation exited0.
  target_ids:
  - CHEBI:66662
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/6α-malonyloxymanoyl-oxide.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Focused one-record strict scan has zero ERROR rows.
  target_ids:
  - CHEBI:66662
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/6α-malonyloxymanoyl-oxide.yaml --out /private/tmp/am-review-session/064-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Independent native SMILES/InChI parsing matches full stereochemical key,
    formula, masses, charge and source mint.
  target_ids:
  - CHEBI:66662
  evidence_ids:
  - chemistry
  command: .venv/bin/python /private/tmp/am-review-session/chem005.py 64
  exit_code: 0
  expected_exit_code: 0
- check_id: structured-context
  name: structured-context
  status: not_applicable
  required: false
  summary: Native record and inspected exact-compound primary abstract name no gene,
    protein target, pathway, transcriptomics dataset or stress-response claim. No
    relevant structured-adapter search or component summary applies.
  target_ids:
  - CHEBI:66662
  evidence_ids:
  - record
  - primary
  - search
- check_id: full-primary
  name: full-primary
  status: unavailable
  required: false
  summary: Full2008 article and SI publisher requests returned403; institutional repository
    explicitly lists restricted access and no attached file; ResearchGate is request-only.
    No paid access or contact used.
  target_ids:
  - CHEBI:66662
  evidence_ids:
  - access
- check_id: reaxys
  name: reaxys
  status: unavailable
  required: false
  summary: Reaxys19154464 is corroborated in current ChEBI but not independently inspected
    through free registry access.
  target_ids:
  - CHEBI:66662
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
  - CHEBI:66662
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
  - CHEBI:66662
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
  - CHEBI:66662
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
  - CHEBI:66662
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
  - CHEBI:66662
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
  - CHEBI:66662
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
  - CHEBI:66662
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
  - CHEBI:66662
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
  - CHEBI:66662
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/6α-malonyloxymanoyl-oxide.yaml
  locator: Entire native YAML read after064 initial capture.
  accessed_at: '2026-10-21T08:14:35Z'
  support: supports
  summary: The SEEDED/EXACT antibacterial record has a malonate-labdane definition,
    specific aerial-parts isolation claim, one exact systematic synonym, three chemical
    parents, role33282, neutral six-stereocentre structure, Reaxys19154464, one source
    concept and three seed/reseed events. No optional evidence, activity_spectrum,
    mechanism, targets, producer, resistance, clinical status or graph objects are
    asserted.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Row1619 in064-raw.json; conf/sources.yaml; extractor176–339 and seeder790–809,1483–1570;
    MANIFEST.
  accessed_at: '2026-10-21T08:14:35Z'
  support: supports
  summary: The record reproduces the maintained ChEBI row. Sole adopted citationPMID18582112
    is deliberately stored as a research lead rather than auto-seeded claim evidence.
    Mechanism_role_ids is empty. Source version2026-08-30 and native seed/reseed history
    agree. All13 initial captured input hashes remain unchanged.
  snapshot_sha256: fa8f2db202ce483bb5a723f26617bf5288b1d205bf2db6aa441531660396608a
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:66662
  locator: Complete official064-chebi.html/txt; PubChem CID24970705 property response064-pubchem.json.
  accessed_at: '2026-10-21T08:14:35Z'
  support: supports
  summary: ChEBI and PubChem agree on full keyJZRGFUZJIZSKTF-ALFLKXBZSA-N, native
    full InChI, C23H36O5, neutral charge and six specified stereocentres. The systematic
    synonym is coherent with the structure. Parents36770 labdane diterpenoid,37407
    cyclic ether,38083 malonate ester are broader.33282 is antibacterial agent. Reaxys19154464
    remains source-asserted. Current ChEBI links the aerial part of Stemodia foliosa
    to the same2008 PMID.
  snapshot_sha256: 4ea81eabb9144dfed6319502f1d6365d48a6796fd2ac804de236e082ff435970
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit calculation
  locator: 064-chemistry.json/log and inspectedchem005.py.
  accessed_at: '2026-10-21T08:14:35Z'
  support: supports
  summary: SMILES and InChI each parse to the same full key, C23H36O5, one neutral
    fragment, average mass392.536 and exact mass392.256274252. All six stereocentres
    are specified. Repository SHA256 source mint antibioticmech:chebi-99bfe821e3 matches.
    These checks establish internal/database consistency, not an independent proof
    of the original absolute-stereochemistry experiment.
  snapshot_sha256: b43b847a4a108372e9b41acab8cbd54f5f52bd925b1cec953dbeb8de49d1d0a2
- evidence_id: primary
  kind: primary_source
  reference: PMID:18582112
  locator: DOI:10.1021/np800106x; complete original abstract and bibliographic metadata
    in064-epmc.json; official PubMed/ACS and author-institution abstract.
  accessed_at: '2026-10-21T08:14:35Z'
  support: supports
  summary: The2008 original report explicitly names6alpha-malonyloxymanoyl oxide as
    compound2, separately from acetate1 and n-butyl ester3. It reports isolation from
    Stemodia foliosa aerial parts and structure characterization by HRESIMS and1D/2D
    NMR. Compound2 showed moderate antibacterial activity, MIC range7–20µg/mL, in
    a panel of S.aureus,B.cereus,B.subtilis,B.anthracis,Micrococcus luteus,M.smegmatis,M.phlei.
    The accessible abstract does not map numerical endpoints to individual strains
    or give medium, incubation, inoculum or assay method; it states no molecular target.
  snapshot_sha256: b0f4c0f9f0394128060f9d2e422b5941ccce0eff6fb50b4587341bd9fdd61311
- evidence_id: access
  kind: authority
  reference: https://acervodigital.unesp.br/handle/11449/26081
  locator: Inspected institutional item lines79–121; ACS full/abstract/PDF/SI routes;
    ResearchGate publication5274331.
  accessed_at: '2026-10-21T08:14:35Z'
  support: context_only
  summary: The institution confirms title, authors,2008 journal volume71 pages1291–1293,
    DOI and full abstract, but marks restricted access and no attached file. ACS abstracts
    were indexed/read, while mainPDF and SI returned403. ResearchGate explicitly offered
    only an author request. These limits prevent inspecting assay tables and original
    stereochemical argument, not using the accessible exact-compound abstract for
    its broad assertions.
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 064-local-hits.txt;064-maintained-search.txt; bounded exact-identity web
    search.
  accessed_at: '2026-10-21T08:14:35Z'
  support: context_only
  summary: Ignored-inclusive focused search found no target-specific maintained decision,
    overlay or prior review in the searched paths. Exact-name/DOI searches recovered
    the adopted paper and secondary labdane summaries, not an inspected exact-compound
    target mechanism. A separate isolation/thesis lead and metabolomics annotations
    do not independently establish biosynthesis or new activity here.
  search_scope: rg --no-ignore --hidden identifier,label,slug throughout007 excluding.git/.venv;
    focused CHEBI:66662,JZRGFUZJIZSKTF,malonyloxymanoyl across curation,reviews,reports/yaml_record_review,conf
    excluding queue. Web6α/6alpha-malonyloxymanoyl oxide plus antibacterial,MIC,mechanism,target;
    exact PMID18582112/DOI10.1021/np800106x plus PDF/Figshare/ResearchGate. Official
    ChEBI,PubChem,PubMed,EuropePMC,ACS and author-institution repository inspected;
    secondary reviews/vendor snippets only discovery context.
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Whole-record identity, evidence, exact compound form, optional fields and
    producer scope; CURATION/HARMONIZATION.
  accessed_at: '2026-10-21T08:14:35Z'
  support: supports
  summary: Optional claim collections are not mandatory. Every quantitative activity
    needs method/units and claim evidence; do not invent strain-specific endpoints
    from an abstract range or derive mechanism from chemical family. Isolation source
    alone does not establish a biosynthetic producer or BGC.
- evidence_id: validation
  kind: validation
  reference: Documented focused native checks
  locator: 064-focused-results.json;064-schema.log,064-strict.log/tsv,064-chemistry.json/log.
  accessed_at: '2026-10-21T08:14:35Z'
  support: supports
  summary: Focused schema,strict and chemistry commands each exited0. Actual shared
    gate outcomes are recorded separately in this bundle.
  snapshot_sha256: 58e8309e9b4599d4984353d55c05d3df6f5bbb061cc80240bd40eb3addfe0bb6
assessments:
- assessment_id: identity
  area: identity
  topic: Exact form and synonym
  outcome: supported
  summary: Official full chemical structures, masses and internal parsing agree on
    the specified neutral malonate ester. The primary abstract names the exact compound2.
  target_ids:
  - CHEBI:66662
  evidence_ids:
  - identity
  - chemistry
  - primary
- assessment_id: grounding
  area: grounding
  topic: Parents and registry
  outcome: supported
  summary: Three parents are chemically broader; external Reaxys link remains corroborated
    only in ChEBI.
  target_ids:
  - CHEBI:66662
  evidence_ids:
  - identity
  - chemistry
- assessment_id: activity
  area: evidence
  topic: Antibacterial definition and filing
  outcome: supported
  summary: Adopted original abstract directly supports antibacterial activity for
    compound2 and the broad role. Per-strain values and experimental details require
    the full article.
  target_ids:
  - CHEBI:66662
  evidence_ids:
  - primary
  - access
- assessment_id: origin
  area: evidence
  topic: Plant extraction source
  outcome: supported
  summary: The exact original abstract supports the native aerial-parts isolation
    statement. No biosynthetic producer or BGC is inferred.
  target_ids:
  - CHEBI:66662
  evidence_ids:
  - primary
  - rubric
- assessment_id: mechanism
  area: completeness
  topic: Mode, targets and causal scope
  outcome: unknown
  summary: No exact-compound mechanism was established in inspected material. Absence
    of optional mechanism/graph fields is appropriate at this evidence boundary and
    is not a defect.
  target_ids:
  - CHEBI:66662
  evidence_ids:
  - primary
  - search
  - rubric
- assessment_id: optional
  area: completeness
  topic: Activity enrichment
  outcome: unknown
  summary: The published MIC range provides a concrete enrichment lead, but numerical
    structured entries need original method and strain mapping. Clinical,resistance,dataset
    and producer claims are unasserted rather than erroneous.
  target_ids:
  - CHEBI:66662
  evidence_ids:
  - primary
  - access
  - rubric
- assessment_id: ownership
  area: ownership
  topic: Maintained provenance/status
  outcome: supported
  summary: Source row and generated field ownership are clear; all13 initial hashes
    remain unchanged and no scientific status or history was altered.
  target_ids:
  - CHEBI:66662
  evidence_ids:
  - source
  - rubric
- assessment_id: schema
  area: schema
  topic: Focused validators
  outcome: supported
  summary: Schema,strict and independent chemistry pass.
  target_ids:
  - CHEBI:66662
  evidence_ids:
  - validation
  - chemistry
findings:
- finding_id: F1
  issue_key: chebi-66662-primary-assay-enrichment-followup
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Retrieve original assay details before quantitative enrichment
  description: The accessible adopted abstract directly supports compound2 antibacterial
    activity and the7–20µg/mL range. Optional activity observations can be added once
    the full table/method supports each organism, strain, endpoint and assay condition.
    No mechanism or producer claim should be supplied merely from labdane family or
    plant isolation.
  target_ids:
  - CHEBI:66662
  field_paths:
  - evidence
  - activity_spectrum
  - discussions
  evidence_ids:
  - primary
  - access
  - rubric
  rule_id: 'native-review-checklist: Activity/Evidence/Producer'
  native_severity: informational optional enrichment
  normalization_reason: No mandatory field or explicit native biological assertion
    was shown wrong; this records an actionable bounded evidence gap.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/6α-malonyloxymanoyl-oxide.yaml
    role: Curator-owned claim evidence/discussion through write_validated_antibiotic
      and native history
actions:
- action_id: A1
  description: When a legitimate free full copy is available, inspect compound2 structure
    characterization and original assay methods/table before optional enrichment.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:66662
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/6α-malonyloxymanoyl-oxide.yaml
    role: Curator-owned claim evidence/discussion through write_validated_antibiotic
      and native history
  acceptance_checks:
  - Map compound2 to the exact neutral malonate ester, retaining six-centre stereochemical
    scope; keep acetate1 and n-butyl ester3 separate.
  - Capture individual organism/strain,MIC,units,qualifier,method,medium,inoculum,incubation
    and controls from inspected primary text. Do not assign the abstract range to
    every strain.
  - Keep aerial-parts isolation as source evidence; a future producer/BGC assertion
    needs actual biosynthesis evidence. Do not infer a target from labdane analogues
    or absence in a bounded search.
  - Write any authorized additions with write_validated_antibiotic and record_curation_event
    at the actual native path, then focused schema/strict plus required corpus/shared
    checks. No generated identity correction is currently justified.
limitations:
- Only the complete abstract of the sole adopted2008 citation was accessible. Full
  main text and SI returned403; the institutional repository lists restricted access/no
  attached file and ResearchGate is request-only.
- Per-strainMICs,assay methods,voucher details and original absolute-stereochemical
  reasoning are therefore unverified. Official structure consistency and broad abstract
  support are not substitutes for those details.
- Reaxys19154464 was corroborated in current ChEBI but not independently inspected.
  No gene/target/dataset context in the exact record or accessible original abstract
  made a structured adapter search applicable. All13 captured hashes remain unchanged.
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
