# Flavocillin: theoretical patent does not establish the imported antibacterial role

- Review: 20261021T162901Z-flavocillin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T16:12:20Z
- Finished UTC: 2026-10-21T16:29:01Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The entire ChEBI-seeded record reproduces its maintained source and passes focused structural checks. The cited patent describes a proposed molecule and explicitly conditions medicinal use on future antibacterial testing; the bounded follow-up found computational docking, not verified antibacterial experiments. One major role-support finding and one informational stereochemical source question remain.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 444; one complete exact record. All thirteen original input hashes were verified before judgment and preserved; the actual ChEBI extraction and seeding owners were confirmed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:194484 | data/antibiotics/antibacterial/flavocillin.yaml | generated | flavocillin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema verification | passed | True | CHEBI:194484 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:194484 | Actual focused execution exited 0. |
| Focused chemistry verification | passed | False | CHEBI:194484 | Actual focused execution exited 0. |
| Current authority graph comparison and patent stereo diagnostic | passed | False | CHEBI:194484 | Native SMILES/InChI, current ChEBI molfile and name-resolved PubChem graph yield the native full key. A separately labelled manual transcription of three patent stereobonds resolves the additional C2 centre; it is not a proposed corpus replacement. |
| Authoritative full QC | failed | True | CHEBI:194484 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:194484 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:194484 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:194484 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:194484 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:194484 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:194484 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:194484 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:194484 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Native graph, authority grounding and stereochemical document scope

identity: supported. Targets: CHEBI:194484.

The native record accurately reproduces the current ChEBI structure and exact systematic names. All chemical properties and graph encodings agree. The original proposed drawing provides one additional stereocentre; that narrower depiction needs explicit source reconciliation without treating the broader graph as a demonstrated mixture.

### Imported antimicrobial and antibacterial roles

evidence: concern. Targets: CHEBI:194484.

The imported roles are correctly reproduced as source assertions, but their cited original is explicitly theoretical and conditions efficacy on future testing. The bounded later evidence inspected does not supply an exact-material antibacterial experiment. This is a material support problem for the unqualified activity assertion, not evidence that flavocillin is inactive.

### Mechanism and other optional biological objects

completeness: supported. Targets: CHEBI:194484.

No native protein, gene, pathway, regulator, stress-response or transcriptomics assertion triggers a structured adapter query. The speculative patent and abstract docking claims do not justify adding a microbial target, MIC, clinical statement or resistance mechanism. Missing optional biological fields are not separate defects.

### Reproducible source transfer and history

provenance: supported. Targets: CHEBI:194484.

All native fields, the actual maintained row, applicable extraction and seeding ownership, sole document reference and absence of adopted citation leads were audited. The issue lies in biological evidence depth, not fabricated provenance or a broken reference.

## Findings

### F1: Qualify the activity claim supported only by a theoretical patent

major / open / confirmed; issue key: flavocillin-theoretical-patent-antibacterial-role-support.

The imported antimicrobial and antibacterial roles are presented without an experimental-evidence qualification. The cited original patent explicitly describes a theoretical proposal and its amended claim makes efficacy contingent on future bacterial testing. The bounded inspected follow-up supplies docking context rather than verified exact-material activity. The current role is therefore not supported as an experimentally established antibacterial assertion by the inspected source chain. This does not prove inactivity or exclude the possibility of additional uninspected evidence.

### F2: Reconcile the patent’s additional stereocentre with the authority scope

informational / open / confirmed; issue key: flavocillin-patent-versus-authority-carboxyl-stereocentre.

Figure 2 assigns the carboxyl-bearing bicyclo C2 centre, whereas native/current ChEBI/PubChem leave that centre unspecified. The diagnostic drawing transcription gives 2S,5R,6R; native names assert only 5R,6R. The patent is a document reference, and no measured product identity has been established here, so this is a bounded source-identity follow-up rather than a confirmed wrong-isomer defect or grounds to infer a mixture.

## Recommended Actions And Acceptance Checks

### A1

Resolve and qualify the maintained flavocillin activity support before scientific sign-off.

