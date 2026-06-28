# Workflow Revision Note: Skills As Persistent Agent Methods

Date: 2026-06-18

Status: accepted and promoted to framework docs/templates

Promoted on: 2026-06-18

Promoted into:

- `docs/stage-handoffs.md`
- `docs/skill-strategy.md`
- `docs/example-organization.md`
- `skills/README.md`
- `templates/model-package.md`

## Context

During the Reservoir Knowledge Base case study, several effective methods emerged only after iteration:

- source acquisition as a Layer 1 skill
- KU extraction as a Layer 2 skill
- synthesis analysis as a Layer 3 skill
- validation scripts tied to each layer

This suggests that skills should become a regular part of the workflow when the project is agent-organized. However, not every piece of code or every iteration needs to become a skill.

## Proposed Revision

Make skills a standard mechanism for preserving effective agent methods, but avoid over-skillifying ordinary code iteration.

Recommended principle:

```text
If the method guides agent behavior across runs, make it a skill.
If the code is just implementation detail, keep it as normal project code.
```

## When A Skill Is Useful

Create or update a skill when the method:

- defines how an agent should perform a recurring research task
- encodes workflow judgment, not just code mechanics
- has reusable steps across projects or runs
- protects important boundaries between stages or layers
- defines extraction, review, validation, or synthesis protocols
- prevents the agent from repeating earlier mistakes
- helps future agents understand what "good work" means in this project

Examples from the Reservoir KB case:

- how to collect and preserve reservoir sources
- how to extract operational KUs from documents
- how to distinguish source discrepancy from operational tradeoff
- how to validate synthesis cards against KU IDs

## When A Skill Is Not Necessary

Do not create a skill for every ordinary code change.

A skill is usually unnecessary when the task is:

- a one-off bug fix
- a normal refactor
- a small utility implementation
- project-specific code that does not encode reusable agent behavior
- ordinary exploratory scripting
- a function or module that belongs naturally in the codebase

For traditional iterative coding, the code itself, tests, and documentation may be enough.

## Agent-Oriented Projects Versus Traditional Code Projects

Skills are especially important when the agent organizes the research process:

```text
agent plans -> agent runs tools -> agent interprets artifacts -> agent prepares review package
```

In this setting, skills become persistent procedural memory.

Skills are less necessary when the project is mainly traditional software development:

```text
developer edits code -> tests run -> code review -> merge
```

In that setting, the stable knowledge usually belongs in source code, tests, README files, or developer documentation rather than a skill.

## Where To Store Agent Artifacts

Agent-related artifacts can be stored under `artifacts/` when they are produced during a project run.

Recommended distinction:

```text
skills/      persistent agent methods and reusable protocols
artifacts/   run-specific outputs, logs, prompts, intermediate products, validation results
```

Examples for `skills/`:

- `reservoir-source-acquisition/`
- `reservoir-ku-extraction/`
- `reservoir-synthesis-analysis/`

Examples for `artifacts/`:

- run logs
- prompts used for a specific run
- generated extraction packets
- intermediate candidate KUs
- validation summaries
- temporary agent scratch outputs
- run-specific decision records

## Possible Agent Artifact Folder

For agent-organized workflows, consider adding a run-specific agent artifact folder:

```text
artifacts/<run_id>/agent/
```

Potential contents:

- `agent_run_log.md`
- `agent_decisions.md`
- `prompts/`
- `intermediate_outputs/`
- `failed_attempts/`
- `handoff_notes.md`

This keeps run-specific agent behavior inspectable without confusing it with persistent skills.

## Naming Recommendation

Avoid calling run-specific artifacts "skills".

Use:

- `skills/` for reusable methods
- `artifacts/<run_id>/agent/` for what the agent did in a particular run
- `artifacts/<run_id>/logs/` for execution logs
- `artifacts/<run_id>/validation/` for validation outputs

## Rationale

Skills should become a normal part of agent-native academic workflows because they preserve process learning. But they should not replace code, tests, or normal documentation.

The key is to separate:

- reusable agent method
- run-specific agent trace
- implementation code
- project documentation

This avoids two failure modes:

1. Losing effective agent methods because they remain only in chat history.
2. Creating too many skills for small implementation details that should simply live in code.

## Promotion Summary

This proposal has now been incorporated into the main framework.

Implemented decisions:

- Reusable agent methods belong in `skills/`.
- Run-specific agent traces, prompts, decisions, intermediate outputs, and failed attempts belong under `artifacts/<run_id>/agent/`.
- Ordinary implementation code, tests, and project documentation should not be turned into skills unless they encode reusable agent behavior.
- Project-specific skills should be promoted to core workflow skills only after reuse and review.

Remaining note:

- The framework now defines where agent artifacts can live, but individual projects still decide which prompts, intermediate outputs, or critique packets are worth preserving.
