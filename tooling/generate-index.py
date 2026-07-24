#!/usr/bin/env python3
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "index.json"
SEARCH = [ROOT / "agents", ROOT / "skills", ROOT / "packs"]


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def main() -> int:
    rows = []
    for base in SEARCH:
        for p in sorted(base.rglob("*.yaml")):
            content = load_yaml(p)
            meta = content.get("metadata", {})
            rows.append(
                {
                    "kind": content.get("kind"),
                    "id": meta.get("id"),
                    "name": meta.get("name"),
                    "version": meta.get("version"),
                    "path": str(p.relative_to(ROOT)),
                }
            )
    rows.sort(key=lambda r: (r["kind"] or "", r["id"] or ""))
    payload = {"items": rows}
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT} with {len(rows)} items.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

