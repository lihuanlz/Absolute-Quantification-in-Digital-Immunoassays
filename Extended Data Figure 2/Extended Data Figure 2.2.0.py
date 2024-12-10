
"""Created on Thu Nov 28 13:39:27 2024@author: lihuan"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm  
from matplotlib.ticker import ScalarFormatter

Nmax = 2000000
N_values = np.logspace(1, np.log10(Nmax), num=100)
K_values = np.logspace(1, np.log10(Nmax-1), num=100)


K, N = np.meshgrid(K_values, N_values)


M = -N * np.log(1 - K / N)


plt.figure(figsize=(10, 8))



contour = plt.contourf(N, K, M, levels=np.logspace(np.log10(K.min()), np.log10(K.max()), num=20), cmap='viridis', norm=LogNorm())

cbar = plt.colorbar(contour)
cbar.set_label('M', fontsize=15)


ticks = np.logspace(np.log10(K.min()), np.log10(K.max()), num=10)
cbar.set_ticks(ticks)  


formatter = ScalarFormatter()
formatter.set_scientific(False)  
formatter.set_powerlimits((-1, 1))  


cbar.ax.yaxis.set_major_formatter(formatter)















dpi_value=300


plt.xticks(fontsize=15)
plt.yticks(fontsize=15)



plt.xscale('log')
plt.yscale('log')
plt.xlabel('N', fontsize=15)
plt.ylabel('K', fontsize=15)
plt.title(f'Relationship between M, N and K\nInitial Nmax={Nmax}', fontsize=15)


plt.savefig('Extended Data Figure 2A.png', dpi=dpi_value)  


plt.show()