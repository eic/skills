# Compatibility matrix

| Capability | Copilot CLI (plugin) | Claude Desktop | Cursor | VS Code |
|---|---|---|---|---|
| Use prompt templates | Yes | Yes | Yes | Yes |
| Reuse agent YAML directly | Partial (translated into `*.agent.md` in `copilot-plugin/agents/`) | Partial (via manual translation) | Partial (rules/profile mapping) | Partial (instructions/prompts mapping) |
| Reuse skill YAML directly | Partial (translated into `SKILL.md` in `copilot-plugin/skills/`) | Partial | Partial | Partial |
| Pack-level workflow guidance | Yes | Yes | Yes | Yes |
| Automated schema validation in repo CI | Yes | Yes | Yes | Yes |

## Notes

- Definitions in this repo are canonical; desktop tools may require a translation step into tool-native formats.
- Integration guides document recommended mapping patterns.
