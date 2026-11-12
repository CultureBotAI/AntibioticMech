# (E)-Roxithromycin: consistent exact structure and supported antibacterial classification

- Review: 20261021T152039Z-e-roxithromycin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:52:14Z
- Finished UTC: 2026-10-21T15:20:39Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The exact E oxime, all eighteen assigned tetrahedral centres and neutral molecular formula agree across native encodings, current ChEBI, DrugCentral structure endpoints, the RCSB ROX component and the public CAS-linked PubChem structure. The original 1986 antibacterial study and exact ROX ribosome deposition support the retained biological classification and a bounded mechanism follow-up. No corrective finding was established; several source-access limits remain. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Queue position 387; one exact record. All thirteen original captured input hashes were verified before assessment and retained. The original ChEBI owner set was confirmed correct.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:48935 | data/antibiotics/antibacterial/e-roxithromycin.yaml | generated | (E)-roxithromycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:48935 | Actual focused schema validation passed. |
| strict | passed | True | CHEBI:48935 | Actual focused strict validation passed. |
| chemistry | passed | False | CHEBI:48935 | Native SMILES/InChI agree in full key, charge, formula and masses. The deterministic source alias reproduces. |
| authority-chemistry | passed | False | CHEBI:48935 | Independent parsing of current ChEBI molfile, three DrugCentral structure encodings, PubChem SMILES/InChI and RCSB ROX canonical SMILES/InChI agrees with the exact native E structure. |
| Authoritative full QC | failed | True | CHEBI:48935 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:48935 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:48935 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:48935 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:48935 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:48935 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:48935 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:48935 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:48935 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact E graph, names and structure hierarchy

identity: supported. Targets: CHEBI:48935.

Native encodings and all successfully inspected official structure endpoints agree, including all eighteen assigned centres and oxime E geometry. The parent leaves that geometry unspecified and is broader. INN language variants and the E-specific chemical synonyms are traceable to current ChEBI.

### External chemical cross references

identity: unknown. Targets: CHEBI:48935.

DrugCentral, RCSB ROX and public CAS-linked PubChem structure checks support the native identity. HMDB and proprietary Beilstein/Reaxys exact structures remain uninspected after bounded free attempts. DrugCentral has an ancillary conflicting Z ChEBI pointer, but its actual graph is exact E. No native xref mismatch was established.

### Antimicrobial roles and primary exact-form activity

evidence: supported. Targets: CHEBI:48935.

The inherited ChEBI antimicrobial and antibacterial-drug roles are retained correctly. The original supplied RU 28965 experiment depicts the E compound and provides direct antibacterial evidence. Exact-form registry and metabolism evidence reinforce the ordinary drug-name mapping; no statement of perfect isomeric purity or individual-strain MIC is fabricated.

### Mode-of-action review and optional biological fields

evidence: supported. Targets: CHEBI:48935.

The exact ROX ribosome deposition supports a bounded ribosomal mechanism follow-up. The native makes no direct protein, gene, regulator, response or transcriptomic claim, so a structured iModulon adapter is not applicable to its asserted fields. No empty optional target, resistance, graph, activity, producer or dataset slot is treated as a corrective defect.

### All adopted citation dispositions

evidence: unknown. Targets: CHEBI:48935.

PMID12575424 is accessible only as title/index metadata and concerns host cytokines. PMID24462419 was read at complete abstract depth and concerns clinical symptom outcomes. Neither was silently used as direct bacterial target or MIC evidence; independent original studies support the biological classification.

### Generated ownership, history and whole-record coverage

provenance: supported. Targets: CHEBI:48935.

