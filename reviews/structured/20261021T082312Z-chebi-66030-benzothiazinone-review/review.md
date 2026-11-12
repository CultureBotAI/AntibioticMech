# Review of CHEBI:66030 (7-hydroxy-5-hydroxymethyl-2H-benzo[1,4]thiazin-3-one)

- Review: 20261021T082312Z-chebi-66030-benzothiazinone-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:16:23Z
- Finished UTC: 2026-10-21T08:23:12Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Native identity and structural encodings agree with current chemical authorities and the exact primary compound. One minor completeness finding identifies verified primary growth-inhibition evidence suitable for annotation. Preserve IC50 versus MIC, organism-specific results and fungal-culture source scope; no molecular target is established.

## Scope And Provenance

Entire exact generated record, ChEBI source ownership, every structural and ontology identifier, source origin and the sole adopted primary paper including original structure, methods and activity table.

Selection: Path-ordered unreviewed queue index 069; exactly one record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:66030 | data/antibiotics/antibacterial/7-hydroxy-5-hydroxymethyl-2h-benzo-1-4-thiazin-3-one.yaml | generated | 7-hydroxy-5-hydroxymethyl-2H-benzo[1,4]thiazin-3-one |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented per-record LinkML validation | passed | True | CHEBI:66030 | Exit 0; No issues found. |
| Documented closed-schema validation | passed | True | CHEBI:66030 | Exit 0; one file and zero ERROR rows. |
| Structure, PubChem and deterministic mint comparison | passed | False | CHEBI:66030 | Exit 0; both native encodings give the recorded key, formula, charge and masses; one fragment and no stereocentres. Current PubChem identity and mint agree. |
| Current exact term, parents, role and xref-string checks | passed | False | CHEBI:66030 | Exit 0; native term, four parents, antibacterial role, synonym, xref string, valid SMILES and InChI match current ChEBI/OLS. |
| Structured expression-context relevance | not_applicable | False | CHEBI:66030 | Current record names no gene, protein, regulator, pathway, stress response or transcriptomic dataset. Fungal source-genus wording alone does not supply an expression-module assertion. |
| Authoritative full QC | failed | True | CHEBI:66030 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:66030 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:66030 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:66030 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:66030 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:66030 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:66030 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:66030 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:66030 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral benzothiazinone

identity: supported. Targets: CHEBI:66030.

All native chemical representations and independent authority identity agree; original depicted compound matches. No structural or stereochemical defect is established.

### Names, parents and role

grounding: supported. Targets: CHEBI:66030.

One exact synonym and all four native parents fit the molecular graph; current term and primary evidence support antibacterial filing.

### External Reaxys locator

grounding: unknown. Targets: CHEBI:66030.

Native xref string reproduces from ChEBI; the external proprietary target was not independently resolved. No mismatch is established.

### Claim-specific primary support

evidence: supported. Targets: CHEBI:66030.

The sole imported PMID resolves to an inspected exact-compound paper. Its activity endpoint supports the broad role, with explicit limits on quantitative interpretation.

### Primary evidence annotation opportunity

completeness: concern. Targets: CHEBI:66030.

Specific verified measurements can support a bounded evidence/activity annotation. The finding concerns useful available evidence, not empty optional fields alone.

### Growth phenotype versus molecular mechanism

scope: unknown. Targets: CHEBI:66030.

No direct molecular target or causal antimicrobial mechanism is established by the inspected study. Retain uncertainty rather than infer a target from scaffold or class.

### Fungal culture source and structured producer scope

representation: supported. Targets: CHEBI:66030.

The native genus-level source wording is supported. Preserve the reported strain if curating source discussion; any stronger biosynthetic pathway or species-level producer claim requires independent support.

### Resistance, clinical, graphs and datasets

representation: not_applicable. Targets: CHEBI:66030.

No such objects are asserted and none is required just to fill optional fields. A growth assay does not establish clinical efficacy.

### Maintained input and history

ownership: supported. Targets: CHEBI:66030.

Generated fields and mint reproduce, with three internally consistent seed/reseed events. All 13 captured input hashes remain unchanged.

### Focused native gates

schema: supported. Targets: CHEBI:66030.

Both documented focused native validators pass; full-corpus checks are separately coordinated.

## Findings

### F1: Exact-compound primary growth-inhibition evidence is available for annotation

minor / open / confirmed; issue key: chebi-66030-primary-growth-activity-evidence-completeness.

