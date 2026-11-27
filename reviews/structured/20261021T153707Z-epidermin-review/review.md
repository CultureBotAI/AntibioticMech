# Review of epidermin

- Review: 20261021T153707Z-epidermin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T15:13:48Z
- Finished UTC: 2026-10-21T15:37:07Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native mature epidermin graph agrees with current ChEBI and PubChem encodings, and the original structural and precursor abstracts support its unusual residues and 21-peptide-amide description. The staphylococcin 1580 synonym is supported by the original identification study. The curated EpiFEG claim preserves donor, engineered-host and collective-gene scope. Its original abstract and sequence accessions corroborate that scope; exact full-method details could not be independently reopened. No confirmed native correction was established. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole SEEDED, EXACT record: structural definition, two typed synonyms, two parents and two activity roles, complete chemistry, CAS/Reaxys and patent links, source concept, five histories and the full curator-owned qualitative EpiFEG resistance object. All five adopted ChEBI PMID leads and the curated original PMID disposed.

Selection: Queue 403 in isolated batch 041. Original 13 hashes and actual ChEBI owners preserved; the native curator-owned resistance lane was identified before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:71659 | data/antibiotics/antibacterial/epidermin.yaml | generated | epidermin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native schema | passed | True | CHEBI:71659 | Exit 0. |
| Native strict terms | passed | True | CHEBI:71659 | Exit 0; no ERROR rows. |
| Native molecular consistency | passed | False | CHEBI:71659 | Graph, key, formula, charge and masses agree. |
| Initial direct graph comparison | failed | False | CHEBI:71659 | Actual exit 1 at the InChI-reader tautomer. This failed supplemental assertion is preserved and is not evidence of a native chemical defect. |
| Explicit official graph comparison | passed | False | CHEBI:71659 | Six Standard InChIKeys agree; four SMILES/molfile encodings match directly with chirality. InChI-reader bond-order differences and parity-preserving adjacency mapping are explicit. |
| Structured donor/host coverage discovery | passed | False | CHEBI:71659 | Dataset discovery preceded mechanism web follow-up. Neither donor nor assay-host species has a matching covered dataset; exact-host searches are not applicable. |
| Whole source and reference ledger | passed | False | CHEBI:71659 | All 13 hashes unchanged, six adopted/curated PMID leads disposed and five ordered histories checked. |
| Authoritative full QC | failed | True | CHEBI:71659 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:71659 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:71659 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:71659 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:71659 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:71659 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:71659 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:71659 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:71659 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact mature structure and naming

identity: supported. Targets: CHEBI:71659.

Official encodings and original structure/precursor evidence agree at the inspected level; no 21-versus 22 false defect.

### Class, roles and identifiers

grounding: supported. Targets: CHEBI:71659.

Class/role terms and chemical source identity resolve; patent is correctly documentary.

### Independent CAS/Reaxys detail

grounding: unknown. Targets: CHEBI:71659.

Current ChEBI repeats the mappings, but exact registry details could not be independently read.

### Donor, host and collective phenotype

scope: supported. Targets: CHEBI:71659.

The native qualitative claim avoids single-gene sufficiency, donor/host conflation, experimental-allele assignment and unmeasured transport.

### Exact full-method/Table 1 confirmation

evidence: unknown. Targets: CHEBI:71659.

Original complete abstract corroborates the main claim; specific prior-curation TM300 and purified-reagent details were not independently reopened.

### Antibacterial and mechanism evidence

evidence: supported. Targets: CHEBI:71659.

Exact original assays support antibacterial role and substrate-associated membrane effects; gallidermin-only endpoints and direct protein binding are excluded.

### Optional mechanism and susceptibility enrichment

completeness: supported. Targets: CHEBI:71659.

No demonstrated required representation defect. Later curation could add exact lipid II and strain-specific assay evidence with full conditions and graph/claim-level citations.

### Source and curated claim preservation

ownership: supported. Targets: CHEBI:71659.

Actual owners and five histories are recorded;13 initial hashes unchanged.

### Native deterministic checks

schema: supported. Targets: CHEBI:71659.

