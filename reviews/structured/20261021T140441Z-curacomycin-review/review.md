# Review of curacomycin

- Review: 20261021T140441Z-curacomycin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T13:49:14Z
- Finished UTC: 2026-10-21T14:04:41Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Curacomycin is the chlorinated homodetic cyclic hexapeptide supported by the original isolation study. Native SMILES cannot kekulize; replacing only the indole n with [nH] restores the exact recorded InChI/key and official graph. A second major finding concerns the broad several-species origin assertion: the cited original distinguishes curacomycin from S. curacoi and dechlorocuracomycin from S. noursei. Native unassigned hydroxyasparagine stereo is appropriate, disk zones are not MICs, and an original-versus-review isoleucine conflict remains qualified.

## Scope And Provenance

Entire SEEDED, EXACT record: definition, systematic cyclic-peptide name, two parents, antibacterial role, complete molecular representation, source concept and three history events. No native molecular targets, activity rows, producer object, clinical assertions or cross-references are present.

Selection: Queue 334 in isolated batch 034. Thirteen original hashes preserved; actual role-label owner identified before detailed judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:156426 | data/antibiotics/antibacterial/curacomycin.yaml | generated | curacomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema validation | passed | True | CHEBI:156426 | Exit 0; run separately after chemistry helper aborted. |
| Documented strict validation | passed | True | CHEBI:156426 | Exit 0; no ERROR rows. |
| Native molecular consistency | failed | True | CHEBI:156426 | Exit 1: native aromatic indole nitrogen cannot kekulize; helper aborts before its validator commands. Independent schema/strict results retained separately. |
| Initial direct bond-order mapping | failed | False | CHEBI:156426 | Exit 1 at direct mapping: reconstructed InChI gives imidic-acid peptide tautomers. This diagnostic failure is retained and resolved by explicit tautomer-aware comparison, separately from the genuine native parse defect. |
| Candidate and tautomer-aware authority comparison | passed | False | CHEBI:156426 | Exit 0; exact [nH] candidate agrees with official graphs, six configured centers and two unassigned centers; no native file changed. |
| Preserved inputs and source reconciliation | passed | False | CHEBI:156426 | Exit 0; thirteen hashes, all source projections, three history events and sole adopted PMID reconcile. |
| Authoritative full QC | failed | True | CHEBI:156426 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:156426 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:156426 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:156426 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:156426 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:156426 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:156426 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:156426 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:156426 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact peptide identity and invalid SMILES

identity: concern. Targets: CHEBI:156426.

InChI, official molfile and exact [nH] candidate support the intended peptide; native SMILES is invalid.

### Partially assigned stereochemistry

representation: unknown. Targets: CHEBI:156426.

Original leaves OHAsn unassigned, matching native. Native L-Ile follows original Marfey reporting, while adopted review says L-allo-Ile; keep source disagreement without forced inversion.

### Exact source-organism scope

evidence: concern. Targets: CHEBI:156426.

Original separates curacomycin from dechlorocuracomycin production; current broad several-species claim inherits a specific source conflation.

### Antibacterial class and assay endpoint

evidence: supported. Targets: CHEBI:156426.

Exact purified compound disk-diffusion experiments support antibacterial classification; no MIC, clinical efficacy or generalized antifungal activity is inferred.

### Structural parent and retained role

grounding: supported. Targets: CHEBI:156426.

The intended graph is a homodetic cyclic hexapeptide with a chloroindole; retained antibacterial role agrees with the primary assay.

### Molecular mechanism remains open

completeness: unknown. Targets: CHEBI:156426.

No exact antimicrobial target is established in inspected sources; biosynthetic NRPS/halogenase discussion is not an antimicrobial mode. Missing optional slots alone are not additional defects.

### Source and audit history

provenance: supported. Targets: CHEBI:156426.

Sole adopted reference is explicitly identified as a review and traced to the primary experiment. All thirteen input hashes and three events reconcile.

## Findings

### F1: Imported indole SMILES lacks the required aromatic NH

major / open / confirmed; issue key: chebi-156426-invalid-indole-smiles.

Native aromatic fragment c2cnc3 cannot kekulize. The single-atom notation correction c2c[nH]c3 agrees with the native InChI/key, valid official molfile and PubChem graph, preserving stereochemistry, formula and charge. Current ChEBI repeats the malformed SMILES, making this an imported representation defect rather than a different compound.

### F2: The several-species origin assertion conflates the chlorinated and dechlorinated compounds

major / open / confirmed; issue key: chebi-156426-curacomycin-dechloro-producer-scope.

