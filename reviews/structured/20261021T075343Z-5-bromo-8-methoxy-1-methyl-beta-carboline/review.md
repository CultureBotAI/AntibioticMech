# Bromomethoxy methyl beta-carboline: SMILES defect and primary MID evidence

- Review: 20261021T075343Z-5-bromo-8-methoxy-1-methyl-beta-carboline
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T07:36:19Z
- Finished UTC: 2026-10-21T07:53:43Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One major inherited SMILES defect is confirmed: missing indole NH prevents parsing although focused native gates pass. Intended alkaloid identity and qualitative definition are supported. One minor follow-up concerns exact MID observations, with journal/thesis disagreement and assay, solvate and source-organism boundaries retained.

## Scope And Provenance

Complete exact-record identity, provenance, evidence-scope and bounded scientific review.

Selection: Queue index 048; exactly CHEBI:65524 in isolated batch005.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65524 | data/antibiotics/antibacterial/5-bromo-8-methoxy-1-methyl-β-carboline.yaml | generated | 5-bromo-8-methoxy-1-methyl-β-carboline |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema validation | passed | True | CHEBI:65524 | Coordinator executed the exact focused command; reviewer inspected successful logs. |
| Focused strict validation | passed | True | CHEBI:65524 | Coordinator executed the exact focused command; reviewer inspected successful logs. |
| Independent native cross-encoding consistency | failed | True | CHEBI:65524 | Corrected chemistry helper fails for the invalid native SMILES; valid InChI and source mint agree. |
| Structured expression-source applicability | not_applicable | False | CHEBI:65524 | The native record names no gene, protein, regulator, pathway, stress response or transcriptomic dataset. P388 and organism-growth assays do not themselves establish a structured expression-source query. |
| Authoritative full QC | failed | True | CHEBI:65524 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65524 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65524 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65524 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65524 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65524 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65524 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65524 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65524 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Intended exact alkaloid

identity: supported. Targets: CHEBI:65524.

The label, synonym, native InChI/key, formula, charge and masses identify the published exact compound. Crystal solvent is separate from the molecular moiety.

### Missing indole NH in SMILES

consistency: concern. Targets: CHEBI:65524.

The native and current ChEBI SMILES lack required indole NH encoding and fail parsing. The validated candidate restores agreement without changing the pyridine nitrogen or intended structure.

### Broader parents and dual activity roles

grounding: supported. Targets: CHEBI:65524.

All four parents are broader valid classes. Both antibacterial and antifungal roles are retained despite ANTIBACTERIAL filing, and the exact primary supplement corroborates activity against the named bacteria/fungi. No xrefs are asserted.

### Isolation, cytotoxicity and activity wording

evidence: supported. Targets: CHEBI:65524.

The definition is properly attributed to ChEBI. Exact primary abstract/supplement support the qualitative isolation, P388 and antimicrobial statements; it makes no false quantitative claim.

### Qualified MID observation disposition

completeness: concern. Targets: CHEBI:65524.

The exact primary row provides a specific annotation opportunity. Preserve MID endpoint, per-disc units, ranges, isolate-source limits and disagreement with the earlier thesis; do not silently normalize to MIC.

### Exact antibacterial mechanism and targets

evidence: unknown. Targets: CHEBI:65524.

No native mode or target is asserted. Phenotypic inhibition and P388 cytotoxicity do not establish direct microbial binding or a lethal causal chain. Related beta-carboline mechanisms are not transferred.

### Natural isolation versus biosynthesis

scope: unknown. Targets: CHEBI:65524.

Species identity and isolation context are supported. A biosynthetic producer, symbiont or BGC is not established by the inspected whole-animal extraction evidence; no structured producer assertion is forced.

### Resistance, clinical, datasets and causal graph

scope: not_applicable. Targets: CHEBI:65524.

No native assertions need correction in these categories. The inspected results do not establish resistance determinants, clinical efficacy/approval, a transcriptomic dataset or a causal graph.

### Maintained ownership and history

provenance: supported. Targets: CHEBI:65524.

The defective encoding is inherited from the adopted and current source. Source concept/version and all seed/reseed events remain consistent; no native status promotion occurred.

### Focused gates versus chemical validity

schema: supported. Targets: CHEBI:65524.

Both actual focused native validators pass, while the separate chemical consistency check fails.

## Findings

### F1: Source-owned SMILES omits the indole NH

major / open / confirmed; issue key: chebi-65524-smiles-missing-indole-nh.

The aromatic indole nitrogen is encoded as n without hydrogen, so the native SMILES cannot be kekulized. The valid native InChI and primary structural evidence require NH. An exact bounded candidate matches every declared structural identifier and mass. Current ChEBI repeats the defective string, requiring a reproducible source correction rather than a record-only patch.

### F2: Retain exact primary MID observations with source disagreement

minor / open / confirmed; issue key: chebi-65524-primary-mid-observation-disposition.

The official revised supplement provides exact compound-specific minimum inhibitory dose ranges that can support qualified activity annotations. A curator disposition should preserve those reported units and endpoint, source-isolate limitations and the earlier thesis disagreement. The seed already has supported qualitative activity; this is a specific evidence opportunity rather than a requirement to populate every optional slot.

