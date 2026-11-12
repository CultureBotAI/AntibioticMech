# AFN-1252: supported active-moiety identity and primary FabI evidence

- Review: 20261021T083604Z-afn-1252-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:21:56Z
- Finished UTC: 2026-10-21T08:36:04Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The neutral E compound, afabicin desphosphono/DEBIO-1452 synonyms and narrow antistaphylococcal activity are supported. One minor finding concerns a curator paraphrase in the verbatim snippet field. Primary binding, strain-scoped resistance, activity and expression studies provide optional enrichment; afabicin prodrug, salt forms, reference proteins and tested subjects remain distinct.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position079; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:curator-8edc5e6516 | data/antibiotics/antibacterial/afn-1252.yaml | generated | AFN-1252 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:curator-8edc5e6516 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:curator-8edc5e6516 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:curator-8edc5e6516 | Actual focused execution exited 0. |
| Structured FabI context | passed | False | antibioticmech:curator-8edc5e6516 | Actual query exited0: one gene and zero modules. |
| Authoritative full QC | failed | True | antibioticmech:curator-8edc5e6516 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:curator-8edc5e6516 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:curator-8edc5e6516 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:curator-8edc5e6516 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:curator-8edc5e6516 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:curator-8edc5e6516 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:curator-8edc5e6516 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:curator-8edc5e6516 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:curator-8edc5e6516 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact active moiety and synonyms

identity: supported. Targets: antibioticmech:curator-8edc5e6516.

Both native encodings and official full-key authorities agree. Original papers equate both synonyms and distinguish the afabicin prodrug and tosylate preparations.

### Proposed curator identity

grounding: supported. Targets: antibioticmech:curator-8edc5e6516.

Stable DOI-fragment mint reproduces; optional missing external ontology grounding does not invalidate this explicit proposed curator record.

### Narrow antistaphylococcal activity

evidence: supported. Targets: antibioticmech:curator-8edc5e6516.

Adopted primary panel supports the exact native activity summary, including methicillin-resistant isolates; it does not imply universal absence of activity outside staphylococci.

### Verbatim evidence placement

evidence: concern. Targets: antibioticmech:curator-8edc5e6516.

The supported curator summary is not a direct quotation and belongs in notes.

### Direct FabI target and pathway evidence

completeness: supported. Targets: antibioticmech:curator-8edc5e6516.

Primary enzyme, structural and radioligand evidence corroborates the definition and offers optional target objects. Reference loci are not experimental subject assignments.

### Bounded resistance observations

completeness: unknown. Targets: antibioticmech:curator-8edc5e6516.

Concrete primary experiments enable careful enrichment after exact variant/strain/protein and form reconciliation. Other-drug resistance and reference annotation are not equivalent evidence.

### Response dataset

completeness: unknown. Targets: antibioticmech:curator-8edc5e6516.

Public GSE19400 offers optional expression context with explicit dose/time/strain; no direct regulator binding follows.

### Clinical, producer and graph boundaries

scope: not_applicable. Targets: antibioticmech:curator-8edc5e6516.

No native assertions require correction. Trial or prodrug distribution reports do not establish approval; no biosynthetic producer or fully curated causal graph is inferred.

### Generated owner and historical evidence

ownership: supported. Targets: antibioticmech:curator-8edc5e6516.

Maintained curator row owns correction; historical checkpoint remains intact. All15 captured hashes are unchanged and proposed status is preserved.

## Findings

### F1: Move the curator paraphrase out of the verbatim snippet field

minor / open / confirmed; issue key: afn-1252-curator-paraphrase-in-snippet.

The Karlowsky-attributed statement accurately summarizes the tested staphylococcal panel but is not word-for-word source text. Retain its interpretation in notes and use a short verified quotation if a snippet is supplied.

### F2: Curate bounded primary target, resistance and expression evidence

informational / open / confirmed; issue key: afn-1252-primary-target-resistance-expression-enrichment.

Available original biochemical, structural, organism-specific activity/resistance and expression evidence can populate optional claims. This review advances beyond the earlier abstract-only access checkpoint while preserving its reference-protein and experimental-identity limitations.

## Recommended Actions And Acceptance Checks

### A1

Correct maintained evidence field placement and regenerate the source concept.

- Move the current paraphrase to evidence_notes in curator_antibiotics.tsv row11; if retained, verify a short evidence_snippet verbatim against PMID19487444 with a precise locator.
- Preserve exact source ID, chemical form and assay scope; reseed with native validated writer/history and check focused schema/strict, chemistry and required corpus gates.

