# Caminoside A: exact glycolipid identity and secretion-assay scope

- Review: 20261021T104414Z-caminoside-a-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:21:12Z
- Finished UTC: 2026-10-21T10:44:14Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native graph and current authorities agree on the acetylated/butyrylated tetrasaccharide glycolipid. Original primary text supports the reported secretion phenotype and isolation, with important mixture-versus-peracetate and assay-method limits. The later C10 absolute-assignment paper was verified bibliographically but its experimental text was inaccessible. No confirmed native correction was established; primary enrichment remains qualified. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position189; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65570 | data/antibiotics/antibacterial/caminoside-a.yaml | generated | caminoside A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:65570 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:65570 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:65570 | Actual focused execution exited 0. |
| Structured pathway-context search | passed | False | CHEBI:65570 | Catalog and E.coli precise1k type III secretion search executed before web follow-up; one gene annotation and zero modules were kept as context only. |
| Authoritative full QC | failed | True | CHEBI:65570 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65570 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65570 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65570 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65570 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65570 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65570 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65570 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65570 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact graph and experimental assignment boundary

identity: supported. Targets: CHEBI:65570.

Molecular encodings, detailed synonym and current authorities agree. Original connectivity and sugar evidence are compatible; later C10 experimental proof remains an explicit access limitation.

### Chemical parents and asserted registry

grounding: unknown. Targets: CHEBI:65570.

All six parents fit and antibacterial classification is source-supported. Reaxys remains independently unverified.

### Isolation and secretion phenotype

evidence: supported. Targets: CHEBI:65570.

The original attributes these observations to caminoside A; preparation and assay limits qualify quantitative use. No protein target or biosynthetic producer is inferred.

### Secretion assay versus molecular target

evidence: unknown. Targets: CHEBI:65570.

Esp secretion inhibition is a pathway-level phenotype. Neither the original assay nor the structured annotation query resolves a direct target.

### Adopted leads and maintained source

provenance: supported. Targets: CHEBI:65570.

Both adopted PMIDs were resolved and their access scopes recorded; source hash capture and seed provenance remain unchanged.

### Optional primary evidence

completeness: unknown. Targets: CHEBI:65570.

Original observations can inform future enrichment after material/assay adjudication; optional blanks are not defects.

### Focused deterministic validation

schema: supported. Targets: CHEBI:65570.

Schema, strict validation and both chemical encodings pass.

## Findings

### F1: Preserve preparation and secretion-assay boundaries during enrichment

informational / open / confirmed; issue key: caminoside-a-primary-material-and-assay-scope.

The original paper offers primary phenotypic evidence beyond the source definition, but distinguishes an underivatized mixture from isolated pure A peracetate. Quantitative adoption requires reconciliation of this material scope and the later A–D study; no incorrect native numeric assay or protein target is populated.

## Recommended Actions And Acceptance Checks

### A1

Optionally curate original evidence after resolving assay material and detailed methods.

