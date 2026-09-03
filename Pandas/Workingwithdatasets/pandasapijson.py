# working on apis in python with json and pandas
import pandas as pd
import requests as r # python library jo ki apis se related help karti hai 
url = 'https://jsonplaceholder.typicode.com/posts'
res = r.get(url)
data = pd.json_normalize(res.json())
data.head()
print(data)
try:
    r.put(url,"Shikhar")
except:
    print("error sending data to API")

