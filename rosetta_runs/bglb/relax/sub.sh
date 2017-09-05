#!/bin/bash
#
#SBATCH --array=1-1000
#SBATCH -o logs/slurm-%A_%a.out
#SBATCH -J relax 

cp -r input output/relax_${SLURM_ARRAY_TASK_ID}
cd $_
module load rosetta 
relax.default.linuxgccrelease @flags 

