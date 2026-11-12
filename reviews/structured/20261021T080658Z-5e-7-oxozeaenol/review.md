# 5E-7-oxozeaenol: false exact synonym and unsupported antibacterial source claim

- Review: 20261021T080658Z-5e-7-oxozeaenol
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T07:56:58Z
- Finished UTC: 2026-10-21T08:06:58Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact E-isomer structure and focused validators are coherent, but two major source-derived defects remain. LL-Z1640-1 is a different molecule in the source-cited primary paper, and that paper reports no antibacterial activity for the exact E compound in its assay. Fungal isolation, cytotoxicity and a human-cell NF-kappaB response are supported; none supplies antibacterial target proof.

## Scope And Provenance

Entire exact record and maintained source ownership; identity and all asserted fields, sole adopted publication and bounded exact-compound follow-up.

Selection: Queue index055, CHEBI:67558 at the locked native path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:67558 | data/antibiotics/antibacterial/5e-7-oxozeaenol.yaml | generated | 5E-7-oxozeaenol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:67558 | Focused LinkML validation exited0. |
| strict | passed | True | CHEBI:67558 | Focused closed validation scanned one file with zero ERROR rows. |
| chemistry | passed | False | CHEBI:67558 | SMILES and InChI parse to the same full stereochemical key; all calculated properties and source mint agree. |
| adapter-initial | failed | False | CHEBI:67558 | Initial public dataset request failed with DNS error in restricted network. |
| adapter-retry | passed | False | CHEBI:67558 | Authorized read-only retry retrieved inventory. No human-cell NF-kappaB/TAK1 or MSX63935 fungal dataset is covered; no matching search or component summary applies. |
| reaxys | unavailable | False | CHEBI:67558 | Reaxys5452473 is corroborated as the ChEBI assertion but was not independently inspected through a free registry. |
| additional-fulltext | unavailable | False | CHEBI:67558 | The2015 TAK1 paper was retrieved at complete official abstract level. PMC challenge, EuropePMC XML500 and author-PDF timeout prevented exact assay-table inspection; its E-isomer potency or covalent mechanism is not adopted. |
| Authoritative full QC | failed | True | CHEBI:67558 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:67558 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:67558 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:67558 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:67558 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:67558 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:67558 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:67558 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:67558 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact E-isomer chemical representation

identity: supported. Targets: CHEBI:67558.

Native label and structure denote the same individual E molecule; charge, masses and source mint agree.

### LL-Z1640-1 exact synonym

identity: concern. Targets: CHEBI:67558.

Primary structure and formula show a different molecule; this is a major false-equivalence claim.

### Structural parents and registry xref

grounding: supported. Targets: CHEBI:67558.

All five parent labels fit the molecular features. Reaxys remains a source assertion with free-access limitations.

### Antibacterial definition and role

evidence: concern. Targets: CHEBI:67558.

The source-cited exact experiment is negative. Bounded research did not resolve the positive source assertion; do not equate this with universal inactivity.

### Cytotoxicity and NF-kappaB scope

evidence: supported. Targets: CHEBI:67558.

Exact host-cell effects support qualified definition clauses without establishing microbial target engagement.

### Fungal origin

evidence: supported. Targets: CHEBI:67558.

Isolation from the cultured fungus supports the broad source statement.

### Optional activity, target, resistance and graph objects

completeness: not_applicable. Targets: CHEBI:67558.

No mandatory-field or missing-object defect is claimed; the correction concerns explicit current assertions.

### Generated source reproduction and history

ownership: supported. Targets: CHEBI:67558.

Source row and native record agree; inherited defects require maintained input/config/decision fixes. All13 hashes unchanged.

### Native focused checks

schema: supported. Targets: CHEBI:67558.

Focused schema and strict gates pass despite semantic findings.

## Findings

### F1: Remove the false LL-Z1640-1 exact synonym

major / open / confirmed; issue key: chebi-67558-false-ll-z1640-1-exact-synonym.

LL-Z1640-1 is primary-paper compound6, C19H24O7, while the native exact E structure is compound4, C19H22O7. The source-inherited exact synonym asserts a different molecule.

### F2: Resolve the antibacterial assertion against the source-cited negative assay

