# Actinodaphnine: exact S identity and assay-material boundaries

- Review: 20261021T083415Z-actinodaphnine
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T08:25:14Z
- Finished UTC: 2026-10-21T08:34:15Z
- Reviewer: Codex dodecanediol_sources subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact neutral S identity, structural parents and antibacterial/antifungal roles are supported. One minor inherited definition typo needs correction. Assay scope separates purified-compound screening from plant fractions and host/protozoan mechanisms; KNApSAcK has an internal displayed-key discrepancy.

## Scope And Provenance

Whole-record review of one exact actinodaphnine record.

Selection: Queue077; CHEBI:2444 in isolated batch008.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:2444 | data/antibiotics/antibacterial/actinodaphnine.yaml | generated | actinodaphnine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused schema | passed | True | CHEBI:2444 | Actual command passed. |
| Focused strict | passed | True | CHEBI:2444 | Actual command passed. |
| Independent structure checks | passed | True | CHEBI:2444 | Native and live source encodings agree, including exact stereochemistry. |
| Structured source applicability | not_applicable | False | CHEBI:2444 | Native record contains no named gene, protein, regulator, pathway, stress response or transcriptomic dataset. Additional host/protozoan studies are retained as context and do not ground a bacterial module claim. |
| Authoritative full QC | failed | True | CHEBI:2444 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:2444 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:2444 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:2444 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:2444 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:2444 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:2444 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:2444 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:2444 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral S aporphine

identity: supported. Targets: CHEBI:2444.

Names, both native encodings, live authorities and independently parsed KEGG stereochemistry agree.

### Broader parents and retained activity roles

grounding: supported. Targets: CHEBI:2444.

Five structural classes are broader and chemically appropriate.1989 compound-specific screening supports antibacterial and antifungal classification.

### Source wording

schema: concern. Targets: CHEBI:2444.

Inherited bering is a small wording error; it does not change chemical identity.

### Resolvable chemical references

provenance: unknown. Targets: CHEBI:2444.

KEGG exact structure is verified. KNApSAcK encodings agree despite its inconsistent displayed key. Reaxys independent equivalence remains unavailable with no demonstrated mismatch.

### Purified compound versus fraction

evidence: supported. Targets: CHEBI:2444.

1989 screening supports the two activity roles. Grouped abstract values require original-table adjudication;2017 FA6 values must remain fraction evidence.

### Antimicrobial mode and targets

evidence: unknown. Targets: CHEBI:2444.

No native target or mechanism is asserted. Host apoptosis and protozoan/DNA-topoisomerase results cannot establish a bacterial/fungal target without organism and compound-specific assay resolution.

### Salt PK and analgesia

scope: not_applicable. Targets: CHEBI:2444.

No clinical claim is native; rabbit hydrochloride PK and analgesia metadata provide no human antimicrobial efficacy or approval evidence.

### Plant origin versus activity attribution

scope: unknown. Targets: CHEBI:2444.

Sources report named compound isolation from plants, but no native producer assertion is present.2017 NMR/MS isolation supports occurrence without independently resolving absolute configuration.

### Optional follow-up fields

completeness: unknown. Targets: CHEBI:2444.

Specific screening and isolation evidence offers bounded curation opportunities; optional blank fields alone are not schema errors or unsupported claims. No resistance determinant, transcriptomic dataset or causal graph is established by inspected evidence.

### Seed ownership and status

provenance: supported. Targets: CHEBI:2444.

Raw/source identity, reproducible mint and all three seed/reseed events agree; SEEDED is preserved.

### Focused validators

schema: supported. Targets: CHEBI:2444.

Both documented focused gates pass.

## Findings

### F1: Correct the inherited definition typo

minor / open / confirmed; issue key: chebi-2444-definition-bering-typo.

The definition says bering where bearing is intended. The raw adopted row and current ChEBI repeat it. This is a bounded wording correction with no identity or activity consequence.

## Recommended Actions And Acceptance Checks

### A1

Correct bering to bearing through the maintained source workflow and regenerate the imported definition.

