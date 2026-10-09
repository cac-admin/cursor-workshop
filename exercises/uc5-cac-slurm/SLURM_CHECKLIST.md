# SLURM script checklist (CAC workshop)

Before you `sbatch` (or before you call a script "done" in dry-run mode):

1. Account and partition match your allocation (placeholders replaced).
2. Time, CPUs, and memory are enough but not absurd for the task.
3. Module names exist on the target system (`module spider` / facilitator sheet).
4. Working directory is explicit (`cd "$SLURM_SUBMIT_DIR"` or absolute paths).
5. Input data path is valid on the cluster filesystem.
6. stdout and stderr go to a writable `logs/` directory.
7. No secrets in the script or in environment exports you paste into chat.
8. Heavy work stays off the login node.

Dry-run is a full success for this workshop if you cannot submit.
