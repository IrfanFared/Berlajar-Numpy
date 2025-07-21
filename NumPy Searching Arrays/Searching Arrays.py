"""
di numpy kita bisa mencari nilai elemenn di indeks berapa pada array dengan mengunakan method whre
agak lambat jika data array sangat besar
where bakan mencari nilai  yang hanya nilainya terpenuhi

"""



import numpy as np

arr = np.array([1,2,3,4,5,5,6,2])

index_array = np.where(arr == 2)
print(index_array)

# kali bisa juga menambahkan logika seperti mencari nilai yang habis di bagi 2
index_nilai_habis_dibagi_dua = np.where(arr%2 == 0)
print(index_nilai_habis_dibagi_dua)