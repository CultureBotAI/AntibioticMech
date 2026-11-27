# Review of cervimycin A

- Review: 20261021T123501Z-cervimycin-a-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:20:03Z
- Finished UTC: 2026-10-21T12:35:01Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Cervimycin A is coherently represented by the native structure and current PubChem and ChEBI, with matching formula, charge, key and 21 configured centers. The cited 2022 source supports the generic polyketide-family definition, but its new experiments concern C/D. Original A–D discovery evidence supports antibacterial context at abstract depth; its full body was not obtained. Later C-specific mechanism results and an unresolved MIBiG producer candidate were not transferred to A. No confirmed native finding is raised, and no scientific status or native data was changed. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire SEEDED, MINTED cervimycin A record: generic definition and cited PMID, ARO structural class, exact PubChem-derived structure, three cross-references, source concept and three history events.

Selection: Queue 274; 13 original input hashes retained and five actual source/producer owner inputs appended, giving 18 unchanged hashes.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-da12e2d9fe | data/antibiotics/antibacterial/cervimycin-a.yaml | generated | cervimycin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema validation | passed | True | antibioticmech:aro-da12e2d9fe | Exit 0; no issues found. |
| Documented strict validation | passed | True | antibioticmech:aro-da12e2d9fe | Exit 0; zero ERROR rows. |
| Supplemental exact structure comparison | passed | False | antibioticmech:aro-da12e2d9fe | Exit 0; native and current chemical authority structures agree. Separate tautomer enumeration emitted transform-limit warnings, retained as a limitation. |
| Supplemental source and preserved-hash reconciliation | passed | False | antibioticmech:aro-da12e2d9fe | Exit 0; 18 hashes, exact adopted definition/structure and the native PMID disposition checked. |
| Structured protein/pathway adapter applicability | not_applicable | False | antibioticmech:aro-da12e2d9fe | The native record names no gene, protein, pathway, regulator, stress response or transcriptomics dataset. C/D protein leads were inspected to prevent congener transfer; no A protein or pathway claim was proposed. |
| Authoritative full QC | failed | True | antibioticmech:aro-da12e2d9fe | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-da12e2d9fe | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-da12e2d9fe | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-da12e2d9fe | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-da12e2d9fe | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-da12e2d9fe | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-da12e2d9fe | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-da12e2d9fe | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-da12e2d9fe | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact A identity and machine representation

identity: supported. Targets: antibioticmech:aro-da12e2d9fe.

Native structure and current exact PubChem/ChEBI representations agree; A is distinguished from adjacent congeners.

### Original stereochemical assignment depth

identity: unknown. Targets: antibioticmech:aro-da12e2d9fe.

The full original A–D NMR/chemical-degradation body was not obtained, so all 21 configured centers were not independently reassigned from primary data.

### Polyketide antibacterial class

grounding: supported. Targets: antibioticmech:aro-da12e2d9fe.

Structural authority and the original discovery abstract support polyketide antibiotic identity and antibacterial context.

### Scope of the adopted PMID

evidence: supported. Targets: antibioticmech:aro-da12e2d9fe.

The cited primary Introduction supports the generic family definition. The record does not incorrectly import its C/D experiments.

### Exact A mechanism

evidence: unknown. Targets: antibioticmech:aro-da12e2d9fe.

No directly verified A molecular mechanism was established in the inspected sources; C/D evidence remains excluded from A claims.

### Producer and biosynthetic context

completeness: unknown. Targets: antibioticmech:aro-da12e2d9fe.

An existing candidate requires exact-identity normalization, taxon/strain reconciliation and primary source checking; automatic publication would be premature.

### Native sources and history

provenance: supported. Targets: antibioticmech:aro-da12e2d9fe.

The definition, structure and three history events are coherent with adopted owners; all 18 hashes are preserved.

### Optional enrichment

completeness: supported. Targets: antibioticmech:aro-da12e2d9fe.

The sparse SEEDED record contains no unsupported mechanistic, quantitative, producer or clinical assertions. Optional enrichment should await exact A evidence.

