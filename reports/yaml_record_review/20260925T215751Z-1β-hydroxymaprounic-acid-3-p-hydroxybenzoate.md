# YAML Record Review: 1β-hydroxymaprounic acid 3-p-hydroxybenzoate

- Repository: CultureBotAI/AntibioticMech
- Record: data/antibiotics/antiviral/1β-hydroxymaprounic-acid-3-p-hydroxybenzoate.yaml
- Started UTC: 2026-09-25T21:57:51Z
- Finished UTC: 2026-09-25T21:57:51Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:66671` |
| Label | `1β-hydroxymaprounic acid 3-p-hydroxybenzoate` |
| Class | `ANTIVIRAL` |
| Curation status | `SEEDED` |
| Grounding status | `EXACT` |
| Maintained owner | `data/raw/chebi_antimicrobials.tsv`, emitted to `data/antibiotics/antiviral/1β-hydroxymaprounic-acid-3-p-hydroxybenzoate.yaml` and locked by `data/antibiotics/PATHS.tsv` |

The reviewed YAML is a generated ChEBI seed for `CHEBI:66671`. It contains one
ChEBI source concept with `role_terms: [CHEBI:53756]`, the ChEBI definition, two
ChEBI synonyms, three ChEBI parents, a CAS xref, a ChEBI-sourced structure, and
a source-seeded `VIRAL_POLYMERASE_INHIBITION` mode of action with
`MICROBIAL_TARGET` scope.

The record has no record-level `evidence`, `molecular_targets`,
`activity_spectrum`, `resistance_mechanisms`, `producer_organisms`,
`causal_graph`, `datasets`, `clinical_status`, or `discussions`.

The ignored-file-inclusive exact search covered `reports/yaml_record_review`,
`data`, and `curation` for `CHEBI:66671`, the exact ChEBI label, the path stem,
and an ASCII `1b-hydroxymaprounic` spelling; it found no prior review report.
The maintained record-specific hits outside generated embedding inventories were
the generated record, `data/antibiotics/PATHS.tsv`, the raw ChEBI row, and
`curation/record_review_queue.tsv`.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antiviral/1β-hydroxymaprounic-acid-3-p-hydroxybenzoate.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/antibiotics/antiviral/1β-hydroxymaprounic-acid-3-p-hydroxybenzoate.yaml --out /tmp/antibioticmech-chebi-66671-strict.tsv` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just verify-corpus --summary` | Passed; 2,939 records on disk exactly reproduce from `data/raw/` plus curator inputs. The only diagnostic was the known unrelated CARD `iclaprim` self-contradictory cross-reference refusal. |
| `uv run python scripts/curation_worklist.py --queue all --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-66671.tsv` | Passed; the exact `CHEBI:66671` rows were `mechanism`, `producer-candidate`, `activity-candidate`, and `review-readiness`. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-chebi-66671-review-queue.tsv` | Passed; `CHEBI:66671` is queued as `MECHANISM_REVIEW: mechanism is source-seeded and not curator-checked; 1 source literature lead(s), 0 record evidence item(s), 0 target(s)`. |
| Source-map lookup in `conf/sources.yaml` | Passed; `CHEBI:53756` maps to `ANTIVIRAL`, `VIRAL_POLYMERASE_INHIBITION`, and `MICROBIAL_TARGET`, matching the generated class, mode, and target scope. |
| Live OLS4 `CHEBI:66671`, parent, and role-term lookups | Passed; `CHEBI:66671` is current and non-obsolete with the same formula, Standard InChIKey, CAS xref, and PubMed xref as the YAML/raw row. Its direct OLS parents are current, non-obsolete `CHEBI:25872`, `CHEBI:35868`, and `CHEBI:36054`; the role term `CHEBI:53756` resolves as current, non-obsolete `HIV-1 reverse transcriptase inhibitor`. |
| PubChem InChIKey lookup for `VGODRAUARQJBJM-FCWPOGGHSA-N` | Passed; PubChem CID `3081903` has the same formula, Standard InChI, Standard InChIKey, exact mass, and charge as the YAML, and lists the ChEBI ID, CAS, and ChEBI IUPAC synonym for this structure. |
| PubMed EFetch for `PMID:7515410` and `PMID:7561895` | Passed; the PMIDs resolve to Pengsuparp et al. 1994, DOI `10.1021/np50105a017`, and Pengsuparp et al. 1995, DOI `10.1021/np50121a006`. |
| ACS DOI fetch for `10.1021/np50105a017` | Blocked; unauthenticated `curl` reached an ACS Cloudflare challenge, so the 1994 full-text structure and assay table were not inspected. |
| NCBI Taxonomy lookup for `Maprounea africana` | Passed; the scientific-name search resolves to active species `NCBITaxon:316848`. |
| `scripts/search_publications.py` PubMed/Semantic Scholar searches for exact label, InChIKey, CAS, `HIV-1 reverse transcriptase`, `Maprounea`, and `1 beta-hydroxyaleuritolic acid` terms | Partially passed; PubMed found the 1994 and 1995 leads above, and Semantic Scholar returned HTTP 429 under its unauthenticated rate limit. |

