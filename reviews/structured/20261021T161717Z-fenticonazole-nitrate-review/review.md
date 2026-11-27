# Fenticonazole nitrate: exact salt and both antimicrobial roles supported

- Review: 20261021T161717Z-fenticonazole-nitrate-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T15:56:41Z
- Finished UTC: 2026-10-21T16:17:17Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The entire seeded record is consistent with its ChEBI source and exact nitrate identity. Independent current-authority encodings agree, and inspected primary studies support antifungal and antibacterial activity. No confirmed corrective defect was identified. Direct compound-specific target validation and some original full texts remain outside the attained evidence depth; the seeded mode is not promoted to a direct binding claim. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 437; one exact complete record. All thirteen initial input hashes were verified before assessment and retained unchanged. The actual maintained source is the captured ChEBI inventory.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:83606 | data/antibiotics/antibacterial/fenticonazole-nitrate.yaml | generated | fenticonazole nitrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema verification | passed | True | CHEBI:83606 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:83606 | Actual focused execution exited 0. |
| Focused chemistry verification | failed | False | CHEBI:83606 | The optional helper exited 1 because it compared the native dot-component formula C24H20Cl2N2OS.HNO3 literally with RDKit flattened C24H21Cl2N3O4S. All encodings, charge, masses and source mint agree. A separate element-count and authority-graph check resolves this notation difference; the original failed execution is retained. |
| Independent authority graph and normalized element-count comparison | passed | False | CHEBI:83606 | Native SMILES/InChI, official ChEBI molfile, KEGG molfile and CAS-resolved PubChem SMILES all reproduce the complete key, formula element counts, neutral charge, two components and masses. |
| Authoritative full QC | failed | True | CHEBI:83606 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:83606 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:83606 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:83606 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:83606 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:83606 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:83606 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:83606 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:83606 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact nitrate form, synonyms and chemical properties

identity: supported. Targets: CHEBI:83606.

The complete current graphs, full key, component counts, normalized formula and masses agree. The definition explicitly identifies the racemate; the stored representation does not purport to distinguish the two enantiomers. The broader racemate parent and properly typed product/document associations preserve their intended scope.

### Filing class, retained roles and clinical-use definition

evidence: supported. Targets: CHEBI:83606.

Both antibacterial and antifungal roles have exact-form support. Priority ANTIBACTERIAL filing is therefore not a contradiction, and the product authority supports the vaginal-candidiasis treatment wording. Seeded cross-activity notes are cautious rather than a confirmed incorrect assertion.

### Seeded sterol-pathway mode and host-shared scope

evidence: unknown. Targets: CHEBI:83606.

The native mode and scope are reproducible qualified database assertions. Direct compound-specific sterol-enzyme inhibition was not independently established from an original biochemical experiment at this review depth. This remains an evidence limit, not proof that the mode is false; no precise binding relation is currently asserted. Host-shared scope is not evidence of clinical selectivity or toxicity.

### Underlying proprietary registry verification

identity: unknown. Targets: CHEBI:83606.

Reaxys:6564060 matches the current ChEBI source cross-reference, but its proprietary underlying structure was not independently inspected. Exact accessible authority graphs agree; the inaccessible registry is retained as a bounded verification limit.

### Optional biological objects and all adopted lead dispositions

completeness: supported. Targets: CHEBI:83606.

Every native field was inspected and all five adopted abstracts were read with distinct clinical, pharmacokinetic and review scope. Absent optional activity, target, resistance, producer, clinical-status and causal-graph objects are not mandatory defects. A curator could add qualified exact-nitrate assays through the native writer without changing source identity.

### Reproducible source ownership and honest seed history

provenance: supported. Targets: CHEBI:83606.