### Focused validity

schema: supported. Targets: antibioticmech:aro-da12e2d9fe.

Documented schema and strict checks and supplemental identity checks pass.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/cervimycin-a.yaml; Entire native YAML and all three source history events | supports | The ARO-minted identifier denotes cervimycin A, not the family as a whole. The exact structure and label distinguish A despite the broad family definition. There are no native target, resistance, MIC, producer, clinical-product, synonym or causal-graph assertions. MINTED is retained transparently; no unsupported REVIEWED status is present. |
| chemistry | PubChem:11557219; CHEBI:209712; ARO:3007601; 274-chemistry.py/.json; native SMILES/InChI, current PubChem structure, current ChEBI SMILES and molfile | supports | All five native/current-authority representations reproduce DTTQURMKQUWCNN-ZVSUTAIVSA-N, C62H82O25, net charge 0 and 21 configured stereocenters, with masses matching native precision. The native graph has the acetyl substituent and terminal dimethylmalonyl ester that distinguish A from the carbamoyl or monomethyl congeners. This computational agreement does not independently reproduce the original NMR assignment of every center. |
| grounding | CHEBI:209712; ARO:3007601; ARO:3005171; 274-chebi.json, 274-ols.json and 274-aro-stanzas.txt | supports | Current ChEBI 209712 resolves exactly to Cervimycin A with the same structure and two-star status; its parents are anthraquinone and glycoside and it has no activity roles in the inspected response. ARO 3007601 resolves to the named antibiotic and supplies the native PubChem/ChEBI links. ARO 3005171 is the stated polyketide-with-antibiotic-activity class. The existence of a ChEBI xref does not alone prove that the native minted identifier should be replaced without a maintained grounding decision. |
| definition | PMID:36173303; DOI:10.1128/spectrum.02567-22; 274-2022.xml/.txt: complete abstract, Introduction, relevant Results/Tables 1 and 5 and mutant-construction methods | partial | The sole adopted PMID resolves. Its Introduction describes the cervimycin A–D antibiotic complex as glycosylated polyketides, supporting the native generic definition. Its newly measured susceptibility and resistance experiments use C and D, with S. aureus SG511 serial selection and allele/knockout comparisons. Those experiments support C/D resistance contexts, not a direct A target or exact A MIC. No C/D table values were promoted to this record. |
| discovery | PMID:15940739; DOI:10.1002/chem.200500320; 274-core.json complete original abstract; public Wiley abstract and graphical-caption page, volume 11 pages 5523–5530 | partial | The original paper explicitly identifies cervimycins A–D, describes structure elucidation by NMR and chemical degradation, and reports antibacterial activity against resistant staphylococci and enterococci from a cave-derived Streptomyces tendae strain. Its abstract distinguishes acetyl/carbamoyl and methylmalonyl/dimethylmalonyl congeners. The full-text link redirected to the abstract; direct body and attempted supplementary retrieval returned 403. Therefore exact A assay rows, concentrations, purity, organism strains and original stereochemical assignment details remain unverified. |
| congener-scope | PMID:38722162; DOI:10.1128/msphere.00764-23; PMID:21077936; DOI:10.1111/j.1574-6968.2010.02143.x; 274-2024.xml/.txt: Introduction, selected Results/Discussion, susceptibility and microscopy methods; complete 2010 abstract in 274-core.json | context_only | The 2024 experiments specifically use cervimycin C. Gyrase supercoiling inhibition appears at high concentrations, whereas lower-dose cellular and omics results indicate a more complicated protein-stress response. Its Introduction cites an earlier A DNA-incorporation result at high concentration, which is historical context rather than a new A gyrase-binding experiment. The 2010 bmrA promoter/mRNA resistance study also tests C. Neither supports importing a Clp, WalK, BmrA, gyrase or ribosome mechanism into the native A record. |
| producer | MIBiG:BGC0001439; PMID:15326518; DOI:10.1039/B409221J; 274-mibig_producers.json adopted version-5 row; 274-chemistry.json separate candidate comparison; original complete 2004 abstract | unknown | The existing MIBiG A row is marked questionable, not expert-reviewed, and names Streptomyces sp. CS113 with a first-legacy-reference citation to a cervimycin C biosynthesis paper. Its RDNLQESQZXBNSG-ZVSUTAIVSA-N key differs from the native DTTQURMKQUWCNN-ZVSUTAIVSA-N in a keto/enol encoding. Supplemental stereo-preserving tautomer canonicalization yielded identical canonical SMILES for both, but hit transform limits and is not permission to bypass the strict exact-key producer join. The relationship between CS113 and original S. tendae HKI0179 was not established. No producer is published in the native record; this unresolved candidate is not a demonstrated omission defect. |
| additional-leads | PMID:15326518; PMID:22179067; PMID:33999625; 274-core.json complete abstracts; 274-lead-dispositions.json | context_only | The 2004 study concerns C biosynthesis and feeding; the 2012 study concerns CerJ biosynthetic ester formation and modified cervimycin variants; the 2021 study synthesizes a K tetrasaccharide fragment as a cyclohexyl glycoside. These are not exact A antibacterial-target experiments. The discovery query also returned ester-cleavage patent leads; none is a native reference or was used to support a finding. |
| owners | data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; scripts/enrich_pubchem_structures.py; scripts/seed_from_sources.py; data/raw/mibig_producers.tsv; 274-source-audit.json; exact source row extracts; seeder build_concepts and attach_mibig_producers lines 3631–3666 | supports | The actual native identity/definition owner is ARO, and the exact structure is supplied by the adopted PubChem enrichment. Initial generic ChEBI owner metadata was corrected without changing captured hashes. The seeder requires an exact full InChIKey for producer attachment and rejects unmatched rows; the distinct MIBiG key explains the absence of that generated producer. All 18 input hashes remain unchanged. |
| search | Exact cervimycin A local and public-source discovery; Ignored-inclusive rg over conf, curation, data/raw, scripts and docs for cervimycin, ARO:3007601, CHEBI:209712, PubChem:11557219 and the native key; public primary title/DOI searches | context_only | The exhaustive local search included ignored files and found the adopted ARO/PubChem rows and the MIBiG candidate. Public-source discovery located the original A–D paper and later congener-specific studies. Search results were used as leads; verdict evidence is restricted to the inspected authority records, primary abstracts and stated full-text sections. |
| validation | Focused documented checks and supplemental diagnostics; 274-strict.tsv, 274-chemistry.json and 274-source-audit.json | supports | Schema, strict, exact-chemistry and preserved-source reconciliation commands all exited 0. RDKit came from the existing 019 interpreter, executed against 028. The separate tautomer diagnostic warnings are retained. These checks do not substitute for shared full-corpus QC, term, reference or history gates. |

