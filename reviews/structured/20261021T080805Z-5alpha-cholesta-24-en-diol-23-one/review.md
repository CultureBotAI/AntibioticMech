# 5alpha-Cholesta-24-en-3beta,20beta-diol-23-one: stereochemical and source adjudication

- Review: 20261021T080805Z-5alpha-cholesta-24-en-diol-23-one
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T07:57:48Z
- Finished UTC: 2026-10-21T08:08:05Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One major exact-form issue concerns five unspecified stereocenters despite the specific steroid name. Native syntax/formula, generated provenance and broad antibacterial classification are supported. One minor follow-up concerns the exact strain disc assay, conditional on identity adjudication. Primary formula/mass conflicts and absent disc dose are preserved.

## Scope And Provenance

Complete one-record identity, evidence placement and bounded scientific review.

Selection: Queue057; exactly CHEBI:228296 in isolated batch006.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:228296 | data/antibiotics/antibacterial/5α-cholesta-24-en-3β-20β-diol-23-one.yaml | generated | 5α-cholesta-24-en-3β,20β-diol-23-one |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema validation | passed | True | CHEBI:228296 | Actual documented focused validator passed. |
| Focused strict validation | passed | True | CHEBI:228296 | Actual documented focused validator passed. |
| Native structure syntax and formula consistency | passed | True | CHEBI:228296 | Both encodings agree internally, but leave five stereocenters unassigned; scientific exact-form assessment is separate. |
| Structured expression-source applicability | not_applicable | False | CHEBI:228296 | No native gene, protein, regulator, pathway, stress response or transcriptomics dataset is named. The paper alpha-glucosidase assay is separate bioactivity and is not proposed as an antibacterial target. |
| Authoritative full QC | failed | True | CHEBI:228296 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:228296 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:228296 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:228296 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:228296 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:228296 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:228296 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:228296 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:228296 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Named5alpha form versus partial stereo encoding

identity: concern. Targets: CHEBI:228296.

The intended named compound is resolved, but its native structure leaves C5 and four other ring centers unspecified. Current ChEBI preserves that representation; LIPIDMAPS/PubChem provide a narrower full-stereo candidate. Exact equivalence needs curator adjudication.

### Primary formula and stereochemical support

evidence: concern. Targets: CHEBI:228296.

The primary formula/mass statements conflict with named connectivity and current database composition. Native C27H44O3 is chemically consistent with its drawing-derived connectivity; it must not be changed merely to mirror the paper text. Primary Figure1 and assignment evidence require further chemical review.

### Broader classes and antibacterial classification

grounding: supported. Targets: CHEBI:228296.

The four broad classes fit the named functionality and the compound1 assay supports the antibacterial role. The exact stereochemical claim is assessed separately.

### Specific disc-diffusion evidence

completeness: concern. Targets: CHEBI:228296.

A source-specific P. aeruginosa ATCC27853 zone observation can be dispositioned after identity adjudication, retaining missing loading and avoiding MIC conversion.

### Antibacterial mode and molecular target

evidence: unknown. Targets: CHEBI:228296.

No native mechanism is asserted. The inspected antibacterial assay establishes growth-inhibition context, not direct target or a causal lethal pathway. Separate alpha-glucosidase/cytotoxicity experiments cannot fill this gap.

### Whole-animal isolation versus biosynthesis

scope: unknown. Targets: CHEBI:228296.

The paper collection/extraction and supplement establish animal isolation context. They do not distinguish animal biosynthesis from diet or microbiome sources; no forced structured producer is justified.

### Resistance, clinical and dataset fields

scope: not_applicable. Targets: CHEBI:228296.

No native assertions require correction; inspected studies do not establish resistance determinants, current clinical use or exact-compound transcriptomics.

### Maintained source and seed history

provenance: supported. Targets: CHEBI:228296.

Raw ownership, mint and three seed/reseed events agree. The structural issue is upstream-derived; SEEDED remains unchanged.

### Focused validation

schema: supported. Targets: CHEBI:228296.

Native schema and strict gates pass despite the scientific stereo concern.

## Findings

### F1: Reconcile the specific steroid label with five unspecified stereocenters

major / open / confirmed; issue key: chebi-228296-partial-stereo-exact-form-adjudication.

The label asserts5alpha, while native SMILES/InChI leave C5,C8,C9,C14,C17 unassigned and use a different full InChIKey from the fully specified same-name LIPIDMAPS/PubChem entry. This partial representation cannot by itself establish the exact named stereoisomer. Primary structure reporting additionally contains a formula/mass conflict, so the alternative full-stereo structure is a candidate for chemical adjudication, not an automatic replacement.

### F2: Disposition the specific compound1 disc-diffusion observation

minor / open / confirmed; issue key: chebi-228296-disc-assay-disposition.

