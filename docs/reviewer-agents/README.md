# Reviewer Agents

Reviewer-agent files define critique-only work for each stage. They are not
stage packages and they do not replace user gates. They tell a separate reviewer
agent what to inspect before the researcher agent responds and asks the user for
the stage gate decision.

Default rule:

```text
Reviewer agents critique only.
Reviewer agents do not modify files unless the user explicitly authorizes edits.
Researcher agents own the stage package and response-to-review.
```

Stage reviewer files:

| Stage | Reviewer file | Reviewed package |
|---|---|---|
| Planning | `planning-reviewer-agent.md` | `templates/plan-package.md` |
| Modeling | `modeling-reviewer-agent.md` | `templates/model-package.md` |
| Reporting | `reporting-reviewer-agent.md` | `templates/reporting-package.md` |
| Reviewing | `reviewing-reviewer-agent.md` | `templates/review-package.md` |

Each reviewer finding should include:

- finding ID
- severity: blocker / major / minor / suggestion / accepted limitation
- evidence or reasoning
- route: Planning / Modeling / Reporting / Reviewing / Terminate
- whether it blocks the stage gate
- recommended action

