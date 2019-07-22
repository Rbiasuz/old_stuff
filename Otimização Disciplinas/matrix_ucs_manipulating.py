import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
import pandas as pd

matrix = pd.read_csv("comp_matriz.csv", header=None, index_col=None, delimiter=',', engine='python')

def zerar(x):
    if x < 0.70:
        y = 0
        return y
    else:
        return x

matrix = matrix.applymap(zerar)

A = np.asarray(matrix)
x,y = A.nonzero()

plt.scatter(x,y,c=A[x,y],s=10,cmap='rainbow',marker='*') #adjust the size to your needs
plt.colorbar()
plt.show()

# fig, ax = plt.subplots(num=None, figsize=(10, 10), facecolor='w', edgecolor='k')
# ax = sns.heatmap(matrix, cmap='magma', yticklabels=800,  xticklabels=800, vmin=0, vmax=1, center=0.4)
