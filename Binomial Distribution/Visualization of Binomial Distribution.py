"""
random bilonomial digunakan untuk mebuat percobaan secara random berapa kali nilai n muncul
method bilnomial memiliki 3 parameter
- n yang berari nilai angka yang kita ingin cek berapa kali keluar
- p= adalah peluang yang kita inginkan
- size yang berarti berapa kali percobaan
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.binomial(n=10, p=0.5, size=1000))

plt.show()