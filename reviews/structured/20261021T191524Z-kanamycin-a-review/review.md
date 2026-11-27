# Review of kanamycin A

- Review: 20261021T191524Z-kanamycin-a-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T18:53:54Z
- Finished UTC: 2026-10-21T19:15:24Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native kanamycin A structure and antibacterial activity are supported. Major corrections are needed for two chemically non-equivalent exact aliases, a ChEMBL stereoisomer cross-reference, and three resistance categories that incorrectly describe Eis-mediated drug inactivation as target alteration. Kantrex also needs minor brand typing. Qualified database assertions and unresolved primary-source boundaries are retained.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position 575; original thirteen inputs preserved and actual maintained owners appended before assessment, for twenty-one verified inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:17630 | data/antibiotics/antibacterial/kanamycin-a.yaml | generated | kanamycin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:17630 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:17630 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:17630 | Actual focused execution exited 0. |
| authority-initial | failed | False | CHEBI:17630 | The initial assertion failed on the current ChEMBL stereoisomer;575-authority-attempt1.json/.log preserve the actual Python exit 1. The shell later printed diagnostics and exited 0. The script was subsequently revised into an explicit comparison, not used to conceal this failure. |
| authority-final | passed | False | CHEBI:17630 | Final diagnostic comparison preserves nineteen encodings: sixteen match native, three CHEMBL223520 encodings do not; atom mapping and parity edits establish the exact difference. |
| ledger | passed | False | CHEBI:17630 | Twenty-one hashes, original thirteen unchanged, five chronological history events, two deterministic mints, 78 current resistance relations, six adopted leads and 90 current discovery records verified. |
| Structured iModulonDB query | passed | False | CHEBI:17630 | Actual search completed; results are expression/gene context rather than direct experimental proof. |
| Structured iModulonDB query | passed | False | CHEBI:17630 | Actual search completed; results are expression/gene context rather than direct experimental proof. |
| Structured iModulonDB query | passed | False | CHEBI:17630 | Actual search completed; results are expression/gene context rather than direct experimental proof. |
| Structured iModulonDB query | passed | False | CHEBI:17630 | Actual search completed; results are expression/gene context rather than direct experimental proof. |
| Structured iModulonDB query | passed | False | CHEBI:17630 | Actual search completed; results are expression/gene context rather than direct experimental proof. |
| Structured iModulonDB query | passed | False | CHEBI:17630 | Actual search completed; results are expression/gene context rather than direct experimental proof. |
| Structured iModulonDB query | passed | False | CHEBI:17630 | Actual search completed; results are expression/gene context rather than direct experimental proof. |
| Authoritative full QC | failed | True | CHEBI:17630 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:17630 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:17630 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:17630 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:17630 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:17630 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:17630 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:17630 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:17630 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact native neutral kanamycin A

identity: supported. Targets: CHEBI:17630.

The native graph agrees with independent exact authorities and the primary decoding-site ligand. Its identity is distinct from salt preparations, B congener aliases and the mismatching ChEMBL structure.

### Chemical and product alias scope

nomenclature: concern. Targets: CHEBI:17630.

Aminodeoxykanamycin denotes B and sulfate denotes a salt; neither is an exact neutral A synonym. Kantrex is a historical product brand. Aspidium and broader conventional kanamycin naming retain explicit limits.

### ChEMBL exact cross-reference

grounding: concern. Targets: CHEBI:17630.

CHEMBL223520 is a demonstrated stereoisomer mismatch; CHEMBL1384 is independently matched to the valid native graph. Other unavailable registries are not treated as confirmed errors.

### Antibacterial class, definition and target

scope: supported. Targets: CHEBI:17630.

The aminoglycoside/kanamycin class and antibacterial role are supported. The direct RNA-model structure can enrich the existing qualified target, while the definition remains a conventional review-based explanation rather than a new whole-cell experiment.

### Eis/WhiB7 normalized resistance mechanism

evidence: concern. Targets: CHEBI:17630.

The current ARO relations are real, but the three target-alteration categories conflict with original acetylation/inactivation experiments. WhiB7 is an indirect regulator and the separate Tap effect concerns streptomycin.

### Remaining resistance, adopted studies and access boundaries

evidence: unknown. Targets: CHEBI:17630.

All current edge memberships and available lead abstracts were inspected, but not every original experimental paper or assay material. Database-only assertions are retained at that tier; genome/coexpression evidence is not upgraded into direct causal proof.

### Source ownership and validation history

provenance: supported. Targets: CHEBI:17630.

Original input hashes, deterministic source identities, chronological history and actual focused validators were checked; the failed initial authority comparison remains recorded.

## Findings

### F1: Two exact aliases denote a different congener or salt

major / open / confirmed; issue key: kanamycin-a-b-congener-and-sulfate-exact-aliases.

Native Aminodeoxykanamycin and Kanamycin sulfate are typed EXACT_SYNONYM. Official MeSH/KEGG identify the former with kanamycin B, with a different formula; the latter contains sulfate absent from the neutral A graph.

### F2: The exact ChEMBL link resolves to a different stereoisomer

major / open / confirmed; issue key: kanamycin-a-chembl223520-stereoisomer-xref.

Native xrefs[8] points to CHEMBL223520, whose current three encodings invert all five centers in one sugar ring. The native structure is supported; matching CHEMBL1384 provides a concrete candidate repair.

### F3: Eis and WhiB7 resistance are misclassified as target alteration

major / open / confirmed; issue key: kanamycin-a-eis-whib7-inactivation-classification.

Native resistance_mechanisms[64–66] normalize Eis and two WhiB7 mutation terms to ANTIBIOTIC_TARGET_ALTERATION through a generic ARO mutation ancestor. Original experiments instead demonstrate kanamycin acetylation/inactivation, regulated indirectly by WhiB7. The resistance associations remain valid; the normalized mechanism is wrong.

### F4: Kantrex needs product-brand typing

