"""
di dalam sebuah array kita bisa mengiterasikan sebuah array dengan for loop
"""



import numpy as np

#iterasi array 1 dimensi
arr_1d = np.array([1,2,3,4,5,5])

for i in arr_1d:
    print(i)

print("-"*10)

# iterasi array 2 dimensi
arr_2d = np.array([[12,3], [12,12]])


#iterasi setiap elemen di array dimensi 2
for i in arr_2d:
    for j in i :
        print(j)
# iterasi baris di array dua dimensi
for i in arr_2d:
    print(i)

print('-'*10)

itarasi_3d = np.array([[[12,12,12],[1,1,1]],[[5,5,5],[7,7,7]]])
print(itarasi_3d.ndim)

#iterasi setiap elemen di erray 3 dimensi
for i in itarasi_3d:
    print(i)
    