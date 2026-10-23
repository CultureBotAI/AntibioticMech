# Review of cezomycin

- Review: 20261021T124904Z-cezomycin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:36:35Z
- Finished UTC: 2026-10-21T12:49:04Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native PubChem-derived representation is internally valid, but its exact ChEBI link disagrees at two already configured stereocenters and specifies four additional centers. Graph mapping and a parity control confirm this is more than unspecified stereochemistry. The sole adopted primary citation supports the named natural product, producer and biosynthetic context; original discovery and ionophore studies further support cezomycin activity. These sources do not authorize silently replacing the native graph or importing calcimycin targets. One major finding requires exact-identity reconciliation before scientific status promotion.

## Scope And Provenance

Entire SEEDED, MINTED cezomycin record: definition and its sole PMID, ionophore class, PubChem-derived neutral structure, three cross-references, source concept and all three history events.

Selection: Queue 282; thirteen original input hashes retained and three actual source owners appended, giving sixteen unchanged input hashes.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-cc357c3b89 | data/antibiotics/antibacterial/cezomycin.yaml | generated | cezomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented schema validation | passed | True | antibioticmech:aro-cc357c3b89 | Exit 0; no schema issues. |
| Documented strict validation | passed | True | antibioticmech:aro-cc357c3b89 | Exit 0; zero ERROR rows. |
| Supplemental native structure and mapped parity comparison | passed | False | antibioticmech:aro-cc357c3b89 | Exit 0; native structure consistency and the exact stereochemical conflict were reproduced. A current external ChEBI SMILES failed parsing and is explicitly recorded; its valid molfile and InChI agree with the fully specified PubChem graph. |
| Supplemental source and preserved-hash reconciliation | passed | False | antibioticmech:aro-cc357c3b89 | Exit 0; sixteen hashes, exact source-derived definition/structure and the sole adopted PMID disposition checked. |
| Structured protein/pathway adapter applicability | not_applicable | False | antibioticmech:aro-cc357c3b89 | No gene, protein, pathway, regulator, stress response or transcriptomics dataset is asserted in the native record. CalC/CalG encountered in the literature are biosynthetic enzymes, not proposed antibacterial targets; no gene or pathway claim was added. |
| Authoritative full QC | failed | True | antibioticmech:aro-cc357c3b89 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-cc357c3b89 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-cc357c3b89 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-cc357c3b89 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-cc357c3b89 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-cc357c3b89 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-cc357c3b89 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-cc357c3b89 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-cc357c3b89 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Native machine representation

identity: supported. Targets: antibioticmech:aro-cc357c3b89.

Native PubChem-derived SMILES, InChI, key, formula, charge and mass are mutually consistent.

### ChEBI exact cross-reference

identity: concern. Targets: antibioticmech:aro-cc357c3b89.

The ChEBI graph inverts two natively specified centers and adds four assignments; this is not exact equivalence.

### Natural-product absolute configuration

identity: unknown. Targets: antibioticmech:aro-cc357c3b89.

Original discovery and biosynthesis material is identified as cezomycin, but a complete primary stereochemical reconstruction selecting a replacement native graph was not completed. The confirmed external-link conflict is sufficient for a bounded major finding.

### Ionophore antibacterial classification

grounding: supported. Targets: antibioticmech:aro-cc357c3b89.

The adopted primary definition and original ionophore/antimicrobial studies support cezomycin natural-product class and activity context. Those activities are not generalized to arbitrary epimers.

### Definition producer scope

evidence: supported. Targets: antibioticmech:aro-cc357c3b89.

The cited final paper and original discovery independently cultivate S. chartreusis NRRL 3882 and recover cezomycin. This is actual production, not merely exposure or resistance.

### Biological mechanism boundary

evidence: unknown. Targets: antibioticmech:aro-cc357c3b89.

Ion transport is supported for defined natural/semisynthetic cezomycin material, but the exact native stereochemical link remains unsettled. CalC/CalG biosynthesis and calcimycin-specific effects are not native antibacterial targets.

### Maintained sources and history

provenance: supported. Targets: antibioticmech:aro-cc357c3b89.

Source fields, sole adopted PMID and three history events are coherent with the inventories; all sixteen hashes are retained.

### Optional enrichment and status

completeness: supported. Targets: antibioticmech:aro-cc357c3b89.

SEEDED/MINTED status honestly exposes the incomplete identity review. Optional mechanism, producer and MIC enrichments should follow exact-identity adjudication; their absence alone is not an additional defect.

### Focused validity

