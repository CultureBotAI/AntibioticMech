# Cellocidin: original isolation and structure papers support the exact diamide

- Review: 20261021T122809Z-cellocidin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:02:32Z
- Finished UTC: 2026-10-21T12:28:09Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

No confirmed corrective finding. Native achiral acetylenedicarboxamide identity, synonyms, broader parents and antibacterial filing are supported. The original discovery paper demonstrates production in a cultured Streptomyces isolate and antibacterial activity; the structure paper confirms the isolated compound by degradation and synthesis. Optional assay and biosynthesis enrichment retains historical strain names and source-specific limits. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position268; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:51763 | data/antibiotics/antibacterial/cellocidin.yaml | generated | cellocidin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:51763 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:51763 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:51763 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:51763 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:51763 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:51763 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:51763 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:51763 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:51763 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:51763 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:51763 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:51763 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact graph, formula and names

identity: supported. Targets: CHEBI:51763.

The full native structure and aliases agree with independent authorities and the original structure determination.

### Broader parents and exact cross-references

grounding: supported. Targets: CHEBI:51763.

Structural parents are appropriate; publicly inspectable chemical cross-references agree. Reaxys remains access-limited.

### Antibacterial filing and assay boundaries

evidence: supported. Targets: CHEBI:51763.

Original agar-streak inhibition supports antibacterial classification. Numeric enrichment would need original historical taxa, censored protocol detail and explicit units.

### Definition producer and pathway scope

evidence: supported. Targets: CHEBI:51763.

Culture and isolation support the historical producer statement. SF-536 tracer evidence is a distinct strain context; environmental origin alone is not used as biosynthesis evidence.

### Optional target, resistance and causal graph fields

scope: not_applicable. Targets: CHEBI:51763.

No populated native target or resistance claim needs correction. Chemical thiol reactivity does not justify a specific intracellular target or causal graph.

### All four adopted publication leads

evidence: supported. Targets: CHEBI:51763.

Discovery, structure, biosynthesis and thiol-reaction citations have explicit source and access dispositions.

### Source-owned content and history

provenance: supported. Targets: CHEBI:51763.

The ChEBI inventory and seed transform explain the record; all initial inputs and four history events are retained.

### Optional clinical, dataset and discussion content

completeness: not_applicable. Targets: CHEBI:51763.

