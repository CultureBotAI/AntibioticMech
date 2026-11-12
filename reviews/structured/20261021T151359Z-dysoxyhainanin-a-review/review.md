# Dysoxyhainanin A: supported identity and antibacterial activity with a plant-part correction

- Review: 20261021T151359Z-dysoxyhainanin-a-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:52:11Z
- Finished UTC: 2026-10-21T15:13:59Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native chemical encodings agree with current ChEBI and the independently parsed Japanese public chemical registry structure. The original supporting information identifies A as compound 1 and reports four Gram-positive strain MICs, supporting the retained antibacterial role. One minor source-provenance correction is needed: the original material was twigs and leaves, not whole plants. Exact primary absolute-stereochemical reasoning remains limited by access to the main article.

## Scope And Provenance

Entire native YAML, all identity/structure/synonym/xref/parent/role fields, definition and source provenance, source concept and deterministic minted alias, and all history entries. The single adopted primary reference and its accessible original supplement were assessed for exact A identity, isolation and antibacterial evidence.

Selection: Queue position 384; one exact record, with all thirteen original input hashes preserved and checked before assessment. Inspection confirmed that the initial ChEBI owner set was already correct.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65817 | data/antibiotics/antibacterial/dysoxyhainanin-a.yaml | generated | dysoxyhainanin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:65817 | Actual focused schema validation passed. |
| strict | passed | True | CHEBI:65817 | Actual focused strict validation passed. |
| chemistry | passed | False | CHEBI:65817 | Native SMILES/InChI independently agree in full key, formula, charge and masses; source alias mint reproduces. |
| authority-chemistry | passed | False | CHEBI:65817 | Current ChEBI molfile and J-GLOBAL displayed SMILES independently reproduce the native full stereochemical key, formula, charge and monoisotopic mass. |
| Authoritative full QC | failed | True | CHEBI:65817 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65817 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65817 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65817 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65817 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65817 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65817 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65817 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65817 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact chemical identity, systematic name and xref scope

identity: supported. Targets: CHEBI:65817.

Current ChEBI molfile, native encodings and independent J-GLOBAL SMILES agree in full stereochemical identity. The original A drawing is concordant at connectivity/relative-depiction level. Reaxys is traceable through ChEBI but was not independently inspected. No wrong structure was established.

### Structural description and plant part

evidence: concern. Targets: CHEBI:65817.

The pentacyclic rearranged oleanane and formamido structure are supported. The named source species is supported, but whole-plant material overstates the actual twigs-and-leaves collection. This bounded correction does not undermine the activity or chemical identity.

### Retained antibacterial role and exact primary observations

evidence: supported. Targets: CHEBI:65817.

The original A-specific table supports activity against four named Gram-positive strains under the reported in vitro conditions. The qualitative definition and antibacterial role are justified. The optional absence of a quantitative activity list is not a defect, and no mechanism or clinical susceptibility interpretation follows from these MICs.

### Native target, resistance, producer and dataset coverage

evidence: not_applicable. Targets: CHEBI:65817.

The native record names no protein, gene, pathway, regulator or expression dataset, so a structured adapter is not applicable. The inspected experiment establishes phenotype, not a direct molecular target. Plant extraction is not promoted to biosynthetic-producer proof. No optional biological slot needs fabrication.

### Generated source ownership, history and completeness

provenance: supported. Targets: CHEBI:65817.

The source row and maintained extractor/seeder reproduce all present fields; scientific status remains SEEDED. Original input hashes were verified before judgment and retained unchanged. The review identifies one bounded source correction without treating blank optional fields as defects.

## Findings

### F1: Specify the published twigs-and-leaves material in the definition

minor / open / confirmed; issue key: dysoxyhainanin-a-whole-plant-isolation-overstatement.

Native and current ChEBI say dysoxyhainanin A was isolated from whole plants. The original supporting information S1.2–S1.3 instead specifies authenticated twigs and leaves collected in Hainan, voucher DHTS-2005-1Y, from which compound1 was isolated. Replace whole plants with twigs and leaves, or use the less specific species-only wording if the maintained definition cannot represent plant parts.

## Recommended Actions And Acceptance Checks

### A1

Correct the plant-part phrase through the maintained source definition path.

