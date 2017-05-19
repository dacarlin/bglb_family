import os
from itertools import product
from Bio.SeqUtils import IUPACData
import pyrosetta
from rosetta.protocols import enzdes, simple_moves, moves
from rosetta.core import pack

INDEX = int(os.getenv('SLURM_ARRAY_TASK_ID'))
INPUT_POSE = 'input_pose.pdb'
PARAMS = 'pnpg.params'
CST_FILE = 'pnpg.cst'
OUT_PATH = 'output_files' 

# initialize PyRosetta
pyrosetta.init('-beta -extra_res_fa pnpg.params -run:preserve_header')

# create a pose
p = pyrosetta.pose_from_file(INPUT_POSE)

# calculate the mutant we are making if there is an index set
if INDEX:
    a = range(1, p.total_residue()+1)
    b = sorted(map(str.upper,IUPACData.protein_letters_3to1.keys()))
    TARGET, NEW_RES = list(product(a,b))[INDEX]
    mut = '{}{}{}'.format(p.sequence()[TARGET-1], TARGET, IUPACData.protein_letters_3to1[NEW_RES.capitalize()])
    print('target:', TARGET, 'new_res:', NEW_RES, 'mut:', mut)
else:
    TARGET = 10
    NEW_RES = 'ILE'
    mut = 'M10I_example'
    # this is a synonymous mutation
    # I think

# get a scorefxn
sfxn = pyrosetta.create_score_function('beta_cst')
soft_rep = pyrosetta.create_score_function('soft_rep')

# enzyme design constraints
addcsts = enzdes.AddOrRemoveMatchCsts()
addcsts.cstfile(CST_FILE)
addcsts.set_cst_action(enzdes.CstAction.ADD_NEW)
addcsts.apply(p)

# predock
predock = enzdes.PredesignPerturbMover()
predock.trans_magnitude(0.1)
predock.rot_magnitude(2)
predock.set_ligand(p.total_residue())

## enzyme design fixed backbone
repack_min = enzdes.EnzRepackMinimize()
repack_min.set_scorefxn_minimize(sfxn)
repack_min.set_scorefxn_repack(soft_rep)
repack_min.set_min_lig(True)
repack_min.set_min_rb(True)
repack_min.set_min_sc(True)
repack_min.set_design(False)

## enzyme design with backbone movement 
repack_min = enzdes.EnzRepackMinimize()
repack_min.set_scorefxn_minimize(sfxn)
repack_min.set_scorefxn_repack(soft_rep)
repack_min.set_min_lig(True)
repack_min.set_min_rb(True)
repack_min.set_min_sc(True)
repack_min.set_design(False)
repack_min.set_min_bb(True)

# init the scoring of the pose
sfxn(p) # you need this for nbr graph to populate

# Sets up the packing/design shells from the global options set above
dp = enzdes.DetectProteinLigandInterface()
dp.init_from_options()

# This restricts the residues define in the constraint file to only be allowed to pack, not designable
canttouchcatres = enzdes.SetCatalyticResPackBehavior()
canttouchcatres.set_fix_catalytic_aa(False) ## seems to freeze them, no repacking if set to True

# push on to the back of the list
tf = pack.task.TaskFactory()
tf.push_back(dp)
tf.push_back(canttouchcatres)
pt = tf.create_task_and_apply_taskoperations(p)
repack_min.task_factory(tf)

#alex's movers
mutate = simple_moves.MutateResidue(TARGET, NEW_RES)

# protocol steps
parsed = moves.SequenceMover()
parsed.add_mover(mutate)
parsed.add_mover(predock)
parsed.add_mover(repack_min)

# monte carlo
mc = simple_moves.GenericMonteCarloMover()
mc.set_drift(True)
mc.set_maxtrials(50)
mc.set_sampletype('low')
mc.set_temperature(0.6)
mc.set_mover(parsed)
mc.set_scorefxn(sfxn)
mc.apply(p)

#output a scored PDB
out_path = os.path.join(OUT_PATH, 'mutant_{}.pdb'.format(mut))
p.dump_scored_pdb(out_path, sfxn)
