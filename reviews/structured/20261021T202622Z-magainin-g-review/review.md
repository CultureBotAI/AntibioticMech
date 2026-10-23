# Review of magainin G

- Review: 20261021T202622Z-magainin-g-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T20:11:21Z
- Finished UTC: 2026-10-21T20:26:22Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native structure is internally consistent and matches current PubChem, but it lacks the Gly residue explicitly retained after the added N-terminal beta-alanine in the adopted original magainin G sequence. This confirmed structure-to-primary-source conflict blocks exact identity sign-off. Published G activity must remain attached to the stated 24-residue material until the source mapping is corrected.

## Scope And Provenance

Entire native record, sole adopted original, both identifiers, broader peptide class, source concept and all three history events; current ARO/PubChem, independent peptide assembly, original page scans and synthesis patent sequence comparison.

Selection: Initially uncovered queue position 626; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-40a2a87cc8 | data/antibiotics/antibacterial/magainin-g.yaml | generated | magainin G |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-40a2a87cc8 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-40a2a87cc8 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-40a2a87cc8 | Actual focused execution exited 0. |
| sequence-comparison | passed | False | antibioticmech:aro-40a2a87cc8 | Actual scratch helper exited 0 from 063; successful deterministic checks do not resolve the primary identity conflict. |
| tautomer-normalization | passed | False | antibioticmech:aro-40a2a87cc8 | Actual scratch helper exited 0 from 063; successful deterministic checks do not resolve the primary identity conflict. |
| source-ledger | passed | False | antibioticmech:aro-40a2a87cc8 | Actual scratch helper exited 0 from 063; successful deterministic checks do not resolve the primary identity conflict. |
| Authoritative full QC | failed | True | antibioticmech:aro-40a2a87cc8 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-40a2a87cc8 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-40a2a87cc8 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-40a2a87cc8 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-40a2a87cc8 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-40a2a87cc8 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-40a2a87cc8 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-40a2a87cc8 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-40a2a87cc8 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact G peptide sequence

identity: concern. Targets: antibioticmech:aro-40a2a87cc8.

The native is a chemically valid 23-residue beta-alanine replacement, but the adopted original G is the 24-residue extension. Source-to-structure identity is not established.

### Encoding and stereo consistency

representation: supported. Targets: antibioticmech:aro-40a2a87cc8.

The existing graph, formula, charge and masses agree internally and with current PubChem. Local tautomer normalization explains the apparent raw InChI mismatch.

### Source identifiers and broader peptide class

grounding: concern. Targets: antibioticmech:aro-40a2a87cc8.

Both asserted registries resolve and the parent is broader, but the exact PubChem mapping conflicts with the sequence in the cited original; current provider repetition is not independent identity proof.

### Exact material and biological endpoints

evidence: unknown. Targets: antibioticmech:aro-40a2a87cc8.

The original and patent support activity of the stated G material. Numerical activity, protozoal membrane injury and host-cell findings must not be transferred across the unresolved peptide identity. No missing direct protein target is inferred.

### Owner chain and source history

provenance: supported. Targets: antibioticmech:aro-40a2a87cc8.

The adopted ARO and PubChem rows reproduce the native, the stable mint is correct, and all three seed-history entries remain intact. A future fix belongs in the maintained source mapping and seeder workflow.

### Whole-record review and source limits

completeness: supported. Targets: antibioticmech:aro-40a2a87cc8.

Every native field and sole adopted reference were reviewed. Optional enrichment is separate from the demonstrated identity conflict. No protein/pathway adapter applies to the native or this sequence/protozoal-physical-injury follow-up.

## Findings

### F1: The native G structure omits a Gly retained in the cited original

blocker / open / confirmed; issue key: magainin-g-missing-n-terminal-gly-source-identity.