- Native definition reads bearing and retains the same structure and locants.
- Keep source provenance explicit; do not hand-edit a generated identity field without a maintained owner.
- Run schema/strict, source reproduction and history gates for the eventual authorized curation change.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/actinodaphnine.yaml; Entire YAML | supports | Read definition, five synonyms, five parents, antibacterial/antifungal roles, structure encodings, masses, four xrefs, source/mint and all three history events. No native quantitative assay, molecular target, mechanism, producer, resistance, clinical or dataset claim. Definition contains the inherited typo bering. |
| owner | data/raw/chebi_antimicrobials.tsv; Row13; PATHS row585; extractor/seeder and configuration | supports | Raw row agrees and supplies PMIDs16168547,2609975,3267205 as leads. Mint reproduces; source role filtering explains why other live ChEBI pharmacological roles are not all imported. Imported definition correction belongs to the maintained source/extractor/seeder pipeline. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:2444; Names, structure, definition, outgoing ontology and references | supports | Current official source matches native neutral S compound, formula C18H17NO4, full key VYJUHRAQPIBWNV-LBPRGKRZSA-N, masses, synonyms, parents, roles and four registry references. It also contains bering. Additional source pharmacological roles are not evidence of an antibacterial target. |
| chemistry | Independent RDKit calculations; Native SMILES/InChI, KEGG MOL and KNApSAcK encodings | supports | All five encodings regenerate the native full key, neutral C18H17NO4, mass311.337, exact311.115758024 and S configuration with accurate CIP assignment. Mint antibioticmech:chebi-c5163c8355 reproduces. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/160502; Full-key PUG resolution | supports | Exact-key lookup returns CID160502 with matching InChI/key, formula, charge and masses. |
| kegg | https://rest.kegg.jp/get/C09322; Compound entry and stereo-encoded MOL | supports | Names, CAS517-69-1, ChEBI2444 and KNApSAcK1790 agree. Independently parsed MOL reproduces the exact native stereochemical key. |
| knapsack | https://www.knapsackfamily.com/knapsack_core/information.php?word=C00001790; Names, CAS, InChI, SMILES and displayed key | partial | Displayed InChI and SMILES regenerate the native exact S structure, but the separately printed key is VYJUHRAQPIBWNV-STGVRZAANA-N. Preserve this source-internal conflict; the full encodings do not demonstrate a wrong native xref. Plant associations and predicted biosynthetic origin are not native producer assertions. |
| term-134209 | https://www.ebi.ac.uk/chebi/CHEBI:134209; Official term definition | supports | Resolved aporphine alkaloid. Structural parent definitions are broader than the exact molecule; antifungal activity is separately supported by primary screening. |
| term-33853 | https://www.ebi.ac.uk/chebi/CHEBI:33853; Official term definition | supports | Resolved phenols. Structural parent definitions are broader than the exact molecule; antifungal activity is separately supported by primary screening. |
| term-35618 | https://www.ebi.ac.uk/chebi/CHEBI:35618; Official term definition | supports | Resolved aromatic ether. Structural parent definitions are broader than the exact molecule; antifungal activity is separately supported by primary screening. |
| term-38164 | https://www.ebi.ac.uk/chebi/CHEBI:38164; Official term definition | supports | Resolved organic heteropentacyclic compound. Structural parent definitions are broader than the exact molecule; antifungal activity is separately supported by primary screening. |
| term-50995 | https://www.ebi.ac.uk/chebi/CHEBI:50995; Official term definition | supports | Resolved secondary amino compound. Structural parent definitions are broader than the exact molecule; antifungal activity is separately supported by primary screening. |
| term-35718 | https://www.ebi.ac.uk/chebi/CHEBI:35718; Official term definition | supports | Resolved antifungal agent. Structural parent definitions are broader than the exact molecule; antifungal activity is separately supported by primary screening. |
| screening | PMID:2733073; 1989 primary abstract; compound1 (+)-actinodaphnine | supports | The abstract distinguishes compound1 from N-methyl derivative2. Compound1 is among the strongest compounds against B.cereus, Micrococcus sp. and S.aureus with the printed inequality MIC ≥50µg/mL. It reports weak E.coli/Klebsiella pneumonia activity at300µg/mL and includes compound1 in antifungal results against Candida/Cryptococcus. The62.5–1000µg/mL antifungal range is pooled across compounds/species; do not assign each value or silently invert the inequality. Full original tables and methods remain uninspected. |
| host-apoptosis | PMID:16168547; DOI10.1016/j.fct.2005.08.005; primary abstract | context_only | Actinodaphnine isolated from Cinnamomum insularimontanum induces apoptosis in human Mahlavu hepatoma cells with ROS/NO, mitochondrial, caspase and NFκB observations. These host-cell findings do not establish antibacterial or antifungal mechanism. |
| salt-pk | PMID:2609975; Primary abstract | context_only | Rabbit pharmacokinetics after intravenous actinodaphine hydrochloride concern a distinct salt and host disposition, not antimicrobial potency of the neutral free base or clinical efficacy. |
| analgesia | PMID:3267205; Bibliographic record only | context_only | Title concerns antipyretic/analgesic actions; no abstract or experiment text was supplied. Citation resolves but cannot support a detailed assay or antimicrobial mechanism. |
| trypanosome | PMID:15124084; DOI10.1055/s-2004-818967; primary abstract | context_only | Three isolated Cassytha alkaloids including actinodaphnine inhibit T.brucei brucei within a pooled3–15µM range. Optical experiments support DNA intercalation and biochemical experiments interference with topoisomerase catalytic activity. The abstract lacks compound-specific enzyme isoform, organism and assay detail; no bacterial or fungal target is established by this host/protozoan study. |
| fraction-boundary | https://link.springer.com/content/pdf/10.1016/j.bjp.2016.08.006.pdf; Full publisher PDF text, pp78–82, compound4 and Table1 footnote | context_only | Purified actinodaphnine is compound4 from FA6.2, characterized by NMR/MS after stem extraction. Table1 instead assays the FA6 column fraction containing actinodaphnine as a major component. Its MIC/MBC values are not pure-compound observations. The source also has inoculum/concentration wording and E.coli table-versus-prose discrepancies. This review does not transfer those quantitative fraction results or infer absolute configuration from NMR alone. |
| registries | https://www.ebi.ac.uk/chebi/CHEBI:2444; CAS and Reaxys references | partial | CAS517-69-1 is consistent across ChEBI, KEGG and KNApSAcK. Reaxys44828 remains verified only as the official source assertion; independent restricted-registry structure detail was unavailable. |
| search | CultureBotAI/AntibioticMech; Ignored-inclusive local search and bounded free literature discovery | context_only | Exact native/raw/PATHS/configuration and curation surfaces were inspected. No historical report path occurred in the ignored-inclusive search output. Substring CHEBI244418 hits were excluded from CHEBI2444 identity. All three adopted citations were resolved; additional screening and fraction-source text was inspected. |
| gates | just validate; just validate-strict; Actual focused commands in batch008 | supports | Both exit0; one record, zero strict ERROR rows. |

