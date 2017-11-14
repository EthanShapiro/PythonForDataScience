import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)     # To get the same random numbers

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)
print(df > 0)
booldf = df > 0
print(df[booldf])
print(df['W'] > 0)
print(df[df['W'] > 0])
print(df[df['Y'] > 0])
