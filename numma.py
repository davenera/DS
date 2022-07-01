#import numpy as np
import pandas as pd

'''my_arr = np.ones((3, 5), dtype=float)
my_arr2 = np.linspace(0, 16, 9, dtype=int)
print(my_arr2)
my_arr3 = my_arr2.reshape((3,3))
print(my_arr3)
print(my_arr3.max())'''

my_ind = pd.Index(['TX','NY','CA','ND','SD'])
df = pd.DataFrame({"year":[2008, 2008, 2016, 2020, 2016],
                   "pop":[20000,30000,40000,50000,60000],
                   "salary":[10000,400000,200000,90000,1000000]}, my_ind)
print(df)
print(df.groupby('year', sort=True)['salary'].sum())
Q1 = pd.DataFrame()
df.pivot_table()