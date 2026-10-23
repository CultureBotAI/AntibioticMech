# Cefodizime: coherent chemical identity with a malformed oxime locant in two source synonyms

- Review: 20261021T113323Z-cefodizime-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T11:08:33Z
- Finished UTC: 2026-10-21T11:33:23Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact neutral cefodizime structure, checked chemical identifiers and antibacterial activity are supported. Two source-imported systematic names display (22Z), requiring a bounded nomenclature check against the intended (2Z) oxime locant. The stored graph is consistently Z; the malformed text is not evidence of a different stereoisomer. Original susceptibility data and patent scope are preserved separately.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position 229; one exact record in path order, captured before judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:63214 | data/antibiotics/antibacterial/cefodizime.yaml | generated | cefodizime |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:63214 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:63214 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:63214 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:63214 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:63214 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:63214 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:63214 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:63214 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:63214 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:63214 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:63214 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:63214 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Maintained sources and history

provenance: supported. Targets: CHEBI:63214.

Source concepts, source-owned assertions and seeding history are coherent. New primary observations require the native validated writer and curation event; source corrections must be reproducible.

### Focused native checks

schema: supported. Targets: CHEBI:63214.

Documented schema and strict validation passed; independent chemistry also passed. Deterministic checks do not establish scientific completeness or native REVIEWED status.

### Exact chemical identity

identity: supported. Targets: CHEBI:63214.

Independent structures and patent compound naming agree with neutral cefodizime, including its Z oxime.

### Systematic-name locant formatting

representation: concern. Targets: CHEBI:63214.

Two exact names contain the malformed (22Z) string; resolve the source notation before normalizing or suppressing the aliases.

### Historical antibacterial experiments

evidence: supported. Targets: CHEBI:63214.

Exact-compound primary assays support antibacterial classification with cohort, material and method limits.

### Mechanism, producer and causal graph

completeness: unknown. Targets: CHEBI:63214.

Optional fields are empty. No named native protein/gene/pathway claim requires the structured adapter. Host immunology or mushroom-enzyme work cannot fill the antibacterial target without independent evidence.

## Findings

### F1: Verify and normalize the (22Z) oxime locant in two exact names

minor / open / provisional; issue key: chebi-63214-malformed-22z-synonym-locant.

Both names place (22Z) in a side chain whose imino carbon is at locant 2. The native graph and independent authorities consistently specify Z. Confirm whether the duplicated 2 arose in source typography or extraction, then supply a verified name or suppress the malformed aliases. No change to native stereochemistry is justified.

## Recommended Actions And Acceptance Checks

### A1

Verify and normalize the (22Z) oxime locant in two exact names

