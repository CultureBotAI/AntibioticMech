# Review of fatsicarpain A

- Review: 20261021T161218Z-fatsicarpain-a-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T15:56:37Z
- Finished UTC: 2026-10-21T16:12:18Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Fatsicarpain A has consistent neutral C30H46O4 identity across seven chemical encodings and an independently reconstructed original crystal model. The original isolation abstract and spectral supplement support the exact compound and plant source. A later primary paper includes positive exact-parent antibacterial observations. Its HBV antigen results and cytotoxicity wording do not resolve selective antiviral support. The original main paper, its correction and direct Reaxys record remain inaccessible; no demonstrated native correction was established. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole SEEDED, EXACT fatsicarpain A record: structural definition, plant isolation, antibacterial and anti-HBV assertions, relative systematic synonym, two parents, two roles, entire chemical structure, Reaxys link, source concept and three histories.

Selection: Queue 433 in isolated batch 044. All actual ChEBI extraction and classification owners were already present in the preserved initial 13 inputs; their roles were made explicit in target ownership.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:69216 | data/antibiotics/antibacterial/fatsicarpain-a.yaml | generated | fatsicarpain A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native schema | passed | True | CHEBI:69216 | Exit 0. |
| Native strict terms | passed | True | CHEBI:69216 | Exit 0; no ERROR rows. |
| Native molecular consistency | passed | False | CHEBI:69216 | Neutral formula, masses, SMILES and InChI agree. |
| Independent authority graph comparison | passed | False | CHEBI:69216 | Seven encodings agree by full reciprocal stereochemical graph matching, including eight configured centers. |
| Original crystal-model comparison | passed | False | CHEBI:69216 | Original CIF fractional coordinates converted to Cartesian geometry; perceived graph and stereo match native. The imprecise Flack value does not independently establish absolute hand. |
| Whole source and reference ledger | passed | False | CHEBI:69216 | All 13 original hashes unchanged; source fields, roles, synonym, sole adopted PMID, parent comparator rows and three chronological histories reconciled. |
| Authoritative full QC | failed | True | CHEBI:69216 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:69216 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:69216 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:69216 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:69216 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:69216 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:69216 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:69216 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:69216 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral compound and relative geometry

identity: supported. Targets: CHEBI:69216.

Native and current authority graphs, original A drawing and deposited crystal model agree. No sibling, salt or hydroxy-position mismatch was established.

### Absolute versus relative stereochemical support

representation: unknown. Targets: CHEBI:69216.

The relative synonym is retained. The encoded hand matches the deposited model, but its imprecise Flack value and inaccessible main argument do not independently establish absolute configuration. No racemate inference or forced edit is justified.

### Parents and antimicrobial filing

grounding: supported. Targets: CHEBI:69216.

The two structural parents fit the graph; antibacterial activity is supported by exact-parent observations. Filing priority and retained role mappings match source owners.

### Plant-isolation statement

evidence: supported. Targets: CHEBI:69216.

The original abstract directly identifies leaves/twigs of Fatsia polycarpa. This is isolation context, not proof of a specific biosynthetic pathway or a separately asserted producer-strain object.

### Anti-HBV claim and selectivity

evidence: unknown. Targets: CHEBI:69216.

ChEBI explicitly supports the imported role, while inspected primary antigen/cytotoxicity results do not resolve selective antiviral evidence. Original and correction access are needed; no blanket no-activity conclusion is made.

### MIC, MBC and assay details

quantity: unknown. Targets: CHEBI:69216.

The positive A bacterial endpoints are distinct and retain their published units. Full strain/protocol details are deferred to the inaccessible original, so no native quantitative observation is proposed yet.

### Exact antimicrobial mechanism

evidence: unknown. Targets: CHEBI:69216.

The native asserts no molecular target. No primary A target mechanism was established in the inspected sources; neighboring host-signaling results cannot fill it. The structured adapter has no applicable native protein/gene/pathway query.

### Reaxys registry mapping

grounding: unknown. Targets: CHEBI:69216.