The inspected primary paper supplies a strain-resolved zone observation that can support a bounded activity annotation once compound identity is adjudicated. It has no stated disc loading and cannot be converted to MIC, susceptibility category, target mechanism or evidence for the companion compound.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate the original steroid structure and reconcile label, source identity and full stereochemical encoding through maintained ownership.

- Inspect original Figure1 and the actual stereochemical assignments, retain the C27H46O3/418 versus named/database C27H44O3/416 conflict, and document which aspects remain unresolved.
- For each C5,C8,C9,C14,C17 position, either substantiate a specific configuration or explicitly preserve uncertainty and reconcile the exact-label/grounding claim; do not fill wedges by steroid-family convention alone.
- If adopting a corrected structure, regenerate SMILES, Standard InChI, complete InChIKey, formula and masses together and compare the candidateJLSGWGFUNKKVBT-YJPGMPNYSA-N at full-stereo level.
- Correct the maintained source/transform and rerun the native seeder and required schema, strict, grounding, reference and history gates. Preserve status/history and avoid one-off generated YAML edits.

### A2

After structure adjudication, curate or explicitly defer the reported compound1 activity with its assay limitations.

- Map the observation to compound1 and P. aeruginosa ATCC27853 separately from species grounding NCBITaxon287; retain21.0±0.06mm as a reported inhibition-zone endpoint.
- Preserve6mm disc,TSA,37C,24h,triplicate and unspecified dose; do not infer MIC, concentration, breakpoint, resistance or potency equivalence.
- Keep separate alpha-glucosidase/cancer-cell/animal-lethality bioactivities out of antibacterial target claims.
- Use claim-level primary evidence, validated writer and curation history, followed by required focused/shared gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/5α-cholesta-24-en-3β-20β-diol-23-one.yaml; Entire native record | supports | Read the ANTIBACTERIAL, SEEDED, EXACT record, label, partly unspecified systematic synonym, four parents, role, complete structure, ChEBI concept and all three seed/reseed events. No definition, external xref, target, mechanism, structured producer, quantitative activity, resistance, clinical, dataset or causal graph assertion is present. |
| owner | data/raw/chebi_antimicrobials.tsv; Row2899 CHEBI228296; PATHS.tsv row538; MANIFEST, conf/sources.yaml, extractor and seeder | supports | Raw and native identity fields agree, with PMID34969331 as the adopted primary lead. The source date2026-08-30 and minted suffixf5a257d63e reproduce. Native structure/synonym issues are inherited from ChEBI and must be fixed through maintained source/transform ownership, not a one-off generated edit. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:228296; Official visible structure, synonym, parents, roles and species-of-metabolite fields | supports | Current ChEBI reproduces native C27H44O3, charge0, masses416.646/416.32905, keyJLSGWGFUNKKVBT-FMDNSJKISA-N and partly specified stereochemistry. Its label expressly says5alpha, while its InChI contains five unknown tetrahedral entries. Whole-body Acanthaster planci provenance cites PMID34969331. Other ChEBI roles include alpha-glucosidase inhibition and animal/marine metabolite, which are not antibacterial mechanisms. |
| parent-131619 | https://www.ebi.ac.uk/chebi/CHEBI:131619; Official parent definition | supports | The parent resolves to C27-steroid and is a broader structural class appropriate to the named connectivity. It does not resolve the stereochemical ambiguity or supply a molecular mechanism. |
| parent-228297 | https://www.ebi.ac.uk/chebi/CHEBI:228297; Official parent definition | supports | The parent resolves to 23-oxo steroid and is a broader structural class appropriate to the named connectivity. It does not resolve the stereochemical ambiguity or supply a molecular mechanism. |
| parent-36836 | https://www.ebi.ac.uk/chebi/CHEBI:36836; Official parent definition | supports | The parent resolves to 3beta-hydroxy steroid and is a broader structural class appropriate to the named connectivity. It does not resolve the stereochemical ambiguity or supply a molecular mechanism. |
| parent-36854 | https://www.ebi.ac.uk/chebi/CHEBI:36854; Official parent definition | supports | The parent resolves to 20-hydroxy steroid and is a broader structural class appropriate to the named connectivity. It does not resolve the stereochemical ambiguity or supply a molecular mechanism. |
| chemistry | RDKit independent native structure calculation; Both native encodings; batch006 locked environment | supports | Both native encodings parse and reproduce the full native key, formula, charge, masses and one fragment. Nine potential tetrahedral centers are detected; only four are assigned. The correct source mint is reproduced. Passing syntax and formula checks do not establish one exact stereoisomer. |
| stereo | Independent atom mapping and source comparison; Native SMILES atom indices mapped to steroid positions; full PubChem structure compared with chirality enabled | refutes | Native C5,C8,C9,C14,C17 are unassigned. The live PubChem/LIPIDMAPS structure defines all nine centers and has keyJLSGWGFUNKKVBT-YJPGMPNYSA-N. It matches the native partial structure with existing chirality respected, but has a different complete stereochemical key. At minimum the named5alpha configuration is not encoded natively; the other center assignments require source adjudication. |
| lipidmaps | https://www.lipidmaps.org/databases/lmsd/LMST01010485?LMID=LMST01010485; Curated exact-name entry, strings and primary citation | supports | LIPIDMAPS supplies C27H44O3 and a fully specified Standard InChI/keyYJPGMPNYSA-N for the same name and cites PMID34969331. This is a useful competing structural representation, not sufficient permission to overwrite the ChEBI record without checking the primary structural evidence. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/170325908; Official PUG View structure fields; LIPIDMAPS deposit SID528408100 inspected separately | supports | PubChem agrees with the fully specified LIPIDMAPS stereoisomer and formula. It is additional identity evidence, not an existing native xref or independent antibacterial experiment. CID and SID are kept distinct. |
| abstract | PMID:34969331; DOI10.1080/14786419.2021.2021200; primary abstract via Europe PMC | supports | The primary abstract maps this named steroid to compound1 and supports antibacterial activity against P. aeruginosa. The second steroid is compound2 and differs in connectivity and oxygen count. |
| primary-structure | DOI:10.1080/14786419.2021.2021200; Author-posted full text, section2.1, manuscript pp3-4; ResearchGate publication357467477 | context_only | Primary text assigns compound1 using spectral comparisons/NOESY, but states C27H46O3 and mass418.6380, conflicting with the named keto-alkene connectivity and database C27H44O3. It also names C21 in a stereochemistry sentence. These discrepancies require adjudication; this review does not independently re-elucidate the isolated molecule or declare an erratum. |
| primary-assay | DOI:10.1080/14786419.2021.2021200; Author-posted full text sections2.2,3.4,3.6 and4; manuscript pp4-7 | supports | Compound1 gives21.0±0.06mm against P. aeruginosa ATCC27853 in disc diffusion:6mm discs,TSA,37C,24h,triplicate. Disc dose is unspecified. This is neither MIC nor a clinical breakpoint. Alpha-glucosidase inhibition is a separate assay without an established antibacterial causal link; cancer-cell and brine-shrimp findings likewise do not establish antibacterial mechanism. |
| supplement | https://ndownloader.figshare.com/files/32411196; Official gnpl_a_2021200_sm9989.docx; FigureS1 andS9 visually inspected; TableS1 text read | supports | FigureS1 traces chromatographic fraction10 to3.4mg compound1 and fraction11 to7.8mg compound2. S9 labels a mass peak418, preserving the primary formula/mass conflict. TableS1 and spectral pages provide structural characterization context but were not independently re-elucidated. No antibacterial dose table is supplied in the inspected supplement. |
| taxon | https://www.atcc.org/products/27853; Official ATCC identity; NCBI species page https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=287&amp;mode=Info | supports | ATCC27853 resolves to P. aeruginosa strain Boston41501. NCBITaxon287 is the species;286 is the broader Pseudomonas genus and must not be substituted. The assay applies to the paper strain, not all members of the species. |
| search | CultureBotAI/AntibioticMech; Ignored-inclusive native/owner references and bounded free source discovery | context_only | Exact native/raw/PATHS references agree. No specific curator override was found in the inspected maintained surfaces. The primary author-posted text and official supplement were read; broad steroid reviews were discovery leads only. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Identity, primary evidence, activity and mechanism rules | supports | Exact-form groundings must not collapse unspecified stereochemistry into a specific isomer. Preserve source conflicts, disk diffusion endpoint and loading limits. Optional empty fields alone are not defects; collection from a whole animal is not proof of its biosynthetic role. |
| validation | just validate; just validate-strict; Actual batch006 focused runs;057-validation.tsv | supports | Both commands exited0: LinkML no issues and strict one file with zero ERROR rows. |