## Recommended Actions And Acceptance Checks

### A1

Correct the exact source-owned indole SMILES through an auditable source/extractor path and regenerate the target.

- Adjudicate COc1ccc(Br)c2c1[nH]c1c(C)nccc12 against the valid native InChI and primary structure; do not indiscriminately change both nitrogen atoms.
- Require parse success and equality to OVNRKQHNHZRXHF-UHFFFAOYSA-N, C13H11BrN2O, charge 0 and the recorded masses.
- Retain upstream correction/override provenance and manifest consistency; use the documented one-record canary before broader regeneration.
- Pass focused schema/strict gates, explicit chemical consistency, source provenance, corpus reproduction and required QC.

### A2

After structural correction, curate or explicitly disposition the exact journal-supplement MID evidence.

- Cite the revised DOI:10.1021/np8007655.s001 Table S5 at each supported observation and keep the exact compound 1 row separate from comparator rows.
- Represent the endpoint as reported minimum inhibitory dose in microgram/disc, preserve range and named organism/source-strain context, and do not manufacture a broth MIC, accession, breakpoint or zone diameter.
- Record the earlier Till thesis disagreement in fungal values and units; do not silently combine or convert incompatible source values.
- Obtain the main article protocol or retain its unavailability explicitly before claiming complete standardized susceptibility context.
- Keep methanol-solvate crystal composition, P388 cytotoxicity and whole-animal isolation separate from antibacterial mechanism and biosynthetic producer assertions.
- Use the native validated writer/history for future curation; leave SEEDED until sign-off criteria pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/5-bromo-8-methoxy-1-methyl-β-carboline.yaml; Every field of the native YAML | supports | The ChEBI-only record is ANTIBACTERIAL, SEEDED and EXACT. Its definition includes source-organism isolation, P388 cytotoxicity and antibacterial/antifungal activity. One synonym, four parents, two roles, full structure, source concept and all three history events were read. No xrefs, direct targets, mechanism, structured activity, resistance, producer, clinical, dataset or causal graph claims are asserted. |
| owner | data/raw/chebi_antimicrobials.tsv; CHEBI:65524 row 1211; data/antibiotics/PATHS.tsv row 1462; MANIFEST, configuration, extractor and seeder | supports | The raw owner contains the same SMILES defect and otherwise agrees with the native identity. Adopted PMID:19220033, source version 2026-08-30 and minted identifier antibioticmech:chebi-16255b92a3 match. The mint was independently checked by the coordinator against the repository SHA256-based algorithm. Source identity corrections belong to the extraction/seeding path; new scientific annotations are curator-owned. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:65524; Official visible identity, full structure, parents, roles, synonym and metabolite species | partial | Current ChEBI repeats the unparseable SMILES COc1ccc(Br)c2c1nc1c(C)nccc12 while the InChI, key OVNRKQHNHZRXHF-UHFFFAOYSA-N, formula C13H11BrN2O, charge 0 and masses describe the NH-containing alkaloid. It retains both antibacterial and antifungal roles and all four broader classes. Pterocella vesiculosa is linked to WoRMS:467054 and PMID:19220033. These are authority assertions, not independent mechanistic measurements. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/42638980; Official PUG property response supplied by coordinator and inspected independently | supports | The complete InChI/key and formula match the native record. ConnectivitySMILES CC1=NC=CC2=C1NC3=C(C=CC(=C23)Br)OC has the expected NH and supports the same unsolvated molecular identity. No PubChem xref was added. |
| parent-22315 | https://www.ebi.ac.uk/chebi/CHEBI:22315; Official class definition | supports | The term resolves to alkaloid, a broader class consistent with the intended molecule. Class membership alone does not supply a direct target or mode of action. |
| parent-35618 | https://www.ebi.ac.uk/chebi/CHEBI:35618; Official class definition | supports | The term resolves to aromatic ether, a broader class consistent with the intended molecule. Class membership alone does not supply a direct target or mode of action. |
| parent-60834 | https://www.ebi.ac.uk/chebi/CHEBI:60834; Official class definition | supports | The term resolves to beta-carbolines, a broader class consistent with the intended molecule. Class membership alone does not supply a direct target or mode of action. |
| parent-37141 | https://www.ebi.ac.uk/chebi/CHEBI:37141; Official class definition; same-session snapshot from the immediately preceding exact review | supports | Organobromine compound denotes compounds containing a carbon-bromine bond and is strictly broader than this molecule. |
| chemistry | RDKit independent chemical consistency; Coordinator actual chem005.py 48 execution, reviewed script/result; scratch 048-chemistry.json | refutes | Native SMILES cannot be kekulized; native InChI parses and produces the complete recorded key, formula, charge, masses and one fragment. Corrected helper execution exits 1 solely for the SMILES failure; mint comparison passes. The earlier helper-algorithm mistake was corrected and is not a native finding. |
| candidate | RDKit InChI regeneration and bounded correction test; Reviewer scratch 048-correction-candidate.json | supports | Both InChI regeneration and a single explicit NH correction yield COc1ccc(Br)c2c1[nH]c1c(C)nccc12. This parses to OVNRKQHNHZRXHF-UHFFFAOYSA-N, C13H11BrN2O, charge 0, average mass 291.148 and exact mass 290.005475072. The second pyridine nitrogen remains n. No native mutation occurred. |
| adopted-primary | PMID:19220033; DOI:10.1021/np8007655; Europe PMC core abstract | supports | The primary abstract names the exact alkaloid as compound 1 isolated from Pterocella vesiculosa, characterized by NMR, mass spectrometry and single-crystal X-ray diffraction. It states that P388 and three microorganism assays were performed. Main article text was unavailable through the attempted publisher route; the official revised supplement supplies exact results. |
| primary-structure | DOI:10.1021/np8007655.s001; https://ndownloader.figshare.com/files/4559464 ; revised supplement pp 4-8, Tables S1-S3 | supports | The primary crystal characterization is explicitly the methanol solvate, formula C14H15BrN2O2, and Table S3 includes the indole N-H bond. The molecular moiety agrees with the native unsolvated InChI; solvate composition should not replace the native formula or be mistaken for the assay preparation. This is small-molecule crystallography, not target binding. |
| primary-activity | DOI:10.1021/np8007655.s001; Same revised supplement p 10, Table S5 exact compound 1 row and footnotes; visually inspected | supports | The exact row reports minimum inhibitory doses of 2-4 microgram/disc against Bacillus subtilis and 7.5-15 microgram/disc against both Candida albicans and Trichophyton mentagrophytes. The strains were held at the University of Canterbury; accession numbers are not supplied. Comparator values are from a separate 1991 paper. These ranges are MID disk endpoints, not broth MICs or measured zone diameters. |
| primary-p388 | DOI:10.1021/np8007655.s001; Same revised supplement p 9, Table S4 row for compound 1 and footnote a | supports | Compound 1 has P388 IC50 5089 ng/mL, defined as 50 percent inhibition of cell growth in ATCC CCL 46. This supports the native cytotoxicity context, without establishing an antibacterial mechanism, in-vivo antitumour efficacy or clinical approval. |
| thesis-conflict | https://hdl.handle.net/10289/2498; Till M, Studies of New Zealand Marine Organisms, MSc thesis (2007), pp 42-43, 68-85 and 115-117; exact file https://researchcommons.waikato.ac.nz/bitstreams/e5440311-d3f0-4531-9b80-a3df0217295b/download | context_only | The original author identifies the same molecule as compound 190. Her p 85 antimicrobial ranges are 2-4, 4-5 and 4-5 microgram/mL for the same three organisms, conflicting with the later revised journal supplement in fungal values and units. The thesis describes disk testing and whole-bryozoan extraction, not a proven biosynthetic producer. Preserve the disagreement; no correction history establishing why values changed was inspected. |
| worms | https://www.marinespecies.org/aphia.php?p=taxdetails&amp;id=467054; Official WoRMS AphiaRecordByAphiaID response | supports | Pterocella vesiculosa (Lamarck, 1816) is accepted at species rank, a marine bryozoan in Catenicellidae. This confirms organism identity in the isolation statement; it does not itself establish which cells biosynthesize the alkaloid. |
| search | CultureBotAI/AntibioticMech; Ignored-inclusive exact-target searches and bounded free source discovery | context_only | Only adopted raw/PATHS and readiness leads appeared in the focused maintained-input search. No existing target-specific curator correction was found in the stated scopes. The initial supplied thesis lead was a later Shrubsall 2017 review chapter; it was not mistaken for Till primary evidence. Correct author thesis and official ACS supplement were subsequently inspected. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Identity, structure, activity, mechanism and producer standards | supports | All structure encodings must agree. Assay units and organism scope require claim-level evidence. Optional blanks alone are not findings; newly inspected exact-compound assay results create a concrete follow-up. Whole-organism extraction is distinct from demonstrated biosynthesis, and cytotoxicity is not a specific microbial target. |
| focused-validation | just validate; just validate-strict; Coordinator actual batch005 executions, logs and scratch 048-focused-results.json/048-strict.tsv | supports | The recorded schema and strict commands both exited 0. LinkML found no issues and strict scanned one record with zero ERROR rows. The reviewer inspected their actual logs; those gates do not detect the independent SMILES defect. |