The exact source row, role inheritance, synonym/xref mappings, source version, alias and all history events are consistent. All original hashes are preserved. SEEDED remains the native status, and the scientific review does not claim a curation mutation or completed native sign-off.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/e-roxithromycin.yaml; Entire native YAML. | supports | CHEBI:48935 is an EXACT, SEEDED record of neutral E-roxithromycin, full key RXZBMPWDPOLZGW-XMRMVWPWSA-N and formula C41H76N2O15. The definition identifies a major geometrical isomer. Four INN forms, three exact synonyms, one broader parent, two activity roles, five registry/component xrefs and one DrugCentral drug xref are present. There are no molecular targets, quantitative observations, resistance mechanisms, producers, clinical-status assertions, datasets or causal graphs. |
| owners | data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; conf/sources.yaml; Complete exact ChEBI row 908, all actual source-row checks, inheritance/extraction code and synonym/xref seeding logic. | supports | The native faithfully reproduces the ChEBI inventory. Reviewed antimicrobial roles are inherited from the broader roxithromycin parent; this is explicit source-transform behavior. INN types remain INN, IUPAC and synonym entries become exact names, and DrugCentral is routed to drug_xrefs. The two retained PMID leads are intentionally not installed as evidence for every claim. No ARO, target, resistance, FDA, PubChem or MIBiG row applies to this exact record. All four history entries, dated source version and minted alias agree with the generated source path. |
| chebi | CHEBI:48935; https://www.ebi.ac.uk/chebi/CHEBI:48935; Complete current entry including definition, all names, chemical descriptors, roles, outgoing relations and cross references. | supports | Current ChEBI retains the exact native E oxime and full stereochemical key, formula, charge and masses. The INN language variants and exact chemical names match. CAS80214-83-1, Beilstein/Reaxys5900029, HMDB0014916, ROX and DrugCentral2410 are the current adopted links. Environmental-contaminant and xenobiotic annotations are outside this corpus antimicrobial-role selection and are not missing antimicrobial roles. |
| parent | CHEBI:48844; https://www.ebi.ac.uk/chebi/CHEBI:48844; Complete current parent page and displayed chemical encodings. | supports | The parent roxithromycin retains the same constitution and assigned tetrahedral centres but does not assign oxime E/Z geometry; its full key is RXZBMPWDPOLZGW-HITVVWEBSA-N. It explicitly has E and Z children and the antibacterial-drug role CHEBI:36047, with antimicrobial-agent CHEBI:33281 in the role hierarchy. This supports the native parent as broader without treating an unspecified graph as an established mixture. |
| official-graph | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/48935; Complete official molfile independently parsed. | supports | The ChEBI graph reproduces the exact native full key, eighteen assigned tetrahedral centres, E oxime, neutral charge and formula. The original antibacterial-study drawing is concordant in scaffold and E oxime depiction; no independent re-elucidation of every absolute centre is claimed. |
| drugcentral | drugcentral:2410; https://drugcentral.org/drugcard/2410; https://drugcentral.org/drug/2410/molfile; Current public card and complete linked SMILES, InChI and molfile inspected and independently parsed. | supports | All three DrugCentral molecular encodings reproduce the native full E-stereochemical key. The card lists CAS80214-83-1 and identifies roxithromycin. Its separate external-link table includes a Z-isomer ChEBI pointer, an internal source inconsistency that does not change the directly inspected DrugCentral graph or establish a wrong native drug_xref. Ancillary drug-card target or product claims were not imported. |
| ccd | pdb-ccd:ROX; https://www.rcsb.org/ligand/ROX; https://files.rcsb.org/ligands/download/ROX.cif; Complete chemical-component descriptor block and public component metadata. | supports | The ROX chemical component has the same full InChI/key, formula and E stereochemistry. Both CACTVS and OpenEye canonical stereochemical SMILES independently parse to the native full key. ROX is the chemical-component identifier, not an assertion that the whole macromolecular structure is chemically identical to the small molecule. |
| cas | CAS:80214-83-1; PubChem:6915744; https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/80214-83-1/property/InChI,InChIKey,MolecularFormula,SMILES/JSON; Complete public CAS-name query response and independent structure parse. | supports | The public CAS-linked record resolves to CID6915744 and exactly matches native SMILES/InChI identity, E geometry, formula and charge. This checks the imported CAS association independently of ChEBI but is not a proprietary CAS Registry inspection. |
| remaining-xrefs | HMDB:HMDB0014916; Beilstein:5900029; Reaxys:5900029; Current ChEBI registry provenance and attempted direct public HMDB page, XML and molfile routes. | context_only | The HMDB link and legacy Beilstein/Reaxys number are confirmed as adopted ChEBI identifiers. Direct HMDB routes returned403; a web result exposed the page title but did not permit reliable inspection of its exact structure descriptors. Beilstein/Reaxys proprietary records were not accessed. These exact graph checks remain unresolved, not reported as either mismatches or completed independent verification. |
| adopted-th2 | PMID:12575424; https://pubmed.ncbi.nlm.nih.gov/12575424/; Complete indexed bibliographic record, title and indexing; no abstract or full text obtained. | context_only | The 2001 Japanese report concerns suppression of Th2 cytokine production, with human T-cell and interleukin indexing. The index exposes no abstract. This is a host-response lead, not inspected direct bacterial activity or exact-isomer mechanism evidence. No quantitative or causal claim is attributed to the unread article. |
| adopted-clinical | PMID:24462419; DOI:10.1016/j.jiac.2013.07.010; Complete original indexed abstract, publisher bibliographic result and author-university abstract. | context_only | This open-label 75-patient pilot compares roxithromycin, ciprofloxacin and aceclofenac for chronic prostatitis/chronic pelvic pain symptoms. Overall treatment efficacy did not differ significantly between groups. It is a clinical symptom and immunomodulation context, not an exact E-isomer bacterial MIC, ribosomal binding assay or regulatory approval. The source-owned lead is valid but does not independently substantiate all native biology. |
| original-antibacterial | PMID:3733515; DOI:10.7164/antibiotics.39.660; https://www.jstage.jst.go.jp/article/antibiotics1968/39/5/39_5_660/_pdf; Complete original nine-page1986 article read; Figure 1 and methods on p661 and Table 1 on p663 visually checked. | supports | The Roussel-Uclaf study identifies RU 28965 and depicts the E oxime in Figure 1. Supplied roxithromycin inhibited bacteria in a275-isolate study and protected experimentally infected mice. Broth macrodilution used twofold concentrations, approximately 10^5 CFU/mL, 36 degrees C and 20 hours; MIC means no visible growth. Media varied by organism. In 69 erythromycin-susceptible staphylococcal isolates the roxithromycin MIC range was 0.3–2.5 micrograms/mL, MIC50 0.6 and MIC90 1.2. Resistant subsets and tested Enterobacteriaceae had substantially higher values. These support antibacterial activity without defining a species-wide spectrum. No quantitative E/Z purity assay is reported for the supplied material. |
| exact-form-context | PMID:10772634; DOI:10.1016/s0090-9556(24)15099-4; Complete original indexed abstract; no full article obtained. | supports | The original human-metabolism study explicitly identifies administered roxithromycin as E-configured and distinguishes its Z-isomer metabolite through analytical comparison with synthesized standards. This supports the ordinary drug-name to E-form mapping and the native major-isomer description. Metabolism or host findings are not transferred to a microbial mechanism. |
| ribosome | PMID:11677599; DOI:10.1038/35101544; PDB:1JZZ; https://www.rcsb.org/structure/1JZZ; Complete original indexed abstract plus original experimental deposition metadata and exact ROX chemical component. Main article PDF route returned HTML, not an article PDF. | supports | The primary experiment reports D. radiodurans 50S ribosome complexes with antibiotics and identifies binding-site 23S rRNA. PDB 1JZZ is the roxithromycin complex at 3.8 angstrom resolution and links exact ROX to the experiment. This provides exact-form structural support for ribosome interaction. It does not by itself measure affinity or establish all downstream cellular effects; detailed contacts were not re-refined and the main article was not read in full. |
| search | 387-inclusive-hits.txt; 387-cache-leads.txt; Ignored-inclusive local native/source/overlay/history search and bounded public original-source follow-up. | context_only | The search found exact raw/native records, the path lock, readiness queue and historical E/Z ad hoc reviews. It found no exact corrective overlay in searched curation/conf paths. Historical reviews supplied literature leads only; their optional-field absence finding is not adopted. Public follow-up recovered the original 1986 full article,2000 metabolism abstract and2001 structural deposition. A separate ignored-inclusive scratch-cache search found citations and later discussions but no cached complete2001 original article. |
| validation | 387-schema.log; 387-strict.log; 387-chemistry.json; 387-xref-chemistry.json; Actual focused checks and independent chemistry, with captured-input hash recheck. | supports | Focused schema, strict, chemistry and exact authority-graph checks all passed. Validation establishes structural consistency, not scientific proof by itself. |

