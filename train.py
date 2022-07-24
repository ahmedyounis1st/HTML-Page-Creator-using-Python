import pandas as pd
import numpy as np

arr = np.full((7, 4), "a")
df = pd.DataFrame(arr, columns=['A', 'B', 'C', 'D'])
df = pd.DataFrame([
    ('A1', 'B1', '1', 'extra'), ('A1', 'B1', '2', 'extra'),
    ('A1', 'B2', '3', 'extra'), ('A1', 'B2', '4', 'extra'),
    ('A2', 'B1', '5', 'extra'), ('A2', 'B1', '6', 'extra'),
    ('A2', 'B2', '7', 'extra'), ('A2', 'B2', '8', 'extra'),
    ], columns=['A', 'B', 'C', 'D'])
print(df.head())