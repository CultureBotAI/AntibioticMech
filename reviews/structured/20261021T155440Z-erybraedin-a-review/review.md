# Review of erybraedin A

- Review: 20261021T155440Z-erybraedin-a-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T15:30:49Z
- Finished UTC: 2026-10-21T15:54:40Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact chemistry and original antibacterial evidence agree. The newly inspected 2007 original confirms erybraedin A antiplasmodial, antimycobacterial and cytotoxic activities. Its isolation account assigns A to E. subumbrans stems, creating a bounded mismatch with the native E. stricta attribution. A minor maintained-source correction is recommended; no claim of universal absence from E. stricta is made.

## Scope And Provenance

Whole SEEDED, EXACT record: structural and biological definition, three typed names, two class parents and two roles, complete molecular structure, three cross-references, source concept and three histories. All five adopted PMID leads, current authorities and exact-congener boundaries reviewed.

Selection: Queue 414 in isolated batch 042. All 13 initial hashes were preserved and actual ChEBI maintained owners confirmed before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65862 | data/antibiotics/antibacterial/erybraedin-a.yaml | generated | erybraedin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native schema | passed | True | CHEBI:65862 | Exit 0. |
| Native strict terms | passed | True | CHEBI:65862 | Exit 0; no ERROR rows. |
| Native molecular consistency | passed | False | CHEBI:65862 | Native graph, key, formula, charge, masses and minted source identifier agree. |
| Exact authority and atom-parity comparison | passed | False | CHEBI:65862 | Eight encodings share the exact key and reciprocal chirality-enabled mapping; both centers are R, with two phenolic hydroxyls and two prenyl groups. |
| Whole source and reference ledger | passed | False | CHEBI:65862 | All 13 hashes unchanged; all five adopted PMIDs disposed, native source fields reconciled and three ordered histories checked. |
| Authoritative full QC | failed | True | CHEBI:65862 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65862 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65862 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65862 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65862 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65862 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65862 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65862 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65862 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact structure, stereo and names

identity: supported. Targets: CHEBI:65862.

Native and official encodings match including atom parity; original antibacterial abstract also names the exact R,R compound.

### Parents and exact database cross-reference

grounding: supported. Targets: CHEBI:65862.

Pterocarpan/phenol class and exact LIPID MAPS grounding are supported.

### Antibacterial and cytotoxic claims

evidence: supported. Targets: CHEBI:65862.

Exact original abstracts support antibacterial activity and A-specific cytotoxicity with tested-panel scope.

### Antiplasmodial and antimycobacterial activities

evidence: supported. Targets: CHEBI:65862.

The original compound 2 row independently confirms both activities within its tested systems.

### Plant isolation attribution

scope: concern. Targets: CHEBI:65862.

E. zeyheri is supported independently; the adopted 2007 isolation account allocates A to E. subumbrans, creating a source-specific mismatch with the E. stricta phrase.

### Independent CAS and Reaxys details

grounding: unknown. Targets: CHEBI:65862.

Both mappings persist in current ChEBI; direct details were inaccessible.

### Congener and mined-data boundaries

scope: supported. Targets: CHEBI:65862.

No bacterial target is asserted. Erybraedin C mechanisms and mined A activity summaries are not promoted to exact A primary mechanism experiments.

### Optional quantitative and mechanistic enrichment

completeness: supported. Targets: CHEBI:65862.

Quantitative enrichment is optional and must preserve exact compound, organism, assay and units. The demonstrated definition-attribution issue is captured separately.

### Source and history reconciliation

ownership: supported. Targets: CHEBI:65862.

Actual maintained owners and all 13 unchanged inputs are recorded; three histories reconcile.

## Findings

### F1: The inherited plant attribution does not follow the adopted isolation account

minor / open / confirmed; issue key: chebi-65862-erybraedin-a-plant-attribution.

The definition names E. stricta, but the adopted 2007 paper explicitly assigns erybraedin A compound 2 to E. subumbrans stems. Its E. stricta isolation list identifies different compounds. This is a bounded source-attribution defect, not evidence that A can never occur in E. stricta; separate exact-compound support would be needed to retain that phrase.

