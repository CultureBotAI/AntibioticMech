# Review of brodimoprim

- Review: 20261021T103143Z-brodimoprim-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:10:58Z
- Finished UTC: 2026-10-21T10:31:43Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

No demonstrated scientific defect was found. Brodimoprim identity agrees across four public external structures. Primary enzyme evidence supports DHFR inhibition, and the record correctly labels the CARD target as needing primary evidence while retaining host-shared target scope. Quantitative/selectivity enrichment would require the original full assay details. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire SEEDED record and five history events; identity, roles, folate mechanism, CARD target provenance and maintained owners; all eleven adopted/ontology-linked PMID leads and two supplemental literature leads; public chemical structure comparisons and native structured target lookup.

Selection: Queue index171; coordinator initial13 inputs preserved, with ARO identity and target-edge tables hashed before inspection. External ARO cache tracked separately.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:131726 | data/antibiotics/antibacterial/brodimoprim.yaml | generated | brodimoprim |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema check | passed | True | CHEBI:131726 | Exit0. |
| Documented strict check | passed | True | CHEBI:131726 | Exit0;zero ERROR rows. |
| Supplemental chemistry/source assertions | passed | False | CHEBI:131726 | Exit0; four external graph comparisons and native role/target provenance agree. |
| Native iModulonDB catalog | passed | False | CHEBI:131726 | Exit0 before open-ended protein research. |
| Native FolA contextual search | passed | False | CHEBI:131726 | Exit0;nine gene hits,zero iModulons;direct folA match is b0048. |
| Authoritative full QC | failed | True | CHEBI:131726 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:131726 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:131726 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:131726 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:131726 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:131726 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:131726 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:131726 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:131726 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact compound

identity: supported. Targets: CHEBI:131726.

Four public structures support native identity; no salt or analogue conflation found.

### Chemical class and activity role

grounding: supported. Targets: CHEBI:131726.

Bromobenzene,methoxybenzene and aminopyrimidine parents fit; antibacterial classification is supported.

### DHFR/folate mechanism

evidence: supported. Targets: CHEBI:131726.

Exact primary enzyme abstract supports broad inhibition; native source attribution and host-shared scope are appropriately bounded.

### Analogue and host scope

scope: supported. Targets: CHEBI:131726.

Carboxylated analogue contacts, general TMP selectivity and host PK outcomes are not transferred into native direct evidence.

### Primary evidence enrichment

completeness: unknown. Targets: CHEBI:131726.

The explicit primary-evidence-needed target could be enriched after full enzyme methods/results are inspected. This acknowledged gap is not a demonstrated false assertion.

### Sources and history

provenance: supported. Targets: CHEBI:131726.

All five history events and eleven adopted/ontology leads checked at declared depth; maintained owners identified.

### Focused gates

schema: supported. Targets: CHEBI:131726.

