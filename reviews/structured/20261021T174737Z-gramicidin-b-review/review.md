# Gramicidin B: coherent Val-B identity and qualified membrane evidence

- Review: 20261021T174737Z-gramicidin-b-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T17:27:43Z
- Finished UTC: 2026-10-21T17:47:37Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The record coherently denotes neutral valine-gramicidin B, a 15-residue peptide with Phe at position 11. Current PubChem agrees, and original model-membrane experiments support the bounded ion-channel and lipid-assembly statements. No confirmed required correction was identified. The imported target remains explicitly database-only; exact-B antibacterial assay details are less fully resolved than its biophysical identity. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Assigned queue position 508; exactly one native record reviewed independently.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-f2b46f8b0e | data/antibiotics/antibacterial/gramicidin-b.yaml | generated | gramicidin B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-f2b46f8b0e | Actual focused execution exited 0. Executed in /private/tmp/antibioticmech-record-reviews-051; chemistry uses the existing019 RDKit environment. |
| Focused schema verification | passed | True | antibioticmech:aro-f2b46f8b0e | Actual focused execution exited 0. Executed in /private/tmp/antibioticmech-record-reviews-051; chemistry uses the existing019 RDKit environment. |
| Focused strict verification | passed | True | antibioticmech:aro-f2b46f8b0e | Actual focused execution exited 0. Executed in /private/tmp/antibioticmech-record-reviews-051; chemistry uses the existing019 RDKit environment. |
| Authoritative full QC | failed | True | antibioticmech:aro-f2b46f8b0e | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-f2b46f8b0e | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-f2b46f8b0e | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-f2b46f8b0e | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-f2b46f8b0e | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-f2b46f8b0e | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-f2b46f8b0e | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-f2b46f8b0e | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-f2b46f8b0e | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact sequence, termini, stereochemistry and concept boundary

identity: supported. Targets: antibioticmech:aro-f2b46f8b0e.

Neutral Val-B matches current CID 25244501. Explicit graph tracing gives the A sequence with only L-Phe at 11 replacing L-Trp, consistent with original 1976/1987 source descriptions and adopted review; no Ile1 structure is inferred.

### Internal chemical representation and numerical precision

consistency: supported. Targets: antibioticmech:aro-f2b46f8b0e.

SMILES and Standard InChI produce the stored key, elemental composition, neutral charge and exact mass. All source-concept mints reproduce. Average masses agree within the precision of the adopted PubChem values; deterministic consistency does not prove natural-product or mixture identity.

### Exact xrefs and strictly broader parent

grounding: supported. Targets: antibioticmech:aro-f2b46f8b0e.

ARO:3009657 is a broader nonribosomal-peptide class, and the minted source identifier is reproducible. The asserted PubChem chemical xref matches the exact Val peptide.

### Definition citation and membrane target provenance

evidence: supported. Targets: antibioticmech:aro-f2b46f8b0e.

All adopted definition leads and current target-term citation leads were disposed at their actual reading depth. The ATTACKED_COMPONENT/MEMBRANE target correctly retains DATABASE_ASSERTION_ONLY, unspecified organism/strain/assay and database notes. Original model-membrane work is compatible with the broad relationship, without promoting it to primary binding evidence.

### Antibacterial filing, optional observations and quantitative scope

completeness: unknown. Targets: antibioticmech:aro-f2b46f8b0e.

The antibiotic identity and model-membrane activity are supported. The inspected 1967 B-enriched fraction assay is not an exact purified Val-B MIC, and original 1965 full structure/assay pages were inaccessible. No numerical whole-cell value is proposed and no required-schema defect follows from absent optional observations.

### Reproducibility, history and required versus optional claims

ownership: supported. Targets: antibioticmech:aro-f2b46f8b0e.

All native fields and history were read. The record is seeded, not curator-reviewed. The actual source and generator owners are captured; future changes must use maintained inputs and validated regeneration. No resistance, producer, clinical-product, dataset or causal-graph claim is silently invented from literature.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optional future enrichment: attach original model-membrane evidence with explicit material and assay scope.

