# Review of CHEBI:28281 (5-methoxyindole-3-acetic acid)

- Review: 20261021T080138Z-chebi-28281-5-methoxyindole-3-acetic-acid-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T07:53:22Z
- Finished UTC: 2026-10-21T08:01:38Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The stored and current ChEBI SMILES omit indole [nH] and fail chemical parsing. Stored InChI, KEGG Molfile, PubChem structure and the precise [nH] repair candidate agree on the same neutral acid. A minor evidence-completeness finding identifies primary qualitative antibacterial activity against Agrobacterium tumefaciens. Full antimicrobial methods and a microbial mechanism remain unresolved; host Nrf2 effects do not establish an antimicrobial target.

## Scope And Provenance

Entire record, maintained source ownership, all structural encodings and ontology identifiers, external xref access, and primary exact-compound antibacterial and antifungal evidence with host-effect boundaries.

Selection: Path-ordered unreviewed queue index 053; exactly one record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:28281 | data/antibiotics/antibacterial/5-methoxyindole-3-acetic-acid.yaml | generated | 5-methoxyindole-3-acetic acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented per-record LinkML validation | passed | True | CHEBI:28281 | Exit 0; No issues found. |
| Documented per-record closed-schema validation | passed | True | CHEBI:28281 | Exit 0; one file, zero ERROR rows. |
| Independent structure and minted-identifier comparison | failed | False | CHEBI:28281 | Exit 1 because stored SMILES fails kekulization. Stored InChI, KEGG Molfile, PubChem SMILES and [nH] repair candidate agree on key, formula, neutral charge and masses; source-concept mint reproduces. |
| Current source term, parent, role and structure comparison | passed | False | CHEBI:28281 | Exit 0 for source reproduction, current term/parents/role, synonyms, InChI and xref-string assertions. The source SMILES is explicitly invalid; this does not substitute for the failed chemistry check. |
| Structured expression-context relevance | not_applicable | False | CHEBI:28281 | The current record contains no gene, protein, regulator, pathway, stress response or transcriptomic dataset annotation. Host Nrf2 appears only in uncurated literature context, not an existing assertion needing module validation. |
| Authoritative full QC | failed | True | CHEBI:28281 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:28281 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:28281 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:28281 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:28281 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:28281 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:28281 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:28281 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:28281 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Intended neutral acid and malformed aromatic encoding

identity: concern. Targets: CHEBI:28281.

InChI, external structures, formula and masses establish one intended neutral acid. The stored SMILES omits indole [nH], is chemically invalid and blocks native structural consistency.

### Names, direct parents and antibacterial role

grounding: supported. Targets: CHEBI:28281.

Current exact ChEBI term, synonyms and parents fit the intended acid. Primary Agrobacterium evidence supports the broad antibacterial filing.

### External identity references

grounding: unknown. Targets: CHEBI:28281.

KEGG structure agrees despite its acetate-form name. HMDB, MetaCyc, CAS and Reaxys exact target structure checks remain incomplete; source-string reproduction is not independent authority validation.

### Direct antibacterial evidence and assay boundaries

evidence: supported. Targets: CHEBI:28281.

The 2002 primary abstract directly supports qualitative A. tumefaciens activity. No numerical MIC, bacterial medium or strain can be inferred. Other compounds and fungal assays must remain distinct.

### Verified primary annotation opportunity

completeness: concern. Targets: CHEBI:28281.

A specific primary antibacterial result can support a bounded evidence annotation. Full methods are needed for quantitative activity; this minor enrichment is separate from the major structural defect.

### Antimicrobial mechanism versus host effects

scope: unknown. Targets: CHEBI:28281.

No exact microbial target or antimicrobial mechanism was established in the inspected sources. Host Nrf2 activation, antioxidant endpoints and 6-MBOA reverse-transcriptase inhibition do not fill that gap.

### Possible biological source versus structured producer

representation: unknown. Targets: CHEBI:28281.

No producer is asserted. Accessible host-study context offers a source lead, but this review has not verified complete production controls or biosynthetic methods, so it is not promoted to a producer claim.

### Resistance, clinical, graph and dataset annotations

representation: not_applicable. Targets: CHEBI:28281.

No such objects are asserted and none is required merely to fill optional schema fields. Neither broad source roles nor host protection establishes clinical antimicrobial efficacy.

### Generated source row and history

ownership: supported. Targets: CHEBI:28281.

Imported identity fields and mint reproduce; three seed/reseed events are internally consistent. Correct maintained source handling, then regenerate with validated history.

### Schema success with failed independent chemistry

schema: concern. Targets: CHEBI:28281.

Both focused native validators pass, but chemistry exits 1 for an actual malformed SMILES. Schema success cannot support native REVIEWED sign-off while this defect remains.

## Findings

### F1: Source-derived SMILES omits indole [nH] and cannot be parsed