The source-seeded record has no claim-level primary evidence despite a verified exact-compound assay. Add a bounded annotation with the correct endpoint and organism scope.

## Recommended Actions And Acceptance Checks

### A1

Curate claim-level primary activity and source context without extending their scope.

- Preserve the reported endpoint, units, strain, uncertainty and inequality. Do not convert an IC50 into MIC/MBC or replace a censored result with an exact value.
- Retain assay-specific incubation and preparation details; pre-culture duration is not the endpoint time. Keep compound numbering and pure-compound versus extract evidence distinct.
- Use evidence or discussions for source context; independently support biosynthesis before a stronger producer_organisms assertion. Do not invent a species, biosynthetic cluster, mechanism, clinical efficacy or safety claim.
- Use the validated writer/history and all required native gates before REVIEWED sign-off.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/7-hydroxy-5-hydroxymethyl-2h-benzo-1-4-thiazin-3-one.yaml; Entire generated record | supports | Read chemical/source definition, one exact synonym, four parents, antibacterial role, full structure, sole Reaxys xref, source concept and three seed/reseed events. No claim-level primary evidence, quantitative activity, mode, target, structured producer, resistance, clinical, graph or dataset annotation is asserted. |
| inventory | data/raw/chebi_antimicrobials.tsv; Exact CHEBI:66030 row; manifest; 069-owner-hits.txt | supports | Identity, definition, complete structure, parents, role, synonym and xref reproduce from the adopted row. Its sole PMID lead 18603789 resolves and the complete paper was read. Ignored-inclusive maintained-input search found no exact curator override. |
| ownership | scripts/extract_source_inventory.py; scripts/seed_from_sources.py; ChEBI import and generated field ownership | supports | Seeded fields belong to the maintained ChEBI inventory and transforms. New claim-level primary annotation belongs to curator-owned evidence/activity/discussion fields through validated writer and history. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:66030; 069-chebi.html current identity and structure | supports | Current ChEBI corroborates the exact label, substitution pattern, neutral formula and valid native SMILES. Source repetition is supplemented here by independent chemistry and primary structure inspection. |
| ontology | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_66030; 069-ols.json, 069-parents.json, 069-has_role.json | supports | Non-obsolete exact term has benzyl-alcohol, lactam, phenol and benzothiazine parents, with antibacterial role. Native synonym and sole reaxys:18590033 string reproduce. Reaxys target structure was not independently resolved. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/CZXYFHNORNVRJZ-UHFFFAOYSA-N/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON; 069-pubchem.json | supports | Independent CID 70678753 has the same standard InChI/key and C9H9NO3S. It corroborates neutral exact identity without adding an unverified native xref. |
| primary | PMID:18603789; DOI:10.1271/bbb.80043; 069-primary2008.pdf all four pages; original structure, methods and Table 1 visually inspected | supports | Compound 1 structure, NMR and HRMS match the intended lactam. It was isolated from cultured Ampelomyces sp. SC0307. MABA growth IC50 values (µg/mL; mean ± SD, n=3) are P. aeruginosa ATCC 9027 0.98±0.12, E. coli ATCC 8739 22.99±1.44, S. aureus ATCC 6538 84.42±1.64, and P. vulgaris CMCC 49027 &gt;128. Methods use MHB/Alamar Blue, 78 µL bacterial suspension prepared at 2×10^5 CFU/mL plus 2 µL dilution, 32 °C until controls turn pink. These are not MICs, bactericidal measurements or target assays. Other compounds and extract disc results remain separate. |
| primary-index | https://europepmc.org/article/MED/18603789; 069-core.json; sole adopted PMID lead | supports | Title, authors, 2008 publication date and DOI resolve to the inspected paper. The index abstract is consistent with exact-compound identification and condition-dependent antibacterial activity. |
| chemistry | RDKit and hashlib calculations; 069-chemistry.py and 069-chemistry.json | supports | SMILES and InChI parse to CZXYFHNORNVRJZ-UHFFFAOYSA-N, C9H9NO3S, charge 0, mass 211.242 and exact mass 211.030314148; no stereocentre is omitted. Source mint antibioticmech:chebi-1b90a10ed1 reproduces. PubChem InChI/key/formula agree. |
| source-check | Current source assertions; 069-source-check.py and 069-source-check.json | supports | Exit 0 verifies non-obsolete exact term and parents, native activity role, synonym and xref string, visible/OLS SMILES, and InChI. Valid source SMILES parses successfully. |
| validation | just validate; just validate-strict; Actual isolated batch 007 executions; 069-strict.tsv | supports | Both documented focused validators exited 0; strict scanned one record with zero ERROR rows. |
| search | Ignored-inclusive local and bounded public exact-name research; 069-local-hits.txt and 069-owner-hits.txt | context_only | Exact-name, CHEBI, InChIKey and adopted-PMID queries led to current chemical authorities and original primary paper. A direct antibacterial mechanism was not established within the inspected sources; this does not prove none exists. |