major / open / confirmed; issue key: chebi-67558-antibacterial-source-support-conflict.

The only adopted primary citation reports exact compound4 inactive in its four-bacterium assay. This is a material support conflict in explicit definition/role claims, not an optional evidence-field omission and not proof that every possible antibacterial assay is negative.

## Recommended Actions And Acceptance Checks

### A1

Exclude LL-Z1640-1 for this ChEBI concept through the maintained source correction or concept-scoped synonym_exclusions, preserving the valid E structure and systematic names.

- Compare the primary drawings/formulas for4 and6 and retain their different identities.
- Re-extract if a source transformation changes and reseed the exact concept; verify the false synonym cannot return on regeneration.
- Run focused schema/strict and full required corpus gates; do not silently rewrite generated YAML.

### A2

Adjudicate the exact E antibacterial claim using any additional primary evidence before retaining the role; if no valid in-scope antimicrobial support can be established, propose a reproducible exclusion decision.

- Retain the2011 negative assay with original conditions and do not relabel its diffusion endpoint as standardized broth MIC.
- Keep prior crude-extract MRSA activity, Z-isomer activity and host NF-kappaB/TAK1 effects separate from E antibacterial evidence.
- If retaining any positive role, cite an inspected exact-E primary assay with organism, method, units and scope; otherwise implement an authorized source/decision correction or conditional exclusion rather than asserting universal inactivity.
- Use the native validated writer/history for curator-owned evidence or discussion and reseed for generated-field changes; run verify-corpus and required validation gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/5e-7-oxozeaenol.yaml; Complete native YAML, read after initial inspect. | supports | CHEBI:67558 is SEEDED/EXACT, ANTIBACTERIAL; three exact synonyms include LL-Z1640-1. Five structural parents, antibacterial role, one Reaxys xref, neutral E-isomer chemistry, one source concept and three seed/reseed events are present. Optional evidence, activity_spectrum, targets, producer, resistance and causal graph objects are absent. |
| source | data/raw/chebi_antimicrobials.tsv; Row1679, complete055-raw.json; conf/sources.yaml chebi and synonym_exclusions; extractor176–339, seeder790–809 and1483–1570; raw MANIFEST and PATHS. | supports | The native record faithfully reproduces the maintained source, including false synonym and unqualified antibacterial claim. Source citation PMID21513293 is a lead deliberately not automatically promoted to claim evidence. No mechanism role is imported. Source version2026-08-30 and three history events are coherent. All13 initial input hashes remain unchanged. |
| identity | https://www.ebi.ac.uk/chebi/CHEBI:67558; Complete official page055-chebi.html/txt; PubChem CID9799061 properties and synonyms055-pubchem*.json. | supports | ChEBI and PubChem exact structures agree with the native neutral C19H22O7, InChI/key NEQZWEXWOFPKOT-ULSULSEOSA-N and two E double bonds. Native systematic names correspond to this structure. ChEBI parents2468 secondary alpha-hydroxy ketone,25106 macrolide,33853 phenols,35618 aromatic ether and35681 secondary alcohol are strictly broader. Role33282 is antibacterial agent. Reaxys5452473 is source-asserted only. Current ChEBI still lists LL-Z1640-1, but agreement among imported labels cannot override the contradictory primary identity evidence. PubChem synonyms contain additional sibling labels and were not treated as authoritative equivalence. |
| chemistry | Independent RDKit calculation; 055-chemistry.json/log; chem005.py source inspected. | supports | Both representations parse to the same full key, formulaC19H22O7, charge0, one fragment, mass362.378 and exact mass362.136553044, with three S stereocentres. SHA256 source mint antibioticmech:chebi-0e9a5203bc matches. This confirms internal E identity but cannot validate a wrong trivial synonym. |
| paper-identity | PMID:21513293; DOI:10.1021/np200062x; complete PMC article055-2011.html/txt and visually inspected055-2011-structures.jpg; compound characterization4 and6. | refutes | The paper identifies 5E-7-oxozeaenol as compound4, C19H22O7, and LL-Z1640-1 as compound6, C19H24O7. The drawing shows4 with the E enone and6 with that alkene reduced. Their different formulas and structures refute exact synonymy independently of the paper’s discussion of stereochemical uncertainty for6. The E and Z entities are separately drawn and characterized. |
| paper-antibacterial | PMID:21513293; Results and Discussion final assay paragraph; Experimental Antimicrobial Assay in complete055-2011.html/txt. | refutes | Exact compounds1–6, including E compound4, showed no activity at500µg/mL against E.coli, S.aureus, M.smegmatis and B.subtilis. Methods describe agar surface diffusion,10µL methanol application, LB or Middlebrook7H9 with1% glycerol and1.5% agar, overnight37°C. Authors report MIC&gt;500µg/mL in Results, but this is not demonstrated standardized broth MIC; strains are unspecified. Prior crude-culture MRSA activity cannot be assigned to purified4. These data fail to support the source’s positive antibacterial claim; they do not prove universal inactivity. |
| paper-host | PMID:21513293; Tables2–3 and cytotoxicity/NF-kappaB methods; complete055-2011.html/txt. | supports | Compound4 reduces human tumor-cell proliferation after72h, with IC50 values4.9,1.2,5.6,4.4,5.5µM across the named panel. Its NF-kappaB p65 endpoint is11.5µM in treated HeLa nuclear extracts. This supports the definition’s cytotoxic and NF-kappaB inhibitory wording as human-cell observations, not direct p65 binding or an antibacterial mechanism. The0.24µM result and cited historical TAK1 potency belong to Z compound5. Broad scaffold HSP90/kinase statements are not exact E-target measurements. |
| paper-source | PMID:21513293; Producing Organism and Fermentation; Extraction and Isolation. | supports | The study grows MSX63935 in defined culture conditions and isolates compound4 from the resulting fermented material. This supports fungal origin in the definition. The strain is only related to Phoma by the authors’ sequence comparison, not conclusively assigned to a species. Optional producer curation would require its own exact strain/taxon evidence; it is not necessary for the current broad origin statement. |
| additional | PMID:26481152; DOI:10.1016/j.bmc.2015.09.037; complete official abstract055-2015-epmc.json. | context_only | The primary follow-up studies TAK1 inhibition in isolated and semisynthetic analogues. The accessible abstract does not establish exact E antibacterial activity or the exact E assay result. Vendor E-potency and covalent-target claims remain leads because the relevant primary table was not retrieved. |
| adapter | https://imodulondb.org/api/datasets; 055-imodulondb-datasets.txt and055-imodulondb-datasets-retry.txt, actual attempts. | context_only | The first request failed DNS; the authorized retry returned the covered dataset list. No human-cell NF-kappaB/TAK1 or fungal MSX63935 context is covered. This makes a component search inapplicable, not negative evidence for pathway biology. |
| search | CultureBotAI/AntibioticMech; 055-local-hits.txt and055-maintained-search.txt; free exact-name/key/CAS publication discovery. | context_only | Ignored-inclusive focused maintained-input search found no existing decision, curated overlay or structured review for this target. Exact searches returned the2011 study, host-kinase follow-up and vendors repeating the2011 assay list; no inspected positive exact E antibacterial primary result was found. Searches do not prove global evidence absence. |
| rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Identity/equivalence, classification, evidence and optional fields; CURATION/HARMONIZATION. | supports | An exact synonym must denote the same structure. Antibacterial support must concern the exact compound and assay. Optional absent targets are not defects, and host response/scaffold activity cannot be transferred. Generated corrections must survive reseeding; no automatic REVIEWED promotion. |
| validation | Documented focused validators; 055-focused-results.json and055-schema.log/055-strict.log/055-strict.tsv. | supports | Actual schema, strict and independent chemistry exits are0. Shared corpus gate results are documented separately in the final bundle. |