schema: supported. Targets: antibioticmech:aro-cc357c3b89.

Documented schema and strict checks pass.

## Findings

### F1: The ChEBI cross-reference conflicts with two configured native stereocenters

major / open / confirmed; issue key: aro-3007769-cezomycin-chebi-stereochemical-conflict.

Native xrefs[1] CHEBI:223155 asserts exact identity, but its valid molfile/InChI differ at two of the three centers already configured in the native PubChem-derived structure. Four additional assignments are also present. Atom-mapped parity controls demonstrate the conflict. The issue is not merely absent stereochemistry and cannot be resolved by treating the names as equivalent. Which representation should define the natural-product record requires a separately documented primary identity adjudication.

## Recommended Actions And Acceptance Checks

### A1

Adjudicate natural cezomycin stereochemistry against the original structure evidence and any verified total synthesis, then make the ARO cross-reference, PubChem enrichment and native identity coherent through maintained inputs. Until that is resolved, withhold the incompatible ChEBI exact link through an explicit source correction and preserve the uncertainty. If the fully specified ChEBI/PubChem 139589064 graph is adopted, verify all seven centers and use its valid molfile/InChI or corrected pyrrole-[nH] SMILES; do not copy the invalid current ChEBI SMILES. Do not silently invert two centers, infer a mixture from four unspecified centers, or promote status on label agreement alone.

