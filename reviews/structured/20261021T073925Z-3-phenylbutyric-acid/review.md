# 3-Phenylbutyric acid: supported identity and antibacterial activity with bounded response evidence

- Review: 20261021T073925Z-3-phenylbutyric-acid
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T07:29:26Z
- Finished UTC: 2026-10-21T07:39:25Z
- Reviewer: Codex review002 subagent with root source cross-check (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The exact constitutional identity with unspecified stereochemistry and its antibacterial role are supported. Focused schema, strict and chemistry checks pass. One informational follow-up concerns optional qualified activity and response-evidence enrichment; MBC is not MIC, response proteins are not demonstrated targets, and activity cannot transfer from the 4-isomer or its sodium salt. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole native record, maintained provenance, authority identity and all seven adopted literature abstracts, with full 2013 antibacterial primary paper.

Selection: Queue index039, CHEBI:166657 at its locked native path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:166657 | data/antibiotics/antibacterial/3-phenylbutyric-acid.yaml | generated | 3-phenylbutyric acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused LinkML validation | passed | True | CHEBI:166657 | No issues found. |
| Focused strict validation | passed | True | CHEBI:166657 | Scanned one file; zero ERROR rows. |
| Independent native chemistry and mint | passed | False | CHEBI:166657 | Both representations reproduce the same full key, formula, charge and rounded masses; one unspecified stereocentre. |
| Structured expression-dataset coverage | passed | False | CHEBI:166657 | Actual inventory request succeeded. No Helicobacter pylori dataset is present for the paper’s DHQase/Pfr/Ppa response context. |
| iModulon search applicability | not_applicable | False | CHEBI:166657 | The exact response organism is not covered. E. coli growth inhibition alone does not justify transferring H. pylori protein responses into an E. coli module search. |
| Independent external registry access | unavailable | False | CHEBI:166657 | ChemSpider direct access returned403 in root research; Reaxys was not independently inspected. HMDB/FooDB were inspected by root, but review002 requests returned403; HMDB full key remains independently unconfirmed. These are bounded access limits, not established wrong xrefs. |
| Authoritative full QC | failed | True | CHEBI:166657 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:166657 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:166657 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:166657 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:166657 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:166657 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:166657 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:166657 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:166657 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact constitutional and stereochemical scope

identity: supported. Targets: CHEBI:166657.

Definition, four synonyms and chemical strings describe the3-isomer with unspecified stereochemistry. Neither the native string nor the2013 test-material description justifies racemate or single-enantiomer claims.

### Parents, role and xrefs

grounding: supported. Targets: CHEBI:166657.

Broader classes and antibacterial role are coherent. CAS and FooDB identity are supported; HMDB MOL agrees in root inspection, with its descriptive confounding and unconfirmed full key retained. ChemSpider/Reaxys access limits remain explicit.

### Direct exact-compound activity

evidence: supported. Targets: CHEBI:166657.

The complete primary paper supports antibacterial activity with strain-specific disc and bactericidal endpoints. These support the role without claiming broad potency or clinical use.

### Response versus direct mechanism

evidence: unknown. Targets: CHEBI:166657.

Native record asserts no target or mode of action. Protein and targeted-transcript changes allow qualified response notes, while direct targets and ROS causality remain unresolved.

### Producers, resistance and clinical context

representation: not_applicable. Targets: CHEBI:166657.

No native fields require correction. Degradation or growth on the compound is not biosynthetic production; organism resistance to metronidazole is not resistance to3-PB; host-cell effects and proposed clinical utility are not established antibiotic use.

### Optional evidence enrichment

completeness: supported. Targets: CHEBI:166657.

Exact-compound measurements and qualified response evidence offer a bounded curation path, with method/caption conflicts retained rather than silently normalized.

### Source, namespace normalization and status

ownership: supported. Targets: CHEBI:166657.

Source row, normalizer, minted identifier and four history events agree. Imported identity fixes belong to source/transform owners; scientific additions belong to the actual native record. All13 captured hashes are unchanged.

### Focused native gates

schema: supported. Targets: CHEBI:166657.

Schema, strict and chemistry pass; these deterministic checks are separate from primary scientific assessment.

## Findings

### F1: Optional primary activity and response evidence can be curated with endpoint and assay qualifications

informational / open / confirmed; issue key: chebi-166657-qualified-primary-activity-enrichment.

The seed’s antibacterial role is supported, but direct disc/MBC observations and bounded protein-response notes remain unrepresented. This is an enrichment opportunity, not a current false measurement or required-field omission. Preserve isomer/stereochemical scope, distinguish MBC from MIC, and retain method/caption conflicts.

## Recommended Actions And Acceptance Checks

### A1

If selected for curation, add exact3-phenylbutyric-acid activity with strain, endpoint, dose, incubation and method qualifiers, and optionally a clearly bounded response note.

- Represent the1 and0.25mg/mL values as MBCs, with99.9% killing and24h exposure/48h recovery; do not convert to MIC.
- Keep disc zone diameter,4mg/disc dose and exact tested organism/strain together; no assay-wide or clinically interpreted resistance extrapolation.
- Retain the inoculum, metronidazole-disc-dose and proteomics-concentration inconsistencies; resolve them before claiming unambiguous normalized conditions.
- Do not add DHQase/Pfr/Ppa as direct molecular targets or ROS as a measured causal event from expression data alone; no clinical use or4-isomer/salt activity transfer.
- Do not infer a racemate or individual enantiomer from unspecified stereochemistry, or biosynthetic production from substrate degradation.
- Use write_validated_antibiotic and native curation history for separately authorized additions; rerun focused schema/strict and required corpus checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/3-phenylbutyric-acid.yaml; Entire native YAML. | supports | CHEBI:166657 is SEEDED and EXACT; definition describes a 3-phenyl-substituted butanoic acid. Four synonyms, two broader parents, one antibacterial role, five xrefs, full chemistry, one ChEBI source concept and four seeder history events are coherent. There are no native activity_spectrum, target, mechanism, producer, resistance, clinical or causal-graph assertions. Optional omissions are not required-field defects. |
| owner | data/raw/chebi_antimicrobials.tsv; Exact CHEBI:166657 row; raw MANIFEST; PATHS; conf/sources.yaml; extract_source_inventory.py ChEBI extraction; seed_from_sources.py normalization, mint, build_concepts and build_record. | supports | The adopted row matches identity, structures, synonyms, parents, role and registry assertions; seven PMIDs are citation leads and mechanism_role_ids is empty. Seeder line232 intentionally normalizes foodb.food:FDB022762 to foodb.compound:FDB022762. The minted identifier antibioticmech:chebi-951971716d is reproduced. All13 initial input hashes remain unchanged; source version2026-08-30 and four history events are coherent. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:166657; Official complete compound page;039-chebi.html. | supports | ChEBI matches the exact name, definition, four synonyms, neutral C10H12O2, mass164.204, monoisotopic mass164.08373, full SMILES/InChI/key and retained xrefs. CHEBI:22712 benzenes and25384 monocarboxylic acid are broader parents;33282 is the antibacterial role. Additional non-antimicrobial roles in the authority need not be imported as required omissions. |
| nist | https://webbook.nist.gov/cgi/cbook.cgi?ID=C4593902; NIST identity header and identifiers. | supports | NIST explicitly matches CAS4593-90-2, the native full InChI and key ZZEWMYILWXCRHZ-UHFFFAOYSA-N, formula and constitutional synonyms. Its historical molecular weight164.2011 does not alter identity or invalidate the current elemental-weight calculation164.204. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/20724; Official PUG response039-pubchem.json. | supports | Current PubChem CID20724 matches the full native InChI/key, formula and IUPAC name. This is independent corroboration, not an additional native xref. |
| xref | https://foodb.ca/compounds/FDB022762; Root inspected FooDB full page and HMDB https://www.hmdb.ca/metabolites/HMDB01955; ChEBI retained xrefs; subsequent review002 requests. | context_only | Root inspected matching FooDB SMILES/InChI/key and matching HMDB MOL; HMDB identifies secondary accession HMDB01955 with primary HMDB0001955. Review002 direct requests returned403, so no independent HMDB InChI/key verification is claimed. HMDB descriptive claims about sodium phenylbutyrate and its therapeutic use cannot be transferred to the exact 3-isomer. ChemSpider19513 and Reaxys2044322 are verified source assertions only, with no independently inspected target record. |
| chemistry | RDKit native structure calculation; 039-chemistry.py and039-chemistry.json. | supports | Both native SMILES and InChI parse independently into one neutral connected C10H12O2 molecule, key ZZEWMYILWXCRHZ-UHFFFAOYSA-N, average mass164.204 and exact mass164.083729624. One stereocentre is unspecified. This does not establish that the material is a racemate. |
| primary-activity | PMID:23727774; DOI:10.1248/cpb.c12-00857; https://www.jstage.jst.go.jp/article/cpb/61/6/61_c12-00857/_pdf; complete039-primary2013.txt/PDF, Table1 and Figure1C visually inspected. | supports | Wako3-phenylbutyric acid, without specified stereochemistry, was tested separately from2-PB/4-PB. At4mg/disc, Table1 reports zones33.5±2.5mm for H.pylori ATCC43504,43.0±1.0mm for clinical No.238 and22.5±1.5mm for E.coli ATCC25922. Reported3-PB MBCs are1mg/mL and0.25mg/mL for the two H.pylori strains: at least99.9% killing after24h exposure, with48h colony recovery. They are not MICs. |
| primary-response | DOI:10.1248/cpb.c12-00857; Methods pp605–606, Tables3–4, Figures2–4 and discussion pp608–610. | context_only | The H.pylori response experiment uses2D protein profiling and targeted RT-PCR. DHQase, Pfr and Ppa increases support a bounded treatment-response observation; there is no direct target inhibition/binding or measured ROS assay. Oxidative stress, membrane entry and electron-transfer explanations are interpretations. Metronidazole-combination effects are pH-conditioned, not evidence of clinical efficacy. Preserve source discrepancies: inoculum10^7 in Methods versus10^8 in Figure1; metronidazole200µg in combination Methods versus100µg in Table3; proteomic concentration0.1mg/mL in Methods versus0.1g/mL in Figure2. |
| adopted-literature | Europe PMC official article metadata and abstracts; 039-epmc.json; all seven adopted PMIDs10470142,16535265,20143352,22925447,23727774,26654204,7118830. | context_only | All identifiers resolve and all abstracts were read. PMID10470142 concerns host-cell growth/histone effects;22925447 concerns leukemic coumarin analogues. PMID16535265 addresses enantioselective degradation,7118830 substrate catabolism, and20143352/26654204 identify the acid as a hydrocarbon degradation intermediate. These do not directly establish antibacterial targets, clinical efficacy, resistance determinants or natural-product biosynthesis. The full2013 study provides the direct activity support. |
| adapter | https://imodulondb.org/api/datasets; Actual source runner output039-imodulondb-datasets.txt. | context_only | The returned28 dataset keys contain no H.pylori dataset for the exact response experiment. No matching-organism search or component summary is applicable. Other assayed bacterial taxa being covered does not permit protein-response transfer. This coverage result is not negative biological evidence. |
| search | CultureBotAI/AntibioticMech; 039-local-hits.txt and039-focused-local-hits.txt. | context_only | The inclusive worktree search located source, generated, index and historical research references. Focused curation/reviews/historical-review/conf search returned no exact-identifier/name matches outside the queue. Historical artifacts were treated as leads, not primary support; no global absence conclusion is drawn. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Native identity, activity, evidence, mechanism, producer and status rules; CURATION/HARMONIZATION. | supports | Optional evidence enrichment is not a required-field defect. Keep salts/isomers and stereochemical scope distinct, assay evidence at claim level, production separate from xenobiotic degradation, and response proteins separate from directly demonstrated targets. |
| validation | Documented per-record validators; Actual worktree004 focused commands and039-strict.tsv. | supports | Both focused validators and independent chemistry passed; shared repository checks are recorded separately with actual outcomes. |

## Limits And Additional Notes

- Root inspected FooDB full structure and HMDB MOL. Subsequent review002 direct requests were forbidden; independent HMDB full InChI/key remains unconfirmed. ChemSpider direct access was403 and Reaxys was not independently inspected; their ChEBI assertions are retained without claiming independent identity verification.
- All seven adopted abstracts and complete2013 antibacterial text were inspected; the other six full texts were not comprehensively reviewed.
- The2013 paper contains method/caption inconsistencies in inoculum, metronidazole combination-disc dose and proteomics concentration. These limit quantitative normalization and do not erase its direct activity evidence.
- Protein and targeted RT-PCR results are response evidence; direct binding/inhibition, ROS measurement, clinical efficacy and biosynthetic production were not established by the inspected experiments.
- iModulonDB has no matching H.pylori dataset. The review and literature search are bounded, not a claim that no further mechanism or activity evidence exists.
- No native record edits or paid research occurred. This review does not promote native scientific status.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T073925Z-3-phenylbutyric-acid
kind: record
repository: CultureBotAI/AntibioticMech
title: '3-Phenylbutyric acid: supported identity and antibacterial activity with bounded
  response evidence'
started_at: '2026-10-21T07:29:26Z'
finished_at: '2026-10-21T07:39:25Z'
reviewer:
  identity: Codex review002 subagent with root source cross-check
  kind: agent
  independence: independent
  independence_basis: Neither reviewer authored the target. Root captured provenance
    before assessment and inspected authority pages and primary sources; review002
    independently read the entire native record, source row and transforms, all adopted
    abstracts, complete 2013 primary text and Figure 1, and reran focused validation
    and chemistry.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: The exact constitutional identity with unspecified stereochemistry and its
  antibacterial role are supported. Focused schema, strict and chemistry checks pass.
  One informational follow-up concerns optional qualified activity and response-evidence
  enrichment; MBC is not MIC, response proteins are not demonstrated targets, and
  activity cannot transfer from the 4-isomer or its sodium salt. Scientific assessment
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
  - path: data/antibiotics/antibacterial/3-phenylbutyric-acid.yaml
    sha256: 24af49fac57fc03316f7342073306cafa04b6279634ffeb5b53e6dc0550b3ada
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
- target_id: CHEBI:166657
  path: data/antibiotics/antibacterial/3-phenylbutyric-acid.yaml
  label: 3-phenylbutyric acid
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
  description: Whole native record, maintained provenance, authority identity and
    all seven adopted literature abstracts, with full 2013 antibacterial primary paper.
  selection: Queue index039, CHEBI:166657 at its locked native path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:166657
  exclusions:
  - target: 2-Phenylbutyric acid, 4-phenylbutyric acid, sodium phenylbutyrate and
      individually configured R/S enantiomers
    reason: Distinct constitutional forms, salt or more specific stereochemical entities;
      their activity, clinical use and molecular mechanisms cannot be substituted
      for this record.
checks:
- check_id: schema
  name: Focused LinkML validation
  status: passed
  required: true
  summary: No issues found.
  target_ids:
  - CHEBI:166657
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/3-phenylbutyric-acid.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict validation
  status: passed
  required: true
  summary: Scanned one file; zero ERROR rows.
  target_ids:
  - CHEBI:166657
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/3-phenylbutyric-acid.yaml --out /private/tmp/am-review-session/039-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: Independent native chemistry and mint
  status: passed
  required: false
  summary: Both representations reproduce the same full key, formula, charge and rounded
    masses; one unspecified stereocentre.
  target_ids:
  - CHEBI:166657
  evidence_ids:
  - chemistry
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/039-chemistry.py
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter
  name: Structured expression-dataset coverage
  status: passed
  required: false
  summary: Actual inventory request succeeded. No Helicobacter pylori dataset is present
    for the paper’s DHQase/Pfr/Ppa response context.
  target_ids:
  - CHEBI:166657
  evidence_ids:
  - adapter
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 datasets
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-scope
  name: iModulon search applicability
  status: not_applicable
  required: false
  summary: The exact response organism is not covered. E. coli growth inhibition alone
    does not justify transferring H. pylori protein responses into an E. coli module
    search.
  target_ids:
  - CHEBI:166657
  evidence_ids:
  - adapter
  - primary-response
- check_id: limited-xrefs
  name: Independent external registry access
  status: unavailable
  required: false
  summary: ChemSpider direct access returned403 in root research; Reaxys was not independently
    inspected. HMDB/FooDB were inspected by root, but review002 requests returned403;
    HMDB full key remains independently unconfirmed. These are bounded access limits,
    not established wrong xrefs.
  target_ids:
  - CHEBI:166657
  evidence_ids:
  - xref
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:166657
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
  - CHEBI:166657
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
  - CHEBI:166657
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
  - CHEBI:166657
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
  - CHEBI:166657
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
  - CHEBI:166657
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
  - CHEBI:166657
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
  - CHEBI:166657
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
  - CHEBI:166657
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/3-phenylbutyric-acid.yaml
  locator: Entire native YAML.
  accessed_at: '2026-10-21T07:37:22Z'
  support: supports
  summary: CHEBI:166657 is SEEDED and EXACT; definition describes a 3-phenyl-substituted
    butanoic acid. Four synonyms, two broader parents, one antibacterial role, five
    xrefs, full chemistry, one ChEBI source concept and four seeder history events
    are coherent. There are no native activity_spectrum, target, mechanism, producer,
    resistance, clinical or causal-graph assertions. Optional omissions are not required-field
    defects.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Exact CHEBI:166657 row; raw MANIFEST; PATHS; conf/sources.yaml; extract_source_inventory.py
    ChEBI extraction; seed_from_sources.py normalization, mint, build_concepts and
    build_record.
  accessed_at: '2026-10-21T07:37:22Z'
  support: supports
  summary: The adopted row matches identity, structures, synonyms, parents, role and
    registry assertions; seven PMIDs are citation leads and mechanism_role_ids is
    empty. Seeder line232 intentionally normalizes foodb.food:FDB022762 to foodb.compound:FDB022762.
    The minted identifier antibioticmech:chebi-951971716d is reproduced. All13 initial
    input hashes remain unchanged; source version2026-08-30 and four history events
    are coherent.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:166657
  locator: Official complete compound page;039-chebi.html.
  accessed_at: '2026-10-21T07:37:22Z'
  support: supports
  summary: ChEBI matches the exact name, definition, four synonyms, neutral C10H12O2,
    mass164.204, monoisotopic mass164.08373, full SMILES/InChI/key and retained xrefs.
    CHEBI:22712 benzenes and25384 monocarboxylic acid are broader parents;33282 is
    the antibacterial role. Additional non-antimicrobial roles in the authority need
    not be imported as required omissions.
- evidence_id: nist
  kind: database
  reference: https://webbook.nist.gov/cgi/cbook.cgi?ID=C4593902
  locator: NIST identity header and identifiers.
  accessed_at: '2026-10-21T07:37:22Z'
  support: supports
  summary: NIST explicitly matches CAS4593-90-2, the native full InChI and key ZZEWMYILWXCRHZ-UHFFFAOYSA-N,
    formula and constitutional synonyms. Its historical molecular weight164.2011 does
    not alter identity or invalidate the current elemental-weight calculation164.204.
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/20724
  locator: Official PUG response039-pubchem.json.
  accessed_at: '2026-10-21T07:37:22Z'
  support: supports
  summary: Current PubChem CID20724 matches the full native InChI/key, formula and
    IUPAC name. This is independent corroboration, not an additional native xref.
  snapshot_sha256: 5e9a3d4c742fdad2906a5b9b2d743c0f1f49dfe29d99cde76bf76861bdcd79c4
- evidence_id: xref
  kind: database
  reference: https://foodb.ca/compounds/FDB022762
  locator: Root inspected FooDB full page and HMDB https://www.hmdb.ca/metabolites/HMDB01955;
    ChEBI retained xrefs; subsequent review002 requests.
  accessed_at: '2026-10-21T07:37:22Z'
  support: context_only
  summary: Root inspected matching FooDB SMILES/InChI/key and matching HMDB MOL; HMDB
    identifies secondary accession HMDB01955 with primary HMDB0001955. Review002 direct
    requests returned403, so no independent HMDB InChI/key verification is claimed.
    HMDB descriptive claims about sodium phenylbutyrate and its therapeutic use cannot
    be transferred to the exact 3-isomer. ChemSpider19513 and Reaxys2044322 are verified
    source assertions only, with no independently inspected target record.
- evidence_id: chemistry
  kind: validation
  reference: RDKit native structure calculation
  locator: 039-chemistry.py and039-chemistry.json.
  accessed_at: '2026-10-21T07:37:22Z'
  support: supports
  summary: Both native SMILES and InChI parse independently into one neutral connected
    C10H12O2 molecule, key ZZEWMYILWXCRHZ-UHFFFAOYSA-N, average mass164.204 and exact
    mass164.083729624. One stereocentre is unspecified. This does not establish that
    the material is a racemate.
  snapshot_sha256: 891019d327f2409bf1a4e38895491bb4beeff48f43e69408f2ad00be1da882ff
- evidence_id: primary-activity
  kind: primary_source
  reference: PMID:23727774
  locator: DOI:10.1248/cpb.c12-00857; https://www.jstage.jst.go.jp/article/cpb/61/6/61_c12-00857/_pdf;
    complete039-primary2013.txt/PDF, Table1 and Figure1C visually inspected.
  accessed_at: '2026-10-21T07:37:22Z'
  support: supports
  summary: 'Wako3-phenylbutyric acid, without specified stereochemistry, was tested
    separately from2-PB/4-PB. At4mg/disc, Table1 reports zones33.5±2.5mm for H.pylori
    ATCC43504,43.0±1.0mm for clinical No.238 and22.5±1.5mm for E.coli ATCC25922. Reported3-PB
    MBCs are1mg/mL and0.25mg/mL for the two H.pylori strains: at least99.9% killing
    after24h exposure, with48h colony recovery. They are not MICs.'
  snapshot_sha256: 461807f70a2b95ba07f255188215c0c6db41ee1eab2fa947b68e30c5cbf73235
- evidence_id: primary-response
  kind: primary_source
  reference: DOI:10.1248/cpb.c12-00857
  locator: Methods pp605–606, Tables3–4, Figures2–4 and discussion pp608–610.
  accessed_at: '2026-10-21T07:37:22Z'
  support: context_only
  summary: 'The H.pylori response experiment uses2D protein profiling and targeted
    RT-PCR. DHQase, Pfr and Ppa increases support a bounded treatment-response observation;
    there is no direct target inhibition/binding or measured ROS assay. Oxidative
    stress, membrane entry and electron-transfer explanations are interpretations.
    Metronidazole-combination effects are pH-conditioned, not evidence of clinical
    efficacy. Preserve source discrepancies: inoculum10^7 in Methods versus10^8 in
    Figure1; metronidazole200µg in combination Methods versus100µg in Table3; proteomic
    concentration0.1mg/mL in Methods versus0.1g/mL in Figure2.'
- evidence_id: adopted-literature
  kind: primary_source
  reference: Europe PMC official article metadata and abstracts
  locator: 039-epmc.json; all seven adopted PMIDs10470142,16535265,20143352,22925447,23727774,26654204,7118830.
  accessed_at: '2026-10-21T07:37:22Z'
  support: context_only
  summary: All identifiers resolve and all abstracts were read. PMID10470142 concerns
    host-cell growth/histone effects;22925447 concerns leukemic coumarin analogues.
    PMID16535265 addresses enantioselective degradation,7118830 substrate catabolism,
    and20143352/26654204 identify the acid as a hydrocarbon degradation intermediate.
    These do not directly establish antibacterial targets, clinical efficacy, resistance
    determinants or natural-product biosynthesis. The full2013 study provides the
    direct activity support.
  snapshot_sha256: 4e23c896f8dc17210cddac6217a556f60641f162df965549afce7b8496866bcf
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Actual source runner output039-imodulondb-datasets.txt.
  accessed_at: '2026-10-21T07:37:22Z'
  support: context_only
  summary: The returned28 dataset keys contain no H.pylori dataset for the exact response
    experiment. No matching-organism search or component summary is applicable. Other
    assayed bacterial taxa being covered does not permit protein-response transfer.
    This coverage result is not negative biological evidence.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 039-local-hits.txt and039-focused-local-hits.txt.
  accessed_at: '2026-10-21T07:37:22Z'
  support: context_only
  summary: The inclusive worktree search located source, generated, index and historical
    research references. Focused curation/reviews/historical-review/conf search returned
    no exact-identifier/name matches outside the queue. Historical artifacts were
    treated as leads, not primary support; no global absence conclusion is drawn.
  search_scope: rg --no-ignore --hidden identifier,label,slug across worktree004 excluding
    .git/.venv; additional exact CHEBI:166657,ZZEWMYILWXCRHZ,3-phenylbutyric and beta/β-methylhydrocinnamic
    in curation,reviews,reports/yaml_record_review,conf excluding record_review_queue.tsv.
    Gitignored files included.
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Native identity, activity, evidence, mechanism, producer and status rules;
    CURATION/HARMONIZATION.
  accessed_at: '2026-10-21T07:37:22Z'
  support: supports
  summary: Optional evidence enrichment is not a required-field defect. Keep salts/isomers
    and stereochemical scope distinct, assay evidence at claim level, production separate
    from xenobiotic degradation, and response proteins separate from directly demonstrated
    targets.
- evidence_id: validation
  kind: validation
  reference: Documented per-record validators
  locator: Actual worktree004 focused commands and039-strict.tsv.
  accessed_at: '2026-10-21T07:37:22Z'
  support: supports
  summary: Both focused validators and independent chemistry passed; shared repository
    checks are recorded separately with actual outcomes.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact constitutional and stereochemical scope
  outcome: supported
  summary: Definition, four synonyms and chemical strings describe the3-isomer with
    unspecified stereochemistry. Neither the native string nor the2013 test-material
    description justifies racemate or single-enantiomer claims.
  target_ids:
  - CHEBI:166657
  evidence_ids:
  - record
  - chebi
  - nist
  - pubchem
  - chemistry
  - primary-activity
- assessment_id: grounding
  area: grounding
  topic: Parents, role and xrefs
  outcome: supported
  summary: Broader classes and antibacterial role are coherent. CAS and FooDB identity
    are supported; HMDB MOL agrees in root inspection, with its descriptive confounding
    and unconfirmed full key retained. ChemSpider/Reaxys access limits remain explicit.
  target_ids:
  - CHEBI:166657
  evidence_ids:
  - chebi
  - nist
  - xref
  - owner
- assessment_id: activity
  area: evidence
  topic: Direct exact-compound activity
  outcome: supported
  summary: The complete primary paper supports antibacterial activity with strain-specific
    disc and bactericidal endpoints. These support the role without claiming broad
    potency or clinical use.
  target_ids:
  - CHEBI:166657
  evidence_ids:
  - primary-activity
  - primary-response
- assessment_id: mechanism
  area: evidence
  topic: Response versus direct mechanism
  outcome: unknown
  summary: Native record asserts no target or mode of action. Protein and targeted-transcript
    changes allow qualified response notes, while direct targets and ROS causality
    remain unresolved.
  target_ids:
  - CHEBI:166657
  evidence_ids:
  - record
  - primary-response
  - adapter
- assessment_id: context
  area: representation
  topic: Producers, resistance and clinical context
  outcome: not_applicable
  summary: No native fields require correction. Degradation or growth on the compound
    is not biosynthetic production; organism resistance to metronidazole is not resistance
    to3-PB; host-cell effects and proposed clinical utility are not established antibiotic
    use.
  target_ids:
  - CHEBI:166657
  evidence_ids:
  - record
  - adopted-literature
  - primary-response
  - rubric
- assessment_id: completeness
  area: completeness
  topic: Optional evidence enrichment
  outcome: supported
  summary: Exact-compound measurements and qualified response evidence offer a bounded
    curation path, with method/caption conflicts retained rather than silently normalized.
  target_ids:
  - CHEBI:166657
  evidence_ids:
  - record
  - primary-activity
  - primary-response
- assessment_id: provenance
  area: ownership
  topic: Source, namespace normalization and status
  outcome: supported
  summary: Source row, normalizer, minted identifier and four history events agree.
    Imported identity fixes belong to source/transform owners; scientific additions
    belong to the actual native record. All13 captured hashes are unchanged.
  target_ids:
  - CHEBI:166657
  evidence_ids:
  - record
  - owner
  - rubric
- assessment_id: schema
  area: schema
  topic: Focused native gates
  outcome: supported
  summary: Schema, strict and chemistry pass; these deterministic checks are separate
    from primary scientific assessment.
  target_ids:
  - CHEBI:166657
  evidence_ids:
  - validation
  - chemistry
findings:
- finding_id: F1
  issue_key: chebi-166657-qualified-primary-activity-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Optional primary activity and response evidence can be curated with endpoint
    and assay qualifications
  description: The seed’s antibacterial role is supported, but direct disc/MBC observations
    and bounded protein-response notes remain unrepresented. This is an enrichment
    opportunity, not a current false measurement or required-field omission. Preserve
    isomer/stereochemical scope, distinguish MBC from MIC, and retain method/caption
    conflicts.
  target_ids:
  - CHEBI:166657
  field_paths:
  - activity_spectrum
  - evidence
  - mode_of_action_notes
  evidence_ids:
  - record
  - primary-activity
  - primary-response
  - rubric
  rule_id: 'native-review-checklist: Activity, Evidence and Mode of action'
  native_severity: informational optional enrichment
  normalization_reason: Current identity and role are supported; omitted optional
    assays and response notes do not establish a schema or scientific error.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/3-phenylbutyric-acid.yaml
    role: Curator-owned scientific additions through write_validated_antibiotic and
      native curation history
actions:
- action_id: A1
  description: If selected for curation, add exact3-phenylbutyric-acid activity with
    strain, endpoint, dose, incubation and method qualifiers, and optionally a clearly
    bounded response note.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:166657
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/3-phenylbutyric-acid.yaml
    role: Curator-owned scientific additions through write_validated_antibiotic and
      native curation history
  acceptance_checks:
  - Represent the1 and0.25mg/mL values as MBCs, with99.9% killing and24h exposure/48h
    recovery; do not convert to MIC.
  - Keep disc zone diameter,4mg/disc dose and exact tested organism/strain together;
    no assay-wide or clinically interpreted resistance extrapolation.
  - Retain the inoculum, metronidazole-disc-dose and proteomics-concentration inconsistencies;
    resolve them before claiming unambiguous normalized conditions.
  - Do not add DHQase/Pfr/Ppa as direct molecular targets or ROS as a measured causal
    event from expression data alone; no clinical use or4-isomer/salt activity transfer.
  - Do not infer a racemate or individual enantiomer from unspecified stereochemistry,
    or biosynthetic production from substrate degradation.
  - Use write_validated_antibiotic and native curation history for separately authorized
    additions; rerun focused schema/strict and required corpus checks.
limitations:
- Root inspected FooDB full structure and HMDB MOL. Subsequent review002 direct requests
  were forbidden; independent HMDB full InChI/key remains unconfirmed. ChemSpider
  direct access was403 and Reaxys was not independently inspected; their ChEBI assertions
  are retained without claiming independent identity verification.
- All seven adopted abstracts and complete2013 antibacterial text were inspected;
  the other six full texts were not comprehensively reviewed.
- The2013 paper contains method/caption inconsistencies in inoculum, metronidazole
  combination-disc dose and proteomics concentration. These limit quantitative normalization
  and do not erase its direct activity evidence.
- Protein and targeted RT-PCR results are response evidence; direct binding/inhibition,
  ROS measurement, clinical efficacy and biosynthetic production were not established
  by the inspected experiments.
- iModulonDB has no matching H.pylori dataset. The review and literature search are
  bounded, not a claim that no further mechanism or activity evidence exists.
- No native record edits or paid research occurred. This review does not promote native
  scientific status.
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
