# Lapachol: valid native quinone with bounded biological and historical evidence

- Review: 20261021T193803Z-lapachol-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T19:16:35Z
- Finished UTC: 2026-10-21T19:38:03Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The native hydroxy-1,4-naphthoquinone is valid and supported by current exact authorities. The different PubChem name-result key represents an alternative tautomer and is not an asserted native xref. Original abstracts support antibacterial and preclinical anticancer activity. No confirmed native defect is established; historical first-isolation detail, HMDB equivalence and full experimental Methods remain explicit limits. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position593; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:6377 | data/antibiotics/antibacterial/lapachol.yaml | generated | lapachol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:6377 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:6377 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:6377 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:6377 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:6377 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:6377 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:6377 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:6377 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:6377 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:6377 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:6377 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:6377 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Native tautomer, composition and structural scope

identity: supported. Targets: CHEBI:6377.

The native p-quinone is supported by multiple exact authorities. A broader preferred-name PubChem tautomer differs but is not an asserted native xref; tautomer handling must precede any identity-alarm claim.

### All reference namespaces, synonyms and ontology terms

grounding: unknown. Targets: CHEBI:6377.

CAS, ChemSpider, KEGG and KNApSAcK support the native graph. HMDB exact equivalence and ultimate historical scope of source names remain unverified. Current NIST names preclude declaring wood aliases erroneous solely from their wording.

### Coarse biological properties versus historical detail

evidence: unknown. Targets: CHEBI:6377.

Original abstracts support antibacterial and preclinical anticancer properties. The first-isolation date/tissue remains source-attributed and historically unverified; the native does not assert clinical efficacy.

### Organism-specific mechanism and evidence tiers

evidence: supported. Targets: CHEBI:6377.

The strongest inspected antibacterial primary abstract supports oxidative stress and protective pathways. Direct binding, computed chelation, yeast interpretation, delivery-system effects and other quinones remain separate. Missing optional target/graph objects are not defects.

### Entire-record and adopted-source coverage

provenance: supported. Targets: CHEBI:6377.

All populated native fields, all ten adopted papers and actual source owners are dispositioned. Original captured hashes, deterministic mint and generation history remain intact.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optional exact-source follow-up before unrestricted sign-off or quantitative enrichment.