## Limits And Additional Notes

- The original 2005 A–D discovery paper was available at complete-abstract and graphical-caption depth only: the full-text link redirected to the abstract and direct body/SI requests returned 403. Exact A MIC rows, purity and original stereochemical assignments were not independently inspected.
- The accessible 2022 and 2024 full papers predominantly test C/D and C respectively. Their selected relevant sections were inspected to enforce congener scope; this review does not claim all experiments in those papers were independently replicated or every supplementary table checked.
- The separate MIBiG comparison uses a different exact key and a keto/enol encoding. Tautomer canonicalization found matching output but emitted max-transform warnings; it is a diagnostic, not a new chemical identity policy or proof that all possible tautomer states were enumerated.
- The MIBiG candidate names CS113 while the original family literature names S. tendae HKI0179. That strain relationship and the exact A biosynthetic evidence were not established. Two current MIBiG JSON routes returned 404; the adopted versioned row, not a current API body, was inspected.
- The native minted identifier and source-derived two-star ChEBI cross-reference were not promoted or merged. A future exact-grounding change requires maintained curation rather than relying on label agreement alone.
- No taxon-specific target, MIC or producer was added. Structured protein/pathway adapters were not applicable to the populated native fields; mechanisms mentioned for other congeners were not proposed as A claims.
- Full-corpus QC, term, reference and history gates are separate from the focused checks recorded here.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native record or maintained source input was changed. All 18 preserved hashes were rechecked.
- A bounded follow-up is to inspect the original A-specific structure and assay tables, then document any exact A mechanism or producer in the native curation lane with its own primary evidence and history event. The current source extraction and strict producer join should remain reproducible.
- The review has no confirmed findings. Unavailable original detail and optional enrichment are represented as unknown assessments and limitations rather than invented native defects.
- Optional links and tags were checked for the exact cervimycin A target; no links to sibling review targets are included.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T123501Z-cervimycin-a-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of cervimycin A
started_at: '2026-10-21T12:20:03Z'
finished_at: '2026-10-21T12:35:01Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Independent read-only review of the complete generated record;
    original hashes preserved and actual ARO, PubChem and producer-input owners appended
    before detailed judgment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
