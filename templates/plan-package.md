# Approved Plan Package

## Planning Workflow Identity

- package status: draft for Planning Review / revised after Planning Review / approved
- Planning Researcher: researcher agent name or runtime
- Planning Reviewer: reviewer agent name or runtime / skipped
- reviewer file: `docs/reviewer-agents/planning-reviewer-agent.md`
- reviewer mode: critique-only / edits explicitly authorized by user / skipped
- Planning Review status: pending / completed / skipped
- researcher-agent response status: pending / completed / not applicable
- user Planning Gate status: pending / approved / revise / backtrack / terminate

## User-Need Profile

- research area:
- intended output:
- workflow mode: full research / compact smoke test / demo / internal report
- idea maturity: exploratory idea / partly formed idea / mature idea / revision or implementation task
- planning depth: full calibration / light calibration / skip or defer
- intended research product: empirical finding / method / dataset / benchmark / skill / workflow demo / manuscript package
- research purpose: discover pattern / build method or tool / validate intervention / revise existing artifact / compare alternatives / other
- practical success criterion:
- target audience or venue:
- venue/output status: confirmed / system-recommended / provisional / undecided / deferred to Reporting
- preferred citation or formatting style:
- available data:
- public data needed:
- time/tooling constraints:
- runtime or API/token constraints:
- method-complexity limit:
- novelty expectation:
- topics, methods, or data types to avoid:
- gate mode: real user gates / synthetic gates / mixed

## Domain Onboarding

Complete this section when user-supplied domain materials were provided before
Planning began. Leave blank and mark "skipped — no user materials" if none.

### Material Inventory

| File or folder | Material type | Domain covered | Date or version |
|---|---|---|---|
| | paper / report / data documentation / policy doc / field notes / other | | |

### Domain Knowledge Summary

Compact record of what was learned from user-supplied materials that is not
obvious from general AI knowledge. This should govern field-specific decisions
throughout Planning, Modeling, and Reporting.

**Key domain concepts and terminology:**

**Field norms or conventions relevant to this project:**

**Domain-specific constraints (data access, measurement, ethics, reporting):**

**Conflicts or uncertainties found in the materials:**

**User resolution for any conflicts:**

### Skill Cards Generated from User Materials

List any research-skill cards produced from user-supplied materials using
`/research-skill-card-distiller`. These supplement cards produced from
retrieved papers in step 6.

| Card ID | Source material | Pattern captured | Status |
|---|---|---|---|
| | | | selected / provisional / rejected |

### Domain Onboarding Status

- status: completed / skipped — no user materials / skipped — user declined / deferred
- materials read: [count] files
- skill cards produced: [count]
- downstream implications flagged: yes / no

## Planning Depth Decision

| Item | Decision | Reason | Downstream implication |
|---|---|---|---|
| idea maturity | exploratory / partly formed / mature / revision |  |  |
| literature/prior-work scan depth | full / light / skipped / deferred |  |  |
| novelty assessment depth | full / light / skipped / deferred |  |  |
| venue/output calibration depth | full / light / skipped / deferred |  |  |
| revisit trigger |  | before scale-up / before Reporting / before Review / before submission / other |  |

## Clarifications Before Planning

| Question or ambiguity | Resolution | Effect on plan |
|---|---|---|
|  |  |  |

## Prior Work, Skill Patterns, and Gaps

This section records the focused literature and prior-work scan. It should be compact, but it should be completed before the full plan is written.

| Cluster or source | What has been done | Reusable skill or method pattern | Gap or opportunity | Relevance to this plan |
|---|---|---|---|---|
|  |  |  |  |  |

## External Tool and Skill Scan

This section records mature external tools, packages, templates, databases, or existing skills that could be reused before creating new project-specific skills.

| Candidate tool, package, template, or skill | Workflow task | Maturity or reason to trust | Output to bring back | Cost/access/limits | Decision |
|---|---|---|---|---|---|
|  | literature / data / model / writing / citation / formatting / review / other |  |  |  | reuse / wrap / adapt / reject / create new skill |

## Skill Construction Decision

| Skill need | External alternative checked | Why external option is sufficient or insufficient | Decision | Promotion status |
|---|---|---|---|---|
|  |  |  | no skill needed / use existing skill / create project-specific skill / promote to core later | none / project-specific / candidate core |

## Research Opportunities Considered

| Opportunity | Prior-work basis | Feasibility | Novelty | Decision |
|---|---|---|---|---|
|  |  |  |  | selected / rejected / backup / future work |

## Feasibility and Cost Check

| Item | Assessment | Evidence or test | Fallback |
|---|---|---|---|
| data access | feasible / uncertain / blocked |  |  |
| text/table/image/API extractability | feasible / uncertain / blocked |  |  |
| candidate sources vs usable acquired data |  |  |  |
| demo scale |  |  |  |
| full-study scale |  |  |  |
| runtime/storage burden |  |  |  |
| API/token cost |  |  |  |
| external tool or skill feasibility |  |  |  |
| licensing/privacy/ethics |  |  |  |

