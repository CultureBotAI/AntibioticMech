# Factumycin: incompatible exact cross-references and an incomplete definition citation

- Review: 20261021T160635Z-factumycin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T15:38:19Z
- Finished UTC: 2026-10-21T16:06:35Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native C44 graph agrees with PubChem and original constitutional evidence. The exact ChEBI xref instead contains an additional methyl, and ChEMBL differs at assigned stereochemistry. The sole 1982 definition citation cannot support later biosynthetic and Acinetobacter claims; the taxon spelling also needs correction.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 424; entire native record. Original thirteen hashes were preserved within 18 actual owner/context inputs before substantive judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-fdb0f4de1c | data/antibiotics/antibacterial/factumycin.yaml | generated | factumycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-fdb0f4de1c | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-fdb0f4de1c | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-fdb0f4de1c | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | antibioticmech:aro-fdb0f4de1c | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-fdb0f4de1c | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-fdb0f4de1c | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-fdb0f4de1c | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-fdb0f4de1c | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-fdb0f4de1c | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-fdb0f4de1c | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-fdb0f4de1c | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-fdb0f4de1c | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### C44 constitution and incompatible exact xrefs

identity: concern. Targets: antibioticmech:aro-fdb0f4de1c.

Original1982 and2024 evidence support C44 composition; ChEBI adds a methyl. ChEMBL shares connectivity but conflicts in assigned stereochemistry. Native partial configuration is not mistaken for a proven mixture, and no complete absolute-configuration re-elucidation is claimed.

### Claim-specific source coverage and taxon spelling

evidence: concern. Targets: antibioticmech:aro-fdb0f4de1c.

The1982 source supports isolation and activity, but not Kitasatospora genomic attribution, later cluster characterization or the A. baumannii-guided activity scope. Those require the later originals with their actual limits. The intended taxon is Acinetobacter baumannii.

### Qualified facT assertion

evidence: supported. Targets: antibioticmech:aro-fdb0f4de1c.

The generic efflux database claim is supported at current-source and original2012 abstract depth. The transporter-family discrepancy and unavailable detailed experiments prevent a stronger unqualified primary upgrade.

### Optional unasserted fields and review status

completeness: supported. Targets: antibioticmech:aro-fdb0f4de1c.

All native fields and adopted leads were assessed at their recorded reading depth. Optional quantitative activity, targets, graphs, clinical status and expression datasets are not automatically required in a SEEDED record. This review does not promote native scientific curation status.

### Generated owners and unchanged input ledger

provenance: supported. Targets: antibioticmech:aro-fdb0f4de1c.

All 18 captured input hashes remain unchanged, including the initial thirteen. Focused schema/strict checks pass; focused internal chemistry passes, which does not certify external xref agreement.

## Findings

### F1: Exact ChEBI xref represents an additional methyl

major / open / confirmed; issue key: factumycin-chebi-extra-methyl-exact-xref.

Reconcile or exclude CHEBI216503 as an exact xref through the maintained owner: its C45H64N2O10 graph has hemiketal O-methyl where the native/original C44 structure has OH. Do not change the native structure merely to match the external label.

### F2: Exact ChEMBL xref conflicts at assigned stereochemistry

major / open / confirmed; issue key: factumycin-chembl-stereochemistry-exact-xref.

Reconcile CHEMBL3218567 with original stereochemical evidence or exclude the incompatible exact association. Atom mapping finds one opposite assigned tetrahedral centre and two E/Z conflicts in addition to different specificity at another centre.

### F3: The sole definition citation does not support later claims

major / open / confirmed; issue key: factumycin-definition-later-claims-single-1982-citation.

Route the extended definition to claim-appropriate original sources or narrow it to the inspected1982 evidence. PMID7166535 contains fermentation, identity and diffusion assays, not the later Kitasatospora/cluster/Acinetobacter statements.

### F4: Acinetobacter baumannii is misspelled

minor / open / confirmed; issue key: factumycin-acinetobacter-baumanii-spelling.