- Retrieve the full1976/1987 methods before attaching numerical channel or lipid measurements; keep the Val/Ile form explicit.
- Retain database qualification until primary evidence is placed on a separate supported claim. Do not import A, D-mixture or S MICs into B. Any native annotation requires the separate validated-writer/history workflow.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/gramicidin-b.yaml; Entire native YAML, including all source concepts, evidence qualifiers, discussions and history | supports | Full exact record read. Identifier antibioticmech:aro-f2b46f8b0e, source ARO:3000223, MINTED and SEEDED. The stored chemistry, asserted xrefs and all 4 seed/reseed history events were examined. One imported membrane attacked-component assertion explicitly states DATABASE_ASSERTION_ONLY, unspecified organism/strain/assay and database rather than primary evidence. |
| owners | data/raw/aro_antibiotics.tsv#ARO:3000223; Exact raw ARO, PubChem, target, resistance, decisions, curator and readiness row projection in 508-source-rows.json | context_only | Actual maintained source rows and applicable extractor, PubChem enrichment, seeder and evidence-qualification owners were inspected. Original 13 input hashes were preserved and expanded to 29 before detailed judgment; no exact curator override or exclusion was found in the ignored-inclusive target search. |
| aro | https://purl.obolibrary.org/obo/aro.obo; Current ARO:3000223, ARO:3009657 and, where applicable, ARO:3000710; 426-current-aro.obo / 426-fetch2-results.json | supports | Official current OBO preserves the native compound concept and nonribosomal-peptide class. The membrane relationship is an ontology assertion, not a strain-specific primary experiment. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/25244501/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON; Current CID25244501 property response | supports | The official structure response agrees with the stored formula, charge and exact InChIKey. This confirms faithful fallback copying; it does not independently establish that the source CID denotes the named natural product or mixture. |
| chemistry | /private/tmp/am-review-session/507510-residue-map.py; 019 RDKit interpreter, cwd051; 508-chemistry.json and residue-map entry508 | supports | Independent SMILES/InChI chemistry, mint calculation and directed peptide-backbone tracing. 15 residues; linear backbone with N-formyl and C-terminal ethanolamide groups. Sequence and alpha-carbon indices/CIP assignments are retained explicitly in the diagnostic JSON; no native graph was changed. |
| review2007 | PMID:17572379; DOI10.1016/j.bbamem.2007.05.011; author PDF pp2012–2013,2016,2018 and linked references | supports | Adopted source is a secondary review. Inspected text identifies A/B/C as 15-residue linear peptides, Trp/Phe/Tyr at 11, Val1/Ile1 subforms, approximately 85%A in the described mixture, head-to-head channel dimers and a specifically LPC-model bilayer-induction comparison. It points to original 1976 channel and 1987 lipid experiments; it is not relabeled primary evidence. |
| primary1976 | PMID:55275; DOI10.1016/0005-2736(76)90348-5; original abstract in EPMC metadata | supports | Original abstract reports measurements of natural and synthetic A/B/C single-channel conductance and lifetime. A/B differ by the Trp-to-Phe substitution; conductance distributions and ratios depend on glycerylmonooleate versus phosphatidylcholine/phosphatidylethanolamine model membranes. It does not supply bacterial MICs or direct antimicrobial protein binding. |
| primary1987 | PMID:2440475; DOI10.1016/0005-2736(87)90118-0; original abstract in EPMC metadata | supports | Original abstract explicitly maps A/B/C to Trp/Phe/Tyr11. DSC, 31P-NMR and small-angle X-ray experiments used defined phospholipid systems; bilayer/HII induction followed natural mixture approximately A greater than B approximately C. This supports a bounded lipid-assembly comparison, not a general bacterial potency ranking. |
| adapter | /private/tmp/am-review-session/507510-adapter-scope.json; Pre-web record-specific applicability review and structured iModulonDB catalog hash | context_only | The full native records name no gene, protein, locus, regulator or expression pathway requiring a covered-dataset query. The membrane component and nonribosomal-peptide structural class are not expression-module claims. No missing-module inference is made. |
| target-bibliography | ARO:3000710; All current membrane-term reference leads: PMID20818945,17572379,8528769,4334683 | context_only | 20818945 is a colistin clinical review;8528769 is a defensin review;17572379 is the gramicidin channel review;4334683 metadata identify polymyxin B and gramicidin S, with no abstract. These broad ontology references do not establish an exact linear-gramicidin strain-specific experiment. Native evidence_status and notes already disclose database-only status, so no new unsupported-primary finding is inferred. |
| primary1967 | PMID:5299675; Original Bull WHO36:447–456; actual scanned pp447–448 and453–455, Fig1/Table6–7; selected text/figures | supports | The study established an A/B/C-containing gramicidin preparation separately from gramicidin S. The measured reference batch contained about 50% A,7% B,25% C; counter-current fractions were biologically compared, with the B-enriched fraction less potent in that assay. This is batch/fraction evidence, not a purified exact-congener MIC. Historical use of a minor component called D on p448 differs from modern mixture nomenclature. |
| primary1998 | PMID:9788907; DOI10.1016/S0006-3495(98)77656-8; original abstract; full main inaccessible in attempted endpoints | supports | Original abstract expressly calls gramicidin D a heterogeneous six-component mixture and reports solvent-dependent heterodimeric crystal structures. Crystal conformation and minor-component effects are not whole-cell assay results or a single exact identity for D. |

