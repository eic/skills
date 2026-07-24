# Cursor integration

## Recommended flow

1. Clone this repository adjacent to your project checkout.
2. Reference selected definitions while creating project rules and prompts.
3. Store tool-specific adaptations in your project-level Cursor config.

## Mapping guidance

- Agent `spec.instructions` -> Cursor project rules/instructions.
- Skill `spec.procedure` -> reusable operational checklist.
- Prompt templates -> `/prompts` snippets used in chats or command-k prompts.

## Team practice

- Link to exact file paths from `eic/skills` in your project docs.
- Pin to a release tag when reproducibility matters.

