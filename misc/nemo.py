# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Working with NEMO files
#
# Here are some examples for plotting outputs on a NEMO grid. 
#
# ## Building variable
#
# Let's first build a bathymetric field using the vertical scale factors: 

# +
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import cartopy.feature as cfeature
import cartopy.crs as ccrs
from matplotlib.axes import Axes
from cartopy.mpl.geoaxes import GeoAxes

data = xr.open_dataset('data/mesh_mask_eORCA1_v2.2.nc')
data.coords["x"] = range(data.dims["x"])
data.coords["y"] = range(data.dims["y"])
data = data.isel(t=0)
tmask = data['tmask'].values
e3t = data['e3t_0'].values
lon = data['glamt'].values
lat = data['gphit'].values

bathy = np.sum(e3t * tmask, axis=0)
bathy = np.ma.masked_where(bathy == 0, bathy)
# -

# ## First try
#
# If we first try to use the `pcolormesh` as we learned, here is what comes out:

fig = plt.figure()
ax = plt.axes(projection=ccrs.PlateCarree())
cs = ax.pcolormesh(lon, lat, bathy, transform=ccrs.PlateCarree())
ax.add_feature(cfeature.LAND, zorder=50)
ax.add_feature(cfeature.COASTLINE, zorder=51)
cb = plt.colorbar(cs, shrink=0.5)

# We have an error message saying that the longitudes and latitudes are not monotonic. It says that corners coordinates should be given instead. And the figure is bad.

# ##  Better way
#
# As indicated in [the documentation](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.pcolormesh.html), the `pcolormesh` method assumes the following layout:
#
# ```
# (X[i+1, j], Y[i+1, j])          (X[i+1, j+1], Y[i+1, j+1])
#                       +--------+
#                       | C[i,j] |
#                       +--------+
#     (X[i, j], Y[i, j])          (X[i, j+1], Y[i, j+1])
# ```
#
# Therefore, the good way to draw is to provide the coordinates of the `F` points (upper-right corners), and to give a sub-array of `T` points.
#
# **Grid layout of NEMO outputs:**
#
# <img src="figs/nemo-index.png" width="30%">

lonf = data['glamf'].data
latf = data['gphif'].data
fig = plt.figure()
ax = plt.gca(projection=ccrs.PlateCarree(central_longitude=0))
cs = ax.pcolormesh(lonf, latf, bathy[1:, 1:], transform=ccrs.PlateCarree(), shading='flat')
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.COASTLINE)
cb = plt.colorbar(cs, shrink=0.5)


