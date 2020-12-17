# ---
# jupyter:
#   jupytext:
#     formats: py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Scatter plots
#
# Scatter plots can be obtained by using the [scatter](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.scatter.html) method.

# +
import numpy as np
import pylab as plt

np.random.seed(seed=1)
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
z = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses
# -

# Scatter plots with the size as a function of data value
plt.figure()
plt.scatter(x, y, s=z, c='k')
plt.show()

# Scatter plots with color as a function of data value
plt.figure()
cs = plt.scatter(x, y, s=600, c=z, 
                 cmap=plt.cm.jet, alpha=0.5, marker='o')
plt.colorbar(cs)
plt.show()

# Scatter plots with color and size as a function of data value
plt.figure()
cs = plt.scatter(x, y, s=z, c=z, 
                 cmap=plt.cm.jet, alpha=0.5, marker='o')
plt.colorbar(cs)
plt.show()
