# YAML Record Review: 1α-acetoxy-2α-hydroxy-6β,9β,15-tribenzoyloxy-β-dihydroagarofuran

- Repository: CultureBotAI/AntibioticMech
- Record: data/antibiotics/antimycobacterial/1α-acetoxy-2α-hydroxy-6β-9β-15-tribenzoyloxy-β-dihydroagarofuran.yaml
- Started UTC: 2026-09-25T20:40:00Z
- Finished UTC: 2026-09-25T20:43:08Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:65774` |
| Label | `1α-acetoxy-2α-hydroxy-6β,9β,15-tribenzoyloxy-β-dihydroagarofuran` |
| Class | `ANTIMYCOBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Maintained owner | `data/raw/chebi_antimicrobials.tsv`, emitted to `data/antibiotics/antimycobacterial/1α-acetoxy-2α-hydroxy-6β-9β-15-tribenzoyloxy-β-dihydroagarofuran.yaml` |

This is a ChEBI-seeded record with one source concept:

```text
CHEBI:65774  1α-acetoxy-2α-hydroxy-6β,9β,15-tribenzoyloxy-β-dihydroagarofuran  source_version=2026-08-30
```

The ChEBI raw row contributes antimicrobial role `CHEBI:33231`
(`antitubercular agent`), xref `reaxys:11042045`, synonym
`1α-acetoxy-2α-hydroxy-6β,9β,15-tribenzoyloxy-β-dihydroagarofuran`, and source
literature lead `PMID:17315960`; the emitted `source_concepts` entry records
the ChEBI identity, minted identifier, role term, and source version.

Ignored-file-inclusive searches covered report Markdown under
`reports/yaml_record_review` plus YAML/TSV files under `curation`, `data/raw`,
and `data/antibiotics`, including all `data/antibiotics` record YAML. They
covered the identifier `CHEBI:65774`, exact label
`1α-acetoxy-2α-hydroxy-6β,9β,15-tribenzoyloxy-β-dihydroagarofuran`, path stem
`1α-acetoxy-2α-hydroxy-6β-9β-15-tribenzoyloxy-β-dihydroagarofuran`, InChIKey
`FCQBGPOADKWYEG-MNRUEBDGSA-N`, and minted identifier
`antibioticmech:chebi-aaa90ee63b`, and found only:

- the active review queue row in `curation/record_review_queue.tsv`;
- the raw ChEBI row in `data/raw/chebi_antimicrobials.tsv`;
- the generated path lock row in `data/antibiotics/PATHS.tsv`; and
- the target YAML.

There was no prior exact review report or duplicate curated YAML in the
maintained/generated corpus searched above.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antimycobacterial/1α-acetoxy-2α-hydroxy-6β-9β-15-tribenzoyloxy-β-dihydroagarofuran.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/antibiotics/antimycobacterial/1α-acetoxy-2α-hydroxy-6β-9β-15-tribenzoyloxy-β-dihydroagarofuran.yaml --out /tmp/antibioticmech-1a-acetoxy-2a-hydroxy-6b-9b-15-tribenzoyloxy-b-dihydroagarofuran-strict.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed; 2939 records expected, 2939 on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, 0 stale lockfile rows. |
| `uv run python scripts/curation_worklist.py --queue all --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-65774.tsv` | Passed; the exact rows for this record were `mechanism`, `producer-candidate`, and `review-readiness`. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-chebi-65774-review-queue.tsv` | Passed; `CHEBI:65774` is queued as `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

`just verify-corpus --summary` and the worklist regeneration printed the known
unrelated `ARO:3000337`/iclaprim CARD cross-reference warning; it did not
involve this record.

## Identity and Grounding

The generated ChEBI identity is internally consistent:

- The public ChEBI page resolved `CHEBI:65774` as a 3-star ChEBI term labeled
  `1α-acetoxy-2α-hydroxy-6β,9β,15-tribenzoyloxy-β-dihydroagarofuran`.
