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

# # EOF analysis
#
# EOF analysis is performed using the [Eofs](https://ajdawson.github.io/eofs/latest/index.html) package.
#
# ## Extraction of Pacific mask
#
# The Pacific mask can first be extracted based on coordinates (longitudes and latitudes) as follows:

# +
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

data = xr.open_dataset('data/mesh_mask_eORCA1_v2.2.nc')
data = data.isel(z=0, t=0)
lon = data['glamt'].values
lat = data['gphit'].values
mask = data['tmask'].values

# mask latitudes greater than 30
ilat = np.abs(lat) > 30
mask[ilat] = 0

# mask domain outside of Pacific (120E/80W)
# done in two ways because of dateline
ilon = (lon >= 120 )| (lon <= -80)
mask[~ilon] = 0

plt.figure()
cs = plt.imshow(mask, interpolation='none')
cb = plt.colorbar(cs)
plt.show()
# -

# We see that the mask contains some points in the Atlantic. One way to remove them is to save the mask in a `.png` file. 

plt.imsave('temp_mask.png', mask)

# When done, edit the mask and rename it, for instance in `corrected-temp_mask.png`. Now, read the corrected image and store the output in a `NetCDF`.

# +
mask = plt.imread('corrected-temp_mask.png')

# Since mask is a 4D array (R, G, B, Alpha)
# we convert it into 2D
mask = np.sum(mask[..., :3], axis=-1)
mask[mask < 1] = 0
mask[mask > 1] = 1

plt.figure()
cs = plt.imshow(mask)
plt.show

dsout = xr.Dataset()
dsout['pacific'] = (['y', 'x'], mask)
dsout.to_netcdf('pacific_mask.nc')
# -

# ## Computation of seasonal anomalies
#
# Now, we need to compute the seasonal anomalies of SST fields. First, we read the SST values.

data = xr.open_dataset("data/surface_thetao.nc")
data = data.isel(olevel=0)
ntime = data.dims['time_counter']
data = data['thetao']

# Now, we compute the anomalies using the `groupy` methods:

clim = data.groupby('time_counter.month').mean()
anoms = data.groupby('time_counter.month') - clim

# ## Using loops
#
# Another method consists of doing it manually using two loops: one for the computation of climatology, one for the computation of the anomalies.

# +
start_time = time.time()
nyears = ntime // 12

index = np.arange(12)
for i in range(nyears):
    if(i == 0):
        clim = data.isel(time_counter=index).data
    else:
        clim += data.isel(time_counter=index).data
    index += 12
clim /= nyears

anoms_2 = np.zeros(data.shape)
index = np.arange(12)
for i in range(nyears):
    anoms_2[index, ...] = data.isel(time_counter=index).values - clim
    index += 12

# replace NaNs by 0
anoms_2[np.isnan(anoms_2)] = 0

end_time = time.time()
dt = (end_time - start_time)
print('Execution time method 2: %f seconds' %dt)
# -

# We see that the latter method is a bit faster than the first one. This is because 

print(np.all(anoms_2 == anoms_1))





