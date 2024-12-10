
"""
Created on Mon Nov  4 15:35:12 2024

@author: lihuan
"""

import pandas as pd
import numpy as np
from scipy.interpolate import LinearNDInterpolator, NearestNDInterpolator
from skimage.measure import marching_cubes
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


filename = '8_Ms_n_N_M_N_data.csv'
data = pd.read_csv(filename)


Ms = data['Ms'].values
postive_ratio = data['postive_ratio'].values
n_N = data['n_N_ratio'].values
relative_error = data['relative_error'].values


x = np.log10(postive_ratio)
y = np.log10(n_N)
z = np.log10(Ms)


xi = np.linspace(np.min(x), np.max(x), 5)
yi = np.linspace(np.min(y), np.max(y), 5)
zi = np.linspace(np.min(z), np.max(z), 5)
xGrid, yGrid, zGrid = np.meshgrid(xi, yi, zi, indexing='ij')


points = np.column_stack((x, y, z))
values = relative_error


F_linear = LinearNDInterpolator(points, values)
vGrid_linear = F_linear(xGrid, yGrid, zGrid)


F_nearest = NearestNDInterpolator(points, values)
vGrid_nearest = F_nearest(xGrid, yGrid, zGrid)


vGrid = np.where(np.isnan(vGrid_linear), vGrid_nearest, vGrid_linear)


isosurface_value = 0.1  



vGrid_t = np.transpose(vGrid, (2, 1, 0))


verts, faces, normals, values = marching_cubes(vGrid_t, isosurface_value, spacing=(zi[1]-zi[0], yi[1]-yi[0], xi[1]-xi[0]))


verts[:, 0] += xi[0]
verts[:, 1] += yi[0]
verts[:, 2] += zi[0]



fig = plt.figure(figsize=(11, 9))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(x, y, z, c=relative_error, cmap='viridis', alpha=1)



cbar = plt.colorbar(sc, ax=ax, fraction=0.02, pad=0.01)


label_fontsize = 15
title_fontsize = 20
cbar_label_fontsize = 15
tick_fontsize = 15  

cbar.set_label('CV', fontsize=cbar_label_fontsize)
ax.set_xlabel('log10(postive %)', labelpad=10, fontsize=label_fontsize)
ax.set_ylabel('log10(n/N)', labelpad=10, fontsize=label_fontsize)
ax.set_zlabel('log10(Ms)', labelpad=10, fontsize=label_fontsize)
ax.set_title('3D Scatter Plot with Colors Representing CV', fontsize=title_fontsize)


cbar.ax.tick_params(labelsize=tick_fontsize)


ax.tick_params(axis='both', which='major', labelsize=tick_fontsize)
ax.tick_params(axis='z', which='major', labelsize=tick_fontsize)

ax.view_init(elev=30, azim=-135)


fig.tight_layout()


dpi_value = 300

plt.savefig('figure 3C Extended Data Figure 5.png', dpi=dpi_value)  
plt.show()









