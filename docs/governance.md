# Governance

## Ownership

- Repository-wide ownership is defined in `CODEOWNERS`.
- Domain definitions should include `metadata.owners`.

## Stability policy

- `apiVersion` remains stable within a major version.
- Identifier changes (`metadata.id`) are treated as breaking.
- Deprecations should include a replacement note in docs.

## Release cadence

- Publish tagged releases for validated definition updates.
- Include changelog notes for new, changed, and deprecated assets.

