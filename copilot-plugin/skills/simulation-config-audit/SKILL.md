---
name: simulation-config-audit
description: Audit simulation configuration changes for consistency and likely behavioral impact.
---

# Simulation Config Audit

Use this skill to identify high-impact simulation setting changes and validate them efficiently.

## Procedure

1. Diff relevant configuration files and defaults.
2. Identify semantically significant setting changes.
3. Estimate impact by subsystem and runtime stage.
4. Propose minimal validation runs to confirm impact.

## Constraints

- Avoid conflating format changes with semantic changes.
- Mark uncertain impacts explicitly.

## Inputs

- `config_diff`
- `execution_context`
- `known_baseline`

## Outputs

- `audit_summary`
- `risk_items`
- `validation_plan`

## Example

- **Prompt:** Audit simulation defaults after a dependency update.
- **Outcome:** High-impact settings and targeted verification actions.
