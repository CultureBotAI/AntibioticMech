# 5,6,7-Trimethoxycoumarin: identity, primary activity and assay units

- Review: 20261021T074947Z-5-6-7-trimethoxycoumarin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T07:36:05Z
- Finished UTC: 2026-10-21T07:49:47Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Exact neutral identity and antibacterial classification are supported. One informational follow-up concerns optional assay-specific evidence, with source-unit and extraction limitations preserved. Growth inhibition does not establish a molecular target; other coumarins, plant extracts and kinetic experiments on different compounds cannot supply its mechanism. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole exact native record, all asserted chemical groundings, source provenance and adopted literature scope, with focused primary activity follow-up.

Selection: Initially uncovered queue position046; batch005 target6 in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:28126 | data/antibiotics/antibacterial/5-6-7-trimethoxycoumarin.yaml | generated | 5,6,7-trimethoxycoumarin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema verification | passed | True | CHEBI:28126 | Correctly configured final execution exited0; initial helper mint error is disclosed separately. |
| Focused strict verification | passed | True | CHEBI:28126 | Correctly configured final execution exited0; initial helper mint error is disclosed separately. |
| Focused chemistry verification | passed | False | CHEBI:28126 | Correctly configured final execution exited0; initial helper mint error is disclosed separately. |
| Structured expression-module applicability | not_applicable | False | CHEBI:28126 | Native record names no gene, protein, regulator, pathway, stress response or transcriptomic dataset. |
| Authoritative full QC | failed | True | CHEBI:28126 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:28126 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:28126 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:28126 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:28126 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:28126 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:28126 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:28126 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:28126 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral methoxylated coumarin

identity: supported. Targets: CHEBI:28126.

Definition, aliases, positional substitutions and both native encodings agree. Parent coumarin, hydroxy analogues and plant mixtures remain separate.

### Broader parents and exact references

grounding: supported. Targets: CHEBI:28126.

Both broader parents fit; KEGG/KNApSAcK independently corroborate exact chemical identity and CAS. Reaxys remains an authority assertion with the stated access limit.

### Positive antibacterial role

evidence: supported. Targets: CHEBI:28126.

Exact-compound primary tests support the role. The record itself makes no unsupported quantitative or clinical claim. Before normalized activity entry, preserve method-specific conditions and resolve source-unit/table extraction limits.

### Antimicrobial molecular action

evidence: unknown. Targets: CHEBI:28126.

No native target or mechanism is asserted. Family-level membrane hypotheses and kinetics for other coumarins do not establish a causal mode for this exact compound.

### Producer, resistance, clinical and graph scope

representation: not_applicable. Targets: CHEBI:28126.

Optional objects are absent without an intrinsic defect. Plant isolation does not prove biosynthesis, and whole-extract therapeutic discussion is not clinical efficacy of the isolated molecule.

### Maintained provenance and native status

ownership: supported. Targets: CHEBI:28126.

Imported fields, mint and three seed/reseed events are coherent. Any future scientific enrichment requires validated writer/history; a review does not confer native REVIEWED.

## Findings

### F1: Primary activity offers optional enrichment with unit and assay qualifications

informational / open / confirmed; issue key: chebi-28126-primary-activity-unit-qualified-enrichment.

Exact-compound tests can support future strain-specific activity evidence. The seed does not assert a false measurement or target. Preserve the two assay methods and unresolved extracted molar-unit discrepancy; kinetics and mechanistic hypotheses for other compounds must not transfer.

## Recommended Actions And Acceptance Checks

### A1

If selected for curation, add inspected exact-compound activity with strain, endpoint, medium and assay qualifications, retaining unresolved molecular mechanism.

