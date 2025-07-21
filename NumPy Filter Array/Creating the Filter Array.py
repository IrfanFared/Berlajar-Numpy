"""
kita juga bisa filtering array mengunakan kosep for in juga
"""

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

arr_yang_diambil = []

for elemen in arr:
    if elemen > 4:
        arr_yang_diambil.append(True)
    else:
        arr_yang_diambil.append(False)

filter_array = arr[arr_yang_diambil]
print(filter_array)