Correct Acinetobacter baumanii to Acinetobacter baumannii through the maintained definition owner.

## Recommended Actions And Acceptance Checks

### A1

Reconcile or exclude CHEBI216503 as an exact xref through the maintained owner: its C45H64N2O10 graph has hemiketal O-methyl where the native/original C44 structure has OH. Do not change the native structure merely to match the external label.

- Every retained exact xref agrees in full constitutional identity.
- Preserve native C44 identity unless stronger exact original evidence justifies a separately reviewed change; rerun schema/strict and source reproduction.

### A2

Reconcile CHEMBL3218567 with original stereochemical evidence or exclude the incompatible exact association. Atom mapping finds one opposite assigned tetrahedral centre and two E/Z conflicts in addition to different specificity at another centre.

- Document a primary atom-mapped stereochemical reconciliation before selecting a replacement.
- All retained exact xrefs match assigned stereochemistry; do not infer that unspecified native centres are mixtures.

### A3

Route the extended definition to claim-appropriate original sources or narrow it to the inspected1982 evidence. PMID7166535 contains fermentation, identity and diffusion assays, not the later Kitasatospora/cluster/Acinetobacter statements.

- Definition references directly support each retained producer, biosynthetic and spectrum statement.
- Retain the2010 unpublished-result qualifier and original2012 access/strain limits; do not turn database repetition into primary support.

### A4

Correct Acinetobacter baumanii to Acinetobacter baumannii through the maintained definition owner.

