# Review of josamycin

- Review: 20261021T191254Z-josamycin-review
- Repository: CultureBotAI/AntibioticMech
- Started UTC: 2026-10-21T18:41:51Z
- Finished UTC: 2026-10-21T19:12:54Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The native josamycin/leucomycin A3 graph, macrolide class, antibacterial role and historical producer definition are supported. Two major grounding issues remain: a kitasamycin-complex source merge imports non-equivalent congeners and resistance assertions, and three other exact chemical cross-references encode conflicting constitution or stereochemistry. Preserve the valid native graph and repair source scope and exact links.

## Scope And Provenance

Entire exact native record, all asserted groundings, source provenance and adopted citation scope, with bounded primary activity and mechanism follow-up.

Selection: Initially uncovered queue position 569; original thirteen input hashes preserved and actual ChEBI/ARO, structure-enrichment and source-qualification owners appended before judgment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base baf3b3203d748d098686e166cdb2a6138f47eb59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:31739 | data/antibiotics/antibacterial/josamycin.yaml | generated | josamycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused chemistry verification | passed | False | CHEBI:31739 | Actual focused execution exited 0. |
| Focused schema verification | passed | True | CHEBI:31739 | Actual focused execution exited 0. |
| Focused strict verification | passed | True | CHEBI:31739 | Actual focused execution exited 0. |
| Independent authority verification | passed | False | CHEBI:31739 | Native/current encodings compared by full graph and mapped tetrahedral parity. Exact candidate CID5282165 agrees; conflicting components/epimers and PDB bond-order changes are explicit. |
| Independent ledger verification | passed | False | CHEBI:31739 | Twenty-one hashes, original thirteen preservation, four chronological history events, three deterministic mints, six current source edges and all lead dispositions verified. |
| Structured Pseudomonas gene discovery | passed | False | CHEBI:31739 | Actual free structured query completed before bacterial-mechanism web follow-up; catalog misses are not absence of biology. |
| Structured Pseudomonas gene discovery | passed | False | CHEBI:31739 | Actual free structured query completed before bacterial-mechanism web follow-up; catalog misses are not absence of biology. |
| Authoritative full QC | failed | True | CHEBI:31739 | Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack library cannot load. Pathway links, lint, documentation, provenance, source queue and curator structure gates passed before collection. This failure does not itself establish a scientific defect in the target. |
| Generated corpus reproduction | passed | True | CHEBI:31739 | 2939 expected and present; zero missing, unexpected, drifted fields or lockfile discrepancies. Unrelated iclaprim source-crossref refusal diagnostic retained. |
| Native review-readiness inventory | passed | False | CHEBI:31739 | 2859 native unsigned readiness rows written; this status queue does not determine structured-review coverage. |
| Supplementary test suite with two unavailable modules excluded | passed | False | CHEBI:31739 | 9455 passed and 248 skipped. Two modules requiring the unavailable SciPy native library were explicitly excluded; this does not replace full QC. |
| Full closed-schema validation | passed | True | CHEBI:31739 | 2939 files, zero ERROR rows. |
| Chemical map consistency | failed | False | CHEBI:31739 | Exited 1 on the same pinned SciPy native library import failure. |
| Generated site consistency | passed | False | CHEBI:31739 | 2939 compound pages and seven class pages current. |
| Corpus statistics | passed | False | CHEBI:31739 | Corpus report completed successfully. |
| Full-corpus history/evidence/reference invariants | passed | True | CHEBI:31739 | 23 full-corpus integrity tests passed, including seed history, evidence placement and internal references. |

## Scientific And Domain Assessments

### Exact josamycin/leucomycin A3 graph

identity: supported. Targets: CHEBI:31739.

The native graph and independent exact authorities agree, and original purification/identity work supports the constituent. Counterparts with altered acyl groups or stereochemistry do not justify changing this valid graph.

### Kitasamycin complex versus exact constituent

grounding: concern. Targets: CHEBI:31739.

The source merge conflates an explicitly defined multi-component antibiotic with one constituent and imports non-equivalent chemical identifiers and three source-scoped resistance claims.

### Other exact chemical links

grounding: concern. Targets: CHEBI:31739.

CID5284579, KNApSAcK C00018736 and CCD JOS fail exact graph/stereo equivalence. HMDB remains unresolved due access limits; drug/document links are assessed under their separate scope.

### Class, roles, historical producer and names

scope: supported. Targets: CHEBI:31739.

Structural parents and antibacterial role fit. Historical producer definition and leucomycin A3 identity are supported; uncommon historical aliases remain current-source-attributed with explicit limits.

### Exact josamycin versus imported mixture resistance

evidence: concern. Targets: CHEBI:31739.

Josamycin-specific23S evidence is supported within stated experimental limits. The three kitasamycin edges cannot be transferred solely through an invalid identity merge; this is not a claim that pure josamycin can never be affected by those determinants.

### Optional ribosome mechanism enrichment

completeness: unknown. Targets: CHEBI:31739.

Exact primary translation studies are discoverable, but original full methods were inaccessible here; structural deposition has a ligand-identity conflict. No mandatory new target is inferred from absence of a native object.

### Preserved source inputs and lead dispositions

provenance: supported. Targets: CHEBI:31739.

Twenty-one inputs, original thirteen preservation, mints, history and every adopted/current reference disposition were checked. All failures and read-depth limits are explicit.

## Findings

### F1: Kitasamycin complex is merged into exact josamycin

major / open / confirmed; issue key: josamycin-kitasamycin-complex-source-conflation.

Source concept ARO3001227 denotes kitasamycin, explicitly a mixture in official material authorities and distinct from leucomycin A3/josamycin in original chemistry. Its imported CHEMBL2106399 and CID5282189 graphs are different acylation states, and its ErmV/MexPQ-OpmE/MuxABC-OpmB assertions are transferred through that invalid merge. Database-assertion wording does not establish exact constituent scope. The valid native josamycin identity remains supported.

### F2: Three additional exact chemical xrefs encode conflicting structures

major / open / confirmed; issue key: josamycin-exact-xref-stereo-and-diene-conflicts.

CID5284579 has one unassigned native centre plus a mapped mycarose epimer; KNApSAcK C00018736 has incompatible/InChI-versus-SMILES stereochemistry and an inconsistent displayed key; CCD JOS shifts the native macrocycle diene. These links do not meet exact chemical equivalence even though their labels say josamycin. CID5282165 matches the native graph as a concrete replacement candidate for the PubChem link.

## Recommended Actions And Acceptance Checks

### A1

