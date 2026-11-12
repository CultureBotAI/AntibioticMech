# Etimicin: supported semisynthetic identity with bounded sulfate evidence

- Review: 20261021T155542Z-etimicin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T15:30:52Z
- Finished UTC: 2026-10-21T15:55:42Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native neutral etimicin structure and twelve assigned stereocentres are coherent. The original patent distinguishes the free base, its sulfate and the natural gentamicin precursor. DrugCentral 5171 names etimicin and is an appropriate drug-level association under the schema; its less specified structure export is contextual rather than an exact-equivalence failure. All ten adopted literature leads were assessed, preserving salt, combination and host-toxicity boundaries. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 419; one exact neutral compound. Original thirteen input hashes preserved within 20 expanded inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:134705 | data/antibiotics/antibacterial/etimicin.yaml | generated | etimicin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Structured source catalog before protein follow-up | passed | False | CHEBI:134705 | Catalog succeeded; no native exact gene or dataset required a covered organism query. |
| Focused chemistry verification | passed | False | CHEBI:134705 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:134705 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:134705 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:134705 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:134705 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:134705 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:134705 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:134705 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:134705 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:134705 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:134705 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:134705 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Neutral semisynthetic structure and synonym scope

identity: supported. Targets: CHEBI:134705.

Native SMILES, InChI, formula, mass and twelve stereocentres are coherent. Current ChEBI and the original patent constitution/numbered glycoside support the specified 1-N-ethylgentamicin C1a entity. Etilmicin is used as an alternate spelling in the original adopted clinical source; no product-brand claim is inferred.

### Drug-level DrugCentral association

grounding: supported. Targets: CHEBI:134705.

DrugCentral 5171 names etimicin. Its export has the same constitution and eleven matching centres while leaving the purpurosamine anomeric centre unspecified. The schema explicitly permits drug-level identifiers to cover stereoisomers, so this difference establishes no native grounding defect and does not require removing the link. No opposite epimer or racemate is inferred.

### Antibacterial and aminoglycoside roles

scope: supported. Targets: CHEBI:134705.

The original sulfate antibacterial study and later exact etimicin-sulfate tests support antibacterial activity at the active-moiety level. The definition does not establish effectiveness against every aminoglycoside-resistant isolate; quantitative or clinical extrapolation beyond the tested studies is not adopted.

### Analytical, clinical and precursor evidence placement

evidence: supported. Targets: CHEBI:134705.

The frozen bibliography contains several analytical/host-exposure papers rather than target experiments. Their presence is not treated as proof of every definition claim. Clinical combinations remain combinations, and precursor biosynthesis remains gentamicin C1a production.

### Optional target, resistance and activity enrichment

completeness: unknown. Targets: CHEBI:134705.

The record has no molecular-target, mode, resistance, activity_spectrum or causal-graph entries. Their absence is not a required-schema defect. Primary quantitative enrichment would need exact salt/potency basis, strain panel and assay metadata; host mitochondrial toxicity cannot fill a bacterial-target field.

### Producer, FDA and collection assertions

scope: not_applicable. Targets: CHEBI:134705.

No FDA product, producer or activity-collection assertion is present. The inspected Micromonospora studies do not justify inventing a natural etimicin producer.

### Actual source and generated history

provenance: supported. Targets: CHEBI:134705.

All four seeded/reseeded events and exact adopted ChEBI fields are coherent. Original thirteen hashes are preserved within 20 expanded inputs. The DrugCentral association is interpreted according to its drug-level field semantics.

### Focused native validation

schema: supported. Targets: CHEBI:134705.