Native definition claims curacomycin occurs in several Streptomyces species. Current ChEBI maps both S. curacoi NBRC 12761 and S. noursei NBRC 15452 to the original DOI, but that primary isolates curacomycin 1 from the former and dechlorocuracomycin 2 from the latter, expressly reporting no compound 1 from noursei under those conditions. Qualify the native source claim to exact-compound evidence. This finding does not assert no other producer can exist.

## Recommended Actions And Acceptance Checks

### A1

In separately authorized curation, correct the CHEBI:156426 maintained source representation using the valid official molfile or the verified exact replacement c2cnc3 to c2c[nH]c3, with a reproducible source-aware extraction correction. Do not perform a global aromatic-n rewrite. Regenerate the native record through its seeder while retaining all other molecular fields and the two unassigned centers.

- Regenerated native SMILES parses and yields CUXAULQHGRSWLF-IKVCUCANSA-N, C37H56ClN9O8, neutral charge and the unchanged configured/unassigned stereo pattern.
- Verify mutual atom mappings against official molfile/PubChem and account explicitly for InChI imidic-acid reconstruction; no unsupported stereo change is introduced.
- Re-extraction and reseeding retain the repair; rerun documented native and required corpus gates.

### A2

Qualify the maintained definition to report isolation of exact curacomycin from S. curacoi NBRC 12761, or supply an inspected exact-compound primary source for any broader producer claim. Keep the S. noursei dechlorinated material distinct. Preserve original-versus-review stereo disagreement in curator evidence/discussion if curated; do not copy review family-level MIC or biosynthetic-target claims into this record.

