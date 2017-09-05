import os 
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Polypeptide import PPBuilder
from Bio.Data import IUPACData
from Bio import SeqIO 

dirs = open('list_of_input_folders.txt').read().split()

outs = []
for d in dirs:
    pdb = os.path.join(d, 'input_pose_0001.pdb')
    target = os.path.join(d, 'target.fasta') 
    r = next(SeqIO.parse(target, 'fasta'))
    print('Generating {} mutants for id "{}" based on {}'.format(20*len(r), r.id, pdb))
    for n, native in enumerate(r.seq, 1):
        for k, v in IUPACData.protein_letters_1to3.items():
            s = '-s {} -parser:script_vars t={} n={} l={} \n'
            result = s.format(pdb, n, v.upper(), len(r.seq)+1)
            outs.append(result) 

with open('list.txt', 'w') as fn:
    result = ''.join(outs) 
    fn.write(result) 