minor / open / confirmed; issue key: kanamycin-a-kantrex-brand-type.

Native synonyms[12] marks the verified historical Kantrex product name EXACT_SYNONYM rather than BRAND_NAME.

## Recommended Actions And Acceptance Checks

### A1

Use the maintained source-specific synonym_exclusions policy for ARO:0000049 to prevent Aminodeoxykanamycin and Kanamycin sulfate from entering exact A aliases. Preserve their valid B/salt records and conventional qualified drug context; do not globally ban the names.

- Regenerated exact A aliases exclude both non-equivalent terms.
- Native neutral structure and separately represented B/salt compounds remain unchanged.

### A2

Correct the source-owned ARO chemical cross-reference through a reproducible extraction/reconciliation policy. Verify CHEMBL1384 against the native full graph and replace the incompatible exact CHEMBL223520 link; preserve the supported native stereochemistry.

- Chosen exact ChEMBL structure matches native by complete key and chirality-aware atom mapping.
- Regeneration does not reintroduce CHEMBL223520 as exact A equivalence.

### A3

Add a narrow determinant-plus-antibiotic normalization correction in the maintained extraction/configuration path so these kanamycin edges describe ANTIBIOTIC_INACTIVATION, while retaining WhiB7 regulatory and mutation context and original database provenance. The existing mechanism_for loop checks ancestors, so simply adding determinant IDs to its current map would not work. Do not globally reclassify all mutation terms, call WhiB7 an acetyltransferase, or transfer Tap-mediated streptomycin efflux to kanamycin.

- All three regenerated kanamycin mechanisms represent drug inactivation with regulator/context qualifications retained.
- Other mutation and efflux edges are not changed by an overbroad ancestor override.
- Meaningful focused generator checks and required schema, term/reference/history/corpus and full QC pass for eventual curation.

### A4

Preserve Kantrex as a historical product alias using source-owned BRAND NAME input typing or a reproducible equivalent policy that emits BRAND_NAME.