ChEBI attribution is verified, but the registry itself was inaccessible.

### Original published correction

scope: unknown. Targets: CHEBI:69216.

The correction exists, but its unknown content is not transferred into a structural or activity finding.

### Maintained fields and history

ownership: supported. Targets: CHEBI:69216.

All 13 unchanged initial inputs include actual owners; the sole adopted lead and all source-derived fields are accounted for.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/fatsicarpain-a.yaml; Entire native YAML | supports | The record denotes fatsicarpain A, with an explicitly relative systematic synonym and configured structure. It asserts antibacterial and anti-HBV activity in its definition/roles, but contains no exact protein target, quantitative MIC, clinical status or ProducerOrganism object. Three source-seeding events are retained. |
| chemistry | CHEBI:69216; PubChem CID53493446; 433-chebi.json/.mol;433-pubchem.json/.sdf;433-authority-chemistry.json | supports | Native SMILES/InChI, current ChEBI SMILES/molfile and public PubChem SMILES/InChI/SDF agree on neutral C30H46O4 and key ZMKQRHHJEZOFLT-KFYXPMKRSA-N. Full reciprocal atom mappings preserve all eight configured centers. PubChem was queried by exact key and is an independent comparison source, not a newly asserted native xref. Database concordance alone is not experimental proof. |
| terms | CHEBI:25872; CHEBI:35868; CHEBI:33282; CHEBI:64951; 433-chebi-25872/35868/33282/64951.json;433-chebi.json ontology relations | supports | Current terms resolve to pentacyclic triterpenoid, hydroxy monocarboxylic acid, antibacterial agent and anti-HBV agent. The exact current ChEBI entry retains the native definition, roles, relative synonym and Reaxys registry mapping. Antibacterial filing follows the maintained role precedence; it does not remove the separate antiviral role. This verifies ontology/source consistency, not antiviral selectivity. |
| adopted | PMID:21766884; DOI:10.1021/np2002435; 433-adopted-core.json complete original abstract | supports | The original names fatsicarpains A–G as compounds 1–7 isolated from leaves and twigs of Fatsia polycarpa. It explicitly reports crystallography of 1, 8, 9, so A has direct crystal-study support. Cytotoxic, HBV and antibacterial assays were evaluated in vitro, but the abstract does not give individual activity outcomes. |
| spectra | DOI:10.1021/np2002435.s004; 433-np2002435_si_004.pdf printed pp3/4, compound 1 proton/carbon spectra;433-si-p3.png;433-si-p4.png | supports | Original compound 1 spectral pages and embedded drawings were visually inspected. They agree with the reported pentacyclic diene, carboxylic acid, secondary alcohol and hydroxymethyl substitution and relative geometry. The displayed structures are A, not the adjacent C/F congeners; full de novo spectral elucidation is not claimed. |
| crystal | DOI:10.1021/np2002435.s001; 433-np2002435_si_001.cif;433-crystal-check.py/.json;433-crystal-derived.mol | supports | The original C30H46O4 crystal dataset was independently reconstructed from its orthorhombic cell and fractional atomic coordinates. Bond/stereo perception yields the exact native key and reciprocal chiral graph match. The deposited Flack value is −0.2(10), which is too imprecise to establish absolute hand independently. Model agreement supports connectivity and relative geometry; it is not evidence of a racemate or grounds to force a stereochemical change. |
| activity | PMID:24145793; DOI:10.3390/molecules181013003; 433-PMC6269735.xml selected Results, Table 2 parent A column, Methods 3.2 and 3.6 | supports | The follow-up original includes exact parent A in comparator rows: H.pylori MBC 64 µg/mL and B.cereus MIC 32 µg/mL. These are distinct endpoints, and the six other bacterial MICs exceed 128 µg/mL. Methods defer assay details to the 2011 source; strain/inoculum/time details remain unresolved. Derivatives 6/7 are chemically modified A and their activities are not transferred. |
| antiviral | PMID:24145793; DOI:10.3390/molecules181013003; 433-PMC6269735.xml Table 1 parent A row and adjoining HBV/cytotoxicity Results | context_only | Table 1 gives A HepG2 2.2.15 cytotoxicity IC50 18.9 and both HBsAg/HBeAg endpoints &gt;50 under a µg/mL header. Nearby derivative prose uses µM and conflates cytotoxicity with replicated-DNA wording. These observations do not establish selective A anti-HBV activity, but above-limit antigen results alone do not prove universal absence. The inaccessible original/correction prevents resolving the explicit ChEBI antiviral assertion. |
| adjacent | PMID:24489593; DOI:10.1155/2013/857213; 433-PMC3899712.xml complete abstract and selected Materials and Methods scope | context_only | The anti-inflammatory original examines plant extract, HOEO/HODA and fatsicarpains D/F. These host-cell pathway and toxicity experiments do not establish an A antimicrobial mechanism. No NF-κB or other adjacent-congener target claim is adopted. |
| correction | DOI:10.1021/np200650p; 433-correction-crossref.json;433-fetch2.json/433-fetch3.json attempted correction html/abs/pdf | context_only | Official metadata confirms a correction to the exact 2011 original in J. Nat. Prod.74:2030. The correction body could not be retrieved and its content is unknown; neither a structural revision nor a unit correction is assumed. |
| registry | reaxys:21876589; 433-chebi.json database_accessions;433-fetch.json direct Reaxys attempt | context_only | Current ChEBI repeats the exact registry number, but direct Reaxys returned 403. Independent registry identity and stereo scope therefore remain unverified; no wrong-ID finding follows. |
| owners | Maintained ChEBI extraction, classification and generation; 433-owner-append.json;433-raw-rows.json;433-source-audit.json | supports | All 13 initial hashes were preserved. Actual source table, role-label table, class configuration, extractor, seeder and decision owner were already captured. Native source-derived fields, relative synonym, sole adopted PMID and all three histories reconcile. Additional plant-metabolite roles in current ChEBI are outside the imported antimicrobial role slice, not an automatic completeness defect. |
| validation | Focused native and identity checks; 433-focused-results.json;433-strict.tsv;433-authority-chemistry.log;433-crystal-check.log;433-ledger.log | supports | Schema, strict terms, native molecular consistency, seven-encoding authority comparison, crystal-model comparison and source ledger passed. None substitutes for unresolved original antiviral experiments or correction content. |
| access | Bounded public exact-compound research; 433-local-hits.txt includes ignored files;433-search-core.json;433-openalex.json;433-fetch.json through 433-fetch4.json;official publisher and PubMed searches | context_only | The original 2011 main and correction returned 403 through attempted official routes; OpenAlex listed the main as closed. The official supplement and deposited CIFs were freely retrieved, as were two relevant later originals. Reaxys returned 403. Broad search leads were screened for exact material; unrelated and adjacent-compound studies are not treated as A evidence. |

