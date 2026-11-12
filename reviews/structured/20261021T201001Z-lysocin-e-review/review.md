# Review of lysocin E

- Review: 20261021T201001Z-lysocin-e-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T19:52:50Z
- Finished UTC: 2026-10-21T20:10:01Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The exact native lysocin E structure, nonribosomal-peptide class, qualified CARD menA association and MIBiG producer link are supported. Primary follow-up preserves roles for both menaquinone and Lipid II rather than disproving menaquinone binding. Original-access limits and a current external ChEBI SMILES defect are retained without assigning them to the valid native graph. No confirmed native defect was identified. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire native record, three xrefs, nonribosomal class/parent, menaquinone definition, one menA resistance edge, one compound-specific MIBiG producer object, two adopted PMID leads and five history events; independent structure and primary mechanism/biosynthesis follow-up.

Selection: Initially uncovered queue position 617; one exact record in path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| antibioticmech:aro-b6c9cc2b59 | data/antibiotics/antibacterial/lysocin-e.yaml | generated | lysocin E |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | antibioticmech:aro-b6c9cc2b59 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | antibioticmech:aro-b6c9cc2b59 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | antibioticmech:aro-b6c9cc2b59 | Actual focused execution exited 0. |
| authority-comparison | passed | False | antibioticmech:aro-b6c9cc2b59 | Actual scratch helper exited 0 against 062; expected external provider failure and resolved exploratory attempts are recorded separately. |
| tautomer-diagnostic | passed | False | antibioticmech:aro-b6c9cc2b59 | Actual scratch helper exited 0 against 062; expected external provider failure and resolved exploratory attempts are recorded separately. |
| source-ledger | passed | False | antibioticmech:aro-b6c9cc2b59 | Actual scratch helper exited 0 against 062; expected external provider failure and resolved exploratory attempts are recorded separately. |
| Authoritative full QC | failed | True | antibioticmech:aro-b6c9cc2b59 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | antibioticmech:aro-b6c9cc2b59 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | antibioticmech:aro-b6c9cc2b59 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | antibioticmech:aro-b6c9cc2b59 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | antibioticmech:aro-b6c9cc2b59 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | antibioticmech:aro-b6c9cc2b59 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | antibioticmech:aro-b6c9cc2b59 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | antibioticmech:aro-b6c9cc2b59 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | antibioticmech:aro-b6c9cc2b59 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact native E graph and stereochemistry

identity: supported. Targets: antibioticmech:aro-b6c9cc2b59.

All seven valid encodings and primary residue/structure descriptions agree. The external ChEBI SMILES error and mobile-H import forms do not justify a native identity edit.

### Current xrefs and NRPS class

grounding: supported. Targets: antibioticmech:aro-b6c9cc2b59.

All three asserted xrefs resolve to E and the current ARO NRPS parent is supported by the biosynthesis study. The MINTED state is explicit; a two-star ChEBI xref does not silently promote the native grounding status.

### Menaquinone statement in evolving mechanism evidence

evidence: supported. Targets: antibioticmech:aro-b6c9cc2b59.

The definition is supported as a nonexclusive menaquinone/lysis claim. Lipid II binding and host-dependent potentiation warrant qualified future context, but the later papers do not demonstrate this native statement false.

### Qualified menA association

evidence: supported. Targets: antibioticmech:aro-b6c9cc2b59.

The exact CARD association is present, and later original deletion experiments support men-pathway resistance in their strain/medium context. Original point-mutant details remain unverified; the native does not assert a precise mutation, MIC or direct MenA binding.

### Exact producer and inherited reference scope

provenance: supported. Targets: antibioticmech:aro-b6c9cc2b59.

The current exact MIBiG entry and independent 2020 primary abstract/SI support production and NRPS knock-out linkage in 3655. The native generic taxon and conservative citation disclaimer are not contradicted.

### Whole-record coverage and optional enrichment

completeness: supported. Targets: antibioticmech:aro-b6c9cc2b59.

All assertions and adopted references were assessed. Future exact mechanism/activity enrichment must preserve Lipid II/ApoA-I context, strain/material details and analogue boundaries; no absent optional structured object is automatically a defect.

