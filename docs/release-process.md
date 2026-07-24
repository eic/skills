# Release process

## Versioning

- Use semantic versioning for repository releases.
- Update definition `metadata.version` when behavior changes.

## Release steps

1. Ensure CI is green.
2. Regenerate `index.json`.
3. Summarize changes by category:
   - Added
   - Changed
   - Deprecated
4. Create a Git tag and GitHub release notes.

## Breaking changes

- Document migration guidance in this file.
- Keep deprecated definitions for at least one release cycle when possible.

