# O/129: exact identity and scoped folate, resistance and activity evidence

- Review: 20261021T070119Z-2-4-diamino-6-7-diisopropylpteridine
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T06:53:06Z
- Finished UTC: 2026-10-21T07:01:19Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Neutral O/129 identity and generated provenance are coherent. One minor and one informational, source-specific curation opportunities concern folate-related mechanism/resistance evidence and named-isolate activity with phosphate-salt and disk-dose boundaries. The record appropriately remains SEEDED.

## Scope And Provenance

Complete assessment of one generated record with bounded primary-source follow-up.

Selection: Queue index012, exactly CHEBI:73908; salts and other compounds are evidence-scope context only.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:73908 | data/antibiotics/antibacterial/2-4-diamino-6-7-diisopropylpteridine.yaml | generated | 2,4-diamino-6,7-diisopropylpteridine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Single-record LinkML schema | passed | True | CHEBI:73908 | Focused gate passed with no errors. |
| Single-record strict validation | passed | True | CHEBI:73908 | Focused gate passed with no errors. |
| Official identity and ontology verification | passed | True | CHEBI:73908 | Official ChEBI agrees with the target structure, parents and role; configured filing and mechanism behavior verified. |
| Independent Reaxys destination access | unavailable | False | CHEBI:73908 | Official ChEBI registry assertion verified; independent Reaxys content not inspected. |
| Expression-module adapter applicability | not_applicable | False | CHEBI:73908 | Current record contains no target/protein/pathway expression assertion. Contextual resistance proteins do not create a record-level expression claim. |
| Independent chemistry assertions | passed | False | CHEBI:73908 | Actual executable calculation exited 0 and all structure and identifier assertions passed. |
| Authoritative full QC | failed | True | CHEBI:73908 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:73908 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:73908 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:73908 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:73908 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:73908 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:73908 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:73908 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:73908 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Neutral compound and chemical-form boundary

identity: supported. Targets: CHEBI:73908.

The exact source structure is coherent. Published phosphate-salt tests require retained form context and cannot silently change the neutral target identity or dose basis.

### Vibriostatic classification and source mapping

grounding: supported. Targets: CHEBI:73908.

The role justifies ANTIBACTERIAL but does not assert every Vibrio strain is susceptible. Missing generic antifolate mapping is not a generated-field error.

### Evidence-backed mechanism and resistance follow-up

completeness: concern. Targets: CHEBI:73908.

There is a concrete folate-related mechanism/resistance literature follow-up. DHFR-associated acquired resistance, taxon-specific knockout results and broad antifolate classification are different evidence types and require separate curation.

### Assay and isolate evidence scope

completeness: concern. Targets: CHEBI:73908.

The full2001 source offers an activity/resistant-isolate follow-up only with phosphate-salt scope and disk units. Its plasmid experiment does not validate the separate proposed chromosomal mechanism.

### Other scientific fields

evidence: not_applicable. Targets: CHEBI:73908.

No producer, clinical-use, causal-graph, dataset or protein-example object is asserted. Their absence is not assigned a blanket defect. No commercial general-mechanism narrative is used to populate them.

### Ownership, imported references and history

provenance: supported. Targets: CHEBI:73908.

Adopted identity and seeder history match. The record remains appropriately SEEDED; structural parents and bibliographic leads occupy different roles. Independent Reaxys verification is limited.

### Focused validation

schema: supported. Targets: CHEBI:73908.

Both focused schema gates pass in the new isolated worktree.

## Findings

### F1: Folate-related primary evidence needs a scoped mechanism and resistance assessment

minor / open / confirmed; issue key: chebi-73908-folate-resistance-curation.

Specific accessible resistance and cellular-response studies offer an actionable curation path. The broad antifolate role, resistant DHFR association and protozoal response cannot be collapsed into one universal target claim. The current empty fields assert nothing incorrect.

### F2: A concrete resistant-isolate source needs salt and disk-dose scope before activity extraction

informational / open / confirmed; issue key: chebi-73908-salt-disk-activity-scope.

The inspected source supplies named isolates and an experimental resistance-transfer result. Any enrichment must preserve the tested phosphate salt and disk endpoints instead of converting them into neutral-compound MIC claims. Optional activity absence itself is not a schema error.

