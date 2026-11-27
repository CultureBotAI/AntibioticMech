# Review of aspyrone

- Review: 20261021T093132Z-aspyrone-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T09:15:49Z
- Finished UTC: 2026-10-21T09:31:32Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Aspyrone identity and all four stereocenters agree with current chemistry sources and primary synthesis/structural literature. Original fungal isolation and nematicidal experiment support the definition. The antibacterial/antifungal roles remain source-supported with only abstract-level access to their key 1998 experiment; derivative,conjugate and host-cell findings are kept distinct. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole ChEBI seed; exact structure,all parent and role assertions,all five adopted PMID records/available abstracts,original synthesis/nematode experiment and bounded related-compound literature.

Selection: Path-ordered queue index 116 prepared and hashed before judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:156387 | data/antibiotics/antibacterial/aspyrone.yaml | generated | aspyrone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema check | passed | True | CHEBI:156387 | Exit 0. |
| Documented strict check | passed | True | CHEBI:156387 | Exit 0;zero ERROR rows. |
| Native and current PubChem chemistry | passed | False | CHEBI:156387 | Exit 0;all four assigned centers,formula,masses and source mint agree. |
| Current ChEBI assertions | passed | False | CHEBI:156387 | Exit 0;parents,roles,synonym,structure and xref strings agree. |
| Native catalog applicability for source biosynthesis lead | passed | False | CHEBI:156387 | Exit 0;catalog checked after a fungal gene lead emerged;fungal organism not covered. Native target had no gene or pathway assertion. |
| Authoritative full QC | failed | True | CHEBI:156387 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:156387 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:156387 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:156387 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:156387 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:156387 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:156387 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:156387 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:156387 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact stereochemical identity

identity: supported. Targets: CHEBI:156387.

Native definition,graph and four configurations agree with primary chemistry.

### Native structure and activity terms

grounding: supported. Targets: CHEBI:156387.

Current ontology reproduces applicable structural/role assertions;both activity classes retained.

### Fungal origin and nematicidal activity

evidence: supported. Targets: CHEBI:156387.

Original cultured-fungus isolation and two-day nematode assay directly support these definition clauses.

### Exact antibacterial/antifungal assay scope

evidence: unknown. Targets: CHEBI:156387.

Abstract supports broad activity but original assay details could not be checked;no contradictory native numerical claim.

### Molecular mechanism

completeness: unknown. Targets: CHEBI:156387.

No validated microbial target established by inspected sources;epoxide rationale and host-cell effects do not fill this gap.

### Adopted citation disposition

provenance: supported. Targets: CHEBI:156387.

All adopted leads scoped;related derivatives and biosynthetic proteins not promoted into targets.

### Focused native gates

schema: supported. Targets: CHEBI:156387.

Schema and strict pass.

## Findings

### F1: Primary evidence can document exact activity and unresolved mechanism

informational / open / confirmed; issue key: chebi-156387-aspyrone-primary-scope-enrichment.

Native identity is coherent and optional claim-level primary evidence is absent. Add the original nematode and chemical-identity evidence and retrieve the exact 1998 antimicrobial assay before quantitative enrichment. Do not borrow activities of chlorinated derivatives or circumdatin conjugates.

## Recommended Actions And Acceptance Checks

### A1

Optionally curate exact primary evidence with explicit source limits.