### Source mint and five seeded history events

provenance: supported. Targets: antibioticmech:aro-b6c9cc2b59.

The source mint is recomputed correctly and the five seeded/reseeded events remain unchanged. This review does not promote status or claim original full-text access that was unavailable.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/lysocin-e.yaml; Entire native; exact source rows; 617-initial-inspect.json and expanded 617-inspect.json | supports | The SEEDED/MINTED ARO-derived record encodes one exact neutral lysocin E structure. The menA claim is explicitly database evidence. The MIBiG object explicitly qualifies its inherited legacy reference and questionable source quality. No separate molecular-target, activity, clinical, dataset or causal-graph objects are present; definition claims were assessed. All thirteen initial hashes remain within nineteen unchanged inputs. |
| identity | PubChem:53373747; CHEBI:220095; MIBiG:BGC0002384.3; 617-authority-check.py;617-authority-chemistry.json;617-normalization-diagnostic.py/.json | supports | Seven valid native/authority/MIBiG encodings agree on QJPVBLGWZKAQRW-BQBICWQZSA-N, C75H116N20O20, charge 0, mass and fifteen mapped stereocentres. InChI import uses twelve imidic-acid and two guanidine mobile-H forms; only local bond/proton transfers, preserving every tetrahedral tag, resolve reciprocal matching. A generic tautomer enumeration limit was diagnosed and not used as identity proof. |
| external-encoding | CHEBI:220095; 617-chebi.json and617-chebi.mol;617-authority-chemistry.json | partial | The current external ChEBI aromatic SMILES cannot kekulize because the indole n omits H. Its official molfile and InChI resolve to the same exact native entity. The native PubChem SMILES is valid and does not share that malformed encoding; the external error does not establish a wrong native graph or wrong xref. |
| structure-primary | PMID:29662210; PMID:31278250; DOI10.1038/s41589-018-0041-4 lysocin identity/Marfey passages; DOI10.1038/s41467-019-10754-4 identity/SAR passages and actual Figure 1 | supports | The originals distinguish E from I/J and synthetic library analogues. They specify the twelve amino-acid residues and configurations, including D-Trp, N-Me-D-Phe and L-Ile, and the 2019 source explicitly preserves the R-3-hydroxy-5-methylhexanoyl group. These agree with the native mapped stereocentres and 37-membered depsipeptide ring; glycine remains achiral. |
| original | PMID:25485686; DOI10.1038/nchembio.1710; complete indexed original abstract in617-adopted.json | partial | The original reports exact E isolation and direct menaquinone interaction associated with bactericidal action. Its complete main paper, exact point-mutant table and supplement were not recovered through the public routes attempted, so fine experimental details from search leads were not promoted to verified primary evidence. |
| lipidII | PMID:29662210; 617-PMC5964011.xml; lysocin Results/Discussion, mutant susceptibility, polymerization and bead-binding Methods | supports | The 2018 original questions whether menaquinone is the primary membrane target, finds men/heme-null resistance not uniquely diagnostic, and demonstrates exact E binding to Lipid II by affinity capture and substrate-dependent inhibition of polymerization. It permits noncompetitive simultaneous interaction or weaker menaquinone affinity. These results establish additional mechanism context; they do not deny every menaquinone interaction. |
| combined-model | PMID:34737305; 617-PMC8568920.xml; Results on lipidII/menaquinone/ApoA-I, Discussion, relevant binding, lipid, susceptibility and liposome Methods; Figure 4 caption | supports | The 2021 original confirms affinities for both lipids, shows menaquinone-dependent disruption in its liposome system, and links host ApoA-I/Lipid II to enhanced antibacterial activity. Its sequential loading/transfer model remains proposed. menA/menB deletion strains remain resistant in the specified TSB experiments. The native nonexclusive menaquinone/lysis statement is compatible with this evidence, while an exclusive universal mechanism would not be established. |
| CARD | ARO:3003915; ARO:3003917; ARO:3003919; ARO:3009657; 617-current-aro-blocks.txt; official 426-current-aro.obo with 426-fetch2-results.json provenance; adopted resistance/source rows | supports | All four current terms resolve, including the exact menA confers_resistance_to_antibiotic lysocin E edge and NRPS parent. The native retains the CARD source tier. menA is a biosynthetic resistance determinant, not an asserted direct lysocin-binding protein; class membership is not experimental mutation proof. |
| adapter | kg-microbe-sources iModulonDB; 617-adapter-menA.txt;617-source-audit.json adapter; successful606 dataset inventory reused | supports | Before menA primary follow-up, the targeted search exited 0 and resolved menA at s_aureus/staph_precise108/USA300HOU_RS05180; ubiE was an additional product-substring hit. No iModulon component was returned, so summarize did not apply. Gene membership is not evidence for resistance or the original mutant strain. |
| producer | MIBiG:BGC0002384.3; NCBITaxon:72226; Exact official version annotations and taxon response:617-mibig-v3.json;617-taxonomy.xml | supports | The active questionable-quality entry has one exact E compound, NRPS class, locusMT410681.1, knock-out evidence, generic Lysobacter sp. taxon72226 and the same first legacy PMID32610008. Exact graph matching confirms the compound join. The native COMPOUND_SPECIFIC scope and inherited-reference disclaimer reproduce that source faithfully. |
| biosynthesis | PMID:32610008; DOI10.1021/acssynbio.0c00067; complete original abstract; official SI Tables S1/S2/S5, captions S2–S10, actual Figure S3 PDF page 11 and Figure S6 page 14 | supports | The original identifies exact E as compound 2 from Lysobacter sp.3655, distinguishes promoter-engineered strains, and describes ORF2698/lesA deletion and complementation. Actual SI FigureS3 shows the E structure and HRMS; FigureS6 compares WT/deletion production with standard compound 2. This independently supports the producer link beyond the conservatively inherited native citation. Official SI MD5 matches; full main remained inaccessible. |
| analogue-boundary | PMID:40656540; 617-PMC12243021.xml; synthesis, antagonization, ITC and microscopy Results | context_only | The 2025 experiments use Hex-LysE 37 with an altered achiral N-terminal lipid. Its nanomolar binding values and membrane images are not transferred to native lysocin E. Exact E and derivatives remain separate despite the paper title/abstract using family names. |
| owners | Adopted ARO, PubChem and MIBiG inventories; extraction and seeding owners; 617-source-rows.json;617-source-audit.json; scripts/enrich_pubchem_structures.py,extract_source_inventory.py,extract_mibig_producers.py,seed_from_sources.py | supports | Maintained input paths are captured before scientific assessment. The seeder attaches the producer by exact key, requires eligible experimental linkage and complete stereo, and labels single-compound versus inherited scopes. The generic initial ChEBI owner description was replaced with actual ARO/PubChem/MIBiG ownership without changing original hashes. |
| discovery | Europe PMC exact lysocin E query; 617-discovery.json;617-source-audit.json dispositions | supports | All 75 returned titles were inspected; both adopted complete abstracts and seven selected follow-up complete abstracts were read. Selected primary full passages were then inspected. Secondary reviews and modified compounds do not supply unqualified native claims; the search is bounded rather than proof of literature absence. |

