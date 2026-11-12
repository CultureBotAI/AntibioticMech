# 1,2-dodecanediol: exact identity and bounded antibacterial evidence review

- Review: 20261021T064400Z-1-2-dodecanediol
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T06:37:32Z
- Finished UTC: 2026-10-21T06:44:00Z
- Reviewer: Codex with dodecanediol_sources research subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact unspecified-stereochemistry diol and its ChEBI antibacterial/antifungal roles are faithfully represented. Primary antibacterial measurements remain uncurated; mechanistic speculation must remain distinct from a demonstrated target. Two minor completeness findings; no identity blocker or unsupported asserted mechanism. Native SEEDED status remains appropriate.

## Scope And Provenance

All fields of the one exact generated record, its adopted ChEBI row, and bounded primary activity/mechanism literature.

Selection: First path lacking a validated structured review target in the sorted data/antibiotics/**/*.yaml corpus at base baf3b3203d748d098686e166cdb2a6138f47eb59: 2939 records, 8 already targeted, 2931 unreviewed. Historical Markdown does not count as structured coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:228133 | data/antibiotics/antibacterial/1-2-dodecanediol.yaml | generated | 1,2-dodecanediol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML record validation | passed | True | CHEBI:228133 | Executed on this exact target; exit0, no validation issues. |
| Closed schema validation | passed | True | CHEBI:228133 | Executed on this exact target; exit0, no validation issues. |
| Structured expression adapter applicability | not_applicable | False | CHEBI:228133 | The record names no gene, locus, protein, regulator, pathway or transcriptomic dataset. Expression-module membership would not validate this chemical structure or MIC. |
| Authoritative full QC | failed | True | CHEBI:228133 | Exited2 at test collection: pinned SciPy1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This is not a scientific failure of this record. |
| Generated corpus reproduction | passed | True | CHEBI:228133 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:228133 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Full closed-schema validation | passed | True | CHEBI:228133 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:228133 | Exited1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:228133 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:228133 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:228133 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. No invented per-record validator. |

## Scientific And Domain Assessments

### Exact charge/stereochemistry, source identity and synonyms

identity: supported. Targets: CHEBI:228133.

Label, formula, neutral charge, unspecified stereochemistry and source concept agree. Neither a salt nor a selected enantiomer is silently substituted.

### Role and parent scope

grounding: supported. Targets: CHEBI:228133.

All three parents are broader classes. Both source activity roles survive ANTIBACTERIAL filing. The antifungal role is a database assertion, not a reassessed experimental claim.

### Strain-specific antibacterial evidence

completeness: concern. Targets: CHEBI:228133.

Exact primary activity is available but not represented as assay-specific observations; the later combination paper is not independent monotherapy replication.

### Mechanism, scope and target confidence

evidence: unknown. Targets: CHEBI:228133.

No mechanism or target is asserted. Published membrane discussion remains hypothetical and does not justify assigning a direct target or microbial selectivity.

### Other optional scientific axes

scope: not_applicable. Targets: CHEBI:228133.

No producer, clinical, dataset, resistance or causal assertion is present to audit. Inspected precursor/reagent literature cannot populate those fields for the parent compound.

### Scientific status and generated ownership

provenance: supported. Targets: CHEBI:228133.

SEEDED and three transparent seed/reseed events accurately describe the record; evidence curation would use native validated writing and events. Seeded identity fixes belong to source/extractor/seeder owners.

## Findings

### activity-gap: Published strain-specific activity is not represented

minor / open / confirmed; issue key: chebi-228133-uncurated-strain-activity.

A concrete optional completeness gap: the inspected exact-compound assay is absent from activity_spectrum. This does not invalidate the existing ChEBI classification or make optional fields schema-required.

### mechanism-gap: Mechanism uncertainty has no explicit discussion

minor / open / confirmed; issue key: chebi-228133-mechanism-review-gap.

Native REVIEWED gate remains unmet. The source does not resolve a molecular mechanism, so a bounded discussion of uncertainty is useful; unsupported target assignment would be worse than the current omission.

## Recommended Actions And Acceptance Checks

### resolve-activity-gap

