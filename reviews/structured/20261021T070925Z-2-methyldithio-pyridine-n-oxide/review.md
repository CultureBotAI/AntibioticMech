# 2-(Methyldithio)pyridine-N-oxide: identity and qualified primary experimental evidence

- Review: 20261021T070925Z-2-methyldithio-pyridine-n-oxide
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T07:00:40Z
- Finished UTC: 2026-10-21T07:09:25Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact identity and source provenance are coherent. Two minor curation opportunities concern qualified mechanism and dataset context and scoped activity; an informational follow-up distinguishes plant isolation from biosynthesis. Candidate enzymes, expression markers and newer analogue experiments do not establish direct targets for this molecule.

## Scope And Provenance

Complete one-record review with bounded primary-source and official-identity research.

Selection: Queue index019, exactly CHEBI:66373.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:66373 | data/antibiotics/antibacterial/2-methyldithio-pyridine-n-oxide.yaml | generated | 2-(methyldithio)pyridine-N-oxide |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Single-record LinkML schema | passed | True | CHEBI:66373 | Focused gate passed with no errors. |
| Single-record strict validation | passed | True | CHEBI:66373 | Focused gate passed with no errors. |
| Official identity and structure verification | passed | True | CHEBI:66373 | Live ChEBI and local chemistry agree on exact structure, net charge, parents and role. |
| Independent Reaxys registry access | unavailable | False | CHEBI:66373 | Registry assertion verified in official ChEBI; independent Reaxys content not inspected. |
| Expression-module follow-up adapter | passed | False | CHEBI:66373 | After the original DNS failure, fresh public adapter search succeeded and resolved trxB2 to Rv3913 in m_tuberculosis/modulome. No matching iModulons were returned for that query; no module membership or mechanism conclusion is inferred. |
| Authoritative full QC | failed | True | CHEBI:66373 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:66373 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:66373 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:66373 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:66373 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:66373 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:66373 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:66373 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:66373 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact N-oxide and disulfide identity

identity: supported. Targets: CHEBI:66373.

Official identity, source row and calculated structure agree. Protonated mass-spectrometry ions do not change the neutral record formula. Analogues remain distinct.

### Antibacterial filing and imported parents

grounding: supported. Targets: CHEBI:66373.

The source role and primary experiment support antibacterial filing. Parent classes are broader and are not treated as exact equivalents.

### Qualified mechanism and experimental context

completeness: concern. Targets: CHEBI:66373.

Specific pathway/response evidence warrants a curator assessment with explicit uncertainty. A mechanistic enum, direct target or causal edge must not be inferred from named candidate enzymes or response markers alone.

### Public expression dataset follow-up

completeness: concern. Targets: CHEBI:66373.

The publication Methods describe compound1 treatment, whereas the linked public project carries legacy garlic-extract wording. Reconcile sample-level provenance before a dataset annotation. A fresh structured-adapter query resolves the trxB2 gene but supplies no matching module evidence and does not establish target binding.

### Strain- and assay-specific activity

completeness: concern. Targets: CHEBI:66373.

The primary source supplies multiple separable experiments. Detailed extraction needs original units, cited assay methods and chemical-column identity; no species-wide susceptibility conclusion is warranted.

### Plant isolation source and unresolved biosynthesis

completeness: unknown. Targets: CHEBI:66373.

Primary extraction and structural characterization support isolation from Allium stipitatum bulbs. They do not establish biosynthesis in that taxon, as required for producer_organisms. The existing source-owned isolation statement is supported; a producer entry remains conditional on additional evidence.

### Direct molecular targets

evidence: unknown. Targets: CHEBI:66373.

No native molecular target is asserted. The inspected study leaves the direct mechanism unresolved, and later analogue experiments cannot settle it for this molecule.

### Resistance, clinical and causal-graph scope

evidence: not_applicable. Targets: CHEBI:66373.

No native resistance, clinical-use or causal-graph assertion needs correction. Optional absence alone is not a defect. Experimental growth inhibition is not treatment efficacy.

### Ownership and native status

provenance: supported. Targets: CHEBI:66373.

Adopted fields and history match. The record appropriately remains SEEDED; future enrichment requires explicit curator provenance.

### Focused schema gates

schema: supported. Targets: CHEBI:66373.

Both required focused gates pass.

## Findings

### F1: Primary response experiments and a matching dataset need a qualified mechanism assessment

minor / open / confirmed; issue key: chebi-66373-qualified-mechanism-dataset-curation.

The adopted paper provides a concrete mechanism-curation path with explicit alternatives. The matching public project can support experimental context after sample metadata reconciliation. The current empty fields assert no false target, and this finding does not require inventing one.

### F2: Primary activity experiments are available for scoped extraction

