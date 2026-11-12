# Review of difloxacin

- Review: 20261021T144027Z-difloxacin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:27:11Z
- Finished UTC: 2026-10-21T14:40:27Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Eight independent/native structure encodings agree on neutral difloxacin, and an explicit molecular substitution check confirms the definition's relationship to pefloxacin. Original 1986 material and susceptibility pages support activity against tested Gram-positive and Gram-negative panels, with hydrochloride reagent and base-equivalent concentrations explicitly distinguished. FDA and historical EMA documents corroborate canine hydrochloride-product use; EMA withdrawal is retained separately. All six adopted citation leads were checked and no confirmed corrective finding was established. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire SEEDED, EXACT record: definition, five synonyms, seven chemical parents, two activity roles, full structure, four exact identifiers, one drug reference, three document references, source concept and four history events. All six adopted PMID leads checked.

Selection: Queue 362 in isolated batch 037; original thirteen hashes preserved. All actual ChEBI identity/role/extraction/seeding owners were already among those inputs and their roles were confirmed before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:4537 | data/antibiotics/antibacterial/difloxacin.yaml | generated | difloxacin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema validation | passed | True | CHEBI:4537 | Exit 0. |
| Documented strict validation | passed | True | CHEBI:4537 | Exit 0; no ERROR rows. |
| Native molecular consistency | passed | False | CHEBI:4537 | Native graph, key, formula, charge and masses agree. |
| Independent chemical and definition mapping | passed | False | CHEBI:4537 | Eight encodings have reciprocal chirality-aware graph agreement, no configured or undefined tetrahedral centers, and matching neutral composition. Replacing the N1 p-fluorophenyl with ethyl yields official pefloxacin. |
| Whole source, citation and history audit | passed | False | CHEBI:4537 | All thirteen hashes, five aliases, seven parents, six adopted PMID records and four history events reconcile. |
| Authoritative full QC | failed | True | CHEBI:4537 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:4537 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:4537 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:4537 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:4537 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:4537 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:4537 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:4537 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:4537 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral difloxacin and definition connectivity

identity: supported. Targets: CHEBI:4537.

Eight independent/native encodings and explicit pefloxacin substitution agree; salt material and metabolites remain distinct.

### Structural classes and antibacterial scope

evidence: supported. Targets: CHEBI:4537.

The seven structural parents match the graph; original tested Gram-positive/negative panels and official veterinary material support antibacterial role.

### Salt-qualified canine-use description

evidence: supported. Targets: CHEBI:4537.

Original FDA and historical EMA records support the definition's hydrochloride-product use. Withdrawal is preserved without implying universal ongoing approval.

### Potential exact gyrase mechanism enrichment

completeness: unknown. Targets: CHEBI:4537.

The native record makes no target assertion. Regulatory/database gyrase descriptions provide context, while an exact original enzyme/cleavage experiment remains uninspected.

### Licensed Reaxys reference

identity: unknown. Targets: CHEBI:4537.

Accessible exact identifiers reconcile; Reaxys was not independently resolved and is not called wrong.

### All adopted leads and unchanged owners

provenance: supported. Targets: CHEBI:4537.

