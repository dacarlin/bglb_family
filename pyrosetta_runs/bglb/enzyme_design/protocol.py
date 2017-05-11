import rosetta
import pyrosetta

INPUT_POSE = 'input_pose.pdb'
PARAMS = 'pnpg.params'
CST_FILE = 'pnpg.cst'
TARGET = 119
NEW_RES = 'PHE' # has to be three-letter code

pyrosetta.init('-beta -extra_res_fa pnpg.params -run:preserve_header')

print('DetectProteinLigandInterface options: ')
print(pyrosetta.rosetta.basic.options.get_real_option('enzdes:cut1'))
print(pyrosetta.rosetta.basic.options.get_real_option('enzdes:cut2'))
print(pyrosetta.rosetta.basic.options.get_real_option('enzdes:cut3'))
print(pyrosetta.rosetta.basic.options.get_real_option('enzdes:cut4'))
print(pyrosetta.rosetta.basic.options.get_boolean_option('enzdes:detect_design_interface'))

# pyrosetta.rosetta.basic.options.set_real_option('enzdes:cut1',10.0)

# get a generic scorefxn
p = pyrosetta.pose_from_file(INPUT_POSE)
sfxn = pyrosetta.create_score_function('beta_cst')
soft_rep = pyrosetta.create_score_function('soft_rep')
orig = p.sequence()

# enzyme design constraints
addcsts = rosetta.protocols.enzdes.AddOrRemoveMatchCsts()
addcsts.cstfile(CST_FILE)
addcsts.set_cst_action(rosetta.protocols.enzdes.CstAction.ADD_NEW)
addcsts.apply(p)

# predock
predock = rosetta.protocols.enzdes.PredesignPerturbMover()
predock.trans_magnitude(0.1)
predock.rot_magnitude(2)
predock.set_ligand(p.total_residue())


## enzyme design fixed backbone
enzdes = rosetta.protocols.enzdes.EnzRepackMinimize()
enzdes.set_scorefxn_minimize(sfxn)
enzdes.set_scorefxn_repack(soft_rep)
enzdes.set_min_lig(True)
enzdes.set_min_rb(True)
enzdes.set_min_sc(True)
enzdes.set_design(False)

## enzyme design flexible backbone
enzdes_wbb = rosetta.protocols.enzdes.EnzRepackMinimize()
enzdes_wbb.set_scorefxn_minimize(sfxn)
enzdes_wbb.set_min_lig(True)
enzdes_wbb.set_min_rb(True)
enzdes_wbb.set_min_sc(True)
enzdes_wbb.set_design(False)
enzdes_wbb.set_scorefxn_repack(soft_rep)
enzdes_wbb.set_min_bb(True)

# init the scoring of the pose
sfxn(p) # you need this for nbr graph to populate


tf = rosetta.core.pack.task.TaskFactory()

# Sets up the packing/design shells from the global options set above
dp = rosetta.protocols.enzdes.DetectProteinLigandInterface()
dp.init_from_options()

# This restricts the residues define in the constraint file to only be allowed to pack, not designable
canttouchcatres = rosetta.protocols.enzdes.SetCatalyticResPackBehavior()
canttouchcatres.set_fix_catalytic_aa(False) ## seems to freeze them, no repacking if set to True

# push on to the back of the list
tf.push_back(dp)
tf.push_back(canttouchcatres)
# tf.push_back(limchi2)

# Create a packer task, specifically for the cstopt mover to work
pt = tf.create_task_and_apply_taskoperations(p)

enzdes.task_factory(tf)
enzdes_wbb.task_factory(tf)

#alex's movers
mutate = rosetta.protocols.simple_moves.MutateResidue(TARGET, NEW_RES)

# protocol steps
parsed = rosetta.protocols.moves.SequenceMover()
parsed.add_mover(mutate)
parsed.add_mover(predock)
parsed.add_mover(enzdes)

# monte carlo
mc = rosetta.protocols.simple_moves.GenericMonteCarloMover()
mc.set_drift(True)
mc.set_maxtrials(500)
mc.set_sampletype('low')
mc.set_temperature(0.6)
mc.set_mover(parsed)
mc.set_scorefxn(sfxn)
mc.apply(p)

#output a scored PDB
p.dump_scored_pdb('input_pose_0001.pdb', sfxn)