- Inspect the 2006 original Methods and compound-specific assays; distinguish natural A, caminoside mixtures and peracetylated derivatives. Preserve original units and do not conflate micrograms/disk with micrograms/mL.
- Retain EPEC secretion IC50 separately from growth MICs and counterassays; identify strains, assay conditions and material purity before creating structured susceptibility observations.
- Verify the adopted 2004 C10 absolute-assignment experiment before native sign-off. Current 10R database agreement is not a substitute for the source.
- Keep sponge isolation and voucher separate from demonstrated biosynthesis. Do not nominate YgeN or another protein from the reference-dataset annotation. Use validated curation/history only under separate authorization.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/caminoside-a.yaml; Entire native YAML; all thirteen initial captured inputs | supports | The SEEDED/EXACT record has a 10R aglycone synonym, six chemical parents, antibacterial role, molecular descriptors, one Reaxys cross-reference, one exact source concept and three seed events. Its definition reports type III secretion inhibition but asserts no particular protein target. Optional quantitative activity, resistance, producer, clinical and causal graph objects are unpopulated. |
| owner | data/raw/chebi_antimicrobials.tsv; Exact CHEBI:65570 row; source configuration, role names, extractor and seeder; 189-local-hits.txt | supports | Adopted ChEBI owns the identity, definition, parents, role and two PMID leads. Ignored-inclusive local search outside Git internals and virtual environments identified maintained owners and generated projections; no additional exact curator override was established. The source mint and three seed events reproduce coherently. |
| chemistry | Independent RDKit parsing of both native molecular encodings; 189-chemistry.json; focused schema and strict output | supports | Both encodings yield XTQWRNIJLVUYJY-ZFMPSFEPSA-N, neutral C49H86O22, one component, matching masses and twenty-one configured tetrahedral centres. The non-glycerol methyl-ketone lipid and four sugars fit the detailed synonym; six parents cover beta-D-glucoside, glycolipid, acetate ester, butyrate ester, methyl ketone and tetrasaccharide derivative. |
| authority | https://www.ebi.ac.uk/chebi/CHEBI:65570; Live OLS term and all six direct parents; 189-chebi.json and 189-parents.json | supports | Current ChEBI reproduces the native structure and claim scope; all six chemical parents fit. A supplementary PubChem exact-key query returns CID21777925 with the same complete InChI and molecular identity. Database agreement does not independently establish experimental stereochemistry. |
| registry | https://www.reaxys.com/reaxys/secured/compound.do?substanceId=9985572; Asserted Reaxys identity request | unknown | The sole asserted Reaxys link returned HTTP403. Its mapping remains source-asserted and independently unverified; access failure is not evidence of a mismatch. |
| discovery | PMID:12423093; DOI:10.1021/ol0268337; Original 2002 article pp4089–4092, rehosted original-paper transcription at https://www.lookchem.com/FreePDFArticle_102517-74-8_6372213.htm | partial | The original article describes a C19 lipid joined to two beta-D-glucose, alpha-L-quinovose and beta-D-6-deoxytalose units. HMBC supports the 1→2 backbone/quinovose and 1→6 talose branch; central glucose bears 3-O-butyryl and 4-O-acetyl. Native material was an inseparable caminoside mixture with differing aglycones; acetylation allowed pure A peracetate isolation. C10 absolute configuration was not resolved by the attempted Mosher method. |
| supporting | DOI:10.1021/ol0268337; ACS supporting information; 189-si-5837829.pdf, Methods pp3–7; the four downloaded supporting files together span pp1–37 | supports | Methods document Caminus sphaeroconia collected at Toucari Caves, Dominica, at10m; voucher ZMA POR16775. Purification produced 3.4mg of pure caminoside A peracetate. Methanolysis and sugar-derivative comparisons support sugar identities; pure-peracetate identity must not be equated with demonstrated purity of the underivatized assay preparation. Isolation is supported; sponge biosynthetic production was not independently demonstrated. |
| phenotype | PMID:12423093; DOI:10.1021/ol0268337; Original final biological-activity paragraph and opening assay rationale | partial | Authors attribute secretion-screen IC50 20micromolar to caminoside A and report MRSA and vancomycin-resistant Enterococcus MIC12micrograms/mL, versus pathogenic E.coli &gt;100micrograms/mL. The screen measures EPEC Esp secretion while counterselecting growth/general secretion effects. These are pathway-associated phenotypes, not direct binding to a named secretion protein. Exact strain, detailed assay conditions and underivatized-material purity need resolution before structured quantitative adoption. |
| later-stereo | PMID:15547902; DOI:10.1002/anie.200461158; PubMed/EPMC bibliographic record; 189-adopted.json; publisher access attempt | unknown | The adopted 2004 paper is specifically about absolute stereochemistry of the caminoside A aglycone. PubMed/EPMC provide no abstract and the Wiley full-text route returned403. The native/current-database 10R assignment is therefore not independently audited against that paper’s experimental CD analysis in this review. Secondary abstract reproductions were treated as leads only. |
| followup | PMID:16499312; DOI:10.1021/np050192h; Complete original abstract on the ACS publication page | partial | The 2006 original abstract reports isolation of caminosides A–D and spectroscopic characterization of new B–D. Detailed original Methods and assay tables were not obtained. It does not, at abstract scope, settle preparation purity or justify importing congener values or converting per-disk observations into concentration MICs. |
| adapter | iModulonDB e_coli/precise1k; 189-imodulondb-datasets.txt and 189-imodulondb-t3ss.txt; structured calls before web follow-up | context_only | The catalog and type III secretion query completed before open-ended literature research. Search returned one putative gene annotation, b2858/ygeN, and no modules. This reference dataset is not the original EPEC assay and provides neither a caminoside response signature nor evidence that YgeN is its molecular target. |

