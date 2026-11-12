# (3Z)-ravenic acid: exact identity and cultured-isolate evidence

- Review: 20261021T074241Z-3z-ravenic-acid
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T07:36:40Z
- Finished UTC: 2026-10-21T07:42:41Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact structure, source classification, ownership and focused validation are supported. One minor source-specific follow-up concerns cultured Penicillium isolate MINAP-9902. Ravenic/ravynic identity and quantitative assay boundaries are explicit; no molecular mechanism or pure-isomer MIC is inferred.

## Scope And Provenance

Complete one-record identity, source-support and bounded scientific review.

Selection: Queue index041; exactly CHEBI:66291 in isolated batch005.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:66291 | data/antibiotics/antibacterial/3z-ravenic-acid.yaml | generated | (3Z)-ravenic acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema validation | passed | True | CHEBI:66291 | Actual focused execution passed with zero errors. |
| Focused strict validation | passed | True | CHEBI:66291 | Actual focused execution passed with zero errors. |
| Exact geometric structure and source identity | passed | True | CHEBI:66291 | Native structure, current authority and independent calculation agree. |
| Direct registry substance detail | unavailable | False | CHEBI:66291 | Reaxys detail unavailable; current ChEBI xref assertion inspected. |
| Structured expression-source applicability | not_applicable | False | CHEBI:66291 | The native record names no gene, protein, regulator, pathway, stress response, trait dataset or transcriptomic dataset. Genus-level producer isolation and compound-identity verification do not supply an expression-module query. |
| Authoritative full QC | failed | True | CHEBI:66291 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:66291 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:66291 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:66291 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:66291 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:66291 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:66291 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:66291 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:66291 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact (3Z) geometric form

identity: supported. Targets: CHEBI:66291.

The current ChEBI structure, native names and full chemistry agree. Original abstract identifies the major geometric isomer. Experimental preparations must not automatically be treated as analytically pure3Z material.

### Broader parents, activity roles and registry

grounding: supported. Targets: CHEBI:66291.

Three broader classes and source antibacterial/antimicrobial roles are appropriate. Reaxys is source-asserted with direct detail unavailable; no contradictory xref evidence was found.

### Adopted publication scope

evidence: supported. Targets: CHEBI:66291.

Both adopted PMIDs resolve to the stated primary papers. The native seed does not promote their citations into unsupported target or potency claims.

### Specific cultured-isolate evidence

completeness: concern. Targets: CHEBI:66291.

Primary full text supplies Penicillium sp.MINAP-9902 culture/extraction and a ravenic-acid HPLC assignment, complementing original isolation. A genus-ranked producer annotation or explicit disposition is a concrete minor follow-up. Species, BGC and host-as-producer inferences remain unsupported.

### Exact-compound quantitative antibacterial activity

evidence: unknown. Targets: CHEBI:66291.

The2016 text distinguishes ravenic25microgram/mL historical comparison from ravynic2.5microgram/mL. The original ravenic assay protocol, exact bacterial isolate and isomeric preparation remain uninspected, so no new quantitative activity observation is justified yet.

### Mode, direct target and causal chain

evidence: unknown. Targets: CHEBI:66291.

No native mechanism or target is asserted, and inspected source text supplies no compound-specific molecular target or lethal causal chain. Polyene or tetramic-acid family membership does not fill that gap.

### Resistance, clinical status and datasets

scope: not_applicable. Targets: CHEBI:66291.

No native assertions require correction in these fields. The inspected isolation/synthesis studies do not establish a resistance determinant, current clinical product status or transcriptomics dataset.

### Generated ownership and scientific status

provenance: supported. Targets: CHEBI:66291.

The raw owner, source concept and three seed/reseed events agree. Any new producer annotation is curator-owned and requires claim-level evidence and validated history; native SEEDED status remains unchanged.

### Focused gates

schema: supported. Targets: CHEBI:66291.

Both focused native validators pass.

## Findings

### F1: Curated disposition of the specific MINAP-9902 producer evidence

minor / open / confirmed; issue key: chebi-66291-minap-9902-producer-disposition.

