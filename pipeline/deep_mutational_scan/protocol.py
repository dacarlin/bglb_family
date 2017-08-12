import os 
import io 
import sys 

import pyrosetta 
import pandas 
from random import choice
from rosetta import core, protocols 
from Bio.Data import IUPACData 

#task_id = os.getenv('SLURM_ARRAY_TASK_ID')
#path = os.path.join('output_files', task_id)
#os.chdir(path) 

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

print('total score at begin', beta(pose)) 

def get_residues_with_constraints(pose):    
    cst_set = pose.constraint_set()
    for n in cst_set.get_all_constraints():
        for residue in n.residues():
            yield int(residue)
    

def get_enzyme_design_features(pose, score_function):
    residues_with_constraints = set(get_residues_with_constraints(pose))
    total_score = score_function(pose) 
    print(total_score, 'total score at `get_enzyme_design_features`') 
    energies = pose.energies() 

    score_types = score_function.get_nonzero_weighted_scoretypes()
    print(score_types) 
    for n, r in enumerate(residues_with_constraints, 1):
        print('Found constraints on residue', r) 
        for st in score_types:
            print(type(st)) 
            val = energies.residue_total_energies(r)[st]
            st_str = str(st).replace('ScoreType.', '')
            print(st, val, st_str) 
            yield 'SR_{}_{}'.format(n, st), val

def deep_mutational_scan(pose, score_function, mask=None):
    targets = []
    for n, native in enumerate(pose.sequence(), 1):
        if native != 'Z':
            for one_letter_code, three_letter_code in IUPACData.protein_letters_1to3.items():
                if one_letter_code != native:
                    pkg = '{}{}{}'.format(native, n, one_letter_code)
                    targets.append(pkg)
    print(len(targets), 'targets')

    if isinstance(mask, int):
        print("Applying mask")
        targets = [choice(targets) for n in range(mask)]
        print(len(targets), 'targets after applying mask')
    
    for n, native in enumerate(pose.sequence(), 1):
        copy_pose = core.pose.Pose() 
        copy_pose.assign(pose) 
        for one_letter_code, three_letter_code in IUPACData.protein_letters_1to3.items():     
            name = '{}{}{}'.format(native, n, one_letter_code)
            if name in targets: 
                try:
                    mutate = protocols.simple_moves.MutateResidue(n, three_letter_code.upper())
                    mutate.apply(copy_pose)
                    total_score = score_function(copy_pose) 
                    feats = list(get_enzyme_design_features(copy_pose, score_function))
                    print(feats) 
                    features = pandas.Series(dict(feats)) 
                    print(features) 
                    features.name = name
                    yield features 
                except:
                    print("Failed on", name)
            
df = pandas.DataFrame(deep_mutational_scan(pose, beta, 10)) 
df.to_csv('features.csv') 
print(df.shape) 