## Limits And Additional Notes

- Original 2002 main text was read as a rehosted article transcription, and its free ACS SI Methods pp3–7 were inspected. The rehosted transparent figure images rendered unreadably; no independent visual structural proof is claimed. Downloaded SI raw NMR panels were not independently reprocessed.
- The 2004 absolute-assignment article was verified at metadata scope only. The 2006 A–D original was read at abstract scope only; detailed assay/material reconciliation remains open.
- Reaxys was inaccessible. Exact bacterial strains, full secretion/growth protocols and purity of the underivatized assay material were not established. This is bounded research, not an exhaustive clinical or mechanism survey.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All thirteen initial input hashes remain unchanged. No native record, source inventory, curation history or status was edited.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T104414Z-caminoside-a-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Caminoside A: exact glycolipid identity and secretion-assay scope'
started_at: '2026-10-21T10:21:12Z'
finished_at: '2026-10-21T10:44:14Z'
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
verdict: blocked
scientific_review: true
summary: The native graph and current authorities agree on the acetylated/butyrylated
  tetrasaccharide glycolipid. Original primary text supports the reported secretion
  phenotype and isolation, with important mixture-versus-peracetate and assay-method
  limits. The later C10 absolute-assignment paper was verified bibliographically but
  its experimental text was inaccessible. No confirmed native correction was established;
  primary enrichment remains qualified. Scientific assessment retains the stated evidence
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
  - path: data/antibiotics/antibacterial/caminoside-a.yaml
    sha256: 68c2b782fa323b1dab383cdd880150809a76f64b70dfeefc919e245ac576518f
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
- target_id: CHEBI:65570
  path: data/antibiotics/antibacterial/caminoside-a.yaml
  label: caminoside A
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
  selection: Initially uncovered queue position189; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65570
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65570
  command: .venv/bin/python /private/tmp/am-review-session/focus014-root.py 189
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65570
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/caminoside-a.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:65570
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/caminoside-a.yaml --out /private/tmp/am-review-session/189-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: structured-adapter
  name: Structured pathway-context search
  status: passed
  required: false
  summary: Catalog and E.coli precise1k type III secretion search executed before
    web follow-up; one gene annotation and zero modules were kept as context only.
  target_ids:
  - CHEBI:65570
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
  - CHEBI:65570
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
  - CHEBI:65570
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
  - CHEBI:65570
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
  - CHEBI:65570
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
  - CHEBI:65570
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
  - CHEBI:65570
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
  - CHEBI:65570
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
  - CHEBI:65570
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
  - CHEBI:65570
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/caminoside-a.yaml
  locator: Entire native YAML; all thirteen initial captured inputs
  accessed_at: '2026-10-21T10:44:13Z'
  support: supports
  summary: The SEEDED/EXACT record has a 10R aglycone synonym, six chemical parents,
    antibacterial role, molecular descriptors, one Reaxys cross-reference, one exact
    source concept and three seed events. Its definition reports type III secretion
    inhibition but asserts no particular protein target. Optional quantitative activity,
    resistance, producer, clinical and causal graph objects are unpopulated.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Exact CHEBI:65570 row; source configuration, role names, extractor and
    seeder; 189-local-hits.txt
  accessed_at: '2026-10-21T10:44:13Z'
  support: supports
  summary: Adopted ChEBI owns the identity, definition, parents, role and two PMID
    leads. Ignored-inclusive local search outside Git internals and virtual environments
    identified maintained owners and generated projections; no additional exact curator
    override was established. The source mint and three seed events reproduce coherently.
  snapshot_sha256: b5e6c3050de73982e47c00cee617bb7bc32ab3e3b74ade79d1041abe5537d39d
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit parsing of both native molecular encodings
  locator: 189-chemistry.json; focused schema and strict output
  accessed_at: '2026-10-21T10:44:13Z'
  support: supports
  summary: Both encodings yield XTQWRNIJLVUYJY-ZFMPSFEPSA-N, neutral C49H86O22, one
    component, matching masses and twenty-one configured tetrahedral centres. The
    non-glycerol methyl-ketone lipid and four sugars fit the detailed synonym; six
    parents cover beta-D-glucoside, glycolipid, acetate ester, butyrate ester, methyl
    ketone and tetrasaccharide derivative.
  snapshot_sha256: 18de48ba969069539cdc14a08609cfe3735330d9571a21a50a58d50cbe084c68
