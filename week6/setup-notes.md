# Week 6 Tool Setup Notes

## Zotero MCP Setup

Installed Zotero MCP server with the course-recommended isolated tool command:

```bash
uv tool install zotero-mcp-server
```

Installed command:

```text
/home/agizz/.local/bin/zotero-mcp
```

Version check:

```bash
zotero-mcp version
```

Result:

```text
Zotero MCP v0.6.0
```

Setup info reported:

```text
Command path: /home/agizz/.local/bin/zotero-mcp
Environment: {"ZOTERO_LOCAL":"true"}
Semantic Search Database: Not configured
```

VS Code MCP config was created at:

```text
.vscode/mcp.json
```

with:

```json
{
  "servers": {
    "zotero": {
      "command": "/home/agizz/.local/bin/zotero-mcp",
      "env": {
        "ZOTERO_LOCAL": "true"
      }
    }
  }
}
```

Local Zotero API check:

```bash
timeout 5 wget -qO- http://127.0.0.1:23119/connector/ping
```

Result:

```html
<!DOCTYPE html><html><body>Zotero is running</body></html>
```

Zotero was installed through the `retorquere/zotero-deb` apt repository and
is available at:

```text
/usr/bin/zotero
```

The Zotero desktop app is running, and the local API is listening at
`127.0.0.1:23119`. The setting "Allow other applications on this computer to
communicate with Zotero" is enabled.

Write/import note: `zotero-cli add file` reports that local-only mode cannot
perform write operations without a Zotero Web API key. For this submission, the
PINN paper set was taken from the locally downloaded PDFs in
`/home/agizz/Desktop/PINN` and `/home/agizz/Downloads`, and
`week6/references.bib` was prepared from their metadata. To populate Zotero's
GUI library later, import `week6/references.bib` or drag the selected PDFs into
the Week 6 Zotero collection.

## NotebookLM Skill Setup

Installed the NotebookLM skill from GitHub:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/PleasePrompto/notebooklm-skill.git ~/.claude/skills/notebooklm
```

Initialized its local environment:

```bash
python3 scripts/run.py auth_manager.py status
```

Result:

```text
Environment ready
Virtual env: /home/agizz/.claude/skills/notebooklm/.venv
Chrome installed
Authenticated: No
```

NotebookLM authentication was completed afterward with:

```bash
cd ~/.claude/skills/notebooklm
python3 scripts/run.py auth_manager.py setup
```

Final status check:

```text
Authenticated: Yes
Last auth: 2026-06-27 18:54:20
```

The Week 6 PINN PDFs were collected for upload in:

```text
/tmp/week6-pinn-pdfs
```

The NotebookLM query response on the uploaded PINN papers was saved in
`week6/literature-notes.md`.

## Remaining Manual Steps

- Restart VS Code or reload the window so it picks up `.vscode/mcp.json`.