### A2

Optionally add the experimentally supported claims with exact identity and assay context.

- Ground the FabI target taxon-agnostically with appropriate experimental protein examples; explicitly verify actual strain/protein joins before using NCTC8325,MRSA252 or USA300HOU reference entries.
- Separate crystal/radioligand binding, enzyme inhibition, cellular precursor incorporation and MIC endpoints; retain3′NADPH versus NADPH, assay conditions, tosylate/freebase equivalence and the distinct afabicin prodrug.
- Keep laboratory strain/variant resistance observations, heterologous E.coli experiments, auxotroph bypass and methicillin resistance distinct. Do not infer clinical breakpoint resistance or universal absence of future resistance.
- For GSE19400 preserve RN4220,50ng/mL,15min,three treated/three controls; treat SaeRS/FapR-linked transcription as downstream response, not direct drug binding.
- Use write_validated_antibiotic and record_curation_event, preserve historical research provenance, and pass focused and required shared gates before independent scientific sign-off.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/afn-1252.yaml; Entire YAML after initial input capture | supports | PROPOSED/MINTED curator compound with FabI-inhibitor definition, two exact synonyms, antibacterial role, PubChem10407120, neutral E structure, one source-concept citation/snippet/notes and one proposed history event. No molecular-target, activity, resistance, producer, clinical, graph or dataset collection is asserted. |
| owner | curation/curator_antibiotics.tsv; Row11; load_curator_concepts and generated emission in seed_from_sources.py | supports | Source DOI fragment, structure, synonyms and evidence reproduce the native record. Seeder copies evidence_snippet without quotation validation. SHA256 of CURATOR&#124;DOI:10.1128/AAC.00400-09#afn-1252 reproduces mint8edc5e6516. Curator-only proposed status is deliberate; no adopted exact grounding or formal override was found in ignored-inclusive maintained searches. All 15 captured input hashes are unchanged. |
| identity | https://pubchem.ncbi.nlm.nih.gov/compound/10407120; 079-pubchem.json; official FDA SRS UNII:T3O718IKKM page | supports | Official PubChem and FDA substance record agree on neutral C22H21N3O3, full key QXTWSUQCXCWEHF-JXMROGBWSA-N and AFN-1252/DEBIO1452/afabicin desphosphono names. The SRS substance identifier is identity evidence, not proof of approval. PubChem connectivity-only SMILES is not mistaken for its complete stereochemical InChI. |
| chemistry | Independent RDKit calculations; 079-chemistry.json; 2012 Figure2 visually inspected | supports | Both native encodings regenerate the same neutral single-fragment full key, formula, trans alkene, no tetrahedral centres, average mass375.428 and exact mass375.158291532. Native mass fields are absent, not erroneous. Original 2012 parent-compound drawing agrees; salt and prodrug structures are distinct. |
| adopted | PMID:19487444; DOI:10.1128/AAC.00400-09; PMC2715641 complete main text and Table1 | supports | CANWARD2007 clinical collection contains502 S.aureus isolates (375MSSA/127MRSA) and51 S.epidermidis (42methicillin-susceptible/9resistant). All were inhibited at≤0.12µg/mL by AFN-1252. CLSI broth microdilution used35°C,20–24h and DMSO stocks; S.aureus ATCC29213 QC MIC0.015µg/mL. Native snippet substance is correct but its author-attributed prose is a paraphrase, not verbatim. Methicillin resistance is not AFN-1252 resistance. Some nonstaphylococcal table values are below4µg/mL despite broad narrative language; native narrow-spectrum wording does not assert universal species exclusivity. |
| target | PMID:22948878; DOI:10.1128/AAC.01411-12; PMC3486558 full main text/Tables1–5; Figures2 and4 visually inspected | supports | Purified S.aureus ATCC35556 FabI inhibition, fatty-acid precursor incorporation and a1.8Å ternary crystal structure (PDB4FS3 with3′NADPH) support FabI as a direct target. Functional IC50 is14nM and reported Ki12.8±0.5nM under that assay; neither is an MIC or interchangeable with a binding KD. The paper explicitly distinguishes freebase AFN1252-0000 from tosylate anhydrate0300 and monohydrate0301, and states all concentrations as freebase equivalents. Preserve material and assay basis. The reported24h time-kill reductions2.0/2.9log do not themselves reach a3log bactericidal threshold. |
| resistance | PMID:24189061; DOI:10.1074/jbc.M113.512905; PMC3868742 full main text,Table1 and figure captions | supports | S.aureus RN4220 FabI substitutions M99T and Y147H are linked to increased AFN-1252 MICs with expression/genetic and biochemical evidence. Wild-type3.9ng/mL versus MWF32(M99T)250 and MWF33(Y147H)500ng/mL were measured in the specified laboratory context; these are relative resistance observations, not clinical breakpoint categories. Radiolabeled drug coelution demonstrates binding to FabI with NADPH; kinetic apparent Ki4nM wild type versus69nM M99T is assay-specific. Y147H catalytic instability prevents a reliable comparable kinetic affinity estimate. Heterologous E.coli assays and engineered double-mutant experiments must remain separate from naturally selected S.aureus observations. Fatty-acid rescue in a defined auxotrophic background rules out a universal no-bypass claim. |
| synonyms | PMID:25691627; PMID:30559136; PMC4394798 abstract/introduction/methods/Table1; PMC6395911 introduction | supports | 2015 explicitly equates Debio1452 with AFN-1252 and distinguishes Debio1450/AFN-1720 as its prodrug. The2019 paper explicitly equates afabicin desphosphono with Debio1452/AFN-1252 while afabicin itself is the prodrug. These directly support native synonyms. The2015 cation-adjusted MHB panel has471 S.aureus and103 coagulase-negative staphylococci, all inhibited at≤0.12 and≤0.5µg/mL respectively; no clinical susceptibility breakpoint for AFN-1252 is asserted. The2019 introduction is used only for synonym/form distinction, not a new clinical-status conclusion. |
| expression | PMID:23459481; DOI:10.1128/AAC.02307-12; PMC3632907 abstract, introduction and complete Methods including accession statement | context_only | RN4220 Affymetrix expression experiment uses50ng/mL AFN-1252 for15min, three treated and three DMSO controls. The paper describes physiological-state-dependent virulence transcription effects with SaeRS genetics and an animal infection model. This is downstream response/regulatory dependence, not demonstrated direct binding of AFN-1252 to SaeR/SaeS or FapR. Only the stated sections were inspected; no raw expression reanalysis. |
| geo | https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE19400; 079-geo.txt official series metadata | context_only | GSE19400 is public expression profiling by array, linked to PMID23459481 and PRJNA121765, six GSM samples and GPL1339, with15min AFN-1252 exposure. This is a concrete optional dataset link; it is distinct from the USA300HOU iModulonDB reference context. |
| historical | research/2026-10-14-afn1252-reference-context.json; Entire maintained checkpoint; owning audit script constants/metadata handling | supports | The earlier checkpoint truthfully recorded publisher403 holds, indexed-abstract-only coverage for PMIDs22948878/24189061, and no biological write. Its UniProt Q2FZQ3/NCTC8325 and Q6GI75/MRSA252 entries are explicitly reference proteins, not experimentally assigned resistant subjects. This review has now read public PMC primary main texts, resolving that access boundary for those passages; it does not silently update the historical artifact, validate every supplemental result, or equate reference strains with tested RN4220/ATCC35556 subjects. |
| adapter | iModulonDB s_aureus/staph_precise165; 079-imodulondb-fabi.txt and inspected same-session dataset inventory | context_only | Before web research, exact fabI query returned USA300HOU_RS05010, enoyl-ACP reductase, one gene and zero modules. This supports a gene-name context only; it neither proves binding nor substitutes USA300HOU for experimental strains. No module summary applies. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Evidence standard, Identity/Equivalence and optional-field rules | supports | Evidence.snippet is verbatim source text; curator interpretation belongs in notes. Exact active moiety, salts and prodrug remain separate. Optional collections require narrow supporting claims when populated but are not mandatory solely because the record is proposed. |
| search | CultureBotAI/AntibioticMech; 079-local-hits.txt;078079-maintained-search.txt; bounded exact-name primary discovery | context_only | Ignored-inclusive searches found the curator row, review queue and prior resistance-reference checkpoint/audit script. No exact source adoption or native claim overlay was found in the examined surfaces. The sole adopted primary study and both checkpoint primary leads were read in full main text; additional papers were inspected only to the stated bounds. No exhaustive evidence-absence claim. |

