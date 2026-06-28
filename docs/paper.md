# A Human-Gated AI Research Workflow for Domain Researchers

## Abstract

Large language models can now retrieve literature, write prose, generate code, and simulate aspects of peer review. Yet for many non-CS researchers, the practical bottleneck is not a lack of isolated AI capabilities. It is the absence of a simple, inspectable workflow that turns a research intent, public or local data, literature, and domain judgment into a reproducible research-output package without handing scientific responsibility to an opaque autonomous agent. We present **AI-Native Academic Research Workflow**, a human-gated and skill-guided framework organized around four stages: **Planning**, **Modeling**, **Reporting / Output Packaging**, and **Reviewing**. Each stage produces a compact package, and each package must pass a gate before downstream use. The workflow is implemented through modular skills for venue calibration, research-skill-card distillation, model-contract execution, evidence packaging, claim-evidence mapping, route-aware review, and gate management. Unlike fully autonomous scientist systems, the framework treats human approval, source provenance, executable analysis, evidence packaging, claim-evidence mapping, and revision routing as first-class mechanisms. The framework also formalizes explicit data-source identity tracking, environment repair decisions, demo-before-scale-up control, output-type-specific citation thresholds, and route-aware review so that downstream research claims remain tied to inspectable evidence. The contribution is architectural and procedural: a practical research operating protocol for evidence-grounded, human-accountable AI-assisted scholarship.

## 1. Introduction

AI-assisted research tooling is advancing quickly. General agent frameworks support tool use and delegated task execution; deep-research systems conduct multi-step retrieval and source synthesis; autonomous scientist systems generate hypotheses, run experiments, draft papers, and simulate review; and specialized scientific RAG tools help answer literature-grounded questions. These systems are useful, but they do not fully solve the everyday problem faced by many domain researchers: how to move from a research idea and available evidence to a manuscript package that is transparent enough to inspect, correct, reproduce, and defend.

The issue is not merely whether AI can produce research-like text. Scientific work requires accountable problem framing, data provenance, executable analysis, claim boundaries, source support, reproducibility, and domain judgment. Recent concerns about fabricated citations and unsupported claims show why manuscript generation cannot be treated as a final writing step detached from evidence control. At the same time, purely autonomous scientific loops can obscure where a research question changed, where data access failed, where analysis assumptions entered, or where a claim exceeded the evidence.

This problem is especially visible from the perspective of researchers outside computer science. Many AI-native research systems are shaped around computer-science research rhythms, where a project can often be scoped, implemented, evaluated, and written within a relatively short cycle. In many non-CS domains, however, research work may unfold over much longer periods, sometimes over several years, because the researcher must combine literature reading, domain judgment, data access, field-specific methods, writing conventions, and institutional constraints. For such researchers, the value of AI assistance is not only faster text production or more autonomous execution. The practical need is a simple, learnable workflow that can reduce the friction of research work while remaining understandable to people who do not want to adopt a complex software engineering stack. This observation motivates the framework's emphasis on modest installation, plain stage packages, explicit gates, and reusable skills that accelerate non-CS research without making the research process harder to inspect or use.

This paper proposes a deliberately modest alternative: **AI-Native Academic Research Workflow**, a workflow kit for human-gated, evidence-grounded academic research. The framework does not claim to replace researchers or train a new model. Instead, it organizes AI assistance into four inspectable stages: **Planning -> Modeling -> Reporting / Output Packaging -> Reviewing**. Each stage has its own package template, its own checks, and its own gate. The human researcher approves, rejects, edits, supplements, or backtracks before outputs move downstream.

The current version of the framework has evolved beyond an initial conceptual outline. It now includes:

