gri_format = '''
## template {five_letter_name}_thread.pdb
# 
scores_from_program: 0
0 {target_sequence}
0 {template_sequence}
--
'''

from skbio import Protein 

Protein.read( 'promals.fasta' ) 