## Limits And Additional Notes

- Full main texts for the2009,2012 and2013 resistance studies were read, with2012 structure/binding figures visually inspected. Supplements and raw assay data were not independently reanalysed; publication-internal methodological discrepancies remain qualifiers.
- The2013 expression paper was inspected through abstract/introduction/Methods and accession metadata;2015 through abstract/introduction/Methods/Table1;2019 introduction only for synonym/prodrug identity. Their remaining results are not claimed as reviewed.
- The2012 paper uses freebase and tosylate forms with stated freebase-equivalent concentrations. Exact preparation must accompany any future assay entry rather than transferring salt mass silently.
- The earlier resistance checkpoint records a different access state and remains historical. Newly accessible primary text does not itself resolve every experimental protein accession or justify replacing reference strain annotations.
- No current clinical approval or biosynthetic producer search was undertaken because neither is asserted. FDA SRS presence and clinical development references alone are not approval evidence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T083604Z-afn-1252-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'AFN-1252: supported active-moiety identity and primary FabI evidence'
started_at: '2026-10-21T08:21:56Z'
finished_at: '2026-10-21T08:36:04Z'
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
summary: The neutral E compound, afabicin desphosphono/DEBIO-1452 synonyms and narrow
  antistaphylococcal activity are supported. One minor finding concerns a curator
  paraphrase in the verbatim snippet field. Primary binding, strain-scoped resistance,
  activity and expression studies provide optional enrichment; afabicin prodrug, salt
  forms, reference proteins and tested subjects remain distinct.
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
  - path: data/antibiotics/antibacterial/afn-1252.yaml
    sha256: a8a0801f12c3b7cb4de8e649746e22b42563182db24e939461c5885f75943efb
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
  - path: scripts/audit_afn1252_references.py
    sha256: 4cb569aadff4510dc9a482030b609b0242c81e7ed634c85d04b161becf68e93c
    role: context
  - path: research/2026-10-14-afn1252-reference-context.json
    sha256: 61d9228df8ba8f7d512b26c8e516d46d22847e5b37d7190fde3a98d8b2ae8274
    role: context
