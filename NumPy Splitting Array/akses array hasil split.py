"""
kita bisa mengases sebuah array yang sudah di split 
kita bisa akses satuan array
"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])