import pandas 
import os 

dfs = []
with open( 'input_pkg/list.txt' ) as fn:
    for i, mutant in enumerate( fn.readlines(), 1):
        pth = os.path.join( 'output_files', str(i), 'score.sc' ) 
        if os.path.isfile( pth ):
            df = pandas.read_csv( pth, sep='\s+' )
            s = df.mean()
            s.name = mutant.split('#')[1].strip()
            dfs.append(s) 
            print('Finished', i) 

df = pandas.DataFrame( dfs ) 
df.to_hdf('features.h5', 'my_key')
print( 'Features of shape', df.shape, 'written to H5!') 


