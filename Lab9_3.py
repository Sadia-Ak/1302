import numpy as np

arr = np.array([3, 5, 23, 54, 32, 45, 123, 12])

arr_split = np.split(arr, [2, 5])

print(arr_split)