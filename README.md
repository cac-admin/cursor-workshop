# Cursor for Research Computing: From Laptop to CAC HPC

Three-hour hands-on workshop for researchers at the [Centre for Advanced Computing](https://cac.queensu.ca/), Queen's University.

Learn Cursor from first principles (Privacy Mode, chat context, Ask / Plan / Agent / Multitask, Projects, skills, `/goal`, `/loop`, tokenomics, MCP) and apply it on a laptop and on CAC's SLURM cluster via SSH.

**Author:** [Shadi Khalifa, PhD](mailto:khalifa.s@queensu.ca)  
**Org:** [cac-admin/cursor-workshop](https://github.com/cac-admin/cursor-workshop)

## Clone this repository

```bash
git clone https://github.com/cac-admin/cursor-workshop.git
cd cursor-workshop
```

Then open the folder in [Cursor](https://cursor.com/).

## Repository layout

| Path | Contents |
|------|----------|
| [`presentations/cursor-cac-workshop.html`](presentations/cursor-cac-workshop.html) | Browser slide deck (Chrome/Edge; arrow keys / Space). Hands-on prompts are on the slides. |
| [`presentations/cursor-cac-workshop.pptx`](presentations/cursor-cac-workshop.pptx) | PowerPoint deck |
| [`presentations/assets/`](presentations/assets/) | Workshop images |
| [`presentations/build_pptx.py`](presentations/build_pptx.py) | Rebuild the PPTX (`python presentations/build_pptx.py`; needs `python-pptx`) |
| [`exercises/`](exercises/) | Sample inputs for each use case |
| [`config/`](config/) | Project rules and sample skill ([`config/SETUP.md`](config/SETUP.md)) |
| [`handouts/`](handouts/) | Agenda, budget card, privacy and context card |
| [`FACILITATOR_GUIDE.md`](FACILITATOR_GUIDE.md) | Timing and demo notes for the instructor |

## Use cases (3 hours)

| ID | Use case | Materials |
|----|----------|-----------|
| UC0 | Foundations: Privacy Mode, chat context, modes, Projects, and tokenomics | [`handouts/privacy-and-context.md`](handouts/privacy-and-context.md), [`handouts/budget-card.md`](handouts/budget-card.md) |
| UC1 | Codebase literacy and documentation grounding | [`exercises/uc1-codebase-literacy`](exercises/uc1-codebase-literacy) |
| UC2 | Local analysis pipeline | [`exercises/uc2-analysis`](exercises/uc2-analysis) |
| UC3 | Skills, `/goal`, and `/loop` | [`exercises/uc3-skills-directives`](exercises/uc3-skills-directives), [`config/.cursor`](config/.cursor) |
| UC4 | Paper method replication | [`exercises/uc4-paper-replication`](exercises/uc4-paper-replication) |
| UC5 | CAC remote work, SLURM jobs, and debugging | [`exercises/uc5-cac-slurm`](exercises/uc5-cac-slurm) |
| UC6 | Multi-agent orchestration | [`exercises/uc6-multi-agent`](exercises/uc6-multi-agent) |
| UC7 | GitHub MCP demo | [`exercises/uc7-github-mcp`](exercises/uc7-github-mcp) |

Agenda: [`handouts/agenda-3h.md`](handouts/agenda-3h.md).

## Quick start for students

1. Install [Cursor](https://cursor.com/) and open this repository as a project.
2. Turn on **Privacy Mode**: `Ctrl+Shift+J` (Windows/Linux) or `Cmd+Shift+J` (macOS) → **General**.
3. Copy workshop Cursor config into the repo root (see [`config/SETUP.md`](config/SETUP.md)).
4. Open [`presentations/cursor-cac-workshop.html`](presentations/cursor-cac-workshop.html) or the `.pptx` and follow the hands-on prompt slides.
5. Keep [`handouts/agenda-3h.md`](handouts/agenda-3h.md) and [`handouts/budget-card.md`](handouts/budget-card.md) nearby.

Dry-run SLURM review counts as success if you cannot `sbatch` today. Workshop exercises use synthetic or public sample data only; do not paste restricted or clinical data into cloud models.

## Prerequisites

- Cursor installed on your laptop
- Comfortable with basic Python or shell for the exercises that run locally
- Optional: CAC account and SSH access for UC5 remote / live `sbatch` (dry-run otherwise)
- Optional: GitHub MCP connected for UC7 (instructor demo; read-first, draft-then-approve writes)

## Rebuilding the PowerPoint

```bash
pip install python-pptx pillow
python presentations/build_pptx.py
```

## License and branding

Training materials for CAC / Queen's University. Queen's tricolour: Blue `#002452`, Gold `#fabd0f`, Red `#b90e31`.

For questions about this workshop, contact Shadi Khalifa, PhD: [khalifa.s@queensu.ca](mailto:khalifa.s@queensu.ca).