- Obtain original historical evidence before revising or affirming the1882 first-isolation date, plant attribution and bark tissue.
- Inspect full antibacterial Methods and exact tables before adding strains, MICs, mutant effects or causal edges; retain oxygen, pH and formulation qualifiers.
- Verify HMDB independently if public access becomes available. Preserve the chosen quinone representation and distinguish exact graph equivalence from tautomer-family equivalence.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/lapachol.yaml; Entire native YAML: definition, sixteen exact names, both parents, role, chemistry, five chemical references, document link, source concept and four history events. | supports | CHEBI6377 is neutral C15H14O3, key CIEYTVIYYGTCCI-UHFFFAOYSA-N. The prenyl alkene has two identical terminal methyl substituents and therefore no omitted E/Z stereochemistry. No chiral centre is present. Native fields assert coarse antibacterial/anticancer properties and historical origin but no MIC, direct target, resistance, clinical indication or causal graph. |
| owners | data/raw/chebi_antimicrobials.tsv:208;conf/sources.yaml;scripts/extract_source_inventory.py;scripts/seed_from_sources.py; Complete adopted row and relevant exact/document-reference routing; ignored/hidden-inclusive owner searches. | supports | The adopted ChEBI row owns identity, all names, terms, links and ten PMID leads. Citation leads are deliberately not emitted as claim-level evidence. The mint recomputes antibioticmech:chebi-63264ba58d; four seed/reseed events describe generation. No exact curator/decision overlay was found in the inspected searches, which included ignored files. Original thirteen input hashes remain intact. |
| authorities | CHEBI:6377;KEGG:C10366;KNApSAcK:C00002835;ChemSpider:10770962; Complete official ChEBI, KEGG and KNApSAcK responses; ChemSpider rendered-page embedded JSON structural properties. | supports | Both native serializations and current ChEBI, KEGG molfile, KNApSAcK InChI and ChemSpider SMILES/Standard InChI reproduce the native full key. The accurate composition is C15H14O3, charge0, calculated exact mass242.09429431, average242.274. Hydroxy-1,4-naphthoquinone and prenylquinone parents agree with the graph. No native PubChem xref is asserted. |
| tautomer | PubChem:3884;593-tautomer-diagnostic.json; Independent parsing of the PubChem name result and exact ChemSpider page, followed by canonical-tautomer comparison. | supports | PubChem name/lapachol resolves a hydroxy-1,2-quinone tautomer with key CWPGNVFCJOPXFB-UHFFFAOYSA-N. Its hydrogen location and carbonyl placement differ from the native p-quinone; both canonicalize to the same tautomer family in the diagnostic. This calculation does not establish solution populations or justify replacing the native representation. The matching ChemSpider exact reference was verified from its actual structural data, despite separate obsolete API routes failing. |
| cas-names | https://webbook.nist.gov/cgi/cbook.cgi?ID=C84797; Complete NIST Chemistry WebBook entry: CAS, Standard InChI/key and historical names. | supports | NIST directly associates CAS84-79-7 with the native full key and includes the wood-related, colour-index, greenhartin, taiguic-acid and tecomin aliases among chemical historical names. Thus their appearance alone does not establish a wrong-material synonym. Exact historical linguistic scope was not independently reconstructed. The CAS registry API required authorization and was not treated as an inspected licensed registry. |
| remaining-links | HMDB:HMDB0253978;https://en.wikipedia.org/wiki/Lapachol; Current ChEBI attribution, attempted HMDB page/XML and Wikipedia topic page. | unknown | HMDB page/XML access returned403, leaving independent exact equivalence unknown. Wikipedia is correctly stored as a document reference. Its alternative-tautomer SMILES is not a native exact chemical mapping and does not disprove the selected ChEBI graph. |
| staph2020 | PMID:32712193;DOI:10.1016/j.freeradbiomed.2020.07.025; Complete original indexed abstract; bounded publisher/repository full-text attempts did not yield a readable main article. | supports | The study reports S. aureus RNA-seq stress responses, BSH redox/ROS measurements, thiol oxidation and mutant phenotypes. KatA and Brx/BSH/YpdA protect against lapachol stress; GapDH/HypR oxidation is an observed response, not proof of direct drug binding. NAC and microaerophilic growth improve survival. The authors found no irreversible protein alkylation/aggregation. These findings support an oxidative antibacterial mechanism at abstract depth, without asserting native target objects or uninspected quantitative assays. |
| tb2020 | PMID:33275860;DOI:10.1089/mdr.2020.0164; Complete original abstract. | supports | Lapachol and beta-lapachone were tested against M. tuberculosis and clinical isolates at neutral/acidic pH and in combinations. Lapachol activity/selectivity improved in acidic conditions and with NAC. The explicitly synergistic beta-lapachone-plus-NAC result cannot automatically be transferred to lapachol. No exact MIC/strain row is imported without full Methods. |
| host2020 | PMID:31935485 DOI:10.1016/j.tiv.2020.104772;PMID:33019942 DOI:10.2174/1874467213666201005122230;PMID:33254016 DOI:10.1016/j.biopha.2020.110936; All three complete original abstracts. | supports | The HL60 study includes parent lapachol IC50 25 micromolar, whereas glycosides are more potent and activate caspases that parent lapachol did not activate. The fibrosarcoma study measures cell invasion and MMP-related responses rather than clinical benefit. The breast-cancer study tests a lapachol-loaded nanoemulsion and compares free drug; delivery-system efficacy must retain that material boundary. These preclinical findings support coarse anticancer properties without claiming proven human treatment. |
| protozoa | PMID:11180522 DOI:10.1002/1099-1573(200102)15:1&lt;44::AID-PTR685&gt;3.0.CO;2-1;PMID:30797783 DOI:10.1016/j.exppara.2019.02.013; Both complete original abstracts. | supports | The2001 study found in-vitro anti-amastigote activity but no protection from L. braziliensis lesions in hamsters at300 mg/kg/day for42 days. The2019 study found activity in different Leishmania species and murine models. Species, regimens and model boundaries explain why these outcomes cannot be collapsed into one universal efficacy claim. Neither is bacterial MIC evidence. |
| other-adopted | PMID:31183610 DOI:10.1007/s12223-019-00722-2;PMID:30896339 DOI:10.1080/10826068.2019.1591991;PMID:32318101 DOI:10.1155/2020/2103239; All three complete original abstracts. | supports | The yeast study names the alternative quinone tautomer and interprets glutathione depletion/oxidative stress, with initial alkylation proposed; this is a different organism and evidence context from the S. aureus study. Fungal biotransformation generates norlapachol, isolapachol and secondary metabolites whose activities cannot be assigned wholesale to parent lapachol. The Fe2+ complexation paper is DFT/QTAIM computation, not experimental bacterial binding evidence. |
| adapter | kg-microbe-sources imodulondb;S. aureus/staph_precise108; Actual four structured-adapter search executions and returned tables; all exits0. | supports | katA maps to USA300HOU_RS06785 and ypdA to USA300HOU_RS07580 in the selected context. PerR returns gene USA300HOU_RS10095 and oxidative-stress iModulon27. The lapachol query returns no matching genes or iModulons in this dataset. These are contextual annotations, not evidence of compound exposure, direct target binding, or absence of a mechanism outside this dataset. |
| history-search | 593-discovery.json;593-discovery-refined.json;593-local-hits.txt;593-owner-hits.txt;DOI:10.1039/CT8926100611; Bounded title/metadata screening, all ten adopted abstracts, current authority follow-up and attempted historical original. | context_only | The first-isolation1882/bark/Tabebuia statement is repeated by current ChEBI but was not independently verified from an original historical publication. Conflicting later summaries are insufficient to establish a replacement date or tissue. The attempted1892 Hooker original was inaccessible. Broad searches include numerous beta-lapachone, derivative and unrelated quinone studies; only bounded selected exact-lapachol leads were examined, not all hits. Modern human-target or photodynamic experiments require their own organism/material/light qualifiers. |