No missing optional field is classified as a defect; pesticide nomenclature is not an approval claim.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/cellocidin.yaml; Entire YAML | supports | Read all identity/status/grounding fields, definition, nine synonyms, three parents, two roles, structure and masses, four chemical cross-references, documentary reference, source concept and four history events. |
| owners | data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; ChEBI row 9464 and source extraction/seed ownership | supports | The source row supplies the full graph and four PMID leads. Initial 13 input hashes remain unchanged; no curator-owned scientific assertions or source overrides were discovered in the ignored-inclusive bounded search. |
| chemistry | Independent RDKit 2026.03.5 native comparison; 268-chemistry.json | supports | SMILES and InChI independently reproduce JBTGHKUTYAMZEZ-UHFFFAOYSA-N, C4H4N2O2, one neutral component, no stereocentres, masses and source mint. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:51763; Current OLS complete identity and annotations | supports | Current ChEBI agrees with the native complete graph, producer wording, names and roles. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/543-21-5/property/InChI,InChIKey,MolecularFormula,SMILES,IUPACName/JSON; CAS lookup; CID 10971 | supports | CAS resolution yields the exact native structure. Independent parsing of both PubChem and ChEBI SMILES/InChI confirms the full key; CAS Registry itself was not accessed. |
| xref-calculation | Independent complete external chemical comparison; 027-root-xref-check.json, target 268 | supports | All four external molecular representations independently generate the native complete key and formula. |
| nist | https://webbook.nist.gov/cgi/cbook.cgi?ID=543-21-5; Identity and Other names | supports | NIST independently lists the same full InChI, InChIKey, formula and CAS, and the Aquamycin, Lenamycin and Renamycin aliases. Small average-mass rounding differences do not indicate another structure. |
| knapsack | https://www.knapsackfamily.com/knapsack_core/information.php?word=C00018677; Exact chemical and organism entry | supports | KNApSAcK gives the same complete key, formula and monoisotopic mass and links Streptomyces chibaensis. Its predicted starting substrates are not treated as experimental biosynthesis evidence. |
| pesticides | https://www.alanwood.net/pesticides/cellocidin.html; Exact nomenclature entry | supports | The native pesticides namespace resolves to this nomenclature page, which gives the same CAS, formula and complete InChI/key and bactericide classification. ISO name status is not regulatory approval. |
| parents | CHEBI:140324; CHEBI:35779; CHEBI:51752; CHEBI:33281; CHEBI:33282; Current OLS definitions, 268-term-*.json | supports | Primary carboxamide, dicarboxylic acid diamide and ynamide are broader structural terms compatible with two terminal carboxamides and the conjugated carbon-carbon triple bond. Antimicrobial and antibacterial agent are supported by original activity observations. |
| discovery1958 | PMID:13563326; DOI 10.11554/antibioticsa.11.3_81; full original pp.81-83; Table 3 visually checked | supports | The original paper cultures the historically named S. chibaensis isolate from Chiba City soil, ferments at 27 degrees C, isolates crystalline cellocidin, and measures agar-streak antibacterial activity. Table 3 gives M. flavus 10, M. pyogenes var. aureus 209P 200, B. agri 200, B. subtilis PCI219 20, Sarcina lutea 50, E. coli 10 and M. tuberculosis BCG 3 micrograms/mL. Assay medium, inoculum and incubation time are not fully specified. This is production evidence beyond the environmental isolation site; host sarcoma experiments remain separate. |
| structure1958 | PMID:13563327; DOI 10.11554/antibioticsa.11.3_84; full pp.84-86; formula I visually checked | supports | Hydrogenation to succinamide, degradation chemistry and synthesis establish acetylenedicarboxamide. Synthetic and isolated material agree by infrared spectroscopy and melting point. This supports the exact native achiral connectivity rather than an inferred compound family. |
| biosynthesis1973 | PMID:4736298; DOI 10.1039/P19730000148; bibliographic record and publisher abstract surfaced by web search | partial | The publisher abstract reports labelled-precursor evidence that cellocidin in Streptomyces SF-536 cultures derives from carbons 2-5 of 2-oxoglutarate as an offshoot of the Krebs cycle. Full methods were not available: direct RSC HTML/PDF requests returned 403. Do not equate SF-536 with the original S. chibaensis isolate or promote a fully resolved pathway. |
| thiol1978 | PMID:711614; DOI 10.7164/antibiotics.31.1065; full pp.1065-1066; Fig.3 visually checked | supports | The original chemical study measures decreased DTNB/glutathione signal at pH 7.6 after 10 minutes with cellocidin and characterizes cysteine addition products at its triple bond. Isolated adducts are reported inactive at 100 micrograms/mL, but the organism and antibacterial protocol are unspecified. Chemical thiol addition is not direct proof of an intracellular protein target; background DNA-precursor/TCA claims cite other work. |
| document | https://en.wikipedia.org/wiki/Cellocidin; Native documentary link | context_only | The document resolves and concerns the named compound; it is not used instead of the original papers. |
| search | Ignored-inclusive repository and bounded primary-source search; 268-local-hits.txt; 268-owner-hits.txt; 268-core.json | context_only | All four adopted PMID leads were resolved. Three original papers were read in full; the 1973 study remains abstract-limited. Local searches include hidden and ignored files outside .git/.venv. Proprietary Reaxys could not be independently inspected. |

## Limits And Additional Notes

