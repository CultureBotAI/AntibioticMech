# Aurachin A: relative stereochemistry is over-specified in the exact encoded structure

- Review: 20261021T093306Z-aurachin-a-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:04:59Z
- Finished UTC: 2026-10-21T09:33:06Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One confirmed major identity-scope conflict: the definition and systematic synonym explicitly describe relative configuration, while ordinary SMILES and Standard InChI fix two absolute stereocentres. Primary isolation and synthesis reports support relative-only natural-product assignment. The antibacterial role and strain occurrence are supported, but assay transfer must preserve this stereochemical boundary.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position120; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:90924 | data/antibiotics/antibacterial/aurachin-a.yaml | generated | aurachin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:90924 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:90924 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:90924 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:90924 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:90924 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:90924 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:90924 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:90924 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:90924 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:90924 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:90924 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:90924 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Internal validation and native status

schema: supported. Targets: CHEBI:90924.

Focused checks pass; native SEEDED status and source history are unchanged. Review coverage does not promote native status.

### Relative versus absolute stereochemical scope

identity: concern. Targets: CHEBI:90924.

Ordinary structures fix an absolute pair despite the native rel- wording and primary relative-only assignment. Source agreement does not repair this semantic conflict.

### Chemical parents and antibacterial role

grounding: supported. Targets: CHEBI:90924.

Structural parents fit the molecular scaffold and original natural-material assays support antibacterial classification.

### Original antibacterial and host respiration experiments

evidence: supported. Targets: CHEBI:90924.

Primary growth evidence exists, but numeric activity must retain preparation, assay and strain limits. Host mitochondrial respiration is not proof of a direct bacterial target.

### Sg a15 and MYX-030 occurrence

evidence: supported. Targets: CHEBI:90924.

The original production and feeding studies support Sg a15 wording. MYX-030 dereplication is distinct and does not supply aurachin A stereochemical proof.

### Mechanism, resistance, clinical and omics enrichment

completeness: unknown. Targets: CHEBI:90924.

Optional fields are absent without a schema defect. No native gene/protein/pathway or transcriptomic claim triggers an organism-specific adapter. Literature biosynthetic genes and aurachin D targets are not native aurachin A mechanism assertions.

## Findings

### F1: Resolve the over-specified absolute stereochemistry

major / open / confirmed; issue key: aurachin-a-relative-configuration-absolute-encoding.

The relative-configuration natural-product entity and rel- synonym are represented by an ordinary absolute SMILES/InChI pair. The primary assignment and accessible later synthesis discussion do not justify choosing that absolute pair. This is a reproducible source identity-scope inconsistency, not proof that the opposite enantiomer is correct or that the natural sample is racemic.

### F2: Preserve original assay and material scope when enriching activity

informational / open / confirmed; issue key: aurachin-a-primary-assay-scope-enrichment.

The 1987 paper provides isolated-natural-material growth and mitochondrial assays. These are useful optional annotations after the relative-versus-absolute identity issue is resolved, with distinct strain and endpoint limits.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate stereochemical scope through maintained source and exact-identity policy before assigning natural-material evidence.

- Obtain primary evidence for the natural absolute configuration if an exact absolute structure is to be retained; matching secondary database keys do not suffice.
- If only relative configuration is supported, use an explicitly supported representation/policy that preserves the relative pair and E alkene without silently choosing an enantiomer. If the exact-record model cannot express this scope, document a maintained exclusion or qualified treatment rather than inventing absolute assignment.
- Do not call the natural material racemic on the basis of a racemic synthesis. Do not simply strip all stereo and erase known relative information.
- Apply source extraction/seeding or supported maintained decisions so identity repairs reproduce; recheck every structure, synonym, full key, parent and xref and run required corpus gates.

### A2

Optionally curate the original natural-material activity and respiration evidence after resolving identity scope.