The actual inventory, extraction/seeding rules, source concept and history agree. Initial hashes were preserved, and scientific review does not promote the native SEEDED status.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/fenticonazole-nitrate.yaml; Complete native YAML, including all identifiers, synonyms, classification, mechanism notes, source concept and six curation events. | supports | CHEBI:83606 denotes the nitrate racemate and explicitly says equimolar R/S forms. The record preserves ANTIBACTERIAL filing plus antifungal and antibacterial roles, an honestly seeded ERGOSTEROL_PATHWAY_INHIBITION mode and HOST_SHARED_TARGET scope. It does not assert an exact protein accession, direct-binding edge, numerical activity, resistance determinant, producer, clinical-status object, dataset or causal graph. Lomexin is correctly typed BRAND_NAME; the remaining aliases describe the nitrate. The SEEDED history makes no scientific sign-off claim. |
| owners | data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; conf/sources.yaml; Complete exact inventory row 2243; applicable ChEBI extraction, synonym/xref normalization, role priority, mode and target-scope rules. | supports | The source row reproduces all imported fields and carries five adopted PMID leads. ChEBI extraction and seeding own future source corrections. ANTIBACTERIAL priority outranks ANTIFUNGAL while retaining all roles. CHEBI:75282 supplies the sterol-pathway mapping; the HOST_SHARED_TARGET rule denotes conserved enzyme-family context rather than host ergosterol synthesis or clinical selectivity. No additional exact ARO, imported target/resistance, FDA, PubChem-enrichment or MIBiG owner row was identified in the inspected inventories. |
| identity | CHEBI:83606; https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:83606; KEGG:D02583; PubChem:51754; CAS:73151-29-8; Entire current ChEBI identity response, KEGG drug entry/molfile and CAS-resolved PubChem property response; independent parsing of all representations. | supports | All five independently parsed representations give FJNRUWDGCVDXLU-UHFFFAOYSA-N. Dot-component and flattened formulas have identical element counts C24H21Cl2N3O4S, charge 0 and masses. ChEBI explicitly describes a racemate and has R/S part entries; this is not an inference from an unassigned graph. CAS and KEGG refer to the nitrate, not the free base. The source systematic names are consistent with this form. Current ChEBI repeats Reaxys:6564060, but its underlying registry record was not independently accessed. |
| ontology | CHEBI:60911; CHEBI:87069; CHEBI:87071; CHEBI:35718; CHEBI:36047; CHEBI:86327; CHEBI:75282; Current official term names/definitions and relevant native ChEBI outgoing relations. | supports | Parents resolve to racemate, imidazole antifungal drug and conazole antifungal drug; they are broader concepts rather than exact compound xrefs. The retained roles resolve to antifungal agent, antibacterial drug and antifungal drug. The inherited sterol-biosynthesis role resolves correctly. Official KEGG also describes an ergosterol-biosynthesis inhibitor and names sterol 14-alpha-demethylase, but this remains database mechanism support rather than an inspected direct enzyme experiment. |
| product | https://cima.aemps.es/cima/dochtml/ft/61715/FT_61715.html; Official AEMPS Lomexin product information: sections 1, 2, 4.1 and 5.1–5.3 read. | supports | The named product contains fenticonazole nitrate in vaginal capsules and is indicated for uncomplicated vulvovaginal candidiasis, supporting the native treatment sentence and brand association. Its pharmacodynamic text describes antifungal, Gram-positive antibacterial and antiparasitic effects and several proposed cellular effects. It does not establish a measured direct CYP51 interaction or turn this record into a formal approval assertion for every formulation or jurisdiction. |
| adopted-clinical | PMID:12017948; PMID:15216954; DOI:10.1179/joc.2004.16.2.179; PMID:8704823; Complete indexed abstracts of all three original clinical studies, read individually. | supports | PMID12017948 compares nitrate vaginal treatment with miconazole in randomized groups. PMID15216954 is an open-label mixed-infection pilot with a per-protocol population, and PMID8704823 is an uncontrolled candidosis study in which most participants also used cream. These support topical use at their actual study depth; uncontrolled outcomes do not establish comparative efficacy, all-species activity or approval status. Full methods, allocation details and complete tables were not obtained. |
| adopted-other | PMID:2019858; DOI:10.1080/1120009x.1991.11739058; PMID:9273113; Complete remaining two adopted abstracts. | context_only | PMID2019858 is an original radiolabeled nitrate absorption study across normal and pathological vaginal conditions, not an antimicrobial-target experiment. PMID9273113 is a secondary therapeutic review, retained only as context. Every adopted lead has a disposition; none is silently treated as whole-record primary support. |
| old-activity | PMID:7199313; PMID:2764547; DOI:10.1128/AAC.33.6.970; Complete indexed abstracts of original in-vitro activity studies. | supports | The 1981 original explicitly names the nitrate Rec15/1476 and reports antifungal and Gram-positive antibacterial activity with pH and serum dependence. The 1989 original reports agar-dilution activity against a bacterial panel. These are supportive whole-cell results at abstract depth; no full-table numerical extraction, target-binding conclusion or universal spectrum is made. |
| activity2019 | PMID:31061161; DOI:10.1128/AAC.02693-18; https://pmc.ncbi.nlm.nih.gov/articles/PMC6591636/; Complete public main text, both tables, methods, discussion, figure captions and acknowledgments read through browser retrieval; figure pixels not separately analysed. | supports | Methods identify Recordati nitrate, and acknowledgments specify batch M0170/069. Broth assays test 318 vaginal isolates, including Candida and bacteria; selected isolates undergo time-kill testing. Fungal MIC means at least 50% growth reduction. Mixed-culture doses are based on the Candida MIC, and reported killing times derive from fitted curves. These experiments support both antimicrobial activities, not clinical breakpoints or universal susceptibility. The discussion cites reviews for ERG11 and other proposed mechanisms; it measures neither direct binding nor ROS and explicitly calls for future ROS investigation. Local HTTP responses were challenge pages and Europe PMC XML failed, so this evidence relies on inspected public browser text rather than a falsely claimed local full-text snapshot. |
| documents | CN101288661; CN101313904; CN101474168; CN101863808; wikipedia.en:Fenticonazole; All four patent titles, abstracts and relevant introductory material; Wikipedia opening/use sections. | context_only | The first three patents concern nitrate vaginal formulations. CN101863808 concerns an intermediate used in nitrate synthesis, not an exact finished-drug structure; its document_xref placement is appropriate. The Wikipedia page concerns the active moiety and its use, likewise as a document association. No patent claims, figures or quantitative efficacy results are asserted as fully audited, and Wikipedia is not used as primary biological proof. |
| adapter | iModulonDB public dataset catalog; kg-microbe-sources imodulondb --timeout 15 datasets; Actual complete catalog output read before web mechanism follow-up. | context_only | No covered Candida/fungal dataset matches this generic fungal pathway claim, and no native gene/locus or transcriptomic experiment is asserted. No strain/module query was justified by the native record. Adapter inapplicability is not negative biological evidence, and expression membership would not establish compound binding. |
| search | 437-inclusive-hits.txt; 437-fetch-results.json; 437-fetch2-results.json; 437-fetch3-results.json; Hidden- and ignored-inclusive local search plus bounded public follow-up. | context_only | The local search covered data, curation, conf, scripts, src, docs, .claude, reviews and reports for the exact label, source/minted IDs, CAS and key. It identified the exact row and adjacent unstructured free-base ChEBI entry; no exact curator override or earlier retained review was found in that bounded surface. Public queries used the adopted PMIDs, exact nitrate name/CAS, antibacterial studies and sterol/mechanism terms. A recent colistin-adjuvant abstract and host-cell oncology studies were not transferred into a standalone antimicrobial-target assertion. |
| checks | 437-focused-results.json; 437-chemistry.json; 437-authority-chemistry.json; Actual focused schema/strict executions and independent normalized chemistry diagnostics. | supports | Schema and strict gates pass. The optional literal-formula helper fails, while normalized element counts and all native/current-authority graph comparisons pass. The original output is preserved. All thirteen captured inputs remain unchanged; these calculations do not substitute for direct target experiments. |

