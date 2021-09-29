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

# # Parallel programing with Dask
#
# [Dask](http://xarray.pydata.org/en/stable/user-guide/dask.html) is a library that allows to decompose an array into objects of small sizes (`chunks`). Therefore, big datasets are not loaded into memory at once. Additionnally, parallel computing is possible on these `chunks` objects. Let's see an example.
#
# First, the SST field is loaded using `xarray`

# +
import matplotlib.pyplot as plt
import xarray as xr

data = xr.open_dataset('data/surface_thetao.nc')
data = data.isel(olevel=0)
data = data['thetao']
data
# -

# Let's compute the time-mean of the given dataset, and load in memory the output.

# %%time
datamean = data.mean(dim='time_counter')
datamean = datamean.compute()  #  does the calculation and store in memory
datamean.min()

# Now, let's spatially divide our dataset into squares of 150x150 pixels. This is done using the `chunk` method (you can also provide a `chunks` argument in the `open_dataset` method).

data = xr.open_dataset('data/surface_thetao.nc')
data = data.isel(olevel=0)
data = data['thetao']
data = data.chunk({'x': 150, 'y': 150})
data

# %%time
datamean2 = data.mean(dim='time_counter')
datamean2 = datamean2.compute()
datamean2.min()

# The computation time is much better using the chunked data array. And the use of memory is reduced. To see how dask manages the computation, you can use the `dask.visualize` method. It first requires that the `dask` object is extracted from the `xarray` object.

datamean2 = data.mean(dim='time_counter')
dask_obj = datamean2.data
dask_obj.visualize()

# In the above graph, it can be seen that each chunk has it's own `(y, x)` map. 
#
# If now the mean over all dimensions is computed: 

datamean3 = data.mean()
dask_obj = datamean3.data
dask_obj.visualize()

# In this case, the mean maps are first computed for each chunk. Then the mean maps for some chunks are recombined together. The last 4 objects are finally aggregated together to give the final output.
#
# Many functions are implemented in `xarray` and which will work with `dask` (cf [the list of available functions](https://numpy.org/doc/stable/reference/ufuncs.html#available-ufuncs)). 
#
# However, if the function that you want to use is missing, user-defined `ufunc` can be created.

# ## Using user-defined functions in parallel.
#
# In order to use a function which is not implemented in the `xarray` list of universal functions, the `xarray.apply_ufunc` method should be used. 
#
# For instance, in order to to implement the `scipy.signal.detrend` function in a parallel manner, 
# First, create a function that takes as arguments **a `numpy.array`**. Note that the dimension on which you will operate (for detrending, that would be `time`) will be the last one.

# +
import scipy.signal as sig
import numpy as np

def gufunc_detrend(x):
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


# Now, we read our data based on a specific chunk layout. **Note that the `time` dimension must remain unchunked, hence the `-1`**.

data = xr.open_dataset('data/surface_thetao.nc', 
                       chunks={'time_counter': -1, 'x': 150, 'y' : 150})
data = data['thetao']
data = data.isel(olevel=0)
data

# Now we compute the monthly anomalies:

dataclim = data.groupby('time_counter.month').mean(dim='time_counter')
dataclim

data = data.groupby('time_counter.month') - dataclim
data = data.chunk({'time_counter': -1, 'y': 150, 'y': 150})
data

# %%time 
calc = xarray_detrend(data, dim='time_counter').compute()

# Note that you can call the `compute` method in association with a progress bar as follows:

from dask.diagnostics import ProgressBar
with ProgressBar():
    calc = xarray_detrend(data, dim='time_counter').compute()
calc

# Now let's check if trend seems ok. First, we extract the detrended time-series on a specific location

coords = dict(x=90, y=165)
calcts = calc.isel(**coords)  # detrendet time series
calcts

# Then, we extract the raw anomalies on the same location

datats = data.isel(**coords)

Now, we can plot the raw anomalies and the associated trend:

plt.plot(datats, label='anomalies')
plt.plot(datats - calcts, label='trend')
plt.legend()

# ## Use on HPCs
#
# It is theoretically possible to parallel Dask operations on HPCs, such as Datarmor. This is achieved by using the [dask-jobqueue](https://jobqueue.dask.org) in association with the `dask.distributed` module. For instance, to run a computation on a `PBS` cluster such as Datarmor, the `PBSCluster` method should be used.
#
# The first step is to create a `jobqueue.yaml` file in the `~/.config/dask` directory. This file contains all the PBS settings for the cluster you are working on (cf. [here](https://jobqueue.dask.org/en/latest/configurations.html#ifremer-datarmor) for the Datarmor configuration). **These are the settings for a single job.**. 
#
# There must be also a `distributed.yaml` configuration file, which contains the settings for the HPC server. An example is available [here](https://github.com/apatlpo/lops-array/blob/master/datarmor/distributed.yaml).
#
# When done, create your Python script as shown below (taken from [dask example page](https://jobqueue.dask.org/en/latest/index.html?highlight=client#example)).
#
# ```
# from dask_jobqueue import PBSCluster
# cluster = PBSCluster()
# cluster.scale(jobs=10)  # launch 10 jobs
# ```
#
# To see the job script: 
#
# ```
# print(cluster.job_script())
# ```
#
# Now init the `Client` object using the cluster defined in the above:
#
# ```
# from dask.distributed import Client
# client = Client(cluster)  # Connect this local process to remote workers
# ```
#
# When done, run your Dask operations
#
# ```
# # wait for jobs to arrive, depending on the queue, this may take some time
# import dask.array as da
# ```
#
# **This is not even clear for me, so use with caution!!!**
#
# For more informations:
# - https://docs.dask.org/en/latest/
# - [presentation-dask.pdf](http://osr-cesbio.ups-tlse.fr/gitlab_cesbio/activites-ia/ds-cb/raw/22e64eeed3cd6fa5643381b3ae928e7d73b3d15e/Julien_Dask/presentation-dask.pdf)
# - [lops-array](https://github.com/apatlpo/lops-array/) for some examples.
