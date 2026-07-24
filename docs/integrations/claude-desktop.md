# Claude Desktop integration

## Recommended flow

1. Keep this repository cloned locally.
2. Select a pack from `packs/`.
3. Translate selected `agents/` and `skills/` entries into your Claude Desktop project instructions.
4. Re-sync when repository definitions update.

## Mapping guidance

- `metadata.name` -> profile name
- `spec.purpose` -> role summary
- `spec.instructions` -> main behavior block
- `spec.constraints` -> explicit "must/must not" rules
- `spec.examples` -> starter prompts

## Update workflow

```bash
cd skills
git pull --ff-only
python tooling/validate-definitions.py
```

