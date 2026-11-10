#!/usr/bin/env python3
"""Write docs/skills.md, the list of skills shown on the documentation site."""
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "skills.md"
BLOB = "https://github.com/eic/skills/blob/main"
GROUPS = {"eic": "EIC skills", "core": "Core skills"}


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def main() -> int:
    packs_of_skill = {}
    for path in sorted((ROOT / "packs").glob("*.yaml")):
        pack = load_yaml(path)
        for skill_id in pack["spec"]["skills"]:
            packs_of_skill.setdefault(skill_id, []).append(pack["metadata"]["id"])

    lines = [
        "# Available skills",
        "",
        "Each skill has a tool-agnostic definition (YAML) and a `SKILL.md` for clients that load",
        "skills from a directory. Packs bundle skills with agents; see `packs/`.",
        "",
    ]
    for group, title in GROUPS.items():
        lines += [f"## {title}", "", "| Skill | Purpose | Packs | Files |", "| --- | --- | --- | --- |"]
        for path in sorted((ROOT / "skills" / group).glob("*.yaml")):
            skill = load_yaml(path)
            skill_id = skill["metadata"]["id"]
            packs = ", ".join(packs_of_skill.get(skill_id, [])) or "–"
            files = (
                f"[YAML]({BLOB}/{path.relative_to(ROOT)}) · "
                f"[SKILL.md]({BLOB}/copilot-plugin/skills/{skill_id}/SKILL.md)"
            )
            lines.append(f"| `{skill_id}` | {skill['spec']['purpose']} | {packs} | {files} |")
        lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
