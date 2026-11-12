# Proflavine dihydrochloride: exact salt identity and evidence boundaries

- Review: 20261021T072657Z-proflavine-dihydrochloride-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T07:18:22Z
- Finished UTC: 2026-10-21T07:26:57Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The record faithfully identifies the two-equivalent hydrochloride salt, with consistent structure, formula, mass and source ownership. No confirmed native scientific defect was found. One informational follow-up preserves salt-specific evidence boundaries: the adopted clinical letter is historical exposure/adverse-effect context, the IARC citation is a review of several salts, and generic proflavine or mixed acriflavine experiments cannot automatically establish this exact salt's antibacterial mechanism. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire native record, adopted source row, exact chemical identity, ontology and CAS grounding, cited publication scope and bounded primary discovery.

Selection: Thirtieth initially uncovered record in sorted path order; tenth in batch003.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:74723 | data/antibiotics/antibacterial/3-6-diaminoacridine-dihydrochloride.yaml | generated | 3,6-diaminoacridine dihydrochloride |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema validation | passed | True | CHEBI:74723 | Actual focused execution exited0 with no validation errors. |
| Documented strict validation | passed | True | CHEBI:74723 | Actual focused execution exited0 with no validation errors. |
| Independent salt structure and minted identity consistency | passed | False | CHEBI:74723 | All assertions passed, including salt formula composition and component count. |
| Structured adapter applicability | not_applicable | False | CHEBI:74723 | The native record names no gene, protein, regulator, pathway, stress response or transcriptomic dataset requiring the structured adapter. |
| Authoritative full QC | failed | True | CHEBI:74723 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:74723 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:74723 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:74723 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:74723 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:74723 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:74723 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:74723 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:74723 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact salt identity and component formula

identity: supported. Targets: CHEBI:74723.

Name, definition, aliases, source structure and independent calculations agree on the two-equivalent hydrochloride. Formula notation, net charge and three-component representation are consistent.

### Hydrochloride parent, antibacterial filing and CAS

grounding: supported. Targets: CHEBI:74723.

The broader hydrochloride parent and imported antibacterial role are current authority assertions. CAS531-73-7 is independently corroborated by historical IARC identity. No literature is required merely to reproduce the ontology classification.

### Adopted publication scope

evidence: supported. Targets: CHEBI:74723.

The record does not falsely claim primary mechanistic support. The explicit dihydrochloride letter concerns historical clinical exposure and adverse effects; the second source is a multi-form review.

### Direct antimicrobial target and exact-form mapping

completeness: unknown. Targets: CHEBI:74723.

No direct target is asserted or established by the inspected exact-salt sources. Authority intercalator roles and other salt experiments require explicit chemical/assay mapping before mechanistic enrichment.

### Activity, resistance, producer, clinical and graph objects

representation: not_applicable. Targets: CHEBI:74723.

These optional fields are absent rather than incorrect. Historical use does not establish current approval or efficacy; no producer or resistance determinant is inferred from the dye class.

### Maintained generated inputs and curation state

ownership: supported. Targets: CHEBI:74723.

Source version, minted identity and seed/reseed history are coherent. No curator override was found in the explicitly ignored-inclusive maintained scopes. Native SEEDED status remains unchanged.

## Findings

### F1: Future mechanism curation needs explicit salt and experimental scope

informational / open / confirmed; issue key: chebi-74723-exact-salt-primary-evidence-followup.

The accessible adopted evidence offers historical exact-salt context but no direct antibacterial mechanism. A concrete follow-up is to locate primary reagent-defined studies and map the active chemical form without pooling monohydrochloride, hemisulphate, hydrates or acriflavine mixtures. This is optional enrichment, not a confirmed erroneous native claim.

## Recommended Actions And Acceptance Checks

### A1

If selected for scientific curation, obtain primary reagent-defined antibacterial and binding experiments, document exact salt/preparation and assay chemistry, and attach evidence to the narrowest supported claims. Retain unresolved mechanism where mapping remains uncertain.