## Limits And Additional Notes

- Reaxys was checked only as a current ChEBI-imported cross-reference, not through its underlying proprietary structure record. No paid access was used.
- All five adopted indexed abstracts were read, but their original full clinical/PK reports were not obtained. The secondary review is explicitly contextual. The older in-vitro studies were read at abstract depth.
- The 2019 primary main text and tables were read publicly through the browser; local retrievals returned challenge HTML and an XML error. Figure captions were read, but plots were not independently digitized. No full-text content is attributed to the failed local downloads.
- The mode and target-scope assertions have transparent seeded database provenance. A direct exact-compound sterol-enzyme experiment was not re-established, so full mechanism sign-off remains limited.
- The optional chemistry helper failed solely on equivalent dot-component versus flattened formula notation. The failed execution remains recorded; a separate normalized calculation and all accessible authority graphs pass.
- Patent inspection was restricted to titles, abstracts and relevant introductory scope, not every claim, example or figure.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No confirmed finding or mandatory corrective action is proposed. Optional exact-assay and mechanism enrichment should retain salt, strain, medium, endpoint and experimental-type boundaries.
- The review retains the thirteen original input hashes and the native seeded status. All conclusions are specific to the nitrate record rather than the neighboring unstructured free-base source entry.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T161717Z-fenticonazole-nitrate-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Fenticonazole nitrate: exact salt and both antimicrobial roles supported'
started_at: '2026-10-21T15:56:41Z'
finished_at: '2026-10-21T16:17:17Z'
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
verdict: blocked
scientific_review: true
summary: The entire seeded record is consistent with its ChEBI source and exact nitrate
  identity. Independent current-authority encodings agree, and inspected primary studies
  support antifungal and antibacterial activity. No confirmed corrective defect was
  identified. Direct compound-specific target validation and some original full texts
  remain outside the attained evidence depth; the seeded mode is not promoted to a
  direct binding claim. Scientific assessment retains the stated evidence limits;
  full verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/fenticonazole-nitrate.yaml
    sha256: 17774fcad7dda895dbd348326bdc2691ee73e06cf3ca9194b23ea81bc00adb3a
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
- target_id: CHEBI:83606
  path: data/antibiotics/antibacterial/fenticonazole-nitrate.yaml
  label: fenticonazole nitrate
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
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Queue position 437; one exact complete record. All thirteen initial input
    hashes were verified before assessment and retained unchanged. The actual maintained
    source is the captured ChEBI inventory.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:83606