The adopted primary sequence and patent distinguish N-terminal beta-alanine addition from Gly1 replacement. Native and current PubChem16132425 encode the replacement, lacking C2H3NO relative to the printed G extension. The record therefore joins a shorter peptide graph to the cited G identity. The definition also compresses the original B/G difference: B has Ala8 whereas G retains Ser8. Database agreement does not resolve this positive conflict, and simply changing addition to substitution would disconnect the record from its adopted source.

## Recommended Actions And Acceptance Checks

### A1

Reconcile the exact G source mapping against the printed original sequence and original synthesis material. Preserve replacement and extension as distinct structures. If retaining the cited G identity, obtain an authoritative structure mapping for the 24-residue extension, update the maintained PubChem/ARO or curator identity lane, and regenerate the exact canary. If retaining the current 23-residue graph, identify and cite its actual distinct analogue instead. Rewrite the definition to state the adjudicated sequence, terminal modification and Ser/Ala distinction; correct the duplicated is and article at the same time. Do not apply the scratch candidate or substitute a guessed CID automatically.

- The exact selected peptide sequence, terminal amide, residue count, formula and all configured centres agree by independent construction and reciprocal chirality-aware graph mapping.
- All exact xrefs and primary citations resolve to the same selected peptide; 23- and 24-residue materials are not treated as synonyms.
- Native definition describes the selected terminal change and relevant B/G residue differences accurately.
- Separately authorized regeneration with just seed-canary ARO:3003569 reproduces the correction; schema, strict, term/reference/history and corpus gates pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/magainin-g.yaml; Entire native; 626-inspect.json and 626-source-rows.json | supports | SEEDED/MINTED ARO-derived record contains a synthetic-analogue definition, one peptide parent/class, two xrefs, one source concept and three seed events. No separate structured mechanism, target, resistance, activity, producer, clinical, dataset or causal-graph objects occur. Sixteen captured inputs preserve all thirteen initial hashes. |
| chemical | Native SMILES/InChI and PubChem CID16132425; 626-chemistry.json; 626-sequence-check.json; 626-normalization-diagnostic.json | supports | Native and current PubChem encodings give MGYZVMMHKLKEHR-QTRCTKFUSA-N, C117H187N31O28S, charge 0 and 23 configured stereocentres. Independent construction of beta-Ala-I-G-K-F-L-H-S-A-K-K-F-A-K-A-F-V-A-E-I-M-N-S-NH2 matches the native graph reciprocally with chirality. The raw InChI mismatch resolves after 24 local imidic-acid-to-amide transfers without changing tetrahedral tags. |
| primary-sequence | PMID:2285300; DOI:10.1128/aac.34.9.1824; actual printed page 1824 peptide sequence; 626-1990-p1824-hires.png | refutes | The adopted original prints G as beta-Ala-G-I-G-K-F-L-H-S-A-K-K-F-A-K-A-F-V-A-E-I-M-N-S-NH2: a 24-residue extension. The native encodes a 23-residue replacement of Gly1 instead. This is a positive sequence conflict, not an inference from a name or absent database entry. |
| sequence-map | Independent sequence-to-graph comparison; 626-sequence-check.py and 626-sequence-check.json | refutes | Assembling the printed 24-residue sequence with its C-terminal amide gives diagnostic formula C119H190N32O29S and key IEGIJVQYFOYCMV-ZAJZLZNTSA-N. Its difference from native is one glycyl residue, C2H3NO and 57.021463716 Da. This candidate is a diagnostic structure, not a source-adopted replacement or a confirmed new PubChem identifier. |
| patent | https://patents.google.com/patent/US5221732A/en; Original patent PDF Table 1, scientific description, synthesis/assay methods, Table 3 and claims 9–11; actual Table 1 and claim pages viewed | supports | The inventors distinguish the 23-residue replacement in claim 9 from the 24-residue extension in claim 11; Table 1 labels the extended Ser8-containing analogue G. These are distinct peptide designs. The patent supplies bacterial growth-inhibition context for named G but does not make the two structures equivalent. |
| activity | PMID:2285300; All original pages 1824–1826; methods, results, discussion and Figure 1 caption | partial | The stated G material produces concentration- and time-dependent protozoal injury. Morphology, motility and membrane leakage are the endpoints, with regrowth assessed separately; they are not MIC or direct protein-binding measurements. Actual Figure 1 concerns B. The paper also describes B/G antibacterial activity, referring to earlier synthesis work; these observations cannot silently validate the shorter native G graph. |
| authorities | ARO:3003569; ARO:3000053; pubchem.compound:16132425; Current official ARO blocks from 620-current-aro.obo; 626-current-aro-blocks.txt; current PUG REST properties and synonyms | partial | Current ARO repeats the adopted definition and PubChem xref. The peptide parent is broader and structurally appropriate. Current PubChem repeats the shorter native sequence. A fresh exact-key lookup for the diagnostic extension returned404, so no replacement CID is asserted. |
| sources | PMID:3410055; PMID:1319823; PMID:8706437; PMID:2001767; PMID:1708887; Complete indexed abstracts; 626-1988-abstract.json and 626-discovery.json | context_only | The 1988 synthesis abstract concerns magainin2 analogues; its full publisher PDF routes returned403. Later lung-cancer, sperm and tumor-cell cytolysis abstracts are exact-name or family follow-up with host-cell endpoints. They do not establish a direct bacterial protein target or resolve the missing Gly. |
| search | Exact magainin G discovery and maintained sources; 626-source-audit.json; 626-fetch1–4.json; initial local hits | supports | All thirteen exact-phrase discovery titles and twelve available abstracts were read, including the sole adopted PMID. The actual ARO inventory and PubChem enrichment owners were captured before assessment; no absence of all literature is claimed. |