Add an evidence-backed source-specific EXCLUDE decision for kitasamycin ARO3001227/mint antibioticmech:aro-0c5d9c9627 using the existing maintained decision mechanism, or correct the upstream concept scope before any future exact mapping. Preserve raw source provenance and exact josamycin/leucomycin A3. Reseed so the mixture source, two non-equivalent chemical IDs and its three transferred assertions no longer enter solely by that merge. Reintroduce any of those resistance determinants only after independent exact-josamycin material/evidence verification; this action does not declare their biological effects impossible.

- Pure josamycin retains CHEBI31739 and full key XJSFLOJWULLJQS-NGVXBBESSA-N.
- Mixture source remains traceable as excluded and does not import its different-congener IDs or automatic exact-constituent resistance assertions.
- All retained or newly adopted resistance claims state tested material, organism, construct and endpoint.
- Regeneration plus schema/strict, reference/history/corpus and full QC pass.

### A2

Correct the source-owned PubChem link to verified candidate CID5282165 with full-graph provenance, and withhold KNApSAcK C00018736 and CCD JOS from exact xrefs until their structures are reconciled upstream or an explicit reviewed source correction is implemented. A PDB deposition may remain a separately scoped scientific reference after ligand evaluation; do not move mismatching structures into drug_xrefs merely to evade equality. Regenerate and verify complete graph/stereo equivalence without changing the supported native structure.