## Limits And Additional Notes

- All ten adopted original abstracts were read completely, but full biological articles were not obtained or fully audited. Publisher403 responses and repeated repository timeouts are retained; an OpenAlex graphical-abstract image is not a full paper.
- The original historical isolation statement and HMDB exact link remain unverified. Database agreement does not by itself establish a precise historical date or tissue.
- The structured adapter is context only. Search screening was bounded; no all-literature coverage, clinical efficacy or direct molecular binding is asserted.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All13 original input hashes remain unchanged. No native scientific field or status changed; full-QC disposition is attached during finalization.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T193803Z-lapachol-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Lapachol: valid native quinone with bounded biological and historical evidence'
started_at: '2026-10-21T19:16:35Z'
finished_at: '2026-10-21T19:38:03Z'
reviewer:
  identity: Codex
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
summary: The native hydroxy-1,4-naphthoquinone is valid and supported by current exact
  authorities. The different PubChem name-result key represents an alternative tautomer
  and is not an asserted native xref. Original abstracts support antibacterial and
  preclinical anticancer activity. No confirmed native defect is established; historical
  first-isolation detail, HMDB equivalence and full experimental Methods remain explicit
  limits. Scientific assessment retains the stated evidence limits; full verification
  is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/lapachol.yaml
    sha256: 77d29f530d6eaabb51ed398331fb85fce52c5c17bdc209e628d5a50b589776f2
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
- target_id: CHEBI:6377
  path: data/antibiotics/antibacterial/lapachol.yaml
  label: lapachol
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
  selection: Initially uncovered queue position593; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:6377
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:6377
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    593
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:6377
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/lapachol.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:6377
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/lapachol.yaml --out /private/tmp/am-review-session/593-strict.tsv
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
  - CHEBI:6377
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
  - CHEBI:6377
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
  - CHEBI:6377
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
  - CHEBI:6377
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
  - CHEBI:6377
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
  - CHEBI:6377
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
  - CHEBI:6377
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
  - CHEBI:6377
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
  - CHEBI:6377
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/lapachol.yaml
  locator: 'Entire native YAML: definition, sixteen exact names, both parents, role,
    chemistry, five chemical references, document link, source concept and four history
    events.'
  accessed_at: '2026-10-21T19:36:04Z'
  support: supports
  summary: CHEBI6377 is neutral C15H14O3, key CIEYTVIYYGTCCI-UHFFFAOYSA-N. The prenyl
    alkene has two identical terminal methyl substituents and therefore no omitted
    E/Z stereochemistry. No chiral centre is present. Native fields assert coarse
    antibacterial/anticancer properties and historical origin but no MIC, direct target,
    resistance, clinical indication or causal graph.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv:208;conf/sources.yaml;scripts/extract_source_inventory.py;scripts/seed_from_sources.py
  locator: Complete adopted row and relevant exact/document-reference routing; ignored/hidden-inclusive
    owner searches.
  accessed_at: '2026-10-21T19:36:04Z'
  support: supports
  summary: The adopted ChEBI row owns identity, all names, terms, links and ten PMID
    leads. Citation leads are deliberately not emitted as claim-level evidence. The
    mint recomputes antibioticmech:chebi-63264ba58d; four seed/reseed events describe
    generation. No exact curator/decision overlay was found in the inspected searches,
    which included ignored files. Original thirteen input hashes remain intact.
  snapshot_sha256: 77581e38ad2eee1444e54c48460167a1bc2b050c30142784fddd4760238019f3
