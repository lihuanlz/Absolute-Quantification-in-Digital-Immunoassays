"""Created on Thu Nov 28 13:39:27 2024@author: lihuan"""
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.interpolate import griddata


N = 2000000  

Ms = 100000   

Ms_postive_ratio = 1 - np.exp(-Ms/N)
error_limit =0.2

n_values = np.logspace(np.log10(1), np.log10(N-1), num=500, dtype=int)


postive_ratios = np.logspace(np.log10(1/N), np.log10(1-1/N), num=500)

results = []

for postive_ratio in postive_ratios:
    M = int(postive_ratio * N)  
    for n in n_values:
        
        M_mean = postive_ratio * n
        M_std = np.sqrt(n * postive_ratio * (1 - postive_ratio) * (N - n) / (N - 1))
        
        Ms_mean = Ms_postive_ratio * n
        Ms_std = np.sqrt(n * Ms_postive_ratio * (1 - Ms_postive_ratio) * (N - n) / (N - 1))
        
        
        if Ms_mean == 0 or M_mean == 0:
            relative_error = np.nan
        else:
            relative_error = np.sqrt((M_std/M_mean)**2 + (Ms_std/Ms_mean)**2)          
            

        
        if relative_error < error_limit:
            results.append((postive_ratio, n / N, relative_error))


csv_filename = '6_5sampling_results_log_range_M_N_filtered2.csv'
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['postive_ratio', 'n / N', 'relative_error'])
    writer.writerows(results)

print(f'Results written to {csv_filename}')


postive_ratios, n_N_values, relative_errors = zip(*results)


grid_M_N, grid_n_N = np.meshgrid(np.unique(postive_ratios), np.unique(n_N_values))


grid_relative_errors = griddata((postive_ratios, n_N_values), relative_errors, (grid_M_N, grid_n_N), method='cubic')


plt.figure(figsize=(10, 8))
cp = plt.contourf(grid_M_N, grid_n_N, grid_relative_errors, levels=np.linspace(np.nanmin(grid_relative_errors), np.nanmax(grid_relative_errors), num=50), cmap='viridis')
plt.colorbar(cp)  





contours = plt.contour(grid_M_N, grid_n_N, grid_relative_errors, levels=[0.05, 0.1], colors=['blue', 'red'], linewidths=2)  




plt.clabel(contours, inline=True, fontsize=15, fmt='     %1.2f')

N=int(N)
Ms=int(Ms)
plt.title(f'Relative Error Contour Plot (CV)\nN={N},Ms={Ms}', fontsize=15)
plt.xlabel('postive %', fontsize=15)
plt.ylabel('n/N', fontsize=15)
plt.xscale('log')








dpi_value = 600

plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.savefig('Figure S8.png', dpi=dpi_value)  

plt.show()