- Every emitted exact chemical xref resolves to native constitution and configured stereochemistry, or is withheld with explicit provenance.
- PubChem replacement is CID5282165 with matching full key and atom-mapped stereo; no blanket rewrite of unrelated PubChem identifiers.
- KNApSAcK internal disagreements and CCD diene bond-order mismatch are explicitly resolved before exact-link restoration.
- Required focused and shared source/reference/history/corpus/QC gates pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/antibiotics/antibacterial/josamycin.yaml; Entire native record, twelve aliases, eight parents, two roles, eleven chemical xrefs, three drug links, document link, three source concepts, six resistance assertions and four history events | supports | The SEEDED/EXACT record has a valid fully configured josamycin graph. It merges josamycin ARO3001221 with kitasamycin ARO3001227. Three resistance entries explicitly cite the latter source, while three cite josamycin. No molecular-target, quantitative MIC, clinical, structured producer or causal-graph object is natively asserted. Definition-level production by S. narbonensis var. josamyceticus is assessed independently. |
| chemistry | CHEBI:31739;CHEMBL224436;KEGG:C12662;KEGG:D01235;pubchem.compound:5282165; 569-authority-chemistry.json and persistent569-authority-check.py; native/current ChEBI, ChEMBL and KEGG snapshots plus exact-key PubChem lookup | supports | Eleven encodings across the native graph, ChEBI, exact ChEMBL, KEGG and candidate CID5282165 agree at XJSFLOJWULLJQS-NGVXBBESSA-N and C42H69NO15, charge 0. Native graph and masses are internally valid. Exact-key lookup provides a concrete PubChem replacement candidate. Graph matching uses atom mappings and chirality, not raw@ symbols or isolated CIP labels. |
| identity-primary | PMID:5482762;DOI:10.7164/antibiotics.23.511; 569-primary1970.pdf, entire pp511–513; actual p512 structure panel and comparison text;569-fetch2.json | supports | The original comparison identifies purified josamycin with leucomycin A3 by TLC, IR, UV and NMR. It separately describes kitasamycin/leucomycin as a complex with multiple isolated active components. Minor components in the starting josamycin tablet extract were removed before the comparison; this does not redefine the exact named constituent as the entire complex. The historical S. narbonensis var. josamyceticus producer is stated. |
| component-primary | DOI:10.7164/antibiotics.21.532; 569-primary1968.pdf; introduction, isolated-material preparation, assay methods, Table1 and comparative Results | supports | Original work separates leucomycins A1/A3–A9 by chromatography and tests them individually. The lactone3-OH versus3-O-acetyl and mycarose4-O-acyl substituents distinguish congeners; A3 has acetate plus isovalerate. The exact A3 panel supports antibacterial activity. Agar-dilution MIC and cup-assay potency are separate endpoints, and values from other congeners or the bulk complex are not transferred. |
| official-mixture | Japanese Pharmacopoeia XV;GSRS:G986N7X02W; 569-jp-kitasamycin.pdf printed pp786–787 and798; actual josamycin p786 drawing/nomenclature viewed;569-gsrs-api.json;569-fetch2.json/569-fetch3.json | supports | The official monograph defines josamycin with C42H69NO15, its stereochemical name, CAS16846-24-5 and historical producer. Kitasamycin is expressly a mixture of macrolides, with controlled component ratios and potency referenced to leucomycin A5. Current GSRS likewise types kitasamycin as mixture and lists josamycin among multiple component substances. These are explicit material definitions, not an inference from unspecified stereochemistry. |
| wrong-congeners | chembl:CHEMBL2106399;pubchem.compound:5282189;ARO:3001227; 569-chembl-2106399.json;569-pubchem-5282189.json;569-authority-chemistry.json;569-aro-blocks.json | supports | The imported kitasamycin ChEMBL graph is C40H67NO14/keyIEMDOFXTVAPVLX-YWQHLDGFSA-N and lacks the native lactone acetate. The imported PubChem graph is C35H59NO13/keyXYJOGTQLTFNMQG-KJHBSLKPSA-N and lacks both native acyl substituents. Neither is exact C42H69NO15 josamycin. Current ARO repeats the mixture-to-CHEBI mapping, so upstream repetition explains the merge without making it valid. |
| wrong-pubchem | pubchem.compound:5284579; 569-pubchem-5284579.json;569-authority-chemistry.json mapped atom/parity experiment | supports | CID5284579 has the same constitution but leaves native atom 2, the methoxy-bearing macrolide carbon, unassigned and inverts native atom 16, the mycarose ester-bearing carbon, from native S to R. Clearing the first tag and inverting the second reproduces the authority graph under reciprocal chirality matching. This is a specific stereochemical mismatch, not a claim that unspecified stereo implies a mixture. CandidateCID5282165 matches all native centres. |
| wrong-knapsack | knapsack:C00018736; 569-knapsack.html current InChI/SMILES/displayed-key fields;569-authority-chemistry.json | supports | The current KNApSAcK InChI has three mapped tetrahedral inversions at native atoms 7/24/27; the corresponding parity edits reproduce that graph. Its SMILES instead leaves atoms 7/24/31 unspecified, and its displayed InChIKey differs from the key calculated from its own InChI. This internally conflicting entry cannot currently serve as exact chemical equivalence. The compound name/CAS and producer metadata remain source observations, not proof of a matching graph. |
| wrong-pdb | pdb-ccd:JOS;PDB:2O44; 569-pdb-JOS.cif descriptor block;569-pdb-2O44.json;569-authority-chemistry.json atom-skeleton comparison | supports | CCD JOS encodes the same atom skeleton/formula but moves the macrocycle diene bond orders, producing PDCICSSHRGGICK-BVVLUKMUSA-N. The skeleton comparison locates four changed bond orders; no tautomer or raw-stereo-symbol explanation is assumed. The linked 2O44 structural deposition is labelled josamycin and concerns D. radiodurans large-subunit binding, but its primary citation is TO BE PUBLISHED. A relevant deposition name does not make the mismatching CCD chemical graph exact; structural evidence can be assessed separately after ligand reconciliation. |
| other-links | CAS:16846-24-5;HMDB0015418;DrugCentral:1518;DrugBank:DB01321;Wikipedia.en:Josamycin; 569-jp-kitasamycin.pdf;569-drugcentral.html;569-wikipedia.html;569-fetch.json/569-fetch3.json; official indexed HMDB excerpt | supports | CAS and exact josamycin identity are supported by the official monograph. Current DrugCentral names josamycin and leucomycin A3 at drug 1518; KEGG D01235 also resolves as drug context. DrugBank and direct HMDB HTML/XML/SDF requests returned 403. The indexed official HMDB excerpt links josamycin to candidate CID5282165 but does not replace an independent exact-graph read. Wikipedia was inspected as the asserted document, not primary scientific support. Drug-level namespaces are not forced into chemical-equivalence semantics. |
| terms | CHEBI:17478;24400;25105;26878;47622;50996;63353;33281;36047;ARO:0000000; 569-chebi-*.json exact definitions and current569-aro-blocks.json | supports | Aldehyde, glycoside, macrolide, tertiary alcohol, acetate ester, tertiary amino compound and disaccharide-derivative parents fit the valid graph. Antimicrobial and antibacterial-drug roles fit the exact compound and official monograph. All twelve source aliases were checked against current ChEBI; the original independently establishes leucomycin A3, while rare EN-141/YL-704/turimycin aliases remain authority-attributed rather than claimed individually proven from original historical papers. |
| pneumococcus | PMID:11120988;DOI:10.1128/AAC.45.1.319-323.2001; 569-PMC90283.html; original susceptibility methods, actual Table2, rrl/L4 transformation Results | supports | The original S. pneumoniae study gives josamycin MIC 0.125 micrograms/mL for CP1000 and 32 for rrlA2062C transformants BM4456/BM4457; donor BM4455 is 64. Transformation and sequencing distinguish the four-copy 23S change from the donor L4 substitution. The assay uses MH/horse-blood agar, 10^4 CFU/spot, 24 h at 37°C with 5% CO2. This supports the native qualified target-alteration relation in that experimental context, not a universal mutation outcome. |
| chlamydia | PMID:15047540;PMID:26622462; 569-PMC375314.html and569-PMC4533178.html selected original methods, Results/Tables and Discussion | supports | Original clinical C. trachomatis cultures show mixed populations with 23S changes and reduced josamycin susceptibility; endpoints are absence of inclusions in infected McCoy cells and, separately, passage-defined MBC. Later serial-exposure experiments show heterogeneous mutation patterns and some resistant isolates lacking 23S changes. These support bounded association and experimental selection, not a universal causal genotype, accepted clinical breakpoint or proof that all reported Chlamydia species share the same target mutation. |
| mechanism | PMID:15385552;PMID:19463886; Complete original abstracts in569-discovery.json; direct2004 JBC PDF request403 in569-fetch4.json | supports | Exact josamycin studies use a pure-component E. coli translation system and examine ribosome binding, sequence-dependent early peptide-bond inhibition and peptidyl-tRNA drop-off. The 2009 study further distinguishes peptide-mediated resistance from drug ejection and implicates tRNA-pool effects. These provide optional exact primary enrichment leads; full original mains were not inspected and no quantitative target object is added. The native absence of a target is not itself treated as a defect. |
| leads | Five adopted and fifteen current ARO PMID records; 569-adopted-core.json;569-current-core.json;569-source-audit.json per-PMID dispositions | supports | All five adopted records and fifteen current MED records were resolved. Three adopted and fourteen current complete available abstracts were read; adopted 5482762 has no abstract but full original was read, while 6072799 remains metadata-only after failed original retrieval. Analytical impurity/chromatography papers are not mechanism assays. PMID 1838760 separately tests josamycin and kitasamycin without enhanced serum killing; that endpoint is not general antibacterial inactivity. ErmW/myrB is not confused with the separate negative myrA result; C. psittaci23S and C. trachomatisL4 findings remain distinct. |
| owners | ChEBI/ARO extraction, exact source merge and maintained exclusion decisions; 569-source-audit.json;569-raw-rows.json;569-owners-search.json;curation/decisions.tsv;conf/sources.yaml;scripts/seed_from_sources.py | supports | Original thirteen hashes are unchanged within twenty-one inputs. Four chronological history events and three deterministic mints verify. Raw ARO3001227 supplies CHEBI31739 plus the two different-congener IDs; the resulting merged record imports its three resistance assertions. Existing source-specific EXCLUDE decisions preserve excluded mixture provenance without emitting it as an exact compound. No generic xref-exclusion configuration is assumed to exist. |
| search | Public exact-identifier/primary search and structured bacterial adapter; 569-owners-search.json;569-adapter-results.json;569-discovery.json;569-fetch1–4 manifests as actually named569-fetch.json through569-fetch4.json | supports | Ignored-inclusive local searches traced actual owners and aliases. P. aeruginosa precise364 mexP/muxA queries returned no matches before web follow-up; this is a catalog limit. Public discovery returned 133 records, with 100 fetched as leads, not an exhaustive full-main audit. Original1967 guessed routes returned 404; MexPQ/MuxABC, JBC and inaccessible authority routes are recorded rather than treated as read. |

## Limits And Additional Notes

