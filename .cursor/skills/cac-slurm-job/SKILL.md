---
name: cac-slurm-job
description: Draft or repair a CAC SLURM batch script from a Python entrypoint. Use when the user asks for sbatch, SLURM, job scripts, or cluster submission help.
---

# CAC SLURM job skill

## Goal

Produce a batch script a researcher can review before `sbatch`, plus a short verification checklist.

## Inputs to gather

1. Entrypoint command (for example `python scripts/analyze_job.py`)
2. Estimated walltime, CPUs, memory
3. Whether this is dry-run only
4. Data path on the cluster

## Steps

1. Read any existing `job*.sh` and `SLURM_CHECKLIST.md` in the workspace.
2. Draft or update a script with:
   - `#SBATCH` job name, time, cpus, mem, output, error
   - `#SBATCH --account=YOUR_ACCOUNT` and `--partition=YOUR_PARTITION` unless the user supplied real values
   - `set -euo pipefail`
   - `module load` with a clearly labeled example module, or the user-provided module
   - `cd "${SLURM_SUBMIT_DIR}"`
   - the entrypoint command
3. List assumptions and open questions (account, partition, module version, data path).
4. Remind the user: validate modules on CAC; do not run the workload on the login node.

## Output format

1. The script in a fenced code block or written to `scripts/job.generated.sh`
2. A 5-bullet "verify before submit" list
3. Dry-run note if the user cannot submit today
