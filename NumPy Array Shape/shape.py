import numpy as np
"""
ataribut shape digunakan untuk melihat besar suat array dalm betuk axis
"""

arr1d = np.array([1,3,4,5,7])
print(arr1d.shape)
print("-"*10)
arr2d = np.array([[12,12,32],[12,23,23]])
print(arr2d.shape)
arr_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])
print(arr_3d.shape)
