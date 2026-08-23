import pandas as pd
import numpy as np
data_list = ['g', 'e', 'e', 'k', 's']
ser = pd.Series(data_list)
print(ser) # kind of ek marked array with 0 based indexing print karne
# wala data structure hota hai ye 
data_dict = {'Geeks': 10, 'for': 20, 'geeks': 30}
ser = pd.Series(data_dict)
print(ser)
ser = pd.Series(np.linspace(1, 10, 5))
print(ser)
ser = pd.Series(range(5, 15))
print(ser)
ser=pd.Series(range(1,20,3), index=[x for x in 'abcdefg'])
print(ser)