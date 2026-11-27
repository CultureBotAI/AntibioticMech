# Licorisoflavan A: supported native structure with an underspecified exact LIPID MAPS link

- Review: 20261021T194918Z-licorisoflavan-a-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T19:32:11Z
- Finished UTC: 2026-10-21T19:49:18Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The entire native record and exact ChEBI source row were assessed. Native 3R chemistry agrees with current ChEBI, an additional PubChem comparator and the adopted primary supplement. The asserted LIPID MAPS accession instead omits the single stereocentre, producing one major exact-grounding finding. Antibacterial activity and G. uralensis isolation have bounded primary support; historical naming and unavailable full methods remain qualified.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Assigned queue position 603; one exact native record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:69083 | data/antibiotics/antibacterial/licorisoflavan-a.yaml | generated | licorisoflavan A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:69083 | Actual focused execution exited 0. Executed against batch061; chemistry used the existing batch019 RDKit interpreter, native validators the batch061 environment. |
| Focused schema verification | passed | True | CHEBI:69083 | Actual focused execution exited 0. Executed against batch061; chemistry used the existing batch019 RDKit interpreter, native validators the batch061 environment. |
| Focused strict verification | passed | True | CHEBI:69083 | Actual focused execution exited 0. Executed against batch061; chemistry used the existing batch019 RDKit interpreter, native validators the batch061 environment. |
| Authoritative full QC | failed | True | CHEBI:69083 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:69083 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:69083 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:69083 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:69083 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:69083 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:69083 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:69083 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:69083 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Native identity and historical derivative nomenclature

identity: supported. Targets: CHEBI:69083.

Native constitution, 3R assignment, neutral state and numerical fields are coherent with current ChEBI/PubChem and the adopted SI drawing. Additional 1992 primary establishes constitution and positive rotation but does not itself assign C3. The historically attested 5-O-methyllicoricidin name is qualified in light of the parent structural revision, not automatically rejected.

### Exact chemical links and parent classifications

grounding: concern. Targets: CHEBI:69083.

LMPK12080046 is an underspecified chemical graph at the one native stereocentre and cannot be treated as full exact equivalence without qualification or upstream correction. This is a source-link issue; the supported native graph should not be broadened to match. All three parent definitions fit. Other registry structural access remains unresolved.

### Antibacterial eligibility and producer claim

evidence: supported. Targets: CHEBI:69083.

The adopted exact-compound abstract supports broad antibacterial activity with concentration/endpoint limits, while official SI directly supports G. uralensis isolation and compound mapping. Additional originals provide corroborating abstract-level leads, without transferring pooled MICs or host effects.

### Optional observations and mechanism enrichment

completeness: unknown. Targets: CHEBI:69083.

No required missing optional field is identified. Exact activity and producer observations may be added only with their primary material and method boundaries. No direct antibacterial protein target is established by the inspected sources.

### Source ownership and complete adopted lead disposition

provenance: supported. Targets: CHEBI:69083.

The sole adopted PMID was resolved and its abstract plus official supplement assessed. All original 13 and expanded 21 input hashes remain unchanged, with actual ChEBI extraction/seeding ownership. Three SEEDED/RESEEDED history events are coherent; no review status was altered.

## Findings

### F1: The exact LIPID MAPS link omits native C3 stereochemistry

major / open / confirmed; issue key: licorisoflavan-a-lipidmaps-unspecified-stereocentre.

Native xrefs[2] asserts LMPK12080046 for a fully specified 3R structure. Both actual registry encodings omit that centre and give GDAAEAXMNLVRCZ-UHFFFAOYSA-N rather than native GDAAEAXMNLVRCZ-SFHVURJKSA-N. Matching constitution, name and formula do not establish exact stereochemical equivalence. This is an unassigned graph, not proof of a racemate or a wrong native enantiomer.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate or qualify the underspecified LIPID MAPS exact link through maintained source ownership.

- Compare both actual registry encodings to the native 3R structure and retain the missing-stereocentre distinction.
- Remove or qualify the exact link unless a corrected exact accession is independently verified. Preserve the source association as provenance where appropriate; do not erase native stereochemistry to force agreement.
- Regenerate and rerun required validators, checking formula, masses, full InChIKey and retained exact links.

### A2

Optional primary enrichment can capture exact isolation and antibacterial observations without assigning an unsupported direct target.