- The original 1967 biological source 6072799 has no indexed abstract and its guessed J-STAGE routes returned 404. The complete 1970 identity paper and selected 1968 exact-congener activity passages were read; they are not misrepresented as the unread1967 experiments.
- Direct HMDB HTML/XML/SDF and DrugBank requests returned 403. Official indexed HMDB text was inspected only at that depth; exact HMDB graph remains unresolved. Drug-level links have separate semantics from chemical xrefs.
- All adopted/current available abstracts were read, with selected native-resistance mains at the stated depth. MexPQ/MuxABC publisher mains returned 403 and exact kitasamycin assay composition remains unresolved. The mixture finding does not prove absence of a josamycin effect.
- KNApSAcK contains conflicting representations; mapped inversions and unspecified centres are described separately. Undefined stereo alone is not a mixture claim. The PDB component mismatch concerns deposited chemical topology, not a blanket rejection of ribosome binding.
- The original 2004 JBC translation paper returned 403; complete original abstract supports an optional mechanism lead, with no quantitative target object or universal lethal mechanism adopted. PDB2O44 primary citation remains unpublished in its metadata.
- Rare historical aliases beyond leucomycin A3 were corroborated at current-authority depth, not each through an original isolation report. No current taxonomic reidentification of the historical producer is asserted.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an invalid Mach-O section on this platform; the same version also failed under Python 3.10 and in the fresh batch-002 environment. No dependency versions were changed. The supplementary test suite, closed-schema, reproduction and corpus-integrity checks do not replace full QC.
- All original thirteen inputs remain byte-identical within twenty-one verified captured inputs. No native record, source inventory, saved bundle, Git or progress state was edited.
- Chemistry used the 019 interpreter against 057; schema, strict, ledger and contract used 057. This is a stable scratch handoff for root audit and ordered saving.
- Bundle completion is partial because full repository QC is unavailable on this runtime; the selected record was read and assessed in full. A saved review does not promote native scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T191254Z-josamycin-review
kind: record
repository: CultureBotAI/AntibioticMech
title: Review of josamycin
started_at: '2026-10-21T18:41:51Z'
finished_at: '2026-10-21T19:12:54Z'
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
summary: 'The native josamycin/leucomycin A3 graph, macrolide class, antibacterial
  role and historical producer definition are supported. Two major grounding issues
  remain: a kitasamycin-complex source merge imports non-equivalent congeners and
  resistance assertions, and three other exact chemical cross-references encode conflicting
  constitution or stereochemistry. Preserve the valid native graph and repair source
  scope and exact links.'
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
  - path: data/antibiotics/antibacterial/josamycin.yaml
    sha256: a167baa7f81ecc83559408a7f5349b5b01cc7fe6559d8353302ae6f5c23b8480
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
- target_id: CHEBI:31739
  path: data/antibiotics/antibacterial/josamycin.yaml
  label: josamycin
  record_class: AntibioticRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: Exact ChEBI identity, structure, names and adopted leads
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Both ARO identity source concepts
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Six resistance database assertions
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_target_edges.tsv
    role: Check target-source presence or absence
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/pubchem_structures.tsv
    role: PubChem structure support
  - repository: CultureBotAI/AntibioticMech
    path: scripts/enrich_pubchem_structures.py
    role: Source structure enrichment owner
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Actual ChEBI and CARD/ARO extraction
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
  selection: Initially uncovered queue position 569; original thirteen input hashes
    preserved and actual ChEBI/ARO, structure-enrichment and source-qualification
    owners appended before judgment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:31739
checks:
- check_id: chemistry
  name: Focused chemistry verification
  status: passed
  required: false
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:31739
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/focus021-root.py
    569
  exit_code: 0
  expected_exit_code: 0
- check_id: schema
  name: Focused schema verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:31739
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate
    data/antibiotics/antibacterial/josamycin.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: strict
  name: Focused strict verification
  status: passed
  required: true
  summary: Actual focused execution exited 0.
  target_ids:
  - CHEBI:31739
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just validate-strict
    data/antibiotics/antibacterial/josamycin.yaml --out /private/tmp/am-review-session/569-strict.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: authority
  name: Independent authority verification
  command: /private/tmp/antibioticmech-record-reviews-019/.venv/bin/python /private/tmp/am-review-session/569-authority-check.py
    > /private/tmp/am-review-session/569-authority-check.log 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Native/current encodings compared by full graph and mapped tetrahedral
    parity. Exact candidate CID5282165 agrees; conflicting components/epimers and
    PDB bond-order changes are explicit.
  target_ids:
  - CHEBI:31739
- check_id: ledger
  name: Independent ledger verification
  command: .venv/bin/python /private/tmp/am-review-session/569-ledger.py > /private/tmp/am-review-session/569-ledger.log
    2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Twenty-one hashes, original thirteen preservation, four chronological history
    events, three deterministic mints, six current source edges and all lead dispositions
    verified.
  target_ids:
  - CHEBI:31739
- check_id: adapter-0
  name: Structured Pseudomonas gene discovery
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism p_aeruginosa --dataset precise364 --query
    mexP > /private/tmp/am-review-session/569-adapter-p_aeruginosa-mexP.txt 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Actual free structured query completed before bacterial-mechanism web follow-up;
    catalog misses are not absence of biology.
  target_ids:
  - CHEBI:31739
- check_id: adapter-1
  name: Structured Pseudomonas gene discovery
  command: env PYTHONDONTWRITEBYTECODE=1 /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb --timeout 15 search --organism p_aeruginosa --dataset precise364 --query
    muxA > /private/tmp/am-review-session/569-adapter-p_aeruginosa-muxA.txt 2>&1
  status: passed
  required: false
  exit_code: 0
  expected_exit_code: 0
  summary: Actual free structured query completed before bacterial-mechanism web follow-up;
    catalog misses are not absence of biology.
  target_ids:
  - CHEBI:31739
- check_id: shared-qc
  name: Authoritative full QC
  status: failed
  required: true
  summary: 'Exited 2 at pytest collection: pinned SciPy 1.15.3 native Mach-O _spropack
    library cannot load. Pathway links, lint, documentation, provenance, source queue
    and curator structure gates passed before collection. This failure does not itself
    establish a scientific defect in the target.'
  target_ids:
  - CHEBI:31739
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
  - CHEBI:31739
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
  - CHEBI:31739
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
  - CHEBI:31739
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
  - CHEBI:31739
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
  - CHEBI:31739
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
  - CHEBI:31739
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
  - CHEBI:31739
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
  - CHEBI:31739
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/am-review-uv-cache just test
    -q tests/test_corpus_integrity.py
  exit_code: 0
  scope_note: Shared execution in /private/tmp/antibioticmech-record-reviews-20261021
    on base baf3b3203d748d098686e166cdb2a6138f47eb59. Corpus and gate inputs are unchanged
    in this isolated worktree; the check applies to this target within all 2939 records.
evidence:
- evidence_id: native
  kind: record_content
  reference: data/antibiotics/antibacterial/josamycin.yaml
  locator: Entire native record, twelve aliases, eight parents, two roles, eleven
    chemical xrefs, three drug links, document link, three source concepts, six resistance
    assertions and four history events
  accessed_at: '2026-10-21T18:57:33Z'
  support: supports
  summary: The SEEDED/EXACT record has a valid fully configured josamycin graph. It
    merges josamycin ARO3001221 with kitasamycin ARO3001227. Three resistance entries
    explicitly cite the latter source, while three cite josamycin. No molecular-target,
    quantitative MIC, clinical, structured producer or causal-graph object is natively
    asserted. Definition-level production by S. narbonensis var. josamyceticus is
    assessed independently.
