# Amikacin disulfate: exact identity and26 verified FDA product assertions

- Review: 20261021T085252Z-amikacin-disulfate
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:41:33Z
- Finished UTC: 2026-10-21T08:52:52Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

Exact1:2 sulfate identity and all26 FDA product assertions are supported, with no demonstrated native corrective defect. Exclude three homonymous nutrition-product citation leads. Future mechanism enrichment must preserve amikacin active-moiety and reagent-composition scope. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole-record review of exact amikacin disulfate.

Selection: Queue091 in isolated batch010.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:2638 | data/antibiotics/antibacterial/amikacin-disulfate.yaml | generated | amikacin disulfate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | CHEBI:2638 | Actual command passed. |
| Focused strict | passed | True | CHEBI:2638 | Actual command passed. |
| Independent structure consistency | passed | True | CHEBI:2638 | Both encodings reproduce exact full key,stoichiometry,charge,masses and mint. |
| Structured adapter applicability | not_applicable | False | CHEBI:2638 | Native record names no gene,protein,pathway,regulator,stress response or transcriptomics dataset. Newly discovered mechanism literature is context only. |
| Authoritative full QC | failed | True | CHEBI:2638 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:2638 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:2638 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:2638 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:2638 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:2638 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:2638 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:2638 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:2638 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact disulfate identity

identity: supported. Targets: CHEBI:2638.

Name,definition,stoichiometry,structure,charge,masses,CAS and exact official identity agree.

### Parent and drug links

grounding: supported. Targets: CHEBI:2638.

Parent is broader; KEGG exact sulfate and DrugBank drug-level links are placed appropriately. Reaxys remains source-asserted.

### Approval and product marketing claims

evidence: supported. Targets: CHEBI:2638.

All26 claims match the current official FDA data, with discontinued/marketed distinction preserved. GSRS verifies exact ingredient structure; liposomal formulation does not imply universal indications.

### Antibacterial clinical role

evidence: supported. Targets: CHEBI:2638.

Official injectable and liposomal labels substantiate antibacterial-drug and antimicrobial roles. Native does not inflate this into strain-wide quantitative activity or unrestricted clinical efficacy.

### Adopted citation relevance

scope: supported. Targets: CHEBI:2638.

Three homonymous nutrition-product papers are excluded from antibiotic evidence; exact disulfate solid-state metadata is not an assay. None is attached as unsupported native evidence.

### Potential primary mechanism annotation

completeness: unknown. Targets: CHEBI:2638.

Primary2023 amikacin work supports RNA/ribosome mechanism enrichment once reagent and active-moiety scope are explicit. Native blank optional fields are not themselves a defect; no unqualified direct protein target or exact-salt quantitative observation is warranted.

### Producer,resistance,dataset and graph assertions

scope: not_applicable. Targets: CHEBI:2638.

No such native assertions require sign-off. The2023 mutant data can be a scoped future resistance lead; clinical formulation and aminoglycoside-family facts are not producer evidence.

### Ownership,mint and history

provenance: supported. Targets: CHEBI:2638.

All source owners were captured, source mint reproduces and six seed/reseed history events remain unchanged. Current source version differences are distinguished from native historical provenance.

### Focused validators

schema: supported. Targets: CHEBI:2638.