- a single Planning stage that begins with purpose clarification, prior-work scanning, skill-pattern distillation, feasibility checks, external tool/skill scanning, and venue calibration;
- a Modeling stage that usually starts uncertain workflows with a small exploratory demo, counts only usable acquired data, records data-source identity, handles environment repair decisions, writes Preliminary Finding Briefs, and runs bounded evidence-deepening loops;
- a Reporting / Output Packaging stage that organizes evidence, provenance, findings, uncertainties, and reader-facing deliverables such as reports, papers, slides, dashboards, web pages, software packages, and review packets;
- a Reviewing stage that combines internal self-review with optional critique-only external-agent review and routes issues across upstream completeness, scientific validity, reproducibility, claim support, disclosure, and readiness;
- a skill strategy distinguishing mature external tools, workflow-native skills, and project-specific skills.

The central claim is that useful AI-native research assistance for non-CS domains should be **staged, evidence-grounded, human-gated, and route-aware**. The framework is intended to make AI assistance easier to inspect and correct, not to maximize autonomy for its own sake.

## 2. Related Work and Positioning

The framework sits between several lines of work.

General autonomous-agent systems such as AutoGPT emphasize open-ended task execution. Multi-agent frameworks such as AutoGen and MetaGPT provide orchestration, role specialization, and tool use. Deep-research products from OpenAI and Google emphasize multi-step retrieval, source synthesis, and user-visible research plans. Autonomous scientist systems such as *The AI Scientist* and *The AI Scientist-v2* pursue end-to-end scientific loops. Data-to-paper systems, research-agent systems, and scientific RAG tools explore narrower research-support capabilities.

These systems supply important building blocks, but they are not identical to the objective here. This framework is not another general agent runtime, not an autonomous scientist benchmark, and not only a citation-backed literature assistant. It targets a practical manuscript-development workflow for researchers who need to inspect and own the result.

| Family | Representative systems | Strength | Remaining gap for this work |
|---|---|---|---|
| General autonomous agents | AutoGPT | broad task automation | not organized around scientific validity gates |
| Multi-agent orchestration | AutoGen, MetaGPT | agent composition and role specialization | not a complete domain-research package protocol |
| Deep research systems | OpenAI Deep Research, Gemini Deep Research | retrieval and source synthesis | not a full Planning-Modeling-Reporting-Reviewing lifecycle |
| Autonomous scientist systems | AI Scientist, AI Scientist-v2 | ideation, experimentation, paper generation | high autonomy; weaker human-gate emphasis |
| Scientific RAG and research agents | PaperQA, ResearchAgent, data-to-paper systems | literature grounding or task-specific research support | not a general human-gated package workflow |
| Proposed framework | AI-Native Academic Research Workflow | package handoffs, gates, evidence controls, route-aware review | trades autonomy for inspectability and accountability |

The novelty claim is therefore procedural rather than model-level. The contribution is a compact operating protocol that makes stage transitions, evidence packages, skill reuse, data acquisition, writing support, and review routing explicit.

## 3. Framework Overview

The framework has two layers.

The first layer is the **workflow layer**: four stages, stage packages, gate decisions, backtracking rules, exploratory demo phases inside Modeling, and final handoffs.

The second layer is the **skill layer**: small reusable skills used inside stages. These skills are not meant to replace mature external tools. Literature-search systems, citation managers, statistical packages, journal templates, document editors, and visualization tools should be reused when they are reliable. Internal workflow-native skills mainly orchestrate, verify, package, and route outputs.

| Stage | Main question | Main output | Gate question |
|---|---|---|---|
| Plan | What exactly should be studied, why, and under what constraints? | Approved Plan Package | Is this the right research route and is it feasible? |
| Model | Can the approved plan be executed on real usable data? | Model Package | Are the outputs correct, sufficient, and reproducible enough for the accepted claim level? |
| Reporting / Output Packaging | What evidence package and reader-facing deliverables are inspectable, and what can be claimed from them? | Reporting Package | Are the outputs evidence-bound, traceable, readable, and ready for review? |
| Review | What would Codex self-review or an external critic challenge? | Review Package | What must be revised, backtracked, accepted as limitation, or terminated? |

