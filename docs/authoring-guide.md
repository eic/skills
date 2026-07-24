# Authoring guide

## File format

- Definitions are YAML.
- Every definition must validate against its schema.

## Common fields

- `apiVersion`
- `kind`
- `metadata` (`id`, `name`, `version`, `owners`, `tags`)
- `spec` (`purpose`, `instructions`, `constraints`, `inputs`, `examples`)

## Writing effective instructions

- Prefer concrete task boundaries.
- Make required evidence explicit (for example, logs, file paths, or commands used).
- Keep constraints testable and unambiguous.

## Example lifecycle

1. Copy a similar definition.
2. Update metadata and purpose.
3. Add at least one realistic example.
4. Validate locally.
5. Open pull request.

