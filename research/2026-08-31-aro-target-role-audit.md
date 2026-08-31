# ARO target-role audit

Date: 2026-08-31
Issue: #93

## Finding

The 252 `targeted_by_antibiotic` inventory edges refer to 54 distinct ARO target
terms and affect 206 corpus records. Three edges collapse during structure
harmonization, so before this audit they became 249 untyped `MolecularTarget`
items. The relationship name alone was treated as though it
meant direct molecular binding, even where the ARO definition described a
resistance mutation, prodrug activation, an attacked membrane/cell-wall
component, or a downstream process.

## Resolution

`conf/aro_target_roles.tsv` is an exhaustive reviewed map: the seeder fails if
an inventory target is unmapped or a stale mapping remains. Each emitted target
now requires:

- an explicit target relation and target type;
- assertion-level experimental context and optional organism/strain;
- source/version/retrieval ownership;
- an evidence status distinguishing primary evidence from a database-only
  assertion.

Database-only direct-binding assertions are retained as honest ARO provenance
but marked `PRIMARY_EVIDENCE_NEEDED` and surfaced by `just worklist --queue
target-evidence`. Other database relations remain `DATABASE_ASSERTION_ONLY`;
they do not acquire a direct-binding claim merely because ARO uses a target
edge.

## Daptomycin correction

The four ARO items on daptomycin are now represented as:

| ARO term | Relation | Reason |
|---|---|---|
| ARO:3003275 cardiolipin synthetase | `SUSCEPTIBILITY_DETERMINANT` | ARO describes resistance-conferring `cls` mutations |
| ARO:3003278 rpoB | `DOWNSTREAM_AFFECTED_PROCESS` | The definition describes RNA-synthesis failure after membrane depolarization, not rpoB binding |
| ARO:3003280 mprF | `SUSCEPTIBILITY_DETERMINANT` | Membrane-charge remodeling and resistance mutations alter susceptibility |
| ARO:3003281 pgsA | `SUSCEPTIBILITY_DETERMINANT` | Phospholipid biosynthesis changes membrane state; direct binding is not established |

A separate curator assertion records the phosphatidylglycerol-rich bacterial
membrane as the direct target with primary evidence from PMID:40455071. That
2025 study reports calcium-dependent stable daptomycin-phosphatidylglycerol
complex formation and selective bacterial-membrane uptake. It does not turn the
four ARO susceptibility/context terms into direct targets.

## Guardrails

- A direct target with only ARO evidence is queued, never presented as
  primary-literature confirmed.
- An organism-specific protein remains a `ProteinExample`, not the target ID.
- A resistance-labeled ARO target cannot carry `DIRECT_BINDING_TARGET`.
- Curator-authored target assertions remain outside the CARD-owned slice and
  survive re-seeding.
