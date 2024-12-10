"""Created on Thu Nov 28 13:39:27 2024@author: lihuan"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

N = 2000000
λ1 = 131 / N

λ2 = 1.2040


x1 = (1 - np.exp(-λ1))*100

x3 = (1 - np.exp(-λ2))*100


CV_1 = 0.1

CV_2 = 0.05

ratios = np.logspace(np.log10(1 / N), np.log10((N - 1) / N), 50)


def calculate_min_n_and_kn_ratio_product(CV, ratios, N):
    results = {}
    for ratio in ratios:
        K = int(N * ratio)  
        
        for n in range(1, N + 1):
            
            
            left_side = CV  
            right_side = math.sqrt((N / (n * K)) * (1 - (K / N)) * ((N - n) / (N - 1)) + (1 / K))  
            if left_side > right_side:
                results[ratio] = n  
                break  
    
    ratios_list = list(results.keys())
    min_n_list = list(results.values())  
    min_n_percent_list = [n / N * 100 for n in min_n_list]  
    return ratios_list, min_n_list, min_n_percent_list


ratios_list_1, min_n_list_1, min_n_percent_list_1 = calculate_min_n_and_kn_ratio_product(CV_1, ratios, N)
kn_ratio_product_1 = [r * k for r, k in zip(ratios_list_1, min_n_list_1)]


ratios_list_2, min_n_list_2, min_n_percent_list_2 = calculate_min_n_and_kn_ratio_product(CV_2, ratios, N)
kn_ratio_product_2 = [r * k for r, k in zip(ratios_list_2, min_n_list_2)]


fig, ax1 = plt.subplots(figsize=(7, 8))


ratios_percentage1 = [r * 100 for r in ratios_list_1]  
ax1.plot(ratios_percentage1, min_n_percent_list_1, '-o', color='tab:blue', label=f'Minimum n/N (%) - CV={CV_1*100}%')


ratios_percentage2 = [r * 100 for r in ratios_list_2]  

ax1.plot(ratios_percentage2, min_n_percent_list_2, '-o', color='tab:orange', label=f'Minimum n/N (%) - CV={CV_2*100}%')

ax1.set_xlabel('K/N%', fontsize=25)
plt.xticks(fontsize=20)

ax1.set_xscale('log')
ax1.set_ylabel('Minimum n/N (%)', color='black', fontsize=25)
ax1.tick_params(axis='y', labelcolor='black')
plt.yticks(fontsize=20)















ax1.axvline(x=x1, color='gray', linestyle='--', label=f'λ1 = 131/N')

ax1.axvline(x=x3, color='green', linestyle='--', label=f'λ2 = {λ2}')


plt.title(f'Minimum n/N (%) vs K/N%\nMinimum k vs K/N%\nN={N} at CV={CV_1 * 100}% and {CV_2 * 100}%', fontsize=20)


dpi_value = 300
fig.tight_layout()  






fig.tight_layout(rect=[0, 0.2, 1, 1])  


ax1.legend(loc='upper right', fontsize=15, bbox_to_anchor=(0.55, -0.2), ncol=1)




confidence_intervals = pd.read_csv('updated_confidence_intervals.csv')



error_length = 4  





for _, row in confidence_intervals.iterrows():

    
    
    
    
    final_lambda_lower = row['final_lambda_lower']
    final_lambda_upper = row['final_lambda_upper']

    
    lower_bound = 1 - np.exp(-final_lambda_lower)
    upper_bound = 1 - np.exp(-final_lambda_upper)
    
    
    
    
    n_over_n = row['n/N']
    
    
    lower_bound_percentage = lower_bound * 100
    upper_bound_percentage = upper_bound * 100
    n_over_n_percentage = n_over_n * 100
    
    
    ax1.plot([lower_bound_percentage, lower_bound_percentage], [n_over_n_percentage - error_length / 2, n_over_n_percentage + error_length / 2], color='black', linestyle='-')
    ax1.plot([upper_bound_percentage, upper_bound_percentage], [n_over_n_percentage - error_length / 2, n_over_n_percentage + error_length / 2], color='black', linestyle='-')
    
    
    ax1.plot([lower_bound_percentage, upper_bound_percentage], [n_over_n_percentage, n_over_n_percentage], color='black', linestyle='-',alpha=0.8)







points_x2 = [ 
0.4926274300 ,
0.1206349861,
0.0134715251 ,
0.0021855169 ,
0.0005919892 ,
0.0005782859 ,
0.0004986182 ,
0.0003624502 
]  
points_y2 = [
9.15895,
9.69785,
16.10805,
13.29205,
16.13205,
13.22875,
16.44545,
20.00275
]  
ax1.plot([x * 100 for x in points_x2], points_y2, 'cx', markersize=10, alpha=1)  



plt.yticks(fontsize=20)

dpi_value = 300
fig.tight_layout()  

plt.savefig('figure 1 Ad and Extended Data Figure 1A.png', dpi=dpi_value)  

plt.show()






































































































































    
    
    
    






    
    
    
    

    




    



    















































































































































































































































































































































































