## Limits And Additional Notes

- The complete 2011 abstract, exact A spectral drawings and deposited crystal model were inspected; the original main paper and its correction were not accessible.
- The deposited crystal model matches the native, but Flack −0.2(10) does not independently establish absolute hand. No full diffraction refinement or de novo NMR assignment was performed.
- The later exact-parent antibacterial table supports activity but defers assay protocol to the 2011 original. MBC and MIC are kept distinct, with no inferred strain, clinical breakpoint or therapeutic efficacy.
- The 2013 HBV/cytotoxicity presentation has endpoint and unit ambiguity. Antigen IC50 values above the tested limit do not by themselves refute activity under other conditions, and cytotoxicity is not selective antiviral efficacy.
- Direct Reaxys access failed 403; current ChEBI registry attribution alone cannot independently validate the linked registry structure.
- Neighboring-congener host anti-inflammatory studies and chemically modified A derivatives are excluded from exact A mechanism claims.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Standalone chemistry used the batch 019 interpreter against batch 044; native schema/strict and ledger used batch 044.
- No native gene, protein, pathway or transcriptional module is asserted, so a structured bacterial mechanism adapter was not applicable.
- A bounded curator follow-up should resolve the original correction and selective antiviral assay support before altering the ChEBI-owned definition/role or enriching mechanism/quantitative fields.
- No native content or scientific status was changed.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T161218Z-fatsicarpain-a-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of fatsicarpain A
started_at: '2026-10-21T15:56:37Z'
finished_at: '2026-10-21T16:12:18Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Entire native and maintained ChEBI row read; all original input
    hashes verified. Independent atom/parity-aware authority comparisons and reconstruction
    from original crystallographic coordinates supplemented visual inspection of original
    A spectral drawings and exact-parent assay rows.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