- Every retained exact cross-reference agrees with the chosen native graph at all configured centers and preserves the intended unspecified scope.
- The original natural-product structure and any adopted absolute assignments are supported by inspected primary evidence; distinct demethyl(C-11) and precezomycin results are excluded.
- SMILES, InChI, key, formula, charge and masses agree, including a valid pyrrole nitrogen representation.
- Retain biosynthetic CalC evidence as biosynthesis context; add any antimicrobial mechanism or MIC only with exact material and assay support.
- Run documented schema, strict, seed-canary and shared full-corpus checks; satisfy native identity gates before any separately authorized REVIEWED promotion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/cezomycin.yaml; Entire native YAML, including all three history events | supports | The native record is an ARO-minted cezomycin concept with a PubChem-derived graph, an explicit source PMID and transparent SEEDED status. It has no synonyms, molecular target, mode enum, resistance determinant, MIC, structured producer, clinical-product assertion or causal graph. Its definition contains the producer and ionophore assertions reviewed below. |
| chemistry | PubChem:134368; CHEBI:223155; PubChem:139589064; 282-chemistry.py/.json; official PubChem JSON, ChEBI compound response and molfile | refutes | Native SMILES and InChI and current PubChem 134368 agree on SFAOBXUZYBPOKX-KBVPZPMPSA-N, C28H34N2O6, charge 0, three configured and four unspecified centers, with masses matching native precision. Current ChEBI 223155 molfile/InChI and PubChem 139589064 agree on WOIQFTIESA-N with seven configured centers. Connectivity-preserving atom mapping shows native atoms 8 and 22 map to ChEBI atoms 22 and 13 with opposite configured stereochemistry. In a diagnostic copy, inverting exactly those two atoms and removing only the four assignments unspecified natively recovers the native key, identical canonical isomeric SMILES and mutual chirality-aware substructure matches. This demonstrates an exact-link conflict without comparing raw @ symbols or treating unspecified centers as a mixture. |
| external-encoding | CHEBI:223155; 282-chebi.json default_structure and 282-chebi.mol | context_only | The current two-star ChEBI entry supplies a fully specified natural-product name and graph, plus a Streptomyces chartreusis NRRL 3882 origin citing the 1982 discovery. Its exported aromatic SMILES lacks pyrrole [nH] and fails RDKit kekulization; the molfile and InChI are valid and agree with PubChem 139589064. This external serialization defect is not present in the native Kekule SMILES and is not a separate native finding. A future correction must not copy the invalid external string blindly. |
| primary-definition | PMID:29654174; DOI:10.1128/AEM.00586-18; 282-2018.html final PMC article and 282-2018-final.txt: complete abstract, Introduction, relevant biosynthetic Results and synthesis/purification Methods; author proof PDF Figure 1 | supports | The sole adopted citation explicitly calls cezomycin a polyether divalent-cation ionophore produced by S. chartreusis. It cultivates NRRL 3882, purifies cezomycin from culture supernatant and identifies it by HPLC retention, UV and mass against a standard. Feeding and purified-enzyme experiments show CalC-dependent formation of cezomycin-CoA during calcimycin biosynthesis. CalC is a substrate-activating biosynthetic enzyme, not an antibacterial binding target. Native producer wording is supported at the named natural-product level; the paper does not independently certify the conflicting database stereochemical encodings. |
| discovery | PMID:6816779; DOI:10.7164/antibiotics.35.1409; 282-1982.pdf: all three pages 1409–1411, Figure 1 and Table 1; Figure 1 visually inspected | supports | The original report obtains cezomycin from S. chartreusis NRRL 3882 by controlled biosynthesis, distinguishes it from calcimycin by loss of the aromatic methylamino group, and presents mass and proton/carbon NMR comparisons. It reports calcium complexation in methanol and preliminary calcium transport across a chloroform membrane. This is not evidence for the demethyl(C-11) congener and does not supply a formal MIC table. The original stereochemical drawing and analytical discussion were inspected, but every absolute center was not independently reconstructed from primary assignment data. |
| ionophore-activity | PMID:3093432; DOI:10.7164/antibiotics.39.934; 282-1986.pdf: complete four-page paper, Table 1/Figure 1 page 935 and Table 2 page 936; Table 1 visually inspected | supports | Compound 3 has the demethylamino calcimycin substitution pattern corresponding to cezomycin: R1=COOH and R2/R3/R4=H. The study measures calcium/magnesium release from isolated rat-liver mitochondria and broth-dilution antimicrobial MICs in five named strains. This supports ionophore and antibacterial context for that defined semisynthetic analog; it is not a direct bacterial protein-target experiment. The authors explicitly decline to establish a strict transport/MIC relationship. No numeric MIC, mammalian therapeutic claim or precise bacterial ion-loss causal chain was imported into the native record. |
| leads | PMID:29654174 and bounded discovery leads; 282-lead-dispositions.json and 282-core.json | supports | The sole adopted PMID was resolved and inspected at full relevant-body depth. Nine additional source dispositions distinguish original discovery/ionophore evidence from precezomycin, demethyl(C-11) cezomycin, goondoxazoles and biosynthetic-regulation studies. In particular, PMID 23881716 assigns the distinct demethyl(C-11) congener and cannot settle native full-methyl cezomycin stereochemistry. The broader discovery result set is not presented as an exhaustive full-text literature review. |
| owners | data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; scripts/enrich_pubchem_structures.py; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; 282-source-audit.json and exact source-row extracts; seeder gate_xrefs/build_record | supports | The source definition and PMID reproduce the adopted ARO row. PubChem 134368 supplies every native structure field. ARO supplies the exact ChEBI 223155 link. ChEBI 223155 is a current two-star entry outside the adopted three-star antimicrobial inventory, so the existing gate has no committed structure key for that external link and retains it. Actual owners were appended and generic ChEBI owner metadata corrected without refreshing any original hashes. All sixteen input hashes are unchanged. |
| search | Exact cezomycin local and public-source discovery; Ignored-inclusive rg for cezomycin, ARO:3007769, CHEBI:223155 and SFAOBXUZYBPOKX across conf,curation,data/raw,scripts and docs; public primary title/DOI and exact structure-key queries | context_only | Ignored files were included. The search located source rows and review-queue context, with no existing native source correction or curated mechanism assertion found in that scope. Current CARD web routes returned 404 and 500; the committed ARO row remains the inspected provenance surface. EPMC full-text XML failed, but the final PMC HTML and public author-hosted proof were obtained. |
| validation | Focused documented validators and supplemental diagnostics; 282-validation.json,282-strict.tsv,282-chemistry.json,282-source-audit.json | supports | Schema, strict, native chemical consistency, mapped scope reconciliation and preserved-input checks pass. A passing diagnostic means the conflict was reproduced, not that the ChEBI link was found equivalent. Full-corpus shared gates remain separate. |

## Limits And Additional Notes