- ChEBI matched the record definition, formula `C38H40O10`, charge `0`,
  average mass `656.728`, monoisotopic mass `656.26215`, SMILES, Standard
  InChI, Standard InChIKey `FCQBGPOADKWYEG-MNRUEBDGSA-N`,
  `reaxys:11042045`, and `pubmed:17315960`.
- PubChem resolved InChIKey `FCQBGPOADKWYEG-MNRUEBDGSA-N` to CID `16109787`;
  CID `16109787` matched formula `C38H40O10`, Standard InChI, InChIKey, and
  the same molecular structure with a different systematic IUPAC rendering.
- ChEBI resolved the record's six stored parent terms as `CHEBI:26979`
  (`organic heterotricyclic compound`), `CHEBI:35681` (`secondary alcohol`),
  `CHEBI:35990` (`bridged compound`), `CHEBI:36054` (`benzoate ester`),
  `CHEBI:47622` (`acetate ester`), and `CHEBI:71548`
  (`dihydroagarofuran sesquiterpenoid`).
- ChEBI resolved `CHEBI:33231` as `antitubercular agent`.

The ChEBI role maps correctly to repository class `ANTIMYCOBACTERIAL`. The
only other ChEBI role on the public page is the broad `CHEBI:25212`
`metabolite` role, which is not an antimicrobial role and is correctly absent
from `activity_roles`. The exact source row in
`data/raw/chebi_antimicrobials.tsv` and path row in
`data/antibiotics/PATHS.tsv` both agree with the target YAML.

## Evidence

`PMID:17315960` resolves to Chen, Chou, Peng, Chen, and Yang,
"Antitubercular dihydroagarofuranoid sesquiterpenes from the roots of
Microtropis fokienensis", *Journal of Natural Products* 70(2):202-205,
DOI `10.1021/np060500r`.

PubMed's abstract supports the broad plant source, compound family, and assay
context behind the ChEBI entry:

- the paper isolated four new dihydroagarofuranoid sesquiterpenes, numbered
  1-4, plus a new hydroxybenzylsalicylaldehyde and nine known compounds from
  roots of `Microtropis fokienensis`;
- the new-compound structures were determined through analysis of physical
  data; and
- compounds 3, 4, 7, and 8 showed in vitro antitubercular activity against
  `Mycobacterium tuberculosis` strain 90-221387, with the abstract giving only
  a cohort-level `MIC <= 26.0 uM` statement.

The DOI resolves to ACS, but unauthenticated `curl -L` was blocked by a
Cloudflare challenge. ChEBI asserts that `CHEBI:65774` is the exact compound in
the paper, and PubMed verifies the citation metadata, but the abstract alone
does not expose which paper compound number corresponds to `CHEBI:65774` or
the exact MIC, units, and assay row for this structure.

A bounded PubMed exact-label search, PubMed exact-CURIE search, and PubMed
InChIKey search found no hits. The repository publication-search adapter wrote
zero candidates for a mechanism-focused exact-label query after Semantic
Scholar returned HTTP 429, so Semantic Scholar did not contribute a reliable
negative check.

## Completeness

The record has enough seeded information to establish a current exact ChEBI
identity, structure, source PMID, Reaxys xref, source role, filing class,
synonym, and six strictly broader ChEBI parents.

Consequential gaps remain:

