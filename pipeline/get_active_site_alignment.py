# requires completed pipeline with "native.pdb" in each folder 


# active site alignments 

from Bio.Data import IUPACData
from itertools import chain 
import os 
import numpy as np 

BASE_DIR = '/share/work/alex/bglb_family/pipeline/output_files/'

result = []

for n in range(1, 3000):
    path = os.path.join(BASE_DIR, str(n), 'native.pdb')
    
    if not os.path.isfile(path):
        continue 

    with open(path) as fn:
        lines = fn.readlines()
        ca = [n for n in lines if n.startswith('ATOM') and 'CA' in n]
        ligand = [n for n in lines if n.startswith('HETATM')]

    def distance(xyz_1, xyz_2):
        x1, y1, z1, x2, y2, z2 = [float(n) for n in chain(xyz_1, xyz_2)]
        return np.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)

    #print(distance(ligand_center, ["1.2", "4.3", "2.2"]))

    for ligand_atom in ligand:
        if len(ligand_atom.split()) != 12:
            continue 

        _, _, atom_name, tlc, _, pos, x, y, z, _, _, _ = ligand_atom.split()
        if atom_name == 'C5':
            ligand_center = x, y, z
            #print(ligand_center)


    active_site_seq = []
    for c in ca:
        if len(c.split()) != 12:
            continue 

        _, _, _, tlc, _, pos, x, y, z, _, _, _ = c.split()

        #print(x, y, z)
        name = tlc.capitalize() + pos 
        dist = distance(ligand_center, (x, y, z))
        #print('CA {} distance to ligand center {} Å'.format(name, dist))

        if dist < 16:
            pkg = IUPACData.protein_letters_3to1[tlc.capitalize()]
            active_site_seq.append(pkg)

    final = ''.join(active_site_seq)
    #print(len(final))
    pkg = '>{}\n{}\n'.format(n, final)
    result.append(pkg)
    
with open('active_site.fa', 'w') as fn:
    fn.write(''.join(result))
    
