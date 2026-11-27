# BE-24566B: correct a structural locant in the definition and preserve stereochemical evidence limits

- Review: 20261021T101621Z-be-24566b-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:38:20Z
- Finished UTC: 2026-10-21T10:16:21Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Native chemistry agrees at its represented, stereochemically unspecified level with official sources and the original connectivity. The definition says methyl positions1 and4 while its own systematic name and scaffold place them at1 and6, a bounded source-owned wording defect. Original fermentation and antibacterial evidence is available, but enantiomers, racemic synthesis and chlorinated congeners must remain separate.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position150; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65474 | data/antibiotics/antibacterial/be-24566b.yaml | generated | BE-24566B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:65474 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:65474 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:65474 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:65474 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65474 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65474 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65474 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65474 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65474 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65474 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65474 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65474 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Source generation, ownership and history

provenance: supported. Targets: CHEBI:65474.

The adopted row and deterministic source handling reproduce the seeded fields. All captured inputs remain unchanged; this review does not promote native status.

### Focused gates

schema: supported. Targets: CHEBI:65474.

Native schema, strict and independent chemistry checks pass. Shared corpus verification is reported separately.

### Represented connectivity and stereo scope

identity: supported. Targets: CHEBI:65474.

Internal chemistry and independent sources agree at the explicitly unassigned two-centre level. Enantiomer and racemic literature remain distinct.

### Methyl substituent locant

identity: concern. Targets: CHEBI:65474.

The1-and4 prose conflicts with the1,6,9,9 systematic name for the same named skeleton. The verified native graph should be preserved while correcting the source-owned locant.

### Producer and antibacterial inclusion

evidence: supported. Targets: CHEBI:65474.

Original culture isolation and separate purified-compound assays support producer wording and antibacterial roles. Moderate potency is qualitative, not a uniform threshold.

### Primary evidence, mechanism and biological scope

completeness: unknown. Targets: CHEBI:65474.

Exact primary producer/activity enrichment is possible. LXR, fatty-acid inhibition of a chlorinated congener, biosynthetic genes and racemic synthesis do not establish the native antibacterial target. Native has no protein/pathway assertion requiring a pre-web adapter query.

## Findings

### F1: Correct the definition’s methyl position4 to position6

minor / open / confirmed; issue key: be24566b-definition-methyl-locant.

The source-owned definition uses methyl positions1 and4, whereas its systematic synonym and represented scaffold specify1,6,9,9. Correct the bounded locant wording through maintained source generation; keep the corroborated chemical structure.

### F2: Add original activity and producer evidence with enantiomer and assay limits

informational / open / confirmed; issue key: be24566b-primary-producer-activity-and-stereo-enrichment.

Original1995 isolation and2016 production genetics can support optional native annotations. The2005 enantiomer/chlorinated-congener study and2020 racemic synthesis require separate identities and evidence scopes.

## Recommended Actions And Acceptance Checks

### A1

Make the structural prose agree with the verified graph.

- Correct to methyl groups at1 and6 and geminal methyls at9, or use a shorter unambiguous structural definition.
- Preserve original source attribution, formula, graph and explicitly unassigned stereo; do not introduce a natural enantiomer or racemate from name alone.
- Apply through upstream/adopted definition ownership or a documented narrow override, confirm reseeding retains the result, and run focused/shared gates.

### A2

Curate exact primary experiments after resolving remaining assay and stereochemical scope.