- The complete natural-product absolute stereochemical assignment was not independently reconstructed. The confirmed finding is the incompatible exact cross-reference; the correct replacement native graph remains an explicit curation question.
- Four native stereocenters are unspecified. That does not establish a physical mixture, and the major finding rests on two already specified centers that conflict.
- The ChEBI exported SMILES fails parsing, while its molfile/InChI and the fully specified PubChem graph agree. That upstream encoding problem is distinct from the valid native representation.
- The original 1982 calcium-transport statement is preliminary; the 1986 work measures mitochondrial cation efflux and antibacterial activity but explicitly does not establish a strict causal transport/MIC relationship. No exact bacterial ion-loss target chain is claimed.
- The 2018 author-hosted PDF contains proof annotations; the final PMC HTML was separately obtained and used for the cited definition, Results and Methods. Supplemental kinetic files were not independently audited.
- Current CARD web routes returned 404/500. The adopted ARO inventory, its PMID and current independent chemical authorities were inspected; no current CARD page content is claimed.
- Only the stated additional discovery leads were inspected. Related precezomycin, demethyl(C-11) cezomycin and calcimycin biosynthetic studies were not transferred to native identity or antibacterial targets.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native record or maintained input was changed, and all sixteen original-plus-appended input hashes were rechecked.
- The sole adopted PMID has an explicit disposition. Optional links and tags refer to cezomycin; no sibling review targets were copied.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T124904Z-cezomycin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of cezomycin
started_at: '2026-10-21T12:36:35Z'
finished_at: '2026-10-21T12:49:04Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: Independent full-record review with original hashes preserved
    and actual CARD/PubChem owners captured before detailed judgment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Confirmed stereochemical cross-reference conflict; natural-product
  identity needs adjudication
scientific_review: true
summary: The native PubChem-derived representation is internally valid, but its exact
  ChEBI link disagrees at two already configured stereocenters and specifies four
  additional centers. Graph mapping and a parity control confirm this is more than
  unspecified stereochemistry. The sole adopted primary citation supports the named
  natural product, producer and biosynthetic context; original discovery and ionophore
  studies further support cezomycin activity. These sources do not authorize silently
  replacing the native graph or importing calcimycin targets. One major finding requires
  exact-identity reconciliation before scientific status promotion.
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
  - path: data/antibiotics/antibacterial/cezomycin.yaml
    sha256: d32f3ce2edd819bd543a07495872e7d7bf255f321264b3eefc3d06a7f98b27a8
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
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: Adopted CARD/ARO definition, class and cross-references
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: Adopted exact chemical structure
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: PubChem structure-enrichment owner
scope:
  description: 'Entire SEEDED, MINTED cezomycin record: definition and its sole PMID,
    ionophore class, PubChem-derived neutral structure, three cross-references, source
    concept and all three history events.'
  selection: Queue 282; thirteen original input hashes retained and three actual source
    owners appended, giving sixteen unchanged input hashes.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-cc357c3b89
targets:
- target_id: antibioticmech:aro-cc357c3b89
  path: data/antibiotics/antibacterial/cezomycin.yaml
  label: cezomycin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: CARD/ARO source extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted CARD/ARO definition, class and cross-references
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact chemical structure
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem structure-enrichment owner
checks:
- check_id: schema
  name: Documented schema validation
  status: passed
  required: true
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/cezomycin.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; no schema issues.
  target_ids:
  - antibioticmech:aro-cc357c3b89
  evidence_ids:
  - validation
- check_id: strict
  name: Documented strict validation
  status: passed
  required: true
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/cezomycin.yaml --out /private/tmp/am-review-session/282-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; zero ERROR rows.
  target_ids:
  - antibioticmech:aro-cc357c3b89
  evidence_ids:
  - validation
- check_id: chemistry
  name: Supplemental native structure and mapped parity comparison
  status: passed
  required: false
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/282-chemistry.py
    > /private/tmp/am-review-session/282-chemistry.log
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; native structure consistency and the exact stereochemical conflict
    were reproduced. A current external ChEBI SMILES failed parsing and is explicitly
    recorded; its valid molfile and InChI agree with the fully specified PubChem graph.
  target_ids:
  - antibioticmech:aro-cc357c3b89
  evidence_ids:
  - chemistry
- check_id: source-reconciliation
  name: Supplemental source and preserved-hash reconciliation
  status: passed
  required: false
  command: .venv/bin/python /private/tmp/am-review-session/282-ledger.py
  exit_code: 0
  expected_exit_code: 0
  summary: Exit 0; sixteen hashes, exact source-derived definition/structure and the
    sole adopted PMID disposition checked.
  target_ids:
  - antibioticmech:aro-cc357c3b89
  evidence_ids:
  - owners
  - leads