- Recover adopted full assay methods before turning abstract growth-inhibition concentrations into strain-level MIC observations.
- Preserve compound 2 versus licoricidin 1 and distinguish VSC neutralization, growth inhibition, bactericidal and biofilm endpoints.
- Keep the historical methyllicoricidin naming explanation qualified until its original structure is inspected; do not infer absolute configuration solely from rotation sign.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/licorisoflavan-a.yaml; Entire record, all four synonyms, three parents, role, four xrefs and history | supports | The record denotes neutral 3R licorisoflavan A, C27H34O5, with 5/7 methoxy and 2′/4′ hydroxyl groups, two normal prenyl groups and key GDAAEAXMNLVRCZ-SFHVURJKSA-N. Definition asserts G. uralensis isolation and antibacterial activity. No separate structured target, resistance, activity spectrum, producer, product or causal graph objects occur; definition claims remain in scope. |
| owners | data/raw/chebi_antimicrobials.tsv; Exact full source row 1751 and readiness row 1536 | context_only | The actual ChEBI row reproduces native structure, naming, ontology and four xrefs, with one adopted PMID22074222. Original 13 captured hashes remain unchanged; actual owner and context capture expanded the set to 21 before detailed judgment. Source extraction and seeding are the generated owners. |
| search | /private/tmp/am-review-session/603-context-search.txt; Preserved initial local search and ignored-inclusive follow-up | context_only | Exact identifier and name searches included hidden and ignored curation, configuration, scripts and raw inventories. No exact maintained curator or decisions override was found in that scope. Related licoricidin and licoricone records were distinguished. |
| adapter | Native structured-source applicability assessment; Complete native field set and definition | context_only | No protein, pathway, regulator or transcriptomic claim is named natively. Structured iModulonDB lookup is not applicable. Host-target titles in additional discovery were not adopted as bacterial mechanisms. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/69083/; Complete current CHEBI:69083 response | supports | Current ChEBI retains the native 3R graph, formula, full key, four synonyms, all three parents and antibacterial role. It explicitly associates the 7-O-methyl functional relationship to licoricidin and PMID22074222 to G. uralensis origin. |
| lipidmaps | https://www.lipidmaps.org/rest/compound/lm_id/LMPK12080046/all/json; Complete asserted LMPK12080046 response | refutes | The entry is named 7-O-methyllicoricidin and gives licorisoflavan A as a synonym. Its actual SMILES and InChI omit C3 stereochemistry and yield GDAAEAXMNLVRCZ-UHFFFAOYSA-N, despite a positive-rotation systematic text label. It has the native constitution and formula but does not encode exact 3R identity. Undefined stereochemistry is not evidence of a racemate. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/licorisoflavan%20A/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass/JSON; Additional independent name lookup CID196831 | supports | PubChem supplies both structural encodings with the native full key, formula and 3R centre. This is an additional comparator, not an asserted native PubChem xref; LIPID MAPS also lists another CID, which is not silently substituted. |
| chemistry | /private/tmp/am-review-session/603-authority-map.json; All eight structural encodings calculated with existing batch019 RDKit against batch061 | supports | Native, current ChEBI and PubChem SMILES/InChI agree at GDAAEAXMNLVRCZ-SFHVURJKSA-N, one R centre, zero charge and C27H34O5. Both LIPID MAPS encodings instead have one unassigned centre and UHFFFAOYSA-N. Native average mass 438.564 and exact mass 438.240624 agree at supplied precision. Neither prenyl alkene has distinct substituents at both ends, so no E/Z descriptor is required. |
| term-76250 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/76250/; Previously retrieved current parent definition | supports | The native isoflavan bears ring hydroxyl groups and satisfies hydroxyisoflavans. |
| term-77002 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/77002/; Previously retrieved current parent definition | supports | The native isoflavan has two aromatic methoxy groups and satisfies methoxyisoflavan. |
| term-35618 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/35618/; Previously retrieved current term definition, actual timestamp retained | supports | Both aromatic methoxy groups satisfy the aromatic ether definition. |
| term-33282 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/33282/; Previously retrieved current term definition, actual timestamp retained | supports | The antibacterial role includes slowing bacterial growth; a direct protein target is not required. |
| registry-limits | CAS:129314-37-0; HMDB:HMDB0034184; Reaxys:5461708; Exact access attempts and current source associations | unknown | Common Chemistry returned 401, HMDB XML returned 403 and Reaxys returned 403. These registry structural contents remain uninspected. ChEBI and LIPID MAPS associations are recorded without treating propagated links as independent exact structural validation. |
| adopted2011 | PMID:22074222; DOI:10.1021/np2004775; Complete original indexed abstract | partial | Exact compound 2 is licorisoflavan A, whereas 1 is licoricidin. The abstract reports marked growth inhibition of S. mutans/S. sobrinus at 10 µg/mL, P. gingivalis at 5 µg/mL and P. intermedia at 2.5 µg/mL for 2. Only compound 1 moderately inhibited F. nucleatum at 10 µg/mL. These are abstract growth-inhibition concentrations, not relabeled strain-level MICs; strain identifiers and full experimental conditions were not recovered. |
| 2011-si | https://ndownloader.figshare.com/files/4211785; Official supplement: actual Figure S1 page 1 and Isolation pages 16–17 | supports | Compound 2 (R = CH3 in the substituent legend) has 5/7 methoxy groups, both normal prenyl groups and a stereobond consistent with native 3R. Multiple fractionation procedures explicitly recover licorisoflavan A from G. uralensis extract. Figure S1 concerns suspected copper-mediated oxidative purification artifacts, not antibacterial action. The supplement supplies identity and isolation support, not the unavailable main antibacterial table. |
| 1992-original | https://triggered.edinburgh.clockss.org/ServeContent?doi=10.3987%2Fcom-91-5951; DOI10.3987/COM-91-5951; Figure 1 p576, exact compound 12 isolation p582 and characterization p585 | partial | The original isolates licorisoflavan A 12 (0.25 g) from G. aspera roots. Its actual Figure 1 depicts native constitution but leaves C3 unassigned, unlike adjacent licoricidin 11. Exact characterization gives positive rotation +5.7° (c 0.265, MeOH), two methoxy signals and two prenyl groups. This independently supports constitution and positive rotation, but is not an independent absolute-configuration determination. Reference 14 points to the 1988 Shizuri abstract; that conference original was not recovered. |
| historical-name | PMID:1529035; DOI:10.1055/s-2006-961435; Complete indexed original metadata; publisher body is an access challenge | context_only | The 1992 original title explicitly uses 5-O-methyllicoricidin from G. uralensis. Indexed metadata associates CAS129314-37-0. No abstract is supplied and the publisher HTTP200 body is a challenge page, so its actual structure and benzodiazepine-binding experiments were not inspected. It establishes historical name usage, not a bacterial target. |
| mesh-name | https://meshb.nlm.nih.gov/record/ui?ui=C076768; Complete NLM supplementary concept C076768 | context_only | NLM links 5-O-methyllicoricidin to CAS129314-37-0 and the 1992 original. This corroborates attested naming without independently verifying that inaccessible source drawing. |
| licoricidin-revision | DOI:10.3987/COM-88-4650; Previously read full 1988 licoricidin revision, actual Figure 1/Table 1 and NOE/CD text | context_only | The authentic-material revision changed the original licoricidin proposal from 7-methoxy/5-hydroxy to 5-methoxy/7-hydroxy. Thus methylating the old proposed 5-OH or the corrected 7-OH leads to the same dimethoxy constitution. This provides a plausible historical explanation for both derivative names, but the inaccessible 1992 naming paper was not represented as confirming that explanation. No required synonym correction is established solely from modern parent locants. |
| additional-activity | PMID:24479468; PMID:22368239; PMID:25531232; Complete indexed original abstracts in bounded discovery results | partial | The 2014 original explicitly includes licorisoflavan A 2 in P. gingivalis testing but gives a pooled MIC range across compounds; no exact individual value is transferred. The 2012 volatile-sulfur study likewise supplies a pooled growth MIC range and an exact 10 µg/mL licorisoflavan A VSC result; neutralization and growth endpoints are distinct. The 2015 Caries Research abstract reports purified licorisoflavan A among three flavonoids with bactericidal effects on S. mutans UA159 at ≥4 µg/mL and biofilm inhibition over 4 µg/mL; full methods/material stereopurity were not inspected. These are corroborating leads, not complete numerical annotations. |
| additional-boundaries | PMID:25963162; PMID:20722535; PMID:31278631; Complete indexed abstracts only | context_only | The G. iconica study reports ECD assignments for licorisoflavan A 4 but the abstract does not give its configuration or exact MIC; its 3S licoricidin comparator must not be merged with native 3R material. Macrophage cytokine/MMP and mouse antidepressant experiments are host assays, not bacterial growth or direct antibacterial target evidence. |
| access | /private/tmp/am-review-session/603-fetch2.json; Actual retrieval outcomes and source-reading boundary | context_only | The 1992 Heterocycles primary PDF was recovered; exact compound 12 sections, Figure 1 and references were inspected, not every unrelated glyasperin derivation. The 1992 naming-paper HTTP200 response was only a challenge. Adopted 2011 main remained unavailable after the retained 600-2011-main.html HTTP403 attempt, while its official supplement was readable. |

