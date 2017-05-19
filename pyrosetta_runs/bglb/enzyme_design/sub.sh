#!/bin/bash
#SBATCH -t 0-02:00
#SBATCH -a 1-9000 
#SBATCH -o logs/%A_%a.txt 
time python protocol.py