## Limits And Additional Notes

- HMDB page/XML/molfile access returned403; exact HMDB structure was not independently inspected. Beilstein and Reaxys records were not accessed. The public CAS query checks the association through PubChem, not a proprietary CAS Registry record.
- The 2001 structural study was read at complete indexed abstract and original PDB deposition depth. Its publisher PDF URL returned 3038 bytes of HTML, not a PDF; detailed full-paper contacts and density were not reanalyzed.
- Adopted PMID12575424 has no indexed abstract and its full Japanese article was not obtained. Adopted PMID24462419 was read at complete original abstract depth, with publisher and author-university bibliographic checks; no exact material or microbiological endpoint is inferred from that clinical pilot.
- The complete 1986 main article was read, with original Figure 1, methods and Table 1 visually checked. It depicts exact E-roxithromycin and identifies supplier material but does not quantify E/Z purity. Population MIC summaries are not individual-strain observations.
- The 2000 metabolism paper was assessed at complete original abstract depth. It is used only for the explicit E starting-form versus Z-metabolite distinction.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No corrective finding was established. Optional future mechanism or activity enrichment should attach evidence to each claim and retain exact structure, organism, strain or population, medium and endpoint boundaries.
- The ancillary DrugCentral Z-isomer link should not override its independently checked E molecular encodings. No cross-record merger or structure replacement is justified by that internal link alone.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T152039Z-e-roxithromycin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: '(E)-Roxithromycin: consistent exact structure and supported antibacterial
  classification'
