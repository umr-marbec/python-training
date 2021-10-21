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

# # Practical session on `xarray`
#
# ## Instructions

# - Load the `python-training/misc/data/mesh_mask_eORCA1_v2.2.nc` file using `open_dataset`.

# - Extract the surface (`z=0`) and first time step (`t=0`) using `isel`

# - Plot the land-sea mask (`tmask`) variable.

# - Compute the cell surface (`e1t x e2t`)

# - Load the `python-training/misc/data/surface_thato.nc` file using `open_dataset`.

# - Extract the SST (`thetao` variable) at the surface (`olevel=0`)

# - Compute and display the time-average SST

# - Compute the mean SST over years 1958-1962

# - Compute the mean over years 2014-2018

# - Plot the SST difference between 2018-2014 and 1958-1962

# - Compute the SST global mean time-series (weight by cell surface $e1t \times e2t$)

# - Remove the monthly clim from the time-series using `groupy` on `time_counter.month`

# - Compute the rolling mean of the time-series, using a 3-year window. Plot the raw and smoothed anomalies

# ## Corrections

# - Load the `python-training/misc/data/mesh_mask_eORCA1_v2.2.nc` file using `open_dataset`.

# +
import xarray as xr

mesh = xr.open_dataset('data/mesh_mask_eORCA1_v2.2.nc')
mesh
# -

# - Extract the surface (`z=0`) and first time step (`t=0`) using `isel`

mesh = mesh.isel(z=0, t=0)
mesh

# - Plot the land-sea mask (`tmask`) variable.

tmask = mesh['tmask']
tmask.plot()

# - Compute the cell surface (`e1t x e2t`)

surface = mesh['e1t'] * mesh['e2t']
surface

# Here the output DatarArray has no name. You can give him one as follows:

surface.name = 'surface'
surface

# - Load the `python-training/misc/data/surface_thato.nc` file using `open_dataset`.

data = xr.open_dataset('data/surface_thetao.nc')
data

# - Extract the SST (`thetao` variable) at the surface (`olevel=0`)

thetao = data['thetao'].isel(olevel=0)
thetao

# - Compute and display the time-average SST

# +
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = False

theta_mean = thetao.mean(dim='time_counter')
theta_mean.plot(robust=True, cmap=plt.cm.jet)
# -

# - Compute the mean SST over years 1958-1962

sst_early = thetao.sel(time_counter=slice('1958-01-01', '1962-12-31')).mean(dim='time_counter')
sst_early

# - Compute the mean over years 2014-2018

sst_late = thetao.sel(time_counter=slice('2014-01-01', '2018-12-31')).mean(dim='time_counter')
sst_late

# - Plot the SST difference between 2014-2018 and 1958-1962

(sst_late - sst_early).plot(robust=True)

# - Compute the SST global mean time-series (weight by cell surface $e1t \times e2t$)

# A first possibility would be to compute it using `sum`:

ts1 = (thetao * surface * tmask).sum(dim=['x', 'y']) / ((surface * tmask).sum(dim=['x', 'y']))
ts1.plot()

# Another solution would be to use the `xarray.weight` method:

theta_weighted = thetao.weighted(surface * tmask)
ts2 = theta_weighted.mean(dim=['x', 'y'])
ts2.plot()

# - Remove the monthly clim from the time-series using `groupy` on `time_counter.month`

clim = ts1.groupby('time_counter.month').mean(dim='time_counter')
clim.plot()

anom = ts1.groupby('time_counter.month') - clim
anom.plot()

# - Compute the rolling mean of the time-series, using a 3-year window. Plot the raw and smoothed anomalies

tsroll = anom.rolling(time_counter=3*12 + 1, center=True).mean(dim='time_counter').dropna('time_counter')
tsroll

anom.plot(label='raw')
tsroll.plot(label='smoothed')
