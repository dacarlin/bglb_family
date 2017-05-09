from Bio import SeqIO

lines = []
for r in SeqIO.parse('bglb.fasta', 'fasta'):
  for i, s in enumerate(r.seq,1):
    for aa in 'ACDEFGHIKLMNPQRSTVY':
      if s != aa:
        params = s, i, aa  
        pkg = '{}{}{}\n'.format(*params)
        lines.append(pkg)      

output_fn='list.all_possible.txt'
with open(output_fn,'w') as fn:
  fn.write( ''.join(lines) )

