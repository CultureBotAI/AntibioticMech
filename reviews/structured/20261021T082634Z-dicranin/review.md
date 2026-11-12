# Dicranin: exact all-Z structure and compound versus extract evidence

- Review: 20261021T082634Z-dicranin
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:18:31Z
- Finished UTC: 2026-10-21T08:26:34Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Exact neutral all-Z identity, broader classes, antibacterial classification and moss isolation are supported. No corrective finding is demonstrated. Quantitative assay methods, precise enzyme-assay scope and independent Reaxys detail remain limited; purified dicranin is distinguished from extract activity. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole-record scientific review of one exact compound.

Selection: Queue071; CHEBI:65768 in isolated batch008.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65768 | data/antibiotics/antibacterial/9z-12z-15z-octadeca-9-12-15-trien-6-ynoic-acid.yaml | generated | (9Z,12Z,15Z)-octadeca-9,12,15-trien-6-ynoic acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | CHEBI:65768 | Actual command passed. |
| Focused strict | passed | True | CHEBI:65768 | Actual command passed. |
| Structure consistency | passed | True | CHEBI:65768 | Both encodings, all-Z locants and current authorities agree. |
| Structured source applicability | passed | False | CHEBI:65768 | Dataset list inspected; no relevant plant/host coverage. |
| Original complete assay methods | unavailable | False | CHEBI:65768 | Primary abstract inspected; full assay tables/methods unavailable through inspected free routes. |
| Authoritative full QC | failed | True | CHEBI:65768 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65768 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65768 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65768 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65768 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65768 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65768 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65768 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65768 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral all-Z dicranin

identity: supported. Targets: CHEBI:65768.

Native encodings, synonym, current ChEBI, exact-key PubChem and LIPID MAPS agree; explicit bond numbering confirms the preferred label.

### Broader classes and antibacterial role

grounding: supported. Targets: CHEBI:65768.

All four parents are broader structural classes. Purified dicranin activity in the primary abstract supports the antibacterial role, with extract-spectrum boundaries retained.

### Isolation and broad antibacterial wording

evidence: supported. Targets: CHEBI:65768.

Exact dicranin was isolated from Dicranum scoparium and shows antibacterial activity. The native definition does not assert the extract’s broader organism spectrum.

### Specific lipoxygenase wording

evidence: unknown. Targets: CHEBI:65768.

Current ChEBI explicitly asserts arachidonate15-lipoxygenase inhibition. The accessible primary abstract describes soybean15-lpo screening and attributes most activity to dicranin, but its exact substrate, enzyme identity, quantitative response and purified-compound protocol require full text. Do not promote this database wording into a bacterial molecular target.

### Disc diffusion and negative E.coli boundary

completeness: unknown. Targets: CHEBI:65768.

Qualitative compound-specific activity is supported, but numerical diameters, disc loading, strains and methods beyond disc diffusion remain unavailable. A future observation must preserve paper-named Streptococcus faecalis and the tested-condition E.coli negative result; no MIC can be invented. Empty optional activity rows alone are not a defect.

### Antibacterial mechanism versus plant/host assays

scope: unknown. Targets: CHEBI:65768.

No antibacterial mechanism or target is asserted natively or demonstrated by the inspected sources. Soybean enzyme inhibition, host platelet endpoints and moss oxylipin metabolism do not establish one.

### Isolation versus biosynthesis

scope: supported. Targets: CHEBI:65768.

Native isolation wording is supported. Moss metabolism of an administered labeled substrate is not by itself proof of the enzyme that biosynthesizes dicranin.

### Registry equivalence

provenance: unknown. Targets: CHEBI:65768.

CAS is supported by current ChEBI and primary-index metadata. Independent Reaxys structure detail remains unverified; no mismatch is demonstrated.

### Resistance, clinical, datasets and causal graphs

scope: not_applicable. Targets: CHEBI:65768.

No such assertions are native, and the reviewed exact-compound sources do not justify adding these claims.

