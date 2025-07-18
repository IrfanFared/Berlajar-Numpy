import numpy as np
"""
berbeda dengan funntion copy yang bisa menyalin objek lain tanpa merubah 
sedangan funtion view hanya membuat salinan diri sendri 
jadi ketika salinanya di ubah makan objek aslinya bakal berubah
maupun sebaliknya

"""
arr =np.array([1,2,12,])
x = arr.view()
arr[0] = 10

print(arr) # jika kode ini menghasilakan none maka array tersebut berdiri sendri
print(x)