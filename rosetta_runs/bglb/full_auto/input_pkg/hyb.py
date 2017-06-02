import pyrosetta 
from rosetta.protocols import hybridization, relax
from glob import glob 
from Bio import SeqIO

pyrosetta.init()

s1 = pyrosetta.create_score_function('score3')
s2 = pyrosetta.create_score_function('score4_smooth_cart')
s3 = pyrosetta.create_score_function('beta_cart')

hy = hybridization.HybridizeProtocol()
hy.set_stage1_scorefxn(s1)
hy.set_stage2_scorefxn(s2)
hy.set_fullatom_scorefxn(s3)

for g in glob( '*thread.pdb' ):
    hy.add_template(g, 'AUTO')
    
for record in SeqIO.parse('target.fasta', 'fasta'):
    seq = ''.join(record.seq)
    
p = pyrosetta.pose_from_sequence(seq)
hy.apply(p)
relax = relax.FastRelax(s3)
relax.apply(p)

p.dump_scored_pdb('cm.pdb', s3)

#<ROSETTASCRIPTS>
#<SCOREFXNS>
#    <ScoreFunction name="stage1" weights="score3" symmetric="0">
#        <Reweight scoretype="atom_pair_constraint" weight="0.5"/>
#    </ScoreFunction>
#    <ScoreFunction name="stage2" weights="score4_smooth_cart" symmetric="0">
#        <Reweight scoretype="atom_pair_constraint" weight="0.5"/>
#    </ScoreFunction>
#    <ScoreFunction name="beta" weights="beta_cart" symmetric="0">
#        <Reweight scoretype="atom_pair_constraint" weight="0.5"/>
#    </ScoreFunction>
#</SCOREFXNS>
#<MOVERS>
#<Hybridize name="hybridize" stage1_scorefxn="stage1" stage2_scorefxn="stage2" fa_scorefxn="beta" batch="1" stage1_increase_cycles="1.0" stage2_increase_cycles="1.0">
#    <Template pdb="../partial_thread/1gnxA_thread.pdb" cst_file="AUTO" weight="1.000" />
#    <Template pdb="../partial_thread/3cmjA_thread.pdb" cst_file="AUTO" weight="1.000" />
#    <Template pdb="../partial_thread/3w53A_thread.pdb" cst_file="AUTO" weight="1.000" />
#    <Template pdb="../partial_thread/4hz6A_thread.pdb" cst_file="AUTO" weight="1.000" />
#</Hybridize>
#<FastRelax name="relax" scorefxn="beta" />
#</MOVERS>
#<PROTOCOLS>
#    <Add mover="hybridize"/>
#    <Add mover="relax"/>
#</PROTOCOLS>
#<OUTPUT scorefxn="beta" />
#</ROSETTASCRIPTS>
#
