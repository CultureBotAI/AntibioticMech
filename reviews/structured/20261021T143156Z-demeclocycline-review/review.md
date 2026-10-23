# Demeclocycline: correct methyl-position wording and brand typing

- Review: 20261021T143156Z-demeclocycline-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:11:39Z
- Finished UTC: 2026-10-21T14:31:56Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The neutral demeclocycline graph is coherent across parsed authorities, including a PubChem tautomer. The definition incorrectly removes a methyl group from position7 rather than6, and Declomycin is incorrectly typed as an exact chemical synonym. The twelve resistance assertions and16S target remain explicitly database-qualified; hydrochloride product and clinical evidence must retain salt/material scope.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position354; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:4392 | data/antibiotics/antibacterial/demeclocycline.yaml | generated | demeclocycline |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:4392 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:4392 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:4392 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:4392 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:4392 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:4392 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:4392 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:4392 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:4392 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:4392 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:4392 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:4392 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Neutral molecular graph and salt boundary

identity: supported. Targets: CHEBI:4392.

Native complete graph, charge, formula, masses and five specified centres agree. The PubChem alternate tautomer is not a wrong-isomer finding; the HCl drug link remains a contextual drug identifier.

### Structural definition and clinical scope

evidence: concern. Targets: CHEBI:4392.

The opening sentence misnumbers the missing methyl substituent. Slow excretion has label support; historical HCl clinical use has scoped evidence, while individual unverified use claims are retained as access/scope limits rather than certified contemporary indications.

### All eleven synonyms

representation: concern. Targets: CHEBI:4392.

The systematic and6-demethyl7-chloro aliases agree with the graph, as do the INN variants and conventional abbreviations. Declomycin needs BRAND_NAME typing.

### Exact, drug and document identifiers

grounding: supported. Targets: CHEBI:4392.

Accessible structural xrefs agree with the explicit tautomer qualification. All patent document identifiers resolve to relevant production context; restricted registries and DrugBank remain bounded limitations.

### Tetracycline class and antibacterial-drug eligibility

scope: supported. Targets: CHEBI:4392.

The broader parents and antibacterial drug role are coherent with structure and inspected antimicrobial/clinical sources. The free-base identity is retained separately from the named hydrochloride material.

### Twelve resistance assertions and16S target

evidence: supported. Targets: CHEBI:4392.

The record correctly marks these as database assertions and retains the primary-evidence-needed target status. No target binding or exact allele-level phenotype is inferred from family labels or iModulon annotations.

### Activity, producer, products and causal graph

completeness: unknown. Targets: CHEBI:4392.

Optional fields are not required merely because more evidence exists. Any future activity or producer enrichment must retain material, strain and assay identity; a pharmaceutical salt and a fermentation broth do not identify the same preparation.

### Generated source ownership and history

provenance: supported. Targets: CHEBI:4392.

Five generated events remain coherent with SEEDED status. Both adopted citation leads were resolved and inspected at the declared depths, and all original captured inputs remain unchanged.

## Findings

### F1: The definition misnumbers the removed methyl substituent

major / open / confirmed; issue key: demeclocycline-methyl-position-seven-definition.

Demeclocycline is6-demethyl7-chlorotetracycline. The native opening sentence instead says that tetracycline lacks a methyl substituent at7, contradicting its exact aliases and complete structure. Correct the maintained ChEBI-derived definition without changing the supported neutral graph.

### F2: Declomycin is a brand name, not an exact chemical synonym

minor / open / confirmed; issue key: demeclocycline-declomycin-brand-type.

The ARO-derived declomycin alias is EXACT_SYNONYM, but official label and NCI evidence identify a branded hydrochloride tablet product. Retain its useful association with correct BRAND_NAME typing and salt/product scope.

## Recommended Actions And Acceptance Checks

### A1

Correct the maintained structural definition to6-demethyl7-chlorotetracycline.

