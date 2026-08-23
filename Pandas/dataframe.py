# ek python dictionary se dataframe banana
import numpy as np
import pandas as pd
data = {'A' : np.array([1,4,7]),
        'B' : np.array([2,5,8]),
         'C' : np.array([2,6,9])}
df = pd.DataFrame(data)
print(df)
data = [
    {'name': 'Mike', 'degree': 'MBA', 'score': 90},
    {'name': 'Dan', 'degree': 'BCA', 'score': 40},
    {'name': 'Emilia', 'degree': 'M.Tech', 'score': 80},
]
df = pd.DataFrame(data)
print(df)
#indexing 
data = {'Name': ['Jake', 'Eve', 'Charlie'],
        'Age': [ 22, 35, 28],
        'Gender': [ 'Male', 'Female', 'Male'],
        'Salary': [40000, 70000, 48000]}
df = pd.DataFrame(data)
print(df.index)
import pandas as pd

data = {'Name': ['Jake', 'Mike'],
        'Age': [25, 30],
        'Salary': [50000, 55000]}
df = pd.DataFrame(data)
res = df.set_index('Name')
print(res)
#Reseting the index
import pandas as pd

data = {'Name': ['Jake', 'Maria', 'Sam'],
        'Age': [25, 30, 22] }
df = pd.DataFrame(data)
res = df.reset_index(drop=True)
print(res)
# indexing with loc
import pandas as pd
data = {'age': [25, 30], 'city': ['NY', 'LA']}
# yaha pe hamne do row bana di hai alice aur bob naam ki
df = pd.DataFrame(data, index=['Alice', 'Bob'])
row = df.loc['Alice']
print(row)
# loc matlab label based indexing
# df.loc['Alice'] -> ye label based hai 
# df.loc[0] -> ye integer position based hai 
# Access the first three rows and the 'Name' and 'Age' column
data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'], 
        'Age': [25, 30, 22, 35, 28], 
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'], 
        'Salary': [50000, 55000, 40000, 70000, 48000]}

df = pd.DataFrame(data)
# Display the entire DataFrame
print(df)
subset = df.loc[0:2,['Name','Age']] # ye kaam kar raha hai 
# since rows are labeled as 0 and 1 but col ke case mai nahi karega
# since waha par cols are not labelled as 0 and 1
print(subset)
filter = df[df['Age'] > 25]
print(filter)
# Access the 'Salary' of the row with label 2
salary_at_index_2 = df.at[2, 'Salary']
print(salary_at_index_2)
# Selecting data
data = pd.read_csv("/content/nba.csv", index_col="Name")
print("Dataset")
print(data.head(5))
first = data["Age"]
print("\nSingle Column selected from Dataset")
print(first.head(5)) # head matlab kitni entries uss col ki 
first = data[["Age", "College", "Salary"]]
print("\nMultiple Columns selected from Dataset")
print(first.head(5))
# We can select specific rows and columns by providing lists of row labels and column names:
# Dataframe.loc[["row1", "row2"], ["column1", "column2", "column3"]]
selection = data.loc[["Avery Bradley", "R.J. Hunter"], ["Team", "Number", "Position"]]
print(selection)
# Access all rows and specific cols
all_rows_specific_columns = data.loc[:, ["Team", "Position", "Salary"]]
print(all_rows_specific_columns)
# selecting using iloc
data = pd.read_csv("/content/nba.csv", index_col="Name")
row = data.iloc[3]
print(row)
# mul rows
rows = data.iloc[[3, 5, 7]]
print(rows)
# mul rows aur cols ek sath
selection = data.iloc[[3, 4], [1, 2]]
print(selection)
# selc sari rows and spec col by position
selection = data.iloc[:, [1, 2]]
print(selection)
value = data.at["Avery","Age"]
print(value)
# res = data.query("Age > 25 and College == Duke")
# print(res)
# Function	Description
# DataFrame.iat[]	Access a single value for a row/column pair by integer position.
# DataFrame.pop()	Return item and drop from DataFrame.
# DataFrame.xs()
# Return a cross-section (row(s) or column(s)) from the DataFrame.
# DataFrame.get()	Get item from object for given key (e.g DataFrame column).
# DataFrame.isin()	Return a boolean DataFrame showing whether each element is contained in values.
# DataFrame.where()	Return an object of the same shape with entries from self where cond is True otherwise from other.
# DataFrame.mask()	Return an object of the same shape with entries from self where cond is False otherwise from other.
# DataFrame.insert()	Insert a column into DataFrame at a specified location.