- Seek an exact-material primary antibacterial experiment with identifiable synthesis/material, organism, assay and endpoint. Do not use docking, parent penicillin activity, separate flavonoid coadministration or patent claims alone as proof.
- If no adequate exact-material support is available, preserve the distinction between a source-reported theoretical role and experimentally established activity in a maintained decision or source qualification. Consider exclusion only through an explicit corpus-scope decision, not as a claim of proven inactivity.
- Regenerate from the maintained owners and run focused schema/strict, corpus reproduction and applicable source-scope checks without promoting the generated native record to REVIEWED.

### A2

Clarify whether CHEBI194484 intentionally denotes unspecified C2 geometry or the narrower proposed patent stereoisomer.

- Compare the original Figure 2 and any characterized exact material with the ChEBI structure and names. Preserve the 5R,6R agreement and the uncertainty about experimental material.
- If the maintained identity is revised, update names and all structure encodings together through the actual source/override pathway and verify the full key. Treat the diagnostic 2S,5R,6R key as a candidate drawing transcription, not an automatic replacement.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/flavocillin.yaml; Entire native YAML, including all names, structural fields, parents, roles, document reference, source concept and four curation events. | supports | The SEEDED, EXACT ChEBI record is filed ANTIBACTERIAL and carries antimicrobial-agent CHEBI33281 and antibacterial-agent CHEBI33282 roles. It asserts no mode of action, molecular target, numerical activity, resistance determinant, producer, clinical object, expression dataset or causal graph. Its only reference is the document cross-reference patent:WO2019155266; there are no adopted PubMed leads. Both exact systematic synonyms specify 5R,6R and leave the carboxyl-bearing bicyclo C2 centre unspecified. |
| owners | data/raw/chebi_antimicrobials.tsv:2868; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; curation/decisions.tsv; Complete exact source row and applicable ChEBI extraction, role inheritance, classification, source-mint and document-reference emission logic. | supports | The complete ChEBI row supplies all native identity, definition, synonyms, parents, roles and patent reference. Its citation and mechanism-role columns are empty. The extractor selects reviewed antimicrobial role edges and inherits ancestor roles; the seeder places the compound in the antibacterial filing class from those roles. The mint antibioticmech:chebi-3192cb728f reproduces. The exact source scan found no additional ARO, target/resistance, FDA, PubChem-enrichment or MIBiG row. The four source events describe initial seeding and reseeding, without scientific REVIEWED status. |
| identity | CHEBI:194484; https://www.ebi.ac.uk/chebi/backend/api/public/compound/194484/; PubChem:168007555; Entire official ChEBI identity response and molfile; current name-resolved PubChem properties; independent graph parsing. | supports | Current ChEBI reproduces the native partial-stereo graph, both systematic names, formula C24H20N2O6S, neutral charge, average mass 464.499 and monoisotopic mass 464.10421. Native SMILES and Standard InChI, current ChEBI molfile and PubChem168007555 all yield FBFNOKWBJGHOGZ-LROQTYINSA-N, with two R centres and one unassigned centre. PubChem is corroborative discovery evidence, not an exact cross-reference present in the native record. The unassigned centre does not establish a mixture or racemate. |
| groundings | CHEBI:140325; CHEBI:17334; CHEBI:22712; CHEBI:24043; CHEBI:33281; CHEBI:33282; Current official term names, definitions and applicable chemical/role relations. | supports | The structural parents denote secondary carboxamide, penicillin, benzenes and flavones and fit the represented scaffold. The two activity roles denote antimicrobial and antibacterial activity; ChEBI currently repeats the direct antibacterial claim. The native definition conveys the intended flavone-linked penam scaffold, while the exact names and graph explicitly represent a benzamido substituent. Current authority repetition establishes provenance, not experimental efficacy. |
| patent | patent:WO2019155266; https://patentimages.storage.googleapis.com/c2/5e/37/44371885423940/WO2019155266A1.pdf; All nine original scanned PDF pages visually read, including description, original claims, amended claims received 2 June 2019, drawing page and international search report. | refutes | The description explicitly attributes the proposal to theoretical studies. The proposed preparation leaves quantities and scales to future expert determination and says HPLC and carbon NMR should be used to establish product identity, without reporting measured yield, spectra or antibacterial tests. Amended claim 1 conditions medicinal use on later tests confirming which bacteria, if any, are affected. Thus the original is not primary experimental support for the imported activity roles. The unqualified promises about resistance and dual action are hypotheses, not measured resistance or mechanism evidence. The patent reference resolves correctly, but its presence does not validate those promises. The HTML transcription omits the amended claims; this conclusion uses the original PDF. |
| patent-stereo | patent:WO2019155266 Figure 2; 444-authority-chemistry.json; Original PDF page 8, drawing sheet 1/1, Figure 2; explicit three-bond coordinate transcription in 444-authority-check.py. | context_only | The proposed flavocillin drawing explicitly depicts the C6-amide bond toward the viewer, C5-H behind the plane and carboxyl-bearing C2-to-carboxyl bond behind the plane. Independent diagnostic transcription gives bicyclo 2S,5R,6R and key FBFNOKWBJGHOGZ-XQBPLPMBSA-N. This preserves the native 5R,6R centres but specifies the third centre that the native and current authority graph leave unresolved. This is a source-scope question requiring reconciliation, not evidence that a measured native material is the opposite isomer or that the unassigned graph represents a mixture. |
| patent-family | https://patents.google.com/patent/EP3752509A1/en; Complete available description and claims text, independently read after the original WO PDF. | context_only | The European family text likewise presents a theoretical synthesis proposal, unspecified quantities, prospective analytical identification and asserted future efficacy. It does not supply a reported assay or measured preparation that resolves the original activity-support question. Patent legal status and examiner background references are not used as scientific approval. |
| followup | DOI:10.32388/5LR8V1.3; Europe PMC PPR621945; Complete indexed original preprint abstract; full preprint access unsuccessful. | context_only | The sole exact title/abstract match describes docking to TrxR, OATP and metallo-beta-lactamase and proposes effects on beta-lactam susceptibility. The inspected abstract reports computational docking, not a bacterial growth assay, isolated-protein inhibition measurement or established whole-cell causality. Full text was not retrieved; this review does not assert that every uninspected section lacks experimental data. These claims are not present in the native record and are not imported as molecular targets. |
| background | PMID:25734256; DOI:10.1089/mdr.2014.0252; PMID:19241386; PMID:13430729; Complete indexed abstracts for the 2015 combination and 2009 physical-chemistry papers; metadata/title only for the 1957 penicillin V paper. | context_only | The search report cites the 2015 work as background: it tests separately coadministered named flavonoids and conventional antibiotics, not the covalent flavocillin structure. The 2009 paper studies lone-pair/aromatic interactions in proteins and models. The 1957 item concerns penicillin V. Those inspected scopes do not establish flavocillin efficacy. The patent also lists DOI10.1021/ja01562a063; its underlying text was not obtained, so no exact experimental claim is drawn from it. |
| search | 444-inclusive-hits.txt; 444-exact-literature.json; 444-fetch-results.json through 444-fetch3-results.json; Hidden- and ignored-inclusive local exact-term search and bounded exact-name public literature/patent-family follow-up. | context_only | The local search finds the exact maintained row, native YAML, PATHS, generated map entries and mechanism-readiness queue; it supplies no additional source-backed activity claim. The exact Europe PMC title/abstract query returns one docking preprint. Broader name search is noisy and was not treated as exact evidence. Within the inspected public sources no experiment establishes antibacterial activity of the exact proposed structure. This bounded result is not proof of universal inactivity or a claim that the molecule has never been synthesized anywhere. |
| checks | 444-focused-results.json; 444-chemistry.json; 444-authority-chemistry.json; Actual schema, strict, standalone chemistry and authority/stereo diagnostic executions; original input-hash preservation. | supports | All focused checks exit 0. Formula, mass, charge, source mint and native full key are internally consistent. Current authority graphs reproduce the same partial stereochemistry. These checks do not establish antibacterial efficacy or resolve whether the patent drawing should define the authority’s exact stereochemical scope. |