- Visually verify the original tables and compound mapping before precise quantitative reuse. Retain mass units and resolve the1999 extracted molar-unit discrepancy rather than silently copying or correcting it.
- Keep agar dilution and broth microdilution separate, with organism accessions,24h/48h incubation, medium and complete-growth endpoint. Do not use the pooled abstract range as one target/strain value.
- Do not transfer kinetics from compounds2/4, mixture efficacy, host irritation/cytotoxicity or generic coumarin membrane hypotheses into exact-compound mechanism or clinical claims.
- Require biosynthetic support before producer annotations; plant isolation alone remains occurrence context.
- Use validated writer/history and focused schema/strict, reproduction and required QC; retain native status until sign-off criteria are satisfied.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/5-6-7-trimethoxycoumarin.yaml; Every native YAML field | supports | Read definition, four synonyms, two parents, one activity role, all structure and mass fields, four xrefs, source concept and three seed/reseed events. No mechanism, target, numerical activity, producer, resistance, clinical, graph or dataset object is asserted. Native SEEDED/EXACT remains unchanged. |
| owner | data/raw/chebi_antimicrobials.tsv; Complete CHEBI:28126 row; MANIFEST, PATHS, source configuration, extractor and seeder | supports | Source identity and all imported fields reproduce the seed; five PMIDs are discovery leads and mechanism_role_ids is empty. The source concept and mint are coherent. The maintained mint uses SHA256 of the source/source-ID pair. Imported changes require maintained source ownership; new scientific evidence belongs to the native curator-owned annotations. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:28126; Entire visible official entry;046-chebi.html | supports | The official entry matches all native identity fields, structures, mass values, synonyms and xrefs. CHEBI:23403 coumarins and35618 aromatic ether are broader parents,33282 the antibacterial role. Functional-parent coumarin and non-antimicrobial metabolite role are distinct relationships; they do not supply a direct target. |
| kegg | https://rest.kegg.jp/get/C09313; Complete official compound record including ATOM/BOND | supports | C09313 is the named trimethoxycoumarin with matching formula, exact mass, CAS55085-47-7, ChEBI28126 and KNApSAcKC00002501. Its17-atom/18-bond connectivity fits the neutral methoxylated coumarin. KEGG PubChem11504 is a source-style link and is not added as a native CID. |
| knapsack | https://www.knapsackfamily.com/knapsack_core/information.php?word=C00002501; Complete metabolite identity and occurrence table | supports | The complete SMILES/InChI/key, formula and CAS match the native exact entity. Listed plant occurrences are source context; the table does not alone establish biosynthetic production by every species. |
| chemistry | RDKit independent calculation; chem005.py46;046-chemistry.json | supports | Both encodings yield FOBNRKTURPWTQX-UHFFFAOYSA-N, C12H12O5, charge0, one fragment, average mass236.223, exact mass236.068473484 and no stereocentres. Correct source mint is antibioticmech:chebi-1f00d2b374. No native consistency defect is established. |
| bibliography | Europe PMC core API; 046-epmc.json;PMIDs11295313,14661854,17613825,18058380,9434601 | context_only | All five identifiers resolve and complete abstracts were read. The first two report plant isolation;17613825 assigns the compound as3 but its radical-scavenging result concerns a separate tetrahydrofuran mixture;18058380 reports host irritation/brine-shrimp effects. The1997 antibacterial abstract names the exact compound among individually tested isolates, but its pooled numerical range alone cannot specify a compound/strain measurement. |
| primary1997 | DOI:10.1055/s-2006-957752; PMID9434601;pp508–510, Methods, HPLC mapping and Table2; https://www.researchgate.net/publication/13795084_Antibacterial_Activity_of_Extracts_and_Constituents_of_Pelargonium_sidoides_and_Pelargonium_reniforme | supports | The exact compound is3. Agar-dilution testing reports growth inhibition across eight named bacterial strains, with Table2 mass concentrations500–1000µg/mL for this compound. Methods distinguish24h/48h endpoints at37°C, standard/blood-supplemented Mueller–Hinton and the special Haemophilus medium. Bactericidal-kinetic experiments concern compounds2 and4, not3; their bacteriostatic interpretation cannot be transferred. Root or leaf extraction is not independent biosynthetic proof. |
| primary1999 | DOI:10.1515/znc-1999-3-405; PMID10349736;pp169–172, Methods, TablesI/II and Discussion; https://www.degruyter.com/document/doi/10.1515/znc-1999-3-405/pdf ; https://www.researchgate.net/publication/12948638_Antibacterial_Activity_of_Simple_Coumarins_Structural_Requirements_for_Biological_Activity | partial | TableI identifies the5,6,7-trimethoxy substitution. Broth microdilution tests the same eight-strain panel at37°C/5%CO2. Its extracted TableII pairs4.2 with1000µg/mL and2.1 with500µg/mL while the heading/abstract renders the molar unit asµM. At236.223g/mol, the mass values imply about4.23/2.12mM; retain this discrepancy pending visual/source adjudication. Membrane interaction is a structure–activity hypothesis, with no exact-compound binding or permeability experiment. Kinetic testing again concerns different coumarins. |
| search | Ignored-inclusive local and bounded free primary discovery; 046-local-hits.txt;046-maintained-search.txt | context_only | No exact identifier or minted-ID override appeared in the focused maintained curation/configuration search, which included ignored files. Exact-name activity searches found the inspected1997 and1999 primary studies. Reviews and unrelated coumarin-family mechanisms were not adopted as exact evidence. |

