# Chlorhexidine: salt names incorrectly treated as exact free-base synonyms

- Review: 20261021T125734Z-chlorhexidine-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:36:41Z
- Finished UTC: 2026-10-21T12:57:34Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One major identity correction is required: three ARO-derived salt names are marked as exact synonyms of the neutral free-base record. The molecular graph itself is coherent. The Eis enzyme measurement matches the original paper, and four resistance items faithfully declare database-only provenance; primary follow-up sharply limits their host, material and phenotype interpretation. Neither enzyme inhibition nor generic resistance links establish the full antibacterial killing mechanism.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position290; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:3614 | data/antibiotics/antibacterial/chlorhexidine.yaml | generated | chlorhexidine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:3614 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:3614 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:3614 | Actual focused execution exited 0. |
| Structured adapter before open research | passed | False | CHEBI:3614 | Catalog and applicable organism gene searches completed; empty component results and absent dataset coverage were kept separate from biological negatives. |
| Authoritative full QC | failed | True | CHEBI:3614 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:3614 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:3614 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:3614 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:3614 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:3614 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:3614 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:3614 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:3614 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Source ownership and history

provenance: supported. Targets: CHEBI:3614.

Maintained source rows and owning extraction/seeding paths were inspected. Initial provenance hashes remain unchanged; source-only and experimental assertions are distinguished.

### Focused documented gates

schema: supported. Targets: CHEBI:3614.

Schema and strict validation passed; independent native chemistry also passed. These checks do not establish biological truth or scientific REVIEWED status.

### Free-base identity and salt aliases

identity: concern. Targets: CHEBI:3614.

Native molecular encoding is internally coherent; three exact synonym assertions cross salt boundaries and need maintained correction.

### Measured Eis association

evidence: supported. Targets: CHEBI:3614.

Original central IC50 and assay match. The native relation accurately records measured enzyme association rather than primary killing mechanism; the protein example stays explicitly unreviewed.

### Database-only resistance evidence

evidence: supported. Targets: CHEBI:3614.

All four source assertions and qualifiers are faithful. Primary evidence has specific salt, expression-host and statistical limits that must accompany future enrichment. No source-only edge is silently promoted to direct transport proof.

### Main antibacterial mechanism and optional detail

completeness: unknown. Targets: CHEBI:3614.

The record does not assert a mode enum or causal graph. The exact Eis measurement does not fill that gap. Additional membrane experiments on specified salts may inform future curation with the material scope made explicit. Optional missing fields are not a second defect.

### Remaining external links

grounding: unknown. Targets: CHEBI:3614.

Full molecular agreement is established for the accessible chemical authorities. LINCS LSM-5633 was not found in the inspected official HMS archive subset; that subset is not the full LINCS registry. Reaxys/VSDB access is limited. These are unresolved mapping checks, not proved wrong links.

## Findings

### F1: Remove exact-synonym equivalence between chlorhexidine free base and its salts

major / open / confirmed; issue key: chlorhexidine-free-base-exact-salt-aliases.

Native synonyms[4], [5] and [6] label acetate, digluconate and gluconate as EXACT_SYNONYM for single-component CHEBI:3614. Independent full molecular comparisons establish distinct multi-component salts already represented by CHEBI:81711 and CHEBI:28312. The generic ARO alias list is broader than molecular identity and must not become exact chemical synonym equivalence.

## Recommended Actions And Acceptance Checks

### A1

Correct ARO-derived salt aliases through the maintained normalization/seeding path while preserving distinct records.

- No acetate or gluconate name remains an EXACT_SYNONYM of the free base.
- Retain related discoverability only through an appropriate non-exact relationship supported by the schema; preserve distinct salt structures and identifiers.
- Do not transfer salt product approvals, strain MICs or formulated antiseptic endpoints onto the free-base record.
- Regeneration reproduces the correction and focused identity/schema/strict plus applicable corpus gates pass.

### A2

Optionally qualify primary target/resistance details with exact experimental scope.

