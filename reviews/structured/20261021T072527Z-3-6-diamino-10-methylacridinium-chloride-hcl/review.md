# 3,6-Diamino-10-methylacridinium chloride.HCl: exact salt and qualified binding evidence

- Review: 20261021T072527Z-3-6-diamino-10-methylacridinium-chloride-hcl
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T07:13:46Z
- Finished UTC: 2026-10-21T07:25:27Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact salt identity, source provenance and focused gates agree. One minor follow-up concerns qualified primary biochemical context and an additional antibacterial study whose exact reagent mapping remains unresolved. Acriflavine mixtures, the PTA complex and single chloride remain distinct; no unverified salt-specific potency or target is adopted.

## Scope And Provenance

Complete one-record review with exact-salt identity checks and bounded primary research.

Selection: Queue index028, exactly CHEBI:74727.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:74727 | data/antibiotics/antibacterial/3-6-diamino-10-methylacridinium-chloride-hcl.yaml | generated | 3,6-diamino-10-methylacridinium chloride.HCl |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Single-record LinkML schema | passed | True | CHEBI:74727 | Focused gate passed with no errors. |
| Single-record strict validation | passed | True | CHEBI:74727 | Focused gate passed with no errors. |
| Exact-salt identity and charge cross-check | passed | True | CHEBI:74727 | ChEBI, PubChem and local chemistry agree on stoichiometry, structure and net charge. |
| Independent CAS detail access | unavailable | False | CHEBI:74727 | Source xrefs corroborated through ChEBI and PubChem; direct registry detail pages/API unavailable. |
| Structured expression-dataset follow-up | not_applicable | False | CHEBI:74727 | No gene or transcriptomic dataset is asserted for this target. The cGAS paper is excluded mixture context, not an exact-target expression lead. |
| Authoritative full QC | failed | True | CHEBI:74727 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:74727 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:74727 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:74727 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:74727 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:74727 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:74727 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:74727 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:74727 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact chloride.HCl composition

identity: supported. Targets: CHEBI:74727.

Official sources and structure recomputation agree. The three SMILES fragments encode the defined salt composition, not an arbitrary acriflavine/proflavine mixture. No incorrect-charge or wrong-salt finding is supported.

### Antibacterial classification and hydrochloride parent

grounding: supported. Targets: CHEBI:74727.

The adopted class and parent are source-supported; missing automatic intercalator mapping is intentional.

### Registry cross-references

identity: supported. Targets: CHEBI:74727.

Both CAS numbers are asserted by ChEBI and corroborated in the exact-key PubChem record. Direct independent CAS detail access remains limited. No narrower stoichiometric inference is drawn from a generic vendor label.

### Qualified nucleic-acid interaction context

completeness: concern. Targets: CHEBI:74727.

The inspected primary preparation and uncomplexed-dye controls provide a concrete curation opportunity. A bounded note can distinguish physical interaction from demonstrated antibacterial mechanism and from the separately prepared complex.

### Direct antibacterial molecular target

evidence: unknown. Targets: CHEBI:74727.

No native target is asserted. Biochemical nucleic-acid association merits assessment, but does not identify a bacterial protein target or establish the full antimicrobial causal chain.

### Organism- and assay-specific potency

evidence: unknown. Targets: CHEBI:74727.

A relevant primary antibacterial study was located, but its reagent identity has not been resolved to this exact salt. Quantitative transfer remains withheld pending that mapping; this is not a claim that no assay literature exists.

### Producer, resistance, clinical, dataset and graph claims

scope: not_applicable. Targets: CHEBI:74727.

No native claims in these categories require correction. Human antiviral mixture experiments cannot populate this salt record. No biosynthetic producer, clinical approval, resistance determinant or causal edge is inferred.

### Generated ownership and status

provenance: supported. Targets: CHEBI:74727.

All seeded fields and history match their owners. Scientific annotations would need separate curator provenance; this review leaves native SEEDED unchanged.

### Focused schema gates

schema: supported. Targets: CHEBI:74727.

Both focused validators pass.

## Findings

### F1: Primary binding evidence and an unresolved assay lead warrant scoped follow-up

minor / open / confirmed; issue key: chebi-74727-qualified-nucleic-acid-binding-context.

The matched historical preparation supports bounded biochemical context. A later antibacterial study is a concrete additional lead, but its exact preparation needs resolution before transfer. The seed makes no false mechanistic assertion; these are non-blocking evidence-specific curation opportunities.

## Recommended Actions And Acceptance Checks