Schema, strict validation, chemistry and source-mint checks pass. Exact structural identifiers are distinguished from the broader drug-level associations explicitly permitted by the schema.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/etimicin.yaml; Entire 75-line native YAML including all names, sources and four history events | supports | The exact neutral etimicin record was read completely; no sulfate preparation or precursor producer is silently substituted. |
| owners | 412413419-raw-rows.json; Exact CHEBI134705 source row and maintained extractor/seeder | supports | The adopted definition, structure, synonyms, roles, patent, DrugCentral identifier and ten PMID leads were inspected in their actual maintained row. Original captures are preserved. |
| search | 412413419-all-local-paths.txt; Hidden- and gitignore-inclusive exact identifier/name search | context_only | The search covered data, curation, conf, scripts, src, reports and reviews. No exact curator override or additional native activity collection was identified. No absence of external research is inferred. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/134705/; Current CHEBI134705 identity, structure, names, CAS and parent relations | supports | Current ChEBI agrees with the native neutral formula, key and all twelve specified stereocentres, identifies the 1-N-ethylgentamicin C1a relationship and supports aminoglycoside/amino-cyclitol-glycoside classification. CAS59711-96-5 is attached to this exact entity. |
| drugcentral | https://drugcentral.org/drugcard/5171; Current DrugCentral 5171 named drug card and linked structure export | supports | The card names etimicin and supports the native drug-level association. Its linked molfile leaves one tetrahedral centre unspecified, but drug_xrefs explicitly does not assert exact stereochemical equivalence. |
| drugcentral-structure | https://drugcentral.org/drug/5171/molfile; Official linked /drug/5171/molfile structure | context_only | Independent parsing gives NZGMVSJQULXLHF-NORJTPJDSA-N with /t19?; native/current ChEBI give NZGMVSJQULXLHF-RAKCNUBFSA-N with /t19+. Formula and connectivity match, and all other eleven tetrahedral assignments agree. This is under-specification, not a demonstrated opposite epimer. This representational difference does not invalidate the schema-permitted drug-level association. |
| chemistry | 419-chemistry.json; 412413419-xref-chemistry.json; RDKit 2026.03.5 independent native and authority parsing; batch019 interpreter against batch042 cwd | supports | Native SMILES and InChI agree in formula C21H43N5O7, neutral charge, masses, all twelve stereocentres and source mint. DrugCentral differs only at its unassigned glycosidic centre. |
| atom-map | 419-anomeric-map.json; InChI atom 19 and original patent numbered sugar | supports | InChI atom 19 is the right-hand purpurosamine anomeric carbon C1-prime: it connects to sugar carbon 11, ring oxygen 31 and glycosidic oxygen 32, which connects to deoxystreptamine carbon 16. Native assignment is R; DrugCentral marks the centre unknown. Original patent general formula 1 depicts the defined glycosidic geometry. |
| patent | https://patents.google.com/patent/US5814488/en; US5814488, disclosure, general formula 1 compound (3), Example 4 and separate formulation examples | supports | The original patent explicitly names 1-N-ethylgentamicin C1a as etimicin. Example 4(3) isolates the free base, followed separately by sulfate formation in 4(4). The reported protonated mass signal 478 is not the molecular weight of a sodium adduct or a new salt. Gentamicin C1a is the fermentation precursor; the ethyl derivative is semisynthetic. Other gentamicin congeners and formulations remain distinct. |
| patent-pdf | https://patentimages.storage.googleapis.com/7d/7b/68/ad430bb4ef8f20/US5814488.pdf; Actual PDF page 11, printed column 2, general formula [1] and compound (3) | supports | The actual structure drawing was viewed. It numbers the right-hand sugar anomeric position 1-prime and specifies its glycosidic geometry. Compound (3) selects hydrogen at R1–R4 and ethyl at R5, consistent with the native 1-N-ethylgentamicin C1a constitution. This is not evidence that every patent formulation is neutral free base. |
| patent-figure | 419-patent-page11.png; Rasterized original PDF page 11 viewed directly | supports | Preserved visual locator for the numbered glycoside and exact compound-variable assignment; structural interpretation is retained separately from the source image. |
| adopted-abstracts | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28EXT_ID%3A11776118%20OR%20EXT_ID%3A11931698%20OR%20EXT_ID%3A22918626%20OR%20EXT_ID%3A22983905%20OR%20EXT_ID%3A25233899%20OR%20EXT_ID%3A25464101%20OR%20EXT_ID%3A26924270%20OR%20EXT_ID%3A28881316%20OR%20EXT_ID%3A30814950%20OR%20EXT_ID%3A31847403%29%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=100; All ten adopted PMID records and complete original abstracts | context_only | Every frozen adopted PMID lead was resolved and its original abstract read. Clinical studies, analytical detection, rat toxicity, precursor production and antibacterial sulfate experiments are distinguished in the explicit disposition ledger. |
| adopted-dispositions | 419-adopted-dispositions.json; Per-PMID reading depth and exact endpoint/material disposition | context_only | All ten adopted bibliography leads have explicit source-specific dispositions, including full-text access limits and salt/combination boundaries. |
| precursor-study | https://pmc.ncbi.nlm.nih.gov/articles/PMC6963548/?pdf=1; PMID31847403, DOI10.3390/antibiotics8040267; Introduction, gentamicin analysis methods and conclusions | supports | The original study engineers genK/genL-related gentamicin precursor production in M. purpurea. Its product is gentamicin C1a used for later chemical synthesis of etimicin. It cannot establish a natural etimicin producer or transfer precursor activity to etimicin. |
| combination-study | https://pmc.ncbi.nlm.nih.gov/articles/PMC6381041/?pdf=1; PMID30814950, DOI10.3389/fphar.2019.00092; Methods and relevant combination results | partial | The original study reports etilmicin with sulbactam or meropenem in retrospective VAP treatment and broth/checkerboard tests on 36 MDR A. baumannii strains. It uses MH broth, serial dilution, 37 °C overnight and historical CLSI M100-S23. Salt/purity is not established in the inspected method; combination outcomes do not prove monotherapy response or direct ribosomal binding. |
| primary2020 | https://pmc.ncbi.nlm.nih.gov/articles/PMC7468263/?pdf=1; PMID31937930, DOI10.1038/s41401-019-0342-5; Chemicals, antibacterial Methods and Table 1 | partial | The original later study explicitly uses etimicin sulfate from Changzhou Fangyuan. It tests 36 clinical isolates, six each of E. coli, K. pneumoniae, E. cloacae, P. mirabilis, P. aeruginosa and S. aureus, by broth microdilution at 37 °C for 18–24 h with a visible-growth endpoint. Table 1 supports broad tested activity but contains unusual interpolated MIC50/MIC90 values; no quantitative observation is imported. Rat mitochondrial/toxicity findings are not a bacterial target mechanism. |
| adapter | iModulonDB dataset catalog; 412413419-adapter-catalog.txt; actual pre-research runner | context_only | The catalog was checked before protein follow-up. No exact protein, taxon-specific locus or dataset is asserted in the native etimicin record. Later precursor biosynthesis and host-toxicity proteins are not silently adopted as native antibacterial targets. |
| gates | 419-focused-results.json; Actual native schema/strict and independent chemistry commands | supports | All focused native checks pass. The external DrugCentral structure comparison is contextual; its less specified stereochemistry does not violate drug_xrefs semantics. |
| access-boundaries | 412413419-fetch1.json through 412413419-fetch4.json; Exact request URLs, timestamps, HTTP responses and hashes | context_only | DrugCentral initially requested a nonexistent structure route; the actual card-linked molfile was then retrieved and parsed. The 2012 antibacterial publisher response was client-challenge HTML, not a full paper. The 2020 DOC supplement was downloaded, but text conversion did not preserve its embedded structure image; that unviewed image is not used as structural evidence. |
| drug-xref-semantics | src/antibioticmech/schema/antibioticmech.yaml; AntibioticRecord.drug_xrefs, lines200–206 | supports | The schema explicitly defines DrugBank, DrugCentral and KEGG DRUG identifiers as drug-level associations covering parents, salts and stereoisomers. These identifiers are not same-structure equivalences; exact-equivalence rules apply to xrefs instead. |

