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

# # Parallel programing with Dask
#
# [Dask](http://xarray.pydata.org/en/stable/user-guide/dask.html) is a library that allows to do parallel computing on multi-dimensional arrays. The advantage is that when working on a laptop, not all the object is loaded at once into the memory.
#
# If you want to compute the time-average of a data array using `xarray`, one can use:

import matplotlib.pyplot as plt
import xarray as xr

# %%time
import xarray as xr
data = xr.open_dataset('data/surface_thetao.nc')
data = data.isel(olevel=0)
data = data['thetao']
datamean = data.mean(dim='time_counter')
datamean.compute()  #  does the calculation
data

# However, this method does not take advantage of multiple cores which are available on most computers. Indeed, each core could manage one specific tile of the domain. 
#
# This can be achieved by using `xarray` in combination with the `dask` library through the `chunks` arguments, which provides the size of the `tile` objects

# %%time
data = xr.open_dataset('data/surface_thetao.nc', 
                       chunks={'time_counter': -1, 'x': 362 // 2, 'y' : 332 // 2})
data = data.isel(olevel=0)
data = data['thetao']
datamean = data.mean(dim='time_counter')
datamean.compute()  # does the calculation
data

# The computation time in this case is a bit small that in the previous one, and the walltime is much smaller than the total time. This likely indicates that the computation has been done in parallel.
#
# Note that most `numpy` functions are implemented. But you can also implement your own functions in a parallel way.

# ## Using user-defined functions in parallel.
#
# In order to use a function which is not implemented in the `xarray` list of functions, the `xarray.apply_ufunc` method should be used. 
#
# For instance, to implement the `scipy.signal.detrend` function in a parallel manner, this is done as follows.
#
# First, create a function that takes as arguments a `numpy.array`. Note that the dimension on which you will operate (for detrending, that would be `time`) will be the last one.

# +
import scipy.signal as sig
import numpy as np

def gufunc_detrend(x):
    print('x.shape', x.shape)
    x[np.isnan(x)] = 0
    return sig.detrend(x)


# -

# Now that it is done, create a new method returns a `xr.apply_ufunc` object. The first argument is the above function, the second argument is the `DataArray`. The `input_core_dims` provides the names of the core dimensions, the ones on which the operations will be performed. In this case, `time`. Since the `detrend` function returns an array of the same size as the input, the `output_core_dims` should be provided as well.

def xarray_detrend(x, dim):
    return xr.apply_ufunc(
        gufunc_detrend,
        x,
        input_core_dims=[[dim]],
        output_core_dims=[[dim]],
        dask="parallelized",
        output_dtypes=[np.float32],
    )


# Now, we read our data based on a specific chunk layout. **Note that the `time` dimension must remain unchanged, hence the `-1`**.

data = xr.open_dataset('data/surface_thetao.nc', 
                       chunks={'time_counter': -1, 'x': 100, 'y' : 100})
data = data['thetao']
data = data.isel(olevel=0)
data

# %time calc = xarray_detrend(data, dim='time_counter').compute()

# Note that you can call the `compute` method in association with a progress bar as follows:

from dask.diagnostics import ProgressBar
with ProgressBar():
    # %time calc = xarray_detrend(data, dim='time_counter').compute()
calc


