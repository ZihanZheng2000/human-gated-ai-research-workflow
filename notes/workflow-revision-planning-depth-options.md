# Workflow Revision Note: Planning Depth Options For Idea And Literature Work

Date: 2026-06-18

Status: proposal only; framework files not yet modified

## Context

The Plan stage already requires purpose clarification, prior-work scan, novelty consideration, feasibility checks, and venue/output calibration. However, real users may not always need the same depth.

In the Reservoir Knowledge Base case study, the user already had a familiar and well-formed idea. A full idea-generation and literature-review process would have slowed down the useful exploratory demo. In other projects, especially vague or early ideas, the literature and novelty work may be essential.

## Proposed Revision

Planning should offer selectable depth for idea generation, idea assessment, novelty positioning, and literature/prior-work review.

Codex should ask the user what level is appropriate before doing heavy planning work.

## Planning Depth Options

### Option A: Full Planning Scan

Use when the idea is new, vague, high-stakes, intended for publication, or the user wants help shaping the research direction.

Includes:

- idea refinement or candidate idea generation
- focused literature and prior-work scan
- novelty and gap assessment
- mature tool/skill scan
- venue/output calibration
- feasibility and cost checks
- candidate research routes

### Option B: Light Planning Scan

Use when the user already has a clear idea but wants basic calibration before execution.

Includes:

- concise research objective
- brief prior-work sanity check
- lightweight novelty/risk note
- feasibility check
- small demo scope
- explicit statement of what is deferred

### Option C: Skip Literature/Novelty For Demo

Use when the user explicitly wants to quickly test workflow mechanics or already understands the domain well.

Still record:

- user chose to skip or defer prior-work/novelty scan
- why skipping is acceptable for this run
- risks of skipping
- whether literature/novelty work must be done before publication, full-scale execution, or manuscript writing

Skipping should not be silent.

## Suggested User Prompt

At the start of Planning, Codex can ask:

```text
Before I write the plan, how much idea/literature calibration do you want?

1. Full scan: idea refinement, prior work, novelty, feasibility, and candidate routes.
2. Light scan: quick prior-work/novelty sanity check, then small demo.
3. Skip for now: you already know the idea; we record the risk and run a small demo.
```

## Gate Rule

If literature/novelty is skipped or light, the Plan Package should explicitly say:

```text
Prior-work scan: skipped / light / full
Novelty assessment: deferred / preliminary / completed
Reason: ...
Risk: ...
Required before: scale-up / reporting / review / writing / publication
```

## Why This Matters

This prevents two failure modes:

1. Over-planning when the user needs a fast exploratory demo.
2. Under-planning when the user is heading toward a publication-level claim.

The workflow should be human-gated and user-calibrated, not rigid.

## Current Decision

Do not modify the main framework yet.

This note records the proposed Planning depth option so it can be reviewed before editing `docs/plan-stage.md`, `templates/plan-package.md`, or `AGENTS.md`.
