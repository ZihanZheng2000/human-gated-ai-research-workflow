# Run Log

## 2026-06-27

1. Read current workflow instructions from `AGENTS.md`, `docs/stage-handoffs.md`,
   `docs/quickstart.md`, and `templates/smoke-test-package.md`.
2. Created example structure under `examples/smoke-test-four-stage-flow/`.
3. Wrote `analyze_workflow_docs.py` to scan active Markdown files.
4. First run scanned only one file because the repository root was calculated
   incorrectly.
5. Fixed root calculation from `parents[4]` to `parents[5]`.
6. Second run scanned 33 Markdown files.
7. Found `demo_gate = 0`.
8. Found `writing_stage = 3`; two were explanatory references, one was legacy
   migration wording.
9. Reworded the two explanatory references to Reporting output-mode language.
10. Reworded Quickstart's Planning-only reviewer standard to all stage gates.
11. Final scan found `demo_gate = 0` and `writing_stage = 1`, with the remaining
    item limited to legacy migration guidance.

