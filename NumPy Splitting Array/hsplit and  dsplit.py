"""
kita bisa split colum tanpa mendifiniskan axis dan tidak menggunakan array split
yang sebernarnya sama aja kayak method split hanya saja lebih spisifik

"""

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr)