started_at: '2026-10-21T14:52:14Z'
finished_at: '2026-10-21T15:20:39Z'
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
summary: The exact E oxime, all eighteen assigned tetrahedral centres and neutral
  molecular formula agree across native encodings, current ChEBI, DrugCentral structure
  endpoints, the RCSB ROX component and the public CAS-linked PubChem structure. The
  original 1986 antibacterial study and exact ROX ribosome deposition support the
  retained biological classification and a bounded mechanism follow-up. No corrective
  finding was established; several source-access limits remain. Scientific assessment
  retains the stated evidence limits; full verification is blocked by the shared native-library
  failure.
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
  - path: data/antibiotics/antibacterial/e-roxithromycin.yaml
    sha256: 2071aaeccf1ec45fe0ccca0ee260a20e344ba40f217c8d881804d94911b75366
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
- target_id: CHEBI:48935
  path: data/antibiotics/antibacterial/e-roxithromycin.yaml
  label: (E)-roxithromycin
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
  selection: Queue position 387; one exact record. All thirteen original captured
    input hashes were verified before assessment and retained. The original ChEBI
    owner set was confirmed correct.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:48935
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Actual focused schema validation passed.
  target_ids:
  - CHEBI:48935
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/e-roxithromycin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Actual focused strict validation passed.
  target_ids:
  - CHEBI:48935
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/e-roxithromycin.yaml --out /private/tmp/am-review-session/387-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Native SMILES/InChI agree in full key, charge, formula and masses. The
    deterministic source alias reproduces.
  target_ids:
  - CHEBI:48935
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 387
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-chemistry
  name: authority-chemistry
  status: passed
  required: false
  summary: Independent parsing of current ChEBI molfile, three DrugCentral structure
    encodings, PubChem SMILES/InChI and RCSB ROX canonical SMILES/InChI agrees with
    the exact native E structure.
  target_ids:
  - CHEBI:48935
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/387-xref-check.py
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
  - CHEBI:48935
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
  - CHEBI:48935
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
  - CHEBI:48935
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
  - CHEBI:48935
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
  - CHEBI:48935
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
  - CHEBI:48935
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
  - CHEBI:48935
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
  - CHEBI:48935
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
  - CHEBI:48935
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/e-roxithromycin.yaml
  locator: Entire native YAML.
  accessed_at: '2026-10-21T15:19:58Z'
  support: supports
  summary: CHEBI:48935 is an EXACT, SEEDED record of neutral E-roxithromycin, full
    key RXZBMPWDPOLZGW-XMRMVWPWSA-N and formula C41H76N2O15. The definition identifies
    a major geometrical isomer. Four INN forms, three exact synonyms, one broader
    parent, two activity roles, five registry/component xrefs and one DrugCentral
    drug xref are present. There are no molecular targets, quantitative observations,
    resistance mechanisms, producers, clinical-status assertions, datasets or causal
    graphs.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py; conf/sources.yaml
  locator: Complete exact ChEBI row 908, all actual source-row checks, inheritance/extraction
    code and synonym/xref seeding logic.
  accessed_at: '2026-10-21T15:19:58Z'
  support: supports
  summary: The native faithfully reproduces the ChEBI inventory. Reviewed antimicrobial
    roles are inherited from the broader roxithromycin parent; this is explicit source-transform
    behavior. INN types remain INN, IUPAC and synonym entries become exact names,
    and DrugCentral is routed to drug_xrefs. The two retained PMID leads are intentionally
    not installed as evidence for every claim. No ARO, target, resistance, FDA, PubChem
    or MIBiG row applies to this exact record. All four history entries, dated source
    version and minted alias agree with the generated source path.
  snapshot_sha256: eb8e495a686d13910e58f085bcb9aa2dc2248bea98b96d18b0f69412c303d6bb
