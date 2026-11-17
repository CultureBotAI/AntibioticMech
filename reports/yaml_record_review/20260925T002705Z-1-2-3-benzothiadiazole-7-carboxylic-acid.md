# YAML Record Review: 1,2,3-benzothiadiazole-7-carboxylic acid

- Repository: CultureBotAI/AntibioticMech
- Record: `data/antibiotics/antifungal/1-2-3-benzothiadiazole-7-carboxylic-acid.yaml`
- Started UTC: 2026-09-25T00:21:30Z
- Finished UTC: 2026-09-25T00:27:05Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `CHEBI:141405` |
| Label | `1,2,3-benzothiadiazole-7-carboxylic acid` |
| Path | `data/antibiotics/antifungal/1-2-3-benzothiadiazole-7-carboxylic-acid.yaml` |
| Record class | `AntibioticRecord` |
| Generated or maintained | Generated from `data/raw/chebi_antimicrobials.tsv` plus `data/antibiotics/PATHS.tsv` |
| `antimicrobial_class` | `ANTIFUNGAL` |
| `curation_status` | `SEEDED` |
| `grounding_status` | `EXACT` |
| Source concepts | `CHEBI:141405`, ChEBI `2026-08-30`, roles `CHEBI:24127` and `CHEBI:86328` |
| Structure key | `COAIOOWBEPAOFY-UHFFFAOYSA-N` |

The full 65-line YAML record was read before reviewing claims. The record is a
ChEBI-seeded antifungal agrochemical with a ChEBI structure, no record-level
`evidence`, no `mode_of_action`, no `molecular_targets`, no
`activity_spectrum`, no `producer_organisms`, no `resistance_mechanisms`, no
`causal_graphs`, no `datasets`, no `discussions`, and only the three
seed/reseed history events from 2026-08-30.

## Validation

