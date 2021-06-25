# ---
# jupyter:
#   jupytext:
#     formats: py:light,ipynb
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Quiver plots
#
# Quiver plots are obtained by using the [quiver](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.quiver.html) function.

# +
import scipy.io.netcdf as nc
import numpy as np
import matplotlib.pyplot as plt

f = nc.netcdf_file('../io/data/UV500storm.nc', mmap=False)
u = f.variables['u'][0]
v = f.variables['v'][0]
u = np.ma.masked_where(np.abs(u)>=999, u)
v = np.ma.masked_where(np.abs(v)>=999, v)
x = f.variables['lon'][:]
y = f.variables['lat'][:]
vel = np.sqrt(u*u + v*v, where=(np.ma.getmaskarray(u) == False))

f.close()
# -

# ## Using colormap

plt.figure()
q = plt.quiver(x, y, u, v, vel, cmap=plt.cm.get_cmap('hsv'), scale=1000)
q.set_clim(0, 50)
cb = plt.colorbar(q)
cb.set_label('Wind speed (m/s)')
plt.show()

# ## Using reference arrow
#
# Adding a reference arrow is done by using the [quiverkey](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.quiverkey.html) function

plt.figure()
q = plt.quiver(x, y, u, v, scale=1000)
keys = plt.quiverkey(q, -131, 21, 70, 'Wind speed\n(50 m/s)', coordinates='data')
plt.show()