- evidence_id: authority
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:65570
  locator: Live OLS term and all six direct parents; 189-chebi.json and 189-parents.json
  accessed_at: '2026-10-21T10:44:13Z'
  support: supports
  summary: Current ChEBI reproduces the native structure and claim scope; all six
    chemical parents fit. A supplementary PubChem exact-key query returns CID21777925
    with the same complete InChI and molecular identity. Database agreement does not
    independently establish experimental stereochemistry.
  snapshot_sha256: b7a7df5027a4797d579e3a4dc53d2996a1b4bdf327c2caaeb37dab37137de0c6
- evidence_id: registry
  kind: database
  reference: https://www.reaxys.com/reaxys/secured/compound.do?substanceId=9985572
  locator: Asserted Reaxys identity request
  accessed_at: '2026-10-21T10:44:13Z'
  support: unknown
  summary: The sole asserted Reaxys link returned HTTP403. Its mapping remains source-asserted
    and independently unverified; access failure is not evidence of a mismatch.
  snapshot_sha256: a0c990be2db1b7c3104aee973d1a9a4cf73f2c70349f1c864f8de59902e046e3
- evidence_id: discovery
  kind: primary_source
  reference: PMID:12423093; DOI:10.1021/ol0268337
  locator: Original 2002 article pp4089–4092, rehosted original-paper transcription
    at https://www.lookchem.com/FreePDFArticle_102517-74-8_6372213.htm
  accessed_at: '2026-10-21T10:44:13Z'
  support: partial
  summary: The original article describes a C19 lipid joined to two beta-D-glucose,
    alpha-L-quinovose and beta-D-6-deoxytalose units. HMBC supports the 1→2 backbone/quinovose
    and 1→6 talose branch; central glucose bears 3-O-butyryl and 4-O-acetyl. Native
    material was an inseparable caminoside mixture with differing aglycones; acetylation
    allowed pure A peracetate isolation. C10 absolute configuration was not resolved
    by the attempted Mosher method.
- evidence_id: supporting
  kind: primary_source
  reference: DOI:10.1021/ol0268337; ACS supporting information
  locator: 189-si-5837829.pdf, Methods pp3–7; the four downloaded supporting files
    together span pp1–37
  accessed_at: '2026-10-21T10:44:13Z'
  support: supports
  summary: Methods document Caminus sphaeroconia collected at Toucari Caves, Dominica,
    at10m; voucher ZMA POR16775. Purification produced 3.4mg of pure caminoside A
    peracetate. Methanolysis and sugar-derivative comparisons support sugar identities;
    pure-peracetate identity must not be equated with demonstrated purity of the underivatized
    assay preparation. Isolation is supported; sponge biosynthetic production was
    not independently demonstrated.
  snapshot_sha256: 5cf1ebbd0c06a7b171e9ff5169a9b44fb4ad7cd5cfae685bd479579377b1c169