- Keep Table 4 serial-dilution MIC separate from Table 3 disk zones; retain unspecified strains where Table 4 does not establish the exact isolate.
- Preserve incomplete fungal inhibition qualifiers and E. coli &gt;50 comparator. The 71 nM beef-heart endpoint is host mitochondrial NADH oxidation, not a bacterial MIC or direct target binding.
- Do not transfer myxocoumarin A assays, aurachin D cryo-EM targets, analog activities or docking-only proposals. Use claim-level primary evidence and the maintained curation workflow.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/aurachin-a.yaml; Entire YAML, including three seed/reseed events | supports | Read the relative-configuration definition, two synonyms, four parents, antibacterial role, complete structure, three chemical xrefs and source mint. The systematic synonym starts rel-. SMILES fixes two carbon centres, and the InChI contains /t23-,25+/m1/s1. No primary mode, target, quantified activity, producer, clinical, graph, resistance or dataset block is present. |
| source | data/raw/chebi_antimicrobials.tsv; Row 2419; ChEBI extraction and seeding | supports | Adopted source reproduces both the relative wording and absolute structure. Four PMID leads are present; they are not automatically promoted to claim-level evidence. No target-specific maintained override was found in the scoped ignored-inclusive search. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:90924; Current entry, OLS parents and PubChem CID 118796887 | partial | Both current sources reproduce neutral C25H33NO3 and key ZEUIHPOXFICJIT-ZVWRMSPBSA-N. ChEBI retains relative configuration in its definition and rel- systematic name. Native parents quinoline N-oxide CHEBI:26508, tertiary alcohol CHEBI:26878, furoquinoline CHEBI:84586 and A-type aurachin CHEBI:90917 are appropriate. The retained antibacterial role is accepted source classification. Matching databases do not independently establish the natural absolute configuration. |
| stereo | Independent RDKit stereochemical interpretation; 120-chemistry.json; native SMILES and InChI | refutes | Both encodings produce two assigned R/S carbon centres and the same full key. These ordinary absolute encodings are more specific than the relative pair in the definition and synonym. The remote E double bond is separately specified and is not implicated by this finding. |
| isolation | PMID:18989924; DOI:10.1021/np8003084; complete abstract | partial | The original feeding study reports isolation of aurachins A–L from Stigmatella aurantiaca Sg a15 and explicitly identifies structures and relative configurations from spectroscopic, particularly NMR, evidence. Isotope-feeding results concern carbon/oxygen origins and interconversion; the abstract does not establish the absolute pair for natural aurachin A. |
| synthesis | DOI:10.1002/adsc.202100884; Stief and Speicher, online 2021 / issue 2022; publisher Introduction through early Results, especially absolute-configuration paragraph | supports | The primary synthesis article explicitly states that natural aurachins A and H had not had their absolute configurations reported. It describes the earlier 2017 aurachin A synthesis as using a racemic epoxide. This supports the native relative-versus-absolute conflict; a synthetic racemate does not prove that the natural product is racemic. Only the accessible Introduction and early Results were read; later publisher access returned 403. |
| primary1987 | PMID:3106289; DOI:10.7164/antibiotics.40.258; complete eight-page paper; original p263 Tables 3–4 visually inspected | supports | The original production paper separates aurachins A–D and documents Sg a15 culture, acetone extraction and chromatographic purification. Table 4 gives aurachin A serial-dilution MICs in standard complex media: B. subtilis 5, S. aureus 2.5, A. aurescens 0.19, B. ammoniagenes 0.39, C. fascians 1.56 and E. coli &gt;50 µg/mL. Table 4 does not itself list strain IDs; do not invent a join to every Table 3 disk-test strain. The 50 µg/mL yeast rows have incomplete inhibition with up to 25% residual turbidity. Table 3 uses 40 µg on 6-mm disks and is a different endpoint. Activity pertains to isolated natural material, not independently established absolute stereochemistry. |
| respiration | DOI:10.7164/antibiotics.40.258; 1987 paper p264 Table 5 and Discussion | supports | Aurachin A inhibits NADH oxidation in beef-heart submitochondrial particles at reported 50%-inhibition concentration 71 nM. The authors explicitly leave the exact mechanism and bacterial inhibitory action unresolved. This host mitochondrial mixture assay is not a bacterial cytochrome-bd binding experiment; later aurachin D or analog structures must not transfer. |
| biosynthesis | PMID:21979787; DOI:10.1039/c1mb05328k; complete abstract | partial | Inactivation mutants in Sg a15 identify tailoring functions in a split aurachin gene-cluster system and motivate a biosynthetic model. Abstract-level evidence supports biosynthetic occurrence, not direct antibacterial targets or the absolute configuration of natural aurachin A. The RSC full-text request returned 403. |
| myxocoumarin | PMID:24367422; DOI:10.3762/bjoc.9.293; PMC3869339 complete main article including Experimental | supports | HPLC–UV–MS and peak/activity correlation identify known aurachins A and C in MYX-030 extracts during dereplication. The newly isolated compounds, extensive NMR, leaf-disk and fungal-growth experiments are myxocoumarins A/B, not aurachin A. This supports bounded occurrence in a different strain but does not assign aurachin A new MICs, absolute stereo or targets. |
| xrefs | Current source chemical crosswalks; ChEBI links and MetaCyc response | partial | CAS 108354-15-0 and Reaxys 19439470 are retained by ChEBI but their registry contents were not directly inspected. MetaCyc CPD-15911 redirects to an account-required page. PubChem matches the stored absolute graph but repeats rather than resolves its natural-product assignment. |
| chemistry | Independent RDKit calculations; 120-chemistry.json; actual focused schema/strict logs | supports | Both native encodings reproduce the complete key, formula, charge, masses and deterministic source mint. Actual schema and strict checks exit 0. These checks establish internal consistency, not the scope of natural-product stereochemistry or biological activity. |
| search | CultureBotAI/AntibioticMech; Initial ignored-inclusive search and 012-root-maintained-search.txt | context_only | Exact identifiers and labels identify native/source and readiness-queue context. No target-specific override was found in the named maintained search scope. This does not establish absence of literature or of files excluded from that search. |