## Limits And Additional Notes

- The main 2009 journal article was unavailable through the attempted free publisher route. Its primary abstract and official revised supplement were inspected, together with the original author thesis; full journal assay protocol remains unresolved.
- The revised supplement and earlier thesis disagree in fungal activity values and units. The supplement explicitly reports MID per disc; these data cannot be silently converted to broth MICs.
- Test strains in the supplement have institutional provenance but no accession numbers. Solvate characterization does not establish the precise assay dosing preparation or prove a molecular target.
- Whole-bryozoan extraction supports isolation context but does not independently establish cellular biosynthesis, a producer strain or BGC. Bounded discovery is not proof that no other exact-compound studies exist.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Coordinator capture preceded assessment. All original input hashes and Git base were preserved and the expanded 20-input capture rechecked.
- The initial supplied 2017 thesis was used only as discovery context; the exact Till 2007 author thesis and official revised ACS supplement were independently located.
- The native record and scientific status were not modified. The corrected chemistry helper, not its earlier mint-algorithm mistake, supports the finding.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T075343Z-5-bromo-8-methoxy-1-methyl-beta-carboline
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Bromomethoxy methyl beta-carboline: SMILES defect and primary MID evidence'
started_at: '2026-10-21T07:36:19Z'
finished_at: '2026-10-21T07:53:43Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Reviewer did not create the seed. Parent captured provenance
    and executed focused gates; reviewer read the whole record, actual outputs, official
    identities and primary supplement/thesis, and independently tested the exact correction
    candidate.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'One major inherited SMILES defect is confirmed: missing indole NH prevents
  parsing although focused native gates pass. Intended alkaloid identity and qualitative
  definition are supported. One minor follow-up concerns exact MID observations, with
  journal/thesis disagreement and assay, solvate and source-organism boundaries retained.'
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
  - path: data/antibiotics/antibacterial/5-bromo-8-methoxy-1-methyl-β-carboline.yaml
    sha256: af1af5a277c719338cd0af3309b1934f244df1b27f3959a9146b6d8771eeb807
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
- target_id: CHEBI:65524
  path: data/antibiotics/antibacterial/5-bromo-8-methoxy-1-methyl-β-carboline.yaml
  label: 5-bromo-8-methoxy-1-methyl-β-carboline
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
  description: Complete exact-record identity, provenance, evidence-scope and bounded
    scientific review.
  selection: Queue index 048; exactly CHEBI:65524 in isolated batch005.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65524
  exclusions:
  - target: Other beta-carbolines, pterocellins and methanol-solvate as a separate
      exact chemical form
    reason: Comparator and structural context only; no automatic activity, target
      or exact-form transfer.