## Recommended Actions And Acceptance Checks

### A1

Read the complete folate/resistance primary papers, resolve tested chemical form and organism, and curate only supported mode/target/resistance assertions or an explicit unresolved disposition. Distinguish acquired resistance determinants from direct target-binding experiments.

- Each target or resistance object has exact-compound, taxon and claim-specific primary evidence; no universal DHFR claim is inferred.
- Native validated writer and record_curation_event used; strict validation, verify-corpus and QC pass.

### A2

Determine whether the repository accepts the phosphate-salt assay as evidence on this parent record; retain the chemical form in evidence notes or use the appropriate existing salt record if applicable. Extract the named-isolate disk phenotype only without unsupported MIC conversion.

- Source form, disk loading, medium, incubation, isolate and original phenotype remain traceable.
- The proposed13408 chromosomal explanation is not marked experimentally confirmed.
- Use native validated writer/history and run focused strict, reproducibility and QC gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/2-4-diamino-6-7-diisopropylpteridine.yaml; Complete YAML including all14 aliases, chemical structure and three history events | supports | Exact ChEBI-only neutral O/129 entry with two chemical parents, one vibriostatic role, one Reaxys xref and SEEDED history. There are no activity collections or curator-owned mechanism, target, activity_spectrum, resistance, producer, clinical, dataset or graph assertions. |
| owner | data/raw/chebi_antimicrobials.tsv; CHEBI:73908 row1888; MANIFEST; extractor and seeder ownership; PATHS.tsv | supports | Every seeded identity, structure, alias, parent and xref matches the adopted row. Six publication leads are stored as discovery metadata, not claim evidence. Source version2026-08-30 and exact minted concept agree. Seed-owned changes must use maintained source/extractor or grounding decisions; curator additions belong on the actual record. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:73908; Identity, structure, outgoing relationships, names and registry number | supports | Official identity agrees on neutral C12H18N6, SMILES/InChI, key LIVXWXAMTVJGCO-UHFFFAOYSA-N and masses246.318/246.15929. Both parents, vibriostatic role, displayed synonyms and Reaxys268787 are consistent. ChEBI additionally names antifolate as a biological role; that broad role does not by itself prove a specific binding target. |
| config | conf/sources.yaml; role_to_class line244 and role_to_mode_of_action lines331ff; data/raw/chebi_role_names.tsv | supports | CHEBI:73911 maps to ANTIBACTERIAL. The generic antifolate role CHEBI:73913 is not in the mechanism map; the specific DHPS/DHFR inhibitor roles are. Therefore an empty seeded mode is reproducible, not source drift. Broader chemical parents are not identity xrefs. |
| local-search | CultureBotAI/AntibioticMech; Ignored-inclusive full-worktree exact-target search and expanded alias search | context_only | The broad search found raw/generated/path/queue and research references. Focused searches found no target-specific curator override or historical prose report in the queried curation/reviews/reports scopes. Complete YAML inspection confirms the empty scientific slots. No literature absence is inferred. |
| rubric | docs/CURATION.md; REVIEWED criteria; evidence and resistance scope; native review checklist and schema | supports | A source role can support seed classification without record-level evidence. Optional empty slots are not invalid schema. New target, activity and resistance assertions need claim-specific evidence; acquired strain resistance must remain distinct from a species-wide phenotype. Native status promotion requires an actual curation assessment. |
| hofer | PMID:11394182; https://imsear.searo.who.int/server/api/core/bitstreams/8dd8362b-6071-4f5f-806c-239a651e35e9/content — full paper pp39–42, Methods, Table and Results | supports | The2001 paper tested Sigma O/129 phosphate salt using10/150 µg disks on Mueller-Hinton and nutrient agar. V.cholerae strains12129 and13408 were resistant; the table reports24h susceptibility readings. Only12129 transferred resistance with a147kb plasmid. A chromosomal explanation for13408 is proposed, not demonstrated. These salt/disk results are not a neutral-free-base150 µg/mL MIC and require explicit chemical-form scope before adoption. |
| dhfr | PMID:3260105; https://pubmed.ncbi.nlm.nih.gov/3260105/ — abstract and citation | supports | The1988 study of29 African V.cholerae isolates associates high-level O/129/trimethoprim resistance with a DHFR activity distinct from typeI, using MIC/hybridization evidence. It supports an acquired-resistance mechanism lead; full experimental details and tested chemical form remain unverified. It does not alone prove every sensitive-organism binding interaction. |
| trypanosome | PMID:18557814; https://pmc.ncbi.nlm.nih.gov/articles/PMC2610392/ — Results: Effect of antifolate and PTR1 inhibitors; Table1 and footnote; DOI10.1111/j.1365-2958.2008.06305.x | supports | Inspected source text identifies O/129 by full chemical name and compares bloodstream T.brucei wild type with DHFR–TS knockout lines. O/129 sensitivity changes little, unlike several comparator inhibitors. The paper discusses it as a PTR1 inhibitor. This prevents extrapolating a uniform DHFR-dependent cellular mechanism across taxa; it is not direct bacterial-target evidence. Reagent-form methods were not retrieved. |
| adopted-metadata | PubMed:13132906,1353821,6394970,7165216; PubMed metadata pages; https://www.nature.com/articles/173208b0 preview | context_only | The four adopted leads resolve to differentiation or resistance papers, but PubMed provides no abstracts. The1954 Nature preview describes classification context and does not expose the O/129 experiment. Titles and index terms are not used as proof of an assay or mechanism. |
| indexed-leads | PMID:3008635; PMID:3013828; PMID:13489185; PubMed/PMC indexed abstracts; direct opens returned challenge/empty pages | context_only | Search-discovered primary abstracts point to plasmid/transposon O/129 resistance, typeI DHFR-associated resistance and historical competitive folate antagonism. These remain access-limited discovery leads; the draft does not treat them as full-text proof. The attempted Collier PDF download was HTML, not inspected PDF content. |
| validation | just validate; just validate-strict; Executed from /private/tmp/antibioticmech-record-reviews-002; /private/tmp/am-review-session/012-validation.tsv | supports | Both commands exited0. LinkML reported no issues; strict scanned1 file and0 ERROR rows. |
| independent-chemistry | RDKit local calculation; /private/tmp/am-review-session/012-chemistry.py and 012-chemistry.json | supports | Both encodings reproduce the recorded InChIKey, formula, neutral charge and masses; minted identifier assertion passes. |

