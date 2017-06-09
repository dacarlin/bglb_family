import pandas 
import shutil 

df = pandas.read_csv('score.sc', sep='\s+', header=0)
df.sort_values(by='total_score', inplace=1)

n = df.head(1).description.values[0]

print(df.shape)
print(df.columns)
print(df.head())

shutil.copyfile('{}.pdb'.format(n), 'low_energy.pdb')