- Compare the original ChEBI nomenclature representation with a verified systematic name; resolve any superscript or markup before replacing (22Z) with (2Z). Do not infer an opposite isomer or racemate from malformed text.
- If the source text is confirmed erroneous, correct its maintained extraction/source representation or add exact source-concept-specific exclusions under CHEBI:63214. Preserve at least a verified exact name and the INN names.
- Use the maintained source/extraction correction or source-specific synonym exclusion; regenerate through the documented seed dry run and exact-record canary. Do not patch generated YAML alone.
- Preserve the independently supported complete structure, charge, stereochemistry and source provenance. Inspect the emitted names, run focused schema/strict, verify-corpus and applicable shared quality gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/cefodizime.yaml; Complete native YAML, all source concepts and every history event. | supports | The complete exact record and all populated assertions were inspected. This observation does not modify the generated record or promote SEEDED status. |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; scripts/seed_from_sources.py; 229-raw-rows.json and actual maintained owner files. | supports | ChEBI supplies identity, names, definition and its document/citation leads; ARO supplies the joined classification and its assertions. Initial hashes are preserved, with actual additional owner inputs appended before detailed judgment. Any correction must survive reseeding. |
| search | 229-local-hits.txt; 229-owner-hits.txt; Exact identifier, label, full key and slug; maintained inputs and related forms. | supports | The ignored-inclusive search distinguished the exact record from related compounds and source references. No exact corrective overlay was identified in the inspected maintained inputs. |
| chemistry | 229-chemistry.json; 227-230-external-chemistry.json; Native SMILES/InChI and independently parsed official PubChem, ChEMBL, KEGG and DrugCentral structures. | supports | Native encodings agree with XDZKBRJLTGRPSS-BGZQYGJUSA-N, C20H20N6O7S4, charge 0 and the retained masses. All inspected independent structure representations agree with the specified stereochemistry. Calculations used the existing batch019 RDKit interpreter against unchanged batch023 inputs. |
| identity | CHEBI:63214; PubChem:5361871; CHEMBL2303613; KEGG:D07643; drugcentral:541; Current ChEBI/OLS, CAS 69739-16-8 resolution and independent official graphs. | supports | The neutral C20H20N6O7S4 structure has two R centers and a Z oxime. Cephalosporin, oxime O-ether and 1,3-thiazole parents fit the graph. Exact chemical structures agree; Reaxys 5789079 was not independently resolved. |
| names | CHEBI:63214; data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/seed_from_sources.py; synonyms[2] and synonyms[3], adopted ChEBI row and current ChEBI display. | supports | Both exact names print (22Z) on the 2-(methoxyimino)acetyl side chain, rather than the expected locant 2. The raw adopted name and current source repeat it. A formatting loss or duplicated character is plausible but its origin is not established. This is a provisional text-normalization finding, not proof of opposite geometry. The existing synonym_exclusions mechanism can suppress a verified malformed alias; no compound-specific exclusion is present. |
| activity | PMID:6295264; DOI:10.1128/AAC.22.4.715; PMC183824; All four original pages 715–718, Methods, Table 1 and discussion visually read. | supports | The study tests 566 clinical isolates collected in 1979–1981 using Hoechst standard powder; the bulk counterion is not specified. MicroMIC2000 broth microdilution used approximately 100000 CFU/mL, with further method details in an earlier reference. MBC subculture used 0.015 mL onto Mueller–Hinton agar. E. coli and K. pneumoniae groups have low MIC90 values, whereas P. aeruginosa, methicillin-resistant S. aureus and S. faecalis groups have much higher values. Table ranges and censored values describe historical cohorts; they are not universal species MICs or present-day breakpoint judgments. |
| other-activity | PMID:6275785; PMID:6092739; PMID:2795858; Complete adopted or exact-compound follow-up abstracts. | supports | The two laboratory studies support organism- and enzyme-dependent antibacterial activity. The pediatric report is a small historical clinical series. Full original methods for these papers were not independently inspected; no all-enzyme stability claim, exact free-acid MIC or modern treatment recommendation is inferred. |
| other-context | PMID:29017833; PMID:21425867; PMID:21518570; PMID:18830875; PMID:11585791; PMID:15673804; PMID:6810737; All other adopted/parent available abstracts or metadata. | supports | These cover allergy, synthetic IgE epitopes, mouse liver chemokine responses, mushroom tyrosinase inhibition and broad beta-lactamase reviews. Mushroom enzyme inhibition and host chemokine effects are not the antibacterial target mechanism. Two parent reviews have no indexed abstracts. |
| patents | https://patents.google.com/patent/BE865632A/en; https://patents.google.com/patent/US4278793A/en; Both titles/metadata/abstracts; US Example 171 and claim 1. | supports | BE865632A concerns new cephalosporin derivatives. US4278793A explicitly names the matching syn-methoximino aminothiazolyl, carboxymethyl-methylthiazolylthio cephalosporin in Example 171 and claim 1. The patent also covers many other derivatives; a syn/anti mixture in another example must not be assigned to cefodizime. Every preparative example and experimental activity table was not audited. |

## Limits And Additional Notes

- Required shared corpus results must be incorporated before final save. Focused success alone does not establish whole-corpus quality.
- No paid source was used. Inaccessible independent registry or article contents remain explicit limits, not evidence of nonexistence.
- Eleven adopted/parent and exact-compound follow-up MED leads were dispositioned: nine available abstracts and two metadata-only parent reviews. The 1982 four-page original was fully read; the 1981 and Japanese antibacterial papers remain abstract-level.
- The 1982 bulk material form and its earlier referenced full method remain unresolved; original table values should not become exact free-acid clinical observations without that qualification.
- The origin of (22Z) is unresolved. This minor provisional finding requests source-text verification, not a chemical-structure correction.
- Reaxys is source-attested only. Patent inspection establishes relevance and the exact US named compound, not every derivative or claim.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T113323Z-cefodizime-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cefodizime: coherent chemical identity with a malformed oxime locant in two
  source synonyms'