checks:
- check_id: schema
  name: Focused schema validation
  status: passed
  required: true
  summary: Coordinator executed the exact focused command; reviewer inspected successful
    logs.
  target_ids:
  - CHEBI:65524
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/5-bromo-8-methoxy-1-methyl-β-carboline.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - focused-validation
- check_id: strict
  name: Focused strict validation
  status: passed
  required: true
  summary: Coordinator executed the exact focused command; reviewer inspected successful
    logs.
  target_ids:
  - CHEBI:65524
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/5-bromo-8-methoxy-1-methyl-β-carboline.yaml --out
    /private/tmp/am-review-session/048-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - focused-validation
- check_id: chemical-consistency
  name: Independent native cross-encoding consistency
  status: failed
  required: true
  summary: Corrected chemistry helper fails for the invalid native SMILES; valid InChI
    and source mint agree.
  target_ids:
  - CHEBI:65524
  command: .venv/bin/python /private/tmp/am-review-session/chem005.py 48
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - chemistry
  - candidate
- check_id: structured-adapter
  name: Structured expression-source applicability
  status: not_applicable
  required: false
  summary: The native record names no gene, protein, regulator, pathway, stress response
    or transcriptomic dataset. P388 and organism-growth assays do not themselves establish
    a structured expression-source query.
  target_ids:
  - CHEBI:65524
  evidence_ids:
  - record
  - primary-activity
  - primary-p388
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:65524
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
  - CHEBI:65524
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
  - CHEBI:65524
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
  - CHEBI:65524
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
  - CHEBI:65524
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
  - CHEBI:65524
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
  - CHEBI:65524
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
  - CHEBI:65524
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
  - CHEBI:65524
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/5-bromo-8-methoxy-1-methyl-β-carboline.yaml
  locator: Every field of the native YAML
  accessed_at: '2026-10-21T07:48:25Z'
  support: supports
  summary: The ChEBI-only record is ANTIBACTERIAL, SEEDED and EXACT. Its definition
    includes source-organism isolation, P388 cytotoxicity and antibacterial/antifungal
    activity. One synonym, four parents, two roles, full structure, source concept
    and all three history events were read. No xrefs, direct targets, mechanism, structured
    activity, resistance, producer, clinical, dataset or causal graph claims are asserted.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: CHEBI:65524 row 1211; data/antibiotics/PATHS.tsv row 1462; MANIFEST, configuration,
    extractor and seeder
  accessed_at: '2026-10-21T07:48:25Z'
  support: supports
  summary: The raw owner contains the same SMILES defect and otherwise agrees with
    the native identity. Adopted PMID:19220033, source version 2026-08-30 and minted
    identifier antibioticmech:chebi-16255b92a3 match. The mint was independently checked
    by the coordinator against the repository SHA256-based algorithm. Source identity
    corrections belong to the extraction/seeding path; new scientific annotations
    are curator-owned.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:65524
  locator: Official visible identity, full structure, parents, roles, synonym and
    metabolite species
  accessed_at: '2026-10-21T07:38:14Z'
  support: partial
  summary: Current ChEBI repeats the unparseable SMILES COc1ccc(Br)c2c1nc1c(C)nccc12
    while the InChI, key OVNRKQHNHZRXHF-UHFFFAOYSA-N, formula C13H11BrN2O, charge
    0 and masses describe the NH-containing alkaloid. It retains both antibacterial
    and antifungal roles and all four broader classes. Pterocella vesiculosa is linked
    to WoRMS:467054 and PMID:19220033. These are authority assertions, not independent
    mechanistic measurements.
  snapshot_sha256: 314a202d96e7fe56a5a8299b54be9b6b04505635ab5a02a0c3b66460718b1817
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/42638980
  locator: Official PUG property response supplied by coordinator and inspected independently
  accessed_at: '2026-10-21T07:38:15Z'
  support: supports
  summary: The complete InChI/key and formula match the native record. ConnectivitySMILES
    CC1=NC=CC2=C1NC3=C(C=CC(=C23)Br)OC has the expected NH and supports the same unsolvated
    molecular identity. No PubChem xref was added.
  snapshot_sha256: 88f3184a6c60c6c6a350cc15bebb40c288286023c0455e7d9e93393da46157ed