## Limits And Additional Notes

- Reaxys5452473 was not independently inspected. PubChem sibling-name contamination was treated cautiously and is not imported into the native record.
- The2011 full primary text and structure figure were inspected; the author-PDF binary request timed out but PMC HTML and its image were obtained. Supporting NMR spectra were not independently reinterpreted.
- The2015 TAK1 follow-up was inspected at official-abstract level only; exact E potency, selectivity and covalent binding are not asserted from vendor summaries.
- Bounded searches do not prove no other antimicrobial evidence exists. Exclusion remains conditional on evidence adjudication. The negative paper assay does not support clinical resistance or universal inactivity.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Coordinator independently inspected the original compound drawings and confirmed that compound4 contains the enone alkene missing from compound6; the exact synonym cannot denote both structures.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T080658Z-5e-7-oxozeaenol
kind: record
repository: CultureBotAI/AntibioticMech
title: '5E-7-oxozeaenol: false exact synonym and unsupported antibacterial source
  claim'
started_at: '2026-10-21T07:56:58Z'
finished_at: '2026-10-21T08:06:58Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author the record. Captured target and maintained
    inputs before assessment, then read the complete native record, source row and
    transforms, current official identity records, and the cited original study including
    its structure figure.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The exact E-isomer structure and focused validators are coherent, but two
  major source-derived defects remain. LL-Z1640-1 is a different molecule in the source-cited
  primary paper, and that paper reports no antibacterial activity for the exact E
  compound in its assay. Fungal isolation, cytotoxicity and a human-cell NF-kappaB
  response are supported; none supplies antibacterial target proof.
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
  - path: data/antibiotics/antibacterial/5e-7-oxozeaenol.yaml
    sha256: 6866486b2e0a694b3bb350e47f240951b7018ae08d150dc2d3a20b93ef0d0607
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
- target_id: CHEBI:67558
  path: data/antibiotics/antibacterial/5e-7-oxozeaenol.yaml
  label: 5E-7-oxozeaenol
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
  description: Entire exact record and maintained source ownership; identity and all
    asserted fields, sole adopted publication and bounded exact-compound follow-up.
  selection: Queue index055, CHEBI:67558 at the locked native path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:67558
  exclusions:
  - target: 5Z-7-oxozeaenol, LL-Z1640-1, other resorcylic acid lactones and crude
      fungal extracts
    reason: Different entities; activity and mechanisms are not transferred to the
      exact E compound.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Focused LinkML validation exited0.
  target_ids:
  - CHEBI:67558
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/5e-7-oxozeaenol.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Focused closed validation scanned one file with zero ERROR rows.
  target_ids:
  - CHEBI:67558
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/5e-7-oxozeaenol.yaml --out /private/tmp/am-review-session/055-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: SMILES and InChI parse to the same full stereochemical key; all calculated
    properties and source mint agree.
  target_ids:
  - CHEBI:67558
  evidence_ids:
  - chemistry
  command: .venv/bin/python /private/tmp/am-review-session/chem005.py 55
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter-initial
  name: adapter-initial
  status: failed
  required: false
  summary: Initial public dataset request failed with DNS error in restricted network.
  target_ids:
  - CHEBI:67558
  evidence_ids:
  - adapter
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 datasets
  exit_code: 2
  expected_exit_code: 0