## Limits And Additional Notes

- The1989 full paper was not obtained; preserve its abstract inequality and grouped organism/compound ranges until original tables and methods are inspected.
- Adopted antipyretic/analgesic citation supplied metadata only. Host apoptosis, rabbit salt PK and protozoan mechanism evidence do not resolve bacterial/fungal mode of action.
- KNApSAcK displayed key disagrees with its own InChI/SMILES; independent Reaxys detail was unavailable. No native identity mismatch follows from these bounded limitations.
- Publisher PDF text was accessible through web retrieval; direct downloads returned a challenge page and were not treated as PDF evidence. The literature search does not establish that no further exact-compound evidence exists.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All captured input hashes were rechecked unchanged. No native record, history or scientific status changed.
- Future assay curation should first obtain1989 original tables and preserve species/strain, units, inequality and preparation. Do not transfer2017 FA6 fraction MIC/MBC values to purified FA6.2 compound4.
- Source-internal defects and host/protozoan mechanism boundaries are preserved as qualifications rather than unsupported native findings.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T083415Z-actinodaphnine
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Actinodaphnine: exact S identity and assay-material boundaries'
started_at: '2026-10-21T08:25:14Z'
finished_at: '2026-10-21T08:34:15Z'
reviewer:
  identity: Codex dodecanediol_sources subagent
  kind: agent
  independence: independent
  independence_basis: Read full native record, raw owner, live identity authorities
    and primary source text independently; did not create the seed.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Exact neutral S identity, structural parents and antibacterial/antifungal
  roles are supported. One minor inherited definition typo needs correction. Assay
  scope separates purified-compound screening from plant fractions and host/protozoan
  mechanisms; KNApSAcK has an internal displayed-key discrepancy.
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
  - path: data/antibiotics/antibacterial/actinodaphnine.yaml
    sha256: 1ed5a9ad1ead2272b68fcd33d164ba74d02671b3af8e2f3f18e447230172e940
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
  - path: conf/record_review.yaml
    sha256: 1c6056581d45a5b902f6c66ffaa20fc05c73ca473a4ffd57745be269fe3e89cf
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: be89e87e5de1e3ee1b45b4070ddbdc7419921d434c69efa3c41aa16fbfd54649
    role: context
  - path: data/antibiotics/PATHS.tsv
    sha256: 3b1d82d007878e4aca2c28f4001a468776b325b726da2e48abb76a3dc551cc38
    role: context
