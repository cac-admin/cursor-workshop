# Lab conventions (workshop sample)

Use this file as grounding context during the codebase literacy exercise.

## Naming

- Prefer `snake_case` for Python modules and functions.
- Measurement tables use columns: `sample_id`, `condition`, `value`, `unit`.

## Analysis expectations

- Drop empty rows before summary statistics.
- Report `n`, mean, and note any excluded rows.
- Do not invent units. If a unit is missing, leave it blank and flag it.

## Cluster notes (CAC)

- Do not run heavy analysis on the login node.
- Prefer a short interactive allocation or a batch job for longer work.
- Keep secrets out of git and out of prompts.

## Citation habit

When Cursor cites this file, check that the claim matches the text above before you trust it.