targets:
- target_id: antibioticmech:curator-8edc5e6516
  path: data/antibiotics/antibacterial/afn-1252.yaml
  label: AFN-1252
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Curator-inventory identity, structure, definition and source evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Curator inventory transform and generated ownership
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding decisions
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position079; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:curator-8edc5e6516
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-8edc5e6516
  command: .venv/bin/python /private/tmp/am-review-session/focus008-root.py 79
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-8edc5e6516
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/afn-1252.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:curator-8edc5e6516
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/afn-1252.yaml --out /private/tmp/am-review-session/079-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-fabi
  name: Structured FabI context
  status: passed
  required: false
  summary: 'Actual query exited0: one gene and zero modules.'
  target_ids:
  - antibioticmech:curator-8edc5e6516
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:curator-8edc5e6516
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
  - antibioticmech:curator-8edc5e6516
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
  - antibioticmech:curator-8edc5e6516
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
  - antibioticmech:curator-8edc5e6516
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
  - antibioticmech:curator-8edc5e6516
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
  - antibioticmech:curator-8edc5e6516
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
  - antibioticmech:curator-8edc5e6516
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
  - antibioticmech:curator-8edc5e6516
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
  - antibioticmech:curator-8edc5e6516
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/afn-1252.yaml
  locator: Entire YAML after initial input capture
  accessed_at: '2026-10-21T08:35:18Z'
  support: supports
  summary: PROPOSED/MINTED curator compound with FabI-inhibitor definition, two exact
    synonyms, antibacterial role, PubChem10407120, neutral E structure, one source-concept
    citation/snippet/notes and one proposed history event. No molecular-target, activity,
    resistance, producer, clinical, graph or dataset collection is asserted.
- evidence_id: owner
  kind: record_content
  reference: curation/curator_antibiotics.tsv
  locator: Row11; load_curator_concepts and generated emission in seed_from_sources.py
  accessed_at: '2026-10-21T08:35:18Z'
  support: supports
  summary: Source DOI fragment, structure, synonyms and evidence reproduce the native
    record. Seeder copies evidence_snippet without quotation validation. SHA256 of
    CURATOR|DOI:10.1128/AAC.00400-09#afn-1252 reproduces mint8edc5e6516. Curator-only
    proposed status is deliberate; no adopted exact grounding or formal override was
    found in ignored-inclusive maintained searches. All 15 captured input hashes are
    unchanged.
  snapshot_sha256: f83be04ea5d9e4afec577ed504487dfb94b8f9bc87e9d821c6cc6238da3c4c2e