## Limits And Additional Notes

- Most older leads were metadata or indexed-abstract only; they are marked discovery context. The2001 full paper and2008 Results/Table1 were inspected. Full bacterial enzyme methods and tested forms remain unresolved.
- Independent Reaxys verification was unavailable; official ChEBI registry provenance was checked.
- Bounded searches do not establish global evidence absence. No paid research or native record edits occurred.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Provenance capture preceded judgment; expanded local inputs retained all original hashes and base revision.
- Hidden and ignored content was included in all searches used for local absence.
- No clinical efficacy or treatment advice follows from diagnostic susceptibility use.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T070119Z-2-4-diamino-6-7-diisopropylpteridine
kind: record
repository: CultureBotAI/AntibioticMech
title: 'O/129: exact identity and scoped folate, resistance and activity evidence'
started_at: '2026-10-21T06:53:06Z'
finished_at: '2026-10-21T07:01:19Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Reviewer did not create or curate this seed and independently
    inspected current sources; agent review is not human scientific sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Neutral O/129 identity and generated provenance are coherent. One minor and
  one informational, source-specific curation opportunities concern folate-related
  mechanism/resistance evidence and named-isolate activity with phosphate-salt and
  disk-dose boundaries. The record appropriately remains SEEDED.
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
  - path: data/antibiotics/antibacterial/2-4-diamino-6-7-diisopropylpteridine.yaml
    sha256: 99ff459c30ccceeff78dc0adba89a57cba45630012af292decf09642268f9575
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
- target_id: CHEBI:73908
  path: data/antibiotics/antibacterial/2-4-diamino-6-7-diisopropylpteridine.yaml
  label: 2,4-diamino-6,7-diisopropylpteridine
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
  description: Complete assessment of one generated record with bounded primary-source
    follow-up.
  selection: Queue index012, exactly CHEBI:73908; salts and other compounds are evidence-scope
    context only.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:73908
  exclusions:
  - target: O/129 salts and comparator antifolates as independent records
    reason: No separate target verdict is assigned; tested form and comparison context
      are preserved.