- evidence_id: parent-22315
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:22315
  locator: Official class definition
  accessed_at: '2026-10-21T07:45:25Z'
  support: supports
  summary: The term resolves to alkaloid, a broader class consistent with the intended
    molecule. Class membership alone does not supply a direct target or mode of action.
  snapshot_sha256: 640c0d651628aac18618288e632829ee4b9094676b870a49e7b8998e5c93d3f0
- evidence_id: parent-35618
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:35618
  locator: Official class definition
  accessed_at: '2026-10-21T07:45:28Z'
  support: supports
  summary: The term resolves to aromatic ether, a broader class consistent with the
    intended molecule. Class membership alone does not supply a direct target or mode
    of action.
  snapshot_sha256: 3fb2e555fde565c4741436915ab2dd8888bb49ebb7cf1a10a582de4acdbb60a9
- evidence_id: parent-60834
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:60834
  locator: Official class definition
  accessed_at: '2026-10-21T07:45:30Z'
  support: supports
  summary: The term resolves to beta-carbolines, a broader class consistent with the
    intended molecule. Class membership alone does not supply a direct target or mode
    of action.
  snapshot_sha256: e3044d9dd758d718863242b78dd403b13d7cf7731d7c7063691905b04062e93b
- evidence_id: parent-37141
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:37141
  locator: Official class definition; same-session snapshot from the immediately preceding
    exact review
  accessed_at: '2026-10-21T07:42:33Z'
  support: supports
  summary: Organobromine compound denotes compounds containing a carbon-bromine bond
    and is strictly broader than this molecule.
  snapshot_sha256: a0a8a6bfb21b42a90d643a0314d0f4246047fcfc1b6c0425af9cc481bab21384
- evidence_id: chemistry
  kind: validation
  reference: RDKit independent chemical consistency
  locator: Coordinator actual chem005.py 48 execution, reviewed script/result; scratch
    048-chemistry.json
  accessed_at: '2026-10-21T07:42:05Z'
  support: refutes
  summary: Native SMILES cannot be kekulized; native InChI parses and produces the
    complete recorded key, formula, charge, masses and one fragment. Corrected helper
    execution exits 1 solely for the SMILES failure; mint comparison passes. The earlier
    helper-algorithm mistake was corrected and is not a native finding.
  snapshot_sha256: 77d32da9f979c4afad60fa67158a6402cc06283130e88da9ec2a67ad03e06db1
- evidence_id: candidate
  kind: validation
  reference: RDKit InChI regeneration and bounded correction test
  locator: Reviewer scratch 048-correction-candidate.json
  accessed_at: '2026-10-21T07:45:30Z'
  support: supports
  summary: Both InChI regeneration and a single explicit NH correction yield COc1ccc(Br)c2c1[nH]c1c(C)nccc12.
    This parses to OVNRKQHNHZRXHF-UHFFFAOYSA-N, C13H11BrN2O, charge 0, average mass
    291.148 and exact mass 290.005475072. The second pyridine nitrogen remains n.
    No native mutation occurred.
  snapshot_sha256: c732cbc5d8a8d4db68ed7ee817dfeaf92ceadb34b3bed6b70a70527680078631
- evidence_id: adopted-primary
  kind: primary_source
  reference: PMID:19220033
  locator: DOI:10.1021/np8007655; Europe PMC core abstract
  accessed_at: '2026-10-21T07:38:12Z'
  support: supports
  summary: The primary abstract names the exact alkaloid as compound 1 isolated from
    Pterocella vesiculosa, characterized by NMR, mass spectrometry and single-crystal
    X-ray diffraction. It states that P388 and three microorganism assays were performed.
    Main article text was unavailable through the attempted publisher route; the official
    revised supplement supplies exact results.
  snapshot_sha256: 45bceead6b7112832286abc8b6a95926617c76a1046c9c272e3e9afe4d2d691f