Inspected primary text names the cultured Penicillium isolate MINAP-9902 and assigns a ravenic-acid peak in its extract, while the original abstract supports isolation from Penicillium mycelia. The seed definition already records genus-level origin; a structured, narrowly evidenced producer claim or explicit applicability disposition would preserve the newly verified isolate context. This is a source-specific annotation opportunity, not a requirement to populate every optional field.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate and, if appropriate, curate the exact ravenic-acid producer link to Penicillium at genus rank with isolate MINAP-9902, retaining source identification limits.

- Attach PMID:12350167 and the specific isolation/culture/HPLC sections of PMID:27519121 to the producer claim or explicit disposition.
- Use NCBITaxon:5073 with taxon_label Penicillium and isolate designation MINAP-9902 separately; do not infer species, genome or BGC.
- State that the2016 HPLC assignment complements the original isolation abstract; do not claim independent isomer-purity characterization or confuse the myxomycete collection substrate with the fungal producer.
- Keep ravynic acid compound3 and its2.5microgram/mL result separate; retrieve original2002/2010 assay details and exact preparation mapping before adding a quantitative activity_spectrum observation.
- Use the native validated writer and curation history for any future annotation and retain SEEDED unless all sign-off criteria pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/3z-ravenic-acid.yaml; Entire native YAML | supports | The exact ChEBI-only structure is ANTIBACTERIAL, SEEDED and EXACT. Definition, two synonyms, three parents, two roles, full structure, Reaxys xref, source concept and all three seed/reseed events were read. No mechanism, target, quantitative activity, structured producer, resistance, clinical, dataset or causal graph claims are asserted. |
| owner | data/raw/chebi_antimicrobials.tsv; CHEBI:66291 row1495; data/antibiotics/PATHS.tsv row1748; MANIFEST, configuration, extractor and seeder | supports | Raw identity, structure, roles, xref, minted identifier antibioticmech:chebi-78504814d2 and source version 2026-08-30 reproduce the target. Adopted publication leads are PMID:12350167 and PMID:20066698. Role extraction is limited to the antimicrobial role hierarchy; omitting the separate Penicillium-metabolite role from activity_roles is not a defect. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:66291; Official visible identity, structure, parents, roles, names, Reaxys and species-of-metabolite fields | supports | The complete native structure and key JJFGJQNWIJPCAN-AJOOJNDDSA-N, formula C15H17NO3, charge0 and both masses match. The authority lists the same names and Reaxys9275104. The direct antibacterial role and inherited antimicrobial role are supported. Species-of-metabolite identifies Penicillium NCBITaxon:5073 with PMID:12350167; this is database provenance, distinct from a curated primary producer assertion. |
| parent-26177 | https://www.ebi.ac.uk/chebi/CHEBI:26177; Official parent definition | supports | The term resolves to polyene antibiotic, a class broader than this individual structure. The class does not justify transferring a family-wide mode of action. |
| parent-33823 | https://www.ebi.ac.uk/chebi/CHEBI:33823; Official parent definition | supports | The term resolves to enol, a class broader than this individual structure. The class does not justify transferring a family-wide mode of action. |
| parent-74223 | https://www.ebi.ac.uk/chebi/CHEBI:74223; Official parent definition | supports | The term resolves to pyrrolidin-2-ones, a class broader than this individual structure. The class does not justify transferring a family-wide mode of action. |
| chemistry | RDKit independent structure calculation; Native SMILES and Standard InChI parsed separately | supports | Both encodings reproduce the native complete InChIKey. Calculation gives C15H17NO3, charge0, one connected component, average mass259.305 and exact mass259.120843404; the stated geometric structure is internally consistent. |
| registry | https://www.reaxys.com/reaxys/secured/search.do?searchType=quick&amp;rid=9275104; Direct registry attempt | partial | The public Reaxys detail route was inaccessible. Reaxys9275104 is verified as the current ChEBI assertion, not independently checked against registry substance detail. |
| isolation | PMID:12350167; DOI10.1021/np0200358; Europe PMC core abstract; ACS supporting information DOI10.1021/np0200358.s001 | supports | The primary abstract explicitly reports isolation from cultured Penicillium mycelia and assigns the major ravenic-acid isomer (3Z,7E,9E,11E,13E). The main text was unavailable through attempted free routes. It does not give a strain designation, bacterial assay protocol, numerical potency or target in the inspected abstract. |
| isolation-supplement | https://ndownloader.figshare.com/files/5826045; Official ACS supplement np0200358_si_001.pdf; visually inspected page1 Figure4 | supports | The proton-NMR page includes the ravenic-acid structural drawing with the tetramic-acid ring and tetraene side chain, consistent with the native structure. This spectral supplement is not antibacterial assay evidence; no independent spectral re-elucidation is claimed. |
| synthesis | PMID:20066698; DOI10.1002/chem.200902544; Europe PMC core abstract and publisher abstract/reference page | context_only | The primary abstract describes synthesis of ravenic acid among 3-oligoenoyl tetramic acids and structure-dependent antimicrobial/cytotoxic activity across the series. Full Methods and compound-specific results were unavailable; the class-level abstract cannot establish an exact ravenic-acid MIC or a direct molecular target. |
| producer-primary | PMID:27519121; DOI10.1039/c6ob00938g; full primary PDF pp8259-8260, Isolation of fungus, Culturing of MINAP-9902 and HPLC; https://researchoutput.csu.edu.au/ws/portalfiles/portal/408867925/317637819.pdf | supports | The paper describes isolation and culture of Penicillium sp. MINAP-9902 from a surface-sterilized Lycogala epidendrum fruiting body. Cultured mycelia were extracted; the six-day potato-dextrose-broth sample had a strong HPLC peak assigned to ravenic acid at14.4min. Combined with the original isolation abstract, this supports a bounded producer follow-up for that isolate at genus rank. The myxomycete is collection context, not the experimentally cultured fungal producer. No species-level identification, sequence accession or BGC is established. |
| analogue-boundary | PMID:27519121; DOI10.1039/c6ob00938g; pp8253-8255 Figure1 and Results; p8260 sensitivity methods; Figure1 visually inspected | context_only | Ravenic acid is compound1; the newly characterized ravynic acid is compound3 with a distinct polyeneyne chain and C15H15NO3 composition. The reported2.5microgram/mL inhibition belongs to ravynic acid. The25microgram/mL ravenic-acid comparison explicitly cites the2002 paper and is not a newly established exact-isomer MIC in this review. Disk screening and OD600 sensitivity methods concern the study system; they cannot substitute for unread original assay conditions or establish a biochemical mechanism. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=5073&amp;mode=Info; Official taxon information, name and rank | supports | NCBITaxon:5073 resolves to Penicillium at genus rank. MINAP-9902 is the paper isolate designation, not a species name or independently verified genome accession. |
| search | CultureBotAI/AntibioticMech; Ignored-inclusive local searches and bounded free primary-source discovery | context_only | The target raw row and PATHS agree. Focused searches found readiness/historical discovery leads but no target-specific curator override. Primary discovery found the two adopted papers and the2016 analogue study. Other broad-search hits were not treated as target-specific mechanism or producer evidence. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Producer, exact-form equivalence, assay and mechanism rules | supports | Optional blanks are not defects. The concrete primary isolate/compound observation warrants a limited producer disposition. A genus-level taxon must not become a species claim; analogue or class activity cannot supply a mechanism or exact-isomer assay. |
| validation | just validate; just validate-strict; Actual batch005 focused executions; scratch041-validation.tsv | supports | Both commands exited0. LinkML reported no issues; strict scanned one target with zero ERROR rows. |