## Limits And Additional Notes

- CAS Common Chemistry returned 401, HMDB XML and Reaxys 403. Their exact registry structural content was not independently validated.
- Adopted 2011 main remained unavailable after a recorded 403 response. Its complete abstract and official SI Figure S1/isolation sections were read. Abstract growth-inhibition concentrations are not complete strain-level MIC annotations.
- The additional 1992 primary was read for exact compound 12, actual Figure 1, isolation, characterization and referenced origins, not all other compounds. Its figure leaves C3 unspecified; positive rotation alone was not used to assign absolute configuration. Raw spectra were not reprocessed.
- The historical 1992 naming paper has no indexed abstract and its publisher page was only an access challenge. NLM and indexed metadata attest the name/CAS association; its structural drawing was not inspected. The 1988 conference original was not recovered.
- Additional antibacterial and host-effect originals were read only through complete indexed abstracts. Pooled activity ranges, unspecified G. iconica stereochemistry, host responses and mechanism hypotheses were not promoted to exact native assertions.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All original 13 and expanded 21 input hashes were verified unchanged. Only scratch evidence and an unsaved draft were created; native/source files, history, progress and Git were not modified.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T194918Z-licorisoflavan-a-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Licorisoflavan A: supported native structure with an underspecified exact
  LIPID MAPS link'
