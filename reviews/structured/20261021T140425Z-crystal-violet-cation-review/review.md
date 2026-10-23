# Crystal violet cation: coherent exact cation identity with bounded active-moiety evidence

- Review: 20261021T140425Z-crystal-violet-cation-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T13:49:08Z
- Finished UTC: 2026-10-21T14:04:25Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

No corrective native-record finding was established. The single +1 crystal-violet cation is distinct from the adjacent chloride salt, and its ChEBI, PubChem and DrugCentral structure encodings agree. ChEBI explicitly supports iminium classification and antibacterial/antifungal roles. Primary studies of gentian-violet reagents support activity at active-moiety scope, without proving an independently isolated counterion-free experimental material. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire native definition, all seven synonyms, iminium parent, two roles, complete structure/properties, CAS and Reaxys xrefs, DrugCentral drug-level link, source concept and all four history events. No citation lead is adopted in the exact source row; bounded original antibacterial and antifungal follow-up assessed.

Selection: Queue 331; original thirteen inputs preserved.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:77181 | data/antibiotics/antibacterial/crystal-violet-cation.yaml | generated | crystal violet cation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:77181 | Actual focused schema validation found no issues. |
| strict | passed | True | CHEBI:77181 | One file scanned; zero strict errors. |
| chemistry | passed | False | CHEBI:77181 | Native SMILES and InChI reproduce the stored full key, charge, element counts and rounded masses; no stereocentres occur and the source mint reproduces. Formula spelling/order is normalized for comparison while charge is checked separately. |
| external-chemistry | passed | False | CHEBI:77181 | Comparison script completed and explicitly reports form differences; this is not a blanket identity pass. ChEBI, PubChem and DrugCentral reproduce the cation; ChEBI, PubChem, KEGG and GSRS reproduce the chloride. All six RCSB CVI encodings reproduce only the cation. |
| Authoritative full QC | failed | True | CHEBI:77181 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:77181 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:77181 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:77181 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:77181 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:77181 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:77181 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:77181 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:77181 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Antibacterial/antifungal filing and experimental scope

evidence: supported. Targets: CHEBI:77181.

ChEBI explicitly assigns both roles, and original studies provide bounded Staphylococcus and Candida activity. Filing priority is reproduced. Preserve distinctions between the exact ionic form, test material, MIC, subculture bactericidal endpoint, biofilm biomass and clinical observations.

### Optional molecular mechanism and response fields

evidence: unknown. Targets: CHEBI:77181.

No native molecular mechanism is asserted. Cellular morphology or reduced fungal biomass does not prove a specific protein target; the available review hypotheses require exact-compound primary follow-up before enrichment.

### Maintained source ownership, seed status and historical inputs

provenance: supported. Targets: CHEBI:77181.

The complete source row and all native history events reconcile with the seed pathway. Initial hashes are retained and actual owners are captured. SEEDED does not imply scientific review, and this observation does not promote native status.

### Exact cation identity, synonyms and identifier scope

identity: supported. Targets: CHEBI:77181.

The native cation graph, seven cation aliases, masses and charge are coherent. DrugCentral is correctly typed as a drug-level link. The adjacent salt is a distinct record, not a duplicate to merge based on shared chromophore.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optionally enrich exact-material primary activity evidence while preserving the cation/salt distinction.