## Limits And Additional Notes

- The Qeios preprint’s complete indexed abstract was inspected, but public page and PDF requests returned 503. Its full methods, any supplementary data and exact docking input representation were not inspected; no absence claim is made about those unread sections.
- All nine original WO patent pages and the European description/claims text were read, but no independent synthesis, spectra, purity measurement or antibacterial assay of a physical flavocillin sample was obtained. Proposed drawings do not establish experimentally realized stereochemistry.
- The exact-name literature search is bounded and may miss unindexed work or alternative chemical naming. It supports a documented gap in the inspected source chain, not universal inactivity or proof that the molecule was never made.
- The imported definition uses the authority’s term nitrilo while the precise systematic names and graph specify benzamido connectivity. This review does not resolve that nomenclature wording beyond verifying the represented connectivity.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All thirteen original input hashes remain unchanged. No missing optional mechanism or activity field is independently classified as a defect.
- The Standard InChI parser exposes an amide/imidic-acid mobile-hydrogen representation on round-trip, but reproduces the same complete native key and formula. That normalization is not treated as a separate identity error.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T162901Z-flavocillin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Flavocillin: theoretical patent does not establish the imported antibacterial
  role'
started_at: '2026-10-21T16:12:20Z'
finished_at: '2026-10-21T16:29:01Z'
reviewer:
  identity: Codex review002 subagent
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
summary: The entire ChEBI-seeded record reproduces its maintained source and passes
  focused structural checks. The cited patent describes a proposed molecule and explicitly
  conditions medicinal use on future antibacterial testing; the bounded follow-up
  found computational docking, not verified antibacterial experiments. One major role-support
  finding and one informational stereochemical source question remain.
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
  - path: data/antibiotics/antibacterial/flavocillin.yaml
    sha256: 07ba2cf005fb557fd9033d7007646b0f5c6adfaad5b8b04c59c16eba1963ccf3
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
- target_id: CHEBI:194484
  path: data/antibiotics/antibacterial/flavocillin.yaml
  label: flavocillin
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
  selection: Queue position 444; one complete exact record. All thirteen original
    input hashes were verified before judgment and preserved; the actual ChEBI extraction
    and seeding owners were confirmed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:194484