- Kantrex is retained with BRAND_NAME and source provenance.
- Product hydration/congener purity are not asserted from the historical name alone.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/kanamycin-a.yaml; Entire689-line native; fourteen aliases, class/role, exact chemical structure, ten exact xrefs, two drug xrefs, document link,78 resistance assertions, one target and five history events | supports | SEEDED/EXACT CHEBI:17630 represents neutral kanamycin A. Native target and resistance entries explicitly identify database assertions. No separate structured MIC, clinical-indication, producer, dataset or causal-graph objects are present; definition claims are assessed below. The target retains PRIMARY_EVIDENCE_NEEDED rather than pretending an original paper has already been curated. |
| chemistry | CHEBI:17630;pubchem.compound:6032;kegg.compound:C01822;pdb-ccd:KAN;vsdb:1921; 575-authority-check.py/575-authority-chemistry.json; snapshots and timestamps in575-fetch.json/575-fetch2.json | supports | Native SMILES/InChI, current ChEBI, PubChem, KEGG, CCD KAN and VSDB structures agree on SBUJHOSQTJFQJX-NOAMYHISSA-N, C18H36N4O11 and charge 0. Reciprocal chirality-aware mapping supports the fully configured exact graph; no mixture inference follows from broader commercial naming. Primary crystallographic material and drug formulations are kept separate. |
| wrongxref | chembl.compound:CHEMBL223520;chembl.compound:CHEMBL1384; 575-chembl.json;575-chembl-exact-key.json;575-authority-chemistry.json atom mapping/parity-edit comparison | refutes | The asserted CHEMBL223520 SMILES, InChI and molfile encode SBUJHOSQTJFQJX-KSACQAOKSA-N. All five centers of one amino-sugar ring invert relative to native mapped atoms 2/4/27/29/31, while constitution is unchanged. This is demonstrated by chirality-aware matching and reconstructing the authority graph with mapped parity edits, not raw @ or CIP-label comparison alone. Exact native-key lookup returns CHEMBL1384, whose three encodings agree. |
| aliases | MeSH:C001495;kegg.compound:C00825;CHEBI:6109; 575-mesh-bekanamycin.html/.txt;575-bekanamycin-kegg.txt;575-amino-original-core.json;574-authority-chemistry.json | refutes | Official MeSH places Aminodeoxykanamycin under bekanamycin/kanamycin B. KEGG C00825 has the B formula C18H37N5O10, distinct from native A. The 1977 original aminodeoxykanamycin abstract also names Kanendomycin but is not used as a bacterial A experiment. Separately, kanamycin sulfate includes an additional sulfate component, independently verified in 574; it is not an exact synonym for the neutral free base. |
| brand | FDA DESI11503;Federal Register35(7),1970-01-10,p397; 574-kantrex-fr1970.pdf and actual574-kantrex-p397.png;574-fetch.json | supports | The official historical notice identifies Kantrex Injection and Kantrex Capsules as kanamycin sulfate products with amounts expressed as kanamycin base. Kantrex is therefore a product brand. This does not assert present marketing status, congener purity or hydration. |
| target | PMID:16214802;DOI:10.1093/nar/gki862;PDB:2ESI; 476-PMC1251667.xml, original Methods, kanamycin A Results and binding Discussion;476-fetch3.json;575-primary2005-fig1.jpg;575-pdb2ESI.json | supports | The original 2005 study crystallizes kanamycin A with a synthetic 23-nucleotide bacterial decoding-site RNA duplex, resolving the kanamycin complex at 3.0 angstroms. It supports direct A-site binding, with A1408/G1491 contacts and displaced A1492/A1493. It is not an intact-ribosome or whole-cell translation experiment. Sigma material has no catalog/salt specification in inspected Methods. One additional nonspecific molecule in one site is not universal binding stoichiometry. CCD KAN agrees with the native graph. |
| eis | PMID:19906990;DOI:10.1073/pnas.0907925106; 575-PMC2785282-alt.html/.txt, allele-replacement Results/actualTable1, Eis biochemistry/TLC/disk diffusion, Discussion and main Methods;575-fetch5.json | supports | Original 2009 experiments show Eis-mediated kanamycin acetylation and loss of antibacterial activity in the complete Eis/acetyl-CoA reaction. Specific eis-promoter mutations raise resistance and allele restoration reverses it. This is antibiotic inactivation, not alteration of the ribosomal target. Exact MIC procedures are delegated to inaccessible SI; catalog/salt and kinetic-protocol inconsistencies remain bounded. No universal clinical-allele interpretation or kinetic constant is adopted. |
| whib | PMID:23380727;DOI:10.1128/AAC.02191-12; 575-PMC3623337-alt.html/.txt, MIC/genetic/lysate Methods, whiB7/eis/tap Results, actualTable1 and Discussion;575-fetch5.json | supports | Original 2013 specific whiB7 untranslated-region mutants increase whiB7/eis expression and kanamycin acetylation. Table 1 shows kanamycin MIC 2 micrograms/mL for parental strains and 20 for K301, returning to 2 after wild-type allele restoration. Deleting tap leaves K301 kanamycin MIC 10 while restoring streptomycin susceptibility, so the Tap result must not be transferred to kanamycin efflux. The mechanism is indirect regulation of drug inactivation, not a modified ribosome or WhiB7 itself acting as an acetyltransferase. Sigma kanamycin salt/catalog are unspecified; agar MIC means &gt;99% growth inhibition after four weeks at 37 C. |
| mapping | scripts/extract_source_inventory.py;conf/sources.yaml;data/raw/aro_resistance_edges.tsv; mechanism_for nearest-ancestor logic;575-mechanism-lineages.json;575-raw-rows.json;575-aro-blocks.json | supports | All 78 current official ARO antibiotic-resistance relations remain present. Eis and both whiB7 terms inherit a broad mutation/target-alteration ancestor and emit ANTIBIOTIC_TARGET_ALTERATION at resistance_mechanisms[64–66]. The extractor checks ancestors rather than the determinant itself. Honest database provenance does not make this normalized category scientifically correct; the original experiments identify an inactivation route. Other assertions retain their database tier and mutation/deletion/organism context. |
| adopted | PMID:10103173;PMID:11083623;PMID:8385262;PMID:22907688;PMID:24336356;PMID:24566637; 575-adopted-core-0.json;575-source-audit.json;575-PMC3958260.xml;542-PMC89199.html | supports | All six adopted leads were resolved. The 1999 source is a review: selected actual opening mechanism/class paragraphs support conventional 30S binding/misreading, not a new experiment. The 1993 complete abstract concerns modifying-enzyme families; the 2000 review has metadata only because no indexed abstract/full text was accessible. The 2013 simulation paper and RNA G-quadruplex paper are bounded to their computational/model-binding scope. The 2014 aptamer original uses kanamycin A disulfate salt dihydrate, a four-drug selection mixture and analytical binding/wastewater experiments, not an exact free-base cellular target assay. |
| discovery | Current ARO references and structured iModulonDB context; 575-current-core-0/1/2/3.json;575-aro-read.txt;575-adapter-results.json/575-adapter2-results.json;575-adapter-whib7-summary.txt | supports | All 90 current ARO discovery records were checked:85 complete available abstracts and five metadata-only records. Original Eis/WhiB7 papers were followed to the specified main-text depth. Other reviews, plasmid/genome surveys, clinical associations, modifying-enzyme studies and mutation reports remain at their actual read depth; missing exact-drug detail does not refute an honestly qualified database edge. Adapter queries preceded primary follow-up: gene hits and the WhiB7 expression module provide context, not causal proof. KdpDE transport/stress review and MipA deletion observations are not generalized into direct kanamycin transport or wild-type resistance. |
| groundings | CHEBI:24951;CHEBI:33281;ARO:0000016;CAS:59-01-8;Beilstein:61647;Gmelin:2044856;LINCS:LSM-5261;drugbank:DB01172;drugcentral:1519;wikipedia.en:Kanamycin; 575-source-audit.json all-identifier dispositions;575-chebi-24951/33281.json;575-drugcentral.html;575-wikipedia.html;300-hms-small-molecules.sdf and300-final-fetch.json | supports | Current class/role terms fit the native amino-sugar/deoxystreptamine scaffold and antibacterial evidence. Public CAS concordance is not paid registry verification. Beilstein/Gmelin remain independently unresolved. DrugBank returned 403; DrugCentral contains drug/form aliases and stays in drug_xrefs without exact-equivalence promotion. Wikipedia redirects to kanamycin A and is a secondary document. The limited 2020 HMS collection has no LSM-5261 among 639 records / 458 populated LINCS IDs, which does not prove a wrong LINCS identifier. Aspidium remains an unresolved repeated alias, not an absence-based finding. |
| provenance | Original captures and maintained source ownership; 575-inspect.json/575-initial-inspect.json;575-owners-search.json;575-source-audit.json | supports | All twenty-one captured input hashes match, including the thirteen immutable originals. Five history events are chronological and both source mints recompute. Actual ChEBI/ARO/PubChem inventories, extractor, seeder, mechanism configuration, target policy and evidence overlay were inspected. No native or maintained source was edited. |

## Limits And Additional Notes

