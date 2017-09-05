import pandas 
import shutil 
from Bio import SeqIO 

r = next(SeqIO.parse('target.fasta', 'fasta')) 
df = pandas.read_csv('score.sc', sep='\s+')
low_model = df.sort_values(by='total_score').head(1).description.values[0] 
shutil.copyfile('{}.pdb'.format(low_model), 'native.pdb')
print('Lowest energy model from docking', low_model, 'for target', r.id) 

