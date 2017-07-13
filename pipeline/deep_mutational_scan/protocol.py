import os 

import pyrosetta 
import pandas 
import sys 
from random import choice
from rosetta import core, protocols


task_id = os.getenv('SLURM_ARRAY_TASK_ID')

pyrosetta.init('-preserve_header -beta -extra_res_fa pnpg.params')
pose = pyrosetta.pose_from_file('native.pdb')
beta = pyrosetta.create_score_function('beta_cst')

emo = core.scoring.methods.EnergyMethodOptions()
emo.hbond_options().decompose_bb_hb_into_pair_energies(True) 
beta.set_energy_method_options(emo)


# add in match constraints (could also use regular restraints) 
add_cst = protocols.enzdes.AddOrRemoveMatchCsts()
add_cst.set_cst_action(protocols.enzdes.ADD_NEW)
add_cst.cstfile('pnpg.cst')
add_cst.apply(pose)


def get_residues_with_constraints(pose):    
    cst_set = pose.constraint_set()
    for n in cst_set.get_all_constraints():
        for residue in n.residues():
            yield int(residue)
            
set(get_residues_with_constraints(pose))

def get_enzyme_design_features(pose, score_function):
    residues_with_constraints = set(get_residues_with_constraints(pose))
    energies = pose.energies()
    score_types = score_function.get_nonzero_weighted_scoretypes()

    for n, r in enumerate(residues_with_constraints, 1):
        for st in score_types:
            val = energies.residue_total_energies(r)[st]
            st_str = str(st).replace('ScoreType.', '')
            yield 'SR_{}_{}'.format(n, st_str), val


def deep_mutational_scan(pose, score_function, mask=None):
    '''
    
    deep_mutational_scan(pose: Pose, score_function: ScoreFunction, mask: int or boolean mask) 
    Returns: 
    
        pandas.DataFrame  
    ''' 
    
    targets = []
    for n, native in enumerate(pose.sequence(), 1):
        if native != 'Z':
            for one_letter_code, three_letter_code in IUPACData.protein_letters_1to3.items():
                pkg = '{}{}{}'.format(native, n, one_letter_code)
                targets.append(pkg)
    print(len(targets))

    if isinstance(mask, int):
        print("Applying mask")
        # mask is an int, that means we only want the first `mask` 
        # samples from the deep mutational scan (for debug) 
        targets = [choice(targets) for n in range(mask)]
        print(targets)
    #elif len(mask) == pose.total_residue():
        # this is a boolean mask 
    #    targets = [t for m, t in zip(mask, targets) if m == 1]          
    
    for n, native in enumerate(pose.sequence(), 1):
        copy_pose = pose.clone()
        for one_letter_code, three_letter_code in IUPACData.protein_letters_1to3.items():     
            name = '{}{}{}'.format(native, n, one_letter_code)
            if name in targets: 
                count += 1 
                
                try:
                    
                    mutate = protocols.simple_moves.MutateResidue(n, three_letter_code.upper())
                    mutate.apply(pose)
                    total_score = score_function(copy_pose) 
                    features = pandas.Series(dict(get_enzyme_design_features(copy_pose, score_function)))
                    features.name = name

                    #sys.stdout.write("\rFinished " + features.name)
                    #sys.stdout.flush()

                    yield features 
                except:
                    print("Failed on", name)
            
df = pandas.DataFrame(deep_mutational_scan(pose, beta)) 
df.head()

df.to_csv('dms_features.csv') 