Focused native checks pass; the supplemental tautomer assertion failure is transparently retained.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/epidermin.yaml; Entire native YAML | supports | The record identifies mature epidermin and a qualitative collective EpiFEG immunity phenotype in laboratory S. carnosus derivatives. Its note explicitly separates donor references, experimental alleles, host lineage and transport hypothesis. No numeric AST, clinical resistance category or direct target object is asserted. |
| chemistry | CHEBI:71659; PubChem CID70698381; 403-chebi.json;403-chebi.mol;403-pubchem.json;403-authority-chemistry.json | supports | Six encodings produce CXTXHTVXPMOOSW-JUEJINBGSA-N and neutral C98H141N25O23S4, with 21 assigned tetrahedral centers and none unspecified. Native/current ChEBI SMILES, ChEBI molfile and PubChem SMILES match reciprocally with chirality. Both InChI readers produce the same imidic-acid tautomer; explicit bond-order-generic adjacency mapping preserves tetrahedral parity and isolates C-N/C-O changes. Database concordance is not an independent primary structural determination. |
| structure | PMID:3769923; DOI:10.1111/j.1432-1033.1986.tb09933.x; DOI:10.1038/333276a0; 403-core-3769923.json and403-nature-core.json complete original abstracts | supports | The original sequencing study describes a tetracyclic21-peptide amide from S. epidermidis Tü 3298, including meso-lanthionine, the specified methyllanthionine and aminovinyl-D-cysteine. The later original precursor study explicitly distinguishes the C-terminal 22-residue precursor segment from the mature21-peptide amide. Thus22-residue shorthand elsewhere does not by itself contradict the native mature-product wording. Full 1986 structure PDF access failed. |
| synonym | PMID:8135526; DOI:10.1128/AEM.60.2.752-755.1994; 403-synonym-p752.png printed p752 visually inspected, plus complete abstract | supports | The original study purifies staphylococcin 1580 from S. epidermidis 1580 to homogeneity and identifies it with epidermin by amino-acid analysis, mass and N-terminal sequence. This supports the exact synonym without equating the 1580 producer strain with Tü 3298. |
| immunity | PMID:8550476; DOI:10.1128/JB.178.2.531-536.1996; 403-core-8550476.json and403-PMC177688.html complete original abstract | supports | The original abstract reports increased epidermin tolerance in the S. carnosus cloning host carrying epiFEG, with the highest tolerance when epiQ is also present. Inactivation of any component loses immunity; all three complement a sensitive S. epidermidis mutant. It proposes an ABC-transporter explanation rather than directly demonstrating transport. This supports the bounded collective qualitative claim, but the precise TM300-derived constructs, purified reagent and Table 1 details stated in prior curation were not independently reread from a full paper in this review. |
| accessions | UniProtKB:Q54002; UniProtKB:Q54003; UniProtKB:Q54004; ENA:U29130; NCBITaxon:1281; 403-uniprot-Q54002.json throughQ54004;403-ena.txt;403-taxon.json | supports | Current UniProt records resolve respectively to epiF, epiE and epiG in S. epidermidis, cite PMID8550476 and specify donor strain Tue3298/plasmid pTue32. They are unreviewed sequence-reference records, not verified experimental alleles. ENA resolves U29130 as a secondary accession of U77778 and carries the same donor genes and paper. Taxon1281 resolves to S. carnosus, without representing the engineered derivative. Native prose preserves these limits. |
| leads | Five adopted ChEBI PMID leads and curated PMID8550476; 403-source-audit.json complete per-lead dispositions;403-core-*.json | supports | All six complete abstracts were inspected. PMID1551392 concerns biosynthetic genetics and heterologous production;16586024 concerns clinical-isolate inhibition and in-vitro catheter adhesion in activity units, not a clinical outcome or mass-based MIC;3769923 concerns structure;8135526 establishes the synonym;8775972 is a biosynthesis review, retained as secondary context;8550476 is the exact immunity original. No single lead is promoted to support the entire record. |
| mechanism | PMID:9791177; DOI:10.1046/j.1365-2958.1998.01065.x; 403-9791177.json complete original abstract | supports | Exact epidermin forms a complex with labeled lipid II and induces marker release in lipid II-containing liposomes. Intact-cell experiments include M. luteus and S. simulans with ramoplanin pretreatment. The result supports substrate-dependent membrane action; it is not direct binding to a protein enzyme. |
| activity | PMID:16569864; DOI:10.1128/AAC.50.4.1449-1457.2006; 403-PMC1426925.html selected material/MIC/biochemical methods, Table1 and exact epidermin results | supports | The study purifies epidermin from Tü 3298 and confirms peptide mass and purity by electrospray MS. Table 1 gives epidermin MICs of 0.002, 0.15 and 0.002 µM against M. flavus DSM 1790, S. simulans 22 and L. lactis subsp.cremoris HP under separately stated broth/incubation conditions. The exact epidermin experiments include pore activity in M. flavus and inhibition of lipid II synthesis/FemX reaction through substrate complexation. Gallidermin-only membrane-composition, kinetic and other strain results are not transferred to epidermin; the native record does not yet claim these quantitative rows. |
| terms | CHEBI:51026; CHEBI:71645; CHEBI:33281; CHEBI:33282; 403-term-51026.json;403-term-71645.json;403-term-33281.json;403-term-33282.json | supports | All four terms resolve to the stated macrocycle, type A lantibiotic, antimicrobial and antibacterial meanings. The native graph, original structural/biosynthetic evidence and exact antibacterial assays support their application. No universal Gram-positive susceptibility is inferred. |
| patent | patent:EP0350810; 403-patent.html description and producer/purification/assay passages, German text with supplied English translation | supports | The exact patent resolves to an epidermin production/isolation process. It specifies S. epidermidis DSM 3095, chromatography and HPLC purification and a diffusion assay using M. luteus ATCC 9341. It is appropriately a document link; this review does not infer current therapeutic approval or silently equate the deposited producer with a different named strain. |
| registry | cas:99165-17-0; reaxys:11305595; 403-chebi.json database_accessions;403-cas.html;403-fetch3.json | context_only | Current ChEBI reproduces both adopted registry mappings. Direct CAS retrieval returned an application error without compound details, and Reaxys returned 403. Their exact public registry graphs therefore remain independently unverified; neither failed retrieval demonstrates a wrong identifier. |
| adapter | iModulonDB dataset catalog; 403-adapter-results.json | context_only | Actual catalog discovery preceded mechanism searches. Neither S. carnosus nor S. epidermidis had a matching covered organism/dataset; no exact-host gene search or module summary was applicable. Catalog absence is not negative evidence about EpiFEG. |
| owners | Maintained ChEBI row and curator-owned resistance lane; 403-owner-append.json;403-raw-rows.json;403-source-audit.json | supports | All 13 original input hashes remain unchanged. Definition, structure, names, parents, roles and links trace to the maintained ChEBI row/extractor/seeder; the later resistance assertion is curated directly in the native record. Ignored-inclusive searches of curation,scripts,data/raw and docs found no separate matching resistance overlay. Five histories remain ordered, and no REVIEWED status is asserted. |
| validation | Native and supplementary checks; 403-focused-results.json;403-strict.tsv;403-authority-chemistry-initial.log;403-authority-chemistry.log;403-ledger.log | supports | Native schema, strict terms and chemistry pass. The initial direct graph assertion fails on the InChI-reader tautomer; the final explicit comparison and source ledger pass. Scientific scope is assessed separately. |
| access | Bounded public epidermin source retrieval; 403-fetch.json through403-fetch5.json;403-curated-owner-hits.txt and403-local-hits.txt include ignored files | context_only | Original immunity and structure full-text routes returned 403, 404 or 500; a nominal PMC PDF response was an HTML challenge, not a PDF. Complete abstracts, original synonym page, later primary mechanism main text, patent and sequence authorities were read at the stated levels. |