## Limits And Additional Notes

- The2002 and2010 primary main texts remained unavailable through attempted free routes. Their abstracts and the2002 spectral supplement were inspected; original assay protocol, exact clinical isolate and tested isomer composition remain unresolved.
- The2016 full text supplies specific culture/HPLC producer context, but its25microgram/mL ravenic result is a retrospective citation. Its2.5microgram/mL result belongs to distinct ravynic acid.
- Reaxys detail was inaccessible; the cross-reference remains verified only as an official ChEBI assertion.
- Bounded literature searches do not prove absence of additional exact-compound studies or establish a molecular mechanism.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Initial capture preceded judgment; all original hashes and Git base are retained in the expanded20-input provenance.
- Ignored and hidden files were included in the stated local search scopes.
- The older ad hoc report was not converted, and its broad missing-optional-field finding was not adopted. No native scientific status or record content was changed.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T074241Z-3z-ravenic-acid
kind: record
repository: CultureBotAI/AntibioticMech
title: '(3Z)-ravenic acid: exact identity and cultured-isolate evidence'
started_at: '2026-10-21T07:36:40Z'
finished_at: '2026-10-21T07:42:41Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Reviewer did not create the seed; whole native record, official
    identity and primary sources were independently inspected. Historical report was
    used only as discovery context.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Exact structure, source classification, ownership and focused validation
  are supported. One minor source-specific follow-up concerns cultured Penicillium
  isolate MINAP-9902. Ravenic/ravynic identity and quantitative assay boundaries are
  explicit; no molecular mechanism or pure-isomer MIC is inferred.
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
  - path: data/antibiotics/antibacterial/3z-ravenic-acid.yaml
    sha256: 29bf181c0eea82551f66db662f74d2d8f259f2d261125f61f2b860bcd166e012
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
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: docs/record-review-profile.md
    sha256: 370ace6db64e85be6c645f9fe45c2a2135a82f309af59f5352cd30f1245ef6df
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
targets:
- target_id: CHEBI:66291
  path: data/antibiotics/antibacterial/3z-ravenic-acid.yaml
  label: (3Z)-ravenic acid
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
  description: Complete one-record identity, source-support and bounded scientific
    review.
  selection: Queue index041; exactly CHEBI:66291 in isolated batch005.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:66291
  exclusions:
  - target: Ravynic acid, other tetramic-acid analogues and alternate isomers
    reason: Boundary context only; their activities and mechanisms are not transferred.