Native schema and strict validation pass; independent chemistry passes after equivalent formula notation is accounted for.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/amikacin-disulfate.yaml; Entire YAML | supports | Read exact disulfate definition, eight synonyms, parent, two roles, all structure fields and xrefs, source/mint, all 26 FDA product assertions and six history events. No native molecular target, mode, quantitative activity, resistance, producer, dataset or graph assertion. |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/fda_clinical_status.tsv; ChEBI row24 and FDA rows716–741; extractor and seeder | supports | Both source owners were captured before assessment. FDA extractor rejects ambiguous name/structure matches and joins exact Standard InChIKey; seeder matches application/product pairs. The 26 native assertions reproduce the adopted rows. Imported literature leads are discovery context, not native claim-level citations. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:2638; Complete current entry | supports | Current ChEBI agrees with exact disulfate identity, component formula, zero total charge, both encodings, masses, parent and antimicrobial/antibacterial-drug roles. The neutral acid/component encoding is compatible with this salt identity; it is not an assertion of solution protonation. |
| chemistry | Independent RDKit calculations; Native SMILES and InChI | supports | Both encodings yield FXKSEJFHKVNEFI-GCZBSULCSA-N, aggregate C22H47N5O21S2, charge0, three fragments, mass781.766 and exact mass781.220495524, with16 specified tetrahedral centres. Aggregate formula equals native component notation C22H43N5O13.2H2O4S. Mint reproduces. Initial helper literal formula comparison was corrected in scratch; no native defect. |
| gsrs | https://gsrs.ncats.nih.gov/api/v1/substances/N6M33094FD?view=full; Chemical structure and registry codes | supports | Live GSRS version39 retains exact native full InChI/key,16 defined stereocentres,1:2 composition and CAS39831-55-5. Native version37 records the adopted historical snapshot; version advance alone is not a discrepancy. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/38351; Full-key PUG lookup | supports | CID38351 and two other returned CIDs share the exact native Standard InChI/key, neutral charge, aggregate formula and compatible masses. |
| parent | https://www.ebi.ac.uk/chebi/CHEBI:38012; Parent class and incoming relation | supports | Aminoglycoside sulfate salt is broader than this exact disulfate and explicitly includes CHEBI:2638. |
| role | https://www.ebi.ac.uk/chebi/CHEBI:36047; Definition and parentage | supports | Antibacterial drug denotes a drug used to treat or prevent bacterial infections and is a subtype of antibacterial agent and antimicrobial drug. |
| kegg | https://rest.kegg.jp/get/D00865; Drug entry identity and links | supports | D00865 is amikacin sulfate with1:2 formula,781.2205 exact mass,CAS39831-55-5 and ChEBI2638. It is appropriately retained under drug_xrefs. KEGG mechanism statements are database assertions, not new primary target evidence. |
| drugbank | https://go.drugbank.com/drugs/DB00479; Public page lines57–104 | partial | DB00479 resolves to amikacin drug/free-base entity with key LKCWBDHBTVXHDL-RMDFUYIESA-N and formula C22H43N5O13; its native placement under drug_xrefs preserves the distinction from exact disulfate xrefs. Public web text was readable although direct download returned403. |
| fda | https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22AMIKACIN%20SULFATE%22&amp;limit=100; All26 native application/product pairs | supports | Every pair is present with matching sponsor, drug name, ingredient, original approved date and marketing status. Discontinued products retain historical approval with currently_marketed false; marketed Prescription products are correctly true. This supports APPROVED status without claiming clinical interchangeability across formulations. |
| fda-comparison | Independent native/live FDA comparison; 26 rows | supports | Application type/number and product number were joined individually; all dates,names,ingredients,sponsors and marketing statuses matched. |
| arikayce | https://api.fda.gov/drug/label.json?search=openfda.brand_name:ARIKAYCE&amp;limit=1; Label effective20260804, sections1,11,12.4 | supports | ARIKAYCE explicitly contains amikacin sulfate1:2,formula C22H43N5O13.2H2SO4,mass781.76,encapsulated in liposomes. Its limited-population accelerated approval for refractory MAC lung disease in combination is formulation-specific; product approval is legitimate evidence for this ingredient, not universal efficacy of every preparation. |
| injection | https://api.fda.gov/drug/label.json?search=openfda.unii:%22N6M33094FD%22&amp;limit=100; Injection label36fb925f-8beb-4691-9136-500772c736fa, description and microbiology | supports | Label identifies the1:2 sulfate and distinguishes doses expressed as amikacin base. It supports antibacterial clinical use and describes ribosomal protein-synthesis inhibition. Its isolated585.61 molecular weight refers to the base despite the nearby sulfate formula and does not override independent exact-salt chemistry. |
| excluded-109983 | PMID:109983; Primary abstract through Europe PMC | context_only | Comparative amino-acid nitrogen nutrition in84 surgical patients; Amikin is a nutrition preparation. This naming collision does not support amikacin antibiotic identity, activity or mechanism. The citation exists only as a raw ChEBI discovery lead, not native evidence. |
| excluded-6162275 | PMID:6162275; Primary abstract through Europe PMC | context_only | Protein-starved dogs receiving amino-acid nutrition Amikin/aminozol; tissue microscopy and metabolism. This naming collision does not support amikacin antibiotic identity, activity or mechanism. The citation exists only as a raw ChEBI discovery lead, not native evidence. |
| excluded-6800084 | PMID:6800084; Primary abstract through Europe PMC | context_only | Aminosol/Amikin nitrogen nutrition in rats and liver enzyme responses. This naming collision does not support amikacin antibiotic identity, activity or mechanism. The citation exists only as a raw ChEBI discovery lead, not native evidence. |
| crystal | PMID:3174816; 1988 Pharmazie43(5):363–364 metadata | context_only | Studies of the crystalline forms of amikacin disulphate is an exact-name solid-state lead. No abstract or accessible experimental text was obtained; no crystal-form or potency result is inferred from its title. |
| ribosome | PMID:37537169; DOI10.1038/s41467-023-40416-5; Results and Methods | partial | Full main text describes T.thermophilus X-ray and E.coli cryo-EM ribosome complexes plus kinetic inhibition and A1408G-mutant testing. The primary functional site is16S-rRNA h44; the observed50S P-site interaction does not establish a second functional inhibitory mechanism. B5 binding is T.thermophilus-specific, absent in E.coli. This is strong amikacin-moiety mechanism context, not a universal direct protein target or an exact-disulfate MIC transfer. |
| reagent | https://www.sigmaaldrich.com/US/en/product/sigma/a2324; Manufacturer identity and Analysis Note; compared with2023 Methods | context_only | 2023 Methods lists amikacin sulfate and kanamycin sulfate with apparently reversed K-1876/A-2324 catalog assignments. Current A2324 page names amikacin sulfate and reports amikacin:sulfate1:1.8, distinct from exact1:2 salt; its displayed structure also differs. Historical lot composition is unverified. Resolve reagent mapping before importing quantitative results; do not discard the experimentally observed amikacin-moiety binding. |
| gates | just validate; just validate-strict; Actual focused commands in batch010 | supports | Both exit0 with one record and zero strict ERROR rows. |
| search | CultureBotAI/AntibioticMech; Ignored-inclusive exact-record/source search | context_only | Identifier,label and slug were searched including ignored files; source owners, maintained curation,PATHS and generated references were inspected. Free official identity,FDA and primary literature follow-up was bounded to this salt. Reaxys exact content was not independently accessible. |