Six adopted abstracts receive individual dispositions; thirteen original hashes and four history events remain unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/difloxacin.yaml; Entire native YAML | supports | The exact neutral compound is distinguished from its commonly used monohydrochloride in the definition. Five synonyms are chemical/INN names, not product brands. No native gene/protein, pathway, MIC, clinical approval, producer or causal graph is asserted. |
| chemistry | CHEBI:4537; PubChem CID56206; KEGG C11234/D07828; VSDB1841; 362-chebi.json/.mol; 362-pubchem.json; both KEGG mol/text pairs; 362-vsdb.html; 362-authority-chemistry.json; 362-pefloxacin.json | supports | All eight encodings match C21H19F2N3O3, NOCJXYPHIIZEHN-UHFFFAOYSA-N, zero charge and no tetrahedral stereocenters. Native mass values reconcile. The N-methylpiperazine and N1 p-fluorophenyl connectivity agree; replacing the latter with ethyl maps exactly to independent PubChem pefloxacin. No hydrochloride, hydrate or separate photoproduct is part of the native graph. |
| terms | Seven ChEBI structural parents and antibacterial/antimicrobial roles; 362-term-23765/25384/46845/46848/83575/86324/87211.json; 362-chebi.json | supports | The parents resolve to quinolone, monocarboxylic acid, N-alkylpiperazine, N-arylpiperazine, monofluorobenzenes, quinolone antibiotic and fluoroquinolone antibiotic. Their scope matches the graph. A monofluorobenzene moiety is present even though the entire molecule has two fluorines; the term does not require only one total molecular fluorine. |
| vsdb | Veterinary Substances Database entry1841; 362-vsdb.html identity, canonical SMILES, CAS, InChI and status sections | supports | The exact entry resolves difloxacin with CAS98106-17-3, matching parent formula/SMILES/key and veterinary antibacterial context. Its molecular-target annotation is database information and is not imported as primary binding evidence. The entry distinguishes current UK/EU nonapproval from historical therapeutic use. |
| patents | EP0131839A1; US4730000A; 362-patent-EP131839A1.html Example 5; 362-patent-US4730000.html Example 5 and adjacent examples | supports | Both documents describe the p-fluorophenyl, N-methylpiperazinyl quinolone acid and distinguish its hydrochloride salt. The European native number resolves with kind code A1; an initial A2 guess returned 404. The US Example 5 heading has a p-difluorophenyl wording inconsistency, but its body and European counterpart specify p-fluorophenyl. The native graph is supported independently rather than inheriting a patent OCR/heading error. |
| primary | PMID:3087274; DOI:10.1128/AAC.29.2.193; 362-primary-page193.png through 362-primary-page196.png: introduction/materials, Figure 1, susceptibility methods and Table 1 first two pages | supports | The original paper identifies A-56619 as difloxacin hydrochloride, with Figure 1 showing the N-methyl group and one HCl. Abbott synthesized the reagent; assay concentrations are expressed as micrograms of base per mL. Agar dilution used Mueller-Hinton agar at pH 7.3 for most species, with separate supplemented media for gonococci/Haemophilus. Table 1 shows tested Gram-negative and staphylococcal/streptococcal activity with species-dependent potency. This supports broad antibacterial scope, not identical efficacy against every bacterium or an independently tested neat free-acid solid. |
| fda | FDA NADA 141-096 original approval FOI,1997-11-20; 362-fda-foi.pdf printed pp 1–3 and 11–13; material, indications, randomized field-trial design and Table 4 | supports | FDA identifies Dicural tablets as difloxacin hydrochloride and documents canine skin/soft-tissue and urinary-infection use. The field comparison used enrofloxacin as positive control and had explicit evaluation exclusions; urinary bacterial elimination and dermal clinical resolution are distinct endpoints. These original regulatory-study details support the historical salt-product context, not current universal authorization or clinical equivalence of every formulation. |
| ema | EMA Dicural EPAR and historical product information; 362-ema.html withdrawal notice; 362-ema-product.pdf printed pp 7–9, dog tablets sections 1–2, 4.1–4.2 and 5 | supports | Dog tablets contain difloxacin as hydrochloride and were indicated for specified susceptible urinary infections and superficial pyoderma. EMA states the marketing authorization was withdrawn at the holder's request; the PDF is marked no longer authorized. The pharmacology text supports broad antibacterial and gyrase-related context but is not an exact enzyme-binding experiment. The native record has no current EMA approval claim to contradict. |
| leads | Six adopted ChEBI PMID leads; 362-adopted-core.json and 362-lead-dispositions.json | context_only | All six complete abstracts were read. Photolysis and sarafloxacin formation, manure/soil persistence and community effects, flounder PK, broiler PK/E. coli context and human PK/metabolites are separately bounded. None is promoted to an exact primary microbial target assertion or universal veterinary/human clinical indication. |
| document | Wikipedia Difloxacin document link; 362-wikipedia.html identity, indications and mechanism sections | context_only | The document resolves the intended compound and distinguishes veterinary use and hydrochloride products. Secondary summaries and comparative-efficacy claims are not substituted for the original activity pages or official product scope. |
| owners | Maintained ChEBI source and generation; 362-inspect.json; 362-owner-confirmation.json; 362-source-row.json; 362-source-audit.json | supports | All thirteen original inputs remain unchanged; source identity, aliases, cross-reference placement, seven parents and four ordered histories reproduce. The exact native target has no structured-adapter trigger, so no protein query is needed to validate an absent edge. |
| validation | Executed focused checks; 362-focused-results.json; 362-focused-run.log; 362-strict.tsv; 362-chemistry-authorities.log; 362-ledger.log | supports | Native chemistry/schema/strict, independent authority/definition mapping and source ledger all exit 0. |
| search | Exact identifiers, adopted leads and original material searches; 362-local-hits.txt includes ignored files; 362-fetch through 362-fetch5 manifests | context_only | Original full XML returned 500, but public scanned pages 193–196 were retrieved and visually read. Initial EP A2 lookup returned 404 and the correct A1 document succeeded. Licensed Reaxys5835542 was not independently resolved. These access boundaries do not establish absent literature or a wrong patent number. |

