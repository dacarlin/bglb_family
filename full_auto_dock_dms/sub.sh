#!/bin/bash 
#SBATCH -J autocm
#SBATCH -t 1-00:00
#SBATCH -o logs/log_%A_%a.txt 
#SBATCH --array=1-5 

# set up project 
OUT_DIR=output_files/$SLURM_ARRAY_TASK_ID
rsync -avz input_pkg/ $OUT_DIR
cd $_ 
pwd 

# load modules and global variables 
module load use.own 
module load hmmer promals rosetta 
localp=/share/work/alex/local_pdb/sequences/pdb_seqres.txt

# use the SLURM_ to get the right target.fasta file 
python get_target.py 

# search for homologs 
phmmer --tblout table.out -A aln.fasta target.fasta $localp
#phmmer --notextw --noali --tblout table.out -A aln.fasta target.fasta $localp
# sort table by coverage first, and then get head 
#awk 'NR>3 {print $1}' table.out | sort -kx | head -5 > templates.txt 
awk 'NR>3 {print $1}' table.out | head -5 > templates.txt 
python process_hmmer.py

# structural alignment 
source activate py27 
promals templates.fasta
source deactivate 

# partial thread 
python partial_thread.py 
partial_thread.linuxgccrelease @pt_flags

# hybridize 
python hyb.py 

# output of this is a model "cm.pdb" 

# infer catalytic residues and run docking 

python guess_catalytic_residues.py 

( cat enzdes_header.txt && grep '^ATOM' cm.pdb && cat pnpg.pdb ) > input_pose.pdb

rosetta_scripts.default.macosclangrelease @dock_flags 