- Keep Eis14±4 micromolar enzyme inhibition separate from antibacterial killing and retain the tested reagent ambiguity until resolved.
- Preserve PmpM heterologous gluconate phenotype and native-host no-change result; retain AbuO/KpnEF/AadT host and statistical limitations.
- Do not infer direct chlorhexidine transport from dye export, or natural-host resistance from recombinant expression alone.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/chlorhexidine.yaml; Entire native YAML, all populated domains and all history events | supports | Read the whole native record without changing it. All initial captured hashes were retained; actual source-owner inputs were appended before detailed assessment. |
| owners | 290-raw-rows.json; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Exact source rows and applicable source assembly/attachment functions | supports | Inspected adopted rows against the native fields, including identifier, source mint, chemical fields, parents, roles, synonyms and source/history scope. Provenance agreement is distinguished from scientific validation. |
| chemistry | 290-chemistry.json; 029-xref-check.json; Independent RDKit native encoding and official external structure comparisons | supports | Native SMILES and InChI agree on the full key, formula, charge, masses and fragment/stereochemical scope. Official external molecular comparisons described below preserve salts and configured stereochemistry. |
| search | 029-local-hits.txt; official source retrieval and original-paper follow-up; Ignored-inclusive local source/curation search; bounded official and primary-source discovery | supports | Local searches included hidden and ignored files in the stated repository source/curation scope. Adopted citation leads were resolved separately from additional discovery. No claim of an exhaustive literature search is made. |
| identity | CHEBI:3614; KEGG:C06902/D07668; ChEMBL:CHEMBL790; PubChem:9552079; DrugBank:DB00878; Complete native/current official molecular comparisons; DrugBank visible structure fields | supports | Native and inspected official structures agree on neutral single-component chlorhexidine, C22H30Cl2N10, GHXZTYHSJHQHIJ-UHFFFAOYSA-N. There are no tetrahedral stereocenters. DrugBank displays the same full key and free-base SMILES. Broader biguanide, monochlorobenzene and disinfectant classes are appropriate. The standardized free-base graph is distinct from the three-component acetate and digluconate records; protonation in solution is a separate issue. |
| salt-aliases | CHEBI:3614; CHEBI:81711; CHEBI:28312; ARO:3007039; Native synonyms[4:7], exact adopted ARO row and independently checked salt structures | refutes | The ARO source supplies chlorhexidine acetate, chlorhexidine digluconate and chlorhexidine gluconate as generic aliases; native assembly types all three EXACT_SYNONYM. Diacetate has WDRFFJWBUDTUCA-UHFFFAOYSA-N and C26H38Cl2N10O4; digluconate has YZIYKJHYYHPJIB-UUPCJSQJSA-N and C34H54Cl2N10O14. Both include additional chemical components. Thus these are related salt names, not exact names of the native free-base molecule. Current ARO repetition does not make exact equivalence true. |
| eis | PMID:25928210; DOI:10.1021/acs.biochem.5b00244; PMC4671295; Original main article Materials/Methods, Table3, inhibition Results and relevant Discussion; BindingDB exact row293339/monomer152706 | supports | Table3 gives chlorhexidine EisBan IC50 14±4 micromolar, matching native central 14000 nM. Purified Eis from B. anthracis Sterne was tested with neomycin, acetyl-CoA and DTNB in 50 mM Tris pH8, 10% DMSO; Ellman absorbance reports acetylation inhibition. The paper calls the Sigma reagent chlorhexidine without a catalog/salt declaration in inspected main text. This is an enzyme-inhibition association, not a Kd, whole-cell MIC or demonstrated bactericidal target. Native MEASURED_TARGET_ASSOCIATION faithfully preserves that scope; other Eis species values are not transferred. |
| protein | UniProtKB:A0A3P1UAV8; Complete current UniProt JSON, organism, entry status, names, sequence metadata | supports | The accession resolves to an unreviewed 385-aa GNAT-family acetyltransferase in B. anthracis (taxon1392). Native UNREVIEWED status and organism are accurate. The protein example is a reference annotation; exact sequence identity to the experimental Sterne BAS2743 construct was not independently established and is not claimed. |
| resistance | ARO:3004077; ARO:3004578; ARO:3004585; ARO:3007669; All four exact raw resistance rows and current CARD determinant pages | supports | PmpM, AbuO, KpnEF and aadT source edges and efflux labels match. Each native entry explicitly identifies a CARD database assertion rather than a primary citation. The generic chlorhexidine drug concept does not independently settle the salt tested, expression host, quantitative endpoint or direct transport mechanism. |
| pmpm | PMID:14679249; DOI:10.1128/JB.186.1.262-265.2004; PMC303449; Full main narrative, table and figure captions | supports | P. aeruginosa PmpM expressed in E. coli KAM32 raises chlorhexidine-gluconate MIC from4.5 to18 microgram/mL. The tested P. aeruginosa deletion/parent/complement conditions each give5, showing no chlorhexidine MIC shift in that native-host comparison. Direct dye transport/proton coupling experiments do not directly measure chlorhexidine transport. The fourfold heterologous phenotype must not be generalized to every P. aeruginosa strain or free-base preparation. |
| abuo | PMID:25512405; PMC4335886; Relevant strain/methods, deletion/complement results and Figure6 caption | partial | The A. baumannii AbuO study reports bounded deletion/complement survival and growth effects under chlorhexidine exposure; the 3.2 microgram/mL comparison is about1.2-fold with P=.001. Other dye-efflux experiments do not prove direct chlorhexidine transport. Salt identity and exact assay material require further method verification before exact-free-base quantitative enrichment. |
| kpnef | PMID:23836167; PMC3754300; Relevant Methods/Results and Figure6 caption | partial | The K. pneumoniae NTUH-K2044 KpnEF study reports a twofold heterologous E. coli chlorhexidine MIC effect with data not shown. A6.39-fold CFU comparison at12.8 microgram/mL has P=.07508 and is not statistically significant. Individual components do not reproduce the paired phenotype. Direct transport of other dyes and generic efflux annotation are distinct from measured chlorhexidine transport; one textual susceptibility-direction inconsistency remains a limit on quantitative interpretation. |
| aadt | PMID:37252766; PMC10268838; Full main Methods/Results/Discussion narrative and captions | supports | AadT from A. nosocomialis AC1530 plasmid pAC1530 was synthesized with a C-terminal tag and expressed from an induced plasmid in E. coli BL21. Broth-microdilution and growth data support a bounded chlorhexidine phenotype in that host. Direct ethidium export is not direct chlorhexidine export. Native-host clinical resistance and a particular free-base formulation cannot be inferred from this recombinant system. |
| adapter | kg-microbe-sources imodulondb; 290-adapter-results.json; catalog and organism-matched gene searches before open research | context_only | The structured adapter was queried first. P. aeruginosa precise364 resolves PmpM/PA1361 but returns no components; A. baumannii precise139 searches for AbuO/aadT return none. The catalog has no matching K. pneumoniae or B. anthracis dataset. These coverage/results do not disprove resistance or mechanism, and no homologous-organism substitute was used. |
| leads | PMID:10848923;11564456;16238008;17602516;24384684;33786648;33805369;33850179;33863402;13172429; All nine adopted ChEBI complete abstracts, ARO original1954 paper all five scanned pages | partial | The nine ChEBI leads concern allergy, taste with gluconate, a bibliographic review, cellulose sorption, port-infection cohort, propolis-mouthrinse comparison, Fusarium treatment, Acanthamoeba combinations and mouse wound healing. They do not establish an exact bacterial free-base target. PMID13172429 directly studies predominantly diacetate and some dihydrochloride while drawing the parent base; it does not report gluconate clinical mouthwash evidence. Its antibacterial observations remain salt/material-specific. No quantitative result is transferred across salts. |
| drugcentral | https://www.drugcentral.org/drugcard/597; Official molfile, InChI and SMILES downloads; 029-extra-chemistry.json | supports | All three independently parsed DrugCentral encodings reproduce the native free-base full key. Its broad drug synonym list does not imply exact molecular equivalence of salts. An additional ChemSpider comparison also matches the free base. |

