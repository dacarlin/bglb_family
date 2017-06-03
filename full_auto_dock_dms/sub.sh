#!/bin/bash

#PROJECT_ROOT=
#PARAMS_PATH=

rsync -avz input_pkg/ output_files 
cd output_files 
pwd 
python guess_catalytic_residues.py 
( cat enzdes_header.txt && grep '^ATOM' ../../hybridize/low_energy.pdb && cat pnpg.pdb ) > input_pose.pdb
rosetta_scripts.default.macosclangrelease @dock_flags 