major / open / confirmed; issue key: chebi-28281-invalid-smiles-missing-indole-hydrogen.

chemical_structure.smiles is COc1ccc2ncc(CC(=O)O)c2c1, which fails RDKit kekulization. Its indole pyrrolic nitrogen needs [nH]. The precise repair COc1ccc2[nH]cc(CC(=O)O)c2c1 matches the stored InChI/key/formula/masses and independent KEGG/PubChem structures. The adopted source row and current ChEBI/OLS share the defect.

### F2: Primary qualitative Agrobacterium activity is available for annotation

minor / open / confirmed; issue key: chebi-28281-primary-antibacterial-evidence-completeness.

The seeded record has no claim-level primary evidence despite an exact-compound antibacterial result in PMID:12106902. A bounded qualitative annotation is supported by its abstract; quantitative assay values and mechanism require further source access.

## Recommended Actions And Acceptance Checks

### A1

Correct the maintained source/generation route for CHEBI:28281 using a verified neutral indole encoding, then regenerate. Candidate: COc1ccc2[nH]cc(CC(=O)O)c2c1.

- Resolve the defective imported ChEBI structure through maintained source handling; do not patch only generated YAML or accept defective OLS SMILES solely because it is authoritative. Preserve the evidence and provenance of any correction.
- Require valid SMILES parsing and agreement with COCNDHOPIHDTHK-UHFFFAOYSA-N, C11H11NO3, charge 0, average mass 205.213 and monoisotopic mass 205.07389. Do not alter correct InChI/key/formula to accommodate invalid input.
- Regenerate only in an authorized curation pass, preserve validated curation history, and run native schema/strict, source reproduction, full-corpus integrity and QC gates before REVIEWED.

### A2

Curate the primary qualitative A. tumefaciens result at the level supported by PMID:12106902 and obtain full methods before quantitative claims.

