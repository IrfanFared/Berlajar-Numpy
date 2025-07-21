"""
di numpy kita bisa mencari nilai elemenn di indeks berapa pada array dengan mengunakan method whre
"""

import numpy as np

arr = np.array([1,2,3,4,5,5,6])

index_array = np.where(arr == 2)
print(index_array)