## Recommended Actions And Acceptance Checks

### A1

Correct the maintained ChEBI definition or apply a documented narrow source correction so this paper supports E. subumbrans stems. Retain E. zeyheri and the verified activities. Retain E. stricta only if an independent exact-compound isolation source is supplied. Do not equate plant isolation with experimentally established biosynthesis.

- Regenerated definition maps each plant attribution to exact-compound primary evidence.
- Preserve the exact R,R graph, identity links and supported activity roles.
- Run documented validation and corpus gates after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/erybraedin-a.yaml; Entire native YAML | supports | The native denotes one configured erybraedin A structure. Its definition includes isolation and four activity contexts, but it has no molecular-target, quantitative MIC, resistance, producer-object or clinical-status assertion. |
| chemistry | CHEBI:65862; LIPID MAPS:LMPK12070044; PubChem CID21141346; 414-chebi.json/.mol;414-lipidmaps.json;414-pubchem.json;414-authority-chemistry.json | supports | All eight parsed native/current ChEBI/PubChem/LIPID MAPS encodings agree on HOGHBEDTLGAJAS-CPJSRVTESA-N and neutral C25H28O4. Reciprocal chirality-enabled mappings preserve both configured R centers. Graph checks find two phenolic hydroxyls and two prenyl groups. Official systematic names specify positions 3,9 and 4,10, respectively, and agree with the native names. Database agreement is distinguished from an independent absolute-configuration experiment. |
| lipidmaps | lipidmaps:LMPK12070044; 414-lipidmaps.json exact identifier, name, systematic name, synonym, formula and structure | supports | The exact cited entry resolves to Erybraedin A, explicitly names the (6aR,11aR) diprenylpterocarpan and lists 4-prenylphaseollidin as a synonym. Its full graph matches the native, rather than merely sharing a family label. |
| antibacterial | PMID:15597305; DOI:10.1002/ptr.1556; 414-core-15597305.json complete original abstract | supports | The study isolates erybraedin A from E. zeyheri roots and explicitly identifies it as the (6aR,11aR)-3,9-dihydroxy-4,10-diprenyl compound. It reports exact-compound VRE growth inhibition, bacteriostatic action and vancomycin combination experiments. The abstract gives a VRE MIC range of 1.56–3.13 µg/mL and does not justify universal susceptibility, clinical efficacy or direct protein binding. Individual isolate methods/tables were not independently retrieved. |
| streptococci | PMID:17055201; DOI:10.1016/j.jep.2006.09.022; 414-core-17055201.json complete original abstract | supports | Erybraedin A is compound 2 isolated from E. subumbrans stems and is among the strongest tested Streptococcus inhibitors. The source separately identifies compound 7, erycristagallin, as the strongest agent across its VRSA panel; those compound 7 results are not attributed to erybraedin A. |
| ancillary | PMID:18087807; DOI:10.1007/BF02977363; Original 2007 pp.1398–1402, especially isolation p.1399 and Results/Table I p.1400; 414-original-web-notes.json records web read depth | supports | Compound 2 is erybraedin A. Table I reports P. falciparum K1 IC50 3.4 µg/mL and M. tuberculosis H37Ra MABA MIC 25 µg/mL, alongside KB/BC/NCI-H187 cytotoxicity of 5.1/2.9/2.1 µg/mL. Isolation and Results assign compound 2 to E. subumbrans stems. The E. stricta isolate list names other compounds. These experiments establish tested-system activity, not direct target binding. |
| isolation | PMID:20521535; DOI:10.1177/1934578X1000500509; PMID:8590641; DOI:10.1016/0031-9422(95)00037-8; 414-core-20521535.json and414-core-8590641.json complete original abstracts | supports | The 2010 source identifies known erybraedin A among pterocarpans from E. melanacantha stem bark using spectroscopic comparisons. The 1995 source identifies A among known compounds from E. eriotricha root bark in antimicrobial-guided work. Neither abstract supplies a new absolute-configuration determination for A; neither source is silently substituted for the stated E. stricta isolation. |
| leads | All five adopted ChEBI citation leads; 414-source-audit.json;414-raw-rows.json;414-core-*.json | supports | All five adopted PMIDs resolved to exact MED records and complete abstracts. The 2007 main text and exact activity row were additionally inspected; other inaccessible full tables remain distinguished from abstract evidence. |
| new-source-scope | PMID:34244528; DOI:10.1038/s41598-021-92964-9; PMID:39125081; DOI:10.3390/molecules29153678; 414-PMC8270993.xml extended-dataset/QSAR sections;414-PMC11313871.xml abstract, isolation and compound-identification passages | context_only | The 2021 paper includes erybraedin A in an extended literature-mined antibacterial dataset; its in-house membrane assays cannot automatically be assigned to A. The 2024 original principally examines bitucarpin A, erybraedin C/D and bituminarins. Its C-congener neuroblastoma and topoisomerase context does not establish an A mechanism. |
| terms | CHEBI:26377; CHEBI:33853; CHEBI:33282; CHEBI:64915; 414-term-26377.json;414-term-33853.json;414-term-33282.json;414-term-64915.json | supports | All four terms resolve. Chemical parents and antibacterial/antiplasmodial roles are supported by the graph and exact primary experiments. The antiplasmodial drug role does not establish clinical approval. |
| registry | cas:119269-76-0; reaxys:9090260; 414-chebi.json database_accessions;414-cas.html;414-fetch.json | context_only | Current ChEBI reproduces both registry mappings. Direct CAS returned an application error without compound detail; Reaxys returned 403. Their exact registry details remain independently unverified, with no wrong-identifier finding inferred from unavailable access. |
| owners | Maintained ChEBI extraction and seeding; 414-owner-append.json;414-raw-rows.json;414-source-audit.json | supports | All 13 original hashes remain unchanged. Exact adopted source rows reproduce the definition, structure, names, roles and links; extractor/seeder/decision owners are recorded. Three histories are ordered and the native remains SEEDED. |
| validation | Focused native and independent chemistry/source checks; 414-focused-results.json;414-strict.tsv;414-authority-chemistry.log;414-ledger.log | supports | Schema, strict terms, native molecular consistency, eight-encoding parity comparison and source ledger all pass. Scientific activity verification limits remain distinct from deterministic validity. |
| access | Bounded public exact-erybraedin-A retrieval; 414-local-hits.txt includes ignored files;414-fetch.json through414-fetch3.json;ignored-inclusive scratch search for DOI/PMID2007;417-fetch3.json;414-original-web-notes.json | context_only | Initial publisher routes returned preview HTML or 403. A later author-uploaded original 2007 PDF was successfully read through web.open despite direct HTTP 403. Main text and extracted Table I were inspected; no local PDF bytes or visual figure inspection are claimed. The earlier retrieval failures remain recorded. |