- Regenerated definition uses the correct species spelling without broadening strain-specific activity.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/factumycin.yaml; Entire native YAML and every history entry | supports | The SEEDED/MINTED record has 0 synonyms, 1 parents, 3 history events and 1 source concept(s). Every populated field was read, including all exact, drug and document references. The facT entry explicitly labels its evidence as a CARD/ARO database assertion. |
| owners | 424-source-rows.json; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Exact source rows and applicable extraction/seeding rules | supports | The ARO row owns the definition, classification and cross-references, the adopted PubChem row owns the chemical structure, and aro_resistance_edges owns facT. The native MINTED identifier is the reproducible ARO alias. ChEBI rows in the initial generic capture are context rather than the scientific field owner. Original hashes were preserved; no native or maintained file was edited. |
| search | 424-local-hits.txt; 424-owners-search.json; 043-root-fetch-manifest.json through 043-root-fetch8-manifest.json; Ignored-inclusive local discovery and bounded current authority/primary-source access | supports | All native identifiers and adopted publication leads were considered. HTTP200 challenge, error and login responses were not counted as structures or full papers. Search coverage is bounded, not evidence that other literature does not exist. |
| semantics | src/antibioticmech/schema/antibioticmech.yaml; xrefs, drug_xrefs and document_xrefs definitions | supports | Exact xrefs require structural equivalence. Drug-level links may cover parents, salts or stereoisomers, and document references establish relevance rather than equivalence. No broader drug-level association is penalized for a different structural scope. |
| chemistry | 043-authority-compare.json; 424-chemistry.json; Independent parsing, formula/charge/key and stereochemical checks | supports | Native SMILES/InChI and current PubChem135410114 agree on C44H62N2O10 and HMBDLBWGDMNPDW-SUXULKRESA-N, with six assigned and two unassigned tetrahedral centres. ChEBI216503 gives C45H64N2O10 and PNAPQJHXPKPELJ-OXCXFXHNSA-N. ChEMBL3218567 has C44 connectivity but key HMBDLBWGDMNPDW-DQTCXKJJSA-N. Unassigned centres are not evidence of a mixture. |
| adapter | 043-root-adapter-catalog.txt; Actual dataset catalog inspected before mechanism follow-up | supports | The catalog has no matching human host, clove, Kitasatospora setae, WAC5292 or CS62 dataset. Covered bacterial backgrounds do not make human S1P signaling, candidate plant biosynthesis or heterologous facT into endogenous bacterial target evidence. No component membership or unsupported gene identity is invented. |
| aro | ARO:3001220;ARO:3001219;ARO:3001310;ARO:3001313; https://purl.obolibrary.org/obo/aro.obo; Exact current terms in the2026-08-11 ontology and adopted raw rows | supports | Factumycin belongs to the kirromycin-like branch under the broader elfamycin class; seeding its declared drug class is intentional. facT remains a qualified antibiotic-efflux assertion. The drug term repeats the same extended definition and1982 reference; repetition is not primary validation. |
| xref-stereo | 424-chembl-mapped-comparison.json; https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL3218567.json; Independent atom mapping with stereochemistry removed solely for constitutional alignment | supports | Constitutional mapping succeeds, but the methoxy-bearing native atom12 is R versus mapped ChEMBL atom21 S, and native bonds9–10 and17–18 are Z versus E. ChEMBL also assigns a centre left unassigned in native. The opposite assigned stereochemistry alone disproves exact equivalence; this is not merely extra specificity or atom-number-dependent CIP comparison. |
| original1982 | PMID:7166535; DOI:10.7164/antibiotics.35.1705; Complete original three-page article text, actual pp1705–1706 Figure1/Table1 | supports | S. lavendulae ATCC31312/MA4758 fermentation yields factumycin/A40A. The original drawing and elemental formula support C44H62N2O10 with hemiketal OH; the analytical sample includes two waters. Antibacterial Table1 is drop diffusion with15 microliters of1000 micrograms/mL in40% aqueous acetone, not MIC. It covers23 named organisms and both Gram-positive/negative responses; it has no Acinetobacter panel or later genome/biosynthetic-cluster work. |
| original2012 | DOI:10.1039/C2MD20038D; https://pubs.rsc.org/en/content/articlelanding/2012/md/c2md20038d; Complete original publisher abstract; full main and linked supplement retrieval failed | supports | The study reports A. baumannii-guided isolation from Cuban Streptomyces WAC5292, selective Gram-negative activity, a sequenced biosynthetic cluster and heterologous facT expression in sensitive S. coelicolor M1154. It calls FacT an ABC transporter whereas current ARO classifies it as MFS; native asserts only efflux, so no family-class contradiction is inserted. Tetracycline synergy is a combination result. No unavailable numeric MIC or exact construct protocol is invented. |
| original2024 | PMID:38632045; DOI:10.1093/jimb/kuae014; PMC11066910; Original factumycin isolation/identification and cluster Results, Table1, actual Figure3 | supports | Hawaiian Streptomyces CS62 supplies12.1 mg purified factumycin from10L. Figure3 NMR correlations and exact masses support C44H62N2O10 ([M+H]+779.4482). The authors explicitly identify and report correction of an erroneous additional-methyl database structure. The current ChEBI216503 representation has that constitutional problem. CS62/WAC5292 cluster similarities support biosynthesis context, not a fresh experimental proof for every gene or Kitasatospora producer. |
| other-originals | PMID:21059706;29705162;39714192;25621700; Selected exact factumycin main-text passages/tables for the first three; complete original abstract for25621700 | supports | The2010 K. setae NBRC14216T genome assigns an84kb cluster and cites experimental confirmation as unpublished results. The2018 S. globosus crude-extract annotation uses m/z743.4268, inconsistent with factumycin779.4477 protonated mass; its peak/activity is not accepted as purified exact-compound proof. The2025 EF-Tu/tRNA FRET study uses factumycin as a known control; the new MGC10 potency belongs to another compound. The2015 abstract groups FacHI with Dieckmann cyclases; without full experimental parsing it is not a complete exact-enzyme assay ledger. |

## Limits And Additional Notes

