# Cefaloram: exact acid identity and sodium-salt antibacterial evidence

- Review: 20261021T110032Z-cefaloram
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T10:44:46Z
- Finished UTC: 2026-10-21T11:00:32Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

No confirmed native defect. The neutral cefaloram graph and cephalosporin classification agree with current ChEBI and independent PubChem structure. Original antibacterial experiments explicitly used the sodium salt, supporting the active moiety while requiring a material qualification for quantitative transfer. The native PBP/cell-wall/lysis description remains authority-sourced: the adopted immunochemistry paper does not demonstrate that chain, and a direct cefaloram-specific PBP experiment was not located in the bounded search. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Whole-record review of exact neutral cefaloram, also called cephaloram.

Selection: Queue 206 in isolated batch 021; initial capture preserved and actual source/guidance inputs recorded before detailed judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:192380 | data/antibiotics/antibacterial/cefaloram.yaml | generated | cefaloram |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | CHEBI:192380 | Actual focused command passed with zero errors. |
| Focused strict | passed | True | CHEBI:192380 | Actual focused command passed with zero errors. |
| Independent molecular encodings and source mint | passed | True | CHEBI:192380 | Both molecular encodings, formula, charge, masses, two R stereocentres and exact ChEBI mint agree. |
| PBP and peptidoglycan structured-source check before web | passed | True | CHEBI:192380 | Live dataset catalog and three searches returned gene annotations and zero iModulons. An initial sandbox DNS failure was resolved by permitted public-network execution; no component summaries were applicable. |
| Authoritative full QC | failed | True | CHEBI:192380 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:192380 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:192380 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:192380 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:192380 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:192380 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:192380 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:192380 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:192380 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral cefaloram

identity: supported. Targets: CHEBI:192380.

Native acid, stereo descriptors, formula, charge, mass and exact source mint agree with current ChEBI and independent PubChem. The primary paper names the matching phenylacetyl/acetoxy active moiety but experiments use sodium salt.

### Cephalosporin and antibacterial filing

grounding: supported. Targets: CHEBI:192380.

The broader cephalosporin parent is structurally appropriate. Source-supported antibiotic and antibacterial-drug roles are consistent with strong measured sodium-cefaloram activity; the salt boundary does not by itself invalidate the active-moiety classification.

### Source accession and adopted literature

grounding: supported. Targets: CHEBI:192380.

CHEBI:192380 resolves to the exact acid and its sole adopted PMID resolves correctly. The paper concerns the named compound but supports immunochemistry, not every mechanistic sentence of the authority definition. No native xrefs require exact-form adjudication.

### Authority PBP, cross-linking and lysis description

evidence: unknown. Targets: CHEBI:192380.

The definition is faithfully attributed to ChEBI. The inspected exact-compound literature does not experimentally establish the whole PBP-to-cross-linking-to-lysis chain. Its underlying class mechanism is plausible but remains authority context here; failure to locate a direct experiment is not proof the claim is false. Do not turn this paragraph into primary-evidenced causal edges.

### Sodium-salt material and historical MICs

evidence: supported. Targets: CHEBI:192380.

The original paper supports antibacterial action of the cefaloram active moiety through named sodium-salt assays. Quantitative adoption requires explicit salt/material scope, exact strains and per-row medium/inoculum; no unqualified neutral-acid MIC or current breakpoint should be fabricated.

### Serial-transfer phenotype

evidence: supported. Targets: CHEBI:192380.

Selected strains acquire higher MICs under the reported passage conditions; this is phenotypic resistance evidence without an identified molecular mechanism. Cephalosporin C enzyme assays cannot be reassigned to cefaloram.

### Immunochemical experiments

scope: supported. Targets: CHEBI:192380.

The adopted source establishes rabbit antibody cross-reactivity involving cephaloram-sensitized erythrocytes. It does not supply an antibacterial host target, microbial target affinity, clinical allergy frequency or therapeutic approval.

### Structured gene annotations

scope: supported. Targets: CHEBI:192380.

Required adapter searches preceded web follow-up; gene hits and zero component hits provide context only. Neither the presence nor absence of these hits adjudicates cefaloram binding.

### Producer, clinical and graph claims

scope: not_applicable. Targets: CHEBI:192380.

No native natural producer, current regulatory status, dataset or causal graph is populated. Historical salt experiments and host immunochemistry must retain their own scope if later curated.

