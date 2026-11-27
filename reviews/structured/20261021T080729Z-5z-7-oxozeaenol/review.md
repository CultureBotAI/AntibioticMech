# 5Z-7-oxozeaenol: exact identity supported, antibacterial source support conflicts

- Review: 20261021T080729Z-5z-7-oxozeaenol
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:01:47Z
- Finished UTC: 2026-10-21T08:07:29Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The Z-isomer chemistry and LL-Z1640-2 synonym are coherent. One major finding concerns the unqualified antibacterial assertion: its sole adopted primary citation reports no activity for exact compound5 in the tested bacterial diffusion assay. Fungal isolation, cytotoxicity and human-cell NF-kappaB effects are supported. Separate fungicidal literature is a concrete follow-up, so neither universal inactivity nor unconditional exclusion is warranted.

## Scope And Provenance

Entire exact native record, maintained source ownership, sole adopted citation, official identity checks and bounded exact-compound literature follow-up.

Selection: Queue index056, CHEBI:67559 at its locked path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:67559 | data/antibiotics/antibacterial/5z-7-oxozeaenol.yaml | generated | 5Z-7-oxozeaenol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:67559 | Focused LinkML validation exited0. |
| strict | passed | True | CHEBI:67559 | Focused strict scan of one file has zero ERROR rows. |
| chemistry | passed | False | CHEBI:67559 | Independent SMILES/InChI parsing agrees on full Z stereochemical key, formula, masses, charge and source mint. |
| structured-context | not_applicable | False | CHEBI:67559 | The inspected same-session iModulonDB inventory has no human-cell NF-kappaB/TAK1 or fungal MSX63935 context. No matching search or component summary applies. |
| reaxys | unavailable | False | CHEBI:67559 | Reaxys8800797 is present in current ChEBI but was not independently inspected through free registry access. |
| additional-fulltext | unavailable | False | CHEBI:67559 | 2014 fungicidal and2003 TAK1 original abstracts are available, but the inspected publisher routes did not expose the full articles.2015 TAK1 table routes also failed; no uninspected quantitative results are adopted. |
| Authoritative full QC | failed | True | CHEBI:67559 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:67559 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:67559 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:67559 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:67559 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:67559 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:67559 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:67559 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:67559 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact Z-isomer and two synonyms

identity: supported. Targets: CHEBI:67559.

Native chemical form and label are consistent; LL-Z1640-2 is confirmed by the source-cited primary structure characterization.

### Parents and registry

grounding: supported. Targets: CHEBI:67559.

All five parents are chemically broader. Reaxys remains source-asserted with access limitation.

### Antibacterial definition and role

evidence: concern. Targets: CHEBI:67559.

The only adopted primary citation is negative in its exact purified-compound bacterial assay. Further positive evidence is required to justify the unqualified source assertion.

### Cytotoxic/NF-kappaB definition scope

evidence: supported. Targets: CHEBI:67559.

Exact Z human-cell effects support these clauses. Host TAK1 evidence must remain separate from antimicrobial mechanism.

### Fungal isolation

evidence: supported. Targets: CHEBI:67559.

The cultured fungus and isolated exact compound support the broad native origin statement.

### Other activity leads and optional objects

completeness: unknown. Targets: CHEBI:67559.

A concrete primary fungicidal lead needs full compound mapping and assay inspection before reclassification; no optional-field failure or universal inactivity is asserted.

### Source reproduction and scientific status

ownership: supported. Targets: CHEBI:67559.

The row and native seed agree, but source agreement does not resolve the biological support conflict. Histories remain untouched and all13 hashes match.

### Focused native checks

schema: supported. Targets: CHEBI:67559.

Focused schema and strict checks pass, as does independent chemistry.

## Findings

### F1: Resolve the antibacterial assertion against its cited negative experiment

major / open / confirmed; issue key: chebi-67559-antibacterial-source-support-conflict.