Focused and supplemental assertions pass.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/brodimoprim.yaml; Whole YAML and five reseed/history events | supports | Exact SEEDED compound has bacterial class, database-attributed folate inhibition and a CARD DHFR direct-target assertion explicitly marked PRIMARY_EVIDENCE_NEEDED. HOST_SHARED_TARGET describes enzyme distribution, not equal inhibition of bacterial and host enzymes. No numerical MIC, biochemical selectivity ratio, producer or protein example is asserted. |
| chemistry | CHEBI:131726;PubChem:68760;ChEMBL:CHEMBL31891;KEGG:D07238;DrugCentral:398; 171-chemistry.py;171-chemistry.json;current downloaded artifacts | supports | Native structure, neutral C13H15BrN4O2, masses and source mints agree. Four external parsed structures reproduce BFCRRLMMHNLSCP-UHFFFAOYSA-N with no stereocenters. The 4-bromo-3,5-dimethoxybenzyl/2,4-diaminopyrimidine definition and current ChEBI broader classes agree. KEGG/DrugCentral remain drug-context links. |
| source | CHEBI:50683;ARO:3000745;ARO:3000269;ARO:3000171; 171-role.json;171-aro-stanzas.txt;data/raw/aro_target_edges.tsv;data/raw/chebi_antimicrobials.tsv | supports | Nonobsolete DHFR-inhibitor role and the adopted target edge reproduce the native source-attributed mechanism. ARO class/compound descriptions agree. The general FolA ontology citation is not an exact-compound target assay. |
| enzyme | PMID:6363003; DOI:10.1159/000238239;171-core.json complete original abstract | supports | Original biochemical work reports brodimoprim as a reversible tight-binding inhibitor of bacterial DHFRs using IC50/Ki evidence, and also reports eukaryotic-enzyme inhibition. This supports the broad target and host-shared scope. It does not justify a precise species/strain-specific potency value or direct-binding geometry without full methods/results. |
| analogue-boundary | PMID:10026296; DOI:10.1021/bi982359u;171-core.json complete abstract | context_only | NMR interactions with Lactobacillus casei DHFR concern carboxylated brodimoprim analogues. Their added carboxylate/Arg57 contacts are not contacts demonstrated for unmodified brodimoprim. The native record does not import them. |
| activity | PMID:6847174; DOI:10.1128/AAC.23.3.490;171-extra-core.json complete abstract | supports | Original anaerobic-bacteria study tests brodimoprim and metioprim separately and with sulfonamides. Relative single-agent and combination results differ, supporting antibacterial activity while requiring regimen-specific interpretation. Full scanned article was not retrieved. |
| clinical-context | PMID:7164825;PMID:8195840;PMID:8195841;PMID:8195848; 171-core.json;abstracts | context_only | Dog bone penetration, human pharmacokinetics and respiratory comparative trials concern exact brodimoprim/Ro10-5970 but do not establish microbial target binding. The8195840 abstract is explicitly truncated at250words. No dosage, efficacy recommendation or quantitative native claim is derived from these summaries. |
| reviews | PMID:7562018;PMID:8195838;PMID:8195832;PMID:8195830;PMID:12781525;PMID:7051237; 171-core.json;171-extra-core.json;complete abstracts | context_only | The first four provide clinical/resistance/spectrum or diaminopyrimidine selectivity context; some primarily discuss trimethoprim.12781525 discusses bacteria lacking conventional FolA, not brodimoprim binding.7051237 compares multiple trimethoprim analogues. None supplies an exact new strain-specific mechanism annotation on its own. |
| leads | All eleven adopted and ontology-linked PMID leads; 171-lead-dispositions.json;171-core.json | context_only | All eleven resolved:ten complete abstracts and one explicitly truncated pharmacokinetic abstract read. Two additional study leads were resolved separately. The single exact native target assertion remains honestly database-attributed. |
| adapter | e_coli/modulome/b0048; 171-imodulondb-datasets.txt;171-imodulondb-fola.txt | context_only | Native lookup precedes web follow-up. folA/b0048 matches DHFR, but zero iModulons were returned. This is contextual discovery, not direct inhibitor binding, and is not imported as the unspecified CARD target organism. |
| aro-cache | External ARO cache; /Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/downloads/aro.obo;171-aro-cache-hash.json | context_only | Hashed before relevant term inspection and rechecked; distinct from repository inputs. |
| validation | Focused native schema/strict gates; 171-strict.tsv | supports | Schema and strict checks pass. Supplementary assertions independently reconcile chemical identifiers and adopted mechanistic owners. |

## Limits And Additional Notes

- The original1984 enzyme study was available as a complete abstract only; the Karger route was inaccessible/403. Species-specific Ki/IC50 values, cofactor conditions and direct structural binding were not independently re-extracted. The native target remains PRIMARY_EVIDENCE_NEEDED.
- Ten adopted abstracts were complete; PMID8195840 is explicitly truncated at250words. A publisher full-text route was inaccessible. Pharmacokinetic/clinical summaries were not used as detailed mechanistic or treatment evidence.
- The supplemental1983 anaerobic study was read at complete-abstract depth; PMC challenged and EPMC XML returned500. No strain-specific quantitative MIC is proposed. The1982 analogue overview was read as a complete abstract only.
- The1999 NMR paper describes carboxylated analogues, not unmodified brodimoprim. It must not be used to assign the analogue Arg57 contacts to this exact compound.
- Licensed Reaxys and authoritative CAS records were not independently accessed. Public ChEBI and four independent exact structures support identity without a licensed registry audit.
- No exhaustive resistance-gene, clinical-outcome or structure-activity survey was undertaken. Optional protein examples/causal graphs require separate exact-system evidence; iModulon discovery does not prove target binding.
- Focused validators do not establish full-corpus success or promote native SEEDED status.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 15 repository input hashes and the external ARO cache remain unchanged; no native or saved-bundle edits.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T103143Z-brodimoprim-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of brodimoprim
started_at: '2026-10-21T10:10:58Z'
finished_at: '2026-10-21T10:31:43Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
native_verdict: Exact identity and bounded database-attributed DHFR mechanism supported
scientific_review: true
summary: No demonstrated scientific defect was found. Brodimoprim identity agrees
  across four public external structures. Primary enzyme evidence supports DHFR inhibition,
  and the record correctly labels the CARD target as needing primary evidence while
  retaining host-shared target scope. Quantitative/selectivity enrichment would require
  the original full assay details. Scientific assessment retains the stated evidence
  limits; full verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/brodimoprim.yaml
    sha256: 15fa626417d0d4e543f08704ad5fe00841fb4fecf65baca06ec278d2235f22e3
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
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: context
scope:
  description: Entire SEEDED record and five history events; identity, roles, folate
    mechanism, CARD target provenance and maintained owners; all eleven adopted/ontology-linked
    PMID leads and two supplemental literature leads; public chemical structure comparisons
    and native structured target lookup.
  selection: Queue index171; coordinator initial13 inputs preserved, with ARO identity
    and target-edge tables hashed before inspection. External ARO cache tracked separately.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:131726
