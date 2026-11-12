# Dalfopristin: supported ribosome mechanism with an exact KEGG stereochemistry conflict

- Review: 20261021T141519Z-dalfopristin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T14:02:21Z
- Finished UTC: 2026-10-21T14:15:19Z
- Reviewer: Codex review002 subagent (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native dalfopristin graph and its curated ribosome mechanism are supported. One major finding concerns a current KEGG COMPOUND exact cross-reference whose molfile encodes the opposite ring-junction configuration. An informational item records the boundary between the faithfully imported CARD ErmB assertion and controlled, context-dependent primary results. Combination treatment, component activity and resistance-enzyme binding remain distinct.

## Scope And Provenance

Entire native record: seven synonyms, definition, twelve parent terms, two roles, structural class, complete chemical representation, seven exact xrefs, three drug links and document link, two source concepts, two primary citations, thirty CARD resistance assertions, both molecular targets, mechanism/scope notes and all history events. All eleven distinct adopted publication leads resolved and disposed at the documented depth.

Selection: Queue 341; the original thirteen captured inputs were verified and preserved before judgment. Six actual ARO and overlay owners were appended, for nineteen inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:4309 | data/antibiotics/antibacterial/dalfopristin.yaml | generated | dalfopristin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CHEBI:4309 | Actual focused native schema validation found no issues. |
| strict | passed | True | CHEBI:4309 | Actual strict validation scanned one file with zero errors. |
| chemistry | passed | False | CHEBI:4309 | Native SMILES and InChI reproduce the stored full key, formula, charge, mass and source mint; all five tetrahedral centres are assigned. |
| external-chemistry | failed | False | CHEBI:4309 | The scratch comparison deliberately asserted equality across all descriptors and exited 1. Its retained output distinguishes expected nonstereochemical DOL descriptors from the substantive KEGG epimer and DrugCentral connectivity differences. This is not a native schema/structure failure or a blanket identity pass. |
| stereo-localization | passed | False | CHEBI:4309 | Independent connectivity mapping localizes the KEGG difference to native atom 0 at the carbonyl-adjacent ring junction: S versus KEGG R. The four other assigned centres agree. |
| Authoritative full QC | failed | True | CHEBI:4309 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:4309 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:4309 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:4309 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:4309 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:4309 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:4309 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:4309 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:4309 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Native exact structure and external equivalence scope

identity: concern. Targets: CHEBI:4309.

The native graph, names and stereochemistry agree with ChEBI, PubChem, ChEMBL and the structural ligand authority. The exact KEGG COMPOUND link encodes an epimer and requires a maintained-source correction or qualification. Drug-level source structure conflicts are explicitly separated.

### Primary ribosome target, enzyme context and mechanism scope

evidence: supported. Targets: CHEBI:4309.

The curated D. radiodurans complex supports direct binding at the 50S peptidyl-transferase centre with the stated combined-drug context. VatD is an inactivating resistance enzyme. The CARD 23S-rRNA target remains honestly evidence-needed; adding the existing primary citation there could improve linkage but its absence is not a confirmed false claim. HOST_SHARED_TARGET is appropriate to the schema meaning.

### Thirty qualified database assertions and controlled ErmB scope

evidence: concern. Targets: CHEBI:4309.

Every imported edge matches the inspected official ontology and is expressly database-qualified. The controlled ErmB study makes a simple single-gene/component interpretation unsafe, while combination constructs demonstrate context effects. Preserve this evidence conflict and resolve it in the maintained qualification layer before functional promotion; do not delete all Erm-family edges by analogy.

### Antibacterial activity, clinical combination prose and adopted leads

evidence: supported. Targets: CHEBI:4309.

The exact semisynthetic component is an antibacterial ribosomal inhibitor; the additional controlled paper measures dalfopristin separately. Native definition explicitly says use in a mixture with quinupristin and does not claim stand-alone VRE efficacy. Combination MICs, parasite effects, clinical case outcomes and quinupristin-specific enzymology are not silently transferred.

### Maintained sources, identifiers, historic REVIEWED status and optional fields

provenance: supported. Targets: CHEBI:4309.

Actual ARO owners and curator-owned target/notes were captured before judgment. Native REVIEWED is a historical event, not automatic validation of every current xref or imported resistance relationship. No optional absent spectrum, producer, causal graph or clinical summary is a corrective defect.

## Findings

### F1: The exact KEGG COMPOUND cross-reference encodes a ring-junction epimer

major / open / confirmed; issue key: dalfopristin-kegg-exact-xref-ring-junction-epimer.

Native xrefs includes kegg.compound:C08033 as a same-structure identity. Its current official molfile has full key SUYRLXYYZQTJHF-PSUTZUHDSA-N and a 26aR ring junction, whereas the native, ChEBI, PubChem, ChEMBL and stereochemical RCSB DOL encodings have SUYRLXYYZQTJHF-VMBLUXKRSA-N and 26aS. Independent graph mapping finds identical connectivity and four matching other centres. Qualify or withhold the exact equivalence until reconciled; do not overwrite the supported native structure from the conflicting KEGG graph. The already drug-level D00853 link is not an additional exact-equivalence claim.

### F2: Retain the controlled ErmB context alongside the qualified database edge

informational / open / confirmed; issue key: dalfopristin-ermb-database-primary-context-reconciliation.

The imported ErmB edge faithfully states a CARD assertion and does not claim primary demonstration. In the inspected controlled study, ermB alone did not increase dalfopristin MIC in two susceptible backgrounds, whereas combinations with satA did. This evidence boundary merits an explicit maintained source-qualification follow-up, not an unqualified causal promotion, universal absence claim or automatic deletion of every Erm-family relation.

## Recommended Actions And Acceptance Checks

### A1

Reconcile the KEGG stereochemical discrepancy in maintained exact-xref handling.

- Retain current KEGG molfile/drawing and independent atom mapping; compare all five centres and full stereochemical keys rather than connectivity-only keys.
- Withhold or explicitly qualify C08033 exact equivalence until the authority encoding is corrected or resolved. Preserve the supported native graph and existing drug-level D00853 context.
- Regenerate through the maintained owner and rerun schema, strict and exact-structure equivalence checks.

### A2

Resolve the bounded ErmB component/context question through the existing source-evidence qualification layer.

- Preserve that CARD explicitly supplies the relation and that the native entry is database-qualified. Capture the controlled vector, ermB-alone and combined-construct outcomes separately.
- Check exact alleles, host backgrounds, expression/induction and tested material before any functional claim. Do not equate combination-drug resistance with dalfopristin-alone resistance, or extrapolate this experiment to all Erm proteins.
- If authorized, add an evidence qualification or primary observation with exact assay context; do not turn a conditional contribution into a universal negative or positive assertion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/dalfopristin.yaml; Entire YAML, including all thirty resistance entries and both differently qualified molecular targets. | supports | CHEBI:4309 is REVIEWED, EXACT and ANTIBACTERIAL. Its neutral C34H50N4O9S graph has key SUYRLXYYZQTJHF-VMBLUXKRSA-N. The curator-owned primary target is the D. radiodurans 50S peptidyl-transferase centre, supported by PMID15059283; the taxon-agnostic CARD 23S-rRNA entry remains PRIMARY_EVIDENCE_NEEDED. Each resistance entry expressly labels itself a database assertion, not primary evidence. No quantitative activity or present clinical-status field is asserted. |
| owners | data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv; data/raw/aro_resistance_edges.tsv; conf/aro_target_roles.tsv; scripts/extract_source_inventory.py; scripts/seed_from_sources.py; Complete exact source rows: ChEBI131, ARO172, target190, resistance3518–3547; relevant extraction/seeding, target-map and preservation code. | supports | The maintained rows reproduce identity, source version, class, roles, aliases and thirty direct confers_resistance_to_antibiotic relations. The extractor does not manufacture those drug-specific edges by drug-class expansion. The target map assigns a nucleic-acid direct-binding relation to ARO3000754; the seeder retains its evidence-needed qualification. Curator primary targets and mechanism notes survive reseeding. No exact dalfopristin overlay occurs in the inspected card_evidence_reviews.json; the generic overlay machinery is an available future owner. |
| identity | CHEBI:4309; PubChem:6323289; CHEMBL1200937; PDB-CCD:DOL; CAS:112362-50-2; Complete official chemical entries/descriptors; native and external SMILES/InChI independently parsed. | supports | ChEBI, PubChem, ChEMBL and the stereochemical RCSB DOL encodings agree with the native full key, formula and five centres. DOL also supplies nonstereochemical descriptor variants; their unassigned stereo keys are expected descriptor scope and not chemical disagreement. ChEBI confirms the seven native names, including the 26aS systematic name and RP54476/INN variants, and CAS112362-50-2. The semisynthetic single component is distinct from its combination product. |
| classification | CHEBI:140325; CHEBI:140326; CHEBI:25105; CHEBI:25106; CHEBI:33308; CHEBI:35681; CHEBI:35850; CHEBI:3992; CHEBI:46812; CHEBI:50996; CHEBI:51751; CHEBI:33281; CHEBI:36047; ARO:0000026; Official term names/definitions and exact-entry relations, with independent graph functional-group inspection. | supports | The secondary and tertiary amides, ester/lactone, ketone, secondary alcohol, sulfone, oxazole, tertiary amine and enamide features are present. The macrolide and streptogramin classifications are broader structural classes, not a claim that dalfopristin is a macrolide-class target-site equivalent. Both antibacterial-drug and antimicrobial roles are explicit. Native HOST_SHARED_TARGET is consistent with the schema definition for microbial-selective drugs acting on conserved machinery; it does not assert direct binding to a named human protein. |
| kegg-conflict | https://rest.kegg.jp/get/C08033/mol; https://rest.kegg.jp/get/D00853/mol; https://www.genome.jp/Fig/compound/C08033.gif; Current official KEGG molfiles independently parsed and mapped; C08033 displayed structural drawing visually inspected. | refutes | Both KEGG encodings give SUYRLXYYZQTJHF-PSUTZUHDSA-N rather than native SUYRLXYYZQTJHF-VMBLUXKRSA-N. Connectivity is identical, but the carbonyl-adjacent five-membered-ring junction corresponding to native atom 0 is R in KEGG and S in the native graph; all four other assigned centres agree. This is the 26a junction, not missing stereo or a salt difference. C08033 is exported as an exact xref. D00853 is already a drug-level link, so its conflicting structure is source context rather than a second exact-xref defect. |
| drug-links | DrugBank:DB01764; DrugCentral:778; KEGG:D00853; wikipedia.en:Dalfopristin; Public DrugBank page via web, complete DrugCentral page and SMILES endpoint, complete KEGG drug entry; Wikipedia topic resolution. | context_only | The public DrugBank page names dalfopristin, RP54476, the native CAS and full key; its visible stereochemical SMILES agrees by inspection with the matched identity. DrugCentral names the correct drug/CAS but its downloadable SMILES gives a different pyrrolidine connectivity, KLRSZNOYZIOTBR-VLAQKBCTSA-N. Do not import that graph. These links are typed drug_xrefs, whose contract permits drug-level aggregation; their predictions, formulations and approval summaries are not native chemical or clinical claims. Wikipedia is correctly a topic link. |
| card | https://raw.githubusercontent.com/arpcard/aro/master/src/ontology/aro.obo; Official current ARO file header dated 2026-08-11; all 33 relevant term blocks and their exact dalfopristin relations examined. | supports | All thirty native resistance identifiers resolve to the expected labels and have an explicit dalfopristin resistance relation in this ontology. The class, compound and 23S-rRNA target blocks also resolve. These checks establish faithful database provenance and type mapping, not thirty independent functional demonstrations. The current ontology still contains broad Erm-to-dalfopristin links; the controlled experiment below exposes a context boundary requiring preservation. Thirty-three individual CARD page requests timed out; the official downloadable ontology supplies the actual inspected authority instead. |
| ribosome | PMID:15059283; DOI:10.1186/1741-7007-2-4; PMC400760; PDB:1SM1; Entire original main text and Table 1 read; Figure 2 on PDF page 4 visually inspected; RCSB experiment/citation metadata independently read. | supports | The 3.42 Å D. radiodurans 50S structure uses fourfold dalfopristin and tenfold quinupristin during co-crystallization. Density supports dalfopristin at the peptidyl-transferase centre and overlapping A/P substrate positions; quinupristin occupies the adjacent tunnel region. The proposed rRNA rearrangement and synergistic functional interpretation are supported structurally but are not a newly measured whole-cell killing endpoint or affinity constant. The native wording preserves the combined-drug structural context. NCBI taxonomy independently confirms taxon1299 as D. radiodurans. |
| vatd | PMID:12771141; DOI:10.1074/jbc.M303766200; PDB:1MRL; Complete original indexed abstract and official PDB entry metadata; publisher PDF/fulltext returned 403. | supports | The original abstract reports VatD structures with dalfopristin at 2.8 Å and supports O18 acetylation and catalytic analysis. PDB1MRL independently identifies the dalfopristin acetyltransferase complex and correct original citation. This supports the native cocrystal note and distinguishes a resistance enzyme that modifies the drug from the lethal ribosomal target. Full assay methods, tables and kinetic numbers were not inspected or imported. |
| ermB-experiment | PMID:10543753; DOI:10.1128/AAC.43.11.2720; PMC89549; Entire original main HTML including Methods, Results, Discussion and Tables 1–3 read; Figure 1 caption read, plot not independently reprocessed. | context_only | Agar dilution on Mueller-Hinton medium and defined pJIM2246 constructs separate single components from the combination. In E. faecium HM1070 and S. aureus RN4220, ermB alone leaves dalfopristin MIC at 1 microgram/mL versus vector while increasing quinupristin MIC. In the same backgrounds, ermB plus satA raises dalfopristin MIC above satA alone. Thus the experiment does not establish a simple, context-free ErmB-only dalfopristin resistance effect, but it also does not prove that ErmB can never contribute to a combined resistance phenotype. Exact reagent counterion/purity is not established in the inspected methods. |
| adopted | PMID:23924572; PMID:23044949; PMID:21453475; PMID:19409762; PMID:18056275; PMID:17563376; PMID:15700955; PMID:15059283; PMID:12771141; PMID:11985218; PMID:1328138; All eleven adopted indexed records resolved; all six available abstracts read completely; five entries lack abstracts. Main full text additionally read for15059283. | context_only | 23924572 is a combination-resistance letter without an abstract.23044949 is an endophthalmitis case without an abstract.21453475 describes intravitreal combination treatment in one postoperative S. aureus case, not dalfopristin-alone efficacy.19409762 is a combination-breakpoint comment without an abstract.18056275 studies combination effects on malaria parasites; do not transfer an exact-component antimalarial role.17563376 concerns Vgb and quinupristin, not dalfopristin/VatD.15700955 and11985218 are reviews without indexed abstracts, not primary support.15059283 and12771141 are separately assessed above.1328138 compares individual RP54476/RP57669 and RP59500, but numerical activity statements in its inspected abstract concern the combination; those are not single-agent MICs. |
| adapter | Structured iModulonDB adapter; Dataset catalog and S. aureus erm/vga plus M. tuberculosis erm searches executed before web follow-up. | context_only | D. radiodurans and Enterococcus are outside the inspected catalog. The S. aureus erm search returned only unrelated substring matches such as permease/spermidine genes and no module; vga returned no genes or modules. The M. tuberculosis search exited 2 because an upstream module regulator was null instead of a JSON list. No expression result or failed adapter call is used as evidence against resistance or direct binding. |
| search | 341-inclusive-hits.txt;341-overlay-hits.txt; Exact-label/identifier/key search including hidden and ignored files; bounded official structures and original-literature follow-up. | context_only | The exact native, maintained source rows and qualified target map were found. No exact dalfopristin card-evidence overlay was found in the actual JSON owner, with ignored files included. All adopted citations are disposed explicitly. The search was bounded rather than an exhaustive survey of every current ChEBI citation or all thirty determinant primary literatures. |
| validation | 341-schema.log;341-strict.log;341-chemistry.json;341-xref-chemistry.json;341-stereo-map.json; Actual focused executions and input hash recheck. | supports | Schema, strict and native chemistry checks exit 0. The external comparison exits 1 and preserves the source differences; the independent localization script exits0. Early ad-hoc ontology reader attempts failed on missing Python packages and a wrong guessed native key; the corrected reader used the actual aro_id key and selected all 33 blocks. No native-data failure is inferred from those scratch-reader mistakes. All nineteen input hashes remain unchanged. |

## Limits And Additional Notes

- HMDB0015566 returned 403 on direct, www and web attempts; its native identifier is confirmed only as the adopted/current ChEBI attestation, not an independently inspected HMDB structure. DrugBank was readable through public web but its direct download returned 403.
- The 2004 ribosome paper was read in full and Figure 2 visually inspected; raw diffraction data and all other figures were not independently reprocessed. Its introduction appears to reverse the component order in one 30:70 sentence; the record contains no ratio, and the controlled 1999 paper correctly specifies quinupristin:dalfopristin 30:70. No new numerical combination claim is adopted.
- The VatD paper was read at complete indexed-abstract depth plus independent PDB metadata, with publisher full text/PDF 403. This supports the narrow cocrystal claim but is not a complete kinetic or mutant-method audit.
- All eleven adopted leads were resolved; six complete abstracts were available and read, five had no abstracts. Except for the 2004 ribosome paper, their full texts were not claimed read. Later current ChEBI leads were not exhaustively reviewed.
- The official ARO ontology validates all thirty exported database relations, but their individual original experimental literatures were not exhaustively read. The extra 1999 controlled study was read completely; its material lacks a separately verified counterion/purity certificate. Figure 1 was not independently quantified.
- The M. tuberculosis structured adapter failed schema parsing on a null regulator field. Successful S. aureus queries returned no relevant module; neither outcome is evidence against biological function.
- DrugCentral778 currently supplies a constitutional-isomer SMILES despite correct drug name/CAS. Keep this source-quality discrepancy visible and do not import that graph. The native drug_xrefs typing does not assert same-structure equivalence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- No native status promotion or curation change is made by this review. Optional enrichment is separate from established corrective findings.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T141519Z-dalfopristin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: 'Dalfopristin: supported ribosome mechanism with an exact KEGG stereochemistry
  conflict'
started_at: '2026-10-21T14:02:21Z'
finished_at: '2026-10-21T14:15:19Z'
reviewer:
  identity: Codex review002 subagent
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
summary: The native dalfopristin graph and its curated ribosome mechanism are supported.
  One major finding concerns a current KEGG COMPOUND exact cross-reference whose molfile
  encodes the opposite ring-junction configuration. An informational item records
  the boundary between the faithfully imported CARD ErmB assertion and controlled,
  context-dependent primary results. Combination treatment, component activity and
  resistance-enzyme binding remain distinct.
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
  - path: data/antibiotics/antibacterial/dalfopristin.yaml
    sha256: 8b9ccad82274b5dd01563bba31e463940b3d61150d51e711ed24bfac81aebdd8
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
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: context
  - path: data/raw/aro_resistance_edges.tsv
    sha256: 5ba15ad08023b89647f964693871fe50e437cfca6654aadcb629d1512f1852df
    role: context
  - path: conf/aro_target_roles.tsv
    sha256: 8cfb773d8cd86aacfd9dab5feba688427f140a571553b460940c901facb81167
    role: context
  - path: curation/card_evidence_reviews.json
    sha256: 584f3e32ce0122eb2315fe09bbe22e058539bef184ad2d75756a6f3016bf2687
    role: context
  - path: scripts/card_evidence_reviews.py
    sha256: f9ec8aff30066bf04b9c2757af7d6f5d179d045e57b9f3b352bbed0b851f50a8
    role: context
targets:
- target_id: CHEBI:4309
  path: data/antibiotics/antibacterial/dalfopristin.yaml
  label: dalfopristin
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
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Adopted ARO identity and class
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Imported CARD target edges
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Imported CARD resistance edges
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/dalfopristin.yaml
    role: Curator-owned primary literature target, mechanism notes, scope and REVIEWED
      history
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Maintained target relation and type map
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Maintained CARD evidence-qualification overlay
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Overlay application and integrity checks
scope:
  description: 'Entire native record: seven synonyms, definition, twelve parent terms,
    two roles, structural class, complete chemical representation, seven exact xrefs,
    three drug links and document link, two source concepts, two primary citations,
    thirty CARD resistance assertions, both molecular targets, mechanism/scope notes
    and all history events. All eleven distinct adopted publication leads resolved
    and disposed at the documented depth.'
  selection: Queue 341; the original thirteen captured inputs were verified and preserved
    before judgment. Six actual ARO and overlay owners were appended, for nineteen
    inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:4309
  exclusions:
  - target: Quinupristin and the quinupristin/dalfopristin combination
    reason: Adjacent component and combination evidence are relevant context but are
      not automatically single-agent dalfopristin observations. No combination clinical
      status, MIC or organism spectrum is transferred.
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Actual focused native schema validation found no issues.
  target_ids:
  - CHEBI:4309
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/dalfopristin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Actual strict validation scanned one file with zero errors.
  target_ids:
  - CHEBI:4309
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/dalfopristin.yaml --out /private/tmp/am-review-session/341-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: chemistry
  name: chemistry
  status: passed
  required: false
  summary: Native SMILES and InChI reproduce the stored full key, formula, charge,
    mass and source mint; all five tetrahedral centres are assigned.
  target_ids:
  - CHEBI:4309
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/111-chemistry-check.py 341
  exit_code: 0
  expected_exit_code: 0
- check_id: external-chemistry
  name: external-chemistry
  status: failed
  required: false
  summary: The scratch comparison deliberately asserted equality across all descriptors
    and exited 1. Its retained output distinguishes expected nonstereochemical DOL
    descriptors from the substantive KEGG epimer and DrugCentral connectivity differences.
    This is not a native schema/structure failure or a blanket identity pass.
  target_ids:
  - CHEBI:4309
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/341-xref-check.py
  exit_code: 1
  expected_exit_code: 0
- check_id: stereo-localization
  name: stereo-localization
  status: passed
  required: false
  summary: 'Independent connectivity mapping localizes the KEGG difference to native
    atom 0 at the carbonyl-adjacent ring junction: S versus KEGG R. The four other
    assigned centres agree.'
  target_ids:
  - CHEBI:4309
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python
    /private/tmp/am-review-session/341-stereo-map.py
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
  - CHEBI:4309
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
  - CHEBI:4309
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
  - CHEBI:4309
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
  - CHEBI:4309
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
  - CHEBI:4309
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
  - CHEBI:4309
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
  - CHEBI:4309
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
  - CHEBI:4309
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
  - CHEBI:4309
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/dalfopristin.yaml
  locator: Entire YAML, including all thirty resistance entries and both differently
    qualified molecular targets.
  accessed_at: '2026-10-21T14:13:49Z'
  support: supports
  summary: CHEBI:4309 is REVIEWED, EXACT and ANTIBACTERIAL. Its neutral C34H50N4O9S
    graph has key SUYRLXYYZQTJHF-VMBLUXKRSA-N. The curator-owned primary target is
    the D. radiodurans 50S peptidyl-transferase centre, supported by PMID15059283;
    the taxon-agnostic CARD 23S-rRNA entry remains PRIMARY_EVIDENCE_NEEDED. Each resistance
    entry expressly labels itself a database assertion, not primary evidence. No quantitative
    activity or present clinical-status field is asserted.
- evidence_id: owners
  kind: record_content
  reference: data/raw/chebi_antimicrobials.tsv; data/raw/aro_antibiotics.tsv; data/raw/aro_target_edges.tsv;
    data/raw/aro_resistance_edges.tsv; conf/aro_target_roles.tsv; scripts/extract_source_inventory.py;
    scripts/seed_from_sources.py
  locator: 'Complete exact source rows: ChEBI131, ARO172, target190, resistance3518–3547;
    relevant extraction/seeding, target-map and preservation code.'
  accessed_at: '2026-10-21T14:13:49Z'
  support: supports
  summary: The maintained rows reproduce identity, source version, class, roles, aliases
    and thirty direct confers_resistance_to_antibiotic relations. The extractor does
    not manufacture those drug-specific edges by drug-class expansion. The target
    map assigns a nucleic-acid direct-binding relation to ARO3000754; the seeder retains
    its evidence-needed qualification. Curator primary targets and mechanism notes
    survive reseeding. No exact dalfopristin overlay occurs in the inspected card_evidence_reviews.json;
    the generic overlay machinery is an available future owner.
  snapshot_sha256: 9f87b0fa6cde91a044ecfd4a942231caca5dff57f93b21e90a79b18d9845535b
- evidence_id: identity
  kind: authority
  reference: CHEBI:4309; PubChem:6323289; CHEMBL1200937; PDB-CCD:DOL; CAS:112362-50-2
  locator: Complete official chemical entries/descriptors; native and external SMILES/InChI
    independently parsed.
  accessed_at: '2026-10-21T14:04:41Z'
  support: supports
  summary: ChEBI, PubChem, ChEMBL and the stereochemical RCSB DOL encodings agree
    with the native full key, formula and five centres. DOL also supplies nonstereochemical
    descriptor variants; their unassigned stereo keys are expected descriptor scope
    and not chemical disagreement. ChEBI confirms the seven native names, including
    the 26aS systematic name and RP54476/INN variants, and CAS112362-50-2. The semisynthetic
    single component is distinct from its combination product.
  snapshot_sha256: 3d21766f1c5f7215f2988ab8f494208541e06bc84a7e2a3d700e5a0c4183a482
- evidence_id: classification
  kind: authority
  reference: CHEBI:140325; CHEBI:140326; CHEBI:25105; CHEBI:25106; CHEBI:33308; CHEBI:35681;
    CHEBI:35850; CHEBI:3992; CHEBI:46812; CHEBI:50996; CHEBI:51751; CHEBI:33281; CHEBI:36047;
    ARO:0000026
  locator: Official term names/definitions and exact-entry relations, with independent
    graph functional-group inspection.
  accessed_at: '2026-10-21T14:06:45Z'
  support: supports
  summary: The secondary and tertiary amides, ester/lactone, ketone, secondary alcohol,
    sulfone, oxazole, tertiary amine and enamide features are present. The macrolide
    and streptogramin classifications are broader structural classes, not a claim
    that dalfopristin is a macrolide-class target-site equivalent. Both antibacterial-drug
    and antimicrobial roles are explicit. Native HOST_SHARED_TARGET is consistent
    with the schema definition for microbial-selective drugs acting on conserved machinery;
    it does not assert direct binding to a named human protein.
  snapshot_sha256: 957190ce7737ea57b16a0ce99e5e7ca8c53ba1f0f5b6a62d144820ef43238ee9
- evidence_id: kegg-conflict
  kind: authority
  reference: https://rest.kegg.jp/get/C08033/mol; https://rest.kegg.jp/get/D00853/mol;
    https://www.genome.jp/Fig/compound/C08033.gif
  locator: Current official KEGG molfiles independently parsed and mapped; C08033
    displayed structural drawing visually inspected.
  accessed_at: '2026-10-21T14:04:41Z'
  support: refutes
  summary: Both KEGG encodings give SUYRLXYYZQTJHF-PSUTZUHDSA-N rather than native
    SUYRLXYYZQTJHF-VMBLUXKRSA-N. Connectivity is identical, but the carbonyl-adjacent
    five-membered-ring junction corresponding to native atom 0 is R in KEGG and S
    in the native graph; all four other assigned centres agree. This is the 26a junction,
    not missing stereo or a salt difference. C08033 is exported as an exact xref.
    D00853 is already a drug-level link, so its conflicting structure is source context
    rather than a second exact-xref defect.
  snapshot_sha256: 1dafb557490fb307e49207fcb1998a15c1b9b77ad5bdb50fb09365de2bfc5cca
- evidence_id: drug-links
  kind: database
  reference: DrugBank:DB01764; DrugCentral:778; KEGG:D00853; wikipedia.en:Dalfopristin
  locator: Public DrugBank page via web, complete DrugCentral page and SMILES endpoint,
    complete KEGG drug entry; Wikipedia topic resolution.
  accessed_at: '2026-10-21T14:04:42Z'
  support: context_only
  summary: The public DrugBank page names dalfopristin, RP54476, the native CAS and
    full key; its visible stereochemical SMILES agrees by inspection with the matched
    identity. DrugCentral names the correct drug/CAS but its downloadable SMILES gives
    a different pyrrolidine connectivity, KLRSZNOYZIOTBR-VLAQKBCTSA-N. Do not import
    that graph. These links are typed drug_xrefs, whose contract permits drug-level
    aggregation; their predictions, formulations and approval summaries are not native
    chemical or clinical claims. Wikipedia is correctly a topic link.
  snapshot_sha256: 2b80a4b9867883fd4f1327051d8b18c4e7ba4153c0934ce0fcf56d2658cc15fb
- evidence_id: card
  kind: database
  reference: https://raw.githubusercontent.com/arpcard/aro/master/src/ontology/aro.obo
  locator: Official current ARO file header dated 2026-08-11; all 33 relevant term
    blocks and their exact dalfopristin relations examined.
  accessed_at: '2026-10-21T14:10:59Z'
  support: supports
  summary: All thirty native resistance identifiers resolve to the expected labels
    and have an explicit dalfopristin resistance relation in this ontology. The class,
    compound and 23S-rRNA target blocks also resolve. These checks establish faithful
    database provenance and type mapping, not thirty independent functional demonstrations.
    The current ontology still contains broad Erm-to-dalfopristin links; the controlled
    experiment below exposes a context boundary requiring preservation. Thirty-three
    individual CARD page requests timed out; the official downloadable ontology supplies
    the actual inspected authority instead.
  snapshot_sha256: d12ec5d36c55f371079c392492b034d115adb256f8d2ff4a84041c6202f4a1c4
- evidence_id: ribosome
  kind: primary_source
  reference: PMID:15059283; DOI:10.1186/1741-7007-2-4; PMC400760; PDB:1SM1
  locator: Entire original main text and Table 1 read; Figure 2 on PDF page 4 visually
    inspected; RCSB experiment/citation metadata independently read.
  accessed_at: '2026-10-21T14:06:18Z'
  support: supports
  summary: The 3.42 Å D. radiodurans 50S structure uses fourfold dalfopristin and
    tenfold quinupristin during co-crystallization. Density supports dalfopristin
    at the peptidyl-transferase centre and overlapping A/P substrate positions; quinupristin
    occupies the adjacent tunnel region. The proposed rRNA rearrangement and synergistic
    functional interpretation are supported structurally but are not a newly measured
    whole-cell killing endpoint or affinity constant. The native wording preserves
    the combined-drug structural context. NCBI taxonomy independently confirms taxon1299
    as D. radiodurans.
  snapshot_sha256: 47c1829f577f2b5ef6e6a1947cfba19e954c9af5647862ab7744e579cc831e89
- evidence_id: vatd
  kind: primary_source
  reference: PMID:12771141; DOI:10.1074/jbc.M303766200; PDB:1MRL
  locator: Complete original indexed abstract and official PDB entry metadata; publisher
    PDF/fulltext returned 403.
  accessed_at: '2026-10-21T14:13:49Z'
  support: supports
  summary: The original abstract reports VatD structures with dalfopristin at 2.8
    Å and supports O18 acetylation and catalytic analysis. PDB1MRL independently identifies
    the dalfopristin acetyltransferase complex and correct original citation. This
    supports the native cocrystal note and distinguishes a resistance enzyme that
    modifies the drug from the lethal ribosomal target. Full assay methods, tables
    and kinetic numbers were not inspected or imported.
  snapshot_sha256: 0a3b8581f0d983f02a45d5727a865d086f987001abf305c338606e98f1bb6a37
- evidence_id: ermB-experiment
  kind: primary_source
  reference: PMID:10543753; DOI:10.1128/AAC.43.11.2720; PMC89549
  locator: Entire original main HTML including Methods, Results, Discussion and Tables
    1–3 read; Figure 1 caption read, plot not independently reprocessed.
  accessed_at: '2026-10-21T14:10:59Z'
  support: context_only
  summary: Agar dilution on Mueller-Hinton medium and defined pJIM2246 constructs
    separate single components from the combination. In E. faecium HM1070 and S. aureus
    RN4220, ermB alone leaves dalfopristin MIC at 1 microgram/mL versus vector while
    increasing quinupristin MIC. In the same backgrounds, ermB plus satA raises dalfopristin
    MIC above satA alone. Thus the experiment does not establish a simple, context-free
    ErmB-only dalfopristin resistance effect, but it also does not prove that ErmB
    can never contribute to a combined resistance phenotype. Exact reagent counterion/purity
    is not established in the inspected methods.
  snapshot_sha256: 9946c0df9e30728f8431ddf2d076508aa37574396a49e0dc628a56bdfbbc69f0
- evidence_id: adopted
  kind: database
  reference: PMID:23924572; PMID:23044949; PMID:21453475; PMID:19409762; PMID:18056275;
    PMID:17563376; PMID:15700955; PMID:15059283; PMID:12771141; PMID:11985218; PMID:1328138
  locator: All eleven adopted indexed records resolved; all six available abstracts
    read completely; five entries lack abstracts. Main full text additionally read
    for15059283.
  accessed_at: '2026-10-21T14:06:52Z'
  support: context_only
  summary: 23924572 is a combination-resistance letter without an abstract.23044949
    is an endophthalmitis case without an abstract.21453475 describes intravitreal
    combination treatment in one postoperative S. aureus case, not dalfopristin-alone
    efficacy.19409762 is a combination-breakpoint comment without an abstract.18056275
    studies combination effects on malaria parasites; do not transfer an exact-component
    antimalarial role.17563376 concerns Vgb and quinupristin, not dalfopristin/VatD.15700955
    and11985218 are reviews without indexed abstracts, not primary support.15059283
    and12771141 are separately assessed above.1328138 compares individual RP54476/RP57669
    and RP59500, but numerical activity statements in its inspected abstract concern
    the combination; those are not single-agent MICs.
  snapshot_sha256: 1565aee9daafeab9cd757c3ff3c792c704d60f8bb801b7ed174f2f81faa4c7e4
- evidence_id: adapter
  kind: database
  reference: Structured iModulonDB adapter
  locator: Dataset catalog and S. aureus erm/vga plus M. tuberculosis erm searches
    executed before web follow-up.
  accessed_at: '2026-10-21T14:13:49Z'
  support: context_only
  summary: D. radiodurans and Enterococcus are outside the inspected catalog. The
    S. aureus erm search returned only unrelated substring matches such as permease/spermidine
    genes and no module; vga returned no genes or modules. The M. tuberculosis search
    exited 2 because an upstream module regulator was null instead of a JSON list.
    No expression result or failed adapter call is used as evidence against resistance
    or direct binding.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: search
  kind: search
  reference: 341-inclusive-hits.txt;341-overlay-hits.txt
  locator: Exact-label/identifier/key search including hidden and ignored files; bounded
    official structures and original-literature follow-up.
  accessed_at: '2026-10-21T14:13:49Z'
  support: context_only
  summary: The exact native, maintained source rows and qualified target map were
    found. No exact dalfopristin card-evidence overlay was found in the actual JSON
    owner, with ignored files included. All adopted citations are disposed explicitly.
    The search was bounded rather than an exhaustive survey of every current ChEBI
    citation or all thirty determinant primary literatures.
  search_scope: 2026-10-21; rg --no-ignore --hidden across data, curation, conf, scripts,
    src, docs, .claude, reviews and reports using dalfopristin, CHEBI4309, ARO3000674
    and the exact InChIKey; actual card_evidence_reviews.json and target-map follow-up;
    public official chemical sources and exact original PMID/DOI searches.
  snapshot_sha256: 970fe66d07f7818a7c3d0fad333ef0057820e18636aaf3b54c310b87fa4a4a6f
- evidence_id: validation
  kind: validation
  reference: 341-schema.log;341-strict.log;341-chemistry.json;341-xref-chemistry.json;341-stereo-map.json
  locator: Actual focused executions and input hash recheck.
  accessed_at: '2026-10-21T14:13:49Z'
  support: supports
  summary: Schema, strict and native chemistry checks exit 0. The external comparison
    exits 1 and preserves the source differences; the independent localization script
    exits0. Early ad-hoc ontology reader attempts failed on missing Python packages
    and a wrong guessed native key; the corrected reader used the actual aro_id key
    and selected all 33 blocks. No native-data failure is inferred from those scratch-reader
    mistakes. All nineteen input hashes remain unchanged.
  snapshot_sha256: d9a647f6564a4e89b58340021dd6781753705b2f81ae81720189fa251f6f14a6
assessments:
- assessment_id: identity
  area: identity
  topic: Native exact structure and external equivalence scope
  outcome: concern
  summary: The native graph, names and stereochemistry agree with ChEBI, PubChem,
    ChEMBL and the structural ligand authority. The exact KEGG COMPOUND link encodes
    an epimer and requires a maintained-source correction or qualification. Drug-level
    source structure conflicts are explicitly separated.
  target_ids:
  - CHEBI:4309
  evidence_ids:
  - native
  - identity
  - classification
  - kegg-conflict
  - drug-links
  - validation
- assessment_id: mechanism
  area: evidence
  topic: Primary ribosome target, enzyme context and mechanism scope
  outcome: supported
  summary: The curated D. radiodurans complex supports direct binding at the 50S peptidyl-transferase
    centre with the stated combined-drug context. VatD is an inactivating resistance
    enzyme. The CARD 23S-rRNA target remains honestly evidence-needed; adding the
    existing primary citation there could improve linkage but its absence is not a
    confirmed false claim. HOST_SHARED_TARGET is appropriate to the schema meaning.
  target_ids:
  - CHEBI:4309
  evidence_ids:
  - ribosome
  - vatd
  - card
  - classification
  - adapter
- assessment_id: resistance
  area: evidence
  topic: Thirty qualified database assertions and controlled ErmB scope
  outcome: concern
  summary: Every imported edge matches the inspected official ontology and is expressly
    database-qualified. The controlled ErmB study makes a simple single-gene/component
    interpretation unsafe, while combination constructs demonstrate context effects.
    Preserve this evidence conflict and resolve it in the maintained qualification
    layer before functional promotion; do not delete all Erm-family edges by analogy.
  target_ids:
  - CHEBI:4309
  evidence_ids:
  - native
  - owners
  - card
  - ermB-experiment
- assessment_id: activity
  area: evidence
  topic: Antibacterial activity, clinical combination prose and adopted leads
  outcome: supported
  summary: The exact semisynthetic component is an antibacterial ribosomal inhibitor;
    the additional controlled paper measures dalfopristin separately. Native definition
    explicitly says use in a mixture with quinupristin and does not claim stand-alone
    VRE efficacy. Combination MICs, parasite effects, clinical case outcomes and quinupristin-specific
    enzymology are not silently transferred.
  target_ids:
  - CHEBI:4309
  evidence_ids:
  - identity
  - classification
  - ribosome
  - ermB-experiment
  - adopted
- assessment_id: provenance
  area: provenance
  topic: Maintained sources, identifiers, historic REVIEWED status and optional fields
  outcome: supported
  summary: Actual ARO owners and curator-owned target/notes were captured before judgment.
    Native REVIEWED is a historical event, not automatic validation of every current
    xref or imported resistance relationship. No optional absent spectrum, producer,
    causal graph or clinical summary is a corrective defect.
  target_ids:
  - CHEBI:4309
  evidence_ids:
  - owners
  - native
  - search
  - validation
findings:
- finding_id: F1
  issue_key: dalfopristin-kegg-exact-xref-ring-junction-epimer
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: The exact KEGG COMPOUND cross-reference encodes a ring-junction epimer
  description: Native xrefs includes kegg.compound:C08033 as a same-structure identity.
    Its current official molfile has full key SUYRLXYYZQTJHF-PSUTZUHDSA-N and a 26aR
    ring junction, whereas the native, ChEBI, PubChem, ChEMBL and stereochemical RCSB
    DOL encodings have SUYRLXYYZQTJHF-VMBLUXKRSA-N and 26aS. Independent graph mapping
    finds identical connectivity and four matching other centres. Qualify or withhold
    the exact equivalence until reconciled; do not overwrite the supported native
    structure from the conflicting KEGG graph. The already drug-level D00853 link
    is not an additional exact-equivalence claim.
  target_ids:
  - CHEBI:4309
  field_paths:
  - xrefs[3]
  evidence_ids:
  - identity
  - kegg-conflict
  - owners
  - validation
  rule_id: src/antibioticmech/schema/antibioticmech.yaml:xrefs same-structure contract;
    review checklist exact stereochemical identity
  native_severity: major
  normalization_reason: A positively established epimer mismatch in an exact chemical
    identifier can misground downstream evidence. The native core structure remains
    supported, so the record itself is not declared the wrong compound.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted same-structure KEGG xref
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI xref extraction and normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible exact-xref generation
- finding_id: F2
  issue_key: dalfopristin-ermb-database-primary-context-reconciliation
  category: evidence
  severity: informational
  status: open
  certainty: confirmed
  title: Retain the controlled ErmB context alongside the qualified database edge
  description: The imported ErmB edge faithfully states a CARD assertion and does
    not claim primary demonstration. In the inspected controlled study, ermB alone
    did not increase dalfopristin MIC in two susceptible backgrounds, whereas combinations
    with satA did. This evidence boundary merits an explicit maintained source-qualification
    follow-up, not an unqualified causal promotion, universal absence claim or automatic
    deletion of every Erm-family relation.
  target_ids:
  - CHEBI:4309
  field_paths:
  - resistance_mechanisms[5]
  evidence_ids:
  - native
  - card
  - ermB-experiment
  - owners
  rule_id: Review checklist evidence specificity and database-versus-primary qualification
  native_severity: informational
  normalization_reason: The native assertion already declares its database evidence
    level and agrees with the source. This is a bounded reconciliation question grounded
    in positive experimental context, not a confirmed false import or a requirement
    to populate optional primary evidence.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Imported direct CARD relations
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Maintained conflict/evidence qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Qualification application and integrity
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/dalfopristin.yaml
    role: Curator-owned exact primary evidence additions
actions:
- action_id: A1
  description: Reconcile the KEGG stereochemical discrepancy in maintained exact-xref
    handling.
  finding_ids:
  - F1
  target_ids:
  - CHEBI:4309
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Adopted same-structure KEGG xref
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ChEBI xref extraction and normalization
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible exact-xref generation
  acceptance_checks:
  - Retain current KEGG molfile/drawing and independent atom mapping; compare all
    five centres and full stereochemical keys rather than connectivity-only keys.
  - Withhold or explicitly qualify C08033 exact equivalence until the authority encoding
    is corrected or resolved. Preserve the supported native graph and existing drug-level
    D00853 context.
  - Regenerate through the maintained owner and rerun schema, strict and exact-structure
    equivalence checks.
- action_id: A2
  description: Resolve the bounded ErmB component/context question through the existing
    source-evidence qualification layer.
  finding_ids:
  - F2
  target_ids:
  - CHEBI:4309
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Imported direct CARD relations
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Maintained conflict/evidence qualification
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Qualification application and integrity
  - repository: CultureBotAI/AntibioticMech
    path: data/antibiotics/antibacterial/dalfopristin.yaml
    role: Curator-owned exact primary evidence additions
  acceptance_checks:
  - Preserve that CARD explicitly supplies the relation and that the native entry
    is database-qualified. Capture the controlled vector, ermB-alone and combined-construct
    outcomes separately.
  - Check exact alleles, host backgrounds, expression/induction and tested material
    before any functional claim. Do not equate combination-drug resistance with dalfopristin-alone
    resistance, or extrapolate this experiment to all Erm proteins.
  - If authorized, add an evidence qualification or primary observation with exact
    assay context; do not turn a conditional contribution into a universal negative
    or positive assertion.
limitations:
- HMDB0015566 returned 403 on direct, www and web attempts; its native identifier
  is confirmed only as the adopted/current ChEBI attestation, not an independently
  inspected HMDB structure. DrugBank was readable through public web but its direct
  download returned 403.
- The 2004 ribosome paper was read in full and Figure 2 visually inspected; raw diffraction
  data and all other figures were not independently reprocessed. Its introduction
  appears to reverse the component order in one 30:70 sentence; the record contains
  no ratio, and the controlled 1999 paper correctly specifies quinupristin:dalfopristin
  30:70. No new numerical combination claim is adopted.
- The VatD paper was read at complete indexed-abstract depth plus independent PDB
  metadata, with publisher full text/PDF 403. This supports the narrow cocrystal claim
  but is not a complete kinetic or mutant-method audit.
- All eleven adopted leads were resolved; six complete abstracts were available and
  read, five had no abstracts. Except for the 2004 ribosome paper, their full texts
  were not claimed read. Later current ChEBI leads were not exhaustively reviewed.
- The official ARO ontology validates all thirty exported database relations, but
  their individual original experimental literatures were not exhaustively read. The
  extra 1999 controlled study was read completely; its material lacks a separately
  verified counterion/purity certificate. Figure 1 was not independently quantified.
- The M. tuberculosis structured adapter failed schema parsing on a null regulator
  field. Successful S. aureus queries returned no relevant module; neither outcome
  is evidence against biological function.
- DrugCentral778 currently supplies a constitutional-isomer SMILES despite correct
  drug name/CAS. Keep this source-quality discrepancy visible and do not import that
  graph. The native drug_xrefs typing does not assert same-structure equivalence.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- No native status promotion or curation change is made by this review. Optional enrichment
  is separate from established corrective findings.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
