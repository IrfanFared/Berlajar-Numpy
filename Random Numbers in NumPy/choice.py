"""
choice adalah method yang digunakan unntuk mengambil sebuah element secara acak
"""
from numpy import random

b = random.choice([1,2,3,32,45,76,43,23,75,53])
print(b)

# memilih secara acak dan di buat kedalam bentuk 2 dimensi
c = random.choice([1,2,3,32,45,76,43,23,75,53],size=(3,2))
print(c)
