# NEXT_TASKS

Backlog for AntibioticMech, newest thinking first. Written 2026-08-29, at the
end of the scaffolding pass that produced the initial 2,603-record corpus.

## Now

- **Curate the first mechanism graphs.** 0 of 2,603 records carry a
  `causal_graph`; that number is the point of the repository. Start with the 324
  records that already have CARD target or resistance evidence to build on —
  `just worklist --queue mechanism` ranks them by how much evidence is waiting.
- **Seed `mode_of_action` from CARD drug classes where it is safe.** Several ARO
  drug classes state the mechanism in their definition text (macrolides bind the
  50S subunit; fluoroquinolones inhibit topoisomerase II). Extracting that per
  class, with the ARO definition as the citation, would move ~1,100 records off
  `UNKNOWN` — but only where the class definition really is a mechanism claim and
  not a structural description. Needs a per-class review, not a regex.
- **Ground the 250 minted records.** `just worklist --queue minted`. Most are
  CARD molecules with a PubChem structure and no ChEBI entry; some deserve a
  ChEBI term request.
- **Re-file the compounds no source classifies well.** After #2 and #3, a
  handful remain filed by ChEBI's generic `antibacterial agent` role against
  clinical reality — ketoconazole is the clearest: ChEBI asserts antibacterial,
  and CARD's "imidazole antibiotic" class deliberately does not state a target
  group. These need a curation decision each, not another inference rule.
- **Resolve the two structure-collision todos.** gramicidin S / gramicidin C and
  patricin A / patricin B share an InChIKey via CARD's PubChem cross-references.
  One CID in each pair is wrong upstream; determine which and file it with CARD.

## Next

- **Find a resistance source for the antiviral records.** CARD covers bacterial
  and (increasingly) fungal resistance; it has nothing for viruses, so all 474
  antiviral records carry an empty `resistance_mechanisms` while 279 antibacterial
  records carry CARD determinants. The obvious candidates are the Stanford HIV
  Drug Resistance Database for HIV, and the literature for HBV/HSV/influenza —
  each would need the same treatment CARD got: a committed inventory, an explicit
  citation on every item, and a mechanism vocabulary that says what it means.
  Until then the asymmetry should be visible in the report rather than read as
  "antivirals have no known resistance".

- **Decide what the 364 structureless concepts are.** `just worklist
  --queue no-structure`. Each is a mixture, a class, a preparation, or a
  compound whose structure simply is not in ChEBI or PubChem. They need
  `EXCLUDE` decisions with rationale, or a structure.
- **Use ChEBI's citation lists.** The extractor already commits a `citations`
  column (PubMed IDs from ChEBI's own entry references) that nothing reads. It is
  a real starting set for a curator writing record-level evidence — but a
  reference cited by a ChEBI entry supports the compound, not necessarily any
  antimicrobial claim about it, so it cannot be seeded blind.
- **Producer organisms and BGCs.** `producer_organisms` is empty. MIBiG is the
  obvious source for natural products and would connect this corpus to
  biosynthesis; it needs a compound→BGC mapping that MIBiG's JSON supports.
- **Activity spectrum.** `activity_spectrum` is empty. Real MIC data would come
  from a screening resource with assays attached; without the assay a number is
  not an observation, so pick the source carefully.
- **A `research/` path.** Sibling repos run model-assisted deep research per
  entity with a manifest of what was actually paid for. The `research` extra in
  `pyproject.toml` is declared and unused; wire it up when there is a question
  worth asking per compound.

## Later

- **Link `resistance_mechanisms` to CARD's real mechanism categories.** The
  determinant→mechanism association lives in `card.json`, not `aro.obo`, so most
  seeded items are `UNKNOWN`. Adding card.json as a third source would fix that.
- **Retired-URL redirects.** The slugs of dropped records are now reserved in
  `data/antibiotics/RETIRED.tsv`, so no URL is ever reissued to a different
  compound — but 134 record pages disappeared without a redirect when unreviewed
  ChEBI relations stopped being trusted, and nothing serves those addresses.
  HabitatMech rebuilds a redirect map from git history; this repository now has
  the history to do the same.
- **Cross-repo links.** A compound record should point at the TraitMech traits it
  perturbs and the MediaIngredientMech ingredients it shares structures with.
