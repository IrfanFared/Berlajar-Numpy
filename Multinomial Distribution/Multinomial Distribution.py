"""
Multinomial Distribution adalah bentuk lebih cangih dari bilonimial yang dimana multibilonomial memliki lebih 2 -
kemungkinan sedang bilonominal memiliki 2 kemungkinan
di kehidupan sehari hari digunakan untuk menhitung peluang mata dadu menghasilkan 1,menghitungn tingkat kepuasan pelanggan,peluang suara pada partai

memiliki paramater tiga
-n jumlah percobaan
pvals probabiltas setiap individu
size mengbalikan nilai peluang dalam bentuk array
"""
import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for the multinomial distribution
n = 100  # Number of trials (e.g., total coin flips, dice rolls, etc.)
pvals = [0.2, 0.3, 0.5]  # Probabilities of each outcome (e.g., outcomes A, B, C)
num_experiments = 1000  # Number of times we run the experiment

# Simulate the multinomial distribution
# The result is an array where each row represents one experiment
# and the columns represent the counts for each outcome.
results = np.random.multinomial(n, pvals, size=num_experiments)

# To visualize, we can sum the results of all experiments to see the total counts
# for each outcome across all experiments.
total_counts = results.sum(axis=0)
outcomes = ['Outcome A', 'Outcome B', 'Outcome C']

# Create a bar chart of the results
plt.figure(figsize=(8, 6))
plt.bar(outcomes, total_counts, color=['skyblue', 'salmon', 'lightgreen'])
plt.title('Simulasi Distribusi Multinomial', fontsize=16)
plt.xlabel('Kategori Hasil', fontsize=12)
plt.ylabel('Jumlah Total', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the plot
plt.savefig('multinomial_distribution.png')

# Print the results for context
print(f"Hasil total dari {num_experiments} eksperimen dengan {n} percobaan:")
for i, outcome in enumerate(outcomes):
    print(f"  {outcome}: {total_counts[i]} kali")

plt.show()