## Limits And Additional Notes

- The1997 primary paper was read through the author-deposited ResearchGate full-text extraction, including Methods, compound mapping, Table2 and Discussion. Direct PDF download failed; no visual table or structure inspection is claimed.
- The1999 primary Methods, TablesI/II and relevant Discussion were read through publisher PDF extraction and publisher-provided ResearchGate text. Subsequent PDF/screenshot retrieval failed or returned an empty file. The displayed molar-unit/mass-unit discrepancy requires visual/source adjudication before quantitative normalization.
- The other four adopted papers were inspected as full abstracts/metadata, not complete experimental texts. Plant isolation, host irritation and brine-shrimp cytotoxicity do not establish this compound’s antimicrobial mechanism.
- Reaxys240375 is corroborated as an official ChEBI assertion, without independent registry inspection.
- The initial scratch chemistry helper used the wrong mint algorithm. After comparison with the maintained seeder, it was corrected to SHA256 of CHEBI&#124;source_id; molecular identity and the correct mint both pass. Initial helper output is retained and is not classified as a native defect.
- Bounded searches do not prove universal absence of additional mechanism, producer or activity evidence. No native edit or paid research occurred.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T074947Z-5-6-7-trimethoxycoumarin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: '5,6,7-Trimethoxycoumarin: identity, primary activity and assay units'
started_at: '2026-10-21T07:36:05Z'
finished_at: '2026-10-21T07:49:47Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the native record. Entire record and
    maintained source were read, chemistry independently recomputed, authoritative
    chemical groundings compared and compound-specific primary activity text inspected.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: Exact neutral identity and antibacterial classification are supported. One
  informational follow-up concerns optional assay-specific evidence, with source-unit
  and extraction limitations preserved. Growth inhibition does not establish a molecular
  target; other coumarins, plant extracts and kinetic experiments on different compounds
  cannot supply its mechanism. Scientific assessment retains the stated evidence limits;
  full verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/5-6-7-trimethoxycoumarin.yaml
    sha256: d29e73ba0811a24609da2cea285bedae3915e2a8630e40940fd25592e3c14cc3
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
- target_id: CHEBI:28126
  path: data/antibiotics/antibacterial/5-6-7-trimethoxycoumarin.yaml
  label: 5,6,7-trimethoxycoumarin
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
  description: Whole exact native record, all asserted chemical groundings, source
    provenance and adopted literature scope, with focused primary activity follow-up.
  selection: Initially uncovered queue position046; batch005 target6 in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:28126
checks:
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Correctly configured final execution exited0; initial helper mint error
    is disclosed separately.
  target_ids:
  - CHEBI:28126
  command: just validate data/antibiotics/antibacterial/5-6-7-trimethoxycoumarin.yaml
  exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Correctly configured final execution exited0; initial helper mint error
    is disclosed separately.
  target_ids:
  - CHEBI:28126
  command: just validate-strict data/antibiotics/antibacterial/5-6-7-trimethoxycoumarin.yaml
    --out /private/tmp/am-review-session/046-strict.tsv
  exit_code: 0
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Correctly configured final execution exited0; initial helper mint error
    is disclosed separately.
  target_ids:
  - CHEBI:28126
  command: .venv/bin/python /private/tmp/am-review-session/chem005.py 46
  exit_code: 0