minor / open / confirmed; issue key: chebi-66373-primary-activity-enrichment.

The inspected paper offers exact-compound activity observations. Preserve compound-column identity and individual organisms, and verify source-internal unit or inoculum ambiguities before detailed extraction. Absence of optional activity fields is not a schema violation.

### F3: Plant isolation supports a source statement; a biosynthetic producer remains unresolved

informational / open / confirmed; issue key: chebi-66373-structured-producer-evidence.

The primary paper isolates compound1 from Allium stipitatum bulbs. This supports the current source definition but does not by itself satisfy the schema requirement that producer_organisms biosynthesize the compound. Investigate biosynthetic support only if a structured producer annotation is pursued; no current producer claim is incorrect.

## Recommended Actions And Acceptance Checks

### A1

Curate a qualified mechanism narrative or explicit unresolved disposition using experimental observations and alternatives. Assess the public expression-dataset link with sample-level provenance before adding it. Keep candidate targets and response markers distinct from directly demonstrated targets.

- Each claim has exact-compound, taxon, assay and primary-source context; no direct binding or enzyme inhibition is invented.
- Dataset accession and original treatment-label caveat remain traceable.
- Native writer/history and focused strict, reproducibility and QC gates are used.

### A2

Extract only compound1 activity observations after consulting original assay references and resolving any presentation ambiguities; keep endpoints and experimental systems separate.

- MIC method, units, endpoint, organism and isolate are present and source-traceable.
- Resistance to comparator drugs is not assigned as resistance to this compound; animal outcomes are not generalized to clinical status.
- Use native validated writer/history and required gates.

### A3

Preserve the supported source-owned isolation statement. Before adding Allium stipitatum to producer_organisms, find exact-compound evidence that supports biosynthesis in that taxon; otherwise retain the unresolved disposition and do not infer production solely from bulb extraction.