The only adopted primary citation reports exact purifiedZ compound5 inactive in the tested four-bacterium diffusion assay. The positive definition/role assertion lacks support from that citation. Separate fungicidal literature is a concrete lead, so the appropriate follow-up is exact evidence adjudication and possible reclassification, not unconditional exclusion or a claim of universal inactivity.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate exact Z antibacterial support and inspect the2014 fungicidal primary report before correcting the maintained definition/role and filing class.

- Keep2011 purified-compound negative diffusion results separate from crude-culture MRSA activity, E-isomer results and host NF-kappaB/TAK1 inhibition.
- Inspect2014 compound6 structure/name and complete assay conditions before adopting fungal or oomycete activity. Preserve organism taxonomy and whole-plant preventative endpoints; do not turn them into bacterial MICs.
- If positive antibacterial evidence is found, cite the exact Z experiment with organism, method, units and limits. If other in-scope antimicrobial activity is verified, use a reproducible supported role/classification instead of excluding solely because the2011 bacterial screen was negative.
- Any exclusion must remain conditional on failure to establish valid in-scope activity; the bounded search does not demonstrate universal inactivity.
- Use authorized maintained-source/config/decision changes and reseeding for generated claims, validated native writer/history for scientific additions, and run focused schema/strict plus verify-corpus and required shared gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/5z-7-oxozeaenol.yaml; Entire native YAML, read after056 initial capture. | supports | The exact Z compound is SEEDED/EXACT and filed ANTIBACTERIAL. It has two exact synonyms, five chemical parents, antibacterial role33282, neutral stereochemical structure, Reaxys8800797, one source concept and three seed/reseed events. No optional claim-level evidence, activity_spectrum, targets, producer, resistance or graph objects are present. |
| source | data/raw/chebi_antimicrobials.tsv; Row1680,056-raw.json; conf/sources.yaml; extractor176–339; seeder790–809 and1483–1570; MANIFEST/PATHS. | supports | The native source fields reproduce the maintained row, including the antibacterial claim. PMID21513293 is the only adopted citation and is deliberately retained as a lead rather than automatically seeded claim evidence. Mechanism roles are empty. Source version2026-08-30 and three histories agree with seeding. All13 initial input hashes remain unchanged. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:67559; Complete official056-chebi.html/txt; PubChem CID9863776 full property record056-pubchem.json and official page. | supports | ChEBI, PubChem and native full InChI/key agree on NEQZWEXWOFPKOT-BYRRXHGESA-N, C19H22O7, neutral charge, mass362.378 and exact mass362.13655. Native systematic name has5Z/11E and three S stereocentres. LL-Z1640-2 also matches the primary paper. Parents2468 secondary alpha-hydroxy ketone,25106 macrolide,33853 phenols,35618 aromatic ether and35681 secondary alcohol are strictly broader. Role33282 correctly denotes antibacterial agent, whose experimental support is separately disputed. Reaxys8800797 remains source-asserted. |
| chemistry | Independent RDKit calculation; 056-chemistry.json/log; inspected helperchem005.py. | supports | Both structures parse to identical full stereochemical key and neutral single fragment, formulaC19H22O7, average mass362.378 and exact mass362.136553044. Three stereocentres are S. Repository SHA256 source mint antibioticmech:chebi-23bb4868f0 matches. This Z entity remains distinct from the E full-key suffix ULSULSEOSA. |
| primary-identity | PMID:21513293; DOI:10.1021/np200062x; complete primary PMC article saved055-2011.html/txt and visually inspected055-2011-structures.jpg; compound5 characterization. | supports | The paper names compound5 as5Z-7-oxozeaenol, also LL-Z1640-2, formulaC19H22O7. Spectroscopic comparison with purchased standard and optical rotation support the known exact structure. It separately draws E compound4 and saturated LL-Z1640-1 compound6. The source Z synonym is supported, unlike the adjacent E record’s imported LL-Z1640-1 synonym. |
| primary-antibacterial | PMID:21513293; Results assay paragraph and Experimental Antimicrobial Assay. | refutes | Compounds1–6, including exactZ5, showed no activity at500µg/mL against E.coli, S.aureus, M.smegmatis and B.subtilis. The method is agar surface diffusion,10µL methanol application, LB or Middlebrook7H9 with1% glycerol/1.5% agar, overnight37°C; strains are unspecified. Results call the endpoints MIC&gt;500µg/mL, but this is not standardized broth MIC. The culture’s earlier MRSA screening hit is a crude-extract observation and was not assigned to purified5. This contradicts using this study as positive antibacterial support, not all possible activity. |
| primary-host | PMID:21513293; Tables2–3 and human-cell assays. | supports | Exact compound5 has cytotoxic IC50 values3.8,1.2,5.1,3.6,3.3µM across MCF-7,H460,SF268,HT-29,MDA-MB-435 after72h exposure. The NF-kappaB p65 endpoint is0.24µM in treated HeLa nuclear extracts. This supports the source’s cytotoxicity and NF-kappaB clauses in host cells, not direct p65 binding or a microbial mechanism. Mitochondrial potential assay was considered inactive at IC50&gt;10µM. |
| primary-origin | PMID:21513293; Producing Organism and Fermentation; Extraction and Isolation. | supports | The study cultured MSX63935 and isolated885.9mg of Z compound5 from its fermented material. It supports the broad fungal-isolation statement. The isolate was related to Phoma by sequence comparison; do not promote that to a precise species assignment or infer a BGC from extraction. Optional producer evidence would require scoped strain grounding. |
| host-tak1 | PMID:12624112; DOI:10.1074/jbc.M207453200; complete official abstract in056-epmc.json and PubMed. | supports | The original study explicitly identifies exact5Z-7-oxozeaenol as inhibiting TAK1 catalytic activity and host proinflammatory signaling in cell culture and an inflammation model. This is primary support for a host pathway context; the abstract does not establish direct antibacterial inhibition, whole-kinome selectivity or a covalent binding measurement. Full publisher routes returned403, so detailed measurements are not adopted. |
| additional | PMID:24635109; DOI:10.1021/jf500248z; complete official PubMed/EuropePMC abstract056-epmc.json and ACS abstract. | context_only | The primary abstract reports whole-plant preventative activity for compound6 against P.viticola at6ppm and P.infestans at200,60,20ppm, plus barnacle-settlement effects. It does not name compound6 in the abstract. Secondary discovery sources map6 to LL-Z1640-2 and mention a Pestalotia assay, but primary structure mapping and that full assay were not retrieved. These are specific follow-up leads before role changes; barnacle settlement itself is not bacterial growth inhibition. |
| adapter | https://imodulondb.org/api/datasets; Actual same-session055-imodulondb-datasets-retry.txt inventory, reused for the identical host/fungal context. | context_only | The covered organism/dataset list contains no human-cell NF-kappaB/TAK1 or MSX63935 fungal dataset. The inventory was retrieved successfully after an earlier DNS failure, both captured under055. No matching search/summary applies, and lack of coverage is not biological evidence. |
| search | CultureBotAI/AntibioticMech; 056-local-hits.txt and056-maintained-search.txt; bounded web discovery and official source retrieval. | context_only | Ignored-inclusive maintained-path search found no prior target-specific decision/overlay/review. Exact-name/synonym searches found a real fungicidal follow-up and many host signaling studies, but no inspected positive exact Z antibacterial primary experiment resolving the2011 conflict. Secondary fungicidal summaries are leads only, not assay evidence. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Identity, classification, evidence, target scope and optional fields; CURATION/HARMONIZATION. | supports | A positive activity role requires the correct compound/organism/assay scope. Optional missing mechanism/evidence objects do not create a defect by themselves. Generated definition/roles must be corrected through maintained sources or adjudication, with scientific additions through native validated writer/history. |
| validation | Documented focused gates; 056-focused-results.json;056-schema.log,056-strict.log/tsv and056-chemistry.json. | supports | Focused schema, strict and chemistry checks all exited0. Shared corpus gates are documented separately in the final bundle. |