- evidence_id: authorities
  kind: authority
  reference: CHEBI:6377;KEGG:C10366;KNApSAcK:C00002835;ChemSpider:10770962
  locator: Complete official ChEBI, KEGG and KNApSAcK responses; ChemSpider rendered-page
    embedded JSON structural properties.
  accessed_at: '2026-10-21T19:36:04Z'
  support: supports
  summary: Both native serializations and current ChEBI, KEGG molfile, KNApSAcK InChI
    and ChemSpider SMILES/Standard InChI reproduce the native full key. The accurate
    composition is C15H14O3, charge0, calculated exact mass242.09429431, average242.274.
    Hydroxy-1,4-naphthoquinone and prenylquinone parents agree with the graph. No
    native PubChem xref is asserted.
  snapshot_sha256: 6f9b4e94c432a0bd143e5b917f2a813453d7d1b99f3fe8566184323158a72479
- evidence_id: tautomer
  kind: validation
  reference: PubChem:3884;593-tautomer-diagnostic.json
  locator: Independent parsing of the PubChem name result and exact ChemSpider page,
    followed by canonical-tautomer comparison.
  accessed_at: '2026-10-21T19:36:04Z'
  support: supports
  summary: PubChem name/lapachol resolves a hydroxy-1,2-quinone tautomer with key
    CWPGNVFCJOPXFB-UHFFFAOYSA-N. Its hydrogen location and carbonyl placement differ
    from the native p-quinone; both canonicalize to the same tautomer family in the
    diagnostic. This calculation does not establish solution populations or justify
    replacing the native representation. The matching ChemSpider exact reference was
    verified from its actual structural data, despite separate obsolete API routes
    failing.
  snapshot_sha256: de0695471f38da937cae6b0ee31de20de51d39ee8a0046c0d489f914584b9ef7
