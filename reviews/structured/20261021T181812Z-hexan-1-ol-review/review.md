# Hexan-1-ol: coherent identity and bounded vapor-phase antibacterial evidence

- Review: 20261021T181812Z-hexan-1-ol-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T18:00:57Z
- Finished UTC: 2026-10-21T18:18:12Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: blocked
- Scientific review: true

## Summary

The exact neutral primary-alcohol graph and broader classes agree with inspected authorities. All ten adopted original abstracts were read and distinguish metabolic, production, behavioral and physical studies from antibacterial evidence. An additional original study directly tests named 1-hexanol vapor, supporting the qualitative role with explicit assay and reporting limitations. No required native correction was established. Scientific assessment retains the stated evidence limits; full verification is blocked by the shared native-library failure.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Assigned queue position 533; one exact native record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:87393 | data/antibiotics/antibacterial/hexan-1-ol.yaml | generated | hexan-1-ol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:87393 | Actual focused execution exited 0. Executed against worktree 054; standalone chemistry used existing 019 RDKit and native validators used the 054 environment. |
| Focused schema verification | passed | True | CHEBI:87393 | Actual focused execution exited 0. Executed against worktree 054; standalone chemistry used existing 019 RDKit and native validators used the 054 environment. |
| Focused strict verification | passed | True | CHEBI:87393 | Actual focused execution exited 0. Executed against worktree 054; standalone chemistry used existing 019 RDKit and native validators used the 054 environment. |
| Authoritative full QC | failed | True | CHEBI:87393 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:87393 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:87393 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:87393 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:87393 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:87393 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:87393 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:87393 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:87393 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact neutral primary alcohol

identity: supported. Targets: CHEBI:87393.

The complete native graph, definition and conventional synonyms are coherent. Twelve authority encodings reproduce the same six-carbon primary alcohol, without stereo, salt or charge ambiguity. No inconsistent chemical synonym was established.

### Exact xrefs, document scope and broader terms

grounding: supported. Targets: CHEBI:87393.

ChEBI, KNApSAcK and PDB CCD identities and both parent terms are directly verified. Wikipedia resolves as a document reference. FooDB, HMDB, MetaCyc, CAS and Reaxys retain explicit independent-access limits; no unsupported claim of universal xref verification or confirmed wrong accession is made.

### Qualitative antibacterial role versus quantitative assay scope

evidence: supported. Targets: CHEBI:87393.

The original 2023 study directly tests the named positional isomer and supports a bounded antibacterial role. Its vapor assay cannot be converted to a liquid MIC or generalized beyond the tested strains. Internal reporting discrepancies and uninspected vegetable figures restrict numerical interpretation without contradicting the broad native role.

### Ten adopted leads and optional mechanisms

completeness: unknown. Targets: CHEBI:87393.

All ten adopted original abstracts were read. They supply biosynthetic, metabolic, aroma, behavioral or physical context rather than a demonstrated antibacterial molecular target. The additional full main study does not establish its proposed LPS mechanism. Absent optional target, resistance, producer and activity_spectrum fields are not defects.

### Generated ownership and unchanged history

provenance: supported. Targets: CHEBI:87393.

The complete native record, exact source row and all five chronological seed/reseed events were inspected. Original 13 and expanded 21 hashes remain unchanged. ChEBI extraction and seeding own generated content; no scientific status promotion or source mutation occurred.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

### A1

Optional evidence enrichment requires exact assay and material qualification.