- evidence_id: chebi
  kind: authority
  reference: CHEBI:48935; https://www.ebi.ac.uk/chebi/CHEBI:48935
  locator: Complete current entry including definition, all names, chemical descriptors,
    roles, outgoing relations and cross references.
  accessed_at: '2026-10-21T15:16:40Z'
  support: supports
  summary: Current ChEBI retains the exact native E oxime and full stereochemical
    key, formula, charge and masses. The INN language variants and exact chemical
    names match. CAS80214-83-1, Beilstein/Reaxys5900029, HMDB0014916, ROX and DrugCentral2410
    are the current adopted links. Environmental-contaminant and xenobiotic annotations
    are outside this corpus antimicrobial-role selection and are not missing antimicrobial
    roles.
  snapshot_sha256: c9d7408b93610ebe031db7af1711df94c52576fefa6ebe3c55a0d852033b17d1
- evidence_id: parent
  kind: authority
  reference: CHEBI:48844; https://www.ebi.ac.uk/chebi/CHEBI:48844
  locator: Complete current parent page and displayed chemical encodings.
  accessed_at: '2026-10-21T15:16:40Z'
  support: supports
  summary: The parent roxithromycin retains the same constitution and assigned tetrahedral
    centres but does not assign oxime E/Z geometry; its full key is RXZBMPWDPOLZGW-HITVVWEBSA-N.
    It explicitly has E and Z children and the antibacterial-drug role CHEBI:36047,
    with antimicrobial-agent CHEBI:33281 in the role hierarchy. This supports the
    native parent as broader without treating an unspecified graph as an established
    mixture.
  snapshot_sha256: 1946fae5123597bdd6cbf54bfcdcce3aa8a00ffbdc79aea06c18d395bbc47047
- evidence_id: official-graph
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/48935
  locator: Complete official molfile independently parsed.
  accessed_at: '2026-10-21T15:16:40Z'
  support: supports
  summary: The ChEBI graph reproduces the exact native full key, eighteen assigned
    tetrahedral centres, E oxime, neutral charge and formula. The original antibacterial-study
    drawing is concordant in scaffold and E oxime depiction; no independent re-elucidation
    of every absolute centre is claimed.
  snapshot_sha256: 6c4247558b361ea922d46edb74ca9a36de6c74f18c7c073f10fd9d021fce9cfb
- evidence_id: drugcentral
  kind: authority
  reference: drugcentral:2410; https://drugcentral.org/drugcard/2410; https://drugcentral.org/drug/2410/molfile
  locator: Current public card and complete linked SMILES, InChI and molfile inspected
    and independently parsed.
  accessed_at: '2026-10-21T15:17:11Z'
  support: supports
  summary: All three DrugCentral molecular encodings reproduce the native full E-stereochemical
    key. The card lists CAS80214-83-1 and identifies roxithromycin. Its separate external-link
    table includes a Z-isomer ChEBI pointer, an internal source inconsistency that
    does not change the directly inspected DrugCentral graph or establish a wrong
    native drug_xref. Ancillary drug-card target or product claims were not imported.
  snapshot_sha256: f8c55999cbf6e63deb97c10b626d134f71aea85e47c55459f701c229a64fe27c
- evidence_id: ccd
  kind: authority
  reference: pdb-ccd:ROX; https://www.rcsb.org/ligand/ROX; https://files.rcsb.org/ligands/download/ROX.cif
  locator: Complete chemical-component descriptor block and public component metadata.
  accessed_at: '2026-10-21T15:16:40Z'
  support: supports
  summary: The ROX chemical component has the same full InChI/key, formula and E stereochemistry.
    Both CACTVS and OpenEye canonical stereochemical SMILES independently parse to
    the native full key. ROX is the chemical-component identifier, not an assertion
    that the whole macromolecular structure is chemically identical to the small molecule.
  snapshot_sha256: 8e9458184db2b58eb83fa95d173f29931cb04d0b2e039b822ede80ae656eab18