## Limits And Additional Notes

- All four adopted abstracts were read. The 1987 production/activity and 2013 myxocoumarin main articles were fully read; the 2008 feeding and 2011 gene study were abstract-only. The 1987 original p263 tables were visually checked because extracted text interleaves columns.
- The 2021/2022 synthesis Introduction and early Results were accessible and read, including its explicit absolute-configuration statement; later page retrieval returned 403. The German repository PDF had a certificate error/timeout and was not read. Raw spectra and synthetic supplementary files were not reanalyzed.
- This bounded search confirms the native text/encoding mismatch but does not claim exhaustive absence of all later absolute-configuration work. Such a primary assignment should be assessed before choosing an exact enantiomer.
- CAS and Reaxys were not directly inspected; MetaCyc required an account. Natural-material optical rotation is not by itself an absolute-configuration assignment.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All captured input hashes were rechecked unchanged before writing the draft. No native record was edited.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T093306Z-aurachin-a-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Aurachin A: relative stereochemistry is over-specified in the exact encoded
  structure'
started_at: '2026-10-21T09:04:59Z'
finished_at: '2026-10-21T09:33:06Z'
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
summary: 'One confirmed major identity-scope conflict: the definition and systematic
  synonym explicitly describe relative configuration, while ordinary SMILES and Standard
  InChI fix two absolute stereocentres. Primary isolation and synthesis reports support
  relative-only natural-product assignment. The antibacterial role and strain occurrence
  are supported, but assay transfer must preserve this stereochemical boundary.'
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
  - path: data/antibiotics/antibacterial/aurachin-a.yaml
    sha256: 36d53d8e1149943ffb5673b1e67604687539be0393185177186aac7973125f1f
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
- target_id: CHEBI:90924
  path: data/antibiotics/antibacterial/aurachin-a.yaml
  label: aurachin A
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
  selection: Initially uncovered queue position120; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:90924
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:90924
  command: .venv/bin/python /private/tmp/am-review-session/focus011-root.py 120
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:90924
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/aurachin-a.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:90924
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/aurachin-a.yaml --out /private/tmp/am-review-session/120-strict.tsv
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
  - CHEBI:90924
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
  - CHEBI:90924
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
  - CHEBI:90924
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
  - CHEBI:90924
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
  - CHEBI:90924
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
  - CHEBI:90924
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
  - CHEBI:90924
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
  - CHEBI:90924
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
  - CHEBI:90924
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/aurachin-a.yaml
  locator: Entire YAML, including three seed/reseed events
  accessed_at: '2026-10-21T09:13:54Z'
  support: supports
  summary: Read the relative-configuration definition, two synonyms, four parents,
    antibacterial role, complete structure, three chemical xrefs and source mint.
    The systematic synonym starts rel-. SMILES fixes two carbon centres, and the InChI
    contains /t23-,25+/m1/s1. No primary mode, target, quantified activity, producer,
    clinical, graph, resistance or dataset block is present.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Row 2419; ChEBI extraction and seeding
  accessed_at: '2026-10-21T09:13:54Z'
  support: supports
  summary: Adopted source reproduces both the relative wording and absolute structure.
    Four PMID leads are present; they are not automatically promoted to claim-level
    evidence. No target-specific maintained override was found in the scoped ignored-inclusive
    search.
  snapshot_sha256: 74c0c47f7b1b699d2dae8cbd3cd9f88bdb45380dbdea0c291cede691ff31e9da
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:90924
  locator: Current entry, OLS parents and PubChem CID 118796887
  accessed_at: '2026-10-21T09:13:54Z'
  support: partial
  summary: Both current sources reproduce neutral C25H33NO3 and key ZEUIHPOXFICJIT-ZVWRMSPBSA-N.
    ChEBI retains relative configuration in its definition and rel- systematic name.
    Native parents quinoline N-oxide CHEBI:26508, tertiary alcohol CHEBI:26878, furoquinoline
    CHEBI:84586 and A-type aurachin CHEBI:90917 are appropriate. The retained antibacterial
    role is accepted source classification. Matching databases do not independently
    establish the natural absolute configuration.
  snapshot_sha256: 7613b62f0e71a8ab723c273a7b95a2b7789da3025860a234a133735b140fe2f5
