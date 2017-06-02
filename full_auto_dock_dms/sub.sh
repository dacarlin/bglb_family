#!/bin/bash

#PROJECT_ROOT=
#PARAMS_PATH=

cp -r input_pkg output_files 
cd output_files 

python generate_input_files.py ../params.json 
( cat enzdes_header.txt && grep '^ATOM' ../../hybridize/low_energy.pdb && cat pnpg.pdb ) > input_pose.pdb
rosetta_scripts.default.macosclangrelease @flags 

