from Bio import SeqIO
import os

FASTA='targets.fa'
task = os.getenv('SLURM_ARRAY_TASK_ID')
task = int(task)
for n, r in enumerate(SeqIO.parse(FASTA, 'fasta'), 1):
    if n == task:
        SeqIO.write([r], 'target.fasta', 'fasta')