## Limits And Additional Notes

- The adopted 2015 full main, exact point-mutant table and SI were unavailable. Its complete original abstract was read; search-indexed mutant details were kept as leads. Later full primary experiments provide additional support with their own contexts.
- The 2020 full main was inaccessible. Its complete original abstract and selected official SI tables/captions and actual Figures S3/S6 were read; all spectra and engineered complementation data were not independently reanalysed.
- The 2018 and2021 mechanism papers differ in their proposed dominant target interpretation. Both lipid interactions remain supported; their sequence, relative contribution and host dependence are not generalized beyond inspected experiments.
- The 2025 Hex-LysE results concern a chemically modified analogue and were excluded from exact-native affinity/activity transfer.
- The external current ChEBI SMILES is malformed, but native SMILES, ChEBI molfile/InChI and other encodings match. Generic tautomer enumeration reached its limit; explicit local mobile-H transformations resolved the native comparison without altering tetrahedral stereo.
- Actual2018 Figure 5 and2021 Figure 4 image routes returned HTML placeholders. Their original methods/results/captions were read, and no plot-derived numerical values were adopted.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All thirteen initial inputs are preserved within nineteen verified hashes. Native records, maintained sources, status and history were not edited. Root owns immutable saving and shared-gate integration.
- Standalone chemistry used019 against 062; native schema/strict, ledger and contract used 062. An incorrect guessed extractor path, limited general tautomer enumeration and unavailable fitz renderer were corrected with the actual extractor, explicit local chemistry diagnostic and pdftoppm; actual attempts are recorded in617-source-audit.json.
- Optional future curation may add exact E Lipid II/ApoA-I mechanism context and strain 3655 detail through the maintained owners. It should not relabel the database menA association as a direct MenA binding target or erase source conflicts.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T201001Z-lysocin-e-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of lysocin E
started_at: '2026-10-21T19:52:50Z'
finished_at: '2026-10-21T20:10:01Z'
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
summary: The exact native lysocin E structure, nonribosomal-peptide class, qualified
  CARD menA association and MIBiG producer link are supported. Primary follow-up preserves
  roles for both menaquinone and Lipid II rather than disproving menaquinone binding.
  Original-access limits and a current external ChEBI SMILES defect are retained without
  assigning them to the valid native graph. No confirmed native defect was identified.
  Scientific assessment retains the stated evidence limits; full verification is blocked
  by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/lysocin-e.yaml
    sha256: 4ad84ad448ec7255fd3066ab01abfedd579268e2ab6c05bf9dc2d8bce7fc4a3d
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
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: data/raw/mibig_producers.tsv
    sha256: d55289619e77e035ed437d432dd692ab382f254c3841c9a314752ef22578a01b
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
    role: context
  - path: scripts/extract_mibig_producers.py
    sha256: a078cdf4c9b2d09999800ab7ae03f93d3972f29b7d2f460ebbbe7d7ec6b31c53
    role: context