targets:
- target_id: CHEBI:131726
  path: data/antibiotics/antibacterial/brodimoprim.yaml
  label: brodimoprim
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
    role: Adopted ARO identity or target edge owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Adopted ARO identity or target edge owner
checks:
- check_id: schema
  name: Documented schema check
  status: passed
  required: true
  summary: Exit0.
  target_ids:
  - CHEBI:131726
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/brodimoprim.yaml
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
  - CHEBI:131726
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/brodimoprim.yaml --out /private/tmp/am-review-session/171-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Supplemental chemistry/source assertions
  status: passed
  required: false
  summary: Exit0; four external graph comparisons and native role/target provenance
    agree.
  target_ids:
  - CHEBI:131726
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/171-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
  - source
- check_id: adapter-catalog
  name: Native iModulonDB catalog
  status: passed
  required: false
  summary: Exit0 before open-ended protein research.
  target_ids:
  - CHEBI:131726
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets > /private/tmp/am-review-session/171-imodulondb-datasets.txt
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: adapter-search
  name: Native FolA contextual search
  status: passed
  required: false
  summary: Exit0;nine gene hits,zero iModulons;direct folA match is b0048.
  target_ids:
  - CHEBI:131726
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset modulome --query folA
    > /private/tmp/am-review-session/171-imodulondb-fola.txt
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
  - CHEBI:131726
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
  - CHEBI:131726
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
  - CHEBI:131726
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
  - CHEBI:131726
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
  - CHEBI:131726
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
  - CHEBI:131726
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
  - CHEBI:131726
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
  - CHEBI:131726
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
  - CHEBI:131726
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/brodimoprim.yaml
  locator: Whole YAML and five reseed/history events
  accessed_at: '2026-10-21T10:20:38Z'
  support: supports
  summary: Exact SEEDED compound has bacterial class, database-attributed folate inhibition
    and a CARD DHFR direct-target assertion explicitly marked PRIMARY_EVIDENCE_NEEDED.
    HOST_SHARED_TARGET describes enzyme distribution, not equal inhibition of bacterial
    and host enzymes. No numerical MIC, biochemical selectivity ratio, producer or
    protein example is asserted.
- evidence_id: chemistry
  kind: validation
  reference: CHEBI:131726;PubChem:68760;ChEMBL:CHEMBL31891;KEGG:D07238;DrugCentral:398
  locator: 171-chemistry.py;171-chemistry.json;current downloaded artifacts
  accessed_at: '2026-10-21T10:20:38Z'
  support: supports
  summary: Native structure, neutral C13H15BrN4O2, masses and source mints agree.
    Four external parsed structures reproduce BFCRRLMMHNLSCP-UHFFFAOYSA-N with no
    stereocenters. The 4-bromo-3,5-dimethoxybenzyl/2,4-diaminopyrimidine definition
    and current ChEBI broader classes agree. KEGG/DrugCentral remain drug-context
    links.
  snapshot_sha256: 83e15a1cd0465a3b07afafe10af28a2d29e300798486b9ad0820eefcccd76977
- evidence_id: source
  kind: database
  reference: CHEBI:50683;ARO:3000745;ARO:3000269;ARO:3000171
  locator: 171-role.json;171-aro-stanzas.txt;data/raw/aro_target_edges.tsv;data/raw/chebi_antimicrobials.tsv
  accessed_at: '2026-10-21T10:20:38Z'
  support: supports
  summary: Nonobsolete DHFR-inhibitor role and the adopted target edge reproduce the
    native source-attributed mechanism. ARO class/compound descriptions agree. The
    general FolA ontology citation is not an exact-compound target assay.
  snapshot_sha256: 4ab59e9053228f390b740ff5038025f88050661b190df982fbf24c853b1af019
