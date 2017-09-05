import pandas 
import os 
from Bio import SeqIO 

def get_dfs():
    for n in range(1, 2889):
        path = os.path.join('output_files', str(n), 'score.sc')
        if os.path.isfile(path):
            r = next(SeqIO.parse(os.path.join('output_files', str(n), 'target.fasta'), 'fasta'))
            df = pandas.read_csv(path, sep='\s+')
            df['id'] = r.id 
            yield df.sort_values(by='total_score').head(1) 
           
df = pandas.concat(get_dfs())
df.to_csv('enzyme_design_features.csv')

def get_dfs():
    for n in range(1, 2889):
        path = os.path.join('output_files', str(n), 'hyb_score.sc')
        if os.path.isfile(path):
            r = next(SeqIO.parse(os.path.join('output_files', str(n), 'target.fasta'), 'fasta'))
            df = pandas.read_csv(path, sep='\s+', header=1)
            df['id'] = r.id 
            yield df.sort_values(by='total_score').head(1) 
           
df = pandas.concat(get_dfs())
df.to_csv('hyb_features.csv')