- Preserve the exact neutral graph and distinguish the hydrochloride context.
- Repair source extraction/harmonization reproducibly and use the canonical writer/history path.
- Pass schema, strict, chemical equivalence, source reproduction and required QC.

### A2

Type Declomycin as a brand association with hydrochloride product scope.

- Use maintained source-specific synonym handling, not a hand edit of generated YAML.
- Retain provenance and check all regenerated synonyms against approved enum typing and source reproduction.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/demeclocycline.yaml; entire YAML; eleven synonyms, six exact xrefs, four drug links, seven documents, twelve resistance assertions, target and five history events | supports | CHEBI4392 denotes neutral C21H21ClN2O8 with five specified centres. No activity_spectrum, causal_graph, clinical product or producer object is populated. The definition explicitly scopes clinical uses mainly to hydrochloride; database resistance and target claims retain their database caveats. |
| owners | data/raw/chebi_antimicrobials.tsv;data/raw/aro_antibiotics.tsv; ChEBI row137 and ARO row166; exact target/resistance rows, source extractor and seeder | supports | ChEBI supplies native definition/graph and most aliases; ARO supplies declomycin, class and twelve resistance assertions. All actual owners were appended to the original capture without refreshing its hashes. The source ARO definition independently says6-methyl and fast absorption, but that definition is not the emitted native text and is not counted as an extra finding. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/4392/; full current compound response, names, structure and relations; native parent/role OLS terms | supports | Current ChEBI repeats the incorrect position7 definition but its complete structure and exact6-demethyl7-chloro aliases agree with the retained graph. CHEBI26895/ARO3000050 are broader tetracycline classes; CHEBI36047 resolves as antibacterial drug. The separate hydrochloride is a has-part neighbor, not the same neutral structure. |
| chemistry | RDKit2026.03.5 / InChI1.07.3; 036-root-chemistry.py;354-authority-chemistry.json | supports | Native SMILES/InChI, ChEBI molfile, ChEMBL1591, DrugCentral802 and KEGG D03680 regenerate FMTDIUIBLCQGJB-SEYHBJAFSA-N. Current PubChem54680690 encodes the tautomer GUXHBMASAHGULD-SEYHBJAFSA-N. Canonical tautomer comparison with sp3/bond stereo removal disabled converges while retaining five assigned centres. KEGG D00290 explicitly includes HCl and belongs in drug_xrefs. Diagnostic assertions exit0. |
| identifiers | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL1591.json;https://drugcentral.org/drug/802/molfile;https://rest.kegg.jp/get/D03680; independently parsed external graphs and current ChEBI registry entries | supports | Accessible exact structure sources agree after the stated tautomer comparison. DrugBank DB00618 returns403. ChemSpider10482117 resolves with the matching formula, systematic names and five of five defined stereocentres; no downloadable graph was independently obtained. CAS127-33-3 and Beilstein2230579 are source-attested; the proprietary registries were not accessed. The initial ChEBI structure route returned SVG and the guessed DrugCentral API returned404; correct official molfile routes were subsequently parsed. |
| original-structure | https://patents.google.com/patent/US2878289A/en; original1959 patent Description: structural proposal,6-methyl/7-halogen paragraph and free-base/salt comparisons | supports | The original describes demethyltetracycline congeners as differing at the6-methyl group, with halogen at7. It explicitly qualifies the then-proposed structure as not proven by unequivocal synthesis. The current parsed graphs and exact systematic aliases independently resolve the positional question, so the finding does not depend on treating that historical proposal as definitive alone. |
| documents | patent:FR1344645;US3012946;US3019172;US3050446;US3154476; all native patent pages resolved; US descriptions and relevant production paragraphs, FR bibliographic title | supports | All six patent identifiers resolve to tetracycline/demethyltetracycline production documents. US3012946 describes7-chloro6-demethyl production by S.aureofaciens ATCC12551 and rice-bran-oil-sludge fermentation comparisons; US3019172 uses methylation inhibitors; US3050446 concerns relative congener production; US3154476 uses homocysteine-related supplements. These are production context, not modern clinical efficacy. FR text was not independently translated. The native Wikipedia document resolves to the expected topic and is not primary scientific support. |
| brand | https://www.accessdata.fda.gov/drugsatfda_docs/label/2008/050261s100lbl.pdf; historical NDA050261 label description and product presentation; current NCI drug dictionary | supports | The official label identifies Declomycin as150/300mg demeclocycline hydrochloride tablets, and the NCI dictionary explicitly calls it the US brand. It is a product name associated with salt formulations, not an exact neutral-molecule synonym. |
| clinical | https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=539add06-e0a0-401a-b4f6-20776084aa9c; Amneal SPL effective2026-04-02; Description, Clinical Pharmacology and Indications; separate historical2008 label | supports | Both labels describe the hydrochloride, with slower absorption than tetracycline and renal clearance less than half that of tetracycline. The current label supports bacterial infection and severe-acne adjunct context, with susceptibility restrictions. It does not independently establish every ChEBI use, such as Lyme disease, or justify generalizing salt products to an exact free-base formulation. This review is not a treatment recommendation or a contemporary treatment-policy assessment. |
| adopted-siad | https://doi.org/10.1001/jama.237.25.2723; PMID194065 complete indexed abstract | supports | The1977 seven-patient study explicitly used demeclocycline hydrochloride and reports correction of hyponatremia with hypotonic urine despite large fluid intake. Its historical efficacy conclusion is material- and cohort-specific; full methods were not recovered and it is not evidence for a current treatment-of-choice recommendation. |
| adopted-aging | https://doi.org/10.1111/acel.12163; PMID24134630/PMC3955372; complete abstract, Table1 and antibacterial-food-control Results | supports | The compound in Table1 is demeclocycline hydrochloride, not isolated neutral free base. The study records16% C.elegans lifespan increase and separately observes inhibition of feeding-strain E.coli OP50 growth by all three antibiotic hits at1.5 times their optimized lifespan concentration. This supports a bounded antibacterial observation and illustrates confounding of longevity by bacterial food effects. Annotated30S pharmacology in the table is not a new direct16S binding experiment. |
| card | https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms; ARO3000667,3000755 and all twelve resistance terms; frozen exact source edges | supports | All identifiers resolve and the current term descriptions support the coarse protein functions: ten ribosomal-protection families, TetX inactivation and LmrP efflux. The native16S target explicitly remains PRIMARY_EVIDENCE_NEEDED. Current annotation and source-edge reproduction establish database provenance, not exact demeclocycline binding, allele-specific resistance or measured MIC for every family. |
| adapter | https://imodulondb.org/api/datasets; 036-root-adapter.json; covered datasets and gene queries before open mechanism research | supports | The S.aureus tet query returns tet38 and TetR-like annotation matches, not exact experimental support for the retained protection families. The E.coli precise1k tetX query has no gene/module hits. These bounded computational searches are not evidence that the mechanisms are absent or present experimentally. |
| uk-siad | https://www.medicines.org.uk/emc/product/100035/smpc; Section4.1 Therapeutic indications of the hydrochloride product | supports | The UK SmPC limits its SIADH indication to chronic hyponatraemia secondary to malignant disease, ineffective water restriction and absence of concomitant cirrhosis. This corroborates a selected clinical-use context, not a recommendation for all SIADH or proof of neutral free-base formulation equivalence. |