- `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, and
  `causal_graph` are absent. The regenerated worklist confirms there are no
  CARD target or resistance edges to build on, and none of the inspected source
  metadata named a compound-specific molecular target or resistance mechanism.
- `activity_spectrum` is absent even though ChEBI cites a paper that tested the
  relevant compound cohort against `Mycobacterium tuberculosis` strain
  90-221387. The ACS full text is still needed to tie this exact compound to
  its paper number and exact MIC value, units, and assay.
- `producer_organisms` is absent. ChEBI and the source metadata identify roots
  of `Microtropis fokienensis` as the isolation source, ChEBI's origin metadata
  grounds that species as `NCBITaxon:1089417`, and NCBI Taxonomy resolves
  `NCBITaxon:1089417` as an active eudicot species, but isolation from a plant
  source has not yet been curated into a biosynthesis claim.

Optional clinical-status and dataset fields are correctly empty; no inspected
source suggested an approved product or public dataset specific to this exact
compound.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| F1 | Major | The record has no curated antimicrobial mechanism, molecular target, causal edge, or structured activity observation. `PMID:17315960` is the right primary-paper lead for antitubercular dihydroagarofuranoid sesquiterpenes from `M. fokienensis`, but the accessible PubMed abstract does not tie `CHEBI:65774` to a paper compound number, exact MIC, or molecular target. | Curator-owned fields on `data/antibiotics/antimycobacterial/1α-acetoxy-2α-hydroxy-6β-9β-15-tribenzoyloxy-β-dihydroagarofuran.yaml` |
| F2 | Minor | `Microtropis fokienensis` is only represented inside the generated ChEBI definition. ChEBI supports roots of this plant as the isolation source and the worklist already flags the phrase as `producer-candidate`; a curator should decide whether that is enough to add `NCBITaxon:1089417` as a plant producer with claim-level `PMID:17315960` evidence. | Curator-owned `producer_organisms` on `data/antibiotics/antimycobacterial/1α-acetoxy-2α-hydroxy-6β-9β-15-tribenzoyloxy-β-dihydroagarofuran.yaml` |

No blocker findings were found.

## Recommended Edits

1. Inspect the ACS full text for `PMID:17315960`, confirm the paper compound
   number that denotes `CHEBI:65774`, and capture its exact 90-221387 result as
   an `ActivityObservation` with measured value, units, assay, strain, and
   claim-level `PMID:17315960`/DOI evidence.
2. Search for primary literature that tests
   `1α-acetoxy-2α-hydroxy-6β,9β,15-tribenzoyloxy-β-dihydroagarofuran` against a
   named microbial molecular target. If found, add `mode_of_action`,
   `mode_of_action_target_scope`, `molecular_targets`, and edge-level
   `causal_graph` entries through the guarded writer. If no target evidence is
   found, leave mechanism fields empty and add a bounded `CURATION_TODO`
   discussion documenting the negative search.
3. Decide the `Microtropis fokienensis` producer lead. If accepted, add a
   `ProducerOrganism` with `taxon_id: NCBITaxon:1089417`,
   `taxon_label: Microtropis fokienensis`, and `PMID:17315960` evidence scoped
   to isolation of this exact compound from roots.

## Follow-up Checks

- Re-run `just validate-strict data/antibiotics/antimycobacterial/1α-acetoxy-2α-hydroxy-6β-9β-15-tribenzoyloxy-β-dihydroagarofuran.yaml --out /tmp/antibioticmech-chebi-65774-strict.tsv`
  after any record mutation.
- Re-run `just verify-corpus --summary` to ensure no seeded fields drifted while
  curator-owned fields were added.
- Re-run `just review-queue --limit 0 --tsv /tmp/antibioticmech-chebi-65774-review-queue.tsv`
  and confirm `CHEBI:65774` leaves the `MECHANISM_REVIEW` gate only after a
  supported mechanism or explicit mechanism TODO is curated.
- If a producer claim is added, re-run
  `uv run python scripts/curation_worklist.py --queue all --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-65774.tsv`
  and confirm the `producer-candidate` row is resolved.

## Additional Notes

- The exact PubMed label, CHEBI CURIE, and InChIKey searches are useful
  bounded discovery checks only; the review report above relies on ChEBI,
  PubChem, NCBI Taxonomy, and the 2007 `Microtropis fokienensis` primary-paper
  metadata for its identity, source, and broad cohort-level activity context.
  Exact `CHEBI:65774` activity remains unverified until the ACS full-text table
  is inspected.
- ChEBI records `Microtropis fokienensis` root metadata with
  `NCBITaxon:1089417`, `BTO:0001188`, and `PMID:17315960`, but the seeded YAML
  correctly omits `producer_organisms` until a curator accepts that isolation
  source as a biosynthesis claim.
