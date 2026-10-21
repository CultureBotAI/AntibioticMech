# (E)-Dodec-2-enal: coherent identity with an incompatible chain-length parent

- Review: 20261021T151646Z-e-dodec-2-enal-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:52:13Z
- Finished UTC: 2026-10-21T15:16:46Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The neutral E-aldehyde graph, names and CAS are corroborated, and exact-compound original abstracts support antibacterial activity. The imported long-chain fatty aldehyde parent is incompatible with its own C13–C22 definition for this C12 molecule. The inherited patent is a document about omega-substituted analogues, not exact identity or antibacterial proof. Full primary assay details and a complete HMDB descriptor comparison remain limited.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position386; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:133741 | data/antibiotics/antibacterial/e-dodec-2-enal.yaml | generated | (E)-dodec-2-enal |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:133741 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:133741 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:133741 | Actual focused execution exited 0. |
| Authoritative full QC | failed | True | CHEBI:133741 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:133741 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:133741 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:133741 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:133741 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:133741 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:133741 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:133741 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:133741 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral E-aldehyde

identity: supported. Targets: CHEBI:133741.

Five chemical encodings agree; CAS and aliases are independently corroborated. The terminal aldehyde and E bond agree with the definition.

### Chain-length class boundary

grounding: concern. Targets: CHEBI:133741.

The inherited long-chain parent has a defined minimum of13 carbons, incompatible with the12-carbon native graph. The alternative medium-chain definition includes12; trans-unsaturated parent remains supported.

### Pure-compound antibacterial evidence

evidence: supported. Targets: CHEBI:133741.

Three original abstracts explicitly test2E-dodecenal against the named Salmonella strain. This is distinct from whole-oil activity and host or nematode studies.

### Target and optional quantitative enrichment

completeness: unknown. Targets: CHEBI:133741.

No direct microbial protein target is established by these abstract-level biophysical interpretations. No native gene/regulator/transcriptomic claim requires a structured adapter. Full original methods should precede detailed MIC or causal-graph enrichment.

### HMDB and patent scope

identity: unknown. Targets: CHEBI:133741.

HMDB names/form context were visible but its complete descriptors were not compared. The patent belongs in document_xrefs, with related analogue context rather than evidence of exact native synthesis or antibacterial activity.

### Resistance, clinical status and producer objects

scope: not_applicable. Targets: CHEBI:133741.

None is asserted. Plant or millipede occurrence does not establish a microbial producer, clinical efficacy or resistance mechanism.

### All adopted leads and maintained source reproduction

provenance: supported. Targets: CHEBI:133741.

The complete source citation list, native fields, deterministic mint and four histories were checked; all fourteen inputs remain unchanged.

## Findings

### F1: Replace the incompatible long-chain fatty aldehyde parent

major / open / confirmed; issue key: e-dodec-2-enal-long-chain-parent-carbon-boundary.

Native parent_compounds includes CHEBI:17176, whose authoritative definition is C13–C22. The verified straight-chain molecule has12 carbons. Current ChEBI repeats the edge, so this is inherited source inconsistency rather than evidence that native composition should change. CHEBI:142621 defines C6–C12 and is the fitting chain-length class; preserve the separately correct trans-2,3-unsaturated fatty aldehyde parent.

## Recommended Actions And Acceptance Checks

### A1

Correct the chain-length relationship through maintained source qualification and regenerate the native projection.

- Resolve the17176 C13–C22 versus142621 C6–C12 definitions and retain a twelve-carbon E-aldehyde graph.
- Remove or replace the incompatible parent without changing chemical identity or the correct84588 parent.
- Run focused schema/strict checks and source reproduction after the separately authorized correction.

### A2

Optional enrichment should recover full exact-compound assay methods and explicitly qualify the inherited patent relation.

