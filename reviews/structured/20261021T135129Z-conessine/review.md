# Conessine: coherent identity and supported antibacterial and antimalarial roles, with assay-specific limits

- Review: 20261021T135129Z-conessine
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T13:38:53Z
- Finished UTC: 2026-10-21T13:51:29Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

No corrective native-record finding was established. The neutral conessine graph and source-grounded synonyms, classes and roles are coherent. Original studies support plant isolation, antibacterial activity and experimental antimalarial activity. A KNApSAcK displayed-key inconsistency is retained as a source-quality limitation because its actual SMILES and InChI both match native. Optional mechanism enrichment must distinguish functional efflux effects from direct binding and preserve assay and material scope. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire native definition, five aliases, two parents, two activity roles, chemical structure/properties, four chemical xrefs, document link, source concept and all four history events. All five adopted citation leads were resolved and assessed at the stated read depth.

Selection: Queue323, exact CHEBI:27965; all thirteen original input hashes preserved.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:27965 | data/antibiotics/antibacterial/conessine.yaml | generated | conessine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:27965 | Zero schema errors. |
| strict | passed | True | CHEBI:27965 | One file; zero strict errors. |
| chemistry | passed | False | CHEBI:27965 | SMILES and InChI agree with full key, neutral charge, formula, masses, eight assigned stereocentres and source mint. |
| external-chemistry | passed | False | CHEBI:27965 | Seven official ChEBI, KEGG, PubChem and KNApSAcK encodings match the native full key; KNApSAcK displayed key discrepancy is separately retained. |
| Authoritative full QC | failed | True | CHEBI:27965 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:27965 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:27965 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:27965 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:27965 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:27965 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:27965 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:27965 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:27965 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact graph, source identifiers and equivalence

identity: supported. Targets: CHEBI:27965.

Native chemical encodings, physical properties, source mint and accessible xref graphs agree. KNApSAcK has a displayed-key metadata conflict despite matching encodings; no native stereoisomer substitution is justified.

### Antibacterial and antimalarial classification

evidence: supported. Targets: CHEBI:27965.

Original studies support the two retained source roles at experimental scope. Neither role establishes approved human treatment, uniform species-wide susceptibility or safety.

### Apocynaceae isolation statement

evidence: supported. Targets: CHEBI:27965.

Original plant-isolation studies support the bounded definition. Extraction is not promoted into a particular biosynthetic pathway or an exact strain producer annotation.

### Optional molecular mechanism follow-up

evidence: unknown. Targets: CHEBI:27965.

Functional efflux evidence is available for optional curation, but no direct MexB binding site or exclusive causal target is demonstrated. Host H3 pharmacology and speculative pore formation are separate claims. The native absence of these optional fields is not a defect.

### Maintained source and adopted citation coverage

provenance: supported. Targets: CHEBI:27965.

All native source-owned fields and history were read and reconcile. Four adopted abstracts were read, two corresponding main articles were inspected, and the 1950 lead remains metadata-only. The additional 2017 primary study was read in full main-text scope.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optionally enrich claim-level activity and functional efflux evidence after resolving source-specific reporting limits.

- Preserve exact strain, medium, exposure, measured endpoint and units. Never transfer extract/fraction MICs to pure conessine or convert µg/disc to µg/mL.
- Distinguish functional efflux modulation from direct MexB binding and retain effects in the deletion strain. Resolve stock-concentration reporting before detailed dose reconstruction.
- Preserve antimalarial strain and vehicle ambiguities and host cytotoxicity. Do not infer clinical approval, a selected bulk salt, or a biosynthetic producer solely from isolation.

### A2

If refreshing the KNApSAcK source, retain its displayed-key inconsistency and verify the underlying graph.

