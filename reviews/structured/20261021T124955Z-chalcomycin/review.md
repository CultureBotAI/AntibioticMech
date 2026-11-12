# Chalcomycin: internally coherent ChEBI structure with incompatible exact chemical cross-references

- Review: 20261021T124955Z-chalcomycin
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T12:36:37Z
- Finished UTC: 2026-10-21T12:49:55Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native ChEBI structure is internally coherent, but its exact PubChem and ChEMBL links encode distinct stereoisomers. This confirmed major cross-reference conflict requires source-level reconciliation; the correct natural-product absolute configuration is not selected here. The producer definition and antibacterial classification have primary support. All three native resistance items correctly declare database-only provenance; inspected primary sources distinguish experimental GimA activity, homology-based ChrB inference and ErmV induction evidence.

## Scope And Provenance

Entire native YAML: identifier, label, antibacterial filing, producer definition and sole DOI, broader macrolide parent/class, complete chemical descriptors and four xrefs, one ARO source concept, all three resistance assertions and all three history events. Actual source rows and extraction, identity selection, resistance assembly and qualification logic were read.

Selection: Queue 285. Thirteen initial input hashes preserved; actual ARO inventory/resistance inventory and CARD qualification loader/overlay appended, giving seventeen inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:80016 | data/antibiotics/antibacterial/chalcomycin.yaml | generated | chalcomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:80016 | No schema issues found. |
| strict | passed | True | CHEBI:80016 | One record scanned; zero strict errors. |
| chemistry | passed | False | CHEBI:80016 | Native SMILES/InChI, descriptors and stable ARO mint agree; run from batch029 with the batch019 RDKit interpreter. |
| external-structure-comparison | passed | False | CHEBI:80016 | Comparison executed successfully and confirmed distinct stereochemical keys; a successful diagnostic is not an identity-equivalence pass. |
| Structured iModulonDB applicability | passed | False | CHEBI:80016 | Catalog retrieved before open-ended web search. No covered dataset matches the source organisms of the three native resistance determinants; no homolog-organism substitution or negative phenotype inference. |
| Authoritative full QC | failed | True | CHEBI:80016 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:80016 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:80016 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:80016 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:80016 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:80016 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:80016 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:80016 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:80016 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Native graph and incompatible exact xrefs

identity: concern. Targets: CHEBI:80016.

The native graph is internally coherent and agrees with current ChEBI. Two linked databases encode different specified stereoisomers; reconcile the exact identity set before treating the seed as scientifically complete. The bounded finding does not choose a natural-product configuration or declare the whole native structure wrong.

### Producer and antibacterial scope

evidence: supported. Targets: CHEBI:80016.

The sole adopted DOI directly supports S. bikiniensis production at complete original abstract depth, and later original work corroborates the producer and antibacterial context. Modern exact-compound isolation supports a bounded S. aureus phenotype. Resolve stereochemical identity before making structure-specific experimental additions.

### Three database assertions and primary depth

evidence: supported. Targets: CHEBI:80016.

Current CARD supports all three native edges. GimA has direct functional evidence in a defined host; ChrB is a sequence-based prediction in the cited source; ErmV sources establish induction context at accessed abstract depth. The native explicit database-only notes are honest and are not silently upgraded.

### Optional exact target, activity and producer objects

completeness: unknown. Targets: CHEBI:80016.

Additional activity and mechanism detail could be curated after exact identity reconciliation. Their optional absence is not a corrective defect. Neither class-level ribosome descriptions, resistance-gene induction nor homolog-based methylation proposals establish exact target engagement. No causal graph is required solely because resistance entries exist.

### Maintained inputs and stable provenance

ownership: supported. Targets: CHEBI:80016.

ARO source mapping and extraction/seeding own the xref conflict. ChEBI owns the selected native structure. CARD evidence-scope qualifications have a maintained overlay path. All seventeen captured input hashes remain unchanged, including all initial captures; SEEDED history remains intact.

## Findings

### F1: Reconcile PubChem and ChEMBL stereoisomers with the selected ChEBI structure

major / open / confirmed; issue key: chalcomycin-specified-stereoisomer-chemical-xrefs.

Native CHEBI:80016 uses KLGADJPDTCIJLO-LJUCOGSUSA-N. xrefs[2] CHEMBL4076923 resolves to KLGADJPDTCIJLO-RVMREVNESA-N, and xrefs[3] PubChem6436271 resolves to KLGADJPDTCIJLO-FCNIXBKESA-N. Independently parsed official SMILES and InChI agree within each database but differ across entries at specified stereocentres. Both external graphs invert the two epoxide centres relative to native, and PubChem also differs at the sugar-bearing macrolactone carbon. ARO imports this mixed set. Correct exact equivalence through the maintained source path; do not select a wholesale structure replacement merely by database majority or sibling crystallography.

## Recommended Actions And Acceptance Checks

### A1

Resolve the conflicting exact chemical mappings through maintained source normalization and regenerate the record.

- Inspect exact chalcomycin primary structural evidence, particularly the 1996 crystallographic article, before deciding whether the selected native structure itself needs revision. The 2017 X-ray experiment is for dihydrochalcomycin and must remain separate.
- Remove or replace incompatible exact xrefs through a reproducible source correction or mapping. Independently compare every retained identifier using full stereochemical graphs, not only formula, connectivity block or name.
- Retain the current native structure unless a separately justified primary identity correction establishes a replacement. Reconcile identifier, source mappings and biological evidence together if that later correction is necessary.
- Regenerate through the owning extraction/seeding path and rerun focused schema/strict, exact chemical comparisons and applicable corpus gates. No native status promotion follows automatically from deterministic passes.