native_verdict: No confirmed native defect; exact A mechanism and original stereochemical-assignment
  depth remain limited
scientific_review: true
summary: Cervimycin A is coherently represented by the native structure and current
  PubChem and ChEBI, with matching formula, charge, key and 21 configured centers.
  The cited 2022 source supports the generic polyketide-family definition, but its
  new experiments concern C/D. Original A–D discovery evidence supports antibacterial
  context at abstract depth; its full body was not obtained. Later C-specific mechanism
  results and an unresolved MIBiG producer candidate were not transferred to A. No
  confirmed native finding is raised, and no scientific status or native data was
  changed. Scientific assessment retains the stated evidence limits; full verification
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
  - path: data/antibiotics/antibacterial/cervimycin-a.yaml
    sha256: 60eb8fb5349acf7ae4f9853f26f3e8efb33dee67ff2d921396f6c456b2cbe289
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
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: data/raw/mibig_producers.tsv
    sha256: d55289619e77e035ed437d432dd692ab382f254c3841c9a314752ef22578a01b
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
  - path: scripts/extract_mibig_producers.py
    sha256: a078cdf4c9b2d09999800ab7ae03f93d3972f29b7d2f460ebbbe7d7ec6b31c53
    role: context
scope:
  description: 'Entire SEEDED, MINTED cervimycin A record: generic definition and
    cited PMID, ARO structural class, exact PubChem-derived structure, three cross-references,
    source concept and three history events.'
  selection: Queue 274; 13 original input hashes retained and five actual source/producer
    owner inputs appended, giving 18 unchanged hashes.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-da12e2d9fe
targets:
- target_id: antibioticmech:aro-da12e2d9fe
  path: data/antibiotics/antibacterial/cervimycin-a.yaml
  label: cervimycin A
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained CARD/ARO inventory extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Actual adopted ARO identity and definition owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Actual adopted exact PubChem structure owner
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/mibig_producers.tsv
    role: Existing exact-compound producer candidate requiring independent scope review
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Maintained exact PubChem enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_mibig_producers.py
    role: Maintained producer extraction and exact structure join
checks:
- check_id: schema
  name: Documented schema validation
  status: passed
  required: true
  summary: Exit 0; no issues found.
  target_ids:
  - antibioticmech:aro-da12e2d9fe
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cervimycin-a.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict validation
  status: passed
  required: true
  summary: Exit 0; zero ERROR rows.
  target_ids:
  - antibioticmech:aro-da12e2d9fe
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cervimycin-a.yaml --out /private/tmp/am-review-session/274-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Supplemental exact structure comparison
  status: passed
  required: false
  summary: Exit 0; native and current chemical authority structures agree. Separate
    tautomer enumeration emitted transform-limit warnings, retained as a limitation.
  target_ids:
  - antibioticmech:aro-da12e2d9fe
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/274-chemistry.py
    > /private/tmp/am-review-session/274-chemistry.log
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: source-reconciliation
  name: Supplemental source and preserved-hash reconciliation
  status: passed
  required: false
  summary: Exit 0; 18 hashes, exact adopted definition/structure and the native PMID
    disposition checked.
  target_ids:
  - antibioticmech:aro-da12e2d9fe
  command: .venv/bin/python /private/tmp/am-review-session/274-ledger.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - owners