- evidence_id: chemistry
  kind: validation
  reference: CHEBI:31739;CHEMBL224436;KEGG:C12662;KEGG:D01235;pubchem.compound:5282165
  locator: 569-authority-chemistry.json and persistent569-authority-check.py; native/current
    ChEBI, ChEMBL and KEGG snapshots plus exact-key PubChem lookup
  accessed_at: '2026-10-21T18:57:33Z'
  support: supports
  summary: Eleven encodings across the native graph, ChEBI, exact ChEMBL, KEGG and
    candidate CID5282165 agree at XJSFLOJWULLJQS-NGVXBBESSA-N and C42H69NO15, charge
    0. Native graph and masses are internally valid. Exact-key lookup provides a concrete
    PubChem replacement candidate. Graph matching uses atom mappings and chirality,
    not raw@ symbols or isolated CIP labels.
  snapshot_sha256: 2a878eb50d4eb344079f2e483ac413bcdd12fbdb73e40cc23b249cb490a17e60
- evidence_id: identity-primary
  kind: primary_source
  reference: PMID:5482762;DOI:10.7164/antibiotics.23.511
  locator: 569-primary1970.pdf, entire pp511–513; actual p512 structure panel and
    comparison text;569-fetch2.json
  accessed_at: '2026-10-21T18:57:33Z'
  support: supports
  summary: The original comparison identifies purified josamycin with leucomycin A3
    by TLC, IR, UV and NMR. It separately describes kitasamycin/leucomycin as a complex
    with multiple isolated active components. Minor components in the starting josamycin
    tablet extract were removed before the comparison; this does not redefine the
    exact named constituent as the entire complex. The historical S. narbonensis var.
    josamyceticus producer is stated.
  snapshot_sha256: a38299690ed5e142f55303b5cc528b772936c9afadf33350f0acf8d452fa2e6e
- evidence_id: component-primary
  kind: primary_source
  reference: DOI:10.7164/antibiotics.21.532
  locator: 569-primary1968.pdf; introduction, isolated-material preparation, assay
    methods, Table1 and comparative Results
  accessed_at: '2026-10-21T18:57:33Z'
  support: supports
  summary: Original work separates leucomycins A1/A3–A9 by chromatography and tests
    them individually. The lactone3-OH versus3-O-acetyl and mycarose4-O-acyl substituents
    distinguish congeners; A3 has acetate plus isovalerate. The exact A3 panel supports
    antibacterial activity. Agar-dilution MIC and cup-assay potency are separate endpoints,
    and values from other congeners or the bulk complex are not transferred.
  snapshot_sha256: 62d056bc125404cabdf2263317fe9ab1a429cbc483d8402e6d9c9988ac32210d
- evidence_id: official-mixture
  kind: authority
  reference: Japanese Pharmacopoeia XV;GSRS:G986N7X02W
  locator: 569-jp-kitasamycin.pdf printed pp786–787 and798; actual josamycin p786
    drawing/nomenclature viewed;569-gsrs-api.json;569-fetch2.json/569-fetch3.json
  accessed_at: '2026-10-21T18:57:33Z'
  support: supports
  summary: The official monograph defines josamycin with C42H69NO15, its stereochemical
    name, CAS16846-24-5 and historical producer. Kitasamycin is expressly a mixture
    of macrolides, with controlled component ratios and potency referenced to leucomycin
    A5. Current GSRS likewise types kitasamycin as mixture and lists josamycin among
    multiple component substances. These are explicit material definitions, not an
    inference from unspecified stereochemistry.
  snapshot_sha256: 73d687b0d926ce95e87181529e74fb7f9da9b9b1a5b1011c8b19a5a9bb6c7087
- evidence_id: wrong-congeners
  kind: authority
  reference: chembl:CHEMBL2106399;pubchem.compound:5282189;ARO:3001227
  locator: 569-chembl-2106399.json;569-pubchem-5282189.json;569-authority-chemistry.json;569-aro-blocks.json
  accessed_at: '2026-10-21T18:57:33Z'
  support: supports
  summary: The imported kitasamycin ChEMBL graph is C40H67NO14/keyIEMDOFXTVAPVLX-YWQHLDGFSA-N
    and lacks the native lactone acetate. The imported PubChem graph is C35H59NO13/keyXYJOGTQLTFNMQG-KJHBSLKPSA-N
    and lacks both native acyl substituents. Neither is exact C42H69NO15 josamycin.
    Current ARO repeats the mixture-to-CHEBI mapping, so upstream repetition explains
    the merge without making it valid.
  snapshot_sha256: 2a878eb50d4eb344079f2e483ac413bcdd12fbdb73e40cc23b249cb490a17e60
- evidence_id: wrong-pubchem
  kind: authority
  reference: pubchem.compound:5284579
  locator: 569-pubchem-5284579.json;569-authority-chemistry.json mapped atom/parity
    experiment
  accessed_at: '2026-10-21T18:57:33Z'
  support: supports
  summary: CID5284579 has the same constitution but leaves native atom 2, the methoxy-bearing
    macrolide carbon, unassigned and inverts native atom 16, the mycarose ester-bearing
    carbon, from native S to R. Clearing the first tag and inverting the second reproduces
    the authority graph under reciprocal chirality matching. This is a specific stereochemical
    mismatch, not a claim that unspecified stereo implies a mixture. CandidateCID5282165
    matches all native centres.
  snapshot_sha256: 2f1edf35f2fc6c27a4488ef9a7373f6341e5a3ab49ef61a13e0bf22f5be164f1
- evidence_id: wrong-knapsack
  kind: authority
  reference: knapsack:C00018736
  locator: 569-knapsack.html current InChI/SMILES/displayed-key fields;569-authority-chemistry.json
  accessed_at: '2026-10-21T18:57:33Z'
  support: supports
  summary: The current KNApSAcK InChI has three mapped tetrahedral inversions at native
    atoms 7/24/27; the corresponding parity edits reproduce that graph. Its SMILES
    instead leaves atoms 7/24/31 unspecified, and its displayed InChIKey differs from
    the key calculated from its own InChI. This internally conflicting entry cannot
    currently serve as exact chemical equivalence. The compound name/CAS and producer
    metadata remain source observations, not proof of a matching graph.
  snapshot_sha256: 2eae871cc4c7a744874792072c2bc9f3b99bac52a992c855164973141393bfd8