- evidence_id: identity
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/10407120
  locator: 079-pubchem.json; official FDA SRS UNII:T3O718IKKM page
  accessed_at: '2026-10-21T08:35:18Z'
  support: supports
  summary: Official PubChem and FDA substance record agree on neutral C22H21N3O3,
    full key QXTWSUQCXCWEHF-JXMROGBWSA-N and AFN-1252/DEBIO1452/afabicin desphosphono
    names. The SRS substance identifier is identity evidence, not proof of approval.
    PubChem connectivity-only SMILES is not mistaken for its complete stereochemical
    InChI.
  snapshot_sha256: e772a967b2c0af74e5555bb067d68dca3936f9117b550b700a85cd15e1f868a3
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit calculations
  locator: 079-chemistry.json; 2012 Figure2 visually inspected
  accessed_at: '2026-10-21T08:35:18Z'
  support: supports
  summary: Both native encodings regenerate the same neutral single-fragment full
    key, formula, trans alkene, no tetrahedral centres, average mass375.428 and exact
    mass375.158291532. Native mass fields are absent, not erroneous. Original 2012
    parent-compound drawing agrees; salt and prodrug structures are distinct.
  snapshot_sha256: 3b1c90dc8e902710e142a37a9c3bf74e051f4e9c16014c89cd4da8443385a773
- evidence_id: adopted
  kind: primary_source
  reference: PMID:19487444
  locator: DOI:10.1128/AAC.00400-09; PMC2715641 complete main text and Table1
  accessed_at: '2026-10-21T08:35:18Z'
  support: supports
  summary: CANWARD2007 clinical collection contains502 S.aureus isolates (375MSSA/127MRSA)
    and51 S.epidermidis (42methicillin-susceptible/9resistant). All were inhibited
    at≤0.12µg/mL by AFN-1252. CLSI broth microdilution used35°C,20–24h and DMSO stocks;
    S.aureus ATCC29213 QC MIC0.015µg/mL. Native snippet substance is correct but its
    author-attributed prose is a paraphrase, not verbatim. Methicillin resistance
    is not AFN-1252 resistance. Some nonstaphylococcal table values are below4µg/mL
    despite broad narrative language; native narrow-spectrum wording does not assert
    universal species exclusivity.
  snapshot_sha256: e7d8744fd00dc38e0d113507fb22044c59a1655a85383cab038780fee86373c9
- evidence_id: target
  kind: primary_source
  reference: PMID:22948878
  locator: DOI:10.1128/AAC.01411-12; PMC3486558 full main text/Tables1–5; Figures2
    and4 visually inspected
  accessed_at: '2026-10-21T08:35:18Z'
  support: supports
  summary: Purified S.aureus ATCC35556 FabI inhibition, fatty-acid precursor incorporation
    and a1.8Å ternary crystal structure (PDB4FS3 with3′NADPH) support FabI as a direct
    target. Functional IC50 is14nM and reported Ki12.8±0.5nM under that assay; neither
    is an MIC or interchangeable with a binding KD. The paper explicitly distinguishes
    freebase AFN1252-0000 from tosylate anhydrate0300 and monohydrate0301, and states
    all concentrations as freebase equivalents. Preserve material and assay basis.
    The reported24h time-kill reductions2.0/2.9log do not themselves reach a3log bactericidal
    threshold.
  snapshot_sha256: 39bd94267d2a5724eef8c36d71b4274461dc865efb73faa1a4e418f2fd8222ee
- evidence_id: resistance
  kind: primary_source
  reference: PMID:24189061
  locator: DOI:10.1074/jbc.M113.512905; PMC3868742 full main text,Table1 and figure
    captions
  accessed_at: '2026-10-21T08:35:18Z'
  support: supports
  summary: S.aureus RN4220 FabI substitutions M99T and Y147H are linked to increased
    AFN-1252 MICs with expression/genetic and biochemical evidence. Wild-type3.9ng/mL
    versus MWF32(M99T)250 and MWF33(Y147H)500ng/mL were measured in the specified
    laboratory context; these are relative resistance observations, not clinical breakpoint
    categories. Radiolabeled drug coelution demonstrates binding to FabI with NADPH;
    kinetic apparent Ki4nM wild type versus69nM M99T is assay-specific. Y147H catalytic
    instability prevents a reliable comparable kinetic affinity estimate. Heterologous
    E.coli assays and engineered double-mutant experiments must remain separate from
    naturally selected S.aureus observations. Fatty-acid rescue in a defined auxotrophic
    background rules out a universal no-bypass claim.
  snapshot_sha256: e2f7907d147ff23fc48b1704ca7bd4fb7f78bcea152fb19b553ee60aa2ae9ab9