checks:
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:83606
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/fenticonazole-nitrate.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:83606
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/fenticonazole-nitrate.yaml --out /private/tmp/am-review-session/437-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: Focused chemistry verification
  status: failed
  required: false
  summary: The optional helper exited 1 because it compared the native dot-component
    formula C24H20Cl2N2OS.HNO3 literally with RDKit flattened C24H21Cl2N3O4S. All
    encodings, charge, masses and source mint agree. A separate element-count and
    authority-graph check resolves this notation difference; the original failed execution
    is retained.
  target_ids:
  - CHEBI:83606
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 437
  exit_code: 1
  expected_exit_code: 0
- check_id: authority-normalized-chemistry
  name: Independent authority graph and normalized element-count comparison
  status: passed
  required: false
  summary: Native SMILES/InChI, official ChEBI molfile, KEGG molfile and CAS-resolved
    PubChem SMILES all reproduce the complete key, formula element counts, neutral
    charge, two components and masses.
  target_ids:
  - CHEBI:83606
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/437-authority-check.py
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
  - CHEBI:83606
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
  - CHEBI:83606
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
  - CHEBI:83606
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
  - CHEBI:83606
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
  - CHEBI:83606
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
  - CHEBI:83606
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
  - CHEBI:83606
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
  - CHEBI:83606
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
  - CHEBI:83606
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/fenticonazole-nitrate.yaml
  locator: Complete native YAML, including all identifiers, synonyms, classification,
    mechanism notes, source concept and six curation events.
  accessed_at: '2026-10-21T16:08:03Z'
  support: supports
  summary: CHEBI:83606 denotes the nitrate racemate and explicitly says equimolar
    R/S forms. The record preserves ANTIBACTERIAL filing plus antifungal and antibacterial
    roles, an honestly seeded ERGOSTEROL_PATHWAY_INHIBITION mode and HOST_SHARED_TARGET
    scope. It does not assert an exact protein accession, direct-binding edge, numerical
    activity, resistance determinant, producer, clinical-status object, dataset or
    causal graph. Lomexin is correctly typed BRAND_NAME; the remaining aliases describe
    the nitrate. The SEEDED history makes no scientific sign-off claim.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py; conf/sources.yaml
  locator: Complete exact inventory row 2243; applicable ChEBI extraction, synonym/xref
    normalization, role priority, mode and target-scope rules.
  accessed_at: '2026-10-21T16:08:03Z'
  support: supports
  summary: The source row reproduces all imported fields and carries five adopted
    PMID leads. ChEBI extraction and seeding own future source corrections. ANTIBACTERIAL
    priority outranks ANTIFUNGAL while retaining all roles. CHEBI:75282 supplies the
    sterol-pathway mapping; the HOST_SHARED_TARGET rule denotes conserved enzyme-family
    context rather than host ergosterol synthesis or clinical selectivity. No additional
    exact ARO, imported target/resistance, FDA, PubChem-enrichment or MIBiG owner
    row was identified in the inspected inventories.
  snapshot_sha256: 6a3e415fb77f6e089705ab99e71b5171291d7318586f939b1fd04b1eb4fd27ff