- Definition no longer relies on dechlorocuracomycin production to claim multiple curacomycin-producing species.
- Any optional producer object identifies the exact compound/strain/primary evidence and distinguishes demonstrated production from biosynthetic prediction.
- Keep disk diffusion separate from MIC, and preserve partial OHAsn stereo and the bounded L-Ile/L-allo-Ile source conflict during regenerated-field review.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/curacomycin.yaml; Entire native YAML | supports | The graph/inventory denotes chlorinated curacomycin with six configured centers and two unassigned hydroxyasparagine centers. Definition lists several Streptomyces species, while source/current ChEBI carry the imported invalid SMILES. No producer object or specific antimicrobial mechanism is asserted. |
| authority | CHEBI:156426; PubChem CID146684495; 334-chebi.json; 334-chebi.mol; 334-pubchem.json; 334-pubchem-name.json | supports | Current ChEBI repeats native definition, systematic name, invalid SMILES and correct InChI/key; its molfile is valid. Official PubChem exact-name and exact-key queries resolve the same partially specified peptide. Parent labels are homodetic cyclic peptide CHEBI:24613 and chloroindole CHEBI:52508; antibacterial CHEBI:33282 is retained. Current ChEBI explicitly attaches both S. curacoi NBRC 12761 and S. noursei NBRC 15452 origins to the original DOI, motivating exact source comparison. |
| chemistry | Native structure and official authority graph reconciliation; 334-authority-chemistry.json; 334-native-parse-failure.log; 334-direct-mapping-failure.log; 334-diagnostic-failures.json | supports | Native SMILES fails kekulization. Changing only c2cnc3 to c2c[nH]c3 produces CUXAULQHGRSWLF-IKVCUCANSA-N, C37H56ClN9O8, charge 0 and matching masses. Candidate, native InChI, ChEBI molfile and PubChem SMILES/InChI agree. InChI reconstruction produces seven imidic-acid tautomers, which initially fail direct bond-order mapping; explicit imidic-acid-to-amide normalization restores mutual chirality-aware atom mapping while retaining all six configured centers and two unassigned centers. The candidate matches ChEBI molfile/PubChem SMILES directly. No mixture or additional structural correction is inferred. |
| primary-structure | DOI:10.1002/ajoc.201700433; 334-original-http.pdf institutional accepted manuscript, full main text read; printed pp2–3,5–6; Figures1/2 on 334-original-page2.png visually inspected | supports | Original MS/NMR identifies chlorinated curacomycin 1 with ClTrp–Val–Leu–Ile–Orn–OHAsn cyclic sequence and indole NH. Modified Marfey analysis reports L-Orn, L-Ile and L-ClTrp with D-Val/D-Leu; p. 6 lists separate L-Ile and L-allo-Ile standards. Printed p. 5 explicitly leaves OHAsn stereochemistry undetermined despite biosynthetic D prediction. Native two unassigned centers should therefore remain unassigned; related-peptide assignments cannot resolve them. |
| primary-producer | DOI:10.1002/ajoc.201700433; 334-original-http.pdf abstract, printed p2 isolation, p5 lines23–27 and p6 experimental isolation | refutes | Exact curacomycin 1 was isolated from S. curacoi NBRC 12761 type strain grown on ISP2 agar at 30°C for 10 days. S. noursei NBRC 15452 yielded dechlorocuracomycin 2 in leucine-supplemented nutrient agar; p. 5 explicitly says that strain did not produce1 under the reported conditions despite a putative halogenase. This refutes the attribution of both original-study products to exact curacomycin. It does not prove universal inability of S. noursei or absence of any future producer. |
| primary-activity | DOI:10.1002/ajoc.201700433; 334-original-http.pdf printed p4 results and pp5–7 strain list/methods; 334-original-page4.png visually inspected | supports | The exact compound was tested by 6 mm paper disk diffusion at 10 µg/disk on nutrient agar, incubated at 30°C for 2 days. Reported zones were 9 mm for B. subtilis NBRC 13719 and S. aureus NBRC 100910,10.5 mm for M. luteus NBRC 3333, and 15 mm for P. aeruginosa NBRC 12689, with the latter described as weak activity. DMSO was the negative control; tetracycline and cycloheximide controls used distinct loads. The dechlorinated analogue was negative in the tested panel. These are disk zones, not MICs, and no protein target or universal spectrum is established. |
| leads | PMID:32727132; DOI:10.3390/antibiotics9080452; 334-adopted-core.json; 334-adopted-review.xml full review main body; 334-lead-dispositions.json | context_only | The sole adopted PMID resolves to a secondary desotamide-family review, whose exact curacomycin reference 20 leads to the primary isolation paper. It groups family production, MIC claims and biosynthesis broadly. Section 4.3 says L-allo-Ile for curacomycin, in conflict with the original L-Ile result; preserve this as a source conflict rather than silently inverting the native side-chain center. Biosynthetic enzyme functions are not antimicrobial targets, and family MIC language is not substituted for the original disk assay. |
| later | DOI:10.3390/molecules28217442; 334-later2023.xml introduction and exact curacomycin reference context | context_only | The later synthetic paper disproves proposed noursamycin A and confirms nicrophorusamide A. Curacomycin appears as a related-structure reference; it does not assign curacomycin OHAsn stereochemistry or correct this native graph. Those sibling experimental results are not transferred. |
| owners | ChEBI inventory/extractor/seeder; 334-source-audit.json; 334-inspect.json; frozen ChEBI row | supports | Thirteen original hashes, all seeded source fields and three ordered history events reconcile. Both defects are already present in maintained imported ChEBI content. Correct through an explicit source-aware inventory/extraction correction and regeneration, not generated-YAML-only edits; no generic structure or definition override is assumed. |
| validation | Actual native and supplemental checks; 334-focused-results.json; 334-schema.log; 334-strict.log; 334-diagnostic-failures.json | supports | Schema and strict pass 0. Native SMILES consistency fails 1. Initial direct comparison fails 1 for a separately resolved tautomer issue, while the normalized candidate comparison passes 0. Passing candidate checks do not make the unchanged native representation valid. |
| search | Ignored-inclusive local and exact curacomycin public-source searches; 333334-local-hits.txt; exact curacomycin producer/stereochemistry/primary-paper searches on2026-10-21; 334-fetch manifests | context_only | Local searches included ignored files. Initial institutional HTTPS routes returned502 and web access429; subsequent HTTP and download=0 routes retrieved identical valid PDF bytes. Bounded later searches did not establish an exact OHAsn assignment or additional confirmed producer. No native gene/protein/pathway claim triggers an adapter; proposed Streptomyces biosynthetic genes are distinguished from antimicrobial targets. |

## Limits And Additional Notes