## Limits And Additional Notes

- The original 1988 synthesis full text remains inaccessible after public Wiley 403 responses. The adopted 1990 complete article and original patent provide directly inspected sequence evidence.
- Current PubChem and ARO repeat the shorter graph/mapping. The diagnostic extension key was not found by exact public PubChem lookup; no corrected database ID or automatic structural replacement is proposed.
- Primary G biological results concern the stated 24-residue sequence. Protozoal morphology/motility, membrane leakage, bacterial growth inhibition and host cytotoxicity remain different endpoints. Figure 1 is B-specific; no G quantitative image measurement was inferred.
- No bacterial gene/protein/pathway, resistance determinant or expression dataset is named by the native; iModulonDB is not applicable to this identity/protozoal membrane review and no absence inference was made.
- The required shared full-QC gate retains the established SciPy import failure. Focused success and draft-contract validation do not replace separately recorded shared corpus, term, reference and history checks.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All thirteen initial hashes were preserved; sixteen actual inputs now cover the ARO/PubChem owners. Native/source/history files and prior immutable reviews were not changed.
- Chemistry used 019 against 063; native validators, source ledger and contract use 063. The initially guessed PMC PDF route returned HTML; actual page scans and a public original PDF were subsequently obtained.
- This review flags the source-to-structure conflict, not chemical invalidity of the shorter peptide. The normalized InChI amide representation is a resolved non-finding.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T202622Z-magainin-g-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of magainin G
started_at: '2026-10-21T20:11:21Z'
finished_at: '2026-10-21T20:26:22Z'
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
summary: The native structure is internally consistent and matches current PubChem,
  but it lacks the Gly residue explicitly retained after the added N-terminal beta-alanine
  in the adopted original magainin G sequence. This confirmed structure-to-primary-source
  conflict blocks exact identity sign-off. Published G activity must remain attached
  to the stated 24-residue material until the source mapping is corrected.
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
  - path: data/antibiotics/antibacterial/magainin-g.yaml
    sha256: 41f6d8ad5ffddd3e7f75cb018f095082b0bfa75a766ed1fc862151f33d44917a
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
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
targets:
- target_id: antibioticmech:aro-40a2a87cc8
  path: data/antibiotics/antibacterial/magainin-g.yaml
  label: magainin G
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted exact ARO identity, definition, class and citation lead
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact peptide chemical encoding
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: CARD/ARO inventory extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Source classification policy
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
scope:
  description: Entire native record, sole adopted original, both identifiers, broader
    peptide class, source concept and all three history events; current ARO/PubChem,
    independent peptide assembly, original page scans and synthesis patent sequence
    comparison.
  selection: Initially uncovered queue position 626; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-40a2a87cc8
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-40a2a87cc8
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    626
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-40a2a87cc8
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/magainin-g.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-40a2a87cc8
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/magainin-g.yaml --out /private/tmp/am-review-session/626-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: sequence-comparison
  name: sequence-comparison
  status: passed
  required: false
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/626-sequence-check.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual scratch helper exited 0 from 063; successful deterministic checks
    do not resolve the primary identity conflict.
  target_ids:
  - antibioticmech:aro-40a2a87cc8
