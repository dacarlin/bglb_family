import pandas
from glob import glob 
import os 

dat = []
mutants = []

with open( 'input_pkg/list.txt' ) as fn:
    muts = enumerate( fn.readlines() )

for n, mutant in muts:
    pth = os.path.join( 'output_files', str(n), 'input_pose_0007.pdb' )
    if os.path.isfile( pth ):
        with open( pth ) as fn:
            for i, line in enumerate( fn.readlines() ):
                if 'BEGIN_POSE' in line:
                    hline = i+1
                if 'END_POSE' in line:
                    fline = i-1

        print('Header line found on line', hline)
        print('Footer line found on line', fline)

        df = pandas.read_csv(pose, header=hline, nrows=fline-hline, sep='\s+')
        df['sequence_position'] = df.index - 1 
        dat.append(df.stack())
        mutants.append(name)
        print('Finished structure {}/{}'.format(n,210))

print('Preparing to create H5 file')
df = pandas.DataFrame(dat, index=mutants)
df.to_hdf('data.h5', 'my_key')
print('Created H5 file!')
print(df.head())
print(df.shape)