## Limits And Additional Notes

- The original primary Figure1 pixels were unavailable; author-posted full article text and official structural supplement were inspected. This review does not independently re-elucidate NMR spectra or select an authoritative corrected stereoisomer.
- Primary compound1 formula/mass text and supplementary418 peak conflict with the named keto-alkene/database C27H44O3 structure. The conflict is retained and is not used to overwrite the internally consistent native formula.
- Disc loading is unspecified. Zone measurements do not establish MIC, clinical susceptibility or molecular mechanism.
- Whole-animal isolation is not proof of animal-specific biosynthesis. Additional exact-compound literature may exist beyond the bounded search.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All20 original/expanded input hashes and Git base were rechecked unchanged; capture preceded judgment.
- Current ChEBI carries the same partial stereochemistry, so a future fix belongs in maintained source/transform ownership.
- No native content, scientific status or curation history was changed.
- Coordinator independently parsed both native structures and confirmed the reported count of unassigned tetrahedral centers; the existing InChI explicitly retains those unknown configurations. No full-stereo replacement was inferred from the missing assignments.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T080805Z-5alpha-cholesta-24-en-diol-23-one
kind: record
repository: CultureBotAI/AntibioticMech
title: '5alpha-Cholesta-24-en-3beta,20beta-diol-23-one: stereochemical and source
  adjudication'