## Limits And Additional Notes

- All five adopted papers were inspected at complete-abstract level; the 2007 main text and Table I were additionally read through public PDF text extraction. Direct download remained 403 and its structure figure was not visually inspected.
- Full strain-level antibacterial protocols in the 2004 and earlier 2007 studies were not independently retrieved. The later 2007 parasite, mycobacterial and cytotoxicity methods and exact A row were inspected; no unreviewed numerical transfer is proposed.
- Current ChEBI, PubChem and LIPID MAPS agree structurally. This is not a new experimental absolute-configuration determination, although the 2004 original abstract explicitly names the R,R compound.
- CAS and Reaxys are mapped by current ChEBI but could not be independently inspected in their public detail services.
- The later QSAR source includes literature-mined A data, while the 2024 neuroblastoma study concerns other congeners. Neither substitutes for exact A mechanism evidence; no specific bacterial target is asserted.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native gene, protein, pathway or target assertion triggers a structured iModulonDB lookup. No bacterial protein-specific follow-up was used.
- Standalone chemistry used the batch 019 interpreter against batch 042; native validation and source ledger used batch 042.
- No native record or scientific status was changed.
- 414-original-web-notes.json is a timestamped reviewer read-depth note, not a source snapshot. The original PDF URL is supplied for independent reinspection.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T155440Z-erybraedin-a-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of erybraedin A
started_at: '2026-10-21T15:30:49Z'
finished_at: '2026-10-21T15:54:40Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Whole native and exact source row read; eight independently
    parsed authority encodings compared with chirality and atom mappings; all adopted
    original abstracts inspected; current ontology/identifier sources and available
    primary source scope checked without transferring congener results. Original 2007
    main text and Table I were subsequently inspected through the author-uploaded
    PDF text extraction.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Structure and stated activities supported; minor source-specific plant
  attribution correction