## Limits And Additional Notes

- The original 1986 structure paper was inspected at complete-abstract level because the full PDF returned 403. Full stereochemical reassignment from primary spectra was not performed; official graph concordance is distinguished from an independent structure determination.
- The original 1996 immunity full main text and Table 1 could not be independently retrieved. Its complete abstract and exact sequence records support the collective phenotype and donor/host distinction, but the prior-curation TM300 and purified-reagent details remain a bounded verification limit.
- CAS and Reaxys are reproduced by current ChEBI, but public direct detail retrieval failed. No identifier error is inferred from that access limit.
- Selected 2006 methods, Table 1 and exact epidermin results were read. Gallidermin-only results and complete supplementary figure inspection are not claimed. The 1998 mechanism paper was inspected at complete-abstract level.
- The initial supplemental direct structure comparison failed because the InChI reader generated an imidic-acid tautomer. The final audit records bond-order differences and preserves all tetrahedral parity; the native chemistry gate passed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Standalone chemistry used the batch 019 interpreter against batch 041; native checks and source ledger used batch 041.
- Optional follow-up belongs in separately authorized curation: represent lipid II binding, context-specific membrane effects and exact published susceptibility rows without converting substrate sequestration into direct binding to FemX or another enzyme.
- No native record, scientific status or immutable review bundle was edited by this review draft.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T153707Z-epidermin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of epidermin
started_at: '2026-10-21T15:13:48Z'
finished_at: '2026-10-21T15:37:07Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Whole native and maintained ChEBI row read; independent official
    encoding comparisons and source-claim audit; all adopted abstracts, selected original
    synonym and mechanism experiments, sequence accessions and patent text inspected.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
