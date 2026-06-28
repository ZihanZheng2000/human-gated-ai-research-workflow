# Workflow Role Configuration

Edit this file to switch between Config A and Config B. Both `AGENTS.md` and
`CLAUDE.md` contain instructions for both roles and will follow this setting.
No other files need to change when switching configs.

## Current Configuration

**Config A**

| Agent | Role |
|---|---|
| Codex | Researcher — runs the four-stage workflow, produces and owns stage packages |
| Claude Code | Reviewer — critiques stage packages, writes structured findings |

## Available Configurations

| Config | Codex role | Claude Code role |
|---|---|---|
| **A** (current) | Researcher | Reviewer |
| B | Reviewer | Researcher |

## How to Switch

To switch to Config B:

1. Change `**Config A**` above to `**Config B**`.
2. Update the table to show Codex as Reviewer and Claude Code as Researcher.
3. Update the `(current)` marker in the Available Configurations table.

That is the only change needed. All stage specs, templates, skills, and
reviewer-agent files remain the same for both configs.
