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

# # Example of covariance using Dask
#
# In this Notebook, the use of Dask is parallel mode is illustrated in goal to compute lead-lag covariances.
#
# ## Import of data
#
# ### SST anomalies
#
# First, SST data are extracted.

# +
import matplotlib.pyplot as plt
import xarray as xr
import scipy.signal as sig
import numpy as np
import pandas as pd
from dask.diagnostics import Profiler, ResourceProfiler, CacheProfiler, visualize

data = xr.open_dataset('data/surface_thetao.nc')
data = data.isel(olevel=0)
data = data['thetao']
data
# -

# Then, monthly anomalies are computed:

clim = data.groupby('time_counter.month').mean(dim='time_counter')

anom = data.groupby('time_counter.month') - clim
anom

# ## Oni index
#
# Now, the ONI index is extracted from the CSV file.

nino = pd.read_csv('data/oni.data', skiprows=1, skipfooter=8, engine='python', header=None, index_col=0, delim_whitespace=True, na_values=-99.9)
nino

# It needs to be converted into 1D array. This is done by manipulating the years and columns

years = nino.index.values
years

months = nino.columns.values
months

mm, yy = np.meshgrid(months, years)
yy = np.ravel(yy)
mm = np.ravel(mm)
date = yy * 100 + mm
date

nino = np.ravel(nino.values)

# Now, we extract the values that correspond to the length of the SST time-series (1958-2018)

iok = np.nonzero((date >= 195801) & (date <= 201812))[0]
date[iok]

# Finally, the time-series is converted into a data arraty.

tmean = xr.DataArray(
    data = nino[iok],
    name = 'oni',
    coords={'time_counter' : data['time_counter']}
)
l = tmean.plot()
tmean

# ## First test on covariance analysis
#
# Here, the covariance is computed using numpy arrays.

nt, ny, nx = data.shape
nt, ny, nx

# Now, the correlation lags are extracted.

lags = sig.correlation_lags(nt, nt)
lags

# The index of the $0$-lag covariance is extracted.

izero = np.nonzero(lags == 0)[0][0]
izero

# Now, the covariance is computed by using a `for` loop using Numpy arrays.

# %%time
covariance = np.zeros((ny, nx, len(lags)))
dataval = anom.values # t, y, x
tmeanval = tmean.values
for s in range(ny):
    for i in range(nx):
        temp = dataval[:, s, i]
        covariance[s, i, :] = sig.correlate(temp, tmeanval) / nt
covariance.shape

cs = plt.pcolormesh(covariance[:, :, izero])
cs.set_clim(-1, 1)
plt.colorbar(cs)

# ## Using user-defined functions in parallel.
#
# To compute covariance in parallel mode, a function that works on Numpy arrays must be created. It basically does the same thing as in the above. Except that in this case, `time` becomes the rightmost dimension.

# +
import scipy.signal as sig
import numpy as np

def gufunc_cov(x, y):
    print("@@@@@@@@@@@@@@@@@@@@@@@@@ ", x.shape, y.shape)
    nx = x.shape[0]
    ny = x.shape[1]
    ntime = x.shape[-1]
    lags = sig.correlation_lags(ntime, ntime)
    nlags = len(lags)
    output = np.zeros((nx, ny, nlags))
    for s in range(nx):
        for i in range(ny):
            temp = x[s, i]
            output[s, i, :] = sig.correlate(temp, y)
    return output


# -

# Now that it is done, create a new method that returns a `xr.apply_ufunc` object. The first argument is the above function, the second argument is the SST `DataArray`, the third argument is the `Nino` index. The `input_core_dims` provides the names of the dimensions that will not be broadcasted (here, `time`). Since the `correlate` function returns an array of dimensions (`y, x, lags`), we need to specify the new lag dimension using the `output_core_dims` anf the `dask_gufunc_kwargs` arguments:

def xarray_cov(x, y, dim):
    return xr.apply_ufunc(
        gufunc_cov,
        x,
        y, 
        input_core_dims=[[dim], [dim]],
        output_core_dims=[['lags']],
        dask="parallelized",
        output_dtypes=[np.float32],
        dask_gufunc_kwargs = {'output_sizes' : {'lags': 1463}}
    )


# Now, we read our data based on a specific chunk layout. **Note that the `time` dimension must remain unchunked.

anom = anom.chunk({'y':50, 'x': 50})
anom

# %%time
with Profiler() as prof, ResourceProfiler(dt=0.25) as rprof, CacheProfiler() as cprof:
    calc = xarray_cov(anom, tmean, dim='time_counter').compute()

# We see that the calculation time is less than the original one. We can now visualize the resource usage:

visualize([prof, rprof, cprof])

# Finally, we can verify that both calculations (Numpy vs. Dask) returns the same results. First, `NaN` values are replaced by 0 in both results.

calc = calc.fillna(0)
covariance[np.isnan(covariance)] = 0

np.all(covariance == calc.values)
