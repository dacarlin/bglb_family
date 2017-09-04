#!/bin/bash 
#SBATCH --time 0-12:00
#SBATCH -J dms 
#SBATCH -o logs/slurm_%A-%a.txt 
#SBATCH --array=1-10 

module load use.own 
module load alex-rosetta 

rsync -avz input_pkg/ output_files/$SLURM_ARRAY_TASK_ID
cd $_
pwd 

awk "NR==$SLURM_ARRAY_TASK_ID" list.txt > mut_flags 
rosetta_scripts.linuxgccrelease @flags @mut_flags