- evidence_id: cas-names
  kind: authority
  reference: https://webbook.nist.gov/cgi/cbook.cgi?ID=C84797
  locator: 'Complete NIST Chemistry WebBook entry: CAS, Standard InChI/key and historical
    names.'
  accessed_at: '2026-10-21T19:36:04Z'
  support: supports
  summary: NIST directly associates CAS84-79-7 with the native full key and includes
    the wood-related, colour-index, greenhartin, taiguic-acid and tecomin aliases
    among chemical historical names. Thus their appearance alone does not establish
    a wrong-material synonym. Exact historical linguistic scope was not independently
    reconstructed. The CAS registry API required authorization and was not treated
    as an inspected licensed registry.
  snapshot_sha256: d7c6906fe2851c4e71b5f5190b321ef8a7501220ae597da4cbca7f2d9827d6a7
- evidence_id: remaining-links
  kind: authority
  reference: HMDB:HMDB0253978;https://en.wikipedia.org/wiki/Lapachol
  locator: Current ChEBI attribution, attempted HMDB page/XML and Wikipedia topic
    page.
  accessed_at: '2026-10-21T19:36:04Z'
  support: unknown
  summary: HMDB page/XML access returned403, leaving independent exact equivalence
    unknown. Wikipedia is correctly stored as a document reference. Its alternative-tautomer
    SMILES is not a native exact chemical mapping and does not disprove the selected
    ChEBI graph.
  snapshot_sha256: 0b8d6ca5a86180a4bd622899f5abea44144bfbb09d4dd19d416876cd656d295d
- evidence_id: staph2020
  kind: primary_source
  reference: PMID:32712193;DOI:10.1016/j.freeradbiomed.2020.07.025
  locator: Complete original indexed abstract; bounded publisher/repository full-text
    attempts did not yield a readable main article.
  accessed_at: '2026-10-21T19:36:04Z'
  support: supports
  summary: The study reports S. aureus RNA-seq stress responses, BSH redox/ROS measurements,
    thiol oxidation and mutant phenotypes. KatA and Brx/BSH/YpdA protect against lapachol
    stress; GapDH/HypR oxidation is an observed response, not proof of direct drug
    binding. NAC and microaerophilic growth improve survival. The authors found no
    irreversible protein alkylation/aggregation. These findings support an oxidative
    antibacterial mechanism at abstract depth, without asserting native target objects
    or uninspected quantitative assays.
  snapshot_sha256: 617a1f86f6d4b9db6bb8be961dded72ee817fdbd146b8d8f268866bc9a49fca7
- evidence_id: tb2020
  kind: primary_source
  reference: PMID:33275860;DOI:10.1089/mdr.2020.0164
  locator: Complete original abstract.
  accessed_at: '2026-10-21T19:36:04Z'
  support: supports
  summary: Lapachol and beta-lapachone were tested against M. tuberculosis and clinical
    isolates at neutral/acidic pH and in combinations. Lapachol activity/selectivity
    improved in acidic conditions and with NAC. The explicitly synergistic beta-lapachone-plus-NAC
    result cannot automatically be transferred to lapachol. No exact MIC/strain row
    is imported without full Methods.
  snapshot_sha256: 617a1f86f6d4b9db6bb8be961dded72ee817fdbd146b8d8f268866bc9a49fca7
- evidence_id: host2020
  kind: primary_source
  reference: PMID:31935485 DOI:10.1016/j.tiv.2020.104772;PMID:33019942 DOI:10.2174/1874467213666201005122230;PMID:33254016
    DOI:10.1016/j.biopha.2020.110936
  locator: All three complete original abstracts.
  accessed_at: '2026-10-21T19:36:04Z'
  support: supports
  summary: The HL60 study includes parent lapachol IC50 25 micromolar, whereas glycosides
    are more potent and activate caspases that parent lapachol did not activate. The
    fibrosarcoma study measures cell invasion and MMP-related responses rather than
    clinical benefit. The breast-cancer study tests a lapachol-loaded nanoemulsion
    and compares free drug; delivery-system efficacy must retain that material boundary.
    These preclinical findings support coarse anticancer properties without claiming
    proven human treatment.
  snapshot_sha256: 617a1f86f6d4b9db6bb8be961dded72ee817fdbd146b8d8f268866bc9a49fca7