- check_id: structured-adapter
  name: Structured protein/pathway adapter applicability
  status: not_applicable
  required: false
  summary: No gene, protein, pathway, regulator, stress response or transcriptomics
    dataset is asserted in the native record. CalC/CalG encountered in the literature
    are biosynthetic enzymes, not proposed antibacterial targets; no gene or pathway
    claim was added.
  target_ids:
  - antibioticmech:aro-cc357c3b89
  evidence_ids:
  - record
  - primary-definition
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-cc357c3b89
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
  - antibioticmech:aro-cc357c3b89
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
  - antibioticmech:aro-cc357c3b89
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
  - antibioticmech:aro-cc357c3b89
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
  - antibioticmech:aro-cc357c3b89
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
  - antibioticmech:aro-cc357c3b89
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
  - antibioticmech:aro-cc357c3b89
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
  - antibioticmech:aro-cc357c3b89
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
  - antibioticmech:aro-cc357c3b89
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/cezomycin.yaml
  locator: Entire native YAML, including all three history events
  accessed_at: '2026-10-21T12:46:05Z'
  support: supports
  summary: The native record is an ARO-minted cezomycin concept with a PubChem-derived
    graph, an explicit source PMID and transparent SEEDED status. It has no synonyms,
    molecular target, mode enum, resistance determinant, MIC, structured producer,
    clinical-product assertion or causal graph. Its definition contains the producer
    and ionophore assertions reviewed below.
- evidence_id: chemistry
  kind: validation
  reference: PubChem:134368; CHEBI:223155; PubChem:139589064
  locator: 282-chemistry.py/.json; official PubChem JSON, ChEBI compound response
    and molfile
  accessed_at: '2026-10-21T12:46:05Z'
  support: refutes
  summary: Native SMILES and InChI and current PubChem 134368 agree on SFAOBXUZYBPOKX-KBVPZPMPSA-N,
    C28H34N2O6, charge 0, three configured and four unspecified centers, with masses
    matching native precision. Current ChEBI 223155 molfile/InChI and PubChem 139589064
    agree on WOIQFTIESA-N with seven configured centers. Connectivity-preserving atom
    mapping shows native atoms 8 and 22 map to ChEBI atoms 22 and 13 with opposite
    configured stereochemistry. In a diagnostic copy, inverting exactly those two
    atoms and removing only the four assignments unspecified natively recovers the
    native key, identical canonical isomeric SMILES and mutual chirality-aware substructure
    matches. This demonstrates an exact-link conflict without comparing raw @ symbols
    or treating unspecified centers as a mixture.
  snapshot_sha256: adf0f6d0eba03cd589d5097a807f61e9ded977346a9880a54744dfc987331768
- evidence_id: external-encoding
  kind: authority
  reference: CHEBI:223155
  locator: 282-chebi.json default_structure and 282-chebi.mol
  accessed_at: '2026-10-21T12:46:05Z'
  support: context_only
  summary: The current two-star ChEBI entry supplies a fully specified natural-product
    name and graph, plus a Streptomyces chartreusis NRRL 3882 origin citing the 1982
    discovery. Its exported aromatic SMILES lacks pyrrole [nH] and fails RDKit kekulization;
    the molfile and InChI are valid and agree with PubChem 139589064. This external
    serialization defect is not present in the native Kekule SMILES and is not a separate
    native finding. A future correction must not copy the invalid external string
    blindly.
  snapshot_sha256: ba83c2adbc0879f8a29d12e564491d0e876242cd7acb4fe45067a0cd3b936dd1
- evidence_id: primary-definition
  kind: primary_source
  reference: PMID:29654174; DOI:10.1128/AEM.00586-18
  locator: '282-2018.html final PMC article and 282-2018-final.txt: complete abstract,
    Introduction, relevant biosynthetic Results and synthesis/purification Methods;
    author proof PDF Figure 1'
  accessed_at: '2026-10-21T12:46:05Z'
  support: supports
  summary: The sole adopted citation explicitly calls cezomycin a polyether divalent-cation
    ionophore produced by S. chartreusis. It cultivates NRRL 3882, purifies cezomycin
    from culture supernatant and identifies it by HPLC retention, UV and mass against
    a standard. Feeding and purified-enzyme experiments show CalC-dependent formation
    of cezomycin-CoA during calcimycin biosynthesis. CalC is a substrate-activating
    biosynthetic enzyme, not an antibacterial binding target. Native producer wording
    is supported at the named natural-product level; the paper does not independently
    certify the conflicting database stereochemical encodings.
  snapshot_sha256: 13a07cb19afe68838455b6966fdbb1e0bf9d970f8f020bb844d3984114fd5bd9