native_verdict: Identity and antibacterial support consistent; antiviral selectivity
  and original correction unresolved
scientific_review: true
summary: Fatsicarpain A has consistent neutral C30H46O4 identity across seven chemical
  encodings and an independently reconstructed original crystal model. The original
  isolation abstract and spectral supplement support the exact compound and plant
  source. A later primary paper includes positive exact-parent antibacterial observations.
  Its HBV antigen results and cytotoxicity wording do not resolve selective antiviral
  support. The original main paper, its correction and direct Reaxys record remain
  inaccessible; no demonstrated native correction was established. Scientific assessment
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
  - path: data/antibiotics/antibacterial/fatsicarpain-a.yaml
    sha256: f4fde55544a37bbdbb899af027a49e32bef353b9b855d78c41323f947e931879
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
scope:
  description: 'Whole SEEDED, EXACT fatsicarpain A record: structural definition,
    plant isolation, antibacterial and anti-HBV assertions, relative systematic synonym,
    two parents, two roles, entire chemical structure, Reaxys link, source concept
    and three histories.'
  selection: Queue 433 in isolated batch 044. All actual ChEBI extraction and classification
    owners were already present in the preserved initial 13 inputs; their roles were
    made explicit in target ownership.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:69216
targets:
- target_id: CHEBI:69216
  path: data/antibiotics/antibacterial/fatsicarpain-a.yaml
  label: fatsicarpain A
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
    path: conf/sources.yaml
    role: Maintained antimicrobial filing-class role mapping
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_role_names.tsv
    role: Adopted role labels
checks:
- check_id: schema
  name: Native schema
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/fatsicarpain-a.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0.
  target_ids:
  - CHEBI:69216
  evidence_ids:
  - validation
- check_id: strict
  name: Native strict terms
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/fatsicarpain-a.yaml --out /private/tmp/am-review-session/433-strict.tsv
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; no ERROR rows.
  target_ids:
  - CHEBI:69216
  evidence_ids:
  - validation
- check_id: native-chemistry
  name: Native molecular consistency
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    433 > /private/tmp/am-review-session/433-focused-run.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Neutral formula, masses, SMILES and InChI agree.
  target_ids:
  - CHEBI:69216
  evidence_ids:
  - chemistry
  - validation
- check_id: authority-chemistry
  name: Independent authority graph comparison
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/433-authority-chemistry.py
    433 > /private/tmp/am-review-session/433-authority-chemistry.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Seven encodings agree by full reciprocal stereochemical graph matching,
    including eight configured centers.
  target_ids:
  - CHEBI:69216
  evidence_ids:
  - chemistry
- check_id: crystal-model
  name: Original crystal-model comparison
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/433-crystal-check.py
    > /private/tmp/am-review-session/433-crystal-check.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Original CIF fractional coordinates converted to Cartesian geometry; perceived
    graph and stereo match native. The imprecise Flack value does not independently
    establish absolute hand.
  target_ids:
  - CHEBI:69216
  evidence_ids:
  - crystal