- Keep MBC separate from MIC and retain exact strain, material and conditions.
- Do not convert essential-oil, host-enzyme or nematode results into a microbial protein target.
- Treat the patent as document context; do not claim the omega-substituted examples are the native molecule.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/e-dodec-2-enal.yaml; Entire native YAML and four seed/reseed events | supports | The neutral C12H22O record has SSNZFFBDIMUILS-ZHACJKMWSA-N, an explicit E double bond, seven typed aliases, two parents, antibacterial role, CAS20407-84-5 and HMDB0031020 exact xrefs, plus EP0282940 in document_xrefs. No mode, target, quantitative activity, resistance, producer, clinical status or graph is populated. |
| owners | data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Exact row2522 and readiness row73;386-source-rows.json; original thirteen hashes plus readiness context | supports | All projected native fields match the adopted ChEBI row. Ten adopted PMID leads were read at their indexed abstract depth. The readiness hint only displays five, so the complete source row controls citation disposition. Fourteen captured inputs remain unchanged; identifier mint and four histories are coherent. |
| chemistry | Independent RDKit2026.03.5 / InChI1.07.3; ChEBI133741; PubChem5283361; 039-root-authority.py;386-authority-chemistry.json; native schema and strict outputs | supports | Native SMILES/InChI, current ChEBI molfile and current PubChem SMILES/InChI all give the same full key, formula and neutral charge with reciprocal chirality-aware matching. There are twelve carbon atoms, an aldehyde and an explicitly E C2–C3 bond. Masses and source mint agree; no salt or E/Z collapse is needed. |
| aliases | https://webbook.nist.gov/cgi/cbook.cgi?ID=20407-84-5; current ChEBI133741; 386-nist.html;386-chebi.json complete aliases/ontology/identifiers | supports | NIST independently gives the exact E InChI/key and CAS20407-84-5, with multiple equivalent trans names. Current ChEBI retains all native aliases. The eryngial name is independently used in the original2013 isolation paper. The UniProt-name projection remains a RELATED_SYNONYM rather than a mistaken protein target. |
| parent-conflict | CHEBI:17176; CHEBI:142621; CHEBI:84588; 039-parent-17176.json;386-mediumchain.json;039-parent-84588.json | refutes | Long-chain fatty aldehyde is explicitly C13–C22, whereas medium-chain fatty aldehyde is C6–C12. The native molecule is C12, so its imported17176 parent violates the authoritative definition even though current ChEBI repeats the edge. The trans-2,3-unsaturated fatty aldehyde84588 parent correctly describes its E bond at carbon2. |
| hmdb | https://hmdb.ca/metabolites/HMDB0031020; Browser-opened record identification, description and 2D MOL section on2026-10-21; subsequent descriptor-section requests failed403 | supports | The browser exposed the exact HMDB accession and described2-dodecenal as eryngial/trans-2-dodecenal and a medium-chain aldehyde, with a13-heavy-atom2D mol block. Shell XML/HTML/TXT requests and later browser descriptor retrievals returned403. Name/form context is corroborated, but no full independently parsed HMDB InChI/SMILES comparison is claimed. |
| anti2004 | PMID:15012807; DOI:10.1111/j.1365-2672.2003.02175.x; PMID:15161192; DOI:10.1021/jf0354186; 386-leads.json complete two original abstracts | supports | Both original studies explicitly report (2E)-dodecenal against S. choleraesuis subsp. choleraesuis ATCC35640, with MBC6.25 micrograms/mL and time-kill evidence. This supports exact-compound antibacterial eligibility. The surfactant interpretation is not direct binding to a specific protein. An MBC is not silently relabelled as MIC, and unpublished detailed conditions or broad-spectrum activity are not inferred. |
| anti2015 | PMID:25870012; DOI:10.1002/ptr.5351; 386-leads.json complete original abstract | supports | The Vietnam coriander study distinguishes whole essential oil, saturated aldehydes, dodecanol and exact2E-dodecenal. It reports6.25 micrograms/mL MBC for the latter against the same ATCC35640 strain, with proposed biophysical action. Whole-oil200 micrograms/mL and dodecanal/decanal100 micrograms/mL values are not assigned to the native molecule. |
| other-adopted | PMID:14194100;15612802;24139239;24243612;25619643; All five complete original abstracts in386-leads.json | context_only | The1964 paper identifies the compound in Rhinocricus insulatus defensive secretion; the2004 aroma paper identifies it in Acorus headspace; the2013 eryngial paper isolates it from Eryngium and tests nematode larvae, not bacteria. The Aristolochia paper evaluates essential oil and major E-decenal, not a demonstrated pure E-dodecenal bacterial endpoint. The human PGR1 paper is host enzyme/substrate research and its abstract emphasizes trans2-decenal; it cannot establish an antibacterial target for native C12 dodecenal. |
| reviews | PMID:21062639;26667677; Complete indexed review abstracts in386-leads.json | context_only | These are botanical/phytochemical reviews, useful for locating original work but not independent pure-compound assay evidence. Their herb, fraction and family claims are not transferred wholesale. |
| current-extra | PMID:6483572; AGR:IND44119408;AGR:IND500604868;AGR:IND600802502; 386-current-extra.json complete retrieved indexed abstracts | context_only | The additional current1984 paper reports Ducrosia oil and oxygenated components with antimicrobial activity but no individual numeric E-dodecenal endpoint in its abstract. Two agricultural originals concern coriander oil composition/mixture activity and genotype-dependent aldehyde yield. The third agricultural item is a botanical review. These are contextual origin or mixture leads, not new exact-compound molecular targets. |
| patent | https://patents.google.com/patent/EP0282940A2/en; Complete description, five examples and four claims; actual PDF p6 inspected visually | context_only | The inherited document is a synthesis patent for omega-substituted E-alkenals. Its C12 examples are12-chloro-E-dodecenal and E-dodeca2,11-dienal; the displayed claims specify terminal halogen, hydroxy or vinyl groups. These are distinct from the native terminal-methyl molecule. The document provides related synthetic-class context, not exact native structure or antimicrobial proof. The schema intentionally allows patent documents broader scope than exact xrefs, so correct slot placement is retained while relevance is qualified. |
| access | Exact compound, original citations and authority searches; 386-owners-search.json;039-root-fetch manifests1–7;OpenAlex2004/2004b/2015 responses | supports | All ten adopted leads and four additional current citation leads were inspected at stated depth. Primary2004/2015 publisher full-text requests returned403 and OpenAlex listed no open copy. PatentA1 failed404 but the actualA2 document and PDF were retrieved. An initially failed HTML-to-text helper was corrected before reading the actual body; no failed output is used as evidence. |

