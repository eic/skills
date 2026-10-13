# EIC data tools (MCP servers)

An agentic assistant such as opencode, Claude Code, Copilot, Codex or Gemini CLI can read files,
run code and call tools. EIC provides tools for it through the
[Model Context Protocol (MCP)](https://modelcontextprotocol.io), so the same servers work with
any assistant. The [AI and MCP tutorial](https://eic.github.io/tutorial-mcp) walks through a full
analysis; this page is the reference.

## The servers

All of them are installed in eic-shell.

| server | tools for | repository |
| --- | --- | --- |
| uproot | reading ROOT and EDM4eic files, histograms, kernels over a dataset | [eic/uproot-mcp-server](https://github.com/eic/uproot-mcp-server) |
| xrootd | browsing and reading the ePIC data stores | [eic/xrootd-mcp-server](https://github.com/eic/xrootd-mcp-server) |
| rucio | finding datasets and files in the data catalogue (read-only) | [eic/rucio-eic-mcp-server](https://github.com/eic/rucio-eic-mcp-server) |
| zenodo | searching Zenodo records, including ePIC documents | [eic/zenodo-mcp-server](https://github.com/eic/zenodo-mcp-server) |

The source cross-reference [LXR](https://eic-code-browser.sdcc.bnl.gov/lxr/source) is also
available as an MCP server on the BNL-hosted services.

## Set up your assistant

Inside eic-shell, in the directory of your analysis:

```bash
eic-mcp config claude      # or opencode, copilot, vscode, cursor, gemini, codex
```

This writes the configuration file your assistant reads, and an `AGENTS.md` with the facts an
assistant needs about EIC data if the directory has none (see [Agent context](agent-context.md)). Start the assistant in that directory,
inside eic-shell or on the host.

On your own computer the servers run as local HTTP services. On a shared machine such as a login
node the assistant starts them itself over stdio, as you, and they exit with it, so nothing is
left running and nothing is reachable by other users. The
[eic-mcp README](https://github.com/eic/eic-mcp) has the details, including macOS and remote
clients.

Without eic-shell, the servers also run as Docker images; see [MCP auto-configuration](integrations/mcp.md).

## Without any setup

The **DISpatcher** bot in Mattermost
([chat.epic-eic.org → dispatcher](https://chat.epic-eic.org/main/channels/dispatcher)) has the
same data tools plus tools for production, physics samples, software and documents. The search
box on [eic.github.io](https://eic.github.io) answers questions about EIC documentation.

## Rules

- **Login nodes are shared.** The assistant itself is lightweight, but an analysis over a large
  dataset is not: run it through the batch system, not on the login node.
- **Never put credentials in a prompt or a file the assistant reads.** The servers use the
  shared read-only `eicread` account; your grid certificate is not needed.
- **A number that did not come from a tool is not a result.** Ask the assistant to show which
  tool call produced each value, and keep the kernel or script it ran.
- **Do not download datasets.** Read `root://` files in place.
- **Review before you commit.** You are responsible for what the assistant writes and runs.