### A1

Add a bounded mechanistic note or explicit curator disposition for the exact-salt biochemical evidence. Assess any nucleic-acid target representation against the assay scope. Keep uncomplexed dye, PTA complex and acriflavine mixtures separate, and leave antimicrobial mode unresolved unless further exact-compound evidence supports it.

- Every added claim cites the exact preparation and uncomplexed-dye experiment, preserving cell-free conditions and nucleic-acid source.
- No protein target, bacterial synthesis-inhibition enum, MIC or complete lethal causal chain is inferred from binding alone.
- No cGAS, HIF, antiviral or mixture result is transferred by name similarity.
- Use native validated writer/history and required focused, reproducibility and QC gates.

### A2

Resolve the 2020 paper preparation using its structure figure and a product identifier or equivalent source evidence before attaching its activity to this salt.

- Preserve tested material identity, strain and assay conditions. Do not silently transfer mixture or single-chloride results.
- Keep microscopy/permeability responses and pull-down candidates distinct from direct binding or proven primary lethal targets.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/3-6-diamino-10-methylacridinium-chloride-hcl.yaml; Complete YAML: identity, chemical fields, six synonyms, two CAS xrefs, source concept and all history events | supports | The exact ChEBI-only seed is ANTIBACTERIAL, SEEDED and EXACT. It represents one chloride.HCl salt composition. No native mechanism, target, activity_spectrum, producer, resistance, clinical, dataset or causal_graphs objects or activity collections are present. |
| owner | data/raw/chebi_antimicrobials.tsv; CHEBI:74727 row1898; PATHS.tsv row2157; MANIFEST, extractor, source configuration and seeder | supports | Identity, structure, source version2026-08-30, minted identifier antibioticmech:chebi-2153d4565a and three history events match. The adopted row contains no PMID. Generated-field corrections belong upstream, while new scientific annotations belong on the actual record. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:74727; Live official entry; scratch028-chebi.html and parsed text | supports | ChEBI matches the exact salt label, definition, six synonyms, both CAS numbers, formula C14H14N3.Cl.HCl, charge0, masses, structure strings and key OEGQPXPIKZELFM-UHFFFAOYSA-N. It assigns hydrochloride CHEBI:36807 and antibacterial role CHEBI:33282. Additional intercalator/antiseptic/carcinogenic roles are source assertions rather than new primary evidence. It distinguishes a has-part single-chloride component from this salt and a separate containing mixture. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/15558347; PUG-View JSON identity descriptors, molecular formula and CAS provenance sections; scratch028-pubchem.json | supports | PubChem CID15558347 reproduces the exact InChI/key and summed formula C14H15Cl2N3. It lists CAS6034-59-9 with a CAS Common Chemistry attribution, and CAS10597-46-3 from other contributors. These corroborate the source xrefs; a shared commercial name does not identify all acriflavine preparations as this pure salt. |
| chemistry | RDKit structure recomputation; Both SMILES and InChI parsed; scratch028-chemistry.json | supports | The written formula sums to C14H15Cl2N3. RDKit gives net charge0, three encoded fragments, average mass296.201, exact mass295.06430284 and the same InChI/key from either representation. The chloride plus HCl encoding is internally consistent; proton normalization does not make it a free base or a proflavine mixture. |
| cas-access | https://commonchemistry.cas.org/; Direct detail pages for 6034-59-9 and 10597-46-3; public detail API attempts | partial | The page shell reported a failed detail load, and both API attempts returned 401. Independent registry detail content was not inspected. ChEBI and attributed PubChem assertions were inspected; no claim of direct CAS verification is made. |
| config | conf/sources.yaml; CHEBI:33282 class mapping and explicit exclusion comment forCHEBI:24853 intercalator | supports | ANTIBACTERIAL filing is reproducible. Intercalator is deliberately excluded from automatic mode mapping because it is too generic to name a target; the empty seeded mechanism is not a mapping defect. |
| primary-binding | PMID:19866747; DOI10.1083/jcb.47.2.500; scanned primary PDF at https://pdfs.semanticscholar.org/5189/d14f24807ef0f6019fa36420b62850d99d21.pdf ; Methods p501, Figure4A p505, TableII p506, TableIII p510 and Discussion p509 | supports | Methods identify recrystallized hydrochloride of 3,6-diamino-10-methylacridinium chloride, with TLC purity assessment. Separate uncomplexed-dye controls show spectral changes with calf-thymus DNA and yeast RNA at 25 µM. Much of the study concerns an acriflavine–phosphotungstate complex; its results must remain separate. This is cell-free binding evidence, not a bacterial MIC or direct demonstration of antibacterial synthesis inhibition. |
| primary-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search; Exact-title core result; scratch028-pta-core.json | supports | Europe PMC resolves PMID19866747, PMCIDPMC2108095 and DOI10.1083/jcb.47.2.500 to the 1970 Ladoulis and Gill paper. Its title and abstract match the downloaded primary PDF; publisher and Europe PMC PDF routes returned 403 before the indexed free copy was retrieved. |
| mixture-primary | PMID:27694309; https://pmc.ncbi.nlm.nih.gov/articles/PMC5224509/ ; DOI10.1093/nar/gkw878; Materials and Methods, Abstract and Discussion; scratch028-cgas.xml | context_only | The cGAS study explicitly used Sigma A8126, a mixture of methylacridinium chloride and proflavine. Its mammalian antiviral response and indirect cGAS engagement do not establish a direct target or antibacterial mechanism for this exact hydrochloride salt. |
| mesh-boundary | https://meshb.nlm.nih.gov/record/ui?ui=D000167; NLM 2026 MeSH descriptor: scope note and registry-related numbers | context_only | NLM defines Acriflavine as a mixture with 3,6-acridinediamine. Its nucleic-acid-intercalation description belongs to that descriptor, so a name-only search result cannot establish exact-salt activity. |
| local-search | CultureBotAI/AntibioticMech; Ignored-inclusive identifier, structure-key, registry and trypaflavine searches | context_only | Raw and PATHS references match. Focused curation, reviews and historical-report searches found no target-specific override or prior prose review in those scopes. Broad generated and research-ledger hits are discovery context only. |
| research-scope | Free primary literature and official identity sources; Exact salt/CAS/trypaflavine searches, followed by source-text inspection | context_only | Bounded research identified a relevant 2020 antibacterial paper using the name acriflavine hydrochloride; its exact purchased preparation remains unverified. Mixture, selective-medium, staining and PTA-complex results cannot supply interchangeable potency. The historical 1929 JAMA lead returned 403. |
| rubric | docs/CURATION.md; Native checklist: mechanism, targets, activity, producer, resistance, clinical status, datasets and graphs | supports | Optional empty fields are not schema defects. Mechanistic notes can retain narrowly supported experimental context without a protein-target claim or automatic antimicrobial-mode enum. Physical nucleic-acid association alone does not prove the organism-specific lethal pathway. |
| validation | just validate; just validate-strict; Isolated worktree003; scratch028-validation.tsv | supports | Both focused commands exited0. LinkML reported no issues; strict scanned one target with zero ERROR rows. |
| h-pylori-lead | PMID:33118020; DOI:10.1093/femsle/fnaa178; author-uploaded full text and PDF text at https://www.researchgate.net/profile/Inderjeet-Kaur-8/publication/347577605_Antibacterial_action_of_acriflavine_hydrochloride_for_eradication_of_the_gastric_pathogen_Helicobacter_pylori/links/607410324585150fe99f96bd/Antibacterial-action-of-acriflavine-hydrochloride-for-eradication-of-the-gastric-pathogen-Helicobacter-pylori.pdf; Introduction, Methods and Results; Figure 1 pixels not inspected | context_only | The 2020 study reports ACF-HCl from Sigma-Aldrich, without a catalog or CAS identifier in inspected Methods. It distinguishes acriflavine mixtures in its introduction. Reported MICs are 2 micrograms/mL for H. pylori 26695 and 20 micrograms/mL for E. coli W3110; clinical isolates used agar dilution. Membrane imaging, PI uptake and pull-down/proteomics provide cellular response and candidate-association evidence. The depicted salt composition and actual purchased preparation remain unresolved here, so these results are a concrete follow-up lead rather than verified CHEBI:74727 measurements or direct protein-binding proof. |

