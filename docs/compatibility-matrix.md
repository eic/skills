# Compatibility matrix

| Capability | Copilot CLI (plugin) | Claude Desktop | Cursor | Codex | VS Code |
|---|---|---|---|---|---|
| Use prompt templates | Yes | Yes | Yes | Yes | Yes |
| Project-level MCP auto-configuration in repo | No | No | Yes (`.cursor/mcp.json`) | Yes (`.codex/config.toml`) | Yes (`.vscode/mcp.json`) |
| Reuse agent YAML directly | Partial (translated into `*.agent.md` in `copilot-plugin/agents/`) | Partial (via manual translation) | Partial (rules/profile mapping) | Partial (project instruction mapping) | Partial (instructions/prompts mapping) |
| Reuse skill YAML directly | Partial (translated into `SKILL.md` in `copilot-plugin/skills/`) | Partial | Partial | Partial | Partial |
| Pack-level workflow guidance | Yes | Yes | Yes | Yes | Yes |
| Automated schema validation in repo CI | Yes | Yes | Yes | Yes | Yes |

## Notes

- Definitions in this repo are canonical; desktop tools may require a translation step into tool-native formats.
- Integration guides document recommended mapping patterns.
