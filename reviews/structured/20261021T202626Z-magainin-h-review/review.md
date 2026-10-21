# Review of magainin H

- Review: 20261021T202626Z-magainin-h-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T20:11:22Z
- Finished UTC: 2026-10-21T20:26:26Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native 23-residue amidated peptide, including D-alanine at positions 9, 13 and 18, agrees with the adopted original and current PubChem. A minor definition correction should remove duplicated wording and describe the additional Ala8-to-Ser8 difference from the printed magainin B sequence. Activity remains endpoint-qualified: the original reports little or no H activity, whereas the inventor patent records weak partial bacterial growth inhibition.

## Scope And Provenance

Entire native record, sole adopted primary, both exact identifiers, peptide class, source concept and all three history events; independent peptide assembly, original page scans, current authorities and original synthesis patent.

Selection: Initially uncovered queue position 627; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-4e94f7ae64 | data/antibiotics/antibacterial/magainin-h.yaml | generated | magainin H |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-4e94f7ae64 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-4e94f7ae64 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-4e94f7ae64 | Actual focused execution exited 0. |
| sequence-comparison | passed | False | antibioticmech:aro-4e94f7ae64 | Actual scratch helper exited 0 from 063. |
| tautomer-normalization | passed | False | antibioticmech:aro-4e94f7ae64 | Actual scratch helper exited 0 from 063. |
| source-ledger | passed | False | antibioticmech:aro-4e94f7ae64 | Actual scratch helper exited 0 from 063. |
| Authoritative full QC | failed | True | antibioticmech:aro-4e94f7ae64 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-4e94f7ae64 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-4e94f7ae64 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-4e94f7ae64 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-4e94f7ae64 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-4e94f7ae64 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-4e94f7ae64 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-4e94f7ae64 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-4e94f7ae64 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact H sequence and stereochemistry

identity: supported. Targets: antibioticmech:aro-4e94f7ae64.

Independent peptide assembly, the original sequence and patent agree with native H, including its 23 residues, C-terminal amide, Ser8 and D-Ala9/13/18.

### Encoding and mass consistency

representation: supported. Targets: antibioticmech:aro-4e94f7ae64.

Native encodings, formula, charge, masses and current PubChem agree. The raw InChI tautomer difference is resolved without stereochemical changes.

### Comparative definition accuracy

evidence: concern. Targets: antibioticmech:aro-4e94f7ae64.

The duplicated is is should be corrected, and the B comparison should include Ala8-to-Ser8 rather than describe only D substitutions. This does not undermine the correct H graph.

### Exact identifiers and broader peptide parent

grounding: supported. Targets: antibioticmech:aro-4e94f7ae64.

Both exact identifiers resolve to the same H graph; ARO:3000053 is a broader structural class.

### Antibacterial filing and exact assay scope

evidence: unknown. Targets: antibioticmech:aro-4e94f7ae64.

The original calls H inactive, while the patent distinguishes weak 50% growth inhibition from above-range complete inhibition. This limited positive signal does not justify a universal absence claim or forced classification removal. No direct H protein target is established.

### Source ownership and history

provenance: supported. Targets: antibioticmech:aro-4e94f7ae64.

The adopted ARO/PubChem rows reproduce native H; its mint is correct and all three history events are intact. Definition correction belongs in the maintained CARD/ARO source lane.

### Whole-record and adopted-reference coverage

completeness: supported. Targets: antibioticmech:aro-4e94f7ae64.

Every native field and sole adopted PMID were assessed. No bacterial gene/protein/pathway adapter applies to this sequence and protozoal physical-injury review. Optional enrichment is separate from the bounded definition correction.

## Findings

### F1: The definition omits one B-to-H residue difference and duplicates is

minor / open / confirmed; issue key: magainin-h-definition-comparison-and-duplicated-word.

The native H graph agrees with the original. Its comparative prose, however, omits the Ala8-to-Ser8 difference between the printed B and H sequences and begins is is. H specifically substitutes D-Ala at positions 9, 13 and 18; Ala15 remains L. Correcting the definition is a bounded wording and sequence-description repair, not a reason to replace the graph.

## Recommended Actions And Acceptance Checks

### A1