- check_id: tautomer-normalization
  name: tautomer-normalization
  status: passed
  required: false
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/626-normalization-diagnostic.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual scratch helper exited 0 from 063; successful deterministic checks
    do not resolve the primary identity conflict.
  target_ids:
  - antibioticmech:aro-40a2a87cc8
- check_id: source-ledger
  name: source-ledger
  status: passed
  required: false
  command: /private/tmp/antibioticmech-record-reviews-063/.venv/bin/python /private/tmp/am-review-session/626-ledger.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual scratch helper exited 0 from 063; successful deterministic checks
    do not resolve the primary identity conflict.
  target_ids:
  - antibioticmech:aro-40a2a87cc8
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-40a2a87cc8
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
  - antibioticmech:aro-40a2a87cc8
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
  - antibioticmech:aro-40a2a87cc8
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
  - antibioticmech:aro-40a2a87cc8
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
  - antibioticmech:aro-40a2a87cc8
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
  - antibioticmech:aro-40a2a87cc8
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
  - antibioticmech:aro-40a2a87cc8
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
  - antibioticmech:aro-40a2a87cc8
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
  - antibioticmech:aro-40a2a87cc8
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/magainin-g.yaml
  locator: Entire native; 626-inspect.json and 626-source-rows.json
  accessed_at: '2026-10-21T20:15:52Z'
  support: supports
  summary: SEEDED/MINTED ARO-derived record contains a synthetic-analogue definition,
    one peptide parent/class, two xrefs, one source concept and three seed events.
    No separate structured mechanism, target, resistance, activity, producer, clinical,
    dataset or causal-graph objects occur. Sixteen captured inputs preserve all thirteen
    initial hashes.
  snapshot_sha256: 28c1e07d27047d52e68a9af76679fcd5b85cdc10800e09ca4e704b4092262935
- evidence_id: chemical
  kind: validation
  reference: Native SMILES/InChI and PubChem CID16132425
  locator: 626-chemistry.json; 626-sequence-check.json; 626-normalization-diagnostic.json
  accessed_at: '2026-10-21T20:15:52Z'
  support: supports
  summary: Native and current PubChem encodings give MGYZVMMHKLKEHR-QTRCTKFUSA-N,
    C117H187N31O28S, charge 0 and 23 configured stereocentres. Independent construction
    of beta-Ala-I-G-K-F-L-H-S-A-K-K-F-A-K-A-F-V-A-E-I-M-N-S-NH2 matches the native
    graph reciprocally with chirality. The raw InChI mismatch resolves after 24 local
    imidic-acid-to-amide transfers without changing tetrahedral tags.
  snapshot_sha256: 5d54d7de4ec6f36ea7402a73c300e9f52f12353e773d7a8b0aa19660e84c1818
