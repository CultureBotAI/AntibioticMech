# YAML Record Review: 12-deoxyphorbol-13-(3E,5E-decadienoate)

- Repository: CultureBotAI/AntibioticMech
- Record: data/antibiotics/antiviral/12-deoxyphorbol-13-3e-5e-decadienoate.yaml
- Started UTC: 2026-09-25T18:04:00Z
- Finished UTC: 2026-09-25T18:25:05Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:65747` |
| Label | `12-deoxyphorbol-13-(3E,5E-decadienoate)` |
| Class | `ANTIVIRAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Maintained owner | `data/raw/chebi_antimicrobials.tsv`, emitted to `data/antibiotics/antiviral/12-deoxyphorbol-13-3e-5e-decadienoate.yaml` |

This is a ChEBI-seeded record with one source concept:

```text
CHEBI:65747  12-deoxyphorbol-13-(3E,5E-decadienoate)  source_version=2026-08-30
```

The source concept contributes antimicrobial role `CHEBI:64946` (`anti-HIV
agent`) and source literature lead `PMID:7623051`.

Ignored-file-inclusive searches over `reports`, `curation`, `data/raw`, and
`data/antibiotics` covered the identifier `CHEBI:65747`, exact label
`12-deoxyphorbol-13-(3E,5E-decadienoate)`, PubMed spelling
`12-deoxyphorbol 13-(3E,5E-decadienoate)`, and path slug
`12-deoxyphorbol-13-3e-5e-decadienoate`. Apart from this report itself, they
found only:

- the active review queue row in `curation/record_review_queue.tsv`;
- the raw ChEBI row in `data/raw/chebi_antimicrobials.tsv`;
- the generated path lock row in `data/antibiotics/PATHS.tsv`; and
- the target YAML.

There was no prior exact review report or duplicate curated YAML in the
maintained/generated corpus searched above.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antiviral/12-deoxyphorbol-13-3e-5e-decadienoate.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/antibiotics/antiviral/12-deoxyphorbol-13-3e-5e-decadienoate.yaml --out /tmp/antibioticmech-chebi-65747-strict.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed; 2939 records expected, 2939 on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, 0 stale lockfile rows. |
| `uv run python scripts/curation_worklist.py --queue all --limit 0 --tsv /tmp/antibioticmech-worklist-chebi65747.tsv` | Passed; the exact rows for this record were `mechanism`, `producer-candidate`, and `review-readiness`. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-chebi65747-review-queue.tsv` | Passed; `CHEBI:65747` is queued as `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

`just verify-corpus --summary` and the worklist regeneration printed the known
unrelated `ARO:3000337`/iclaprim CARD cross-reference warning; it did not
involve this record.

## Identity and Grounding

The generated ChEBI identity is internally consistent:

- OLS4 resolved `CHEBI:65747` as a current, non-obsolete, 3-star ChEBI term
  labeled `12-deoxyphorbol-13-(3E,5E-decadienoate)`.
- OLS4 matched the record definition, formula `C30H42O6`, charge `0`, average
  mass `498.66`, monoisotopic mass `498.29814`, SMILES, Standard InChI,
  Standard InChIKey `AZEXNJIEBDRVJS-OSHOESKRSA-N`, and `pubmed:7623051`.
- PubChem resolved `AZEXNJIEBDRVJS-OSHOESKRSA-N` to CID `6474968`; CID
  `6474968` matched formula `C30H42O6`, Standard InChI, InChIKey, exact mass
  `498.29813906`, molecular weight `498.6`, charge `0`, and an IUPAC name for
  the same `12-deoxyphorbol-13-(3E,5E-decadienoate)` structure.
- OLS4 resolved the record's four ChEBI parent terms as current, non-obsolete
  `CHEBI:139592` (`tertiary alpha-hydroxy ketone`), `CHEBI:15734`
  (`primary alcohol`), `CHEBI:26878` (`tertiary alcohol`), and `CHEBI:37532`
  (`phorbol ester`).
- OLS4 resolved the antimicrobial role `CHEBI:64946` as current,
  non-obsolete `anti-HIV agent`.

The `anti-HIV agent` role maps correctly to repository class `ANTIVIRAL`. The
exact source row in `data/raw/chebi_antimicrobials.tsv` and path row in
`data/antibiotics/PATHS.tsv` both agree with the target YAML.

## Evidence

`PMID:7623051` resolves to Erickson, Beutler, Cardellina, McMahon, Newman, and
Boyd, "A novel phorbol ester from Excoecaria agallocha", *Journal of Natural
Products* 58(5):769-772, DOI `10.1021/np50119a020`.

PubMed's abstract supports the broad identity and qualitative anti-HIV activity
claims that ChEBI copied into the definition:

- the paper isolated 12-deoxyphorbol 13-(3E,5E-decadienoate), compound 1, from
  leaves and stems of `Excoecaria agallocha` collected in northwest Australia;
- the same abstract describes compound 1 as the plant material's anti-HIV
  principle;
- the structure was determined spectrally; and
- compound 1 displaced radiolabeled phorbol dibutyrate from rat brain
  membranes.