Correct the maintained source definition to remove is is and describe H as the 23-residue C-terminal amide with Ser8 and D-Ala9/13/18. If retaining a comparison with the printed B sequence, include Ala8-to-Ser8; alternatively use the explicitly identified all-L Ser8 comparator F. Preserve the supported H structure and exact identifiers. Regenerate only in a separately authorized curation task.

- Definition matches the original printed H sequence and does not imply D-Ala15 or a change at isoleucine centres.
- The Ala8-to-Ser8 distinction is included if B remains the comparator; duplicated wording is removed.
- The existing H graph, formula, exact identifiers and configured stereochemistry remain supported by independent construction.
- Separately authorized just seed-canary ARO:3003570 reproduces the definition; schema, strict, term/reference/history and corpus gates pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/magainin-h.yaml; Entire native; 627-inspect.json and 627-source-rows.json | supports | SEEDED/MINTED ARO-derived H record contains one definition, one peptide parent/class, two xrefs, one source concept and three seed events. No separate structured mechanism, target, resistance, activity, producer, clinical, dataset or causal-graph objects occur. Sixteen captured inputs preserve all thirteen original hashes. |
| chemical | Native H and PubChem CID16132431; 627-chemistry.json; 627-sequence-check.json; 627-normalization-diagnostic.json | supports | Native and current PubChem give OUWDLUAYXCGSSS-KIKDIOEMSA-N, C116H185N31O28S and charge 0. Independent construction of the printed 23-residue amidated H sequence with D-Ala9/13/18 matches reciprocally with chirality. All 23 configured centres agree. The raw InChI mismatch resolves after 24 local imidic-acid-to-amide transfers without changing tetrahedral tags. |
| primary-sequence | PMID:2285300; DOI:10.1128/aac.34.9.1824; actual printed page 1824 peptide sequences and legend; 626-1990-p1824-hires.png | partial | The original H sequence has Ser8 and D-Ala at positions 9, 13 and 18, with Ala15 remaining L and the C terminus amidated. Native H agrees. The same page prints B with Ala8, so the B-to-H change includes Ala8-to-Ser8 as well as the three D substitutions; the native comparative definition omits that difference. |
| patent-sequence | https://patents.google.com/patent/US5221732A/en; Original patent Table 1 and claim 12, actual pages viewed; synthesis and purification description | supports | The inventor patent independently prints the same H sequence and distinguishes the all-L Ser8 analogue F from B. H identity and its C-terminal amide are supported; D substitutions do not imply inversion of Ala15 or either isoleucine side-chain centre. |
| activity | PMID:2285300; All original pages 1824–1826; methods, results, discussion and Figure 1 caption | partial | H causes no reported B. hominis injury at 500 micrograms/mL for 2 h and no apparent E. histolytica injury at that concentration; slight T. cruzi injury leaves resistant clumps. These morphology/motility and membrane-injury observations are not MICs, complete killing or direct target-binding assays. The paper calls H bacterially inactive. Figure 1 concerns B, and B/G membrane conclusions are not established for H. |
| patent-activity | https://patents.google.com/patent/US5221732A/en; Original Table 3, actual 627-patent-table3.png; bacterial assay methods and surrounding no-activity prose | partial | H shows 50% growth inhibition at 70 micrograms/mL for E. coli ATCC25922 and at 100 for K. pneumoniae ATCC13883, P. aeruginosa ATCC27853 and S. agalactiae ATCC12386. Complete inhibition is above 100 for all seven strains; the other three also exceed 100 for 50% inhibition. Thus the general no-activity prose does not erase weak partial growth inhibition. No clinical susceptibility category or modern standardized MIC is inferred. |
| authorities | ARO:3003570; ARO:3000053; pubchem.compound:16132431; 627-current-aro-blocks.txt from current official 620-current-aro.obo; 627-pubchem.json and 627-pubchem-synonyms.json | partial | Current ARO resolves and repeats the source definition and exact PubChem mapping. Current PubChem matches the independently assembled H graph. The peptide-antibiotic parent is broader and structurally applicable; registry placement alone does not resolve the limited antibacterial assay scope. |
| discovery | Exact magainin H public discovery and maintained source search; 627-discovery.json; 626-1988-abstract.json; 627-source-audit.json | supports | All four exact-phrase discovery titles and complete abstracts were read. Magainin-H2 simulation is not automatically exact H, and two reviews do not add direct original evidence. The 1988 synthesis abstract was read; public full-text Wiley routes returned 403. The complete adopted 1990 original and inventor patent were inspected. |

