import pyrosetta
from rosetta.protocols import simple_moves, residue_selectors
from rosetta.core import select, chemical 
import numpy as np 
import sys 
import seaborn as sns
import pandas
from Bio.Data import IUPACData

pyrosetta.init('-beta -extra_res_fa example_input/pnpg.params')

pose = pyrosetta.pose_from_file('example_input/input_pose_0001.pdb')
score = pyrosetta.create_score_function('beta_cst') 

wild_type_energy = score( pose )
print( 'Wild type energy:', wild_type_energy ) 

def run_all_20( position_index ):
    
    residues = []
    scores = []
    for olc, tlc in IUPACData.protein_letters_1to3.items():
        copy_pose = pose.clone()
        protocol = [
            simple_moves.MutateResidue(position_index, tlc.upper()), 
        ]
        for item in protocol: 
            item.apply(copy_pose) 
        residues.append(olc) 
        scores.append(score(copy_pose)) 
        
    sys.stdout.write("\rFinished position {1:0d}".format(position_index))
    sys.stdout.flush()
    return dict(zip(residues, scores)) 

data = list( map( run_all_20, range( 1, 10 ) ) ) 

# In[16]:

df = pandas.DataFrame( data, columns=fmt.keys() )
df.index = df.index + 1 
df.shape


# In[17]:

seaborn.heatmap(df, cmap='viridis')


# In[8]:

df.mean( axis=0 ).sort_values()


# In[17]:

df.mean( axis=1 )


# In[30]:

#df.to_csv( 'repack_mutated_residue_only.csv' ) 