The DOI resolves to ACS, but unauthenticated `curl -L` was blocked by a
Cloudflare `403` challenge. PubMed supplied the citation metadata and abstract,
but the full paper's purification, spectral, and anti-HIV assay details were not
inspected.

The bounded PubMed searches for the exact stereochemical label and for
InChIKey stem `AZEXNJIEBDRVJS` found no hits. Searching PubMed title/abstracts
for `Excoecaria agallocha`, `phorbol`, and `HIV` found one hit: `PMID:7623051`.
No inspected source metadata identified a compound-specific viral molecular
target or resistance mechanism.

## Completeness

The record has enough seeded information to establish a current exact ChEBI
identity, structure, source PMID, anti-HIV activity role, antiviral filing
class, and four strictly broader ChEBI parents.

Consequential gaps remain:

- `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, and
  `causal_graph` are absent. The regenerated worklist confirms there are no
  CARD target or resistance edges to build on, and none of the inspected source
  metadata named a supported molecular target or resistance mechanism for this
  exact compound.
- `activity_spectrum` is absent. The inspected abstract verifies qualitative
  anti-HIV activity but not a structured MIC, IC50, EC50, selectivity index,
  assay, cell line, or virus strain measurement.
- `producer_organisms` is absent. The definition and source abstract identify
  `Excoecaria agallocha` as the plant source, and NCBI Taxonomy resolved that
  name to active species `NCBITaxon:241838`, but the regenerated worklist
  correctly flags it only as `SOURCE only - may not be the producer`.

Optional clinical-status and dataset fields are correctly empty; no inspected
source suggested an approved product or public dataset specific to this exact
compound.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| F1 | Major | The record has no curated antimicrobial mechanism, molecular target, causal edge, or structured anti-HIV activity observation. `PMID:7623051` verifies qualitative anti-HIV activity for this exact compound, but the original ACS full text remains blocked and no source inspected during this review identified a supported viral molecular target or machine-readable activity value for `12-deoxyphorbol-13-(3E,5E-decadienoate)`. | Curator-owned fields on `data/antibiotics/antiviral/12-deoxyphorbol-13-3e-5e-decadienoate.yaml` |
| F2 | Minor | `Excoecaria agallocha` is only represented inside the generated ChEBI definition. The paper abstract supports leaves and stems of this plant as the isolation source and the worklist already flags the phrase as `producer-candidate`; a curator should decide whether a host plant source belongs in `ProducerOrganism` or whether the candidate should remain only as definition evidence. | Curator-owned `producer_organisms` or discussion fields on `data/antibiotics/antiviral/12-deoxyphorbol-13-3e-5e-decadienoate.yaml` |

No blocker findings were found.

## Recommended Edits

1. Inspect the ACS full text for `PMID:7623051`, capture the exact anti-HIV
   assay result as an `ActivityObservation` if the paper reports a supported
   potency, units, assay, cell line, and viral context, and attach
   compound-level `PMID:7623051`/DOI evidence.
2. Search for primary literature that tests
   `12-deoxyphorbol-13-(3E,5E-decadienoate)` against a named HIV or host
   molecular target. If found, add `mode_of_action`,
   `mode_of_action_target_scope`, `molecular_targets`, and edge-level
   `causal_graph` entries through the guarded writer. If no target evidence is
   found, leave mechanism fields empty and add a bounded `CURATION_TODO`
   discussion documenting the negative search.
3. Decide the `Excoecaria agallocha` producer lead. If accepted, add a
   `ProducerOrganism` with `taxon_id: NCBITaxon:241838`,
   `taxon_label: Excoecaria agallocha`, and `PMID:7623051` evidence scoped to
   isolation of 12-deoxyphorbol-13-(3E,5E-decadienoate) from leaves and stems.

## Follow-up Checks

- Re-run `just validate-strict data/antibiotics/antiviral/12-deoxyphorbol-13-3e-5e-decadienoate.yaml --out /tmp/antibioticmech-chebi-65747-strict.tsv`
  after any record mutation.
- Re-run `just verify-corpus --summary` to ensure no seeded fields drifted while
  curator-owned fields were added.
- Re-run `just review-queue --limit 0 --tsv /tmp/antibioticmech-chebi65747-review-queue.tsv`
  and confirm `CHEBI:65747` leaves the `MECHANISM_REVIEW` gate only after a
  supported mechanism or explicit mechanism TODO is curated.
- If a producer claim or source veto is added, re-run
  `uv run python scripts/curation_worklist.py --queue all --limit 0 --tsv /tmp/antibioticmech-worklist-chebi65747.tsv`
  and confirm the `producer-candidate` row is resolved or intentionally
  documented.

## Additional Notes

- The source abstract uses the positionally identical label `12-deoxyphorbol
  13-(3E,5E-decadienoate)` without the record label's extra hyphen after
  `13`; the structure/InChIKey verified that the generated record denotes the
  intended compound 1.
- PubMed's `HIV-1` MeSH descriptor is an index term on the article, not a
  substitute for a structured virus or target assertion on the record.