## Limits And Additional Notes

- Original 1986 scanned pp 193–196 and complete abstract were read; the remaining pages and all raw time-kill/interaction experiments were not independently inspected. The reagent is hydrochloride and potencies are base-equivalent; the native free acid is the identified antibacterial moiety rather than a separately tested solid form.
- All six adopted PMID abstracts were checked, but their full original methods/results were not all inspected. The broiler abstract has an incomplete MIC unit, so no numerical native observation was extracted.
- Historical canine authorization and tested product efficacy do not establish present-day approval in every jurisdiction. EMA explicitly records withdrawal; the record contains no structured current approval assertion.
- Patents are broad chemical disclosures. Their exact Example 5 relevance was checked, but original spectra and every formula image were not independently reconstructed; an inconsistent US heading was not adopted over matching graph/body evidence.
- VSDB and regulatory gyrase descriptions are not a newly verified direct-binding experiment. Missing native mechanism detail is optional enrichment and no protein or resistance relation was added.
- The licensed Reaxys record remains inaccessible in this review. Current ChEBI bibliographic associations beyond the six adopted leads were not exhaustively reviewed.
- All focused native checks passed; shared corpus gates retain separate actual outcomes. No native record or maintained input was modified.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- The definition already qualifies the commonly used hydrochloride form, so parent-versus-salt evidence is not silently treated as a chemical-identity error.
- No stereocenter is encoded or required by the exact scaffold; the achiral graph is not evidence of a racemic mixture.
- Review artifacts were written in scratch. Native checks used batch 037 and standalone chemistry used the recorded batch 019 interpreter.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T144027Z-difloxacin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of difloxacin
started_at: '2026-10-21T14:27:11Z'
finished_at: '2026-10-21T14:40:27Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Independent whole-record/source reconciliation, exact-authority
    molecular graphs and pefloxacin substitution mapping, original scanned in-vitro
    methods/identity/results pages, official canine clinical material and regulatory
    documents, and individual adopted-lead dispositions.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
native_verdict: Exact neutral difloxacin, antibacterial role and salt-qualified historical
  canine use supported
scientific_review: true
summary: Eight independent/native structure encodings agree on neutral difloxacin,
  and an explicit molecular substitution check confirms the definition's relationship
  to pefloxacin. Original 1986 material and susceptibility pages support activity
  against tested Gram-positive and Gram-negative panels, with hydrochloride reagent
  and base-equivalent concentrations explicitly distinguished. FDA and historical
  EMA documents corroborate canine hydrochloride-product use; EMA withdrawal is retained
  separately. All six adopted citation leads were checked and no confirmed corrective
  finding was established. Scientific assessment retains the stated evidence limits;
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
  - path: data/antibiotics/antibacterial/difloxacin.yaml
    sha256: 039746c7c855789aa4b241e10b9b283909194c4f89aa839845cf3d19a69abb14
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
  description: 'Entire SEEDED, EXACT record: definition, five synonyms, seven chemical
    parents, two activity roles, full structure, four exact identifiers, one drug
    reference, three document references, source concept and four history events.
    All six adopted PMID leads checked.'
  selection: Queue 362 in isolated batch 037; original thirteen hashes preserved.
    All actual ChEBI identity/role/extraction/seeding owners were already among those
    inputs and their roles were confirmed before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:4537