## Limits And Additional Notes

- The full1957 JACS original returned403; the relevant original1959 patent description was inspected instead, with its explicitly provisional historical structural wording preserved. Current independently parsed graphs resolve the methyl-position comparison.
- All native patent identifiers resolved. Relevant US description/production passages were read, not every experimental example or raw spectrum; the French patent was verified at bibliographic-title depth only.
- The adopted1977 SIADH source was read at complete-abstract depth. The2013 aging paper was read for Table1 and relevant bacterial-control Results; raw supplementary growth curves were not reprocessed.
- The clinical definition is historical broad-use prose, not a verified current recommendation or uniform indication list. Current labeling supports specific susceptible-infection/acne contexts, but this review does not independently establish the Lyme-disease use or all bronchitis settings.
- DrugBank returned403 and ChemSpider supplied matching identity metadata and defined-centre count, without an independently parsed graph. CAS and Beilstein were source-attested without proprietary register access.
- The twelve resistance mechanisms remain database-qualified; no exhaustive primary-paper proof of each exact allele/demeclocycline combination was attempted. The structured adapter results cannot prove direct binding or resistance.
- All initial hashes were preserved and all repository searches used hidden/ignored-inclusive matching. No native scientific status or product was edited.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T143156Z-demeclocycline-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Demeclocycline: correct methyl-position wording and brand typing'
started_at: '2026-10-21T14:11:39Z'
finished_at: '2026-10-21T14:31:56Z'
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
summary: The neutral demeclocycline graph is coherent across parsed authorities, including
  a PubChem tautomer. The definition incorrectly removes a methyl group from position7
  rather than6, and Declomycin is incorrectly typed as an exact chemical synonym.
  The twelve resistance assertions and16S target remain explicitly database-qualified;
  hydrochloride product and clinical evidence must retain salt/material scope.
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
  - path: data/antibiotics/antibacterial/demeclocycline.yaml
    sha256: 2816d588aa9ff3e61c566f785c7c3f540b169bb316f78d719e664bb17916d813
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
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
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
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: context
  - path: data/raw/fda_clinical_status.tsv
    sha256: a6952f85426afa53c5704c588681a078e599ce245bf18f7c9dd390d70e7bb16c
    role: context
  - path: scripts/card_evidence_reviews.py
    sha256: f9ec8aff30066bf04b9c2757af7d6f5d179d045e57b9f3b352bbed0b851f50a8
    role: context
