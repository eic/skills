---
name: geometry-validation
description: Validate detector geometry changes and isolate geometry-specific faults.
---

# Geometry Validation

Use this skill to evaluate detector geometry updates with traceable evidence.

## Procedure

1. Record geometry version and relevant configuration inputs.
2. Run overlap and placement checks with captured logs.
3. Compare warnings and errors against baseline outputs.
4. Report suspected components and verification reruns.

## Constraints

- Keep reconstruction-side effects separate from geometry defects.
- Include command lines and log excerpts for each finding.

## Inputs

- `geometry_config`
- `validation_logs`
- `baseline_logs`

## Outputs

- `validation_report`
- `suspected_components`
- `rerun_plan`

## Example

- **Prompt:** Validate a new detector geometry commit with overlap warnings.
- **Outcome:** Prioritized defect candidates with traceable evidence.