- check_id: adapter-retry
  name: adapter-retry
  status: passed
  required: false
  summary: Authorized read-only retry retrieved inventory. No human-cell NF-kappaB/TAK1
    or MSX63935 fungal dataset is covered; no matching search or component summary
    applies.
  target_ids:
  - CHEBI:67558
  evidence_ids:
  - adapter
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache PYTHONDONTWRITEBYTECODE=1
    uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb --timeout 15 datasets
  exit_code: 0
  expected_exit_code: 0
- check_id: reaxys
  name: reaxys
  status: unavailable
  required: false
  summary: Reaxys5452473 is corroborated as the ChEBI assertion but was not independently
    inspected through a free registry.
  target_ids:
  - CHEBI:67558
  evidence_ids:
  - identity
- check_id: additional-fulltext
  name: additional-fulltext
  status: unavailable
  required: false
  summary: The2015 TAK1 paper was retrieved at complete official abstract level. PMC
    challenge, EuropePMC XML500 and author-PDF timeout prevented exact assay-table
    inspection; its E-isomer potency or covalent mechanism is not adopted.
  target_ids:
  - CHEBI:67558
  evidence_ids:
  - additional
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
  - CHEBI:67558
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
  - CHEBI:67558
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
  - CHEBI:67558
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
  - CHEBI:67558
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
  - CHEBI:67558
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
  - CHEBI:67558
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
  - CHEBI:67558
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
  - CHEBI:67558
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
  - CHEBI:67558
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/5e-7-oxozeaenol.yaml
  locator: Complete native YAML, read after initial inspect.
  accessed_at: '2026-10-21T08:01:29Z'
  support: supports
  summary: CHEBI:67558 is SEEDED/EXACT, ANTIBACTERIAL; three exact synonyms include
    LL-Z1640-1. Five structural parents, antibacterial role, one Reaxys xref, neutral
    E-isomer chemistry, one source concept and three seed/reseed events are present.
    Optional evidence, activity_spectrum, targets, producer, resistance and causal
    graph objects are absent.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Row1679, complete055-raw.json; conf/sources.yaml chebi and synonym_exclusions;
    extractor176–339, seeder790–809 and1483–1570; raw MANIFEST and PATHS.
  accessed_at: '2026-10-21T08:01:29Z'
  support: supports
  summary: The native record faithfully reproduces the maintained source, including
    false synonym and unqualified antibacterial claim. Source citation PMID21513293
    is a lead deliberately not automatically promoted to claim evidence. No mechanism
    role is imported. Source version2026-08-30 and three history events are coherent.
    All13 initial input hashes remain unchanged.
  snapshot_sha256: c70d7b21c186f75fe93e72b514912a44c4faad90860da51a3a2dca9e691e6345