## Limits And Additional Notes

- The original 1988 synthesis full text remains inaccessible after public Wiley 403 responses. The complete adopted 1990 article and original inventor patent supply directly inspected H sequence and assay evidence.
- Weak partial bacterial growth inhibition in the patent and above-range complete inhibition remain separate endpoints. General inactivity prose is not interpreted as universal absence of antibacterial effects; no clinical susceptibility threshold or standardized MIC is inferred.
- B/G membrane-injury evidence and magainin-H2 simulations do not establish a direct H mechanism. Figure 1 in the adopted article is B-specific; no H image quantification was performed.
- No named bacterial gene/protein/pathway, resistance determinant or expression dataset occurs in the native; iModulonDB is not applicable to this scoped follow-up.
- The required shared full-QC gate retains the established SciPy import failure. Focused checks and draft-contract success do not substitute for separately recorded shared corpus, term, reference and history gates.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All thirteen original hashes were preserved; sixteen actual inputs cover the ARO/PubChem owner chain. Native/source/history files and prior immutable reviews were not changed.
- Chemistry used the 019 interpreter against 063; native validators, source ledger and contract use 063. Shared primary snapshots retain their original 626 retrieval manifests and hashes.
- The imidic-acid/amide representation discrepancy is a resolved non-finding. The retained minor definition issue does not imply a different H structure or removal of its broader peptide parent.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T202626Z-magainin-h-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of magainin H
started_at: '2026-10-21T20:11:22Z'
finished_at: '2026-10-21T20:26:26Z'
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
summary: 'The native 23-residue amidated peptide, including D-alanine at positions
  9, 13 and 18, agrees with the adopted original and current PubChem. A minor definition
  correction should remove duplicated wording and describe the additional Ala8-to-Ser8
  difference from the printed magainin B sequence. Activity remains endpoint-qualified:
  the original reports little or no H activity, whereas the inventor patent records
  weak partial bacterial growth inhibition.'
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
  - path: data/antibiotics/antibacterial/magainin-h.yaml
    sha256: 6c540c27f05744dd3543f0d14e0dc1277cd59675fd1bdfb1268af05e721b773d
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
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
targets:
- target_id: antibioticmech:aro-4e94f7ae64
  path: data/antibiotics/antibacterial/magainin-h.yaml
  label: magainin H
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted exact ARO identity, definition, class and citation lead
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact peptide chemical encoding
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: CARD/ARO inventory extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Source classification policy
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
scope:
  description: Entire native record, sole adopted primary, both exact identifiers,
    peptide class, source concept and all three history events; independent peptide
    assembly, original page scans, current authorities and original synthesis patent.
  selection: Initially uncovered queue position 627; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-4e94f7ae64
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-4e94f7ae64
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    627
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-4e94f7ae64
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/magainin-h.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-4e94f7ae64
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/magainin-h.yaml --out /private/tmp/am-review-session/627-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: sequence-comparison
  name: sequence-comparison
  status: passed
  required: false
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/627-sequence-check.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual scratch helper exited 0 from 063.
  target_ids:
  - antibioticmech:aro-4e94f7ae64
- check_id: tautomer-normalization
  name: tautomer-normalization
  status: passed
  required: false
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/627-normalization-diagnostic.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual scratch helper exited 0 from 063.
  target_ids:
  - antibioticmech:aro-4e94f7ae64