scientific_review: true
summary: Exact chemistry and original antibacterial evidence agree. The newly inspected
  2007 original confirms erybraedin A antiplasmodial, antimycobacterial and cytotoxic
  activities. Its isolation account assigns A to E. subumbrans stems, creating a bounded
  mismatch with the native E. stricta attribution. A minor maintained-source correction
  is recommended; no claim of universal absence from E. stricta is made.
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
  - path: data/antibiotics/antibacterial/erybraedin-a.yaml
    sha256: dd79f51ea16455e6452b15d7d82433a1900d5dc237807d2d36aab90c162e6020
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
  description: 'Whole SEEDED, EXACT record: structural and biological definition,
    three typed names, two class parents and two roles, complete molecular structure,
    three cross-references, source concept and three histories. All five adopted PMID
    leads, current authorities and exact-congener boundaries reviewed.'
  selection: Queue 414 in isolated batch 042. All 13 initial hashes were preserved
    and actual ChEBI maintained owners confirmed before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65862
targets:
- target_id: CHEBI:65862
  path: data/antibiotics/antibacterial/erybraedin-a.yaml
  label: erybraedin A
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
checks:
- check_id: schema
  name: Native schema
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/erybraedin-a.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0.
  target_ids:
  - CHEBI:65862
  evidence_ids:
  - validation
- check_id: strict
  name: Native strict terms
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/erybraedin-a.yaml --out /private/tmp/am-review-session/414-strict.tsv
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; no ERROR rows.
  target_ids:
  - CHEBI:65862
  evidence_ids:
  - validation
- check_id: native-chemistry
  name: Native molecular consistency
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    414 > /private/tmp/am-review-session/414-focused-run.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Native graph, key, formula, charge, masses and minted source identifier
    agree.
  target_ids:
  - CHEBI:65862
  evidence_ids:
  - chemistry
  - validation
- check_id: authority-chemistry
  name: Exact authority and atom-parity comparison
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/414-authority-chemistry.py
    > /private/tmp/am-review-session/414-authority-chemistry.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Eight encodings share the exact key and reciprocal chirality-enabled mapping;
    both centers are R, with two phenolic hydroxyls and two prenyl groups.
  target_ids:
  - CHEBI:65862
  evidence_ids:
  - chemistry
- check_id: source-ledger
  name: Whole source and reference ledger
  command: .venv/bin/python /private/tmp/am-review-session/414-ledger.py > /private/tmp/am-review-session/414-ledger.log
    2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: All 13 hashes unchanged; all five adopted PMIDs disposed, native source
    fields reconciled and three ordered histories checked.
  target_ids:
  - CHEBI:65862
  evidence_ids:
  - owners
  - leads
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:65862
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
  - CHEBI:65862
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
  - CHEBI:65862
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
  - CHEBI:65862
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
  - CHEBI:65862
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
  - CHEBI:65862
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
  - CHEBI:65862
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
  - CHEBI:65862
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
  - CHEBI:65862
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/erybraedin-a.yaml
  locator: Entire native YAML
  accessed_at: '2026-10-21T15:42:00Z'
  support: supports
  summary: The native denotes one configured erybraedin A structure. Its definition
    includes isolation and four activity contexts, but it has no molecular-target,
    quantitative MIC, resistance, producer-object or clinical-status assertion.