Curate the two reported strain-specific MIC observations from the primary study, retaining assay, units, solvent, purity and incubation context; keep regrowth distinct from resistance.

- Each new claim cites inspected exact-compound primary evidence and preserves its experimental limits.
- Use record_curation_event and write_validated_antibiotic for any separately authorized curation.
- Run just validate-strict on the target, just verify-corpus --summary and just qc; no native status promotion before all four REVIEWED criteria pass.

### resolve-mechanism-gap

Document the bounded mechanistic uncertainty in a curator-owned discussion. Search exact-compound experiments before any mechanism/target assignment; preserve hypotheses as hypotheses.

- Each new claim cites inspected exact-compound primary evidence and preserves its experimental limits.
- Use record_curation_event and write_validated_antibiotic for any separately authorized curation.
- Run just validate-strict on the target, just verify-corpus --summary and just qc; no native status promotion before all four REVIEWED criteria pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/1-2-dodecanediol.yaml; entire YAML; chemical_structure, source_concepts and curation_history | supports | Entire record read: one exact ChEBI source, five synonyms, two activity roles, three parents, two registry xrefs and three seed/reseed events. There are no asserted molecular-target, activity, resistance, producer, clinical, dataset, causal-graph or mechanism objects. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:228133; Identity, structure, names, ontology and registry sections | supports | Live ChEBI agrees on neutral C12H26O2, InChIKey ZITKDVFRMRXIJQ-UHFFFAOYSA-N, SMILES/InChI, masses, synonyms, CAS1119-87-5 and Reaxys1700179. Parent terms CHEBI:142605/167095/195615 are broader alcohol/diol classes. Roles CHEBI:33282 and CHEBI:35718 denote antibacterial and antifungal agents. No absolute stereoisomer is specified. |
| seed | data/raw/chebi_antimicrobials.tsv; chebi_id=CHEBI:228133; conf/sources.yaml class priorities; seed_from_sources.py mode_of_action_from_roles | supports | The three-star source row agrees with emitted identity and contains five publication leads but no mechanism role. Bacteria-first filing preserves both roles. The seeder emits no mechanism without a mapped role; absent mechanism is not seed drift. Manifest pins the inventory and 2026-08-30 retrieval. |
| chemistry | RDKit 2026.3.5; SMILES and InChI independently parsed; /private/tmp/am-review-session/001-chemistry.json | supports | Both representations regenerate the stored InChIKey. Computed formula C12H26O2, charge0, average mass202.338 and exact mass202.193280072 agree; one unassigned stereocenter remains unassigned, consistent with the source. |
| paper1 | https://www.jstage.jst.go.jp/article/jos/68/8/68_ess19074/_pdf; p760 sections2.1–2.2; p761 sections3.1–3.2, Table1; p761–762 Discussion | supports | The 2019 study tests exact commercial 1,2-dodecanediol: MIC50.0 µg/mL for S. aureus NBRC13276 and S. epidermidis NBRC12993. OD660 broth assay: pH6 buffer, 2% ethanol, 37°C, 24h/48h respectively. Agar regrowth occurred throughout50–400 µg/mL. Material was90% pure. Membrane penetration is proposed, without a compound-specific target experiment. |
| paper2 | https://www.jstage.jst.go.jp/article/jos/70/6/70_ess20362/_pdf; pp788–789 sections2.1–2.5; p790 section3.1/Figure2; p795 Discussion | context_only | The 2021 combination study reuses the 2019 monotherapy MIC and Figure2. Its mixture antagonism is condition-dependent, not a genetic resistance route. Membrane/aggregation explanations remain hypotheses. |
| paper3 | https://pubmed.ncbi.nlm.nih.gov/19820828/; Abstract | context_only | The abstract concerns diamine/amino-alcohol derivatives synthesized from starting alcohols/diol. Derivative antitubercular MICs cannot be assigned to unchanged dodecanediol. |
| paper4 | https://pubmed.ncbi.nlm.nih.gov/21435649/; Abstract | context_only | The abstract uses dodecanediol as a ferrite synthesis reducing reagent; it does not establish antimicrobial activity or mechanism. |
| paper5 | https://pubmed.ncbi.nlm.nih.gov/2245210/; Abstract | context_only | The abstract concerns human erythrocyte hemolysis, not a microbial target. Fluidity observations on named different compounds cannot transfer to dodecanediol. |
| paper6 | https://pubmed.ncbi.nlm.nih.gov/24831550/; Abstract | context_only | The abstract tests diamine/amino-alcohol derivatives against T. cruzi; it does not establish activity of unchanged dodecanediol. |
| search | local repository search; rg --no-ignore --hidden -l -F for identifier, exact label and slug | context_only | Found target, adopted row, generated pages, queues/research ledgers and historical report. Focused ignored-inclusive search of decisions.tsv and curator_antibiotics.tsv found no matching override or curator seed row. Field absence claims describe the read target only. |
| history | reports/yaml_record_review/20260925T020806Z-1-2-dodecanediol.md; Historical ad hoc assessment and source leads | context_only | Read for discovery only; its sources were rechecked and commands rerun. Its absence and severity conclusions are not imported as current facts. |
| rubric | docs/CURATION.md; What a REVIEWED record means; Evidence rules; native checklist | supports | A checked mode is required for native REVIEWED status. Optional fields need not all be populated; quantitative activity and mechanism claims require their own evidence. |