- Retain A24566/FERM BP3994 and FJS31-2 strain identifiers and distinguish cultured production from the organism originally isolated from lichen.
- Use the original Table3 exact strains/values and resolve missing medium/temperature before quantitative activity annotation.
- Inspect full2005 stereo/assay data before assigning enantiomer-specific potency, LXR binding or fatty-acid mechanism; do not transfer chlorinated-congener values.
- Do not create self-resistance from abxA annotation or a microbial target from biosynthetic deletion; no automatic REVIEWED promotion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/be-24566b.yaml; Entire YAML and all three seed events | supports | Read the exact ChEBI identity, definition, one systematic synonym, five parents, two roles, complete chemistry and sole Reaxys xref. Two potential carbon stereocentres are unspecified. No native mechanism, target, producer object, quantitative activity, resistance, clinical, graph or dataset claims. |
| source | data/raw/chebi_antimicrobials.tsv; 150-raw.json and maintained definition ownership | supports | The native source row and current ChEBI both contain the1-and4 methyl phrase, while the systematic name explicitly says1,6,9,9-tetramethyl for the same parent scaffold. This is inherited source wording, not a native curation edit. The extractor/seeder own reproducible correction. |
| identity | CHEBI:65474;PubChem exact-key lookup; Current full ChEBI entry, parents and PubChem structure | supports | Native neutral C27H24O7/MDUGEFRGUDVHQH-UHFFFAOYSA-N encodes four phenols, bridged oxygen rings, cyclic ketone and four methyl groups. Five broader chemical parents fit. Exact-key PubChem agrees at the unspecified two-centre level; this does not prove natural enantiomer identity or a racemate. Reaxys15840383 is current source mapping only. |
| original | PMID:8557611;DOI:10.7164/antibiotics.48.1506; 150-primary1995.pdf; all three pages read and visually inspected, including Figures1–3 and Tables1–3 | supports | Original work cultures lichen-isolate A24566, assigned to S.violaceusniger and deposited asFERM BP3994, and isolates209.6mg BE24566B from fermentation mycelia. NMR/MS and methylation/NOE work establish the bridged connectivity shown without absolute stereo labels. Formula isC27H24O7. Twofold dilution/5microlitre inoculation from10^6CFU/mL and18h incubation yield MIC1.56 for B.subtilisATCC6633 and S.aureusFDA209P,3.13 for S.aureusSmith and MRSA BB6152, in micrograms/mL. The inspected short report does not specify every assay-medium/temperature detail; do not invent them. |
| enantiomer | PMID:16180833;DOI:10.1021/np050176k; 150-adopted-abstracts.txt complete original abstract | partial | The paper explicitly identifies negative-ABX as an enantiomer of BE24566B, and separately studies negative bischloro-ABX. LXR binding values and predominant typeII fatty-acid-synthesis inhibition by the chlorinated compound must not transfer to BE24566B. The abstract reports antibacterial activity across three compounds but full per-compound tables, stereochemical assignment and Methods were not retrieved. |
| biosynthesis | PMID:27248985;DOI:10.3390/molecules21060711; 150-primary2016.xml; main Introduction, Results, Discussion and Methods | partial | Streptomyces sp.FJS31-2/CGMCC4.7321 yields chemically characterized BE24566B and distinct chlorinated zunyimycinA. Deleting abxp/abxk/abxs abolishes the assigned product peak, supporting biosynthesis. Gene annotations for regulation/resistance and putative halogenase function are not direct BE24566B antimicrobial targets or demonstrated self-resistance. Strain/extract activity does not assign every tested fungal/bacterial effect to pure BE24566B. Full absolute stereochemical equivalence requires care. |
| synthesis | PMID:31944523;DOI:10.1002/anie.201914657; 150-primary2020.xml full main text | partial | The synthetic study explicitly makes racemic ABX, verifies connectivity by NMR/MS and crystallography, and identifies BE24566B/L755805 names as background. A racemic synthetic sample is not automatically the exact naturally isolated enantiomer; synthetic-method scope does not supply new native antimicrobial mechanism. Supporting spectra and crystallographic file were not audited. |
| patent | patent:US5334613A; 150-patent.html abstract and claims | context_only | The patent names BE24566B, FERM BP3994 production and pharmaceutically acceptable salts. This is consistent historical context, but broad therapeutic claims are not independent human efficacy or clinical approval evidence. Patent drawings and full example/legal-history audit were not performed. |
| chemistry | Independent native SMILES/InChI, formula, mass, charge and source-mint checks; 150-chemistry.json and focused command logs | supports | Both native encodings independently reproduce the stored full key, formula, neutral single component and masses at stored precision. Mint agrees. Actual focused schema and strict commands exit 0; chemical consistency does not prove biological mechanism. |
| search | CultureBotAI/AntibioticMech and free primary literature; 150-local-hits.txt; initial inspection and adopted/discovery snapshots | context_only | Initial ignored-inclusive local source/ownership search and exact raw-row inspection were followed by current official chemical sources, all adopted citation records and available abstracts, and bounded primary follow-up. Discovery queries are capped and selected relevant papers were pursued; no exhaustive literature absence claim is made. |