started_at: '2026-10-21T19:32:11Z'
finished_at: '2026-10-21T19:49:18Z'
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
verdict: needs_curation
scientific_review: true
summary: The entire native record and exact ChEBI source row were assessed. Native
  3R chemistry agrees with current ChEBI, an additional PubChem comparator and the
  adopted primary supplement. The asserted LIPID MAPS accession instead omits the
  single stereocentre, producing one major exact-grounding finding. Antibacterial
  activity and G. uralensis isolation have bounded primary support; historical naming
  and unavailable full methods remain qualified.
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
  - path: data/antibiotics/antibacterial/licorisoflavan-a.yaml
    sha256: 6530901b4c1ec61e21d693b0220ebb93e2462672a7503a79de9c47a22bf5ef5a
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
  - path: curation/record_review_queue.tsv
    sha256: 3828a5120b892ee0ee0b776affc6c3e4f1f1a3355ec4edd30e6005762de00e70
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
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
targets:
- target_id: CHEBI:69083
  path: data/antibiotics/antibacterial/licorisoflavan-a.yaml
  label: licorisoflavan A
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
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Assigned queue position 603; one exact native record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:69083
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0. Executed against batch061; chemistry
    used the existing batch019 RDKit interpreter, native validators the batch061 environment.
  target_ids:
  - CHEBI:69083
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    603
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Executed against batch061; chemistry
    used the existing batch019 RDKit interpreter, native validators the batch061 environment.
  target_ids:
  - CHEBI:69083
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/licorisoflavan-a.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Executed against batch061; chemistry
    used the existing batch019 RDKit interpreter, native validators the batch061 environment.
  target_ids:
  - CHEBI:69083
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/licorisoflavan-a.yaml --out /private/tmp/am-review-session/603-strict.tsv
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
  - CHEBI:69083
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
  - CHEBI:69083
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
  - CHEBI:69083
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
  - CHEBI:69083
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
  - CHEBI:69083
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
  - CHEBI:69083
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
  - CHEBI:69083
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
  - CHEBI:69083
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
  - CHEBI:69083
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/licorisoflavan-a.yaml
  locator: Entire record, all four synonyms, three parents, role, four xrefs and history
  accessed_at: '2026-10-21T19:47:17Z'
  support: supports
  summary: The record denotes neutral 3R licorisoflavan A, C27H34O5, with 5/7 methoxy
    and 2′/4′ hydroxyl groups, two normal prenyl groups and key GDAAEAXMNLVRCZ-SFHVURJKSA-N.
    Definition asserts G. uralensis isolation and antibacterial activity. No separate
    structured target, resistance, activity spectrum, producer, product or causal
    graph objects occur; definition claims remain in scope.
  snapshot_sha256: 6530901b4c1ec61e21d693b0220ebb93e2462672a7503a79de9c47a22bf5ef5a
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Exact full source row 1751 and readiness row 1536
  accessed_at: '2026-10-21T19:47:17Z'
  support: context_only
  summary: The actual ChEBI row reproduces native structure, naming, ontology and
    four xrefs, with one adopted PMID22074222. Original 13 captured hashes remain
    unchanged; actual owner and context capture expanded the set to 21 before detailed
    judgment. Source extraction and seeding are the generated owners.
  snapshot_sha256: 6fa189b5b7aa391e35c4672bcbfd7c45db96ff9d0650724f68fa4f6322038676
- evidence_id: search
  kind: search
  reference: /private/tmp/am-review-session/603-context-search.txt
  locator: Preserved initial local search and ignored-inclusive follow-up
  accessed_at: '2026-10-21T19:47:17Z'
  support: context_only
  summary: Exact identifier and name searches included hidden and ignored curation,
    configuration, scripts and raw inventories. No exact maintained curator or decisions
    override was found in that scope. Related licoricidin and licoricone records were
    distinguished.
  snapshot_sha256: cbaeb8c6addcac63f10b05ae499702c3076d2a49b194787dc614ca0d730bd2b7
  search_scope: Preserved 603-local-hits plus rg --no-ignore --hidden -n -i for CHEBI:69083
    and licorisoflavan A in curation, conf, scripts and data/raw.