## Limits And Additional Notes

- The original Eis main article was inspected in the relevant methods/results/table/discussion; the attempted supporting PDF returned a small HTML challenge, so its reagent structure figure was not read. Exact experimental Sterne/reference-protein sequence identity was not independently checked.
- PmpM and AadT main narratives/tables/captions were read; AbuO and KpnEF were read in the relevant methods/results/caption sections. Figure pixels and all supplementary experiments were not independently audited.
- The nine adopted ChEBI leads were inspected at complete abstract depth. Their full assay/clinical protocols are not claimed as verified.
- LINCS archive search covered only the official HMS downloadable subset, not all LINCS registrations. Proprietary Reaxys and unavailable VSDB content remain unverified; no dead-link or identity defect is inferred from access failure alone.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native record, maintained input, scientific status or history was changed. This review is evidence for separately authorized curation, not status promotion.
- Root completed the entire native-record audit, preserved every captured input hash and inspected each adopted literature lead at the explicitly documented depth. Final saved conclusions retain all access, material, organism and assay boundaries.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T125734Z-chlorhexidine-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Chlorhexidine: salt names incorrectly treated as exact free-base synonyms'
started_at: '2026-10-21T12:36:41Z'
finished_at: '2026-10-21T12:57:34Z'
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
summary: 'One major identity correction is required: three ARO-derived salt names
  are marked as exact synonyms of the neutral free-base record. The molecular graph
  itself is coherent. The Eis enzyme measurement matches the original paper, and four
  resistance items faithfully declare database-only provenance; primary follow-up
  sharply limits their host, material and phenotype interpretation. Neither enzyme
  inhibition nor generic resistance links establish the full antibacterial killing
  mechanism.'
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
  - path: data/antibiotics/antibacterial/chlorhexidine.yaml
    sha256: 09093926720375f83d1b246e80df4009a2200b51958ce3620d879c10efad2ce3
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 25f0d80c0bf26da7741a1514a5e1759dde484ab054f0f56df7938bdda8383a91
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
  - path: data/raw/bindingdb_target_measurements.tsv
    sha256: faccfe5634f467801aeb256e6560af09d193cdb53bdbf29dea195c9c0488c480
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
  - path: scripts/extract_bindingdb_targets.py
    sha256: 9914a61b93326808b9800f3680dc935af2abcfa1e9925d6c3dd39180dbc78a2d
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
- target_id: CHEBI:3614
  path: data/antibiotics/antibacterial/chlorhexidine.yaml
  label: chlorhexidine
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
    role: ChEBI activity role label resolution
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: CARD/ARO identity and aliases
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: CARD/ARO source-owned resistance assertions
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: CARD/ARO source-owned molecular target assertions
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/bindingdb_target_measurements.tsv
    role: BindingDB literature-curated quantitative measurement
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_bindingdb_targets.py
    role: BindingDB assay selection and exact-structure join
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position290; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:3614
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3614
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    290
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3614
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/chlorhexidine.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:3614
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/chlorhexidine.yaml --out /private/tmp/am-review-session/290-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: structured-adapter
  name: Structured adapter before open research
  status: passed
  required: false
  summary: Catalog and applicable organism gene searches completed; empty component
    results and absent dataset coverage were kept separate from biological negatives.
  target_ids:
  - CHEBI:3614
  evidence_ids:
  - adapter
  command: PYTHONDONTWRITEBYTECODE=1 kg-microbe-sources imodulondb; see 290-adapter-results.json
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
  - CHEBI:3614
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
  - CHEBI:3614
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
  - CHEBI:3614
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
  - CHEBI:3614
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
  - CHEBI:3614
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
  - CHEBI:3614
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
  - CHEBI:3614
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
  - CHEBI:3614
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
  - CHEBI:3614
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/chlorhexidine.yaml
  locator: Entire native YAML, all populated domains and all history events
  accessed_at: '2026-10-21T12:52:33Z'
  support: supports
  summary: Read the whole native record without changing it. All initial captured
    hashes were retained; actual source-owner inputs were appended before detailed
    assessment.
