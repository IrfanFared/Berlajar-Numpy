"""
kita bisa bida split sebuah aray susuai dengan keinginan kita 
kaya split colom saja atau baris saja
"""


import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(arr)
newarr = np.array_split(arr, 3, axis=1)
print(newarr[0])

print(newarr)