- evidence_id: cas
  kind: authority
  reference: CAS:80214-83-1; PubChem:6915744; https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/80214-83-1/property/InChI,InChIKey,MolecularFormula,SMILES/JSON
  locator: Complete public CAS-name query response and independent structure parse.
  accessed_at: '2026-10-21T15:16:41Z'
  support: supports
  summary: The public CAS-linked record resolves to CID6915744 and exactly matches
    native SMILES/InChI identity, E geometry, formula and charge. This checks the
    imported CAS association independently of ChEBI but is not a proprietary CAS Registry
    inspection.
  snapshot_sha256: 725e9a9b5198c9f1f8a3c7360b471439ad004e65904080d4a6fde45abac71846
- evidence_id: remaining-xrefs
  kind: authority
  reference: HMDB:HMDB0014916; Beilstein:5900029; Reaxys:5900029
  locator: Current ChEBI registry provenance and attempted direct public HMDB page,
    XML and molfile routes.
  accessed_at: '2026-10-21T15:19:58Z'
  support: context_only
  summary: The HMDB link and legacy Beilstein/Reaxys number are confirmed as adopted
    ChEBI identifiers. Direct HMDB routes returned403; a web result exposed the page
    title but did not permit reliable inspection of its exact structure descriptors.
    Beilstein/Reaxys proprietary records were not accessed. These exact graph checks
    remain unresolved, not reported as either mismatches or completed independent
    verification.
  snapshot_sha256: 51a0bcc565b60b12ffd8d8289d93512d42aed7a6cbe0c9063805dc50a99ab597
- evidence_id: adopted-th2
  kind: database
  reference: PMID:12575424; https://pubmed.ncbi.nlm.nih.gov/12575424/
  locator: Complete indexed bibliographic record, title and indexing; no abstract
    or full text obtained.
  accessed_at: '2026-10-21T15:16:41Z'
  support: context_only
  summary: The 2001 Japanese report concerns suppression of Th2 cytokine production,
    with human T-cell and interleukin indexing. The index exposes no abstract. This
    is a host-response lead, not inspected direct bacterial activity or exact-isomer
    mechanism evidence. No quantitative or causal claim is attributed to the unread
    article.
  snapshot_sha256: ededbee66ce3577c2c07276144e82477deeb938cffd39dd7418243fad979e408
- evidence_id: adopted-clinical
  kind: primary_source
  reference: PMID:24462419; DOI:10.1016/j.jiac.2013.07.010
  locator: Complete original indexed abstract, publisher bibliographic result and
    author-university abstract.
  accessed_at: '2026-10-21T15:16:41Z'
  support: context_only
  summary: This open-label 75-patient pilot compares roxithromycin, ciprofloxacin
    and aceclofenac for chronic prostatitis/chronic pelvic pain symptoms. Overall
    treatment efficacy did not differ significantly between groups. It is a clinical
    symptom and immunomodulation context, not an exact E-isomer bacterial MIC, ribosomal
    binding assay or regulatory approval. The source-owned lead is valid but does
    not independently substantiate all native biology.
  snapshot_sha256: ededbee66ce3577c2c07276144e82477deeb938cffd39dd7418243fad979e408
- evidence_id: original-antibacterial
  kind: primary_source
  reference: PMID:3733515; DOI:10.7164/antibiotics.39.660; https://www.jstage.jst.go.jp/article/antibiotics1968/39/5/39_5_660/_pdf
  locator: Complete original nine-page1986 article read; Figure 1 and methods on p661
    and Table 1 on p663 visually checked.
  accessed_at: '2026-10-21T15:17:24Z'
  support: supports
  summary: The Roussel-Uclaf study identifies RU 28965 and depicts the E oxime in
    Figure 1. Supplied roxithromycin inhibited bacteria in a275-isolate study and
    protected experimentally infected mice. Broth macrodilution used twofold concentrations,
    approximately 10^5 CFU/mL, 36 degrees C and 20 hours; MIC means no visible growth.
    Media varied by organism. In 69 erythromycin-susceptible staphylococcal isolates
    the roxithromycin MIC range was 0.3–2.5 micrograms/mL, MIC50 0.6 and MIC90 1.2.
    Resistant subsets and tested Enterobacteriaceae had substantially higher values.
    These support antibacterial activity without defining a species-wide spectrum.
    No quantitative E/Z purity assay is reported for the supplied material.
  snapshot_sha256: 82e0b71c8869e226063787d168a8e363339102b9f9dcbcb8a4e9fd04d3ff7d32