### Maintained source and seeded status

provenance: supported. Targets: CHEBI:192380.

Single ChEBI source concept/mint and three seed events are coherent. Owners were captured and SEEDED status remains unchanged.

### Bounded optional enrichment

completeness: supported. Targets: CHEBI:192380.

Primary activity and serial-transfer observations provide actionable enrichment leads. Empty optional slots alone are not findings; exact material handling and mechanistic uncertainty must be preserved.

### Focused deterministic gates

schema: supported. Targets: CHEBI:192380.

Schema, strict and independent chemistry pass; this is distinct from the unresolved primary mechanism qualification.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optionally curate salt-qualified primary activity and serial-transfer observations.

- Use PMID 14126054 original Table 1/Methods to record that the tested material was sodium cefaloram. Do not present its MICs as an independently measured neutral-acid preparation; resolve representation under the native schema before adoption.
- Retain the exact strain, historical medium, inoculum, incubation, units and comparator relation for each selected observation. Distinguish single-agent, combination and serial-passage assays.
- Do not infer contemporary breakpoint categories, resistance genes, target mutations or prevalence from the serial-transfer experiment.
- Do not transfer cephalosporin C hydrolysis results or its combination behavior to cefaloram.
- Run native schema, strict, term/reference/history and applicable corpus checks after separately authorized curation.

### A2

Optionally resolve exact-compound support for the authority mechanism before adding curated target or causal claims.