targets:
- target_id: CHEBI:2444
  path: data/antibiotics/antibacterial/actinodaphnine.yaml
  label: actinodaphnine
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
  description: Whole-record review of one exact actinodaphnine record.
  selection: Queue077; CHEBI:2444 in isolated batch008.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:2444
  exclusions:
  - target: Hydrochloride salt, N-methyl derivative, plant fractions and other aporphines
    reason: Separate preparations or comparators; their results are not automatically
      transferred.
checks:
- check_id: schema
  name: Focused schema
  status: passed
  required: true
  summary: Actual command passed.
  target_ids:
  - CHEBI:2444
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/actinodaphnine.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: strict
  name: Focused strict
  status: passed
  required: true
  summary: Actual command passed.
  target_ids:
  - CHEBI:2444
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/actinodaphnine.yaml --out /private/tmp/am-review-session/077-validation.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - gates
- check_id: chemistry
  name: Independent structure checks
  status: passed
  required: true
  summary: Native and live source encodings agree, including exact stereochemistry.
  target_ids:
  - CHEBI:2444
  evidence_ids:
  - chemistry
  - chebi
  - pubchem
  - kegg
- check_id: adapter
  name: Structured source applicability
  status: not_applicable
  required: false
  summary: Native record contains no named gene, protein, regulator, pathway, stress
    response or transcriptomic dataset. Additional host/protozoan studies are retained
    as context and do not ground a bacterial module claim.
  target_ids:
  - CHEBI:2444
  evidence_ids:
  - native
  - host-apoptosis
  - trypanosome
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:2444
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
  - CHEBI:2444
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
  - CHEBI:2444
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
  - CHEBI:2444
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
  - CHEBI:2444
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
  - CHEBI:2444
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
  - CHEBI:2444
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
  - CHEBI:2444
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
  - CHEBI:2444
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/actinodaphnine.yaml
  locator: Entire YAML
  accessed_at: '2026-10-21T08:30:33Z'
  support: supports
  summary: Read definition, five synonyms, five parents, antibacterial/antifungal
    roles, structure encodings, masses, four xrefs, source/mint and all three history
    events. No native quantitative assay, molecular target, mechanism, producer, resistance,
    clinical or dataset claim. Definition contains the inherited typo bering.
- evidence_id: owner
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv
  locator: Row13; PATHS row585; extractor/seeder and configuration
  accessed_at: '2026-10-21T08:30:33Z'
  support: supports
  summary: Raw row agrees and supplies PMIDs16168547,2609975,3267205 as leads. Mint
    reproduces; source role filtering explains why other live ChEBI pharmacological
    roles are not all imported. Imported definition correction belongs to the maintained
    source/extractor/seeder pipeline.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:2444
  locator: Names, structure, definition, outgoing ontology and references
  accessed_at: '2026-10-21T08:25:52Z'
  support: supports
  summary: Current official source matches native neutral S compound, formula C18H17NO4,
    full key VYJUHRAQPIBWNV-LBPRGKRZSA-N, masses, synonyms, parents, roles and four
    registry references. It also contains bering. Additional source pharmacological
    roles are not evidence of an antibacterial target.
  snapshot_sha256: d141843ec6135861eb4665305c400182391991917abb9e4df45dac5d32eebc11
