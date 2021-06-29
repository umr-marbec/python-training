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

# ## Detrending the time-series
#
# Now that the anomalies have been computed, we need to remove the linear trend.

# +
import scipy.signal as sig
import time

anoms_data = anoms.data
anoms_data[np.isnan(anoms_data)] = 0
anoms_detrend = sig.detrend(anoms_data, axis=0)
# -

# ## Extracting the weights
#
# Now, the next step is to extract the weights for the EOFs, based on the cell surface and mask.

mask = xr.open_dataset('pacific_mask.nc')['pacific'].values
mesh = xr.open_dataset('data/mesh_mask_eORCA1_v2.2.nc')
surf = mesh['e1t'] * mesh['e2t']
surf = surf[0].values * mask
weights = surf / np.sum(surf)

plt.figure()
plt.plot(anoms_detrend[:, 160, 100])

# ## Computation of EOFS
#
# The EOFS can now be computed. First, an EOF solver must be initialized:

# +
import eofs
from eofs.standard import Eof

ilat, ilon = np.nonzero(mask == 1)
solver = Eof(anoms_detrend[:, ilat, ilon], weights=weights[ilat, ilon])
# -

# Now, EOF components can be extracted. First, we recover the covariance maps:

# +
neofs = 2
nlat, nlon = surf.shape
covmaps = np.zeros((neofs, nlat, nlon))
covmaps[:, ilat, ilon] = solver.eofsAsCovariance(neofs=neofs)
print(covmaps.min(), covmaps.max())

plt.figure()
cs = plt.imshow(covmaps[0], cmap=plt.cm.RdBu_r)
cs.set_clim(-1, 1)
plt.colorbar(cs)
# -

# Then, we can recover the explained variance:

eofvar = solver.varianceFraction(neigs=neofs)

# Finally, we can obtain the principal components

print(np.sum(weights[ilat, ilon]))

plt.show()
