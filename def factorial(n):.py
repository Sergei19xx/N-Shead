def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

import pandas as pd

path = '/Users/nicks/Documents/GitHub/N-Shead/CSV4.csv'

df = pd.read_csv(path)
df
text = df['TEXT'].iloc[0]
print(text)