- Attach the exact-compound primary citation with explicit abstract-only access and qualitative scope. Do not invent a bacterial MIC, isolate, dose, bacterial medium or incubation time; the stated potato-dextrose agar belongs to the fungal assay.
- Keep 6-MBOA fungal and HIV-1 reverse-transcriptase results and other pineal-indole antibacterial outcomes separate. Review the 2001 fungal observations independently before any broader activity-role curation.
- Leave microbial mechanism and target unresolved unless independently supported. Host Nrf2 and oxidative-injury outcomes are not antimicrobial target evidence; verify full production methods before any producer_organisms claim.
- Use the validated writer with curation history and complete required native gates before REVIEWED sign-off.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/5-methoxyindole-3-acetic-acid.yaml; Entire generated record | supports | Read definition, five synonyms, two parents, antibacterial role, complete structure, five xrefs, source concept and three seed/reseed events. No primary evidence, mode, target, activity observation, producer, resistance, clinical, graph or dataset object is asserted. |
| inventory | data/raw/chebi_antimicrobials.tsv; Full CHEBI:28281 row, manifest and ignored-inclusive maintained-input search | supports | Adopted row reproduces the malformed SMILES and matching InChI/key, formula, masses, synonyms, roles and xrefs. Ten imported PMID leads are bibliographic discovery inputs, not automatic claim evidence. No exact curator override was found in the ignored-inclusive maintained-input search. |
| ownership | scripts/extract_source_inventory.py; ChEBI structure import, scripts/seed_from_sources.py structure_from_chebi and curator merge | supports | The source extractor copies the source SMILES string and the seeder reproduces it. The correction belongs in maintained source handling and reproducible regeneration; new primary annotations belong to curator-owned fields with validated history. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:28281; 053-chebi.html, current visible SMILES, InChI and identity fields | supports | Current ChEBI also displays COc1ccc2ncc(CC(=O)O)c2c1. Its missing pyrrolic [nH] is inconsistent with its own chemically valid InChI and neutral C11H11NO3 entity; database repetition is not a chemical validity check. |
| ontology | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28281; 053-ols.json, 053-parents.json and 053-has_role.json | supports | The non-obsolete exact term has indole-3-acetic-acids and aromatic-ether parents and antibacterial-agent role. Five native synonyms and all five xref strings match. OLS repeats the defective SMILES while retaining the correct InChI/key. |
| kegg | https://rest.kegg.jp/get/C05660; 053-kegg.html and 053-keggmol.html, plain-text downloads despite suffix | supports | KEGG C05660 names 5-methoxyindoleacetate but its downloaded Molfile represents the same neutral acid: COCNDHOPIHDTHK-UHFFFAOYSA-N, C11H11NO3 and charge zero. Name wording alone does not imply a charge mismatch. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/18986/property/InChI,InChIKey,MolecularFormula,CanonicalSMILES/JSON; 053-pubchem.json, CID 18986 structure properties | supports | Independent valid PubChem SMILES, InChI/key and formula match the intended neutral acid and the [nH] repair candidate. |
| xref-limits | HMDB:HMDB0004096; MetaCyc:CPD-12020; cas:3471-31-6; reaxys:187161; 053-fetch-results.json and public authority responses | context_only | HMDB XML returned 403. MetaCyc returned an account-access page, CAS a JavaScript application shell; neither furnished a readable target structure. Reaxys target was not independently resolved. Source xref strings reproduce, but exact external target verification remains incomplete. |
| primary2002 | PMID:12106902; DOI:10.1016/S1532-0456(02)00071-6; abstract in 053-primarycore.json | supports | The study directly compares pineal indoles against Agrobacterium tumefaciens and reports 5-methoxyindole-3-acetic acid as most potent among the compounds tested. The accessible abstract supplies no numerical bacterial MIC, strain or bacterial assay method. Potato-dextrose agar describes the fungal assay. The strongest fungal and HIV-1 reverse-transcriptase results belong to 6-MBOA, a different compound. |
| primary2001 | PMID:11701394; DOI:10.1016/S1532-0456(01)00264-2; abstract in 053-primarycore.json | context_only | The abstract attributes antifungal effects against Mycosphaerella arachidicola, Botrytis cinerea and Physalospora piricola to 5-methoxyindole-3-acetic acid and 6-MBOA. Named Proteus vulgaris antibacterial activity belongs to 6-MBOA and Staphylococcus aureus/Bacillus subtilis activity to 5-methoxytryptamine. Those outcomes cannot be transferred to this record; the different bacterial panel does not refute the later Agrobacterium result. |
| host-context | https://pmc.ncbi.nlm.nih.gov/articles/PMC7329068/; 2020 Gut-Resident Lactobacilli Activate Hepatic Nrf2 and Protect Against Oxidative Liver Injury; accessible indexed abstract/selected narrative, full XML failed | context_only | This primary study concerns host hepatic Nrf2 activation and protection against oxidative injury, with a Lactobacillus-associated 5-methoxyindoleacetic-acid source claim. It is not direct evidence of a microbial antimicrobial target. Producer attribution needs its complete methods and controls before structured curation; no biosynthetic pathway or producer object is added here. |
| chemistry | RDKit and hashlib calculations; 053-chemistry.py and 053-chemistry.json | supports | Stored SMILES fails kekulization. InChI, PubChem SMILES, KEGG Molfile and candidate COc1ccc2[nH]cc(CC(=O)O)c2c1 yield the recorded InChIKey, formula, neutral charge and masses. Deterministic source-concept mint agrees. Script exits 1 specifically for the stored-SMILES failure. |
| source-check | Focused current-source assertions; 053-source-check.py and 053-source-check.json | supports | Term, non-obsolete parents and role, synonyms, InChI and xref strings agree. Both current source displays preserve the malformed SMILES, explicitly recognized as invalid rather than counted as chemically verified. |
| validation | just validate; just validate-strict; Actual isolated batch-006 executions; 053-strict.tsv | supports | Both documented per-record validators exited 0. Strict validation scanned one record with zero ERROR rows. These schema gates do not detect the chemical parsing defect. |
| search | Ignored-inclusive local and bounded public source discovery; 053-local-hits.txt and exact-name public searches | context_only | Identity and exact-compound primary studies were prioritized. Current source methods and chemical checks establish a specific defect; the literature search does not establish absence of a microbial mechanism in all publications. |
| all-adopted-leads | PMID:11459072; PMID:11701394; PMID:12106902; PMID:15950974; PMID:16141651; PMID:16318213; PMID:16512423; PMID:19185928; PMID:2423155; PMID:2446428; 053-allcore.json and 053-lead-dispositions.json; all ten complete abstracts inspected | context_only | All ten adopted PMID records resolve and their abstracts were read. The eight beyond the two antimicrobial papers concern rat/trout pineal regulation (11459072,15950974,19185928), analytical methods (16318213,16512423), rat embryo effects (16141651), mouse transplacental tumor induction (2423155), or urinary excretion in cancer patients (2446428). They do not establish an antimicrobial target, clinical antimicrobial efficacy or safe therapeutic use. |

## Limits And Additional Notes