## Limits And Additional Notes

- Reaxys8800797 was corroborated only through current ChEBI. All13 initial target/input hashes remain unchanged.
- The complete2011 cited primary paper and figure were inspected. The2003 TAK1 and2014 fungicidal papers were read at complete official abstract level only; exact2014 compound6 mapping and Pestalotia potency remain unadopted leads.
- The2015 host-kinase follow-up was identified and its official abstract inspected during the immediately preceding E review; full-table access was unavailable and no result is transferred to this record.
- The dataset inventory is a same-session source-context check and offers no human or relevant fungal coverage. Bounded searches neither rule out other antimicrobial evidence nor justify transferring effects among E/Z isomers.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T080729Z-5z-7-oxozeaenol
kind: record
repository: CultureBotAI/AntibioticMech
title: '5Z-7-oxozeaenol: exact identity supported, antibacterial source support conflicts'
started_at: '2026-10-21T08:01:47Z'
finished_at: '2026-10-21T08:07:29Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the native record. Captured this exact
    target before assessment and read the entire native record, maintained source
    row and transforms. The cited full primary paper and its structure figure were
    inspected, with Z compound5 assessed independently from E compound4.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'The Z-isomer chemistry and LL-Z1640-2 synonym are coherent. One major finding
  concerns the unqualified antibacterial assertion: its sole adopted primary citation
  reports no activity for exact compound5 in the tested bacterial diffusion assay.
  Fungal isolation, cytotoxicity and human-cell NF-kappaB effects are supported. Separate
  fungicidal literature is a concrete follow-up, so neither universal inactivity nor
  unconditional exclusion is warranted.'
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
  - path: data/antibiotics/antibacterial/5z-7-oxozeaenol.yaml
    sha256: 4fae214ca5b074f8d7c598a0d76c165e7d989a6a9b6cc20ce4f83035e8c52100
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
- target_id: CHEBI:67559
  path: data/antibiotics/antibacterial/5z-7-oxozeaenol.yaml
  label: 5Z-7-oxozeaenol
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
  description: Entire exact native record, maintained source ownership, sole adopted
    citation, official identity checks and bounded exact-compound literature follow-up.
  selection: Queue index056, CHEBI:67559 at its locked path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:67559
  exclusions:
  - target: E-isomer, LL-Z1640-1, crude fungal extracts and other resorcylic acid
      lactones
    reason: Different chemical entities or mixtures; their activity and target evidence
      are not transferred.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Focused LinkML validation exited0.
  target_ids:
  - CHEBI:67559
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/5z-7-oxozeaenol.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Focused strict scan of one file has zero ERROR rows.
  target_ids:
  - CHEBI:67559
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/5z-7-oxozeaenol.yaml --out /private/tmp/am-review-session/056-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Independent SMILES/InChI parsing agrees on full Z stereochemical key, formula,
    masses, charge and source mint.
  target_ids:
  - CHEBI:67559
  evidence_ids:
  - chemistry
  command: .venv/bin/python /private/tmp/am-review-session/chem005.py 56
  exit_code: 0
  expected_exit_code: 0
