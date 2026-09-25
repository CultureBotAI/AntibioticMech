# YAML Record Review: 12-methyl-5-dehydroacetylhorminone

- Repository: CultureBotAI/AntibioticMech
- Record: data/antibiotics/antimycobacterial/12-methyl-5-dehydroacetylhorminone.yaml
- Started UTC: 2026-09-25T19:01:00Z
- Finished UTC: 2026-09-25T19:05:08Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:66365` |
| Label | `12-methyl-5-dehydroacetylhorminone` |
| Class | `ANTIMYCOBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Maintained owner | `data/raw/chebi_antimicrobials.tsv`, emitted to `data/antibiotics/antimycobacterial/12-methyl-5-dehydroacetylhorminone.yaml` |

This is a ChEBI-seeded record with one source concept:

```text
CHEBI:66365  12-methyl-5-dehydroacetylhorminone  source_version=2026-08-30
```

The ChEBI raw row contributes antimicrobial role `CHEBI:33231`
(`antitubercular agent`), xref `reaxys:7890385`, and source literature lead
`PMID:9428161`; the emitted `source_concepts` entry records the ChEBI identity,
minted identifier, role term, and source version.

Ignored-file-inclusive searches over `reports`, `curation`, `data/raw`, and
`data/antibiotics` covered the identifier `CHEBI:66365`, exact label
`12-methyl-5-dehydroacetylhorminone`, and path slug
`12-methyl-5-dehydroacetylhorminone`. They found only:

- the active review queue row in `curation/record_review_queue.tsv`;
- the raw ChEBI row in `data/raw/chebi_antimicrobials.tsv`;
- the generated path lock row in `data/antibiotics/PATHS.tsv`; and
- the target YAML.

There was no prior exact review report or duplicate curated YAML in the
maintained/generated corpus searched above.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antimycobacterial/12-methyl-5-dehydroacetylhorminone.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/antibiotics/antimycobacterial/12-methyl-5-dehydroacetylhorminone.yaml --out /tmp/antibioticmech-chebi-66365-strict.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed; 2939 records expected, 2939 on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, 0 stale lockfile rows. |
| `uv run python scripts/curation_worklist.py --queue all --limit 0 --tsv /tmp/antibioticmech-worklist-chebi66365.tsv` | Passed; the exact rows for this record were `mechanism`, `producer-candidate`, and `review-readiness`. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-chebi66365-review-queue.tsv` | Passed; `CHEBI:66365` is queued as `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

`just verify-corpus --summary` and the worklist regeneration printed the known
unrelated `ARO:3000337`/iclaprim CARD cross-reference warning; it did not
involve this record.

## Identity and Grounding

The generated ChEBI identity is internally consistent:

- OLS4 resolved `CHEBI:66365` as a current, non-obsolete, 3-star ChEBI term
  labeled `12-methyl-5-dehydroacetylhorminone`.
- OLS4 matched the record definition, formula `C23H30O5`, charge `0`, average
  mass `386.488`, monoisotopic mass `386.20932`, SMILES, Standard InChI,
  Standard InChIKey `KRHKKRFFQDNBIN-FATZIPQQSA-N`, `reaxys:7890385`, and
  `pubmed:9428161`.
- PubChem resolved `KRHKKRFFQDNBIN-FATZIPQQSA-N` to CID `467787`; CID `467787`
  matched formula `C23H30O5`, Standard InChI, InChIKey, exact mass
  `386.20932405`, molecular weight `386.5`, charge `0`, and the record's
  acetate IUPAC synonym.
- OLS4 resolved the record's four ChEBI parent terms as current, non-obsolete
  `CHEBI:25830` (`p-quinones`), `CHEBI:36762` (`abietane diterpenoid`),
  `CHEBI:47622` (`acetate ester`), and `CHEBI:47985` (`enol ether`).
- OLS4 resolved `CHEBI:33231` as current, non-obsolete `antitubercular agent`.

The ChEBI role maps correctly to repository class `ANTIMYCOBACTERIAL`. The
exact source row in `data/raw/chebi_antimicrobials.tsv` and path row in
`data/antibiotics/PATHS.tsv` both agree with the target YAML.

## Evidence

`PMID:9428161` resolves to Ulubelen, Topcu, and Johansson,
"Norditerpenoids and diterpenoids from Salvia multicaulis with antituberculous
activity", *Journal of Natural Products* 60(12):1275-1280, DOI
`10.1021/np9700681`.

PubMed's abstract supports the broad identity and activity claims that ChEBI
copied into the definition:

- the paper isolated compound 6, `12-methyl-5-dehydroacetylhorminone`, from
  the roots of `Salvia multicaulis`;
- compounds 1-7 were new norditerpenoids, abietane diterpenoids, or pimarane
  diterpenoids whose structures were established with 1D/2D NMR and chemical
  methods; and
- the antituberculous activity of compounds 1-7 was tested against
  `Mycobacterium tuberculosis` strain H37Rv, with all compounds active and
  compounds 2 and 4-6 reported as the most potent.