- check_id: structured-adapter
  name: Structured protein/pathway adapter applicability
  status: not_applicable
  required: false
  summary: The native record names no gene, protein, pathway, regulator, stress response
    or transcriptomics dataset. C/D protein leads were inspected to prevent congener
    transfer; no A protein or pathway claim was proposed.
  target_ids:
  - antibioticmech:aro-da12e2d9fe
  evidence_ids:
  - record
  - congener-scope
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-da12e2d9fe
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
  - antibioticmech:aro-da12e2d9fe
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
  - antibioticmech:aro-da12e2d9fe
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
  - antibioticmech:aro-da12e2d9fe
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
  - antibioticmech:aro-da12e2d9fe
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
  - antibioticmech:aro-da12e2d9fe
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
  - antibioticmech:aro-da12e2d9fe
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
  - antibioticmech:aro-da12e2d9fe
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
  - antibioticmech:aro-da12e2d9fe
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/cervimycin-a.yaml
  locator: Entire native YAML and all three source history events
  accessed_at: '2026-10-21T12:34:06Z'
  support: supports
  summary: The ARO-minted identifier denotes cervimycin A, not the family as a whole.
    The exact structure and label distinguish A despite the broad family definition.
    There are no native target, resistance, MIC, producer, clinical-product, synonym
    or causal-graph assertions. MINTED is retained transparently; no unsupported REVIEWED
    status is present.
- evidence_id: chemistry
  kind: validation
  reference: PubChem:11557219; CHEBI:209712; ARO:3007601
  locator: 274-chemistry.py/.json; native SMILES/InChI, current PubChem structure,
    current ChEBI SMILES and molfile
  accessed_at: '2026-10-21T12:34:06Z'
  support: supports
  summary: All five native/current-authority representations reproduce DTTQURMKQUWCNN-ZVSUTAIVSA-N,
    C62H82O25, net charge 0 and 21 configured stereocenters, with masses matching
    native precision. The native graph has the acetyl substituent and terminal dimethylmalonyl
    ester that distinguish A from the carbamoyl or monomethyl congeners. This computational
    agreement does not independently reproduce the original NMR assignment of every
    center.
  snapshot_sha256: 11d3ded6cc4f26cd34c8ff7a4873d0254e1cb41ea60cf15d6beda4007884a675
- evidence_id: grounding
  kind: authority
  reference: CHEBI:209712; ARO:3007601; ARO:3005171
  locator: 274-chebi.json, 274-ols.json and 274-aro-stanzas.txt
  accessed_at: '2026-10-21T12:34:06Z'
  support: supports
  summary: Current ChEBI 209712 resolves exactly to Cervimycin A with the same structure
    and two-star status; its parents are anthraquinone and glycoside and it has no
    activity roles in the inspected response. ARO 3007601 resolves to the named antibiotic
    and supplies the native PubChem/ChEBI links. ARO 3005171 is the stated polyketide-with-antibiotic-activity
    class. The existence of a ChEBI xref does not alone prove that the native minted
    identifier should be replaced without a maintained grounding decision.
  snapshot_sha256: 137b2eddcee95c194fd5be00e98a6e5facfa42c08bc1d0db017b764b5a1b7468
- evidence_id: definition
  kind: primary_source
  reference: PMID:36173303; DOI:10.1128/spectrum.02567-22
  locator: '274-2022.xml/.txt: complete abstract, Introduction, relevant Results/Tables
    1 and 5 and mutant-construction methods'
  accessed_at: '2026-10-21T12:34:06Z'
  support: partial
  summary: The sole adopted PMID resolves. Its Introduction describes the cervimycin
    A–D antibiotic complex as glycosylated polyketides, supporting the native generic
    definition. Its newly measured susceptibility and resistance experiments use C
    and D, with S. aureus SG511 serial selection and allele/knockout comparisons.
    Those experiments support C/D resistance contexts, not a direct A target or exact
    A MIC. No C/D table values were promoted to this record.
  snapshot_sha256: 571563deb53e4ecdf391db262053dd2c022534737f7d43a45cd131a90b397d35
