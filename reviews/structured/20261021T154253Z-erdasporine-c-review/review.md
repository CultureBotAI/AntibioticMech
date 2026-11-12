# Erdasporine C: conflicting hydrogenation in the native SMILES and InChI

- Review: 20261021T154253Z-erdasporine-c-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T15:13:52Z
- Finished UTC: 2026-10-21T15:42:53Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native SMILES parses to a molecule with two fewer hydrogens than the stored formula and InChI. Current ChEBI repeats this discrepancy. The official molfile, adopted MIBiG graph and original compound 3 drawing support the stored InChI constitution. One identity blocker requires correction through the maintained source path. The unassigned stereocentre and the spontaneous final oxidation are preserved as scope boundaries, without inferring a racemate or a direct enzyme-catalyzed final step.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 410; one entire native record. All thirteen initial input hashes were verified before judgment and retained. Actual MIBiG table and extractor owners were appended, giving fifteen captured inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:156315 | data/antibiotics/antibacterial/erdasporine-c.yaml | generated | erdasporine C |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema verification | passed | True | CHEBI:156315 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:156315 | Actual focused execution exited 0. |
| Focused chemistry verification | failed | False | CHEBI:156315 | Actual focused execution exited 1. |
| authority-map | passed | False | CHEBI:156315 | Native InChI, official ChEBI molfile and adopted MIBiG graph independently agree on full standard InChI, formula and one unassigned stereocentre. |
| graph-comparison | passed | False | CHEBI:156315 | The native SMILES parses but has two fewer hydrogen atoms and different bond orders from the official molfile. Diagnostic completion does not imply chemical agreement. |
| adapter-catalog | passed | False | CHEBI:156315 | Actual catalog inspected before mechanism follow-up and byte-identical to the immediately preceding fully read catalog. No exact environmental producer or endogenous gene mapping is supplied by native. |
| Authoritative full QC | failed | True | CHEBI:156315 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:156315 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:156315 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:156315 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:156315 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:156315 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:156315 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:156315 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:156315 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact constitution, hydrogenation and stereochemical scope

identity: concern. Targets: CHEBI:156315.

The SMILES denotes a different two-hydrogen-deficient molecule from the original drawing, stored InChI and official molfile. The unknown stereocentre is separate and does not prove a mixture. Correcting hydrogenation does not authorize assigning an absolute configuration.

### Antibacterial role and tested material

evidence: supported. Targets: CHEBI:156315.

The original compound 3 assay supports antibacterial class/role and bounded human-cell activity. Numeric MIC, IC50 and strain context are kept distinct. Optional numerical fields are not required defects.

### Environmental origin versus spontaneous oxidation

evidence: supported. Targets: CHEBI:156315.

The broad gene-cluster origin is supported, with a spontaneous final B-to-C oxidation explicitly reported. No named natural producer or direct Esp-mediated final oxidation is inferred, and the absent MIBiG producer object follows the actual stereo admission gate.

### Optional mode, targets and other biology

completeness: supported. Targets: CHEBI:156315.

The inspected original does not establish a molecular antimicrobial target. Biosynthetic proteins and host-cell activity are not targets. Empty mechanism, resistance, producer, clinical, activity, graph and dataset fields are not automatic defects for this SEEDED record.

### Maintained source, sole lead and history

provenance: supported. Targets: CHEBI:156315.

All native fields and the sole adopted lead were assessed. Three source history events are preserved, and the current ChEBI textual representation still owns the demonstrated conflict. Actual MIBiG owners were appended without replacing any initial hash.

## Findings

### F1: Reconcile the SMILES with the supported erdasporine C constitution

blocker / open / confirmed; issue key: erdasporine-c-smiles-two-hydrogen-identity-conflict.

The native SMILES parses to C22H13N3O3 and key NFUDGOUTRQELSP-UHFFFAOYSA-N, while the record states C22H15N3O3 and DOZODIABNANYHJ-UHFFFAOYSA-N. The original compound 3 drawing, native InChI, current ChEBI molfile and adopted MIBiG structure all support the latter hydrogenation state. Two indolic N–H groups are missing from the SMILES, with altered bond orders. Correct the source-owned representation without assigning the unresolved stereocentre or replacing the exact compound with a sibling.