targets:
- target_id: CHEBI:4537
  path: data/antibiotics/antibacterial/difloxacin.yaml
  label: difloxacin
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
    path: data/raw/chebi_role_names.tsv
    role: Adopted antimicrobial and antibacterial role labels
checks:
- check_id: schema
  name: Documented schema validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/difloxacin.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0.
  target_ids:
  - CHEBI:4537
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/difloxacin.yaml --out /private/tmp/am-review-session/362-strict.tsv
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; no ERROR rows.
  target_ids:
  - CHEBI:4537
  evidence_ids:
  - validation
- check_id: native-chemistry
  name: Native molecular consistency
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    362
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Native graph, key, formula, charge and masses agree.
  target_ids:
  - CHEBI:4537
  evidence_ids:
  - chemistry
  - validation
- check_id: authority-chemistry
  name: Independent chemical and definition mapping
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/362-chemistry-authorities.py
    > /private/tmp/am-review-session/362-chemistry-authorities.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Eight encodings have reciprocal chirality-aware graph agreement, no configured
    or undefined tetrahedral centers, and matching neutral composition. Replacing
    the N1 p-fluorophenyl with ethyl yields official pefloxacin.
  target_ids:
  - CHEBI:4537
  evidence_ids:
  - chemistry
- check_id: ledger
  name: Whole source, citation and history audit
  command: .venv/bin/python /private/tmp/am-review-session/362-ledger.py > /private/tmp/am-review-session/362-ledger.log
    2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: All thirteen hashes, five aliases, seven parents, six adopted PMID records
    and four history events reconcile.
  target_ids:
  - CHEBI:4537
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
  - CHEBI:4537
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
  - CHEBI:4537
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
  - CHEBI:4537
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
  - CHEBI:4537
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
  - CHEBI:4537
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
  - CHEBI:4537
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
  - CHEBI:4537
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
  - CHEBI:4537
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
  - CHEBI:4537
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/difloxacin.yaml
  locator: Entire native YAML
  accessed_at: '2026-10-21T14:38:31Z'
  support: supports
  summary: The exact neutral compound is distinguished from its commonly used monohydrochloride
    in the definition. Five synonyms are chemical/INN names, not product brands. No
    native gene/protein, pathway, MIC, clinical approval, producer or causal graph
    is asserted.
- evidence_id: chemistry
  kind: authority
  reference: CHEBI:4537; PubChem CID56206; KEGG C11234/D07828; VSDB1841
  locator: 362-chebi.json/.mol; 362-pubchem.json; both KEGG mol/text pairs; 362-vsdb.html;
    362-authority-chemistry.json; 362-pefloxacin.json
  accessed_at: '2026-10-21T14:38:31Z'
  support: supports
  summary: All eight encodings match C21H19F2N3O3, NOCJXYPHIIZEHN-UHFFFAOYSA-N, zero
    charge and no tetrahedral stereocenters. Native mass values reconcile. The N-methylpiperazine
    and N1 p-fluorophenyl connectivity agree; replacing the latter with ethyl maps
    exactly to independent PubChem pefloxacin. No hydrochloride, hydrate or separate
    photoproduct is part of the native graph.
  snapshot_sha256: 8b6b9fe846e730a7a13e738d940bf77fbd9eff779eef8b894c04cca14eb274f2
