import numpy as np


arr1 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr2 = np.array([[[2, 4, 6], [8, 10, 12]], [[14, 16, 18], [20, 22, 24]]])

arr_mult = arr1 * arr2

print(arr_mult)