- evidence_id: discovery
  kind: primary_source
  reference: PMID:15940739; DOI:10.1002/chem.200500320
  locator: 274-core.json complete original abstract; public Wiley abstract and graphical-caption
    page, volume 11 pages 5523–5530
  accessed_at: '2026-10-21T12:34:06Z'
  support: partial
  summary: The original paper explicitly identifies cervimycins A–D, describes structure
    elucidation by NMR and chemical degradation, and reports antibacterial activity
    against resistant staphylococci and enterococci from a cave-derived Streptomyces
    tendae strain. Its abstract distinguishes acetyl/carbamoyl and methylmalonyl/dimethylmalonyl
    congeners. The full-text link redirected to the abstract; direct body and attempted
    supplementary retrieval returned 403. Therefore exact A assay rows, concentrations,
    purity, organism strains and original stereochemical assignment details remain
    unverified.
  snapshot_sha256: 921a4ff88c51b12cc5cc74f04a8257e1c4221cc384831db1b85c561d29c3e894
- evidence_id: congener-scope
  kind: primary_source
  reference: PMID:38722162; DOI:10.1128/msphere.00764-23; PMID:21077936; DOI:10.1111/j.1574-6968.2010.02143.x
  locator: '274-2024.xml/.txt: Introduction, selected Results/Discussion, susceptibility
    and microscopy methods; complete 2010 abstract in 274-core.json'
  accessed_at: '2026-10-21T12:34:06Z'
  support: context_only
  summary: The 2024 experiments specifically use cervimycin C. Gyrase supercoiling
    inhibition appears at high concentrations, whereas lower-dose cellular and omics
    results indicate a more complicated protein-stress response. Its Introduction
    cites an earlier A DNA-incorporation result at high concentration, which is historical
    context rather than a new A gyrase-binding experiment. The 2010 bmrA promoter/mRNA
    resistance study also tests C. Neither supports importing a Clp, WalK, BmrA, gyrase
    or ribosome mechanism into the native A record.
  snapshot_sha256: 11d631592adff08922e27b8f95da1f03af5fd500e7941b381162f942ca8030a9
- evidence_id: producer
  kind: database
  reference: MIBiG:BGC0001439; PMID:15326518; DOI:10.1039/B409221J
  locator: 274-mibig_producers.json adopted version-5 row; 274-chemistry.json separate
    candidate comparison; original complete 2004 abstract
  accessed_at: '2026-10-21T12:34:06Z'
  support: unknown
  summary: The existing MIBiG A row is marked questionable, not expert-reviewed, and
    names Streptomyces sp. CS113 with a first-legacy-reference citation to a cervimycin
    C biosynthesis paper. Its RDNLQESQZXBNSG-ZVSUTAIVSA-N key differs from the native
    DTTQURMKQUWCNN-ZVSUTAIVSA-N in a keto/enol encoding. Supplemental stereo-preserving
    tautomer canonicalization yielded identical canonical SMILES for both, but hit
    transform limits and is not permission to bypass the strict exact-key producer
    join. The relationship between CS113 and original S. tendae HKI0179 was not established.
    No producer is published in the native record; this unresolved candidate is not
    a demonstrated omission defect.
  snapshot_sha256: a9923444b5f9d43aa0fba2cd4f38da3ff02412dc8cc6d4d92fb15d19fca33546