## Limits And Additional Notes

- Reaxys registry content could not be independently inspected; its identifier remains a current ChEBI assertion.
- PMID3174816 experimental text was unavailable; no solid-state result was inferred from metadata.
- The2023 mechanistic study has a catalog-number ordering discrepancy and current A2324 is nonstoichiometric sulfate. Historical preparation composition and quantitative transfer to exact disulfate remain unresolved.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All22 input hashes rechecked unchanged; no native edits.
- Curator follow-up: use inspected2023 ribosome work for explicit active-moiety mechanism context after reagent adjudication, retain h44 RNA complex scope, distinguish functional inhibition from observed secondary-site binding and ground any strain-level MIC with its method and tested preparation.
- Raw ChEBI literature discovery should exclude PMID109983,6162275,6800084 by compound identity rather than promote a shared brand-name match. This is a source-quality note, not an unsupported native citation finding.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T085252Z-amikacin-disulfate
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Amikacin disulfate: exact identity and26 verified FDA product assertions'
started_at: '2026-10-21T08:41:33Z'
finished_at: '2026-10-21T08:52:52Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Whole-record review, captured raw owners, independent chemistry,
    official identity/regulatory comparison and primary source inspection.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: Exact1:2 sulfate identity and all26 FDA product assertions are supported,
  with no demonstrated native corrective defect. Exclude three homonymous nutrition-product
  citation leads. Future mechanism enrichment must preserve amikacin active-moiety
  and reagent-composition scope. Scientific assessment retains the stated evidence
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
  - path: data/antibiotics/antibacterial/amikacin-disulfate.yaml
    sha256: 3458a3d2048547fc106420cad4ff665913a2e3e3c7a96705b562a49904a4bd00
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
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
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
  - path: data/raw/fda_clinical_status.tsv
    sha256: a6952f85426afa53c5704c588681a078e599ce245bf18f7c9dd390d70e7bb16c
    role: context
  - path: scripts/extract_fda_clinical_status.py
    sha256: f30f385ea6d530dc1749e3d805dbcdbc8715fbc476abc510bf144ea13964e171
    role: context
