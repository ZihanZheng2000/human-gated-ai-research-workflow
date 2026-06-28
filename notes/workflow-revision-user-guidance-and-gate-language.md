# Workflow Revision Note: User Guidance And Gate Language

Date: 2026-06-18

Status: proposal only; framework files not yet modified

## Context

During the Reservoir Knowledge Base case study, the user noticed that Codex should provide more guiding language during the workflow.

The framework already has gates, stage packages, and stage handoffs, but the user experience can still feel unclear if Codex does not explicitly say:

- what stage the work is in
- what has just been completed
- what is waiting for approval
- what the next step would be
- what choices the user has

## Proposed Revision

Add explicit user-facing guidance language to each stage and gate.

Codex should regularly orient the user with short, concrete guidance:

```text
We are at the Planning Gate.
The plan is ready for review.
You can approve it, ask for edits, or pause.
If approved, the next step is a small exploratory demo, not full-scale execution.
```

## Why This Matters

Human-gated workflows require the human to understand where they are in the process. If the agent only produces artifacts, the user may not know:

- whether something is done
- whether they need to approve
- whether they are allowed to revise
- whether the next step is exploratory or full-scale
- whether the workflow is moving too fast

Guidance language turns gates from hidden control logic into explicit collaboration.

## Recommended Guidance Pattern

At the end of any substantial stage or substage, Codex should include:

1. Current stage
2. What was completed
3. What the artifact is
4. What decision is needed
5. What happens if the user approves
6. What alternatives the user can choose

Example:

```text
Current stage: Modeling / Exploratory Demo

Completed:
- acquired 5 official sources
- extracted text
- generated 40 KUs
- produced 8 synthesis cards

Decision needed:
Do you approve this demo structure?

If approved:
We will scale up to a broader tiered source set.

Other options:
- revise source tiers
- change KU dimensions
- modify synthesis categories
- pause and review artifacts manually
```

## Gate Prompt Examples

### Planning Gate

```text
Planning package is ready.
Please review whether the research objective, prior-work scan, feasibility scope, and demo route are acceptable.

Approve to enter Modeling / Exploratory Demo.
Request edits if the framing, novelty, source scope, or output target should change.
```

### Demo Gate

```text
The small demo has run end to end.
Please decide whether the workflow structure is acceptable before scaling up.

Approve to run a broader version.
Request edits if source acquisition, KU extraction, synthesis categories, or validation should change.
```

### Modeling Gate

```text
The modeling/execution package is ready.
Please review whether the results are sufficient for Reporting / Packaging.

Approve to package the results for human review.
Request a Modeling addendum if more data, validation, or analysis is needed.
```

### Reporting / Packaging Gate

```text
The review package is ready.
Please review whether the short report, technical appendix, artifact index, and limitations are clear enough for review.

Approve to enter Reviewing.
Request edits if the package is confusing, incomplete, or overclaims.
```

### Reviewing Gate

```text
Review is complete.
Please decide whether the findings are ready for Writing, need another execution cycle, or should be scoped down.
```

## Tone Guidance

Guidance language should be direct and lightweight, not bureaucratic.

Good:

```text
This is a gate moment. If you approve, I will move to the broader demo. If not, we can revise the source tiers first.
```

Avoid:

```text
Per protocol, the user must now render a gate decision.
```

## Implications For Framework Revision

When updating the framework, consider adding:

- gate prompt examples to each stage document
- a required `Decision Needed` section in every stage package
- a `Next If Approved` section in every package template
- guidance language examples in `AGENTS.md`
- stronger reminders to not silently continue through gates

## Current Decision

Do not modify the main framework yet.

This note records the proposed guidance-language improvement so it can be reviewed before editing `AGENTS.md`, stage docs, templates, or skills.