- Locate and inspect a cefaloram-specific PBP or peptidoglycan experiment with explicit material and assay identity, or retain the description explicitly as authority/class context.
- Keep PMID 4108368 attached only to the immunochemical claim it actually tests; it does not validate PBP binding or cell lysis.
- Do not mark a mechanism false solely because the bounded search did not locate its primary experiment, and do not create primary-evidenced causal edges from the imported definition alone.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/cefaloram.yaml; Entire YAML | supports | Read exact identity, ChEBI-sourced definition, INN/systematic synonyms, cephalosporin parent, antibiotic and antibacterial-drug roles, full neutral structure, exact source concept and all three seed events. No exact/drug/document xrefs or populated mode, molecular_targets, activity_spectrum, resistance, producer, clinical or graph blocks. |
| owners | data/raw/chebi_antimicrobials.tsv; Exact CHEBI:192380 source row; extract/seeder and source configuration | supports | The ChEBI row owns native identity, structure, roles and the sole PMID 4108368 lead. Maintained extraction/seeding and decision owners were inspected. Hidden/ignored-inclusive search found native/raw/generated and historical references without an exact curator override. Original captures were preserved. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:192380; Current structure, definition, ontology and citation | supports | Current ChEBI matches neutral C18H18N2O6S, GOFCPYKUMJBHBH-RHSMWYFYSA-N, the phenylacetamido/acetoxymethyl cephalosporin identity and retained antibiotic/drug context. It repeats the PBP-to-cell-lysis description, with PMID 4108368 as the retained literature lead. The authority source is not itself a compound-specific PBP experiment. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/68940; Current PUG exact structure | supports | CID 68940, cephalosporin G/cefaloram, reproduces the complete native neutral-acid InChIKey and C18H18N2O6S formula. This is independent corroboration, not a newly adopted native xref. |
| chemistry | Independent RDKit 2026.03.5 check; 206-chemistry.json | supports | Both encodings parse as one neutral fragment, give the exact full key and formula, match source-precision masses and assign the two expected R centres. The exact ChEBI source mint matches. |
| adopted-reference | https://pubmed.ncbi.nlm.nih.gov/4108368/; Europe PMC core metadata/abstract | context_only | PMID 4108368 resolves to Hamilton-Miller and Abraham, Biochemical Journal 1971, DOI 10.1042/bj1230183, on haemagglutinating antibodies to penicillins/cephalosporins. Its experimental subject is immunochemical recognition, not bacterial PBP engagement. The full original eight pages were inspected separately. |
| immunochemistry | https://doi.org/10.1042/bj1230183; Original pp.183–190; Table 3 and Results p.187; Discussion pp.189–190 | context_only | Cephaloram is explicitly identified by its phenylacetyl side chain. Red cells sensitized with it cross-react with rabbit antisera to benzylpenicillin, unlike several different-side-chain comparators. This supports bounded immunochemical compound context. Antibody recognition, erythrocyte sensitization and proposed conjugate chemistry are not measurements of bacterial PBP binding, peptidoglycan cross-linking or bacteriolysis. |
| primary-material | https://doi.org/10.1111/j.1476-5381.1964.tb01540.x; PMID 14126054; original Table 1 and Methods p.23 | supports | Table 1 identifies cephaloram as 7-phenylacetamidocephalosporanic acid with the acetoxy substituent, matching the native active moiety. Methods explicitly state that all antibiotics except cephalosporin P1 were used as sodium salts. Thus the assay material is not the exact neutral-acid form. |
| primary-activity | https://doi.org/10.1111/j.1476-5381.1964.tb01540.x; Original pp.23–25; Table 2 | supports | Sodium-cephaloram MICs after 24 h at 37 °C include S. aureus H 0.125 µg/mL in Oxoid broth, S. pyogenes CN10 0.2 µg/mL in 10% serum broth, and E. coli type 2 31 µg/mL. Inoculum dilutions differ across rows. The assay used twofold dilutions in 0.5-mL broth with 0.02 mL culture inoculum. Retain salt identity and original methods; no present-day clinical breakpoint is established. |
| primary-resistance | https://doi.org/10.1111/j.1476-5381.1964.tb01540.x; Original Table 5 and discussion p.26; full pp.22–33 inspected | supports | Repeated in-vitro transfer selected increased cephaloram MICs in six S. aureus backgrounds. R1 changed from 0.5 to 64 µg/mL after 48 transfers. Persistence after antibiotic-free subculture differed between strain groups. This is a selected phenotype, not identification of a resistance gene, target mutation or general clinical resistance prevalence. |
| primary-boundary | https://doi.org/10.1111/j.1476-5381.1964.tb01540.x; Methods p.23; combination results pp.29–32 | context_only | The enzyme assay concerns cephalosporin C and benzylpenicillin, so it does not establish a cefaloram-specific hydrolysis mechanism. Combination effects vary by partner and strain; cephaloram/benzylpenicillin lacked synergy in the reported D3R in-vitro and G2 in-vivo comparisons. These results do not supply the native complete PBP-to-lysis mechanism. |
| adapter | iModulonDB structured source runner; 205206-adapter-results.json; dataset catalog and searches before open web | context_only | E. coli precise1k and S. aureus staph_precise108 searches returned PBP/peptidoglycan gene annotations, including e_coli/precise1k/b0084/ftsI and s_aureus/staph_precise108/USA300HOU_RS08285/pbp2B. All searches returned zero iModulons. Resistance-enzyme annotations such as blaZ are not cefaloram binding evidence. No assay or target identity is inferred solely from this context. |
| search | Ignored-inclusive repository and free primary search; 206-owner-hits.txt; 206-search.json; exact cefaloram/cephaloram strings | context_only | Repository search included hidden and ignored files outside .git/.venv. The adopted immunochemistry source and additional 1964 antibacterial source were inspected. PMID 16742517 concerns cephalothin metabolism and prior cephaloram disposition context; it is not direct PBP evidence. No exact cefaloram PBP competition or cross-linking experiment was located within this bounded follow-up. |
| gates | Actual focused commands; 206-focused-results.json; 206-validation.tsv | supports | Schema and strict each exit zero with no target errors; independent chemistry also passes. All 20 expanded input hashes were rechecked unchanged. |

## Limits And Additional Notes

- The direct antibacterial paper used sodium salts. It supports cefaloram active-moiety activity, but numeric transfer to the neutral-acid native entity requires explicit material qualification or another exact-form source.
- No cefaloram-specific PBP competition, peptidoglycan cross-linking or lysis experiment was located within the bounded search. The native description remains ChEBI-sourced, with no demonstrated contradiction.
- The sole adopted PMID and the additional 1964 antibacterial paper were read in full through original scanned pages; the 1967 cephalothin-metabolism follow-up lead was inspected only at metadata/abstract scope.
- Historical culture methods, selected resistance and combination results do not establish modern clinical breakpoints, population prevalence or a molecular resistance determinant.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Original 13 captured input hashes preserved; expanded source/guidance capture contains 20 unchanged files. No native/source/status/history edits.
- Schema/strict used batch 021; chemistry used existing locked batch 019 RDKit 2026.03.5 against batch 021 cwd.
- Primary source images and actual fetch timestamps/hashes are retained in 206-pages-fetch-results.json. The sodium-salt boundary is explicit, not inferred from a generic cephalosporin label.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T110032Z-cefaloram
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Cefaloram: exact acid identity and sodium-salt antibacterial evidence'
started_at: '2026-10-21T10:44:46Z'
finished_at: '2026-10-21T11:00:32Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Independent complete native and ChEBI owner review, structured
    PBP/peptidoglycan adapter before web, current exact identity comparison, adopted
    immunochemistry article and full original 1964 antibacterial paper.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: blocked
