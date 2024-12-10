# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 20:26:26 2024

@author: lihuan
"""
import numpy as np
import matplotlib.pyplot as plt
import math
import csv



magnetic_beads = 500000  
error_up_limit = 0.1  

N=magnetic_beads


def calculate_cv(N, K, n):
    return np.sqrt(((1 - K / N) * ((N - n) / (N - 1))) / (n * (K / N)))


N_values = np.logspace(0, np.log10(N), num=100)
K_values = np.logspace(0, np.log10(N), num=100)
n_values = np.logspace(0, np.log10(N), num=100)


min_n_values = np.zeros((len(N_values), len(K_values)))


for i, N in enumerate(N_values):
    for j, K in enumerate(K_values):
        if K <= N:  
            for n in n_values:
                min_cv = calculate_cv(N, K, n)
                if min_cv <= error_up_limit:
                    min_n_values[i, j] = n
                    break


with open('min_n_values.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['N', 'K', 'min_n'])
    for i in range(len(N_values)):
        for j in range(len(K_values)):
            if K_values[j] <= N_values[i]:
                csvwriter.writerow([N_values[i], K_values[j], min_n_values[i, j]])


plt.figure(figsize=(8, 6))

N_grid, K_grid = np.meshgrid(N_values, K_values)
contour = plt.contourf(N_grid, K_grid, np.log10(min_n_values.T), levels=20, cmap='viridis')


cbar = plt.colorbar(contour)
cbar.set_label('Minimum log(n)', fontsize=15)  
plt.xlabel('N', fontsize=15)
plt.ylabel('K', fontsize=15)

plt.xscale('log')
plt.yscale('log')

plt.title(f'Minimum n\nCV={error_up_limit*100}% Nmax={(magnetic_beads)}', fontsize=15)

dpi_value = 300
plt.savefig('figure 1B and Extended Data Figure 1B.png', dpi=dpi_value, bbox_inches='tight', pad_inches=0)  

plt.show()