started_at: '2026-10-21T07:57:48Z'
finished_at: '2026-10-21T08:08:05Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Reviewer independently read the complete seed, current authorities,
    author-posted primary text and official structural supplement; did not create
    the seed.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: One major exact-form issue concerns five unspecified stereocenters despite
  the specific steroid name. Native syntax/formula, generated provenance and broad
  antibacterial classification are supported. One minor follow-up concerns the exact
  strain disc assay, conditional on identity adjudication. Primary formula/mass conflicts
  and absent disc dose are preserved.
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
  - path: data/antibiotics/antibacterial/5α-cholesta-24-en-3β-20β-diol-23-one.yaml
    sha256: 929bc029ffafacb40df6536a3b86a1a979da914e2c299ada905b8271c335c778
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
  - path: CLAUDE.md
    sha256: 36fb92f8919481cfbf3f17ddde4a1e244c81f76c64396dbbac910c4815fb9f16
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: data/antibiotics/PATHS.tsv
    sha256: 3b1d82d007878e4aca2c28f4001a468776b325b726da2e48abb76a3dc551cc38
    role: context
targets:
- target_id: CHEBI:228296
  path: data/antibiotics/antibacterial/5α-cholesta-24-en-3β-20β-diol-23-one.yaml
  label: 5α-cholesta-24-en-3β,20β-diol-23-one
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
  description: Complete one-record identity, evidence placement and bounded scientific
    review.
  selection: Queue057; exactly CHEBI:228296 in isolated batch006.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:228296
  exclusions:
  - target: Companion compound2, other steroids and whole starfish extracts
    reason: Boundary context only; identities, assays and mechanisms are not transferred.
checks:
- check_id: schema
  name: Focused schema validation
  status: passed
  required: true
  summary: Actual documented focused validator passed.
  target_ids:
  - CHEBI:228296
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/5α-cholesta-24-en-3β-20β-diol-23-one.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Focused strict validation
  status: passed
  required: true
  summary: Actual documented focused validator passed.
  target_ids:
  - CHEBI:228296
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/5α-cholesta-24-en-3β-20β-diol-23-one.yaml --out
    /private/tmp/am-review-session/057-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Native structure syntax and formula consistency
  status: passed
  required: true
  summary: Both encodings agree internally, but leave five stereocenters unassigned;
    scientific exact-form assessment is separate.
  target_ids:
  - CHEBI:228296
  evidence_ids:
  - chemistry
  - stereo
- check_id: structured-adapter
  name: Structured expression-source applicability
  status: not_applicable
  required: false
  summary: No native gene, protein, regulator, pathway, stress response or transcriptomics
    dataset is named. The paper alpha-glucosidase assay is separate bioactivity and
    is not proposed as an antibacterial target.
  target_ids:
  - CHEBI:228296
  evidence_ids:
  - record
  - primary-assay
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:228296
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
  - CHEBI:228296
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
  - CHEBI:228296
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
  - CHEBI:228296
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
  - CHEBI:228296
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
  - CHEBI:228296
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
  - CHEBI:228296
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
  - CHEBI:228296
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
  - CHEBI:228296
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/5α-cholesta-24-en-3β-20β-diol-23-one.yaml
  locator: Entire native record
  accessed_at: '2026-10-21T08:02:01Z'
  support: supports
  summary: Read the ANTIBACTERIAL, SEEDED, EXACT record, label, partly unspecified
    systematic synonym, four parents, role, complete structure, ChEBI concept and
    all three seed/reseed events. No definition, external xref, target, mechanism,
    structured producer, quantitative activity, resistance, clinical, dataset or causal
    graph assertion is present.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Row2899 CHEBI228296; PATHS.tsv row538; MANIFEST, conf/sources.yaml, extractor
    and seeder
  accessed_at: '2026-10-21T08:02:01Z'
  support: supports
  summary: Raw and native identity fields agree, with PMID34969331 as the adopted
    primary lead. The source date2026-08-30 and minted suffixf5a257d63e reproduce.
    Native structure/synonym issues are inherited from ChEBI and must be fixed through
    maintained source/transform ownership, not a one-off generated edit.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:228296
  locator: Official visible structure, synonym, parents, roles and species-of-metabolite
    fields
  accessed_at: '2026-10-21T07:58:20Z'
  support: supports
  summary: Current ChEBI reproduces native C27H44O3, charge0, masses416.646/416.32905,
    keyJLSGWGFUNKKVBT-FMDNSJKISA-N and partly specified stereochemistry. Its label
    expressly says5alpha, while its InChI contains five unknown tetrahedral entries.
    Whole-body Acanthaster planci provenance cites PMID34969331. Other ChEBI roles
    include alpha-glucosidase inhibition and animal/marine metabolite, which are not
    antibacterial mechanisms.
  snapshot_sha256: f784262aff19368082bf4f2a43b38bff68eab5d4b97d6aa86d20578d2d72a83c
