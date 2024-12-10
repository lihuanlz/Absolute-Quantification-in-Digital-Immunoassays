
"""
Created on Mon Nov 25 10:34:14 2024

@author: lihuan
"""

import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.interpolate import griddata

import math

def calculate_max_balls_on_sphere(big_radius, small_radius):
    max_balls = (4 * math.pi * big_radius ** 2) / (3 * small_radius ** 2)
    return max_balls








magnetic_beads = 2000000  
N = (magnetic_beads)

Y = 100000   

error_limit =0.2

n_values = np.logspace(np.log10(1), np.log10(N-1), num=200)


postive_ratios = np.logspace(np.log10(1/N), np.log10(1-1/N), num=200)

results = []

for postive_ratio in postive_ratios:
    M = int(postive_ratio * N)  
    for n in n_values:
        
        M_mean = postive_ratio * n
        M_std = np.sqrt(n * postive_ratio * (1 - postive_ratio) * (N - n) / (N - 1))
        
        Y_mean = Y/N * n
        Y_std = np.sqrt(n * Y/N * (1 - Y/N) * (N - n) / (N - 1))
        
        
        if Y_mean == 0 or M_mean == 0:
            relative_error = np.nan
        else:
                    
            relative_error = np.sqrt((M_std/M_mean)**2 + (Y_std/Y_mean)**2+M_mean**(-1)+Y_mean**(-1))         
            
     
        if relative_error < error_limit:
            results.append((postive_ratio, n / N, relative_error))



postive_ratios, n_N_values, relative_errors = zip(*results)


postive_ratios = -np.log(1 - np.array(postive_ratios))
lambda_values = postive_ratios
print (postive_ratios)



csv_filename = '6_5sampling_results_log_range_M_N_filtered2.csv'
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['postive_ratio', 'n / N', 'postive_ratios', 'relative_error'])  
    
    for result, lambda_value in zip(results, postive_ratios):
        writer.writerow([result[0], result[1], lambda_value, result[2]])

print(f'Results written to {csv_filename}')




grid_M_N, grid_n_N = np.meshgrid(np.unique(postive_ratios), np.unique(n_N_values))


grid_relative_errors = griddata((postive_ratios, n_N_values), relative_errors, (grid_M_N, grid_n_N), method='cubic')


plt.figure(figsize=(10, 8))
cp = plt.contourf(grid_M_N, grid_n_N, grid_relative_errors, levels=np.linspace(np.nanmin(grid_relative_errors), np.nanmax(grid_relative_errors), num=50), cmap='viridis')
plt.colorbar(cp)  

contours = plt.contour(grid_M_N, grid_n_N, grid_relative_errors, levels=[0.05,0.1], colors='white')
plt.clabel(contours, inline=True, fontsize=15, fmt='     %1.2f')

N=int(N)
Y=int(Y)
plt.title(f'Relative Error Contour Plot (CV)\nN={N},Ms={Y}', fontsize=15)
plt.xlabel('λ', fontsize=15)
plt.ylabel('n/N', fontsize=15)
plt.xscale('log')




plt.axvline(x=131/N, color='red', linestyle='--', label='131/N')
plt.axvline(x=1.2404, color='red', linestyle='--', label='0.2146')


dpi_value = 300

plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.savefig('fugure 4.png', dpi=dpi_value)  

plt.show()