- evidence_id: synonyms
  kind: primary_source
  reference: PMID:25691627; PMID:30559136
  locator: PMC4394798 abstract/introduction/methods/Table1; PMC6395911 introduction
  accessed_at: '2026-10-21T08:35:18Z'
  support: supports
  summary: 2015 explicitly equates Debio1452 with AFN-1252 and distinguishes Debio1450/AFN-1720
    as its prodrug. The2019 paper explicitly equates afabicin desphosphono with Debio1452/AFN-1252
    while afabicin itself is the prodrug. These directly support native synonyms.
    The2015 cation-adjusted MHB panel has471 S.aureus and103 coagulase-negative staphylococci,
    all inhibited at≤0.12 and≤0.5µg/mL respectively; no clinical susceptibility breakpoint
    for AFN-1252 is asserted. The2019 introduction is used only for synonym/form distinction,
    not a new clinical-status conclusion.
  snapshot_sha256: 044f95196c7e298cfe1b744a10d8a48aa7a020359456e499ef490f535120d214
- evidence_id: expression
  kind: primary_source
  reference: PMID:23459481
  locator: DOI:10.1128/AAC.02307-12; PMC3632907 abstract, introduction and complete
    Methods including accession statement
  accessed_at: '2026-10-21T08:35:18Z'
  support: context_only
  summary: RN4220 Affymetrix expression experiment uses50ng/mL AFN-1252 for15min,
    three treated and three DMSO controls. The paper describes physiological-state-dependent
    virulence transcription effects with SaeRS genetics and an animal infection model.
    This is downstream response/regulatory dependence, not demonstrated direct binding
    of AFN-1252 to SaeR/SaeS or FapR. Only the stated sections were inspected; no
    raw expression reanalysis.
  snapshot_sha256: 6adf4cb2e734b7564a632d8f132c76394b32bfda38375e45ebd3ff185ef4988b
- evidence_id: geo
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE19400
  locator: 079-geo.txt official series metadata
  accessed_at: '2026-10-21T08:35:18Z'
  support: context_only
  summary: GSE19400 is public expression profiling by array, linked to PMID23459481
    and PRJNA121765, six GSM samples and GPL1339, with15min AFN-1252 exposure. This
    is a concrete optional dataset link; it is distinct from the USA300HOU iModulonDB
    reference context.
  snapshot_sha256: b76eddae68c4dc3a579ccafe4205e8628f6a1553619f2c0fd3b786457781b03b
- evidence_id: historical
  kind: record_content
  reference: research/2026-10-14-afn1252-reference-context.json
  locator: Entire maintained checkpoint; owning audit script constants/metadata handling
  accessed_at: '2026-10-21T08:35:18Z'
  support: supports
  summary: The earlier checkpoint truthfully recorded publisher403 holds, indexed-abstract-only
    coverage for PMIDs22948878/24189061, and no biological write. Its UniProt Q2FZQ3/NCTC8325
    and Q6GI75/MRSA252 entries are explicitly reference proteins, not experimentally
    assigned resistant subjects. This review has now read public PMC primary main
    texts, resolving that access boundary for those passages; it does not silently
    update the historical artifact, validate every supplemental result, or equate
    reference strains with tested RN4220/ATCC35556 subjects.