checks:
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:194484
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/flavocillin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:194484
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/flavocillin.yaml --out /private/tmp/am-review-session/444-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:194484
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 444
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-chemistry
  name: Current authority graph comparison and patent stereo diagnostic
  status: passed
  required: false
  summary: Native SMILES/InChI, current ChEBI molfile and name-resolved PubChem graph
    yield the native full key. A separately labelled manual transcription of three
    patent stereobonds resolves the additional C2 centre; it is not a proposed corpus
    replacement.
  target_ids:
  - CHEBI:194484
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/444-authority-check.py
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
  - CHEBI:194484
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
  - CHEBI:194484
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
  - CHEBI:194484
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
  - CHEBI:194484
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
  - CHEBI:194484
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
  - CHEBI:194484
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
  - CHEBI:194484
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
  - CHEBI:194484
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
  - CHEBI:194484
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/flavocillin.yaml
  locator: Entire native YAML, including all names, structural fields, parents, roles,
    document reference, source concept and four curation events.
  accessed_at: '2026-10-21T16:22:12Z'
  support: supports
  summary: The SEEDED, EXACT ChEBI record is filed ANTIBACTERIAL and carries antimicrobial-agent
    CHEBI33281 and antibacterial-agent CHEBI33282 roles. It asserts no mode of action,
    molecular target, numerical activity, resistance determinant, producer, clinical
    object, expression dataset or causal graph. Its only reference is the document
    cross-reference patent:WO2019155266; there are no adopted PubMed leads. Both exact
    systematic synonyms specify 5R,6R and leave the carboxyl-bearing bicyclo C2 centre
    unspecified.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv:2868; conf/sources.yaml; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py; curation/decisions.tsv
  locator: Complete exact source row and applicable ChEBI extraction, role inheritance,
    classification, source-mint and document-reference emission logic.
  accessed_at: '2026-10-21T16:22:12Z'
  support: supports
  summary: The complete ChEBI row supplies all native identity, definition, synonyms,
    parents, roles and patent reference. Its citation and mechanism-role columns are
    empty. The extractor selects reviewed antimicrobial role edges and inherits ancestor
    roles; the seeder places the compound in the antibacterial filing class from those
    roles. The mint antibioticmech:chebi-3192cb728f reproduces. The exact source scan
    found no additional ARO, target/resistance, FDA, PubChem-enrichment or MIBiG row.
    The four source events describe initial seeding and reseeding, without scientific
    REVIEWED status.
  snapshot_sha256: d70f2f180fcdecc54564903b5d1568aa8ac2f892c9ad50ddba1a3c4a7344af50