- evidence_id: primary-structure
  kind: primary_source
  reference: DOI:10.1021/np8007655.s001
  locator: https://ndownloader.figshare.com/files/4559464 ; revised supplement pp
    4-8, Tables S1-S3
  accessed_at: '2026-10-21T07:45:42Z'
  support: supports
  summary: The primary crystal characterization is explicitly the methanol solvate,
    formula C14H15BrN2O2, and Table S3 includes the indole N-H bond. The molecular
    moiety agrees with the native unsolvated InChI; solvate composition should not
    replace the native formula or be mistaken for the assay preparation. This is small-molecule
    crystallography, not target binding.
  snapshot_sha256: 6f2c23e73a988432afa6644bdc76ba44c92234f4ac7739dfe94760f856cdf0a1
- evidence_id: primary-activity
  kind: primary_source
  reference: DOI:10.1021/np8007655.s001
  locator: Same revised supplement p 10, Table S5 exact compound 1 row and footnotes;
    visually inspected
  accessed_at: '2026-10-21T07:45:42Z'
  support: supports
  summary: The exact row reports minimum inhibitory doses of 2-4 microgram/disc against
    Bacillus subtilis and 7.5-15 microgram/disc against both Candida albicans and
    Trichophyton mentagrophytes. The strains were held at the University of Canterbury;
    accession numbers are not supplied. Comparator values are from a separate 1991
    paper. These ranges are MID disk endpoints, not broth MICs or measured zone diameters.
  snapshot_sha256: 6f2c23e73a988432afa6644bdc76ba44c92234f4ac7739dfe94760f856cdf0a1
- evidence_id: primary-p388
  kind: primary_source
  reference: DOI:10.1021/np8007655.s001
  locator: Same revised supplement p 9, Table S4 row for compound 1 and footnote a
  accessed_at: '2026-10-21T07:45:42Z'
  support: supports
  summary: Compound 1 has P388 IC50 5089 ng/mL, defined as 50 percent inhibition of
    cell growth in ATCC CCL 46. This supports the native cytotoxicity context, without
    establishing an antibacterial mechanism, in-vivo antitumour efficacy or clinical
    approval.
  snapshot_sha256: 6f2c23e73a988432afa6644bdc76ba44c92234f4ac7739dfe94760f856cdf0a1
- evidence_id: thesis-conflict
  kind: primary_source
  reference: https://hdl.handle.net/10289/2498
  locator: Till M, Studies of New Zealand Marine Organisms, MSc thesis (2007), pp
    42-43, 68-85 and 115-117; exact file https://researchcommons.waikato.ac.nz/bitstreams/e5440311-d3f0-4531-9b80-a3df0217295b/download
  accessed_at: '2026-10-21T07:46:07Z'
  support: context_only
  summary: The original author identifies the same molecule as compound 190. Her p
    85 antimicrobial ranges are 2-4, 4-5 and 4-5 microgram/mL for the same three organisms,
    conflicting with the later revised journal supplement in fungal values and units.
    The thesis describes disk testing and whole-bryozoan extraction, not a proven
    biosynthetic producer. Preserve the disagreement; no correction history establishing
    why values changed was inspected.
  snapshot_sha256: ef79298ffab0250c606d6ae26c630d178e2cfaedbd930502e55365d4e6848d43
- evidence_id: worms
  kind: authority
  reference: https://www.marinespecies.org/aphia.php?p=taxdetails&id=467054
  locator: Official WoRMS AphiaRecordByAphiaID response
  accessed_at: '2026-10-21T07:45:23Z'
  support: supports
  summary: Pterocella vesiculosa (Lamarck, 1816) is accepted at species rank, a marine
    bryozoan in Catenicellidae. This confirms organism identity in the isolation statement;
    it does not itself establish which cells biosynthesize the alkaloid.
  snapshot_sha256: 5d5adb2eb770103b26a498700b63d280ff6f625926b29f7892bbf610def2823a
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: Ignored-inclusive exact-target searches and bounded free source discovery
  accessed_at: '2026-10-21T07:48:25Z'
  support: context_only
  summary: Only adopted raw/PATHS and readiness leads appeared in the focused maintained-input
    search. No existing target-specific curator correction was found in the stated
    scopes. The initial supplied thesis lead was a later Shrubsall 2017 review chapter;
    it was not mistaken for Till primary evidence. Correct author thesis and official
    ACS supplement were subsequently inspected.
  search_scope: Coordinator prepare.py 48 searched batch005 with rg --no-ignore --hidden
    excluding .git/.venv. Reviewer repeated exact65524,key,minted identifier and full-name
    searches across raw, curation, conf, scripts, reviews, reports and data/antibiotics/PATHS.tsv.
    Hidden and ignored files were included. Free searches used DOI,np8007655,exact
    alkaloid name and Pterocella/carboline; the official author repository and ACS
    Figshare supplement were inspected. Related carbolines and review snippets were
    discovery context only.
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Identity, structure, activity, mechanism and producer standards
  accessed_at: '2026-10-21T07:48:25Z'
  support: supports
  summary: All structure encodings must agree. Assay units and organism scope require
    claim-level evidence. Optional blanks alone are not findings; newly inspected
    exact-compound assay results create a concrete follow-up. Whole-organism extraction
    is distinct from demonstrated biosynthesis, and cytotoxicity is not a specific
    microbial target.