- check_id: adapter
  name: Structured expression-module applicability
  status: not_applicable
  required: false
  summary: Native record names no gene, protein, regulator, pathway, stress response
    or transcriptomic dataset.
  target_ids:
  - CHEBI:28126
  evidence_ids:
  - record
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:28126
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
  - CHEBI:28126
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
  - CHEBI:28126
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
  - CHEBI:28126
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
  - CHEBI:28126
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
  - CHEBI:28126
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
  - CHEBI:28126
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
  - CHEBI:28126
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
  - CHEBI:28126
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/5-6-7-trimethoxycoumarin.yaml
  locator: Every native YAML field
  accessed_at: '2026-10-21T07:44:18Z'
  support: supports
  summary: Read definition, four synonyms, two parents, one activity role, all structure
    and mass fields, four xrefs, source concept and three seed/reseed events. No mechanism,
    target, numerical activity, producer, resistance, clinical, graph or dataset object
    is asserted. Native SEEDED/EXACT remains unchanged.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Complete CHEBI:28126 row; MANIFEST, PATHS, source configuration, extractor
    and seeder
  accessed_at: '2026-10-21T07:44:18Z'
  support: supports
  summary: Source identity and all imported fields reproduce the seed; five PMIDs
    are discovery leads and mechanism_role_ids is empty. The source concept and mint
    are coherent. The maintained mint uses SHA256 of the source/source-ID pair. Imported
    changes require maintained source ownership; new scientific evidence belongs to
    the native curator-owned annotations.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:28126
  locator: Entire visible official entry;046-chebi.html
  accessed_at: '2026-10-21T07:44:18Z'
  support: supports
  summary: The official entry matches all native identity fields, structures, mass
    values, synonyms and xrefs. CHEBI:23403 coumarins and35618 aromatic ether are
    broader parents,33282 the antibacterial role. Functional-parent coumarin and non-antimicrobial
    metabolite role are distinct relationships; they do not supply a direct target.
  snapshot_sha256: 601ca0945d3ce83f17ba3ebacf38f2d97454806432e11af65dfa26a7462d9d32
- evidence_id: kegg
  kind: database
  reference: https://rest.kegg.jp/get/C09313
  locator: Complete official compound record including ATOM/BOND
  accessed_at: '2026-10-21T07:44:18Z'
  support: supports
  summary: C09313 is the named trimethoxycoumarin with matching formula, exact mass,
    CAS55085-47-7, ChEBI28126 and KNApSAcKC00002501. Its17-atom/18-bond connectivity
    fits the neutral methoxylated coumarin. KEGG PubChem11504 is a source-style link
    and is not added as a native CID.
  snapshot_sha256: 66426f02bf969502bea55751473ba32107061a90695e5f2f2b068b3d4bde07ce
- evidence_id: knapsack
  kind: database
  reference: https://www.knapsackfamily.com/knapsack_core/information.php?word=C00002501
  locator: Complete metabolite identity and occurrence table
  accessed_at: '2026-10-21T07:44:18Z'
  support: supports
  summary: The complete SMILES/InChI/key, formula and CAS match the native exact entity.
    Listed plant occurrences are source context; the table does not alone establish
    biosynthetic production by every species.
  snapshot_sha256: 9531229ae0e62d4cf2bc48744a028d7b5d30039df455e838576684076e4e33a5
- evidence_id: chemistry
  kind: validation
  reference: RDKit independent calculation
  locator: chem005.py46;046-chemistry.json
  accessed_at: '2026-10-21T07:44:18Z'
  support: supports
  summary: Both encodings yield FOBNRKTURPWTQX-UHFFFAOYSA-N, C12H12O5, charge0, one
    fragment, average mass236.223, exact mass236.068473484 and no stereocentres. Correct
    source mint is antibioticmech:chebi-1f00d2b374. No native consistency defect is
    established.
  snapshot_sha256: 7279fc23c0736df99fea282204eb83c6826c4d5edb9718a3ba71582f0a76fab4
- evidence_id: bibliography
  kind: primary_source
  reference: Europe PMC core API
  locator: 046-epmc.json;PMIDs11295313,14661854,17613825,18058380,9434601
  accessed_at: '2026-10-21T07:44:18Z'
  support: context_only
  summary: All five identifiers resolve and complete abstracts were read. The first
    two report plant isolation;17613825 assigns the compound as3 but its radical-scavenging
    result concerns a separate tetrahydrofuran mixture;18058380 reports host irritation/brine-shrimp
    effects. The1997 antibacterial abstract names the exact compound among individually
    tested isolates, but its pooled numerical range alone cannot specify a compound/strain
    measurement.
  snapshot_sha256: aa07a3b0998b6f2406bcd769a92e98c19b7334172c9796a9e969679c16eed45d