### A2

If adding primary detail after identity resolution, preserve assay and resistance-evidence scope.

- Keep GimA crude-extract glycosylation and host survival distinct from purified-enzyme kinetics; do not assign spiramycin-producer identity as chalcomycin production.
- Keep ChrB G748 methylation and self-resistance as homology-based inference unless an exact functional experiment is inspected. Keep ErmV induction separate from resistance challenge endpoints.
- For any 2017 MIC addition retain exact compound2, strain, medium, incubation, visible-growth endpoint and the unusual reported inoculum, with clarification if needed. Preserve greater-than bounds and do not transfer sibling1/3 results.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/antibiotics/antibacterial/chalcomycin.yaml; Entire YAML, including all source and history entries. | supports | SEEDED, EXACT and ANTIBACTERIAL. Neutral C35H56O14, charge zero, one connected molecular graph, key KLGADJPDTCIJLO-LJUCOGSUSA-N. No native molecular target, numeric activity, clinical assertion, causal graph or transcriptomic dataset is asserted. Three resistance entries explicitly state database assertion rather than primary citation. |
| source | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_resistance_edges.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; conf/sources.yaml; Complete matching rows: ChEBI 2042, ARO 210 and resistance 3869–3871. Source extraction, build_concepts/resolve_identity and attach_aro_mechanism. | supports | ARO:3001222 owns the producer definition, DOI, class, four xrefs and sole source concept. The two-star CHEBI:80016 row is outside adopted role scope but intentionally supplies structure and exact identity to the ARO seed. No independent ChEBI source concept is implied. Resistance rows exactly reproduce gimA, chrB and ErmV with database-only notes. PubChem is an external xref, not the adopted structure source. |
| qualification-owner | curation/card_evidence_reviews.json; scripts/card_evidence_reviews.py; Complete current overlay and loader/apply_review logic. | context_only | No entry qualifies this compound. The existing maintained mechanism can attach narrow evidence-scope notes while preserving CARD assertion ownership, source-row hashes and exact compound binding. Lack of such optional qualification is not itself a native defect. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:80016; Complete visible official entry, structure fields and ontology. | supports | Current ChEBI reproduces the native SMILES, InChI, full key, formula, charge and masses. It is a two-star third-party entry, with macrolide parent CHEBI:25106 and CAS 20283-48-1. CAS is independently attested by current ARO, but the paid CAS registry was not consulted. This database agreement does not settle the conflicting absolute stereochemical representations. |
| aro | https://card.mcmaster.ca/aro/3001222; https://card.mcmaster.ca/aro/0000000; Complete visible compound and class pages. | partial | ARO confirms the adopted producer definition, 1963 DOI, all four xrefs, broader macrolide class and three resistance relations. Its visible SMILES matches the ChEMBL representation rather than native ChEBI at the epoxide stereocentres. The broader parent is a class and not a separate exact molecule. Class-level ribosome wording is not adopted as exact primary target evidence. |
| xref-conflict | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6436271/property/InChI,InChIKey,MolecularFormula,SMILES,IUPACName/JSON; https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL4076923.json; Complete official responses and independent SMILES/InChI parses plus chirality-independent graph mapping. | refutes | PubChem 6436271 yields KLGADJPDTCIJLO-FCNIXBKESA-N and ChEMBL4076923 yields KLGADJPDTCIJLO-RVMREVNESA-N. Both differ from native KLGADJPDTCIJLO-LJUCOGSUSA-N. All have the same connectivity and formula. Mapping finds opposite R/S assignments at native epoxide atoms 12 and 14 in both linked structures; PubChem additionally inverts native atom 25, the sugar-bearing macrolactone carbon. These are specified stereochemical differences, not alternate SMILES traversals or protonation states. No replacement identity is chosen. |
| producer1963 | DOI:10.1139/m63-088; https://www.researchgate.net/publication/237191747_Chalcomycin_a_new_antibiotic_Biological_studies; Complete original abstract displayed on the publication page; title/authors/1963 journal pages/DOI cross-checked against ARO. Publisher route returned 403; full article unavailable. | supports | Coffey and colleagues report obtaining chalcomycin from culture filtrates of two S. bikiniensis strains and antibacterial activity against S. aureus and S. pyogenes. This directly supports the narrow native producer statement and antibacterial filing. The publication page has a later online metadata date; the original bibliographic year is 1963. No exact quantitative assay is imported from abstract-only access. |
| activity2017 | PMID:28555051; DOI:10.3390/md15060153; https://pmc.ncbi.nlm.nih.gov/articles/PMC5484103/; Full main narrative, tables and captions; Figure 1 visually inspected; publisher supplement Materials/Methods, isolation and Table S1 read as PDF text. | partial | Exact chalcomycin is compound 2, isolated as 11.2 mg from cultured Streptomyces sp. HK-2006-1 and identified by NMR comparison. Table 2 gives S. aureus 209P MIC 4 micrograms/mL and values above 512 for E. coli ATCC0111 and both tested fungi. Supplement specifies twofold dilution, beef extract medium, 37 C for 12 h and no visible growth; its stated 1.8e10 CFU/mL inoculum must be retained as reported or clarified, not silently replaced by a standard inoculum. Figure 1 distinguishes exact 2 from dihydro 1 and E 3. Crystallographic analysis is exclusively compound 1, with reported Flack 0.5, and is not proof of exact 2 absolute configuration. |
| stereo-access | DOI:10.1016/S0040-4020(96)00052-X; https://www.sciencedirect.com/science/article/abs/pii/S004040209600052X; Original publisher abstract visible in indexed result; full page request returned 403. | context_only | Woo and Rubin report establishing chalcomycin stereochemistry by single-crystal X-ray analysis. The original detailed drawing, crystallographic model and absolute-assignment reasoning were not available in this review. This is a useful resolution lead, not grounds to choose among the conflicting official structures. |
| resistance-databases | https://card.mcmaster.ca/aro/3000463; https://card.mcmaster.ca/aro/3001302; https://card.mcmaster.ca/aro/3002824; Complete visible determinant definitions, classifications, exact chalcomycin relations and cited publication lists. | supports | Current CARD confirms gimA/inactivation, chrB/target alteration and ErmV/target alteration, including ErmV synonym ermSV. Source organisms are S. ambofaciens, S. bikiniensis and S. viridochromogenes respectively. The native record faithfully represents these as database assertions; reference sequences and predicted protein-family descriptions are not automatically primary experimental results. |
| gimA-primary | PMID:9756764; DOI:10.1128/AAC.42.10.2612; https://pmc.ncbi.nlm.nih.gov/articles/PMC105906/; Abstract, full Methods/Results/Discussion narrative, Table 1 and figure captions; images not visually checked. | supports | The cloned S. ambofaciens gimA was expressed in susceptible S. lividans OS456, compared with empty-vector control. Sigma chalcomycin was inactivated by crude S30 extracts with UDP-glucose, and radiolabel transfer supported glycosylation. Survival assays on HT agar showed a bounded low-level resistance phenotype. These are functional experiments, but not purified-enzyme kinetics or proof that S. ambofaciens produces chalcomycin. Exact tested-material stereochemistry was not re-elucidated. |
| chrB-primary | PMID:15561847; DOI:10.1128/AAC.48.12.4703-4712.2004; https://pmc.ncbi.nlm.nih.gov/articles/PMC529187/; Abstract, Introduction, strain/production Methods, Table 2 chrB row, Resistance genes Results and relevant discussion. Other biosynthetic sections were inspected as context, not complete independent validation of all pathway assignments. | partial | The paper uses S. bikiniensis NRRL2737 as the chalcomycin producer. ChrB is 58 percent identical to TlrB in Table 2; G748 methylation and self-resistance are explicitly inferred from homology, not directly measured in a ChrB experiment. The article distinguishes exact chalcomycin from heterologous-host hybrid products and states that ribosome structural studies cited in its introduction did not include chalcomycin. Do not promote this source to direct ChrB methylation, exact binding-site proof or a chalcomycin causal graph. |
| ermV-primary | PMID:6163765; DOI:10.1128/jb.146.2.621-631.1981; PMID:9055987; DOI:10.1128/aac.41.3.530; Complete original indexed abstracts, cross-checked with official PMC publication pages; original PDF requests returned HTML challenges. | partial | The 1981 paper describes inducible resistance and rRNA methylation in Streptomyces, including an S. viridochromogenes NRRL2860 model. The 1997 experiment compares ermSV and ermC translational attenuator-lac reporter constructs; chalcomycin selectively induces ermSV relative to ermC. Induction is not itself an exact chalcomycin MIC or a direct drug-binding result. Full tables and precise chalcomycin-specific challenge protocols remain uninspected. |
| adapter | 285-imodulondb-datasets.txt; Actual adapter catalog output obtained before open-ended web search. | context_only | The installed adapter provides Streptomyces albidoflavus and coelicolor datasets, but none for the three determinant source species or the S. lividans functional host. Follow-up matching-organism module search is not applicable. This coverage boundary supplies no negative resistance or mechanism evidence. |
| search | 285-inclusive-hits.txt; bounded public chalcomycin exact-name/DOI research; Hidden and ignored files included in local search. Public official databases and original literature at documented depths. | context_only | Relevant exact hits comprise the native record, maintained chemical/resistance rows, readiness queue, PATHS and generated embeddings. No matching curator decision or overlay was found in the stated scope. The broad Europe PMC discovery response returned the first 100 of 150 hits and was used for leads, not an exhaustive literature claim. No paid access or external mutation was used. |
| validation | 285-schema.log; 285-strict.log; 285-strict.tsv; 285-chemistry.json; 285-xref-chemistry.json; 285-xref-stereodiff.json; Actual focused outputs and independent native/external graph parses. | supports | Focused schema and strict commands exit 0. Native encodings reproduce the full key, formula, neutral charge, average mass 700.819 and monoisotopic mass 700.367006472; stable ARO mint recomputes exactly. External comparison succeeds and detects the stereochemical conflict. The first external helper attempt used a wrong native field name and failed; it was corrected to standard_inchi and rerun successfully. Deterministic native checks do not detect cross-database stereochemical disagreement. |

