# Agent context

An assistant needs facts about ePIC data that it cannot discover on its own: where the
stores are, how a dataset is named, which tool calls to make first, and what not to do on
a shared login node. Those facts are kept in one data model and rendered per site into an
`AGENTS.md`, so the file is correct for the machine the agent is on.

- Source: `tooling/agent-context/defaults.yaml` plus one `sites/<site>.yaml` per site. A
  site names only what differs; a `null` value makes the file tell the agent to find out
  instead of guessing.
- Rendered files: `docs/agents.d/<site>/` with one topic file each for scope, tools,
  data, the shared machine and policies, and the assembled `AGENTS.md`.
- Each rule is a fact, the correct call or path, an explicit "do not" and the reason. The
  files are written to the agent, not to you. Numbers that change are not in them.
- Regenerate after editing the model: `python tooling/generate-agent-context.py`. CI fails
  when the rendered files are out of date.

| site | file |
| --- | --- |
| eic-shell on your own machine | [agents.d/eic-shell/AGENTS.md](agents.d/eic-shell/AGENTS.md) |
| BNL SDCC (eicsub) | [agents.d/bnl-sdcc/AGENTS.md](agents.d/bnl-sdcc/AGENTS.md) |
| JLab ifarm | [agents.d/jlab-ifarm/AGENTS.md](agents.d/jlab-ifarm/AGENTS.md) |

## Loading it

`eic-mcp config <client>` writes the eic-shell file as `AGENTS.md` next to a project-local
client config, and for Claude Code or Gemini a `CLAUDE.md` or `GEMINI.md` that imports
it. opencode, Codex, Copilot and Cursor read `AGENTS.md` directly.

To load a site file for every project instead, once per machine:

- Claude Code: `printf '\n@/path/to/AGENTS.md\n' >> ~/.claude/CLAUDE.md`
- Codex: `ln -s /path/to/AGENTS.md ~/.codex/AGENTS.md` (Codex reads one global file; do not use `ln -sf`, it discards an existing file)
- Gemini CLI: `ln -s /path/to/AGENTS.md ~/.gemini/AGENTS.md` and add `{"context": {"fileName": ["GEMINI.md", "AGENTS.md"]}}` to `~/.gemini/settings.json`
- opencode: add `{"instructions": ["/path/to/AGENTS.md"]}` to `~/.config/opencode/opencode.json`

## The rendered files

### eic-shell on your own machine

[eic-shell](agents.d/eic-shell/AGENTS.md ':include')

### BNL SDCC (eicsub)

[bnl-sdcc](agents.d/bnl-sdcc/AGENTS.md ':include')

### JLab ifarm

[jlab-ifarm](agents.d/jlab-ifarm/AGENTS.md ':include')