## Identity and Grounding

- `CHEBI:66671` is the correct ChEBI grounding for the exact neutral structure
  in the generated record. The live OLS4 term, committed raw row, generated
  YAML, and PubChem CID `3081903` agree on Standard InChIKey
  `VGODRAUARQJBJM-FCWPOGGHSA-N`, formula `C37H52O6`, charge `0`, Standard
  InChI, and monoisotopic mass.
- The direct ChEBI parents are current, non-obsolete `CHEBI:25872` pentacyclic
  triterpenoid, `CHEBI:35868` hydroxy monocarboxylic acid, and `CHEBI:36054`
  benzoate ester. All are broader chemical classes, not exact-identity xrefs.
- `activity_roles: [CHEBI:53756]` preserves the raw ChEBI source role used by
  the seeder. The source map files the role under `ANTIVIRAL`, maps the coarse
  mechanism to `VIRAL_POLYMERASE_INHIBITION`, and derives `MICROBIAL_TARGET`
  scope because HIV-1 reverse transcriptase is viral.
- The CAS xref `cas:155510-77-3` resolves through both PubMed indexing for the
  1994 paper and PubChem CID `3081903` synonym metadata for the same InChIKey.

## Evidence

The current YAML inherits ChEBI database provenance and a seeded mechanism
restatement but has no primary-paper `molecular_targets`, quantitative target
measurements, organism-level activity observations, producer evidence, or
causal-graph edges.

| Lead | Supports the antiviral record? | Review |
|---|---|---|
| `PMID:7515410` / `DOI:10.1021/np50105a017` | Bibliographic and database-indexed support for the Maprounea triterpene HIV-1 reverse-transcriptase lead, but not enough accessible full-text support to curate exact assay details. | PubMed resolves the paper titled "Pentacyclic triterpenes derived from Maprounea africana are potent inhibitors of HIV-1 reverse transcriptase" and indexes CAS `155510-77-3` under `1-hydroxymaprounic 3-p-hydroxybenzoate`; however, the PubMed record has no abstract, and ACS blocked unauthenticated full-text inspection. |
| `PMID:7561895` / `DOI:10.1021/np50121a006` | Strong follow-up mechanism lead for a Maprounea-derived triterpene on HIV-1 reverse transcriptase. | The accessible abstract reports `1 beta-hydroxyaleuritolic acid 3-p-hydroxybenzoate` as compound 2 from *Maprounea africana* roots, gives an HIV-1 reverse-transcriptase DNA-polymerase IC50 of 3.7 micromolar, and reports kinetic data consistent with nonspecific binding to the enzyme at non-substrate sites. A curator should inspect the full article or a synonym authority before treating the `aleuritolic` and `maprounic` labels as exactly equivalent. |
| ChEBI `CHEBI:66671` | Exact seeded identity and role support. | The live term repeats the same formula, Standard InChIKey, CAS xref, and PubMed xref as the generated YAML; the committed raw ChEBI row supplies `CHEBI:53756` as the source `HIV-1 reverse transcriptase inhibitor` role. |
| PubChem CID `3081903` | Secondary structure and registry cross-check. | PubChem resolves the record InChIKey to the same neutral structure, formula, exact mass, ChEBI ID, CAS, and IUPAC synonym. It does not list the `1 beta-hydroxyaleuritolic acid` alternate name used in the 1995 PubMed abstract. |
| NCBI Taxonomy `NCBITaxon:316848` | Exact plant taxon check for a future producer decision. | NCBI resolves *Maprounea africana* as an active species; this verifies the candidate taxon but does not itself decide whether plant isolation should become a structured producer claim. |

## Completeness

- **Mechanism and target:** partially complete. The seeded
  `VIRAL_POLYMERASE_INHIBITION` value is correctly traceable to ChEBI role
  `CHEBI:53756`, but the YAML has no curator-checked `MolecularTarget` for
  HIV-1 reverse transcriptase and no primary evidence object or IC50 measurement
  from `PMID:7561895`.
- **Activity:** incomplete. ChEBI's source row states activity against HIV-1
  reverse transcriptase rather than against a named virus, cell line, or host
  organism. The worklist therefore emits only a subjectless `activity-candidate`
  row, and no inspected source exposed a structured virus-level activity assay
  to encode.
- **Producer:** incomplete. The definition and source literature support
  *Maprounea africana* as the plant source for this compound or a close alternate
  label, and NCBI resolves the species as `NCBITaxon:316848`, but the YAML has
  no `producer_organisms` entry.
- **Resistance:** empty and not currently consequential. This ChEBI-only
  antiviral record has no CARD targets or resistance mechanisms to build on.
- **Clinical status and datasets:** empty and not currently consequential for
  this plant natural-product reverse-transcriptase inhibitor seed. No inspected
  source exposed a regulatory product or durable dataset accession for the exact
  compound.