targets:
- target_id: CHEBI:2638
  path: data/antibiotics/antibacterial/amikacin-disulfate.yaml
  label: amikacin disulfate
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
    path: data/raw/fda_clinical_status.tsv
    role: Adopted FDA approval and marketing claims joined to exact GSRS structure
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_fda_clinical_status.py
    role: Maintained FDA/GSRS extraction and exact identity join
scope:
  description: Whole-record review of exact amikacin disulfate.
  selection: Queue091 in isolated batch010.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:2638
  exclusions:
  - target: Free-base amikacin,nonstoichiometric sulfate preparations and unrelated
      nutrition Amikin
    reason: Distinct identities or preparation scopes; comparator context only.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual command passed.
  target_ids:
  - CHEBI:2638
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/amikacin-disulfate.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: strict
  name: Focused strict
  status: passed
  required: true
  summary: Actual command passed.
  target_ids:
  - CHEBI:2638
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/amikacin-disulfate.yaml --out /private/tmp/am-review-session/091-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Independent structure consistency
  status: passed
  required: true
  summary: Both encodings reproduce exact full key,stoichiometry,charge,masses and
    mint.
  target_ids:
  - CHEBI:2638
  evidence_ids:
  - chemistry
- check_id: adapter
  name: Structured adapter applicability
  status: not_applicable
  required: false
  summary: Native record names no gene,protein,pathway,regulator,stress response or
    transcriptomics dataset. Newly discovered mechanism literature is context only.
  target_ids:
  - CHEBI:2638
  evidence_ids:
  - native
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:2638
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
  - CHEBI:2638
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
  - CHEBI:2638
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
  - CHEBI:2638
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
  - CHEBI:2638
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
  - CHEBI:2638
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
  - CHEBI:2638
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
  - CHEBI:2638
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
  - CHEBI:2638
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/amikacin-disulfate.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T08:46:29Z'
  support: supports
  summary: Read exact disulfate definition, eight synonyms, parent, two roles, all
    structure fields and xrefs, source/mint, all 26 FDA product assertions and six
    history events. No native molecular target, mode, quantitative activity, resistance,
    producer, dataset or graph assertion.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/fda_clinical_status.tsv
  locator: ChEBI row24 and FDA rows716–741; extractor and seeder
  accessed_at: '2026-10-21T08:46:29Z'
  support: supports
  summary: Both source owners were captured before assessment. FDA extractor rejects
    ambiguous name/structure matches and joins exact Standard InChIKey; seeder matches
    application/product pairs. The 26 native assertions reproduce the adopted rows.
    Imported literature leads are discovery context, not native claim-level citations.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:2638
  locator: Complete current entry
  accessed_at: '2026-10-21T08:44:10Z'
  support: supports
  summary: Current ChEBI agrees with exact disulfate identity, component formula,
    zero total charge, both encodings, masses, parent and antimicrobial/antibacterial-drug
    roles. The neutral acid/component encoding is compatible with this salt identity;
    it is not an assertion of solution protonation.
  snapshot_sha256: 5cdad89d71d4d66c2eef20182a4512c3f974c4657aa542ac5f362ab1f5b11d06
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit calculations
  locator: Native SMILES and InChI
  accessed_at: '2026-10-21T08:44:11Z'
  support: supports
  summary: Both encodings yield FXKSEJFHKVNEFI-GCZBSULCSA-N, aggregate C22H47N5O21S2,
    charge0, three fragments, mass781.766 and exact mass781.220495524, with16 specified
    tetrahedral centres. Aggregate formula equals native component notation C22H43N5O13.2H2O4S.
    Mint reproduces. Initial helper literal formula comparison was corrected in scratch;
    no native defect.
  snapshot_sha256: 4c12a2b07a7391ca17014de250bed3c2fd7dcc51f92cadc80f95a2cb3a3c3c2f