- Any producer annotation has evidence for biosynthesis, exact taxon grounding and claim-specific provenance; bulb isolation alone is not sufficient.
- If no biosynthetic support is established, leave the optional producer list empty and preserve the supported isolation statement.
- Use native writer/history and focused strict, reproducibility and QC gates for any separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/2-methyldithio-pyridine-n-oxide.yaml; Complete YAML, structure, single xref, source concept and three seeder events | supports | The exact ChEBI-only seed asserts antibacterial classification and a source definition describing isolation from Allium stipitatum. It has no curator mechanism, target, activity_spectrum, resistance, producer_organisms, clinical, dataset or causal_graphs objects and no activity collections. |
| owner | data/raw/chebi_antimicrobials.tsv; CHEBI:66373 row1517; MANIFEST; extractor/seeder; PATHS.tsv row1771 | supports | All adopted identity, chemical and provenance fields match the generated record. PMID19093848 is the single discovery lead. Source version2026-08-30, minted identifier and history agree. Seed-owned changes belong upstream; new scientific annotations belong on the actual record. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:66373; Live official page reached through AmiGO originating-resource link; structure, ontology, names, registry and species sections | supports | Official ChEBI agrees on C6H7NOS2, net charge0, mass173.262, exact mass172.99691, structure strings and key XKLCDAACRKRTLY-UHFFFAOYSA-N. The three chemical parents, exact synonym, antibacterial role and Reaxys19619270 agree. Species annotation identifies A.stipitatum bulbs with PMID19093848. The internally charged N-oxide representation has net zero charge and is not a salt. |
| structure | RDKit structure recomputation; SMILES parsed locally; formula, net formal charge, InChI/key, average and exact masses recomputed | supports | Calculated C6H7NOS2, charge0, identical InChI/key, average173.262 and exact172.996905844 match the record. This is an internal consistency check, separate from official identity evidence. |
| config | conf/sources.yaml; role_to_class, role_to_mode_of_action and adopted role_names | supports | CHEBI:33282 maps to ANTIBACTERIAL. No specific mechanism role is adopted; the blank seeded mode is reproducible. The three broader chemical parents are not external identity xrefs. |
| local-search | CultureBotAI/AntibioticMech; Ignored-inclusive exact and alias searches | context_only | Broad hits are raw, generated, queue and research-ledger references. Focused curation/reviews/historical-report searches found no target-specific curated override or prose report in those scopes. Complete target inspection establishes which scientific objects are absent; no global evidence-absence claim is made. |
| rubric | docs/CURATION.md; Native review checklist: mechanism, targets, activity, producer, datasets and REVIEWED criteria | supports | Optional empty slots are not schema defects. A concrete source can warrant enrichment, with claim-specific evidence and exact-compound scope. Expression response is not target binding, and activity in an antibiotic-resistant isolate is not a resistance mechanism against this compound. Native changes need validated writer/history and a separate readiness decision. |
| primary | PMID:19093848; https://pmc.ncbi.nlm.nih.gov/articles/PMC2765505/ — DOI10.1021/np800572r; Results and Discussion, Table2, Figure1, Experimental Section | supports | Exact compound1 was isolated from A.stipitatum bulbs and confirmed by synthesis. In M.smegmatis,30 µg/mL blocked acetate incorporation into soluble lipids; FAS-I,AccD1,FabH and generalized toxicity remain alternatives. Expression changes indicate stress, not binding. Figure1 gives BCG MIC0.1 µg/mL by spot-culture growth inhibition; Table2 separates compound1 from analogues and individual isolates. The30mg/kg mouse regimen lacked efficacy. The fast-growing-bacteria assay delegates details to earlier references; HTML table/prose units and inoculum descriptions need checking before precise extraction. |
| bioproject | https://www.ncbi.nlm.nih.gov/bioproject/PRJNA118583; Public BioProject summary, accession, GEO relationship and publication | supports | Official project connects GSE17640 to PMID19093848 and describes compound1 exposure of M.tuberculosis at2,5,10 µg/mL for6h, matching the publication Methods. It describes oxidative/heat-shock transcriptional responses. A legacy treatment label calls the material garlic extract. This is a metadata discrepancy requiring sample-level reconciliation, not proof that the published experiment used a mixed extract. |
| geo-lead | https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE17640; Indexed GEO series metadata; direct GEO/sample access returned challenge pages | context_only | Indexed source lists four arrays, GPL9036, and sample titles using garlic-extract wording. Individual sample metadata and raw files were not inspected. This is a dataset follow-up lead; the inspected BioProject supports the public accession relationship. |
| analogues | DOI:10.1038/s41598-017-18948-w; https://www.nature.com/articles/s41598-017-18948-w —2018 Results, Figures1–3, Methods | supports | The new efflux and biofilm experiments test synthetic compounds13–16. The natural target appears in historical comparison context. Those experiments therefore cannot establish efflux-pump inhibition or biofilm mechanism for CHEBI:66373. |
| other-chemical | https://pmc.ncbi.nlm.nih.gov/articles/PMC6471189/; 2019 paper discovery result: compound identity and study title | context_only | The broad-spectrum2019 study tests 2-(methyldithio)pyridine-3-carbonitrile, a chemically different compound. Its MIC, killing and antifungal results are not adopted for the N-oxide. |
| adapter | kg-microbe-sources imodulondb datasets; Runner at /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw; public iModulonDB fallback | supports | The installed console command was absent, but a local claw project runner resolved. Its datasets call exited2 on DNS failure for https://imodulondb.org/api/datasets. The fallback public site exposed no readable content. No module absence or target claim is inferred. The native seed itself has no expression object. |
| validation | just validate; just validate-strict; Isolated worktree002; /private/tmp/am-review-session/019-validation.tsv | supports | Both focused commands exited0. LinkML reported no issues; strict scanned1 target and0 ERROR rows. |
| producer-boundary | DOI:10.1021/np800572r; Primary article reproduced at https://www.lookchem.com/FreePDFArticle_14173-25-2_8791422.htm — Plant Material; Extraction and Isolation; Results and Discussion. Native producer rule: .claude/skills/curate-yaml-record/references/review-checklist.md:40 and src/antibioticmech/schema/antibioticmech.yaml:263,562. | context_only | Methods document purchased bulbs, solvent extraction, HPLC isolation and chemical characterization. The inspected experiment establishes a natural isolation source, not biosynthesis in the plant. Native producer semantics require the latter. Microarray Methods explicitly name compound1; FAS-I, AccD1 and mtFabH remain proposed explanations, with nonspecific toxicity unresolved. |
| adapter-followup | kg-microbe-sources imodulondb search; m_tuberculosis/modulome; exact query trxB2; /private/tmp/am-review-session/019-adversarial-imodulondb-trxB2.txt | context_only | After discovery of m_tuberculosis/modulome in the successful public dataset inventory, the fresh query exited0: one gene, m_tuberculosis/modulome/Rv3913 (trxB2, thioredoxin reductase), and zero matching iModulons. This resolves a gene-context identifier only. It does not measure this compound response, assign module membership, or demonstrate a molecular target. |

## Limits And Additional Notes