## Limits And Additional Notes

- Direct CAS Common Chemistry detail access failed; official ChEBI and attributed PubChem registry data were inspected.
- The primary 1970 paper was inspected as a scanned free copy, including visual checks of reagent identification and uncomplexed-dye Figure4. Its observations are biochemical; the review does not establish exact-salt bacterial killing mechanism or potency.
- Mixture-specific host-response experiments were inspected only to bound applicability. Bounded research does not establish global absence of additional exact-salt studies.
- The newly located H. pylori study was read as full text and PDF text, but its structure image and reagent catalog identity were not independently verified. Exact-salt applicability remains unresolved.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Capture preceded judgment; all original hashes and Git revision were retained when provenance inputs were expanded.
- Local searches used for absence statements included ignored and hidden files.
- The native record remains SEEDED; the finding concerns an inspected source rather than absent optional fields in general.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T072527Z-3-6-diamino-10-methylacridinium-chloride-hcl
kind: record
repository: CultureBotAI/AntibioticMech
title: '3,6-Diamino-10-methylacridinium chloride.HCl: exact salt and qualified binding
  evidence'
started_at: '2026-10-21T07:13:46Z'
finished_at: '2026-10-21T07:25:27Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Reviewer did not create or curate the seed and independently
    inspected official identity, primary Methods and relevant results; agent review
    is not human scientific sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Exact salt identity, source provenance and focused gates agree. One minor
  follow-up concerns qualified primary biochemical context and an additional antibacterial
  study whose exact reagent mapping remains unresolved. Acriflavine mixtures, the
  PTA complex and single chloride remain distinct; no unverified salt-specific potency
  or target is adopted.
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
  - path: data/antibiotics/PATHS.tsv
    sha256: 3b1d82d007878e4aca2c28f4001a468776b325b726da2e48abb76a3dc551cc38
    role: context
  - path: data/antibiotics/antibacterial/3-6-diamino-10-methylacridinium-chloride-hcl.yaml
    sha256: 847a6710880406e83f7364159f658a88acf35f44d00e07860fe0cd1f69287826
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
- target_id: CHEBI:74727
  path: data/antibiotics/antibacterial/3-6-diamino-10-methylacridinium-chloride-hcl.yaml
  label: 3,6-diamino-10-methylacridinium chloride.HCl
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
  description: Complete one-record review with exact-salt identity checks and bounded
    primary research.
  selection: Queue index028, exactly CHEBI:74727.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:74727
  exclusions:
  - target: Acriflavine mixtures, acriflavinium cation and single chloride records
    reason: Identity and source-boundary context only; each requires a separate record
      review.