- evidence_id: chemistry
  kind: authority
  reference: CHEBI:65862; LIPID MAPS:LMPK12070044; PubChem CID21141346
  locator: 414-chebi.json/.mol;414-lipidmaps.json;414-pubchem.json;414-authority-chemistry.json
  accessed_at: '2026-10-21T15:42:00Z'
  support: supports
  summary: All eight parsed native/current ChEBI/PubChem/LIPID MAPS encodings agree
    on HOGHBEDTLGAJAS-CPJSRVTESA-N and neutral C25H28O4. Reciprocal chirality-enabled
    mappings preserve both configured R centers. Graph checks find two phenolic hydroxyls
    and two prenyl groups. Official systematic names specify positions 3,9 and 4,10,
    respectively, and agree with the native names. Database agreement is distinguished
    from an independent absolute-configuration experiment.
  snapshot_sha256: b18f6ad01e4233f59a6a09344b4218056b1d0d0b89688d40e322431a806492a6
- evidence_id: lipidmaps
  kind: authority
  reference: lipidmaps:LMPK12070044
  locator: 414-lipidmaps.json exact identifier, name, systematic name, synonym, formula
    and structure
  accessed_at: '2026-10-21T15:39:15.955375Z'
  support: supports
  summary: The exact cited entry resolves to Erybraedin A, explicitly names the (6aR,11aR)
    diprenylpterocarpan and lists 4-prenylphaseollidin as a synonym. Its full graph
    matches the native, rather than merely sharing a family label.
  snapshot_sha256: a96ca18141ec3783aef3c4301b6598c0079ae2401ffd8c53de6cea91e32e99c8
- evidence_id: antibacterial
  kind: primary_source
  reference: PMID:15597305; DOI:10.1002/ptr.1556
  locator: 414-core-15597305.json complete original abstract
  accessed_at: '2026-10-21T15:39:17.596671Z'
  support: supports
  summary: The study isolates erybraedin A from E. zeyheri roots and explicitly identifies
    it as the (6aR,11aR)-3,9-dihydroxy-4,10-diprenyl compound. It reports exact-compound
    VRE growth inhibition, bacteriostatic action and vancomycin combination experiments.
    The abstract gives a VRE MIC range of 1.56–3.13 µg/mL and does not justify universal
    susceptibility, clinical efficacy or direct protein binding. Individual isolate
    methods/tables were not independently retrieved.
  snapshot_sha256: 541ed2a8ed2373f76a84d19a65b99c44a369578835a4eb581e9b09ec4a9a601d
- evidence_id: streptococci
  kind: primary_source
  reference: PMID:17055201; DOI:10.1016/j.jep.2006.09.022
  locator: 414-core-17055201.json complete original abstract
  accessed_at: '2026-10-21T15:39:18.035917Z'
  support: supports
  summary: Erybraedin A is compound 2 isolated from E. subumbrans stems and is among
    the strongest tested Streptococcus inhibitors. The source separately identifies
    compound 7, erycristagallin, as the strongest agent across its VRSA panel; those
    compound 7 results are not attributed to erybraedin A.
  snapshot_sha256: c4e1d10991c1baefae12039ec1b338822939b84eb90bd8751986b29114458f85
- evidence_id: ancillary
  kind: primary_source
  reference: PMID:18087807; DOI:10.1007/BF02977363
  locator: Original 2007 pp.1398–1402, especially isolation p.1399 and Results/Table
    I p.1400; 414-original-web-notes.json records web read depth
  accessed_at: '2026-10-21T15:46:36Z'
  support: supports
  summary: Compound 2 is erybraedin A. Table I reports P. falciparum K1 IC50 3.4 µg/mL
    and M. tuberculosis H37Ra MABA MIC 25 µg/mL, alongside KB/BC/NCI-H187 cytotoxicity
    of 5.1/2.9/2.1 µg/mL. Isolation and Results assign compound 2 to E. subumbrans
    stems. The E. stricta isolate list names other compounds. These experiments establish
    tested-system activity, not direct target binding.