- The original institutional accepted manuscript was read in full; key structure/correlation and assay pages were visually inspected. Its separate supplementary chromatograms were not obtained or independently reprocessed.
- The adopted 2020 review uses L-allo-Ile whereas the original reports L-Ile and lists both comparison standards. No exact later curacomycin experiment resolving that conflict was verified; it is not grounds for a forced native inversion.
- The original paper leaves hydroxyasparagine stereochemistry undetermined; biosynthetic D prediction and later sibling synthetic studies do not supply an experimental exact assignment.
- The primary disk assay uses isolated material after TFA-containing chromatography without an adopted explicit stoichiometric salt characterization. The review records its reported assay conditions and does not invent neutral-material potency corrections or MICs.
- Failure to observe chlorinated product from S. noursei is bounded to the original conditions; no universal production impossibility or exhaustive producer list is asserted.
- Native chemistry remains failed despite passing schema/strict and candidate diagnostics; shared corpus gates are separate and native REVIEWED promotion is not authorized.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Native records, maintained inputs and history are unchanged.
- Chemistry used the batch 019 RDKit environment against batch 034 files; schema/strict used batch 034.
- The definition lists residues in reverse traversal from the conventional N-to-C systematic name; the original explicitly gives ClTrp–Val–Leu–Ile–Orn–OHAsn connectivity. Clarify direction during any definition edit without treating ring traversal alone as proof of a second structural defect.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T140441Z-curacomycin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of curacomycin
started_at: '2026-10-21T13:49:14Z'
finished_at: '2026-10-21T14:04:41Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Whole record independently checked against current/frozen ChEBI,
    official molfile/PubChem, sole adopted review and full original institutional
    manuscript; graph correction and peptide/producer evidence are independently reconciled.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: 'Two major findings: invalid indole SMILES and producer-scope conflation'
scientific_review: true
summary: 'Curacomycin is the chlorinated homodetic cyclic hexapeptide supported by
  the original isolation study. Native SMILES cannot kekulize; replacing only the
  indole n with [nH] restores the exact recorded InChI/key and official graph. A second
  major finding concerns the broad several-species origin assertion: the cited original
  distinguishes curacomycin from S. curacoi and dechlorocuracomycin from S. noursei.
  Native unassigned hydroxyasparagine stereo is appropriate, disk zones are not MICs,
  and an original-versus-review isoleucine conflict remains qualified.'
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
  - path: data/antibiotics/antibacterial/curacomycin.yaml
    sha256: 4d6704d64c76c2d694c0d337c97c5b8938848a322968b9fb515525c693bd1eb7
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
  description: 'Entire SEEDED, EXACT record: definition, systematic cyclic-peptide
    name, two parents, antibacterial role, complete molecular representation, source
    concept and three history events. No native molecular targets, activity rows,
    producer object, clinical assertions or cross-references are present.'
  selection: Queue 334 in isolated batch 034. Thirteen original hashes preserved;
    actual role-label owner identified before detailed judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:156426
targets:
- target_id: CHEBI:156426
  path: data/antibiotics/antibacterial/curacomycin.yaml
  label: curacomycin
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
    role: Adopted antibacterial role labels
checks:
- check_id: schema
  name: Documented schema validation
  status: passed
  required: true
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/curacomycin.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; run separately after chemistry helper aborted.
  target_ids:
  - CHEBI:156426
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict validation
  status: passed
  required: true
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/curacomycin.yaml --out /private/tmp/am-review-session/334-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; no ERROR rows.
  target_ids:
  - CHEBI:156426
  evidence_ids:
  - validation
- check_id: native-chemistry
  name: Native molecular consistency
  status: failed
  required: true
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    334
  exit_code: 1
  expected_exit_code: 0
  summary: 'Exit 1: native aromatic indole nitrogen cannot kekulize; helper aborts
    before its validator commands. Independent schema/strict results retained separately.'
  target_ids:
  - CHEBI:156426
  evidence_ids:
  - chemistry
  - validation
- check_id: direct-comparison
  name: Initial direct bond-order mapping
  status: failed
  required: false
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/334-chemistry.py
  exit_code: 1
  expected_exit_code: 0
  summary: 'Exit 1 at direct mapping: reconstructed InChI gives imidic-acid peptide
    tautomers. This diagnostic failure is retained and resolved by explicit tautomer-aware
    comparison, separately from the genuine native parse defect.'
  target_ids:
  - CHEBI:156426
  evidence_ids:
  - chemistry
- check_id: normalized-comparison
  name: Candidate and tautomer-aware authority comparison
  status: passed
  required: false
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/334-chemistry-normalized.py
    > /private/tmp/am-review-session/334-chemistry-normalized.log
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; exact [nH] candidate agrees with official graphs, six configured
    centers and two unassigned centers; no native file changed.
  target_ids:
  - CHEBI:156426
  evidence_ids:
  - chemistry
