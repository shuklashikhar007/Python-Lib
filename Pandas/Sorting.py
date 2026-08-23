import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Score': [85, 90, 95, 80]}
df = pd.DataFrame(data)
sorted_df = df.sort_values(by='Age', ascending=False)
print(sorted_df)
sorted_df = df.sort_values(by=['Age', 'Score'])
print(sorted_df)
data_with_nan = {"Name": ["Alice", "Bob", "Charlie", "David"],"Age": [28, 22, None, 22]}
df_nan = pd.DataFrame(data_with_nan)
sorted_df = df_nan.sort_values(by="Age", na_position="first")
print(sorted_df)
# using a sort algorithmn 
# sorting ke orders yahi pe laga do 
res = df.sort_values(['Age','Score'],ascending=[True,False])
print(res)
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [28, 22, 25, 22, 28],
    "Score": [85, 90, 95, 80, 88]
}
df = pd.DataFrame(data)
sorted_df = df.sort_values(by='Age', kind='mergesort')
print(sorted_df)
