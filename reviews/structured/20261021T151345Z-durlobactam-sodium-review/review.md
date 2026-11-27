# Review of durlobactam sodium

- Review: 20261021T151345Z-durlobactam-sodium-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:52:10Z
- Finished UTC: 2026-10-21T15:13:45Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Eight chemical encodings support one durlobactam anion with one sodium counterion, matching the official named ingredient and both configured carbon centers. The primary experimental literature supports the durlobactam moiety as a serine beta-lactamase inhibitor, while the regulatory indication belongs to the sulbactam-containing product. No confirmed native defect was established. DrugBank access and the sole adopted citation full text remain limited; an initial direct graph comparison failed on an InChI-read tautomer and was resolved with explicit stereo-preserving comparison. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole SEEDED, EXACT sodium-salt record: definition, two synonyms, organic-sodium-salt parent, antibacterial role, complete chemical structure, exact CAS, two drug-context identifiers, source concept and four histories. Sole adopted/current PMID37452667 disposition recorded.

Selection: Queue 382 in isolated batch 039. Initial thirteen hashes preserved; actual maintained ChEBI owners were already included and verified before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:229544 | data/antibiotics/antibacterial/durlobactam-sodium.yaml | generated | durlobactam sodium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native schema | passed | True | CHEBI:229544 | Exit 0. |
| Native strict terms | passed | True | CHEBI:229544 | Exit 0; no ERROR rows. |
| Native molecular consistency | passed | False | CHEBI:229544 | Native formula, key, mass and charge check passes. |
| Initial direct graph comparison | failed | False | CHEBI:229544 | Executed exit 1 at native-inchi: RDKit reads an imidate/proton-placement tautomer despite the identical Standard InChIKey. Retained as a failed supplemental check; not an unavailable gate or a demonstrated wrong molecule. |
| Explicit formula-unit and stereo comparison | passed | False | CHEBI:229544 | Eight encodings match after explicitly recorded common fragment protonation/tautomer comparison. Original composition, two ionic components, charges, key, masses and configured-carbon parity checked before normalization. |
| Structured mechanism context before primary follow-up | passed | False | CHEBI:229544 | Dataset discovery and representative A. baumannii/E. coli gene searches exit 0; no iModulon hit requiring summary. |
| Source, identifiers, citation and history ledger | passed | False | CHEBI:229544 | Thirteen hashes unchanged; all source fields/identifier placements, sole adopted/current citation and four histories checked. |
| Authoritative full QC | failed | True | CHEBI:229544 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:229544 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:229544 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:229544 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:229544 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:229544 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:229544 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:229544 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:229544 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact monosodium salt

identity: supported. Targets: CHEBI:229544.

Independent authorities and current official ingredient description agree, with two ionic components retained and configured carbon parity mapped.

### Definition, names, parent and role

nomenclature: supported. Targets: CHEBI:229544.

The monosodium description and sodium-qualified ETX2514 alias fit the exact graph. Antibacterial-drug role is consistent with its inhibitor ingredient scope.

### Moiety mechanism and assay boundaries

evidence: supported. Targets: CHEBI:229544.

Original enzyme/structure data support the active moiety; experiment salt is not explicitly established. No combination MIC is transferred as sodium-salt monotherapy activity.

### DrugBank and adopted full-text access

identity: unknown. Targets: CHEBI:229544.

DrugBank contents and the sole adopted citation full text remain unverified; no contradiction is inferred.

### Optional mechanism and clinical enrichment

completeness: supported. Targets: CHEBI:229544.

No missing mandatory representation was established for this SEEDED record. Any later mechanism/clinical addition should preserve parent-versus-salt and combination scope.

### Owners, source fields and histories

provenance: supported. Targets: CHEBI:229544.

