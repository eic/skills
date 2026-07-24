---
name: plotting-and-qa
description: Produce reproducible analysis plots and accompanying quality assurance checks.
---

# Plotting and QA

Use this skill for deterministic plotting workflows with explicit QA checks.

## Procedure

1. Define required inputs, selection criteria, and expected outputs.
2. Build plot generation steps with explicit parameters.
3. Run QA checks on binning, normalization, and uncertainties.
4. Summarize interpretation caveats and next actions.

## Constraints

- Preserve reproducibility through explicit commands and versions.
- Separate plotting defects from underlying data-quality issues.

## Inputs

- `analysis_code`
- `dataset_metadata`
- `figure_requirements`

## Outputs

- `plotting_steps`
- `qa_results`
- `interpretation_notes`

## Example

- **Prompt:** Recreate a figure for internal review and provide QA notes.
- **Outcome:** Deterministic plotting instructions and a QA summary.