- evidence_id: terms
  kind: authority
  reference: Seven ChEBI structural parents and antibacterial/antimicrobial roles
  locator: 362-term-23765/25384/46845/46848/83575/86324/87211.json; 362-chebi.json
  accessed_at: '2026-10-21T14:35:21.783109Z'
  support: supports
  summary: The parents resolve to quinolone, monocarboxylic acid, N-alkylpiperazine,
    N-arylpiperazine, monofluorobenzenes, quinolone antibiotic and fluoroquinolone
    antibiotic. Their scope matches the graph. A monofluorobenzene moiety is present
    even though the entire molecule has two fluorines; the term does not require only
    one total molecular fluorine.
  snapshot_sha256: 46500ca98bcd373a0330bd31948ca17c24efbbbf697f7b104921997527a1d837
- evidence_id: vsdb
  kind: database
  reference: Veterinary Substances Database entry1841
  locator: 362-vsdb.html identity, canonical SMILES, CAS, InChI and status sections
  accessed_at: '2026-10-21T14:35:22.467045Z'
  support: supports
  summary: The exact entry resolves difloxacin with CAS98106-17-3, matching parent
    formula/SMILES/key and veterinary antibacterial context. Its molecular-target
    annotation is database information and is not imported as primary binding evidence.
    The entry distinguishes current UK/EU nonapproval from historical therapeutic
    use.
  snapshot_sha256: c87160cfd0d283bcf79b3cc776e98ac8312e3438c33184c4453522b9e19399a0
- evidence_id: patents
  kind: primary_source
  reference: EP0131839A1; US4730000A
  locator: 362-patent-EP131839A1.html Example 5; 362-patent-US4730000.html Example
    5 and adjacent examples
  accessed_at: '2026-10-21T14:35:49.166912Z'
  support: supports
  summary: Both documents describe the p-fluorophenyl, N-methylpiperazinyl quinolone
    acid and distinguish its hydrochloride salt. The European native number resolves
    with kind code A1; an initial A2 guess returned 404. The US Example 5 heading
    has a p-difluorophenyl wording inconsistency, but its body and European counterpart
    specify p-fluorophenyl. The native graph is supported independently rather than
    inheriting a patent OCR/heading error.
  snapshot_sha256: e8b152069e3f1a3f5d305d3827ccd693bc832ad2ae529f512f974ecc9e567f7b
- evidence_id: primary
  kind: primary_source
  reference: PMID:3087274; DOI:10.1128/AAC.29.2.193
  locator: '362-primary-page193.png through 362-primary-page196.png: introduction/materials,
    Figure 1, susceptibility methods and Table 1 first two pages'
  accessed_at: '2026-10-21T14:36:38.466277Z'
  support: supports
  summary: The original paper identifies A-56619 as difloxacin hydrochloride, with
    Figure 1 showing the N-methyl group and one HCl. Abbott synthesized the reagent;
    assay concentrations are expressed as micrograms of base per mL. Agar dilution
    used Mueller-Hinton agar at pH 7.3 for most species, with separate supplemented
    media for gonococci/Haemophilus. Table 1 shows tested Gram-negative and staphylococcal/streptococcal
    activity with species-dependent potency. This supports broad antibacterial scope,
    not identical efficacy against every bacterium or an independently tested neat
    free-acid solid.
  snapshot_sha256: 96eed03a56d8e528f0c2582468a6857d4c79ca339c5c6a7cd5de2d7f2f50547a
- evidence_id: fda
  kind: authority
  reference: FDA NADA 141-096 original approval FOI,1997-11-20
  locator: 362-fda-foi.pdf printed pp 1–3 and 11–13; material, indications, randomized
    field-trial design and Table 4
  accessed_at: '2026-10-21T14:35:49.166971Z'
  support: supports
  summary: FDA identifies Dicural tablets as difloxacin hydrochloride and documents
    canine skin/soft-tissue and urinary-infection use. The field comparison used enrofloxacin
    as positive control and had explicit evaluation exclusions; urinary bacterial
    elimination and dermal clinical resolution are distinct endpoints. These original
    regulatory-study details support the historical salt-product context, not current
    universal authorization or clinical equivalence of every formulation.
  snapshot_sha256: dfcf5e647136f71eea8fb626a1efca9dfc9c431c936e86815310f1234ca9c1a7