checks:
- check_id: schema
  name: Single-record LinkML schema
  status: passed
  required: true
  summary: Focused gate passed with no errors.
  target_ids:
  - CHEBI:74727
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/3-6-diamino-10-methylacridinium-chloride-hcl.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: strict
  name: Single-record strict validation
  status: passed
  required: true
  summary: Focused gate passed with no errors.
  target_ids:
  - CHEBI:74727
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/3-6-diamino-10-methylacridinium-chloride-hcl.yaml
    --out /private/tmp/am-review-session/028-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
- check_id: identity
  name: Exact-salt identity and charge cross-check
  status: passed
  required: true
  summary: ChEBI, PubChem and local chemistry agree on stoichiometry, structure and
    net charge.
  target_ids:
  - CHEBI:74727
  evidence_ids:
  - chebi
  - pubchem
  - chemistry
- check_id: registry
  name: Independent CAS detail access
  status: unavailable
  required: false
  summary: Source xrefs corroborated through ChEBI and PubChem; direct registry detail
    pages/API unavailable.
  target_ids:
  - CHEBI:74727
  evidence_ids:
  - chebi
  - pubchem
  - cas-access
- check_id: structured-adapter
  name: Structured expression-dataset follow-up
  status: not_applicable
  required: false
  summary: No gene or transcriptomic dataset is asserted for this target. The cGAS
    paper is excluded mixture context, not an exact-target expression lead.
  target_ids:
  - CHEBI:74727
  evidence_ids:
  - record
  - mixture-primary
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:74727
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
  - CHEBI:74727
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
  - CHEBI:74727
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
  - CHEBI:74727
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
  - CHEBI:74727
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
  - CHEBI:74727
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
  - CHEBI:74727
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
  - CHEBI:74727
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
  - CHEBI:74727
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/3-6-diamino-10-methylacridinium-chloride-hcl.yaml
  locator: 'Complete YAML: identity, chemical fields, six synonyms, two CAS xrefs,
    source concept and all history events'
  accessed_at: '2026-10-21T07:17:55Z'
  support: supports
  summary: The exact ChEBI-only seed is ANTIBACTERIAL, SEEDED and EXACT. It represents
    one chloride.HCl salt composition. No native mechanism, target, activity_spectrum,
    producer, resistance, clinical, dataset or causal_graphs objects or activity collections
    are present.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: CHEBI:74727 row1898; PATHS.tsv row2157; MANIFEST, extractor, source configuration
    and seeder
  accessed_at: '2026-10-21T07:17:55Z'
  support: supports
  summary: Identity, structure, source version2026-08-30, minted identifier antibioticmech:chebi-2153d4565a
    and three history events match. The adopted row contains no PMID. Generated-field
    corrections belong upstream, while new scientific annotations belong on the actual
    record.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:74727
  locator: Live official entry; scratch028-chebi.html and parsed text
  accessed_at: '2026-10-21T07:14:21Z'
  support: supports
  summary: ChEBI matches the exact salt label, definition, six synonyms, both CAS
    numbers, formula C14H14N3.Cl.HCl, charge0, masses, structure strings and key OEGQPXPIKZELFM-UHFFFAOYSA-N.
    It assigns hydrochloride CHEBI:36807 and antibacterial role CHEBI:33282. Additional
    intercalator/antiseptic/carcinogenic roles are source assertions rather than new
    primary evidence. It distinguishes a has-part single-chloride component from this
    salt and a separate containing mixture.
  snapshot_sha256: ff89a8d46e1071d1c25e83987a70c78067447e424adeb15ef74f95a2b14708cc
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/15558347
  locator: PUG-View JSON identity descriptors, molecular formula and CAS provenance
    sections; scratch028-pubchem.json
  accessed_at: '2026-10-21T07:14:20Z'
  support: supports
  summary: PubChem CID15558347 reproduces the exact InChI/key and summed formula C14H15Cl2N3.
    It lists CAS6034-59-9 with a CAS Common Chemistry attribution, and CAS10597-46-3
    from other contributors. These corroborate the source xrefs; a shared commercial
    name does not identify all acriflavine preparations as this pure salt.
  snapshot_sha256: 4f32575a1434de4b0a2139ec8d7ba8c4a2b7cb2a2b3b57e0d61cc8f3d0471b32