- evidence_id: primary-sequence
  kind: primary_source
  reference: PMID:2285300
  locator: DOI:10.1128/aac.34.9.1824; actual printed page 1824 peptide sequence; 626-1990-p1824-hires.png
  accessed_at: '2026-10-21T20:15:52Z'
  support: refutes
  summary: 'The adopted original prints G as beta-Ala-G-I-G-K-F-L-H-S-A-K-K-F-A-K-A-F-V-A-E-I-M-N-S-NH2:
    a 24-residue extension. The native encodes a 23-residue replacement of Gly1 instead.
    This is a positive sequence conflict, not an inference from a name or absent database
    entry.'
  snapshot_sha256: 25cdf1ec797e7f173dfd0169377e3a400c7b23c63d1f081a8b031efceaffec84
- evidence_id: sequence-map
  kind: validation
  reference: Independent sequence-to-graph comparison
  locator: 626-sequence-check.py and 626-sequence-check.json
  accessed_at: '2026-10-21T20:15:52Z'
  support: refutes
  summary: Assembling the printed 24-residue sequence with its C-terminal amide gives
    diagnostic formula C119H190N32O29S and key IEGIJVQYFOYCMV-ZAJZLZNTSA-N. Its difference
    from native is one glycyl residue, C2H3NO and 57.021463716 Da. This candidate
    is a diagnostic structure, not a source-adopted replacement or a confirmed new
    PubChem identifier.
  snapshot_sha256: 5d54d7de4ec6f36ea7402a73c300e9f52f12353e773d7a8b0aa19660e84c1818
- evidence_id: patent
  kind: primary_source
  reference: https://patents.google.com/patent/US5221732A/en
  locator: Original patent PDF Table 1, scientific description, synthesis/assay methods,
    Table 3 and claims 9–11; actual Table 1 and claim pages viewed
  accessed_at: '2026-10-21T20:15:52Z'
  support: supports
  summary: The inventors distinguish the 23-residue replacement in claim 9 from the
    24-residue extension in claim 11; Table 1 labels the extended Ser8-containing
    analogue G. These are distinct peptide designs. The patent supplies bacterial
    growth-inhibition context for named G but does not make the two structures equivalent.
  snapshot_sha256: b11506108b20c42700706e1f269707a7831df446edd3c478560c1cf37debd634
- evidence_id: activity
  kind: primary_source
  reference: PMID:2285300
  locator: All original pages 1824–1826; methods, results, discussion and Figure 1
    caption
  accessed_at: '2026-10-21T20:15:52Z'
  support: partial
  summary: The stated G material produces concentration- and time-dependent protozoal
    injury. Morphology, motility and membrane leakage are the endpoints, with regrowth
    assessed separately; they are not MIC or direct protein-binding measurements.
    Actual Figure 1 concerns B. The paper also describes B/G antibacterial activity,
    referring to earlier synthesis work; these observations cannot silently validate
    the shorter native G graph.
  snapshot_sha256: 25cdf1ec797e7f173dfd0169377e3a400c7b23c63d1f081a8b031efceaffec84
- evidence_id: authorities
  kind: authority
  reference: ARO:3003569; ARO:3000053; pubchem.compound:16132425
  locator: Current official ARO blocks from 620-current-aro.obo; 626-current-aro-blocks.txt;
    current PUG REST properties and synonyms
  accessed_at: '2026-10-21T20:15:52Z'
  support: partial
  summary: Current ARO repeats the adopted definition and PubChem xref. The peptide
    parent is broader and structurally appropriate. Current PubChem repeats the shorter
    native sequence. A fresh exact-key lookup for the diagnostic extension returned404,
    so no replacement CID is asserted.
  snapshot_sha256: 28c1e07d27047d52e68a9af76679fcd5b85cdc10800e09ca4e704b4092262935
- evidence_id: sources
  kind: primary_source
  reference: PMID:3410055; PMID:1319823; PMID:8706437; PMID:2001767; PMID:1708887
  locator: Complete indexed abstracts; 626-1988-abstract.json and 626-discovery.json
  accessed_at: '2026-10-21T20:15:52Z'
  support: context_only
  summary: The 1988 synthesis abstract concerns magainin2 analogues; its full publisher
    PDF routes returned403. Later lung-cancer, sperm and tumor-cell cytolysis abstracts
    are exact-name or family follow-up with host-cell endpoints. They do not establish
    a direct bacterial protein target or resolve the missing Gly.
  snapshot_sha256: 28c1e07d27047d52e68a9af76679fcd5b85cdc10800e09ca4e704b4092262935
