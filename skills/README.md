# Skills

This folder contains workflow-native skills for the AI-native research workflow.

These skills are not meant to replace mature external research tools. They are small reusable control modules that help the four stages stay inspectable, evidence-bound, and human-gated.

## Skill Strategy

Use the strategy in `../docs/skill-strategy.md`:

1. Reuse mature external tools for standardized research operations.
2. Use workflow-native skills to orchestrate, verify, package, and route outputs.
3. Create project-specific skills only when the needed operation is not already covered well enough.
4. Promote project-specific skills into this folder only after reuse and review.

Recommended external research skills are listed in `../docs/skill-strategy.md#recommended-external-research-skills`. Keep those tools outside this `skills/` folder unless this project later adds a thin adapter skill that exposes inputs, outputs, evidence logs, and failure modes.

## Current Workflow-Native Skills

| Skill | Main role |
|---|---|
| `venue-calibration/` | Calibrate a project to target venue, audience, official requirements, and exemplar patterns |
| `research-skill-card-distiller/` | Convert prior work into reusable research-skill cards or method patterns |
| `model-contract-runner/` | Run Model-stage work under explicit contracts, success rules, and bounded loops |
| `figure-table-narrative/` | Design empirical, conceptual, method, and appendix visuals around Reporting deliverables and evidence claims |
| `claim-evidence-mapper/` | Tie claims to citations, model artifacts, limitations, or approved user knowledge |
| `route-aware-reviewer/` | Review evidence packages or deliverables and route findings to Planning, Modeling, Reporting, Reviewing, or termination |
| `gate-manager/` | Record human gate decisions and manage stage advancement or backtracking |

## External Handoff Expectations

When a skill uses or recommends an external tool, the stage package should record:

- tool or source name
- version, access date, API endpoint, model, package version, or template version when relevant
- input query, prompt, file, dataset, or manuscript section
- output artifact path or citation
- verification status
- limitations or known failure modes
- whether the output is evidence, a suggestion, formatting support, or a convenience artifact

## Project-Specific Skills

Project-specific skills should usually live in the project or run artifacts while they are being tested, for example `artifacts/<run_id>/agent/` in a worked example. They can be promoted into `skills/` only when they are reusable across projects, documented, and clearly add workflow value beyond external tools.
