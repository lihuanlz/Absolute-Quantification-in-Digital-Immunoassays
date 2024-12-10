"""Created on Thu Nov 28 13:39:27 2024@author: lihuan"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


N = 2000000
Ms = 100000
error_limit = 0.1



N_values = np.logspace(np.log10(1), np.log10(N), num=250,dtype=int)
M_N_ratios = np.logspace(np.log10(1/N), np.log10(int(-np.log(1/N))), num=250)


data_list = []


for N in N_values:
    
    for M_N_ratio in M_N_ratios:
        M = M_N_ratio * N  
        if M > 0 and (Ms/N) > 0:  
            C1 = (1 - np.exp(-M / N)) / (1 - np.exp(-Ms / N))
            C2 = M / Ms
            relative_error = np.abs((C1 - C2) / C2)
            
            if relative_error < error_limit:
                data_list.append({'N': N, 'M_N_ratio': M_N_ratio,  'relative_error': relative_error})


df = pd.DataFrame(data_list)


grid_df = df.pivot_table(index='N', columns='M_N_ratio', values='relative_error', aggfunc='min')

X, Y = np.meshgrid(grid_df.columns, grid_df.index)
Z = grid_df.values

plt.figure(figsize=(10, 8))
contour_filled = plt.contourf(X, Y, Z, levels=100, cmap='viridis', fontsize=15)
plt.colorbar(contour_filled)

contour_lines = plt.contour(X, Y, Z, levels=[0.05, 0.1], colors=['blue', 'red'], linewidths=2)  




plt.xlabel('M/N ratio', fontsize=15)
plt.ylabel('N', fontsize=15)
plt.title(f'Relative Error Contour Plot\nError Limit = {error_limit},Ms={Ms}', fontsize=15)
plt.xscale('log')


plt.xticks(fontsize=15)
plt.yticks(fontsize=15)







plt.savefig('figure S7B.png', dpi=600)
plt.show()


df.to_csv('5_6relative_error_data.csv', index=False)
