#!/bin/bash 
#SBATCH --time 0-12:00

module load rosetta 
rosetta_scripts.default.linuxgccrelease @flags 