## Limits And Additional Notes

- All ten adopted PMID abstracts were inspected. Full methods were not obtained for the older clinical and analytical sources; the 2012 antibacterial publisher page returned a JavaScript challenge. No uninspected numeric or isolated-material detail is inferred.
- The original patent disclosure, exact free-base/sulfate Example 4, general formula and actual numbered structure page were inspected. All 22 patent pages and every NMR/MS trace were not independently reanalyzed.
- The 2020 study was inspected for exact sulfate material, antibacterial Methods and Table 1. Host toxicology figures and the embedded structure image in its legacy DOC supplement were not independently viewed; the original patent drawing provides the retained structural evidence.
- Etimicin-sulfate and combination-therapy results support bounded active-moiety context but are not numerically transferred into neutral free-base MIC observations. Modern resistance surveillance and clinical efficacy are not exhaustively reviewed.
- The CAS assignment was checked in the current ChEBI record. A separate Common Chemistry page could not be retrieved through the attempted web route, so independent CAS-registry verification is not claimed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native or maintained source was edited. Original captures and hashes were preserved; all expanded inputs were checked unchanged. Optional links, tags and notes are specific to etimicin.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T155542Z-etimicin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Etimicin: supported semisynthetic identity with bounded sulfate evidence'
started_at: '2026-10-21T15:30:52Z'
finished_at: '2026-10-21T15:55:42Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
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
summary: The native neutral etimicin structure and twelve assigned stereocentres are
  coherent. The original patent distinguishes the free base, its sulfate and the natural
  gentamicin precursor. DrugCentral 5171 names etimicin and is an appropriate drug-level
  association under the schema; its less specified structure export is contextual
  rather than an exact-equivalence failure. All ten adopted literature leads were
  assessed, preserving salt, combination and host-toxicity boundaries. Scientific
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
  - path: data/antibiotics/antibacterial/etimicin.yaml
    sha256: 4e17237c2e7b9111d9869955958030330b23ab4d6102676dfcb1816b24271859
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
- target_id: CHEBI:134705
  path: data/antibiotics/antibacterial/etimicin.yaml
  label: etimicin
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
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 419; one exact neutral compound. Original thirteen input
    hashes preserved within 20 expanded inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:134705