- Identify the actual tested reagent, salt and composition before adding measurements. Do not copy chloride concentrations as independently tested counterion-free cation measurements.
- Keep cellular effects and review hypotheses separate from directly demonstrated microbial molecular targets. Validate any authorized additions with native evidence and schema/strict gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/chebi_role_names.tsv; conf/sources.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; data/raw/MANIFEST.yaml; Complete exact ChEBI row 1957 and adjacent-form row; relevant role/name extraction, synonym, xref partitioning, mint and priority code. | supports | The native ChEBI identity, definition, aliases, parent, roles, structure and source version reproduce the maintained row. ChEBI confirmed names are extracted, brand and INN types are preserved, and ANTIBACTERIAL priority outranks ANTIFUNGAL without deleting either role. The cation source row contains no adopted citation leads. |
| roles | CHEBI:33282; CHEBI:35718; CHEBI:35286; Current official ChEBI parent and role entries and exact entry relations. | supports | The parent is iminium ion, structurally broader than the exact cation. Both antibacterial and antifungal role relations are explicit. The antibacterial definition includes a substance or its active part; role scope does not require that the isolated counterion-free cation was weighed as an experimental bulk material. |
| antibacterial | DOI:10.11150/kansenshogakuzasshi1970.66.914; https://www.jstage.jst.go.jp/article/kansenshogakuzasshi1970/66/7/66_7_914/_pdf; Entire original 1992 paper main text pp914–922 read from extracted Japanese text, English abstract and captions; tabular images and electron micrographs not independently reprocessed. | supports | Saji explicitly identifies gentiana violet/pyoktanin blue as methylrosanilinium chloride and uses Wako reagent-grade material, without a lot-specific purity certificate. The study tests 66 MRSA and 42 MSSA clinical isolates plus S. aureus ATCC6538. Broth bactericidal endpoints are subculture/no-growth endpoints, separate from agar MIC for four MRSA isolates because dye interferes with turbidity. It also reports a small uncontrolled twelve-patient topical series. Electron-microscope changes after treatment are cellular observations, not direct target binding. This provides active-moiety context for the cation role; it is not an exact counterion-free material assay and no numerical result is transferred to this record. |
| antifungal | PMID:21444708; DOI:10.1128/AAC.01601-10; PMC3101405; Complete original main article HTML including Methods, Results, Table 1, Discussion and figure captions. Figure images and raw data not independently reprocessed. | supports | Six oral Candida isolates from HIV-infected patients were tested with Sigma-Aldrich gentian violet of unspecified catalog/purity/counterion certification. CLSI M27-A3 planktonic MICs, germination and 48-hour PMMA biofilm dry weight/architecture are distinct endpoints. At 4 micrograms/mL, Table 1 has significant biomass reductions for four of six isolates, not universal biofilm elimination. The authors did not measure biofilm viability with XTT and did not establish a molecular mechanism. Some prose calls thickness changes significant despite listed p values above 0.05; those significance claims are not adopted. The cation role is supported at active-moiety scope, not by a separately characterized unsalted test material. |
| mechanism-context | PMID:2272286; DOI:10.3109/03602539009041083; PMC4396813; Complete indexed abstract of the adopted 1990 review and selected mechanism discussion of the later review; discovery context only. | context_only | Reviews discuss multiple proposed mechanisms across bacterial, fungal, host-cell and protozoan systems. The later review explicitly distinguishes brilliant-green thioredoxin-reductase work from gentian violet. These summaries do not establish an exact bacterial molecular target or justify transferring host NADPH-oxidase effects, photodynamic conditions or a sibling dye’s covalent target to either native record. |
| adapter | Structured source applicability assessment; Native assertions and maintained rows inspected before mechanism follow-up. | context_only | Neither record asserts a gene, protein, locus, regulator, pathway, stress response or transcriptomics dataset. The iModulonDB adapter is not applicable to these native chemical/role and regulatory assertions. Mechanism hypotheses encountered in reviews are not promoted into native claims. |
| search | 331332-inclusive-hits.txt;331332-literature.json;331332-primary-followup.json; Ignored-inclusive exact-label, identifier, full-key and product search plus bounded public literature/authority follow-up. | context_only | Both distinct native forms and their ChEBI source rows were found. The precise maintained-table scan found no adopted ARO, molecular-target, resistance, MIBiG or curator evidence row for these exact entities; no mechanism absence is inferred from a default ignored-aware search. Many broad crystal-violet hits use the dye as a biomass stain or degradation substrate and are not antimicrobial assays. No optional missing field is treated as a defect. |
| validation | 331-schema.log;331-strict.log;331-chemistry.json;331332-xref-chemistry.json; Actual focused checks, external chemistry comparisons and captured-input hash recheck. | supports | Schema, strict and native chemistry checks exit 0. The corrected external comparison script also exits 0 while reporting CVI as cation-only. Its first scratch attempt mistakenly tried to parse an InChIKey descriptor as SMILES; that helper error is retained in 331332-xref-chemistry-initial.log and was corrected before the final comparison. No native chemistry defect follows from that helper error. All captured input hashes remain unchanged. |
| native | data/antibiotics/antibacterial/crystal-violet-cation.yaml; Entire native YAML. | supports | CHEBI:77181 is SEEDED/EXACT/ANTIBACTERIAL, with +1 C25H30N3 and full key LGLFFNDHMLKUMI-UHFFFAOYSA-N. Seven aliases explicitly denote the cation; the chloride counterion is absent by design. The definition’s minor inherited spelling typo does not alter chemical meaning. No clinical-status or product assertion is populated. |
| identity | https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:77181; pubchem.compound:3468; cas:7438-46-2; Complete current ChEBI entry and PubChem molecular properties, independently parsed. | supports | Native SMILES/InChI, mass, element count and +1 charge agree with current ChEBI and PubChem CID3468. The iminium name and dimethylamino substitution description are coherent with the graph; the shared aromatic resonance representation does not make a new isomer. ChEBI explicitly distinguishes the chloride CHEBI:41688 by a has-part relation. CAS 7438-46-2 is attested for the cation; no chloride salt identifier is imported as an exact native xref. |
| drug | https://drugcentral.org/drugcard/4138; https://drugcentral.org/drug/4138/smiles; Full public DrugCentral page and actual SMILES endpoint. | context_only | The DrugCentral structure independently yields the exact cation key. Its broader drug page also uses the gentian-violet name, chloride CAS and mixture prose; native drug_xrefs explicitly permits drug-level aggregation across forms. That wording is not an assertion that the native cation graph is a mixture. DrugCentral predictions and human receptor annotations are not native microbial target evidence. |