- The 1973 biosynthesis study was inspected at publisher-abstract and bibliographic depth; its original full methods remained unavailable.
- Original 1958 susceptibility methods lack complete modern assay metadata. No strain accession or taxonomic synonym is invented.
- Proprietary Reaxys content was not independently accessed. A guessed PPDB URL was unrelated to the native pesticides namespace and was excluded from evidence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- The entire native record was assessed; no native data or scientific status changed. All 13 captured input hashes remain unchanged.
- The three primary PDFs and key original figures/tables were read; computed precursor predictions and unspecified-organism adduct inactivity are not promoted to exact biological assertions.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T122809Z-cellocidin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cellocidin: original isolation and structure papers support the exact diamide'
started_at: '2026-10-21T12:02:32Z'
finished_at: '2026-10-21T12:28:09Z'
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
summary: No confirmed corrective finding. Native achiral acetylenedicarboxamide identity,
  synonyms, broader parents and antibacterial filing are supported. The original discovery
  paper demonstrates production in a cultured Streptomyces isolate and antibacterial
  activity; the structure paper confirms the isolated compound by degradation and
  synthesis. Optional assay and biosynthesis enrichment retains historical strain
  names and source-specific limits. Scientific assessment retains the stated evidence
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
  - path: data/antibiotics/antibacterial/cellocidin.yaml
    sha256: 9e4436a152d36504cb2273bacd17907a33bc8e200936a646a82e914f85ebebe8
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
- target_id: CHEBI:51763
  path: data/antibiotics/antibacterial/cellocidin.yaml
  label: cellocidin
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
  selection: Initially uncovered queue position268; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:51763
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:51763
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    268
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:51763
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cellocidin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:51763
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cellocidin.yaml --out /private/tmp/am-review-session/268-strict.tsv
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
  - CHEBI:51763
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
  - CHEBI:51763
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
  - CHEBI:51763
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
  - CHEBI:51763
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
  - CHEBI:51763
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
  - CHEBI:51763
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
  - CHEBI:51763
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
  - CHEBI:51763
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
  - CHEBI:51763
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/cellocidin.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: Read all identity/status/grounding fields, definition, nine synonyms, three
    parents, two roles, structure and masses, four chemical cross-references, documentary
    reference, source concept and four history events.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: ChEBI row 9464 and source extraction/seed ownership
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: The source row supplies the full graph and four PMID leads. Initial 13
    input hashes remain unchanged; no curator-owned scientific assertions or source
    overrides were discovered in the ignored-inclusive bounded search.
  snapshot_sha256: 5efce5831b19492665bdf2f00bc56ac0d9a4904d1e93c6ff89deaaad67fc3973
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit 2026.03.5 native comparison
  locator: 268-chemistry.json
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: SMILES and InChI independently reproduce JBTGHKUTYAMZEZ-UHFFFAOYSA-N, C4H4N2O2,
    one neutral component, no stereocentres, masses and source mint.
  snapshot_sha256: 02dc5deba191f3bef16bd4d86f69ed6388be75b6cbeb513d2dfe428164245830
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:51763
  locator: Current OLS complete identity and annotations
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: Current ChEBI agrees with the native complete graph, producer wording,
    names and roles.
  snapshot_sha256: 4cb1ca5bc49034ff644082ba9fb9cec3fb6bf99b83a67f7b9bc07fc2e376bd7c
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/543-21-5/property/InChI,InChIKey,MolecularFormula,SMILES,IUPACName/JSON
  locator: CAS lookup; CID 10971
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: CAS resolution yields the exact native structure. Independent parsing of
    both PubChem and ChEBI SMILES/InChI confirms the full key; CAS Registry itself
    was not accessed.
  snapshot_sha256: 2315cfc037b898c7d748e1e9c5e05015e071416f20c7ea7f08aa6e6b93dd718c
- evidence_id: xref-calculation
  kind: validation
  reference: Independent complete external chemical comparison
  locator: 027-root-xref-check.json, target 268
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: All four external molecular representations independently generate the
    native complete key and formula.
  snapshot_sha256: fae7157a323812f8e3eeb541fc3b030c11787e689fc5e413d94f2737984bbe2e
- evidence_id: nist
  kind: authority
  reference: https://webbook.nist.gov/cgi/cbook.cgi?ID=543-21-5
  locator: Identity and Other names
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: NIST independently lists the same full InChI, InChIKey, formula and CAS,
    and the Aquamycin, Lenamycin and Renamycin aliases. Small average-mass rounding
    differences do not indicate another structure.
  snapshot_sha256: 37f9199d79167ba26a82bbb081d9a720f219ae96e6ae32a5e6500bb80559e0d6
- evidence_id: knapsack
  kind: database
  reference: https://www.knapsackfamily.com/knapsack_core/information.php?word=C00018677
  locator: Exact chemical and organism entry
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: KNApSAcK gives the same complete key, formula and monoisotopic mass and
    links Streptomyces chibaensis. Its predicted starting substrates are not treated
    as experimental biosynthesis evidence.
  snapshot_sha256: b03e87dce2e41935543ad08183abc610f5ab22526baa6dc8cfcd09e1f2cb7f4b