- evidence_id: gsrs
  kind: authority
  reference: https://gsrs.ncats.nih.gov/api/v1/substances/N6M33094FD?view=full
  locator: Chemical structure and registry codes
  accessed_at: '2026-10-21T08:44:04Z'
  support: supports
  summary: Live GSRS version39 retains exact native full InChI/key,16 defined stereocentres,1:2
    composition and CAS39831-55-5. Native version37 records the adopted historical
    snapshot; version advance alone is not a discrepancy.
  snapshot_sha256: a213e6e28558717ccad958d62db4485b058891b338e4b08b660b7650594a0ef4
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/38351
  locator: Full-key PUG lookup
  accessed_at: '2026-10-21T08:44:04Z'
  support: supports
  summary: CID38351 and two other returned CIDs share the exact native Standard InChI/key,
    neutral charge, aggregate formula and compatible masses.
  snapshot_sha256: 1a2c952e37d380ffed5b1110bdcaf720d63aecdbc9b07929348cdcda06360663
- evidence_id: parent
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:38012
  locator: Parent class and incoming relation
  accessed_at: '2026-10-21T08:44:05Z'
  support: supports
  summary: Aminoglycoside sulfate salt is broader than this exact disulfate and explicitly
    includes CHEBI:2638.
  snapshot_sha256: 526ae926e81c66bd35c5eee240dc4293cfa5670785102a457b3a508a35f340c5
- evidence_id: role
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:36047
  locator: Definition and parentage
  accessed_at: '2026-10-21T08:44:05Z'
  support: supports
  summary: Antibacterial drug denotes a drug used to treat or prevent bacterial infections
    and is a subtype of antibacterial agent and antimicrobial drug.
  snapshot_sha256: 25e5a4653a4575af20660924240df5fccda5f522e021870b41ed1008b3fbdf4d
- evidence_id: kegg
  kind: database
  reference: https://rest.kegg.jp/get/D00865
  locator: Drug entry identity and links
  accessed_at: '2026-10-21T08:44:04Z'
  support: supports
  summary: D00865 is amikacin sulfate with1:2 formula,781.2205 exact mass,CAS39831-55-5
    and ChEBI2638. It is appropriately retained under drug_xrefs. KEGG mechanism statements
    are database assertions, not new primary target evidence.
  snapshot_sha256: bd2f805adf1bc68bfff58916a22834c3d27832a116882417b23321833856829c
- evidence_id: drugbank
  kind: database
  reference: https://go.drugbank.com/drugs/DB00479
  locator: Public page lines57–104
  accessed_at: '2026-10-21T08:46:29Z'
  support: partial
  summary: DB00479 resolves to amikacin drug/free-base entity with key LKCWBDHBTVXHDL-RMDFUYIESA-N
    and formula C22H43N5O13; its native placement under drug_xrefs preserves the distinction
    from exact disulfate xrefs. Public web text was readable although direct download
    returned403.