- evidence_id: protozoa
  kind: primary_source
  reference: PMID:11180522 DOI:10.1002/1099-1573(200102)15:1<44::AID-PTR685>3.0.CO;2-1;PMID:30797783
    DOI:10.1016/j.exppara.2019.02.013
  locator: Both complete original abstracts.
  accessed_at: '2026-10-21T19:36:04Z'
  support: supports
  summary: The2001 study found in-vitro anti-amastigote activity but no protection
    from L. braziliensis lesions in hamsters at300 mg/kg/day for42 days. The2019 study
    found activity in different Leishmania species and murine models. Species, regimens
    and model boundaries explain why these outcomes cannot be collapsed into one universal
    efficacy claim. Neither is bacterial MIC evidence.
  snapshot_sha256: 617a1f86f6d4b9db6bb8be961dded72ee817fdbd146b8d8f268866bc9a49fca7
- evidence_id: other-adopted
  kind: primary_source
  reference: PMID:31183610 DOI:10.1007/s12223-019-00722-2;PMID:30896339 DOI:10.1080/10826068.2019.1591991;PMID:32318101
    DOI:10.1155/2020/2103239
  locator: All three complete original abstracts.
  accessed_at: '2026-10-21T19:36:04Z'
  support: supports
  summary: The yeast study names the alternative quinone tautomer and interprets glutathione
    depletion/oxidative stress, with initial alkylation proposed; this is a different
    organism and evidence context from the S. aureus study. Fungal biotransformation
    generates norlapachol, isolapachol and secondary metabolites whose activities
    cannot be assigned wholesale to parent lapachol. The Fe2+ complexation paper is
    DFT/QTAIM computation, not experimental bacterial binding evidence.
  snapshot_sha256: 617a1f86f6d4b9db6bb8be961dded72ee817fdbd146b8d8f268866bc9a49fca7
- evidence_id: adapter
  kind: database
  reference: kg-microbe-sources imodulondb;S. aureus/staph_precise108
  locator: Actual four structured-adapter search executions and returned tables; all
    exits0.
  accessed_at: '2026-10-21T19:36:04Z'
  support: supports
  summary: katA maps to USA300HOU_RS06785 and ypdA to USA300HOU_RS07580 in the selected
    context. PerR returns gene USA300HOU_RS10095 and oxidative-stress iModulon27.
    The lapachol query returns no matching genes or iModulons in this dataset. These
    are contextual annotations, not evidence of compound exposure, direct target binding,
    or absence of a mechanism outside this dataset.
  snapshot_sha256: 324524787308fa4ed8f274fb74b917b003af9aa08019d609aaa03c3606f3f9ac
- evidence_id: history-search
  kind: search
  reference: 593-discovery.json;593-discovery-refined.json;593-local-hits.txt;593-owner-hits.txt;DOI:10.1039/CT8926100611
  locator: Bounded title/metadata screening, all ten adopted abstracts, current authority
    follow-up and attempted historical original.
  accessed_at: '2026-10-21T19:36:04Z'
  support: context_only
  summary: The first-isolation1882/bark/Tabebuia statement is repeated by current
    ChEBI but was not independently verified from an original historical publication.
    Conflicting later summaries are insufficient to establish a replacement date or
    tissue. The attempted1892 Hooker original was inaccessible. Broad searches include
    numerous beta-lapachone, derivative and unrelated quinone studies; only bounded
    selected exact-lapachol leads were examined, not all hits. Modern human-target
    or photodynamic experiments require their own organism/material/light qualifiers.
  search_scope: 2026-10-21; lapachol exact label, CHEBI6377, full key, all ten adopted
    PMIDs, primary2020 mechanism DOI and historical1892 DOI; local searches included
    ignored/hidden files.
  snapshot_sha256: e8063f1110ffa04eaa320a32c3afe3701bde95a2016af9988cca25d1aa9f800a