checks:
- check_id: schema
  name: Focused schema validation
  status: passed
  required: true
  summary: Actual focused execution passed with zero errors.
  target_ids:
  - CHEBI:66291
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/3z-ravenic-acid.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Focused strict validation
  status: passed
  required: true
  summary: Actual focused execution passed with zero errors.
  target_ids:
  - CHEBI:66291
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/3z-ravenic-acid.yaml --out /private/tmp/am-review-session/041-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: identity
  name: Exact geometric structure and source identity
  status: passed
  required: true
  summary: Native structure, current authority and independent calculation agree.
  target_ids:
  - CHEBI:66291
  evidence_ids:
  - chebi
  - chemistry
  - isolation
  - isolation-supplement
- check_id: registry
  name: Direct registry substance detail
  status: unavailable
  required: false
  summary: Reaxys detail unavailable; current ChEBI xref assertion inspected.
  target_ids:
  - CHEBI:66291
  evidence_ids:
  - registry
- check_id: structured-adapter
  name: Structured expression-source applicability
  status: not_applicable
  required: false
  summary: The native record names no gene, protein, regulator, pathway, stress response,
    trait dataset or transcriptomic dataset. Genus-level producer isolation and compound-identity
    verification do not supply an expression-module query.
  target_ids:
  - CHEBI:66291
  evidence_ids:
  - record
  - producer-primary
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:66291
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
  - CHEBI:66291
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
  - CHEBI:66291
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
  - CHEBI:66291
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
  - CHEBI:66291
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
  - CHEBI:66291
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
  - CHEBI:66291
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
  - CHEBI:66291
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
  - CHEBI:66291
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/3z-ravenic-acid.yaml
  locator: Entire native YAML
  accessed_at: '2026-10-21T07:41:40Z'
  support: supports
  summary: The exact ChEBI-only structure is ANTIBACTERIAL, SEEDED and EXACT. Definition,
    two synonyms, three parents, two roles, full structure, Reaxys xref, source concept
    and all three seed/reseed events were read. No mechanism, target, quantitative
    activity, structured producer, resistance, clinical, dataset or causal graph claims
    are asserted.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: CHEBI:66291 row1495; data/antibiotics/PATHS.tsv row1748; MANIFEST, configuration,
    extractor and seeder
  accessed_at: '2026-10-21T07:41:40Z'
  support: supports
  summary: Raw identity, structure, roles, xref, minted identifier antibioticmech:chebi-78504814d2
    and source version 2026-08-30 reproduce the target. Adopted publication leads
    are PMID:12350167 and PMID:20066698. Role extraction is limited to the antimicrobial
    role hierarchy; omitting the separate Penicillium-metabolite role from activity_roles
    is not a defect.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:66291
  locator: Official visible identity, structure, parents, roles, names, Reaxys and
    species-of-metabolite fields
  accessed_at: '2026-10-21T07:38:56Z'
  support: supports
  summary: The complete native structure and key JJFGJQNWIJPCAN-AJOOJNDDSA-N, formula
    C15H17NO3, charge0 and both masses match. The authority lists the same names and
    Reaxys9275104. The direct antibacterial role and inherited antimicrobial role
    are supported. Species-of-metabolite identifies Penicillium NCBITaxon:5073 with
    PMID:12350167; this is database provenance, distinct from a curated primary producer
    assertion.
  snapshot_sha256: da5d2393ecaf72aa334aa0749a184671eb7cb4a438e93de495071b7c152b379e