- evidence_id: wrong-pdb
  kind: authority
  reference: pdb-ccd:JOS;PDB:2O44
  locator: 569-pdb-JOS.cif descriptor block;569-pdb-2O44.json;569-authority-chemistry.json
    atom-skeleton comparison
  accessed_at: '2026-10-21T18:57:33Z'
  support: supports
  summary: CCD JOS encodes the same atom skeleton/formula but moves the macrocycle
    diene bond orders, producing PDCICSSHRGGICK-BVVLUKMUSA-N. The skeleton comparison
    locates four changed bond orders; no tautomer or raw-stereo-symbol explanation
    is assumed. The linked 2O44 structural deposition is labelled josamycin and concerns
    D. radiodurans large-subunit binding, but its primary citation is TO BE PUBLISHED.
    A relevant deposition name does not make the mismatching CCD chemical graph exact;
    structural evidence can be assessed separately after ligand reconciliation.
  snapshot_sha256: 436fe0f62119711698021f742f4494e60c28579d3ad45b85ce27d6be01bc7bc3
- evidence_id: other-links
  kind: authority
  reference: CAS:16846-24-5;HMDB0015418;DrugCentral:1518;DrugBank:DB01321;Wikipedia.en:Josamycin
  locator: 569-jp-kitasamycin.pdf;569-drugcentral.html;569-wikipedia.html;569-fetch.json/569-fetch3.json;
    official indexed HMDB excerpt
  accessed_at: '2026-10-21T18:57:33Z'
  support: supports
  summary: CAS and exact josamycin identity are supported by the official monograph.
    Current DrugCentral names josamycin and leucomycin A3 at drug 1518; KEGG D01235
    also resolves as drug context. DrugBank and direct HMDB HTML/XML/SDF requests
    returned 403. The indexed official HMDB excerpt links josamycin to candidate CID5282165
    but does not replace an independent exact-graph read. Wikipedia was inspected
    as the asserted document, not primary scientific support. Drug-level namespaces
    are not forced into chemical-equivalence semantics.
  snapshot_sha256: d2d3f9c095c76803efe2fac20658a492c47a2ac77d38001bdc1ac8c0d587bed0
- evidence_id: terms
  kind: authority
  reference: CHEBI:17478;24400;25105;26878;47622;50996;63353;33281;36047;ARO:0000000
  locator: 569-chebi-*.json exact definitions and current569-aro-blocks.json
  accessed_at: '2026-10-21T18:57:33Z'
  support: supports
  summary: Aldehyde, glycoside, macrolide, tertiary alcohol, acetate ester, tertiary
    amino compound and disaccharide-derivative parents fit the valid graph. Antimicrobial
    and antibacterial-drug roles fit the exact compound and official monograph. All
    twelve source aliases were checked against current ChEBI; the original independently
    establishes leucomycin A3, while rare EN-141/YL-704/turimycin aliases remain authority-attributed
    rather than claimed individually proven from original historical papers.
  snapshot_sha256: 55d84dd0073972541568f293f1c919a7f7054e9de43221cd38adcf96382b5f90
- evidence_id: pneumococcus
  kind: primary_source
  reference: PMID:11120988;DOI:10.1128/AAC.45.1.319-323.2001
  locator: 569-PMC90283.html; original susceptibility methods, actual Table2, rrl/L4
    transformation Results
  accessed_at: '2026-10-21T18:57:33Z'
  support: supports
  summary: The original S. pneumoniae study gives josamycin MIC 0.125 micrograms/mL
    for CP1000 and 32 for rrlA2062C transformants BM4456/BM4457; donor BM4455 is 64.
    Transformation and sequencing distinguish the four-copy 23S change from the donor
    L4 substitution. The assay uses MH/horse-blood agar, 10^4 CFU/spot, 24 h at 37°C
    with 5% CO2. This supports the native qualified target-alteration relation in
    that experimental context, not a universal mutation outcome.
  snapshot_sha256: 5b2b59503b72301198681c3cd1b61103bba781e44fe89093e333ed4b0987e3f2
- evidence_id: chlamydia
  kind: primary_source
  reference: PMID:15047540;PMID:26622462
  locator: 569-PMC375314.html and569-PMC4533178.html selected original methods, Results/Tables
    and Discussion
  accessed_at: '2026-10-21T18:57:33Z'
  support: supports
  summary: Original clinical C. trachomatis cultures show mixed populations with 23S
    changes and reduced josamycin susceptibility; endpoints are absence of inclusions
    in infected McCoy cells and, separately, passage-defined MBC. Later serial-exposure
    experiments show heterogeneous mutation patterns and some resistant isolates lacking
    23S changes. These support bounded association and experimental selection, not
    a universal causal genotype, accepted clinical breakpoint or proof that all reported
    Chlamydia species share the same target mutation.
  snapshot_sha256: 5fed438085bea9740d40ff2ce1fda9591f4fe07d3619475f5a21ed0af7c01e77
- evidence_id: mechanism
  kind: primary_source
  reference: PMID:15385552;PMID:19463886
  locator: Complete original abstracts in569-discovery.json; direct2004 JBC PDF request403
    in569-fetch4.json
  accessed_at: '2026-10-21T18:57:33Z'
  support: supports
  summary: Exact josamycin studies use a pure-component E. coli translation system
    and examine ribosome binding, sequence-dependent early peptide-bond inhibition
    and peptidyl-tRNA drop-off. The 2009 study further distinguishes peptide-mediated
    resistance from drug ejection and implicates tRNA-pool effects. These provide
    optional exact primary enrichment leads; full original mains were not inspected
    and no quantitative target object is added. The native absence of a target is
    not itself treated as a defect.
  snapshot_sha256: a7dd5d7bf40b4bf3fe99e2c553a01e75d5883e4f9df77f6b9072a0d70258db84
- evidence_id: leads
  kind: database
  reference: Five adopted and fifteen current ARO PMID records
  locator: 569-adopted-core.json;569-current-core.json;569-source-audit.json per-PMID
    dispositions
  accessed_at: '2026-10-21T18:57:33Z'
  support: supports
  summary: All five adopted records and fifteen current MED records were resolved.
    Three adopted and fourteen current complete available abstracts were read; adopted
    5482762 has no abstract but full original was read, while 6072799 remains metadata-only
    after failed original retrieval. Analytical impurity/chromatography papers are
    not mechanism assays. PMID 1838760 separately tests josamycin and kitasamycin
    without enhanced serum killing; that endpoint is not general antibacterial inactivity.
    ErmW/myrB is not confused with the separate negative myrA result; C. psittaci23S
    and C. trachomatisL4 findings remain distinct.
  snapshot_sha256: d2d3f9c095c76803efe2fac20658a492c47a2ac77d38001bdc1ac8c0d587bed0