targets:
- target_id: CHEBI:4392
  path: data/antibiotics/antibacterial/demeclocycline.yaml
  label: demeclocycline
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
  selection: Initially uncovered queue position354; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:4392
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:4392
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    354
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:4392
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/demeclocycline.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:4392
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/demeclocycline.yaml --out /private/tmp/am-review-session/354-strict.tsv
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
  - CHEBI:4392
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
  - CHEBI:4392
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
  - CHEBI:4392
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
  - CHEBI:4392
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
  - CHEBI:4392
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
  - CHEBI:4392
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
  - CHEBI:4392
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
  - CHEBI:4392
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
  - CHEBI:4392
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/demeclocycline.yaml
  locator: entire YAML; eleven synonyms, six exact xrefs, four drug links, seven documents,
    twelve resistance assertions, target and five history events
  accessed_at: '2026-10-21T14:23:47Z'
  support: supports
  summary: CHEBI4392 denotes neutral C21H21ClN2O8 with five specified centres. No
    activity_spectrum, causal_graph, clinical product or producer object is populated.
    The definition explicitly scopes clinical uses mainly to hydrochloride; database
    resistance and target claims retain their database caveats.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv;data/raw/aro_antibiotics.tsv
  locator: ChEBI row137 and ARO row166; exact target/resistance rows, source extractor
    and seeder
  accessed_at: '2026-10-21T14:23:47Z'
  support: supports
  summary: ChEBI supplies native definition/graph and most aliases; ARO supplies declomycin,
    class and twelve resistance assertions. All actual owners were appended to the
    original capture without refreshing its hashes. The source ARO definition independently
    says6-methyl and fast absorption, but that definition is not the emitted native
    text and is not counted as an extra finding.
  snapshot_sha256: dd49236c1201d1e971bd9e52d172ad1e4a4793765585df0267e1c01324189526
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/4392/
  locator: full current compound response, names, structure and relations; native
    parent/role OLS terms
  accessed_at: '2026-10-21T14:23:47Z'
  support: supports
  summary: Current ChEBI repeats the incorrect position7 definition but its complete
    structure and exact6-demethyl7-chloro aliases agree with the retained graph. CHEBI26895/ARO3000050
    are broader tetracycline classes; CHEBI36047 resolves as antibacterial drug. The
    separate hydrochloride is a has-part neighbor, not the same neutral structure.
  snapshot_sha256: 0d92e78d43effc1a9678fc923171fabe453f19f04d2a36da4febd69bb50861af
