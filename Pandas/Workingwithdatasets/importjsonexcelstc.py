import pandas as pd
path = "D:\Coding-3rdyear\AIML\Pandas\Workingwithdatasets\people.csv"
df = pd.read_csv(path)
#print(df)
jsondata = df.to_json() # cvs data converted to json 
names = pd.read_csv(path, usecols=["Name","Gender"])
print(names)
hei = pd.read_csv(path, usecols=["Height(cm)"])
print(hei)
df = pd.read_csv(path,index_col="Name") # now the index col is the dataframe index
# now this will act as the row label 
# handling missing values (imp)
df = pd.read_csv(path,na_values=["N/A","Unknown"])
# na values ke andar jo bhi hoga agar esa kahi bhi kuch mila csv
# ke andar to it will replace it with NaN
# sep ke sath reading
#df = pd.read_csv('sample.csv',sep='[:, |_]',engine='python')  
# rows limiter
df = pd.read_csv(path,nrows=3)
print(df)
# skip rows
df = pd.read_csv(path,skiprows=[0,2])
print(df)
df = pd.read_csv(path, parse_dates=["Date of Birth"])
print(df)
# reading csv sidha url se 
url = "https://media.geeksforgeeks.org/wp-content/uploads/20241121154629307916/people_data.csv"
df = pd.read_csv(url)
print(df)
Shikhar = {
    "Name" : "Shikhar",
    "Gender" : "Male",
    "Skin Color" : "Fair",
}
dp = pd.DataFrame(Shikhar)
dp.to_csv("Shikhar.csv", sep = "\t", index = False)
new_df = pd.read_csv("Shikhar.csv", sep = "\t")
new_df