- evidence_id: chemistry
  kind: validation
  reference: Independent RDKit calculations
  locator: Native SMILES/InChI, KEGG MOL and KNApSAcK encodings
  accessed_at: '2026-10-21T08:26:15Z'
  support: supports
  summary: All five encodings regenerate the native full key, neutral C18H17NO4, mass311.337,
    exact311.115758024 and S configuration with accurate CIP assignment. Mint antibioticmech:chebi-c5163c8355
    reproduces.
  snapshot_sha256: d9b278500cb41f1fb6c12522811a8bb3110081e49025a7ded03cf0081654dbb0
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/160502
  locator: Full-key PUG resolution
  accessed_at: '2026-10-21T08:25:49Z'
  support: supports
  summary: Exact-key lookup returns CID160502 with matching InChI/key, formula, charge
    and masses.
  snapshot_sha256: 6769ab8ba38d4f69f7c40c543a55e490a8272ae06d8ea0fca309c29c42f81c64
- evidence_id: kegg
  kind: database
  reference: https://rest.kegg.jp/get/C09322
  locator: Compound entry and stereo-encoded MOL
  accessed_at: '2026-10-21T08:25:49Z'
  support: supports
  summary: Names, CAS517-69-1, ChEBI2444 and KNApSAcK1790 agree. Independently parsed
    MOL reproduces the exact native stereochemical key.
  snapshot_sha256: f93f6c35e5108645738a0cde52a5aa7dfbae6f5594c6328d9e21b33f7af8a1a3
- evidence_id: knapsack
  kind: database
  reference: https://www.knapsackfamily.com/knapsack_core/information.php?word=C00001790
  locator: Names, CAS, InChI, SMILES and displayed key
  accessed_at: '2026-10-21T08:25:51Z'
  support: partial
  summary: Displayed InChI and SMILES regenerate the native exact S structure, but
    the separately printed key is VYJUHRAQPIBWNV-STGVRZAANA-N. Preserve this source-internal
    conflict; the full encodings do not demonstrate a wrong native xref. Plant associations
    and predicted biosynthetic origin are not native producer assertions.
  snapshot_sha256: 44086f29bd8bec9537acb619fdf3509e224951c28ede149661cf94c579c391d3
- evidence_id: term-134209
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:134209
  locator: Official term definition
  accessed_at: '2026-10-21T08:25:52Z'
  support: supports
  summary: Resolved aporphine alkaloid. Structural parent definitions are broader
    than the exact molecule; antifungal activity is separately supported by primary
    screening.
  snapshot_sha256: cd3e33a9186e8381346ea3680bdece3916e931282ef45951535f836aacbb83d1
- evidence_id: term-33853
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:33853
  locator: Official term definition
  accessed_at: '2026-10-21T08:25:51Z'
  support: supports
  summary: Resolved phenols. Structural parent definitions are broader than the exact
    molecule; antifungal activity is separately supported by primary screening.
  snapshot_sha256: 7fae6be80345ba894e58007ae8a56ee0123fa217c329d6b18bd2d16139871b72
- evidence_id: term-35618
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:35618
  locator: Official term definition
  accessed_at: '2026-10-21T08:26:01Z'
  support: supports
  summary: Resolved aromatic ether. Structural parent definitions are broader than
    the exact molecule; antifungal activity is separately supported by primary screening.
  snapshot_sha256: 3fb2e555fde565c4741436915ab2dd8888bb49ebb7cf1a10a582de4acdbb60a9
- evidence_id: term-38164
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:38164
  locator: Official term definition
  accessed_at: '2026-10-21T08:25:51Z'
  support: supports
  summary: Resolved organic heteropentacyclic compound. Structural parent definitions
    are broader than the exact molecule; antifungal activity is separately supported
    by primary screening.
  snapshot_sha256: ed6faf11114bfd21ba8d5d0a6e652230a7e7f6a04d98d132326050104f7ff1dd