- check_id: source-ledger
  name: Whole source and reference ledger
  command: .venv/bin/python /private/tmp/am-review-session/433-ledger.py > /private/tmp/am-review-session/433-ledger.log
    2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: All 13 original hashes unchanged; source fields, roles, synonym, sole adopted
    PMID, parent comparator rows and three chronological histories reconciled.
  target_ids:
  - CHEBI:69216
  evidence_ids:
  - owners
  - adopted
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:69216
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
  - CHEBI:69216
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
  - CHEBI:69216
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
  - CHEBI:69216
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
  - CHEBI:69216
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
  - CHEBI:69216
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
  - CHEBI:69216
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
  - CHEBI:69216
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
  - CHEBI:69216
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/fatsicarpain-a.yaml
  locator: Entire native YAML
  accessed_at: '2026-10-21T16:07:06Z'
  support: supports
  summary: The record denotes fatsicarpain A, with an explicitly relative systematic
    synonym and configured structure. It asserts antibacterial and anti-HBV activity
    in its definition/roles, but contains no exact protein target, quantitative MIC,
    clinical status or ProducerOrganism object. Three source-seeding events are retained.
- evidence_id: chemistry
  kind: authority
  reference: CHEBI:69216; PubChem CID53493446
  locator: 433-chebi.json/.mol;433-pubchem.json/.sdf;433-authority-chemistry.json
  accessed_at: '2026-10-21T16:07:06Z'
  support: supports
  summary: Native SMILES/InChI, current ChEBI SMILES/molfile and public PubChem SMILES/InChI/SDF
    agree on neutral C30H46O4 and key ZMKQRHHJEZOFLT-KFYXPMKRSA-N. Full reciprocal
    atom mappings preserve all eight configured centers. PubChem was queried by exact
    key and is an independent comparison source, not a newly asserted native xref.
    Database concordance alone is not experimental proof.
  snapshot_sha256: e10ee51dfee5047a6367aa2f9be7dca4128a021126fba4f05ab5959e5d365e4b
- evidence_id: terms
  kind: authority
  reference: CHEBI:25872; CHEBI:35868; CHEBI:33282; CHEBI:64951
  locator: 433-chebi-25872/35868/33282/64951.json;433-chebi.json ontology relations
  accessed_at: '2026-10-21T16:02:05.129388Z'
  support: supports
  summary: Current terms resolve to pentacyclic triterpenoid, hydroxy monocarboxylic
    acid, antibacterial agent and anti-HBV agent. The exact current ChEBI entry retains
    the native definition, roles, relative synonym and Reaxys registry mapping. Antibacterial
    filing follows the maintained role precedence; it does not remove the separate
    antiviral role. This verifies ontology/source consistency, not antiviral selectivity.
  snapshot_sha256: 7651f5d816c4aa96fba0cb8efe5dfd78bbefe1153b366739d7d2e9a777bd58ca
- evidence_id: adopted
  kind: primary_source
  reference: PMID:21766884; DOI:10.1021/np2002435
  locator: 433-adopted-core.json complete original abstract
  accessed_at: '2026-10-21T16:02:05.130473Z'
  support: supports
  summary: The original names fatsicarpains A–G as compounds 1–7 isolated from leaves
    and twigs of Fatsia polycarpa. It explicitly reports crystallography of 1, 8,
    9, so A has direct crystal-study support. Cytotoxic, HBV and antibacterial assays
    were evaluated in vitro, but the abstract does not give individual activity outcomes.
  snapshot_sha256: e735872ab85e688bfbcb28983cc79480cce28a3c69f141505f293806f50f75ba
- evidence_id: spectra
  kind: primary_source
  reference: DOI:10.1021/np2002435.s004
  locator: 433-np2002435_si_004.pdf printed pp3/4, compound 1 proton/carbon spectra;433-si-p3.png;433-si-p4.png
  accessed_at: '2026-10-21T16:04:09.255423Z'
  support: supports
  summary: Original compound 1 spectral pages and embedded drawings were visually
    inspected. They agree with the reported pentacyclic diene, carboxylic acid, secondary
    alcohol and hydroxymethyl substitution and relative geometry. The displayed structures
    are A, not the adjacent C/F congeners; full de novo spectral elucidation is not
    claimed.
  snapshot_sha256: 6b6c33ff37d4781e3dff6c09637aa375e102454fdb36c436af3421e261a6080a
