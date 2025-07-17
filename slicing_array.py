"""
slicing array digunakan untung mengabil elemen dari x sampai ke y
[start : end]
"""


import numpy as np

arr = np.array([1,2,3,4,4,5,6,2,7])
# mengabila dari 0 sampai indeks 
print(arr[1:4])
# mengambil elemen daari awal samapai 2 (indeks 2 tidak termasuk)
print(arr[:2])
# negatice slicing
print(arr[-1:-5])
# mengebelikan elemen lain dari x sampai y denga dengan melewati z indeks
print(arr[1:5:2])
# mengabil ideks dari awal  sampai akhir dengan melawati  x kali
print(arr[::2])