- evidence_id: term-50995
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:50995
  locator: Official term definition
  accessed_at: '2026-10-21T08:25:51Z'
  support: supports
  summary: Resolved secondary amino compound. Structural parent definitions are broader
    than the exact molecule; antifungal activity is separately supported by primary
    screening.
  snapshot_sha256: a24d3711276a87c0490b87dd23c15de8fa1a35632155030c4fa76d20b32a3292
- evidence_id: term-35718
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:35718
  locator: Official term definition
  accessed_at: '2026-10-21T08:25:53Z'
  support: supports
  summary: Resolved antifungal agent. Structural parent definitions are broader than
    the exact molecule; antifungal activity is separately supported by primary screening.
  snapshot_sha256: 00609b86a5cd623402e94a4b58b7f6e74e4887706201b36cfa2a24b58569c282
- evidence_id: screening
  kind: primary_source
  reference: PMID:2733073
  locator: 1989 primary abstract; compound1 (+)-actinodaphnine
  accessed_at: '2026-10-21T08:25:52Z'
  support: supports
  summary: The abstract distinguishes compound1 from N-methyl derivative2. Compound1
    is among the strongest compounds against B.cereus, Micrococcus sp. and S.aureus
    with the printed inequality MIC ≥50µg/mL. It reports weak E.coli/Klebsiella pneumonia
    activity at300µg/mL and includes compound1 in antifungal results against Candida/Cryptococcus.
    The62.5–1000µg/mL antifungal range is pooled across compounds/species; do not
    assign each value or silently invert the inequality. Full original tables and
    methods remain uninspected.
  snapshot_sha256: 9fae607b73588156561f844e3e7eb856e2f0abb3ce8890c928a1c5e3bce6a3a6
- evidence_id: host-apoptosis
  kind: primary_source
  reference: PMID:16168547
  locator: DOI10.1016/j.fct.2005.08.005; primary abstract
  accessed_at: '2026-10-21T08:25:52Z'
  support: context_only
  summary: Actinodaphnine isolated from Cinnamomum insularimontanum induces apoptosis
    in human Mahlavu hepatoma cells with ROS/NO, mitochondrial, caspase and NFκB observations.
    These host-cell findings do not establish antibacterial or antifungal mechanism.
  snapshot_sha256: 60865d1b9408540fc9040d2c0daddcc00d5435e273fa6425d96cb085919c8dab
- evidence_id: salt-pk
  kind: primary_source
  reference: PMID:2609975
  locator: Primary abstract
  accessed_at: '2026-10-21T08:25:52Z'
  support: context_only
  summary: Rabbit pharmacokinetics after intravenous actinodaphine hydrochloride concern
    a distinct salt and host disposition, not antimicrobial potency of the neutral
    free base or clinical efficacy.
  snapshot_sha256: 518979d651aa151780d8b8128cae82104200f0170de36f4f7f260d300ddb41cb
- evidence_id: analgesia
  kind: primary_source
  reference: PMID:3267205
  locator: Bibliographic record only
  accessed_at: '2026-10-21T08:25:52Z'
  support: context_only
  summary: Title concerns antipyretic/analgesic actions; no abstract or experiment
    text was supplied. Citation resolves but cannot support a detailed assay or antimicrobial
    mechanism.
  snapshot_sha256: 619fe64d18aca3cce9cac863eeaeb664fab1c0168f223aa8064b448a969fc033
- evidence_id: trypanosome
  kind: primary_source
  reference: PMID:15124084
  locator: DOI10.1055/s-2004-818967; primary abstract
  accessed_at: '2026-10-21T08:28:53Z'
  support: context_only
  summary: Three isolated Cassytha alkaloids including actinodaphnine inhibit T.brucei
    brucei within a pooled3–15µM range. Optical experiments support DNA intercalation
    and biochemical experiments interference with topoisomerase catalytic activity.
    The abstract lacks compound-specific enzyme isoform, organism and assay detail;
    no bacterial or fungal target is established by this host/protozoan study.
  snapshot_sha256: e859622bbca3c99d7003db1431e97a48e8c4a45f19b3336d4e65c08e3c30ecbc