## Recommended Actions And Acceptance Checks

### A1

Correct the maintained SMILES encoding to the independently supported C constitution and regenerate.

- Use the inspected original compound 3 drawing and official molfile to preserve both indolic N–H groups, the lactam, methyl ester and complete bond pattern. Retain source provenance for any normalization or override.
- Require SMILES to reproduce the stored neutral C22H15N3O3 formula, full key DOZODIABNANYHJ-UHFFFAOYSA-N and masses. Treat equivalent lactam/lactim normalization separately from the confirmed two-hydrogen difference.
- Leave the stereocentre unspecified unless exact primary evidence justifies its assignment. Do not infer a racemate, natural producer or enzyme-catalyzed final oxidation from source shorthand.
- Regenerate through the maintained source path and pass focused schema, strict, chemistry and source-reproduction checks. Preserve SEEDED status pending all separate sign-off requirements.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/erdasporine-c.yaml; Entire native YAML. | supports | The SEEDED, EXACT CHEBI156315 record has two systematic exact synonyms, four broader parents, one antibacterial role, one ChEBI source concept and three seed/reseed events. Its stored neutral formula is C22H15N3O3 with key DOZODIABNANYHJ-UHFFFAOYSA-N. The definition describes an oxo methyl ester, environmental-DNA gene-cluster origin, and HCT116/S. aureus effects. No external xrefs, target, mode, numerical activity, resistance, producer, clinical, dataset, causal-graph or discussion object is asserted. |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/mibig_producers.tsv; scripts/extract_source_inventory.py; scripts/extract_mibig_producers.py; scripts/seed_from_sources.py; conf/sources.yaml; Entire exact source rows, configured source versions and applicable extraction, structure selection and MIBiG merge code. | supports | ChEBI row 2754 supplies all native molecular fields and the sole adopted lead PMID24171465. MIBiG row 652 is compound 3 of 3 in BGC0001336, version 5, questionable quality, not expert reviewed, with expression-based evidence and uncultured-bacterium taxon 77133. Its valid graph matches the stored key but stereo_complete is false. The producer attachment first rejects this incomplete potential stereochemistry; the unnamed taxon is an additional boundary. No exact ARO, FDA or PubChem row owns the record. Original capture hashes were preserved when actual owners were appended. |
| chebi | CHEBI:156315; https://www.ebi.ac.uk/chebi/CHEBI:156315; Complete official entry, definition, names, properties and relationships. | supports | Current ChEBI repeats native SMILES, InChI, key, formula and masses, including their chemical inconsistency. Both systematic synonyms describe the oxo methyl ester. The broader parents resolve to methyl ester 25248, indolocarbazole alkaloid 37697, secondary amino compound 50995 and organic heterohexacyclic compound 51914; role 33282 is antibacterial agent. Its functional-parent relation to B is a derivative relationship, not an exact B identity or automatically required is_a parent. |
| chemical-conflict | 410-chemistry.json; 410-graph-comparison.json; https://www.ebi.ac.uk/chebi/backend/api/public/molfile/156315; Independent native SMILES and InChI parsing, nitrogen-H inspection and official molfile comparison. | refutes | The native SMILES produces C22H13N3O3, full key NFUDGOUTRQELSP-UHFFFAOYSA-N and monoisotopic mass 367.095691276. Its two indolic nitrogens have zero hydrogen and altered bond orders. The native InChI, official ChEBI molfile and adopted MIBiG SMILES instead give C22H15N3O3, DOZODIABNANYHJ-UHFFFAOYSA-N and mass 369.11134134, with both indolic N–H groups present. This two-hydrogen difference is not a resonance serialization or mobile-H tautomer difference. InChI import separately displays the equivalent lactim tautomer of the lactam; that same-formula normalization is not the reported defect. |
| valid-identity | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/156315; MIBiG:BGC0001336; Official molfile, native InChI and adopted MIBiG SMILES independently parsed. | supports | All three valid encodings agree on the full stored key, neutral formula and one unassigned tetrahedral centre at the ester-bearing lactam carbon. Neither the source drawing nor these encodings assigns an absolute hand. An unassigned centre is not proof of a mixture, racemate or opposite enantiomer. The hydrogenation conflict is independent of this unresolved stereochemical scope. |
| mibig | MIBiG:BGC0001336.5; https://mibig.secondarymetabolites.org/repository/BGC0001336.5/; Complete exact versioned public page, all compound sections, locus, quality and history. | supports | The page lists erdasporine C with C22H15N3O3 alongside A and B. BGC0001336 is active, questionable quality and complete, with experimental expression evidence for KF551865.1 positions 2596–15215, uncultured bacterium and PMID24171465. Esp proteins are biosynthetic annotations; their presence does not identify an antibacterial target. The visible annotation history ends at entry version 4 while the public route and cluster identifier are version 5; that presentation difference is not silently rewritten. |
| original | PMID:24171465; DOI:10.1021/ja408683p; PMC3878720; https://pmc.ncbi.nlm.nih.gov/articles/PMC3878720/; Complete original main article including methods and captions; Figures 2, 4 and 5 visually inspected and compound 3 independently mapped. | supports | Compound 3 is erdasporine C. Its original Figure 2 drawing contains the lactam carbonyl, methyl ester, two indolic N–H groups and a lactam N–H, matching the official molfile and stored InChI. No absolute stereochemistry is drawn. C is isolated at 1.1 mg from a 2 L EspODPM E. coli BL21 culture after 36 h. The paper explicitly observes B spontaneously oxidizing to C both during extended incubation and when purified B is held in DMSO. Thus environmental-cluster origin is supported at pathway/product level, but the final oxidation is not demonstrated as an enzyme-catalyzed step. E. coli is a heterologous host and predicted actinobacterial ancestry does not name a cultured natural producer. |
| activity | PMID:24171465; DOI:10.1021/ja408683p; Figure 2 and Bioactivity assays; Original exact-compound figure values and complete assay methods. | supports | For compound 3, Figure 2 reports S. aureus MIC 8.5 µM and HCT116 IC50 13 µM. The caption specifies µM; the methods prepare a twofold dilution series in µg/mL. S. aureus strain 6538P is tested in LB, after 10^6-fold dilution of overnight culture, for 18 h at 30°C, with MIC defined by OD600 &lt; 0.05. HCT116 ATCC CCL247 is assessed by 72 h crystal-violet biomass. The results support antibacterial classification for the tested C material without assigning an enantiomer, species-wide potency, bactericidal endpoint or molecular mechanism. |
| adapter | iModulonDB public dataset catalog; Actual complete catalog inspected before open-ended mechanism follow-up. | context_only | No exact named natural producer, native locus or transcriptomic experiment is asserted. The recovered environmental cluster cannot be mapped to a covered endogenous E. coli program merely because an E. coli strain was used for heterologous expression. Assay recipients are also distinct from producer organisms. No component summary or biological absence was inferred. |
| search | 410-inclusive-hits.txt; 410-fetch-results.json; 410-fetch2-results.json; Ignored-inclusive repository search and bounded exact-name/identity primary follow-up. | context_only | Hidden and ignored files were included across data, curation, conf, scripts, src, docs, .claude, reviews and reports. The focused override/report search finds the readiness queue but no exact curator override or earlier review. The sole adopted PMID resolves to the inspected original main article. Exact C stereochemistry/rotation and mechanism searches did not supply inspected primary evidence for an assigned hand or direct antimicrobial target; this is a bounded search limit. The 2013 SI routes returned an HTML challenge, an empty 202 response or 403, not readable spectra. |
| checks | 410-schema.log; 410-strict.log; 410-chemistry.json; 410-xref-chemistry.json; Actual focused execution and unchanged-input recheck. | supports | Schema and strict checks pass. Chemistry fails because parsed SMILES disagrees with native formula, InChIKey and masses. The source-concept minted alias reproduces. Independent valid authority graphs confirm the intended constitution; passing deterministic schema checks does not repair the molecular conflict. |