- Compare the official SMILES and InChI as well as the displayed key. Current encodings reproduce native, so do not replace the native graph or xref with a different stereoisomer based only on the printed key.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/conessine.yaml; Entire native YAML. | supports | SEEDED/EXACT/ANTIBACTERIAL, neutral C24H40N2, full key GPLGAQQQNWMVMM-MYAJQUOBSA-N. The definition asserts isolation from Apocynaceae plants, not a particular biosynthetic pathway. No quantitative activity, target, mechanism, resistance, producer annotation, clinical status or causal graph is populated. |
| owners | data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; data/raw/MANIFEST.yaml; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Complete ChEBI row 513 and relevant extraction, role, class, synonym, xref and structure transformations. | supports | The maintained ChEBI row owns all imported native fields and supplies five publication leads. Source names, broader parents, roles, definition and structure reproduce native. No matching ARO, PubChem-enrichment, target, resistance, FDA or MIBiG row occurred in the inspected maintained tables. The source mint reproduces. The filing class preserves the antimalarial role rather than discarding it. |
| identity | https://www.ebi.ac.uk/chebi/backend/api/public/compound/27965/; https://rest.kegg.jp/get/C06545; http://www.knapsackfamily.com/knapsack_core/information.php?word=C00002243; Complete official ChEBI entry, KEGG entry/molfile, and KNApSAcK page with graph encodings. | supports | ChEBI confirms all five native aliases, exact graph, CAS 546-06-5, KEGG C06545, KNApSAcK C00002243 and Reaxys 4702160. Independently parsed ChEBI, KEGG, PubChem and KNApSAcK graphs all yield GPLGAQQQNWMVMM-MYAJQUOBSA-N. KNApSAcK prints GPLGAQQQNWMVMM-CBKQAVQNNA-N, inconsistent with its own standard InChI and SMILES; this does not establish an xref to a different stereoisomer. Reaxys is source-attested without paid inspection. Wikipedia remains a document link. |
| terms | CHEBI:26767; CHEBI:50996; CHEBI:33282; CHEBI:38068; Complete official term definitions and relevant outgoing classifications. | supports | Steroid alkaloid and tertiary amino compound are broader than this graph. Antibacterial-agent and antimalarial are the exact retained source roles. The latter is a role classification, not a populated human clinical-approval assertion. Current ChEBI also carries host H3-antagonist and plant-metabolite context outside the native antimicrobial-role slice. |
| antibacterial-isolation | PMID:20161899; DOI:10.4314/ajtcam.v4i3.31229; https://pmc.ncbi.nlm.nih.gov/articles/PMC2816488/; Entire original main article inspected through web, including Methods and Tables 1–3; original figure images not independently read. | supports | H. floribunda bark, voucher 20147/SFR/CAM, yielded crystallized conessine identified by reported spectroscopy/literature comparison. At 30 µg/disc, inhibition zones were 18, 23, 23 and 24.5 mm for B. cereus F3748, B. subtilis NCTC 3610, B. megaterium 8174 and B. stearothermophilus CNCH 5781. Table 3 MIC/MBC values concern extracts/fractions, not pure conessine. The Discussion proposes pore formation without a conessine-specific membrane experiment. No such mechanism is imported. EuropePMC XML failed and local PMC HTTP returned challenge HTML, but the public web route supplied the full article. |
| antibacterial-abstract | PMID:21834632; DOI:10.1080/14786419.2010.537268; Complete original indexed abstract; publisher full text403. | supports | The study tested methanolic H. pubescens bark extract, fractions and pure conessine by agar diffusion. The reported conessine endpoint against Micrococcus luteus ATCC 9341 is 15.6 µg per disc. That mass-per-disc result must not be normalized into a broth MIC in µg/mL. The abstract also reports marginal antifungal activity; full tables and material characterization were not inspected. |
| antimalarial | PMID:23758861; DOI:10.1186/1475-2875-12-194; PMC3685520; Entire original main XML, Methods, Results, Tables 1–4 and figure caption. | supports | Conessine isolated from H. antidysenterica bark, voucher NIMRHAR-101-HA, showed reported P. falciparum IC50 values 1.9 µg/mL by schizont maturation and 1.3 µg/mL by pLDH; L6 host-cell IC50 was 14 µg/mL. Oral dosing in P. berghei NK65-infected mice reduced parasitaemia, with incomplete survival and biochemical toxicity signals. The Methods heading names K1 but its prose names FSG and GHA strains; vehicle and volume/concentration notation also contain inconsistencies. These are limits on precise enrichment, not proof of clinical efficacy or a molecular parasite target. |
| host-pharmacology | PMID:18683917; DOI:10.1021/jm8003625; Complete original indexed abstract. | context_only | Radioligand screening and affinity results concern rat/human histamine H3 receptors. They are host pharmacology, not an antibacterial target. The cognition experiment concerns optimized analogue 13c, not conessine itself. Neither direct microbial H3 binding nor analogue efficacy is transferred. |
| historical | PMID:15413865; Original bibliographic metadata; no abstract available. | unknown | Leusch, Ann Soc Belg Med Trop 30(1):113–117, 1950, Practical therapeutic experiments with conessine, is resolved as an adopted lead. No original abstract or full text was inspected; no clinical outcome, chemical salt or treatment indication is inferred from its title. |
| efflux | PMID:28806947; DOI:10.1186/s12906-017-1913-y; PMC5557310; Entire original main XML, Methods, Results, Table 1 and all figure captions; fluorescence images not independently reanalyzed. | supports | Sigma conessine in DMSO had reported broth MIC 40 mg/L against P. aeruginosa PAO1 K767, nalB K1455 and ΔmexB K1523. At 20 mg/L it potentiated several antibiotics and increased Hoechst 33342 accumulation; NPN uptake did not increase under the tested conditions. Effects persisted in ΔmexB for most antibiotics, so exclusive MexB dependence is not established. Proposed competitive binding and a MexB pocket location remain hypotheses, not direct binding measurements. The stated 1 mg/L stock conflicts with tested 20–40 mg/L concentrations and is retained as a source-reporting limitation. Bulk salt/purity certification is not supplied. |
| adapter | Structured source applicability assessment; Native record and maintained source rows inspected before web research. | context_only | No native gene, protein, pathway, stress response or transcriptomic dataset is asserted. An iModulonDB cross-check was therefore not applicable to the native claims. New efflux literature is optional mechanistic context, not a silently added native target. |
| search | 323-inclusive-hits.txt; 323-literature.json; Ignored-inclusive local exact-identifier/name/key search and bounded public exact-name/citation research. | context_only | Local results include native/source and generated worklist context. No exact maintained override or curator evidence overlay appeared in the searched scope. Public research resolved all five adopted leads and accessible original studies. Uninspected additional literature remains discovery context; no exhaustive absence claim is made. |
| validation | 323-schema.log;323-strict.log;323-chemistry.json;323-xref-chemistry.json; Actual focused schema, strict and native/external chemical checks. | supports | All focused checks exit 0. All thirteen original source input hashes remain unchanged. Deterministic agreement is not independent experimental stereochemical or purity characterization. |