## Limits And Additional Notes

- Primary antifungal support was not established from the six inspected publications; ChEBI supports the database role. This is not a claim that no antifungal evidence exists.
- Reaxys:1700179 was checked as a ChEBI registry assertion, without independent licensed Reaxys access. NIST direct retrieval failed; CAS mapping is supported by inspected ChEBI.
- Four peripheral citations were inspected at abstract level; two Journal of Oleo Science articles were inspected in full. Citation discovery is bounded, not exhaustive.
- No native REVIEWED status promotion; schema/provenance checks do not establish experimental truth.
- Authoritative just qc failed during collection because the pinned SciPy1.15.3 native library has an invalid Mach-O section on this platform; identical pinned version also failed under Python3.10. No dependency versions were changed. Full closed-schema, reproduction and corpus-integrity gates passed independently; these do not replace full QC.
- Source inspection was expanded before saving to include the discovered historical report and curator inventory; all original input hashes remained unchanged.
- No claim is made that absent optional target, producer, clinical, dataset, graph or resistance fields are schema violations.
- Bundle completion is partial because full repository QC is not available on this runtime; the selected record was read and assessed in full. A saved review does not promote scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T064400Z-1-2-dodecanediol
kind: record
repository: CultureBotAI/AntibioticMech
title: '1,2-dodecanediol: exact identity and bounded antibacterial evidence review'
started_at: '2026-10-21T06:37:32Z'
finished_at: '2026-10-21T06:44:00Z'
reviewer:
  identity: Codex with dodecanediol_sources research subagent
  kind: agent
  independence: independent
  independence_basis: Review agents did not create or curate this seeded record. Root
    checked identity and local ownership; research subagent independently inspected
    cited primary sources. This is agent review, not independent human sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The exact unspecified-stereochemistry diol and its ChEBI antibacterial/antifungal
  roles are faithfully represented. Primary antibacterial measurements remain uncurated;
  mechanistic speculation must remain distinct from a demonstrated target. Two minor
  completeness findings; no identity blocker or unsupported asserted mechanism. Native
  SEEDED status remains appropriate.
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
  - path: data/antibiotics/antibacterial/1-2-dodecanediol.yaml
    sha256: 4a47700e02a8a07babaea315e314d8aaa62d41b9dd1df2ab5df808dae9157f97
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
  - path: reports/yaml_record_review/20260925T020806Z-1-2-dodecanediol.md
    sha256: fbb42440f45808d48623758813dd2d748ab21d10e7c28f87d10dfc757be843e9
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
- target_id: CHEBI:228133
  path: data/antibiotics/antibacterial/1-2-dodecanediol.yaml
  label: 1,2-dodecanediol
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted chemical identity, roles and citations
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Upstream ChEBI extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Curator grounding and exclusion decisions
scope:
  description: All fields of the one exact generated record, its adopted ChEBI row,
    and bounded primary activity/mechanism literature.
  selection: 'First path lacking a validated structured review target in the sorted
    data/antibiotics/**/*.yaml corpus at base baf3b3203d748d098686e166cdb2a6138f47eb59:
    2939 records, 8 already targeted, 2931 unreviewed. Historical Markdown does not
    count as structured coverage.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:228133