- check_id: source-ledger
  name: source-ledger
  status: passed
  required: false
  command: /private/tmp/antibioticmech-record-reviews-063/.venv/bin/python /private/tmp/am-review-session/627-ledger.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual scratch helper exited 0 from 063.
  target_ids:
  - antibioticmech:aro-4e94f7ae64
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-4e94f7ae64
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
  - antibioticmech:aro-4e94f7ae64
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
  - antibioticmech:aro-4e94f7ae64
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
  - antibioticmech:aro-4e94f7ae64
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
  - antibioticmech:aro-4e94f7ae64
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
  - antibioticmech:aro-4e94f7ae64
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
  - antibioticmech:aro-4e94f7ae64
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
  - antibioticmech:aro-4e94f7ae64
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
  - antibioticmech:aro-4e94f7ae64
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/magainin-h.yaml
  locator: Entire native; 627-inspect.json and 627-source-rows.json
  accessed_at: '2026-10-21T20:19:04Z'
  support: supports
  summary: SEEDED/MINTED ARO-derived H record contains one definition, one peptide
    parent/class, two xrefs, one source concept and three seed events. No separate
    structured mechanism, target, resistance, activity, producer, clinical, dataset
    or causal-graph objects occur. Sixteen captured inputs preserve all thirteen original
    hashes.
  snapshot_sha256: fb660e6ff69968c35c611bf8376b6eaace85655ec0a8c7d5d70d1cdee6162b50
- evidence_id: chemical
  kind: validation
  reference: Native H and PubChem CID16132431
  locator: 627-chemistry.json; 627-sequence-check.json; 627-normalization-diagnostic.json
  accessed_at: '2026-10-21T20:19:04Z'
  support: supports
  summary: Native and current PubChem give OUWDLUAYXCGSSS-KIKDIOEMSA-N, C116H185N31O28S
    and charge 0. Independent construction of the printed 23-residue amidated H sequence
    with D-Ala9/13/18 matches reciprocally with chirality. All 23 configured centres
    agree. The raw InChI mismatch resolves after 24 local imidic-acid-to-amide transfers
    without changing tetrahedral tags.
  snapshot_sha256: 5c668af69927ec35cc3538a926613afcf15d9e9215ff3ea135e9c7950ed58329
- evidence_id: primary-sequence
  kind: primary_source
  reference: PMID:2285300
  locator: DOI:10.1128/aac.34.9.1824; actual printed page 1824 peptide sequences and
    legend; 626-1990-p1824-hires.png
  accessed_at: '2026-10-21T20:19:04Z'
  support: partial
  summary: The original H sequence has Ser8 and D-Ala at positions 9, 13 and 18, with
    Ala15 remaining L and the C terminus amidated. Native H agrees. The same page
    prints B with Ala8, so the B-to-H change includes Ala8-to-Ser8 as well as the
    three D substitutions; the native comparative definition omits that difference.
  snapshot_sha256: 25cdf1ec797e7f173dfd0169377e3a400c7b23c63d1f081a8b031efceaffec84
- evidence_id: patent-sequence
  kind: primary_source
  reference: https://patents.google.com/patent/US5221732A/en
  locator: Original patent Table 1 and claim 12, actual pages viewed; synthesis and
    purification description
  accessed_at: '2026-10-21T20:19:04Z'
  support: supports
  summary: The inventor patent independently prints the same H sequence and distinguishes
    the all-L Ser8 analogue F from B. H identity and its C-terminal amide are supported;
    D substitutions do not imply inversion of Ala15 or either isoleucine side-chain
    centre.
  snapshot_sha256: b11506108b20c42700706e1f269707a7831df446edd3c478560c1cf37debd634
- evidence_id: activity
  kind: primary_source
  reference: PMID:2285300
  locator: All original pages 1824–1826; methods, results, discussion and Figure 1
    caption
  accessed_at: '2026-10-21T20:19:04Z'
  support: partial
  summary: H causes no reported B. hominis injury at 500 micrograms/mL for 2 h and
    no apparent E. histolytica injury at that concentration; slight T. cruzi injury
    leaves resistant clumps. These morphology/motility and membrane-injury observations
    are not MICs, complete killing or direct target-binding assays. The paper calls
    H bacterially inactive. Figure 1 concerns B, and B/G membrane conclusions are
    not established for H.
  snapshot_sha256: 25cdf1ec797e7f173dfd0169377e3a400c7b23c63d1f081a8b031efceaffec84
- evidence_id: patent-activity
  kind: primary_source
  reference: https://patents.google.com/patent/US5221732A/en
  locator: Original Table 3, actual 627-patent-table3.png; bacterial assay methods
    and surrounding no-activity prose
  accessed_at: '2026-10-21T20:19:04Z'
  support: partial
  summary: H shows 50% growth inhibition at 70 micrograms/mL for E. coli ATCC25922
    and at 100 for K. pneumoniae ATCC13883, P. aeruginosa ATCC27853 and S. agalactiae
    ATCC12386. Complete inhibition is above 100 for all seven strains; the other three
    also exceed 100 for 50% inhibition. Thus the general no-activity prose does not
    erase weak partial growth inhibition. No clinical susceptibility category or modern
    standardized MIC is inferred.
  snapshot_sha256: b11506108b20c42700706e1f269707a7831df446edd3c478560c1cf37debd634
