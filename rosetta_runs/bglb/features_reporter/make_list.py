import os 

paths = []
for n in range(1, 9000):
    for p in range(1, 11):
        path = '../enzyme_design/output_files/{0}/input_pose_{1:04d}.pdb'.format(n, p)
        if os.path.isfile(path):
            paths.append(path + '\n')
        else:
            print('File {}, {} ({}) not found'.format(n, p, path))

with open( 'list.txt', 'w' ) as fn:
    fn.write( ''.join( paths ) )