- Read depth is explicit: six adopted leads, ninety current discovery records with eighty-five available abstracts, and selected original primary passages/actual tables. This is not a claim to have read ninety complete originals.
- The 2009 Eis SI download was an HTML challenge despite its .pdf extension and is excluded. Exact kanamycin catalog/salt in the 2005/2009/2013 mechanism experiments remains unresolved; no universal genotype, clinical breakpoint or quantitative kinetic constant is inferred.
- Initial PMC challenge pages and failed XML/CARD/LINCS retrievals are recorded separately from successful primary HTML. DrugBank, Beilstein and Gmelin remain independently unresolved. A limited HMS archive absence does not prove a wrong LINCS mapping.
- Aspidium is repeated by the source but independently unresolved. Broader kanamycin naming and commercial mixtures do not invalidate the fully specified native A graph.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- Native records and maintained sources remain read-only. All thirteen original hashes are preserved within twenty-one verified inputs.
- Standalone chemistry used the 019 interpreter against 058; native schema/strict, ledger and contract used 058. The initial failed authority assertion is retained alongside the successful diagnostic run.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T191524Z-kanamycin-a-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of kanamycin A
started_at: '2026-10-21T18:53:54Z'
finished_at: '2026-10-21T19:15:24Z'
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
summary: The native kanamycin A structure and antibacterial activity are supported.
  Major corrections are needed for two chemically non-equivalent exact aliases, a
  ChEMBL stereoisomer cross-reference, and three resistance categories that incorrectly
  describe Eis-mediated drug inactivation as target alteration. Kantrex also needs
  minor brand typing. Qualified database assertions and unresolved primary-source
  boundaries are retained.
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
  - path: data/antibiotics/antibacterial/kanamycin-a.yaml
    sha256: ae1f4597070b1e1878d7e4454a53bcbcf0e5187bfa8b39940e73cd76f1bbcc38
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
  - path: data/raw/aro_target_edges.tsv
    sha256: 556c2ad9d389e3df28b4ff4006f83991bf94e80076cb10fba67bbddfb752bc81
    role: context
  - path: data/raw/pubchem_structures.tsv
    sha256: feff7c22bdca2b4af95c8df328c6f23561ec71403a3d2ed779c5074ade3e616b
    role: context
  - path: scripts/enrich_pubchem_structures.py
    sha256: c4299aa8385272ade40ee12c44b908c25bd901eb8459560f13ba3b7c1823b4bd
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
- target_id: CHEBI:17630
  path: data/antibiotics/antibacterial/kanamycin-a.yaml
  label: kanamycin A
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: ChEBI exact free-base structure, names, parent and adopted leads
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_role_names.tsv
    role: Antibacterial role grounding
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Exact ARO identity, definition, names and adopted lead
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Seventy-eight resistance database assertions
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: 16S rRNA target database assertion
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: Exact PubChem structure enrichment
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Source structure enrichment owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Actual CARD/ARO extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Generated identity, source assertions and enrichment
  - repository: CultureBotAI/AntibioticMech
    path: conf/aro_target_roles.tsv
    role: Target relation and primary-evidence-needed policy
  - repository: CultureBotAI/AntibioticMech
    path: curation/card_evidence_reviews.json
    role: Source-assertion qualification owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/card_evidence_reviews.py
    role: Source-assertion qualification application
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Source scope and names/grounding policy
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Maintained exact grounding decisions
scope:
  description: Entire exact native record, all asserted groundings, source provenance
    and adopted citation scope, with bounded primary activity and mechanism follow-up.
  selection: Initially uncovered queue position 575; original thirteen inputs preserved
    and actual maintained owners appended before assessment, for twenty-one verified
    inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:17630
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:17630
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    575
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:17630
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/kanamycin-a.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:17630
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/kanamycin-a.yaml --out /private/tmp/am-review-session/575-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: authority-initial
  name: authority-initial
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/575-authority-check.py
  status: failed
  required: false
  exit_code: 1
  expected_exit_code: 0
  summary: The initial assertion failed on the current ChEMBL stereoisomer;575-authority-attempt1.json/.log
    preserve the actual Python exit 1. The shell later printed diagnostics and exited
    0. The script was subsequently revised into an explicit comparison, not used to
    conceal this failure.
  target_ids:
  - CHEBI:17630
- check_id: authority-final
  name: authority-final
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/575-authority-check.py
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: 'Final diagnostic comparison preserves nineteen encodings: sixteen match
    native, three CHEMBL223520 encodings do not; atom mapping and parity edits establish
    the exact difference.'
  target_ids:
  - CHEBI:17630
- check_id: ledger
  name: ledger
  command: .venv/bin/python /private/tmp/am-review-session/575-ledger.py > /private/tmp/am-review-session/575-ledger.log
    2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Twenty-one hashes, original thirteen unchanged, five chronological history
    events, two deterministic mints, 78 current resistance relations, six adopted
    leads and 90 current discovery records verified.
  target_ids:
  - CHEBI:17630
- check_id: adapter-0
  name: Structured iModulonDB query
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset precise1k --query rrsB
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Actual search completed; results are expression/gene context rather than
    direct experimental proof.
  target_ids:
  - CHEBI:17630
- check_id: adapter-1
  name: Structured iModulonDB query
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset precise1k --query acrD
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Actual search completed; results are expression/gene context rather than
    direct experimental proof.
  target_ids:
  - CHEBI:17630
- check_id: adapter-2
  name: Structured iModulonDB query
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset precise1k --query mipA
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Actual search completed; results are expression/gene context rather than
    direct experimental proof.
  target_ids:
  - CHEBI:17630
- check_id: adapter-3
  name: Structured iModulonDB query
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism e_coli --dataset precise1k --query kdpD
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Actual search completed; results are expression/gene context rather than
    direct experimental proof.
  target_ids:
  - CHEBI:17630
- check_id: adapter-4
  name: Structured iModulonDB query
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism m_tuberculosis --dataset modulome --query
    eis
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Actual search completed; results are expression/gene context rather than
    direct experimental proof.
  target_ids:
  - CHEBI:17630
- check_id: adapter-5
  name: Structured iModulonDB query
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism m_tuberculosis --dataset modulome --query
    whiB7
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Actual search completed; results are expression/gene context rather than
    direct experimental proof.
  target_ids:
  - CHEBI:17630
