import numpy as np
import matplotlib.pyplot as plt

# Rata-rata waktu tunggu antar pelanggan adalah 3 menit.
# Berarti, scale = 3.
scale_param = 3

# Kita mau mensimulasikan 1000 waktu tunggu
# np.random.exponential(scale, size)
simulated_data = np.random.exponential(scale=scale_param, size=1000)

print("10 sampel pertama dari data simulasi:")
print(simulated_data[:10])

# ---

# Biar lebih kebayang, kita bisa visualisasikan pake histogram
plt.figure(figsize=(10, 6))
plt.hist(simulated_data, bins=50, density=True, alpha=0.6, color='b', edgecolor='black')
plt.title(f'Distribusi Eksponensial dengan Scale = {scale_param}')
plt.xlabel('Waktu Tunggu (menit)')
plt.ylabel('Probabilitas')
plt.grid(axis='y', alpha=0.75)
plt.show()