- evidence_id: chemistry
  kind: validation
  reference: RDKit2026.03.5 / InChI1.07.3
  locator: 036-root-chemistry.py;354-authority-chemistry.json
  accessed_at: '2026-10-21T14:23:47Z'
  support: supports
  summary: Native SMILES/InChI, ChEBI molfile, ChEMBL1591, DrugCentral802 and KEGG
    D03680 regenerate FMTDIUIBLCQGJB-SEYHBJAFSA-N. Current PubChem54680690 encodes
    the tautomer GUXHBMASAHGULD-SEYHBJAFSA-N. Canonical tautomer comparison with sp3/bond
    stereo removal disabled converges while retaining five assigned centres. KEGG
    D00290 explicitly includes HCl and belongs in drug_xrefs. Diagnostic assertions
    exit0.
  snapshot_sha256: 640fe9271a12f9adce9ec372ddba0db62e5672631cc38afea9d708e0ab09793f
- evidence_id: identifiers
  kind: authority
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL1591.json;https://drugcentral.org/drug/802/molfile;https://rest.kegg.jp/get/D03680
  locator: independently parsed external graphs and current ChEBI registry entries
  accessed_at: '2026-10-21T14:23:47Z'
  support: supports
  summary: Accessible exact structure sources agree after the stated tautomer comparison.
    DrugBank DB00618 returns403. ChemSpider10482117 resolves with the matching formula,
    systematic names and five of five defined stereocentres; no downloadable graph
    was independently obtained. CAS127-33-3 and Beilstein2230579 are source-attested;
    the proprietary registries were not accessed. The initial ChEBI structure route
    returned SVG and the guessed DrugCentral API returned404; correct official molfile
    routes were subsequently parsed.
  snapshot_sha256: 864c4d9d5d293d4c7e41f8c1d78a2d7f9c762530a23ccd1dd59b36dde8354768
- evidence_id: original-structure
  kind: primary_source
  reference: https://patents.google.com/patent/US2878289A/en
  locator: 'original1959 patent Description: structural proposal,6-methyl/7-halogen
    paragraph and free-base/salt comparisons'
  accessed_at: '2026-10-21T14:23:47Z'
  support: supports
  summary: The original describes demethyltetracycline congeners as differing at the6-methyl
    group, with halogen at7. It explicitly qualifies the then-proposed structure as
    not proven by unequivocal synthesis. The current parsed graphs and exact systematic
    aliases independently resolve the positional question, so the finding does not
    depend on treating that historical proposal as definitive alone.
  snapshot_sha256: 3d6d8022ea462c58b0be72feb3b4c472a11b3e85a5e2e188a9cc9b7b5c37261c
- evidence_id: documents
  kind: primary_source
  reference: patent:FR1344645;US3012946;US3019172;US3050446;US3154476
  locator: all native patent pages resolved; US descriptions and relevant production
    paragraphs, FR bibliographic title
  accessed_at: '2026-10-21T14:23:47Z'
  support: supports
  summary: All six patent identifiers resolve to tetracycline/demethyltetracycline
    production documents. US3012946 describes7-chloro6-demethyl production by S.aureofaciens
    ATCC12551 and rice-bran-oil-sludge fermentation comparisons; US3019172 uses methylation
    inhibitors; US3050446 concerns relative congener production; US3154476 uses homocysteine-related
    supplements. These are production context, not modern clinical efficacy. FR text
    was not independently translated. The native Wikipedia document resolves to the
    expected topic and is not primary scientific support.
