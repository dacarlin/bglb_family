from Bio import SeqIO 
from subprocess import check_output 
import shutil 

# create the grishin file 

grishin_format = '''
## not_used {template_name}_thread
#
scores_from_program: 0
0 {target_sequence}
0 {template_sequence}
--
'''

# get the name of the target 
for record in SeqIO.parse('target.fasta', 'fasta'):
    target = record.name 

# get the target sequence as aligned 
for record in SeqIO.parse('templates.fasta.promals.aln', 'clustal'):
    if record.description == target:
        target_sequence = record.seq

# print out the grishin 
grish = []
for record in SeqIO.parse('templates.fasta.promals.aln', 'clustal'):
    if record.description != target:
        grish.append( grishin_format.format(template_name=record.description[:6].replace('_',''), target_sequence=target_sequence, template_sequence=record.seq ) )

grish = ''.join( grish ) 
with open( 'ali.gri', 'w' ) as fn:
    fn.write( grish ) 

# copy the pdbs 
pth = '/share/work/alex/local_pdb/structures/{}/pdb{}.ent.gz'

with open('templates.txt') as fn:
    templates = fn.read().split()

for t in templates:
    label, chain = t.split('_')
    cmd = [ 'gunzip', '-c', pth.format(t[1:3], t[0:4]) ]
    lines = check_output(cmd, universal_newlines=True) 
    lines = lines.split('\n')
    sele = [n + '\n' for n in lines if n.startswith('ATOM') and n[21] == chain]
    with open( '{}A.pdb'.format(label), 'w' ) as fn:
        fn.write( ''.join(sele) ) 
    
# craete pt_flags 
flags_template = '''
-ignore_unrecognized_res
-beta
-in:file:fasta target.fasta 
-in:file:alignment ali.gri
-in:file:template_pdb {} {} {} {} {} 
'''

template_names = [ '{}A.pdb'.format(n[0:4]) for n in templates ] 
with open( 'pt_flags', 'w') as fn:
    fn.write(flags_template.format(*template_names))
