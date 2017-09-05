#!/bin/bash
#SBATCH -J pipeline-dms
#SBATCH -o log_dms/log-%A-%a
#SBATCH --array=1
#SBATCH -t 0-00:15
#SBATCH -p gc128

# brief: this code performs deep mutational scanning 
# prep needed: run the comparative modeling code 

# set up project
OUT_DIR=output_files/$SLURM_ARRAY_TASK_ID
cp deep_mutational_scan/protocol.py $OUT_DIR
cd $_
pwd
hostname -f 

# run the DMS and collect features into a CSV or H5
which python 
python protocol.py 
cat dms_features.csv 
