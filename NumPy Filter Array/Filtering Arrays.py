"""
filtering array digunakan untuk memilih element pada array kita ingginkan
"""

import numpy as np
arr = np.array([1,2,3])

x = [True,False,True]

hasil_filtering_array = arr[x] # ini bakal ngasi tau python kalo ambil nilai yang bernilai true
print(hasil_filtering_array)