scientific_review: true
summary: 'No confirmed native defect. The neutral cefaloram graph and cephalosporin
  classification agree with current ChEBI and independent PubChem structure. Original
  antibacterial experiments explicitly used the sodium salt, supporting the active
  moiety while requiring a material qualification for quantitative transfer. The native
  PBP/cell-wall/lysis description remains authority-sourced: the adopted immunochemistry
  paper does not demonstrate that chain, and a direct cefaloram-specific PBP experiment
  was not located in the bounded search. Scientific assessment retains the stated
  evidence limits; full verification is blocked by the shared native-library failure.'
source:
  git_revision: baf3b3203d748d098686e166cdb2a6138f47eb59
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 5e2e1f975f8aa64f92a06c134c98c750c968fd78f02620a73c9cb611ac018ed8
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: CLAUDE.md
    sha256: 36fb92f8919481cfbf3f17ddde4a1e244c81f76c64396dbbac910c4815fb9f16
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
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
  - path: data/antibiotics/antibacterial/cefaloram.yaml
    sha256: 9d873bbb84a2038e42d48703d3f539d0fcc68be8c1fe1cd6896735ebe025516d
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
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 5e59c2be29bcd058aee058fb2763f63102ea77817b016802d5a3b3ae2938f4b6
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
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
- target_id: CHEBI:192380
  path: data/antibiotics/antibacterial/cefaloram.yaml
  label: cefaloram
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted exact ChEBI identity, structure, roles and citation leads
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding and exclusion overrides
scope:
  description: Whole-record review of exact neutral cefaloram, also called cephaloram.
  selection: Queue 206 in isolated batch 021; initial capture preserved and actual
    source/guidance inputs recorded before detailed judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:192380
  exclusions:
  - target: Sodium cefaloram, cephalosporin C derivatives, benzylpenicillin and other
      assay comparators
    reason: The parent acid, tested salt and distinct comparator compounds are kept
      separate. The antibacterial salt data are explicitly qualified as evidence for
      the active moiety.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual focused command passed with zero errors.
  target_ids:
  - CHEBI:192380
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cefaloram.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: strict
  name: Focused strict
  status: passed
  required: true
  summary: Actual focused command passed with zero errors.
  target_ids:
  - CHEBI:192380
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cefaloram.yaml --out /private/tmp/am-review-session/206-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Independent molecular encodings and source mint
  status: passed
  required: true
  summary: Both molecular encodings, formula, charge, masses, two R stereocentres
    and exact ChEBI mint agree.
  target_ids:
  - CHEBI:192380
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/check199200.py
    206 (cwd /private/tmp/antibioticmech-record-reviews-021)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - chemistry