### Generated ownership and history

provenance: supported. Targets: CHEBI:65768.

Source date, mint, row, filing, identity and three seed/reseed events agree. SEEDED is retained; review does not promote scientific status.

### Focused native checks

schema: supported. Targets: CHEBI:65768.

Schema and strict checks pass.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/9z-12z-15z-octadeca-9-12-15-trien-6-ynoic-acid.yaml; Entire YAML | supports | Read exact identifier and dicranin synonym, definition, four parents, antibacterial role, all structure fields, CAS/Reaxys xrefs, source metadata and three history events. The record is neutral, EXACT and SEEDED. No quantitative activity, molecular target, mechanism, resistance, clinical, dataset or causal-graph assertion is present. |
| owner | data/raw/chebi_antimicrobials.tsv; Row1301; PATHS1553; source configuration, extraction and seeding | supports | The source row agrees with the complete native seed and contains adopted PMIDs1632297,1636161,21604791,8377015. Mint antibioticmech:chebi-8001a4c8c7 reproduces. Imported fixes belong to raw inventory/extractor/seeder; future annotations belong to the actual native record via validated writer and history. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:65768; Structure, definition, synonyms, four is-a relations, roles, registry and species | supports | Current ChEBI agrees with exact neutral Z,Z,Z structure, C18H26O2, key UXMMIMGEKFYPFK-PDBXOOCHSA-N, mass274.404/exact274.19328, dicranin, CAS61481-30-9 and Reaxys4432637. It asserts moss isolation and arachidonate15-lipoxygenase inhibition; those are database assertions. Metabolite and enzyme-inhibitor roles are outside the configured antimicrobial role subset. |
| parent-15904 | https://www.ebi.ac.uk/chebi/CHEBI:15904; Official term identity/definition | supports | Resolves to long-chain fatty acid; strictly broader structural class supported by the native linear C18 chain, triple bond and three double bonds. |
| parent-25380 | https://www.ebi.ac.uk/chebi/CHEBI:25380; Official term identity/definition | supports | Resolves to acetylenic fatty acid; strictly broader structural class supported by the native linear C18 chain, triple bond and three double bonds. |
| parent-59202 | https://www.ebi.ac.uk/chebi/CHEBI:59202; Official term identity/definition | supports | Resolves to straight-chain fatty acid; strictly broader structural class supported by the native linear C18 chain, triple bond and three double bonds. |
| parent-73155 | https://www.ebi.ac.uk/chebi/CHEBI:73155; Official term identity/definition | supports | Resolves to trienoic fatty acid; strictly broader structural class supported by the native linear C18 chain, triple bond and three double bonds. |
| role | https://www.ebi.ac.uk/chebi/CHEBI:33282; Official role definition | supports | Antibacterial agent denotes killing or slowing bacterial growth. Current ChEBI and the exact-compound primary abstract support this role, without implying species-wide spectrum. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/44584408; Exact-full-InChIKey PUG resolution | supports | Exact-key query resolves CID44584408 with identical stereochemical InChI/key, formula, neutral charge and compatible masses. Unspecified-stereo CID6441084 discovered by name search was not substituted. |
| lipidmaps | https://lipidmaps.org/databases/lmsd/LMFA01031109; Structure strings and reference | supports | LIPID MAPS gives the same full key and all-Z structure, PMID8377015 and Dicranum scoparium source. This supports exact identity, not independent assay replication. |
| chemistry | Independent RDKit calculation; Native SMILES and Standard InChI; acid-carbon numbering | supports | Both encodings reproduce full key, neutral charge, one fragment, formula and mass274.404/exact274.193280072. Accurate CIP confirms Z at acid-numbered9–10,12–13,15–16; the triple bond is6–7. |
| antibacterial | PMID:8377015; DOI10.1021/np50097a010; original primary abstract | supports | The isolated Z,Z,Z acid is explicitly named dicranin. Purified compound showed its strongest disc-diffusion effect against paper-named Streptococcus faecalis and was inactive against E.coli. The larger Bacillus/Staphylococcus/E.coli spectrum refers to the CH2Cl2 moss extract. Soybean15-lipoxygenase inhibition is described separately; no bacterial causal target is established. No numeric diameter, disc loading, strain or MIC is supplied in the abstract. |
| platelets1 | PMID:1632297; DOI10.1007/978-3-0348-7262-1_30; primary abstract | context_only | Dicranin isolated from the moss was tested in platelet arachidonate metabolism: weak cyclooxygenase inhibition, increased12-HETE, hydroxylated metabolite and inhibited aggregation. These are host platelet endpoints, not bacterial susceptibility or an antibacterial mode of action. |
| platelets2 | PMID:1636161; DOI10.1016/0049-3848(92)90108-m; primary abstract and publication metadata | context_only | This related duplicate-publication record reports the platelet experiment with preincubation-dependent inhibition and altered12-HETE. Do not count it as independent antibacterial evidence or convert12-lipoxygenase-product increase into15-lipoxygenase inhibition. |
| oxylipins | PMID:21604791; DOI10.1021/ol201114g; primary abstract | context_only | After moss wounding, dicranin is converted to volatile oxylipins. Synthetic deuterium-labeled substrate tracing identifies a conjugatedC13 allene alongsideC5 products. This supports moss metabolism context; substrate transformation alone does not establish a dicranin biosynthetic enzyme or antibacterial mechanism. |
| adapter | kg-microbe-sources imodulondb datasets; Installed CLAW runner; completed free public dataset listing | context_only | Adapter was applied before open-ended web follow-up because the definition names a lipoxygenase. The completed dataset list covers neither soybean nor human/moss model systems; no applicable organism/dataset search or component summary was warranted. Dataset absence is not negative biological evidence. A later sandbox retry failed DNS and the network-enabled retry exited0. |
| registries | https://www.ebi.ac.uk/chebi/CHEBI:65768; Registry Numbers | partial | CAS61481-30-9 is also reported in primary PubMed substance metadata. Reaxys4432637 remains official-ChEBI asserted; independent restricted-registry structure detail was not inspected. |
| search | CultureBotAI/AntibioticMech; Ignored-inclusive local search and bounded free primary discovery | context_only | Whole record, raw/PATHS/config and maintained curation surfaces were inspected. The historical report is discovery context only; its blanket major finding based on absent optional annotations is not adopted. All four adopted abstracts were independently inspected. ACS main text access failed403/paywall; no original quantitative assay table or detailed lipoxygenase protocol was read. |
| gates | just validate; just validate-strict; Actual focused commands in batch008 | supports | Both focused commands exited0, one record and zero strictERROR rows. |