- evidence_id: chemistry
  kind: validation
  reference: RDKit structure recomputation
  locator: Both SMILES and InChI parsed; scratch028-chemistry.json
  accessed_at: '2026-10-21T07:14:41Z'
  support: supports
  summary: The written formula sums to C14H15Cl2N3. RDKit gives net charge0, three
    encoded fragments, average mass296.201, exact mass295.06430284 and the same InChI/key
    from either representation. The chloride plus HCl encoding is internally consistent;
    proton normalization does not make it a free base or a proflavine mixture.
  snapshot_sha256: 76b060aca6188d425baa5fe3c41d500fe6b9d0771b086cca3722415f105e6bb9
- evidence_id: cas-access
  kind: authority
  reference: https://commonchemistry.cas.org/
  locator: Direct detail pages for 6034-59-9 and 10597-46-3; public detail API attempts
  accessed_at: '2026-10-21T07:17:55Z'
  support: partial
  summary: The page shell reported a failed detail load, and both API attempts returned
    401. Independent registry detail content was not inspected. ChEBI and attributed
    PubChem assertions were inspected; no claim of direct CAS verification is made.
- evidence_id: config
  kind: record_content
  reference: conf/sources.yaml
  locator: CHEBI:33282 class mapping and explicit exclusion comment forCHEBI:24853
    intercalator
  accessed_at: '2026-10-21T07:17:55Z'
  support: supports
  summary: ANTIBACTERIAL filing is reproducible. Intercalator is deliberately excluded
    from automatic mode mapping because it is too generic to name a target; the empty
    seeded mechanism is not a mapping defect.
- evidence_id: primary-binding
  kind: primary_source
  reference: PMID:19866747
  locator: DOI10.1083/jcb.47.2.500; scanned primary PDF at https://pdfs.semanticscholar.org/5189/d14f24807ef0f6019fa36420b62850d99d21.pdf
    ; Methods p501, Figure4A p505, TableII p506, TableIII p510 and Discussion p509
  accessed_at: '2026-10-21T07:15:58Z'
  support: supports
  summary: Methods identify recrystallized hydrochloride of 3,6-diamino-10-methylacridinium
    chloride, with TLC purity assessment. Separate uncomplexed-dye controls show spectral
    changes with calf-thymus DNA and yeast RNA at 25 µM. Much of the study concerns
    an acriflavine–phosphotungstate complex; its results must remain separate. This
    is cell-free binding evidence, not a bacterial MIC or direct demonstration of
    antibacterial synthesis inhibition.
  snapshot_sha256: edefd1c736b98fc9fbe93d2397290326e070751394fb15428ba2597f93b1310b
