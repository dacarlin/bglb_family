#!/bin/bash
#SBATCH -J pipeline
#SBATCH -o logs/log_%A_%a.txt
#SBATCH --array=1-2888
#SBATCH -t 1-06:00
#SBATCH -p gc128 

# load modules and global variables
module load use.own
module load hmmer promals alex-rosetta 

# set up project
OUT_DIR=output_files/$SLURM_ARRAY_TASK_ID
rsync -avz comparative_modeling/ $OUT_DIR
cd $_
pwd
hostname -f 
env 

# use the SLURM env vars to get the right target 
python get_target.py # -> target.fasta 

# search for homologs
localp=/share/work/alex/local_pdb/sequences/pdb_seqres.txt
phmmer --noali --tblout table.out -A aln.fasta target.fasta $localp 
awk 'NR>3' table.out | cut -c 1-144 > raw_hmmer.txt 
python process_hmmer.py # -> templates.txt, templates.fasta 

# structural alignment (switch to Python 2 env for this) 
source activate snakes 
promals templates.fasta
source deactivate

# partial thread
python partial_thread.py
partial_thread.linuxgccrelease @pt_flags

# hybridize
python set_up_hyb.py 
rosetta_scripts.linuxgccrelease @hyb_flags # -> S_0001.pdb 
mv score.sc hyb_score.sc 
python process_hyb.py 

# docking (infer catalytic residues, construct input file, run) 
python guess_catalytic_residues.py # -> input_pose.pdb 
rosetta_scripts.linuxgccrelease @dock_flags
python process_dock.py