- Before adding a quantitative observation from PMID:37628096, reconcile the dilution/headspace and table concentration discrepancies and preserve vapor exposure, strain, medium and categorical endpoint.
- Do not infer a demonstrated LPS target from the discussion hypothesis, or transfer essential-oil mixture, behavioral, production or host-metabolome outcomes to purified-compound antibacterial activity.
- Resolve the inaccessible authority pages before claiming every chemical xref was independently verified; lack of access alone does not require deletion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/hexan-1-ol.yaml; Entire native record, all 16 synonyms, parents, role, chemistry, seven chemical xrefs, document xref and five history events | supports | The SEEDED exact record denotes neutral hexan-1-ol, C6H14O, key ZSIAUFGUXNUGDI-UHFFFAOYSA-N. Its terminal alcohol has no stereocentre. No target, resistance, activity_spectrum, producer, causal graph or clinical-product claim is present. Conventional alcohol aliases were not treated as independent evidence of another compound. |
| owners | data/raw/chebi_antimicrobials.tsv#CHEBI:87393; Adopted row 2389, readiness row 1380 and exact curator/decision searches | context_only | The complete source row supplies identity, roles, synonyms and ten PMID leads. The raw foodb.food prefix is normalized to the appropriate foodb.compound field in the native record. No exact curator or decision override was found. All original 13 input hashes were preserved and expanded to 21 owner/context inputs. |
| search | /private/tmp/am-review-session/533-context-search.txt; Initial whole-tree and exact owner searches | context_only | Identifier, label and slug searches included hidden and gitignored files. No absence conclusion relies on a default ignored-file search. |
| chebi | https://www.ebi.ac.uk/chebi/backend/api/public/compound/87393/; Current CHEBI:87393 identity and database associations | supports | The current graph, formula, charge, definition and names match the native terminal primary alcohol. The source lists the same chemical associations, which are distinguished from independent verification of inaccessible registry pages. |
| knapsack | https://www.knapsackfamily.com/knapsack_core/information.php?word=C00000358; Current C00000358 structure and identifier fields | supports | KNApSAcK directly supplies matching SMILES, Standard InChI and key, formula, name and CAS association. Its organism list is database occurrence evidence and was not imported as an experimentally verified producer list. |
| ccd | https://files.rcsb.org/ligands/download/HE2.cif; Official chemical component HE2 descriptors and atom/bond graph | supports | The official ligand component is hexan-1-ol. Its five software SMILES encodings and Standard InChI agree with the native neutral C6 chain ending in OH. This validates an exact chemical xref, not antibacterial target binding. |
| mapping | /private/tmp/am-review-session/533-map.py; 019 RDKit 2026.03.5 run against cwd 054; 12 native/authority encodings | supports | Both native and ChEBI encodings, KNApSAcK SMILES/InChI and all six CCD encodings reproduce the full key, formula, neutral charge and reciprocal graph match. No stereocentre is present. Focused mass and minted-identifier checks also pass. |
| term143552 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/143552/; Current CHEBI:143552 definition | supports | Resolved hexanol: A fatty alcohol consisting of a hydroxy function at any position of an unbranched saturated chain of six carbon atoms. The native terminal OH and unbranched six-carbon chain satisfy this broader class. |
| term15734 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/15734/; Current CHEBI:15734 definition | supports | Resolved primary alcohol: A primary alcohol is a compound in which a hydroxy group, ‒OH, is attached to a saturated carbon atom which has either three hydrogen atoms attached to it or only one other carbon atom and two hydrogen atoms attached to it. The native terminal OH and unbranched six-carbon chain satisfy this broader class. |
| role | https://www.ebi.ac.uk/chebi/backend/api/public/compound/33282/; Current antibacterial-agent role; shared official snapshot | supports | The qualitative role concerns bacterial growth inhibition or killing, without prescribing a clinical indication, potency threshold or identified molecular target. |
| xref-limits | https://metacyc.org/compound?orgid=META&amp;id=HEXANOL-CMPD; Exact MetaCyc page and API, FooDB, HMDB, CAS and Reaxys access disposition | context_only | MetaCyc page/API returned an account-login page without the compound graph. FooDB page/JSON and HMDB page/XML returned 403; CAS detail returned 401. Reaxys 969167 registry content was not independently accessible through the free routes. These remain unresolved access boundaries, not evidence that an xref is wrong. Individual response hashes and timestamps are retained in the fetch manifests. |
| xref-fetches | /private/tmp/am-review-session/533-fetch2.json; Exact response statuses, URLs, times and SHA-256 values | context_only | This manifest preserves the additional FooDB/HMDB and MetaCyc attempts plus successful full-primary XML retrieval. The initial PMID query using a PMCID as EXT_ID returned no results; corrected PMID:37628096 metadata was retrieved separately. HTTP 200 for a login page is not treated as chemical verification. |
| document | https://en.wikipedia.org/wiki/1-Hexanol; Native document_xrefs Wikipedia 1-Hexanol page | context_only | The document resolves to the corresponding primary six-carbon alcohol. This broad secondary page was used to verify document scope only, not as primary activity or mechanism evidence. |
| pmid20055983 | PMID:20055983; DOI 10.1186/1471-2180-10-4; original abstract read | context_only | A human synbiotic-food intervention measures gut-community and fecal-metabolite changes. It is not administration of purified hexan-1-ol or a direct antibacterial assay. |
| pmid24508043 | PMID:24508043; DOI 10.1016/j.phytochem.2014.01.005; original abstract read | context_only | Pea-moth antennal, wind-tunnel and field responses concern volatile blends. Hexan-1-ol is one blend component and a secondary attractant in that context; no antibacterial endpoint is reported in the abstract. |
| pmid24634069 | PMID:24634069; DOI 10.1002/cbdv.201300234; original abstract read | context_only | The original identifies and evaluates aroma-active constituents of Evolvulus alsinoides essential oils, including hexan-1-ol. Mixture composition and odor activity are not pure-compound antibacterial evidence. |
| pmid29402559 | PMID:29402559; DOI 10.1016/j.saa.2018.01.041; original abstract read | context_only | Near-infrared measurements and anharmonic calculations compare n-hexanol, cyclohexanol and phenol. These are physical spectroscopy results, not antibacterial assays. |
| pmid29431748 | PMID:29431748; DOI 10.1039/c7cp07511a; original abstract read | context_only | Light scattering and molecular simulations examine 1-hexanol effects on synthetic C12E10 micelles. This does not directly establish disruption of bacterial membranes or a molecular target. |
| pmid35547160 | PMID:35547160; DOI 10.3389/fbioe.2022.850370; original abstract read | context_only | Clostridium carboxidivorans P7 produces hexanol during optimized syngas fermentation. Product titer and process productivity are not inhibitory concentrations. |
| pmid35568911 | PMID:35568911; DOI 10.1186/s12934-022-01802-8; original abstract read | context_only | Engineered Clostridium ljungdahlii produces butanol and hexanol after introduced biosynthesis genes. This is engineered biosynthesis, not an antibacterial target or native producer assignment without strain qualification. |
| pmid36087769 | PMID:36087769; DOI 10.1016/j.actatropica.2022.106680; original abstract read | context_only | Controlled-release 1-hexanol formulations attract Nyssomyia neivai sand flies with sex/feeding-state differences. Vector attraction is not parasite killing or antibacterial action. |
| pmid36374655 | PMID:36374655; DOI 10.1016/j.biortech.2022.128201; original abstract read | context_only | Extractive fermentation removes hexanol from Clostridium carboxidivorans P7 broth and improves production. The tested extraction-solvent inhibition and process titers do not provide a purified 1-hexanol MIC. |
| pmid37110426 | PMID:37110426; DOI 10.3390/microorganisms11041003; original abstract read | context_only | A continuous Clostridium co-culture produces C2–C6 alcohols. The stated growth inhibition concerns carbon monoxide, not an antibacterial endpoint for hexan-1-ol. |
| primary2023 | PMID:37628096; DOI 10.3390/foods12163097; full main text, Methods 2.1–2.4, Tables 1–2 and figure captions read | supports | Separate 1-, 2- and 3-hexanol reagents came from FUJIFILM Wako; catalog and purity are unspecified. In sealed dishes, 100 µL preculture was spread on 20 mL TSA or MRS agar; 50 µL ethanol-diluted reagent was applied to a lid-mounted disc and cultured for 48 h, with two repetitions. Table 1 gives clear inhibition zones at reported 300 ppm for E. coli IAM1264, P. aeruginosa ATCC10145 and S. enterica Enteritidis IFO3313. At reported 150 ppm, the first two show delayed/sparse growth and Salmonella a clear zone. The four Gram-positive strains and 2-/3-isomers are negative in this panel. These categorical vapor results are not liquid MICs. |
| primary2023-limits | PMID:37628096; Methods 2.1 versus Table 1; Discussion and vegetable experiment boundaries | context_only | The methods list nominal headspace concentrations 300/200/100/50 ppm, whereas Table 1 uses 300/150/75/38 ppm. The printed dilution units and delivery volumes do not independently establish measured gas-phase exposure, and Bacillus incubation is listed at both 37 and 30 °C. These reporting conflicts prevent unqualified quantitative transfer. Vegetable CFU results concern mixed surface communities; their figures were not independently viewed because the attempted image routes returned 403. Outer-membrane/LPS action is explicitly a hypothesis, without a direct mechanistic assay. |
| adapter | /private/tmp/am-review-session/533-adapter-scope.json; Native applicability assessed before open-web follow-up | context_only | The native record names no gene, protein, pathway or expression dataset. No structured expression query was applicable, and production enzymes mentioned only in additional literature do not become native antibacterial targets. |