## Limits And Additional Notes

- The primary antibacterial paper identifies chloride reagent material but does not provide a lot-specific composition/purity certificate; the antifungal paper only identifies a Sigma-Aldrich gentian-violet reagent. No quantitative endpoint is silently assigned to separately isolated counterion-free cation or to every historical gentian-violet mixture.
- The 1992 Japanese main text and English abstract were read; tables embedded as images and electron micrographs were not independently reprocessed. Its English abstract rounds the lowest MIC differently from the Japanese results, and the time-kill caption and prose have differing inoculum/replicate descriptions. No numerical observation is curated from those ambiguities.
- Reaxys registry entries were not independently accessed through a paid service. Their exact numbers are verified as adopted/current ChEBI attestations, with that independent-registry limitation retained.
- Neither record contains optional molecular targets, causal graphs, activity-spectrum observations, producers or resistance mechanisms. These absences alone are not corrective findings. Hypotheses and host-cell effects in reviews do not establish a microbial direct-binding mechanism.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T140425Z-crystal-violet-cation-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Crystal violet cation: coherent exact cation identity with bounded active-moiety
  evidence'
started_at: '2026-10-21T13:49:08Z'
finished_at: '2026-10-21T14:04:25Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author the native seed. Verified the original captured
    hashes before judgment, read the entire native and actual source rows and transforms,
    independently parsed public chemical encodings, and inspected primary antibacterial
    and antifungal studies with explicit chemical-material and access limits.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: No corrective native-record finding was established. The single +1 crystal-violet
  cation is distinct from the adjacent chloride salt, and its ChEBI, PubChem and DrugCentral
  structure encodings agree. ChEBI explicitly supports iminium classification and
  antibacterial/antifungal roles. Primary studies of gentian-violet reagents support
  activity at active-moiety scope, without proving an independently isolated counterion-free
  experimental material. Scientific assessment retains the stated evidence limits;
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
  - path: data/antibiotics/antibacterial/crystal-violet-cation.yaml
    sha256: 6c15d517119dd4999b21014c16da56b3e6e09ee426371c3d4e18d74b9607bc11
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
- target_id: CHEBI:77181
  path: data/antibiotics/antibacterial/crystal-violet-cation.yaml
  label: crystal violet cation
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
  description: Entire native definition, all seven synonyms, iminium parent, two roles,
    complete structure/properties, CAS and Reaxys xrefs, DrugCentral drug-level link,
    source concept and all four history events. No citation lead is adopted in the
    exact source row; bounded original antibacterial and antifungal follow-up assessed.
  selection: Queue 331; original thirteen inputs preserved.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:77181
  exclusions:
  - target: Adjacent cation/chloride form and historical gentian-violet mixtures
    reason: The cation and chloride salt are distinct exact records. Some commercial
      gentian-violet preparations may contain other methylated dyes; their composition
      is not inferred from an exact single-structure graph or a generic trade name.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Actual focused schema validation found no issues.
  target_ids:
  - CHEBI:77181
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/crystal-violet-cation.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: One file scanned; zero strict errors.
  target_ids:
  - CHEBI:77181
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/crystal-violet-cation.yaml --out /private/tmp/am-review-session/331-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Native SMILES and InChI reproduce the stored full key, charge, element
    counts and rounded masses; no stereocentres occur and the source mint reproduces.
    Formula spelling/order is normalized for comparison while charge is checked separately.
  target_ids:
  - CHEBI:77181
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/331332-chemistry-check.py 331
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: external-chemistry
  name: external-chemistry
  status: passed
  required: false
  summary: Comparison script completed and explicitly reports form differences; this
    is not a blanket identity pass. ChEBI, PubChem and DrugCentral reproduce the cation;
    ChEBI, PubChem, KEGG and GSRS reproduce the chloride. All six RCSB CVI encodings
    reproduce only the cation.
  target_ids:
  - CHEBI:77181
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/331332-xref-check.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:77181
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
  - CHEBI:77181
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
  - CHEBI:77181
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
  - CHEBI:77181
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
  - CHEBI:77181
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
  - CHEBI:77181
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
  - CHEBI:77181
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
  - CHEBI:77181
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
  - CHEBI:77181
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/chebi_role_names.tsv; conf/sources.yaml;
    scripts/extract_source_inventory.py; scripts/seed_from_sources.py; data/raw/MANIFEST.yaml
  locator: Complete exact ChEBI row 1957 and adjacent-form row; relevant role/name
    extraction, synonym, xref partitioning, mint and priority code.
  accessed_at: '2026-10-21T13:59:21Z'
  support: supports
  summary: The native ChEBI identity, definition, aliases, parent, roles, structure
    and source version reproduce the maintained row. ChEBI confirmed names are extracted,
    brand and INN types are preserved, and ANTIBACTERIAL priority outranks ANTIFUNGAL
    without deleting either role. The cation source row contains no adopted citation
    leads.
  snapshot_sha256: 340fa59203fb4b99f87a62d28053c4a098857fb03ced1eb08515204205f3c98c