Thirteen inputs and all native source fields, the citation and four histories were checked.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/durlobactam-sodium.yaml; Whole native YAML | supports | One exact monosodium salt with two chemical aliases. No native molecular-target, resistance, MIC, producer, clinical-status assertion or causal-graph objects are populated; the record does not assert standalone treatment efficacy. |
| chemistry | CHEBI:229544; UNII:F78MDZ9CW9; PubChem CID89851851; KEGG D11592; 382-chebi.json/.mol; 382-gsrs.json; 382-pubchem.json; 382-kegg.txt/.mol; 382-authority-chemistry.json | supports | Eight encodings agree on C8H10N3NaO6S, net zero charge, one organic anion plus one sodium cation and WHHNOICWPZIYKI-IBTYICNHSA-M. The two configured carbon centers map reciprocally with chirality retained. GSRS can additionally label the constrained bridgehead nitrogen, whereas the Standard InChI records the two carbon descriptors; this is not evidence of a mixture or missing required carbon stereochemistry. The InChI reader yields an imidate/proton-placement tautomer. Explicit component-preserving comparison at common protonation/tautomer states retains atom-neighbor parity and resolves the initial direct-match failure. |
| identity-label | DailyMed XACDURO SPL c0167aec-a89d-4e96-afe5-2ccf3e89fe72; 382-label.xml section11, ingredient identity and formulation | supports | The label identifies durlobactam sodium as the pure (2S,5R) trans form with formula C8H10N3NaO6S. The co-packaged product contains separate sulbactam and durlobactam vials; each durlobactam vial supplies 0.5g parent-equivalent from 0.54g sodium salt. These data support exact salt identity without making the combination product an exact synonym of this molecule. |
| terms | CHEBI:38700; CHEBI:36047; KEGG D11592; 382-term-38700.json; shared371-role.json; exact ChEBI and KEGG records | supports | The organic sodium salt parent fits the explicit ion pair. CAS1467157-21-6 and ETX2514 sodium resolve to this salt in official chemical/drug authorities. The antibacterial-drug role is supported at beta-lactamase-inhibitor ingredient scope; it does not require standalone activity against every pathogen. |
| clinical | DailyMed XACDURO; 382-label.xml sections1,12.4 and14 | context_only | The indication is the sulbactam-containing product for adult HABP/VABP caused by susceptible A. baumannii-calcoaceticus complex. The label distinguishes sulbactam PBP1/PBP3 activity from durlobactam protection against certain serine beta-lactamases and says durlobactam alone lacks activity against ABC isolates. The randomized trial also used background imipenem/cilastatin. None of these combination results establishes monotherapy efficacy or universal absence of intrinsic activity in other organisms. |
| primary | PMID:30862744; DOI:10.1128/mBio.00159-19; 382-PMC6414696.xml Methods critical reagents/kinetics/mass spectrometry/crystallography; Results kinetic analysis, mass adducts and structure | supports | The original study uses Entasis ETX2514 powder, with no explicit salt or catalog in the inspected reagent statement. Purified ADC-7/OXA-58 assays, mass adducts and OXA-24/40 crystallography establish inhibition and covalent ring-opened binding of the durlobactam moiety. The OXA-24/40 adduct is attached to catalytic S81; it is not an intact sodium ion pair bound to the target. Sulbactam-combination isolate tests use fixed 4 mg/L ETX2514 in agar dilution and are not assigned as single-agent salt MICs. |
| original-design | PMID:28665414; DOI:10.1038/nmicrobiol.2017.104; 383-core-28665414.json complete original abstract | context_only | The design paper describes expanded-spectrum serine beta-lactamase/PBP inhibition, intrinsic Enterobacteriaceae activity and sulbactam-combination efficacy. The abstract does not independently establish the exact solid form used in each experiment; the publisher page/supplement attempts did not yield inspected full experimental text. This prevents a universal no-intrinsic-activity inference from the ABC-specific label statement. |
| lead | PMID:37452667; DOI:10.1093/ajhp/zxad143; 382-adopted-core.json sole adopted and current ChEBI citation | context_only | The bibliographic record resolves as Sulbactam Sodium and Durlobactam Sodium. No abstract is available and its full text was not inspected, so the title is not substituted as direct scientific evidence. Independent official and original sources above support the actual native claims. |
| adapter | iModulonDB a_baumannii/precise139 and e_coli/modulome; 382-adapter-results.json | context_only | The native salt record contains no specific gene. Before mechanism follow-up, representative searches identified ABUW_2876 mrdA/PBP2 and b0635 mrdA, plus A. baumannii OXA-69/OXA-23 entries. No component hit required summarization. These are bounded dataset identifiers, not binding proof or an explanation of experimental isolates. |
| owners | Maintained ChEBI inventory and projection; 382-inspect.json; 382-owner-review.json; 382-chebi-row.json; 382-source-audit.json | supports | The original thirteen hashes include every actual maintained owner and remain unchanged. Definition, names, graph, role/parent, exact CAS and two drug-context links reproduce the source. Four histories are ordered. The sole adopted/current citation was explicitly disposed. |
| validation | Executed native and supplementary checks; 382-focused-results.json; 382-strict.tsv; chemistry/source logs | supports | Native chemistry, schema and strict checks pass. The supplemental direct comparison really failed before explicit tautomer/protonation handling; the resolved component/stereo comparison and source ledger pass. |
| access | Exact salt and primary-source searches; 382-local-hits.txt includes ignored files; 382-fetch.json through 382-fetch4.json | context_only | DrugBank DBSALT003190 returned403, leaving that drug-context content unresolved. Nature returned an interstitial, and the nominal supplementary PDF response was HTML rather than an inspected PDF; another route had DNS failure. No paid access was used. Primary mBio full XML and official ingredient/label sources were successfully read. |