- evidence_id: fraction-boundary
  kind: primary_source
  reference: https://link.springer.com/content/pdf/10.1016/j.bjp.2016.08.006.pdf
  locator: Full publisher PDF text, pp78–82, compound4 and Table1 footnote
  accessed_at: '2026-10-21T08:30:33Z'
  support: context_only
  summary: Purified actinodaphnine is compound4 from FA6.2, characterized by NMR/MS
    after stem extraction. Table1 instead assays the FA6 column fraction containing
    actinodaphnine as a major component. Its MIC/MBC values are not pure-compound
    observations. The source also has inoculum/concentration wording and E.coli table-versus-prose
    discrepancies. This review does not transfer those quantitative fraction results
    or infer absolute configuration from NMR alone.
- evidence_id: registries
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:2444
  locator: CAS and Reaxys references
  accessed_at: '2026-10-21T08:30:33Z'
  support: partial
  summary: CAS517-69-1 is consistent across ChEBI, KEGG and KNApSAcK. Reaxys44828
    remains verified only as the official source assertion; independent restricted-registry
    structure detail was unavailable.
- evidence_id: search
  kind: search
  reference: CultureBotAI/AntibioticMech
  locator: Ignored-inclusive local search and bounded free literature discovery
  accessed_at: '2026-10-21T08:30:33Z'
  support: context_only
  summary: Exact native/raw/PATHS/configuration and curation surfaces were inspected.
    No historical report path occurred in the ignored-inclusive search output. Substring
    CHEBI244418 hits were excluded from CHEBI2444 identity. All three adopted citations
    were resolved; additional screening and fraction-source text was inspected.
  search_scope: prepare.py77 used rg --no-ignore --hidden for ID, label and slug across
    batch008 excluding.git/.venv; exact row/key follow-up. Free searches used actinodaphnine,actinodaphine,517-69-1,primary
    titles and DOIs. EPMC abstracts and publisher PDF text were read; the1989 full
    text was not obtained.
- evidence_id: gates
  kind: validation
  reference: just validate; just validate-strict
  locator: Actual focused commands in batch008
  accessed_at: '2026-10-21T08:29:05Z'
  support: supports
  summary: Both exit0; one record, zero strict ERROR rows.
  snapshot_sha256: 3841032dc52685ea3bacd1a5e8f28a01bed898ac4edbf46b9ed118789b148971
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral S aporphine
  outcome: supported
  summary: Names, both native encodings, live authorities and independently parsed
    KEGG stereochemistry agree.
  target_ids:
  - CHEBI:2444
  evidence_ids:
  - native
  - chebi
  - chemistry
  - pubchem
  - kegg
- assessment_id: parentage
  area: grounding
  topic: Broader parents and retained activity roles
  outcome: supported
  summary: Five structural classes are broader and chemically appropriate.1989 compound-specific
    screening supports antibacterial and antifungal classification.
  target_ids:
  - CHEBI:2444
  evidence_ids:
  - chemistry
  - term-134209
  - term-33853
  - term-35618
  - term-38164
  - term-50995
  - term-35718
  - screening
- assessment_id: definition
  area: schema
  topic: Source wording
  outcome: concern
  summary: Inherited bering is a small wording error; it does not change chemical
    identity.
  target_ids:
  - CHEBI:2444
  evidence_ids:
  - native
  - owner
  - chebi
- assessment_id: xrefs
  area: provenance
  topic: Resolvable chemical references
  outcome: unknown
  summary: KEGG exact structure is verified. KNApSAcK encodings agree despite its
    inconsistent displayed key. Reaxys independent equivalence remains unavailable
    with no demonstrated mismatch.
  target_ids:
  - CHEBI:2444
  evidence_ids:
  - kegg
  - knapsack
  - registries
  - chemistry
- assessment_id: activity
  area: evidence
  topic: Purified compound versus fraction
  outcome: supported
  summary: 1989 screening supports the two activity roles. Grouped abstract values
    require original-table adjudication;2017 FA6 values must remain fraction evidence.
  target_ids:
  - CHEBI:2444
  evidence_ids:
  - screening
  - fraction-boundary
- assessment_id: mechanism
  area: evidence
  topic: Antimicrobial mode and targets
  outcome: unknown
  summary: No native target or mechanism is asserted. Host apoptosis and protozoan/DNA-topoisomerase
    results cannot establish a bacterial/fungal target without organism and compound-specific
    assay resolution.
  target_ids:
  - CHEBI:2444
  evidence_ids:
  - native
  - host-apoptosis
  - trypanosome