## Limits And Additional Notes

- All ten adopted original abstracts were read, but their full experiments and supplementary data were not exhaustively reviewed. The additional 2023 primary main text, both tables and figure captions were read; the actual vegetable plots were not independently inspected after image requests returned 403. No figure-derived numerical values are used to justify the native role.
- The 2023 reagent catalog/purity, measured headspace exposure, inconsistent printed concentrations/dilution units and duplicated Bacillus incubation temperatures remain unresolved. Qualitative activity does not establish clinical efficacy, a molecular target or a transferable MIC.
- FooDB and HMDB returned 403, CAS returned 401, MetaCyc served an account-login page, and independent Reaxys registry access was unavailable. Matching source associations do not substitute for those exact authority checks.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All original 13 and expanded 21 input hashes were rechecked unchanged. Native files, source tables, history, saved bundles, progress and Git were not modified.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T181812Z-hexan-1-ol-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Hexan-1-ol: coherent identity and bounded vapor-phase antibacterial evidence'
started_at: '2026-10-21T18:00:57Z'
finished_at: '2026-10-21T18:18:12Z'
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
summary: The exact neutral primary-alcohol graph and broader classes agree with inspected
  authorities. All ten adopted original abstracts were read and distinguish metabolic,
  production, behavioral and physical studies from antibacterial evidence. An additional
  original study directly tests named 1-hexanol vapor, supporting the qualitative
  role with explicit assay and reporting limitations. No required native correction
  was established. Scientific assessment retains the stated evidence limits; full
  verification is blocked by the shared native-library failure.
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
  - path: data/antibiotics/antibacterial/hexan-1-ol.yaml
    sha256: 59f405cc4c035c383de7ebef4ba2aafa35434f853dc13ff1a05ac5454341b7f9
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
- target_id: CHEBI:87393
  path: data/antibiotics/antibacterial/hexan-1-ol.yaml
  label: hexan-1-ol
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
  selection: Assigned queue position 533; one exact native record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:87393
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0. Executed against worktree 054; standalone
    chemistry used existing 019 RDKit and native validators used the 054 environment.
  target_ids:
  - CHEBI:87393
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    533
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Executed against worktree 054; standalone
    chemistry used existing 019 RDKit and native validators used the 054 environment.
  target_ids:
  - CHEBI:87393
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/hexan-1-ol.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0. Executed against worktree 054; standalone
    chemistry used existing 019 RDKit and native validators used the 054 environment.
  target_ids:
  - CHEBI:87393
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/hexan-1-ol.yaml --out /private/tmp/am-review-session/533-strict.tsv
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
  - CHEBI:87393
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
  - CHEBI:87393
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
  - CHEBI:87393
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
  - CHEBI:87393
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
  - CHEBI:87393
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
  - CHEBI:87393
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
  - CHEBI:87393
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
  - CHEBI:87393
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
  - CHEBI:87393
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/hexan-1-ol.yaml
  locator: Entire native record, all 16 synonyms, parents, role, chemistry, seven
    chemical xrefs, document xref and five history events
  accessed_at: '2026-10-21T18:18:06Z'
  support: supports
  summary: The SEEDED exact record denotes neutral hexan-1-ol, C6H14O, key ZSIAUFGUXNUGDI-UHFFFAOYSA-N.
    Its terminal alcohol has no stereocentre. No target, resistance, activity_spectrum,
    producer, causal graph or clinical-product claim is present. Conventional alcohol
    aliases were not treated as independent evidence of another compound.
  snapshot_sha256: 59f405cc4c035c383de7ebef4ba2aafa35434f853dc13ff1a05ac5454341b7f9
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv#CHEBI:87393
  locator: Adopted row 2389, readiness row 1380 and exact curator/decision searches
  accessed_at: '2026-10-21T18:18:06Z'
  support: context_only
  summary: The complete source row supplies identity, roles, synonyms and ten PMID
    leads. The raw foodb.food prefix is normalized to the appropriate foodb.compound
    field in the native record. No exact curator or decision override was found. All
    original 13 input hashes were preserved and expanded to 21 owner/context inputs.
  snapshot_sha256: f3449c0a3c9d2dc089280a4ecd6170fb5661e2530455b3b610de7fb179d2273b
