"""
apa itu split di  numpy jadi funtion split di gunakan untuk memecah array menjadi n yang kita ingikan
"""

import numpy as np

arr = np.array([1,2,3,4,5,6])

divide_array = np.array_split(arr,3)
print(divide_array)

#ada kondisi dimana kita ingin memecah array mejadi yang kita ingikan tapi array tersebut tidak habis di bagi n makan akan di pecah menajadi yang kita ingikan hanya saja tidak sempurna
arr_ganjil = np.array([1,2,3,4,5,6])
divide_array_cacat = np.array_split(arr_ganjil,4)
print(divide_array_cacat)