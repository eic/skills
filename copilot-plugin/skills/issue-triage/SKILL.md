---
name: issue-triage
description: Triage incoming issues into reproducible bug reports or actionable enhancement requests.
---

# Issue Triage

Use this skill to structure incoming reports into clear, actionable follow-up.

## Procedure

1. Confirm scope, expected behavior, and observed behavior.
2. Gather reproduction details and environment metadata.
3. Classify severity and likely ownership area.
4. Produce a concise next-action checklist.

## Constraints

- Do not classify as fixed without reproduction evidence.
- Separate symptom statements from root-cause hypotheses.

## Inputs

- `issue_text`
- `logs`
- `environment`

## Outputs

- `triage_summary`
- `severity`
- `owner_suggestion`
- `next_steps`

## Example

- **Prompt:** Triage a crash report with incomplete logs from a nightly build.
- **Outcome:** A clear follow-up request and provisional ownership path.