targets:
- target_id: antibioticmech:aro-b6c9cc2b59
  path: data/antibiotics/antibacterial/lysocin-e.yaml
  label: lysocin E
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted definition, class, identifiers and primary lead
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Exact adopted menA resistance association
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Adopted exact chemical encoding
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/mibig_producers.tsv
    role: Exact compound-key producer linkage and inherited-reference qualifier
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: CARD/ARO inventory extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: PubChem structure extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_mibig_producers.py
    role: MIBiG producer extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Role and source policy
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
scope:
  description: Entire native record, three xrefs, nonribosomal class/parent, menaquinone
    definition, one menA resistance edge, one compound-specific MIBiG producer object,
    two adopted PMID leads and five history events; independent structure and primary
    mechanism/biosynthesis follow-up.
  selection: Initially uncovered queue position 617; one exact record in path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - antibioticmech:aro-b6c9cc2b59
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-b6c9cc2b59
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    617
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-b6c9cc2b59
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/lysocin-e.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - antibioticmech:aro-b6c9cc2b59
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/lysocin-e.yaml --out /private/tmp/am-review-session/617-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-comparison
  name: authority-comparison
  status: passed
  required: false
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/617-authority-check.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual scratch helper exited 0 against 062; expected external provider
    failure and resolved exploratory attempts are recorded separately.
  target_ids:
  - antibioticmech:aro-b6c9cc2b59
- check_id: tautomer-diagnostic
  name: tautomer-diagnostic
  status: passed
  required: false
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/617-normalization-diagnostic.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual scratch helper exited 0 against 062; expected external provider
    failure and resolved exploratory attempts are recorded separately.
  target_ids:
  - antibioticmech:aro-b6c9cc2b59