- evidence_id: additional-leads
  kind: database
  reference: PMID:15326518; PMID:22179067; PMID:33999625
  locator: 274-core.json complete abstracts; 274-lead-dispositions.json
  accessed_at: '2026-10-21T12:34:06Z'
  support: context_only
  summary: The 2004 study concerns C biosynthesis and feeding; the 2012 study concerns
    CerJ biosynthetic ester formation and modified cervimycin variants; the 2021 study
    synthesizes a K tetrasaccharide fragment as a cyclohexyl glycoside. These are
    not exact A antibacterial-target experiments. The discovery query also returned
    ester-cleavage patent leads; none is a native reference or was used to support
    a finding.
  snapshot_sha256: 28b7c352a368d35d1fb95de5548be02db3553e72b5963e0698a0bf4ccbae4838
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; scripts/enrich_pubchem_structures.py;
    scripts/seed_from_sources.py; data/raw/mibig_producers.tsv
  locator: 274-source-audit.json; exact source row extracts; seeder build_concepts
    and attach_mibig_producers lines 3631–3666
  accessed_at: '2026-10-21T12:34:06Z'
  support: supports
  summary: The actual native identity/definition owner is ARO, and the exact structure
    is supplied by the adopted PubChem enrichment. Initial generic ChEBI owner metadata
    was corrected without changing captured hashes. The seeder requires an exact full
    InChIKey for producer attachment and rejects unmatched rows; the distinct MIBiG
    key explains the absence of that generated producer. All 18 input hashes remain
    unchanged.
  snapshot_sha256: 0e2aaad845e6e85ffb11b8244d8c19c5c7ea6e0a3836fc3122a0d548cafdf23a
- evidence_id: search
  kind: search
  reference: Exact cervimycin A local and public-source discovery
  locator: Ignored-inclusive rg over conf, curation, data/raw, scripts and docs for
    cervimycin, ARO:3007601, CHEBI:209712, PubChem:11557219 and the native key; public
    primary title/DOI searches
  accessed_at: '2026-10-21T12:34:06Z'
  support: context_only
  summary: The exhaustive local search included ignored files and found the adopted
    ARO/PubChem rows and the MIBiG candidate. Public-source discovery located the
    original A–D paper and later congener-specific studies. Search results were used
    as leads; verdict evidence is restricted to the inspected authority records, primary
    abstracts and stated full-text sections.
  snapshot_sha256: 95a02989e118a7fe15eee4a5fe590931e62317d26b159f7f73806b83929590a2
  search_scope: Ignored-inclusive rg over conf, curation, data/raw, scripts and docs
    for cervimycin, ARO:3007601, CHEBI:209712, PubChem:11557219 and the native key;
    public primary title/DOI searches
- evidence_id: validation
  kind: validation
  reference: Focused documented checks and supplemental diagnostics
  locator: 274-strict.tsv, 274-chemistry.json and 274-source-audit.json
  accessed_at: '2026-10-21T12:34:06Z'
  support: supports
  summary: Schema, strict, exact-chemistry and preserved-source reconciliation commands
    all exited 0. RDKit came from the existing 019 interpreter, executed against 028.
    The separate tautomer diagnostic warnings are retained. These checks do not substitute
    for shared full-corpus QC, term, reference or history gates.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact A identity and machine representation
  outcome: supported
  summary: Native structure and current exact PubChem/ChEBI representations agree;
    A is distinguished from adjacent congeners.
  target_ids:
  - antibioticmech:aro-da12e2d9fe
  evidence_ids:
  - chemistry
  - grounding
- assessment_id: primary-identity
  area: identity
  topic: Original stereochemical assignment depth
  outcome: unknown
  summary: The full original A–D NMR/chemical-degradation body was not obtained, so
    all 21 configured centers were not independently reassigned from primary data.
  target_ids:
  - antibioticmech:aro-da12e2d9fe
  evidence_ids:
  - discovery
  - chemistry
- assessment_id: classification
  area: grounding
  topic: Polyketide antibacterial class
  outcome: supported
  summary: Structural authority and the original discovery abstract support polyketide
    antibiotic identity and antibacterial context.
  target_ids:
  - antibioticmech:aro-da12e2d9fe
  evidence_ids:
  - grounding
  - discovery
  - definition
