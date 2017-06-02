#!/bin/bash 
module load rosetta 
rosetta_scripts.linuxgccrelease @flags 
python get_low.py 