- evidence_id: identity
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:67558
  locator: Complete official page055-chebi.html/txt; PubChem CID9799061 properties
    and synonyms055-pubchem*.json.
  accessed_at: '2026-10-21T08:01:29Z'
  support: supports
  summary: ChEBI and PubChem exact structures agree with the native neutral C19H22O7,
    InChI/key NEQZWEXWOFPKOT-ULSULSEOSA-N and two E double bonds. Native systematic
    names correspond to this structure. ChEBI parents2468 secondary alpha-hydroxy
    ketone,25106 macrolide,33853 phenols,35618 aromatic ether and35681 secondary alcohol
    are strictly broader. Role33282 is antibacterial agent. Reaxys5452473 is source-asserted
    only. Current ChEBI still lists LL-Z1640-1, but agreement among imported labels
    cannot override the contradictory primary identity evidence. PubChem synonyms
    contain additional sibling labels and were not treated as authoritative equivalence.
  snapshot_sha256: 024ac3856dae28ef2a41f31d8b6707fe2041c2b6e1c9501cf2eb7f4495af05cb
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit calculation
  locator: 055-chemistry.json/log; chem005.py source inspected.
  accessed_at: '2026-10-21T08:01:29Z'
  support: supports
  summary: Both representations parse to the same full key, formulaC19H22O7, charge0,
    one fragment, mass362.378 and exact mass362.136553044, with three S stereocentres.
    SHA256 source mint antibioticmech:chebi-0e9a5203bc matches. This confirms internal
    E identity but cannot validate a wrong trivial synonym.
  snapshot_sha256: 9ba80607ae685155d5129d6b22eeafa0aea9d6949841cb032d1f55e9fcb9a58f
- evidence_id: paper-identity
  kind: primary_source
  reference: PMID:21513293
  locator: DOI:10.1021/np200062x; complete PMC article055-2011.html/txt and visually
    inspected055-2011-structures.jpg; compound characterization4 and6.
  accessed_at: '2026-10-21T08:01:29Z'
  support: refutes
  summary: The paper identifies 5E-7-oxozeaenol as compound4, C19H22O7, and LL-Z1640-1
    as compound6, C19H24O7. The drawing shows4 with the E enone and6 with that alkene
    reduced. Their different formulas and structures refute exact synonymy independently
    of the paper’s discussion of stereochemical uncertainty for6. The E and Z entities
    are separately drawn and characterized.
  snapshot_sha256: f591e80913f8c902222e2defc1774fc7a679c0b546a7d2c42b02b5e4690f4db1
