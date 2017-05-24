from Bio import SeqIO
import os 

FASTA='/share/work/alex/bglb_family/family_1_in_freezer/all_sequences.fasta'
task = os.getenv('SLURM_ARRAY_TASK_ID')
for n, r in enumerate(SeqIO.parse(FASTA, 'fasta')):
    if str(n) == task:
        SeqIO.write([record], 'target.fasta', 'fasta')
    