- check_id: source-ledger
  name: source-ledger
  status: passed
  required: false
  command: /private/tmp/antibioticmech-record-reviews-062/.venv/bin/python /private/tmp/am-review-session/617-ledger.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual scratch helper exited 0 against 062; expected external provider
    failure and resolved exploratory attempts are recorded separately.
  target_ids:
  - antibioticmech:aro-b6c9cc2b59
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - antibioticmech:aro-b6c9cc2b59
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
  - antibioticmech:aro-b6c9cc2b59
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
  - antibioticmech:aro-b6c9cc2b59
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
  - antibioticmech:aro-b6c9cc2b59
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
  - antibioticmech:aro-b6c9cc2b59
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
  - antibioticmech:aro-b6c9cc2b59
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
  - antibioticmech:aro-b6c9cc2b59
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
  - antibioticmech:aro-b6c9cc2b59
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
  - antibioticmech:aro-b6c9cc2b59
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/lysocin-e.yaml
  locator: Entire native; exact source rows; 617-initial-inspect.json and expanded
    617-inspect.json
  accessed_at: '2026-10-21T20:07:36Z'
  support: supports
  summary: The SEEDED/MINTED ARO-derived record encodes one exact neutral lysocin
    E structure. The menA claim is explicitly database evidence. The MIBiG object
    explicitly qualifies its inherited legacy reference and questionable source quality.
    No separate molecular-target, activity, clinical, dataset or causal-graph objects
    are present; definition claims were assessed. All thirteen initial hashes remain
    within nineteen unchanged inputs.
  snapshot_sha256: 6f698f67d0d1ca4240db4125276e328dd69967be3a0d19feb19012c7dbaf5eab
- evidence_id: identity
  kind: validation
  reference: PubChem:53373747; CHEBI:220095; MIBiG:BGC0002384.3
  locator: 617-authority-check.py;617-authority-chemistry.json;617-normalization-diagnostic.py/.json
  accessed_at: '2026-10-21T20:07:36Z'
  support: supports
  summary: Seven valid native/authority/MIBiG encodings agree on QJPVBLGWZKAQRW-BQBICWQZSA-N,
    C75H116N20O20, charge 0, mass and fifteen mapped stereocentres. InChI import uses
    twelve imidic-acid and two guanidine mobile-H forms; only local bond/proton transfers,
    preserving every tetrahedral tag, resolve reciprocal matching. A generic tautomer
    enumeration limit was diagnosed and not used as identity proof.
  snapshot_sha256: c97612021cc27c44d47168c45891885a454b373c0979e848bf8efedacac57646
- evidence_id: external-encoding
  kind: authority
  reference: CHEBI:220095
  locator: 617-chebi.json and617-chebi.mol;617-authority-chemistry.json
  accessed_at: '2026-10-21T20:07:36Z'
  support: partial
  summary: The current external ChEBI aromatic SMILES cannot kekulize because the
    indole n omits H. Its official molfile and InChI resolve to the same exact native
    entity. The native PubChem SMILES is valid and does not share that malformed encoding;
    the external error does not establish a wrong native graph or wrong xref.
  snapshot_sha256: 1e8ebb6e7628339fb2c2c23419da2718a8ef22798ac22254a8a0e101f4378f8a
- evidence_id: structure-primary
  kind: primary_source
  reference: PMID:29662210; PMID:31278250
  locator: DOI10.1038/s41589-018-0041-4 lysocin identity/Marfey passages; DOI10.1038/s41467-019-10754-4
    identity/SAR passages and actual Figure 1
  accessed_at: '2026-10-21T20:07:36Z'
  support: supports
  summary: The originals distinguish E from I/J and synthetic library analogues. They
    specify the twelve amino-acid residues and configurations, including D-Trp, N-Me-D-Phe
    and L-Ile, and the 2019 source explicitly preserves the R-3-hydroxy-5-methylhexanoyl
    group. These agree with the native mapped stereocentres and 37-membered depsipeptide
    ring; glycine remains achiral.
  snapshot_sha256: 720d2f02a1fe0b2a77981d817f7d3f67d2bf7d7414da45a32fbd56662cb71935
- evidence_id: original
  kind: primary_source
  reference: PMID:25485686
  locator: DOI10.1038/nchembio.1710; complete indexed original abstract in617-adopted.json
  accessed_at: '2026-10-21T20:07:36Z'
  support: partial
  summary: The original reports exact E isolation and direct menaquinone interaction
    associated with bactericidal action. Its complete main paper, exact point-mutant
    table and supplement were not recovered through the public routes attempted, so
    fine experimental details from search leads were not promoted to verified primary
    evidence.
  snapshot_sha256: 9dd56ba802588cc7e46f481d2cc6f12c8934ffe96c81bdd673c2903bc74f6a1d