- check_id: adapter-6
  name: Structured iModulonDB query
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism p_aeruginosa --dataset precise364 --query
    pvrR
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Actual search completed; results are expression/gene context rather than
    direct experimental proof.
  target_ids:
  - CHEBI:17630
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:17630
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
  - CHEBI:17630
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
  - CHEBI:17630
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
  - CHEBI:17630
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
  - CHEBI:17630
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
  - CHEBI:17630
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
  - CHEBI:17630
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
  - CHEBI:17630
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
  - CHEBI:17630
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/kanamycin-a.yaml
  locator: Entire689-line native; fourteen aliases, class/role, exact chemical structure,
    ten exact xrefs, two drug xrefs, document link,78 resistance assertions, one target
    and five history events
  accessed_at: '2026-10-21T19:14:38Z'
  support: supports
  summary: SEEDED/EXACT CHEBI:17630 represents neutral kanamycin A. Native target
    and resistance entries explicitly identify database assertions. No separate structured
    MIC, clinical-indication, producer, dataset or causal-graph objects are present;
    definition claims are assessed below. The target retains PRIMARY_EVIDENCE_NEEDED
    rather than pretending an original paper has already been curated.
- evidence_id: chemistry
  kind: validation
  reference: CHEBI:17630;pubchem.compound:6032;kegg.compound:C01822;pdb-ccd:KAN;vsdb:1921
  locator: 575-authority-check.py/575-authority-chemistry.json; snapshots and timestamps
    in575-fetch.json/575-fetch2.json
  accessed_at: '2026-10-21T19:14:38Z'
  support: supports
  summary: Native SMILES/InChI, current ChEBI, PubChem, KEGG, CCD KAN and VSDB structures
    agree on SBUJHOSQTJFQJX-NOAMYHISSA-N, C18H36N4O11 and charge 0. Reciprocal chirality-aware
    mapping supports the fully configured exact graph; no mixture inference follows
    from broader commercial naming. Primary crystallographic material and drug formulations
    are kept separate.
  snapshot_sha256: e672fee3de3055370d4083feff6fcc31315e64514622c7bae838c5d21779707c
- evidence_id: wrongxref
  kind: authority
  reference: chembl.compound:CHEMBL223520;chembl.compound:CHEMBL1384
  locator: 575-chembl.json;575-chembl-exact-key.json;575-authority-chemistry.json
    atom mapping/parity-edit comparison
  accessed_at: '2026-10-21T19:14:38Z'
  support: refutes
  summary: The asserted CHEMBL223520 SMILES, InChI and molfile encode SBUJHOSQTJFQJX-KSACQAOKSA-N.
    All five centers of one amino-sugar ring invert relative to native mapped atoms
    2/4/27/29/31, while constitution is unchanged. This is demonstrated by chirality-aware
    matching and reconstructing the authority graph with mapped parity edits, not
    raw @ or CIP-label comparison alone. Exact native-key lookup returns CHEMBL1384,
    whose three encodings agree.
  snapshot_sha256: 1c9f8a2ba9e47aace23dbd96b6321190d7d4b0b6fde74762d042de8175b93054
- evidence_id: aliases
  kind: authority
  reference: MeSH:C001495;kegg.compound:C00825;CHEBI:6109
  locator: 575-mesh-bekanamycin.html/.txt;575-bekanamycin-kegg.txt;575-amino-original-core.json;574-authority-chemistry.json
  accessed_at: '2026-10-21T19:14:38Z'
  support: refutes
  summary: Official MeSH places Aminodeoxykanamycin under bekanamycin/kanamycin B.
    KEGG C00825 has the B formula C18H37N5O10, distinct from native A. The 1977 original
    aminodeoxykanamycin abstract also names Kanendomycin but is not used as a bacterial
    A experiment. Separately, kanamycin sulfate includes an additional sulfate component,
    independently verified in 574; it is not an exact synonym for the neutral free
    base.
  snapshot_sha256: ba4200b2491e376ce4eedbf50530cf617240e47f94ecdaa52d318131f96af132
- evidence_id: brand
  kind: authority
  reference: FDA DESI11503;Federal Register35(7),1970-01-10,p397
  locator: 574-kantrex-fr1970.pdf and actual574-kantrex-p397.png;574-fetch.json
  accessed_at: '2026-10-21T19:14:38Z'
  support: supports
  summary: The official historical notice identifies Kantrex Injection and Kantrex
    Capsules as kanamycin sulfate products with amounts expressed as kanamycin base.
    Kantrex is therefore a product brand. This does not assert present marketing status,
    congener purity or hydration.
  snapshot_sha256: 5e4a68268763a9da1a71c776a27541f1063e95704edfdee945aac0ec62d667d6
- evidence_id: target
  kind: primary_source
  reference: PMID:16214802;DOI:10.1093/nar/gki862;PDB:2ESI
  locator: 476-PMC1251667.xml, original Methods, kanamycin A Results and binding Discussion;476-fetch3.json;575-primary2005-fig1.jpg;575-pdb2ESI.json
  accessed_at: '2026-10-21T19:14:38Z'
  support: supports
  summary: The original 2005 study crystallizes kanamycin A with a synthetic 23-nucleotide
    bacterial decoding-site RNA duplex, resolving the kanamycin complex at 3.0 angstroms.
    It supports direct A-site binding, with A1408/G1491 contacts and displaced A1492/A1493.
    It is not an intact-ribosome or whole-cell translation experiment. Sigma material
    has no catalog/salt specification in inspected Methods. One additional nonspecific
    molecule in one site is not universal binding stoichiometry. CCD KAN agrees with
    the native graph.
  snapshot_sha256: 1999a8a9aa83f35c77300c7006ad609ee09d7d83ff1095bb028286d92ae442d8