## Limits And Additional Notes

- The original 1963 adopted paper was inspected at complete abstract depth only; the publisher denied full text. The original 1996 exact crystallographic paper was available only as an indexed publisher abstract, so correct absolute stereochemistry among the conflicting source graphs remains unresolved.
- The 2017 full main narrative, tables, Figure1 and supplement Methods/TableS1 were inspected. Supplemental spectral images and the dihydro sibling crystallographic file were not independently reanalyzed. The unusually high stated inoculum limits quantitative portability.
- The 1998 GimA main Methods/Results/Discussion and captions were read, but figure images were not independently verified. The 2004 paper was read in relevant producer/resistance and structural-context sections; no independent validation of its complete biosynthesis proposal is claimed.
- ErmV papers were inspected at complete original abstract depth. PMC PDF requests returned small HTML challenges rather than article PDFs; full induction/challenge tables remain unverified. One initial 1981 retrieval used the wrong PMCID; it was recognized as unrelated and excluded, then corrected to PMC217005.
- The adapter catalog does not cover the relevant Streptomyces species; this is a not-applicable dataset boundary, not evidence against resistance. Paid CAS registry access was not used.
- Scientific completion remains partial. Optional enrichment and unavailable primary text are not automatically defects; the confirmed finding is the exact chemical cross-reference mismatch.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Root read the entire native record and scientific draft, verified all seventeen input hashes, inspected the mapped stereochemical differences, original 2017 Figure 1 and relevant supplement material/assay sections before ordered persistence.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T124955Z-chalcomycin
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Chalcomycin: internally coherent ChEBI structure with incompatible exact chemical
  cross-references'