- evidence_id: crystal
  kind: primary_source
  reference: DOI:10.1021/np2002435.s001
  locator: 433-np2002435_si_001.cif;433-crystal-check.py/.json;433-crystal-derived.mol
  accessed_at: '2026-10-21T16:04:09.255532Z'
  support: supports
  summary: The original C30H46O4 crystal dataset was independently reconstructed from
    its orthorhombic cell and fractional atomic coordinates. Bond/stereo perception
    yields the exact native key and reciprocal chiral graph match. The deposited Flack
    value is −0.2(10), which is too imprecise to establish absolute hand independently.
    Model agreement supports connectivity and relative geometry; it is not evidence
    of a racemate or grounds to force a stereochemical change.
  snapshot_sha256: afe3af65d0e1c267a4af1ff7651479819b6d6aa59cdc02e6c8444709a923545f
- evidence_id: activity
  kind: primary_source
  reference: PMID:24145793; DOI:10.3390/molecules181013003
  locator: 433-PMC6269735.xml selected Results, Table 2 parent A column, Methods 3.2
    and 3.6
  accessed_at: '2026-10-21T16:03:25.679579Z'
  support: supports
  summary: 'The follow-up original includes exact parent A in comparator rows: H.pylori
    MBC 64 µg/mL and B.cereus MIC 32 µg/mL. These are distinct endpoints, and the
    six other bacterial MICs exceed 128 µg/mL. Methods defer assay details to the
    2011 source; strain/inoculum/time details remain unresolved. Derivatives 6/7 are
    chemically modified A and their activities are not transferred.'
  snapshot_sha256: d6485c70036c3b55150905f6343846004f1373012a8a785aa113d07f2cf091f0
- evidence_id: antiviral
  kind: primary_source
  reference: PMID:24145793; DOI:10.3390/molecules181013003
  locator: 433-PMC6269735.xml Table 1 parent A row and adjoining HBV/cytotoxicity
    Results
  accessed_at: '2026-10-21T16:03:25.679579Z'
  support: context_only
  summary: Table 1 gives A HepG2 2.2.15 cytotoxicity IC50 18.9 and both HBsAg/HBeAg
    endpoints >50 under a µg/mL header. Nearby derivative prose uses µM and conflates
    cytotoxicity with replicated-DNA wording. These observations do not establish
    selective A anti-HBV activity, but above-limit antigen results alone do not prove
    universal absence. The inaccessible original/correction prevents resolving the
    explicit ChEBI antiviral assertion.
  snapshot_sha256: d6485c70036c3b55150905f6343846004f1373012a8a785aa113d07f2cf091f0
- evidence_id: adjacent
  kind: primary_source
  reference: PMID:24489593; DOI:10.1155/2013/857213
  locator: 433-PMC3899712.xml complete abstract and selected Materials and Methods
    scope
  accessed_at: '2026-10-21T16:03:25.851984Z'
  support: context_only
  summary: The anti-inflammatory original examines plant extract, HOEO/HODA and fatsicarpains
    D/F. These host-cell pathway and toxicity experiments do not establish an A antimicrobial
    mechanism. No NF-κB or other adjacent-congener target claim is adopted.
  snapshot_sha256: f7d5fb60583240124e3752b46891250720308cfe1de72c1137cd5adef2d1dc9e
- evidence_id: correction
  kind: authority
  reference: DOI:10.1021/np200650p
  locator: 433-correction-crossref.json;433-fetch2.json/433-fetch3.json attempted
    correction html/abs/pdf
  accessed_at: '2026-10-21T16:03:57.748652Z'
  support: context_only
  summary: Official metadata confirms a correction to the exact 2011 original in J.
    Nat. Prod.74:2030. The correction body could not be retrieved and its content
    is unknown; neither a structural revision nor a unit correction is assumed.
  snapshot_sha256: 75c4c8645ec0ff94a5dd6ce66431e456cf234ca30c2882d99f1baa65ef3d8a40