- evidence_id: identity
  kind: authority
  reference: CHEBI:194484; https://www.ebi.ac.uk/chebi/backend/api/public/compound/194484/;
    PubChem:168007555
  locator: Entire official ChEBI identity response and molfile; current name-resolved
    PubChem properties; independent graph parsing.
  accessed_at: '2026-10-21T16:16:33Z'
  support: supports
  summary: Current ChEBI reproduces the native partial-stereo graph, both systematic
    names, formula C24H20N2O6S, neutral charge, average mass 464.499 and monoisotopic
    mass 464.10421. Native SMILES and Standard InChI, current ChEBI molfile and PubChem168007555
    all yield FBFNOKWBJGHOGZ-LROQTYINSA-N, with two R centres and one unassigned centre.
    PubChem is corroborative discovery evidence, not an exact cross-reference present
    in the native record. The unassigned centre does not establish a mixture or racemate.
  snapshot_sha256: 6f825e950456e18cdd46e7061a2a074351db7aa01eac1d154916da26f713b1b1
- evidence_id: groundings
  kind: authority
  reference: CHEBI:140325; CHEBI:17334; CHEBI:22712; CHEBI:24043; CHEBI:33281; CHEBI:33282
  locator: Current official term names, definitions and applicable chemical/role relations.
  accessed_at: '2026-10-21T16:16:34Z'
  support: supports
  summary: The structural parents denote secondary carboxamide, penicillin, benzenes
    and flavones and fit the represented scaffold. The two activity roles denote antimicrobial
    and antibacterial activity; ChEBI currently repeats the direct antibacterial claim.
    The native definition conveys the intended flavone-linked penam scaffold, while
    the exact names and graph explicitly represent a benzamido substituent. Current
    authority repetition establishes provenance, not experimental efficacy.
  snapshot_sha256: da5e4c1011949f2c38dc273d8cdb520c11a08a4673eb7ed63095ba751645785d
- evidence_id: patent
  kind: primary_source
  reference: patent:WO2019155266; https://patentimages.storage.googleapis.com/c2/5e/37/44371885423940/WO2019155266A1.pdf
  locator: All nine original scanned PDF pages visually read, including description,
    original claims, amended claims received 2 June 2019, drawing page and international
    search report.
  accessed_at: '2026-10-21T16:17:19Z'
  support: refutes
  summary: The description explicitly attributes the proposal to theoretical studies.
    The proposed preparation leaves quantities and scales to future expert determination
    and says HPLC and carbon NMR should be used to establish product identity, without
    reporting measured yield, spectra or antibacterial tests. Amended claim 1 conditions
    medicinal use on later tests confirming which bacteria, if any, are affected.
    Thus the original is not primary experimental support for the imported activity
    roles. The unqualified promises about resistance and dual action are hypotheses,
    not measured resistance or mechanism evidence. The patent reference resolves correctly,
    but its presence does not validate those promises. The HTML transcription omits
    the amended claims; this conclusion uses the original PDF.
  snapshot_sha256: dfbc7b5580af3e0daca6d6325d056f9a4c8e72ae865f78595a0dca3559450e2b
- evidence_id: patent-stereo
  kind: primary_source
  reference: patent:WO2019155266 Figure 2; 444-authority-chemistry.json
  locator: Original PDF page 8, drawing sheet 1/1, Figure 2; explicit three-bond coordinate
    transcription in 444-authority-check.py.
  accessed_at: '2026-10-21T16:22:12Z'
  support: context_only
  summary: The proposed flavocillin drawing explicitly depicts the C6-amide bond toward
    the viewer, C5-H behind the plane and carboxyl-bearing C2-to-carboxyl bond behind
    the plane. Independent diagnostic transcription gives bicyclo 2S,5R,6R and key
    FBFNOKWBJGHOGZ-XQBPLPMBSA-N. This preserves the native 5R,6R centres but specifies
    the third centre that the native and current authority graph leave unresolved.
    This is a source-scope question requiring reconciliation, not evidence that a
    measured native material is the opposite isomer or that the unassigned graph represents
    a mixture.
  snapshot_sha256: 27ba4d90c541b920e77738652941a013ae9f824b7bb2ff4d1becbe06fc85f761