- evidence_id: stereo
  kind: validation
  reference: Independent RDKit stereochemical interpretation
  locator: 120-chemistry.json; native SMILES and InChI
  accessed_at: '2026-10-21T09:13:54Z'
  support: refutes
  summary: Both encodings produce two assigned R/S carbon centres and the same full
    key. These ordinary absolute encodings are more specific than the relative pair
    in the definition and synonym. The remote E double bond is separately specified
    and is not implicated by this finding.
  snapshot_sha256: ee563773b04e93a6a3b296956e68138c8a66f9c26eef6596b3d35ebb36d19890
- evidence_id: isolation
  kind: primary_source
  reference: PMID:18989924
  locator: DOI:10.1021/np8003084; complete abstract
  accessed_at: '2026-10-21T09:13:54Z'
  support: partial
  summary: The original feeding study reports isolation of aurachins A–L from Stigmatella
    aurantiaca Sg a15 and explicitly identifies structures and relative configurations
    from spectroscopic, particularly NMR, evidence. Isotope-feeding results concern
    carbon/oxygen origins and interconversion; the abstract does not establish the
    absolute pair for natural aurachin A.
  snapshot_sha256: 28f45713fa3a81efb85d3724ee41b05221d7f4fc6e43d1fb933bac5f014f49d7
- evidence_id: synthesis
  kind: primary_source
  reference: DOI:10.1002/adsc.202100884
  locator: Stief and Speicher, online 2021 / issue 2022; publisher Introduction through
    early Results, especially absolute-configuration paragraph
  accessed_at: '2026-10-21T09:13:54Z'
  support: supports
  summary: The primary synthesis article explicitly states that natural aurachins
    A and H had not had their absolute configurations reported. It describes the earlier
    2017 aurachin A synthesis as using a racemic epoxide. This supports the native
    relative-versus-absolute conflict; a synthetic racemate does not prove that the
    natural product is racemic. Only the accessible Introduction and early Results
    were read; later publisher access returned 403.
