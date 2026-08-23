import pandas as py
# using all types of joins here
import pandas as pd
data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K1', 'K0', 'K1'],
         'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],}
data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K0', 'K0', 'K0'],
         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}
df = pd.DataFrame(data1)
df1 = pd.DataFrame(data2)
print(df, "\n\n", df1) 
res = pd.merge(df,df1, how = 'left', on = ['key','key1'])
print(res)
res1 = pd.merge(df, df1, how='right', on=['key', 'key1'])
print(res1)
#union of tables
res2 = pd.merge(df,df1,how = 'outer',on = ['key','key1'])
print(res2)
# inner (intersection of tables)
res3 = pd.merge(df,df1,how = 'inner', on = ['key','key1'])
print(res3)
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32]}
data2 = {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']}
df = pd.DataFrame(data1,index=['K0', 'K1', 'K2', 'K3'])
df1 = pd.DataFrame(data2, index=['K0', 'K2', 'K3', 'K4'])
print(df, "\n\n", df1)
res = df.join(df1)
print(res)
res1 = df.join(df1,how = 'outer')
print(res1)