## Limits And Additional Notes

- The complete 2013 main article and original Figures 2, 4 and 5 were read, but supplementary spectra and any reported optical rotation were not obtained. No new spectral elucidation, enantiomeric composition or absolute configuration is claimed.
- The C graph has one unassigned stereocentre in native InChI, official molfile and adopted MIBiG. This is unresolved stereochemical scope, not proof that a mixture must be excluded.
- The actual production experiment uses refactored E. coli and includes spontaneous oxidation of B. It does not identify a cultured natural producer, direct antimicrobial target or clinical use.
- The original article has apparent method-reporting inconsistencies, including a 64:38 HPLC solvent ratio for B and a 100 ml human-cell dye-extraction volume. These are retained as source limits, not silently corrected or used to construct a native numerical activity object.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- The failed chemistry check is a positive contradiction between exact native encodings; it is not an inference from missing literature.
- Current ChEBI contains both the incorrect textual SMILES and a matching valid molfile. A reproducible source normalization is required rather than a record-only patch.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T154253Z-erdasporine-c-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Erdasporine C: conflicting hydrogenation in the native SMILES and InChI'
started_at: '2026-10-21T15:13:52Z'
finished_at: '2026-10-21T15:42:53Z'
reviewer:
  identity: Codex review002 subagent
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
summary: The native SMILES parses to a molecule with two fewer hydrogens than the
  stored formula and InChI. Current ChEBI repeats this discrepancy. The official molfile,
  adopted MIBiG graph and original compound 3 drawing support the stored InChI constitution.
  One identity blocker requires correction through the maintained source path. The
  unassigned stereocentre and the spontaneous final oxidation are preserved as scope
  boundaries, without inferring a racemate or a direct enzyme-catalyzed final step.
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
  - path: data/antibiotics/antibacterial/erdasporine-c.yaml
    sha256: 4bf808fac31a44ceaa5d3d92ea03d91ca8ca43b4cf572687ac52964a4edad680
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
  - path: data/raw/mibig_producers.tsv
    sha256: d55289619e77e035ed437d432dd692ab382f254c3841c9a314752ef22578a01b
    role: context
  - path: docs/CURATION.md
    sha256: a364598a9c2bdaf9e0e71895d5b7a2fd61d3e726e0ed0da12bd895cc4c30e98c
    role: context
  - path: docs/HARMONIZATION.md
    sha256: fb8b58abca016ca5a7d856fcc6f1ec2deb210e0927394a480853830b39e1f060
    role: context
  - path: scripts/extract_mibig_producers.py
    sha256: a078cdf4c9b2d09999800ab7ae03f93d3972f29b7d2f460ebbbe7d7ec6b31c53
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
- target_id: CHEBI:156315
  path: data/antibiotics/antibacterial/erdasporine-c.yaml
  label: erdasporine C
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
    path: data/raw/mibig_producers.tsv
    role: Actual maintained source input for the record
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_mibig_producers.py
    role: Actual adopted MIBiG extraction owner
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 410; one entire native record. All thirteen initial input
    hashes were verified before judgment and retained. Actual MIBiG table and extractor
    owners were appended, giving fifteen captured inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:156315
