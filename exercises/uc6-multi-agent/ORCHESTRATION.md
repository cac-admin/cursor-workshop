# Multi-agent orchestration card

## Shared goal

Produce a reviewed SLURM script for `exercises/uc5-cac-slurm/scripts/analyze_job.py` without submitting it.

## Roles

| Agent | Mode bias | Allowed to edit? | Deliverable |
|-------|-----------|------------------|-------------|
| Explorer | Ask | No | File map + risks (10 bullets max) |
| Implementer | Plan then Agent | Yes, only under `uc5-cac-slurm/scripts/` | `job.generated.sh` |
| Reviewer | Ask | No | Checklist pass/fail against `SLURM_CHECKLIST.md` |

## Handoff rules

1. Explorer finishes before Implementer starts.
2. Implementer must list assumptions at the top of the script as comments.
3. Reviewer does not fix code; Reviewer only reports gaps.
4. Human decides whether to accept, revise, or (outside class) submit.

## Anti-patterns for class

- Three agents editing the same file at once
- Multitask with overlapping write scopes
- Looping forever on a failed mock status