## Limits And Additional Notes

- Required shared full-corpus checks are incorporated separately by the root reviewer before finalization; actual focused gates are recorded here.
- The adopted 2007 source is a secondary review; its relevant full text and cited original 1976/1987 abstracts were inspected. Original 1965 sequence studies were not read in full; attempted B/C ACS pages returned 403. Their titles alone were not used as structural proof. The 1976/1987 full methods were not retrieved.
- Multiple EPMC fullTextXML requests returned 500; PMC PDF endpoints sometimes returned HTTP 200 browser-challenge HTML rather than PDFs. These are access failures, retained in fetch manifests. The 1998 original was read at abstract depth only.
- No exact purified Val-B bacterial MIC, complete primary 1965 structure proof, or strain-specific membrane experiment was established in this bounded reading. That limitation does not show absence of activity or invalidate the correctly qualified CARD relationship.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All 13 original input hashes and the expanded 29 inputs were rechecked unchanged before draft writing. No native record/source, history, progress file or saved review bundle was edited.
- The four neighbouring gramicidin records are reviewed separately; shared source retrieval does not collapse exact-component and mixture identities.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T174737Z-gramicidin-b-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Gramicidin B: coherent Val-B identity and qualified membrane evidence'
started_at: '2026-10-21T17:27:43Z'
finished_at: '2026-10-21T17:47:37Z'
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
summary: The record coherently denotes neutral valine-gramicidin B, a 15-residue peptide
  with Phe at position 11. Current PubChem agrees, and original model-membrane experiments
  support the bounded ion-channel and lipid-assembly statements. No confirmed required
  correction was identified. The imported target remains explicitly database-only;
  exact-B antibacterial assay details are less fully resolved than its biophysical
  identity. Scientific assessment retains the stated evidence limits; full verification
  is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/gramicidin-b.yaml
    sha256: 575e96e642ca513d7c9e0ccc67b85d3c91f4875e7751d53aa8e06c4a2ac1f3d1
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
  - path: CLAUDE.md
    sha256: 36fb92f8919481cfbf3f17ddde4a1e244c81f76c64396dbbac910c4815fb9f16
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
    role: context
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
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
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: scripts/card_evidence_reviews.py
    sha256: f9ec8aff30066bf04b9c2757af7d6f5d179d045e57b9f3b352bbed0b851f50a8
    role: context
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
targets:
- target_id: antibioticmech:aro-f2b46f8b0e
  path: data/antibiotics/antibacterial/gramicidin-b.yaml
  label: gramicidin B
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO definition, exact xrefs and bibliography
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: PubChem fallback structure
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem fallback retrieval
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding/exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Imported membrane target assertion
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Target relation mapping
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Database evidence qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Qualification transform
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Assigned queue position 508; exactly one native record reviewed independently.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-f2b46f8b0e
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0. Executed in /private/tmp/antibioticmech-record-reviews-051;
    chemistry uses the existing019 RDKit environment.
  target_ids:
  - antibioticmech:aro-f2b46f8b0e
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    508
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Executed in /private/tmp/antibioticmech-record-reviews-051;
    chemistry uses the existing019 RDKit environment.
  target_ids:
  - antibioticmech:aro-f2b46f8b0e
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/gramicidin-b.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Executed in /private/tmp/antibioticmech-record-reviews-051;
    chemistry uses the existing019 RDKit environment.
  target_ids:
  - antibioticmech:aro-f2b46f8b0e
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/gramicidin-b.yaml --out /private/tmp/am-review-session/508-strict.tsv
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
  - antibioticmech:aro-f2b46f8b0e
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
  - antibioticmech:aro-f2b46f8b0e
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
  - antibioticmech:aro-f2b46f8b0e
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
  - antibioticmech:aro-f2b46f8b0e
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
  - antibioticmech:aro-f2b46f8b0e
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
  - antibioticmech:aro-f2b46f8b0e
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
  - antibioticmech:aro-f2b46f8b0e
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
  - antibioticmech:aro-f2b46f8b0e
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
  - antibioticmech:aro-f2b46f8b0e
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/gramicidin-b.yaml
  locator: Entire native YAML, including all source concepts, evidence qualifiers,
    discussions and history
  accessed_at: '2026-10-21T17:45:00Z'
  support: supports
  summary: Full exact record read. Identifier antibioticmech:aro-f2b46f8b0e, source
    ARO:3000223, MINTED and SEEDED. The stored chemistry, asserted xrefs and all 4
    seed/reseed history events were examined. One imported membrane attacked-component
    assertion explicitly states DATABASE_ASSERTION_ONLY, unspecified organism/strain/assay
    and database rather than primary evidence.
  snapshot_sha256: 575e96e642ca513d7c9e0ccc67b85d3c91f4875e7751d53aa8e06c4a2ac1f3d1
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv#ARO:3000223
  locator: Exact raw ARO, PubChem, target, resistance, decisions, curator and readiness
    row projection in 508-source-rows.json
  accessed_at: '2026-10-21T17:45:00Z'
  support: context_only
  summary: Actual maintained source rows and applicable extractor, PubChem enrichment,
    seeder and evidence-qualification owners were inspected. Original 13 input hashes
    were preserved and expanded to 29 before detailed judgment; no exact curator override
    or exclusion was found in the ignored-inclusive target search.
  snapshot_sha256: 837ccccb908e631f1def36c074aab6861091da86b8095539707433e9d6b89c1b
  search_scope: 'Initial 508-local-hits.txt plus 507510-context-search.txt: identifier,
    label, slug and ARO concept searched with hidden/ignored files included in the
    isolated051 worktree; exact maintained source rows projected separately.'