- evidence_id: discovery
  kind: primary_source
  reference: PMID:6816779; DOI:10.7164/antibiotics.35.1409
  locator: '282-1982.pdf: all three pages 1409–1411, Figure 1 and Table 1; Figure
    1 visually inspected'
  accessed_at: '2026-10-21T12:46:05Z'
  support: supports
  summary: The original report obtains cezomycin from S. chartreusis NRRL 3882 by
    controlled biosynthesis, distinguishes it from calcimycin by loss of the aromatic
    methylamino group, and presents mass and proton/carbon NMR comparisons. It reports
    calcium complexation in methanol and preliminary calcium transport across a chloroform
    membrane. This is not evidence for the demethyl(C-11) congener and does not supply
    a formal MIC table. The original stereochemical drawing and analytical discussion
    were inspected, but every absolute center was not independently reconstructed
    from primary assignment data.
  snapshot_sha256: 8f122583f24cb361ab3422c4d121f712d639b8e1ddbb1ff18af2bb078fd831ca
- evidence_id: ionophore-activity
  kind: primary_source
  reference: PMID:3093432; DOI:10.7164/antibiotics.39.934
  locator: '282-1986.pdf: complete four-page paper, Table 1/Figure 1 page 935 and
    Table 2 page 936; Table 1 visually inspected'
  accessed_at: '2026-10-21T12:46:05Z'
  support: supports
  summary: 'Compound 3 has the demethylamino calcimycin substitution pattern corresponding
    to cezomycin: R1=COOH and R2/R3/R4=H. The study measures calcium/magnesium release
    from isolated rat-liver mitochondria and broth-dilution antimicrobial MICs in
    five named strains. This supports ionophore and antibacterial context for that
    defined semisynthetic analog; it is not a direct bacterial protein-target experiment.
    The authors explicitly decline to establish a strict transport/MIC relationship.
    No numeric MIC, mammalian therapeutic claim or precise bacterial ion-loss causal
    chain was imported into the native record.'
  snapshot_sha256: a602684a978f9bdd2650fbb7b29da371ab949b9e29a767fb2b2bc9dbd7b17105
- evidence_id: leads
  kind: database
  reference: PMID:29654174 and bounded discovery leads
  locator: 282-lead-dispositions.json and 282-core.json
  accessed_at: '2026-10-21T12:46:05Z'
  support: supports
  summary: The sole adopted PMID was resolved and inspected at full relevant-body
    depth. Nine additional source dispositions distinguish original discovery/ionophore
    evidence from precezomycin, demethyl(C-11) cezomycin, goondoxazoles and biosynthetic-regulation
    studies. In particular, PMID 23881716 assigns the distinct demethyl(C-11) congener
    and cannot settle native full-methyl cezomycin stereochemistry. The broader discovery
    result set is not presented as an exhaustive full-text literature review.
  snapshot_sha256: b39b3e486021c443508a232bb8a16fc6b24fbe10ffbf2de2d70731ae9bd231a4
- evidence_id: owners
  kind: record_content
  reference: data/raw/aro_antibiotics.tsv; data/raw/pubchem_structures.tsv; scripts/enrich_pubchem_structures.py;
    scripts/extract_source_inventory.py; scripts/seed_from_sources.py
  locator: 282-source-audit.json and exact source-row extracts; seeder gate_xrefs/build_record
  accessed_at: '2026-10-21T12:46:05Z'
  support: supports
  summary: The source definition and PMID reproduce the adopted ARO row. PubChem 134368
    supplies every native structure field. ARO supplies the exact ChEBI 223155 link.
    ChEBI 223155 is a current two-star entry outside the adopted three-star antimicrobial
    inventory, so the existing gate has no committed structure key for that external
    link and retains it. Actual owners were appended and generic ChEBI owner metadata
    corrected without refreshing any original hashes. All sixteen input hashes are
    unchanged.
  snapshot_sha256: 212347db97588143ca601878c13eb3fe3e6681637821bbd003bc8ffbf6488077
- evidence_id: search
  kind: search
  reference: Exact cezomycin local and public-source discovery
  locator: Ignored-inclusive rg for cezomycin, ARO:3007769, CHEBI:223155 and SFAOBXUZYBPOKX
    across conf,curation,data/raw,scripts and docs; public primary title/DOI and exact
    structure-key queries
  accessed_at: '2026-10-21T12:46:05Z'
  support: context_only
  summary: Ignored files were included. The search located source rows and review-queue
    context, with no existing native source correction or curated mechanism assertion
    found in that scope. Current CARD web routes returned 404 and 500; the committed
    ARO row remains the inspected provenance surface. EPMC full-text XML failed, but
    the final PMC HTML and public author-hosted proof were obtained.
  snapshot_sha256: 338c4f206426e0f2e9cf0baa4c0ec12f2d7f9e53ef65cd3c38f2b854ccd8a4be
  search_scope: Ignored-inclusive rg for cezomycin, ARO:3007769, CHEBI:223155 and
    SFAOBXUZYBPOKX across conf,curation,data/raw,scripts and docs; public primary
    title/DOI and exact structure-key queries
