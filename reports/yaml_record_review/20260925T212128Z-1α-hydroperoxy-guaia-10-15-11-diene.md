# YAML Record Review: 1α-hydroperoxy-guaia-10(15),11-diene

- Repository: CultureBotAI/AntibioticMech
- Record: data/antibiotics/antiprotozoal/1α-hydroperoxy-guaia-10-15-11-diene.yaml
- Started UTC: 2026-09-25T21:21:28Z
- Finished UTC: 2026-09-25T21:21:28Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:66473` |
| Label | `1α-hydroperoxy-guaia-10(15),11-diene` |
| Class | `ANTIPROTOZOAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Maintained owner | `data/raw/chebi_antimicrobials.tsv`, emitted to `data/antibiotics/antiprotozoal/1α-hydroperoxy-guaia-10-15-11-diene.yaml` and locked by `data/antibiotics/PATHS.tsv` |

The reviewed YAML is a generated ChEBI seed for `CHEBI:66473`. It contains one
ChEBI source concept with `role_terms: [CHEBI:36335]`, the ChEBI definition, one
ChEBI IUPAC synonym, two ChEBI parents, a ChEBI-sourced structure, and one
`reaxys` xref.

The record has no record-level `evidence`, `mode_of_action`,
`mode_of_action_target_scope`, `mode_of_action_notes`, `molecular_targets`,
`activity_spectrum`, `resistance_mechanisms`, `producer_organisms`,
`causal_graph`, `datasets`, `clinical_status`, or `discussions`.

The ignored-file-inclusive exact search covered `reports/yaml_record_review`,
`data`, and `curation` for `CHEBI:66473`, the exact ChEBI label,
`1α-hydroperoxy-guaia`, and `1a-hydroperoxy-guaia`; it found no prior review
report and only the generated record, `data/antibiotics/PATHS.tsv`, the raw
ChEBI row, and `curation/record_review_queue.tsv`.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antiprotozoal/1α-hydroperoxy-guaia-10-15-11-diene.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/antibiotics/antiprotozoal/1α-hydroperoxy-guaia-10-15-11-diene.yaml --out /tmp/antibioticmech-chebi-66473-strict.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed; 2,939 records on disk exactly reproduce from `data/raw/` plus curator inputs. The only diagnostic was the known unrelated CARD `iclaprim` self-contradictory cross-reference refusal. |
| `uv run python scripts/curation_worklist.py --queue all --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-66473.tsv` | Passed; the exact `CHEBI:66473` rows were `mechanism`, `producer-candidate`, and `review-readiness`. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-chebi-66473-review-queue.tsv` | Passed; `CHEBI:66473` is queued as `MECHANISM_REVIEW: mechanism is absent; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| Live OLS4 `CHEBI:66473`, parent, and role-term lookups | Passed; `CHEBI:66473` is current and non-obsolete with the same formula, charge, mass values, Standard InChI, InChIKey, SMILES, PubMed xref, Reaxys xref, and direct parents `CHEBI:35924` and `CHEBI:36744`. The role term `CHEBI:36335` resolved as current, non-obsolete `trypanocidal drug`. |
| PubChem InChIKey lookup for `LSSAEGXLQBRSBC-PMOUVXMZSA-N` | Passed; PubChem CID `11481776` has the same formula, Standard InChI, Standard InChIKey, exact mass, and charge as the YAML. |
| PubMed EFetch for `PMID:15577255` | Passed; the PMID resolves to Kiuchi et al. 2004, *Chemical & Pharmaceutical Bulletin* 52(12):1495-1496, DOI `10.1248/cpb.52.1495`. |
| J-STAGE PDF for `DOI:10.1248/cpb.52.1495` | Passed; the publisher PDF was downloadable and inspectable. |
| NCBI Taxonomy lookup for `Pogostemon cablin` | Passed; the scientific-name search resolves to active species `NCBITaxon:28511`. |
| `scripts/search_publications.py` PubMed/Semantic Scholar searches for the exact label, InChIKey, ASCII `1a` label, and mechanism terms | Partially passed; exact PubMed searches wrote 0 candidates and Semantic Scholar returned HTTP 429 under its unauthenticated rate limit. A broader `Trypanosoma cruzi` query returned off-target 2026 PubMed hits and no useful CHEBI:66473 mechanism lead. |