## Limits And Additional Notes

- The original antibacterial paper was available at abstract level; numerical susceptibility results, strains, disc loading, controls and detailed enzyme protocol were not verified.
- Native arachidonate15-lipoxygenase wording is a current ChEBI assertion. The accessible primary abstract names soybean15-lpo; exact substrate/enzyme mapping needs the original methods and cannot establish an antibacterial mechanism.
- Reaxys equivalence remains source-asserted. Bounded search does not establish absence of other exact-compound literature.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All captured maintained-input hashes were rechecked unchanged; no native edit or curation event was made.
- Concrete follow-up: obtain the original Borel1993 assay tables and curate or explicitly defer method-qualified dicranin observations, preserving extract-versus-purified and negative-result boundaries. Inspect the original enzyme assay before changing or expanding the source definition.
- The historical ad hoc report’s optional-field-based major finding was not adopted; optional absence is not a schema or scientific defect by itself.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T082634Z-dicranin
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Dicranin: exact all-Z structure and compound versus extract evidence'
started_at: '2026-10-21T08:18:31Z'
finished_at: '2026-10-21T08:26:34Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independently read full native record, current authorities and
    all adopted primary abstracts; historical report used only as discovery context.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: Exact neutral all-Z identity, broader classes, antibacterial classification
  and moss isolation are supported. No corrective finding is demonstrated. Quantitative
  assay methods, precise enzyme-assay scope and independent Reaxys detail remain limited;
  purified dicranin is distinguished from extract activity. Scientific assessment
  retains the stated evidence limits; full verification is blocked by the shared native-library
  failure.