- Record counterion, stoichiometry, hydration, mixture composition and experimental solution conditions; cross-form active-moiety inference must be explicit and justified rather than assuming identical chemical identity.
- Separate direct nucleic-acid interaction from causal bacterial killing, mutagenicity, photochemical effects and host-cell endpoints. Do not invent a specific protein target.
- Keep the1972 letter as bounded historical exposure/adverse-effect evidence, without a numerical incidence or current clinical approval claim; do not label IARC review statements as primary experiments.
- Use validated writer and curation history for additions, then focused schema/strict and required corpus gates. Keep native SEEDED until REVIEWED criteria are actually met.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/3-6-diaminoacridine-dihydrochloride.yaml; Every field of generated YAML | supports | Read definition, five exact aliases, hydrochloride parent, antibacterial role, full structure, CAS xref, source concept and three seed/reseed events. SEEDED/EXACT is retained. No molecular mechanism, target, assay, resistance, producer, clinical, dataset or causal graph object is asserted. |
| owner | data/raw/chebi_antimicrobials.tsv; Complete CHEBI:74723 row; source manifest, role mappings, extractor and seeder | supports | Imported name, aliases, parents, role, structure, CAS and source identity agree with the native record. The raw citation leads are PMID4639267 and7009393; mechanism_role_ids is empty. Ignored-inclusive exact-identifier and minted-ID searches in maintained curation tables and conf returned no override. Scientific enrichment is curator-owned; generated identity corrections must reproduce through the maintained source pipeline. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:74723; Full official visible entry;030-chebi.html | supports | The authority agrees on all identity fields, hydrochloride parent CHEBI36807, antibacterial role CHEBI33282 and CAS531-73-7. It explicitly defines two hydrogen-chloride equivalents and distinguishes the mixture CHEBI74728 that contains this salt. Its additional intercalator/antiseptic/carcinogenic roles are not primary evidence and are not all imported by the antimicrobial subset. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/10750; PUG REST formula, InChI, InChIKey and IUPAC name;030-pubchem.json | supports | The official property response agrees on acridine-3,6-diamine dihydrochloride and YHIHFKAEJAVELI-UHFFFAOYSA-N. Its summed elemental formula C13H13Cl2N3 is equivalent to the native component formula C13H11N3.2HCl; the notation difference is not a defect. |
| chemistry | RDKit and hashlib independent calculation; 030-chemistry.py;030-chemistry.json | supports | Both stored encodings independently reproduce YHIHFKAEJAVELI-UHFFFAOYSA-N, summed C13H13Cl2N3, net charge0, three disconnected components, no stereocentres, average mass282.174 and exact mass281.048652776. Minted identifier antibioticmech:chebi-e457b20e3d is reproduced. Neutral base plus two HCl components is the adopted salt encoding; it is not mistaken for a one-equivalent hydrochloride. |
| clinical1972 | DOI:10.1001/archderm.1972.01620150098035; PMID4639267; https://jamanetwork.com/journals/jamadermatology/article-abstract/532968 publisher abstract/excerpt | context_only | Mitchell explicitly names proflavine dihydrochloride and describes historical preoperative skin use and recurrent contact dermatitis. Exposure and affected-patient denominators were not documented. This supports bounded historical exposure context, not a susceptibility measurement, clinical efficacy trial, molecular target or current approved indication. |
| iarc1980 | https://inchem.org/documents/iarc/vol24/proflavin.html; Official IARC historical Summary and Evaluation, Volume24 p195; PMID7009393 metadata identifies a Review;030-iarc.html | context_only | The summary separately lists the free base, dihydrochloride CAS531-73-7, hemisulphate and monohydrochloride CAS952-23-8. Its experimental and evaluation sections cover different forms, and its mutagenicity discussion is not an exact-dihydrochloride antibacterial experiment. It supplies historical context and bibliography leads only; broad review claims are not promoted to primary mechanism evidence. |
| metadata | Europe PMC core API; 030-epmc.json, complete adopted PMID metadata | context_only | Both adopted identifiers resolve to their intended publications. Europe PMC supplies no abstract for either; the primary letter excerpt was therefore read at the publisher and the review summary at IARC. Indexing as a local anti-infective adverse-effect article does not itself prove antibacterial efficacy. |
| hemisulphate | https://discovery.ucl.ac.uk/1367849/1/a12153.pdf; Jones and Neidle1975, Acta Crystallographica B31 p1324; introduction and Experimental sections | context_only | The experiment explicitly crystallizes commercial proflavine hemisulphate from water. Its nucleic-acid-binding background and the distinct crystal structure are not experiments on the native dihydrochloride. The text cites the1974 dihydrochloride-dihydrate study as a separate chemical form. |
| hydrate-lead | Proflavine Dichloride Dihydrate, Obendorf, Carrell and Glusker1974; Acta Crystallographica B30 pp1408–1411; indexed primary PDF text; full retrieval failed | context_only | The title identifies a dichloride-dihydrate crystal study. It remains a discovery lead because full retrieval failed; no formula, detailed structural result or antibacterial inference is adopted from its search snippet. |
| search | Ignored-inclusive local search and bounded public primary discovery; 030-local-hits.txt; focused maintained-override search; exact-salt queries | context_only | Local evidence supports maintained-source reproduction. Public exact-salt searches resolved the historical letter and review, and distinguished other salts, hydrates and mixtures. Generic DNA-binding, phototoxicity or cancer experiments were not automatically assigned to this exact salt. |