## Identity and Grounding

- `CHEBI:66473` is the correct ChEBI grounding for the exact sesquiterpene
  hydroperoxide named by this record. Live OLS4, the committed raw ChEBI row,
  the generated YAML, and PubChem CID `11481776` agree on Standard InChIKey
  `LSSAEGXLQBRSBC-PMOUVXMZSA-N`, formula `C15H24O2`, charge `0`, Standard
  InChI, and monoisotopic mass.
- The direct ChEBI parents are current, non-obsolete `CHEBI:35924` `peroxol`
  and `CHEBI:36744` `guaiane sesquiterpenoid`. Both are broader chemical
  classes rather than exact-identity xrefs.
- `activity_roles: [CHEBI:36335]` preserves ChEBI's `trypanocidal drug` role
  and correctly files the record as `ANTIPROTOZOAL`.
- The IUPAC synonym in the YAML matches the ChEBI synonym from the committed raw
  row and the live OLS4 term.
- `reaxys:9928499` is inherited from ChEBI as an exact external registry xref.

## Evidence

The current YAML inherits ChEBI database provenance but does not yet encode
primary-paper activity, target, mechanism, resistance, producer, or causal-graph
evidence.

| Lead | Supports the antiprotozoal record? | Review |
|---|---|---|
| `PMID:15577255` / `DOI:10.1248/cpb.52.1495` | Exact identity, plant source, and trypanocidal activity support for compound 2. | Kiuchi et al. 2004 reports activity-guided isolation of three hydroperoxides from dried *Pogostemon cablin* herb, identifies compound 2 as `1a-hydroperoxy-guaia-10(15),11-diene`, reports the same `C15H24O2` formula, and measures a minimum lethal concentration of 1.7 micromolar against *Trypanosoma cruzi* epimastigotes. The paper does not report a molecular target. |
| ChEBI `CHEBI:66473` | Exact seeded identity and role support. | The live term repeats the same formula, Standard InChI, InChIKey, SMILES, Reaxys xref, and PubMed xref as the generated YAML; the committed raw ChEBI row supplies `CHEBI:36335` as the imported `trypanocidal drug` role. |
| PubChem CID `11481776` | Secondary structure cross-check. | PubChem resolves the record InChIKey to the same neutral structure and formula; this is useful identifier corroboration, not source evidence for the assay. |
| NCBI Taxonomy `NCBITaxon:28511` | Exact plant taxon check for a future producer decision. | NCBI resolves *Pogostemon cablin* as an active species. This verifies the candidate taxon, but a future curation pass still needs to decide whether an isolated-higher-plant source should be structured as a `ProducerOrganism`. |
| Exact PubMed/Semantic Scholar mechanism searches | No additional inspected mechanism evidence. | The exact label and InChIKey searches found no PubMed candidates; Semantic Scholar was rate-limited. The bounded search did not identify a primary source that assigns a molecular target or mode of action to compound 2. |

## Completeness

- **Mechanism:** incomplete. The record has no `mode_of_action`, target scope,
  molecular target, or causal edge, and neither ChEBI nor the inspected Kiuchi et
  al. 2004 paper establishes an exact molecular target for compound 2's
  trypanocidal activity.
- **Activity:** incomplete. Kiuchi et al. 2004 reports compound 2 with a 1.7
  micromolar minimum lethal concentration against *Trypanosoma cruzi* Tulahuen
  strain epimastigotes in a 24-hour duplicate microscopic motility assay, but
  the YAML has no `ActivityObservation` encoding the organism, strain, endpoint,
  value, units, and method.
- **Producer:** incomplete. The source paper supports dried *Pogostemon cablin*
  herb as the plant material from which compound 2 was isolated, and the
  worklist correctly keeps this as a `producer-candidate` marked `SOURCE only`
  until a curator decides whether to add `NCBITaxon:28511` as a structured plant
  producer with primary-paper evidence.
- **Resistance:** empty and not currently a consequential gap. This ChEBI-only
  antiprotozoal seed has no CARD targets or resistance edges to build on.
- **Clinical status and datasets:** empty and not currently consequential for
  this plant natural-product seed; no inspected source identified a regulatory
  product or accessioned dataset for the exact compound.