- evidence_id: owners
  kind: record_content
  reference: 290-raw-rows.json; scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  locator: Exact source rows and applicable source assembly/attachment functions
  accessed_at: '2026-10-21T12:52:33Z'
  support: supports
  summary: Inspected adopted rows against the native fields, including identifier,
    source mint, chemical fields, parents, roles, synonyms and source/history scope.
    Provenance agreement is distinguished from scientific validation.
  snapshot_sha256: 148e7f01824aafc1af31544e56dff30e40bb065e931d7b0b789d0aa9766cd4d6
- evidence_id: chemistry
  kind: validation
  reference: 290-chemistry.json; 029-xref-check.json
  locator: Independent RDKit native encoding and official external structure comparisons
  accessed_at: '2026-10-21T12:52:33Z'
  support: supports
  summary: Native SMILES and InChI agree on the full key, formula, charge, masses
    and fragment/stereochemical scope. Official external molecular comparisons described
    below preserve salts and configured stereochemistry.
  snapshot_sha256: b1433eeb3283cb7184b449137e94818af747000ec8da3193df3c0fbf5f21b827
- evidence_id: search
  kind: search
  reference: 029-local-hits.txt; official source retrieval and original-paper follow-up
  locator: Ignored-inclusive local source/curation search; bounded official and primary-source
    discovery
  accessed_at: '2026-10-21T12:52:33Z'
  support: supports
  summary: Local searches included hidden and ignored files in the stated repository
    source/curation scope. Adopted citation leads were resolved separately from additional
    discovery. No claim of an exhaustive literature search is made.
  search_scope: Exact compound names/identifiers in conf, curation, data/raw, scripts
    and docs using rg --no-ignore --hidden; official registries and original-paper
    sources retrieved 2026-10-21.
  snapshot_sha256: d9a197c22e7a2a8497755404097bbdde15925d25a022cebdd7e38c3162d58d94
