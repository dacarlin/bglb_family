from glob import glob 

inputs = glob( '../benchmark/out/*pdb' )
lines = [ '{}\n'.format( i ) for i in inputs ] 

with open( 'list', 'w' ) as fn:
    fn.write( ''.join( lines ) ) 