- The primary full-text Results, tables and Methods were inspected; cited older assay protocols and publisher PDF were not. Presentation ambiguities require resolution before fine-grained activity extraction.
- GEO sample/raw data access was blocked; the public BioProject linkage and publication Methods were inspected. The original iModulonDB discovery attempt failed on DNS; a later focused query succeeded but provided gene context only, without module evidence.
- Independent Reaxys content was not inspected; official ChEBI registry assertion was verified.
- Bounded research does not establish global evidence absence. No paid research or native record edits occurred.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Provenance capture preceded judgment; expanded inputs preserved every original hash and base revision.
- Ignored and hidden files were included in all searches used for local absence.
- The native record remains SEEDED; optional empty fields are not blanket schema defects.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T070925Z-2-methyldithio-pyridine-n-oxide
kind: record
repository: CultureBotAI/AntibioticMech
title: '2-(Methyldithio)pyridine-N-oxide: identity and qualified primary experimental
  evidence'
started_at: '2026-10-21T07:00:40Z'
finished_at: '2026-10-21T07:09:25Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Reviewer did not create or curate the seed and independently
    inspected primary text and official sources; agent review is not human scientific
    sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Exact identity and source provenance are coherent. Two minor curation opportunities
  concern qualified mechanism and dataset context and scoped activity; an informational
  follow-up distinguishes plant isolation from biosynthesis. Candidate enzymes, expression
  markers and newer analogue experiments do not establish direct targets for this
  molecule.
source:
  git_revision: baf3b3203d748d098686e166cdb2a6138f47eb59
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 5e2e1f975f8aa64f92a06c134c98c750c968fd78f02620a73c9cb611ac018ed8
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: CLAUDE.md
    sha256: 36fb92f8919481cfbf3f17ddde4a1e244c81f76c64396dbbac910c4815fb9f16
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
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
  - path: data/antibiotics/PATHS.tsv
    sha256: 3b1d82d007878e4aca2c28f4001a468776b325b726da2e48abb76a3dc551cc38
    role: context
  - path: data/antibiotics/antibacterial/2-methyldithio-pyridine-n-oxide.yaml
    sha256: d5f535c2ab4f972603b15bfcf9d837ef8813744b5ea11f94d12721072df7eb33
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
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
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
- target_id: CHEBI:66373
  path: data/antibiotics/antibacterial/2-methyldithio-pyridine-n-oxide.yaml
  label: 2-(methyldithio)pyridine-N-oxide
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
  description: Complete one-record review with bounded primary-source and official-identity
    research.
  selection: Queue index019, exactly CHEBI:66373.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:66373
  exclusions:
  - target: Related disulfides, pyrithione and carbonitrile analogues as independent
      records
    reason: Comparison context only; no transferred activity or mechanism and no additional
      target verdict.
checks:
- check_id: schema
  name: Single-record LinkML schema
  status: passed
  required: true
  summary: Focused gate passed with no errors.
  target_ids:
  - CHEBI:66373
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/2-methyldithio-pyridine-n-oxide.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Single-record strict validation
  status: passed
  required: true
  summary: Focused gate passed with no errors.
  target_ids:
  - CHEBI:66373
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/2-methyldithio-pyridine-n-oxide.yaml --out /private/tmp/am-review-session/019-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: identity
  name: Official identity and structure verification
  status: passed
  required: true
  summary: Live ChEBI and local chemistry agree on exact structure, net charge, parents
    and role.
  target_ids:
  - CHEBI:66373
  evidence_ids:
  - chebi
  - structure
  - config
- check_id: reaxys
  name: Independent Reaxys registry access
  status: unavailable
  required: false
  summary: Registry assertion verified in official ChEBI; independent Reaxys content
    not inspected.
  target_ids:
  - CHEBI:66373
  evidence_ids:
  - chebi
- check_id: imodulondb
  name: Expression-module follow-up adapter
  status: passed
  required: false
  summary: After the original DNS failure, fresh public adapter search succeeded and
    resolved trxB2 to Rv3913 in m_tuberculosis/modulome. No matching iModulons were
    returned for that query; no module membership or mechanism conclusion is inferred.
  target_ids:
  - CHEBI:66373
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 search --organism m_tuberculosis --dataset
    modulome --query trxB2
  evidence_ids:
  - adapter
  - adapter-followup
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
  - CHEBI:66373
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
  - CHEBI:66373
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
  - CHEBI:66373
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
  - CHEBI:66373
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
  - CHEBI:66373
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
  - CHEBI:66373
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
  - CHEBI:66373
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
  - CHEBI:66373
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
  - CHEBI:66373
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/2-methyldithio-pyridine-n-oxide.yaml
  locator: Complete YAML, structure, single xref, source concept and three seeder
    events
  accessed_at: '2026-10-21T07:03:19Z'
  support: supports
  summary: The exact ChEBI-only seed asserts antibacterial classification and a source
    definition describing isolation from Allium stipitatum. It has no curator mechanism,
    target, activity_spectrum, resistance, producer_organisms, clinical, dataset or
    causal_graphs objects and no activity collections.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: CHEBI:66373 row1517; MANIFEST; extractor/seeder; PATHS.tsv row1771
  accessed_at: '2026-10-21T07:03:19Z'
  support: supports
  summary: All adopted identity, chemical and provenance fields match the generated
    record. PMID19093848 is the single discovery lead. Source version2026-08-30, minted
    identifier and history agree. Seed-owned changes belong upstream; new scientific
    annotations belong on the actual record.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:66373
  locator: Live official page reached through AmiGO originating-resource link; structure,
    ontology, names, registry and species sections
  accessed_at: '2026-10-21T07:03:19Z'
  support: supports
  summary: Official ChEBI agrees on C6H7NOS2, net charge0, mass173.262, exact mass172.99691,
    structure strings and key XKLCDAACRKRTLY-UHFFFAOYSA-N. The three chemical parents,
    exact synonym, antibacterial role and Reaxys19619270 agree. Species annotation
    identifies A.stipitatum bulbs with PMID19093848. The internally charged N-oxide
    representation has net zero charge and is not a salt.