- check_id: source-ledger
  name: Preserved inputs and source reconciliation
  status: passed
  required: false
  command: .venv/bin/python /private/tmp/am-review-session/334-ledger.py
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; thirteen hashes, all source projections, three history events and
    sole adopted PMID reconcile.
  target_ids:
  - CHEBI:156426
  evidence_ids:
  - owners
  - leads
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:156426
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
  - CHEBI:156426
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
  - CHEBI:156426
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
  - CHEBI:156426
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
  - CHEBI:156426
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
  - CHEBI:156426
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
  - CHEBI:156426
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
  - CHEBI:156426
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
  - CHEBI:156426
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/curacomycin.yaml
  locator: Entire native YAML
  accessed_at: '2026-10-21T14:00:09Z'
  support: supports
  summary: The graph/inventory denotes chlorinated curacomycin with six configured
    centers and two unassigned hydroxyasparagine centers. Definition lists several
    Streptomyces species, while source/current ChEBI carry the imported invalid SMILES.
    No producer object or specific antimicrobial mechanism is asserted.
- evidence_id: authority
  kind: authority
  reference: CHEBI:156426; PubChem CID146684495
  locator: 334-chebi.json; 334-chebi.mol; 334-pubchem.json; 334-pubchem-name.json
  accessed_at: '2026-10-21T13:54:16.421206Z'
  support: supports
  summary: Current ChEBI repeats native definition, systematic name, invalid SMILES
    and correct InChI/key; its molfile is valid. Official PubChem exact-name and exact-key
    queries resolve the same partially specified peptide. Parent labels are homodetic
    cyclic peptide CHEBI:24613 and chloroindole CHEBI:52508; antibacterial CHEBI:33282
    is retained. Current ChEBI explicitly attaches both S. curacoi NBRC 12761 and
    S. noursei NBRC 15452 origins to the original DOI, motivating exact source comparison.
  snapshot_sha256: c955bf33d3cffb6ebde2b6dee8f957300c5ec6a163d7ef78b69345e1b1f75e6e
- evidence_id: chemistry
  kind: validation
  reference: Native structure and official authority graph reconciliation
  locator: 334-authority-chemistry.json; 334-native-parse-failure.log; 334-direct-mapping-failure.log;
    334-diagnostic-failures.json
  accessed_at: '2026-10-21T14:00:09Z'
  support: supports
  summary: Native SMILES fails kekulization. Changing only c2cnc3 to c2c[nH]c3 produces
    CUXAULQHGRSWLF-IKVCUCANSA-N, C37H56ClN9O8, charge 0 and matching masses. Candidate,
    native InChI, ChEBI molfile and PubChem SMILES/InChI agree. InChI reconstruction
    produces seven imidic-acid tautomers, which initially fail direct bond-order mapping;
    explicit imidic-acid-to-amide normalization restores mutual chirality-aware atom
    mapping while retaining all six configured centers and two unassigned centers.
    The candidate matches ChEBI molfile/PubChem SMILES directly. No mixture or additional
    structural correction is inferred.
  snapshot_sha256: bd8f03a44869b7010b92ca79f4ab043fdddac5e3f60da119f5fd957c8cdd5e31
- evidence_id: primary-structure
  kind: primary_source
  reference: DOI:10.1002/ajoc.201700433
  locator: 334-original-http.pdf institutional accepted manuscript, full main text
    read; printed pp2–3,5–6; Figures1/2 on 334-original-page2.png visually inspected
  accessed_at: '2026-10-21T13:56:16.242272Z'
  support: supports
  summary: Original MS/NMR identifies chlorinated curacomycin 1 with ClTrp–Val–Leu–Ile–Orn–OHAsn
    cyclic sequence and indole NH. Modified Marfey analysis reports L-Orn, L-Ile and
    L-ClTrp with D-Val/D-Leu; p. 6 lists separate L-Ile and L-allo-Ile standards.
    Printed p. 5 explicitly leaves OHAsn stereochemistry undetermined despite biosynthetic
    D prediction. Native two unassigned centers should therefore remain unassigned;
    related-peptide assignments cannot resolve them.
  snapshot_sha256: b39250f17d3b1aad87f4b8a6af7f4dfed264b7c1ddfcb86d15632507ad66343a
- evidence_id: primary-producer
  kind: primary_source
  reference: DOI:10.1002/ajoc.201700433
  locator: 334-original-http.pdf abstract, printed p2 isolation, p5 lines23–27 and
    p6 experimental isolation
  accessed_at: '2026-10-21T13:56:16.242272Z'
  support: refutes
  summary: Exact curacomycin 1 was isolated from S. curacoi NBRC 12761 type strain
    grown on ISP2 agar at 30°C for 10 days. S. noursei NBRC 15452 yielded dechlorocuracomycin
    2 in leucine-supplemented nutrient agar; p. 5 explicitly says that strain did
    not produce1 under the reported conditions despite a putative halogenase. This
    refutes the attribution of both original-study products to exact curacomycin.
    It does not prove universal inability of S. noursei or absence of any future producer.
  snapshot_sha256: b39250f17d3b1aad87f4b8a6af7f4dfed264b7c1ddfcb86d15632507ad66343a
