"""
kita bisa membuat array dari mudule random dan kita sendri bisa menetukan panjang array tersebut
"""

from numpy import random

b = random.randint(200,size=100)
print(b)

# membuatt array 2 dimensi dengan random
c = random.randint(1,10,size=(2,2))
print(c)