- The1982 article and actual Figure1/Table1 were read. Its historical structure is not a modern complete absolute-configuration proof. The2024 reading covers exact identity/cluster Results and Figure3, not every experimental method or supplementary spectrum; the supplement route returned a challenge rather than a ZIP.
- The2012 original was available at complete-abstract depth only; publisher main routes returned403 and linked supplement404. No numeric MIC, purified efflux rate or transporter-family resolution is invented. The2010 producer confirmation is explicitly unpublished.
- The2018 and2025 papers were inspected for exact factumycin passages rather than fully audited; the2015 cyclase article was read only as an abstract. A full experimental stereochemical reconciliation is required before replacing either incompatible xref.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native/source edit or biological sign-off was performed. Independent chemistry used the existing batch019 interpreter against batch043; native gates used batch043. Shared required gates are attached from actual unchanged-base executions during finalization.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T160635Z-factumycin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Factumycin: incompatible exact cross-references and an incomplete definition
  citation'
started_at: '2026-10-21T15:38:19Z'
finished_at: '2026-10-21T16:06:35Z'
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
summary: The native C44 graph agrees with PubChem and original constitutional evidence.
  The exact ChEBI xref instead contains an additional methyl, and ChEMBL differs at
  assigned stereochemistry. The sole 1982 definition citation cannot support later
  biosynthetic and Acinetobacter claims; the taxon spelling also needs correction.
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
  - path: data/antibiotics/antibacterial/factumycin.yaml
    sha256: 8b414bcc53c3e339dc082b536424a9d63746cc0bb87e8d48d826bb938ce76d0f
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
  - path: curation/record_review_queue.tsv
    sha256: 3828a5120b892ee0ee0b776affc6c3e4f1f1a3355ec4edd30e6005762de00e70
    role: context
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
targets:
- target_id: antibioticmech:aro-fdb0f4de1c
  path: data/antibiotics/antibacterial/factumycin.yaml
  label: factumycin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted identity, definition, classification and xrefs
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Qualified facT resistance assertion
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact structure
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding override owner
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 424; entire native record. Original thirteen hashes were
    preserved within 18 actual owner/context inputs before substantive judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-fdb0f4de1c
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-fdb0f4de1c
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/111-chemistry-check.py
    424
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-fdb0f4de1c
  command: just validate data/antibiotics/antibacterial/factumycin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-fdb0f4de1c
  command: just validate-strict data/antibiotics/antibacterial/factumycin.yaml --out
    /private/tmp/am-review-session/424-strict.tsv
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
  - antibioticmech:aro-fdb0f4de1c
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
  - antibioticmech:aro-fdb0f4de1c
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
  - antibioticmech:aro-fdb0f4de1c
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
  - antibioticmech:aro-fdb0f4de1c
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
  - antibioticmech:aro-fdb0f4de1c
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
  - antibioticmech:aro-fdb0f4de1c
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
  - antibioticmech:aro-fdb0f4de1c
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
  - antibioticmech:aro-fdb0f4de1c
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
  - antibioticmech:aro-fdb0f4de1c
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/factumycin.yaml
  locator: Entire native YAML and every history entry
  accessed_at: '2026-10-21T16:01:14Z'
  support: supports
  summary: The SEEDED/MINTED record has 0 synonyms, 1 parents, 3 history events and
    1 source concept(s). Every populated field was read, including all exact, drug
    and document references. The facT entry explicitly labels its evidence as a CARD/ARO
    database assertion.
- evidence_id: owners
  kind: record_content
  reference: 424-source-rows.json; scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  locator: Exact source rows and applicable extraction/seeding rules
  accessed_at: '2026-10-21T16:01:14Z'
  support: supports
  summary: The ARO row owns the definition, classification and cross-references, the
    adopted PubChem row owns the chemical structure, and aro_resistance_edges owns
    facT. The native MINTED identifier is the reproducible ARO alias. ChEBI rows in
    the initial generic capture are context rather than the scientific field owner.
    Original hashes were preserved; no native or maintained file was edited.
  snapshot_sha256: b940dedf5db1779e23c4e43b0596f39f8e7288ddbf8b7acf160d3ef0dcfbe36f
