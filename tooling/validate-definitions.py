#!/usr/bin/env python3
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parent.parent
SCHEMAS = ROOT / "schemas"
KIND_TO_SCHEMA = {
    "Agent": SCHEMAS / "agent.schema.json",
    "Skill": SCHEMAS / "skill.schema.json",
    "Pack": SCHEMAS / "pack.schema.json",
}
SEARCH_DIRS = [ROOT / "agents", ROOT / "skills", ROOT / "packs"]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def iter_definition_files():
    for base in SEARCH_DIRS:
        for p in sorted(base.rglob("*.yaml")):
            yield p


def main() -> int:
    validators = {
        kind: Draft202012Validator(load_json(schema_path))
        for kind, schema_path in KIND_TO_SCHEMA.items()
    }
    failures = []
    for definition_file in iter_definition_files():
        content = load_yaml(definition_file)
        kind = content.get("kind")
        validator = validators.get(kind)
        if validator is None:
            failures.append(f"{definition_file}: unsupported or missing kind '{kind}'")
            continue
        errors = sorted(validator.iter_errors(content), key=lambda e: e.path)
        for error in errors:
            path = ".".join([str(seg) for seg in error.path]) or "<root>"
            failures.append(f"{definition_file}: {path}: {error.message}")
    if failures:
        print("Validation failed:")
        for failure in failures:
            print(f" - {failure}")
        return 1
    print("All definitions validate.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

