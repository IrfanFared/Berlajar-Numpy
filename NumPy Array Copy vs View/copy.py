import numpy as np
"""
jadi kata kunci copy digunakan pada numpy untuk menyali elemen dari obejek numoy tampa mengubah objek aslinya
jadi jatonya membuat objek sendiri
"""

arr =np.array([1,2,12,])
x = arr.copy()
arr[0] = 10

print(arr)
print(x)