The stage packages matter because they prevent downstream stages from reconstructing context from scattered notes. The package is the approved memory of the stage.

## 4. Plan Stage

The Plan stage converts a vague or concrete research intent into one approved plan package. In the current framework, Plan is **purpose-first, literature-calibrated, skill-aware, feasibility-aware, venue-aware, and creativity-preserving**.

Plan should not begin by asking AI to generate polished project ideas from general intuition. It should begin by clarifying the user's actual research purpose and intended product. It should then ask missing questions, run a focused literature and prior-work scan, scan for mature external tools or existing skills, distill useful prior work into research-skill cards or method patterns, extract gaps and opportunities, run feasibility and cost checks, and calibrate the intended venue or output route.

The current Plan flow is:

1. Clarify research purpose and intended product.
2. Ask missing questions before writing the plan.
3. Run a focused literature and prior-work scan.
4. Scan for mature external tools, packages, templates, and existing skills.
5. Distill useful prior work into research-skill cards or skill candidates.
6. Extract gaps, opportunities, and possible research routes.
7. Run feasibility and cost checks.
8. Calibrate target venue, audience, or output format using official requirements and exemplar articles.
9. Generate candidate research plans only if multiple plausible routes remain.
10. Pass through the Plan Gate.
11. Output one Approved Plan Package.

Two additions are especially important.

First, Plan now includes **external tool and skill scanning**. Before creating a new project-specific skill, the workflow asks whether mature external tools, packages, templates, datasets, or public skills already solve the task. The preferred order is to reuse mature tools, wrap them through workflow-native skills when needed, and create new project-specific skills only when no adequate external operation exists.

Second, Plan now records **data-source identity** before Model begins. For data projects, it is not enough to name a dataset loosely. The package should distinguish:

- exact raw data host or query endpoint;
- official data source or data owner;
- documentation source;
- citation source;
- version, release date, query date, or access date;
- license or access constraints.

This distinction matters because raw data, official documentation, package excerpts, mirrors, and citation sources can diverge. A mirror or package excerpt should not silently stand in for the official data source unless that relationship is verified.

## 5. Model Stage

The Model stage converts the Approved Plan Package into executable artifacts: data acquisition, data-quality checks, analysis code, logs, figures, tables, and a validated result summary.

Model is not just "write code and run it." It is a bounded evidence-building loop. The current design contains:

- modeling contract;
- data-source identity confirmation;
- acquisition under explicit success rules;
- preflight checks;
- data-quality audit and cleaning log;
- minimal executable analysis;
- execution logs;
- validation against the contract;
- Preliminary Finding Brief;
- model state tracker;
- model critic pass;
- next-analysis queue;
- repair, cleaning, environment repair, method-fidelity, and evidence-deepening loops;
- claim-readiness matrix;
- Model Gate.

The most important rule is that **candidate links, metadata records, search hits, or inaccessible files do not count as usable data** unless the plan explicitly defines them as data. A table counts only when it can be read; a document counts only when required text or metadata can be extracted; an API record counts only when required fields are present.

The Model stage also now includes **Environment Repair Decisions**. If execution fails because of missing packages, incompatible versions, shell differences, unavailable binaries, hardware limits, or runtime constraints, the workflow should not simply stop. It should choose and log a repair path:

- install dependencies;
- simplify the implementation;
- use a container or managed runtime;
- change hardware or runtime;
- reduce scope;
- backtrack to Plan.

This mechanism prevents a common failure mode in AI-assisted analysis: stopping after the first execution error or silently changing the computational setup without recording why. The environment repair decision makes the response to execution failure inspectable.

The **Preliminary Finding Brief** is another key control. After the first executable result, the system must ask first whether the result is correct, then whether it is sufficient. A correct but insufficient result should trigger evidence deepening, a user decision, a claim-level downgrade, or a backtrack. A possibly incorrect result should trigger repair before interpretation.