- evidence_id: adapter
  kind: search
  reference: Native structured-source applicability assessment
  locator: Complete native field set and definition
  accessed_at: '2026-10-21T19:47:17Z'
  support: context_only
  summary: No protein, pathway, regulator or transcriptomic claim is named natively.
    Structured iModulonDB lookup is not applicable. Host-target titles in additional
    discovery were not adopted as bacterial mechanisms.
  snapshot_sha256: 6530901b4c1ec61e21d693b0220ebb93e2462672a7503a79de9c47a22bf5ef5a
  search_scope: Full native definition, ontology links and fields checked for named
    protein/pathway assertions.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/69083/
  locator: Complete current CHEBI:69083 response
  accessed_at: '2026-10-21T19:44:13.533677Z'
  support: supports
  summary: Current ChEBI retains the native 3R graph, formula, full key, four synonyms,
    all three parents and antibacterial role. It explicitly associates the 7-O-methyl
    functional relationship to licoricidin and PMID22074222 to G. uralensis origin.
  snapshot_sha256: 54fc82844678a63af0405692d2f4f987fda2927f8248ae0b4bbeb680a4ab32e6
- evidence_id: lipidmaps
  kind: authority
  reference: https://www.lipidmaps.org/rest/compound/lm_id/LMPK12080046/all/json
  locator: Complete asserted LMPK12080046 response
  accessed_at: '2026-10-21T19:44:13.539708Z'
  support: refutes
  summary: The entry is named 7-O-methyllicoricidin and gives licorisoflavan A as
    a synonym. Its actual SMILES and InChI omit C3 stereochemistry and yield GDAAEAXMNLVRCZ-UHFFFAOYSA-N,
    despite a positive-rotation systematic text label. It has the native constitution
    and formula but does not encode exact 3R identity. Undefined stereochemistry is
    not evidence of a racemate.
  snapshot_sha256: 0ce309ab06db8efaf495d872b06f782ebf89bbcac8fc699ae07278fdee0576aa
- evidence_id: pubchem
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/licorisoflavan%20A/property/IsomericSMILES,InChI,InChIKey,MolecularFormula,MolecularWeight,MonoisotopicMass/JSON
  locator: Additional independent name lookup CID196831
  accessed_at: '2026-10-21T19:44:13.545935Z'
  support: supports
  summary: PubChem supplies both structural encodings with the native full key, formula
    and 3R centre. This is an additional comparator, not an asserted native PubChem
    xref; LIPID MAPS also lists another CID, which is not silently substituted.
  snapshot_sha256: 2d25b763f9d8fe5f315740f8758304ae5c9e286bfa8ffc800e4ed9ad65bb954f
- evidence_id: chemistry
  kind: validation
  reference: /private/tmp/am-review-session/603-authority-map.json
  locator: All eight structural encodings calculated with existing batch019 RDKit
    against batch061
  accessed_at: '2026-10-21T19:47:17Z'
  support: supports
  summary: Native, current ChEBI and PubChem SMILES/InChI agree at GDAAEAXMNLVRCZ-SFHVURJKSA-N,
    one R centre, zero charge and C27H34O5. Both LIPID MAPS encodings instead have
    one unassigned centre and UHFFFAOYSA-N. Native average mass 438.564 and exact
    mass 438.240624 agree at supplied precision. Neither prenyl alkene has distinct
    substituents at both ends, so no E/Z descriptor is required.
  snapshot_sha256: 13a6951d3c046878f4e46a9ca545532120be4082a224845709ee466a826a3e08
- evidence_id: term-76250
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/76250/
  locator: Previously retrieved current parent definition
  accessed_at: '2026-10-21T19:35:48.092807Z'
  support: supports
  summary: The native isoflavan bears ring hydroxyl groups and satisfies hydroxyisoflavans.
  snapshot_sha256: 0d7e9b8682af888a75f1ce4c32de0fb41f42f062e049d7d3050dc6c9ca0e50b9
- evidence_id: term-77002
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/77002/
  locator: Previously retrieved current parent definition
  accessed_at: '2026-10-21T19:35:48.105608Z'
  support: supports
  summary: The native isoflavan has two aromatic methoxy groups and satisfies methoxyisoflavan.
  snapshot_sha256: 0762ec96ccb2263ef73d1e9b648438ecbdbf83e70c5bff7c824c738e7cb2eb67
- evidence_id: term-35618
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/35618/
  locator: Previously retrieved current term definition, actual timestamp retained
  accessed_at: '2026-10-21T19:24:41Z'
  support: supports
  summary: Both aromatic methoxy groups satisfy the aromatic ether definition.
  snapshot_sha256: 313f535b9f2b86e55b4da02cdd6f05e29bea628f236abdb72d96bee2d1900891
- evidence_id: term-33282
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/33282/
  locator: Previously retrieved current term definition, actual timestamp retained
  accessed_at: '2026-10-21T19:24:36Z'
  support: supports
  summary: The antibacterial role includes slowing bacterial growth; a direct protein
    target is not required.
  snapshot_sha256: 20d92ce7e00c204b1753184671c043160821d692438278344335446aadcd5082
