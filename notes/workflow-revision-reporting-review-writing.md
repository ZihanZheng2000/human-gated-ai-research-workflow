# Workflow Revision Note: Reporting, Review, and Writing Order

Date: 2026-06-18

Status: proposal only; framework files not yet modified

## Context

During the Reservoir Knowledge Base case study, the workflow exposed a sequencing issue: formal manuscript writing should not happen before review.

The original stage language can make "Reporting" feel like a writing/manuscript stage. In practice, the Reservoir KB run showed that the output immediately after Modeling/Execution is not ready for formal academic writing. It first needs to be packaged for human review.

## Proposed Revision

Separate "Reporting / Packaging" from formal "Writing".

Recommended stage order:

```text
Planning -> Modeling / Execution -> Reporting / Packaging -> Reviewing -> Writing
```

Alternative wording:

```text
Planning -> Execution -> Evidence Package -> Review -> Manuscript Writing
```

## Key Distinction

Reporting is not manuscript writing.

Reporting / Packaging should mean:

- organize modeling/execution artifacts into a human-reviewable package
- summarize results without overstating claims
- prepare short reports, technical appendices, artifact maps, validation summaries, key tables/figures, limitations, and review questions
- make it possible for a human reviewer, domain expert, PI, or collaborator to inspect the work

Writing should happen after review, when reviewed findings and accepted claims are known.

## Rationale

Modeling/Execution produces artifacts, not necessarily review-ready knowledge:

- raw sources
- extracted text
- scripts
- JSONL outputs
- validation files
- figures/tables
- intermediate findings
- limitations and unresolved issues

If the workflow moves directly from Modeling to Reviewing, reviewers may face too many raw artifacts. If it moves directly from Modeling to Writing, the manuscript may be built on unreviewed or unstable claims.

Reporting / Packaging creates a useful bridge:

```text
Modeling answers: What did we do and what came out?
Reporting answers: How do we package it for human review?
Reviewing answers: What is reliable and what should change?
Writing answers: How do we turn reviewed results into a manuscript?
```

## Suggested Stage Definitions

### Planning

Define the research goal, scope, sources/data, methods, success criteria, risks, and gate conditions.

### Modeling / Execution

Run the actual research workflow: collect data, process sources, build models, extract evidence, run experiments, generate intermediate artifacts, and perform automated validation.

This stage should not be responsible for producing polished narrative writing.

### Reporting / Packaging

Transform execution artifacts into a review package.

Expected outputs may include:

- short report
- technical appendix
- artifact index
- validation summary
- key findings brief
- figures and tables for review
- limitations and caveats
- open questions for reviewers
- recommended next steps

### Reviewing

Perform human review, domain review, PI review, self-critique, evidence review, claim review, or method review.

The review stage decides:

- which findings are reliable
- which claims need to be weakened or removed
- which evidence needs more checking
- which artifacts are acceptable
- what must change before writing

### Writing

Produce the formal manuscript, paper, proposal, presentation, or final polished deliverable from reviewed findings.

Writing should not be treated as complete until it reflects review decisions.

## Implications For Future Framework Revision

When the framework is revised, update:

- `AGENTS.md` stage definitions
- README workflow diagrams
- templates that currently imply Reporting equals manuscript writing
- review package templates
- any skill or command descriptions that route directly from modeling outputs to paper writing

## Current Decision

Do not modify the framework yet.

This note records the proposed change so it can be reviewed before editing the main workflow files.