- evidence_id: primary-activity
  kind: primary_source
  reference: DOI:10.1002/ajoc.201700433
  locator: 334-original-http.pdf printed p4 results and pp5–7 strain list/methods;
    334-original-page4.png visually inspected
  accessed_at: '2026-10-21T13:56:16.242272Z'
  support: supports
  summary: The exact compound was tested by 6 mm paper disk diffusion at 10 µg/disk
    on nutrient agar, incubated at 30°C for 2 days. Reported zones were 9 mm for B.
    subtilis NBRC 13719 and S. aureus NBRC 100910,10.5 mm for M. luteus NBRC 3333,
    and 15 mm for P. aeruginosa NBRC 12689, with the latter described as weak activity.
    DMSO was the negative control; tetracycline and cycloheximide controls used distinct
    loads. The dechlorinated analogue was negative in the tested panel. These are
    disk zones, not MICs, and no protein target or universal spectrum is established.
  snapshot_sha256: b39250f17d3b1aad87f4b8a6af7f4dfed264b7c1ddfcb86d15632507ad66343a
- evidence_id: leads
  kind: database
  reference: PMID:32727132; DOI:10.3390/antibiotics9080452
  locator: 334-adopted-core.json; 334-adopted-review.xml full review main body; 334-lead-dispositions.json
  accessed_at: '2026-10-21T13:54:36.925113Z'
  support: context_only
  summary: The sole adopted PMID resolves to a secondary desotamide-family review,
    whose exact curacomycin reference 20 leads to the primary isolation paper. It
    groups family production, MIC claims and biosynthesis broadly. Section 4.3 says
    L-allo-Ile for curacomycin, in conflict with the original L-Ile result; preserve
    this as a source conflict rather than silently inverting the native side-chain
    center. Biosynthetic enzyme functions are not antimicrobial targets, and family
    MIC language is not substituted for the original disk assay.
  snapshot_sha256: 96331c300ff545d140d57a2c3c2468699a1270bc9577e06dc33e94f291e01553
- evidence_id: later
  kind: primary_source
  reference: DOI:10.3390/molecules28217442
  locator: 334-later2023.xml introduction and exact curacomycin reference context
  accessed_at: '2026-10-21T13:54:36.925207Z'
  support: context_only
  summary: The later synthetic paper disproves proposed noursamycin A and confirms
    nicrophorusamide A. Curacomycin appears as a related-structure reference; it does
    not assign curacomycin OHAsn stereochemistry or correct this native graph. Those
    sibling experimental results are not transferred.
  snapshot_sha256: 79ddc5b4e66e9b0109d2abcbf4e179653afce7a3b476ec2e12e65c231680db27
- evidence_id: owners
  kind: database
  reference: ChEBI inventory/extractor/seeder
  locator: 334-source-audit.json; 334-inspect.json; frozen ChEBI row
  accessed_at: '2026-10-21T14:00:09Z'
  support: supports
  summary: Thirteen original hashes, all seeded source fields and three ordered history
    events reconcile. Both defects are already present in maintained imported ChEBI
    content. Correct through an explicit source-aware inventory/extraction correction
    and regeneration, not generated-YAML-only edits; no generic structure or definition
    override is assumed.
  snapshot_sha256: 8ddbcd15829d0ee45a48e4de2ae99f9188488007381158fbe9de42b068818de2
- evidence_id: validation
  kind: validation
  reference: Actual native and supplemental checks
  locator: 334-focused-results.json; 334-schema.log; 334-strict.log; 334-diagnostic-failures.json
  accessed_at: '2026-10-21T14:00:09Z'
  support: supports
  summary: Schema and strict pass 0. Native SMILES consistency fails 1. Initial direct
    comparison fails 1 for a separately resolved tautomer issue, while the normalized
    candidate comparison passes 0. Passing candidate checks do not make the unchanged
    native representation valid.
  snapshot_sha256: 7981cc99b1d38487d230f64188e17e41243e4407d94b893b6e41bb77811a72b6
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local and exact curacomycin public-source searches
  locator: 333334-local-hits.txt; exact curacomycin producer/stereochemistry/primary-paper
    searches on2026-10-21; 334-fetch manifests
  accessed_at: '2026-10-21T14:00:09Z'
  support: context_only
  summary: Local searches included ignored files. Initial institutional HTTPS routes
    returned502 and web access429; subsequent HTTP and download=0 routes retrieved
    identical valid PDF bytes. Bounded later searches did not establish an exact OHAsn
    assignment or additional confirmed producer. No native gene/protein/pathway claim
    triggers an adapter; proposed Streptomyces biosynthetic genes are distinguished
    from antimicrobial targets.
  snapshot_sha256: 47576c595021876c5488373e8e1d0c1c16424dfcd7698ebe6a0c76aa12fe1125
  search_scope: 333334-local-hits.txt; exact curacomycin producer/stereochemistry/primary-paper
    searches on2026-10-21; 334-fetch manifests