started_at: '2026-10-21T12:36:37Z'
finished_at: '2026-10-21T12:49:55Z'
reviewer:
  identity: Codex review002 subagent
  kind: agent
  independence: independent
  independence_basis: Did not author the seed. Read the entire native record and maintained
    source rows, inspected official structures and primary literature at the documented
    depths, and independently parsed chemical identities. Initial provenance preceded
    judgment; appended actual owners preserve every original hash.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The native ChEBI structure is internally coherent, but its exact PubChem
  and ChEMBL links encode distinct stereoisomers. This confirmed major cross-reference
  conflict requires source-level reconciliation; the correct natural-product absolute
  configuration is not selected here. The producer definition and antibacterial classification
  have primary support. All three native resistance items correctly declare database-only
  provenance; inspected primary sources distinguish experimental GimA activity, homology-based
  ChrB inference and ErmV induction evidence.
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
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: curation/curator_antibiotics.tsv
    sha256: 224cbb7261add427184b2762a29c2ff3e85c85e0a06cf22b144545346487247b
    role: context
  - path: curation/decisions.tsv
    sha256: a5834b44307b0449b0df9362c551b7fcd707f3ae51f73d429d37d51f5a169d61
    role: context
  - path: data/antibiotics/antibacterial/chalcomycin.yaml
    sha256: fde1fffcdd4830fe0fc3736e6019c14bf0ea9f7ac8c0a237ca67d5bfe3b79015
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 25f0d80c0bf26da7741a1514a5e1759dde484ab054f0f56df7938bdda8383a91
    role: context
  - path: data/raw/aro_antibiotics.tsv
    sha256: d62b642ebad8f678480b1c7ad2c6202b76a232d246705fdd6d292046a91e9801
    role: context
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
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
  - path: scripts/card_evidence_reviews.py
    sha256: f9ec8aff30066bf04b9c2757af7d6f5d179d045e57b9f3b352bbed0b851f50a8
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
- target_id: CHEBI:80016
  path: data/antibiotics/antibacterial/chalcomycin.yaml
  label: chalcomycin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Out-of-role-scope ChEBI structure and exact identity lookup for the ARO
      seed
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO and ChEBI extraction and reproducible source normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated field owner
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Grounding or exclusion override
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted name, producer definition, DOI, class and chemical cross-references
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Three imported CARD resistance relations
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Maintained CARD assertion qualification loader and overlay
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Maintained CARD assertion qualification loader and overlay
scope:
  description: 'Entire native YAML: identifier, label, antibacterial filing, producer
    definition and sole DOI, broader macrolide parent/class, complete chemical descriptors
    and four xrefs, one ARO source concept, all three resistance assertions and all
    three history events. Actual source rows and extraction, identity selection, resistance
    assembly and qualification logic were read.'
  selection: Queue 285. Thirteen initial input hashes preserved; actual ARO inventory/resistance
    inventory and CARD qualification loader/overlay appended, giving seventeen inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:80016
  exclusions:
  - target: Dihydrochalcomycin, chalcomycin E and other macrolides
    reason: Sibling structural, crystallographic, activity and target experiments
      are not exact chalcomycin evidence.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: No schema issues found.
  target_ids:
  - CHEBI:80016
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/chalcomycin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: One record scanned; zero strict errors.
  target_ids:
  - CHEBI:80016
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/chalcomycin.yaml --out /private/tmp/am-review-session/285-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Native SMILES/InChI, descriptors and stable ARO mint agree; run from batch029
    with the batch019 RDKit interpreter.
  target_ids:
  - CHEBI:80016
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 285
  exit_code: 0
  expected_exit_code: 0
- check_id: external-structure-comparison
  name: external-structure-comparison
  status: passed
  required: false
  summary: Comparison executed successfully and confirmed distinct stereochemical
    keys; a successful diagnostic is not an identity-equivalence pass.
  target_ids:
  - CHEBI:80016
  evidence_ids:
  - validation
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/285-xref-check.py
  exit_code: 0
  expected_exit_code: 0