- evidence_id: identity
  kind: authority
  reference: CHEBI:83606; https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:83606;
    KEGG:D02583; PubChem:51754; CAS:73151-29-8
  locator: Entire current ChEBI identity response, KEGG drug entry/molfile and CAS-resolved
    PubChem property response; independent parsing of all representations.
  accessed_at: '2026-10-21T16:03:04Z'
  support: supports
  summary: All five independently parsed representations give FJNRUWDGCVDXLU-UHFFFAOYSA-N.
    Dot-component and flattened formulas have identical element counts C24H21Cl2N3O4S,
    charge 0 and masses. ChEBI explicitly describes a racemate and has R/S part entries;
    this is not an inference from an unassigned graph. CAS and KEGG refer to the nitrate,
    not the free base. The source systematic names are consistent with this form.
    Current ChEBI repeats Reaxys:6564060, but its underlying registry record was not
    independently accessed.
  snapshot_sha256: 3f23daf59907a0147e64f87fc114099f8b544a142c2b987feedf4b68dc02d889
- evidence_id: ontology
  kind: authority
  reference: CHEBI:60911; CHEBI:87069; CHEBI:87071; CHEBI:35718; CHEBI:36047; CHEBI:86327;
    CHEBI:75282
  locator: Current official term names/definitions and relevant native ChEBI outgoing
    relations.
  accessed_at: '2026-10-21T16:03:04Z'
  support: supports
  summary: Parents resolve to racemate, imidazole antifungal drug and conazole antifungal
    drug; they are broader concepts rather than exact compound xrefs. The retained
    roles resolve to antifungal agent, antibacterial drug and antifungal drug. The
    inherited sterol-biosynthesis role resolves correctly. Official KEGG also describes
    an ergosterol-biosynthesis inhibitor and names sterol 14-alpha-demethylase, but
    this remains database mechanism support rather than an inspected direct enzyme
    experiment.
  snapshot_sha256: 23df54de8c74d9830257d83596eade8cf15d94999c7d561e9bbca457ebb56404