## Limits And Additional Notes

- The official clinical product is co-packaged sulbactam plus durlobactam sodium. Neither its indication nor trial outcomes establish efficacy of durlobactam sodium alone; ABC-specific lack of intrinsic activity does not establish inactivity in all bacteria.
- The primary biochemical/crystallographic study identifies Entasis ETX2514 powder but does not specify the solid-form salt in the inspected methods. Its bound drug-moiety evidence is retained at that scope.
- The sole adopted PMID has no abstract and its full text was not inspected. DrugBank was blocked. Original design-paper full text/supplement retrieval did not yield usable inspected content.
- Standard InChI reading changes amide/proton placement. The initial exact direct graph test failed; subsequent explicit fragment protonation/tautomer comparison preserved composition, charges and original chiral parity. No structural correction is inferred from the tool representation alone.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- The two parsed carbon centers correspond to the regulator (2S,5R) description. Extra bridgehead-nitrogen descriptors in some systematic names do not justify adding an arbitrary stereocenter or inferring a mixture.
- Standalone chemistry used the batch 019 interpreter against batch 039; native schema/strict and source-ledger commands used batch 039.
- A text-extraction attempt using an unavailable BeautifulSoup dependency failed; the source XML was subsequently read with the standard-library XML parser. This did not alter native inputs or suppress a validation result.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T151345Z-durlobactam-sodium-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of durlobactam sodium
started_at: '2026-10-21T14:52:10Z'
finished_at: '2026-10-21T15:13:45Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Entire native read, exact maintained-owner reconciliation, independent
    official structure and formula-unit comparisons with chiral parity checks, current
    regulator label, structured adapter before mechanism follow-up, original biochemical/crystallographic
    methods and results.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
native_verdict: Exact monosodium salt supported; clinical combination and experimental
  material boundaries retained
scientific_review: true
summary: Eight chemical encodings support one durlobactam anion with one sodium counterion,
  matching the official named ingredient and both configured carbon centers. The primary
  experimental literature supports the durlobactam moiety as a serine beta-lactamase
  inhibitor, while the regulatory indication belongs to the sulbactam-containing product.
  No confirmed native defect was established. DrugBank access and the sole adopted
  citation full text remain limited; an initial direct graph comparison failed on
  an InChI-read tautomer and was resolved with explicit stereo-preserving comparison.
  Scientific assessment retains the stated evidence limits; full verification is blocked
  by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/durlobactam-sodium.yaml
    sha256: a643866d328a48cc5143501faf5d4888e79b0198c06059666ce9fa64c6d509a1
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
  description: 'Whole SEEDED, EXACT sodium-salt record: definition, two synonyms,
    organic-sodium-salt parent, antibacterial role, complete chemical structure, exact
    CAS, two drug-context identifiers, source concept and four histories. Sole adopted/current
    PMID37452667 disposition recorded.'
  selection: Queue 382 in isolated batch 039. Initial thirteen hashes preserved; actual
    maintained ChEBI owners were already included and verified before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:229544
