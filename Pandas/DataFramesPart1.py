import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)     # To get the same random numbers

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)
print(df['W'])
print(df.W) # Don't use this
print(df[['W', 'Y']])
df['new'] = df['W'] + df['Y']
print(df)
df.drop('new', axis=1, inplace=True)    # Inplace has to be true or else df must equal df.drop()
print(df)
df.drop('E', axis=0, inplace=True)
print(df)
print(df.shape)
print(df.loc['A'])
print(df.iloc[2])
print(df.loc['B', 'Y'])
print(df.loc[['A', 'B'], ['W', 'Y']])
