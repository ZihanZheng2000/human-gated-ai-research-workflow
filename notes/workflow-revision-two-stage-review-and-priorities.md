# Workflow Revision Note: Two-Stage Review And Priority Improvements

Date: 2026-06-18

Status: proposal only; framework files not yet modified

## Context

After the Reservoir Knowledge Base case study, several workflow improvements appeared valuable enough to consider for the main framework. The user approved the general direction of these improvements and proposed a stronger two-stage review process.

This note records the proposed review redesign and the priority changes to consider when revising the framework.

## Review Should Have Two Substages

The current Review stage should be split into two review modes:

```text
Review A: Internal Self Review
Review B: External Agent Review
```

The goal is to combine self-critique and independent critique without allowing multiple agents to modify the project at the same time.

## Review A: Internal Self Review

The internal review is performed by Codex itself in critic mode.

Codex should not continue producing new research outputs during this substage. It should inspect what it has already produced.

Internal review should check:

- artifact completeness
- package readability
- source/KU/synthesis consistency
- validation status and limitations
- unsupported or overstrong claims
- missing caveats
- stage-rule violations
- reproducibility issues
- file/path clarity
- whether the package is ready for external review

Codex may fix issues during Internal Self Review.

Expected outputs:

- internal issue list
- fixes made
- unresolved issues
- internal review log

## Review B: External Agent Review

The external review is performed by another agent, such as Claude Code, when available and requested by the user.

Default rule:

```text
External reviewer critiques only. It does not modify files.
```

The external reviewer should inspect the reporting package, technical appendix, artifact index, validation outputs, and selected artifacts. It should return a list of issues, risks, unsupported claims, reproducibility problems, and suggested improvements.

External review should check:

- whether the workflow output is understandable to a reviewer
- whether claims are supported by evidence
- whether limitations are explicit
- whether validation is sufficient for the claim level
- whether artifacts are findable and reproducible
- whether the method is coherent
- whether there are contradictions between report, appendix, and artifacts

External review should not edit by default because multi-agent editing can create conflicts.

## Response To External Review

After external review:

```text
External issue list -> Codex triage -> Codex fixes -> response-to-review log -> user gate
```

Codex should classify each external issue as:

- accepted and fixed
- accepted but deferred
- rejected with reason
- needs user decision

Only Codex should modify files unless the user explicitly asks another agent to edit.

## User Gate After Review

After review and response:

```text
Ready for Writing?
Need more Modeling / Execution?
Need more Reporting / Packaging?
Need another external review?
Terminate / archive?
```

The user makes the final gate decision.

## Writing Review Is Deferred

At this stage, do not include a dedicated writing review mode in the core review redesign. Writing review belongs later, after the workflow has a formal Writing stage and manuscript draft.

The current priority is evidence, artifact, method, and claim review.

## Priority Improvements To Framework

The following improvements are approved as useful proposal directions.

### 1. Planning Depth Options

Planning should ask how much idea/literature calibration the user wants:

- full scan
- light scan
- skip/defer for demo

Skipping literature or novelty assessment should be recorded with risk and required future timing.

### 2. Idea Maturity Classification

Planning should identify whether the project begins from:

- mature idea
- semi-formed idea
- early idea

This affects whether the workflow should emphasize idea generation, novelty assessment, feasibility checking, or rapid demo execution.

### 3. Exploratory Demo Before Full Scale

First runs should usually be small, complete demos.

Recommended structure:

```text
small demo -> Demo Gate -> revise workflow -> scale-up execution
```

Do not run full scale until the small demo has exposed and resolved major workflow assumptions.

### 4. Demo Gate Before Scale-Up

Add a specific Demo Gate:

```text
Do you approve the small demo structure before broader execution?
```

The user can approve, revise source scope, modify schemas, adjust synthesis categories, or pause.

### 5. Reporting / Packaging Before Review, Writing After Review

Separate:

- Reporting / Packaging: package artifacts for human review
- Reviewing: inspect evidence, claims, methods, and artifacts
- Writing: produce formal manuscript or polished deliverable after review

Reporting is not manuscript writing.

### 6. Run Manifest And Run Log

Every substantial run should include:

- `run_manifest.json`
- `run_log.md`
- `run_summary.md`
- validation outputs
- artifact links

The run log should record decisions, deviations, failed attempts, fixes, schema changes, and known limitations.

### 7. Skills As Persistent Agent Methods

Effective agent methods should become skills when they guide recurring agent behavior.

Recommended distinction:

```text
skills/      persistent reusable agent methods
artifacts/   run-specific outputs, logs, prompts, and intermediate products
code/        ordinary implementation code and tests
```

Do not create skills for ordinary code iteration.

### 8. Skill Promotion Ladder

Useful methods can move through:

```text
run note -> candidate skill -> formal skill
```

This prevents both losing useful methods and creating too many premature skills.

### 9. User Guidance And Gate Language

Codex should explicitly guide the user at each stage:

```text
Current stage:
Completed:
Decision needed:
If approved:
Other options:
```

Gate language should be lightweight and collaborative.

### 10. Claim Status

Substantive claims should have a status:

- candidate claim
- automated-supported claim
- human-reviewed claim
- limited claim
- rejected claim
- needs evidence

This prevents demo-level synthesis from being mistaken for final expert-reviewed findings.

### 11. Templates As Checklists

Stage templates should behave more like checklists, not blank prose shells.

Useful checklist fields:

- prior-work scan depth
- novelty status
- demo gate status
- source tiers defined
- run log created
- validation type
- claim status
- human review status
- external review status

### 12. Standardized Artifact Directories

Future projects should use more consistent run directories.

Possible pattern:

```text
artifacts/
  runs/
    20260618_small_demo/
      run_manifest.json
      run_log.md
      sources/
      kus/
      synthesis/
      validation/
      agent/
      reports/
```

## Current Decision

Do not modify the main framework yet.

This note records the approved revision ideas so they can be reviewed together before editing `AGENTS.md`, stage docs, templates, skills, and example packages.