## Limits And Additional Notes

- The three key antibacterial originals were read at complete indexed-abstract depth; original full assay methods and tables were unavailable. No quantitative native observation was added.
- NIST confirms exact key/CAS; HMDB browser retrieval exposed identity and2D structure context, but full independent descriptor parsing remained blocked.
- The patent description, examples and actual claim page concern omega-substituted analogues. Its document-only placement is correct; exact native-compound relevance remains limited.
- Two adopted items and one additional agricultural item are reviews. Mixture, homolog, human-enzyme and anthelmintic evidence are not substituted for pure-compound antibacterial data.
- Current source17176 edge conflicts with its own definition; the review identifies the maintained-source correction without changing native files. Shared required gates are attached separately.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T151646Z-e-dodec-2-enal-review
kind: record
repository: CultureBotAI/AntibioticMech
title: '(E)-Dodec-2-enal: coherent identity with an incompatible chain-length parent'
started_at: '2026-10-21T14:52:13Z'
finished_at: '2026-10-21T15:16:46Z'
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
summary: The neutral E-aldehyde graph, names and CAS are corroborated, and exact-compound
  original abstracts support antibacterial activity. The imported long-chain fatty
  aldehyde parent is incompatible with its own C13–C22 definition for this C12 molecule.
  The inherited patent is a document about omega-substituted analogues, not exact
  identity or antibacterial proof. Full primary assay details and a complete HMDB
  descriptor comparison remain limited.
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
  - path: data/antibiotics/antibacterial/e-dodec-2-enal.yaml
    sha256: 3ae8d45e2c23df164db51a4077ae95b1ba0803ecaa468870f94aa8d877bbc20a
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
targets:
- target_id: CHEBI:133741
  path: data/antibiotics/antibacterial/e-dodec-2-enal.yaml
  label: (E)-dodec-2-enal
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
  selection: Initially uncovered queue position386; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:133741
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:133741
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    386
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:133741
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/e-dodec-2-enal.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:133741
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/e-dodec-2-enal.yaml --out /private/tmp/am-review-session/386-strict.tsv
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
  - CHEBI:133741
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
  - CHEBI:133741
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
  - CHEBI:133741
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
  - CHEBI:133741
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
  - CHEBI:133741
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
  - CHEBI:133741
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
  - CHEBI:133741
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
  - CHEBI:133741
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
  - CHEBI:133741
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/e-dodec-2-enal.yaml
  locator: Entire native YAML and four seed/reseed events
  accessed_at: '2026-10-21T14:59:52Z'
  support: supports
  summary: The neutral C12H22O record has SSNZFFBDIMUILS-ZHACJKMWSA-N, an explicit
    E double bond, seven typed aliases, two parents, antibacterial role, CAS20407-84-5
    and HMDB0031020 exact xrefs, plus EP0282940 in document_xrefs. No mode, target,
    quantitative activity, resistance, producer, clinical status or graph is populated.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: Exact row2522 and readiness row73;386-source-rows.json; original thirteen
    hashes plus readiness context
  accessed_at: '2026-10-21T14:59:52Z'
  support: supports
  summary: All projected native fields match the adopted ChEBI row. Ten adopted PMID
    leads were read at their indexed abstract depth. The readiness hint only displays
    five, so the complete source row controls citation disposition. Fourteen captured
    inputs remain unchanged; identifier mint and four histories are coherent.
  snapshot_sha256: df3cd417b930791b70839ce0470bd92a7253d6f731c19965cab27cc0e0bec89e
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit2026.03.5 / InChI1.07.3; ChEBI133741; PubChem5283361
  locator: 039-root-authority.py;386-authority-chemistry.json; native schema and strict
    outputs
  accessed_at: '2026-10-21T14:59:52Z'
  support: supports
  summary: Native SMILES/InChI, current ChEBI molfile and current PubChem SMILES/InChI
    all give the same full key, formula and neutral charge with reciprocal chirality-aware
    matching. There are twelve carbon atoms, an aldehyde and an explicitly E C2–C3
    bond. Masses and source mint agree; no salt or E/Z collapse is needed.
  snapshot_sha256: 7807e2818e9745fc039e4f91ce09e1d332558d14b3a40885f270eed3c5c345a9