checks:
- check_id: structured-adapter
  name: Structured source catalog before protein follow-up
  status: passed
  required: false
  target_ids:
  - CHEBI:134705
  evidence_ids:
  - adapter
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
  exit_code: 0
  expected_exit_code: 0
  summary: Catalog succeeded; no native exact gene or dataset required a covered organism
    query.
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:134705
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/412413419-focused.py
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:134705
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/etimicin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:134705
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/etimicin.yaml --out /private/tmp/am-review-session/419-strict.tsv
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
  - CHEBI:134705
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
  - CHEBI:134705
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
  - CHEBI:134705
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
  - CHEBI:134705
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
  - CHEBI:134705
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
  - CHEBI:134705
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
  - CHEBI:134705
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
  - CHEBI:134705
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
  - CHEBI:134705
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/etimicin.yaml
  locator: Entire 75-line native YAML including all names, sources and four history
    events
  accessed_at: '2026-10-21T15:44:01Z'
  support: supports
  summary: The exact neutral etimicin record was read completely; no sulfate preparation
    or precursor producer is silently substituted.
- evidence_id: owners
  kind: record_content
  reference: 412413419-raw-rows.json
  locator: Exact CHEBI134705 source row and maintained extractor/seeder
  accessed_at: '2026-10-21T15:44:01Z'
  support: supports
  summary: The adopted definition, structure, synonyms, roles, patent, DrugCentral
    identifier and ten PMID leads were inspected in their actual maintained row. Original
    captures are preserved.
  snapshot_sha256: c546fff3c15dd28b31ced02ac53f2f0e227666149841f6d23b09c868299cbed7
- evidence_id: search
  kind: search
  reference: 412413419-all-local-paths.txt
  locator: Hidden- and gitignore-inclusive exact identifier/name search
  accessed_at: '2026-10-21T15:44:01Z'
  support: context_only
  summary: The search covered data, curation, conf, scripts, src, reports and reviews.
    No exact curator override or additional native activity collection was identified.
    No absence of external research is inferred.
  search_scope: rg --no-ignore --hidden -il 'CHEBI:60070|CHEBI:404903|CHEBI:134705|ertapenem|etimicin'
    data curation conf scripts src reports reviews
  snapshot_sha256: 0ddb1e1c4005691595186e8f80b8c6c15cef3a3b6086b7acb0d8ebe880b600d6
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/134705/
  locator: Current CHEBI134705 identity, structure, names, CAS and parent relations
  accessed_at: '2026-10-21T15:37:07.154851Z'
  support: supports
  summary: Current ChEBI agrees with the native neutral formula, key and all twelve
    specified stereocentres, identifies the 1-N-ethylgentamicin C1a relationship and
    supports aminoglycoside/amino-cyclitol-glycoside classification. CAS59711-96-5
    is attached to this exact entity.
  snapshot_sha256: 721c54732324181ac3ab6119d336104882ad82f98f5e62408188626300293512