## Limits And Additional Notes

- Reaxys 4702160 is source-attested but was not inspected through paid access. KNApSAcK prints an InChIKey inconsistent with its own matching standard InChI and SMILES.
- PMID 15413865 remains metadata-only. PMID 21834632 and PMID 18683917 were read at complete indexed-abstract depth; their full original methods were not inspected. The 2012 publisher route returned 403.
- The 2007 full article was read through public web rendering after XML and local HTTP access failed. Its figure images and underlying spectral dataset were not independently examined; plant isolation and named-compound assignment do not by themselves newly establish absolute stereochemistry.
- The 2013 antimalarial paper contains strain-label and dosing/notation inconsistencies. The 2017 paper contains an incompatible stated stock concentration. Both main texts were read; fluorescence or structure figure images and original raw data were not independently reprocessed.
- The literature survey is bounded. Additional computational docking, antiviral, host and ethnopharmacology leads are not treated as primary support for native antimicrobial molecular targets. Optional absent fields do not warrant corrective findings.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T135129Z-conessine
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Conessine: coherent identity and supported antibacterial and antimalarial
  roles, with assay-specific limits'
started_at: '2026-10-21T13:38:53Z'
finished_at: '2026-10-21T13:51:29Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author the native seed. Verified all thirteen initial
    captured hashes before assessment, read the complete native and source row, inspected
    official identities and independently parsed molecular encodings, and read original
    antibacterial and antimalarial studies with explicit access boundaries.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: No corrective native-record finding was established. The neutral conessine
  graph and source-grounded synonyms, classes and roles are coherent. Original studies
  support plant isolation, antibacterial activity and experimental antimalarial activity.
  A KNApSAcK displayed-key inconsistency is retained as a source-quality limitation
  because its actual SMILES and InChI both match native. Optional mechanism enrichment
  must distinguish functional efflux effects from direct binding and preserve assay
  and material scope. Scientific assessment retains the stated evidence limits; full
  verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/conessine.yaml
    sha256: f922743e46cc0abcb00a70c7a7eef3d1003e2e9210092ccdcbfe5bc610c0c7b3
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
- target_id: CHEBI:27965
  path: data/antibiotics/antibacterial/conessine.yaml
  label: conessine
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
  description: Entire native definition, five aliases, two parents, two activity roles,
    chemical structure/properties, four chemical xrefs, document link, source concept
    and all four history events. All five adopted citation leads were resolved and
    assessed at the stated read depth.
  selection: Queue323, exact CHEBI:27965; all thirteen original input hashes preserved.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:27965
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Zero schema errors.
  target_ids:
  - CHEBI:27965
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/conessine.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: One file; zero strict errors.
  target_ids:
  - CHEBI:27965
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/conessine.yaml --out /private/tmp/am-review-session/323-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: SMILES and InChI agree with full key, neutral charge, formula, masses,
    eight assigned stereocentres and source mint.
  target_ids:
  - CHEBI:27965
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 323
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: external-chemistry
  name: external-chemistry
  status: passed
  required: false
  summary: Seven official ChEBI, KEGG, PubChem and KNApSAcK encodings match the native
    full key; KNApSAcK displayed key discrepancy is separately retained.
  target_ids:
  - CHEBI:27965
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/323-xref-check.py
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
  - CHEBI:27965
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
  - CHEBI:27965
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
  - CHEBI:27965
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
  - CHEBI:27965
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
  - CHEBI:27965
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
  - CHEBI:27965
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
  - CHEBI:27965
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
  - CHEBI:27965
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
  - CHEBI:27965
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/conessine.yaml
  locator: Entire native YAML.
  accessed_at: '2026-10-21T13:42:23Z'
  support: supports
  summary: SEEDED/EXACT/ANTIBACTERIAL, neutral C24H40N2, full key GPLGAQQQNWMVMM-MYAJQUOBSA-N.
    The definition asserts isolation from Apocynaceae plants, not a particular biosynthetic
    pathway. No quantitative activity, target, mechanism, resistance, producer annotation,
    clinical status or causal graph is populated.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; conf/sources.yaml; data/raw/MANIFEST.yaml;
    scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  locator: Complete ChEBI row 513 and relevant extraction, role, class, synonym, xref
    and structure transformations.
  accessed_at: '2026-10-21T13:42:23Z'
  support: supports
  summary: The maintained ChEBI row owns all imported native fields and supplies five
    publication leads. Source names, broader parents, roles, definition and structure
    reproduce native. No matching ARO, PubChem-enrichment, target, resistance, FDA
    or MIBiG row occurred in the inspected maintained tables. The source mint reproduces.
    The filing class preserves the antimalarial role rather than discarding it.
  snapshot_sha256: 78cba7612635efe2f40e3d54294d04c4aceab8da3c68bad9d00dace9741bae84