- Use original S1.2–S1.3 to replace whole plants with twigs and leaves, retaining D. hainanense and the supported antibacterial statement. Do not add a biosynthesis claim.
- Preserve source provenance and regenerate through the maintained extractor/seeder path. The exact record graph, identifier and activity role should still agree with their sources.
- Inspect the resulting definition and run focused schema/strict plus source reproduction. If quantitative MICs are added in separate curation, retain strain, medium, endpoint, time, units and the unresolved printed inoculum anomaly.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/dysoxyhainanin-a.yaml; Entire native YAML. | supports | CHEBI:65817 is an EXACT, SEEDED neutral pentacyclic compound, C31H45NO4, key ZZTXYUVDEDOUDW-XYNNUCQCSA-N, with eight assigned tetrahedral centres and a specified exocyclic alkene. One systematic exact synonym and Reaxys accession are present. Antibacterial role CHEBI:33282 is retained. There are no targets, modes, resistance, MIC observations, producer objects, clinical claims, causal graphs or datasets. |
| owners | data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; conf/sources.yaml; Complete exact inventory row 1321; ChEBI extraction, structure copy, synonym-type mapping and role/class import paths. | supports | The native fields faithfully reproduce the three-star ChEBI row, including the whole-plant definition, role, three broader parents, exact synonym, Reaxys xref and PMID18771268 lead. The extractor retains compound citations as curator leads rather than pretending they independently support every claim. No ARO, PubChem, target, resistance, FDA or MIBiG owner row applies. Source mint and all three seed/reseed events are consistent. |
| chebi | CHEBI:65817; https://www.ebi.ac.uk/chebi/CHEBI:65817; Complete current entry, names, structure descriptors, outgoing ontology relations, registry number, species/component assertion and sole publication lead. | supports | Current ChEBI exactly retains the native full key, formula, charge, masses and systematic name. Parents are formamides CHEBI:24079, oxo monocarboxylic acid CHEBI:35871 and pentacyclic triterpenoid CHEBI:25872, each structurally broader. CHEBI:33282 is antibacterial agent. The entry continues to label the plant component whole plant; this is contradicted by the original supplement. Reaxys19175393 is verified as ChEBI provenance, not independently resolved in paid Reaxys. |
| authority-graph | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/65817; Complete original molfile; independent parsing and visual rendering compared with the original A drawing. | supports | The molfile independently produces the same full native key and eight assigned centres. Its skeleton, exocyclic alkene and relative wedge depiction agree with the displayed A structure in the original supplement. This comparison does not independently determine absolute configuration from raw spectra. |
| jglobal | J-GLOBAL:200907004239364069; https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=200907004239364069; Complete public chemical entry inspected through the web tool; displayed SMILES independently parsed. Direct download returned 503. | supports | The Japanese Science and Technology Agency registry publishes the same formula, full InChI/key and a separately encoded stereochemical SMILES, together with the same systematic name and rearranged oleanane name. The independent parser comparison supports exact structure/name consistency across the inspected registries; it is not new experimental structure elucidation. |
| original-abstract | PMID:18771268; DOI:10.1021/ol801834y; Complete original indexed abstract and bibliographic record; main publisher article unavailable. | supports | The original study distinguishes dysoxyhainanin A (1), with a contracted A ring and formamido appendage, from dysoxyhainanin B (2). It explicitly reports Gram-positive antibacterial activity for A. This supports the core definition and role at the stated qualitative scope. |
| isolation | DOI:10.1021/ol801834y supporting information; https://pstorage-acs-6854636.s3.amazonaws.com/4608808/ol801834y_si_001.pdf; Complete experimental sections S1.1–S1.3, printed page 3. | refutes | The study collected twigs and leaves of D. hainanense in Hainan in September 2005, authenticated the plant and deposited voucher DHTS-2005-1Y. Two kilograms of air-dried material yielded 10 mg A and 6 mg B after ethanol extraction, partitioning and chromatography. This directly contradicts the native whole-plant wording but does not dispute the species association. Extraction is not evidence that a particular organism biosynthesizes the compound. |
| activity | DOI:10.1021/ol801834y supporting information; Complete S1.5 and antimicrobial table, printed pages 5–6; both pages visually inspected. | supports | A compound 1 has MICs of 12.5 micrograms/mL against S. aureus ATCC25923, 6.25 against S. epidermidis ATCC12228, 12.5 against M. luteus ATCC9341 and 6.25 against B. subtilis CMCC63501. MIC is inhibition of visible growth; tests were triplicate. Broth cultures use Mueller Hinton medium, DMSO vehicle, 37 degrees C for 18 hours aerobically, with magnolol controls. A is greater than 50 micrograms/mL against E. coli ATCC25922, H. pylori SS1 and ATCC43504, and C. albicans labelled ACTT1600. These are bounded strain/assay observations, not species-wide resistance or clinical breakpoints. The printed inoculum exponent is anomalous and must not be silently repaired. |
| primary-structure | DOI:10.1021/ol801834y supporting information; Contents, crystallography subsection S1.4 and displayed A structures in S2 page 7 and S5 page 10 inspected; labelled EIMS molecular ion viewed. | supports | The supplement separately labels A and B and depicts A with the formamido-containing exocyclic alkene, rearranged pentacyclic core and carboxylic acid. The displayed A EIMS has an m/z495 molecular-ion label, consistent at nominal-mass level with native C31H45NO4. The diffraction data and CCDC656630 belong to B, not A; they are not treated as A absolute-stereochemistry proof. Complete NMR correlations and raw spectra were not reinterpreted. |
| search | 384-inclusive-hits.txt; 384-curation-hits.txt; Ignored-inclusive native-input and historical-evidence search; bounded public original-source search. | context_only | The local search found the raw/native entries, path lock, generated projections and readiness queue. A focused ignored-inclusive curation/conf/reports/reviews search found no exact corrective overlay. Public exact-name/DOI queries recovered the original abstract and original SI, while the main publisher route returned403 and author-linked pages offered only the abstract. Secondary grouped MIC ranges and vendor summaries were not used to assign A-specific measurements. |
| validation | 384-schema.log; 384-strict.log; 384-chemistry.json; 384-xref-chemistry.json; Actual focused validators and independent chemistry; unchanged-input hash recheck. | supports | All four executed checks passed. Native, official ChEBI molfile and J-GLOBAL displayed SMILES yield the same full key, formula and charge. Deterministic validation supports representation consistency but does not substitute for primary assay or absolute-stereochemical evidence. |