native_verdict: Exact mature peptide and bounded qualitative immunity claim supported,
  with original full-text access limits
scientific_review: true
summary: The native mature epidermin graph agrees with current ChEBI and PubChem encodings,
  and the original structural and precursor abstracts support its unusual residues
  and 21-peptide-amide description. The staphylococcin 1580 synonym is supported by
  the original identification study. The curated EpiFEG claim preserves donor, engineered-host
  and collective-gene scope. Its original abstract and sequence accessions corroborate
  that scope; exact full-method details could not be independently reopened. No confirmed
  native correction was established. Scientific assessment retains the stated evidence
  limits; full verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/epidermin.yaml
    sha256: 77304621867a2f20d51f7c5e504447ee7f6fd3d9b320e9d95514dff1a241e4c5
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
  description: 'Whole SEEDED, EXACT record: structural definition, two typed synonyms,
    two parents and two activity roles, complete chemistry, CAS/Reaxys and patent
    links, source concept, five histories and the full curator-owned qualitative EpiFEG
    resistance object. All five adopted ChEBI PMID leads and the curated original
    PMID disposed.'
  selection: Queue 403 in isolated batch 041. Original 13 hashes and actual ChEBI
    owners preserved; the native curator-owned resistance lane was identified before
    assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:71659
targets:
- target_id: CHEBI:71659
  path: data/antibiotics/antibacterial/epidermin.yaml
  label: epidermin
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
    path: data/antibiotics/antibacterial/epidermin.yaml
    role: Curator-owned qualitative EpiFEG resistance assertion
checks:
- check_id: schema
  name: Native schema
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/epidermin.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0.
  target_ids:
  - CHEBI:71659
  evidence_ids:
  - validation
- check_id: strict
  name: Native strict terms
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/epidermin.yaml --out /private/tmp/am-review-session/403-strict.tsv
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; no ERROR rows.
  target_ids:
  - CHEBI:71659
  evidence_ids:
  - validation
- check_id: native-chemistry
  name: Native molecular consistency
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    403 > /private/tmp/am-review-session/403-focused-run.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Graph, key, formula, charge and masses agree.
  target_ids:
  - CHEBI:71659
  evidence_ids:
  - chemistry
  - validation
- check_id: initial-authorities
  name: Initial direct graph comparison
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/403-authority-chemistry-initial.py
    > /private/tmp/am-review-session/403-authority-chemistry-initial.log 2>&1
  status: failed
  required: false
  exit_code: 1
  expected_exit_code: 0
  summary: Actual exit 1 at the InChI-reader tautomer. This failed supplemental assertion
    is preserved and is not evidence of a native chemical defect.
  target_ids:
  - CHEBI:71659
  evidence_ids:
  - chemistry
- check_id: authority-chemistry
  name: Explicit official graph comparison
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/403-authority-chemistry.py
    > /private/tmp/am-review-session/403-authority-chemistry.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Six Standard InChIKeys agree; four SMILES/molfile encodings match directly
    with chirality. InChI-reader bond-order differences and parity-preserving adjacency
    mapping are explicit.
  target_ids:
  - CHEBI:71659
  evidence_ids:
  - chemistry
- check_id: adapter
  name: Structured donor/host coverage discovery
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/403-adapter.py
    > /private/tmp/am-review-session/403-adapter.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Dataset discovery preceded mechanism web follow-up. Neither donor nor assay-host
    species has a matching covered dataset; exact-host searches are not applicable.
  target_ids:
  - CHEBI:71659
  evidence_ids:
  - adapter