- evidence_id: parent-131619
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:131619
  locator: Official parent definition
  accessed_at: '2026-10-21T07:58:30Z'
  support: supports
  summary: The parent resolves to C27-steroid and is a broader structural class appropriate
    to the named connectivity. It does not resolve the stereochemical ambiguity or
    supply a molecular mechanism.
  snapshot_sha256: d107365fd523e53bd51acce5e5681dc47a7f4b33c99032c24f32c6a15d1be7a7
- evidence_id: parent-228297
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:228297
  locator: Official parent definition
  accessed_at: '2026-10-21T07:58:31Z'
  support: supports
  summary: The parent resolves to 23-oxo steroid and is a broader structural class
    appropriate to the named connectivity. It does not resolve the stereochemical
    ambiguity or supply a molecular mechanism.
  snapshot_sha256: 8cc8e7f246ea81f6f51fc5927b408222973c77939114041a9d87742dbdb27069
- evidence_id: parent-36836
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:36836
  locator: Official parent definition
  accessed_at: '2026-10-21T07:58:33Z'
  support: supports
  summary: The parent resolves to 3beta-hydroxy steroid and is a broader structural
    class appropriate to the named connectivity. It does not resolve the stereochemical
    ambiguity or supply a molecular mechanism.
  snapshot_sha256: 434601e8f2e93c358791c365990c0c9f40d965be0c0fdf91b50f4bfbcff0ad68
- evidence_id: parent-36854
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:36854
  locator: Official parent definition
  accessed_at: '2026-10-21T07:58:35Z'
  support: supports
  summary: The parent resolves to 20-hydroxy steroid and is a broader structural class
    appropriate to the named connectivity. It does not resolve the stereochemical
    ambiguity or supply a molecular mechanism.
  snapshot_sha256: 9a0ba880ad0445d734cf2ed0f227aed7e8fa46818b4fcfa6ee438e633b47ff4e
- evidence_id: chemistry
  kind: validation
  reference: RDKit independent native structure calculation
  locator: Both native encodings; batch006 locked environment
  accessed_at: '2026-10-21T07:58:17Z'
  support: supports
  summary: Both native encodings parse and reproduce the full native key, formula,
    charge, masses and one fragment. Nine potential tetrahedral centers are detected;
    only four are assigned. The correct source mint is reproduced. Passing syntax
    and formula checks do not establish one exact stereoisomer.
  snapshot_sha256: 8bf0334c77b7c1435d33909f381cef05ee101eb7a0ee6b36e65527452f19650e
- evidence_id: stereo
  kind: validation
  reference: Independent atom mapping and source comparison
  locator: Native SMILES atom indices mapped to steroid positions; full PubChem structure
    compared with chirality enabled
  accessed_at: '2026-10-21T08:00:02Z'
  support: refutes
  summary: Native C5,C8,C9,C14,C17 are unassigned. The live PubChem/LIPIDMAPS structure
    defines all nine centers and has keyJLSGWGFUNKKVBT-YJPGMPNYSA-N. It matches the
    native partial structure with existing chirality respected, but has a different
    complete stereochemical key. At minimum the named5alpha configuration is not encoded
    natively; the other center assignments require source adjudication.
  snapshot_sha256: 81fef19a1b6b790eda85ab94dcb76c5304a4dc7a6a76064845a3d918ffa9db19
- evidence_id: lipidmaps
  kind: database
  reference: https://www.lipidmaps.org/databases/lmsd/LMST01010485?LMID=LMST01010485
  locator: Curated exact-name entry, strings and primary citation
  accessed_at: '2026-10-21T07:58:48Z'
  support: supports
  summary: LIPIDMAPS supplies C27H44O3 and a fully specified Standard InChI/keyYJPGMPNYSA-N
    for the same name and cites PMID34969331. This is a useful competing structural
    representation, not sufficient permission to overwrite the ChEBI record without
    checking the primary structural evidence.
  snapshot_sha256: 1431eb0153d104a3f6c4e0b3f115f7935e47fb6a00a6a7dc1b8e888116a18d1b
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/170325908
  locator: Official PUG View structure fields; LIPIDMAPS deposit SID528408100 inspected
    separately
  accessed_at: '2026-10-21T07:58:46Z'
  support: supports
  summary: PubChem agrees with the fully specified LIPIDMAPS stereoisomer and formula.
    It is additional identity evidence, not an existing native xref or independent
    antibacterial experiment. CID and SID are kept distinct.
  snapshot_sha256: 537f82378f5f3a0b2f03c0430924b69768b0125a1ddc8fed007d2a0cf33be8e6