- evidence_id: patent-family
  kind: primary_source
  reference: https://patents.google.com/patent/EP3752509A1/en
  locator: Complete available description and claims text, independently read after
    the original WO PDF.
  accessed_at: '2026-10-21T16:20:17Z'
  support: context_only
  summary: The European family text likewise presents a theoretical synthesis proposal,
    unspecified quantities, prospective analytical identification and asserted future
    efficacy. It does not supply a reported assay or measured preparation that resolves
    the original activity-support question. Patent legal status and examiner background
    references are not used as scientific approval.
  snapshot_sha256: 46eb9c93c638e45b366523b0e9f9ed8f24ca60e1daa42f4d513e93a5297a1553
- evidence_id: followup
  kind: primary_source
  reference: DOI:10.32388/5LR8V1.3; Europe PMC PPR621945
  locator: Complete indexed original preprint abstract; full preprint access unsuccessful.
  accessed_at: '2026-10-21T16:17:19Z'
  support: context_only
  summary: The sole exact title/abstract match describes docking to TrxR, OATP and
    metallo-beta-lactamase and proposes effects on beta-lactam susceptibility. The
    inspected abstract reports computational docking, not a bacterial growth assay,
    isolated-protein inhibition measurement or established whole-cell causality. Full
    text was not retrieved; this review does not assert that every uninspected section
    lacks experimental data. These claims are not present in the native record and
    are not imported as molecular targets.
  snapshot_sha256: 8107b873f31433babb45028d15223748446d19fe6db064cc9d5ee497bafe2b38
- evidence_id: background
  kind: database
  reference: PMID:25734256; DOI:10.1089/mdr.2014.0252; PMID:19241386; PMID:13430729
  locator: Complete indexed abstracts for the 2015 combination and 2009 physical-chemistry
    papers; metadata/title only for the 1957 penicillin V paper.
  accessed_at: '2026-10-21T16:17:19Z'
  support: context_only
  summary: 'The search report cites the 2015 work as background: it tests separately
    coadministered named flavonoids and conventional antibiotics, not the covalent
    flavocillin structure. The 2009 paper studies lone-pair/aromatic interactions
    in proteins and models. The 1957 item concerns penicillin V. Those inspected scopes
    do not establish flavocillin efficacy. The patent also lists DOI10.1021/ja01562a063;
    its underlying text was not obtained, so no exact experimental claim is drawn
    from it.'
  snapshot_sha256: 5defcc474ad831f5ca200329538ecfc590c487f46587d8926519d10a46cc5fb7
- evidence_id: search
  kind: search
  reference: 444-inclusive-hits.txt; 444-exact-literature.json; 444-fetch-results.json
    through 444-fetch3-results.json
  locator: Hidden- and ignored-inclusive local exact-term search and bounded exact-name
    public literature/patent-family follow-up.
  accessed_at: '2026-10-21T16:22:12Z'
  support: context_only
  summary: The local search finds the exact maintained row, native YAML, PATHS, generated
    map entries and mechanism-readiness queue; it supplies no additional source-backed
    activity claim. The exact Europe PMC title/abstract query returns one docking
    preprint. Broader name search is noisy and was not treated as exact evidence.
    Within the inspected public sources no experiment establishes antibacterial activity
    of the exact proposed structure. This bounded result is not proof of universal
    inactivity or a claim that the molecule has never been synthesized anywhere.
  search_scope: 2026-10-21; rg --no-ignore --hidden across data, curation, conf, scripts,
    src, docs, .claude, reviews and reports for CHEBI:194484, flavocillin, FBFNOKWBJGHOGZ,
    WO2019155266 and chebi-3192cb728f. Europe PMC TITLE_ABS:flavocillin OR TITLE_ABS:flavocilin,
    exact-name web follow-up, current ChEBI/PubChem and original WO/EP patent-family
    documents.
  snapshot_sha256: 8ab466100c3126824b492190fd108c392a7e331792a773fc2dc09323f8d3473b