- evidence_id: search
  kind: search
  reference: /private/tmp/am-review-session/533-context-search.txt
  locator: Initial whole-tree and exact owner searches
  accessed_at: '2026-10-21T18:18:06Z'
  support: context_only
  summary: Identifier, label and slug searches included hidden and gitignored files.
    No absence conclusion relies on a default ignored-file search.
  snapshot_sha256: b133c07000686243539049f8d8a82ddcd48d86abb8c36e30b9696e9e1a382e7a
  search_scope: Worktree 054; initial 533-local-hits.txt plus rg --no-ignore --hidden
    across curation/conf/scripts/data/raw.
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/87393/
  locator: Current CHEBI:87393 identity and database associations
  accessed_at: '2026-10-21T18:12:56.326794Z'
  support: supports
  summary: The current graph, formula, charge, definition and names match the native
    terminal primary alcohol. The source lists the same chemical associations, which
    are distinguished from independent verification of inaccessible registry pages.
  snapshot_sha256: 0165de5ab9a29e1e29472d23fc6e7525cabb8337312dbb3dff1e3fdb504532ff
- evidence_id: knapsack
  kind: authority
  reference: https://www.knapsackfamily.com/knapsack_core/information.php?word=C00000358
  locator: Current C00000358 structure and identifier fields
  accessed_at: '2026-10-21T18:12:56.656694Z'
  support: supports
  summary: KNApSAcK directly supplies matching SMILES, Standard InChI and key, formula,
    name and CAS association. Its organism list is database occurrence evidence and
    was not imported as an experimentally verified producer list.
  snapshot_sha256: d5bca70623bdd0766764c24682cfe8ae05cdcdd1bf4ee1188654c5339769b0db