started_at: '2026-10-21T11:08:33Z'
finished_at: '2026-10-21T11:33:23Z'
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
summary: The exact neutral cefodizime structure, checked chemical identifiers and
  antibacterial activity are supported. Two source-imported systematic names display
  (22Z), requiring a bounded nomenclature check against the intended (2Z) oxime locant.
  The stored graph is consistently Z; the malformed text is not evidence of a different
  stereoisomer. Original susceptibility data and patent scope are preserved separately.
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
  - path: data/antibiotics/antibacterial/cefodizime.yaml
    sha256: 998567380ebbbc4aa7fda4764b1b30abca6398e47ec4f8370b744578de56645a
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
targets:
- target_id: CHEBI:63214
  path: data/antibiotics/antibacterial/cefodizime.yaml
  label: cefodizime
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
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity and reference leads
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position 229; one exact record in path order,
    captured before judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:63214
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:63214
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    229
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:63214
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefodizime.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:63214
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefodizime.yaml --out /private/tmp/am-review-session/229-strict.tsv
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
  - CHEBI:63214
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
  - CHEBI:63214
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
  - CHEBI:63214
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
  - CHEBI:63214
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
  - CHEBI:63214
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
  - CHEBI:63214
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
  - CHEBI:63214
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
  - CHEBI:63214
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
  - CHEBI:63214
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/cefodizime.yaml
  locator: Complete native YAML, all source concepts and every history event.
  accessed_at: '2026-10-21T11:32:57Z'
  support: supports
  summary: The complete exact record and all populated assertions were inspected.
    This observation does not modify the generated record or promote SEEDED status.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; scripts/seed_from_sources.py
  locator: 229-raw-rows.json and actual maintained owner files.
  accessed_at: '2026-10-21T11:32:57Z'
  support: supports
  summary: ChEBI supplies identity, names, definition and its document/citation leads;
    ARO supplies the joined classification and its assertions. Initial hashes are
    preserved, with actual additional owner inputs appended before detailed judgment.
    Any correction must survive reseeding.
  snapshot_sha256: 9f0cbf727839bf91b65f54cb7378d4f580d1c02540c1e6ce944843e58f7ea6bd
- evidence_id: search
  kind: search
  reference: 229-local-hits.txt; 229-owner-hits.txt
  locator: Exact identifier, label, full key and slug; maintained inputs and related
    forms.
  accessed_at: '2026-10-21T11:32:57Z'
  support: supports
  summary: The ignored-inclusive search distinguished the exact record from related
    compounds and source references. No exact corrective overlay was identified in
    the inspected maintained inputs.
  search_scope: rg --no-ignore --hidden across the isolated worktree, excluding .git
    and .venv internals; exact identifiers, label, key and slug.
  snapshot_sha256: 4e96ed36a0ff590868a50386308260508d1f1ba063cad52b2c640a020bf57658
- evidence_id: chemistry
  kind: validation
  reference: 229-chemistry.json; 227-230-external-chemistry.json
  locator: Native SMILES/InChI and independently parsed official PubChem, ChEMBL,
    KEGG and DrugCentral structures.
  accessed_at: '2026-10-21T11:32:57Z'
  support: supports
  summary: Native encodings agree with XDZKBRJLTGRPSS-BGZQYGJUSA-N, C20H20N6O7S4,
    charge 0 and the retained masses. All inspected independent structure representations
    agree with the specified stereochemistry. Calculations used the existing batch019
    RDKit interpreter against unchanged batch023 inputs.
  snapshot_sha256: 7ba36332f8e33091739e45acaad31ef5ed53e4ce633ff69a1eb9a4c3e40393fc
- evidence_id: identity
  kind: database
  reference: CHEBI:63214; PubChem:5361871; CHEMBL2303613; KEGG:D07643; drugcentral:541
  locator: Current ChEBI/OLS, CAS 69739-16-8 resolution and independent official graphs.
  accessed_at: '2026-10-21T11:32:57Z'
  support: supports
  summary: The neutral C20H20N6O7S4 structure has two R centers and a Z oxime. Cephalosporin,
    oxime O-ether and 1,3-thiazole parents fit the graph. Exact chemical structures
    agree; Reaxys 5789079 was not independently resolved.
  snapshot_sha256: c147e8f647cc217f703e3cd6499e7c9bf9813e061f5f2e807a0d1948e487d742