- evidence_id: registry-limits
  kind: authority
  reference: CAS:129314-37-0; HMDB:HMDB0034184; Reaxys:5461708
  locator: Exact access attempts and current source associations
  accessed_at: '2026-10-21T19:47:17Z'
  support: unknown
  summary: Common Chemistry returned 401, HMDB XML returned 403 and Reaxys returned
    403. These registry structural contents remain uninspected. ChEBI and LIPID MAPS
    associations are recorded without treating propagated links as independent exact
    structural validation.
  snapshot_sha256: 818c403823d1f4db9a99f7723d42c28d778a4daa6562d69a30f3643755911566
- evidence_id: adopted2011
  kind: primary_source
  reference: PMID:22074222; DOI:10.1021/np2004775
  locator: Complete original indexed abstract
  accessed_at: '2026-10-21T19:44:13.724334Z'
  support: partial
  summary: Exact compound 2 is licorisoflavan A, whereas 1 is licoricidin. The abstract
    reports marked growth inhibition of S. mutans/S. sobrinus at 10 µg/mL, P. gingivalis
    at 5 µg/mL and P. intermedia at 2.5 µg/mL for 2. Only compound 1 moderately inhibited
    F. nucleatum at 10 µg/mL. These are abstract growth-inhibition concentrations,
    not relabeled strain-level MICs; strain identifiers and full experimental conditions
    were not recovered.
  snapshot_sha256: be10530cbe4e654226ae7658b18f4c76cfac56686f71c1fda57732f3343b8c7d
- evidence_id: 2011-si
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/4211785
  locator: 'Official supplement: actual Figure S1 page 1 and Isolation pages 16–17'
  accessed_at: '2026-10-21T19:32:56.874396Z'
  support: supports
  summary: Compound 2 (R = CH3 in the substituent legend) has 5/7 methoxy groups,
    both normal prenyl groups and a stereobond consistent with native 3R. Multiple
    fractionation procedures explicitly recover licorisoflavan A from G. uralensis
    extract. Figure S1 concerns suspected copper-mediated oxidative purification artifacts,
    not antibacterial action. The supplement supplies identity and isolation support,
    not the unavailable main antibacterial table.
  snapshot_sha256: bb2e36884535f43f6ec19e1dcb47c7b4fb9c512fdbae1332eb78eb6a044f967b
- evidence_id: 1992-original
  kind: primary_source
  reference: https://triggered.edinburgh.clockss.org/ServeContent?doi=10.3987%2Fcom-91-5951
  locator: DOI10.3987/COM-91-5951; Figure 1 p576, exact compound 12 isolation p582
    and characterization p585
  accessed_at: '2026-10-21T19:46:03.264710Z'
  support: partial
  summary: The original isolates licorisoflavan A 12 (0.25 g) from G. aspera roots.
    Its actual Figure 1 depicts native constitution but leaves C3 unassigned, unlike
    adjacent licoricidin 11. Exact characterization gives positive rotation +5.7°
    (c 0.265, MeOH), two methoxy signals and two prenyl groups. This independently
    supports constitution and positive rotation, but is not an independent absolute-configuration
    determination. Reference 14 points to the 1988 Shizuri abstract; that conference
    original was not recovered.
  snapshot_sha256: 90ee2a692f5482728cb4c294a72b4a805a36f0476aff3d14528f9fcd81dc2a6c
- evidence_id: historical-name
  kind: primary_source
  reference: PMID:1529035; DOI:10.1055/s-2006-961435
  locator: Complete indexed original metadata; publisher body is an access challenge
  accessed_at: '2026-10-21T19:46:03.264943Z'
  support: context_only
  summary: The 1992 original title explicitly uses 5-O-methyllicoricidin from G. uralensis.
    Indexed metadata associates CAS129314-37-0. No abstract is supplied and the publisher
    HTTP200 body is a challenge page, so its actual structure and benzodiazepine-binding
    experiments were not inspected. It establishes historical name usage, not a bacterial
    target.
  snapshot_sha256: a942f3d03d55c437f37e80320e8df7209277e70691f9b9fef0ea23e342e221b5
- evidence_id: mesh-name
  kind: authority
  reference: https://meshb.nlm.nih.gov/record/ui?ui=C076768
  locator: Complete NLM supplementary concept C076768
  accessed_at: '2026-10-21T19:46:03.267418Z'
  support: context_only
  summary: NLM links 5-O-methyllicoricidin to CAS129314-37-0 and the 1992 original.
    This corroborates attested naming without independently verifying that inaccessible
    source drawing.
  snapshot_sha256: a688a2d5efa639c8093a8c5eb39231ed19c6813b5b1ea23f548eeaa9f02bedce