## Limits And Additional Notes

- The sole adopted PMID was resolved and its complete four-page primary paper read; original structure, assay methods and numerical table were viewed. The bounded follow-up did not establish a direct antimicrobial mechanism.
- Reaxys 18590033 was corroborated as a ChEBI xref string but its external target structure was not independently resolved. This is uncertainty, not a confirmed broken reference.
- The primary paper does not give a fixed assay endpoint time or detailed biosynthetic pathway. Native scientific status was not changed; actual shared gate outcomes are recorded separately.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Only scratch review artifacts were written. No native record, maintained input or curation history changed. All 13 input hashes were rechecked unchanged.
- The PDF text extraction renders the micro symbol incorrectly; original pixels confirm µg/mL and µL.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T082312Z-chebi-66030-benzothiazinone-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of CHEBI:66030 (7-hydroxy-5-hydroxymethyl-2H-benzo[1,4]thiazin-3-one)
started_at: '2026-10-21T08:16:23Z'
finished_at: '2026-10-21T08:23:12Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Identity, structure, source origin and broad antibacterial role supported;
  minor primary-evidence annotation opportunity remains and direct mechanism is unresolved
scientific_review: true
summary: Native identity and structural encodings agree with current chemical authorities
  and the exact primary compound. One minor completeness finding identifies verified
  primary growth-inhibition evidence suitable for annotation. Preserve IC50 versus
  MIC, organism-specific results and fungal-culture source scope; no molecular target
  is established.
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
  - path: data/antibiotics/antibacterial/7-hydroxy-5-hydroxymethyl-2h-benzo-1-4-thiazin-3-one.yaml
    sha256: a9059ad040133b9b4dfbe5c08ee0a13b04d6f3c548cb03cc74a71e49bc8b47cd
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
  description: Entire exact generated record, ChEBI source ownership, every structural
    and ontology identifier, source origin and the sole adopted primary paper including
    original structure, methods and activity table.
  selection: Path-ordered unreviewed queue index 069; exactly one record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:66030
targets:
- target_id: CHEBI:66030
  path: data/antibiotics/antibacterial/7-hydroxy-5-hydroxymethyl-2h-benzo-1-4-thiazin-3-one.yaml
  label: 7-hydroxy-5-hydroxymethyl-2H-benzo[1,4]thiazin-3-one
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
checks:
- check_id: schema
  name: Documented per-record LinkML validation
  status: passed
  required: true
  summary: Exit 0; No issues found.
  target_ids:
  - CHEBI:66030
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/7-hydroxy-5-hydroxymethyl-2h-benzo-1-4-thiazin-3-one.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented closed-schema validation
  status: passed
  required: true
  summary: Exit 0; one file and zero ERROR rows.
  target_ids:
  - CHEBI:66030
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/7-hydroxy-5-hydroxymethyl-2h-benzo-1-4-thiazin-3-one.yaml
    --out /private/tmp/am-review-session/069-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Structure, PubChem and deterministic mint comparison
  status: passed
  required: false
  summary: Exit 0; both native encodings give the recorded key, formula, charge and
    masses; one fragment and no stereocentres. Current PubChem identity and mint agree.
  target_ids:
  - CHEBI:66030
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/069-chemistry.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: source-check
  name: Current exact term, parents, role and xref-string checks
  status: passed
  required: false
  summary: Exit 0; native term, four parents, antibacterial role, synonym, xref string,
    valid SMILES and InChI match current ChEBI/OLS.
  target_ids:
  - CHEBI:66030
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/069-source-check.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - source-check
- check_id: imodulondb
  name: Structured expression-context relevance
  status: not_applicable
  required: false
  summary: Current record names no gene, protein, regulator, pathway, stress response
    or transcriptomic dataset. Fungal source-genus wording alone does not supply an
    expression-module assertion.
  target_ids:
  - CHEBI:66030
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:66030
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
  - CHEBI:66030
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
  - CHEBI:66030
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
  - CHEBI:66030
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
  - CHEBI:66030
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
  - CHEBI:66030
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
  - CHEBI:66030
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
  - CHEBI:66030
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
  - CHEBI:66030
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/7-hydroxy-5-hydroxymethyl-2h-benzo-1-4-thiazin-3-one.yaml
  locator: Entire generated record
  accessed_at: '2026-10-21T08:18:39Z'
  support: supports
  summary: Read chemical/source definition, one exact synonym, four parents, antibacterial
    role, full structure, sole Reaxys xref, source concept and three seed/reseed events.
    No claim-level primary evidence, quantitative activity, mode, target, structured
    producer, resistance, clinical, graph or dataset annotation is asserted.
