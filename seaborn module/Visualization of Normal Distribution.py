import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random

sns.displot(random.normal(size=1000),kind="kde")

plt.show()