targets:
- target_id: CHEBI:229544
  path: data/antibiotics/antibacterial/durlobactam-sodium.yaml
  label: durlobactam sodium
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
  name: Native schema
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/durlobactam-sodium.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0.
  target_ids:
  - CHEBI:229544
  evidence_ids:
  - validation
- check_id: strict
  name: Native strict terms
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/durlobactam-sodium.yaml --out /private/tmp/am-review-session/382-strict.tsv
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; no ERROR rows.
  target_ids:
  - CHEBI:229544
  evidence_ids:
  - validation
- check_id: native-chemistry
  name: Native molecular consistency
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    382
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Native formula, key, mass and charge check passes.
  target_ids:
  - CHEBI:229544
  evidence_ids:
  - chemistry
  - validation
- check_id: direct-authorities
  name: Initial direct graph comparison
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/382-chemistry-direct-initial.py
    382 > /private/tmp/am-review-session/382-chemistry-direct-recheck.log 2>&1
  status: failed
  required: false
  exit_code: 1
  expected_exit_code: 0
  summary: 'Executed exit 1 at native-inchi: RDKit reads an imidate/proton-placement
    tautomer despite the identical Standard InChIKey. Retained as a failed supplemental
    check; not an unavailable gate or a demonstrated wrong molecule.'
  target_ids:
  - CHEBI:229544
  evidence_ids:
  - chemistry
- check_id: authority-chemistry
  name: Explicit formula-unit and stereo comparison
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/382-chemistry-authorities.py
    382 > /private/tmp/am-review-session/382-chemistry-authorities.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Eight encodings match after explicitly recorded common fragment protonation/tautomer
    comparison. Original composition, two ionic components, charges, key, masses and
    configured-carbon parity checked before normalization.
  target_ids:
  - CHEBI:229544
  evidence_ids:
  - chemistry
- check_id: adapter
  name: Structured mechanism context before primary follow-up
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/382-adapter.py
    > /private/tmp/am-review-session/382-adapter.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Dataset discovery and representative A. baumannii/E. coli gene searches
    exit 0; no iModulon hit requiring summary.
  target_ids:
  - CHEBI:229544
  evidence_ids:
  - adapter
- check_id: source-ledger
  name: Source, identifiers, citation and history ledger
  command: .venv/bin/python /private/tmp/am-review-session/382-ledger.py 382 > /private/tmp/am-review-session/382-ledger.log
    2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Thirteen hashes unchanged; all source fields/identifier placements, sole
    adopted/current citation and four histories checked.
  target_ids:
  - CHEBI:229544
  evidence_ids:
  - owners
  - lead
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:229544
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
  - CHEBI:229544
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
  - CHEBI:229544
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
  - CHEBI:229544
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
  - CHEBI:229544
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
  - CHEBI:229544
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
  - CHEBI:229544
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
  - CHEBI:229544
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
  - CHEBI:229544
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/durlobactam-sodium.yaml
  locator: Whole native YAML
  accessed_at: '2026-10-21T15:10:52Z'
  support: supports
  summary: One exact monosodium salt with two chemical aliases. No native molecular-target,
    resistance, MIC, producer, clinical-status assertion or causal-graph objects are
    populated; the record does not assert standalone treatment efficacy.