- All ten adopted PMID records and complete abstracts were inspected through Europe PMC core metadata. The two antimicrobial papers remain abstract-only: complete methods, quantitative tables and supplements were not retrieved; the 2002 publisher endpoint returned 403. No numerical MIC/MBC or direct microbial target is asserted.
- The 2020 host study was only inspected in accessible indexed abstract/selected narrative; fullTextXML returned HTTP 500 and direct PMC access encountered a browser challenge. Its biological-source claim was not promoted to a structured producer assertion.
- HMDB XML returned 403; MetaCyc returned an account-access page, CAS an application shell, and Reaxys target identity was not independently resolved. Source-string agreement is narrower than direct xref target validation.
- Current ChEBI and OLS repeat the same malformed SMILES. The independent chemistry check intentionally fails; schema and strict-schema success do not resolve it.
- This bounded review is not an exhaustive literature inventory. Native REVIEWED sign-off is blocked by the major structural defect and remains incomplete pending evidence curation, unresolved checks and required gates.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Only scratch review artifacts were written. No native record, maintained input, generated artifact or curation history was modified.
- Coordinator independently confirmed that the native SMILES fails parsing and the exact [nH] candidate gives COCNDHOPIHDTHK-UHFFFAOYSA-N. An initial scratch display used an incorrect metadata-key name and raised KeyError; rerunning with the native standard_inchi_key field confirmed the result without changing any input.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T080138Z-chebi-28281-5-methoxyindole-3-acetic-acid-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of CHEBI:28281 (5-methoxyindole-3-acetic acid)
started_at: '2026-10-21T07:53:22Z'
finished_at: '2026-10-21T08:01:38Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Read-only review by an agent uninvolved in authoring the generated
    record; exact target and maintained input hashes captured before assessment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Major invalid source-derived SMILES blocks native REVIEWED structural
  consistency; neutral acid identity and antibacterial classification supported
scientific_review: true
summary: The stored and current ChEBI SMILES omit indole [nH] and fail chemical parsing.
  Stored InChI, KEGG Molfile, PubChem structure and the precise [nH] repair candidate
  agree on the same neutral acid. A minor evidence-completeness finding identifies
  primary qualitative antibacterial activity against Agrobacterium tumefaciens. Full
  antimicrobial methods and a microbial mechanism remain unresolved; host Nrf2 effects
  do not establish an antimicrobial target.
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
  - path: data/antibiotics/antibacterial/5-methoxyindole-3-acetic-acid.yaml
    sha256: 5f5b82ae5435d385db626d37a051a2f9d30395cda08d1112228c724f60949bda
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
  description: Entire record, maintained source ownership, all structural encodings
    and ontology identifiers, external xref access, and primary exact-compound antibacterial
    and antifungal evidence with host-effect boundaries.
  selection: Path-ordered unreviewed queue index 053; exactly one record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:28281
targets:
- target_id: CHEBI:28281
  path: data/antibiotics/antibacterial/5-methoxyindole-3-acetic-acid.yaml
  label: 5-methoxyindole-3-acetic acid
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
  - CHEBI:28281
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/5-methoxyindole-3-acetic-acid.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Documented per-record closed-schema validation
  status: passed
  required: true
  summary: Exit 0; one file, zero ERROR rows.
  target_ids:
  - CHEBI:28281
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/5-methoxyindole-3-acetic-acid.yaml --out /private/tmp/am-review-session/053-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: chemistry
  name: Independent structure and minted-identifier comparison
  status: failed
  required: false
  summary: Exit 1 because stored SMILES fails kekulization. Stored InChI, KEGG Molfile,
    PubChem SMILES and [nH] repair candidate agree on key, formula, neutral charge
    and masses; source-concept mint reproduces.
  target_ids:
  - CHEBI:28281
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/053-chemistry.py
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: source-check
  name: Current source term, parent, role and structure comparison
  status: passed
  required: false
  summary: Exit 0 for source reproduction, current term/parents/role, synonyms, InChI
    and xref-string assertions. The source SMILES is explicitly invalid; this does
    not substitute for the failed chemistry check.
  target_ids:
  - CHEBI:28281
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache uv run python
    /private/tmp/am-review-session/053-source-check.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ontology
  - source-check
- check_id: imodulondb
  name: Structured expression-context relevance
  status: not_applicable
  required: false
  summary: The current record contains no gene, protein, regulator, pathway, stress
    response or transcriptomic dataset annotation. Host Nrf2 appears only in uncurated
    literature context, not an existing assertion needing module validation.
  target_ids:
  - CHEBI:28281
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:28281
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
  - CHEBI:28281
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
  - CHEBI:28281
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
  - CHEBI:28281
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
  - CHEBI:28281
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
  - CHEBI:28281
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
  - CHEBI:28281
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
  - CHEBI:28281
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
  - CHEBI:28281
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/5-methoxyindole-3-acetic-acid.yaml
  locator: Entire generated record
  accessed_at: '2026-10-21T07:57:52Z'
  support: supports
  summary: Read definition, five synonyms, two parents, antibacterial role, complete
    structure, five xrefs, source concept and three seed/reseed events. No primary
    evidence, mode, target, activity observation, producer, resistance, clinical,
    graph or dataset object is asserted.
- evidence_id: inventory
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Full CHEBI:28281 row, manifest and ignored-inclusive maintained-input search
  accessed_at: '2026-10-21T07:57:52Z'
  support: supports
  summary: Adopted row reproduces the malformed SMILES and matching InChI/key, formula,
    masses, synonyms, roles and xrefs. Ten imported PMID leads are bibliographic discovery
    inputs, not automatic claim evidence. No exact curator override was found in the
    ignored-inclusive maintained-input search.
