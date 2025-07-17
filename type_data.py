#tipe data pada numpy bisa kita cek dengan dtype
import numpy as np

arr = np.array([1,2,3,5,5])
print(arr.dtype)

# membuat array dan mendefinisiakn dengan tipe data yang pasti

arr1 = np.array([1,2,3,5,5], dtype="i4")
print(arr1.dtype)