## Limits And Additional Notes

- Both adopted citations were checked: the1995 original was read fully with all pages visually inspected; the2005 ACS study remains abstract-only. Later2016 and2020 main texts were read, but their supplementary raw spectra and absolute-stereo evidence were not independently audited.
- The represented structure leaves two centres unassigned. This is preserved as explicit identity granularity; no native racemate claim or forced absolute assignment is made.
- A hidden/ignored-inclusive exact name/key/BGC/anthrabenzoxocinone search in the captured maintained MIBiG inventory returned no matching row. That bounded local result does not imply absence from the live external MIBiG resource or literature.
- The2017 zunyimycin paper was a discovery lead only and was not used to transfer its congener activities. Reaxys was not independently queried; patent assessment is limited to abstract/claims.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 14 captured maintained inputs remain unchanged. No native record was edited. Empty optional fields are not automatically defects.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T101621Z-be-24566b-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'BE-24566B: correct a structural locant in the definition and preserve stereochemical
  evidence limits'
started_at: '2026-10-21T09:38:20Z'
finished_at: '2026-10-21T10:16:21Z'
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
summary: Native chemistry agrees at its represented, stereochemically unspecified
  level with official sources and the original connectivity. The definition says methyl
  positions1 and4 while its own systematic name and scaffold place them at1 and6,
  a bounded source-owned wording defect. Original fermentation and antibacterial evidence
  is available, but enantiomers, racemic synthesis and chlorinated congeners must
  remain separate.
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
  - path: data/antibiotics/antibacterial/be-24566b.yaml
    sha256: ec6871311f64bc123e27c5d5f3b7e503bd0b081e057509b3e8a82a9792d14b8a
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
  - path: data/raw/mibig_producers.tsv
    sha256: d55289619e77e035ed437d432dd692ab382f254c3841c9a314752ef22578a01b
    role: context
targets:
- target_id: CHEBI:65474
  path: data/antibiotics/antibacterial/be-24566b.yaml
  label: BE-24566B
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
  selection: Initially uncovered queue position150; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65474
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65474
  command: .venv/bin/python /private/tmp/am-review-session/focus014-root.py 150
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65474
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/be-24566b.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65474
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/be-24566b.yaml --out /private/tmp/am-review-session/150-strict.tsv
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
  - CHEBI:65474
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
  - CHEBI:65474
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
  - CHEBI:65474
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
  - CHEBI:65474
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
  - CHEBI:65474
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
  - CHEBI:65474
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
  - CHEBI:65474
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
  - CHEBI:65474
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
  - CHEBI:65474
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/be-24566b.yaml
  locator: Entire YAML and all three seed events
  accessed_at: '2026-10-21T09:49:53Z'
  support: supports
  summary: Read the exact ChEBI identity, definition, one systematic synonym, five
    parents, two roles, complete chemistry and sole Reaxys xref. Two potential carbon
    stereocentres are unspecified. No native mechanism, target, producer object, quantitative
    activity, resistance, clinical, graph or dataset claims.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: 150-raw.json and maintained definition ownership
  accessed_at: '2026-10-21T09:49:53Z'
  support: supports
  summary: The native source row and current ChEBI both contain the1-and4 methyl phrase,
    while the systematic name explicitly says1,6,9,9-tetramethyl for the same parent
    scaffold. This is inherited source wording, not a native curation edit. The extractor/seeder
    own reproducible correction.
  snapshot_sha256: d4e21715bb7d095d94fedd798f2935cd808b1e81f9bac7c230297fb39cec0355