- evidence_id: ccd
  kind: authority
  reference: https://files.rcsb.org/ligands/download/HE2.cif
  locator: Official chemical component HE2 descriptors and atom/bond graph
  accessed_at: '2026-10-21T18:12:57.822209Z'
  support: supports
  summary: The official ligand component is hexan-1-ol. Its five software SMILES encodings
    and Standard InChI agree with the native neutral C6 chain ending in OH. This validates
    an exact chemical xref, not antibacterial target binding.
  snapshot_sha256: a607d95d28bb25bdbb4352d02308bdc3267e1040e1024c09e6e37d44ca4481f9
- evidence_id: mapping
  kind: validation
  reference: /private/tmp/am-review-session/533-map.py
  locator: 019 RDKit 2026.03.5 run against cwd 054; 12 native/authority encodings
  accessed_at: '2026-10-21T18:18:06Z'
  support: supports
  summary: Both native and ChEBI encodings, KNApSAcK SMILES/InChI and all six CCD
    encodings reproduce the full key, formula, neutral charge and reciprocal graph
    match. No stereocentre is present. Focused mass and minted-identifier checks also
    pass.
  snapshot_sha256: 35c669aeee7edde9428b8ab5f43306e4ad7a300809aa2605e4e7a599bf5f57be
- evidence_id: term143552
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/143552/
  locator: Current CHEBI:143552 definition
  accessed_at: '2026-10-21T18:12:59.250631Z'
  support: supports
  summary: 'Resolved hexanol: A fatty alcohol consisting of a hydroxy function at
    any position of an unbranched saturated chain of six carbon atoms. The native
    terminal OH and unbranched six-carbon chain satisfy this broader class.'
  snapshot_sha256: f40c4c2da2bde5bbd23397c030d4f9725ea973a4339b63f0d2b37e62c5665882
- evidence_id: term15734
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/15734/
  locator: Current CHEBI:15734 definition
  accessed_at: '2026-10-21T18:12:59.253155Z'
  support: supports
  summary: 'Resolved primary alcohol: A primary alcohol is a compound in which a hydroxy
    group, ‒OH, is attached to a saturated carbon atom which has either three hydrogen
    atoms attached to it or only one other carbon atom and two hydrogen atoms attached
    to it. The native terminal OH and unbranched six-carbon chain satisfy this broader
    class.'
  snapshot_sha256: 65634f82228203f66e1734ac2a57db2e158bf589836f240006c87d66db3c7fcb
- evidence_id: role
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/33282/
  locator: Current antibacterial-agent role; shared official snapshot
  accessed_at: '2026-10-21T18:18:06Z'
  support: supports
  summary: The qualitative role concerns bacterial growth inhibition or killing, without
    prescribing a clinical indication, potency threshold or identified molecular target.
  snapshot_sha256: 20d92ce7e00c204b1753184671c043160821d692438278344335446aadcd5082
- evidence_id: xref-limits
  kind: authority
  reference: https://metacyc.org/compound?orgid=META&id=HEXANOL-CMPD
  locator: Exact MetaCyc page and API, FooDB, HMDB, CAS and Reaxys access disposition
  accessed_at: '2026-10-21T18:12:56.918814Z'
  support: context_only
  summary: MetaCyc page/API returned an account-login page without the compound graph.
    FooDB page/JSON and HMDB page/XML returned 403; CAS detail returned 401. Reaxys
    969167 registry content was not independently accessible through the free routes.
    These remain unresolved access boundaries, not evidence that an xref is wrong.
    Individual response hashes and timestamps are retained in the fetch manifests.
  snapshot_sha256: 7c31f7080f0d3cf9d9fbd45c49780bb65e1e210855cff5bb395c5e72d05fd43d
- evidence_id: xref-fetches
  kind: validation
  reference: /private/tmp/am-review-session/533-fetch2.json
  locator: Exact response statuses, URLs, times and SHA-256 values
  accessed_at: '2026-10-21T18:18:06Z'
  support: context_only
  summary: This manifest preserves the additional FooDB/HMDB and MetaCyc attempts
    plus successful full-primary XML retrieval. The initial PMID query using a PMCID
    as EXT_ID returned no results; corrected PMID:37628096 metadata was retrieved
    separately. HTTP 200 for a login page is not treated as chemical verification.
  snapshot_sha256: af5228008664e1f5f6c5ab1e8e5d3e251292faa93d06af9645c4a75d87087f8d
