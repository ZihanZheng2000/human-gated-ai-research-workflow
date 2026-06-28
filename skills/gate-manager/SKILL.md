---
name: gate-manager
description: Use whenever Planning, Modeling, Reporting, or Reviewing reaches a Human Gate; records approval, revision, backtracking, scale-up, finalization, archive, or termination decisions and automatically advances to the next stage after approval unless blocked or explicitly paused.
---

# Gate Manager Skill

## Use When

- a stage package is ready for user approval
- a Modeling package needs approval after an exploratory demo phase or full-scale execution
- the user says approve, revise, backtrack, pause, or terminate
- stage transition behavior must be recorded

## Inputs

- current stage package
- demo-phase summary, if Modeling used an exploratory demo
- gate questions
- user decision and notes
- known blockers
- gate mode: real user gate, synthetic gate, or mixed

## Procedure

1. Record the gate decision.
2. Label whether the decision is a real user gate, synthetic gate, or mixed gate.
3. If approved, mark the package status as approved.
4. Immediately begin the next stage unless the user explicitly pauses or the next stage is blocked.
5. If revised, route changes to the current stage.
6. If backtracked, route to the appropriate earlier stage.
7. If blocked, write the smallest next action needed.

## Default Transitions

- Planning approval -> Modeling
- Modeling approval -> Reporting / Output Packaging
- Reporting approval -> Reviewing
- Reviewing approval -> finalization, sharing, submission, archive, another routed Modeling/Reporting cycle, or termination

## Guardrails

- Approval is an action, not only a label.
- Synthetic gates are acceptable for framework smoke tests, but must not be represented as real user, domain-owner, or expert approval.
- Do not continue if the user says pause, stop, or wait.
- Do not hide blockers; state them and the next action.
- At each gate, state what was completed, what decision is needed, what happens if approved, and what alternatives exist.