- evidence_id: search
  kind: search
  reference: 424-local-hits.txt; 424-owners-search.json; 043-root-fetch-manifest.json
    through 043-root-fetch8-manifest.json
  locator: Ignored-inclusive local discovery and bounded current authority/primary-source
    access
  accessed_at: '2026-10-21T16:01:14Z'
  support: supports
  summary: All native identifiers and adopted publication leads were considered. HTTP200
    challenge, error and login responses were not counted as structures or full papers.
    Search coverage is bounded, not evidence that other literature does not exist.
  search_scope: Exact native identifier, name and key search with rg --no-ignore --hidden
    across repository data, curation, conf, scripts, src, docs, reviews and reports;
    linked public authorities, EuropePMC and free original publisher/supplement routes.
  snapshot_sha256: 62387ea7fe19f28967881415368321fb82514028f6fc2ee93f0bb64361abfe56
- evidence_id: semantics
  kind: record_content
  reference: src/antibioticmech/schema/antibioticmech.yaml
  locator: xrefs, drug_xrefs and document_xrefs definitions
  accessed_at: '2026-10-21T16:01:14Z'
  support: supports
  summary: Exact xrefs require structural equivalence. Drug-level links may cover
    parents, salts or stereoisomers, and document references establish relevance rather
    than equivalence. No broader drug-level association is penalized for a different
    structural scope.
- evidence_id: chemistry
  kind: validation
  reference: 043-authority-compare.json; 424-chemistry.json
  locator: Independent parsing, formula/charge/key and stereochemical checks
  accessed_at: '2026-10-21T16:01:14Z'
  support: supports
  summary: Native SMILES/InChI and current PubChem135410114 agree on C44H62N2O10 and
    HMBDLBWGDMNPDW-SUXULKRESA-N, with six assigned and two unassigned tetrahedral
    centres. ChEBI216503 gives C45H64N2O10 and PNAPQJHXPKPELJ-OXCXFXHNSA-N. ChEMBL3218567
    has C44 connectivity but key HMBDLBWGDMNPDW-DQTCXKJJSA-N. Unassigned centres are
    not evidence of a mixture.
  snapshot_sha256: 68ec5d3ab452a0f514033cbde3ea4767bc69579f1f6d7df76afbd175e52deb3d
- evidence_id: adapter
  kind: database
  reference: 043-root-adapter-catalog.txt
  locator: Actual dataset catalog inspected before mechanism follow-up
  accessed_at: '2026-10-21T16:01:14Z'
  support: supports
  summary: The catalog has no matching human host, clove, Kitasatospora setae, WAC5292
    or CS62 dataset. Covered bacterial backgrounds do not make human S1P signaling,
    candidate plant biosynthesis or heterologous facT into endogenous bacterial target
    evidence. No component membership or unsupported gene identity is invented.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: aro
  kind: database
  reference: ARO:3001220;ARO:3001219;ARO:3001310;ARO:3001313; https://purl.obolibrary.org/obo/aro.obo
  locator: Exact current terms in the2026-08-11 ontology and adopted raw rows
  accessed_at: '2026-10-21T16:01:14Z'
  support: supports
  summary: Factumycin belongs to the kirromycin-like branch under the broader elfamycin
    class; seeding its declared drug class is intentional. facT remains a qualified
    antibiotic-efflux assertion. The drug term repeats the same extended definition
    and1982 reference; repetition is not primary validation.
  snapshot_sha256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
- evidence_id: xref-stereo
  kind: validation
  reference: 424-chembl-mapped-comparison.json; https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL3218567.json
  locator: Independent atom mapping with stereochemistry removed solely for constitutional
    alignment
  accessed_at: '2026-10-21T16:01:14Z'
  support: supports
  summary: Constitutional mapping succeeds, but the methoxy-bearing native atom12
    is R versus mapped ChEMBL atom21 S, and native bonds9–10 and17–18 are Z versus
    E. ChEMBL also assigns a centre left unassigned in native. The opposite assigned
    stereochemistry alone disproves exact equivalence; this is not merely extra specificity
    or atom-number-dependent CIP comparison.
  snapshot_sha256: 7008d02ed707015fca025a7b403ab9bb0ba38b675be75cc75f5bd9fbfd834c25
