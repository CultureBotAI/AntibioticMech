# Review of biapenem

- Review: 20261021T102347Z-biapenem-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:53:32Z
- Finished UTC: 2026-10-21T10:23:47Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Biapenem identity, formula, stereochemistry and five independently parsed public structure mappings agree. The definition says 1-hydroxymethyl where the encoded molecule and systematic synonyms have (1R)-1-hydroxyethyl. This narrow wording correction does not require changing the structure. Compound-specific primary abstracts support antibacterial activity and optional PBP-mechanism enrichment, with full-text access limitations.

## Scope And Provenance

Whole SEEDED record and four history events; adopted ChEBI/ARO identity owners and all five compound/class literature leads; current chemistry mappings and bounded primary activity/mechanism follow-up.

Selection: Queue index155; coordinator preserved initial13 inputs before judgment; two additional owner tables and external ARO cache hashed before reading.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:3089 | data/antibiotics/antibacterial/biapenem.yaml | generated | biapenem |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema check | passed | True | CHEBI:3089 | Exit0. |
| Documented strict check | passed | True | CHEBI:3089 | Exit0;zero ERROR rows. |
| Supplemental literal source-text comparison | failed | False | CHEBI:3089 | Exit1 after exact graph checks: current OLS definition contains HTML emphasis markup. |
| Supplemental graph and substituent verification | passed | False | CHEBI:3089 | Exit0 after removing HTML tags only from definition comparison. No structural normalization weakened the exact graph comparison. |
| Native iModulonDB catalog | passed | False | CHEBI:3089 | Exit0 before detailed protein-paper follow-up. The native record itself names no protein. |
| Native iModulonDB contextual search | passed | False | CHEBI:3089 | Exit0;five pneumococcal PBP genes,zero iModulons; no summary applied. |
| Authoritative full QC | failed | True | CHEBI:3089 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:3089 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:3089 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:3089 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:3089 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:3089 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:3089 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:3089 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:3089 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact encoded chemical entity

identity: supported. Targets: CHEBI:3089.

Zwitterionic structure, all configured centers and independently parsed public mappings agree.

### Definition substituent

nomenclature: concern. Targets: CHEBI:3089.

The definition names a different carbon-length substituent from the graph and systematic synonyms.

### Broader classes and activity roles

grounding: supported. Targets: CHEBI:3089.

Three ChEBI structural parents and ARO carbapenem class fit; primary activity supports antibacterial filing.

### Claim and source scope

evidence: supported. Targets: CHEBI:3089.

No native mechanism is overclaimed. Available primary abstracts provide qualified optional target/activity follow-up.

### Generated provenance and leads

provenance: supported. Targets: CHEBI:3089.

Five adopted/ontology-linked lead records are accounted for, including one metadata-only class review. Four-event history is consistent.

### Correction and optional enrichment

completeness: concern. Targets: CHEBI:3089.

Correct the narrow definition; optional mechanism fields require full methods and exact protein/assay scope before import.

### Focused checks

schema: supported. Targets: CHEBI:3089.

Schema and strict checks pass, with supplemental assertion failure and normalized rerun retained.

## Findings

### F1: Correct hydroxymethyl to hydroxyethyl in the definition

minor / open / confirmed; issue key: chebi-3089-definition-hydroxymethyl-hydroxyethyl.

The C6 side chain is (1R)-1-hydroxyethyl, CH(OH)CH3. The source-derived definition instead says 1-hydroxymethyl. Native graph, formula, stereochemical identifiers and systematic synonyms are consistent with biapenem, so the demonstrated defect is bounded to the textual substituent description.

## Recommended Actions And Acceptance Checks

### A1

Repair the source-owned definition while preserving the verified exact graph.