- evidence_id: lipidII
  kind: primary_source
  reference: PMID:29662210
  locator: 617-PMC5964011.xml; lysocin Results/Discussion, mutant susceptibility,
    polymerization and bead-binding Methods
  accessed_at: '2026-10-21T20:07:36Z'
  support: supports
  summary: The 2018 original questions whether menaquinone is the primary membrane
    target, finds men/heme-null resistance not uniquely diagnostic, and demonstrates
    exact E binding to Lipid II by affinity capture and substrate-dependent inhibition
    of polymerization. It permits noncompetitive simultaneous interaction or weaker
    menaquinone affinity. These results establish additional mechanism context; they
    do not deny every menaquinone interaction.
  snapshot_sha256: 9309d5c538260a4cc5fe4c2300addbe51febd9ab6002caba7ee286bdc782b75d
- evidence_id: combined-model
  kind: primary_source
  reference: PMID:34737305
  locator: 617-PMC8568920.xml; Results on lipidII/menaquinone/ApoA-I, Discussion,
    relevant binding, lipid, susceptibility and liposome Methods; Figure 4 caption
  accessed_at: '2026-10-21T20:07:36Z'
  support: supports
  summary: The 2021 original confirms affinities for both lipids, shows menaquinone-dependent
    disruption in its liposome system, and links host ApoA-I/Lipid II to enhanced
    antibacterial activity. Its sequential loading/transfer model remains proposed.
    menA/menB deletion strains remain resistant in the specified TSB experiments.
    The native nonexclusive menaquinone/lysis statement is compatible with this evidence,
    while an exclusive universal mechanism would not be established.
  snapshot_sha256: 066f2d5505c9377a994bfa13d04ebc7898d9fac44c81751ee0f954358d676f20
- evidence_id: CARD
  kind: database
  reference: ARO:3003915; ARO:3003917; ARO:3003919; ARO:3009657
  locator: 617-current-aro-blocks.txt; official 426-current-aro.obo with 426-fetch2-results.json
    provenance; adopted resistance/source rows
  accessed_at: '2026-10-21T20:07:36Z'
  support: supports
  summary: All four current terms resolve, including the exact menA confers_resistance_to_antibiotic
    lysocin E edge and NRPS parent. The native retains the CARD source tier. menA
    is a biosynthetic resistance determinant, not an asserted direct lysocin-binding
    protein; class membership is not experimental mutation proof.
  snapshot_sha256: a9c43eb9b42aece1e0eddeeae949841520ed809b0f6fd9ce696b2b96a3db4c14
- evidence_id: adapter
  kind: database
  reference: kg-microbe-sources iModulonDB
  locator: 617-adapter-menA.txt;617-source-audit.json adapter; successful606 dataset
    inventory reused
  accessed_at: '2026-10-21T20:07:36Z'
  support: supports
  summary: Before menA primary follow-up, the targeted search exited 0 and resolved
    menA at s_aureus/staph_precise108/USA300HOU_RS05180; ubiE was an additional product-substring
    hit. No iModulon component was returned, so summarize did not apply. Gene membership
    is not evidence for resistance or the original mutant strain.
  snapshot_sha256: c2a295d9de4e51278832ae6c78ded174eb6c42d4b031679dbb631e0bb9d7e5a0
- evidence_id: producer
  kind: authority
  reference: MIBiG:BGC0002384.3; NCBITaxon:72226
  locator: Exact official version annotations and taxon response:617-mibig-v3.json;617-taxonomy.xml
  accessed_at: '2026-10-21T20:07:36Z'
  support: supports
  summary: The active questionable-quality entry has one exact E compound, NRPS class,
    locusMT410681.1, knock-out evidence, generic Lysobacter sp. taxon72226 and the
    same first legacy PMID32610008. Exact graph matching confirms the compound join.
    The native COMPOUND_SPECIFIC scope and inherited-reference disclaimer reproduce
    that source faithfully.
  snapshot_sha256: 84a770bbd126be6d6193b54ae01786b8caefa59cce506ad5a7e4aaedb0127cf7