- evidence_id: registry
  kind: authority
  reference: reaxys:21876589
  locator: 433-chebi.json database_accessions;433-fetch.json direct Reaxys attempt
  accessed_at: '2026-10-21T16:02:05.129388Z'
  support: context_only
  summary: Current ChEBI repeats the exact registry number, but direct Reaxys returned
    403. Independent registry identity and stereo scope therefore remain unverified;
    no wrong-ID finding follows.
  snapshot_sha256: 7651f5d816c4aa96fba0cb8efe5dfd78bbefe1153b366739d7d2e9a777bd58ca
- evidence_id: owners
  kind: database
  reference: Maintained ChEBI extraction, classification and generation
  locator: 433-owner-append.json;433-raw-rows.json;433-source-audit.json
  accessed_at: '2026-10-21T16:07:06Z'
  support: supports
  summary: All 13 initial hashes were preserved. Actual source table, role-label table,
    class configuration, extractor, seeder and decision owner were already captured.
    Native source-derived fields, relative synonym, sole adopted PMID and all three
    histories reconcile. Additional plant-metabolite roles in current ChEBI are outside
    the imported antimicrobial role slice, not an automatic completeness defect.
  snapshot_sha256: c4f8e1908f92a13e3151a8a9e975167e3aeef8ba91f61c8aeae099b8f636794d
- evidence_id: validation
  kind: validation
  reference: Focused native and identity checks
  locator: 433-focused-results.json;433-strict.tsv;433-authority-chemistry.log;433-crystal-check.log;433-ledger.log
  accessed_at: '2026-10-21T16:07:06Z'
  support: supports
  summary: Schema, strict terms, native molecular consistency, seven-encoding authority
    comparison, crystal-model comparison and source ledger passed. None substitutes
    for unresolved original antiviral experiments or correction content.
  snapshot_sha256: 129b6b2a664b442203ace2680822ca1562d1dc7b137a9a72430ad419a1f9d338
- evidence_id: access
  kind: search
  reference: Bounded public exact-compound research
  locator: 433-local-hits.txt includes ignored files;433-search-core.json;433-openalex.json;433-fetch.json
    through 433-fetch4.json;official publisher and PubMed searches
  accessed_at: '2026-10-21T16:07:06Z'
  support: context_only
  summary: The original 2011 main and correction returned 403 through attempted official
    routes; OpenAlex listed the main as closed. The official supplement and deposited
    CIFs were freely retrieved, as were two relevant later originals. Reaxys returned
    403. Broad search leads were screened for exact material; unrelated and adjacent-compound
    studies are not treated as A evidence.
  snapshot_sha256: 6ed3e2bec569751d14f388edd2f550c65288335ca47223610466b71f5e46db58
  search_scope: 433-local-hits.txt includes ignored files;433-search-core.json;433-openalex.json;433-fetch.json
    through 433-fetch4.json;official publisher and PubMed searches
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral compound and relative geometry
  outcome: supported
  summary: Native and current authority graphs, original A drawing and deposited crystal
    model agree. No sibling, salt or hydroxy-position mismatch was established.
  target_ids:
  - CHEBI:69216
  evidence_ids:
  - chemistry
  - spectra
  - crystal
- assessment_id: stereo
  area: representation
  topic: Absolute versus relative stereochemical support
  outcome: unknown
  summary: The relative synonym is retained. The encoded hand matches the deposited
    model, but its imprecise Flack value and inaccessible main argument do not independently
    establish absolute configuration. No racemate inference or forced edit is justified.
  target_ids:
  - CHEBI:69216
  evidence_ids:
  - crystal
  - spectra
  - chemistry
- assessment_id: classification
  area: grounding
  topic: Parents and antimicrobial filing
  outcome: supported
  summary: The two structural parents fit the graph; antibacterial activity is supported
    by exact-parent observations. Filing priority and retained role mappings match
    source owners.
  target_ids:
  - CHEBI:69216
  evidence_ids:
  - terms
  - chemistry
  - activity
  - owners
- assessment_id: plant
  area: evidence
  topic: Plant-isolation statement
  outcome: supported
  summary: The original abstract directly identifies leaves/twigs of Fatsia polycarpa.
    This is isolation context, not proof of a specific biosynthetic pathway or a separately
    asserted producer-strain object.
  target_ids:
  - CHEBI:69216
  evidence_ids:
  - adopted
  - record