- evidence_id: drugcentral
  kind: authority
  reference: https://drugcentral.org/drugcard/5171
  locator: Current DrugCentral 5171 named drug card and linked structure export
  accessed_at: '2026-10-21T15:37:07.846962Z'
  support: supports
  summary: The card names etimicin and supports the native drug-level association.
    Its linked molfile leaves one tetrahedral centre unspecified, but drug_xrefs explicitly
    does not assert exact stereochemical equivalence.
  snapshot_sha256: 65ba514791f165ac6dcec849aceb3777ac99f540a1a4f41af281ceb884854012
- evidence_id: drugcentral-structure
  kind: authority
  reference: https://drugcentral.org/drug/5171/molfile
  locator: Official linked /drug/5171/molfile structure
  accessed_at: '2026-10-21T15:38:22.864294Z'
  support: context_only
  summary: Independent parsing gives NZGMVSJQULXLHF-NORJTPJDSA-N with /t19?; native/current
    ChEBI give NZGMVSJQULXLHF-RAKCNUBFSA-N with /t19+. Formula and connectivity match,
    and all other eleven tetrahedral assignments agree. This is under-specification,
    not a demonstrated opposite epimer. This representational difference does not
    invalidate the schema-permitted drug-level association.
  snapshot_sha256: 9268424b26c3541907840f78d30d59b0b9d2aa313f661730b768871950195d46
- evidence_id: chemistry
  kind: record_content
  reference: 419-chemistry.json; 412413419-xref-chemistry.json
  locator: RDKit 2026.03.5 independent native and authority parsing; batch019 interpreter
    against batch042 cwd
  accessed_at: '2026-10-21T15:44:01Z'
  support: supports
  summary: Native SMILES and InChI agree in formula C21H43N5O7, neutral charge, masses,
    all twelve stereocentres and source mint. DrugCentral differs only at its unassigned
    glycosidic centre.
  snapshot_sha256: 244f6d89d046a96750ccb2205d82fd09368a63d477dad250e5681c2d6cddbfc5
- evidence_id: atom-map
  kind: record_content
  reference: 419-anomeric-map.json
  locator: InChI atom 19 and original patent numbered sugar
  accessed_at: '2026-10-21T15:44:01Z'
  support: supports
  summary: 'InChI atom 19 is the right-hand purpurosamine anomeric carbon C1-prime:
    it connects to sugar carbon 11, ring oxygen 31 and glycosidic oxygen 32, which
    connects to deoxystreptamine carbon 16. Native assignment is R; DrugCentral marks
    the centre unknown. Original patent general formula 1 depicts the defined glycosidic
    geometry.'
  snapshot_sha256: 80ab52c29664b2e5fca42771c20bb4d94212e433e0feebc6e04b7be04eae9324
- evidence_id: patent
  kind: primary_source
  reference: https://patents.google.com/patent/US5814488/en
  locator: US5814488, disclosure, general formula 1 compound (3), Example 4 and separate
    formulation examples
  accessed_at: '2026-10-21T15:37:08.871816Z'
  support: supports
  summary: The original patent explicitly names 1-N-ethylgentamicin C1a as etimicin.
    Example 4(3) isolates the free base, followed separately by sulfate formation
    in 4(4). The reported protonated mass signal 478 is not the molecular weight of
    a sodium adduct or a new salt. Gentamicin C1a is the fermentation precursor; the
    ethyl derivative is semisynthetic. Other gentamicin congeners and formulations
    remain distinct.
  snapshot_sha256: 6edf4ad7619ea0e5d659f53365634232c13f271adedce42f89c7f7071ae4bae0
- evidence_id: patent-pdf
  kind: primary_source
  reference: https://patentimages.storage.googleapis.com/7d/7b/68/ad430bb4ef8f20/US5814488.pdf
  locator: Actual PDF page 11, printed column 2, general formula [1] and compound
    (3)
  accessed_at: '2026-10-21T15:40:13.379048Z'
  support: supports
  summary: The actual structure drawing was viewed. It numbers the right-hand sugar
    anomeric position 1-prime and specifies its glycosidic geometry. Compound (3)
    selects hydrogen at R1–R4 and ethyl at R5, consistent with the native 1-N-ethylgentamicin
    C1a constitution. This is not evidence that every patent formulation is neutral
    free base.
  snapshot_sha256: c0043dd1cccf3d5f20eee69ad0e53a93ef58e501046c04a5b3535020aeb69b04
