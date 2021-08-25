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

from dask.diagnostics import Profiler, ResourceProfiler, CacheProfiler, visualize
import xarray as xr
from dask.diagnostics import visualize
import matplotlib.pyplot as plt

data = xr.open_dataset('data/surface_thetao.nc')
data = data.isel(olevel=0)

mesh = xr.open_dataset('data/mesh_mask_eORCA1_v2.2.nc')
mesh = mesh.isel(z=0, t=0)

volume = mesh['e2t'] * mesh['e3t_0'] * mesh['e1t']
volume

chunk = {'time_counter': 70}
#chunk = {'x': 150, 'y':100}
thetao = data['thetao'].chunk(chunk)
thetao

tmean = (thetao * volume).sum(dim=['x', 'y']) / volume.sum(dim=['x', 'y'])

# %%time
with Profiler() as prof, ResourceProfiler(dt=0.25) as rprof, CacheProfiler() as cprof:
    tmean.compute()

visualize([prof, rprof, cprof])

tmean.data.visualize()

l = tmean.plot()

#thetao = thetao.chunk({'time_counter': -1, 'x': 150, 'y': 100})
thetao

time_mean = thetao.mean(dim='time_counter')

# %%time
with Profiler() as prof, ResourceProfiler(dt=0.25) as rprof, CacheProfiler() as cprof:
    time_mean.compute()

visualize([prof, rprof, cprof])

time_mean.data.visualize()

l = time_mean.plot(robust=True, cmap=plt.cm.jet)