- evidence_id: document
  kind: database
  reference: https://en.wikipedia.org/wiki/1-Hexanol
  locator: Native document_xrefs Wikipedia 1-Hexanol page
  accessed_at: '2026-10-21T18:12:59.919851Z'
  support: context_only
  summary: The document resolves to the corresponding primary six-carbon alcohol.
    This broad secondary page was used to verify document scope only, not as primary
    activity or mechanism evidence.
  snapshot_sha256: 31a9a6a776b3152bacfc1dc0f9c9005fcb3fd4325c8c623540a9df6abce1c1a2
- evidence_id: pmid20055983
  kind: primary_source
  reference: PMID:20055983
  locator: DOI 10.1186/1471-2180-10-4; original abstract read
  accessed_at: '2026-10-21T18:12:56.326991Z'
  support: context_only
  summary: A human synbiotic-food intervention measures gut-community and fecal-metabolite
    changes. It is not administration of purified hexan-1-ol or a direct antibacterial
    assay.
  snapshot_sha256: b22c830e8b8cacf8f67dd5d7cb5bd313fdbf1abac897e2abee64295543c0c85d
- evidence_id: pmid24508043
  kind: primary_source
  reference: PMID:24508043
  locator: DOI 10.1016/j.phytochem.2014.01.005; original abstract read
  accessed_at: '2026-10-21T18:12:56.326991Z'
  support: context_only
  summary: Pea-moth antennal, wind-tunnel and field responses concern volatile blends.
    Hexan-1-ol is one blend component and a secondary attractant in that context;
    no antibacterial endpoint is reported in the abstract.
  snapshot_sha256: b22c830e8b8cacf8f67dd5d7cb5bd313fdbf1abac897e2abee64295543c0c85d
- evidence_id: pmid24634069
  kind: primary_source
  reference: PMID:24634069
  locator: DOI 10.1002/cbdv.201300234; original abstract read
  accessed_at: '2026-10-21T18:12:56.326991Z'
  support: context_only
  summary: The original identifies and evaluates aroma-active constituents of Evolvulus
    alsinoides essential oils, including hexan-1-ol. Mixture composition and odor
    activity are not pure-compound antibacterial evidence.
  snapshot_sha256: b22c830e8b8cacf8f67dd5d7cb5bd313fdbf1abac897e2abee64295543c0c85d
- evidence_id: pmid29402559
  kind: primary_source
  reference: PMID:29402559
  locator: DOI 10.1016/j.saa.2018.01.041; original abstract read
  accessed_at: '2026-10-21T18:12:56.326991Z'
  support: context_only
  summary: Near-infrared measurements and anharmonic calculations compare n-hexanol,
    cyclohexanol and phenol. These are physical spectroscopy results, not antibacterial
    assays.
  snapshot_sha256: b22c830e8b8cacf8f67dd5d7cb5bd313fdbf1abac897e2abee64295543c0c85d
- evidence_id: pmid29431748
  kind: primary_source
  reference: PMID:29431748
  locator: DOI 10.1039/c7cp07511a; original abstract read
  accessed_at: '2026-10-21T18:12:56.326991Z'
  support: context_only
  summary: Light scattering and molecular simulations examine 1-hexanol effects on
    synthetic C12E10 micelles. This does not directly establish disruption of bacterial
    membranes or a molecular target.
  snapshot_sha256: b22c830e8b8cacf8f67dd5d7cb5bd313fdbf1abac897e2abee64295543c0c85d
- evidence_id: pmid35547160
  kind: primary_source
  reference: PMID:35547160
  locator: DOI 10.3389/fbioe.2022.850370; original abstract read
  accessed_at: '2026-10-21T18:12:56.326991Z'
  support: context_only
  summary: Clostridium carboxidivorans P7 produces hexanol during optimized syngas
    fermentation. Product titer and process productivity are not inhibitory concentrations.
  snapshot_sha256: b22c830e8b8cacf8f67dd5d7cb5bd313fdbf1abac897e2abee64295543c0c85d
- evidence_id: pmid35568911
  kind: primary_source
  reference: PMID:35568911
  locator: DOI 10.1186/s12934-022-01802-8; original abstract read
  accessed_at: '2026-10-21T18:12:56.326991Z'
  support: context_only
  summary: Engineered Clostridium ljungdahlii produces butanol and hexanol after introduced
    biosynthesis genes. This is engineered biosynthesis, not an antibacterial target
    or native producer assignment without strain qualification.
  snapshot_sha256: b22c830e8b8cacf8f67dd5d7cb5bd313fdbf1abac897e2abee64295543c0c85d