- Keep all four natural stereocenters and distinguish aspyrone from asperlactone,chlorohydroaspyrones,dihydroaspyrone and conjugates.
- Represent original nematode mortality with species,concentration,24°C and 2-day context;do not convert it into MIC or a microbial endpoint.
- Retrieve and inspect exact 1998 antimicrobial methods/tables before numerical antibacterial/antifungal claims;retain abstract-only qualification until then.
- Do not promote epoxide reactivity or host-cell cytotoxicity into experimentally proven microbial DNA/protein targeting;biosynthetic aomsas is not a susceptibility target.
- Preserve source ownership and complete required native gates before scientific status promotion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/aspyrone.yaml; Complete native YAML including three seed/reseed events | supports | ChEBI-derived SEEDED exact aspyrone has both antibacterial/antifungal roles and a detailed stereochemical definition. No exact target,quantitative assay,producer object or resistance determinant is asserted. |
| sources | CHEBI:156387; 116-ols.json;116-parents.json;116-source-check.json | supports | Current nonobsolete ChEBI reproduces five native parents,two activity roles,the exact synonym,CAS and chemistry. Parent structures match epoxide,secondary alcohol,polyketide and dihydro-2-pyranone. ANTIBACTERIAL follows the local priority while retaining antifungal role. |
| chemistry | RDKit;PubChem exact-name resolution; 116-chemistry.py;116-chemistry.json;116-pubchem.json | supports | Native encodings and current PubChem agree on neutral C9H12O4,RCAULRNMJFUWRP-HETMPLHPSA-N and four assigned centers;formula,masses and ChEBI mint reproduce. |
| synthesis | PMID:8534985; DOI:10.1271/bbb.59.1921;116-primary1995.pdf all four pages visually inspected | supports | Chiral synthesis explicitly targets the 5S,6R,side-chain S,S aspyrone configuration and yields material with spectral/physical agreement to natural aspyrone. Its trans-epoxide is distinguished from the minor cis isomer. This is exact chemistry evidence,not an antimicrobial mechanism experiment. |
| stereochemistry | DOI:10.1039/P19840001021;PMID:31284571; RSC complete1984 abstract;116-primary2019.xml structural Results and X-ray Methods | supports | The 1984 report assigns 5S,6R,8S,9S using degradative optical work with relative X-ray corroboration. The 2019 aspyrone6 crystal agrees;reported absolute-structure parameter 0.0(5) should not be portrayed as independently decisive by itself. Identity is supported jointly with synthesis and earlier work. |
| nematicide | DOI:10.1271/bbb.60.1375; 116-primary1996.pdf both pages visually inspected including table and Methods | supports | Purified aspyrone from Aspergillus melleus culture filtrate produced 39.0% and 80.8% mortality relative to control at 100 and 300 mg/liter after 2 days at 24°C in Pratylenchus penetrans. Acetylaspyrone and other metabolites were separate tests. This is a nematode mortality experiment,not a bacterial MIC or molecular-target assay. |
| antimicrobial | DOI:10.1002/(SICI)1096-9063(199805)53:1&lt;9::AID-PS745&gt;3.0.CO;2-P; Crossref metadata116-primary1998-crossref.json;complete abstract reached from author publication profile at https://www.researchgate.net/publication/247953845_Bactericidal_and_fungicidal_activity_ofAspergillus_ochraceus_metabolites_and_some_derivatives | partial | The original comparative-study abstract reports antibacterial/fungal activity of aspyrone and distinguishes it from asperlactone and derivatives. Full assay methods/tables unavailable;no numerical MIC,MBC,MFC or broad species panel is accepted here. Epoxide-dependent activity is a structure-activity observation,not proof of a specific covalent microbial target. |
| derivatives | PMID:18661951; 116-core.json;complete PubMed/ACS abstract;ACS full-page request403 | context_only | Aspyrone is isolated as compound 3,whereas the abstract antibacterial MICs belong to chlorohydroaspyrones 1 and 2. Those values cannot support an exact aspyrone activity object. |
| host-context | PMID:31284571;PMID:32875235; 116-primary2019.xml;116-primary2020.xml selected exact-compound Results and assay context | context_only | Aspyrone 6 in 2019 has host-cell cytotoxicity,distinct from the conjugates. Epoxide alkylation language is explanatory speculation without a direct DNA/protein adduct assay. Aspyrone 13 in 2020 has limited neutrophil superoxide effect;other compounds account for reported elastase/cancer effects. Neither establishes microbial mechanism. |
| leads | Five adopted ChEBI PMID leads; 116-core.json;116-lead-dispositions.json | context_only | All five indexed records and available abstracts were read. PMID19589392 concerns fungal biosynthetic complementation,not an antimicrobial target. PMID28958507 is chemical-marker detection,not purified antibacterial testing. PMID8534985 lacks indexed abstract but its original four-page paper was read. |
| adapter | Native iModulonDB catalog; 116-imodulondb-datasets.txt | context_only | Executed after source research surfaced aomsas. Aspergillus is outside catalog coverage;no matching query or component summary applies. No gene is asserted in the native record and no expression evidence is used. |
| validation | Documented schema and strict checks; 116-strict.tsv | supports | Both focused native checks pass. |
| search | Ignored-inclusive local search; 116-local-hits.txt;116-inspect.json | context_only | One exact target;all 13 captured input hashes unchanged. |