checks:
- check_id: schema
  name: LinkML record validation
  status: passed
  required: true
  summary: Executed on this exact target; exit0, no validation issues.
  target_ids:
  - CHEBI:228133
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/1-2-dodecanediol.yaml
  exit_code: 0
  evidence_ids:
  - record
- check_id: strict
  name: Closed schema validation
  status: passed
  required: true
  summary: Executed on this exact target; exit0, no validation issues.
  target_ids:
  - CHEBI:228133
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/1-2-dodecanediol.yaml --out /private/tmp/am-review-session/001-strict.tsv
  exit_code: 0
  evidence_ids:
  - record
- check_id: imodulondb
  name: Structured expression adapter applicability
  status: not_applicable
  required: false
  summary: The record names no gene, locus, protein, regulator, pathway or transcriptomic
    dataset. Expression-module membership would not validate this chemical structure
    or MIC.
  target_ids:
  - CHEBI:228133
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited2 at test collection: pinned SciPy1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This is not a scientific
    failure of this record.'
  target_ids:
  - CHEBI:228133
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just qc
  exit_code: 2
  scope_note: Shared execution on unchanged base corpus; applies to the current target
    as part of all2939 records.
- check_id: shared-verify-corpus
  name: Generated corpus reproduction
  status: passed
  required: true
  summary: 2939 expected and present; zero missing, unexpected, drifted fields or
    lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic
    retained.
  target_ids:
  - CHEBI:228133
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just verify-corpus
    --summary
  exit_code: 0
  scope_note: Shared execution on unchanged base corpus; applies to the current target
    as part of all2939 records.
- check_id: shared-review-queue
  name: Native review-readiness inventory
  status: passed
  required: false
  summary: 2859 native unsigned readiness rows written; this status queue does not
    determine structured-review coverage.
  target_ids:
  - CHEBI:228133
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just review-queue
    --limit 0 --tsv /private/tmp/am-review-session/native-queue.tsv
  exit_code: 0
  scope_note: Shared execution on unchanged base corpus; applies to the current target
    as part of all2939 records.
- check_id: shared-validate-all
  name: Full closed-schema validation
  status: passed
  required: true
  summary: 2939 files, zero ERROR rows.
  target_ids:
  - CHEBI:228133
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-all
    --quiet --workers 2 --out /private/tmp/am-review-session/corpus-validation.tsv
  exit_code: 0
  scope_note: Shared execution on unchanged base corpus; applies to the current target
    as part of all2939 records.
- check_id: shared-chemical-map-check
  name: Chemical map consistency
  status: failed
  required: false
  summary: Exited1 on the same pinned SciPy native library import failure.
  target_ids:
  - CHEBI:228133
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just chemical-map-check
  exit_code: 1
  scope_note: Shared execution on unchanged base corpus; applies to the current target
    as part of all2939 records.
- check_id: shared-render-check
  name: Generated site consistency
  status: passed
  required: false
  summary: 2939 compound pages and seven class pages current.
  target_ids:
  - CHEBI:228133
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just render-check
  exit_code: 0
  scope_note: Shared execution on unchanged base corpus; applies to the current target
    as part of all2939 records.
- check_id: shared-report
  name: Corpus statistics
  status: passed
  required: false
  summary: Corpus report completed successfully.
  target_ids:
  - CHEBI:228133
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just report
  exit_code: 0
  scope_note: Shared execution on unchanged base corpus; applies to the current target
    as part of all2939 records.