- check_id: adapter
  name: Structured iModulonDB applicability
  status: passed
  required: false
  summary: Catalog retrieved before open-ended web search. No covered dataset matches
    the source organisms of the three native resistance determinants; no homolog-organism
    substitution or negative phenotype inference.
  target_ids:
  - CHEBI:80016
  evidence_ids:
  - adapter
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 datasets
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
  - CHEBI:80016
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
  - CHEBI:80016
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
  - CHEBI:80016
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
  - CHEBI:80016
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
  - CHEBI:80016
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
  - CHEBI:80016
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
  - CHEBI:80016
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
  - CHEBI:80016
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
  - CHEBI:80016
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/antibiotics/antibacterial/chalcomycin.yaml
  locator: Entire YAML, including all source and history entries.
  accessed_at: '2026-10-21T12:46:03Z'
  support: supports
  summary: SEEDED, EXACT and ANTIBACTERIAL. Neutral C35H56O14, charge zero, one connected
    molecular graph, key KLGADJPDTCIJLO-LJUCOGSUSA-N. No native molecular target,
    numeric activity, clinical assertion, causal graph or transcriptomic dataset is
    asserted. Three resistance entries explicitly state database assertion rather
    than primary citation.
- evidence_id: source
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_resistance_edges.tsv;
    scripts/extract_source_inventory.py; scripts/seed_from_sources.py; conf/sources.yaml
  locator: 'Complete matching rows: ChEBI 2042, ARO 210 and resistance 3869–3871.
    Source extraction, build_concepts/resolve_identity and attach_aro_mechanism.'
  accessed_at: '2026-10-21T12:46:03Z'
  support: supports
  summary: ARO:3001222 owns the producer definition, DOI, class, four xrefs and sole
    source concept. The two-star CHEBI:80016 row is outside adopted role scope but
    intentionally supplies structure and exact identity to the ARO seed. No independent
    ChEBI source concept is implied. Resistance rows exactly reproduce gimA, chrB
    and ErmV with database-only notes. PubChem is an external xref, not the adopted
    structure source.
  snapshot_sha256: 46924a1a1dda493ad5659c864abaaf0fc549f3d9e35ddd2da5780bdd26d025e8
- evidence_id: qualification-owner
  kind: record_content
  reference: curation/card_evidence_reviews.json; scripts/card_evidence_reviews.py
  locator: Complete current overlay and loader/apply_review logic.
  accessed_at: '2026-10-21T12:46:03Z'
  support: context_only
  summary: No entry qualifies this compound. The existing maintained mechanism can
    attach narrow evidence-scope notes while preserving CARD assertion ownership,
    source-row hashes and exact compound binding. Lack of such optional qualification
    is not itself a native defect.
- evidence_id: chebi
  kind: database
  reference: https://www.ebi.ac.uk/chebi/CHEBI:80016
  locator: Complete visible official entry, structure fields and ontology.
  accessed_at: '2026-10-21T12:40:34Z'
  support: supports
  summary: Current ChEBI reproduces the native SMILES, InChI, full key, formula, charge
    and masses. It is a two-star third-party entry, with macrolide parent CHEBI:25106
    and CAS 20283-48-1. CAS is independently attested by current ARO, but the paid
    CAS registry was not consulted. This database agreement does not settle the conflicting
    absolute stereochemical representations.
  snapshot_sha256: c7b69c7c3ac35ff4affa13ecca9f7ee0a87e9cd337d744ab471d022ad45b4e56
- evidence_id: aro
  kind: database
  reference: https://card.mcmaster.ca/aro/3001222; https://card.mcmaster.ca/aro/0000000
  locator: Complete visible compound and class pages.
  accessed_at: '2026-10-21T12:40:34Z'
  support: partial
  summary: ARO confirms the adopted producer definition, 1963 DOI, all four xrefs,
    broader macrolide class and three resistance relations. Its visible SMILES matches
    the ChEMBL representation rather than native ChEBI at the epoxide stereocentres.
    The broader parent is a class and not a separate exact molecule. Class-level ribosome
    wording is not adopted as exact primary target evidence.
  snapshot_sha256: 7b9e96e17112fb32ca84bfbe0b8cb1245e7436e89486d82f8272c7478da3506a
- evidence_id: xref-conflict
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6436271/property/InChI,InChIKey,MolecularFormula,SMILES,IUPACName/JSON;
    https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL4076923.json
  locator: Complete official responses and independent SMILES/InChI parses plus chirality-independent
    graph mapping.
  accessed_at: '2026-10-21T12:46:03Z'
  support: refutes
  summary: PubChem 6436271 yields KLGADJPDTCIJLO-FCNIXBKESA-N and ChEMBL4076923 yields
    KLGADJPDTCIJLO-RVMREVNESA-N. Both differ from native KLGADJPDTCIJLO-LJUCOGSUSA-N.
    All have the same connectivity and formula. Mapping finds opposite R/S assignments
    at native epoxide atoms 12 and 14 in both linked structures; PubChem additionally
    inverts native atom 25, the sugar-bearing macrolactone carbon. These are specified
    stereochemical differences, not alternate SMILES traversals or protonation states.
    No replacement identity is chosen.
  snapshot_sha256: 07d840f11bc7e99851ffbeb19323897a4cac6efee024345393a40e7ef0fda235
- evidence_id: producer1963
  kind: primary_source
  reference: DOI:10.1139/m63-088; https://www.researchgate.net/publication/237191747_Chalcomycin_a_new_antibiotic_Biological_studies
  locator: Complete original abstract displayed on the publication page; title/authors/1963
    journal pages/DOI cross-checked against ARO. Publisher route returned 403; full
    article unavailable.
  accessed_at: '2026-10-21T12:46:03Z'
  support: supports
  summary: Coffey and colleagues report obtaining chalcomycin from culture filtrates
    of two S. bikiniensis strains and antibacterial activity against S. aureus and
    S. pyogenes. This directly supports the narrow native producer statement and antibacterial
    filing. The publication page has a later online metadata date; the original bibliographic
    year is 1963. No exact quantitative assay is imported from abstract-only access.