## Limits And Additional Notes

- All five adopted PMID records/available abstracts read;the missing indexed abstract for PMID8534985 was resolved by reading all four original PDF pages.
- The 1996 nematicide PDF was read in full as page images. The 1984 structural report was abstract-only;2019 structural Results/X-ray Methods and host-cell Results were inspected rather than a full-paper review.
- The 1998 antimicrobial full text was not retrieved:publisher requests failed403/inaccessible URL. DOI metadata resolved without an abstract;the full abstract was read on the publication page linked from an author profile. No author was contacted.
- A guessed ResearchGate URL resolved to an unrelated education paper and was excluded;only the subsequently resolved correct publication page is used.
- ACS2008 full page returned403;its complete abstract was available. Its MIC data are derivative-specific.
- Broader 59-hit search was screened selectively. Diospyrone/asperpyrone and generic efflux papers were excluded as near misses;no claim that no microbial mechanism exists in uninspected literature.
- CAS identity corroborated through current ChEBI;proprietary registry not independently queried.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 13 captured input hashes unchanged;no native record edits.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T093132Z-aspyrone-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of aspyrone
started_at: '2026-10-21T09:15:49Z'
finished_at: '2026-10-21T09:31:32Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
native_verdict: Exact stereochemical identity and fungal origin supported; antimicrobial
  assay detail limited
scientific_review: true
summary: Aspyrone identity and all four stereocenters agree with current chemistry
  sources and primary synthesis/structural literature. Original fungal isolation and
  nematicidal experiment support the definition. The antibacterial/antifungal roles
  remain source-supported with only abstract-level access to their key 1998 experiment;
  derivative,conjugate and host-cell findings are kept distinct. Scientific assessment
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
  - path: data/antibiotics/antibacterial/aspyrone.yaml
    sha256: 0df7272cffbdc0dfbf8b627af9ada8429d3055e641037c224e3edfc80db4cf65
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
  description: Whole ChEBI seed; exact structure,all parent and role assertions,all
    five adopted PMID records/available abstracts,original synthesis/nematode experiment
    and bounded related-compound literature.
  selection: Path-ordered queue index 116 prepared and hashed before judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:156387
targets:
- target_id: CHEBI:156387
  path: data/antibiotics/antibacterial/aspyrone.yaml
  label: aspyrone
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
  name: Documented schema check
  status: passed
  required: true
  summary: Exit 0.
  target_ids:
  - CHEBI:156387
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/aspyrone.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict check
  status: passed
  required: true
  summary: Exit 0;zero ERROR rows.
  target_ids:
  - CHEBI:156387
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/aspyrone.yaml --out /private/tmp/am-review-session/116-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Native and current PubChem chemistry
  status: passed
  required: false
  summary: Exit 0;all four assigned centers,formula,masses and source mint agree.
  target_ids:
  - CHEBI:156387
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/116-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: sources
  name: Current ChEBI assertions
  status: passed
  required: false
  summary: Exit 0;parents,roles,synonym,structure and xref strings agree.
  target_ids:
  - CHEBI:156387
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/116-source-check.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - sources
- check_id: adapter
  name: Native catalog applicability for source biosynthesis lead
  status: passed
  required: false
  summary: Exit 0;catalog checked after a fungal gene lead emerged;fungal organism
    not covered. Native target had no gene or pathway assertion.
  target_ids:
  - CHEBI:156387
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
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
  - CHEBI:156387
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
  - CHEBI:156387
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
  - CHEBI:156387
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
  - CHEBI:156387
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
  - CHEBI:156387
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
  - CHEBI:156387
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
  - CHEBI:156387
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
  - CHEBI:156387
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
  - CHEBI:156387
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/aspyrone.yaml
  locator: Complete native YAML including three seed/reseed events
  accessed_at: '2026-10-21T09:18:45Z'
  support: supports
  summary: ChEBI-derived SEEDED exact aspyrone has both antibacterial/antifungal roles
    and a detailed stereochemical definition. No exact target,quantitative assay,producer
    object or resistance determinant is asserted.
