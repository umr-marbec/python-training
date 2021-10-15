# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
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

# # Working with NEMO files
#
# Here are some examples for plotting outputs on a NEMO grid. 
#
# ## Building variable
#
# Let's first build a bathymetric field using the vertical scale factors.

# +
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import cartopy.feature as cfeature
import cartopy.crs as ccrs

data = xr.open_dataset('data/mesh_mask_eORCA1_v2.2.nc')
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

fig = plt.figure(figsize=(12, 15))
ax = plt.axes(projection=ccrs.PlateCarree())
cs = ax.pcolormesh(lon, lat, bathy, transform=ccrs.PlateCarree())
ax.add_feature(cfeature.LAND, zorder=50)
ax.add_feature(cfeature.COASTLINE, zorder=51)
cb = plt.colorbar(cs, shrink=0.3)

# We have an error message saying that the longitudes and latitudes are not monotonic. Let's improve our figure.

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
ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=0))
cs = ax.pcolormesh(lonf, latf, bathy[1:, 1:], transform=ccrs.PlateCarree(), shading='flat')
ax.set_extent([-20, 20, -20, 20], crs=ccrs.PlateCarree())
ax.add_feature(cfeature.COASTLINE, zorder=2)
ax.add_feature(cfeature.LAND, zorder=1)
cb = plt.colorbar(cs, shrink=0.5)

# ## Contour plots

# However, the  drawing of contour plots is not simple on irregular grid. Instead, we need to use the
# `tricontour` method, as indicated [here](https://matplotlib.org/stable/gallery/images_contours_and_fields/irregulardatagrid.html). 

# First, we recover the coordinates on the `T` points, not on the `F` points as for `pcolormesh`.

lont = data['glamt'].data
latt = data['gphit'].data

# Then, we extract the data mask.

mask = (np.ma.getmaskarray(bathy))

# Now, we extract the bathy, longitudes and latitudes on wet points and we convert into 1D arrays:

lon1d = np.ravel(lont[~mask])
lat1d = np.ravel(latt[~mask])
bat1d = np.ravel(bathy[~mask])
bat1d

# The next step is to convert our 1D geographical coordinates (lon/lat) into the coordinates of the output map. If we want to draw our contours on a Mollweide projection:

# +
projin = ccrs.PlateCarree()
projout = ccrs.Mollweide(central_longitude=180)
#projout = ccrs.PlateCarree(central_longitude=0)

output = projout.transform_points(projin, lon1d, lat1d)
lonout = output[..., 0]
latout = output[..., 1]
latout.shape
# -

# Now, we can add contours using the `tricontour` method:

fig = plt.figure(figsize=(12, 12))
ax = plt.axes(projection=projout)
cs = ax.pcolormesh(lonf, latf, bathy[1:, 1:], transform=projin)
cl = ax.tricontour(lonout, latout, bat1d, levels=np.arange(0, 6000 + 1000, 1000), colors='k', linewidths=0.5)
ax.add_feature(cfeature.LAND, zorder=100)
l = ax.add_feature(cfeature.COASTLINE, zorder=101, linewidth=2)