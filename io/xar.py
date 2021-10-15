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

# # NetCDF
#
# A very efficient way to read, analyze and write NetCDF files is to use the [xarray](http://xarray.pydata.org/en/stable/) Python library, which can be viewed as a ND counterpart of the [pandas](http://pandas.pydata.org). 
#
# ## Reading NetCDF
#
# ### Reading single file
#
# Reading NetCDF files is dones by using the `xarray.open_dataset` method, which returns a [xarray.Dataset](http://xarray.pydata.org/en/stable/data-structures.html#dataset) object.

# +
import xarray as xr
import numpy as np

data = xr.open_dataset('data/UV500storm.nc')
data
# -

# ### Reading multiple files
#
# Often, a variable is stored in multiple NetCDF files (one file per year for instance). The `xarray.open_mfdataset` allows to open all the files at one and to concatenate them along *record* dimension (`UNLIMITED` dimension, which is usually time) and spatial dimensions.
#
# Below, the four `ISAS13` files are opened at once and are automatically concanated along the record dimension, hence leading to a dataset with 4 time steps.

data = xr.open_mfdataset("data/*ISAS*nc", combine='by_coords')
data

# Furthermore, complex models are often paralellized using the [Message Passing Interface (MPI)](https://fr.wikipedia.org/wiki/Message_Passing_Interface), in which each processor manages a subdomain. If each processor saves output in its sub-region, there will be as many output files as there are processors.
# `xarray` allows to reconstruct the global file by concatenating the subregional files according to their coordinates.
#
# <div class="alert alert-danger">
#     <strong>Warning!</strong> This actually works only if the decomposition into subregions is regular, and if subfiles contain coordinates
# </div>

data = xr.open_mfdataset("data/GYRE_OOPE*", combine='by_coords', engine='netcdf4')
data['OOPE']

# In the 2 previous examples, `chunksize` variable attribute appeared. This is due to the fact that opening multiple datasets automatically generates `dask` arrays, which are ready for parallel computing. These are discussed in a specific section

# ### Accessing dimensions, variables, attributes

data = xr.open_dataset("data/UV500storm.nc")
data

# #### Dimensions
#
# Recovering dimensions is dony by accessing the `dims` attribute of the dataset, which returns a `dictionary`, the `keys` of which are the dataset dimension names and the values are the number of elements along the dimension.

data.dims

data.dims['lat']

# #### Variables
#
# Variables can be accessed by using the `data_vars` attribute, which returns a `dictionary`,  the `keys` of which are the dataset variable names.

data.data_vars

data.data_vars['u']

# Note that data variables can also be accessed by using variable name as the key to the dataset object, as follows:

data['v']

# Note that variables are returned as `xarray.DataArray`.

# To recover the variable as a `numpy` array, the `values` attribute can be used. In this case, missing values are set to `NaN`.

v = data['v']
v = v.values
v

# In order to obtain a masked array instead, use the `to_masked_array()` method:

v = data['v']
v = v.to_masked_array()
v

# #### Time management
#
# By default, the time variable is detected by `xarray` by using the NetCDF attributes, and is converted into a human time. This is done by xarray by using the [cftime](https://pypi.org/project/cftime/) module

data = xr.open_mfdataset("data/*ISAS*", combine='by_coords')
data['time']

# Then, the user can access the `year`, `month`, `day`, `hour`, `minute`, `second`, `microsecond`, `nanosecond`, `date`, `time`, `dayofyear`, `weekofyear`, `dayofweek`, `quarter` as follows:

data['time.year']

data['time.month']

data['time.day']

data['time.dayofyear']

# <div class="alert alert-info">
#     <strong>Warning</strong> Replace <i>time</i> by the name of your time variable (<i>time_counter</i> in NEMO for instance)
# </div>
#
# If the user does not want `xarray` to convert time into a human date, set the `decode_times` argument to False.

data = xr.open_mfdataset("data/*ISAS*", combine='by_coords', decode_times=False)
data['time']

# **In this case, years, months, etc. cannot be extracted**

# #### Attributes
#
# To get variable attributes, use the `attrs` attribute, which exists for `xarray.Dataset` (global attributes) and `xarray.DataArray` objects (variable's attributes). It returns a `dictionary` containing the attribute names and values.

data.attrs

data.attrs['NCO']

time = data['time']
time.attrs

time.attrs['units']

# ## Indexing
#
# As in `pandas`, there is 2 ways to extract part of a dataset. Let's consider the ISAS dataset, which contains 152 vertical levels unevenly from 0 to 2000m. 

data = xr.open_mfdataset('data/*ISAS*', combine='by_coords')
data

# ### Extracting using indexes
#
# To extract the ten first level and the first to time steps, the `isel` method should be used, which can be applied on either `DataSet` or `DataArray`.
#
# <div class='alert alert-info'>
#     <strong>Note</strong> It is the xarray counterpart of the Pandas iloc method
# </div>        

data.isel(depth=range(10), time=0)

