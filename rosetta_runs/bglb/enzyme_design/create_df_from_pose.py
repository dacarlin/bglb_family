import pandas 

pose='input_pose_0001.pdb'
with open(pose) as fn:
  for i, line in enumerate(fn.readlines()):
    if 'BEGIN_POSE' in line:
      hline = i

with open(pose) as fn:
  for i, line in enumerate(fn.readlines()):
    if 'END_POSE' in line:
      fline = i 

print('Header line found on line', hline)

df = pandas.read_csv('