- check_id: source-ledger
  name: Whole source and reference ledger
  command: .venv/bin/python /private/tmp/am-review-session/403-ledger.py > /private/tmp/am-review-session/403-ledger.log
    2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: All 13 hashes unchanged, six adopted/curated PMID leads disposed and five
    ordered histories checked.
  target_ids:
  - CHEBI:71659
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
  - CHEBI:71659
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
  - CHEBI:71659
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
  - CHEBI:71659
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
  - CHEBI:71659
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
  - CHEBI:71659
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
  - CHEBI:71659
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
  - CHEBI:71659
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
  - CHEBI:71659
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
  - CHEBI:71659
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/epidermin.yaml
  locator: Entire native YAML
  accessed_at: '2026-10-21T15:34:40Z'
  support: supports
  summary: The record identifies mature epidermin and a qualitative collective EpiFEG
    immunity phenotype in laboratory S. carnosus derivatives. Its note explicitly
    separates donor references, experimental alleles, host lineage and transport hypothesis.
    No numeric AST, clinical resistance category or direct target object is asserted.
- evidence_id: chemistry
  kind: authority
  reference: CHEBI:71659; PubChem CID70698381
  locator: 403-chebi.json;403-chebi.mol;403-pubchem.json;403-authority-chemistry.json
  accessed_at: '2026-10-21T15:34:40Z'
  support: supports
  summary: Six encodings produce CXTXHTVXPMOOSW-JUEJINBGSA-N and neutral C98H141N25O23S4,
    with 21 assigned tetrahedral centers and none unspecified. Native/current ChEBI
    SMILES, ChEBI molfile and PubChem SMILES match reciprocally with chirality. Both
    InChI readers produce the same imidic-acid tautomer; explicit bond-order-generic
    adjacency mapping preserves tetrahedral parity and isolates C-N/C-O changes. Database
    concordance is not an independent primary structural determination.
  snapshot_sha256: 37f0dc6eab7e6349a6587dc2dd1274d9df04c5fe3306f77b5974c6112ca22583
- evidence_id: structure
  kind: primary_source
  reference: PMID:3769923; DOI:10.1111/j.1432-1033.1986.tb09933.x; DOI:10.1038/333276a0
  locator: 403-core-3769923.json and403-nature-core.json complete original abstracts
  accessed_at: '2026-10-21T15:28:49.560886Z'
  support: supports
  summary: The original sequencing study describes a tetracyclic21-peptide amide from
    S. epidermidis Tü 3298, including meso-lanthionine, the specified methyllanthionine
    and aminovinyl-D-cysteine. The later original precursor study explicitly distinguishes
    the C-terminal 22-residue precursor segment from the mature21-peptide amide. Thus22-residue
    shorthand elsewhere does not by itself contradict the native mature-product wording.
    Full 1986 structure PDF access failed.
  snapshot_sha256: d63c731935cb1e962d341dde784eb769cff4daa8e85089bae32d943256a3e478
- evidence_id: synonym
  kind: primary_source
  reference: PMID:8135526; DOI:10.1128/AEM.60.2.752-755.1994
  locator: 403-synonym-p752.png printed p752 visually inspected, plus complete abstract
  accessed_at: '2026-10-21T15:31:30.859079Z'
  support: supports
  summary: The original study purifies staphylococcin 1580 from S. epidermidis 1580
    to homogeneity and identifies it with epidermin by amino-acid analysis, mass and
    N-terminal sequence. This supports the exact synonym without equating the 1580
    producer strain with Tü 3298.
  snapshot_sha256: 5334d7e26c88abbd4c9b754474493584b48f9f3bc2b7b107f70e244e4c98e418
- evidence_id: immunity
  kind: primary_source
  reference: PMID:8550476; DOI:10.1128/JB.178.2.531-536.1996
  locator: 403-core-8550476.json and403-PMC177688.html complete original abstract
  accessed_at: '2026-10-21T15:28:50.222127Z'
  support: supports
  summary: The original abstract reports increased epidermin tolerance in the S. carnosus
    cloning host carrying epiFEG, with the highest tolerance when epiQ is also present.
    Inactivation of any component loses immunity; all three complement a sensitive
    S. epidermidis mutant. It proposes an ABC-transporter explanation rather than
    directly demonstrating transport. This supports the bounded collective qualitative
    claim, but the precise TM300-derived constructs, purified reagent and Table 1
    details stated in prior curation were not independently reread from a full paper
    in this review.
  snapshot_sha256: cb40e29550e7a9e20763c96046308d5b89824fdb50d8f7ec2ef4f82bf38f8b5d
