from __future__ import print_function 
from Bio import SeqIO 

with open('templates.txt') as fn:
    templates = fn.read().split()

for record in SeqIO.parse('target.fasta', 'fasta'):
    target = record 

print('templates', templates) 

localp = '/share/work/alex/local_pdb/sequences/pdb_seqres.txt'
wanted = [target] + [n for n in SeqIO.parse(localp, 'fasta') if n.name in templates]
SeqIO.write(wanted, 'templates.fasta', 'fasta') 

print('wanted', wanted) 