- evidence_id: primary1987
  kind: primary_source
  reference: PMID:3106289
  locator: DOI:10.7164/antibiotics.40.258; complete eight-page paper; original p263
    Tables 3–4 visually inspected
  accessed_at: '2026-10-21T09:13:54Z'
  support: supports
  summary: 'The original production paper separates aurachins A–D and documents Sg
    a15 culture, acetone extraction and chromatographic purification. Table 4 gives
    aurachin A serial-dilution MICs in standard complex media: B. subtilis 5, S. aureus
    2.5, A. aurescens 0.19, B. ammoniagenes 0.39, C. fascians 1.56 and E. coli >50
    µg/mL. Table 4 does not itself list strain IDs; do not invent a join to every
    Table 3 disk-test strain. The 50 µg/mL yeast rows have incomplete inhibition with
    up to 25% residual turbidity. Table 3 uses 40 µg on 6-mm disks and is a different
    endpoint. Activity pertains to isolated natural material, not independently established
    absolute stereochemistry.'
  snapshot_sha256: 56573cace27c9b51785c05459dee5d45dcbe2f0b65b6a1416aa0dc3e46a7303b
- evidence_id: respiration
  kind: primary_source
  reference: DOI:10.7164/antibiotics.40.258
  locator: 1987 paper p264 Table 5 and Discussion
  accessed_at: '2026-10-21T09:13:54Z'
  support: supports
  summary: Aurachin A inhibits NADH oxidation in beef-heart submitochondrial particles
    at reported 50%-inhibition concentration 71 nM. The authors explicitly leave the
    exact mechanism and bacterial inhibitory action unresolved. This host mitochondrial
    mixture assay is not a bacterial cytochrome-bd binding experiment; later aurachin
    D or analog structures must not transfer.
  snapshot_sha256: 56573cace27c9b51785c05459dee5d45dcbe2f0b65b6a1416aa0dc3e46a7303b
- evidence_id: biosynthesis
  kind: primary_source
  reference: PMID:21979787
  locator: DOI:10.1039/c1mb05328k; complete abstract
  accessed_at: '2026-10-21T09:13:54Z'
  support: partial
  summary: Inactivation mutants in Sg a15 identify tailoring functions in a split
    aurachin gene-cluster system and motivate a biosynthetic model. Abstract-level
    evidence supports biosynthetic occurrence, not direct antibacterial targets or
    the absolute configuration of natural aurachin A. The RSC full-text request returned
    403.
  snapshot_sha256: 28f45713fa3a81efb85d3724ee41b05221d7f4fc6e43d1fb933bac5f014f49d7
- evidence_id: myxocoumarin
  kind: primary_source
  reference: PMID:24367422
  locator: DOI:10.3762/bjoc.9.293; PMC3869339 complete main article including Experimental
  accessed_at: '2026-10-21T09:13:54Z'
  support: supports
  summary: HPLC–UV–MS and peak/activity correlation identify known aurachins A and
    C in MYX-030 extracts during dereplication. The newly isolated compounds, extensive
    NMR, leaf-disk and fungal-growth experiments are myxocoumarins A/B, not aurachin
    A. This supports bounded occurrence in a different strain but does not assign
    aurachin A new MICs, absolute stereo or targets.
  snapshot_sha256: 7b019bddd6ada2c8ecaeb673c8b4b054cbcd97d19d299d03377516da428df3ca
