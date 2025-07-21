"""
search shorted adalah sebuah method numpy yang digunakan untuk mencari nilai x di indeks berapa
hanya saja search shorted sebuah arraynya haru sudah terurut jika tidak maka akan menghasikan nilai indeks yang ramdom
search shorted gapangya digunakan untuk mencari nilai x bisa disisipkan dimana 
"""

import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)
print(x)

# kita bisa mencari dari dari kanan maupun kiri
arr1 = np.array([6, 7, 8, 9])

y = np.searchsorted(arr1, 7, side='right')

print(y)


# pencarian search shorte juga bisa multiple nilai
arr2 = np.array([1, 3, 5, 7])

z = np.searchsorted(arr2, [2, 4, 6])

print(z)