"""
jadi funntion bawaan numpy concetenate digunalan untuk menyambungkan array yang sudah ada
misal kita definisikan axis= 0 makan akan menyabungkan baris array1 dan baris array 2
axis = 1 maka kita akan meyabungkan kolom array satu dan array 2
jadi axis 0 = vertikal axis = 1 horizontal
"""




import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([1,2,3,4])


arr = np.concatenate((arr1, arr2))
print(arr)



arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7,2 ]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)