- evidence_id: chemistry
  kind: authority
  reference: CHEBI:229544; UNII:F78MDZ9CW9; PubChem CID89851851; KEGG D11592
  locator: 382-chebi.json/.mol; 382-gsrs.json; 382-pubchem.json; 382-kegg.txt/.mol;
    382-authority-chemistry.json
  accessed_at: '2026-10-21T15:10:52Z'
  support: supports
  summary: Eight encodings agree on C8H10N3NaO6S, net zero charge, one organic anion
    plus one sodium cation and WHHNOICWPZIYKI-IBTYICNHSA-M. The two configured carbon
    centers map reciprocally with chirality retained. GSRS can additionally label
    the constrained bridgehead nitrogen, whereas the Standard InChI records the two
    carbon descriptors; this is not evidence of a mixture or missing required carbon
    stereochemistry. The InChI reader yields an imidate/proton-placement tautomer.
    Explicit component-preserving comparison at common protonation/tautomer states
    retains atom-neighbor parity and resolves the initial direct-match failure.
  snapshot_sha256: aa94d0568023766dfb9eb2b3e854d75e08cc205aca0b8892be1986bd786e47b3
- evidence_id: identity-label
  kind: authority
  reference: DailyMed XACDURO SPL c0167aec-a89d-4e96-afe5-2ccf3e89fe72
  locator: 382-label.xml section11, ingredient identity and formulation
  accessed_at: '2026-10-21T15:07:06.406833Z'
  support: supports
  summary: The label identifies durlobactam sodium as the pure (2S,5R) trans form
    with formula C8H10N3NaO6S. The co-packaged product contains separate sulbactam
    and durlobactam vials; each durlobactam vial supplies 0.5g parent-equivalent from
    0.54g sodium salt. These data support exact salt identity without making the combination
    product an exact synonym of this molecule.
  snapshot_sha256: 01d6b21826563aac5d80c7ef8ea24cb1b659c97cca0cf6621dc9aa6f02fd2561
- evidence_id: terms
  kind: authority
  reference: CHEBI:38700; CHEBI:36047; KEGG D11592
  locator: 382-term-38700.json; shared371-role.json; exact ChEBI and KEGG records
  accessed_at: '2026-10-21T15:06:26.967011Z'
  support: supports
  summary: The organic sodium salt parent fits the explicit ion pair. CAS1467157-21-6
    and ETX2514 sodium resolve to this salt in official chemical/drug authorities.
    The antibacterial-drug role is supported at beta-lactamase-inhibitor ingredient
    scope; it does not require standalone activity against every pathogen.
  snapshot_sha256: 261c4663b5f7c1c560ba8e61b349b699fc8d6da4bb7afe9e4ea7cbfaee26908a
- evidence_id: clinical
  kind: authority
  reference: DailyMed XACDURO
  locator: 382-label.xml sections1,12.4 and14
  accessed_at: '2026-10-21T15:07:06.406833Z'
  support: context_only
  summary: The indication is the sulbactam-containing product for adult HABP/VABP
    caused by susceptible A. baumannii-calcoaceticus complex. The label distinguishes
    sulbactam PBP1/PBP3 activity from durlobactam protection against certain serine
    beta-lactamases and says durlobactam alone lacks activity against ABC isolates.
    The randomized trial also used background imipenem/cilastatin. None of these combination
    results establishes monotherapy efficacy or universal absence of intrinsic activity
    in other organisms.
  snapshot_sha256: 01d6b21826563aac5d80c7ef8ea24cb1b659c97cca0cf6621dc9aa6f02fd2561
- evidence_id: primary
  kind: primary_source
  reference: PMID:30862744; DOI:10.1128/mBio.00159-19
  locator: 382-PMC6414696.xml Methods critical reagents/kinetics/mass spectrometry/crystallography;
    Results kinetic analysis, mass adducts and structure
  accessed_at: '2026-10-21T15:07:58.973201Z'
  support: supports
  summary: The original study uses Entasis ETX2514 powder, with no explicit salt or
    catalog in the inspected reagent statement. Purified ADC-7/OXA-58 assays, mass
    adducts and OXA-24/40 crystallography establish inhibition and covalent ring-opened
    binding of the durlobactam moiety. The OXA-24/40 adduct is attached to catalytic
    S81; it is not an intact sodium ion pair bound to the target. Sulbactam-combination
    isolate tests use fixed 4 mg/L ETX2514 in agar dilution and are not assigned as
    single-agent salt MICs.
  snapshot_sha256: b918cf17d6b771433bbbb9caebdf4ce5e29c855a5814c815855927544f4bc255
