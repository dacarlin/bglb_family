import os 

def has_native():
    for n in range(1, 2888+1):
        path = os.path.join('output_files', str(n), 'native.pdb')
        if os.path.isfile(path):
            yield path 

def has_cm():
    for n in range(1, 2889+1):
        path = os.path.join('output_files', str(n), 'cm_low_energy.pdb')
        if os.path.isfile(path):
            yield path 

print('Natives:', len(list(has_native())))
print('CM:', len(list(has_cm())))
