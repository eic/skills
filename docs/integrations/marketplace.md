# Plugin marketplace

The `eic/skills` repository is published to the agent/skill plugin marketplace and
is discoverable via [GitHub Agent Finder](https://agentfinder.github.com).

## Marketplace manifests

The repository includes platform-specific marketplace manifests so AI coding
tools can discover and install the EIC skills plugin:

| File | Platform |
|------|----------|
| `.cursor-plugin/marketplace.json` | Cursor |
| `.cursor-plugin/plugin.json` | Cursor |
| `.claude-plugin/marketplace.json` | Claude Code |
| `.claude-plugin/plugin.json` | Claude Code |
| `.codex-plugin/marketplace.json` | OpenAI Codex |
| `.codex-plugin/plugin.json` | OpenAI Codex |
| `plugin.json` | GitHub Copilot CLI |

## Install from the marketplace

### Cursor

```bash
cursor plugin install eic/skills
```

### Claude Code

```bash
claude plugin install eic/skills
```

### Codex / OpenAI

```bash
codex plugin install eic/skills
```

### GitHub Copilot CLI

```bash
copilot plugin install eic/skills
```

## Discovery

Once the repository is listed in the marketplace index, users can find it via:

```
https://agentfinder.github.com
```

Search for "EIC", "particle physics", "simulation", or "reconstruction" to find
the `eic-skills` plugin.

## Updating the marketplace listing

1. Update version fields in `plugin.json`, `.cursor-plugin/plugin.json`,
   `.claude-plugin/plugin.json`, and `.codex-plugin/plugin.json`.
2. Tag a new release (`vX.Y.Z`) on GitHub — the marketplace index picks up
   the new version from the release tag.
