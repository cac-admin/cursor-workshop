# Cursor configuration setup

Author: Shadi Khalifa, PhD \<khalifa.s@queensu.ca\>  
From the workshop root (`Cursor AI/`):

## Project rules and skills (recommended for class)

Copy the bundled config into a `.cursor` folder at the workshop root:

```powershell
Copy-Item -Recurse -Force config\.cursor .cursor
```

On macOS/Linux:

```bash
cp -R config/.cursor .cursor
```

This installs:

- `.cursor/rules/cac-research.mdc`
- `.cursor/skills/cac-slurm-job/SKILL.md`

## Personal skill (optional)

To reuse the SLURM skill across all projects, copy `config/.cursor/skills/cac-slurm-job` into your user Agent Store skills directory (Cursor Settings → skills / Agent Store path on your machine).

## SSH to CAC

1. Install the Remote SSH capability in Cursor.
2. Use your CAC login host from CAC documentation or facilitator notes.
3. Open a remote folder under your `$HOME` or project space.
4. Copy workshop exercise folders you need; do not run heavy jobs on the login node.

## GitHub MCP (facilitator)

1. Enable the GitHub MCP integration available in your Cursor build.
2. Authenticate with the minimum scopes for the demo.
3. Use a public demo repository when possible.