- evidence_id: licoricidin-revision
  kind: primary_source
  reference: DOI:10.3987/COM-88-4650
  locator: Previously read full 1988 licoricidin revision, actual Figure 1/Table 1
    and NOE/CD text
  accessed_at: '2026-10-21T19:37:40.280461Z'
  support: context_only
  summary: The authentic-material revision changed the original licoricidin proposal
    from 7-methoxy/5-hydroxy to 5-methoxy/7-hydroxy. Thus methylating the old proposed
    5-OH or the corrected 7-OH leads to the same dimethoxy constitution. This provides
    a plausible historical explanation for both derivative names, but the inaccessible
    1992 naming paper was not represented as confirming that explanation. No required
    synonym correction is established solely from modern parent locants.
  snapshot_sha256: c236deedbda5e415a3cff2f759042cfd2fe2907614df8487992f7df75ccd5149
- evidence_id: additional-activity
  kind: primary_source
  reference: PMID:24479468; PMID:22368239; PMID:25531232
  locator: Complete indexed original abstracts in bounded discovery results
  accessed_at: '2026-10-21T19:44:13.765503Z'
  support: partial
  summary: The 2014 original explicitly includes licorisoflavan A 2 in P. gingivalis
    testing but gives a pooled MIC range across compounds; no exact individual value
    is transferred. The 2012 volatile-sulfur study likewise supplies a pooled growth
    MIC range and an exact 10 µg/mL licorisoflavan A VSC result; neutralization and
    growth endpoints are distinct. The 2015 Caries Research abstract reports purified
    licorisoflavan A among three flavonoids with bactericidal effects on S. mutans
    UA159 at ≥4 µg/mL and biofilm inhibition over 4 µg/mL; full methods/material stereopurity
    were not inspected. These are corroborating leads, not complete numerical annotations.
  snapshot_sha256: cabbcc64f637c12ce3539e9c05fd91a476790737affe5e610b58fd9841a3e088
- evidence_id: additional-boundaries
  kind: primary_source
  reference: PMID:25963162; PMID:20722535; PMID:31278631
  locator: Complete indexed abstracts only
  accessed_at: '2026-10-21T19:44:13.765503Z'
  support: context_only
  summary: The G. iconica study reports ECD assignments for licorisoflavan A 4 but
    the abstract does not give its configuration or exact MIC; its 3S licoricidin
    comparator must not be merged with native 3R material. Macrophage cytokine/MMP
    and mouse antidepressant experiments are host assays, not bacterial growth or
    direct antibacterial target evidence.
  snapshot_sha256: cabbcc64f637c12ce3539e9c05fd91a476790737affe5e610b58fd9841a3e088
- evidence_id: access
  kind: validation
  reference: /private/tmp/am-review-session/603-fetch2.json
  locator: Actual retrieval outcomes and source-reading boundary
  accessed_at: '2026-10-21T19:47:17Z'
  support: context_only
  summary: The 1992 Heterocycles primary PDF was recovered; exact compound 12 sections,
    Figure 1 and references were inspected, not every unrelated glyasperin derivation.
    The 1992 naming-paper HTTP200 response was only a challenge. Adopted 2011 main
    remained unavailable after the retained 600-2011-main.html HTTP403 attempt, while
    its official supplement was readable.
  snapshot_sha256: 6cf255d09a138450c1f57a3f8441f31083581d41ad3a9b7dd1e1b22074aa1bcb
assessments:
- assessment_id: identity
  area: identity
  topic: Native identity and historical derivative nomenclature
  outcome: supported
  summary: Native constitution, 3R assignment, neutral state and numerical fields
    are coherent with current ChEBI/PubChem and the adopted SI drawing. Additional
    1992 primary establishes constitution and positive rotation but does not itself
    assign C3. The historically attested 5-O-methyllicoricidin name is qualified in
    light of the parent structural revision, not automatically rejected.
  target_ids:
  - CHEBI:69083
  evidence_ids:
  - native
  - chebi
  - pubchem
  - chemistry
  - 2011-si
  - 1992-original
  - historical-name
  - mesh-name
  - licoricidin-revision
- assessment_id: grounding
  area: grounding
  topic: Exact chemical links and parent classifications
  outcome: concern
  summary: LMPK12080046 is an underspecified chemical graph at the one native stereocentre
    and cannot be treated as full exact equivalence without qualification or upstream
    correction. This is a source-link issue; the supported native graph should not
    be broadened to match. All three parent definitions fit. Other registry structural
    access remains unresolved.
  target_ids:
  - CHEBI:69083
  evidence_ids:
  - lipidmaps
  - chemistry
  - chebi
  - registry-limits
  - term-35618
  - term-76250
  - term-77002
