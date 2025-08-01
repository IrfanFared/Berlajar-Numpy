import numpy as np
import matplotlib.pyplot as plt
import random
a = np.random.multinomial(100 , pvals=[1/2,1/2] ,size=[2,3])
print(a)