# Reuse-permission outreach

Date drafted: 2026-08-31
Issue: #106
Status: **PARTIALLY SENT — three official GitHub requests open; one email request pending**

These requests deliberately identify the exact data scope and ask separately
about access, modification, commercial redistribution, attribution, and
third-party content. A reply should be archived verbatim with its date and
sender before any source is marked adopted.

## Request log

| Source | Sent on | Channel | Request | Response |
| --- | --- | --- | --- | --- |
| BV-BRC | 2026-08-31 | Official API GitHub tracker | [BV-BRC-API #204](https://github.com/BV-BRC/BV-BRC-API/issues/204) | Pending |
| Stanford HIVDB | 2026-08-31 | Official Sierra GitHub tracker | [hivdb/sierra #40](https://github.com/hivdb/sierra/issues/40) | Pending |
| BacDive | 2026-08-31 | Official BacDive API GitHub tracker | [LeibnizDSMZ/bacdive-api #1](https://github.com/LeibnizDSMZ/bacdive-api/issues/1) | Pending |
| CO-ADD | Not sent | `info@co-add.org` | Draft below | No authenticated mail channel in this workspace |

The three GitHub requests were posted by the authenticated repository maintainer
account and link back to AntibioticMech issue #106. Opening a public request does
not change a source's reuse determination: BV-BRC and HIVDB remain unverified,
and BacDive remains a candidate, until authorized maintainers answer the precise
data-content questions.

## BV-BRC — `help@bv-brc.org`

Sent through the official BV-BRC API issue tracker as
[BV-BRC-API #204](https://github.com/BV-BRC/BV-BRC-API/issues/204); response pending.

Subject: Reuse terms for laboratory-method BV-BRC AMR phenotype rows

We maintain AntibioticMech, a publicly redistributed CC BY 4.0 corpus of
chemical structures and evidence. We are evaluating only BV-BRC AMR phenotype
or `genome_amr` rows whose evidence is `Laboratory Method`; we will exclude all
computational predictions and classifier outputs.

Could you confirm whether those API/download rows may be (1) programmatically
downloaded, (2) filtered, normalized, joined to chemical and taxonomic
identifiers, and otherwise modified, and (3) redistributed in a corpus that
permits commercial reuse? Please state the applicable licence, required
attribution/citation, version or retrieval-date requirements, and whether any
fields or contributing sources have different terms. If a machine-readable
licence or terms URL exists, please provide it.

## BacDive — official BacDive API GitHub tracker

Sent through the official BacDive API issue tracker as
[LeibnizDSMZ/bacdive-api #1](https://github.com/LeibnizDSMZ/bacdive-api/issues/1);
response pending. The issue distinguishes the API client's MIT software licence
from the data-content terms that require confirmation.

Subject: Confirm CC BY 4.0 scope for BacDive susceptibility API/bulk rows

The current BacDive site footer links its Copyright & License statement to CC
BY 4.0. We are evaluating strain-level antibiotic susceptibility fields for a
CC BY 4.0 corpus.

Could you confirm that CC BY 4.0 covers susceptibility data returned through
the BacDive API and any bulk/download mechanism, including permission to
filter, normalize, join to external chemical/taxonomic identifiers, and
redistribute modified rows for commercial and non-commercial use? Please also
state the required attribution/citation, database version/retrieval-date
requirements, and any third-party fields excluded from that licence.

## CO-ADD — `info@co-add.org`

Not sent. CO-ADD exposes an email address but no official public issue tracker;
this workspace has no authenticated mail channel. The request remains ready for
a maintainer.

Subject: Request for a separately licensed CO-ADD antimicrobial screening distribution

We maintain AntibioticMech, a CC BY 4.0 corpus of chemical structures and
evidence. CO-ADD screening results in ChEMBL are useful but remain under
ChEMBL's CC BY-SA 3.0 terms, while the CO-ADD website copyright page prohibits
systematic download and redistribution without permission.

Does CO-ADD offer an independent machine-readable distribution containing
compound identity, organism/strain, assay, concentration or MIC, units, medium,
detection method, result, and citation? If so, may we programmatically obtain,
filter/normalize/modify, and commercially redistribute derived observation rows
under CC BY 4.0 or another non-restrictive licence? Please identify the exact
dataset scope, licence, attribution/citation, version/retrieval requirements,
and any depositor or third-party restrictions. We are not asking to relicense
the ChEMBL copy.

## Stanford HIVDB — `hivdbteam@lists.stanford.edu`

Sent through the official Sierra issue tracker as
[hivdb/sierra #40](https://github.com/hivdb/sierra/issues/40); response pending.

Subject: Reuse terms for Stanford HIVDB resistance data

We maintain AntibioticMech, a publicly redistributed CC BY 4.0 corpus. We are
evaluating HIVDB download/API data describing HIV drug-resistance mutations,
drug susceptibility/interpretation evidence, algorithm/database version, and
primary references. We would scope any use to HIV and preserve record-level
provenance.

Could you confirm whether these database rows may be programmatically
downloaded, filtered/normalized/modified, joined to drug and mutation
identifiers, and redistributed in a corpus permitting commercial reuse? Please
state the applicable data licence, exact covered endpoints/downloads, required
attribution/citation, version/retrieval-date requirements, and any third-party
fields with separate terms. We have found GPL terms for the public CMS code but
do not assume they license the resistance database itself.