- evidence_id: inventory
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Exact CHEBI:66030 row; manifest; 069-owner-hits.txt
  accessed_at: '2026-10-21T08:18:39Z'
  support: supports
  summary: Identity, definition, complete structure, parents, role, synonym and xref
    reproduce from the adopted row. Its sole PMID lead 18603789 resolves and the complete
    paper was read. Ignored-inclusive maintained-input search found no exact curator
    override.
- evidence_id: ownership
  kind: record_content
  reference: scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  locator: ChEBI import and generated field ownership
  accessed_at: '2026-10-21T08:18:39Z'
  support: supports
  summary: Seeded fields belong to the maintained ChEBI inventory and transforms.
    New claim-level primary annotation belongs to curator-owned evidence/activity/discussion
    fields through validated writer and history.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:66030
  locator: 069-chebi.html current identity and structure
  accessed_at: '2026-10-21T08:18:39Z'
  support: supports
  summary: Current ChEBI corroborates the exact label, substitution pattern, neutral
    formula and valid native SMILES. Source repetition is supplemented here by independent
    chemistry and primary structure inspection.
  snapshot_sha256: b67e7c15aeee7203aafa339ae0b880cb90ee21eeec87a40992f84c1b3c668d01
- evidence_id: ontology
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_66030
  locator: 069-ols.json, 069-parents.json, 069-has_role.json
  accessed_at: '2026-10-21T08:18:39Z'
  support: supports
  summary: Non-obsolete exact term has benzyl-alcohol, lactam, phenol and benzothiazine
    parents, with antibacterial role. Native synonym and sole reaxys:18590033 string
    reproduce. Reaxys target structure was not independently resolved.
  snapshot_sha256: 1692ea3bd5cb2ac1fad3ad833cf5fe098428643909ccdb9e294d581422e6544f
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/CZXYFHNORNVRJZ-UHFFFAOYSA-N/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON
  locator: 069-pubchem.json
  accessed_at: '2026-10-21T08:18:39Z'
  support: supports
  summary: Independent CID 70678753 has the same standard InChI/key and C9H9NO3S.
    It corroborates neutral exact identity without adding an unverified native xref.
  snapshot_sha256: ee22faddad1055d91bf87b57d2ce6ab45b9fde44daab9a170369f8ab47a6402b
- evidence_id: primary
  kind: primary_source
  reference: PMID:18603789
  locator: DOI:10.1271/bbb.80043; 069-primary2008.pdf all four pages; original structure,
    methods and Table 1 visually inspected
  accessed_at: '2026-10-21T08:18:39Z'
  support: supports
  summary: Compound 1 structure, NMR and HRMS match the intended lactam. It was isolated
    from cultured Ampelomyces sp. SC0307. MABA growth IC50 values (µg/mL; mean ± SD,
    n=3) are P. aeruginosa ATCC 9027 0.98±0.12, E. coli ATCC 8739 22.99±1.44, S. aureus
    ATCC 6538 84.42±1.64, and P. vulgaris CMCC 49027 >128. Methods use MHB/Alamar
    Blue, 78 µL bacterial suspension prepared at 2×10^5 CFU/mL plus 2 µL dilution,
    32 °C until controls turn pink. These are not MICs, bactericidal measurements
    or target assays. Other compounds and extract disc results remain separate.
  snapshot_sha256: f7062a1e8ef4eadc9d39730f002b1be3c81a7a71ad7474d44393fd5ae34b3027