- evidence_id: abstract
  kind: primary_source
  reference: PMID:34969331
  locator: DOI10.1080/14786419.2021.2021200; primary abstract via Europe PMC
  accessed_at: '2026-10-21T07:58:21Z'
  support: supports
  summary: The primary abstract maps this named steroid to compound1 and supports
    antibacterial activity against P. aeruginosa. The second steroid is compound2
    and differs in connectivity and oxygen count.
  snapshot_sha256: f838ffea476ddd710b8f9a94d9c4e59de306f003ff383bc155eabffba80485ab
- evidence_id: primary-structure
  kind: primary_source
  reference: DOI:10.1080/14786419.2021.2021200
  locator: Author-posted full text, section2.1, manuscript pp3-4; ResearchGate publication357467477
  accessed_at: '2026-10-21T07:59:19Z'
  support: context_only
  summary: Primary text assigns compound1 using spectral comparisons/NOESY, but states
    C27H46O3 and mass418.6380, conflicting with the named keto-alkene connectivity
    and database C27H44O3. It also names C21 in a stereochemistry sentence. These
    discrepancies require adjudication; this review does not independently re-elucidate
    the isolated molecule or declare an erratum.
  snapshot_sha256: bdc05cbf57870933bb12a772ac44be2824a8619f08ccbea6feb8272e94e85203
- evidence_id: primary-assay
  kind: primary_source
  reference: DOI:10.1080/14786419.2021.2021200
  locator: Author-posted full text sections2.2,3.4,3.6 and4; manuscript pp4-7
  accessed_at: '2026-10-21T08:00:30Z'
  support: supports
  summary: Compound1 gives21.0±0.06mm against P. aeruginosa ATCC27853 in disc diffusion:6mm
    discs,TSA,37C,24h,triplicate. Disc dose is unspecified. This is neither MIC nor
    a clinical breakpoint. Alpha-glucosidase inhibition is a separate assay without
    an established antibacterial causal link; cancer-cell and brine-shrimp findings
    likewise do not establish antibacterial mechanism.
  snapshot_sha256: ea95c0fdcf211c1240318824a5305b7f227a5a9755ce5a85ab7a486dee98ccde
- evidence_id: supplement
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/32411196
  locator: Official gnpl_a_2021200_sm9989.docx; FigureS1 andS9 visually inspected;
    TableS1 text read
  accessed_at: '2026-10-21T07:59:19Z'
  support: supports
  summary: FigureS1 traces chromatographic fraction10 to3.4mg compound1 and fraction11
    to7.8mg compound2. S9 labels a mass peak418, preserving the primary formula/mass
    conflict. TableS1 and spectral pages provide structural characterization context
    but were not independently re-elucidated. No antibacterial dose table is supplied
    in the inspected supplement.
  snapshot_sha256: f02b76de913df298a5af8f465e2447c4bf5dbe9e0dc5afbb38838861fb51cf52
- evidence_id: taxon
  kind: authority
  reference: https://www.atcc.org/products/27853
  locator: Official ATCC identity; NCBI species page https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=287&mode=Info
  accessed_at: '2026-10-21T08:02:01Z'
  support: supports
  summary: ATCC27853 resolves to P. aeruginosa strain Boston41501. NCBITaxon287 is
    the species;286 is the broader Pseudomonas genus and must not be substituted.
    The assay applies to the paper strain, not all members of the species.
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: Ignored-inclusive native/owner references and bounded free source discovery
  accessed_at: '2026-10-21T08:02:01Z'
  support: context_only
  summary: Exact native/raw/PATHS references agree. No specific curator override was
    found in the inspected maintained surfaces. The primary author-posted text and
    official supplement were read; broad steroid reviews were discovery leads only.
  search_scope: prepare.py57 used rg --no-ignore --hidden across batch006 excluding
    .git/.venv. Follow-up ignored-inclusive searches covered raw, curation, conf,
    reviews, reports and PATHS for228296, exact label, full key and minted suffix.
    Free searches used the exact steroid name, PMID34969331, full article title and
    DOI. PubMed/EPMC, author-posted ResearchGate text, official T&F Figshare supplement,
    ChEBI, LIPIDMAPS and PubChem were inspected; direct RG raw download returned403
    and Figure1 pixels remained unavailable.
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Identity, primary evidence, activity and mechanism rules
  accessed_at: '2026-10-21T08:02:01Z'
  support: supports
  summary: Exact-form groundings must not collapse unspecified stereochemistry into
    a specific isomer. Preserve source conflicts, disk diffusion endpoint and loading
    limits. Optional empty fields alone are not defects; collection from a whole animal
    is not proof of its biosynthetic role.
