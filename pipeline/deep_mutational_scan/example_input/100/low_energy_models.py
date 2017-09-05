import pandas 

df = pandas.read_csv('score.sc', sep='\s+')
df.sort_values(['total_score',], inplace=True)
print(df.head())