checks:
- check_id: schema
  name: Single-record LinkML schema
  status: passed
  required: true
  summary: Focused gate passed with no errors.
  target_ids:
  - CHEBI:73908
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/2-4-diamino-6-7-diisopropylpteridine.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Single-record strict validation
  status: passed
  required: true
  summary: Focused gate passed with no errors.
  target_ids:
  - CHEBI:73908
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/2-4-diamino-6-7-diisopropylpteridine.yaml --out
    /private/tmp/am-review-session/012-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: identity
  name: Official identity and ontology verification
  status: passed
  required: true
  summary: Official ChEBI agrees with the target structure, parents and role; configured
    filing and mechanism behavior verified.
  target_ids:
  - CHEBI:73908
  evidence_ids:
  - chebi
  - config
- check_id: reaxys
  name: Independent Reaxys destination access
  status: unavailable
  required: false
  summary: Official ChEBI registry assertion verified; independent Reaxys content
    not inspected.
  target_ids:
  - CHEBI:73908
  evidence_ids:
  - chebi
- check_id: imodulondb
  name: Expression-module adapter applicability
  status: not_applicable
  required: false
  summary: Current record contains no target/protein/pathway expression assertion.
    Contextual resistance proteins do not create a record-level expression claim.
  target_ids:
  - CHEBI:73908
  evidence_ids:
  - record
- check_id: independent-chemistry
  name: Independent chemistry assertions
  status: passed
  required: false
  target_ids:
  - CHEBI:73908
  summary: Actual executable calculation exited 0 and all structure and identifier
    assertions passed.
  command: .venv/bin/python /private/tmp/am-review-session/012-chemistry.py
  exit_code: 0
  evidence_ids:
  - independent-chemistry
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:73908
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
  - CHEBI:73908
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
  - CHEBI:73908
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
  - CHEBI:73908
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
  - CHEBI:73908
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
  - CHEBI:73908
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
  - CHEBI:73908
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
  - CHEBI:73908
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
  - CHEBI:73908
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/2-4-diamino-6-7-diisopropylpteridine.yaml
  locator: Complete YAML including all14 aliases, chemical structure and three history
    events
  accessed_at: '2026-10-21T06:54:54Z'
  support: supports
  summary: Exact ChEBI-only neutral O/129 entry with two chemical parents, one vibriostatic
    role, one Reaxys xref and SEEDED history. There are no activity collections or
    curator-owned mechanism, target, activity_spectrum, resistance, producer, clinical,
    dataset or graph assertions.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: CHEBI:73908 row1888; MANIFEST; extractor and seeder ownership; PATHS.tsv
  accessed_at: '2026-10-21T06:54:54Z'
  support: supports
  summary: Every seeded identity, structure, alias, parent and xref matches the adopted
    row. Six publication leads are stored as discovery metadata, not claim evidence.
    Source version2026-08-30 and exact minted concept agree. Seed-owned changes must
    use maintained source/extractor or grounding decisions; curator additions belong
    on the actual record.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:73908
  locator: Identity, structure, outgoing relationships, names and registry number
  accessed_at: '2026-10-21T06:54:54Z'
  support: supports
  summary: Official identity agrees on neutral C12H18N6, SMILES/InChI, key LIVXWXAMTVJGCO-UHFFFAOYSA-N
    and masses246.318/246.15929. Both parents, vibriostatic role, displayed synonyms
    and Reaxys268787 are consistent. ChEBI additionally names antifolate as a biological
    role; that broad role does not by itself prove a specific binding target.
- evidence_id: config
  kind: record_content
  reference: conf/sources.yaml
  locator: role_to_class line244 and role_to_mode_of_action lines331ff; data/raw/chebi_role_names.tsv
  accessed_at: '2026-10-21T06:54:54Z'
  support: supports
  summary: CHEBI:73911 maps to ANTIBACTERIAL. The generic antifolate role CHEBI:73913
    is not in the mechanism map; the specific DHPS/DHFR inhibitor roles are. Therefore
    an empty seeded mode is reproducible, not source drift. Broader chemical parents
    are not identity xrefs.
