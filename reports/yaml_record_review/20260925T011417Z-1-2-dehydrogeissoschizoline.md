# YAML Record Review: 1,2-dehydrogeissoschizoline

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antiprotozoal/1-2-dehydrogeissoschizoline.yaml`
- Started UTC: 2026-09-25T01:11:28Z
- Finished UTC: 2026-09-25T01:15:16Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:65736` |
| Label | `1,2-dehydrogeissoschizoline` |
| Class | `ANTIPROTOZOAL` |
| Status | `SEEDED` |
| Grounding | `EXACT` |
| Maintained owner | Generated from `data/raw/chebi_antimicrobials.tsv`; future identity, structure, parent, role, and xref changes belong in the ChEBI extractor/seeder path or `curation/decisions.tsv` |

The full 50-line YAML record was read. It is a generated ChEBI-only seed with:

- one source concept, `CHEBI:65736`, minted as `antibioticmech:chebi-fbb59d4d2a`
- one antimicrobial role, `CHEBI:64915`
- three ChEBI parents, `CHEBI:15734`, `CHEBI:38164`, and `CHEBI:38958`
- one exact synonym, `(15β,16α)-1,2-didehydrocuran-17-ol`
- one registry xref, `reaxys:9080520`
- SMILES, Standard InChI, Standard InChIKey `XJEKUKWZYMNSDW-XTXPVBGVSA-N`, formula `C19H24N2O`, charge `0`, average mass `296.414`, and monoisotopic mass `296.18886`
- no `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, `activity_spectrum`, `resistance_mechanisms`, `producer_organisms`, `causal_graphs`, `datasets`, `discussions`, or record-level `evidence`
- only seed/reseed history events from `seed_from_sources`

## Validation

| Check | Result |
|---|---|
| `just worklist` | Passed; regenerated the global backlog. The known unrelated `iclaprim` self-contradictory CARD cross-reference warning was printed. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv` | Passed; wrote 2,859 review-readiness rows. The target is row 161 with `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| `just worklist --queue mechanism --limit 0 --tsv /tmp/antibioticmech-mechanism-queue.tsv` | Passed; wrote 2,848 rows. The target is row 467 with `0 CARD target(s), 0 resistance edge(s) to build on`. |
| `just worklist --queue activity-candidate --limit 0 --tsv /tmp/antibioticmech-activity-candidate-queue.tsv` | Passed; wrote 496 rows. `CHEBI:65736` is absent from this queue. |
| `just worklist --queue producer-candidate --limit 0 --tsv /tmp/antibioticmech-producer-candidate-queue.tsv` | Passed; wrote 965 rows. The target is row 190 because the ChEBI definition says it was isolated from *Geissospermum sericeum*, which is source context but not direct biosynthesis evidence. |
| `just validate data/antibiotics/antiprotozoal/1-2-dehydrogeissoschizoline.yaml` | Passed with `No issues found`. |
| `just validate-strict data/antibiotics/antiprotozoal/1-2-dehydrogeissoschizoline.yaml --out /tmp/dehydrogeissoschizoline-65736-validate-strict.tsv` | Passed; one file scanned, zero `ERROR` rows. |
| `just verify-corpus --summary` | Passed after the same unrelated `iclaprim` diagnostic; 2,939 records expected, 2,939 on disk, and no missing, unexpected, drifted, absent-from-`PATHS.tsv`, or stale-lockfile rows. |

No narrower repository `just` targets exist for standalone term, reference, or
history validation; those checks are covered here by the schema, strict writer
schema, generated-corpus reproducibility, and corpus tests in the full `just qc`
gate that should run before merging the report PR.

## Identity and Grounding

ChEBI's live `CHEBI:65736` page agrees with the generated record on the exact
identifier, label, three-star status, definition, formula, net charge, average
and monoisotopic masses, SMILES, Standard InChI, Standard InChIKey, IUPAC name,
single Reaxys registry number, and `PMID:11809075` citation.

The generated `parent_compounds` match the direct ChEBI `is a` edges shown on
the official term page:

| Parent | ChEBI label |
|---|---|
| `CHEBI:15734` | `primary alcohol` |
| `CHEBI:38164` | `organic heteropentacyclic compound` |
| `CHEBI:38958` | `indole alkaloid` |

The generated `activity_roles` correctly keeps `CHEBI:64915`, `antiplasmodial
drug`, the only antimicrobial role on the ChEBI page that `conf/sources.yaml`
maps into scope. ChEBI also asserts duplicate `metabolite` roles; those are not
antimicrobial roles and are correctly absent from `activity_roles`.

PubChem resolves the same InChIKey to CID `15538076`, and the CID properties
agree with the generated Standard InChI, Standard InChIKey, formula, charge, and
monoisotopic mass. Its isomeric SMILES is equivalent but not byte-identical to
ChEBI's canonical emitted SMILES, which is acceptable because this corpus stores
the ChEBI representation for ChEBI-grounded records.

A hidden-inclusive search for `CHEBI:65736`,
`1,2-dehydrogeissoschizoline`, `XJEKUKWZYMNSDW-XTXPVBGVSA-N`, and `9080520`
covered `data/antibiotics`, `data/raw`, `curation`,
`reports/yaml_record_review`, `/tmp/antibioticmech-review-queue.tsv`, and
`.git`. It found exactly one generated target record, its `PATHS.tsv` row, the
single raw ChEBI inventory row, and the queued review row. A focused
hidden-inclusive search over curation inputs and ignored reports found no prior
review report, no `curation/decisions.tsv` row for
`antibioticmech:chebi-fbb59d4d2a`, and no curator inventory row for this
identifier.

The similar row for `CHEBI:5283`, geissoschizoline, is a true sibling rather
than a duplicate: it carries formula `C19H26N2O` and InChIKey
`FAQGZHFLASTWAV-RWANUPMISA-N`, while `CHEBI:65736` is the dehydro derivative
with formula `C19H24N2O` and InChIKey `XJEKUKWZYMNSDW-XTXPVBGVSA-N`.

## Evidence

`PMID:11809075` resolves in PubMed and Europe PMC to Steele, Veitch, Kite,
Simmonds, and Warhurst, 2002, `Indole and beta-carboline alkaloids from
Geissospermum sericeum.`, *Journal of Natural Products* 65(1):85-88, DOI
`10.1021/np0101705`.

The PubMed abstract supports the exact identity and biological assay context:
the authors report that geissoschizoline, geissoschizoline N(4)-oxide,
`1,2-dehydrogeissoschizoline`, and flavopereirine were obtained from the bark of
*Geissospermum sericeum* and evaluated in vitro against chloroquine-resistant
K1 and chloroquine-sensitive T9-96 *Plasmodium falciparum*, with KB-cell
cytotoxicity also determined.

The exact activity table was not inspected. The DOI redirects to the ACS article
page, but `pubs.acs.org` returned a Cloudflare challenge instead of article
content. An open 2023 article citing Steele et al. confirms the same plant,
alkaloid set, and source publication, but it discusses KB cytotoxicity rather
than the exact antiplasmodial values and should be treated only as a secondary
context source.

Bounded publication searches:

- NCBI ESearch for `"1,2-dehydrogeissoschizoline"` in `Title/Abstract`, the
  IUPAC synonym in `Title/Abstract`, `XJEKUKWZYMNSDW`, or `9080520` returned only
  `PMID:11809075`. NCBI reported no phrase match for the InChIKey, Reaxys
  number, or IUPAC synonym.
- NCBI ESearch for `"1,2-dehydrogeissoschizoline"` in `All Fields` returned
  only `PMID:11809075`.
- NCBI ESearch for `"Geissospermum sericeum"` with either `antiplasmodial` or
  `Plasmodium` in `Title/Abstract` returned only `PMID:11809075`.
- A Europe PMC query for the same exact compound and identifier strings was too
  noisy because the unfielded `9080520` token also matches PMIDs and PMCIDs. It
  was used only to rediscover `PMID:11809075`, not to support record claims.

## Completeness

The current record is a faithful ChEBI seed, but it is not complete enough for
`REVIEWED`.

- The exact identity, ChEBI grounding, source concept, structure, class, and
  antiplasmodial role are supported.
- Leaving `producer_organisms` empty is correct. The inspected source and live
  ChEBI page say the compound was isolated from bark of
  *Geissospermum sericeum*, not that the plant, an endophyte, or another
  organism is experimentally shown to biosynthesize it.
- The source lead appears to contain direct antiplasmodial IC50 data, but the
  table has not been inspected and the current `ActivityObservation` numeric
  slots are MIC-specific. A curator should not coerce an IC50 into `mic_value`.
- No microbial or parasite molecular target was found in the bounded exact-name
  PubMed searches, and the source abstract reports activity screening rather
  than mechanism.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record has a source-supported antiplasmodial role but no curated antimicrobial mechanism, molecular target, or causal graph. | The YAML has no `mode_of_action`, no `molecular_targets`, and no `causal_graphs`; `review-readiness` flags `MECHANISM_REVIEW: mechanism is absent`; exact-name PubMed searches found the isolation/activity paper but no mechanism paper. | Curator-owned fields in `data/antibiotics/antiprotozoal/1-2-dehydrogeissoschizoline.yaml`, written only through `record_curation_event` and `write_validated_antibiotic`. |
| Minor | The exact primary activity values are not represented and cannot yet be structured honestly as MICs. | `PMID:11809075` evaluated the exact compound against K1 and T9-96 *P. falciparum*, but the ACS activity table was blocked and the schema's only numeric activity fields are `mic_value`, `mic_units`, and `mic_qualifier`. | Curator-owned activity observations in this record, plus a future schema change if antiplasmodial IC50 values need first-class numeric slots. |

## Recommended Edits

1. Keep seeded identity fields unchanged. They agree with ChEBI, PubChem, and the
   committed raw row.
2. Search full text and cited/citing mechanism literature for
   `1,2-dehydrogeissoschizoline` before assigning `mode_of_action`. If no target
   or pathway evidence exists, add a concrete `Discussion` explaining that only
   whole-parasite activity has been found and leave `mode_of_action`,
   `mode_of_action_target_scope`, `molecular_targets`, and `causal_graphs`
   empty.
3. Inspect the table in Steele et al. 2002. If the record can represent the
   assay without mislabeling IC50 values as MICs, add one `ActivityObservation`
   per *P. falciparum* strain with `taxon_id: NCBITaxon:5833`, the source strain
   in `strain`, the assay context, and `EvidenceItem.reference: PMID:11809075`.
   Preserve the IC50 values in evidence notes only if no first-class IC50 fields
   exist.
4. Treat *Geissospermum sericeum* as source-of-isolation context only unless a
   source demonstrates biosynthesis. Do not add it to `producer_organisms` from
   this isolation statement alone.

## Follow-up Checks

After any future curation edit:

1. Read the post-mutation YAML and confirm `identifier: CHEBI:65736`.
2. Run `just validate data/antibiotics/antiprotozoal/1-2-dehydrogeissoschizoline.yaml`.
3. Run `just validate-strict data/antibiotics/antiprotozoal/1-2-dehydrogeissoschizoline.yaml --out /tmp/dehydrogeissoschizoline-65736-validate-strict.tsv`.
4. Run `just verify-corpus --summary` to prove generated fields still reproduce.
5. Run `just qc` before merging.

Manual checks needed:

- ACS full text for DOI `10.1021/np0101705`, because PubMed does not expose the
  activity table.
- Exact compound plus mechanism searches before adding a mode of action.

## Additional Notes

- Reports are gitignored by `reports/`, so this file must be staged with
  `git add -f`.
- A hidden-inclusive whole-tree probe was interrupted because it entered ignored
  virtualenv packages and generated site blobs; it was not used to establish an
  absence claim in this review.