- evidence_id: adapter
  kind: database
  reference: iModulonDB s_aureus/staph_precise165
  locator: 079-imodulondb-fabi.txt and inspected same-session dataset inventory
  accessed_at: '2026-10-21T08:35:18Z'
  support: context_only
  summary: Before web research, exact fabI query returned USA300HOU_RS05010, enoyl-ACP
    reductase, one gene and zero modules. This supports a gene-name context only;
    it neither proves binding nor substitutes USA300HOU for experimental strains.
    No module summary applies.
  snapshot_sha256: 596166a3b00e07a69e27ee5efc9e750adf0cb5a5ab23f8ab3f897c144484e8d6
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Evidence standard, Identity/Equivalence and optional-field rules
  accessed_at: '2026-10-21T08:35:18Z'
  support: supports
  summary: Evidence.snippet is verbatim source text; curator interpretation belongs
    in notes. Exact active moiety, salts and prodrug remain separate. Optional collections
    require narrow supporting claims when populated but are not mandatory solely because
    the record is proposed.
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 079-local-hits.txt;078079-maintained-search.txt; bounded exact-name primary
    discovery
  accessed_at: '2026-10-21T08:35:18Z'
  support: context_only
  summary: Ignored-inclusive searches found the curator row, review queue and prior
    resistance-reference checkpoint/audit script. No exact source adoption or native
    claim overlay was found in the examined surfaces. The sole adopted primary study
    and both checkpoint primary leads were read in full main text; additional papers
    were inspected only to the stated bounds. No exhaustive evidence-absence claim.
  search_scope: rg --no-ignore --hidden across isolated batch008 excluding .git/.venv;
    focused maintained surfaces and exact AFN-1252/key/mint follow-up. Official PubChem/FDA-SRS/EuropePMC/PMC/GEO
    and structured iModulonDB; no paid sources.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact active moiety and synonyms
  outcome: supported
  summary: Both native encodings and official full-key authorities agree. Original
    papers equate both synonyms and distinguish the afabicin prodrug and tosylate
    preparations.
  target_ids:
  - antibioticmech:curator-8edc5e6516
  evidence_ids:
  - identity
  - chemistry
  - synonyms
  - target
- assessment_id: grounding
  area: grounding
  topic: Proposed curator identity
  outcome: supported
  summary: Stable DOI-fragment mint reproduces; optional missing external ontology
    grounding does not invalidate this explicit proposed curator record.
  target_ids:
  - antibioticmech:curator-8edc5e6516
  evidence_ids:
  - owner
  - native
- assessment_id: activity
  area: evidence
  topic: Narrow antistaphylococcal activity
  outcome: supported
  summary: Adopted primary panel supports the exact native activity summary, including
    methicillin-resistant isolates; it does not imply universal absence of activity
    outside staphylococci.
  target_ids:
  - antibioticmech:curator-8edc5e6516
  evidence_ids:
  - adopted
  - synonyms
- assessment_id: snippet
  area: evidence
  topic: Verbatim evidence placement
  outcome: concern
  summary: The supported curator summary is not a direct quotation and belongs in
    notes.
  target_ids:
  - antibioticmech:curator-8edc5e6516
  evidence_ids:
  - owner
  - adopted
  - rubric
- assessment_id: target
  area: completeness
  topic: Direct FabI target and pathway evidence
  outcome: supported
  summary: Primary enzyme, structural and radioligand evidence corroborates the definition
    and offers optional target objects. Reference loci are not experimental subject
    assignments.
  target_ids:
  - antibioticmech:curator-8edc5e6516
  evidence_ids:
  - target
  - resistance
  - adapter
  - historical
- assessment_id: resistance
  area: completeness
  topic: Bounded resistance observations
  outcome: unknown
  summary: Concrete primary experiments enable careful enrichment after exact variant/strain/protein
    and form reconciliation. Other-drug resistance and reference annotation are not
    equivalent evidence.
  target_ids:
  - antibioticmech:curator-8edc5e6516
  evidence_ids:
  - resistance
  - historical
- assessment_id: dataset
  area: completeness
  topic: Response dataset
  outcome: unknown
  summary: Public GSE19400 offers optional expression context with explicit dose/time/strain;
    no direct regulator binding follows.
  target_ids:
  - antibioticmech:curator-8edc5e6516
  evidence_ids:
  - expression
  - geo
  - adapter
- assessment_id: other
  area: scope
  topic: Clinical, producer and graph boundaries
  outcome: not_applicable
  summary: No native assertions require correction. Trial or prodrug distribution
    reports do not establish approval; no biosynthetic producer or fully curated causal
    graph is inferred.
  target_ids:
  - antibioticmech:curator-8edc5e6516
  evidence_ids:
  - native
  - synonyms
  - rubric
- assessment_id: ownership
  area: ownership
  topic: Generated owner and historical evidence
  outcome: supported
  summary: Maintained curator row owns correction; historical checkpoint remains intact.
    All15 captured hashes are unchanged and proposed status is preserved.
  target_ids:
  - antibioticmech:curator-8edc5e6516
  evidence_ids:
  - owner
  - historical