- evidence_id: names
  kind: record_content
  reference: CHEBI:63214; data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; scripts/seed_from_sources.py
  locator: synonyms[2] and synonyms[3], adopted ChEBI row and current ChEBI display.
  accessed_at: '2026-10-21T11:32:57Z'
  support: supports
  summary: Both exact names print (22Z) on the 2-(methoxyimino)acetyl side chain,
    rather than the expected locant 2. The raw adopted name and current source repeat
    it. A formatting loss or duplicated character is plausible but its origin is not
    established. This is a provisional text-normalization finding, not proof of opposite
    geometry. The existing synonym_exclusions mechanism can suppress a verified malformed
    alias; no compound-specific exclusion is present.
  snapshot_sha256: 9f0cbf727839bf91b65f54cb7378d4f580d1c02540c1e6ce944843e58f7ea6bd
- evidence_id: activity
  kind: primary_source
  reference: PMID:6295264; DOI:10.1128/AAC.22.4.715; PMC183824
  locator: All four original pages 715–718, Methods, Table 1 and discussion visually
    read.
  accessed_at: '2026-10-21T11:32:57Z'
  support: supports
  summary: The study tests 566 clinical isolates collected in 1979–1981 using Hoechst
    standard powder; the bulk counterion is not specified. MicroMIC2000 broth microdilution
    used approximately 100000 CFU/mL, with further method details in an earlier reference.
    MBC subculture used 0.015 mL onto Mueller–Hinton agar. E. coli and K. pneumoniae
    groups have low MIC90 values, whereas P. aeruginosa, methicillin-resistant S.
    aureus and S. faecalis groups have much higher values. Table ranges and censored
    values describe historical cohorts; they are not universal species MICs or present-day
    breakpoint judgments.
  snapshot_sha256: 95599dbce3ab6730f5f7aa172f8c5b88d59bab5451b2fbeccc1bc30fdc6320f6
- evidence_id: other-activity
  kind: primary_source
  reference: PMID:6275785; PMID:6092739; PMID:2795858
  locator: Complete adopted or exact-compound follow-up abstracts.
  accessed_at: '2026-10-21T11:32:57Z'
  support: supports
  summary: The two laboratory studies support organism- and enzyme-dependent antibacterial
    activity. The pediatric report is a small historical clinical series. Full original
    methods for these papers were not independently inspected; no all-enzyme stability
    claim, exact free-acid MIC or modern treatment recommendation is inferred.
  snapshot_sha256: a3c6587ba0dd9b13dc299fe043b6e8362b1b2753fcfa95504729fff4fbb1d788
- evidence_id: other-context
  kind: database
  reference: PMID:29017833; PMID:21425867; PMID:21518570; PMID:18830875; PMID:11585791;
    PMID:15673804; PMID:6810737
  locator: All other adopted/parent available abstracts or metadata.
  accessed_at: '2026-10-21T11:32:57Z'
  support: supports
  summary: These cover allergy, synthetic IgE epitopes, mouse liver chemokine responses,
    mushroom tyrosinase inhibition and broad beta-lactamase reviews. Mushroom enzyme
    inhibition and host chemokine effects are not the antibacterial target mechanism.
    Two parent reviews have no indexed abstracts.
  snapshot_sha256: a3c6587ba0dd9b13dc299fe043b6e8362b1b2753fcfa95504729fff4fbb1d788
- evidence_id: patents
  kind: primary_source
  reference: https://patents.google.com/patent/BE865632A/en; https://patents.google.com/patent/US4278793A/en
  locator: Both titles/metadata/abstracts; US Example 171 and claim 1.
  accessed_at: '2026-10-21T11:32:57Z'
  support: supports
  summary: BE865632A concerns new cephalosporin derivatives. US4278793A explicitly
    names the matching syn-methoximino aminothiazolyl, carboxymethyl-methylthiazolylthio
    cephalosporin in Example 171 and claim 1. The patent also covers many other derivatives;
    a syn/anti mixture in another example must not be assigned to cefodizime. Every
    preparative example and experimental activity table was not audited.
  snapshot_sha256: e227757c94e7bc90acdb90c93369e2797a2b010c88d1f1f833b7ddf4a943d29e
assessments:
- assessment_id: provenance
  area: provenance
  topic: Maintained sources and history
  outcome: supported
  summary: Source concepts, source-owned assertions and seeding history are coherent.
    New primary observations require the native validated writer and curation event;
    source corrections must be reproducible.
  target_ids:
  - CHEBI:63214
  evidence_ids:
  - record
  - owners
  - search
- assessment_id: validation
  area: schema
  topic: Focused native checks
  outcome: supported
  summary: Documented schema and strict validation passed; independent chemistry also
    passed. Deterministic checks do not establish scientific completeness or native
    REVIEWED status.
  target_ids:
  - CHEBI:63214
  evidence_ids:
  - chemistry