- evidence_id: activity2017
  kind: primary_source
  reference: PMID:28555051; DOI:10.3390/md15060153; https://pmc.ncbi.nlm.nih.gov/articles/PMC5484103/
  locator: Full main narrative, tables and captions; Figure 1 visually inspected;
    publisher supplement Materials/Methods, isolation and Table S1 read as PDF text.
  accessed_at: '2026-10-21T12:42:30Z'
  support: partial
  summary: Exact chalcomycin is compound 2, isolated as 11.2 mg from cultured Streptomyces
    sp. HK-2006-1 and identified by NMR comparison. Table 2 gives S. aureus 209P MIC
    4 micrograms/mL and values above 512 for E. coli ATCC0111 and both tested fungi.
    Supplement specifies twofold dilution, beef extract medium, 37 C for 12 h and
    no visible growth; its stated 1.8e10 CFU/mL inoculum must be retained as reported
    or clarified, not silently replaced by a standard inoculum. Figure 1 distinguishes
    exact 2 from dihydro 1 and E 3. Crystallographic analysis is exclusively compound
    1, with reported Flack 0.5, and is not proof of exact 2 absolute configuration.
  snapshot_sha256: da38fd727d2c571c041be38cd0a89b9cd5a6bca04fb371477cd8da24ae5830cc
- evidence_id: stereo-access
  kind: primary_source
  reference: DOI:10.1016/S0040-4020(96)00052-X; https://www.sciencedirect.com/science/article/abs/pii/S004040209600052X
  locator: Original publisher abstract visible in indexed result; full page request
    returned 403.
  accessed_at: '2026-10-21T12:46:03Z'
  support: context_only
  summary: Woo and Rubin report establishing chalcomycin stereochemistry by single-crystal
    X-ray analysis. The original detailed drawing, crystallographic model and absolute-assignment
    reasoning were not available in this review. This is a useful resolution lead,
    not grounds to choose among the conflicting official structures.
- evidence_id: resistance-databases
  kind: database
  reference: https://card.mcmaster.ca/aro/3000463; https://card.mcmaster.ca/aro/3001302;
    https://card.mcmaster.ca/aro/3002824
  locator: Complete visible determinant definitions, classifications, exact chalcomycin
    relations and cited publication lists.
  accessed_at: '2026-10-21T12:40:35Z'
  support: supports
  summary: Current CARD confirms gimA/inactivation, chrB/target alteration and ErmV/target
    alteration, including ErmV synonym ermSV. Source organisms are S. ambofaciens,
    S. bikiniensis and S. viridochromogenes respectively. The native record faithfully
    represents these as database assertions; reference sequences and predicted protein-family
    descriptions are not automatically primary experimental results.
  snapshot_sha256: 6d7b59f4e724c693e5c50ccffbdc1e8763166928b684cef99d5020e57969e95e
- evidence_id: gimA-primary
  kind: primary_source
  reference: PMID:9756764; DOI:10.1128/AAC.42.10.2612; https://pmc.ncbi.nlm.nih.gov/articles/PMC105906/
  locator: Abstract, full Methods/Results/Discussion narrative, Table 1 and figure
    captions; images not visually checked.
  accessed_at: '2026-10-21T12:43:02Z'
  support: supports
  summary: The cloned S. ambofaciens gimA was expressed in susceptible S. lividans
    OS456, compared with empty-vector control. Sigma chalcomycin was inactivated by
    crude S30 extracts with UDP-glucose, and radiolabel transfer supported glycosylation.
    Survival assays on HT agar showed a bounded low-level resistance phenotype. These
    are functional experiments, but not purified-enzyme kinetics or proof that S.
    ambofaciens produces chalcomycin. Exact tested-material stereochemistry was not
    re-elucidated.
  snapshot_sha256: 36460e9c5fc3deabe308d6cd86aba41ca97a8731c435c7d26127acc6b6e0b576
- evidence_id: chrB-primary
  kind: primary_source
  reference: PMID:15561847; DOI:10.1128/AAC.48.12.4703-4712.2004; https://pmc.ncbi.nlm.nih.gov/articles/PMC529187/
  locator: Abstract, Introduction, strain/production Methods, Table 2 chrB row, Resistance
    genes Results and relevant discussion. Other biosynthetic sections were inspected
    as context, not complete independent validation of all pathway assignments.
  accessed_at: '2026-10-21T12:43:02Z'
  support: partial
  summary: The paper uses S. bikiniensis NRRL2737 as the chalcomycin producer. ChrB
    is 58 percent identical to TlrB in Table 2; G748 methylation and self-resistance
    are explicitly inferred from homology, not directly measured in a ChrB experiment.
    The article distinguishes exact chalcomycin from heterologous-host hybrid products
    and states that ribosome structural studies cited in its introduction did not
    include chalcomycin. Do not promote this source to direct ChrB methylation, exact
    binding-site proof or a chalcomycin causal graph.
  snapshot_sha256: bcf5c8d9c6a80290596b2a791613242047298f640dff287fc2488069fa7c35d9
- evidence_id: ermV-primary
  kind: primary_source
  reference: PMID:6163765; DOI:10.1128/jb.146.2.621-631.1981; PMID:9055987; DOI:10.1128/aac.41.3.530
  locator: Complete original indexed abstracts, cross-checked with official PMC publication
    pages; original PDF requests returned HTML challenges.
  accessed_at: '2026-10-21T12:42:30Z'
  support: partial
  summary: The 1981 paper describes inducible resistance and rRNA methylation in Streptomyces,
    including an S. viridochromogenes NRRL2860 model. The 1997 experiment compares
    ermSV and ermC translational attenuator-lac reporter constructs; chalcomycin selectively
    induces ermSV relative to ermC. Induction is not itself an exact chalcomycin MIC
    or a direct drug-binding result. Full tables and precise chalcomycin-specific
    challenge protocols remain uninspected.
  snapshot_sha256: ca881ed2c611d427ab9940cacb05b71ce10483b57bf64fa49e5fbc31ff70d1bb