- evidence_id: pmid36087769
  kind: primary_source
  reference: PMID:36087769
  locator: DOI 10.1016/j.actatropica.2022.106680; original abstract read
  accessed_at: '2026-10-21T18:12:56.326991Z'
  support: context_only
  summary: Controlled-release 1-hexanol formulations attract Nyssomyia neivai sand
    flies with sex/feeding-state differences. Vector attraction is not parasite killing
    or antibacterial action.
  snapshot_sha256: b22c830e8b8cacf8f67dd5d7cb5bd313fdbf1abac897e2abee64295543c0c85d
- evidence_id: pmid36374655
  kind: primary_source
  reference: PMID:36374655
  locator: DOI 10.1016/j.biortech.2022.128201; original abstract read
  accessed_at: '2026-10-21T18:12:56.326991Z'
  support: context_only
  summary: Extractive fermentation removes hexanol from Clostridium carboxidivorans
    P7 broth and improves production. The tested extraction-solvent inhibition and
    process titers do not provide a purified 1-hexanol MIC.
  snapshot_sha256: b22c830e8b8cacf8f67dd5d7cb5bd313fdbf1abac897e2abee64295543c0c85d
- evidence_id: pmid37110426
  kind: primary_source
  reference: PMID:37110426
  locator: DOI 10.3390/microorganisms11041003; original abstract read
  accessed_at: '2026-10-21T18:12:56.326991Z'
  support: context_only
  summary: A continuous Clostridium co-culture produces C2–C6 alcohols. The stated
    growth inhibition concerns carbon monoxide, not an antibacterial endpoint for
    hexan-1-ol.
  snapshot_sha256: b22c830e8b8cacf8f67dd5d7cb5bd313fdbf1abac897e2abee64295543c0c85d
- evidence_id: primary2023
  kind: primary_source
  reference: PMID:37628096
  locator: DOI 10.3390/foods12163097; full main text, Methods 2.1–2.4, Tables 1–2
    and figure captions read
  accessed_at: '2026-10-21T18:14:59.538943Z'
  support: supports
  summary: Separate 1-, 2- and 3-hexanol reagents came from FUJIFILM Wako; catalog
    and purity are unspecified. In sealed dishes, 100 µL preculture was spread on
    20 mL TSA or MRS agar; 50 µL ethanol-diluted reagent was applied to a lid-mounted
    disc and cultured for 48 h, with two repetitions. Table 1 gives clear inhibition
    zones at reported 300 ppm for E. coli IAM1264, P. aeruginosa ATCC10145 and S.
    enterica Enteritidis IFO3313. At reported 150 ppm, the first two show delayed/sparse
    growth and Salmonella a clear zone. The four Gram-positive strains and 2-/3-isomers
    are negative in this panel. These categorical vapor results are not liquid MICs.
  snapshot_sha256: 9780e1a329d01c5920781ee64c56ff36622142b64d0be2c9bcf073295e07547d
- evidence_id: primary2023-limits
  kind: primary_source
  reference: PMID:37628096
  locator: Methods 2.1 versus Table 1; Discussion and vegetable experiment boundaries
  accessed_at: '2026-10-21T18:14:59.538943Z'
  support: context_only
  summary: The methods list nominal headspace concentrations 300/200/100/50 ppm, whereas
    Table 1 uses 300/150/75/38 ppm. The printed dilution units and delivery volumes
    do not independently establish measured gas-phase exposure, and Bacillus incubation
    is listed at both 37 and 30 °C. These reporting conflicts prevent unqualified
    quantitative transfer. Vegetable CFU results concern mixed surface communities;
    their figures were not independently viewed because the attempted image routes
    returned 403. Outer-membrane/LPS action is explicitly a hypothesis, without a
    direct mechanistic assay.
  snapshot_sha256: 9780e1a329d01c5920781ee64c56ff36622142b64d0be2c9bcf073295e07547d
- evidence_id: adapter
  kind: search
  reference: /private/tmp/am-review-session/533-adapter-scope.json
  locator: Native applicability assessed before open-web follow-up
  accessed_at: '2026-10-21T18:18:06Z'
  support: context_only
  summary: The native record names no gene, protein, pathway or expression dataset.
    No structured expression query was applicable, and production enzymes mentioned
    only in additional literature do not become native antibacterial targets.
  snapshot_sha256: f0d680db0a0f1350737815d5bde34c4e429181683485d0adaa03e80ac696f3dc
  search_scope: Entire native 533 and preserved shared catalog 456460-adapter-catalog.txt;
    no applicable native gene or pathway claim.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact neutral primary alcohol
  outcome: supported
  summary: The complete native graph, definition and conventional synonyms are coherent.
    Twelve authority encodings reproduce the same six-carbon primary alcohol, without
    stereo, salt or charge ambiguity. No inconsistent chemical synonym was established.
  target_ids:
  - CHEBI:87393
  evidence_ids:
  - native
  - chebi
  - knapsack
  - ccd
  - mapping
