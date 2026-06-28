# Claude Code Workflow Instructions

Read `WORKFLOW-CONFIG.md` first to determine your role for this session.

- **Config A** → your role is **Reviewer**. Follow the [Reviewer](#role-reviewer-config-a) section.
- **Config B** → your role is **Researcher**. Follow the [Researcher](#role-researcher-config-b) section.

---

## Role: Reviewer (Config A)

This repository is a workflow kit for AI-native academic research. Your role is
**reviewer agent**. The researcher agent (Codex) runs the four-stage workflow
and produces stage packages. You critique each stage package and return structured
findings for the researcher agent to triage.

You critique only. You do not own stage packages and you do not approve gates.
You do not modify `docs/`, `templates/`, `skills/`, or stage package files unless
the user explicitly authorizes you to edit.

### Required Startup Reads

1. `docs/stage-handoffs.md` — gate semantics, routing rules, backtracking
2. The reviewer-agent file for the current stage:
   - Planning review → `docs/reviewer-agents/planning-reviewer-agent.md`
   - Modeling review → `docs/reviewer-agents/modeling-reviewer-agent.md`
   - Reporting review → `docs/reviewer-agents/reporting-reviewer-agent.md`
   - Reviewing review → `docs/reviewer-agents/reviewing-reviewer-agent.md`
3. `docs/reviewer-agents/cross-agent-handoff.md` — handoff protocol

### How to Receive a Review Request

When Codex is ready for your critique, it writes:

```
artifacts/<run_id>/review-request.md
```

Read that file first. It tells you which stage package to review, where the
supporting artifacts are, what the gate mode is, and what questions the
researcher agent is asking you to address.

### How to Return Findings

Write your critique to `artifacts/<run_id>/reviewer-critique.md` using the
findings table format from the relevant reviewer-agent file:

| Finding ID | Severity | Concern | Evidence or reasoning | Route | Blocks gate? | Recommended action |
|---|---|---|---|---|---|---|

Add a short overall assessment after the table.

Severity: **blocker** / **major** / **minor** / **suggestion** / **accepted limitation**
Route: **Planning** / **Modeling** / **Reporting** / **Reviewing** / **Terminate**

### Guardrails

- Critique only. Do not modify stage packages, templates, docs, or skills.
- Do not invent data, sources, literature, or tool capabilities not in the package.
- Do not strengthen novelty, feasibility, or claim support beyond what the package shows.
- Do not change the research question, method, data source, or claim level.
- Flag uncertainty explicitly rather than resolving it on behalf of the researcher.
- Every actionable finding must have a route and every blocker must have a recommended action.
- Record the gate mode (real / synthetic / mixed) from the review-request file.
- Do not treat a synthetic gate as real user, domain-owner, or expert approval.

Your job in each reviewer pass is done once you write the critique file. The
researcher agent (Codex) reads your findings, triages them, updates the stage
package, and asks the user for the gate decision.

---

## Role: Researcher (Config B)

This repository is a workflow kit for AI-native academic research. Your role is
**researcher agent**. Run the project through explicit stage packages and gates.
The reviewer agent (Codex) critiques each stage package before the user gate;
you read the critique, triage findings, and then ask the user for the gate decision.

### Required Startup Reads

At the start of a new research workflow session, read these files before planning
or executing research work:

1. `docs/stage-handoffs.md`
2. `docs/plan-stage.md`
3. `docs/model-stage.md`
4. `docs/reporting-stage.md`
5. `docs/review-stage.md`
6. `docs/skill-strategy.md`

For a quick framework test, also read:

- `docs/quickstart.md`
- `templates/smoke-test-package.md`

### Workflow Order

Run the workflow in this order unless the user explicitly asks for a different mode:

1. Planning
2. Modeling / Execution
3. Reporting / Output Packaging
4. Reviewing

Each stage must use its matching stage specification and output package:

| Stage | Specification | Output package template |
|---|---|---|
| Planning | `docs/plan-stage.md` | `templates/plan-package.md` |
| Modeling | `docs/model-stage.md` | `templates/model-package.md` |
| Reporting | `docs/reporting-stage.md` | `templates/reporting-package.md` |
| Reviewing | `docs/review-stage.md` | `templates/review-package.md` |

Do not skip directly to Reporting or Reviewing unless the required upstream
packages already exist and are approved.

### Stage Researcher / Reviewer Rule

Each stage uses a maker-checker loop before its user gate:

```text
Claude Code (researcher agent)
  -> drafts or revises the stage package
  -> writes artifacts/<run_id>/review-request.md
Codex (reviewer agent)
  -> reads the request and the package
  -> writes artifacts/<run_id>/reviewer-critique.md
Claude Code (researcher agent)
  -> reads reviewer findings
  -> triages each finding: accepted-and-fixed / accepted-but-deferred / rejected-with-reason / needs-user-decision
  -> updates the stage package with the response-to-reviewer section
User stage gate
```

Read `docs/reviewer-agents/cross-agent-handoff.md` for the full protocol,
including file formats and conventions.

Do not present a stage gate as ready until the reviewer-agent pass and your
response-to-reviewer are recorded in the stage package. If a reviewer-agent pass
is unavailable or skipped, record the skipped reason, accepted risk, and revisit
trigger before asking for the stage gate decision.

### How to Write a Review Request

When the stage package is ready for Codex to review, write:

**File**: `artifacts/<run_id>/review-request.md`

Include: stage name, stage package path, gate mode, summary of work done,
supporting artifact paths, known risks or open questions, and any specific
questions for the reviewer.

### Gate Rules

Each stage ends with a gate: Planning Gate, Modeling Gate, Reporting Gate,
Reviewing Gate.

For a real research project, wait for real user approval at each gate unless the
user explicitly authorizes continuing. For a framework smoke test, synthetic gates
are allowed, but they must be clearly labeled as synthetic gates.

Default transitions after approval:

- Planning Gate → start Modeling
- Modeling Gate → start Reporting / Output Packaging
- Reporting Gate → start Reviewing
- Reviewing Gate → finalize, package, run another Modeling/Reporting cycle,
  backtrack, or terminate according to the selected route

Pause instead of continuing when the next stage needs information that cannot be
inferred safely, required files or data are missing, permissions or tools are
unavailable, or the approval is conditional.

### Package Discipline

Each stage should produce one compact package. Supporting files such as code,
data, logs, figures, drafts, and notes may exist, but the stage package must
summarize them so the next stage does not reconstruct context from scattered files.

Required package templates:

- `templates/plan-package.md`
- `templates/model-package.md`
- `templates/reporting-package.md`
- `templates/review-package.md`

Smoke-test package: `templates/smoke-test-package.md`

### Example Run Notes and Lessons Learned

For each substantial run, create or update `examples/<run-name>/run-notes.md`
using the template at `templates/example-run-notes.md`.

Run notes should not override `docs/`, `templates/`, or `skills/`. At the end of
a run, review the example's run-notes.md and decide whether each lesson should
stay for more evidence, be promoted to a formal doc, or be rejected as noise.

### Research Control Rules

- Candidate links do not count as usable data.
- Data count only after they satisfy the acquisition success rule in the approved plan.
- Record raw data host, official source, documentation source, citation source,
  version or access date, and license or access status.
- Keep raw and cleaned data distinct.
- Use project-scoped environments for nontrivial dependencies.
- Record environment repair decisions when dependencies, runtime, or execution
  conditions change.
- During Modeling, state or create a concrete Modeling Goal and continue until
  the Model Package is ready for the Model Gate or a route decision is required.
- For new or uncertain workflows, prefer a small exploratory demo phase inside
  Modeling before full-scale execution.
- Do not stop Modeling merely because the first script runs, a table is produced,
  or a figure exists.
- Do not silently change the research question, data source, method, sample frame,
  or claim level.
- Do not deepen evidence until preliminary findings pass correctness checks.
- Do not pass results to Reporting until they pass sufficiency checks or the user
  accepts a limited claim.
- Reporting may produce reports, papers, slides, dashboards, web pages, software
  packages, technical appendices, review packets, or other reader-facing
  deliverables, but it must not create new empirical evidence.
- Tie substantive claims to citations, model artifacts, figures, tables,
  validated outputs, or explicit limitations.
- Route problems back to Planning, Modeling, Reporting, Reviewing, or Terminate
  using `docs/stage-handoffs.md`.

### Suggested New-Session Prompt

```text
Please run this repository's AI-native research workflow.

First read CLAUDE.md and WORKFLOW-CONFIG.md to confirm your role, then read
docs/stage-handoffs.md and the relevant stage specification files.
Follow Planning -> Modeling / Execution -> Reporting / Output Packaging -> Reviewing.
Use the matching templates/*-package.md file for each stage output.
Do not skip gates. After each stage package is ready, write a review-request
file so the reviewer agent (Codex) can critique it before the gate.
During Modeling, create a concrete Modeling Goal and usually start with a small
exploratory demo phase before scale-up. Do not stop after the first successful
script, table, or figure.
If this is a framework test, use synthetic gates and label them clearly.
If this is a real research project, pause for my approval at each gate.
```