- evidence_id: validation
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual batch006 focused runs;057-validation.tsv
  accessed_at: '2026-10-21T07:58:27Z'
  support: supports
  summary: 'Both commands exited0: LinkML no issues and strict one file with zero
    ERROR rows.'
  snapshot_sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
assessments:
- assessment_id: identity
  area: identity
  topic: Named5alpha form versus partial stereo encoding
  outcome: concern
  summary: The intended named compound is resolved, but its native structure leaves
    C5 and four other ring centers unspecified. Current ChEBI preserves that representation;
    LIPIDMAPS/PubChem provide a narrower full-stereo candidate. Exact equivalence
    needs curator adjudication.
  target_ids:
  - CHEBI:228296
  evidence_ids:
  - record
  - chebi
  - chemistry
  - stereo
  - lipidmaps
  - pubchem
- assessment_id: primary-identity
  area: evidence
  topic: Primary formula and stereochemical support
  outcome: concern
  summary: The primary formula/mass statements conflict with named connectivity and
    current database composition. Native C27H44O3 is chemically consistent with its
    drawing-derived connectivity; it must not be changed merely to mirror the paper
    text. Primary Figure1 and assignment evidence require further chemical review.
  target_ids:
  - CHEBI:228296
  evidence_ids:
  - primary-structure
  - supplement
  - chemistry
  - lipidmaps
- assessment_id: grounding
  area: grounding
  topic: Broader classes and antibacterial classification
  outcome: supported
  summary: The four broad classes fit the named functionality and the compound1 assay
    supports the antibacterial role. The exact stereochemical claim is assessed separately.
  target_ids:
  - CHEBI:228296
  evidence_ids:
  - parent-131619
  - parent-228297
  - parent-36836
  - parent-36854
  - abstract
  - primary-assay
- assessment_id: activity
  area: completeness
  topic: Specific disc-diffusion evidence
  outcome: concern
  summary: A source-specific P. aeruginosa ATCC27853 zone observation can be dispositioned
    after identity adjudication, retaining missing loading and avoiding MIC conversion.
  target_ids:
  - CHEBI:228296
  evidence_ids:
  - primary-assay
  - taxon
  - rubric
- assessment_id: mechanism
  area: evidence
  topic: Antibacterial mode and molecular target
  outcome: unknown
  summary: No native mechanism is asserted. The inspected antibacterial assay establishes
    growth-inhibition context, not direct target or a causal lethal pathway. Separate
    alpha-glucosidase/cytotoxicity experiments cannot fill this gap.
  target_ids:
  - CHEBI:228296
  evidence_ids:
  - record
  - primary-assay
- assessment_id: producer
  area: scope
  topic: Whole-animal isolation versus biosynthesis
  outcome: unknown
  summary: The paper collection/extraction and supplement establish animal isolation
    context. They do not distinguish animal biosynthesis from diet or microbiome sources;
    no forced structured producer is justified.
  target_ids:
  - CHEBI:228296
  evidence_ids:
  - primary-assay
  - supplement
  - chebi
  - rubric
- assessment_id: other
  area: scope
  topic: Resistance, clinical and dataset fields
  outcome: not_applicable
  summary: No native assertions require correction; inspected studies do not establish
    resistance determinants, current clinical use or exact-compound transcriptomics.
  target_ids:
  - CHEBI:228296
  evidence_ids:
  - record
  - primary-assay
- assessment_id: provenance
  area: provenance
  topic: Maintained source and seed history
  outcome: supported
  summary: Raw ownership, mint and three seed/reseed events agree. The structural
    issue is upstream-derived; SEEDED remains unchanged.
  target_ids:
  - CHEBI:228296
  evidence_ids:
  - record
  - owner
  - chemistry