- evidence_id: fda
  kind: authority
  reference: https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22AMIKACIN%20SULFATE%22&limit=100
  locator: All26 native application/product pairs
  accessed_at: '2026-10-21T08:44:04Z'
  support: supports
  summary: Every pair is present with matching sponsor, drug name, ingredient, original
    approved date and marketing status. Discontinued products retain historical approval
    with currently_marketed false; marketed Prescription products are correctly true.
    This supports APPROVED status without claiming clinical interchangeability across
    formulations.
  snapshot_sha256: a25184d6ed6b9e6e4bccce5da2f3be8a5f42a697231103cc44a80f5c2468f1e6
- evidence_id: fda-comparison
  kind: validation
  reference: Independent native/live FDA comparison
  locator: 26 rows
  accessed_at: '2026-10-21T08:44:26Z'
  support: supports
  summary: Application type/number and product number were joined individually; all
    dates,names,ingredients,sponsors and marketing statuses matched.
  snapshot_sha256: dc2981041839f77ec1cd4a09efcd91363fc6c80e15116e10304ffdc1171e74d9
- evidence_id: arikayce
  kind: authority
  reference: https://api.fda.gov/drug/label.json?search=openfda.brand_name:ARIKAYCE&limit=1
  locator: Label effective20260804, sections1,11,12.4
  accessed_at: '2026-10-21T08:45:02Z'
  support: supports
  summary: ARIKAYCE explicitly contains amikacin sulfate1:2,formula C22H43N5O13.2H2SO4,mass781.76,encapsulated
    in liposomes. Its limited-population accelerated approval for refractory MAC lung
    disease in combination is formulation-specific; product approval is legitimate
    evidence for this ingredient, not universal efficacy of every preparation.
  snapshot_sha256: f81fc3db8118d18ccc372dbf646654eb892e3a44ba4f8107eab82a5b01028072
- evidence_id: injection
  kind: authority
  reference: https://api.fda.gov/drug/label.json?search=openfda.unii:%22N6M33094FD%22&limit=100
  locator: Injection label36fb925f-8beb-4691-9136-500772c736fa, description and microbiology
  accessed_at: '2026-10-21T08:44:04Z'
  support: supports
  summary: Label identifies the1:2 sulfate and distinguishes doses expressed as amikacin
    base. It supports antibacterial clinical use and describes ribosomal protein-synthesis
    inhibition. Its isolated585.61 molecular weight refers to the base despite the
    nearby sulfate formula and does not override independent exact-salt chemistry.
  snapshot_sha256: acbbc8f8711c7a39f9d15932788840ba6aa1f254b9b7933fac0038c5b4769d9a
- evidence_id: excluded-109983
  kind: primary_source
  reference: PMID:109983
  locator: Primary abstract through Europe PMC
  accessed_at: '2026-10-21T08:44:30Z'
  support: context_only
  summary: Comparative amino-acid nitrogen nutrition in84 surgical patients; Amikin
    is a nutrition preparation. This naming collision does not support amikacin antibiotic
    identity, activity or mechanism. The citation exists only as a raw ChEBI discovery
    lead, not native evidence.
  snapshot_sha256: 974d4f4a0d5cb775821bfc739b5499b811d2a66720c2b07fdc36a9823effe5a3
- evidence_id: excluded-6162275
  kind: primary_source
  reference: PMID:6162275
  locator: Primary abstract through Europe PMC
  accessed_at: '2026-10-21T08:44:30Z'
  support: context_only
  summary: Protein-starved dogs receiving amino-acid nutrition Amikin/aminozol; tissue
    microscopy and metabolism. This naming collision does not support amikacin antibiotic
    identity, activity or mechanism. The citation exists only as a raw ChEBI discovery
    lead, not native evidence.
  snapshot_sha256: 9d35104b42007e228fe2275d0965227b407b09ac19338d849172ece5aadb3e3f