- evidence_id: paper-antibacterial
  kind: primary_source
  reference: PMID:21513293
  locator: Results and Discussion final assay paragraph; Experimental Antimicrobial
    Assay in complete055-2011.html/txt.
  accessed_at: '2026-10-21T08:01:29Z'
  support: refutes
  summary: Exact compounds1–6, including E compound4, showed no activity at500µg/mL
    against E.coli, S.aureus, M.smegmatis and B.subtilis. Methods describe agar surface
    diffusion,10µL methanol application, LB or Middlebrook7H9 with1% glycerol and1.5%
    agar, overnight37°C. Authors report MIC>500µg/mL in Results, but this is not demonstrated
    standardized broth MIC; strains are unspecified. Prior crude-culture MRSA activity
    cannot be assigned to purified4. These data fail to support the source’s positive
    antibacterial claim; they do not prove universal inactivity.
  snapshot_sha256: f591e80913f8c902222e2defc1774fc7a679c0b546a7d2c42b02b5e4690f4db1
- evidence_id: paper-host
  kind: primary_source
  reference: PMID:21513293
  locator: Tables2–3 and cytotoxicity/NF-kappaB methods; complete055-2011.html/txt.
  accessed_at: '2026-10-21T08:01:29Z'
  support: supports
  summary: Compound4 reduces human tumor-cell proliferation after72h, with IC50 values4.9,1.2,5.6,4.4,5.5µM
    across the named panel. Its NF-kappaB p65 endpoint is11.5µM in treated HeLa nuclear
    extracts. This supports the definition’s cytotoxic and NF-kappaB inhibitory wording
    as human-cell observations, not direct p65 binding or an antibacterial mechanism.
    The0.24µM result and cited historical TAK1 potency belong to Z compound5. Broad
    scaffold HSP90/kinase statements are not exact E-target measurements.
  snapshot_sha256: f591e80913f8c902222e2defc1774fc7a679c0b546a7d2c42b02b5e4690f4db1
- evidence_id: paper-source
  kind: primary_source
  reference: PMID:21513293
  locator: Producing Organism and Fermentation; Extraction and Isolation.
  accessed_at: '2026-10-21T08:01:29Z'
  support: supports
  summary: The study grows MSX63935 in defined culture conditions and isolates compound4
    from the resulting fermented material. This supports fungal origin in the definition.
    The strain is only related to Phoma by the authors’ sequence comparison, not conclusively
    assigned to a species. Optional producer curation would require its own exact
    strain/taxon evidence; it is not necessary for the current broad origin statement.
  snapshot_sha256: f591e80913f8c902222e2defc1774fc7a679c0b546a7d2c42b02b5e4690f4db1
- evidence_id: additional
  kind: primary_source
  reference: PMID:26481152
  locator: DOI:10.1016/j.bmc.2015.09.037; complete official abstract055-2015-epmc.json.
  accessed_at: '2026-10-21T08:01:29Z'
  support: context_only
  summary: The primary follow-up studies TAK1 inhibition in isolated and semisynthetic
    analogues. The accessible abstract does not establish exact E antibacterial activity
    or the exact E assay result. Vendor E-potency and covalent-target claims remain
    leads because the relevant primary table was not retrieved.
  snapshot_sha256: 86b579d9ac54462e9c562db2650e0f18f745dbc35ef04afdaa172ee33b85b044
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: 055-imodulondb-datasets.txt and055-imodulondb-datasets-retry.txt, actual
    attempts.
  accessed_at: '2026-10-21T08:01:29Z'
  support: context_only
  summary: The first request failed DNS; the authorized retry returned the covered
    dataset list. No human-cell NF-kappaB/TAK1 or fungal MSX63935 context is covered.
    This makes a component search inapplicable, not negative evidence for pathway
    biology.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: 055-local-hits.txt and055-maintained-search.txt; free exact-name/key/CAS
    publication discovery.
  accessed_at: '2026-10-21T08:01:29Z'
  support: context_only
  summary: Ignored-inclusive focused maintained-input search found no existing decision,
    curated overlay or structured review for this target. Exact searches returned
    the2011 study, host-kinase follow-up and vendors repeating the2011 assay list;
    no inspected positive exact E antibacterial primary result was found. Searches
    do not prove global evidence absence.
  search_scope: rg --no-ignore --hidden for identifier,label,slug across worktree006
    excluding.git/.venv; focused CHEBI:67558,NEQZWEXWOFPKOT-ULSULSEOSA-N,5e-7-oxozeaenol,LL-Z1640-1
    across curation,reviews,reports/yaml_record_review,conf excluding queue. Web queries
    exact 5E-7-oxozeaenol with antibacterial, antimicrobial, minimum inhibitory; full
    key plus antimicrobial;1198574-97-8 plus antibacterial primary; exact E name with
    TAK1. Official PMC, EuropePMC, ChEBI and PubChem texts inspected. Vendor/review
    hits are leads only.
