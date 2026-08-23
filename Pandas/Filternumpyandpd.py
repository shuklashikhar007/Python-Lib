import pandas as pd
import numpy as np
dataFrame = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                   '  ROSS    ', 'CHANDLER', ' JOEY    '],
                          'Age': [30, 35, 37, 33, 34, 30],
                          'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
                          'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                  'IT', 'ARTIST']})                                 
filtered_values = np.where((dataFrame['Salary']>=100000) & (dataFrame['Age']< 40) & (dataFrame['JOB'].str.startswith('D')))
print(filtered_values)
print(dataFrame.loc[filtered_values])
# assign data
dataFrame = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                   '  ROSS    ', 'CHANDLER', ' JOEY    '],
                          
                          'Age': [30, 35, 37, 33, 34, 30],
                          
                          'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
                          
                          'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                  'IT', 'ARTIST']})
# filter dataframe
print(dataFrame.loc[(dataFrame['Salary']>=100000) & (dataFrame['Age']< 40) & (dataFrame['JOB'].str.startswith('D')),
                    ['Name','JOB']])
# label based search ki ek array pass hogi yaha par
# + Name aur Jobs wale cols bhi chaiye hoge
# filter dataframe using numpy
filtered_values = np.where((dataFrame['Salary']>=100000) & (dataFrame['Age']< 40) & (dataFrame['JOB'].str.startswith('D')))
# filtedred values will be a array of indexs that satisfy our given conditions
print(dataFrame.loc[filtered_values])
# query method to filter ( works only with columns )
print(dataFrame.query('Salary  <= 100000 & Age < 40 & JOB.str.startswith("C").values'))
# loc works with column labels and indexes.
# eval and query works only with columns.
# Boolean indexing works with values in a column only.