checks:
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:156315
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/erdasporine-c.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:156315
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/erdasporine-c.yaml --out /private/tmp/am-review-session/410-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: Focused chemistry verification
  status: failed
  required: false
  summary: Actual focused execution exited 1.
  target_ids:
  - CHEBI:156315
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 410
  exit_code: 1
  expected_exit_code: 0
- check_id: authority-map
  name: authority-map
  status: passed
  required: false
  summary: Native InChI, official ChEBI molfile and adopted MIBiG graph independently
    agree on full standard InChI, formula and one unassigned stereocentre.
  target_ids:
  - CHEBI:156315
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/410-xref-check.py
  exit_code: 0
  expected_exit_code: 0
- check_id: graph-comparison
  name: graph-comparison
  status: passed
  required: false
  summary: The native SMILES parses but has two fewer hydrogen atoms and different
    bond orders from the official molfile. Diagnostic completion does not imply chemical
    agreement.
  target_ids:
  - CHEBI:156315
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/410-compare.py
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-catalog
  name: adapter-catalog
  status: passed
  required: false
  summary: Actual catalog inspected before mechanism follow-up and byte-identical
    to the immediately preceding fully read catalog. No exact environmental producer
    or endogenous gene mapping is supplied by native.
  target_ids:
  - CHEBI:156315
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
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
  - CHEBI:156315
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
  - CHEBI:156315
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
  - CHEBI:156315
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
  - CHEBI:156315
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
  - CHEBI:156315
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
  - CHEBI:156315
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
  - CHEBI:156315
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
  - CHEBI:156315
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
  - CHEBI:156315
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/erdasporine-c.yaml
  locator: Entire native YAML.
  accessed_at: '2026-10-21T15:42:25Z'
  support: supports
  summary: The SEEDED, EXACT CHEBI156315 record has two systematic exact synonyms,
    four broader parents, one antibacterial role, one ChEBI source concept and three
    seed/reseed events. Its stored neutral formula is C22H15N3O3 with key DOZODIABNANYHJ-UHFFFAOYSA-N.
    The definition describes an oxo methyl ester, environmental-DNA gene-cluster origin,
    and HCT116/S. aureus effects. No external xrefs, target, mode, numerical activity,
    resistance, producer, clinical, dataset, causal-graph or discussion object is
    asserted.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/mibig_producers.tsv; scripts/extract_source_inventory.py;
    scripts/extract_mibig_producers.py; scripts/seed_from_sources.py; conf/sources.yaml
  locator: Entire exact source rows, configured source versions and applicable extraction,
    structure selection and MIBiG merge code.
  accessed_at: '2026-10-21T15:42:25Z'
  support: supports
  summary: ChEBI row 2754 supplies all native molecular fields and the sole adopted
    lead PMID24171465. MIBiG row 652 is compound 3 of 3 in BGC0001336, version 5,
    questionable quality, not expert reviewed, with expression-based evidence and
    uncultured-bacterium taxon 77133. Its valid graph matches the stored key but stereo_complete
    is false. The producer attachment first rejects this incomplete potential stereochemistry;
    the unnamed taxon is an additional boundary. No exact ARO, FDA or PubChem row
    owns the record. Original capture hashes were preserved when actual owners were
    appended.
  snapshot_sha256: b48da385dadc418948751a43fb6e28bcfaf6b2e6e8d9cee5de55cbf92bcc5b61