- evidence_id: aliases
  kind: authority
  reference: https://webbook.nist.gov/cgi/cbook.cgi?ID=20407-84-5; current ChEBI133741
  locator: 386-nist.html;386-chebi.json complete aliases/ontology/identifiers
  accessed_at: '2026-10-21T14:59:52Z'
  support: supports
  summary: NIST independently gives the exact E InChI/key and CAS20407-84-5, with
    multiple equivalent trans names. Current ChEBI retains all native aliases. The
    eryngial name is independently used in the original2013 isolation paper. The UniProt-name
    projection remains a RELATED_SYNONYM rather than a mistaken protein target.
  snapshot_sha256: db39585fb88ed078f598e16dc1324b42b1204f748b0ea5a373ee09a0632b84d4
- evidence_id: parent-conflict
  kind: authority
  reference: CHEBI:17176; CHEBI:142621; CHEBI:84588
  locator: 039-parent-17176.json;386-mediumchain.json;039-parent-84588.json
  accessed_at: '2026-10-21T14:59:52Z'
  support: refutes
  summary: Long-chain fatty aldehyde is explicitly C13–C22, whereas medium-chain fatty
    aldehyde is C6–C12. The native molecule is C12, so its imported17176 parent violates
    the authoritative definition even though current ChEBI repeats the edge. The trans-2,3-unsaturated
    fatty aldehyde84588 parent correctly describes its E bond at carbon2.
  snapshot_sha256: c204eff29d78e0bf4904698ea2b3062cffc748c48e98b9cb9f1b4fc96f32017a