## Limits And Additional Notes

- The main 2008 publisher article returned403 and was not obtained from an authorized free route. The complete indexed abstract and original supplementary experimental sections were read; primary reasoning for all absolute configurations was not independently reconstructed.
- Original supporting information pages3–6 were read, with pages5–6 visually checked; A structures and labelled EIMS were inspected on pages7 and10. Complete spectral datasets were not reprocessed. The X-ray experiment belongs to B and supplies no direct A absolute-configuration proof.
- The supplement prints the broth inoculum as 5 × 10^-5–10^-6 CFU/mL, an implausible negative-exponent range. This was visually confirmed rather than silently normalized. Quantitative reuse should retain the source anomaly or resolve it from the original protocol; the phenotype table remains explicit.
- Reaxys19175393 was verified as the adopted ChEBI registry link but its proprietary record was not accessed. J-GLOBAL was inspected through the web tool; the direct HTTP retrieval returned503.
- An initial ChEBI structure endpoint returned SVG despite its scratch .mol suffix; it was not parsed as a molfile. The actual molfile linked from the public page was separately retrieved and independently checked.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- The source study supports antibacterial activity of exact compound1 under its tested conditions. Neither optional mechanism absence nor lack of a separately curated MIC list is an additional corrective finding.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T151359Z-dysoxyhainanin-a-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Dysoxyhainanin A: supported identity and antibacterial activity with a plant-part
  correction'