- evidence_id: identity
  kind: database
  reference: CHEBI:65474;PubChem exact-key lookup
  locator: Current full ChEBI entry, parents and PubChem structure
  accessed_at: '2026-10-21T09:49:53Z'
  support: supports
  summary: Native neutral C27H24O7/MDUGEFRGUDVHQH-UHFFFAOYSA-N encodes four phenols,
    bridged oxygen rings, cyclic ketone and four methyl groups. Five broader chemical
    parents fit. Exact-key PubChem agrees at the unspecified two-centre level; this
    does not prove natural enantiomer identity or a racemate. Reaxys15840383 is current
    source mapping only.
  snapshot_sha256: 6820e6ecac237350fec8f124d34c9325317ca0b855eecd40f691b3a07659dc34
- evidence_id: original
  kind: primary_source
  reference: PMID:8557611;DOI:10.7164/antibiotics.48.1506
  locator: 150-primary1995.pdf; all three pages read and visually inspected, including
    Figures1–3 and Tables1–3
  accessed_at: '2026-10-21T09:49:53Z'
  support: supports
  summary: Original work cultures lichen-isolate A24566, assigned to S.violaceusniger
    and deposited asFERM BP3994, and isolates209.6mg BE24566B from fermentation mycelia.
    NMR/MS and methylation/NOE work establish the bridged connectivity shown without
    absolute stereo labels. Formula isC27H24O7. Twofold dilution/5microlitre inoculation
    from10^6CFU/mL and18h incubation yield MIC1.56 for B.subtilisATCC6633 and S.aureusFDA209P,3.13
    for S.aureusSmith and MRSA BB6152, in micrograms/mL. The inspected short report
    does not specify every assay-medium/temperature detail; do not invent them.
  snapshot_sha256: 73ccfea7e9ec8d7e226d0ed08d93c085b835d546621ca54d64f2aa10369d1b37
- evidence_id: enantiomer
  kind: primary_source
  reference: PMID:16180833;DOI:10.1021/np050176k
  locator: 150-adopted-abstracts.txt complete original abstract
  accessed_at: '2026-10-21T09:49:53Z'
  support: partial
  summary: The paper explicitly identifies negative-ABX as an enantiomer of BE24566B,
    and separately studies negative bischloro-ABX. LXR binding values and predominant
    typeII fatty-acid-synthesis inhibition by the chlorinated compound must not transfer
    to BE24566B. The abstract reports antibacterial activity across three compounds
    but full per-compound tables, stereochemical assignment and Methods were not retrieved.
  snapshot_sha256: 6354e116d496feb2d9935193bb4e30f6fe860c5a3b2d82c2d6043e13eda2b420
- evidence_id: biosynthesis
  kind: primary_source
  reference: PMID:27248985;DOI:10.3390/molecules21060711
  locator: 150-primary2016.xml; main Introduction, Results, Discussion and Methods
  accessed_at: '2026-10-21T09:49:53Z'
  support: partial
  summary: Streptomyces sp.FJS31-2/CGMCC4.7321 yields chemically characterized BE24566B
    and distinct chlorinated zunyimycinA. Deleting abxp/abxk/abxs abolishes the assigned
    product peak, supporting biosynthesis. Gene annotations for regulation/resistance
    and putative halogenase function are not direct BE24566B antimicrobial targets
    or demonstrated self-resistance. Strain/extract activity does not assign every
    tested fungal/bacterial effect to pure BE24566B. Full absolute stereochemical
    equivalence requires care.
  snapshot_sha256: 4a88d93fe4bae792c2f642d39ac2bfa81b0937efcc842097b0354d644193aaa3
- evidence_id: synthesis
  kind: primary_source
  reference: PMID:31944523;DOI:10.1002/anie.201914657
  locator: 150-primary2020.xml full main text
  accessed_at: '2026-10-21T09:49:53Z'
  support: partial
  summary: The synthetic study explicitly makes racemic ABX, verifies connectivity
    by NMR/MS and crystallography, and identifies BE24566B/L755805 names as background.
    A racemic synthetic sample is not automatically the exact naturally isolated enantiomer;
    synthetic-method scope does not supply new native antimicrobial mechanism. Supporting
    spectra and crystallographic file were not audited.
  snapshot_sha256: 065250a4a0913f9a386d027e5a252d8ebe6c06222cab9a9432a1f33d97018dc8