- evidence_id: primary1997
  kind: primary_source
  reference: DOI:10.1055/s-2006-957752
  locator: PMID9434601;pp508–510, Methods, HPLC mapping and Table2; https://www.researchgate.net/publication/13795084_Antibacterial_Activity_of_Extracts_and_Constituents_of_Pelargonium_sidoides_and_Pelargonium_reniforme
  accessed_at: '2026-10-21T07:44:18Z'
  support: supports
  summary: The exact compound is3. Agar-dilution testing reports growth inhibition
    across eight named bacterial strains, with Table2 mass concentrations500–1000µg/mL
    for this compound. Methods distinguish24h/48h endpoints at37°C, standard/blood-supplemented
    Mueller–Hinton and the special Haemophilus medium. Bactericidal-kinetic experiments
    concern compounds2 and4, not3; their bacteriostatic interpretation cannot be transferred.
    Root or leaf extraction is not independent biosynthetic proof.
- evidence_id: primary1999
  kind: primary_source
  reference: DOI:10.1515/znc-1999-3-405
  locator: PMID10349736;pp169–172, Methods, TablesI/II and Discussion; https://www.degruyter.com/document/doi/10.1515/znc-1999-3-405/pdf
    ; https://www.researchgate.net/publication/12948638_Antibacterial_Activity_of_Simple_Coumarins_Structural_Requirements_for_Biological_Activity
  accessed_at: '2026-10-21T07:44:18Z'
  support: partial
  summary: TableI identifies the5,6,7-trimethoxy substitution. Broth microdilution
    tests the same eight-strain panel at37°C/5%CO2. Its extracted TableII pairs4.2
    with1000µg/mL and2.1 with500µg/mL while the heading/abstract renders the molar
    unit asµM. At236.223g/mol, the mass values imply about4.23/2.12mM; retain this
    discrepancy pending visual/source adjudication. Membrane interaction is a structure–activity
    hypothesis, with no exact-compound binding or permeability experiment. Kinetic
    testing again concerns different coumarins.
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local and bounded free primary discovery
  locator: 046-local-hits.txt;046-maintained-search.txt
  accessed_at: '2026-10-21T07:44:18Z'
  support: context_only
  summary: No exact identifier or minted-ID override appeared in the focused maintained
    curation/configuration search, which included ignored files. Exact-name activity
    searches found the inspected1997 and1999 primary studies. Reviews and unrelated
    coumarin-family mechanisms were not adopted as exact evidence.
  search_scope: prepare.py46:rg --no-ignore --hidden across batch005 excluding.git/.venv.
    Additional exact CHEBI:28126 and mint search covered curation/decisions.tsv,curation/curator_antibiotics.tsv
    and conf, returning1/no matches. Free public queries used the full systematic
    name with antibacterial/mechanism and the original1997 title; followed official
    publisher and author-deposited primary text. This is bounded discovery, not a
    global absence claim.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral methoxylated coumarin
  outcome: supported
  summary: Definition, aliases, positional substitutions and both native encodings
    agree. Parent coumarin, hydroxy analogues and plant mixtures remain separate.
  target_ids:
  - CHEBI:28126
  evidence_ids:
  - record
  - chebi
  - chemistry
  - knapsack
- assessment_id: grounding
  area: grounding
  topic: Broader parents and exact references
  outcome: supported
  summary: Both broader parents fit; KEGG/KNApSAcK independently corroborate exact
    chemical identity and CAS. Reaxys remains an authority assertion with the stated
    access limit.
  target_ids:
  - CHEBI:28126
  evidence_ids:
  - chebi
  - kegg
  - knapsack
- assessment_id: activity
  area: evidence
  topic: Positive antibacterial role
  outcome: supported
  summary: Exact-compound primary tests support the role. The record itself makes
    no unsupported quantitative or clinical claim. Before normalized activity entry,
    preserve method-specific conditions and resolve source-unit/table extraction limits.
  target_ids:
  - CHEBI:28126
  evidence_ids:
  - record
  - primary1997
  - primary1999
- assessment_id: mechanism
  area: evidence
  topic: Antimicrobial molecular action
  outcome: unknown
  summary: No native target or mechanism is asserted. Family-level membrane hypotheses
    and kinetics for other coumarins do not establish a causal mode for this exact
    compound.
  target_ids:
  - CHEBI:28126
  evidence_ids:
  - record
  - primary1997
  - primary1999
