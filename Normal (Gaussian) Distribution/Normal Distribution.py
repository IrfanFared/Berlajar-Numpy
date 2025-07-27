"""
di module numpu kita bisa generete angka untuk menghasilkan nila norma distrubusi

random.normal()
di dalam method norma terdiri dari  3 parameter
- loc atau mean yang menjadi titik puncak
- scale atau standard devitation 
- size atau ukuran array
"""

from numpy import random

x = random.normal(loc=1, scale=2, size=(2, 3))

print(x)

# deviasi sangat berpengaruh terhadap gemuk atau kuru suatu grafik jikan deviasinya 0.5 makan akan kurus ataupun sebaliknya