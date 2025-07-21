"""
ada cara lain juga mengunakan cara lain
"""
import numpy as np

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr] # ini adalah kondisi array apa yang harus di short

print(filter_arr)
print(newarr)