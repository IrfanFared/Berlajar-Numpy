import numpy as np
import matplotlib.pyplot as plt

# Generate Chi-Square distributed data with different degrees of freedom
df1 = 3
df2 = 6
df3 = 10

data1 = np.random.chisquare(df=df1, size=1000)
data2 = np.random.chisquare(df=df2, size=1000)
data3 = np.random.chisquare(df=df3, size=1000)

# Create a figure with subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=True)

# Plotting the histograms for each dataset
axes[0].hist(data1, bins=50, color='skyblue', edgecolor='black', alpha=0.7)
axes[0].set_title(f'Chi-Square Distribution (df={df1})', fontsize=14)
axes[0].set_xlabel('Value', fontsize=12)
axes[0].set_ylabel('Frequency', fontsize=12)
axes[0].grid(True, linestyle='--', alpha=0.6)

axes[1].hist(data2, bins=50, color='lightgreen', edgecolor='black', alpha=0.7)
axes[1].set_title(f'Chi-Square Distribution (df={df2})', fontsize=14)
axes[1].set_xlabel('Value', fontsize=12)
axes[1].grid(True, linestyle='--', alpha=0.6)

axes[2].hist(data3, bins=50, color='salmon', edgecolor='black', alpha=0.7)
axes[2].set_title(f'Chi-Square Distribution (df={df3})', fontsize=14)
axes[2].set_xlabel('Value', fontsize=12)
axes[2].grid(True, linestyle='--', alpha=0.6)

# Adjust layout
plt.tight_layout()
plt.suptitle('Visualisasi Distribusi Chi-Square dengan Derajat Kebebasan yang Berbeda', fontsize=16, y=1.02)
plt.savefig('chi_square_distribution.png')

plt.show()