- evidence_id: patent
  kind: primary_source
  reference: patent:US5334613A
  locator: 150-patent.html abstract and claims
  accessed_at: '2026-10-21T09:49:53Z'
  support: context_only
  summary: The patent names BE24566B, FERM BP3994 production and pharmaceutically
    acceptable salts. This is consistent historical context, but broad therapeutic
    claims are not independent human efficacy or clinical approval evidence. Patent
    drawings and full example/legal-history audit were not performed.
  snapshot_sha256: 1bd155436de91298c77eb5d964defb4733e22a778d783cda596d57e9b0a2ec97
- evidence_id: chemistry
  kind: validation
  reference: Independent native SMILES/InChI, formula, mass, charge and source-mint
    checks
  locator: 150-chemistry.json and focused command logs
  accessed_at: '2026-10-21T09:49:53Z'
  support: supports
  summary: Both native encodings independently reproduce the stored full key, formula,
    neutral single component and masses at stored precision. Mint agrees. Actual focused
    schema and strict commands exit 0; chemical consistency does not prove biological
    mechanism.
  snapshot_sha256: b5394133ed7122fcb8020e8be9af7f123868c2a39c75a805eb4b7f2841c2dd67
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech and free primary literature
  locator: 150-local-hits.txt; initial inspection and adopted/discovery snapshots
  accessed_at: '2026-10-21T09:49:53Z'
  support: context_only
  summary: Initial ignored-inclusive local source/ownership search and exact raw-row
    inspection were followed by current official chemical sources, all adopted citation
    records and available abstracts, and bounded primary follow-up. Discovery queries
    are capped and selected relevant papers were pursued; no exhaustive literature
    absence claim is made.
  search_scope: rg --no-ignore --hidden in the isolated batch015 worktree excluding
    .git and .venv. Exact target identifier, name and slug; maintained raw inventories,
    config, extraction and generation context. Free public databases and original
    papers; no paid provider.
  snapshot_sha256: df30031e4fdfb7ea6688940ff11e34508613519d674f45a05be201b2c980a569
assessments:
- assessment_id: provenance
  area: provenance
  topic: Source generation, ownership and history
  outcome: supported
  summary: The adopted row and deterministic source handling reproduce the seeded
    fields. All captured inputs remain unchanged; this review does not promote native
    status.
  target_ids:
  - CHEBI:65474
  evidence_ids:
  - native
  - source
  - chemistry
- assessment_id: schema
  area: schema
  topic: Focused gates
  outcome: supported
  summary: Native schema, strict and independent chemistry checks pass. Shared corpus
    verification is reported separately.
  target_ids:
  - CHEBI:65474
  evidence_ids:
  - chemistry
- assessment_id: identity
  area: identity
  topic: Represented connectivity and stereo scope
  outcome: supported
  summary: Internal chemistry and independent sources agree at the explicitly unassigned
    two-centre level. Enantiomer and racemic literature remain distinct.
  target_ids:
  - CHEBI:65474
  evidence_ids:
  - identity
  - original
  - enantiomer
  - synthesis
  - chemistry
- assessment_id: definition
  area: identity
  topic: Methyl substituent locant
  outcome: concern
  summary: The1-and4 prose conflicts with the1,6,9,9 systematic name for the same
    named skeleton. The verified native graph should be preserved while correcting
    the source-owned locant.
  target_ids:
  - CHEBI:65474
  evidence_ids:
  - native
  - source
  - identity
  - original
- assessment_id: activity
  area: evidence
  topic: Producer and antibacterial inclusion
  outcome: supported
  summary: Original culture isolation and separate purified-compound assays support
    producer wording and antibacterial roles. Moderate potency is qualitative, not
    a uniform threshold.
  target_ids:
  - CHEBI:65474
  evidence_ids:
  - original
  - biosynthesis
- assessment_id: optional
  area: completeness
  topic: Primary evidence, mechanism and biological scope
  outcome: unknown
  summary: Exact primary producer/activity enrichment is possible. LXR, fatty-acid
    inhibition of a chlorinated congener, biosynthetic genes and racemic synthesis
    do not establish the native antibacterial target. Native has no protein/pathway
    assertion requiring a pre-web adapter query.
  target_ids:
  - CHEBI:65474
  evidence_ids:
  - enantiomer
  - biosynthesis
  - synthesis
  - native