- evidence_id: identity
  kind: authority
  reference: CHEBI:3614; KEGG:C06902/D07668; ChEMBL:CHEMBL790; PubChem:9552079; DrugBank:DB00878
  locator: Complete native/current official molecular comparisons; DrugBank visible
    structure fields
  accessed_at: '2026-10-21T12:52:33Z'
  support: supports
  summary: Native and inspected official structures agree on neutral single-component
    chlorhexidine, C22H30Cl2N10, GHXZTYHSJHQHIJ-UHFFFAOYSA-N. There are no tetrahedral
    stereocenters. DrugBank displays the same full key and free-base SMILES. Broader
    biguanide, monochlorobenzene and disinfectant classes are appropriate. The standardized
    free-base graph is distinct from the three-component acetate and digluconate records;
    protonation in solution is a separate issue.
  snapshot_sha256: 2bd3073de0a4ad66b0f52af0c65894f7dc6651bfc914cac8b6bd3f8c79fae70e
- evidence_id: salt-aliases
  kind: authority
  reference: CHEBI:3614; CHEBI:81711; CHEBI:28312; ARO:3007039
  locator: Native synonyms[4:7], exact adopted ARO row and independently checked salt
    structures
  accessed_at: '2026-10-21T12:52:33Z'
  support: refutes
  summary: The ARO source supplies chlorhexidine acetate, chlorhexidine digluconate
    and chlorhexidine gluconate as generic aliases; native assembly types all three
    EXACT_SYNONYM. Diacetate has WDRFFJWBUDTUCA-UHFFFAOYSA-N and C26H38Cl2N10O4; digluconate
    has YZIYKJHYYHPJIB-UUPCJSQJSA-N and C34H54Cl2N10O14. Both include additional chemical
    components. Thus these are related salt names, not exact names of the native free-base
    molecule. Current ARO repetition does not make exact equivalence true.
  snapshot_sha256: 148e7f01824aafc1af31544e56dff30e40bb065e931d7b0b789d0aa9766cd4d6
- evidence_id: eis
  kind: primary_source
  reference: PMID:25928210; DOI:10.1021/acs.biochem.5b00244; PMC4671295
  locator: Original main article Materials/Methods, Table3, inhibition Results and
    relevant Discussion; BindingDB exact row293339/monomer152706
  accessed_at: '2026-10-21T12:52:33Z'
  support: supports
  summary: Table3 gives chlorhexidine EisBan IC50 14±4 micromolar, matching native
    central 14000 nM. Purified Eis from B. anthracis Sterne was tested with neomycin,
    acetyl-CoA and DTNB in 50 mM Tris pH8, 10% DMSO; Ellman absorbance reports acetylation
    inhibition. The paper calls the Sigma reagent chlorhexidine without a catalog/salt
    declaration in inspected main text. This is an enzyme-inhibition association,
    not a Kd, whole-cell MIC or demonstrated bactericidal target. Native MEASURED_TARGET_ASSOCIATION
    faithfully preserves that scope; other Eis species values are not transferred.
  snapshot_sha256: faa76f3f50939f9936d2467de8303bf44646ce7e6d9fe110194fe907661f9dac
- evidence_id: protein
  kind: authority
  reference: UniProtKB:A0A3P1UAV8
  locator: Complete current UniProt JSON, organism, entry status, names, sequence
    metadata
  accessed_at: '2026-10-21T12:52:33Z'
  support: supports
  summary: The accession resolves to an unreviewed 385-aa GNAT-family acetyltransferase
    in B. anthracis (taxon1392). Native UNREVIEWED status and organism are accurate.
    The protein example is a reference annotation; exact sequence identity to the
    experimental Sterne BAS2743 construct was not independently established and is
    not claimed.
  snapshot_sha256: 498f0e4bb59b550a741f34fb5e05cb81ab5432a3403063312131bb6c67517c3b
