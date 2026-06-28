# Cross-Agent Handoff Protocol

This document defines how the researcher agent and reviewer agent exchange work
inside each stage's maker-checker loop.

Check `WORKFLOW-CONFIG.md` to see which agent is currently the researcher and
which is the reviewer:

| Config | Researcher agent | Reviewer agent |
|---|---|---|
| A | Codex | Claude Code |
| B | Claude Code | Codex |

The handoff protocol below is the same for both configs. Substitute the current
researcher and reviewer agents from the table above.

---

## The Loop

```
[researcher-agent] drafts or revises the stage package
  -> [researcher-agent] writes artifacts/<run_id>/review-request.md
  -> [reviewer-agent] reads the request and the stage package
  -> [reviewer-agent] critiques and writes artifacts/<run_id>/reviewer-critique.md
  -> [researcher-agent] reads findings, triages each one, updates the stage package
  -> [researcher-agent] asks the user for the stage gate decision
  -> User approves, revises, backtracks, or terminates
```

---

## Step 1: Researcher Writes the Review Request

**File**: `artifacts/<run_id>/review-request.md`

The researcher agent writes this file when the stage package is ready for
reviewer critique. The file must contain:

```markdown
# Review Request

- Stage: [Planning / Modeling / Reporting / Reviewing]
- Run ID: <run_id>
- Gate mode: [real user gate / synthetic gate / mixed]
- Stage package path: <path to the stage package file>
- Researcher agent: [Codex / Claude Code]
- Date: <date>

## Summary of Work Done

<brief summary of what was completed in this stage>

## Supporting Artifacts

<list of paths to data files, figures, run logs, scripts, or other artifacts
that the reviewer should inspect>

## Known Risks or Open Questions

<list any issues the researcher is uncertain about or wants the reviewer to focus on>

## Specific Questions for the Reviewer

<optional: specific questions for the reviewer agent>
```

---

## Step 2: Reviewer Reads and Critiques

The reviewer agent reads:

1. `artifacts/<run_id>/review-request.md`
2. The stage package at the path listed in the request
3. The relevant reviewer-agent file:
   - Planning → `docs/reviewer-agents/planning-reviewer-agent.md`
   - Modeling → `docs/reviewer-agents/modeling-reviewer-agent.md`
   - Reporting → `docs/reviewer-agents/reporting-reviewer-agent.md`
   - Reviewing → `docs/reviewer-agents/reviewing-reviewer-agent.md`
4. Supporting artifacts referenced in the request

The reviewer agent writes findings to:

**File**: `artifacts/<run_id>/reviewer-critique.md`

The file must contain:

```markdown
# Reviewer Critique

- Stage: [Planning / Modeling / Reporting / Reviewing]
- Reviewer agent: [Codex / Claude Code]
- Gate mode acknowledged: [real / synthetic / mixed]
- Date: <date>

## Findings

| Finding ID | Severity | Concern | Evidence or reasoning | Route | Blocks gate? | Recommended action |
|---|---|---|---|---|---|---|
| RC-1 | blocker/major/minor/suggestion/accepted limitation | | | Planning/Modeling/Reporting/Reviewing/Terminate | yes/no | |

## Overall Assessment

<one short paragraph: is the stage package ready for the user gate as-is,
ready after minor fixes, or does it need substantial revision before the gate>
```

---

## Step 3: Researcher Reads Findings and Responds

The researcher agent reads `artifacts/<run_id>/reviewer-critique.md` and adds a
**Response to Reviewer** section to the stage package. Each finding must be
classified as one of:

- **Accepted and fixed**: what was changed
- **Accepted but deferred**: why and when it will be addressed
- **Rejected**: reason for rejection
- **Needs user decision**: escalated to the user at the gate

After triaging all findings, the researcher agent presents the stage gate to the
user with: what was completed, what the reviewer found, how each finding was
triaged, what decision is needed, what will happen if approved, and what
alternative routes exist.

---

## Skipped Reviewer Pass

If the reviewer agent is unavailable or the reviewer pass is skipped for any
stage, the researcher agent must record in the stage package:

- reason the pass was skipped
- accepted risk
- revisit trigger (when or under what condition the critique will be done)

A skipped reviewer pass does not block the gate, but it must be labeled in the
package and presented to the user at the gate decision.

---

## File Conventions

- `<run_id>` is consistent across all files for the same run.
  Use a descriptive slug such as `smoke-test-2026-06-28` or `water-env-plan-v1`.
- Do not delete review-request or reviewer-critique files after a stage completes.
  Keep them under `artifacts/<run_id>/` for traceability.
- For revision passes, append `-r2`, `-r3`, etc.:
  `artifacts/<run_id>/reviewer-critique-r2.md`
- Reviewer-critique files are reviewer input to the researcher agent's
  response-to-reviewer section. They are not stage packages and do not replace
  user gate decisions.
