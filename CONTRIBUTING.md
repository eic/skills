# Contributing

## Scope

Contributions should improve one or more of:
- `agents/`
- `skills/`
- `packs/`
- `docs/`
- `schemas/`

## Required checks

Before opening a pull request:

1. Run `python tooling/validate-definitions.py`.
2. Run `python tooling/generate-index.py`.
3. Commit regenerated `index.json` if content changed.

## Definition conventions

- Follow schemas in `schemas/`.
- Use clear, actionable `purpose` and `instructions`.
- Keep safety constraints explicit in `spec.constraints`.
- Add at least one usage example to each new definition.
- Keep identifiers stable once released.

## Review expectations

- Changes must be reviewed by at least one code owner.
- Breaking schema changes require a migration note in `docs/release-process.md`.
- New packs should reference existing agents/skills where possible.