- evidence_id: patent-figure
  kind: record_content
  reference: 419-patent-page11.png
  locator: Rasterized original PDF page 11 viewed directly
  accessed_at: '2026-10-21T15:44:01Z'
  support: supports
  summary: Preserved visual locator for the numbered glycoside and exact compound-variable
    assignment; structural interpretation is retained separately from the source image.
  snapshot_sha256: de7ee3e911cfb6f802a59178db89ca5c7c7c89ff86a46846d52eeb140440db6d
- evidence_id: adopted-abstracts
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%28EXT_ID%3A11776118%20OR%20EXT_ID%3A11931698%20OR%20EXT_ID%3A22918626%20OR%20EXT_ID%3A22983905%20OR%20EXT_ID%3A25233899%20OR%20EXT_ID%3A25464101%20OR%20EXT_ID%3A26924270%20OR%20EXT_ID%3A28881316%20OR%20EXT_ID%3A30814950%20OR%20EXT_ID%3A31847403%29%20AND%20SRC%3AMED&format=json&resultType=core&pageSize=100
  locator: All ten adopted PMID records and complete original abstracts
  accessed_at: '2026-10-21T15:37:08.035624Z'
  support: context_only
  summary: Every frozen adopted PMID lead was resolved and its original abstract read.
    Clinical studies, analytical detection, rat toxicity, precursor production and
    antibacterial sulfate experiments are distinguished in the explicit disposition
    ledger.
  snapshot_sha256: 3b76078264b2afcd91b75db0c4d780e2246fe7cc4434b9837b19423e01a3f613
- evidence_id: adopted-dispositions
  kind: record_content
  reference: 419-adopted-dispositions.json
  locator: Per-PMID reading depth and exact endpoint/material disposition
  accessed_at: '2026-10-21T15:44:01Z'
  support: context_only
  summary: All ten adopted bibliography leads have explicit source-specific dispositions,
    including full-text access limits and salt/combination boundaries.
  snapshot_sha256: 68d96fb5ab6dd2e5ed7b34adc97649382322f7ad677c99a76e0e2c250627f9b1
- evidence_id: precursor-study
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6963548/?pdf=1
  locator: PMID31847403, DOI10.3390/antibiotics8040267; Introduction, gentamicin analysis
    methods and conclusions
  accessed_at: '2026-10-21T15:38:23.123845Z'
  support: supports
  summary: The original study engineers genK/genL-related gentamicin precursor production
    in M. purpurea. Its product is gentamicin C1a used for later chemical synthesis
    of etimicin. It cannot establish a natural etimicin producer or transfer precursor
    activity to etimicin.
  snapshot_sha256: afbe09309401db9692941ee3fbcd9455e84e333997ca15e584fdf1f43ea27898
- evidence_id: combination-study
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6381041/?pdf=1
  locator: PMID30814950, DOI10.3389/fphar.2019.00092; Methods and relevant combination
    results
  accessed_at: '2026-10-21T15:38:23.368932Z'
  support: partial
  summary: The original study reports etilmicin with sulbactam or meropenem in retrospective
    VAP treatment and broth/checkerboard tests on 36 MDR A. baumannii strains. It
    uses MH broth, serial dilution, 37 °C overnight and historical CLSI M100-S23.
    Salt/purity is not established in the inspected method; combination outcomes do
    not prove monotherapy response or direct ribosomal binding.
  snapshot_sha256: ce42406333ce4657ac66dec30f73e7573b7bf4b22d89197617057858ebe00724
- evidence_id: primary2020
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC7468263/?pdf=1
  locator: PMID31937930, DOI10.1038/s41401-019-0342-5; Chemicals, antibacterial Methods
    and Table 1
  accessed_at: '2026-10-21T15:38:23.371086Z'
  support: partial
  summary: The original later study explicitly uses etimicin sulfate from Changzhou
    Fangyuan. It tests 36 clinical isolates, six each of E. coli, K. pneumoniae, E.
    cloacae, P. mirabilis, P. aeruginosa and S. aureus, by broth microdilution at
    37 °C for 18–24 h with a visible-growth endpoint. Table 1 supports broad tested
    activity but contains unusual interpolated MIC50/MIC90 values; no quantitative
    observation is imported. Rat mitochondrial/toxicity findings are not a bacterial
    target mechanism.
  snapshot_sha256: 04106672151d0a2c0f2162b44d6ba41b903681f1030861425604e32276d94d59