- evidence_id: adapter
  kind: database
  reference: 285-imodulondb-datasets.txt
  locator: Actual adapter catalog output obtained before open-ended web search.
  accessed_at: '2026-10-21T12:46:03Z'
  support: context_only
  summary: The installed adapter provides Streptomyces albidoflavus and coelicolor
    datasets, but none for the three determinant source species or the S. lividans
    functional host. Follow-up matching-organism module search is not applicable.
    This coverage boundary supplies no negative resistance or mechanism evidence.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: search
  kind: search
  reference: 285-inclusive-hits.txt; bounded public chalcomycin exact-name/DOI research
  locator: Hidden and ignored files included in local search. Public official databases
    and original literature at documented depths.
  accessed_at: '2026-10-21T12:46:03Z'
  support: context_only
  summary: Relevant exact hits comprise the native record, maintained chemical/resistance
    rows, readiness queue, PATHS and generated embeddings. No matching curator decision
    or overlay was found in the stated scope. The broad Europe PMC discovery response
    returned the first 100 of 150 hits and was used for leads, not an exhaustive literature
    claim. No paid access or external mutation was used.
  snapshot_sha256: a14a024d80943af3c7bbd5d9eec252f819c1b5e4d04e64910ec30d89e26e54ca
  search_scope: rg --no-ignore --hidden -n -F for CHEBI:80016, chalcomycin, KLGADJPDTCIJLO-LJUCOGSUSA-N,
    antibioticmech:aro-6574c1f99e and ARO:3001222 across data, curation, conf, scripts,
    src, docs, .claude, reviews and reports. Exact public title/DOI searches and official
    entry retrieval on 2026-10-21.
- evidence_id: validation
  kind: validation
  reference: 285-schema.log; 285-strict.log; 285-strict.tsv; 285-chemistry.json; 285-xref-chemistry.json;
    285-xref-stereodiff.json
  locator: Actual focused outputs and independent native/external graph parses.
  accessed_at: '2026-10-21T12:46:03Z'
  support: supports
  summary: Focused schema and strict commands exit 0. Native encodings reproduce the
    full key, formula, neutral charge, average mass 700.819 and monoisotopic mass
    700.367006472; stable ARO mint recomputes exactly. External comparison succeeds
    and detects the stereochemical conflict. The first external helper attempt used
    a wrong native field name and failed; it was corrected to standard_inchi and rerun
    successfully. Deterministic native checks do not detect cross-database stereochemical
    disagreement.
  snapshot_sha256: 98c737b08dc84c225414ee1dea7fc4eb278847a87f6f2fe47e673ca62d39b26b
assessments:
- assessment_id: identity
  area: identity
  topic: Native graph and incompatible exact xrefs
  outcome: concern
  summary: The native graph is internally coherent and agrees with current ChEBI.
    Two linked databases encode different specified stereoisomers; reconcile the exact
    identity set before treating the seed as scientifically complete. The bounded
    finding does not choose a natural-product configuration or declare the whole native
    structure wrong.
  target_ids:
  - CHEBI:80016
  evidence_ids:
  - record
  - source
  - chebi
  - aro
  - xref-conflict
  - stereo-access
  - validation
- assessment_id: definition
  area: evidence
  topic: Producer and antibacterial scope
  outcome: supported
  summary: The sole adopted DOI directly supports S. bikiniensis production at complete
    original abstract depth, and later original work corroborates the producer and
    antibacterial context. Modern exact-compound isolation supports a bounded S. aureus
    phenotype. Resolve stereochemical identity before making structure-specific experimental
    additions.
  target_ids:
  - CHEBI:80016
  evidence_ids:
  - producer1963
  - activity2017
  - chrB-primary
- assessment_id: resistance
  area: evidence
  topic: Three database assertions and primary depth
  outcome: supported
  summary: Current CARD supports all three native edges. GimA has direct functional
    evidence in a defined host; ChrB is a sequence-based prediction in the cited source;
    ErmV sources establish induction context at accessed abstract depth. The native
    explicit database-only notes are honest and are not silently upgraded.
  target_ids:
  - CHEBI:80016
  evidence_ids:
  - resistance-databases
  - gimA-primary
  - chrB-primary
  - ermV-primary
- assessment_id: completeness
  area: completeness
  topic: Optional exact target, activity and producer objects
  outcome: unknown
  summary: Additional activity and mechanism detail could be curated after exact identity
    reconciliation. Their optional absence is not a corrective defect. Neither class-level
    ribosome descriptions, resistance-gene induction nor homolog-based methylation
    proposals establish exact target engagement. No causal graph is required solely
    because resistance entries exist.
  target_ids:
  - CHEBI:80016
  evidence_ids:
  - record
  - activity2017
  - chrB-primary
  - ermV-primary
- assessment_id: ownership
  area: ownership
  topic: Maintained inputs and stable provenance
  outcome: supported
  summary: ARO source mapping and extraction/seeding own the xref conflict. ChEBI
    owns the selected native structure. CARD evidence-scope qualifications have a
    maintained overlay path. All seventeen captured input hashes remain unchanged,
    including all initial captures; SEEDED history remains intact.
  target_ids:
  - CHEBI:80016
  evidence_ids:
  - source
  - qualification-owner
  - search
  - validation
