import pandas as pd
import csv

df = pd.read_csv('total_stars.csv')
del df['Luminosity']
del df['Star_name']
del df['Distance']
del df['Mass']
del df['Radius']

final_data = df.dropna()
final_data.reset_index(drop=True,inplace = True)

df.to_csv('pro30.csv')

