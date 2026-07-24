---
name: release-notes
description: Produce clear release notes grouped by user impact and migration requirements.
---

# Release Notes

Use this skill to generate concise, user-focused, migration-aware release notes.

## Procedure

1. Collect merged changes and related issues.
2. Group by added, changed, fixed, and deprecated behavior.
3. Highlight migration steps and operational risks.
4. Produce concise summaries for both users and maintainers.

## Constraints

- Do not omit known breaking changes.
- Keep wording consistent with repository terminology.

## Inputs

- `merged_prs`
- `issues`
- `changelog_context`

## Outputs

- `release_notes`
- `migration_notes`

## Example

- **Prompt:** Draft release notes for a monthly update with one breaking config change.
- **Outcome:** Categorized notes with explicit migration actions.

