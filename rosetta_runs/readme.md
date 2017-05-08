Rosetta models of BglB homologs
===============================

What's in the data sets?
------------------------

Proteins we model here:

Name|Uniprot ID|Data set|Parameters|Reference
----|----------|--------|---------
BglB| P22505 |k<sub>cat</sub>, K<sub>M</sub>, k<sub>cat</sub>/K<sub>M</sub>, T<sub>50</sub>|Carlin-Caster data set|[[1](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0147596)]
Family_A | Q7MG41 | k<sub>cat</sub>, K<sub>M</sub>, k<sub>cat</sub>/K<sub>M</sub>, T<sub>50</sub>| Caster data set|
Family_B | Q97AX4 |k<sub>cat</sub>, K<sub>M</sub>, k<sub>cat</sub>/K<sub>M</sub>, T<sub>50</sub>| Caster data set|
Family_C | Q59976 | k<sub>cat</sub>, K<sub>M</sub>, k<sub>cat</sub>/K<sub>M</sub>, T<sub>50</sub>|Caster data set|
Bgl3|Q59976 |log<sub>10</sub> enrichment after heat| Romero data set|[[3](http://www.pnas.org/content/112/23/7159.short)]

### Contents of each model

#### Crystal structures

If the model is derived from a crystal structure, we run the `relax` protocol, which provides us with a low-energy Rosetta model.

#### Comparative modeling

If there is no crystal structure available (or, in the case of Bgl3, there is a crystal structure avaiale muct it is is missing denisty), then we model the structure based on the sequence using RosettaCM.

To do this, we search the PDB with HMMER. For example, we may get (for Family_A, above) these top 5 HMMER hits:

- 3ta9
- 4ptv
- 2o9p
- 2jie
- 1np2

Ran Promals3D and retrieved alignments. We make a `partial_thread` working dir. Next, we run `hybridize`.

Workflow:

1. hand-make all grishans
2. run partial thread
3. set up hydridzie
4. run hybridize

#### Transition state docking/multi state docking

We can easily dock, becuase we know the catalytic geometry. Here is the workflow: 

1. ovrlay the models with BglB model
2. transfrom the pNPG from BglB model
3. run each through repack/min
4. then generate mutants for each one
5. score for features (same features as for the native model)
6. train elastic net on BglB data set, and then do blind predictions
7. if those aren't very good, then try using bagging
8. write up results, whatever they are, and present to Justin as a paper
9. profit?