- evidence_id: local-search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: Ignored-inclusive full-worktree exact-target search and expanded alias
    search
  accessed_at: '2026-10-21T06:54:54Z'
  support: context_only
  summary: The broad search found raw/generated/path/queue and research references.
    Focused searches found no target-specific curator override or historical prose
    report in the queried curation/reviews/reports scopes. Complete YAML inspection
    confirms the empty scientific slots. No literature absence is inferred.
  search_scope: prepare.py12 used rg --no-ignore --hidden over the worktree, excluding
    .git/.venv. Follow-up rg --no-ignore --hidden -n -F for CHEBI:73908, LIVXWXAMTVJGCO-UHFFFAOYSA-N
    and5a4f687ac6 in raw/curation/reviews/PATHS; alias search -i for vibriostat, O/129
    anddiisopropylpteridine in curation reviews reports/yaml_record_review, excluding
    record_review_queue.tsv. Ignored and hidden files included.
- evidence_id: rubric
  kind: record_content
  reference: docs/CURATION.md
  locator: REVIEWED criteria; evidence and resistance scope; native review checklist
    and schema
  accessed_at: '2026-10-21T06:54:54Z'
  support: supports
  summary: A source role can support seed classification without record-level evidence.
    Optional empty slots are not invalid schema. New target, activity and resistance
    assertions need claim-specific evidence; acquired strain resistance must remain
    distinct from a species-wide phenotype. Native status promotion requires an actual
    curation assessment.
- evidence_id: hofer
  kind: primary_source
  reference: PMID:11394182
  locator: https://imsear.searo.who.int/server/api/core/bitstreams/8dd8362b-6071-4f5f-806c-239a651e35e9/content
    — full paper pp39–42, Methods, Table and Results
  accessed_at: '2026-10-21T06:54:54Z'
  support: supports
  summary: The2001 paper tested Sigma O/129 phosphate salt using10/150 µg disks on
    Mueller-Hinton and nutrient agar. V.cholerae strains12129 and13408 were resistant;
    the table reports24h susceptibility readings. Only12129 transferred resistance
    with a147kb plasmid. A chromosomal explanation for13408 is proposed, not demonstrated.
    These salt/disk results are not a neutral-free-base150 µg/mL MIC and require explicit
    chemical-form scope before adoption.
- evidence_id: dhfr
  kind: primary_source
  reference: PMID:3260105
  locator: https://pubmed.ncbi.nlm.nih.gov/3260105/ — abstract and citation
  accessed_at: '2026-10-21T06:54:54Z'
  support: supports
  summary: The1988 study of29 African V.cholerae isolates associates high-level O/129/trimethoprim
    resistance with a DHFR activity distinct from typeI, using MIC/hybridization evidence.
    It supports an acquired-resistance mechanism lead; full experimental details and
    tested chemical form remain unverified. It does not alone prove every sensitive-organism
    binding interaction.
- evidence_id: trypanosome
  kind: primary_source
  reference: PMID:18557814
  locator: 'https://pmc.ncbi.nlm.nih.gov/articles/PMC2610392/ — Results: Effect of
    antifolate and PTR1 inhibitors; Table1 and footnote; DOI10.1111/j.1365-2958.2008.06305.x'
  accessed_at: '2026-10-21T06:54:54Z'
  support: supports
  summary: Inspected source text identifies O/129 by full chemical name and compares
    bloodstream T.brucei wild type with DHFR–TS knockout lines. O/129 sensitivity
    changes little, unlike several comparator inhibitors. The paper discusses it as
    a PTR1 inhibitor. This prevents extrapolating a uniform DHFR-dependent cellular
    mechanism across taxa; it is not direct bacterial-target evidence. Reagent-form
    methods were not retrieved.
- evidence_id: adopted-metadata
  kind: database
  reference: PubMed:13132906,1353821,6394970,7165216
  locator: PubMed metadata pages; https://www.nature.com/articles/173208b0 preview
  accessed_at: '2026-10-21T06:54:54Z'
  support: context_only
  summary: The four adopted leads resolve to differentiation or resistance papers,
    but PubMed provides no abstracts. The1954 Nature preview describes classification
    context and does not expose the O/129 experiment. Titles and index terms are not
    used as proof of an assay or mechanism.