- Replace the erroneous 1-hydroxymethyl description with (1R)-1-hydroxyethyl, keeping its C6 attachment and the remaining supported ring/substituent description chemically correct.
- Obtain a corrected upstream ChEBI definition or use a maintained literature/structure-backed override with truthful definition_source. Do not silently attribute curator-rewritten text to an unchanged source.
- Canary regeneration must reproduce the corrected definition with unchanged verified structure identifiers and stereochemistry. Pass required native gates and append history only through the authorized writer if a future curation edit is made.
- If optionally enriching mechanism/activity, inspect original methods and preserve protein species/construct, covalent-adduct interpretation and assay scope. Do not turn MIC90 into a single isolate MIC or purified hydrolysis into automatic host resistance.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/biapenem.yaml; Entire YAML and four history events | supports | SEEDED exact zwitterion with carbapenem class, antimicrobial/antibacterial roles and database identity provenance. No molecular target, mode of action, resistance, MIC or causal graph is asserted. |
| chemistry | CHEBI:3089;PubChem:71339;ChEMBL:CHEMBL285347;KEGG:C11268;KEGG:D01057;DrugCentral:365; 155-chemistry-normalized.py;155-chemistry.json;current database artifacts | partial | Native SMILES/InChI, C15H18N4O4S, net charge0, masses, four configured centers and both mints agree. All five parsed external graphs yield MRMBZHPJVKCOMA-YJFSRANCSA-N. Native atom21 bears OH and methyl (atoms23/22), a CH(OH)CH3 substituent; no CH2OH motif exists. The systematic native synonyms independently name 1-hydroxyethyl. |
| definition | CHEBI:3089; 155-ols.json;data/raw/chebi_antimicrobials.tsv | partial | Current and adopted ChEBI definitions both retain 1-hydroxymethyl, inconsistent with their structure and systematic synonym. OLS italic markup around the ring-fusion letter is a separate rendering difference. Current parents are organic sulfide, carbapenems and pyrazolotriazole; these are appropriate broader classes. |
| activity | PMID:8031067; DOI:10.1128/AAC.38.4.889;155-core.json;155-activity-primary.html abstract | supports | The original complete abstract reports broth-microdilution testing of441 clinical anaerobic strains and supports the antibacterial classification. Its population MIC90 values are not individual-strain observations, universal breakpoints or direct target assays. |
| leads | All five adopted compound/class PMID leads; 155-core.json;155-lead-dispositions.json | context_only | Both ChEBI citations and both ARO compound citations resolve, with8031067 shared. PMID28543395 is a cefotiam-specific allergy case/control context; it is not biapenem antibacterial or allergy proof. PMID12381221 is a biapenem review. Class leads11585791 and15673804 are beta-lactamase reviews; the latter has no abstract and was metadata-only. |
| pbp | PMID:18391040;PMID:7768785; DOI:10.1128/AAC.01456-07;DOI:10.1093/jac/35.1.75;155-pbp-core.json;155-extra-core.json;complete abstracts | context_only | The crystallographic study reports biapenem complexes with trypsin-digested pneumococcal R6 PBP2X/PBP1A. The earlier biochemical study reports species-specific PBP binding and distinguishes permeability from beta-lactamase susceptibility. These support optional bounded primary mechanism enrichment; they do not justify copying intact-parent identity onto a covalent ring-opened adduct. |
| additional | PMID:7574520;PMID:8239623; 155-extra-core.json;complete abstracts | context_only | The first paper distinguishes purified metallo-beta-lactamase inactivation from failure of some expressed enzymes to confer host resistance. The second reports activity across771 clinical isolates. Neither is evidence that all beta-lactamases are resisted or that every strain is susceptible. |
| aro | ARO:3007083;ARO:0000020; 155-aro-stanzas.txt;data/raw/aro_antibiotics.tsv | supports | ARO preserves biapenem identity and carbapenem class, including source synonyms Biapenern/Bipenem/Omegacin. Brand spelling is database context, not evidence that every formulation is the isolated exact zwitterion. |
| aro-cache | External ARO cache; /Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/downloads/aro.obo;155-aro-cache-hash.json | context_only | Hashed before relevant stanza reading and rechecked. Kept separate from repository input provenance. |
| adapter | iModulonDB native CLI; 155-imodulondb-datasets.txt;155-imodulondb-pbp.txt | context_only | Context search returned SP_0336/pbpX and SP_0369/ponA among five genes, but zero iModulons. The dataset is not asserted to be the experimental R6 construct, and gene membership is not direct drug-binding evidence. |
| validation | Focused native validators; 155-strict.tsv | supports | Schema/strict exit0; optional source-string check initially failed on HTML markup, then passed with tag stripping. The chemical naming concern is a scientific comparison beyond those gates. |
| owners | Maintained ChEBI extraction/seeding path; data/raw/chebi_antimicrobials.tsv;scripts/extract_source_inventory.py;scripts/seed_from_sources.py | context_only | The native definition copies the adopted ChEBI definition, so any correction needs an updated upstream/adopted source or maintained attributed override that survives regeneration. |

