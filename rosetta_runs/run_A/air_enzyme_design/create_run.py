from Bio import SeqIO
from Bio.Data import IUPACData

fmt = IUPACData.protein_letters_1to3

#from sys import argv

#allowed = None 
#if len(argv) > 1:
#    fn = argv[1]
#    print('Restricting mutants generated to those found in', fn)
#    with open(fn) as fn:
#        allowed = fn.read().split()

lines = []
for r in SeqIO.parse('../partial_thread/target.fasta', 'fasta'):
  for i, s in enumerate(r.seq,1):
    for aa in 'ACDEFGHIKLMNPQRSTVY':
      if s != aa:
        neat_name = '{}{}{}'.format(s,i,aa) 
        pkg = '-parser:script_vars t={} n={} #{}\n' 
        params = i, fmt[aa].upper()
        lines.append(pkg.format(*params, neat_name))      

output_fn='input_pkg/list.txt'
with open(output_fn,'w') as fn:
  fn.write( ''.join(lines) )

print('Add to sub.sh: #SBATCH --array=1-{}'.format(len(lines)))
