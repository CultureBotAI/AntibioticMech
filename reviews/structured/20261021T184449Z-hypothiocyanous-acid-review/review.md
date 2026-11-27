# Review of hypothiocyanous acid

- Review: 20261021T184449Z-hypothiocyanous-acid-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T18:07:34Z
- Finished UTC: 2026-10-21T18:44:49Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The neutral HOSCN graph, formula and structural parents are supported. One major grounding issue remains: the exact CAS reference and Hypothiocyanite alias identify the conjugate anion in independent authorities. Preserve the valid neutral graph and distinguish aqueous acid/anion equilibrium, enzyme-generated oxidant systems and host-protein experiments when interpreting the supported qualitative antimicrobial roles.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position 544; all original 13 captured input hashes preserved. Actual ChEBI extraction, role and generator owners were identified before assessment and were already among the captured inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:133907 | data/antibiotics/antibacterial/hypothiocyanous-acid.yaml | generated | hypothiocyanous acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:133907 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:133907 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:133907 | Actual focused execution exited 0. |
| Independent structure and acid/anion comparison | passed | False | CHEBI:133907 | Eleven neutral encodings agree. Exact native CAS resolves to anion; a one-proton/oxygen-charge operation reproduces its distinct key without changing connectivity. |
| Source, reference and history audit | passed | False | CHEBI:133907 | All 13 original hashes, three chronological history events, deterministic mint and ten adopted complete-abstract dispositions verified. |
| Structured bacterial protein discovery | passed | False | CHEBI:133907 | Actual free structured query completed before protein-specific primary follow-up; discovery membership is not mechanistic evidence. |
| Structured bacterial protein discovery | passed | False | CHEBI:133907 | Actual free structured query completed before protein-specific primary follow-up; discovery membership is not mechanistic evidence. |
| Structured bacterial protein discovery | passed | False | CHEBI:133907 | Actual free structured query completed before protein-specific primary follow-up; discovery membership is not mechanistic evidence. |
| Authoritative full QC | failed | True | CHEBI:133907 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:133907 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:133907 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:133907 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:133907 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:133907 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:133907 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:133907 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:133907 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Neutral HOSCN constitution and structural parents

identity: supported. Targets: CHEBI:133907.

Native valid graph, formula, mass and current chemical encodings agree. One-carbon sulfur oxoacid classification and structural definition fit.

### Exact acid versus conjugate-anion name and CAS

grounding: concern. Targets: CHEBI:133907.

The native anion alias/CAS cannot be exact neutral-acid equivalents under this repository contract. Current source repetition is preserved as a source conflict; acid-base equilibrium does not erase the formal identity distinction.

### Qualitative antibacterial, antiviral and antifungal roles

scope: supported. Targets: CHEBI:133907.

Original experiments support these bounded activities in aqueous acid/anion and enzyme-generated contexts. Fungal comparator and host/viral scopes are explicit; no pure-acid quantitative potency or clinical claim is added.

### Optional exact primary biochemical detail

completeness: unknown. Targets: CHEBI:133907.

The record makes no target claim. E. coli L-TrxR inhibition is a primary enrichment candidate with explicit preparation/assay scope; it is not established here as the sole cause of killing across taxa. Host eNOS/GAPDH data remain host effects.

### Complete native source and lead disposition

provenance: supported. Targets: CHEBI:133907.

All thirteen original inputs, exact maintained owners, three history events and ten adopted references were checked. Direct-access and indexed-authority limitations are stated rather than hidden.

## Findings

### F1: Neutral acid is assigned the conjugate-anion CAS and exact alias

major / open / confirmed; issue key: hypothiocyanous-acid-anion-cas-and-exact-alias.

The neutral acid CHNOS/key...-N is valid, but cas:63296-34-4 maps independently to hypothiocyanite CNOS⁻/key...-M, and Hypothiocyanite is typed EXACT_SYNONYM. FDA and CAS-attributed PubChem data distinguish the anion; original kinetic literature likewise distinguishes the conjugate forms. ChEBI/HMDB naming conflation does not satisfy the repository same-structure xref contract. This is one linked acid/anion grounding issue, not a proposed replacement of the native graph.

## Recommended Actions And Acceptance Checks

### A1

Retain the neutral HOSCN graph. Correct or withhold cas:63296-34-4 through the maintained ChEBI extraction/grounding lane, recording the FDA/CAS-attributed source conflict. Candidate acid CAS64253-39-0 needs direct registry or equivalently authoritative exact-form confirmation before adoption. Add a CHEBI:133907-specific Hypothiocyanite entry to existing synonym_exclusions, or preserve the name only with an explicit non-exact conjugate-base relationship if the native schema supports one. Regenerate and reseed; do not globally ban the correct anion name, move the CAS into an unrelated drug namespace, or hand-edit the emitted record alone.