- assessment_id: definition
  area: evidence
  topic: Scope of the adopted PMID
  outcome: supported
  summary: The cited primary Introduction supports the generic family definition.
    The record does not incorrectly import its C/D experiments.
  target_ids:
  - antibioticmech:aro-da12e2d9fe
  evidence_ids:
  - definition
  - record
- assessment_id: mechanism
  area: evidence
  topic: Exact A mechanism
  outcome: unknown
  summary: No directly verified A molecular mechanism was established in the inspected
    sources; C/D evidence remains excluded from A claims.
  target_ids:
  - antibioticmech:aro-da12e2d9fe
  evidence_ids:
  - congener-scope
  - discovery
- assessment_id: producer
  area: completeness
  topic: Producer and biosynthetic context
  outcome: unknown
  summary: An existing candidate requires exact-identity normalization, taxon/strain
    reconciliation and primary source checking; automatic publication would be premature.
  target_ids:
  - antibioticmech:aro-da12e2d9fe
  evidence_ids:
  - producer
  - owners
- assessment_id: provenance
  area: provenance
  topic: Native sources and history
  outcome: supported
  summary: The definition, structure and three history events are coherent with adopted
    owners; all 18 hashes are preserved.
  target_ids:
  - antibioticmech:aro-da12e2d9fe
  evidence_ids:
  - record
  - owners
- assessment_id: completeness
  area: completeness
  topic: Optional enrichment
  outcome: supported
  summary: The sparse SEEDED record contains no unsupported mechanistic, quantitative,
    producer or clinical assertions. Optional enrichment should await exact A evidence.
  target_ids:
  - antibioticmech:aro-da12e2d9fe
  evidence_ids:
  - record
  - congener-scope
  - producer
- assessment_id: schema
  area: schema
  topic: Focused validity
  outcome: supported
  summary: Documented schema and strict checks and supplemental identity checks pass.
  target_ids:
  - antibioticmech:aro-da12e2d9fe
  evidence_ids:
  - validation
findings: []
actions: []
limitations:
- 'The original 2005 A–D discovery paper was available at complete-abstract and graphical-caption
  depth only: the full-text link redirected to the abstract and direct body/SI requests
  returned 403. Exact A MIC rows, purity and original stereochemical assignments were
  not independently inspected.'
- The accessible 2022 and 2024 full papers predominantly test C/D and C respectively.
  Their selected relevant sections were inspected to enforce congener scope; this
  review does not claim all experiments in those papers were independently replicated
  or every supplementary table checked.
- The separate MIBiG comparison uses a different exact key and a keto/enol encoding.
  Tautomer canonicalization found matching output but emitted max-transform warnings;
  it is a diagnostic, not a new chemical identity policy or proof that all possible
  tautomer states were enumerated.
- The MIBiG candidate names CS113 while the original family literature names S. tendae
  HKI0179. That strain relationship and the exact A biosynthetic evidence were not
  established. Two current MIBiG JSON routes returned 404; the adopted versioned row,
  not a current API body, was inspected.
- The native minted identifier and source-derived two-star ChEBI cross-reference were
  not promoted or merged. A future exact-grounding change requires maintained curation
  rather than relying on label agreement alone.
- No taxon-specific target, MIC or producer was added. Structured protein/pathway
  adapters were not applicable to the populated native fields; mechanisms mentioned
  for other congeners were not proposed as A claims.
- Full-corpus QC, term, reference and history gates are separate from the focused
  checks recorded here.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native record or maintained source input was changed. All 18 preserved hashes
  were rechecked.
- A bounded follow-up is to inspect the original A-specific structure and assay tables,
  then document any exact A mechanism or producer in the native curation lane with
  its own primary evidence and history event. The current source extraction and strict
  producer join should remain reproducible.
- The review has no confirmed findings. Unavailable original detail and optional enrichment
  are represented as unknown assessments and limitations rather than invented native
  defects.
- Optional links and tags were checked for the exact cervimycin A target; no links
  to sibling review targets are included.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links: []
tags:
- record-review
- cervimycin-a
- exact-congener
- primary-source-scope
```
