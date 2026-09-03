import pandas as pd
import json
data = {"One": {"0": 60, "1": 60, "2": 60, "3": 45, "4": 45, "5": 60},
        "Two": {"0": 110, "1": 117, "2": 103, "3": 109, "4": 117, "5": 102}}
json_data = json.dumps(data)
# normalising data 
# ye imp hai since api ka data nested form mai ata hai to we need this to flatten it to a good level
df_normalize = pd.json_normalize(json.loads(json_data))
print("\nDataFrame using JSON module and `pd.json_normalize()` method:")
print(df_normalize)