## Limits And Additional Notes

- The adopted activity original was accessible as a complete abstract/scanned-article landing page; its exact linked PDF returned a browser challenge. Detailed methods/tables were not independently read.
- Both primary PBP papers and the additional enzyme/activity studies were inspected through complete abstracts. The PBP full-text XML returned500, PMC renderings returned browser challenges and Europe PMC returned403; no full original target Methods were claimed. An initial guessed publisher DOI was not the resolved paper and was rejected as evidence.
- PMID15673804 has no abstract; only its bibliographic metadata were checked. The cefotiam case report was read as a complete abstract and retained only as context, without inferring biapenem cross-reactivity or activity.
- Beilstein identifiers were not independently checked against a licensed source. CAS mapping is reproduced by adopted/public identity sources rather than an independently accessed registry.
- Initial public requests failed sandbox DNS and were retried successfully where stated. ChEMBL initially timed out and succeeded on retry. The graph check initially failed only on OLS HTML markup; the failed result remains explicit.
- The pre-web trigger is absent from the native record; after exploratory protein leads appeared, the native adapter was run before detailed follow-up. No expression-module result was used as binding proof.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 15 repository input hashes and the external ARO cache are unchanged. No native record or maintained source was edited.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T102347Z-biapenem-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of biapenem
started_at: '2026-10-21T09:53:32Z'
finished_at: '2026-10-21T10:23:47Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Exact zwitterionic structure supported; source-derived definition
  has a substituent naming error
scientific_review: true
summary: Biapenem identity, formula, stereochemistry and five independently parsed
  public structure mappings agree. The definition says 1-hydroxymethyl where the encoded
  molecule and systematic synonyms have (1R)-1-hydroxyethyl. This narrow wording correction
  does not require changing the structure. Compound-specific primary abstracts support
  antibacterial activity and optional PBP-mechanism enrichment, with full-text access
  limitations.
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
  - path: data/antibiotics/antibacterial/biapenem.yaml
    sha256: 69f0cb71be6a546e3f89b89bf612fb0b67b2235f49aac56c281e3b24475b7682
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
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
scope:
  description: Whole SEEDED record and four history events; adopted ChEBI/ARO identity
    owners and all five compound/class literature leads; current chemistry mappings
    and bounded primary activity/mechanism follow-up.
  selection: Queue index155; coordinator preserved initial13 inputs before judgment;
    two additional owner tables and external ARO cache hashed before reading.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:3089
targets:
- target_id: CHEBI:3089
  path: data/antibiotics/antibacterial/biapenem.yaml
  label: biapenem
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
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO/PubChem source owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted ARO/PubChem source owner
checks:
- check_id: schema
  name: Documented schema check
  status: passed
  required: true
  summary: Exit0.
  target_ids:
  - CHEBI:3089
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/biapenem.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict check
  status: passed
  required: true
  summary: Exit0;zero ERROR rows.
  target_ids:
  - CHEBI:3089
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/biapenem.yaml --out /private/tmp/am-review-session/155-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry-literal
  name: Supplemental literal source-text comparison
  status: failed
  required: false
  summary: 'Exit1 after exact graph checks: current OLS definition contains HTML emphasis
    markup.'
  target_ids:
  - CHEBI:3089
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/155-chemistry.py
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: chemistry
  name: Supplemental graph and substituent verification
  status: passed
  required: false
  summary: Exit0 after removing HTML tags only from definition comparison. No structural
    normalization weakened the exact graph comparison.
  target_ids:
  - CHEBI:3089
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/155-chemistry-normalized.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: adapter-catalog
  name: Native iModulonDB catalog
  status: passed
  required: false
  summary: Exit0 before detailed protein-paper follow-up. The native record itself
    names no protein.
  target_ids:
  - CHEBI:3089
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-search
  name: Native iModulonDB contextual search
  status: passed
  required: false
  summary: Exit0;five pneumococcal PBP genes,zero iModulons; no summary applied.
  target_ids:
  - CHEBI:3089
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism s_pneumoniae --dataset precise718 --query
    penicillin
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:3089
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
  - CHEBI:3089
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
  - CHEBI:3089
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
  - CHEBI:3089
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
  - CHEBI:3089
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
  - CHEBI:3089
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
  - CHEBI:3089
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
  - CHEBI:3089
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
  - CHEBI:3089
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/biapenem.yaml
  locator: Entire YAML and four history events
  accessed_at: '2026-10-21T10:04:20Z'
  support: supports
  summary: SEEDED exact zwitterion with carbapenem class, antimicrobial/antibacterial
    roles and database identity provenance. No molecular target, mode of action, resistance,
    MIC or causal graph is asserted.