- evidence_id: sources
  kind: database
  reference: CHEBI:156387
  locator: 116-ols.json;116-parents.json;116-source-check.json
  accessed_at: '2026-10-21T09:18:45Z'
  support: supports
  summary: Current nonobsolete ChEBI reproduces five native parents,two activity roles,the
    exact synonym,CAS and chemistry. Parent structures match epoxide,secondary alcohol,polyketide
    and dihydro-2-pyranone. ANTIBACTERIAL follows the local priority while retaining
    antifungal role.
  snapshot_sha256: ec5ac493003a4448989bc6909bd78ff37b64c0a1403c967030b0e82ba9fcb20c
- evidence_id: chemistry
  kind: validation
  reference: RDKit;PubChem exact-name resolution
  locator: 116-chemistry.py;116-chemistry.json;116-pubchem.json
  accessed_at: '2026-10-21T09:18:45Z'
  support: supports
  summary: Native encodings and current PubChem agree on neutral C9H12O4,RCAULRNMJFUWRP-HETMPLHPSA-N
    and four assigned centers;formula,masses and ChEBI mint reproduce.
  snapshot_sha256: bb5ad79014d41ba563d378f1170d62f258492089c5151a0eb4d08c1a848c2f2e
- evidence_id: synthesis
  kind: primary_source
  reference: PMID:8534985
  locator: DOI:10.1271/bbb.59.1921;116-primary1995.pdf all four pages visually inspected
  accessed_at: '2026-10-21T09:18:45Z'
  support: supports
  summary: Chiral synthesis explicitly targets the 5S,6R,side-chain S,S aspyrone configuration
    and yields material with spectral/physical agreement to natural aspyrone. Its
    trans-epoxide is distinguished from the minor cis isomer. This is exact chemistry
    evidence,not an antimicrobial mechanism experiment.
  snapshot_sha256: 3c300b45ff4a6c27ba2c0b177ce7fa1aec571f2b27da4f3eeb1b22bbba714eec
- evidence_id: stereochemistry
  kind: primary_source
  reference: DOI:10.1039/P19840001021;PMID:31284571
  locator: RSC complete1984 abstract;116-primary2019.xml structural Results and X-ray
    Methods
  accessed_at: '2026-10-21T09:18:45Z'
  support: supports
  summary: The 1984 report assigns 5S,6R,8S,9S using degradative optical work with
    relative X-ray corroboration. The 2019 aspyrone6 crystal agrees;reported absolute-structure
    parameter 0.0(5) should not be portrayed as independently decisive by itself.
    Identity is supported jointly with synthesis and earlier work.
  snapshot_sha256: f58278aef1aeb0b9a93ed107df8bec6c3036a4ae11f72d90dee5322e1bd16e65
- evidence_id: nematicide
  kind: primary_source
  reference: DOI:10.1271/bbb.60.1375
  locator: 116-primary1996.pdf both pages visually inspected including table and Methods
  accessed_at: '2026-10-21T09:18:45Z'
  support: supports
  summary: Purified aspyrone from Aspergillus melleus culture filtrate produced 39.0%
    and 80.8% mortality relative to control at 100 and 300 mg/liter after 2 days at
    24°C in Pratylenchus penetrans. Acetylaspyrone and other metabolites were separate
    tests. This is a nematode mortality experiment,not a bacterial MIC or molecular-target
    assay.
  snapshot_sha256: aeeff1074ab29feff67b5422cad03a74c3a59040bfb4489518fa496041f08a21
- evidence_id: antimicrobial
  kind: primary_source
  reference: DOI:10.1002/(SICI)1096-9063(199805)53:1<9::AID-PS745>3.0.CO;2-P
  locator: Crossref metadata116-primary1998-crossref.json;complete abstract reached
    from author publication profile at https://www.researchgate.net/publication/247953845_Bactericidal_and_fungicidal_activity_ofAspergillus_ochraceus_metabolites_and_some_derivatives
  accessed_at: '2026-10-21T09:18:45Z'
  support: partial
  summary: The original comparative-study abstract reports antibacterial/fungal activity
    of aspyrone and distinguishes it from asperlactone and derivatives. Full assay
    methods/tables unavailable;no numerical MIC,MBC,MFC or broad species panel is
    accepted here. Epoxide-dependent activity is a structure-activity observation,not
    proof of a specific covalent microbial target.
  snapshot_sha256: 0a7bab3222fe80f13438eb73506db8ffaeef4ebfa3892e627ab11cc8104bfa0d