- evidence_id: exact-form-context
  kind: primary_source
  reference: PMID:10772634; DOI:10.1016/s0090-9556(24)15099-4
  locator: Complete original indexed abstract; no full article obtained.
  accessed_at: '2026-10-21T15:18:20Z'
  support: supports
  summary: The original human-metabolism study explicitly identifies administered
    roxithromycin as E-configured and distinguishes its Z-isomer metabolite through
    analytical comparison with synthesized standards. This supports the ordinary drug-name
    to E-form mapping and the native major-isomer description. Metabolism or host
    findings are not transferred to a microbial mechanism.
  snapshot_sha256: 8004483c632ec9073bda2ab4bea7ca68e7f478d9bdc049fc38653d82c0233851
- evidence_id: ribosome
  kind: primary_source
  reference: PMID:11677599; DOI:10.1038/35101544; PDB:1JZZ; https://www.rcsb.org/structure/1JZZ
  locator: Complete original indexed abstract plus original experimental deposition
    metadata and exact ROX chemical component. Main article PDF route returned HTML,
    not an article PDF.
  accessed_at: '2026-10-21T15:17:24Z'
  support: supports
  summary: The primary experiment reports D. radiodurans 50S ribosome complexes with
    antibiotics and identifies binding-site 23S rRNA. PDB 1JZZ is the roxithromycin
    complex at 3.8 angstrom resolution and links exact ROX to the experiment. This
    provides exact-form structural support for ribosome interaction. It does not by
    itself measure affinity or establish all downstream cellular effects; detailed
    contacts were not re-refined and the main article was not read in full.
  snapshot_sha256: 5006dee8bb01b5a04a8b532b3149102d5734fd14404019e9e112dcfc0fc20275
- evidence_id: search
  kind: search
  reference: 387-inclusive-hits.txt; 387-cache-leads.txt
  locator: Ignored-inclusive local native/source/overlay/history search and bounded
    public original-source follow-up.
  accessed_at: '2026-10-21T15:19:58Z'
  support: context_only
  summary: The search found exact raw/native records, the path lock, readiness queue
    and historical E/Z ad hoc reviews. It found no exact corrective overlay in searched
    curation/conf paths. Historical reviews supplied literature leads only; their
    optional-field absence finding is not adopted. Public follow-up recovered the
    original 1986 full article,2000 metabolism abstract and2001 structural deposition.
    A separate ignored-inclusive scratch-cache search found citations and later discussions
    but no cached complete2001 original article.
  search_scope: '2026-10-21: rg --no-ignore --hidden over data, curation, conf, scripts,
    src, docs, .claude, reviews and reports for CHEBI:48935, full native key and e-roxithromycin;
    separate ignored-inclusive scratch search for DOI35101544 and original paper title.
    Public searches used exact identifiers, E/Z roxithromycin, adopted PMIDs, original
    1986 antibacterial title and original 2001 ribosome DOI. No paid source was used.'
  snapshot_sha256: 96245d7a16a683045f3d64030d9a6e326ca05ffd6e5568ed398ce5b057e61260
- evidence_id: validation
  kind: validation
  reference: 387-schema.log; 387-strict.log; 387-chemistry.json; 387-xref-chemistry.json
  locator: Actual focused checks and independent chemistry, with captured-input hash
    recheck.
  accessed_at: '2026-10-21T15:19:58Z'
  support: supports
  summary: Focused schema, strict, chemistry and exact authority-graph checks all
    passed. Validation establishes structural consistency, not scientific proof by
    itself.
  snapshot_sha256: 4a59b9faa2fb756632b165db4169151c4f74733300026d3713c21647acfb2939
assessments:
- assessment_id: identity
  area: identity
  topic: Exact E graph, names and structure hierarchy
  outcome: supported
  summary: Native encodings and all successfully inspected official structure endpoints
    agree, including all eighteen assigned centres and oxime E geometry. The parent
    leaves that geometry unspecified and is broader. INN language variants and the
    E-specific chemical synonyms are traceable to current ChEBI.
  target_ids:
  - CHEBI:48935
  evidence_ids:
  - native
  - chebi
  - parent
  - official-graph
  - ccd
  - cas
  - drugcentral
  - validation