- evidence_id: parent-26177
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:26177
  locator: Official parent definition
  accessed_at: '2026-10-21T07:39:24Z'
  support: supports
  summary: The term resolves to polyene antibiotic, a class broader than this individual
    structure. The class does not justify transferring a family-wide mode of action.
  snapshot_sha256: 9211fb7977806382f55310fd0e25987b52f036d45e2204d2c6a9e2eb8c1da4a2
- evidence_id: parent-33823
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:33823
  locator: Official parent definition
  accessed_at: '2026-10-21T07:39:28Z'
  support: supports
  summary: The term resolves to enol, a class broader than this individual structure.
    The class does not justify transferring a family-wide mode of action.
  snapshot_sha256: 23dc6975390ceb07b17efd5d51aa735757451df43998ae58fbff60bcc7f3b7c6
- evidence_id: parent-74223
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:74223
  locator: Official parent definition
  accessed_at: '2026-10-21T07:39:29Z'
  support: supports
  summary: The term resolves to pyrrolidin-2-ones, a class broader than this individual
    structure. The class does not justify transferring a family-wide mode of action.
  snapshot_sha256: 90bc2def30209227995d9f256442289ddf82779e65be8b30fa1124c7c3fa1719
- evidence_id: chemistry
  kind: validation
  reference: RDKit independent structure calculation
  locator: Native SMILES and Standard InChI parsed separately
  accessed_at: '2026-10-21T07:39:29Z'
  support: supports
  summary: Both encodings reproduce the native complete InChIKey. Calculation gives
    C15H17NO3, charge0, one connected component, average mass259.305 and exact mass259.120843404;
    the stated geometric structure is internally consistent.
  snapshot_sha256: 13d75fa4dd576b90158f2bb67a1384e93aa33abdecd07381366713367a407d35
- evidence_id: registry
  kind: authority
  reference: https://www.reaxys.com/reaxys/secured/search.do?searchType=quick&rid=9275104
  locator: Direct registry attempt
  accessed_at: '2026-10-21T07:41:40Z'
  support: partial
  summary: The public Reaxys detail route was inaccessible. Reaxys9275104 is verified
    as the current ChEBI assertion, not independently checked against registry substance
    detail.
- evidence_id: isolation
  kind: primary_source
  reference: PMID:12350167
  locator: DOI10.1021/np0200358; Europe PMC core abstract; ACS supporting information
    DOI10.1021/np0200358.s001
  accessed_at: '2026-10-21T07:38:57Z'
  support: supports
  summary: The primary abstract explicitly reports isolation from cultured Penicillium
    mycelia and assigns the major ravenic-acid isomer (3Z,7E,9E,11E,13E). The main
    text was unavailable through attempted free routes. It does not give a strain
    designation, bacterial assay protocol, numerical potency or target in the inspected
    abstract.
  snapshot_sha256: 2388e13ffd0c3aa31c4f44fc342a08e0b83abbcebebe211e73d607a3812d0428