- assessment_id: schema
  area: schema
  topic: Focused validation
  outcome: supported
  summary: Native schema and strict gates pass despite the scientific stereo concern.
  target_ids:
  - CHEBI:228296
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: chebi-228296-partial-stereo-exact-form-adjudication
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile the specific steroid label with five unspecified stereocenters
  description: The label asserts5alpha, while native SMILES/InChI leave C5,C8,C9,C14,C17
    unassigned and use a different full InChIKey from the fully specified same-name
    LIPIDMAPS/PubChem entry. This partial representation cannot by itself establish
    the exact named stereoisomer. Primary structure reporting additionally contains
    a formula/mass conflict, so the alternative full-stereo structure is a candidate
    for chemical adjudication, not an automatic replacement.
  target_ids:
  - CHEBI:228296
  field_paths:
  - label
  - synonyms[0]
  - grounding_status
  - chemical_structure.smiles
  - chemical_structure.standard_inchi
  - chemical_structure.standard_inchi_key
  evidence_ids:
  - record
  - chebi
  - stereo
  - lipidmaps
  - pubchem
  - primary-structure
  - supplement
  - rubric
  rule_id: native-review-checklist:Identity
  native_severity: major exact-form representation gap
  normalization_reason: Intended compound and connectivity are resolved, so this is
    not a wrong-compound blocker. However five unassigned centers, including explicitly
    namedC5, materially weaken exact-form identity and require maintained source adjudication.
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
- finding_id: F2
  issue_key: chebi-228296-disc-assay-disposition
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Disposition the specific compound1 disc-diffusion observation
  description: The inspected primary paper supplies a strain-resolved zone observation
    that can support a bounded activity annotation once compound identity is adjudicated.
    It has no stated disc loading and cannot be converted to MIC, susceptibility category,
    target mechanism or evidence for the companion compound.
  target_ids:
  - CHEBI:228296
  field_paths:
  - activity_spectrum
  evidence_ids:
  - primary-assay
  - taxon
  - rubric
  rule_id: native-review-checklist:Activity
  native_severity: minor specific assay evidence opportunity
  normalization_reason: Current broad classification is supported; this is a concrete
    primary result opportunity, not an error caused solely by an optional empty field.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/5α-cholesta-24-en-3β-20β-diol-23-one.yaml
    role: Curator-owned scientific annotations through validated writer and history
actions:
- action_id: A1
  description: Adjudicate the original steroid structure and reconcile label, source
    identity and full stereochemical encoding through maintained ownership.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:228296
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
  generator: scripts/extract_source_inventory.py and scripts/seed_from_sources.py
  acceptance_checks:
  - Inspect original Figure1 and the actual stereochemical assignments, retain the
    C27H46O3/418 versus named/database C27H44O3/416 conflict, and document which aspects
    remain unresolved.
  - For each C5,C8,C9,C14,C17 position, either substantiate a specific configuration
    or explicitly preserve uncertainty and reconcile the exact-label/grounding claim;
    do not fill wedges by steroid-family convention alone.
  - If adopting a corrected structure, regenerate SMILES, Standard InChI, complete
    InChIKey, formula and masses together and compare the candidateJLSGWGFUNKKVBT-YJPGMPNYSA-N
    at full-stereo level.
  - Correct the maintained source/transform and rerun the native seeder and required
    schema, strict, grounding, reference and history gates. Preserve status/history
    and avoid one-off generated YAML edits.
- action_id: A2
  description: After structure adjudication, curate or explicitly defer the reported
    compound1 activity with its assay limitations.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:228296
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/5α-cholesta-24-en-3β-20β-diol-23-one.yaml
    role: Curator-owned scientific annotations through validated writer and history
  depends_on:
  - A1
  acceptance_checks:
  - Map the observation to compound1 and P. aeruginosa ATCC27853 separately from species
    grounding NCBITaxon287; retain21.0±0.06mm as a reported inhibition-zone endpoint.
  - Preserve6mm disc,TSA,37C,24h,triplicate and unspecified dose; do not infer MIC,
    concentration, breakpoint, resistance or potency equivalence.
  - Keep separate alpha-glucosidase/cancer-cell/animal-lethality bioactivities out
    of antibacterial target claims.
  - Use claim-level primary evidence, validated writer and curation history, followed
    by required focused/shared gates.
limitations:
- The original primary Figure1 pixels were unavailable; author-posted full article
  text and official structural supplement were inspected. This review does not independently
  re-elucidate NMR spectra or select an authoritative corrected stereoisomer.
- Primary compound1 formula/mass text and supplementary418 peak conflict with the
  named keto-alkene/database C27H44O3 structure. The conflict is retained and is not
  used to overwrite the internally consistent native formula.
- Disc loading is unspecified. Zone measurements do not establish MIC, clinical susceptibility
  or molecular mechanism.
- Whole-animal isolation is not proof of animal-specific biosynthesis. Additional
  exact-compound literature may exist beyond the bounded search.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All20 original/expanded input hashes and Git base were rechecked unchanged; capture
  preceded judgment.
- Current ChEBI carries the same partial stereochemistry, so a future fix belongs
  in maintained source/transform ownership.
- No native content, scientific status or curation history was changed.
- Coordinator independently parsed both native structures and confirmed the reported
  count of unassigned tetrahedral centers; the existing InChI explicitly retains those
  unknown configurations. No full-stereo replacement was inferred from the missing
  assignments.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:228296
- https://doi.org/10.1080/14786419.2021.2021200
- https://doi.org/10.6084/m9.figshare.17708220.v1
- https://www.lipidmaps.org/databases/lmsd/LMST01010485
tags:
- antibacterial
- steroid
- stereochemistry
- source-conflict
- seeded
```