- evidence_id: validation
  kind: validation
  reference: Focused documented validators and supplemental diagnostics
  locator: 282-validation.json,282-strict.tsv,282-chemistry.json,282-source-audit.json
  accessed_at: '2026-10-21T12:46:05Z'
  support: supports
  summary: Schema, strict, native chemical consistency, mapped scope reconciliation
    and preserved-input checks pass. A passing diagnostic means the conflict was reproduced,
    not that the ChEBI link was found equivalent. Full-corpus shared gates remain
    separate.
assessments:
- assessment_id: native-encoding
  area: identity
  topic: Native machine representation
  outcome: supported
  summary: Native PubChem-derived SMILES, InChI, key, formula, charge and mass are
    mutually consistent.
  target_ids:
  - antibioticmech:aro-cc357c3b89
  evidence_ids:
  - chemistry
  - owners
- assessment_id: equivalence
  area: identity
  topic: ChEBI exact cross-reference
  outcome: concern
  summary: The ChEBI graph inverts two natively specified centers and adds four assignments;
    this is not exact equivalence.
  target_ids:
  - antibioticmech:aro-cc357c3b89
  evidence_ids:
  - chemistry
  - external-encoding
- assessment_id: natural-identity
  area: identity
  topic: Natural-product absolute configuration
  outcome: unknown
  summary: Original discovery and biosynthesis material is identified as cezomycin,
    but a complete primary stereochemical reconstruction selecting a replacement native
    graph was not completed. The confirmed external-link conflict is sufficient for
    a bounded major finding.
  target_ids:
  - antibioticmech:aro-cc357c3b89
  evidence_ids:
  - discovery
  - primary-definition
  - chemistry
- assessment_id: classification
  area: grounding
  topic: Ionophore antibacterial classification
  outcome: supported
  summary: The adopted primary definition and original ionophore/antimicrobial studies
    support cezomycin natural-product class and activity context. Those activities
    are not generalized to arbitrary epimers.
  target_ids:
  - antibioticmech:aro-cc357c3b89
  evidence_ids:
  - primary-definition
  - discovery
  - ionophore-activity
- assessment_id: producer
  area: evidence
  topic: Definition producer scope
  outcome: supported
  summary: The cited final paper and original discovery independently cultivate S.
    chartreusis NRRL 3882 and recover cezomycin. This is actual production, not merely
    exposure or resistance.
  target_ids:
  - antibioticmech:aro-cc357c3b89
  evidence_ids:
  - primary-definition
  - discovery
- assessment_id: mechanism
  area: evidence
  topic: Biological mechanism boundary
  outcome: unknown
  summary: Ion transport is supported for defined natural/semisynthetic cezomycin
    material, but the exact native stereochemical link remains unsettled. CalC/CalG
    biosynthesis and calcimycin-specific effects are not native antibacterial targets.
  target_ids:
  - antibioticmech:aro-cc357c3b89
  evidence_ids:
  - ionophore-activity
  - primary-definition
  - leads
- assessment_id: provenance
  area: provenance
  topic: Maintained sources and history
  outcome: supported
  summary: Source fields, sole adopted PMID and three history events are coherent
    with the inventories; all sixteen hashes are retained.
  target_ids:
  - antibioticmech:aro-cc357c3b89
  evidence_ids:
  - record
  - owners
- assessment_id: completeness
  area: completeness
  topic: Optional enrichment and status
  outcome: supported
  summary: SEEDED/MINTED status honestly exposes the incomplete identity review. Optional
    mechanism, producer and MIC enrichments should follow exact-identity adjudication;
    their absence alone is not an additional defect.
  target_ids:
  - antibioticmech:aro-cc357c3b89
  evidence_ids:
  - record
  - leads
- assessment_id: schema
  area: schema
  topic: Focused validity
  outcome: supported
  summary: Documented schema and strict checks pass.
  target_ids:
  - antibioticmech:aro-cc357c3b89
  evidence_ids:
  - validation