- evidence_id: focused-validation
  kind: validation
  reference: just validate; just validate-strict
  locator: Coordinator actual batch005 executions, logs and scratch 048-focused-results.json/048-strict.tsv
  accessed_at: '2026-10-21T07:42:05Z'
  support: supports
  summary: The recorded schema and strict commands both exited 0. LinkML found no
    issues and strict scanned one record with zero ERROR rows. The reviewer inspected
    their actual logs; those gates do not detect the independent SMILES defect.
  snapshot_sha256: e44714244e914254fd9ad3e329952dc191caec6fadbc10635d3028aab558eb43
assessments:
- assessment_id: identity
  area: identity
  topic: Intended exact alkaloid
  outcome: supported
  summary: The label, synonym, native InChI/key, formula, charge and masses identify
    the published exact compound. Crystal solvent is separate from the molecular moiety.
  target_ids:
  - CHEBI:65524
  evidence_ids:
  - record
  - chebi
  - pubchem
  - adopted-primary
  - primary-structure
- assessment_id: structure
  area: consistency
  topic: Missing indole NH in SMILES
  outcome: concern
  summary: The native and current ChEBI SMILES lack required indole NH encoding and
    fail parsing. The validated candidate restores agreement without changing the
    pyridine nitrogen or intended structure.
  target_ids:
  - CHEBI:65524
  evidence_ids:
  - chemistry
  - candidate
  - chebi
  - primary-structure
- assessment_id: grounding
  area: grounding
  topic: Broader parents and dual activity roles
  outcome: supported
  summary: All four parents are broader valid classes. Both antibacterial and antifungal
    roles are retained despite ANTIBACTERIAL filing, and the exact primary supplement
    corroborates activity against the named bacteria/fungi. No xrefs are asserted.
  target_ids:
  - CHEBI:65524
  evidence_ids:
  - chebi
  - parent-22315
  - parent-35618
  - parent-37141
  - parent-60834
  - primary-activity
- assessment_id: definition
  area: evidence
  topic: Isolation, cytotoxicity and activity wording
  outcome: supported
  summary: The definition is properly attributed to ChEBI. Exact primary abstract/supplement
    support the qualitative isolation, P388 and antimicrobial statements; it makes
    no false quantitative claim.
  target_ids:
  - CHEBI:65524
  evidence_ids:
  - record
  - adopted-primary
  - primary-activity
  - primary-p388
  - worms
- assessment_id: activity
  area: completeness
  topic: Qualified MID observation disposition
  outcome: concern
  summary: The exact primary row provides a specific annotation opportunity. Preserve
    MID endpoint, per-disc units, ranges, isolate-source limits and disagreement with
    the earlier thesis; do not silently normalize to MIC.
  target_ids:
  - CHEBI:65524
  evidence_ids:
  - primary-activity
  - thesis-conflict
  - rubric
- assessment_id: mechanism
  area: evidence
  topic: Exact antibacterial mechanism and targets
  outcome: unknown
  summary: No native mode or target is asserted. Phenotypic inhibition and P388 cytotoxicity
    do not establish direct microbial binding or a lethal causal chain. Related beta-carboline
    mechanisms are not transferred.
  target_ids:
  - CHEBI:65524
  evidence_ids:
  - record
  - primary-activity
  - primary-p388
  - rubric
- assessment_id: producer
  area: scope
  topic: Natural isolation versus biosynthesis
  outcome: unknown
  summary: Species identity and isolation context are supported. A biosynthetic producer,
    symbiont or BGC is not established by the inspected whole-animal extraction evidence;
    no structured producer assertion is forced.
  target_ids:
  - CHEBI:65524
  evidence_ids:
  - adopted-primary
  - thesis-conflict
  - worms
  - rubric
- assessment_id: other
  area: scope
  topic: Resistance, clinical, datasets and causal graph
  outcome: not_applicable
  summary: No native assertions need correction in these categories. The inspected
    results do not establish resistance determinants, clinical efficacy/approval,
    a transcriptomic dataset or a causal graph.
  target_ids:
  - CHEBI:65524
  evidence_ids:
  - record
  - primary-activity
  - primary-p388
- assessment_id: provenance
  area: provenance
  topic: Maintained ownership and history
  outcome: supported
  summary: The defective encoding is inherited from the adopted and current source.
    Source concept/version and all seed/reseed events remain consistent; no native
    status promotion occurred.
  target_ids:
  - CHEBI:65524
  evidence_ids:
  - record
  - owner
  - chebi
- assessment_id: schema
  area: schema
  topic: Focused gates versus chemical validity
  outcome: supported
  summary: Both actual focused native validators pass, while the separate chemical
    consistency check fails.
  target_ids:
  - CHEBI:65524
  evidence_ids:
  - focused-validation
  - chemistry