assessments:
- assessment_id: structure
  area: identity
  topic: Exact peptide identity and invalid SMILES
  outcome: concern
  summary: InChI, official molfile and exact [nH] candidate support the intended peptide;
    native SMILES is invalid.
  target_ids:
  - CHEBI:156426
  evidence_ids:
  - record
  - authority
  - chemistry
  - primary-structure
- assessment_id: stereo
  area: representation
  topic: Partially assigned stereochemistry
  outcome: unknown
  summary: Original leaves OHAsn unassigned, matching native. Native L-Ile follows
    original Marfey reporting, while adopted review says L-allo-Ile; keep source disagreement
    without forced inversion.
  target_ids:
  - CHEBI:156426
  evidence_ids:
  - chemistry
  - primary-structure
  - leads
  - later
- assessment_id: producer
  area: evidence
  topic: Exact source-organism scope
  outcome: concern
  summary: Original separates curacomycin from dechlorocuracomycin production; current
    broad several-species claim inherits a specific source conflation.
  target_ids:
  - CHEBI:156426
  evidence_ids:
  - record
  - authority
  - primary-producer
- assessment_id: activity
  area: evidence
  topic: Antibacterial class and assay endpoint
  outcome: supported
  summary: Exact purified compound disk-diffusion experiments support antibacterial
    classification; no MIC, clinical efficacy or generalized antifungal activity is
    inferred.
  target_ids:
  - CHEBI:156426
  evidence_ids:
  - primary-activity
  - authority
- assessment_id: terms
  area: grounding
  topic: Structural parent and retained role
  outcome: supported
  summary: The intended graph is a homodetic cyclic hexapeptide with a chloroindole;
    retained antibacterial role agrees with the primary assay.
  target_ids:
  - CHEBI:156426
  evidence_ids:
  - chemistry
  - primary-structure
  - authority
- assessment_id: mechanism
  area: completeness
  topic: Molecular mechanism remains open
  outcome: unknown
  summary: No exact antimicrobial target is established in inspected sources; biosynthetic
    NRPS/halogenase discussion is not an antimicrobial mode. Missing optional slots
    alone are not additional defects.
  target_ids:
  - CHEBI:156426
  evidence_ids:
  - record
  - leads
  - primary-activity
- assessment_id: provenance
  area: provenance
  topic: Source and audit history
  outcome: supported
  summary: Sole adopted reference is explicitly identified as a review and traced
    to the primary experiment. All thirteen input hashes and three events reconcile.
  target_ids:
  - CHEBI:156426
  evidence_ids:
  - owners
  - leads
  - validation
findings:
- finding_id: F1
  issue_key: chebi-156426-invalid-indole-smiles
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Imported indole SMILES lacks the required aromatic NH
  description: Native aromatic fragment c2cnc3 cannot kekulize. The single-atom notation
    correction c2c[nH]c3 agrees with the native InChI/key, valid official molfile
    and PubChem graph, preserving stereochemistry, formula and charge. Current ChEBI
    repeats the malformed SMILES, making this an imported representation defect rather
    than a different compound.
  target_ids:
  - CHEBI:156426
  field_paths:
  - chemical_structure.smiles
  evidence_ids:
  - chemistry
  - authority
  - primary-structure
  - validation
  rule_id: 'review-checklist: Structure'
  native_severity: Major unusable chemical serialization
  normalization_reason: The intended exact compound remains resolvable through concordant
    valid representations; the molecular SMILES field itself fails parsing.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted chemistry and definition owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ChEBI extraction and reproducible source correction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Regenerate imported record fields
