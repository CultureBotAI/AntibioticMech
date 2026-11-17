# Attribution

The record content in this repository is licensed [CC BY 4.0](LICENSE-DATA) and
is derived from the sources below. If you redistribute it, in whole or in part,
carry this attribution with it.

## Required attribution

> AntibioticMech (CultureBotAI), CC BY 4.0. Derived from ChEBI (EMBL-EBI,
> CC BY 4.0), the Antibiotic Resistance Ontology (CARD, McMaster University,
> CC BY 4.0), MIBiG (CC BY 4.0), BindingDB (CC BY 4.0), PHI-base
> (CC BY 4.0), the CRyPTIC Consortium Dataset (CC BY 4.0), Drugs@FDA
> (U.S. Food and Drug Administration), FDA GSRS / UNII (FDA and NCATS), and
> Stanford HIVDB hivfacts (Unlicense), with chemical structures from PubChem
> (NCBI).

## Per-record provenance

Attribution is machine-readable, not only a notice. Every record carries a
`source_concepts` block naming each ChEBI, ARO, or curator concept that
resolved to its chemical structure identity, with that source's own identifier
and label:

```yaml
source_concepts:
- source: CHEBI
  source_id: CHEBI:42355
  source_label: erythromycin A
  minted_identifier: antibioticmech:chebi-...
- source: ARO
  source_id: ARO:0000006
  source_label: erythromycin
  minted_identifier: antibioticmech:aro-...
```

Source-owned mechanism, activity, production, and regulatory assertions carry
their source on the item itself: `producer_organisms[].source`,
`molecular_targets[].source`, `resistance_mechanisms[].source`,
`activity_spectrum[].source`, `genotype_resistance_score_rules[].source`, and
`clinical_status_assertions[].source`.

A consumer taking a subset of the corpus can derive exactly which upstream
resources that subset depends on from both record identity and item-level
source fields, rather than carrying a blanket notice.

## Sources

**ChEBI** — Chemical Entities of Biological Interest, EMBL-EBI. CC BY 4.0.
Supplies identity, structures, definitions, synonyms, cross-references and the
antimicrobial role hierarchy. <https://www.ebi.ac.uk/chebi/>

Hastings J, Owen G, Dekker A, et al. ChEBI in 2016: Improved services and an
expanding collection of metabolites. *Nucleic Acids Res.* 2016;44(D1):D1214-9.
doi:10.1093/nar/gkv1031

**CARD / ARO** — the Antibiotic Resistance Ontology, McMaster University.
CC BY 4.0 (the ontology files; CARD's other materials carry different, more
restrictive terms and are **not** used here). Supplies the antibiotic molecule
subtree, drug classes, resistance determinants and drug targets.
<https://card.mcmaster.ca/>

Alcock BP, Huynh W, Chalil R, et al. CARD 2023: expanded curation, support for
machine learning, and resistome prediction at the Comprehensive Antibiotic
Resistance Database. *Nucleic Acids Res.* 2023;51(D1):D690-D699.
doi:10.1093/nar/gkac920

**MIBiG** — the Minimum Information about a Biosynthetic Gene Cluster
repository. CC BY 4.0. Supplies producer organisms, biosynthetic gene cluster
accessions, and the per-locus evidence grading the compound-to-producer link.
<https://mibig.secondarymetabolites.org/>

Zdouc MM, Blin K, Louwen NLL, et al. MIBiG 4.0: advancing biosynthetic gene
cluster curation through global collaboration. *Nucleic Acids Res.*
2025;53(D1):D678-D690. doi:10.1093/nar/gkae1115

**BindingDB** — CC BY 4.0 for records curated directly from primary
literature by BindingDB. Supplies quantitative compound-target measurements
from article-curated rows. Rows BindingDB imported from ChEMBL and other
providers are excluded. <https://www.bindingdb.org/>

Liu T, Hwang L, Burley SK, Nitsche CI, Southan C, Walters WP, Gilson MK.
BindingDB in 2024: a FAIR knowledgebase of protein-small molecule binding data.
*Nucleic Acids Res.* 2025;53(D1):D1633-D1644. doi:10.1093/nar/gkae1075

**PHI-base** — the Pathogen-Host Interactions database. CC BY 4.0. Supplies
curated ChEBI-grounded pathogen gene--antimicrobial resistance interactions
with primary PubMed citations. <https://phi5.phi-base.org/>

Urban M, Cuzick A, Seager J, et al. PHI-base: the multi-species pathogen-host
interaction database in 2025. *Nucleic Acids Res.* 2025;53(D1):D826-D838.
doi:10.1093/nar/gkae1084

**CRyPTIC Consortium Dataset** — CRyPTIC Consortium. CC BY 4.0. Supplies
grouped DST and UKMYC *Mycobacterium tuberculosis* complex activity
observations from exact-mapped drug codes. <https://zenodo.org/records/15680920>

CRyPTIC Consortium. CRyPTIC Consortium Dataset. Zenodo.
doi:10.5281/zenodo.15680920

**Stanford HIVDB / hivfacts** — Stanford HIV Drug Resistance Database
hivfacts. Unlicense. Supplies exact HIV-1 drug-specific HIVDB 10.2 genotype
score-rule formula terms for exact-mapped antiretroviral compounds.
<https://github.com/hivdb/hivfacts/>

**Drugs@FDA** — U.S. Food and Drug Administration. United States government
public-domain data. Supplies product-level human-drug approval and marketing
facts for exact GSRS-grounded single-ingredient products.
<https://www.fda.gov/drugs/drug-approvals-and-databases/drugsfda-data-files>

**FDA GSRS / UNII** — U.S. Food and Drug Administration and the National Center
for Advancing Translational Sciences. United States government public data;
GSRS materials are Apache-2.0. Supplies the UNII and chemical-structure
identity layer used to ground Drugs@FDA products exactly. <https://gsrs.ncats.nih.gov/>

**PubChem** — NCBI, NLM, NIH. Public domain (US Government work). Supplies
structures for the CARD molecules ChEBI does not cover.
<https://pubchem.ncbi.nlm.nih.gov/>

Kim S, Chen J, Cheng T, et al. PubChem 2023 update. *Nucleic Acids Res.*
2023;51(D1):D1373-D1380. doi:10.1093/nar/gkac956

## Project-authored material

Project-authored data and narrative documentation are [CC BY 4.0](LICENSE-DATA).
Project-authored code, schemas, scripts, tests and website templates are
[BSD-3-Clause](LICENSE-CODE). Source material retains its applicable terms and
attributions. See [LICENSE](LICENSE) for the complete scope.