- assessment_id: optional
  area: representation
  topic: Producer, resistance, clinical and graph scope
  outcome: not_applicable
  summary: Optional objects are absent without an intrinsic defect. Plant isolation
    does not prove biosynthesis, and whole-extract therapeutic discussion is not clinical
    efficacy of the isolated molecule.
  target_ids:
  - CHEBI:28126
  evidence_ids:
  - record
  - bibliography
  - primary1997
  - knapsack
- assessment_id: ownership
  area: ownership
  topic: Maintained provenance and native status
  outcome: supported
  summary: Imported fields, mint and three seed/reseed events are coherent. Any future
    scientific enrichment requires validated writer/history; a review does not confer
    native REVIEWED.
  target_ids:
  - CHEBI:28126
  evidence_ids:
  - record
  - owner
  - chemistry
findings:
- finding_id: F1
  issue_key: chebi-28126-primary-activity-unit-qualified-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Primary activity offers optional enrichment with unit and assay qualifications
  description: Exact-compound tests can support future strain-specific activity evidence.
    The seed does not assert a false measurement or target. Preserve the two assay
    methods and unresolved extracted molar-unit discrepancy; kinetics and mechanistic
    hypotheses for other compounds must not transfer.
  target_ids:
  - CHEBI:28126
  field_paths:
  - activity_spectrum
  - evidence
  - mode_of_action_notes
  evidence_ids:
  - record
  - primary1997
  - primary1999
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/5-6-7-trimethoxycoumarin.yaml
    role: Curator-owned claim-level evidence and activity annotations through validated
      writer and native history
  rule_id: native-review-checklist:Activity, Evidence and Mode of action
  native_severity: informational optional primary-evidence enrichment
  normalization_reason: Current identity and role are supported; missing optional
    assays alone are not a scientific defect.
actions:
- action_id: A1
  description: If selected for curation, add inspected exact-compound activity with
    strain, endpoint, medium and assay qualifications, retaining unresolved molecular
    mechanism.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:28126
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/5-6-7-trimethoxycoumarin.yaml
    role: Curator-owned claim-level evidence and activity annotations through validated
      writer and native history
  acceptance_checks:
  - Visually verify the original tables and compound mapping before precise quantitative
    reuse. Retain mass units and resolve the1999 extracted molar-unit discrepancy
    rather than silently copying or correcting it.
  - Keep agar dilution and broth microdilution separate, with organism accessions,24h/48h
    incubation, medium and complete-growth endpoint. Do not use the pooled abstract
    range as one target/strain value.
  - Do not transfer kinetics from compounds2/4, mixture efficacy, host irritation/cytotoxicity
    or generic coumarin membrane hypotheses into exact-compound mechanism or clinical
    claims.
  - Require biosynthetic support before producer annotations; plant isolation alone
    remains occurrence context.
  - Use validated writer/history and focused schema/strict, reproduction and required
    QC; retain native status until sign-off criteria are satisfied.
limitations:
- The1997 primary paper was read through the author-deposited ResearchGate full-text
  extraction, including Methods, compound mapping, Table2 and Discussion. Direct PDF
  download failed; no visual table or structure inspection is claimed.
- The1999 primary Methods, TablesI/II and relevant Discussion were read through publisher
  PDF extraction and publisher-provided ResearchGate text. Subsequent PDF/screenshot
  retrieval failed or returned an empty file. The displayed molar-unit/mass-unit discrepancy
  requires visual/source adjudication before quantitative normalization.
- The other four adopted papers were inspected as full abstracts/metadata, not complete
  experimental texts. Plant isolation, host irritation and brine-shrimp cytotoxicity
  do not establish this compound’s antimicrobial mechanism.
- Reaxys240375 is corroborated as an official ChEBI assertion, without independent
  registry inspection.
- The initial scratch chemistry helper used the wrong mint algorithm. After comparison
  with the maintained seeder, it was corrected to SHA256 of CHEBI|source_id; molecular
  identity and the correct mint both pass. Initial helper output is retained and is
  not classified as a native defect.
- Bounded searches do not prove universal absence of additional mechanism, producer
  or activity evidence. No native edit or paid research occurred.
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