- evidence_id: pesticides
  kind: database
  reference: https://www.alanwood.net/pesticides/cellocidin.html
  locator: Exact nomenclature entry
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: The native pesticides namespace resolves to this nomenclature page, which
    gives the same CAS, formula and complete InChI/key and bactericide classification.
    ISO name status is not regulatory approval.
  snapshot_sha256: 308c6e3c3c0c0ced172efdfd3c4fc4ba900f8a672bed590455183c382c121c67
- evidence_id: parents
  kind: authority
  reference: CHEBI:140324; CHEBI:35779; CHEBI:51752; CHEBI:33281; CHEBI:33282
  locator: Current OLS definitions, 268-term-*.json
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: Primary carboxamide, dicarboxylic acid diamide and ynamide are broader
    structural terms compatible with two terminal carboxamides and the conjugated
    carbon-carbon triple bond. Antimicrobial and antibacterial agent are supported
    by original activity observations.
- evidence_id: discovery1958
  kind: primary_source
  reference: PMID:13563326
  locator: DOI 10.11554/antibioticsa.11.3_81; full original pp.81-83; Table 3 visually
    checked
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: The original paper cultures the historically named S. chibaensis isolate
    from Chiba City soil, ferments at 27 degrees C, isolates crystalline cellocidin,
    and measures agar-streak antibacterial activity. Table 3 gives M. flavus 10, M.
    pyogenes var. aureus 209P 200, B. agri 200, B. subtilis PCI219 20, Sarcina lutea
    50, E. coli 10 and M. tuberculosis BCG 3 micrograms/mL. Assay medium, inoculum
    and incubation time are not fully specified. This is production evidence beyond
    the environmental isolation site; host sarcoma experiments remain separate.
  snapshot_sha256: 824a74d94efbd11db21d8450ba80bdec4ebf36700cafc02f2d37f762ce53afef
- evidence_id: structure1958
  kind: primary_source
  reference: PMID:13563327
  locator: DOI 10.11554/antibioticsa.11.3_84; full pp.84-86; formula I visually checked
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: Hydrogenation to succinamide, degradation chemistry and synthesis establish
    acetylenedicarboxamide. Synthetic and isolated material agree by infrared spectroscopy
    and melting point. This supports the exact native achiral connectivity rather
    than an inferred compound family.
  snapshot_sha256: 7c66ed9d3b7224989561848280c8b7674d57db568769995501faded15b7a6961
- evidence_id: biosynthesis1973
  kind: primary_source
  reference: PMID:4736298
  locator: DOI 10.1039/P19730000148; bibliographic record and publisher abstract surfaced
    by web search
  accessed_at: '2026-10-21T12:21:17Z'
  support: partial
  summary: 'The publisher abstract reports labelled-precursor evidence that cellocidin
    in Streptomyces SF-536 cultures derives from carbons 2-5 of 2-oxoglutarate as
    an offshoot of the Krebs cycle. Full methods were not available: direct RSC HTML/PDF
    requests returned 403. Do not equate SF-536 with the original S. chibaensis isolate
    or promote a fully resolved pathway.'
- evidence_id: thiol1978
  kind: primary_source
  reference: PMID:711614
  locator: DOI 10.7164/antibiotics.31.1065; full pp.1065-1066; Fig.3 visually checked
  accessed_at: '2026-10-21T12:21:17Z'
  support: supports
  summary: The original chemical study measures decreased DTNB/glutathione signal
    at pH 7.6 after 10 minutes with cellocidin and characterizes cysteine addition
    products at its triple bond. Isolated adducts are reported inactive at 100 micrograms/mL,
    but the organism and antibacterial protocol are unspecified. Chemical thiol addition
    is not direct proof of an intracellular protein target; background DNA-precursor/TCA
    claims cite other work.
  snapshot_sha256: e20c982bd7e43422154e8e83cadbc42426d525dd4332bd2569d57d780b2c90d7
- evidence_id: document
  kind: database
  reference: https://en.wikipedia.org/wiki/Cellocidin
  locator: Native documentary link
  accessed_at: '2026-10-21T12:21:17Z'
  support: context_only
  summary: The document resolves and concerns the named compound; it is not used instead
    of the original papers.
  snapshot_sha256: 10dd4f3f168b1c7519a96e0da4faf5d499557a16cfe06d8559d958ae703d6895