- evidence_id: structure
  kind: validation
  reference: RDKit structure recomputation
  locator: SMILES parsed locally; formula, net formal charge, InChI/key, average and
    exact masses recomputed
  accessed_at: '2026-10-21T07:03:19Z'
  support: supports
  summary: Calculated C6H7NOS2, charge0, identical InChI/key, average173.262 and exact172.996905844
    match the record. This is an internal consistency check, separate from official
    identity evidence.
- evidence_id: config
  kind: record_content
  reference: conf/sources.yaml
  locator: role_to_class, role_to_mode_of_action and adopted role_names
  accessed_at: '2026-10-21T07:03:19Z'
  support: supports
  summary: CHEBI:33282 maps to ANTIBACTERIAL. No specific mechanism role is adopted;
    the blank seeded mode is reproducible. The three broader chemical parents are
    not external identity xrefs.
- evidence_id: local-search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: Ignored-inclusive exact and alias searches
  accessed_at: '2026-10-21T07:03:19Z'
  support: context_only
  summary: Broad hits are raw, generated, queue and research-ledger references. Focused
    curation/reviews/historical-report searches found no target-specific curated override
    or prose report in those scopes. Complete target inspection establishes which
    scientific objects are absent; no global evidence-absence claim is made.
  search_scope: prepare.py19 used rg --no-ignore --hidden over the worktree excluding
    .git/.venv. Exact CHEBI:66373,key and minted-ID searches in raw/curation/reviews/PATHS;
    expanded -i methyldithio,methyldisulfanyl-pyridine,66373 in curation reviews reports/yaml_record_review
    excluding record_review_queue.tsv. Hidden and ignored files included.
- evidence_id: rubric
  kind: record_content
  reference: docs/CURATION.md
  locator: 'Native review checklist: mechanism, targets, activity, producer, datasets
    and REVIEWED criteria'
  accessed_at: '2026-10-21T07:03:19Z'
  support: supports
  summary: Optional empty slots are not schema defects. A concrete source can warrant
    enrichment, with claim-specific evidence and exact-compound scope. Expression
    response is not target binding, and activity in an antibiotic-resistant isolate
    is not a resistance mechanism against this compound. Native changes need validated
    writer/history and a separate readiness decision.
- evidence_id: primary
  kind: primary_source
  reference: PMID:19093848
  locator: https://pmc.ncbi.nlm.nih.gov/articles/PMC2765505/ — DOI10.1021/np800572r;
    Results and Discussion, Table2, Figure1, Experimental Section
  accessed_at: '2026-10-21T07:03:19Z'
  support: supports
  summary: Exact compound1 was isolated from A.stipitatum bulbs and confirmed by synthesis.
    In M.smegmatis,30 µg/mL blocked acetate incorporation into soluble lipids; FAS-I,AccD1,FabH
    and generalized toxicity remain alternatives. Expression changes indicate stress,
    not binding. Figure1 gives BCG MIC0.1 µg/mL by spot-culture growth inhibition;
    Table2 separates compound1 from analogues and individual isolates. The30mg/kg
    mouse regimen lacked efficacy. The fast-growing-bacteria assay delegates details
    to earlier references; HTML table/prose units and inoculum descriptions need checking
    before precise extraction.
- evidence_id: bioproject
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/bioproject/PRJNA118583
  locator: Public BioProject summary, accession, GEO relationship and publication
  accessed_at: '2026-10-21T07:03:19Z'
  support: supports
  summary: Official project connects GSE17640 to PMID19093848 and describes compound1
    exposure of M.tuberculosis at2,5,10 µg/mL for6h, matching the publication Methods.
    It describes oxidative/heat-shock transcriptional responses. A legacy treatment
    label calls the material garlic extract. This is a metadata discrepancy requiring
    sample-level reconciliation, not proof that the published experiment used a mixed
    extract.