- evidence_id: roles
  kind: authority
  reference: CHEBI:33282; CHEBI:35718; CHEBI:35286
  locator: Current official ChEBI parent and role entries and exact entry relations.
  accessed_at: '2026-10-21T13:51:45Z'
  support: supports
  summary: The parent is iminium ion, structurally broader than the exact cation.
    Both antibacterial and antifungal role relations are explicit. The antibacterial
    definition includes a substance or its active part; role scope does not require
    that the isolated counterion-free cation was weighed as an experimental bulk material.
  snapshot_sha256: 20d92ce7e00c204b1753184671c043160821d692438278344335446aadcd5082
- evidence_id: antibacterial
  kind: primary_source
  reference: DOI:10.11150/kansenshogakuzasshi1970.66.914; https://www.jstage.jst.go.jp/article/kansenshogakuzasshi1970/66/7/66_7_914/_pdf
  locator: Entire original 1992 paper main text pp914–922 read from extracted Japanese
    text, English abstract and captions; tabular images and electron micrographs not
    independently reprocessed.
  accessed_at: '2026-10-21T13:53:45Z'
  support: supports
  summary: Saji explicitly identifies gentiana violet/pyoktanin blue as methylrosanilinium
    chloride and uses Wako reagent-grade material, without a lot-specific purity certificate.
    The study tests 66 MRSA and 42 MSSA clinical isolates plus S. aureus ATCC6538.
    Broth bactericidal endpoints are subculture/no-growth endpoints, separate from
    agar MIC for four MRSA isolates because dye interferes with turbidity. It also
    reports a small uncontrolled twelve-patient topical series. Electron-microscope
    changes after treatment are cellular observations, not direct target binding.
    This provides active-moiety context for the cation role; it is not an exact counterion-free
    material assay and no numerical result is transferred to this record.
  snapshot_sha256: ba38eb5de371b528bca1a0771084dcf9de410d29c2e3537030966d28984c9e42