- evidence_id: chemistry
  kind: validation
  reference: CHEBI:3089;PubChem:71339;ChEMBL:CHEMBL285347;KEGG:C11268;KEGG:D01057;DrugCentral:365
  locator: 155-chemistry-normalized.py;155-chemistry.json;current database artifacts
  accessed_at: '2026-10-21T10:04:20Z'
  support: partial
  summary: Native SMILES/InChI, C15H18N4O4S, net charge0, masses, four configured
    centers and both mints agree. All five parsed external graphs yield MRMBZHPJVKCOMA-YJFSRANCSA-N.
    Native atom21 bears OH and methyl (atoms23/22), a CH(OH)CH3 substituent; no CH2OH
    motif exists. The systematic native synonyms independently name 1-hydroxyethyl.
  snapshot_sha256: 0bcf97afbd7e858448fa1936f54a5f5d10b1ab10347e5ff87095122ac09cbafe
- evidence_id: definition
  kind: database
  reference: CHEBI:3089
  locator: 155-ols.json;data/raw/chebi_antimicrobials.tsv
  accessed_at: '2026-10-21T10:04:20Z'
  support: partial
  summary: Current and adopted ChEBI definitions both retain 1-hydroxymethyl, inconsistent
    with their structure and systematic synonym. OLS italic markup around the ring-fusion
    letter is a separate rendering difference. Current parents are organic sulfide,
    carbapenems and pyrazolotriazole; these are appropriate broader classes.
  snapshot_sha256: 27ec813929fb173e9f600e752c1c6c3c19e6c59b5de50ee5eddf71996f1eda9d
- evidence_id: activity
  kind: primary_source
  reference: PMID:8031067
  locator: DOI:10.1128/AAC.38.4.889;155-core.json;155-activity-primary.html abstract
  accessed_at: '2026-10-21T10:04:20Z'
  support: supports
  summary: The original complete abstract reports broth-microdilution testing of441
    clinical anaerobic strains and supports the antibacterial classification. Its
    population MIC90 values are not individual-strain observations, universal breakpoints
    or direct target assays.
  snapshot_sha256: dff4c1cee178b3917781bbf1ba1fa287fa25b059b05313bb7673a1addd3ac98f
- evidence_id: leads
  kind: search
  reference: All five adopted compound/class PMID leads
  locator: 155-core.json;155-lead-dispositions.json
  accessed_at: '2026-10-21T10:04:20Z'
  support: context_only
  summary: Both ChEBI citations and both ARO compound citations resolve, with8031067
    shared. PMID28543395 is a cefotiam-specific allergy case/control context; it is
    not biapenem antibacterial or allergy proof. PMID12381221 is a biapenem review.
    Class leads11585791 and15673804 are beta-lactamase reviews; the latter has no
    abstract and was metadata-only.
  snapshot_sha256: 5b2f0899ee32a67bccf26a6df1bc96c94b079a754063f9df0756017df68fbb26
  search_scope: All three unique compound-level leads plus two ARO class-parent leads
    were resolved; four complete abstracts and one metadata-only record. No review
    or unrelated allergy result was upgraded to a primary biapenem assay.
- evidence_id: pbp
  kind: primary_source
  reference: PMID:18391040;PMID:7768785
  locator: DOI:10.1128/AAC.01456-07;DOI:10.1093/jac/35.1.75;155-pbp-core.json;155-extra-core.json;complete
    abstracts
  accessed_at: '2026-10-21T10:04:20Z'
  support: context_only
  summary: The crystallographic study reports biapenem complexes with trypsin-digested
    pneumococcal R6 PBP2X/PBP1A. The earlier biochemical study reports species-specific
    PBP binding and distinguishes permeability from beta-lactamase susceptibility.
    These support optional bounded primary mechanism enrichment; they do not justify
    copying intact-parent identity onto a covalent ring-opened adduct.
  snapshot_sha256: 57c73e352e3820a1706e583a3c38573ab2b61c6ec920085cab7333567daee6d2