started_at: '2026-10-21T14:52:11Z'
finished_at: '2026-10-21T15:13:59Z'
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
summary: 'The native chemical encodings agree with current ChEBI and the independently
  parsed Japanese public chemical registry structure. The original supporting information
  identifies A as compound 1 and reports four Gram-positive strain MICs, supporting
  the retained antibacterial role. One minor source-provenance correction is needed:
  the original material was twigs and leaves, not whole plants. Exact primary absolute-stereochemical
  reasoning remains limited by access to the main article.'
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
  - path: data/antibiotics/antibacterial/dysoxyhainanin-a.yaml
    sha256: 5a5ffbe19e35b656e5f4a8f1f22525599672f753dde6ce73bca7318f9cf3fc86
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
- target_id: CHEBI:65817
  path: data/antibiotics/antibacterial/dysoxyhainanin-a.yaml
  label: dysoxyhainanin A
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
  description: Entire native YAML, all identity/structure/synonym/xref/parent/role
    fields, definition and source provenance, source concept and deterministic minted
    alias, and all history entries. The single adopted primary reference and its accessible
    original supplement were assessed for exact A identity, isolation and antibacterial
    evidence.
  selection: Queue position 384; one exact record, with all thirteen original input
    hashes preserved and checked before assessment. Inspection confirmed that the
    initial ChEBI owner set was already correct.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65817
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Actual focused schema validation passed.
  target_ids:
  - CHEBI:65817
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/dysoxyhainanin-a.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Actual focused strict validation passed.
  target_ids:
  - CHEBI:65817
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/dysoxyhainanin-a.yaml --out /private/tmp/am-review-session/384-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Native SMILES/InChI independently agree in full key, formula, charge and
    masses; source alias mint reproduces.
  target_ids:
  - CHEBI:65817
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 384
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-chemistry
  name: authority-chemistry
  status: passed
  required: false
  summary: Current ChEBI molfile and J-GLOBAL displayed SMILES independently reproduce
    the native full stereochemical key, formula, charge and monoisotopic mass.
  target_ids:
  - CHEBI:65817
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/384-xref-check.py
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
  - CHEBI:65817
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
  - CHEBI:65817
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
  - CHEBI:65817
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
  - CHEBI:65817
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
  - CHEBI:65817
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
  - CHEBI:65817
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
  - CHEBI:65817
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
  - CHEBI:65817
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
  - CHEBI:65817
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/dysoxyhainanin-a.yaml
  locator: Entire native YAML.
  accessed_at: '2026-10-21T15:10:30Z'
  support: supports
  summary: CHEBI:65817 is an EXACT, SEEDED neutral pentacyclic compound, C31H45NO4,
    key ZZTXYUVDEDOUDW-XYNNUCQCSA-N, with eight assigned tetrahedral centres and a
    specified exocyclic alkene. One systematic exact synonym and Reaxys accession
    are present. Antibacterial role CHEBI:33282 is retained. There are no targets,
    modes, resistance, MIC observations, producer objects, clinical claims, causal
    graphs or datasets.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py; conf/sources.yaml
  locator: Complete exact inventory row 1321; ChEBI extraction, structure copy, synonym-type
    mapping and role/class import paths.
  accessed_at: '2026-10-21T15:10:30Z'
  support: supports
  summary: The native fields faithfully reproduce the three-star ChEBI row, including
    the whole-plant definition, role, three broader parents, exact synonym, Reaxys
    xref and PMID18771268 lead. The extractor retains compound citations as curator
    leads rather than pretending they independently support every claim. No ARO, PubChem,
    target, resistance, FDA or MIBiG owner row applies. Source mint and all three
    seed/reseed events are consistent.
  snapshot_sha256: cd2b864d9a5c2270248ee234fb3ea2bc9db5939409a0795a72deb6d99ea3c041
- evidence_id: chebi
  kind: authority
  reference: CHEBI:65817; https://www.ebi.ac.uk/chebi/CHEBI:65817
  locator: Complete current entry, names, structure descriptors, outgoing ontology
    relations, registry number, species/component assertion and sole publication lead.
  accessed_at: '2026-10-21T15:07:59Z'
  support: supports
  summary: Current ChEBI exactly retains the native full key, formula, charge, masses
    and systematic name. Parents are formamides CHEBI:24079, oxo monocarboxylic acid
    CHEBI:35871 and pentacyclic triterpenoid CHEBI:25872, each structurally broader.
    CHEBI:33282 is antibacterial agent. The entry continues to label the plant component
    whole plant; this is contradicted by the original supplement. Reaxys19175393 is
    verified as ChEBI provenance, not independently resolved in paid Reaxys.
  snapshot_sha256: f34a33837227648f1ab5e43a8035b0b88669b7fcfc9d1e8ba9a71997e26a922e