- evidence_id: phenotype
  kind: primary_source
  reference: PMID:12423093; DOI:10.1021/ol0268337
  locator: Original final biological-activity paragraph and opening assay rationale
  accessed_at: '2026-10-21T10:44:13Z'
  support: partial
  summary: Authors attribute secretion-screen IC50 20micromolar to caminoside A and
    report MRSA and vancomycin-resistant Enterococcus MIC12micrograms/mL, versus pathogenic
    E.coli >100micrograms/mL. The screen measures EPEC Esp secretion while counterselecting
    growth/general secretion effects. These are pathway-associated phenotypes, not
    direct binding to a named secretion protein. Exact strain, detailed assay conditions
    and underivatized-material purity need resolution before structured quantitative
    adoption.
- evidence_id: later-stereo
  kind: database
  reference: PMID:15547902; DOI:10.1002/anie.200461158
  locator: PubMed/EPMC bibliographic record; 189-adopted.json; publisher access attempt
  accessed_at: '2026-10-21T10:44:13Z'
  support: unknown
  summary: The adopted 2004 paper is specifically about absolute stereochemistry of
    the caminoside A aglycone. PubMed/EPMC provide no abstract and the Wiley full-text
    route returned403. The native/current-database 10R assignment is therefore not
    independently audited against that paper’s experimental CD analysis in this review.
    Secondary abstract reproductions were treated as leads only.
  snapshot_sha256: 1dcffae796a57391728d5e76cf428a1c28058b72d95ceaf24399bda6c97a9f32
- evidence_id: followup
  kind: primary_source
  reference: PMID:16499312; DOI:10.1021/np050192h
  locator: Complete original abstract on the ACS publication page
  accessed_at: '2026-10-21T10:44:13Z'
  support: partial
  summary: The 2006 original abstract reports isolation of caminosides A–D and spectroscopic
    characterization of new B–D. Detailed original Methods and assay tables were not
    obtained. It does not, at abstract scope, settle preparation purity or justify
    importing congener values or converting per-disk observations into concentration
    MICs.
- evidence_id: adapter
  kind: database
  reference: iModulonDB e_coli/precise1k
  locator: 189-imodulondb-datasets.txt and 189-imodulondb-t3ss.txt; structured calls
    before web follow-up
  accessed_at: '2026-10-21T10:44:13Z'
  support: context_only
  summary: The catalog and type III secretion query completed before open-ended literature
    research. Search returned one putative gene annotation, b2858/ygeN, and no modules.
    This reference dataset is not the original EPEC assay and provides neither a caminoside
    response signature nor evidence that YgeN is its molecular target.
  snapshot_sha256: 775119e735cb3a410b73cef480549035364a0d9be97eed08b3e01194fe279ec7
assessments:
- assessment_id: identity
  area: identity
  topic: Exact graph and experimental assignment boundary
  outcome: supported
  summary: Molecular encodings, detailed synonym and current authorities agree. Original
    connectivity and sugar evidence are compatible; later C10 experimental proof remains
    an explicit access limitation.
  target_ids:
  - CHEBI:65570
  evidence_ids:
  - native
  - chemistry
  - authority
  - discovery
  - later-stereo
- assessment_id: grounding
  area: grounding
  topic: Chemical parents and asserted registry
  outcome: unknown
  summary: All six parents fit and antibacterial classification is source-supported.
    Reaxys remains independently unverified.
  target_ids:
  - CHEBI:65570
  evidence_ids:
  - authority
  - registry
  - phenotype
- assessment_id: definition
  area: evidence
  topic: Isolation and secretion phenotype
  outcome: supported
  summary: The original attributes these observations to caminoside A; preparation
    and assay limits qualify quantitative use. No protein target or biosynthetic producer
    is inferred.
  target_ids:
  - CHEBI:65570
  evidence_ids:
  - discovery
  - supporting
  - phenotype
