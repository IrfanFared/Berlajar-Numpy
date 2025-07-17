"""
astype adalah fungsu dalam sebuah nupy yang digunakan untuk menguba atau mentranformais sebuah data di array

"""
import numpy as np
arr = np.array([1,2,3,4,5]) 
print(arr.dtype)

# mengubah ke bolean
array_bolean = arr.astype(bool)
print(array_bolean.dtype)

#mengubah bolean ke int
arr = np.array([1.2,2.4,3.9,4.1,5.0])
arr_ke_int = arr.astype(int)
print(arr_ke_int.dtype)