- evidence_id: ownership
  kind: record_content
  reference: scripts/extract_source_inventory.py
  locator: ChEBI structure import, scripts/seed_from_sources.py structure_from_chebi
    and curator merge
  accessed_at: '2026-10-21T07:57:52Z'
  support: supports
  summary: The source extractor copies the source SMILES string and the seeder reproduces
    it. The correction belongs in maintained source handling and reproducible regeneration;
    new primary annotations belong to curator-owned fields with validated history.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:28281
  locator: 053-chebi.html, current visible SMILES, InChI and identity fields
  accessed_at: '2026-10-21T07:57:52Z'
  support: supports
  summary: Current ChEBI also displays COc1ccc2ncc(CC(=O)O)c2c1. Its missing pyrrolic
    [nH] is inconsistent with its own chemically valid InChI and neutral C11H11NO3
    entity; database repetition is not a chemical validity check.
  snapshot_sha256: 4d1034d9d2cf0e024dbde9c015f91d9543a5d6f9ec26f1d373c6354ddb910515
- evidence_id: ontology
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28281
  locator: 053-ols.json, 053-parents.json and 053-has_role.json
  accessed_at: '2026-10-21T07:57:52Z'
  support: supports
  summary: The non-obsolete exact term has indole-3-acetic-acids and aromatic-ether
    parents and antibacterial-agent role. Five native synonyms and all five xref strings
    match. OLS repeats the defective SMILES while retaining the correct InChI/key.
  snapshot_sha256: 8164ab6ebe286c28f46227590eca910b0856e4917da1ed29543dddb77bc5cc6b
- evidence_id: kegg
  kind: database
  reference: https://rest.kegg.jp/get/C05660
  locator: 053-kegg.html and 053-keggmol.html, plain-text downloads despite suffix
  accessed_at: '2026-10-21T07:57:52Z'
  support: supports
  summary: 'KEGG C05660 names 5-methoxyindoleacetate but its downloaded Molfile represents
    the same neutral acid: COCNDHOPIHDTHK-UHFFFAOYSA-N, C11H11NO3 and charge zero.
    Name wording alone does not imply a charge mismatch.'
  snapshot_sha256: 70ff4dcfe2535b76479267ac08c4556495553d290d288e94cf8d2da7414971b1
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/18986/property/InChI,InChIKey,MolecularFormula,CanonicalSMILES/JSON
  locator: 053-pubchem.json, CID 18986 structure properties
  accessed_at: '2026-10-21T07:57:52Z'
  support: supports
  summary: Independent valid PubChem SMILES, InChI/key and formula match the intended
    neutral acid and the [nH] repair candidate.
  snapshot_sha256: 19ccb7661605450461f0a7a61678d3347271d8890e180fec76cf0e410d2f5911
- evidence_id: xref-limits
  kind: database
  reference: HMDB:HMDB0004096; MetaCyc:CPD-12020; cas:3471-31-6; reaxys:187161
  locator: 053-fetch-results.json and public authority responses
  accessed_at: '2026-10-21T07:57:52Z'
  support: context_only
  summary: HMDB XML returned 403. MetaCyc returned an account-access page, CAS a JavaScript
    application shell; neither furnished a readable target structure. Reaxys target
    was not independently resolved. Source xref strings reproduce, but exact external
    target verification remains incomplete.
  snapshot_sha256: 6409a449dee9d75ffcc03f52f316e8a1f7dd5b359c27e95da913c7d143f6932e
- evidence_id: primary2002
  kind: primary_source
  reference: PMID:12106902
  locator: DOI:10.1016/S1532-0456(02)00071-6; abstract in 053-primarycore.json
  accessed_at: '2026-10-21T07:57:52Z'
  support: supports
  summary: The study directly compares pineal indoles against Agrobacterium tumefaciens
    and reports 5-methoxyindole-3-acetic acid as most potent among the compounds tested.
    The accessible abstract supplies no numerical bacterial MIC, strain or bacterial
    assay method. Potato-dextrose agar describes the fungal assay. The strongest fungal
    and HIV-1 reverse-transcriptase results belong to 6-MBOA, a different compound.
  snapshot_sha256: 9170f509235dff8951246637be177d7134e744bec1011335ee1060f0f6d97930
- evidence_id: primary2001
  kind: primary_source
  reference: PMID:11701394
  locator: DOI:10.1016/S1532-0456(01)00264-2; abstract in 053-primarycore.json
  accessed_at: '2026-10-21T07:57:52Z'
  support: context_only
  summary: The abstract attributes antifungal effects against Mycosphaerella arachidicola,
    Botrytis cinerea and Physalospora piricola to 5-methoxyindole-3-acetic acid and
    6-MBOA. Named Proteus vulgaris antibacterial activity belongs to 6-MBOA and Staphylococcus
    aureus/Bacillus subtilis activity to 5-methoxytryptamine. Those outcomes cannot
    be transferred to this record; the different bacterial panel does not refute the
    later Agrobacterium result.
  snapshot_sha256: 9170f509235dff8951246637be177d7134e744bec1011335ee1060f0f6d97930
