""" 
terkadan kita kesuliatan untuk iterasi yang dimensinya n maka bakal kaselitan untuk membuat foor lopnya
alternatif yang lebih efiesien kita bisa gunakan sebuah funtion bawaan dari numpy  yautu nditer()

"""
import numpy as np
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)