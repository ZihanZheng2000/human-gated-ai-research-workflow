# Four-Stage Workflow Smoke Test

This example tests whether the repository's current workflow can run as:

```text
Planning -> Modeling -> Reporting -> Reviewing
```

Gate mode: synthetic gates, auto-approved for framework testing.

Research task: scan the repository's active Markdown workflow files and check
whether they reflect the four-stage structure, reviewer-agent maker-checker
rules, and removal of Demo Gate as an independent gate.

Main outputs:

- `packages/planning-package.md`
- `packages/modeling-package.md`
- `packages/reporting-package.md`
- `packages/reviewing-package.md`
- `deliverables/workflow-smoke-test-report.md`
- `artifacts/20260627_four_stage_flow/tables/workflow_term_scan.csv`
- `artifacts/20260627_four_stage_flow/data/workflow_term_scan_summary.json`
- `artifacts/20260627_four_stage_flow/figures/workflow_term_scan.svg`