- evidence_id: adapter
  kind: database
  reference: iModulonDB dataset catalog
  locator: 412413419-adapter-catalog.txt; actual pre-research runner
  accessed_at: '2026-10-21T15:44:01Z'
  support: context_only
  summary: The catalog was checked before protein follow-up. No exact protein, taxon-specific
    locus or dataset is asserted in the native etimicin record. Later precursor biosynthesis
    and host-toxicity proteins are not silently adopted as native antibacterial targets.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: gates
  kind: record_content
  reference: 419-focused-results.json
  locator: Actual native schema/strict and independent chemistry commands
  accessed_at: '2026-10-21T15:44:01Z'
  support: supports
  summary: All focused native checks pass. The external DrugCentral structure comparison
    is contextual; its less specified stereochemistry does not violate drug_xrefs
    semantics.
  snapshot_sha256: ffdbdefa5a4f588da8f22c61a1f548f960db5ed7787541c568722445c10a9062
- evidence_id: access-boundaries
  kind: search
  reference: 412413419-fetch1.json through 412413419-fetch4.json
  locator: Exact request URLs, timestamps, HTTP responses and hashes
  accessed_at: '2026-10-21T15:44:01Z'
  support: context_only
  summary: DrugCentral initially requested a nonexistent structure route; the actual
    card-linked molfile was then retrieved and parsed. The 2012 antibacterial publisher
    response was client-challenge HTML, not a full paper. The 2020 DOC supplement
    was downloaded, but text conversion did not preserve its embedded structure image;
    that unviewed image is not used as structural evidence.
  search_scope: All ten adopted PMID leads, exact current chemical identifiers, the
    full native patent and directly relevant free original activity/precursor papers
    and supplements; no paid research.
  snapshot_sha256: 2b3b500d8e5afb7715a033094296511afda9d8169005264c9e6b84beb4b6509a
- evidence_id: drug-xref-semantics
  kind: record_content
  reference: src/antibioticmech/schema/antibioticmech.yaml
  locator: AntibioticRecord.drug_xrefs, lines200–206
  accessed_at: '2026-10-21T15:47:02Z'
  support: supports
  summary: The schema explicitly defines DrugBank, DrugCentral and KEGG DRUG identifiers
    as drug-level associations covering parents, salts and stereoisomers. These identifiers
    are not same-structure equivalences; exact-equivalence rules apply to xrefs instead.
  snapshot_sha256: de62be2dd2dd55f141a0c14ff666eaa00efc6f3b431d651d0196ebcfddfbb301
assessments:
- assessment_id: identity
  area: identity
  topic: Neutral semisynthetic structure and synonym scope
  outcome: supported
  summary: Native SMILES, InChI, formula, mass and twelve stereocentres are coherent.
    Current ChEBI and the original patent constitution/numbered glycoside support
    the specified 1-N-ethylgentamicin C1a entity. Etilmicin is used as an alternate
    spelling in the original adopted clinical source; no product-brand claim is inferred.
  target_ids:
  - CHEBI:134705
  evidence_ids:
  - native
  - chemistry
  - chebi
  - patent
  - patent-pdf
  - atom-map
  - combination-study
- assessment_id: grounding
  area: grounding
  topic: Drug-level DrugCentral association
  outcome: supported
  summary: DrugCentral 5171 names etimicin. Its export has the same constitution and
    eleven matching centres while leaving the purpurosamine anomeric centre unspecified.
    The schema explicitly permits drug-level identifiers to cover stereoisomers, so
    this difference establishes no native grounding defect and does not require removing
    the link. No opposite epimer or racemate is inferred.
  target_ids:
  - CHEBI:134705
  evidence_ids:
  - native
  - drugcentral
  - drugcentral-structure
  - chemistry
  - atom-map
  - drug-xref-semantics
