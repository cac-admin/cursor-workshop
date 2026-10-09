#!/bin/bash
#SBATCH --job-name=workshop-broken
#SBATCH --output=logs/slurm-%j.out
#SBATCH --error=logs/slurm-%j.err
#SBATCH --time=00:05:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
# Intentionally incomplete for the debugging exercise:
# - missing account/partition placeholders discussion
# - wrong module name
# - wrong working directory assumption

module load python/999.0.0

# Bug: runs from submit dir assumptions without cd
python scripts/analyze_job.py
