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
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Computation of global mean SST
#
# In this example, we illustrate possible bad choices of chunk when computing horizontal mean SST time-series and time-average SST.

# # Extraction of data
#
# First, the SST data is extracted, as well as the cell surfaces.

from dask.diagnostics import Profiler, ResourceProfiler, CacheProfiler, visualize
import xarray as xr
import matplotlib.pyplot as plt

data = xr.open_dataset('data/surface_thetao.nc')
data = data.isel(olevel=0)

mesh = xr.open_dataset('data/mesh_mask_eORCA1_v2.2.nc')
mesh = mesh.isel(z=0, t=0)

surface = mesh['e2t'] * mesh['e1t']
surface

# ## Bad choice of chunks
#
# First, let's make a try by divinding our dataset into tiles:

chunk = {'x': 150, 'y':100}
thetao = data['thetao'].chunk(chunk)
thetao

# The surface array is also decomposed into the same chunks

surfbis = surface.chunk(chunk)
surfbis

# Now, the mean time-series is computing by weighting using the cell surface:

tmean = (thetao * surfbis).sum(dim=['x', 'y']) / surfbis.sum(dim=['x', 'y'])

# %%time
with Profiler() as prof, ResourceProfiler(dt=0.25) as rprof, CacheProfiler() as cprof:
    tmean.compute()

visualize([prof, rprof, cprof], show=False)

tmean.data.visualize()

l = tmean.plot()

# Now, the time-average map is computed:

time_mean = thetao.mean(dim='time_counter')

# %%time
with Profiler() as prof, ResourceProfiler(dt=0.25) as rprof, CacheProfiler() as cprof:
    time_mean.compute()

visualize([prof, rprof, cprof], show=False)

time_mean.data.visualize()

l = time_mean.plot(robust=True, cmap=plt.cm.jet)

# ## Better choice of chunks
#
# The performance in the above are disappointing. This this due to a bad chunking choice. If the SST is now chunked along the time only.

chunk = {'time_counter': 70}
thetao = data['thetao'].chunk(chunk)
thetao

tmean = (thetao * surface).sum(dim=['x', 'y']) / surface.sum(dim=['x', 'y'])

# %%time
with Profiler() as prof, ResourceProfiler(dt=0.25) as rprof, CacheProfiler() as cprof:
    tmean.compute()

visualize([prof, rprof, cprof], show=False)

tmean.data.visualize()

l = tmean.plot()

time_mean = thetao.mean(dim='time_counter')

# %%time
with Profiler() as prof, ResourceProfiler(dt=0.25) as rprof, CacheProfiler() as cprof:
    time_mean.compute()

visualize([prof, rprof, cprof], show=False)

time_mean.data.visualize()

l = time_mean.plot(robust=True, cmap=plt.cm.jet)