- evidence_id: brand
  kind: authority
  reference: https://www.accessdata.fda.gov/drugsatfda_docs/label/2008/050261s100lbl.pdf
  locator: historical NDA050261 label description and product presentation; current
    NCI drug dictionary
  accessed_at: '2026-10-21T14:23:47Z'
  support: supports
  summary: The official label identifies Declomycin as150/300mg demeclocycline hydrochloride
    tablets, and the NCI dictionary explicitly calls it the US brand. It is a product
    name associated with salt formulations, not an exact neutral-molecule synonym.
  snapshot_sha256: 1a2a07faf7791f3dc03763d05b479719567849fd8daadf1f3c4e76af51a9347a
- evidence_id: clinical
  kind: authority
  reference: https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=539add06-e0a0-401a-b4f6-20776084aa9c
  locator: Amneal SPL effective2026-04-02; Description, Clinical Pharmacology and
    Indications; separate historical2008 label
  accessed_at: '2026-10-21T14:23:47Z'
  support: supports
  summary: Both labels describe the hydrochloride, with slower absorption than tetracycline
    and renal clearance less than half that of tetracycline. The current label supports
    bacterial infection and severe-acne adjunct context, with susceptibility restrictions.
    It does not independently establish every ChEBI use, such as Lyme disease, or
    justify generalizing salt products to an exact free-base formulation. This review
    is not a treatment recommendation or a contemporary treatment-policy assessment.
  snapshot_sha256: 8e78588acc3df700a546a9afda662ff9d0d109ab00557089e52d50d1fe61e174
- evidence_id: adopted-siad
  kind: primary_source
  reference: https://doi.org/10.1001/jama.237.25.2723
  locator: PMID194065 complete indexed abstract
  accessed_at: '2026-10-21T14:23:47Z'
  support: supports
  summary: The1977 seven-patient study explicitly used demeclocycline hydrochloride
    and reports correction of hyponatremia with hypotonic urine despite large fluid
    intake. Its historical efficacy conclusion is material- and cohort-specific; full
    methods were not recovered and it is not evidence for a current treatment-of-choice
    recommendation.
  snapshot_sha256: ba7c00f8baf4b23f7589dc38b82eec0479a1c31d6f2adaef1b6d99a9eb5a11d7
- evidence_id: adopted-aging
  kind: primary_source
  reference: https://doi.org/10.1111/acel.12163
  locator: PMID24134630/PMC3955372; complete abstract, Table1 and antibacterial-food-control
    Results
  accessed_at: '2026-10-21T14:23:47Z'
  support: supports
  summary: The compound in Table1 is demeclocycline hydrochloride, not isolated neutral
    free base. The study records16% C.elegans lifespan increase and separately observes
    inhibition of feeding-strain E.coli OP50 growth by all three antibiotic hits at1.5
    times their optimized lifespan concentration. This supports a bounded antibacterial
    observation and illustrates confounding of longevity by bacterial food effects.
    Annotated30S pharmacology in the table is not a new direct16S binding experiment.
  snapshot_sha256: 0437e8114d4a736a9339c6e67054d2ea187301eb3b29dea2d21b531086b258ae
- evidence_id: card
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/aro/terms
  locator: ARO3000667,3000755 and all twelve resistance terms; frozen exact source
    edges
  accessed_at: '2026-10-21T14:23:47Z'
  support: supports
  summary: 'All identifiers resolve and the current term descriptions support the
    coarse protein functions: ten ribosomal-protection families, TetX inactivation
    and LmrP efflux. The native16S target explicitly remains PRIMARY_EVIDENCE_NEEDED.
    Current annotation and source-edge reproduction establish database provenance,
    not exact demeclocycline binding, allele-specific resistance or measured MIC for
    every family.'
  snapshot_sha256: 780bd6270dc510a8749155a7be26e9314a64dc770a65be89ce93059d2e199bfd
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: 036-root-adapter.json; covered datasets and gene queries before open mechanism
    research
  accessed_at: '2026-10-21T14:23:47Z'
  support: supports
  summary: The S.aureus tet query returns tet38 and TetR-like annotation matches,
    not exact experimental support for the retained protection families. The E.coli
    precise1k tetX query has no gene/module hits. These bounded computational searches
    are not evidence that the mechanisms are absent or present experimentally.
  snapshot_sha256: 069dd406397dca0b77ba4f44807c1a9b5f9756b3a4db4ba40ce72d7b1e2a2db1