## Limits And Additional Notes

- The1972 clinical letter was inspected as the publisher-rendered abstract/excerpt. Direct HTML and preview retrieval returned403; full PDF was not retrieved. It is not evidence of antibacterial potency or a current indication.
- The1980 IARC citation was inspected through its official historical summary and Europe PMC metadata. Full-volume PDF endpoints returned404. It is a review across several chemical forms, not an exact-salt primary mechanism experiment. No current carcinogenicity classification is asserted.
- The1974 dichloride-dihydrate crystal paper was found as indexed primary text but its PDF could not be fetched; the1975 hemisulphate crystal paper was inspected at its introductory/experimental sections. These distinct hydrate/counterion forms were not used to override the native anhydrous salt.
- Bounded searches did not resolve an exact dihydrochloride antibacterial target or quantitative susceptibility experiment. This is not proof that none exists. No paid source, author contact or native record change was used.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T072657Z-proflavine-dihydrochloride-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Proflavine dihydrochloride: exact salt identity and evidence boundaries'
started_at: '2026-10-21T07:18:22Z'
finished_at: '2026-10-21T07:26:57Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the target. Entire record and maintained
    source ownership were inspected; chemistry was independently calculated and cited
    literature was checked at the accessible source level.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: 'The record faithfully identifies the two-equivalent hydrochloride salt,
  with consistent structure, formula, mass and source ownership. No confirmed native
  scientific defect was found. One informational follow-up preserves salt-specific
  evidence boundaries: the adopted clinical letter is historical exposure/adverse-effect
  context, the IARC citation is a review of several salts, and generic proflavine
  or mixed acriflavine experiments cannot automatically establish this exact salt''s
  antibacterial mechanism. Scientific assessment retains the stated evidence limits;
  full verification is blocked by the shared native-library failure.'
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
  - path: data/antibiotics/antibacterial/3-6-diaminoacridine-dihydrochloride.yaml
    sha256: ef5e85075769edcc0102d1e3dfe3a7574b4e2841d27051a089d5b6b9c1f1fc87
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
- target_id: CHEBI:74723
  path: data/antibiotics/antibacterial/3-6-diaminoacridine-dihydrochloride.yaml
  label: 3,6-diaminoacridine dihydrochloride
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
  description: Entire native record, adopted source row, exact chemical identity,
    ontology and CAS grounding, cited publication scope and bounded primary discovery.
  selection: Thirtieth initially uncovered record in sorted path order; tenth in batch003.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:74723
checks:
- check_id: schema
  name: Documented schema validation
  status: passed
  required: true
  summary: Actual focused execution exited0 with no validation errors.
  target_ids:
  - CHEBI:74723
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/3-6-diaminoacridine-dihydrochloride.yaml
  exit_code: 0
- check_id: strict
  name: Documented strict validation
  status: passed
  required: true
  summary: Actual focused execution exited0 with no validation errors.
  target_ids:
  - CHEBI:74723
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/3-6-diaminoacridine-dihydrochloride.yaml --out
    /private/tmp/am-review-session/030-strict.tsv
  exit_code: 0
- check_id: chemistry
  name: Independent salt structure and minted identity consistency
  status: passed
  required: false
  summary: All assertions passed, including salt formula composition and component
    count.
  target_ids:
  - CHEBI:74723
  command: .venv/bin/python /private/tmp/am-review-session/030-chemistry.py
  exit_code: 0
  evidence_ids:
  - chemistry