- evidence_id: hmdb
  kind: authority
  reference: https://hmdb.ca/metabolites/HMDB0031020
  locator: Browser-opened record identification, description and 2D MOL section on2026-10-21;
    subsequent descriptor-section requests failed403
  accessed_at: '2026-10-21T14:59:52Z'
  support: supports
  summary: The browser exposed the exact HMDB accession and described2-dodecenal as
    eryngial/trans-2-dodecenal and a medium-chain aldehyde, with a13-heavy-atom2D
    mol block. Shell XML/HTML/TXT requests and later browser descriptor retrievals
    returned403. Name/form context is corroborated, but no full independently parsed
    HMDB InChI/SMILES comparison is claimed.
- evidence_id: anti2004
  kind: primary_source
  reference: PMID:15012807; DOI:10.1111/j.1365-2672.2003.02175.x; PMID:15161192; DOI:10.1021/jf0354186
  locator: 386-leads.json complete two original abstracts
  accessed_at: '2026-10-21T14:59:52Z'
  support: supports
  summary: Both original studies explicitly report (2E)-dodecenal against S. choleraesuis
    subsp. choleraesuis ATCC35640, with MBC6.25 micrograms/mL and time-kill evidence.
    This supports exact-compound antibacterial eligibility. The surfactant interpretation
    is not direct binding to a specific protein. An MBC is not silently relabelled
    as MIC, and unpublished detailed conditions or broad-spectrum activity are not
    inferred.
  snapshot_sha256: 42f0468bb2386b3b47ed06d89fb8aeddab40defb6b931663aad2497d2bd02d13
- evidence_id: anti2015
  kind: primary_source
  reference: PMID:25870012; DOI:10.1002/ptr.5351
  locator: 386-leads.json complete original abstract
  accessed_at: '2026-10-21T14:59:52Z'
  support: supports
  summary: The Vietnam coriander study distinguishes whole essential oil, saturated
    aldehydes, dodecanol and exact2E-dodecenal. It reports6.25 micrograms/mL MBC for
    the latter against the same ATCC35640 strain, with proposed biophysical action.
    Whole-oil200 micrograms/mL and dodecanal/decanal100 micrograms/mL values are not
    assigned to the native molecule.
  snapshot_sha256: 42f0468bb2386b3b47ed06d89fb8aeddab40defb6b931663aad2497d2bd02d13
- evidence_id: other-adopted
  kind: primary_source
  reference: PMID:14194100;15612802;24139239;24243612;25619643
  locator: All five complete original abstracts in386-leads.json
  accessed_at: '2026-10-21T14:59:52Z'
  support: context_only
  summary: The1964 paper identifies the compound in Rhinocricus insulatus defensive
    secretion; the2004 aroma paper identifies it in Acorus headspace; the2013 eryngial
    paper isolates it from Eryngium and tests nematode larvae, not bacteria. The Aristolochia
    paper evaluates essential oil and major E-decenal, not a demonstrated pure E-dodecenal
    bacterial endpoint. The human PGR1 paper is host enzyme/substrate research and
    its abstract emphasizes trans2-decenal; it cannot establish an antibacterial target
    for native C12 dodecenal.
  snapshot_sha256: 42f0468bb2386b3b47ed06d89fb8aeddab40defb6b931663aad2497d2bd02d13
- evidence_id: reviews
  kind: database
  reference: PMID:21062639;26667677
  locator: Complete indexed review abstracts in386-leads.json
  accessed_at: '2026-10-21T14:59:52Z'
  support: context_only
  summary: These are botanical/phytochemical reviews, useful for locating original
    work but not independent pure-compound assay evidence. Their herb, fraction and
    family claims are not transferred wholesale.
  snapshot_sha256: 42f0468bb2386b3b47ed06d89fb8aeddab40defb6b931663aad2497d2bd02d13