## Data Source Identity

Use this section whenever data will be downloaded, scraped, queried, or extracted. Distinguish exact raw data from documentation and citation sources.

| Role | Source name or URL | Version/date/access date | License/access status | Notes |
|---|---|---|---|---|
| raw data host |  |  |  |  |
| official data source |  |  |  |  |
| documentation source |  |  |  |  |
| citation source |  |  |  |  |

## Venue or Output Calibration

| Candidate venue/output | Why it fits | Tradeoffs | Decision |
|---|---|---|---|
|  |  |  | selected / rejected / backup / deferred |

If no venue is selected, state the provisional route and when it should be revisited.

### Official Venue Requirements

| Requirement | Official rule or constraint | Effect on plan |
|---|---|---|
| article type and scope |  |  |
| manuscript structure |  |  |
| word/page limit |  |  |
| abstract format |  |  |
| reference style |  |  |
| figure/table rules |  |  |
| data/code availability |  |  |
| ethics/funding/COI/AI disclosure |  |  |
| reporting checklist or supplement rules |  |  |

### Venue Exemplar Scan

Inspect 2-5 recent structurally similar articles from the selected or candidate venue when the intended output is a formal manuscript.

| Exemplar | Why similar | Structure pattern | Evidence/validation pattern | Figure/table pattern | Citation pattern | Implication for this plan |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

### Venue-Derived Plan Constraints

| Constraint from venue or exemplars | Required plan response | Status |
|---|---|---|
|  | data scale / validation / robustness / citation depth / article type / visual plan / disclosure | satisfied / needs Model / needs Reporting / infeasible / deferred |

## Candidate Research Plans Considered

Use this section only if more than one plausible route was considered.

| Plan | RQ | Data | Method | Venue/output fit | Decision |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Planning Reviewer Critique

Use this section before the user Planning Gate. The reviewer agent should be separate from the researcher agent when available and approved by the user. The reviewer critiques only unless the user explicitly authorizes edits.

| Finding ID | Reviewer concern | Severity | Evidence or reasoning | Route |
|---|---|---|---|---|
| PR-1 |  | blocker / major / minor / suggestion / accepted limitation |  | Planning fix / Modeling constraint / user decision / accepted limitation / terminate |

If external Planning Review was skipped, record why:

- skipped reason:
- risk accepted:
- revisit trigger:

## Researcher-Agent Response to Planning Review

The researcher agent must respond to reviewer findings before the user Planning Gate.

| Finding ID | Response status | Change made or planned | Blocks Planning Gate? | Notes |
|---|---|---|---|---|
| PR-1 | accepted and fixed / accepted but deferred / rejected with reason / needs user decision |  | yes / no |  |

## Approved Research Question

`<one clear question>`

## Working Title

`<title>`

## Hypotheses or Expected Claims

- `<hypothesis or expected claim>`

## Data Plan

- primary data source:
- backup data source:
- exact raw data host:
- official data source:
- documentation source:
- data version or access date:
- license/access status:
- acquisition success rule:
- minimum viable data scale:
- full-study data scale:
- key variables:
- unit of analysis:
- time/spatial coverage:
- access or licensing concerns:

## Method Blueprint

1. `<analysis step>`
2. `<analysis step>`
3. `<analysis step>`

## Expected Manuscript Package

- figures:
- tables:
- likely method/conceptual visuals:
- claim-evidence map:
- limitations to acknowledge:
- reproducibility artifacts:

## Risks and Gate Notes

| Risk | Severity | Mitigation |
|---|---|---|
|  |  |  |

## Planning Gate Decision

- decision: approve for Modeling / revise Planning / request another Planning Review / backtrack / terminate
- gate mode: real user gate / synthetic gate / mixed
- decision maker:
- date:
- required changes before Modeling:
- accepted limitations:
- unresolved user decisions:

## Acceptance Rubric for Model Stage

The Model stage can begin only if:

- the research purpose and final product are clear
- the planning depth decision is explicit
- the prior-work scan supports the proposed gap or opportunity, or its skip/defer decision is recorded with a revisit trigger
- useful prior-work patterns or skill candidates have been captured
- the required data can be accessed or a fallback data source is approved
- candidate sources have been distinguished from actually usable data
- the selected method is feasible under the user's constraints
- expected runtime and API/token cost are acceptable or capped
- the core assumptions are explicit
- expected figures or tables are defined
- unresolved risks are either mitigated or accepted by the user
- Planning Reviewer findings are fixed, deferred with triggers, rejected with reasons, or escalated for user decision
- the user has approved the Planning Gate after the researcher-agent response to Planning Review