- evidence_id: aro
  kind: database
  reference: https://purl.obolibrary.org/obo/aro.obo
  locator: Current ARO:3000223, ARO:3009657 and, where applicable, ARO:3000710; 426-current-aro.obo
    / 426-fetch2-results.json
  accessed_at: '2026-10-21T15:57:42Z'
  support: supports
  summary: Official current OBO preserves the native compound concept and nonribosomal-peptide
    class. The membrane relationship is an ontology assertion, not a strain-specific
    primary experiment.
  snapshot_sha256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/25244501/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass,Charge/JSON
  locator: Current CID25244501 property response
  accessed_at: '2026-10-21T17:37:11.742283Z'
  support: supports
  summary: The official structure response agrees with the stored formula, charge
    and exact InChIKey. This confirms faithful fallback copying; it does not independently
    establish that the source CID denotes the named natural product or mixture.
  snapshot_sha256: 393cf0c8ec1eea95b957516448d6dbb493c64daa68d5bf36109f87f9c6dca2e5
- evidence_id: chemistry
  kind: validation
  reference: /private/tmp/am-review-session/507510-residue-map.py
  locator: 019 RDKit interpreter, cwd051; 508-chemistry.json and residue-map entry508
  accessed_at: '2026-10-21T17:45:00Z'
  support: supports
  summary: Independent SMILES/InChI chemistry, mint calculation and directed peptide-backbone
    tracing. 15 residues; linear backbone with N-formyl and C-terminal ethanolamide
    groups. Sequence and alpha-carbon indices/CIP assignments are retained explicitly
    in the diagnostic JSON; no native graph was changed.
  snapshot_sha256: 469f91f67471d49bac54dcb2e3ffd52f55ea1af9711d368a0279db9d1f6951fa