- evidence_id: derivatives
  kind: primary_source
  reference: PMID:18661951
  locator: 116-core.json;complete PubMed/ACS abstract;ACS full-page request403
  accessed_at: '2026-10-21T09:18:45Z'
  support: context_only
  summary: Aspyrone is isolated as compound 3,whereas the abstract antibacterial MICs
    belong to chlorohydroaspyrones 1 and 2. Those values cannot support an exact aspyrone
    activity object.
- evidence_id: host-context
  kind: primary_source
  reference: PMID:31284571;PMID:32875235
  locator: 116-primary2019.xml;116-primary2020.xml selected exact-compound Results
    and assay context
  accessed_at: '2026-10-21T09:18:45Z'
  support: context_only
  summary: Aspyrone 6 in 2019 has host-cell cytotoxicity,distinct from the conjugates.
    Epoxide alkylation language is explanatory speculation without a direct DNA/protein
    adduct assay. Aspyrone 13 in 2020 has limited neutrophil superoxide effect;other
    compounds account for reported elastase/cancer effects. Neither establishes microbial
    mechanism.
- evidence_id: leads
  kind: database
  reference: Five adopted ChEBI PMID leads
  locator: 116-core.json;116-lead-dispositions.json
  accessed_at: '2026-10-21T09:18:45Z'
  support: context_only
  summary: All five indexed records and available abstracts were read. PMID19589392
    concerns fungal biosynthetic complementation,not an antimicrobial target. PMID28958507
    is chemical-marker detection,not purified antibacterial testing. PMID8534985 lacks
    indexed abstract but its original four-page paper was read.
  snapshot_sha256: 848e643f2db498e731011fc2076ca6b5f2a6524a9437ea23a38a67a1808ee40b
- evidence_id: adapter
  kind: database
  reference: Native iModulonDB catalog
  locator: 116-imodulondb-datasets.txt
  accessed_at: '2026-10-21T09:18:45Z'
  support: context_only
  summary: Executed after source research surfaced aomsas. Aspergillus is outside
    catalog coverage;no matching query or component summary applies. No gene is asserted
    in the native record and no expression evidence is used.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: validation
  kind: validation
  reference: Documented schema and strict checks
  locator: 116-strict.tsv
  accessed_at: '2026-10-21T09:18:45Z'
  support: supports
  summary: Both focused native checks pass.
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local search
  locator: 116-local-hits.txt;116-inspect.json
  accessed_at: '2026-10-21T09:18:45Z'
  support: context_only
  summary: One exact target;all 13 captured input hashes unchanged.
  search_scope: prepare.py 116 used rg --no-ignore --hidden excluding .git/.venv.
    All 59 broader titles screened;selected relevant abstracts and source sections
    read. No claim of exhaustive full-text coverage.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact stereochemical identity
  outcome: supported
  summary: Native definition,graph and four configurations agree with primary chemistry.
  target_ids:
  - CHEBI:156387
  evidence_ids:
  - chemistry
  - synthesis
  - stereochemistry
- assessment_id: grounding
  area: grounding
  topic: Native structure and activity terms
  outcome: supported
  summary: Current ontology reproduces applicable structural/role assertions;both
    activity classes retained.
  target_ids:
  - CHEBI:156387
  evidence_ids:
  - sources
  - antimicrobial
- assessment_id: origin
  area: evidence
  topic: Fungal origin and nematicidal activity
  outcome: supported
  summary: Original cultured-fungus isolation and two-day nematode assay directly
    support these definition clauses.
  target_ids:
  - CHEBI:156387
  evidence_ids:
  - nematicide