- check_id: structured-source
  name: PBP and peptidoglycan structured-source check before web
  status: passed
  required: true
  summary: Live dataset catalog and three searches returned gene annotations and zero
    iModulons. An initial sandbox DNS failure was resolved by permitted public-network
    execution; no component summaries were applicable.
  target_ids:
  - CHEBI:192380
  command: 'env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets

    env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset precise1k --query penicillin

    env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism s_aureus --dataset staph_precise108
    --query penicillin

    env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset precise1k --query peptidoglycan'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - adapter
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:192380
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
  - CHEBI:192380
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
  - CHEBI:192380
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
  - CHEBI:192380
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
  - CHEBI:192380
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
  - CHEBI:192380
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
  - CHEBI:192380
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
  - CHEBI:192380
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
  - CHEBI:192380
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/cefaloram.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T10:59:22Z'
  support: supports
  summary: Read exact identity, ChEBI-sourced definition, INN/systematic synonyms,
    cephalosporin parent, antibiotic and antibacterial-drug roles, full neutral structure,
    exact source concept and all three seed events. No exact/drug/document xrefs or
    populated mode, molecular_targets, activity_spectrum, resistance, producer, clinical
    or graph blocks.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Exact CHEBI:192380 source row; extract/seeder and source configuration
  accessed_at: '2026-10-21T10:59:22Z'
  support: supports
  summary: The ChEBI row owns native identity, structure, roles and the sole PMID
    4108368 lead. Maintained extraction/seeding and decision owners were inspected.
    Hidden/ignored-inclusive search found native/raw/generated and historical references
    without an exact curator override. Original captures were preserved.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:192380
  locator: Current structure, definition, ontology and citation
  accessed_at: '2026-10-21T10:51:27Z'
  support: supports
  summary: Current ChEBI matches neutral C18H18N2O6S, GOFCPYKUMJBHBH-RHSMWYFYSA-N,
    the phenylacetamido/acetoxymethyl cephalosporin identity and retained antibiotic/drug
    context. It repeats the PBP-to-cell-lysis description, with PMID 4108368 as the
    retained literature lead. The authority source is not itself a compound-specific
    PBP experiment.
  snapshot_sha256: d7b5b314a24e8df0dce10b9cbc8191ef4231e0fd234f6e5366c224a3ea918ade
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/68940
  locator: Current PUG exact structure
  accessed_at: '2026-10-21T10:51:29Z'
  support: supports
  summary: CID 68940, cephalosporin G/cefaloram, reproduces the complete native neutral-acid
    InChIKey and C18H18N2O6S formula. This is independent corroboration, not a newly
    adopted native xref.
  snapshot_sha256: ae807fd3f95dc36c5fa9349981fd2a3693c3a69afba04b06f36978a8a776d335
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit 2026.03.5 check
  locator: 206-chemistry.json
  accessed_at: '2026-10-21T10:50:51Z'
  support: supports
  summary: Both encodings parse as one neutral fragment, give the exact full key and
    formula, match source-precision masses and assign the two expected R centres.
    The exact ChEBI source mint matches.
  snapshot_sha256: c7d045f7093ebaccd37ef111adeda67851a68ab7d29b27e3648e1ad2d84e861c
- evidence_id: adopted-reference
  kind: database
  reference: https://pubmed.ncbi.nlm.nih.gov/4108368/
  locator: Europe PMC core metadata/abstract
  accessed_at: '2026-10-21T10:51:26Z'
  support: context_only
  summary: PMID 4108368 resolves to Hamilton-Miller and Abraham, Biochemical Journal
    1971, DOI 10.1042/bj1230183, on haemagglutinating antibodies to penicillins/cephalosporins.
    Its experimental subject is immunochemical recognition, not bacterial PBP engagement.
    The full original eight pages were inspected separately.
  snapshot_sha256: 9dc1fdbaf2088c319a2cc9a1c26c5a6d361000fd875e1513ae5ebe6b74883bdf
- evidence_id: immunochemistry
  kind: primary_source
  reference: https://doi.org/10.1042/bj1230183
  locator: Original pp.183–190; Table 3 and Results p.187; Discussion pp.189–190
  accessed_at: '2026-10-21T10:52:37Z'
  support: context_only
  summary: Cephaloram is explicitly identified by its phenylacetyl side chain. Red
    cells sensitized with it cross-react with rabbit antisera to benzylpenicillin,
    unlike several different-side-chain comparators. This supports bounded immunochemical
    compound context. Antibody recognition, erythrocyte sensitization and proposed
    conjugate chemistry are not measurements of bacterial PBP binding, peptidoglycan
    cross-linking or bacteriolysis.
  snapshot_sha256: f29457759a540f3b25bd41098a97079f21cf4012b6da7886607f9e502f9eec63
- evidence_id: primary-material
  kind: primary_source
  reference: https://doi.org/10.1111/j.1476-5381.1964.tb01540.x
  locator: PMID 14126054; original Table 1 and Methods p.23
  accessed_at: '2026-10-21T10:52:36Z'
  support: supports
  summary: Table 1 identifies cephaloram as 7-phenylacetamidocephalosporanic acid
    with the acetoxy substituent, matching the native active moiety. Methods explicitly
    state that all antibiotics except cephalosporin P1 were used as sodium salts.
    Thus the assay material is not the exact neutral-acid form.
  snapshot_sha256: 09bb837278bb8e92dcc771669f3968dbf089073df84f880908005c8c465b4f27