- evidence_id: review2007
  kind: database
  reference: PMID:17572379
  locator: DOI10.1016/j.bbamem.2007.05.011; author PDF pp2012–2013,2016,2018 and linked
    references
  accessed_at: '2026-10-21T17:41:46.055917Z'
  support: supports
  summary: Adopted source is a secondary review. Inspected text identifies A/B/C as
    15-residue linear peptides, Trp/Phe/Tyr at 11, Val1/Ile1 subforms, approximately
    85%A in the described mixture, head-to-head channel dimers and a specifically
    LPC-model bilayer-induction comparison. It points to original 1976 channel and
    1987 lipid experiments; it is not relabeled primary evidence.
  snapshot_sha256: a9276bf160777f2696fb6cec8ed994743ab310e328c857f84974d01b8a9379f9
- evidence_id: primary1976
  kind: primary_source
  reference: PMID:55275
  locator: DOI10.1016/0005-2736(76)90348-5; original abstract in EPMC metadata
  accessed_at: '2026-10-21T17:39:29.629447Z'
  support: supports
  summary: Original abstract reports measurements of natural and synthetic A/B/C single-channel
    conductance and lifetime. A/B differ by the Trp-to-Phe substitution; conductance
    distributions and ratios depend on glycerylmonooleate versus phosphatidylcholine/phosphatidylethanolamine
    model membranes. It does not supply bacterial MICs or direct antimicrobial protein
    binding.
  snapshot_sha256: d16614a3792fb151ba0fe93b956b5f7c96dfd76d575a068f36675b92af69d26d
- evidence_id: primary1987
  kind: primary_source
  reference: PMID:2440475
  locator: DOI10.1016/0005-2736(87)90118-0; original abstract in EPMC metadata
  accessed_at: '2026-10-21T17:39:29.629207Z'
  support: supports
  summary: Original abstract explicitly maps A/B/C to Trp/Phe/Tyr11. DSC, 31P-NMR
    and small-angle X-ray experiments used defined phospholipid systems; bilayer/HII
    induction followed natural mixture approximately A greater than B approximately
    C. This supports a bounded lipid-assembly comparison, not a general bacterial
    potency ranking.
  snapshot_sha256: aa935161dbdd016776a56a2fb3c1b4837b5f651b4bb850f9e3bf48efc9396aea
- evidence_id: adapter
  kind: search
  reference: /private/tmp/am-review-session/507510-adapter-scope.json
  locator: Pre-web record-specific applicability review and structured iModulonDB
    catalog hash
  accessed_at: '2026-10-21T17:45:00Z'
  support: context_only
  summary: The full native records name no gene, protein, locus, regulator or expression
    pathway requiring a covered-dataset query. The membrane component and nonribosomal-peptide
    structural class are not expression-module claims. No missing-module inference
    is made.
  snapshot_sha256: b770463630c1ca2dca45ad28e6d2f120195e3dba6e9cd215c9b74cde35900620
  search_scope: Before open web follow-up, the complete native record was checked
    for genes, proteins, loci, regulators and named pathways against the available
    iModulonDB catalog; none of those native query types is present. Only a generic
    membrane component and a chemical structural class are named.