- evidence_id: original-design
  kind: primary_source
  reference: PMID:28665414; DOI:10.1038/nmicrobiol.2017.104
  locator: 383-core-28665414.json complete original abstract
  accessed_at: '2026-10-21T15:07:43.334089Z'
  support: context_only
  summary: The design paper describes expanded-spectrum serine beta-lactamase/PBP
    inhibition, intrinsic Enterobacteriaceae activity and sulbactam-combination efficacy.
    The abstract does not independently establish the exact solid form used in each
    experiment; the publisher page/supplement attempts did not yield inspected full
    experimental text. This prevents a universal no-intrinsic-activity inference from
    the ABC-specific label statement.
  snapshot_sha256: 6013d3a8bb0d669658ebd06d749e99e5238909201dc5c604f34fb77e0540665c
- evidence_id: lead
  kind: primary_source
  reference: PMID:37452667; DOI:10.1093/ajhp/zxad143
  locator: 382-adopted-core.json sole adopted and current ChEBI citation
  accessed_at: '2026-10-21T15:06:26.967156Z'
  support: context_only
  summary: The bibliographic record resolves as Sulbactam Sodium and Durlobactam Sodium.
    No abstract is available and its full text was not inspected, so the title is
    not substituted as direct scientific evidence. Independent official and original
    sources above support the actual native claims.
  snapshot_sha256: ce73bd7863f24fa7b7ae6ba7d9be9cf2254139e6a77899a45ac5f927623d0830
- evidence_id: adapter
  kind: database
  reference: iModulonDB a_baumannii/precise139 and e_coli/modulome
  locator: 382-adapter-results.json
  accessed_at: '2026-10-21T15:10:52Z'
  support: context_only
  summary: The native salt record contains no specific gene. Before mechanism follow-up,
    representative searches identified ABUW_2876 mrdA/PBP2 and b0635 mrdA, plus A.
    baumannii OXA-69/OXA-23 entries. No component hit required summarization. These
    are bounded dataset identifiers, not binding proof or an explanation of experimental
    isolates.
  snapshot_sha256: 81fe83c206f8259ad4dc6c5795c14d6d0d6b0177bd02da9debe51aa801c116ad
- evidence_id: owners
  kind: database
  reference: Maintained ChEBI inventory and projection
  locator: 382-inspect.json; 382-owner-review.json; 382-chebi-row.json; 382-source-audit.json
  accessed_at: '2026-10-21T15:10:52Z'
  support: supports
  summary: The original thirteen hashes include every actual maintained owner and
    remain unchanged. Definition, names, graph, role/parent, exact CAS and two drug-context
    links reproduce the source. Four histories are ordered. The sole adopted/current
    citation was explicitly disposed.
  snapshot_sha256: 69d87936f5a8d9ccbeb95e15e3c82066d5e9fd922564613f53897a1d369a4d1f
- evidence_id: validation
  kind: validation
  reference: Executed native and supplementary checks
  locator: 382-focused-results.json; 382-strict.tsv; chemistry/source logs
  accessed_at: '2026-10-21T15:10:52Z'
  support: supports
  summary: Native chemistry, schema and strict checks pass. The supplemental direct
    comparison really failed before explicit tautomer/protonation handling; the resolved
    component/stereo comparison and source ledger pass.
  snapshot_sha256: dd8614ceaca2dfeb68714ea9fa5173a72f3d1b7b8021a11d588532d8ae1b43a4
- evidence_id: access
  kind: search
  reference: Exact salt and primary-source searches
  locator: 382-local-hits.txt includes ignored files; 382-fetch.json through 382-fetch4.json
  accessed_at: '2026-10-21T15:10:52Z'
  support: context_only
  summary: DrugBank DBSALT003190 returned403, leaving that drug-context content unresolved.
    Nature returned an interstitial, and the nominal supplementary PDF response was
    HTML rather than an inspected PDF; another route had DNS failure. No paid access
    was used. Primary mBio full XML and official ingredient/label sources were successfully
    read.
  snapshot_sha256: 8ab9790b5e0742047deb1f042e42295cde00297e5e68b2827d634ccb06cc28f4
  search_scope: 382-local-hits.txt includes ignored files; 382-fetch.json through
    382-fetch4.json