| Check | Result |
|---|---|
| `just validate data/antibiotics/antifungal/1-2-3-benzothiadiazole-7-carboxylic-acid.yaml` | Passed: `No issues found`. |
| `just validate-strict data/antibiotics/antifungal/1-2-3-benzothiadiazole-7-carboxylic-acid.yaml --out /tmp/benzothiadiazole-141405-validate-strict.tsv` | Passed: scanned 1 file with 0 ERROR rows. |
| `just verify-corpus --summary` | Passed: 2,939 records expected and on disk; 0 missing, unexpected, drifted, `PATHS.tsv`, or stale-lockfile rows. The only diagnostic printed was the known unrelated `iclaprim` / `CHEBI:31724` CARD cross-reference refusal. |
| `just worklist` | Passed and rebuilt the curation backlog. `CHEBI:141405` is on `review-readiness` and owes `MECHANISM_REVIEW`. |
| `just review-queue --limit 0 --tsv /tmp/antibioticmech-review-queue.tsv` | Passed and wrote the full 2,859-row review-readiness queue. |
| Hidden-inclusive target/xref search | Passed for the bounded review. `rg --no-ignore --hidden` over `data/antibiotics`, `data/raw`, `curation`, `reports/yaml_record_review`, `/tmp/antibioticmech-review-queue.tsv`, and `.git` resolved the generated record and raw ChEBI row. Exact xrefs `cas:35272-27-6`, `reaxys:975928`, and InChIKey `COAIOOWBEPAOFY-UHFFFAOYSA-N` were found only on the raw ChEBI row and target YAML in the searched non-git trees. No prior exact review report for `CHEBI:141405` or its full label was present in the searched reports tree. |
| OLS4 lookup for `CHEBI:141405` | Passed. Current OLS/ChEBI returned `obo_id` `CHEBI:141405`, the matching label and definition, formula, charge, masses, SMILES, Standard InChI, exact InChIKey `COAIOOWBEPAOFY-UHFFFAOYSA-N`, the two generated xrefs, and the two PubMed xrefs from the committed ChEBI row. |
| OLS4 parent lookup for `CHEBI:141405` | Passed. Current OLS direct parents are the two generated `parent_compounds`: `CHEBI:33859` / aromatic carboxylic acid and `CHEBI:48864` / benzothiadiazole. |
| OLS4 role lookup for `CHEBI:141405` | Passed with one intentional local omission. Current OLS direct `has_role` edges are `CHEBI:24127` / fungicide, `CHEBI:86328` / antifungal agrochemical, and `CHEBI:73182` / plant activator. The generated record preserves the two antimicrobial roles that map to `ANTIFUNGAL` in `conf/sources.yaml`; `plant activator` is outside AntibioticMech's in-scope antimicrobial role map. |
| PubMed `efetch` for the two ChEBI literature xrefs | Passed. `PMID:11455656` and `PMID:21726155` both resolved to PubMed records. |
| PubMed exact-name search | Passed as a bounded discovery check. Searching `acibenzolar acid`, `CGA 210 007`, `1,2,3-benzothiadiazole-7-carboxylic acid`, and `benzo[1,2,3]thiadiazole-7-carboxylic acid` returned 13 hits. |
| PubMed activity/mechanism search | Passed as a bounded discovery check. Re-querying PubMed with the exact names that matched plus fungicide, antifungal, fungal, MIC, minimum-inhibitory, *Pseudomonas*, bacterial, and systemic-acquired-resistance terms returned 4 hits; a parallel target/mechanism query returned 2 hits. No inspected abstract reported a microbial MIC or a wet direct microbial molecular target for the exact acid. |
| PubMed CAS/InChIKey search | Passed as a negative bounded check. NCBI reported 0 hits for `35272-27-6` or `COAIOOWBEPAOFY`. |
| Repository publication search helper | Partial pass. The PubMed provider wrote 20 candidates to `/tmp/benzothiadiazole-publications.jsonl`; the anonymous Semantic Scholar provider returned HTTP 429. The PubMed exact-name `efetch` above was used for claim-level review instead of the helper's broad normalized output. |
| CAS Common Chemistry lookup for `35272-27-6` | Not independently resolved. The public detail page returned an Angular shell with `Get detail failed`. |
| Reaxys `975928` | Not checked directly: no public Reaxys resolver was available in this workflow. |

No narrower term, reference, or history validator is exposed in `justfile` for a
single generated ChEBI record. `just validate-strict` and `just verify-corpus
--summary` are the narrowest documented structural and generated-provenance
checks for this read-only review.

## Identity and Grounding

The record denotes the ChEBI structure `CHEBI:141405` exactly. The generated
label, definition, SMILES, Standard InChI, Standard InChIKey, formula, charge,
average mass, monoisotopic mass, xrefs, parents, source roles, and two source
PubMed IDs match row 2639 of `data/raw/chebi_antimicrobials.tsv`. Current OLS
agrees with the same identity, parents, structure, and schema-supported xrefs.

The two adjacent benzothiadiazoles found in the hidden-inclusive search are
distinct ChEBI records with distinct structures: `CHEBI:73178` is
acibenzolar-S-methyl, the S-methyl thioester with InChIKey
`UELITFHSCLAHKR-UHFFFAOYSA-N`, and `CHEBI:73185` is acibenzolar, the
carbothioic acid with InChIKey `CGIHPACLZJDCBQ-UHFFFAOYSA-N`. The reviewed
record is the carboxylic-acid metabolite with InChIKey
`COAIOOWBEPAOFY-UHFFFAOYSA-N`.

`CHEBI:24127` resolves to `fungicide`, and `CHEBI:86328` resolves to
`antifungal agrochemical`; both are mapped to `ANTIFUNGAL` in
`conf/sources.yaml`, so the filesystem category is consistent with the
generated source roles. Current OLS also lists `CHEBI:73182` / plant activator
as a role, and the exact PubMed leads are more consistent with plant-defense
activation than direct fungal toxicity, but that role is not an antimicrobial
role in this repository's mapping.