- check_id: structured-context
  name: structured-context
  status: not_applicable
  required: false
  summary: The inspected same-session iModulonDB inventory has no human-cell NF-kappaB/TAK1
    or fungal MSX63935 context. No matching search or component summary applies.
  target_ids:
  - CHEBI:67559
  evidence_ids:
  - adapter
- check_id: reaxys
  name: reaxys
  status: unavailable
  required: false
  summary: Reaxys8800797 is present in current ChEBI but was not independently inspected
    through free registry access.
  target_ids:
  - CHEBI:67559
  evidence_ids:
  - identity
- check_id: additional-fulltext
  name: additional-fulltext
  status: unavailable
  required: false
  summary: 2014 fungicidal and2003 TAK1 original abstracts are available, but the
    inspected publisher routes did not expose the full articles.2015 TAK1 table routes
    also failed; no uninspected quantitative results are adopted.
  target_ids:
  - CHEBI:67559
  evidence_ids:
  - additional
  - host-tak1
  - search
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:67559
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
  - CHEBI:67559
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
  - CHEBI:67559
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
  - CHEBI:67559
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
  - CHEBI:67559
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
  - CHEBI:67559
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
  - CHEBI:67559
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
  - CHEBI:67559
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
  - CHEBI:67559
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/5z-7-oxozeaenol.yaml
  locator: Entire native YAML, read after056 initial capture.
  accessed_at: '2026-10-21T08:04:54Z'
  support: supports
  summary: The exact Z compound is SEEDED/EXACT and filed ANTIBACTERIAL. It has two
    exact synonyms, five chemical parents, antibacterial role33282, neutral stereochemical
    structure, Reaxys8800797, one source concept and three seed/reseed events. No
    optional claim-level evidence, activity_spectrum, targets, producer, resistance
    or graph objects are present.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Row1680,056-raw.json; conf/sources.yaml; extractor176–339; seeder790–809
    and1483–1570; MANIFEST/PATHS.
  accessed_at: '2026-10-21T08:04:54Z'
  support: supports
  summary: The native source fields reproduce the maintained row, including the antibacterial
    claim. PMID21513293 is the only adopted citation and is deliberately retained
    as a lead rather than automatically seeded claim evidence. Mechanism roles are
    empty. Source version2026-08-30 and three histories agree with seeding. All13
    initial input hashes remain unchanged.
  snapshot_sha256: 4c95c64578275513eec5036a4b4919d6619979e6fa26833341b35652419bc9a2
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:67559
  locator: Complete official056-chebi.html/txt; PubChem CID9863776 full property record056-pubchem.json
    and official page.
  accessed_at: '2026-10-21T08:04:54Z'
  support: supports
  summary: ChEBI, PubChem and native full InChI/key agree on NEQZWEXWOFPKOT-BYRRXHGESA-N,
    C19H22O7, neutral charge, mass362.378 and exact mass362.13655. Native systematic
    name has5Z/11E and three S stereocentres. LL-Z1640-2 also matches the primary
    paper. Parents2468 secondary alpha-hydroxy ketone,25106 macrolide,33853 phenols,35618
    aromatic ether and35681 secondary alcohol are strictly broader. Role33282 correctly
    denotes antibacterial agent, whose experimental support is separately disputed.
    Reaxys8800797 remains source-asserted.
  snapshot_sha256: 46dffe6be632a123f90af39b47a2c0e05d920b9f03ba976b00c7cec6669fdaf7
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit calculation
  locator: 056-chemistry.json/log; inspected helperchem005.py.
  accessed_at: '2026-10-21T08:04:54Z'
  support: supports
  summary: Both structures parse to identical full stereochemical key and neutral
    single fragment, formulaC19H22O7, average mass362.378 and exact mass362.136553044.
    Three stereocentres are S. Repository SHA256 source mint antibioticmech:chebi-23bb4868f0
    matches. This Z entity remains distinct from the E full-key suffix ULSULSEOSA.
  snapshot_sha256: da73ac087c9e9520cf63fc0f6f4cb2c05ba2e548e4c100260848a64dd541e528