- evidence_id: identity
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/27965/; https://rest.kegg.jp/get/C06545;
    http://www.knapsackfamily.com/knapsack_core/information.php?word=C00002243
  locator: Complete official ChEBI entry, KEGG entry/molfile, and KNApSAcK page with
    graph encodings.
  accessed_at: '2026-10-21T13:42:23Z'
  support: supports
  summary: ChEBI confirms all five native aliases, exact graph, CAS 546-06-5, KEGG
    C06545, KNApSAcK C00002243 and Reaxys 4702160. Independently parsed ChEBI, KEGG,
    PubChem and KNApSAcK graphs all yield GPLGAQQQNWMVMM-MYAJQUOBSA-N. KNApSAcK prints
    GPLGAQQQNWMVMM-CBKQAVQNNA-N, inconsistent with its own standard InChI and SMILES;
    this does not establish an xref to a different stereoisomer. Reaxys is source-attested
    without paid inspection. Wikipedia remains a document link.
  snapshot_sha256: dcc63706ae317e0530ce1682021d17dbfb204cb89ab28a67ce0dff8c444e55fa
- evidence_id: terms
  kind: authority
  reference: CHEBI:26767; CHEBI:50996; CHEBI:33282; CHEBI:38068
  locator: Complete official term definitions and relevant outgoing classifications.
  accessed_at: '2026-10-21T13:39:53Z'
  support: supports
  summary: Steroid alkaloid and tertiary amino compound are broader than this graph.
    Antibacterial-agent and antimalarial are the exact retained source roles. The
    latter is a role classification, not a populated human clinical-approval assertion.
    Current ChEBI also carries host H3-antagonist and plant-metabolite context outside
    the native antimicrobial-role slice.
  snapshot_sha256: 73cfec1682edcf42b19ebd2e050e9613a739d59bfe36f983d440569aa3282c13