- evidence_id: indexed-leads
  kind: search
  reference: PMID:3008635; PMID:3013828; PMID:13489185
  locator: PubMed/PMC indexed abstracts; direct opens returned challenge/empty pages
  accessed_at: '2026-10-21T06:54:54Z'
  support: context_only
  summary: Search-discovered primary abstracts point to plasmid/transposon O/129 resistance,
    typeI DHFR-associated resistance and historical competitive folate antagonism.
    These remain access-limited discovery leads; the draft does not treat them as
    full-text proof. The attempted Collier PDF download was HTML, not inspected PDF
    content.
  search_scope: Exact O/129 plus dihydrofolate/antagonism and adopted PMIDs; direct
    PubMed, EuropePMC, PMC and publisher attempts. No paid access or commercial technical-guide
    claims used.
- evidence_id: validation
  kind: validation
  reference: just validate; just validate-strict
  locator: Executed from /private/tmp/antibioticmech-record-reviews-002; /private/tmp/am-review-session/012-validation.tsv
  accessed_at: '2026-10-21T06:54:54Z'
  support: supports
  summary: Both commands exited0. LinkML reported no issues; strict scanned1 file
    and0 ERROR rows.
- evidence_id: independent-chemistry
  kind: validation
  reference: RDKit local calculation
  locator: /private/tmp/am-review-session/012-chemistry.py and 012-chemistry.json
  accessed_at: '2026-10-21T07:01:03Z'
  support: supports
  summary: Both encodings reproduce the recorded InChIKey, formula, neutral charge
    and masses; minted identifier assertion passes.
  snapshot_sha256: f1188db6a8969ddb4947c6f6edf0d530f41263eafac2297a3c259f7647fa18e1
assessments:
- assessment_id: identity
  area: identity
  topic: Neutral compound and chemical-form boundary
  outcome: supported
  summary: The exact source structure is coherent. Published phosphate-salt tests
    require retained form context and cannot silently change the neutral target identity
    or dose basis.
  target_ids:
  - CHEBI:73908
  evidence_ids:
  - record
  - chebi
  - hofer
- assessment_id: classification
  area: grounding
  topic: Vibriostatic classification and source mapping
  outcome: supported
  summary: The role justifies ANTIBACTERIAL but does not assert every Vibrio strain
    is susceptible. Missing generic antifolate mapping is not a generated-field error.
  target_ids:
  - CHEBI:73908
  evidence_ids:
  - chebi
  - config
  - hofer
- assessment_id: mechanism
  area: completeness
  topic: Evidence-backed mechanism and resistance follow-up
  outcome: concern
  summary: There is a concrete folate-related mechanism/resistance literature follow-up.
    DHFR-associated acquired resistance, taxon-specific knockout results and broad
    antifolate classification are different evidence types and require separate curation.
  target_ids:
  - CHEBI:73908
  evidence_ids:
  - record
  - dhfr
  - trypanosome
  - chebi
  - rubric
- assessment_id: activity
  area: completeness
  topic: Assay and isolate evidence scope
  outcome: concern
  summary: The full2001 source offers an activity/resistant-isolate follow-up only
    with phosphate-salt scope and disk units. Its plasmid experiment does not validate
    the separate proposed chromosomal mechanism.
  target_ids:
  - CHEBI:73908
  evidence_ids:
  - record
  - hofer
  - rubric
- assessment_id: optional
  area: evidence
  topic: Other scientific fields
  outcome: not_applicable
  summary: No producer, clinical-use, causal-graph, dataset or protein-example object
    is asserted. Their absence is not assigned a blanket defect. No commercial general-mechanism
    narrative is used to populate them.
  target_ids:
  - CHEBI:73908
  evidence_ids:
  - record
  - rubric
- assessment_id: provenance
  area: provenance
  topic: Ownership, imported references and history
  outcome: supported
  summary: Adopted identity and seeder history match. The record remains appropriately
    SEEDED; structural parents and bibliographic leads occupy different roles. Independent
    Reaxys verification is limited.
  target_ids:
  - CHEBI:73908
  evidence_ids:
  - record
  - owner
  - chebi
