import os 
from Bio.Data import IUPACData
from Bio import SeqIO 

fmt = IUPACData.protein_letters_1to3

base = '/share/work/alex/bglb_family/pipeline/output_files'
target = 2885 

def generate_flags():
    r = next(SeqIO.parse(os.path.join(base, target, 'target.fasta', 'fasta')) 
    for pos, native in enumerate(r.seq, 1):
        for k in fmt.keys():
            path = os.path.join(base, target, 'DMS_input.pdb')
            pkg = (path, len(r) + 1, pos, fmt[k].upper(), r.id, native, pos, k) 
            yield '-s {} -parser:script_vars l={} t={} n={} # {} {}{}{}\n'.format(*pkg)

with open('input_pkg/list.txt', 'w') as fn:
    fn.write(''.join(generate_flags())

