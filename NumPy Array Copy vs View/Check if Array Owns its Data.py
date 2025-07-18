import numpy as np
"""
kita dapat mengecek apakah sebuah array berdiri sendiri atau hanya salinan objek itu sendri
kita bisa mengecek dengan atribut base
"""
arr =np.array([1,2,12,])
x = arr.view()
arr[0] = 10

print(arr.base)
print(x.base)