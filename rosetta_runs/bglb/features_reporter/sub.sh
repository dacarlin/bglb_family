#!/bin/bash
#SBATCH -t 0-24:00
#SBATCH -J feat_bgl
#SBATCH -o log.txt 
#SBATCH --mem-per-cpu=16G 
module load rosetta 
rosetta_scripts.linuxgccrelease @flags 