- evidence_id: target-bibliography
  kind: database
  reference: ARO:3000710
  locator: 'All current membrane-term reference leads: PMID20818945,17572379,8528769,4334683'
  accessed_at: '2026-10-21T17:39:29.629207Z'
  support: context_only
  summary: 20818945 is a colistin clinical review;8528769 is a defensin review;17572379
    is the gramicidin channel review;4334683 metadata identify polymyxin B and gramicidin
    S, with no abstract. These broad ontology references do not establish an exact
    linear-gramicidin strain-specific experiment. Native evidence_status and notes
    already disclose database-only status, so no new unsupported-primary finding is
    inferred.
  snapshot_sha256: aa935161dbdd016776a56a2fb3c1b4837b5f651b4bb850f9e3bf48efc9396aea
- evidence_id: primary1967
  kind: primary_source
  reference: PMID:5299675
  locator: Original Bull WHO36:447–456; actual scanned pp447–448 and453–455, Fig1/Table6–7;
    selected text/figures
  accessed_at: '2026-10-21T17:40:14.741405Z'
  support: supports
  summary: The study established an A/B/C-containing gramicidin preparation separately
    from gramicidin S. The measured reference batch contained about 50% A,7% B,25%
    C; counter-current fractions were biologically compared, with the B-enriched fraction
    less potent in that assay. This is batch/fraction evidence, not a purified exact-congener
    MIC. Historical use of a minor component called D on p448 differs from modern
    mixture nomenclature.
  snapshot_sha256: 3a689bc0f7ecfa2fb9712ebaf9a3dc04b2a4a90922e6e3c15858d68b2dd70d16
- evidence_id: primary1998
  kind: primary_source
  reference: PMID:9788907
  locator: DOI10.1016/S0006-3495(98)77656-8; original abstract; full main inaccessible
    in attempted endpoints
  accessed_at: '2026-10-21T17:39:29.629207Z'
  support: supports
  summary: Original abstract expressly calls gramicidin D a heterogeneous six-component
    mixture and reports solvent-dependent heterodimeric crystal structures. Crystal
    conformation and minor-component effects are not whole-cell assay results or a
    single exact identity for D.
  snapshot_sha256: aa935161dbdd016776a56a2fb3c1b4837b5f651b4bb850f9e3bf48efc9396aea
assessments:
- assessment_id: identity
  area: identity
  topic: Exact sequence, termini, stereochemistry and concept boundary
  outcome: supported
  summary: Neutral Val-B matches current CID 25244501. Explicit graph tracing gives
    the A sequence with only L-Phe at 11 replacing L-Trp, consistent with original
    1976/1987 source descriptions and adopted review; no Ile1 structure is inferred.
  target_ids:
  - antibioticmech:aro-f2b46f8b0e
  evidence_ids:
  - native
  - pubchem
  - aro
  - chemistry
  - primary1976
  - primary1987
- assessment_id: structure
  area: consistency
  topic: Internal chemical representation and numerical precision
  outcome: supported
  summary: SMILES and Standard InChI produce the stored key, elemental composition,
    neutral charge and exact mass. All source-concept mints reproduce. Average masses
    agree within the precision of the adopted PubChem values; deterministic consistency
    does not prove natural-product or mixture identity.
  target_ids:
  - antibioticmech:aro-f2b46f8b0e
  evidence_ids:
  - native
  - pubchem
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Exact xrefs and strictly broader parent
  outcome: supported
  summary: ARO:3009657 is a broader nonribosomal-peptide class, and the minted source
    identifier is reproducible. The asserted PubChem chemical xref matches the exact
    Val peptide.
  target_ids:
  - antibioticmech:aro-f2b46f8b0e
  evidence_ids:
  - aro
  - pubchem
  - chemistry
  - native