- evidence_id: primary-identity
  kind: primary_source
  reference: PMID:21513293
  locator: DOI:10.1021/np200062x; complete primary PMC article saved055-2011.html/txt
    and visually inspected055-2011-structures.jpg; compound5 characterization.
  accessed_at: '2026-10-21T08:04:54Z'
  support: supports
  summary: The paper names compound5 as5Z-7-oxozeaenol, also LL-Z1640-2, formulaC19H22O7.
    Spectroscopic comparison with purchased standard and optical rotation support
    the known exact structure. It separately draws E compound4 and saturated LL-Z1640-1
    compound6. The source Z synonym is supported, unlike the adjacent E record’s imported
    LL-Z1640-1 synonym.
  snapshot_sha256: f591e80913f8c902222e2defc1774fc7a679c0b546a7d2c42b02b5e4690f4db1
- evidence_id: primary-antibacterial
  kind: primary_source
  reference: PMID:21513293
  locator: Results assay paragraph and Experimental Antimicrobial Assay.
  accessed_at: '2026-10-21T08:04:54Z'
  support: refutes
  summary: Compounds1–6, including exactZ5, showed no activity at500µg/mL against
    E.coli, S.aureus, M.smegmatis and B.subtilis. The method is agar surface diffusion,10µL
    methanol application, LB or Middlebrook7H9 with1% glycerol/1.5% agar, overnight37°C;
    strains are unspecified. Results call the endpoints MIC>500µg/mL, but this is
    not standardized broth MIC. The culture’s earlier MRSA screening hit is a crude-extract
    observation and was not assigned to purified5. This contradicts using this study
    as positive antibacterial support, not all possible activity.
  snapshot_sha256: f591e80913f8c902222e2defc1774fc7a679c0b546a7d2c42b02b5e4690f4db1
