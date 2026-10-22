---
name: stats-report
description: "Generate reproducible corpus, source, grounding, and data-quality statistics from the current AntibioticMech corpus."
category: reporting
requires_database: false
requires_internet: false
version: 1.0.0
tags: [reporting, statistics, metrics, corpus]
---

# Statistics report

Use this skill for current AntibioticMech repository counts, README statistics,
publication summaries, or before/after measurements for an import or curation
batch.

## Commands

```bash
just report
just docs-stats
just docs-check
```

Run `just report` (`uv run python scripts/antibiotic_report.py`) and `just docs-stats` (`uv run python scripts/check_docs.py`) to generate reproducible corpus, class, grounding, and review-status statistics.

Never copy a hardcoded record count from skill prose: always derive counts at
run time because the corpus changes continuously.

## Verification

- Record the exact command and git commit used for published figures.
- Do not hand-edit generated statistics tables or JSON/Markdown reports and present them as a fresh run.
- Run `just validate-strict` alongside reporting commands when summarizing corpus health.