- Exact neutral record retains N#CSO, CHNOS, charge 0 and ZCZCOXLLICTZAH-UHFFFAOYSA-N.
- No exact name/CAS assertion equates it to CNOS⁻/key...-M; source disagreement and any approved replacement provenance remain explicit.
- Any added activity or mechanism keeps aqueous equilibrium, pH, generated-system controls, organism and host-versus-microbial scope.
- Focused schema/strict plus required source/reference/history/corpus and full QC pass for eventual native curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/hypothiocyanous-acid.yaml; Entire record, definition, all five synonyms, two structural parents, three roles, four xrefs, source concept and three history events | supports | The SEEDED/EXACT record encodes neutral N#CSO with formula CHNOS and charge zero. It has the exact alias Hypothiocyanite at synonyms[2] and cas:63296-34-4 at xrefs[0]. No molecular target, resistance mechanism, activity observation, clinical assertion, producer or causal graph is natively asserted. |
| chemistry | CHEBI:133907;pubchem.compound:124985;chemspider:111270; 544-authority-chemistry.json; current ChEBI JSON/mol, PubChem key lookup and ChemSpider HTML;544-fetch.json | supports | Eleven native/current neutral encodings agree at ZCZCOXLLICTZAH-UHFFFAOYSA-N, CHNOS and zero charge, with no stereocentres. ChemSpider 111270 explicitly contains the matching InChI and SMILES despite mixed acid/anion aliases. Native masses agree at declared precision. The intended acid structure does not need repair. |
| anion | CAS:63296-34-4;FDA UNII:N84CZ7T0OY;pubchem.compound:124984; 544-pubchem-cas.json;544-gsrs.html;544-pubchem-anion-view.json;544-fetch3.json/544-fetch4.json | supports | Exact CAS lookup returns C(#N)S[O-], CNOS⁻, charge −1 and ZCZCOXLLICTZAH-UHFFFAOYSA-M. FDA independently names HYPOTHIOCYANITE ION and maps the same CAS/name to that anion key. PubChem explicitly attributes the CAS registration to CAS Common Chemistry. Direct CAS API requests returned 401, so CAS authority is inspected through attributed PubChem data and independent FDA corroboration, not a claimed direct registry read. |
| source-conflict | CHEBI:133907;hmdb:HMDB0012974;reaxys:2958668; 544-chebi-133907.json;544-fetch.json/544-fetch2.json; official HMDB indexed search excerpt;544-source-audit.json | supports | Current ChEBI repeats the anion name and CAS on its neutral graph. Direct HMDB HTML/XML/SDF access returned 403; the official indexed excerpt displays neutral OSC#N and CHNOS under the Hypothiocyanite title, so the label alone does not prove a wrong HMDB graph. Reaxys 2958668 remains source-attributed without a licensed structure read. PubChem maps candidate acid CAS64253-39-0 to the neutral structure, but direct registry verification is still required before replacing the native CAS. |
| terms | CHEBI:33402;CHEBI:64708;CHEBI:22587;CHEBI:33282;CHEBI:35718; 544-chebi-33402/64708/22587/33282/35718.json and raw ChEBI row | supports | Sulfur oxoacid and one-carbon compound parents fit CN-S-OH. Role terms resolve to antiviral, antibacterial and antifungal agents. The structural definition and systematic acid names remain consistent; uncommon source aliases are not treated as independently proven nomenclature beyond the inspected authority context. |
| equilibrium | PMID:19821602;DOI:10.1021/tx900249d;PMID:22031955;DOI:10.1021/ja2083152; 544-adopted-core.json complete abstracts; direct ACS main requests403 and OpenAlex access metadata in544-fetch2.json/544-fetch4.json | supports | The original kinetic studies explicitly distinguish HOSCN from its conjugate base OSCN−. The 2009 abstract reports pKa 4.85 at 25°C and ionic strength 120 mM, and thiolate/acid reaction chemistry; the 2011 abstract describes pH-dependent decomposition and reaction products. These support the chemical distinction, not a universal pKa under all conditions or a numerical antimicrobial assay. Full original mains were not available. |
| adapter | iModulonDB E.coli precise1k and P.aeruginosa precise364; 544-adapter-results.json and three saved exact query outputs | supports | E. coli gapA/trxB and P. aeruginosa gor were queried before bacterial-protein follow-up. Gene or module discovery is not evidence of direct HOSCN targeting. Native absence of a target assertion is preserved; no target is inserted from catalogue membership. |
| bacterial-primary | PMID:23629660;DOI:10.1074/jbc.M113.468090; 544-PMC3689984.html; original abstract/introduction, methods, bacterial/enzyme Results, Tables1/2, Fig2/3 captions and relevant Discussion;544-fetch5.json | supports | The study prepares aqueous oxidant using LPO/thiocyanate/peroxide at pH 7.4, removes peroxide with catalase and proteins by filtration, and quantifies reactive oxidant. Recombinant E. coli L-TrxR is inhibited in a defined NADPH-containing assay; mammalian Sec-containing TrxR instead metabolizes the oxidant under tested conditions. Separate AB1157/PAO1 and clinical-isolate exposures use an enzyme-coupled system at pH 6.8/7.4 and CFU viability. Acid/anion equilibrium, biochemical inhibition and system-level killing are distinct; these results do not prove a sole universal bacterial target or universal host safety. |
| fungal-primary | PMID:23662084;DOI:10.2147/CCIDEN.S10891; 544-PMC3645462.xml; original abstract, organism/generation methods, thiocyanate comparator Results and Discussion | supports | C. albicans ATCC10231 was tested with glucose/glucose-oxidase/LPO/thiocyanate systems and appropriate peroxide/system controls. The thiocyanate system yields modest colony reduction or delayed attachment under selected conditions; iodide-generated hypoiodite is substantially stronger and more durable. Retain qualified antifungal support without transferring hypoiodite results, claiming durable sterilization of every strain, or treating system substrate concentration as a pure-HOSCN MIC. |
| viral-primary | PMID:23540488;DOI:10.1016/j.ijheh.2013.03.001; 544-adopted-core.json complete original abstract; publisher main403 in544-fetch5.json | supports | The original abstract reports in vitro A/H1N1/2009 virucidal activity of enzyme-free hypothiocyanite/HOSCN preparation, including direct virus challenge and subsequent cell exposure. This supports a bounded qualitative antiviral role. Exact assay pH/material speciation and full controls were not independently inspected, and no pure-acid EC50, clinical efficacy or general safety claim is adopted. |
| adopted | All ten adopted PMID leads; 544-adopted-core.json and544-source-audit.json individual dispositions | supports | All ten complete available abstracts were read.19705807/19821602/22031955 concern reaction chemistry;22053976/24632382 are reviews;23088652/24112082/24120969 concern host HDL, eNOS or endothelial injury;24657078 measures olive-extract effects on LPO production;23540488 is the exact influenza experiment. Host enzymes, decomposition products and oxidant-production assays are not silently recast as bacterial targets or direct antimicrobial potency. |
| owners | ChEBI inventory and roles, extraction, seeding, conf/sources.yaml and curation decisions; 544-owners-search.json;544-raw-rows.json;544-source-audit.json;docs/CURATION.md exact-xref contract andseed_from_sources.py xref gates | supports | All original 13 hashes are unchanged; actual owners were already captured. Three chronological history events and the deterministic source mint agree. Native xrefs explicitly mean the same structure and exclude conjugate acids/bases. The current source imports both disputed values; synonym_exclusions supports an exact source-scoped name withholding, while a CAS correction requires an explicit source/grounding decision rather than a silent global namespace change. |
| discovery | Bounded public HOSCN/OSCN− antibacterial and antifungal discovery; 544-discovery.json;544-PMC11088529.html;544-PMC13423671.xml;544-source-audit.json | supports | The query returned 93 records and informed selected primary follow-up; it is not an exhaustive full-main review. The 2024 review was used to locate its original fungal reference 77. The 2026 Pseudomonas article is explicitly a review-article and was not misclassified as a new primary experiment. Searches and failed direct-authority routes are retained. |

## Limits And Additional Notes

- Direct CAS Common Chemistry API returned 401; CAS attribution was inspected in PubChem and independently corroborated by the official FDA substance record. Candidate acid CAS64253-39-0 remains a candidate, not a verified direct-registry replacement.
- HMDB direct HTML, XML and structure downloads returned 403. Its indexed official neutral structure was read, but the full current entry was not fetched. Reaxys 2958668 was not independently accessed. ChemSpider direct HTML succeeded although the browser route returned 403.
- All ten adopted abstracts were inspected; original kinetic/decomposition and antiviral mains returned 403. Their abstract-level support is stated. The bacterial and fungal original main passages were read at the declared depth; figures were read through captions/text, not independently digitized.
- Published HOSCN preparations here are aqueous equilibria or enzymatic oxidant systems. No assay is represented as an isolated neutral-acid measurement solely because the article calls its preparation HOSCN. pKa and potency are condition-dependent.
- The fungal thiocyanate comparator is weaker and less durable than hypoiodite. Positive results are not transferred from iodide systems or combination formulations, and incomplete efficacy is not treated as proof of no antifungal role.
- Host injury papers and the 2013 host-tolerance experiment have different materials and conditions; no universal harmlessness or sole bacterial molecular target is inferred. No exhaustive absence claim about other targets or later literature is made.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native record, maintained source, saved bundle or history was edited. All original thirteen input hashes remain unchanged.
- Chemistry used the 019 interpreter against 055; schema, strict, ledger and contract use 055. Stable scratch draft is handed to the root finalizer for ordered review saving.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T184449Z-hypothiocyanous-acid-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of hypothiocyanous acid
started_at: '2026-10-21T18:07:34Z'
finished_at: '2026-10-21T18:44:49Z'
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
summary: 'The neutral HOSCN graph, formula and structural parents are supported. One
  major grounding issue remains: the exact CAS reference and Hypothiocyanite alias
  identify the conjugate anion in independent authorities. Preserve the valid neutral
  graph and distinguish aqueous acid/anion equilibrium, enzyme-generated oxidant systems
  and host-protein experiments when interpreting the supported qualitative antimicrobial
  roles.'
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
  - path: data/antibiotics/antibacterial/hypothiocyanous-acid.yaml
    sha256: 4d0b2be0c1c5906829b3f8ecaf36a0710ddb542d9415b0686a4a605f23ec0ed5
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
- target_id: CHEBI:133907
  path: data/antibiotics/antibacterial/hypothiocyanous-acid.yaml
  label: hypothiocyanous acid
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Exact identity, definition, synonyms, parents, roles and adopted lead
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_role_names.tsv
    role: Role labels
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated record and role policy
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusions
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Class and role configuration
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position 544; all original 13 captured input
    hashes preserved. Actual ChEBI extraction, role and generator owners were identified
    before assessment and were already among the captured inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:133907
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:133907
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    544
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:133907
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/hypothiocyanous-acid.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:133907
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/hypothiocyanous-acid.yaml --out /private/tmp/am-review-session/544-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: authority
  name: Independent structure and acid/anion comparison
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/544-authority-check.py
    > /private/tmp/am-review-session/544-authority-check.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Eleven neutral encodings agree. Exact native CAS resolves to anion; a one-proton/oxygen-charge
    operation reproduces its distinct key without changing connectivity.
  target_ids:
  - CHEBI:133907
- check_id: ledger
  name: Source, reference and history audit
  command: .venv/bin/python /private/tmp/am-review-session/544-ledger.py > /private/tmp/am-review-session/544-ledger.log
    2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: All 13 original hashes, three chronological history events, deterministic
    mint and ten adopted complete-abstract dispositions verified.
  target_ids:
  - CHEBI:133907
- check_id: adapter-0
  name: Structured bacterial protein discovery
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset precise1k --query gapA
    > /private/tmp/am-review-session/544-adapter-e_coli-gapA.txt 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Actual free structured query completed before protein-specific primary
    follow-up; discovery membership is not mechanistic evidence.
  target_ids:
  - CHEBI:133907
- check_id: adapter-1
  name: Structured bacterial protein discovery
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset precise1k --query trxB
    > /private/tmp/am-review-session/544-adapter-e_coli-trxB.txt 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Actual free structured query completed before protein-specific primary
    follow-up; discovery membership is not mechanistic evidence.
  target_ids:
  - CHEBI:133907
- check_id: adapter-2
  name: Structured bacterial protein discovery
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism p_aeruginosa --dataset precise364 --query
    gor > /private/tmp/am-review-session/544-adapter-p_aeruginosa-gor.txt 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Actual free structured query completed before protein-specific primary
    follow-up; discovery membership is not mechanistic evidence.
  target_ids:
  - CHEBI:133907
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:133907
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
  - CHEBI:133907
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
  - CHEBI:133907
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
  - CHEBI:133907
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
  - CHEBI:133907
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
  - CHEBI:133907
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
  - CHEBI:133907
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
  - CHEBI:133907
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
  - CHEBI:133907
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/hypothiocyanous-acid.yaml
  locator: Entire record, definition, all five synonyms, two structural parents, three
    roles, four xrefs, source concept and three history events
  accessed_at: '2026-10-21T18:44:24Z'
  support: supports
  summary: The SEEDED/EXACT record encodes neutral N#CSO with formula CHNOS and charge
    zero. It has the exact alias Hypothiocyanite at synonyms[2] and cas:63296-34-4
    at xrefs[0]. No molecular target, resistance mechanism, activity observation,
    clinical assertion, producer or causal graph is natively asserted.
- evidence_id: chemistry
  kind: validation
  reference: CHEBI:133907;pubchem.compound:124985;chemspider:111270
  locator: 544-authority-chemistry.json; current ChEBI JSON/mol, PubChem key lookup
    and ChemSpider HTML;544-fetch.json
  accessed_at: '2026-10-21T18:44:24Z'
  support: supports
  summary: Eleven native/current neutral encodings agree at ZCZCOXLLICTZAH-UHFFFAOYSA-N,
    CHNOS and zero charge, with no stereocentres. ChemSpider 111270 explicitly contains
    the matching InChI and SMILES despite mixed acid/anion aliases. Native masses
    agree at declared precision. The intended acid structure does not need repair.
  snapshot_sha256: e71015905388f4778d908ff9f5e69665f076ca40633f12d3f0273ddd329d1f98
- evidence_id: anion
  kind: authority
  reference: CAS:63296-34-4;FDA UNII:N84CZ7T0OY;pubchem.compound:124984
  locator: 544-pubchem-cas.json;544-gsrs.html;544-pubchem-anion-view.json;544-fetch3.json/544-fetch4.json
  accessed_at: '2026-10-21T18:44:24Z'
  support: supports
  summary: Exact CAS lookup returns C(#N)S[O-], CNOS⁻, charge −1 and ZCZCOXLLICTZAH-UHFFFAOYSA-M.
    FDA independently names HYPOTHIOCYANITE ION and maps the same CAS/name to that
    anion key. PubChem explicitly attributes the CAS registration to CAS Common Chemistry.
    Direct CAS API requests returned 401, so CAS authority is inspected through attributed
    PubChem data and independent FDA corroboration, not a claimed direct registry
    read.
  snapshot_sha256: 0151536b2294d1ba302c5096d5fa2dd96a19e9d6c66bc2583e41c2a0d37a1233
- evidence_id: source-conflict
  kind: authority
  reference: CHEBI:133907;hmdb:HMDB0012974;reaxys:2958668
  locator: 544-chebi-133907.json;544-fetch.json/544-fetch2.json; official HMDB indexed
    search excerpt;544-source-audit.json
  accessed_at: '2026-10-21T18:44:24Z'
  support: supports
  summary: Current ChEBI repeats the anion name and CAS on its neutral graph. Direct
    HMDB HTML/XML/SDF access returned 403; the official indexed excerpt displays neutral
    OSC#N and CHNOS under the Hypothiocyanite title, so the label alone does not prove
    a wrong HMDB graph. Reaxys 2958668 remains source-attributed without a licensed
    structure read. PubChem maps candidate acid CAS64253-39-0 to the neutral structure,
    but direct registry verification is still required before replacing the native
    CAS.
  snapshot_sha256: 5fb78909abcc297e834b5837c94031091353ccc3b3d2fa11aea0d2e67ab40cc6
- evidence_id: terms
  kind: authority
  reference: CHEBI:33402;CHEBI:64708;CHEBI:22587;CHEBI:33282;CHEBI:35718
  locator: 544-chebi-33402/64708/22587/33282/35718.json and raw ChEBI row
  accessed_at: '2026-10-21T18:44:24Z'
  support: supports
  summary: Sulfur oxoacid and one-carbon compound parents fit CN-S-OH. Role terms
    resolve to antiviral, antibacterial and antifungal agents. The structural definition
    and systematic acid names remain consistent; uncommon source aliases are not treated
    as independently proven nomenclature beyond the inspected authority context.
  snapshot_sha256: 25f2bb3191e96f69422c0ead3f17cfb67dbdfed5d8d2ad0e105172adeed8bfea
- evidence_id: equilibrium
  kind: primary_source
  reference: PMID:19821602;DOI:10.1021/tx900249d;PMID:22031955;DOI:10.1021/ja2083152
  locator: 544-adopted-core.json complete abstracts; direct ACS main requests403 and
    OpenAlex access metadata in544-fetch2.json/544-fetch4.json
  accessed_at: '2026-10-21T18:44:24Z'
  support: supports
  summary: The original kinetic studies explicitly distinguish HOSCN from its conjugate
    base OSCN−. The 2009 abstract reports pKa 4.85 at 25°C and ionic strength 120
    mM, and thiolate/acid reaction chemistry; the 2011 abstract describes pH-dependent
    decomposition and reaction products. These support the chemical distinction, not
    a universal pKa under all conditions or a numerical antimicrobial assay. Full
    original mains were not available.
  snapshot_sha256: 93d2e8b1d504985a6656e1dbb5395caa6dda57b1c4212d89613b84391020c31a
- evidence_id: adapter
  kind: search
  reference: iModulonDB E.coli precise1k and P.aeruginosa precise364
  locator: 544-adapter-results.json and three saved exact query outputs
  accessed_at: '2026-10-21T18:44:24Z'
  support: supports
  summary: E. coli gapA/trxB and P. aeruginosa gor were queried before bacterial-protein
    follow-up. Gene or module discovery is not evidence of direct HOSCN targeting.
    Native absence of a target assertion is preserved; no target is inserted from
    catalogue membership.
  search_scope: Free structured exact gene queries in catalogue-valid bacterial datasets,
    followed by bounded original thiol/enzyme and whole-cell literature inspection.
  snapshot_sha256: 84e987dc4704f0134f7582474ed8c7abee924dee8dc7e93e668925be2a465a2c
- evidence_id: bacterial-primary
  kind: primary_source
  reference: PMID:23629660;DOI:10.1074/jbc.M113.468090
  locator: 544-PMC3689984.html; original abstract/introduction, methods, bacterial/enzyme
    Results, Tables1/2, Fig2/3 captions and relevant Discussion;544-fetch5.json
  accessed_at: '2026-10-21T18:44:24Z'
  support: supports
  summary: The study prepares aqueous oxidant using LPO/thiocyanate/peroxide at pH
    7.4, removes peroxide with catalase and proteins by filtration, and quantifies
    reactive oxidant. Recombinant E. coli L-TrxR is inhibited in a defined NADPH-containing
    assay; mammalian Sec-containing TrxR instead metabolizes the oxidant under tested
    conditions. Separate AB1157/PAO1 and clinical-isolate exposures use an enzyme-coupled
    system at pH 6.8/7.4 and CFU viability. Acid/anion equilibrium, biochemical inhibition
    and system-level killing are distinct; these results do not prove a sole universal
    bacterial target or universal host safety.
  snapshot_sha256: 0a07c7af88b01e542e6ce616e76132acc91b17a541c877696ac0668cb7bf060f
- evidence_id: fungal-primary
  kind: primary_source
  reference: PMID:23662084;DOI:10.2147/CCIDEN.S10891
  locator: 544-PMC3645462.xml; original abstract, organism/generation methods, thiocyanate
    comparator Results and Discussion
  accessed_at: '2026-10-21T18:44:24Z'
  support: supports
  summary: C. albicans ATCC10231 was tested with glucose/glucose-oxidase/LPO/thiocyanate
    systems and appropriate peroxide/system controls. The thiocyanate system yields
    modest colony reduction or delayed attachment under selected conditions; iodide-generated
    hypoiodite is substantially stronger and more durable. Retain qualified antifungal
    support without transferring hypoiodite results, claiming durable sterilization
    of every strain, or treating system substrate concentration as a pure-HOSCN MIC.
  snapshot_sha256: 2c9b7b20b87983532fdd62c87609b3ef087ed2d12001815d0299c79bfb7a5bb1
- evidence_id: viral-primary
  kind: primary_source
  reference: PMID:23540488;DOI:10.1016/j.ijheh.2013.03.001
  locator: 544-adopted-core.json complete original abstract; publisher main403 in544-fetch5.json
  accessed_at: '2026-10-21T18:44:24Z'
  support: supports
  summary: The original abstract reports in vitro A/H1N1/2009 virucidal activity of
    enzyme-free hypothiocyanite/HOSCN preparation, including direct virus challenge
    and subsequent cell exposure. This supports a bounded qualitative antiviral role.
    Exact assay pH/material speciation and full controls were not independently inspected,
    and no pure-acid EC50, clinical efficacy or general safety claim is adopted.
  snapshot_sha256: 93d2e8b1d504985a6656e1dbb5395caa6dda57b1c4212d89613b84391020c31a
- evidence_id: adopted
  kind: database
  reference: All ten adopted PMID leads
  locator: 544-adopted-core.json and544-source-audit.json individual dispositions
  accessed_at: '2026-10-21T18:44:24Z'
  support: supports
  summary: All ten complete available abstracts were read.19705807/19821602/22031955
    concern reaction chemistry;22053976/24632382 are reviews;23088652/24112082/24120969
    concern host HDL, eNOS or endothelial injury;24657078 measures olive-extract effects
    on LPO production;23540488 is the exact influenza experiment. Host enzymes, decomposition
    products and oxidant-production assays are not silently recast as bacterial targets
    or direct antimicrobial potency.
  snapshot_sha256: ede48a6c05b2eae5d6a20ff2b408dfa53d89c4e83a9a2196d25e532f53c261b5
- evidence_id: owners
  kind: validation
  reference: ChEBI inventory and roles, extraction, seeding, conf/sources.yaml and
    curation decisions
  locator: 544-owners-search.json;544-raw-rows.json;544-source-audit.json;docs/CURATION.md
    exact-xref contract andseed_from_sources.py xref gates
  accessed_at: '2026-10-21T18:44:24Z'
  support: supports
  summary: All original 13 hashes are unchanged; actual owners were already captured.
    Three chronological history events and the deterministic source mint agree. Native
    xrefs explicitly mean the same structure and exclude conjugate acids/bases. The
    current source imports both disputed values; synonym_exclusions supports an exact
    source-scoped name withholding, while a CAS correction requires an explicit source/grounding
    decision rather than a silent global namespace change.
  snapshot_sha256: ede48a6c05b2eae5d6a20ff2b408dfa53d89c4e83a9a2196d25e532f53c261b5
- evidence_id: discovery
  kind: search
  reference: Bounded public HOSCN/OSCN− antibacterial and antifungal discovery
  locator: 544-discovery.json;544-PMC11088529.html;544-PMC13423671.xml;544-source-audit.json
  accessed_at: '2026-10-21T18:44:24Z'
  support: supports
  summary: The query returned 93 records and informed selected primary follow-up;
    it is not an exhaustive full-main review. The 2024 review was used to locate its
    original fungal reference 77. The 2026 Pseudomonas article is explicitly a review-article
    and was not misclassified as a new primary experiment. Searches and failed direct-authority
    routes are retained.
  search_scope: Ignored-inclusive local owner/identifier search; all adopted EuropePMC
    MED records; bounded title/abstract discovery for HOSCN or hypothiocyanite with
    antibacterial/antifungal terms; exact CAS, FDA, PubChem, ChEBI, HMDB and ChemSpider
    authority routes.
  snapshot_sha256: ede48a6c05b2eae5d6a20ff2b408dfa53d89c4e83a9a2196d25e532f53c261b5
assessments:
- assessment_id: chemical
  area: identity
  topic: Neutral HOSCN constitution and structural parents
  outcome: supported
  summary: Native valid graph, formula, mass and current chemical encodings agree.
    One-carbon sulfur oxoacid classification and structural definition fit.
  target_ids:
  - CHEBI:133907
  evidence_ids:
  - native
  - chemistry
  - terms
- assessment_id: grounding
  area: grounding
  topic: Exact acid versus conjugate-anion name and CAS
  outcome: concern
  summary: The native anion alias/CAS cannot be exact neutral-acid equivalents under
    this repository contract. Current source repetition is preserved as a source conflict;
    acid-base equilibrium does not erase the formal identity distinction.
  target_ids:
  - CHEBI:133907
  evidence_ids:
  - native
  - anion
  - source-conflict
  - equilibrium
  - owners
- assessment_id: activity
  area: scope
  topic: Qualitative antibacterial, antiviral and antifungal roles
  outcome: supported
  summary: Original experiments support these bounded activities in aqueous acid/anion
    and enzyme-generated contexts. Fungal comparator and host/viral scopes are explicit;
    no pure-acid quantitative potency or clinical claim is added.
  target_ids:
  - CHEBI:133907
  evidence_ids:
  - bacterial-primary
  - fungal-primary
  - viral-primary
  - adopted
- assessment_id: mechanism
  area: completeness
  topic: Optional exact primary biochemical detail
  outcome: unknown
  summary: The record makes no target claim. E. coli L-TrxR inhibition is a primary
    enrichment candidate with explicit preparation/assay scope; it is not established
    here as the sole cause of killing across taxa. Host eNOS/GAPDH data remain host
    effects.
  target_ids:
  - CHEBI:133907
  evidence_ids:
  - bacterial-primary
  - adapter
  - adopted
- assessment_id: provenance
  area: provenance
  topic: Complete native source and lead disposition
  outcome: supported
  summary: All thirteen original inputs, exact maintained owners, three history events
    and ten adopted references were checked. Direct-access and indexed-authority limitations
    are stated rather than hidden.
  target_ids:
  - CHEBI:133907
  evidence_ids:
  - owners
  - adopted
  - source-conflict
  - discovery
findings:
- finding_id: F1
  issue_key: hypothiocyanous-acid-anion-cas-and-exact-alias
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Neutral acid is assigned the conjugate-anion CAS and exact alias
  description: The neutral acid CHNOS/key...-N is valid, but cas:63296-34-4 maps independently
    to hypothiocyanite CNOS⁻/key...-M, and Hypothiocyanite is typed EXACT_SYNONYM.
    FDA and CAS-attributed PubChem data distinguish the anion; original kinetic literature
    likewise distinguishes the conjugate forms. ChEBI/HMDB naming conflation does
    not satisfy the repository same-structure xref contract. This is one linked acid/anion
    grounding issue, not a proposed replacement of the native graph.
  target_ids:
  - CHEBI:133907
  field_paths:
  - xrefs[0]
  - synonyms[2]
  evidence_ids:
  - native
  - chemistry
  - anion
  - source-conflict
  - equilibrium
  - owners
  rule_id: 'docs/CURATION.md: an xref is the same structure, not a conjugate acid;
    exact synonym scope'
  normalization_reason: Major wrong grounding; the valid record identity and chemical
    representation remain neutral HOSCN, so no native-structure blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Source-owned exact alias and CAS assertion
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reproducible ChEBI extraction
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Existing source-specific synonym_exclusions and identity policy
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Exact chemical-xref gates and synonym emission
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained grounding decisions where applicable
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - CHEBI:133907
  description: Retain the neutral HOSCN graph. Correct or withhold cas:63296-34-4
    through the maintained ChEBI extraction/grounding lane, recording the FDA/CAS-attributed
    source conflict. Candidate acid CAS64253-39-0 needs direct registry or equivalently
    authoritative exact-form confirmation before adoption. Add a CHEBI:133907-specific
    Hypothiocyanite entry to existing synonym_exclusions, or preserve the name only
    with an explicit non-exact conjugate-base relationship if the native schema supports
    one. Regenerate and reseed; do not globally ban the correct anion name, move the
    CAS into an unrelated drug namespace, or hand-edit the emitted record alone.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Source-owned exact alias and CAS assertion
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reproducible ChEBI extraction
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Existing source-specific synonym_exclusions and identity policy
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Exact chemical-xref gates and synonym emission
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained grounding decisions where applicable
  generator: scripts/extract_source_inventory.py and scripts/seed_from_sources.py
  acceptance_checks:
  - Exact neutral record retains N#CSO, CHNOS, charge 0 and ZCZCOXLLICTZAH-UHFFFAOYSA-N.
  - No exact name/CAS assertion equates it to CNOS⁻/key...-M; source disagreement
    and any approved replacement provenance remain explicit.
  - Any added activity or mechanism keeps aqueous equilibrium, pH, generated-system
    controls, organism and host-versus-microbial scope.
  - Focused schema/strict plus required source/reference/history/corpus and full QC
    pass for eventual native curation.
limitations:
- Direct CAS Common Chemistry API returned 401; CAS attribution was inspected in PubChem
  and independently corroborated by the official FDA substance record. Candidate acid
  CAS64253-39-0 remains a candidate, not a verified direct-registry replacement.
- HMDB direct HTML, XML and structure downloads returned 403. Its indexed official
  neutral structure was read, but the full current entry was not fetched. Reaxys 2958668
  was not independently accessed. ChemSpider direct HTML succeeded although the browser
  route returned 403.
- All ten adopted abstracts were inspected; original kinetic/decomposition and antiviral
  mains returned 403. Their abstract-level support is stated. The bacterial and fungal
  original main passages were read at the declared depth; figures were read through
  captions/text, not independently digitized.
- Published HOSCN preparations here are aqueous equilibria or enzymatic oxidant systems.
  No assay is represented as an isolated neutral-acid measurement solely because the
  article calls its preparation HOSCN. pKa and potency are condition-dependent.
- The fungal thiocyanate comparator is weaker and less durable than hypoiodite. Positive
  results are not transferred from iodide systems or combination formulations, and
  incomplete efficacy is not treated as proof of no antifungal role.
- Host injury papers and the 2013 host-tolerance experiment have different materials
  and conditions; no universal harmlessness or sole bacterial molecular target is
  inferred. No exhaustive absence claim about other targets or later literature is
  made.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native record, maintained source, saved bundle or history was edited. All original
  thirteen input hashes remain unchanged.
- Chemistry used the 019 interpreter against 055; schema, strict, ledger and contract
  use 055. Stable scratch draft is handed to the root finalizer for ordered review
  saving.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