- evidence_id: biosynthesis
  kind: primary_source
  reference: PMID:32610008
  locator: DOI10.1021/acssynbio.0c00067; complete original abstract; official SI Tables
    S1/S2/S5, captions S2–S10, actual Figure S3 PDF page 11 and Figure S6 page 14
  accessed_at: '2026-10-21T20:07:36Z'
  support: supports
  summary: The original identifies exact E as compound 2 from Lysobacter sp.3655,
    distinguishes promoter-engineered strains, and describes ORF2698/lesA deletion
    and complementation. Actual SI FigureS3 shows the E structure and HRMS; FigureS6
    compares WT/deletion production with standard compound 2. This independently supports
    the producer link beyond the conservatively inherited native citation. Official
    SI MD5 matches; full main remained inaccessible.
  snapshot_sha256: fe9cc81e3d2d2ae1ec4697114d8d9e5817b6ce03f7b04826b1b09095066123ac
- evidence_id: analogue-boundary
  kind: primary_source
  reference: PMID:40656540
  locator: 617-PMC12243021.xml; synthesis, antagonization, ITC and microscopy Results
  accessed_at: '2026-10-21T20:07:36Z'
  support: context_only
  summary: The 2025 experiments use Hex-LysE 37 with an altered achiral N-terminal
    lipid. Its nanomolar binding values and membrane images are not transferred to
    native lysocin E. Exact E and derivatives remain separate despite the paper title/abstract
    using family names.
  snapshot_sha256: f033fd5fe605eee2982f324c10e66138f842a724cbed832df823cc7868ea97f8
- evidence_id: owners
  kind: record_content
  reference: Adopted ARO, PubChem and MIBiG inventories; extraction and seeding owners
  locator: 617-source-rows.json;617-source-audit.json; scripts/enrich_pubchem_structures.py,extract_source_inventory.py,extract_mibig_producers.py,seed_from_sources.py
  accessed_at: '2026-10-21T20:07:36Z'
  support: supports
  summary: Maintained input paths are captured before scientific assessment. The seeder
    attaches the producer by exact key, requires eligible experimental linkage and
    complete stereo, and labels single-compound versus inherited scopes. The generic
    initial ChEBI owner description was replaced with actual ARO/PubChem/MIBiG ownership
    without changing original hashes.
  snapshot_sha256: 6f698f67d0d1ca4240db4125276e328dd69967be3a0d19feb19012c7dbaf5eab
- evidence_id: discovery
  kind: search
  reference: Europe PMC exact lysocin E query
  locator: 617-discovery.json;617-source-audit.json dispositions
  accessed_at: '2026-10-21T20:07:36Z'
  support: supports
  summary: All 75 returned titles were inspected; both adopted complete abstracts
    and seven selected follow-up complete abstracts were read. Selected primary full
    passages were then inspected. Secondary reviews and modified compounds do not
    supply unqualified native claims; the search is bounded rather than proof of literature
    absence.
  search_scope: Exact phrase lysocin E, Europe PMC resultType=core,pageSize 100; 75
    hits/75 returned. Local owner searches used rg --no-ignore --hidden across curation,conf,scripts,data/raw.
  snapshot_sha256: 00f631bf596612e3e2858300d3944f22ac777cfd2457179b4aa343e2d5bf3f50
assessments:
- assessment_id: identity
  area: identity
  topic: Exact native E graph and stereochemistry
  outcome: supported
  summary: All seven valid encodings and primary residue/structure descriptions agree.
    The external ChEBI SMILES error and mobile-H import forms do not justify a native
    identity edit.
  target_ids:
  - antibioticmech:aro-b6c9cc2b59
  evidence_ids:
  - identity
  - external-encoding
  - structure-primary
  - biosynthesis
- assessment_id: grounding
  area: grounding
  topic: Current xrefs and NRPS class
  outcome: supported
  summary: All three asserted xrefs resolve to E and the current ARO NRPS parent is
    supported by the biosynthesis study. The MINTED state is explicit; a two-star
    ChEBI xref does not silently promote the native grounding status.
  target_ids:
  - antibioticmech:aro-b6c9cc2b59
  evidence_ids:
  - identity
  - CARD
  - biosynthesis
