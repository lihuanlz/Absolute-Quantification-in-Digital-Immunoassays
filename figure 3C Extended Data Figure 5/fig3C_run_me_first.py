"""Created on Thu Nov 28 13:39:27 2024@author: lihuan"""
import numpy as np
import csv


N = 2000000  
error_up_limit = 0.15  

n_values = np.logspace(np.log10(1), np.log10(N), num=100)
pos_Ms_values = np.logspace(np.log10(1), np.log10(N-1), num=100)      
postive_ratios = np.logspace(np.log10(1/N), np.log10(1-1/N), num=100)

results = []

for postive_ratio in postive_ratios:
    
    for n in n_values:
        for pos_Ms in pos_Ms_values:
            
            Ms = pos_Ms
            
            
            Ms_mean = pos_Ms / N * n
            Ms_std = np.sqrt(n * (pos_Ms / N) * (1 - pos_Ms / N) * (N - n) / (N - 1))
            
            
            M_mean = postive_ratio * n
            M_std = np.sqrt(n * postive_ratio * (1 - postive_ratio) * (N - n) / (N - 1))
            
            
            if Ms_mean == 0 or M_mean == 0:
                relative_error = np.nan
            else:
                
                relative_error = np.sqrt((M_std/M_mean)**2 + (Ms_std/Ms_mean)**2+M_mean**-1+Ms_mean**-1)         
            
            if relative_error < error_up_limit:
                results.append((Ms, postive_ratio, n / N, relative_error))


csv_filename = '8_Ms_n_N_M_N_data.csv'
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Ms', 'postive_ratio', 'n_N_ratio', 'relative_error'])
    writer.writerows(results)