- evidence_id: geo-lead
  kind: search
  reference: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE17640
  locator: Indexed GEO series metadata; direct GEO/sample access returned challenge
    pages
  accessed_at: '2026-10-21T07:03:19Z'
  support: context_only
  summary: Indexed source lists four arrays, GPL9036, and sample titles using garlic-extract
    wording. Individual sample metadata and raw files were not inspected. This is
    a dataset follow-up lead; the inspected BioProject supports the public accession
    relationship.
  search_scope: Exact GSE17640 and PMID19093848; direct GEO series and GSM440246 attempted
    without paid access.
- evidence_id: analogues
  kind: primary_source
  reference: DOI:10.1038/s41598-017-18948-w
  locator: https://www.nature.com/articles/s41598-017-18948-w —2018 Results, Figures1–3,
    Methods
  accessed_at: '2026-10-21T07:03:19Z'
  support: supports
  summary: The new efflux and biofilm experiments test synthetic compounds13–16. The
    natural target appears in historical comparison context. Those experiments therefore
    cannot establish efflux-pump inhibition or biofilm mechanism for CHEBI:66373.
- evidence_id: other-chemical
  kind: search
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6471189/
  locator: '2019 paper discovery result: compound identity and study title'
  accessed_at: '2026-10-21T07:03:19Z'
  support: context_only
  summary: The broad-spectrum2019 study tests 2-(methyldithio)pyridine-3-carbonitrile,
    a chemically different compound. Its MIC, killing and antifungal results are not
    adopted for the N-oxide.
  search_scope: Exact target name plus antibacterial/mechanism; structural analogues
    retained only as discovery boundaries.
- evidence_id: adapter
  kind: validation
  reference: kg-microbe-sources imodulondb datasets
  locator: Runner at /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw;
    public iModulonDB fallback
  accessed_at: '2026-10-21T07:03:19Z'
  support: supports
  summary: The installed console command was absent, but a local claw project runner
    resolved. Its datasets call exited2 on DNS failure for https://imodulondb.org/api/datasets.
    The fallback public site exposed no readable content. No module absence or target
    claim is inferred. The native seed itself has no expression object.
- evidence_id: validation
  kind: validation
  reference: just validate; just validate-strict
  locator: Isolated worktree002; /private/tmp/am-review-session/019-validation.tsv
  accessed_at: '2026-10-21T07:03:19Z'
  support: supports
  summary: Both focused commands exited0. LinkML reported no issues; strict scanned1
    target and0 ERROR rows.
- evidence_id: producer-boundary
  kind: primary_source
  reference: DOI:10.1021/np800572r
  locator: 'Primary article reproduced at https://www.lookchem.com/FreePDFArticle_14173-25-2_8791422.htm
    — Plant Material; Extraction and Isolation; Results and Discussion. Native producer
    rule: .claude/skills/curate-yaml-record/references/review-checklist.md:40 and
    src/antibioticmech/schema/antibioticmech.yaml:263,562.'
  accessed_at: '2026-10-21T07:08:53Z'
  support: context_only
  summary: Methods document purchased bulbs, solvent extraction, HPLC isolation and
    chemical characterization. The inspected experiment establishes a natural isolation
    source, not biosynthesis in the plant. Native producer semantics require the latter.
    Microarray Methods explicitly name compound1; FAS-I, AccD1 and mtFabH remain proposed
    explanations, with nonspecific toxicity unresolved.
- evidence_id: adapter-followup
  kind: validation
  reference: kg-microbe-sources imodulondb search
  locator: m_tuberculosis/modulome; exact query trxB2; /private/tmp/am-review-session/019-adversarial-imodulondb-trxB2.txt
  accessed_at: '2026-10-21T07:08:53Z'
  support: context_only
  summary: 'After discovery of m_tuberculosis/modulome in the successful public dataset
    inventory, the fresh query exited0: one gene, m_tuberculosis/modulome/Rv3913 (trxB2,
    thioredoxin reductase), and zero matching iModulons. This resolves a gene-context
    identifier only. It does not measure this compound response, assign module membership,
    or demonstrate a molecular target.'
assessments:
- assessment_id: identity
  area: identity
  topic: Exact N-oxide and disulfide identity
  outcome: supported
  summary: Official identity, source row and calculated structure agree. Protonated
    mass-spectrometry ions do not change the neutral record formula. Analogues remain
    distinct.
  target_ids:
  - CHEBI:66373
  evidence_ids:
  - record
  - owner
  - chebi
  - structure
  - primary
  - analogues