- evidence_id: search
  kind: search
  reference: Exact magainin G discovery and maintained sources
  locator: 626-source-audit.json; 626-fetch1–4.json; initial local hits
  accessed_at: '2026-10-21T20:15:52Z'
  support: supports
  summary: All thirteen exact-phrase discovery titles and twelve available abstracts
    were read, including the sole adopted PMID. The actual ARO inventory and PubChem
    enrichment owners were captured before assessment; no absence of all literature
    is claimed.
  search_scope: Europe PMC exact phrase magainin G, public primary publisher/PMC and
    patent routes, official PubChem exact CID/key. Local rg --no-ignore --hidden across
    data/raw,curation,scripts,src for identifier,label,slug; ignored files included.
    No exhaustive literature absence assertion.
  snapshot_sha256: 28c1e07d27047d52e68a9af76679fcd5b85cdc10800e09ca4e704b4092262935
assessments:
- assessment_id: identity
  area: identity
  topic: Exact G peptide sequence
  outcome: concern
  summary: The native is a chemically valid 23-residue beta-alanine replacement, but
    the adopted original G is the 24-residue extension. Source-to-structure identity
    is not established.
  target_ids:
  - antibioticmech:aro-40a2a87cc8
  evidence_ids:
  - primary-sequence
  - sequence-map
  - patent
- assessment_id: representation
  area: representation
  topic: Encoding and stereo consistency
  outcome: supported
  summary: The existing graph, formula, charge and masses agree internally and with
    current PubChem. Local tautomer normalization explains the apparent raw InChI
    mismatch.
  target_ids:
  - antibioticmech:aro-40a2a87cc8
  evidence_ids:
  - chemical
- assessment_id: grounding
  area: grounding
  topic: Source identifiers and broader peptide class
  outcome: concern
  summary: Both asserted registries resolve and the parent is broader, but the exact
    PubChem mapping conflicts with the sequence in the cited original; current provider
    repetition is not independent identity proof.
  target_ids:
  - antibioticmech:aro-40a2a87cc8
  evidence_ids:
  - authorities
  - primary-sequence
- assessment_id: evidence
  area: evidence
  topic: Exact material and biological endpoints
  outcome: unknown
  summary: The original and patent support activity of the stated G material. Numerical
    activity, protozoal membrane injury and host-cell findings must not be transferred
    across the unresolved peptide identity. No missing direct protein target is inferred.
  target_ids:
  - antibioticmech:aro-40a2a87cc8
  evidence_ids:
  - activity
  - patent
  - sources
- assessment_id: provenance
  area: provenance
  topic: Owner chain and source history
  outcome: supported
  summary: The adopted ARO and PubChem rows reproduce the native, the stable mint
    is correct, and all three seed-history entries remain intact. A future fix belongs
    in the maintained source mapping and seeder workflow.
  target_ids:
  - antibioticmech:aro-40a2a87cc8
  evidence_ids:
  - native
  - chemical
  - search
- assessment_id: coverage
  area: completeness
  topic: Whole-record review and source limits
  outcome: supported
  summary: Every native field and sole adopted reference were reviewed. Optional enrichment
    is separate from the demonstrated identity conflict. No protein/pathway adapter
    applies to the native or this sequence/protozoal-physical-injury follow-up.
  target_ids:
  - antibioticmech:aro-40a2a87cc8
  evidence_ids:
  - native
  - activity
  - search