assessments:
- assessment_id: identity
  area: identity
  topic: Native tautomer, composition and structural scope
  outcome: supported
  summary: The native p-quinone is supported by multiple exact authorities. A broader
    preferred-name PubChem tautomer differs but is not an asserted native xref; tautomer
    handling must precede any identity-alarm claim.
  target_ids:
  - CHEBI:6377
  evidence_ids:
  - native
  - authorities
  - tautomer
- assessment_id: grounding
  area: grounding
  topic: All reference namespaces, synonyms and ontology terms
  outcome: unknown
  summary: CAS, ChemSpider, KEGG and KNApSAcK support the native graph. HMDB exact
    equivalence and ultimate historical scope of source names remain unverified. Current
    NIST names preclude declaring wood aliases erroneous solely from their wording.
  target_ids:
  - CHEBI:6377
  evidence_ids:
  - authorities
  - cas-names
  - remaining-links
- assessment_id: definition
  area: evidence
  topic: Coarse biological properties versus historical detail
  outcome: unknown
  summary: Original abstracts support antibacterial and preclinical anticancer properties.
    The first-isolation date/tissue remains source-attributed and historically unverified;
    the native does not assert clinical efficacy.
  target_ids:
  - CHEBI:6377
  evidence_ids:
  - staph2020
  - tb2020
  - host2020
  - history-search
- assessment_id: mechanism
  area: evidence
  topic: Organism-specific mechanism and evidence tiers
  outcome: supported
  summary: The strongest inspected antibacterial primary abstract supports oxidative
    stress and protective pathways. Direct binding, computed chelation, yeast interpretation,
    delivery-system effects and other quinones remain separate. Missing optional target/graph
    objects are not defects.
  target_ids:
  - CHEBI:6377
  evidence_ids:
  - staph2020
  - other-adopted
  - protozoa
  - adapter
- assessment_id: provenance
  area: provenance
  topic: Entire-record and adopted-source coverage
  outcome: supported
  summary: All populated native fields, all ten adopted papers and actual source owners
    are dispositioned. Original captured hashes, deterministic mint and generation
    history remain intact.
  target_ids:
  - CHEBI:6377
  evidence_ids:
  - native
  - owners
  - history-search
findings: []
actions:
- action_id: A1
  description: Optional exact-source follow-up before unrestricted sign-off or quantitative
    enrichment.
  finding_ids: []
  target_ids:
  - CHEBI:6377
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Maintained identity/definition/source assertions
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated native field owner
  acceptance_checks:
  - Obtain original historical evidence before revising or affirming the1882 first-isolation
    date, plant attribution and bark tissue.
  - Inspect full antibacterial Methods and exact tables before adding strains, MICs,
    mutant effects or causal edges; retain oxygen, pH and formulation qualifiers.
  - Verify HMDB independently if public access becomes available. Preserve the chosen
    quinone representation and distinguish exact graph equivalence from tautomer-family
    equivalence.
limitations:
- All ten adopted original abstracts were read completely, but full biological articles
  were not obtained or fully audited. Publisher403 responses and repeated repository
  timeouts are retained; an OpenAlex graphical-abstract image is not a full paper.
- The original historical isolation statement and HMDB exact link remain unverified.
  Database agreement does not by itself establish a precise historical date or tissue.
- The structured adapter is context only. Search screening was bounded; no all-literature
  coverage, clinical efficacy or direct molecular binding is asserted.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All13 original input hashes remain unchanged. No native scientific field or status
  changed; full-QC disposition is attached during finalization.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
