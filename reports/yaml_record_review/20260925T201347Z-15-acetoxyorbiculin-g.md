# YAML Record Review: 15-acetoxyorbiculin G

- Repository: CultureBotAI/AntibioticMech
- Record: data/antibiotics/antimycobacterial/15-acetoxyorbiculin-g.yaml
- Started UTC: 2026-09-25T20:07:00Z
- Finished UTC: 2026-09-25T20:13:48Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:65364` |
| Label | `15-acetoxyorbiculin G` |
| Class | `ANTIMYCOBACTERIAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Maintained owner | `data/raw/chebi_antimicrobials.tsv`, emitted to `data/antibiotics/antimycobacterial/15-acetoxyorbiculin-g.yaml` |

This is a ChEBI-seeded record with one source concept:

```text
CHEBI:65364  15-acetoxyorbiculin G  source_version=2026-08-30
```

The ChEBI raw row contributes antimicrobial role `CHEBI:33231`
(`antitubercular agent`), xref `reaxys:18842487`, and source literature
lead `PMID:18471021`; the emitted `source_concepts` entry records the
ChEBI identity, minted identifier, role term, and source version.

Ignored-file-inclusive searches covered report Markdown under
`reports/yaml_record_review` plus YAML/TSV files under `curation`, `data/raw`,
and `data/antibiotics`, including all `data/antibiotics` record YAML. They
covered the identifier `CHEBI:65364`, exact label `15-acetoxyorbiculin G`,
InChIKey `YOWBCRNBOMRTPW-NPIRVHPYSA-N`, minted identifier
`antibioticmech:chebi-d8d395979b`, and path slug `15-acetoxyorbiculin-g`, and
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
| `just validate data/antibiotics/antimycobacterial/15-acetoxyorbiculin-g.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/antibiotics/antimycobacterial/15-acetoxyorbiculin-g.yaml --out /tmp/antibioticmech-15-acetoxyorbiculin-g-strict.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed; 2939 records expected, 2939 on disk, 0 missing, 0 unexpected, 0 drifted fields, 0 identifiers absent from `PATHS.tsv`, 0 stale lockfile rows. |
| `uv run python scripts/curation_worklist.py --queue all --limit 0 --tsv /tmp/antibioticmech-worklist-15-acetoxyorbiculin-g.tsv` | Passed; the exact rows for this record were `mechanism`, `producer-candidate`, and `review-readiness`. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-15-acetoxyorbiculin-g-review-queue.tsv` | Passed; `CHEBI:65364` is queued as `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |

`just verify-corpus --summary` and the worklist regeneration printed the known
unrelated `ARO:3000337`/iclaprim CARD cross-reference warning; it did not
involve this record.

## Identity and Grounding

The generated ChEBI identity is internally consistent:

- The public ChEBI page resolved `CHEBI:65364` as a 3-star ChEBI term labeled
  `15-acetoxyorbiculin G`.
- ChEBI matched the record definition, formula `C40H42O11`, charge `0`,
  average mass `698.765`, monoisotopic mass `698.27271`, SMILES, Standard
  InChI, Standard InChIKey `YOWBCRNBOMRTPW-NPIRVHPYSA-N`,
  `reaxys:18842487`, and `pubmed:18471021`.
- PubChem resolved both `15-acetoxyorbiculin G` and InChIKey
  `YOWBCRNBOMRTPW-NPIRVHPYSA-N` to CID `24898039`; CID `24898039` matched
  formula `C40H42O11`, Standard InChI, InChIKey, and the same molecular
  structure with a different systematic IUPAC rendering.
- ChEBI resolved the record's five stored parent terms as `CHEBI:26979`
  (`organic heterotricyclic compound`), `CHEBI:35990` (`bridged compound`),
  `CHEBI:36054` (`benzoate ester`), `CHEBI:37407` (`cyclic ether`), and
  `CHEBI:71548` (`dihydroagarofuran sesquiterpenoid`).
- ChEBI resolved `CHEBI:33231` as `antitubercular agent`.

The ChEBI role maps correctly to repository class `ANTIMYCOBACTERIAL`.
ChEBI also records `CHEBI:66828` orbiculin G as a functional parent, but that
edge is related-structure provenance for a 15-acetoxy derivative rather than a
strictly broader `is_a` parent and is correctly absent from
`parent_compounds`. The exact source row in `data/raw/chebi_antimicrobials.tsv`
and path row in `data/antibiotics/PATHS.tsv` both agree with the target YAML.

## Evidence

`PMID:18471021` resolves to Chen, Yang, Peng, Chen, and Miaw,
"Dihydroagarofuranoid sesquiterpenes, a lignan derivative, a benzenoid, and
antitubercular constituents from the stem of Microtropis japonica", *Journal
of Natural Products* 71(6):1016-1021, DOI `10.1021/np800097t`.

PubMed's abstract supports the broad identity and activity claims that ChEBI
copied into the definition:

- the paper isolated compound 2, `15-acetoxyorbiculin G`, from the stem of
  `Microtropis japonica`;
- the paper reports `15-acetoxyorbiculin G` as one of two new
  dihydroagarofuranoid sesquiterpenes and says the new-compound structures
  were determined through analysis of physical data; and
- the paper reports antituberculosis activity for `15-acetoxyorbiculin G`
  against `Mycobacterium tuberculosis` H37Rv in vitro, with the abstract
  giving only a cohort-level `MIC <= 39.6 uM` bound for compounds 2, 6, and 7.

The DOI resolves to ACS, but unauthenticated `curl -L` was blocked by a
Cloudflare challenge. PubMed supplied the citation metadata and abstract, but
the original MIC table, assay method, and any additional organism rows were
not inspected.

A bounded PubMed exact-label search found only `PMID:18471021`; exact PubMed
searches for `CHEBI:65364` and `YOWBCRNBOMRTPW-NPIRVHPYSA-N` found no hits.
The repository publication-search adapter wrote zero candidates for a
mechanism-focused exact-label query after Semantic Scholar returned HTTP 429,
so Semantic Scholar did not contribute a reliable negative check.

## Completeness

The record has enough seeded information to establish a current exact ChEBI
identity, structure, source PMID, Reaxys xref, source role, filing class, and
five strictly broader ChEBI parents.

Consequential gaps remain:

- `mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`, and
  `causal_graph` are absent. The regenerated worklist confirms there are no
  CARD target or resistance edges to build on, and none of the inspected source
  metadata named a compound-specific molecular target or resistance mechanism.
- `activity_spectrum` is absent even though the source abstract says the exact
  compound was tested against `Mycobacterium tuberculosis` H37Rv
  (`NCBITaxon:83332`). The full ACS table is still needed for the exact MIC
  value, units, and assay.
- `producer_organisms` is absent. ChEBI and the source abstract identify
  `Microtropis japonica` stems as the isolation source, ChEBI's origin metadata
  grounds that species as `NCBITaxon:1089418`, and NCBI Taxonomy resolves
  `NCBITaxon:1089418` as an active eudicot species, but isolation from a plant
  source has not yet been curated into a biosynthesis claim.

Optional clinical-status and dataset fields are correctly empty; no inspected
source suggested an approved product or public dataset specific to this exact
compound.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| F1 | Major | The record has no curated antimicrobial mechanism, molecular target, causal edge, or structured H37Rv activity observation. `PMID:18471021` verifies qualitative antitubercular activity against `M. tuberculosis` H37Rv for this exact compound, but the original ACS table remains uninspected and no source inspected during this review identified a supported molecular target or machine-readable activity value for `15-acetoxyorbiculin G`. | Curator-owned fields on `data/antibiotics/antimycobacterial/15-acetoxyorbiculin-g.yaml` |
| F2 | Minor | `Microtropis japonica` is only represented inside the generated ChEBI definition. ChEBI and the paper abstract support stems of this plant as the isolation source and the worklist already flags the phrase as `producer-candidate`; a curator should decide whether that is enough to add `NCBITaxon:1089418` as a plant producer with claim-level `PMID:18471021` evidence. | Curator-owned `producer_organisms` on `data/antibiotics/antimycobacterial/15-acetoxyorbiculin-g.yaml` |

No blocker findings were found.

## Recommended Edits

1. Inspect the ACS full text for `PMID:18471021`, capture compound 2's exact
   H37Rv result as an `ActivityObservation` with `taxon_id: NCBITaxon:83332`,
   strain `H37Rv`, measured value, units, assay, and claim-level
   `PMID:18471021`/DOI evidence.
2. Search for primary literature that tests `15-acetoxyorbiculin G` against a
   named microbial molecular target. If found, add `mode_of_action`,
   `mode_of_action_target_scope`, `molecular_targets`, and edge-level
   `causal_graph` entries through the guarded writer. If no target evidence is
   found, leave mechanism fields empty and add a bounded `CURATION_TODO`
   discussion documenting the negative search.
3. Decide the `Microtropis japonica` producer lead. If accepted, add a
   `ProducerOrganism` with `taxon_id: NCBITaxon:1089418`,
   `taxon_label: Microtropis japonica`, and `PMID:18471021` evidence scoped to
   isolation of 15-acetoxyorbiculin G from stems.

## Follow-up Checks

- Re-run `just validate-strict data/antibiotics/antimycobacterial/15-acetoxyorbiculin-g.yaml --out /tmp/antibioticmech-15-acetoxyorbiculin-g-strict.tsv`
  after any record mutation.
- Re-run `just verify-corpus --summary` to ensure no seeded fields drifted while
  curator-owned fields were added.
- Re-run `just review-queue --limit 0 --tsv /tmp/antibioticmech-15-acetoxyorbiculin-g-review-queue.tsv`
  and confirm `CHEBI:65364` leaves the `MECHANISM_REVIEW` gate only after a
  supported mechanism or explicit mechanism TODO is curated.
- If a producer claim is added, re-run
  `uv run python scripts/curation_worklist.py --queue all --limit 0 --tsv /tmp/antibioticmech-worklist-15-acetoxyorbiculin-g.tsv`
  and confirm the `producer-candidate` row is resolved.

## Additional Notes

- ChEBI imports the activity role and xref but not the DOI/PMID into
  `source_concepts.evidence`; source literature leads remain in
  `data/raw/chebi_antimicrobials.tsv` and the derived review queue.
- The exact PubMed label, CHEBI CURIE, and InChIKey searches are useful
  bounded discovery checks only; the review report above relies on ChEBI,
  PubChem, NCBI Taxonomy, and the cited 2008 primary experiment for its
  identity, source, and H37Rv activity judgements.