- evidence_id: original1982
  kind: primary_source
  reference: PMID:7166535; DOI:10.7164/antibiotics.35.1705
  locator: Complete original three-page article text, actual pp1705–1706 Figure1/Table1
  accessed_at: '2026-10-21T16:01:14Z'
  support: supports
  summary: S. lavendulae ATCC31312/MA4758 fermentation yields factumycin/A40A. The
    original drawing and elemental formula support C44H62N2O10 with hemiketal OH;
    the analytical sample includes two waters. Antibacterial Table1 is drop diffusion
    with15 microliters of1000 micrograms/mL in40% aqueous acetone, not MIC. It covers23
    named organisms and both Gram-positive/negative responses; it has no Acinetobacter
    panel or later genome/biosynthetic-cluster work.
  snapshot_sha256: 7e88662d0f96d87c15352ad9d60b2bde04c181e91912d99a17a13cbfdc835fdb
- evidence_id: original2012
  kind: primary_source
  reference: DOI:10.1039/C2MD20038D; https://pubs.rsc.org/en/content/articlelanding/2012/md/c2md20038d
  locator: Complete original publisher abstract; full main and linked supplement retrieval
    failed
  accessed_at: '2026-10-21T16:01:14Z'
  support: supports
  summary: The study reports A. baumannii-guided isolation from Cuban Streptomyces
    WAC5292, selective Gram-negative activity, a sequenced biosynthetic cluster and
    heterologous facT expression in sensitive S. coelicolor M1154. It calls FacT an
    ABC transporter whereas current ARO classifies it as MFS; native asserts only
    efflux, so no family-class contradiction is inserted. Tetracycline synergy is
    a combination result. No unavailable numeric MIC or exact construct protocol is
    invented.
- evidence_id: original2024
  kind: primary_source
  reference: PMID:38632045; DOI:10.1093/jimb/kuae014; PMC11066910
  locator: Original factumycin isolation/identification and cluster Results, Table1,
    actual Figure3
  accessed_at: '2026-10-21T16:01:14Z'
  support: supports
  summary: Hawaiian Streptomyces CS62 supplies12.1 mg purified factumycin from10L.
    Figure3 NMR correlations and exact masses support C44H62N2O10 ([M+H]+779.4482).
    The authors explicitly identify and report correction of an erroneous additional-methyl
    database structure. The current ChEBI216503 representation has that constitutional
    problem. CS62/WAC5292 cluster similarities support biosynthesis context, not a
    fresh experimental proof for every gene or Kitasatospora producer.
  snapshot_sha256: f62c54c762e4e12884cbf1c1d1140c602c89d4bcde14cd936e5d925fc62d3d40
- evidence_id: other-originals
  kind: primary_source
  reference: PMID:21059706;29705162;39714192;25621700
  locator: Selected exact factumycin main-text passages/tables for the first three;
    complete original abstract for25621700
  accessed_at: '2026-10-21T16:01:14Z'
  support: supports
  summary: The2010 K. setae NBRC14216T genome assigns an84kb cluster and cites experimental
    confirmation as unpublished results. The2018 S. globosus crude-extract annotation
    uses m/z743.4268, inconsistent with factumycin779.4477 protonated mass; its peak/activity
    is not accepted as purified exact-compound proof. The2025 EF-Tu/tRNA FRET study
    uses factumycin as a known control; the new MGC10 potency belongs to another compound.
    The2015 abstract groups FacHI with Dieckmann cyclases; without full experimental
    parsing it is not a complete exact-enzyme assay ledger.
  snapshot_sha256: 5aa764285474385c2f0776993cb9a3bca3c42239ad631b407ab63ffabc1f8eff
assessments:
- assessment_id: identity
  area: identity
  topic: C44 constitution and incompatible exact xrefs
  outcome: concern
  summary: Original1982 and2024 evidence support C44 composition; ChEBI adds a methyl.
    ChEMBL shares connectivity but conflicts in assigned stereochemistry. Native partial
    configuration is not mistaken for a proven mixture, and no complete absolute-configuration
    re-elucidation is claimed.
  target_ids:
  - antibioticmech:aro-fdb0f4de1c
  evidence_ids:
  - native
  - chemistry
  - xref-stereo
  - original1982
  - original2024
  - semantics