- evidence_id: isolation-supplement
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/5826045
  locator: Official ACS supplement np0200358_si_001.pdf; visually inspected page1
    Figure4
  accessed_at: '2026-10-21T07:39:23Z'
  support: supports
  summary: The proton-NMR page includes the ravenic-acid structural drawing with the
    tetramic-acid ring and tetraene side chain, consistent with the native structure.
    This spectral supplement is not antibacterial assay evidence; no independent spectral
    re-elucidation is claimed.
  snapshot_sha256: 79ff3c42f3c7412d36e9ef3fa104ade8ee19ce06e8eb8a1fe499e7034d4a4bce
- evidence_id: synthesis
  kind: primary_source
  reference: PMID:20066698
  locator: DOI10.1002/chem.200902544; Europe PMC core abstract and publisher abstract/reference
    page
  accessed_at: '2026-10-21T07:38:57Z'
  support: context_only
  summary: The primary abstract describes synthesis of ravenic acid among 3-oligoenoyl
    tetramic acids and structure-dependent antimicrobial/cytotoxic activity across
    the series. Full Methods and compound-specific results were unavailable; the class-level
    abstract cannot establish an exact ravenic-acid MIC or a direct molecular target.
  snapshot_sha256: 2388e13ffd0c3aa31c4f44fc342a08e0b83abbcebebe211e73d607a3812d0428
- evidence_id: producer-primary
  kind: primary_source
  reference: PMID:27519121
  locator: DOI10.1039/c6ob00938g; full primary PDF pp8259-8260, Isolation of fungus,
    Culturing of MINAP-9902 and HPLC; https://researchoutput.csu.edu.au/ws/portalfiles/portal/408867925/317637819.pdf
  accessed_at: '2026-10-21T07:39:48Z'
  support: supports
  summary: The paper describes isolation and culture of Penicillium sp. MINAP-9902
    from a surface-sterilized Lycogala epidendrum fruiting body. Cultured mycelia
    were extracted; the six-day potato-dextrose-broth sample had a strong HPLC peak
    assigned to ravenic acid at14.4min. Combined with the original isolation abstract,
    this supports a bounded producer follow-up for that isolate at genus rank. The
    myxomycete is collection context, not the experimentally cultured fungal producer.
    No species-level identification, sequence accession or BGC is established.
  snapshot_sha256: 50f48f1b56bfd212b97e3c8018330a585e0c3a317f611bc7edaf5ebd7f5dd870
- evidence_id: analogue-boundary
  kind: primary_source
  reference: PMID:27519121
  locator: DOI10.1039/c6ob00938g; pp8253-8255 Figure1 and Results; p8260 sensitivity
    methods; Figure1 visually inspected
  accessed_at: '2026-10-21T07:39:48Z'
  support: context_only
  summary: Ravenic acid is compound1; the newly characterized ravynic acid is compound3
    with a distinct polyeneyne chain and C15H15NO3 composition. The reported2.5microgram/mL
    inhibition belongs to ravynic acid. The25microgram/mL ravenic-acid comparison
    explicitly cites the2002 paper and is not a newly established exact-isomer MIC
    in this review. Disk screening and OD600 sensitivity methods concern the study
    system; they cannot substitute for unread original assay conditions or establish
    a biochemical mechanism.
  snapshot_sha256: 50f48f1b56bfd212b97e3c8018330a585e0c3a317f611bc7edaf5ebd7f5dd870
