# Merging pull requests in AntibioticMech

When `main` requires GitHub's native merge queue, use the queue after review
and required PR checks pass. This applies to documentation changes too.

1. Open a PR against `main` and complete its review.
2. Wait for the required checks listed below.
3. Use the PR's merge control to enter the queue. From the CLI, run
   `gh pr merge <number> --repo CultureBotAI/AntibioticMech` after those checks pass.
4. Follow the new `merge_group` workflow runs. They validate the combined
   commit containing current `main`, this PR, and any earlier queued changes.
5. Let GitHub merge after the queue checks pass. If the PR is removed from
   the queue, inspect the failed queue run, fix the cause, and enter again.

## Required checks

- `qc (3.10)` from `.github/workflows/main.yaml`.
- `qc (3.12)` from `.github/workflows/main.yaml`.
- `vendored-sync` from `.github/workflows/vendored-sync.yaml`.

The queue runs the same validation commands as a PR. A passing PR run does
not replace validation of the combined queue commit. New commits can cancel
older PR runs; separate queue runs retain their own verdicts.

The repository's branch rules select the queue merge method. Do not use
`gh pr merge --admin` for routine merges, because it bypasses the queue.
See the [GitHub CLI merge reference](https://cli.github.com/manual/gh_pr_merge)
and [GitHub merge queue documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue).