- evidence_id: host-context
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC7329068/
  locator: 2020 Gut-Resident Lactobacilli Activate Hepatic Nrf2 and Protect Against
    Oxidative Liver Injury; accessible indexed abstract/selected narrative, full XML
    failed
  accessed_at: '2026-10-21T07:57:52Z'
  support: context_only
  summary: This primary study concerns host hepatic Nrf2 activation and protection
    against oxidative injury, with a Lactobacillus-associated 5-methoxyindoleacetic-acid
    source claim. It is not direct evidence of a microbial antimicrobial target. Producer
    attribution needs its complete methods and controls before structured curation;
    no biosynthetic pathway or producer object is added here.
- evidence_id: chemistry
  kind: validation
  reference: RDKit and hashlib calculations
  locator: 053-chemistry.py and 053-chemistry.json
  accessed_at: '2026-10-21T07:57:52Z'
  support: supports
  summary: Stored SMILES fails kekulization. InChI, PubChem SMILES, KEGG Molfile and
    candidate COc1ccc2[nH]cc(CC(=O)O)c2c1 yield the recorded InChIKey, formula, neutral
    charge and masses. Deterministic source-concept mint agrees. Script exits 1 specifically
    for the stored-SMILES failure.
  snapshot_sha256: 98e97189477ed70ba7e3837ba352c016cc9b549fd37f689d8e9d3427a9e68444
- evidence_id: source-check
  kind: validation
  reference: Focused current-source assertions
  locator: 053-source-check.py and 053-source-check.json
  accessed_at: '2026-10-21T07:57:52Z'
  support: supports
  summary: Term, non-obsolete parents and role, synonyms, InChI and xref strings agree.
    Both current source displays preserve the malformed SMILES, explicitly recognized
    as invalid rather than counted as chemically verified.
  snapshot_sha256: 43e916b18ae17be7ccc02cd1ffec5be4b6a2f5fbedf263152a3b659650091c6b
- evidence_id: validation
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual isolated batch-006 executions; 053-strict.tsv
  accessed_at: '2026-10-21T07:57:52Z'
  support: supports
  summary: Both documented per-record validators exited 0. Strict validation scanned
    one record with zero ERROR rows. These schema gates do not detect the chemical
    parsing defect.
- evidence_id: search
  kind: search
  reference: Ignored-inclusive local and bounded public source discovery
  locator: 053-local-hits.txt and exact-name public searches
  accessed_at: '2026-10-21T07:57:52Z'
  support: context_only
  summary: Identity and exact-compound primary studies were prioritized. Current source
    methods and chemical checks establish a specific defect; the literature search
    does not establish absence of a microbial mechanism in all publications.
  search_scope: prepare.py 53 ran rg --no-ignore --hidden excluding only .git and
    .venv before judgment. Follow-up searched maintained data/curation/conf for CHEBI:28281,
    minted identity, exact name and aliases. Public queries covered exact name, antibacterial
    activity, Agrobacterium, antifungal activity, mechanism and host Nrf2; inspected
    current ChEBI/OLS, KEGG and PubChem structures, two primary abstracts and bounded
    host-study context.
- evidence_id: all-adopted-leads
  kind: primary_source
  reference: PMID:11459072; PMID:11701394; PMID:12106902; PMID:15950974; PMID:16141651;
    PMID:16318213; PMID:16512423; PMID:19185928; PMID:2423155; PMID:2446428
  locator: 053-allcore.json and 053-lead-dispositions.json; all ten complete abstracts
    inspected
  accessed_at: '2026-10-21T08:00:48Z'
  support: context_only
  summary: All ten adopted PMID records resolve and their abstracts were read. The
    eight beyond the two antimicrobial papers concern rat/trout pineal regulation
    (11459072,15950974,19185928), analytical methods (16318213,16512423), rat embryo
    effects (16141651), mouse transplacental tumor induction (2423155), or urinary
    excretion in cancer patients (2446428). They do not establish an antimicrobial
    target, clinical antimicrobial efficacy or safe therapeutic use.
  snapshot_sha256: 553196e3517393c80a25e0060aea7de4981b6929967ef95cdb5cd858e963d0ff
assessments:
- assessment_id: identity
  area: identity
  topic: Intended neutral acid and malformed aromatic encoding
  outcome: concern
  summary: InChI, external structures, formula and masses establish one intended neutral
    acid. The stored SMILES omits indole [nH], is chemically invalid and blocks native
    structural consistency.
  target_ids:
  - CHEBI:28281
  evidence_ids:
  - record
  - chebi
  - chemistry
  - pubchem
  - kegg
