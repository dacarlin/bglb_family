#!/bin/bash

UNALIGNED_FASTA=../full_auto/targets.fa
OUT_IMAGE=out.png 

muscle -in $UNALIGNED_FASTA -out out.fa 
./FastTree out.fa > tree.nwk 
source activate snakes 
python graphlan/graphlan_annotate.py --annot annotations.txt tree.nwk $OUT_IMAGE
open $_
