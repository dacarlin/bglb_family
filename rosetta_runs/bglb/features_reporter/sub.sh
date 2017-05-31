#!/bin/bash
# 
#SBATCH -t 0-10:00
#SBATCH --output=logs/slurm.out
#SBATCH --error=logs/slurm.err
#SBATCH --job-name=features 
#SBATCH --array=1 
#SBATCH -p gc128 
#SBATCH --mem-per-cpu=10G 

module load rosetta 
rosetta_scripts.linuxgccrelease @flags 