## Evidence

The record has no curator-owned evidence objects. That is acceptable for
ChEBI-seeded identity and class metadata, because the source concept supplies
database provenance, but it leaves the host-mediated mechanism, any
organism-level activity, and the absence of direct microbial inhibition
unreviewed.

| Reference | Review |
|---|---|
| `PMID:11455656` | Exact source lead for the acid as `CGA 210 007`, but not evidence of direct antimicrobial activity. The public abstract reports that acibenzolar-S-methyl and its acid derivative were quantified in tomato leaves, that tomato treatment with either compound at 250 microM protected plants against *Pseudomonas syringae* pv. tomato, and that neither compound inhibited bacterial growth in vitro; the authors interpret protection as activation of plant defense mechanisms. |
| `PMID:21726155` | Exact source lead for soil residue analysis only. The public abstract describes HPLC-DAD measurement of acibenzolar-S-methyl and its major conversion product, benzo[1,2,3]thiadiazole-7-carboxylic acid / `CGA 210 007`, in soil, then reports extraction, detection, quantification, recovery, and half-life metrics. |
| `PMID:33836466` | Exact mechanism near miss for a host-plant target. The public abstract reports reversible inhibition of purified recombinant *Arabidopsis thaliana* shikimate hydroxycinnamoyltransferase by acibenzolar acid, but HST is a plant enzyme and not a microbial target. |
| `PMID:22142181` | Plant-activator scaffold lead. The public abstract reports synthesis and systemic-acquired-resistance testing for benzo-1,2,3-thiadiazole-7-carboxylate derivatives and is a lead for plant-defense chemistry rather than for a microbial target of the exact acid. |
| Other exact PubMed hits | `PMID:42523179`, `PMID:37564187`, `PMID:33680135`, `PMID:32905931`, `PMID:25781308`, `PMID:42111998`, `PMID:17090124`, and `PMID:16794326` were toxicology, regulatory-residue, analytical, derivative-synthesis, or plant-signaling leads. Their public abstracts did not report direct antifungal MICs or direct microbial target evidence for `CHEBI:141405`. |

## Completeness

`mode_of_action`, `mode_of_action_target_scope`, `molecular_targets`,
`causal_graphs`, and `activity_spectrum` are consequentially absent. Unlike a
conventional antifungal pesticide that inhibits a fungal enzyme or process, the
inspected exact leads for this record point to plant defense activation by the
acid metabolite of acibenzolar-S-methyl. The tomato source lead explicitly says
direct bacterial growth was not inhibited in vitro, and no inspected public
abstract reported a direct antifungal MIC.

Empty `producer_organisms`, `resistance_mechanisms`,
`clinical_status_assertions`, `datasets`, and `discussions` are not immediate
validation defects for this ChEBI-only agrochemical metabolite. The bounded
exact searches over PubMed, local raw data, curated records, and prior reports
did not find a CARD/ARO resistance slice, public dataset, clinical/regulatory
assertion, or exact microbial biosynthesis claim for `CHEBI:141405`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record remains an uncurated plant-defense antimicrobial stub with no explicit host-mediated mechanism or activity observations. | The YAML has no `mode_of_action`, `activity_spectrum`, `molecular_targets`, or `causal_graphs`. OLS now also calls the acid a `plant activator`; `PMID:11455656` reports plant protection from *Pseudomonas syringae* pv. tomato but explicitly says neither acibenzolar-S-methyl nor `CGA 210 007` inhibited bacterial growth in vitro. No inspected exact-name PubMed hit reported a direct antifungal MIC or direct microbial target for the exact acid. | Curator-owned additions in `data/antibiotics/antifungal/1-2-3-benzothiadiazole-7-carboxylic-acid.yaml`, written only through `record_curation_event` plus `write_validated_antibiotic`. |
| Minor | The ChEBI definition likely contains an upstream wording error that calls the acid an active `herbicide` rather than a plant activator or fungicide metabolite. | The generated definition exactly mirrors current OLS/ChEBI: "The active herbicide of the proherbicide acibenzolar-S-methyl." ChEBI's roles on the same term are `fungicide`, `antifungal agrochemical`, and live `plant activator`; `PMID:11455656`, `PMID:21726155`, and `PMID:33836466` describe a plant activator/metabolite context, not herbicidal activity. The typo does not change the exact chemical identity. | ChEBI-owned `definition` imported through `data/raw/chebi_antimicrobials.tsv`; fix upstream or through a reproducible definition override rather than by hand-editing the generated record. |