- assessment_id: definition
  area: evidence
  topic: Claim-specific source coverage and taxon spelling
  outcome: concern
  summary: The1982 source supports isolation and activity, but not Kitasatospora genomic
    attribution, later cluster characterization or the A. baumannii-guided activity
    scope. Those require the later originals with their actual limits. The intended
    taxon is Acinetobacter baumannii.
  target_ids:
  - antibioticmech:aro-fdb0f4de1c
  evidence_ids:
  - native
  - original1982
  - original2012
  - original2024
  - other-originals
- assessment_id: resistance
  area: evidence
  topic: Qualified facT assertion
  outcome: supported
  summary: The generic efflux database claim is supported at current-source and original2012
    abstract depth. The transporter-family discrepancy and unavailable detailed experiments
    prevent a stronger unqualified primary upgrade.
  target_ids:
  - antibioticmech:aro-fdb0f4de1c
  evidence_ids:
  - native
  - aro
  - original2012
  - adapter
- assessment_id: coverage
  area: completeness
  topic: Optional unasserted fields and review status
  outcome: supported
  summary: All native fields and adopted leads were assessed at their recorded reading
    depth. Optional quantitative activity, targets, graphs, clinical status and expression
    datasets are not automatically required in a SEEDED record. This review does not
    promote native scientific curation status.
  target_ids:
  - antibioticmech:aro-fdb0f4de1c
  evidence_ids:
  - native
  - owners
  - search
- assessment_id: provenance
  area: provenance
  topic: Generated owners and unchanged input ledger
  outcome: supported
  summary: All 18 captured input hashes remain unchanged, including the initial thirteen.
    Focused schema/strict checks pass; focused internal chemistry passes, which does
    not certify external xref agreement.
  target_ids:
  - antibioticmech:aro-fdb0f4de1c
  evidence_ids:
  - owners
  - chemistry
  - search
findings:
- finding_id: F1
  issue_key: factumycin-chebi-extra-methyl-exact-xref
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Exact ChEBI xref represents an additional methyl
  description: 'Reconcile or exclude CHEBI216503 as an exact xref through the maintained
    owner: its C45H64N2O10 graph has hemiketal O-methyl where the native/original
    C44 structure has OH. Do not change the native structure merely to match the external
    label.'
  target_ids:
  - antibioticmech:aro-fdb0f4de1c
  field_paths:
  - xrefs[1]
  evidence_ids:
  - native
  - chemistry
  - original1982
  - original2024
  - semantics
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted identity, definition, classification and xrefs
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding override owner
  rule_id: review-checklist:Identity/Names/Definition
  native_severity: major
  normalization_reason: The finding concerns an asserted exact structure or claim-source
    association.
- finding_id: F2
  issue_key: factumycin-chembl-stereochemistry-exact-xref
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Exact ChEMBL xref conflicts at assigned stereochemistry
  description: Reconcile CHEMBL3218567 with original stereochemical evidence or exclude
    the incompatible exact association. Atom mapping finds one opposite assigned tetrahedral
    centre and two E/Z conflicts in addition to different specificity at another centre.
  target_ids:
  - antibioticmech:aro-fdb0f4de1c
  field_paths:
  - xrefs[2]
  evidence_ids:
  - chemistry
  - xref-stereo
  - semantics
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted identity, definition, classification and xrefs
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding override owner
  rule_id: review-checklist:Identity/Names/Definition
  native_severity: major
  normalization_reason: The finding concerns an asserted exact structure or claim-source
    association.
- finding_id: F3
  issue_key: factumycin-definition-later-claims-single-1982-citation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The sole definition citation does not support later claims
  description: Route the extended definition to claim-appropriate original sources
    or narrow it to the inspected1982 evidence. PMID7166535 contains fermentation,
    identity and diffusion assays, not the later Kitasatospora/cluster/Acinetobacter
    statements.
  target_ids:
  - antibioticmech:aro-fdb0f4de1c
  field_paths:
  - definition_source
  - definition
  evidence_ids:
  - native
  - original1982
  - original2012
  - original2024
  - other-originals
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted identity, definition, classification and xrefs
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding override owner
  rule_id: review-checklist:Evidence
  native_severity: major
  normalization_reason: The finding concerns an asserted exact structure or claim-source
    association.