- evidence_id: checks
  kind: validation
  reference: 444-focused-results.json; 444-chemistry.json; 444-authority-chemistry.json
  locator: Actual schema, strict, standalone chemistry and authority/stereo diagnostic
    executions; original input-hash preservation.
  accessed_at: '2026-10-21T16:22:12Z'
  support: supports
  summary: All focused checks exit 0. Formula, mass, charge, source mint and native
    full key are internally consistent. Current authority graphs reproduce the same
    partial stereochemistry. These checks do not establish antibacterial efficacy
    or resolve whether the patent drawing should define the authority’s exact stereochemical
    scope.
  snapshot_sha256: ca38f355b6306146de0471afcede0f1a1e9188ecaa114187abcbfa11fabcf87b
assessments:
- assessment_id: identity
  area: identity
  topic: Native graph, authority grounding and stereochemical document scope
  outcome: supported
  summary: The native record accurately reproduces the current ChEBI structure and
    exact systematic names. All chemical properties and graph encodings agree. The
    original proposed drawing provides one additional stereocentre; that narrower
    depiction needs explicit source reconciliation without treating the broader graph
    as a demonstrated mixture.
  target_ids:
  - CHEBI:194484
  evidence_ids:
  - native
  - identity
  - groundings
  - patent-stereo
  - checks
- assessment_id: activity
  area: evidence
  topic: Imported antimicrobial and antibacterial roles
  outcome: concern
  summary: The imported roles are correctly reproduced as source assertions, but their
    cited original is explicitly theoretical and conditions efficacy on future testing.
    The bounded later evidence inspected does not supply an exact-material antibacterial
    experiment. This is a material support problem for the unqualified activity assertion,
    not evidence that flavocillin is inactive.
  target_ids:
  - CHEBI:194484
  evidence_ids:
  - owners
  - groundings
  - patent
  - patent-family
  - followup
  - background
  - search
- assessment_id: completeness
  area: completeness
  topic: Mechanism and other optional biological objects
  outcome: supported
  summary: No native protein, gene, pathway, regulator, stress-response or transcriptomics
    assertion triggers a structured adapter query. The speculative patent and abstract
    docking claims do not justify adding a microbial target, MIC, clinical statement
    or resistance mechanism. Missing optional biological fields are not separate defects.
  target_ids:
  - CHEBI:194484
  evidence_ids:
  - native
  - patent
  - followup
- assessment_id: provenance
  area: provenance
  topic: Reproducible source transfer and history
  outcome: supported
  summary: All native fields, the actual maintained row, applicable extraction and
    seeding ownership, sole document reference and absence of adopted citation leads
    were audited. The issue lies in biological evidence depth, not fabricated provenance
    or a broken reference.
  target_ids:
  - CHEBI:194484
  evidence_ids:
  - native
  - owners
  - search
  - checks
findings:
- finding_id: F1
  issue_key: flavocillin-theoretical-patent-antibacterial-role-support
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Qualify the activity claim supported only by a theoretical patent
  description: The imported antimicrobial and antibacterial roles are presented without
    an experimental-evidence qualification. The cited original patent explicitly describes
    a theoretical proposal and its amended claim makes efficacy contingent on future
    bacterial testing. The bounded inspected follow-up supplies docking context rather
    than verified exact-material activity. The current role is therefore not supported
    as an experimentally established antibacterial assertion by the inspected source
    chain. This does not prove inactivity or exclude the possibility of additional
    uninspected evidence.
  target_ids:
  - CHEBI:194484
  field_paths:
  - activity_roles
  - antimicrobial_class
  evidence_ids:
  - owners
  - groundings
  - patent
  - patent-family
  - followup
  - background
  - search
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Maintained imported ChEBI identity and activity assertions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI role and structure extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible classification and record generation
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained scope or identity decision when required
  rule_id: Review skill claim-level evidence and scope rules; native correct-class
    and activity-role checklist
  native_severity: major
  normalization_reason: The finding concerns unsupported biological scope that determines
    record inclusion and filing, not merely a missing optional MIC field or an unavailable
    paper.