## Recommended Edits

1. Review full text for the exact acid literature before adding any
   `ActivityObservation`. The most promising activity lead is `PMID:11455656`,
   but its public abstract supports plant-mediated protection from
   *Pseudomonas syringae* pv. tomato and direct in vitro inactivity, not a
   microbial MIC.

2. If full text confirms that the antimicrobial effect is solely plant-mediated,
   use a `Discussion` to record that curation gap unless there is a
   schema-supported way to model a crop-host defense node. Do not force the
   effect into `mode_of_action`, `mode_of_action_target_scope`, or
   `molecular_targets` unless primary evidence supports a direct microbial
   target or a future schema pattern explicitly represents plant-mediated
   protection.

3. Re-check the live ChEBI `CHEBI:73182` / plant activator role after the next
   ChEBI extraction. It is correctly absent from the current local
   antimicrobial `activity_roles`, but the future source row should continue to
   retain only roles that AntibioticMech maps as antimicrobial.

4. Check ChEBI's `active herbicide` wording upstream. If ChEBI corrects the
   text, a normal extractor refresh and seed will fix the generated definition;
   if it does not, a reproducible definition override would be needed before a
   local correction could survive `just verify-corpus`.

## Follow-up Checks

| After | Check |
|---|---|
| Any activity or host-mediated mechanism curation | `just validate-strict data/antibiotics/antifungal/1-2-3-benzothiadiazole-7-carboxylic-acid.yaml --out /tmp/benzothiadiazole-141405-validate-strict.tsv` |
| Any source-owned definition or role-filter change | `just seed`, then `just seed-canary CHEBI:141405`, then `just verify-corpus --summary` |
| Any curated YAML mutation | Re-read `data/antibiotics/antifungal/1-2-3-benzothiadiazole-7-carboxylic-acid.yaml` and confirm every `ActivityObservation`, `MolecularTarget`, and `CausalEdge` carries claim-level evidence on the object rather than record-level evidence. |
| Any direct CAS/Reaxys xref review | Re-fetch official OLS/ChEBI and compare the accession against the exact InChIKey `COAIOOWBEPAOFY-UHFFFAOYSA-N`; the public CAS Common Chemistry and Reaxys checks in this review did not expose independent resolvable records. |

## Additional Notes

- Current `review-readiness` row 160 shows the two source literature leads
  (`PMID:11455656` and `PMID:21726155`) and correctly classifies the next gate
  as `MECHANISM_REVIEW: mechanism is absent`.
- Current OLS lists `CHEBI:73182` / plant activator in addition to the two
  generated role terms. A hidden-inclusive `rg --no-ignore --hidden` search for
  `CHEBI:73182|plant activator` over `data/raw`, `conf/sources.yaml`,
  `curation/decisions.tsv`, and the target YAML found no local mapping for that
  role; it appeared only in definitions of the sibling `CHEBI:73178`
  acibenzolar-S-methyl and `CHEBI:73185` acibenzolar rows.
- `cas:35272-27-6` and `reaxys:975928` are consistent with current ChEBI as
  inherited database cross-references, but neither was directly checkable in a
  public structure resolver during this review.