- evidence_id: accessions
  kind: authority
  reference: UniProtKB:Q54002; UniProtKB:Q54003; UniProtKB:Q54004; ENA:U29130; NCBITaxon:1281
  locator: 403-uniprot-Q54002.json throughQ54004;403-ena.txt;403-taxon.json
  accessed_at: '2026-10-21T15:28:47.457131Z'
  support: supports
  summary: Current UniProt records resolve respectively to epiF, epiE and epiG in
    S. epidermidis, cite PMID8550476 and specify donor strain Tue3298/plasmid pTue32.
    They are unreviewed sequence-reference records, not verified experimental alleles.
    ENA resolves U29130 as a secondary accession of U77778 and carries the same donor
    genes and paper. Taxon1281 resolves to S. carnosus, without representing the engineered
    derivative. Native prose preserves these limits.
  snapshot_sha256: 01c66174fb355d8d148e7b45b0f5a39ef019eec6dee2bd2cc30b4b3c9dcee502
- evidence_id: leads
  kind: primary_source
  reference: Five adopted ChEBI PMID leads and curated PMID8550476
  locator: 403-source-audit.json complete per-lead dispositions;403-core-*.json
  accessed_at: '2026-10-21T15:34:40Z'
  support: supports
  summary: All six complete abstracts were inspected. PMID1551392 concerns biosynthetic
    genetics and heterologous production;16586024 concerns clinical-isolate inhibition
    and in-vitro catheter adhesion in activity units, not a clinical outcome or mass-based
    MIC;3769923 concerns structure;8135526 establishes the synonym;8775972 is a biosynthesis
    review, retained as secondary context;8550476 is the exact immunity original.
    No single lead is promoted to support the entire record.
  snapshot_sha256: 62c808d75e0160b87bf81a91fba01f2ad79c20d9e5797a803c5256ad95b51075
- evidence_id: mechanism
  kind: primary_source
  reference: PMID:9791177; DOI:10.1046/j.1365-2958.1998.01065.x
  locator: 403-9791177.json complete original abstract
  accessed_at: '2026-10-21T15:32:30.463073Z'
  support: supports
  summary: Exact epidermin forms a complex with labeled lipid II and induces marker
    release in lipid II-containing liposomes. Intact-cell experiments include M. luteus
    and S. simulans with ramoplanin pretreatment. The result supports substrate-dependent
    membrane action; it is not direct binding to a protein enzyme.
  snapshot_sha256: 8df3a5f071cc3117020f30674da64f9470086d3e003c1abe50100f6d3c43271f
- evidence_id: activity
  kind: primary_source
  reference: PMID:16569864; DOI:10.1128/AAC.50.4.1449-1457.2006
  locator: 403-PMC1426925.html selected material/MIC/biochemical methods, Table1 and
    exact epidermin results
  accessed_at: '2026-10-21T15:32:30.460212Z'
  support: supports
  summary: The study purifies epidermin from Tü 3298 and confirms peptide mass and
    purity by electrospray MS. Table 1 gives epidermin MICs of 0.002, 0.15 and 0.002
    µM against M. flavus DSM 1790, S. simulans 22 and L. lactis subsp.cremoris HP
    under separately stated broth/incubation conditions. The exact epidermin experiments
    include pore activity in M. flavus and inhibition of lipid II synthesis/FemX reaction
    through substrate complexation. Gallidermin-only membrane-composition, kinetic
    and other strain results are not transferred to epidermin; the native record does
    not yet claim these quantitative rows.
  snapshot_sha256: 359ce55faf82b057037d8540ca4f571b43b00408b09b03227deb99544abb2555
- evidence_id: terms
  kind: authority
  reference: CHEBI:51026; CHEBI:71645; CHEBI:33281; CHEBI:33282
  locator: 403-term-51026.json;403-term-71645.json;403-term-33281.json;403-term-33282.json
  accessed_at: '2026-10-21T15:28:48.281738Z'
  support: supports
  summary: All four terms resolve to the stated macrocycle, type A lantibiotic, antimicrobial
    and antibacterial meanings. The native graph, original structural/biosynthetic
    evidence and exact antibacterial assays support their application. No universal
    Gram-positive susceptibility is inferred.
  snapshot_sha256: 3a835d3ee55fba207bf39152a3e5fb42766ea8bbf384e6301690adaf7700ecef