- assessment_id: classification
  area: scope
  topic: Antibacterial and aminoglycoside roles
  outcome: supported
  summary: The original sulfate antibacterial study and later exact etimicin-sulfate
    tests support antibacterial activity at the active-moiety level. The definition
    does not establish effectiveness against every aminoglycoside-resistant isolate;
    quantitative or clinical extrapolation beyond the tested studies is not adopted.
  target_ids:
  - CHEBI:134705
  evidence_ids:
  - native
  - chebi
  - adopted-abstracts
  - adopted-dispositions
  - primary2020
- assessment_id: evidence
  area: evidence
  topic: Analytical, clinical and precursor evidence placement
  outcome: supported
  summary: The frozen bibliography contains several analytical/host-exposure papers
    rather than target experiments. Their presence is not treated as proof of every
    definition claim. Clinical combinations remain combinations, and precursor biosynthesis
    remains gentamicin C1a production.
  target_ids:
  - CHEBI:134705
  evidence_ids:
  - adopted-dispositions
  - precursor-study
  - combination-study
  - primary2020
  - patent
- assessment_id: completeness
  area: completeness
  topic: Optional target, resistance and activity enrichment
  outcome: unknown
  summary: The record has no molecular-target, mode, resistance, activity_spectrum
    or causal-graph entries. Their absence is not a required-schema defect. Primary
    quantitative enrichment would need exact salt/potency basis, strain panel and
    assay metadata; host mitochondrial toxicity cannot fill a bacterial-target field.
  target_ids:
  - CHEBI:134705
  evidence_ids:
  - native
  - search
  - adopted-dispositions
  - primary2020
- assessment_id: other-domains
  area: scope
  topic: Producer, FDA and collection assertions
  outcome: not_applicable
  summary: No FDA product, producer or activity-collection assertion is present. The
    inspected Micromonospora studies do not justify inventing a natural etimicin producer.
  target_ids:
  - CHEBI:134705
  evidence_ids:
  - native
  - search
  - precursor-study
  - patent
- assessment_id: provenance
  area: provenance
  topic: Actual source and generated history
  outcome: supported
  summary: All four seeded/reseeded events and exact adopted ChEBI fields are coherent.
    Original thirteen hashes are preserved within 20 expanded inputs. The DrugCentral
    association is interpreted according to its drug-level field semantics.
  target_ids:
  - CHEBI:134705
  evidence_ids:
  - native
  - owners
  - gates
- assessment_id: validation
  area: schema
  topic: Focused native validation
  outcome: supported
  summary: Schema, strict validation, chemistry and source-mint checks pass. Exact
    structural identifiers are distinguished from the broader drug-level associations
    explicitly permitted by the schema.
  target_ids:
  - CHEBI:134705
  evidence_ids:
  - gates
  - chemistry
  - drugcentral-structure
findings: []
actions: []
limitations:
- All ten adopted PMID abstracts were inspected. Full methods were not obtained for
  the older clinical and analytical sources; the 2012 antibacterial publisher page
  returned a JavaScript challenge. No uninspected numeric or isolated-material detail
  is inferred.
- The original patent disclosure, exact free-base/sulfate Example 4, general formula
  and actual numbered structure page were inspected. All 22 patent pages and every
  NMR/MS trace were not independently reanalyzed.
- The 2020 study was inspected for exact sulfate material, antibacterial Methods and
  Table 1. Host toxicology figures and the embedded structure image in its legacy
  DOC supplement were not independently viewed; the original patent drawing provides
  the retained structural evidence.
- Etimicin-sulfate and combination-therapy results support bounded active-moiety context
  but are not numerically transferred into neutral free-base MIC observations. Modern
  resistance surveillance and clinical efficacy are not exhaustively reviewed.
- The CAS assignment was checked in the current ChEBI record. A separate Common Chemistry
  page could not be retrieved through the attempted web route, so independent CAS-registry
  verification is not claimed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native or maintained source was edited. Original captures and hashes were preserved;
  all expanded inputs were checked unchanged. Optional links, tags and notes are specific
  to etimicin.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:134705
- https://patents.google.com/patent/US5814488A/en
- https://doi.org/10.1038/s41401-019-0342-5
tags:
- etimicin
- semisynthetic-aminoglycoside
- drug-level-association
```
