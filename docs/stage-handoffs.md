# Stage Handoffs

This document summarizes how the workflow stages connect. Each stage outputs one compact package. Downstream stages should read the approved package rather than reconstructing context from scattered notes.

## Linear Path

| Stage | Primary input | Primary output | Gate |
|---|---|---|---|
| Planning | user need, idea maturity, optional prior-work/novelty scan, feasibility checks, research-skill cards or skill candidates, Planning Reviewer critique, researcher-agent response/fix | Approved Planning Package | Planning Gate after reviewer response |
| Modeling / Execution | Approved Planning Package | Modeling Package, often after an exploratory demo phase inside Modeling | Modeling Gate |
| Reporting / Output Packaging | Approved Planning Package + Modeling Package | Reporting Package and reader-facing deliverables | Reporting Gate |
| Reviewing | Approved Planning Package + Modeling Package + Reporting Package | Review Package | Reviewing Gate |

## Default Route

The default route is:

1. Planning
2. Modeling / Execution, usually starting with a small exploratory demo when the workflow is new or uncertain
3. Reporting / Output Packaging
4. Reviewing

Reporting produces the reader-facing outputs. A paper, report, slide deck,
dashboard, web page, software package, technical appendix, or review packet is
a Reporting output mode, not a separate stage. Reviewing happens after
Reporting because reviewer agents need a concrete package and deliverables to
inspect.

## Stage Maker-Checker Rule

Each stage uses the same internal pattern before its user gate:

```text
Researcher agent produces or revises the stage package
-> Reviewer agent critiques the package and deliverables
-> Researcher agent responds, fixes, defers, rejects with reason, or escalates
-> User gate
```

Reviewer agents critique only by default. They should not modify files unless
the user explicitly authorizes edits. Reviewer findings should be recorded in
the stage package or linked as an agent artifact. The researcher-agent response
must classify each finding as accepted and fixed, accepted but deferred,
rejected with reason, or needing user decision.

If a reviewer-agent pass is skipped for any stage, the stage package must record
the reason, accepted risk, and revisit trigger before the user gate is presented
as ready.

## Backtracking Rules

Backtracking is normal. It is not a system failure.

| Trigger | Typical route |
|---|---|
| research question, idea maturity, or scope is wrong | Reviewing/Reporting/Modeling -> Planning |
| prior-work or novelty basis is too weak for the target claim | Reviewing/Reporting -> Planning or targeted literature addendum |
| data cannot support the approved method | Modeling/Reviewing -> Planning |
| exploratory demo does not pass basic feasibility or value checks | Modeling -> Planning or revise Modeling demo |
| code, robustness, extraction, validation, or empirical figure is missing | Reporting/Reviewing -> Modeling |
| evidence package is hard to inspect or lacks provenance | Reviewing -> Reporting |
| target venue or output route does not fit | Reviewing/Reporting -> Planning or Reporting |
| citation, source-support, or deliverable gap is local | Reviewing -> Reporting or targeted literature addendum |
| manuscript, slide, web, dashboard, or software-package argument is weak or report-like | Reviewing -> Reporting |
| project is infeasible, noncompliant, or misleading | Any stage -> Terminate |

## Package Discipline

The workflow should avoid creating many unreviewed side artifacts. Extra files can exist for code, data, figures, validation outputs, working notes, and drafts, but each stage should summarize them in its package.

Required packages:

- `templates/plan-package.md`
- `templates/model-package.md`
- `templates/reporting-package.md`
- `templates/review-package.md`

Supporting templates:

- `templates/research-skill-card.md`
- `templates/smoke-test-package.md`

Worked examples should not keep every file in the example root. Use the layout in [example-organization.md](example-organization.md):

- `packages/` for approved Planning, Modeling, Reporting, and Reviewing handoffs
- `deliverables/` for final or near-final reader-facing outputs
- `notes/` for literature, feasibility, method, and other working notes
- `artifacts/` for input, data, code, logs, tables, figures, validation outputs, and run-specific agent artifacts
- `archive/` for superseded files kept only for traceability

The example root should usually contain only `README.md`, `run-notes.md`, and the main folders above. This keeps the approved package flow separate from generated evidence and exploratory notes.

## Run Logs and Agent Artifacts

For substantial runs, especially exploratory demos that may later scale up, maintain:

- `artifacts/<run_id>/run_manifest.json` for version, scope, inputs, outputs, tools, and status
- `artifacts/<run_id>/run_log.md` for chronological decisions, failures, repairs, and gate notes
- `artifacts/<run_id>/run_summary.md` for the human-readable summary of what the run proved

If agent-specific skills, prompts, critiques, or coordination notes are created during a run, store them under:

- `artifacts/<run_id>/agent/`

Promote only reusable, evidence-backed agent methods into `skills/`. Keep run-specific agent material in artifacts.

## Human Gates

Each gate should answer three questions:

1. Is the stage output scientifically acceptable for its stated claim level?
2. What must be changed before downstream use?
3. Should the workflow proceed, revise locally, backtrack, scale up, finalize, release, archive, or terminate?

For autonomous framework tests, gate decisions must be labeled as **synthetic gates** rather than real user approvals. Synthetic gates are acceptable for smoke tests and QA runs, but they do not replace user, domain-owner, or expert approval in a real research project.

## Approval Semantics

Gate approval is an action, not only a status label. When the user approves a stage, the default behavior is to immediately begin the next downstream stage in the same turn if there is enough context and no explicit pause request.

Default transitions:

| User approval | Default next action |
|---|---|
| Planning Gate approved | Start Modeling by locking the modeling contract and, when appropriate, running a small exploratory demo first; this requires recorded Planning Reviewer critique or a recorded skip rationale plus researcher-agent response |
| Modeling Gate approved | Start Reporting / Output Packaging by ingesting the approved Planning and Modeling packages |
| Reporting Gate approved | Start Reviewing by stress-testing the evidence package and writing a Review Package |
| Reviewing Gate approved | Finalize, submit, share, archive, run a routed Modeling/Reporting addendum cycle, backtrack, or terminate according to the selected route |

The workflow should pause after approval only when:

- the user explicitly says to stop, pause, or wait
- the next stage needs information that cannot be inferred safely
- required data, tools, permissions, or files are unavailable
- the approval is conditional and the condition must be resolved first

If a stage is approved but the next stage cannot begin, the package should state why and list the smallest next action.

## Gate Language

At each gate, Codex should guide the user with a short decision prompt:

- current stage and package produced
- what was completed
- what decision is needed
- what will happen if the user approves
- what alternative routes are available

Use concrete language such as:

```text
This completes the Modeling package. The exploratory demo phase has been incorporated into the Modeling evidence and revision notes. If you approve the Modeling Gate, I will move to Reporting / Output Packaging. Alternative routes are: revise Modeling, narrow the scope, or return to Planning.
```