- evidence_id: additional
  kind: primary_source
  reference: PMID:7574520;PMID:8239623
  locator: 155-extra-core.json;complete abstracts
  accessed_at: '2026-10-21T10:04:20Z'
  support: context_only
  summary: The first paper distinguishes purified metallo-beta-lactamase inactivation
    from failure of some expressed enzymes to confer host resistance. The second reports
    activity across771 clinical isolates. Neither is evidence that all beta-lactamases
    are resisted or that every strain is susceptible.
  snapshot_sha256: b83fcf6f4493a33b0ad5db702663f678a66d5b91d68a02db13d377eb60c240aa
- evidence_id: aro
  kind: database
  reference: ARO:3007083;ARO:0000020
  locator: 155-aro-stanzas.txt;data/raw/aro_antibiotics.tsv
  accessed_at: '2026-10-21T10:04:20Z'
  support: supports
  summary: ARO preserves biapenem identity and carbapenem class, including source
    synonyms Biapenern/Bipenem/Omegacin. Brand spelling is database context, not evidence
    that every formulation is the isolated exact zwitterion.
  snapshot_sha256: 786b543e18ca6644d878e327f1a3a5840e51973ed2f8cda2d3af8fc948cf12f7
- evidence_id: aro-cache
  kind: database
  reference: External ARO cache
  locator: /Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/downloads/aro.obo;155-aro-cache-hash.json
  accessed_at: '2026-10-21T10:04:20Z'
  support: context_only
  summary: Hashed before relevant stanza reading and rechecked. Kept separate from
    repository input provenance.
  snapshot_sha256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
- evidence_id: adapter
  kind: validation
  reference: iModulonDB native CLI
  locator: 155-imodulondb-datasets.txt;155-imodulondb-pbp.txt
  accessed_at: '2026-10-21T10:04:20Z'
  support: context_only
  summary: Context search returned SP_0336/pbpX and SP_0369/ponA among five genes,
    but zero iModulons. The dataset is not asserted to be the experimental R6 construct,
    and gene membership is not direct drug-binding evidence.
- evidence_id: validation
  kind: validation
  reference: Focused native validators
  locator: 155-strict.tsv
  accessed_at: '2026-10-21T10:04:20Z'
  support: supports
  summary: Schema/strict exit0; optional source-string check initially failed on HTML
    markup, then passed with tag stripping. The chemical naming concern is a scientific
    comparison beyond those gates.
- evidence_id: owners
  kind: record_content
  reference: Maintained ChEBI extraction/seeding path
  locator: data/raw/chebi_antimicrobials.tsv;scripts/extract_source_inventory.py;scripts/seed_from_sources.py
  accessed_at: '2026-10-21T10:04:20Z'
  support: context_only
  summary: The native definition copies the adopted ChEBI definition, so any correction
    needs an updated upstream/adopted source or maintained attributed override that
    survives regeneration.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact encoded chemical entity
  outcome: supported
  summary: Zwitterionic structure, all configured centers and independently parsed
    public mappings agree.
  target_ids:
  - CHEBI:3089
  evidence_ids:
  - chemistry
- assessment_id: wording
  area: nomenclature
  topic: Definition substituent
  outcome: concern
  summary: The definition names a different carbon-length substituent from the graph
    and systematic synonyms.
  target_ids:
  - CHEBI:3089
  evidence_ids:
  - definition
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Broader classes and activity roles
  outcome: supported
  summary: Three ChEBI structural parents and ARO carbapenem class fit; primary activity
    supports antibacterial filing.
  target_ids:
  - CHEBI:3089
  evidence_ids:
  - definition
  - aro
  - activity
- assessment_id: evidence
  area: evidence
  topic: Claim and source scope
  outcome: supported
  summary: No native mechanism is overclaimed. Available primary abstracts provide
    qualified optional target/activity follow-up.
  target_ids:
  - CHEBI:3089
  evidence_ids:
  - record
  - activity
  - pbp
  - additional
  - leads