findings:
- finding_id: F1
  issue_key: be24566b-definition-methyl-locant
  category: identity
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the definition’s methyl position4 to position6
  description: The source-owned definition uses methyl positions1 and4, whereas its
    systematic synonym and represented scaffold specify1,6,9,9. Correct the bounded
    locant wording through maintained source generation; keep the corroborated chemical
    structure.
  target_ids:
  - CHEBI:65474
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - native
  - source
  - identity
  - original
  rule_id: 'native-review-checklist: exact identity and claim-level experimental scope'
  native_severity: minor
  normalization_reason: The source-owned definition uses methyl positions1 and4, whereas
    its systematic synonym and represented scaffold specify1,6,9,9. Correct the bounded
    locant wording through maintained source generation; keep the corroborated chemical
    structure.
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
  issue_key: be24566b-primary-producer-activity-and-stereo-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Add original activity and producer evidence with enantiomer and assay limits
  description: Original1995 isolation and2016 production genetics can support optional
    native annotations. The2005 enantiomer/chlorinated-congener study and2020 racemic
    synthesis require separate identities and evidence scopes.
  target_ids:
  - CHEBI:65474
  field_paths:
  - evidence
  - producer_organisms
  - activity_spectrum
  - discussions
  evidence_ids:
  - original
  - enantiomer
  - biosynthesis
  - synthesis
  rule_id: 'native-review-checklist: exact identity and claim-level experimental scope'
  native_severity: informational
  normalization_reason: Original1995 isolation and2016 production genetics can support
    optional native annotations. The2005 enantiomer/chlorinated-congener study and2020
    racemic synthesis require separate identities and evidence scopes.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/be-24566b.yaml
    role: Curator-owned exact primary evidence and optional biological annotations
      through validated writer/history helpers
actions:
- action_id: A1
  description: Make the structural prose agree with the verified graph.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:65474
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
  - Correct to methyl groups at1 and6 and geminal methyls at9, or use a shorter unambiguous
    structural definition.
  - Preserve original source attribution, formula, graph and explicitly unassigned
    stereo; do not introduce a natural enantiomer or racemate from name alone.
  - Apply through upstream/adopted definition ownership or a documented narrow override,
    confirm reseeding retains the result, and run focused/shared gates.
- action_id: A2
  description: Curate exact primary experiments after resolving remaining assay and
    stereochemical scope.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:65474
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/be-24566b.yaml
    role: Curator-owned exact primary evidence and optional biological annotations
      through validated writer/history helpers
  acceptance_checks:
  - Retain A24566/FERM BP3994 and FJS31-2 strain identifiers and distinguish cultured
    production from the organism originally isolated from lichen.
  - Use the original Table3 exact strains/values and resolve missing medium/temperature
    before quantitative activity annotation.
  - Inspect full2005 stereo/assay data before assigning enantiomer-specific potency,
    LXR binding or fatty-acid mechanism; do not transfer chlorinated-congener values.
  - Do not create self-resistance from abxA annotation or a microbial target from
    biosynthetic deletion; no automatic REVIEWED promotion.
limitations:
- 'Both adopted citations were checked: the1995 original was read fully with all pages
  visually inspected; the2005 ACS study remains abstract-only. Later2016 and2020 main
  texts were read, but their supplementary raw spectra and absolute-stereo evidence
  were not independently audited.'
- The represented structure leaves two centres unassigned. This is preserved as explicit
  identity granularity; no native racemate claim or forced absolute assignment is
  made.
- A hidden/ignored-inclusive exact name/key/BGC/anthrabenzoxocinone search in the
  captured maintained MIBiG inventory returned no matching row. That bounded local
  result does not imply absence from the live external MIBiG resource or literature.
- The2017 zunyimycin paper was a discovery lead only and was not used to transfer
  its congener activities. Reaxys was not independently queried; patent assessment
  is limited to abstract/claims.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 14 captured maintained inputs remain unchanged. No native record was edited.
  Empty optional fields are not automatically defects.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://doi.org/10.7164/antibiotics.48.1506
- https://doi.org/10.1021/np050176k
- https://doi.org/10.3390/molecules21060711
```