- assessment_id: antiviral
  area: evidence
  topic: Anti-HBV claim and selectivity
  outcome: unknown
  summary: ChEBI explicitly supports the imported role, while inspected primary antigen/cytotoxicity
    results do not resolve selective antiviral evidence. Original and correction access
    are needed; no blanket no-activity conclusion is made.
  target_ids:
  - CHEBI:69216
  evidence_ids:
  - terms
  - antiviral
  - correction
- assessment_id: quantitative
  area: quantity
  topic: MIC, MBC and assay details
  outcome: unknown
  summary: The positive A bacterial endpoints are distinct and retain their published
    units. Full strain/protocol details are deferred to the inaccessible original,
    so no native quantitative observation is proposed yet.
  target_ids:
  - CHEBI:69216
  evidence_ids:
  - activity
  - access
- assessment_id: target
  area: evidence
  topic: Exact antimicrobial mechanism
  outcome: unknown
  summary: The native asserts no molecular target. No primary A target mechanism was
    established in the inspected sources; neighboring host-signaling results cannot
    fill it. The structured adapter has no applicable native protein/gene/pathway
    query.
  target_ids:
  - CHEBI:69216
  evidence_ids:
  - record
  - adjacent
- assessment_id: registry
  area: grounding
  topic: Reaxys registry mapping
  outcome: unknown
  summary: ChEBI attribution is verified, but the registry itself was inaccessible.
  target_ids:
  - CHEBI:69216
  evidence_ids:
  - registry
- assessment_id: correction
  area: scope
  topic: Original published correction
  outcome: unknown
  summary: The correction exists, but its unknown content is not transferred into
    a structural or activity finding.
  target_ids:
  - CHEBI:69216
  evidence_ids:
  - correction
  - access
- assessment_id: ownership
  area: ownership
  topic: Maintained fields and history
  outcome: supported
  summary: All 13 unchanged initial inputs include actual owners; the sole adopted
    lead and all source-derived fields are accounted for.
  target_ids:
  - CHEBI:69216
  evidence_ids:
  - owners
  - validation
findings: []
actions: []
limitations:
- The complete 2011 abstract, exact A spectral drawings and deposited crystal model
  were inspected; the original main paper and its correction were not accessible.
- The deposited crystal model matches the native, but Flack −0.2(10) does not independently
  establish absolute hand. No full diffraction refinement or de novo NMR assignment
  was performed.
- The later exact-parent antibacterial table supports activity but defers assay protocol
  to the 2011 original. MBC and MIC are kept distinct, with no inferred strain, clinical
  breakpoint or therapeutic efficacy.
- The 2013 HBV/cytotoxicity presentation has endpoint and unit ambiguity. Antigen
  IC50 values above the tested limit do not by themselves refute activity under other
  conditions, and cytotoxicity is not selective antiviral efficacy.
- Direct Reaxys access failed 403; current ChEBI registry attribution alone cannot
  independently validate the linked registry structure.
- Neighboring-congener host anti-inflammatory studies and chemically modified A derivatives
  are excluded from exact A mechanism claims.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Standalone chemistry used the batch 019 interpreter against batch 044; native schema/strict
  and ledger used batch 044.
- No native gene, protein, pathway or transcriptional module is asserted, so a structured
  bacterial mechanism adapter was not applicable.
- A bounded curator follow-up should resolve the original correction and selective
  antiviral assay support before altering the ChEBI-owned definition/role or enriching
  mechanism/quantitative fields.
- No native content or scientific status was changed.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:69216
- https://pubchem.ncbi.nlm.nih.gov/compound/53493446
- https://doi.org/10.1021/np2002435
- https://doi.org/10.1021/np200650p
- https://doi.org/10.1021/np2002435.s001
- https://doi.org/10.1021/np2002435.s004
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6269735/
tags:
- record-review
- fatsicarpain-a
- triterpenoid
- exact-compound
```