- evidence_id: eis
  kind: primary_source
  reference: PMID:19906990;DOI:10.1073/pnas.0907925106
  locator: 575-PMC2785282-alt.html/.txt, allele-replacement Results/actualTable1,
    Eis biochemistry/TLC/disk diffusion, Discussion and main Methods;575-fetch5.json
  accessed_at: '2026-10-21T19:14:38Z'
  support: supports
  summary: Original 2009 experiments show Eis-mediated kanamycin acetylation and loss
    of antibacterial activity in the complete Eis/acetyl-CoA reaction. Specific eis-promoter
    mutations raise resistance and allele restoration reverses it. This is antibiotic
    inactivation, not alteration of the ribosomal target. Exact MIC procedures are
    delegated to inaccessible SI; catalog/salt and kinetic-protocol inconsistencies
    remain bounded. No universal clinical-allele interpretation or kinetic constant
    is adopted.
  snapshot_sha256: 1abd1a379c0d4b86b87ac6b41d0942f10d9664403d9082f6779104c7c5127495
- evidence_id: whib
  kind: primary_source
  reference: PMID:23380727;DOI:10.1128/AAC.02191-12
  locator: 575-PMC3623337-alt.html/.txt, MIC/genetic/lysate Methods, whiB7/eis/tap
    Results, actualTable1 and Discussion;575-fetch5.json
  accessed_at: '2026-10-21T19:14:38Z'
  support: supports
  summary: Original 2013 specific whiB7 untranslated-region mutants increase whiB7/eis
    expression and kanamycin acetylation. Table 1 shows kanamycin MIC 2 micrograms/mL
    for parental strains and 20 for K301, returning to 2 after wild-type allele restoration.
    Deleting tap leaves K301 kanamycin MIC 10 while restoring streptomycin susceptibility,
    so the Tap result must not be transferred to kanamycin efflux. The mechanism is
    indirect regulation of drug inactivation, not a modified ribosome or WhiB7 itself
    acting as an acetyltransferase. Sigma kanamycin salt/catalog are unspecified;
    agar MIC means >99% growth inhibition after four weeks at 37 C.
  snapshot_sha256: 8ca8377e0f256ec2b3639a53500b487857b3eee58f0c03d50ea31f2f211c73af
- evidence_id: mapping
  kind: validation
  reference: scripts/extract_source_inventory.py;conf/sources.yaml;data/raw/aro_resistance_edges.tsv
  locator: mechanism_for nearest-ancestor logic;575-mechanism-lineages.json;575-raw-rows.json;575-aro-blocks.json
  accessed_at: '2026-10-21T19:14:38Z'
  support: supports
  summary: All 78 current official ARO antibiotic-resistance relations remain present.
    Eis and both whiB7 terms inherit a broad mutation/target-alteration ancestor and
    emit ANTIBIOTIC_TARGET_ALTERATION at resistance_mechanisms[64–66]. The extractor
    checks ancestors rather than the determinant itself. Honest database provenance
    does not make this normalized category scientifically correct; the original experiments
    identify an inactivation route. Other assertions retain their database tier and
    mutation/deletion/organism context.
  snapshot_sha256: e856e1392418ac56eff39f5017cfec767e360f1a052e9ce31f4b2384703c4410
- evidence_id: adopted
  kind: primary_source
  reference: PMID:10103173;PMID:11083623;PMID:8385262;PMID:22907688;PMID:24336356;PMID:24566637
  locator: 575-adopted-core-0.json;575-source-audit.json;575-PMC3958260.xml;542-PMC89199.html
  accessed_at: '2026-10-21T19:14:38Z'
  support: supports
  summary: 'All six adopted leads were resolved. The 1999 source is a review: selected
    actual opening mechanism/class paragraphs support conventional 30S binding/misreading,
    not a new experiment. The 1993 complete abstract concerns modifying-enzyme families;
    the 2000 review has metadata only because no indexed abstract/full text was accessible.
    The 2013 simulation paper and RNA G-quadruplex paper are bounded to their computational/model-binding
    scope. The 2014 aptamer original uses kanamycin A disulfate salt dihydrate, a
    four-drug selection mixture and analytical binding/wastewater experiments, not
    an exact free-base cellular target assay.'
  snapshot_sha256: 64ccedc15de015ac52f7b16e80ff2349b465997a842ecc9ce191ec611f3d5934
- evidence_id: discovery
  kind: search
  reference: Current ARO references and structured iModulonDB context
  locator: 575-current-core-0/1/2/3.json;575-aro-read.txt;575-adapter-results.json/575-adapter2-results.json;575-adapter-whib7-summary.txt
  accessed_at: '2026-10-21T19:14:38Z'
  support: supports
  summary: 'All 90 current ARO discovery records were checked:85 complete available
    abstracts and five metadata-only records. Original Eis/WhiB7 papers were followed
    to the specified main-text depth. Other reviews, plasmid/genome surveys, clinical
    associations, modifying-enzyme studies and mutation reports remain at their actual
    read depth; missing exact-drug detail does not refute an honestly qualified database
    edge. Adapter queries preceded primary follow-up: gene hits and the WhiB7 expression
    module provide context, not causal proof. KdpDE transport/stress review and MipA
    deletion observations are not generalized into direct kanamycin transport or wild-type
    resistance.'
  search_scope: All adopted ChEBI/ARO citations and current references for the78 native
    resistance nodes, exact decoding-site primary evidence, Eis/WhiB7 original mechanisms,
    and structured iModulonDB gene/module queries. Local absence searches included
    ignored files.
  snapshot_sha256: 64ccedc15de015ac52f7b16e80ff2349b465997a842ecc9ce191ec611f3d5934
- evidence_id: groundings
  kind: authority
  reference: CHEBI:24951;CHEBI:33281;ARO:0000016;CAS:59-01-8;Beilstein:61647;Gmelin:2044856;LINCS:LSM-5261;drugbank:DB01172;drugcentral:1519;wikipedia.en:Kanamycin
  locator: 575-source-audit.json all-identifier dispositions;575-chebi-24951/33281.json;575-drugcentral.html;575-wikipedia.html;300-hms-small-molecules.sdf
    and300-final-fetch.json
  accessed_at: '2026-10-21T19:14:38Z'
  support: supports
  summary: Current class/role terms fit the native amino-sugar/deoxystreptamine scaffold
    and antibacterial evidence. Public CAS concordance is not paid registry verification.
    Beilstein/Gmelin remain independently unresolved. DrugBank returned 403; DrugCentral
    contains drug/form aliases and stays in drug_xrefs without exact-equivalence promotion.
    Wikipedia redirects to kanamycin A and is a secondary document. The limited 2020
    HMS collection has no LSM-5261 among 639 records / 458 populated LINCS IDs, which
    does not prove a wrong LINCS identifier. Aspidium remains an unresolved repeated
    alias, not an absence-based finding.
  snapshot_sha256: 64ccedc15de015ac52f7b16e80ff2349b465997a842ecc9ce191ec611f3d5934
