# Workflow Revision Note: Exploratory Demo Before Full-Scale Runs

Date: 2026-06-18

Status: accepted and promoted to framework docs/templates

Promoted on: 2026-06-18

Promoted into:

- `AGENTS.md`
- `docs/stage-handoffs.md`
- `docs/model-stage.md`
- `templates/model-package.md`
- `templates/smoke-test-package.md`
- `docs/example-organization.md`
- `docs/quickstart.md`

## Context

During the Reservoir Knowledge Base case study, the first modeling attempt revealed another workflow issue: the first pass should not immediately behave like a full-scale production run.

At the beginning of a new project, the research workflow, source structure, extraction schema, validation logic, and review criteria are often still uncertain. Setting a rigid goal too early or running the full source/data set too soon can create unnecessary churn.

## Proposed Revision

Add an explicit exploratory demo phase before full-scale execution.

Recommended flow:

```text
Planning -> Exploratory Demo -> Review Demo -> Scale-Up Execution -> Reporting / Packaging -> Reviewing -> Writing
```

Or, if keeping the higher-level stage names:

```text
Planning -> Modeling / Execution
  -> small demo run
  -> review and revise workflow
  -> versioned scale-up run
Reporting / Packaging -> Reviewing -> Writing
```

## Key Principle

Do not start with full scale.

The first pass should:

- move slowly and deliberately
- use a small sample
- run through all workflow layers end to end
- expose missing schema fields, bad assumptions, and unclear stage boundaries
- produce a small but complete demo
- support human discussion before scaling

Only after the small demo works should the workflow switch to broader or full-scale execution.

## Goal Setting

Avoid setting a rigid production goal too early.

Early-stage goals should be exploratory:

- understand the source landscape
- test the layer boundaries
- test extraction schema
- test validation logic
- test whether outputs are human-reviewable
- identify what needs to change before scale-up

Production goals should be set after the small demo has been reviewed.

## Recommended Demo Pattern

For a new project, run a small complete demo:

```text
3-5 sources or a small representative sample
-> source acquisition
-> text extraction
-> KU extraction
-> synthesis
-> automated validation
-> short review package
-> human discussion
```

Then revise:

- source tiers
- schema fields
- extraction rules
- synthesis categories
- validation checks
- report structure
- run logging

Only then scale up:

```text
broader source set / full dataset
-> versioned run
-> reproducible logs
-> reporting package
```

## Versioning And Logs

Each iteration should have explicit versioning and logs.

Recommended run directory pattern:

```text
artifacts/<case_or_project>/runs/<YYYYMMDD>_<run_name>/
```

or:

```text
artifacts/<case_or_project>_<run_type>_<YYYYMMDD>/
```

Each run should include:

- `run_manifest.json`: what the run intended to do
- `run_log.md`: what happened, decisions, deviations, failures, fixes
- `source_manifest.json`: planned sources or data inputs
- `source_inventory.jsonl`: acquired and preserved sources
- `validation/*.json`: automated validation outputs
- `run_summary.md`: concise human-readable result summary
- links to KU, synthesis, report, and appendix artifacts

## Run Log Content

The run log should record:

- run ID and date
- stage or layer being tested
- source/sample scope
- tools/scripts used
- important decisions
- deviations from plan
- failed downloads or extraction problems
- schema changes
- validation results
- known limitations
- next iteration recommendations

## Rationale

Small demos reveal workflow problems early. In the Reservoir KB case study, the small run helped identify:

- the need to separate KU extraction from synthesis
- the need for a Layer 1 source-acquisition skill
- the need to split source discrepancy from operational tradeoff
- the need to remove artificial KU count limits
- the need to separate Reporting/Packaging from formal Writing
- the need for better versioning and run logs

These changes would have been harder to see cleanly in a full-scale run.

## Promotion Summary

This proposal has now been incorporated into the main framework.

Implemented decisions:

- Modeling should usually start with a small exploratory demo when the workflow, data source, extraction method, or validation approach is uncertain.
- A Demo Gate can pause the workflow before scale-up.
- Substantial runs should record `run_manifest.json`, `run_log.md`, and `run_summary.md`.
- Run-specific agent artifacts can be stored under `artifacts/<run_id>/agent/`.
- The workflow should not treat a first successful script, table, figure, or extraction as sufficient by itself.

Remaining note:

- The exact run-directory naming convention is still flexible. The framework currently standardizes required run files and allows projects to choose the surrounding folder layout.