findings:
- finding_id: F1
  issue_key: magainin-g-missing-n-terminal-gly-source-identity
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: The native G structure omits a Gly retained in the cited original
  description: 'The adopted primary sequence and patent distinguish N-terminal beta-alanine
    addition from Gly1 replacement. Native and current PubChem16132425 encode the
    replacement, lacking C2H3NO relative to the printed G extension. The record therefore
    joins a shorter peptide graph to the cited G identity. The definition also compresses
    the original B/G difference: B has Ala8 whereas G retains Ser8. Database agreement
    does not resolve this positive conflict, and simply changing addition to substitution
    would disconnect the record from its adopted source.'
  target_ids:
  - antibioticmech:aro-40a2a87cc8
  field_paths:
  - chemical_structure
  - xrefs[1]
  - definition
  - definition_source
  evidence_ids:
  - primary-sequence
  - sequence-map
  - patent
  - authorities
  rule_id: One exact structure; cited sequence and chemical graph must agree
  normalization_reason: A missing glycyl residue changes the molecular constitution,
    so the exact-identity conflict is a blocker rather than a major wording issue.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Exact G definition, citation and PubChem mapping
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted peptide structure
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem exact source enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: CARD/ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated identity and structure emission
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained exact-identity adjudication
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - antibioticmech:aro-40a2a87cc8
  description: Reconcile the exact G source mapping against the printed original sequence
    and original synthesis material. Preserve replacement and extension as distinct
    structures. If retaining the cited G identity, obtain an authoritative structure
    mapping for the 24-residue extension, update the maintained PubChem/ARO or curator
    identity lane, and regenerate the exact canary. If retaining the current 23-residue
    graph, identify and cite its actual distinct analogue instead. Rewrite the definition
    to state the adjudicated sequence, terminal modification and Ser/Ala distinction;
    correct the duplicated is and article at the same time. Do not apply the scratch
    candidate or substitute a guessed CID automatically.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Exact G definition, citation and PubChem mapping
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted peptide structure
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem exact source enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: CARD/ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated identity and structure emission
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained exact-identity adjudication
  generator: scripts/extract_source_inventory.py, scripts/enrich_pubchem_structures.py
    and scripts/seed_from_sources.py after exact-source adjudication
  acceptance_checks:
  - The exact selected peptide sequence, terminal amide, residue count, formula and
    all configured centres agree by independent construction and reciprocal chirality-aware
    graph mapping.
  - All exact xrefs and primary citations resolve to the same selected peptide; 23-
    and 24-residue materials are not treated as synonyms.
  - Native definition describes the selected terminal change and relevant B/G residue
    differences accurately.
  - Separately authorized regeneration with just seed-canary ARO:3003569 reproduces
    the correction; schema, strict, term/reference/history and corpus gates pass.
limitations:
- The original 1988 synthesis full text remains inaccessible after public Wiley 403
  responses. The adopted 1990 complete article and original patent provide directly
  inspected sequence evidence.
- Current PubChem and ARO repeat the shorter graph/mapping. The diagnostic extension
  key was not found by exact public PubChem lookup; no corrected database ID or automatic
  structural replacement is proposed.
- Primary G biological results concern the stated 24-residue sequence. Protozoal morphology/motility,
  membrane leakage, bacterial growth inhibition and host cytotoxicity remain different
  endpoints. Figure 1 is B-specific; no G quantitative image measurement was inferred.
- No bacterial gene/protein/pathway, resistance determinant or expression dataset
  is named by the native; iModulonDB is not applicable to this identity/protozoal
  membrane review and no absence inference was made.
- The required shared full-QC gate retains the established SciPy import failure. Focused
  success and draft-contract validation do not replace separately recorded shared
  corpus, term, reference and history checks.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All thirteen initial hashes were preserved; sixteen actual inputs now cover the
  ARO/PubChem owners. Native/source/history files and prior immutable reviews were
  not changed.
- Chemistry used 019 against 063; native validators, source ledger and contract use
  063. The initially guessed PMC PDF route returned HTML; actual page scans and a
  public original PDF were subsequently obtained.
- This review flags the source-to-structure conflict, not chemical invalidity of the
  shorter peptide. The normalized InChI amide representation is a resolved non-finding.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