- evidence_id: product
  kind: authority
  reference: https://cima.aemps.es/cima/dochtml/ft/61715/FT_61715.html
  locator: 'Official AEMPS Lomexin product information: sections 1, 2, 4.1 and 5.1–5.3
    read.'
  accessed_at: '2026-10-21T16:03:37Z'
  support: supports
  summary: The named product contains fenticonazole nitrate in vaginal capsules and
    is indicated for uncomplicated vulvovaginal candidiasis, supporting the native
    treatment sentence and brand association. Its pharmacodynamic text describes antifungal,
    Gram-positive antibacterial and antiparasitic effects and several proposed cellular
    effects. It does not establish a measured direct CYP51 interaction or turn this
    record into a formal approval assertion for every formulation or jurisdiction.
  snapshot_sha256: 750855f5522f9746df6dd5addc8f02de485f61cab3f358b2c62045fcc33cb4c8
- evidence_id: adopted-clinical
  kind: primary_source
  reference: PMID:12017948; PMID:15216954; DOI:10.1179/joc.2004.16.2.179; PMID:8704823
  locator: Complete indexed abstracts of all three original clinical studies, read
    individually.
  accessed_at: '2026-10-21T16:03:04Z'
  support: supports
  summary: PMID12017948 compares nitrate vaginal treatment with miconazole in randomized
    groups. PMID15216954 is an open-label mixed-infection pilot with a per-protocol
    population, and PMID8704823 is an uncontrolled candidosis study in which most
    participants also used cream. These support topical use at their actual study
    depth; uncontrolled outcomes do not establish comparative efficacy, all-species
    activity or approval status. Full methods, allocation details and complete tables
    were not obtained.
  snapshot_sha256: 07fed98442f042d8a3b3586445e69029a717c711ada51a6d75b40907ac1ebfe9
- evidence_id: adopted-other
  kind: database
  reference: PMID:2019858; DOI:10.1080/1120009x.1991.11739058; PMID:9273113
  locator: Complete remaining two adopted abstracts.
  accessed_at: '2026-10-21T16:03:04Z'
  support: context_only
  summary: PMID2019858 is an original radiolabeled nitrate absorption study across
    normal and pathological vaginal conditions, not an antimicrobial-target experiment.
    PMID9273113 is a secondary therapeutic review, retained only as context. Every
    adopted lead has a disposition; none is silently treated as whole-record primary
    support.
  snapshot_sha256: 07fed98442f042d8a3b3586445e69029a717c711ada51a6d75b40907ac1ebfe9
- evidence_id: old-activity
  kind: primary_source
  reference: PMID:7199313; PMID:2764547; DOI:10.1128/AAC.33.6.970
  locator: Complete indexed abstracts of original in-vitro activity studies.
  accessed_at: '2026-10-21T16:03:04Z'
  support: supports
  summary: The 1981 original explicitly names the nitrate Rec15/1476 and reports antifungal
    and Gram-positive antibacterial activity with pH and serum dependence. The 1989
    original reports agar-dilution activity against a bacterial panel. These are supportive
    whole-cell results at abstract depth; no full-table numerical extraction, target-binding
    conclusion or universal spectrum is made.
  snapshot_sha256: 82b2b3554e3e594eef85811b1842b8e206848c57ce4d8d3c099d7bd63b55ffce
- evidence_id: activity2019
  kind: primary_source
  reference: PMID:31061161; DOI:10.1128/AAC.02693-18; https://pmc.ncbi.nlm.nih.gov/articles/PMC6591636/
  locator: Complete public main text, both tables, methods, discussion, figure captions
    and acknowledgments read through browser retrieval; figure pixels not separately
    analysed.
  accessed_at: '2026-10-21T16:08:03Z'
  support: supports
  summary: Methods identify Recordati nitrate, and acknowledgments specify batch M0170/069.
    Broth assays test 318 vaginal isolates, including Candida and bacteria; selected
    isolates undergo time-kill testing. Fungal MIC means at least 50% growth reduction.
    Mixed-culture doses are based on the Candida MIC, and reported killing times derive
    from fitted curves. These experiments support both antimicrobial activities, not
    clinical breakpoints or universal susceptibility. The discussion cites reviews
    for ERG11 and other proposed mechanisms; it measures neither direct binding nor
    ROS and explicitly calls for future ROS investigation. Local HTTP responses were
    challenge pages and Europe PMC XML failed, so this evidence relies on inspected
    public browser text rather than a falsely claimed local full-text snapshot.