- evidence_id: chebi
  kind: authority
  reference: CHEBI:156315; https://www.ebi.ac.uk/chebi/CHEBI:156315
  locator: Complete official entry, definition, names, properties and relationships.
  accessed_at: '2026-10-21T15:40:38Z'
  support: supports
  summary: Current ChEBI repeats native SMILES, InChI, key, formula and masses, including
    their chemical inconsistency. Both systematic synonyms describe the oxo methyl
    ester. The broader parents resolve to methyl ester 25248, indolocarbazole alkaloid
    37697, secondary amino compound 50995 and organic heterohexacyclic compound 51914;
    role 33282 is antibacterial agent. Its functional-parent relation to B is a derivative
    relationship, not an exact B identity or automatically required is_a parent.
  snapshot_sha256: 88fed79709664f281c46a73c224a93cfdcaae70b196ddd874b33ac6e76c9491e
- evidence_id: chemical-conflict
  kind: validation
  reference: 410-chemistry.json; 410-graph-comparison.json; https://www.ebi.ac.uk/chebi/backend/api/public/molfile/156315
  locator: Independent native SMILES and InChI parsing, nitrogen-H inspection and
    official molfile comparison.
  accessed_at: '2026-10-21T15:42:25Z'
  support: refutes
  summary: The native SMILES produces C22H13N3O3, full key NFUDGOUTRQELSP-UHFFFAOYSA-N
    and monoisotopic mass 367.095691276. Its two indolic nitrogens have zero hydrogen
    and altered bond orders. The native InChI, official ChEBI molfile and adopted
    MIBiG SMILES instead give C22H15N3O3, DOZODIABNANYHJ-UHFFFAOYSA-N and mass 369.11134134,
    with both indolic N–H groups present. This two-hydrogen difference is not a resonance
    serialization or mobile-H tautomer difference. InChI import separately displays
    the equivalent lactim tautomer of the lactam; that same-formula normalization
    is not the reported defect.
  snapshot_sha256: 537d0376204f20cde4af78d3960538c54191d355152bc7bff7bfe4dc0b85d07b