- evidence_id: owners
  kind: validation
  reference: ChEBI/ARO extraction, exact source merge and maintained exclusion decisions
  locator: 569-source-audit.json;569-raw-rows.json;569-owners-search.json;curation/decisions.tsv;conf/sources.yaml;scripts/seed_from_sources.py
  accessed_at: '2026-10-21T18:57:33Z'
  support: supports
  summary: Original thirteen hashes are unchanged within twenty-one inputs. Four chronological
    history events and three deterministic mints verify. Raw ARO3001227 supplies CHEBI31739
    plus the two different-congener IDs; the resulting merged record imports its three
    resistance assertions. Existing source-specific EXCLUDE decisions preserve excluded
    mixture provenance without emitting it as an exact compound. No generic xref-exclusion
    configuration is assumed to exist.
  snapshot_sha256: d2d3f9c095c76803efe2fac20658a492c47a2ac77d38001bdc1ac8c0d587bed0
- evidence_id: search
  kind: search
  reference: Public exact-identifier/primary search and structured bacterial adapter
  locator: 569-owners-search.json;569-adapter-results.json;569-discovery.json;569-fetch1–4
    manifests as actually named569-fetch.json through569-fetch4.json
  accessed_at: '2026-10-21T18:57:33Z'
  support: supports
  summary: Ignored-inclusive local searches traced actual owners and aliases. P. aeruginosa
    precise364 mexP/muxA queries returned no matches before web follow-up; this is
    a catalog limit. Public discovery returned 133 records, with 100 fetched as leads,
    not an exhaustive full-main audit. Original1967 guessed routes returned 404; MexPQ/MuxABC,
    JBC and inaccessible authority routes are recorded rather than treated as read.
  search_scope: All exact native chemical/drug/document identifiers, all adopted/current
    cited MED records, original josamycin/leucomycin identity/activity and selected
    native resistance evidence, plus ignored-inclusive local source/owner searches.
  snapshot_sha256: d2d3f9c095c76803efe2fac20658a492c47a2ac77d38001bdc1ac8c0d587bed0
assessments:
- assessment_id: identity
  area: identity
  topic: Exact josamycin/leucomycin A3 graph
  outcome: supported
  summary: The native graph and independent exact authorities agree, and original
    purification/identity work supports the constituent. Counterparts with altered
    acyl groups or stereochemistry do not justify changing this valid graph.
  target_ids:
  - CHEBI:31739
  evidence_ids:
  - native
  - chemistry
  - identity-primary
  - component-primary
  - official-mixture
- assessment_id: merge
  area: grounding
  topic: Kitasamycin complex versus exact constituent
  outcome: concern
  summary: The source merge conflates an explicitly defined multi-component antibiotic
    with one constituent and imports non-equivalent chemical identifiers and three
    source-scoped resistance claims.
  target_ids:
  - CHEBI:31739
  evidence_ids:
  - native
  - identity-primary
  - official-mixture
  - wrong-congeners
  - owners
- assessment_id: xref
  area: grounding
  topic: Other exact chemical links
  outcome: concern
  summary: CID5284579, KNApSAcK C00018736 and CCD JOS fail exact graph/stereo equivalence.
    HMDB remains unresolved due access limits; drug/document links are assessed under
    their separate scope.
  target_ids:
  - CHEBI:31739
  evidence_ids:
  - chemistry
  - wrong-pubchem
  - wrong-knapsack
  - wrong-pdb
  - other-links
- assessment_id: scope
  area: scope
  topic: Class, roles, historical producer and names
  outcome: supported
  summary: Structural parents and antibacterial role fit. Historical producer definition
    and leucomycin A3 identity are supported; uncommon historical aliases remain current-source-attributed
    with explicit limits.
  target_ids:
  - CHEBI:31739
  evidence_ids:
  - terms
  - identity-primary
  - official-mixture
  - component-primary
- assessment_id: resistance
  area: evidence
  topic: Exact josamycin versus imported mixture resistance
  outcome: concern
  summary: Josamycin-specific23S evidence is supported within stated experimental
    limits. The three kitasamycin edges cannot be transferred solely through an invalid
    identity merge; this is not a claim that pure josamycin can never be affected
    by those determinants.
  target_ids:
  - CHEBI:31739
  evidence_ids:
  - pneumococcus
  - chlamydia
  - leads
  - owners
  - official-mixture
- assessment_id: completeness
  area: completeness
  topic: Optional ribosome mechanism enrichment
  outcome: unknown
  summary: Exact primary translation studies are discoverable, but original full methods
    were inaccessible here; structural deposition has a ligand-identity conflict.
    No mandatory new target is inferred from absence of a native object.
  target_ids:
  - CHEBI:31739
  evidence_ids:
  - mechanism
  - wrong-pdb
  - search
- assessment_id: provenance
  area: provenance
  topic: Preserved source inputs and lead dispositions
  outcome: supported
  summary: Twenty-one inputs, original thirteen preservation, mints, history and every
    adopted/current reference disposition were checked. All failures and read-depth
    limits are explicit.
  target_ids:
  - CHEBI:31739
  evidence_ids:
  - owners
  - leads
  - search
