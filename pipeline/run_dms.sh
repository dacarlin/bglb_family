#!/bin/bash
#SBATCH -J dms 
#SBATCH -o logs/log_%A_%a.txt
#SBATCH --array=1-2888
#SBATCH -t 0-06:00
#SBATCH -p gc128 
module load use.own
module load alex-rosetta 

# set up project
OUT_DIR=output_files/$SLURM_ARRAY_TASK_ID
rsync -avz deep_mutational_scan/ $OUT_DIR
cd $_
pwd
hostname -f 
env 

python protocol.py 
