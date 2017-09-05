#!/bin/bash
#SBATCH -J dms
#SBATCH --time=0-01:00
#SBATCH -o logs/slurm-%A_%a.txt 
#SBATCH --array=1-10 
module load use.own 
module load alex-rosetta 

rsync -avz input_pkg/ output_files/$SLURM_ARRAY_TASK_ID
cd $_
pwd 

python set_up_run.py 
rosetta_scripts.linuxgccrelease @flags @mut_flags