- assessment_id: classification
  area: grounding
  topic: Antibacterial filing and imported parents
  outcome: supported
  summary: The source role and primary experiment support antibacterial filing. Parent
    classes are broader and are not treated as exact equivalents.
  target_ids:
  - CHEBI:66373
  evidence_ids:
  - chebi
  - config
  - primary
- assessment_id: mechanism
  area: completeness
  topic: Qualified mechanism and experimental context
  outcome: concern
  summary: Specific pathway/response evidence warrants a curator assessment with explicit
    uncertainty. A mechanistic enum, direct target or causal edge must not be inferred
    from named candidate enzymes or response markers alone.
  target_ids:
  - CHEBI:66373
  evidence_ids:
  - record
  - primary
  - rubric
- assessment_id: dataset
  area: completeness
  topic: Public expression dataset follow-up
  outcome: concern
  summary: The publication Methods describe compound1 treatment, whereas the linked
    public project carries legacy garlic-extract wording. Reconcile sample-level provenance
    before a dataset annotation. A fresh structured-adapter query resolves the trxB2
    gene but supplies no matching module evidence and does not establish target binding.
  target_ids:
  - CHEBI:66373
  evidence_ids:
  - record
  - bioproject
  - geo-lead
  - adapter
- assessment_id: activity
  area: completeness
  topic: Strain- and assay-specific activity
  outcome: concern
  summary: The primary source supplies multiple separable experiments. Detailed extraction
    needs original units, cited assay methods and chemical-column identity; no species-wide
    susceptibility conclusion is warranted.
  target_ids:
  - CHEBI:66373
  evidence_ids:
  - record
  - primary
  - rubric
- assessment_id: producer
  area: completeness
  topic: Plant isolation source and unresolved biosynthesis
  outcome: unknown
  summary: Primary extraction and structural characterization support isolation from
    Allium stipitatum bulbs. They do not establish biosynthesis in that taxon, as
    required for producer_organisms. The existing source-owned isolation statement
    is supported; a producer entry remains conditional on additional evidence.
  target_ids:
  - CHEBI:66373
  evidence_ids:
  - record
  - primary
  - chebi
  - producer-boundary
- assessment_id: targets
  area: evidence
  topic: Direct molecular targets
  outcome: unknown
  summary: No native molecular target is asserted. The inspected study leaves the
    direct mechanism unresolved, and later analogue experiments cannot settle it for
    this molecule.
  target_ids:
  - CHEBI:66373
  evidence_ids:
  - record
  - primary
  - analogues
- assessment_id: other
  area: evidence
  topic: Resistance, clinical and causal-graph scope
  outcome: not_applicable
  summary: No native resistance, clinical-use or causal-graph assertion needs correction.
    Optional absence alone is not a defect. Experimental growth inhibition is not
    treatment efficacy.
  target_ids:
  - CHEBI:66373
  evidence_ids:
  - record
  - primary
  - rubric
- assessment_id: provenance
  area: provenance
  topic: Ownership and native status
  outcome: supported
  summary: Adopted fields and history match. The record appropriately remains SEEDED;
    future enrichment requires explicit curator provenance.
  target_ids:
  - CHEBI:66373
  evidence_ids:
  - record
  - owner
  - rubric
- assessment_id: schema
  area: schema
  topic: Focused schema gates
  outcome: supported
  summary: Both required focused gates pass.
  target_ids:
  - CHEBI:66373
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: chebi-66373-qualified-mechanism-dataset-curation
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Primary response experiments and a matching dataset need a qualified mechanism
    assessment
  description: The adopted paper provides a concrete mechanism-curation path with
    explicit alternatives. The matching public project can support experimental context
    after sample metadata reconciliation. The current empty fields assert no false
    target, and this finding does not require inventing one.
  target_ids:
  - CHEBI:66373
  field_paths:
  - mode_of_action
  - mode_of_action_notes
  - molecular_targets
  - datasets
  evidence_ids:
  - record
  - primary
  - bioproject
  - geo-lead
  - rubric
  rule_id: native-review-checklist:Mode of action, Molecular targets and Datasets
  native_severity: minor evidence-specific readiness gap
  normalization_reason: Specific inspected evidence warrants follow-up, while the
    current seed makes no unsupported mechanistic assertion.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2-methyldithio-pyridine-n-oxide.yaml
    role: Curator-owned scientific annotations; use native validated writer and curation
      event