- check_id: imodulondb
  name: Structured adapter applicability
  status: not_applicable
  required: false
  summary: The native record names no gene, protein, regulator, pathway, stress response
    or transcriptomic dataset requiring the structured adapter.
  target_ids:
  - CHEBI:74723
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
  - CHEBI:74723
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
  - CHEBI:74723
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
  - CHEBI:74723
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
  - CHEBI:74723
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
  - CHEBI:74723
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
  - CHEBI:74723
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
  - CHEBI:74723
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
  - CHEBI:74723
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
  - CHEBI:74723
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/3-6-diaminoacridine-dihydrochloride.yaml
  locator: Every field of generated YAML
  accessed_at: '2026-10-21T07:25:04Z'
  support: supports
  summary: Read definition, five exact aliases, hydrochloride parent, antibacterial
    role, full structure, CAS xref, source concept and three seed/reseed events. SEEDED/EXACT
    is retained. No molecular mechanism, target, assay, resistance, producer, clinical,
    dataset or causal graph object is asserted.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Complete CHEBI:74723 row; source manifest, role mappings, extractor and
    seeder
  accessed_at: '2026-10-21T07:25:04Z'
  support: supports
  summary: Imported name, aliases, parents, role, structure, CAS and source identity
    agree with the native record. The raw citation leads are PMID4639267 and7009393;
    mechanism_role_ids is empty. Ignored-inclusive exact-identifier and minted-ID
    searches in maintained curation tables and conf returned no override. Scientific
    enrichment is curator-owned; generated identity corrections must reproduce through
    the maintained source pipeline.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:74723
  locator: Full official visible entry;030-chebi.html
  accessed_at: '2026-10-21T07:25:04Z'
  support: supports
  summary: The authority agrees on all identity fields, hydrochloride parent CHEBI36807,
    antibacterial role CHEBI33282 and CAS531-73-7. It explicitly defines two hydrogen-chloride
    equivalents and distinguishes the mixture CHEBI74728 that contains this salt.
    Its additional intercalator/antiseptic/carcinogenic roles are not primary evidence
    and are not all imported by the antimicrobial subset.
  snapshot_sha256: 628f791682c554d828823e81ec93cc0a68bfedcd5e3f6e887afdddb6e898e7ff
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/10750
  locator: PUG REST formula, InChI, InChIKey and IUPAC name;030-pubchem.json
  accessed_at: '2026-10-21T07:25:04Z'
  support: supports
  summary: The official property response agrees on acridine-3,6-diamine dihydrochloride
    and YHIHFKAEJAVELI-UHFFFAOYSA-N. Its summed elemental formula C13H13Cl2N3 is equivalent
    to the native component formula C13H11N3.2HCl; the notation difference is not
    a defect.
  snapshot_sha256: ea761defa6142501e765dd728fe46c2607b04997c3746be1af062dbd44f8cb8b
- evidence_id: chemistry
  kind: validation
  reference: RDKit and hashlib independent calculation
  locator: 030-chemistry.py;030-chemistry.json
  accessed_at: '2026-10-21T07:25:04Z'
  support: supports
  summary: Both stored encodings independently reproduce YHIHFKAEJAVELI-UHFFFAOYSA-N,
    summed C13H13Cl2N3, net charge0, three disconnected components, no stereocentres,
    average mass282.174 and exact mass281.048652776. Minted identifier antibioticmech:chebi-e457b20e3d
    is reproduced. Neutral base plus two HCl components is the adopted salt encoding;
    it is not mistaken for a one-equivalent hydrochloride.
  snapshot_sha256: e134797097ab23e3b94f679fb0d525e9788b7aa5f6871472059b4a874d277803
- evidence_id: clinical1972
  kind: primary_source
  reference: DOI:10.1001/archderm.1972.01620150098035
  locator: PMID4639267; https://jamanetwork.com/journals/jamadermatology/article-abstract/532968
    publisher abstract/excerpt
  accessed_at: '2026-10-21T07:25:04Z'
  support: context_only
  summary: Mitchell explicitly names proflavine dihydrochloride and describes historical
    preoperative skin use and recurrent contact dermatitis. Exposure and affected-patient
    denominators were not documented. This supports bounded historical exposure context,
    not a susceptibility measurement, clinical efficacy trial, molecular target or
    current approved indication.
- evidence_id: iarc1980
  kind: database
  reference: https://inchem.org/documents/iarc/vol24/proflavin.html
  locator: Official IARC historical Summary and Evaluation, Volume24 p195; PMID7009393
    metadata identifies a Review;030-iarc.html
  accessed_at: '2026-10-21T07:25:04Z'
  support: context_only
  summary: The summary separately lists the free base, dihydrochloride CAS531-73-7,
    hemisulphate and monohydrochloride CAS952-23-8. Its experimental and evaluation
    sections cover different forms, and its mutagenicity discussion is not an exact-dihydrochloride
    antibacterial experiment. It supplies historical context and bibliography leads
    only; broad review claims are not promoted to primary mechanism evidence.
  snapshot_sha256: a872b773c77a326cb89311ecd1b1de9389530046eb463cf8cff380726f2d66cf