- evidence_id: valid-identity
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/156315; MIBiG:BGC0001336
  locator: Official molfile, native InChI and adopted MIBiG SMILES independently parsed.
  accessed_at: '2026-10-21T15:42:25Z'
  support: supports
  summary: All three valid encodings agree on the full stored key, neutral formula
    and one unassigned tetrahedral centre at the ester-bearing lactam carbon. Neither
    the source drawing nor these encodings assigns an absolute hand. An unassigned
    centre is not proof of a mixture, racemate or opposite enantiomer. The hydrogenation
    conflict is independent of this unresolved stereochemical scope.
  snapshot_sha256: 10e9c92fff4d628d39aca7e97ed6eeb31ed3479c53a5097cd53b02070ad8622b
- evidence_id: mibig
  kind: authority
  reference: MIBiG:BGC0001336.5; https://mibig.secondarymetabolites.org/repository/BGC0001336.5/
  locator: Complete exact versioned public page, all compound sections, locus, quality
    and history.
  accessed_at: '2026-10-21T15:41:12Z'
  support: supports
  summary: The page lists erdasporine C with C22H15N3O3 alongside A and B. BGC0001336
    is active, questionable quality and complete, with experimental expression evidence
    for KF551865.1 positions 2596–15215, uncultured bacterium and PMID24171465. Esp
    proteins are biosynthetic annotations; their presence does not identify an antibacterial
    target. The visible annotation history ends at entry version 4 while the public
    route and cluster identifier are version 5; that presentation difference is not
    silently rewritten.
  snapshot_sha256: b3589310b7d5c0dd41a536991376d3fcb10b78ccc4ad239c823dfb721bc2ad0f
- evidence_id: original
  kind: primary_source
  reference: PMID:24171465; DOI:10.1021/ja408683p; PMC3878720; https://pmc.ncbi.nlm.nih.gov/articles/PMC3878720/
  locator: Complete original main article including methods and captions; Figures
    2, 4 and 5 visually inspected and compound 3 independently mapped.
  accessed_at: '2026-10-21T15:33:24Z'
  support: supports
  summary: Compound 3 is erdasporine C. Its original Figure 2 drawing contains the
    lactam carbonyl, methyl ester, two indolic N–H groups and a lactam N–H, matching
    the official molfile and stored InChI. No absolute stereochemistry is drawn. C
    is isolated at 1.1 mg from a 2 L EspODPM E. coli BL21 culture after 36 h. The
    paper explicitly observes B spontaneously oxidizing to C both during extended
    incubation and when purified B is held in DMSO. Thus environmental-cluster origin
    is supported at pathway/product level, but the final oxidation is not demonstrated
    as an enzyme-catalyzed step. E. coli is a heterologous host and predicted actinobacterial
    ancestry does not name a cultured natural producer.
  snapshot_sha256: 82b5c3c92b3de3699cc4f04829b58103c1c34247f1ce15cc8839c68f860df40b
- evidence_id: activity
  kind: primary_source
  reference: PMID:24171465; DOI:10.1021/ja408683p; Figure 2 and Bioactivity assays
  locator: Original exact-compound figure values and complete assay methods.
  accessed_at: '2026-10-21T15:35:24Z'
  support: supports
  summary: For compound 3, Figure 2 reports S. aureus MIC 8.5 µM and HCT116 IC50 13
    µM. The caption specifies µM; the methods prepare a twofold dilution series in
    µg/mL. S. aureus strain 6538P is tested in LB, after 10^6-fold dilution of overnight
    culture, for 18 h at 30°C, with MIC defined by OD600 < 0.05. HCT116 ATCC CCL247
    is assessed by 72 h crystal-violet biomass. The results support antibacterial
    classification for the tested C material without assigning an enantiomer, species-wide
    potency, bactericidal endpoint or molecular mechanism.
  snapshot_sha256: 08d4a3bc4ca6d2ce42376c066f5ee0598d8e77c1199cacf81144590a2db9adba