- evidence_id: primary-activity
  kind: primary_source
  reference: https://doi.org/10.1111/j.1476-5381.1964.tb01540.x
  locator: Original pp.23–25; Table 2
  accessed_at: '2026-10-21T10:52:36Z'
  support: supports
  summary: Sodium-cephaloram MICs after 24 h at 37 °C include S. aureus H 0.125 µg/mL
    in Oxoid broth, S. pyogenes CN10 0.2 µg/mL in 10% serum broth, and E. coli type
    2 31 µg/mL. Inoculum dilutions differ across rows. The assay used twofold dilutions
    in 0.5-mL broth with 0.02 mL culture inoculum. Retain salt identity and original
    methods; no present-day clinical breakpoint is established.
  snapshot_sha256: 3ad80dfb0e8b46881f21769f987be5e9dbfdac1c922ebcfb31a44849504c3eef
- evidence_id: primary-resistance
  kind: primary_source
  reference: https://doi.org/10.1111/j.1476-5381.1964.tb01540.x
  locator: Original Table 5 and discussion p.26; full pp.22–33 inspected
  accessed_at: '2026-10-21T10:52:36Z'
  support: supports
  summary: Repeated in-vitro transfer selected increased cephaloram MICs in six S.
    aureus backgrounds. R1 changed from 0.5 to 64 µg/mL after 48 transfers. Persistence
    after antibiotic-free subculture differed between strain groups. This is a selected
    phenotype, not identification of a resistance gene, target mutation or general
    clinical resistance prevalence.
  snapshot_sha256: 6eafb5e5e540429b7f46590b9979ce82596867f812c9f72f93a592df43bc26d5
- evidence_id: primary-boundary
  kind: primary_source
  reference: https://doi.org/10.1111/j.1476-5381.1964.tb01540.x
  locator: Methods p.23; combination results pp.29–32
  accessed_at: '2026-10-21T10:52:36Z'
  support: context_only
  summary: The enzyme assay concerns cephalosporin C and benzylpenicillin, so it does
    not establish a cefaloram-specific hydrolysis mechanism. Combination effects vary
    by partner and strain; cephaloram/benzylpenicillin lacked synergy in the reported
    D3R in-vitro and G2 in-vivo comparisons. These results do not supply the native
    complete PBP-to-lysis mechanism.
  snapshot_sha256: e46a6463704e005f6ad17024bd5b3de0afa923b269982111da73e72c1a95b911
- evidence_id: adapter
  kind: database
  reference: iModulonDB structured source runner
  locator: 205206-adapter-results.json; dataset catalog and searches before open web
  accessed_at: '2026-10-21T10:51:07Z'
  support: context_only
  summary: E. coli precise1k and S. aureus staph_precise108 searches returned PBP/peptidoglycan
    gene annotations, including e_coli/precise1k/b0084/ftsI and s_aureus/staph_precise108/USA300HOU_RS08285/pbp2B.
    All searches returned zero iModulons. Resistance-enzyme annotations such as blaZ
    are not cefaloram binding evidence. No assay or target identity is inferred solely
    from this context.
  snapshot_sha256: 22dc6dcb5b4853d51fafa06115acf9fd86afa0a07fc55d37e096b6255e263985
- evidence_id: search
  kind: search
  reference: Ignored-inclusive repository and free primary search
  locator: 206-owner-hits.txt; 206-search.json; exact cefaloram/cephaloram strings
  accessed_at: '2026-10-21T10:51:26Z'
  support: context_only
  summary: Repository search included hidden and ignored files outside .git/.venv.
    The adopted immunochemistry source and additional 1964 antibacterial source were
    inspected. PMID 16742517 concerns cephalothin metabolism and prior cephaloram
    disposition context; it is not direct PBP evidence. No exact cefaloram PBP competition
    or cross-linking experiment was located within this bounded follow-up.
  snapshot_sha256: a228d541e1388477250e563aa657166a814914ee57fe81753c7df80c11205993
  search_scope: rg --no-ignore --hidden exact identifier/label/slug/key across isolated
    batch 021 outside .git/.venv; structured PBP/peptidoglycan lookup followed by
    free current ChEBI/PubChem, EPMC exact-name search and complete original PMC scanned
    articles, accessed 2026-10-21.
