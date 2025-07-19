"""
kiya bisa mengenumerat sebuah iterasi di numpy dengan fungsi ndnumerete

"""
import numpy as np

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)