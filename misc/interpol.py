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

# # Data interpolation
#
# Data interpolation is achieved by using the [xesmf](https://xesmf.readthedocs.io/en/latest/) library.
#
# It works easily with `xarray` and `dask` and therefore can manage parallel computation. As a start, let's try to interpolate our global `SST` temperature from the ORCA grid to a regular one.
#
# ## Reading of the SST

# +
import xarray as xr
import numpy as np
import xesmf as xe

data = xr.open_dataset("data/surface_thetao.nc")
data = data['thetao']
data
# -

# ## Initialisation of the output grid
#
# Then, a `Dataset` object that contains the output grid must be created

dsout = xr.Dataset()
dsout['lon'] = (['lon'], np.arange(-179, 179 + 1))
dsout['lat'] = (['lat'], np.arange(-89, 89 + 1))
dsout

# ## Renaming the input coordinates
#
# We also need to insure that the coordinates variables have the same names.

data = data.rename({'nav_lon' : 'lon', 'nav_lat' : 'lat'})
data

# ## Creating the interpolator
#
# When this is done, the interpolator object can be created as follows:

regridder = xe.Regridder(data, dsout, 'bilinear', ignore_degenerate=True, reuse_weights=False, periodic=True, filename='weights.nc')
regridder

# Note that the `ignore_degenerate` argument is necessary for handling the ORCA grid.
#
# ## Interpolating the data set

dataout = regridder(data)

# ## Comparing the results
#
# Let's display the original SST values for the first time-step

# +
import matplotlib.pyplot as plt

mesh = xr.open_dataset("data/mesh_mask_eORCA1_v2.2.nc")
lonf = mesh['glamf'].data[0]
latf = mesh['gphif'].data[0]

toplot = data.isel(time_counter=0, olevel=0).data
cs = plt.pcolormesh(lonf, latf, toplot[1:, 1:], cmap=plt.cm.jet)
cs.set_clim(-2, 30)
# -

toplot = dataout.isel(time_counter=0, olevel=0).data
cs = plt.pcolormesh(dataout['lon'], dataout['lat'], toplot[1:, 1:], cmap=plt.cm.jet)
cs.set_clim(-2, 30)