- evidence_id: current-extra
  kind: primary_source
  reference: PMID:6483572; AGR:IND44119408;AGR:IND500604868;AGR:IND600802502
  locator: 386-current-extra.json complete retrieved indexed abstracts
  accessed_at: '2026-10-21T14:59:52Z'
  support: context_only
  summary: The additional current1984 paper reports Ducrosia oil and oxygenated components
    with antimicrobial activity but no individual numeric E-dodecenal endpoint in
    its abstract. Two agricultural originals concern coriander oil composition/mixture
    activity and genotype-dependent aldehyde yield. The third agricultural item is
    a botanical review. These are contextual origin or mixture leads, not new exact-compound
    molecular targets.
  snapshot_sha256: c8c5b7f27f9485e268e736349f361a8e90abc245c3ccf290b365c014021dc9f7
- evidence_id: patent
  kind: primary_source
  reference: https://patents.google.com/patent/EP0282940A2/en
  locator: Complete description, five examples and four claims; actual PDF p6 inspected
    visually
  accessed_at: '2026-10-21T14:59:52Z'
  support: context_only
  summary: The inherited document is a synthesis patent for omega-substituted E-alkenals.
    Its C12 examples are12-chloro-E-dodecenal and E-dodeca2,11-dienal; the displayed
    claims specify terminal halogen, hydroxy or vinyl groups. These are distinct from
    the native terminal-methyl molecule. The document provides related synthetic-class
    context, not exact native structure or antimicrobial proof. The schema intentionally
    allows patent documents broader scope than exact xrefs, so correct slot placement
    is retained while relevance is qualified.
  snapshot_sha256: 6dba58c1fbfc17330bfc95f9911d49913de5411a95ccf28f4e9508e73a28d26e
- evidence_id: access
  kind: search
  reference: Exact compound, original citations and authority searches
  locator: 386-owners-search.json;039-root-fetch manifests1–7;OpenAlex2004/2004b/2015
    responses
  accessed_at: '2026-10-21T14:59:52Z'
  support: supports
  summary: All ten adopted leads and four additional current citation leads were inspected
    at stated depth. Primary2004/2015 publisher full-text requests returned403 and
    OpenAlex listed no open copy. PatentA1 failed404 but the actualA2 document and
    PDF were retrieved. An initially failed HTML-to-text helper was corrected before
    reading the actual body; no failed output is used as evidence.
  search_scope: 2026-10-21; rg --no-ignore --hidden over maintained curation/conf/scripts/data/raw/.claude
    for exact name, eryngial, ChEBI133741, key and patent. Public exact PMID/DOI,
    NIST/HMDB and original-document retrieval. Bounded search, not an exhaustive absence
    assertion.
  snapshot_sha256: f7520cb5c196181efd2c2f584c974815ea62291a718e16cdf12bac001c95902b
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral E-aldehyde
  outcome: supported
  summary: Five chemical encodings agree; CAS and aliases are independently corroborated.
    The terminal aldehyde and E bond agree with the definition.
  target_ids:
  - CHEBI:133741
  evidence_ids:
  - chemistry
  - aliases
  - native
- assessment_id: parents
  area: grounding
  topic: Chain-length class boundary
  outcome: concern
  summary: The inherited long-chain parent has a defined minimum of13 carbons, incompatible
    with the12-carbon native graph. The alternative medium-chain definition includes12;
    trans-unsaturated parent remains supported.
  target_ids:
  - CHEBI:133741
  evidence_ids:
  - parent-conflict
  - chemistry
- assessment_id: eligibility
  area: evidence
  topic: Pure-compound antibacterial evidence
  outcome: supported
  summary: Three original abstracts explicitly test2E-dodecenal against the named
    Salmonella strain. This is distinct from whole-oil activity and host or nematode
    studies.
  target_ids:
  - CHEBI:133741
  evidence_ids:
  - anti2004
  - anti2015
  - other-adopted
