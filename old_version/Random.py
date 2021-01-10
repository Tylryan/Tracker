import random
import pandas as pd

df = pd.read_csv('record.csv')

for x in df:
    for i in df.index:
        if i % 2 == 0:
            print('')
        else:
            print(df[x])