source:
  git_revision: baf3b3203d748d098686e166cdb2a6138f47eb59
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 5e2e1f975f8aa64f92a06c134c98c750c968fd78f02620a73c9cb611ac018ed8
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: CLAUDE.md
    sha256: 36fb92f8919481cfbf3f17ddde4a1e244c81f76c64396dbbac910c4815fb9f16
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
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
  - path: data/antibiotics/PATHS.tsv
    sha256: 3b1d82d007878e4aca2c28f4001a468776b325b726da2e48abb76a3dc551cc38
    role: context
  - path: data/antibiotics/antibacterial/9z-12z-15z-octadeca-9-12-15-trien-6-ynoic-acid.yaml
    sha256: 0113ae68ee0640a2d055129b0dc5e145da9264f7d1eea82c950e1738970172d2
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
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
    role: context
  - path: reports/yaml_record_review/20260922T160814Z-9z-12z-15z-octadeca-9-12-15-trien-6-ynoic-acid.md
    sha256: ad8e763a60d5c85b785ee67b61e0c5f21e91a4e9a70a6ab2c2a959aa616d2fcb
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
- target_id: CHEBI:65768
  path: data/antibiotics/antibacterial/9z-12z-15z-octadeca-9-12-15-trien-6-ynoic-acid.yaml
  label: (9Z,12Z,15Z)-octadeca-9,12,15-trien-6-ynoic acid
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
  description: Whole-record scientific review of one exact compound.
  selection: Queue071; CHEBI:65768 in isolated batch008.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65768
  exclusions:
  - target: Moss extracts, triglycerides containing dicranin, oxylipin products and
      unspecified-stereo PubChem CID6441084
    reason: Context or related structures only; not substituted for the exact neutral
      all-Z acid.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual command passed.
  target_ids:
  - CHEBI:65768
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/9z-12z-15z-octadeca-9-12-15-trien-6-ynoic-acid.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: strict
  name: Focused strict
  status: passed
  required: true
  summary: Actual command passed.
  target_ids:
  - CHEBI:65768
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/9z-12z-15z-octadeca-9-12-15-trien-6-ynoic-acid.yaml
    --out /private/tmp/am-review-session/071-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Structure consistency
  status: passed
  required: true
  summary: Both encodings, all-Z locants and current authorities agree.
  target_ids:
  - CHEBI:65768
  evidence_ids:
  - chemistry
  - chebi
  - pubchem
- check_id: adapter
  name: Structured source applicability
  status: passed
  required: false
  summary: Dataset list inspected; no relevant plant/host coverage.
  target_ids:
  - CHEBI:65768
  command: env UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run --no-sync --project
    /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources
    imodulondb --timeout 15 datasets
  exit_code: 0
  evidence_ids:
  - adapter