- evidence_id: patent
  kind: primary_source
  reference: patent:EP0350810
  locator: 403-patent.html description and producer/purification/assay passages, German
    text with supplied English translation
  accessed_at: '2026-10-21T15:28:47.457023Z'
  support: supports
  summary: The exact patent resolves to an epidermin production/isolation process.
    It specifies S. epidermidis DSM 3095, chromatography and HPLC purification and
    a diffusion assay using M. luteus ATCC 9341. It is appropriately a document link;
    this review does not infer current therapeutic approval or silently equate the
    deposited producer with a different named strain.
  snapshot_sha256: 3efc2909165082cb5e7701b3cbd475c19842a09fa7b89f542f6b43f3d20ac65f
- evidence_id: registry
  kind: authority
  reference: cas:99165-17-0; reaxys:11305595
  locator: 403-chebi.json database_accessions;403-cas.html;403-fetch3.json
  accessed_at: '2026-10-21T15:28:47.456448Z'
  support: context_only
  summary: Current ChEBI reproduces both adopted registry mappings. Direct CAS retrieval
    returned an application error without compound details, and Reaxys returned 403.
    Their exact public registry graphs therefore remain independently unverified;
    neither failed retrieval demonstrates a wrong identifier.
  snapshot_sha256: 1b038c7485793b61d457eaee9a79dbdf49dcc9f29dd0dcc9b990c368f07b4df5
- evidence_id: adapter
  kind: database
  reference: iModulonDB dataset catalog
  locator: 403-adapter-results.json
  accessed_at: '2026-10-21T15:34:40Z'
  support: context_only
  summary: Actual catalog discovery preceded mechanism searches. Neither S. carnosus
    nor S. epidermidis had a matching covered organism/dataset; no exact-host gene
    search or module summary was applicable. Catalog absence is not negative evidence
    about EpiFEG.
  snapshot_sha256: ca6cc68e64cb2924dfc870eb492fd39640e6d17d0d79a494172add05b237e102
- evidence_id: owners
  kind: database
  reference: Maintained ChEBI row and curator-owned resistance lane
  locator: 403-owner-append.json;403-raw-rows.json;403-source-audit.json
  accessed_at: '2026-10-21T15:34:40Z'
  support: supports
  summary: All 13 original input hashes remain unchanged. Definition, structure, names,
    parents, roles and links trace to the maintained ChEBI row/extractor/seeder; the
    later resistance assertion is curated directly in the native record. Ignored-inclusive
    searches of curation,scripts,data/raw and docs found no separate matching resistance
    overlay. Five histories remain ordered, and no REVIEWED status is asserted.
  snapshot_sha256: 62c808d75e0160b87bf81a91fba01f2ad79c20d9e5797a803c5256ad95b51075
- evidence_id: validation
  kind: validation
  reference: Native and supplementary checks
  locator: 403-focused-results.json;403-strict.tsv;403-authority-chemistry-initial.log;403-authority-chemistry.log;403-ledger.log
  accessed_at: '2026-10-21T15:34:40Z'
  support: supports
  summary: Native schema, strict terms and chemistry pass. The initial direct graph
    assertion fails on the InChI-reader tautomer; the final explicit comparison and
    source ledger pass. Scientific scope is assessed separately.
  snapshot_sha256: e08ea27afd8851458f64ac85053c50b6a005c7be839c742100df8f0fc70f1ced
- evidence_id: access
  kind: search
  reference: Bounded public epidermin source retrieval
  locator: 403-fetch.json through403-fetch5.json;403-curated-owner-hits.txt and403-local-hits.txt
    include ignored files
  accessed_at: '2026-10-21T15:34:40Z'
  support: context_only
  summary: Original immunity and structure full-text routes returned 403, 404 or 500;
    a nominal PMC PDF response was an HTML challenge, not a PDF. Complete abstracts,
    original synonym page, later primary mechanism main text, patent and sequence
    authorities were read at the stated levels.
  snapshot_sha256: f0bbe4f2f2f44c9f8d5dcde7539b5f3b12408c834f435c1781e1ae2084f663ed
  search_scope: 403-fetch.json through403-fetch5.json;403-curated-owner-hits.txt and403-local-hits.txt
    include ignored files
assessments:
- assessment_id: identity
  area: identity
  topic: Exact mature structure and naming
  outcome: supported
  summary: Official encodings and original structure/precursor evidence agree at the
    inspected level; no 21-versus 22 false defect.
  target_ids:
  - CHEBI:71659
  evidence_ids:
  - chemistry
  - structure
  - synonym
