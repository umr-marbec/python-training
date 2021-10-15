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

# +
ax = plt.axes(projection=ccrs.PlateCarree())
cmap = plt.cm.jet

nshapes = len(shapes)
nshapes / (nshapes - 1)

for i in range(4, 5):
    
    print('@@@@@@@@@@@@@ shape ', i, '/', nshapes)
    
    # get the shapes and extract the points
    single = shapes[i]
    points = np.array(single.points)
    npoints = len(points)
    
    # get the number of parts
    parts = list(single.parts)
    nparts = len(parts)
    
    #print(parts)
    
    # get the colour
    color = cmap(i / (nshapes - 1))
    
    #plt.plot(points[:, 0], points[:, 1], marker='.', linestyle='none', color=color, markersize=0.1, transform=ccrs.PlateCarree())
    
    # get the record
    singlerec = records[i]
    xmin, xmax = points[:, 0].min(), points[:, 0].max()
    ymin, ymax = points[:, 1].min(), points[:, 1].max()
    
    if nparts == 1:
        plt.plot(points[:, 0], points[:, 1])
    else:
        #if(nparts > 10):
        #    continue
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
            start = parts[p]
            end = parts[p + 1]
            iii = range(start, end)
            #test = list(iii)
            #print(test[0], test[-1])
            plt.plot(points[iii, 0], points[iii, 1], color=color, transform=ccrs.PlateCarree(), linewidth=0.5)
l = ax.add_feature(cfeature.LAND)
l = ax.add_feature(cfeature.COASTLINE)
ax.set_global()
plt.show()
# -