- evidence_id: xrefs
  kind: database
  reference: Current source chemical crosswalks
  locator: ChEBI links and MetaCyc response
  accessed_at: '2026-10-21T09:13:54Z'
  support: partial
  summary: CAS 108354-15-0 and Reaxys 19439470 are retained by ChEBI but their registry
    contents were not directly inspected. MetaCyc CPD-15911 redirects to an account-required
    page. PubChem matches the stored absolute graph but repeats rather than resolves
    its natural-product assignment.
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit calculations
  locator: 120-chemistry.json; actual focused schema/strict logs
  accessed_at: '2026-10-21T09:13:54Z'
  support: supports
  summary: Both native encodings reproduce the complete key, formula, charge, masses
    and deterministic source mint. Actual schema and strict checks exit 0. These checks
    establish internal consistency, not the scope of natural-product stereochemistry
    or biological activity.
  snapshot_sha256: ee563773b04e93a6a3b296956e68138c8a66f9c26eef6596b3d35ebb36d19890
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: Initial ignored-inclusive search and 012-root-maintained-search.txt
  accessed_at: '2026-10-21T09:13:54Z'
  support: context_only
  summary: Exact identifiers and labels identify native/source and readiness-queue
    context. No target-specific override was found in the named maintained search
    scope. This does not establish absence of literature or of files excluded from
    that search.
  search_scope: rg --no-ignore --hidden across curation, conf, scripts, src and data/raw;
    exact names, ChEBI IDs and full-key stems; excluded .git, .venv and .obo/.jsonl/.html
    files in the bounded maintained pass. Initial prepare search also included ignored
    files. Free official database, Europe PMC and primary publisher searches.
  snapshot_sha256: 80838d5ef4c016780141b1f7ed126dd26d66a75824e8c6e38a1070f856bd652b
assessments:
- assessment_id: schema
  area: schema
  topic: Internal validation and native status
  outcome: supported
  summary: Focused checks pass; native SEEDED status and source history are unchanged.
    Review coverage does not promote native status.
  target_ids:
  - CHEBI:90924
  evidence_ids:
  - chemistry
  - native
- assessment_id: identity
  area: identity
  topic: Relative versus absolute stereochemical scope
  outcome: concern
  summary: Ordinary structures fix an absolute pair despite the native rel- wording
    and primary relative-only assignment. Source agreement does not repair this semantic
    conflict.
  target_ids:
  - CHEBI:90924
  evidence_ids:
  - native
  - identity
  - stereo
  - isolation
  - synthesis
- assessment_id: classification
  area: grounding
  topic: Chemical parents and antibacterial role
  outcome: supported
  summary: Structural parents fit the molecular scaffold and original natural-material
    assays support antibacterial classification.
  target_ids:
  - CHEBI:90924
  evidence_ids:
  - identity
  - primary1987
- assessment_id: activity
  area: evidence
  topic: Original antibacterial and host respiration experiments
  outcome: supported
  summary: Primary growth evidence exists, but numeric activity must retain preparation,
    assay and strain limits. Host mitochondrial respiration is not proof of a direct
    bacterial target.
  target_ids:
  - CHEBI:90924
  evidence_ids:
  - primary1987
  - respiration
- assessment_id: producer
  area: evidence
  topic: Sg a15 and MYX-030 occurrence
  outcome: supported
  summary: The original production and feeding studies support Sg a15 wording. MYX-030
    dereplication is distinct and does not supply aurachin A stereochemical proof.
  target_ids:
  - CHEBI:90924
  evidence_ids:
  - primary1987
  - isolation
  - biosynthesis
  - myxocoumarin
- assessment_id: optional
  area: completeness
  topic: Mechanism, resistance, clinical and omics enrichment
  outcome: unknown
  summary: Optional fields are absent without a schema defect. No native gene/protein/pathway
    or transcriptomic claim triggers an organism-specific adapter. Literature biosynthetic
    genes and aurachin D targets are not native aurachin A mechanism assertions.
  target_ids:
  - CHEBI:90924
  evidence_ids:
  - native
  - biosynthesis
  - respiration