findings:
- finding_id: F1
  issue_key: chalcomycin-specified-stereoisomer-chemical-xrefs
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile PubChem and ChEMBL stereoisomers with the selected ChEBI structure
  description: Native CHEBI:80016 uses KLGADJPDTCIJLO-LJUCOGSUSA-N. xrefs[2] CHEMBL4076923
    resolves to KLGADJPDTCIJLO-RVMREVNESA-N, and xrefs[3] PubChem6436271 resolves
    to KLGADJPDTCIJLO-FCNIXBKESA-N. Independently parsed official SMILES and InChI
    agree within each database but differ across entries at specified stereocentres.
    Both external graphs invert the two epoxide centres relative to native, and PubChem
    also differs at the sugar-bearing macrolactone carbon. ARO imports this mixed
    set. Correct exact equivalence through the maintained source path; do not select
    a wholesale structure replacement merely by database majority or sibling crystallography.
  target_ids:
  - CHEBI:80016
  field_paths:
  - xrefs[2]
  - xrefs[3]
  evidence_ids:
  - source
  - chebi
  - aro
  - xref-conflict
  - stereo-access
  - validation
  rule_id: 'docs/CURATION.md: every chemical xref denotes the same structure; native-review-checklist:
    Equivalence'
  native_severity: major
  normalization_reason: Confirmed stereoisomer links can misjoin chemical and biological
    evidence. Native identity is internally coherent, so the bounded defect is major
    exact-cross-reference inconsistency rather than a proven blocker requiring full
    structure replacement.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Imported mixed exact chemical cross-reference assertion
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reproducible upstream normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Exact identity selection and chemical xref reconciliation
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Selected structure owner if primary evidence ultimately warrants revision
actions:
- action_id: A1
  description: Resolve the conflicting exact chemical mappings through maintained
    source normalization and regenerate the record.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:80016
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Imported mixed exact chemical cross-reference assertion
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reproducible upstream normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Exact identity selection and chemical xref reconciliation
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Selected structure owner if primary evidence ultimately warrants revision
  acceptance_checks:
  - Inspect exact chalcomycin primary structural evidence, particularly the 1996 crystallographic
    article, before deciding whether the selected native structure itself needs revision.
    The 2017 X-ray experiment is for dihydrochalcomycin and must remain separate.
  - Remove or replace incompatible exact xrefs through a reproducible source correction
    or mapping. Independently compare every retained identifier using full stereochemical
    graphs, not only formula, connectivity block or name.
  - Retain the current native structure unless a separately justified primary identity
    correction establishes a replacement. Reconcile identifier, source mappings and
    biological evidence together if that later correction is necessary.
  - Regenerate through the owning extraction/seeding path and rerun focused schema/strict,
    exact chemical comparisons and applicable corpus gates. No native status promotion
    follows automatically from deterministic passes.
- action_id: A2
  description: If adding primary detail after identity resolution, preserve assay
    and resistance-evidence scope.
  finding_ids: []
  target_ids:
  - CHEBI:80016
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/chalcomycin.yaml
    role: Curator-owned exact primary activity, producer and mechanism additions
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Optional bounded CARD evidence-scope qualification
  acceptance_checks:
  - Keep GimA crude-extract glycosylation and host survival distinct from purified-enzyme
    kinetics; do not assign spiramycin-producer identity as chalcomycin production.
  - Keep ChrB G748 methylation and self-resistance as homology-based inference unless
    an exact functional experiment is inspected. Keep ErmV induction separate from
    resistance challenge endpoints.
  - For any 2017 MIC addition retain exact compound2, strain, medium, incubation,
    visible-growth endpoint and the unusual reported inoculum, with clarification
    if needed. Preserve greater-than bounds and do not transfer sibling1/3 results.
limitations:
- The original 1963 adopted paper was inspected at complete abstract depth only; the
  publisher denied full text. The original 1996 exact crystallographic paper was available
  only as an indexed publisher abstract, so correct absolute stereochemistry among
  the conflicting source graphs remains unresolved.
- The 2017 full main narrative, tables, Figure1 and supplement Methods/TableS1 were
  inspected. Supplemental spectral images and the dihydro sibling crystallographic
  file were not independently reanalyzed. The unusually high stated inoculum limits
  quantitative portability.
- The 1998 GimA main Methods/Results/Discussion and captions were read, but figure
  images were not independently verified. The 2004 paper was read in relevant producer/resistance
  and structural-context sections; no independent validation of its complete biosynthesis
  proposal is claimed.
- ErmV papers were inspected at complete original abstract depth. PMC PDF requests
  returned small HTML challenges rather than article PDFs; full induction/challenge
  tables remain unverified. One initial 1981 retrieval used the wrong PMCID; it was
  recognized as unrelated and excluded, then corrected to PMC217005.
- The adapter catalog does not cover the relevant Streptomyces species; this is a
  not-applicable dataset boundary, not evidence against resistance. Paid CAS registry
  access was not used.
- Scientific completion remains partial. Optional enrichment and unavailable primary
  text are not automatically defects; the confirmed finding is the exact chemical
  cross-reference mismatch.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Root read the entire native record and scientific draft, verified all seventeen
  input hashes, inspected the mapped stereochemical differences, original 2017 Figure
  1 and relevant supplement material/assay sections before ordered persistence.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