- evidence_id: authorities
  kind: authority
  reference: ARO:3003570; ARO:3000053; pubchem.compound:16132431
  locator: 627-current-aro-blocks.txt from current official 620-current-aro.obo; 627-pubchem.json
    and 627-pubchem-synonyms.json
  accessed_at: '2026-10-21T20:19:04Z'
  support: partial
  summary: Current ARO resolves and repeats the source definition and exact PubChem
    mapping. Current PubChem matches the independently assembled H graph. The peptide-antibiotic
    parent is broader and structurally applicable; registry placement alone does not
    resolve the limited antibacterial assay scope.
  snapshot_sha256: fb660e6ff69968c35c611bf8376b6eaace85655ec0a8c7d5d70d1cdee6162b50
- evidence_id: discovery
  kind: search
  reference: Exact magainin H public discovery and maintained source search
  locator: 627-discovery.json; 626-1988-abstract.json; 627-source-audit.json
  accessed_at: '2026-10-21T20:19:04Z'
  support: supports
  summary: All four exact-phrase discovery titles and complete abstracts were read.
    Magainin-H2 simulation is not automatically exact H, and two reviews do not add
    direct original evidence. The 1988 synthesis abstract was read; public full-text
    Wiley routes returned 403. The complete adopted 1990 original and inventor patent
    were inspected.
  search_scope: Europe PMC exact phrase magainin H; public publisher/PMC and inventor
    patent routes; official PubChem exact CID and current ARO. Local rg --no-ignore
    --hidden across data/raw, curation, scripts and src for exact identifier, label
    and slug; ignored files included. No exhaustive literature absence claim.
  snapshot_sha256: fb660e6ff69968c35c611bf8376b6eaace85655ec0a8c7d5d70d1cdee6162b50
assessments:
- assessment_id: identity
  area: identity
  topic: Exact H sequence and stereochemistry
  outcome: supported
  summary: Independent peptide assembly, the original sequence and patent agree with
    native H, including its 23 residues, C-terminal amide, Ser8 and D-Ala9/13/18.
  target_ids:
  - antibioticmech:aro-4e94f7ae64
  evidence_ids:
  - chemical
  - primary-sequence
  - patent-sequence
- assessment_id: representation
  area: representation
  topic: Encoding and mass consistency
  outcome: supported
  summary: Native encodings, formula, charge, masses and current PubChem agree. The
    raw InChI tautomer difference is resolved without stereochemical changes.
  target_ids:
  - antibioticmech:aro-4e94f7ae64
  evidence_ids:
  - chemical
- assessment_id: definition
  area: evidence
  topic: Comparative definition accuracy
  outcome: concern
  summary: The duplicated is is should be corrected, and the B comparison should include
    Ala8-to-Ser8 rather than describe only D substitutions. This does not undermine
    the correct H graph.
  target_ids:
  - antibioticmech:aro-4e94f7ae64
  evidence_ids:
  - native
  - primary-sequence
  - patent-sequence
- assessment_id: grounding
  area: grounding
  topic: Exact identifiers and broader peptide parent
  outcome: supported
  summary: Both exact identifiers resolve to the same H graph; ARO:3000053 is a broader
    structural class.
  target_ids:
  - antibioticmech:aro-4e94f7ae64
  evidence_ids:
  - authorities
  - chemical
- assessment_id: activity
  area: evidence
  topic: Antibacterial filing and exact assay scope
  outcome: unknown
  summary: The original calls H inactive, while the patent distinguishes weak 50%
    growth inhibition from above-range complete inhibition. This limited positive
    signal does not justify a universal absence claim or forced classification removal.
    No direct H protein target is established.
  target_ids:
  - antibioticmech:aro-4e94f7ae64
  evidence_ids:
  - activity
  - patent-activity
  - authorities
