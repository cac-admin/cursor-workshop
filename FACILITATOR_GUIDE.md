# Facilitator guide

Cursor for Research Computing (3 hours)  
Centre for Advanced Computing, Queen's University

**Author / contact:** Shadi Khalifa, PhD \<khalifa.s@queensu.ca\>

The student decks (`presentations/cursor-cac-workshop.html` and `.pptx`) speak directly to learners. Hands-on prompts are on the slides. This file is for the instructor only.

## Before class

1. Confirm Cursor version used in the room and that Remote SSH works for at least the demo account.
2. Copy `config/.cursor` into the workshop root (see `config/SETUP.md`).
3. Open `presentations/cursor-cac-workshop.html` once on the projector machine (fonts load from Google; offline fallback uses system fonts).
4. Keep `presentations/cursor-cac-workshop.pptx` as backup.
5. For UC7 GitHub MCP demo, authenticate GitHub MCP with minimal scopes against a public demo repo. Draft-then-approve only for writes.
6. Print or share `handouts/budget-card.md`, `handouts/privacy-and-context.md`, and `handouts/agenda-3h.md`.
7. Decide live `sbatch` vs dry-run. Dry-run is the default success path.
8. Live demo Privacy Mode toggle at minute zero; ask everyone to verify before UC1 Codebase literacy.

## Timing

See `handouts/agenda-3h.md`. If you slip:

- Shorten UC4 Paper method replication verification to Ask-only line-by-line check.
- Make UC6 Multi-agent orchestration a led trio of chats instead of everyone running three agents.
- Keep UC7 GitHub MCP demo as a 10-minute walkthrough.

## Use case notes

### UC0 Foundations: Privacy Mode, chat context, modes, Projects, and tokenomics

Start with Privacy Mode. Cover chat context before modes. Walk Ask → Plan → Agent on `exercises/uc1-codebase-literacy` using the prompt slides. Stress included vs on-demand usage. For `/loop`, edit `STATUS.mock.txt` to `DONE` after a tick or two.

### UC1 Codebase literacy and documentation grounding

Students should catch at least one shaky claim. Celebrate the catch.

### UC2 Local analysis pipeline

If pandas is missing, have Agent stick to csv + matplotlib or pure stdlib. Running the script matters more than the library.

### UC3 Skills, /goal, and /loop

Confirm skills/rules are copied. Cap loops. Teach stopping on purpose.

### UC4 Paper method replication

`PAPER_BRIEF.md` is the paper stand-in. Honest incompleteness beats fake fidelity.

### UC5 CAC remote work, SLURM jobs, and debugging

If SSH fails for half the room, stay local with the broken logs. Module names in templates are examples.

### UC6 Multi-agent orchestration

Enforce write scopes. Reviewer Ask-only. Human gate before anyone talks about `sbatch`.

### UC7 GitHub MCP demo

Read first. Draft comment second. Post only if you say "post it" out loud.

## File map

| Need | Path |
|------|------|
| Student prompts | In the HTML/PPTX slides (not a separate `prompts/` folder) |
| Rules / skill | `config/.cursor/` |
| Broken job + logs | `exercises/uc5-cac-slurm/` |
| Orchestration card | `exercises/uc6-multi-agent/ORCHESTRATION.md` |
| Rebuild PPTX | `python presentations/build_pptx.py` |

## Responsible use script (2 minutes)

- Synthetic or public data in class.
- No restricted or clinical pastes into cloud models.
- Students still own the science; Cursor drafts, they verify.
- Cluster policy still applies when an agent suggests a command.
