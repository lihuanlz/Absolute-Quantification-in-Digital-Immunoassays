"""Created on Thu Nov 28 13:39:27 2024@author: lihuan"""
import numpy as np
from scipy.stats import hypergeom, binom, stats
import pandas as pd
import scipy.stats as stats

def calculate_confidence_interval(N, n, k):
    
    K_values = np.arange(k, N - (n - k) + 1)

    
    pmf_values = hypergeom.pmf(k, N, K_values, n)

    
    pmf_values /= pmf_values.sum()

    
    cdf_values = np.cumsum(pmf_values)

    
    lower_bound = K_values[np.searchsorted(cdf_values, 0.025)]
    upper_bound = K_values[np.searchsorted(cdf_values, 0.975)]

    return lower_bound, upper_bound


N_values = [2000000, 2000000, 2000000, 2000000, 2000000, 2000000, 2000000, 2000000]
n_values = [183179, 193957, 322161, 265841, 322641, 264575, 328909, 400055]
k_values = [90239, 23398, 4340, 581, 191, 153, 164, 145]


assert len(N_values) == len(n_values) == len(k_values), "N, n, k 列表的长度不一致！"


results = []


for N, n, k in zip(N_values, n_values, k_values):
    lower_bound, upper_bound = calculate_confidence_interval(N, n, k)
    results.append((N, n, k, lower_bound, upper_bound))

    
    print(f"N={N}, n={n}, k={k} => 95% 置信区间为 [{lower_bound}, {upper_bound}]")


df = pd.DataFrame(results, columns=["N", "n", "k", "Lower Bound", "Upper Bound"])


df["n/N"] = df["n"] / df["N"]


df.to_csv("confidence_intervals_with_ratios.csv", index=False)
print("计算完成，结果已保存到 'confidence_intervals_with_ratios.csv' 文件中。")


df = pd.read_csv('confidence_intervals_with_ratios.csv')


alpha = 0.05  


final_lower_list = []
final_upper_list = []


for index, row in df.iterrows():
    
    N = row['N']  

    lower_bound = row['Lower Bound']
    upper_bound = row['Upper Bound']

    
    lower_bound_events = lower_bound / N
    upper_bound_events = upper_bound / N

    
    
    



    lower_bound_lower = stats.beta.ppf(alpha / 2, lower_bound, N - lower_bound + 1)
    lower_bound_upper = stats.beta.ppf(1 - alpha / 2, lower_bound + 1, N - lower_bound)

    
    



    
    
    
    
    upper_bound_lower = stats.beta.ppf(alpha / 2, upper_bound, N - upper_bound + 1)
    upper_bound_upper = stats.beta.ppf(1 - alpha / 2, upper_bound + 1, N - upper_bound)
    
    print("lower_bound_lower:", lower_bound_lower)
    print("lower_bound_upper:", lower_bound_upper)
    print("upper_bound_lower:", upper_bound_lower)
    print("upper_bound_upper:", upper_bound_upper)
    
    
    final_lower = -np.log(1-lower_bound_lower)
    final_upper = -np.log(1-upper_bound_upper)

    final_lower_list.append(final_lower)
    final_upper_list.append(final_upper)


df['final_lambda_lower'] = final_lower_list
df['final_lambda_upper'] = final_upper_list


df.to_csv('updated_confidence_intervals.csv', index=False)


print(df.head())