- check_id: fulltext
  name: Original complete assay methods
  status: unavailable
  required: false
  summary: Primary abstract inspected; full assay tables/methods unavailable through
    inspected free routes.
  target_ids:
  - CHEBI:65768
  evidence_ids:
  - antibacterial
  - search
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:65768
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
  - CHEBI:65768
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
  - CHEBI:65768
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
  - CHEBI:65768
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
  - CHEBI:65768
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
  - CHEBI:65768
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
  - CHEBI:65768
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
  - CHEBI:65768
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
  - CHEBI:65768
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/9z-12z-15z-octadeca-9-12-15-trien-6-ynoic-acid.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T08:21:44Z'
  support: supports
  summary: Read exact identifier and dicranin synonym, definition, four parents, antibacterial
    role, all structure fields, CAS/Reaxys xrefs, source metadata and three history
    events. The record is neutral, EXACT and SEEDED. No quantitative activity, molecular
    target, mechanism, resistance, clinical, dataset or causal-graph assertion is
    present.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Row1301; PATHS1553; source configuration, extraction and seeding
  accessed_at: '2026-10-21T08:21:44Z'
  support: supports
  summary: The source row agrees with the complete native seed and contains adopted
    PMIDs1632297,1636161,21604791,8377015. Mint antibioticmech:chebi-8001a4c8c7 reproduces.
    Imported fixes belong to raw inventory/extractor/seeder; future annotations belong
    to the actual native record via validated writer and history.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:65768
  locator: Structure, definition, synonyms, four is-a relations, roles, registry and
    species
  accessed_at: '2026-10-21T08:19:25Z'
  support: supports
  summary: Current ChEBI agrees with exact neutral Z,Z,Z structure, C18H26O2, key
    UXMMIMGEKFYPFK-PDBXOOCHSA-N, mass274.404/exact274.19328, dicranin, CAS61481-30-9
    and Reaxys4432637. It asserts moss isolation and arachidonate15-lipoxygenase inhibition;
    those are database assertions. Metabolite and enzyme-inhibitor roles are outside
    the configured antimicrobial role subset.
  snapshot_sha256: 669d49ddc2e3640bddea8846af24b5bdbd8cf33c7672f1e9e9d7ddf749a2c4cf
- evidence_id: parent-15904
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:15904
  locator: Official term identity/definition
  accessed_at: '2026-10-21T08:19:36Z'
  support: supports
  summary: Resolves to long-chain fatty acid; strictly broader structural class supported
    by the native linear C18 chain, triple bond and three double bonds.
  snapshot_sha256: 3da748d75ff180342d618db256a7b70a7601c4e2817ecf8d8e42a35e43d2231d
- evidence_id: parent-25380
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:25380
  locator: Official term identity/definition
  accessed_at: '2026-10-21T08:19:30Z'
  support: supports
  summary: Resolves to acetylenic fatty acid; strictly broader structural class supported
    by the native linear C18 chain, triple bond and three double bonds.
  snapshot_sha256: a99e3ae995306345be0a855259accc444df7a9e4b94b83e0af49d1e6ff131590
- evidence_id: parent-59202
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:59202
  locator: Official term identity/definition
  accessed_at: '2026-10-21T08:19:26Z'
  support: supports
  summary: Resolves to straight-chain fatty acid; strictly broader structural class
    supported by the native linear C18 chain, triple bond and three double bonds.
  snapshot_sha256: b9fc04511f19403b6bec8c2e0caa8525bc8b438fe90268b737706fd6b362a18f
- evidence_id: parent-73155
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:73155
  locator: Official term identity/definition
  accessed_at: '2026-10-21T08:19:24Z'
  support: supports
  summary: Resolves to trienoic fatty acid; strictly broader structural class supported
    by the native linear C18 chain, triple bond and three double bonds.
  snapshot_sha256: 56bc954610ce7f625923816f74e70cdecce1fd2a57e0fcc33d7ee63c29635cdf
- evidence_id: role
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:33282
  locator: Official role definition
  accessed_at: '2026-10-21T08:19:33Z'
  support: supports
  summary: Antibacterial agent denotes killing or slowing bacterial growth. Current
    ChEBI and the exact-compound primary abstract support this role, without implying
    species-wide spectrum.
  snapshot_sha256: b01c6b5fdd1b347f419247657124ebfe9a2770af7974844696755ce975a1ba21
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/44584408
  locator: Exact-full-InChIKey PUG resolution
  accessed_at: '2026-10-21T08:19:21Z'
  support: supports
  summary: Exact-key query resolves CID44584408 with identical stereochemical InChI/key,
    formula, neutral charge and compatible masses. Unspecified-stereo CID6441084 discovered
    by name search was not substituted.
  snapshot_sha256: 0732123d9c255bb4bf84f2b9fe6cd6c9e06a67bf0d6cfc1c9cb28f4da49e86e7