findings:
- finding_id: F1
  issue_key: chebi-65524-smiles-missing-indole-nh
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Source-owned SMILES omits the indole NH
  description: The aromatic indole nitrogen is encoded as n without hydrogen, so the
    native SMILES cannot be kekulized. The valid native InChI and primary structural
    evidence require NH. An exact bounded candidate matches every declared structural
    identifier and mass. Current ChEBI repeats the defective string, requiring a reproducible
    source correction rather than a record-only patch.
  target_ids:
  - CHEBI:65524
  field_paths:
  - chemical_structure.smiles
  evidence_ids:
  - record
  - owner
  - chebi
  - pubchem
  - chemistry
  - candidate
  - primary-structure
  rule_id: native-review-checklist:Structure;docs/HARMONIZATION.md
  native_severity: major chemical structure consistency defect
  normalization_reason: The SMILES representation is chemically invalid despite schema
    success; the intended exact identity remains recoverable from independently supported
    InChI/key, so no wrong-compound grounding is alleged.
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
  issue_key: chebi-65524-primary-mid-observation-disposition
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Retain exact primary MID observations with source disagreement
  description: The official revised supplement provides exact compound-specific minimum
    inhibitory dose ranges that can support qualified activity annotations. A curator
    disposition should preserve those reported units and endpoint, source-isolate
    limitations and the earlier thesis disagreement. The seed already has supported
    qualitative activity; this is a specific evidence opportunity rather than a requirement
    to populate every optional slot.
  target_ids:
  - CHEBI:65524
  field_paths:
  - activity_spectrum
  evidence_ids:
  - primary-activity
  - thesis-conflict
  - rubric
  rule_id: native-review-checklist:Activity
  native_severity: minor source-specific annotation opportunity
  normalization_reason: No existing quantitative assertion is false. Directly inspected
    primary data warrant a limited follow-up with explicit disagreement and endpoint
    scope.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/5-bromo-8-methoxy-1-methyl-β-carboline.yaml
    role: Curator-owned scientific annotations through the validated writer and curation
      history
actions:
- action_id: A1
  description: Correct the exact source-owned indole SMILES through an auditable source/extractor
    path and regenerate the target.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:65524
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
  generator: scripts/extract_source_inventory.py and scripts/seed_from_sources.py
  acceptance_checks:
  - Adjudicate COc1ccc(Br)c2c1[nH]c1c(C)nccc12 against the valid native InChI and
    primary structure; do not indiscriminately change both nitrogen atoms.
  - Require parse success and equality to OVNRKQHNHZRXHF-UHFFFAOYSA-N, C13H11BrN2O,
    charge 0 and the recorded masses.
  - Retain upstream correction/override provenance and manifest consistency; use the
    documented one-record canary before broader regeneration.
  - Pass focused schema/strict gates, explicit chemical consistency, source provenance,
    corpus reproduction and required QC.
- action_id: A2
  description: After structural correction, curate or explicitly disposition the exact
    journal-supplement MID evidence.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:65524
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/5-bromo-8-methoxy-1-methyl-β-carboline.yaml
    role: Curator-owned scientific annotations through the validated writer and curation
      history
  depends_on:
  - A1
  acceptance_checks:
  - Cite the revised DOI:10.1021/np8007655.s001 Table S5 at each supported observation
    and keep the exact compound 1 row separate from comparator rows.
  - Represent the endpoint as reported minimum inhibitory dose in microgram/disc,
    preserve range and named organism/source-strain context, and do not manufacture
    a broth MIC, accession, breakpoint or zone diameter.
  - Record the earlier Till thesis disagreement in fungal values and units; do not
    silently combine or convert incompatible source values.
  - Obtain the main article protocol or retain its unavailability explicitly before
    claiming complete standardized susceptibility context.
  - Keep methanol-solvate crystal composition, P388 cytotoxicity and whole-animal
    isolation separate from antibacterial mechanism and biosynthetic producer assertions.
  - Use the native validated writer/history for future curation; leave SEEDED until
    sign-off criteria pass.
limitations:
- The main 2009 journal article was unavailable through the attempted free publisher
  route. Its primary abstract and official revised supplement were inspected, together
  with the original author thesis; full journal assay protocol remains unresolved.
- The revised supplement and earlier thesis disagree in fungal activity values and
  units. The supplement explicitly reports MID per disc; these data cannot be silently
  converted to broth MICs.
- Test strains in the supplement have institutional provenance but no accession numbers.
  Solvate characterization does not establish the precise assay dosing preparation
  or prove a molecular target.
- Whole-bryozoan extraction supports isolation context but does not independently
  establish cellular biosynthesis, a producer strain or BGC. Bounded discovery is
  not proof that no other exact-compound studies exist.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Coordinator capture preceded assessment. All original input hashes and Git base
  were preserved and the expanded 20-input capture rechecked.
- The initial supplied 2017 thesis was used only as discovery context; the exact Till
  2007 author thesis and official revised ACS supplement were independently located.
- The native record and scientific status were not modified. The corrected chemistry
  helper, not its earlier mint-algorithm mistake, supports the finding.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:65524
- https://pubchem.ncbi.nlm.nih.gov/compound/42638980
- https://doi.org/10.1021/np8007655
- https://doi.org/10.1021/np8007655.s001
- https://hdl.handle.net/10289/2498
tags:
- antibacterial
- antifungal
- beta-carboline
- smiles
- source-defect
- MID
```