- evidence_id: gates
  kind: validation
  reference: Actual focused commands
  locator: 206-focused-results.json; 206-validation.tsv
  accessed_at: '2026-10-21T10:50:51Z'
  support: supports
  summary: Schema and strict each exit zero with no target errors; independent chemistry
    also passes. All 20 expanded input hashes were rechecked unchanged.
  snapshot_sha256: 77c75289c0d621ce9484183ba60193d4b0a07b908704e45110cef917bf8aa8b3
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral cefaloram
  outcome: supported
  summary: Native acid, stereo descriptors, formula, charge, mass and exact source
    mint agree with current ChEBI and independent PubChem. The primary paper names
    the matching phenylacetyl/acetoxy active moiety but experiments use sodium salt.
  target_ids:
  - CHEBI:192380
  evidence_ids:
  - native
  - chebi
  - pubchem
  - chemistry
  - primary-material
- assessment_id: grounding
  area: grounding
  topic: Cephalosporin and antibacterial filing
  outcome: supported
  summary: The broader cephalosporin parent is structurally appropriate. Source-supported
    antibiotic and antibacterial-drug roles are consistent with strong measured sodium-cefaloram
    activity; the salt boundary does not by itself invalidate the active-moiety classification.
  target_ids:
  - CHEBI:192380
  evidence_ids:
  - chebi
  - primary-material
  - primary-activity
- assessment_id: references
  area: grounding
  topic: Source accession and adopted literature
  outcome: supported
  summary: CHEBI:192380 resolves to the exact acid and its sole adopted PMID resolves
    correctly. The paper concerns the named compound but supports immunochemistry,
    not every mechanistic sentence of the authority definition. No native xrefs require
    exact-form adjudication.
  target_ids:
  - CHEBI:192380
  evidence_ids:
  - chebi
  - adopted-reference
  - immunochemistry
  - native
- assessment_id: definition-mechanism
  area: evidence
  topic: Authority PBP, cross-linking and lysis description
  outcome: unknown
  summary: The definition is faithfully attributed to ChEBI. The inspected exact-compound
    literature does not experimentally establish the whole PBP-to-cross-linking-to-lysis
    chain. Its underlying class mechanism is plausible but remains authority context
    here; failure to locate a direct experiment is not proof the claim is false. Do
    not turn this paragraph into primary-evidenced causal edges.
  target_ids:
  - CHEBI:192380
  evidence_ids:
  - chebi
  - immunochemistry
  - primary-boundary
  - search
  - adapter
- assessment_id: activity
  area: evidence
  topic: Sodium-salt material and historical MICs
  outcome: supported
  summary: The original paper supports antibacterial action of the cefaloram active
    moiety through named sodium-salt assays. Quantitative adoption requires explicit
    salt/material scope, exact strains and per-row medium/inoculum; no unqualified
    neutral-acid MIC or current breakpoint should be fabricated.
  target_ids:
  - CHEBI:192380
  evidence_ids:
  - primary-material
  - primary-activity
- assessment_id: resistance
  area: evidence
  topic: Serial-transfer phenotype
  outcome: supported
  summary: Selected strains acquire higher MICs under the reported passage conditions;
    this is phenotypic resistance evidence without an identified molecular mechanism.
    Cephalosporin C enzyme assays cannot be reassigned to cefaloram.
  target_ids:
  - CHEBI:192380
  evidence_ids:
  - primary-resistance
  - primary-boundary
- assessment_id: host-scope
  area: scope
  topic: Immunochemical experiments
  outcome: supported
  summary: The adopted source establishes rabbit antibody cross-reactivity involving
    cephaloram-sensitized erythrocytes. It does not supply an antibacterial host target,
    microbial target affinity, clinical allergy frequency or therapeutic approval.
  target_ids:
  - CHEBI:192380
  evidence_ids:
  - immunochemistry
  - adopted-reference
- assessment_id: adapter-scope
  area: scope
  topic: Structured gene annotations
  outcome: supported
  summary: Required adapter searches preceded web follow-up; gene hits and zero component
    hits provide context only. Neither the presence nor absence of these hits adjudicates
    cefaloram binding.
  target_ids:
  - CHEBI:192380
  evidence_ids:
  - adapter
- assessment_id: optional-domains
  area: scope
  topic: Producer, clinical and graph claims
  outcome: not_applicable
  summary: No native natural producer, current regulatory status, dataset or causal
    graph is populated. Historical salt experiments and host immunochemistry must
    retain their own scope if later curated.
  target_ids:
  - CHEBI:192380
  evidence_ids:
  - native
  - primary-material
  - immunochemistry
