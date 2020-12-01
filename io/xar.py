# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # NetCDF
#
# A very efficient way to read and write NetCDF files is to use the [xarray](http://xarray.pydata.org/en/stable/) Python library, which can be viewed as a ND counterpart of the [pandas](http://pandas.pydata.org).
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
print(data)
# -

# ### Reading multiple files
#
# Often, a variable is stored in multiple NetCDF files (one file per year for instance). The `xarray.open_mfdataset` allows to open all the files in one row and to concatenate them along *record* dimension (`UNLIMITED` dimension, which is usually time) and the data coordinates.
#
# Below, the four `ISAS13` files are opened at once and are automatically concanated along the record dimension, hence leading to a dataset with 4 time steps.

data = xr.open_mfdataset("data/*ISAS*nc", combine='by_coords')
print(data)

# Furthermore, complex models are often paralellized using the [Message Passing Interface (MPI)](https://fr.wikipedia.org/wiki/Message_Passing_Interface), in which each processor manages a subdomain. If each processor saves output in its sub-region, there will be as many output files as there are processors.
# `xarray` allows to reconstruct the global file by concatenating the subregional files according to their coordinates.
#
# <div class="alert alert-danger">
#     <strong>Warning!</strong> This actually works only if the decomposition into subregions is regular, and if subfiles contain coordinates
# </div>

data = xr.open_mfdataset("data/GYRE_OOPE*", combine='by_coords')
print(data)

# ### Accessing dimensions, variables, attributes

data = xr.open_dataset("data/UV500storm.nc")
print(data)

# #### Dimensions
#
# Recovering dimensions is dony by accessing the `dims` attribute of the dataset, which returns a `dictionary`, the `keys` of which are the dataset dimension names.

# Recovering the number of values along a dimension
for k, v in data.dims.items():
    print('dim', k, 'n=', v)
print(data.dims['lat'])

# #### Variables
#
# Variables can be accessed by using the `data_vars` attribute, which returns a `dictionary`,  the `keys` of which are the dataset variable names.

# +
var = data.data_vars
for k, v in var.items():
    print('var', k, 'shape', v.shape)   

u = data.data_vars['u']
# -

# Note that data variables can also be accessed by using variable name as the key to the dataset object as follows:

v = data['v']

# In this case, the `data_vars` attribute is not used. 
#
# In the above, the variable is extracted into a 
# [xarray.DataArray](http://xarray.pydata.org/en/stable/data-structures.html#dataarray) object.

# To recover the variable as a `numpy` array, the `values` attribute can be used. In this case, missing values are set to `NaN`.

# +
v = data['v']
print(type(v))
v = v.values
print(type(v))

v.mean()
# -

# In order to obtain a masked array instead, use the `to_masked_array()` method:

# +
v = data['v']
print(type(v))
v = v.to_masked_array()
print(type(v))

v.mean()
# -

# #### Time management
#
# By default, the time variable is detected by `xarray` by using the NetCDF attributes, and is converted into a human time. This is done by xarray by using the [cftime](https://pypi.org/project/cftime/) module

data = xr.open_mfdataset("data/*ISAS*", combine='by_coords')
print(data['time'].values)

# Then, the user can access the `year`, `month`, `day`, `hour`, `minute`, `second`, `microsecond`, `nanosecond`, `date`, `time`, `dayofyear`, `weekofyear`, `dayofweek`, `quarter` as follows:

print(data['time.year'].values)
print(data['time.month'].values)
print(data['time.day'].values)
print(data['time.dayofyear'].values)

# <div class="alert alert-info">
#     <strong>Warning</strong> Replace <i>time</i> by the name of your time variable (<i>time_counter</i> in NEMO for instance)
# </div>
#
# If the user does not want `xarray` to convert time into a human date, set the `decode_times` argument to False.

data = xr.open_mfdataset("data/*ISAS*", combine='by_coords', decode_times=False)
print(data['time'].values)
# print(data['time.year'].values)  #  crashes because time is a float, not a date

# #### Attributes
#
# To get variable attributes, use the `attrs` attribute, which exists for DataSet and DataArray objects. It returns a `dictionaray` containing the attribute names and values.

# Recovering global (file) attributes
for k, v in data.attrs.items():
    print('attr', k, 'val', v)
print(data.attrs['history'])

time = data['time']
# Recovering variable attributes
for k, v in time.attrs.items():
    print('attr', k, 'val', v)
print(time.attrs['units'])

# ## Indexing
#
# As in `pandas`, there is 2 ways to extract part of a dataset. Let's consider the ISAS dataset, which contains 152 vertical levels unevenly from 0 to 2000m. 