- assessment_id: grounding
  area: grounding
  topic: Class, roles and identifiers
  outcome: supported
  summary: Class/role terms and chemical source identity resolve; patent is correctly
    documentary.
  target_ids:
  - CHEBI:71659
  evidence_ids:
  - terms
  - chemistry
  - patent
- assessment_id: registry-limits
  area: grounding
  topic: Independent CAS/Reaxys detail
  outcome: unknown
  summary: Current ChEBI repeats the mappings, but exact registry details could not
    be independently read.
  target_ids:
  - CHEBI:71659
  evidence_ids:
  - registry
  - access
- assessment_id: immunity
  area: scope
  topic: Donor, host and collective phenotype
  outcome: supported
  summary: The native qualitative claim avoids single-gene sufficiency, donor/host
    conflation, experimental-allele assignment and unmeasured transport.
  target_ids:
  - CHEBI:71659
  evidence_ids:
  - record
  - immunity
  - accessions
- assessment_id: immunity-methods
  area: evidence
  topic: Exact full-method/Table 1 confirmation
  outcome: unknown
  summary: Original complete abstract corroborates the main claim; specific prior-curation
    TM300 and purified-reagent details were not independently reopened.
  target_ids:
  - CHEBI:71659
  evidence_ids:
  - immunity
  - access
- assessment_id: activity
  area: evidence
  topic: Antibacterial and mechanism evidence
  outcome: supported
  summary: Exact original assays support antibacterial role and substrate-associated
    membrane effects; gallidermin-only endpoints and direct protein binding are excluded.
  target_ids:
  - CHEBI:71659
  evidence_ids:
  - activity
  - mechanism
  - leads
- assessment_id: completeness
  area: completeness
  topic: Optional mechanism and susceptibility enrichment
  outcome: supported
  summary: No demonstrated required representation defect. Later curation could add
    exact lipid II and strain-specific assay evidence with full conditions and graph/claim-level
    citations.
  target_ids:
  - CHEBI:71659
  evidence_ids:
  - record
  - mechanism
  - activity
- assessment_id: ownership
  area: ownership
  topic: Source and curated claim preservation
  outcome: supported
  summary: Actual owners and five histories are recorded;13 initial hashes unchanged.
  target_ids:
  - CHEBI:71659
  evidence_ids:
  - owners
- assessment_id: validation
  area: schema
  topic: Native deterministic checks
  outcome: supported
  summary: Focused native checks pass; the supplemental tautomer assertion failure
    is transparently retained.
  target_ids:
  - CHEBI:71659
  evidence_ids:
  - validation
  - chemistry
findings: []
actions: []
limitations:
- The original 1986 structure paper was inspected at complete-abstract level because
  the full PDF returned 403. Full stereochemical reassignment from primary spectra
  was not performed; official graph concordance is distinguished from an independent
  structure determination.
- The original 1996 immunity full main text and Table 1 could not be independently
  retrieved. Its complete abstract and exact sequence records support the collective
  phenotype and donor/host distinction, but the prior-curation TM300 and purified-reagent
  details remain a bounded verification limit.
- CAS and Reaxys are reproduced by current ChEBI, but public direct detail retrieval
  failed. No identifier error is inferred from that access limit.
- Selected 2006 methods, Table 1 and exact epidermin results were read. Gallidermin-only
  results and complete supplementary figure inspection are not claimed. The 1998 mechanism
  paper was inspected at complete-abstract level.
- The initial supplemental direct structure comparison failed because the InChI reader
  generated an imidic-acid tautomer. The final audit records bond-order differences
  and preserves all tetrahedral parity; the native chemistry gate passed.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Standalone chemistry used the batch 019 interpreter against batch 041; native checks
  and source ledger used batch 041.
- 'Optional follow-up belongs in separately authorized curation: represent lipid II
  binding, context-specific membrane effects and exact published susceptibility rows
  without converting substrate sequestration into direct binding to FemX or another
  enzyme.'
- No native record, scientific status or immutable review bundle was edited by this
  review draft.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:71659
- https://doi.org/10.1111/j.1432-1033.1986.tb09933.x
- https://doi.org/10.1038/333276a0
- https://pmc.ncbi.nlm.nih.gov/articles/PMC201380/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC177688/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC1426925/
- https://patents.google.com/patent/EP0350810A2/en
tags:
- record-review
- epidermin
- lantibiotic
- qualitative-immunity
```