- evidence_id: isolation
  kind: primary_source
  reference: PMID:20521535; DOI:10.1177/1934578X1000500509; PMID:8590641; DOI:10.1016/0031-9422(95)00037-8
  locator: 414-core-20521535.json and414-core-8590641.json complete original abstracts
  accessed_at: '2026-10-21T15:39:18.216863Z'
  support: supports
  summary: The 2010 source identifies known erybraedin A among pterocarpans from E.
    melanacantha stem bark using spectroscopic comparisons. The 1995 source identifies
    A among known compounds from E. eriotricha root bark in antimicrobial-guided work.
    Neither abstract supplies a new absolute-configuration determination for A; neither
    source is silently substituted for the stated E. stricta isolation.
  snapshot_sha256: a42f96d82225fced15f6655078b558a0b72250679d8ac6ee7069ea90c76c311b
- evidence_id: leads
  kind: database
  reference: All five adopted ChEBI citation leads
  locator: 414-source-audit.json;414-raw-rows.json;414-core-*.json
  accessed_at: '2026-10-21T15:42:00Z'
  support: supports
  summary: All five adopted PMIDs resolved to exact MED records and complete abstracts.
    The 2007 main text and exact activity row were additionally inspected; other inaccessible
    full tables remain distinguished from abstract evidence.
  snapshot_sha256: 46d32c00458789e9ba9e976a2f299bb20fbcb3e8af2f22ac741f4fe8c11db243
- evidence_id: new-source-scope
  kind: primary_source
  reference: PMID:34244528; DOI:10.1038/s41598-021-92964-9; PMID:39125081; DOI:10.3390/molecules29153678
  locator: 414-PMC8270993.xml extended-dataset/QSAR sections;414-PMC11313871.xml abstract,
    isolation and compound-identification passages
  accessed_at: '2026-10-21T15:40:23.426463Z'
  support: context_only
  summary: The 2021 paper includes erybraedin A in an extended literature-mined antibacterial
    dataset; its in-house membrane assays cannot automatically be assigned to A. The
    2024 original principally examines bitucarpin A, erybraedin C/D and bituminarins.
    Its C-congener neuroblastoma and topoisomerase context does not establish an A
    mechanism.
  snapshot_sha256: 235b79b426431b377d1c4eab556abc06f7d9b8866db3bb76381a92917e6dc9fb
- evidence_id: terms
  kind: authority
  reference: CHEBI:26377; CHEBI:33853; CHEBI:33282; CHEBI:64915
  locator: 414-term-26377.json;414-term-33853.json;414-term-33282.json;414-term-64915.json
  accessed_at: '2026-10-21T15:39:17.484713Z'
  support: supports
  summary: All four terms resolve. Chemical parents and antibacterial/antiplasmodial
    roles are supported by the graph and exact primary experiments. The antiplasmodial
    drug role does not establish clinical approval.
  snapshot_sha256: 3bb4d59a00e953a70a2f65443be1eb8cb436e51e4c0d260643e9999e91849824
- evidence_id: registry
  kind: authority
  reference: cas:119269-76-0; reaxys:9090260
  locator: 414-chebi.json database_accessions;414-cas.html;414-fetch.json
  accessed_at: '2026-10-21T15:39:15.954548Z'
  support: context_only
  summary: Current ChEBI reproduces both registry mappings. Direct CAS returned an
    application error without compound detail; Reaxys returned 403. Their exact registry
    details remain independently unverified, with no wrong-identifier finding inferred
    from unavailable access.
  snapshot_sha256: d8a3835dca6cdf38762a787c8efc6e66ab03d5141d563d7a9ec4209754b3842c
- evidence_id: owners
  kind: database
  reference: Maintained ChEBI extraction and seeding
  locator: 414-owner-append.json;414-raw-rows.json;414-source-audit.json
  accessed_at: '2026-10-21T15:42:00Z'
  support: supports
  summary: All 13 original hashes remain unchanged. Exact adopted source rows reproduce
    the definition, structure, names, roles and links; extractor/seeder/decision owners
    are recorded. Three histories are ordered and the native remains SEEDED.
  snapshot_sha256: 46d32c00458789e9ba9e976a2f299bb20fbcb3e8af2f22ac741f4fe8c11db243