- evidence_id: antifungal
  kind: primary_source
  reference: PMID:21444708; DOI:10.1128/AAC.01601-10; PMC3101405
  locator: Complete original main article HTML including Methods, Results, Table 1,
    Discussion and figure captions. Figure images and raw data not independently reprocessed.
  accessed_at: '2026-10-21T13:53:45Z'
  support: supports
  summary: Six oral Candida isolates from HIV-infected patients were tested with Sigma-Aldrich
    gentian violet of unspecified catalog/purity/counterion certification. CLSI M27-A3
    planktonic MICs, germination and 48-hour PMMA biofilm dry weight/architecture
    are distinct endpoints. At 4 micrograms/mL, Table 1 has significant biomass reductions
    for four of six isolates, not universal biofilm elimination. The authors did not
    measure biofilm viability with XTT and did not establish a molecular mechanism.
    Some prose calls thickness changes significant despite listed p values above 0.05;
    those significance claims are not adopted. The cation role is supported at active-moiety
    scope, not by a separately characterized unsalted test material.
  snapshot_sha256: 7ef3da96072463ccfd964823f8b8771964d083b5db9c8980a96c0032c0c34f4b
- evidence_id: mechanism-context
  kind: database
  reference: PMID:2272286; DOI:10.3109/03602539009041083; PMC4396813
  locator: Complete indexed abstract of the adopted 1990 review and selected mechanism
    discussion of the later review; discovery context only.
  accessed_at: '2026-10-21T13:53:45Z'
  support: context_only
  summary: Reviews discuss multiple proposed mechanisms across bacterial, fungal,
    host-cell and protozoan systems. The later review explicitly distinguishes brilliant-green
    thioredoxin-reductase work from gentian violet. These summaries do not establish
    an exact bacterial molecular target or justify transferring host NADPH-oxidase
    effects, photodynamic conditions or a sibling dye’s covalent target to either
    native record.
  snapshot_sha256: 3e08a069ff7e8294257025d001eff1ad22b023fb9adca2669f5214113e43f605
- evidence_id: adapter
  kind: database
  reference: Structured source applicability assessment
  locator: Native assertions and maintained rows inspected before mechanism follow-up.
  accessed_at: '2026-10-21T13:59:21Z'
  support: context_only
  summary: Neither record asserts a gene, protein, locus, regulator, pathway, stress
    response or transcriptomics dataset. The iModulonDB adapter is not applicable
    to these native chemical/role and regulatory assertions. Mechanism hypotheses
    encountered in reviews are not promoted into native claims.