## 6. Reporting Output Modes

Reporting is not only a review packet. It is the output-production stage for the
workflow. A manuscript, paper, slide deck, web page, dashboard, software
package, decision brief, technical appendix, or internal report is a Reporting
output mode.

For manuscript or paper outputs, Reporting builds:

- section evidence bundles;
- a major claim-evidence map;
- a citation-grounded claim map at sentence, clause, or claim level;
- citation sufficiency checks;
- targeted literature addenda for missing source support;
- manuscript architecture;
- figure/table narrative;
- section-level argument plans;
- draft body;
- citation integrity and source-support checks;
- claim strength and abstract scope checks;
- reproducible Methods checks;
- specific limitations;
- reviewer anticipation notes;
- Reporting Gate.

The central citation rule is:

> Draft from evidence bundles, not from memory.

Every substantive literature claim, method claim, gap claim, comparison claim, and model-supported claim should be tied to a verified citation, figure, table, artifact, or approved user-supplied knowledge before the manuscript or other deliverable is considered ready for Review.

The current framework also recognizes that citation strictness depends on output type. An internal note and a submission-ready journal article should not be held to the same reference-formatting standard, but they must be labeled correctly.

| Output type | Minimum citation threshold |
|---|---|
| Internal note | sources and artifacts must be traceable; informal URLs may be acceptable if unresolved items are recorded |
| Demo or proof-of-concept | core factual, data, method, and result claims need traceable sources or artifacts |
| Preliminary manuscript or preprint | cited works should be verified for existence, relevance, and source support |
| Submission-ready journal or conference manuscript | in-text citations and reference-list entries must match; metadata, DOI/URL, and sentence-level support should be verified wherever possible |

This threshold is recorded in the Reporting Package. A lower threshold can support an internal or demo output, but it must not be mislabeled as submission-ready.

## 7. Review Stage

The Review stage stress-tests the Reporting Package, reader-facing deliverables, and upstream artifacts before the output is treated as submission-ready, release-ready, or externally shareable.

Review is **adversarial, actionable, route-aware, and submission-aware**. It checks upstream completeness, scientific validity, method and reproducibility, claim strength, citation support, manuscript argument, venue fit, ethics/disclosure, responsible AI use, and likely reviewer objections.

Review findings are severity-labeled:

- **Blocker**: must be fixed before moving forward.
- **Major**: substantial revision needed.
- **Minor**: local correction or clarification.
- **Suggestion**: optional improvement.
- **Accepted limitation**: real issue that can be disclosed rather than fixed.

Each actionable finding is routed to the correct stage:

| Route | Used when |
|---|---|
| Plan | research question, scope, literature basis, feasibility, venue route |
| Model | data, code, robustness, figures, validation, reproducibility |
| Reporting | deliverable argument, structure, claim wording, citations, limitations, formatting |
| Review | severity calibration, final acceptance of limitations |
| Terminate | project is infeasible, misleading, or noncompliant |

The Review stage also checks whether claimed human or expert approval has actually occurred. AI self-review, author review, domain-owner review, and independent expert review should not be conflated.

## 8. Skill Strategy

The skill layer has three categories.

**External mature tools** are tools, services, APIs, packages, templates, databases, or checklists that already solve a standard research operation. Examples include literature-search systems, citation managers, journal templates, statistical libraries, visualization packages, systematic-review checklists, and document tools.

**Workflow-native skills** are the reusable skills maintained in the repository. Their job is not to replace external tools. Their job is to control the research workflow: clarify venue fit, distill prior work into research patterns, enforce modeling contracts, map claims to evidence, design figure/table narrative, route review findings, and manage gates.

**Project-specific skills** are narrow skills created for one domain or project. They should usually remain inside examples until reused and stable enough to promote into core skills.

The current workflow-native skills are:

| Skill | Primary stage | Responsibility |
|---|---|---|
| Venue calibration | Plan, Reporting | target venue/output requirements and exemplar patterns |
| Research-skill-card distillation | Plan | convert prior work into reusable research patterns |
| Model-contract runner | Model | execute data/model work under explicit contracts |
| Figure/table narrative | Reporting | align visuals with deliverable claims |
| Claim-evidence mapper | Reporting, Review | tie claims to citations, artifacts, or limitations |
| Route-aware reviewer | Review | stress-test and route findings |
| Gate manager | All stages | record gate decisions and transitions |

The main design principle is: **reuse mature external tools for commodity tasks; use internal skills for orchestration, verification, packaging, and routing; create project skills only when the needed operation is not already covered well enough**.

## 9. Case Study: Water-Science Manuscript Revision

The second example is a domain case study on revising AI-written water-science manuscript text toward field-appropriate academic writing. The original user goal was not full paper generation. The goal was to build a skill that can revise an AI-written draft so that wording, phrasing, and rhetorical style better match water-science journal conventions.

This case study exposed a different kind of workflow lesson. A generic "make this more academic" prompt is not enough. The useful research question became narrower: which descriptive verbs, adjectives, and phrase patterns distinguish water-science writing from general AI writing or broader non-water corpora, and how can those patterns guide revision without replacing domain content?

The workflow therefore shifted from broad text polishing to a field-calibrated skill construction process:

- collect or identify water-science and comparison corpora;
- focus analysis on writing-oriented markers rather than topic nouns;
- derive a revision skill from corpus patterns and domain judgment;
- validate revised paragraphs against field fit, overclaiming, and AI-style markers;
- keep the output as paragraph-level manuscript revision rather than full manuscript generation.

This case study is important because it shows why the framework needs both Plan-stage clarification and Reporting-stage claim/style control. The user's true research product was not "write a paper"; it was a reusable domain revision skill grounded in field writing patterns.

## 10. Prototype Architecture

A v0.1 implementation does not require a new model or a large multi-agent runtime. A simple state-machine orchestrator plus Markdown/JSON packages is enough.

Recommended prototype components:

| Layer | Practical v0.1 choice | Role |
|---|---|---|
| Orchestration | simple state machine or human-operated stage runner | manage stage order and gate transitions |
| Packages | Markdown templates | preserve inspectable handoffs |
| Retrieval | scholarly APIs, web search, local documents | support Plan, Reporting, and Review evidence |
| Data/model execution | scripts, notebooks, containers when needed | produce reproducible artifacts |
| Citation management | Zotero, BibTeX, Crossref/OpenAlex/Semantic Scholar | verify citation existence and metadata |
| Visualization | matplotlib, seaborn, ggplot2, SVG, document tools | create empirical and conceptual visuals |
| Review | route-aware review package | convert findings into stage-specific actions |

The repository currently implements the framework primarily as documentation, templates, skills, and examples rather than as a packaged software library. That is appropriate for the current stage: the main contribution is the protocol and its inspectable artifacts.

## 11. Evaluation Plan

Evaluation should test the framework's central claims rather than only final prose quality.

The most important ablations are:

1. **No gate vs. human-gated workflow**.
2. **Generic one-shot prompt vs. stage-specific packages and skills**.
3. **Candidate links counted as data vs. usable-data acquisition rule**.
4. **No claim-evidence map vs. citation-grounded claim map**.
5. **No route-aware review vs. routed review findings**.

Key metrics:

| Metric | Definition | Why it matters |
|---|---|---|
| Usable data acquisition rate | usable data items divided by target count | tests whether data acquisition is real |
| Reproducibility success | scripts/notebooks rerun from a clean environment | prevents paper-like but irreproducible outputs |
| Environment repair success | failures resolved through logged repair decisions | tests bounded persistence |
| Claim-evidence coverage | checkable claims with mapped sources/artifacts | measures grounding |
| Citation validity | cited works that exist and support attached claims | targets hallucination and misuse |
| Claim-strength alignment | claims whose wording matches evidence level | prevents overclaiming |
| Gate edit burden | edits or cycles needed to pass each stage | measures human workload |
| Backtrack precision | backtracks judged necessary divided by all backtracks | evaluates routing quality |
| Submission readiness | expert decision for external sharing/submission | pragmatic final endpoint |