- finding_id: F2
  issue_key: chebi-156426-curacomycin-dechloro-producer-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The several-species origin assertion conflates the chlorinated and dechlorinated
    compounds
  description: Native definition claims curacomycin occurs in several Streptomyces
    species. Current ChEBI maps both S. curacoi NBRC 12761 and S. noursei NBRC 15452
    to the original DOI, but that primary isolates curacomycin 1 from the former and
    dechlorocuracomycin 2 from the latter, expressly reporting no compound 1 from
    noursei under those conditions. Qualify the native source claim to exact-compound
    evidence. This finding does not assert no other producer can exist.
  target_ids:
  - CHEBI:156426
  field_paths:
  - definition
  evidence_ids:
  - record
  - authority
  - primary-producer
  - leads
  rule_id: 'review-checklist: Producer and preservation of source scope'
  native_severity: Major source-to-compound producer misattribution
  normalization_reason: The cited original directly separates the products; a near-identical
    biosynthetic cluster or related molecule does not establish production of exact
    chlorinated curacomycin.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted chemistry and definition owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ChEBI extraction and reproducible source correction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Regenerate imported record fields
actions:
- action_id: A1
  description: In separately authorized curation, correct the CHEBI:156426 maintained
    source representation using the valid official molfile or the verified exact replacement
    c2cnc3 to c2c[nH]c3, with a reproducible source-aware extraction correction. Do
    not perform a global aromatic-n rewrite. Regenerate the native record through
    its seeder while retaining all other molecular fields and the two unassigned centers.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:156426
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted chemistry and definition owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ChEBI extraction and reproducible source correction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Regenerate imported record fields
  acceptance_checks:
  - Regenerated native SMILES parses and yields CUXAULQHGRSWLF-IKVCUCANSA-N, C37H56ClN9O8,
    neutral charge and the unchanged configured/unassigned stereo pattern.
  - Verify mutual atom mappings against official molfile/PubChem and account explicitly
    for InChI imidic-acid reconstruction; no unsupported stereo change is introduced.
  - Re-extraction and reseeding retain the repair; rerun documented native and required
    corpus gates.
- action_id: A2
  description: Qualify the maintained definition to report isolation of exact curacomycin
    from S. curacoi NBRC 12761, or supply an inspected exact-compound primary source
    for any broader producer claim. Keep the S. noursei dechlorinated material distinct.
    Preserve original-versus-review stereo disagreement in curator evidence/discussion
    if curated; do not copy review family-level MIC or biosynthetic-target claims
    into this record.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:156426
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted chemistry and definition owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ChEBI extraction and reproducible source correction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Regenerate imported record fields
  acceptance_checks:
  - Definition no longer relies on dechlorocuracomycin production to claim multiple
    curacomycin-producing species.
  - Any optional producer object identifies the exact compound/strain/primary evidence
    and distinguishes demonstrated production from biosynthetic prediction.
  - Keep disk diffusion separate from MIC, and preserve partial OHAsn stereo and the
    bounded L-Ile/L-allo-Ile source conflict during regenerated-field review.
limitations:
- The original institutional accepted manuscript was read in full; key structure/correlation
  and assay pages were visually inspected. Its separate supplementary chromatograms
  were not obtained or independently reprocessed.
- The adopted 2020 review uses L-allo-Ile whereas the original reports L-Ile and lists
  both comparison standards. No exact later curacomycin experiment resolving that
  conflict was verified; it is not grounds for a forced native inversion.
- The original paper leaves hydroxyasparagine stereochemistry undetermined; biosynthetic
  D prediction and later sibling synthetic studies do not supply an experimental exact
  assignment.
- The primary disk assay uses isolated material after TFA-containing chromatography
  without an adopted explicit stoichiometric salt characterization. The review records
  its reported assay conditions and does not invent neutral-material potency corrections
  or MICs.
- Failure to observe chlorinated product from S. noursei is bounded to the original
  conditions; no universal production impossibility or exhaustive producer list is
  asserted.
- Native chemistry remains failed despite passing schema/strict and candidate diagnostics;
  shared corpus gates are separate and native REVIEWED promotion is not authorized.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Native records, maintained inputs and history are unchanged.
- Chemistry used the batch 019 RDKit environment against batch 034 files; schema/strict
  used batch 034.
- The definition lists residues in reverse traversal from the conventional N-to-C
  systematic name; the original explicitly gives ClTrp–Val–Leu–Ile–Orn–OHAsn connectivity.
  Clarify direction during any definition edit without treating ring traversal alone
  as proof of a second structural defect.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://doi.org/10.1002/ajoc.201700433
- https://shizuoka.repo.nii.ac.jp/records/10871
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7459860/
tags:
- record-review
- curacomycin
- invalid-smiles
- producer-scope
```