The DOI resolves to ACS, but unauthenticated `curl -L` was blocked by a
Cloudflare `403` challenge. PubMed supplied the citation metadata and abstract,
but the original MIC, assay, and any additional bacterial-culture table rows
were not inspected.

A bounded PubMed exact-label search found `PMID:9428161` and `PMID:34225624`.
The latter is a 2021 systematic review that names the compound as a potential
anti-TB phytochemical but does not, in the inspected abstract, identify a
compound-specific molecular target or primary activity measurement. A PubMed
InChIKey-stem search found no hits; the PubMed title/abstract search for
`Salvia multicaulis` and `dehydroacetylhorminone` found only `PMID:9428161`.

## Completeness

The record has enough seeded information to establish a current exact ChEBI
identity, structure, source PMID, Reaxys xref, source role, filing class, and
four strictly broader ChEBI parents.

Consequential gaps remain:

- `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, and
  `causal_graph` are absent. The regenerated worklist confirms there are no
  CARD target or resistance edges to build on, and none of the inspected source
  metadata named a compound-specific molecular target or resistance mechanism.
- `activity_spectrum` is absent even though the source abstract says the exact
  compound was tested against `Mycobacterium tuberculosis` H37Rv
  (`NCBITaxon:83332`). The full ACS table is still needed for the exact value,
  units, and assay.
- `producer_organisms` is absent. The definition and source abstract identify
  `Salvia multicaulis` roots as the isolation source, and NCBI Taxonomy
  resolved `Salvia multicaulis` to active species `NCBITaxon:1685714`, but no
  structured producer claim has yet been curated.

Optional clinical-status and dataset fields are correctly empty; no inspected
source suggested an approved product or public dataset specific to this exact
compound.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| F1 | Major | The record has no curated antimicrobial mechanism, molecular target, causal edge, or structured H37Rv activity observation. `PMID:9428161` verifies qualitative antitubercular activity against `M. tuberculosis` H37Rv for this exact compound, but the original ACS table remains uninspected and no source inspected during this review identified a supported molecular target or machine-readable activity value for `12-methyl-5-dehydroacetylhorminone`. | Curator-owned fields on `data/antibiotics/antimycobacterial/12-methyl-5-dehydroacetylhorminone.yaml` |
| F2 | Minor | `Salvia multicaulis` is only represented inside the generated ChEBI definition. The paper abstract supports roots of this plant as the isolation source and the worklist already flags the phrase as `producer-candidate`; a curator should decide whether that is enough to add `NCBITaxon:1685714` as a plant producer with claim-level `PMID:9428161` evidence. | Curator-owned `producer_organisms` on `data/antibiotics/antimycobacterial/12-methyl-5-dehydroacetylhorminone.yaml` |

No blocker findings were found.

## Recommended Edits

1. Inspect the ACS full text for `PMID:9428161`, capture compound 6's exact
   H37Rv result as an `ActivityObservation` with `taxon_id: NCBITaxon:83332`,
   strain `H37Rv`, measured value, units, assay, and claim-level
   `PMID:9428161`/DOI evidence.
2. Search for primary literature that tests
   `12-methyl-5-dehydroacetylhorminone` against a named microbial molecular
   target. If found, add `mode_of_action`, `mode_of_action_target_scope`,
   `molecular_targets`, and edge-level `causal_graph` entries through the
   guarded writer. If no target evidence is found, leave mechanism fields empty
   and add a bounded `CURATION_TODO` discussion documenting the negative
   search.
3. Decide the `Salvia multicaulis` producer lead. If accepted, add a
   `ProducerOrganism` with `taxon_id: NCBITaxon:1685714`,
   `taxon_label: Salvia multicaulis`, and `PMID:9428161` evidence scoped to
   isolation of 12-methyl-5-dehydroacetylhorminone from the roots.

## Follow-up Checks

- Re-run `just validate-strict data/antibiotics/antimycobacterial/12-methyl-5-dehydroacetylhorminone.yaml --out /tmp/antibioticmech-chebi-66365-strict.tsv`
  after any record mutation.
- Re-run `just verify-corpus --summary` to ensure no seeded fields drifted while
  curator-owned fields were added.
- Re-run `just review-queue --limit 0 --tsv /tmp/antibioticmech-chebi66365-review-queue.tsv`
  and confirm `CHEBI:66365` leaves the `MECHANISM_REVIEW` gate only after a
  supported mechanism or explicit mechanism TODO is curated.
- If a producer claim is added, re-run
  `uv run python scripts/curation_worklist.py --queue all --limit 0 --tsv /tmp/antibioticmech-worklist-chebi66365.tsv`
  and confirm the `producer-candidate` row is resolved.

## Additional Notes

- The source abstract spells the same paper's compound 5 as
  `12-methyl-5-dethydrohorminone`, but it spells compound 6,
  `12-methyl-5-dehydroacetylhorminone`, exactly as ChEBI does.
- The exact-label PubMed search's secondary-review hit is useful for vocabulary
  and literature discovery only; the review report above relies on the cited
  1997 primary experiment for the identity and H37Rv activity claims.