- evidence_id: taxon
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=5073&mode=Info
  locator: Official taxon information, name and rank
  accessed_at: '2026-10-21T07:41:40Z'
  support: supports
  summary: NCBITaxon:5073 resolves to Penicillium at genus rank. MINAP-9902 is the
    paper isolate designation, not a species name or independently verified genome
    accession.
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: Ignored-inclusive local searches and bounded free primary-source discovery
  accessed_at: '2026-10-21T07:41:40Z'
  support: context_only
  summary: The target raw row and PATHS agree. Focused searches found readiness/historical
    discovery leads but no target-specific curator override. Primary discovery found
    the two adopted papers and the2016 analogue study. Other broad-search hits were
    not treated as target-specific mechanism or producer evidence.
  search_scope: prepare.py41 used rg --no-ignore --hidden across batch005 excluding
    .git/.venv. Follow-up searches covered raw, curation, conf, scripts, tests, reviews,
    reports and the actual data/antibiotics/PATHS.tsv for66291,ravenic,full key and
    minted identifier. An initial mistaken root PATHS.tsv location was corrected.
    Hidden and ignored files were included. Europe PMC exact phrase ravenic acid and
    free web queries combined both DOIs, ravenic acid, MINAP9902, antimicrobial and25;
    ACS/Wiley full texts were inaccessible. Historical September report served only
    as a lead and its blanket missing-field severity was not adopted.
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Producer, exact-form equivalence, assay and mechanism rules
  accessed_at: '2026-10-21T07:41:40Z'
  support: supports
  summary: Optional blanks are not defects. The concrete primary isolate/compound
    observation warrants a limited producer disposition. A genus-level taxon must
    not become a species claim; analogue or class activity cannot supply a mechanism
    or exact-isomer assay.
- evidence_id: validation
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual batch005 focused executions; scratch041-validation.tsv
  accessed_at: '2026-10-21T07:38:38Z'
  support: supports
  summary: Both commands exited0. LinkML reported no issues; strict scanned one target
    with zero ERROR rows.
  snapshot_sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
assessments:
- assessment_id: identity
  area: identity
  topic: Exact (3Z) geometric form
  outcome: supported
  summary: The current ChEBI structure, native names and full chemistry agree. Original
    abstract identifies the major geometric isomer. Experimental preparations must
    not automatically be treated as analytically pure3Z material.
  target_ids:
  - CHEBI:66291
  evidence_ids:
  - record
  - chebi
  - chemistry
  - isolation
  - isolation-supplement
- assessment_id: grounding
  area: grounding
  topic: Broader parents, activity roles and registry
  outcome: supported
  summary: Three broader classes and source antibacterial/antimicrobial roles are
    appropriate. Reaxys is source-asserted with direct detail unavailable; no contradictory
    xref evidence was found.
  target_ids:
  - CHEBI:66291
  evidence_ids:
  - owner
  - chebi
  - parent-26177
  - parent-33823
  - parent-74223
  - registry
- assessment_id: evidence
  area: evidence
  topic: Adopted publication scope
  outcome: supported
  summary: Both adopted PMIDs resolve to the stated primary papers. The native seed
    does not promote their citations into unsupported target or potency claims.
  target_ids:
  - CHEBI:66291
  evidence_ids:
  - owner
  - isolation
  - synthesis
- assessment_id: producer
  area: completeness
  topic: Specific cultured-isolate evidence
  outcome: concern
  summary: Primary full text supplies Penicillium sp.MINAP-9902 culture/extraction
    and a ravenic-acid HPLC assignment, complementing original isolation. A genus-ranked
    producer annotation or explicit disposition is a concrete minor follow-up. Species,
    BGC and host-as-producer inferences remain unsupported.
  target_ids:
  - CHEBI:66291
  evidence_ids:
  - producer-primary
  - isolation
  - taxon
  - rubric
- assessment_id: activity
  area: evidence
  topic: Exact-compound quantitative antibacterial activity
  outcome: unknown
  summary: The2016 text distinguishes ravenic25microgram/mL historical comparison
    from ravynic2.5microgram/mL. The original ravenic assay protocol, exact bacterial
    isolate and isomeric preparation remain uninspected, so no new quantitative activity
    observation is justified yet.
  target_ids:
  - CHEBI:66291
  evidence_ids:
  - isolation
  - synthesis
  - analogue-boundary
- assessment_id: mechanism
  area: evidence
  topic: Mode, direct target and causal chain
  outcome: unknown
  summary: No native mechanism or target is asserted, and inspected source text supplies
    no compound-specific molecular target or lethal causal chain. Polyene or tetramic-acid
    family membership does not fill that gap.
  target_ids:
  - CHEBI:66291
  evidence_ids:
  - record
  - isolation
  - synthesis
  - analogue-boundary
  - rubric