- evidence_id: search
  kind: search
  reference: 331332-inclusive-hits.txt;331332-literature.json;331332-primary-followup.json
  locator: Ignored-inclusive exact-label, identifier, full-key and product search
    plus bounded public literature/authority follow-up.
  accessed_at: '2026-10-21T13:59:21Z'
  support: context_only
  summary: Both distinct native forms and their ChEBI source rows were found. The
    precise maintained-table scan found no adopted ARO, molecular-target, resistance,
    MIBiG or curator evidence row for these exact entities; no mechanism absence is
    inferred from a default ignored-aware search. Many broad crystal-violet hits use
    the dye as a biomass stain or degradation substrate and are not antimicrobial
    assays. No optional missing field is treated as a defect.
  search_scope: 2026-10-21; rg --no-ignore --hidden for crystal/gentian violet labels,
    CHEBI:77181, CHEBI:41688, exact InChIKeys, 085017 and J4Z741D6O5 across data,
    curation, conf, scripts, src, docs, .claude, reviews and reports; exact PMID follow-up
    and bounded public official compound/product sources. Ignored and hidden files
    were included.
  snapshot_sha256: bbe36bb9990ef805bc4fae94bae2a56a9aa10830e57d0a7cdecfa9a24926e529
- evidence_id: validation
  kind: validation
  reference: 331-schema.log;331-strict.log;331-chemistry.json;331332-xref-chemistry.json
  locator: Actual focused checks, external chemistry comparisons and captured-input
    hash recheck.
  accessed_at: '2026-10-21T13:59:21Z'
  support: supports
  summary: Schema, strict and native chemistry checks exit 0. The corrected external
    comparison script also exits 0 while reporting CVI as cation-only. Its first scratch
    attempt mistakenly tried to parse an InChIKey descriptor as SMILES; that helper
    error is retained in 331332-xref-chemistry-initial.log and was corrected before
    the final comparison. No native chemistry defect follows from that helper error.
    All captured input hashes remain unchanged.
  snapshot_sha256: d1e740950eda456651db3df7f064170017dfdc59f26d9c807773e76595f4f86d
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/crystal-violet-cation.yaml
  locator: Entire native YAML.
  accessed_at: '2026-10-21T13:59:21Z'
  support: supports
  summary: CHEBI:77181 is SEEDED/EXACT/ANTIBACTERIAL, with +1 C25H30N3 and full key
    LGLFFNDHMLKUMI-UHFFFAOYSA-N. Seven aliases explicitly denote the cation; the chloride
    counterion is absent by design. The definition’s minor inherited spelling typo
    does not alter chemical meaning. No clinical-status or product assertion is populated.
- evidence_id: identity
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:77181; pubchem.compound:3468;
    cas:7438-46-2
  locator: Complete current ChEBI entry and PubChem molecular properties, independently
    parsed.
  accessed_at: '2026-10-21T13:51:45Z'
  support: supports
  summary: Native SMILES/InChI, mass, element count and +1 charge agree with current
    ChEBI and PubChem CID3468. The iminium name and dimethylamino substitution description
    are coherent with the graph; the shared aromatic resonance representation does
    not make a new isomer. ChEBI explicitly distinguishes the chloride CHEBI:41688
    by a has-part relation. CAS 7438-46-2 is attested for the cation; no chloride
    salt identifier is imported as an exact native xref.
  snapshot_sha256: 492ff97e02d5c48733d49588bbd0d96b13b7a37c726a6d201384c3ab6f3ebca7
- evidence_id: drug
  kind: database
  reference: https://drugcentral.org/drugcard/4138; https://drugcentral.org/drug/4138/smiles
  locator: Full public DrugCentral page and actual SMILES endpoint.
  accessed_at: '2026-10-21T13:53:45Z'
  support: context_only
  summary: The DrugCentral structure independently yields the exact cation key. Its
    broader drug page also uses the gentian-violet name, chloride CAS and mixture
    prose; native drug_xrefs explicitly permits drug-level aggregation across forms.
    That wording is not an assertion that the native cation graph is a mixture. DrugCentral
    predictions and human receptor annotations are not native microbial target evidence.
  snapshot_sha256: 2e49e05ea3b1e7cf98b606676fb8239e29612597d14d694b0b9adfb475aaa13b
