from Bio import SeqIO 
import pandas 
import os 

def get_features():
    for n in range(1, 2889):

        features = []
        base = '/share/work/alex/bglb_family/completed_pipeline/output_files/'
        r = next(SeqIO.parse(os.path.join(base, str(n), 'target.fasta'), 'fasta'))
        name = r.id

        if os.path.isfile(os.path.join(base, str(n), 'input_pose_0001.pdb')):
            features.append(1)
        else:
            features.append(0)

        sf = os.path.join(base, str(n), 'score.sc')
        if os.path.isfile(sf):
            df = pandas.read_csv(sf, sep='\s+')
            df = df.sort_values('total_score').head(1)
        
        yield (name, *features) 

df = pandas.DataFrame(get_features())
print(df.head())
print(df.shape) 
df.to_hdf('results.h5', 'my_key') 
