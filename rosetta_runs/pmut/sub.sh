#!/bin/bash 

~/Documents/rosetta-main/source/bin/pmut_scan_parallel.default.macosclangdebug -s example_input/native.pdb -mutants_list mutants.txt -output_mutant_structures -ex1 -ex2 -ex3 -extrachi_cutoff 1 -use_input_sc -ignore_unrecognized_res -no_his_his_pairE -multi_cool_annealer 10 