- assessment_id: schema
  area: schema
  topic: Focused validation
  outcome: supported
  summary: Both focused schema gates pass in the new isolated worktree.
  target_ids:
  - CHEBI:73908
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: chebi-73908-folate-resistance-curation
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Folate-related primary evidence needs a scoped mechanism and resistance assessment
  description: Specific accessible resistance and cellular-response studies offer
    an actionable curation path. The broad antifolate role, resistant DHFR association
    and protozoal response cannot be collapsed into one universal target claim. The
    current empty fields assert nothing incorrect.
  target_ids:
  - CHEBI:73908
  field_paths:
  - mode_of_action
  - mode_of_action_notes
  - molecular_targets
  - resistance_mechanisms
  evidence_ids:
  - record
  - chebi
  - dhfr
  - trypanosome
  - rubric
  rule_id: native-review-checklist:Mode of action and Resistance
  native_severity: minor evidence-specific readiness gap
  normalization_reason: Specific evidence enables follow-up; no false asserted mechanism,
    identity error or schema violation is present.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2-4-diamino-6-7-diisopropylpteridine.yaml
    role: Curator-owned scientific annotations; use native validated writer and curation
      event
- finding_id: F2
  issue_key: chebi-73908-salt-disk-activity-scope
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: A concrete resistant-isolate source needs salt and disk-dose scope before
    activity extraction
  description: The inspected source supplies named isolates and an experimental resistance-transfer
    result. Any enrichment must preserve the tested phosphate salt and disk endpoints
    instead of converting them into neutral-compound MIC claims. Optional activity
    absence itself is not a schema error.
  target_ids:
  - CHEBI:73908
  field_paths:
  - activity_spectrum
  evidence_ids:
  - record
  - hofer
  - rubric
  rule_id: native-review-checklist:Activity and evidence scope
  native_severity: informational form-aware activity follow-up
  normalization_reason: The tested salt applicability remains unresolved, and the
    current record makes no false activity assertion; this is an evidence-triage opportunity
    rather than a demonstrated defect.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2-4-diamino-6-7-diisopropylpteridine.yaml
    role: Curator-owned scientific annotations; use native validated writer and curation
      event
actions:
- action_id: A1
  description: Read the complete folate/resistance primary papers, resolve tested
    chemical form and organism, and curate only supported mode/target/resistance assertions
    or an explicit unresolved disposition. Distinguish acquired resistance determinants
    from direct target-binding experiments.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:73908
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2-4-diamino-6-7-diisopropylpteridine.yaml
    role: Curator-owned scientific annotations; use native validated writer and curation
      event
  acceptance_checks:
  - Each target or resistance object has exact-compound, taxon and claim-specific
    primary evidence; no universal DHFR claim is inferred.
  - Native validated writer and record_curation_event used; strict validation, verify-corpus
    and QC pass.
- action_id: A2
  description: Determine whether the repository accepts the phosphate-salt assay as
    evidence on this parent record; retain the chemical form in evidence notes or
    use the appropriate existing salt record if applicable. Extract the named-isolate
    disk phenotype only without unsupported MIC conversion.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:73908
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2-4-diamino-6-7-diisopropylpteridine.yaml
    role: Curator-owned scientific annotations; use native validated writer and curation
      event
  acceptance_checks:
  - Source form, disk loading, medium, incubation, isolate and original phenotype
    remain traceable.
  - The proposed13408 chromosomal explanation is not marked experimentally confirmed.
  - Use native validated writer/history and run focused strict, reproducibility and
    QC gates.
limitations:
- Most older leads were metadata or indexed-abstract only; they are marked discovery
  context. The2001 full paper and2008 Results/Table1 were inspected. Full bacterial
  enzyme methods and tested forms remain unresolved.
- Independent Reaxys verification was unavailable; official ChEBI registry provenance
  was checked.
- Bounded searches do not establish global evidence absence. No paid research or native
  record edits occurred.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Provenance capture preceded judgment; expanded local inputs retained all original
  hashes and base revision.
- Hidden and ignored content was included in all searches used for local absence.
- No clinical efficacy or treatment advice follows from diagnostic susceptibility
  use.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:73908
- https://imsear.searo.who.int/server/api/core/bitstreams/8dd8362b-6071-4f5f-806c-239a651e35e9/content
- https://pubmed.ncbi.nlm.nih.gov/3260105/
tags:
- antibacterial
- antifolate
- seeded
- chemical-form-scope
```
