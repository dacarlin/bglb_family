#!/bin/bash 
#SBATCH --time 2-00:00
#SBATCH -J hyb
#SBATCH -o log.txt 
module load rosetta 
rosetta_scripts.linuxgccrelease @flags 