- assessment_id: evidence
  area: evidence
  topic: Antibacterial eligibility and producer claim
  outcome: supported
  summary: The adopted exact-compound abstract supports broad antibacterial activity
    with concentration/endpoint limits, while official SI directly supports G. uralensis
    isolation and compound mapping. Additional originals provide corroborating abstract-level
    leads, without transferring pooled MICs or host effects.
  target_ids:
  - CHEBI:69083
  evidence_ids:
  - adopted2011
  - 2011-si
  - additional-activity
  - additional-boundaries
  - term-33282
- assessment_id: completeness
  area: completeness
  topic: Optional observations and mechanism enrichment
  outcome: unknown
  summary: No required missing optional field is identified. Exact activity and producer
    observations may be added only with their primary material and method boundaries.
    No direct antibacterial protein target is established by the inspected sources.
  target_ids:
  - CHEBI:69083
  evidence_ids:
  - adapter
  - search
  - adopted2011
  - additional-activity
  - additional-boundaries
  - access
- assessment_id: provenance
  area: provenance
  topic: Source ownership and complete adopted lead disposition
  outcome: supported
  summary: The sole adopted PMID was resolved and its abstract plus official supplement
    assessed. All original 13 and expanded 21 input hashes remain unchanged, with
    actual ChEBI extraction/seeding ownership. Three SEEDED/RESEEDED history events
    are coherent; no review status was altered.
  target_ids:
  - CHEBI:69083
  evidence_ids:
  - native
  - owners
  - chebi
  - adopted2011
  - 2011-si
findings:
- finding_id: F1
  issue_key: licorisoflavan-a-lipidmaps-unspecified-stereocentre
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: The exact LIPID MAPS link omits native C3 stereochemistry
  description: Native xrefs[2] asserts LMPK12080046 for a fully specified 3R structure.
    Both actual registry encodings omit that centre and give GDAAEAXMNLVRCZ-UHFFFAOYSA-N
    rather than native GDAAEAXMNLVRCZ-SFHVURJKSA-N. Matching constitution, name and
    formula do not establish exact stereochemical equivalence. This is an unassigned
    graph, not proof of a racemate or a wrong native enantiomer.
  target_ids:
  - CHEBI:69083
  field_paths:
  - xrefs[2]
  evidence_ids:
  - native
  - owners
  - lipidmaps
  - chemistry
  - 2011-si
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
  rule_id: 'review-yaml-record: exact chemical grounding'
  normalization_reason: Major exact chemical grounding defect. The native graph itself
    is supported, so this is not a wrong-identity blocker.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - CHEBI:69083
  description: Adjudicate or qualify the underspecified LIPID MAPS exact link through
    maintained source ownership.
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
  generator: scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  acceptance_checks:
  - Compare both actual registry encodings to the native 3R structure and retain the
    missing-stereocentre distinction.
  - Remove or qualify the exact link unless a corrected exact accession is independently
    verified. Preserve the source association as provenance where appropriate; do
    not erase native stereochemistry to force agreement.
  - Regenerate and rerun required validators, checking formula, masses, full InChIKey
    and retained exact links.
- action_id: A2
  finding_ids: []
  target_ids:
  - CHEBI:69083
  description: Optional primary enrichment can capture exact isolation and antibacterial
    observations without assigning an unsupported direct target.
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
  acceptance_checks:
  - Recover adopted full assay methods before turning abstract growth-inhibition concentrations
    into strain-level MIC observations.
  - Preserve compound 2 versus licoricidin 1 and distinguish VSC neutralization, growth
    inhibition, bactericidal and biofilm endpoints.
  - Keep the historical methyllicoricidin naming explanation qualified until its original
    structure is inspected; do not infer absolute configuration solely from rotation
    sign.
limitations:
- CAS Common Chemistry returned 401, HMDB XML and Reaxys 403. Their exact registry
  structural content was not independently validated.
- Adopted 2011 main remained unavailable after a recorded 403 response. Its complete
  abstract and official SI Figure S1/isolation sections were read. Abstract growth-inhibition
  concentrations are not complete strain-level MIC annotations.
- The additional 1992 primary was read for exact compound 12, actual Figure 1, isolation,
  characterization and referenced origins, not all other compounds. Its figure leaves
  C3 unspecified; positive rotation alone was not used to assign absolute configuration.
  Raw spectra were not reprocessed.
- The historical 1992 naming paper has no indexed abstract and its publisher page
  was only an access challenge. NLM and indexed metadata attest the name/CAS association;
  its structural drawing was not inspected. The 1988 conference original was not recovered.
- Additional antibacterial and host-effect originals were read only through complete
  indexed abstracts. Pooled activity ranges, unspecified G. iconica stereochemistry,
  host responses and mechanism hypotheses were not promoted to exact native assertions.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All original 13 and expanded 21 input hashes were verified unchanged. Only scratch
  evidence and an unsaved draft were created; native/source files, history, progress
  and Git were not modified.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