- assessment_id: evidence
  area: evidence
  topic: Definition citation and membrane target provenance
  outcome: supported
  summary: All adopted definition leads and current target-term citation leads were
    disposed at their actual reading depth. The ATTACKED_COMPONENT/MEMBRANE target
    correctly retains DATABASE_ASSERTION_ONLY, unspecified organism/strain/assay and
    database notes. Original model-membrane work is compatible with the broad relationship,
    without promoting it to primary binding evidence.
  target_ids:
  - antibioticmech:aro-f2b46f8b0e
  evidence_ids:
  - native
  - review2007
  - primary1976
  - primary1987
  - target-bibliography
- assessment_id: activity
  area: completeness
  topic: Antibacterial filing, optional observations and quantitative scope
  outcome: unknown
  summary: The antibiotic identity and model-membrane activity are supported. The
    inspected 1967 B-enriched fraction assay is not an exact purified Val-B MIC, and
    original 1965 full structure/assay pages were inaccessible. No numerical whole-cell
    value is proposed and no required-schema defect follows from absent optional observations.
  target_ids:
  - antibioticmech:aro-f2b46f8b0e
  evidence_ids:
  - native
  - primary1976
  - primary1987
  - primary1967
- assessment_id: ownership
  area: ownership
  topic: Reproducibility, history and required versus optional claims
  outcome: supported
  summary: All native fields and history were read. The record is seeded, not curator-reviewed.
    The actual source and generator owners are captured; future changes must use maintained
    inputs and validated regeneration. No resistance, producer, clinical-product,
    dataset or causal-graph claim is silently invented from literature.
  target_ids:
  - antibioticmech:aro-f2b46f8b0e
  evidence_ids:
  - native
  - owners
  - adapter
findings: []
actions:
- action_id: A1
  description: 'Optional future enrichment: attach original model-membrane evidence
    with explicit material and assay scope.'
  finding_ids: []
  target_ids:
  - antibioticmech:aro-f2b46f8b0e
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Imported membrane target assertion
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Database evidence qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Qualification transform
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/gramicidin-b.yaml
    role: Future curator-owned literature target/activity annotation
  acceptance_checks:
  - Retrieve the full1976/1987 methods before attaching numerical channel or lipid
    measurements; keep the Val/Ile form explicit.
  - Retain database qualification until primary evidence is placed on a separate supported
    claim. Do not import A, D-mixture or S MICs into B. Any native annotation requires
    the separate validated-writer/history workflow.
  generator: scripts/seed_from_sources.py
limitations:
- Required shared full-corpus checks are incorporated separately by the root reviewer
  before finalization; actual focused gates are recorded here.
- The adopted 2007 source is a secondary review; its relevant full text and cited
  original 1976/1987 abstracts were inspected. Original 1965 sequence studies were
  not read in full; attempted B/C ACS pages returned 403. Their titles alone were
  not used as structural proof. The 1976/1987 full methods were not retrieved.
- Multiple EPMC fullTextXML requests returned 500; PMC PDF endpoints sometimes returned
  HTTP 200 browser-challenge HTML rather than PDFs. These are access failures, retained
  in fetch manifests. The 1998 original was read at abstract depth only.
- No exact purified Val-B bacterial MIC, complete primary 1965 structure proof, or
  strain-specific membrane experiment was established in this bounded reading. That
  limitation does not show absence of activity or invalidate the correctly qualified
  CARD relationship.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All 13 original input hashes and the expanded 29 inputs were rechecked unchanged
  before draft writing. No native record/source, history, progress file or saved review
  bundle was edited.
- The four neighbouring gramicidin records are reviewed separately; shared source
  retrieval does not collapse exact-component and mixture identities.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
