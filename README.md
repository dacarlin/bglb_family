# Software pipeline for modeling the GH01 enzyme family 

This pipeline is designed to handle thousands of input sequences and run on Cabernet in a few days. 

Broadly, we have three parts 

## Comparative modeling for overall protein fold

Each target sequence is transformed into a 3D structure using RosettaCM (initially, stock, and later, using Steve's improved enzyme CM)

## Model enzyme active site with transition state structure 

Next, the target substrate or substrates is created, parameterized for Rosetta, and then docked into the active site. In order to do this, we infer the identity of the catalytic residues based on a multiple sequence alignment (or, if that doesn't work, a Bayesian method I came up with described later) 

## Deep mutational scan to generate feature sets for point mutations 

Once we have a complete model of the enzyme with transition state structure, we can model all possible point mutations to the enzyme-substrate complex (including differnet chemical groups on the substrate) to predict function 