- evidence_id: validation
  kind: validation
  reference: Focused native and independent chemistry/source checks
  locator: 414-focused-results.json;414-strict.tsv;414-authority-chemistry.log;414-ledger.log
  accessed_at: '2026-10-21T15:42:00Z'
  support: supports
  summary: Schema, strict terms, native molecular consistency, eight-encoding parity
    comparison and source ledger all pass. Scientific activity verification limits
    remain distinct from deterministic validity.
  snapshot_sha256: 05675bd753848212ee3a31c7bbdf5202c0815e1476b3e0f4f9db42de48282dc3
- evidence_id: access
  kind: search
  reference: Bounded public exact-erybraedin-A retrieval
  locator: 414-local-hits.txt includes ignored files;414-fetch.json through414-fetch3.json;ignored-inclusive
    scratch search for DOI/PMID2007;417-fetch3.json;414-original-web-notes.json
  accessed_at: '2026-10-21T15:46:36Z'
  support: context_only
  summary: Initial publisher routes returned preview HTML or 403. A later author-uploaded
    original 2007 PDF was successfully read through web.open despite direct HTTP 403.
    Main text and extracted Table I were inspected; no local PDF bytes or visual figure
    inspection are claimed. The earlier retrieval failures remain recorded.
  snapshot_sha256: 6084b186e2bf48b24ee3a122dcf766630cbf03e2afa7ffc9acd4856de4390ee0
  search_scope: 414-local-hits.txt includes ignored files;414-fetch.json through414-fetch3.json;ignored-inclusive
    scratch search for DOI/PMID2007
assessments:
- assessment_id: identity
  area: identity
  topic: Exact structure, stereo and names
  outcome: supported
  summary: Native and official encodings match including atom parity; original antibacterial
    abstract also names the exact R,R compound.
  target_ids:
  - CHEBI:65862
  evidence_ids:
  - chemistry
  - lipidmaps
  - antibacterial
- assessment_id: grounding
  area: grounding
  topic: Parents and exact database cross-reference
  outcome: supported
  summary: Pterocarpan/phenol class and exact LIPID MAPS grounding are supported.
  target_ids:
  - CHEBI:65862
  evidence_ids:
  - chemistry
  - lipidmaps
  - terms
- assessment_id: activity
  area: evidence
  topic: Antibacterial and cytotoxic claims
  outcome: supported
  summary: Exact original abstracts support antibacterial activity and A-specific
    cytotoxicity with tested-panel scope.
  target_ids:
  - CHEBI:65862
  evidence_ids:
  - antibacterial
  - streptococci
  - ancillary
- assessment_id: ancillary
  area: evidence
  topic: Antiplasmodial and antimycobacterial activities
  outcome: supported
  summary: The original compound 2 row independently confirms both activities within
    its tested systems.
  target_ids:
  - CHEBI:65862
  evidence_ids:
  - ancillary
  - terms
  - access
- assessment_id: isolation
  area: scope
  topic: Plant isolation attribution
  outcome: concern
  summary: E. zeyheri is supported independently; the adopted 2007 isolation account
    allocates A to E. subumbrans, creating a source-specific mismatch with the E.
    stricta phrase.
  target_ids:
  - CHEBI:65862
  evidence_ids:
  - antibacterial
  - ancillary
  - isolation
- assessment_id: registry
  area: grounding
  topic: Independent CAS and Reaxys details
  outcome: unknown
  summary: Both mappings persist in current ChEBI; direct details were inaccessible.
  target_ids:
  - CHEBI:65862
  evidence_ids:
  - registry
  - access
- assessment_id: mechanism
  area: scope
  topic: Congener and mined-data boundaries
  outcome: supported
  summary: No bacterial target is asserted. Erybraedin C mechanisms and mined A activity
    summaries are not promoted to exact A primary mechanism experiments.
  target_ids:
  - CHEBI:65862
  evidence_ids:
  - record
  - new-source-scope
