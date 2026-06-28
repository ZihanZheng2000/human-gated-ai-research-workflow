# Open Questions

## Plan Stage

- How many papers are enough for the initial skill-card distillation?
- Should skill cards be generated per paper, per cluster of papers, or per method pattern?
- How strict should the human gate be before Model begins?
- Should the Plan stage always produce multiple candidate plans, or only when the user's intent is vague?
- What is the smallest useful manuscript package for each target domain?
- How often should Plan recommend venues versus simply asking the user for a target?
- What minimum venue guidance is enough before Model begins, and what can safely wait until Writing?

## Evaluation

- How should manuscript usefulness be scored?
- Should non-CS users compare this workflow against ordinary ChatGPT, Deep Research, or a human-only baseline?
- What is the right balance between speed and rigor?

## Model Stage

- What default iteration budget should be used for repair and optimization loops?
- Should every Model run require a fresh-session rerun before Writing begins?
- How should the system distinguish legitimate robustness checks from specification searching?
- What level of containerization is necessary for non-CS usability?
- When should weak or null results be passed to Writing rather than optimized further?
- What should be the boundary between Discussion writing and Model addendum runs for additional empirical figures or robustness checks?

## Writing Stage

- How can Writing avoid producing a short report-like summary rather than a real manuscript argument?
- What minimum discussion-support artifacts should Writing require before drafting the Discussion section?
- Should Writing always create a manuscript architecture before drafting, or only when the source material is complex?
- What is the right depth for the Discussion in a compact manuscript package?
- How should the system detect when Related Work is becoming a list of summaries rather than positioning?
- Should target-venue calibration happen at Plan, Writing, or both? Current direction: ask provisionally in Plan, retrieve detailed author instructions in Writing if a venue is selected.
- How should the workflow handle venue requirements that conflict with the best argument structure?

## Review Stage

- How many reviewer roles are necessary for a lightweight v1?
- Should adversarial review be independent from the writing reviewer?
- What severity thresholds should block submission or external sharing?
- How should accepted limitations be distinguished from unresolved major problems?
- Should Review rerun code, or only inspect the Model Package unless a reproducibility concern is found?
