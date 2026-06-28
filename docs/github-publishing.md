# GitHub Publishing Guide

Recommended repository name:

`human-gated-ai-native-academic-research-workflow`

Recommended display title:

`A Human-Gated AI Research Workflow for Domain Researchers`

## Before Creating the Repository

1. Review `docs/release-checklist.md`.
2. Make sure `.env` is not committed.
3. Decide whether generated example data and figures should be included.
4. Replace contributor names and citation metadata if desired.
5. Review `docs/paper.md` for citation correctness.

## Suggested Repository Description

Human-gated, skill-guided workflow for evidence-grounded academic research by domain researchers.

## Suggested Topics

- ai-research
- academic-research
- research-workflow
- human-in-the-loop
- reproducible-research
- research-reporting
- research-agents
- llm-workflow

## First Commit Checklist

From the repository folder:

```powershell
git init
git add README.md LICENSE CONTRIBUTING.md CHANGELOG.md CITATION.cff .gitignore .env.example docs templates skills examples
git status
git commit -m "Prepare AI-Native Academic Research Workflow v0.1"
```

Then create a GitHub repository named `human-gated-ai-native-academic-research-workflow` and follow GitHub's instructions to add the remote and push.

After the repository URL exists, update:

- `CITATION.cff`
- `docs/paper.md`
- `docs/release-checklist.md`

## Suggested v0.1 Release Notes

Initial development release of AI-Native Academic Research Workflow, including:

- four-stage Planning -> Modeling -> Reporting / Output Packaging -> Reviewing framework
- demo-before-scale-up control and run-log conventions
- human gate and synthetic gate semantics
- package templates
- workflow-native skills
- smoke-test mode
- lightweight examples folder and example organization rules
- accompanying paper draft