assessments:
- assessment_id: activity
  area: evidence
  topic: Antibacterial/antifungal filing and experimental scope
  outcome: supported
  summary: ChEBI explicitly assigns both roles, and original studies provide bounded
    Staphylococcus and Candida activity. Filing priority is reproduced. Preserve distinctions
    between the exact ionic form, test material, MIC, subculture bactericidal endpoint,
    biofilm biomass and clinical observations.
  target_ids:
  - CHEBI:77181
  evidence_ids:
  - roles
  - antibacterial
  - antifungal
  - owners
- assessment_id: mechanism
  area: evidence
  topic: Optional molecular mechanism and response fields
  outcome: unknown
  summary: No native molecular mechanism is asserted. Cellular morphology or reduced
    fungal biomass does not prove a specific protein target; the available review
    hypotheses require exact-compound primary follow-up before enrichment.
  target_ids:
  - CHEBI:77181
  evidence_ids:
  - mechanism-context
  - antibacterial
  - antifungal
  - adapter
- assessment_id: provenance
  area: provenance
  topic: Maintained source ownership, seed status and historical inputs
  outcome: supported
  summary: The complete source row and all native history events reconcile with the
    seed pathway. Initial hashes are retained and actual owners are captured. SEEDED
    does not imply scientific review, and this observation does not promote native
    status.
  target_ids:
  - CHEBI:77181
  evidence_ids:
  - native
  - owners
  - validation
  - search
- assessment_id: identity
  area: identity
  topic: Exact cation identity, synonyms and identifier scope
  outcome: supported
  summary: The native cation graph, seven cation aliases, masses and charge are coherent.
    DrugCentral is correctly typed as a drug-level link. The adjacent salt is a distinct
    record, not a duplicate to merge based on shared chromophore.
  target_ids:
  - CHEBI:77181
  evidence_ids:
  - native
  - identity
  - drug
  - roles
  - validation
findings: []
actions:
- action_id: A1
  description: Optionally enrich exact-material primary activity evidence while preserving
    the cation/salt distinction.
  finding_ids: []
  target_ids:
  - CHEBI:77181
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/crystal-violet-cation.yaml
    role: Curator-owned primary evidence additions
  acceptance_checks:
  - Identify the actual tested reagent, salt and composition before adding measurements.
    Do not copy chloride concentrations as independently tested counterion-free cation
    measurements.
  - Keep cellular effects and review hypotheses separate from directly demonstrated
    microbial molecular targets. Validate any authorized additions with native evidence
    and schema/strict gates.
limitations:
- The primary antibacterial paper identifies chloride reagent material but does not
  provide a lot-specific composition/purity certificate; the antifungal paper only
  identifies a Sigma-Aldrich gentian-violet reagent. No quantitative endpoint is silently
  assigned to separately isolated counterion-free cation or to every historical gentian-violet
  mixture.
- The 1992 Japanese main text and English abstract were read; tables embedded as images
  and electron micrographs were not independently reprocessed. Its English abstract
  rounds the lowest MIC differently from the Japanese results, and the time-kill caption
  and prose have differing inoculum/replicate descriptions. No numerical observation
  is curated from those ambiguities.
- Reaxys registry entries were not independently accessed through a paid service.
  Their exact numbers are verified as adopted/current ChEBI attestations, with that
  independent-registry limitation retained.
- Neither record contains optional molecular targets, causal graphs, activity-spectrum
  observations, producers or resistance mechanisms. These absences alone are not corrective
  findings. Hypotheses and host-cell effects in reviews do not establish a microbial
  direct-binding mechanism.
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