data.isel(time=slice(0, 2), depth=slice(0, 10))

data['TEMP'].isel(time=slice(0, 2), depth=range(0, 10))

# ### Extracting using values
#
# To extract the data between 100m and 500m and for a given period, the `sel` method should be used, which can be applied on either `DataSet` or `DataArray`. It allows use values rather than indexes.
#
# <div class='alert alert-info'>
#     <strong>Note</strong> It is the xarray counterpart of the Pandas loc method
# </div>     

data.sel(time=slice('2012-01-15', '2012-02-15'))

zmin = 100
zmax = 1000
data.sel(time=slice('2012-01-15', '2012-02-15'), depth=slice(zmin, zmax))

# ### Plotting
#
# As for `pandas`, `xarray` comes with plotting functions. The plot depends on the dimension of the fields:
#
# - 1D: curve
# - 2D: pcolormesh
# - 3D, 4D, ... : histogram

data = xr.open_dataset('data/UV500storm.nc')
data

l = data['u'].isel(timestep=0).plot()

l = data['u'].isel(timestep=0, lat=15).plot()

# ## Mathematical operations
#
# As for `pandas`, `xarray` comes with mathematical operations.

data = xr.open_mfdataset('data/*ISAS*', combine='by_coords')

# To compute the mean over the entire dataset:

data.mean()

# To compute the mean along time dimension:

data.mean(dim='time')

# Mean over the depth dimension:

data.mean(dim='depth')

# **Contrary to `numpy` eager evaluations, `xarray` performs lazy operations.** As indicated on the `xarray` website:
#
# ```
# Operations queue up a series of tasks mapped over blocks, and no computation is performed until you actually ask values to be computed (e.g., to print results to your screen or write to disk)
# ```
#
# To force the computation, the `compute` and/or `load` methods must be used. Let's compare the outputs below:

data['TEMP'].mean(dim='time')

data['TEMP'].mean(dim='time').compute()

# In the first output, no values are displayed. The `mean` has not been computed yet. In the second output, the effective mean values are shown because computation has been forced using `compute`.

# ## Group-by operations
#
# The [groupby](http://xarray.pydata.org/en/stable/groupby.html) methods allows to easily perform operations on indepedent groups. For instance, to compute temporal (yearly, monthly, seasonal) means:

data.groupby('time.month').mean(dim='time')

data.groupby('time.year').mean(dim='time')

data.groupby('time.season').mean(dim='time')

# Defining discrete binning (for depth intervals for instance) is done by using the 
# [groupby_bins](http://xarray.pydata.org/en/stable/generated/xarray.Dataset.groupby_bins.html#xarray.Dataset.groupby_bins) method.

depth_bins = np.arange(0, 1000 + 250, 250)
depth_bins

zmean = data.groupby_bins('depth', depth_bins).mean(dim='depth')
zmean

import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = False
cs = zmean['TEMP'].plot()

# Let's reload the ISAS dataset

data = xr.open_mfdataset('data/*ISAS*', combine='by_coords').isel(time=0)
data

# There is the possibility to compute rolling means along the depth dimensions as follows:

datar = data.rolling({'depth': 31}, center=True).mean(dim='depth')
datar

data['TEMP'].plot(label='original')
datar['TEMP'].plot(label='rolling', marker='o', linestyle='none')
plt.legend()

# ## Creating NetCDF
#
# An easy way to write a NetCDF is to create a `DataSet` object. First, let'sdefine some dummy variables:

# +
import numpy as np
import cftime

nx = 10
ny = 20
ntime = 5
x = np.arange(nx)
y = np.arange(ny)

data = np.random.rand(ntime, ny, nx) - 0.5
data = np.ma.masked_where(data < 0, data)

# converts time into date
time = np.arange(ntime)
date = cftime.num2date(time, 'days since 1900-01-01 00:00:00')
# -

date

data.shape

# First, init an empty `Dataset` object by calling the [xarray.Dataset](http://xarray.pydata.org/en/stable/generated/xarray.Dataset.html) method.

ds = xr.Dataset()

# Then, add to the dataset the variables and coordinates. Note that they should be provided as a tuple that contains two elements:
# - A list of dimension names
# - The numpy array

ds['data'] = (['time', 'y', 'x'], data)
ds['x'] = (['x'], x)
ds['y'] = (['y'], y)
ds['time'] = (['time'], date)
ds

# Then, add global and variable attributes to the dataset as follows:

# +
import os
from datetime import datetime

# Set file global attributes (file directory name + date)
ds.attrs['script'] = os.getcwd()
ds.attrs['date'] = str(datetime.today())

ds['data'].attrs['description'] = 'Random draft'
ds
# -

# Finally, create the NetCDF file by using the [to_netcdf](http://xarray.pydata.org/en/stable/generated/xarray.Dataset.to_netcdf.html) method.

ds.to_netcdf('data/example.nc', unlimited_dims='time', format='NETCDF4')

# Note that xarray automatically writes the `_FillValue` attribute and the `time:units` attributes.