- evidence_id: authority-graph
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/65817
  locator: Complete original molfile; independent parsing and visual rendering compared
    with the original A drawing.
  accessed_at: '2026-10-21T15:08:28Z'
  support: supports
  summary: The molfile independently produces the same full native key and eight assigned
    centres. Its skeleton, exocyclic alkene and relative wedge depiction agree with
    the displayed A structure in the original supplement. This comparison does not
    independently determine absolute configuration from raw spectra.
  snapshot_sha256: 80d5a587c94e80fe015722c1d6b509dba01a0f06adafcd6c9a086cf71b81eccc
- evidence_id: jglobal
  kind: authority
  reference: J-GLOBAL:200907004239364069; https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=200907004239364069
  locator: Complete public chemical entry inspected through the web tool; displayed
    SMILES independently parsed. Direct download returned 503.
  accessed_at: '2026-10-21T15:10:30Z'
  support: supports
  summary: The Japanese Science and Technology Agency registry publishes the same
    formula, full InChI/key and a separately encoded stereochemical SMILES, together
    with the same systematic name and rearranged oleanane name. The independent parser
    comparison supports exact structure/name consistency across the inspected registries;
    it is not new experimental structure elucidation.
- evidence_id: original-abstract
  kind: primary_source
  reference: PMID:18771268; DOI:10.1021/ol801834y
  locator: Complete original indexed abstract and bibliographic record; main publisher
    article unavailable.
  accessed_at: '2026-10-21T15:07:59Z'
  support: supports
  summary: The original study distinguishes dysoxyhainanin A (1), with a contracted
    A ring and formamido appendage, from dysoxyhainanin B (2). It explicitly reports
    Gram-positive antibacterial activity for A. This supports the core definition
    and role at the stated qualitative scope.
  snapshot_sha256: 21e6db41e8ae9ac7d2027947fdb422ffbc222bb8eb566515a325ebefc82f69f8
- evidence_id: isolation
  kind: primary_source
  reference: DOI:10.1021/ol801834y supporting information; https://pstorage-acs-6854636.s3.amazonaws.com/4608808/ol801834y_si_001.pdf
  locator: Complete experimental sections S1.1–S1.3, printed page 3.
  accessed_at: '2026-10-21T15:07:59Z'
  support: refutes
  summary: The study collected twigs and leaves of D. hainanense in Hainan in September
    2005, authenticated the plant and deposited voucher DHTS-2005-1Y. Two kilograms
    of air-dried material yielded 10 mg A and 6 mg B after ethanol extraction, partitioning
    and chromatography. This directly contradicts the native whole-plant wording but
    does not dispute the species association. Extraction is not evidence that a particular
    organism biosynthesizes the compound.
  snapshot_sha256: 7bed6ce2cc85a3ccbd3434193578235f9f6496f756b4ebf1545b4eb7be3ae977
- evidence_id: activity
  kind: primary_source
  reference: DOI:10.1021/ol801834y supporting information
  locator: Complete S1.5 and antimicrobial table, printed pages 5–6; both pages visually
    inspected.
  accessed_at: '2026-10-21T15:07:59Z'
  support: supports
  summary: A compound 1 has MICs of 12.5 micrograms/mL against S. aureus ATCC25923,
    6.25 against S. epidermidis ATCC12228, 12.5 against M. luteus ATCC9341 and 6.25
    against B. subtilis CMCC63501. MIC is inhibition of visible growth; tests were
    triplicate. Broth cultures use Mueller Hinton medium, DMSO vehicle, 37 degrees
    C for 18 hours aerobically, with magnolol controls. A is greater than 50 micrograms/mL
    against E. coli ATCC25922, H. pylori SS1 and ATCC43504, and C. albicans labelled
    ACTT1600. These are bounded strain/assay observations, not species-wide resistance
    or clinical breakpoints. The printed inoculum exponent is anomalous and must not
    be silently repaired.
  snapshot_sha256: 7bed6ce2cc85a3ccbd3434193578235f9f6496f756b4ebf1545b4eb7be3ae977