- evidence_id: documents
  kind: authority
  reference: CN101288661; CN101313904; CN101474168; CN101863808; wikipedia.en:Fenticonazole
  locator: All four patent titles, abstracts and relevant introductory material; Wikipedia
    opening/use sections.
  accessed_at: '2026-10-21T16:03:07Z'
  support: context_only
  summary: The first three patents concern nitrate vaginal formulations. CN101863808
    concerns an intermediate used in nitrate synthesis, not an exact finished-drug
    structure; its document_xref placement is appropriate. The Wikipedia page concerns
    the active moiety and its use, likewise as a document association. No patent claims,
    figures or quantitative efficacy results are asserted as fully audited, and Wikipedia
    is not used as primary biological proof.
  snapshot_sha256: 662c5516f69ced0c1c7588b781a750e98f6aa76471e5abc1a4c7d42f7c58ea38
- evidence_id: adapter
  kind: database
  reference: iModulonDB public dataset catalog; kg-microbe-sources imodulondb --timeout
    15 datasets
  locator: Actual complete catalog output read before web mechanism follow-up.
  accessed_at: '2026-10-21T16:08:03Z'
  support: context_only
  summary: No covered Candida/fungal dataset matches this generic fungal pathway claim,
    and no native gene/locus or transcriptomic experiment is asserted. No strain/module
    query was justified by the native record. Adapter inapplicability is not negative
    biological evidence, and expression membership would not establish compound binding.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: search
  kind: search
  reference: 437-inclusive-hits.txt; 437-fetch-results.json; 437-fetch2-results.json;
    437-fetch3-results.json
  locator: Hidden- and ignored-inclusive local search plus bounded public follow-up.
  accessed_at: '2026-10-21T16:08:03Z'
  support: context_only
  summary: The local search covered data, curation, conf, scripts, src, docs, .claude,
    reviews and reports for the exact label, source/minted IDs, CAS and key. It identified
    the exact row and adjacent unstructured free-base ChEBI entry; no exact curator
    override or earlier retained review was found in that bounded surface. Public
    queries used the adopted PMIDs, exact nitrate name/CAS, antibacterial studies
    and sterol/mechanism terms. A recent colistin-adjuvant abstract and host-cell
    oncology studies were not transferred into a standalone antimicrobial-target assertion.
  snapshot_sha256: bdd3605a874f2288d30921f0f88207fcf797f5fc68f002f523ae866648c7ce30
  search_scope: 2026-10-21; rg --no-ignore --hidden across the stated local paths
    for CHEBI:83606, fenticonazole, FJNRUWDGCVDXLU, 73151-29-8 and chebi-aacddd8ee7;
    public Europe PMC and exact-name/sterol/mechanism searches.
- evidence_id: checks
  kind: validation
  reference: 437-focused-results.json; 437-chemistry.json; 437-authority-chemistry.json
  locator: Actual focused schema/strict executions and independent normalized chemistry
    diagnostics.
  accessed_at: '2026-10-21T16:08:03Z'
  support: supports
  summary: Schema and strict gates pass. The optional literal-formula helper fails,
    while normalized element counts and all native/current-authority graph comparisons
    pass. The original output is preserved. All thirteen captured inputs remain unchanged;
    these calculations do not substitute for direct target experiments.
  snapshot_sha256: 6adb08e305a6d8806a8df8fc068ef41a53053751ae50cd63612f0d6f9fc90ed0
assessments:
- assessment_id: identity
  area: identity
  topic: Exact nitrate form, synonyms and chemical properties
  outcome: supported
  summary: The complete current graphs, full key, component counts, normalized formula
    and masses agree. The definition explicitly identifies the racemate; the stored
    representation does not purport to distinguish the two enantiomers. The broader
    racemate parent and properly typed product/document associations preserve their
    intended scope.
  target_ids:
  - CHEBI:83606
  evidence_ids:
  - native
  - identity
  - ontology
  - product
  - documents
  - checks