- assessment_id: grounding
  area: grounding
  topic: Names, direct parents and antibacterial role
  outcome: supported
  summary: Current exact ChEBI term, synonyms and parents fit the intended acid. Primary
    Agrobacterium evidence supports the broad antibacterial filing.
  target_ids:
  - CHEBI:28281
  evidence_ids:
  - ontology
  - primary2002
  - source-check
- assessment_id: xrefs
  area: grounding
  topic: External identity references
  outcome: unknown
  summary: KEGG structure agrees despite its acetate-form name. HMDB, MetaCyc, CAS
    and Reaxys exact target structure checks remain incomplete; source-string reproduction
    is not independent authority validation.
  target_ids:
  - CHEBI:28281
  evidence_ids:
  - kegg
  - xref-limits
- assessment_id: evidence
  area: evidence
  topic: Direct antibacterial evidence and assay boundaries
  outcome: supported
  summary: The 2002 primary abstract directly supports qualitative A. tumefaciens
    activity. No numerical MIC, bacterial medium or strain can be inferred. Other
    compounds and fungal assays must remain distinct.
  target_ids:
  - CHEBI:28281
  evidence_ids:
  - primary2002
  - primary2001
- assessment_id: completeness
  area: completeness
  topic: Verified primary annotation opportunity
  outcome: concern
  summary: A specific primary antibacterial result can support a bounded evidence
    annotation. Full methods are needed for quantitative activity; this minor enrichment
    is separate from the major structural defect.
  target_ids:
  - CHEBI:28281
  evidence_ids:
  - record
  - primary2002
- assessment_id: mechanism
  area: scope
  topic: Antimicrobial mechanism versus host effects
  outcome: unknown
  summary: No exact microbial target or antimicrobial mechanism was established in
    the inspected sources. Host Nrf2 activation, antioxidant endpoints and 6-MBOA
    reverse-transcriptase inhibition do not fill that gap.
  target_ids:
  - CHEBI:28281
  evidence_ids:
  - primary2002
  - primary2001
  - host-context
- assessment_id: producer
  area: representation
  topic: Possible biological source versus structured producer
  outcome: unknown
  summary: No producer is asserted. Accessible host-study context offers a source
    lead, but this review has not verified complete production controls or biosynthetic
    methods, so it is not promoted to a producer claim.
  target_ids:
  - CHEBI:28281
  evidence_ids:
  - record
  - host-context
- assessment_id: optional
  area: representation
  topic: Resistance, clinical, graph and dataset annotations
  outcome: not_applicable
  summary: No such objects are asserted and none is required merely to fill optional
    schema fields. Neither broad source roles nor host protection establishes clinical
    antimicrobial efficacy.
  target_ids:
  - CHEBI:28281
  evidence_ids:
  - record
  - host-context
- assessment_id: provenance
  area: ownership
  topic: Generated source row and history
  outcome: supported
  summary: Imported identity fields and mint reproduce; three seed/reseed events are
    internally consistent. Correct maintained source handling, then regenerate with
    validated history.
  target_ids:
  - CHEBI:28281
  evidence_ids:
  - record
  - inventory
  - ownership
  - chemistry
- assessment_id: schema-assessment
  area: schema
  topic: Schema success with failed independent chemistry
  outcome: concern
  summary: Both focused native validators pass, but chemistry exits 1 for an actual
    malformed SMILES. Schema success cannot support native REVIEWED sign-off while
    this defect remains.
  target_ids:
  - CHEBI:28281
  evidence_ids:
  - validation
  - chemistry
findings:
- finding_id: F1
  issue_key: chebi-28281-invalid-smiles-missing-indole-hydrogen
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Source-derived SMILES omits indole [nH] and cannot be parsed
  description: chemical_structure.smiles is COc1ccc2ncc(CC(=O)O)c2c1, which fails
    RDKit kekulization. Its indole pyrrolic nitrogen needs [nH]. The precise repair
    COc1ccc2[nH]cc(CC(=O)O)c2c1 matches the stored InChI/key/formula/masses and independent
    KEGG/PubChem structures. The adopted source row and current ChEBI/OLS share the
    defect.
  target_ids:
  - CHEBI:28281
  field_paths:
  - chemical_structure.smiles
  evidence_ids:
  - record
  - inventory
  - chebi
  - chemistry
  - kegg
  - pubchem
  rule_id: 'review-checklist: Chemical identity and structural consistency'
  native_severity: major core structure inconsistency blocking native REVIEWED
  normalization_reason: A core structural encoding is invalid, but independent representations
    establish the intended exact entity. This is a repairable major defect rather
    than an unresolved identity blocker.
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
  issue_key: chebi-28281-primary-antibacterial-evidence-completeness
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Primary qualitative Agrobacterium activity is available for annotation
  description: The seeded record has no claim-level primary evidence despite an exact-compound
    antibacterial result in PMID:12106902. A bounded qualitative annotation is supported
    by its abstract; quantitative assay values and mechanism require further source
    access.
  target_ids:
  - CHEBI:28281
  field_paths:
  - evidence
  - activity_spectrum
  - discussions
  evidence_ids:
  - record
  - primary2002
  - primary2001
  rule_id: 'review-checklist: Evidence standard, Activity and Audit'
  native_severity: minor actionable primary-evidence completeness gap
  normalization_reason: A specific verified primary result is available. Empty optional
    fields alone are not an error and the abstract does not justify numerical or target
    claims.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/5-methoxyindole-3-acetic-acid.yaml
    role: Curator-owned evidence, activity_spectrum and discussions through validated
      writer and history