findings:
- finding_id: F1
  issue_key: aro-3007769-cezomycin-chebi-stereochemical-conflict
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: The ChEBI cross-reference conflicts with two configured native stereocenters
  description: Native xrefs[1] CHEBI:223155 asserts exact identity, but its valid
    molfile/InChI differ at two of the three centers already configured in the native
    PubChem-derived structure. Four additional assignments are also present. Atom-mapped
    parity controls demonstrate the conflict. The issue is not merely absent stereochemistry
    and cannot be resolved by treating the names as equivalent. Which representation
    should define the natural-product record requires a separately documented primary
    identity adjudication.
  target_ids:
  - antibioticmech:aro-cc357c3b89
  field_paths:
  - xrefs[1]
  - chemical_structure
  - grounding_status
  evidence_ids:
  - chemistry
  - external-encoding
  - discovery
  - owners
  rule_id: 'docs/CURATION.md and review-checklist: exact chemical xref equivalence
    and identity sign-off'
  native_severity: 'Major: incompatible exact chemical grounding'
  normalization_reason: The native representation is parseable and internally consistent,
    but an exact external identity assertion is disproved. This review does not declare
    a replacement natural-product configuration from database consensus alone.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted chemical links and definition
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted PubChem 134368 graph
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Future verified structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source-specific link correction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Exact identity gate and generated representation
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Future explicit grounding adjudication if supported
actions:
- action_id: A1
  description: Adjudicate natural cezomycin stereochemistry against the original structure
    evidence and any verified total synthesis, then make the ARO cross-reference,
    PubChem enrichment and native identity coherent through maintained inputs. Until
    that is resolved, withhold the incompatible ChEBI exact link through an explicit
    source correction and preserve the uncertainty. If the fully specified ChEBI/PubChem
    139589064 graph is adopted, verify all seven centers and use its valid molfile/InChI
    or corrected pyrrole-[nH] SMILES; do not copy the invalid current ChEBI SMILES.
    Do not silently invert two centers, infer a mixture from four unspecified centers,
    or promote status on label agreement alone.
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-cc357c3b89
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted chemical links and definition
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted PubChem 134368 graph
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Future verified structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained source-specific link correction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Exact identity gate and generated representation
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Future explicit grounding adjudication if supported
  ownership_note: The adopted ARO row and PubChem structure row are separate maintained
    owners. The seeder currently compares only known inventory structure keys and
    has no automatic reconciliation for this two-star ChEBI external entry. A blind
    refresh reproduces the source conflict.
  generator: just extract-inventory; just extract-pubchem-canary ARO:3007769; just
    seed; just seed-canary antibioticmech:aro-cc357c3b89
  acceptance_checks:
  - Every retained exact cross-reference agrees with the chosen native graph at all
    configured centers and preserves the intended unspecified scope.
  - The original natural-product structure and any adopted absolute assignments are
    supported by inspected primary evidence; distinct demethyl(C-11) and precezomycin
    results are excluded.
  - SMILES, InChI, key, formula, charge and masses agree, including a valid pyrrole
    nitrogen representation.
  - Retain biosynthetic CalC evidence as biosynthesis context; add any antimicrobial
    mechanism or MIC only with exact material and assay support.
  - Run documented schema, strict, seed-canary and shared full-corpus checks; satisfy
    native identity gates before any separately authorized REVIEWED promotion.
limitations:
- The complete natural-product absolute stereochemical assignment was not independently
  reconstructed. The confirmed finding is the incompatible exact cross-reference;
  the correct replacement native graph remains an explicit curation question.
- Four native stereocenters are unspecified. That does not establish a physical mixture,
  and the major finding rests on two already specified centers that conflict.
- The ChEBI exported SMILES fails parsing, while its molfile/InChI and the fully specified
  PubChem graph agree. That upstream encoding problem is distinct from the valid native
  representation.
- The original 1982 calcium-transport statement is preliminary; the 1986 work measures
  mitochondrial cation efflux and antibacterial activity but explicitly does not establish
  a strict causal transport/MIC relationship. No exact bacterial ion-loss target chain
  is claimed.
- The 2018 author-hosted PDF contains proof annotations; the final PMC HTML was separately
  obtained and used for the cited definition, Results and Methods. Supplemental kinetic
  files were not independently audited.
- Current CARD web routes returned 404/500. The adopted ARO inventory, its PMID and
  current independent chemical authorities were inspected; no current CARD page content
  is claimed.
- Only the stated additional discovery leads were inspected. Related precezomycin,
  demethyl(C-11) cezomycin and calcimycin biosynthetic studies were not transferred
  to native identity or antibacterial targets.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native record or maintained input was changed, and all sixteen original-plus-appended
  input hashes were rechecked.
- The sole adopted PMID has an explicit disposition. Optional links and tags refer
  to cezomycin; no sibling review targets were copied.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links: []
tags:
- record-review
- cezomycin
- stereochemical-equivalence
- biosynthetic-scope
```
