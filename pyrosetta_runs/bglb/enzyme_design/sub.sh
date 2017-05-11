#!/bin/bash
#SBATCH -t 0-02:00
#SBATCH -a 1-10
#SBATCH -o logs/%A_%a.txt 
python protocol.py