- assessment_id: mechanism
  area: evidence
  topic: Secretion assay versus molecular target
  outcome: unknown
  summary: Esp secretion inhibition is a pathway-level phenotype. Neither the original
    assay nor the structured annotation query resolves a direct target.
  target_ids:
  - CHEBI:65570
  evidence_ids:
  - phenotype
  - adapter
- assessment_id: provenance
  area: provenance
  topic: Adopted leads and maintained source
  outcome: supported
  summary: Both adopted PMIDs were resolved and their access scopes recorded; source
    hash capture and seed provenance remain unchanged.
  target_ids:
  - CHEBI:65570
  evidence_ids:
  - owner
  - discovery
  - later-stereo
- assessment_id: completeness
  area: completeness
  topic: Optional primary evidence
  outcome: unknown
  summary: Original observations can inform future enrichment after material/assay
    adjudication; optional blanks are not defects.
  target_ids:
  - CHEBI:65570
  evidence_ids:
  - phenotype
  - supporting
  - followup
- assessment_id: schema
  area: schema
  topic: Focused deterministic validation
  outcome: supported
  summary: Schema, strict validation and both chemical encodings pass.
  target_ids:
  - CHEBI:65570
  evidence_ids:
  - chemistry
findings:
- finding_id: F1
  issue_key: caminoside-a-primary-material-and-assay-scope
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Preserve preparation and secretion-assay boundaries during enrichment
  description: The original paper offers primary phenotypic evidence beyond the source
    definition, but distinguishes an underivatized mixture from isolated pure A peracetate.
    Quantitative adoption requires reconciliation of this material scope and the later
    A–D study; no incorrect native numeric assay or protein target is populated.
  target_ids:
  - CHEBI:65570
  field_paths:
  - evidence
  - activity_spectrum
  - mode_of_action
  evidence_ids:
  - discovery
  - supporting
  - phenotype
  - followup
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/caminoside-a.yaml
    role: Optional curator-owned primary claims through validated writer/history
  rule_id: 'review-checklist: exact compound and claim-level evidence'
  native_severity: informational optional enrichment
  normalization_reason: This is a bounded opportunity and access limitation, not a
    confirmed native scientific error.
actions:
- action_id: A1
  description: Optionally curate original evidence after resolving assay material
    and detailed methods.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:65570
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/caminoside-a.yaml
    role: Optional curator-owned primary claims through validated writer/history
  acceptance_checks:
  - Inspect the 2006 original Methods and compound-specific assays; distinguish natural
    A, caminoside mixtures and peracetylated derivatives. Preserve original units
    and do not conflate micrograms/disk with micrograms/mL.
  - Retain EPEC secretion IC50 separately from growth MICs and counterassays; identify
    strains, assay conditions and material purity before creating structured susceptibility
    observations.
  - Verify the adopted 2004 C10 absolute-assignment experiment before native sign-off.
    Current 10R database agreement is not a substitute for the source.
  - Keep sponge isolation and voucher separate from demonstrated biosynthesis. Do
    not nominate YgeN or another protein from the reference-dataset annotation. Use
    validated curation/history only under separate authorization.
limitations:
- Original 2002 main text was read as a rehosted article transcription, and its free
  ACS SI Methods pp3–7 were inspected. The rehosted transparent figure images rendered
  unreadably; no independent visual structural proof is claimed. Downloaded SI raw
  NMR panels were not independently reprocessed.
- The 2004 absolute-assignment article was verified at metadata scope only. The 2006
  A–D original was read at abstract scope only; detailed assay/material reconciliation
  remains open.
- Reaxys was inaccessible. Exact bacterial strains, full secretion/growth protocols
  and purity of the underivatized assay material were not established. This is bounded
  research, not an exhaustive clinical or mechanism survey.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All thirteen initial input hashes remain unchanged. No native record, source inventory,
  curation history or status was edited.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