- evidence_id: adapter
  kind: database
  reference: iModulonDB public dataset catalog
  locator: Actual complete catalog inspected before open-ended mechanism follow-up.
  accessed_at: '2026-10-21T15:42:25Z'
  support: context_only
  summary: No exact named natural producer, native locus or transcriptomic experiment
    is asserted. The recovered environmental cluster cannot be mapped to a covered
    endogenous E. coli program merely because an E. coli strain was used for heterologous
    expression. Assay recipients are also distinct from producer organisms. No component
    summary or biological absence was inferred.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: search
  kind: search
  reference: 410-inclusive-hits.txt; 410-fetch-results.json; 410-fetch2-results.json
  locator: Ignored-inclusive repository search and bounded exact-name/identity primary
    follow-up.
  accessed_at: '2026-10-21T15:42:25Z'
  support: context_only
  summary: Hidden and ignored files were included across data, curation, conf, scripts,
    src, docs, .claude, reviews and reports. The focused override/report search finds
    the readiness queue but no exact curator override or earlier review. The sole
    adopted PMID resolves to the inspected original main article. Exact C stereochemistry/rotation
    and mechanism searches did not supply inspected primary evidence for an assigned
    hand or direct antimicrobial target; this is a bounded search limit. The 2013
    SI routes returned an HTML challenge, an empty 202 response or 403, not readable
    spectra.
  search_scope: '2026-10-21: rg --no-ignore --hidden searches for CHEBI:156315, erdasporine
    C/name/slug and DOZODIABNANYHJ across the stated repository paths. Public search
    queries included "erdasporine C" stereochemistry rotation and "erdasporine C"
    antibacterial mechanism; exact official ChEBI/MIBiG routes and the adopted PMID
    were inspected. Search snippets and computational BGC similarities were not promoted
    to producer, structure or mechanism proof.'
  snapshot_sha256: c0795d62a334d73a10567023343818379057435c21cdd4e9dbe3c6c9ce796670
- evidence_id: checks
  kind: validation
  reference: 410-schema.log; 410-strict.log; 410-chemistry.json; 410-xref-chemistry.json
  locator: Actual focused execution and unchanged-input recheck.
  accessed_at: '2026-10-21T15:42:25Z'
  support: supports
  summary: Schema and strict checks pass. Chemistry fails because parsed SMILES disagrees
    with native formula, InChIKey and masses. The source-concept minted alias reproduces.
    Independent valid authority graphs confirm the intended constitution; passing
    deterministic schema checks does not repair the molecular conflict.
  snapshot_sha256: a411433ae2fa2bb5314cf437e01a14014ad278aa2656b67fbd909905e3f8481b
assessments:
- assessment_id: identity
  area: identity
  topic: Exact constitution, hydrogenation and stereochemical scope
  outcome: concern
  summary: The SMILES denotes a different two-hydrogen-deficient molecule from the
    original drawing, stored InChI and official molfile. The unknown stereocentre
    is separate and does not prove a mixture. Correcting hydrogenation does not authorize
    assigning an absolute configuration.
  target_ids:
  - CHEBI:156315
  evidence_ids:
  - native
  - chebi
  - chemical-conflict
  - valid-identity
  - original
- assessment_id: classification
  area: evidence
  topic: Antibacterial role and tested material
  outcome: supported
  summary: The original compound 3 assay supports antibacterial class/role and bounded
    human-cell activity. Numeric MIC, IC50 and strain context are kept distinct. Optional
    numerical fields are not required defects.
  target_ids:
  - CHEBI:156315
  evidence_ids:
  - activity
  - original
  - chebi
- assessment_id: biosynthesis
  area: evidence
  topic: Environmental origin versus spontaneous oxidation
  outcome: supported
  summary: The broad gene-cluster origin is supported, with a spontaneous final B-to-C
    oxidation explicitly reported. No named natural producer or direct Esp-mediated
    final oxidation is inferred, and the absent MIBiG producer object follows the
    actual stereo admission gate.
  target_ids:
  - CHEBI:156315
  evidence_ids:
  - original
  - owners
  - mibig
  - adapter
- assessment_id: coverage
  area: completeness
  topic: Optional mode, targets and other biology
  outcome: supported
  summary: The inspected original does not establish a molecular antimicrobial target.
    Biosynthetic proteins and host-cell activity are not targets. Empty mechanism,
    resistance, producer, clinical, activity, graph and dataset fields are not automatic
    defects for this SEEDED record.
  target_ids:
  - CHEBI:156315
  evidence_ids:
  - native
  - original
  - search
