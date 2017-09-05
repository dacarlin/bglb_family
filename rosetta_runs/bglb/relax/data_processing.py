import pandas 
from glob import glob 
import os 

dfs = []
g = glob( 'output/relax*' ) 
for dir_path in g:
    score_path = dir_path + '/score.sc' 
    if os.path.isfile( score_path ):
        df = pandas.read_csv( score_path, sep='\s+', header=2 )
