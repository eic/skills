# EIC Skills

`eic/skills` is a shared repository of AI-ready agent and skill definitions for the EIC community.

It provides:
- Reusable, tool-agnostic definitions for agents, skills, and packs.
- Integration instructions for Claude Desktop, Cursor, and VS Code.
- Validation tooling and CI checks so contributed content stays consistent.

## Quick start

1. Clone this repository.
2. Read `docs/quickstart.md`.
3. Pick a pack from `packs/` and copy the referenced agents/skills into your local AI tool configuration workflow.

## Repository layout

- `agents/`: reusable assistant definitions.
- `skills/`: reusable task or workflow skills.
- `packs/`: curated bundles of agents and skills.
- `schemas/`: JSON Schema definitions for validation.
- `docs/`: usage guides, governance, and integration docs.
- `prompts/templates/`: reusable prompt templates.
- `tooling/`: validation and index generation scripts.

## Supported desktop tools (v1)

- Claude Desktop
- Cursor
- VS Code

See `docs/compatibility-matrix.md` and `docs/integrations/`.

## Documentation site

Repository docs are published to GitHub Pages with Docsify from `docs/`.
After GitHub Pages is enabled for the repository, the site URL is:
`https://eic.github.io/skills/`.