- evidence_id: resistance
  kind: database
  reference: ARO:3004077; ARO:3004578; ARO:3004585; ARO:3007669
  locator: All four exact raw resistance rows and current CARD determinant pages
  accessed_at: '2026-10-21T12:52:33Z'
  support: supports
  summary: PmpM, AbuO, KpnEF and aadT source edges and efflux labels match. Each native
    entry explicitly identifies a CARD database assertion rather than a primary citation.
    The generic chlorhexidine drug concept does not independently settle the salt
    tested, expression host, quantitative endpoint or direct transport mechanism.
  snapshot_sha256: 148e7f01824aafc1af31544e56dff30e40bb065e931d7b0b789d0aa9766cd4d6
- evidence_id: pmpm
  kind: primary_source
  reference: PMID:14679249; DOI:10.1128/JB.186.1.262-265.2004; PMC303449
  locator: Full main narrative, table and figure captions
  accessed_at: '2026-10-21T12:52:33Z'
  support: supports
  summary: P. aeruginosa PmpM expressed in E. coli KAM32 raises chlorhexidine-gluconate
    MIC from4.5 to18 microgram/mL. The tested P. aeruginosa deletion/parent/complement
    conditions each give5, showing no chlorhexidine MIC shift in that native-host
    comparison. Direct dye transport/proton coupling experiments do not directly measure
    chlorhexidine transport. The fourfold heterologous phenotype must not be generalized
    to every P. aeruginosa strain or free-base preparation.
  snapshot_sha256: 2856c76378571caad18bbddd9476200c16cbacd53916158de819ff94f185e678
- evidence_id: abuo
  kind: primary_source
  reference: PMID:25512405; PMC4335886
  locator: Relevant strain/methods, deletion/complement results and Figure6 caption
  accessed_at: '2026-10-21T12:52:33Z'
  support: partial
  summary: The A. baumannii AbuO study reports bounded deletion/complement survival
    and growth effects under chlorhexidine exposure; the 3.2 microgram/mL comparison
    is about1.2-fold with P=.001. Other dye-efflux experiments do not prove direct
    chlorhexidine transport. Salt identity and exact assay material require further
    method verification before exact-free-base quantitative enrichment.
  snapshot_sha256: 29dca1a0ff222ef81315988f7229d079925caf35a880ab8bd4dd38f653d4a8a6
- evidence_id: kpnef
  kind: primary_source
  reference: PMID:23836167; PMC3754300
  locator: Relevant Methods/Results and Figure6 caption
  accessed_at: '2026-10-21T12:52:33Z'
  support: partial
  summary: The K. pneumoniae NTUH-K2044 KpnEF study reports a twofold heterologous
    E. coli chlorhexidine MIC effect with data not shown. A6.39-fold CFU comparison
    at12.8 microgram/mL has P=.07508 and is not statistically significant. Individual
    components do not reproduce the paired phenotype. Direct transport of other dyes
    and generic efflux annotation are distinct from measured chlorhexidine transport;
    one textual susceptibility-direction inconsistency remains a limit on quantitative
    interpretation.
  snapshot_sha256: a23e5825bef986e49e58f51defdc37ecb2c19f9a51a9290fa1599362994e9777
- evidence_id: aadt
  kind: primary_source
  reference: PMID:37252766; PMC10268838
  locator: Full main Methods/Results/Discussion narrative and captions
  accessed_at: '2026-10-21T12:52:33Z'
  support: supports
  summary: AadT from A. nosocomialis AC1530 plasmid pAC1530 was synthesized with a
    C-terminal tag and expressed from an induced plasmid in E. coli BL21. Broth-microdilution
    and growth data support a bounded chlorhexidine phenotype in that host. Direct
    ethidium export is not direct chlorhexidine export. Native-host clinical resistance
    and a particular free-base formulation cannot be inferred from this recombinant
    system.
  snapshot_sha256: dd6e9f7d18c279d2e29548165e8fb29306f6dd4b27936112e94e07e2ed72d1f5
