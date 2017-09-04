from Bio import SeqIO
from Bio.Data import IUPACData
import pandas 
fmt = IUPACData.protein_letters_1to3

# We will begin with a input PDB and associated params and constraint files 
# that have the names `input_pose.pdb`, `pnpg.params`, and `pnpg.cst`, 
# as well as a `target.fasta` that is the sequnce of th input pdb 

def create_list():
    r = next(SeqIO.parse('target.fasta', 'fasta'))
    for i, s in enumerate(r.seq,1):
        for aa in 'ACDEFGHIKLMNPQRSTVY':
            if s != aa:
                neat_name = '{}{}{}'.format(s,i,aa) 
                pkg = '-parser:script_vars t={} n={} #{}\n' 
                yield pkg.format(i, fmt[aa].upper(), neat_name)       

output_fn='input_pkg/list.txt'
with open(output_fn,'w') as fn:
    contents = ''.join(create_list())
    fn.write(contents)

print('Add sub.sh: #SBATCH --array=1-{}'.format(len(lines)))
print('or run with "sbatch sub.sh --array=1-{}"'.format(len(lines)))