- assessment_id: xref
  area: identity
  topic: External chemical cross references
  outcome: unknown
  summary: DrugCentral, RCSB ROX and public CAS-linked PubChem structure checks support
    the native identity. HMDB and proprietary Beilstein/Reaxys exact structures remain
    uninspected after bounded free attempts. DrugCentral has an ancillary conflicting
    Z ChEBI pointer, but its actual graph is exact E. No native xref mismatch was
    established.
  target_ids:
  - CHEBI:48935
  evidence_ids:
  - drugcentral
  - ccd
  - cas
  - remaining-xrefs
- assessment_id: activity
  area: evidence
  topic: Antimicrobial roles and primary exact-form activity
  outcome: supported
  summary: The inherited ChEBI antimicrobial and antibacterial-drug roles are retained
    correctly. The original supplied RU 28965 experiment depicts the E compound and
    provides direct antibacterial evidence. Exact-form registry and metabolism evidence
    reinforce the ordinary drug-name mapping; no statement of perfect isomeric purity
    or individual-strain MIC is fabricated.
  target_ids:
  - CHEBI:48935
  evidence_ids:
  - owners
  - chebi
  - parent
  - original-antibacterial
  - exact-form-context
- assessment_id: mechanism
  area: evidence
  topic: Mode-of-action review and optional biological fields
  outcome: supported
  summary: The exact ROX ribosome deposition supports a bounded ribosomal mechanism
    follow-up. The native makes no direct protein, gene, regulator, response or transcriptomic
    claim, so a structured iModulon adapter is not applicable to its asserted fields.
    No empty optional target, resistance, graph, activity, producer or dataset slot
    is treated as a corrective defect.
  target_ids:
  - CHEBI:48935
  evidence_ids:
  - native
  - ribosome
  - original-antibacterial
- assessment_id: citations
  area: evidence
  topic: All adopted citation dispositions
  outcome: unknown
  summary: PMID12575424 is accessible only as title/index metadata and concerns host
    cytokines. PMID24462419 was read at complete abstract depth and concerns clinical
    symptom outcomes. Neither was silently used as direct bacterial target or MIC
    evidence; independent original studies support the biological classification.
  target_ids:
  - CHEBI:48935
  evidence_ids:
  - adopted-th2
  - adopted-clinical
  - original-antibacterial
  - ribosome
- assessment_id: provenance
  area: provenance
  topic: Generated ownership, history and whole-record coverage
  outcome: supported
  summary: The exact source row, role inheritance, synonym/xref mappings, source version,
    alias and all history events are consistent. All original hashes are preserved.
    SEEDED remains the native status, and the scientific review does not claim a curation
    mutation or completed native sign-off.
  target_ids:
  - CHEBI:48935
  evidence_ids:
  - owners
  - native
  - search
  - validation
findings: []
actions: []
limitations:
- HMDB page/XML/molfile access returned403; exact HMDB structure was not independently
  inspected. Beilstein and Reaxys records were not accessed. The public CAS query
  checks the association through PubChem, not a proprietary CAS Registry record.
- The 2001 structural study was read at complete indexed abstract and original PDB
  deposition depth. Its publisher PDF URL returned 3038 bytes of HTML, not a PDF;
  detailed full-paper contacts and density were not reanalyzed.
- Adopted PMID12575424 has no indexed abstract and its full Japanese article was not
  obtained. Adopted PMID24462419 was read at complete original abstract depth, with
  publisher and author-university bibliographic checks; no exact material or microbiological
  endpoint is inferred from that clinical pilot.
- The complete 1986 main article was read, with original Figure 1, methods and Table
  1 visually checked. It depicts exact E-roxithromycin and identifies supplier material
  but does not quantify E/Z purity. Population MIC summaries are not individual-strain
  observations.
- The 2000 metabolism paper was assessed at complete original abstract depth. It is
  used only for the explicit E starting-form versus Z-metabolite distinction.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No corrective finding was established. Optional future mechanism or activity enrichment
  should attach evidence to each claim and retain exact structure, organism, strain
  or population, medium and endpoint boundaries.
- The ancillary DrugCentral Z-isomer link should not override its independently checked
  E molecular encodings. No cross-record merger or structure replacement is justified
  by that internal link alone.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