- check_id: shared-corpus-integrity
  name: Full-corpus history/evidence/reference invariants
  status: passed
  required: true
  summary: 23 full-corpus integrity tests passed, including seed history, evidence
    placement and internal references. No invented per-record validator.
  target_ids:
  - CHEBI:228133
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution on unchanged base corpus; applies to the current target
    as part of all2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/1-2-dodecanediol.yaml
  locator: entire YAML; chemical_structure, source_concepts and curation_history
  accessed_at: '2026-10-21T06:40:52Z'
  support: supports
  summary: 'Entire record read: one exact ChEBI source, five synonyms, two activity
    roles, three parents, two registry xrefs and three seed/reseed events. There are
    no asserted molecular-target, activity, resistance, producer, clinical, dataset,
    causal-graph or mechanism objects.'
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:228133
  locator: Identity, structure, names, ontology and registry sections
  accessed_at: '2026-10-21T06:40:52Z'
  support: supports
  summary: Live ChEBI agrees on neutral C12H26O2, InChIKey ZITKDVFRMRXIJQ-UHFFFAOYSA-N,
    SMILES/InChI, masses, synonyms, CAS1119-87-5 and Reaxys1700179. Parent terms CHEBI:142605/167095/195615
    are broader alcohol/diol classes. Roles CHEBI:33282 and CHEBI:35718 denote antibacterial
    and antifungal agents. No absolute stereoisomer is specified.
- evidence_id: seed
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: chebi_id=CHEBI:228133; conf/sources.yaml class priorities; seed_from_sources.py
    mode_of_action_from_roles
  accessed_at: '2026-10-21T06:40:52Z'
  support: supports
  summary: The three-star source row agrees with emitted identity and contains five
    publication leads but no mechanism role. Bacteria-first filing preserves both
    roles. The seeder emits no mechanism without a mapped role; absent mechanism is
    not seed drift. Manifest pins the inventory and 2026-08-30 retrieval.
- evidence_id: chemistry
  kind: validation
  reference: RDKit 2026.3.5
  locator: SMILES and InChI independently parsed; /private/tmp/am-review-session/001-chemistry.json
  accessed_at: '2026-10-21T06:40:52Z'
  support: supports
  summary: Both representations regenerate the stored InChIKey. Computed formula C12H26O2,
    charge0, average mass202.338 and exact mass202.193280072 agree; one unassigned
    stereocenter remains unassigned, consistent with the source.
- evidence_id: paper1
  kind: primary_source
  reference: https://www.jstage.jst.go.jp/article/jos/68/8/68_ess19074/_pdf
  locator: p760 sections2.1–2.2; p761 sections3.1–3.2, Table1; p761–762 Discussion
  accessed_at: '2026-10-21T06:40:52Z'
  support: supports
  summary: 'The 2019 study tests exact commercial 1,2-dodecanediol: MIC50.0 µg/mL
    for S. aureus NBRC13276 and S. epidermidis NBRC12993. OD660 broth assay: pH6 buffer,
    2% ethanol, 37°C, 24h/48h respectively. Agar regrowth occurred throughout50–400
    µg/mL. Material was90% pure. Membrane penetration is proposed, without a compound-specific
    target experiment.'
- evidence_id: paper2
  kind: primary_source
  reference: https://www.jstage.jst.go.jp/article/jos/70/6/70_ess20362/_pdf
  locator: pp788–789 sections2.1–2.5; p790 section3.1/Figure2; p795 Discussion
  accessed_at: '2026-10-21T06:40:52Z'
  support: context_only
  summary: The 2021 combination study reuses the 2019 monotherapy MIC and Figure2.
    Its mixture antagonism is condition-dependent, not a genetic resistance route.
    Membrane/aggregation explanations remain hypotheses.
- evidence_id: paper3
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/19820828/
  locator: Abstract
  accessed_at: '2026-10-21T06:40:52Z'
  support: context_only
  summary: The abstract concerns diamine/amino-alcohol derivatives synthesized from
    starting alcohols/diol. Derivative antitubercular MICs cannot be assigned to unchanged
    dodecanediol.
- evidence_id: paper4
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/21435649/
  locator: Abstract
  accessed_at: '2026-10-21T06:40:52Z'
  support: context_only
  summary: The abstract uses dodecanediol as a ferrite synthesis reducing reagent;
    it does not establish antimicrobial activity or mechanism.
- evidence_id: paper5
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/2245210/
  locator: Abstract
  accessed_at: '2026-10-21T06:40:52Z'
  support: context_only
  summary: The abstract concerns human erythrocyte hemolysis, not a microbial target.
    Fluidity observations on named different compounds cannot transfer to dodecanediol.