assessments:
- assessment_id: identity
  area: identity
  topic: Exact monosodium salt
  outcome: supported
  summary: Independent authorities and current official ingredient description agree,
    with two ionic components retained and configured carbon parity mapped.
  target_ids:
  - CHEBI:229544
  evidence_ids:
  - chemistry
  - identity-label
- assessment_id: terms
  area: nomenclature
  topic: Definition, names, parent and role
  outcome: supported
  summary: The monosodium description and sodium-qualified ETX2514 alias fit the exact
    graph. Antibacterial-drug role is consistent with its inhibitor ingredient scope.
  target_ids:
  - CHEBI:229544
  evidence_ids:
  - terms
  - identity-label
  - clinical
- assessment_id: mechanism
  area: evidence
  topic: Moiety mechanism and assay boundaries
  outcome: supported
  summary: Original enzyme/structure data support the active moiety; experiment salt
    is not explicitly established. No combination MIC is transferred as sodium-salt
    monotherapy activity.
  target_ids:
  - CHEBI:229544
  evidence_ids:
  - primary
  - original-design
  - clinical
  - adapter
- assessment_id: external
  area: identity
  topic: DrugBank and adopted full-text access
  outcome: unknown
  summary: DrugBank contents and the sole adopted citation full text remain unverified;
    no contradiction is inferred.
  target_ids:
  - CHEBI:229544
  evidence_ids:
  - access
  - lead
- assessment_id: completeness
  area: completeness
  topic: Optional mechanism and clinical enrichment
  outcome: supported
  summary: No missing mandatory representation was established for this SEEDED record.
    Any later mechanism/clinical addition should preserve parent-versus-salt and combination
    scope.
  target_ids:
  - CHEBI:229544
  evidence_ids:
  - record
  - primary
  - clinical
- assessment_id: provenance
  area: provenance
  topic: Owners, source fields and histories
  outcome: supported
  summary: Thirteen inputs and all native source fields, the citation and four histories
    were checked.
  target_ids:
  - CHEBI:229544
  evidence_ids:
  - owners
  - validation
findings: []
actions: []
limitations:
- The official clinical product is co-packaged sulbactam plus durlobactam sodium.
  Neither its indication nor trial outcomes establish efficacy of durlobactam sodium
  alone; ABC-specific lack of intrinsic activity does not establish inactivity in
  all bacteria.
- The primary biochemical/crystallographic study identifies Entasis ETX2514 powder
  but does not specify the solid-form salt in the inspected methods. Its bound drug-moiety
  evidence is retained at that scope.
- The sole adopted PMID has no abstract and its full text was not inspected. DrugBank
  was blocked. Original design-paper full text/supplement retrieval did not yield
  usable inspected content.
- Standard InChI reading changes amide/proton placement. The initial exact direct
  graph test failed; subsequent explicit fragment protonation/tautomer comparison
  preserved composition, charges and original chiral parity. No structural correction
  is inferred from the tool representation alone.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- The two parsed carbon centers correspond to the regulator (2S,5R) description. Extra
  bridgehead-nitrogen descriptors in some systematic names do not justify adding an
  arbitrary stereocenter or inferring a mixture.
- Standalone chemistry used the batch 019 interpreter against batch 039; native schema/strict
  and source-ledger commands used batch 039.
- A text-extraction attempt using an unavailable BeautifulSoup dependency failed;
  the source XML was subsequently read with the standard-library XML parser. This
  did not alter native inputs or suppress a validation result.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:229544
- https://www.kegg.jp/entry/D11592
- https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=c0167aec-a89d-4e96-afe5-2ccf3e89fe72
- https://doi.org/10.1128/mBio.00159-19
tags:
- record-review
- durlobactam-sodium
- salt-identity
- combination-scope
```
