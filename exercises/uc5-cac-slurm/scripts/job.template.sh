#!/bin/bash
#SBATCH --job-name=workshop-analyze
#SBATCH --output=logs/slurm-%j.out
#SBATCH --error=logs/slurm-%j.err
#SBATCH --time=00:10:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
# Replace these with values from your CAC allocation / facilitator notes:
#SBATCH --account=YOUR_ACCOUNT
#SBATCH --partition=YOUR_PARTITION

set -euo pipefail

# Load the Python module available on your CAC system (example name only):
module load python/3.11.5

# Always work from the directory you intend
cd "${SLURM_SUBMIT_DIR}"

mkdir -p logs
export WORKSHOP_DATA="${SLURM_SUBMIT_DIR}/../uc2-analysis/data/measurements.csv"

python scripts/analyze_job.py
