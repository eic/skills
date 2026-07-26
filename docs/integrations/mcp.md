# MCP auto-configuration (Cursor, Codex, and Copilot)

This repository includes project-level MCP configuration files that compatible clients can load automatically:

- Cursor: `.cursor/mcp.json`
- Codex: `.codex/config.toml`
- GitHub Copilot in VS Code: `.vscode/mcp.json`

## Default MCP servers

- `github` → `https://api.githubcopilot.com/mcp/`
- `uproot` → `ghcr.io/eic/uproot-mcp-server:latest`
- `zenodo` → `ghcr.io/eic/zenodo-mcp-server:latest`
- `xrootd` → `ghcr.io/eic/xrootd-mcp-server:latest`

The default `xrootd` server configuration sets:

```
XROOTD_SERVER=root://dtn-eic.jlab.org
XROOTD_BASE_DIR=/volatile/eic/EPIC
```

## Recommended runtime strategy

Use Docker images from GHCR for `uproot`, `zenodo`, and `xrootd`.

This is the most reliable default because it:

- avoids local Python/Node/XRootD dependency drift
- provides consistent startup behavior across Cursor, Codex, and Copilot
- aligns with the upstream server repositories, which provide container builds

## Prerequisites

Install Docker and pre-pull images:

```bash
docker --version
docker pull ghcr.io/eic/uproot-mcp-server:latest
docker pull ghcr.io/eic/zenodo-mcp-server:latest
docker pull ghcr.io/eic/xrootd-mcp-server:latest
```

## How this is used

1. Clone `eic/skills`.
2. Ensure Docker is running.
3. Open the repository in Cursor, Codex, or VS Code with Copilot.
4. Approve/sign in when the client prompts for MCP access.

## Notes

- Keep credentials out of committed config; use each client's secure auth flow.
- If your team needs additional MCP servers, add them to all three files so clients stay aligned.
- If Docker is unavailable, install each server locally and replace the `docker run` command entries in the client config with local executable paths:
  - <https://github.com/eic/uproot-mcp-server>
  - <https://github.com/eic/zenodo-mcp-server>
  - <https://github.com/eic/xrootd-mcp-server>