Peer-review outcome may be recorded as a downstream signal, but it should not be the only validity criterion for early versions. Expert review, reproducibility, evidence grounding, and claim control are better primary metrics for v0.1.

## 12. Implementation Roadmap

The immediate release goal is no longer only a conceptual arXiv draft. It is a public GitHub repository plus an accompanying paper or technical note.

Short-term milestones:

1. Publish the repository under the name `ai-native-academic-research-workflow`.
2. Clean the README, license, citation metadata, contribution guide, quick start, and release checklist.
3. Keep the water-science manuscript-revision example as the first domain case study.
4. Add at least one framework overview figure and one stage-gate figure.
5. Polish citation metadata in this paper.
6. Add a second domain case study with executable data/model artifacts.
7. Revise the paper after external or domain-expert feedback.

Medium-term milestones:

- convert core templates into machine-readable schemas;
- add optional scripts for package validation;
- create example notebooks or scripts for common data tasks;
- add citation verification helpers;
- add a small benchmark comparing generic prompting against the staged workflow;
- collect user feedback from one or more domain researchers.

## 13. Discussion

The most important conceptual choice is to reject the idea that "more autonomy is always better" for scientific work. In research, the human is not merely a safety fallback. The human is the scientific validator, contextual completer, and accountable author.

The framework's limitations are clear. First, its novelty is architectural and procedural rather than model-level. The paper therefore needs concrete domain examples and evaluation artifacts to avoid reading as a renamed workflow. Second, human gates improve accountability but may increase workload; edit burden and active human time should be measured. Third, continuous retrieval and external tool reuse introduce source-quality problems; this is why the workflow records data-source identity, citation thresholds, and external handoff logs. Fourth, AI self-review and author review cannot substitute for independent domain expertise when a manuscript is intended for external submission.

The framework is strongest when it is modest. It does not need to claim autonomous discovery. It only needs to show that AI-assisted academic research can be made more inspectable through staged packages, explicit evidence controls, executable modeling, claim-grounded writing, and route-aware review.

## 14. Conclusion

AI-Native Academic Research Workflow is a practical protocol for evidence-grounded, human-accountable AI-assisted research. It organizes research work into Planning, Modeling, Reporting / Output Packaging, and Reviewing; separates mature external tools from workflow-native skills; records data-source identity and acquisition success; handles environment repair; maps claims to evidence; calibrates citation strictness to output type; and routes review findings to the correct stage.

The current repository demonstrates the framework through a water-science manuscript-revision case study and a set of reusable workflow specifications, templates, and skills. The next step is to publish the repository, add additional domain case studies, strengthen evaluation, and polish the accompanying paper. If successful, the contribution is not another autonomous agent. It is a research operating protocol for researchers who want AI help without losing evidence, reproducibility, or responsibility.

## References

[1] Significant Gravitas, "AutoGPT," GitHub repository. https://github.com/Significant-Gravitas/AutoGPT. Accessed: May 29, 2026.

[2] Microsoft Research, "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework." https://www.microsoft.com/en-us/research/publication/autogen-enabling-next-gen-llm-applications-via-multi-agent-conversation-framework/. Accessed: May 29, 2026.

[3] Q. Wu et al., "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation," arXiv:2308.08155, 2023. https://arxiv.org/abs/2308.08155.

[4] S. Hong et al., "MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework," arXiv:2308.00352, 2023. https://arxiv.org/abs/2308.00352.

[5] OpenAI, "Introducing deep research." https://openai.com/index/introducing-deep-research/. Accessed: May 29, 2026.

