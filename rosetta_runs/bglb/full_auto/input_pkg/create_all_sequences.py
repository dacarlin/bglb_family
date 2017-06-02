from Bio import SeqIO 

amino_acids = 'ACDEFGHIKLMNPQRSTVWY'
assert len( amino_acids ) == 20 

seqs = []
for record in SeqIO.parse('bglb_model.fa', 'fasta'):
  for pos, native in enumerate(record.seq, 1):
    for designed in amino_acids:
      s = list(str(record.seq[:]))
      s[pos-1] = designed
      s = ''.join(s) 
      name = '{}{}{}'.format(native, pos, designed)
      seq = '>{}\n{}\n'.format(name, s)
      seqs.append(seq)

with open('all_sequences.fa', 'w') as fn:
  fn.write(''.join(seqs)) 