- assessment_id: mechanism
  area: completeness
  topic: Target and optional quantitative enrichment
  outcome: unknown
  summary: No direct microbial protein target is established by these abstract-level
    biophysical interpretations. No native gene/regulator/transcriptomic claim requires
    a structured adapter. Full original methods should precede detailed MIC or causal-graph
    enrichment.
  target_ids:
  - CHEBI:133741
  evidence_ids:
  - native
  - anti2004
  - anti2015
  - access
- assessment_id: references
  area: identity
  topic: HMDB and patent scope
  outcome: unknown
  summary: HMDB names/form context were visible but its complete descriptors were
    not compared. The patent belongs in document_xrefs, with related analogue context
    rather than evidence of exact native synthesis or antibacterial activity.
  target_ids:
  - CHEBI:133741
  evidence_ids:
  - hmdb
  - patent
  - owners
- assessment_id: other
  area: scope
  topic: Resistance, clinical status and producer objects
  outcome: not_applicable
  summary: None is asserted. Plant or millipede occurrence does not establish a microbial
    producer, clinical efficacy or resistance mechanism.
  target_ids:
  - CHEBI:133741
  evidence_ids:
  - native
  - other-adopted
  - current-extra
- assessment_id: provenance
  area: provenance
  topic: All adopted leads and maintained source reproduction
  outcome: supported
  summary: The complete source citation list, native fields, deterministic mint and
    four histories were checked; all fourteen inputs remain unchanged.
  target_ids:
  - CHEBI:133741
  evidence_ids:
  - owners
  - access
  - chemistry
findings:
- finding_id: F1
  issue_key: e-dodec-2-enal-long-chain-parent-carbon-boundary
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Replace the incompatible long-chain fatty aldehyde parent
  description: Native parent_compounds includes CHEBI:17176, whose authoritative definition
    is C13–C22. The verified straight-chain molecule has12 carbons. Current ChEBI
    repeats the edge, so this is inherited source inconsistency rather than evidence
    that native composition should change. CHEBI:142621 defines C6–C12 and is the
    fitting chain-length class; preserve the separately correct trans-2,3-unsaturated
    fatty aldehyde parent.
  target_ids:
  - CHEBI:133741
  field_paths:
  - parent_compounds
  evidence_ids:
  - native
  - chemistry
  - parent-conflict
  rule_id: Broader structural classes must contain the exact native chemical graph
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted parent relationship
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Regenerated parent_compounds
actions:
- action_id: A1
  description: Correct the chain-length relationship through maintained source qualification
    and regenerate the native projection.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:133741
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted parent relationship
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Regenerated parent_compounds
  acceptance_checks:
  - Resolve the17176 C13–C22 versus142621 C6–C12 definitions and retain a twelve-carbon
    E-aldehyde graph.
  - Remove or replace the incompatible parent without changing chemical identity or
    the correct84588 parent.
  - Run focused schema/strict checks and source reproduction after the separately
    authorized correction.
- action_id: A2
  description: Optional enrichment should recover full exact-compound assay methods
    and explicitly qualify the inherited patent relation.
  finding_ids: []
  target_ids:
  - CHEBI:133741
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/e-dodec-2-enal.yaml
    role: Future curated evidence
  acceptance_checks:
  - Keep MBC separate from MIC and retain exact strain, material and conditions.
  - Do not convert essential-oil, host-enzyme or nematode results into a microbial
    protein target.
  - Treat the patent as document context; do not claim the omega-substituted examples
    are the native molecule.
limitations:
- The three key antibacterial originals were read at complete indexed-abstract depth;
  original full assay methods and tables were unavailable. No quantitative native
  observation was added.
- NIST confirms exact key/CAS; HMDB browser retrieval exposed identity and2D structure
  context, but full independent descriptor parsing remained blocked.
- The patent description, examples and actual claim page concern omega-substituted
  analogues. Its document-only placement is correct; exact native-compound relevance
  remains limited.
- Two adopted items and one additional agricultural item are reviews. Mixture, homolog,
  human-enzyme and anthelmintic evidence are not substituted for pure-compound antibacterial
  data.
- Current source17176 edge conflicts with its own definition; the review identifies
  the maintained-source correction without changing native files. Shared required
  gates are attached separately.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