[6] OpenAI, "Deep research," OpenAI API documentation. https://platform.openai.com/docs/guides/deep-research. Accessed: May 29, 2026.

[7] Google, "Use Deep Research in Gemini Apps," Gemini Apps Help. https://support.google.com/gemini/answer/15719111. Accessed: May 29, 2026.

[8] C. Lu et al., "The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery," arXiv:2408.06292, 2024. https://arxiv.org/abs/2408.06292.

[9] Y. Yamada et al., "The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search," arXiv:2504.08066, 2025. https://arxiv.org/abs/2504.08066.

[10] S. Amershi et al., "Guidelines for Human-AI Interaction," CHI 2019. https://doi.org/10.1145/3290605.3300233.

[11] X. Wu et al., "A Survey of Human-in-the-loop for Machine Learning," arXiv:2108.00941, 2021. https://arxiv.org/abs/2108.00941.

[12] P. Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks," arXiv:2005.11401, 2020. https://arxiv.org/abs/2005.11401.

[13] M. H. Teepe et al., "AI Usage Cards: Responsibly Reporting AI-generated Content," arXiv:2303.03886, 2023. https://arxiv.org/abs/2303.03886.

[14] OpenAlex, "API Overview." https://docs.openalex.org/how-to-use-the-api/api-overview. Accessed: May 29, 2026.

[15] Crossref, "REST API." https://www.crossref.org/documentation/retrieve-metadata/rest-api/. Accessed: May 29, 2026.

[16] Semantic Scholar, "Academic Graph API." https://www.semanticscholar.org/product/api. Accessed: May 29, 2026.

[17] arXiv, "arXiv API User Manual." https://info.arxiv.org/help/api/user-manual.html. Accessed: May 29, 2026.

[18] NCBI, "APIs - Develop - NCBI." https://www.ncbi.nlm.nih.gov/home/develop/api/. Accessed: May 29, 2026.

[19] Project Jupyter, "Jupyter Documentation." https://docs.jupyter.org/. Accessed: May 29, 2026.

[20] Docker, "Docker Docs." https://docs.docker.com/. Accessed: May 29, 2026.

[21] Pandoc, "Pandoc User's Guide." https://pandoc.org/MANUAL.html. Accessed: May 29, 2026.

[22] Zotero, "Zotero Documentation." https://www.zotero.org/support/. Accessed: May 29, 2026.

[23] Elasticsearch, "Elasticsearch Guide." https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html. Accessed: May 29, 2026.

[24] pgvector, "pgvector: Open-source vector similarity search for Postgres." https://github.com/pgvector/pgvector. Accessed: May 29, 2026.

[25] Meta AI, "Faiss: A library for efficient similarity search." https://github.com/facebookresearch/faiss. Accessed: May 29, 2026.

[26] S. H. J. Kim et al., "LLM hallucinations in the wild: Large-scale evidence from non-existent citations," arXiv:2605.07723, 2026. https://arxiv.org/abs/2605.07723.

[27] T. Ifargan, L. Hafner, M. Kern, O. Alcalay, and R. Kishony, "Autonomous LLM-driven research from data to human-verifiable research papers," arXiv:2404.17605, 2024. https://arxiv.org/abs/2404.17605.

[28] A. Ashokkumar, L. Hewitt, I. Ghezae, and B. T. McInnes, "Agent Laboratory: Using LLM Agents as Research Assistants," arXiv:2501.04227, 2025. https://arxiv.org/abs/2501.04227.

[29] J. Gottweis et al., "Towards an AI co-scientist," arXiv:2502.18864, 2025. https://arxiv.org/abs/2502.18864.

[30] A. Lala et al., "PaperQA: Retrieval-Augmented Generative Agent for Scientific Research," arXiv:2312.07559, 2023. https://arxiv.org/abs/2312.07559.

[31] C. Baek et al., "ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models," arXiv:2404.07738, 2024. https://arxiv.org/abs/2404.07738.