- evidence_id: primary-host
  kind: primary_source
  reference: PMID:21513293
  locator: Tables2–3 and human-cell assays.
  accessed_at: '2026-10-21T08:04:54Z'
  support: supports
  summary: Exact compound5 has cytotoxic IC50 values3.8,1.2,5.1,3.6,3.3µM across MCF-7,H460,SF268,HT-29,MDA-MB-435
    after72h exposure. The NF-kappaB p65 endpoint is0.24µM in treated HeLa nuclear
    extracts. This supports the source’s cytotoxicity and NF-kappaB clauses in host
    cells, not direct p65 binding or a microbial mechanism. Mitochondrial potential
    assay was considered inactive at IC50>10µM.
  snapshot_sha256: f591e80913f8c902222e2defc1774fc7a679c0b546a7d2c42b02b5e4690f4db1
- evidence_id: primary-origin
  kind: primary_source
  reference: PMID:21513293
  locator: Producing Organism and Fermentation; Extraction and Isolation.
  accessed_at: '2026-10-21T08:04:54Z'
  support: supports
  summary: The study cultured MSX63935 and isolated885.9mg of Z compound5 from its
    fermented material. It supports the broad fungal-isolation statement. The isolate
    was related to Phoma by sequence comparison; do not promote that to a precise
    species assignment or infer a BGC from extraction. Optional producer evidence
    would require scoped strain grounding.
  snapshot_sha256: f591e80913f8c902222e2defc1774fc7a679c0b546a7d2c42b02b5e4690f4db1
- evidence_id: host-tak1
  kind: primary_source
  reference: PMID:12624112
  locator: DOI:10.1074/jbc.M207453200; complete official abstract in056-epmc.json
    and PubMed.
  accessed_at: '2026-10-21T08:04:54Z'
  support: supports
  summary: The original study explicitly identifies exact5Z-7-oxozeaenol as inhibiting
    TAK1 catalytic activity and host proinflammatory signaling in cell culture and
    an inflammation model. This is primary support for a host pathway context; the
    abstract does not establish direct antibacterial inhibition, whole-kinome selectivity
    or a covalent binding measurement. Full publisher routes returned403, so detailed
    measurements are not adopted.
  snapshot_sha256: cf805cfe4f6aa5f9fbe7bf343e99d8aa43c3c40cf46bc52bf72ce521e847a49c