data = xr.open_mfdataset('data/*ISAS*', combine='by_coords')
print(data['depth'])

# ### Extracting using indexes
#
# To extract the ten first level and the first to time steps, the `isel` method should be used, which can be applied on either `DataSet` or `DataArray`.
#
# <div class='alert alert-info'>
#     <strong>Note</strong> It is the xarray counterpart of the Pandas iloc method
# </div>        

# +
data_s = data.isel(time=slice(0, 2), depth=range(0, 10))
print(data_s)

temp = data['TEMP'].isel(time=slice(0, 2), depth=range(0, 10))
print(temp)
# -

# ### Extracting using values
#
# To extract the data between 100m and 500m and for a given period, the `sel` method should be used, which can be applied on either `DataSet` or `DataArray`. It allows use values rather than indexes.
#
# <div class='alert alert-info'>
#     <strong>Note</strong> It is the xarray counterpart of the Pandas loc method
# </div>     

data_s = data.sel(time=slice('2012-01-15', '2012-02-15'), depth=slice(100, 500))
print(data_s)

# ### Plotting
#
# As for `pandas`, `xarray` comes with plotting functions.

# +
import matplotlib.pyplot as plt

data = xr.open_dataset('data/UV500storm.nc')
data = data.isel(timestep=0)  # extract first time step

plt.figure()
data['u'].plot()  # draws map
plt.show()

data = data.sel(lon=-100)  # extracts lon=-100
plt.figure()
data['u'].plot()  # draw curves
plt.show()
# -

# ## Mathematical operations
#
# As for `pandas`, `xarray` comes with mathematical operations.

# +
data = xr.open_mfdataset('data/*ISAS*', combine='by_coords')

print('------------- full mean')
print(data.mean())
print(data.mean(dim=('time', 'depth')))
print('------------- time mean')
print(data.mean(dim='time'))
print('------------- depth mean')
print(data.mean(dim='depth'))
# -

# ## Group-by operations
#
# The [groupby](http://xarray.pydata.org/en/stable/groupby.html) methods allows to easily perform operations on indepedent groups. For instance, to compute temporal (yearly, monthly, seasonal) means:

monthlymean = data.groupby('time.month').mean(dim='time')
print(monthlymean)

yearlymean = data.groupby('time.year').mean(dim='time')
print(yearlymean)

seasonmean = data.groupby('time.season').mean(dim='time')
print(seasonmean)

# Defining discrete binning (for depth intervals for instance) is done by using the 
# [groupby_bins](http://xarray.pydata.org/en/stable/generated/xarray.Dataset.groupby_bins.html#xarray.Dataset.groupby_bins) method.

# +
depth_bins = np.arange(0, 1000 + 250, 250)
zmean = data.groupby_bins('depth', depth_bins).mean(dim='depth')
print(zmean)
bins = zmean['depth_bins'].values

plt.figure()
zmean['TEMP'].plot()
plt.show()
# -

# ## Creating NetCDF
#
# An easy way to write a NetCDF is to create a `DataSet` object.

# +
import numpy as np
from cftime import utime

nx = 10
ny = 20
ntime = 5
x = np.arange(nx)
y = np.arange(ny)

data = np.random.rand(ntime, ny, nx) - 0.5
data = np.ma.masked_where(data < 0, data)

# converts time into date
time = np.arange(ntime)
date = utime('days since 1900-01-01 00:00:00').num2date(time)
# -

# First, init an empty `Dataset` object by calling the [xarray.Dataset](http://xarray.pydata.org/en/stable/generated/xarray.Dataset.html)method.

ds = xr.Dataset()

# Then, add to the dataset the variables and coordinates. Note that they should be provided as a tuple that contains two elements:
# - A list of dimension names
# - The numpy array

# +
print(time.shape)
print(data.shape)

ds['data'] = (['time', 'y', 'x'], data)
ds['x'] = (['x'], x)
ds['y'] = (['y'], y)
ds['time'] = (['time'], date)
# -

# Then, add the dataset and variable attributes as follows:

# +
import os
from datetime import datetime

# Set file global attributes (file directory name + date)
ds.attrs['script'] = os.getcwd()
ds.attrs['date'] = str(datetime.today())

ds['data'].attrs['description'] = 'Random draft'
# -

# Finally, create the NetCDF file by using the [to_netcdf](http://xarray.pydata.org/en/stable/generated/xarray.Dataset.to_netcdf.html) method.

ds.to_netcdf('data/example.nc', unlimited_dims='time', format='NETCDF4')

# Note that xarray automatically writes the `_FillValue` attribute and the `time:units` attributes.
