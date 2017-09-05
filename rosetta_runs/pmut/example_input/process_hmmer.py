from Bio import SeqIO
import pandas 

names = '''target accession query accession Evalue1 score1 bias1 Evalue 
           score bias exp reg clu ov env dom rep inc'''.split() # god damn you hmmer 

df = pandas.read_csv('raw_hmmer.txt', comment='#', sep='\s+', header=None)
df.columns = names 

record = next(SeqIO.parse('target.fasta', 'fasta'))
templates = df.head(10)['target'] # -> pandas Series 

localp = '/share/work/alex/local_pdb/sequences/pdb_seqres.txt'
wanted = [record] + [n for n in SeqIO.parse(localp, 'fasta') if n.name in templates.values]
SeqIO.write(wanted, 'templates.fasta', 'fasta')

# also write out templates file 
with open('templates.txt', 'w') as fn:
    fn.write(' '.join(templates.values))

print('Using {} templates from HMMER search'.format(len(wanted))) 