- evidence_id: enzyme
  kind: primary_source
  reference: PMID:6363003
  locator: DOI:10.1159/000238239;171-core.json complete original abstract
  accessed_at: '2026-10-21T10:20:38Z'
  support: supports
  summary: Original biochemical work reports brodimoprim as a reversible tight-binding
    inhibitor of bacterial DHFRs using IC50/Ki evidence, and also reports eukaryotic-enzyme
    inhibition. This supports the broad target and host-shared scope. It does not
    justify a precise species/strain-specific potency value or direct-binding geometry
    without full methods/results.
  snapshot_sha256: e6e14784798dfef7e6d0ca7690fd7c3f857295fcf34f4a06c30f5369dfcd197f
- evidence_id: analogue-boundary
  kind: primary_source
  reference: PMID:10026296
  locator: DOI:10.1021/bi982359u;171-core.json complete abstract
  accessed_at: '2026-10-21T10:20:38Z'
  support: context_only
  summary: NMR interactions with Lactobacillus casei DHFR concern carboxylated brodimoprim
    analogues. Their added carboxylate/Arg57 contacts are not contacts demonstrated
    for unmodified brodimoprim. The native record does not import them.
  snapshot_sha256: e6e14784798dfef7e6d0ca7690fd7c3f857295fcf34f4a06c30f5369dfcd197f
- evidence_id: activity
  kind: primary_source
  reference: PMID:6847174
  locator: DOI:10.1128/AAC.23.3.490;171-extra-core.json complete abstract
  accessed_at: '2026-10-21T10:20:38Z'
  support: supports
  summary: Original anaerobic-bacteria study tests brodimoprim and metioprim separately
    and with sulfonamides. Relative single-agent and combination results differ, supporting
    antibacterial activity while requiring regimen-specific interpretation. Full scanned
    article was not retrieved.
  snapshot_sha256: 3fb356e0d2e90fde123c1cb5d4bb8bd1914f328aacd110ccf8fb3306e0321d4a
- evidence_id: clinical-context
  kind: primary_source
  reference: PMID:7164825;PMID:8195840;PMID:8195841;PMID:8195848
  locator: 171-core.json;abstracts
  accessed_at: '2026-10-21T10:20:38Z'
  support: context_only
  summary: Dog bone penetration, human pharmacokinetics and respiratory comparative
    trials concern exact brodimoprim/Ro10-5970 but do not establish microbial target
    binding. The8195840 abstract is explicitly truncated at250words. No dosage, efficacy
    recommendation or quantitative native claim is derived from these summaries.
  snapshot_sha256: e6e14784798dfef7e6d0ca7690fd7c3f857295fcf34f4a06c30f5369dfcd197f
- evidence_id: reviews
  kind: database
  reference: PMID:7562018;PMID:8195838;PMID:8195832;PMID:8195830;PMID:12781525;PMID:7051237
  locator: 171-core.json;171-extra-core.json;complete abstracts
  accessed_at: '2026-10-21T10:20:38Z'
  support: context_only
  summary: The first four provide clinical/resistance/spectrum or diaminopyrimidine
    selectivity context; some primarily discuss trimethoprim.12781525 discusses bacteria
    lacking conventional FolA, not brodimoprim binding.7051237 compares multiple trimethoprim
    analogues. None supplies an exact new strain-specific mechanism annotation on
    its own.
- evidence_id: leads
  kind: search
  reference: All eleven adopted and ontology-linked PMID leads
  locator: 171-lead-dispositions.json;171-core.json
  accessed_at: '2026-10-21T10:20:38Z'
  support: context_only
  summary: All eleven resolved:ten complete abstracts and one explicitly truncated
    pharmacokinetic abstract read. Two additional study leads were resolved separately.
    The single exact native target assertion remains honestly database-attributed.
  search_scope: Seven ChEBI references, three ARO compound references with one overlap,
    one class reference and one target-term reference; bounded extra activity/analogue
    follow-up.
- evidence_id: adapter
  kind: validation
  reference: e_coli/modulome/b0048
  locator: 171-imodulondb-datasets.txt;171-imodulondb-fola.txt
  accessed_at: '2026-10-21T10:20:38Z'
  support: context_only
  summary: Native lookup precedes web follow-up. folA/b0048 matches DHFR, but zero
    iModulons were returned. This is contextual discovery, not direct inhibitor binding,
    and is not imported as the unspecified CARD target organism.
