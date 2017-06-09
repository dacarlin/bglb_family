from Bio import SeqIO
import os 

FASTA='/share/work/alex/bglb_family/full_auto_dock_dms/targets.fa'
task = os.getenv('SLURM_ARRAY_TASK_ID')
task = int(task)
for n, r in enumerate(SeqIO.parse(FASTA, 'fasta')):
    print(n, task)
    if n == task:
        SeqIO.write([r], 'target.fasta', 'fasta')
    
