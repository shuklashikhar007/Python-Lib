import pandas as pd
df = pd.DataFrame() # dataframe ek method hai isse call karke
# we can directly create a dataframe
print(df)
lst = ['Shikhar','Shukla','chemical','engineering','IIT BHU']
pdf = pd.DataFrame(lst)
print(pdf)
arr = [[1,2,3],[4,5,6],[7,8,9]]
arrdf = pd.DataFrame(arr)
print(arrdf)
