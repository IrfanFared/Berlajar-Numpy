"""
jadi kalo ditribusi poison digunakan untuk  menghitung berapa kejadian yang terjadi dalama rentang waktu 
sebaliknya kalo exponetial ditribution menghitung berapa lama waktu yang dibutuhkan dari kejadian berhasil kejadian berhasil selanjutnya

memiliki parameter 
scale adalah rata rata
size
"""
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.exponential(size=1000), kind="kde")

plt.show()