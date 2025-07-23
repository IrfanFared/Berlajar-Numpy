"""
contoh mengahsilkan sebuah array dengan random distribusi
"""
import numpy as np # Biasa kita import numpy as np, biar lebih standar
from numpy import random

# note peluang dari data distribusi haru jika di jumlah sama dengan 1
a = random.choice([1,3,4,9], p=[0.2,0.3,0.4,0.1], size=(3,2))
print(a)