- evidence_id: adapter
  kind: database
  reference: kg-microbe-sources imodulondb
  locator: 290-adapter-results.json; catalog and organism-matched gene searches before
    open research
  accessed_at: '2026-10-21T12:52:33Z'
  support: context_only
  summary: The structured adapter was queried first. P. aeruginosa precise364 resolves
    PmpM/PA1361 but returns no components; A. baumannii precise139 searches for AbuO/aadT
    return none. The catalog has no matching K. pneumoniae or B. anthracis dataset.
    These coverage/results do not disprove resistance or mechanism, and no homologous-organism
    substitute was used.
  snapshot_sha256: 3afc81196c795df94f0ffa04c2837288f235e142bd2bc7ea0d6e175a9ba029f2
- evidence_id: leads
  kind: primary_source
  reference: PMID:10848923;11564456;16238008;17602516;24384684;33786648;33805369;33850179;33863402;13172429
  locator: All nine adopted ChEBI complete abstracts, ARO original1954 paper all five
    scanned pages
  accessed_at: '2026-10-21T12:52:33Z'
  support: partial
  summary: The nine ChEBI leads concern allergy, taste with gluconate, a bibliographic
    review, cellulose sorption, port-infection cohort, propolis-mouthrinse comparison,
    Fusarium treatment, Acanthamoeba combinations and mouse wound healing. They do
    not establish an exact bacterial free-base target. PMID13172429 directly studies
    predominantly diacetate and some dihydrochloride while drawing the parent base;
    it does not report gluconate clinical mouthwash evidence. Its antibacterial observations
    remain salt/material-specific. No quantitative result is transferred across salts.
  snapshot_sha256: 322a79ba13c41095fe03b17fccabdabaab852da45155da3f9d8bbfd3eb083ed3
- evidence_id: drugcentral
  kind: authority
  reference: https://www.drugcentral.org/drugcard/597
  locator: Official molfile, InChI and SMILES downloads; 029-extra-chemistry.json
  accessed_at: '2026-10-21T12:57:15Z'
  support: supports
  summary: All three independently parsed DrugCentral encodings reproduce the native
    free-base full key. Its broad drug synonym list does not imply exact molecular
    equivalence of salts. An additional ChemSpider comparison also matches the free
    base.
  snapshot_sha256: baf2cda56a543db71357af4c0bd920a45e0f672e152fce79782960223bf08283
assessments:
- assessment_id: provenance
  area: provenance
  topic: Source ownership and history
  outcome: supported
  summary: Maintained source rows and owning extraction/seeding paths were inspected.
    Initial provenance hashes remain unchanged; source-only and experimental assertions
    are distinguished.
  target_ids:
  - CHEBI:3614
  evidence_ids:
  - native
  - owners
- assessment_id: validation
  area: schema
  topic: Focused documented gates
  outcome: supported
  summary: Schema and strict validation passed; independent native chemistry also
    passed. These checks do not establish biological truth or scientific REVIEWED
    status.
  target_ids:
  - CHEBI:3614
  evidence_ids:
  - chemistry
- assessment_id: identity
  area: identity
  topic: Free-base identity and salt aliases
  outcome: concern
  summary: Native molecular encoding is internally coherent; three exact synonym assertions
    cross salt boundaries and need maintained correction.
  target_ids:
  - CHEBI:3614
  evidence_ids:
  - identity
  - salt-aliases
  - chemistry
- assessment_id: target
  area: evidence
  topic: Measured Eis association
  outcome: supported
  summary: Original central IC50 and assay match. The native relation accurately records
    measured enzyme association rather than primary killing mechanism; the protein
    example stays explicitly unreviewed.
  target_ids:
  - CHEBI:3614
  evidence_ids:
  - eis
  - protein
  - owners
- assessment_id: resistance
  area: evidence
  topic: Database-only resistance evidence
  outcome: supported
  summary: All four source assertions and qualifiers are faithful. Primary evidence
    has specific salt, expression-host and statistical limits that must accompany
    future enrichment. No source-only edge is silently promoted to direct transport
    proof.
  target_ids:
  - CHEBI:3614
  evidence_ids:
  - resistance
  - pmpm
  - abuo
  - kpnef
  - aadt