- evidence_id: rubric
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Identity/equivalence, classification, evidence and optional fields; CURATION/HARMONIZATION.
  accessed_at: '2026-10-21T08:01:29Z'
  support: supports
  summary: An exact synonym must denote the same structure. Antibacterial support
    must concern the exact compound and assay. Optional absent targets are not defects,
    and host response/scaffold activity cannot be transferred. Generated corrections
    must survive reseeding; no automatic REVIEWED promotion.
- evidence_id: validation
  kind: validation
  reference: Documented focused validators
  locator: 055-focused-results.json and055-schema.log/055-strict.log/055-strict.tsv.
  accessed_at: '2026-10-21T08:01:29Z'
  support: supports
  summary: Actual schema, strict and independent chemistry exits are0. Shared corpus
    gate results are documented separately in the final bundle.
  snapshot_sha256: 7e5d89c22eafd8609e9a50d5262c11bce040bb765a67b204286f80e1b3b804a6
assessments:
- assessment_id: chemistry
  area: identity
  topic: Exact E-isomer chemical representation
  outcome: supported
  summary: Native label and structure denote the same individual E molecule; charge,
    masses and source mint agree.
  target_ids:
  - CHEBI:67558
  evidence_ids:
  - identity
  - chemistry
  - paper-identity
- assessment_id: synonym
  area: identity
  topic: LL-Z1640-1 exact synonym
  outcome: concern
  summary: Primary structure and formula show a different molecule; this is a major
    false-equivalence claim.
  target_ids:
  - CHEBI:67558
  evidence_ids:
  - record
  - source
  - paper-identity
- assessment_id: parents
  area: grounding
  topic: Structural parents and registry xref
  outcome: supported
  summary: All five parent labels fit the molecular features. Reaxys remains a source
    assertion with free-access limitations.
  target_ids:
  - CHEBI:67558
  evidence_ids:
  - identity
  - chemistry
- assessment_id: activity
  area: evidence
  topic: Antibacterial definition and role
  outcome: concern
  summary: The source-cited exact experiment is negative. Bounded research did not
    resolve the positive source assertion; do not equate this with universal inactivity.
  target_ids:
  - CHEBI:67558
  evidence_ids:
  - paper-antibacterial
  - search
  - source
- assessment_id: host
  area: evidence
  topic: Cytotoxicity and NF-kappaB scope
  outcome: supported
  summary: Exact host-cell effects support qualified definition clauses without establishing
    microbial target engagement.
  target_ids:
  - CHEBI:67558
  evidence_ids:
  - paper-host
  - additional
  - adapter
- assessment_id: origin
  area: evidence
  topic: Fungal origin
  outcome: supported
  summary: Isolation from the cultured fungus supports the broad source statement.
  target_ids:
  - CHEBI:67558
  evidence_ids:
  - paper-source
  - identity
- assessment_id: optional
  area: completeness
  topic: Optional activity, target, resistance and graph objects
  outcome: not_applicable
  summary: No mandatory-field or missing-object defect is claimed; the correction
    concerns explicit current assertions.
  target_ids:
  - CHEBI:67558
  evidence_ids:
  - record
  - rubric
- assessment_id: ownership
  area: ownership
  topic: Generated source reproduction and history
  outcome: supported
  summary: Source row and native record agree; inherited defects require maintained
    input/config/decision fixes. All13 hashes unchanged.
  target_ids:
  - CHEBI:67558
  evidence_ids:
  - source
  - rubric
- assessment_id: validation
  area: schema
  topic: Native focused checks
  outcome: supported
  summary: Focused schema and strict gates pass despite semantic findings.
  target_ids:
  - CHEBI:67558
  evidence_ids:
  - validation
  - chemistry