- evidence_id: primary-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search
  locator: Exact-title core result; scratch028-pta-core.json
  accessed_at: '2026-10-21T07:15:38Z'
  support: supports
  summary: Europe PMC resolves PMID19866747, PMCIDPMC2108095 and DOI10.1083/jcb.47.2.500
    to the 1970 Ladoulis and Gill paper. Its title and abstract match the downloaded
    primary PDF; publisher and Europe PMC PDF routes returned 403 before the indexed
    free copy was retrieved.
  snapshot_sha256: 47f4faf2e6ef92ff4f36c628088384d497cd5a0e361e4fe3cd4103e0427c112f
- evidence_id: mixture-primary
  kind: primary_source
  reference: PMID:27694309
  locator: https://pmc.ncbi.nlm.nih.gov/articles/PMC5224509/ ; DOI10.1093/nar/gkw878;
    Materials and Methods, Abstract and Discussion; scratch028-cgas.xml
  accessed_at: '2026-10-21T07:15:00Z'
  support: context_only
  summary: The cGAS study explicitly used Sigma A8126, a mixture of methylacridinium
    chloride and proflavine. Its mammalian antiviral response and indirect cGAS engagement
    do not establish a direct target or antibacterial mechanism for this exact hydrochloride
    salt.
  snapshot_sha256: 85440cec099816ca627a4902dfb63bba9d68a739a78bffb3319160dbc47fd5cc
- evidence_id: mesh-boundary
  kind: authority
  reference: https://meshb.nlm.nih.gov/record/ui?ui=D000167
  locator: 'NLM 2026 MeSH descriptor: scope note and registry-related numbers'
  accessed_at: '2026-10-21T07:17:55Z'
  support: context_only
  summary: NLM defines Acriflavine as a mixture with 3,6-acridinediamine. Its nucleic-acid-intercalation
    description belongs to that descriptor, so a name-only search result cannot establish
    exact-salt activity.
- evidence_id: local-search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: Ignored-inclusive identifier, structure-key, registry and trypaflavine
    searches
  accessed_at: '2026-10-21T07:17:55Z'
  support: context_only
  summary: Raw and PATHS references match. Focused curation, reviews and historical-report
    searches found no target-specific override or prior prose review in those scopes.
    Broad generated and research-ledger hits are discovery context only.
  search_scope: prepare.py28 used rg --no-ignore --hidden over the worktree excluding
    .git/.venv. Exact CHEBI:74727,key,minted-ID searches covered raw,curation,reviews,PATHS;
    expanded 74727,trypaflavine,10597-46-3,6034-59-9 searches covered curation,reviews,reports/yaml_record_review
    excluding queue and large JSON files. Hidden and ignored files included.
- evidence_id: research-scope
  kind: search
  reference: Free primary literature and official identity sources
  locator: Exact salt/CAS/trypaflavine searches, followed by source-text inspection
  accessed_at: '2026-10-21T07:17:55Z'
  support: context_only
  summary: Bounded research identified a relevant 2020 antibacterial paper using the
    name acriflavine hydrochloride; its exact purchased preparation remains unverified.
    Mixture, selective-medium, staining and PTA-complex results cannot supply interchangeable
    potency. The historical 1929 JAMA lead returned 403.
  search_scope: Queries included exact CAS identifiers, trypaflavine hydrochloride,
    full salt name, antibacterial, DNA, intercalation and purified. Primary1970 PDF
    and 2016 XML were inspected; other search outputs were leads only. Follow-up inspected
    the 2020 H. pylori full author-uploaded text and PDF text. Browser screenshot
    output contained a placeholder without accessible pixels; direct PDF/figure retrieval
    returned 403, so no visual structure match is claimed.
- evidence_id: rubric
  kind: record_content
  reference: docs/CURATION.md
  locator: 'Native checklist: mechanism, targets, activity, producer, resistance,
    clinical status, datasets and graphs'
  accessed_at: '2026-10-21T07:17:55Z'
  support: supports
  summary: Optional empty fields are not schema defects. Mechanistic notes can retain
    narrowly supported experimental context without a protein-target claim or automatic
    antimicrobial-mode enum. Physical nucleic-acid association alone does not prove
    the organism-specific lethal pathway.
- evidence_id: validation
  kind: validation
  reference: just validate; just validate-strict
  locator: Isolated worktree003; scratch028-validation.tsv
  accessed_at: '2026-10-21T07:14:02Z'
  support: supports
  summary: Both focused commands exited0. LinkML reported no issues; strict scanned
    one target with zero ERROR rows.
  snapshot_sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