- assessment_id: primary
  area: completeness
  topic: Main antibacterial mechanism and optional detail
  outcome: unknown
  summary: The record does not assert a mode enum or causal graph. The exact Eis measurement
    does not fill that gap. Additional membrane experiments on specified salts may
    inform future curation with the material scope made explicit. Optional missing
    fields are not a second defect.
  target_ids:
  - CHEBI:3614
  evidence_ids:
  - native
  - eis
  - leads
- assessment_id: registry
  area: grounding
  topic: Remaining external links
  outcome: unknown
  summary: Full molecular agreement is established for the accessible chemical authorities.
    LINCS LSM-5633 was not found in the inspected official HMS archive subset; that
    subset is not the full LINCS registry. Reaxys/VSDB access is limited. These are
    unresolved mapping checks, not proved wrong links.
  target_ids:
  - CHEBI:3614
  evidence_ids:
  - identity
  - search
findings:
- finding_id: F1
  issue_key: chlorhexidine-free-base-exact-salt-aliases
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Remove exact-synonym equivalence between chlorhexidine free base and its
    salts
  description: Native synonyms[4], [5] and [6] label acetate, digluconate and gluconate
    as EXACT_SYNONYM for single-component CHEBI:3614. Independent full molecular comparisons
    establish distinct multi-component salts already represented by CHEBI:81711 and
    CHEBI:28312. The generic ARO alias list is broader than molecular identity and
    must not become exact chemical synonym equivalence.
  target_ids:
  - CHEBI:3614
  field_paths:
  - synonyms[4]
  - synonyms[5]
  - synonyms[6]
  evidence_ids:
  - native
  - owners
  - identity
  - salt-aliases
  rule_id: Exact chemical identity and salt/base separation
  native_severity: major
  normalization_reason: Wrong exact salt aliases can merge chemical identities and
    transfer assay or clinical evidence between compounds; the native base graph itself
    is not wrong.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Generic salt aliases adopted from ARO
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Exact chemical synonym typing and source merge
actions:
- action_id: A1
  description: Correct ARO-derived salt aliases through the maintained normalization/seeding
    path while preserving distinct records.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:3614
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Generic salt aliases adopted from ARO
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Exact chemical synonym typing and source merge
  acceptance_checks:
  - No acetate or gluconate name remains an EXACT_SYNONYM of the free base.
  - Retain related discoverability only through an appropriate non-exact relationship
    supported by the schema; preserve distinct salt structures and identifiers.
  - Do not transfer salt product approvals, strain MICs or formulated antiseptic endpoints
    onto the free-base record.
  - Regeneration reproduces the correction and focused identity/schema/strict plus
    applicable corpus gates pass.
- action_id: A2
  description: Optionally qualify primary target/resistance details with exact experimental
    scope.
  finding_ids: []
  target_ids:
  - CHEBI:3614
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/chlorhexidine.yaml
    role: Curator-owned primary evidence and assay qualifications
  acceptance_checks:
  - Keep Eis14±4 micromolar enzyme inhibition separate from antibacterial killing
    and retain the tested reagent ambiguity until resolved.
  - Preserve PmpM heterologous gluconate phenotype and native-host no-change result;
    retain AbuO/KpnEF/AadT host and statistical limitations.
  - Do not infer direct chlorhexidine transport from dye export, or natural-host resistance
    from recombinant expression alone.
limitations:
- The original Eis main article was inspected in the relevant methods/results/table/discussion;
  the attempted supporting PDF returned a small HTML challenge, so its reagent structure
  figure was not read. Exact experimental Sterne/reference-protein sequence identity
  was not independently checked.
- PmpM and AadT main narratives/tables/captions were read; AbuO and KpnEF were read
  in the relevant methods/results/caption sections. Figure pixels and all supplementary
  experiments were not independently audited.
- The nine adopted ChEBI leads were inspected at complete abstract depth. Their full
  assay/clinical protocols are not claimed as verified.
- LINCS archive search covered only the official HMS downloadable subset, not all
  LINCS registrations. Proprietary Reaxys and unavailable VSDB content remain unverified;
  no dead-link or identity defect is inferred from access failure alone.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native record, maintained input, scientific status or history was changed. This
  review is evidence for separately authorized curation, not status promotion.
- Root completed the entire native-record audit, preserved every captured input hash
  and inspected each adopted literature lead at the explicitly documented depth. Final
  saved conclusions retain all access, material, organism and assay boundaries.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
