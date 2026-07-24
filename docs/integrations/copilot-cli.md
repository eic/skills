# GitHub Copilot CLI plugin integration

This repository can be installed as a Copilot CLI plugin because it now includes:

- a root `plugin.json` manifest
- plugin-compatible agent profiles in `copilot-plugin/agents/`
- plugin-compatible skills in `copilot-plugin/skills/`

## Install

Install directly from GitHub:

```bash
copilot plugin install eic/skills
```

Or install from a local clone:

```bash
git clone https://github.com/eic/skills.git
cd skills
copilot plugin install .
```

## Verify

```bash
copilot plugin list
```

Then, in an interactive Copilot CLI session, run:

- `/agent` to confirm custom agents are available
- `/skills list` to confirm plugin skills are available

The plugin manifest name is `eic-skills`.

## Layout and maintenance

- Canonical EIC definitions remain in `agents/**/*.yaml` and `skills/**/*.yaml`.
- Copilot CLI consumes the translated plugin assets in `copilot-plugin/**`.
- Keep both in sync when updating or adding agents/skills.