- evidence_id: provenance
  kind: validation
  reference: Original captures and maintained source ownership
  locator: 575-inspect.json/575-initial-inspect.json;575-owners-search.json;575-source-audit.json
  accessed_at: '2026-10-21T19:14:38Z'
  support: supports
  summary: All twenty-one captured input hashes match, including the thirteen immutable
    originals. Five history events are chronological and both source mints recompute.
    Actual ChEBI/ARO/PubChem inventories, extractor, seeder, mechanism configuration,
    target policy and evidence overlay were inspected. No native or maintained source
    was edited.
  snapshot_sha256: 64ccedc15de015ac52f7b16e80ff2349b465997a842ecc9ce191ec611f3d5934
assessments:
- assessment_id: identity
  area: identity
  topic: Exact native neutral kanamycin A
  outcome: supported
  summary: The native graph agrees with independent exact authorities and the primary
    decoding-site ligand. Its identity is distinct from salt preparations, B congener
    aliases and the mismatching ChEMBL structure.
  target_ids:
  - CHEBI:17630
  evidence_ids:
  - native
  - chemistry
  - target
- assessment_id: aliases
  area: nomenclature
  topic: Chemical and product alias scope
  outcome: concern
  summary: Aminodeoxykanamycin denotes B and sulfate denotes a salt; neither is an
    exact neutral A synonym. Kantrex is a historical product brand. Aspidium and broader
    conventional kanamycin naming retain explicit limits.
  target_ids:
  - CHEBI:17630
  evidence_ids:
  - aliases
  - brand
  - groundings
- assessment_id: xref
  area: grounding
  topic: ChEMBL exact cross-reference
  outcome: concern
  summary: CHEMBL223520 is a demonstrated stereoisomer mismatch; CHEMBL1384 is independently
    matched to the valid native graph. Other unavailable registries are not treated
    as confirmed errors.
  target_ids:
  - CHEBI:17630
  evidence_ids:
  - wrongxref
  - chemistry
  - groundings
- assessment_id: role
  area: scope
  topic: Antibacterial class, definition and target
  outcome: supported
  summary: The aminoglycoside/kanamycin class and antibacterial role are supported.
    The direct RNA-model structure can enrich the existing qualified target, while
    the definition remains a conventional review-based explanation rather than a new
    whole-cell experiment.
  target_ids:
  - CHEBI:17630
  evidence_ids:
  - native
  - chemistry
  - target
  - eis
  - whib
  - adopted
- assessment_id: resistance
  area: evidence
  topic: Eis/WhiB7 normalized resistance mechanism
  outcome: concern
  summary: The current ARO relations are real, but the three target-alteration categories
    conflict with original acetylation/inactivation experiments. WhiB7 is an indirect
    regulator and the separate Tap effect concerns streptomycin.
  target_ids:
  - CHEBI:17630
  evidence_ids:
  - mapping
  - eis
  - whib
  - discovery
- assessment_id: limits
  area: evidence
  topic: Remaining resistance, adopted studies and access boundaries
  outcome: unknown
  summary: All current edge memberships and available lead abstracts were inspected,
    but not every original experimental paper or assay material. Database-only assertions
    are retained at that tier; genome/coexpression evidence is not upgraded into direct
    causal proof.
  target_ids:
  - CHEBI:17630
  evidence_ids:
  - discovery
  - adopted
  - groundings
- assessment_id: provenance
  area: provenance
  topic: Source ownership and validation history
  outcome: supported
  summary: Original input hashes, deterministic source identities, chronological history
    and actual focused validators were checked; the failed initial authority comparison
    remains recorded.
  target_ids:
  - CHEBI:17630
  evidence_ids:
  - provenance
  - mapping
  - chemistry
