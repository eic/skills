---
name: recon-log-investigation
description: Investigate reconstruction logs to isolate regressions, failures, and pipeline bottlenecks.
---

# Reconstruction Log Investigation

Use this skill to turn large reconstruction logs into ranked, evidence-backed hypotheses.

## Procedure

1. Identify earliest anomaly signatures in logs.
2. Correlate anomalies with reconstruction stages and config context.
3. Separate deterministic failures from intermittent symptoms.
4. Produce a ranked hypothesis list with next checks.

## Constraints

- Include exact log anchors for every hypothesis.
- Keep hypotheses ranked by evidence strength.

## Inputs

- `reconstruction_logs`
- `config_snapshot`
- `baseline_logs`

## Outputs

- `anomaly_map`
- `ranked_hypotheses`
- `next_checks`

## Example

- **Prompt:** Investigate nightly log anomalies after enabling a new tracking option.
- **Outcome:** Stage-localized suspects and a focused follow-up plan.

