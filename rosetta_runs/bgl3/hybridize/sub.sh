#!/bin/bash 
#SBATCH --time 5-00:00
#SBATCH -J rom_cm
#SBATCH -p gc128 
module load rosetta 
rosetta_scripts.linuxgccrelease @flags 