- assessment_id: provenance
  area: provenance
  topic: Source ownership and history
  outcome: supported
  summary: The adopted ARO/PubChem rows reproduce native H; its mint is correct and
    all three history events are intact. Definition correction belongs in the maintained
    CARD/ARO source lane.
  target_ids:
  - antibioticmech:aro-4e94f7ae64
  evidence_ids:
  - native
  - chemical
  - discovery
- assessment_id: coverage
  area: completeness
  topic: Whole-record and adopted-reference coverage
  outcome: supported
  summary: Every native field and sole adopted PMID were assessed. No bacterial gene/protein/pathway
    adapter applies to this sequence and protozoal physical-injury review. Optional
    enrichment is separate from the bounded definition correction.
  target_ids:
  - antibioticmech:aro-4e94f7ae64
  evidence_ids:
  - native
  - discovery
  - activity
findings:
- finding_id: F1
  issue_key: magainin-h-definition-comparison-and-duplicated-word
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: The definition omits one B-to-H residue difference and duplicates is
  description: The native H graph agrees with the original. Its comparative prose,
    however, omits the Ala8-to-Ser8 difference between the printed B and H sequences
    and begins is is. H specifically substitutes D-Ala at positions 9, 13 and 18;
    Ala15 remains L. Correcting the definition is a bounded wording and sequence-description
    repair, not a reason to replace the graph.
  target_ids:
  - antibioticmech:aro-4e94f7ae64
  field_paths:
  - definition
  evidence_ids:
  - native
  - primary-sequence
  - patent-sequence
  rule_id: Definition must accurately describe the exact source sequence
  normalization_reason: Exact H identity is independently supported; the demonstrated
    issue is incomplete comparative wording and a duplicated word.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Exact H definition and citation
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: CARD/ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition emission
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained source-definition adjudication
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-4e94f7ae64
  description: Correct the maintained source definition to remove is is and describe
    H as the 23-residue C-terminal amide with Ser8 and D-Ala9/13/18. If retaining
    a comparison with the printed B sequence, include Ala8-to-Ser8; alternatively
    use the explicitly identified all-L Ser8 comparator F. Preserve the supported
    H structure and exact identifiers. Regenerate only in a separately authorized
    curation task.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Exact H definition and citation
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: CARD/ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition emission
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained source-definition adjudication
  generator: scripts/extract_source_inventory.py and scripts/seed_from_sources.py
    after source-definition adjudication
  acceptance_checks:
  - Definition matches the original printed H sequence and does not imply D-Ala15
    or a change at isoleucine centres.
  - The Ala8-to-Ser8 distinction is included if B remains the comparator; duplicated
    wording is removed.
  - The existing H graph, formula, exact identifiers and configured stereochemistry
    remain supported by independent construction.
  - Separately authorized just seed-canary ARO:3003570 reproduces the definition;
    schema, strict, term/reference/history and corpus gates pass.
limitations:
- The original 1988 synthesis full text remains inaccessible after public Wiley 403
  responses. The complete adopted 1990 article and original inventor patent supply
  directly inspected H sequence and assay evidence.
- Weak partial bacterial growth inhibition in the patent and above-range complete
  inhibition remain separate endpoints. General inactivity prose is not interpreted
  as universal absence of antibacterial effects; no clinical susceptibility threshold
  or standardized MIC is inferred.
- B/G membrane-injury evidence and magainin-H2 simulations do not establish a direct
  H mechanism. Figure 1 in the adopted article is B-specific; no H image quantification
  was performed.
- No named bacterial gene/protein/pathway, resistance determinant or expression dataset
  occurs in the native; iModulonDB is not applicable to this scoped follow-up.
- The required shared full-QC gate retains the established SciPy import failure. Focused
  checks and draft-contract success do not substitute for separately recorded shared
  corpus, term, reference and history gates.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All thirteen original hashes were preserved; sixteen actual inputs cover the ARO/PubChem
  owner chain. Native/source/history files and prior immutable reviews were not changed.
- Chemistry used the 019 interpreter against 063; native validators, source ledger
  and contract use 063. Shared primary snapshots retain their original 626 retrieval
  manifests and hashes.
- The imidic-acid/amide representation discrepancy is a resolved non-finding. The
  retained minor definition issue does not imply a different H structure or removal
  of its broader peptide parent.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
