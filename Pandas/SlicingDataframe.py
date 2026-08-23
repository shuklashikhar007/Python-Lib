import pandas as pd
player_list = [['M.S.Dhoni', 36, 75, 5428000],
               ['A.B.D Villers', 38, 74, 3428000],
               ['V.Kohli', 31, 70, 8428000],
               ['S.Smith', 34, 80, 4428000],
               ['C.Gayle', 40, 100, 4528000],
               ['J.Root', 33, 72, 7028000],
               ['K.Peterson', 42, 85, 2528000]]
df = pd.DataFrame(player_list, columns=['Name', 'Age', 'Weight', 'Salary'])
print(df)
df1 = df.iloc[0:4]
print(df1)
df2 = df.iloc[:,0:2]
print(df2)
value = df.iloc[2,3]
print("Spec Cell Value:",value)
res = df.query("Age > 25 and Salary > 8000000")
print(res)
# yaha pe set index pandas ko batata hai ki 
# konse column ko row label banana hai (index)
# to ye name col ko row index bana dega
# taki we can use loc method
df.set_index('Name', inplace=True)
custom = df.loc['A.B.D Villers':'S.Smith']


