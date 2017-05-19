import pandas
import os 
from glob import glob 

search_path = '/share/work/alex/output__bglb_family/pyrosetta_runs/bglb/enzyme_design/*.pdb'
L = list(glob((search_path)))
mutants = []
dat = []
for g in L: 
    name = os.path.basename(g)
    with open(g) as fn:
        for i, line in enumerate(fn.readlines()):
            if 'BEGIN_POSE' in line:
                hline = i+1
            if 'END_POSE' in line:
                fline = i-1

    print(g)
    print(name)
    print('Header line found on line', hline)
    print('Footer line found on line', fline)
    
    nr = fline-hline
    print(nr)
    df = pandas.read_csv(g, header=hline, nrows=nr, sep='\s+')
    df['sequence_position'] = df.index - 1 
    dat.append(df.stack())
    mutants.append(name)
    print('Finished structure {}/{}'.format(n,len(L)))

print('Preparing to create H5 file')
df = pandas.DataFrame(dat, index=mutants)
df.to_hdf('data.h5', 'my_key')
print('Created H5 file!')
print('Printing df.head() and df.shape')
print(df.head())
print(df.shape)