- **Discussions:** empty. If the 1994 ACS table remains inaccessible, a future
  curation pass should either resolve exact identity/activity from the full
  text or add a `CURATION_TODO` that names the remaining paper-table gap.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| F1 | Major | The record has a seeded HIV-1 reverse-transcriptase mode and scope but lacks a curator-owned molecular target with claim-level evidence. `PMID:7561895` is a strong follow-up mechanism lead reporting HIV-1 RT inhibition and a 3.7 micromolar IC50 for a Maprounea triterpene, but the exact `CHEBI:66671` synonym bridge to the paper's `1 beta-hydroxyaleuritolic acid 3-p-hydroxybenzoate` name still needs a full-text or registry check before the target assertion is curated. | Curator-owned `molecular_targets`, `mode_of_action_notes`, and optional target-measurement fields on `data/antibiotics/antiviral/1β-hydroxymaprounic-acid-3-p-hydroxybenzoate.yaml`, written through `write_validated_antibiotic` with a specific `CurationEvent`. |
| F2 | Minor | *Maprounea africana* is only represented inside the generated definition. PubMed and ChEBI tie the compound or close alternate Maprounea triterpene label to this plant source, NCBI resolves the species as `NCBITaxon:316848`, and the regenerated worklist still flags the phrase as a `producer-candidate`. | Curator-owned `producer_organisms` on `data/antibiotics/antiviral/1β-hydroxymaprounic-acid-3-p-hydroxybenzoate.yaml`, if the corpus elects to represent this higher-plant natural-product source structurally. |

No blocker findings were found.

## Recommended Edits

1. Inspect the ACS full text for `PMID:7515410` and `PMID:7561895`, or an
   equivalent stable registry, to prove whether the 1995 abstract's alternate
   `1 beta-hydroxyaleuritolic acid 3-p-hydroxybenzoate` label denotes the exact
   same structure as `CHEBI:66671`; then add an HIV-1 reverse-transcriptase
   `MolecularTarget` with `PMID:7561895` evidence and the reported 3.7
   micromolar IC50 only if the synonym bridge is exact.
2. If the target is curated, claim the source-seeded `mode_of_action` with a
   `CURATOR:` note that cites the primary target evidence while preserving
   `VIRAL_POLYMERASE_INHIBITION` and `MICROBIAL_TARGET` scope.
3. Add a `CURATION_TODO` discussion if the 1994 ACS paper remains inaccessible
   and the exact compound number, structure table, or assay table cannot be
   inspected.
4. Decide whether isolation from *Maprounea africana* should become a structured
   plant `ProducerOrganism`; if yes, add `NCBITaxon:316848` with narrow
   `PMID:7515410` evidence after the full-text source is inspected.
5. Leave the seeded ChEBI identifier, structure, parent terms, role term, and CAS
   xref untouched unless the ChEBI inventory or extractor changes them; ChEBI,
   PubChem, PubMed CAS indexing, and the committed raw row agree on the identity
   that the current record denotes.

## Follow-up Checks

- Re-run `just validate-strict data/antibiotics/antiviral/1β-hydroxymaprounic-acid-3-p-hydroxybenzoate.yaml --out /tmp/antibioticmech-chebi-66671-strict.tsv`
  after any curator-owned target or producer edit.
- Re-run `just verify-corpus --summary` to confirm the new curator-owned
  mechanism and producer fields survive reseeding rather than creating
  generated-record drift.
- Re-run `uv run python scripts/curation_worklist.py --queue all --limit 0 --tsv /tmp/antibioticmech-worklist-chebi-66671.tsv`
  and confirm `CHEBI:66671` leaves the `mechanism` and `producer-candidate` rows
  only after primary evidence has been attached or an explicit discussion has
  been added.
- Re-run `just review-queue --limit 0 --tsv /tmp/antibioticmech-chebi-66671-review-queue.tsv`
  and confirm `CHEBI:66671` leaves the source-seeded `MECHANISM_REVIEW` gate
  only after a curator has checked its reverse-transcriptase mechanism.
- Manually reread the YAML after writing molecular-target evidence to verify
  HIV-1 reverse transcriptase is represented as a viral target rather than as an
  organism-specific protein accession.

## Additional Notes

- The exact `1β-hydroxymaprounic acid 3-p-hydroxybenzoate` label did not appear
  in the accessible `PMID:7561895` abstract; that abstract instead used the
  `1 beta-hydroxyaleuritolic acid 3-p-hydroxybenzoate` alternate label for
  compound 2. PubChem CID `3081903` does not list that `aleuritolic` synonym, so
  the synonym bridge needs an inspected full-text or registry source before the
  mechanism paper can be used as exact CHEBI:66671 target evidence.
- The repository publication adapter found `PMID:7515410` and `PMID:7561895`
  through PubMed; Semantic Scholar was rate-limited on the unauthenticated exact
  searches, so the publication search should be treated as bounded rather than
  exhaustive.