- evidence_id: additional
  kind: primary_source
  reference: PMID:24635109
  locator: DOI:10.1021/jf500248z; complete official PubMed/EuropePMC abstract056-epmc.json
    and ACS abstract.
  accessed_at: '2026-10-21T08:04:54Z'
  support: context_only
  summary: The primary abstract reports whole-plant preventative activity for compound6
    against P.viticola at6ppm and P.infestans at200,60,20ppm, plus barnacle-settlement
    effects. It does not name compound6 in the abstract. Secondary discovery sources
    map6 to LL-Z1640-2 and mention a Pestalotia assay, but primary structure mapping
    and that full assay were not retrieved. These are specific follow-up leads before
    role changes; barnacle settlement itself is not bacterial growth inhibition.
  snapshot_sha256: cf805cfe4f6aa5f9fbe7bf343e99d8aa43c3c40cf46bc52bf72ce521e847a49c
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Actual same-session055-imodulondb-datasets-retry.txt inventory, reused
    for the identical host/fungal context.
  accessed_at: '2026-10-21T08:04:54Z'
  support: context_only
  summary: The covered organism/dataset list contains no human-cell NF-kappaB/TAK1
    or MSX63935 fungal dataset. The inventory was retrieved successfully after an
    earlier DNS failure, both captured under055. No matching search/summary applies,
    and lack of coverage is not biological evidence.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 056-local-hits.txt and056-maintained-search.txt; bounded web discovery
    and official source retrieval.
  accessed_at: '2026-10-21T08:04:54Z'
  support: context_only
  summary: Ignored-inclusive maintained-path search found no prior target-specific
    decision/overlay/review. Exact-name/synonym searches found a real fungicidal follow-up
    and many host signaling studies, but no inspected positive exact Z antibacterial
    primary experiment resolving the2011 conflict. Secondary fungicidal summaries
    are leads only, not assay evidence.
  search_scope: rg --no-ignore --hidden identifier,label,slug throughout006 excluding.git/.venv;
    focused CHEBI:67559,NEQZWEXWOFPKOT-BYRRXHGESA-N,5z-7-oxozeaenol,LL-Z1640-2 across
    curation,reviews,reports/yaml_record_review,conf excluding queue. Web queries
    exact5Z-7-oxozeaenol plus antibacterial MIC or Pestalotia; LL-Z1640-2 plus antibacterial,antifungal,primary;
    exact2014 title/DOI and2003 TAK1 DOI. PMC,PubMed,EuropePMC,ACS and JBC routes
    inspected; ACS main text unavailable, ResearchGate offered request-only, no contact
    or paid source used.
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Identity, classification, evidence, target scope and optional fields; CURATION/HARMONIZATION.
  accessed_at: '2026-10-21T08:04:54Z'
  support: supports
  summary: A positive activity role requires the correct compound/organism/assay scope.
    Optional missing mechanism/evidence objects do not create a defect by themselves.
    Generated definition/roles must be corrected through maintained sources or adjudication,
    with scientific additions through native validated writer/history.
- evidence_id: validation
  kind: validation
  reference: Documented focused gates
  locator: 056-focused-results.json;056-schema.log,056-strict.log/tsv and056-chemistry.json.
  accessed_at: '2026-10-21T08:04:54Z'
  support: supports
  summary: Focused schema, strict and chemistry checks all exited0. Shared corpus
    gates are documented separately in the final bundle.
  snapshot_sha256: ca913b8d13cc6f2f31598a2cc66c9fc3612fb6feed69337b9c2f1201166f67a9
assessments:
- assessment_id: identity
  area: identity
  topic: Exact Z-isomer and two synonyms
  outcome: supported
  summary: Native chemical form and label are consistent; LL-Z1640-2 is confirmed
    by the source-cited primary structure characterization.
  target_ids:
  - CHEBI:67559
  evidence_ids:
  - identity
  - chemistry
  - primary-identity
- assessment_id: grounding
  area: grounding
  topic: Parents and registry
  outcome: supported
  summary: All five parents are chemically broader. Reaxys remains source-asserted
    with access limitation.
  target_ids:
  - CHEBI:67559
  evidence_ids:
  - identity
  - chemistry
- assessment_id: activity
  area: evidence
  topic: Antibacterial definition and role
  outcome: concern
  summary: The only adopted primary citation is negative in its exact purified-compound
    bacterial assay. Further positive evidence is required to justify the unqualified
    source assertion.
  target_ids:
  - CHEBI:67559
  evidence_ids:
  - primary-antibacterial
  - source
  - search
- assessment_id: host
  area: evidence
  topic: Cytotoxic/NF-kappaB definition scope
  outcome: supported
  summary: Exact Z human-cell effects support these clauses. Host TAK1 evidence must
    remain separate from antimicrobial mechanism.
  target_ids:
  - CHEBI:67559
  evidence_ids:
  - primary-host
  - host-tak1
  - adapter
- assessment_id: origin
  area: evidence
  topic: Fungal isolation
  outcome: supported
  summary: The cultured fungus and isolated exact compound support the broad native
    origin statement.
  target_ids:
  - CHEBI:67559
  evidence_ids:
  - primary-origin
