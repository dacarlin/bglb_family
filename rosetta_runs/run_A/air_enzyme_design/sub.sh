#!/bin/bash 

#SBATCH --time 0-12:00
#SBATCH -J runA
#SBATCH -o logs/slurm_%A-%a.txt 
#SBATCH --array=1-8
##SBATCH --array=1-8092
#SBATCH -p gc128 

rsync -avz input_pkg/ output_files/$SLURM_ARRAY_TASK_ID/
cd $_
pwd 

awk "NR==$SLURM_ARRAY_TASK_ID" list.txt > mut_flags 

module load rosetta 
rosetta_scripts.linuxgccrelease @flags @mut_flags
