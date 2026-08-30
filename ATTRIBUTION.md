# Attribution

The record content in this repository is licensed [CC BY 4.0](LICENSE-DATA) and
is derived from the sources below. If you redistribute it, in whole or in part,
carry this attribution with it.

## Required attribution

> AntibioticMech (CultureBotAI), CC BY 4.0. Derived from ChEBI (EMBL-EBI,
> CC BY 4.0) and the Antibiotic Resistance Ontology (CARD, McMaster University,
> CC BY 4.0), with chemical structures from PubChem (NCBI).

## Per-record provenance

Attribution is machine-readable, not only a notice. Every record carries a
`source_concepts` block naming each upstream concept that resolved to it, with
that source's own identifier and label:

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

A consumer taking a subset of the corpus can therefore derive exactly which
upstream resources that subset depends on, rather than carrying a blanket notice.

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

**PubChem** — NCBI, NLM, NIH. Public domain (US Government work). Supplies
structures for the CARD molecules ChEBI does not cover.
<https://pubchem.ncbi.nlm.nih.gov/>

Kim S, Chen J, Cheng T, et al. PubChem 2023 update. *Nucleic Acids Res.*
2023;51(D1):D1373-D1380. doi:10.1093/nar/gkac956

## What is CC0

Everything that is this repository's own work rather than an upstream source's:
the code under `scripts/` and `src/`, the schema, the tests, the configuration,
the documentation, and the curation decisions in `curation/`. See [LICENSE](LICENSE).