- assessment_id: grounding
  area: grounding
  topic: Exact xrefs, document scope and broader terms
  outcome: supported
  summary: ChEBI, KNApSAcK and PDB CCD identities and both parent terms are directly
    verified. Wikipedia resolves as a document reference. FooDB, HMDB, MetaCyc, CAS
    and Reaxys retain explicit independent-access limits; no unsupported claim of
    universal xref verification or confirmed wrong accession is made.
  target_ids:
  - CHEBI:87393
  evidence_ids:
  - chebi
  - knapsack
  - ccd
  - mapping
  - term143552
  - term15734
  - document
  - xref-limits
  - xref-fetches
- assessment_id: activity
  area: evidence
  topic: Qualitative antibacterial role versus quantitative assay scope
  outcome: supported
  summary: The original 2023 study directly tests the named positional isomer and
    supports a bounded antibacterial role. Its vapor assay cannot be converted to
    a liquid MIC or generalized beyond the tested strains. Internal reporting discrepancies
    and uninspected vegetable figures restrict numerical interpretation without contradicting
    the broad native role.
  target_ids:
  - CHEBI:87393
  evidence_ids:
  - role
  - primary2023
  - primary2023-limits
- assessment_id: completeness
  area: completeness
  topic: Ten adopted leads and optional mechanisms
  outcome: unknown
  summary: All ten adopted original abstracts were read. They supply biosynthetic,
    metabolic, aroma, behavioral or physical context rather than a demonstrated antibacterial
    molecular target. The additional full main study does not establish its proposed
    LPS mechanism. Absent optional target, resistance, producer and activity_spectrum
    fields are not defects.
  target_ids:
  - CHEBI:87393
  evidence_ids:
  - owners
  - pmid20055983
  - pmid24508043
  - pmid24634069
  - pmid29402559
  - pmid29431748
  - pmid35547160
  - pmid35568911
  - pmid36087769
  - pmid36374655
  - pmid37110426
  - primary2023-limits
  - adapter
- assessment_id: provenance
  area: provenance
  topic: Generated ownership and unchanged history
  outcome: supported
  summary: The complete native record, exact source row and all five chronological
    seed/reseed events were inspected. Original 13 and expanded 21 hashes remain unchanged.
    ChEBI extraction and seeding own generated content; no scientific status promotion
    or source mutation occurred.
  target_ids:
  - CHEBI:87393
  evidence_ids:
  - native
  - owners
  - search
findings: []
actions:
- action_id: A1
  description: Optional evidence enrichment requires exact assay and material qualification.
  finding_ids: []
  target_ids:
  - CHEBI:87393
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/hexan-1-ol.yaml
    role: Future validated curator-owned literature annotation
  acceptance_checks:
  - Before adding a quantitative observation from PMID:37628096, reconcile the dilution/headspace
    and table concentration discrepancies and preserve vapor exposure, strain, medium
    and categorical endpoint.
  - Do not infer a demonstrated LPS target from the discussion hypothesis, or transfer
    essential-oil mixture, behavioral, production or host-metabolome outcomes to purified-compound
    antibacterial activity.
  - Resolve the inaccessible authority pages before claiming every chemical xref was
    independently verified; lack of access alone does not require deletion.
limitations:
- All ten adopted original abstracts were read, but their full experiments and supplementary
  data were not exhaustively reviewed. The additional 2023 primary main text, both
  tables and figure captions were read; the actual vegetable plots were not independently
  inspected after image requests returned 403. No figure-derived numerical values
  are used to justify the native role.
- The 2023 reagent catalog/purity, measured headspace exposure, inconsistent printed
  concentrations/dilution units and duplicated Bacillus incubation temperatures remain
  unresolved. Qualitative activity does not establish clinical efficacy, a molecular
  target or a transferable MIC.
- FooDB and HMDB returned 403, CAS returned 401, MetaCyc served an account-login page,
  and independent Reaxys registry access was unavailable. Matching source associations
  do not substitute for those exact authority checks.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All original 13 and expanded 21 input hashes were rechecked unchanged. Native files,
  source tables, history, saved bundles, progress and Git were not modified.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
