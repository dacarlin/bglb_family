# Software pipeline for modeling the GH01 enzyme family 

## How to run 

See notes on required software below. 

1. `bash cm-sub.sh` # runs the comparative modeling
2. `bash dms-sub.sh` # runs the deep mutational scan 

## Runtime and limitations 

This pipeline is designed to handle thousands of input sequences and run on Cabernet in about 1 day per thousand sequences if nodes are available. Each sequence takes about 30 compute hours to generate the comparative model.  

## Overview 

Broadly, we have three parts 

## Comparative modeling for overall protein fold

Each target sequence is transformed into a 3D structure using RosettaCM (initially, stock, and later, using Steve's improved enzyme CM)

## Model enzyme active site with transition state structure 

Next, the target substrate or substrates is created, parameterized for Rosetta, and then docked into the active site. In order to do this, we infer the identity of the catalytic residues based on a multiple sequence alignment (or, if that doesn't work, a Bayesian method I came up with described later) 

## Deep mutational scan to generate feature sets for point mutations 

Once we have a complete model of the enzyme with transition state structure, we can model all possible point mutations to the enzyme-substrate complex (including differnet chemical groups on the substrate) to predict function 


# Dependencies 

Anaconda Python 3 with PyRosetta installed ([instructions on how to install PyRosetta](http://www.pyrosetta.org/dow). 

Additionally, right now you must create a special conda environment for promals to run in (Python 2), since promals has not been updated to Python 3. To do this (and you only have to do it once):

```bash
conda create --name snakes python=2 anaconda 
curl -O url://of/promals
cd promals
python setup.py install 
``` 

The rest of the software can be found as modules on Cabernet (the `phmmer` software can be accessed with `module load phmmer`) and so doesn't need to be installed by you 


