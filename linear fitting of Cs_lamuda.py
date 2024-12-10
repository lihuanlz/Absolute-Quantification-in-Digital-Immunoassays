# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:57:43 2024
@author: lihuan
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 调整后的模型函数：C_s(λ') = a * (λ' - b)
def model(lambda_, a, b):
    return a * (lambda_ - b)

# 输入数据（假设 lambda_data 代表 λ' = λ + b）
lambda_data = np.array([0.0043,
0.005,
0.0098,
0.015,
0.11,
0.52,
1



], dtype=np.float64)
Cs_data = np.array([0,
0.1,
0.5,
1,
10,
50,
100
 

], dtype=np.float64)


# 使用 curve_fit 来拟合模型，得到参数 a 和 b
# popt, pcov = curve_fit(model, lambda_data, Cs_data)
popt, pcov = curve_fit(model, lambda_data, Cs_data, method='trf')

# 拟合得到的参数 popt[0] 和 popt[1] 就分别是 a 和 b 的最佳估计
a_fitted, b_fitted = popt

# 计算 R^2（决定系数）
# 首先计算拟合曲线的值
Cs_fitted = model(lambda_data, a_fitted, b_fitted)

# 计算总平方和 (Total Sum of Squares)
SS_tot = np.sum((Cs_data - np.mean(Cs_data))**2)

# 计算残差平方和 (Residual Sum of Squares)
SS_res = np.sum((Cs_data - Cs_fitted)**2)

# 计算 R^2
R2 = 1 - (SS_res / SS_tot)

# 打印拟合结果，使用高精度输出
print(f"拟合得到的方程形式: C_s(λ') = {a_fitted:.8f} * (λ' - {b_fitted:.8f})")
print(f"决定系数 R^2: {R2:.8f}")

# 可选：绘制拟合曲线与数据点
lambda_fine = np.linspace(min(lambda_data), max(lambda_data), 100)  # 生成细分的 λ' 数据
Cs_fitted_fine = model(lambda_fine, a_fitted, b_fitted)  # 计算拟合曲线的 C_s(λ')

plt.scatter(lambda_data, Cs_data, color='red', label='Data')
plt.plot(lambda_fine, Cs_fitted_fine, label='Fitted curve', color='blue')
plt.xlabel('λ\'')
plt.ylabel('C_s(λ\')')
plt.legend()
plt.show()