- evidence_id: paper6
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/24831550/
  locator: Abstract
  accessed_at: '2026-10-21T06:40:52Z'
  support: context_only
  summary: The abstract tests diamine/amino-alcohol derivatives against T. cruzi;
    it does not establish activity of unchanged dodecanediol.
- evidence_id: search
  kind: search
  reference: local repository search
  locator: rg --no-ignore --hidden -l -F for identifier, exact label and slug
  accessed_at: '2026-10-21T06:40:52Z'
  support: context_only
  summary: Found target, adopted row, generated pages, queues/research ledgers and
    historical report. Focused ignored-inclusive search of decisions.tsv and curator_antibiotics.tsv
    found no matching override or curator seed row. Field absence claims describe
    the read target only.
  search_scope: Fresh isolated clone, all files including hidden/ignored except .git
    object/history storage and .venv installed dependencies; exact CHEBI:228133, 1,2-dodecanediol,
    1-2-dodecanediol. Focused override search also used minted source ID. Does not
    cover another checkout or unavailable external stores.
- evidence_id: history
  kind: prior_review
  reference: reports/yaml_record_review/20260925T020806Z-1-2-dodecanediol.md
  locator: Historical ad hoc assessment and source leads
  accessed_at: '2026-10-21T06:40:52Z'
  support: context_only
  summary: Read for discovery only; its sources were rechecked and commands rerun.
    Its absence and severity conclusions are not imported as current facts.
- evidence_id: rubric
  kind: authority
  reference: docs/CURATION.md
  locator: What a REVIEWED record means; Evidence rules; native checklist
  accessed_at: '2026-10-21T06:40:52Z'
  support: supports
  summary: A checked mode is required for native REVIEWED status. Optional fields
    need not all be populated; quantitative activity and mechanism claims require
    their own evidence.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact charge/stereochemistry, source identity and synonyms
  outcome: supported
  summary: Label, formula, neutral charge, unspecified stereochemistry and source
    concept agree. Neither a salt nor a selected enantiomer is silently substituted.
  target_ids:
  - CHEBI:228133
  evidence_ids:
  - record
  - chebi
  - chemistry
  - seed
- assessment_id: classification
  area: grounding
  topic: Role and parent scope
  outcome: supported
  summary: All three parents are broader classes. Both source activity roles survive
    ANTIBACTERIAL filing. The antifungal role is a database assertion, not a reassessed
    experimental claim.
  target_ids:
  - CHEBI:228133
  evidence_ids:
  - chebi
  - seed
- assessment_id: activity
  area: completeness
  topic: Strain-specific antibacterial evidence
  outcome: concern
  summary: Exact primary activity is available but not represented as assay-specific
    observations; the later combination paper is not independent monotherapy replication.
  target_ids:
  - CHEBI:228133
  evidence_ids:
  - record
  - paper1
  - paper2
- assessment_id: mechanism
  area: evidence
  topic: Mechanism, scope and target confidence
  outcome: unknown
  summary: No mechanism or target is asserted. Published membrane discussion remains
    hypothetical and does not justify assigning a direct target or microbial selectivity.
  target_ids:
  - CHEBI:228133
  evidence_ids:
  - record
  - paper1
  - paper2
  - paper5
- assessment_id: other-fields
  area: scope
  topic: Other optional scientific axes
  outcome: not_applicable
  summary: No producer, clinical, dataset, resistance or causal assertion is present
    to audit. Inspected precursor/reagent literature cannot populate those fields
    for the parent compound.
  target_ids:
  - CHEBI:228133
  evidence_ids:
  - record
  - paper3
  - paper4
  - paper6
- assessment_id: status
  area: provenance
  topic: Scientific status and generated ownership
  outcome: supported
  summary: SEEDED and three transparent seed/reseed events accurately describe the
    record; evidence curation would use native validated writing and events. Seeded
    identity fixes belong to source/extractor/seeder owners.
  target_ids:
  - CHEBI:228133
  evidence_ids:
  - record
  - seed
  - rubric
