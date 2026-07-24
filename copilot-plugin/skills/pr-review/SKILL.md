---
name: pr-review
description: Review pull requests for correctness, risk, and maintainability with actionable comments.
---

# Pull Request Review

Use this skill to produce high-confidence, impact-oriented code review findings.

## Procedure

1. Identify change intent and touched subsystems.
2. Inspect high-risk paths first, then broader consistency.
3. Validate compatibility impacts and migration needs.
4. Summarize blocking findings and optional follow-ups.

## Constraints

- Prioritize high-confidence findings over style preferences.
- Tie each finding to a specific file location and impact.

## Inputs

- `pr_diff`
- `related_issue`
- `test_results`

## Outputs

- `review_summary`
- `blocking_findings`
- `follow_ups`

## Example

- **Prompt:** Review a reconstruction refactor with mixed logic and configuration changes.
- **Outcome:** Focused risk findings and concrete remediation suggestions.