- evidence_id: uk-siad
  kind: authority
  reference: https://www.medicines.org.uk/emc/product/100035/smpc
  locator: Section4.1 Therapeutic indications of the hydrochloride product
  accessed_at: '2026-10-21T14:25:36Z'
  support: supports
  summary: The UK SmPC limits its SIADH indication to chronic hyponatraemia secondary
    to malignant disease, ineffective water restriction and absence of concomitant
    cirrhosis. This corroborates a selected clinical-use context, not a recommendation
    for all SIADH or proof of neutral free-base formulation equivalence.
assessments:
- assessment_id: identity
  area: identity
  topic: Neutral molecular graph and salt boundary
  outcome: supported
  summary: Native complete graph, charge, formula, masses and five specified centres
    agree. The PubChem alternate tautomer is not a wrong-isomer finding; the HCl drug
    link remains a contextual drug identifier.
  target_ids:
  - CHEBI:4392
  evidence_ids:
  - native
  - chemistry
  - chebi
- assessment_id: definition
  area: evidence
  topic: Structural definition and clinical scope
  outcome: concern
  summary: The opening sentence misnumbers the missing methyl substituent. Slow excretion
    has label support; historical HCl clinical use has scoped evidence, while individual
    unverified use claims are retained as access/scope limits rather than certified
    contemporary indications.
  target_ids:
  - CHEBI:4392
  evidence_ids:
  - chebi
  - original-structure
  - clinical
  - adopted-siad
  - uk-siad
- assessment_id: synonyms
  area: representation
  topic: All eleven synonyms
  outcome: concern
  summary: The systematic and6-demethyl7-chloro aliases agree with the graph, as do
    the INN variants and conventional abbreviations. Declomycin needs BRAND_NAME typing.
  target_ids:
  - CHEBI:4392
  evidence_ids:
  - native
  - brand
  - chebi
- assessment_id: groundings
  area: grounding
  topic: Exact, drug and document identifiers
  outcome: supported
  summary: Accessible structural xrefs agree with the explicit tautomer qualification.
    All patent document identifiers resolve to relevant production context; restricted
    registries and DrugBank remain bounded limitations.
  target_ids:
  - CHEBI:4392
  evidence_ids:
  - chemistry
  - identifiers
  - documents
- assessment_id: classification
  area: scope
  topic: Tetracycline class and antibacterial-drug eligibility
  outcome: supported
  summary: The broader parents and antibacterial drug role are coherent with structure
    and inspected antimicrobial/clinical sources. The free-base identity is retained
    separately from the named hydrochloride material.
  target_ids:
  - CHEBI:4392
  evidence_ids:
  - chebi
  - brand
  - clinical
  - adopted-aging
- assessment_id: mechanism
  area: evidence
  topic: Twelve resistance assertions and16S target
  outcome: supported
  summary: The record correctly marks these as database assertions and retains the
    primary-evidence-needed target status. No target binding or exact allele-level
    phenotype is inferred from family labels or iModulon annotations.
  target_ids:
  - CHEBI:4392
  evidence_ids:
  - native
  - card
  - adapter
- assessment_id: optional
  area: completeness
  topic: Activity, producer, products and causal graph
  outcome: unknown
  summary: Optional fields are not required merely because more evidence exists. Any
    future activity or producer enrichment must retain material, strain and assay
    identity; a pharmaceutical salt and a fermentation broth do not identify the same
    preparation.
  target_ids:
  - CHEBI:4392
  evidence_ids:
  - native
  - adopted-aging
  - documents
  - clinical