findings:
- finding_id: F1
  issue_key: josamycin-kitasamycin-complex-source-conflation
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Kitasamycin complex is merged into exact josamycin
  description: Source concept ARO3001227 denotes kitasamycin, explicitly a mixture
    in official material authorities and distinct from leucomycin A3/josamycin in
    original chemistry. Its imported CHEMBL2106399 and CID5282189 graphs are different
    acylation states, and its ErmV/MexPQ-OpmE/MuxABC-OpmB assertions are transferred
    through that invalid merge. Database-assertion wording does not establish exact
    constituent scope. The valid native josamycin identity remains supported.
  target_ids:
  - CHEBI:31739
  field_paths:
  - source_concepts[1]
  - xrefs[0]
  - xrefs[9]
  - xrefs[10]
  - resistance_mechanisms[1]
  - resistance_mechanisms[2]
  - resistance_mechanisms[3]
  evidence_ids:
  - native
  - identity-primary
  - component-primary
  - official-mixture
  - wrong-congeners
  - owners
  - leads
  rule_id: One exact chemical structure per record; docs/HARMONIZATION.md mixture
    exclusion; docs/CURATION.md exact xrefs
  normalization_reason: Major wrong grounding and source-scope transfer. The requested
    josamycin record has a valid supported graph, so no wrong-native-structure blocker
    is asserted.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Existing source-specific mixture exclusion and grounding decisions
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Kitasamycin source concept and wrong exact cross-references
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Three kitasamycin-specific database relations
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source inventory extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Concept aggregation, xrefs and resistance transfer
- finding_id: F2
  issue_key: josamycin-exact-xref-stereo-and-diene-conflicts
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Three additional exact chemical xrefs encode conflicting structures
  description: CID5284579 has one unassigned native centre plus a mapped mycarose
    epimer; KNApSAcK C00018736 has incompatible/InChI-versus-SMILES stereochemistry
    and an inconsistent displayed key; CCD JOS shifts the native macrocycle diene.
    These links do not meet exact chemical equivalence even though their labels say
    josamycin. CID5282165 matches the native graph as a concrete replacement candidate
    for the PubChem link.
  target_ids:
  - CHEBI:31739
  field_paths:
  - xrefs[5]
  - xrefs[6]
  - xrefs[8]
  evidence_ids:
  - native
  - chemistry
  - wrong-pubchem
  - wrong-knapsack
  - wrong-pdb
  rule_id: docs/CURATION.md same-structure chemical xref contract
  normalization_reason: Major wrong chemical grounding; the native josamycin graph,
    name and class are supported. No mixture inference from unassigned stereochemistry.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Josamycin source PubChem identifier
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: ChEBI-owned KNApSAcK and PDB component links
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reproducible source correction/withholding
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Exact chemical-xref contract and regenerated output
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - CHEBI:31739
  description: Add an evidence-backed source-specific EXCLUDE decision for kitasamycin
    ARO3001227/mint antibioticmech:aro-0c5d9c9627 using the existing maintained decision
    mechanism, or correct the upstream concept scope before any future exact mapping.
    Preserve raw source provenance and exact josamycin/leucomycin A3. Reseed so the
    mixture source, two non-equivalent chemical IDs and its three transferred assertions
    no longer enter solely by that merge. Reintroduce any of those resistance determinants
    only after independent exact-josamycin material/evidence verification; this action
    does not declare their biological effects impossible.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: curation/decisions.tsv
    role: Existing source-specific mixture exclusion and grounding decisions
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Kitasamycin source concept and wrong exact cross-references
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_resistance_edges.tsv
    role: Three kitasamycin-specific database relations
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Source inventory extraction
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Concept aggregation, xrefs and resistance transfer
  generator: scripts/extract_source_inventory.py and scripts/seed_from_sources.py
  acceptance_checks:
  - Pure josamycin retains CHEBI31739 and full key XJSFLOJWULLJQS-NGVXBBESSA-N.
  - Mixture source remains traceable as excluded and does not import its different-congener
    IDs or automatic exact-constituent resistance assertions.
  - All retained or newly adopted resistance claims state tested material, organism,
    construct and endpoint.
  - Regeneration plus schema/strict, reference/history/corpus and full QC pass.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - CHEBI:31739
  description: Correct the source-owned PubChem link to verified candidate CID5282165
    with full-graph provenance, and withhold KNApSAcK C00018736 and CCD JOS from exact
    xrefs until their structures are reconciled upstream or an explicit reviewed source
    correction is implemented. A PDB deposition may remain a separately scoped scientific
    reference after ligand evaluation; do not move mismatching structures into drug_xrefs
    merely to evade equality. Regenerate and verify complete graph/stereo equivalence
    without changing the supported native structure.
  owner_paths:
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/aro_antibiotics.tsv
    role: Josamycin source PubChem identifier
  - repository: CultureBotAI/AntibioticMech
    path: data/raw/chebi_antimicrobials.tsv
    role: ChEBI-owned KNApSAcK and PDB component links
  - repository: CultureBotAI/AntibioticMech
    path: scripts/extract_source_inventory.py
    role: Reproducible source correction/withholding
  - repository: CultureBotAI/AntibioticMech
    path: scripts/seed_from_sources.py
    role: Exact chemical-xref contract and regenerated output
  generator: scripts/extract_source_inventory.py and scripts/seed_from_sources.py
  acceptance_checks:
  - Every emitted exact chemical xref resolves to native constitution and configured
    stereochemistry, or is withheld with explicit provenance.
  - PubChem replacement is CID5282165 with matching full key and atom-mapped stereo;
    no blanket rewrite of unrelated PubChem identifiers.
  - KNApSAcK internal disagreements and CCD diene bond-order mismatch are explicitly
    resolved before exact-link restoration.
  - Required focused and shared source/reference/history/corpus/QC gates pass.
limitations:
- The original 1967 biological source 6072799 has no indexed abstract and its guessed
  J-STAGE routes returned 404. The complete 1970 identity paper and selected 1968
  exact-congener activity passages were read; they are not misrepresented as the unread1967
  experiments.
- Direct HMDB HTML/XML/SDF and DrugBank requests returned 403. Official indexed HMDB
  text was inspected only at that depth; exact HMDB graph remains unresolved. Drug-level
  links have separate semantics from chemical xrefs.
- All adopted/current available abstracts were read, with selected native-resistance
  mains at the stated depth. MexPQ/MuxABC publisher mains returned 403 and exact kitasamycin
  assay composition remains unresolved. The mixture finding does not prove absence
  of a josamycin effect.
- KNApSAcK contains conflicting representations; mapped inversions and unspecified
  centres are described separately. Undefined stereo alone is not a mixture claim.
  The PDB component mismatch concerns deposited chemical topology, not a blanket rejection
  of ribosome binding.
- The original 2004 JBC translation paper returned 403; complete original abstract
  supports an optional mechanism lead, with no quantitative target object or universal
  lethal mechanism adopted. PDB2O44 primary citation remains unpublished in its metadata.
- Rare historical aliases beyond leucomycin A3 were corroborated at current-authority
  depth, not each through an original isolation report. No current taxonomic reidentification
  of the historical producer is asserted.
- Authoritative just qc failed during collection because pinned SciPy 1.15.3 has an
  invalid Mach-O section on this platform; the same version also failed under Python
  3.10 and in the fresh batch-002 environment. No dependency versions were changed.
  The supplementary test suite, closed-schema, reproduction and corpus-integrity checks
  do not replace full QC.
notes:
- All original thirteen inputs remain byte-identical within twenty-one verified captured
  inputs. No native record, source inventory, saved bundle, Git or progress state
  was edited.
- Chemistry used the 019 interpreter against 057; schema, strict, ledger and contract
  used 057. This is a stable scratch handoff for root audit and ordered saving.
- Bundle completion is partial because full repository QC is unavailable on this runtime;
  the selected record was read and assessed in full. A saved review does not promote
  native scientific status.
```
