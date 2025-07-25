import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

data_umur = random.randint(10,50,size= 45)

sns.displot(data_umur,kind="kde")

plt.show() #method ini digunakan untuk menvisuliasikan hasil