- evidence_id: ema
  kind: authority
  reference: EMA Dicural EPAR and historical product information
  locator: 362-ema.html withdrawal notice; 362-ema-product.pdf printed pp 7–9, dog
    tablets sections 1–2, 4.1–4.2 and 5
  accessed_at: '2026-10-21T14:35:49.166731Z'
  support: supports
  summary: Dog tablets contain difloxacin as hydrochloride and were indicated for
    specified susceptible urinary infections and superficial pyoderma. EMA states
    the marketing authorization was withdrawn at the holder's request; the PDF is
    marked no longer authorized. The pharmacology text supports broad antibacterial
    and gyrase-related context but is not an exact enzyme-binding experiment. The
    native record has no current EMA approval claim to contradict.
  snapshot_sha256: 68aae806cd5df5fbdea0c60d6f8198f3a5cd947bfeb3592332b11e979f41c753
- evidence_id: leads
  kind: database
  reference: Six adopted ChEBI PMID leads
  locator: 362-adopted-core.json and 362-lead-dispositions.json
  accessed_at: '2026-10-21T14:38:31Z'
  support: context_only
  summary: All six complete abstracts were read. Photolysis and sarafloxacin formation,
    manure/soil persistence and community effects, flounder PK, broiler PK/E. coli
    context and human PK/metabolites are separately bounded. None is promoted to an
    exact primary microbial target assertion or universal veterinary/human clinical
    indication.
  snapshot_sha256: 531578898a92c9830850d9494b78e548a2444afe7d9a886b3797688b28ec546d
- evidence_id: document
  kind: database
  reference: Wikipedia Difloxacin document link
  locator: 362-wikipedia.html identity, indications and mechanism sections
  accessed_at: '2026-10-21T14:35:22.478308Z'
  support: context_only
  summary: The document resolves the intended compound and distinguishes veterinary
    use and hydrochloride products. Secondary summaries and comparative-efficacy claims
    are not substituted for the original activity pages or official product scope.
  snapshot_sha256: 6c22033f71b67c8ee0a1b7d49a61f2aab3dad0f0d253ce8fe552d969093821e2
- evidence_id: owners
  kind: database
  reference: Maintained ChEBI source and generation
  locator: 362-inspect.json; 362-owner-confirmation.json; 362-source-row.json; 362-source-audit.json
  accessed_at: '2026-10-21T14:38:31Z'
  support: supports
  summary: All thirteen original inputs remain unchanged; source identity, aliases,
    cross-reference placement, seven parents and four ordered histories reproduce.
    The exact native target has no structured-adapter trigger, so no protein query
    is needed to validate an absent edge.
  snapshot_sha256: 4b4c9ad17ca96aebceafabda1fd947dd148ee126edb13bf8ee4aab9f391c87b6
- evidence_id: validation
  kind: validation
  reference: Executed focused checks
  locator: 362-focused-results.json; 362-focused-run.log; 362-strict.tsv; 362-chemistry-authorities.log;
    362-ledger.log
  accessed_at: '2026-10-21T14:38:31Z'
  support: supports
  summary: Native chemistry/schema/strict, independent authority/definition mapping
    and source ledger all exit 0.
  snapshot_sha256: 3004b8301e66b01b11afbffae62ee35d1ca420fab99a110a10a621d72640feab
- evidence_id: search
  kind: search
  reference: Exact identifiers, adopted leads and original material searches
  locator: 362-local-hits.txt includes ignored files; 362-fetch through 362-fetch5
    manifests
  accessed_at: '2026-10-21T14:38:31Z'
  support: context_only
  summary: Original full XML returned 500, but public scanned pages 193–196 were retrieved
    and visually read. Initial EP A2 lookup returned 404 and the correct A1 document
    succeeded. Licensed Reaxys5835542 was not independently resolved. These access
    boundaries do not establish absent literature or a wrong patent number.
  snapshot_sha256: e450b1d7ce0042eb9871d7e5a5b1169a42f07c98fd08436f4b7f52f054368948
  search_scope: 362-local-hits.txt includes ignored files; 362-fetch through 362-fetch5
    manifests
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral difloxacin and definition connectivity
  outcome: supported
  summary: Eight independent/native encodings and explicit pefloxacin substitution
    agree; salt material and metabolites remain distinct.
  target_ids:
  - CHEBI:4537
  evidence_ids:
  - chemistry
  - patents
