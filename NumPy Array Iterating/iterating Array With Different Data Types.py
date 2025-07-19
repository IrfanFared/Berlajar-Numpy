"""
ngiterasi array tapi sambil mengubah tipe datanya secara on-the-fly. Ini pro-level banget! 🤩
"""
import numpy as np

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)