- evidence_id: primary-structure
  kind: primary_source
  reference: DOI:10.1021/ol801834y supporting information
  locator: Contents, crystallography subsection S1.4 and displayed A structures in
    S2 page 7 and S5 page 10 inspected; labelled EIMS molecular ion viewed.
  accessed_at: '2026-10-21T15:07:59Z'
  support: supports
  summary: The supplement separately labels A and B and depicts A with the formamido-containing
    exocyclic alkene, rearranged pentacyclic core and carboxylic acid. The displayed
    A EIMS has an m/z495 molecular-ion label, consistent at nominal-mass level with
    native C31H45NO4. The diffraction data and CCDC656630 belong to B, not A; they
    are not treated as A absolute-stereochemistry proof. Complete NMR correlations
    and raw spectra were not reinterpreted.
  snapshot_sha256: 7bed6ce2cc85a3ccbd3434193578235f9f6496f756b4ebf1545b4eb7be3ae977
- evidence_id: search
  kind: search
  reference: 384-inclusive-hits.txt; 384-curation-hits.txt
  locator: Ignored-inclusive native-input and historical-evidence search; bounded
    public original-source search.
  accessed_at: '2026-10-21T15:10:30Z'
  support: context_only
  summary: The local search found the raw/native entries, path lock, generated projections
    and readiness queue. A focused ignored-inclusive curation/conf/reports/reviews
    search found no exact corrective overlay. Public exact-name/DOI queries recovered
    the original abstract and original SI, while the main publisher route returned403
    and author-linked pages offered only the abstract. Secondary grouped MIC ranges
    and vendor summaries were not used to assign A-specific measurements.
  search_scope: '2026-10-21: rg --no-ignore --hidden across data, curation, conf,
    scripts, src, docs, .claude, reviews and reports for dysoxyhainanin and CHEBI:65817,
    followed by a focused ignored-inclusive curation/conf/reports/reviews search including
    ZZTXYUVDEDOUDW. Public searches used the exact compound name, PMID18771268 and
    DOI10.1021/ol801834y with full-text, structure and antibacterial terms.'
  snapshot_sha256: eae005c80d861d7535dd098304dc7aa61df40f48205e5e3bac7c23a2041c1a77
- evidence_id: validation
  kind: validation
  reference: 384-schema.log; 384-strict.log; 384-chemistry.json; 384-xref-chemistry.json
  locator: Actual focused validators and independent chemistry; unchanged-input hash
    recheck.
  accessed_at: '2026-10-21T15:10:30Z'
  support: supports
  summary: All four executed checks passed. Native, official ChEBI molfile and J-GLOBAL
    displayed SMILES yield the same full key, formula and charge. Deterministic validation
    supports representation consistency but does not substitute for primary assay
    or absolute-stereochemical evidence.
  snapshot_sha256: 4e766623e65e85a3ae6f25edabad9c37effe1d8158c065cb57c19b5d4475964a
assessments:
- assessment_id: identity
  area: identity
  topic: Exact chemical identity, systematic name and xref scope
  outcome: supported
  summary: Current ChEBI molfile, native encodings and independent J-GLOBAL SMILES
    agree in full stereochemical identity. The original A drawing is concordant at
    connectivity/relative-depiction level. Reaxys is traceable through ChEBI but was
    not independently inspected. No wrong structure was established.
  target_ids:
  - CHEBI:65817
  evidence_ids:
  - native
  - chebi
  - authority-graph
  - jglobal
  - primary-structure
  - validation
- assessment_id: definition
  area: evidence
  topic: Structural description and plant part
  outcome: concern
  summary: The pentacyclic rearranged oleanane and formamido structure are supported.
    The named source species is supported, but whole-plant material overstates the
    actual twigs-and-leaves collection. This bounded correction does not undermine
    the activity or chemical identity.
  target_ids:
  - CHEBI:65817
  evidence_ids:
  - chebi
  - original-abstract
  - isolation
  - primary-structure
- assessment_id: activity
  area: evidence
  topic: Retained antibacterial role and exact primary observations
  outcome: supported
  summary: The original A-specific table supports activity against four named Gram-positive
    strains under the reported in vitro conditions. The qualitative definition and
    antibacterial role are justified. The optional absence of a quantitative activity
    list is not a defect, and no mechanism or clinical susceptibility interpretation
    follows from these MICs.
  target_ids:
  - CHEBI:65817
  evidence_ids:
  - original-abstract
  - activity
  - chebi