- assessment_id: mechanism
  area: evidence
  topic: Menaquinone statement in evolving mechanism evidence
  outcome: supported
  summary: The definition is supported as a nonexclusive menaquinone/lysis claim.
    Lipid II binding and host-dependent potentiation warrant qualified future context,
    but the later papers do not demonstrate this native statement false.
  target_ids:
  - antibioticmech:aro-b6c9cc2b59
  evidence_ids:
  - original
  - lipidII
  - combined-model
- assessment_id: resistance
  area: evidence
  topic: Qualified menA association
  outcome: supported
  summary: The exact CARD association is present, and later original deletion experiments
    support men-pathway resistance in their strain/medium context. Original point-mutant
    details remain unverified; the native does not assert a precise mutation, MIC
    or direct MenA binding.
  target_ids:
  - antibioticmech:aro-b6c9cc2b59
  evidence_ids:
  - CARD
  - combined-model
  - lipidII
  - adapter
- assessment_id: producer
  area: provenance
  topic: Exact producer and inherited reference scope
  outcome: supported
  summary: The current exact MIBiG entry and independent 2020 primary abstract/SI
    support production and NRPS knock-out linkage in 3655. The native generic taxon
    and conservative citation disclaimer are not contradicted.
  target_ids:
  - antibioticmech:aro-b6c9cc2b59
  evidence_ids:
  - producer
  - biosynthesis
  - owners
- assessment_id: coverage
  area: completeness
  topic: Whole-record coverage and optional enrichment
  outcome: supported
  summary: All assertions and adopted references were assessed. Future exact mechanism/activity
    enrichment must preserve Lipid II/ApoA-I context, strain/material details and
    analogue boundaries; no absent optional structured object is automatically a defect.
  target_ids:
  - antibioticmech:aro-b6c9cc2b59
  evidence_ids:
  - native
  - analogue-boundary
  - discovery
  - owners
- assessment_id: history
  area: provenance
  topic: Source mint and five seeded history events
  outcome: supported
  summary: The source mint is recomputed correctly and the five seeded/reseeded events
    remain unchanged. This review does not promote status or claim original full-text
    access that was unavailable.
  target_ids:
  - antibioticmech:aro-b6c9cc2b59
  evidence_ids:
  - native
  - owners
  - original
findings: []
actions: []
limitations:
- The adopted 2015 full main, exact point-mutant table and SI were unavailable. Its
  complete original abstract was read; search-indexed mutant details were kept as
  leads. Later full primary experiments provide additional support with their own
  contexts.
- The 2020 full main was inaccessible. Its complete original abstract and selected
  official SI tables/captions and actual Figures S3/S6 were read; all spectra and
  engineered complementation data were not independently reanalysed.
- The 2018 and2021 mechanism papers differ in their proposed dominant target interpretation.
  Both lipid interactions remain supported; their sequence, relative contribution
  and host dependence are not generalized beyond inspected experiments.
- The 2025 Hex-LysE results concern a chemically modified analogue and were excluded
  from exact-native affinity/activity transfer.
- The external current ChEBI SMILES is malformed, but native SMILES, ChEBI molfile/InChI
  and other encodings match. Generic tautomer enumeration reached its limit; explicit
  local mobile-H transformations resolved the native comparison without altering tetrahedral
  stereo.
- Actual2018 Figure 5 and2021 Figure 4 image routes returned HTML placeholders. Their
  original methods/results/captions were read, and no plot-derived numerical values
  were adopted.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All thirteen initial inputs are preserved within nineteen verified hashes. Native
  records, maintained sources, status and history were not edited. Root owns immutable
  saving and shared-gate integration.
- Standalone chemistry used019 against 062; native schema/strict, ledger and contract
  used 062. An incorrect guessed extractor path, limited general tautomer enumeration
  and unavailable fitz renderer were corrected with the actual extractor, explicit
  local chemistry diagnostic and pdftoppm; actual attempts are recorded in617-source-audit.json.
- Optional future curation may add exact E Lipid II/ApoA-I mechanism context and strain
  3655 detail through the maintained owners. It should not relabel the database menA
  association as a direct MenA binding target or erase source conflicts.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