- evidence_id: lipidmaps
  kind: database
  reference: https://lipidmaps.org/databases/lmsd/LMFA01031109
  locator: Structure strings and reference
  accessed_at: '2026-10-21T08:19:22Z'
  support: supports
  summary: LIPID MAPS gives the same full key and all-Z structure, PMID8377015 and
    Dicranum scoparium source. This supports exact identity, not independent assay
    replication.
  snapshot_sha256: b625b7297ed48bc138f41537b264b4b6056fefe3210c14cb609e43a427bcf001
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit calculation
  locator: Native SMILES and Standard InChI; acid-carbon numbering
  accessed_at: '2026-10-21T08:20:00Z'
  support: supports
  summary: Both encodings reproduce full key, neutral charge, one fragment, formula
    and mass274.404/exact274.193280072. Accurate CIP confirms Z at acid-numbered9–10,12–13,15–16;
    the triple bond is6–7.
  snapshot_sha256: 6b5d5d9c08c8ba5560231daf3f121c54490ad7534f64bf6bca29d842a55700c2
- evidence_id: antibacterial
  kind: primary_source
  reference: PMID:8377015
  locator: DOI10.1021/np50097a010; original primary abstract
  accessed_at: '2026-10-21T08:19:24Z'
  support: supports
  summary: The isolated Z,Z,Z acid is explicitly named dicranin. Purified compound
    showed its strongest disc-diffusion effect against paper-named Streptococcus faecalis
    and was inactive against E.coli. The larger Bacillus/Staphylococcus/E.coli spectrum
    refers to the CH2Cl2 moss extract. Soybean15-lipoxygenase inhibition is described
    separately; no bacterial causal target is established. No numeric diameter, disc
    loading, strain or MIC is supplied in the abstract.
  snapshot_sha256: f24b240f7cd56f503d9ef35857d00d4a55db69daee5b2bef5336aaac68e97153
- evidence_id: platelets1
  kind: primary_source
  reference: PMID:1632297
  locator: DOI10.1007/978-3-0348-7262-1_30; primary abstract
  accessed_at: '2026-10-21T08:19:23Z'
  support: context_only
  summary: 'Dicranin isolated from the moss was tested in platelet arachidonate metabolism:
    weak cyclooxygenase inhibition, increased12-HETE, hydroxylated metabolite and
    inhibited aggregation. These are host platelet endpoints, not bacterial susceptibility
    or an antibacterial mode of action.'
  snapshot_sha256: b7c1b28b2f0dd9f8aec5a54cb5ff9f19d14feae66891273d66e358951d358503
- evidence_id: platelets2
  kind: primary_source
  reference: PMID:1636161
  locator: DOI10.1016/0049-3848(92)90108-m; primary abstract and publication metadata
  accessed_at: '2026-10-21T08:19:24Z'
  support: context_only
  summary: This related duplicate-publication record reports the platelet experiment
    with preincubation-dependent inhibition and altered12-HETE. Do not count it as
    independent antibacterial evidence or convert12-lipoxygenase-product increase
    into15-lipoxygenase inhibition.
  snapshot_sha256: a5b5e115755a4e94e26c36a6ad3f6d38a122b29b3ace1c5a58f180ca900bfdf4
- evidence_id: oxylipins
  kind: primary_source
  reference: PMID:21604791
  locator: DOI10.1021/ol201114g; primary abstract
  accessed_at: '2026-10-21T08:19:24Z'
  support: context_only
  summary: After moss wounding, dicranin is converted to volatile oxylipins. Synthetic
    deuterium-labeled substrate tracing identifies a conjugatedC13 allene alongsideC5
    products. This supports moss metabolism context; substrate transformation alone
    does not establish a dicranin biosynthetic enzyme or antibacterial mechanism.
  snapshot_sha256: c268df9fd5dfec4629c4b9d69e97f2d856cd39785dc0109b0f653a994b242f03