- assessment_id: antimicrobial
  area: evidence
  topic: Exact antibacterial/antifungal assay scope
  outcome: unknown
  summary: Abstract supports broad activity but original assay details could not be
    checked;no contradictory native numerical claim.
  target_ids:
  - CHEBI:156387
  evidence_ids:
  - antimicrobial
  - derivatives
- assessment_id: mechanism
  area: completeness
  topic: Molecular mechanism
  outcome: unknown
  summary: No validated microbial target established by inspected sources;epoxide
    rationale and host-cell effects do not fill this gap.
  target_ids:
  - CHEBI:156387
  evidence_ids:
  - host-context
  - antimicrobial
- assessment_id: provenance
  area: provenance
  topic: Adopted citation disposition
  outcome: supported
  summary: All adopted leads scoped;related derivatives and biosynthetic proteins
    not promoted into targets.
  target_ids:
  - CHEBI:156387
  evidence_ids:
  - leads
  - derivatives
- assessment_id: validation
  area: schema
  topic: Focused native gates
  outcome: supported
  summary: Schema and strict pass.
  target_ids:
  - CHEBI:156387
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: chebi-156387-aspyrone-primary-scope-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Primary evidence can document exact activity and unresolved mechanism
  description: Native identity is coherent and optional claim-level primary evidence
    is absent. Add the original nematode and chemical-identity evidence and retrieve
    the exact 1998 antimicrobial assay before quantitative enrichment. Do not borrow
    activities of chlorinated derivatives or circumdatin conjugates.
  target_ids:
  - CHEBI:156387
  field_paths:
  - evidence
  - activity_spectrum
  - molecular_targets
  - discussions
  evidence_ids:
  - nematicide
  - synthesis
  - antimicrobial
  - derivatives
  - host-context
  rule_id: 'review-checklist: exact identity and narrow evidence scope'
  native_severity: informational optional enrichment
  normalization_reason: No demonstrated native false target or numerical activity
    assertion;unavailable primary assay details remain a limitation.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/aspyrone.yaml
    role: Curator-owned evidence,activity and discussions
actions:
- action_id: A1
  description: Optionally curate exact primary evidence with explicit source limits.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:156387
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/aspyrone.yaml
    role: Curator-owned evidence,activity and discussions
  acceptance_checks:
  - Keep all four natural stereocenters and distinguish aspyrone from asperlactone,chlorohydroaspyrones,dihydroaspyrone
    and conjugates.
  - Represent original nematode mortality with species,concentration,24°C and 2-day
    context;do not convert it into MIC or a microbial endpoint.
  - Retrieve and inspect exact 1998 antimicrobial methods/tables before numerical
    antibacterial/antifungal claims;retain abstract-only qualification until then.
  - Do not promote epoxide reactivity or host-cell cytotoxicity into experimentally
    proven microbial DNA/protein targeting;biosynthetic aomsas is not a susceptibility
    target.
  - Preserve source ownership and complete required native gates before scientific
    status promotion.
limitations:
- All five adopted PMID records/available abstracts read;the missing indexed abstract
  for PMID8534985 was resolved by reading all four original PDF pages.
- The 1996 nematicide PDF was read in full as page images. The 1984 structural report
  was abstract-only;2019 structural Results/X-ray Methods and host-cell Results were
  inspected rather than a full-paper review.
- The 1998 antimicrobial full text was not retrieved:publisher requests failed403/inaccessible
  URL. DOI metadata resolved without an abstract;the full abstract was read on the
  publication page linked from an author profile. No author was contacted.
- A guessed ResearchGate URL resolved to an unrelated education paper and was excluded;only
  the subsequently resolved correct publication page is used.
- ACS2008 full page returned403;its complete abstract was available. Its MIC data
  are derivative-specific.
- Broader 59-hit search was screened selectively. Diospyrone/asperpyrone and generic
  efflux papers were excluded as near misses;no claim that no microbial mechanism
  exists in uninspected literature.
- CAS identity corroborated through current ChEBI;proprietary registry not independently
  queried.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 13 captured input hashes unchanged;no native record edits.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:156387
- https://doi.org/10.1271/bbb.59.1921
- https://doi.org/10.1271/bbb.60.1375
- https://doi.org/10.3390/md17070400
tags:
- record-review
- aspyrone
- stereochemistry
- primary-evidence
```