- evidence_id: h-pylori-lead
  kind: primary_source
  reference: PMID:33118020
  locator: DOI:10.1093/femsle/fnaa178; author-uploaded full text and PDF text at https://www.researchgate.net/profile/Inderjeet-Kaur-8/publication/347577605_Antibacterial_action_of_acriflavine_hydrochloride_for_eradication_of_the_gastric_pathogen_Helicobacter_pylori/links/607410324585150fe99f96bd/Antibacterial-action-of-acriflavine-hydrochloride-for-eradication-of-the-gastric-pathogen-Helicobacter-pylori.pdf;
    Introduction, Methods and Results; Figure 1 pixels not inspected
  accessed_at: '2026-10-21T07:24:49Z'
  support: context_only
  summary: The 2020 study reports ACF-HCl from Sigma-Aldrich, without a catalog or
    CAS identifier in inspected Methods. It distinguishes acriflavine mixtures in
    its introduction. Reported MICs are 2 micrograms/mL for H. pylori 26695 and 20
    micrograms/mL for E. coli W3110; clinical isolates used agar dilution. Membrane
    imaging, PI uptake and pull-down/proteomics provide cellular response and candidate-association
    evidence. The depicted salt composition and actual purchased preparation remain
    unresolved here, so these results are a concrete follow-up lead rather than verified
    CHEBI:74727 measurements or direct protein-binding proof.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact chloride.HCl composition
  outcome: supported
  summary: Official sources and structure recomputation agree. The three SMILES fragments
    encode the defined salt composition, not an arbitrary acriflavine/proflavine mixture.
    No incorrect-charge or wrong-salt finding is supported.
  target_ids:
  - CHEBI:74727
  evidence_ids:
  - record
  - owner
  - chebi
  - pubchem
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Antibacterial classification and hydrochloride parent
  outcome: supported
  summary: The adopted class and parent are source-supported; missing automatic intercalator
    mapping is intentional.
  target_ids:
  - CHEBI:74727
  evidence_ids:
  - chebi
  - config
- assessment_id: xref
  area: identity
  topic: Registry cross-references
  outcome: supported
  summary: Both CAS numbers are asserted by ChEBI and corroborated in the exact-key
    PubChem record. Direct independent CAS detail access remains limited. No narrower
    stoichiometric inference is drawn from a generic vendor label.
  target_ids:
  - CHEBI:74727
  evidence_ids:
  - chebi
  - pubchem
  - cas-access
- assessment_id: mechanism
  area: completeness
  topic: Qualified nucleic-acid interaction context
  outcome: concern
  summary: The inspected primary preparation and uncomplexed-dye controls provide
    a concrete curation opportunity. A bounded note can distinguish physical interaction
    from demonstrated antibacterial mechanism and from the separately prepared complex.
  target_ids:
  - CHEBI:74727
  evidence_ids:
  - record
  - primary-binding
  - rubric
- assessment_id: targets
  area: evidence
  topic: Direct antibacterial molecular target
  outcome: unknown
  summary: No native target is asserted. Biochemical nucleic-acid association merits
    assessment, but does not identify a bacterial protein target or establish the
    full antimicrobial causal chain.
  target_ids:
  - CHEBI:74727
  evidence_ids:
  - record
  - primary-binding
  - rubric
  - h-pylori-lead
- assessment_id: activity
  area: evidence
  topic: Organism- and assay-specific potency
  outcome: unknown
  summary: A relevant primary antibacterial study was located, but its reagent identity
    has not been resolved to this exact salt. Quantitative transfer remains withheld
    pending that mapping; this is not a claim that no assay literature exists.
  target_ids:
  - CHEBI:74727
  evidence_ids:
  - record
  - research-scope
  - mixture-primary
  - mesh-boundary
  - h-pylori-lead
- assessment_id: other
  area: scope
  topic: Producer, resistance, clinical, dataset and graph claims
  outcome: not_applicable
  summary: No native claims in these categories require correction. Human antiviral
    mixture experiments cannot populate this salt record. No biosynthetic producer,
    clinical approval, resistance determinant or causal edge is inferred.
  target_ids:
  - CHEBI:74727
  evidence_ids:
  - record
  - mixture-primary
  - rubric
- assessment_id: provenance
  area: provenance
  topic: Generated ownership and status
  outcome: supported
  summary: All seeded fields and history match their owners. Scientific annotations
    would need separate curator provenance; this review leaves native SEEDED unchanged.
  target_ids:
  - CHEBI:74727
  evidence_ids:
  - record
  - owner
  - rubric
