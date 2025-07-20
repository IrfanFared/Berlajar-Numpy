"""
di numpy ada yang namanya funtion stack yang dimana fungsinya hapir mirip dengan conactenate -
hanya saja di memiliki perilaku yang unix dimana dia mengubah array sesuai axis yang kita definisikan 
berbedan dengan concate yang hanya menyabunkan sebuah array stack merubah bentuk array dan mengabunkan
"""

import numpy as np
arr1 = np.array([1,2,3,4,5,])
arr2 = np.array([1,2,3,3,4,])

arr = np.stack((arr1,arr2), axis=1)
print(arr)