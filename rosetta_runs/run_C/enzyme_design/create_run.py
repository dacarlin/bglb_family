from Bio import SeqIO
from Bio.Data import IUPACData
import pandas 
import shutil 

fmt = IUPACData.protein_letters_1to3

# first, get a starting model 
df = pandas.read_csv('../tss_docking/score.sc', sep='\s+')
s = df.sort_values('total_score').head(1)['description'].values[0]
print(s)
shutil.copyfile('../tss_docking/{}.pdb'.format(s), 'input_pkg/input_pose.pdb')
print('Using', s) 

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
