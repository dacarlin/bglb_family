#!/bin/bash

source activate snakes 

#muscle -in ../alignments/PFGH01_trimmed.fasta -out aln.fa
#python uniqify_fasta.py # -> uniq_aln.fa
#./FastTree uniq_aln.fa > tree.nwk 
python graphlan/graphlan_annotate.py --annot annot.txt ../alignments/tree.nwk input.xml 
python graphlan/graphlan.py input.xml out.png  --dpi 200 