- assessment_id: classification
  area: evidence
  topic: Structural classes and antibacterial scope
  outcome: supported
  summary: The seven structural parents match the graph; original tested Gram-positive/negative
    panels and official veterinary material support antibacterial role.
  target_ids:
  - CHEBI:4537
  evidence_ids:
  - terms
  - primary
  - vsdb
- assessment_id: clinical-context
  area: evidence
  topic: Salt-qualified canine-use description
  outcome: supported
  summary: Original FDA and historical EMA records support the definition's hydrochloride-product
    use. Withdrawal is preserved without implying universal ongoing approval.
  target_ids:
  - CHEBI:4537
  evidence_ids:
  - record
  - fda
  - ema
- assessment_id: mechanism
  area: completeness
  topic: Potential exact gyrase mechanism enrichment
  outcome: unknown
  summary: The native record makes no target assertion. Regulatory/database gyrase
    descriptions provide context, while an exact original enzyme/cleavage experiment
    remains uninspected.
  target_ids:
  - CHEBI:4537
  evidence_ids:
  - record
  - ema
  - vsdb
- assessment_id: xref
  area: identity
  topic: Licensed Reaxys reference
  outcome: unknown
  summary: Accessible exact identifiers reconcile; Reaxys was not independently resolved
    and is not called wrong.
  target_ids:
  - CHEBI:4537
  evidence_ids:
  - chemistry
  - vsdb
  - search
- assessment_id: provenance
  area: provenance
  topic: All adopted leads and unchanged owners
  outcome: supported
  summary: Six adopted abstracts receive individual dispositions; thirteen original
    hashes and four history events remain unchanged.
  target_ids:
  - CHEBI:4537
  evidence_ids:
  - leads
  - owners
  - validation
findings: []
actions: []
limitations:
- Original 1986 scanned pp 193–196 and complete abstract were read; the remaining
  pages and all raw time-kill/interaction experiments were not independently inspected.
  The reagent is hydrochloride and potencies are base-equivalent; the native free
  acid is the identified antibacterial moiety rather than a separately tested solid
  form.
- All six adopted PMID abstracts were checked, but their full original methods/results
  were not all inspected. The broiler abstract has an incomplete MIC unit, so no numerical
  native observation was extracted.
- Historical canine authorization and tested product efficacy do not establish present-day
  approval in every jurisdiction. EMA explicitly records withdrawal; the record contains
  no structured current approval assertion.
- Patents are broad chemical disclosures. Their exact Example 5 relevance was checked,
  but original spectra and every formula image were not independently reconstructed;
  an inconsistent US heading was not adopted over matching graph/body evidence.
- VSDB and regulatory gyrase descriptions are not a newly verified direct-binding
  experiment. Missing native mechanism detail is optional enrichment and no protein
  or resistance relation was added.
- The licensed Reaxys record remains inaccessible in this review. Current ChEBI bibliographic
  associations beyond the six adopted leads were not exhaustively reviewed.
- All focused native checks passed; shared corpus gates retain separate actual outcomes.
  No native record or maintained input was modified.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- The definition already qualifies the commonly used hydrochloride form, so parent-versus-salt
  evidence is not silently treated as a chemical-identity error.
- No stereocenter is encoded or required by the exact scaffold; the achiral graph
  is not evidence of a racemic mixture.
- Review artifacts were written in scratch. Native checks used batch 037 and standalone
  chemistry used the recorded batch 019 interpreter.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:4537
- https://sitem.herts.ac.uk/aeru/vsdb/Reports/1841.htm
- https://www.ema.europa.eu/en/medicines/veterinary/EPAR/dicural
- https://doi.org/10.1128/AAC.29.2.193
- https://patents.google.com/patent/EP0131839A1/en
tags:
- record-review
- difloxacin
- veterinary-material-scope
```