- evidence_id: antibacterial-isolation
  kind: primary_source
  reference: PMID:20161899; DOI:10.4314/ajtcam.v4i3.31229; https://pmc.ncbi.nlm.nih.gov/articles/PMC2816488/
  locator: Entire original main article inspected through web, including Methods and
    Tables 1–3; original figure images not independently read.
  accessed_at: '2026-10-21T13:42:23Z'
  support: supports
  summary: H. floribunda bark, voucher 20147/SFR/CAM, yielded crystallized conessine
    identified by reported spectroscopy/literature comparison. At 30 µg/disc, inhibition
    zones were 18, 23, 23 and 24.5 mm for B. cereus F3748, B. subtilis NCTC 3610,
    B. megaterium 8174 and B. stearothermophilus CNCH 5781. Table 3 MIC/MBC values
    concern extracts/fractions, not pure conessine. The Discussion proposes pore formation
    without a conessine-specific membrane experiment. No such mechanism is imported.
    EuropePMC XML failed and local PMC HTTP returned challenge HTML, but the public
    web route supplied the full article.
- evidence_id: antibacterial-abstract
  kind: primary_source
  reference: PMID:21834632; DOI:10.1080/14786419.2010.537268
  locator: Complete original indexed abstract; publisher full text403.
  accessed_at: '2026-10-21T13:39:54Z'
  support: supports
  summary: The study tested methanolic H. pubescens bark extract, fractions and pure
    conessine by agar diffusion. The reported conessine endpoint against Micrococcus
    luteus ATCC 9341 is 15.6 µg per disc. That mass-per-disc result must not be normalized
    into a broth MIC in µg/mL. The abstract also reports marginal antifungal activity;
    full tables and material characterization were not inspected.
  snapshot_sha256: bde6fa5a7c037406a951c36a1bea4a1025e59bdf2622e37ca64fa7cde4f511b4
- evidence_id: antimalarial
  kind: primary_source
  reference: PMID:23758861; DOI:10.1186/1475-2875-12-194; PMC3685520
  locator: Entire original main XML, Methods, Results, Tables 1–4 and figure caption.
  accessed_at: '2026-10-21T13:40:15Z'
  support: supports
  summary: Conessine isolated from H. antidysenterica bark, voucher NIMRHAR-101-HA,
    showed reported P. falciparum IC50 values 1.9 µg/mL by schizont maturation and
    1.3 µg/mL by pLDH; L6 host-cell IC50 was 14 µg/mL. Oral dosing in P. berghei NK65-infected
    mice reduced parasitaemia, with incomplete survival and biochemical toxicity signals.
    The Methods heading names K1 but its prose names FSG and GHA strains; vehicle
    and volume/concentration notation also contain inconsistencies. These are limits
    on precise enrichment, not proof of clinical efficacy or a molecular parasite
    target.
  snapshot_sha256: 3999554f1a331ab73bc217ead3e585e8f392925b113ab5ac54e6250d1ea74d78
- evidence_id: host-pharmacology
  kind: primary_source
  reference: PMID:18683917; DOI:10.1021/jm8003625
  locator: Complete original indexed abstract.
  accessed_at: '2026-10-21T13:39:54Z'
  support: context_only
  summary: Radioligand screening and affinity results concern rat/human histamine
    H3 receptors. They are host pharmacology, not an antibacterial target. The cognition
    experiment concerns optimized analogue 13c, not conessine itself. Neither direct
    microbial H3 binding nor analogue efficacy is transferred.
  snapshot_sha256: bde6fa5a7c037406a951c36a1bea4a1025e59bdf2622e37ca64fa7cde4f511b4