- evidence_id: metadata
  kind: database
  reference: Europe PMC core API
  locator: 030-epmc.json, complete adopted PMID metadata
  accessed_at: '2026-10-21T07:25:04Z'
  support: context_only
  summary: Both adopted identifiers resolve to their intended publications. Europe
    PMC supplies no abstract for either; the primary letter excerpt was therefore
    read at the publisher and the review summary at IARC. Indexing as a local anti-infective
    adverse-effect article does not itself prove antibacterial efficacy.
  snapshot_sha256: 25529059edc6323c73a39f85496a11bc36469a96ba738ea9cc60e2a5d1e62fdd
- evidence_id: hemisulphate
  kind: primary_source
  reference: https://discovery.ucl.ac.uk/1367849/1/a12153.pdf
  locator: Jones and Neidle1975, Acta Crystallographica B31 p1324; introduction and
    Experimental sections
  accessed_at: '2026-10-21T07:25:04Z'
  support: context_only
  summary: The experiment explicitly crystallizes commercial proflavine hemisulphate
    from water. Its nucleic-acid-binding background and the distinct crystal structure
    are not experiments on the native dihydrochloride. The text cites the1974 dihydrochloride-dihydrate
    study as a separate chemical form.
- evidence_id: hydrate-lead
  kind: search
  reference: Proflavine Dichloride Dihydrate, Obendorf, Carrell and Glusker1974
  locator: Acta Crystallographica B30 pp1408–1411; indexed primary PDF text; full
    retrieval failed
  accessed_at: '2026-10-21T07:25:04Z'
  support: context_only
  summary: The title identifies a dichloride-dihydrate crystal study. It remains a
    discovery lead because full retrieval failed; no formula, detailed structural
    result or antibacterial inference is adopted from its search snippet.
  search_scope: Exact-title search and attempted free indexed PDF retrieval at electronicsandbooks.com;
    network/timeout failure prevented full PDF inspection.
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local search and bounded public primary discovery
  locator: 030-local-hits.txt; focused maintained-override search; exact-salt queries
  accessed_at: '2026-10-21T07:25:04Z'
  support: context_only
  summary: Local evidence supports maintained-source reproduction. Public exact-salt
    searches resolved the historical letter and review, and distinguished other salts,
    hydrates and mixtures. Generic DNA-binding, phototoxicity or cancer experiments
    were not automatically assigned to this exact salt.
  search_scope: rg --no-ignore --hidden exact identifier/full label/slug across worktree003
    excluding .git and .venv; exact CHEBI74723 and minted ID in curation/decisions.tsv,
    curation/curator_antibiotics.tsv and conf. Free web queries combined proflavine
    dihydrochloride with antibacterial, MIC, DNA binding, Peacocke and the adopted
    letter title. Official ChEBI, PubChem, Europe PMC, JAMA publisher excerpt, IARC
    summary and accessible primary crystal-paper sections were inspected. Search is
    bounded, not an exhaustive absence proof.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact salt identity and component formula
  outcome: supported
  summary: Name, definition, aliases, source structure and independent calculations
    agree on the two-equivalent hydrochloride. Formula notation, net charge and three-component
    representation are consistent.
  target_ids:
  - CHEBI:74723
  evidence_ids:
  - record
  - chebi
  - pubchem
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Hydrochloride parent, antibacterial filing and CAS
  outcome: supported
  summary: The broader hydrochloride parent and imported antibacterial role are current
    authority assertions. CAS531-73-7 is independently corroborated by historical
    IARC identity. No literature is required merely to reproduce the ontology classification.
  target_ids:
  - CHEBI:74723
  evidence_ids:
  - record
  - chebi
  - iarc1980
- assessment_id: evidence
  area: evidence
  topic: Adopted publication scope
  outcome: supported
  summary: The record does not falsely claim primary mechanistic support. The explicit
    dihydrochloride letter concerns historical clinical exposure and adverse effects;
    the second source is a multi-form review.
  target_ids:
  - CHEBI:74723
  evidence_ids:
  - record
  - clinical1972
  - iarc1980
  - metadata