- assessment_id: broader
  area: completeness
  topic: Other activity leads and optional objects
  outcome: unknown
  summary: A concrete primary fungicidal lead needs full compound mapping and assay
    inspection before reclassification; no optional-field failure or universal inactivity
    is asserted.
  target_ids:
  - CHEBI:67559
  evidence_ids:
  - additional
  - search
  - rubric
- assessment_id: ownership
  area: ownership
  topic: Source reproduction and scientific status
  outcome: supported
  summary: The row and native seed agree, but source agreement does not resolve the
    biological support conflict. Histories remain untouched and all13 hashes match.
  target_ids:
  - CHEBI:67559
  evidence_ids:
  - source
  - rubric
- assessment_id: schema
  area: schema
  topic: Focused native checks
  outcome: supported
  summary: Focused schema and strict checks pass, as does independent chemistry.
  target_ids:
  - CHEBI:67559
  evidence_ids:
  - validation
  - chemistry
findings:
- finding_id: F1
  issue_key: chebi-67559-antibacterial-source-support-conflict
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Resolve the antibacterial assertion against its cited negative experiment
  description: The only adopted primary citation reports exact purifiedZ compound5
    inactive in the tested four-bacterium diffusion assay. The positive definition/role
    assertion lacks support from that citation. Separate fungicidal literature is
    a concrete lead, so the appropriate follow-up is exact evidence adjudication and
    possible reclassification, not unconditional exclusion or a claim of universal
    inactivity.
  target_ids:
  - CHEBI:67559
  field_paths:
  - definition
  - activity_roles
  - antimicrobial_class
  evidence_ids:
  - record
  - source
  - primary-antibacterial
  - additional
  - search
  rule_id: 'native-review-checklist: Classification/Evidence'
  native_severity: major unsupported explicit activity assertion
  normalization_reason: This concerns the content of explicit source-derived claims,
    not absence of an optional evidence collection. The negative result is bounded
    to its assay.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI definition and role assertions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source assertion extraction and inventory reproduction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field selection
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Evidence-backed scope or classification adjudication
actions:
- action_id: A1
  description: Adjudicate exact Z antibacterial support and inspect the2014 fungicidal
    primary report before correcting the maintained definition/role and filing class.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:67559
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI definition and role assertions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source assertion extraction and inventory reproduction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field selection
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Evidence-backed scope or classification adjudication
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/5z-7-oxozeaenol.yaml
    role: Curator-owned evidence/discussion through write_validated_antibiotic and
      native curation history
  acceptance_checks:
  - Keep2011 purified-compound negative diffusion results separate from crude-culture
    MRSA activity, E-isomer results and host NF-kappaB/TAK1 inhibition.
  - Inspect2014 compound6 structure/name and complete assay conditions before adopting
    fungal or oomycete activity. Preserve organism taxonomy and whole-plant preventative
    endpoints; do not turn them into bacterial MICs.
  - If positive antibacterial evidence is found, cite the exact Z experiment with
    organism, method, units and limits. If other in-scope antimicrobial activity is
    verified, use a reproducible supported role/classification instead of excluding
    solely because the2011 bacterial screen was negative.
  - Any exclusion must remain conditional on failure to establish valid in-scope activity;
    the bounded search does not demonstrate universal inactivity.
  - Use authorized maintained-source/config/decision changes and reseeding for generated
    claims, validated native writer/history for scientific additions, and run focused
    schema/strict plus verify-corpus and required shared gates.
limitations:
- Reaxys8800797 was corroborated only through current ChEBI. All13 initial target/input
  hashes remain unchanged.
- The complete2011 cited primary paper and figure were inspected. The2003 TAK1 and2014
  fungicidal papers were read at complete official abstract level only; exact2014
  compound6 mapping and Pestalotia potency remain unadopted leads.
- The2015 host-kinase follow-up was identified and its official abstract inspected
  during the immediately preceding E review; full-table access was unavailable and
  no result is transferred to this record.
- The dataset inventory is a same-session source-context check and offers no human
  or relevant fungal coverage. Bounded searches neither rule out other antimicrobial
  evidence nor justify transferring effects among E/Z isomers.
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
