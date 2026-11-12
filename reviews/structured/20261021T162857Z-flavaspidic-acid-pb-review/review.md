# Review of flavaspidic acid PB

- Review: 20261021T162857Z-flavaspidic-acid-pb-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T16:12:20Z
- Finished UTC: 2026-10-21T16:28:57Z
- Reviewer: Codex agent validation_plan (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact PB structure, source occurrence and bounded antioxidant/antibacterial claims are supported. However, CHEBI:26195 requires at least two hydroxy-substituted benzene rings, while this molecule has only one; the other ring contains a gem-dimethyl quaternary carbon that cannot become aromatic by keto–enol tautomerism. The inherited polyphenol parent and opening definition require a maintained-source correction. Registry tautomer differences do not establish a different congener, and quantitative antibacterial and mechanism limits remain.

## Scope And Provenance

Whole SEEDED, EXACT flavaspidic acid PB record: definition, exact systematic synonym, three broader parents, antibacterial role, complete chemical structure, both registry links, source concept and three histories. Both adopted primary leads and additional PB-specific identity/enzyme evidence were checked.

Selection: Queue 443 in isolated batch 045. Original 13 inputs preserved; actual source-lead queue appended before assessment, giving 14 unchanged hashes.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:65898 | data/antibiotics/antibacterial/flavaspidic-acid-pb.yaml | generated | flavaspidic acid PB |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native chemistry | passed | False | CHEBI:65898 | Actual exit 0; molecular, schema and strict-term checks remain distinct from scientific sign-off. |
| Native schema | passed | True | CHEBI:65898 | Actual exit 0; molecular, schema and strict-term checks remain distinct from scientific sign-off. |
| Native strict | passed | True | CHEBI:65898 | Actual exit 0; molecular, schema and strict-term checks remain distinct from scientific sign-off. |
| Independent exact-authority comparison | passed | False | CHEBI:65898 | Eight valid encodings preserve formula and charge and converge under tautomer normalization with stereochemistry removal disabled. Raw different registry keys are retained. |
| Source, reference, term and history ledger | passed | False | CHEBI:65898 | Fourteen unchanged hashes, two adopted references, all source fields, registry dispositions, PB enzyme table row and three histories checked. |
| Structured source adapter | passed | False | CHEBI:65898 | Actual exit 0. Catalogue/gene identity supplies bounded context, not PB binding or antibacterial mechanism. |
| Structured source adapter discarded dataset query | passed | False | CHEBI:65898 | Command actually returned 0, but precise1 was not in the listed dataset catalogue. Its zero-hit result is discarded, not negative evidence; a corrected precise1k query follows. |
| Structured source adapter | passed | False | CHEBI:65898 | Actual exit 0. Catalogue/gene identity supplies bounded context, not PB binding or antibacterial mechanism. |
| Independent formal parent topology check | passed | False | CHEBI:65898 | Exit0 confirms one benzene ring and the nonaromatizable gem-dimethyl ring in each exact compound; this is positive evidence of the formal parent conflict, not a passing classification judgment. |
| Authoritative full QC | failed | True | CHEBI:65898 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:65898 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:65898 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:65898 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:65898 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:65898 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:65898 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:65898 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:65898 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### PB exact identity and synonym

identity: supported. Targets: CHEBI:65898.

Formula, neutral charge, acyl pattern, source synonym, original drawings and authentic-material comparison agree. No family or sibling compound is substituted.

### Parents, role and definition

grounding: concern. Targets: CHEBI:65898.

The CHEBI:26195 parent and polyphenol opening conflict with the exact formal class definition. Other listed parent classes and bounded occurrence/activity statements remain supported.

### Registry scope

grounding: unknown. Targets: CHEBI:65898.

ChemSpider agrees under explicitly documented tautomer normalization. Reaxys is supported only by current source attribution; direct independent registry access failed.

### Antibacterial mode and target

evidence: unknown. Targets: CHEBI:65898.

PB has a measured weak beta-glucuronidase effect, but no inspected experiment connects this to bacterial growth inhibition. Bovine-milk XO and sibling docking results do not establish its antibacterial target.

### Quantitative antibacterial observations

quantity: unknown. Targets: CHEBI:65898.

The original qualitative antibacterial abstract is available, but PB-specific zones, MICs and detailed protocol were not verified. No numerical native observation is asserted.

### Input and audit consistency

ownership: supported. Targets: CHEBI:65898.

Fourteen unchanged inputs and three chronological seeded events preserve provenance. The source-derived parent and definition need a maintained correction; changing only the generated YAML would not persist.

## Findings

### F1: Polyphenol parent conflicts with its two-benzene-ring requirement

major / open / confirmed; issue key: chebi-65898-polyphenol-parent-requires-two-benzene-rings.

The native definition opens with polyphenol and parent_compounds[0] is CHEBI:26195. That class explicitly requires at least two hydroxy-substituted benzene rings. The exact supported molecule contains one benzene ring and one nonaromatic cyclohexadienone ring with a gem-dimethyl quaternary carbon. Ordinary keto–enol tautomerism cannot remove that four-carbon-bond valence constraint. Current ChEBI repeats the conflicting class assignment; its provenance does not make the graph satisfy the class definition.

## Recommended Actions And Acceptance Checks

### A1

Implement a documented maintained-source correction that excludes CHEBI:26195 for this exact record and replaces the opening with A phloroglucinol derivative, retaining the supported occurrence and activity clauses. Use the ChEBI extraction/input ownership lane and regenerate; do not silently patch only the generated YAML or change the valid molecular graph to fit the class. A replacement parent is optional and requires its own exact definition check.

- Generated parent_compounds no longer includes CHEBI:26195 and the definition no longer asserts its incompatible formal class. Preserve the other supported parent classes.
- Preserve exact chemical identity and all structure encodings; one aromatic benzene ring and the gem-dimethyl nonaromatic ring remain correct. Do not aromatize by deleting methyl groups or changing connectivity.
- Document the current upstream conflict and ensure the maintained correction survives extraction and reseeding.
- After authorized curation, rerun molecular checks, schema, strict terms, corpus reproducibility/history and full QC; retain SEEDED until all required native REVIEWED gates are satisfied.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/flavaspidic-acid-pb.yaml; Entire native YAML | supports | PB has a propionyl group on the nonaromatic ring and a butyryl group on the aromatic ring. The systematic 2-bridge/6-propionyl/4,4-dimethyl cyclohexa-2,5-dien-1-one synonym matches the native structure. No quantitative MIC, target, clinical or producer object is asserted. |
| chemistry | CHEBI:65898; ChemSpider:23275363; PubChem CID25096978; 443-authority-chemistry.json;443-chebi.json/.mol;443-chemspider.html;443-pubchem-name.json | supports | Native SMILES/InChI and official ChEBI molfile give C23H28O8, charge 0 and NGODKUCEKYYIFN-UHFFFAOYSA-N. ChemSpider ZKYZZLVDUWSDOJ-UHFFFAOYSA-N and PubChem XGOUJSICOGRIKX-UHFFFAOYSA-N use alternative keto–enol depictions. All eight encodings converge under explicit canonical tautomer normalization preserving sp3 and bond stereo. No different acyl congener or configured stereoisomer is demonstrated. |
| authority | CHEBI:65898; CHEBI:26195; CHEBI:55380; CHEBI:76224; CHEBI:33282; 443-chebi.json and shared 442 term snapshots | supports | Current ChEBI repeats the native identity, definition and polyphenol parent, so simple source refresh would retain the classification conflict. The exact CHEBI:26195 definition requires two or more benzene rings, each bearing hydroxy. Beta-hydroxy ketone and aromatic ketone remain supported, and PB correctly lacks the methyl-ketone parent used for AB. |
| antioxidant | PMID:12951487; DOI:10.1248/bpb.26.1354; 442-original2003.pdf full original; compound 1 in Figure 1/Table 1, printed p1355, visually read | supports | PB is compound 1, with propionyl substituent R=CH2CH3, distinguished from AB compound 2 R=CH3. It was isolated from D. crassirhizoma rhizomes, voucher CNU 1011. PB DPPH, superoxide and rat-brain lipid-peroxidation IC50 values are 71.7, 58.6 and 12.9 µM. The paper supports the radical-scavenging definition; proposed iron chelation in that experiment is not a bacterial molecular target. |
| antibacterial | PMID:19471878; DOI:10.1007/s12272-009-1502-9; 443-adopted-core.json both complete adopted abstracts;442-PMC7091015.xml original antibacterial abstract | supports | The antibacterial original describes isolated, spectrally characterized PB and AB tested by the paper-disc method, with Gram-positive activity including source-described MRSA S. aureus KCTC 1928, S. mutans and B. subtilis. No exact per-congener zone or MIC value is imported because the main tables were not retrieved. Negative fungi/chlorella outcomes remain bounded to the tested panel. |
| early-identity | DOI:10.1248/cpb.30.4102; 443-original1982.pdf all five scanned pages visually read; Chart 1 p4103; PB experimental paragraph p4105 | supports | The original isolates PB as compound I from D. abbreviata in Turkey and reports matching melting point/spectra and identity with authentic PB. Chart 1 matches the native acyl pattern; experimental MS gives molecular ion 432 and C23H28O8. This separately supports identity, without conflating D. abbreviata with the native D. crassirhizoma occurrence. |
| later-isolation | PMID:33383880; DOI:10.3390/molecules26010122; 442-PMC7796287.xml selected isolation, PB compound 3 physicochemical data, Tables 1/2 and methods | supports | PB compound 3 is separately purified and assigned C23H28O8 with [M-H]- m/z431.1705 and propionyl/butyryl NMR data. Its xanthine-oxidase experiment uses bovine-milk enzyme; the measured noncompetitive inhibition does not establish a bacterial target. |
| enzyme | PMID:36295840; DOI:10.3390/metabo12100938; 443-PMC9610990.xml compound list, Table 1 row23, Results and Methods4.1–4.4 | context_only | PB is compound 23, tested against commercial E. coli beta-glucuronidase G7396 with PNPG substrate. Its IC50 is 76.5 ± 1.5 µM and inhibition at 100 µM is 73.5 ± 0.7%. Kinetic and docking analyses were restricted to compounds 13–15 and 26–28, not PB. This is enzyme inhibition, not evidence connecting beta-glucuronidase to PB antibacterial growth effects or establishing PB direct binding. |
| adapter | iModulonDB e_coli/precise1k/b1617; 443-adapter-results.json;443-adapter-corrected-results.json | context_only | Before enzyme-paper follow-up, datasets returned 0. An initial precise1 query used an unlisted dataset and its zero hits were discarded. Corrected precise1k uidA search returned gene b1617 beta-glucuronidase and no components. This is gene-catalogue identity, not PB binding, enzyme inhibition or growth evidence. |
| owners | Maintained ChEBI source lane; 443-raw-rows.json;443-source-audit.json;ChEBI extractor field mapping and seeder | supports | All imported fields, exact synonym and both citation leads agree with the frozen row. Original 13 hashes remain intact and source-lead queue gives 14 unchanged inputs; three chronological histories remain appropriate to SEEDED status. |
| validation | Actual focused checks; 443-focused-results.json;443-chemistry.json;443-schema.log;443-strict.log;443-ledger.log | supports | Native chemistry, schema, strict terms, independent authority comparison and source ledger all exit 0. These checks do not establish a bacterial mode or authorize REVIEWED status. |
| access | Bounded exact-PB public research; 443-local-hits.txt ignored-inclusive data/curation/conf/scripts/src/tests search;443-fetch1/2.json;shared 442-fetch1/2/3.json | context_only | Native-key PubChem lookup 404 was followed by a name lookup and independent tautomer comparison. Reaxys 2684769 returned 403. The antibacterial main PDF attempts returned HTML or 403; OA metadata routes returned 404. The 1982 scanned PDF was read as images. BB, isoflavaspidic PB and AB/nor-AB fraction studies were kept outside exact-PB antibacterial mechanism evidence. |
| ring-topology | Native graph; CHEBI:26195 definition; original structure drawing; 442443-ring-audit.json;442443-ring-check.py;442443-ring-check.log;442-chebi-26195.json; original2003 Figure1 printedp1355 | refutes | Both native graphs have exactly two six-carbon rings, only one aromatic. In the other ring, zero-based atom17 has four carbon-carbon single bonds, including two methyl substituents, and zero hydrogens. It cannot become a benzene carbon while preserving connectivity. All584 enumerated keto–enol tautomers have at most one benzene ring. This refutes the formal two-benzene requirement, not the published exact structure or broad natural-products use of polyphenolic. |

## Limits And Additional Notes

- Independent Reaxys 2684769 identity remains unresolved. ChemSpider/PubChem raw keys differ because of keto–enol depictions; the review reports normalization explicitly rather than asserting equal raw representations.
- The 2009 antibacterial main tables and methods were not retrieved; no numerical PB potency or source-described MRSA strain status is independently reclassified.
- The beta-glucuronidase assay does not demonstrate a PB antibacterial causal mechanism. PB was not among the compounds subjected to competitive kinetics or docking, and no such relation is transferred.
- Structured search initially used an unlisted precise1 dataset despite exit 0; that result was discarded and corrected to precise1k. Neither result is compound-effect evidence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Standalone chemistry used the batch 019 interpreter against batch 045; ledger and contract use batch 045. Shared 442 primary artifacts retain their actual manifests and hashes.
- No native protein claim required adapter correction. An additional exact-PB bacterial-enzyme lead prompted the bounded adapter query before source follow-up.
- All native bytes and scientific status remain unchanged; optional absent measurements or target fields are not treated as errors.
- Before saving, an independent reviewer raised the formal polyphenol requirement. A separate atom-level recheck confirmed it, and this unsaved review was revised. Broad natural-products terminology is distinguished from the explicit ontology constraint.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T162857Z-flavaspidic-acid-pb-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of flavaspidic acid PB
started_at: '2026-10-21T16:12:20Z'
finished_at: '2026-10-21T16:28:57Z'
reviewer:
  identity: Codex agent validation_plan
  kind: agent
  independence: independent
  independence_basis: The reviewer independently read the entire PB native record,
    preserved original input hashes, checked its own authority structures and systematic
    synonym, and mapped PB-specific passages in shared original papers. Earlier AB
    conclusions were not substituted for PB measurements.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: Major formal parent/definition conflict; exact chemical identity supported
scientific_review: true
summary: The exact PB structure, source occurrence and bounded antioxidant/antibacterial
  claims are supported. However, CHEBI:26195 requires at least two hydroxy-substituted
  benzene rings, while this molecule has only one; the other ring contains a gem-dimethyl
  quaternary carbon that cannot become aromatic by keto–enol tautomerism. The inherited
  polyphenol parent and opening definition require a maintained-source correction.
  Registry tautomer differences do not establish a different congener, and quantitative
  antibacterial and mechanism limits remain.
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
  - path: data/antibiotics/antibacterial/flavaspidic-acid-pb.yaml
    sha256: f25406af901ea5863d4cd834dfc3fd176a19a225375e8ce3a534dea4110b24f4
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
scope:
  description: 'Whole SEEDED, EXACT flavaspidic acid PB record: definition, exact
    systematic synonym, three broader parents, antibacterial role, complete chemical
    structure, both registry links, source concept and three histories. Both adopted
    primary leads and additional PB-specific identity/enzyme evidence were checked.'
  selection: Queue 443 in isolated batch 045. Original 13 inputs preserved; actual
    source-lead queue appended before assessment, giving 14 unchanged hashes.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:65898
targets:
- target_id: CHEBI:65898
  path: data/antibiotics/antibacterial/flavaspidic-acid-pb.yaml
  label: flavaspidic acid PB
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
checks:
- check_id: chemistry
  name: Native chemistry
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    443
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Actual exit 0; molecular, schema and strict-term checks remain distinct
    from scientific sign-off.
  target_ids:
  - CHEBI:65898
  evidence_ids:
  - validation
- check_id: schema
  name: Native schema
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/flavaspidic-acid-pb.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Actual exit 0; molecular, schema and strict-term checks remain distinct
    from scientific sign-off.
  target_ids:
  - CHEBI:65898
  evidence_ids:
  - validation
- check_id: strict
  name: Native strict
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/flavaspidic-acid-pb.yaml --out /private/tmp/am-review-session/443-strict.tsv
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Actual exit 0; molecular, schema and strict-term checks remain distinct
    from scientific sign-off.
  target_ids:
  - CHEBI:65898
  evidence_ids:
  - validation
- check_id: authority
  name: Independent exact-authority comparison
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/443-authority-check.py
    > /private/tmp/am-review-session/443-authority-check.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Eight valid encodings preserve formula and charge and converge under tautomer
    normalization with stereochemistry removal disabled. Raw different registry keys
    are retained.
  target_ids:
  - CHEBI:65898
  evidence_ids:
  - chemistry
- check_id: ledger
  name: Source, reference, term and history ledger
  command: .venv/bin/python /private/tmp/am-review-session/443-ledger.py > /private/tmp/am-review-session/443-ledger.log
    2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Fourteen unchanged hashes, two adopted references, all source fields, registry
    dispositions, PB enzyme table row and three histories checked.
  target_ids:
  - CHEBI:65898
  evidence_ids:
  - owners
- check_id: adapter-initial-0
  name: Structured source adapter
  command: PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Actual exit 0. Catalogue/gene identity supplies bounded context, not PB
    binding or antibacterial mechanism.
  target_ids:
  - CHEBI:65898
  evidence_ids:
  - adapter
- check_id: adapter-initial-1
  name: Structured source adapter discarded dataset query
  command: PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset precise1 --query uidA
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Command actually returned 0, but precise1 was not in the listed dataset
    catalogue. Its zero-hit result is discarded, not negative evidence; a corrected
    precise1k query follows.
  target_ids:
  - CHEBI:65898
  evidence_ids:
  - adapter
- check_id: adapter-corrected-0
  name: Structured source adapter
  command: PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset precise1k --query uidA
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Actual exit 0. Catalogue/gene identity supplies bounded context, not PB
    binding or antibacterial mechanism.
  target_ids:
  - CHEBI:65898
  evidence_ids:
  - adapter
- check_id: ring-topology
  name: Independent formal parent topology check
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/442443-ring-check.py
    > /private/tmp/am-review-session/442443-ring-check.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Exit0 confirms one benzene ring and the nonaromatizable gem-dimethyl ring
    in each exact compound; this is positive evidence of the formal parent conflict,
    not a passing classification judgment.
  target_ids:
  - CHEBI:65898
  evidence_ids:
  - ring-topology
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:65898
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
  - CHEBI:65898
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
  - CHEBI:65898
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
  - CHEBI:65898
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
  - CHEBI:65898
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
  - CHEBI:65898
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
  - CHEBI:65898
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
  - CHEBI:65898
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
  - CHEBI:65898
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/flavaspidic-acid-pb.yaml
  locator: Entire native YAML
  accessed_at: '2026-10-21T16:21:23Z'
  support: supports
  summary: PB has a propionyl group on the nonaromatic ring and a butyryl group on
    the aromatic ring. The systematic 2-bridge/6-propionyl/4,4-dimethyl cyclohexa-2,5-dien-1-one
    synonym matches the native structure. No quantitative MIC, target, clinical or
    producer object is asserted.
- evidence_id: chemistry
  kind: validation
  reference: CHEBI:65898; ChemSpider:23275363; PubChem CID25096978
  locator: 443-authority-chemistry.json;443-chebi.json/.mol;443-chemspider.html;443-pubchem-name.json
  accessed_at: '2026-10-21T16:21:23Z'
  support: supports
  summary: Native SMILES/InChI and official ChEBI molfile give C23H28O8, charge 0
    and NGODKUCEKYYIFN-UHFFFAOYSA-N. ChemSpider ZKYZZLVDUWSDOJ-UHFFFAOYSA-N and PubChem
    XGOUJSICOGRIKX-UHFFFAOYSA-N use alternative keto–enol depictions. All eight encodings
    converge under explicit canonical tautomer normalization preserving sp3 and bond
    stereo. No different acyl congener or configured stereoisomer is demonstrated.
  snapshot_sha256: 46873ad5e90a4198dce4e0541d2c3150f55ba0487998e0055e719167caecb11e
- evidence_id: authority
  kind: authority
  reference: CHEBI:65898; CHEBI:26195; CHEBI:55380; CHEBI:76224; CHEBI:33282
  locator: 443-chebi.json and shared 442 term snapshots
  accessed_at: '2026-10-21T16:18:48.829991Z'
  support: supports
  summary: Current ChEBI repeats the native identity, definition and polyphenol parent,
    so simple source refresh would retain the classification conflict. The exact CHEBI:26195
    definition requires two or more benzene rings, each bearing hydroxy. Beta-hydroxy
    ketone and aromatic ketone remain supported, and PB correctly lacks the methyl-ketone
    parent used for AB.
  snapshot_sha256: 7df77195fbcc05f12f85b9110e1e506cad3dfd77222380920e5ce4903b2a59b6
- evidence_id: antioxidant
  kind: primary_source
  reference: PMID:12951487; DOI:10.1248/bpb.26.1354
  locator: 442-original2003.pdf full original; compound 1 in Figure 1/Table 1, printed
    p1355, visually read
  accessed_at: '2026-10-21T16:15:52.003410Z'
  support: supports
  summary: PB is compound 1, with propionyl substituent R=CH2CH3, distinguished from
    AB compound 2 R=CH3. It was isolated from D. crassirhizoma rhizomes, voucher CNU
    1011. PB DPPH, superoxide and rat-brain lipid-peroxidation IC50 values are 71.7,
    58.6 and 12.9 µM. The paper supports the radical-scavenging definition; proposed
    iron chelation in that experiment is not a bacterial molecular target.
  snapshot_sha256: afdff7bf2f11c89886a556389579c977c3c2b5b3b385ed7588a1d59eaf7a0da3
- evidence_id: antibacterial
  kind: primary_source
  reference: PMID:19471878; DOI:10.1007/s12272-009-1502-9
  locator: 443-adopted-core.json both complete adopted abstracts;442-PMC7091015.xml
    original antibacterial abstract
  accessed_at: '2026-10-21T16:18:49.239251Z'
  support: supports
  summary: The antibacterial original describes isolated, spectrally characterized
    PB and AB tested by the paper-disc method, with Gram-positive activity including
    source-described MRSA S. aureus KCTC 1928, S. mutans and B. subtilis. No exact
    per-congener zone or MIC value is imported because the main tables were not retrieved.
    Negative fungi/chlorella outcomes remain bounded to the tested panel.
  snapshot_sha256: 61a8d7f581991d449b9b1bd64ca2838c418b85e89a84f33a5293dbb033e73bc9
- evidence_id: early-identity
  kind: primary_source
  reference: DOI:10.1248/cpb.30.4102
  locator: 443-original1982.pdf all five scanned pages visually read; Chart 1 p4103;
    PB experimental paragraph p4105
  accessed_at: '2026-10-21T16:19:32.203275Z'
  support: supports
  summary: The original isolates PB as compound I from D. abbreviata in Turkey and
    reports matching melting point/spectra and identity with authentic PB. Chart 1
    matches the native acyl pattern; experimental MS gives molecular ion 432 and C23H28O8.
    This separately supports identity, without conflating D. abbreviata with the native
    D. crassirhizoma occurrence.
  snapshot_sha256: 3980e8c999150e90fbb10dae724e0e07657c7939e9c556159246192e413a972d
- evidence_id: later-isolation
  kind: primary_source
  reference: PMID:33383880; DOI:10.3390/molecules26010122
  locator: 442-PMC7796287.xml selected isolation, PB compound 3 physicochemical data,
    Tables 1/2 and methods
  accessed_at: '2026-10-21T16:15:52.533976Z'
  support: supports
  summary: PB compound 3 is separately purified and assigned C23H28O8 with [M-H]-
    m/z431.1705 and propionyl/butyryl NMR data. Its xanthine-oxidase experiment uses
    bovine-milk enzyme; the measured noncompetitive inhibition does not establish
    a bacterial target.
  snapshot_sha256: b389bd7225516a7532d4a89c9565d086fd0e54414dc3d7e2400c5006aff13a1b
- evidence_id: enzyme
  kind: primary_source
  reference: PMID:36295840; DOI:10.3390/metabo12100938
  locator: 443-PMC9610990.xml compound list, Table 1 row23, Results and Methods4.1–4.4
  accessed_at: '2026-10-21T16:19:32.202733Z'
  support: context_only
  summary: PB is compound 23, tested against commercial E. coli beta-glucuronidase
    G7396 with PNPG substrate. Its IC50 is 76.5 ± 1.5 µM and inhibition at 100 µM
    is 73.5 ± 0.7%. Kinetic and docking analyses were restricted to compounds 13–15
    and 26–28, not PB. This is enzyme inhibition, not evidence connecting beta-glucuronidase
    to PB antibacterial growth effects or establishing PB direct binding.
  snapshot_sha256: 8bccc6ef577feb518feaeb22af603bf7ff6593ff47d8df47d8a5384bdc13ddc9
- evidence_id: adapter
  kind: database
  reference: iModulonDB e_coli/precise1k/b1617
  locator: 443-adapter-results.json;443-adapter-corrected-results.json
  accessed_at: '2026-10-21T16:21:23Z'
  support: context_only
  summary: Before enzyme-paper follow-up, datasets returned 0. An initial precise1
    query used an unlisted dataset and its zero hits were discarded. Corrected precise1k
    uidA search returned gene b1617 beta-glucuronidase and no components. This is
    gene-catalogue identity, not PB binding, enzyme inhibition or growth evidence.
  snapshot_sha256: 4f1f8669d2930da2c357798dbf8a663749302a24fcd4db9a1234b60aec804759
- evidence_id: owners
  kind: database
  reference: Maintained ChEBI source lane
  locator: 443-raw-rows.json;443-source-audit.json;ChEBI extractor field mapping and
    seeder
  accessed_at: '2026-10-21T16:21:23Z'
  support: supports
  summary: All imported fields, exact synonym and both citation leads agree with the
    frozen row. Original 13 hashes remain intact and source-lead queue gives 14 unchanged
    inputs; three chronological histories remain appropriate to SEEDED status.
  snapshot_sha256: 7b025b1f7d1438cafcf2ee468b9a8d3e523737075041efbeac88e693dc0c2b6b
- evidence_id: validation
  kind: validation
  reference: Actual focused checks
  locator: 443-focused-results.json;443-chemistry.json;443-schema.log;443-strict.log;443-ledger.log
  accessed_at: '2026-10-21T16:21:23Z'
  support: supports
  summary: Native chemistry, schema, strict terms, independent authority comparison
    and source ledger all exit 0. These checks do not establish a bacterial mode or
    authorize REVIEWED status.
  snapshot_sha256: 15e39a69e9a727e5248068eb614418204f10cb7de4d5bc5cd6dc6c0b7efc3ba1
- evidence_id: access
  kind: search
  reference: Bounded exact-PB public research
  locator: 443-local-hits.txt ignored-inclusive data/curation/conf/scripts/src/tests
    search;443-fetch1/2.json;shared 442-fetch1/2/3.json
  accessed_at: '2026-10-21T16:21:23Z'
  support: context_only
  summary: Native-key PubChem lookup 404 was followed by a name lookup and independent
    tautomer comparison. Reaxys 2684769 returned 403. The antibacterial main PDF attempts
    returned HTML or 403; OA metadata routes returned 404. The 1982 scanned PDF was
    read as images. BB, isoflavaspidic PB and AB/nor-AB fraction studies were kept
    outside exact-PB antibacterial mechanism evidence.
  snapshot_sha256: 28019021342f42f35120fedcff4db4e91d149071c45fd6138c223d6b7696000a
  search_scope: 443-local-hits.txt ignored-inclusive data/curation/conf/scripts/src/tests
    search;443-fetch1/2.json;shared 442-fetch1/2/3.json
- evidence_id: ring-topology
  kind: validation
  reference: Native graph; CHEBI:26195 definition; original structure drawing
  locator: 442443-ring-audit.json;442443-ring-check.py;442443-ring-check.log;442-chebi-26195.json;
    original2003 Figure1 printedp1355
  accessed_at: '2026-10-21T16:27:01Z'
  support: refutes
  summary: Both native graphs have exactly two six-carbon rings, only one aromatic.
    In the other ring, zero-based atom17 has four carbon-carbon single bonds, including
    two methyl substituents, and zero hydrogens. It cannot become a benzene carbon
    while preserving connectivity. All584 enumerated keto–enol tautomers have at most
    one benzene ring. This refutes the formal two-benzene requirement, not the published
    exact structure or broad natural-products use of polyphenolic.
  snapshot_sha256: 46fef0d16cc881f5e052358d9f3ce264e5087f11b449ac1dc9ffa67bbddbbe46
assessments:
- assessment_id: identity
  area: identity
  topic: PB exact identity and synonym
  outcome: supported
  summary: Formula, neutral charge, acyl pattern, source synonym, original drawings
    and authentic-material comparison agree. No family or sibling compound is substituted.
  target_ids:
  - CHEBI:65898
  evidence_ids:
  - record
  - chemistry
  - antioxidant
  - early-identity
  - later-isolation
- assessment_id: grounding
  area: grounding
  topic: Parents, role and definition
  outcome: concern
  summary: The CHEBI:26195 parent and polyphenol opening conflict with the exact formal
    class definition. Other listed parent classes and bounded occurrence/activity
    statements remain supported.
  target_ids:
  - CHEBI:65898
  evidence_ids:
  - authority
  - ring-topology
  - antioxidant
  - antibacterial
- assessment_id: registry
  area: grounding
  topic: Registry scope
  outcome: unknown
  summary: ChemSpider agrees under explicitly documented tautomer normalization. Reaxys
    is supported only by current source attribution; direct independent registry access
    failed.
  target_ids:
  - CHEBI:65898
  evidence_ids:
  - chemistry
  - authority
  - access
- assessment_id: mechanism
  area: evidence
  topic: Antibacterial mode and target
  outcome: unknown
  summary: PB has a measured weak beta-glucuronidase effect, but no inspected experiment
    connects this to bacterial growth inhibition. Bovine-milk XO and sibling docking
    results do not establish its antibacterial target.
  target_ids:
  - CHEBI:65898
  evidence_ids:
  - enzyme
  - later-isolation
  - adapter
- assessment_id: quantity
  area: quantity
  topic: Quantitative antibacterial observations
  outcome: unknown
  summary: The original qualitative antibacterial abstract is available, but PB-specific
    zones, MICs and detailed protocol were not verified. No numerical native observation
    is asserted.
  target_ids:
  - CHEBI:65898
  evidence_ids:
  - antibacterial
  - access
- assessment_id: ownership
  area: ownership
  topic: Input and audit consistency
  outcome: supported
  summary: Fourteen unchanged inputs and three chronological seeded events preserve
    provenance. The source-derived parent and definition need a maintained correction;
    changing only the generated YAML would not persist.
  target_ids:
  - CHEBI:65898
  evidence_ids:
  - owners
  - validation
findings:
- finding_id: F1
  issue_key: chebi-65898-polyphenol-parent-requires-two-benzene-rings
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Polyphenol parent conflicts with its two-benzene-ring requirement
  description: The native definition opens with polyphenol and parent_compounds[0]
    is CHEBI:26195. That class explicitly requires at least two hydroxy-substituted
    benzene rings. The exact supported molecule contains one benzene ring and one
    nonaromatic cyclohexadienone ring with a gem-dimethyl quaternary carbon. Ordinary
    keto–enol tautomerism cannot remove that four-carbon-bond valence constraint.
    Current ChEBI repeats the conflicting class assignment; its provenance does not
    make the graph satisfy the class definition.
  target_ids:
  - CHEBI:65898
  field_paths:
  - parent_compounds[0]
  - definition
  evidence_ids:
  - ring-topology
  - authority
  - chemistry
  - owners
  rule_id: 'review-checklist: Parent compounds must be strictly broader and scientifically
    valid'
  native_severity: Major required chemical-class correction; native REVIEWED classification
    gate blocked
  normalization_reason: This is a false formal chemical parent and corresponding defining
    statement, not a spelling issue or a distinct-compound identity claim. Exact structure,
    congener and activity evidence remain intact.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted CHEBI:65898 definition and parent_ids input
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ChEBI definition and parent extraction policy
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproduce corrected source fields in the generated record
actions:
- action_id: A1
  description: Implement a documented maintained-source correction that excludes CHEBI:26195
    for this exact record and replaces the opening with A phloroglucinol derivative,
    retaining the supported occurrence and activity clauses. Use the ChEBI extraction/input
    ownership lane and regenerate; do not silently patch only the generated YAML or
    change the valid molecular graph to fit the class. A replacement parent is optional
    and requires its own exact definition check.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:65898
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted CHEBI:65898 definition and parent_ids input
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Maintained ChEBI definition and parent extraction policy
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproduce corrected source fields in the generated record
  acceptance_checks:
  - Generated parent_compounds no longer includes CHEBI:26195 and the definition no
    longer asserts its incompatible formal class. Preserve the other supported parent
    classes.
  - Preserve exact chemical identity and all structure encodings; one aromatic benzene
    ring and the gem-dimethyl nonaromatic ring remain correct. Do not aromatize by
    deleting methyl groups or changing connectivity.
  - Document the current upstream conflict and ensure the maintained correction survives
    extraction and reseeding.
  - After authorized curation, rerun molecular checks, schema, strict terms, corpus
    reproducibility/history and full QC; retain SEEDED until all required native REVIEWED
    gates are satisfied.
limitations:
- Independent Reaxys 2684769 identity remains unresolved. ChemSpider/PubChem raw keys
  differ because of keto–enol depictions; the review reports normalization explicitly
  rather than asserting equal raw representations.
- The 2009 antibacterial main tables and methods were not retrieved; no numerical
  PB potency or source-described MRSA strain status is independently reclassified.
- The beta-glucuronidase assay does not demonstrate a PB antibacterial causal mechanism.
  PB was not among the compounds subjected to competitive kinetics or docking, and
  no such relation is transferred.
- Structured search initially used an unlisted precise1 dataset despite exit 0; that
  result was discarded and corrected to precise1k. Neither result is compound-effect
  evidence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Standalone chemistry used the batch 019 interpreter against batch 045; ledger and
  contract use batch 045. Shared 442 primary artifacts retain their actual manifests
  and hashes.
- No native protein claim required adapter correction. An additional exact-PB bacterial-enzyme
  lead prompted the bounded adapter query before source follow-up.
- All native bytes and scientific status remain unchanged; optional absent measurements
  or target fields are not treated as errors.
- Before saving, an independent reviewer raised the formal polyphenol requirement.
  A separate atom-level recheck confirmed it, and this unsaved review was revised.
  Broad natural-products terminology is distinguished from the explicit ontology constraint.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:65898
- https://www.chemspider.com/Chemical-Structure.23275363.html
- https://doi.org/10.1248/bpb.26.1354
- https://doi.org/10.1007/s12272-009-1502-9
- https://doi.org/10.1248/cpb.30.4102
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7796287/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC9610990/
tags:
- record-review
- flavaspidic-acid-pb
- phloroglucinol
```
