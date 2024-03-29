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

# # Reading shapefiles
#
# ## Downloading the file
#
# First, we will download a sample shape file:

# +
import wget
import zipfile
import os.path

if  not os.path.isfile('data/IPBES_Regions_Subregions2.shp'):
    url = 'https://zenodo.org/record/3928281/files/ipbes_regions_subregions_shape_1.1.zip'
    wget.download(url, 'data/ipbes_regions_subregions_shape_1.1.zip')
    with zipfile.ZipFile("data/ipbes_regions_subregions_shape_1.1.zip","r") as zip_ref:
        zip_ref.extractall("data")
# -

# ## Reading the shapefile

import shapefile as pyshp
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

data = pyshp.Reader('data/IPBES_Regions_Subregions2.shp', encoding='ISO8859-1')
data

shapes = data.shapes()

nshapes = len(shapes)

single = shapes[0]

single.shapeType

single.shapeTypeName

parts = single.parts
parts

points = np.array(single.points)  # npoints, nx, ny
points.shape 

fields = data.fields
fields

records = data.records()
singlerec = records[4]
singlerec
i = 0
for a in records:
    count = a[2]
    if(count == 'France'):
        break
    i += 1

# +
ax = plt.axes(projection=ccrs.PlateCarree())

cmap = plt.cm.jet

# get the shapes and extract the points
single = shapes[i]
points = np.array(single.points)
npoints = len(points)

# get the number of parts
parts = list(single.parts)
nparts = len(parts)

# get the record
singlerec = records[i]
xmin, xmax = points[:, 0].min(), points[:, 0].max()
ymin, ymax = points[:, 1].min(), points[:, 1].max()

if nparts == 1:
    plt.plot(points[:, 0], points[:, 1])
else:
    # if parts does not start with 0:
    # we add 0 at the beginning of the list
    if parts[0] != 0:
        parts = [0] + parts
    # if parts does not end with npoints 
    # it is added at the end.
    if parts[-1] != npoints:
        parts = parts + [npoints]
    nparts = len(parts) - 1
    for p in range(nparts):
        # get the colour
        color = cmap(p / (nparts - 1))
        start = parts[p]
        end = parts[p + 1]
        iii = range(start, end)
        plt.plot(points[iii, 0], points[iii, 1], color=color, transform=ccrs.PlateCarree(), linewidth=2)
#l = ax.add_feature(cfeature.LAND)
#l = ax.add_feature(cfeature.COASTLINE)
ax.set_extent([xmin, xmax, ymin, ymax])
plt.show()
# -