- assessment_id: history
  area: provenance
  topic: Maintained source and seeded status
  outcome: supported
  summary: Single ChEBI source concept/mint and three seed events are coherent. Owners
    were captured and SEEDED status remains unchanged.
  target_ids:
  - CHEBI:192380
  evidence_ids:
  - owners
  - native
  - chemistry
- assessment_id: completeness
  area: completeness
  topic: Bounded optional enrichment
  outcome: supported
  summary: Primary activity and serial-transfer observations provide actionable enrichment
    leads. Empty optional slots alone are not findings; exact material handling and
    mechanistic uncertainty must be preserved.
  target_ids:
  - CHEBI:192380
  evidence_ids:
  - primary-activity
  - primary-resistance
  - primary-material
  - search
- assessment_id: schema
  area: schema
  topic: Focused deterministic gates
  outcome: supported
  summary: Schema, strict and independent chemistry pass; this is distinct from the
    unresolved primary mechanism qualification.
  target_ids:
  - CHEBI:192380
  evidence_ids:
  - gates
  - chemistry
findings: []
actions:
- action_id: A1
  description: Optionally curate salt-qualified primary activity and serial-transfer
    observations.
  finding_ids: []
  target_ids:
  - CHEBI:192380
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefaloram.yaml
    role: Curator-owned activity_spectrum and resistance observations through validated
      writer
  acceptance_checks:
  - Use PMID 14126054 original Table 1/Methods to record that the tested material
    was sodium cefaloram. Do not present its MICs as an independently measured neutral-acid
    preparation; resolve representation under the native schema before adoption.
  - Retain the exact strain, historical medium, inoculum, incubation, units and comparator
    relation for each selected observation. Distinguish single-agent, combination
    and serial-passage assays.
  - Do not infer contemporary breakpoint categories, resistance genes, target mutations
    or prevalence from the serial-transfer experiment.
  - Do not transfer cephalosporin C hydrolysis results or its combination behavior
    to cefaloram.
  - Run native schema, strict, term/reference/history and applicable corpus checks
    after separately authorized curation.
- action_id: A2
  description: Optionally resolve exact-compound support for the authority mechanism
    before adding curated target or causal claims.
  finding_ids: []
  target_ids:
  - CHEBI:192380
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Source-owned definition if a source correction is warranted
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/cefaloram.yaml
    role: Curator-owned evidence/target/graph annotations
  acceptance_checks:
  - Locate and inspect a cefaloram-specific PBP or peptidoglycan experiment with explicit
    material and assay identity, or retain the description explicitly as authority/class
    context.
  - Keep PMID 4108368 attached only to the immunochemical claim it actually tests;
    it does not validate PBP binding or cell lysis.
  - Do not mark a mechanism false solely because the bounded search did not locate
    its primary experiment, and do not create primary-evidenced causal edges from
    the imported definition alone.
limitations:
- The direct antibacterial paper used sodium salts. It supports cefaloram active-moiety
  activity, but numeric transfer to the neutral-acid native entity requires explicit
  material qualification or another exact-form source.
- No cefaloram-specific PBP competition, peptidoglycan cross-linking or lysis experiment
  was located within the bounded search. The native description remains ChEBI-sourced,
  with no demonstrated contradiction.
- The sole adopted PMID and the additional 1964 antibacterial paper were read in full
  through original scanned pages; the 1967 cephalothin-metabolism follow-up lead was
  inspected only at metadata/abstract scope.
- Historical culture methods, selected resistance and combination results do not establish
  modern clinical breakpoints, population prevalence or a molecular resistance determinant.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Original 13 captured input hashes preserved; expanded source/guidance capture contains
  20 unchanged files. No native/source/status/history edits.
- Schema/strict used batch 021; chemistry used existing locked batch 019 RDKit 2026.03.5
  against batch 021 cwd.
- Primary source images and actual fetch timestamps/hashes are retained in 206-pages-fetch-results.json.
  The sodium-salt boundary is explicit, not inferred from a generic cephalosporin
  label.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:192380
- https://doi.org/10.1111/j.1476-5381.1964.tb01540.x
- https://doi.org/10.1042/bj1230183
tags:
- cefaloram
- salt-material-scope
- primary-evidence
- authority-mechanism
```