- evidence_id: excluded-6800084
  kind: primary_source
  reference: PMID:6800084
  locator: Primary abstract through Europe PMC
  accessed_at: '2026-10-21T08:44:33Z'
  support: context_only
  summary: Aminosol/Amikin nitrogen nutrition in rats and liver enzyme responses.
    This naming collision does not support amikacin antibiotic identity, activity
    or mechanism. The citation exists only as a raw ChEBI discovery lead, not native
    evidence.
  snapshot_sha256: f038475ad4ebbda95b4fa337e1ee43e791322644e70c90d3baf1fd45a0c0a796
- evidence_id: crystal
  kind: primary_source
  reference: PMID:3174816
  locator: 1988 Pharmazie43(5):363–364 metadata
  accessed_at: '2026-10-21T08:44:30Z'
  support: context_only
  summary: Studies of the crystalline forms of amikacin disulphate is an exact-name
    solid-state lead. No abstract or accessible experimental text was obtained; no
    crystal-form or potency result is inferred from its title.
  snapshot_sha256: 01d82b7e938217a4c40431d3dcf78a238dd622dec099e7a636bf7a2791eb202a
- evidence_id: ribosome
  kind: primary_source
  reference: PMID:37537169
  locator: DOI10.1038/s41467-023-40416-5; Results and Methods
  accessed_at: '2026-10-21T08:45:03Z'
  support: partial
  summary: Full main text describes T.thermophilus X-ray and E.coli cryo-EM ribosome
    complexes plus kinetic inhibition and A1408G-mutant testing. The primary functional
    site is16S-rRNA h44; the observed50S P-site interaction does not establish a second
    functional inhibitory mechanism. B5 binding is T.thermophilus-specific, absent
    in E.coli. This is strong amikacin-moiety mechanism context, not a universal direct
    protein target or an exact-disulfate MIC transfer.
  snapshot_sha256: 2c55435981b62655cd27bc57798382a2731efc815ba1edfa4094a782df311ea5
- evidence_id: reagent
  kind: authority
  reference: https://www.sigmaaldrich.com/US/en/product/sigma/a2324
  locator: Manufacturer identity and Analysis Note; compared with2023 Methods
  accessed_at: '2026-10-21T08:46:29Z'
  support: context_only
  summary: 2023 Methods lists amikacin sulfate and kanamycin sulfate with apparently
    reversed K-1876/A-2324 catalog assignments. Current A2324 page names amikacin
    sulfate and reports amikacin:sulfate1:1.8, distinct from exact1:2 salt; its displayed
    structure also differs. Historical lot composition is unverified. Resolve reagent
    mapping before importing quantitative results; do not discard the experimentally
    observed amikacin-moiety binding.
- evidence_id: gates
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual focused commands in batch010
  accessed_at: '2026-10-21T08:45:03Z'
  support: supports
  summary: Both exit0 with one record and zero strict ERROR rows.
  snapshot_sha256: b2a69cee26f16770014c48c0f7487cf1084bc4892e6bd13576426fc98b14ed30
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: Ignored-inclusive exact-record/source search
  accessed_at: '2026-10-21T08:46:29Z'
  support: context_only
  summary: Identifier,label and slug were searched including ignored files; source
    owners, maintained curation,PATHS and generated references were inspected. Free
    official identity,FDA and primary literature follow-up was bounded to this salt.
    Reaxys exact content was not independently accessible.
  search_scope: prepare.py91 rg --no-ignore --hidden excluding.git/.venv; source raw
    full-key joins and FDA source code; official ChEBI/GSRS/PubChem/KEGG/DrugBank/openFDA;
    all four adopted PMID leads and2023 full primary text.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact disulfate identity
  outcome: supported
  summary: Name,definition,stoichiometry,structure,charge,masses,CAS and exact official
    identity agree.
  target_ids:
  - CHEBI:2638
  evidence_ids:
  - native
  - chebi
  - chemistry
  - gsrs
  - pubchem
- assessment_id: grounding
  area: grounding
  topic: Parent and drug links
  outcome: supported
  summary: Parent is broader; KEGG exact sulfate and DrugBank drug-level links are
    placed appropriately. Reaxys remains source-asserted.
  target_ids:
  - CHEBI:2638
  evidence_ids:
  - parent
  - kegg
  - drugbank
  - search
