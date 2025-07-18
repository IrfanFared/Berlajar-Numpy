"""reshape adalah suatu method yang ada di numpy digunakan untuk mengubah sebuah arra ke dalam bentu dimensi yang kita ingignkan"""
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])
# megubah aray 1 dimensi ke dalam benetuk 2 dimesi
covert_to_2d = arr.reshape(2,5) # ubah ke dalam 2 baris 1 kolom # reshape termasuk ke dalam bagian view
print(covert_to_2d)

# mengubah 1 dimensi ke dalam 3 d
arr1 = np.array([1,2,3,4,5,6,7,8,9,10,12,34])
covert_to_3d = arr1.reshape(2,3,2)
print(covert_to_3d)