- evidence_id: primary-index
  kind: database
  reference: https://europepmc.org/article/MED/18603789
  locator: 069-core.json; sole adopted PMID lead
  accessed_at: '2026-10-21T08:18:39Z'
  support: supports
  summary: Title, authors, 2008 publication date and DOI resolve to the inspected
    paper. The index abstract is consistent with exact-compound identification and
    condition-dependent antibacterial activity.
  snapshot_sha256: 22a9714746e1f92d48bc603b269c8aeddb877a45773430506ec5328fe1706da1
- evidence_id: chemistry
  kind: validation
  reference: RDKit and hashlib calculations
  locator: 069-chemistry.py and 069-chemistry.json
  accessed_at: '2026-10-21T08:18:39Z'
  support: supports
  summary: SMILES and InChI parse to CZXYFHNORNVRJZ-UHFFFAOYSA-N, C9H9NO3S, charge
    0, mass 211.242 and exact mass 211.030314148; no stereocentre is omitted. Source
    mint antibioticmech:chebi-1b90a10ed1 reproduces. PubChem InChI/key/formula agree.
  snapshot_sha256: bd5807043049ae6dfa44eadbb96fa9efc3f51a48cb9fd9f0e3173ef8b7b2a719
- evidence_id: source-check
  kind: validation
  reference: Current source assertions
  locator: 069-source-check.py and 069-source-check.json
  accessed_at: '2026-10-21T08:18:39Z'
  support: supports
  summary: Exit 0 verifies non-obsolete exact term and parents, native activity role,
    synonym and xref string, visible/OLS SMILES, and InChI. Valid source SMILES parses
    successfully.
  snapshot_sha256: 1e094b66d06cca6cb43a0e2348dcc33d08efe0c3b8148ed421176b797cf92e95
- evidence_id: validation
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual isolated batch 007 executions; 069-strict.tsv
  accessed_at: '2026-10-21T08:18:39Z'
  support: supports
  summary: Both documented focused validators exited 0; strict scanned one record
    with zero ERROR rows.
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local and bounded public exact-name research
  locator: 069-local-hits.txt and 069-owner-hits.txt
  accessed_at: '2026-10-21T08:18:39Z'
  support: context_only
  summary: Exact-name, CHEBI, InChIKey and adopted-PMID queries led to current chemical
    authorities and original primary paper. A direct antibacterial mechanism was not
    established within the inspected sources; this does not prove none exists.
  search_scope: prepare.py 69 ran rg --no-ignore --hidden excluding only .git and
    .venv before judgment. Follow-up searched maintained data/raw,curation,conf for
    exact CHEBI,mint,key; public queries covered exact name,Ampelomyces,mechanism
    and Reaxys identifier. Unrelated similarly named compounds were excluded.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral benzothiazinone
  outcome: supported
  summary: All native chemical representations and independent authority identity
    agree; original depicted compound matches. No structural or stereochemical defect
    is established.
  target_ids:
  - CHEBI:66030
  evidence_ids:
  - record
  - chebi
  - pubchem
  - chemistry
  - primary
- assessment_id: grounding
  area: grounding
  topic: Names, parents and role
  outcome: supported
  summary: One exact synonym and all four native parents fit the molecular graph;
    current term and primary evidence support antibacterial filing.
  target_ids:
  - CHEBI:66030
  evidence_ids:
  - ontology
  - primary
  - source-check
- assessment_id: xref
  area: grounding
  topic: External Reaxys locator
  outcome: unknown
  summary: Native xref string reproduces from ChEBI; the external proprietary target
    was not independently resolved. No mismatch is established.
  target_ids:
  - CHEBI:66030
  evidence_ids:
  - ontology
- assessment_id: evidence
  area: evidence
  topic: Claim-specific primary support
  outcome: supported
  summary: The sole imported PMID resolves to an inspected exact-compound paper. Its
    activity endpoint supports the broad role, with explicit limits on quantitative
    interpretation.
  target_ids:
  - CHEBI:66030
  evidence_ids:
  - primary
  - primary-index
- assessment_id: completeness
  area: completeness
  topic: Primary evidence annotation opportunity
  outcome: concern
  summary: Specific verified measurements can support a bounded evidence/activity
    annotation. The finding concerns useful available evidence, not empty optional
    fields alone.
  target_ids:
  - CHEBI:66030
  evidence_ids:
  - record
  - primary