findings:
- finding_id: F1
  issue_key: aurachin-a-relative-configuration-absolute-encoding
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Resolve the over-specified absolute stereochemistry
  description: The relative-configuration natural-product entity and rel- synonym
    are represented by an ordinary absolute SMILES/InChI pair. The primary assignment
    and accessible later synthesis discussion do not justify choosing that absolute
    pair. This is a reproducible source identity-scope inconsistency, not proof that
    the opposite enantiomer is correct or that the natural sample is racemic.
  target_ids:
  - CHEBI:90924
  field_paths:
  - chemical_structure
  - synonyms
  - definition
  - grounding_status
  evidence_ids:
  - native
  - identity
  - stereo
  - isolation
  - synthesis
  rule_id: 'native-review-checklist: Identity, Equivalence, Evidence and Completeness'
  native_severity: major
  normalization_reason: The relative-configuration natural-product entity and rel-
    synonym are represented by an ordinary absolute SMILES/InChI pair. The primary
    assignment and accessible later synthesis discussion do not justify choosing that
    absolute pair. This is a reproducible source identity-scope inconsistency, not
    proof that the opposite enantiomer is correct or that the natural sample is racemic.
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
- finding_id: F2
  issue_key: aurachin-a-primary-assay-scope-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Preserve original assay and material scope when enriching activity
  description: The 1987 paper provides isolated-natural-material growth and mitochondrial
    assays. These are useful optional annotations after the relative-versus-absolute
    identity issue is resolved, with distinct strain and endpoint limits.
  target_ids:
  - CHEBI:90924
  field_paths:
  - activity_spectrum
  - mode_of_action
  - molecular_targets
  - evidence
  evidence_ids:
  - primary1987
  - respiration
  - myxocoumarin
  rule_id: 'native-review-checklist: Identity, Equivalence, Evidence and Completeness'
  native_severity: informational
  normalization_reason: The 1987 paper provides isolated-natural-material growth and
    mitochondrial assays. These are useful optional annotations after the relative-versus-absolute
    identity issue is resolved, with distinct strain and endpoint limits.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/aurachin-a.yaml
    role: Curator-owned primary activity, evidence and discussions
actions:
- action_id: A1
  description: Adjudicate stereochemical scope through maintained source and exact-identity
    policy before assigning natural-material evidence.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:90924
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
  acceptance_checks:
  - Obtain primary evidence for the natural absolute configuration if an exact absolute
    structure is to be retained; matching secondary database keys do not suffice.
  - If only relative configuration is supported, use an explicitly supported representation/policy
    that preserves the relative pair and E alkene without silently choosing an enantiomer.
    If the exact-record model cannot express this scope, document a maintained exclusion
    or qualified treatment rather than inventing absolute assignment.
  - Do not call the natural material racemic on the basis of a racemic synthesis.
    Do not simply strip all stereo and erase known relative information.
  - Apply source extraction/seeding or supported maintained decisions so identity
    repairs reproduce; recheck every structure, synonym, full key, parent and xref
    and run required corpus gates.
- action_id: A2
  description: Optionally curate the original natural-material activity and respiration
    evidence after resolving identity scope.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:90924
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/aurachin-a.yaml
    role: Curator-owned primary activity, evidence and discussions
  acceptance_checks:
  - Keep Table 4 serial-dilution MIC separate from Table 3 disk zones; retain unspecified
    strains where Table 4 does not establish the exact isolate.
  - Preserve incomplete fungal inhibition qualifiers and E. coli >50 comparator. The
    71 nM beef-heart endpoint is host mitochondrial NADH oxidation, not a bacterial
    MIC or direct target binding.
  - Do not transfer myxocoumarin A assays, aurachin D cryo-EM targets, analog activities
    or docking-only proposals. Use claim-level primary evidence and the maintained
    curation workflow.
limitations:
- All four adopted abstracts were read. The 1987 production/activity and 2013 myxocoumarin
  main articles were fully read; the 2008 feeding and 2011 gene study were abstract-only.
  The 1987 original p263 tables were visually checked because extracted text interleaves
  columns.
- The 2021/2022 synthesis Introduction and early Results were accessible and read,
  including its explicit absolute-configuration statement; later page retrieval returned
  403. The German repository PDF had a certificate error/timeout and was not read.
  Raw spectra and synthetic supplementary files were not reanalyzed.
- This bounded search confirms the native text/encoding mismatch but does not claim
  exhaustive absence of all later absolute-configuration work. Such a primary assignment
  should be assessed before choosing an exact enantiomer.
- CAS and Reaxys were not directly inspected; MetaCyc required an account. Natural-material
  optical rotation is not by itself an absolute-configuration assignment.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All captured input hashes were rechecked unchanged before writing the draft. No
  native record was edited.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
