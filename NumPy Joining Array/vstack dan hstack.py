"""
hstack digunakan untuk mengabugkan elemen di dari dua kolom menjadi baris
vstack digunakan untuk mengabukan elemen dari dua kolom mejadi kolom kesatuan
"""
import numpy as np

# Data nilai siswa: matematika dan fisika
matematika = np.array([[80], [90], [75]]) # Bentuk (3, 1)
fisika = np.array([[85], [92], [70]])     # Bentuk (3, 1)

print("Nilai Matematika:\n", matematika)
print("Nilai Fisika:\n", fisika)

# Gabungkan nilai secara horizontal (tambah kolom nilai fisika)
nilai_gabung_horizontal = np.hstack((matematika, fisika))
print("\nNilai Gabung Horizontal (hstack):\n", nilai_gabung_horizontal)
# Output:
# [[80 85]
#  [90 92]
#  [75 70]]
# Bentuknya jadi (3, 2)

import numpy as np

# Data penjualan Q1 (Jan-Mar)
penjualan_q1 = np.array([[100, 120, 110],  # Penjualan Toko A
                         [150, 130, 160]]) # Penjualan Toko B

# Data penjualan Q2 (Apr-Jun)
penjualan_q2 = np.array([[180, 170, 190],  # Penjualan Toko A
                         [200, 210, 220]]) # Penjualan Toko B

print("Penjualan Q1:\n", penjualan_q1)
print("Penjualan Q2:\n", penjualan_q2)

# Gabungkan penjualan secara vertikal (tambah baris penjualan Q2)
penjualan_gabung_vertikal = np.vstack((penjualan_q1, penjualan_q2))
print("\nPenjualan Gabung Vertikal (vstack):\n", penjualan_gabung_vertikal)
# Output:
# [[100 120 110]
#  [150 130 160]
#  [180 170 190]
#  [200 210 220]]
# Bentuknya jadi (4, 3)