#!/bin/bash 
#SBATCH -J autocm
#SBATCH -t 0-01:00
#SBATCH -o logs/log_%A_%a.txt 
#SBATCH --array=1-5 

######### CHANGE TIME BACK BEFORE SUBMIT!!!!!!!! 

# completely automated cm for glycoside hydrolases 
# use like 
# 
#   sbatch sub.sh 
#
# after editing input files 

OUT_DIR=freezer/$SLURM_ARRAY_TASK_ID
rsync -avz input_pkg/ $OUT_DIR
cd $_ 
pwd 

module load use.own 
module load hmmer promals rosetta 
localp=/share/work/alex/local_pdb/sequences/pdb_seqres.txt

python get_target.py 

# search for homologs 
phmmer --tblout table.out -A aln.fasta target.fasta $localp
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
