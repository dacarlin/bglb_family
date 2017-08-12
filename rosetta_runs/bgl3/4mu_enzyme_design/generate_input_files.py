from itertools import product
from Bio.SeqUtils import IUPACData

def fmt(upper_3):
    result = IUPACData.protein_letters_3to1[ upper_3.capitalize() ]
    return result 

POSE_LEN = 480 

possible_residues = [
    "ALA", "ARG", "ASN", "ASP", "CYS", "GLU", "GLN",
    "GLY", "HIS", "ILE", "LEU", "LYS", "MET", "PHE",
    "PRO", "SER", "THR", "TRP", "TYR", "VAL"
]

mutants = []
for i, (pos, new) in enumerate( product( range(1, POSE_LEN), possible_residues ) ):
    native = 'X'
    mut = '{}{}{}\n'.format( native, pos, fmt(new) )
    mutants.append(mut)
    #with open( 'output_files/{}/mutant_flags'.format(i+1), 'w' ) as fn:
    #    flags = '-parser:script_vars target={target}  new_res={new_res}'
    #    fn.write( flags.format( target=pos, new_res=new ) ) 

with open( 'input_pkg/list.txt', 'w' ) as fn:
    fn.write( ''.join(mutants) ) 


#dfs = []
#for i, (pos, new) in enumerate( product( range(1, 480), possible_residues ) ):
#    score_path = 'output_files/{}/score.sc'.format(i+1)
#    if os.path.isfile( score_path ):
#        df = pandas.read_csv( score_path, sep='\s+' )
#        df[ 'new' ] = new 
#        df[ 'pos' ] = pos 
#        dfs.append( df ) 

#df = pandas.concat( dfs ) 