- evidence_id: historical
  kind: database
  reference: PMID:15413865
  locator: Original bibliographic metadata; no abstract available.
  accessed_at: '2026-10-21T13:39:54Z'
  support: unknown
  summary: Leusch, Ann Soc Belg Med Trop 30(1):113–117, 1950, Practical therapeutic
    experiments with conessine, is resolved as an adopted lead. No original abstract
    or full text was inspected; no clinical outcome, chemical salt or treatment indication
    is inferred from its title.
  snapshot_sha256: bde6fa5a7c037406a951c36a1bea4a1025e59bdf2622e37ca64fa7cde4f511b4
- evidence_id: efflux
  kind: primary_source
  reference: PMID:28806947; DOI:10.1186/s12906-017-1913-y; PMC5557310
  locator: Entire original main XML, Methods, Results, Table 1 and all figure captions;
    fluorescence images not independently reanalyzed.
  accessed_at: '2026-10-21T13:40:15Z'
  support: supports
  summary: Sigma conessine in DMSO had reported broth MIC 40 mg/L against P. aeruginosa
    PAO1 K767, nalB K1455 and ΔmexB K1523. At 20 mg/L it potentiated several antibiotics
    and increased Hoechst 33342 accumulation; NPN uptake did not increase under the
    tested conditions. Effects persisted in ΔmexB for most antibiotics, so exclusive
    MexB dependence is not established. Proposed competitive binding and a MexB pocket
    location remain hypotheses, not direct binding measurements. The stated 1 mg/L
    stock conflicts with tested 20–40 mg/L concentrations and is retained as a source-reporting
    limitation. Bulk salt/purity certification is not supplied.
  snapshot_sha256: 6547ffc8c7a900843c49d2a512c2cacad527b89ac85c80caa80bbb44668f10c4
- evidence_id: adapter
  kind: database
  reference: Structured source applicability assessment
  locator: Native record and maintained source rows inspected before web research.
  accessed_at: '2026-10-21T13:42:23Z'
  support: context_only
  summary: No native gene, protein, pathway, stress response or transcriptomic dataset
    is asserted. An iModulonDB cross-check was therefore not applicable to the native
    claims. New efflux literature is optional mechanistic context, not a silently
    added native target.
- evidence_id: search
  kind: search
  reference: 323-inclusive-hits.txt; 323-literature.json
  locator: Ignored-inclusive local exact-identifier/name/key search and bounded public
    exact-name/citation research.
  accessed_at: '2026-10-21T13:42:23Z'
  support: context_only
  summary: Local results include native/source and generated worklist context. No
    exact maintained override or curator evidence overlay appeared in the searched
    scope. Public research resolved all five adopted leads and accessible original
    studies. Uninspected additional literature remains discovery context; no exhaustive
    absence claim is made.
  snapshot_sha256: a83cc3ad5cefcfe85ae954602fd2fff4a2c12b4516660ad00e1d9a8e01172fbd
  search_scope: 2026-10-21; rg --no-ignore --hidden for CHEBI:27965, conessine and
    full key across data, curation, conf, scripts, src, docs, .claude, reviews and
    reports. EuropePMC TITLE_ABS:conessine and exact adopted PMIDs, official entries,
    PMC/publisher free routes.
- evidence_id: validation
  kind: validation
  reference: 323-schema.log;323-strict.log;323-chemistry.json;323-xref-chemistry.json
  locator: Actual focused schema, strict and native/external chemical checks.
  accessed_at: '2026-10-21T13:42:23Z'
  support: supports
  summary: All focused checks exit 0. All thirteen original source input hashes remain
    unchanged. Deterministic agreement is not independent experimental stereochemical
    or purity characterization.
  snapshot_sha256: a7d4011c94bc027090a2560a957edcdd62a14220a78600b7596e364941372cad
assessments:
- assessment_id: identity
  area: identity
  topic: Exact graph, source identifiers and equivalence
  outcome: supported
  summary: Native chemical encodings, physical properties, source mint and accessible
    xref graphs agree. KNApSAcK has a displayed-key metadata conflict despite matching
    encodings; no native stereoisomer substitution is justified.
  target_ids:
  - CHEBI:27965
  evidence_ids:
  - native
  - identity
  - validation
