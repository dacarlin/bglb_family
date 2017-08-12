#!/bin/bash
#
#SBATCH --time 0-12:00
#SBATCH -J 4mu 
#SBATCH --array=1-9580
#SBATCH -p gc128 
#SBATCH -o logs/slurm.%A-%a.out

hostname -f 
rsync -avz input_pkg/ output_files/${SLURM_ARRAY_TASK_ID}
cd $_
pwd
module load rosetta 
rosetta_scripts.linuxgccrelease @flags @mutant_flags 

#~/Applications/main/source/bin/rosetta_scripts.default.macosclangrelease @flags @mutant_flags