- **Discussions:** empty. Missing mechanism, assay extraction, and plant
  producer representation are concrete follow-up tasks; if a future pass cannot
  support a molecular target, the record should carry an explicit
  `CURATION_TODO` discussion or curated mechanism veto instead of leaving the
  absence unexplained.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| F1 | Major | The exact trypanocidal record has primary assay support but lacks a curated `ActivityObservation`, mode of action, molecular target, causal graph, or explicit unresolved mechanism discussion. The YAML is `SEEDED` from ChEBI with role `CHEBI:36335`; it has no claim-level evidence objects, and regenerated queues keep `CHEBI:66473` in `mechanism` and `review-readiness` with 0 targets and 0 record evidence items. | Curator-owned additions on `data/antibiotics/antiprotozoal/1α-hydroperoxy-guaia-10-15-11-diene.yaml`, written through `write_validated_antibiotic` with a specific `CurationEvent`. |
| F2 | Minor | *Pogostemon cablin* is only represented inside the generated definition. Kiuchi et al. 2004 supports the plant as the source material, NCBI resolves the species as `NCBITaxon:28511`, and the regenerated worklist still flags the phrase as a `producer-candidate`. | Curator-owned `producer_organisms` on `data/antibiotics/antiprotozoal/1α-hydroperoxy-guaia-10-15-11-diene.yaml`, if the corpus elects to represent this higher-plant natural-product source structurally. |

No blocker findings were found.

## Recommended Edits

1. Add an `ActivityObservation` for Kiuchi et al. 2004 after extracting the exact
   assay semantics for compound 2: *Trypanosoma cruzi* Tulahuen strain
   epimastigotes, minimum lethal concentration, 1.7 micromolar, 24-hour
   incubation, duplicate microscopic motility endpoint, and solvent/control
   context where representable.
2. Search beyond the exact label and InChIKey for any primary paper that tests
   `1α-hydroperoxy-guaia-10(15),11-diene` against a named microbial molecular
   target. If none is found, add a `CURATION_TODO` discussion or curated
   `UNKNOWN`/mechanism veto rather than inferring a mechanism from the
   hydroperoxide group.
3. Decide whether the isolation of compound 2 from dried *Pogostemon cablin*
   herb should become a structured `ProducerOrganism`; if yes, add the active
   species taxon `NCBITaxon:28511` with claim-level `PMID:15577255` evidence.
4. Leave the seeded ChEBI identifier, class, activity role, structure, parent
   terms, and Reaxys xref untouched unless the ChEBI inventory or extractor
   changes them; the live ChEBI, PubChem, primary-paper, and committed raw
   identity fields agree.

## Follow-up Checks

- Re-run `just validate-strict data/antibiotics/antiprotozoal/1α-hydroperoxy-guaia-10-15-11-diene.yaml --out /tmp/antibioticmech-chebi-66473-strict.tsv`
  after any curator-owned edit.
- Re-run `just verify-corpus --summary` to confirm any new curator-owned fields
  survive reseeding rather than creating generated-record drift.
- Re-run `uv run python scripts/curation_worklist.py --queue all --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-66473.tsv`
  and confirm `CHEBI:66473` leaves the `producer-candidate` row if a producer is
  added and leaves `mechanism` or carries an intentional unresolved discussion
  if a mechanism is vetoed.
- Re-run `just review-queue --limit 0 --tsv /tmp/antibioticmech-chebi-66473-review-queue.tsv`
  and confirm `CHEBI:66473` leaves the `MECHANISM_REVIEW` gate only after a
  curator has checked and documented the missing mechanism.
- Manually reread the YAML after writing activity, producer, or mechanism
  evidence to verify each citation sits on the narrow assay, organism, target,
  or edge it supports.

## Additional Notes

- The J-STAGE PDF text extraction used `pypdf` through `uvx` because neither a
  PDF library nor `pdftotext` was available in the project environment. The
  extracted text contained font-encoding artifacts around symbols such as alpha,
  micro, and greater-than signs, but the compound 2 structural conclusion,
  formula, assay row, DOI, title, authors, and Tulahuen-strain method were
  readable enough for this identity and activity review.
- A broad repository publication search for the CHEBI:66473 label joined by OR
  to the InChIKey and `Trypanosoma cruzi` terms returned off-target 2026 PubMed
  results about Chagas disease or unrelated compounds. Those rows were treated
  as search noise, not near-miss evidence.