- evidence_id: search
  kind: search
  reference: Ignored-inclusive repository and bounded primary-source search
  locator: 268-local-hits.txt; 268-owner-hits.txt; 268-core.json
  accessed_at: '2026-10-21T12:21:17Z'
  support: context_only
  summary: All four adopted PMID leads were resolved. Three original papers were read
    in full; the 1973 study remains abstract-limited. Local searches include hidden
    and ignored files outside .git/.venv. Proprietary Reaxys could not be independently
    inspected.
  search_scope: Exact name, identifier, full key and source owners; all adopted leads,
    official identities and free primary publications; no claim of exhaustive literature
    coverage.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact graph, formula and names
  outcome: supported
  summary: The full native structure and aliases agree with independent authorities
    and the original structure determination.
  target_ids:
  - CHEBI:51763
  evidence_ids:
  - native
  - chemistry
  - chebi
  - pubchem
  - nist
  - structure1958
- assessment_id: grounding
  area: grounding
  topic: Broader parents and exact cross-references
  outcome: supported
  summary: Structural parents are appropriate; publicly inspectable chemical cross-references
    agree. Reaxys remains access-limited.
  target_ids:
  - CHEBI:51763
  evidence_ids:
  - parents
  - xref-calculation
  - knapsack
  - pesticides
  - document
- assessment_id: activity
  area: evidence
  topic: Antibacterial filing and assay boundaries
  outcome: supported
  summary: Original agar-streak inhibition supports antibacterial classification.
    Numeric enrichment would need original historical taxa, censored protocol detail
    and explicit units.
  target_ids:
  - CHEBI:51763
  evidence_ids:
  - discovery1958
  - thiol1978
- assessment_id: producer
  area: evidence
  topic: Definition producer and pathway scope
  outcome: supported
  summary: Culture and isolation support the historical producer statement. SF-536
    tracer evidence is a distinct strain context; environmental origin alone is not
    used as biosynthesis evidence.
  target_ids:
  - CHEBI:51763
  evidence_ids:
  - native
  - discovery1958
  - biosynthesis1973
- assessment_id: mechanism
  area: scope
  topic: Optional target, resistance and causal graph fields
  outcome: not_applicable
  summary: No populated native target or resistance claim needs correction. Chemical
    thiol reactivity does not justify a specific intracellular target or causal graph.
  target_ids:
  - CHEBI:51763
  evidence_ids:
  - native
  - thiol1978
- assessment_id: leads
  area: evidence
  topic: All four adopted publication leads
  outcome: supported
  summary: Discovery, structure, biosynthesis and thiol-reaction citations have explicit
    source and access dispositions.
  target_ids:
  - CHEBI:51763
  evidence_ids:
  - discovery1958
  - structure1958
  - biosynthesis1973
  - thiol1978
- assessment_id: provenance
  area: provenance
  topic: Source-owned content and history
  outcome: supported
  summary: The ChEBI inventory and seed transform explain the record; all initial
    inputs and four history events are retained.
  target_ids:
  - CHEBI:51763
  evidence_ids:
  - native
  - owners
  - search
- assessment_id: optional
  area: completeness
  topic: Optional clinical, dataset and discussion content
  outcome: not_applicable
  summary: No missing optional field is classified as a defect; pesticide nomenclature
    is not an approval claim.
  target_ids:
  - CHEBI:51763
  evidence_ids:
  - native
  - pesticides
findings: []
actions: []
limitations:
- The 1973 biosynthesis study was inspected at publisher-abstract and bibliographic
  depth; its original full methods remained unavailable.
- Original 1958 susceptibility methods lack complete modern assay metadata. No strain
  accession or taxonomic synonym is invented.
- Proprietary Reaxys content was not independently accessed. A guessed PPDB URL was
  unrelated to the native pesticides namespace and was excluded from evidence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- The entire native record was assessed; no native data or scientific status changed.
  All 13 captured input hashes remain unchanged.
- The three primary PDFs and key original figures/tables were read; computed precursor
  predictions and unspecified-organism adduct inactivity are not promoted to exact
  biological assertions.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:51763
- https://doi.org/10.11554/antibioticsa.11.3_81
- https://doi.org/10.11554/antibioticsa.11.3_84
tags:
- cellocidin
- primary-structure
- producer-evidence
```
