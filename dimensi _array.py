import numpy as np

# Array 1D
# jadi array 1 dimensi namanya vektor
arr_1d = np.array([1, 2, 3, 4, 5])
print(f"Dimensi arr_1d: {arr_1d.ndim}") # Output: 1

# Array 2D namanya matiks
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Dimensi arr_2d: {arr_2d.ndim}") # Output: 2

# Array 3D namanya tensor
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"Dimensi arr_3d: {arr_3d.ndim}") # Output: 3


"""
dimensi di array itu kayak arah atau indeks untuk menemukan suatu elemen
"""

# bagaimana cara mengakses sebuah nilai di arry numpy
# jika 1 dimensi  cara mengasesnya seperti mengakses sebuah list
print(arr_1d[0])

#jika 2 dimensi cara mengasesnya seperti koodinat kartesius
print(arr_2d[1,1])

print(arr_3d)


# Bikin array 3D (2 lapisan, tiap lapisan 2 baris, 3 kolom)
arr_3d = np.array([
    [[1, 2, 3], [4, 5, 6]], # Lapisan 0
    [[7, 8, 9], [10, 11, 12]] # Lapisan 1
])
print(f"Array 3D:\n{arr_3d}")
print("-" * 30)

# Ngakses elemen di lapisan 0, baris 0, kolom 0 (angka 1)
print(f"Elemen di [0, 0, 0]: {arr_3d[0, 0, 0]}") # Output: 1

# Ngakses elemen di lapisan 1, baris 1, kolom 2 (angka 12)
print(f"Elemen di [1, 1, 2]: {arr_3d[1, 1, 2]}") # Output: 12

# Ngambil satu lapisan penuh (lapisan 0)
print(f"Lapisan pertama:\n{arr_3d[0]}")
# Output:
# [[1 2 3]
#  [4 5 6]]

# Ngambil semua baris dan kolom dari lapisan 1
print(f"Semua elemen di lapisan kedua:\n{arr_3d[1, :, :]}")
# Output:
# [[ 7  8  9]
#  [10 11 12]]

# Ngambil kolom pertama dari semua lapisan dan baris
print(f"Kolom pertama dari semua lapisan dan baris:\n{arr_3d[:, :, 0]}")
# Output:
# [[ 1  4]
#  [ 7 10]]n