- finding_id: F4
  issue_key: factumycin-acinetobacter-baumanii-spelling
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: Acinetobacter baumannii is misspelled
  description: Correct Acinetobacter baumanii to Acinetobacter baumannii through the
    maintained definition owner.
  target_ids:
  - antibioticmech:aro-fdb0f4de1c
  field_paths:
  - definition
  evidence_ids:
  - native
  - original2012
  - original2024
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted identity, definition, classification and xrefs
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding override owner
  rule_id: review-checklist:Identity/Names/Definition
  native_severity: minor
  normalization_reason: Local terminology correction does not change the molecular
    identity.
actions:
- action_id: A1
  description: 'Reconcile or exclude CHEBI216503 as an exact xref through the maintained
    owner: its C45H64N2O10 graph has hemiketal O-methyl where the native/original
    C44 structure has OH. Do not change the native structure merely to match the external
    label.'
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-fdb0f4de1c
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted identity, definition, classification and xrefs
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding override owner
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Every retained exact xref agrees in full constitutional identity.
  - Preserve native C44 identity unless stronger exact original evidence justifies
    a separately reviewed change; rerun schema/strict and source reproduction.
- action_id: A2
  description: Reconcile CHEMBL3218567 with original stereochemical evidence or exclude
    the incompatible exact association. Atom mapping finds one opposite assigned tetrahedral
    centre and two E/Z conflicts in addition to different specificity at another centre.
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:aro-fdb0f4de1c
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted identity, definition, classification and xrefs
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding override owner
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Document a primary atom-mapped stereochemical reconciliation before selecting
    a replacement.
  - All retained exact xrefs match assigned stereochemistry; do not infer that unspecified
    native centres are mixtures.
- action_id: A3
  description: Route the extended definition to claim-appropriate original sources
    or narrow it to the inspected1982 evidence. PMID7166535 contains fermentation,
    identity and diffusion assays, not the later Kitasatospora/cluster/Acinetobacter
    statements.
  finding_ids:
  - F3
  target_ids:
  - antibioticmech:aro-fdb0f4de1c
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted identity, definition, classification and xrefs
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding override owner
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Definition references directly support each retained producer, biosynthetic and
    spectrum statement.
  - Retain the2010 unpublished-result qualifier and original2012 access/strain limits;
    do not turn database repetition into primary support.
- action_id: A4
  description: Correct Acinetobacter baumanii to Acinetobacter baumannii through the
    maintained definition owner.
  finding_ids:
  - F4
  target_ids:
  - antibioticmech:aro-fdb0f4de1c
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted identity, definition, classification and xrefs
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding override owner
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Regenerated definition uses the correct species spelling without broadening strain-specific
    activity.
limitations:
- The1982 article and actual Figure1/Table1 were read. Its historical structure is
  not a modern complete absolute-configuration proof. The2024 reading covers exact
  identity/cluster Results and Figure3, not every experimental method or supplementary
  spectrum; the supplement route returned a challenge rather than a ZIP.
- The2012 original was available at complete-abstract depth only; publisher main routes
  returned403 and linked supplement404. No numeric MIC, purified efflux rate or transporter-family
  resolution is invented. The2010 producer confirmation is explicitly unpublished.
- The2018 and2025 papers were inspected for exact factumycin passages rather than
  fully audited; the2015 cyclase article was read only as an abstract. A full experimental
  stereochemical reconciliation is required before replacing either incompatible xref.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native/source edit or biological sign-off was performed. Independent chemistry
  used the existing batch019 interpreter against batch043; native gates used batch043.
  Shared required gates are attached from actual unchanged-base executions during
  finalization.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
