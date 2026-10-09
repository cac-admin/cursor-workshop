# Privacy Mode and chat context (workshop card)

Author: Shadi Khalifa, PhD \<khalifa.s@queensu.ca\>

## Privacy Mode (do this first)

1. Windows/Linux: `Ctrl+Shift+J`. macOS: `Cmd+Shift+J`.
2. Open **General**.
3. Toggle **Privacy Mode** on.
4. Confirm on Teams/Enterprise whether an admin already enforces it.

### What it means

- Your code is **not used for training** by Cursor or model providers (supported models, Privacy Mode on).
- Prompts and code context **still go to the provider** to generate answers. This is not a local-only mode.
- It does **not** authorize pasting restricted, clinical, or identifiable research data.
- Some models need admin approval for provider retention. BYOK follows the provider's terms.

More: https://cursor.com/help/security-and-privacy/privacy

## Chat context

Context = prior turns + attachments + rules + tool output + replies. It is finite.

### Do in the same chat

- One objective
- Short follow-ups
- `@` only the files you need
- Ask then Agent if the goal is unchanged

### Do not in the same chat

- Unrelated topic hopping
- Re-pasting huge logs
- Scope creep after "done"
- Mixing restricted data into a public workshop thread
- Leaving `/loop` running while starting another task

### When context is full

Older turns may drop or compact. Answers get vaguer or contradict earlier decisions; cost often stays high.

**Fix:** new chat + short handoff + `@` key files (or a `HANDOFF.md`). Put stable policy in rules/skills.
