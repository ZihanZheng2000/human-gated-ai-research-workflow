# Planning Package

## Planning Workflow Identity

- package status: approved
- Planning Researcher: Codex runtime
- Planning Reviewer: simulated reviewer agent
- reviewer file: `docs/reviewer-agents/planning-reviewer-agent.md`
- reviewer mode: critique-only
- Planning Review status: completed
- researcher-agent response status: completed
- user Planning Gate status: synthetic approved

## User-Need Profile

- research area: workflow QA for AI-native academic research process
- intended output: framework smoke-test report
- workflow mode: compact smoke test
- idea maturity: revision or implementation task
- planning depth: skip/defer external literature; use local workflow docs as data
- intended research product: workflow demo
- practical success criterion: complete Planning -> Modeling -> Reporting -> Reviewing with reviewer passes and synthetic gates
- target audience or venue: repository maintainer
- gate mode: synthetic gates

## Planning Depth Decision

| Item | Decision | Reason | Downstream implication |
|---|---|---|---|
| idea maturity | revision | user requested workflow test | use existing repository docs |
| literature/prior-work scan depth | skipped | framework mechanics test, no external claims | no novelty claim |
| novelty assessment depth | skipped | not a research contribution | report only operational findings |
| venue/output calibration depth | skipped | internal smoke test | use Reporting report mode |
| revisit trigger | before publication | if converted into a formal paper | add literature/venue work |

## Approved Research Question

Can the current repository workflow run end to end as four stages with reviewer-agent critique, researcher-agent response, synthetic gates, and Modeling demo as an internal phase rather than a separate gate?

## Data Plan

- primary data source: repository Markdown files under `AGENTS.md`, `README.md`, `docs/`, `templates/`, and `skills/`
- exact raw data host: local repository
- acquisition success rule: scan at least 25 active Markdown files and produce summary JSON, CSV table, and SVG figure
- key variables: term counts for four-stage terms, reviewer-agent terms, researcher-agent terms, stage gates, Demo Gate, Writing-stage references
- access or licensing concerns: local repository files only

## Method Blueprint

1. Scan active Markdown files, excluding notes.
2. Count workflow-control terms with deterministic regex patterns.
3. Generate CSV, JSON, and SVG artifacts.
4. Interpret residual Demo Gate and Writing-stage hits.
5. Produce stage packages and a final review package.

## Planning Reviewer Critique

| Finding ID | Reviewer concern | Severity | Evidence or reasoning | Route |
|---|---|---|---|---|
| PR-1 | External literature is skipped. | accepted limitation | This is a framework mechanics test, not a scientific literature claim. | Planning |
| PR-2 | Regex scan may miss semantic inconsistencies. | minor | Term counts are necessary but not sufficient for full workflow validation. | Reporting |

## Researcher-Agent Response to Planning Review

| Finding ID | Response status | Change made or planned | Blocks Planning Gate? | Notes |
|---|---|---|---|---|
| PR-1 | accepted but deferred | Label output as internal smoke test only. | no | No novelty claim will be made. |
| PR-2 | accepted and fixed | Add qualitative review notes in Reporting and Reviewing. | no | Regex results are treated as evidence, not full proof. |

## Planning Gate Decision

- decision: approve for Modeling
- gate mode: synthetic gate
- decision maker: user-authorized auto gate
- required changes before Modeling: none
- accepted limitations: local-doc QA only