- assessment_id: classification
  area: evidence
  topic: Filing class, retained roles and clinical-use definition
  outcome: supported
  summary: Both antibacterial and antifungal roles have exact-form support. Priority
    ANTIBACTERIAL filing is therefore not a contradiction, and the product authority
    supports the vaginal-candidiasis treatment wording. Seeded cross-activity notes
    are cautious rather than a confirmed incorrect assertion.
  target_ids:
  - CHEBI:83606
  evidence_ids:
  - owners
  - ontology
  - product
  - adopted-clinical
  - old-activity
  - activity2019
- assessment_id: mechanism
  area: evidence
  topic: Seeded sterol-pathway mode and host-shared scope
  outcome: unknown
  summary: The native mode and scope are reproducible qualified database assertions.
    Direct compound-specific sterol-enzyme inhibition was not independently established
    from an original biochemical experiment at this review depth. This remains an
    evidence limit, not proof that the mode is false; no precise binding relation
    is currently asserted. Host-shared scope is not evidence of clinical selectivity
    or toxicity.
  target_ids:
  - CHEBI:83606
  evidence_ids:
  - native
  - owners
  - ontology
  - product
  - activity2019
  - adapter
- assessment_id: xref-access
  area: identity
  topic: Underlying proprietary registry verification
  outcome: unknown
  summary: Reaxys:6564060 matches the current ChEBI source cross-reference, but its
    proprietary underlying structure was not independently inspected. Exact accessible
    authority graphs agree; the inaccessible registry is retained as a bounded verification
    limit.
  target_ids:
  - CHEBI:83606
  evidence_ids:
  - identity
- assessment_id: coverage
  area: completeness
  topic: Optional biological objects and all adopted lead dispositions
  outcome: supported
  summary: Every native field was inspected and all five adopted abstracts were read
    with distinct clinical, pharmacokinetic and review scope. Absent optional activity,
    target, resistance, producer, clinical-status and causal-graph objects are not
    mandatory defects. A curator could add qualified exact-nitrate assays through
    the native writer without changing source identity.
  target_ids:
  - CHEBI:83606
  evidence_ids:
  - native
  - adopted-clinical
  - adopted-other
  - old-activity
  - activity2019
  - search
- assessment_id: provenance
  area: provenance
  topic: Reproducible source ownership and honest seed history
  outcome: supported
  summary: The actual inventory, extraction/seeding rules, source concept and history
    agree. Initial hashes were preserved, and scientific review does not promote the
    native SEEDED status.
  target_ids:
  - CHEBI:83606
  evidence_ids:
  - owners
  - native
  - checks
findings: []
actions: []
limitations:
- Reaxys was checked only as a current ChEBI-imported cross-reference, not through
  its underlying proprietary structure record. No paid access was used.
- All five adopted indexed abstracts were read, but their original full clinical/PK
  reports were not obtained. The secondary review is explicitly contextual. The older
  in-vitro studies were read at abstract depth.
- The 2019 primary main text and tables were read publicly through the browser; local
  retrievals returned challenge HTML and an XML error. Figure captions were read,
  but plots were not independently digitized. No full-text content is attributed to
  the failed local downloads.
- The mode and target-scope assertions have transparent seeded database provenance.
  A direct exact-compound sterol-enzyme experiment was not re-established, so full
  mechanism sign-off remains limited.
- The optional chemistry helper failed solely on equivalent dot-component versus flattened
  formula notation. The failed execution remains recorded; a separate normalized calculation
  and all accessible authority graphs pass.
- Patent inspection was restricted to titles, abstracts and relevant introductory
  scope, not every claim, example or figure.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No confirmed finding or mandatory corrective action is proposed. Optional exact-assay
  and mechanism enrichment should retain salt, strain, medium, endpoint and experimental-type
  boundaries.
- The review retains the thirteen original input hashes and the native seeded status.
  All conclusions are specific to the nitrate record rather than the neighboring unstructured
  free-base source entry.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