- assessment_id: identity
  area: identity
  topic: Exact chemical identity
  outcome: supported
  summary: Independent structures and patent compound naming agree with neutral cefodizime,
    including its Z oxime.
  target_ids:
  - CHEBI:63214
  evidence_ids:
  - identity
  - chemistry
  - patents
- assessment_id: names
  area: representation
  topic: Systematic-name locant formatting
  outcome: concern
  summary: Two exact names contain the malformed (22Z) string; resolve the source
    notation before normalizing or suppressing the aliases.
  target_ids:
  - CHEBI:63214
  evidence_ids:
  - names
  - record
  - identity
- assessment_id: activity
  area: evidence
  topic: Historical antibacterial experiments
  outcome: supported
  summary: Exact-compound primary assays support antibacterial classification with
    cohort, material and method limits.
  target_ids:
  - CHEBI:63214
  evidence_ids:
  - activity
  - other-activity
- assessment_id: optional
  area: completeness
  topic: Mechanism, producer and causal graph
  outcome: unknown
  summary: Optional fields are empty. No named native protein/gene/pathway claim requires
    the structured adapter. Host immunology or mushroom-enzyme work cannot fill the
    antibacterial target without independent evidence.
  target_ids:
  - CHEBI:63214
  evidence_ids:
  - record
  - other-context
findings:
- finding_id: F1
  issue_key: chebi-63214-malformed-22z-synonym-locant
  category: representation
  severity: minor
  status: open
  certainty: provisional
  title: Verify and normalize the (22Z) oxime locant in two exact names
  description: Both names place (22Z) in a side chain whose imino carbon is at locant
    2. The native graph and independent authorities consistently specify Z. Confirm
    whether the duplicated 2 arose in source typography or extraction, then supply
    a verified name or suppress the malformed aliases. No change to native stereochemistry
    is justified.
  target_ids:
  - CHEBI:63214
  field_paths:
  - synonyms[2].synonym_text
  - synonyms[3].synonym_text
  evidence_ids:
  - record
  - owners
  - identity
  - chemistry
  - names
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Existing source-specific synonym_exclusions configuration
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI name provenance
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reproducible source-name extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-specific synonym suppression and native regeneration
  rule_id: 'native-review-checklist: identity, equivalence and accurate names'
  native_severity: minor bounded nomenclature defect
  normalization_reason: The supported molecular graph and exact grounding remain intact;
    the finding concerns specific source-imported name text.
actions:
- action_id: A1
  description: Verify and normalize the (22Z) oxime locant in two exact names
  finding_ids:
  - F1
  target_ids:
  - CHEBI:63214
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Existing source-specific synonym_exclusions configuration
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI name provenance
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reproducible source-name extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Source-specific synonym suppression and native regeneration
  acceptance_checks:
  - Compare the original ChEBI nomenclature representation with a verified systematic
    name; resolve any superscript or markup before replacing (22Z) with (2Z). Do not
    infer an opposite isomer or racemate from malformed text.
  - If the source text is confirmed erroneous, correct its maintained extraction/source
    representation or add exact source-concept-specific exclusions under CHEBI:63214.
    Preserve at least a verified exact name and the INN names.
  - Use the maintained source/extraction correction or source-specific synonym exclusion;
    regenerate through the documented seed dry run and exact-record canary. Do not
    patch generated YAML alone.
  - Preserve the independently supported complete structure, charge, stereochemistry
    and source provenance. Inspect the emitted names, run focused schema/strict, verify-corpus
    and applicable shared quality gates.
limitations:
- Required shared corpus results must be incorporated before final save. Focused success
  alone does not establish whole-corpus quality.
- No paid source was used. Inaccessible independent registry or article contents remain
  explicit limits, not evidence of nonexistence.
- 'Eleven adopted/parent and exact-compound follow-up MED leads were dispositioned:
  nine available abstracts and two metadata-only parent reviews. The 1982 four-page
  original was fully read; the 1981 and Japanese antibacterial papers remain abstract-level.'
- The 1982 bulk material form and its earlier referenced full method remain unresolved;
  original table values should not become exact free-acid clinical observations without
  that qualification.
- The origin of (22Z) is unresolved. This minor provisional finding requests source-text
  verification, not a chemical-structure correction.
- Reaxys is source-attested only. Patent inspection establishes relevance and the
  exact US named compound, not every derivative or claim.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