- assessment_id: completeness
  area: completeness
  topic: Optional quantitative and mechanistic enrichment
  outcome: supported
  summary: Quantitative enrichment is optional and must preserve exact compound, organism,
    assay and units. The demonstrated definition-attribution issue is captured separately.
  target_ids:
  - CHEBI:65862
  evidence_ids:
  - record
  - leads
  - ancillary
- assessment_id: ownership
  area: ownership
  topic: Source and history reconciliation
  outcome: supported
  summary: Actual maintained owners and all 13 unchanged inputs are recorded; three
    histories reconcile.
  target_ids:
  - CHEBI:65862
  evidence_ids:
  - owners
  - validation
findings:
- finding_id: F1
  issue_key: chebi-65862-erybraedin-a-plant-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: The inherited plant attribution does not follow the adopted isolation account
  description: The definition names E. stricta, but the adopted 2007 paper explicitly
    assigns erybraedin A compound 2 to E. subumbrans stems. Its E. stricta isolation
    list identifies different compounds. This is a bounded source-attribution defect,
    not evidence that A can never occur in E. stricta; separate exact-compound support
    would be needed to retain that phrase.
  target_ids:
  - CHEBI:65862
  field_paths:
  - definition
  evidence_ids:
  - record
  - ancillary
  - owners
  rule_id: 'review-checklist: Exact compound and source attribution'
  native_severity: Minor source attribution mismatch
  normalization_reason: The exact chemical identity and all stated activity types
    remain supported; the correction is confined to the plant attribution in prose.
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
actions:
- action_id: A1
  description: Correct the maintained ChEBI definition or apply a documented narrow
    source correction so this paper supports E. subumbrans stems. Retain E. zeyheri
    and the verified activities. Retain E. stricta only if an independent exact-compound
    isolation source is supplied. Do not equate plant isolation with experimentally
    established biosynthesis.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:65862
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
  - Regenerated definition maps each plant attribution to exact-compound primary evidence.
  - Preserve the exact R,R graph, identity links and supported activity roles.
  - Run documented validation and corpus gates after separately authorized curation.
limitations:
- All five adopted papers were inspected at complete-abstract level; the 2007 main
  text and Table I were additionally read through public PDF text extraction. Direct
  download remained 403 and its structure figure was not visually inspected.
- Full strain-level antibacterial protocols in the 2004 and earlier 2007 studies were
  not independently retrieved. The later 2007 parasite, mycobacterial and cytotoxicity
  methods and exact A row were inspected; no unreviewed numerical transfer is proposed.
- Current ChEBI, PubChem and LIPID MAPS agree structurally. This is not a new experimental
  absolute-configuration determination, although the 2004 original abstract explicitly
  names the R,R compound.
- CAS and Reaxys are mapped by current ChEBI but could not be independently inspected
  in their public detail services.
- The later QSAR source includes literature-mined A data, while the 2024 neuroblastoma
  study concerns other congeners. Neither substitutes for exact A mechanism evidence;
  no specific bacterial target is asserted.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native gene, protein, pathway or target assertion triggers a structured iModulonDB
  lookup. No bacterial protein-specific follow-up was used.
- Standalone chemistry used the batch 019 interpreter against batch 042; native validation
  and source ledger used batch 042.
- No native record or scientific status was changed.
- 414-original-web-notes.json is a timestamped reviewer read-depth note, not a source
  snapshot. The original PDF URL is supplied for independent reinspection.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:65862
- https://www.lipidmaps.org/databases/lmsd/LMPK12070044
- https://doi.org/10.1002/ptr.1556
- https://doi.org/10.1016/j.jep.2006.09.022
- https://doi.org/10.1007/BF02977363
- https://doi.org/10.1177/1934578X1000500509
- https://doi.org/10.1016/0031-9422(95)00037-8
- https://www.researchgate.net/profile/Apichart-Suksamrarn/publication/5760588_Biological_Activities_of_the_Chemical_Constituents_ofErythrina_stricta_andErythrina_subumbrans/links/0fcfd510a489e350b3000000/Biological-Activities-of-the-Chemical-Constituents-ofErythrina-stricta-andErythrina-subumbrans.pdf
tags:
- record-review
- erybraedin-a
- pterocarpan
- exact-congener
```