- assessment_id: provenance
  area: provenance
  topic: Generated provenance and leads
  outcome: supported
  summary: Five adopted/ontology-linked lead records are accounted for, including
    one metadata-only class review. Four-event history is consistent.
  target_ids:
  - CHEBI:3089
  evidence_ids:
  - record
  - leads
  - owners
- assessment_id: completeness
  area: completeness
  topic: Correction and optional enrichment
  outcome: concern
  summary: Correct the narrow definition; optional mechanism fields require full methods
    and exact protein/assay scope before import.
  target_ids:
  - CHEBI:3089
  evidence_ids:
  - definition
  - pbp
  - additional
- assessment_id: schema
  area: schema
  topic: Focused checks
  outcome: supported
  summary: Schema and strict checks pass, with supplemental assertion failure and
    normalized rerun retained.
  target_ids:
  - CHEBI:3089
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: chebi-3089-definition-hydroxymethyl-hydroxyethyl
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: Correct hydroxymethyl to hydroxyethyl in the definition
  description: The C6 side chain is (1R)-1-hydroxyethyl, CH(OH)CH3. The source-derived
    definition instead says 1-hydroxymethyl. Native graph, formula, stereochemical
    identifiers and systematic synonyms are consistent with biapenem, so the demonstrated
    defect is bounded to the textual substituent description.
  target_ids:
  - CHEBI:3089
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - chemistry
  - definition
  - owners
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
  rule_id: 'review-checklist: definition agrees with exact structure and source scope'
  native_severity: minor source-derived chemical naming error
  normalization_reason: The text needs a substantive naming correction, but all exact
    identity fields and systematic names already denote the supported compound; no
    encoded graph or grounding error was found.
actions:
- action_id: A1
  description: Repair the source-owned definition while preserving the verified exact
    graph.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:3089
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
  acceptance_checks:
  - Replace the erroneous 1-hydroxymethyl description with (1R)-1-hydroxyethyl, keeping
    its C6 attachment and the remaining supported ring/substituent description chemically
    correct.
  - Obtain a corrected upstream ChEBI definition or use a maintained literature/structure-backed
    override with truthful definition_source. Do not silently attribute curator-rewritten
    text to an unchanged source.
  - Canary regeneration must reproduce the corrected definition with unchanged verified
    structure identifiers and stereochemistry. Pass required native gates and append
    history only through the authorized writer if a future curation edit is made.
  - If optionally enriching mechanism/activity, inspect original methods and preserve
    protein species/construct, covalent-adduct interpretation and assay scope. Do
    not turn MIC90 into a single isolate MIC or purified hydrolysis into automatic
    host resistance.
limitations:
- The adopted activity original was accessible as a complete abstract/scanned-article
  landing page; its exact linked PDF returned a browser challenge. Detailed methods/tables
  were not independently read.
- Both primary PBP papers and the additional enzyme/activity studies were inspected
  through complete abstracts. The PBP full-text XML returned500, PMC renderings returned
  browser challenges and Europe PMC returned403; no full original target Methods were
  claimed. An initial guessed publisher DOI was not the resolved paper and was rejected
  as evidence.
- PMID15673804 has no abstract; only its bibliographic metadata were checked. The
  cefotiam case report was read as a complete abstract and retained only as context,
  without inferring biapenem cross-reactivity or activity.
- Beilstein identifiers were not independently checked against a licensed source.
  CAS mapping is reproduced by adopted/public identity sources rather than an independently
  accessed registry.
- Initial public requests failed sandbox DNS and were retried successfully where stated.
  ChEMBL initially timed out and succeeded on retry. The graph check initially failed
  only on OLS HTML markup; the failed result remains explicit.
- The pre-web trigger is absent from the native record; after exploratory protein
  leads appeared, the native adapter was run before detailed follow-up. No expression-module
  result was used as binding proof.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 15 repository input hashes and the external ARO cache are unchanged. No native
  record or maintained source was edited.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:3089
- https://pubchem.ncbi.nlm.nih.gov/compound/71339
- https://doi.org/10.1128/AAC.38.4.889
- https://doi.org/10.1128/AAC.01456-07
tags:
- record-review
- biapenem
- carbapenem
- definition-correction
```