- assessment_id: mechanism
  area: completeness
  topic: Direct antimicrobial target and exact-form mapping
  outcome: unknown
  summary: No direct target is asserted or established by the inspected exact-salt
    sources. Authority intercalator roles and other salt experiments require explicit
    chemical/assay mapping before mechanistic enrichment.
  target_ids:
  - CHEBI:74723
  evidence_ids:
  - record
  - chebi
  - hemisulphate
  - search
- assessment_id: optional
  area: representation
  topic: Activity, resistance, producer, clinical and graph objects
  outcome: not_applicable
  summary: These optional fields are absent rather than incorrect. Historical use
    does not establish current approval or efficacy; no producer or resistance determinant
    is inferred from the dye class.
  target_ids:
  - CHEBI:74723
  evidence_ids:
  - record
  - clinical1972
  - iarc1980
- assessment_id: ownership
  area: ownership
  topic: Maintained generated inputs and curation state
  outcome: supported
  summary: Source version, minted identity and seed/reseed history are coherent. No
    curator override was found in the explicitly ignored-inclusive maintained scopes.
    Native SEEDED status remains unchanged.
  target_ids:
  - CHEBI:74723
  evidence_ids:
  - owner
  - chemistry
  - record
findings:
- finding_id: F1
  issue_key: chebi-74723-exact-salt-primary-evidence-followup
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Future mechanism curation needs explicit salt and experimental scope
  description: The accessible adopted evidence offers historical exact-salt context
    but no direct antibacterial mechanism. A concrete follow-up is to locate primary
    reagent-defined studies and map the active chemical form without pooling monohydrochloride,
    hemisulphate, hydrates or acriflavine mixtures. This is optional enrichment, not
    a confirmed erroneous native claim.
  target_ids:
  - CHEBI:74723
  field_paths:
  - evidence
  - mode_of_action
  - mode_of_action_notes
  - activity_spectrum
  - discussions
  evidence_ids:
  - record
  - clinical1972
  - iarc1980
  - hemisulphate
  - search
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/3-6-diaminoacridine-dihydrochloride.yaml
    role: Curator-owned evidence and bounded scientific annotations through validated
      writer and curation history
  rule_id: 'native-review-checklist: Exact identity, Evidence standard and Mode of
    action'
  native_severity: informational bounded primary-evidence follow-up
  normalization_reason: Optional fields are not mandatory defects. Current identity
    and imported classification are consistent; the follow-up prevents unsupported
    chemical-form and endpoint transfer during later curation.
actions:
- action_id: A1
  description: If selected for scientific curation, obtain primary reagent-defined
    antibacterial and binding experiments, document exact salt/preparation and assay
    chemistry, and attach evidence to the narrowest supported claims. Retain unresolved
    mechanism where mapping remains uncertain.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:74723
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/3-6-diaminoacridine-dihydrochloride.yaml
    role: Curator-owned evidence and bounded scientific annotations through validated
      writer and curation history
  acceptance_checks:
  - Record counterion, stoichiometry, hydration, mixture composition and experimental
    solution conditions; cross-form active-moiety inference must be explicit and justified
    rather than assuming identical chemical identity.
  - Separate direct nucleic-acid interaction from causal bacterial killing, mutagenicity,
    photochemical effects and host-cell endpoints. Do not invent a specific protein
    target.
  - Keep the1972 letter as bounded historical exposure/adverse-effect evidence, without
    a numerical incidence or current clinical approval claim; do not label IARC review
    statements as primary experiments.
  - Use validated writer and curation history for additions, then focused schema/strict
    and required corpus gates. Keep native SEEDED until REVIEWED criteria are actually
    met.
limitations:
- The1972 clinical letter was inspected as the publisher-rendered abstract/excerpt.
  Direct HTML and preview retrieval returned403; full PDF was not retrieved. It is
  not evidence of antibacterial potency or a current indication.
- The1980 IARC citation was inspected through its official historical summary and
  Europe PMC metadata. Full-volume PDF endpoints returned404. It is a review across
  several chemical forms, not an exact-salt primary mechanism experiment. No current
  carcinogenicity classification is asserted.
- The1974 dichloride-dihydrate crystal paper was found as indexed primary text but
  its PDF could not be fetched; the1975 hemisulphate crystal paper was inspected at
  its introductory/experimental sections. These distinct hydrate/counterion forms
  were not used to override the native anhydrous salt.
- Bounded searches did not resolve an exact dihydrochloride antibacterial target or
  quantitative susceptibility experiment. This is not proof that none exists. No paid
  source, author contact or native record change was used.
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
