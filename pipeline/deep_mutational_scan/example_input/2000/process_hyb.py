import pandas 
import shutil 

df = pandas.read_csv('hyb_score.sc', sep='\s+', header=1) #because it starts with "SEQUENCE:" line 
low_model = df.sort_values(by='total_score').head(1).description.values[0] 
shutil.copyfile('{}.pdb'.format(low_model), 'cm_low_energy.pdb')

print('Lowest energy model from docking', low_model, 'has been saved as cm_low_energy.pdb') 