- evidence_id: adapter
  kind: validation
  reference: kg-microbe-sources imodulondb datasets
  locator: Installed CLAW runner; completed free public dataset listing
  accessed_at: '2026-10-21T08:19:48Z'
  support: context_only
  summary: Adapter was applied before open-ended web follow-up because the definition
    names a lipoxygenase. The completed dataset list covers neither soybean nor human/moss
    model systems; no applicable organism/dataset search or component summary was
    warranted. Dataset absence is not negative biological evidence. A later sandbox
    retry failed DNS and the network-enabled retry exited0.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: registries
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:65768
  locator: Registry Numbers
  accessed_at: '2026-10-21T08:21:44Z'
  support: partial
  summary: CAS61481-30-9 is also reported in primary PubMed substance metadata. Reaxys4432637
    remains official-ChEBI asserted; independent restricted-registry structure detail
    was not inspected.
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: Ignored-inclusive local search and bounded free primary discovery
  accessed_at: '2026-10-21T08:21:44Z'
  support: context_only
  summary: Whole record, raw/PATHS/config and maintained curation surfaces were inspected.
    The historical report is discovery context only; its blanket major finding based
    on absent optional annotations is not adopted. All four adopted abstracts were
    independently inspected. ACS main text access failed403/paywall; no original quantitative
    assay table or detailed lipoxygenase protocol was read.
  search_scope: prepare.py71 ran rg --no-ignore --hidden for exact ID,label,slug across
    batch008 excluding.git/.venv; raw/key/mint and maintained curation searches followed.
    Free web queries used dicranin, exact title, PMID8377015, DOI10.1021/np50097a010,
    full key and soybean lipoxygenase. EPMC core abstracts, official ChEBI, exact-key
    PubChem and LIPID MAPS were read. ResearchGate author-page discovery exposed the
    abstract only; plant-extract and triglyceride literature was not transferred.
- evidence_id: gates
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual focused commands in batch008
  accessed_at: '2026-10-21T08:20:39Z'
  support: supports
  summary: Both focused commands exited0, one record and zero strictERROR rows.
  snapshot_sha256: 0f5f78b806bc954aa827ac5b08476be786c92053dddceabb735510bc05fbb464
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral all-Z dicranin
  outcome: supported
  summary: Native encodings, synonym, current ChEBI, exact-key PubChem and LIPID MAPS
    agree; explicit bond numbering confirms the preferred label.
  target_ids:
  - CHEBI:65768
  evidence_ids:
  - native
  - chebi
  - pubchem
  - lipidmaps
  - chemistry
- assessment_id: classification
  area: grounding
  topic: Broader classes and antibacterial role
  outcome: supported
  summary: All four parents are broader structural classes. Purified dicranin activity
    in the primary abstract supports the antibacterial role, with extract-spectrum
    boundaries retained.
  target_ids:
  - CHEBI:65768
  evidence_ids:
  - parent-15904
  - parent-25380
  - parent-59202
  - parent-73155
  - role
  - antibacterial
- assessment_id: definition
  area: evidence
  topic: Isolation and broad antibacterial wording
  outcome: supported
  summary: Exact dicranin was isolated from Dicranum scoparium and shows antibacterial
    activity. The native definition does not assert the extract’s broader organism
    spectrum.
  target_ids:
  - CHEBI:65768
  evidence_ids:
  - native
  - antibacterial
  - chebi
- assessment_id: enzyme
  area: evidence
  topic: Specific lipoxygenase wording
  outcome: unknown
  summary: Current ChEBI explicitly asserts arachidonate15-lipoxygenase inhibition.
    The accessible primary abstract describes soybean15-lpo screening and attributes
    most activity to dicranin, but its exact substrate, enzyme identity, quantitative
    response and purified-compound protocol require full text. Do not promote this
    database wording into a bacterial molecular target.
  target_ids:
  - CHEBI:65768
  evidence_ids:
  - chebi
  - antibacterial
  - adapter