- evidence_id: aro-cache
  kind: database
  reference: External ARO cache
  locator: /Users/marcin/Documents/VIMSS/ontology/Mechs/AntibioticMech/downloads/aro.obo;171-aro-cache-hash.json
  accessed_at: '2026-10-21T10:20:38Z'
  support: context_only
  summary: Hashed before relevant term inspection and rechecked; distinct from repository
    inputs.
  snapshot_sha256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
- evidence_id: validation
  kind: validation
  reference: Focused native schema/strict gates
  locator: 171-strict.tsv
  accessed_at: '2026-10-21T10:20:38Z'
  support: supports
  summary: Schema and strict checks pass. Supplementary assertions independently reconcile
    chemical identifiers and adopted mechanistic owners.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact compound
  outcome: supported
  summary: Four public structures support native identity; no salt or analogue conflation
    found.
  target_ids:
  - CHEBI:131726
  evidence_ids:
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Chemical class and activity role
  outcome: supported
  summary: Bromobenzene,methoxybenzene and aminopyrimidine parents fit; antibacterial
    classification is supported.
  target_ids:
  - CHEBI:131726
  evidence_ids:
  - chemistry
  - activity
  - source
- assessment_id: mechanism
  area: evidence
  topic: DHFR/folate mechanism
  outcome: supported
  summary: Exact primary enzyme abstract supports broad inhibition; native source
    attribution and host-shared scope are appropriately bounded.
  target_ids:
  - CHEBI:131726
  evidence_ids:
  - enzyme
  - source
  - record
- assessment_id: scope
  area: scope
  topic: Analogue and host scope
  outcome: supported
  summary: Carboxylated analogue contacts, general TMP selectivity and host PK outcomes
    are not transferred into native direct evidence.
  target_ids:
  - CHEBI:131726
  evidence_ids:
  - analogue-boundary
  - reviews
  - clinical-context
- assessment_id: completeness
  area: completeness
  topic: Primary evidence enrichment
  outcome: unknown
  summary: The explicit primary-evidence-needed target could be enriched after full
    enzyme methods/results are inspected. This acknowledged gap is not a demonstrated
    false assertion.
  target_ids:
  - CHEBI:131726
  evidence_ids:
  - record
  - enzyme
- assessment_id: provenance
  area: provenance
  topic: Sources and history
  outcome: supported
  summary: All five history events and eleven adopted/ontology leads checked at declared
    depth; maintained owners identified.
  target_ids:
  - CHEBI:131726
  evidence_ids:
  - record
  - source
  - leads
- assessment_id: schema
  area: schema
  topic: Focused gates
  outcome: supported
  summary: Focused and supplemental assertions pass.
  target_ids:
  - CHEBI:131726
  evidence_ids:
  - validation
  - chemistry
findings: []
actions: []
limitations:
- The original1984 enzyme study was available as a complete abstract only; the Karger
  route was inaccessible/403. Species-specific Ki/IC50 values, cofactor conditions
  and direct structural binding were not independently re-extracted. The native target
  remains PRIMARY_EVIDENCE_NEEDED.
- Ten adopted abstracts were complete; PMID8195840 is explicitly truncated at250words.
  A publisher full-text route was inaccessible. Pharmacokinetic/clinical summaries
  were not used as detailed mechanistic or treatment evidence.
- The supplemental1983 anaerobic study was read at complete-abstract depth; PMC challenged
  and EPMC XML returned500. No strain-specific quantitative MIC is proposed. The1982
  analogue overview was read as a complete abstract only.
- The1999 NMR paper describes carboxylated analogues, not unmodified brodimoprim.
  It must not be used to assign the analogue Arg57 contacts to this exact compound.
- Licensed Reaxys and authoritative CAS records were not independently accessed. Public
  ChEBI and four independent exact structures support identity without a licensed
  registry audit.
- No exhaustive resistance-gene, clinical-outcome or structure-activity survey was
  undertaken. Optional protein examples/causal graphs require separate exact-system
  evidence; iModulon discovery does not prove target binding.
- Focused validators do not establish full-corpus success or promote native SEEDED
  status.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 15 repository input hashes and the external ARO cache remain unchanged; no native
  or saved-bundle edits.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://pubmed.ncbi.nlm.nih.gov/6363003/
- https://doi.org/10.1021/bi982359u
- https://pubchem.ncbi.nlm.nih.gov/compound/68760
tags:
- record-review
- brodimoprim
- dhfr
```