- finding_id: F2
  issue_key: chebi-66373-primary-activity-enrichment
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Primary activity experiments are available for scoped extraction
  description: The inspected paper offers exact-compound activity observations. Preserve
    compound-column identity and individual organisms, and verify source-internal
    unit or inoculum ambiguities before detailed extraction. Absence of optional activity
    fields is not a schema violation.
  target_ids:
  - CHEBI:66373
  field_paths:
  - activity_spectrum
  evidence_ids:
  - record
  - primary
  - rubric
  rule_id: native-review-checklist:Activity
  native_severity: minor evidence-specific readiness gap
  normalization_reason: A concrete source enables enrichment; no incorrect activity
    object is currently asserted.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2-methyldithio-pyridine-n-oxide.yaml
    role: Curator-owned scientific annotations; use native validated writer and curation
      event
- finding_id: F3
  issue_key: chebi-66373-structured-producer-evidence
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Plant isolation supports a source statement; a biosynthetic producer remains
    unresolved
  description: The primary paper isolates compound1 from Allium stipitatum bulbs.
    This supports the current source definition but does not by itself satisfy the
    schema requirement that producer_organisms biosynthesize the compound. Investigate
    biosynthetic support only if a structured producer annotation is pursued; no current
    producer claim is incorrect.
  target_ids:
  - CHEBI:66373
  field_paths:
  - producer_organisms
  evidence_ids:
  - record
  - primary
  - chebi
  - producer-boundary
  rule_id: native-review-checklist:Producer
  native_severity: Informational conditional enrichment opportunity
  normalization_reason: The optional producer list is absent and isolation alone does
    not establish the biosynthetic claim required to populate it.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2-methyldithio-pyridine-n-oxide.yaml
    role: Curator-owned scientific annotations; use native validated writer and curation
      event
actions:
- action_id: A1
  description: Curate a qualified mechanism narrative or explicit unresolved disposition
    using experimental observations and alternatives. Assess the public expression-dataset
    link with sample-level provenance before adding it. Keep candidate targets and
    response markers distinct from directly demonstrated targets.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:66373
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2-methyldithio-pyridine-n-oxide.yaml
    role: Curator-owned scientific annotations; use native validated writer and curation
      event
  acceptance_checks:
  - Each claim has exact-compound, taxon, assay and primary-source context; no direct
    binding or enzyme inhibition is invented.
  - Dataset accession and original treatment-label caveat remain traceable.
  - Native writer/history and focused strict, reproducibility and QC gates are used.
- action_id: A2
  description: Extract only compound1 activity observations after consulting original
    assay references and resolving any presentation ambiguities; keep endpoints and
    experimental systems separate.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:66373
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2-methyldithio-pyridine-n-oxide.yaml
    role: Curator-owned scientific annotations; use native validated writer and curation
      event
  acceptance_checks:
  - MIC method, units, endpoint, organism and isolate are present and source-traceable.
  - Resistance to comparator drugs is not assigned as resistance to this compound;
    animal outcomes are not generalized to clinical status.
  - Use native validated writer/history and required gates.
- action_id: A3
  description: Preserve the supported source-owned isolation statement. Before adding
    Allium stipitatum to producer_organisms, find exact-compound evidence that supports
    biosynthesis in that taxon; otherwise retain the unresolved disposition and do
    not infer production solely from bulb extraction.
  finding_ids:
  - F3
  target_ids:
  - CHEBI:66373
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/2-methyldithio-pyridine-n-oxide.yaml
    role: Curator-owned scientific annotations; use native validated writer and curation
      event
  acceptance_checks:
  - Any producer annotation has evidence for biosynthesis, exact taxon grounding and
    claim-specific provenance; bulb isolation alone is not sufficient.
  - If no biosynthetic support is established, leave the optional producer list empty
    and preserve the supported isolation statement.
  - Use native writer/history and focused strict, reproducibility and QC gates for
    any separately authorized curation.
limitations:
- The primary full-text Results, tables and Methods were inspected; cited older assay
  protocols and publisher PDF were not. Presentation ambiguities require resolution
  before fine-grained activity extraction.
- GEO sample/raw data access was blocked; the public BioProject linkage and publication
  Methods were inspected. The original iModulonDB discovery attempt failed on DNS;
  a later focused query succeeded but provided gene context only, without module evidence.
- Independent Reaxys content was not inspected; official ChEBI registry assertion
  was verified.
- Bounded research does not establish global evidence absence. No paid research or
  native record edits occurred.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Provenance capture preceded judgment; expanded inputs preserved every original hash
  and base revision.
- Ignored and hidden files were included in all searches used for local absence.
- The native record remains SEEDED; optional empty fields are not blanket schema defects.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:66373
- https://pmc.ncbi.nlm.nih.gov/articles/PMC2765505/
- https://www.ncbi.nlm.nih.gov/bioproject/PRJNA118583
tags:
- antibacterial
- disulfide
- seeded
- mechanism-uncertainty
- expression-dataset
```