- assessment_id: activity
  area: completeness
  topic: Disc diffusion and negative E.coli boundary
  outcome: unknown
  summary: Qualitative compound-specific activity is supported, but numerical diameters,
    disc loading, strains and methods beyond disc diffusion remain unavailable. A
    future observation must preserve paper-named Streptococcus faecalis and the tested-condition
    E.coli negative result; no MIC can be invented. Empty optional activity rows alone
    are not a defect.
  target_ids:
  - CHEBI:65768
  evidence_ids:
  - antibacterial
  - search
- assessment_id: mechanism
  area: scope
  topic: Antibacterial mechanism versus plant/host assays
  outcome: unknown
  summary: No antibacterial mechanism or target is asserted natively or demonstrated
    by the inspected sources. Soybean enzyme inhibition, host platelet endpoints and
    moss oxylipin metabolism do not establish one.
  target_ids:
  - CHEBI:65768
  evidence_ids:
  - native
  - antibacterial
  - platelets1
  - platelets2
  - oxylipins
- assessment_id: producer
  area: scope
  topic: Isolation versus biosynthesis
  outcome: supported
  summary: Native isolation wording is supported. Moss metabolism of an administered
    labeled substrate is not by itself proof of the enzyme that biosynthesizes dicranin.
  target_ids:
  - CHEBI:65768
  evidence_ids:
  - antibacterial
  - oxylipins
- assessment_id: registry
  area: provenance
  topic: Registry equivalence
  outcome: unknown
  summary: CAS is supported by current ChEBI and primary-index metadata. Independent
    Reaxys structure detail remains unverified; no mismatch is demonstrated.
  target_ids:
  - CHEBI:65768
  evidence_ids:
  - registries
  - chebi
- assessment_id: other
  area: scope
  topic: Resistance, clinical, datasets and causal graphs
  outcome: not_applicable
  summary: No such assertions are native, and the reviewed exact-compound sources
    do not justify adding these claims.
  target_ids:
  - CHEBI:65768
  evidence_ids:
  - native
  - antibacterial
  - platelets1
  - oxylipins
- assessment_id: audit
  area: provenance
  topic: Generated ownership and history
  outcome: supported
  summary: Source date, mint, row, filing, identity and three seed/reseed events agree.
    SEEDED is retained; review does not promote scientific status.
  target_ids:
  - CHEBI:65768
  evidence_ids:
  - native
  - owner
  - chemistry
- assessment_id: schema
  area: schema
  topic: Focused native checks
  outcome: supported
  summary: Schema and strict checks pass.
  target_ids:
  - CHEBI:65768
  evidence_ids:
  - gates
findings: []
actions: []
limitations:
- The original antibacterial paper was available at abstract level; numerical susceptibility
  results, strains, disc loading, controls and detailed enzyme protocol were not verified.
- Native arachidonate15-lipoxygenase wording is a current ChEBI assertion. The accessible
  primary abstract names soybean15-lpo; exact substrate/enzyme mapping needs the original
  methods and cannot establish an antibacterial mechanism.
- Reaxys equivalence remains source-asserted. Bounded search does not establish absence
  of other exact-compound literature.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All captured maintained-input hashes were rechecked unchanged; no native edit or
  curation event was made.
- 'Concrete follow-up: obtain the original Borel1993 assay tables and curate or explicitly
  defer method-qualified dicranin observations, preserving extract-versus-purified
  and negative-result boundaries. Inspect the original enzyme assay before changing
  or expanding the source definition.'
- The historical ad hoc report’s optional-field-based major finding was not adopted;
  optional absence is not a schema or scientific defect by itself.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:65768
- https://doi.org/10.1021/np50097a010
- https://lipidmaps.org/databases/lmsd/LMFA01031109
tags:
- antibacterial
- fatty-acid
- compound-extract-boundary
- seeded
```
