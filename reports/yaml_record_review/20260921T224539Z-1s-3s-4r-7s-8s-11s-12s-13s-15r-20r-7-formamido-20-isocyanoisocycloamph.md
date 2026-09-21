# YAML Record Review: (1S,3S,4R,7S,8S,11S,12S,13S,15R,20R)-7-formamido-20-isocyanoisocycloamphilectane

- Repository: `CultureBotAI/AntibioticMech`
- Record: `data/antibiotics/antiprotozoal/1s-3s-4r-7s-8s-11s-12s-13s-15r-20r-7-formamido-20-isocyanoisocycloamph.yaml`
- Started UTC: 2026-09-21T22:43:30Z
- Finished UTC: 2026-09-21T22:45:39Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:65905` |
| Label | `(1S,3S,4R,7S,8S,11S,12S,13S,15R,20R)-7-formamido-20-isocyanoisocycloamphilectane` |
| Path | `data/antibiotics/antiprotozoal/1s-3s-4r-7s-8s-11s-12s-13s-15r-20r-7-formamido-20-isocyanoisocycloamph.yaml` |
| Class | `ANTIPROTOZOAL` |
| Curation status | `SEEDED` |
| Grounding | `EXACT` |
| Source concept | `CHEBI:65905`, version `2026-08-30`, minted key `antibioticmech:chebi-09036d27dd` |
| Structure | `XBSPNOJIQRUQDQ-OXEUSEQRSA-N`; formula `C22H34N2O`; charge `0` |
| Evidence-bearing objects | None |

This review covered one generated ChEBI-seeded antiplasmodial marine natural product. The record has
source-derived identity, definition, parent, role, structure, and Reaxys metadata, but no
curator-owned activity, producer, target, resistance, discussion, or causal-graph assertions.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antiprotozoal/1s-3s-4r-7s-8s-11s-12s-13s-15r-20r-7-formamido-20-isocyanoisocycloamph.yaml` | Pass: `linkml-validate` reported `No issues found`. |
| `just validate-strict data/antibiotics/antiprotozoal/1s-3s-4r-7s-8s-11s-12s-13s-15r-20r-7-formamido-20-isocyanoisocycloamph.yaml --out /tmp/antibioticmech-forma-methyl-65905-validation.tsv` | Pass: 1 file scanned, 0 files with `ERROR`, 0 error rows. |
| `just verify-corpus --summary` | Pass: 2939 expected records, 2939 on disk, no missing records, no unexpected records, no drifted fields, no identifiers absent from `PATHS.tsv`, no stale lockfile rows. The unrelated known `ARO:3000337` CARD cross-reference warning was emitted. |
| `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist-forma-methyl-65905.tsv` | Pass: full worklist TSV was written. `CHEBI:65905` appears on `mechanism`, `producer-candidate`, and `review-readiness`. |
| `just review-queue --limit 37` | Pass: `CHEBI:65905` is the next queued unreported record after `CHEBI:47351`; its row carries source lead `PMID:19199790` and says `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

No narrower single-record term, reference, or history validator is exposed for this ChEBI-seeded record;
the schema/strict checks and `verify-corpus` are the narrowest documented local gates.

## Identity and Grounding

`CHEBI:65905` is a current, non-obsolete 3-star ChEBI term. OLS resolves it to the same label,
definition, SMILES, Standard InChI, Standard InChIKey, formula, charge, average mass, monoisotopic mass,
`reaxys:19756168`, and `pubmed:19199790` values captured in the committed ChEBI inventory and generated
record.

The ChEBI graph exposes the record's three direct `subClassOf` parents, `CHEBI:24079` formamides,
`CHEBI:35353` isocyanide, and `CHEBI:52557` tetracyclic diterpenoid. It also exposes a direct `has role`
edge to `CHEBI:64915` antiplasmodial drug, which `conf/sources.yaml` maps to the `ANTIPROTOZOAL` filing
class.

An ignored-inclusive search for `XBSPNOJIQRUQDQ` across `data`, `curation`, and `reports` found only the
raw ChEBI row and this generated YAML. No other curated or proposed record is claiming the same Standard
InChIKey.

## Evidence

There are no evidence-bearing assertions in the target record. That is legal for a ChEBI-seeded record
because the source concept supplies database provenance and no mechanism, target, resistance, activity,
producer, or causal edge has been promoted to a curator-owned assertion.

The ChEBI definition and PubMed source lead both point to the same primary paper, PMID:19199790 /
DOI:10.1021/np800654w. The repository PubMed adapter resolved that PMID to the Wright and Lang-Unnasch
2009 Journal of Natural Products paper on diterpene formamides from *Cymbastela hooperi*. Its abstract
reports isolation and characterization of five new diterpene formamides from dichloromethane-soluble
fractions of the sponge and reports compound 1, the formamide-plus-isonitrile compound matching this
ChEBI entry, as moderately active in in vitro antiplasmodial bioassays at `IC50 0.5 microg/mL`.

The public PubMed and DOI HTML endpoints were not inspectable through `curl` in this environment:
PubMed returned an anti-automation cookie challenge and ACS returned a Cloudflare challenge. The bounded
repository adapter query still found exactly one PubMed candidate for the ChEBI PMID/exact-name/search
terms, while the Semantic Scholar provider returned HTTP 429.

## Completeness

The record is incomplete as a reviewed antimicrobial activity record. PMID:19199790 reports a quantitative
antiplasmodial result for the exact compound, but the YAML has no `activity_spectrum` item carrying the
assay organism, assay description, represented endpoint, units, or primary evidence. That result should
be curated only after inspecting the full paper far enough to recover the *Plasmodium* species or strain,
assay setup, and a schema-valid representation; the abstract reports an `IC50`, while
`ActivityObservation`'s numeric fields are MIC-specific.

The missing `mode_of_action`, `molecular_targets`, `resistance_mechanisms`, and `causal_graphs` are
honest unknowns from the inspected source text. The exact mechanism of action was not stated in the
ChEBI definition, OLS role graph, or the PubMed abstract.

The missing `producer_organisms` slot is also deliberate. ChEBI says the compound was isolated from the
tropical marine sponge *Cymbastela hooperi*, and `just worklist` therefore raises a
`producer-candidate` row, but the source organism is an animal sponge, not a microbial biosynthetic
producer that should be written into `ProducerOrganism`.

An ignored-inclusive search for `CHEBI:65905` across `data/antibiotics`, `data/raw`, `curation`, and
`reports` found only the PATHS row, raw ChEBI row, review-queue row, and generated YAML. No existing
curation decision, overlay, curator-inventory row, or prior review report for the identifier was found.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The known quantitative antiplasmodial assay from PMID:19199790 is not represented as evidence-backed activity or as an explicit schema gap. The PubMed abstract reports compound 1 with `IC50 0.5 microg/mL`, while the generated YAML has no organism-level activity item, no primary evidence, and no discussion of whether an IC50 can be represented without overloading MIC slots. | ChEBI `pubmed:19199790` xref; repository PubMed search result for PMID:19199790; `just worklist` row for `CHEBI:65905`. | Curator-owned fields in `data/antibiotics/antiprotozoal/1s-3s-4r-7s-8s-11s-12s-13s-15r-20r-7-formamido-20-isocyanoisocycloamph.yaml`, written only through `record_curation_event` and `write_validated_antibiotic`. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Inspect PMID:19199790 full text and curate the reported in vitro antiplasmodial assay only if the
   article supplies the tested *Plasmodium* taxon or strain, assay method, and a MIC or other
   schema-valid endpoint for compound 1. If the only quantitative endpoint is IC50, add a bounded
   `CURATION_TODO` discussion instead of storing the value in MIC-specific slots.

2. Add record-level `PMID:19199790` evidence to document that the ChEBI definition's isolation and
   antiplasmodial-activity statements have been checked against the primary paper.

3. Leave `producer_organisms` empty unless later evidence establishes a microbial producer; the sponge
   isolation source is not a valid microbial producer claim for this schema.

## Follow-up Checks

- Re-run `just validate-strict data/antibiotics/antiprotozoal/1s-3s-4r-7s-8s-11s-12s-13s-15r-20r-7-formamido-20-isocyanoisocycloamph.yaml --out /tmp/antibioticmech-record-validation.tsv`
  after any evidence or activity curation.
- Re-run `just verify-corpus --summary` to prove any guarded edits are all curator-owned.
- Re-run `just worklist --limit 0 --tsv /tmp/antibioticmech-worklist.tsv`; the `producer-candidate`
  row is expected to remain until there is a curator-owned way to mark the sponge phrase as a checked
  non-producer.
- Re-run `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv`; this record should
  remain on `review-readiness` until at least the activity evidence has been curated and mechanism
  completeness has been assessed from more than the abstract.

## Additional Notes

- ChEBI/OLS checks were direct official registry reads through `curl`.
- The exact slug also appears inside `data/embeddings/chemical-structure-map.json`; that generated,
  minified map was not used for any record-level claim because it is not source evidence.
