# Quick Start

This repository is a workflow kit for AI-assisted academic research. It is not a fully autonomous research agent and not a Python package.

## Choose a Mode

### Full Workflow Mode

Use this for a real research project.

1. Generate a Planning Researcher draft from `templates/plan-package.md` with the researcher agent.
2. Run Planning Reviewer critique with a separate reviewer agent when available and approved.
3. Have the researcher agent respond to reviewer findings, revise or route issues, and then ask for the user Planning Gate.
4. Run Modeling using `templates/model-package.md`.
5. Run Reporting using `templates/reporting-package.md`.
6. Run Reviewing using `templates/review-package.md`.
7. Finalize, release, archive, or backtrack according to the Reviewing Gate decision.
8. Move forward only after the relevant gate is approved.

### Smoke-Test Mode

Use this to test the framework on a small public-data task.

1. Start from `templates/smoke-test-package.md`.
2. Select a small question and public dataset.
3. Use synthetic gates and label them as synthetic.
4. Download or read real usable data.
5. Run a minimal executable analysis.
6. Generate at least one table and one figure.
7. Produce one compact Reporting Package and one route-aware Review Package.
8. Record framework issues discovered by the run.

## Minimum Standards

For any mode:

- Candidate links do not count as data.
- Each stage gate should happen after reviewer-agent critique and researcher-agent response, or after an explicit skipped-review rationale is recorded.
- Data count only when usable under the acquisition success rule.
- Raw data host, official source, documentation source, version/access date, and license/access status should be recorded.
- Environment failures should trigger an environment repair decision.
- Claims should be tied to citations, artifacts, model outputs, or explicit limitations.
- New or uncertain workflows should usually start with a small Modeling demo before full-scale execution.
- Substantial runs should record `run_manifest.json`, `run_log.md`, and `run_summary.md`.
- Citation strictness should match the output type.

## Suggested First Test

Run a smoke test with a small public CSV dataset and organize it according to `docs/example-organization.md`.

## Suggested Prompt for a New Codex Session

```text
Please run a complete smoke test of this repository's workflow.

Use `templates/smoke-test-package.md`.
Do not ask me for a research idea; choose a small public-data question yourself.
Run Planning -> Modeling -> Reporting -> Reviewing.
Download or read real usable data locally.
Generate a script, cleaned data, at least one table, and at least one figure.
If the environment fails, record an Environment Repair Decision and continue.
During Modeling, create a concrete Modeling Goal and usually begin with a small exploratory demo phase before scale-up. Do not stop after the first successful script, table, or figure; continue until the Model Package is ready for the Modeling Gate, or until a route decision is required.
Use synthetic gates and label them as synthetic.
Write the final summary in Chinese.
```