- assessment_id: schema
  area: schema
  topic: Focused schema gates
  outcome: supported
  summary: Both focused validators pass.
  target_ids:
  - CHEBI:74727
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: chebi-74727-qualified-nucleic-acid-binding-context
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Primary binding evidence and an unresolved assay lead warrant scoped follow-up
  description: The matched historical preparation supports bounded biochemical context.
    A later antibacterial study is a concrete additional lead, but its exact preparation
    needs resolution before transfer. The seed makes no false mechanistic assertion;
    these are non-blocking evidence-specific curation opportunities.
  target_ids:
  - CHEBI:74727
  field_paths:
  - evidence
  - mode_of_action_notes
  - molecular_targets
  - activity_spectrum
  evidence_ids:
  - record
  - primary-binding
  - rubric
  - h-pylori-lead
  rule_id: native-review-checklist:Mode of action and Molecular targets
  native_severity: minor evidence-specific readiness gap
  normalization_reason: Specific inspected primary data warrant assessment; no blanket
    requirement to fill optional fields or infer bacterial synthesis inhibition is
    imposed.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/3-6-diamino-10-methylacridinium-chloride-hcl.yaml
    role: Curator-owned scientific annotations; use native validated writer and curation
      event
actions:
- action_id: A1
  description: Add a bounded mechanistic note or explicit curator disposition for
    the exact-salt biochemical evidence. Assess any nucleic-acid target representation
    against the assay scope. Keep uncomplexed dye, PTA complex and acriflavine mixtures
    separate, and leave antimicrobial mode unresolved unless further exact-compound
    evidence supports it.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:74727
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/3-6-diamino-10-methylacridinium-chloride-hcl.yaml
    role: Curator-owned scientific annotations; use native validated writer and curation
      event
  acceptance_checks:
  - Every added claim cites the exact preparation and uncomplexed-dye experiment,
    preserving cell-free conditions and nucleic-acid source.
  - No protein target, bacterial synthesis-inhibition enum, MIC or complete lethal
    causal chain is inferred from binding alone.
  - No cGAS, HIF, antiviral or mixture result is transferred by name similarity.
  - Use native validated writer/history and required focused, reproducibility and
    QC gates.
- action_id: A2
  description: Resolve the 2020 paper preparation using its structure figure and a
    product identifier or equivalent source evidence before attaching its activity
    to this salt.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:74727
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/3-6-diamino-10-methylacridinium-chloride-hcl.yaml
    role: Curator-owned scientific annotations; use native validated writer and curation
      event
  acceptance_checks:
  - Preserve tested material identity, strain and assay conditions. Do not silently
    transfer mixture or single-chloride results.
  - Keep microscopy/permeability responses and pull-down candidates distinct from
    direct binding or proven primary lethal targets.
limitations:
- Direct CAS Common Chemistry detail access failed; official ChEBI and attributed
  PubChem registry data were inspected.
- The primary 1970 paper was inspected as a scanned free copy, including visual checks
  of reagent identification and uncomplexed-dye Figure4. Its observations are biochemical;
  the review does not establish exact-salt bacterial killing mechanism or potency.
- Mixture-specific host-response experiments were inspected only to bound applicability.
  Bounded research does not establish global absence of additional exact-salt studies.
- The newly located H. pylori study was read as full text and PDF text, but its structure
  image and reagent catalog identity were not independently verified. Exact-salt applicability
  remains unresolved.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Capture preceded judgment; all original hashes and Git revision were retained when
  provenance inputs were expanded.
- Local searches used for absence statements included ignored and hidden files.
- The native record remains SEEDED; the finding concerns an inspected source rather
  than absent optional fields in general.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:74727
- https://pubchem.ncbi.nlm.nih.gov/compound/15558347
- https://doi.org/10.1083/jcb.47.2.500
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5224509/
- https://pubmed.ncbi.nlm.nih.gov/33118020/
- https://www.researchgate.net/profile/Inderjeet-Kaur-8/publication/347577605_Antibacterial_action_of_acriflavine_hydrochloride_for_eradication_of_the_gastric_pathogen_Helicobacter_pylori/links/607410324585150fe99f96bd/Antibacterial-action-of-acriflavine-hydrochloride-for-eradication-of-the-gastric-pathogen-Helicobacter-pylori.pdf
tags:
- antibacterial
- acridinium
- hydrochloride
- seeded
- mixture-boundary
```
