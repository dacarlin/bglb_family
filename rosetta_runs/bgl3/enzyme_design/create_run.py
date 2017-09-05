from Bio import SeqIO
from Bio.Data import IUPACData

fmt = IUPACData.protein_letters_1to3

lines = []
for r in SeqIO.parse('bgl3.fasta', 'fasta'):
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

