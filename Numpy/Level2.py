import numpy as np
import time as t
arr = np.array([
    [10, 20, 30],
    [ 5, 25, 35],
    [15, 10, 40]
])
min_along_col = np.min(arr, axis=0)
min_along_row = np.min(arr,axis=1)
print(min_along_col)
print(min_along_row)