- assessment_id: roles
  area: evidence
  topic: Antibacterial and antimalarial classification
  outcome: supported
  summary: Original studies support the two retained source roles at experimental
    scope. Neither role establishes approved human treatment, uniform species-wide
    susceptibility or safety.
  target_ids:
  - CHEBI:27965
  evidence_ids:
  - terms
  - antibacterial-isolation
  - antibacterial-abstract
  - antimalarial
- assessment_id: plant
  area: evidence
  topic: Apocynaceae isolation statement
  outcome: supported
  summary: Original plant-isolation studies support the bounded definition. Extraction
    is not promoted into a particular biosynthetic pathway or an exact strain producer
    annotation.
  target_ids:
  - CHEBI:27965
  evidence_ids:
  - antibacterial-isolation
  - antimalarial
  - identity
- assessment_id: mechanism
  area: evidence
  topic: Optional molecular mechanism follow-up
  outcome: unknown
  summary: Functional efflux evidence is available for optional curation, but no direct
    MexB binding site or exclusive causal target is demonstrated. Host H3 pharmacology
    and speculative pore formation are separate claims. The native absence of these
    optional fields is not a defect.
  target_ids:
  - CHEBI:27965
  evidence_ids:
  - efflux
  - host-pharmacology
  - antibacterial-isolation
  - adapter
- assessment_id: provenance
  area: provenance
  topic: Maintained source and adopted citation coverage
  outcome: supported
  summary: All native source-owned fields and history were read and reconcile. Four
    adopted abstracts were read, two corresponding main articles were inspected, and
    the 1950 lead remains metadata-only. The additional 2017 primary study was read
    in full main-text scope.
  target_ids:
  - CHEBI:27965
  evidence_ids:
  - owners
  - historical
  - search
  - validation
findings: []
actions:
- action_id: A1
  description: Optionally enrich claim-level activity and functional efflux evidence
    after resolving source-specific reporting limits.
  finding_ids: []
  target_ids:
  - CHEBI:27965
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/conessine.yaml
    role: Curator-owned primary activity and mechanism additions
  acceptance_checks:
  - Preserve exact strain, medium, exposure, measured endpoint and units. Never transfer
    extract/fraction MICs to pure conessine or convert µg/disc to µg/mL.
  - Distinguish functional efflux modulation from direct MexB binding and retain effects
    in the deletion strain. Resolve stock-concentration reporting before detailed
    dose reconstruction.
  - Preserve antimalarial strain and vehicle ambiguities and host cytotoxicity. Do
    not infer clinical approval, a selected bulk salt, or a biosynthetic producer
    solely from isolation.
- action_id: A2
  description: If refreshing the KNApSAcK source, retain its displayed-key inconsistency
    and verify the underlying graph.
  finding_ids: []
  target_ids:
  - CHEBI:27965
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Maintained source xref provenance
  acceptance_checks:
  - Compare the official SMILES and InChI as well as the displayed key. Current encodings
    reproduce native, so do not replace the native graph or xref with a different
    stereoisomer based only on the printed key.
limitations:
- Reaxys 4702160 is source-attested but was not inspected through paid access. KNApSAcK
  prints an InChIKey inconsistent with its own matching standard InChI and SMILES.
- PMID 15413865 remains metadata-only. PMID 21834632 and PMID 18683917 were read at
  complete indexed-abstract depth; their full original methods were not inspected.
  The 2012 publisher route returned 403.
- The 2007 full article was read through public web rendering after XML and local
  HTTP access failed. Its figure images and underlying spectral dataset were not independently
  examined; plant isolation and named-compound assignment do not by themselves newly
  establish absolute stereochemistry.
- The 2013 antimalarial paper contains strain-label and dosing/notation inconsistencies.
  The 2017 paper contains an incompatible stated stock concentration. Both main texts
  were read; fluorescence or structure figure images and original raw data were not
  independently reprocessed.
- The literature survey is bounded. Additional computational docking, antiviral, host
  and ethnopharmacology leads are not treated as primary support for native antimicrobial
  molecular targets. Optional absent fields do not warrant corrective findings.
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