- assessment_id: clinical
  area: evidence
  topic: Approval and product marketing claims
  outcome: supported
  summary: All26 claims match the current official FDA data, with discontinued/marketed
    distinction preserved. GSRS verifies exact ingredient structure; liposomal formulation
    does not imply universal indications.
  target_ids:
  - CHEBI:2638
  evidence_ids:
  - fda
  - fda-comparison
  - gsrs
  - arikayce
- assessment_id: activity
  area: evidence
  topic: Antibacterial clinical role
  outcome: supported
  summary: Official injectable and liposomal labels substantiate antibacterial-drug
    and antimicrobial roles. Native does not inflate this into strain-wide quantitative
    activity or unrestricted clinical efficacy.
  target_ids:
  - CHEBI:2638
  evidence_ids:
  - role
  - injection
  - arikayce
- assessment_id: literature
  area: scope
  topic: Adopted citation relevance
  outcome: supported
  summary: Three homonymous nutrition-product papers are excluded from antibiotic
    evidence; exact disulfate solid-state metadata is not an assay. None is attached
    as unsupported native evidence.
  target_ids:
  - CHEBI:2638
  evidence_ids:
  - excluded-109983
  - excluded-6162275
  - excluded-6800084
  - crystal
- assessment_id: mechanism
  area: completeness
  topic: Potential primary mechanism annotation
  outcome: unknown
  summary: Primary2023 amikacin work supports RNA/ribosome mechanism enrichment once
    reagent and active-moiety scope are explicit. Native blank optional fields are
    not themselves a defect; no unqualified direct protein target or exact-salt quantitative
    observation is warranted.
  target_ids:
  - CHEBI:2638
  evidence_ids:
  - ribosome
  - reagent
  - native
- assessment_id: other
  area: scope
  topic: Producer,resistance,dataset and graph assertions
  outcome: not_applicable
  summary: No such native assertions require sign-off. The2023 mutant data can be
    a scoped future resistance lead; clinical formulation and aminoglycoside-family
    facts are not producer evidence.
  target_ids:
  - CHEBI:2638
  evidence_ids:
  - native
  - ribosome
- assessment_id: provenance
  area: provenance
  topic: Ownership,mint and history
  outcome: supported
  summary: All source owners were captured, source mint reproduces and six seed/reseed
    history events remain unchanged. Current source version differences are distinguished
    from native historical provenance.
  target_ids:
  - CHEBI:2638
  evidence_ids:
  - owners
  - chemistry
  - gsrs
- assessment_id: schema
  area: schema
  topic: Focused validators
  outcome: supported
  summary: Native schema and strict validation pass; independent chemistry passes
    after equivalent formula notation is accounted for.
  target_ids:
  - CHEBI:2638
  evidence_ids:
  - gates
  - chemistry
findings: []
actions: []
limitations:
- Reaxys registry content could not be independently inspected; its identifier remains
  a current ChEBI assertion.
- PMID3174816 experimental text was unavailable; no solid-state result was inferred
  from metadata.
- The2023 mechanistic study has a catalog-number ordering discrepancy and current
  A2324 is nonstoichiometric sulfate. Historical preparation composition and quantitative
  transfer to exact disulfate remain unresolved.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All22 input hashes rechecked unchanged; no native edits.
- 'Curator follow-up: use inspected2023 ribosome work for explicit active-moiety mechanism
  context after reagent adjudication, retain h44 RNA complex scope, distinguish functional
  inhibition from observed secondary-site binding and ground any strain-level MIC
  with its method and tested preparation.'
- Raw ChEBI literature discovery should exclude PMID109983,6162275,6800084 by compound
  identity rather than promote a shared brand-name match. This is a source-quality
  note, not an unsupported native citation finding.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:2638
- https://gsrs.ncats.nih.gov/api/v1/substances/N6M33094FD?view=full
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10400623/
tags:
- antibacterial
- salt
- regulatory
- source-scope
```
