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
# EOF analysis is performed using the [Eofs](https://ajdawson.github.io/eofs/latest/index.html) package. In the following, the steps for the computation of an EOF decomposition is provided. The objective would be to compute the El Nino index based on the SST of the Northern Pacific.
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

# converts lon from Atl to Pac.
lon[lon < 0] += 360

# mask based on latitudes
ilat = (lat <= 60) & (lat >= -20)
mask[~ilat] = 0

# mask based on longitudes
ilon = (lon >= 117 ) & (lon <= 260)
mask[~ilon] = 0

# extracting the domain using the slices
ilat, ilon = np.nonzero(mask == 1)
ilat = slice(ilat.min(), ilat.max() + 1)
ilon = slice(ilon.min(), ilon.max() + 1)
mask = mask[ilat, ilon]

plt.figure()
cs = plt.imshow(mask, interpolation='none')
cb = plt.colorbar(cs)
# -

# ## Computation of seasonal anomalies
#
# Now, we need to compute the seasonal anomalies of SST fields. First, we read the SST values and extract the spurious `olevel` dimension.

data = xr.open_dataset("data/surface_thetao.nc")
data = data.isel(olevel=0, x=ilon, y=ilat)
ntime = data.dims['time_counter']
data = data['thetao']

# Now, we compute the anomalies using the `groupy` methods:

clim = data.groupby('time_counter.month').mean()
anoms = data.groupby('time_counter.month') - clim

# ## Detrending the time-series
#
# Now that the anomalies have been computed, the linear trend is removed using the `detrend` function. Since the detrend function does not manage NaNs, the filled values are first replaced by 0s 

# +
import scipy.signal as sig
import time

anoms = anoms.fillna(0)
anoms_detrend = sig.detrend(anoms, axis=0)
print(type(anoms_detrend))
# -

# Note that in the `detrend` function returns a `numpy.array` object. Hence, no benefit will be taken from the `xarray` structure in the EOF calculation.

# ## Extracting the weights
#
# Now, the next step is to extract the weights for the EOFs, based on the cell surface and mask.

mesh = xr.open_dataset('data/mesh_mask_eORCA1_v2.2.nc')
mesh = mesh.isel(t=0, x=ilon, y=ilat)
surf = mesh['e1t'] * mesh['e2t']
surf = surf.data * mask  # surf in Pacific, 0 elsewhere
weights = surf / np.sum(surf)  # normalization of weights

# **Since EOF are based on covariance, the root-square of the weights must be used.**

weights = np.sqrt(weights)

# ## Computation of EOFS (standard mode)
#
# The EOFS can now be computed. First, an EOF solver must be initialized. **The `time` dimension must always be the first one when using numpy.array as inputs.**

# +
import eofs
from eofs.standard import Eof

solver = Eof(anoms_detrend, weights=weights)
# -

# Now, EOF components can be extracted. First, the covariance maps are extracted.

# +
neofs = 2
nlat, nlon = surf.shape
covmaps = solver.eofsAsCovariance(neofs=neofs)
print(type(covmaps))

plt.figure()
plt.subplot(211)
cs = plt.imshow(covmaps[0], cmap=plt.cm.RdBu_r)
cs.set_clim(-1, 1)
cb = plt.colorbar(cs)
plt.subplot(212)
cs = plt.imshow(covmaps[1], cmap=plt.cm.RdBu_r)
cs.set_clim(-1, 1)
cb = plt.colorbar(cs)
# -

# Then, we can recover the explained variance:

eofvar = solver.varianceFraction(neigs=neofs) * 100
eofvar

# Finally, we can obtain the principal components. To obtain normalized time-series, the `pscaling` argument must be equal to 1.

pcs = solver.pcs(pcscaling=1, npcs=neofs).T
plt.figure()
plt.plot(pcs[0], label='pc1')
plt.plot(pcs[1], label='pc2')
leg = plt.legend()

# ## EOF computation (xarray mode)
#
# In order to have EOF as an `xarray` with all its features, the Eof method of the `eofs.xarray` submodule must be used.

from eofs.xarray import Eof

# Since it uses named labels, the `time_counter` dimension must first be renamed in `time`:

anoms = anoms.rename({'time_counter': 'time'})
solver = Eof(anoms, weights=weights)

# +
neofs = 2
covmaps = solver.eofsAsCovariance(neofs=neofs)

plt.figure()
cs = covmaps.isel(mode=0).plot()
cs.set_clim(-1, 1)
# -

pcs = solver.pcs(pcscaling=1, npcs=neofs)
plt.figure()
l = pcs.plot.line(x='time')
