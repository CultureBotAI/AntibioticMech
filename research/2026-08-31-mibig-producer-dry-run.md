# MIBiG producer import dry run

Date: 2026-08-31  
Issue: #104  
Release: MIBiG 4.0.1, Zenodo record 14835872  
Archive SHA-256: `d02a387c7d62f8e54d7bcdc03984301e513ce56c1782ecbc9ce957a76039444f`

Command:

```text
uv run --extra chemical-map python scripts/extract_mibig_producers.py \
  --dry-run --archive /tmp/mibig_json_4.0.tar.gz
```

## Pre-write result

| Outcome | Count | Meaning |
|---|---:|---|
| matched | 3 | One exact Standard InChIKey and one corpus record |
| ambiguous | 17 | Connectivity-only match or an unassigned potential stereoelement; not written |
| rejected | 0 | No eligible compound lacked taxonomy, structure, parsable chemistry, or a reference |
| out of scope | 23 | No exact/connectivity match to the current corpus |

The source archive contained 3,013 entries. Twenty-four were both active and
carried a non-placeholder reviewer; those entries supplied 43 structurally valid
compound rows. The exact matches were:

- BGC0000432 streptothricin F → `CHEBI:60821`
- BGC0000432 streptothricin D → `CHEBI:60828`
- BGC0000455 vancomycin → `CHEBI:28001`

Balhimycin (`BGC0000311`) matched a corpus record by connectivity only, not by
the full Standard InChIKey, and was therefore not imported. MIBiG bioactivity
labels were not read into any AntibioticMech activity field.