- assessment_id: clinical
  area: scope
  topic: Salt PK and analgesia
  outcome: not_applicable
  summary: No clinical claim is native; rabbit hydrochloride PK and analgesia metadata
    provide no human antimicrobial efficacy or approval evidence.
  target_ids:
  - CHEBI:2444
  evidence_ids:
  - salt-pk
  - analgesia
  - native
- assessment_id: producer
  area: scope
  topic: Plant origin versus activity attribution
  outcome: unknown
  summary: Sources report named compound isolation from plants, but no native producer
    assertion is present.2017 NMR/MS isolation supports occurrence without independently
    resolving absolute configuration.
  target_ids:
  - CHEBI:2444
  evidence_ids:
  - host-apoptosis
  - fraction-boundary
  - knapsack
- assessment_id: completeness
  area: completeness
  topic: Optional follow-up fields
  outcome: unknown
  summary: Specific screening and isolation evidence offers bounded curation opportunities;
    optional blank fields alone are not schema errors or unsupported claims. No resistance
    determinant, transcriptomic dataset or causal graph is established by inspected
    evidence.
  target_ids:
  - CHEBI:2444
  evidence_ids:
  - native
  - screening
  - search
- assessment_id: history
  area: provenance
  topic: Seed ownership and status
  outcome: supported
  summary: Raw/source identity, reproducible mint and all three seed/reseed events
    agree; SEEDED is preserved.
  target_ids:
  - CHEBI:2444
  evidence_ids:
  - owner
  - native
  - chemistry
- assessment_id: schema
  area: schema
  topic: Focused validators
  outcome: supported
  summary: Both documented focused gates pass.
  target_ids:
  - CHEBI:2444
  evidence_ids:
  - gates
findings:
- finding_id: F1
  issue_key: chebi-2444-definition-bering-typo
  category: other
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the inherited definition typo
  description: The definition says bering where bearing is intended. The raw adopted
    row and current ChEBI repeat it. This is a bounded wording correction with no
    identity or activity consequence.
  target_ids:
  - CHEBI:2444
  field_paths:
  - definition
  evidence_ids:
  - native
  - owner
  - chebi
  rule_id: review-yaml-record:minor-wording
  native_severity: minor wording
  normalization_reason: Non-blocking spelling defect; structures, chemical locants
    and role classification remain supported.
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
actions:
- action_id: A1
  description: Correct bering to bearing through the maintained source workflow and
    regenerate the imported definition.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:2444
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
  - Native definition reads bearing and retains the same structure and locants.
  - Keep source provenance explicit; do not hand-edit a generated identity field without
    a maintained owner.
  - Run schema/strict, source reproduction and history gates for the eventual authorized
    curation change.
limitations:
- The1989 full paper was not obtained; preserve its abstract inequality and grouped
  organism/compound ranges until original tables and methods are inspected.
- Adopted antipyretic/analgesic citation supplied metadata only. Host apoptosis, rabbit
  salt PK and protozoan mechanism evidence do not resolve bacterial/fungal mode of
  action.
- KNApSAcK displayed key disagrees with its own InChI/SMILES; independent Reaxys detail
  was unavailable. No native identity mismatch follows from these bounded limitations.
- Publisher PDF text was accessible through web retrieval; direct downloads returned
  a challenge page and were not treated as PDF evidence. The literature search does
  not establish that no further exact-compound evidence exists.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All captured input hashes were rechecked unchanged. No native record, history or
  scientific status changed.
- Future assay curation should first obtain1989 original tables and preserve species/strain,
  units, inequality and preparation. Do not transfer2017 FA6 fraction MIC/MBC values
  to purified FA6.2 compound4.
- Source-internal defects and host/protozoan mechanism boundaries are preserved as
  qualifications rather than unsupported native findings.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
links:
- https://www.ebi.ac.uk/chebi/CHEBI:2444
- https://pubmed.ncbi.nlm.nih.gov/2733073/
- https://doi.org/10.1016/j.bjp.2016.08.006
tags:
- antibacterial
- antifungal
- aporphine
- exact-stereochemistry
- fraction-boundary
```
