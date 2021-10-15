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

# # Python libraries
#
# ## Install libraries
#
# To install libraries, you can either use [conda](https://docs.conda.io/en/latest/), [pip](https://pip.pypa.io/en/stable/) or install from source files.
#
# *Pip* only installs Python packages. The user needs to manually install the required external tools (compilers, C libraries, etc.).
#
# *Conda* installs everything that is needed (compiler, libraries) and has the ability to create isolated environments, which may contain different versions of the packages.
#
# <div class="alert alert-success">
#   <strong>Pip vs. Conda!</strong> For further details about the difference between Pip and Conda, visit    
#     <a href="https://www.anaconda.com/understanding-conda-and-pip/" target="_blank">anaconda.com</a>
# </div>
#
# ### Install from Pip
#
# All the packages available on Pip are listed on the [pip](https://pypi.org/) webpage. To install any of them, type on a terminal:
#
# ```
# pip install package_name
# ```
#
# For install, to manipulate NetCDF files, 
#
# ```
# pip install netCDF4 xarray
# ```
#
# ### Install from Conda
#
# All the packages available on the Conda default channel are listed on the [Conda repository](https://repo.anaconda.com/pkgs/). To install any of them, type on a terminal:
#
# ```
# conda install package_name
# ```
#
# For install, to manipulate NetCDF files, 
#
# ```
# conda install netCDF4 xarray
# ```
#
# #### Conda virtual environments
#
# To create virtual environments (for instance for spatial representation), type in a terminal:
#
# ```
# # PyNGL env. for Python 3
# conda create --name pyngl3 --channel conda-forge pynio pyngl
#
# # PyNGL env. for Python 2
# conda create --name pyngl2 --channel conda-forge pynio pyngl python=2.7
# ```
#
# In this case, the packages are downloaded from a community channel, the [conda-forge](https://conda-forge.org/).
#
# To change environment, type
#
# ```
# conda activate pyngl2  # switch env. to pygnl2
# conda activate pyngl3  # switch env. to pygnl3
# conda activate base    # go back to default env.
# ```
#
# To list all the environments, type: 
#
# ```
# conda env list
# ```
#
# <div class="alert alert-info">
#     <strong>Default environment!</strong> The default environment is named <i>base</i>
# </div>
#
# #### Export environment
#
# Conda allows to export an environment into a text file as follows:
#
# ```
# conda env export > env.yaml
# ```
#
# #### Import environment
#
# You can also import an environment as follows:
#
# ```
# conda env create -f env.yaml
# ```
#
# #### Connect environments to Jupyter
#
# You can also allow Jupyter to access your environments as follows:
#
# ```
# conda activate pyngl
# conda install ipython ipykernel
# ipython kernel install --name "pyngl" --user
# ```
#
# ### Install from source
#
# To install a package from sources, unzip the archive and type:
#     
# ```
# python setup.py install --home=/my/directory/
# ```
#
# <div class="alert alert-info">
#     <strong>Note. </strong>At the beginning, you are unlikely to do that.
# </div>
#
# ## Loading  libraries
#    
# Libraries are loaded by using the `import` statement (generally at the beginning of the scripts) as follows:

# +
# loading the numpy library
import numpy

# loading matplotlib with the shortname mp
import matplotlib as mp
# -

# In this case, the objects of the imported modules are stored into defined **namespaces**, which prevent conflicts among object names. 

# ### Calling functions
#
# Using namespaces, a module's function is called as follows:
#
# `module.function(arg1, arg2, arg3, ...)`
#
# For instance:

numpy.mean([0, 1, 2], keepdims=True)

mp.is_interactive()

# To get some help about a function, use the `help` function:

help(mp.is_interactive)

# ### Bad practice!
#
# Libraries can also be loaded as follows:

from pandas import DataFrame

# Here, we import the `DataFrame` from the `pandas` module.

from scipy.stats import *

# Here, we import all the content of the `scipy.stats` module into the current namespace.

# <div class="alert alert-danger">
#     <strong>Warning!</strong> I strongly recommend to <strong>never</strong> use this way of importing modules, since they may be in conflict with other objects.
# </div>

import numpy as np
x = np.array([1e4, 1e6])
x

from numpy import *
log10(x)

from math import *
# log10(x[0])) 

# Here, the `numpy.log10` method has been overwritten by the `math.log10` one, which works on `float` objects, not on `arrays`.