- assessment_id: provenance
  area: provenance
  topic: Maintained source, sole lead and history
  outcome: supported
  summary: All native fields and the sole adopted lead were assessed. Three source
    history events are preserved, and the current ChEBI textual representation still
    owns the demonstrated conflict. Actual MIBiG owners were appended without replacing
    any initial hash.
  target_ids:
  - CHEBI:156315
  evidence_ids:
  - owners
  - chebi
  - checks
  - search
findings:
- finding_id: F1
  issue_key: erdasporine-c-smiles-two-hydrogen-identity-conflict
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Reconcile the SMILES with the supported erdasporine C constitution
  description: The native SMILES parses to C22H13N3O3 and key NFUDGOUTRQELSP-UHFFFAOYSA-N,
    while the record states C22H15N3O3 and DOZODIABNANYHJ-UHFFFAOYSA-N. The original
    compound 3 drawing, native InChI, current ChEBI molfile and adopted MIBiG structure
    all support the latter hydrogenation state. Two indolic N–H groups are missing
    from the SMILES, with altered bond orders. Correct the source-owned representation
    without assigning the unresolved stereocentre or replacing the exact compound
    with a sibling.
  target_ids:
  - CHEBI:156315
  field_paths:
  - chemical_structure.smiles
  - chemical_structure.standard_inchi
  - chemical_structure.standard_inchi_key
  - chemical_structure.molecular_formula
  evidence_ids:
  - native
  - chemical-conflict
  - valid-identity
  - original
  - checks
  rule_id: Exact molecular encodings must denote the same compound; a valid graph
    with wrong composition is an identity defect
  native_severity: blocker
  normalization_reason: Unlike a merely unparseable encoding, the native SMILES successfully
    denotes a different hydrogenation state with a different formula and full key.
    This is a confirmed exact-identity conflict; its correction does not depend on
    resolving absolute stereochemistry.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted contradictory SMILES
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source structure extraction and normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated exact molecular representation
actions:
- action_id: A1
  description: Correct the maintained SMILES encoding to the independently supported
    C constitution and regenerate.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:156315
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted contradictory SMILES
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source structure extraction and normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated exact molecular representation
  acceptance_checks:
  - Use the inspected original compound 3 drawing and official molfile to preserve
    both indolic N–H groups, the lactam, methyl ester and complete bond pattern. Retain
    source provenance for any normalization or override.
  - Require SMILES to reproduce the stored neutral C22H15N3O3 formula, full key DOZODIABNANYHJ-UHFFFAOYSA-N
    and masses. Treat equivalent lactam/lactim normalization separately from the confirmed
    two-hydrogen difference.
  - Leave the stereocentre unspecified unless exact primary evidence justifies its
    assignment. Do not infer a racemate, natural producer or enzyme-catalyzed final
    oxidation from source shorthand.
  - Regenerate through the maintained source path and pass focused schema, strict,
    chemistry and source-reproduction checks. Preserve SEEDED status pending all separate
    sign-off requirements.
limitations:
- The complete 2013 main article and original Figures 2, 4 and 5 were read, but supplementary
  spectra and any reported optical rotation were not obtained. No new spectral elucidation,
  enantiomeric composition or absolute configuration is claimed.
- The C graph has one unassigned stereocentre in native InChI, official molfile and
  adopted MIBiG. This is unresolved stereochemical scope, not proof that a mixture
  must be excluded.
- The actual production experiment uses refactored E. coli and includes spontaneous
  oxidation of B. It does not identify a cultured natural producer, direct antimicrobial
  target or clinical use.
- The original article has apparent method-reporting inconsistencies, including a
  64:38 HPLC solvent ratio for B and a 100 ml human-cell dye-extraction volume. These
  are retained as source limits, not silently corrected or used to construct a native
  numerical activity object.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- The failed chemistry check is a positive contradiction between exact native encodings;
  it is not an inference from missing literature.
- Current ChEBI contains both the incorrect textual SMILES and a matching valid molfile.
  A reproducible source normalization is required rather than a record-only patch.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