- assessment_id: provenance
  area: provenance
  topic: Generated source ownership and history
  outcome: supported
  summary: Five generated events remain coherent with SEEDED status. Both adopted
    citation leads were resolved and inspected at the declared depths, and all original
    captured inputs remain unchanged.
  target_ids:
  - CHEBI:4392
  evidence_ids:
  - owners
  - native
  - adopted-aging
  - adopted-siad
findings:
- finding_id: F1
  issue_key: demeclocycline-methyl-position-seven-definition
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The definition misnumbers the removed methyl substituent
  description: Demeclocycline is6-demethyl7-chlorotetracycline. The native opening
    sentence instead says that tetracycline lacks a methyl substituent at7, contradicting
    its exact aliases and complete structure. Correct the maintained ChEBI-derived
    definition without changing the supported neutral graph.
  target_ids:
  - CHEBI:4392
  field_paths:
  - definition
  evidence_ids:
  - native
  - chebi
  - chemistry
  - original-structure
  - owners
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
  rule_id: native-review-checklist:Identity
  native_severity: major inaccurate chemical definition
  normalization_reason: The graph is correctly identified, but the explicit positional
    structural assertion is chemically wrong and inherited from the maintained source.
- finding_id: F2
  issue_key: demeclocycline-declomycin-brand-type
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Declomycin is a brand name, not an exact chemical synonym
  description: The ARO-derived declomycin alias is EXACT_SYNONYM, but official label
    and NCI evidence identify a branded hydrochloride tablet product. Retain its useful
    association with correct BRAND_NAME typing and salt/product scope.
  target_ids:
  - CHEBI:4392
  field_paths:
  - synonyms[10]
  evidence_ids:
  - brand
  - owners
  - native
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Imported declomycin synonym
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source-specific alias extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Synonym typing and validated generation
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Source-scoped synonym configuration
  rule_id: native-review-checklist:Nomenclature
  native_severity: minor name-type defect
  normalization_reason: This does not invalidate the molecular graph but can make
    product names look like exact molecular identities.
actions:
- action_id: A1
  description: Correct the maintained structural definition to6-demethyl7-chlorotetracycline.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:4392
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
  acceptance_checks:
  - Preserve the exact neutral graph and distinguish the hydrochloride context.
  - Repair source extraction/harmonization reproducibly and use the canonical writer/history
    path.
  - Pass schema, strict, chemical equivalence, source reproduction and required QC.
- action_id: A2
  description: Type Declomycin as a brand association with hydrochloride product scope.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:4392
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Imported declomycin synonym
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source-specific alias extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Synonym typing and validated generation
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Source-scoped synonym configuration
  acceptance_checks:
  - Use maintained source-specific synonym handling, not a hand edit of generated
    YAML.
  - Retain provenance and check all regenerated synonyms against approved enum typing
    and source reproduction.
limitations:
- The full1957 JACS original returned403; the relevant original1959 patent description
  was inspected instead, with its explicitly provisional historical structural wording
  preserved. Current independently parsed graphs resolve the methyl-position comparison.
- All native patent identifiers resolved. Relevant US description/production passages
  were read, not every experimental example or raw spectrum; the French patent was
  verified at bibliographic-title depth only.
- The adopted1977 SIADH source was read at complete-abstract depth. The2013 aging
  paper was read for Table1 and relevant bacterial-control Results; raw supplementary
  growth curves were not reprocessed.
- The clinical definition is historical broad-use prose, not a verified current recommendation
  or uniform indication list. Current labeling supports specific susceptible-infection/acne
  contexts, but this review does not independently establish the Lyme-disease use
  or all bronchitis settings.
- DrugBank returned403 and ChemSpider supplied matching identity metadata and defined-centre
  count, without an independently parsed graph. CAS and Beilstein were source-attested
  without proprietary register access.
- The twelve resistance mechanisms remain database-qualified; no exhaustive primary-paper
  proof of each exact allele/demeclocycline combination was attempted. The structured
  adapter results cannot prove direct binding or resistance.
- All initial hashes were preserved and all repository searches used hidden/ignored-inclusive
  matching. No native scientific status or product was edited.
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