- finding_id: F2
  issue_key: flavocillin-patent-versus-authority-carboxyl-stereocentre
  category: identity
  severity: informational
  status: open
  certainty: confirmed
  title: Reconcile the patent’s additional stereocentre with the authority scope
  description: Figure 2 assigns the carboxyl-bearing bicyclo C2 centre, whereas native/current
    ChEBI/PubChem leave that centre unspecified. The diagnostic drawing transcription
    gives 2S,5R,6R; native names assert only 5R,6R. The patent is a document reference,
    and no measured product identity has been established here, so this is a bounded
    source-identity follow-up rather than a confirmed wrong-isomer defect or grounds
    to infer a mixture.
  target_ids:
  - CHEBI:194484
  field_paths:
  - chemical_structure
  - synonyms
  - document_xrefs
  evidence_ids:
  - native
  - identity
  - patent-stereo
  - checks
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Maintained imported ChEBI identity and activity assertions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI role and structure extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible classification and record generation
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained scope or identity decision when required
  rule_id: Exact-structure identity model and preservation of unresolved source scope
  native_severity: informational
  normalization_reason: Current authority and native graphs agree. The narrower proposed
    drawing merits reconciliation, but does not independently demonstrate that the
    source concept or native measured material has the wrong identity.
actions:
- action_id: A1
  description: Resolve and qualify the maintained flavocillin activity support before
    scientific sign-off.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:194484
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Maintained imported ChEBI identity and activity assertions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI role and structure extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible classification and record generation
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained scope or identity decision when required
  acceptance_checks:
  - Seek an exact-material primary antibacterial experiment with identifiable synthesis/material,
    organism, assay and endpoint. Do not use docking, parent penicillin activity,
    separate flavonoid coadministration or patent claims alone as proof.
  - If no adequate exact-material support is available, preserve the distinction between
    a source-reported theoretical role and experimentally established activity in
    a maintained decision or source qualification. Consider exclusion only through
    an explicit corpus-scope decision, not as a claim of proven inactivity.
  - Regenerate from the maintained owners and run focused schema/strict, corpus reproduction
    and applicable source-scope checks without promoting the generated native record
    to REVIEWED.
  generator: scripts/extract_source_inventory.py; scripts/seed_from_sources.py
- action_id: A2
  description: Clarify whether CHEBI194484 intentionally denotes unspecified C2 geometry
    or the narrower proposed patent stereoisomer.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:194484
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Maintained imported ChEBI identity and activity assertions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI role and structure extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible classification and record generation
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained scope or identity decision when required
  acceptance_checks:
  - Compare the original Figure 2 and any characterized exact material with the ChEBI
    structure and names. Preserve the 5R,6R agreement and the uncertainty about experimental
    material.
  - If the maintained identity is revised, update names and all structure encodings
    together through the actual source/override pathway and verify the full key. Treat
    the diagnostic 2S,5R,6R key as a candidate drawing transcription, not an automatic
    replacement.
  generator: scripts/extract_source_inventory.py; scripts/seed_from_sources.py
limitations:
- The Qeios preprint’s complete indexed abstract was inspected, but public page and
  PDF requests returned 503. Its full methods, any supplementary data and exact docking
  input representation were not inspected; no absence claim is made about those unread
  sections.
- All nine original WO patent pages and the European description/claims text were
  read, but no independent synthesis, spectra, purity measurement or antibacterial
  assay of a physical flavocillin sample was obtained. Proposed drawings do not establish
  experimentally realized stereochemistry.
- The exact-name literature search is bounded and may miss unindexed work or alternative
  chemical naming. It supports a documented gap in the inspected source chain, not
  universal inactivity or proof that the molecule was never made.
- The imported definition uses the authority’s term nitrilo while the precise systematic
  names and graph specify benzamido connectivity. This review does not resolve that
  nomenclature wording beyond verifying the represented connectivity.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All thirteen original input hashes remain unchanged. No missing optional mechanism
  or activity field is independently classified as a defect.
- The Standard InChI parser exposes an amide/imidic-acid mobile-hydrogen representation
  on round-trip, but reproduces the same complete native key and formula. That normalization
  is not treated as a separate identity error.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