findings:
- finding_id: F1
  issue_key: afn-1252-curator-paraphrase-in-snippet
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Move the curator paraphrase out of the verbatim snippet field
  description: The Karlowsky-attributed statement accurately summarizes the tested
    staphylococcal panel but is not word-for-word source text. Retain its interpretation
    in notes and use a short verified quotation if a snippet is supplied.
  target_ids:
  - antibioticmech:curator-8edc5e6516
  field_paths:
  - source_concepts.evidence.snippet
  evidence_ids:
  - owner
  - adopted
  - rubric
  rule_id: 'native-review-checklist: Evidence standard'
  native_severity: minor evidence-format provenance
  normalization_reason: Supported scientific content is in the wrong evidence slot;
    this is not fabricated activity.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Curator-inventory identity, structure, definition and source evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Curator inventory transform and generated ownership
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding decisions
- finding_id: F2
  issue_key: afn-1252-primary-target-resistance-expression-enrichment
  category: completeness
  severity: informational
  status: open
  certainty: confirmed
  title: Curate bounded primary target, resistance and expression evidence
  description: Available original biochemical, structural, organism-specific activity/resistance
    and expression evidence can populate optional claims. This review advances beyond
    the earlier abstract-only access checkpoint while preserving its reference-protein
    and experimental-identity limitations.
  target_ids:
  - antibioticmech:curator-8edc5e6516
  field_paths:
  - evidence
  - molecular_targets
  - activity_spectrum
  - resistance_mechanisms
  - datasets
  - discussions
  evidence_ids:
  - target
  - resistance
  - expression
  - geo
  - historical
  - rubric
  rule_id: 'native-review-checklist: Targets, Resistance, Activity and Datasets'
  native_severity: informational optional enrichment
  normalization_reason: The definition is supported and optional missing objects are
    not required-field errors.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/afn-1252.yaml
    role: Curator-owned claims, evidence, activity, resistance and dataset links through
      validated writer/history
actions:
- action_id: A1
  description: Correct maintained evidence field placement and regenerate the source
    concept.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:curator-8edc5e6516
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/curator_antibiotics.tsv
    role: Curator-inventory identity, structure, definition and source evidence
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Curator inventory transform and generated ownership
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding decisions
  acceptance_checks:
  - Move the current paraphrase to evidence_notes in curator_antibiotics.tsv row11;
    if retained, verify a short evidence_snippet verbatim against PMID19487444 with
    a precise locator.
  - Preserve exact source ID, chemical form and assay scope; reseed with native validated
    writer/history and check focused schema/strict, chemistry and required corpus
    gates.
- action_id: A2
  description: Optionally add the experimentally supported claims with exact identity
    and assay context.
  finding_ids:
  - F2
  target_ids:
  - antibioticmech:curator-8edc5e6516
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/afn-1252.yaml
    role: Curator-owned claims, evidence, activity, resistance and dataset links through
      validated writer/history
  acceptance_checks:
  - Ground the FabI target taxon-agnostically with appropriate experimental protein
    examples; explicitly verify actual strain/protein joins before using NCTC8325,MRSA252
    or USA300HOU reference entries.
  - Separate crystal/radioligand binding, enzyme inhibition, cellular precursor incorporation
    and MIC endpoints; retain3′NADPH versus NADPH, assay conditions, tosylate/freebase
    equivalence and the distinct afabicin prodrug.
  - Keep laboratory strain/variant resistance observations, heterologous E.coli experiments,
    auxotroph bypass and methicillin resistance distinct. Do not infer clinical breakpoint
    resistance or universal absence of future resistance.
  - For GSE19400 preserve RN4220,50ng/mL,15min,three treated/three controls; treat
    SaeRS/FapR-linked transcription as downstream response, not direct drug binding.
  - Use write_validated_antibiotic and record_curation_event, preserve historical
    research provenance, and pass focused and required shared gates before independent
    scientific sign-off.
limitations:
- Full main texts for the2009,2012 and2013 resistance studies were read, with2012
  structure/binding figures visually inspected. Supplements and raw assay data were
  not independently reanalysed; publication-internal methodological discrepancies
  remain qualifiers.
- The2013 expression paper was inspected through abstract/introduction/Methods and
  accession metadata;2015 through abstract/introduction/Methods/Table1;2019 introduction
  only for synonym/prodrug identity. Their remaining results are not claimed as reviewed.
- The2012 paper uses freebase and tosylate forms with stated freebase-equivalent concentrations.
  Exact preparation must accompany any future assay entry rather than transferring
  salt mass silently.
- The earlier resistance checkpoint records a different access state and remains historical.
  Newly accessible primary text does not itself resolve every experimental protein
  accession or justify replacing reference strain annotations.
- No current clinical approval or biosynthetic producer search was undertaken because
  neither is asserted. FDA SRS presence and clinical development references alone
  are not approval evidence.
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