actions:
- action_id: A1
  description: 'Correct the maintained source/generation route for CHEBI:28281 using
    a verified neutral indole encoding, then regenerate. Candidate: COc1ccc2[nH]cc(CC(=O)O)c2c1.'
  finding_ids:
  - F1
  target_ids:
  - CHEBI:28281
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
  acceptance_checks:
  - Resolve the defective imported ChEBI structure through maintained source handling;
    do not patch only generated YAML or accept defective OLS SMILES solely because
    it is authoritative. Preserve the evidence and provenance of any correction.
  - Require valid SMILES parsing and agreement with COCNDHOPIHDTHK-UHFFFAOYSA-N, C11H11NO3,
    charge 0, average mass 205.213 and monoisotopic mass 205.07389. Do not alter correct
    InChI/key/formula to accommodate invalid input.
  - Regenerate only in an authorized curation pass, preserve validated curation history,
    and run native schema/strict, source reproduction, full-corpus integrity and QC
    gates before REVIEWED.
- action_id: A2
  description: Curate the primary qualitative A. tumefaciens result at the level supported
    by PMID:12106902 and obtain full methods before quantitative claims.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:28281
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/5-methoxyindole-3-acetic-acid.yaml
    role: Curator-owned evidence, activity_spectrum and discussions through validated
      writer and history
  acceptance_checks:
  - Attach the exact-compound primary citation with explicit abstract-only access
    and qualitative scope. Do not invent a bacterial MIC, isolate, dose, bacterial
    medium or incubation time; the stated potato-dextrose agar belongs to the fungal
    assay.
  - Keep 6-MBOA fungal and HIV-1 reverse-transcriptase results and other pineal-indole
    antibacterial outcomes separate. Review the 2001 fungal observations independently
    before any broader activity-role curation.
  - Leave microbial mechanism and target unresolved unless independently supported.
    Host Nrf2 and oxidative-injury outcomes are not antimicrobial target evidence;
    verify full production methods before any producer_organisms claim.
  - Use the validated writer with curation history and complete required native gates
    before REVIEWED sign-off.
limitations:
- 'All ten adopted PMID records and complete abstracts were inspected through Europe
  PMC core metadata. The two antimicrobial papers remain abstract-only: complete methods,
  quantitative tables and supplements were not retrieved; the 2002 publisher endpoint
  returned 403. No numerical MIC/MBC or direct microbial target is asserted.'
- The 2020 host study was only inspected in accessible indexed abstract/selected narrative;
  fullTextXML returned HTTP 500 and direct PMC access encountered a browser challenge.
  Its biological-source claim was not promoted to a structured producer assertion.
- HMDB XML returned 403; MetaCyc returned an account-access page, CAS an application
  shell, and Reaxys target identity was not independently resolved. Source-string
  agreement is narrower than direct xref target validation.
- Current ChEBI and OLS repeat the same malformed SMILES. The independent chemistry
  check intentionally fails; schema and strict-schema success do not resolve it.
- This bounded review is not an exhaustive literature inventory. Native REVIEWED sign-off
  is blocked by the major structural defect and remains incomplete pending evidence
  curation, unresolved checks and required gates.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Only scratch review artifacts were written. No native record, maintained input,
  generated artifact or curation history was modified.
- Coordinator independently confirmed that the native SMILES fails parsing and the
  exact [nH] candidate gives COCNDHOPIHDTHK-UHFFFAOYSA-N. An initial scratch display
  used an incorrect metadata-key name and raised KeyError; rerunning with the native
  standard_inchi_key field confirmed the result without changing any input.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:28281
- https://rest.kegg.jp/get/C05660
- https://pubchem.ncbi.nlm.nih.gov/compound/18986
- https://doi.org/10.1016/S1532-0456(02)00071-6
- https://doi.org/10.1016/S1532-0456(01)00264-2
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7329068/
tags:
- record-review
- indole
- invalid-smiles
- source-owned-correction
- primary-activity
- host-effect-scope
```