- assessment_id: mechanism
  area: evidence
  topic: Native target, resistance, producer and dataset coverage
  outcome: not_applicable
  summary: The native record names no protein, gene, pathway, regulator or expression
    dataset, so a structured adapter is not applicable. The inspected experiment establishes
    phenotype, not a direct molecular target. Plant extraction is not promoted to
    biosynthetic-producer proof. No optional biological slot needs fabrication.
  target_ids:
  - CHEBI:65817
  evidence_ids:
  - native
  - activity
  - isolation
- assessment_id: provenance
  area: provenance
  topic: Generated source ownership, history and completeness
  outcome: supported
  summary: The source row and maintained extractor/seeder reproduce all present fields;
    scientific status remains SEEDED. Original input hashes were verified before judgment
    and retained unchanged. The review identifies one bounded source correction without
    treating blank optional fields as defects.
  target_ids:
  - CHEBI:65817
  evidence_ids:
  - owners
  - native
  - search
  - validation
findings:
- finding_id: F1
  issue_key: dysoxyhainanin-a-whole-plant-isolation-overstatement
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Specify the published twigs-and-leaves material in the definition
  description: Native and current ChEBI say dysoxyhainanin A was isolated from whole
    plants. The original supporting information S1.2–S1.3 instead specifies authenticated
    twigs and leaves collected in Hainan, voucher DHTS-2005-1Y, from which compound1
    was isolated. Replace whole plants with twigs and leaves, or use the less specific
    species-only wording if the maintained definition cannot represent plant parts.
  target_ids:
  - CHEBI:65817
  field_paths:
  - definition
  evidence_ids:
  - native
  - owners
  - chebi
  - isolation
  rule_id: Preserve source material and narrowest supported provenance scope
  native_severity: minor
  normalization_reason: The species, compound identity and antibacterial activity
    remain supported. The defect is a bounded overstatement of the harvested plant
    part, not proof of a different compound or producer.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted source definition
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source-specific definition qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition emission
actions:
- action_id: A1
  description: Correct the plant-part phrase through the maintained source definition
    path.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:65817
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted source definition
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source-specific definition qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition emission
  acceptance_checks:
  - Use original S1.2–S1.3 to replace whole plants with twigs and leaves, retaining
    D. hainanense and the supported antibacterial statement. Do not add a biosynthesis
    claim.
  - Preserve source provenance and regenerate through the maintained extractor/seeder
    path. The exact record graph, identifier and activity role should still agree
    with their sources.
  - Inspect the resulting definition and run focused schema/strict plus source reproduction.
    If quantitative MICs are added in separate curation, retain strain, medium, endpoint,
    time, units and the unresolved printed inoculum anomaly.
limitations:
- The main 2008 publisher article returned403 and was not obtained from an authorized
  free route. The complete indexed abstract and original supplementary experimental
  sections were read; primary reasoning for all absolute configurations was not independently
  reconstructed.
- Original supporting information pages3–6 were read, with pages5–6 visually checked;
  A structures and labelled EIMS were inspected on pages7 and10. Complete spectral
  datasets were not reprocessed. The X-ray experiment belongs to B and supplies no
  direct A absolute-configuration proof.
- The supplement prints the broth inoculum as 5 × 10^-5–10^-6 CFU/mL, an implausible
  negative-exponent range. This was visually confirmed rather than silently normalized.
  Quantitative reuse should retain the source anomaly or resolve it from the original
  protocol; the phenotype table remains explicit.
- Reaxys19175393 was verified as the adopted ChEBI registry link but its proprietary
  record was not accessed. J-GLOBAL was inspected through the web tool; the direct
  HTTP retrieval returned503.
- An initial ChEBI structure endpoint returned SVG despite its scratch .mol suffix;
  it was not parsed as a molfile. The actual molfile linked from the public page was
  separately retrieved and independently checked.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- The source study supports antibacterial activity of exact compound1 under its tested
  conditions. Neither optional mechanism absence nor lack of a separately curated
  MIC list is an additional corrective finding.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
