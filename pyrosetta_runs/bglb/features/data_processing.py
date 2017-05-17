import pandas
from glob import glob 

dat = []
mutants = []
for n in range(1,8026+1):

    # first, find a low-energy model 
    #sc = pandas.read_csv('output_files/{}/score.sc'.format(n))

    g = glob('output_files/{}/*_0007.pdb'.format(n))
    if g:
        pose = g[0]
        name = pose.split('_')[2]
        with open(pose) as fn:
            for i, line in enumerate(fn.readlines()):
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
