# Available skills

Each skill has a tool-agnostic definition (YAML) and a `SKILL.md` for clients that load skills
from a directory. Packs bundle skills with agents; see `packs/`.

## EIC skills

| Skill | Purpose | Packs | Files |
| --- | --- | --- | --- |
| `geometry-validation` | Validate detector geometry changes and isolate geometry-specific faults. | simulation-pack | [YAML](https://github.com/eic/skills/blob/main/skills/eic/geometry-validation.yaml) · [SKILL.md](https://github.com/eic/skills/blob/main/copilot-plugin/skills/geometry-validation/SKILL.md) |
| `lambda-fit` | Reconstruct and fit the Lambda0 -> p pi- invariant-mass peak in ePIC EDM4eic data through the EIC MCP servers. Worked example from the [MCP tutorial](https://eic.github.io/tutorial-mcp/). | – | [YAML](https://github.com/eic/skills/blob/main/skills/eic/lambda-fit.yaml) · [SKILL.md](https://github.com/eic/skills/blob/main/copilot-plugin/skills/lambda-fit/SKILL.md) |
| `plotting-and-qa` | Produce reproducible analysis plots and accompanying quality assurance checks. | analysis-pack | [YAML](https://github.com/eic/skills/blob/main/skills/eic/plotting-and-qa.yaml) · [SKILL.md](https://github.com/eic/skills/blob/main/copilot-plugin/skills/plotting-and-qa/SKILL.md) |
| `recon-log-investigation` | Investigate reconstruction logs to isolate regressions, failures, and pipeline bottlenecks. | reconstruction-pack | [YAML](https://github.com/eic/skills/blob/main/skills/eic/recon-log-investigation.yaml) · [SKILL.md](https://github.com/eic/skills/blob/main/copilot-plugin/skills/recon-log-investigation/SKILL.md) |
| `simulation-config-audit` | Audit simulation configuration changes for consistency and likely behavioral impact. | simulation-pack | [YAML](https://github.com/eic/skills/blob/main/skills/eic/simulation-config-audit.yaml) · [SKILL.md](https://github.com/eic/skills/blob/main/copilot-plugin/skills/simulation-config-audit/SKILL.md) |

## Core skills

| Skill | Purpose | Packs | Files |
| --- | --- | --- | --- |
| `issue-triage` | Triage incoming issues into reproducible bug reports or actionable enhancement requests. | onboarding-pack | [YAML](https://github.com/eic/skills/blob/main/skills/core/issue-triage.yaml) · [SKILL.md](https://github.com/eic/skills/blob/main/copilot-plugin/skills/issue-triage/SKILL.md) |
| `pr-review` | Review pull requests for correctness, risk, and maintainability with actionable comments. | analysis-pack, onboarding-pack | [YAML](https://github.com/eic/skills/blob/main/skills/core/pr-review.yaml) · [SKILL.md](https://github.com/eic/skills/blob/main/copilot-plugin/skills/pr-review/SKILL.md) |
| `release-notes` | Produce clear release notes grouped by user impact and migration requirements. | reconstruction-pack | [YAML](https://github.com/eic/skills/blob/main/skills/core/release-notes.yaml) · [SKILL.md](https://github.com/eic/skills/blob/main/copilot-plugin/skills/release-notes/SKILL.md) |