findings:
- finding_id: activity-gap
  issue_key: chebi-228133-uncurated-strain-activity
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Published strain-specific activity is not represented
  description: 'A concrete optional completeness gap: the inspected exact-compound
    assay is absent from activity_spectrum. This does not invalidate the existing
    ChEBI classification or make optional fields schema-required.'
  target_ids:
  - CHEBI:228133
  field_paths:
  - activity_spectrum
  evidence_ids:
  - record
  - paper1
  rule_id: 'AntibioticRecord review checklist: Activity/Mode of action/Audit'
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/1-2-dodecanediol.yaml
    role: Future curator-owned activity/evidence/discussion fields; native validated
      writer and curation event required
- finding_id: mechanism-gap
  issue_key: chebi-228133-mechanism-review-gap
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Mechanism uncertainty has no explicit discussion
  description: Native REVIEWED gate remains unmet. The source does not resolve a molecular
    mechanism, so a bounded discussion of uncertainty is useful; unsupported target
    assignment would be worse than the current omission.
  target_ids:
  - CHEBI:228133
  field_paths:
  - mode_of_action
  - discussions
  evidence_ids:
  - record
  - paper1
  - paper2
  - rubric
  rule_id: 'AntibioticRecord review checklist: Activity/Mode of action/Audit'
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/1-2-dodecanediol.yaml
    role: Future curator-owned activity/evidence/discussion fields; native validated
      writer and curation event required
actions:
- action_id: resolve-activity-gap
  description: Curate the two reported strain-specific MIC observations from the primary
    study, retaining assay, units, solvent, purity and incubation context; keep regrowth
    distinct from resistance.
  finding_ids:
  - activity-gap
  target_ids:
  - CHEBI:228133
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/1-2-dodecanediol.yaml
    role: Future curator-owned activity/evidence/discussion fields; native validated
      writer and curation event required
  acceptance_checks:
  - Each new claim cites inspected exact-compound primary evidence and preserves its
    experimental limits.
  - Use record_curation_event and write_validated_antibiotic for any separately authorized
    curation.
  - Run just validate-strict on the target, just verify-corpus --summary and just
    qc; no native status promotion before all four REVIEWED criteria pass.
- action_id: resolve-mechanism-gap
  description: Document the bounded mechanistic uncertainty in a curator-owned discussion.
    Search exact-compound experiments before any mechanism/target assignment; preserve
    hypotheses as hypotheses.
  finding_ids:
  - mechanism-gap
  target_ids:
  - CHEBI:228133
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/1-2-dodecanediol.yaml
    role: Future curator-owned activity/evidence/discussion fields; native validated
      writer and curation event required
  acceptance_checks:
  - Each new claim cites inspected exact-compound primary evidence and preserves its
    experimental limits.
  - Use record_curation_event and write_validated_antibiotic for any separately authorized
    curation.
  - Run just validate-strict on the target, just verify-corpus --summary and just
    qc; no native status promotion before all four REVIEWED criteria pass.
limitations:
- Primary antifungal support was not established from the six inspected publications;
  ChEBI supports the database role. This is not a claim that no antifungal evidence
  exists.
- Reaxys:1700179 was checked as a ChEBI registry assertion, without independent licensed
  Reaxys access. NIST direct retrieval failed; CAS mapping is supported by inspected
  ChEBI.
- Four peripheral citations were inspected at abstract level; two Journal of Oleo
  Science articles were inspected in full. Citation discovery is bounded, not exhaustive.
- No native REVIEWED status promotion; schema/provenance checks do not establish experimental
  truth.
- Authoritative just qc failed during collection because the pinned SciPy1.15.3 native
  library has an invalid Mach-O section on this platform; identical pinned version
  also failed under Python3.10. No dependency versions were changed. Full closed-schema,
  reproduction and corpus-integrity gates passed independently; these do not replace
  full QC.
notes:
- Source inspection was expanded before saving to include the discovered historical
  report and curator inventory; all original input hashes remained unchanged.
- No claim is made that absent optional target, producer, clinical, dataset, graph
  or resistance fields are schema violations.
- Bundle completion is partial because full repository QC is not available on this
  runtime; the selected record was read and assessed in full. A saved review does
  not promote scientific status.
```