- assessment_id: mechanism
  area: scope
  topic: Growth phenotype versus molecular mechanism
  outcome: unknown
  summary: No direct molecular target or causal antimicrobial mechanism is established
    by the inspected study. Retain uncertainty rather than infer a target from scaffold
    or class.
  target_ids:
  - CHEBI:66030
  evidence_ids:
  - primary
  - search
- assessment_id: source-origin
  area: representation
  topic: Fungal culture source and structured producer scope
  outcome: supported
  summary: The native genus-level source wording is supported. Preserve the reported
    strain if curating source discussion; any stronger biosynthetic pathway or species-level
    producer claim requires independent support.
  target_ids:
  - CHEBI:66030
  evidence_ids:
  - record
  - primary
- assessment_id: optional
  area: representation
  topic: Resistance, clinical, graphs and datasets
  outcome: not_applicable
  summary: No such objects are asserted and none is required just to fill optional
    fields. A growth assay does not establish clinical efficacy.
  target_ids:
  - CHEBI:66030
  evidence_ids:
  - record
  - primary
- assessment_id: provenance
  area: ownership
  topic: Maintained input and history
  outcome: supported
  summary: Generated fields and mint reproduce, with three internally consistent seed/reseed
    events. All 13 captured input hashes remain unchanged.
  target_ids:
  - CHEBI:66030
  evidence_ids:
  - inventory
  - ownership
  - chemistry
- assessment_id: schema
  area: schema
  topic: Focused native gates
  outcome: supported
  summary: Both documented focused native validators pass; full-corpus checks are
    separately coordinated.
  target_ids:
  - CHEBI:66030
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: chebi-66030-primary-growth-activity-evidence-completeness
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Exact-compound primary growth-inhibition evidence is available for annotation
  description: The source-seeded record has no claim-level primary evidence despite
    a verified exact-compound assay. Add a bounded annotation with the correct endpoint
    and organism scope.
  target_ids:
  - CHEBI:66030
  field_paths:
  - evidence
  - activity_spectrum
  - discussions
  evidence_ids:
  - record
  - primary
  - primary-index
  rule_id: 'review-checklist: Evidence standard and Activity'
  native_severity: minor actionable primary-evidence completeness gap
  normalization_reason: A concrete primary annotation is available; identity and existing
    broad claims are supported, and optional emptiness alone is not an error.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/7-hydroxy-5-hydroxymethyl-2h-benzo-1-4-thiazin-3-one.yaml
    role: Curator-owned evidence, activity_spectrum and discussions through validated
      writer/history
actions:
- action_id: A1
  description: Curate claim-level primary activity and source context without extending
    their scope.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:66030
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/7-hydroxy-5-hydroxymethyl-2h-benzo-1-4-thiazin-3-one.yaml
    role: Curator-owned evidence, activity_spectrum and discussions through validated
      writer/history
  acceptance_checks:
  - Preserve the reported endpoint, units, strain, uncertainty and inequality. Do
    not convert an IC50 into MIC/MBC or replace a censored result with an exact value.
  - Retain assay-specific incubation and preparation details; pre-culture duration
    is not the endpoint time. Keep compound numbering and pure-compound versus extract
    evidence distinct.
  - Use evidence or discussions for source context; independently support biosynthesis
    before a stronger producer_organisms assertion. Do not invent a species, biosynthetic
    cluster, mechanism, clinical efficacy or safety claim.
  - Use the validated writer/history and all required native gates before REVIEWED
    sign-off.
limitations:
- The sole adopted PMID was resolved and its complete four-page primary paper read;
  original structure, assay methods and numerical table were viewed. The bounded follow-up
  did not establish a direct antimicrobial mechanism.
- Reaxys 18590033 was corroborated as a ChEBI xref string but its external target
  structure was not independently resolved. This is uncertainty, not a confirmed broken
  reference.
- The primary paper does not give a fixed assay endpoint time or detailed biosynthetic
  pathway. Native scientific status was not changed; actual shared gate outcomes are
  recorded separately.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Only scratch review artifacts were written. No native record, maintained input or
  curation history changed. All 13 input hashes were rechecked unchanged.
- The PDF text extraction renders the micro symbol incorrectly; original pixels confirm
  µg/mL and µL.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:66030
- https://pubchem.ncbi.nlm.nih.gov/compound/70678753
- https://doi.org/10.1271/bbb.80043
- https://www.jstage.jst.go.jp/article/bbb/72/7/72_80043/_pdf
tags:
- record-review
- benzothiazinone
- primary-activity
- ic50-not-mic
- fungal-culture-source
```