findings:
- finding_id: F1
  issue_key: kanamycin-a-b-congener-and-sulfate-exact-aliases
  category: nomenclature
  severity: major
  status: open
  certainty: confirmed
  title: Two exact aliases denote a different congener or salt
  description: Native Aminodeoxykanamycin and Kanamycin sulfate are typed EXACT_SYNONYM.
    Official MeSH/KEGG identify the former with kanamycin B, with a different formula;
    the latter contains sulfate absent from the neutral A graph.
  target_ids:
  - CHEBI:17630
  field_paths:
  - synonyms[6]
  - synonyms[9]
  evidence_ids:
  - native
  - aliases
  - chemistry
  rule_id: Exact chemical scope and claim-level source support
  normalization_reason: Material exact-identity grounding errors in aliases; the separately
    supported native graph itself remains correct.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Source-concept-specific synonym exclusions
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO imported aliases
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Synonym policy and native enum generation
- finding_id: F2
  issue_key: kanamycin-a-chembl223520-stereoisomer-xref
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: The exact ChEMBL link resolves to a different stereoisomer
  description: Native xrefs[8] points to CHEMBL223520, whose current three encodings
    invert all five centers in one sugar ring. The native structure is supported;
    matching CHEMBL1384 provides a concrete candidate repair.
  target_ids:
  - CHEBI:17630
  field_paths:
  - xrefs[8]
  evidence_ids:
  - native
  - wrongxref
  - chemistry
  rule_id: Exact chemical scope and claim-level source support
  normalization_reason: Wrong exact cross-reference is major grounding; it does not
    invalidate the independently supported native structure.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Source-owned exact ChEMBL cross-reference
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO xref extraction and reconciliation
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible exact-xref seeding
- finding_id: F3
  issue_key: kanamycin-a-eis-whib7-inactivation-classification
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Eis and WhiB7 resistance are misclassified as target alteration
  description: Native resistance_mechanisms[64–66] normalize Eis and two WhiB7 mutation
    terms to ANTIBIOTIC_TARGET_ALTERATION through a generic ARO mutation ancestor.
    Original experiments instead demonstrate kanamycin acetylation/inactivation, regulated
    indirectly by WhiB7. The resistance associations remain valid; the normalized
    mechanism is wrong.
  target_ids:
  - CHEBI:17630
  field_paths:
  - resistance_mechanisms[64].mechanism_type
  - resistance_mechanisms[65].mechanism_type
  - resistance_mechanisms[66].mechanism_type
  evidence_ids:
  - mapping
  - eis
  - whib
  rule_id: Exact chemical scope and claim-level source support
  normalization_reason: Material mechanistic misclassification produced by a shared
    ancestor-based generator; database provenance does not remove the scientific conflict.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: ARO mechanism normalization policy
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Nearest-ancestor mechanism_for implementation
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Generated normalized mechanism and ancestor provenance
- finding_id: F4
  issue_key: kanamycin-a-kantrex-brand-type
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: Kantrex needs product-brand typing
  description: Native synonyms[12] marks the verified historical Kantrex product name
    EXACT_SYNONYM rather than BRAND_NAME.
  target_ids:
  - CHEBI:17630
  field_paths:
  - synonyms[12].synonym_type
  evidence_ids:
  - native
  - brand
  rule_id: Exact chemical scope and claim-level source support
  normalization_reason: Bounded product-alias typing defect, without changing native
    identity.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO product-alias source
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO synonym typing
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: BRAND NAME to BRAND_NAME mapping
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - CHEBI:17630
  description: Use the maintained source-specific synonym_exclusions policy for ARO:0000049
    to prevent Aminodeoxykanamycin and Kanamycin sulfate from entering exact A aliases.
    Preserve their valid B/salt records and conventional qualified drug context; do
    not globally ban the names.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: Source-concept-specific synonym exclusions
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO imported aliases
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Synonym policy and native enum generation
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Regenerated exact A aliases exclude both non-equivalent terms.
  - Native neutral structure and separately represented B/salt compounds remain unchanged.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - CHEBI:17630
  description: Correct the source-owned ARO chemical cross-reference through a reproducible
    extraction/reconciliation policy. Verify CHEMBL1384 against the native full graph
    and replace the incompatible exact CHEMBL223520 link; preserve the supported native
    stereochemistry.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Source-owned exact ChEMBL cross-reference
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO xref extraction and reconciliation
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Reproducible exact-xref seeding
  generator: scripts/extract_source_inventory.py and scripts/seed_from_sources.py
  acceptance_checks:
  - Chosen exact ChEMBL structure matches native by complete key and chirality-aware
    atom mapping.
  - Regeneration does not reintroduce CHEMBL223520 as exact A equivalence.
- action_id: A3
  finding_ids:
  - F3
  target_ids:
  - CHEBI:17630
  description: Add a narrow determinant-plus-antibiotic normalization correction in
    the maintained extraction/configuration path so these kanamycin edges describe
    ANTIBIOTIC_INACTIVATION, while retaining WhiB7 regulatory and mutation context
    and original database provenance. The existing mechanism_for loop checks ancestors,
    so simply adding determinant IDs to its current map would not work. Do not globally
    reclassify all mutation terms, call WhiB7 an acetyltransferase, or transfer Tap-mediated
    streptomycin efflux to kanamycin.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: conf/sources.yaml
    role: ARO mechanism normalization policy
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Nearest-ancestor mechanism_for implementation
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Generated normalized mechanism and ancestor provenance
  generator: scripts/extract_source_inventory.py
  acceptance_checks:
  - All three regenerated kanamycin mechanisms represent drug inactivation with regulator/context
    qualifications retained.
  - Other mutation and efflux edges are not changed by an overbroad ancestor override.
  - Meaningful focused generator checks and required schema, term/reference/history/corpus
    and full QC pass for eventual curation.
- action_id: A4
  finding_ids:
  - F4
  target_ids:
  - CHEBI:17630
  description: Preserve Kantrex as a historical product alias using source-owned BRAND
    NAME input typing or a reproducible equivalent policy that emits BRAND_NAME.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: ARO product-alias source
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: ARO synonym typing
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: BRAND NAME to BRAND_NAME mapping
  generator: scripts/extract_source_inventory.py and scripts/seed_from_sources.py
  acceptance_checks:
  - Kantrex is retained with BRAND_NAME and source provenance.
  - Product hydration/congener purity are not asserted from the historical name alone.
limitations:
- 'Read depth is explicit: six adopted leads, ninety current discovery records with
  eighty-five available abstracts, and selected original primary passages/actual tables.
  This is not a claim to have read ninety complete originals.'
- The 2009 Eis SI download was an HTML challenge despite its .pdf extension and is
  excluded. Exact kanamycin catalog/salt in the 2005/2009/2013 mechanism experiments
  remains unresolved; no universal genotype, clinical breakpoint or quantitative kinetic
  constant is inferred.
- Initial PMC challenge pages and failed XML/CARD/LINCS retrievals are recorded separately
  from successful primary HTML. DrugBank, Beilstein and Gmelin remain independently
  unresolved. A limited HMS archive absence does not prove a wrong LINCS mapping.
- Aspidium is repeated by the source but independently unresolved. Broader kanamycin
  naming and commercial mixtures do not invalidate the fully specified native A graph.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- Native records and maintained sources remain read-only. All thirteen original hashes
  are preserved within twenty-one verified inputs.
- Standalone chemistry used the 019 interpreter against 058; native schema/strict,
  ledger and contract used 058. The initial failed authority assertion is retained
  alongside the successful diagnostic run.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