- assessment_id: other
  area: scope
  topic: Resistance, clinical status and datasets
  outcome: not_applicable
  summary: No native assertions require correction in these fields. The inspected
    isolation/synthesis studies do not establish a resistance determinant, current
    clinical product status or transcriptomics dataset.
  target_ids:
  - CHEBI:66291
  evidence_ids:
  - record
  - producer-primary
  - analogue-boundary
- assessment_id: provenance
  area: provenance
  topic: Generated ownership and scientific status
  outcome: supported
  summary: The raw owner, source concept and three seed/reseed events agree. Any new
    producer annotation is curator-owned and requires claim-level evidence and validated
    history; native SEEDED status remains unchanged.
  target_ids:
  - CHEBI:66291
  evidence_ids:
  - record
  - owner
  - rubric
- assessment_id: schema
  area: schema
  topic: Focused gates
  outcome: supported
  summary: Both focused native validators pass.
  target_ids:
  - CHEBI:66291
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: chebi-66291-minap-9902-producer-disposition
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Curated disposition of the specific MINAP-9902 producer evidence
  description: Inspected primary text names the cultured Penicillium isolate MINAP-9902
    and assigns a ravenic-acid peak in its extract, while the original abstract supports
    isolation from Penicillium mycelia. The seed definition already records genus-level
    origin; a structured, narrowly evidenced producer claim or explicit applicability
    disposition would preserve the newly verified isolate context. This is a source-specific
    annotation opportunity, not a requirement to populate every optional field.
  target_ids:
  - CHEBI:66291
  field_paths:
  - producer_organisms
  evidence_ids:
  - record
  - producer-primary
  - isolation
  - taxon
  - rubric
  rule_id: native-review-checklist:Producer
  native_severity: minor evidence-specific producer provenance gap
  normalization_reason: The seed is not scientifically contradicted; the newly inspected
    primary isolate evidence creates a non-blocking curator follow-up.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/3z-ravenic-acid.yaml
    role: Curator-owned scientific annotations through the validated writer and curation
      history
actions:
- action_id: A1
  description: Adjudicate and, if appropriate, curate the exact ravenic-acid producer
    link to Penicillium at genus rank with isolate MINAP-9902, retaining source identification
    limits.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:66291
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/3z-ravenic-acid.yaml
    role: Curator-owned scientific annotations through the validated writer and curation
      history
  acceptance_checks:
  - Attach PMID:12350167 and the specific isolation/culture/HPLC sections of PMID:27519121
    to the producer claim or explicit disposition.
  - Use NCBITaxon:5073 with taxon_label Penicillium and isolate designation MINAP-9902
    separately; do not infer species, genome or BGC.
  - State that the2016 HPLC assignment complements the original isolation abstract;
    do not claim independent isomer-purity characterization or confuse the myxomycete
    collection substrate with the fungal producer.
  - Keep ravynic acid compound3 and its2.5microgram/mL result separate; retrieve original2002/2010
    assay details and exact preparation mapping before adding a quantitative activity_spectrum
    observation.
  - Use the native validated writer and curation history for any future annotation
    and retain SEEDED unless all sign-off criteria pass.
limitations:
- The2002 and2010 primary main texts remained unavailable through attempted free routes.
  Their abstracts and the2002 spectral supplement were inspected; original assay protocol,
  exact clinical isolate and tested isomer composition remain unresolved.
- The2016 full text supplies specific culture/HPLC producer context, but its25microgram/mL
  ravenic result is a retrospective citation. Its2.5microgram/mL result belongs to
  distinct ravynic acid.
- Reaxys detail was inaccessible; the cross-reference remains verified only as an
  official ChEBI assertion.
- Bounded literature searches do not prove absence of additional exact-compound studies
  or establish a molecular mechanism.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Initial capture preceded judgment; all original hashes and Git base are retained
  in the expanded20-input provenance.
- Ignored and hidden files were included in the stated local search scopes.
- The older ad hoc report was not converted, and its broad missing-optional-field
  finding was not adopted. No native scientific status or record content was changed.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:66291
- https://doi.org/10.1021/np0200358
- https://doi.org/10.1002/chem.200902544
- https://doi.org/10.1039/c6ob00938g
tags:
- antibacterial
- ravenic-acid
- producer
- exact-stereochemistry
- seeded
```