findings:
- finding_id: F1
  issue_key: chebi-67558-false-ll-z1640-1-exact-synonym
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Remove the false LL-Z1640-1 exact synonym
  description: LL-Z1640-1 is primary-paper compound6, C19H24O7, while the native exact
    E structure is compound4, C19H22O7. The source-inherited exact synonym asserts
    a different molecule.
  target_ids:
  - CHEBI:67558
  field_paths:
  - synonyms[2]
  evidence_ids:
  - paper-identity
  - record
  - source
  rule_id: 'native-review-checklist: Identity/Equivalence'
  native_severity: major false equivalence
  normalization_reason: The native core identity remains recoverable, but an explicit
    assertion is materially wrong or unsupported; deterministic validity does not
    settle the scientific claim.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI assertions and source citation lead
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction and inventory reproduction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition, synonym and role owner
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Concept-scoped synonym_exclusions
- finding_id: F2
  issue_key: chebi-67558-antibacterial-source-support-conflict
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Resolve the antibacterial assertion against the source-cited negative assay
  description: The only adopted primary citation reports exact compound4 inactive
    in its four-bacterium assay. This is a material support conflict in explicit definition/role
    claims, not an optional evidence-field omission and not proof that every possible
    antibacterial assay is negative.
  target_ids:
  - CHEBI:67558
  field_paths:
  - definition
  - activity_roles
  - antimicrobial_class
  evidence_ids:
  - paper-antibacterial
  - search
  - source
  rule_id: 'native-review-checklist: Classification/Evidence'
  native_severity: major unsupported positive activity assertion
  normalization_reason: The native core identity remains recoverable, but an explicit
    assertion is materially wrong or unsupported; deterministic validity does not
    settle the scientific claim.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI assertions and source citation lead
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction and inventory reproduction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition, synonym and role owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Evidence-backed scope or exclusion adjudication
actions:
- action_id: A1
  description: Exclude LL-Z1640-1 for this ChEBI concept through the maintained source
    correction or concept-scoped synonym_exclusions, preserving the valid E structure
    and systematic names.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:67558
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI assertions and source citation lead
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction and inventory reproduction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition, synonym and role owner
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Concept-scoped synonym_exclusions
  acceptance_checks:
  - Compare the primary drawings/formulas for4 and6 and retain their different identities.
  - Re-extract if a source transformation changes and reseed the exact concept; verify
    the false synonym cannot return on regeneration.
  - Run focused schema/strict and full required corpus gates; do not silently rewrite
    generated YAML.
- action_id: A2
  description: Adjudicate the exact E antibacterial claim using any additional primary
    evidence before retaining the role; if no valid in-scope antimicrobial support
    can be established, propose a reproducible exclusion decision.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:67558
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted ChEBI assertions and source citation lead
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source extraction and inventory reproduction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated definition, synonym and role owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Evidence-backed scope or exclusion adjudication
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/5e-7-oxozeaenol.yaml
    role: Curator-owned claim-level evidence or discussion through write_validated_antibiotic
      and curation history
  acceptance_checks:
  - Retain the2011 negative assay with original conditions and do not relabel its
    diffusion endpoint as standardized broth MIC.
  - Keep prior crude-extract MRSA activity, Z-isomer activity and host NF-kappaB/TAK1
    effects separate from E antibacterial evidence.
  - If retaining any positive role, cite an inspected exact-E primary assay with organism,
    method, units and scope; otherwise implement an authorized source/decision correction
    or conditional exclusion rather than asserting universal inactivity.
  - Use the native validated writer/history for curator-owned evidence or discussion
    and reseed for generated-field changes; run verify-corpus and required validation
    gates.
limitations:
- Reaxys5452473 was not independently inspected. PubChem sibling-name contamination
  was treated cautiously and is not imported into the native record.
- The2011 full primary text and structure figure were inspected; the author-PDF binary
  request timed out but PMC HTML and its image were obtained. Supporting NMR spectra
  were not independently reinterpreted.
- The2015 TAK1 follow-up was inspected at official-abstract level only; exact E potency,
  selectivity and covalent binding are not asserted from vendor summaries.
- Bounded searches do not prove no other antimicrobial evidence exists. Exclusion
  remains conditional on evidence adjudication. The negative paper assay does not
  support clinical resistance or universal inactivity.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Coordinator independently inspected the original compound drawings and confirmed
  that compound4 contains the enone alkene missing from compound6; the exact synonym
  cannot denote both structures.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
